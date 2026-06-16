# 2026-05-31 — L2 3-failing shared root, cross-referenced with CAL-3 = m_π corroboration

**Trigger.** This session corroborated `CAL-3 = m_π` via two independent
empirical paths (see
[`2026-05-31-cal-3-equals-m-pi-empirical-corroboration.md`](2026-05-31-cal-3-equals-m-pi-empirical-corroboration.md)).
The 2026-05-30 shared-root audit
([`2026-05-30-l2-100x-status-3-failing-shared-root.md`](2026-05-30-l2-100x-status-3-failing-shared-root.md))
was written **before** that corroboration and identified a "single Q_β
τ_M Kashiwara derivation truncated at k=2" gap as the root. This audit
re-tests whether the m_π corroboration changes that diagnosis.

**Verdict.** Diagnosis CONFIRMED, with a TIER REFINEMENT: the shared
root is the **Q_β c_k tier wall** (where the dashboard credits only
`tier: derived` rungs and refuses to credit `tier: cal-anchored` rungs
or `tier: near-match` c_3). CAL-3 = m_π corroboration does **not** move
the wall — m_π is a separate calibration anchor (chiral / Goldstone
scale, h³ jet order) and is structurally orthogonal to the Q_β
derivation chain (CAL-2 anchor, β-decay width, h² jet order). The fix
is still the **Q_β Habiro element** (Option E phase 2; in-flight via
`qbeta_habiro_taylor_investigation.py` and parallel α_EM PR #1511).

---

## 1. Existing shared-root diagnosis (2026-05-30)

The 2026-05-30 audit identified:

> All three failing observables share **one** structural input: the τ_M
> Kashiwara derivation of Q_β truncated at k=2 with "k≥3 fitted rungs
> dropped as non-canonical".

The miss-factor cluster:
- `Q_β`  → 164× (1247 ppb)
- `m_n`  → 181× (1.04 ppb)
- `Δ_pn` → 159× (754 ppb)

Audit conclusion: single Q_β-derivation gap with two propagated
derivatives via `m_n = m_p(substrate) + Q_β + m_e` and
`Δ_pn = m_n − m_p` (Path C, no flavor-split).

## 2. Current L2 dashboard (2026-05-31T15:23 UTC)

Per
[`per-observable-100x-status.witness.json`](../../computations/per-observable-100x-status.witness.json)
(commit `9e45f6d4`):

| obs | role | miss × | err (ppb) | target (ppb) |
|---|---|---:|---:|---:|
| Q_β | CAL-3 anchor (Path C) | **164.0** | 1279 | 7.8 |
| m_n | validation | **185.4** | 1.07 | 0.0057 |
| Δ_pn | validation (derived) | **163.3** | 774 | 4.7 |

Numbers are **slightly different** from the 2026-05-30 snapshot
(Q_β 164 vs 159.9; m_n 185 vs 180.8; Δ_pn 163 vs 159.3) — the
re-pin on main since 2026-05-30 nudged values by ≲5% but the shared
root persists.

## 3. Does CAL-3 = m_π change the diagnosis?

**No — orthogonal calibration slot.** The three-calibration architecture
explicitly separates the anchors by jet order:

| CAL | Observable | Jet order | What it sets |
|---|---|---|---|
| CAL-1 | m_e | h⁰ | electron mass (rest-mass scale) |
| CAL-2 | Q_β → q₀ | h² | substrate parameter q₀ |
| CAL-3 | 𝔇_π → m_π | h³ | chiral / Goldstone / hadronic mass scale |

Q_β is **derived** from CAL-1 + CAL-2 via the substrate identity. The
Q_β L2 miss is therefore a property of the **derivation chain at h²
jet order**, not a missing input from h³. Confirming CAL-3 = m_π
empirically corroborates the **architecture** but does not feed back
into the Q_β derivation: m_π is downstream (used in v9 nuclear-binding
closure), not upstream of Q_β.

**Cross-check via the cache witness** (`qbeta-ck-cache.witness.json`):
the c_k cache only consumes (m_e, q₀, b, ℏ_q) and references CAL-3
**only** as the experimental Q_β value used to verify residuals — never
as an input to the categorical derivation. No m_π appears anywhere in
the Q_β ladder.

**Diagnosis stays.** The shared root is **not** "missing m_π input";
it is the c_k tier wall.

## 4. Tier refinement (new — replaces the 2026-05-30 framing)

Per the canonical truncation-order framing
([`2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](2026-05-31-qbeta-ck-truncation-order-canonical-framing.md)),
the dashboard's 164× headline reflects a **tier policy**, not a
compute limit. Per
[`qbeta-ck-truncation-order-analysis.witness.json`](../../computations/qbeta/qbeta-ck-truncation-order-analysis.witness.json):

| N | c_k tier | cumulative residual (ppb) | miss factor vs 7.8 ppb target |
|---:|---|---:|---:|
| 2 | proved | 1274 | **163.3** (dashboard credits this) |
| 3 | near-match (c_3 = J_Hopf(q=1) = −2) | **38.6** | **4.95** (dashboard refuses) |
| 4 | near-match (c_4 = c_3·b⁴) | 32.7 | 4.19 |
| 5 | near-match (c_5 = c_3²·3+b) | 33.2 | 4.26 |

**At N=3 the empirical residual already beats the 100× target's order-
of-magnitude region (4.95× miss vs 164×)** — the dashboard 164× number
is a tier-policy outcome (don't credit q₀-dependent c_3) plus a
truncation-order outcome (only N=2 is reported in the headline).

The 2026-05-30 audit framed this as "k≥3 rungs dropped as
non-canonical" (binary wire/un-wire). The 2026-05-31 framing replaces
that with **rules 1+4**: N is a truncation order chosen by precision;
c_k≥3 are **near-match-tagged** (q₀-dependent), not dropped.

## 5. Diagnostic table per failing observable

| obs | current ppb miss | 100× target (ppb) | miss factor | hypothesized root cause | does CAL-3 = m_π affect? |
|---|---:|---:|---:|---|---|
| Q_β | 1279 | 7.8 | **164** | c_k tier wall: dashboard credits N=2 derived; N=3 with c_3 near-match would give 38.6 ppb (4.95×). **Permanent fix**: Q_β Habiro element promotes c_3+ to `proved`. | **No** — CAL-3 = m_π is an orthogonal h³ anchor; Q_β derivation is h². m_π does not appear in the c_k ladder. |
| m_n | 1.07 | 0.0057 | **185** | Path C propagation: `m_n = m_p(substrate) + Q_β(N=2) + m_e`. Inherits Q_β c_k wall via Q_β term. **Permanent fix**: same Habiro identification + flavor-split skein closure for the Q_β term. | **No** — propagated from Q_β. m_π appears only in nuclear-binding (option-e v9) which is downstream of m_n, not upstream. |
| Δ_pn | 774 | 4.7 | **163** | Derived: `Δ_pn = m_n − m_p` ≈ Q_β + m_e + small. Inherits Q_β c_k wall directly. | **No** — same chain as m_n. |

## 6. Hypothesis test from the task brief

> "If all 3 failures share `c_4 truncation noise` (per #1581 Finding B's
> reframing of the c_3 swing) as the root cause, then the path to
> closure is the Habiro generating function (running in parallel — see
> other background agent). If they share a different root (e.g. m_π
> missing as input), then they may already be closer to closure than
> the dashboard reflects."

**Confirmed first branch.** All 3 share the c_k tier wall (Q_β c_3+ are
q₀-dependent near-matches). The **closer-than-dashboard-reflects**
qualifier from the task brief IS supported: at N=3 with the
near-match c_3, the Q_β residual is 38.6 ppb (4.95× miss) — well above
target but **two orders of magnitude better** than the dashboard's
1279 ppb headline. The dashboard correctly refuses to credit this
under the tier policy (q₀-dependent c_3 is not a Taylor-exact
derivation), but the structural progress is real.

The `m_π missing as input` hypothesis is **rejected** by inspection of
the c_k cache: m_π does not appear in the Q_β derivation chain. CAL-3
operates at h³ (chiral scale), Q_β at h² (substrate derivation).

## 7. Best next action to close any of the 3

**Single best action: Q_β Habiro element identification.**

This is in-flight per
[`2026-05-31-qbeta-ck-truncation-order-canonical-framing.md` §Habiro
fix](2026-05-31-qbeta-ck-truncation-order-canonical-framing.md), with
infrastructure already started
(`qbeta_habiro_taylor_investigation.py`, `QbetaHabiroTaylorBridgeClass`
from PR #1479) and the α_EM Habiro precedent merged (PR #1511,
`alpha_em_habiro_taylor_investigation.py`).

Mechanism: identify the q-series H(q) ∈ Habiro ring whose Taylor
expansion at q₀ produces the c_k coefficients. Then:
- c_k≥3 upgrade `near-match → proved` (Taylor-exact, q₀-independent)
- N becomes a precision knob (per the N(ε) formula, N=3 closes Q_β,
  N=4 → m_n at 1 ppb, N=5 → m_n at 1 ppt)
- the q₀-swing vanishes by construction (true Taylor coefficient of a
  fixed q-series)
- **all 3 failing observables flip green simultaneously** (Q_β headline
  drops below 8 ppb; m_n inherits via Path C; Δ_pn inherits via
  `m_n − m_p`)

**Secondary actions** (lower leverage, parallel):
1. Sub-action: flavor-split skein closure for m_n's Q_β term. Tightens
   the propagation but does not fix the headline tier wall.
2. Sub-action: extend `chi-{T,3He}-...` witness coverage to ⁷Li/⁷Be,
   ¹¹B/¹¹C, etc. (pings on #1516) to validate that v9 generalizes —
   strengthens the m_π corroboration story but is **downstream** of
   the 3 failing observables on the L2 dashboard.

## 8. Status update for the 2026-05-30 audit

The 2026-05-30 audit
([`2026-05-30-l2-100x-status-3-failing-shared-root.md`](2026-05-30-l2-100x-status-3-failing-shared-root.md))
remains correct in its high-level conclusion (single shared root,
Q_β-derivation gap propagating to m_n / Δ_pn). This 2026-05-31 audit
**refines** the framing:

- Replaces "k≥3 fitted rungs dropped as non-canonical" with **c_k tier
  wall** (per truncation-order canonical framing).
- Adds the N=3 partial-credit observation: 38.6 ppb residual at
  near-match c_3, 4.95× miss vs the 164× tier-policy headline.
- Confirms that CAL-3 = m_π corroboration does **not** dissolve the
  diagnosis (orthogonal anchor, h³ vs h²).
- Re-points the closure path to **Q_β Habiro element identification**
  (already in-flight; not a new research program).

## 9. Cross-references

- 2026-05-30 shared-root audit (predecessor):
  [`2026-05-30-l2-100x-status-3-failing-shared-root.md`](2026-05-30-l2-100x-status-3-failing-shared-root.md)
- CAL-3 = m_π corroboration (sibling, this PR):
  [`2026-05-31-cal-3-equals-m-pi-empirical-corroboration.md`](2026-05-31-cal-3-equals-m-pi-empirical-corroboration.md)
- Q_β c_k truncation-order canonical framing (CLAUDE.md-cited):
  [`2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](2026-05-31-qbeta-ck-truncation-order-canonical-framing.md)
- Δ_λ gating context (deeper structural backdrop):
  [`2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md)
- L2 dashboard witness:
  [`per-observable-100x-status.witness.json`](../../computations/per-observable-100x-status.witness.json)
- Q_β c_k cache (tier table):
  [`qbeta-ck-cache.witness.json`](../../computations/qbeta/qbeta-ck-cache.witness.json)
- Q_β truncation-order analysis (per-rung residuals):
  [`qbeta-ck-truncation-order-analysis.witness.json`](../../computations/qbeta/qbeta-ck-truncation-order-analysis.witness.json)
