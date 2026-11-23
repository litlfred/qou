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
  uses: ["prop:qou-canonical-action", "def:coulomb-charge", "conj:weinberg-angle-categorical"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-22",
      body: "Coulomb item rewritten 2026-11-22 (issue #9102, PR #9103). The previous text said each proton–proton crossing's q-deformed wedge asymmetry \"evaluates directly to the electrostatic penalty\" via a U(1) sub-action; nothing in the corpus derives that, and audit `docs/audits/2026-11-21-neutron-heavier-sign.md` §26–§29 shows no braid element or invariant pair coupling gives a Q_A·Q_B term. Input table from audit §25. Bounded-degree statement: `QOU.Hecke.BoundedDegreeCoulomb`. Coulomb needs sin²θ_W and Z removal: `QOU/QBeta/NeutralExchangeSplit.lean`, `QOU/QBeta/CoulombNeedsZRemoval.lean` (sorry-free). α_EM: owner ruling 2026-11-21 (the canonical α_em form stays open, bean `qou-aemx`); conditional on the Gram matrix with no instance of `ChernSimonsCorrectionConjecture` (bean `qou-gbsa`). Producer: `computations/coulomb_energy.py`.",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): A witness now exists: [`mirror-split-continuum-em`](../../../computations/deltalambda/mirror-split-continuum-em.witness.json), computed by [`coulomb_energy.py`](../../../computations/coulomb_energy.py) with **zero fitted constants**." },
    {
      kind: "note",
      body:
        "Lean sibling lives on the observable/archimedean side of the substrate→archimedean wall (AGENTS.md §7c): the fractional mass-number powers $A^{2/3}$, $A^{1/3}$ (`Real.rpow`), rational divisors, and the substrate inverse $q^{-1}$ at the real evaluation $q\\mapsto q_0>1$ force $\\mathbb{R}$. The archimedean specialisation is intended, not a base-ring leak — the Lean docstring already states this side placement.",
    },
  ],
});
