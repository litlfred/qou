# tr_M(D) reconciliation (post-#472, #473, #475 → corrected by pr-442)

After PR #457 merged, two PRs landed on main that *appeared* to resolve the
tr_M-normalization ambiguity:

- **PR #472** (content): [`prop:habiro-residue-sum-equivalence`](../content/quantum-observable-universe/braids-and-knots/habiro-residue-sum-equivalence.md) — cross-validates `tr_M(D, q_0)` between the polynomial-ring path and the residue-spectral-sum path at relative tolerance $\leq 10^{-9}$.
- **PR #473** (computation registry): `D-tr-M-q0.derivation.json` — registered `tr_M(D, q_0) = 0.17743692421543206` as the "canonical" value via an 8-step derivation chain.

## Update (pr-442): the registry value is τ_SW, not the canonical τ_M

[`prop:markov-trace-frobenius-selection`](https://github.com/litlfred/qou/blob/25a204efaf61ceba7c11f4f8861c533b6d37f0cf/content/quantum-observable-universe/braids-and-knots/markov-trace-frobenius-selection.md) (proven at commit [`25a204e`](https://github.com/litlfred/qou/commit/25a204efaf61ceba7c11f4f8861c533b6d37f0cf), pending merge as part of pr-442) shows the QOU mass formula's Frobenius co-Casimir construction
$C_{\dim_q} = \sum_\lambda [\dim_q(\lambda)\cdot \tau(p_\lambda)]^{-1} p_\lambda$
requires $\tau$ **non-degenerate on every Wedderburn block**. Two
distinct Frobenius pairings on $H_n(q)$ compete:

| name | weights $w_\lambda$ | non-degenerate? | $\tau(D, q_0)$ |
|---|---|:---:|---:|
| Jones-Markov $\tau_M$ | Wenzl-bridge $y_\lambda$ (Markov-axiom solve) | ✓ | **0.288326** |
| Schur-Weyl $\tau_{\mathrm{SW}}$ | $s_\lambda(q,q^{-1})\cdot d_\lambda / H_q(\lambda)$ | × kernel = height > 2 | 0.177437 |

The selection theorem proves QOU's mass formula picks $\tau_M$. PR #472's
polynomial path and PR #473's registry both compute $\tau_{\mathrm{SW}}$
(via the Schur-Weyl weight formula); PR #472's "equivalence" is between
two pipelines computing the same $\tau_{\mathrm{SW}}$, not a confirmation
of $\tau_M$.

| Trace | $\tau(p)$ | $\tau(n)$ | $\tau(D)$ |
|------------|--------:|--------:|--------:|
| $\tau_M$ (Wenzl-bridge / Markov-axiom) — `atomic-tr-m-wenzl-bridge.witness.json` | 0.998367 | 0.998367 | **0.288326** |
| $\tau_{\mathrm{SW}}$ — `*-tr-M-q0.derivation.json` registry (mislabeled "tr_M") | 2.122582 | 1.589393 | 0.177437 |

The from-scratch chain on this branch
([`folio-assistant/computations/from_scratch/wedderburn_markov.py`](../folio-assistant/computations/from_scratch/wedderburn_markov.py))
independently derives $\tau_M(D, q_0) = 0.288326$ from the Markov axioms
$\tau(1)=1$, $\tau(\sigma_i)=z$, $\tau(xy)=\tau(yx)$, $\tau(x\sigma_n)=z\tau(x)$
— matching the Wenzl-bridge witness bit-exactly.

## D walkthrough — recomputed under canonical $\tau_M$

[`probe_multi_term_tau_M_corrected.py`](../folio-assistant/computations/probe_multi_term_tau_M_corrected.py)
re-runs the multi-term assembly with $\tau_M$ in T1
(everything else unchanged — T2+T3+T4+T5 don't depend on the trace
functional):

| Variant | $\tau_M$ B_pred | $\tau_{\mathrm{SW}}$ B_pred | $\tau_M$ residual |
|---------|---------------:|---------------:|---------:|
| T1 alone ($m_e\rho|\tau|$) | 0.1473 | 0.0907 | $-93.4\%$ |
| T1 + T4 Frobenius | 1.4234 | 1.3668 | $-36.0\%$ |
| T1+T2+T3 (algebraic Vol_q tower) | 2.1027 | 2.0461 | $-5.5\%$ |
| T1+T2+T3+T4+T5 (naive sum) | $-2.2526$ | $-2.3092$ | sign-flipped (T5 dominates) |

The shift from $\tau_{\mathrm{SW}}$ → $\tau_M$ moves D's T1 by
$+0.057\,\text{MeV}$ — small relative to the AME binding, but
structurally important: the chain now uses the
Frobenius-non-degenerate functional that the mass formula
requires.

## Conclusions

1. **τ_SW vs τ_M is a structural correction, not a numerical fitting**:
   τ_SW is degenerate on height>2 blocks, so $C_{\dim_q}$ isn't even
   well-defined under it. The selection theorem rules τ_SW out
   structurally.
2. **The naive multi-term sum still doesn't yield AME binding** — this
   confirms the post-PR-475 finding that "terms are alternatives, not
   additive". Switching trace conventions doesn't change that.
3. **Brane-tower regularization** still gates further progress. The
   algebraic Vol_q^tower form is finite and physically scaled
   ($O(1)$ per atom); the Φ_q (Kashaev) form is finite-but-pathological
   near the substrate boundary. Per
   [`prop:mass-endomorphism-tower`](../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.md)
   the algebraic form is the canonical statement.

## Open work carried forward

- **Registry relabel**: rename `D-tr-M-q0.derivation.json` →
  `D-tau-SW-q0.derivation.json` (keep the chain — it documents
  $\tau_{\mathrm{SW}}$ correctly) and add new `D-tau-M-q0.derivation.json`
  for the canonical $\tau_M$ chain (already done on pr-442). Same for
  $n,p$.
- **Selection-theorem block on main**: pr-442's
  `prop:markov-trace-frobenius-selection` (the Lean proof + .md) is
  not yet on main. Once merged, every downstream chain referencing the
  "tr_M" registry needs an `interprets`/`uses` link to it.
- **Brane-tower regularization** is the remaining theory gap and is
  independent of the trace convention.
