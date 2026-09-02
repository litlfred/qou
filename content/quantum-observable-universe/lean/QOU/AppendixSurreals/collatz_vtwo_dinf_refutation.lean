import Mathlib.Tactic
import QOU.MathlibExt.LaurentTwoValuation

/-!
# `v_[2]` is not a descent measure on `D∞` (bean `qou-4atn`, settled negative)

`reaches_cycle_of_descent_domainStable` reduces `q`-Collatz convergence on the
domain-stable cone to the existence of a measure `μ : Skein → ℕ` with

    ∀ P, domainStable P → P ≠ attractor → μ (C P) < μ P.

The natural candidate is the `[2]_q`-adic valuation `v_[2]`. Two landed results
bracketed it without settling it:

* `collatz_vtwo_obstruction.qcollatz_vTwo_increases_on_odd_branch` — `v_[2]`
  increases on the witness `-X-2`;
* `collatz_vtwo_domain_rescope.qcollatz_vTwo_witness_escapes_domain` — but that
  witness **escapes the domain**, so it says nothing about `D∞`.

The positive datum was `collatz_vtwo_cycle_descent`: `v_[2]` does drop `1 → 0` on
the even step of the fundamental cycle. Bean `qou-4atn` recorded the question as
re-opened.

**This file settles it: `v_[2]` does not descend on `D∞`.** The reason is
structural rather than a lucky witness, and that is what makes it useful.

## The obstruction

`μ` takes values in `ℕ`. So `μ (C P) < μ P` is *impossible* wherever `μ P = 0` —
nothing in `ℕ` lies below `0`. Hence any working descent measure must be
**strictly positive at every non-attractor point of the cone**
(`descent_measure_pos_off_target`).

But `v_[2]` vanishes on every `q`-odd element: `q`-odd means `[2]_q ∣ P + 1`, and
if `[2]_q` also divided `P` it would divide `1` and be a unit, which it is not
(`T1_add_one_not_isUnit`). So `v_[2] P = 0` for every `q`-odd `P`
(`laurentTwoVal_qOdd`).

`D∞` contains `q`-odd elements other than the attractor. Therefore `v_[2]` fails.

## The witness, and how it was found

`witnessP = q⁻¹·(q⁶+7q⁵+20q⁴+29q³+21q²+6q+1)` is `q`-odd, lies in `D∞`, and its
Collatz image is `witnessCP = q⁻¹·(q+1)⁷` — so `v_[2]` goes `0 → 7` in one step.

It was produced by **construction, not search**
(`computations/qcollatz_vtwo_domain_stable_probe.py`): every backward orbit of
the attractor cycle lies in `D∞` by definition, because if `C^[n](P)` is the
cycle then every forward iterate of `P` is defined. The probe generates that
backward tree exactly — even-preimage `[2]_q·P`, odd-preimage `([2]_q P − 1)/[3]_q`
when exact — in exact `ℤ[q^{±1}]` arithmetic, and *also* verifies each node
forward by iterating to the cycle, so `D∞` membership is established twice.
`witnessP` reaches the cycle in 7 steps. The probe finds the same failure at
every odd-branch node it generates (3 of 3, at `v_[2]` jumps `0 → 7`, `0 → 13`,
`0 → 19`) — as the structural argument predicts, since *every* `q`-odd point sits
at valuation `0`.

## Scope — (a), and what it does *not* say

This is a **scope-(a) negative**: it refutes `v_[2]` as *the* descent measure, and
says nothing about whether some *other* measure descends on `D∞`. It is not a
structural exclusion of the descent route.

What it does buy going forward is a genuine **necessary condition** on any
candidate `μ`: by `descent_measure_pos_off_target`, `μ` must be strictly positive
at every non-attractor point of `D∞`. Since `D∞` contains `q`-odd points, any
valuation-like candidate that vanishes on the `q`-odd part is excluded for the
same reason — so the next candidate must not be one.

Base ring: the obstruction is over an arbitrary type; the witness identity is over
a generic `[CommRing R]` with `q` a unit (§7c); only the valuation statement needs
the Laurent ring.
-/

namespace QOU.AppendixSurreals.CollatzVTwoDinfRefutation

open LaurentPolynomial QOU.MathlibExt.LaurentTwoValuation

/-! ## Part 1 — the general obstruction

Stated for an arbitrary `f`, `target`, cone `S` and measure `μ`, matching the
hypothesis shape of `reaches_of_descent_of_forward` exactly, so it applies
verbatim to `reaches_cycle_of_descent_domainStable`. -/

/-- **Any `ℕ`-valued descent measure is strictly positive off the target.**
    Immediate, and the whole content of the refutation: `μ (f x) < μ x` cannot
    hold when `μ x = 0`, because `ℕ` has nothing below `0`. -/
theorem descent_measure_pos_off_target {α : Type*} (f : α → α) (target : α)
    (S : α → Prop) (μ : α → ℕ)
    (hdesc : ∀ x, S x → x ≠ target → μ (f x) < μ x) :
    ∀ x, S x → x ≠ target → 0 < μ x := by
  intro x hx hne
  have h := hdesc x hx hne
  omega

/-- **Contrapositive — a measure that vanishes anywhere off the target cannot be
    a descent measure.** This is the form used to refute a candidate. -/
theorem not_descent_of_vanishes_off_target {α : Type*} (f : α → α) (target : α)
    (S : α → Prop) (μ : α → ℕ) (x₀ : α)
    (hS : S x₀) (hne : x₀ ≠ target) (hzero : μ x₀ = 0) :
    ¬ (∀ x, S x → x ≠ target → μ (f x) < μ x) := by
  intro hdesc
  have h := descent_measure_pos_off_target f target S μ hdesc x₀ hS hne
  omega

/-! ## Part 2 — `v_[2]` vanishes on every `q`-odd element -/

/-- **A `q`-odd element is not divisible by `[2]_q`.** If `[2]_q` divided both `P`
    and `P + 1` it would divide `1`, making it a unit — which it is not. -/
theorem qOdd_not_dvd {P : LaurentPolynomial ℤ}
    (h : (T 1 + 1 : LaurentPolynomial ℤ) ∣ (P + 1)) :
    ¬ (T 1 + 1 : LaurentPolynomial ℤ) ∣ P := by
  intro hP
  have hone : (T 1 + 1 : LaurentPolynomial ℤ) ∣ 1 := by
    have := dvd_sub h hP
    simpa using this
  exact T1_add_one_not_isUnit (isUnit_of_dvd_one hone)

/-- **`v_[2]` vanishes on every `q`-odd element.** -/
theorem laurentTwoVal_qOdd {P : LaurentPolynomial ℤ}
    (h : (T 1 + 1 : LaurentPolynomial ℤ) ∣ (P + 1)) :
    laurentTwoVal P = 0 := by
  unfold laurentTwoVal
  have h0 : emultiplicity (T 1 + 1 : LaurentPolynomial ℤ) P = ((0 : ℕ) : ℕ∞) :=
    emultiplicity_eq_of_dvd_of_not_dvd (by rw [pow_zero]; exact one_dvd _)
      (by rw [pow_one]; exact qOdd_not_dvd h)
  exact_mod_cast h0

/-! ## Part 3 — the concrete `D∞` witness

Stated first over a generic `[CommRing R]` with `q` a unit, matching the style of
`qcollatz_fundamental_odd_step`, then instantiated at `ℤ[q^{±1}]`. -/

/-- **The witness Collatz step, generically.** With `X = q`, `Y = q⁻¹`,

      P  = Y·(X⁶+7X⁵+20X⁴+29X³+21X²+6X+1),   C(P) = Y·(X+1)⁷,

    the odd branch `[3]_q·P + 1 = [2]_q·C(P)` holds. (Cleared of `Y` this is the
    integer identity `(X²+X+1)·A + X = (X+1)⁸`.) -/
theorem witness_odd_step {R : Type*} [CommRing R] (X Y : R) (hq : X * Y = 1) :
    (X ^ 2 + X + 1) *
        (Y * (X ^ 6 + 7 * X ^ 5 + 20 * X ^ 4 + 29 * X ^ 3 + 21 * X ^ 2 + 6 * X + 1))
        + 1
      = (X + 1) * (Y * (X + 1) ^ 7) := by
  linear_combination (-1 : R) * hq

/-- **The witness is `q`-odd, generically**: `P + 1 = [2]_q · (Y·B)` with
    `B = X⁵+6X⁴+14X³+15X²+6X+1`. -/
theorem witness_qOdd {R : Type*} [CommRing R] (X Y : R) (hq : X * Y = 1) :
    Y * (X ^ 6 + 7 * X ^ 5 + 20 * X ^ 4 + 29 * X ^ 3 + 21 * X ^ 2 + 6 * X + 1) + 1
      = (X + 1) * (Y * (X ^ 5 + 6 * X ^ 4 + 14 * X ^ 3 + 15 * X ^ 2 + 6 * X + 1)) := by
  linear_combination (-1 : R) * hq

/-- `q` is a unit in `ℤ[q^{±1}]`, with inverse `q⁻¹`. -/
theorem qunit : (T 1 : LaurentPolynomial ℤ) * T (-1) = 1 := by
  rw [← T_add]; simp [T_zero]

/-- The witness `P = q⁻¹·(q⁶+7q⁵+20q⁴+29q³+21q²+6q+1)`, an element of `D∞`
    verified in `computations/qcollatz_vtwo_domain_stable_probe.py` (it reaches
    the attractor cycle in 7 steps). -/
noncomputable def witnessP : LaurentPolynomial ℤ :=
  T (-1) * ((T 1) ^ 6 + 7 * (T 1) ^ 5 + 20 * (T 1) ^ 4 + 29 * (T 1) ^ 3
    + 21 * (T 1) ^ 2 + 6 * (T 1) + 1)

/-- Its Collatz image `C(P) = q⁻¹·(q+1)⁷`. -/
noncomputable def witnessCP : LaurentPolynomial ℤ :=
  T (-1) * (T 1 + 1) ^ 7

/-- The odd branch takes `witnessP` to `witnessCP`. -/
theorem witnessP_step :
    ((T 1 : LaurentPolynomial ℤ) ^ 2 + T 1 + 1) * witnessP + 1
      = (T 1 + 1) * witnessCP :=
  witness_odd_step (T 1) (T (-1)) qunit

/-- `witnessP` is `q`-odd. -/
theorem witnessP_qOdd :
    (T 1 + 1 : LaurentPolynomial ℤ) ∣ (witnessP + 1) :=
  ⟨T (-1) * ((T 1) ^ 5 + 6 * (T 1) ^ 4 + 14 * (T 1) ^ 3 + 15 * (T 1) ^ 2
      + 6 * (T 1) + 1),
   witness_qOdd (T 1) (T (-1)) qunit⟩

/-- **`v_[2](witnessP) = 0`.** -/
theorem laurentTwoVal_witnessP : laurentTwoVal witnessP = 0 :=
  laurentTwoVal_qOdd witnessP_qOdd

/-- **`v_[2](C(witnessP)) ≥ 7`** — exhibited by `C(P) = q⁻¹·(q+1)⁷`. So the step
    does not merely fail to descend, it climbs by seven. -/
theorem witnessCP_pow_dvd :
    (T 1 + 1 : LaurentPolynomial ℤ) ^ 7 ∣ witnessCP :=
  ⟨T (-1), by rw [witnessCP]; ring⟩

/-! ## Part 4 — the refutation -/

/-- **`v_[2]` is not a descent measure on any cone containing `witnessP`.**

    In particular it is not one on `D∞`, which does contain `witnessP` (verified
    both by construction as a backward orbit of the attractor and forward by
    iteration). Instantiating `f` at the Skein-Collatz map, `target` at the
    attractor and `S` at `domainStable` refutes exactly the `hdesc` hypothesis of
    `reaches_cycle_of_descent_domainStable` for `μ = v_[2]`.

    **Scope (a).** This excludes `v_[2]`, not the descent route: some other `μ`
    may still work. What survives as forward guidance is
    `descent_measure_pos_off_target` — any candidate must be strictly positive at
    every non-attractor point of the cone. -/
theorem vTwo_not_descent_measure
    (f : LaurentPolynomial ℤ → LaurentPolynomial ℤ)
    (target : LaurentPolynomial ℤ) (S : LaurentPolynomial ℤ → Prop)
    (hS : S witnessP) (hne : witnessP ≠ target) :
    ¬ (∀ x, S x → x ≠ target →
        (laurentTwoVal (f x)).toNat < (laurentTwoVal x).toNat) :=
  not_descent_of_vanishes_off_target f target S
    (fun P => (laurentTwoVal P).toNat) witnessP hS hne
    (by show (laurentTwoVal witnessP).toNat = 0
        rw [laurentTwoVal_witnessP]
        rfl)

end QOU.AppendixSurreals.CollatzVTwoDinfRefutation
