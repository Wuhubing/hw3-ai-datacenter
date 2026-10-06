# Two-minute website demonstration

The video uses the student’s supplied English recording. Long pauses are shortened and speech is accelerated by 1.095x with pitch preserved to fit 120 seconds. No synthetic voice is used.

The visuals are an edited sequence of actual hosted website screenshots and the system diagram, not a continuous screen recording. Captures show earlier real testing; their timestamps are historical. The website and GitHub repository are now public. Native recording controls did not respond during this revision, so existing captures were retained.

## Reading script and scene timing

The following is the intended reading script, not a verbatim transcription of pronunciation, hesitations, or repetitions in the recording.

### 0.0–17.2 seconds: The investment decision

Welcome to Compute Commons. This website evaluates a proposed university AI data center. My recommendation is to lease capacity first, while keeping a smaller, phased facility as an option. There are no signed long-term computing commitments or confirmed grid terms.

### 17.2–29.8 seconds: Stress the demand

The model compares building, leasing, and a phased hybrid. Here, I halve GPU utilization. The cost of owned capacity rises sharply because fixed costs remain, even when equipment is underused.

### 29.8–47.6 seconds: Inspect ten years of cash flow

The investment page shows ten years of cash flow. It separates facility and GPU costs, including electricity, staffing, maintenance, equipment replacement, and financing. These prices are clearly labeled assumptions, not supplier quotations.

### 47.6–62.1 seconds: Compare three countries

The country comparison covers the United States, China, and Singapore. Sources and reporting years are visible. National electricity generation does not prove that power is available at a particular site.

### 62.1–82.5 seconds: Plan for failure

This diagram shows the conditional first phase: five megawatts of IT load and six point two five megawatts of total demand. It includes backup power, cooling, networking, and failure paths. The forty-eight-hour backup concept still requires engineering verification.

### 82.5–98.4 seconds: Refresh evidence safely

The evidence page distinguishes facts, assumptions, calculations, and unknowns. An authorized user can refresh the external dataset without rebuilding the website. Retrieval times are visible, and failed updates preserve existing data.

### 98.4–105.9 seconds: Ask about the saved design

The AI adviser reads the saved design and evidence. It reports the baseline PUE of one point two five.

### 105.9–111.4 seconds: Inspect the evidence used

It explains uncertainties and links to supporting sources.

### 111.4–120.0 seconds: Review the decision package

Finally, the submission package includes the investment memo, system diagrams, presentation, and test results. Thank you.

## Rebuild

Run `python scripts/build-demo.py /absolute/path/to/narration.m4a` with the supplied source recording, Pillow, ffmpeg and ffprobe. The original personal recording is kept outside the repository; its voice appears in the public finished video. Timing/edit metadata is in `data/demo-edit-metadata.json`.
