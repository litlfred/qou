# Deriving the corrected keystone arena: it's the FULL Hecke trace, not a finite colour-SU(3)

**Date:** 2026-06-16
**Branch:** `claude/keystone-full-hecke-not-su3-arena-2026-06-16`
**Status:** reconciliation — deriving the corrected arena collides (productively) with a just-merged sibling
result; the finite colour-SU(3) Sasakian arena is ruled out. Verified, no fit.
**Discipline:** corpus-grep + critical-distance + coordinate §6 (reconcile, don't paper over).

## What "derive the corrected arena" produced

After #2398 ruled out the `SU(3)/SO(3)` quotient (the spacetime-fixed Schur-centralizer obstruction), the next
step was to derive the colour `U(1)⊂SU(3)` Reeb on the *independent* colour factor. Reading the just-merged
sibling audit
[`2026-06-16-s5-s3-symmetry-review-and-suq3-trace-question.md`](2026-06-16-s5-s3-symmetry-review-and-suq3-trace-question.md)
(PR #2389) before deriving — per corpus-grep — shows the colour-SU(3) target itself is the wrong functional.

## The collision (and reconciliation)

Two facts, both resting on the **same Schur row-bound** `s_λ(x_1..x_k)=0 ⟺ rows(λ)>k` (verified n=5,6 in
`scripts/keystone_full_hecke_not_su3_arena.py`):

| | bound | rules out | status |
|---|---|---|---|
| this session #2364 | electron `(3,1,1)` has 3 rows → needs `k≥3` | spinor `ℂ²` (`k=2`) | **lower** bound |
| sibling #2389 | full `tr_M` needs `>3`-row blocks (SU_q(3) misses **3.4%** @⁴He, growing with A) | any finite `ℂ^N` | **upper** bound |

Together: **no finite `ℂ^N` tensor space carries the production trace.** The production trace is the **full Hecke
/ Wenzl principal specialization** `s_λ(1,q,q²,…)` (nonzero for every λ, no row cutoff) — the canonical Markov
trace. The SU_q(3) finite-3-variable specialization `s_λ(1,q,q²)` is a *structurally different* functional (zero
for `>3`-row λ), not an approximation.

**Consequence for the keystone:** my "**colour ℂ³ strand fibre / SU(3) Sasakian arena**" (#2364, #2370,
scope-doc) realized the SU_q(3) `≤3`-row truncation — the **wrong trace functional**. There is therefore **no
finite colour-SU(3) Reeb arena to derive**: the geometric realization, if one exists, must carry the **full Hecke
principal-specialization trace**, which the bond-dimension verdict shows is intrinsically `O(p(3A))`-dimensional
(no finite colour fibre).

## What still stands

- **#2364's lower bound** (spinor `ℂ²` cannot host the electron) is correct and unaffected — it's the `k=2` case
  of the same row-bound.
- **#2398's spacetime⊥colour** (the Schur-centralizer obstruction) is **confirmed** by the corpus: the sibling
  audit cites `color-spacetime-s5-factorization.md` — `S5 = S2 × S3 = spacetime × colour`. My Reeb-centralizer
  argument independently re-derived this factorization.
- The **`Δ_λ = magnitude × chirality`** decomposition and the **PROBE-4 positivity prune** are statements about
  the abstract `H_n(q)` Wedderburn blocks and are unaffected (they never assumed a finite colour fibre).

## Net (honest terminus of the geometric-derivation push)

Deriving the corrected arena **rules out** the finite colour-SU(3) Sasakian (it's the invalid SU_q(3) truncation)
and shifts the target to the **full Hecke principal-specialization trace** — an infinite-variable / large-`N`
object, intrinsically `p(3A)`-dimensional. So the keystone's geometric leg is **not** a finite-dimensional
Sasakian construction; a finite-`N` colour arena is ruled out. The remaining question (is there *any* geometric
realization of the full Hecke principal trace, and does its index reproduce the Markov weights) is genuine
infinite-dimensional differential geometry — well beyond in-session derivation, and now correctly *aimed*.

## Cross-references

- `docs/audits/2026-06-16-s5-s3-symmetry-review-and-suq3-trace-question.md` (#2389) — full-Hecke vs SU_q(3) resolution; `S5=S2×S3`
- `docs/audits/2026-06-16-s5so3-ingredient4-fibre-schur-weyl-constraint.md` (#2364) — the `ℂ²` lower bound (same row-bound)
- `docs/audits/2026-06-16-keystone-wu-manifold-reeb-obstruction.md` (#2398) — spacetime⊥colour (Schur centralizer)
- `content/.../mass-endomorphism/color-spacetime-s5-factorization.md` — corpus `S5=S2×S3`
- `scripts/keystone_full_hecke_not_su3_arena.py` — the row-bound + reconciliation (exit 0)
