# tr_M(D) reconciliation (post-#472, post-#473)

After PR #457 merged, two PRs landed on main that resolved the
tr_M-normalization ambiguity I flagged in
`docs/derivation-tracking-methodology.md`:

- **PR #472** (content): [`prop:habiro-residue-sum-equivalence`](../content/quantum-observable-universe/braids-and-knots/habiro-residue-sum-equivalence.md) — cross-validates `tr_M(D, q_0)` between the polynomial-ring path and the residue-spectral-sum path at relative tolerance $\leq 10^{-9}$.
- **PR #473** (computation registry): `D-tr-M-q0.derivation.json` — registers `tr_M(D, q_0) = 0.17743692421543206` as the canonical value via an 8-step derivation chain from the 7 first-principles entrypoints.

| Convention | tr_M(p) | tr_M(n) | tr_M(D) |
|------------|--------:|--------:|--------:|
| **Canonical (post-#472, #473)** — `markov-substrate-realization.witness.json` | 2.122582 | 1.589393 | **0.177437** |
| `atomic-tr-m-mpfr-50dps.witness.json` (used by my round 4–7 probes) | 1.065306 | 0.923233 | 0.388286 |

The two are off by factor ~2 — different 3-strand-folding conventions inside Wenzl–Schur. The canonical convention (tr_M(D) = 0.177) is the one endorsed by the new equivalence theorem.

## D walkthrough — recomputed under canonical tr_M

| Variant | B_pred (MeV) | residual |
|---------|-------------:|---------:|
| S1: $m_e\rho\|tr_M\|$ | 0.0907 | **−95.9 %** (was −91.1 % with old tr_M) |
| S2: + T4 Frobenius $m_e(2+1/[2]_q)$ | 1.3668 | **−38.6 %** (was −33.7 %) |
| S3–5: + T2+T3 raw | 866,885 | divergent (Φ_q pole at z=1) |

Conclusions unchanged from my pre-merge analysis:
1. The brane-tower terms diverge under the canonical convention as before — Φ_q's pole at z=1 is the issue, not the tr_M normalization.
2. T1 + T4 closes most of the gap (~60 percentage points); the remaining ~40 % is what regularized T2+T3+T5+T6 must supply.
3. The numerical −95.9 % single-term residual under canonical tr_M is **stronger evidence** that the single-term formula is insufficient on its own, not an indictment of the chain.

## Open work carried forward (pre-merge → post-merge)

- **Brane-tower regularization** — the divergent Φ_q is a paper-level theory issue. PR #472's Habiro pipeline extension to deuteron didn't address it. Next investigation: does the Habiro tail expansion regularize the brane-tower contribution?
- **Round-8 atomic bond topology** — paused as before; still gated on the regularization question.
