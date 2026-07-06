import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:lqg-entropy-qdim-partition-pole",
  title: "Horizon entropy as the $q$-dimension partition-function pole",
  lean: {
    ref: "qou:QOU.GravitySpacetime.LQGEntropyQDimPartitionPole",
  },
  uses: [
    "prop:reeb-u1-chart-swap",
    "def:projective-line-object",
    "prop:three-parameters-wedderburn",
  ],
  cites: [
    "domagala-lewandowski-2004",
    "meissner2004",
    "ashtekar-baez-corichi-krasnov-1998",
  ],
});
