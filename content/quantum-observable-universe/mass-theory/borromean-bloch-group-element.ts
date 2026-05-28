import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:borromean-bloch-group-element",
  title:
    "Borromean rings represent a non-trivial element of $K_3(\\mathbb{C})$ / Bloch group with regulator $r_2 = 8G$",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.BorromeanBlochGroupElement",
    validation: "not_checked",
  },
  uses: [
    "rem:quantum-bloch-group",
    "prop:kashiwara-jones-c4-categorical",
    "rem:kashaev-volume-density",
    "prop:vol-through-tau",
    "rem:vol-as-motivic-period",
    "prop:binding-scale-catalan",
    "prop:dilogarithm-archimedean-limit",
  ],
  cites: [
    "bloch2000",
    "neumann-zagier1985",
    "suslin1990",
    "zagier1986",
    "kashaev1997",
  ],
  tags: [
    "bloch-group",
    "k-theory",
    "duality-d16",
    "borromean",
    "regulator",
    "k3-c",
    "motivic-period",
    "h4-closure-route",
    "axiom-class",
    "open-problem",
    "conditional-on-class",
    "non-scholarly-voice-exception",
    "quantum-dilogarithm",
  ],
});
