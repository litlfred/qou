import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-meson",
  title: "Meson (categorical)",
  tags: ["meson", "hadron", "knot", "categorical", "quark-antiquark"],
  lean: { ref: "qou:QOU.Torsion.CategoricalMeson",
    validation: "not_checked",
  },
  uses: ["def:quark-antiquark-production"],
});
