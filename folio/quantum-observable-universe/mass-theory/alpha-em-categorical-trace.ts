import { remark } from "../../schema/builders";

export default remark({
  label: "rem:alpha-em-categorical-trace",
  title: "Legacy empirical $\\alpha_{EM}$ forms (deprecated — superseded by the pre-archimedean trace-ratio)",
  interprets: "thm:em-spectral-completeness",
  uses: [
    "prop:alpha-em-categorical-trace-ratio",
    "cor:gauge-coupling-uniqueness",
    "prop:em-coupling-bring-zero-mode",
  ],
  authorNotes: [
    {
      kind: "deprecated",
      date: "2026-06-10",
      body:
        "The obsolete empirical / PSLQ $\\alpha_{EM}$ closed forms ($45[3]_q(1+\\delta_{CS}+8q\\delta_{CS}^2)$, the gluon-octet conjecture) were moved OUT of this block into [docs/audits/2026-06-10-alpha-em-legacy-empirical-forms.md](../../../docs/audits/2026-06-10-alpha-em-legacy-empirical-forms.md) per the owner directive (keep the audit trail, but not in the paper). They were single-point PSLQ matches at $q_0$, not derivations — the multiplicative $q$-rational family was ruled out by the 100-dps 54-element scan. The canonical form is the pre-archimedean trace-ratio [prop:alpha-em-categorical-trace-ratio](#prop:alpha-em-categorical-trace-ratio) (no $\\pi$); the archimedean correction is [prop:em-coupling-bring-zero-mode](#prop:em-coupling-bring-zero-mode). Do not revive the empirical product forms.",
    },
  ],
});
