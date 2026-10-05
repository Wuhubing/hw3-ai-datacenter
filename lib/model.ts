export type Inputs = {itMW:number;pue:number;utilization:number;availability:number;efficiency:number;gpuKW:number;gpuShare:number;gpuPrice:number;facilityPerMW:number;gridCost:number;powerPrice:number;leasePrice:number;discount:number;debtShare:number;interest:number;idleFraction:number;fixedOpex:number;maintenance:number};
export const defaults:Inputs={itMW:20,pue:1.25,utilization:.65,availability:.99,efficiency:.9,gpuKW:1,gpuShare:.7,gpuPrice:40000,facilityPerMW:10000000,gridCost:20000000,powerPrice:.09,leasePrice:3,discount:.08,debtShare:.5,interest:.07,idleFraction:.4,fixedOpex:4000000,maintenance:.025};
export const scenarioNames={base:'Base case',delay:'Power delayed 1 year',half:'Half GPU utilization'};
export type Scenario=keyof typeof scenarioNames;
export type Strategy='Build & own'|'Lease capacity'|'Phased hybrid';
export function validateInputs(i:Inputs){for(const [k,v] of Object.entries(i)){if(!Number.isFinite(v)||v<0)throw Error(`Invalid ${k}`);}if(i.pue<1||i.pue>2||i.itMW<1||i.itMW>100||i.gpuKW<=0||i.availability>1||i.efficiency>1||i.utilization>1||i.gpuShare>1||i.debtShare>.9||i.idleFraction>1||i.discount>.3||i.interest>.3)throw Error('Inputs outside model limits');return i;}
export function energy(i:Inputs){return {facilityMW:i.itMW*i.pue,annualGWh:i.itMW*i.pue*8.76};}
export function calculate(i:Inputs=defaults,scenario:Scenario='base',strategy:Strategy='Build & own'){
validateInputs(i);const isLease=strategy==='Lease capacity',hybrid=strategy==='Phased hybrid';
const share=isLease?0:hybrid?.25:1;const util=i.utilization*(scenario==='half'?.5:1);
const gpuCount=Math.floor(i.itMW*1000*i.gpuShare/i.gpuKW);const demand=gpuCount*8760*util*i.availability*i.efficiency;
const facility=i.itMW*i.pue*i.facilityPerMW*share;const grid=i.gridCost*share;const fleet=gpuCount*i.gpuPrice*share;const upfront=facility+grid+fleet;
const debt=(facility+grid)*i.debtShare;const annualPrincipal=debt/10;
const openYear=isLease?1:scenario==='delay'?2:1;
let cumulative=upfront,npv=upfront,pvHours=0,totalHours=0,totalCost=upfront;
const rows=[];
for(let year=1;year<=10;year++){
 const operating=year>=openYear;const replacement=operating&&(year-openYear===4||year-openYear===8)?fleet:0;
 const onsiteHours=operating?demand*share:0;const leasedHours=demand-onsiteHours;
 const electricity=operating?i.itMW*share*i.pue*(i.idleFraction+(1-i.idleFraction)*util)*8760*1000*i.powerPrice:0;
 const staffing=share?(operating?i.fixedOpex*Math.max(share,.4):i.fixedOpex*.2*share):0;
 const maintenance=(facility+fleet)*i.maintenance*(operating?1:.2);
 const lease=leasedHours/(i.availability*i.efficiency)*i.leasePrice;
 const delayCost=!operating&&!isLease?(facility+grid)*.03:0;
 const opex=electricity+staffing+maintenance+lease;
 const idleBurden=operating?((staffing+maintenance)*(1-util)+i.itMW*share*i.pue*i.idleFraction*(1-util)*8760*1000*i.powerPrice):0;
 const interest=Math.max(0,debt-(year-1)*annualPrincipal)*i.interest;
 const cost=opex+replacement+delayCost;const cash=cost+interest+annualPrincipal;
 cumulative+=cost;totalCost+=cost;totalHours+=demand;npv+=cost/(1+i.discount)**year;pvHours+=demand/(1+i.discount)**year;
 rows.push({year,operating,onsiteHours,leasedHours,productiveHours:demand,idleBurden,electricity,staffing,maintenance,lease,opex,replacement,delayCost,interest,principal:annualPrincipal,projectCost:cost,equityCash:cash,cumulative});
}
const preopening=upfront+(openYear===2?rows[0].opex+rows[0].delayCost+rows[0].interest:0)+rows[openYear-1].lease*.25;
const risk=(facility+grid)*.8+fleet*.7+rows[openYear-1].lease*.25;
return {strategy,scenario,share,gpuCount:gpuCount*share,demand,facility,grid,fleet,upfront,debt,equity:upfront-debt,openYear,preopening,risk,rows,totalCost,totalHours,npv,costPerHour:pvHours?npv/pvHours:null,annualOpex:rows[openYear-1].opex};
}
export function compare(i:Inputs,s:Scenario){return (['Build & own','Lease capacity','Phased hybrid'] as Strategy[]).map(x=>calculate(i,s,x));}
