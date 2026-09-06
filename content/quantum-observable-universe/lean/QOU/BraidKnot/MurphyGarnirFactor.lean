import QOU.BraidKnot.DescentNodeExists
import QOU.BraidKnot.HeckeMurphyYoung

/-!
# 3.13's factorisation, lifted to the Hecke algebra

Mathas' Lemma 3.13 says a row-standard non-standard tableau `t` factors as `t = g · w`
through a **Garnir** tableau `g` with `ℓ(d(t)) = ℓ(d(g)) + ℓ(w)`.  That is a statement about
**permutations**; 3.14's induction consumes a statement about **Murphy elements**:

    m_{s t}  =  m_{s g} · T_w

This file is that lift, and it is exactly what length-additivity buys.  `T` is not a
homomorphism from `S_n` — `T_u · T_v` is a `q`-combination in general — but on a
length-additive factorisation it is, which is `TwBasis.Tw_mul_Tw`.

## The handedness, for the fourth time on this arc

`Tw_mul_Tw` reads `T_v · T_w = T_{w·v}` — the *flipped* order forced by `orbitMap`, not a
typo (see `QOU/Hecke/TwMul.lean`).  So the permutation factorisation `d(t) = w · d(g)` lifts
to the algebra factorisation

    T_{d(t)}  =  T_{d(g)} · T_w

with `T_w` on the **right**.  That is the side Mathas needs — `m_{st} = T*_{d(s)} · x_λ ·
T_{d(t)}` has `T_{d(t)}` rightmost, so the Garnir factor `T_{d(g)}` ends up adjacent to
`x_λ` and `T_w` is peeled off outside.  Had the convention been the unflipped one the same
lemma would have produced `T_w · T_{d(g)}` and stranded `T_w` in the middle, where it is
useless.  Worth stating because the three earlier instances of this trap (`sortPerm`'s
orientation, `IsDistinguishedL`, and `T_w⁻¹`'s triangularity against `w⁻¹`) were each found
only after something had been built the wrong way round.

## Two reference tableaux, and the gap that leaves — read this before using §4

`d(t)` is "the permutation carrying **the reference tableau** to `t`", and this corpus has
**two** reference tableaux, in two different files, both called `dOf`:

| | reference | file |
|---|---|---|
| `TableauPerm.dOf` | **row**-superstandard `t^λ` — Mathas' | `QOU/BraidKnot/TableauPerm.lean` |
| `HeckeMurphyYoung.dOf` | **column**-superstandard | `QOU/BraidKnot/HeckeMurphyYoung.lean` |

The whole Garnir chain (`GarnirTableau`, `GarnirDescentAdditive`, `DescentNodeExists`,
`length_dOf_smul_eq_add_iff`) is built on the **row** one; `murphyM` is built on the
**column** one.  They differ by a fixed permutation on the right — writing `c` for
`colSuperstandard ≫ (t^λ)⁻¹`,

    HeckeMurphyYoung.dOf t  =  TableauPerm.dOf t * c

so the *factorisation* `dOf (w • g) = w * dOf g` holds for **both** (it is insensitive to
the reference — §1 proves it for the column one, `TableauPerm.dOf_smul` for the row one),
while **length additivity does not transfer**: `ℓ(x)` and `ℓ(x · c)` are unrelated, and
`length_mul_eq_add_iff` turns the hypothesis into an inversion-set containment that
right-multiplication by `c` does not preserve.

**Consequence, stated plainly:** §3's Garnir corollary is proved for the **row**-referenced
`T_{d(t)}`, which is Mathas'; §4's `murphyM_smul` is proved for `murphyM` as it is currently
defined, i.e. column-referenced, and takes its length hypothesis as given.  **The two are
not yet composed**, and composing them is not a rewrite — it is either restating `murphyM`
over `refTab` (a definitional change to merged code) or re-proving the Garnir length
additivity against the column reference.  Do not write a corollary chaining §3 into §4
without doing one of those; it would be false as an inference even though both halves are
true.

## What this does NOT prove

3.14 itself.  This supplies one rewriting step of its induction — the step that turns a
non-standard `t` into a Garnir `g` plus a `T_w` factor.  What remains is that the resulting
terms drop in `MurphyInductionMeasure.murphyLex`, which needs 3.12's algebra half, which
needs 3.9.  `MurphyInductionMeasure` supplies the well-founded measure; nothing here touches
the mathematics of the descent.
-/

open Equiv
open QOU.Hecke.TwBasis QOU.Hecke.SymmetricCoxeter

namespace QOU.BraidKnot.MurphyGarnirFactor

variable {μ : YoungDiagram} {n : ℕ}
variable (K : Type*) [Field K] (q : K)

/-! ### 1. The factorisation bridge for the column-superstandard `d(t)`

`TableauPerm.dOf_smul` proves `d(w • g) = w · d(g)` for the row-superstandard reference.
The same statement for `HeckeMurphyYoung.dOf` was missing, and it is what §4 needs.  Both
proofs are the same one: `dOf t = ref ≫ t⁻¹` for *some* fixed `ref`, and the reference
cancels. -/

/-- **`d(w • g) = w · d(g)` for the column-superstandard reference.**  The companion of
`TableauPerm.dOf_smul`, which proves it for the row-superstandard one. -/
theorem HeckeMurphyYoung_dOf_smul (w : Perm (Fin (QOU.BraidKnot.Specht.nOf μ)))
    (g : QOU.BraidKnot.Specht.Tableau μ) :
    QOU.BraidKnot.HeckeMurphyYoung.dOf (w • g)
      = w * QOU.BraidKnot.HeckeMurphyYoung.dOf g := by
  refine Equiv.ext fun x => ?_
  simp [QOU.BraidKnot.HeckeMurphyYoung.dOf]
  rfl

/-- The same, transported to `Fin (n+1)` where the Coxeter system lives. -/
theorem dAt_smul (hn : QOU.BraidKnot.Specht.nOf μ = n + 1)
    (w : Perm (Fin (QOU.BraidKnot.Specht.nOf μ))) (g : QOU.BraidKnot.Specht.Tableau μ) :
    QOU.BraidKnot.HeckeMurphyYoung.dAt n hn (w • g)
      = Equiv.permCongrHom (finCongr hn) w
        * QOU.BraidKnot.HeckeMurphyYoung.dAt n hn g := by
  unfold QOU.BraidKnot.HeckeMurphyYoung.dAt
  rw [HeckeMurphyYoung_dOf_smul]
  exact map_mul _ _ _

/-! ### 2. The lift: a length-additive tableau factorisation becomes a `T`-basis one

This is the content of the file.  Everything else is packaging. -/

open QOU.BraidKnot.TableauPerm in
/-- **`T_{d(w • g)} = T_{d(g)} · T_w`** when the lengths add — the row-superstandard
(Mathas) reference.

The hypothesis is exactly the conclusion of `length_dOf_smul_eq_add_iff`, so a Garnir
descent node feeds it directly (§3). -/
theorem Tw_dOf_smul (hn : QOU.BraidKnot.Specht.nOf μ = n + 1)
    (w : Perm (Fin (QOU.BraidKnot.Specht.nOf μ))) (g : QOU.BraidKnot.Specht.Tableau μ)
    (hlen : (permCoxeterSystem n).length (toFinSucc hn (dOf (w • g)))
        = (permCoxeterSystem n).length (toFinSucc hn w)
          + (permCoxeterSystem n).length (toFinSucc hn (dOf g))) :
    Tw K q n (toFinSucc hn (dOf (w • g)))
      = Tw K q n (toFinSucc hn (dOf g)) * Tw K q n (toFinSucc hn w) := by
  have hd : toFinSucc hn (dOf (w • g)) = toFinSucc hn w * toFinSucc hn (dOf g) := by
    rw [dOf_smul, toFinSucc_mul]
  rw [hd, ← Tw_mul_Tw K q n (toFinSucc hn (dOf g)) (toFinSucc hn w)
    (by rw [← hd]; exact hlen)]

/-- The same lift for the **column**-superstandard reference, in the `dAt` form `murphyM`
consumes. -/
theorem Tw_dAt_smul (hn : QOU.BraidKnot.Specht.nOf μ = n + 1)
    (w : Perm (Fin (QOU.BraidKnot.Specht.nOf μ))) (g : QOU.BraidKnot.Specht.Tableau μ)
    (hlen : (permCoxeterSystem n).length (QOU.BraidKnot.HeckeMurphyYoung.dAt n hn (w • g))
        = (permCoxeterSystem n).length (Equiv.permCongrHom (finCongr hn) w)
          + (permCoxeterSystem n).length (QOU.BraidKnot.HeckeMurphyYoung.dAt n hn g)) :
    Tw K q n (QOU.BraidKnot.HeckeMurphyYoung.dAt n hn (w • g))
      = Tw K q n (QOU.BraidKnot.HeckeMurphyYoung.dAt n hn g)
        * Tw K q n (Equiv.permCongrHom (finCongr hn) w) := by
  have hd := dAt_smul hn w g
  rw [hd, ← Tw_mul_Tw K q n (QOU.BraidKnot.HeckeMurphyYoung.dAt n hn g)
    (Equiv.permCongrHom (finCongr hn) w) (by rw [← hd]; exact hlen)]

/-! ### 3. The Garnir corollary, in Mathas' reference

`DescentNodeExists.exists_garnir_length_additive` gives the inversion-set containment;
`length_dOf_smul_eq_add_iff` turns it into length additivity; §2 turns that into the
`T`-basis factorisation.  The `w` is recovered from `d` being a bijection.

Note the shape of the conclusion: `T_{d(t)}` **factors through the Garnir tableau**, with the
residual `T_w` on the right.  That is the rewriting step 3.14's induction performs. -/

open QOU.BraidKnot.TableauPerm QOU.Hecke.Inversions in
/-- Inversion-set containment survives the re-indexing `Fin (nOf μ) ≃ Fin (n+1)`.

Needed because `exists_garnir_length_additive` states its containment over `Fin (nOf μ)`
while `length_dOf_smul_eq_add_iff` wants it over `Fin (n+1)`, where the Coxeter system
lives.  The content is that `finCongr` preserves `Fin.val`, hence the order, hence which
pairs are inversions. -/
theorem invSet_toFinSucc_mono (hn : QOU.BraidKnot.Specht.nOf μ = n + 1)
    {a b : Perm (Fin (QOU.BraidKnot.Specht.nOf μ))}
    (hab : invSet a ⊆ invSet b) :
    invSet (toFinSucc hn a) ⊆ invSet (toFinSucc hn b) := by
  intro p hp
  simp only [invSet, Finset.mem_filter, Finset.mem_univ, true_and, toFinSucc,
    Equiv.permCongr_apply, finCongr_apply, Fin.lt_def, Fin.coe_cast] at hp ⊢
  have key : ((finCongr hn).symm p.1, (finCongr hn).symm p.2) ∈ invSet a := by
    simp only [invSet, Finset.mem_filter, Finset.mem_univ, true_and, Fin.lt_def,
      finCongr_symm, finCongr_apply, Fin.coe_cast]
    exact hp
  simpa only [invSet, Finset.mem_filter, Finset.mem_univ, true_and, Fin.lt_def,
    finCongr_symm, finCongr_apply, Fin.coe_cast] using hab key

open QOU.BraidKnot.TableauPerm QOU.BraidKnot.GarnirTableau
  QOU.BraidKnot.RowStandardTableau QOU.BraidKnot.DescentNodeExists in
/-- **The `w` that carries one tableau to another.**  `d` is a bijection onto `S_n`, so
`t = w • g` has a unique solution. -/
theorem smul_eq_of_dOf (t g : QOU.BraidKnot.Specht.Tableau μ) :
    (dOf t * (dOf g)⁻¹) • g = t := by
  refine dOf_injective ?_
  rw [dOf_smul, mul_assoc, inv_mul_cancel, mul_one]

open QOU.BraidKnot.TableauPerm QOU.BraidKnot.GarnirTableau
  QOU.BraidKnot.RowStandardTableau QOU.BraidKnot.DescentNodeExists in
/-- **Mathas 3.13, lifted to the `T`-basis.**

A row-standard non-standard tableau's `T_{d(t)}` factors as `T_{d(g)} · T_w` for a Garnir
tableau `g`.  Both halves come from elsewhere — the descent node from
`exists_garnir_length_additive`, the lift from `Tw_dOf_smul` — and this is where they meet. -/
theorem exists_garnir_Tw_factor (hn : QOU.BraidKnot.Specht.nOf μ = n + 1)
    {t : QOU.BraidKnot.Specht.Tableau μ}
    (hrs : IsRowStandard t) (hns : ¬ IsStandard t) :
    ∃ (i j : ℕ) (h : (i + 1, j) ∈ μ) (w : Perm (Fin (QOU.BraidKnot.Specht.nOf μ))),
      w • garnirTab i j h = t ∧
      Tw K q n (toFinSucc hn (dOf t))
        = Tw K q n (toFinSucc hn (dOf (garnirTab i j h))) * Tw K q n (toFinSucc hn w) := by
  obtain ⟨i, j, h, hsub⟩ := exists_garnir_length_additive hrs hns
  refine ⟨i, j, h, dOf t * (dOf (garnirTab i j h))⁻¹, smul_eq_of_dOf t _, ?_⟩
  set g := garnirTab i j h with hg
  set w := dOf t * (dOf g)⁻¹ with hw
  have hsm : w • g = t := smul_eq_of_dOf t g
  have hlen : (permCoxeterSystem n).length (toFinSucc hn (dOf (w • g)))
      = (permCoxeterSystem n).length (toFinSucc hn w)
        + (permCoxeterSystem n).length (toFinSucc hn (dOf g)) := by
    refine (length_dOf_smul_eq_add_iff hn w g).2 ?_
    rw [hsm]
    -- `invSet (d(g)) ⊆ invSet (d(t))` is exactly the descent-node conclusion, once
    -- `d(g)` is recognised as the Garnir permutation and both sides are re-indexed.
    refine invSet_toFinSucc_mono hn ?_
    rw [hg, dOf_garnirTab]
    exact hsub
  have := Tw_dOf_smul K q hn w g hlen
  rw [hsm] at this
  exact this

/-! ### 4. The Murphy element itself

With `murphyM` as currently defined — column-superstandard reference — the factorisation of
`T_{d(t)}` passes straight through to `m_{st}`, because `T_{d(t)}` is the rightmost factor.

Read the scope note in the module docstring before chaining this to §3: the length hypothesis
here is about the **column**-referenced `d`, and the Garnir result of §3 supplies it for the
**row**-referenced one.  They are different hypotheses. -/

/-- **`m_{s, w • g} = m_{s, g} · T_w`** on a length-additive factorisation.

This is the Murphy-element form of `Tw_dAt_smul`, and the step 3.14's induction rewrites
with.  Nothing is assumed about `g` being Garnir — the lemma is exactly as strong as its
length hypothesis. -/
theorem murphyM_smul (hn : QOU.BraidKnot.Specht.nOf μ = n + 1)
    (s g : QOU.BraidKnot.Specht.Tableau μ)
    (w : Perm (Fin (QOU.BraidKnot.Specht.nOf μ)))
    [DecidablePred (· ∈ QOU.BraidKnot.HeckeMurphyYoung.youngSubgroup n hn
      (QOU.BraidKnot.ColSuperstandardTableau.colSuperstandard μ))]
    (hlen : (permCoxeterSystem n).length (QOU.BraidKnot.HeckeMurphyYoung.dAt n hn (w • g))
        = (permCoxeterSystem n).length (Equiv.permCongrHom (finCongr hn) w)
          + (permCoxeterSystem n).length (QOU.BraidKnot.HeckeMurphyYoung.dAt n hn g)) :
    QOU.BraidKnot.HeckeMurphyYoung.murphyM K q n hn s (w • g)
      = QOU.BraidKnot.HeckeMurphyYoung.murphyM K q n hn s g
        * Tw K q n (Equiv.permCongrHom (finCongr hn) w) := by
  simp only [QOU.BraidKnot.HeckeMurphyYoung.murphyM, Tw_dAt_smul K q hn w g hlen, mul_assoc]

end QOU.BraidKnot.MurphyGarnirFactor
