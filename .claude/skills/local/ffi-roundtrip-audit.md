---
name: ffi-roundtrip-audit
roles: [collaborator, owner]
description: >
  Audit Python compute scripts for Python ↔ Rust ping-pong patterns —
  Python loops that cross the PyO3 (or `subprocess`) boundary per
  iteration, instead of one boundary crossing for the whole pipeline.
  Each occurrence forfeits typically 20-50% of wall time to FFI
  marshalling + Python combine overhead (empirical: ⁶Li mass-table
  trace was 117 s back-and-forth → 95 s all-Rust, 19% saved; the
  Tier 1.A landing on PR #886).
allowed-tools: Read Bash Grep Glob Edit Write Agent
---

# FFI roundtrip audit

## Role

When a user asks "find back-and-forth Python ↔ Rust", "where are we
shuttling data across PyO3 in a loop", "FFI ping-pong audit",
"compute boundary audit", "where should we consolidate to Rust",
or "20% wall opportunity audit" — run the scanner, read the output,
and produce a ranked workplan.  Companion to
[`compute-audit.md`](compute-audit.md) but narrower: only catches
the boundary-crossing anti-pattern.  Performance-only — no
correctness change.

## When to use

- "audit FFI" / "ffi roundtrip" / "rust-python ping-pong" / "back-and-forth"
- "where are we crossing PyO3 in a loop"
- "find 20%+ wall savings via consolidation"
- After landing a new Rust kernel (sweep for callers stuck on
  per-item APIs when a batch exists or could be added)
- Before optimising a Python compute that calls `pyhecke_native`
  or `subprocess.run([rust_bin, ...])`

## What the anti-pattern looks like

A **Python loop** that calls a **Rust function** per iteration,
then does Python-side combine (mpmath, sympy, dict-merge, etc.):

```python
# ANTI-PATTERN — N FFI crossings + N Python combines
total = mp.mpf(0)
for shape in partitions:
    chi = pyhecke_native.chi_lambda_braid(shape, word, q)   # ← per-item FFI
    y = y_at_q0.get(shape)                                   # ← Python lookup
    total += y * mp.mpf(str(chi))                            # ← Python mpmath combine
```

The same compute done as a **single FFI call**:

```python
# CONSOLIDATED — 1 FFI crossing, Python only stamps the result
result_str = pyhecke_native.tr_m_atomic_mpfr(
    signed_word, n_strands, q_str, dps
)
return mp.mpf(result_str)
```

(Example from `markov_peel_rust_bridge.py:tr_M_atomic_rust_full`,
PR #886.)

## Why the cost is non-trivial

Each crossing pays:

1. **PyO3 GIL acquire + release** — ~1 µs minimum, more for larger
   args/returns.
2. **Marshal Python → Rust**: list / tuple / dict allocation + per-
   item type conversion + serialisation of `BigInt`/`BigRational`
   to decimal strings if your kernel uses them.
3. **Marshal Rust → Python**: reverse of (2), plus Python object
   construction for nested results.
4. **Python combine work** — the loop body's mpmath / sympy ops are
   often 10-100× slower than the equivalent Rust MPFR ops.

For N=100 partitions and per-call cost ~10 ms, that's ~1 s of FFI
overhead alone — ignoring the Python combine.  At N=4000 (atomic
braids in `tr_m_atomic_mpfr`'s reduced state), N ms of overhead
becomes the wall.

## Workflow

1. **Survey** — run the scanner (below) to enumerate Python files
   under `computations/` containing `pyhecke_native.`
   or `subprocess.run([..., bin_path, ...])` calls inside a loop.

2. **Classify** each finding into one of the patterns:
   - **P-F1: Per-item FFI in a Python loop.**  `for x in items:
     rust_fn(x)`.
   - **P-F2: FFI + Python combine.**  P-F1 plus a mpmath / sympy
     accumulator that should have stayed on the Rust side.
   - **P-F3: Decimal-string shuttle.**  Per-item FFI where the
     return value is a decimal string (BigInt / MPFR) that the
     Python loop re-parses to mpmath.
   - **P-F4: Subprocess-per-item.**  `subprocess.run([rust_bin,
     ...])` inside a Python loop — same anti-pattern via
     stdin/stdout instead of PyO3.

3. **Pick the fix** for each (in order of cheapness):
   - **F-A. Use the existing batch API** if one exists (e.g.
     `chi_lambdas_braid(shapes, ...)` instead of N calls to
     `chi_lambda_braid(shape, ...)`).
   - **F-B. Add a batch API** if none exists.  Typical pattern:
     `chi_q_atomic` is per-shape, has no batch.  Add
     `chi_q_atomic_all_partitions(factors, q)` to
     `tools/pyhecke-native/src/lib.rs` (delegates to a rayon-
     parallel inner loop in `tools/hecke-engine/src/seminormal.rs`
     or `wenzl_lr.rs`).
   - **F-C. Push the combine into Rust + return one scalar string.**
     The Tier 1.A `tr_m_atomic_mpfr` is the exemplar — full
     pipeline returns one MPFR decimal string.  Use this when the
     Python combine loop is non-trivial (mpmath accumulation,
     mass-table sweep, etc.).
   - **F-D. Keep the Python loop** if N is small (< 10) AND the
     per-call work is large (seconds per item).  In that regime,
     the FFI overhead is negligible.  Documented exemption — note
     in a code comment.

4. **Verify equivalence at q₀** — every consolidation must match
   the per-item version to 1e-25 relative on a representative
   atom set (matches the Tier 1.A acceptance).  Cross-check
   protocol: parallel evaluate both, assert `abs(rs - ref) / abs(ref) < 1e-25`
   on every catalogued atom.  No silent precision loss.

5. **Bench** — report wall before/after on a real atom.  The
   commit message should include a small table.

## Scanner (manual, until automated)

Run from repo root:

```bash
# P-F1 candidates: pyhecke_native call inside a `for` block
grep -rnB4 "pyhecke_native\." computations/*.py 2>/dev/null \
  | grep -B0 "for " \
  | sort -u

# P-F2 candidates: per-iteration call + mpmath/sympy accumulator
grep -rnA5 "pyhecke_native\." computations/*.py 2>/dev/null \
  | grep -B1 "mp\.mpf\|sp\.Float\|total +=" \
  | sort -u

# P-F4 candidates: subprocess.run([rust_bin, ...]) in a loop
grep -rnB4 "subprocess\.run(" computations/*.py 2>/dev/null \
  | grep -B0 "for "
```

For each candidate, manually open the file at the cited line.
The static scan has false positives (e.g. `for c, d, gen in word`
to *build* a single Rust input is fine).

## Catalogued offenders on `main` (2026-05-22)

These were enumerated during the Tier 1.A delivery (PR #886).
Each is a real ping-pong; the suggested fix is in the **Fix**
column.

| File:line | Pattern | Rust API called | N (typical) | Fix |
|-----------|--------:|----------------:|------------:|-----|
| [`compute_atom_chi_rust.py:73`](../../computations/compute_atom_chi_rust.py) | P-F1 | `chi_q_atomic(shape, factors, q)` | ~77 (H_12) | **F-B**: add `chi_q_atomic_all_partitions(factors, q)` (rayon-parallel) — no batch exists today |
| [`delta_lambda_fr_identity_phase5c.py:110`](../../computations/delta_lambda_fr_identity_phase5c.py) | P-F2 | `chi_lambda_braid(lam, word, q)` | ~77 (H_12) | **F-A**: switch to `chi_lambdas_braid(shapes, word, q)` (already in `pyhecke-native`); for the mpmath combine consider F-C |
| [`chirality_avg_content_chiral.py:174`](../../computations/chirality_avg_content_chiral.py) | P-F1/P-F2 | `chi_lambda_braid(shape, word, q)` | ~77 | **F-A** |
| [`chirality_braid_average.py:136`](../../computations/chirality_braid_average.py) | P-F1 | `chi_lambda_braid_word(shape, word, q)` | ~50 | **F-A** |
| [`constit_factor_varying_q_phase5k2.py:76`](../../computations/constit_factor_varying_q_phase5k2.py) | P-F2 | `chi_lambda_braid(lam, word_m, q_str, dps)` | ~77 | **F-A** (use `chi_lambdas_braid_mpfr`) |
| [`chirality_avg_content_atomic.py:192`](../../computations/chirality_avg_content_atomic.py) | P-F1 | `chi_lambda_braid(shape, word, q)` | ~77 | **F-A** |
| [`closed_form_tau_M_verification_phase5q.py:72`](../../computations/closed_form_tau_M_verification_phase5q.py) | P-F2 | `chi_lambda_braid` (via wrapper) | ~3 (H_3) | **F-D**: N is small, leave as-is |
| [`markov_peel_rust_bridge.py:tr_M_atomic_rust_recursive`](../../computations/markov_peel_rust_bridge.py) | P-F2/P-F3 | `tr_m_word_lq(word, n)` per reduced word | ~4000 | **F-C**: superseded on PR #886 by `tr_M_atomic_rust_full` → `tr_m_atomic_mpfr` — keep both during migration, deprecate `_recursive` after sweep |

### Status update (2026-05-29) — catalogue RESOLVED

Re-verified against the current tree (static read; line numbers drift,
so the check is by call-site shape, not line). **All seven catalogued
offenders are discharged:**

| File | 2026-05-22 fix | Current state |
|------|----------------|---------------|
| `compute_atom_chi_rust.py` | F-B | ✅ uses `chi_q_atomic_all_partitions` (batch) |
| `delta_lambda_fr_identity_phase5c.py` | F-A | ✅ uses `chi_lambdas_braid` (has a `# F-A:` comment) |
| `chirality_avg_content_chiral.py` | F-A | ✅ uses `chi_lambdas_braid` |
| `chirality_avg_content_atomic.py` | F-A | ✅ uses `chi_lambdas_braid` |
| `constit_factor_varying_q_phase5k2.py` | F-A | ✅ uses `chi_lambdas_braid` (MPFR `q_str`) |
| `chirality_braid_average.py` | F-A | ⚠️ still per-shape, but the loop is over the **3** H_3 partitions — correctly **F-D-exempt** (N small), not ~50 as originally catalogued |
| `closed_form_tau_M_verification_phase5q.py` | F-D | ✅ N=3, left as-is per F-D |
| `markov_peel_rust_bridge.py:tr_M_atomic_rust_recursive` | F-C | ✅ superseded by `tr_M_atomic_rust_full` (single PyO3 call) — `_recursive` is no longer on any production caller; deprecation is a cleanup follow-up |

No open per-item-FFI-in-loop offenders remain on the mass/binding
critical path. A fresh `awk`-window scan of
`computations/*.py` (2026-05-29) finds only batch-API
calls, docstrings/comments, and the F-D-exempt N=3 loop. See
[`docs/audits/2026-05-29-mass-binding-compute-ffi-rounding-audit.md`](../../../docs/audits/2026-05-29-mass-binding-compute-ffi-rounding-audit.md).

**Estimated wall savings** (historical, 2026-05-22): each F-A / F-B fix
saved 1.2-2× on the caller's wall; F-C saved 1.5-3×.  Combined across the
seven offenders, ~30-50% wall reduction on the H_12+ compute set — now
realised.

## Pattern catalogue (cross-reference with `compute-audit.md` §P1-P32)

P-F1/P-F2/P-F3/P-F4 are FFI-specific patterns.  They differ from
the P1-P32 patterns in `compute-audit.md` (which focus on
correctness or single-process performance):

- **P11** (recursive fn bypassing its `lru_cache`) and **P21**
  (`BlockCache` for Hoefsmit construction) — related to caching;
  orthogonal to FFI.
- **P22** (sparse representation when nnz < 0.1·dim²) — also
  orthogonal.
- **P23** (process-pool parallelism per-irrep) — *opposite* of
  P-F1/F-B: if you want parallelism, push it into rayon on the
  Rust side and call once, not into Python multiprocessing.

When a script triggers BOTH a P-F pattern and a P1-P32 pattern,
fix the P-F pattern first — the boundary is the cheapest single
change and unlocks subsequent optimisations.

## How to add a new batch API (F-B)

Pattern for adding `chi_X_all_partitions(...)`:

1. **`tools/hecke-engine/src/<kernel>.rs`**: add a
   `chi_X_all_partitions_<flavour>(n_strands, ..., q)` that
   enumerates partitions internally (use `seminormal::partitions_of`)
   and rayon-parallelises (use `rayon::prelude::*` then
   `partitions.par_iter().map(...).collect()`).
2. **`tools/pyhecke-native/src/lib.rs`**: add a `#[pyfunction]`
   wrapper that returns `Vec<(Vec<usize>, f64)>` or
   `Vec<(Vec<usize>, String)>` (MPFR decimal-string variant).
3. **`tools/pyhecke-native/Cargo.toml` + `pyproject.toml`**: bump
   the version (minor bump for new public API).
4. **`computations/<caller>.py`**: replace the
   Python loop with the batch call.
5. **Cross-check** at q₀ on a representative atom — 1e-25 rel.diff
   gate.
6. **Bench** before/after on the actual workload.
7. **Audit-doc** the change under `docs/audits/<date>-<theme>.md`.

The Tier 1.A delivery (`tr_m_atomic_mpfr`) followed this exact
pattern; it's the reference implementation for F-C.  For F-B,
see `chi_lambda_all_partitions_f64` and `chi_lambda_all_partitions_mpfr`
in `tools/pyhecke-native/src/lib.rs` (already on `main`).

## Anti-pattern in subprocess form (P-F4)

`canonical_mass_table_extended.py` (rust_f64 / rust_mpfr paths)
calls a Rust binary via `subprocess.run`.  The binary takes one
input JSON, returns one output JSON — that's *fine*, not P-F4.
P-F4 fires when the *Python loop* invokes the binary per item:

```python
# P-F4 anti-pattern (none in current repo, but watch for):
for atom in atoms:
    result = subprocess.run([rust_bin, atom_spec],
                            capture_output=True)
    parsed = json.loads(result.stdout)
    ...
```

The fix is the same as F-B: have the binary accept a list of
specs and return a list of results in one invocation.  Or
expose the kernel as a PyO3 binding and skip subprocess entirely.

## Verification harness

After every consolidation, add a cross-check test like:

```python
# Pseudo-test — cross-check old vs new path
import pyhecke_native
from old_module import old_function
from new_module import new_function_batch

for atom in test_atoms:
    old = old_function(atom)   # Python loop + per-item FFI
    new = new_function_batch(atom)  # single FFI call
    rel = abs(old - new) / abs(old) if old != 0 else abs(new)
    assert rel < 1e-25, f"{atom}: rel.diff {rel} > 1e-25"
```

The cross-check passes at 1e-25 because both paths use the same
Rust kernel internally; only the boundary differs.

## Skill output

Produce a markdown table:

```
| file:line | pattern | rust api | N | fix | est savings |
|-----------|--------:|----------|--:|-----|-------------|
| ...                                                          |
```

Plus a prose summary noting which fixes are mechanical (F-A,
F-D) vs require Rust-side work (F-B, F-C).  No code changes
from the audit pass itself — the agent that *acts* on the
audit is `compute-author` for the Rust side and a follow-up
PR for the Python side.

## Out of scope

- Numerical correctness changes (use `compute-audit` for those).
- Inner-kernel performance (e.g. BigRational GCD batching) — see
  `compute-author.md` for those.
- Architectural overhauls that change the compute graph — those
  are roadmap-level decisions, not audit-level.

## References

- [`docs/audits/2026-05-22-rust-laurent-q-reduce-results.md`] —
  the exemplar consolidation (Tier 1.A on PR #886).
- [`docs/audits/2026-05-20-compute-optimization-roadmap.md`] —
  Tier 1.A scope.
- [`docs/audits/2026-05-20-markov-peel-bottleneck-profile.md`] —
  bottleneck profile that motivated Tier 1.A.
- [`compute-audit.md`] — the broader P1-P32 catalogue (this skill
  is the FFI-specific complement).
- [`compute-author.md`] — guidance for writing new compute that
  avoids these anti-patterns up front.
