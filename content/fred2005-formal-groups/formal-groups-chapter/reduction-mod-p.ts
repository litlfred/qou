import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:reduction-mod-p",
  title: "Reduction modulo $p$",
  lean: { ref: "fred2005:Fred2005.reduction_mod_p_commutative",
    validation: "not_checked",
  },
  tags: ["reduction", "formal-group", "commutative"],
  uses: ["def:non-commutative-formal-group"],
  cites: ["fred2005"],
});
