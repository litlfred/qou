Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
substrate parameter $q$
([quantum observable universe](#def:quantum-observable-universe)).
Let $\hat{V}_i^{\mathrm{full}}$ denote the additive Wedderburn traced
volume at generator $i$
([three-invariant mass formula](#sec:atomic-braid-mass)).

### Algebraic form

Via the Kashaev volume--density reading
([Kashaev volume--density](#rem:kashaev-volume-density)), the tower
admits a compact algebraic statement: *for every braid
$\beta \in B_{n}$ with $n - 1$ generators,*

$$
  \mathfrak{m}(\varrho)
  \;=\;
  \rho_{q} \cdot
  \mathrm{Vol}_{q}^{\mathrm{tower}}(\beta),
  \qquad
  \mathrm{Vol}_{q}^{\mathrm{tower}}(\beta)
  \;\in\; \mathbb{Z}[q^{1/2}, q^{-1/2}],
$$

*where $\rho_{q} = 1/\hbar_{q}^{2}$ is the substrate density
([quantum Planck constant](#def:quantum-planck-constant)) and*

$$
  \mathrm{Vol}_{q}^{\mathrm{tower}}(\beta)
  \;=\;
  \prod_{i=0}^{n-2} \hat{V}_{i}^{\mathrm{full}}
  \;+\;
  \sum_{\emptyset \neq S \subseteq \{0,\ldots,n-2\},\;\lvert S \rvert \leq 2}
    z^{\lvert S \rvert}
    \cdot \mathrm{Vol}_{q}^{(S)}(\beta),
$$

*with each $\mathrm{Vol}_{q}^{(S)}(\beta) \in \mathbb{Z}[q^{1/2},
q^{-1/2}]$ a Markov trace over the transfer-matrix chain supported on
$S$
([Markov trace product](#thm:markov-trace-product)), and $z = 1/(q^{1/2}
+ q^{-1/2})$ the Markov parameter.*

Every per-generator contribution is a finite Laurent polynomial in $q$;
no quantum-dilogarithm evaluation is required to **state** the tower.
The archimedean realisation $\mathrm{Vol}_{q}^{(S)} \rightsquigarrow
\Phi_{q}$ is a specialisation via the Kashaev limit, recorded in the
expanded form below.

### Quantum-dilogarithm form (archimedean specialisation)

Let $\Phi_q(z) = \prod_{k=1}^{\infty}(1 - q^{-k}z)^{-1}$ denote
the non-perturbative quantum dilogarithm
([quantum Bloch group](#def:quantum-bloch-group)).

**Trace-vs-evaluation note (added 2026-05-03).**
The R-side algebraic form of the tower above expresses each
$\mathrm{Vol}_q^{(S)}(\beta)$ as a Markov trace over the chain on $S$
— each term is therefore Markov-invariant.  The archimedean
specialisation $\mathrm{Vol}_q^{(S)} \rightsquigarrow \Phi_q$ below
replaces this trace with $\Phi_q(|\hat V_i^{\mathrm{full}}|)$, which
evaluates the dilogarithm on a per-generator amplitude.  Per-generator
amplitudes are **not** Markov-invariant — different reduced words for
the same braid give different per-generator amplitudes — so the
literal $\Phi_q(|\hat V_i|)$ form is a basis-dependent expansion, not
itself a trace.  At $q_0 \approx 1.11$ the divergence of $\Phi_q$
near $|\hat V_i| \to 1$ amplifies tiny p/n asymmetries into hundreds
of MeV (mirror nuclei T = 1p+2n vs $^3$He = 2p+1n predict T − $^3$He
$\approx -737$ MeV against CODATA $+0.019$ MeV; see
`brane-tower-isospin-diagnosis.witness.json`).

**Trace reformulation (Plancherel series).**
The Heine identity recovers Markov-invariance term-by-term:

$$
  \Phi_q(z) \;=\; (1 - z) \cdot \sum_{n \geq 0} \frac{z^n}{(q^{-1}; q^{-1})_n},
  \qquad (q^{-1}; q^{-1})_n = \prod_{k=1}^{n}(1 - q^{-k}).
$$

With $z = |\hat V_i^{\mathrm{full}}|$ and the standard recognition of
$|\hat V_i|^n$ as the $n$-th power evaluation of the per-generator
transfer-matrix chain, each $z^n$ summand factors through
$\mathrm{tr}_M(\sigma_i^n)$ — which IS Markov-invariant.  See
`brane_tower_plancherel_scaffold.py` for a numerical scaffold; the
production wiring depends on PR #526's term-trace infrastructure.
An equivalent Kähler-derivative reformulation is available via
`kahler_lift.py` (recursion fix landed in PR #526).

**Proposition.**
*The mass of a vortex $\varrho$ with braid representative
$\beta \in B_n$ and $n - 1$ generators is*

$$
  \mathfrak{m}(\varrho)
  =
  \Bigl\lvert \prod_{i=0}^{n-2} \hat{V}_i^{\mathrm{full}} \Bigr\rvert
  +
  \sum_{i=0}^{n-2}
    \Phi_q\!\bigl(\lvert\hat{V}_i^{\mathrm{full}}\rvert\bigr)
  +
  \sum_{0 \leq i < j \leq n-2}
    z^2 \cdot \Phi_q\!\bigl(\lvert\hat{V}_i^{\mathrm{full}}
      \cdot \hat{V}_j^{\mathrm{full}}\rvert\bigr),
$$

*where $z = 1/(q^{1/2} + q^{-1/2})$ is the Markov parameter
([Jones--Markov trace](#thm:jones-markov-trace)).*

*The three sums correspond to the three types of blow-up centre
in the brane tower
([topological decomposition](#thm:topological-mass)):*

1. *The **descended term** $\lvert\prod \hat{V}_i\rvert$ is the
   base-level Markov trace
   ([categorical mass as Markov trace](#prop:categorical-mass-markov)).*
2. *Each **single-generator blow-up** at generator $i$ contributes
   $\Phi_q(\lvert\hat{V}_i\rvert)$.  (The Markov weight
   $\mathrm{tr}_M(\sigma_i) = z$ is already absorbed into the
   traced volume $\hat{V}_i$, which is computed via the Markov
   trace of the transfer chain.)*
3. *Each **pair blow-up** at the product $\sigma_i\sigma_j$
   (any $i < j$) contributes
   $z^2 \cdot \Phi_q(\lvert\hat{V}_i \hat{V}_j\rvert)$, weighted by
   $\mathrm{tr}_M(\sigma_i\sigma_j) = z^2$.*

*The weight $z^2$ holds for every pair $(i, j)$ with $i < j$ by
the Markov-trace factorization theorem
([Markov trace factorization](#thm:markov-trace-factorization)):
for adjacent generators ($\lvert i - j\rvert = 1$) it reduces
$\sigma_i\sigma_j$ via the Hecke braid relation and applies the
Markov property $\mathrm{tr}_M(x\sigma_{n-2}) = z\,\mathrm{tr}_M(x)$;
for non-adjacent generators ($\lvert i - j\rvert \geq 2$)
far-commutativity makes $\sigma_j$ the rightmost active generator,
and the Markov property peels first $\sigma_j$ then $\sigma_i$ — two
successive Markov reductions each contributing a factor $z$, giving
$\mathrm{tr}_M(\sigma_i\sigma_j) = z^2$.  In both cases the pair
supports an independent blow-up centre at the product spectral
coordinate $\hat{V}_i\hat{V}_j$.*

*The element $\sigma_i\sigma_j\sigma_i$
($\lvert i - j\rvert = 1$) reduces via the Yang--Baxter relation
to $\sigma_j\sigma_i\sigma_j$ and does not contribute an independent
order-3 centre; such triple interactions ascend to the next jet
level ([jet-tower reformulation](#rem:mass-endomorphism-jet-tower))
rather than appearing as explicit cubic terms.*

*Proof.*
The Hecke mass element $\Phi_{\mathrm{mass}}(\beta) \in H_n(R, q)$
([Hecke mass element](#def:hecke-mass-element)) decomposes via the
descent involution into descended and transient contributions.  The
transient trace localises to blow-up centres $p$ in the brane tower
([topological decomposition](#thm:topological-mass)); integrating the
$q$-deformed expansion flow $\ln_q(1+t)/t$ along the radial
coordinate of the Briggs--Klein chart
([Briggs--Klein chart](#def:briggs-klein-chart)) over each resolved
defect $E_i \cong \mathbb{P}^1(\mathbb{C})$ yields the quantum
dilogarithm
([quantum dilogarithm as localised torsion volume](#cor:quantum-dilogarithm)):

$$
  \Phi_q(z_p) \;=\; \int_0^{z_p} \frac{\ln_q(1+t)}{t}\,dt
             \;=\; \prod_{k\geq 1}(1 - q^{-k} z_p)^{-1},
$$

where $z_p$ is the spectral coordinate of the blow-up centre.

The NF basis of $H_n(R, q)$ decomposes by generator content.  Each
subset $S \subseteq \{0,\dots,n-2\}$ contributes a blow-up centre
with spectral coordinate $\prod_{i\in S}\hat{V}_i$ and Markov
weight $z^{|S|}$; triples and higher generator subsets are not
independent at level $n$ (they ascend to jet level $n+1$ via the
pentagon closure of $\Phi_q$, see
[quantum Bloch group](#def:quantum-bloch-group)).  The independent
order-1 and order-2 subsets enumerate exactly the singleton and
pair sums above.

For the adjacent pair $\{i, i+1\}$ the NF elements
$\sigma_i\sigma_{i+1}$ and $\sigma_{i+1}\sigma_i$ share the same
spectral support $\hat{V}_i\hat{V}_{i+1}$ (the same blow-up centre,
distinct elements of $H_n(R, q)$ modulo Yang--Baxter); their combined
weight is $z^2$, not $2z^2$.  For a non-adjacent pair
$\{i, j\}$ with $\lvert i-j\rvert\geq 2$ far-commutativity gives
$\sigma_i\sigma_j = \sigma_j\sigma_i$ and
$\mathrm{tr}_M(\sigma_i\sigma_j) = z \cdot z = z^2$ — a single NF
element supporting a single blow-up centre.  In every case the
combined pair weight is $z^2$.  Summing over all pairs $i<j$ gives
the claimed quadratic term.

The element $\sigma_0\sigma_1\sigma_0$ is not an independent blow-up
centre: it decomposes as $\sigma_1\sigma_0\sigma_1$ via Yang--Baxter,
the same transient support as the adjacent pair.  Higher-order
subsets of size $\geq 3$ are similarly subsumed — not into level-$n$
singletons and pairs, but into the level-$(n{+}1)$ jet contribution
via the pentagon identity of the quantum dilogarithm (for the
explicit ascension see [jet-tower reformulation](#rem:mass-endomorphism-jet-tower)).
$\square$

## Application to the proton--electron mass ratio

For the electron (trefoil $\sigma_1^3$ on $2$ strands,
$1$ generator, additive Wedderburn
$\hat{V}_e^{\mathrm{full}} \approx 0.594$):

$$
  \mathfrak{m}_e
  =
  \lvert\hat{V}_e\rvert
  + \Phi_q(\lvert\hat{V}_e\rvert).
$$

For the proton ($\mathcal{B}_3 \times \mathfrak{u}\mathfrak{u}\mathfrak{d}$
with gluon self-coupling on $3$ strands, $2$ generators,
$\hat{V}_0^{\mathrm{full}} \approx 0.989$,
$\hat{V}_1^{\mathrm{full}} \approx 0.971$):

$$
  \mathfrak{m}_{\mathfrak{p}}
  =
  \lvert\hat{V}_0\hat{V}_1\rvert
  + \Phi_q(\lvert\hat{V}_0\rvert)
  + \Phi_q(\lvert\hat{V}_1\rvert)
  + z^2 \cdot \Phi_q(\lvert\hat{V}_0\hat{V}_1\rvert).
$$

The proton's $11$ crossings (from the $4$-channel production vertex
$\gamma\gamma \to \mathfrak{q}\bar{\mathfrak{q}}$,
[photon channel chain](#rem:photon-channel-wedderburn-chain)) produce
spectral coordinates near $1$, where $\Phi_q$ diverges.  The
electron's $3$ crossings produce $\hat{V}_e \approx 0.594$, well
below the singularity.  The mass ratio is:

$$
  \frac{\mathfrak{m}_{\mathfrak{p}}}{\mathfrak{m}_e}
  \approx 1870
  \qquad (\text{CODATA: } 1836.15, \;\text{error } 1.8\%).
$$

No parameters are fitted.  The inputs are the substrate parameter
$q_0$ and the electron mass $m_e$ (energy scale).

## Gluon derivation from the integer LP dual

The proton's $11$ crossings decompose as $6$ (Borromean
$\mathcal{B}_3$) $+ 3$ (quark Garside $\Delta_3$) $+ 2$ (gluon).
The gluon count is **derived** from the integer LP dual:

1. **LP instability.**  The $9$-crossing element
   $\mathcal{B}_3 \times \Delta_3(\mathfrak{u}\mathfrak{u}\mathfrak{d})$
   violates Frobenius positivity: $(Gx)_\gamma < 0$.

2. **Integer LP.**  Enumerate all feasible integer gluon
   combinations (up to $3$ operations from
   $\{\sigma_0, \sigma_1, L_+, L_-\}$), requiring Frobenius
   stability $Gx \geq 0$ at every intermediate step.
   Among the $84$ feasible solutions, minimize $|\mathrm{tr}_M|$.

3. **Solution: $\sigma_0 \to \sigma_0$** (two bare $\sigma_0$
   crossings on generator~$0$).  This is the **unique integer
   optimum** with $|\mathrm{tr}_M| = 0.027$ — the closest
   integer point to the continuous LP boundary
   $\mathrm{tr}_M = 0$.

The shadow price is $y_\gamma = -1$: the photon channel
is the sole binding Frobenius constraint.  The gluon's role
is to push the proton from $\mathrm{tr}_M < 0$ (unstable)
to $\mathrm{tr}_M > 0$ (stable) with minimum categorical
action.

**Witness**: `mass-endomorphism.witness.json`.

**Extension beyond $|S| = 2$ (archimedean realisation).**
*The tower formula $\mathrm{Vol}_q^{\mathrm{tower}}(\beta)$ above is
truncated at subset size $|S| \leq 2$.  Higher subset sizes
$|S| \geq 3$ are accessible — but only on the archimedean side of
$\tau \colon R \hookrightarrow \mathbb{C}$ — via the
([jet-GB-PL correspondence](#prop:jet-gb-pl-correspondence)).
The $|S| = 3$ contribution corresponds to the simultaneous product
of three colour-sheet prolongations on the color-tube cubic
([baryon product from Alt](#prop:baryon-product-from-alt)), which
under the fibre functor becomes the baryon Picard–Lefschetz period
$\Pi^{(3)}$
([SW-period thimble equivalence](#prop:sw-period-thimble-equivalence)).
Higher $|S| \geq 4$ contributions correspond to higher-jet bundles
$J^p\mathcal{S}$ for $p \geq 4$ and their PL evaluations.*

*Strict archimedean split: the truncation at $|S| \leq 2$ is the
maximal $R$-side statement available without invoking PL machinery
(which is intrinsically $\mathbb{C}$-side); the extension to
$|S| \geq 3$ requires moving across $\tau$ and so is recorded as an
archimedean addendum, not as part of the $R$-side tower formula.*
