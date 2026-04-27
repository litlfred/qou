import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:schur-weyl-mass-decomposition",
  label: "rem:q-character-closes-parity-gap",
  title:
    "Symbolic Hecke $q$-character via Hoefsmit seminormal form distinguishes proton from neutron",
  tags: [
    "hecke-character",
    "hoefsmit",
    "seminormal",
    "q-deformation",
    "proton-neutron",
    "parity",
  ],
  uses: ["rem:mn-classical-parity-blind"],
});
