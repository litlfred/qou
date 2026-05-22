The linear $\mathrm{C}_6$ chain
([linear C$_{6}$](#ex:carbon-chain-c6)) and benzene
([benzene ring](#ex:benzene-ring)) represent two fundamentally
different topological states of six carbon atoms: pairwise
Hopf-linked versus threaded by $T(2,6)$.

**Energy accounting via Alexander polynomials.**

The crossing energy of each structure is proportional to its
Alexander polynomial weight at the substrate parameter $q$
([threading link](#def:threading-link)):

| Structure | Binding topology | $\Delta(q)$ | At $q \approx 1$ |
|-----------|-----------------|-------------|------------------:|
| Chain $\mathcal{C}_6$ | 5 Hopf links $T(2,2)$ | $5 \times 1$ | 5 |
| Pairwise ring | 6 Hopf links $T(2,2)$ | $6 \times 1$ | 6 |
| Threaded ring $\mathcal{R}_6$ | $T(2,6)$ | $q^2 + 1 + q^{-2}$ | 3 |

The threaded ring binds all 6 carbons with Alexander weight
$\approx 3$ — **less than the chain's weight of 5**, despite
binding one more atom.

**Why the chain exists.**
If the ring is lower in energy, why does the linear chain
exist at all?  Because the transition from pairwise to
threaded topology is **discontinuous**.  The chain cannot
continuously deform into the ring — the binding structure must
be dissolved and reformed:

1. **Dissolve**: the 5 pairwise Hopf links release their
   crossing energy.

2. **Reconfigure**: the 6 carbon atoms must adopt a cyclic
   spatial arrangement that admits the threading link.

3. **Thread**: the $T(2,6)$ link forms, threading through all
   6 atoms at once.

Step 2 is the bottleneck.  The 6 carbons must be in the correct
geometric configuration — a near-planar hexagon — before the
threading link can form.  A fully extended chain has its
endpoints far apart; they must be brought together and the
intervening atoms rearranged.  This geometric reconfiguration
is the **activation barrier**.

**The spring analogy, revised.**
The open chain is a spring held apart.  The endpoints are free,
the interior oscillates
([spring-like modes](#rem:chain-spring-modes)).  Snapping it
shut means:

- Bringing the endpoints together (geometric cost).
- Dissolving the pairwise links (bond-breaking cost).
- Forming the threading link (topological phase transition).

Once the threading forms, the energy drops below the chain —
the spring has snapped into a lower-energy, locked
configuration.  The lock is the threading link itself: a
non-local topological structure that cannot be broken by any
local perturbation.

**Asymmetry of the barriers.**
The closure barrier (chain $\to$ ring) is primarily **geometric**:
getting the atoms into position.  The opening barrier (ring $\to$
chain) is primarily **topological**: dissolving the threading
link $T(2,6)$ into 5 separate Hopf links, which costs

$$
  \Delta E_{\mathrm{open}}
   \propto 
  (N - 1) - \Delta_{T(2,N)}(q)
  = 
  5 - (q^2 + 1 + q^{-2})
   \approx 
  2
  \quad (|q| \approx 1)
$$

in additional Alexander weight — the ring must "expand" its
compact threading back into the less efficient pairwise
encoding.  Opening the ring is harder than closing it.
