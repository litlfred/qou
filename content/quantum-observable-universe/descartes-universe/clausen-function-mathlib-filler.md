**Remark (Clausen function `Cl_2` as repo-internal Mathlib filler).**

Mathlib does not currently expose the Clausen function

$$
  \mathrm{Cl}_2(\theta)
  \;:=\;
  \sum_{k = 1}^\infty \frac{\sin(k\theta)}{k^2}
  \;=\; \mathrm{Im}\,\mathrm{Li}_2(e^{i\theta}),
$$

which is the imaginary part of the dilogarithm on the unit circle
and the standard ingredient in hyperbolic-volume formulas:

$$
  \mathrm{Vol}(4_1)\;=\;2\,\mathrm{Cl}_2(\pi/3)\;\approx\;:val[Vol_4_1]{precision=6},
  \qquad
  \mathrm{Vol}(\mathcal{B}_3)\;=\;8\,\mathrm{Cl}_2(\pi/4)\;=\;8G\;\approx\;7.327724.
$$

The Lean file [`clausen-function-mathlib-filler.lean`](clausen-function-mathlib-filler.lean)
provides:

| Definition | Content | Status |
|---|---|---|
| `Cl_2 : ℝ → ℝ` | $\sum_{k\geq 1}\sin(k\theta)/k^2$ via `tsum` | unconditional, no longer opaque |
| `Cl_2_zero` | $\mathrm{Cl}_2(0) = 0$ | proved by `simp` |
| `Catalan_constant` | $G = \mathrm{Cl}_2(\pi/2)$ carrier | unconditional def |
| `Vol_figure_8` | $2\,\mathrm{Cl}_2(\pi/3)$ carrier | unconditional def |
| `Vol_Borromean` | $8\,\mathrm{Cl}_2(\pi/4)$ carrier | unconditional def |
| `Cl_2_reflection_2pi_open` | sketch placeholder | open (Fourier-series infra) |
| `Cl_2_pi_third_positive_open` | sketch placeholder | open (tail bounds) |

This unconditionalises the BW values used throughout the α_EM
chain, replacing the previous opaque-or-cited references with
explicit Lean carriers. Downstream blocks
[`em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode),
[`figure-8-archimedean-illustration`](../braids-and-knots/figure-8-archimedean-illustration.md),
[`bring-hyperbolic-knot-bloch-decomposition`](#conj:bring-hyperbolic-knot-bloch-decomposition),
and
[`binding-scale-catalan`](../braids-and-knots/binding-scale-catalan.md)
can now reference $\mathrm{Cl}_2$, $\mathrm{Vol}(4_1)$, and
$\mathrm{Vol}(\mathcal{B}_3)$ via the Lean carriers in this file.

## Mathlib gaps still open after this filler

| Missing piece | Used by | Substantive work needed |
|---|---|---|
| `Real.dilog` / `Complex.dilog` | Bloch-Wigner $D$ on $\mathbb{C}\setminus\{0,1\}$ | partial (`LiTwo` in dilogarithm-archimedean-limit.lean) |
| `BlochGroup F` for number field $F$ | Suslin map, `BlochSuslinUniqueness` | substantial — quotient of free abelian group on $F^\times \times F^\times$ by 5-term pentagon |
| Suslin map $K_3^{\mathrm{ind}}(\mathbb{C}) \to \mathbb{R}$ | `BlochSuslinUniqueness` | depends on `BlochGroup` |
| Fourier-series identities for $\mathrm{Cl}_2$ | reflection / functional equation | depends on Mathlib's Fourier-series infra (in progress upstream) |

The four §3b-cond classes (BlochSuslinUniqueness, ArchimedeanLimit,
BringZeroModeBlochClass, BringHyperbolicDecomposition,
BWQIndependence, BlochWignerInjective) remain as the residual
mathematical infrastructure gaps — closing them in Lean requires
either upstream Mathlib contributions (the natural place) or
repo-internal substantial formalisations.

## Pattern

Each Mathlib gap is a separate, scoped task. The Cl_2 filler
above shows the cleanest case: one well-known function, defined as
a `tsum`, with two unconditional boundary lemmas and four
sketched-but-open extensions awaiting Fourier-series
infrastructure. The same pattern can be applied to:

* a `Real.dilog` filler (extending the existing `LiTwo` to the
  complex domain via `Complex.dilog`);
* a minimal `BlochGroup F` filler (free abelian group quotient by
  5-term pentagon relations) — substantial, ~200 lines.

These are not addressed here; the present file restricts to the
single-function $\mathrm{Cl}_2$ filler that directly supports the
α_EM and figure-8 chains.
