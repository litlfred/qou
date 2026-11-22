import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "caveat", date: "2026-11-21", body: "Lean now states the containment with an honest `sorry`. The class field `support_subset`, which held the conclusion, is deleted (round-trip audit pass 2, C04). The narrative proof also misses the $a = n$ case and the third induced component, and mixes tower levels; see the audit doc." },
  ],
  label: "prop:pieri-photon-shift",
  title:
    "Multiplication by a degree-one Hecke element is a non-commutative Fourier shift (Pieri rule)",
  lean: {
    ref: "qou:QOU.Photon.pieri_one_box_shift",
    validation: "not_checked",
  },
  uses: ["lem:degree-one-braid-trivial-volume", "def:photon"],
  cites: ["fulton1997", "kassel1995"],
  tags: [
    "pieri-rule",
    "non-commutative-fourier",
    "young-diagrams",
    "hecke-algebra",
    "photon",
    "raising-lowering-operator",
  ],
});
