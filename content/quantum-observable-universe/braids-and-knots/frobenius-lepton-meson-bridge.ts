import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "While the underlying branching rule $V_{(2,1)} \\downarrow V_{(2)} \\oplus V_{(1,1)}$ is standard representation theory (derived from the Pieri / Littlewood-Richardson rule), the mathematical novelty here lies in its formal topological application: lifting a strictly representation-theoretic branching into a geometric constraint on the observable mass spectrum, and demonstrating that the physical entanglement of lepton channels uniquely maps to the single mass-carrying partition of the meson sector." },
  ],
  label: "prop:frobenius-lepton-meson-bridge",
  title:
    "Frobenius restriction: $V_{(2,1)} \\!\\downarrow_{H_2} = V_{(2)} \\oplus V_{(1,1)}$",
  lean: { ref: "qou:QOU.BraidsAndKnots.standard_restricts_to_both_leptons" },
  uses: ["prop:c-equals-bar-iff-all-1dim"],
  cites: [
    "wenzl1988c",
    "jones1987",
  ],
  tags: [
    "frobenius-reciprocity",
    "branching",
    "lepton",
    "meson",
    "standard-representation",
    "entanglement",
    "hoefsmit",
  ],
});
