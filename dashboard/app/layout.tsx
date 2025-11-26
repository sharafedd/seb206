import "./globals.css";
import type { Metadata } from "next";

import {Header} from "@/components/Header";
import {Footer} from "@/components/Footer";

export const metadata: Metadata = {
  title: "My Next App",
  description: "Simple app with header, footer and multiple pages",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <div className="layout">
          {/* HEADER */}
          <Header />

          {/* MAIN CONTENT */}
          <main className="main">{children}</main>

          {/* FOOTER */}
          <Footer />
        </div>
      </body>
    </html>
  );
}
