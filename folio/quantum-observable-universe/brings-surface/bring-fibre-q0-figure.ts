import { diagram } from "../../schema/builders";

export default diagram({
  label: "fig:bring-fibre-q0",
  title:
    "Bring chiral fibre at $q \\to 0$: branch-point neighbourhood with sheet merging",
  caption:
    "Two panels. **Left:** the $\\mathbb{CP}^1$ base (one-point compactification rendered as a unit circle, with each $z$ mapped to $z/(1+|z|)$ for display) showing the 6 branch points of the chiral cubic $X^3 + (z+1)X^2 + (z^2+z+1)X + (z^3+z^2+z+1) = 0$ as filled black dots, plus a dashed neighbourhood circle of radius $0.15$ around the chosen branch point. **Right:** the three sheets $X_1, X_2, X_3$ as $z$ traverses the dashed circle, parametrised by angle $\\theta \\in [0, 2\\pi]$. Two sheets (solid + dashed) come close — the $B_3$-monodromy signature of sheet merging near the branch point — while the third (dotted) remains well-separated.",
  tags: [
    "brings-surface",
    "chiral-fibre",
    "branch-point",
    "monodromy",
    "descartes-universe",
    "figure",
    "phase-1-pr-1075",
  ],
  uses: [
    "rem:brings-curve",
  ],
  meta: {
    file: "figures/bring-fibre-q0.pdf",
    altFile: "figures/bring-fibre-q0.svg",
    generator: "computations/bring_chiral_fibre_figure.py",
    witness: "computations/bring-chiral-fibre-figure.witness.json",
    workplan: "docs/workplans/2026-05-24-pr31-affine-light-cone-redo.md",
  },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Branch point $z_c \\approx 0.106 - 0.937i$ (see the `branch_point_chosen` field in the witness). We generate this figure programmatically via [`bring_chiral_fibre_figure.py`](../../../computations/bring_chiral_fibre_figure.py). We record parameters and verified sample values in [`bring-chiral-fibre-figure.witness.json`](../../../computations/bring-chiral-fibre-figure.witness.json)." },
  ],
});
