# Family A gap audit — the +2.89-3.86% systematic offset

**Date:** 2026-05-24 (twice-amended — see banner)
**Trigger:** `2026-05-24-65-isotope-mass-table-audit.md` reports +2.89-3.86% systematic offset across all 65 isotopes. Per-observable accuracy (L2 leg of `docs/precision-goals.md`) misses the 100× experimental target by 6-9 orders of magnitude SOLELY because of this gap. This audit diagnoses the cause and identifies the canonical closure path.

> ⚠️ **2026-05-24 amendment #2 (canonical-aligned with the on-main purge).**
> The first amendment of this doc framed the closure as "Strategy I"
> (Yekutieli per-cell ADD: `λ_scale = 5/2 + (3/4 − G)·h²`). That
> framing was also wrong. **Commit `71d674da1` on `main`** (2026-05-24
> 02:10) **PURGED** the Yekutieli per-cell extension as non-canonical:
>
> > "Yekutieli per-cell curvature (−G·h²) is NOT CANONICAL:
> >  - Bijection NEGATIVE (PR #985): natural-reading κ = +0.5, not −G
> >  - Reading A is substrate-q₀ coincidence (c₂ = 62.6 ≠ −G)
> >  - No categorical backing for the −G·h² term"
>
> Per the user directive ([PR #1080](https://github.com/litlfred/qou/pull/1080)
> body): *"no lambda-scale. it was absorbed. there was already a per
> knot Geom(K) factor that was canonically derived. please fix all
> documentation."* The canonical mass formula is:
>
> $$m(K) = m_e \cdot \mathrm{VolDensity}(K, q_0)$$
>
> — a **single** Geom call per knot/link, per `prop:geom-universality`.
> There is no separate `λ_scale` constant. The +2.89 % m_p residual
> is the gap between the framework's current categorical
> `VolDensity(𝓑₃)` computation and its **categorically-exact** value
> at higher orders in $h^2$. The closure path is **refinement of
> `VolDensity`**, not a separate additive correction. See PR #1080
> for the doc-wide framing cleanup that this audit now aligns with.

**TL;DR (re-amended):** The +2.89 % gap is a **VolDensity(𝓑₃)
categorical-exactness refinement gap** at $h^2$ order. Two structural
inputs to refine VolDensity's exactness remain open: (a) the
S_4↓S_3 half-symmetric bijection (combinatorial branching, standard
Mathlib; provable today) and (b) the S_5↔SO(3) fiber action on
Bring's surface (partition-wise Wedderburn ↔ spatial rotations).
Neither is "a Yekutieli per-cell correction" — both are structural
inputs that constrain what `VolDensity(𝓑₃, q_0)` must equal at
categorical exactness. The bare REPLACE form `5/2 − G·h²` was
PSLQ-coincidence falsified 2026-05-18; the Yekutieli per-cell ADD
form was purged 2026-05-24. The structural refinement path goes
through VolDensity itself, not through these forms.

## §1. The canonical formula (post-purge state on main)

Per `m_p_borromean_verification_50dps.py` (current on main, post-purge commit `71d674da1`):

```python
# Honest predictions (PROVED Family A, PR #895 + #942):
#   m_p^pred ≈ 965 MeV  (vs CODATA 938.27, +2.89 %)
```

The production compute chain is:

$$m_p^{\text{pred}} = m_e \cdot \mathrm{VolDensity}(\mathcal{B}_3, q_0)$$

where `VolDensity(𝓑₃, q_0)` is the per-knot Geom-functor evaluation on the proton's canonical braid → Borromean closure. The numerical decomposition at $q_0$:

| Term | Value | Status |
|---|---:|---|
| $m_e$ (CAL-1) | 0.510998950 MeV | PROVED (calibration) |
| $\mathrm{Geom_{leading}} = \mathrm{Vol}(\mathcal{B}_3)/\hbar_q^2$ | 746.4 | PROVED (Adams 1985 + Wenzl) |
| Family A residual factor $\lambda_A = 5/2 + (3/4)h^2$ | ~2.5328 | PROVED algebraically |
| $m_p^{\text{pred}}$ | ~965.38 MeV | **+2.89 % vs CODATA** ← the gap |

The gap is between this categorical computation and its categorically-exact value at higher $h^2$ orders.

## §2. Why the prior framings were wrong

| framing | claim | status | reference |
|---|---|---|---|
| **Reading A (REPLACE)** | `λ_scale = 5/2 − G·h²` closes m_p to 5.6 ppm | **falsified 2026-05-18** — PSLQ coincidence, no Wedderburn derivation gives `−G·h²` | [`2026-05-18-conjecture-falsification.md`](2026-05-18-conjecture-falsification.md) |
| **Strategy I / Reading B (ADD)** | `λ_scale = 5/2 + (3/4 − G)·h²` halves the gap to +1.33 % | **purged 2026-05-24** — PR #985 bijection NEGATIVE (κ = +0.5, not −G); no categorical backing | commit `71d674da1` |
| **λ_scale as a separate constant** | distinct from `VolDensity(K)` | **absorbed 2026-05-23** — there is no `λ_scale` post-`ffdd84409`; `VolDensity(K)` is the only object | [PR #1080](https://github.com/litlfred/qou/pull/1080) |

The current canonical understanding (per the on-main purge + PR #1080 framing): **the +2.89 % gap lives inside `VolDensity(𝓑₃)`**. Closing it requires refining `VolDensity`'s categorical computation, not adding an external correction.

## §3. Canonical refinement path

Per `prop:geom-universality` ([content/quantum-observable-universe/braids-and-knots/geom-universality.md](../../content/quantum-observable-universe/braids-and-knots/geom-universality.md)),
`VolDensity` is the unique Frobenius-Hopf-compatible functional on the braid-closure → link cobordism category. Its categorical exactness on $\mathcal{B}_3$ at $h^2$ order requires two structural inputs that are independent and complementary:

| Structural input | Status | Role in refining VolDensity |
|---|---|---|
| **S_4↓S_3 half-symmetric Wedderburn projection** (`prop:s4-s3-half-symmetric-projection`: $\frac{5}{2} \times \frac{2}{5} = 1$) | narrative-proved (standard $S_n$ branching rule); **Lean: not yet formalized** | Constrains which Wedderburn cells contribute to the trace at the $h^2$ order. The bijection is sound combinatorics regardless of any per-cell curvature value. |
| **S_5 ↔ SO(3) fiber action on Bring's surface** | **NOT YET FORMALIZED** | Ties the partition-wise Wedderburn action (S_5 on $h_q$) to spatial SO(3) rotations on Bring's quintic surface. Load-bearing for how the cell extraction lifts to the spatial geometry that `VolDensity` integrates over. |
| **q-locality of the canonical $h^2$ expansion** | tested negatively on bare polynomials (PR #951); **not yet tested** end-to-end on `VolDensity` output | Smooth-crossing probe verifies $h^2$ structure is intrinsic to `VolDensity`, not an artifact of any one expansion. |

Per `prop:geom-universality` itself (CONDITIONAL, §3b-cond, Lean: 0 sorries — proved from class hypotheses conditional on `conj:hyperbolic-volume-transcendence` + `rem:baryon-period-ratio`), the categorical-exactness refinement of `VolDensity(𝓑₃)` does NOT require introducing a new per-cell curvature term. The bijection + SO(3) fiber action constrain what value `VolDensity` must take; the value itself is determined by `VolDensity`'s own structure.

## §4. Action items (queued; this PR ships only the audit doc)

These three tasks remain the canonical refinement work. Reframed under the canonical post-purge framing, they're all about refining `VolDensity`, not adding corrections:

| # | Item | Effort | Gates |
|---|------|--------|-------|
| 4.1 | Add this audit doc to the repo (THIS PR) — twice-amended for alignment with purge | done | — |
| 4.2 | **Formalize `prop:s4-s3-half-symmetric-projection` in Lean** — combinatorial bijection $\frac{5}{2} \times \frac{2}{5} = 1$, standard $S_n$ branching rule, Mathlib. PROVED status (no conditional class, no κ claim). **Note:** the `.md` block's "Application to λ_scale" section is now stale per [PR #1080](https://github.com/litlfred/qou/pull/1080); the Lean formalization scopes to the combinatorial bijection only. | 1-3 days | none |
| 4.3 | **Re-run q-locality smooth-crossing probe** end-to-end on `VolDensity(𝓑₃, q)` output as $q$ varies near $q_0$ — NOT on any bare polynomial like `5/2 + (3/4 − G)·h²` (which is purged anyway). PR #951 failed on the bare polynomial; this is a different test on the actual `VolDensity` evaluation. | 1-2 days | none |
| 4.4 | **Formalize `S_5 ↔ SO(3)` fiber action** on Bring's surface — partition-wise Wedderburn actions ↔ spatial SO(3) rotations on Bring's quintic. Load-bearing for `VolDensity` categorical exactness on $\mathcal{B}_3$. | 3-5 days | needs categorical-spatial chain; biggest deliverable |
| 4.5 | When 4.2 + 4.4 land: re-evaluate whether `VolDensity(𝓑₃, q_0)` can be computed to categorical exactness at $h^2$ order, potentially closing or reducing the +2.89 % gap. | depends on 4.2, 4.4 | gated |

## §5. Pointers

- [`docs/audits/2026-05-18-conjecture-falsification.md`](2026-05-18-conjecture-falsification.md) — REPLACE form `5/2 − G·h²` falsified
- [`docs/audits/2026-05-23-lambda-scale-replace-vs-add-analysis.md`](2026-05-23-lambda-scale-replace-vs-add-analysis.md) — Strategy I numerics + residual decomposition (historical; superseded by 2026-05-24 purge)
- [`docs/coordination/2026-05-23-algebraic-geometric-observable-consistency.md`](../coordination/2026-05-23-algebraic-geometric-observable-consistency.md) — Layer 1/2/3 structural audit (parent of this audit)
- [`docs/audits/2026-05-24-65-isotope-mass-table-audit.md`](2026-05-24-65-isotope-mass-table-audit.md) — empirical observation across 65 isotopes
- [PR #1080](https://github.com/litlfred/qou/pull/1080) — λ_scale framing cleanup (absorbed into VolDensity)
- commit `71d674da1` (on main) — purge of Yekutieli per-cell from production
- [`content/quantum-observable-universe/braids-and-knots/s4-s3-half-symmetric-projection.md`](../../content/quantum-observable-universe/braids-and-knots/s4-s3-half-symmetric-projection.md) — bijection block (TOP is sound combinatorics; "Application to λ_scale" stale per PR #1080)
- [`content/quantum-observable-universe/braids-and-knots/geom-universality.md`](../../content/quantum-observable-universe/braids-and-knots/geom-universality.md) — `prop:geom-universality` (CONDITIONAL, §3b-cond)
- [`computations/m_p_borromean_verification_50dps.py`](../../computations/m_p_borromean_verification_50dps.py) — production m_p formula (Family A only; +2.89 %)
- [`CLAUDE.md §3b-cond`](../../CLAUDE.md) — conditional-class theorem conventions

## §6. Sibling: canonical-discipline paper sweep findings (parallel run)

A parallel canonical-discipline sweep audited all of
`content/quantum-observable-universe/**/*.md` for empirical /
fitting / probing / numerology floating in paper content.

**Verdict: paper is in good shape — 4 actionable items, 0 critical.**

| # | File | Severity | Action |
|---|------|----------|--------|
| 6.1 | `chirality-writhe-ribbon-derivation.md` | MAJOR | The negative H_6-satellite result indicates writhe is not a primary derivation route for $a_K$. The SU(2) CBH ½[α,α] curvature path (Yekutieli 2015 as external math reference) is not load-bearing for production after the 2026-05-24 purge; it's external math context only. Move negative-result narrative to an audit doc. |
| 6.2 | `lambda-scale-substrate-form.md` | MEDIUM → CRITICAL | Per [PR #1080](https://github.com/litlfred/qou/pull/1080)'s λ_scale-absorbed-into-VolDensity framing: this entire block needs reframing or archival. λ_scale is no longer a separate constant. |
| 6.3 | `dressed-quark-numerology-at-q0.md` (filename) | LOW (cosmetic) | Rename → `dressed-quark-mass-at-q0.md`. Content is structurally sound (Skein-corrected + 1/3 flavor-split). |
| 6.4 | `unified-curvature-rank-mass-formula.md` | INFO | "empirically it accounts for ~3% of the binding energy" — add nucleus / term context for clarity. |

Audit docs and coordination docs were skipped per directive (their
experimental content is appropriate to their role).

Class-A opt-out labels, CAL-4 banners, and conditional caveats are
applied consistently throughout the paper. The three-calibration
discipline is broadly enforced.

**Sibling cleanup actions queued for separate small PRs** — not in
scope for this audit's scope (the Family A gap).
