import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:local-substrate-q",
  label: "rem:crystal-probe-q",
  title: "Crystal-lattice probe of $q$",
  uses: [
    "prop:local-substrate-q",
    "ex:q-torsion-leaf",
  ],
  tags: ["crystal", "substrate", "observation"],
});
