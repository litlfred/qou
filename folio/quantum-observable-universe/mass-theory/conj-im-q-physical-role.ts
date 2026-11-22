import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:im-q-physical-role",
  lean: {
    ref: "qou:QOU.BraidKnot.ImQPhysicalRole",
    validation: "not_checked",
  },
  title:
    "Physical role of $\\mathrm{Im}(q)$: a substrate moduli parameter not constrained by current QOU observables, with three candidate roles (chirality / phase coordinate / non-Hermitian deformation).",
  uses: ["rem:im-q-vs-p-skew"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): to the precision documented in `per-observable-100x-status.witness.json`." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): - [`prop:rho-k-pair-gen-canonical-form`](../mass-endomorphism/conj-rho-k-pair-gen-canonical-form.md) —" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): reproduced by\n[`the_apollonius_circle_from_cal2_reproduces_exactly_probe.py`](../../../computations/probes/the_apollonius_circle_from_cal2_reproduces_exactly_probe.py)\n(4/4), which also records that **no $q_0$ enters**:" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): the Lean carrier\n`all_six_agree` says so in its own docstring, and\n[the Fermi-relation block]" },
    {
      kind: "note",
      body: "An earlier version of this section stated that the coupling and phase-space integral were not supplied anywhere in the corpus; they are, in the hadron half-life rate formula.",
    },
    {
      kind: "status",
      date: "2026-05-25",
      body:
        "**Open conjecture (PR #1127).** Direct answer to the question 'what IS Im(q)?'. " +
        "The framework's current observables (masses via modulus projection; bar-symmetric " +
        "content via P_avg projection) are insensitive to Im(q) at leading order. Im(q) " +
        "is therefore a substrate moduli parameter without a current physical interpretation. " +
        "This conjecture catalogues three candidate roles; identifying which (if any) is " +
        "the physical one is open work.",
    },
    {
      kind: "refined-framing",
      date: "2026-05-25",
      body:
        "**Three candidate roles** (none currently proved, listed in order of structural " +
        "plausibility): " +
        "(i) **Chirality / orientation parameter** — for q on the unit circle " +
        "$|q| = 1$ with $\\arg q = 2\\pi/N$, q is an $N$-th root of unity giving " +
        "Kashaev's root-of-unity regime where Vol_q^tower → hyperbolic volume; Im(q) " +
        "would parametrize chirality direction. (ii) **Phase coordinate dual to CAL-2** " +
        "— CAL-2 (`m_μ/m_e = 206.77`) is ONE real equation on TWO real unknowns " +
        "(Re q, Im q), giving an Apollonius circle of admissible q values; Im(q) is " +
        "the arc-coordinate orthogonal to the real-axis solution. (iii) **Non-Hermitian " +
        "/ Wick-rotation deformation** — real q gives Hermitian Hecke representations " +
        "(Hoefsmit basis); complex q breaks unitarity, potentially encoding decay widths " +
        "/ open-system dynamics. Each candidate is testable against specific observables: " +
        "(i) via root-of-unity arithmetic; (ii) via the Apollonius parametrization probe " +
        "(see Phase A v2 audit); (iii) via non-unitary representations and their physical " +
        "interpretation.",
    },
    {
      kind: "caveat",
      date: "2026-05-25",
      body:
        "**What Im(q) is NOT.** Per " +
        "[`rem:im-q-vs-p-skew`](rem-im-q-vs-p-skew.md), Im(q) is **NOT** the EM / " +
        "P_skew channel — the bar-projection (P_avg / P_skew) operates on real q and " +
        "P_skew has real content there. Im(q) is a separate modulus-projection-discarded " +
        "degree of freedom, structurally orthogonal to the bar decomposition. The two " +
        "mechanisms must be distinguished.",
    },
    {
      kind: "refined-framing",
      date: "2026-09-03",
      body:
        "**Carrier rewritten: the conjecture now asserts something.** The Lean " +
        "sibling previously carried this conjecture as `def im_q_observable_pairing " +
        "(role : ImQCandidateRole) : Prop` returning `True` on all three branches — " +
        "a content-free carrier, which AGENTS.md \u00a73b-tax bans (`proof-claims-unencoded` " +
        "/ `true-class-field`), and a `def : Prop` where a `class` is required. It is " +
        "now the class `QOU.BraidKnot.ImQPhysicalRole obs q`, whose two fields are the " +
        "genuine hypotheses: the observable is `\u2016F \u00b7\u2016` for a conjugation-equivariant " +
        "`F`, and at leading order its value at q equals its value at Re q. The payoff " +
        "`im_q_undetermined` is **derived**, not asserted \u2014 such an observable cannot " +
        "tell q from a real number. lean-direct exit 0, zero warnings, all seven " +
        "declarations on the standard three axioms. There is deliberately **no instance** " +
        "for the QOU mass observable; supplying one is the open work.",
    },
    {
      kind: "caveat",
      date: "2026-09-03",
      body:
        "**Sign vs magnitude \u2014 do not conflate the two results.** " +
        "`obs_conj_invariance` uses only the first field and is therefore " +
        "unconditional for any modulus observable: it shows such an observable cannot " +
        "see the **sign** of Im(q). The conjecture is about the **magnitude** and is " +
        "carried entirely by the second field. The proved sign-blindness is not " +
        "evidence for the conjectured magnitude-blindness.",
    },
  ],
  tags: [
    "tier:S",
    "im-q",
    "substrate-moduli",
    "complex-q",
    "chirality",
    "non-hermitian",
    "open-conjecture",
    "phase-3",
  ],
});
