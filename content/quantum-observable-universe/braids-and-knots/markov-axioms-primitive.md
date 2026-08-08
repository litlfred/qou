Let $R$ be a commutative ring and $q \in R^{\times}$ an invertible element with a chosen square root $q^{1/2}$. The Markov trace $\mathrm{tr}_M$ on the Iwahori-Hecke algebra $H_n(R, q)$ is the unique linear functional satisfying:

1. **Normalisation:** $\mathrm{tr}_M(1) = 1$.
2. **Cyclicity:** $\mathrm{tr}_M(xy) = \mathrm{tr}_M(yx)$ for all $x, y$.
3. **Stabilisation by $\sigma_n$:** $\mathrm{tr}_M(x \sigma_n) = z \cdot \mathrm{tr}_M(x)$ for $x \in H_n(R, q)$, where $z = q^3/(q^2 + 1)$ is the Markov-trace loop value.

Stabilisation by $\sigma_n^{-1}$ — often listed as a fourth axiom — is not an independent condition. Substituting the Hecke quadratic relation $\sigma_n^{-1} = \sigma_n - (q - q^{-1})$ into axiom 3 and using linearity of the trace (with $x \cdot 1 = x$) forces
$$
  \mathrm{tr}_M(x \sigma_n^{-1}) \;=\; z_{-} \cdot \mathrm{tr}_M(x),
  \qquad
  z_{-} \;:=\; z - (q - q^{-1}),
$$
so the negative-crossing loop value $z_{-}$ differs from $z$ whenever $q \neq \pm 1$. No choice of trace parameter makes the two stabilisations scale by mutually inverse factors either: $z \cdot z_{-} = 1$ has the sole solutions $z = q$ and $z = -q^{-1}$, the one-dimensional characters of $H_n(R, q)$, both of which are degenerate. Link invariance of the Jones polynomial is instead restored by the writhe prefactor outside the trace ([Jones–Markov trace](#thm:jones-markov-trace)).

Axioms 1–3 force $\mathrm{tr}_M$ to be the non-degenerate Jones-Markov trace.
Axioms 1–2 with an unspecified stabilisation parameter admit a one-parameter
family, so the value of $z$ selects one member of it. The value above is
**convention D** of the
[trace-convention registry](../../../docs/coordination/trace-convention-registry.md)
— the Jones / $\mathrm{SU}_q(2)$ value, whose braid closure is the Jones
polynomial and whose three-row weight vanishes, $y_{(1^3)} = 0$. Being a
rational function of $q$, it needs no square root; the chosen $q^{1/2}$ above
is retained only for the writhe prefactor.

**The selection is forced, and by two independent steps, neither of which
consults a measured value.**

*Bar-covariance excludes any bar-even $z$ — in particular convention C,
$z = 1/(q^{1/2}+q^{-1/2})$.* The bar involution
([`def:bar-involution`](bar-involution.md)) sends $q \mapsto q^{-1}$ **and**
$\sigma_i \mapsto \sigma_i^{-1}$. Axiom 3 contains $\sigma_n$, so the
bar-partner of $z$ is not $z$: it is the negative-stabilisation value
$z_{-} = z - h$ derived immediately above. Hence the covariance condition
axiom 3 supports is
$$
  \overline{z} \;=\; z - h,
  \qquad
  h = q - q^{-1}.
$$
Convention D satisfies it, both sides equalling $1/(q^3+q)$. Convention C is
invariant under the coefficient half alone ($z(q^{-1}) = z(q)$), so it
violates the condition by exactly $h$ — at every $q$ with $q^2 \neq \pm 1$.
Computing "is $z$ bar-invariant?" as $z(q^{-1}) = z(q)$ applies one half of
the involution while holding the algebra fixed, which is what previously made
C look like the bar-respecting choice.

*Temperley–Lieb faithfulness then picks D out of what remains.* The condition
$\overline{z} = z - h$ is a single equation, so it does not pin $z$ by itself:
its solutions are $q^3/(q^2+1)$ plus any bar-even function. Within that set,
$\mathrm{tr}_M$ factoring through $\mathrm{TL}_3$ and remaining faithful on it
has the unique non-degenerate solution $z = q^3/(q^2+1)$
([`MarkovTraceTLUniqueness`](../lean/QOU/BraidsAndKnots/MarkovTraceTLUniqueness.lean)).

Both steps are proved sorry-free —
[`MarkovParameterFibreRank`](../lean/QOU/BraidKnot/MarkovParameterFibreRank.lean)
(`zD_bar_sub`, `zC_ne_bar_sub`, `bar_sub_of_bar_even`) and
`MarkovTraceTLUniqueness` respectively.

**The full-Hecke trace is still used, deliberately, elsewhere.** Convention C
— the full-Hecke Ocneanu / Wenzl $z$-trace, with $y_{(1^3)} \neq 0$ — is the
trace the **binding** channel runs, and continues to run. That is a
channel-local selection recorded in the
[registry](../../../docs/coordination/trace-convention-registry.md), not a
competing definition of $\mathrm{tr}_M$ here. The bar argument above says C is
not the bar-covariant stabilisation parameter; it does not say the binding
channel is wrong to use the full-Hecke trace, and no binding value changes.

 Because $\mathrm{tr}_M$ is compatible with the tower inclusions and evaluates disjoint generators by iterated application of axiom 3, the joint Markov trace of two braids acting on disjoint strand sets is strictly multiplicative:
$$
  \mathrm{tr}_M(K_1 \sqcup K_2) \;=\; \mathrm{tr}_M(K_1) \cdot \mathrm{tr}_M(K_2).
$$
Appending $k$ further strands, each stabilised by one positive crossing, multiplies this value by $z^k$ (one factor of $z$ per application of axiom 3). This derives the inter-knot decoupling theorem from primitive Markov axioms.
