# tr_M(D) reconciliation (post-#472, #473, #475, #447)

After PR #457 merged, two PRs landed on main that *appeared* to resolve the
tr_M-normalization ambiguity:

- **PR #472** (content): [`prop:habiro-residue-sum-equivalence`](../content/quantum-observable-universe/braids-and-knots/habiro-residue-sum-equivalence.md) — cross-validates `tr_M(D, q_0)` between the polynomial-ring path and the residue-spectral-sum path at relative tolerance $\leq 10^{-9}$.
- **PR #473** (computation registry): `D-tr-M-q0.derivation.json` — registered $0.177437$ as the "canonical" value via an 8-step derivation chain.

## Correction (PR #447, now merged): the registry value is τ_SW, not τ_M

[`prop:markov-trace-frobenius-selection`](../content/quantum-observable-universe/braids-and-knots/markov-trace-frobenius-selection.md)
(merged via PR #447) shows the QOU mass formula's Frobenius co-Casimir construction
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
| $\tau_M$ (Wenzl-bridge / Markov-axiom) — direct from atomic braid | **+1.733851** | **+1.405980** | **+0.288326** (SDP-canonical) / 0.336821 (hand-built H_6) |
| $\tau_{\mathrm{SW}}$ — `*-tr-M-q0.derivation.json` registry (mislabeled "tr_M") | 2.122582 | 1.589393 | 0.177437 |

`atomic-tr-m-wenzl-bridge.witness.json` records 0.998367 for p, n, ³He
— bit-exact identical, with identical per-block $\mathrm{Tr}(\rho_\lambda) = (1, 1.994, 1)$
— a witness-generation bug surfaced by PR #487's audit. Direct
re-computation via [`atomic_braid_to_crossings`](../computations/hecke/hecke_character_symbolic.py)
+ [`wenzl_y_lambda`](../computations/from_scratch/wedderburn_markov.py)
gives the parity-distinguishing values shown.

For D, the SDP-canonical 6-strand atom braid reduced to H_3 gives
$\tau_M = 0.288326$ (validated bit-exactly by the from-scratch
chain on this branch and matching `atomic-tr-m-wenzl-bridge`'s
deuteron entry which IS correct). The "hand-built H_6 atom" braid
registered by PR #447's [`D-tau-M-q0.derivation.json`](../computations/D-tau-M-q0.derivation.json)
chain gives $0.336821$ — same trace functional ($\tau_M$), different
braid representative.

## D walkthrough — recomputed under canonical $\tau_M$

[`probe_multi_term_tau_M_corrected.py`](../computations/probe_multi_term_tau_M_corrected.py)
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

## Wenzl-bridge witness audit (PR #487 follow-up)

Direct re-computation of τ_M for free p, n via the canonical
[`atomic_braid_to_crossings`](../computations/hecke/hecke_character_symbolic.py)
+ [`wenzl_y_lambda`](../computations/from_scratch/wedderburn_markov.py)
flagged a **witness-generation bug** in
[`atomic-tr-m-wenzl-bridge.witness.json`](../computations/atomic-tr-m-wenzl-bridge.witness.json):

  Witness's proton, neutron, ³He entries all share bit-exact
  $\tau_M = 0.998366751$. Per-block breakdown shows
  $\mathrm{Tr}(\rho_\lambda) = (1, 1.994, 1)$ identically across the
  three atoms — strongly suggesting the `dump-block-matrices` Rust
  binary used the same trivial / single-nucleon braid for all three.

[`probe_wenzl_bridge_witness_audit.py`](../computations/probe_wenzl_bridge_witness_audit.py)
documents the bug and computes corrected free-atom values:

| atom | witness | direct τ_M (3-strand free) | match? |
|------|--------:|---------------------------:|:------:|
| proton | 0.998367 | **+1.733851** | ✗ |
| neutron | 0.998367 | **+1.405980** | ✗ |
| deuteron | 0.288326 | (needs H_5) — from-scratch chain agrees | ✓ |
| tritium | 0.012889 | (needs H_8) — from-scratch chain agrees | ✓ |
| ³He | 0.998367 | (needs H_8) — value unverified | ✗ pending |

Round-6 trace-deficit hypothesis re-evaluated under the
audit-corrected p, n values
([`probe_round6_tau_M_canonical.py`](../computations/probe_round6_tau_M_canonical.py)):

| atom | deficit | $E_0 = m_p/\|\tau_M(p)\|$ | $E_0 = m_e$ |
|------|--------:|---------------------------:|------------:|
| D | 2.852 | 1543.09 MeV (+69266%) | **1.457 MeV (−34.5%)** |
| T | 4.533 | 2452.99 MeV (+28821%) | 2.316 MeV (−72.7%) |
| ³He | 3.875 | 2097.12 MeV (+27072%) | 1.980 MeV (−74.3%) |

Under $E_0 = m_e$ with the audit-corrected p, n, the trace-deficit
hypothesis gets D within **−34.5 %** of AME — substantially better
than the −60 % seen under the buggy witness, but still not a
canonical match. The proton-calibration prefactor ($\approx 540$
MeV/τ-unit at the corrected p value) gives mass-scale errors
(four orders of magnitude high) under either the buggy or
corrected convention. The 938-MeV nucleon rest mass continues to
require physics outside the categorical-binding chain.

³He remains pending — needs H_8 Wenzl y_λ + 33-crossing character
evaluation, deferred to a future PR alongside the other H_n>5
extensions on PR #484.

## Open work carried forward

- **Registry relabel**: rename `D-tr-M-q0.derivation.json` →
  `D-tau-SW-q0.derivation.json` (keep the chain — it documents
  $\tau_{\mathrm{SW}}$ correctly) and add new `D-tau-M-q0.derivation.json`
  for the canonical $\tau_M$ chain (already done on pr-442). Same for
  $n,p$.
- **Cross-link the selection theorem from downstream chains**: now
  that `prop:markov-trace-frobenius-selection` is on main (PR #447),
  every downstream chain referencing the "tr_M" registry should add
  an `interprets`/`uses` link to it. Most chains were authored before
  the selection theorem landed and don't yet reference it.
- **Brane-tower regularization** is the remaining theory gap and is
  independent of the trace convention.
