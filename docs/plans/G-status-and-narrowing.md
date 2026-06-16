# Plan G — implementation status and narrowing

**Status:** Plan G's first concrete advance — a narrowing analysis based on the α\* table from `prop:atom-knot-mass-derivation` that identifies which `manual-historical-volume-match` entries can have their SnapPy `Vol_hyp(K)` shortcut retired today vs which are blocked on R5-full.

## Per-entry readiness

| Entry | Knot/link | α\* (PSD) | T_w canonical? | Plan-G blocker |
|---|---|---|---|---|
| ²H (deuteron) | 6_2 | 0.546 | **no** — 5 of 7 blocks fail PSD relative to historical 6_2 | R5-full SDP-as-solver must determine canonical T_w first |
| ³H (tritium) | 8_11 | **0.424** | **no** — largest gap in registry; 8_11 may be wrong | R5-full + structural review of historical ID |
| ³He | L_6a4 (Borromean) | **1.000** | **yes** — all 3 blocks PSD | **none — clear first target** |
| electron | T_{2,3} = σ_1^3 | 0.577 | partial — sign block ρ_{(1,1)} = −q^{-3} (algebraic) | not flagged `manual-historical-volume-match`; Plan G N/A |

Of the four entries Plan G originally targeted, only **³He is unblocked** — its canonical T_w is on the principled pipeline (α\* = 1) and the Borromean braid presentation σ_1 σ_2^{-1} σ_1 σ_2^{-1} σ_1 σ_2^{-1} on B_3 is well-defined.

## Existing infrastructure that already does most of the work

- `computations/markov/markov_trace_canonical.py` — symbolic `tr_M_element(braid_word)` in `H_n(q)`. Works on any word over σ_0..σ_{n−2}, returns a sympy expression in q.
- `computations/atom_nf_symbolic_D.py` — already runs the full categorical pipeline for ²H (D = deuteron): GB-NF reduction → symbolic Markov trace → Jones polynomial. Witness `atom-nf-symbolic-D.witness.json` reports `markov_trace = 0` for D's atom braid (suspicious; the reported Jones polynomial `q − 1 + 2/q − 2/q² + 2/q³ − 2/q⁴ + 1/q⁵` is the standard `J_{6_2}(q)`). The discrepancy is exactly what Plan G needs to investigate — does D's atom braid actually close to 6_2, or is the historical ID wrong (which the α\* = 0.546 already suggests)?
- `computations/q_mn_recursive_memoized.py` + `y_lambda_wenzl_bridge_extended.py` — supply χ_λ(T_w) and y_λ(q) for the Wedderburn-block decomposition.

The existing scripts emit `precision: f64_numeric_fallback`. Migrating them to mpmath @ 50 dps is Plan F (orthogonal).

## Concrete next steps (in dependency order)

1. **(unblocked)** Write `computations/tr_m_canonical_3he_borromean.py` — applies `markov_trace_canonical.tr_M_element` to the Borromean braid σ_1 σ_2^{-1} σ_1 σ_2^{-1} σ_1 σ_2^{-1} on B_3, evaluates at q_0 to 50 dps, compares against `2 m_e × Vol_hyp(L_6a4) ≈ 2 × 0.51100 × 7.32772 = 7.4889 MeV` (current shortcut). Goal: replace the shortcut for ³He.
2. **(unblocked)** Audit `atom_nf_symbolic_D.witness.json`'s `markov_trace = 0` claim. Either confirm it is genuinely zero (which would falsify the 6_2 ID and validate the α\* = 0.546 anomaly), or find the bug.
3. **(blocked on R5-full)** Once R5-full produces canonical T_w for ²H and ³H, re-run `markov_trace_canonical.tr_M_element` on those T_w and emit the symbolic-tr_M witnesses.
4. **(blocked on R5-full)** Update `low_isotope_binding_sweep.py` to read tr_M from the symbolic witnesses instead of the SnapPy `VOL_*` constants, gated by whether each entry has a symbolic-tr_M witness yet.

## Smoke test / exit criterion

For ³He: the symbolic tr_M(T_w_{³He}) at q_0 (mpmath @ 50 dps) should agree with the SnapPy `Vol_hyp(L_6a4)` reading to within the volume-conjecture's known asymptotic precision (~6 digits), and should improve to ≥ 50 dps once the prediction path itself is on MPFR (Plan F). At that point the M_err for ³He should drop from the current +81 ppm toward whatever the structural Term-7 / pp-pairing residual is — the level documented in the `claude/he3-outlier` investigation.

## What this changes in the queued plan

- Plan G's effort estimate ("1–2 days per knot, parallelizable") was optimistic. With R5-full as a hard prerequisite for ²H and ³H, the parallel-day count collapses to a single track for ³He today, and the others wait for R5-full.
- The α\* = 0.424 anomaly on ³H is the highest-value structural lead (remarked in the recommendation summary on PR #446). It should be investigated before any tr_M derivation for ³H — there is no point computing tr_M of the wrong T_w.
