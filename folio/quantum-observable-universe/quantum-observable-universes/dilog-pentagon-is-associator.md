**Proposition.** *Fix the monoidal argument operations — the product $x,y \mapsto xy$, the complement $x \mapsto 1-x$, and division. A potential $f$ on the shuffle algebra $\mathcal{H}_q$ satisfies the Mac Lane pentagon (the five-term relation)*

$$
  f(y) + f(x) = f(xy) + f\!\left(\frac{x(1-y)}{1-xy}\right) + f\!\left(\frac{y(1-x)}{1-xy}\right)
$$

*if and only if it is the evaluation map of a $q$-dilogarithm datum with those arguments.*

The equivalence holds because a $q$-dilogarithm datum is defined by this pentagon, so it restates that definition. It does not show that the rigid-monoidal axioms of $\mathbf{C}$ force $\mathrm{Li}_2^q$; that would need the categorical-to-scalar descent marked below as not formalised. Together with the uniqueness of the level-2 primitive ([inhabitation of the $q$-dilogarithm structure](#prop:q-dilogarithm-exists)), the pentagon axiom names $\mathrm{Li}_2^q$.

## Two guises of the one pentagon

The same Mac Lane coherence has already appeared above in two guises, which this proposition records as one law:

- **Cochain / 3-cocycle guise.** The additive twist associator $\alpha = dF$ satisfies the pentagon automatically because $d^2 = 0$.
- **Dilogarithm five-term guise.** The pentagon condition of the $q$-dilogarithm datum, whose operator form is the Faddeev–Kashaev pentagon $\Phi(\mathsf P)\Phi(\mathsf Q) = \Phi(\mathsf Q)\Phi(\mathsf P+\mathsf Q)\Phi(\mathsf P)$ ([the $q$-dilogarithm pentagon as the monoidal associator axiom](#rem:q-dilogarithm-pentagon-associator)).

A third, braided guise is in the literature at a root of unity. McPhail-Snyder and Reshetikhin show that the holonomy braiding of $U_\xi(\mathfrak{sl}_2)$ at a positive, non-pinched, log-colored crossing factors as $\tfrac1N Z_b(Z_r \otimes Z_l) Z_t$, each factor defined by a quantum dilogarithm \cite[\S4.3, Thm.~4.5, eq.~(4.19)]{mcphail-snyder-reshetikhin2025}, and that these R-matrices satisfy a holonomy Yang--Baxter equation for admissible colorings \cite[\S4.4, Thm.~4.7]{mcphail-snyder-reshetikhin2025}. That is a statement about the braiding at a root of unity; it does not supply the scalar equivalence of this proposition or the categorical-to-scalar descent of the scope boundary below.

## Proof outline

The biconditional holds over an arbitrary carrier with an addition, with no further structure. The forward direction packages the solution of the pentagon as a $q$-dilogarithm datum; the reverse reads the datum's five-term condition.

## Scope boundary

The equivalence is at the level of the scalar pentagon potential. The *categorical $\to$ scalar* descent (that the morphism-level Mac Lane pentagon on $\alpha_{X,Y,Z}$ reduces to this scalar five-term equation) is the classical shuffle–associator identification of Faddeev–Kashaev; the analytic five-term relation at $q \neq 1$ remains conjectural.
