*Under convention D the three interface letters are $\sigma + d$ with*

$$
  d_{pp} = 0, \qquad d_{nn} = -h, \qquad d_{pn} = -h\,(1 - \delta/2)/2,
  \qquad h = q - q^{-1},
$$

*and the third is exactly the weighted average of the first two:*

$$
  d_{pn} \;=\; \Bigl(\tfrac12 + \tfrac{\delta}{4}\Bigr) d_{pp}
             + \Bigl(\tfrac12 - \tfrac{\delta}{4}\Bigr) d_{nn},
  \qquad \text{weights summing to } 1,
  \text{ both non-negative iff } |\delta| \le 2 .
$$

*Since the two-strand trace is affine in the offset,
[$\mathrm{tr}_2(\sigma + d) = z + d$](#rem:canonical-trace-factorises-over-chain),
an affine map sends that convex combination to the same convex combination, so
$z + d_{pn}$ lies strictly between $z + d_{nn}$ and $z + d_{pp}$; and
$L = -\log(z+d)$ is strictly decreasing in $d$. Hence*

$$
  L_{pp} \;<\; L_{pn} \;<\; L_{nn}
  \qquad\text{for every } q > 0 \text{ and every } \delta \in (0,2).
$$

## Why it matters at $A = 2$

At two nucleons there is one bond, one word, and no ordering or arrangement
convention to choose, so nothing mediates between the bond constants and the
prediction:

| system | bond | $L$ | $\alpha L$ (MeV) | reality |
|---|---|---|---|---|
| $^2$He | $pp$ | $0.489899$ | $2.0507$ | unbound, no bound diproton |
| $^2$H | $pn$ | $0.676822$ | $2.8332$ | **bound**, $2.22452$ MeV |
| $2n$ | $nn$ | $0.907262$ | $3.7978$ | unbound, no bound dineutron |

Exactly one of the three binds, and it is $pn$. A constant that ranks binding
strength must therefore put $pn$ at an **extreme** — and a convex combination
is never an extreme. The deuteron is assigned the middle value, and is also
overshot by $1.274\times$.

Nothing here is tunable. $\delta = (q-1)^2(1-q^{-4})/3$ equals $0.00138$ at
$q_0$, and would have to reach $2$ — at $q \approx 3.458$ against
$q_0 = 1.10998$ — before the convexity even breaks.

## The caveat, before the conclusion

This arc's $L$ carries no spin, and the real distinction *is* a spin one: the
deuteron binds in the $^3S_1$ triplet channel, and every $^1S_0$ two-body
system — $pp$, $pn$, $nn$ alike — is unbound. A spinless bond constant cannot
be expected to separate bound from unbound, and no claim is made that it
should. What does not follow from the absence of spin is the *order*: nothing
about lacking a spin channel requires the unbound $nn$ system to be ranked
above the bound $pn$ one. That ranking comes from the averaging convention,
and would survive into a spin-resolved theory that kept the same letter.

## Not a contradiction with the $np$-pairing channel

The corpus's $np$ preference does not live in the bond constants. It lives in
the self-conjugate $(2,2) \vdash 4$ partition, as the categorical Wigner energy
$\Delta_{(2,2)} = m_e [3]_q [2]_q^2 = 6.2894$ MeV of
[$np$ pairing](#prop:wigner-np-pairing). That is a level-four object and there
is no $(2,2)$ partition of $2$, so it supplies nothing at $A = 2$. The two
statements are consistent — which is the difficulty, because it leaves the
two-body ordering with nothing to rescue it.

The ordering result above constrains $L$, which is a free-energy difference;
whether $B = \alpha L$ is a binding energy at all is the separate open claim.

## What would have to change

One of these, none of them settled here: the $pn$ interface stops being an
average over crossing sign, so that its letter falls outside the segment
$[d_{nn}, d_{pp}]$; or the bond constant stops being what ranks binding, and a
channel the two-body sector actually possesses carries the $np$ preference; or
the framework declares the bond constant channel-averaged and says explicitly
what it averages over, since at $A = 2$ the $^1S_0$ / $^3S_1$ split is the
entire content.

## What is proved

The convex-combination identity, the strict betweenness of the offsets
for $0 < \delta < 2$, its transport through the affine
trace, and the ordering $L_{pp} < L_{pn} < L_{nn}$
itself are proved. Not proved, because it is empirical input: that
only $pn$ binds. The measurement, the $\delta$ bound and the Wigner reading are
numerical.
