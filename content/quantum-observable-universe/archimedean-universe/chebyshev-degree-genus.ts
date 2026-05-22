import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:chebyshev-degree-genus",
  lean: { ref: "qou:QOU.Descartes.chebyshev_degree_genus",
    validation: "not_checked",
  },
  title: "Chebyshev degree equals Seifert genus for $T_{2,p}$",
  tags: ["chebyshev", "seifert-genus", "torus-knot", "hecke-recurrence"],
  uses: [],
  proofs: ["prf:chebyshev-degree-genus"],
});
