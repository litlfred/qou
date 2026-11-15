import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:modular-s-transform-q-q-tilde",
  title:
    "Modular $S$-transform $q \\leftrightarrow \\tilde q = \\exp(-2\\pi i / \\tau)$ for Hecke parameter analytic continuation",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.ModularSTransformQQTilde",
    validation: "not_checked",
  },
  uses: [
    "def:bar-involution",
    "def:hecke-normal-form",
    "rem:vol-as-motivic-period",
  ],
  cites: [
    "garoufalidis2013",
    "kashaev1997",
    "neumann-zagier1985",
    "kashaev-tirkkonen2014",
  ],
  tags: [
    "tier:S",
    "modular-s-transform",
    "duality-d14",
    "q-tilde",
    "root-of-unity",
    "tqft",
    "axiom-class",
    "open-problem",
  ],
});
