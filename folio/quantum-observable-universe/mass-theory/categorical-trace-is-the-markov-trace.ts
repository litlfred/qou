import { remark } from "../../schema/builders";

export default remark({
  label: "rem:categorical-trace-is-the-markov-trace",
  title: "The rigid trace of the tensor representation is the Markov trace",
  interprets: "prop:markov-trace-frobenius-selection",
  lean: { ref: "qou:QOU.MassTheory.qtrace_rHecke_div", validation: "not_checked" },
  uses: [
    "prop:markov-trace-frobenius-selection",
    "rem:trace-ledger",
    "def:chern-character",
    "def:grothendieck-group-of-a-qou",
  ],
  cites: ["jones1987", "reshetikhin-turaev1990", "kassel1995"],
  tags: ["markov-trace", "quantum-trace", "rigid-trace", "convention-d", "hecke-algebra", "trace"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): this is the identity `qtrace_rHecke_div` of the Lean file named in the manifest." },
    {
      kind: "status",
      date: "2026-09-15",
      body:
        "Part of the 2026-09-15 explicit-layer selection (owner option B). Closes the ledger item \"rigid trace versus Markov trace\" of `rem:trace-ledger`: the Markov trace at the convention-D parameter is the rigid (quantum) trace of the tensor representation normalised by `dim_q(V)^n`. The one-generator value `Tr(K Ř)/(1+q²)² = q³/(q²+1) = z_D` is `QOU.MassTheory.qtrace_rHecke_div` (TensorPictureGenerator.lean, sorry-free); the tower-level statement is `prop:markov-trace-frobenius-selection` itself, whose weights `[n−2k+1]_q/[2]_q^n` are the quantum dimensions of the irreducible summands of `V^{⊗n}` over `[2]_q^n`.",
    },
  ],
});
