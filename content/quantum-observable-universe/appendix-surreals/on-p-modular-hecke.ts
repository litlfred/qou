import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:on-p-modular-hecke",
  title:
    "Modular Hecke at $q = \\zeta_p$ corresponds to nimber surreals $\\mathbf{On}_p$",
  tags: [
    "surreal-numbers",
    "characteristic-p",
    "nimbers",
    "modular-hecke",
    "kazhdan-lusztig",
    "root-of-unity",
    "p-ary-fusion",
    "open-problem",
  ],
  uses: [
    "prop:hoefsmit-is-surreal-construction",
    "rem:algebraic-core-survives",
  ],
  cites: ["conway1976", "gonshor1986", "ehrlich2012"],
});
