import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:su2-emergence-volume-determinant",
  lean: { ref: "qou:QOU.su2_emergence_volume_determinant",
    validation: "not_checked",
  },
  title: "Volume constraint forces $\\det(g_V) = 1$",
  tags: ["tannaka-krein", "volume-constraint", "determinant", "sl2"],
  uses: ["thm:su2-emergence"],
  proofs: ["prf:su2-emergence-volume-determinant"],
});
