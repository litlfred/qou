import { definition } from "../../schema/builders";

export default definition({
  label: "def:two-stage-garside",
  title:
    "Two-stage Garside construction in $H_{3A}(q)$",
  tags: [
    "garside-element",
    "hecke-algebra",
    "quark-level",
    "borromean",
    "confinement",
    "nuclear",
    "typed-crossing",
  ],
  lean: {
    decl: "QOU.Descartes.TwoStageGarside",
    validation: "not_checked",
  },
  uses: [
    "def:typed-crossing-operator",
    "def:typed-garside-element",
    "def:borromean-baryon",
    "prop:braiding-induced-ordering",
    "prop:confinement-lp",
  ],
});
