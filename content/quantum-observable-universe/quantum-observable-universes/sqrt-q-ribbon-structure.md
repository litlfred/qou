The braiding eigenvalues
([braiding-eigenvalue-extraction](#prop:braiding-eigenvalue-extraction))
are $q$ and $-q^{-1}$.  Neither involves $q^{1/2}$.  The element
$v := q^{1/2}$ does **not** appear in the core QOU axioms; it enters
only when one equips $\mathbf{C}$ with a **ribbon structure**.

**What a ribbon structure adds.**  A ribbon structure on a braided
monoidal category $\mathbf{C}$ is a natural isomorphism
$\varTheta_V \colon V \xrightarrow{\sim} V$ (the *twist* or *framing
morphism*) satisfying

$$
  \varTheta_{V \otimes W} = (c_{W,V} \circ c_{V,W}) \circ (\varTheta_V \otimes \varTheta_W),
  \qquad
  \varTheta_{V^\vee} = (\varTheta_V)^\vee,
$$

and compatible with duals.  For the standard $\mathrm{SU}_q(2)$
representation on $V$, the twist acts as scalar multiplication by
$v = q^{1/2}$ on the defining representation, so that
$\varTheta_V = q^{1/2}\,\mathrm{id}_V$.

**Why $q^{1/2}$ is absent from QOU core.**  The QOU axioms
([quantum-observable-universe](#def:quantum-observable-universe)) require
a braided rigid monoidal category with a $*$-structure and volume
constraint — but not a ribbon structure.  The differential-geometric
layer (Reeb field, $q$-connection, categorical Dirac operator) does not
use $\varTheta$.  The element $q^{1/2}$ would only be needed to:

1. define invariants of *framed* links (as opposed to oriented links);
2. construct a topological quantum field theory from $\mathbf{C}$
   via the Reshetikhin--Turaev functor ([TQFT context](#rem:tqft-context));
3. write the full modular tensor category (MTC) datum for
   quantum-group Chern--Simons theory.

None of these are part of the present paper's main development.

**When $q^{1/2}$ enters.**  If a future extension equips the QOU with
a ribbon structure $\varTheta$, then $v = q^{1/2}$ is determined (up to
sign) by the already-fixed $q$ via $v^2 = q$.  The sign ambiguity
corresponds to a choice of spin structure on the framing.  This choice
is separate from the braiding-orientation convention
([rem:braiding-unit-circle-convention](#rem:braiding-unit-circle-convention)).
