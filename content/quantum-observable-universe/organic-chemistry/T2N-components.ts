import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:T2N-components",
  title: "Component count, writhe, and signature of $T(2,N)$",
  tags: [
    "torus-link",
    "T2N",
    "components",
    "writhe",
    "signature",
    "threading",
  ],
  lean: { ref: "qou:QOU.Organic.t2nComponents",
    validation: "not_checked",
  },
  uses: ["def:threading-link"],
  cites: [],
});
