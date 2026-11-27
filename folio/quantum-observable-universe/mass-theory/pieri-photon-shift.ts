import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:pieri-photon-shift",
  title:
    "Multiplication by a degree-one Hecke element is a non-commutative Fourier shift (Pieri rule)",
  lean: {
    ref: "qou:QOU.StandardModel.Photon.pieri_one_box_shift",
    validation: "not_checked",
  },
  uses: ["lem:degree-one-braid-trivial-volume", "def:photon"],
  cites: ["fulton1997", "kassel1995"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-23",
      body:
        "**Lean closed 2026-11-23.** The 2026-11-21 caveat said the containment was stated with an honest `sorry` over an " +
        "abstract `PieriInterface` that could not be proved. `pieri_one_box_shift` is now proved, sorry-free, for every " +
        "$m$ and every partition: it re-exports `QOU.SchurWeyl.SeminormalRep.pieri_support`, which derives the rule from the " +
        "seminormal branching (`compress_seminormalRep_heckeIncl`). It covers case 2 up to the restriction to " +
        "$V_\\square^{\\otimes(n+1)}$; the three-row component vanishing there is the Schur–Weyl step of the narrative proof. " +
        "Case 1 is `commute_photon_of_commute` (and `supportedOn_mul_left`). The $a = n$ case stays out of scope, as the statement says.",
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
