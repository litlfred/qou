import { proposition } from "../../schema/builders";

export default proposition({
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
