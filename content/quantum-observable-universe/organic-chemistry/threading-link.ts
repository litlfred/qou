import { definition } from "../../schema/builders";

export default definition({
  label: "def:threading-link",
  title: "Threading link $T(2,N)$",
  tags: [
    "threading",
    "torus-link",
    "T26",
    "alexander-polynomial",
    "molecular",
    "ring",
    "non-local",
    "correlated",
  ],
  lean: { ref: "qou:QOU.Organic.ThreadingLink",
    validation: "not_checked",
  },
  uses: ["def:molecular-hopf-chain"],
});
