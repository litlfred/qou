import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:categorical-fourier",
  label: "rem:laplace-fourier-wick-rotation",
  title: "Laplace and Fourier as Wick-rotated grouplike pairings",
  tags: ["laplace", "fourier", "wick-rotation", "hopf-algebra", "grouplike"],
  uses: [
    "def:categorical-fourier",
    "def:q-exponential",
  ],
});
