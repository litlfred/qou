import { definition } from "../../schema/builders";

export default definition({
  label: "def:skein-binding-lagrangian",
  title: "Skein binding Lagrangian for multi-nucleon links",
  tags: [
    "lagrangian",
    "binding",
    "skein",
    "nuclear",
    "coulomb",
    "strong-force",
    "pauli",
  ],
  lean: { ref: "qou:QOU.Braiding.SkeinBindingLagrangian",
    validation: "not_checked",
  },
  uses: ["prop:qou-canonical-action"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): A witness now exists: [`mirror-split-continuum-em`](../../../computations/deltalambda/mirror-split-continuum-em.witness.json), computed by [`coulomb_energy.py`](../../../computations/coulomb_energy.py) with **zero fitted constants**." },
    {
      kind: "note",
      body:
        "Lean sibling lives on the observable/archimedean side of the substrate→archimedean wall (AGENTS.md §7c): the fractional mass-number powers $A^{2/3}$, $A^{1/3}$ (`Real.rpow`), rational divisors, and the substrate inverse $q^{-1}$ at the real evaluation $q\\mapsto q_0>1$ force $\\mathbb{R}$. The archimedean specialisation is intended, not a base-ring leak — the Lean docstring already states this side placement.",
    },
  ],
});
