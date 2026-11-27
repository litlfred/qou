import { example } from "../../schema/builders";

export default example({
  label: "ex:nucleon-hecke-element-examples",
  title: "Proton and neutron Hecke elements",
  interprets: "def:nucleon-hecke-element",
  tags: ["nucleon", "proton", "neutron"],
  uses: [
    "def:nucleon-hecke-element",
    "def:typed-crossing-operator",
  ],
});
