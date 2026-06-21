# Q_β residue-A — fibre-level KLR / crystal kernel: research scope (2026-06-05)

## Status: OWNER-AUTHORIZED multi-session research (kickoff doc)

The owner authorized the deep path on 2026-06-05 (after PR #1811's Step-4
finding that the single-formula route is saturated). **This document scopes
the program; it does NOT claim a result and contains no compute.** The heavy
work belongs in future *focused* sessions (one tranche at a time — long
mega-sessions are the observed failure mode).

This is the productive direction the cal-anchored acceptance left open
(GAP-A-3 / GAP-A-4 + Option E); it is **not** a 7th single-formula ansatz
(forbidden — see below).

## The target

Construct a **fibre-level** element `F(q)` (Habiro ring `Habiro(ℤ)` /
KLR-categorified object) whose **archimedean evaluation** at each `q₀` anchor
reproduces the observed Q_β `c_3` — the "residue A" that the single-formula
search could not derive.

Residue magnitude at the proton-pinned `q₀`: `A ≈ 1.804e-15`
(per [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
"Still active" row).

## What is already DEAD — do NOT re-attempt (corpus-checked)

| Route | Verdict | Source |
|---|---|---|
| Single real formula `c_3 = f(q₀)` | **SATURATED** — 28 candidates; formally cal-anchored | [`docs/audits/2026-06-03-qbeta-residue-a-cal-anchored-acceptance.md`](../audits/2026-06-03-qbeta-residue-a-cal-anchored-acceptance.md) |
| Finite roots of unity | **REFUTED** (nearest singularity 2.5e5× closer than any RoU) | PR #1821 |
| Real-q `[3]_q/25` form | **FALSIFIED** across anchors (rigid 2.5e7×) | PR #1811 Hopf probe + rigidity audit |
| Bar-even invariant | shipped — not a `c_3` closure | PR #1875 |
| Odd-parity avatar (closed-form) | **SATURATED** (`c_3 = g`; 9 candidates NEGATIVE) | PR #1880 |
| Single Markov-stabilization | **REFUTED at trace level** (z<1; identity-trace = 1 ≠ 2.53) | PR #1850 |
| Demazure n ≤ 5 | **NEGATIVE** | chain-4 n=5 verdict |
| **7th single-formula ansatz** | **FORBIDDEN** (3-calibration discipline) | AGENTS.md §Δ_λ gate |

## Critical framing — fibre vs observable (AGENTS.md)

The `c_k` live in the **fibre** (formal `q`, potentially complex). Do **not**
search for a real `f(q₀)` — that is the known-dead single-formula route. Search
for a fibre-level `F(q)` whose **archimedean evaluation** (post-`τ` functor) at
any `q₀` reproduces `c_3` at *that* anchor. The cross-anchor "swing" repeatedly
caught as a near-match is precisely the signature of a fibre object with
structure beyond a real constant — i.e. a complex-analytic `c_3(q)` evaluated at
real `q₀`. (`lusztig_q_0_imaginary_part_zero` is an *archimedean* constraint on
the evaluation, **not** a fibre claim — do not conflate the two levels.)

## The honest KLR / crystal caveat — READ FIRST

AGENTS.md §7b lists Type-B folding / KL-decategorification / Demazure
sub-crystals as **authoring guidance, not a closure shortcut**. The
[2026-05-30 KLR dialog assessment](../audits/2026-05-30-klr-dialog-assessment.md)
found **0/6 candidate proofs would meaningfully shorten** with a KLR layer.
Recurrent re-pitch failure modes (do **not** repeat): re-introducing the purged
`λ_scale`; Bloch–Wigner / dilog-transcendence on the (non-hyperbolic) trefoil.
KLR is **not** magic — it is a possible organizing language for the
brane-tower-level-selection question, nothing more.

## Foundation (from PR #1811 — merging)

The verified
[`MarkovTraceOnHecke.lean`](../../content/quantum-observable-universe/lean/QOU/Machinery/MarkovTraceOnHecke.lean)
(concrete H₃ Markov trace + cyclicity), plus `trace_formal.py` (formal-q Markov
trace over `ℚ(s)`) and `gram.py`'s `markov_trace_combo`, are the algebraic
substrate. The residue-A element, if it exists, is a `Habiro(ℤ)` element whose
Markov trace / archimedean evaluation yields `c_3`. (This branch is based on
`main`; rebase once #1811 lands to pick up the machinery.)

## First tractable sub-goals (future sessions, in order)

1. **Pin the archimedean evaluation map** `τ : Habiro(ℤ) → ℝ` at `q₀`. What does
   `τ` do to a Habiro element? (Parallels the `α_EM` element `[2]_q·(1−h²α)`, PR #1511 — a fibre-level
   element whose *real* Taylor coefficients are what get evaluated; here
   `h = q−q⁻¹` is the fibre-level Hecke parameter, **not** the observable
   `ℏ_q`.)
2. **Categorical residue identification.** Is `A ≈ 1.804e-15` equal to `ℏ_q^N`?
   `b^N·ℏ_q^M`? `Q_β·ε_struct`? Re-derive at the proton-pinned `q₀`
   (1ppq-qbeta.md "Still active").
3. **Crystal-component selection.** Does the Kashiwara crystal / KLR canonical
   basis of `H_n(q)` distinguish the `c_3`-carrying component? This is the
   GAP-A-3 brane-tower-level-selection question stated categorically.
4. **Discipline gate (every step).** 3-calibration compliant; no 7th fit;
   fibre-vs-observable kept distinct; nothing wired to production until a
   *derivation* (not a near-match) is in hand. The
   production-vs-exploratory-discipline review will catch a fit.

## Out of scope / hard gates

- **Absolute `m_p` / `m_n` / `⁴He` closure** (L2 Subgoal-2) — owner *declined*
  2026-05-08; this program is about `c_3`'s fibre origin, not substrate
  derivation of `q₀`.
- **Any single-formula fit** — forbidden.
- This doc is **scope only**: no code, no `c_3` claim, nothing wired.

## Cross-refs

- [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md) — master ledger (this kicks off the "Still active" `F(u)` row)
- [`docs/audits/2026-06-03-qbeta-residue-a-cal-anchored-acceptance.md`](../audits/2026-06-03-qbeta-residue-a-cal-anchored-acceptance.md)
- [`docs/audits/2026-05-30-klr-dialog-assessment.md`](../audits/2026-05-30-klr-dialog-assessment.md) — recurrent re-pitch failure modes
- PRs: #1811 (Markov-trace machinery foundation), #1850, #1821, #1875, #1880
- AGENTS.md §7b (symmetric-crystal authoring guidance), §"Im(q) fibre vs observable", §Δ_λ gate
