## An axiom set that admits a model it was not meant to admit

The surreal-field axiom system used in this corpus asks for more than an ordered field. It also demands Conway's birthday — a map $\mathrm{birthday} : K \to \mathrm{Ordinal}$ — constrained by six axioms: its values at $0$ and $1$, its invariance under negation, a bound for sums, a bound for averages, and a bound of $\omega$ on the birthdays of real numbers.

Those six do not pin down the intended object.

**Theorem.**
*Let $\beta(x) = 0$ if $x = 0$ and $\beta(x) = 1$ otherwise, on the hyperreals $\mathbb{R}^*$. Then $\beta$ satisfies*

$$
  \beta\!\left(\frac{x + y}{2}\right) \;\le\; \beta(x) \oplus \beta(y) + 1
  \qquad\text{for all } x, y,
$$

*and likewise each of the other five birthday axioms.*

A function taking only the values $0$ and $1$ is visibly not Conway's birthday, under which $\omega$ is born at stage $\omega$ and the dyadic rationals are spread across every finite stage. Yet it satisfies the axioms in full.

## The axiom with the most design commentary is the one satisfied with the least effort

The average bound is documented in the corpus as "exactly Conway's $\{L \mid R\}$ recipe" and as "genuinely independent" of the sum bound. Under $\beta$ it holds for a reason that has nothing to do with either: the right-hand side is at least $0 + 1 = 1$ whatever $x$ and $y$ are, and the left-hand side is at most $1$ because $\beta$ is bounded by $1$. The inequality is satisfied by slack alone. Under a bounded birthday the axiom constrains nothing.

That is the sharpest form of the defect. The axiom carrying the most design commentary is the one the unintended model satisfies by default, and no amount of reading the commentary would reveal that — only exhibiting the model does.

## What follows, and what does not

**What follows.** Any theorem proved *from these axioms alone* is also true of the model in which every nonzero element is born on day $1$. Such a theorem therefore says nothing specific about birthdays, whatever its statement appears to be about. This is a statement about the axioms, not about Conway's theory, which is untouched.

**What does not follow.** The axioms are not *inconsistent*, and nothing here says the surreal material built on them is wrong. It says that material is weaker than its vocabulary suggests, and that the gap is invisible from inside.

The practical consequence: the structure on $\mathbb{R}^*$ given by $\beta$ must **never** be treated as the intended one. Doing so would silently apply every theorem proved from these axioms to the hyperreals under a birthday that is not Conway's — turning a documented defect into a silent one.

## The limit-transfer conjecture, and why this does not rescue it

The surreal limit-transfer conjecture was stated over this carrier. Its actual analytic content — that limits are computed by the standard part of an $\omega$-evaluation, that eventual domination transfers to $\mathbb{R}^*$, and the resulting limit-comparison inequality — mentions no birthday at all, and is proved directly as ordinary hyperreal analysis.

So the conjecture discharges in a precise and deflationary sense: **its content is birthday-free, and it was stated over a carrier that is not.** The honest repair is to weaken the class's carrier so the statement lives where its content lives — not to promote the instance and declare the conjecture closed.

One limitation is worth stating because it bounds the whole approach. Convergence along the hyperfilter is strictly weaker than convergence along $\mathrm{atTop}$: only the direction $\mathrm{Tendsto\ atTop} \Rightarrow \mathrm{IsSt}$ is available, and the converse fails. Everything here therefore *pushes* real limits into $\mathbb{R}^*$. Nothing discharges an ordinary limit goal by a standard-part computation, because $\mathrm{IsSt}$ at one chosen infinite element is not the "for every infinite hypernatural" statement a genuine non-standard limit argument needs.

**Standard-part machinery does not replace the $\varepsilon$–$\delta$ arguments in this corpus.** Any claim that it shortens them should be checked against this asymmetry first.

## Scope

Nothing here is a result about surreal numbers. Conway's birthday and Robinson's non-standard analysis are classical and unaffected; the finding is about one axiomatisation in this corpus, and it is a negative one. It is recorded because an under-determined axiom set is the kind of defect that compiles, passes review, and propagates silently.
