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
  ],
});
