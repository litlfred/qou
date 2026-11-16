import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:partition-sum-proton-residual",
  title:
    "Proton tower residual = $m_e \\cdot \\mathrm{tr}_M(C_{\\mathrm{Frob}}) = m_e(2 + 1/[2]_q)$",
  lean: {
    ref: "qou:QOU.BraidKnot.proton_tower_residual_frobenius",
    validation: "not_checked",
  },
  uses: ["prop:schur-weyl-mass-decomposition"],
  computation: {
    engine: "python",
    script: "computations/proton_residual_rootcause.py",
    witness: [
      "computations/proton-residual-rootcause.witness.json",
      "computations/codata-masses.witness.json",
    ],
    status: "verified",
  },
  tags: [
    "proton",
    "residual",
    "frobenius",
    "co-casimir",
    "self-dual",
    "partition-sum",
    "hook-length",
    "mass-endomorphism",
    "gb-filtration",
  ],
  authorNotes: [
    { kind: "status", date: "2026-11-16", body: "Demoted from proposition on owner ruling 2026-11-16 (card \"Demote all six\"): the claim is not proved from established results, so it is stated as a conjecture. Label renamed conj:partition-sum-proton-residual -> conj:partition-sum-proton-residual." },
    {
      kind: "caveat",
      date: "2026-11-16",
      body: "Statement changed from '=' to '≈' for the CODATA comparison. Three problems: (1) the residual 1.2779 MeV is a recorded number, not CODATA minus the live tower mass (938.7228 MeV gives -0.451 MeV, opposite sign); (2) the classical (5/2) m_e matches better (0.03%) than the q-form (0.14%); (3) absolute nucleon mass is excised as a target (owner, 2026-08-11). The Lean theorem proves a numeric bound on hardcoded values and `invDimPartitionSum` is a stub returning 0. Queued for demotion to a remark or conjecture.",
    },
  ],
});
