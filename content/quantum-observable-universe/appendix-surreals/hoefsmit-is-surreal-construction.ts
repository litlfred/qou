import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hoefsmit-is-surreal-construction",
  proofs: ["prf:hoefsmit-is-surreal-construction"],
  lean: {
    ref: "qou:QOU.AppendixSurreals.hoefsmit_is_surreal_construction",
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
  uses: ["def:sign-sequence-of-braid"],
  cites: ["gonshor1986", "conway1976"],
});
