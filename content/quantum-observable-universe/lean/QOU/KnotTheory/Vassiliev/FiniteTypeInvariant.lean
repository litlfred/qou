import QOU.KnotTheory.Vassiliev.WeightSystem
import Mathlib.Data.Finsupp.Basic
import Mathlib.Tactic

/-!
# Finite-type (Vassiliev) invariants

A knot invariant `v : K → R` extends to *singular* knots (immersions with
transverse double points) by the **Vassiliev skein relation**

`v(⨉) = v(over-crossing) − v(under-crossing)`,

resolving each double point into the signed difference of its two smoothings.
`v` has **order ≤ m** when this extension vanishes on every singular knot with
more than `m` double points.

This file formalizes the notion abstractly, over a `VassilievSetup`: the datum
of a type of `k`-fold singular objects together with their resolution into a
signed sum of knots and the one-double-point desingularization realizing the
skein relation.  We prove the genuinely definitional structural facts:

* `vExt` is `R`-linear in the invariant `v`;
* the extension of a `(k+1)`-singular object is the difference of the
  extensions of its two `k`-singular smoothings (`vExt_desingularize`);
* order-`≤ m` invariants form a submodule `finiteTypeSubmodule m` of `K → R`,
  and these are **filtered**: `finiteTypeSubmodule m ≤ finiteTypeSubmodule m'`
  for `m ≤ m'`.

The **symbol** of an order-`≤ m` invariant is its value on the `m`-singular
objects; the fundamental theorem that the symbol descends to a *weight system*
on chord diagrams (`WeightSystem.lean`), and Kontsevich's converse, are stated
as honest conjecture classes in `MilnorVassilievBridge.lean` — they are **not**
proved here and **not** axiomatized.

## References

* Bar-Natan, *On the Vassiliev knot invariants*, Topology 34 (1995) 423–472,
  <https://doi.org/10.1016/0040-9383(95)93237-2>.
* Vassiliev, *Cohomology of knot spaces*, in *Theory of Singularities and its
  Applications*, Adv. Soviet Math. 1 (1990) 23–69.
-/

namespace QOU.KnotTheory.Vassiliev

open scoped Classical
open Finsupp

universe u v

/-- Data presenting the singular-knot resolution underlying finite-type theory
for a type `K` of knots.

* `Sing k` — objects with exactly `k` transverse double points (`Sing 0 = K`
  morally).
* `resolve s` — the full resolution of every double point into a signed sum of
  honest knots (the Vassiliev skein, applied at all `k` double points).
* `desingularize s` — resolve *one* distinguished double point of a
  `(k+1)`-singular object into its positive and negative smoothings, each a
  `k`-singular object.
* `resolve_step` — the skein relation at the distinguished double point:
  `resolve s = resolve s₊ − resolve s₋`. -/
structure VassilievSetup (K : Type u) where
  /-- `k`-fold singular objects. -/
  Sing : ℕ → Type v
  /-- Full resolution into a signed formal sum of knots. -/
  resolve : ∀ {k : ℕ}, Sing k → (K →₀ ℤ)
  /-- Resolve one distinguished double point into `(positive, negative)`
  smoothings. -/
  desingularize : ∀ {k : ℕ}, Sing (k + 1) → Sing k × Sing k
  /-- The Vassiliev skein relation at the distinguished double point. -/
  resolve_step : ∀ {k : ℕ} (s : Sing (k + 1)),
    resolve s = resolve (desingularize s).1 - resolve (desingularize s).2

namespace VassilievSetup

variable {K : Type u} {R : Type*} [CommRing R] (S : VassilievSetup.{u, v} K)

/-- The extension of an invariant `v : K → R` to a `k`-singular object: apply
`v` `R`-linearly through the resolution. -/
noncomputable def vExt (v : K → R) {k : ℕ} (s : S.Sing k) : R :=
  (S.resolve s).sum (fun knot c => (c : R) * v knot)

/-- `vExt` is additive in the invariant. -/
theorem vExt_add (v w : K → R) {k : ℕ} (s : S.Sing k) :
    S.vExt (v + w) s = S.vExt v s + S.vExt w s := by
  simp only [vExt, Pi.add_apply, Finsupp.sum, mul_add, Finset.sum_add_distrib]

/-- `vExt` is homogeneous in the invariant. -/
theorem vExt_smul (r : R) (v : K → R) {k : ℕ} (s : S.Sing k) :
    S.vExt (r • v) s = r * S.vExt v s := by
  simp only [vExt, Pi.smul_apply, smul_eq_mul, Finsupp.sum, Finset.mul_sum]
  refine Finset.sum_congr rfl (fun knot _ => ?_)
  ring

/-- The zero invariant extends to zero. -/
@[simp] theorem vExt_zero {k : ℕ} (s : S.Sing k) :
    S.vExt (0 : K → R) s = 0 := by
  simp [vExt]

/-- The extension of a `(k+1)`-singular object is the difference of the
extensions of its two `k`-singular smoothings — the first-difference
(discrete-derivative) structure of the Vassiliev skein. -/
theorem vExt_desingularize (v : K → R) {k : ℕ} (s : S.Sing (k + 1)) :
    S.vExt v s
      = S.vExt v (S.desingularize s).1 - S.vExt v (S.desingularize s).2 := by
  unfold vExt
  rw [S.resolve_step s]
  rw [Finsupp.sum_sub_index]
  intro a b₁ b₂
  push_cast
  ring

/-! ## Order ≤ m and the Vassiliev filtration -/

/-- `v : K → R` is a **finite-type invariant of order ≤ m** when its extension
vanishes on every singular object with more than `m` double points. -/
def IsFiniteType (m : ℕ) (v : K → R) : Prop :=
  ∀ {k : ℕ}, m < k → ∀ s : S.Sing k, S.vExt v s = 0

variable {S}

/-- Order is monotone: an order-`≤ m` invariant is also order-`≤ m'` for
`m ≤ m'` (vanishing on `> m` double points implies vanishing on `> m'`). -/
theorem IsFiniteType.mono {m m' : ℕ} (hmm : m ≤ m') {v : K → R}
    (hv : S.IsFiniteType m v) : S.IsFiniteType m' v := by
  intro k hk s
  exact hv (lt_of_le_of_lt hmm hk) s

/-- The zero invariant has every finite order. -/
theorem isFiniteType_zero (m : ℕ) : S.IsFiniteType m (0 : K → R) := by
  intro k _ s; simp

/-- Finite-type invariants of order `≤ m` are closed under addition. -/
theorem IsFiniteType.add {m : ℕ} {v w : K → R} (hv : S.IsFiniteType m v)
    (hw : S.IsFiniteType m w) : S.IsFiniteType m (v + w) := by
  intro k hk s
  rw [S.vExt_add, hv hk s, hw hk s, add_zero]

/-- Finite-type invariants of order `≤ m` are closed under scalar
multiplication. -/
theorem IsFiniteType.smul {m : ℕ} (r : R) {v : K → R}
    (hv : S.IsFiniteType m v) : S.IsFiniteType m (r • v) := by
  intro k hk s
  rw [S.vExt_smul, hv hk s, mul_zero]

variable (S) in
/-- The submodule of order-`≤ m` finite-type invariants inside `K → R`. -/
noncomputable def finiteTypeSubmodule (m : ℕ) : Submodule R (K → R) where
  carrier := {v | S.IsFiniteType m v}
  add_mem' hv hw := hv.add hw
  zero_mem' := isFiniteType_zero m
  smul_mem' r _ hv := hv.smul r

@[simp] theorem mem_finiteTypeSubmodule {m : ℕ} {v : K → R} :
    v ∈ S.finiteTypeSubmodule (R := R) m ↔ S.IsFiniteType m v := Iff.rfl

/-- **The Vassiliev filtration.** The order-`≤ m` invariants are nested. -/
theorem finiteTypeSubmodule_mono {m m' : ℕ} (hmm : m ≤ m') :
    S.finiteTypeSubmodule (R := R) m ≤ S.finiteTypeSubmodule (R := R) m' := by
  intro v hv
  exact IsFiniteType.mono hmm hv

/-! ## The symbol map (degree-`m` part)

The **symbol** of an invariant records its value on the `m`-singular objects.
For an order-`≤ m` invariant the symbol is the top-degree data; the fundamental
theorem that it descends to a weight system on `ChordDiagram m` (via the chord
diagram of the double-point pattern) is the honest conjecture class in
`MilnorVassilievBridge.lean`. -/

variable (S) in
/-- The degree-`m` symbol of an invariant: its extension restricted to
`m`-singular objects. -/
noncomputable def symbol (v : K → R) (m : ℕ) (s : S.Sing m) : R := S.vExt v s

/-- The symbol is additive in the invariant. -/
theorem symbol_add (v w : K → R) (m : ℕ) (s : S.Sing m) :
    S.symbol (v + w) m s = S.symbol v m s + S.symbol w m s :=
  S.vExt_add v w s

/-- One order below its order, a finite-type invariant's symbol vanishes:
an order-`≤ m` invariant is annihilated on `(m+1)`-singular objects. -/
theorem symbol_succ_eq_zero {m : ℕ} {v : K → R} (hv : S.IsFiniteType m v)
    (s : S.Sing (m + 1)) : S.symbol v (m + 1) s = 0 :=
  hv (Nat.lt_succ_self m) s

end VassilievSetup

end QOU.KnotTheory.Vassiliev
