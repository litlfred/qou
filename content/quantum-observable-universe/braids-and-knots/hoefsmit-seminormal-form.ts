import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hoefsmit-seminormal-form",
  title:
    "Hoefsmit seminormal matrices as $R$-matrix evaluations in $H_n(q)$",
  lean: { ref: "qou:QOU.BraidKnot.hoefsmit_seminormal_form",
    validation: "not_checked",
  },
  uses: [
        "prop:figure-eight-bw-coefficients",
  ],
  cites: ["hoefsmit1974", "wenzl1988"],
  tags: [
    "hoefsmit",
    "seminormal",
    "r-matrix",
    "wedderburn-artin",
    "young-tableaux",
    "representation-theory",
  ],
});
