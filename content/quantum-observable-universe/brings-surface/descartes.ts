import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:descartes",
  lean: { ref: "qou:QOU.Archimedean.descartes",
    validation: "not_checked",
  },
  title: "Descartes theorem",
  tags: ["archimedean-universe", "terminal-object", "brings-surface"],
  uses: [
    "prop:brings-is-qou",
    "prop:genus-maximal-descent",
  ],
  proofs: ["prf:descartes"],
});
