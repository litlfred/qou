import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-meson",
  title: "Meson",
  tags: ["meson", "hadron", "knot", "categorical", "quark-antiquark"],
  lean: { ref: "qou:QOU.Torsion.CategoricalMeson",
    validation: "not_checked",
  },
  uses: [
    // A meson IS a valence-2 hadron; the definition is stated in these terms.
    "def:hadron",
    "def:quark-antiquark-production",
    // Establishes L_+ / L_-, which the crossing-pair table uses unexplained.
    "sec:knot-notation-convention",
  ],
});
