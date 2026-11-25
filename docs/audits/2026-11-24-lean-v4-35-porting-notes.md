# Lean v4.24 -> v4.35 porting notes (Mathlib f897ebc -> 56a0058)

Measured on qou branch claude/lean-upgrade-verso-2026-11-24.

- MonoidAlgebra is now a STRUCTURE wrapping `coeff : M →₀ R` (not a Finsupp).
  `F x` -> `F.coeff x`; `F.support` -> `F.coeff.support`;
  `Finsupp.add_apply/sub_apply/smul_apply` on an MA need
  `MonoidAlgebra.coeff_add/coeff_sub/coeff_smul/coeff_neg/coeff_sum` first (all rfl);
  `MonoidAlgebra.single_apply` -> `MonoidAlgebra.coeff_single_apply`;
  `(single m r).coeff = Finsupp.single m r` is `MonoidAlgebra.coeff_single`;
  `Finsupp.sum_single F` -> `MonoidAlgebra.sum_coeff_single F`;
  `MonoidAlgebra.support_mul` -> `MonoidAlgebra.support_coeff_mul_subset`;
  `MonoidAlgebra.ext` is `coeff_inj`-based: `apply MonoidAlgebra.ext; ext x`.
  MonoidAlgebra instances are noncomputable: mark defs `noncomputable`.
  `MonoidAlgebra.algHom_ext'` takes a second argument (scalar part);
  for k-algebra maps out of k use `(Subsingleton.elim _ _)`.
- `List.Sorted r l` was literally `List.Pairwise r l`: replace by `List.Pairwise`;
  `List.sorted_cons` -> `List.pairwise_cons`, `List.sorted_singleton` -> `List.pairwise_singleton`.
- `IsTotal α r` -> `Std.Total r` (instance class).
- `List.isChain_cons'` -> `List.isChain_cons`.
- `Option.noConfusion h` on `none = some _` -> `cases h` (or `nomatch h`).
- `Real.pi` "unknown constant": the file's imports no longer reach
  `Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic` — add that import.
- `List.get!` removed: use `l[i]!` or `l.getD i default` with the same meaning.
- `Finset.filter_card_add_filter_neg_card_eq_card` renamed; search Mathlib for the
  statement (`grep -rn "filter_card_add" .lake/packages/mathlib/Mathlib`).
- simp sets: `[] ++ l` may survive a `simpa only [...]`; add `List.nil_append`.
- `simp at h; omega` where simp now closes the goal: `simp at h <;> omega`.
- Removed Mathlib modules were remapped already (commit "remap 28 Mathlib modules").
- `Ordinal.nadd` lives in `MathlibExt.OrdinalNaturalOps` (ported from Mathlib).
- Deprecation warnings are fine; only errors matter.

Finding a renamed lemma: grep `.lake/packages/mathlib/Mathlib` for the old name
in `deprecated` attributes first (`grep -rn "deprecated.*OLDNAME\|alias.*OLDNAME"`),
then for the statement shape.

## Added from batch D (QOU non-MassTheory, 66 files)

- Hyperreal: `epsilon_lt_pos r h` -> `epsilon_lt_of_pos h`; `Hyperreal.st`/`.Infinite`/`st_add`
  were removed -> `ArchimedeanClass.stdPart`, `ArchimedeanClass.mk x < 0`, `stdPart_add`.
- `isUnit_of_mul_eq_one a b h` -> `IsUnit.of_mul_eq_one (a := a) b h`;
  `isCyclic_of_subgroup_isDomain` -> `isCyclic_of_injective_ringHom`;
  `MulAction.mul_smul` -> `mul_smul`; `LieHom.map_zero` -> `map_zero`;
  `Matrix.mul_eq_one_comm` -> `mul_eq_one_comm`;
  `linearIndependent_unique _ h` -> `linearIndependent_unique_iff.mpr h`;
  `measureReal_univ_eq_one` -> `probReal_univ`; `NormedSpace.exp 𝕂 x` -> `NormedSpace.exp x`;
  `Fin.castSucc_lt_succ i` -> `Fin.castSucc_lt_succ (i := i)`;
  `Matrix.PosDef`: `hpos.2 v hv` -> `hpos.dotProduct_mulVec_pos hv`;
  `Finset.diag` -> rewrite with `Finset.diag_eq_filter`;
  `Algebra.adjoinCommRingOfComm` removed (use `Algebra.isMulCommutative_adjoin`).
- `LieRing.ofAssociativeRing` is a local instance now:
  `attribute [local instance 100] LieRing.ofAssociativeRing`.
- Imports no longer reached transitively: `Mathlib.Tactic.Ring`, `Mathlib.Tactic.LinearCombination`,
  `Mathlib.Tactic.NoncommRing`, `Mathlib.Data.Fintype.Fin`,
  `Mathlib.Algebra.Module.Torsion.Field` (for `smul_eq_zero`).
- `deriving Fintype` fails outside Mathlib-style modules: write `Fintype.ofList [...]` instances.
- Lean 4.35 no longer generalises universe metavariables in structure/class fields: pin them
  (AGENTS §7d).
- `simp`/`simpa` no longer unfold a field projection of a def/instance structure literal, nor
  beta-reduce a bundled-hom literal: use the class projection, `change`/`exact`, or `rfl`.
- `simp only at h` that makes no progress is now an error: delete it.
- `add_le_add_right h c` now gives `c + a ≤ c + b`; `(mul_lt_mul_left h).mpr` -> `mul_lt_mul_of_pos_left`.
- `Rep.ofDistribMulAction` carriers are no longer reducibly the underlying type: prove by defeq.
