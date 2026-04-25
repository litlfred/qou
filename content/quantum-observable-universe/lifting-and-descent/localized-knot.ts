import { definition } from "../../schema/builders";

export default definition({
  label: "def:localized-knot",
  title: "Localized knot (knot at a point)",
  tags: ["knot", "point", "fibre", "categorical"],
  lean: { ref: "qou:QOU.LocalizedKnot",
    validation: "not_checked",
  },
  uses: [
    "def:categorical-point",
    "def:projective-line-object",
  ],
});
