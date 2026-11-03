import type { Config } from "tailwindcss";

export default {
  content: ["./app/**/*.{ts,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Roobert", "ui-sans-serif", "system-ui", "sans-serif"],
      },
      colors: {
        oat: { 100: "#FEFDFB", 200: "#F4F3F0", 300: "#D1CDC7", 400: "#7B7974", 500: "#1B1A18" },
        line: "#E6E8EC",
      },
      keyframes: {
        dash: { to: { strokeDashoffset: "-24" } },
        glow: {
          "0%,100%": { boxShadow: "0 0 0 0 rgba(253,190,17,0.55)" },
          "50%": { boxShadow: "0 0 0 8px rgba(253,190,17,0)" },
        },
      },
      animation: {
        dash: "dash 0.8s linear infinite",
        glow: "glow 1.4s ease-in-out infinite",
      },
    },
  },
  plugins: [],
} satisfies Config;
