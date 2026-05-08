# Compute Audit & Workplan — 2026-05-08

**Skill:** [`local/compute-audit`](../../.claude/skills/local/compute-audit.md)
**Scanner:** [`folio-assistant/computations/compute_audit_scan.py`](../../folio-assistant/computations/compute_audit_scan.py)
**Witness:** [`folio-assistant/computations/compute-audit-scan.witness.json`](../../folio-assistant/computations/compute-audit-scan.witness.json)

The 30 patterns (P1–P30) are extracted from a 50-commit review of
QOU compute landings 2026-04 → 2026-05; full catalogue and references
live in the skill file.  Group A (P1–P16) is correctness; Group B
(P17–P30) is performance.  The static scanner mechanically detects
P11, P14, P15, P16, P21, P30; the rest require semantic review.

## Scanner findings (245 files scanned, 261 hits)

| Pattern | Hits | One-line meaning |
|---|---:|---|
| P14 | 1   | `pickle` for cache files (RCE-on-tamper risk) |
| P15 | 64  | `sp.cancel` on full rational expression |
| P16 | 71  | `sp.simplify` before numerical `evalf` at q₀ |
| P21 | 21  | Hoefsmit construction without `BlockCache` |
| P30 | 104 | `.witness.json` written without `WitnessBuilder` |

### Top-15 files by finding count

```
markov_weights_symbolic.py            14  (P15,P16,P21,P30)
schur_weyl_symbolic.py                12  (P16,P30)
markov_trace_atomic_proton_full.py    10  (P15,P30)
gb_filtration_jet_tracker.py           9  (P16,P30)
hecke_symbolic.py                      9  (P15,P16)
probe_term4_conventions.py             8  (P16,P30)
shift_from_nf_basis.py                 8  (P15)
atom_nf_symbolic_D.py                  7  (P16,P30)
frobenius_partition_sum.py             7  (P16,P30)
hecke_character_symbolic.py            7  (P15,P16,P21,P30)
hoefsmit_symbolic.py                   6  (P15,P21)
markov_trace_axiomatic_proton.py       6  (P15,P30)
alpha_shift_torus.py                   5  (P15,P21)
beta_ew_delta_I_full_spectrum.py       5  (P15,P21,P30)
ocneanu_cancellation_derivation.py     5  (P15,P21)
```

## Ranked workplan

Items are ordered by **(impact / risk-of-regression)**.  Each item
cites the matching pattern and a prior successful instance.

### Tier 1 — Safe & high-leverage (begin immediately, **no questions**)

1. **Skill + scanner + workplan landed (this PR).**
   Status: ✅ delivered.

### Tier 2 — Safe sweeps (one-line-per-file, can batch — but each file needs a smoke run)

2. **P30 sweep — port `.witness.json` writers to `WitnessBuilder`.**
   104 files.  Each port is mechanical:
   - Replace `json.dump({...}, open("foo.witness.json","w"))`
     with the `WitnessBuilder("foo", engine=...)` builder pattern.
   - Witnesses gain `scriptHash` + `scriptCommitSha` so
     `run_pipeline.py` can detect staleness.
   - Reference: [`witness_base.py:136-330`](../../folio-assistant/computations/witness_base.py).
   - **Question that blocks autonomous sweep:** which witnesses are
     hand-curated reference values that should be flagged
     `set_audit_only(...)` vs which are computational outputs that
     re-derive on every run?  Defer per-file decision to author.
   - Recommended: bulk-process in batches of ≤ 10 files per PR, with
     each batch including a `bun run scripts/audit-wiring.ts` pass.

3. **P15 sweep — replace `sp.cancel` with `sp.together` + targeted
   `sp.div` where the full GCD is unnecessary.** 64 hits.
   - Reference fix: `term6_residues_at_roots.py` (commit 18fce929).
   - Tritium-scale wins: 120 s walltime → < 1 s.
   - **Question that blocks autonomous sweep:** some `sp.cancel`
     calls *do* depend on full GCD reduction (e.g. when the next
     step is a polynomial divisibility test).  Each finding needs
     a 2-line read to confirm the GCD is unused downstream.

### Tier 3 — High value, single-file scoped fixes (low-medium risk)

4. **`hoefsmit_symbolic.py`** — already delegates to canonical
   `hecke_character_symbolic` engine (per 7f0359b3).  Verify the
   `sp.cancel` and `BlockCache` flags from the scanner are residual
   shims, not active bottlenecks.

5. **`markov_weights_symbolic.py`** — top finding-count file.
   Audit:
   - 4× P15 (`sp.cancel`) — likely the y_λ closed-form pipeline;
     check whether `sp.together` would suffice.
   - 5× P16 (`sp.simplify`) — gate behind `simplify=False` opt-in
     per the 2834792d pattern.
   - 1× P21 — likely calls `build_seminormal_matrices` for cross-
     validation; wire through `BlockCache` if numerical-q.
   - 1× P30 — port to `WitnessBuilder`.

6. **`schur_weyl_symbolic.py`** — 12 P16 hits, no P15.  Consistent
   pattern: `sp.simplify` after a Schur-symbol expansion.  Apply the
   `simplify=False` parameter pattern across the file.

7. **`gb_filtration_jet_tracker.py`** — 9 hits (P16, P30).  Already
   used by `piece1_three_routes_gb_filtration_probe.py` (3f5271db);
   the `simplify` calls are likely cosmetic for jet-tracker debug
   output.  Gate behind a `verbose=False` default.

### Tier 4 — Targeted P21 wiring (per-file judgment required)

8. **Numerical-q Hoefsmit callers — wire through `BlockCache`.**
   21 candidate files.  The `BlockCache` API in
   [`syt_prefix_cache.py`](../../folio-assistant/computations/syt_prefix_cache.py)
   uses `float`/`math.sqrt` arithmetic; **only** numerical-q callers
   can use it directly.  Symbolic-q callers must continue using
   `hoefsmit_matrices_symbolic`.  Per-file triage:

   | File | Likely q kind | Action |
   |---|---|---|
   | `alpha_k_jones_markov_h3.py` | numerical | wire BlockCache |
   | `alpha_shift_torus.py` | numerical | wire BlockCache |
   | `beta_ew_delta_I_full_spectrum.py` | numerical | wire BlockCache |
   | `beta_ew_delta_I_numerical_spectrum.py` | numerical (per name) | wire BlockCache |
   | `canonical_tower.py` | mixed | review |
   | `conjugate_symmetry.py` | mixed | review |
   | `hecke_character_symbolic.py` | symbolic | leave as-is, justify |
   | `hecke_characters.py` | both paths | already canonical engine |
   | `hecke_wedderburn.py` | mixed | review |
   | `hoefsmit_symbolic.py` | symbolic | leave as-is, justify |
   | `light_isotope_sweep.py` | numerical | wire BlockCache |
   | `markov_weights_symbolic.py` | symbolic | leave as-is |
   | `mass_at_3A_proper.py` | numerical | already disk-cached (P14 below) |
   | `ocneanu_cancellation_derivation.py` | numerical | wire BlockCache |
   | `paper_six_term_shadow_price_sweep.py` | numerical | wire BlockCache |
   | `probe_atom_shell_self_duality_mpfr.py` | mpfr | needs mpmath BlockCache variant |
   | `probe_d_height_stratification.py` | mixed | review |
   | `probe_gamma_gamma_lr_embed_h6.py` | numerical | wire BlockCache |
   | `probe_sdp_canonical_paper_formula.py` | numerical | wire BlockCache |
   | `staircase_ew_disjoint_spectrum.py` | numerical | wire BlockCache |
   | `tr_m_wenzl_bridge_mpfr.py` | mpfr | needs mpmath BlockCache variant |

   Expected speedup: 5–20× per call on n ≥ 8 (per `ocneanu_weights`
   wiring).  **Required cross-check:** numerical-equivalence at q₀
   `Δ < 1e-12` for each migrated caller.

### Tier 5 — Single discrete decision (one question, then mechanical)

9. **P14 — `mass_at_3A_proper.py:146-167` pickle disk cache.**
   - Cache content: output of `build_seminormal_matrices(shape)` —
     a tuple of numpy arrays + SYT dicts.
   - Local-only (`.cache/seminormal/`); RCE risk requires local
     write access.
   - **Decision needed:** migrate to (a) `numpy.savez` (handles
     arrays natively, safe), or (b) JSON of `str(sympy.Expr)` per
     0eda79c6 convention.  `numpy.savez` is the better fit here;
     0eda79c6's JSON convention is for sympy Expr caches.
   - Once decided: 5-line edit.

### Tier 6 — Out of mechanical scope (require semantic review)

10. **P1–P13 sweeps** — trace-cyclicity, normalisation confusion,
    chain-rule pole-order bugs, etc.  Already audited in
    `borromean-axial-coupling` (P1) and reviewed per file as
    findings emerge; no static-scan applicable.

11. **P17 (LaurentQ wiring) extension to A ≥ 5.**  The 17aee993
    benchmark shows speedup fades past A=4 because GS reduction
    dominates.  R4 quotient-ideal port into LaurentQ would
    recover the gap but is research-grade.  Defer.

12. **P25 (det-pair law) opportunistic deployment.**  Already
    landed in `det_pair_law.py`; audit downstream Markov-trace
    aggregations to identify where `(λ, λ′)` halving is unused.

## Implementation begun in this PR

- [x] `local/compute-audit` skill written.
- [x] Routing wired into `CLAUDE.md` (skill table + collaborator
      role row) and `.github/copilot-instructions.md` §12.
- [x] `compute_audit_scan.py` static scanner.
- [x] `compute-audit-scan.witness.json` (audit-only, points at this
      workplan).
- [x] This workplan document with per-file ranked recommendations.

Tier 2 onward is **paused for user judgment** because every item
either (a) requires per-file semantic review of `sp.cancel` /
`sp.simplify` necessity, (b) requires the P21 numerical-vs-symbolic
triage from the table in §8, or (c) hangs on the single P14
serializer choice in §9.  Per the
"begin implementation where no questions" directive, these are not
in scope for autonomous landing.

## Re-running the audit

```bash
python folio-assistant/computations/compute_audit_scan.py
```

Findings change only when scripts change.  After each Tier-2/3/4
landing, re-run and confirm the matching pattern's hit count drops.

## Conventions reinforced

- Every speedup PR must include a per-atom benchmark table in the
  commit message AND the `.witness.json` (P28).
- Every speedup PR must cross-check numerical equivalence at q₀
  with `Δ < 1e-15` (or `< 1e-12` for numerical-only paths).
- Honest reports: small-atom regressions (e.g. proton 0.6×) must
  be stated and gated behind `use_fast=True` opt-in default
  (e69d0acf).
- Never remove the slow path; keep it as `use_fast=False` opt-out
  for symbolic-output callers.
