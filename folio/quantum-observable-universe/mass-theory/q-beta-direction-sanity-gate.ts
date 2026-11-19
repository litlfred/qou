import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-beta-direction-sanity-gate",
  title:
    "$\\mathfrak{Q}_\\beta$ precision-ladder $\\S 4(d)$ formalize-first gate — any candidate Habiro element $F(q_0)$ must have magnitude consistent with the target observable's order of magnitude; the $z(q_0) \\approx 0.6127 < 1$ direction obstruction is the canonical refutation precedent",
  lean: {
    ref: "qou:QOU.QBeta.DirectionSanityGate.qbeta_direction_sanity_magnitude_match",
    validation: "not_checked",
  },
  interprets: "prop:q-beta-q-eq-one-shadow-gate",
  uses: [
    "prop:q-beta-q-eq-one-shadow-gate",
    "prop:q-beta-bar-even-kernel-invariant",
    "prop:q-beta-c-k-recursion-from-habiro-q-difference",
  ],
  cites: ["jones1987", "wenzl1988", "habiro2004"],
  computation: {
    engine: "python+mpmath",
    script:
      "computations/qbeta/qbeta_direction_sanity_gate_probe.py",
    witness: [
      "computations/qbeta/qbeta-direction-sanity-gate-probe.witness.json",
      "computations/qbeta/qbeta-c3-ladder-trace-convention-sensitivity.witness.json",
    ],
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
    { kind: "status", date: "2026-11-16", body: "Demoted from proposition on owner ruling 2026-11-16 (card \"Demote all six\"): the claim is not proved from established results, so it is stated as a remark (a screening policy, not a theorem). Label renamed rem:q-beta-direction-sanity-gate -> rem:q-beta-direction-sanity-gate." },
    {
      kind: "caveat",
      date: "2026-11-16",
      body: "'Structurally REFUTED' replaced: a 10x window is a heuristic screen with no proved invariant, so it is a scope-(a) filter, not an exclusion (AGENTS 'Before declaring refuted'). Target magnitude is ~1 only on the retired z=1 base; ~1.76 on the ruled z_D base. Queued for demotion to a remark (it is a policy, not a theorem).",
    },
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
        "(pass at $F(q_0) = 1.001$, fail with the $z(q_0) = 0.4993$ (convention-C) pattern " +
        "at target $> 1$).",
    },
  ],
});
