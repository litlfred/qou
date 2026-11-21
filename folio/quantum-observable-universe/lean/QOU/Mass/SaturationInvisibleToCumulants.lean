/-
# The saturation mechanism is invisible to `b₃` and `b₄`

`QOU.Mass.SaturationSignGateTension` proved that `b₃ > 0`, `b₄ > 0` and a
saturating binding force **at least two** contributions of opposite curvature,
and the natural pairing to try was the corpus's own two pieces: a **convex**
`s`-shell term (support-bounded, dying at `A = 5`) plus a **saturating**
bounded-degree coordination term (`QOU.Mass.CoordinationSaturation`).

**That pairing is degenerate on the data, and this file says why.**

## The bond count of a degree-capped graph

A coordination cap at degree `k` gives the bond count `f_k(A) = A·min(A−1,k)/2`.
For `A ≤ k+1` the cap does not bind — `min(A−1,k) = A−1` — so `f_k` is
*identically* the complete-graph count `C(A,2)` there. With `k ≥ 3` that covers
the whole `A ≤ 4` window in which `b₃` and `b₄` are measured, and the
complete-graph count contributes exactly zero to both:

    b₃-contribution = C(3,2) − 3·C(2,2) = 3 − 3 = 0
    b₄-contribution = C(4,2) − 4·C(3,2) + 6·C(2,2) = 6 − 12 + 6 = 0

`complete_contributes_nothing`. Measured, `k = 2` also gives zero at `b₃`; only
`k = 1` — a pure dimer model, each nucleon bonded to one partner — contributes at
all, and it has the wrong sign.

## What that costs the two-term programme

**A coordination cap at `k ≥ 2` contributes nothing to either cumulant.** It only
bites at `A ≥ 5`. So it cannot be one of the two terms inside the window: there,
effectively, there is **one** term, and it must carry `b₂`, `b₃` and `b₄` by
itself.

That is *not* a contradiction with the two-term necessity theorem — the two terms
act in disjoint regimes rather than together. But it changes the test completely:
the convex term now faces **three constraints on one coefficient**, hence **two
parameter-free predictions**, namely the ratios

    b₃/b₂ = 0.6411228    b₄/b₂ = 4.1551403      (isospin average)
    b₃/b₂ = 0.8127866    b₄/b₂ = 3.4684851      (Coulomb-corrected)

Nothing tested comes close — `dim[1^A]` gives `(−2.333, 3.5)`, `A³` gives
`(0.375, 0.5)`, `A!` gives `(0, 6)`, the `k = 1` dimer `(−1.5, 2)`, `2^A`
`(−1, 2)`. Measured in
`computations/probes/two_term_structure_degeneracy_probe.py`.

## Scope

This refutes **the specific pairing** — shell-plus-saturation — as a way to
explain the cumulants, by showing the saturating half is inert where they live.
It does not touch `CoordinationSaturation` itself, which is about `A → ∞` and is
unaffected by having no signature at `A ≤ 4`; nor does it refute two-term
structures in general. What it supplies is a much sharper target: a
**two-number fingerprint** `(b₃/b₂, b₄/b₂)` that a candidate convex term must hit
with **zero** free parameters, replacing the single ratio the programme had
before.

Base ring is a generic `CommRing`; the content is arithmetic on three values.

Bean `qou-edt7`.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring

namespace QOU.Mass.SaturationInvisibleToCumulants

variable {R : Type*} [CommRing R]

/-- The `b₃` contribution of a term taking values `f₂, f₃` at `A = 2, 3`. -/
def b3Contrib (f₂ f₃ : R) : R := f₃ - 3 * f₂

/-- The `b₄` contribution of a term taking values `f₂, f₃, f₄`. -/
def b4Contrib (f₂ f₃ f₄ : R) : R := f₄ - 4 * f₃ + 6 * f₂

/-- **A degree cap at `k ≥ 3` is invisible to both cumulants.** For `A ≤ k+1` the
cap does not bind, so the bond count is the complete-graph count `1, 3, 6` at
`A = 2, 3, 4` — and that contributes exactly zero to `b₃`. -/
theorem complete_b3_eq_zero : b3Contrib (1 : R) 3 = 0 := by
  unfold b3Contrib; ring

/-- And exactly zero to `b₄`. -/
theorem complete_b4_eq_zero : b4Contrib (1 : R) 3 6 = 0 := by
  unfold b4Contrib; ring

/-- Both at once: the complete-graph bond count — which is what *any* cap
`k ≥ 3` reduces to on `A ≤ 4` — contributes nothing to either cumulant, so a
saturating coordination term has **no signature in the window where `b₃` and `b₄`
are measured**. -/
theorem complete_contributes_nothing :
    b3Contrib (1 : R) 3 = 0 ∧ b4Contrib (1 : R) 3 6 = 0 :=
  ⟨complete_b3_eq_zero, complete_b4_eq_zero⟩

/-- The `k = 2` cap gives bond counts `1, 3, 4` and still contributes nothing to
`b₃` — only `b₄` sees it, and with the wrong sign (`−2`). -/
theorem cap_two_b3_eq_zero : b3Contrib (1 : R) 3 = 0 := complete_b3_eq_zero

/-- **The single-term consequence.** With the saturating half inert, one term
carries all three cumulants, so its `b₃/b₂` and `b₄/b₂` are fixed by its shape
alone — no coefficient can move them. Stated as: scaling a term by `γ` leaves
both ratios unchanged. -/
theorem ratios_are_scale_free (γ f₂ f₃ f₄ : R) :
    b3Contrib (γ * f₂) (γ * f₃) = γ * b3Contrib f₂ f₃ ∧
      b4Contrib (γ * f₂) (γ * f₃) (γ * f₄) = γ * b4Contrib f₂ f₃ f₄ := by
  refine ⟨?_, ?_⟩
  · unfold b3Contrib; ring
  · unfold b4Contrib; ring


/-- **First projection of scale-freeness for `b3Contrib` (`qou-bmz8`).**
Scaling `(f₂, f₃)` by `γ` scales `b3Contrib` by `γ`. -/
theorem b3Contrib_scale (γ f₂ f₃ : R) :
    b3Contrib (γ * f₂) (γ * f₃) = γ * b3Contrib f₂ f₃ :=
  (ratios_are_scale_free γ f₂ f₃ 0).1

end QOU.Mass.SaturationInvisibleToCumulants
