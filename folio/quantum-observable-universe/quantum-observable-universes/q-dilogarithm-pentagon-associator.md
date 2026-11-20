The $q$-dilogarithm is not imported into the framework as a separate datum; it is the solution of a coherence condition the substrate category $\mathbf{C}$ already carries. Because $\mathbf{C}$ is monoidal, its associator $\alpha_{X,Y,Z}\colon (X\otimes Y)\otimes Z \to X\otimes(Y\otimes Z)$ satisfies the Mac Lane **pentagon coherence** — the five reassociations of a fourfold tensor commute. Passing to the shuffle Hopf algebra $\mathcal{H}_q$ of the braiding, that coherence descends to a functional equation on the level-2 shuffle primitive: the five reassociations collapse to the **five-term relation**

$$
  \mathrm{Li}_2^q(y) + \mathrm{Li}_2^q(x) = \mathrm{Li}_2^q(xy) + \mathrm{Li}_2^q\!\left(\frac{x(1-y)}{1-xy}\right) + \mathrm{Li}_2^q\!\left(\frac{y(1-x)}{1-xy}\right).
$$

By the [definition of the $q$-dilogarithm](#def:q-dilogarithm) there is exactly one level-2 primitive satisfying this relation, so the pentagon axiom *names* $\mathrm{Li}_2^q$ rather than merely constraining it — the dilogarithm is the unique scalar shadow of the associator. In operator form this is the Faddeev–Kashaev identity: the quantum dilogarithm is the **quantum associator** (equivalently the $6j$-symbol), and the operator pentagon

$$
  \Phi(\mathsf P)\,\Phi(\mathsf Q) = \Phi(\mathsf Q)\,\Phi(\mathsf P+\mathsf Q)\,\Phi(\mathsf P)
$$

on a Weyl pair $\mathsf P\mathsf Q = \mathsf Q\mathsf P + 1$ is the same coherence read as a fusion move.

The equivalence of the pentagon with the $q$-dilogarithm, proved below, is *scalar*: a potential on $\mathcal{H}_q$ satisfies the five-term relation exactly when it is a $q$-dilogarithm datum. The descent from the morphism-level Mac Lane pentagon on $\alpha_{X,Y,Z}$ to that scalar equation is the classical shuffle--associator identification of Faddeev--Kashaev, and the analytic five-term relation at $q \neq 1$ remains conjectural. So the pentagon *names* $\mathrm{Li}_2^q$ within the scalar layer, and the passage from the categorical axiom to that layer rests on the cited identification.

**Two faces of the one associator.** On the substrate branch (real $q$) the pentagon is realised by the *compact* dilogarithm $\Phi_q / \mathrm{Li}_2^q$ — the bar-even face that drives mass and binding. Continued to the fibre branch $|q|=1$, where the compact product's zeros accumulate on the unit circle and it ceases to be well defined, the surviving realisation is Faddeev's *non-compact modular double* $\Phi_b = \Phi_{1/b}$ (with $q = e^{2\pi i b^2}$) — the bar-odd face carrying the decay observable. Both solve the *same* pentagon; they are the two archimedean lenses of the identification of the $\Phi_q$ machinery with the AJ-conjecture machinery in the stochastic-mechanics chapter (real versus root-of-unity saddle of the one $\hat{A}_K$), not two different objects.

**The observable is a pairing, not a product.** Where an archimedean number is finally extracted, the dilogarithm associator enters as an analytic *operator* paired against the algebraic Markov-trace *state* — a Hopf–Drinfeld pairing (equivalently a $q$-difference-module action), not a scalar multiplication: the continuous flow is contracted against the finite cyclotomic trace data. This "analytic paired with algebraic" structure fixes the *shape* of the observable. It does not, by itself, determine the analytic monodromy datum away from the roots of unity — that datum is genuinely resurgent and remains open.
