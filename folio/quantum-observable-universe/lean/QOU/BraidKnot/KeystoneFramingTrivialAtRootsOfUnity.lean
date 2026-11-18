import QOU.BraidKnot.PolynomialShadowRigidity

/-!
# Matching at *every* root of unity forces the Seifert framing to be trivial

This composes two things the corpus already had into a conclusion neither carried
alone, and it closes — for the concrete RT/Seifert row — the object
`BWVacuumRowConcrete.lean` named as *surviving*.

## The two inputs

1. **The concrete row** (`BWVacuumRowConcrete.lean`, de-opaquing `bwS0_eq_hecke`):
   the RT/Seifert vacuum row of the framed `S³/2I` is
   `bwS0Concrete(λ) = S_{0λ} · θ_λ^f`, with `S_{0λ} = d_q(λ)/D` and the ribbon
   twist `θ_λ = q^{c(λ)}` (`KeystoneModularTwist.theta`, a **`zpow` with integer
   exponent** `c(λ) = contentSum λ`), `f : ℤ` the forced Seifert framing. Its
   capstone `bwS0Concrete_eq_hecke_forces_trivial_twist` shows the gate forces
   `θ_λ^f = 1` on every block — and stops there.

   That file records the `f ≠ 0` case as **REFUTED at the archimedean anchor**
   (real `q₀ > 1` makes `q₀^{c(λ)}` not a root of unity), while explicitly
   leaving open *"the **fibre** root-of-unity form (`|q| = 1`, hence
   `|θ_λ| = 1`) at the pre-τ categorical level, archimedean-continued to `q₀`"*.

2. **The reduction** (`KeystoneRootsOfUnityReduction.lean`): for rational
   functions, agreement at **all** roots of unity already forces agreement at
   `q₀` — no continuation step. The BW side qualifies: since `f·c(λ) ∈ ℤ`, the
   twist `θ_λ^f = q^{f·c(λ)}` is a **Laurent monomial**, and it multiplies the
   *same* `S_{0λ} = d_q/D` that the Hecke side carries — so the irrational `D`
   cancels from the comparison and what remains is rational. (This answers bean
   `qou-zngd` affirmatively for this construction.)

## What is proved here

`zpow_eq_one_on_rootsOfUnity_iff` — `q^k = 1` at **every** root of unity iff
`k = 0`. Elementary, via `eq_of_eval_eq_on_rootsOfUnity`: the polynomials `X^k`
and `1` agree on an infinite set, hence are equal, hence `k = 0` by degree.

`framing_trivial_of_gate_on_rootsOfUnity` — therefore, if the de-opaqued gate
holds at every root of unity, then `f · c(λ) = 0`; and if any block has
`c(λ) ≠ 0`, then **`f = 0`**.

## Why that closes the route rather than advancing it

`BWVacuumRowConcrete.lean` states in its own terms that *"the framing `f = 0`
carries zero Σ(2,3,5) data (reduces to the compact datum — a tautology)"*. So the
two horns are now both pinned:

| demand | consequence |
|---|---|
| match at **all** roots of unity | `f = 0` — tautological framing, no Σ(2,3,5) content |
| match at **finitely many** roots | does not pin: the n=5 vacuum row needs 25..33 values, Σ(2,3,5) supplies 5 (probe `wlambda_rational_shadow_degree_probe.py`) |

There is no third option that reaches `q₀`, because the reduction needs *all*
roots of unity to transport a value there, and the fibre geometry cannot supply
more than five.

### The load-bearing reading, stated rather than left implicit

"Closes the surviving object" depends on one interpretation, which is asserted
here so a reader can reject it rather than have to reconstruct it:

**A fibre-level identity of two objects means they agree at *every* root of
unity, not at one chosen level.** That is what it means for two Habiro / unified-
WRT elements to *be the same element* — the corpus's own framing, since a Habiro
element "can be considered as a function whose domain is the set of roots of
unity" (Beliakova–Le, quoted in `HabiroDomainVanishing.lean`). Under that
reading the theorem below applies and forces `f = 0`.

Under the *weaker* reading — the gate holds at one root of unity `ζ` of order `n`
— the conclusion does **not** follow, and should not be claimed: `ζ^{f·c(λ)} = 1`
merely needs `n ∣ f·c(λ)`, which is satisfiable with `f ≠ 0` (e.g. `f = n`). What
such a match does *not* come with is any route to `q₀`: the reduction needs the
full root-of-unity family, and the finite-data horn above shows five values do
not pin the function either. So the weaker reading leaves the framing
unconstrained but leaves the keystone exactly where it was — with the archimedean
step unbridged.

Nothing here excludes some *other* transport from a single level to `q₀`. It says
only that for this concrete row, both sides are explicit rational functions, so
whatever "continuation" means it has no freedom left: the two either agree as
rational functions (`⟺ f·c(λ) = 0`) or they disagree at `q₀`.

## Scope — this is a (b), and here is the invariant

Scope-**(b) structural exclusion**, per AGENTS.md §"Before declaring refuted",
citing a *proved* invariant rather than a magnitude probe: the exponent
`f · c(λ)` is an **integer**, and a nonzero integer power of the indeterminate is
not the constant `1` in `ℂ[X]` — a degree argument, discharged below.

The exclusion is **narrow and must not be over-read**. It says: *the concrete
RT/Seifert row `S_{0λ}·θ_λ^f`, with the twist entering as an integer power,
cannot match the compact Hecke datum at every root of unity unless the framing is
trivial.* It does **not** exclude:

* other constructions of the BW / path-integral vacuum row (a non-monomial
  twist, a `λ`-dependent framing, a correction term, an `f` varying with the
  root of unity);
* `bwS0_eq_hecke` itself under any such other construction;
* the Beasley–Witten localization program, which is a separate open construction
  (`bwse`, PR #4969) and is untouched by this.

It closes one named route, with its invariant on the table.

-- Ref: [beasleywitten2005] https://doi.org/10.4310/jdg/1143593746
-- Ref: [bakalovkirillov2001] Lectures on Tensor Categories and Modular Functors
-- Ref: [leitner2026] docs/coordination/s5-so3-keystone.md
-/

namespace QOU.BraidKnot.Keystone

open Polynomial

/-- A root of unity is nonzero: some positive power of it is `1`. -/
theorem isRootOfUnity_ne_zero {z : ℂ} (hz : IsRootOfUnity z) : z ≠ 0 := by
  obtain ⟨n, hn, hzn⟩ := hz
  intro h
  rw [h, zero_pow hn.ne'] at hzn
  exact zero_ne_one hzn

/-- `q ^ k = 1` at **every** root of unity iff the natural exponent is `0`.

The forward direction is the rigidity of the polynomial shadow: `X ^ k` and `1`
agree on an infinite set, so they are equal in `ℂ[X]`, so `k = 0` by degree. -/
theorem pow_eq_one_on_rootsOfUnity_iff (k : ℕ) :
    (∀ z : ℂ, IsRootOfUnity z → z ^ k = 1) ↔ k = 0 := by
  constructor
  · intro h
    have hpoly : (Polynomial.X : Polynomial ℂ) ^ k = 1 := by
      refine eq_of_eval_eq_on_rootsOfUnity ?_
      intro z hz
      simpa using h z hz
    have := congrArg Polynomial.natDegree hpoly
    simpa using this
  · rintro rfl
    intro z _
    simp

/-- **The integer-exponent form** — the shape the ribbon twist actually has,
`θ_λ^f = q ^ (f · c(λ))` with `f · c(λ) : ℤ`. It is `1` at every root of unity
iff the exponent vanishes. -/
theorem zpow_eq_one_on_rootsOfUnity_iff (k : ℤ) :
    (∀ z : ℂ, IsRootOfUnity z → z ^ k = 1) ↔ k = 0 := by
  constructor
  · intro h
    have hnat : ∀ z : ℂ, IsRootOfUnity z → z ^ k.natAbs = 1 := by
      intro z hz
      have hz0 : z ≠ 0 := isRootOfUnity_ne_zero hz
      have hk := h z hz
      rcases Int.natAbs_eq k with hEq | hEq
      · rw [hEq, zpow_natCast] at hk; exact hk
      · rw [hEq, zpow_neg, zpow_natCast, inv_eq_one] at hk; exact hk
    have := (pow_eq_one_on_rootsOfUnity_iff k.natAbs).mp hnat
    omega
  · rintro rfl
    intro z _
    simp

/-- **The keystone conclusion.** If the de-opaqued gate holds at *every* root of
unity — i.e. the twist contribution `q ^ (f · c(λ))` is trivial there — then the
integer `f · c(λ)` vanishes. -/
theorem framing_trivial_of_gate_on_rootsOfUnity {f c : ℤ}
    (h : ∀ z : ℂ, IsRootOfUnity z → z ^ (f * c) = 1) : f * c = 0 :=
  (zpow_eq_one_on_rootsOfUnity_iff (f * c)).mp h

/-- **The framing is forced to zero** as soon as one block has nonvanishing
content sum. `f = 0` is the framing `BWVacuumRowConcrete.lean` describes as
carrying zero Σ(2,3,5) data — the gate becomes a tautology. -/
theorem framing_eq_zero_of_gate_on_rootsOfUnity {f c : ℤ} (hc : c ≠ 0)
    (h : ∀ z : ℂ, IsRootOfUnity z → z ^ (f * c) = 1) : f = 0 := by
  have := framing_trivial_of_gate_on_rootsOfUnity h
  exact (mul_eq_zero.mp this).resolve_right hc

/-- **Non-vacuity of the hypothesis**: the gate condition genuinely holds when the
exponent vanishes, so the theorems above are not conditioned on an unsatisfiable
premise. -/
example (c : ℤ) : ∀ z : ℂ, IsRootOfUnity z → z ^ ((0 : ℤ) * c) = 1 := by
  intro z _; simp

/-- Adding any integer offset to a product forced to zero by root-of-unity triviality leaves the offset unchanged. -/
theorem framing_trivial_add_eq_self {f c d : ℤ}
    (h : ∀ z : ℂ, IsRootOfUnity z → z ^ (f * c) = 1) : f * c + d = d := by
  rw [framing_trivial_of_gate_on_rootsOfUnity h, zero_add]

end QOU.BraidKnot.Keystone
