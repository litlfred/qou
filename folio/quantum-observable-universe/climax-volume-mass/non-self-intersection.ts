import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:non-self-intersection",
  lean: { ref: "qou:QOU.Braiding.non_self_intersection",
    validation: "not_checked",
  },
  title: "Obstruction to self-intersection",
  authorNotes: [
    { kind: "note", body: "Archimedean specialisation over R (§7c)." },
    {
      kind: "note",
      date: "2026-08-23",
      body:
        "**A sibling `.lean` was shadowing the declaration this ref names** " +
        "(bean `qou-lo1t`). `lean.ref` names " +
        "`QOU.Braiding.non_self_intersection`, which exists in the library and " +
        "states the block's actual claim — for every threshold `M` there is a " +
        "separation `ε` below which the categorical Möbius energy exceeds `M`, " +
        "i.e. the energy diverges at self-intersection. Resolution took the " +
        "sibling `non-self-intersection.lean` first, which declared no such " +
        "theorem: a `NonSelfIntersection` structure (one of three unrelated " +
        "types sharing that name) plus `noncocomm_iff_quantum`, returning its " +
        "own `noncocomm_pos` field. Sibling deleted per §0a.",
    },
    {
      kind: "caveat",
      date: "2026-08-23",
      body:
        "Two things worth recording about what the deleted sibling contained. " +
        "Its theorem was named `noncocomm_iff_quantum` and contained no `iff`: " +
        "it returned positivity unconditionally, so the `q ≠ 1` regime played " +
        "no part. And its structure asserted `0 < energy` and `0 < noncocomm` " +
        "as separate fields while relating them by nothing — so the mechanism " +
        "the block is about, non-cocommutativity *producing* the energy " +
        "barrier, was absent from the type. The library target states the " +
        "divergence directly and is the better home; it remains a §3b-cond " +
        "context-class projection (`:= ctx.claim_energy_diverges M`), i.e. the " +
        "claim is stated and assumed, not derived.",
    },
  ],
  tags: ["self-avoidance", "r-matrix", "non-cocommutativity", "knot-energy"],
  uses: [
    "prop:mobius-energy",
    "rem:r-matrix-braiding",
  ],
  proofs: ["prf:non-self-intersection"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/non-self-intersection-0.svg", blockIndex: 0, hash: "5471f3de17cb" },
  ],
});
