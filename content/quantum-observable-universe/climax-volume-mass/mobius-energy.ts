import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mobius-energy",
  lean: { ref: "qou:QOU.Braiding.mobius_energy",
    validation: "not_checked",
  },
  title: "Categorical recovery of Möbius energy",
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-23",
      body:
        "**A sibling `.lean` was shadowing the declaration this ref names** " +
        "(bean `qou-lo1t`). `lean.ref` names `QOU.Braiding.mobius_energy`, " +
        "which exists in the library at `QOU/Braiding/mobius_energy.lean` and " +
        "states the block's actual claim — `q = 1 → E_cat = c_topo * E_class`, " +
        "the classical-limit recovery. Resolution took the sibling " +
        "`mobius-energy.lean` first, and that file declared no `mobius_energy` " +
        "at all: a `CategoricalMobiusEnergy` structure (one of three unrelated " +
        "types sharing that name across the corpus) plus `mobius_energy_nonneg`, " +
        "returning its own `energy_classical_nonneg` field under the name of a " +
        "cited Freedman–He–Wang theorem. So the block advertised the " +
        "classical-limit claim and resolved to an assumed positivity. Sibling " +
        "deleted per §0a; the ref now reaches the library declaration.",
    },
    {
      kind: "caveat",
      date: "2026-08-23",
      body:
        "The library target is a §3b-cond context-class projection " +
        "(`:= ctx.claim_mobius_energy`) and says so in its own docstring: \"the " +
        "substantive mathematical content is carried by the context-class " +
        "axioms, and a full derivation from substrate primitives remains " +
        "pending.\" That is still an assumption rather than a derivation. It is " +
        "the honest form of one — it states the manuscript claim, names what is " +
        "open, and carries a record of a prior repair (the antecedent once " +
        "constrained a private `q_real` tied to the context's own `q` by " +
        "nothing) — which the deleted sibling was not.",
    },
  ],
  tags: ["mobius-energy", "categorical-mass", "knot-energy", "q-deformation"],
  uses: [
    "def:categorical-action",
    "thm:topological-mass",
    "rem:frobenius-simplification",
  ],
  proofs: ["prf:mobius-energy"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/mobius-energy-0.svg", blockIndex: 0, hash: "1582a4fa10bb" },
  ],
});
