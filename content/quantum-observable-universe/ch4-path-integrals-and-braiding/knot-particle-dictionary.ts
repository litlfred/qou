import { remark } from "../../schema/builders";

export default remark({
  label: "rem:knot-particle-dictionary",
  title: "Knot–particle dictionary",
  tags: ["knot", "particle", "dictionary", "mass", "borromean"],
  uses: [
    "def:localized-knot",
    "def:hadron",
    "conj:borromean-quark",
    "def:borromean-baryon",
  ],
});
