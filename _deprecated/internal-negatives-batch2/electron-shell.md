**Definition.**
*Let $P_{\mathrm{nuc}}$ be a [confined particle](#def:confined-particle)
at level $\ell = 1$ (nucleon-level atom) with coarse braid
$K_{\mathrm{nuc}} \in H_A(R, q)$.  An **electron shell of multiplicity
$Z$** attached to $P_{\mathrm{nuc}}$ is a triple*

$$
  S \;=\;
  \bigl(
    \{e_1, \ldots, e_Z\},\ \iota,\ W_{\mathrm{bind}}
  \bigr)
$$

*where:*

1. *$\{e_1, \ldots, e_Z\}$ is a collection of $Z$ **electron
   particles** — each $e_k$ is a confined particle
   $([\sigma_1^3]_M, 2)$ (trefoil on two strands, $\ell = 0$);*

2. *$\iota: H_A(R, q) \hookrightarrow H_{A+Z}(R, q)$ is the **cabling
   embedding** that extends the nucleon-level Hecke algebra by $Z$
   additional strands — one per electron;*

3. *$W_{\mathrm{bind}} \in H_{A+Z}(R, q)$ is the **binding subword**,
   a product of Hecke generators $\sigma_{i}^{\pm 1}$ selected by
   the [confinement SDP](#prop:confinement-sdp) solved at level
   $\ell = 6$ (atom-electron) of the multi-level hierarchy.*

*The electrons live as additional strands in the unified braid
$\iota(K_{\mathrm{nuc}}) \cdot W_{\mathrm{bind}}$ rather than as
separate Hopf-linked components — each electron is a cable strand,
not an external component.  Binding is the SDP subword, not a
single topological crossing.*

**Binding multiplicity.**
*Let $\mathcal{S}^*(S, q)$ be the active dual support of the SDP at
optimum ([confinement SDP](#prop:confinement-sdp)).  The number*

$$
  \mu(S, q) \;=\; |\mathcal{S}^*(S, q)|
$$

*is the **binding multiplicity** of the shell at $q$.
Generic $Z$: $\mu = 1$ (single-block binding, recovering the scalar
LP regime).  Magic $Z \in \{2, 10, 18, 36, 54, 86\}$ (noble-gas
configuration): $\mu \ge 2$ — multiple Wedderburn blocks are
simultaneously tight, so the binding subword is a genuine sum over
blocks:*

$$
  W_{\mathrm{bind}}
  \;=\;
  \sum_{\lambda \in \mathcal{S}^*} w_\lambda \cdot \pi_\lambda \cdot \Phi^*.
$$

*The witness `electron-shell-ilp` ("electrons alternate between
$\sigma_1^{-1}$ and $\sigma_0^{-1}$ — Hund's rule pairing") is the
empirical signature of $\mu \ge 2$: two generators carry equal
weight because two Wedderburn blocks are simultaneously tight.*

**Orbital labels.**
*The active support $\mathcal{S}^*$ admits a natural parameterisation
by atomic quantum numbers $(n, \ell, m, s)$:*

- *Principal number $n$ identifies which 2$\times$2 PSD block of the
  multi-level SDP is saturated.*
- *Orbital $\ell$ and magnetic $m$ index generators $\sigma_i$ in
  the active block.*
- *Spin $s \in \{\pm\tfrac12\}$ labels the two dual eigenvectors of
  the saturated block.*

*Pauli exclusion is the structural statement that no two electrons
$e_i, e_j$ share the same $(n, \ell, m, s)$, which is equivalent
to the SDP refusing to double-count any dual eigenvector of a
saturated block.*

**Relation to "cabling" and earlier link pictures.**
*The earlier colored-Hopf-link picture (each electron = separate
component with linking number 1 around the nucleus) is **refuted**
by the multi-operator SDP structure: magic-number closure requires
$\mu \ge 2$, which a single Hopf crossing cannot provide.  The
cabling picture — electrons as strands in $H_{A+Z}(q)$ with
SDP-selected binding subword — matches the computational witnesses
(`atom_braid_electron.py`, `electron-shell-quotient.py`,
`electron-shell-ilp.py`) exactly.*
