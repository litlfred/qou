import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:tannaka-krein-isomorphism",
  title: "Tannaka--Krein duality for the substrate",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.IsTannakaKreinDual",
    validation: "not_checked",
  },
  uses: [
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
