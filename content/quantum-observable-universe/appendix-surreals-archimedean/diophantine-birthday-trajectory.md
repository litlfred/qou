## What "separated by birthday trajectory" can and cannot mean

The appendix carries a conjecture that algebraic and transcendental numbers are separated by *birthday trajectory*, motivated by Liouville and Roth. Taken literally as a statement about the birthday of the number, it is not open — it is **impossible**.

The axiom $\mathrm{birthday}(\iota r) \le \omega$ places every real, algebraic and transcendental alike, inside $[0,\omega]$. In Conway's surreals the collapse is total: the dyadic rationals are born strictly before day $\omega$ and **every other real is born exactly on day $\omega$**, so

$$
  \mathrm{birthday}(\sqrt{2}) \;=\; \omega \;=\; \mathrm{birthday}(\pi).
$$

Two numbers with equal birthday are indistinguishable to every predicate of the birthday, so no criterion phrased in $\mathrm{birthday} \circ \iota$ can separate them, however cleverly chosen.

The conjecture's own wording already said where to look. *Trajectory* is load-bearing: Liouville and Roth are about how fast rationals approximate $\alpha$, which in surreal terms is the shape of the **sign expansion** — the path — not the ordinal at which it terminates.

## The obstruction does not transfer, and it nearly did

Moving to trajectories invites the same collapse a second time. Two reals whose sign expansions share a tail differ by a dyadic rational, so any criterion that is a function of the *trajectory* must be invariant under adding a rational. That is exactly the kind of blanket invariance which flattened the birthday version.

It survives, for a reason that is a theorem rather than a hope:

| criterion | invariant under the ambiguity | constant on the irrationals |
|---|---|---|
| $\mathrm{birthday} \circ \iota$ | — | **yes** — separates nothing |
| $\mathrm{LiouvilleWith}\ p$ | yes | **no** — separates |

Approximability to order $p$ is invariant under a rational shift *and* takes both truth values. So the redirection is not a change of wording; it moves to a criterion that survives the invariance its own encoding forces.

## ⚠ Two things the conjecture's framing gets wrong

**One direction is already a theorem.** Liouville's theorem — a real approximable to every order is transcendental — is fully formalised, with $\sum 2^{-n!}$ as a concrete witness. Presenting the separation as wholly open overstates what is open.

**Roth does not help, though the motivation cites it.** Roth sharpens the direction that is *already closed*: an algebraic irrational has approximation exponent exactly $2$, so approximability to any order $p>2$ already forces transcendence, improving Liouville's degree-dependent bound. It says nothing about reals that approximate *slowly*. The naive converse — that slow approximation implies algebraicity — is **false at every $p$**, since almost every real is transcendental with exponent exactly $2$.

## The bridge, and where the exponent actually lives

The sign expansion of a real is the greedy bisection: emit $+$ when the current value undershoots $\alpha$, $-$ otherwise. It provably brackets $\alpha$ at every step, and once bracketed each further sign halves the bracket, giving

$$
  \bigl\lvert \alpha - v_{n+k} \bigr\rvert \;\le\; \frac{\mathrm{gap}_n}{2^{k}} .
$$

**That rate alone certifies nothing.** The error falls as $2^{-k}$ but the denominator grows as $2^{k}$ too, so it is approximation of exponent $1$ — and *every* real is approximable to order $1$ for free. The bracket rate is the denominator, not the discriminator.

The exponent lives in the **run structure**. A $+$ keeps the upper bound and raises the lower; a $-$ does the reverse. So a run of $k$ identical signs **freezes one endpoint** while the bracket keeps halving, leaving a rational fixed *before the run began* that approximates $\alpha$ to accuracy $2^{-k}$ better:

$$
  \Bigl\lvert \alpha - \frac{m}{2^{n}} \Bigr\rvert \;\le\; \frac{\mathrm{gap}_n}{2^{k}} ,
$$

with the denominator pinned by the invariant that every bound after $n$ steps is a dyadic over $2^n$. Accuracy decouples from denominator, which is precisely what an approximation exponent above $1$ means.

## ⚠ Where the difficulty actually is

What remains is a **quantifier**, not machinery: a Liouville condition needs *infinitely many* $n$ carrying a run long enough to beat the exponent. That is a property of the individual $\alpha$ — by Roth the runs are bounded for an algebraic irrational, and unbounded for a Liouville number — and proving it for any particular $\alpha$ is the hard Diophantine mathematics the conjecture was always about.

So the surreal side is not the obstacle, which is the opposite of what the conjecture's placement in this appendix suggests. A second, independent gap remains on that side and should not be confused with this one: lifting any of the above to *birthday* needs a per-step bound on $\mathrm{birthday}(x/2)$, which the axioms do not supply and do not imply.
