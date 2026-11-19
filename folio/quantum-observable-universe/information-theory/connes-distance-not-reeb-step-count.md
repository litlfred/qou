A spectral distance built from $D_\nabla$ is often read as counting Reeb steps: the
minimal number of applications of the flow needed to carry one state to another. The
reading is available only in a limit, and the qualification belongs next to the
identification of the Reeb coefficient rather than in a footnote to it.

The two coefficients of $D_\nabla$ are a convex pair,

$$
  q^{-1} \;+\; \bigl(1 - q^{-1}\bigr) \;=\; 1 ,
$$

with $q^{-1}$ weighting the gradient direction and $\hbar_q = 1-q^{-1}$ the Reeb
direction. A metric induced by $D_\nabla$ therefore measures a *mixture*. It reduces
to a pure Reeb step count exactly when the gradient share vanishes, that is as
$q \to \infty$, where the operator becomes purely contact. At the opposite end,
$q = 1$, the Reeb share vanishes and the operator is pure gradient --- the classical
point, where there is no Reeb period at all.

At the aether parameter $q_0$ the mixture is lopsided in the *wrong* direction for the
step-count reading. The gradient carries $90.09\,\%$ of the weight and the Reeb
direction $9.908\,\%$ (specifically, $q_0^{-1} = 0.90091828395574149216$ and
$\hbar_{q_0} = 0.09908171604425850784$), so nine parts in ten of what the metric
measures is not Reeb transport. Any identification of $d_{\mathrm{Connes}}$ with a
minimal step count at $q_0$ would therefore be off by an order of magnitude in its
dominant term, and the gap is not a small correction to be absorbed.

Two obstructions to the spectral-distance programme are in play and they are
independent. The mixing above says that even a well-defined distance is not the
quantity one wanted. Separately,
[the degeneracy obstruction](#prop:gram-degeneracy-blocks-connes) says the
distance built from the Markov--Gram form is not well-defined at all until the
radical is quotiented away. Repairing either leaves the other standing.
