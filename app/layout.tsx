import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Compute Commons | University AI Infrastructure",
  description: "Evidence-led decisions for shared university AI infrastructure. Compare build, lease and phased capacity.",
  other: {
    "codex-preview": "development",
  },
  icons: {
    icon: "/favicon.svg",
    shortcut: "/favicon.svg",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased">{children}</body>
    </html>
  );
}
