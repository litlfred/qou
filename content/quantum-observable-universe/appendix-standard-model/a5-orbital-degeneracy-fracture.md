If the archimedean truncation of [the truncation conjecture](#conj:sm-gauge-truncation) is the right picture — observable-scale symmetry descending from the fibre's discrete automorphisms rather than a continuous rotation group — then atomic orbital degeneracies inherit a specific discrete fingerprint. Restricting the $(2l+1)$-dimensional $\mathrm{SO}(3)$ representations to the icosahedral group $A_5 \subset S_5$ (the orientation-preserving automorphisms of the Bring fibre) gives, by exact character arithmetic:

| orbital | $2l+1$ | $A_5$ decomposition |
|---|---|---|
| $s$ | $1$ | $\mathbf{1}$ |
| $p$ | $3$ | $\mathbf{3}$ |
| $d$ | $5$ | $\mathbf{5}$ |
| $f$ | $7$ | $\mathbf{3}' \oplus \mathbf{4}$ |
| $g$ | $9$ | $\mathbf{4} \oplus \mathbf{5}$ |
| $h$ | $11$ | $\mathbf{3} \oplus \mathbf{3}' \oplus \mathbf{5}$ |

The $s$, $p$, $d$ degeneracies are *native* — they are exactly the dimensions $1, 3, 5$ of $A_5$ irreducibles and restrict irreducibly. Every degeneracy above five fractures: the group has no irreducible of dimension greater than $5$, so the $f$ orbital's seven states are, under the truncated symmetry, a composite of a $\mathbf{3}'$ and a $\mathbf{4}$ that a continuous rotation group would hold together. The branching arithmetic is standard finite-group representation theory, computed exactly and pinned in the witness `a5-so3-branching.witness.json`.

The physical reading — that $f$-shell degeneracy is only approximate, with a fine-structure split along the $\mathbf{3}' \oplus \mathbf{4}$ seam — is conditional on the truncation conjecture and is recorded here as an interpretive consequence, not a prediction wired to any computation. Its value is falsifiability in principle: a truncated discrete symmetry *cannot* hold seven states exactly degenerate, while exact $\mathrm{SO}(3)$ can, so the two pictures differ at some resolution on lanthanide-scale spectroscopy.
