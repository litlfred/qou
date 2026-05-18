import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:substrate-self-duality",
  title: "Self-duality of the algebraic substrate",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.substrate_self_duality",
    validation: "not_checked",
  },
  uses: ["def:rigid-dualizing-complex"],
  cites: ["yekutieli2015", "kock2004"],
  tags: ["self-duality", "frobenius", "dualizing-complex"],
});
