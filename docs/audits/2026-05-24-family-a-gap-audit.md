# Family A gap audit — the +2.89-3.86% systematic offset

**Date:** 2026-05-24 (amended)
**Trigger:** `2026-05-24-65-isotope-mass-table-audit.md` reports +2.89-3.86% systematic offset across all 65 isotopes. m_p / m_n / Δ_pn miss the 1ppb-100×-experimental target by 6-9 orders of magnitude SOLELY because of this gap. This audit diagnoses the cause and identifies the canonical closure path.

> ⚠️ **2026-05-24 amendment.** The original audit framed the closure as
> `λ_scale = 5/2 − G·h²` (REPLACE form, "Reading A") and cited
> `lambda-scale-rd1-geometric.witness.json` as empirical confirmation.
> **That framing was wrong.** The REPLACE form was **structurally
> falsified** on 2026-05-18 (see
> [`2026-05-18-conjecture-falsification.md`](2026-05-18-conjecture-falsification.md)):
> no categorical realization of the half-symmetric H_4 projection
> yields `−G·h²` from Wedderburn data, and the 5.6 ppm CODATA match
> was deemed a PSLQ-style numerical coincidence. The empirical probe
> is **not** evidence for Reading A; it is evidence for *some*
> closure near `−G·h²` numerically, which Reading B (Strategy I,
> Yekutieli ADD form) recovers structurally to within +1.33 %.
>
> The canonical closure path is **Strategy I (Yekutieli ADD)**:
> `λ_scale = 5/2 + (3/4 − G)·h²`. It closes 2.22× of the wedge
> (from +2.89 % to +1.33 %) and is anchored in the S_4↓S_3 half-
> symmetric bijection (`prop:s4-s3-half-symmetric-projection`).
> The residual +1.33 % ("Strategy K gap") remains open as a separate
> research direction. See §1, §2, §3 below for the corrected
> structural diagnosis. The original §1-§3 are preserved in the
> git history of this branch (commits prior to this amendment).

**TL;DR (amended):** The gap is the algebra-vs-geometry skip in the
production mass formula. Family A's algebraic
`λ_scale = 5/2 + (3/4)·h²` (Wedderburn dimensions at H_4) has not
been augmented with the Yekutieli per-cell curvature correction
on the Borromean complement. The canonical-conditional Strategy I
closure is **`λ_scale = 5/2 + (3/4 − G)·h²`** (Wenzl + Yekutieli
ADD), which closes m_p to **+1.33 %** — a 2.2× improvement over
the current +2.89 % gap. **Wiring is gated on formalizing the
S_4↓S_3 bijection in Lean and the per-cell Yekutieli integration.**
The remaining +1.33 % residual is a known open frontier
("Strategy K"), tracked separately.

## §1. Empirical diagnosis (corrected reading)

The empirical probe `lambda-scale-rd1-geometric.witness.json`
reports a numerical fit to the implied closure coefficient. The
**correct structural reading** of that probe is **not** that
`λ = 5/2 − G·h²` (REPLACE), but that the gap is consistent with a
Yekutieli per-cell additive correction:

| Quantity | Value | Meaning |
|----------|------:|---------|
| `pi_alg_at_q0` | 2.5328 | Family A's `λ_A(q₀) = 5/2 + (3/4)·h²(q₀)` (PROVED Wedderburn) |
| `lambda_p_target` | 2.4600 | What λ needs to be for m_p closure |
| Family A residual | +2.89 % | m_p propagation gap (Wenzl-only) |
| Strategy I (ADD) value | 2.4927 | `5/2 + (3/4 − G)·h²` (Wenzl + Yekutieli) |
| **Strategy I residual** | **+1.33 %** | m_p propagation gap (Strategy I, post-Yekutieli) |
| Numerical coincidence `5/2 − G·h²` | 2.4600 | PSLQ match at 5.6 ppm — **falsified structurally 2026-05-18** |

The implied **Strategy I** (Yekutieli ADD) closure:

$$
\lambda_{\text{scale}}^{\text{Strategy I}}
  = \underbrace{\tfrac{5}{2} + \tfrac{3}{4} h^2}_{\text{Family A (Wenzl, PROVED)}}
    + \underbrace{(-G)\cdot h^2}_{\text{Yekutieli per-cell, ONE octahedron}}
  = \tfrac{5}{2} + \bigl(\tfrac{3}{4} - G\bigr)\cdot h^2
$$

where $G = \mathrm{Catalan} \approx 0.9160$.

Numerical check at $q_0 \approx 1.1098$, $h \approx 0.2087$, $h^2 \approx 0.0436$:

$$
\lambda_{\text{scale}}^{\text{Strategy I}}(q_0)
  \approx 2.5 + 0.0327 - 0.0399 \approx 2.4928
$$

Propagating to $m_p$: **~13 313 ppm (+1.33 %)** vs. the Family A
**+29 605 ppm (+2.89 %)** — a 2.22× improvement. The remaining
+1.33 % is the "Strategy K" frontier (see §4).

## §2. Structural diagnosis (the bijection)

Per [`docs/coordination/2026-05-23-algebraic-geometric-observable-consistency.md`](../coordination/2026-05-23-algebraic-geometric-observable-consistency.md),
the production compute pipeline currently does:

```
ALGEBRAIC (Wenzl):    dim_q V_λ at H_4 → (1/4) Σ_λ dim_q V_λ
                                       = 5/2 + (3/4)·h²
                                              ↑
                                       PROVED (Family A)
GEOMETRIC (Yekutieli): per-cell curvature −Vol(𝓑₃)/8 = −G
                       on ONE octahedral cell (extracted by
                       half-symmetric H_4 projection)
                                              ↑
                       conditional on S_4↓S_3 bijection
                       + Yekutieli integration formalization
TOTAL (Strategy I):   5/2 + (3/4 − G)·h²
                                              ↑
                       closes +2.89 % → +1.33 %
```

**Why "one cell"?** Per `prop:s4-s3-half-symmetric-projection`
([content/quantum-observable-universe/braids-and-knots/s4-s3-half-symmetric-projection.md](../../content/quantum-observable-universe/braids-and-knots/s4-s3-half-symmetric-projection.md)),
the half-symmetric Wedderburn projection on $H_4(q)$ combined with the
$S_3$-trivial subspace projection extracts the curvature contribution
of exactly one of the 8 ideal octahedra in the Borromean complement:

$$
  \underbrace{\tfrac{5}{2}}_{\text{half-sym H_4 count}}
  \times \underbrace{\tfrac{2}{5}}_{S_3\text{-trivial factor}}
  = 1.
$$

With Adams 1985 ($\operatorname{Vol}(\mathcal{B}_3) = 8G$), the
per-cell contribution at $h^2$ order is $-G$.

**This is the bijection** that anchors the Yekutieli ADD form — not
a REPLACE of Family A, but a structural augmentation of it. The
falsified Reading-A `5/2 − G·h²` was numerologically suggestive
because Reading A and Strategy I (ADD) converge to within 1.33 % at
$q_0$, but only Strategy I has a categorical bijection backing it.

## §3. Canonical-derivation status (the gate)

Per user directive (2026-05-24): "WE NEED CANONICALLY DERIVED ONLY...
probe is ok, but nothing gets wired into pipeline that isnt".

| Component | Status | Notes |
|-----------|--------|-------|
| Family A algebraic `λ_A = 5/2 + (3/4)·h²` | **PROVED** | `lambda_scale_all_c_i_family_a.py` + Lean (PR #895 / #942); h-series terminates at h² exactly |
| Vol(𝓑₃) = 8·G | **PROVED** | PR #843 fix; Adams 1985 + Λ(π/4) = G/2 |
| `prop:s4-s3-half-symmetric-projection` (bijection: 5/2 × 2/5 = 1) | **NARRATIVE-PROVED, LEAN NOT YET FORMALIZED** | Standard $S_n$ branching rule; one-page combinatorial proof |
| `prop:geom-universality` (Geom(K) is the unique Frobenius-Hopf-compatible functional) | **CONDITIONAL** (§3b-cond) | Lean: 0 sorries; proved from class hypotheses. Conditional on `conj:hyperbolic-volume-transcendence` + `rem:baryon-period-ratio` |
| `prop:geom-yekutieli-alignment` (per-cell `−G` from Yekutieli non-abelian Stokes) | **partially formalized** | Yekutieli 2015 (arXiv:1007.1250v4) per-cell volume integration; Lean stub exists; full proof pending |
| **REPLACE form** `5/2 − G·h²` (Reading A) | **FALSIFIED 2026-05-18** | No Wedderburn derivation yields `−G·h²`; 5.6 ppm match is PSLQ coincidence. Do not cite as canonical. |
| **Strategy K** (+1.33 % residual closure) | **OPEN** | Post-Yekutieli residual matches `+(3/4)·h²` to 316 ppm — see [`2026-05-23-lambda-scale-replace-vs-add-analysis.md §2`](2026-05-23-lambda-scale-replace-vs-add-analysis.md) for the two reconciliations |

**Wiring readiness assessment:**

Strategy I (ADD form) `λ_scale = 5/2 + (3/4 − G)·h²` is
**conditionally canonical** — its two structural inputs are
(a) the S_4↓S_3 half-symmetric bijection (narrative-proved,
combinatorial) and (b) the Yekutieli per-cell integration
(partially formalized, conditional on Geom-universality).

Per CLAUDE.md §3b-cond, conditional-class theorems CAN be wired
into production with explicit conditional banners + Lean class
hypotheses + `uses[]` declaring the conjectures. The bijection
itself has no conjectural dependencies and is the next mechanical
formalization step.

## §4. Recommendation (corrected)

**Three actions, in order:**

1. **Formalize `prop:s4-s3-half-symmetric-projection` in Lean** as
   a PROVED proposition (no conditional class — the standard
   $S_n$ branching rule is fully in Mathlib). 1-3 days. **Unblocks
   geometric h² → PROVED status for the bijection half of
   Strategy I.**

2. **Re-run q-locality smooth-crossing probe** on the
   Strategy I (ADD) form `5/2 + (3/4 − G)·h²` end-to-end through
   the full Geom(K) functor output, not on the bare polynomial.
   PR #951 failed on the standalone polynomial `5/2 − G·h²`
   because (a) that was the falsified REPLACE form and (b) it was
   tested as a bare polynomial without the Geom-functor pull-back.
   1-2 days. **Validates that Strategy I survives q-locality.**

3. **Formalize `S_5 ↔ SO(3)` fiber action on Bring's surface** —
   the explicit map between partition-wise Wedderburn actions
   (S_5 on h_q) and spatial SO(3) rotations on Bring's quintic
   surface. This is the missing structural piece tying the
   Wedderburn `5/2` to the spatial 8-cell tessellation. 3-5 days.
   **Unblocks the per-cell Yekutieli integration as a fully
   structural step.**

**The +1.33 % Strategy K residual remains open** after #1-#3 land.
The residual decomposition (`(λ_Strategy I − λ_fit) / h² ≈ 0.7503`
matching `+(3/4)·h²` to 316 ppm — see
[`2026-05-23-lambda-scale-replace-vs-add-analysis.md §2`](2026-05-23-lambda-scale-replace-vs-add-analysis.md))
gives two structural candidates for a "Strategy K" closure: a
third independent correction near `+(3/4)·h²`, or a structural
re-evaluation of whether Family A's contribution to the m_p
formula should be present at all. Strategy K is not gated on this
audit; it is a forward-research direction.

## §5. Action items (queued; this PR ships only the audit)

| # | Item | Effort | Gates |
|---|------|--------|-------|
| 5.1 | Add this audit doc to the repo (THIS PR) | done | — |
| 5.2 | **Formalize `prop:s4-s3-half-symmetric-projection` in Lean** — PROVED status for the bijection (5/2 × 2/5 = 1) | 1-3 days | none — combinatorial $S_n$ branching rule, standard Mathlib |
| 5.3 | **Re-run q-locality probe** on Strategy I (ADD) end-to-end through Geom(K), not bare polynomial | 1-2 days | none — direct re-run with full functor output |
| 5.4 | **Formalize `S_5 ↔ SO(3)` fiber action** on Bring's surface — partition Wedderburn actions ↔ spatial rotations | 3-5 days | needs categorical-spatial chain; biggest deliverable |
| 5.5 | When 5.2-5.4 land: wire Strategy I as **opt-in flag** `method="strategy_i_yekutieli"` in `m_p_borromean_verification_50dps.py`; document +1.33 % Strategy K residual in witness | 1 day | gated on 5.2-5.4 |
| 5.6 | **Strategy K research-direction spec** — separate audit doc enumerating the two reconciliations from §2 above + concrete test plans | 1 day | non-blocking; documents the open frontier |
| 5.7 | Regen stale `canonical-mass-table-extended.witness.json` — done in PR #1064 (merged 2026-05-24) | done | — |

## §6. Pointers

- [`docs/audits/2026-05-18-conjecture-falsification.md`](2026-05-18-conjecture-falsification.md) — REPLACE form `5/2 − G·h²` falsified (PSLQ coincidence)
- [`docs/audits/2026-05-23-lambda-scale-replace-vs-add-analysis.md`](2026-05-23-lambda-scale-replace-vs-add-analysis.md) — Strategy I numerics + Strategy K residual decomposition
- [`docs/coordination/2026-05-23-algebraic-geometric-observable-consistency.md`](../coordination/2026-05-23-algebraic-geometric-observable-consistency.md) — Layer 1/2/3 structural audit (parent of this audit)
- [`docs/audits/2026-05-24-65-isotope-mass-table-audit.md`](2026-05-24-65-isotope-mass-table-audit.md) — empirical observation across 65 isotopes
- [`content/quantum-observable-universe/braids-and-knots/s4-s3-half-symmetric-projection.md`](../../content/quantum-observable-universe/braids-and-knots/s4-s3-half-symmetric-projection.md) — the bijection (Reading B / Strategy I anchor)
- [`content/quantum-observable-universe/braids-and-knots/geom-universality.md`](../../content/quantum-observable-universe/braids-and-knots/geom-universality.md) — `prop:geom-universality` (conditional, §3b-cond)
- [`folio-assistant/computations/lambda_scale_all_c_i_family_a.py`](../../folio-assistant/computations/lambda_scale_all_c_i_family_a.py) — Family A PROVED source
- [`folio-assistant/computations/lambda_scale_strategy_i_yekutieli_probe.py`](../../folio-assistant/computations/lambda_scale_strategy_i_yekutieli_probe.py) — Strategy I numerical verification
- [`folio-assistant/computations/m_p_borromean_verification_50dps.py`](../../folio-assistant/computations/m_p_borromean_verification_50dps.py) — production m_p formula (currently Family A only)
- [`CLAUDE.md §3b-cond`](../../CLAUDE.md) — conditional-class theorem conventions

## §7. Sibling: canonical-discipline paper sweep findings (parallel run)

A parallel canonical-discipline sweep audited all of
`content/quantum-observable-universe/**/*.md` for empirical /
fitting / probing / numerology floating in paper content.

**Verdict: paper is in good shape — 4 actionable items, 0 critical.**

| # | File | Severity | Action |
|---|------|----------|--------|
| 7.1 | `chirality-writhe-ribbon-derivation.md` | MAJOR | **Re-contextualize** as a Yekutieli entry-point — the negative H_6-satellite result indicates writhe is not a primary derivation route for $a_K$, but the SU(2) CBH ½[α,α] curvature path (Yekutieli 2015 per-cell) IS load-bearing for Strategy I. Don't move out of paper; re-frame. |
| 7.2 | `lambda-scale-substrate-form.md` | MEDIUM | Refactor: move original "Conjecture (now empirical)" block to a historical footnote; lead with reframed structural constant-C problem. |
| 7.3 | `dressed-quark-numerology-at-q0.md` (filename) | LOW (cosmetic) | Rename → `dressed-quark-mass-at-q0.md`. Content is structurally sound (Skein-corrected + 1/3 flavor-split). |
| 7.4 | `unified-curvature-rank-mass-formula.md` | INFO | "empirically it accounts for ~3% of the binding energy" — add nucleus / term context for clarity. |

Audit docs and coordination docs were skipped per directive (their
experimental content is appropriate to their role).

Class-A opt-out labels, CAL-4 banners, and conditional caveats are
applied consistently throughout the paper. The three-calibration
discipline is broadly enforced.

**Sibling cleanup actions queued for separate small PRs** — not in
scope for this audit's scope (the Family A gap).
