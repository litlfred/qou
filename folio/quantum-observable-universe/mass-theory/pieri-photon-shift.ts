import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:pieri-photon-shift",
  title:
    "Multiplication by a degree-one Hecke element is a non-commutative Fourier shift (Pieri rule)",
  lean: {
    ref: "qou:QOU.SchurWeyl.SeminormalRep.pieri_support",
    validation: "not_checked",
  },
  uses: ["lem:degree-one-braid-trivial-volume"],
  cites: ["fulton1997", "kassel1995"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-18",
      body:
        "**Rewritten 2026-11-18.** The Lean was an axiomatised `PieriInterface` class whose theorem returned " +
        "its own field. It is replaced by `QOU/SchurWeyl/PieriSupport.lean`, which proves the rule for every " +
        "partition and every $m$ from the seminormal branching (`compress_seminormalRep_heckeIncl`), " +
        "sorry-free. The old statement also listed $\\lambda - \\square$; that was the second addable box " +
        "$(\\lambda_1, \\lambda_2 + 1)$ under a spin relabelling, not a removal, and a product never removes a box.",
    },
  ],
  tags: [
    "pieri-rule",
    "non-commutative-fourier",
    "young-diagrams",
    "hecke-algebra",
    "photon",
    "raising-lowering-operator",
  ],
});
