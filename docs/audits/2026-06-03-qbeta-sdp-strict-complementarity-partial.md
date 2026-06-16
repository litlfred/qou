# Q_β via q-rational SDP strict-complementarity — honest PARTIAL

**Date**: 2026-06-03
**Branch / PR**: `claude/qbeta-sdp-strict-complementarity-2026-06-03` / PR #1752
**Script**: [`computations/qbeta/qbeta_symbolic_sdp_strict_complementarity.py`](../../computations/qbeta/qbeta_symbolic_sdp_strict_complementarity.py)
**Witness**: `computations/qbeta/qbeta-symbolic-sdp-strict-complementarity.witness.json`
**Sibling**: PR #1739 (`qbeta_symbolic_tbeta_min_l2.py` — the symbolic T_β shape this reuses)

## Goal

Replace the archimedean, CODATA-anchored **min-L2** selection of the β-decay
knot operator `T_β` with a **q-rational SDP strict-complementarity** selection,
to test whether the CODATA scalar `S = Q_β(q₀)/E_0(q₀)` cancels from the `c_k`
directions — which would enable a Q_β prediction independent of CODATA Q_β.

The production "knot-operator SDP" (`qbeta_decay_sdp_solver.py`) is *not* an SDP:
it is the min-L2 closed form `x* = (n_target/(t·t))·t` with `n_target := Q_β/E_0`
(lines 78, 94). The net target IS the CODATA Q_β — so the production selection
is circular and cannot *predict* Q_β.

## Method

Built the q-rational operator-selection inputs over the 6-element NF basis
`(γ, σ₀, σ₁, L₊, L₋, e⁻)` of `H_3(q)`:

- cost `t_i(q) = τ_M(b_i)` (Markov trace; `t_γ = 1` exactly),
- Frobenius Gram `G_{ij}(q) = τ_M(b_i b_j)`,

from Hoefsmit seminormal blocks + Schur-element `y_λ(q)` (same source as #1739).
Cross-check `t_i(q) ≡ #1739 A_i(q)`: **YES**. Solved the genuine
`solve_operator_selection_lp(t, G, n_target)` (primal + dual emitted per the
LP/SDP first-class-infra rule), at `n_target = 1` (q-rational unit net) and at a
CODATA-shaped value.

## Findings

1. **The Frobenius Gram is INDEFINITE.** Eigenvalues at q₀:
   `[-0.855, +0.102, +0.855, +0.855, +0.855, +3.477]`. The Markov-trace pairing
   has signature; the cone `{Gx ≥ 0}` is not the PSD cone. Consequently the LP
   **min-trace objective is degenerate** — the optimum `t·x` is driven to ≈ 0,
   not to the physical `T_β`. **The operator-selection LP objective does not
   single out the β-decay operator.** This is precisely why the production rule
   uses the strictly-convex min-‖x‖² selection — the LP and the Q_β selection are
   *different programs*.

2. **The selector DIRECTION is S-independent and q-rational.** Strict
   complementarity fixes a unique active set (`active_set = [0]`, the identity
   channel; `y_star = [1,0,0,0,0,0]`; strong-duality gap ≈ 1e-14). The normalized
   selector is scale-invariant: `max|x*(n_a)/n_a − x*(n_b)/n_b| = 1.4e-14`. So the
   dimensionless precision-ladder factors `(1 + c_k u^k)` — ratios of the
   frozen-direction q-shape — **are S-independent**.

3. **The Q_β SCALE is supplied CODATA-Q_β-free by Q_A to 0.17%.** The q-rational
   Form-A baseline `Q_A(q₀) = m_e·|q²−2q−1|(q+1)/(2q³)` gives `0.78365 MeV` vs
   CODATA `Q_β = 0.78233 MeV` — **0.168 %** error with **zero** CODATA-Q_β input.
   The S-independent c_k ladder refines this.

## Verdict — honest PARTIAL (not a closure, not a fit)

- **CODATA-Q_β-free**: the c_k *directions* (S-independent, q-rational) and the
  Q_β *scale* to ~0.17 % (via the q-rational `Q_A`).
- **NOT CODATA-Q_β-free**: the sub-ppb (7.8 ppb L2) absolute normalisation of the
  c_k ladder. The SDP fixes the **shape** of `T_β`, not its **trace magnitude**;
  the production rule pins that magnitude via `n_target = Q_β/E_0`, which is the
  CODATA Q_β.

**No CAL-4 fit was introduced** — the direction is forced by complementarity, the
scale by the substrate Q_A. The honest conclusion: the SDP strict-complementarity
route **does not** by itself make Q_β CODATA-independent at the L2 target. It
recovers the 0.17 % Form-A result CODATA-free and confirms the c_k directions are
S-independent, but the sub-ppb normalisation remains pinned to CODATA Q_β.

## Why S does not fully cancel (one-line)

The operator-selection program has two degrees of freedom — *direction* and
*scale*. Strict complementarity (q-rational `t, G`) fixes the **direction**;
the affine net-constraint `Σx_i = n_target` supplies the **scale**, and the only
trace-magnitude available for `n_target` is `τ_M(T_β) = Q_β/E_0` itself. The
substrate gives the scale only to Form-A accuracy (`Q_A`, 0.17 %), not to 7.8 ppb.
