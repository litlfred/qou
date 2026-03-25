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
    "def:descartes-condition",
    "def:brings-surface",
    "prop:brings-is-qou",
    "thm:qu-to-qou",
    "prop:genus-maximal-descent",
  ],
  proofs: ["prf:descartes"],
});
