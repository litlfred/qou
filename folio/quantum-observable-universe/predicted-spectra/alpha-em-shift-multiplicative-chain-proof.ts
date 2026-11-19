import { proof } from "../../schema/builders";

export default proof({
  label: "prf:alpha-em-shift-multiplicative-chain",
  title: "Proof of alpha em shift multiplicative chain",
  uses: ["prop:alpha-em-shift-multiplicative-chain"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body: "Witness provenance moved from prose: 50-dps mpmath check in `computations/alpha/alpha-em-shift-multiplicative-chain.witness.json`, reading upstream values from `computations/alpha/alpha-shift-torus.witness.json`.",
    },
  ],
});
