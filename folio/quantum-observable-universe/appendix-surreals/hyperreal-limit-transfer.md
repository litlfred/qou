## Limit transfer, at the hyperreals, without the surreal apparatus

The appendix carries a conjecture packaging "limits become surreal equalities": an $\omega$-evaluation sending each real sequence to a surreal number, compatible with the algebra and the order, and computing limits through the standard part. It is stated over the abstract surreal-field axioms without an explicit model on that carrier.

The content needs none of that structure.

**Theorem.**
*Let $a_n \to L$ in the $\varepsilon$–$N$ sense. Then, in the hyperreals $\mathbb{R}^*$,*

$$
  \mathrm{st}\bigl(\,{}^{*}\!a\,\bigr) \;=\; L ,
$$

*where ${}^{*}\!a$ is the germ of the sequence at the hyperfilter. Eventual domination transfers to the hyperreal order, and the limit-comparison inequality follows from monotonicity of the standard part.*

## The bridge is a definitional unfolding

The corpus's notion of two surreals being infinitesimally close, applied to a hyperreal and an embedded real, unfolds to

$$
  \forall \varepsilon > 0,\quad \lvert x - r\rvert < \varepsilon ,
$$

which is literally the standard-part relation $\mathrm{IsSt}(x, r)$ on $\mathbb{R}^*$. So the conjecture's analytic content is the standard part of the hyperreals, and the surreal carrier plays no role in it.

## Scope and non-equivalence with sequential convergence

Hyperfilter convergence is strictly weaker than sequential convergence as $n \to \infty$. The arrow

$$
  a_n \to L \ \text{along } \mathrm{atTop}
  \quad\Longrightarrow\quad
  \mathrm{IsSt}({}^{*}\!a, L)
$$

is available; **the converse is false**. Everything here therefore *pushes* real limits into $\mathbb{R}^*$. Nothing here proves sequential convergence as $n \to \infty$ by a single standard-part computation, because $\mathrm{IsSt}({}^{*}\!a, r)$ says $a(\omega) \approx r$ for one specific $\omega$, not for every infinite hypernatural — which is what a genuine nonstandard limit argument requires, and which evaluating at the single diagonal class of one ultrapower does not supply.

**So surreal and standard-part machinery does not replace standard $\varepsilon$–$\delta$ arguments.** That was the hoped-for payoff.

## A defect in the surrounding axioms

Instantiating these axioms on $\mathbb{R}^*$ also exposes a structural feature of the six birthday conditions. The two-valued function

$$
  \mathrm{birthday}(x) \;=\; \begin{cases} 0 & x = 0\\ 1 & x \neq 0\end{cases}
$$

satisfies **all six** birthday axioms. So those axioms do not characterise Conway's birthday; they admit a model in which every nonzero element is born on day one. In particular **no lower bound on birthday is derivable from them** — any statement $\mathrm{birthday}(x) \ge f(x)$ with $f$ unbounded is refuted by that model. Upper bounds are unaffected, which is why the bounds actually proved in the appendix survive: they are all upper bounds, and correspondingly weak.
