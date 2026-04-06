import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:descartes",
  lean: {
    decl: "QOU.Descartes.descartes",
    validation: "not_checked",
  },
  title: "Descartes theorem",
  tags: ["descartes-universe", "terminal-object", "brings-surface"],
  uses: [
    "prop:brings-is-qou",
    "prop:genus-maximal-descent",
  ],
  proofs: ["prf:descartes"],
});
