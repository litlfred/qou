import { remark } from "../../schema/builders";

export default remark({
  label: "rem:crystal-probe-q",
  title: "Crystal-lattice probe of $q$",
  uses: ["prop:local-substrate-q", "def:q-torsion-leaf", "def:q-harmonic-form"],
  tags: ["crystal", "substrate", "observation"],
});
