import Mathlib.RingTheory.Polynomial.Cyclotomic.Basic
import Mathlib.RingTheory.Ideal.Quotient.Operations
import Mathlib.Algebra.Ring.Subring.Basic
import QOU.BraidKnot.ResidueAtRoot

/-!
# QOU.BraidKnot.QHabiroCompletion — the q-Habiro completion as a thread ring

This file constructs, over `ℤ`, the Habiro completion

  `ℤ̂[q] = varprojlim_N ℤ[q] ⧸ ((q; q)_N)`

as a concrete `CommRing`: the subring of **compatible threads** in the product
`Π N, ℤ[X] ⧸ ((q;q)_N)`, where `(q;q)_N = ∏_{k=1}^N (1 - q^k)` is the
q-Pochhammer symbol (written `qPoch N`, with the polynomial variable `X`
standing for `q`). It then builds the cyclotomic projections
`ℤ̂[q] → ℤ[q] ⧸ (Φ_n(q))` and packages them as an instance of the existing
class `QOU.BraidKnot.ResidueAtRoot`. Style follows `ZHabiroCompletion` in
`QOU/MassEndomorphism/ZHabiroCauchy.lean`.

## What is proved (all sorry-free, no new axioms)

* `qPoch_dvd_succ`, `qPoch_dvd_of_le` — `(q;q)_N ∣ (q;q)_M` for `N ≤ M`;
  hence the ideals `((q;q)_N)` form a descending chain (`qPochIdeal_le`).
* `Habiro` — the subring of threads `x` with
  `factor_{M→N} (x M) = x N` for **every** `N ≤ M` (not only `M = N+1`);
  closure under `0, 1, +, *, −` is proved field by field.
* `cyclotomic_dvd_qPoch` — `Φ_n ∣ (q;q)_n` for `n ≠ 0` (because
  `Φ_n ∣ q^n − 1` and `1 − q^n` is a factor of `(q;q)_n`).
* `project n hn : Habiro →+* ℤ[X] ⧸ (Φ_n)` — read the thread at level `n`, then
  reduce along `((q;q)_n) ≤ (Φ_n)`.
* `ofPoly : ℤ[X] →+* Habiro` (constant threads), and the non-vacuity check
  `project_ofPoly : project n hn (ofPoly p) = mk (Φ_n) p` — on polynomials the
  projection is the ordinary reduction mod `Φ_n`. Consequently `project n hn`
  is surjective (`project_surjective`).
* `instance : ResidueAtRoot Habiro` with the **index shift** convention
  `target n := ℤ[X] ⧸ (Φ_{n+1})`, `project n := project (n+1) _`. The class
  quantifies over all `n : ℕ`, while `Φ_0 = 1` would give the zero ring; the
  shift makes index `n` mean the primitive `(n+1)`-th root of unity, so index
  `0` is `q = 1` (`Φ_1 = q − 1`). This is a convention, recorded here so that
  no consumer reads index `n` as `ζ_n`.

## What is NOT proved here

* Nothing here shows that any **specific** element — in particular no
  Markov-trace value such as `Φ_q · tr_{M,ℓ}`, no Jones / colored-Jones
  evaluation, no quantum-dilogarithm series — lies in `Habiro` (beyond the
  images of honest polynomials under `ofPoly`). Membership of any such
  element is a separate claim and remains open as far as this file is
  concerned.
* No injectivity statement is proved: neither that `ofPoly` is injective nor
  Habiro's theorem that the joint cyclotomic evaluation map on `ℤ̂[q]` is
  injective.
* The instance discharges `ResidueAtRoot` for this concrete ring only; it does
  not by itself establish the downstream content of
  `conj:gs-residue-at-root-existence` for any other carrier `R`.

-- Ref: [habiro2004cyclotomic]
-/

namespace QOU.BraidKnot.QHabiro

open Polynomial

/-- The q-Pochhammer symbol `(q; q)_N = ∏_{k=1}^{N} (1 - q^k)` in `ℤ[q]`
    (polynomial variable `X` for `q`). `qPoch 0 = 1`. -/
noncomputable def qPoch (N : ℕ) : ℤ[X] :=
  ∏ k ∈ Finset.range N, (1 - X ^ (k + 1))

@[simp] theorem qPoch_zero : qPoch 0 = 1 := by
  simp [qPoch]

theorem qPoch_succ (N : ℕ) : qPoch (N + 1) = qPoch N * (1 - X ^ (N + 1)) := by
  simp [qPoch, Finset.prod_range_succ]

/-- `(q;q)_N ∣ (q;q)_{N+1}`. -/
theorem qPoch_dvd_succ (N : ℕ) : qPoch N ∣ qPoch (N + 1) := by
  rw [qPoch_succ]
  exact dvd_mul_right _ _

/-- Monotone divisibility: `(q;q)_N ∣ (q;q)_M` whenever `N ≤ M`. -/
theorem qPoch_dvd_of_le {N M : ℕ} (h : N ≤ M) : qPoch N ∣ qPoch M :=
  Finset.prod_dvd_prod_of_subset _ _ _ (Finset.range_subset_range.mpr h)

/-- The level-`N` ideal `((q;q)_N) ⊆ ℤ[q]`. -/
noncomputable abbrev qPochIdeal (N : ℕ) : Ideal ℤ[X] :=
  Ideal.span {qPoch N}

/-- The ideals descend: `((q;q)_M) ≤ ((q;q)_N)` for `N ≤ M`. -/
theorem qPochIdeal_le {N M : ℕ} (h : N ≤ M) : qPochIdeal M ≤ qPochIdeal N :=
  Ideal.span_singleton_le_span_singleton.mpr (qPoch_dvd_of_le h)

/-- The bonding map `ℤ[q]/((q;q)_M) → ℤ[q]/((q;q)_N)` for `N ≤ M`. -/
noncomputable abbrev bond {N M : ℕ} (h : N ≤ M) :
    ℤ[X] ⧸ qPochIdeal M →+* ℤ[X] ⧸ qPochIdeal N :=
  Ideal.Quotient.factor (qPochIdeal_le h)

/-- **The Habiro completion** `ℤ̂[q] = varprojlim_N ℤ[q]/((q;q)_N)`, realised as
    the subring of compatible threads in `Π N, ℤ[q]/((q;q)_N)`: `x` is a thread
    iff `bond h (x M) = x N` for every `N ≤ M`. Closure under the ring
    operations holds because each `bond h` is a ring homomorphism. -/
-- Ref: [habiro2004cyclotomic]
noncomputable def Habiro : Subring (∀ N, ℤ[X] ⧸ qPochIdeal N) where
  carrier := { x | ∀ N M (h : N ≤ M), bond h (x M) = x N }
  mul_mem' {x y} hx hy N M h := by
    simp only [Pi.mul_apply, map_mul, hx N M h, hy N M h]
  one_mem' N M h := by
    simp only [Pi.one_apply, map_one]
  add_mem' {x y} hx hy N M h := by
    simp only [Pi.add_apply, map_add, hx N M h, hy N M h]
  zero_mem' N M h := by
    simp only [Pi.zero_apply, map_zero]
  neg_mem' {x} hx N M h := by
    simp only [Pi.neg_apply, map_neg, hx N M h]

/-- Membership in `Habiro` is exactly thread-compatibility. -/
theorem mem_Habiro (x : ∀ N, ℤ[X] ⧸ qPochIdeal N) :
    x ∈ Habiro ↔ ∀ N M (h : N ≤ M), bond h (x M) = x N :=
  Iff.rfl

/-- `Φ_n ∣ (q;q)_n` for `n ≠ 0`: `Φ_n ∣ q^n − 1`, and `1 − q^n` is the
    `k = n − 1` factor of `(q;q)_n`. -/
theorem cyclotomic_dvd_qPoch {n : ℕ} (hn : n ≠ 0) :
    cyclotomic n ℤ ∣ qPoch n := by
  have h1 : cyclotomic n ℤ ∣ 1 - X ^ n := by
    have := cyclotomic.dvd_X_pow_sub_one n ℤ
    rw [← neg_sub]
    exact (dvd_neg).mpr this
  have hmem : n - 1 ∈ Finset.range n := Finset.mem_range.mpr (by omega)
  have h2 : (1 - X ^ (n - 1 + 1) : ℤ[X]) ∣ qPoch n :=
    Finset.dvd_prod_of_mem (fun k => (1 - X ^ (k + 1) : ℤ[X])) hmem
  rw [Nat.sub_add_cancel (Nat.one_le_iff_ne_zero.mpr hn)] at h2
  exact h1.trans h2

/-- `((q;q)_n) ≤ (Φ_n)` for `n ≠ 0`. -/
theorem qPochIdeal_le_cyclotomic {n : ℕ} (hn : n ≠ 0) :
    qPochIdeal n ≤ Ideal.span {cyclotomic n ℤ} :=
  Ideal.span_singleton_le_span_singleton.mpr (cyclotomic_dvd_qPoch hn)

/-- **The cyclotomic projection** `ℤ̂[q] → ℤ[q]/(Φ_n)` (`n ≠ 0`): evaluate the
    thread at level `n`, then reduce along `((q;q)_n) ≤ (Φ_n)`. -/
noncomputable def project (n : ℕ) (hn : n ≠ 0) :
    Habiro →+* ℤ[X] ⧸ Ideal.span {cyclotomic n ℤ} :=
  (Ideal.Quotient.factor (qPochIdeal_le_cyclotomic hn)).comp
    ((Pi.evalRingHom (fun N => ℤ[X] ⧸ qPochIdeal N) n).comp Habiro.subtype)

theorem project_apply (n : ℕ) (hn : n ≠ 0) (x : Habiro) :
    project n hn x =
      Ideal.Quotient.factor (qPochIdeal_le_cyclotomic hn) ((x : ∀ N, ℤ[X] ⧸ qPochIdeal N) n) :=
  rfl

/-- The constant threads: `p ↦ (N ↦ p mod (q;q)_N)`. -/
noncomputable def ofPoly : ℤ[X] →+* Habiro :=
  RingHom.codRestrict (Pi.ringHom fun N => Ideal.Quotient.mk (qPochIdeal N)) Habiro
    (fun p N M h => by
      simp only [Pi.ringHom_apply, bond, Ideal.Quotient.factor_mk])

@[simp] theorem ofPoly_apply (p : ℤ[X]) (N : ℕ) :
    ((ofPoly p : Habiro) : ∀ N, ℤ[X] ⧸ qPochIdeal N) N = Ideal.Quotient.mk (qPochIdeal N) p :=
  rfl

/-- **Non-vacuity.** On polynomials the cyclotomic projection is the ordinary
    reduction modulo `Φ_n`. -/
theorem project_ofPoly (n : ℕ) (hn : n ≠ 0) (p : ℤ[X]) :
    project n hn (ofPoly p) = Ideal.Quotient.mk (Ideal.span {cyclotomic n ℤ}) p := by
  rw [project_apply, ofPoly_apply, Ideal.Quotient.factor_mk]

/-- Each cyclotomic projection is surjective (already on constant threads). -/
theorem project_surjective (n : ℕ) (hn : n ≠ 0) : Function.Surjective (project n hn) := by
  intro y
  obtain ⟨p, rfl⟩ := Ideal.Quotient.mk_surjective y
  exact ⟨ofPoly p, project_ofPoly n hn p⟩

/-- **`ResidueAtRoot` instance for the Habiro completion.** Index convention:
    index `n` is the primitive `(n+1)`-th root of unity, i.e.
    `target n = ℤ[q]/(Φ_{n+1})` and `project n` is the level-`(n+1)` cyclotomic
    projection (this avoids `Φ_0 = 1`, which would give the zero ring). -/
noncomputable instance instResidueAtRoot : QOU.BraidKnot.ResidueAtRoot.{0} Habiro where
  target n := ℤ[X] ⧸ Ideal.span {cyclotomic (n + 1) ℤ}
  targetRing _ := inferInstance
  project n := project (n + 1) (Nat.succ_ne_zero n)

/-- The instance's residue on a polynomial is reduction mod `Φ_{n+1}`. -/
theorem residue_ofPoly (n : ℕ) (p : ℤ[X]) :
    QOU.BraidKnot.residue (R := Habiro) n (ofPoly p)
      = (Ideal.Quotient.mk (Ideal.span {cyclotomic (n + 1) ℤ}) p :
          ℤ[X] ⧸ Ideal.span {cyclotomic (n + 1) ℤ}) :=
  project_ofPoly (n + 1) (Nat.succ_ne_zero n) p

end QOU.BraidKnot.QHabiro
