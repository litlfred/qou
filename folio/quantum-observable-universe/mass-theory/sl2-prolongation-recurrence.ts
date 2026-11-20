import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:sl2-prolongation-recurrence",
  lean: {
    ref: "qou:QOU.Mass.sl2_prolongation_recurrence",
    validation: "validated",
  },
  title: "Symplectic prolongation (det B = 1) gives a one-parameter recurrence",
  uses: [
    "prop:prolonged-periods-fixed-depth",
    "prop:sw-period-residue-sum",
    "prop:sl2-period-conserved-quantity",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): is proved for every $n$ in the Lean sibling." },
    {
      kind: "refined-framing",
      date: "2026-08-29",
      body:
        "Scoped to $n \\le 4$. An earlier version of this block ended \"pinning " +
        "$\\theta$ is the last open number of the depth correspondence, and is " +
        "solvable from three residue weights via " +
        "$\\tau = (a_D^{(2)} + a_D^{(4)})/a_D^{(3)}$\". Both halves are withdrawn. " +
        "The premise is false: $a_D^{(n)} = S(n)/n$ is a closed form for every $n$, " +
        "so no number was open there. And the identity offered is the $n = 2$ " +
        "instance of the block's own recurrence rearranged, so the $n = 4$ " +
        "agreement it produces is true by construction rather than a test. The " +
        "$\\det B = 1$ symplectic argument and the Lean implication are untouched.",
      see: "docs/audits/2026-06-25-sw-jet-prolongation-explicit-and-fork.md",
    },
  ],
  proofs: ["prf:sl2-prolongation-recurrence"],
});
