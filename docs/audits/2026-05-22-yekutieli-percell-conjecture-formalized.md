# Yekutieli per-cell curvature for λ_scale — framework's substrate-pure prediction

**Date:** 2026-05-22 (revised evening per user direction "framework B only, remove A")
**Branch:** `claude/lambda-scale-alts-strategy-d-2026-05-22`
**Status:** Framework's honest Yekutieli-extended λ_scale prediction stated;
load-bearing categorical-bijection conjecture formalised; no full proof.

## Context

After PR #895 settled `λ_scale := λ_A(q) = 5/2 + (3/4)·h²` (Family A,
proved theorem) as the framework's substrate value with ~3% residual
to CODATA, and after the q-dilog Tier 0 / Tier 1+ basis-extension
searches all came up negative
([af2d27ee on main](https://github.com/litlfred/qou/commit/af2d27ee52b7ecde5fddd624010a6ee59208573d) /
[PR #928](https://github.com/litlfred/qou/pull/928) /
[PR #916 commit e64b2806](https://github.com/litlfred/qou/commit/e64b2806)), the
remaining substrate-pure-research direction is the
**Yekutieli per-cell curvature** structural argument from
[`docs/audits/2026-05-18-conjecture-proof-step3-yekutieli.md`](2026-05-18-conjecture-proof-step3-yekutieli.md).

That audit ("Step 3") argues a per-cell hyperbolic volume contribution
of `−G` at h² order, from the categorical non-abelian Stokes
(Yekutieli 2015) integrated over 𝓑_3's 8-fold ideal-octahedral
tessellation. It is **structurally distinct** from PR #701's
falsified Wedderburn-sum search: the contribution comes from
non-abelian-multiplicative-integral curvature on the Borromean ribbon
surface, not from sums of `dim_q V_λ` over partitions. PR #701's
falsification of `5/2 − h²·G` only rules out the *Wedderburn-sum*
incarnation of that form.

## Framework's substrate-pure prediction (Reading B; per 2026-05-22 user direction "framework B only")

The framework's honest λ_scale prediction is the **categorical SUM** of
two independently-derived contributions:

```
λ_scale^Yekutieli = λ_Wedderburn + λ_curvature
                  = Family A (proved theorem) + Yekutieli per-cell (load-bearing conjecture)
                  = (5/2 + (3/4)·h²)           + (−G · h²)
                  = 5/2 + (3/4 − G) · h²       + O(h⁴)
```

At q_0:
- `λ_scale^Yekutieli(q_0)  ≈  2.49266`
- `m_p^pred(q_0)  ≈  m_e · Vol(𝓑_3)/ℏ_q² · 2.493  ≈  951 MeV`
- vs CODATA `938.27 MeV`  →  **+1.4 % framework gap** (halved from
  Family A's ~3 % gap)

This is the framework's honest m_p prediction under the Yekutieli-extended
substrate-pure derivation.

**Why this is the framework's prediction (not a fit):** both
contributing terms are derived from independent substrate-natural
principles:
- **Family A** = `(1/4) · Σ_{λ ⊢ 4} dim_q V_λ`. Proved theorem
  (PR #701 + sympy + Lean; on production via PR #895). The
  Wedderburn h² coefficient `+3/4` is exact; the series TERMINATES
  at h².
- **Yekutieli per-cell** = `−Vol(𝓑_3) / 8 = −G`. Cell-level
  hyperbolic volume; comes from the non-abelian-Stokes structural
  argument of `2026-05-18-conjecture-proof-step3-yekutieli.md`
  §3-5. Per-cell `G = V_oct / 2 = Λ(π/4)` is standard differential
  geometry (Adams 1985 + Lobachevsky); the `−` sign comes from the
  orientation convention of the Yekutieli integral.

Neither contribution is fit against CODATA; the +1.4 % residual is
what the framework knows.

## The load-bearing conjecture (formalised)

The Yekutieli audit Step 3 has one provably-true input (Wedderburn
h² coefficient `+3/4` from Family A, PR #701), one derived input
(`Vol(𝓑_3) = 8G` from Adams 1985), one standard-differential-
geometry input (curvature = hyperbolic volume), and **one load-
bearing conjecture** the audit itself flags:

**Conjecture (cell-extraction-by-half-symmetric-projection).**
*Let `Π_HS : H_4(q) → H_4(q)` be the half-symmetric Wedderburn
projection (onto the conjugate-pair-symmetric sub-algebra at H_4).
The non-abelian-multiplicative-integral of the q-deformation
curvature 2-form across the Borromean ribbon surface, restricted
via `Π_HS`, extracts the curvature contribution of exactly **one**
of the 8 ideal octahedral cells in the 𝓑_3-complement tessellation,
at h² order.*

Stated symbolically:

```
τ^{(2)}_{half-sym}(β_Bor)  :=  (1/2) · d²/dq² |_{q=1} [ Π_HS ∘ τ_q ] (β_Bor)
                            =  −G   ( = −Vol(𝓑_3) / 8 )
```

with the right-hand side being the per-cell hyperbolic volume of
**one** of the 8 ideal octahedra (sign by the absorption convention
in [Yekutieli, 2015]).

## Where the conjecture comes from

The audit's structural sketch (`2026-05-18-conjecture-proof-step3-
yekutieli.md` §"Concrete next R&D" item 1):

| Wedderburn block (λ ⊢ 4) | conj | Octahedral cell type |
|---|---|---|
| (4), (1,1,1,1) | conjugate pair | "vertex" octahedra (2 of 8) |
| (3,1), (2,1,1) | conjugate pair | "edge" octahedra (4 of 8) |
| (2,2) | self-conjugate | "center" octahedron (1 of 8, ×2 multiplicity?) |

The combinatorial argument for "extracts ONE cell" is informally
2 + 4 + 2 = 8 cells in the tessellation, half-symmetric projection
extracts (1/2)·(2 + 4) + 1 = 4 conjugate-pair-averaged contributions
plus the self-conjugate; the audit then claims this reduces to ONE
octahedral cell contribution by symmetry, but the explicit
construction of the bijection is exactly the audit's `Concrete next
R&D` item 1 and is the load-bearing step.

## Numerical landscape (witness)

[`computations/lambda_scale_alt_i_yekutieli_percell_numerical.py`](../../computations/lambda_scale_alt_i_yekutieli_percell_numerical.py)
emits the witness
[`lambda-scale-alt-i-yekutieli-percell-numerical.witness.json`](../../computations/lambda-scale-alt-i-yekutieli-percell-numerical.witness.json)
documenting:

  | quantity | value at q_0 |
  |---|---:|
  | Family A (current production, #895) | 2.5327796637 |
  | **λ_scale^Yekutieli (framework prediction)** | **2.4926599595** |
  | CODATA target (retired empirical anchor) | 2.4599527869 |
  | Family A vs CODATA | +2.96 % |
  | **Yekutieli vs CODATA** | **+1.33 %** ← gap halved |
  | Yekutieli vs Family A | −1.58 % ← per-cell correction |

## Alternative reading (REMOVED per 2026-05-22 user direction "framework B only")

An earlier version of this audit also discussed an alternative reading
`λ = 5/2 − G·h²` (in which the Yekutieli mechanism REPLACES the
Wedderburn h² coefficient rather than ADDING to it). That reading
was **removed as a framework candidate** because:

1. It lands at +5.6 ppm from CODATA — the same coincidence basin as
   the empirical `5/2 − h²·G` PSLQ candidate that PR #701 falsified
   across 5 independent structural routes.
2. It would conflict with Family A's PROVED theorem at h² order
   (Family A's +3/4 coefficient is exact, sympy + Lean verified).
3. Treating it as the framework's prediction would amount to picking
   the coincidence basin without a categorical bijection proof —
   which is the same antipattern PR #895 escaped by adopting Family A
   in production.

The framework's substrate-pure Yekutieli prediction is the categorical
SUM (Reading B above), not the coincidence-basin REPLACEMENT.

## What this audit does NOT do

- **No proof** of the load-bearing categorical bijection. The audit
  §"Concrete next R&D" item 1 (explicit cell-↔-half-sym-projection
  bijection construction at H_4) is the required categorical theory
  work; this audit only formalises the conjecture.
- **No Lean formalisation.** Mathlib lacks the non-abelian
  multiplicative integral primitive
  ([audit §4 R&D item 4](2026-05-18-conjecture-proof-step3-yekutieli.md)
  classifies this as a long-term dependency).
- **No production wiring.** Family A (per #895) remains the
  framework's substrate λ_scale in production. The Yekutieli-
  extended Reading B is the framework's *honest predictive* formula
  given both substrate-natural contributions, but a production update
  from Family A → Reading B (5/2 + (3/4)h² → 5/2 + (3/4 − G)h²)
  should happen in a follow-up PR once:
  1. The cell-↔-projection bijection is rigorously closed, OR
  2. The repo owner explicitly authorises the production move
     pending bijection proof (treating the Yekutieli per-cell
     contribution as accepted under the same conjecture-conditional
     status that Family A had pre-#895).

## Open follow-ups for production-update consideration

If the user directs a production move from Family A → Yekutieli
(Reading B):

- Update `m_p_borromean_verification_50dps.py`'s λ_scale formula
- Refresh `per-observable-100x-status.witness.json` with Yekutieli
  prediction (m_p ≈ 951 MeV; framework gap drops from 3 % to 1.4 %)
- Add a note to `docs/canonical-derivation-cheat-sheet.md §5` Item #1
  recording the Yekutieli extension
- Coordinate with #920 (cheat-sheet manager tracker), #917
  (per-observable 100× dashboard)

## Cross-references

- [`docs/audits/2026-05-18-conjecture-proof-step3-yekutieli.md`](2026-05-18-conjecture-proof-step3-yekutieli.md) — original Yekutieli structural argument (May 18)
- [`prop:yekutieli-stokes-mass`](../../content/quantum-observable-universe/lifting-and-descent/) — categorical Stokes block family
- [`docs/audits/2026-05-22-q-dilog-tower-spike-lambda-scale.md`](2026-05-22-q-dilog-tower-spike-lambda-scale.md) — q-dilog Tier 0 negative (af2d27ee on main)
- [PR #928](https://github.com/litlfred/qou/pull/928) — q-dilog Tier 1+ negative (|V̂_S| + Q(ζ_60) + knot vols, coeff 10³⁰)
- [`docs/agent-briefs/2026-05-22-lambda-scale-qdilog-tower-direct.md`](../agent-briefs/2026-05-22-lambda-scale-qdilog-tower-direct.md) §Recommended ordering — Yekutieli (Strategy I) is the remaining open direction; categorical theory work, not compute.
