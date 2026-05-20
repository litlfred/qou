Closing a molecular Hopf chain into a ring is a **topological
phase transition**: the pairwise Hopf link structure is replaced
by a single threading link $T(2,N)$
([threading link](#def:threading-link)).  The energy barrier
arises not from adding one more bond, but from reorganising the
entire binding topology.

**Statement.**
Let $\mathcal{C}_N$ be a molecular Hopf chain of length $N$
([molecular Hopf chain](#def:molecular-hopf-chain)), and let
$\mathcal{R}_N$ be the corresponding threaded ring
([molecular Hopf ring](#def:molecular-hopf-ring)).  The crossing
energies, measured by Alexander polynomial evaluation at the
substrate parameter $q$, are:

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathcal{C}_N)
   \propto 
  (N-1) \cdot \Delta_{T(2,2)}(q)
  = 
  N - 1,
$$

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathcal{R}_N)
   \propto 
  \Delta_{T(2,N)}(q)
  = 
  \frac{q^{N/2} - q^{-N/2}}{q - q^{-1}}
  \quad (\text{for even } N).
$$

For $N = 6$:

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathcal{C}_6)
   \propto  5,
  \qquad
  \mathfrak{E}_{\mathrm{cross}}(\mathcal{R}_6)
   \propto 
  q^2 + 1 + q^{-2}
   \approx  3
  \quad (|q| \approx 1).
$$

The ring has **lower crossing energy** than the chain.  It binds
6 atoms with Alexander weight $\approx 3$, compared to the
chain's weight of $5$ for only 5 pairwise bonds.

**The barrier: topological reorganisation.**
Despite the ring being energetically favourable, the transition
$\mathcal{C}_N \to \mathcal{R}_N$ requires a discontinuous
change in topology: $N - 1$ separate Hopf links must be
**replaced** by a single threading link $T(2,N)$.  This is not a
continuous deformation — the braid word changes from a product of
non-adjacent generators $\sigma_i^2$ to the correlated product
$(\sigma_1 \cdots \sigma_{N-1})^2$.

The transition state is the configuration where the chain's
pairwise links are partially dissolved but the threading link has
not yet formed.  At this point, some bonds are broken but no
threading stabilisation has been gained — the crossing energy is
at a **maximum**:

$$
  \mathfrak{E}_{\mathrm{cross}}(\text{transition})
   > 
  \max\bigl(
    \mathfrak{E}_{\mathrm{cross}}(\mathcal{C}_N),
    \mathfrak{E}_{\mathrm{cross}}(\mathcal{R}_N)
  \bigr).
$$

The activation barrier is the energy required to reach this
intermediate state.

**Ring super-stability from threading.**
Once the threading link $T(2,N)$ forms, it locks the ring in a
deep topological trap.  Breaking the ring requires not just
severing one bond but **dissolving the threading link entirely**
— converting the correlated $T(2,N)$ back into $N$ separate
Hopf links.  The energy cost of ring-opening is:

$$
  \Delta E_{\mathrm{open}}
  = 
  (N - 1) - \Delta_{T(2,N)}(q)
  + 
  E_{\mathrm{activation}}.
$$

For $N = 6$: the threading provides $5 - 3 = 2$ units of
additional stabilisation beyond the pairwise picture, plus the
full activation barrier must be re-climbed.  The ring is
super-stable because the threading link is a **lower-energy
encoding** of the same binding — reverting to the pairwise
encoding costs energy.

**The spring analogy.**
The open chain is a spring held apart.  The threading link is
what happens when the spring snaps shut: the separate coils
(pairwise Hopf links) merge into a single, tighter winding
($T(2,N)$).  The merged winding is more efficient (lower
Alexander weight) and cannot be separated without unwinding
the entire structure.
