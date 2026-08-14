import { proposition } from "../../schema/builders";

/**
 * Neutron-proton mass splitting from quark crossing change.
 */
export default proposition({
  label: "prop:neutron-proton-splitting",
  authorNotes: [
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
  title: "Neutron--proton mass splitting",
  uses: ["thm:wedderburn-mass-formula"],
});
