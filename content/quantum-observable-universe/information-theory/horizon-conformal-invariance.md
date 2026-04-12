**Proposition.**
*Let $\mathcal{H}$ be a jet horizon
([jet horizon](#def:jet-horizon)) in an affine chart $U$,
and let $A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots$
be the brane tower.*

*The boundary datum $\partial\mathcal{A} = (A_1/A_0, A_2/A_0)|_{\mathcal{H}}$
that survives the horizon is invariant under rescaling of $A_0$:
for any $\lambda \in \mathcal{O}(U)^{\times}$,*

$$
  (A_1 / \lambda A_0,\; A_2 / \lambda A_0)\big|_{\mathcal{H}}
  \;=\;
  (A_1 / A_0,\; A_2 / A_0)\big|_{\mathcal{H}}.
$$

*In particular, the boundary datum depends only on the
**conformal class** of $A_0$ (its zero locus), not on the
specific generator of the horizon ideal $\mathfrak{h}$.*

**Proof sketch.**
On $\mathcal{H}$, the ideal $\mathfrak{h}$ vanishes:
$s|_{\mathcal{H}} = 0$ for all $s \in A_0$.  The quotient
$A_k/A_0$ restricted to $\mathcal{H}$ depends only on the
equivalence class of sections modulo $\mathfrak{h}$.
Rescaling $A_0 \mapsto \lambda A_0$ with
$\lambda|_{\mathcal{H}} \neq 0$ does not change the ideal
$\mathfrak{h}$ (since $\lambda s$ vanishes on $\mathcal{H}$
iff $s$ does).  Therefore the quotients are identical on
$\mathcal{H}$.  $\square$

**Interpretation.**
This is the QOU analogue of conformal invariance in
Penrose's CCC \cite{penrose2010}.  In CCC, massless particles
are conformally invariant: they do not see the conformal
factor $\Omega$.  Here, the degree $\geq 1$ jet data does not
see the "size" of $A_0$ — only its vanishing locus matters.

The observability axioms of the QOU
([observation](#def:observation)) require a non-degenerate
Frobenius pairing to detect degree-$0$ data.  At the horizon,
$A_0 = 0$ and the Frobenius pairing degenerates on that
component.  The surviving observations are those that act on
$A_k/A_0$ — the higher-jet conformal data.  **Conformal
invariance at the horizon is a consequence of the
observability axioms**, not an additional assumption.
