import { diagram } from "../../schema/builders";

export default diagram({
  label: "fig:bring-fibre-qhalf",
  title:
    "Bring chiral fibre at $q = \\tfrac{1}{2}$: real segment with well-separated sheets",
  caption:
    "Two panels. **Left:** the $\\mathbb{CP}^1$ base (one-point compactification rendered as a unit circle, with each $z$ mapped to $z/(1+|z|)$ for display) with the real segment $z \\in [-0.5, 1.5]$ highlighted as a thick black line, well away from the six complex branch points of the chiral cubic $X^3 + (z+1)X^2 + (z^2+z+1)X + (z^3+z^2+z+1) = 0$. **Right (stacked):** Re$(X)$ and Im$(X)$ sub-plots showing the three sheets along the highlighted real segment. One sheet is real (Im $X = 0$, solid line); the other two form a complex-conjugate pair (dashed + dotted) with imaginary parts equal in magnitude and opposite in sign.",
  tags: [
    "brings-surface",
    "chiral-fibre",
    "real-segment",
    "descartes-universe",
    "figure",
    "phase-1-pr-1075",
  ],
  uses: ["fig:bring-fibre-q0"],
  meta: {
    file: "figures/bring-fibre-qhalf.pdf",
    altFile: "figures/bring-fibre-qhalf.svg",
    generator: "computations/bring_chiral_fibre_figure.py",
    witness: "computations/bring-chiral-fibre-figure.witness.json",
    workplan: "docs/workplans/2026-05-24-pr31-affine-light-cone-redo.md",
  },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): We generate this via [`bring_chiral_fibre_figure.py`](../../../computations/bring_chiral_fibre_figure.py), witnessed by [`bring-chiral-fibre-figure.witness.json`](../../../computations/bring-chiral-fibre-figure.witness.json)." },
  ],
});
