import { proposition } from "../../schema/builders";

/**
 * The provable core of the jet-filtration binding: it is EXTENSIVE — a finite
 * sum of non-negative body-order terms, hence monotone (and strictly increasing
 * when a body-order contributes positively) in the body-order cutoff A. This is
 * the property the intensive rotation-phase θ_λ route structurally lacked.
 * Lean sorry-free (QOU.Mass.jetBinding_mono / jetBinding_lt_succ).
 */
export default proposition({
  label: "prop:jet-filtration-binding-extensive",
  title: "The jet-filtration binding is extensive (monotone in body order)",
  lean: {
    ref: "qou:QOU.Mass.jetBinding_mono",
    validation: "not_checked",
  },
  uses: [
    // conj:binding-manybody-eq-jet-filtration removed (qou-tm3c): the claim is monotonicity of a finite non-negative sum; the conjecture only names B.
  ],
  tags: [
    "binding",
    "jet-filtration",
    "extensive",
    "na-stokes",
    "reeb",
    "body-order",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): (see the failed\none-parameter closure in `probe_full_theta_binding.py`)\n\nform `prop:sw-period-residue-sum`)\n\nit is axiomatised as the §3b conjecture class\n`QOU.Mass.NaStokesKeystone.ProlongationPeriodMeanQuantumDim`, which has no\ninstance.\n\n[`2026-08-29-jet-filtration-three-inputs-corpus-grep.md`](" },
  ],
});
