import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:ccg-crossed-module-structure",
  lean: { ref: "qou:QOU.LiftingDescent.ccg_crossed_module_structure",
    validation: "not_checked",
  },
  title: "Crossed-module structure on $(\\mathrm{SU}_{q_n}(2), \\mathcal{O}_M^{\\times})$",
  tags: ["crossed-module", "central-extension", "peiffer-identity", "gerbe-band"],
  uses: [],
  proofs: ["prf:ccg-crossed-module-structure"],
  cites: ["yekutieli2014-descent"],
});
