import { proposition } from "../../schema/builders";

/**
 * Neutron-proton mass splitting from quark crossing change.
 */
export default proposition({
  label: "prop:neutron-proton-splitting",
  authorNotes: [
    {
      kind: "note",
      body: "Computational witnesses: computations/m-p-substrate-identity-50dps.witness.json, two-term-qed-isotope-and-nucleon-compute.witness.json, qbeta/qbeta-wedderburn-phase-twoterm-pin.witness.json.",
    },
    {
      kind: "status",
      date: "2026-11-15",
      body:
        "**CODATA comparison moved out of Lean (owner decision, bean " +
        "`neutron_proton_splitting`).** The Lean theorem now states only the " +
        /* <!-- literal-source: historical rounded 4-digit convention-C product 3.7449 * 0.3476 = 1.30172724 --> */
        "model value `α·|Φ(udd) − Φ(uud)| = 3.7449·0.3476 = 1.30172724`; the " +
        "CODATA-tolerance conjunct and `codataNeutronProtonSplittingMeV` are " +
        "removed. The comparison (+0.65 % vs CODATA 2022 1.29333378 MeV; the " +
        "old prose said 0.63 % and the old Lean said 0.68 % against the " +
        "rounded 1.293) is in the block's comparison paragraph.",
    },
    {
      kind: "status",
      date: "2026-11-15",
      body:
        "**Convention C replaced by convention D (owner ruling 2026-11-15: " +
        "replace convention-C values with convention D even if worse).** The " +
        "Phi pins were computed with z = 4993/10000 (rounded convention-C " +
        "sqrt(q)/(q+1)). Recomputed at 50 dps with z = q^3/(q^2+1) at the " +
        "proton q0, all-pairs strand reading of level1-qvalues.py: " +
        "Phi(uud) = -0.6148859839, Phi(udd) = -0.8963949769, |dPhi| = " +
        "0.2815089929, model value 1.0542 MeV, -18.49 % vs CODATA 2022. The " +
        "adjacent-crossing reading (pn_splitting_proof_provenance_probe.py) " +
        "gives -2.875 % under D but does not reproduce the old neutron value, " +
        "so the all-pairs reading is kept. The C figure (+0.65 %) stays in " +
        "the prose only as a labelled historical comparison.",
    },
    {
      kind: "status",
      date: "2026-08-14",
      body:
        "**Lean carrier restructured — sorry-free (bean `qou-octr`, PR #5019).** " +
        "The flat exact-equality conjunct `m_n − m_p = α·|Φ(udd) − Φ(uud)|` was " +
        "refutable as written (`neutron_proton_splitting_unconstrained_false`) " +
        "and violated the §7ab approximation convention (the block claims ≈ " +
        "with tolerance, never exact =). Now: the corpus values of α, Φ(uud), " +
        "Φ(udd) are provenance-cited hypothesis pins " +
        "(`NeutronProtonSplittingNumerics`; provenance " +
        "`docs/audits/2026-07-11-quark-volume-provenance.md`), and the CODATA " +
        "agreement (0.68 % < 1 %) is derived from them by arithmetic, " +
        "lean-direct exit 0. Open remainder: port the exact closed-form " +
        "traced-volumes to Lean so the pins become theorems.",
    },
  ],
  lean: { ref: "qou:QOU.Torsion.neutron_proton_splitting", validation: "not_checked" },
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: [
      "computations/codata-2022-validation-masses.witness.json",
      "computations/m-p-substrate-identity-50dps.witness.json",
      "computations/two-term-qed-isotope-and-nucleon-compute.witness.json",
      "computations/markov-free-energy-qvalues.witness.json",
      "computations/catalan-binding.witness.json",
    ],
    status: "verified",
  },
  title: "Neutron--proton mass splitting",
  uses: ["thm:wedderburn-mass-formula"],
});
