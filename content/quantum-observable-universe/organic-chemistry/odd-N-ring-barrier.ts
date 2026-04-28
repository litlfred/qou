import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:odd-N-ring-barrier",
  title:
    "Odd-$N$ ring closure barrier from $T(2, N)$ torus knot",
  tags: [
    "odd-N",
    "ring-closure",
    "barrier",
    "torus-knot",
    "alexander-polynomial",
    "non-aromatic",
  ],
  lean: { ref: "qou:QOU.Organic.oddNRingBarrier",
    validation: "not_checked",
  },
  uses: [
    "def:torus-knot-T2-odd-alexander",
    "prop:ring-closure-barrier-quantitative",
    "prop:molecular-crossing-quantum",
  ],
  cites: [],
});
