import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic

/-!
# The additive per-bond chain cannot produce a saturation peak

`computations/probe_collective_binding_residual.py` argues — at what its own
docstring calls "near-proof level" — that the linear-chain binding form

    B_sym = α · [ (Z−1)·L_pp + L_pn + (N−1)·L_nn ]

"has **no mechanism to produce a saturation PEAK** at a specific mass number".
That argument is load-bearing: it is what narrows the collective-binding search
and tells the keystone what kind of term is missing. But AGENTS.md
§"Before declaring 'refuted'" permits a **scope-(b) structural exclusion** only
when a *proved invariant* forbids the class. A near-proof in a Python docstring
is not that. This file supplies the invariant.

## The invariant

Fix an isobaric chain — an isospin excess `d = N − Z` held constant, so
`Z = (A−d)/2` and `N = (A+d)/2`. Then the per-nucleon chain binding is
**exactly a hyperbola in `A`**:

    B_sym(A)/A  =  c₁ + c₂/A,
      c₁ = α·(L_pp + L_nn)/2                                   (independent of d)
      c₂ = α·[ (−d/2 − 1)·L_pp + L_pn + (d/2 − 1)·L_nn ]       (carries all d-dependence)

`chainPerNucleon_eq_hyperbola`, proved by `ring` — an identity, not an estimate.

And a hyperbola `c₁ + c₂/A` is **monotone** on `A > 0`, so it never exceeds both
of its neighbours: `hyperbola_no_interior_max`. Hence the chain form attains no
strict interior maximum in `A` — no saturation peak — for *any* values of the
per-bond constants, of `α`, and of `d`.

## Why this is the right invariant to prove

The asymptote `c₁` does **not** depend on `d`. So the exclusion is not an
artifact of looking along `N = Z`: every isobaric chain is a hyperbola
approaching the *same* limit `α(L_pp + L_nn)/2`, differing only in the `1/A`
coefficient. Varying the bond-type composition moves `c₂`, which changes how the
curve approaches the plateau — but not that it approaches monotonically.

Measured `B/A` has an interior maximum near ⁵⁶Fe. So the missing term is not a
re-weighting of the per-bond constants, and no choice of `L_pp, L_pn, L_nn` can
be made to produce the peak. That is the content the search needed, now as a
theorem.

## Scope — (b), and precisely delimited

Scope-**(b) structural exclusion**, invariant: the exact hyperbolic identity plus
monotonicity of `x ↦ c₂/x` on `x > 0`.

It excludes: **additive per-bond-type sums with constants fixed along an isobaric
chain** as a source of the saturation peak.

It does **not** exclude:

* the chain form as a *contribution* — an inaccurate total does not make a proved
  per-bond factor wrong (AGENTS.md permanence principle 1). The chain remains a
  valid additive term; what is excluded is its producing the peak *alone*.
* per-bond constants that themselves depend on `A` (then `c₁`, `c₂` are not
  constants and the identity does not apply);
* super-pairwise / collective terms, which is exactly where AGENTS.md already
  places the missing object ("a separate, super-pairwise additive extensive
  object");
* any statement about the *magnitude* of the residual. This is about shape.

## Base ring (§7c)

`ℝ` throughout, and genuinely so: the statement is an ordering fact
(`0 < a < b < c`, strict inequalities, `nlinarith`), i.e. archimedean content on
the observable side of the wall. There is no generic-`R` version — a hyperbola
having no interior maximum is meaningless without an order.

-- Ref: [leitner2026] computations/probe_collective_binding_residual.py
-- Ref: [leitner2026] docs/audits/2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md
-/

namespace QOU.MassTheory

/-- **The monotonicity invariant.** A hyperbola `A ↦ c₁ + c₂/A` on `A > 0` never
takes a value at an interior point `b` strictly greater than at *both* of
`a < b < c`. It is monotone, so it has no strict interior maximum.

Proof: the two hypotheses force `c₂ < 0` and `c₂ > 0` respectively. -/
theorem hyperbola_no_interior_max (c₁ c₂ : ℝ) {a b c : ℝ}
    (ha : 0 < a) (hab : a < b) (hbc : b < c) :
    ¬ (c₁ + c₂ / a < c₁ + c₂ / b ∧ c₁ + c₂ / c < c₁ + c₂ / b) := by
  rintro ⟨h1, h2⟩
  have hb : 0 < b := ha.trans hab
  have hc : 0 < c := hb.trans hbc
  rw [add_lt_add_iff_left] at h1 h2
  rw [div_lt_div_iff₀ ha hb] at h1
  rw [div_lt_div_iff₀ hc hb] at h2
  nlinarith [h1, h2, sub_pos.mpr hab, sub_pos.mpr hbc]

/-- Per-nucleon linear-chain binding along the isobaric chain of isospin excess
`d = N − Z`, i.e. with `Z = (A−d)/2` and `N = (A+d)/2`:

    B_sym/A = α·[ (Z−1)L_pp + L_pn + (N−1)L_nn ] / A. -/
noncomputable def chainPerNucleon (α Lpp Lpn Lnn d A : ℝ) : ℝ :=
  α * (((A - d) / 2 - 1) * Lpp + Lpn + ((A + d) / 2 - 1) * Lnn) / A

/-- **The exact hyperbolic identity.** Along any isobaric chain the per-nucleon
chain binding is exactly `c₁ + c₂/A`, with the asymptote `c₁ = α(L_pp+L_nn)/2`
**independent of the isospin excess `d`** — all of the `d`-dependence sits in the
`1/A` coefficient. An identity, discharged by `ring`. -/
theorem chainPerNucleon_eq_hyperbola (α Lpp Lpn Lnn d : ℝ) {A : ℝ} (hA : A ≠ 0) :
    chainPerNucleon α Lpp Lpn Lnn d A
      = α * (Lpp + Lnn) / 2
        + (α * ((-d / 2 - 1) * Lpp + Lpn + (d / 2 - 1) * Lnn)) / A := by
  unfold chainPerNucleon
  field_simp
  ring

/-- **No saturation peak.** For any per-bond constants, any `α`, and any isospin
excess, the per-nucleon chain binding does not exceed both of its neighbours at
an interior mass number — so it cannot reproduce the measured interior maximum of
`B/A`. -/
theorem chain_no_saturation_peak (α Lpp Lpn Lnn d : ℝ) {A₁ A₂ A₃ : ℝ}
    (h1 : 0 < A₁) (h12 : A₁ < A₂) (h23 : A₂ < A₃) :
    ¬ (chainPerNucleon α Lpp Lpn Lnn d A₁ < chainPerNucleon α Lpp Lpn Lnn d A₂ ∧
       chainPerNucleon α Lpp Lpn Lnn d A₃ < chainPerNucleon α Lpp Lpn Lnn d A₂) := by
  have h2 : 0 < A₂ := h1.trans h12
  have h3 : 0 < A₃ := h2.trans h23
  rw [chainPerNucleon_eq_hyperbola α Lpp Lpn Lnn d h1.ne',
      chainPerNucleon_eq_hyperbola α Lpp Lpn Lnn d h2.ne',
      chainPerNucleon_eq_hyperbola α Lpp Lpn Lnn d h3.ne']
  exact hyperbola_no_interior_max _ _ h1 h12 h23

/-- **Non-vacuity.** The chain form is a genuine hyperbola with a nonzero `1/A`
coefficient for admissible constants — the exclusion is not about a degenerate
constant function. Here `α = 1, L_pp = L_nn = 0, L_pn = 1, d = 0` gives
`chainPerNucleon = 1/A`, strictly decreasing. -/
example {A : ℝ} (hA : A ≠ 0) : chainPerNucleon 1 0 1 0 0 A = 1 / A := by
  unfold chainPerNucleon; field_simp; ring

end QOU.MassTheory
