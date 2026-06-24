**Conjecture ($\tau$ at all orders — dichotomy).**
*Let $\alpha_k := \operatorname{tr}(h^k\text{-curvature})$ denote the
algebraic $h^k$-coefficient of the $Q_8$ crossed-module
multiplicative-integral trace along the Borromean braid, and let
$\kappa_k$ denote the corresponding $h^k$-coefficient of the
Markov-trace expansion of the same braid via the Jones polynomial
$J_{\mathcal{B}_3}(q)$ at $t = q^2$, with the skein parametrization
$h = q - q^{-1}$.
Exactly one of the following holds:*

1. *(**Order-mixing**.) There exists a lower-triangular linear map
   $T \colon \alpha_\bullet \longmapsto \kappa_\bullet$ with
   $T_{k,j} \in \mathbb{R}$, $T_{k,j} = 0$ for $j > k$, $T_{k,k} \neq 0$,
   such that*
   $$
     \kappa_{2k} \;=\; \sum_{j \le k}\; T_{k,j}\,\alpha_{2j}
     \qquad \text{for all } k \ge 1,
   $$
   *and this $T$ is realised by the fibre functor $\tau$ of
   [`conj:geom-universality`](#conj:geom-universality) acting on
   the $h$-graded multiplicative-integral expansion.*

2. *(**Distinct invariants**.) No such $T$ exists at all orders.
   The algebraic and Markov-trace sides measure genuinely different
   categorical invariants of the Borromean braid that happen to share
   only the $h^2$ value (the categorical Euler-characteristic
   $-12 = \dim(V)\cdot\chi(\Sigma_4)$ on the algebraic side,
   $\tfrac{3}{16}$ on the boundary side, related by the
   $h^2$-only coincidence $-64$ that [`rem:geom-bridge-status`](#rem:geom-bridge-status)
   disproves as structural).*

This dichotomy sharpens the open question recorded in
[`rem:geom-bridge-status`](#rem:geom-bridge-status) Link 5. The
$-64$ normalisation (Link 4) has been **disproved as structural**
— at $h^4$, $\alpha_4/\kappa_4 = +7.92 \neq -64$. The conjecture
above is the residual content: the disproof rules out $T$ being a
*constant*, but leaves open whether $T$ is a *non-constant* (i.e.
genuinely order-mixing) linear map, or whether no map exists at all.

## Why a dichotomy

Both hypotheses are categorically meaningful and observationally
testable, and at present neither is settled.

**Why (1) is plausible.**
Yekutieli's non-abelian Stokes theorem
\cite{yekutieli2015} guarantees that the algebraic multiplicative
integral and a $\tau$-image geometric integral *are* connected by a
fibre-functor relation at each order — but the relation is not
required to be order-preserving. A genuine non-trivial $\tau$ can
mix orders if the categorical $h$-grading on the algebraic side
disagrees with the natural $h$-grading on the Markov-trace side
(which it does for the Borromean braid: the algebraic side counts
crossings, the Markov side counts Vassiliev order, and these differ
at $h^4$).

**Why (2) is plausible.**
The algebraic trace counts the crossed-module Euler characteristic
$\dim(V)\cdot\chi(\Sigma_4) = -12$, an integer invariant of the
finite group $Q_8$ acting on Bring's surface. The Markov trace
(skein parametrization $h = q - q^{-1}$) counts the SU$_q(2)$
skein-equivalence class via the Jones polynomial of the same braid. These are invariants of *different
categorical structures* (a $Q_8$-action on a genus-4 surface vs. a
quantum-group skein category), and there is no a priori reason for
them to agree beyond the universal $h^2$-coefficient that records the
algebraic Euler characteristic on both sides via the trivial-strand
expansion.

## Empirical test

The conjecture is sharpened by a finite computation. Define

$$
  M_K \;:=\; \begin{pmatrix}
    \alpha_2 \\ \alpha_4 \\ \alpha_6 \\ \vdots \\ \alpha_{2K}
  \end{pmatrix},
  \qquad
  K_K \;:=\; \begin{pmatrix}
    \kappa_2 \\ \kappa_4 \\ \kappa_6 \\ \vdots \\ \kappa_{2K}
  \end{pmatrix}.
$$

For each $K \ge 2$, ask: does the linear system $K_K = T\,M_K$ admit a
lower-triangular real solution $T$?

**Result (computed; refines the test).**  The $h^6,\,h^8$ extension was
run in
[`tau_all_orders_h6_empirical.py`](../../../computations/probes/tau_all_orders_h6_empirical.py)
(witness `tau-all-orders-empirical-bridge.witness.json`). Two facts
emerged that **sharpen the conjecture and correct the naive test**:

1. **The algebraic side is degree-4 in $h$.**  Although the Borromean
   braid has six crossings, the order-six multiplicative-integral term
   (the single full product, traced) **vanishes**: $\alpha_6 = 0$, and
   $\alpha_{2k} = 0$ for all $k \ge 3$.  So $\alpha$ carries nonzero
   data at *only* $h^2,\,h^4$ — the two integers $-12$ and $-6$ —
   whereas the Markov series $\kappa$ is infinite
   ($\kappa_6 = -0.2024\ldots,\ \kappa_8 = 0.00967\ldots \ne 0$).
   This $2$-versus-$\infty$ asymmetry is concrete structural evidence
   that the two sides are different categorical invariants.

2. **The number-level fit is non-discriminating.**  At a fixed
   substrate $q_0$ both $\alpha_\bullet$ and $\kappa_\bullet$ are
   *constant* (the $Q_8$ rep is $q$-independent; the Jones Taylor
   coefficients are pure numbers).  The diagonal fit
   $T_{k,k} = \kappa_{2k}/\alpha_{2k}$ fails at $k = 3$ (since
   $\alpha_6 = 0$), but a **non-diagonal** lower-triangular fit still
   exists — row $k$ reads
   $\kappa_{2k} = T_{k,1}\alpha_2 + T_{k,2}\alpha_4$ (one equation, two
   free unknowns, since the higher $\alpha$ vanish), always solvable.
   Hence hypothesis (1) "$\exists$ lower-triangular $T$" is *trivially*
   inhabited at the number level, and the naive fit cannot distinguish
   (1) from (2).

**Consequence for the formalisation.**  The genuine open content is
therefore **not** "does a lower-triangular $T$ exist" (it does,
vacuously).  Note that even a *single* $T$ holding at all orders
simultaneously — which is what the Lean
$\mathrm{TauOrderMixingMap}.\mathrm{bridgeAtOrder}\colon \forall k$
already requires — is **still** trivially inhabited, because each row
$k$ of $T$ carries independent free entries $T_{k,1},\dots,T_{k,k}$ and
is solved on its own.  The constraint that would make the dichotomy
non-trivial is a **finite-support / banded** structure: $T_{k,j} =
f(k-j)$ for a fixed finitely-supported kernel $f$ (a *convolution*),
reflecting a single categorical operator rather than a per-row solve.
A genuine fibre-functor realisation of $\tau$ would supply exactly such
a kernel.  This banded-kernel constraint is now formalised as the Lean
class $\mathrm{TauBandedKernelMap}$ (kernel $f$, finite `bandWidth`,
`leadingNonzero` $f(0) \neq 0$, and the convolution `bridge`
$\kappa_k = \sum_{j \le k} f(k-j)\,\alpha_j$ at every order with the
*same* $f$); the refined dichotomy `tau_all_orders_bridge` is stated
against it, while the naive arbitrary-$T$ hypothesis (1) is retained as
`tau_order_mixing_naive_hyp1` (a single existence claim, not a
dichotomy) with its trivially-inhabited caveat. The
$h^2$ anchor $f(0) = T_{1,1} = -1/64$ is fixed regardless, and the
disproof shows the band-width-0 (constant) kernel already fails at
$h^4$ — so the open question is whether a *wider* finite band closes
the bridge.

## What does *not* settle the conjecture

- **The proved $-12 = \dim(V)\cdot\chi(\Sigma_4)$ identity** of
  [`prop:crossed-module-euler-characteristic`](#prop:crossed-module-euler-characteristic).
  This is the algebraic endpoint of the chain, not a statement about
  $\tau$.
- **The proved Vol$(\mathcal{B}_3) = 8G$ + bridge factor $2G/3$** of
  [`rem:geom-bridge-status`](#rem:geom-bridge-status) Links 2–3.
  These are the geometric face, also independent of $\tau$.
- **The disproved $-64$ normalisation** ([`rem:geom-bridge-status`](#rem:geom-bridge-status)
  Link 4). This rules out the *constant* form of $\tau$; both
  hypotheses (1) and (2) above are consistent with that disproof.

The conjecture is therefore the genuine remaining mathematical
question — not numerology recovery, not a fit, and not a re-derivation
of any proved identity.

## Lean structure

The Lean file [`tau-all-orders-bridge.lean`](tau-all-orders-bridge.lean) axiomatises hypothesis
(1) as a class `TauOrderMixingMap` carrying the coefficients $T_{k,j}$
and the bridge equation. Downstream consequences (any concrete
prediction following from the existence of such a $T$) can then be
stated as conditional theorems with `[TauOrderMixingMap]` as a class
hypothesis, in the §3b-cond pattern.

A separate class `TauDistinctInvariants` records hypothesis (2);
the disjunction `TauOrderMixingMap ∨ TauDistinctInvariants` is the
conjecture proper. Neither class has an instance — that is the
honest reflection of the open status.
