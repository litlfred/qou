**Brunnian property and confinement.**  The defining property of
the Borromean link $\mathcal{B}_3$ is that *every two-component
sub-link is the unlink* — the three components are
topologically inseparable, yet no two of them are pairwise
linked.  Concretely, deleting any one of the three unknots that
make up a [Borromean baryon](#def:borromean-baryon) leaves a
trivial two-component unlink, so the topological binding of the
remaining two strands collapses immediately on the removal.

**Implication for quark isolation.**  An "isolated quark" would
be the configuration produced by lifting one unknot out of
$\mathcal{B}_3$.  Such a configuration is not stable in the
Borromean topology: the same move that extracts one strand
unlinks the other two, so the would-be free quark arrives
together with the dissolution of the bound state.  Pulling on a
single constituent therefore cannot produce a free quark; it
produces three unbound unknots.  This is the topological face of
*color confinement* — the empirical fact that quarks are never
observed in isolation is exactly the Brunnian property of
$\mathcal{B}_3$, with no separate dynamical assumption required.

**Location of the computation.**  The energetic cost
attached to the unlinking move — the bare topological mass that
distinguishes a confined Borromean baryon from three free
unknots — is the hyperbolic-volume contribution computed in the
[Borromean baryon mass formula](#conj:borromean-baryon-mass-formula);
the corresponding Bloch-group element lives in
[Borromean Bloch-group element](#conj:borromean-bloch-group-element).
The present remark records only the *topological* mechanism so
that the confinement statement has a single named home in the
manifest.  The formal Lean counterpart is
[Brunnian property of $\mathcal{B}_3$](#conj:brunnian-property-of-borromean),
which states that every two-component sub-link of the Borromean
rings is the unlink and traces the formalisation gap to the
absence of Mathlib Reidemeister-move primitives.
