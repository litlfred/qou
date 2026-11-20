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

## Lean structure

All four parts are formalized (generic commutative ring where the
statement permits):

- **(1)–(2)** `QOU.Mass.MilnorIndeterminacyGate` —
  `gate_kills_hopf_spectator` ($|\ell_{ij}|=1 \Rightarrow
  \mathrm{Subsingleton}\,(\mathbb{Z}/\Delta\mathbb{Z})$) and
  `gate_open_iff_brunnian` ($\Delta = 0 \iff$ all $\ell_{ij}=0$), with the
  structure-level `ClusterTriple.residue_nontrivial_of_brunnian`.
- **(3)** `QOU.Mass.MilnorSignRepObstruction.equivariant_linearMap_eq_zero`
  (Schur-lemma vanishing of the $\Sigma_3$ sign-rep coupling over any
  `CommRing`), with `coupling_vanishes_on_charge_bilinears`.
- **(4)** `QOU.Mass.BondChannelClassSelection.wplane_term_eq_zero_of_vol_eq_zero`
  ($\mathrm{Vol}=0 \Rightarrow \mathfrak{m}_e\,\mathrm{Vol}\,q = 0$). The
  companion CAL-3 class-selection statement
  (`eq_cal3_of_support_ne_zero_of_ledger`) is a *conditional* result on
  the `BindingVolumeLedger` class (no instance declared — the ledger is an open
  input, not part of this proposition's proved content).

**Scope.** Only the *topological activation gate* — which inter-cluster bond
channels are on or off, and the chirality-even coupling — is asserted here. The
binding **magnitudes** $B(\text{cluster})$, the light-spectator coefficient $b$,
the gated pair coefficient $g$, and the resulting $\le 0.31\%$ multi-isotope
closure ("Model G") are **not** part of this proposition. Those enter the
cluster bindings at their *measured* AME values and calibrate $b$, $g$
empirically; they are recorded — labelled as a structural/phenomenological
model, **not** a parameter-free derivation — in the interpreting remark
[Model G: a phenomenological $\alpha$-cluster binding closure](#rem:alpha-cluster-model-g-closure).
