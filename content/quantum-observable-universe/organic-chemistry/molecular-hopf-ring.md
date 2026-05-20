A **molecular Hopf ring** is not a chain with its ends joined —
it is a fundamentally different topological object.  Where the
chain bonds atoms pairwise via Hopf links
([molecular Hopf chain](#def:molecular-hopf-chain)), the ring
binds all atoms simultaneously via a single **threading link**
([threading link](#def:threading-link)).

**Definition.**
Let $\mathcal{A}_1, \ldots, \mathcal{A}_N$ be atoms arranged in
a cycle.  A **molecular Hopf ring** of length $N$ is the
composite

$$
  \mathcal{R}_N
  = 
  [\mathcal{A}_1, \ldots, \mathcal{A}_N]
   \oplus 
  \mathcal{T}_N,
$$

where $\mathcal{T}_N = T(2, N)$ is the threading link — a single
torus link that passes through all $N$ atoms.  The threading
link's braid word in $B_N$ is

$$
  \hat{\beta}_N
  = 
  (\sigma_1  \sigma_2  \cdots  \sigma_{N-1})^2,
$$

with $2(N-1)$ crossings, all of the same sign.

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
