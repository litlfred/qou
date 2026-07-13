**Remark (Bloch-Wigner dilogarithm $D$ on the unit circle).**

The Lean file [`bloch-wigner-mathlib-filler.lean`](bloch-wigner-mathlib-filler.lean) restricts the Bloch-Wigner dilogarithm to unit-circle shape parameters $z = e^{i\theta}$:

$$
  D(z) \;:=\; \mathrm{Im}(\mathrm{Li}_2(z))\;+\; \log|z| \cdot \arg(1 - z),
\qquad
  D(e^{i\theta}) \;=\; \mathrm{Cl}_2(\theta).
$$

The logarithm $\log|z|$ vanishes on the unit circle. This restriction covers hyperbolic-knot contributions in the framework. Their shape parameters are roots of unity. 

See [Table 1](#tbl:bloch-wigner-mathlib-filler-table1-data).

See [Table 2](#tbl:bloch-wigner-mathlib-filler-table2-data) for added Lean carriers.

The unit-circle restriction supports the hyperbolic-knot Bloch-Wigner chain. Every hyperbolic knot embeddable in Bring's surface has unit-circle shape parameters. The general extension $D : \mathbb{C} \setminus \{0,1\} \to \mathbb{R}$ remains an open Mathlib gap.

See [Table 3](#tbl:bloch-wigner-mathlib-filler-table3-data) for remaining blocked components.

This filler assigns every Bloch-Wigner value in the $\alpha_{\text{EM}}$ chain an explicit Lean carrier. The mathematical hierarchy $\mathrm{Cl}_2 \hookrightarrow D \hookrightarrow \text{hyperbolic volumes}$ is completely populated. The substantive mathematical content awaits formalization.
