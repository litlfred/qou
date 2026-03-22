import { definition } from "../../schema/builders";

export default definition({
  label: "def:localized-knot",
  title: "Localized knot (knot at a point)",
  tags: ["knot", "point", "fibre", "categorical"],
  lean: {
    decl: "QOU.LocalizedKnot",
    validation: "not_checked",
  },
  status: "has_sorry",
  uses: [
    "def:categorical-point",
    "def:projective-line-object",
    "def:quantum-observable-universe",
  ],
});
