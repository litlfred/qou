*The [chain form](#prop:canonical-closure-torus-chain) has an algebraic
consequence that is stronger than the topological one. Write the canonical
Hecke word as $\prod_i p_i(\sigma_i)$, one polynomial per generator in Coxeter
order -- the averaged letters sit inside the power of their own generator, so
this needs no branch to be chosen. Then the normalised Markov trace on
$H_{3A}$ is the product of two-strand traces,*

$$
  \mathrm{tr}_M\Bigl(\prod_i p_i(\sigma_i)\Bigr)
  \;=\;
  \prod_i \bigl[\,w_+\,p_i(q) + w_-\,p_i(-q^{-1})\,\bigr],
  \qquad
  w_+ = \frac{[3]_q}{[3]_q+1},\quad w_- = \frac{1}{[3]_q+1},
$$

*because a closed braid whose word is a product of sub-words on strand sets
overlapping in one strand is a connected sum, and the Markov trace -- like
every multiplicative link invariant -- is multiplicative under connected sum,
not only under the split union of
[the KS shortcut](#rem:ks-multiplicativity-via-markov). Each interface
generator carries the single letter $\sigma + d$, whose two-strand trace is*

$$
  w_+(q + d) + w_-(-q^{-1} + d) \;=\; z + d,
  \qquad z = \frac{q^3}{q^2+1},
$$

*so the free-minus-atom log-ratio is exactly a sum over the $A-1$ interfaces:*

$$
  L(Z,N) \;=\; \sum_{\text{interfaces}} -\log(z + d_i),
  \qquad
  L_{pp} = -\log z,\quad
  L_{nn} = -\log(z - h) = \log\bigl(q(q^2+1)\bigr),\quad
  L_{pn} = -\log(z + d_{pn}).
$$

## Measured

At 200 bits, with $q$ from the fifty-digit substrate value, the full
$H_{3A}$ Markov trace of the canonical word against the product of two-strand
factors: $^2$H ($n=6$) $2.3\times10^{-59}$, $^3$H and $^3$He ($n=9$)
$3.1\times10^{-59}$, $^4$He ($n=12$) $4.0\times10^{-59}$; the Jones
polynomial of the closure equals $\prod_i V(T(2,e_i))$ exactly on both
classical branches for $A \le 4$. The three constants $-\log(z+d)$ reproduce
the binding arc's bond constants -- measured there in $H_6$ -- to all sixty
digits (`the_canonical_mass_trace_factorises_over_the_chain_probe.py`).

## What it means for the binding gap

The [linear-chain closed form](#thm:markov-trace-factorization)
$B_{\mathrm{sym}} = a\,[(Z-1)L_{pp} + L_{pn} + (N-1)L_{nn}]$, which the Lean
formalisation of that result took as its *named structural input*, is a
corollary of the topology: connected sum $\Rightarrow$ multiplicative trace
$\Rightarrow$ additive $L$. The canonical closure therefore carries **no
many-body binding at all** -- not by measurement, by theorem. The many-body
cumulants the binding arc found ($c_3 < 0$, $c_4 < 0$, $c_5 > 0$, the
order-six datum) belong to the *all-pairs* bond model, whose band-routed
bonds interleave generators across blocks and destroy the chain form. The
$62\,\%$ that $^4$He is short is absent from the canonical closure because a
connected sum has nothing to put there; any closure that carries genuinely
many-body binding must fail to be composite -- non-split, prime, with the kind
of irreducibly multi-component linking the Borromean rings have and this
chain does not. That is the precise form of "the missing binding is not in the
bond graph", and it says which topology the search has to move to.

## What is formalised, what is checked, what is cited

`QOU.Mass.ChainTraceFactor` (sorry-free) proves the factor algebra: the
affine law $\mathrm{tr}_2(\sigma + d) = z + d$ from the level-2 Wenzl weights
(`twoStrandTrace_eq`); the mirror factor $z - h = 1/(q(q^2+1))$ and
$\mathrm{tr}_2(\sigma)\,\mathrm{tr}_2(\sigma^{-1}) = 1/[2]_q^2$, hence
$L_{pp} + L_{nn} = 2\log(q + q^{-1})$; positivity of all three factors for
$q \ge 1$; and that $-\log$ of a product of positive factors is the sum of the
$-\log$s. The factorisation of the $H_{3A}$ trace is checked at $A \le 4$ and
rests on the chain form (verified through $A = 12$) plus the connected-sum
multiplicativity of the Markov trace, which is classical \cite{birman1974}
and not formalised. Nothing here says which prime closure would carry
many-body binding, or that one exists in the framework.
