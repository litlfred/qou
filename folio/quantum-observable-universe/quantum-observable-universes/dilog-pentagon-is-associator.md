**Proposition.** *Fix the monoidal argument operations — the product $x,y \mapsto xy$, the complement $x \mapsto 1-x$, and division. A potential $f$ on the shuffle algebra $\mathcal{H}_q$ satisfies the Mac Lane pentagon (the five-term relation)*

$$
  f(y) + f(x) = f(xy) + f\!\left(\frac{x(1-y)}{1-xy}\right) + f\!\left(\frac{y(1-x)}{1-xy}\right)
$$

*if and only if it is the evaluation map of a $q$-dilogarithm datum with those arguments.*

This is the precise sense in which the $q$-dilogarithm is **forced by the rigid-monoidal axioms** of $\mathbf{C}$: the pentagon coherence of the associator $\alpha$ does not merely *constrain* $\mathrm{Li}_2^q$ — *being a solution of the pentagon is equivalent to being a $q$-dilogarithm.* Together with the uniqueness of the level-2 primitive ([inhabitation of the $q$-dilogarithm structure](#prop:q-dilogarithm-exists)), the pentagon axiom names $\mathrm{Li}_2^q$.

## Two guises of the one pentagon

The same Mac Lane coherence has already appeared above in two guises, which this proposition records as one law:

- **Cochain / 3-cocycle guise.** The additive twist associator $\alpha = dF$ satisfies the pentagon automatically because $d^2 = 0$.
- **Dilogarithm five-term guise.** The pentagon condition of the $q$-dilogarithm datum, whose operator form is the Faddeev–Kashaev pentagon $\Phi(\mathsf P)\Phi(\mathsf Q) = \Phi(\mathsf Q)\Phi(\mathsf P+\mathsf Q)\Phi(\mathsf P)$ ([the $q$-dilogarithm pentagon as the monoidal associator axiom](#rem:q-dilogarithm-pentagon-associator)).

## Proof outline

The biconditional holds over an arbitrary carrier with an addition, with no further structure. The forward direction packages the solution of the pentagon as a $q$-dilogarithm datum; the reverse reads the datum's five-term condition.

## Scope boundary

The equivalence is at the level of the scalar pentagon potential. The *categorical $\to$ scalar* descent (that the morphism-level Mac Lane pentagon on $\alpha_{X,Y,Z}$ reduces to this scalar five-term equation) is the classical shuffle–associator identification of Faddeev–Kashaev; the analytic five-term relation at $q \neq 1$ remains conjectural.
