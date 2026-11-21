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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): `QOU.Mass.FreeEnergyReadingIsSigned` proves the general statements:\n`minusSummand_neg`, `no_real_energy_for_minus_block`,\n`positivity_would_need_d_gt_inv_q`, `admissible_letters_nonpos`, the\npositive-but-signed pairing at each of the three letters, and\n`pn_blockSum_eq_h_delta_half`. Measured at $q_0$ in\n`the_free_energy_reading_has_no_energy_spectrum_probe.py`." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): (the normalisation is exact: `wPlus_add_wMinus` in `QOU.Mass.ChainTraceFactor`); $L_{pp} + L_{nn} = 2\\log[2]_q$ (all in `QOU.Mass.ChainTraceFactor`)." },
  ],
});
