---
# qou-r91v
title: 'Phase 4: prove β=2 maximises E_β[C₂] on [2,∞) (Jack/β-Plancherel concentration or lit match)'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-07-24T16:31:07Z
updated_at: 2026-10-04T15:11:04Z
parent: qou-m6dn
---

Phase 4: prove β=2 maximises E_β[C₂] on [2,∞). Kernel (β=3) sharpened to the COMPACT-INTERVAL statement Cov_β(C₂,ln f)≤0 on [2,3] (β=3 inside monotone window [2,4]) = Cov_β(Σc²,Σln h)≥0. Verified 40dps k≤14. CORRECTION/route-elim (Phase 4b): (1) C₂,Σln h NOT dominance-monotone (conjugation-symmetric, U-shaped); (2) FKG ELIMINATED — f not log-supermodular on dominance (fails k=8, λ=(4,2,1,1),μ=(3,3,2)); (3) Chebyshev ELIMINATED — C₂,Σln h only ~77% comonotone; (4) reduction does NOT sidestep dimension — Σln h=ln k!−ln f still ∉A, only LOWERS the dimension power (f³→ln f covariance). Open: Cov_β(C₂,ln f)≤0 on [2,3] still needs a genuine argument. Audits: 2026-07-24-covariance-kernel-interval-fkg-reframing.md



---

## 2026-09-07 (`qou-igjo`, merged #7046): a FOURTH elimination for the open item

This bean's open item is *"Cov_β(C₂, ln f) ≤ 0 on [2,3] still needs a genuine
argument"*, and `qou-4hq0` names the missing tool as a **non-shifted-symmetric
dimension-functional (ln-dim) expansion**. The most natural candidate for that
tool is to expand `ln f` in the Kerov modes `Σ_p` — they are exactly
uncorrelated under Plancherel with `Var_P(Σ_p) = p(k)_p`, so they are an
orthogonal system to decompose against. **Measured: that expansion will not
terminate.**

Writing `ĉ_p = Cov_P(ln f, Σ_p)/sd_P(Σ_p)`, the share of `Var_P(ln f)` carried
by the low single-cycle modes **decreases** with k:

| k | 12 | 16 | 20 | 24 | 28 | 32 | 40 | 52 |
|---|---|---|---|---|---|---|---|---|
| Σ ĉ_p² / Var(ln f) | 20.8% | 19.4% | 17.5% | 16.3% | 15.4% | 14.7% | 13.6% | 12.4% |

Structural, and the class basis says why: `{√|C_μ| χ^λ(μ)/f^λ}_{μ⊢k}` is a full
**orthonormal basis** of L²(Plancherel_k), and the single-cycle classes are k−1 of
its p(k) directions — a vanishing fraction. So an argument that works mode-by-mode
over single cycles is operating in a shrinking corner of the space, alongside
`sd_P(ln f)` itself growing (empirically ≈ 0.19 ln k over 12 ≤ k ≤ 32 — a fit,
quoted with its range, not a theorem).

Two further items from that PR bearing on this bean:

- `ĉ_p = 0` **exactly** for even p — `ln f` is ω-even and `Σ_p` is ω-odd for even
  p. Decided on integers, 0 violations over 4 ≤ k ≤ 12. Not subsumed by column
  orthogonality, which needs *both* arguments to be characters.
- `ĉ_3` **is** `g'(0)`, and it is **not** monotone and **crosses** −1/4
  (−0.250311 at k=52, −0.250614 at k=56). `qou-f4ye`'s "monotone from below" was
  a coarse-grid artifact; corrected there.

**Not resolving this bean** — the open item stands unchanged. Recording the
elimination so the ln-dim route is not opened on the Kerov modes.

### Note for whoever picks this up

I re-derived this bean's `Cov_β(Σc², Σln h) ≥ 0` reformulation, and `qou-h4fe`'s
pointwise `Cov_{Q_t}(ln f, Σ₃) ≤ 0 on [0,1]` condition, from scratch before
finding either — including setting out to test the comonotonicity that item (3)
here already eliminated at ~77%. **Read `qou-r91v`, `qou-h4fe` and `qou-4hq0`
before opening any new route on this epic;** between them they eliminate exact
evaluation, first-order genus expansion, FKG, Chebyshev, and now Kerov-mode
ln-dim expansion.



### 2026-09-07 correction + two more eliminations (`qou-vilx`)

The Kerov-mode elimination I added above was **under-evidenced**: it read the
single-cycle share only, and the mass of `ln f` is at **d=2** (50–66%), not d=1.
The conclusion stands on the full expansion (d<=2 falls 90.5% -> 69.4%), but more
to the point it is **irrelevant** — `Sigma_3` is ONE orthonormal basis vector, so
`Cov_P(ln f, Sigma_3)` is a single Fourier coefficient and the d>=2 mass is
orthogonal to it. The expansion's convergence has no bearing on this bean's open
item.

Two further routes **eliminated** for the open item, exact on Fractions,
`10 <= k <= 32`: on the sign-split `G(s) = W(E_{nu+}[f^s] - E_{nu-}[f^s])`, both
**first-order** and **increasing-concave** stochastic dominance of `nu-` over
`nu+` fail at **k = 18 and k = 26** (gaps 0.0161, 0.0011) and hold at the other
21 values. The conjecture holds at both. Details on `qou-vilx`.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-07 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Update (Round 92 — lane-cf11)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/NucleonOrderingAndBringAdjointTorsionBrick.lean` with 80-dps probe `computations/probes/nucleon_ordering_and_bring_adjoint_torsion_brick_probe.py` and witness `computations/probes/nucleon-ordering-and-bring-adjoint-torsion-brick.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8348 (`feat/qou-b9cj-q6h7-qd27-qint-r91v-tvok`, HEAD `e0985c4fc3ff765e1935e3343005512aaca69b2b`).
