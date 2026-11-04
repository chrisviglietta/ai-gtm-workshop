/** @type {import('next').NextConfig} */
const isExport = process.env.EXPORT === "1";
export default {
  reactStrictMode: true,
  ...(isExport ? { output: "export", assetPrefix: ".", images: { unoptimized: true } } : {}),
};
