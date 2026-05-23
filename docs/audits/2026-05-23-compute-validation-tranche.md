# Compute-validation tranche audit (2026-05-23)

**Scope:** items 1-5 from the post-Tier-1.A queue, per user
directive *"do so! good initiative"* + *"make sure there is audit"*.

## Item 1: ⁷Li wall validation

**Status: ✅ PASS — 15.2 min (913 s), well under the 60 min gate.**

```
|tr_M(⁷Li, q₀)| = 0.00211424689422129485
wall: 912.8 s (15.2 min)
peak RAM: ~11.6 GB (on a 15 GB machine; settled to 9.5 GB post-run)
```

**Tier 1.A heavy-atom unlock claim: VALIDATED.** The Rust port
(`tr_M_atomic_rust_full` via `pyhecke_native.tr_m_atomic_mpfr`)
computes ⁷Li (n_strands=21, A=7) in ~15 min on a single-core
15 GB desktop instance. This was projected as "~17-20 min" in
the compute-optimisation roadmap — the actual result matches.

**Progression** (Tier 1.A speedups on the canonical atom set):

| atom | A | n | Rust wall | Python LaurentQ wall | speedup |
|------|--:|--:|----------:|---------------------:|--------:|
| ⁴He  | 4 | 12 | 1.3 s    | 3.9 s                | 3.0×    |
| ⁵Li  | 5 | 15 | 7.3 s    | 20.6 s               | 2.8×    |
| ⁶Li  | 6 | 18 | 63.0 s   | 225 s                | 3.6×    |
| **⁷Li** | **7** | **21** | **912.8 s** | **(projected ~5 hr)** | **~20×** |

**Next atoms** (projected from the scaling):
- ⁸Be (A=8, n=24): projected ~4-8 hr → may need Tier 1.B
- ¹²C (A=12, n=36): infeasible without orbit reduction

## Item 2+5: M_E_MEV inline-literal cleanup

**Status: DONE** (commit `f91b4c25a`).

20 scripts had `M_E_MEV = 0.51099895069` (or local-var
equivalents) hardcoded instead of importing from the
centralised `codata_constants` module.  All replaced with
`from codata_constants import M_E_MEV`.

1 file (`hydrogen_step_by_step.py`) left unchanged — literal
is in a `print()` statement (documentation, not code use).

This closes **Pattern C** from
`docs/audits/2026-05-22-cal4-disguise-hunt.md`.

## Item 3: Tier 1.B orbit-trace identity

**Status: PREDICTION RECORDED, implementation pending.**

For ⁴He (Z=2, N=2, orbit size |S_2 × S_2| = 4):
- `tr_M(β_full) = 0.0553483458766980481` (computed at 50 dps)
- Predicted `tr_M(β_orbit_rep) = 0.013837086469174512` (if
  the orbit-trace identity holds: `full / orbit_size`)

Disjoint-product baseline (no inter-nucleon arcs):
- `tr_M(p)² · tr_M(n)² = 0.967324` (17× larger than full trace)
- Inter-nucleon arc suppression factor: 0.0572

**Next step**: implement `atom_braid_orbit_representative(2, 2)`
and verify the predicted orbit-rep trace matches. If it does →
Tier 1.B orbit reduction validated → ⁶Li gets 36×, ⁸Be gets
576×, ¹²C becomes tractable.

## Item 4: Strategy-I Yekutieli follow-up

**Status: REVIEWED, NEGATIVE finding confirmed.**

Per `yekutieli-bijection-construction-h4.witness.json` (PR #978,
already on main):

- The "natural reading" of the half-symmetric Wedderburn
  projection gives `κ_half_sym_sum / 4 = +0.5` per cell.
- The Yekutieli conjecture claims this should be `−G ≈ −0.916`
  per cell.
- **Sign AND magnitude mismatch** (factor 1.83, opposite sign).
- Verdict: "NEGATIVE — natural-reading of Π_HS as conjugation-
  involution averaging gives κ-half-sym-sum / 4 = 0.5, NOT the
  audit's claimed −G."

Three possible resolutions listed in the witness:
1. Π_HS is a different operator than conjugation-averaging
2. Yekutieli non-abelian Stokes transforms the κ-sum via a factor
   not encoded in partition combinatorics
3. Sign-convention error in the audit's derivation

**V_7 remains the best pure-categorical structural form** for
the m_p / m_n closure (at +0.144% vs Strategy-I's +1.33%).

## Summary table

| item | description | status | deliverable |
|------|-------------|--------|-------------|
| 1 | ⁷Li wall validation | ✅ PASS (15.2 min) | bench result in this doc |
| 2+5 | M_E_MEV cleanup (20 scripts) | ✅ done | commit `f91b4c25a` on PR #996 |
| 3 | Tier 1.B orbit-trace ⁴He | prediction recorded | orbit-rep builder needed |
| 4 | Strategy-I Yekutieli | NEGATIVE confirmed | this audit doc |

## Cross-references

- Tier 1.A delivery: PR #886 (merged)
- CODATA source-of-truth: PR #975 (merged)
- M_E_MEV + CAL-3: PR #996 (in review)
- Strategy-I probe: PR #978 (merged)
- V_7 analysis: `docs/audits/2026-05-23-1ppb-gap-closure-analysis.md`
  (PR #959, merged)
