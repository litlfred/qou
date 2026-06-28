## Proof

*Proof (Lean: `tau_M_asymptotic_rep_theory`).* The factorisation defines
$F_\lambda$; the substance is the parity and the proved rungs.

**Parity (even in $\hbar_q$).** Markov cyclicity $\tau_M(xy) = \tau_M(yx)$ with
the bar involution $q \leftrightarrow q^{-1}$ forces
$F_\lambda(\hbar_q) = F_\lambda(-\hbar_q)$: the single-wrap character
symmetrises over the two eigenphases of $\rho_\lambda$ into
$\mathrm{tr}\,\rho_\lambda(\beta)\cdot\cos\alpha$
([`prop:hoefsmit-V21-cos-symmetrization`](#prop:hoefsmit-V21-cos-symmetrization),
[`prop:q-beta-cos-resummation`](#prop:q-beta-cos-resummation)), and
$\cos$ is even; the rung exponents $u_\lambda^k = b_\lambda^k\hbar_q^{2k}$ are
even in $\hbar_q$ by construction. The bar-parity alternation of the rung
coefficients ($\overline{c_k} = (-1)^k c_k$, bar-even seed $c_2 = -1$) is the
sorry-free `esymm_bar_parity` of
[`prop:q-beta-c-k-recursion-from-habiro-q-difference`](#prop:q-beta-c-k-recursion-from-habiro-q-difference).
$\square$ (parity)

**Baseline $c_0 = 0$.** At $q = 1$, $\hbar_q = 0$ and
$\rho_\lambda(\sigma_i) \mapsto$ the symmetric-group permutation matrix, so
$\tau_M^{V_\lambda} = \mathrm{Tr}\,\rho_\lambda(\beta)$ and $F_\lambda(0) = 1$,
i.e. $c_0 = 0$. $\square$

**One-dimensional irreps.** For $V_{(n)}$ (trivial) and $V_{(1^n)}$ (sign),
$\rho_\lambda(\sigma_i)$ is a scalar, the off-diagonal coupling vanishes
($b_\lambda = 0$, hence $u_\lambda = 0$), and the Markov-symmetrised character
equals the bare character; thus $F_\lambda \equiv 1$. The 1-d closed forms are
[`prop:hecke-1d-irrep-closed-form-character`](#prop:hecke-1d-irrep-closed-form-character).
$\square$

**$N=1$ envelope (coupling $b$), $V_{(2,1)}$.** The first non-trivial irrep is
the 2-d $V_{(2,1)}$ of $H_3$. Its single $\tilde f_1$ Kashiwara edge carries
weight $b_\lambda = b$, giving the eigenphase shift $-b\,\hbar_q^2/2$ (the
$\tilde f_1$ matrix element in the seminormal basis times $\hbar_q^2/2$),
resummed into the $\cos(\alpha - b\hbar_q^2/2)$ envelope. This is the $N=1$
result of
[`prop:hoefsmit-V21-cos-symmetrization`](#prop:hoefsmit-V21-cos-symmetrization).
$\square$

**Second rung (production wire), $V_{(2,1)}$: $c_2 = -1$.** The first product
rung is $(1 + c_2 u^2)$ with $u = b\hbar_q^2$. The seed $c_2 = -1$ is proved
categorically (the bar-even constraint, PR #1602), giving the factor
$(1 - u^2) = (1 - b^2\hbar_q^4)$ — exactly the second-order correction the
production neutron consumes
($\mathfrak{Q}_\beta = \mathfrak{Q}_\beta^{(N=1)}\cdot(1 - b^2\hbar_q^4)$,
`derived_masses.q_beta_kashiwara_n2_mev`). One coupling $b$ thus drives both the
$N=1$ envelope and the proved second rung. $\square$

The proof determines $c_0$, the 1-d triviality, the $N=1$ coupling $b$, and the
proved seed $c_2 = -1$, together with the $\hbar_q$-parity. The rungs
$c_k^{(\lambda)}$ for $k \geq 3$ are *generated* by the proved recursion of
[`prop:q-beta-c-k-recursion-from-habiro-q-difference`](#prop:q-beta-c-k-recursion-from-habiro-q-difference)
once its kernel $R(q,\xi)$ is fixed; that kernel is the open keystone (see
below). $\blacksquare$
