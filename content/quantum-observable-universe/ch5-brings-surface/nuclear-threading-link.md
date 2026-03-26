The pairwise nucleus $\mathcal{N}(p,n) = p\,\mathfrak{p} \bowtie
n\,\mathfrak{n}$ ([stable nucleus](#def:stable-nucleus)) binds $A = p+n$
nucleons via $\sim A$ nearest-neighbour Hopf junctions, each contributing
Alexander weight $\Delta_{T(2,2)}(q) = 1$.  The **nuclear threading link**
replaces this pairwise encoding with a single torus link that threads
through all $A$ nucleons at once — the nuclear analogue of the molecular
threading link ([threading link](#def:threading-link)) that replaces
pairwise bonds in aromatic rings.

**Definition.**
Let $\mathcal{N}(p,n)$ be a nucleus with $A = p + n$ nucleons.  The
**threaded nucleus** is the composite

$$
  \mathcal{N}^{\mathrm{thr}}(p,n)
  \;=\;
  [\mathfrak{p}_1, \ldots, \mathfrak{p}_p,\,
   \mathfrak{n}_1, \ldots, \mathfrak{n}_n]
  \;\bowtie\;
  \mathcal{T}_A,
$$

where $\mathcal{T}_A = T(2, A)$ is the threading link — a single torus
link whose braid word in $B_A$ is

$$
  \hat{\beta}_A
  \;=\;
  (\sigma_1 \, \sigma_2 \, \cdots \, \sigma_{A-1})^2
$$

with $2(A-1)$ crossings.  The threading link winds twice around the
torus defined by the $A$ nucleons, passing through every nucleon on
each winding.

**Braid shortcut.**
The key structural difference from the pairwise nucleus:

| Encoding | Binding topology | Alexander weight | Crossings |
|----------|-----------------|:---:|:---:|
| Pairwise $\mathcal{N}(p,n)$ | $\sim A$ Hopf links $T(2,2)$ | $\sim A$ | $\sim 2A$ |
| Threaded $\mathcal{N}^{\mathrm{thr}}(p,n)$ | single $T(2,A)$ | $\Delta_{T(2,A)}(q) \approx A/2$ | $2(A-1)$ |

The threading carries roughly **half the Alexander weight** of the
pairwise construction.  This factor of $\tfrac{1}{2}$ propagates
into the crossing energy ([crossing energy](#def:crossing-energy)),
making the threaded nucleus lower in energy than the pairwise
version — a **braid shortcut**.

**Alexander polynomial of the nuclear threading link.**
For even $A = 2m$:

$$
  \Delta_{T(2,2m)}(q)
  \;=\;
  \frac{q^m - q^{-m}}{q - q^{-1}}
  \;=\;
  q^{m-1} + q^{m-3} + \cdots + q^{-(m-1)}.
$$

For odd $A = 2m+1$, the threading is a knot (single component):

$$
  \Delta_{T(2,2m+1)}(q)
  \;=\;
  \frac{q^{m+1/2} - q^{-(m+1/2)}}{q^{1/2} - q^{-1/2}}.
$$

**Which crossings are adjacent.**
In the braid word $(\sigma_1 \cdots \sigma_{A-1})^2$, each generator
$\sigma_i$ crosses strand $i$ over strand $i+1$.  The nucleon species
assigned to strand $i$ determines the crossing character:

- If strands $i$ and $i+1$ are both $\mathfrak{p}$: **positive**
  crossing, Skein weight $q$.
- If strands $i$ and $i+1$ are both $\mathfrak{n}$: **negative**
  crossing, Skein weight $q^{-1}$.
- If strands $i$ and $i+1$ are mixed ($\mathfrak{p}$--$\mathfrak{n}$):
  **neutral** crossing, Skein weight $\tfrac{1}{2}(q + q^{-1})$.

In the pairwise nucleus, the $\binom{p}{2}$ proton--proton crossings
are spread across separate Hopf junctions.  In the threaded nucleus,
the same crossing asymmetry is **concentrated into the braid word**:
the arrangement of protons and neutrons along the $A$ strands
determines which $\sigma_i$ carry positive, negative, or mixed weight.

**Optimal strand ordering.**
The threading energy depends on how the $p$ protons and $n$ neutrons
are distributed among the $A$ strands.  The lowest-energy arrangement
**alternates** species to maximise the number of mixed
($\mathfrak{p}$--$\mathfrak{n}$) crossings, which carry the baseline
weight $\tfrac{1}{2}(q + q^{-1})$ without Coulomb excess.

When $p = n = A/2$ (even-even, $N = Z$ nuclei), perfect alternation
is possible:

$$
  \mathfrak{p}, \mathfrak{n}, \mathfrak{p}, \mathfrak{n}, \ldots,
  \mathfrak{p}, \mathfrak{n}
$$

giving $A - 1$ mixed crossings per winding, $2(A-1)$ mixed crossings
total, and **zero Coulomb excess** from the threading link.  This is
the maximal braid shortcut — the threading is purely strong-force
binding with no electromagnetic penalty.

When $p \neq n$, at least $|p - n|$ same-species adjacencies are
forced per winding.  Each such adjacency carries Coulomb excess
$\tfrac{1}{2}(q - q^{-1})$, raising the threading energy.
The Coulomb cost of the threaded nucleus is therefore

$$
  \mathcal{L}_{\mathrm{Coul}}^{\mathrm{thr}}
  \;\propto\;
  (q - q^{-1}) \cdot |p - n|,
$$

linear in the neutron excess — in contrast to the pairwise Coulomb
term, which scales as $p(p-1)/A^{1/3}$.

**Why threading stabilises.**
The threaded nucleus is more stable than the pairwise version for
the same reason the benzene ring is more stable than a chain of 6
Hopf links: the threading link is a **non-local, correlated binding
structure** that cannot be broken by any local perturbation.
Dissolving the threading requires unwinding all $A$ strands
simultaneously — a global topological operation.

The transition from pairwise to threaded is discontinuous (a
topological phase transition), just as in the molecular case
([chain-ring energy](#rem:chain-ring-energy)).  Once the threading
forms, the nucleus drops into a lower-energy basin from which
return to the pairwise state is topologically forbidden without
supplying the full Alexander weight difference
$\sim A - \Delta_{T(2,A)}(q) \approx A/2$.
