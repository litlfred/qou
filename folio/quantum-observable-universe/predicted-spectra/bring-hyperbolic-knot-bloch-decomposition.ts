import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:bring-hyperbolic-knot-bloch-decomposition",
  title:
    "Bloch-group decomposition of $2/(3\\pi)$ from $S_5$-equivariantly embeddable hyperbolic knots in Bring's surface",
  uses: [
    "prop:em-coupling-bring-zero-mode",
    "rem:figure-8-archimedean-illustration",
  ],
  cites: [
    "suslin1991",
    "bloch2000",
    "thurston1978",
    "borel1974",
    "zagier1986",
    "kashaev1997",
    "murakami-murakami2001",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
  tags: [
    "tier:E",
    "bloch-group",
    "borel-regulator",
    "k-theory",
    "brings-surface",
    "hyperbolic-knot",
    "bloch-wigner",
    "alpha-em",
    "fine-structure-constant",
    "cyclotomic-field",
    "structural-sub-conjecture",
  ],
  lean: {
    ref: "qou:QOU.Archimedean.bring_hyperbolic_decomposition",
    validation: "not_checked",
  },
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Electron ruling (owner, 2026-11-21): relabelled the electron from the trefoil T_{2,3} to the word sigma_0 sigma_1 sigma_0 in B_3 (closure: Hopf link). Wording only; no number moved. The row previously read e^- = sigma_1^3 with closure the trefoil; the word sigma_0 sigma_1 sigma_0 closes to the Hopf link (ElectronWordCandidates.numCycles_s0s1s0). The sentence 'No basis element closes to a hyperbolic knot' still holds." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean file [`bring-hyperbolic-knot-bloch-decomposition.lean`](bring-hyperbolic-knot-bloch-decomposition.lean) formalizes the algebraic constraints:\n\n- `r2Cyclotomic` — $r_2(\\mathbb{Q}(\\zeta_n)) = \\varphi(n)/2$.\n- `r2_zeta3_eq_one`, `r2_zeta4_eq_one`, `r2_zeta5_eq_two`, `r2_zeta12_eq_two`, `r2_zeta15_eq_four`, `r2_zeta60_eq_eight` — concrete values.\n- `compositum_rank_decomposition_narrow` — $r_2(\\mathbb{Q}(\\zeta_{15})) = r_2(\\mathbb{Q}(\\zeta_3)) + r_2(\\mathbb{Q}(\\zeta_5)) + 1$.\n- `compositum_rank_decomposition_full` — $r_2(\\mathbb{Q}(\\zeta_{60})) = r_2(\\mathbb{Q}(\\zeta_{15})) + r_2(\\mathbb{Q}(\\zeta_4)) + 3$.\n- `bring_zero_mode_value_positive`, `bring_zero_mode_value_ne_zero` — analytic bounds on $2/(3\\pi)$.\n- `BringHyperbolicDecomposition` — typeclass axiomatizing the finite multi-set $\\{(K_i, n_i)\\}$.\n- `bring_hyperbolic_decomposition` — conditional theorem proving `BringZeroModeBlochClass` given the decomposition instance.\n- `BWQIndependence cl2_pi_3 cl2_pi_4` — typeclass axiomatizing the linear independence of $\\{2/(3\\pi), \\mathrm{Cl}_2(\\pi/3), \\mathrm{Cl}_2(\\pi/4)\\}$ over $\\mathbb{Q}$.\n- `two_knot_decomposition_insufficient` — lemma establishing that no $\\mathbb{Z}$-linear combination of $D[Z_{4_1}]$ and $D[Z_{\\mathcal{B}_3}]$ equals $2/(3\\pi)$." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ([`knot-operator-lp-selection`](../mass-theory/knot-operator-lp-selection.md), [`knot-operator-table.witness.json`](../../../computations/knot-operator-table.witness.json))" },
    {
      kind: "status",
      body:
        "**Open structural sub-conjecture.** This is the K-theoretic identification required to inhabit the typeclass [`QOU.Archimedean.BringZeroModeBlochClass`](em-coupling-bring-zero-mode.lean) from [prop:em-coupling-bring-zero-mode](#prop:em-coupling-bring-zero-mode). The statement is a concrete, falsifiable prediction once the '$S_5$-equivariantly embeddable' condition is made precise. The proof attempt below establishes (i) the relevant field structure unconditionally, (ii) the figure-8 contribution as a worked classical sub-piece, and (iii) the irreducible open problem.",
    },
  ],
});
