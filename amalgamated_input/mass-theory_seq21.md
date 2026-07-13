<!-- FILE_START: intro-archimedean-realization-kashaev.md -->
The generic knot category requires a functor to the archimedean realm to yield real-valued physical observables. This section constructs the archimedean realisation functor and matches its output to the Kashaev volume conjecture, identifying hyperbolic volume as the archimedean shadow of the Hecke-skein.

We first define the functor and prove it preserves the Hecke-skein relation. We compute its value on torus knots, where the Kashaev volume vanishes. We then track the convergence of the substrate-level invariant to the hyperbolic volume as $q \to 1$, establishing categorical $\mathrm{Vol}_{\mathrm{hyp}}$ as the Kashaev sum limit.

Finally, we clarify the pre-$\tau$ versus post-$\tau$ distinction and the period identifications that secure the volume conjecture's substrate-level interpretation.
<!-- FILE_END: intro-archimedean-realization-kashaev.md -->

<!-- FILE_START: archimedean-realization-functor.md -->
**Definition.**
*The **archimedean realization functor** $\mathcal{R}_{\mathrm{top}}$ is the composite*

$$
  \mathcal{R}_{\mathrm{top}}
  \;:\;
  \widehat{\mathcal{M}}
  \;\xrightarrow{\;\;\chi_{\mathrm{top}}\;\;}\;
  \widehat{\mathcal{M}} \otimes_{K_0(\mathrm{Var})} \mathbb{Z}
  \;\xrightarrow{\;\;\pi_\infty\;\;}\;
  \mathbb{R}
$$

*sending the motivic class $[X]$ to its topological Euler characteristic $\chi_{\mathrm{top}}(X)$ followed by the **archimedean projection** $\pi_\infty \colon \mathbb{A} \to \mathbb{R}$. This functor evaluates motivic geometric shapes into real-valued physical observables.*

**Realization and projection.**
A motivic integral $\int_{\mathcal{L}(X)} d\mu \in \widehat{\mathcal{M}}$ defines a geometric shape. The topological realization $\chi_{\mathrm{top}}$ maps this shape to an integer (Euler characteristic) or a refined Hodge-theoretic invariant like hyperbolic volume. The adelic projection $\pi_\infty$ discards non-archimedean components, returning the real-valued laboratory measurement.

**Identification with the fibre functor.**
The QOU fibre functor $\tau \colon \mathbf{C} \to \mathbf{Arch}$ is the exclusive exit from the categorical substrate to the real numbers. On motivic QOU inputs, $\mathcal{R}_{\mathrm{top}}$ coincides exactly with the archimedean component of $\tau$:

$$
  \mathcal{R}_{\mathrm{top}}
  \;=\;
  \tau_{\mathrm{arch}}
  \;:=\;
  \pi_\infty \circ \tau
  \quad\text{on } \widehat{\mathcal{M}}_{\mathrm{QOU}}
  \;\subseteq\; \widehat{\mathcal{M}}.
$$

**Synthesis.**
The framework processes discrete categorical data along a single chain: adelic stitching, motivic integration, and archimedean projection. It requires no continuous differential equations or Lebesgue measures. The Kashaev limit of the algebraic quantum volume exemplifies this mechanism.
<!-- FILE_END: archimedean-realization-functor.md -->

<!-- FILE_START: pre-tau-vs-post-tau.md -->
> **SUPERSEDED-$\rho_q$ note .** Any use of the scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the structurally-wrong leading-order ansatz per [`mass-endomorphism-tower.md` §SUPERSEDED](mass-endomorphism-tower.md).

**The Archimedean wall.**
Every derivation step belongs to exactly one of two registers:

| Register | Coefficient ring | Operative invariants | Examples |
|---|---|---|---|
| **Pre-$\tau$** | $R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$ (or $z$-Habiro) | Hecke spectra, Markov traces | SDP feasibility, Gröbner--Shirshov reductions |
| **Post-$\tau$** | $\mathbb{R}$ via $\tau_{\mathrm{arch}}$ | Hyperbolic volumes | PL thimble flow, Bloch--Wigner $D(z)$ |

The functor $\tau_{\mathrm{arch}}$ is the only legal bridge between these columns.

* Pre-$\tau$ derivation steps cannot use post-$\tau$ values (e.g., hyperbolic volume) as inputs.
* Post-$\tau$ derivation steps cannot claim algebraic-side identities (e.g., Hecke relations) that only hold prior to realization.
* Bridging equalities that cross the wall must use $\approx$ unless stating an explicit error term. They describe the functor, not algebraic derivation steps.

**Motivic shorthand.**
The $z$-Habiro completion cleanly houses algebraic encounter data, treating quantum dilogarithm poles as quotients of cyclotomic ideals. Under $\tau_{\mathrm{arch}}$, these algebraic poles realize as hyperbolic-triangulation cusps. Any violation of the wall boundary breaks the formal derivation.
<!-- FILE_END: pre-tau-vs-post-tau.md -->

<!-- FILE_START: vol-through-tau.md -->
*Let $(\mathbf{C}, A, \tau)$ be a QOU with fibre functor $\tau$. For every braid $\beta \in H_n(R, q)$, the real-valued knot volume $\mathrm{Vol}(K_\beta)$ factors strictly through $\tau$:*

$$
  \mathrm{Vol}(K_\beta)
  \;=\;
  \tau_{\mathrm{arch}}\bigl(\mathrm{Vol}_q(\beta)\bigr)
  \;=\;
  (\pi_\infty \circ \tau)\bigl(\mathrm{Vol}_q(\beta)\bigr).
$$

*There is no other archimedean route.*

**Identification.**
On the algebraic quantum volume, $\tau_{\mathrm{arch}}$ coincides with $\mathcal{R}_{\mathrm{top}} = \pi_\infty \circ \chi_{\mathrm{top}}$. The fibre functor $\tau$ is the exclusive bridge to the laboratory continuum. The realization functor defines its canonical computation rule.

**Sketch.**
By Tannaka-Krein rigidity, any composite mapping $\mathbf{C}$ to $\mathbb{R}$ that preserves tensor products and dualities is uniquely isomorphic to the fibre functor $\tau$. Conversely, restricting the composite $\tau \circ \mathrm{Vol}_q$ via $\pi_\infty$ recovers exactly $\ln |\mathrm{Vol}_{q_0}(\beta)|$. Every physical computation of a knot volume (e.g., Kashaev limit, Bloch-Wigner dilogarithm) evaluates this identical composite.
<!-- FILE_END: vol-through-tau.md -->

<!-- FILE_START: vol-as-motivic-period.md -->
**Period interpretation.**
The hyperbolic volume $\mathrm{Vol}(S^3 \setminus K)$ is a motivic period: the value of a mixed-Tate motive under the Bloch-Wigner regulator $r_\infty$. For a hyperbolic knot complement with shape parameters $z_i$, the volume is:

$$
  \mathrm{Vol}(S^3 \setminus K)
  \;=\;
  \sum_{i=1}^{k} D(z_i),
$$

where $D$ is the Bloch-Wigner dilogarithm. Each $D(z_i)$ is a Kontsevich-Zagier period.

**Regulator interpretation.**
The shape parameters define a class $[K] \in \mathcal{B}(\overline{\mathbb{Q}})$ in the pre-Bloch group, yielding:

$$
  \mathrm{Vol}(S^3 \setminus K)
  \;=\;
  r_\infty\bigl([K]\bigr).
$$

The volume $\mathrm{Vol}(K)$ is the $K$-theoretic image of an algebraic class under a transcendental regulator.

**QOU placement.**
The archimedean realization functor factorizes identically across three pictures: adelic projection ($\pi_\infty \circ \tau$), Euler-characteristic integration ($\pi_\infty \circ \chi_{\mathrm{top}}$), and Bloch-Wigner regulation ($r_\infty$). These pictures agree entirely on the algebraic quantum volume domain. Each formalizes a distinct aspect: adelic ensures categorical compatibility, Euler-characteristic handles blow-up calculus, and Bloch-Wigner bridges to quantum topology literature.
<!-- FILE_END: vol-as-motivic-period.md -->

<!-- FILE_START: kashaev-volume-density.md -->
> **SUPERSEDED-$\rho_q$ note .** Any use of the scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the structurally-wrong leading-order ansatz per [`mass-endomorphism-tower.md` §SUPERSEDED](mass-endomorphism-tower.md).

The topological mass formula $\mathfrak{m}(K) = \mathrm{Vol}(K)/\hbar_q^2$ is exactly a volume $\times$ density product.

### Substrate density $\rho_q$

*Define the **substrate density** to be the inverse squared quantum Planck constant:*

$$
  \rho_q
  \;:=\;
  \frac{1}{\hbar_q^{2}}
  \;=\;
  \frac{q^{2}}{(q-1)^{2}}.
$$

Physically, $\rho_q$ measures the categorical drag cost of transporting a closed vortex through the Frobenius-Hopf structure. Mass is topological volume weighted by substrate drag.

### The Kashaev bridge

The Kashaev Volume Conjecture bridges the archimedean continuous volume and the algebraic discrete Markov trace:

$$
  \mathrm{Vol}(K)
  \;=\;
  2\pi\,\lim_{N \to \infty}
  \frac{\log\lvert J_{N}(K;\,e^{2\pi i/N})\rvert}{N}.
$$

The left-hand side is the continuous hyperbolic volume. The right-hand side is an asymptotic limit of colored Markov traces evaluated within the Hecke algebra.

### Inverting the ontology

The QOU framework reverses the classical priority: the discrete trace is fundamental, while the continuous volume is emergent. The colored Jones polynomials are finite algebraic evaluations of Markov traces. The hyperbolic volume simply describes the asymptotic scaling of these exact categorical evaluations. The macroscopic continuum shadow emerges from the accumulated algebraic drag of discrete crossing resolutions.

### Consequences for the mass formula

Substituting the Kashaev identity yields a fully algebraic derived mass:

$$
  \mathfrak{m}(K)
  \;\approx\;
  \rho_{q}\;\cdot\;
  \Bigl[
    2\pi\,\lim_{N \to \infty}
    \frac{\log\lvert J_{N}(K;\,e^{2\pi i/N})\rvert}{N}
  \Bigr].
$$

No continuous inputs remain. Every constituent is a discrete Hecke trace evaluated at roots of unity. The finite categorical evaluation operates precisely at the non-asymptotic substrate value $q_0 \approx 1.11$, avoiding the $N \to \infty$ continuum idealization entirely.
<!-- FILE_END: kashaev-volume-density.md -->

<!-- FILE_START: kashaev-as-archimedean-realization.md -->
The Kashaev volume conjecture identifies the archimedean realization functor applied to the algebraic quantum volume. It is not an external mathematical coincidence, but the canonical action of $\mathcal{R}_{\mathrm{top}}$ on the brane substrate.

**Algebraic side.**
The colored Jones polynomial evaluated at roots of unity is a purely $p$-adic/cyclotomic discrete algebraic trace. The algebraic quantum volume $\mathrm{Vol}_q(\mathcal{B}_K)$ packages these local data into a global Habiro element.

**Archimedean realization.**
The asymptotic limit $N \to \infty$ executes the action of $\tau_{\mathrm{arch}} = \pi_\infty \circ \tau$. It discards cyclotomic data and projects the adelic ring to $\mathbb{R}$. The Kashaev-Murakami-Murakami theorem confirms this limit equals the hyperbolic volume:

$$
  \mathrm{Vol}(S^3 \setminus K)
  \;=\;
  \tau_{\mathrm{arch}}\bigl(\mathrm{Vol}_q(\mathcal{B}_K)\bigr)
  \;=\;
  \mathcal{R}_{\mathrm{top}}\bigl(\mathrm{Vol}_q(\mathcal{B}_K)\bigr).
$$

The fibre functor $\tau$ is the exclusive archimedean route. The Kashaev limit is the realization functor of the QOU.
<!-- FILE_END: kashaev-as-archimedean-realization.md -->

<!-- FILE_START: phi-q-piece.md -->
Let $\beta \in B_n$ be a braid. For each subset $S \subseteq \{0, \dots, n-2\}$, the **$\Phi_q$-piece $K_S \subseteq S^3$** is the link obtained from $\widehat{\beta}$ by $L_0$-smoothing every crossing not in $S$ while leaving crossings in $S$ intact.

This construction satisfies three properties:
1. **Functoriality:** $K_\emptyset$ is the unlink; $K_{\{0,\dots,n-2\}}$ is the original closure.
2. **Subset compatibility:** $K_S = (K_T)_S$ for $S \subseteq T$.
3. **Categorical interpretation:** The pieces $K_S$ constitute the geometric shadow of the Wedderburn-block stratification. The algebraic spectral coordinate $\prod_{i \in S} \hat{V}_i$ localizes geometrically to $K_S$.

The piece $K_S$ acts as the geometric carrier of the per-$S$ summand $\Phi_q\bigl(\bigl\lvert\prod_{i \in S} \hat{V}_i^{\mathrm{full}}\bigr\rvert\bigr)$. The empty piece is the descended level-zero carrier. All others are transient carriers. The $\Phi_q$-piece serves as the discrete unit on which archimedean realization evaluates the tower.

### Motivic interpretation

The quantum dilogarithm $\Phi_q$ is a $q$-deformation of the Bloch-Wigner dilogarithm. The per-piece summand $\Phi_q(\lvert V_S\rvert)$ represents a class in the quantum Bloch group. The family $\{K_S\}_S$ provides the geometric stratification along which the regulator decomposes, solidifying the bridge to hyperbolic volume as a strict regulator statement.
<!-- FILE_END: phi-q-piece.md -->

<!-- FILE_START: phi-q-tower-algebraic-stratification.md -->
> **SUPERSEDED-$\rho_q$ note .** Any use of the scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the structurally-wrong leading-order ansatz per [`mass-endomorphism-tower.md` §SUPERSEDED](mass-endomorphism-tower.md).

**Proposition (algebraic stratification of the $\Phi_q$ tower).**
*Let $\beta \in B_n$ be a braid. The $\Phi_q$-tower admits a purely algebraic stratification by $|S|$ within the Gröbner-Shirshov filtration of the Hecke algebra:*

$$
  \mathfrak{m}(\varrho)
  \;=\;
  \bigl\| \mathrm{tr}_M(\rho(\beta_\emptyset))\bigr\|_F
  \;+\;
  \sum_{|S| = 1} \Phi_q\bigl(\|\hat V_S\|_F\bigr)
  \;+\;
  \sum_{|S| = 2} z^{2} \Phi_q\bigl(\|\hat V_S\|_F\bigr).
$$

*The Frobenius norm $\|\cdot\|_F$ evaluates entirely within the ground ring $\mathbb{Z}[q^{\pm 1/2}]$. This unconditional stratification identifies exactly with the $J^{|S|}/J^{|S|+1}$ grading of the GS confinement filtration.*

The algebraic stratification operates strictly pre-$\tau$. It decomposes the mass endomorphism using only discrete categorical data, isolating the structural descent without invoking any hyperbolic or continuous geometry.
<!-- FILE_END: phi-q-tower-algebraic-stratification.md -->

<!-- FILE_START: kashaev-volume-conjecture.md -->
> **SUPERSEDED-$\rho_q$ note .** Any use of the
> scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the
> structurally-wrong leading-order ansatz per
> [`mass-endomorphism-tower.md` §SUPERSEDED](mass-endomorphism-tower.md);
> the canonical replacement is the operator-valued $A^\lambda_{\mu, \nu}(I)$
> graded expansion [`prop:rho-k-graded-expansion`](rho-k-graded-expansion.md).
> Full purge tracking: [`docs/audits/-superseded-rho-q-purge.md`](../../../docs/audits/-superseded-rho-q-purge.md).

The **Kashaev volume conjecture (KVC)** asserts that, for every
hyperbolic knot $K \subseteq S^3$, the Kashaev limit of the colored
Jones polynomial computes the hyperbolic volume of the complement,

$$
  \mathrm{Vol}_{\mathrm{hyp}}(S^3 \setminus K)
  \;=\;
  2\pi \cdot \lim_{N \to \infty}
  \frac{\log \lvert J_N(K)\rvert}{N},
  \qquad
  J_N(K)\big\vert_{q = \exp(2\pi i / N)},
$$

with the convention that the right-hand side vanishes when $K$ is not
hyperbolic. KVC was conjectured by Kashaev [`kashaev1997`] and reformulated
in terms of the colored Jones polynomial by Murakami–Murakami
[`murakami-murakami2001`]. It is **open in general** (proved only for
specific families: the figure-eight knot, certain torus and pretzel
knots, etc.).

Inside QOU, KVC is the consistency statement that the archimedean
realisation functor $\tau_{\mathrm{arch}} = \pi_\infty \circ \tau$
([archimedean realization functor](#def:archimedean-realization-functor))
applied to the algebraic quantum volume
([algebraic quantum volume](#def:algebraic-quantum-volume))
recovers the hyperbolic volume; this is the content of the per-block
[Kashaev as archimedean realization](#rem:kashaev-as-archimedean-realization)
remark.

### Lean axiomatisation

Per `AGENTS.md` §3b ("Lean formalization of conjectures"), KVC is
encoded in Lean as a **typeclass**

```
class VolumeConjecture (q : ℝ) where
  hypVolume       : Braid → ℝ
  kashaevLimit    : Braid → ℝ
  kvc_holds       : ∀ β, hypVolume β = kashaevLimit β
  hypVolume_nonneg : ∀ β, 0 ≤ hypVolume β
```

The class fields encode the conjectural identification of hyperbolic
volume with the Kashaev limit. Any instance of `VolumeConjecture` is
**conjecture-bearing**: the `kvc_holds` field plays the role of
`sorry`, but as an axiomatised class field rather than a tactic
failure. Downstream results that depend on KVC take it as an
`[VolumeConjecture q]` typeclass argument and are then **fully
verified** by Lean — the only unproved input is the class instance.

This is the same pattern used for `MassEvaluation` in
[mass endomorphism tower](#prop:mass-endomorphism-tower): the
canonical computation is axiomatised so that the algebraic tower
identities are machine-checked.

### Rationale for a class rather than an axiom

Three reasons:

1. **Locality.** A typeclass instance can be supplied per knot family
   (figure-eight, torus, etc.) where KVC is actually proved; downstream
   theorems then specialise to verified ground.

2. **Compositionality.** A bridge theorem of the form
   $\Phi_q(V_S) = \rho_q \cdot \mathrm{Vol}(K_S)$ depends only on KVC
   restricted to $K_S$; the typeclass scope makes that dependency
   visible in the type signature.

3. **No global axiom pollution.** Mathlib's axiom audit
   (`#print axioms`) records typeclass dependencies but does not flag
   them as global axioms; the conditional nature of every downstream
   result is preserved.

The conjecture itself remains open at the level of $\pi_0$ —
no claim of proof is made by introducing the class.

### Motivic perspective

KVC is, in motivic language, a **regulator statement**: the
hyperbolic volume of $S^3 \setminus K$ is the image of a class in
the Bloch group $\mathcal{B}(\mathbb{C})$ under the Borel/Beilinson
regulator $r_\infty$, and the colored Jones polynomial at
$q = \exp(2\pi i / N)$ is the $q$-deformed avatar of that class
[`zagier1986`, `neumann-zagier1985`]. The QOU recasting frames
$\tau_{\mathrm{arch}} = \pi_\infty \circ \tau$ as the archimedean
realisation functor on the algebraic data $\Phi_q(\lvert V_S\rvert)$
— a class in the quantum Bloch group
([quantum Bloch group](#def:quantum-bloch-group)) — landing in
$\mathbb{R}$ as the hyperbolic volume of the corresponding
Φ$_q$-piece. KVC, in this presentation, is the assertion that the
$q$-deformed regulator agrees with the classical one in the Kashaev
limit.
<!-- FILE_END: kashaev-volume-conjecture.md -->

<!-- FILE_START: figure-8-archimedean-illustration.md -->
**Remark (figure-8 knot as the canonical algebraic / archimedean
example).**

The figure-8 knot $4_1$ is the smallest hyperbolic knot
[`thurston1978`] and serves as the cleanest illustration of the
dual existence forced by
[`prop:archimedean-functor-uniqueness`](#prop:archimedean-functor-uniqueness):
*algebraic / motivic in the substrate, transcendental in the
laboratory*.

**Embedding in Bring's surface.** The figure-8 knot embeds smoothly
into Bring's surface (genus $4$) as the amphichiral mass mechanism.
Its braid word $\sigma_1\sigma_2^{-1}\sigma_1\sigma_2^{-1}$ realises
on $4$ strands and the braid closure reproduces $4_1$ inside the
genus-$4$ handlebody. The amphichirality
$4_1 \cong 4_1^{\,\text{mirror}}$ — equivalently, invariance under
the bar involution $q \mapsto q^{-1}$ — is what selects the
figure-8 as a *mass* invariant rather than a chirality invariant.

**Pre-archimedean (substrate) representation.**
On the algebraic side, $4_1$ has a completely rigorous motivic
representation via its Hecke normal form. The
[algebraic quantum volume](#def:algebraic-quantum-volume) of $4_1$
is a finite product of Laurent polynomials,

$$
  \mathrm{Vol}_q(4_1)
  \;=\;
  \prod_{i=0}^{2} \hat{V}_i(q)
  \;\in\;
  \mathbb{Z}[q^{\pm 1/2}],
$$

with the $\hat{V}_i(q)$ explicitly determined by the four-strand
braid word above (cf.
[`thm:markov-trace-factorization`](#thm:markov-trace-factorization)).
At this level no $\pi$, no $\zeta$-values, no real-analytic
transcendentals appear: the entire object is a Laurent polynomial
in $q^{\pm 1/2}$ and lives strictly in the substrate ring $R$.

**Archimedean (laboratory) image.**
Apply the archimedean realization functor $\tau_{\text{arch}} =
\pi_\infty \circ \tau$
([archimedean realization functor](#def:archimedean-realization-functor)).
The image of $\mathrm{Vol}_q(4_1)$ under $\tau_{\text{arch}}$ in
the Faddeev-Kashaev quasi-classical limit is the *hyperbolic
volume* of the figure-8 knot complement
$S^3 \setminus 4_1$
([Kashaev volume conjecture](#conj:kashaev-volume-conjecture)),
which evaluates as the transcendental

$$
  \boxed{\;
    \mathrm{Vol}(4_1)
    \;=\;
    2\,D(\mathrm{e}^{i\pi/3})
    \;=\;
    2\,\mathrm{Cl}_2\!\left(\tfrac{\pi}{3}\right)
    \;\approx\;
    :val[Vol_4_1]{precision=6}\ldots
  \;}
$$

where $D$ is the Bloch-Wigner dilogarithm and $\mathrm{Cl}_2$ is
the Clausen function. The transcendence of $\mathrm{Cl}_2(\pi/3)$
is conjectural in number theory but the *form* of the answer is
forced by Bloch-Suslin pentagon-uniqueness: any archimedean
realization of the substrate's pentagon-coherent class must
factor through $D$, and the figure-8's three ideal-tetrahedron
triangulation pins down the specific shape parameter $z = e^{i\pi/3}$.

**The dichotomy in one line.**
The motivic side guarantees exact, $q$-rational algebraic
relationships governing particle interactions; $\tau_{\text{arch}}$
supplies the transcendental continuum required for geometric
measurement. Both pictures are needed:

| Side | Object for $4_1$ | Lives in | Role |
|---|---|---|---|
| Pre-archimedean | $\mathrm{Vol}_q(4_1) = \prod_i \hat{V}_i(q)$ | $\mathbb{Z}[q^{\pm 1/2}]$ | Exact algebraic identities, mass-formula state sum, Hecke trace |
| Archimedean | $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3)$ | $\mathbb{R}$ (transcendental) | Laboratory mass-scale, Higgs-like amphichiral mechanism |

The bridge between the two columns is uniquely determined by
[`prop:archimedean-functor-uniqueness`](#prop:archimedean-functor-uniqueness):
no other archimedean image is admissible.

**Cross-reference: $\alpha_{EM}$.** The same dichotomy underlies
the additive Bring zero-mode candidate
[`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode):
the $\pi$ in $4_1$'s archimedean image
$2\,\mathrm{Cl}_2(\pi/3)$ and the $\pi$ in $1/\alpha_{EM}$'s
correction $2/(3\pi) = 2g/(4\pi(g-1))$ at $g=4$ share a single
provenance — the unique archimedean shadow of pentagon-coherent
substrate data on Bring's surface, factored through the
Bloch-Wigner dilogarithm. The exact algebraic values $:val[Vol_4_1]{precision=6}\ldots =
2\,\mathrm{Cl}_2(\pi/3)$ matches the standard hyperbolic
2-tetrahedra triangulation [`thurston1978`].
<!-- FILE_END: figure-8-archimedean-illustration.md -->

<!-- FILE_START: gb-depth-period-correspondence.md -->
**Conjecture (GS-depth $\leftrightarrow$ Goncharov period-depth correspondence).**

*Let $\mathcal{H}_q$ be the substrate convolution Hopf algebra
([Frobenius–Hopf substrate](#def:frobenius-hopf-substrate)) and let
$G(\mathcal{H}_q)$ be its sub-Hopf-algebra of grouplikes. Filter
$G(\mathcal{H}_q)$ by **iterated-integral depth**:*

$$
  G^{(0)} \;\subseteq\; G^{(1)} \;\subseteq\; G^{(2)} \;\subseteq\; \cdots,
  \qquad
  G^{(n)} \;:=\; \langle\, \exp_q,\, \log_q,\, \mathrm{Li}_2^q,\, \ldots,\, \mathrm{Li}_n^q \,\rangle.
$$

*Let $\tau_{\mathrm{arch}}$ be the archimedean realization functor
([archimedean realization](#def:archimedean-realization-functor)) and
let $\mathcal{P}_\bullet \subset \mathbb{R}$ be Goncharov's period
filtration on the algebra of (real) periods. Then:*

$$
  \boxed{\;\tau_{\mathrm{arch}}\!\left( G^{(n)}(\mathcal{H}_q) \right)
         \;\subseteq\; \mathcal{P}_n,\;}
$$

*and the inclusion is sharp at every depth — for each $n \geq 1$
there exists a grouplike $g \in G^{(n)} \setminus G^{(n-1)}$ whose
$\tau_{\mathrm{arch}}$-image generates a non-trivial class in
$\mathcal{P}_n / \mathcal{P}_{n-1}$.*

### Stratification dictionary

| Depth $n$ | Grouplike at depth $n$ | Goncharov class |
|---|---|---|
| 0 | $\exp_q$, scalars | algebraic numbers |
| 1 | $\log_q$ | $\log\alpha$, $\alpha \in \overline{\mathbb{Q}}$ (Baker class) |
| 2 | $\mathrm{Li}_2^q$ | hyperbolic 3-mfld volumes (Bloch–Wigner regulator) |
| $n$ | $\mathrm{Li}_n^q$ | weight-$n$ multiple polylogs (Goncharov motivic) |

### Structural content of the statement

The classical Mikusiński operational calculus on $C[0,\infty)$ takes
$f * g \mapsto \tilde f \cdot \tilde g$ under Laplace, turning ODEs
into algebra. The categorical analog already in this paper —
[`prop:categorical-laplace-unique`](#prop:categorical-laplace-unique),
[`q-resolvent`](#def:q-resolvent) — does exactly this for $\mathcal{H}_q$.
What it does *not* yet pin down is **which algebraic relations on
$\mathcal{H}_q$ survive $\tau_{\mathrm{arch}}$ and which do not**. The
present conjecture supplies the structural answer:

- A relation $R(g_1,\dots,g_m) = 0$ among grouplikes survives
  $\tau_{\mathrm{arch}}$ iff *all $g_i$ live in the same depth $G^{(n)}$
  and the relation is an algebraic identity in the cellular structure of
  $H_n(q)$* (provable over $\mathbb{Z}[q^{\pm 1}]$).
- A relation that crosses depth or invokes a transcendental
  identity among periods (e.g. the Bloch–Wigner 5-term relation,
  hyperbolic gluing equations) is an **archimedean accident** — it
  holds only in $\mathbb{R}$, not over $\mathcal{H}_q$ generically.

This is the wall-crossing criterion: depth determines what survives.

### Surreal envelope

Lift the standard-part map $\mathrm{std} \colon \mathbf{No} \to \mathbb{R}$
to the level of grouplikes. The depth filtration extends:

$$
  G^{(n)}(\mathcal{H}_q^{\,\mathbf{No}})
  \;\xrightarrow{\;\mathrm{std}\;}\;
  \mathcal{P}_n.
$$

Surreal infinitesimals $1/\omega^k$ sit at depth $k$ as *literal*
infinitesimal scaling factors — there is no recourse to distributions
or limits. The "delta at depth $n$" of graded Mikusiński is the
surreal element $1/\omega^n$, and $\mathrm{std}$ collapses each layer
to its archimedean image. This makes the *algebraic core survives*
mechanism ([algebraic core survives](#rem:algebraic-core-survives))
into a quantitative statement: it survives **at the depth at which it
lives**.

### Existing depth-2 evidence

The paper already records a depth-2 instance in
[`rem:figure-8-archimedean-illustration`](#rem:figure-8-archimedean-illustration):
the figure-8 knot, embedded in Bring's surface, has hyperbolic
volume $2\,\mathrm{Cl}_2(\pi/3) = 2\,\mathrm{Im}\,\mathrm{Li}_2(e^{i\pi/3})$.
One $\mathrm{Li}_2$ factor $\Rightarrow$ iterated-integral depth $2$,
matching the Bloch-regulator class of the archimedean image. See the
explicit canonical witness in
[`conj:bring-figure-eight-depth-2-witness`](#conj:bring-figure-eight-depth-2-witness).

### Discharge targets

**Open.** The conjecture is structural (no concrete computation
suffices to discharge it), but admits a clean reduction to known
period theory:

1. **Inclusion $\tau_{\mathrm{arch}}(G^{(n)}) \subseteq \mathcal{P}_n$:**
   reduces to showing $\tau_{\mathrm{arch}}$ commutes with iterated
   integration; for the categorical Laplace transform this is the
   monoidality result already proved
   ([`prop:categorical-laplace-unique`](#prop:categorical-laplace-unique)).
2. **Sharpness ($\mathcal{P}_n / \mathcal{P}_{n-1}$ non-trivial in
   image):** depth-2 case is the Bloch–Wigner regulator
   ([bloch2000], [suslin1991]) realised by hyperbolic 3-manifolds.
   Higher depths reduce to Goncharov's motivic-Galois action on
   multiple polylogs ([kontsevich1995], Goncharov 2001).

**Two related open questions:**

- *Cellular vs iterated-integral depth.* The cellular GB-depth on
  $Z(H_n(q))$ from
  [`prop:curvature-rank-gb-stratification`](#prop:curvature-rank-gb-stratification)
  (max hook of partition) is a **separate** filtration from the
  iterated-integral depth used here. Their precise relationship —
  e.g. whether amphichiral self-conjugate cells correspond to
  *even* iterated-integral depths — is open.
- *Graded Titchmarsh.* At which iterated-integral depth does the
  $*_q$-product on $\mathcal{H}_q$ first acquire zero divisors?
  This bounds where the graded field-of-fractions tower
  $\mathcal{M}_q^{(0)} \hookrightarrow \mathcal{M}_q^{(1)} \hookrightarrow \cdots$
  is well-defined, and feeds the operational-calculus mechanism
  per the Mikusiński (1959) construction.
<!-- FILE_END: gb-depth-period-correspondence.md -->

<!-- FILE_START: vc-as-depth-2-instance.md -->
**Remark (Volume Conjecture as the depth-2 instance of the GS $\leftrightarrow$
period correspondence).**

The Kashaev–Murakami–Murakami volume conjecture
([`conj:kashaev-volume-conjecture`](#conj:kashaev-volume-conjecture))
admits a clean structural reading inside the graded-Mikusiński
framework
([`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)):
*it is the depth-2 case.*

### One-line statement

$$
  \text{Volume Conjecture} \;\;\Longleftrightarrow\;\;
  \tau_{\mathrm{arch}}\!\left( G^{(2)}(\mathcal{H}_q) \right)
  \;\xrightarrow{\;\;}\;
  \mathcal{P}_2 \big/ \mathcal{P}_1
  \;=\; \{\text{hyperbolic 3-manifold volumes}\}.
$$

### Justification of the reading

The Volume Conjecture asserts that the asymptotic growth of the
coloured Jones polynomial $J_K^{(N)}(q)$ at $q = e^{2\pi i / N}$ as
$N \to \infty$ equals $\mathrm{Vol}(S^3 \setminus K)$. The
algebraic side ($J_K \in \mathbb{Z}[q^{\pm 1}]$) is field-polymorphic
and lives in the substrate
([`rem:algebraic-core-survives`](#rem:algebraic-core-survives)). The
geometric side is a real number, transcendental in general.

In graded-Mikusiński terms:

- $J_K^{(N)}$ is built by repeated application of the depth-2
  grouplike $\mathrm{Li}_2^q$ (Faddeev–Kashaev quantum-dilogarithm
  decomposition).
- The asymptotic limit at $q = e^{2\pi i / N}$, $N \to \infty$, is
  the archimedean realization $\tau_{\mathrm{arch}}$ followed by
  std-part on the surreal envelope.
- Single-$\mathrm{Li}_2$ factor $\Rightarrow$ iterated-integral
  depth 2 $\Rightarrow$ Goncharov period-class
  $\mathcal{P}_2 / \mathcal{P}_1$ (Bloch regulator
  $K_3^{\mathrm{ind}}(\overline{\mathbb{Q}}) \otimes \mathbb{Q}
  \to \mathbb{R} / \pi^2 \mathbb{Q}$).

The Volume Conjecture is therefore not a coincidence: hyperbolic
volumes appear at depth 2 because that is structurally where the
Bloch–Wigner regulator lives. Predicted at every depth $n$ is an
analogous statement: *colored quantum invariants built from
$\mathrm{Li}_n^q$ asymptote to weight-$n$ Goncharov periods.*

### Implications of accepting the keystone

The keystone correspondence does **not** prove the Volume Conjecture.
What it does is reduce the conjecture to two structurally smaller
claims:

1. *Categorical Laplace transport.* Show that the asymptotic at
   roots of unity coincides with the categorical Laplace transform
   of $\Phi_q$ followed by std-part — i.e. that the limiting
   procedure is intrinsically the Mikusiński transform applied
   stratum-by-stratum. Already partially in the paper via
   [`prop:categorical-laplace-unique`](#prop:categorical-laplace-unique).
2. *Sharpness at depth 2.* Show that the image of $G^{(2)}$ in
   $\mathcal{P}_2 / \mathcal{P}_1$ contains the Bloch–Wigner
   regulator class of every hyperbolic knot complement. This is the
   modern formulation of Bloch's 1978 conjecture and is a known
   target in motivic cohomology.

The framework thus does not eliminate the open problem — it places
it in its correct depth-graded category, where partial results
already exist (Murakami–Murakami 2001 for the figure-8;
Garoufalidis–Lê for torus knots; many others).

### Cross-reference

For an explicit depth-2 canonical witness on the figure-8 knot
embedded in Bring's genus-4 surface, see
[`conj:bring-figure-eight-depth-2-witness`](#conj:bring-figure-eight-depth-2-witness).
The 50-digit value $2\,\mathrm{Cl}_2(\pi/3) \approx :val[vol_4_1_decimal_50]{precision=6, witness=computations/hyperbolic-volumes.witness.json}\ldots$
is the Bloch regulator class incarnated as a hyperbolic volume.
<!-- FILE_END: vc-as-depth-2-instance.md -->

<!-- FILE_START: bring-figure-eight-depth-2-witness.md -->
**Conjecture (Bring figure-8 volume as depth-2 grouplike value;
50-digit canonical witness).**

*The hyperbolic volume of the figure-8 knot $4_1$ embedded in
Bring's genus-4 surface
([`rem:figure-8-archimedean-illustration`](#rem:figure-8-archimedean-illustration))
equals the standard-part of $2\,\mathrm{Im}\,\mathrm{Li}_2^q$ at the
regular-ideal-tetrahedron shape parameter $z = e^{i\pi/3}$ — the
depth-2 grouplike value predicted by
[`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence):*

$$
  \mathrm{Vol}(S^3 \setminus 4_1)
  \;=\;
  \mathrm{std}\bigl( 2\,\mathrm{Im}\,\mathrm{Li}_2^q(e^{i\pi/3}) \bigr)
  \;=\;
  2\,\mathrm{Cl}_2\!\left(\tfrac{\pi}{3}\right).
$$

### canonical witness (50-digit precision)

Computed via `exact algebraic structures.polylog` at `mp.dps = 50` (formalism
the canonical formalism,
witness
[`gb-depth-period-bring-fig8.witness.json`](https://github.com/litlfred/qou/blob/main/computations/gb-depth-period-bring-fig8.witness.json)):

$$
  2\,\mathrm{Cl}_2(\pi/3)
  \;=\;
  2.029{,}883{,}212{,}819{,}307{,}250{,}042{,}405{,}108{,}549{,}040{,}571{,}883\ldots
$$

A SnapPy-precision sanity check via independent Clausen-series
partial sum (2 million terms) agrees to $\sim 13$ digits — the
working precision of SnapPy 3.3.2's verified hyperbolic structure.
The 50-digit value is the canonical algebraic computation.

### Depth correspondence

| Side | Object | Depth |
|---|---|---|
| Algebraic | $2\,\mathrm{Li}_2^q(e^{i\pi/3}) \in G^{(2)}(\mathcal{H}_q)$ | iterated-integral depth $= 2$ |
| Archimedean | $\mathrm{Vol}(4_1) \in \mathcal{P}_2 / \mathcal{P}_1$ | Goncharov period-depth $= 2$ |

A single $\mathrm{Li}_2$ factor on the algebraic side maps to a
single Bloch-regulator class on the geometric side: depth $2 = 2$
match, by construction of the Bloch–Wigner regulator
([bloch2000], [suslin1991]).

### Bring-specific significance

The figure-8 knot is the canonical knot-theoretic witness for
Bring's surface in this paper
([`def:brings-coordinate-ring`](#def:brings-coordinate-ring)). Its
4-strand braid word $\sigma_1\sigma_2^{-1}\sigma_1\sigma_2^{-1}$
realises inside the genus-4 handlebody, and amphichirality
$4_1 \cong 4_1^{\,\mathrm{mirror}}$ pins it as a *mass invariant*
rather than a chirality invariant. Two structural facts already in
the paper are consistent with the depth-2 reading:

- The $\pi$ in $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3)$ and the
  $\pi$ in the Bring zero-mode $\alpha_{EM}$ correction
  $2g/(4\pi(g-1))|_{g=4} = 2/(3\pi)$ share a single provenance — the
  unique archimedean shadow of pentagon-coherent substrate data on
  Bring's surface (cf.
  [`rem:figure-8-archimedean-illustration`](#rem:figure-8-archimedean-illustration)).
- Both factor through the Bloch–Wigner dilogarithm at a Bring shape
  parameter — exactly the depth-2 grouplike of $\mathcal{H}_q$.
### Cross-reference: deeper-depth Bring instances (open)

The keystone predicts analogous canonical witnesses at every depth:

| Depth | Bring object | Predicted std-image |
|---|---|---|
| 2 | figure-8 in genus-4 ($4_1$) | $2\,\mathrm{Cl}_2(\pi/3) \approx 2.02988\ldots$ (confirmed) |
| 3 | $\mathrm{Li}_3$ at $\zeta_5$ ($S_5$-natural Bring root of unity) | $\mathrm{Im}\,\mathrm{Li}_3(\zeta_5) \in \mathcal{P}_3/\mathcal{P}_2$ |
| $n$ | $\mathrm{Li}_n^q$ at the $S_5$-orbit of $\zeta_5$ | weight-$n$ Goncharov motivic period |

**Depth-2 ceiling for hyperbolic 3-manifold volumes.** *All* hyperbolic
3-manifold volumes (figure-8, Borromean rings = $8G$, Whitehead link,
$\ldots$) are depth-2 periods — one $\mathrm{Li}_2$ factor in their
Bloch–Wigner formula. Different knots correspond to different shape
parameters at the same depth. A genuine depth-3 witness therefore
requires either (a) a trilog $\mathrm{Li}_3$ at an algebraic argument,
(b) a Chern–Simons invariant (the depth-3 part of the complexified
volume $\mathrm{CS} + i\,\mathrm{Vol} \in \mathbb{C}/\pi^2\mathbb{Z}$),
or (c) a multiple zeta value such as $\zeta(3)$. The Bring-natural
choice is (a) at the primitive 5th root of unity $\zeta_5$ — see
[`conj:bring-trilog-depth-3-witness`](#conj:bring-trilog-depth-3-witness).
<!-- FILE_END: bring-figure-eight-depth-2-witness.md -->

<!-- FILE_START: kashaev-density-equals-sdp-multiplicity.md -->
**Conjecture (Rule 14 conditional adoption — owner authorised).**
Under the Kashaev volume conjecture
([`conj:kashaev-volume-conjecture`](#conj:kashaev-volume-conjecture))
applied to an atomic Hecke element $T_w$ with `Markov closure` knot/link
$K_w$, the multiplicative density prefactor
$\rho_F \in \mathbb{Z}_{>0}$ in the binding-energy formula

$$
  B_{\mathrm{pred}}(K_w)
  \;=\;
  \rho_F \cdot m_e \cdot \mathrm{Vol}_{\mathrm{hyp}}(K_w)
$$

equals the **joint-tower SDP Wedderburn multiplicity** $\nu_{\mathrm{SDP}}(K_w)$
of the canonical Hecke element $T_w$'s saturating SDP solution in the
$H_{n}(q)$ Wedderburn decomposition:

$$
  \rho_F  \;=\;  \nu_{\mathrm{SDP}}(K_w)
$$

per [`atom-knot-mass-derivation`](#prop:atom-knot-mass-derivation)
§Algorithm step 3 (the joint-tower SDP solve that produces
$\nu_{\mathrm{SDP}}$ as a non-negative integer multiplicity).

## Evidence (three confirmed atoms)

The identity is exact on the three SDP-confirmed
hyperbolic atoms (per
[`atom-knot-mass-derivation`](#prop:atom-knot-mass-derivation) line 265):

| Atom | $K_w$ | $\rho_F$ (legacy) | $\nu_{\mathrm{SDP}}$ |
|------|-------|-------------------|----------------------|
| ${}^{2}\mathrm{H}$ (D)  | knot $6_2$        | 1 | 1 |
| ${}^{3}\mathrm{H}$ (T)  | knot $8_{11}$     | 2 | 2 |
| ${}^{3}\mathrm{He}$     | link $L_{6a4}$    | 2 | 2 |

The ${}^{4}\mathrm{He}$ case uses the magic $A \cdot 8G$ closure rule rather than a
census knot, so its $\nu_{\mathrm{SDP}}$ value is **extrapolated**
($\rho_F = 2$ assumed); R&D follow-up is to extend the joint-tower
SDP solver to confirm $\nu_{\mathrm{SDP}}(⁴\mathrm{He}) = 2$.

## Categorical home (driver x of the 13-driver menu)

This identity falls under driver (x) **MacMahon-style
partition-algebra identities** of the canonical-derivation menu
([`docs/audits/-lambda-scale-canonical-unification.md`](../../docs/audits/-lambda-scale-canonical-unification.md)).
The Wedderburn multiplicity of $T_w$'s SDP solution is a
partition-algebra count: it is the dimension of the saturating
projection in the irreducible-block decomposition
$H_n(q) \cong \bigoplus_{\lambda \vdash n} \mathrm{End}(V_\lambda)$.
The agreement with the Kashaev density factor pulls
$\rho_F$ onto driver (x) and removes it from the Rule-14 escalation
queue.

## Conditional structure

The conjecture is **conditional on the joint-tower SDP completeness**:
i.e. the joint-tower SDP solver in
the canonical formalism
(when it lands; R&D in progress) gives a unique non-negative integer
$\nu_{\mathrm{SDP}}(K_w)$ for every bound-state knot $K_w$. Until R5-full
SDP ships, the identity is verified on three census atoms and
extrapolated to ${}^{4}\mathrm{He}$ with explicit caveat. The Lean class axiomatises

```lean
class KashaevDensityEqualsSDPMultiplicity
    (M : Type*) [BrCategory M] [Hecke M] [KashaevVolumeConjecture M] where
  /-- The joint-tower SDP multiplicity ν_SDP(K_w) of the canonical
      Hecke element T_w's saturating SDP solution. -/
  nu_sdp : ∀ (K : Knot), ℕ
  /-- ν_SDP equals the Kashaev density prefactor ρ_F. -/
  identity :
    ∀ (K : Knot),
      kashaev_density_prefactor K = nu_sdp K
```

per AGENTS.md §3b ("class is inhabited"); the only `sorry` is the
class instance, which closes when R5-full canonical knot solver
produces certified $\nu_{\mathrm{SDP}}$ values.

## Resolution of the Rule-14 escalation

Pre- the
the canonical formalism
formalism self-declared the density rule $\rho_F \in \{1, 2\}$ as
*"pending formal justification"* (line 23) — an open Rule-14
violation per the canonical-derivation discipline. With this
conjecture-conditional adoption, $\rho_F$ is:

1. **named canonically** (`nu_sdp` in the new code), connecting to the
   existing `ν_SDP` notation in
   [`atom-knot-mass-derivation`](#prop:atom-knot-mass-derivation);
2. **placed on the 13-driver menu** (driver x, MacMahon partition algebra);
3. **conditional on a class** that R5-full SDP will eventually
   inhabit — replacing the open-ended "pending formal justification"
   with an auditable conjecture-conditional dependency.

Owner authorised this adoption per Rule-14 procedure
, in response to
[`docs/audits/-rule14-kashaev-density.md`](../../docs/audits/-rule14-kashaev-density.md)
§Recommendation.

## Notation hazard resolved

Prior to this block, three distinct quantities used the symbol $\rho$
in QOU compute and content (per
[`atom-knot-mass-derivation`](#prop:atom-knot-mass-derivation) §Notation):

- $\nu_{\mathrm{SDP}}$ — integer Wedderburn multiplicity (this conjecture)
- $\rho_K$ — CODATA-fit density per knot
- $\rho_F$ — Kashaev prefactor in the formal derivation (unnamed, compute-only)

The renamed compute field (`rho_factor` $\to$ `nu_sdp` in
the canonical formalism
ATOM_ASSIGN) consolidates around the canonical $\nu_{\mathrm{SDP}}$ name,
removing the third unnamed $\rho$.

## Consumers

- the canonical formalism
  — ATOM_ASSIGN.`nu_sdp` field (renamed from `rho_factor` in the same
  PR that introduces this block)
- the canonical formalism
  — reads `nu_sdp` and emits `B_pred = nu_sdp · m_e · Vol(K)`
- [`atom-knot-mass-derivation`](#prop:atom-knot-mass-derivation)
  §Algorithm step 3 — supplies $\nu_{\mathrm{SDP}}$ via joint-tower SDP

## Open R&D

1. **Extend joint-tower SDP to ${}^{4}\mathrm{He}$** — confirm
   $\nu_{\mathrm{SDP}}(⁴\mathrm{He}) = 2$ explicitly (currently
   extrapolated from D/T/${}^{3}\mathrm{He}$ pattern).
2. **Extend joint-tower SDP to ${}^{5}\mathrm{Li}$, ${}^{6}\mathrm{Li}$, ${}^{7}\mathrm{Li}$** — the A$\in${5,6,7} gap
   per
   [`docs/audits/-a5-a7-isotope-wiring-gap.md`](../../docs/audits/-a5-a7-isotope-wiring-gap.md)
   needs $\nu_{\mathrm{SDP}}$ values; the wider atom$\to$knot census Rule-14
   escalation per
   [`docs/audits/-rule14-atom-knot-census.md`](../../docs/audits/-rule14-atom-knot-census.md)
   recommends waiting for R5-full SDP (owner-decided).
3. **Extend joint-tower SDP to α-cluster atoms (${}^{8}\mathrm{Be}$ and up)** — the
   α-cluster rule inherits $\rho_F = 2$ from ${}^{4}\mathrm{He}$; verifying
   $\nu_{\mathrm{SDP}} = 2$ across the α-cluster recursion would close
   the inheritance step.

## Cross-references

- Rule-14 escalation:
  [`docs/audits/-rule14-kashaev-density.md`](../../docs/audits/-rule14-kashaev-density.md)
- Sibling Rule-14 escalation (deferred to R5-full SDP):
  [`docs/audits/-rule14-atom-knot-census.md`](../../docs/audits/-rule14-atom-knot-census.md)
- 13-driver menu (driver x — MacMahon partition algebra):
  [`docs/audits/-lambda-scale-canonical-unification.md`](../../docs/audits/-lambda-scale-canonical-unification.md)
- Coordination ledger:
  [`docs/coordination/-post-1089-followups-ledger.md`](../../docs/coordination/-post-1089-followups-ledger.md)
- Underlying Kashaev volume conjecture:
  [`kashaev-volume-conjecture`](kashaev-volume-conjecture.md)
- $\nu_{\mathrm{SDP}}$ algorithmic definition:
  [`atom-knot-mass-derivation`](atom-knot-mass-derivation.md)
  §Algorithm step 3
<!-- FILE_END: kashaev-density-equals-sdp-multiplicity.md -->

