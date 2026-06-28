> **SUPERSEDED-$\rho_q$ note .** Any use of the
> scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the
> structurally-wrong leading-order ansatz per
> [`mass-endomorphism-tower.md` §SUPERSEDED](mass-endomorphism-tower.md);
> the canonical replacement is the operator-valued $A^\lambda_{\mu, \nu}(I)$
> graded expansion [`prop:rho-k-graded-expansion`](rho-k-graded-expansion.md).
> Full purge tracking: [`docs/audits/-superseded-rho-q-purge.md`](../../../docs/audits/-superseded-rho-q-purge.md).

The Markov chain
([Hecke transition operator](#prop:hecke-markov-transition)),
the knot-theoretic operations on a closed braid, and the
partition $\lambda \vdash n$ labelling an irrep of $H_n(R, q)$
are tied together by Wedderburn semisimplicity. This remark
records the $\lambda$-block decomposition and its consequence for
the Markov chain; the companion remarks
([knot operations split into $\lambda$-preserving and
$\lambda$-changing moves](#rem:markov-lambda-knot-operations-moves))
and ([Jones polynomial as a Plancherel sum over
$\lambda$](#rem:markov-lambda-jones-plancherel)) carry the other two
ties.

## $\lambda$-block decomposition (Wedderburn)

Semisimplicity of $H_n(R, q)$ (generic $q$) gives a decomposition

$$
  H_n(R, q)
  \;\cong\;
  \bigoplus_{\lambda \vdash n}
    \mathrm{End}_R(V_\lambda),
  \qquad
  \dim V_\lambda = d_\lambda = |\mathrm{SYT}(\lambda)|,
$$

The amplitude matrix of any braid $\beta \in B_n$ splits

$$
  \rho_q(\beta)
  \;=\;
  \bigoplus_{\lambda \vdash n} \rho^\lambda_q(\beta).
$$

**Consequence for the Markov chain.** Each $\lambda$ is a closed
sector with its own discrete state space $\mathrm{SYT}(\lambda)$
([SYT paths on the Young graph](#rem:hecke-markov-interpretation)).
Hecke-generator amplitudes
$\rho^\lambda_q(\sigma_i)$ never mix irreps: the chain on the
union of SYTs (over all shapes $\lambda \vdash n$) is a direct
sum of independent $\lambda$-chains.

**Block-diagonality.**  Hecke generators act within a single
$\lambda$-sector; the chain decomposes as $\bigoplus_\lambda$
independent SYT-chains. Which knot operations respect these blocks,
and how the Jones polynomial sums over them, are taken up in the
companion remarks.
