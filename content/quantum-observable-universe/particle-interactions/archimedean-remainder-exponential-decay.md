**Conjecture (archimedean remainder exponential decay).**

*Fix a free-neutron sector $K \subset H_3(q)$ — the canonical typed
braid word together with its Gröbner–Shirshov filtration — and evaluate
at the substrate parameter $q = q_0$. Let $\mathfrak{Q}_\beta^{(N)}$ be the
depth-$N$ brane-tower truncation of the $\beta$-decay $Q$-value (Form A
or Form B, [`prop:q-beta-spectral-bridge`](#prop:q-beta-spectral-bridge)),
and let $\mathfrak{Q}_\beta^{\mathrm{exact}}$ be the value of the full
spectral decomposition. Then there exist constants $C(K), c(K) > 0$,
depending only on the sector data $K$, such that the truncation
remainder*

$$
  R_N(K) \;:=\; \mathfrak{Q}_\beta^{(N)} - \mathfrak{Q}_\beta^{\mathrm{exact}}
$$

*decays exponentially in the truncation depth:*

$$
  \bigl\lvert R_N(K) \bigr\rvert
  \;\le\;
  C(K)\,e^{-c(K)\,N}
  \qquad (N \ge 0).
$$

## Geometric and exponential phrasings coincide

The exponential form above and the geometric form used by the
categorical precision ladder are the **same** statement. With
$\hbar_q = (q_0 - 1)/q_0$ the Hecke quadratic structure gives the
explicit ceiling

$$
  \bigl\lvert R_N(K) \bigr\rvert
  \;\le\;
  \frac{\hbar_q^{\,2(N+1)}}{1 - \hbar_q^{2}},
$$

which is exactly $C \, e^{-c N}$ with

$$
  c \;=\; -2\ln \hbar_q,
  \qquad
  C \;=\; \frac{\hbar_q^{2}}{1 - \hbar_q^{2}},
$$

since $\hbar_q^{\,2(N+1)} = \hbar_q^{2}\,(\hbar_q^{2})^{N}
= \hbar_q^{2}\,e^{-2N\ln(1/\hbar_q)}$. At $q_0 \approx 1.110$ one has
$\hbar_q^2 \approx 9.82 \times 10^{-3}$, so $c \approx 4.62$ and
$C \approx 9.91 \times 10^{-3}$. The conjecture asserts that *some*
pair $(C(K), c(K))$ controls the operator's own remainder; the
geometric ceiling above is the canonical witness rate, and the true
operator rate may be tighter (larger $c(K)$).

## Remark — what the bound buys

This is the **open conjectural input** that makes the formally infinite
brane-tower product collapse to a finite-precision real prediction. With
the bound in hand, each new rung tightens the prediction by a factor
$\hbar_q^{2} \approx 100^{-1}$, so the truncation order required for a
target relative precision $\varepsilon$ is

$$
  N \;\ge\; \frac{\log_{10}(1/\varepsilon)}{2\log_{10}(1/\hbar_q)} - 1,
$$

the precision-ceiling used by
[`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder).
It supplies the eigenfunction *dampening* principle behind
[`prop:q-beta-spectral-bridge`](#prop:q-beta-spectral-bridge): Form A at
$N = 0$ already lands at $+0.168\%$ residual because the $N = 0$ term sits
inside the structural ceiling, with a $\sim 5.9\times$ headroom against the
observed residual (verified at $50$ dps,
[`c_k_beta_decay_witness.py`](https://github.com/litlfred/qou/blob/main/computations/c_k_beta_decay_witness.py)).
The remainder feeds the per-knot bound of Mechanism 1 in
[`prop:categorical-chain-convergence-mechanisms`](#prop:categorical-chain-convergence-mechanisms),
whose Lean proves the geometric *decay* relation
$c_K\text{Bound}(N+1) = \hbar_q^{2}\cdot c_K\text{Bound}(N)$ and delegates the
*bound itself* to this conjecture.

## Status of the conjecture

The bound is **conjectural**: the substrate identity fixes a *witness*
rate $(C, c)$ that the $N = 0$ residual respects empirically, but a
proof that the operator's spectral tail along the Gröbner–Shirshov
filtration of $K$ decays at this (or any) exponential rate is not
available. Pinning $c(K)$ for the operator is the open lift-formula part
of the brane-tower $z$-Habiro programme. The conjecture is **primary**:
it is not stated conditionally on any other conjecture.
