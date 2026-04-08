import { definition } from "../../schema/builders";

export default definition({
  label: "def:nucleon-hecke-element",
  title: "Nucleon Hecke element",
  tags: [
    "nucleon",
    "proton",
    "neutron",
    "hecke-algebra",
    "normal-form",
    "borromean",
    "typed-crossing",
  ],
  lean: {
    decl: "QOU.Braiding.NucleonHeckeElement",
    validation: "not_checked",
  },
  uses: [
    "def:typed-crossing-operator",
    "def:borromean-baryon",
  ],
});
