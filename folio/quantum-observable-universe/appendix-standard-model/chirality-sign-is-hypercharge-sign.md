**Proposition.** On five strands with charge $Q(\alpha) = T_3 + \alpha Y_0$,
$Y_0 = (-2,-2,-2,3,3)$:

1. $Q(-\alpha)_S = -Q(\alpha)_{s(S)}$, where $s$ swaps the two isospin strands; hence the
   even part at $-\alpha$ has the charge spectrum of the odd part at $\alpha$. The two open
   signs, which part is matter and which root $\alpha = \pm 1/6$ of
   [`prop:neutral-lepton-fixes-charges`](neutral-lepton-fixes-charges.md), are one sign:
   only their product is physical;
2. at $\alpha = 1/6$ strand $4$ is neutral, and $S \mapsto S \,\triangle\, \{4\}$ is a
   bijection from the even part to the odd part that preserves electric charge and fixes
   the colour strands. Colour and electric charge cannot see the sign;
3. six even states have $Y_0 = 1$ and no odd state does, so no bijection between the two
   parts preserves hypercharge.

So the chirality sign is the sign of hypercharge relative to the matter part. It is a
weak-sector datum, as expected: the strong and electromagnetic sectors are vector-like.

**Proof.** Item 1 is `qWeight5_neg` summed over $S$, then reindexing by $s$ and the
complement bijection of [`prop:even-strand-generation`](even-strand-generation.md).
Item 2: adding or removing a neutral strand does not change the charge, and toggling one
strand flips parity. Item 3 is a count over the thirty-two subsets.

**What stays open.** The value of the single remaining sign.

## Lean structure

`QOU.EightfoldWay.ChiralitySignIsHyperchargeSign`: `stateCharge_neg_alpha`,
`even_neg_alpha_eq_odd`, `stateCharge_toggle`, `electric_spectrum_even_eq_odd`,
`hyper_eq`, `hypercharge_count_even`, `hypercharge_count_odd`,
`no_hypercharge_bijection`. Sorry-free.
