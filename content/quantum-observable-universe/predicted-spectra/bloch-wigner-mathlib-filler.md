**Remark (Bloch-Wigner dilogarithm $D$ on the unit circle).**

Building on [`rem:clausen-function-mathlib-filler`](#rem:clausen-function-mathlib-filler), the Lean file [`bloch-wigner-mathlib-filler.lean`](bloch-wigner-mathlib-filler.lean) defines the Bloch-Wigner dilogarithm restricted to unit-circle shape parameters $z = e^{i\theta}$:

$$
  D(z) \;:=\; \mathrm{Im}(\mathrm{Li}_2(z))\;+\; \log|z| \cdot \arg(1 - z),
\qquad
  D(e^{i\theta}) \;=\; \mathrm{Cl}_2(\theta) \quad (\text{since } |z|=1, \log|z|=0).
$$

This is the case relevant to QOU's hyperbolic-knot contributions, where shape parameters are unit-circle roots. See [Table 1](#tbl:bloch-wigner-mathlib-filler-table1-data).

See [Table 2](#tbl:bloch-wigner-mathlib-filler-table2-data) for added Lean carriers.

The unit-circle restriction of $D$ is sufficient for the hyperbolic-knot/Bloch-Wigner chain in the framework. Every hyperbolic knot embeddable in Bring's surface has shape parameters on the unit circle. The general $D : \mathbb{C} \setminus \{0,1\} \to \mathbb{R}$ remains an open Mathlib gap but does not block the chain.

See [Table 3](#tbl:bloch-wigner-mathlib-filler-table3-data) for remaining blocked components.

With this filler, every Bloch-Wigner value referenced in the $\alpha_{\text{EM}}$ chain is a Lean carrier with an explicit definition. The combination 

$$
  \mathrm{Cl}_2 \;\hookrightarrow\;
  \text{BW dilogarithm on unit circle} \;\hookrightarrow\;
  \text{hyperbolic-knot volumes}
$$

is fully populated at the carrier level. The substantive mathematical content remains as documented Mathlib gaps, but the infrastructure for stating those gaps is in place.
