import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "ABM Plan Generator | Clay",
  description: "Your personalized ABM strategy for 2027.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="font-sans">{children}</body>
    </html>
  );
}
