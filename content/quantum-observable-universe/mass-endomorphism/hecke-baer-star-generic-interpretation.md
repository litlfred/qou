### Co-location with the Volume Conjecture

The Kashaev–Murakami–Murakami volume conjecture
([`conj:kashaev-volume-conjecture`](#conj:kashaev-volume-conjecture))
takes $q = e^{2\pi i / N}$ for $N \to \infty$, i.e. $q$ runs over
*primitive $N$-th roots of unity*. As $N$ grows past $n$, $q$ enters
the failure locus $\mathrm{NonBaer}(H_n(q))$:

- For $N = 2k$ with $k \leq n$: $q = \zeta_{2k}$ is in the failure
  locus — Baer-* fails, Wedderburn fails, asymptotic-$N$ regime
  active.
- For $N$ very large ($N \gg n$): $q = \zeta_N$ may be *outside*
  the failure locus for the $H_n(q)$ algebra at fixed $n$ — but
  asymptotically as $N \to \infty$, the relevant Hecke order
  $n$ grows with the colored-Jones level, eventually entering the
  failure locus.

So: **the Volume Conjecture's archimedean asymptotic regime is
exactly the trajectory through the Baer-*-failure locus**. The
loss of Baer-* projection-generation IS the structural mechanism
of the wall-crossing transition.

This co-location is **not coincidental** — it is the Hecke-algebra
side of the same phenomenon that makes hyperbolic 3-mfd volumes
appear at depth 2 in the period filtration: the radical at the
failure locus *is* what produces the period-class-non-trivial
elements upon archimedean specialisation. See
[`rem:vc-as-depth-2-instance`](#rem:vc-as-depth-2-instance)
for the depth-2 reading.

### Significance for B1

Combined with [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence),
the projections $\{e_\lambda\}$ become **explicit witnesses** for
Goncharov period classes: $e_{\lambda_K} \cdot \mathrm{Li}_2^q(z_K)$
under $\tau_{\mathrm{arch}}$ generates the period class
$[\mathrm{Vol}(K)] \in \mathcal{P}_2 / \mathcal{P}_1$ for any
hyperbolic knot $K$ with dominant cell $\lambda_K$ and shape
parameter $z_K$. The figure-8 instance: $e_{(2,2)} \cdot \mathrm{Li}_2^q(\zeta_6)$.
