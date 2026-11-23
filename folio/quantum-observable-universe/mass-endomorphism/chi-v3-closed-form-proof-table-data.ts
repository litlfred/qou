import { table } from "../../schema/builders";
export default table({
  label: "tbl:chi-v3-closed-form-proof-table-data",
  title: "Lean theorems: $\\chi_{V_3}$ closed-form identities",
  caption: "Three sorry-free Lean theorems establishing the $\\chi_{V_3}$ neutron-proton difference in factored and polynomial forms.",
  uses: ["rem:chi-v3-closed-form-proof"],
  tags: ["chi-V3", "lean-theorems", "closed-form"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): | theorem | statement |\n|---|---|\n| `chi_V3_difference_eq_factored` | $\\chi_n - \\chi_p = -(q^2+1)^2 (q^2-1) / (4q)$ |\n| `chi_V3_difference_factored_eq_polynomial` | factored $\\leftrightarrow$ polynomial form |\n| `chi_V3_difference_eq_polynomial` | $\\chi_n - \\chi_p = -(q^5 + q^3 - q - q^{-1})/4$ |\n| `chi_V3_difference_decomposition` | split into polynomial part + geometric part |\n| `chi_V3_polynomial_part_at_one` | polynomial part vanishes at $q = 1$ |\n| `chi_V3_geom_part_at_one` | geometric part equals $1/4$ at $q = 1$ |\n| `chi_V3_difference_at_two` | numerical: $-75/8$ at $q = 2$ |\n| `chi_V3_difference_at_one` | vanishes at $q = 1$ (isospin invariance) |\n| `chi_V3_decomposition_at_two` | decomposition verified at $q = 2$ |\n" },
  ],
});
