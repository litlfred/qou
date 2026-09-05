*The Markov trace under convention D is a* **state sum**. *On $H_2$ the two
Wedderburn blocks $(2)$ and $(1,1)$ carry Wenzl weights*

$$
  w_+ = \frac{[3]_q}{[3]_q + 1} = 0.752702113\ldots, \qquad
  w_- = \frac{1}{[3]_q + 1} = 0.247297887\ldots, \qquad
  w_+ + w_- = 1
$$

*(the normalisation is exact: `wPlus_add_wMinus` in `QOU.Mass.ChainTraceFactor`),
so $w$ is a genuine probability measure on the blocks, on which $\sigma$ acts by
the block eigenvalues $q$ and $-q^{-1}$. The interface trace is therefore an
expectation,*

$$
  \mathrm{tr}_2(\sigma + d) \;=\; \mathbb{E}_w[\lambda + d] \;=\; z + d,
  \qquad z = \frac{q^3}{q^2+1},
$$

*and since the canonical chain's Markov trace is exactly the product of these
factors ([the chain factorisation](#rem:canonical-trace-factorises-over-chain),
measured to $\sim 10^{-59}$), the quantity the binding arc computes is*

$$
  L \;=\; \log\frac{Z_{\text{free}}}{Z_{\text{bonded}}}
    \;=\; \sum_{\text{interfaces}} -\log \mathbb{E}_w[\lambda + d_i],
$$

***a free-energy difference in the standard sense*** *— dimensionless, in units
of $kT$, per-interface additive, and positive because every factor $z + d$ lies
in $(0,1)$ at $q_0$.*

## This part is settled

$L$ is exact, canonical to convention D, and correct wherever it appears. The
three constants are closed forms:

| bond | $d$ | $z + d$ | $L = -\log(z+d)$ |
|---|---|---|---|
| $pp$ | $0$ | $0.612688037146$ | $0.489899384255$ |
| $nn$ | $-h$ | $0.403627738351$ | $0.907262265533$ |
| $pn$ | $d_{pn}$ | $0.508229789377$ | $0.676821592386$ |

with $L_{pp} = -\log z$, $L_{nn} = \log\bigl(q(q^2+1)\bigr)$ and
$L_{pp} + L_{nn} = 2\log[2]_q$ (all in `QOU.Mass.ChainTraceFactor`, sorry-free).

One caveat belongs with the identification: the observable is **signed**, since
the $(1,1)$ eigenvalue $-q^{-1}$ is negative. So this is the free energy of a
signed observable over a quasi-probability, not of a positive one, and the sign
is exactly the $\sigma$ / $\sigma^{-1}$ split — the $p$/$n$ distinction itself.
Convexity intuitions imported from ordinary statistical mechanics need checking
rather than assuming.

## The separate claim, which is open

**That $B = \alpha L$ is the nuclear binding energy is an interpretation, not a
result.** It is recorded here as open, with the evidence that bears on it:

- **At $A = 2$, where no ordering or arrangement convention is in play, the
  ordering is wrong.** $L_{pp} < L_{pn} < L_{nn}$ is forced for every $q$ and
  every $\delta \in (0,2)$, because the $pn$ letter is by construction the
  convex combination of the $pp$ and $nn$ letters
  ([why](#rem:pn-bond-cannot-be-extremal)). So the model ranks the unbound
  dineutron above the bound deuteron. The absence of a spin channel explains
  why a spinless constant cannot separate bound from unbound; it does not
  explain the order.
- **No sum over per-bond constants can have a valley of stability.** $B$ is then
  linear in $Z$ for the chain and convex in $Z$ for all pairs, so its maximum
  sits at an endpoint: the most bound isobar is always the most neutron-rich.
- **The chain delivers $31\,\%$ of $^4$He** ($8.68$ MeV against
  $B_{\mathrm{AME}} = 28.2957$), and no interface offset can close the gap —
  the required offset is $2.43\times$ more negative than the most negative
  letter the algebra has.

None of that shows $L$ is the wrong quantity. It shows that the step from this
free energy to an energy in MeV is not established, and the corpus's own
working binding route is a different one (the Layer-1 canonical
$|\mathrm{tr}_M(q_0)|$ table, which reaches $-0.16\,\%$ to $+5.87\,\%$ on
$\mathrm{D}$, $\mathrm{T}$, $^3$He and $^4$He).

## Scope

Nothing is retracted and no number moves. Every computation of $L$ in the
corpus stands as a correct free-energy difference; only the sentence "and this
is the binding energy" is marked open. The all-pairs extension is a separate
matter and is retired for a separate reason: its bond multiset does not
determine a braid word at all
([the ordering ambiguity](#prop:canonical-closure-torus-chain)).
