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
