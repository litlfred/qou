import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:im-q-physical-role",
  lean: {
    ref: "qou:QOU.BraidKnot.ImQPhysicalRole.im_q_observable_pairing",
    validation: "not_checked",
  },
  title:
    "Physical role of $\\mathrm{Im}(q)$: a substrate moduli parameter not constrained by current QOU observables, with three candidate roles (chirality / phase coordinate / non-Hermitian deformation).",
  uses: ["rem:im-q-vs-p-skew"],
  authorNotes: [
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
