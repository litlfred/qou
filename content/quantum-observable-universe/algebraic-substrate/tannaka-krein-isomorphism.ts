import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:tannaka-krein-isomorphism",
  title: "Tannaka--Krein duality for the substrate",
  lean: {
    decl: "QOU.AlgebraicSubstrate.tannaka_krein_isomorphism",
    validation: "not_checked",
  },
  uses: [
    "def:frobenius-hopf-substrate",
    "def:categorical-reeb-derivation",
    "def:local-cohomology-group",
  ],
  tags: [
    "tannaka-krein",
    "duality",
    "representation",
    "quantum-group",
    "reconstruction",
  ],
  cites: ["reshetikhin1991"],
});
