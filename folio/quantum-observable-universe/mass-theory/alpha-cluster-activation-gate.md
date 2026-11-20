**Proposition ($\alpha$-cluster activation gate).**
*Let a three-cluster arrangement carry pairwise linking numbers
$(\ell_{12},\ell_{13},\ell_{23})\in\mathbb{Z}^3$, and let
$\Delta = \gcd(\ell_{12},\ell_{13},\ell_{23})$. The Milnor triple-linking
residue $\bar\mu$ is a well-defined invariant only in $\mathbb{Z}/\Delta\mathbb{Z}$
[`milnor1954`]. Then:*

1. *(**Hopf-spectator gate closed**) if some pairwise linking is a unit
   $|\ell_{ij}| = 1$, then $\Delta = 1$, so $\mathbb{Z}/\Delta\mathbb{Z}$ is a
   subsingleton and $\bar\mu$ carries no invariant triple content — the bond
   channel is **inactive**;*
2. *(**Brunnian gate open**) the residue space is the full $\mathbb{Z}$ (the gate
   is open, $\Delta = 0$) **iff** all pairwise linkings vanish,
   $\ell_{12}=\ell_{13}=\ell_{23}=0$ — the Brunnian/Borromean pattern;*
3. *(**sign-representation obstruction**) any $\Sigma_3$-equivariant linear map
   from the pair-vector module to the sign representation is identically zero
   over any commutative ring; the inter-cluster coupling therefore factors
   through $|\bar\mu|$ only (no chirality-odd channel);*
4. *(**$\mathrm{Vol}=0$ annihilation**) the W-plane binding term
   $\mathfrak{m}_e\,\mathrm{Vol}\,q$ on a bond channel of hyperbolic volume
   $\mathrm{Vol}=0$ is identically zero.*

Together (1)–(4) are a **topological selection rule**: a three-cluster bond
channel contributes body-order binding content only when its arrangement is
Brunnian (2) and its sub-link has $\mathrm{Vol}\neq 0$ (4), and any surviving
coupling is chirality-even (3). Hopf-linked spectator pairs (1) are switched
off. This is the categorical origin of the "$k\ge 3$, $\alpha$-only" activation
pattern: two $\alpha$-clusters share a Hopf-type spectator link (gate closed),
whereas a Borromean triple of $\alpha$-clusters opens the gate.

## Status

All four parts are proved, over a generic commutative ring where the statement permits:

- **(1)–(2)** A Hopf-linked spectator, $|\ell_{ij}| = 1$, makes the indeterminacy quotient $\mathbb{Z}/\Delta\mathbb{Z}$ trivial; and the gate is open, $\Delta = 0$, iff all $\ell_{ij} = 0$. A Brunnian cluster triple therefore has a non-trivial residue.
- **(3)** The $\Sigma_3$ sign-representation coupling vanishes by Schur's lemma, over any commutative ring, and in particular on the charge bilinears.
- **(4)** $\mathrm{Vol} = 0 \Rightarrow \mathfrak{m}_e\,\mathrm{Vol}\,q = 0$. The companion selection of the CAL-3 class is a *conditional* result: it assumes a binding-volume ledger, which is an open input and not part of this proposition's proved content.
