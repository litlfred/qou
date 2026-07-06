The recursive brane tower
([recursive brane tower](#def:recursive-brane-tower))
$A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots$
and its direct limit
([direct limit algebra](#def:direct-limit-algebra))
$\mathcal{A}_\infty = \varinjlim_n \mathrm{End}_{\mathbf{C}}(A_n)$
provide a categorical counterpart of the Swampland Distance
Conjecture.

**The Swampland statement.**
Traversing an infinite geodesic distance $\Delta\phi$ in moduli space
produces an infinite tower of states whose masses fall exponentially,
$m \sim m_0\, e^{-c\,\Delta\phi}$, and the local effective field theory
description breaks down \cite{ooguri-vafa2007}.

**QOU translation.**
Each jet prolongation $J^1(A_n)$ adds a floor to the tower; the
order-$\geq 3$ interaction defects that cannot be absorbed at level $n$
ascend one jet level at a time
([mass endomorphism jet tower](#rem:mass-endomorphism-jet-tower)),
generating an infinite sequence of successively higher-order
topological states. At a jet horizon
([jet horizon](#def:jet-horizon)) the degree-$0$ algebra vanishes while
the higher-degree jet data leak through: the fibre-valued
particle-identity description fails there, and only the tower of
higher-order data survives — the categorical analogue of an effective
description breaking down into a surviving tower of states.

**Scope.**
The brane tower, its colimit, and the jet horizon are defined, and the
horizon is Lean-formalised. The identification of the transfinite limit
with an infinite-distance point of a moduli space, and the reading of
the jet-horizon vanishing $A_0 \to 0$ as the generic endpoint of that
limit, are interpretive: the framework carries no metric moduli space,
and a global Frobenius degeneration at the limit is not established —
the axioms in fact propagate Frobenius non-degeneracy up the tower. We
read the dictionary in one direction: the jet horizon furnishes a
concrete instance of the Distance-Conjecture picture, not a proof of
it.
