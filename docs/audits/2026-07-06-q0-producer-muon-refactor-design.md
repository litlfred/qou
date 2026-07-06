# q₀ producer→witness refactor: mechanism, traps, and safe implementation plan

**Date:** 2026-07-06
**Branch:** `claude/q0-producer-muon-source-2026-07-06`
**Bean:** [`yfvb`](../../.beans/yfvb--gap-9b-fr-frontier-producerwitness-q-refactor-prer.md) (Prereq 1)

## Problem

The ~840 committed `computations/*.witness.json` are the **muon-q₀ canonical** derivation
(AGENTS.md §"q₀ anchor convention"), but re-running any producer in a sandbox drifts its witness
**proton-ward by ~11.5 ppb** — the recurring `tnjb` bug. Root cause: `computations/substrate/q_parameter.py`
is a shim that does `from qou_substrate.constants import *`, and since the 2026-05-28 re-pin
`qou_substrate.constants.Q` is the **proton** value (`q_at()`), while the committed witnesses are muon.

## Findings (this investigation)

### F1 — the canonical value matches NEITHER current code path
| Source | q₀ (f64) |
|---|---|
| committed witnesses (e.g. `fr-pullback-k3-test`) | `1.1099785955573347` |
| `q-pinning-50-digit.witness.json` `derived_50_digit.q` | `1.10997859555733471989…` ✅ matches |
| `qou_substrate.constants.q_at()` (proton, current default) | `1.10997858275138…` ✗ |
| `qou_substrate.constants.q_muon_at()` (muon *closed form*) | `1.10997859555418…` ✗ (differs at digit ~11!) |

**So the ONLY faithful source is `q-pinning-50-digit.witness.json`.** Do **not** recompute q via
`q_muon_at()` — it gives a *different* muon value (`…5541806` vs the canonical `…5573347`). The witness
`derived_50_digit` already carries canonical strings for `q, q_inv, hbar_q, hbar_q_sq, H_A, two_q,
s_skein, z_markov`.

### F2 — closure trap: functions capture the PACKAGE globals, not q_parameter's
`q_int`, `log_q`, `q_int_err` are *defined inside* `qou_substrate.constants` and reference **that
module's** `Q`/`Q_INV`/`HA`/`LN_Q` (proton). `from q_parameter import q_int` imports the *same function
object* — still closing over proton globals. So overriding `q_parameter.Q` does **not** change what
`q_int(n)` computes. `q_int` is imported by 13 scripts. A correct single-point override **must also
re-define** `q_int`/`log_q`/`q_int_err` to close over the muon globals.

### F3 — the full family (≥22 names) must be re-derived consistently
f64: `Q, HBAR_Q, HBAR_Q_SQ, Q_INV, HA, E_CROSS, S_SKEIN, TWO_Q, TANH_LN_Q, LN_Q` (+ `_ERR` variants);
mpf `_MP` mirrors of each; `Q_50_DIGIT_STR`. A *partial* override (only Q/Q_INV/HA — what a naïve
wrapper does) leaves `HBAR_Q`, `TWO_Q`, `_MP`, etc. at proton and produces **grossly wrong** results
(an 88× B_MeV error was observed with the partial-patch wrapper).

### F4 — second choke point: `mass_at_3A_proper`
`mass_at_3A_proper.py` does `from q_parameter import Q as Q0, Q_INV as QI, HA as HA_VAL` and is imported
by many producers. It captures q_parameter's values at *its* import time, so it inherits whatever
q_parameter exports (fixed once q_parameter is corrected — no separate change needed, but it is a
second reader to include in validation).

## Recommended implementation (safe, single-point, validated)

Append to `computations/substrate/q_parameter.py`, **after** the `import *` (line 57):

1. Read `q-pinning-50-digit.witness.json` `derived_50_digit` (path: `../q-pinning-50-digit.witness.json`
   relative to `substrate/`). Take `q, q_inv, hbar_q, hbar_q_sq, H_A, two_q, s_skein` as canonical
   strings.
2. Rebind the **f64** family: `Q=float(q)`, and the rest from the witness strings where present, else
   the source formula (`E_CROSS=0.5*HA`, `TANH_LN_Q=HA/TWO_Q`, `LN_Q=math.log(Q)`).
3. Rebind the **`_MP`** family from `Q_MP=mpmath.mpf(q)` (set dps ≥ 55 first), mirroring
   `constants.py` lines 249–266 exactly.
4. Set `Q_50_DIGIT_STR = q` (the witness string).
5. **Re-define `q_int`, `log_q`, `q_int_err`** in q_parameter to close over the *new* muon globals
   (copy the bodies from `constants.py`).
6. Leave the package layer (`qou_substrate.constants`) untouched — precision/prediction scripts that
   need proton import it directly (AGENTS.md).

## Validation gate (REQUIRED before merge — the blast radius is ~840 witnesses)

- **Harness:** re-run every producer under the patched q_parameter and diff each emitted witness
  against its committed version with the provenance-drift filter
  (`computedAt|commitSha|scriptCommitSha|scriptHash|durationMs|engineVersion`). PASS = **substantive
  diff empty** for all.
- **Spot F2:** explicitly re-run a `q_int`-using producer (13 candidates) — these are the ones the
  closure trap would silently break.
- **Spot F4:** re-run a `mass_at_3A_proper`-consuming producer.
- Any producer whose committed witness is *intentionally* proton (precision dashboards importing
  `qou_substrate` directly) must be enumerated and **excluded** from the muon expectation.

**Do not merge on a sample.** A missed constant/closure corrupts the canonical layer silently; only a
full re-run+diff sweep proves correctness. This is a focused-session task with the harness above.

## Validation result (2026-07-06) — implementation landed on this branch

The override is **implemented** in `computations/substrate/q_parameter.py` (appended after the
`import *`) and validated on the FR producer:

- **q-derived content BIT-EXACT.** `fr_pullback_k3_test.py` under the override reproduces every
  `B_MeV` in `fr-pullback-k3-test.witness.json` exactly (q0_f64 = `1.1099785955573347`; all `B_MeV`
  gone from the drift-filtered diff).
- **Closure trap (F2) fixed.** `q_int(3)` now returns `3.043706218232901` (muon), matching the
  witness `[3]_q`.
- **Key correction:** derive the f64 dependents via the *same* f64 ops as `constants.py`
  (`Q_INV = 1.0/Q`, …), taking only `q` from the witness — reading `q_inv`/`hbar_q` *strings* rounds
  ~1 ULP off and perturbs `dim_q` at the ~15th digit. (`float(50-digit q)` IS bit-identical to the
  committed `q0_f64`.)

### Separate pre-existing artifact (NOT q₀, do not conflate)
The only residual diff is `B_AME_MeV` — the *experimental* literal `mp.mpf("8.4817962")` — rendered at
a different dps (committed = f64/dps-15; sandbox = dps-50), which also shifts the downstream
`ratio_pred_over_AME` / `max_over_min` at the ~16th digit. This appears in the **no-override baseline
too**, so it is an import-time-dps artifact of experimental literals, orthogonal to the q₀ refactor.
The full-sweep validation must filter (or resolve) this experimental-literal precision drift so it is
not mistaken for a q₀ regression.

### Status
Implementation is a **validated proof-of-concept on one producer**. Merge still gated on the full
re-run+diff sweep of ALL producers (design §"Validation gate") + resolving the B_AME experimental-
literal dps artifact. NOT auto-merged.

## Sweep result (2026-07-06) — the corpus is MIXED; a blanket flip is WRONG

Ran `q0_muon_reproduction_sweep.py` (numeric-tolerant diff, `rel-tol 1e-10`, which
tolerates provenance + the codata ≥50-dps experimental-precision drift while catching
q₀-scale changes) on a 10-producer sample under the muon override:

| Result | producers |
|---|---|
| **PASS** (muon-committed, reproduced) | `mass_table_l1_full_crosscheck`, `interface_quadratic_identity`, `q_block_rmatrix_spectrum` |
| **SUBSTANTIVE — committed is PROTON** | `low_isotope_binding_model_comparison`, `binding_sym_vs_lin_two_models` (both show `parameters.q0 = 1.10997858275` **proton** vs fresh muon) |
| **SUBSTANTIVE — q₀-scale diff (~1e-9…2e-7)** | `charge_coulomb_tn3he_derived`, `three_body_joint_trace_a3`, `per_bond_growth_a3`, `symmetrized_binding_closure`, `landauer_crossing_energy_probe` (magnitude = μ–p × sensitivity ⇒ also proton-committed) |

**Corpus-wide count (committed `*.witness.json` @ HEAD):**
- **279** contain the proton q₀ `1.10997858275`
- **455** contain the muon q₀ `1.109978595557`
- 1137 carry some q₀ field.

### Conclusion — the refactor is NOT a q_parameter flip
The corpus is **genuinely mixed**: ~279 producers are **proton-committed**, ~455 muon.
A blanket muon override in `q_parameter` would silently rewrite the 279 proton witnesses
to muon. So bean `yfvb` Prereq 1 cannot be a single-point flip — it needs a **per-producer
canonical-anchor decision**. The muon override (this branch) is *validated correct for the
muon producers* (3/3 PASS bit-exact), but must NOT be merged as a global default.

### OWNER DECISION REQUIRED
Are the 279 proton-committed witnesses:
- **(a) `tnjb` regressions** — they *should* be muon (AGENTS.md "computations/ is muon-canonical"),
  so the muon override is the *fix* and those 279 should be regenerated muon; or
- **(b) intentionally proton** (precision/prediction producers) — then the refactor must **tag
  the anchor per producer** and only muon-override the muon set; or
- **(c) a mix** — classify per producer.

Until this is decided, the override stays **WIP on this branch** (validated, not merged). The
sweep harness (`q0_muon_reproduction_sweep.py`) is the tool to classify the full set once the
anchor policy is set.

## CAL-layer anchor selection (owner ruling 2026-07-06) — implemented + validated

Per the owner's CAL two-layer convention: the anchor is **per-producer by CAL layer**, not a
blanket flip.
- **IDEAL / canonical 3-CAL → muon** (CAL-2 = 𝔇_β, proxy m_μ/m_e); the ~455 muon witnesses.
- **PHYSICAL-Observations → proton** (m_p/m_e, most precise); the ~279 proton witnesses.

**Implementation.** `q_parameter.py`'s override is now **gated on `QOU_Q0_ANCHOR`**: default
`physical` (proton, unchanged `import *`); `ideal`/`muon`/`canonical` applies the muon override
(witness-sourced, full family + closures). Canonical-derivation producers run muon-consistent by
exporting `QOU_Q0_ANCHOR=ideal`; physical producers leave it unset. `qou_substrate.constants`
untouched. Verified: default Q=1.10997858275 (proton), `QOU_Q0_ANCHOR=ideal` Q=1.10997859556 (muon).

**Sweep harness** (`q0_muon_reproduction_sweep.py`) now picks each producer's anchor from its own
committed q₀ signature and, when absent/ambiguous, tries **both** and keeps whichever reproduces
(auto-classify).

**Sample (10 producers):**
- **6 PASS at the correct layer** — `mass_table_l1_full_crosscheck`, `interface_quadratic_identity`,
  `q_block_rmatrix_spectrum` (muon); `low_isotope_binding_model_comparison`,
  `binding_sym_vs_lin_two_models` (proton). The two proton producers reproduce under proton (they
  failed under the earlier blanket muon), confirming the per-layer design.
- **4 residual (both anchors)** — `charge_coulomb_tn3he_derived`, `three_body_joint_trace_a3`,
  `landauer_crossing_energy_probe`, `per_bond_growth_a3`, `symmetrized_binding_closure`: ~1e-8 diffs
  that anchor-selection does NOT fix ⇒ **not q₀**. Causes seen: committed-side rounding
  (`three_body … AME_MeV = 8.4818` vs fresh `8.4817962`) + precision-path / possibly the *old*
  `q_muon_at` value (`…5541806`) in the committed witness. These are per-producer follow-ups, not
  anchor-policy issues.

### Status
The CAL-layer anchor mechanism is **implemented and validated** (opt-in, default proton, no blanket
flip — safe). Full-corpus classification + the ~4 per-producer residual fixes are the remaining
focused-session work; the auto-classifying sweep is the tool.
