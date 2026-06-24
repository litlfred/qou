import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-zero-complex-extension",
  proofs: ["prf:q-zero-complex-extension"],
  lean: {
    ref: "qou:QOU.BraidKnot.QZeroComplexExtension.complex_q_is_unit",
    validation: "not_checked",
  },
  title:
    "The pre-Archimedean substrate is polymorphic in its base ring: specializing to $R = \\mathbb{C}$ with $|q| > 1$ is admissible without modifying the Hecke quadratic, the bar involution, the Frobenius pairing, or the Markov trace. The current real-axis convention $q_0 \\in \\mathbb{R}$, $q_0 > 1$ is one such specialization; complex $q_0$ with $|q_0| > 1$ and $\\mathrm{Im}(q_0) \\neq 0$ is uninstantiated infrastructure (audit: [`2026-05-24-q-zero-reality-audit`](../../../docs/audits/2026-05-24-q-zero-reality-audit.md)).",
  uses: [
    "def:bar-involution",
    "thm:jones-markov-trace",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-05-24",
      body: "**Research-grade infrastructure (PR #1127).** This proposition records the *structural admissibility* of complex $q$; it does **not** propose that $q_0$ is in fact complex. The dominant 2.89% L2 gap for $m_p$, $m_n$ is bar-symmetric (see [`2026-05-24-q-zero-reality-audit.md`](../../../docs/audits/2026-05-24-q-zero-reality-audit.md)) and is not naturally targeted by an $\\mathrm{Im}(q_0)$ contribution; the complex lift is infrastructure for the bar-symmetric / bar-anti-symmetric decomposition (cheat-sheet §4), not a fix for the current numerical residual. A genuine $\\mathrm{Im}(q_0) \\neq 0$ would require either (a) a function expressing $\\mathrm{Im}(q_0)$ in terms of the existing three calibrations $(m_e, m_\\mu/m_e, \\mathfrak{Q}_\\beta)$ — *not* a fourth input, which the 3-calibration discipline forbids — or (b) a structural constraint fixing $\\mathrm{Im}(q_0)$ from substrate data. Neither is currently supplied.",
    },
  ],
  tags: [
    "substrate",
    "categorical-action",
    "complex-q",
    "base-ring",
    "research-grade",
  ],
  cites: [
    "wenzl1988",
    "jones1987",
  ],
});
