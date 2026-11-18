import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:partition-sum-proton-residual",
  title:
    "Proton tower residual compared with $m_e\\sum_{\\lambda\\vdash3}1/\\dim_q\\lambda = m_e(2 + 1/[2]_q)$",
  lean: {
    ref: "qou:QOU.BraidKnot.proton_tower_residual_frobenius",
    validation: "not_checked",
  },
  uses: ["prop:schur-weyl-mass-decomposition", "prop:h3-frobenius-casimir-markov-trace"],
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
    { kind: "caveat", date: "2026-11-18", body: "The integer 12 in m_p/m_e = 2(Vol(4_1)/hbar_q^2) F_Bor - 12 is a FIT: selected because 2 m_mu F_Bor(q_0) exceeds m_p by about 12 m_e (docs/audits/2026-05-25-proton-mass-identity-12-me-ocneanu.md, status: empirical near-identity, needs categorical proof). The Ocneanu -1/12 reading was retracted 2026-05-26; 12 = dim V_(2,1)*|S_3| = 2 F_Bor(1) are readings only. Owner ruling 2026-11-18 (card: label as fit). Derivation gap tracked in a bean." },
    { kind: "status", date: "2026-11-16", body: "Comparison rewritten against the live convention-D tower (issue #8118). The production identity m_p/m_e = 2(Vol(4_1)/hbar_q^2) F_Bor - 12 has tower 944.404 MeV; the residual is -12 m_e at the proton pin (by construction, since q_0 is solved from the identity) and -11.99955 m_e at the muon pin, where m_p = 938.271861 MeV (-244 ppb). The +1.278 MeV and -0.451 MeV residuals used the archived towers 936.994 and 938.7228 MeV, which no live producer reproduces; both are kept as records. No mass number changed." },
    { kind: "status", date: "2026-11-16", body: "Restated (issue #8094): the claim tr_M(C_Frob) = 2 + 1/[2]_q is false for the Frobenius Casimir of H_3(q) (prop:h3-frobenius-casimir-markov-trace); the conjecture now compares the residual with the formal sum. Residual sign recorded for both tower values on record. Tables 1 and 4 relabelled; no number changed." },
    { kind: "status", date: "2026-11-16", body: "Demoted from proposition on owner ruling 2026-11-16 (card \"Demote all six\"): the claim is not proved from established results, so it is stated as a conjecture. Label renamed conj:partition-sum-proton-residual -> conj:partition-sum-proton-residual." },
    {
      kind: "caveat",
      date: "2026-11-16",
      body: "Statement changed from '=' to '≈' for the CODATA comparison. Three problems: (1) the residual 1.2779 MeV is a recorded number, not CODATA minus the live tower mass (938.7228 MeV gives -0.451 MeV, opposite sign); (2) the classical (5/2) m_e matches better (0.03%) than the q-form (0.14%); (3) absolute nucleon mass is excised as a target (owner, 2026-08-11). The Lean theorem proves a numeric bound on hardcoded values and `invDimPartitionSum` is a stub returning 0. Queued for demotion to a remark or conjecture.",
    },
  ],
});
