import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:pontryagin-dual-coxeter-character",
  proofs: ["prf:pontryagin-dual-coxeter-character"],
  title:
    "Pontryagin self-duality on abelianised Coxeter group $S_n^{\\mathrm{ab}} \\cong \\mathbb{Z}/2$",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.PontryaginDualCoxeterCharacter",
    validation: "not_checked",
  },
  uses: [
    "def:hecke-normal-form",
    "def:bar-involution",
  ],
  cites: [
    "pontryagin1934",
    "hewitt-ross1979",
  ],
  tags: [
    "pontryagin",
    "duality-d20",
    "abelianised-coxeter",
    "character-measure",
    "low-priority",
    "non-abelian-restriction",
    "closure-tier-a",
    "phase-1-discharge",
  ],
});
