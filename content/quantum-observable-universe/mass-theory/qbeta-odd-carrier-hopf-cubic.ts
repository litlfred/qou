import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:q-beta-c-k-recursion-from-habiro-q-difference",
  label: "rem:qbeta-odd-carrier-hopf-cubic",
  title:
    "The $\\mathfrak{Q}_\\beta$ odd-channel obstruction is an irreducible cubic in the trace variable, sourced by the Hopf (double-crossing) sector",
  uses: ["prop:q-beta-c-k-recursion-from-habiro-q-difference"],
  computation: {
    engine: "python",
    script:
      "computations/qbeta/qbeta_odd_carrier_sector_decomposition.py",
    witness:
      "computations/qbeta/qbeta-odd-carrier-sector-decomposition.witness.json",
    status: "verified",
  },
  tags: [
    "q-beta",
    "precision-ladder",
    "c-3",
    "odd-channel",
    "structural",
    "no-fit",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-07-07",
      body: "Lean certificate (sorry-free, `lean`-direct exit 0): [`QBetaZeta4ResidueRefutation.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/QBeta/QBetaZeta4ResidueRefutation.lean) — `numOdd_at_phi4_root` (Φ₄ ∤ num, ζ₄-residue absent), `R12_eq_cubic_trace` (trace-cubic reduction), `cubicC_sector_decomp` + `cubicC_Hopf_rrt_candidates_all_nonzero` (Hopf-sector cubic, irreducible). Structural/exclusion certificate, not a c_3 value; nothing wired, no registry tier change (flip-flop guard, `ck-dk-canonical-registry.md` §8). Full audit: [`2026-07-07-zeta4-residue-lean-certificate-and-surviving-cubic.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-07-07-zeta4-residue-lean-certificate-and-surviving-cubic.md).",
    },
  ],
});
