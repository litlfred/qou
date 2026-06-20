*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Remark (Bloch-Wigner dilogarithm $D$ on the unit circle).**

Building on
[`rem:clausen-function-mathlib-filler`](#rem:clausen-function-mathlib-filler),
the Lean file [`bloch-wigner-mathlib-filler.lean`](bloch-wigner-mathlib-filler.lean)
defines the Bloch-Wigner dilogarithm restricted to unit-circle
shape parameters $z = e^{i\theta}$:

$$
  D(z) \;:=\; \mathrm{Im}(\mathrm{Li}_2(z))\;+\; \log|z| \cdot \arg(1 - z),
\qquad
  D(e^{i\theta}) \;=\; \mathrm{Cl}_2(\theta) \quad (\text{since } |z|=1, \log|z|=0).
$$

This is the case relevant to QOU's hyperbolic-knot contributions,
where shape parameters are unit-circle roots:

See [Table 1](#tbl:bloch-wigner-mathlib-filler-table1-data).

## Lean carriers added

See [Table 2](#tbl:bloch-wigner-mathlib-filler-table2-data).

## Mathlib gaps remaining

The unit-circle restriction of $D$ is **all that's needed for the
hyperbolic-knot $\leftrightarrow$ Bloch-Wigner chain in the QOU framework**: every
hyperbolic knot embeddable in Bring's surface has shape parameters
on the unit circle (since the corresponding Kleinian groups are
arithmetic). The general $D : \mathbb{C} \setminus \{0,1\} \to \mathbb{R}$
with the boundary correction $\log|z| \arg(1-z)$ is a Mathlib gap
remaining open, but it is **not blocking** the QOU chain.

What is still blocked:

See [Table 3](#tbl:bloch-wigner-mathlib-filler-table3-data).

## Significance

With this filler added, **every BW value referenced in the α_EM
chain is now a Lean carrier with explicit definition**, not an
opaque or cited reference. The combination

$$
  \mathrm{Cl}_2 \;\hookrightarrow\;
  \text{BW dilogarithm on unit circle} \;\hookrightarrow\;
  \text{hyperbolic-knot volumes}
$$

is fully populated at the carrier level. The substantive
mathematical content (pentagon identity, BlochGroup, Suslin
uniqueness) remains as documented Mathlib gaps — but the
*infrastructure for stating those gaps* is now in place.
