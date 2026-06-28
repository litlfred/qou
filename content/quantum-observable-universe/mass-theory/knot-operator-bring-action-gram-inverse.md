The Gram matrix of the six knot operators
([knot-operator action on the Bring surface](#rem:knot-operator-bring-action))
has an inverse $G^{-1}$ that defines the Frobenius dual basis; on
the Bring surface this realises operator selection as a minimum-action
principle.

## The Gram inverse on the Bring surface

The Gram inverse $G^{-1}$ defines the Frobenius dual basis:
$b_k^\vee = \sum_j (G^{-1})_{kj} b_j$. On the Bring surface,
$G^{-1}$ is the **metric inverse** — it converts between the
"crossing basis" (knot operators $b_k$) and the "demand basis"
(Frobenius duals $b_k^\vee$).

The LP/SDP operator-selection framework minimises
$\sum t_k x_k$ subject to Gram constraints. In the Bring-surface
interpretation, this is a **minimum-action principle on
$\Sigma_4$**: the optimal knot operator is the one that minimises
the action functional (Markov trace) over the moduli space of
braid embeddings in the Bring surface.

The $\mathrm{SO}(3)$ extension would make this a minimum-action
principle on $\Sigma_4 \times \mathrm{SO}(3) / S_3$ — optimising
over both the knot type AND the orientation. If the minimum over
orientations is unique (which would follow from the Bring
surface's rigidity as a hyperbolic 3-manifold complement), this
would derive the averaged-crossing convention from a variational
principle — closing
[`conj:canonical-knot-id-sdp`](#conj:canonical-knot-id-sdp).
