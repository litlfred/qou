*Let $L$ be a function on subsets $S$ of the $A$ nucleons of an
[atomic braid](#def:atomic-braid) with $L(\varnothing) = 0$, and define its
**Möbius cumulants** over the Boolean lattice by the recursion*

$$
  \mathrm{cum}(S) \;=\; L(S) \;-\; \sum_{T \subsetneq S} \mathrm{cum}(T).
$$

*Then, with no further hypothesis on $L$:*

1. *(Reconstruction.) $\displaystyle \sum_{T \subseteq S} \mathrm{cum}(T) = L(S)$ for every $S$.*
2. *(The $c_k$-only recursion.) If $L(S)$ depends only on $|S|$, say
   $L(S) = f(|S|)$, then $\mathrm{cum}(S) = c_{|S|}$ where*
   $$
     c_k \;=\; f(k) \;-\; \sum_{j<k} \binom{k}{j}\, c_j .
   $$
3. *(Mixed cumulants vanish across an additive split.) If the nucleons split
   as $\mathcal{A} \sqcup \mathcal{B}$ and $L(S) = L(S \cap \mathcal{A}) +
   L(S \cap \mathcal{B})$ for every $S$, then $\mathrm{cum}(S) = 0$ whenever
   $S$ meets both $\mathcal{A}$ and $\mathcal{B}$.*

## Application to cluster-cumulant extraction

The bond model of binding reads the many-body content of a nucleus off the
Markov trace: with bonds placed among the nucleons in $S$, in the interleaved
order the [canonical interface composition](#def:canonical-braid-interface-composition)
fixes, one sets $L(S) = \log\bigl(\mathrm{tr}_{\mathrm{free}} / \mathrm{tr}_S\bigr)$
and reads the genuine $k$-body term as the order-$k$ cumulant. Item 1 is what
makes the cumulants a decomposition of the full $L$ rather than a rearrangement
of it; item 3 is what makes them *cumulants* in the standard sense (independence
kills every mixed one) and it is the property that turns the
Markov trace's multiplicativity on split links (an unbonded nucleon is a
separate component, contributing equally to numerator and denominator) into
additivity of $L$ on disjoint bonded parts.

Item 2 is the working tool. For an exchangeable system (every nucleon the
same, so $L(S)$ sees only $|S|$), the $2^A - A - 1$ subset traces at $3A$
strands collapse to $A - 1$ scalar inputs $f(k) = L_k$, each of which can be
computed in its own minimal system of $3k$ strands because $L(S)$ does not see
nucleons outside $S$. At $A = 6$ that is five trace pairs, one of them at
$n = 18$, in place of fifty-seven traces at $n = 18$; it is the difference
between an order-six cumulant existing and not.

## Combinatorial inversion identity versus numerical evaluation

The three items are algebra, true for every set function on every commutative
ring. The two
facts that make the bond model an instance (that the homonuclear $L(S)$
depends only on $|S|$, and that it does not see nucleons outside $S$) are
properties of this particular trace. They are established at 200-bit precision
(residuals at the working floor, $\sim 10^{-59}$, at $A = 3, 4, 5$), whereas the general algebraic trace axiomatisation carries cyclicity
and single-generator conjugation rather than the split-link tensor rule, and the band
routing of a far bond sits between other letters where conjugation invariance
does not reach.
