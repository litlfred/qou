import { proof } from "../../schema/builders";

export default proof({
  label: "prf:polynomial-bar-involution",
  title: "Proof of polynomial bar involution",
  uses: ["prop:polynomial-bar-involution"],
  authorNotes: [
    {
      kind: "status",
      body: "Formalised in `polynomial-bar-involution.lean` via Mathlib `Polynomial.comp` lemmas (`barPoly_X`, `barPoly_neg_X`, `barPoly_C`, `barPoly_add`, `barPoly_mul`, `barPoly_one`, `barPoly_zero`, `barPoly_involutive`, `barPoly_X_pow_two`, `barPoly_X_pow`, `barPoly_X_pow_even`, `barPoly_X_pow_odd`, `barPoly_natCast`, `barPoly_sub`, `barPoly_neg`, `barPoly_c5_denominator`, `barPoly_c5_taylor_6`, `barPoly_cos_truncated_6`, `barPoly_cosh_truncated_6`, `three_layer_truncated_all_bar_symmetric`, `barPoly_evenPoly_6`, `barPoly_even_truncated_arbitrary`, `barPoly_odd_truncated_arbitrary`, `c5_taylor_6_eval_zero`, `c5_taylor_6_eval_one`).",
    },
  ],
});
