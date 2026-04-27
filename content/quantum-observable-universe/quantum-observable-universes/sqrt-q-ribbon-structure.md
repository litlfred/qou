The braiding eigenvalues
([braiding-eigenvalue-extraction](#prop:braiding-eigenvalue-extraction))
are $q$ and $-q^{-1}$; neither involves $q^{1/2}$.  The element
$v := q^{1/2}$ is *post-Archimedean naming*: pre-Archimedean it is a
formal adjoined square root in the splitting field $\mathbb{Q}(q^{1/2})$
and carries no geometric content; post-Archimedean (after the
realization functor at $q_0$) it becomes the real number $q_0^{1/2}$,
and the binary sign choice is the spin structure on the realized
worldline (see [sign-as-spin-structure](#rem:sign-as-spin-structure)).

A *ribbon structure* on $\mathbf{C}$ is a natural twist
$\varTheta_V \colon V \xrightarrow{\sim} V$ satisfying
$\varTheta_{V \otimes W} = (c_{W,V} \circ c_{V,W}) \circ (\varTheta_V \otimes \varTheta_W)$
and $\varTheta_{V^\vee} = (\varTheta_V)^\vee$.  By Schur, on a simple
object the twist is a scalar; combining the twist axiom with the Hecke
eigenvalues $(q, -q^{-1})$ forces this scalar to $\pm q^{1/2}$, so on
the defining $\mathrm{SU}_q(2)$ representation
$\varTheta_V = q^{1/2}\,\mathrm{id}_V$.

The ribbon datum is post-Archimedean: it is needed exactly when the
realization target carries a framing — e.g.\ for the Reshetikhin--Turaev
functor ([tqft-context](#rem:tqft-context)) or for an MTC structure on
$\mathrm{Rep}(\mathbf{C})$ — and so it does not enter the QOU core
axioms ([quantum-observable-universe](#def:quantum-observable-universe)).
