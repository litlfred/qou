**Crossing energy of the ring.**
The crossing energy is determined by the threading link's
Alexander polynomial evaluated at the substrate parameter:

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathcal{R}_N)
   \propto 
  \Delta_{T(2,N)}(q).
$$

For even $N = 2m$:

$$
  \Delta_{T(2,2m)}(q)
  = 
  \frac{q^m - q^{-m}}{q - q^{-1}}.
$$

**Contrast with the pairwise picture.**
A naïve ring built from $N$ separate Hopf links would have
crossing energy proportional to $N \cdot \Delta_{T(2,2)}(q) = N$.
The threading link replaces this with a single polynomial that
evaluates to roughly $N/2$ — the threading is **topologically
more efficient** than pairwise bonding.

| Structure | Binding | Alexander weight | Crossings |
|-----------|---------|:---:|:---:|
| Chain ($N-1$ Hopf links) | pairwise | $N - 1$ | $2(N-1)$ |
| Ring ($N$ Hopf links) | pairwise | $N$ | $2N$ + rearrangement |
| Ring ($T(2,N)$ threading) | non-local | $\Delta_{T(2,N)}(q) \approx N/2$ | $2(N-1)$ |

The threading ring has **fewer crossings than the pairwise ring**
and **no rearrangement cost** — the threading link already
connects all strands.

**Rigidity.**
The threading link passes through every atom twice (once per
winding).  Deforming the ring requires moving the threading link
through all $N$ atoms simultaneously — a global operation.  This
is the topological origin of ring rigidity: it is not that
individual bonds are stiff, but that the threading link
correlates all atoms non-locally.
