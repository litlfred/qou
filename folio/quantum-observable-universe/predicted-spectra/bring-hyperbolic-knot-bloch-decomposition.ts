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
    {
      kind: "status",
      body:
        "**Open structural sub-conjecture.** This is the K-theoretic identification required to inhabit the typeclass [`QOU.Archimedean.BringZeroModeBlochClass`](em-coupling-bring-zero-mode.lean) from [prop:em-coupling-bring-zero-mode](#prop:em-coupling-bring-zero-mode). The statement is a concrete, falsifiable prediction once the '$S_5$-equivariantly embeddable' condition is made precise. The proof attempt below establishes (i) the relevant field structure unconditionally, (ii) the figure-8 contribution as a worked classical sub-piece, and (iii) the irreducible open problem.",
    },
    {
      kind: "note",
      date: "2026-11-19",
      body: "Lean declaration inventory moved from prose (`bring-hyperbolic-knot-bloch-decomposition.lean`): `r2Cyclotomic`, `r2_zeta3_eq_one`, `r2_zeta4_eq_one`, `r2_zeta5_eq_two`, `r2_zeta12_eq_two`, `r2_zeta15_eq_four`, `r2_zeta60_eq_eight`, `compositum_rank_decomposition_narrow`, `compositum_rank_decomposition_full`, `bring_zero_mode_value_positive`, `bring_zero_mode_value_ne_zero`, `BringHyperbolicDecomposition`, `bring_hyperbolic_decomposition`, `BWQIndependence cl2_pi_3 cl2_pi_4`, and `two_knot_decomposition_insufficient`. Cross-file and witness pointers moved from Observations 4–5: `ew-interface-knot`, `conj:categorical-higgs-mechanism`, `prop:knot-operator-lp-selection`, and `computations/knot-operator-table.witness.json`.",
    },
  ],
});
