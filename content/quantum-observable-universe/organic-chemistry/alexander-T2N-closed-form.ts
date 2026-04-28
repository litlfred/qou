import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:alexander-T2N-closed-form",
  title:
    "Closed form of $\\Delta_{T(2,N)}(q)$",
  tags: [
    "alexander-polynomial",
    "torus-link",
    "T2N",
    "closed-form",
    "threading",
  ],
  lean: { ref: "qou:QOU.Organic.alexanderT2NClosedForm",
    validation: "not_checked",
  },
  uses: ["def:threading-link"],
  cites: [],
});
