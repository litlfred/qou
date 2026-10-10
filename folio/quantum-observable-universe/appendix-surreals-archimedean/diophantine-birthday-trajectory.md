## What "separated by birthday trajectory" can and cannot mean

The appendix carries a conjecture that algebraic and transcendental numbers are separated by *birthday trajectory*, motivated by Liouville and Roth. Taken literally as a statement about the birthday of the number, it is not open — it is **impossible**.

The axiom $\mathrm{birthday}(\iota r) \le \omega$ places every real, algebraic and transcendental alike, inside $[0,\omega]$. In Conway's surreals the collapse is total: the dyadic rationals are born strictly before day $\omega$ and **every other real is born exactly on day $\omega$**, so

$$
  \mathrm{birthday}(\sqrt{2}) \;=\; \omega \;=\; \mathrm{birthday}(\pi).
$$

Two numbers with equal birthday are indistinguishable to every predicate of the birthday, so no criterion phrased in $\mathrm{birthday} \circ \iota$ can separate them, however cleverly chosen.

The conjecture's own wording already said where to look. *Trajectory* is load-bearing: Liouville and Roth are about how fast rationals approximate $\alpha$, which in surreal terms is the shape of the **sign expansion** — the path — not the ordinal at which it terminates.

## The obstruction does not transfer

Moving to trajectories invites the same collapse a second time. Two reals whose sign expansions share a tail differ by a dyadic rational, so any criterion that is a function of the *trajectory* must be invariant under adding a rational. That is exactly the kind of blanket invariance which flattened the birthday version.

It survives, and for a reason that is a theorem:

| criterion | invariant under the ambiguity | constant on the irrationals |
|---|---|---|
| $\mathrm{birthday} \circ \iota$ | — | **yes** — separates nothing |
| $\mathrm{LiouvilleWith}\ p$ | yes | **no** — separates |

Approximability to order $p$ is invariant under a rational shift *and* takes both truth values. So the redirection moves to a criterion that survives the invariance its own encoding forces.

## ⚠ Two things the conjecture's framing gets wrong

**One direction is already a theorem.** Liouville's theorem — a real approximable to every order is transcendental — is fully formalised, with $\sum 2^{-n!}$ as a concrete witness. Presenting the separation as wholly open overstates what is open.

**Roth does not help, though the motivation cites it.** Roth sharpens the direction that is *already closed*: an algebraic irrational has approximation exponent exactly $2$, so approximability to any order $p>2$ already forces transcendence, improving Liouville's degree-dependent bound. It says nothing about reals that approximate *slowly*. The naive converse — that slow approximation implies algebraicity — is **false at every $p$**, since almost every real is transcendental with exponent exactly $2$.

## The bridge, and where the exponent actually lives

The sign expansion of a real is the greedy bisection: emit $+$ when the current value undershoots $\alpha$, $-$ otherwise. It provably brackets $\alpha$ at every step, and once bracketed each further sign halves the bracket, giving

$$
  \bigl\lvert \alpha - v_{n+k} \bigr\rvert \;\le\; \frac{\mathrm{gap}_n}{2^{k}} .
$$

**That rate alone certifies nothing.** The error falls as $2^{-k}$ but the denominator grows as $2^{k}$ too, so it is approximation of exponent $1$ — and *every* real is approximable to order $1$ for free.

The exponent lives in the **run structure**. A $+$ keeps the upper bound and raises the lower; a $-$ does the reverse. So a run of $k$ identical signs **freezes one endpoint** while the bracket keeps halving, leaving a rational fixed *before the run began* that approximates $\alpha$ to accuracy $2^{-k}$ better:

$$
  \Bigl\lvert \alpha - \frac{m}{2^{n}} \Bigr\rvert \;\le\; \frac{\mathrm{gap}_n}{2^{k}} ,
$$

with the denominator pinned by the invariant that every bound after $n$ steps is a dyadic over $2^n$. Accuracy decouples from denominator, which is precisely what an approximation exponent above $1$ means.

Measuring the run against $n$ rather than absolutely turns this into an exponent: a run of length $k \ge n t$ gives $\lvert \alpha - m/2^n \rvert \le 1/(2^n)^t$. And that closes the loop to the standard predicate —

$$
  \Bigl(\text{runs of length } \ge n t \text{ for infinitely many } n\Bigr)
  \;\wedge\;
  \alpha \notin \mathbb{Q}
  \quad\Longrightarrow\quad
  \mathrm{LiouvilleWith}\ t\ \alpha .
$$

So the trajectory picture's central assertion — that run structure in the sign expansion controls the Diophantine exponent — is a proved implication. Irrationality is not a technicality here: a rational $\alpha$ eventually *is* one of its own dyadic approximants, and the standard predicate excludes that case by definition.

## ⚠ The remaining input is a theorem, not a conjecture

What makes the criterion separate is **Thue–Siegel–Roth**: an algebraic irrational has approximation exponent exactly $2$, hence is not approximable to any order $p > 2$. Granting that, "approximable to order $3$" does what a separation must — it fails on *every* algebraic irrational and holds on an exhibited transcendental:

$$
  \text{Roth}
  \;\Longrightarrow\;
  \Bigl(\ \forall\, \alpha \ \text{algebraic irrational},\ \ \neg\,\mathrm{LiouvilleWith}\,3\,\alpha \Bigr)
  \ \wedge\
  \mathrm{LiouvilleWith}\,3\Bigl(\textstyle\sum_{n} 2^{-n!}\Bigr).
$$

The second conjunct is unconditional; the first is exactly Roth.

**So this should not be recorded as an open conjecture.** Roth proved it in 1955. What is missing is a *formalisation*, not a proof — and the distinction matters here, because this conjecture has already carried three separate epistemic mislabelings: an "honest open state" that encoded nothing, a separation impossible as stated, and a direction already proved elsewhere.

⚠ A name collision makes the opposite error easy too. Searching a formal library for "Roth's theorem" *succeeds* — and returns the **additive-combinatorics** result on three-term arithmetic progressions, an unrelated theorem sharing the name. Thue–Siegel–Roth is absent, and a search by name says otherwise.

So the surreal side is not the obstacle, which is the opposite of what this conjecture's placement suggests. One genuine gap does remain on that side and should not be confused with the above: lifting any of this to *birthday* needs a per-step bound on $\mathrm{birthday}(x/2)$, which the axioms neither supply nor imply.
