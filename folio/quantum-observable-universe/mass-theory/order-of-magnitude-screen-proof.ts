import { proof } from "../../schema/builders";

export default proof({
  label: "prf:order-of-magnitude-screen",
  title: "Proof of the order-of-magnitude screen properties",
  uses: ["prop:order-of-magnitude-screen"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Lean.** `screen_mono`, `screen_refl`, `screen_abs_iff`, `screen_symm`, `screen_trans`, `screen_mul`, `screen_prod_one`, `ne_of_not_screen_of_screen`, `screen_one_add`, `screen_ladder_prod`, `mul_pow_lt_of_lt`, `mul_prod_lt_of_lt`, `not_screen_pow_of_le`, `eventually_not_screen_pow`, `additive_admits_zero`, `additive_iff_le_of_nonneg`, `additive_of_screen_of_nonneg` and `operational_test_not_sufficient` in the sibling file, over any linearly ordered field (Archimedean for `eventually_not_screen_pow`). Sorry-free, lean-direct exit 0." },
  ],
});
