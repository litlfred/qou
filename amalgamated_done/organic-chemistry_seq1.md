<!-- FILE_START: molecular-chains-rings-intro.md -->
We assemble atoms into extended molecular structures. A **[molecular Hopf chain](#def:molecular-hopf-chain)** of length $N$ composes $N - 1$ covalent bonds along a backbone, giving a tridiagonal linking matrix with free endpoint sites. To pass to closed rings, we replace the naïve picture — $N$ pairwise Hopf links — with a single non-local invariant: the **[threading link](#def:threading-link)** $T(2,N)$. Its braid word winds twice through every atom, and its Alexander polynomial records half the pairwise Alexander weight. A **[molecular Hopf ring](#def:molecular-hopf-ring)** binds atoms globally by the threading link rather than locally by Hopf links.

The remaining blocks read off the dynamical consequences. Open chains behave as topological springs. Ring closure is a topological phase transition. The transition state is the barrier where pairwise bonds dissolve before the threading link forms. The same mechanism explains ring super-stability.
<!-- FILE_END: molecular-chains-rings-intro.md -->

<!-- FILE_START: molecular-hopf-chain.md -->
**Definition.**
Let $\mathcal{A}_1, \ldots, \mathcal{A}_N$ be atoms with residual sub-links $R_1, \ldots, R_N$. A **molecular Hopf chain** of length $N$ and bond order $k$ is the composite

$$
  \mathcal{C}_N^{(k)}
  = 
  \mathcal{A}_1
   \underset{B_k}{\oplus}
  \mathcal{A}_2
   \underset{B_k}{\oplus}
  \cdots
   \underset{B_k}{\oplus}
  \mathcal{A}_N
$$

where $\underset{B_k}{\oplus}$ joins two adjacent atoms by an order-$k$ covalent bond $B_k(R_i, R_{i+1})$. The **linking matrix** is the tridiagonal $N \times N$ matrix:

$$
  L^{\mathrm{chain}}_{ij}
  = 
  \begin{cases}
    k & \text{if } |i - j| = 1, \\
    0 & \text{otherwise}.
  \end{cases}
$$

**Boundary conditions.**
The endpoint atoms $\mathcal{A}_1$ and $\mathcal{A}_N$ consume only $k$ of their available linking sites for the chain bond. The remaining open sites are **free endpoints**.

**Crossing energy of the chain.**
The total crossing energy is the sum over $N - 1$ bonds:

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathcal{C}_N^{(k)})
  = 
  (N - 1) \cdot E_{\mathrm{bond}}(k).
$$

The absence of a bond between $\mathcal{A}_1$ and $\mathcal{A}_N$ is the missing link distinguishing chains from rings.
<!-- FILE_END: molecular-hopf-chain.md -->

<!-- FILE_START: threading-link.md -->
**Definition.**
Let $\mathcal{A}_1, \ldots, \mathcal{A}_N$ be atoms arranged in a cycle. The **threading link** of the ring is the torus link

$$
  \mathcal{T}_N =  T(2, N),
$$

whose closure in the braid group $B_N$ is

$$
  \hat{\beta}_N
  = 
  (\sigma_1  \sigma_2  \cdots  \sigma_{N-1})^2.
$$

The threading link winds **twice** around the torus defined by the $N$ atoms, passing through every atom on each winding. It has $2(N-1)$ crossings.

**Component structure.**
The number of components of $T(2,N)$ is $\gcd(2,N)$. For even $N$, the threading link is a 2-component link. These two components are the topological realisation of the two delocalised $\pi$ electrons.

**Alexander polynomial.**
The Alexander polynomial of $T(2,N)$ for even $N = 2m$ is

$$
  \Delta_{T(2,2m)}(t)
  = 
  \frac{t^m - t^{-m}}{t - t^{-1}}.
$$

Evaluated at the substrate parameter $t = q$:

| Threading | $m$ | $\Delta(q)$ |
|-----------|:---:|-------------|
| $T(2,2)$ (Hopf) | 1 | $1$ |
| $T(2,4)$ | 2 | $q + q^{-1}$ |
| $T(2,6)$ | 3 | $q^2 + 1 + q^{-2}$ |
| $T(2,8)$ | 4 | $q^3 + q + q^{-1} + q^{-3}$ |
<!-- FILE_END: threading-link.md -->

<!-- FILE_START: threading-link-weight.md -->
**Key identity.**
The threading link's Alexander weight sets the ring-closure barrier. For $T(2,6)$:

$$
  \Delta_{T(2,6)}(q)
  = 
  q^2 + 1 + q^{-2}
  = 
  (q + q^{-1})^2 - 1.
$$

The threading link's Alexander weight is **one less than the square** of the Hopf link energy quantum $|q + q^{-1}|_{\mathrm{mol}}$.

**Contrast with pairwise Hopf links.**
The pairwise picture bonds $N$ atoms with $N$ separate Hopf links, giving total Alexander weight $N \cdot \Delta_{T(2,2)}(q) = N$. The threading link replaces all $N$ bonds with a single invariant:

$$
  \frac{\Delta_{T(2,2m)}(q)}{N}
  = 
  \frac{q^2 + 1 + q^{-2}}{6}
   \approx 
  \frac{1}{2}
  \qquad (|q| \approx 1).
$$

The threading carries **half the Alexander weight** of the pairwise construction. This propagates into the crossing energy, halving the predicted ring-closure barrier.
<!-- FILE_END: threading-link-weight.md -->

<!-- FILE_START: molecular-hopf-ring.md -->
A **molecular Hopf ring** binds all atoms simultaneously via a single threading link.

**Definition.**
Let $\mathcal{A}_1, \ldots, \mathcal{A}_N$ be atoms arranged in a cycle. A **molecular Hopf ring** of length $N$ is the composite

$$
  \mathcal{R}_N
  = 
  [\mathcal{A}_1, \ldots, \mathcal{A}_N]
   \oplus 
  \mathcal{T}_N,
$$

where $[\mathcal{A}_1, \ldots, \mathcal{A}_N]$ denotes the $N$ atoms in cyclic arrangement, and $\oplus$ superposes that arrangement with the threading link $\mathcal{T}_N = T(2, N)$.
<!-- FILE_END: molecular-hopf-ring.md -->

<!-- FILE_START: hopf-ring-rigidity.md -->
**Crossing energy of the ring.**
The crossing energy is determined by the Alexander polynomial evaluated at the substrate parameter:

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathcal{R}_N)
   \propto 
  \Delta_{T(2,N)}(q).
$$

**Contrast with the pairwise picture.**
A naïve pairwise ring has crossing energy proportional to $N$. The threading link evaluates to roughly $N/2$. The threading is topologically more efficient.

| Structure | Binding | Alexander weight | Crossings |
|-----------|---------|:---:|:---:|
| Chain ($N-1$ Hopf links) | pairwise | $N - 1$ | $2(N-1)$ |
| Ring ($N$ Hopf links) | pairwise | $N$ | $2N$ + rearrangement |
| Ring ($T(2,N)$ threading) | non-local | $\Delta_{T(2,N)}(q) \approx N/2$ | $2(N-1)$ |

The threading ring has **fewer crossings than the pairwise ring** and **no rearrangement cost**.

**Rigidity.**
The threading link passes through every atom twice. Deforming the ring requires moving the threading link through all $N$ atoms simultaneously. This global operation is the topological origin of ring rigidity.
<!-- FILE_END: hopf-ring-rigidity.md -->

<!-- FILE_START: chain-spring-modes.md -->
An open molecular Hopf chain behaves like a **topological spring**. Free endpoints undergo Reidemeister I moves, and Reidemeister II moves propagate without affecting interior bonds.

**Longitudinal modes.**
A compression or extension corresponds to a correlated sequence of Reidemeister II moves along the backbone.

**Bending modes.**
The chain bends at any interior atom. The bending stiffness depends on the bond order $k$: single-bond backbones are flexible, double-bond backbones are rigid.

**Endpoint oscillation.**
Free endpoints are soft. Dangling trefoils oscillate at low energies. This is the topological analogue of the stretching vibration of terminal groups.

In a closed ring, these soft modes are quenched. Every atom is interior, and deformation requires a global braid rearrangement.
<!-- FILE_END: chain-spring-modes.md -->

<!-- FILE_START: ring-closure-barrier.md -->
Closing a molecular Hopf chain into a ring is a **topological phase transition**: pairwise Hopf links are replaced by a single threading link $T(2,N)$. The energy barrier arises from reorganising the binding topology.

**Statement.**
Let $\mathcal{C}_N$ be a molecular Hopf chain, and $\mathcal{R}_N$ the threaded ring. The crossing energies are:

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathcal{C}_N)
   \propto 
  N - 1,
$$

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathcal{R}_N)
   \propto 
  \Delta_{T(2,N)}(q)
  \quad (\text{for even } N).
$$

For $N = 6$, the ring has lower crossing energy than the chain.

**The barrier: topological reorganisation.**
The transition $\mathcal{C}_N \to \mathcal{R}_N$ requires a discontinuous change in topology. $N - 1$ separate Hopf links are replaced by a single threading link $T(2,N)$. 

The transition state is the configuration where the chain's pairwise links are partially dissolved but the threading link has not yet formed. The crossing energy is at a maximum.

The energy cost of ring-opening is:

$$
  \Delta E_{\mathrm{open}}
  = 
  (N - 1) - \Delta_{T(2,N)}(q)
  + 
  E_{\mathrm{activation}}.
$$
<!-- FILE_END: ring-closure-barrier.md -->

<!-- FILE_START: ring-closure-superstability.md -->
**The spring analogy.**
The open chain is a spring held apart. Closing it into a ring snaps the spring shut. The separate coils merge into a single tighter winding.

**Ring super-stability from threading.**
For $N = 6$, crossing weight drops from $5$ to $\approx 3$, providing additional stabilisation. Breaking the ring requires dissolving the threading link entirely back into $N$ separate Hopf links. The threading link is a lower-energy encoding of the binding. Reverting to the pairwise encoding costs energy.

**The barrier: topological reorganisation.**
The transition $\mathcal{C}_N \to \mathcal{R}_N$ requires a discontinuous change in topology. The braid word changes from a product of non-adjacent generators to the correlated product $(\sigma_1 \cdots \sigma_{N-1})^2$.
<!-- FILE_END: ring-closure-superstability.md -->
