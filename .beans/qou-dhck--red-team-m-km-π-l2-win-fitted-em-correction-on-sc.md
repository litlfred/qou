---
# qou-dhck
title: 'RED-TEAM m_K/m_π L2 win: fitted EM correction on scan-selected term, NOT parameter-free'
status: todo
type: task
created_at: 2026-08-22T15:35:55Z
updated_at: 2026-08-22T15:35:55Z
---

Verdict: the single claimed L2 accuracy success (m_K/m_π, 23.45 ppb, 'beats 100x') is NOT a genuine parameter-free prediction.

Formula: m_K^2/m_pi^2 = [3]_q[4]_q + (alpha_em/pi)(3q^2-1)/(2q^2).

Ablation (mpmath 70dps, reproduces witness):
- strong-only sqrt([3]_q[4]_q): 101.6 ppm -> MISSES 100x target (264 ppb) by 385x.
- full: 23.45 ppb -> beats. Entire win is the EM correction.
- (3q^2-1)/(2q^2) is a 3-term truncation of 1+log(1+hbar_q); the truncation (23.4 ppb) BEATS the untruncated series (51.5 ppb) => stopping point chosen against data (ladder-fit signature).
- alpha_em value barely matters (CODATA vs derived: 23.40 vs 23.45 ppb); the truncation is the lever.

DOF: scan-selected pair (3,4) [audit: 'found by scanning q-integer products', 'spin assignment post-hoc'] + alpha_em (4th input, conditional on open Witten-kappa Lean sorry, own selected crossings 9,10) + data-selected truncation order. >=3 discrete knobs + conditional input.

'Only observable that beats 100x' partly because kaon target (264 ppb) is ~85000x looser than m_p target (0.003 ppb) - kaon measured to only 26 ppm.

Lean 'both pieces proved': meson_qCG_3x4 = q-CG fusion decomposition (real algebra, says nothing about kaon); meson_EM_closed_form = rational-function rewrite (X=X tautology class). sorry-free != derived.

Honest count of UNCONDITIONAL parameter-free sub-100x predictions: 0/5, not 1/5.

Doc: docs/audits/2026-08-22-mK-mpi-l2-red-team.md. Read-only audit; recommends footnoting the dashboard/AGENTS.md row as conditional+truncation-selected and marking stale meson-kaon-pion-derivation.witness.json (retracted (9/5)^2 power-scan fit).

---

## RESOLUTION 2026-08-22 (PR #5467) — recommendations 1–3 all actioned; the 0/5 verdict STANDS

**The verdict is not retracted.** One of the three knobs is removed; the
other two — the scan-selected `(3,4)` pair and `α_em`'s conditionality on
the open Witten-κ `sorry` — are untouched. `m_K/m_π` remains conditional
and is no longer labelled DERIVED anywhere.

**What this audit did not know when written.** The truncation had already
been ruled out by the owner on **2026-08-09** (`docs/precision-goals.md`
§L2), with the same reasoning and the same cost figure. No producer was
ever updated, so this audit red-teamed the stale formula in good faith
and independently reached the same conclusion. Second confirmation, not
discovery. The failure mode worth naming: a durable ruling recorded in
prose, with no code change and no bean, is indistinguishable from no
ruling at all.

**Sharpened evidence.** The full stopping-order sweep (now emitted as
`em_truncation_order_sweep_ppb`) is stronger than §2's two-row
comparison: 479.11 / **23.45** / 53.55 / 51.31 / 51.49 / 51.474 / 51.4755
ppb for ℏ¹…ℏ⁷, converging to 51.4754. Order 2 is the *unique* order below
the limit — which selection explains and convergence cannot.

**Cost:** 23.45 → 51.48 ppb against a 263.6 ppb target. Margin 11.2× →
5.1×. Scorecard unchanged at 1/5 scoreable. The fit was never
load-bearing.

**Recommendation 3, beyond marking the stale witness:** the
`(9/5)²` route is not merely stale on disk, it is live in the paper as
`prf:meson-kaon-pion-hecke-seifert`, whose proof body read that a power
scan "confirms that n_q = 2 uniquely minimises the PDG residual" and
whose producer emitted a field named `squaring_proof` concluding "The
data selects n_q = 2". Re-scoped as a consistency check.

**One calibration on this audit's own framing.** §3 lists the truncation
order and the `(9/5)²` power scan as the same class. They are not. The
truncation was a unique dip in a converging series — only selection
explains that. The exponent was named in advance by the two-body
rationale, with only three integer candidates, two missing by 44 % and
80 %. That is *overstated*, not *fitted*. Both needed fixing; conflating
them would over-call the second.

**Commits:** `e3ebd00a6` (de-fit), `0463a10be` (tracker + §8),
`f711201aa` (content block), `a353ba0ed` (de-launder the power scan).
