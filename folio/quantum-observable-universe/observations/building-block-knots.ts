import { remark } from "../../schema/builders";

export default remark({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    {
      kind: "note",
      date: "2026-11-24",
      body: "Reconciled Tables 1, 3, and 5 (`qou-jbbk`) at 80-dps (`computations/homfly_skein_braid.py` specialized at $v = q, z = q^{1/2} - q^{-1/2}$ and `computations/q_parameter.py` `q_at(80) = 1.1099785827513808...`, proton anchor): removed the spurious $q^{1-g^2}$ shift from $5_1, 7_1, 9_1$, wrote out exact $T_{3,4}$ and $T_{3,5}$ polynomials, corrected Solomon link $L4a1$ volume from $\\approx 6.45$ to $0$, and aligned every $J(q_0)$ value in Table 5. Note: the unreferenced local definition `jones_cinquefoil` in `building-block-knots.lean:128` still carries the $q^{-3}$-shifted exponent pending Lean-unfreeze cleanup.",
    },
  ],
  interprets: "prop:torus-knot-generators",
  label: "rem:building-block-knots",
  title:
    "Building block knots: classification, polynomials, and volumes",
  tags: [
    "knot",
    "torus-knot",
    "jones-polynomial",
    "hyperbolic-volume",
    "particle",
    "classification",
    "building-block",
    "amphichiral",
    "mirror",
    "appendix",
  ],
  uses: ["def:antineutrino-knot"],
});
