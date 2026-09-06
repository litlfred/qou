import QOU.BraidKnot.MurphyGarnirFactor

/-!
# The Murphy element with its reference tableau made explicit — and 3.13 composed onto it

`MurphyGarnirFactor` proves two halves and refuses to compose them, because `d(t)` means
two different things in the corpus:

* the Garnir chain (`GarnirTableau`, `DescentNodeExists`, `exists_garnir_Tw_factor`) uses
  `TableauPerm.dOf`, whose reference is the **row**-superstandard `t^λ` — Mathas';
* `murphyM` uses `HeckeMurphyYoung.dOf`, whose reference is **column**-superstandard.

`murphy_reference_tableau_additivity_probe.py` then measured that the difference is not
cosmetic: 3.13's length additivity holds at every one of 1789 row-standard non-standard
tableaux under the row reference and fails for **48 %** of them at `n = 6` under the column
one, with the smallest counterexample at `λ = (2,1,1)`.  So the composition cannot be
obtained by re-proving the Garnir side; the Murphy element has to be stated over `t^λ`.

## What this file does, and what it deliberately does not

It does **not** edit `HeckeMurphyYoung`.  Instead it makes the reference an **explicit
parameter** — the thing whose absence caused the collision — and recovers the existing
definitions as instances:

    dOfRef r t        d(t) relative to an arbitrary reference `r`
    dAtRef n h r t    the same at the Hecke algebra's index
    murphyMRef r s t  T*_{d_r(s)} · x_r · T_{d_r(t)}

    murphyMRef (colSuperstandard μ) = murphyM      (`murphyMRef_colSuperstandard`, `rfl`)
    murphyMRow := murphyMRef (refTab μ)            Mathas' element

Nothing downstream of `murphyM` changes: `murphyM` is *definitionally* one instance of
`murphyMRef`, so `murphyFamily`, `basisOfSpanning` and `murphyBasisOfSpanning` are
untouched and keep proving exactly what they proved.

**The rank axis is clear for the row instance, and this was checked rather than assumed.**
`murphy_supp_rsk_probe.py`'s rank guard reports **row 6/6, 24/24, 120/120 — FULL** at
`n = 3,4,5`, the same as the column reference.  (That guard sat below its file's
`if __name__` block and had never run; it is wired in now.  What its result licenses is
narrow: the reference does not change the **rank**. It does change 3.13's length
additivity, which is the whole reason this file exists — so do not restate it as "the
reference does not matter".)

## The composition

`exists_garnir_murphyMRow_factor` is the point: for a row-standard non-standard `t`,

    m^row_{s t}  =  m^row_{s g} · T_w

with `g` a Garnir tableau.  This is the rewriting step Mathas' Lemma 3.14 performs, on the
element 3.14 is actually about.  In `MurphyGarnirFactor` the two halves could only be
stated separately; here they meet.

## Still not 3.14

The step is proved; the induction is not run.  What remains is that the terms this rewriting
produces descend in `MurphyInductionMeasure.murphyLex`, which needs 3.12's algebra half and
hence 3.9 at basis level.  `murphyLex_wellFounded` says such an induction terminates; it does
not say the terms descend.
-/

open Equiv
open QOU.Hecke.TwBasis QOU.Hecke.SymmetricCoxeter

namespace QOU.BraidKnot.MurphyRefTab

open QOU.BraidKnot.HeckeMurphyYoung (antiAutTw youngSubgroup)
open QOU.BraidKnot.HeckeMurphy (murphySum)

variable {μ : YoungDiagram} {n : ℕ}
variable (K : Type*) [Field K] (q : K)

/-! ### 1. The reference as a parameter -/

/-- **`d_r(t)`** — the permutation carrying an arbitrary reference tableau `r` to `t`.

`HeckeMurphyYoung.dOf` is this at `r = colSuperstandard μ` and `TableauPerm.dOf` at
`r = refTab μ`; both are `rfl` instances (`dOfRef_colSuperstandard`, `dOfRef_refTab`). -/
noncomputable def dOfRef (r t : QOU.BraidKnot.Specht.Tableau μ) :
    Perm (Fin (QOU.BraidKnot.Specht.nOf μ)) :=
  r.trans t.symm

@[simp] theorem dOfRef_colSuperstandard (t : QOU.BraidKnot.Specht.Tableau μ) :
    dOfRef (QOU.BraidKnot.ColSuperstandardTableau.colSuperstandard μ) t
      = QOU.BraidKnot.HeckeMurphyYoung.dOf t := rfl

@[simp] theorem dOfRef_refTab (t : QOU.BraidKnot.Specht.Tableau μ) :
    dOfRef (QOU.BraidKnot.TableauPerm.refTab μ) t = QOU.BraidKnot.TableauPerm.dOf t := rfl

/-- **The factorisation is reference-insensitive.**  `d_r(w • g) = w · d_r(g)` for *every*
reference — one proof, where the corpus had two (`TableauPerm.dOf_smul` and
`MurphyGarnirFactor.HeckeMurphyYoung_dOf_smul`) and no statement connecting them.

This is the half that transfers.  The half that does not is length additivity, and that is
what forces `murphyMRow` below. -/
theorem dOfRef_smul (r : QOU.BraidKnot.Specht.Tableau μ)
    (w : Perm (Fin (QOU.BraidKnot.Specht.nOf μ))) (g : QOU.BraidKnot.Specht.Tableau μ) :
    dOfRef r (w • g) = w * dOfRef r g := by
  refine Equiv.ext fun x => ?_
  simp [dOfRef]
  rfl

/-- `d_r(t)` at the Hecke algebra's index. -/
noncomputable def dAtRef (n : ℕ) (h : QOU.BraidKnot.Specht.nOf μ = n + 1)
    (r t : QOU.BraidKnot.Specht.Tableau μ) : Perm (Fin (n + 1)) :=
  Equiv.permCongrHom (finCongr h) (dOfRef r t)

@[simp] theorem dAtRef_colSuperstandard (h : QOU.BraidKnot.Specht.nOf μ = n + 1)
    (t : QOU.BraidKnot.Specht.Tableau μ) :
    dAtRef n h (QOU.BraidKnot.ColSuperstandardTableau.colSuperstandard μ) t
      = QOU.BraidKnot.HeckeMurphyYoung.dAt n h t := rfl

@[simp] theorem dAtRef_refTab (h : QOU.BraidKnot.Specht.nOf μ = n + 1)
    (t : QOU.BraidKnot.Specht.Tableau μ) :
    dAtRef n h (QOU.BraidKnot.TableauPerm.refTab μ) t
      = QOU.BraidKnot.TableauPerm.toFinSucc h (QOU.BraidKnot.TableauPerm.dOf t) := rfl

theorem dAtRef_smul (h : QOU.BraidKnot.Specht.nOf μ = n + 1)
    (r : QOU.BraidKnot.Specht.Tableau μ)
    (w : Perm (Fin (QOU.BraidKnot.Specht.nOf μ))) (g : QOU.BraidKnot.Specht.Tableau μ) :
    dAtRef n h r (w • g)
      = Equiv.permCongrHom (finCongr h) w * dAtRef n h r g := by
  unfold dAtRef
  rw [dOfRef_smul]
  exact map_mul _ _ _

/-! ### 2. The Murphy element over an arbitrary reference

`x_λ` is the Murphy element of the **reference's** row stabiliser, so the reference appears
twice in `m_{st}`: in `d_r` and in `x_r`.  Both move together. -/

/-- **Murphy's `m_{st}`, with the reference tableau explicit**:
`T*_{d_r(s)} · x_r · T_{d_r(t)}`. -/
noncomputable def murphyMRef (h : QOU.BraidKnot.Specht.nOf μ = n + 1)
    (r s t : QOU.BraidKnot.Specht.Tableau μ)
    [DecidablePred (· ∈ youngSubgroup n h r)] :
    QOU.Hecke.IwahoriHecke K q n :=
  (antiAutTw K q n (Tw K q n (dAtRef n h r s))).unop
    * murphySum K q n {w | w ∈ youngSubgroup n h r}
    * Tw K q n (dAtRef n h r t)

/-- **`murphyM` is the column-superstandard instance** — definitionally, so nothing
downstream of `murphyM` is disturbed by this file's existence. -/
theorem murphyMRef_colSuperstandard (h : QOU.BraidKnot.Specht.nOf μ = n + 1)
    (s t : QOU.BraidKnot.Specht.Tableau μ)
    [DecidablePred (· ∈ youngSubgroup n h
      (QOU.BraidKnot.ColSuperstandardTableau.colSuperstandard μ))] :
    murphyMRef K q h (QOU.BraidKnot.ColSuperstandardTableau.colSuperstandard μ) s t
      = QOU.BraidKnot.HeckeMurphyYoung.murphyM K q n h s t := rfl

/-- **Mathas' Murphy element**: the row-superstandard instance.  This is the object 3.13
and 3.14 are about, and the one `exists_garnir_murphyMRow_factor` below factors. -/
noncomputable def murphyMRow (h : QOU.BraidKnot.Specht.nOf μ = n + 1)
    (s t : QOU.BraidKnot.Specht.Tableau μ)
    [DecidablePred (· ∈ youngSubgroup n h (QOU.BraidKnot.TableauPerm.refTab μ))] :
    QOU.Hecke.IwahoriHecke K q n :=
  murphyMRef K q h (QOU.BraidKnot.TableauPerm.refTab μ) s t

/-! ### 3. The lift, for every reference at once

`MurphyGarnirFactor.Tw_dOf_smul` and `.Tw_dAt_smul` are this statement for the two
references separately; with the parameter explicit it is one lemma. -/

/-- **`T_{d_r(w • g)} = T_{d_r(g)} · T_w`** when the lengths add.

The `T_w` is on the **right** — the flipped handedness of `Tw_mul_Tw`, which is the side
`m_{st}` needs since `T_{d(t)}` is its rightmost factor. -/
theorem Tw_dAtRef_smul (h : QOU.BraidKnot.Specht.nOf μ = n + 1)
    (r : QOU.BraidKnot.Specht.Tableau μ)
    (w : Perm (Fin (QOU.BraidKnot.Specht.nOf μ))) (g : QOU.BraidKnot.Specht.Tableau μ)
    (hlen : (permCoxeterSystem n).length (dAtRef n h r (w • g))
        = (permCoxeterSystem n).length (Equiv.permCongrHom (finCongr h) w)
          + (permCoxeterSystem n).length (dAtRef n h r g)) :
    Tw K q n (dAtRef n h r (w • g))
      = Tw K q n (dAtRef n h r g) * Tw K q n (Equiv.permCongrHom (finCongr h) w) := by
  have hd := dAtRef_smul h r w g
  rw [hd, ← Tw_mul_Tw K q n (dAtRef n h r g)
    (Equiv.permCongrHom (finCongr h) w) (by rw [← hd]; exact hlen)]

/-- **`m^r_{s, w • g} = m^r_{s, g} · T_w`** on a length-additive factorisation, for every
reference `r`.  `MurphyGarnirFactor.murphyM_smul` is the `colSuperstandard` case. -/
theorem murphyMRef_smul (h : QOU.BraidKnot.Specht.nOf μ = n + 1)
    (r s g : QOU.BraidKnot.Specht.Tableau μ)
    (w : Perm (Fin (QOU.BraidKnot.Specht.nOf μ)))
    [DecidablePred (· ∈ youngSubgroup n h r)]
    (hlen : (permCoxeterSystem n).length (dAtRef n h r (w • g))
        = (permCoxeterSystem n).length (Equiv.permCongrHom (finCongr h) w)
          + (permCoxeterSystem n).length (dAtRef n h r g)) :
    murphyMRef K q h r s (w • g)
      = murphyMRef K q h r s g * Tw K q n (Equiv.permCongrHom (finCongr h) w) := by
  simp only [murphyMRef, Tw_dAtRef_smul K q h r w g hlen, mul_assoc]

/-! ### 4. The composition `MurphyGarnirFactor` could not make

At `r = refTab μ` the length hypothesis of §3 **is** the conclusion of
`TableauPerm.length_dOf_smul_eq_add_iff`, which is what the Garnir descent node supplies.
So the two halves meet, and they meet only here — under the column reference the hypothesis
is false for 48 % of `n = 6` tableaux. -/

open QOU.BraidKnot.TableauPerm QOU.BraidKnot.GarnirTableau
  QOU.BraidKnot.RowStandardTableau QOU.BraidKnot.MurphyGarnirFactor
  QOU.BraidKnot.DescentNodeExists in
/-- **Mathas 3.13, on Mathas' Murphy element.**

A row-standard non-standard `t` gives a Garnir tableau `g` and a `w` with

    m^row_{s t}  =  m^row_{s g} · T_w

This is 3.14's rewriting step, on the object 3.14 is about.  It does **not** hold for the
column-superstandard `murphyM` — see the module docstring; that is why the reference had to
become a parameter first. -/
theorem exists_garnir_murphyMRow_factor (hn : QOU.BraidKnot.Specht.nOf μ = n + 1)
    (s : QOU.BraidKnot.Specht.Tableau μ) {t : QOU.BraidKnot.Specht.Tableau μ}
    [DecidablePred (· ∈ youngSubgroup n hn (refTab μ))]
    (hrs : IsRowStandard t) (hns : ¬ IsStandard t) :
    ∃ (i j : ℕ) (h : (i + 1, j) ∈ μ) (w : Perm (Fin (QOU.BraidKnot.Specht.nOf μ))),
      w • garnirTab i j h = t ∧
      murphyMRow K q hn s t
        = murphyMRow K q hn s (garnirTab i j h)
          * Tw K q n (Equiv.permCongrHom (finCongr hn) w) := by
  obtain ⟨i, j, h, hsub⟩ := exists_garnir_length_additive hrs hns
  refine ⟨i, j, h, dOf t * (dOf (garnirTab i j h))⁻¹, smul_eq_of_dOf t _, ?_⟩
  set g := garnirTab i j h with hg
  set w := dOf t * (dOf g)⁻¹ with hw
  have hsm : w • g = t := smul_eq_of_dOf t g
  have hlen : (permCoxeterSystem n).length (dAtRef n hn (refTab μ) (w • g))
      = (permCoxeterSystem n).length (Equiv.permCongrHom (finCongr hn) w)
        + (permCoxeterSystem n).length (dAtRef n hn (refTab μ) g) := by
    refine (length_dOf_smul_eq_add_iff hn w g).2 ?_
    rw [hsm]
    refine invSet_toFinSucc_mono hn ?_
    rw [hg, dOf_garnirTab]
    exact hsub
  have := murphyMRef_smul K q hn (refTab μ) s g w hlen
  rw [hsm] at this
  exact this

end QOU.BraidKnot.MurphyRefTab
