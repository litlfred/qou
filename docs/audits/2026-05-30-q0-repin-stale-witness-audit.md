# q₀ re-pin — stale witness audit (the "1e-8 discrepancy" explained)

**Date:** 2026-05-30
**Trigger:** While proving the orbit-trace identity (#1483) a ~1e-8 gap
surfaced between the computed `tr_M(⁴He)` and a value quoted from the
Tier 1.A doc. This audit runs it down.

## TL;DR

The ~1e-8 gap is **not** a solver bug and **not** a sympy-vs-rust path
difference (those agree to **6.3×10⁻¹⁶**). It is an **incomplete
witness-regeneration after an intentional q₀ re-pin**:

- **2026-05-28, commit `01c18125`** re-pinned q₀ from the muon anchor
  (`m_μ/m_e`) to the **proton anchor** (`m_p/m_e` — "the most precise
  anchor", σ ≈ 2853 ppQ vs the muon's higher sensitivity). Reviewed
  (`81d3a970`, `9d90990f`). `m_μ/m_e` is now a *prediction*.
- This shifted q₀ **1.1099785955541805 → 1.1099785827513808** (~1.3×10⁻⁸),
  which propagates ~1e-8 into every derived observable (`tr_M`, masses,
  bindings).
- The regen was only **partially** done — `0aa024cb` regenerated the m_p
  substrate-identity witness ("→ 4/7"). **≈394 committed
  `*.witness.json` still carry the pre-re-pin (muon) q₀.**

## Evidence

| quantity | pre-re-pin (committed witnesses) | post-re-pin (current compute) |
|----------|----------------------------------|-------------------------------|
| q₀ | `1.1099785955541805…` | `1.1099785827513808…` |
| `tr_M(⁴He)` | `0.0553483458766980…` | `0.0553483351637685…` |

- **Path self-consistency (current):** sympy `markov_peel.tr_M_atomic(2,2)`
  vs rust-MPFR `tr_M_atomic_rust_full(2,2)` agree to `rel = 6.3×10⁻¹⁶`
  — well within the 1 ppQ L1 floor. So the compute is sound; only the
  *committed witnesses* are stale.
- `binding-canonical.witness.json` records q₀ `1.1099785955541805`
  (muon, pre-re-pin); `4he-binding-full-pipeline.witness.json` records
  `tr_M(⁴He) = 0.05534834587…` (pre-re-pin).
- `grep -l '1.1099785955541805\|0.05534834587' *.witness.json | wc -l`
  → **≈394**.

## Conclusion

- **No correctness bug** in the current compute (proton-anchored q₀,
  self-consistent to 6e-16). The re-pin is intentional, reviewed, and is
  the live value in `qou_substrate.constants`.
- **≈394 witnesses are stale** — they predate the re-pin and quote the
  muon-anchored q₀ / its downstream observables. This affects any L2
  binding-energy comparison that reads those witnesses.
- **Two stale-doc artefacts** fixed in this PR:
  - `q_parameter.py` docstring said "derived from CODATA m_μ/m_e" — now
    "m_p/m_e (re-pinned 2026-05-28; m_μ/m_e is a prediction)".
  - `orbit_trace_identity_proof.py` hard-coded the pre-re-pin
    `tr_M(⁴He)`/`tr_M(⁵Li)` as the "canonical" sanity reference (the
    source of the original confusion); updated to the post-re-pin values
    and the proof doc's "sympy-vs-rust nuance" note corrected to this
    re-pin staleness.

## Systemic fix — the staleness gate is q₀-blind (root cause)

The deeper finding: **`run_pipeline.py`'s staleness check keys on the
producer script's `scriptHash`** (file content + deps), so a constant
re-pin that touches *no producer script* — exactly what the q₀ re-pin
was — is **invisible to it**. The pipeline cheerfully reports all 392
stale witnesses as "fresh". This is why the re-pin silently left a
two-month staleness window.

**Detector landed this PR:**
[`witness_constant_staleness.py`](../../computations/substrate/witness_constant_staleness.py)
scans every `*.witness.json` for q₀-shaped decimals (`1.10997…`) that
differ from the live `Q_50_DIGIT_STR` and flags them. Confirmed it
detects **392** stale witnesses (`1.109978595554` muon vs
`1.109978582751` proton). Modes: bare report, `--strict` (exit 1 for
CI), `--list` (full list, drives the regen). Wiring it into
`witness-pipeline.yml` closes the gate the `scriptHash` check leaves
open — any future constant re-pin auto-flags its blast radius.

## Recommendation — batched regen is a dedicated job, not interactive

**Complete the q₀ re-pin regeneration sweep.** This is a *known-good
mechanical sweep* — re-run the witness producers against the current
proton-anchored q₀ (the value is already live in
`qou_substrate.constants`; both compute paths agree to 6e-16, so the
regenerated values are trustworthy). It should be batched (per the
`compute-integration-watcher` / `integration-backlog` sweep discipline)
and cross-checked against the m_p anchor identity that `0aa024cb`
already validated (4/7). The new `WitnessBuilder.environment` block
(landed this session) records exact lib versions on each regenerated
witness so future drift is attributable.

**Cost finding (measured this session):** a single producer
(`run_pipeline.py --force <one witness>`) takes **~2.5 min** because
`--force` runs the *dependency cascade* (one producer pulled in 13
downstream witnesses before timing out at 2m30s; that partial run was
reverted). At ~2.5 min × 392 that is a **~15-hour** job — a dedicated
batch/CI run with progress logging (per AGENTS.md "Long-compute logging
discipline"), **not** an interactive session task. Recommended shape:
a `q0-repin-regen.yml` workflow (or an overnight `nohup` batch) that
walks `witness_constant_staleness.py --list`, regenerates in dependency
order, and re-runs the detector with `--strict` as the green gate.

Quick triage list (or use the detector's `--list`):
```bash
python3 computations/substrate/witness_constant_staleness.py --list
grep -rl '1.1099785955541805' computations/*.witness.json
```
