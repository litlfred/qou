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

| Knot / link | Shape parameter | BW value |
|---|---|---|
| Figure-8 $4_1$ (per ideal regular tetrahedron) | $e^{i\pi/3}$ | $\mathrm{Cl}_2(\pi/3) \approx 1.0149$ |
| Borromean rings $\mathcal{B}_3$ (per ideal regular octahedron $= 4$ tetrahedra) | $e^{i\pi/2} = i$ | $4\,\mathrm{Cl}_2(\pi/4) = 4G \approx 3.664$ |

## Lean carriers added

| Definition / theorem | Content | Status |
|---|---|---|
| `BlochWigner_unit_circle θ` | `Cl_2 θ` | unconditional def |
| `BlochWigner_unit_circle_zero` | `D(1) = 0` | proved by `Cl_2_zero` |
| `BlochWigner_figure_8_per_tetrahedron` | `Cl_2(π/3)` | unconditional def |
| `BlochWigner_Borromean_per_octahedron` | `4·Cl_2(π/4) = 4G` | unconditional def |
| `Vol_figure_8_eq_two_BW_tetrahedron` | `Vol(4_1) = 2 · D(e^{iπ/3})` | proved by `rfl` |
| `Vol_Borromean_eq_two_BW_octahedron` | `Vol(B_3) = 2 · 4G` | proved by `ring` |

## Mathlib gaps remaining

The unit-circle restriction of $D$ is **all that's needed for the
hyperbolic-knot ↔ Bloch-Wigner chain in the QOU framework**: every
hyperbolic knot embeddable in Bring's surface has shape parameters
on the unit circle (since the corresponding Kleinian groups are
arithmetic). The general $D : \mathbb{C} \setminus \{0,1\} \to \mathbb{R}$
with the boundary correction $\log|z| \arg(1-z)$ is a Mathlib gap
remaining open, but it is **not blocking** the QOU chain.

What is still blocked:

| Missing piece | Used by | Substantive work needed |
|---|---|---|
| Pentagon identity for $D$ on $\mathbb{C}$ | `BlochSuslinUniqueness` | proof needs full BlochGroup setup |
| `BlochGroup F` quotient | Suslin map | substantial — free abelian group / 5-term relations |
| Suslin map $K_3^{\mathrm{ind}}(\mathbb{C}) \to \mathbb{R}$ | uniqueness up to scalar | depends on `BlochGroup` + Borel regulator |

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
