import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:b1-hyperbolic-rows-theorem",
  title:
    "B1 at additional hyperbolic-knot rows (Borromean, Whitehead, twist knots) is theorem-level",
  lean: {
    ref: "qou:QOU.AppendixSurreals.B1HyperbolicRowsTheorem.b1_hyperbolic_rows",
    validation: "not_checked",
  },
  uses: [
    "conj:gb-depth-period-correspondence",
    "prop:depth-2-identification-bloch-suslin",
    "prop:borel-partial-resolution",
    "prop:b1-figure-8-row-theorem",
    "prop:b1-torus-knot-rows-theorem",
    "prop:b1-soft-sharpness-theorem",
    "rem:bring-embeddable-knots",
  ],
  cites: [
    "murakami-murakami2001",
    "bloch2000",
    "suslin1991",
    "thurston1978",
  ],
  tags: [
    "B1-discharge",
    "borromean-rings",
    "whitehead-link",
    "twist-knots",
    "volume-conjecture-discharged",
    "van-der-veen",
    "theorem-level",
    "graded-mikusinski",
  ],
});
