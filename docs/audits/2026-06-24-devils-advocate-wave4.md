# Devil's-advocate audit — Wave 4 (Hecke/trace machinery) + mechanical sweep

**Watcher:** [`local/devils-advocate-watcher`](../../.claude/skills/local/devils-advocate-watcher.md)
**Date:** 2026-06-24 · **Branch:** `claude/lucid-gates-92e98s`
**Model:** claude-opus-4-8 · L1–L4 lenses + adjudicator.

Wave 4 covers the Hecke/trace machinery: the Markov-trace inductive limit, the H₃ Markov–Wenzl weights, the Hoefsmit binding amplitude, the Q_β bar-even kernel invariant, and the Brunnian property. It also introduces the two **mechanical checkers** built to sweep the two recurring failure classes corpus-wide (classes 2 & 3 from the wave-1–3 tally).

## Results (5 blocks)

| Block | Verdict | Strongest objection |
|-------|---------|---------------------|
| [`markov-trace-inductive-limit`](../../content/quantum-observable-universe/braids-and-knots/markov-trace-inductive-limit.md) | 🟡 survivable | Lean **asserts** the per-n trace conclusions by constant assignment (`tau_identity:=1`, …) rather than **deriving** them from the global trace; and `τ_M : B_∞→ℝ` mislabels the domain (the Jones trace lives on the **Hecke tower**, not the braid group). |
| [`q-beta-bar-even-kernel-invariant`](../../content/quantum-observable-universe/mass-theory/q-beta-bar-even-kernel-invariant.md) | 🟡 survivable | The headline **iff** ("clean integer-u ladder ⟺ R bar-even") is asserted; the Lean formalizes only the N=2 prototype's three `ring` identities. |
| [`hoefsmit-binding-amplitude`](../../content/quantum-observable-universe/braids-and-knots/hoefsmit-binding-amplitude.md) | 🟢 clean | Only the citation (`wenzl1988c` placeholder, already CI-flagged `bib-cite-resolves: FAIL`; the Hoefsmit thesis `hoefsmit1974` is uncited). Math is exact + Lean-verified. |
| [`h3-markov-wenzl-weights`](../../content/quantum-observable-universe/mass-theory/h3-markov-wenzl-weights.md) | 🟢 clean | Boxed closed forms not formalized (Lean proves only the q=1 normalization); honestly deferred, rigorous prose proof. |
| [`brunnian-property-of-borromean`](../../content/quantum-observable-universe/particle-interactions/brunnian-property-of-borromean.md) | 🟢 clean | Sanctioned §3b-cond conjecture; only "quarks … *exactly* the Brunnian property, no dynamical assumption" overstates a kinematic analogy (partial). |

Wave 4 is the cleanest wave (3 clean) — the Hecke/trace machinery is mostly honest about its deferred-formalization status. The two survivable findings are both **assert-vs-derive** gaps (a recurring class-1 pattern).

## Mechanical sweep — the two cheap checkers

Built to operationalize the two recurring classes the per-block waves surfaced ≥3× each. Both are **report-only by default** (exit 0; `--strict` to gate), **agent-free**, stdlib-only, and do **not** write `da-*` sidecars (the da-axis is agent-only) — they feed the watcher's backlog.

### Class 3 — witness hollowness → [`computations/witness_hollowness_audit.py`](../../computations/witness_hollowness_audit.py)

Two offence kinds over 1593 active witnesses (skips `_deprecated/`):

- **`null-dual` — 11 witnesses.** LP/SDP/operator-selection witnesses whose dual certificate (`y0_star`/`y_star`/`active_set`/`duality_gap`) is emitted as keys with **null values**. This **generalizes the wave-3 `operator-selection-lp` open-objection into a corpus-wide pattern** — `lp_dual_witness_validator.py` checks key *presence*, so all 11 pass CI while computing no shadow prices. The 11:
  `confinement-operator-selection`, `binding-lp-delta-audit`, `e-0-lp-dual-h3`,
  `rho-k-h3a-wenzl-bridge`, `shadow-price-c-321-q0`, `toffoli-lp-stability`,
  `wedderburn-lp-ew-wiring`, `compound-binding-via-differences`,
  `delta-n2-placeholder-audit`, `deuteron-delta-i-audit`,
  `sweeps/paper-six-term-shadow-price-sweep`.
- **`hollow-verification` — 401 witnesses (high-recall advisory).** Witnesses with an explicitly empty `assertions: []` + a success claim and no other validation array. High-recall; triage before acting.

**Recommended follow-up (not in this PR):** harden `lp_dual_witness_validator.py` to reject null dual *values* under `--strict` (the one-line fix that would have caught all 11), and recompute the 11 duals via `lp_dual_solver.py`.

### Class 2 — status-label overclaim → [`computations/status_label_overclaim_audit.py`](../../computations/status_label_overclaim_audit.py)

Flags blocks wearing a **closure label** (`proved` / `closed-form` / `no-fit` / `RESOLVED` / `sorry-free` / `✅ proved`) over a **non-closure signal** in the same triple (`.lean` `sorry`/`:True`/`:=trivial`, `validation:not_checked|stub`, `status:experimental`, `kind:conjecture`).

- **227 candidates total** (high-recall).
- **95 SHARP** — closure label over a `.lean` `sorry`/`:True`/`:=trivial` (the genuine vacuity-overclaim). Examples: `qbeta-ck-truncation-canonical` (already a wave-1 finding), `b1-figure-8-row-theorem` ("proved" over `: True`), `depth-2-identification-bloch-suslin`, `wenzl-positivity-implies-substrate-positivity`, `binding-qbeta-complex-volume`.

The 95-sharp subset is the actionable class-2 backlog; `qa:fail` was deliberately dropped as a signal (stale bib criteria flooded it).

## Running tally (waves 1–4, 19 blocks)

**3 open-objection · 11 survivable-objection · 5 clean.** The mechanical sweep now quantifies the two cheapest-to-fix recurring classes at corpus scale: **11 null-dual witnesses** and **95 sharp status-label overclaims** — both far larger than the per-block waves alone revealed, and both addressable by a script + a focused PR rather than block-by-block agent audits.
