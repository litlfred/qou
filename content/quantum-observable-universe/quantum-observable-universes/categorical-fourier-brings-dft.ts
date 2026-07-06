import { remark } from "../../schema/builders";

export default remark({
  label: "rem:categorical-fourier-brings-dft",
  interprets: "def:categorical-fourier",
  title: "Abelian instance: the Bring's-surface DFT and Briggs--Klein smoothness",
  tags: ["fourier", "dft", "bring-surface", "briggs-klein", "lagrange-resolvent"],
  uses: [
    "def:categorical-fourier",
    "def:briggs-klein-chart",
    "rem:lagrange-resolvents",
    "rem:brings-smoothness",
  ],
});
