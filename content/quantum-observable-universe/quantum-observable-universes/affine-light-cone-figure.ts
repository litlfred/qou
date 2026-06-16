import { diagram } from "../../schema/builders";

export default diagram({
  label: "fig:affine-light-cone",
  title:
    "Affine light cone on Bring's brane (formal math-book style)",
  caption:
    "Single-panel figure showing the affine light-cone wedge on the brane locus of Bring's chiral cubic, in the spacetime affine chart $z = x_0/x_1 \\in \\mathbb{CP}^1$. **Brane**: the thick black curve $(z, X(z))$ where $X(z)$ is the real root of $X^3 + (z+1)X^2 + (z^2+z+1)X + (z^3+z^2+z+1) = 0$ over the real interval $z \\in [-1.5, 2.5]$ (well away from the six complex branch points). **Affine light cone**: a wedge with vertex at the big-bang endpoint $(z_{\\text{vertex}}, X(z_{\\text{vertex}}))$ opening toward the heat-death endpoint $(z_{\\text{horizon}}, X(z_{\\text{horizon}}))$; two thin straight lines bound the wedge (no fabricated 3D surface, no gradient). **Observer**: a small filled circle at the substrate $q_0 \\approx 1.1099786$ (imported from `q_parameter.Q`), with a vertical dotted line marking the substrate slice. **Annotation**: corner box $\\chi(A) = -6$, recording the Euler-characteristic constraint $\\chi(\\Sigma_4) = -6$ for Bring's surface.",
  tags: [
    "brings-surface",
    "affine-light-cone",
    "brane",
    "spacetime-affine-chart",
    "substrate-q0",
    "euler-characteristic",
    "descartes-universe",
    "figure",
    "phase-2-pr-1075",
  ],
  uses: [
    "fig:bring-fibre-q0",
  ],
  meta: {
    file: "figures/affine-light-cone.pdf",
    altFile: "figures/affine-light-cone.svg",
    generator: "computations/affine_light_cone_figure.py",
    witness: "computations/affine-light-cone-figure.witness.json",
    workplan: "docs/workplans/2026-05-24-pr31-affine-light-cone-redo.md",
  },
});
