import { remark } from "../../schema/builders";

export default remark({
  label: "rem:coulomb-charge-channels",
  title: "The Coulomb charge in the channel decomposition of the crossing energy",
  interprets: "def:coulomb-charge",
  tags: ["coulomb", "crossing-energy"],
  uses: [
    "def:coulomb-charge",
    "def:crossing-energy",
    "prop:crossing-energy-decomposition",
    "conj:sm-hypercharge-invariant",
  ],
});
