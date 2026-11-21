import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:categorical-mass-markov",
  label: "rem:markov-trace-gibbs-free-energy",
  title:
    "Binding as a free-energy difference: the Markov trace in the partition-function slot",
  tags: [
    "markov-trace",
    "gibbs-state",
    "free-energy",
    "information",
    "channel-entropy",
  ],
  uses: ["prop:categorical-mass-markov"],
  cites: ["jones1987", "orellana1998"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): `QOU.Mass.FreeEnergyReadingIsSigned`;\n`the_free_energy_reading_has_no_energy_spectrum_probe.py`. The identification" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): At the opposite end, the per-crossing information rate is bounded by the operational entropy $\\eta_q$ of the [fibre channel capacity](#rem:fibre-channel-capacity). Thus, a braid's information content (and the free energy available to channel reweighting) grows at most linearly in its crossing number." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): See [the free-energy reading](#rem:bond-log-ratio-is-a-free-energy)." },
  ],
});
