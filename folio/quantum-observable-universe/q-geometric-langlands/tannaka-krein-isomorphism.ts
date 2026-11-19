import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:tannaka-krein-isomorphism",
  title: "Tannaka--Krein duality for the aether",
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
  authorNotes: [
    {
      kind: "note",
      body: "The Lean carrier `IsTannakaKreinDual` states the fibre-functor-compatible equivalence condition over arbitrary parameter categories and is satisfiable via the identity equivalence on a category over its own fibre functor; no instance is supplied for `Rep_loc(A)` and `Comod(H_xi)`.",
    },
  ],
});
