import Mathlib.Tactic

/-!
# The linear-chain bond sum is ordering-dependent unless the substrate is classical

`atom_braid_word_3A` builds an atom's braid word from
`ordering = ['p']*Z + ['n']*N` — a hard-coded arrangement of the nucleons on a
line. The chain binding is then a sum over *adjacent* pairs,

    B(w) = α · ∑_{adjacent (a,b) in w} L_{ab},   L ∈ {L_pp, L_pn, L_nn},

so it depends on the arrangement `w` and not only on `(Z, N)`. A nucleus has no
arrangement, so the dependence is a non-physical degree of freedom. Measured
under convention C (2026-08-08, `qou-h7mh`) the spread reached **2.27 MeV** at
⁴He and **2.88 MeV** at ⁷Li, and the hard-coded choice was not even the best one
(³He `ppn` gives −11.9 % against AME where `pnp` gives +0.79 %).

This file asks the structural question that measurement cannot: **can the
arrangement dependence be removed by choosing the bond scalars better?**

## Result

`orderIndependent_iff` — the chain bond sum is invariant under every
rearrangement **iff** `L_pp = L_pn = L_nn`. The two `A = 3` witnesses force it:

    B(ppn) = L_pp + L_pn      vs   B(pnp) = 2·L_pn      ⟹  L_pp = L_pn
    B(nnp) = L_nn + L_pn      vs   B(npn) = 2·L_pn      ⟹  L_nn = L_pn

and conversely a constant scalar makes `B` a function of the nucleon count alone
(`bondSum_const`).

`not_orderIndependent_of_ne` — so `L_pp ≠ L_nn` is already enough to make the
chain arrangement-dependent, at every `A ≥ 3`.

## Why this is an exclusion and not a nuisance

`QOU/QBeta/InterfaceScalar.charge_independence_iff` proves (sorry-free)
`L_pp = L_nn ↔ h = 0 ↔ q = 1`. Combining it with `not_orderIndependent_of_ne`:
**the linear-chain bond sum is arrangement-independent only in the classical
limit**, where the Hecke structure collapses. At the substrate `q₀ ≠ 1` there is
no assignment of bond scalars that repairs it.

Scope **(b)**, invariant named (the two `A = 3` rearrangements above). What it
excludes is *the linear-chain ansatz as a well-defined binding functional at
`q ≠ 1`* — not the bond picture itself. Symmetrising over arrangements, or
choosing a different convention, cannot help: the defect is that the chain has
an arrangement at all. The repair has to change the **bond set** — a coordination
graph, an all-pairs sum, or a derived edge set (`qou-h7mh` proposes deriving it
from the SU(4) partition shape) — which is a different object, not a better
ordering.

Consequence for the body-order programme (`qou-i5yp`, `qou-d9sk`): the Ursell
cumulants `b₃`, `b₄` are built from `A ≥ 3` bindings, so each inherits this
freedom. Extending the inversion to ⁶Li/⁷Li — the prerequisite for the
body-order recurrence test to be falsifiable — inherits it too, and the
arrangement must be settled first or the extension measures the convention.

Stated over a generic ring per AGENTS.md §7c; letters are `Bool` with `true` for
a proton, and nothing here is archimedean.
-/

namespace QOU.MassTheory.ChainBondOrderDependence

variable {R : Type*}

/-- The scalar attached to an adjacent pair: like pairs get `Lpp` / `Lnn`,
unlike pairs get `Lpn`. `true` is a proton. -/
def bondOf (Lpp Lpn Lnn : R) (a b : Bool) : R :=
  if a = b then (if a then Lpp else Lnn) else Lpn

/-- The linear-chain bond sum over the adjacent pairs of an arrangement. -/
def bondSum [AddMonoid R] (Lpp Lpn Lnn : R) : List Bool → R
  | [] => 0
  | [_] => 0
  | a :: b :: rest => bondOf Lpp Lpn Lnn a b + bondSum Lpp Lpn Lnn (b :: rest)

section Monoid

variable [AddMonoid R] {Lpp Lpn Lnn : R}

@[simp] theorem bondSum_nil : bondSum Lpp Lpn Lnn [] = 0 := rfl

@[simp] theorem bondSum_singleton (a : Bool) : bondSum Lpp Lpn Lnn [a] = 0 := rfl

@[simp] theorem bondSum_cons_cons (a b : Bool) (rest : List Bool) :
    bondSum Lpp Lpn Lnn (a :: b :: rest)
      = bondOf Lpp Lpn Lnn a b + bondSum Lpp Lpn Lnn (b :: rest) := rfl

/-- With one scalar on every bond, the sum counts bonds and forgets the
arrangement entirely. -/
theorem bondSum_const (L : R) : ∀ (a : Bool) (w : List Bool),
    bondSum L L L (a :: w) = w.length • L := by
  intro a w
  induction w generalizing a with
  | nil => simp
  | cons b rest ih =>
    rw [bondSum_cons_cons, ih b]
    have hb : bondOf L L L a b = L := by
      unfold bondOf; split <;> [split <;> rfl; rfl]
    rw [hb, List.length_cons, succ_nsmul']
    
end Monoid

section Ring

variable [AddCommGroup R] {Lpp Lpn Lnn : R}

/-- `ppn` — the hard-coded arrangement at `A = 3`, `Z = 2`. -/
theorem bondSum_ppn : bondSum Lpp Lpn Lnn [true, true, false] = Lpp + Lpn := by
  simp [bondOf]

/-- `pnp` — the same nucleus, rearranged. -/
theorem bondSum_pnp : bondSum Lpp Lpn Lnn [true, false, true] = Lpn + Lpn := by
  simp [bondOf]

/-- `nnp` — the hard-coded arrangement at `A = 3`, `Z = 1`. -/
theorem bondSum_nnp : bondSum Lpp Lpn Lnn [false, false, true] = Lnn + Lpn := by
  simp [bondOf]

/-- `npn` — the same nucleus, rearranged. -/
theorem bondSum_npn : bondSum Lpp Lpn Lnn [false, true, false] = Lpn + Lpn := by
  simp [bondOf]

/-- The two `A = 3` rearrangements force all three bond scalars to coincide. -/
theorem eq_of_orderIndependent
    (h : ∀ w v : List Bool, w.Perm v →
      bondSum Lpp Lpn Lnn w = bondSum Lpp Lpn Lnn v) :
    Lpp = Lpn ∧ Lnn = Lpn := by
  constructor
  · have h1 := h [true, true, false] [true, false, true] (by decide)
    rw [bondSum_ppn, bondSum_pnp] at h1
    exact add_right_cancel h1
  · have h2 := h [false, false, true] [false, true, false] (by decide)
    rw [bondSum_nnp, bondSum_npn] at h2
    exact add_right_cancel h2

/-- **The chain bond sum is arrangement-independent exactly when the three bond
scalars coincide.** -/
theorem orderIndependent_iff :
    (∀ w v : List Bool, w.Perm v →
        bondSum Lpp Lpn Lnn w = bondSum Lpp Lpn Lnn v)
      ↔ (Lpp = Lpn ∧ Lnn = Lpn) := by
  refine ⟨eq_of_orderIndependent, fun ⟨h1, h2⟩ w v hwv => ?_⟩
  subst h1; subst h2
  match w, v with
  | [], v => simpa using (List.Perm.nil_eq hwv) ▸ rfl
  | a :: w', [] => exact absurd hwv.length_eq (by simp)
  | a :: w', b :: v' =>
    rw [bondSum_const, bondSum_const]
    have : (a :: w').length = (b :: v').length := hwv.length_eq
    simp only [List.length_cons] at this
    rw [Nat.succ_inj.mp this]

/-- Distinct like-pair scalars already break arrangement-independence. With
`InterfaceScalar.charge_independence_iff` (`L_pp = L_nn ↔ h = 0 ↔ q = 1`) this
says the chain is well defined only in the classical limit. -/
theorem not_orderIndependent_of_ne (hne : Lpp ≠ Lnn) :
    ¬ (∀ w v : List Bool, w.Perm v →
        bondSum Lpp Lpn Lnn w = bondSum Lpp Lpn Lnn v) := by
  intro h
  obtain ⟨h1, h2⟩ := eq_of_orderIndependent h
  exact hne (h1.trans h2.symm)

end Ring

end QOU.MassTheory.ChainBondOrderDependence
