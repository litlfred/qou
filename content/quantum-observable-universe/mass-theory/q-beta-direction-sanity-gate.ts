import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-beta-direction-sanity-gate",
  title:
    "$\\mathfrak{Q}_\\beta$ precision-ladder $\\S 4(d)$ formalize-first gate — any candidate Habiro element $F(q_0)$ must have magnitude consistent with the target observable's order of magnitude; the $z(q_0) = 0.4993 < 1$ direction obstruction is the canonical refutation precedent",
  lean: {
    ref: "qou:QOU.QBeta.DirectionSanityGate.qbeta_direction_sanity_magnitude_match",
    validation: "not_checked",
  },
  uses: [
    "prop:q-beta-q-eq-one-shadow-gate",
    "prop:q-beta-radius-of-convergence-gate",
    "prop:q-beta-bar-even-kernel-invariant",
    "prop:q-beta-c-k-recursion-from-habiro-q-difference",
  ],
  cites: ["jones1987", "wenzl1988", "habiro2004"],
  computation: {
    engine: "python+sympy+mpmath",
    script:
      "folio-assistant/computations/qbeta/qbeta_direction_sanity_gate_probe.py",
    witness:
      "folio-assistant/computations/qbeta/qbeta-direction-sanity-gate-probe.witness.json",
    status: "verified",
  },
  tags: [
    "q-beta",
    "precision-ladder",
    "structural",
    "formalize-first",
    "direction-sanity",
    "kernel-invariant",
    "no-fit",
  ],
  authorNotes: [
    {
      kind: "status",
      body:
        "**Theorem (this proposition).** Sorry-free Lean proof " +
        "(`q-beta-direction-sanity-gate.lean`) — §3b-cond conditional class " +
        "`DirectionSanityGateClass` with a single field hypothesis encoding " +
        "the magnitude-match condition, plus a rejection lemma showing any " +
        "candidate with order-of-magnitude mismatch fails the gate. " +
        "**Compute (sympy + mpmath):** verified in " +
        "`qbeta_direction_sanity_gate_probe.py` (witness " +
        "`qbeta-direction-sanity-gate-probe.witness.json`) — target magnitude " +
        "at $q_0 \\approx 0.998$; gate demonstrated on synthetic candidates " +
        "(pass at $F(q_0) = 1.001$, fail with the $z(q_0) = 0.4993$ pattern " +
        "at target $> 1$).",
    },
  ],
});
