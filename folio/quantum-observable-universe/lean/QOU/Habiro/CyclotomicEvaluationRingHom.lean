import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.RingTheory.Ideal.Quotient.Operations
import QOU.Habiro.CyclotomicEvaluation

/-!
# The Habiro cyclotomic evaluation **is** a ring homomorphism — and it exists only
# at roots of unity

This file settles one question, and it is the question on which PR #7216's
class-D exclusion turns.

## Why this is the hinge

`qou-brng` class D (PR #7216) excludes the fibre-level tower as an *independent*
escape from the pair-additive bond-count caps. Its lead invariant is
`bondSum_map`: a bond count is a polynomial with integer coefficients in its
energies and counts, so it commutes with **every ring homomorphism**; the
rendering of a fibre-level bond count is therefore itself a bond count, and every
cap applies to it. That exclusion carries exactly one undischarged hypothesis,
named in the PR body:

> *that the rendering is a ring homomorphism* — evaluation of an analytic
> function at `q₀` is; evaluation of a general Habiro element at a
> non-root-of-unity point is not defined at all (bean `qou-ix0x`, item 4). Where
> the rendering is not a ring map, `bondSum_map` says nothing, **and that is the
> one genuinely open door class D still has.**

Bean `qou-ix0x` proposes the Habiro/cyclotomic summation on the other side of
precisely that door, on the ground that cyclotomic summation converges at every
root of unity rather than along a ray. So the two fronts meet at one decidable
question.

## What is proved here, and what it costs class D

**A dichotomy, both halves formal.** Write `ev_ζ` for the rendering of a
cyclotomic series `Σ_m a_m (q;q)_m` at `ζ`.

* **At a root of unity, `ev_ζ` IS a ring homomorphism.**
  `cyclotomicEvalHom` is `Polynomial.evalRingHom ζ`; `qPochPoly_mem_ker` shows it
  kills `(q;q)_N`; `cyclotomicQuotientEval` is the induced **`→+*`** out of the
  level-`N` truncation `R[q]/((q;q)_N)` — which is exactly the object the Habiro
  ring is the inverse limit of. So `bondSum_map` applies verbatim to the
  cyclotomic rendering, and class D's exclusion **extends through it**.
* **Off the roots of unity there is no rendering at all to be, or fail to be, a
  ring map.** Over a domain, `exists_pow_eq_one_of_qPochDiag_eq_zero` shows the
  truncation `(ζ;ζ)_N = 0` that makes `habiroEval` independent of its level
  *forces* `ζ^k = 1` for some `1 ≤ k ≤ N`. Contrapositively
  (`habiroEval_one_ne_succ_of_not_root`), at a non-root-of-unity `ζ` the
  all-ones series has `ev_ζ` at level `N+1` differing from level `N` **for every
  `N`** — the truncations never stabilise, so there is no value to render.

So both branches of the door are shut: on one the exclusion transports, on the
other there is nothing to transport.

## The corpus caveat this corrects, and the sense in which it was right

`QOU.Habiro.CyclotomicEvaluation`'s docstring says:

> **Multiplicativity is NOT proved here.** The Habiro product in cyclotomic
> coordinates is not termwise, so `ev_ζ` being a *ring* hom is a larger build. …
> **Do not cite it as a ring hom.**

That is correct **about the coordinates** and wrong if read as a statement about
the map. `habiroEval a ζ N` is the coordinate map `a ↦ value`, and it is indeed
only additive: the `(q;q)_m` do not multiply termwise, so there is no
coefficientwise product on sequences. The *map on the ring* is a different
object, and `habiroEval_eq_cyclotomicEvalHom` factors the coordinate map through
it: `habiroEval a ζ N = ev_ζ (habiroPoly a N)`. `habiroEval_mul_of_repr` then
restates multiplicativity in coordinates with the Habiro product supplied as a
hypothesis (`hc`, which is its definition — the product taken in
`R[q]/((q;q)_N)`), rather than assumed as a conclusion.

The caveat should therefore be read as *"the cyclotomic coordinates are not a
multiplicative basis"*, which is true and is Habiro's own point, not as *"`ev_ζ`
is not a ring map"*, which is false.

## Scope — AGENTS.md §"Before declaring refuted"

**Scope (b) for the evaluation-shaped renderings**, on a proved structural
invariant (a ring hom's compatibility with a polynomial, plus
`Finset.prod_eq_zero_iff` in a domain) rather than any numerical estimate.

**It does NOT exclude every fibre-level rendering.** Explicitly untouched:

* a rendering that is not an evaluation — a pairing, a state integral, or a
  coefficient extraction. Coefficient extraction is genuinely *not* a ring hom
  (linear, not multiplicative); that channel is covered separately by #7216's
  second invariant `bondSum_tower`, not by anything here;
* an evaluation into a ring where `(ζ;ζ)_N` is a zero divisor without `ζ` being a
  root of unity — the dichotomy above assumes `IsDomain`;
* anything about *magnitudes*. Nothing here computes `b₃`, and per bean
  `qou-ix0x` ROAST-1 this is a statement about where an object can live, not a
  derivation of one.

**Nothing is fitted.** No root of unity, truncation order or completion is
selected here at all; `ζ` and `N` are arbitrary throughout.

**Base ring (§7c).** Generic `[CommRing R]`, with `[IsDomain R]` only where the
prime-factorisation step needs it. No ordering, no `ℝ`, no analysis.

**There is no archimedean instance at the substrate pin, and §4 is the reason.**
An earlier draft of this docstring said one lived in
`QOU.Habiro.CyclotomicEvaluationAtSubstrate`. **No such declaration exists** —
zero hits corpus-wide — and the omission is not an oversight to be filled later:
the substrate pin `q₀ ≈ 1.11` is not a root of unity, so
`habiroEval_one_ne_succ_of_not_root` says the truncations never stabilise there
and there is no value to instantiate. A file of that name would have to
contradict §4 of this one.

Ref: [habiro2004] https://doi.org/10.2140/gt.2004.8.1127
Ref: [leitner2026] conj:binding-manybody-eq-jet-filtration
-/

open Finset Polynomial

namespace QOU.Habiro

open QOU.Common

variable {R : Type*} [CommRing R]

/-! ## 1. The cyclotomic coordinates as polynomials -/

/-- The diagonal `q`-Pochhammer `(q;q)_m = ∏_{k=1}^{m} (1 - q^k)` as a **polynomial**.
    `qPochDiag` is its evaluation; keeping the polynomial is what lets the whole
    construction be read through `Polynomial.evalRingHom`. -/
noncomputable def qPochPoly (R : Type*) [CommRing R] (m : ℕ) : Polynomial R :=
  ∏ k ∈ Finset.range m, (1 - X ^ (k + 1))

@[simp] theorem eval_qPochPoly (ζ : R) (m : ℕ) :
    (qPochPoly R m).eval ζ = qPochDiag ζ m := by
  unfold qPochPoly qPochDiag
  rw [Polynomial.eval_prod]
  exact Finset.prod_congr rfl (fun k _ => by simp)

/-- A cyclotomic series truncated at level `N`, as a polynomial. -/
noncomputable def habiroPoly (a : ℕ → R) (N : ℕ) : Polynomial R :=
  ∑ m ∈ Finset.range N, C (a m) * qPochPoly R m

/-- **The coordinate map factors through polynomial evaluation.** -/
theorem eval_habiroPoly (a : ℕ → R) (ζ : R) (N : ℕ) :
    (habiroPoly a N).eval ζ = habiroEval a ζ N := by
  unfold habiroPoly habiroEval
  rw [Polynomial.eval_finset_sum]
  exact Finset.sum_congr rfl (fun m _ => by simp)

/-! ## 2. The evaluation as a ring homomorphism -/

/-- Evaluation at `ζ`, **as a ring homomorphism** on `R[q]`. This is nothing but
    `Polynomial.evalRingHom`; it is named here so the class-D hypothesis can be
    discharged by pointing at an object of type `→+*`. -/
noncomputable def cyclotomicEvalHom (ζ : R) : Polynomial R →+* R :=
  Polynomial.evalRingHom ζ

@[simp] theorem cyclotomicEvalHom_apply (ζ : R) (p : Polynomial R) :
    cyclotomicEvalHom ζ p = p.eval ζ := rfl

/-- **The Habiro coordinate map is a ring hom applied to a polynomial.**
    This is the precise sense in which `ev_ζ` is a ring map: the non-multiplicativity
    of the cyclotomic *coordinates* is a fact about the presentation, and the
    presentation is not the map. -/
theorem habiroEval_eq_cyclotomicEvalHom (a : ℕ → R) (ζ : R) (N : ℕ) :
    habiroEval a ζ N = cyclotomicEvalHom ζ (habiroPoly a N) := by
  rw [cyclotomicEvalHom_apply, eval_habiroPoly]

theorem eval_qPochPoly_eq_zero_of_pow_eq_one (ζ : R) {N : ℕ} (hN : 0 < N)
    (hζ : ζ ^ N = 1) : (qPochPoly R N).eval ζ = 0 := by
  rw [eval_qPochPoly]
  exact qPochDiag_eq_zero_of_pow_eq_one ζ hN hζ

/-- At a root of unity the evaluation kills the level-`N` Pochhammer. -/
theorem qPochPoly_mem_ker (ζ : R) {N : ℕ} (hN : 0 < N) (hζ : ζ ^ N = 1) :
    qPochPoly R N ∈ RingHom.ker (cyclotomicEvalHom ζ) := by
  rw [RingHom.mem_ker, cyclotomicEvalHom_apply]
  exact eval_qPochPoly_eq_zero_of_pow_eq_one ζ hN hζ

theorem span_qPochPoly_le_ker (ζ : R) {N : ℕ} (hN : 0 < N) (hζ : ζ ^ N = 1) :
    Ideal.span ({qPochPoly R N} : Set (Polynomial R)) ≤ RingHom.ker (cyclotomicEvalHom ζ) := by
  rw [Ideal.span_le, Set.singleton_subset_iff]
  exact qPochPoly_mem_ker ζ hN hζ

/-- **THE STATEMENT CLASS D NEEDS.** At a root of unity, evaluation descends to the
    level-`N` truncation `R[q]/((q;q)_N)` **as a ring homomorphism** — and that
    truncation is exactly the object the Habiro ring `Ẑ[q] = lim_← R[q]/((q;q)_N)`
    is the inverse limit of.

    So a rendering of a Habiro element at a root of unity is a ring map, and every
    invariant of the form "this quantity commutes with ring homomorphisms"
    — `bondSum_map` in particular — transports through it unchanged. -/
noncomputable def cyclotomicQuotientEval (ζ : R) {N : ℕ} (hN : 0 < N) (hζ : ζ ^ N = 1) :
    (Polynomial R ⧸ Ideal.span ({qPochPoly R N} : Set (Polynomial R))) →+* R :=
  Ideal.Quotient.lift _ (cyclotomicEvalHom ζ) (fun _ hx => span_qPochPoly_le_ker ζ hN hζ hx)

@[simp] theorem cyclotomicQuotientEval_mk (ζ : R) {N : ℕ} (hN : 0 < N) (hζ : ζ ^ N = 1)
    (p : Polynomial R) :
    cyclotomicQuotientEval ζ hN hζ (Ideal.Quotient.mk _ p) = p.eval ζ :=
  Ideal.Quotient.lift_mk _ _ _

/-- The Habiro value at a root of unity, read off the quotient. -/
theorem habiroEval_eq_quotientEval (a : ℕ → R) (ζ : R) {N : ℕ} (hN : 0 < N)
    (hζ : ζ ^ N = 1) :
    habiroEval a ζ N
      = cyclotomicQuotientEval ζ hN hζ (Ideal.Quotient.mk _ (habiroPoly a N)) := by
  rw [cyclotomicQuotientEval_mk, eval_habiroPoly]

/-! ## 3. Multiplicativity in coordinates — the corpus caveat, restated correctly

`CyclotomicEvaluation` proves `habiroEval_add` and stops, noting the product is
not termwise. It is not, and it does not need to be: the Habiro product of two
series is *defined* as the product taken in `R[q]/((q;q)_N)`, and that is the
hypothesis `hc` below. With it supplied, multiplicativity is immediate — which
is the whole content of "the map is a ring hom, the coordinates are not a
multiplicative basis". -/

/-- **Multiplicativity of the cyclotomic evaluation**, with the Habiro product
    supplied as a hypothesis rather than assumed as a conclusion: `hc` says that
    `c` represents the product of `a` and `b` in `R[q]/((q;q)_N)`. -/
theorem habiroEval_mul_of_repr (a b c : ℕ → R) (ζ : R) {N : ℕ} (hN : 0 < N)
    (hζ : ζ ^ N = 1)
    (hc : qPochPoly R N ∣ (habiroPoly c N - habiroPoly a N * habiroPoly b N)) :
    habiroEval c ζ N = habiroEval a ζ N * habiroEval b ζ N := by
  obtain ⟨d, hd⟩ := hc
  have h := congrArg (fun p => Polynomial.eval ζ p) hd
  simp only [Polynomial.eval_sub, Polynomial.eval_mul, eval_qPochPoly] at h
  rw [qPochDiag_eq_zero_of_pow_eq_one ζ hN hζ, zero_mul, sub_eq_zero] at h
  rw [← eval_habiroPoly, ← eval_habiroPoly, ← eval_habiroPoly, h]

/-- **Anti-vacuity for `habiroEval_mul_of_repr`.** The hypothesis `hc` is
    satisfiable: at level `1` the cyclotomic coordinates are the constant term
    alone, and the representing sequence is the plain product. Without an instance
    the theorem above would be a statement about an empty hypothesis class. -/
theorem habiroPoly_one_mul (a b : ℕ → R) :
    habiroPoly (fun m => if m = 0 then a 0 * b 0 else 0) 1
      = habiroPoly a 1 * habiroPoly b 1 := by
  unfold habiroPoly qPochPoly
  simp [Polynomial.C_mul]

/-! ## 4. The other half of the dichotomy: no rendering off the roots of unity -/

/-- Over a domain, the truncation that makes `habiroEval` level-independent can only
    happen at a root of unity: `(ζ;ζ)_N = 0` forces `ζ^k = 1` for some `1 ≤ k ≤ N`. -/
theorem exists_pow_eq_one_of_qPochDiag_eq_zero [IsDomain R] (ζ : R) {N : ℕ}
    (h : qPochDiag ζ N = 0) : ∃ k, 0 < k ∧ k ≤ N ∧ ζ ^ k = 1 := by
  unfold qPochDiag at h
  obtain ⟨k, hk, hk0⟩ := Finset.prod_eq_zero_iff.mp h
  rw [Finset.mem_range] at hk
  refine ⟨k + 1, by omega, by omega, ?_⟩
  have : ζ ^ (k + 1) = 1 := by linear_combination -hk0
  exact this

/-- Contrapositive: at a non-root-of-unity `ζ` no level ever truncates. -/
theorem qPochDiag_ne_zero_of_not_root [IsDomain R] (ζ : R)
    (h : ∀ k, 0 < k → ζ ^ k ≠ 1) (N : ℕ) : qPochDiag ζ N ≠ 0 := by
  intro hz
  obtain ⟨k, hk, _, hk1⟩ := exists_pow_eq_one_of_qPochDiag_eq_zero ζ hz
  exact h k hk hk1

/-- Consecutive truncations of the all-ones cyclotomic series differ by exactly
    `(ζ;ζ)_N`. -/
theorem habiroEval_one_succ_sub (ζ : R) (N : ℕ) :
    habiroEval (fun _ => (1 : R)) ζ (N + 1) - habiroEval (fun _ => (1 : R)) ζ N
      = qPochDiag ζ N := by
  unfold habiroEval
  rw [Finset.sum_range_succ]
  simp

/-- **No stabilisation off the roots of unity — so there is nothing to render.**

    At a `ζ` that is not a root of unity, the all-ones cyclotomic series has a
    *different* value at every truncation level: level `N+1` differs from level `N`
    for every `N`. `habiroEval_stable` — the well-definedness that makes `ev_ζ` a
    map on the inverse limit at all — is therefore unavailable, and there is no
    value for class D to render, ring map or otherwise.

    This is bean `qou-ix0x` ROAST item 4 (*"the substrate `q₀ ≈ 1.11` is not a root
    of unity, so a cyclotomic route has to explain how root-of-unity data reaches an
    evaluation at a non-root-of-unity point"*) answered in the negative for
    evaluation-shaped renderings: it does not reach it by evaluating. -/
theorem habiroEval_one_ne_succ_of_not_root [IsDomain R] (ζ : R)
    (h : ∀ k, 0 < k → ζ ^ k ≠ 1) (N : ℕ) :
    habiroEval (fun _ => (1 : R)) ζ (N + 1) ≠ habiroEval (fun _ => (1 : R)) ζ N := by
  intro heq
  apply qPochDiag_ne_zero_of_not_root ζ h N
  rw [← habiroEval_one_succ_sub ζ N, heq, sub_self]

/-! ## 5. The transport itself

`bondSum_map` (PR #7216) is the statement that a bond count commutes with every
ring homomorphism. The instance that matters here is stated directly, so this
file does not depend on an unmerged branch: a bond count is an `ℕ`-weighted sum
of energies, and such a sum is carried by `cyclotomicEvalHom` because it is a
ring map. -/

/-- **A bond count transports through the cyclotomic evaluation.** An `ℕ`-weighted
    sum of fibre-level energies renders to the `ℕ`-weighted sum of their renderings
    — i.e. the rendering of a fibre-level bond count *is* a bond count, with the
    same counts. Every cap proved for bond counts therefore applies to it. -/
theorem map_bondCount {ι : Type*} (s : Finset ι) (e : ι → Polynomial R) (n : ι → ℕ)
    (ζ : R) :
    cyclotomicEvalHom ζ (∑ i ∈ s, (n i : Polynomial R) * e i)
      = ∑ i ∈ s, (n i : R) * cyclotomicEvalHom ζ (e i) := by
  rw [map_sum]
  exact Finset.sum_congr rfl (fun i _ => by rw [map_mul, map_natCast])

/-- The same statement one level up, on the level-`N` truncation of the Habiro ring:
    the rendering of a bond count whose energies are Habiro elements is a bond
    count over `R`. -/
theorem quotientEval_bondCount {ι : Type*} (s : Finset ι)
    (ζ : R) {N : ℕ} (hN : 0 < N) (hζ : ζ ^ N = 1)
    (e : ι → (Polynomial R ⧸ Ideal.span ({qPochPoly R N} : Set (Polynomial R))))
    (n : ι → ℕ) :
    cyclotomicQuotientEval ζ hN hζ (∑ i ∈ s, (n i : _) * e i)
      = ∑ i ∈ s, (n i : R) * cyclotomicQuotientEval ζ hN hζ (e i) := by
  rw [map_sum]
  exact Finset.sum_congr rfl (fun i _ => by rw [map_mul, map_natCast])

end QOU.Habiro
