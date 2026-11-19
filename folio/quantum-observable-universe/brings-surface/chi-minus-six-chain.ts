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
        "Lean formalization: `QOU.Brings.CohomologicalGenusFourAndSymplecticEmbeddings` (`folio/quantum-observable-universe/lean/QOU/Brings/CohomologicalGenusFourAndSymplecticEmbeddings.lean`) proves the three cohomological identities for $2 - 2g$ (`rank2_deg0_index_eq_top_euler`, `hkr_alternating_betti_eq_top_euler`, `de_rham_hodge_dim_iff_genus_four`), the contrast between mixed-chirality ($b = 4, g = 2$ and $b = 5, g = 3$) and uniform-chirality ($\\epsilon_j = 1$, $3 \\mid b$) $\\mathbb{Z}_3$-Kummer covers (`mixed_vs_uniform_chirality_z3_kummer`), the minimal hyperbolic uniform-chirality bound $b = 6, g = 4, \\chi_{\\mathrm{eu}} = -6$ selecting the moduli stratum $\\mathcal{M}_4$ (`minimal_hyperbolic_z3_kummer_forces_genus_four`), and the cohomological torus-knot genus saturation under the discrete gauge-carrier cutoff (`cohomological_knot_saturation_forces_genus_four`). Within $\\mathcal{M}_4$, Step 7 selects Bring's curve $\\Sigma_4$ by maximal $S_5$ symmetry (`[reyescarocca2022]`, `[braden-disney-hogg-2022]`); on $\\Sigma_4$ itself (whose $\\mathbb{Z}_3 \\subset S_5$ quotients are unramified of genus 2), the invariant 6 is realized by the 6 simple branch points of the non-Galois 3-sheeted colour-cubic projection ($R = 12$) and the 6 Weierstrass points fixed per transposition in $S_5$ ($60 = 6 \\times 10$).",
    },
  ],
});
