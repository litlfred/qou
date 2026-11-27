import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:local-aether-q",
  label: "rem:crystal-probe-q",
  title: "Crystal-lattice probe of $q$",
  uses: [
    "prop:local-aether-q",
    "ex:q-torsion-leaf",
  ],
  tags: ["crystal", "substrate", "observation"],
});
