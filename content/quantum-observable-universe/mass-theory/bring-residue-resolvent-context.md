## The shared smaller-scope open math, now scaffolded

The α_shift universal derivation chain identified the pole-order origin
of the q-integer indices in several "empirical" fits.  What remained shared across the α_EM, p-n averaging,
and meson m_K/m_π treatments was
the residue/resolvent step: deriving the closed form
$F_n(q) = 1 / (1 - h_q \cdot q^n)$ from the contour-integral
evaluation on Bring's surface.

This proposition scaffolds that derivation as a single Lean class
+ theorem, then specialises to the three concrete pole orders used
downstream.

## Lean structure

- `class BringResidueAtOrder {R} [Field R] (n : ℕ) (q : R)` — the
  contour-integral / Schwarz-integral axiomatisation.  Its sole field
  `pole_nonzero : 1 - h_q · q^n ≠ 0` records the **pole
  non-vanishing** — the substantive output any concrete contour route
  must establish.
- `theorem bring_residue_equation` — sorry-free: given the class, the
  canonical resolvent $F_n(q) = (1 - h_q \cdot q^n)^{-1}$ satisfies the
  **resolvent equation** $(1 - h_q \cdot q^n) \cdot F_n(q) = 1$ (proof:
  `mul_inv_cancel₀ h.pole_nonzero`).
- Three specialisations:
  - `bring_residue_at_T_3_5` — pole order 10, used by p-n averaging
    ([p-n averaging uniqueness](#prop:pn-averaging-uniqueness));
  - `bring_residue_at_T_2_9` — pole order 9, used by 1/α_EM
    ([fine-structure observation](#rem:fine-structure-observation));
  - `bring_residue_meson_pair` — pole orders 3 and 4, used by
    $m_K^2/m_\pi^2$
    ([meson color-tube uniqueness](#prop:meson-color-tube-uniqueness)).
- `bring_residue_subsingleton` — Subsingleton companion.

## Closing the class instance

Closing `BringResidueAtOrder n q` requires either:

1. **Analytic route:** the Mathlib residue machinery
   (`Mathlib.Analysis.Complex.RemovableSingularity`,
    `Mathlib.MeasureTheory.Integral.CircleIntegral`) applied to the
   $\sigma$-action on Hecke representations at the torus-knot
   surface.  Standard but voluminous Mathlib imports.
2. **Algebraic route:** via the substrate's Bloch-Suslin framework
   in `em-coupling-bring-zero-mode.lean`'s `BringZeroModeBlochClass`,
   identifying the contour integral with a specific Bloch-group
   class on Bring's surface (the open computational sub-problem
   already scoped there).

Both routes converge on the same closed form
$F_n(q) = 1 / (1 - h_q \cdot q^n)$.  Closing the class is a
Mathlib-import follow-up; until then this file states the
**conditional uniqueness** of the resolvent form.

## Downstream consequence

Each specialisation collapses a separate residue-normalisation gap
into a **single shared open class instance**:

| where used | downstream form | resolvent specialisation |
|---|---|---|
| [fine-structure observation](#rem:fine-structure-observation) | $1/\alpha_{\rm EM} = q \cdot [9]_q \cdot [10]_q + 2/(3\pi)$ | `BringResidueAtOrder 9` + `10` (genus-4 pair) |
| [p-n averaging uniqueness](#prop:pn-averaging-uniqueness) | $\sigma_{pn}(q)$ Bring color-tube weight $1/(1 - h_q \cdot q^{10})$ | `BringResidueAtOrder 10` |
| [meson color-tube uniqueness](#prop:meson-color-tube-uniqueness) | $m_K^2 / m_\pi^2 = [3]_q \cdot [4]_q$ | `BringResidueAtOrder 3` + `4` (meson pair) |

Closing the class once therefore discharges the residue open math
in all three cases.

## Lean formalization

This proposition is **proved conditional on
`BringResidueAtOrder` class instances at the relevant pole orders**.
The four specialised theorems above are sorry-free conditional on
the class.  Closing the class is the Mathlib-import follow-up.
