import { remark } from "../../schema/builders";

export default remark({
  label: "rem:dressed-quark-heavier-flavors",
  title: "Heavier-flavor dressed masses unconstrained by the nucleon-doublet derivation",
  tags: ["flavor", "quark-mass", "strangelet", "heavy-quark"],
  interprets: "prop:flavor-dressed-mass-from-substrate-split",
  uses: ["thm:flavor-mass-splitting-bound"],
});
