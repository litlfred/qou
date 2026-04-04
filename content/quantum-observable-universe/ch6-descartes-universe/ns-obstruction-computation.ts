import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:ns-obstruction-computation",
  title:
    "Computation of the NS obstruction for the Descartes universe",
  uses: [
    "prop:ns-obstruction-tower",
    "def:ns-regular-qou",
    "thm:qu-to-qou",
    "prop:euler-char-stability",
    "prop:root-of-unity-truncation",
    "prop:core-levi-form",
    "conj:levi-degeneracy",
  ],
  tags: [
    "computation",
    "obstruction",
    "descartes",
    "euler-characteristic",
    "brings-surface",
  ],
});
