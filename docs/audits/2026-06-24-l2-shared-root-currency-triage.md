# L2 100× shared root (Q_β / m_n / Δ_pn) — currency triage + honest gate (2026-06-24)

**Date:** 2026-06-24
**Branch:** `claude/mass-open-keystone-w-l2-root-2026-06-24`
**Status:** triage only (no new compute). Confirms the 2026-05-30 shared-root diagnosis is still canonical, re-scopes the gate post-repin, flags a stale-witness backlog.

## Question

What is the single root cause behind the 3 L2-failing mass observables (Q_β, m_n,
Δ_pn), is the 2026-05-30 diagnosis still current after the 2026-05-28 proton-anchor
re-pin, and is anything tractable now?

## Current margins (dashboard, `per-observable-100x-status.witness.json`, computed 2026-06-22)

| Observable | role | error | 100× target | miss | meets? |
|---|---|---|---|---|---|
| m_p | CAL-2 anchor | 0.0004 ppb | 0.31 | 0.13× | ✓ |
| m_e | CAL-1 anchor | 0 | 0.29 | — | ✓ |
| m_K/m_π | meson validation | 28 ppb | 264 | 0.11× | ✓ |
| **Q_β** | CAL-3 (derived) | **1279 ppb** | 7.8 | **164×** | ✗ |
| **m_n** | validation | **1.07 ppb** | 0.0057 | **185×** | ✗ |
| **Δ_pn** | validation (derived) | **774 ppb** | 4.7 | **163×** | ✗ |
| **m_μ** | validation (post-repin) | **210 ppb** | 0.22 | **964×** | ✗ |

**3/7 meet.** The Q_β/m_n/Δ_pn trio clusters at **160–185×** (one shared root);
**m_μ's 964× is independent** (μ–p substrate floor — a separate item, not this root).

## The shared root (still canonical)

`docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`: all three share the
**`c_k` truncation / tier wall** in the Q_β τ_M (Kashiwara) derivation. The dashboard
credits only DERIVED-tier rungs (`c_2 = −1`, proved Taylor-exact); it refuses the
q₀-dependent NEAR-MATCH rungs `c_k ≥ 3`. m_n and Δ_pn **inherit** the Q_β miss via
`m_n = m_p(substrate) + Q_β + m_e` and `Δ_pn = m_n − m_p`. So it is **one** structural
input, not three independent failures.

Refinements (do not contradict): 2026-05-31 reframes it as the c_k tier wall
explicitly; with the near-match `c_3 = −2` the Q_β residual is ≈ 38.6 ppb (≈5× miss)
vs the 164× headline — two orders better, but structurally q₀-dependent, so the
dashboard correctly declines to credit it.

## The gate (re-scoped post-repin)

| candidate gate | status |
|---|---|
| **Δ_λ / Option-E KLR menu** | **NOT the gate** — the cont-9 menu paths (Wenzl×q-Poch, Demazure, Type-B, KLR canonical) were **refuted** at u² magnitude/sign (`2026-06-06-l2-shared-root-post-klr-update.md`, PRs #1911/#1914/#1924). |
| **Subgoal-2 (q₀ derivation)** | **inapplicable** — the shared root sits above the CAL-2 floor (~780 ppb), so Subgoal-1 closure suffices; the narrow 2026-06-19 keystone reversal is for the s5-so3 geometric `W_λ` only, not this. |
| **Q_β Habiro element** | **THE live gate** — in-flight, **not closed**. |

The Q_β Habiro-element route (`2026-06-13-qbeta-habiro-element-ledger.md`):
the Wenzl decomposition `c_3 = −2 − (3/2)·W₄(q)`, `W₄ = 1/[4]_q!`, is **structurally
identified** (Phase 2, residual ≈ −0.0005 ppm) but **not yet closed** to a
fibre-level Habiro-ring element `F(q)` reproducing `c_k` at *every* anchor, and **not
wired** (AGENTS.md guardrail: no wiring until cross-anchor validation at q_proton AND
q_muon). bean `kehn` tracks "improve m_n via Q_β/Habiro (lever 1)".

## Verdict — honest

**Nothing in the trio is tractable-to-green without closing the Q_β Habiro element.**
The mechanism is known (the Wenzl/Habiro framework, reused from the merged α_EM
`[2]_q·(1−h²α)` #1511), and the c_3 structural form is identified; but the closed
fibre-level `F(q)` with cross-anchor validation remains a research-grade open problem.
Once closed and wired, **all three flip green simultaneously** (m_n and Δ_pn inherit).

### Actionable side-finding (independent of the closure)

The 2026-05-28 re-pin was invisible to scriptHash staleness detection (the q₀
*constant* changed, not the producer scripts). Per
`2026-05-30-q0-repin-stale-witness-audit.md`, **~394 witnesses still carry the
muon-anchored q₀** — including the Q_β cache whose pre-repin "5.7 ppb Habiro-exact"
result is **stale** (the live figure is the 1279 ppb dashboard value). A batched
regen at the proton anchor (`witness_constant_staleness.py` flags them) would refresh
the trio's true current margins — a concrete, non-research-grade backlog item.

## Discipline

Triage of existing artifacts; corpus-grep currency check; no new compute, no fit. The
"gated on the Q_β Habiro element" verdict is a factual corpus-status claim (the
corpus-grep paths above return the supporting audits; the Δ_λ-menu and Subgoal-2
alternatives are positively excluded by cited refutations).
