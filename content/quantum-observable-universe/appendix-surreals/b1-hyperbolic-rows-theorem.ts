import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:b1-hyperbolic-rows-theorem",
  title:
    "B1 conditionally reduces to Volume Conjecture at Borromean rings, Whitehead link, and twist knots",
  lean: {
    ref: "qou:QOU.AppendixSurreals.B1HyperbolicRowsTheorem.b1_hyperbolic_rows",
    validation: "not_checked",
  },
  uses: ["prop:b1-torus-knot-rows-theorem"],
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
    "graded-mikusinski",
  ],
});
