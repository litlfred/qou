import Mathlib.Algebra.Module.Submodule.Lattice
import Mathlib.Algebra.Module.LinearMap.Defs
import QOU.BraidKnot.CentreGradingObstruction

/-!
# QOU.BraidKnot.GSFiltrationUnitObstruction — the unit coefficient closes the front

Bean `qou-09e0`, continuing `qou-wjbd` / `wpdb`. Six sites read

    Z^(k)(A) = span{ e_λ : gbDepth λ = k }

off `prop:curvature-rank-gb-stratification`, which stratifies **words**.
[`CentreGradingObstruction`](CentreGradingObstruction.lean) excluded all three
corpus readings of `J^•` and, via `shift_cannot_fill_a_gap`, every re-indexing
of the surviving Coxeter one. It left the front here:

> Any candidate must either fail to be an algebra filtration, or place a
> **second central element in `F_1`** — and Lemma 2 shows the Coxeter one
> cannot.

This file answers that, in the negative, for a class of filtrations named
precisely enough to be checked: **no filtration that either places the unit in
degree `0`, or is monomial in the Gröbner–Shirshov normal-form basis, induces
the `gbDepth` grading on the centre — at any `n ≥ 4`, under any shift.**

## Why the element-level statement is so much more rigid than the dimension one

The previous pass compared the two sides as **multiplicity functions** `ℕ → ℕ`
and had to work to exclude a shift, because a dimension sequence carries little
information. But the corpus statement is an equality of **spans of named
elements**, and that pins two things a dimension count cannot see:

1. `1 = Σ_λ e_λ` has **every** idempotent coordinate nonzero, so
   `1 ∈ span{e_λ : gbDepth λ ≤ j}` forces `j ≥ max gbDepth`. The unit is not
   somewhere in the filtration; it is at the very **top** of it
   (`all_strata_below_of_unit_mem`).
2. `τ(e_λ) ≠ 0` for every `λ`, where `τ` is the canonical symmetrizing trace
   (the `T_e` coefficient). So **`T_e` lies in the support of every central
   primitive idempotent** — and a monomial filtration cannot admit any `e_λ`
   without admitting `T_e = 1` along with it.

Put together: the unit is forced to the top of the filtration by (1) and forced
to the bottom by (2), and the two meet only when `gbDepth` is **constant**.

## The one algebra input, and where it is measured

`τ(e_λ) ≠ 0` enters as the hypothesis `hτ`. It is standard —
`τ(e_λ) = d_λ / c_λ` with `c_λ` the Schur element, nonzero at generic `q` — but
it is load-bearing for a scope-(b) exclusion, so it is **measured** in
[`docs/audits/scripts/central_idempotent_unit_coefficient.py`](../../../../../docs/audits/scripts/central_idempotent_unit_coefficient.py):
exactly, `n = 2 … 5`, two independent backends (`Fraction` over `ℚ`, and `𝔽_p`
with `p = 2⁶¹ − 1`) at several specialisations of `q`, with no floating point
anywhere. It is measured as a **rank** — in the idempotent basis the form
`(x, y) ↦ τ(xy)` restricted to `Z` is `diag(τ(e_λ))`, so non-degeneracy *is* the
claim — which sidesteps splitting `Z` into idempotents. The specialisation
direction is the safe one: `rank B(q₀) ≤ rank B(q)` generically, and the probe
reports **full** rank.

## What is and is not claimed

**Not claimed:** that the identification is false in the abstract. As
`CentreGradingObstruction` records, a filtration inducing the `gbDepth` grading
exists trivially — filter by the Wedderburn blocks, `F_k := ⊕_{gbDepth λ ≤ k}
R·e_λ`. That one satisfies every hypothesis below **except** `hmono` (it is not
monomial: its pieces are spanned by idempotents, not by normal forms) and
except `hunit0` (its unit sits in degree `n`, not `0`). So the two hypotheses
are exactly what separates the excluded class from the realisable one, and
neither is idle.

**Not claimed:** that any mass or binding number is wrong. `J^•` enters the
downstream chain as an **indexing** — which body order an `a_D^{(n)}` belongs
to — not as a magnitude. Nothing here touches the Wedderburn decomposition, the
Markov trace, `tr_M`, `y_λ`, the idempotents themselves, or `gbDepth` as a
definition.

**Scope (b) — structural exclusion**, with the invariant cited: *the unit's
idempotent coordinates are all nonzero, and `τ` does not vanish on any central
primitive idempotent*. The first is `hu` (immediate from `1 = Σ_λ e_λ`), the
second is `hτ` (measured above).
-/

namespace QOU.BraidKnot

section Abstract

variable {R A : Type*} [CommRing R] [Nontrivial R] [AddCommGroup A] [Module R A]

/-! ### 1. The unit sits at the TOP of any idempotent-graded filtration

`V j` below is the corpus's `span{e_λ : gbDepth λ ≤ j}`, presented by its
**coordinate** description: a central element lies in it exactly when all its
idempotent coordinates in strata above `j` vanish. `π l` is the coordinate
functional of `e l`.
-/

/-- **If the unit lies in stratum `j`, then every stratum is at or below `j`.**

`1 = Σ_λ e_λ` has *every* coordinate equal to `1`, so it cannot be missing any
idempotent — and `V j` is precisely the span of those with `deg ≤ j`. This is
the half that pushes the unit to the top of the filtration.

Note it uses `Nontrivial R` essentially: over the zero ring `1 = 0` and the
statement is false. -/
theorem all_strata_below_of_unit_mem
    {Λ : Type*} (deg : Λ → ℕ) (π : Λ → (A →ₗ[R] R)) (u : A)
    (Z : Submodule R A) (V : ℕ → Submodule R A)
    (hV : ∀ (j : ℕ) (x : A), x ∈ V j ↔ (x ∈ Z ∧ ∀ l : Λ, j < deg l → π l x = 0))
    (hu : ∀ l : Λ, π l u = 1)
    {j : ℕ} (hj : u ∈ V j) : ∀ l : Λ, deg l ≤ j := by
  intro l
  by_contra hcon
  have h0 : π l u = 0 := ((hV j u).1 hj).2 l (by omega)
  rw [hu l] at h0
  exact one_ne_zero h0

/-! ### 2. A filtration with the unit in degree `0` forces the grading to be constant -/

/-- **If the unit is in filtration degree `0`, the partition grading is
constant.**

Immediate from §1: `1 ∈ Z ⊓ F 0 = V c` puts every stratum at or below `c`,
while `hbot` (which is `Z ⊓ F_{-1} = 0`, i.e. the filtration starts at `0`)
puts every stratum at or above `c`.

This covers, in one stroke, **every** reading of `J^•` in which the empty word
has depth `0` — which is all three of them, and is what "definable from the
rewriting data" means in practice. It needs no monomiality at all, so it also
excludes non-monomial candidates such as the Jucys–Murphy content filtration
`Z_{≤d} = span of symmetric functions in the `L_i` of degree ≤ d`, whose degree-
`0` piece is `R·1`. -/
theorem unit_in_degree_zero_forces_constant_grading
    {Λ : Type*} (deg : Λ → ℕ) (π : Λ → (A →ₗ[R] R)) (u : A)
    (Z : Submodule R A) (F V : ℕ → Submodule R A) (c : ℕ)
    (hV : ∀ (j : ℕ) (x : A), x ∈ V j ↔ (x ∈ Z ∧ ∀ l : Λ, j < deg l → π l x = 0))
    (hu : ∀ l : Λ, π l u = 1) (huZ : u ∈ Z)
    (hid : ∀ k : ℕ, Z ⊓ F k = V (k + c))
    (hbot : ∀ l : Λ, c ≤ deg l)
    (hunit0 : u ∈ F 0) :
    ∀ l l' : Λ, deg l = deg l' := by
  have hmem : u ∈ V (0 + c) := by
    rw [← hid 0]; exact Submodule.mem_inf.2 ⟨huZ, hunit0⟩
  have hle := all_strata_below_of_unit_mem deg π u Z V hV hu hmem
  intro l l'
  have h1 := hle l
  have h2 := hle l'
  have h3 := hbot l
  have h4 := hbot l'
  omega

/-! ### 3. A monomial filtration forces the grading to be constant

`hmono` is the whole of "definable from the Gröbner–Shirshov data": if
`F k = span{T_w : w ∈ S k}` for a set of normal forms `S k`, then either
`e ∈ S k` — in which case `T_e = 1 ∈ F k` — or every element of `F k` has zero
`T_e`-coefficient, i.e. `τ` vanishes on `F k`. Stated contrapositively, that is
exactly `hmono`. A filtration whose pieces are *not* spanned by normal forms —
the Wedderburn-block filtration — does not satisfy it, which is why this
theorem does not contradict its existence.
-/

/-- **Every stratum lies at or below `deg l₀`, for each `l₀`** — the engine of
the monomial case.

The idempotent `e l₀` lives in its own stratum, hence in `F (deg l₀ - c)`. It
has nonzero trace, so monomiality drags the **unit** into that same piece; and
§1 then puts the whole grading below `deg l₀`. -/
theorem strata_below_of_monomial
    {Λ : Type*} [DecidableEq Λ] (deg : Λ → ℕ) (π : Λ → (A →ₗ[R] R)) (e : Λ → A)
    (u : A) (τ : A →ₗ[R] R)
    (Z : Submodule R A) (F V : ℕ → Submodule R A) (c : ℕ)
    (hV : ∀ (j : ℕ) (x : A), x ∈ V j ↔ (x ∈ Z ∧ ∀ l : Λ, j < deg l → π l x = 0))
    (hu : ∀ l : Λ, π l u = 1) (huZ : u ∈ Z)
    (heZ : ∀ l : Λ, e l ∈ Z)
    (hπe : ∀ l l' : Λ, π l' (e l) = if l' = l then (1 : R) else 0)
    (hτ : ∀ l : Λ, τ (e l) ≠ 0)
    (hmono : ∀ (k : ℕ) (x : A), x ∈ F k → τ x ≠ 0 → u ∈ F k)
    (hid : ∀ k : ℕ, Z ⊓ F k = V (k + c))
    (hbot : ∀ l : Λ, c ≤ deg l)
    (l₀ : Λ) : ∀ l : Λ, deg l ≤ deg l₀ := by
  -- `e l₀` lies in its own stratum `V (deg l₀)`.
  have hstep : deg l₀ - c + c = deg l₀ := Nat.sub_add_cancel (hbot l₀)
  have hein : e l₀ ∈ V (deg l₀ - c + c) := by
    rw [hstep]
    refine (hV (deg l₀) (e l₀)).2 ⟨heZ l₀, ?_⟩
    intro l' hlt
    rw [hπe l₀ l']
    have : l' ≠ l₀ := by rintro rfl; omega
    simp [this]
  -- hence in `F (deg l₀ - c)`; its trace is nonzero, so the unit is there too.
  have heF : e l₀ ∈ F (deg l₀ - c) := (Submodule.mem_inf.1 (by rw [hid]; exact hein)).2
  have huF : u ∈ F (deg l₀ - c) := hmono _ _ heF (hτ l₀)
  have humem : u ∈ V (deg l₀ - c + c) := by
    rw [← hid]; exact Submodule.mem_inf.2 ⟨huZ, huF⟩
  rw [hstep] at humem
  exact all_strata_below_of_unit_mem deg π u Z V hV hu humem

/-- **A filtration monomial in the Gröbner–Shirshov normal-form basis forces the
partition grading to be constant.**

Antisymmetry of `strata_below_of_monomial` applied at both indices. -/
theorem monomial_filtration_forces_constant_grading
    {Λ : Type*} [DecidableEq Λ] (deg : Λ → ℕ) (π : Λ → (A →ₗ[R] R)) (e : Λ → A)
    (u : A) (τ : A →ₗ[R] R)
    (Z : Submodule R A) (F V : ℕ → Submodule R A) (c : ℕ)
    (hV : ∀ (j : ℕ) (x : A), x ∈ V j ↔ (x ∈ Z ∧ ∀ l : Λ, j < deg l → π l x = 0))
    (hu : ∀ l : Λ, π l u = 1) (huZ : u ∈ Z)
    (heZ : ∀ l : Λ, e l ∈ Z)
    (hπe : ∀ l l' : Λ, π l' (e l) = if l' = l then (1 : R) else 0)
    (hτ : ∀ l : Λ, τ (e l) ≠ 0)
    (hmono : ∀ (k : ℕ) (x : A), x ∈ F k → τ x ≠ 0 → u ∈ F k)
    (hid : ∀ k : ℕ, Z ⊓ F k = V (k + c))
    (hbot : ∀ l : Λ, c ≤ deg l) :
    ∀ l l' : Λ, deg l = deg l' := by
  intro l l'
  have h1 := strata_below_of_monomial deg π e u τ Z F V c hV hu huZ heZ hπe hτ hmono hid hbot l' l
  have h2 := strata_below_of_monomial deg π e u τ Z F V c hV hu huZ heZ hπe hτ hmono hid hbot l l'
  omega

end Abstract

/-! ### 4. Instantiated at `n = 4`, where the partition grading first separates

`gbDepth_ne_on_H4` (`[2,2] ↦ 3`, `[4] ↦ 4`) is exactly the failure of
constancy, so both theorems above become refutations there — and `n = 4` is the
smallest `n` at which they can be, since `gbDepth_const_on_H3` says the grading
*is* constant at `n = 3`. That boundary is not a coincidence: `n ≤ 3` is
precisely where the excluded class is realisable, by the trivial filtration.
-/

section AtFour

variable {R A : Type*} [CommRing R] [Nontrivial R] [AddCommGroup A] [Module R A]

/-- **No filtration placing the unit in degree `0` induces the `gbDepth` grading
on `Z(H₄(q))`.**

`a` and `b` are the index-set elements carrying the two partitions of `4` whose
depths differ; everything else is the §2 hypothesis set. -/
theorem unit_degree_zero_filtration_excluded_at_four
    {Λ : Type*} (deg : Λ → ℕ) (π : Λ → (A →ₗ[R] R)) (u : A)
    (Z : Submodule R A) (F V : ℕ → Submodule R A) (c : ℕ) (a b : Λ)
    (ha : deg a = gbDepth p22) (hb : deg b = gbDepth p4)
    (hV : ∀ (j : ℕ) (x : A), x ∈ V j ↔ (x ∈ Z ∧ ∀ l : Λ, j < deg l → π l x = 0))
    (hu : ∀ l : Λ, π l u = 1) (huZ : u ∈ Z)
    (hid : ∀ k : ℕ, Z ⊓ F k = V (k + c))
    (hbot : ∀ l : Λ, c ≤ deg l)
    (hunit0 : u ∈ F 0) : False := by
  have hconst :=
    unit_in_degree_zero_forces_constant_grading deg π u Z F V c hV hu huZ hid hbot hunit0 a b
  rw [ha, hb] at hconst
  exact gbDepth_ne_on_H4 hconst.symm

/-- **No filtration monomial in the Gröbner–Shirshov normal-form basis induces
the `gbDepth` grading on `Z(H₄(q))`.**

This is the answer to the question bean `qou-09e0` was opened on. The front was
*"find a filtration putting a second central element in `F_1`"*; the obstruction
is that a monomial filtration admitting **any** `e_λ` must admit `T_e = 1` too,
because `τ(e_λ) ≠ 0` — and then it must admit every other `e_μ` as well, so it
cannot separate the strata at all. There is no `F_1` with two central elements
and not all of them.

**Not vacuous.** Every hypothesis is separately satisfiable — the Wedderburn-
block filtration realises all of them but `hmono`, and the trivial filtration
`F k = ⊤` realises all of them (including `hmono`) at `n ≤ 3`, where `deg`
genuinely is constant. What is impossible is the conjunction *with* a
non-constant grading, which is what `gbDepth_ne_on_H4` supplies. Each of `hmono`,
`hτ`, `hu` and `hbot` is used in the proof term. -/
theorem monomial_filtration_excluded_at_four
    {Λ : Type*} [DecidableEq Λ] (deg : Λ → ℕ) (π : Λ → (A →ₗ[R] R)) (e : Λ → A)
    (u : A) (τ : A →ₗ[R] R)
    (Z : Submodule R A) (F V : ℕ → Submodule R A) (c : ℕ) (a b : Λ)
    (ha : deg a = gbDepth p22) (hb : deg b = gbDepth p4)
    (hV : ∀ (j : ℕ) (x : A), x ∈ V j ↔ (x ∈ Z ∧ ∀ l : Λ, j < deg l → π l x = 0))
    (hu : ∀ l : Λ, π l u = 1) (huZ : u ∈ Z)
    (heZ : ∀ l : Λ, e l ∈ Z)
    (hπe : ∀ l l' : Λ, π l' (e l) = if l' = l then (1 : R) else 0)
    (hτ : ∀ l : Λ, τ (e l) ≠ 0)
    (hmono : ∀ (k : ℕ) (x : A), x ∈ F k → τ x ≠ 0 → u ∈ F k)
    (hid : ∀ k : ℕ, Z ⊓ F k = V (k + c))
    (hbot : ∀ l : Λ, c ≤ deg l) : False := by
  have hconst :=
    monomial_filtration_forces_constant_grading deg π e u τ Z F V c
      hV hu huZ heZ hπe hτ hmono hid hbot a b
  rw [ha, hb] at hconst
  exact gbDepth_ne_on_H4 hconst.symm

end AtFour

/-! ### 5. The hypothesis set is SATISFIABLE — these are implications, not `False → _`

A refutation is only worth the paper it is on if its hypotheses can be met. The
witness below discharges **every** hypothesis of §3 simultaneously, over `ℤ`
with a one-element index set: the trivial filtration `F k = ⊤` on a one-block
"centre", where `deg` is (vacuously) constant.

Together with the delete-a-binder check — each of `hV`, `hu`, `huZ`, `heZ`,
`hπe`, `hτ`, `hmono`, `hid`, `hbot`, `hunit0` is used in the proof term, so
removing any one of them stops the file compiling — this pins the content of §4
exactly: the hypotheses are jointly satisfiable, each is necessary, and what is
impossible is their conjunction **with a non-constant grading**. That last
ingredient is `gbDepth_ne_on_H4`, and it is the whole of what `n ≥ 4` buys.

It also says something about the mathematics rather than the bookkeeping. The
model that satisfies everything is the degenerate one — one stratum — which is
the `n ≤ 3` situation `gbDepth_const_on_H3` describes. The excluded class is
realisable exactly where the partition grading has nothing to say. -/

section NonVacuity

/-- **Every §3 hypothesis, discharged simultaneously.** So
`monomial_filtration_forces_constant_grading` is a genuine implication: its
antecedent has a model, and the model's grading is constant, as the theorem
predicts. -/
theorem monomial_hypotheses_satisfiable :
    ∃ (deg : Unit → ℕ) (π : Unit → (ℤ →ₗ[ℤ] ℤ)) (e : Unit → ℤ) (u : ℤ) (τ : ℤ →ₗ[ℤ] ℤ)
      (Z : Submodule ℤ ℤ) (F V : ℕ → Submodule ℤ ℤ) (c : ℕ),
      (∀ (j : ℕ) (x : ℤ), x ∈ V j ↔ (x ∈ Z ∧ ∀ l : Unit, j < deg l → π l x = 0))
      ∧ (∀ l : Unit, π l u = 1)
      ∧ u ∈ Z
      ∧ (∀ l : Unit, e l ∈ Z)
      ∧ (∀ l l' : Unit, π l' (e l) = if l' = l then (1 : ℤ) else 0)
      ∧ (∀ l : Unit, τ (e l) ≠ 0)
      ∧ (∀ (k : ℕ) (x : ℤ), x ∈ F k → τ x ≠ 0 → u ∈ F k)
      ∧ (∀ k : ℕ, Z ⊓ F k = V (k + c))
      ∧ (∀ l : Unit, c ≤ deg l)
      ∧ (1 : ℤ) ∈ (⊤ : Submodule ℤ ℤ) := by
  refine ⟨fun _ => 0, fun _ => LinearMap.id, fun _ => 1, 1, LinearMap.id,
    ⊤, fun _ => ⊤, fun _ => ⊤, 0, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
    simp

end NonVacuity

/-! ### 6. An independent route: the anti-diagonal "Poincaré duality of strata"

`rem:quantum-dilogarithm-stratified-partial-argument` Step 1 states, of the centre,

    ⟨Z^(k)(A), Z^(ℓ)(A)⟩ = 0   whenever k + ℓ ≠ N,

and calls the residual `Z^(k) × Z^(N-k) → R` the *Poincaré duality of
curvature-rank strata*. It cites `prf:spectral-sequence-collapse`
§"Frobenius duality of strata" — which states an **annihilator** duality
`(J^ℓ)^⊥ = J^{N-ℓ}` for the ideal filtration of the **whole algebra** `A`. That
is a reasonable thing to say about a Frobenius algebra. What is not reasonable
is transporting it to the centre's *idempotent* strata, and this section is why.

On `Z`, the pairing is `⟨a, b⟩ = φ(ab)` for the Frobenius integral `φ`, and
distinct central primitive idempotents **annihilate each other**: `e_λ e_μ = 0`
for `λ ≠ μ`. So the pairing matrix in the idempotent basis is `diag(φ(e_λ))` —
**diagonal**, not anti-diagonal. A stratum therefore pairs with *itself*, and
the anti-diagonal law can only hold if every occupied depth satisfies `2k = N`,
i.e. if there is a single stratum.

So this site's Step 1 collapses to the same conclusion as §2–§3 — the grading
must be constant — by a completely **independent** route: it uses no filtration
of words at all, only the multiplication table of the idempotents and the same
measured `φ(e_λ) ≠ 0`. It is worth recording separately because it means the
site is not repaired by fixing the word/partition bridge: its own Step 1 is
already inconsistent with a non-constant grading.

**Scope (b) — structural exclusion.** Invariant cited: *distinct central
primitive idempotents multiply to zero, and the Frobenius integral does not
vanish on any of them.* The first is the definition of a Wedderburn
decomposition; the second is the measured fact above — and is in any case
**implied by the same block's own assertion** that the pairing restricts to `Z`
non-degenerately. -/

section AntiDiagonal

/-! `φ` lands in any type with a zero: the pairing argument needs nothing else
of the coefficients, so `[Zero R]` is the whole requirement. -/

variable {R : Type*} [Zero R]

/-- **An anti-diagonal pairing law on idempotent strata forces the grading to
be constant.**

`hanti` is the block's own displayed hypothesis, restricted to the spanning
idempotents (so it is *weaker* than what the block asserts, which makes the
refutation stronger). `hidem` and `hφ` are the two structural inputs.

The argument is three lines: were some `l` to have `2 · deg l ≠ N`, `hanti`
would give `φ(e_l · e_l) = 0`, i.e. `φ(e_l) = 0` by idempotency, contradicting
`hφ`. So every degree is `N / 2`, hence all equal.

`φ` is taken as a bare function, not a linear map: linearity is never used, and
the weaker hypothesis makes the theorem stronger. -/
theorem antidiagonal_pairing_forces_constant_grading
    {A : Type*} [Ring A] {Λ : Type*} (deg : Λ → ℕ) (e : Λ → A) (φ : A → R) (N : ℕ)
    (hidem : ∀ l : Λ, e l * e l = e l)
    (hφ : ∀ l : Λ, φ (e l) ≠ 0)
    (hanti : ∀ l l' : Λ, deg l + deg l' ≠ N → φ (e l * e l') = 0) :
    ∀ l l' : Λ, deg l = deg l' := by
  have h : ∀ l : Λ, 2 * deg l = N := by
    intro l
    by_contra hc
    exact hφ l (by rw [← hidem l]; exact hanti l l (by omega))
  intro l l'
  have h1 := h l
  have h2 := h l'
  omega

/-- **The anti-diagonal strata pairing is unavailable at `n = 4`.**

Instantiating §6 against `gbDepth_ne_on_H4`. This refutes
`rem:quantum-dilogarithm-stratified-partial-argument` Step 1 **without using the word filtration
at all** — so, unlike the six sites' shared defect, it is not repaired by
supplying the missing word/partition bridge. -/
theorem antidiagonal_pairing_excluded_at_four
    {A : Type*} [Ring A] {Λ : Type*} (deg : Λ → ℕ) (e : Λ → A) (φ : A → R) (N : ℕ)
    (a b : Λ) (ha : deg a = gbDepth p22) (hb : deg b = gbDepth p4)
    (hidem : ∀ l : Λ, e l * e l = e l)
    (hφ : ∀ l : Λ, φ (e l) ≠ 0)
    (hanti : ∀ l l' : Λ, deg l + deg l' ≠ N → φ (e l * e l') = 0) : False := by
  have hconst := antidiagonal_pairing_forces_constant_grading deg e φ N hidem hφ hanti a b
  rw [ha, hb] at hconst
  exact gbDepth_ne_on_H4 hconst.symm

end AntiDiagonal

end QOU.BraidKnot
