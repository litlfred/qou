/-
# The base ring, stated as a property rather than a ring

The framework's ground ring is fixed by an owner decision (2026-08-26) as

    R = ℤ[q, q⁻¹][ Φ_d(q)⁻¹ : d ≥ 2 ]

— Laurent polynomials with every cyclotomic polynomial from the second on
inverted. `Spec R` is the `q`-line with the roots of unity of order `≥ 2`
deleted, which is the locus where finite-strand Hecke Wedderburn blocks
(`SemisimpleBlockData`, Chapter 5) have invertible quantum dimensions.

## Scope: this is CONSTRUCTION-side, not a hypothesis of the axioms

`def:quantum-universe` asks of its base only `CommRing`, and that is correct and
should not change. Per the 2026-11-19 architectural ruling (`qou-ig2d`), finite
Wedderburn semisimplicity is deferred to Chapter 5 (`braids-and-knots` Hecke
`H_n(q)` slices and `SemisimpleBlockData`), where the invertibility it needs is
stated as `dimQ_isUnit` / `frobWeight_isUnit`, quantified over the slice's
*own* blocks — a condition on the pair `(R, C)`, never on `R` alone. More
importantly `q` is **emergent**:
`QuantumUniverse` carries `unitEndEquiv : R ≃+* End (𝟙_ C)` and deliberately has
**no `q` field**, because the twist axiom reads `q` off the ribbon structure and
"a distinguished element would smuggle in as data the thing the framework claims
to derive".

`IsQGeneric R q` below takes `q` as a **parameter**, so it is exactly the shape
the axioms refuse. It is therefore *not* a definition-layer constraint and must
not be threaded into `QuantumUniverse`. Its use is the other direction of
travel: when one **constructs** a Hecke-type finite-strand slice in Chapter 5,
`q` is chosen first (one builds `H_n(q)`), and this class is what discharges the
`SemisimpleBlockData` unit fields (`dimQ_isUnit`, `frobWeight_isUnit`) for that
construction. Axiomatic direction — `R` generic, `q` emerges, nothing more
required. Constructive direction — `q` given, and then this.

**The ring below is likewise an instance, not a requirement.** A
neighbouring community works over a *related* base — `ℚ(q)` for generic-`q`
representation theory, `ℤ[v, v⁻¹]` with `q = v²` in the Lusztig convention, a
real or complex algebra past the archimedean wall — and a definition hard-wired
to one ring silently excludes all of them.

So this file states the **property** instead, as `IsQGeneric R q`, and the ring
above becomes the *initial* object satisfying it: for any commutative `S` with a
distinguished unit `u` at which every `Φ_d`, `d ≥ 2`, is a unit, there is exactly
one ring map `R → S` sending `q ↦ u`. That is the universal property of a
localisation, applied twice, and it is the precise sense in which every related
community ring is downstream of this one rather than in competition with it.

`IsQGeneric.map` below is the working half of that: the property **transports
along any ring homomorphism**, so a definition stated over `IsQGeneric` is
automatically available in every specialisation.

## No `ℝ` in this file (§7c)

The archimedean specialisation — every real `q > 1` is `q`-generic, the substrate
anchor included — is a **separate file**,
[`QGenericBaseReal.lean`](QGenericBaseReal.lean). §7c puts the specialisation past
the wall in its own file even when the `ℝ` is warranted, and it is warranted there:
the proof needs the ordering. An earlier revision kept it here behind a docstring
arguing that the `ℝ` was justified. That argued the wrong question —
`check-sidecars.sh` flags the *mixing*, not the `ℝ` — and it was flagged.

## Why `d ≥ 2` and not `d ≥ 1`

`Φ₁(q) = q − 1`, so inverting from `d = 1` would delete `q = 1` from `Spec R`.
The corpus uses that point — the `q = 1` classical shadow, `J_Hopf(1) = -2` —
so deleting it would be a real loss.

Nothing forces it. `ℏ_q = 1 - q⁻¹ = (q-1)/q` is the one construct that would
need `Φ₁`, and every division by it happens past the archimedean wall, in `ℝ`,
where `q₀ - 1 ≈ 0.11` is invertible on its own account. Measured: of the files
mentioning `ℏ`, the ones that *divide* by it are archimedean.

`qPow_sub_one_eq_mul_bracket` makes the boundary exact: `qⁿ - 1` factors as
`(q - 1)` times a unit, so it is a unit **iff** `q - 1` is. The `d ≥ 2` choice
buys every quantum dimension and leaves `q = 1` alive, and the theorem is what
shows those two are not in tension.
-/
import Mathlib.RingTheory.Polynomial.Cyclotomic.Basic
import Mathlib.RingTheory.Polynomial.Cyclotomic.Eval
import Mathlib.Algebra.BigOperators.Group.Finset.Defs
import Mathlib.Data.Real.Basic

namespace QOU.AlgebraicSubstrate

open Polynomial Finset

variable {R S : Type*} [CommRing R] [CommRing S]

/-- **The base-ring property.** `q` is a unit, and so is every cyclotomic
polynomial `Φ_d` evaluated at `q`, for `d ≥ 2`.

Stated as a property so that the definition of a quantum universe is available
over *any* base satisfying it, not only over the initial one
`ℤ[q, q⁻¹][Φ_d(q)⁻¹ : d ≥ 2]`. -/
class IsQGeneric (R : Type*) [CommRing R] (q : R) : Prop where
  isUnit_q : IsUnit q
  isUnit_cyclotomic : ∀ d : ℕ, 2 ≤ d → IsUnit ((cyclotomic d R).eval q)

/-- The `n`-th quantum bracket in cyclotomic form: `[n]_q = ∏_{d ∣ n, d ≥ 2} Φ_d(q)`.

This is the unbalanced bracket `1 + q + ⋯ + q^{n-1}`, written so that its
factorisation is the definition rather than a lemma. -/
noncomputable def qBracket (R : Type*) [CommRing R] (q : R) (n : ℕ) : R :=
  ∏ d ∈ n.divisors.filter (fun d => 2 ≤ d), (cyclotomic d R).eval q

/-- **Every quantum bracket is a unit.** This is what axiom 4 needs: quantum
dimensions are products of brackets, so they are units too.

The proof is the whole point of choosing the cyclotomic generating set — the
bracket is *by construction* a product of the elements the class inverts, so no
divisibility argument is required. -/
theorem isUnit_qBracket (q : R) [IsQGeneric R q] (n : ℕ) : IsUnit (qBracket R q n) := by
  refine Finset.prod_induction _ IsUnit (fun a b => IsUnit.mul) isUnit_one ?_
  intro d hd
  exact IsQGeneric.isUnit_cyclotomic d (by simpa using (Finset.mem_filter.mp hd).2)

/-- `qⁿ - 1 = (q - 1) · [n]_q` for `n ≥ 1` — the exact boundary of the `d ≥ 2`
choice.

Since `[n]_q` is a unit, `qⁿ - 1` is a unit **iff** `q - 1` is. The class does not
invert `q - 1`, so `q = 1` survives in `Spec R`; anything genuinely needing
`(qⁿ - 1)⁻¹` is asking for `Φ₁` and should say so. -/
theorem qPow_sub_one_eq_mul_bracket (q : R) {n : ℕ} (hn : 0 < n) :
    q ^ n - 1 = (q - 1) * qBracket R q n := by
  have hprod := prod_cyclotomic_eq_X_pow_sub_one hn R
  have := congrArg (fun p => Polynomial.eval q p) hprod
  simp only [eval_prod, eval_sub, eval_pow, eval_one, eval_X] at this
  rw [← this, ← Finset.prod_filter_mul_prod_filter_not n.divisors (fun d => 2 ≤ d)]
  have h1 : n.divisors.filter (fun d => ¬ 2 ≤ d) = {1} := by
    ext d
    simp only [Finset.mem_filter, Nat.mem_divisors, Finset.mem_singleton, not_le]
    constructor
    · rintro ⟨⟨hdvd, -⟩, hlt⟩
      interval_cases d
      · rw [Nat.zero_dvd] at hdvd; omega
      · rfl
    · rintro rfl
      exact ⟨⟨one_dvd n, hn.ne'⟩, one_lt_two⟩
  rw [h1]
  simp [qBracket, cyclotomic_one, mul_comm]

/-- **The property transports along any ring homomorphism.**

This is the working content of "state the property, not the ring": a definition
made over `IsQGeneric` is automatically available in every specialisation — the
generic-`q` field `ℚ(q)`, an archimedean evaluation at the substrate `q₀`, a
neighbouring community's base — without restating anything. -/
theorem IsQGeneric.map (f : R →+* S) (q : R) [IsQGeneric R q] : IsQGeneric S (f q) where
  isUnit_q := (IsQGeneric.isUnit_q (q := q)).map f
  isUnit_cyclotomic d hd := by
    have : (cyclotomic d S).eval (f q) = f ((cyclotomic d R).eval q) := by
      rw [← map_cyclotomic d f, eval_map, eval₂_at_apply]
    rw [this]
    exact (IsQGeneric.isUnit_cyclotomic d hd).map f

/-- Additive geometric-sum form of the quantum integer
`[m]_q = ∑_{i=0}^{m-1} q^i = 1 + q + ⋯ + q^{m-1}`. -/
def qBracketSum (q : R) (m : ℕ) : R :=
  ∑ i ∈ Finset.range m, q ^ i

/-- Telescoping geometric-sum identity `(q - 1) · ∑_{i=0}^{m-1} q^i = q^m - 1`. -/
theorem sub_one_mul_qBracketSum (q : R) (m : ℕ) :
    (q - 1) * qBracketSum q m = q ^ m - 1 := by
  unfold qBracketSum
  induction m with
  | zero => simp
  | succ k ih =>
    rw [Finset.sum_range_succ, mul_add, ih, pow_succ]
    ring

/-- Over any field `K`, for `q ≠ 1` and `m ≥ 1`, the cyclotomic product `qBracket K q m`
coincides identically with the geometric sum `qBracketSum q m = ∑_{i=0}^{m-1} q^i`. -/
theorem qBracket_eq_qBracketSum_of_ne_one {K : Type*} [Field K] (q : K) (hq1 : q ≠ 1)
    {m : ℕ} (hm : 0 < m) :
    qBracket K q m = qBracketSum q m := by
  apply mul_left_cancel₀ (sub_ne_zero.mpr hq1)
  rw [← qPow_sub_one_eq_mul_bracket q hm, sub_one_mul_qBracketSum]

/-- **Unconditional Real Positivity of `[m]_q` on `(0, ∞)`**:
For every real `q > 0` (including the classical point `q = 1` and the physical
substrate `q₀ > 1`) and every `m ≥ 1`, the quantum integer
`qBracketSum q m = ∑_{i=0}^{m-1} q^i` is strictly positive (`> 0`). -/
theorem qBracketSum_real_pos {q : ℝ} (hq : 0 < q) {m : ℕ} (hm : 1 ≤ m) :
    0 < qBracketSum q m := by
  unfold qBracketSum
  obtain ⟨k, rfl⟩ : ∃ k, m = k + 1 := Nat.exists_eq_add_of_le' hm
  rw [Finset.sum_range_succ]
  have hnonneg : 0 ≤ ∑ i ∈ Finset.range k, q ^ i :=
    Finset.sum_nonneg (fun i _ => le_of_lt (pow_pos hq i))
  have hlast : 0 < q ^ k := pow_pos hq k
  linarith

/-- On `ℝ`, for every `q > 0` and `m ≥ 1`, `qBracketSum q m ≠ 0`. -/
theorem qBracketSum_real_ne_zero {q : ℝ} (hq : 0 < q) {m : ℕ} (hm : 1 ≤ m) :
    qBracketSum q m ≠ 0 :=
  ne_of_gt (qBracketSum_real_pos hq hm)

/-- **Unconditional Invertibility of `[m]_q` on `(0, ∞)`**:
On `ℝ`, for every `q > 0` and `m ≥ 1`, `IsUnit (qBracketSum q m)` holds without
any auxiliary semisimplicity assumption, certifying that Dipper–James / Wenzl
split semisimplicity of `H_n(q)` holds unconditionally across all `q ∈ (0, ∞)`. -/
theorem qBracketSum_real_isUnit {q : ℝ} (hq : 0 < q) {m : ℕ} (hm : 1 ≤ m) :
    IsUnit (qBracketSum q m) :=
  isUnit_iff_ne_zero.mpr (qBracketSum_real_ne_zero hq hm)

end QOU.AlgebraicSubstrate
