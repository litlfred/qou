---
name: compute-audit
roles: [collaborator, owner]
description: >
  Audit Python compute scripts under folio-assistant/computations/ for
  the 30 patterns (P1-P30) extracted from a 50-commit review of QOU
  performance and mathematical-improvement landings. Distinguishes
  CORRECTNESS antipatterns (P1-P16) from PERFORMANCE antipatterns
  (P17-P30). Produces a ranked workplan citing concrete files+lines.
allowed-tools: Read Bash Grep Glob Edit Write Agent
---

# Compute Audit Skill

## Role

When a user asks "audit compute", "what can be sped up", "improvements
to compute", "compute audit", "performance audit", "find slow scripts",
or "where are we burning sympy" — run the scanner, read the witness,
and produce a ranked workplan. **Never** rewrite scripts blindly: every
change must cite a specific commit pattern (P1–P30) and verify
numerical equivalence at q₀ before/after.

## When to Use This Skill

- "audit compute" / "compute audit"
- "what can be sped up?" / "improvements to compute"
- "find slow scripts" / "what's the bottleneck"
- "where is sympy.simplify being called on huge expressions?"
- "are we missing LaurentQ wiring?"
- "is BlockCache wired everywhere it should be?"
- After a new compute script lands (review pass)
- Before a release (perf regression sweep)

## Workflow

1. Run `python folio-assistant/computations/compute_audit_scan.py`
   (writes `compute-audit-scan.witness.json` next to the script).
2. Read the JSON: it lists per-file findings tagged by pattern ID.
3. Cross-reference findings against `docs/audits/2026-05-08-compute-audit-workplan.md`
   for ranked next-actions.
4. For each candidate fix, **verify the antipattern is real** by
   reading the cited lines — the static scanner has false positives
   on idiomatic uses (e.g. `sp.simplify` on a single small symbol is fine).
5. Implement only items where you can:
   - Cite the matching pattern (P-id) from the catalogue below.
   - Cite a prior successful instance from `docs/audits/`.
   - Provide a numerical-equivalence cross-check at q₀.
6. Update `proof-objects.json` only if a content block's witness
   changes — pure perf changes do not change formalization status.

## The 30 Patterns (extracted from 50-commit review, 2026-04 → 2026-05)

### Group A — Correctness antipatterns (must fix before optimising)

- **P1. Trace-cyclic conjugation.** `tr(β·X·β⁻¹)` is forced equal to
  `tr(X)` by Markov axiom (M1); any "observable" computed this way
  is structurally trivial. Always a red flag. Fix: use the G⁻¹ + LP
  active-set master formula (see `bound_state_observable_validator.py`
  and `confinement-frobenius-reciprocity.md`).

- **P2. Markov vs Plancherel vs partition-sum normalisation
  confusion.** `w_λ/f^λ`, `dim_q(λ)²/[n]_q!`, and the canonical
  Ocneanu–Wenzl `y_λ(q)` agree only at q=1. Always state which
  normalisation is in use. (e857733d, 089ac8b8.)

- **P3. Mirror-knot β\* convention drift.** Four different choices
  of "β\*" (reverse+invert / mirror knot / reverse-only / averaged)
  give different Gram values; pick one and document it
  (term5_aK_audit.py, d9b77cd1).

- **P4. Cycle type ≠ braid identity.** Two atoms with the same S_n
  cycle type can have distinct Hoefsmit characters (³H vs ³He;
  b61a4845). Never collapse atoms by permutation cycle type.

- **P5. Schur–Weyl trace ≠ Markov trace.** Document which trace
  every script is computing (term6_full_pole_sum: 9d77c2c0 caveat).

- **P6. `len(standard_young_tableaux(...))` returns the 3-tuple
  length (=3), not f^λ.** Unpack syts via 3-tuple destructuring.
  (7f0359b3.)

- **P7. Truncation-bound off-by-one.** `max_gen < n-1` should be
  `max_gen < n-2` for 0-based reduced-word indices in H_n.
  (markov_trace_recursive, ce5bbefb.)

- **P8. Chain-rule shortcut for higher-order poles.** `Res_q[tr_M] =
  2u₀·Res_u[U]` is correct **only** for simple poles in u; integrate
  `2u·U(u)` along the contour for any pole order. (1cb6850e.)

- **P9. `sqrt(q)` branch-cut crossing.** Numerical Cauchy contour
  through ζ_2 = −1 crosses the branch cut. Substitute q = u² up
  front. (2e410269.)

- **P10. Cache key not incorporating coefficient.** Caching by
  `(word,)` alone is wrong if the element carries a symbolic
  coefficient. Key on `frozenset((word, str(coeff)))`. (5b2e8180.)

- **P11. Recursive function bypassing its `lru_cache` decorator.**
  Internal recursion must call the decorated entry point, not the
  bare worker. (29ca235c, hecke_character_q_deformed.)

- **P12. Sign-balance "filter activates when q_n > p_n" criterion.**
  Falsified empirically; signature oscillates around 50%. Use the
  cancellation-precision-budget criterion instead. (6e82a20c.)

- **P13. "GB-NF event count = 2·|S_n|" universality claim.**
  Falsified by 24-word sweep; counts are word-specific. (7b5b51a8.)

- **P14. Pickle for cache files.** RCE risk on tampered cache.
  Use JSON of `str(sympy.Expr)` and re-`sympify` on load.
  (0eda79c6.)

- **P15. `sp.cancel` across whole rational expression with huge
  numerator/denominator.** Walls past 120s on tritium-scale
  inputs because of full GCD reduction. Use `sp.together` (no GCD)
  followed by `sp.div` for the next step. (18fce929.)

- **P16. `sp.simplify` on the aggregated trace before numerical
  evalf.** For evalf at q₀, simplification is purely cosmetic and
  can exceed 30 minutes on a 5000-op expression. Add
  `simplify=False` parameter, default True for back-compat.
  (2834792d.)

### Group B — Performance patterns (apply when correctness clean)

- **P17. Wrong number kernel.** Hecke generators have Laurent-poly
  coefficients in q over ℚ by construction. `sympy.Expr` is overkill;
  use `LaurentQ` (folio-assistant/computations/laurent_q.py).
  Sweet spot: A=3 (3–6× speedup); A≥5 fades. (79ca1200, 17aee993.)

- **P18. Symbolic partial-fraction polar split** instead of per-pole
  `sp.residue` numerical Cauchy contour. Replace
  `tr_u(u) = N(u)/D(u)` with `entire(u) + A(u)/u^k + B(u)/Dprime(u)`
  via one `sp.div` + one factoring + one power-series invert.
  (18fce929: deuteron 30 min → 1.2 s.)

- **P19. Substitution to remove branch points** (q → u²) before any
  rational-function manipulation. Empirically the post-substitution
  denominator factors as `c·u^a·(u²+1)^b`, so all ζ_ℓ with ℓ≥3
  short-circuit to residue 0. (b342ab3c.)

- **P20. Recursive Markov-axiom ascent** beats per-Wedderburn-block
  matrix multiplication for A≥4. dim-462 sympy matmul times out at
  >45 min/atom; recursive ascent finishes ⁴He in 60 s.
  (markov_peel.tr_M_atomic, 8bae1306, 2834792d.)

- **P21. Shared `BlockCache` across irreps for Hoefsmit construction.**
  Block values keyed by content distance ρ; precompute SYT→index
  dict per shape to eliminate the O(d_λ²) swap-partner search.
  (syt_prefix_cache.BlockCache; ocneanu_weights wires it.)
  **Audit gap**: 21 numerical Hoefsmit callers in
  `folio-assistant/computations/` do not yet use BlockCache.

- **P22. Sparse representation when nnz < 0.1·dim²** for Hoefsmit
  matrices. `build_seminormal_matrices_cached` already auto-switches
  at dim>500; instrument lower-dim callers to confirm threshold.

- **P23. Process-pool parallelism on per-irrep work.** Per-partition
  Hoefsmit matrix product is independent across λ; embarrassingly
  parallel. Use `ProcessPoolExecutor` with str-serialised exprs to
  dodge sympy-Symbol pickling fragility. (287fbacd.)

- **P24. Disk caches for restart-safety on multi-hour runs.** Two
  layers: `.hoefsmit_cache/n<n>_lam<λ>.json` (atom-independent),
  `.term_cache/Z<Z>_N<N>_inter<i>_lam<λ>.txt` (per-atom checkpoints).
  Both `.gitignored`. (66682798, 7eacc86e.)

- **P25. Conjugate-pair / det-law symmetry.** For any braid word w
  and conjugate (λ, λ′), `det ρ_λ(w)·det ρ_{λ′}(w) = ±1` exactly
  (sign = (−1)^{L·dim_λ}); halves Wedderburn-weighted Markov-trace
  work. (det_pair_law.py, conjugate-pair-det-law memory.)

- **P26. Bar-involution kernel** as a first-class compute primitive
  (`bar_involution.py`; cbcc716e). Use it whenever a script needs
  the q ↔ q⁻¹ symmetry.

- **P27. Pre-parse / hoist setup out of inner loops.** Parse Habiro
  coefficients once outside the (p,q) loop; build cross_d_table
  once per worker, not per crossing. (6e777542, 0eda79c6.)

- **P28. Always emit a per-atom benchmark table in the commit
  message and `.witness.json`** when landing a speedup. Caller-vs-
  caller, with cross-check `Δ < 1e-15` at q₀. Every fast-path PR
  in the 50-commit review did this; it is the convention.

- **P29. Profile to identify the actual bottleneck before
  optimising.** ³He profile showed `sp.simplify` (not the loop) was
  the cost (2834792d); Wenzl-bridge profile showed matrix matmul
  (not formula evaluation) was the cost (6e82a20c).

- **P30. WitnessBuilder scriptHash + scriptFile metadata.** Every
  Python `.witness.json` should carry these so `run_pipeline.py`
  can detect staleness. Hand-written witnesses are treated as
  current and silently skip regeneration (workflow memory:
  run_pipeline.py:152-177).

- **P31. Hardcoded CODATA literal outside the registry.** CODATA
  mass / Q-value literals must come from `codata_constants.py`
  (validation aliases) or `experimental_constants.py`, NEVER as
  free-floating string literals in production scripts.  Free-floating
  CODATA literals (`"0.51099895"`, `"938.272"`, `"939.565"`,
  `"0.78233"`, `"206.7682830"`, etc.) silently inflate the
  three-calibration count and bypass the deprecation warning that
  `codata_constants.__getattr__` emits on legacy aliases.  Reference
  fix: `codata_constants.py` (single source of truth + validation
  cross-check).  Scanner: `compute_audit_scan.py` flags any of the
  five canonical CODATA strings outside an allowlist of registry /
  bib / audit files.  Audit-only scripts may use them inside an
  explicit `# noqa: P31` comment justifying the audit purpose.

- **P32. Non-deterministic `*.derivation.json` builder.** A builder
  script must produce **byte-equal** output across two consecutive
  runs in the same environment. Drift (different bytes) typically
  indicates dict-iteration order (set `PYTHONHASHSEED=0`), an
  embedded timestamp, float-precision variation, or hand-edits to
  the committed JSON that the script does not reproduce. Reference
  fix: `witness_reproducibility_check.py` (snapshot → re-run →
  byte-diff). Audit-only: explicit registry of (script, output)
  pairs avoids auto-discovery mistakes for builders with CLI args.
  Failure mode this catches in practice: hand-edits to a committed
  `.derivation.json` that drift on the next CI regeneration (see
  build_markov_trace_assembly_neutron_chain.py 2026-05-12 fix).

## Pattern → fix-success references

| Pattern | Reference fix |
|---|---|
| P15, P16, P18 | term6_residues_at_roots.py (18fce929) |
| P17 | hecke_laurent_fast.py + laurent_q.py (79ca1200) |
| P20 | markov_peel.py recursive ascent (8bae1306) |
| P21 | syt_prefix_cache.py + ocneanu_weights wiring |
| P23 | habiro_coefficients_atomic_fast.py (287fbacd) |
| P24 | habiro_coefficients_atomic_fast.py disk caches |
| P25 | det_pair_law.py |
| P26 | bar_involution.py (cbcc716e) |
| P30 | witness_base.py:136-183 |
| P31 | codata_constants.py + canonical_derivation_pipeline_compliance.py |
| P32 | witness_reproducibility_check.py + build_markov_trace_assembly_neutron_chain.py:260 (drift fix) |

## Verification checklist before landing any speedup

1. **Numerical equivalence at q₀** vs the slow path, `Δ < 1e-15`.
2. **Per-atom benchmark table** in commit message AND witness JSON.
3. **Honesty**: if the new path is slower on small atoms (e.g.
   LaurentQ on the proton: 0.6×), say so and gate by atom size or
   keep both paths via `use_fast=True` opt-in default.
4. **Cross-check** D(u) closed forms (or analogous structural
   invariants) where applicable — speedups must not perturb
   exact algebraic outputs.
5. **Run `bun run validate`** for any content-block touch.

## Anti-patterns this skill explicitly rejects

- "Numerology": pattern-matching numerical agreements without a
  categorical derivation. Demote to remark or null result.
- "Three-route convergence" claims when the routes compute different
  categorical objects (3f5271db, 7b5b51a8).
- "Universal" extrapolation from a single atom (b ≠ 2·|S_n|; 7b5b51a8).
- Removing the slow path. Always keep it as `use_fast=False` opt-out
  for symbolic-output callers (e69d0acf).
