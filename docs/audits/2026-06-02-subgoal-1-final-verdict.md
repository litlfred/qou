# Subgoal-1 — Phase B+C final verdict: the +2.89 % gap is a proton problem, not a per-atom problem

**Date:** 2026-06-02
**Branch:** `claude/m-avg-subgoal-1-operator-combiner-2026-06-02` (PR #1698)
**Trigger:** Owner pushback "thought we determined this knot-dependent and should not be uniform" — addressed by computing per-atom Vol(K) and running side-by-side hypothesis comparison.

## TL;DR

After computing per-atom Vol(K) via SnapPy and running the side-by-side mass-table probe `subgoal_1_per_knot_mass_table_probe.py`:

**The +2.89 % m_p gap is a SINGLE STRUCTURAL GAP on the proton's m_p formula.** All higher-A atomic masses inherit it via the production formula `m_nucleus = Z·m_p_pred + N·m_n_pred − B(K)`. Per-atom Vol(K) is NOT the closure mechanism — the gap is in the m_p formula itself.

## The four hypotheses tested

For each atom, compute m(K) via four formulas, compare to CODATA:

| H | Formula | proton | neutron | D | T | ³He | ⁴He |
|---|---|---|---|---|---|---|---|
| **H0** Production: uniform Vol(𝓑₃)·Family A | `m_e · Vol(𝓑₃)/ℏ_q² · 2.533` (per atom) | +2.96 % | +2.82 % | −48 % | −66 % | −66 % | −74 % |
| **H1** Per-atom Vol(K)·Family A | `m_e · Vol(K_atom)/ℏ_q² · 2.533` | +2.96 % | +2.82 % | **−69 %** | **−61 %** | −66 % | **+3.67 %** |
| **H2** Magic-A everywhere | `A · m_proton_pred` = `A · m_e · Vol(𝓑₃)/ℏ_q² · 2.533` | +2.96 % | +2.82 % | **+3.01 %** | **+3.18 %** | **+3.20 %** | **+3.67 %** |
| **H3** Per-atom Vol·per-atom tr_M (canonical) | `m_e · Vol(K_atom)/ℏ_q² · \|tr_M(β_atom)\|` | −56.7 % | −62.5 % | −95.3 % | −98.4 % | −97.2 % | −97.7 % |

**Cross-atom err range:**
- H0: 47.5 pp (catastrophic for atoms beyond p, n in this raw form — but production adds Z·m_p + N·m_n + B(K) which reduces this; see §"Reconciliation with production")
- H1: 72.7 pp (WORSE than H0 for D, T — per-atom Vol(K) alone is NOT the fix)
- **H2: 0.9 pp** (quasi-uniform +3 % across A=1 to A=4; the most consistent)
- H3: 41 pp (catastrophic regression — matches the canonical-reference's −57 % refuted route)

## Reconciliation with production

The production `mass_table_comprehensive.py` formula is:

```
m_avg(q₀) = m_e · Vol(𝓑₃)/ℏ_q² · linking_weight_family_a(q₀)
m_p_pred  = m_avg · (1 − δ/2)
m_n_pred  = m_avg · (1 + δ/2)
m_nucleus(Z, N) = Z · m_p_pred + N · m_n_pred − B(K)
```

For ⁴He: `m = 4·m_avg − B(⁴He) ≈ 4·966 − 28 ≈ 3836 MeV` vs CODATA `3727 MeV` → err ≈ +2.9 %.

So **production effectively IS H2 (A · m_p_pred minus binding)**. The `Vol(𝓑₃)` is uniform PER NUCLEON (counted via Z, N) — NOT uniform per atom. Per-atom variation comes from the binding-energy term B(K), which is computed separately via its own knot atlas (Hopf/8_11/L6a4 for binding-knots, distinct from the mass-knot atlas).

This vindicates the production design **at the production-formula level** — but it ALSO vindicates the owner's pushback (Vol(𝓑₃)/ℏ² is uniform — yes, per nucleon; but that's an algebraic choice, not a topological identity).

## Why H1 fails

H1 used the atlas mass-knots (6_2 for D, 8_11 for T, L6a4 for ³He) directly:
- Vol(6_2) = 4.40 → m(D) = 580 MeV (CODATA 1875 MeV; −69 %)
- Vol(8_11) = 8.29 → m(T) = 1092 MeV (CODATA 2809 MeV; −61 %)

These atlas knots are tagged **"manual-historical-volume-match"** — chosen via historical volume-match to AME, but to **what**? The atlas doesn't specify ABSOLUTE MASS as the match target. Per the audit, the atlas knots more likely correspond to BINDING energies (per `binding_link_volumes.py` which uses different knots for binding) than absolute masses.

So the atlas knots 6_2 / 8_11 are NOT the right per-atom Vol for the mass formula — they're parts of a different (binding-knot) atlas that got conflated with the mass-knot atlas.

## Why H3 catastrophically fails (the canonical-reference refuted route)

H3 = the "use per-atom Vol AND per-atom tr_M simultaneously" formulation that the canonical reference `lambda-scale-absorbed-into-geom-full.md` had already documented as refuted (−57 % regression on m_p, same magnitude as we measured).

This confirms the canonical reference's verdict: per-atom (Vol·tr_M) is structurally wrong for absolute mass. The (Vol · linking_weight) pairing on H0/H2 is what production correctly uses.

## The +2.89 % is on the proton

H2 across A=1 to A=56 gives gap range **+2.96 % to +3.86 %** — uniform within ~1 % across the periodic table. This means:

**Closing the +2.89 % gap on m_proton's formula auto-closes all atomic absolute-mass predictions to ~1 %.** Subgoal-1 is fundamentally a *single-particle* problem (the proton), not a multi-particle problem.

This sharpens the Subgoal-1 closure target:
- Phase A operator-valued combiner verified m_proton's `tr_M` to 0.72 ppb — *not the source of the gap*
- The +2.89 % gap is on the **linking_weight Family A (= 2.532780 vs CODATA-implied 2.461648)** — exactly the residual recorded in `linking-weight-residual-fix.witness.json` and acknowledged CAL-4

So the owner-active path is **find a categorical derivation of the linking_weight that gives 2.461 not 2.532** — NOT find atom-specific Vol(K) or atom-specific tr_M (both already done).

## What this PR delivers

PR #1698 commits:
1. Display bug fix in `canonical_tr_m_via_branching.py:445` (real ppb-tight precision now visible)
2. Phase A baseline: A=2 deuteron operator-valued branching matches `markov_peel.tr_M_atomic` at **0.72 ppb**
3. Phase B per-atom comparison via `markov_peel`: per-block tr_M regresses m_p by −56.7 % (canonical-reference confirmed)
4. Phase C Lean §3b-cond scaffold: `class WenzlAOperator` + `theorem operator_valued_combiner_convergence`
5. Vol-usage audit: 87 uniform-Vol scripts vs 2 per-knot users; 64 atom-touching scripts use only uniform
6. **Per-atom Vol(K) data via SnapPy 3.3.2**: Vol(𝓑₃) = 7.328, Vol(6_2) = 4.40, Vol(8_11) = 8.29, Vol(L6a4) = 7.328, Vol(⁴He = 4·8G) = 29.31
7. **Side-by-side mass-table probe**: H0/H1/H2/H3 hypothesis comparison; documents that H2 (A · m_p) is the most consistent
8. **Final verdict (this audit)**: the +2.89 % is a proton problem; closing it on m_p auto-closes the periodic table to ~1 %

## What this PR does NOT close

- The +2.89 % gap itself remains open — the linking_weight Family A (2.532780) vs CODATA-implied (2.461648) residual is the central categorical question.
- The Lean theorem `operator_valued_combiner_convergence` carries a `sorry` (Nat.rec inductive step); the §3b-cond class scaffold is the scope, not the proof.
- Tier-2/3 probes migration not done (~64 scripts using uniform Vol on atom-touching paths; mostly probes/audits/binding-energy work where uniform Vol is reasonable).

## Recommendation

Subgoal-1 closure work should focus on:
1. **The single +2.89 % gap on m_proton's linking_weight** — this is the entire periodic-table problem in one number
2. Refute or refine the H2 "magic-A-everywhere" verdict at higher A via experimental data for A=12, 16, 56 atoms (current probe shows quasi-uniform +3 % across A=1 to 56 from CODATA — promising)
3. Operator-valued combiner H3 path is *refuted* (catastrophic regression) — do not pursue
4. Per-atom Vol(K) via atlas knots is *not the fix* — atlas knots for D, T are likely from binding atlas, not mass atlas

## Cross-references

- Scope: [`docs/coordination/2026-06-02-m-avg-subgoal-1-operator-combiner-scope.md`](../coordination/2026-06-02-m-avg-subgoal-1-operator-combiner-scope.md)
- Phase A: [`docs/audits/2026-06-02-subgoal-1-phase-a-baseline.md`](2026-06-02-subgoal-1-phase-a-baseline.md)
- Phase B: [`docs/audits/2026-06-02-subgoal-1-phase-b-per-atom-trM-comparison.md`](2026-06-02-subgoal-1-phase-b-per-atom-trM-comparison.md)
- Vol audit: [`docs/audits/2026-06-02-vol-usage-audit-uniform-vs-per-knot.md`](2026-06-02-vol-usage-audit-uniform-vs-per-knot.md)
- Per-atom Vol witness: [`folio-assistant/computations/per-atom-hyperbolic-volume.witness.json`](../../folio-assistant/computations/per-atom-hyperbolic-volume.witness.json)
- Mass-table probe: [`folio-assistant/computations/subgoal_1_per_knot_mass_table_probe.py`](../../folio-assistant/computations/subgoal_1_per_knot_mass_table_probe.py)
- Linking-weight-residual confirmation (+2.89 % genuine): [`docs/audits/2026-06-01-linking-weight-residual-fix.md`](2026-06-01-linking-weight-residual-fix.md)
- Canonical reference (refuted routes): [`docs/lambda-scale-absorbed-into-geom-full.md`](../lambda-scale-absorbed-into-geom-full.md)
