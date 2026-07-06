# Wiring q-Bessel-2nd-kind corrections into `m_sym` / `m_qCLT` — what can go to production, and the blockers (2026-06-15)

**Branch:** `claude/vigilant-brown-x0tzat`
**Owner request:** "wire up into production all that we can. what are blockers?"
**Discipline gate:** [`production-vs-exploratory-discipline`](../../.claude/skills/local/production-vs-exploratory-discipline.md)
+ CLAUDE.md §"Δ_λ gate" (no 7th ansatz).

## TL;DR — the honest production verdict

The **production observable layer** (`mass_table_ppb.py`, `per-observable-100x-status.witness.json`,
`onepb-status-dashboard.witness.json`, the cheat-sheet "closed" status) **cannot
take any of this**, because every candidate either (a) misses on the gated
nucleon-mass gap (+2.89 %, Subgoal-2, owner-declined 2026-05-08) or (b) rests on
the still-open Δ_λ exponent keystone (`10A−5 = 5(2A−1)`, being worked on PR #2316),
or (c) contains a non-derived bond-graph modeling choice. Promoting any of them
to a production observable would be exactly the CAL-4 antipattern the discipline
skill exists to stop.

What **can** be wired is the **canonical-infrastructure channel** with derived
inputs, plus a derive-or-refute probe:

| item | target | category | verdict |
|---|---|---|---|
| 1 | factorized bond-type q-CLT → `m_qclt_approx.py` | CANONICAL INFRASTRUCTURE | **WIRE** — derived inputs (per-bond-type sub-braid traces + E₀), resolves T/³He split |
| 3 | `2cosh(10η₀)` vs `Δ_λ^sym` residual | EXPLORATORY probe | **PROBE** (derive-or-refute), not a production wire |
| 2 | PR #2316 keystone (`10A−5` from Bring crossings) | coordination | read + coordinate; it is THE gate |

## The corrections, traced

`m_sym` = `m_symbolic` ↔ binding form `B_sym = α·ln(tr_free/tr_atom)` (exact
Kashaev log-trace). `m_qCLT` = `m_qCLT_approx` ↔ `B_qCLT`. The q-Bessel
second-kind work (q-Lommel **order** recurrence, `b = q₀¹⁰+q₀⁻¹⁰ = 2cosh(10η₀)`,
[`QLommelOrderRecurrence.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/QLommelOrderRecurrence.lean))
supplies two distinct things:

1. a **derived** binding *correction* for the `B_qCLT` channel — the factorized
   bond-type form `B = α·Σ_i ln|V_i|` already prototyped (exploratory) in
   [`binding_single_pipeline_comparison.py`](../../computations/binding_single_pipeline_comparison.py);
   its `V_i` are 2-nucleon sub-braid trace ratios (p-p 0.69 / p-n 0.93 / n-n 1.24),
   all from the one canonical transfer path — **no fit**;
2. a **near-match** structural law for the Δ_λ residual (`b = 2cosh(10η₀)`,
   second-kind branch `β/α ≈ 0.43`), which item 3 tests against the *exact-log*
   residual `Δ_λ^sym = B_AME/B_sym` rather than the linear `Δ_λ^lin`.

## Blockers (the answer to "what are blockers?")

1. **Nucleon-mass gap +2.89 %** — caps the *absolute* accuracy of any mass
   channel. It is Subgoal-2 (100× target below the CAL-2 ~780 ppb floor), which
   the coordination ledger **declined** on 2026-05-08 (requires substrate
   derivation of q₀). Not removable here. The derived spectral-phase factor
   θ/(8ℏ²) closes it ~35× but is itself EXPLORATORY/unwired (its "why" is a Lean
   `True := by trivial` stub — **pre-promotion requirement P1 below**). ⇒
   `m_qclt_approx` stays a structural estimator, not a ppb observable.
2. **Δ_λ exponent keystone OPEN** — the binding *production* formula
   `B(K) = m_e·Σ_λ y_λ χ^λ Δ_λ` needs `Δ_λ`, whose `q₀^{10A−5}` exponent
   `10A−5 = 5(2A−1)` is not yet derived from Bring's-surface crossings (PR #2316).
   Until it lands, wiring a closed Δ_λ would be the forbidden **7th fit-ansatz**.
3. **Bond-graph modeling choice** — the factorized q-CLT's chain-(A−1) vs
   all-pairs-C(A,2) bond count is *not derived* (audit's own caveat); A≥4
   undershoots ~1.6×. ⇒ `B_qCLT` is a ~1–1.6× estimator, fine for infrastructure,
   not for a production prediction.
4. **Lean env down** — `release.lean-lang.org` is firewalled in this sandbox
   (`failed to parse release data`). Any `.lean` touch needs the `lake-cache/qou-*`
   orphan-branch restore (CLAUDE.md §"VERIFY a single file with lean-direct").
   Items 1 & 3 are Python + witness only, so this does not block them.

## Pre-promotion requirements (must clear BEFORE any production wire)

- **P1 — replace the spectral-phase `True := by trivial` stub.** The
  θ/(8ℏ²) "why" step (consumed by `spectral_correction_borromean`) is a vacuous
  `True` proposition. Per CLAUDE.md §"No shadowing stubs" + `lean-proof-vacuity-audit`,
  a vacuous `True` must be replaced with a concrete statement (target type +
  surjective/convergence map encoding the intended property) before the spectral
  regime may move from EXPLORATORY → production. Tracked here so it is not lost;
  out of scope for this PR (we are *not* wiring the spectral regime — item 1 uses
  the derived factorized bond-type form, not θ/(8ℏ²)). Raised by Gemini on #2325.

## Coordination (2026-06-15, `/coordinate`)

Scope map — **no open overlapping siblings remain**; the q-Bessel/Δ_λ/binding
theme has consolidated onto `main`:

| PR | state | relationship | action |
|---|---|---|---|
| #2316 Δ_λ q₀⁵-per-site | **merged 19:37Z** | the open keystone (`10A−5 = 5(2A−1)`) — now `main` notes | rebased onto its landings; keystone still framework-open (blocker 2) |
| #2320 single-pipeline B_sym/B_qCLT | **merged 17:30Z** | source of the factorized q-CLT I lift (item 1) | rebased; lifting from `main` |
| #2285 i9 de-float | open | mass-table CODATA de-float; **zero file overlap** with `m_qclt`/low-isotope | no intent comment (not genuinely overlapping — avoids noise) |

Because #2316 merged with the keystone **explicitly open** ("framework-standing
complex-q item, not a session-sized chip"), blocker 2 stands: no closed Δ_λ to
wire. Ledger: `docs/coordination/2026-06-05-step9-binding-closure.md`.

## Status checklist

- [x] Read discipline skill; rebase onto origin/main (+2 witness-validator commits)
- [x] Blocker analysis (this doc)
- [x] Item 2 — coordinate: #2316 & #2320 merged (no open overlapping siblings); rebased onto landings
- [x] Item 1 — wired factorized bond-type binding into `m_qclt_approx.py` (+ witness, 6 green; resolves T/³He)
- [x] Item 3 — derive-or-refute probe (witness, 3 green): 2nd-kind `b` → `Δ_λ^lin` (m_qCLT), not `Δ_λ^sym` (m_sym)
- [x] Updated `q-clt-jsj-mass-scaling.md` channel-2 (factorized derived binding; `bun run validate` exit 0)
- [x] Consolidated audit: [`2026-06-15-qbessel-2ndkind-msym-mqclt-wiring.md`](../audits/2026-06-15-qbessel-2ndkind-msym-mqclt-wiring.md)

**Done.** Production observable layer stays gated (blockers 1–2, framework-level).
Wired: m_qCLT infrastructure factorized derived binding. Disambiguated: 2nd-kind
correction belongs to m_qCLT (linear), already realized by m_sym (log-trace).
