import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:topological-mass",
  examples: ["ex:topological-mass-su2"],
  title: "Topological Decomposition of Mass",
  tags: ["mass", "topological-decomposition", "descent-involution"],
  lean: { ref: "qou:QOU.Torsion.mass_decomposition_categorical",
    validation: "not_checked",
  },
  uses: [
    "def:mass-identity",
    "def:brane-boundary",
    "prop:descent-eigenspaces",
  ],
  proofs: ["prf:topological-mass-categorical", "prf:topological-mass"],
  computation: {
    engine: "sympy",
    script: "computations/mass-from-q-symbolic.py",
    witness: "computations/mass-from-q-symbolic.witness.json",
    status: "verified",
  },
  authorNotes: [
    { kind: "note", body: "Archimedean specialisation over R (§7c)." },
  ],
});
