import { remark } from "../../schema/builders";

export default remark({
  label: "rem:schwinger-measure-unit-remark",
  title: "Rigidity and canonicity of the Schwinger measure unit",
  interprets: "def:schwinger-measure-unit",
  tags: ["schwinger", "measure"],
  uses: [
    "def:schwinger-measure-unit",
    "conj:schwinger-measure-computational-time",
    "prop:horizon-conformal-invariance",
    "def:boltzmann-constant",
  ],
});
