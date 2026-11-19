import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:b1-hyperbolic-rows-theorem",
  title:
    "The depth correspondence conditionally reduces to the Volume Conjecture at Borromean rings, the Whitehead link, and twist knots",
  lean: {
    ref: "qou:QOU.AppendixSurreals.B1HyperbolicRowsTheorem.b1_hyperbolic_rows",
    validation: "not_checked",
  },
  uses: ["prop:b1-torus-knot-rows-theorem"],
  cites: [
    "murakami-murakami2001",
    "bloch2000",
    "suslin1991",
    "thurston1978",
  ],
  tags: [
    "B1-discharge",
    "borromean-rings",
    "whitehead-link",
    "twist-knots",
    "volume-conjecture-discharged",
    "van-der-veen",
    "graded-mikusinski",
  ],
  authorNotes: [
    {
      kind: "note",
      body:
        "Whitehead link volume and saddle squeeze in Lean: QOU.Archimedean.WhiteheadVolume.vol_L5a1_eq_half_vol_B3, vol_L5a1_eq_4_catalan, QOU.Knot.WhiteheadSaddle.saddle_integral, whitehead_vc_innerSum_half (WhiteheadSaddleClausen.lean), QOU.Knot.WhiteheadVC.whitehead_vc_of_saddle_value (WhiteheadVolumeConjecture.lean), and catalanG_eq_clausen_pi_div_two; index alignment for whitehead_volume_conjecture ((N-1)/2 vs floor(N/2)) is tracked in bean qou-1gkf. Supporting scripts and audit notes: computations/whitehead_c_sigma_hiprec.py, computations/one_loop_torsion.py, docs/audits/2026-07-26-whitehead-vc-verification-and-p-exponent.md, docs/audits/2026-08-02-whitehead-c-sigma-closed-form-2-pow-minus-3-4.md, docs/audits/2026-08-08-c-sigma-derivation-status.md, docs/audits/2026-08-08-per-cusp-factor-dissolves.md.",
    },
  ],
});
