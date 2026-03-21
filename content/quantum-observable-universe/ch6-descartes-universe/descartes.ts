import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:descartes",
  title: "Descartes theorem",
  hasProof: true,
  tags: ["descartes-universe", "terminal-object", "brings-surface"],
  uses: [
    "def:descartes-condition",
    "def:brings-surface",
    "prop:brings-is-qou",
    "thm:qu-to-qou",
    "prop:genus-maximal-descent",
  ],
});
