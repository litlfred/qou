/-
# The `T_w` basis of `H_n(q)`, and promotion at the level of algebra elements

`QOU.Mathlib.HeckeAlgebra` already carries the abstract `IwahoriHeckeAlgebra`
and `MarkovTrace` classes together with concrete `H_2` and `H_3` carriers. What
it does not carry -- and what two other files in the tree say they are waiting
for, `MathlibExt.RegTraceGram` and `MathlibExt.HeckeGramFactorial` -- is a
general-`n` `T_w` basis as an actual Lean object. Every `T_w` elsewhere in the
corpus is a docstring or a hardcoded tuple.

This file supplies it, in the smallest form the jet-promotion argument needs.

## The carrier and the rule

`Hecke R m` is `Equiv.Perm (Fin m) ->0 R`: finitely-supported `R`-combinations
of permutations, i.e. the free module on `{T_w}`. The Hecke right-action rule
has two branches,

    T_w * T_i  =  T_{w s_i}                if l(w s_i) > l(w)
               =  A * T_w + T_{w s_i}      otherwise

with `A = q - q^{-1}`, and only the second splits a term across two grades.
`genTerm` is that rule on one basis element; `mulGen` extends it by linearity.

The rule is stated for an arbitrary `s`, not only an adjacent transposition.
Nothing below needs `s` to be simple -- what the promotion argument needs is
that the length rises, and that is supplied as a hypothesis or, at the top
generator, as a theorem.

## What is proved

`mulGen_eq_mapDomain` is the general form: whenever the length rises on every
element of the support, multiplication IS relabelling -- `Finsupp.mapDomain`
along `(. * s)`. Nothing splits, nothing collapses, and every coefficient is
carried across unchanged. `mulGen_apply_mul` then reads a coefficient off the
product.

`gf_mulGen` is the join. The grade generating function of the product is `X`
times that of the original, so composing interfaces multiplies -- the step that
`GradedGeneratingFunction` proved for an abstract shifted degree function, now
with the shift coming from Hecke multiplication rather than assumed.

At the fresh top generator the length hypothesis is discharged outright by
`JetGradeLengthShift.length_mul_sTop`, giving `gf_mulGen_top` with no
side condition beyond the permutations fixing the top point.

## What this still does not do

It does not prove the braid relations, does not construct the algebra
structure on `Hecke R m` (there is no `Mul` instance here -- `mulGen` is right
multiplication by a single generator, which is all the argument uses), and says
nothing about the Markov trace. Those are separate jobs.

-- Ref: [bjorner-brenti2005] https://doi.org/10.1007/3-540-27596-7
-/
import Mathlib.Tactic.Abel
import QOU.Knot.JetGradeLengthShift
import QOU.Knot.GradedGeneratingFunction

namespace QOU.Knot.HeckeTwBasis

open Polynomial
open QOU.Knot.JetGradePromotion
open QOU.Knot.JetGradeLengthShift
open QOU.Knot.GradedGeneratingFunction

variable {R : Type*} [CommRing R] {m n : ℕ}

/-- The `T_w` basis carrier: finitely-supported `R`-combinations of the `n!`
permutations. This is the free module on `{T_w : w}` and nothing more; the
algebra structure is not built here. -/
abbrev Hecke (R : Type*) [CommRing R] (m : ℕ) := (Equiv.Perm (Fin m)) →₀ R

/-- The basis element `T_w`. -/
noncomputable def Tw (w : Equiv.Perm (Fin m)) : Hecke R m := Finsupp.single w 1

/-- The Hecke right-action rule applied to a single term `c * T_w`, with Hecke
parameter `A = q - q⁻¹`. The second branch is the one that splits a term across
two filtration grades. -/
noncomputable def genTerm (A : R) (s w : Equiv.Perm (Fin m)) (c : R) : Hecke R m :=
  if length w < length (w * s) then Finsupp.single (w * s) c
  else Finsupp.single w (A * c) + Finsupp.single (w * s) c

/-- Right multiplication by the generator `T_s`, extended linearly. -/
noncomputable def mulGen (A : R) (s : Equiv.Perm (Fin m)) (x : Hecke R m) : Hecke R m :=
  x.sum (genTerm A s)

/-- **Multiplication is relabelling when the length rises.** If every element of
the support ascends under `s`, the splitting branch is never taken, so the whole
product is `Finsupp.mapDomain` along `(· * s)`: every coefficient carried across
to a new index, nothing split and nothing collapsed. -/
theorem mulGen_eq_mapDomain (A : R) (s : Equiv.Perm (Fin m)) (x : Hecke R m)
    (hasc : ∀ w ∈ x.support, length w < length (w * s)) :
    mulGen A s x = Finsupp.mapDomain (· * s) x := by
  rw [mulGen, Finsupp.mapDomain]
  refine Finsupp.sum_congr fun w hw => ?_
  simp [genTerm, hasc w hw]

/-- Right multiplication by a fixed permutation is injective. -/
theorem mul_right_inj (s : Equiv.Perm (Fin m)) :
    Function.Injective (fun w : Equiv.Perm (Fin m) => w * s) :=
  fun _ _ h => mul_right_cancel h

/-- **Coefficient transport.** The product's coefficient at `w · s` is the
original's coefficient at `w` -- the "every coefficient preserved" half of the
promotion observation. -/
theorem mulGen_apply_mul (A : R) (s : Equiv.Perm (Fin m)) (x : Hecke R m)
    (hasc : ∀ w ∈ x.support, length w < length (w * s)) (w : Equiv.Perm (Fin m)) :
    (mulGen A s x) (w * s) = x w := by
  rw [mulGen_eq_mapDomain A s x hasc]
  exact Finsupp.mapDomain_apply (mul_right_inj s) x w

/-- The support of the product is the relabelled support. -/
theorem mulGen_support (A : R) (s : Equiv.Perm (Fin m)) (x : Hecke R m)
    (hasc : ∀ w ∈ x.support, length w < length (w * s)) :
    (mulGen A s x).support = x.support.image (· * s) := by
  rw [mulGen_eq_mapDomain A s x hasc]
  exact Finsupp.mapDomain_support_of_injective (mul_right_inj s) x

/-- **The join, in general form.** The grade generating function of the product
is `X` times that of the original, whenever the length rises across the support.

This is the step `GradedGeneratingFunction.gf_shift` proved for an abstract
shifted degree function; here the shift comes from Hecke multiplication rather
than being assumed. -/
theorem gf_mulGen (A : R) (s : Equiv.Perm (Fin m)) (x : Hecke R m)
    (hasc : ∀ w ∈ x.support, length w < length (w * s))
    (hlen : ∀ w ∈ x.support, length (w * s) = length w + 1) :
    gf (mulGen A s x).support (fun w => (mulGen A s x) w) length
      = X * gf x.support (fun w => x w) length := by
  rw [mulGen_support A s x hasc, gf, Finset.sum_image
    (fun a _ b _ h => mul_right_inj s h)]
  rw [gf, Finset.mul_sum]
  refine Finset.sum_congr rfl fun w hw => ?_
  rw [mulGen_apply_mul A s x hasc w, hlen w hw]
  ring

/-- **The join at the fresh top generator**, with the length hypothesis
discharged by `JetGradeLengthShift.length_mul_sTop` rather than assumed. For an
element supported on permutations that fix the top point -- i.e. one embedded
from `H_{n+1}` into `H_{n+2}` -- multiplying by the new generator multiplies the
grade generating function by `X`.

This is the promotion observation of `computations/jet_history_retention_probe.py`
as a theorem about algebra elements. -/
theorem gf_mulGen_top (A : R) (x : Hecke R (n + 2))
    (hfix : ∀ w ∈ x.support, w top = top) :
    gf (mulGen A sTop x).support (fun w => (mulGen A sTop x) w) length
      = X * gf x.support (fun w => x w) length := by
  have hlen : ∀ w ∈ x.support, length (w * sTop) = length w + 1 :=
    fun w hw => length_mul_sTop (hfix w hw)
  exact gf_mulGen A sTop x (fun w hw => by rw [hlen w hw]; omega) hlen


/-! ## Is this rule actually the Hecke algebra's?

`genTerm` is a *definition*, so nothing so far rules out its being the wrong
rule written down confidently. The falsifiable check is the Hecke relation
itself: `T_s^2 = A * T_s + 1`, i.e. applying `mulGen` twice must equal
`A * (once) + (identity)`. That is proved below, and it is not automatic --
see the hypothesis `hne`, which is where the rule would genuinely fail. -/

theorem genTerm_zero (A : R) (s w : Equiv.Perm (Fin m)) : genTerm A s w 0 = 0 := by
  simp [genTerm]

theorem genTerm_add (A : R) (s w : Equiv.Perm (Fin m)) (a b : R) :
    genTerm A s w (a + b) = genTerm A s w a + genTerm A s w b := by
  by_cases h : length w < length (w * s) <;>
    (simp [genTerm, h, Finsupp.single_add, mul_add]; try abel)

/-- `mulGen` really is linear, not merely described as such. -/
theorem mulGen_add (A : R) (s : Equiv.Perm (Fin m)) (x y : Hecke R m) :
    mulGen A s (x + y) = mulGen A s x + mulGen A s y :=
  Finsupp.sum_add_index' (genTerm_zero A s) (genTerm_add A s)

theorem mulGen_single (A : R) (s w : Equiv.Perm (Fin m)) (c : R) :
    mulGen A s (Finsupp.single w c) = genTerm A s w c :=
  Finsupp.sum_single_index (genTerm_zero A s w)

/-- **The Hecke relation.** Applying the rule twice gives `A ·(once) + (id)`,
which is `T_s² = A·T_s + 1` read on the basis element `T_w`.

The hypothesis `hne` is the real content and is not decoration. If the length
were allowed to stay put under `s`, the descending branch would be taken twice
and the relation would fail outright -- so this theorem is a genuine constraint
on `s`, satisfied by a simple reflection (where the length parity flips) and not
by an arbitrary permutation. Stating it for arbitrary `s` without `hne` would be
false, which is precisely why it is worth proving rather than assuming. -/
theorem mulGen_mulGen_single (A : R) (s : Equiv.Perm (Fin m)) (hs : s * s = 1)
    {w : Equiv.Perm (Fin m)} (hne : length (w * s) ≠ length w) (c : R) :
    mulGen A s (mulGen A s (Finsupp.single w c))
      = A • mulGen A s (Finsupp.single w c) + Finsupp.single w c := by
  have hss : w * s * s = w := by rw [mul_assoc, hs, mul_one]
  by_cases h : length w < length (w * s)
  · have h2 : ¬ (length (w * s) < length w) := by omega
    simp only [mulGen_single, genTerm, if_pos h, hss, if_neg h2,
      Finsupp.smul_single, smul_eq_mul]
  · have hlt : length (w * s) < length w := lt_of_le_of_ne (by omega) hne
    simp only [mulGen_single, genTerm, if_neg h, mulGen_add, mulGen_single, hss,
      if_pos hlt, smul_add, Finsupp.smul_single, smul_eq_mul]


/-- **The relation, unconditionally, at the fresh top generator.** For a
permutation fixing the top point the length hypothesis is discharged by
`JetGradeLengthShift.length_mul_sTop`, so nothing is assumed.

This is what stops `mulGen_mulGen_single` from being a vacuous statement about
an unsatisfiable hypothesis: here the hypothesis is a theorem. -/
theorem mulGen_mulGen_single_top (A : R) {w : Equiv.Perm (Fin (n + 2))}
    (hw : w top = top) (c : R) :
    mulGen A sTop (mulGen A sTop (Finsupp.single w c))
      = A • mulGen A sTop (Finsupp.single w c) + Finsupp.single w c :=
  mulGen_mulGen_single A sTop (Equiv.swap_mul_self _ _)
    (by rw [length_mul_sTop hw]; omega) c

end QOU.Knot.HeckeTwBasis
