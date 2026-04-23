import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hoefsmit-is-surreal-construction",
  lean: {
    decl: "QOU.AppendixSurreals.hoefsmit_is_surreal_construction",
    validation: "not_checked",
  },
  title:
    "Hoefsmit seminormal form is Conway's $\\{L \\mid R\\}$ construction",
  tags: [
    "surreal-numbers",
    "hoefsmit",
    "hecke-eigenspace",
    "conway-construction",
    "L-R-split",
    "bridge",
  ],
  uses: [
    "prop:hoefsmit-seminormal-form",
    "def:sign-sequence-of-braid",
    "def:birthday-grading",
  ],
  cites: ["gonshor1986", "conway1976"],
});
