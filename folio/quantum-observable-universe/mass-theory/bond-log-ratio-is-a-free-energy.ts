import { remark } from "../../schema/builders";

/**
 * Q2 (owner decision, 2026-09-05). The canonical statement of what the bond
 * log-ratio L actually is: a free-energy difference over the Markov state sum,
 * exact and well defined. The separate claim B = alpha L, i.e. that this free
 * energy IS the nuclear binding energy, is marked here as an open
 * interpretation rather than a result, with the evidence against it.
 *
 * One block so there is one canonical place; the blocks that use the bond
 * constants point here rather than each restating the caveat.
 *
 * Identification and inventory: docs/audits/2026-09-04-what-L-is-and-what-
 * retiring-it-would-cost.md (bean qou-qnqf). Nothing is retracted and no
 * number changes: every L in the corpus remains a correct free energy.
 */
export default remark({
  interprets: "thm:markov-trace-factorization",
  label: "rem:bond-log-ratio-is-a-free-energy",
  title:
    "The bond log-ratio is a free-energy difference; that it is the binding energy is a separate, open claim",
  uses: [
    "thm:markov-trace-factorization",
    "rem:canonical-trace-factorises-over-chain",
    "rem:pn-bond-cannot-be-extremal",
  ],
  tags: [
    "mass-theory",
    "markov-trace",
    "binding-energy",
    "bond-constants",
    "free-energy",
    "open-problem",
    "draft",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Computational provenance: the_free_energy_reading_has_no_energy_spectrum_probe.py.",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: [
      "computations/hecke-channel-binding.witness.json",
      "computations/probes/uic_per_block_log_valley_scan_probe.witness.json",
      "computations/probes/the_free_energy_reading_has_no_energy_spectrum_probe.witness.json",
      "computations/meson/cut-entropy-is-A-independent.witness.json",
    ],
    status: "verified",
  },
});
