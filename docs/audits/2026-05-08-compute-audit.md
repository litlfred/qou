# Compute Audit — Performance & Correctness Sweep

**Date**: 2026-05-08
**Branch**: `claude/audit-content-blocks-hzjAf`
**Skill**: `local/compute-audit`
**Scanner**: `computations/compute_audit_scan.py`
**Witness**: `computations/compute-audit-scan.witness.json`

Companion to `2026-05-08-content-block-audit.md` — the content-block
audit covered correctness/hygiene of `.ts/.md/.lean` triples; this
audit covers Python compute scripts under
`computations/` against the 30 patterns
(P1–P16 correctness, P17–P30 performance) catalogued in the skill
spec.

---

## 1. Headline numbers

| Metric | Count | Status |
|---|---:|---|
| Python compute scripts scanned | 245 | — |
| Total findings | 260 | — |
| **P14 — pickle cache (RCE risk)** | **1** | ❌ correctness/security |
| **P15 — `sp.cancel` on huge rationals (>120 s walls)** | **64** | ❌ perf |
| **P16 — `sp.simplify` before `evalf` (>30 min stalls)** | **71** | ❌ perf |
| **P17 — `sympy.Expr` where `LaurentQ` should be used** | ~70 of 75 sympy users (6 adopted) | ❌ perf |
| **P21 — Hoefsmit callers not using shared `BlockCache`** | **21** | ❌ perf |
| P30 — witness JSON missing `scriptHash` / `scriptFile` | 103 | ❌ staleness-tracking |
| Patterns with **0** hits (P1–P13, P18–P20, P22–P29) | 22 of 30 | ✓ |

---

## 2. Top-pressure files

### P15 (`sp.cancel`) — replace with `sp.together` + `sp.div`
*(P18 reference fix landed on `term6_residues_at_roots.py`: deuteron 30 min → 1.2 s)*

| File | hits |
|---|---:|
| `markov_weights_symbolic.py` | 10 |
| `markov_trace_atomic_proton_full.py` | 9 |
| `shift_from_nf_basis.py` | 8 |
| `hoefsmit_symbolic.py` | 5 |
| `markov_trace_axiomatic_proton.py` | 5 |
| `alpha_shift_torus.py` | 4 |
| `hecke_character_symbolic.py` | 4 |
| `ocneanu_cancellation_derivation.py` | 4 |
| `beta_ew_delta_I_full_spectrum.py` | 3 |
| `habiro_coefficients_atomic.py` | 2 |

### P16 (`sp.simplify` before evalf) — add `simplify=False` flag
*(2834792d on ³He: profile showed `sp.simplify` was the cost, not the loop)*

| File | hits |
|---|---:|
| `schur_weyl_symbolic.py` | 11 |
| `gb_filtration_jet_tracker.py` | 8 |
| `hecke_symbolic.py` | 7 |
| `probe_term4_conventions.py` | 7 |
| `atom_nf_symbolic_D.py` | 6 |
| `frobenius_partition_sum.py` | 6 |
| `hecke_core_symbolic.py` | 4 |
| `y_lambda_symbolic_validate.py` | 4 |
| `witness_polynomial.py` | 3 |
| `beta_ew_delta_I_eigenvalues.py` | 2 |

### P21 (BlockCache not wired) — 21 numerical Hoefsmit callers
The skill spec (P21) explicitly says these 21 should be using
`syt_prefix_cache.BlockCache`. Files:

`alpha_k_jones_markov_h3.py`, `alpha_shift_torus.py`,
`beta_ew_delta_I_full_spectrum.py`,
`beta_ew_delta_I_numerical_spectrum.py`, `canonical_tower.py`,
`conjugate_symmetry.py`, `hecke_character_symbolic.py`,
`hecke_characters.py`, `hecke_wedderburn.py`,
`hoefsmit_symbolic.py`, `light_isotope_sweep.py`,
`markov_weights_symbolic.py`, `mass_at_3A_proper.py`,
`ocneanu_cancellation_derivation.py`,
`paper_six_term_shadow_price_sweep.py`,
`probe_atom_shell_self_duality_mpfr.py`,
`probe_d_height_stratification.py`,
`probe_gamma_gamma_lr_embed_h6.py`,
`probe_sdp_canonical_paper_formula.py`,
`staircase_ew_disjoint_spectrum.py`, `tr_m_wenzl_bridge_mpfr.py`.

### P14 — pickle cache (security)

`mass_at_3A_proper.py:1` uses `pickle` for `.pkl` cache files.
Per pattern catalogue (0eda79c6), this is an RCE vector on a
tampered cache. Replace with JSON of `str(sympy.Expr)` and re-`sympify`
on load.

### P17 — LaurentQ wiring

| Status | Count |
|---|---:|
| Files using `laurent_q` / `LaurentQ` | 6 |
| Files using `sympy` | 75 |
| **Files using sympy without LaurentQ migration** | **70** |

Sweet spot for migration is A=3 (3–6× speedup); A≥5 the gain fades.
Triage these 70 by the atom size they target; migrate only the
A=3 (and a few A=2) callers, keep the slow path as opt-out
(per the skill's anti-pattern rule "never remove the slow path").

---

## 3. Highest-leverage files (multi-pattern hits)

| File | patterns | total hits |
|---|---|---:|
| `markov_weights_symbolic.py` | P15, P16, P21, P30 | 14 |
| `schur_weyl_symbolic.py` | P16, P30 | 12 |
| `markov_trace_atomic_proton_full.py` | P15, P30 | 10 |
| `gb_filtration_jet_tracker.py` | P16, P30 | 9 |
| `hecke_symbolic.py` | P15, P16 | 9 |
| `probe_term4_conventions.py` | P16, P30 | 8 |
| `shift_from_nf_basis.py` | P15 | 8 |
| `atom_nf_symbolic_D.py` | P16, P30 | 7 |
| `frobenius_partition_sum.py` | P16, P30 | 7 |
| `hecke_character_symbolic.py` | P15, P16, P21, P30 | 7 |
| `hoefsmit_symbolic.py` | P15, P21 | 6 |
| `markov_trace_axiomatic_proton.py` | P15, P30 | 6 |
| `alpha_shift_torus.py` | P15, P21 | 5 |
| `beta_ew_delta_I_full_spectrum.py` | P15, P21, P30 | 5 |
| `ocneanu_cancellation_derivation.py` | P15, P21 | 5 |

---

## 4. Workplan (priority-ordered)

### P0 — security (immediate)

1. **Replace `pickle` in `mass_at_3A_proper.py`** with JSON +
   `sympify`. Single file, ~30 min. Skill: P14.

### P1 — biggest wins (1–2 days each)

2. **Add `simplify=False` flag to the top-5 P16 files**
   (`schur_weyl_symbolic.py`, `gb_filtration_jet_tracker.py`,
   `hecke_symbolic.py`, `probe_term4_conventions.py`,
   `atom_nf_symbolic_D.py`). Default `True` for back-compat;
   evalf-only callers pass `False`. Pattern: P16, reference
   commit `2834792d`. Verification: ³He benchmark
   `Δ < 1e-15` at q₀.

3. **Replace `sp.cancel` with `sp.together` + `sp.div` in the
   top-5 P15 files** (`markov_weights_symbolic.py`,
   `markov_trace_atomic_proton_full.py`, `shift_from_nf_basis.py`,
   `hoefsmit_symbolic.py`, `markov_trace_axiomatic_proton.py`).
   Pattern: P15 / P18, reference fix `term6_residues_at_roots.py`
   (18fce929). Verification: deuteron 30-min wall ⇒ ≤ 5 s.

4. **Wire `BlockCache` into the 21 P21 callers.** Use
   `syt_prefix_cache.BlockCache`; `ocneanu_weights` already
   demonstrates the integration. Order: start with the multi-hit
   files (`markov_weights_symbolic.py`,
   `hecke_character_symbolic.py`, `hoefsmit_symbolic.py`,
   `alpha_shift_torus.py`, `beta_ew_delta_I_full_spectrum.py`,
   `ocneanu_cancellation_derivation.py`).

### P2 — broader migration (1 week)

5. **LaurentQ migration for A=3 callers (P17).** Triage the 70
   sympy-only files by target atom size; migrate the A=3 ones
   (3–6× speedup). Keep the slow path with `use_fast=False`
   opt-out flag. Reference: `hecke_laurent_fast.py` /
   `laurent_q.py` (79ca1200).

6. **Sweep remaining P15 (59 hits) and P16 (66 hits)** in the
   long tail. Most are 1–2 hits per file and trivial to fix.

### P3 — staleness-tracking (background)

7. **Backfill P30 (`scriptHash` / `scriptFile`)** in the 103
   witness JSONs that lack them. Use `WitnessBuilder` per
   `witness_base.py:136-183`. Without these, `run_pipeline.py`
   (lines 152-177) treats hand-written witnesses as current and
   silently skips regeneration — masking staleness across
   substrate-parameter sweeps.

---

## 5. Estimated speedup

If P0–P1 land cleanly:

| Workload | Before | After (estimated) |
|---|---|---|
| `term6_residues_at_roots.py` deuteron | 30 min (already fixed) | 1.2 s ✓ |
| `markov_weights_symbolic.py` per-atom | minutes-to-tens-of-minutes | seconds (P15+P16+P21+P17) |
| `hecke_character_symbolic.py` Wedderburn pass | tens of minutes (P15+P16+P21) | minutes |
| `³He / ⁴He` Markov trace pipeline | dominated by P16 | sub-minute |

Numbers extrapolated from prior fixes in the 50-commit pattern
catalogue (skill spec §"reference fixes"); each landed PR must
emit its own per-atom benchmark table per P28.

---

## 6. Anti-patterns this audit explicitly rejects

Per the skill's "Anti-patterns" section (lines 224-232):

- **Removing the slow path.** Always keep `use_fast=False` opt-out.
- **Numerology**: pattern-matching numerical agreement without
  categorical derivation.
- **"Three-route convergence" / "universal extrapolation"** without
  a single concrete derivation chain.

If a remediation PR drifts into one of these, reject it and
demand the categorical derivation first.

---

## 7. What this audit did **not** cover

- **Profile-driven verification** (P29). The scanner is static;
  it cannot tell whether a `sp.simplify` is the actual hot path
  in any given run. Before landing each P15/P16 fix, profile the
  target script with `python -X importtime` or `cProfile` to
  confirm the bottleneck.
- **Numerical equivalence at q₀** for any candidate fix. Each
  remediation PR must include the cross-check (skill §"verification
  checklist", item 1).
- **Cross-paper compute** (UGB, Fred2005). Scope was QOU only.
