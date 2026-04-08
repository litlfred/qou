import { definition } from "../../schema/builders";

export default definition({
  label: "def:typed-crossing-operator",
  title: "Typed crossing operator",
  tags: [
    "crossing",
    "quark",
    "hecke-algebra",
    "borromean",
    "flavor",
    "skein",
  ],
  lean: {
    decl: "QOU.Braiding.TypedCrossingOperator",
    validation: "not_checked",
  },
  uses: [
    "def:up-quark",
    "def:down-quark",
    "def:borromean-baryon",
    "rem:hecke-algebra-from-braiding",
  ],
});
