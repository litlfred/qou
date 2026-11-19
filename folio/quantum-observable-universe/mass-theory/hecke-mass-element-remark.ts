import { remark } from "../../schema/builders";

export default remark({
  label: "rem:hecke-mass-element-remark",
  title: "Hecke-valuedness and descent splitting of the Hecke mass element",
  interprets: "def:hecke-mass-element",
  uses: [
    "def:hecke-mass-element",
    "def:mass-identity",
    "rem:hecke-algebra-from-braiding",
    "prop:descent-eigenspaces",
  ],
});
