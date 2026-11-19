import { proof } from "../../schema/builders";

export default proof({
  label: "prf:c5-involution-leibniz-decomposition",
  title: "Proof of c5 involution leibniz decomposition",
  uses: ["prop:c5-involution-leibniz-decomposition", "prop:neutron-qvalue-symbolic", "prop:silver-ratio-beta-decay-null"],
  authorNotes: [
    {
      kind: "status",
      body: "All 24 algebraic/analytic steps formalised in `c5-involution-leibniz-decomposition.lean` (`hoefsmit_b_squared_eq_one_minus_inv_quantum_two_squared`, `c5_decomposition_via_quantum_two`, `c5_classical_limit_eq_neg_five_quarters`, `c5_classical_eq_wedderburn_nonsign_dim_half`, `quantumTwo_at_silver_ratio_squared`, `b_squared_at_silver_ratio`, `c5_at_silver_ratio_is_minus_11_over_8`, `quantum_two_squared_eq_skein_squared_plus_four`, `c5_as_function_of_skein`, `c5RationalMap_at_skein_eq_c5Decomposition`, `h_sq_plus_four_pos`, `h_sq_plus_four_ne_zero`, `c5RationalMap_even`, `c5RationalMap_le_neg_five_quarters`, `c5RationalMap_gt_neg_three_halves`, `c5RationalMap_strict_neg`, `c5RationalMap_max_at_zero`, `c5OfHSquared_antitone_on_nonneg`, `c5RationalMap_factor`).",
    },
  ],
});
