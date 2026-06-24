The constituent baseline $Z \mathfrak{m}_{\mathfrak{p}} + N \mathfrak{m}_{\mathfrak{n}} + Z m_e$ uses CODATA inputs.

The Wedderburn 3-term correction is the paper's
[Wedderburn mass formula](#thm:wedderburn-mass-formula) with $\alpha = m_e \cdot 8G$ from
[binding scale](#prop:binding-scale-catalan).
The functionals $\Phi_1, \Phi_2, \Phi_3$ are evaluated using only
inter-nucleon generators of the atomic braid: this convention isolates
inter-nucleon interactions, and ensures free nucleons ($A = 1$)
contribute exactly zero to $\Phi$ (preserving the constituent baseline
inputs and the proton-neutron mass splitting exactly).

$\Delta_W$ is the paper's
[Wigner $T=0$ np pairing](#prop:wigner-np-pairing) for the
self-conjugate partition $(2,2) \vdash 4$.
$\Delta_{T=1}$ is the natural extension to $T=1$ same-flavor pairs
using the same partition and the same $\min/A$ structure, replacing
$\min(Z,N)$ (number of $T=0$ pn pairs) by $n_{pp} + n_{nn}$ (number
of $T=1$ same-flavor pairs).

Numerical evaluation at $q_0 = 1.109978595554181\ldots$ (50 dps) uses
[`computations/derived_only_formula.py`](#)
(witness `derived-only-formula.witness.json`).
$\qquad\blacksquare$
