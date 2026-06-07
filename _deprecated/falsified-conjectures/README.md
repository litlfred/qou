# Falsified conjectures (deprecated)

Blocks moved here were `kind: "conjecture"` content objects whose
**stated form was falsified or refuted** by in-corpus computation /
audit. They are retained out-of-pipeline for the historical audit
trail; they are **not** part of the live paper and **not** validated.

Deprecated 2026-06-07 (conjecture status-drift triage, PR #1946 — see
[`docs/audits/2026-06-07-conjecture-triage.md`](../../docs/audits/2026-06-07-conjecture-triage.md)).

| Block | Why falsified |
|-------|---------------|
| `conj-chirality-ribbon-frobenius` | The exact ribbon-twist Markov-trace ratio diverges by ~10⁴ from the empirical `(1+h)(1−h)≈0.956` pattern at the audited atomic braids D ($H_6$), T ($H_9$), ³He ($H_9$). Witness `chirality-avg-content-atomic.witness.json`. Refuted at A≥2 in its stated form. |
| `reading-a-conditional-linking-weight` | The `−G·h²` (Catalan) coefficient directly contradicts the proved Family-A theorem `thm:lambda-scale-substrate-form` (`5/2 + ¾·h²`); the Wedderburn-sum incarnation was falsified across five structural routes. Carried only as a striking ppm-level numerical coincidence; never production. |

Neither block had any incoming `uses[]` from live content, and neither
Lean declaration was imported by the `QOU` Lake library (only a prose
comment in `QOU/Substrate/MuOverDetermination.lean` mentions the
`ReadingAValidAtH2` §3b-cond pattern by name).
