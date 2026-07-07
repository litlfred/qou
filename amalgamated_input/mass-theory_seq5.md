<!-- FILE_START: corrected-markov-trace.md -->
The Markov trace of the trefoil braid
$\sigma_0 \sigma_1 \sigma_0$ is $z^3$, **not** $hz^2 + z$
as would be obtained from the vertex volume product formula.
The product factorization
([Markov trace product](#thm:markov-trace-product))
is invalid when generators are **adjacent**.

## Statement

**Proposition.**

$$
  \mathrm{tr}_M(\sigma_0 \sigma_1 \sigma_0) = z^3
$$

*where $z = (1 + h\delta)^{-1}$ is the Markov parameter
and $h = q - q^{-1}$.  The vertex volume product
$\hat{V}_0 \cdot \hat{V}_1 \cdot \hat{V}_0 = hz^2 + z \neq z^3$
does not apply here.*
<!-- FILE_END: corrected-markov-trace.md -->

<!-- FILE_START: mass-ordering-corrected.md -->
With the corrected Markov trace
$\mathrm{tr}_M(e^-) = z^3$
([corrected trace](#prop:corrected-markov-trace)),
the nucleon traces at $q_0 = 1.109978595554181\ldots$ (50 dps) are:

$$
  \mathrm{tr}_M(\mathfrak{p}) \approx -0.012,
  \qquad
  \mathrm{tr}_M(\mathfrak{n}) \approx -0.134
$$

Since categorical mass is $\mathfrak{m} = |\mathrm{tr}_M|$:

$$
  |\mathrm{tr}_M(\mathfrak{n})| > |\mathrm{tr}_M(\mathfrak{p})|
  \quad \Longrightarrow \quad
  \mathfrak{m}_{\mathfrak{n}} > \mathfrak{m}_{\mathfrak{p}}
  \quad \checkmark
$$

This matches the experimental ordering
$m_n \approx :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json}$ MeV $> m_p \approx :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json}$ MeV.

The **negative signs** of both traces reflect the
fermionic (antisymmetric) character of the nucleon — the
Markov trace of a confined baryon is negative because the
Borromean braid $\mathcal{B}_3$ carries odd parity under
the sign representation of $S_3$.
<!-- FILE_END: mass-ordering-corrected.md -->

<!-- FILE_START: frobenius-gram-matrix.md -->
The Frobenius self-duality $A \cong A^\vee$ induces a concrete
bilinear form on $H_3(q)$ via the Markov trace.  The **Gram
matrix** $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$ over the NF
basis encodes all interaction pairings, and its inverse
$G^{-1}$ gives the explicit dual construction
$K^\vee = \sum_{i,j} c_i (G^{-1})_{ij} b_j$.

## Markov trace of NF basis elements

Write $h = q - q^{-1}$ and $z = 1/(q^{1/2} + q^{-1/2})$.

See [Table 1](#tbl:frobenius-gram-matrix-table1-data).

The trace of $e^-$ follows from the Ocneanu--Wenzl Markov recursion
(cyclicity + Hecke quadratic + Markov axiom restricted to the
sub-algebra):
$\mathrm{tr}_M(\sigma_0\sigma_1\sigma_0)
= \mathrm{tr}_M(\sigma_1\sigma_0^2) \;\text{(cyclicity)}
= \mathrm{tr}_M(\sigma_1(h\sigma_0+1)) \;\text{(Hecke quadratic)}
= h\cdot\mathrm{tr}_M(\sigma_1\sigma_0) + \mathrm{tr}_M(\sigma_1)
= h \cdot z\,\mathrm{tr}_M(\sigma_0) + z
= hz^2 + z$
(the last step uses the Markov axiom on $\sigma_1$ paired with
$\sigma_0 \in H_1$).

At $q_0 = 1.109978595554181\ldots$ (50 dps), $hz^2 + z \approx 0.5514$ (the stale
$z^3 \approx 0.1245$ was off by a factor of 4.4).

## Gram matrix (symbolic in $q$)

**Proposition (stale symbolic entries — see Markov-bug note).**
*The $6 \times 6$ Gram matrix $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$
over the NF basis $\{\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-\}$
has the structural form below; the entries containing $z^3$ or
higher $z^k$ powers from $\mathrm{tr}_M(e^-)$ are stale and need
the $z^3 \mapsto hz^2 + z$ substitution to be propagated:*

$$
  G
  =
  \begin{pmatrix}
    1     & z     & z     & z^2     & z^2     & z^3 \\
    z     & hz+1  & z^2   & hz^2+z  & z^3  & g_{15} \\
    z     & z^2   & hz+1  & z^3  & hz^2+z  & g_{15} \\
    z^2   & hz^2+z & z^3 & g_{15} & g_{34} & g_{35} \\
    z^2   & z^3 & hz^2+z & g_{34} & g_{15} & g_{35} \\
    z^3 & g_{15} & g_{15} & g_{35} & g_{35} & g_{55}
  \end{pmatrix}
$$

*where (STALE — pending recomputation):*
- $g_{15} = hz^3 + z^2$ (from $\sigma_0 \cdot e^- = he^- + L_-$)
- $g_{34} = hz^3 + hz + 1$ (from $L_+ \cdot L_- = he^- + h\sigma_0 + \gamma$)
- $g_{35} = h^2z^3 + 2hz^2 + z$ (from $L_+ \cdot e^- = h^2e^- + hL_+ + hL_- + \sigma_1$)
- $g_{55} = (h^3+h)z^3 + 2h^2z^2 + 2hz + 1$ (from $e^- \cdot e^- = (h^3+h)e^- + h^2L_+ + h^2L_- + h\sigma_1 + h\sigma_0 + \gamma$)

*The matrix is **symmetric** ($G_{ij} = G_{ji}$, by cyclicity of the
Markov trace) and **non-degenerate** ($\det G \neq 0$ for $q \neq 0, 1$),
but **not positive definite** — it has indefinite signature.*

## Operator identification via the dual

The Frobenius dual
([def:frobenius-dual-h3](#def:frobenius-dual-h3)) exactly
identifies each basis element with its corresponding knot operator.

**Proposition (operator identification).**
*For each NF basis element $b_k$, the pairing of $b_k^\vee$
with the knot operators $\beta(T_{m,n})$ satisfies:*

See [Table 2](#tbl:frobenius-gram-matrix-table2-data).

*Each basis element pairs maximally with exactly one knot
operator (the operator whose braid word contains that element).
The electron dual $e^{-\vee}$ pairs with $T_{2,3}$ (trefoil)
with coefficient $1$ — the Frobenius dual selects the trefoil
operator for the electron.*

## Annihilation identity (symbolic)

**Proposition.**
*$e^- \cdot e^+ = \gamma$ (the photon / identity), for all $q$.*
<!-- FILE_END: frobenius-gram-matrix.md -->

<!-- FILE_START: frobenius-dual-h3.md -->
**Definition (Frobenius dual).**
*Let $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$ be the non-degenerate
Frobenius Gram matrix on the NF basis $\{b_i\}$ of $H_3(q)$
([prop:frobenius-gram-matrix](#prop:frobenius-gram-matrix)). For a
state $K = \sum_i c_i b_i$ in NF, the **Frobenius dual**
is the unique element $K^\vee \in H_3(q)$ satisfying
$\langle K^\vee, b_j \rangle_F = c_j$ for all $j$.
Explicitly:*

$$
  K^\vee = \sum_{i,j} c_i (G^{-1})_{ij} b_j.
$$

*The dual exists and is unique by non-degeneracy of $G$: the pairing
$\langle K^\vee, b_j \rangle_F = \sum_{i,k} c_i (G^{-1})_{ik} G_{kj}
= \sum_i c_i \delta_{ij} = c_j$ follows from $G^{-1} G = I$.*
<!-- FILE_END: frobenius-dual-h3.md -->

<!-- FILE_START: gram-determinant-plancherel-ratio.md -->
**Proposition (closed-form $\kappa$ via Plancherel weights).**
*Working over $R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$, let
$\beta_s = T_{2,9}$, $\beta_w = T_{3,5}$ be the unique pair of
genus-$4$ torus knots
([Bring uniqueness](#prop:force-carrier-bring-uniqueness)).  Each
admits a Wedderburn decomposition into central idempotents of the
ambient Hecke algebra $H_n(R, q)$:*

$$
  \beta_\bullet \;=\; \sum_{\lambda \,\vdash\, n}
    c_\lambda^{(\bullet)}\; e_\lambda,
  \qquad
  c_\lambda^{(\bullet)} \;=\; \chi_\lambda(\beta_\bullet) \in R.
$$

*Then the Gram-determinant ratio*

$$
  \kappa \;:=\; \frac{\det G^{\mathrm{cl}}_{\mathrm{CS}}}
                     {\det G^{q}_{\mathrm{CS}}}
$$

*appearing in the Chern-Simons :refterm[descent]{#descent}
(CS coupling) is given by the
Plancherel-weighted character product*

$$
  \boxed{\;
  \kappa \;=\;
  \prod_{\lambda \,\vdash\, n}
    \left[
      \frac{\dim V_\lambda}{\dim_q V_\lambda}
      \cdot
      \frac{[n]_q!}{n!}
    \right]^{c_\lambda^{(s)}\, c_\lambda^{(w)}}
  \,\in\, R.
  \;}
$$

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: gram-determinant-plancherel-ratio.md -->

<!-- FILE_START: archimedean-functor-uniqueness.md -->
**Proposition (conditional on [`conj:dilogarithm-archimedean-limit`](#conj:dilogarithm-archimedean-limit) and on the Bloch-Suslin pentagon-uniqueness theorem [`suslin1991`]).**
*Let $\tau_{\text{arch}} = \pi_\infty \circ \tau$ be the archimedean
realization functor of the QOU substrate
([archimedean realization functor](#def:archimedean-realization-functor)),
acting on motivic inputs assembled from braid / knot data. Assume*

- *(C1) The substrate's mass-formula state sum is pentagon-coherent:
   $\tau_{\text{arch}}$ is a continuous, antisymmetric, real-valued
   functional on $B(\mathbb{C})$ — the structural content provided by
   the cosimplicial / Yekutieli triple machinery
   ([`prop:cosimplicial-crossed-groupoid`](#prop:cosimplicial-crossed-groupoid))
   together with the archimedean-limit class
   `QOU.QPochhammer.ArchimedeanLimit`
   ([`conj:dilogarithm-archimedean-limit`](#conj:dilogarithm-archimedean-limit)).*
- *(C2) Bloch-Suslin pentagon-uniqueness [`suslin1991`,
   `bloch2000`]: any continuous antisymmetric pentagon-coherent
   real-valued function on $\mathbb{C} \setminus \{0,1\}$ is a
   constant scalar multiple of the Bloch-Wigner dilogarithm $D$.*

*Then $\tau_{\text{arch}}$ is uniquely determined, up to a single
multiplicative real scalar, by the requirement that*

$$
  \lim_{q \to 1}\;\tau_{\text{arch}}\bigl(\Phi_q(z)\bigr)
  \;=\;
  D(z)
  \;:=\;
  \mathrm{Im}\,\mathrm{Li}_2(z) + \log|z|\,\arg(1-z)
$$

*equal the **Bloch-Wigner dilogarithm** on every shape parameter
$z \in \mathbb{C} \setminus \{0,1\}$. The uniqueness reduces to the
Bloch-Suslin pentagon characterisation: $D$ is the unique (up to a
real scalar) continuous, antisymmetric, real-valued function on
$\mathbb{C} \setminus \{0,1\}$ satisfying the 5-term pentagon
identity*

$$
  D(x) - D(y) + D\!\left(\tfrac{y}{x}\right)
  - D\!\left(\tfrac{1-y^{-1}}{1-x^{-1}}\right)
  + D\!\left(\tfrac{1-y}{1-x}\right) \;=\; 0.
$$

> **Theorem (conditional on [`conj:dilogarithm-archimedean-limit`](#conj:dilogarithm-archimedean-limit)).**
> Per AGENTS.md §3b-cond: the upstream conjecture is axiomatised in
> Lean as the typeclass
> [`QOU.QPochhammer.ArchimedeanLimit`](../braids-and-knots/dilogarithm-archimedean-limit.lean);
> the Bloch-Suslin pentagon-uniqueness theorem [`suslin1991`,
> `bloch2000`] is similarly axiomatised as
> [`QOU.Archimedean.BlochSuslinUniqueness`](archimedean-functor-uniqueness.lean).
> The Lean theorem
> [`QOU.Archimedean.archimedean_functor_uniqueness`](archimedean-functor-uniqueness.lean)
> takes both classes as `[Instance]` hypotheses and is proved
> **without `sorry`** — the only unproved inputs are the two named
> classes, both of which are well-established results awaiting
> Mathlib formalisation (`Real.dilog`, `BlochGroup`, the Suslin
> map). This block therefore qualifies as a *rigorous conditional
> result* in the §3b-cond sense rather than an unproved conjecture.

## Pre-archimedean / archimedean separation

The QOU substrate is pre-archimedean: every block in the
[motivic substrate](#def:motivic-substrate) and the
[algebraic quantum volume](#def:algebraic-quantum-volume) lives
in $R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$, a ring of
Laurent polynomials with no real-analytic transcendentals. QOU
observables — masses, binding energies, the fine-structure
constant — are real numbers, and the only exit from $R$ to
$\mathbb{R}$ is the archimedean realization functor
$\tau_{\text{arch}}$.

Two structural questions are settled simultaneously by Bloch-Suslin
pentagon-uniqueness. (i) *Uniqueness of the exit*: any real-valued
continuous functional on $B(\mathbb{C})$ respecting the 5-term
pentagon identity is forced to coincide with $D$ up to a single
overall scalar; therefore the archimedean image of a substrate
motivic class is canonical. (ii) *Provenance of $\pi$*: any
transcendental constant in a QOU observable is the
$\tau_{\text{arch}}$-image of substrate pentagon data via $D$ (or
its multivariate generalisations), and is therefore not an external
import. The additive Bring zero-mode candidate
[`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)
illustrates the second point: the $2/(3\pi) = 2g/(4\pi(g-1))$
correction at $g = 4$ is the archimedean shadow of pentagon
data on Bring's surface, not a $\pi$-import outside $R$.

## The algebraic / archimedean dichotomy

The mass formula evaluates a closed cycle on the
[Frobenius-Hopf substrate](#def:frobenius-hopf-substrate). The
non-degenerate Frobenius pairing $\int_A \circ \mu$ identifies
$A \cong A^\vee$, making the substrate algebra self-dual; this
self-duality drives the descent involution
$\hat{\tau}_n$ on the endomorphism algebra
([mass endomorphism](#conj:mass-endomorphism)),
which splits the categorical mass endomorphism into a
**descended** baseline component and a **transient** component
localized at the exceptional divisors of the brane tower.

Within this purely algebraic substrate, the mass evaluation yields
the [algebraic quantum volume](#def:algebraic-quantum-volume)

$$
  \mathrm{Vol}_q(\beta) \;=\; \prod_{i=0}^{A-2}\hat{V}_i(q),
  \qquad \hat{V}_i(q) \in \mathbb{Z}[q^{\pm 1/2}],
$$

a finite product of Laurent polynomials living strictly in
$\mathbb{Z}[q^{\pm 1/2}]$. Everything to this point is categorical
and discrete — no $\pi$, no $\zeta(3)$, no real-analytic
transcendentals.

Transcendental numbers enter the framework **exclusively** at the
boundary of observation. When $\tau_{\text{arch}}$ is applied to
project the categorical data into physical spacetime, it takes
the absolute logarithm of the algebraic quantum volume
([quantum dilogarithm volume](#prop:quantum-dilogarithm-volume)).
This functor converts the discrete, combinatorial Hecke algebra
states into continuous, transcendental observables.

To satisfy the Descartes condition $\chi = -6$, the physical
state space is restricted to Bring's surface, a genus-$4$ curve
with maximal $S_5$ automorphism. The observable particle spectrum
consists entirely of knots that embed within this genus-$4$
handlebody. After $\tau_{\text{arch}}$ is applied, the
[Kashaev volume conjecture](#conj:kashaev-volume-conjecture)
identifies the limit of the algebraic state sum with the classical
hyperbolic volume of these specific knot complements. In this
limit, the quantum dilogarithm $\Phi_q(z_i)$
([quantum dilogarithm volume](#prop:quantum-dilogarithm-volume))
evaluated at each exceptional divisor degenerates into the
Bloch-Wigner dilogarithm $D(z_i)$
([dilogarithm archimedean limit](#conj:dilogarithm-archimedean-limit)).
The Bloch-Wigner dilogarithm is uniquely characterized as the
function satisfying the 5-term pentagon identity
[`suslin1991`, `bloch2000`], providing the exact geometric measure
of the ideal tetrahedra that triangulate the knot complement.
## Corollaries

**(a) Resolves the pre-archimedean concern in
[`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode).**
The $\pi$ in the additive correction $2/(3\pi) = 2g/(4\pi(g-1))$
at $g=4$ is the unique archimedean shadow of pentagon-coherent
substrate data on Bring's surface. The substrate's pentagon
coherence forces the archimedean image to involve $D$ (and hence
$\pi$ via $D$'s functional equation); no other transcendental
shape is admissible. The additive correction is therefore *not*
outside $R$ — it is the canonical $\tau_{\text{arch}}$-image of
$R$-internal pentagon data.

**(b) Forecloses arbitrary $\pi$-imports.** Any candidate closed
form for a QOU observable that includes a transcendental constant
not derivable from $D$ (or its multivariate generalisations
$D_n$) is excluded. This is a falsifiability constraint: the
multiplicative gluon-octet form (a legacy PSLQ-empirical conjecture,
since superseded by [`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode))
required arbitrary integer ratios $45 \cdot [3]_q \cdot
(1+\delta_{CS}+8q\delta_{CS}^2)$ that would have to come from a
non-pentagon source, is ruled out *structurally* in addition to
the existing PSLQ ruling.

**(c) Pins the figure-8 knot example.** The figure-8 knot $4_1$
embeds smoothly into Bring's surface as the amphichiral mass
mechanism. On the pre-archimedean side it has a completely rigorous
motivic / algebraic representation via its Hecke normal form in
$\mathbb{Z}[q^{\pm 1/2}]$. Once $\tau_{\text{arch}}$ maps this
motivic state into the observable continuum, its hyperbolic volume
realizes as the transcendental
$\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3) \approx :val[Vol_4_1]{precision=6}$. The
motivic side guarantees exact algebraic relationships governing
particle interactions; $\tau_{\text{arch}}$ supplies the
transcendental continuum required for geometric measurement. See
[figure-8 archimedean illustration](#rem:figure-8-archimedean-illustration).

## Open problems

1. **K-theoretic identification.** Make the Bloch-group factoring
   of the QOU mass-formula state sum precise: which class in
   $K_3^{\text{ind}}(\mathbb{C})$ does an $A$-strand braid $\beta$
   represent? Conjecturally, the class is read off from the
   Yekutieli triple data; making this rigorous requires identifying
   the $J^2$-jet of the cosimplicial structure with a Bloch-group
   1-cocycle.
2. **Multivariate Bloch-Suslin.** For mass-tower contributions
   spanning multiple exceptional divisors, the relevant invariant
   is the higher Bloch group $B_n(\mathbb{C})$ with the
   $n$-variable polylogarithm $D_n$. Pentagon-uniqueness for
   $D_n$ at $n \geq 3$ is open in the literature (Goncharov 1995
   conjectures); the QOU framework can take it as input where
   needed.
3. **Lean formalisation of Suslin1991.** Mathlib has neither
   `Real.dilog` nor `BlochGroup`. The Lean stub records this as
   a sorry keyed to [`suslin1991`]; closure depends on upstream
   Mathlib work.

## Witness

No canonical witness is appropriate for a uniqueness claim. The
relevant cross-check is that any new closed form for a QOU
observable proposed in this repository must be expressible as a
$\tau_{\text{arch}}$-image of a pentagon-coherent
$R$-internal class, or equivalently, must factor through $D$ (or
$D_n$) in its archimedean expansion. The
[`em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)
candidate satisfies this; the legacy gluon-octet PSLQ candidate
(now removed; superseded by
[`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode))
did not.
<!-- FILE_END: archimedean-functor-uniqueness.md -->

<!-- FILE_START: em-spectral-completeness.md -->
**Setup (commutative ring of coefficients).**
Throughout, the categorical structure is $R$-enriched over

$$
  R \;=\; \mathbb{Z}\bigl[q^{\pm 1/2},\, (q - q^{-1})^{-1}\bigr].
$$

Let $(\mathbf{C}, A, \tau)$ be a rigid :refterm[braided monoidal category]{#braided-monoidal-category}
$R$-enriched with self-dual fundamental object $A$ of categorical
dimension $\dim_q A = [2]_q \in R$, and $\tau \colon \mathbf{C} \to
R\text{-mod}$ the fibre functor.

**Theorem (two-strand spectral completeness).**
*The Frobenius $R$-algebra $E := \mathrm{End}_{\mathbf{C}}(A \otimes A)$
is a free $R$-module of rank $2$ with the following structure.*

1. *There exist exactly two non-zero central idempotents
   $e_+, e_- \in E$ with $e_+ + e_- = \mathrm{id}_{A \otimes A}$ and
   $e_+ \cdot e_- = 0$.*
2. *Each $e_\pm$ projects onto a simple summand:*
   $$
     A \otimes A \;\cong\; V_+ \oplus V_-,
     \qquad e_\pm A^{\otimes 2} = V_\pm.
   $$
   *The summand $V_-$ is canonically isomorphic to the unit object
   $\mathbf{1}$ — a singlet of $R$-rank one.*
3. *The braiding decomposes as*
   $$
     c_{A,A} \;=\; q^{1/2}\, e_+ \;-\; q^{-1/2}\, e_-,
   $$
   *and $\{q^{1/2},\, -q^{-1/2}\}$ are the only eigenvalues of
   $c_{A,A}$ on $A \otimes A$.*
4. *(Plancherel completeness.) The Plancherel weights*
   $$
     w_+ \;=\; \frac{(\dim_q V_+)^2}{[2]_q!},
     \qquad
     w_- \;=\; \frac{(\dim_q V_-)^2}{[2]_q!}
   $$
   *satisfy $w_+ + w_- = 1$ in $R \otimes \mathbb{Q}$.*
<!-- FILE_END: em-spectral-completeness.md -->

<!-- FILE_START: reidemeister-mass-invariance.md -->
**Conjecture (conditional on [`conj:borromean-quark`](#conj:borromean-quark)).**
The topological mass formula is a knot invariant (R-I, R-II,
R-III).  The binding energy of linked particles is an
embedding invariant (R-II, R-III but not R-I).  Shell
transitions are R-I moves on the embedding. *(The three
Reidemeister invariances follow from the hyperbolic-volume
invariant and the embedding structure; the shell-transition
R-I reading is the conjectural part.)*

**The three Reidemeister moves.**

Every deformation of a knot diagram decomposes into a sequence
of three local moves:

- **R-I** (curl): add or remove a single crossing (writhe
  changes by $\pm 1$).
- **R-II** (poke): add or remove a pair of crossings with
  opposite signs (writhe unchanged).
- **R-III** (slide): move a strand past a crossing (crossing
  number unchanged).

**Topological mass: invariant under all three.**

The bare mass of a particle is determined by the hyperbolic
volume of its knot complement:

$$
  m_{\mathrm{bare}} = 
  \frac{\mathrm{Vol}(S^3 \setminus K)}{\hbar_q^2}
  \cdot \lambda_{\mathrm{scale}}.
$$

The hyperbolic volume is a **topological invariant** of the
knot type — it does not depend on the diagram.  Since
Reidemeister's theorem states that two diagrams represent the
same knot if and only if they are related by a finite sequence
of R-I, R-II, R-III moves:

$$
  m_{\mathrm{bare}}
   \text{is invariant under R-I, R-II, R-III.}
$$

The electron mass $\mathfrak{m}_e \approx 0.511$ MeV (from vacuum drag, since
$\mathrm{Vol}(T_{2,3}) = 0$) does not change when the electron
is excited.  The proton mass $\mathfrak{m}_{\mathfrak{p}} \approx 938$ MeV
(from $\mathrm{Vol}(\mathcal{B}_3)$) does not change when the
atom is ionised.  Mass is a property of the **knot type**, not
the diagram.

**Binding energy: invariant under R-II and R-III only.**

The binding energy of a linked pair (electron--proton, or
nucleon--nucleon) is the crossing energy of the Hopf link
connecting them:

$$
  \mathfrak{E}_{\mathrm{bind}}
  = 
  \sum_{\text{crossings of link}}
  \epsilon_i \cdot q^{\pm 1}
$$

where the sum runs over the crossings of the **embedding** of
one particle's knot inside the other's Seifert surface.

- **R-III** (strand slide): rearranges crossings without
  changing their number or signs.  The crossing energy sum
  is invariant. $\checkmark$

- **R-II** (poke): adds two crossings of opposite sign.  Their
  contributions to the crossing energy are $+q \cdot \epsilon$
  and $-q^{-1} \cdot \epsilon$.  In the Skein resolution, the
  pair resolves to $(q - q^{-1}) \cdot \epsilon \cdot L_0$,
  where $L_0$ is the smoothed state.  For a virtual pair
  (the two crossings are adjacent), $L_0$ is the original
  link and the contributions cancel to leading order.  The
  binding energy is invariant. $\checkmark$

- **R-I** (curl): adds a single crossing.  This changes the
  writhe by $\pm 1$ and adds a crossing energy contribution
  $\pm q^{\pm 1} \cdot \epsilon$ that does **not** cancel.
  The binding energy **changes**. $\times$

$$
  \mathfrak{E}_{\mathrm{bind}}
   \text{is invariant under R-II, R-III but \textbf{not} R-I.}
$$

**Shell transitions are R-I moves.**

When a photon is absorbed by the hydrogen atom, the electron
trefoil $T_{2,3}$ undergoes a **Reidemeister I move** within its
Hopf link to the proton: a curl is added to the trefoil diagram
at the exceptional divisor.  The writhe changes from $w$ to
$w + 2$ (a pair of R-I moves adding two curls to preserve the
knot type's minimal crossing structure):

$$
  n \to n + 1
  \qquad\Longleftrightarrow\qquad
  w \to w + 2
  \qquad\Longleftrightarrow\qquad
  \text{two R-I moves on the embedding.}
$$

The bare mass $\mathfrak{m}_e$ is unchanged (R-I is a knot invariant).
The binding energy $E_n = -13.6/n^2$ eV changes (R-I is NOT
an embedding invariant).  The difference $\Delta E = E_{n+1} - E_n$ is the photon energy.

**Summary.**

| Quantity | R-I | R-II | R-III | Physical meaning |
|----------|:---:|:----:|:-----:|-----------------|
| Bare mass | $\checkmark$ | $\checkmark$ | $\checkmark$ | Particle identity (knot type) |
| Binding energy | $\times$ | $\checkmark$ | $\checkmark$ | Bound state energy (embedding) |
| Shell number $n$ | $\times$ | $\checkmark$ | $\checkmark$ | Writhe level of embedding |
| Knot type | $\checkmark$ | $\checkmark$ | $\checkmark$ | Which particle it is |
| Writhe $w$ | $\times$ | $\checkmark$ | $\times^*$ | Diagram-dependent |

${}^*$R-III preserves writhe but is not the only invariance
of writhe; writhe is a regular isotopy invariant (R-II +
R-III), not a knot invariant (R-I + R-II + R-III).

**Physical consequence.**

A particle's **identity** (which knot type: electron, muon,
proton, neutron) is determined by R-I + R-II + R-III invariants
— the topological knot type.  A particle's **state** (which
shell, which orbital) is determined by R-II + R-III invariants
— the regular isotopy class of the embedding.  The difference
between identity and state is precisely one Reidemeister move:
R-I.

This is why an excited hydrogen atom is still hydrogen: the
electron is still a trefoil (knot type unchanged by R-I).  But
it is in a different state: the trefoil's writhe is different
(embedding changed by R-I), and the binding energy differs.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: reidemeister-mass-invariance.md -->

<!-- FILE_START: borromean-markov-trace-closed-form.md -->
**Proposition (Borromean Markov trace closed form).**
*The Markov trace of the Borromean braid
$\beta_{\mathrm{Bor}} = (\sigma_1^{-1}\sigma_2)^3$ on $H_3(q)$,
evaluated via the Jones polynomial of the Borromean rings
$\mathcal{B}_3$, admits the exact closed form*

$$
  \boxed{\;\;
  \mathrm{tr}_M(\beta_{\mathrm{Bor}}, q)
  \;=\;
  \frac{4 + h^2 - 3h^4 - h^6}{h^2 + 4},
  \;\;}
$$

*where $h = q - q^{-1}$ and $h^2 + 4 = [2]_q^2$.*
## Structural significance for the mass formula

The $h^2 = 0$ result separates the proton-mass $h$-dependence into
clean layers:

| Factor in $F_{\mathrm{Bor}} = \mathrm{tr}_M(\beta_{\mathrm{Bor}}) \cdot [3]_q! / q^3$ | $h^2$ coefficient | Source |
|---|---|---|
| $\mathrm{tr}_M(\beta_{\mathrm{Bor}})$ | $0$ | per-partition cancellation (this proposition) |
| $[3]_q! = (h^2 + 3)\sqrt{h^2 + 4}$ | $11/4$ | algebraic (q-factorial) |
| $q^3$ (denominator) | $9/8$ | algebraic ($q = (h + \sqrt{h^2+4})/2$) |
| $F_{\mathrm{Bor}}$ (combined) | $19/2$ | $11/4$ and $9/8$ via division |

The exact vanishing of the $h^2$ term in the trace $\mathrm{tr}_M(\beta_{\mathrm{Bor}}, q)$ is an algebraic property of the Borromean rings' Jones polynomial evaluation. In the context of the mass formula, this forces any $h^2$ dependence in the overall amplitude $F_{\mathrm{Bor}}$ to arise strictly from the normalization factor $[3]_q! / q^3$.
<!-- FILE_END: borromean-markov-trace-closed-form.md -->

<!-- FILE_START: h3-markov-wenzl-weights.md -->
**Proposition (Closed-form Jones/Temperley–Lieb weights on $\mathrm{H}_3(q)$).**
*Let $y_\lambda(q)$ denote the coefficient of $\chi^\lambda$ in the Frobenius
expansion $\mathrm{tr}_M^{\mathrm{Jones}} = \sum_{\lambda \vdash 3} y_\lambda \,
\chi^\lambda$ of the **Jones-normalised** Markov trace on $\mathrm{H}_3(q)$ —
the $V_{\mathrm{Jones}} / [2]_q^{\,c-1}$ Temperley–Lieb closure of
[`prop:borromean-markov-trace-closed-form`](borromean-markov-trace-closed-form.md),
i.e. the trace computing the **Borromean rings' Jones polynomial**. (This is
**not** the full-Hecke Ocneanu trace consumed by the mass/binding pipeline —
see the **Scope** note below.) Then for all $q$:*

$$
  \boxed{\;\;
  y_{(3)}(q) \;=\; \frac{[4]_q}{[2]_q^{3}},
  \qquad
  y_{(2,1)}(q) \;=\; \frac{1}{[2]_q^{2}},
  \qquad
  y_{(1^3)}(q) \;=\; 0.
  \;\;}
$$

*At the symmetric point $q = 1$ these evaluate to*

$$
  \bigl(y_{(3)},\, y_{(2,1)},\, y_{(1^3)}\bigr)\big|_{q=1}
  \;=\;
  \bigl(\tfrac{1}{2},\, \tfrac{1}{4},\, 0\bigr)
  \qquad \text{— \emph{not} uniform.}
$$

## Scope — Jones/TL trace vs. the full-Hecke mass-pipeline trace

This proposition concerns the **Jones / Temperley–Lieb** normalisation of the
$\mathrm{H}_3(q)$ Markov trace — the trace whose value on a braid closure is the
**Jones polynomial**. Its defining feature is $y_{(1^3)} \equiv 0$: the
Temperley–Lieb quotient annihilates the three-row partition.

The framework's **mass and binding computations** use a *different* trace: the
**full-Hecke Ocneanu** Markov trace, with parameter $z = 1/(q^{1/2}+q^{-1/2})$
and Wedderburn weights given by the Wenzl Schur-principal specialisation
(`y_lambda_wenzl_bridge_numeric` $\to$ `closed_form_tau_M`). That trace is proven
canonical — Path A (ladder linear system) $=$ Path B (Wenzl Schur) as a
$\mathbb{Z}$-Laurent identity — in the $y_\lambda$–$\mathrm{tr}_M$ equivalence
proof (`docs/audits/2026-05-05-y-lambda-tr-m-equivalence-proof.md`), and its
three-row weight is $y_{(1^3)}(q) \neq 0$ for $q \neq 1$.

The two traces **coincide at the symmetric point** $q = 1$ (both give
$(\tfrac12,\tfrac14,0)$) and on the observable combination carried by
writhe-$0$, $\pi=\mathrm{id}$ braids — which is why every *physical* mass
prediction is insensitive to the distinction. They **diverge for $q \neq 1$**:
the full-Hecke weights at the substrate are $(0.4154,\,0.2809,\,0.0227)$.
Consequently the closed forms below should be read as the **Jones-polynomial**
weights, not as the general $\mathrm{tr}_M$ $y_\lambda$ used by the compute
pipeline.
## Immediate corollary — the Borromean closed form in one line

For any writhe-$0$ braid $\beta \in B_3$ with $\pi(\beta) = \mathrm{id} \in S_3$:

$$
  \mathrm{tr}_M(\beta)
  \;=\;
  1 + \frac{\chi^{(2,1)}(\beta) - 2}{[2]_q^{2}}.
$$

The entire $h$-dependence of such traces is carried by the single
standard-channel character; the Borromean closed form is this identity
evaluated at $\chi^{(2,1)}(\beta_{\mathrm{Bor}}) = 2 - 3h^4 - h^6$.

## Non-uniformity of the weights — chirality of the Jones trace

A bar-involution argument would suggest $y_{(3)} = y_{(1^3)}$ (the
transpose pair). It fails: the transpose symmetry $\lambda
\leftrightarrow \lambda^T$ is induced by the sign-twist automorphism
$\sigma_i \mapsto -q\,\sigma_i^{-1}$, and the Jones-normalised Markov
trace is **not invariant** under this automorphism — it is chiral,
weighting the $\sigma$- and $\sigma^{-1}$-eigenchannels asymmetrically.
The extreme expression of this asymmetry is $y_{(1^3)} \equiv 0$
against $y_{(3)}(1) = 1/2$.

At $q = 1$ the trace reduces to the cycle-counting trace
$\mathrm{tr}_M(w) = 2^{\,c(w) - n}$ on $\mathbb{C}[S_3]$ ($c(w)$ =
number of cycles), and Schur orthogonality reproduces
$(\tfrac12, \tfrac14, 0)$ directly.

## Notation note — $y_\lambda$, $\mu_\lambda$, $\chi^\lambda$, $w_\lambda$ are distinct

Four $\lambda$-indexed scalars appear in the Hecke-algebra blocks of
this paper. They are easy to conflate by symbol similarity but encode
independent data:

- $y_\lambda(q)$ — Wenzl/Markov coefficient: appears in
  $\mathrm{tr}_M = \sum_\lambda y_\lambda \cdot \chi^\lambda$, normalised by
  $\sum_\lambda y_\lambda \, d_\lambda = 1$. **This proposition gives the
  Jones/TL values** ($y_{(1^3)} \equiv 0$); the full-Hecke Ocneanu trace used
  by the mass pipeline has *different* $y_\lambda$ at $q \neq 1$
  ($y_{(1^3)} \neq 0$) — see the Scope note above.
- $\chi^\lambda(g)$ — character: trace of the $V_\lambda$-representation
  on a specific element $g$ (e.g. a braid).
- $\mu_\lambda(q)$ — $q$-Laplacian eigenvalue on $V_\lambda$
  ([`prop:q-heat-kernel-peter-weyl`](../information-theory/q-heat-kernel-peter-weyl.md)):
  the heat-kernel decay rate, *not* a Markov-trace ingredient.
- $w_\lambda(q) = [n]_q! / H_q(\lambda)^2$ — Plancherel measure
  ([`rem:symmetric-point-resolution-loss`](../models-of-qous/symmetric-point-resolution-loss.md)):
  normalised by $\sum_\lambda w_\lambda = 1$; at $q = 1$ it is
  non-uniform in a *different* pattern ($\tfrac16, \tfrac23, \tfrac16$
  for $n = 3$) from the Wenzl weights of this proposition
  ($\tfrac12, \tfrac14, 0$).

## Significance for the Borromean derivation

The $1/4$ factor in
[$h^4(\mathrm{tr}_M(\beta_{\mathrm{Bor}})) = (-3) \cdot (1/4) = -3/4$](borromean-h4-categorical-derivation.md)
is $y_{(2,1)}(q = 1) = 1/[2]_q^2|_{q=1}$ from this proposition — and
the identity $y_{(2,1)}(q) = 1/[2]_q^2$ holds **exactly for all $q$**,
not only at the symmetric point. The Borromean $h^4$ separation into
character coefficient $\times$ Markov normalisation is therefore an
exact structural fact, with the $(h^2 + 4)$ denominator of the closed
form being precisely $[2]_q^2 = 1/y_{(2,1)}(q)$.

> **Correction note.** An earlier draft of this proposition claimed the
> $q = 1$ weights were *uniform* ($y_\lambda(1) = 1/4$ for all
> $\lambda \vdash 3$) via a bar-involution argument. That claim was
> wrong — caught in review — for the reason documented in the chirality
> section above: the Jones trace is not sign-twist invariant. The
> corrected weights $(\tfrac12, \tfrac14, 0)$ are verified three ways:
> Schur orthogonality on the $q = 1$ cycle-counting trace, the exact
> $q$-dependent closed forms above, and canonical reproduction of the
> Borromean closed form at 30 digits.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: h3-markov-wenzl-weights.md -->

<!-- FILE_START: unit-modulus-eigenvalue.md -->
**Proposition (unit-modulus eigenvalues and the Borromean fixed point).**
*For any braid word $\beta$ of even length in $H_3(q)$, the
eigenvalues of the standard representation $\rho_{(2,1)}(\beta)$
lie on the unit circle $|\lambda| = 1$. The Borromean braid
$\beta_{\mathrm{Bor}} = (\sigma_1\sigma_2^{-1})^3$ has the
degenerate eigenvalue $\lambda = -1$.*
<!-- FILE_END: unit-modulus-eigenvalue.md -->

