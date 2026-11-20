import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:gb-filtration",
  title: "Gröbner–Shirshov length filtration",
  uses: [
    "prop:gb-spectral-sequence",
  ],
  computation: {
    engine: "python",
    script: "computations/gb_filtration_jet_tracker.py",
    witness: "computations/gb-filtration-jet-order.witness.json",
    status: "verified",
  },
  tags: [
    "mba",
    "step-7",
    "gb-filtration",
    "spectral-sequence",
    "length-grading",
    "canonical-chain",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "**$E_2$ collapse removed from this block (owner, 2026-11-20, bean `qou-6qbv`).** It was cited from `prop:gb-spectral-sequence`, which no longer asserts it; for the Hochschild complex of $H_3$ filtered by length, $d_2$ and $d_4$ are nonzero and the sequence stabilises at $E_5$ (`computations/probes/gb_spectral_sequence_h3_probe.py`, exact). The step only needed that the standard basis splits the length filtration, which is now what it cites. The witness `gb-filtration-jet-order.witness.json` never carried a $d_2$ certificate, although this appendix said it did." },
  ],
});
