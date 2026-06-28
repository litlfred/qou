**Proposition.**
*Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be a QOU and let
$U \subset M_0$ be an affine chart admitting a chain of
adjacent aeons
$\ldots, \mathcal{A}_{-1}, \mathcal{A}_0, \mathcal{A}_1, \ldots$
([aeon](#def:aeon)).  Then the aeon chain satisfies the three
defining properties of a conformal cyclic cosmology
\cite{penrose2010}:*

**(CCC-1) Conformal invariance at boundaries.**
*At each aeon boundary $\mathcal{S}_b$, the boundary datum
$\partial\mathcal{A}|_b = (A_1/A_0, A_2/A_0)|_{\mathcal{S}_b}$
is invariant under rescaling of $A_0$
([conformal invariance](#prop:horizon-conformal-invariance)).
The surviving data depends only on the conformal class of the
horizon ideal $\mathfrak{h}$ — its vanishing locus, not the
specific generator.*

**(CCC-2) Boundary data inheritance.**
*The CMB of aeon $\mathcal{A}_{k+1}$
([CMB boundary datum](#def:cmb-boundary-datum)) equals the
terminal boundary datum of aeon $\mathcal{A}_k$:*

$$
  \mathrm{CMB}(\mathcal{S}_0^{(k+1)})
  = 
  \partial\mathcal{A}_k\big|_b.
$$

*The degree $\geq 1$ jet data that survives the terminal horizon
of one aeon is identically the seed of the next.*

**(CCC-3) Only conformally invariant data crosses.**
*At each boundary, the degree-$0$ algebra vanishes:
$A_0|_{\mathcal{S}_b} = 0$.  By the observability axioms
([observation](#def:observation)), the Frobenius pairing
degenerates on $A_0$ at the boundary, so no degree-$0$
observable can detect a difference between the two sides.
The only data that crosses is the degree $\geq 1$ quotient
— the conformal data.*

**Proof.**
(CCC-1) is the content of
[conformal invariance at the jet horizon](#prop:horizon-conformal-invariance).

(CCC-2) follows from the definition of aeon adjacency
([aeon](#def:aeon)): adjacent aeons share the boundary
$\mathcal{S}_b$, and the CMB of the successor aeon is by
definition the degree $\geq 1$ data at its past boundary,
which is the same locus $\mathcal{S}_b$.

(CCC-3) follows from the definition of a jet horizon
([jet horizon](#def:jet-horizon)): $A_0|_{\mathcal{H}} = 0$
is the defining condition, and the Frobenius non-degeneracy
axiom requires $A_0 \neq 0$ for degree-$0$ observations to
be well-defined.  At the boundary where $A_0 = 0$, the
pairing degenerates and degree-$0$ data is unobservable.
$\square$

**Limitations of the claim.**
The proposition establishes that a QOU *with aeons* is
structurally a CCC.  It does **not** claim:
- that any particular affine chart admits aeons (this is dynamical),
- that the aeon chain is infinite in either direction,
- that Penrose's specific conformal rescaling $g \mapsto \Omega^2 g$
  is the mechanism (the QOU mechanism is ideal vanishing, not
  metric rescaling).

The content is that the CCC structure is a **theorem of the
QOU axioms**, not an additional postulate: conformal invariance
at boundaries, data inheritance, and the restriction to
conformally invariant observables all follow from the
observability axioms and the brane tower structure.
