import { example } from "../../schema/builders";

export default example({
  label: "ex:chi-minus-six-derivation",
  title: "$\\chi_{\\mathrm{eu}}(M_0) = -6$: the derivation chain",
  interprets: "def:archimedean-condition",
  uses: [
    "def:archimedean-condition",
    "def:motivic-substrate",
    "prop:euler-char-stability",
    "rem:kummer-tower",
    "thm:motivic-perpetual-obstruction",
    "rem:three-euler-characteristics",
  ],
  tags: ["descartes", "chi", "derivation", "example", "motivic-galois"],
  cites: ["reyescarocca2022", "braden-disney-hogg-2022"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body:
        "Lean formalization: `QOU.Brings.CohomologicalGenusFourAndSymplecticEmbeddings` (`folio/quantum-observable-universe/lean/QOU/Brings/CohomologicalGenusFourAndSymplecticEmbeddings.lean`) and `QOU.Brings.BringTranspositionSixFixedPointsAndEllipticQuotient` (`folio/quantum-observable-universe/lean/QOU/Brings/BringTranspositionSixFixedPointsAndEllipticQuotient.lean`) prove the three cohomological identities for $2 - 2g$ (`rank2_deg0_index_eq_top_euler`, `hkr_alternating_betti_eq_top_euler`, `de_rham_hodge_dim_iff_genus_four`), the contrast between mixed-chirality ($b = 4, g = 2$ and $b = 5, g = 3$) and uniform-chirality ($\\epsilon_j = 1$, $3 \\mid b$) $\\mathbb{Z}_3$-Kummer covers (`mixed_vs_uniform_chirality_z3_kummer`), the minimal hyperbolic uniform-chirality bound $b = 6, g = 4, \\chi_{\\mathrm{eu}} = -6$ selecting the moduli stratum $\\mathcal{M}_4$ (`minimal_hyperbolic_z3_kummer_forces_genus_four`), the cohomological torus-knot genus saturation under the discrete gauge-carrier cutoff (`cohomological_knot_saturation_forces_genus_four`), and the exact algebraic reduction of each transposition involution $\\tau \\in S_5$ on $\\Sigma_4$ to the separable cubic $P_\\tau(t) = t^3 + 2t^2 + 3t + 4 = 0$ ($\\Delta = -200$, `bring_transposition_fixed_iff_vieta`, `transposition_cubic_discriminant_eq_neg_200`) with $3! = 6$ fixed points per transposition, pairwise disjointness across the $\\binom{5}{2} = 10$ transpositions giving $10 \\times 6 = 60 = 4^3 - 4$ Weierstrass points (`overlapping_transpositions_disjoint`, `disjoint_transpositions_disjoint`, `bring_weierstrass_point_count_from_transpositions`), and the degree-2 elliptic quotient Riemann–Hurwitz identity $\\chi(\\Sigma_4) = 2\\chi(E_\\tau) - 6 = -6$ (`bring_elliptic_quotient_forces_chi_eq_neg_six`, bean `qou-qhcr`).",
    },
  ],
});
