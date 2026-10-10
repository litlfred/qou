# Quantum Observable Universe — STATUS

> Always-current dashboard for the QOU folio. Each row links to the
> **master ledger** for that goal. Agents update relevant ledgers at
> session start (intent) + session end (results).

> Convention: see `.claude/skills/local/session-intent.md` (TBD)
> and `.claude/skills/local/coordinate.md` for the ledger discipline.

## Goals + ledgers

| Goal | Status | Ledger | Active PRs |
|------|--------|--------|------------|
| **L1: 1 ppQ compute precision** | **CERTIFIED 2026-07-13 — 6/6 production atoms** (p, n, D, T, ³He, ⁴He). `cross_check_trM_1ppb.py` reports `allPassed=True`; worst closed-form χ-anchor \|Δ\| = **5.6e-50**; no float64 in the hot path. Last gap (⁴He, H₁₂) closed by building `pyhecke-native` from source. **Supersedes** the 2026-06-17 "NOT certified" finding (PR #2444), whose float64-limited `markov_peel` witness was replaced by the mpf / native-Rust path. ⚠ the aggregate `onepb-status-dashboard.witness.json` (2026-07-06) **predates this and is stale** | [`audits/2026-07-13-l1-4he-certification-complete.md`](docs/audits/2026-07-13-l1-4he-certification-complete.md) | — |
| **L2: per-observable 100× exp** | **2/7 met** — m_e (CAL-1 anchor) + **m_K/m_π** (the one genuine prediction that meets). The other 5 miss: m_p ~437×, m_μ ~964×, Q_β ~160×, m_n ~416×, Δ_pn ~159×. **m_p dropped from "met" 2026-07-04** when its fitted Habiro tower `(1+46u⁴)(1+4u⁵)(1−29u⁶)` was removed; de-fitted round-trip is +1.35 ppb. Live source `per-observable-100x-status.witness.json` (`beats_100x_count=2`, computedAt 2026-07-18). **Not 3/7, not 4/7** | [`docs/precision-goals.md`](docs/precision-goals.md) | — |
| **1 ppQ — Q_β only (achievable)** | open. The **entire 1248 ppb residual is the c₃-and-beyond truncation**; `c_2 = −1` is the only Taylor-exact Lean-proved rung, and `c_3` is stamped `tier: "cal-anchored"` in `qbeta-ck-cache` ("NOT a prediction — must not count toward any dashboard pass"). Real-q₀ routes closed scope-(b) (#4282/#4288/#4293); surviving carrier is a **fibre-level complex phase**. **New hard constraint (2026-08-08):** the proton/muon anchor swing on Q_β is **29.96 ppb = 3.8× the entire 7.797 ppb target** — deriving c₃ is necessary but *not sufficient*. Q_β drives **3 of the 5 L2 misses** via `m_n = m_p+Q_β+m_e`, `Δ_pn = Q_β+m_e` | [`1ppq-qbeta.md`](docs/coordination/1ppq-qbeta.md) | #4788 |
| **Δ_λ closure** | **VALUE PROVED** (2026-08-02, sorry-free, general-n): `Δ_λ = (−1)^{n(λ)}·dim V_λ`, the signed Springer dimension (`dtEuler_eq_deltaLambda_unconditional`, #4580). **Still open:** (a) the **many-body MAGNITUDE** — the deuteron `r* ≈ 1.585` deficit, which is what all six ansätze actually failed; proved *not* expressible as a per-block Δ_λ reweight (pairwise cap `ρ_A ≤ C(A,2)`, `exchangeDet_pow_two_le_four`), so the missing object is a separate additive ≥3-body extensive term; (b) the **geometric concentration**, which needs an external Springer-geometry input. **Do not restate as "gate closed"** — that is the sorry-free ≠ derived error | [`option-e.md`](docs/coordination/option-e.md) · [`audits/2026-08-02-deltalambda-value-proved-…`](docs/audits/2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md) | #4617 |
| **Volume–binding (L2 binding targets)** | **The four-point test cannot be run** (2026-08-08). Reading 1 (literal mass-braid H₉ closures) → all non-hyperbolic, 0 usable points. Reading 2 (SDP registry) → `n_atoms = 3`, deuteron maps to the Seifert-fibred Hopf link (Vol = 0), and **⁴He has no SDP binding link at all** (solver scope A ≤ 3). ⇒ **2 usable points of 4 required** (T, ³He) — the same mirror pair as the original two-point observation. Blocked on **data**, not on the pending Reading-1-vs-Reading-2 ruling | [`2026-08-07-l2-volume-binding-cluster.md`](docs/coordination/2026-08-07-l2-volume-binding-cluster.md) | #4788 |
| **α_EM canonical derivation** | F-construction T1–T5 + R1 closed; parameter-free target assembled. **R2 only** remains — loop-weight provenance, **owner-ruled NOT proved**; `1/(8π)` stays phase-4, **do not wire** | [`alpha-em.md`](docs/coordination/alpha-em.md) | — |
| **Q_β c_k flip-flop prevention** | enforcement live on main (PR #1577 merged: canonical-no-negative-result + ck-tiered-not-binary) | (lives in 1ppq-qbeta.md flip-flop history) | — |
| **Lean uniqueness wiring** | ~18% witness coverage — ⚠ *not re-verified in the 2026-08-08 pass; treat as of 2026-06-17* | (per-PR) | — |
| **Mass-sweep gap (A ≥ 4)** | ⚠ *not re-verified in the 2026-08-08 pass; as of 2026-06-17.* mean abs err 4.25% pre-2026-06-03; α-cluster wire-up landed PR #1756 — 7 atoms (¹⁶O / ²⁰Ne / ²⁴Mg / ²⁸Si / ³²S / ³⁶Ar / ⁴⁰Ca) moved from B=0 to α-recursion B_pred, m_err improved from ~+0.9% to ~−0.1% (10× better); non-α-cluster A > 12 (32 atoms) still gated on H_{3A} kernel | (lives in option-e.md + [`docs/workplans/2026-06-03-per-knot-mass-table-wireup-workplan.md`](docs/workplans/2026-06-03-per-knot-mass-table-wireup-workplan.md)) | #1756 |
| **s5-so3 fibre-action keystone** | ⚠ *not re-verified in the 2026-08-08 pass; as of 2026-06-17.* combinatorial / representation-theoretic leg done; selection ℓ→λ **realized** by the Hopf moment map μ; strand fibre ≥ colour ℂ³ (a *lower* bound — the production trace is the full-Hecke principal specialization, so **no finite colour-SU(3) arena**, #2406); refuted = 210 ppb muon + colour⊗spin + Reeb-resonance + **Wu-manifold SU(3)/SO(3) arena** (#2398: spacetime ⊥ colour, no spacetime-fixing Reeb); **open** = does the full-Hecke principal-specialization Markov trace admit *any* geometric realization reproducing the canonical weights? (finite-dim Sasakian ruled out; `W_λ = d_q(λ)²/[n]_q!` is the q-Plancherel measure, **not** the production weight) | [`s5-so3-keystone.md`](docs/coordination/s5-so3-keystone.md) | (PRs through #2431; sibling A≥3 compute #2369/#2371/#2372) |

## Cross-cutting queues

| Queue | Purpose | Items |
|-------|---------|-------|
| [`.beans/1ppq-qbeta-queue.json`](.beans/1ppq-qbeta-queue.json) | Per-goal 1ppQ-Q_β work | 6 (3 done, 1 in_progress, 2 blocked) |
| [`.beans/lean-discharge-queue.json`](.beans/lean-discharge-queue.json) | Mechanical Lean sorry discharge (NOT §3b-cond) | 8 items + 1 registry of permanent sorries |
| [`.beans/research-queue.json`](.beans/research-queue.json) | Research-grade open items across goals | 7 items (Q_β Habiro, Φ_q×spectral, (1+q)/2, multi-nucleon A=4, atom→knot A≥5, fibre/observable doc, q_0 declined) |

## Active sessions

> Tracked by active PR (sessions are ephemeral). The 1ppQ frontier is densely worked — coordinate before touching Q_β / L1 / operator-extraction files.

| PR | Goal scope | Updated | Status |
|----|------------|---------|--------|
| #4788 | L2 gap prunes — HH¹ Bring root, volume-binding four-point, STATUS refresh | 2026-08-08 | active |
| #4664 | L2 closure attacks; non-EM binding terms; extended Bloch; volume term | 2026-08-07 | active |
| #4617 | Δ_λ / deuteron μ₃ submodularity (Δ_λ magnitude) | 2026-08-07 | active |
| #4658 | 5₂ sum rule, Bloch–Wigner caveat | 2026-08-07 | active |
| #4610 | `Vol(T)`, `Vol(³He)` of braid closures (SnapPy) | 2026-08-02 | stale |
| #4591 | `Vol + i·CS` census for m_τ | 2026-08-02 | stale |

> The 2026-06-17 rows (#2444, #2106, #2442/#2434, #2371) are long since
> resolved or superseded and have been dropped.

## Conventions

- **Read this file first** at session start. Every agent.
- **Update the relevant ledger** with intent at session start; results at session end.
- **Watch main** continuously (per `.claude/skills/local/watch.md`); log relevant landings to ledger.
- **Coordinate with siblings** via `.claude/skills/local/coordinate.md`; cross-link active PRs in this table.
- **STATUS.md is a board, not a narrative.** Use master ledgers for chronology + open probes + retraction history.

## Session history (recent)

- **2026-08-08** (Claude, `claude/l2-gap-prunes-2026-08-08`, PR #4788): refreshed
  this board after a 7-week stall (it read L2 3/7 and L1 "NOT certified"; both
  were wrong — L2 is 2/7 since the 2026-07-04 m_p de-fitting, L1 was certified
  6/6 atoms 2026-07-13). Ran bean `qou-jcmw`: `dim HH¹(H₅(ζ₅)) = 1` and the
  outer class acts with **rank 1 on the 7-dim cocenter** (trace-visible, exact
  direction) — the prune the 08-08 Q_β assessment expected to be a cheap kill
  came back **alive**; parity measured Θ-even under the *sign-twisted* bar and
  explicitly **not** recorded as a bar-parity result. Found the proposed
  volume-binding four-point test **unrunnable**: 2 usable points of 4, blocked
  on missing A=4 SDP data rather than on the pending reading ruling.
- **2026-06-17** (Claude, `claude/laughing-hopper-lbo214`, 4 PRs merged): refuted the difference-link-volume geometric route to the per-isotope binding residual `q₀^(10A−5)` (PR #2435, non-constant 2.36× prefactor); Lean-grounded the Q_β silver anchor — `b²=7/8` derived from `q²−2q−1=0` (PR #2445); **corrected** that PR's dominance overclaim — the silver/Q_A zero is a *genuine but subdominant* F-pole (char root 3.12, not the dominant 117.4; PR #2454), via the GB-`Δ(net)(1+√2)=82216+58136√2≠0` (an earlier cheat-sheet check was circular); confirmed PR #2444's L1-not-certified finding live and backed out a stale "L1 met" precision-goals.md edit. Refreshed this board.
- **2026-05-31 / 2026-06-01** (Claude, ~10 PRs): Built coordination infrastructure (STATUS.md, master ledgers for 1ppq-qbeta + option-e + alpha-em, queue files, `/session-intent` + `/pending-show` skills, SessionStart hook), bumped precision defaults (compute 65 → 70 dps, output 50 → 60 dps), settled c_3 q_0-stability as NEAR-MATCH not Taylor-exact (5th-and-final settlement; flip-flop history catalogued), refuted Li_2^q × spectral combiner (mech #7), recorded Δtr_M bar-decomposition as structural observation (sym 7.7% + antisym 92.3% in t=q^(1/2) basis), made fibre/observable Im(q) distinction explicit in AGENTS.md. PRs: #1580, #1585, #1587, #1594, #1599, #1603, #1609, #1615, plus this one.

## Last updated

2026-08-08 by Claude (`claude/l2-gap-prunes-2026-08-08`, PR #4788): L1 → certified
(supersedes #2444), L2 → 2/7 (m_p de-fitted 2026-07-04), Q_β row rewritten around
the c₃ truncation + the 29.96 ppb anchor swing, Δ_λ row split into proved-value vs
open-magnitude, new volume–binding row, α_EM → R2-only, active-PR table replaced.
Three rows that could not be re-verified in this pass are marked ⚠ with their
as-of date rather than silently carried forward.

> **Staleness note.** This board went 7 weeks without a refresh and in that time
> contradicted the live witnesses on both headline legs. If you are reading a row
> without a 2026-08-08 date, check the ledger it links to before relying on it.
