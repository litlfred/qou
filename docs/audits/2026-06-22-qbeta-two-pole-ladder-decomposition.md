# Q_β F(q) — two-pole ladder decomposition + the pole-structure map

**Date:** 2026-06-22
**PR:** [#2611](https://github.com/litlfred/qou/pull/2611) (branch `claude/epic-hopper-f97it3`)
**Status:** structural diagnostic — no closure, no fit, no wiring, no tier change
**Script:** [`qbeta_two_pole_ladder_decomposition.py`](../../computations/qbeta/qbeta_two_pole_ladder_decomposition.py) · witness `qbeta-two-pole-ladder-decomposition.witness.json`

## Why this exists

The 1ppQ Q_β keystone is the fibre-level Habiro element `F(q)` / its kernel
`R(q,ξ)`. Two F-poles of the precision-ladder generating function
`g(u) = Σ_{k≥2} c_k u^k` (`u = b·ℏ_q²` at q₀) are now characterized in
**separate** PRs that were never reconciled against each other or against the
actual coefficients:

- **Dominant** — simple pole at `u_substrate`, char root `1/u_substrate ≈ 117.41`,
  tail amplitude `L = lim c_k u_subst^k ≈ 2.118e-13`, residue
  `A = u_subst·L ≈ 1.804e-15` (PR #1727; A precision-capped at ~4 sig figs by
  having only 3 tail rungs, [PR #1805 verdict](2026-06-04-qbeta-residue-a-precision-ceiling-verdict.md)).
- **Subdominant silver** — `Q_A` zero, char root `1/u_silver ≈ 3.1154`
  (PR #2454). Established **purely algebraically** (`Q_A(silver)=0` while
  `Δ(net)(silver) = 82216 + 58136√2 ≠ 0`) — **never tested against the `c_k`**.

This doc reconciles them against the canonical `c₂…c₁₀` and consolidates the
scattered findings into one **pole-structure map** for the kernel search.

## What is already settled (do not re-derive)

- The ladder is **asymptotic**: `g(u)` has a simple pole at the physical point
  `u_substrate`; the product `F = Π(1+c_k u^k)` has an essential singularity
  ([2026-06-02 audit](2026-06-02-qbeta-1ppq-singularity-simple-pole-fibre-level.md)).
- The **residue-A precision ceiling** (~4 sig figs, limited by 3 tail rungs, not
  arithmetic) and the suspicious `A ≈ 1ppQ` scale are **settled** (PR #1727/#1805).
  The categorical residue-A search is comprehensively NEGATIVE across ~8 families;
  the genuine unblock is **canonical c₁₁…c₁₅**, itself gated on the kernel.

This PR adds nothing to those; it characterizes the **low/mid-rung** structure
(where the open rungs live), which the residue-A work never examined.

## Findings

### 1. Rung partition — the dominant pole is TAIL-only

Dominant-pole contribution `D_k = L·root_sub^k`; fraction `|D_k / c_k|`:

| k | 2 | 3 | 4 | 5 | 6 | 7 | 8–10 |
|---|---|---|---|---|---|---|---|
| `\|D_k/c_k\|` | 2.9e-9 | 1.7e-7 | 3.5e-5 | 0.39% | 16% | 114% | ~100% |

The dominant pole (the most-studied object) contributes **< 0.4 % to the open
rungs c₃, c₄, c₅**, ~16 % at c₆, and only overtakes at c₇. So the
**1ppQ-blocking open rungs are not a dominant-pole phenomenon** — they live in
the subdominant + entire sector.

### 2. The silver pole is not the leading subdominant ladder structure

Peeling the dominant pole, the residual `r_k = c_k − D_k` (trusted for k≤7,
given L's 4 sig figs) has ratios `1.07, −2.40, −2.71` — it **changes sign at
k=6** and shows **no clean `+3.1154` geometric**. The canonical `c_k` therefore
**do not corroborate** the silver zero as the leading subdominant ladder
structure. This is the first direct test of PR #2454 against the coefficients,
and it **confirms PR #2454's own caution** ("does not change any rung's tier"):
the silver/`Q_A` zero is a genuine *F-singularity* but is *screened* in the
ladder by the entire/A-sector. Separating a genuine silver contribution from the
A-sector needs canonical higher-order `c_k` or the kernel — not a 4-rung fit.

### 3. Two simple poles do not close the ladder — minimal denominator deg ≥ 3

The depth-2 annihilator of both roots,
`h_k = c_k − (root_sub+root_silver)·c_{k-1} + (root_sub·root_silver)·c_{k-2}`,
is large at low k (entire sector: `|h_k/c_k|` ~ 10²–10³) and collapses to
`1.5e-5·c_k` in the tail. So the minimal denominator
`Q(u) ⊇ (1−root_sub·u)(1−root_silver·u)` but has **degree ≥ 3** — re-confirming
refuted class **C5** (constant kernel) *from the pole side*. The deg≥3 remainder
**is** the open kernel `R(q,ξ)`; `h_k` is the concrete residual the exact
(non-SDP) extraction must reproduce.

## The pole-structure map (consolidated)

`g(u) = Σ c_k u^k` is a C-finite (rational) series whose poles are the
reciprocal characteristic roots (`QOU.QBeta.RationalCoeffRecurrence`). Empirically:

| sector | object | char root / locus | governs rungs | status |
|--------|--------|-------------------|---------------|--------|
| **entire / A** | polynomial part (PR #1622 A-sector) | — | **c₂…c₅ (open)** | the real c₄,c₅ target; entire-sector content |
| **subdominant** | silver / `Q_A` zero | `3.1154` (`u_silver≈0.321`) | screened — leads no rung | genuine F-singularity, small ladder weight (#2454, this PR) |
| **dominant** | non-`Q_A` simple pole | `117.41` (`u_substrate≈0.0085`) | **c₇…∞ (tail)** | residue A capped ~4 sig figs (#1727/#1805) |
| **ζ₄ / B** | fibre bar-antifixed pole | `qi=−q`, `[2]_q=0` | (fibre, not u-plane) | bar-odd residue numerator (`QBetaResidueHabiroDual`) |

**Net for the kernel search:** closing the open rungs c₄,c₅ is an
**entire/A-sector** problem, not a pole-resummation one — the dominant pole is a
tail artifact and the silver pole is screened. Consistent with
[#2106](https://github.com/litlfred/qou/pull/2106) Finding 5 (H₃ operator route
stops at ℓ=3 ⇒ c₄ needs the H₄ towers) and localizes
[#2474](https://github.com/litlfred/qou/pull/2474)'s σ₃-lift target.

## Discipline

- No fit, no wiring, no registry tier change; flip-flop guard + critical-distance
  respected.
- Corpus-grepped before authoring: the residue-A floor/ceiling is settled
  (#1727/#1805) and not re-reported; this is the low/mid-rung complement.
- Pole data from the canonical proton-anchored PR #2454 witness; NO FLOAT, 70 dps.

## Cross-references

- PR #1727 / #1805 — dominant pole + residue-A precision ceiling.
- PR #2454 — silver/`Q_A` subdominant pole (algebraic).
- PR #1622 — three-sector (A/B/C) q-difference decomposition.
- Refuted-class map [C5](2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md)
  — constant kernel (re-confirmed here from the pole side).
- [c_k/d_k canonical registry](../coordination/ck-dk-canonical-registry.md);
  [1ppQ master ledger](../coordination/1ppq-qbeta.md).
