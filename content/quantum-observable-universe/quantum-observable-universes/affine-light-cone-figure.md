**Figure (affine light cone on Bring's brane, formal math-book style).**

*Single-panel illustration of the affine light-cone wedge over the
brane locus in the spacetime affine chart $z = x_0/x_1 \in \mathbb{CP}^1$,
re-derived from natural Bring coordinates per the the prior work redo workplan
(Phase 2).*

**Brane curve.** The thick black curve is the locus
$\{(z, X_{\mathrm{real}}(z)) : z \in [-1.5, 2.5]\}$
where $X_{\mathrm{real}}(z)$ is the real root of the canonical Bring
chiral cubic

$$
  X^3 + (z+1)\, X^2 + (z^2+z+1)\, X + (z^3 + z^2 + z + 1) = 0
$$

at the given $z$. The cubic's discriminant has six complex zeros at
$z \approx (0.119, \pm 1.054)$, $(0.106, \pm 0.937)$,
$(-0.975, \pm 0.223)$ (see [fig:bring-fibre-q0](#fig:bring-fibre-q0));
the real interval $z \in [-1.5, 2.5]$ stays well outside any
neighbourhood of those branch points, so $X_{\mathrm{real}}$ is a
single-valued smooth function on the interval.

**Affine light cone.** Two thin straight lines bound a wedge opening
from the big-bang vertex
$(-1.5, X_{\mathrm{real}}(-1.5)) \approx (-1.5, 0.811)$
toward the heat-death horizon at $z = 2.5$, with a vertical opening of
$\pm 1.5$ in the $X$ direction. No fabricated 3D surface or
exponential-profile brane — the wedge is purely a 2D bounded region
of the spacetime-affine-chart $(z, X)$-plane.

**Observer.** A small filled black circle at the substrate point
$q_0 \approx 1.1099786$ (imported from `q_parameter.Q`,
which derives $q_0$ from the CODATA 2022 $m_\mu / m_e$ ratio and the
SnapPy hyperbolic volume of the figure-eight knot complement; see
`docs/canonical-derivation-cheat-sheet.md`). The observer sits on the
brane at $(q_0, X_{\mathrm{real}}(q_0)) \approx (1.110, -1.743)$. A
vertical dotted line marks the substrate slice.

**Euler-characteristic annotation.** The corner box records
$\chi(A) = -6$, equivalently $\chi(\Sigma_4) = -6$, the
Euler-characteristic constraint of Bring's surface that fixes the
algebraic substrate's topology in the QOU framework
([archimedean-condition.md](../archimedean-universe/archimedean-condition.md)).

This figure is generated programmatically by
[`affine_light_cone_figure.py`](../../../computations/affine_light_cone_figure.py),
with the parameters and verified sample values recorded in
[`affine-light-cone-figure.witness.json`](../../../computations/affine-light-cone-figure.witness.json).
Formal math-book style (black ink on white, line styles only, no
gradient or decorative color) per author directive.
