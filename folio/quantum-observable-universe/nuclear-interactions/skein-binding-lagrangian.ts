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
    { kind: "note", body: "Archimedean specialisation (moved from the definition prose 2026-11-19): What follows sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs\u2014real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical/$q$-deformation identities it relies upon remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here." },
    {
      kind: "note",
      body:
        "Lean sibling lives on the observable/archimedean side of the substrate→archimedean wall (AGENTS.md §7c): the fractional mass-number powers $A^{2/3}$, $A^{1/3}$ (`Real.rpow`), rational divisors, and the substrate inverse $q^{-1}$ at the real evaluation $q\\mapsto q_0>1$ force $\\mathbb{R}$. The archimedean specialisation is intended, not a base-ring leak — the Lean docstring already states this side placement.",
    },
  ],
});
