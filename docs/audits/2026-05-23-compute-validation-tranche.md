# Compute-validation tranche audit (2026-05-23)

**Scope:** items 1-5 from the post-Tier-1.A queue, per user
directive *"do so! good initiative"* + *"make sure there is audit"*.

## Item 1: ⁷Li wall validation

**Status: IN PROGRESS** (launched background bench).

At 13 minutes: 11.6 GB RAM on a 15 GB machine, 100% CPU.
Memory growth rate ~1 GB/min suggests OOM risk within 2-3 min.

If ⁷Li OOMs at 15 GB: validates that **Tier 1.A alone is
insufficient for ⁷Li on desktop** — confirms Tier 1.B (orbit
reduction) or algorithm change (crystal basis) is needed before
the heavy-atom unlock claim holds.

**Expected outcome** (from the Tier 1.A roadmap):
- ⁷Li projected wall with Rust reduce: ~17-20 min
- ⁸Be projected: infeasible without orbit reduction
- ¹²C: infeasible without orbit reduction

*Result will be appended when the bench completes.*

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
| 1 | ⁷Li wall validation | in progress (bench running) | audit + result doc |
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
