import { example } from "../../schema/builders";

export default example({
  label: "ex:bach-intensity-profile",
  title: "Digitized Intensity Profile (Bach et al. 2013, Figure 3e)",
  uses: ["ex:bach-single-electron-buildup", "rem:bach-slit-parameters"],
  tags: [
    "imported", "arxiv:1210.6243", "double-slit", "experimental",
    "intensity-profile", "digitized-data",
  ],
  meta: {
    source: "arxiv:1210.6243",
    originalSection: "3",
    originalFigure: "3e",
    digitizedFrom: "Figure 3e, 6235 electron detections",
    digitizationMethod: "Threshold-based pixel extraction from arXiv PDF, 150-bin histogram",
    importedAt: "2026-03-25T00:00:00Z",
  },
});
