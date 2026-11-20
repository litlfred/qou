import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:jet-prefix-transport",
  title: "Jet-prefix transport in the $q \\to 1$ limit",
  uses: [
    "prop:jet-prefix-gb-filtration",
    "prop:gb-spectral-sequence",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/gb_filtration_jet_order_reader.py",
    witness: "computations/gb-filtration-jet-order-reader.witness.json",
    status: "verified",
  },
  tags: [
    "mba",
    "step-8",
    "jet-order",
    "q-limit",
    "canonical-chain",
  ],
  authorNotes: [
    { kind: "caveat", date: "2026-11-20", body: "**Caveat (2026-11-20, bean `qou-6qbv`): the cited `prop:gb-spectral-sequence` no longer supplies $E_2$ collapse.** It was rewritten on the Coxeter length filtration and now states the Hochschild spectral sequence of $H_n(R, q)$; at $n = 3$ that sequence has $d_4 \\neq 0$ and stabilises only at $E_5$ (`computations/probes/gb_spectral_sequence_h3_probe.py`, exact). The step here that relies on $E_2$ collapse is therefore unsupported by its citation. Whether a different filtered object collapses at $E_2$ is not settled here." },
  ],
});
