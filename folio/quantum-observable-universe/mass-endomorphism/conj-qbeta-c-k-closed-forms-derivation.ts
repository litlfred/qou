import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:qbeta-c-k-closed-forms",
  label: "rem:qbeta-c-k-closed-forms-derivation",
  title: "Convention-D generating-function derivations, quartic cumulant candidates, and historical Convention-C calibration record for the $c_k$",
  tags: ["qbeta", "precision-ladder", "ck-coefficients", "convention-d", "derivation-chain"],
  uses: ["conj:qbeta-c-k-closed-forms"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body: "Inadmissibility of $z = 1$ under Convention D is proved in `ConventionDAdmissibleRoots.lean`; the all-order Convention-D generating function, Lagrange–Bürmann radius $R_u \\approx 0.3690$, $N = 3$ Habiro–Kashiwara jet, and quartic cumulant candidates ($+1/6$ vs $+101/288$) are proved in `ConventionDAllOrderCkGeneratingFunction.lean`, `ConventionDC3AndTailSelectionDerivation.lean`, and `ConventionDC4QuarticCumulantDerivation.lean`.",
    },
  ],
  computation: {
    engine: "python",
    script: "computations/qbeta/qbeta_convention_d_all_order_ck_generating_probe.py",
    witness: [
      "computations/qbeta/qbeta-convention-d-all-order-ck-generating.witness.json",
      "computations/qbeta/qbeta-cos-resummation-d.witness.json",
    ],
    status: "verified",
  },
});
