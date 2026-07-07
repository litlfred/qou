<!-- FILE_START: schur-weyl-mass-decomposition.md -->
Let $(Z, N)$ be an atom with atomic braid
$\mathcal{A} \in H_{3A}(q)$ on $3A$ strands
([atomic braid](#def:atomic-braid)), and let
$V^{\otimes 3A} \cong \bigoplus_{\lambda \vdash 3A} S^\lambda
\otimes V_\lambda$ be the Schur–Weyl decomposition, with $S^\lambda$
the Specht module of $H_{3A}(q)$ and $V_\lambda$ the corresponding
$\mathrm{GL}_q$-irreducible.

**Proposition.**
*The Markov trace of the atomic braid decomposes over partitions
$\lambda \vdash 3A$ as*

$$
  \mathrm{tr}_M(\mathcal{A})
  \;=\;
  \sum_{\lambda \,\vdash\, 3A}
    \frac{s_\lambda(\mathbf{q})}{H_q(\lambda)}
    \cdot
    \chi^\lambda(\mathcal{A}),
$$

*where $s_\lambda$ is the Schur function evaluated on
$\mathbf{q} = (q, q^{-1})$, $H_q(\lambda) = \prod_{x \in \lambda}
[h_x(\lambda)]_q$ is the $q$-hook product
([hook-weight derivation](#prop:hook-weight-derivation)), and
$\chi^\lambda$ is the Specht-module character.  Equivalently,
writing $w_\lambda(q) = s_\lambda(\mathbf{q})/H_q(\lambda)$ and
$\mathrm{tr}_\lambda = \chi^\lambda(\mathcal{A})$:*

$$
  \mathrm{tr}_M(\mathcal{A})
  \;=\;
  \sum_{\lambda \,\vdash\, 3A} w_\lambda(q)\, \mathrm{tr}_\lambda,
  \qquad
  w_\lambda(q) \in \mathbb{Z}[q, q^{-1}].
$$

**Three-channel regrouping for $A = 1$.**
*When $A = 1$ (single nucleon, $H_3(R, q)$), the partitions of $3$
are $\{(3), (2,1), (1,1,1)\}$ corresponding respectively to the
symmetric, standard, and antisymmetric Wedderburn blocks:*

$$
  w_{\mathrm{sym}} = w_{(3)} = \frac{[3]_q [2]_q}{[3]_q [2]_q [1]_q},
  \quad
  w_{\mathrm{std}} = w_{(2,1)} = \frac{[2]_q}{[3]_q [1]_q^2},
  \quad
  w_{\mathrm{alt}} = w_{(1,1,1)} = \frac{1}{[3]_q [2]_q [1]_q}.
$$

*These match the three-parameter Wedderburn weights
([three parameters Wedderburn](#prop:three-parameters-wedderburn))
and recover the three-invariant formula
([Wedderburn mass formula](#thm:wedderburn-mass-formula)) as the
$A=1$ specialisation.*

**Additive-Wedderburn approximation and its failure mode.**
*The current computation engine uses the **additive-Wedderburn**
approximation: for an $A$-nucleon atom it sums the $A=1$ weights
$(w_{\mathrm{sym}}, w_{\mathrm{std}}, w_{\mathrm{alt}})$ over
each of the $3A-1$ generators of $\mathcal{A}$.  This is exact
only when the atomic braid factors through independent copies
of $H_3(R, q)$, which is not the case in general:*

1. *For $A \geq 2$ the exact sum runs over all
   $p(3A)$ partitions of $3A$, not over $A$ copies of
   $\{(3), (2,1), (1,1,1)\}$.*
2. *The additive-Wedderburn trace drops the partitions whose
   Young diagrams have rows longer than $3$, i.e., the
   Schur–Weyl content coming from inter-nucleon entanglement.*
3. *For light atoms ($A \leq 3$) the excluded partitions carry
   small $w_\lambda(q_0)$ and the approximation is within
   $\lesssim 1\%$.  For $A \geq 6$ the excluded partitions
   include configurations like $(3A - 2, 2)$ and $(3A - 2, 1, 1)$
   whose weights grow with $A$, producing the observed
   $5\%$–$20\%$ binding-energy discrepancies in the
   mass-table-best witness at $^4$He through $^{40}$Ca.*

**Algebraic origin of each channel.**
*Schur–Weyl duality assigns each partition $\lambda$ a role:*

1. *$\lambda = (3A)$ **(fully symmetric)** — base-volume channel.
   Scales as the trace of the identity on the $\mathrm{Sym}^{3A}$
   representation; contributes a term proportional to $A$ (forced
   by extensivity of the Markov trace on a tensor product).*
2. *$\lambda = (3A-1, 1)$ **(standard defect)** — boundary channel.
   Scales as $A^{2/3}$ by the Weyl dimension formula for boundary
   Specht modules; this is the algebraic origin of the
   surface-like correction.*
3. *$\lambda = (3A-2, 2)$, $\lambda = (3A-2, 1, 1)$ **(pair defects)**
   — pair-crossing channels.  Scale as
   $\binom{A}{2}/A^{1/3}$ by counting pairs of generators whose
   transfer matrices share a Schur–Weyl component.  These are the
   algebraic origin of the pair-crossing correction captured in
   the SDP cross-channel path
   ([Markov pair, $\mathbb{Z}_2$](#prop:markov-pair-z2)).*
4. *Rectangular $\lambda$ **(closed-shell)** — shell-closure
   channel.  When $\lambda$ is rectangular of size $3A$, the
   hook product $H_q(\lambda)$ factorises sharply and $w_\lambda$
   acquires a large value at $q = q_0$; this is the algebraic
   origin of shell-closure enhancement at the magic nucleon
   counts
   ([shell–Schur–Weyl self-duality](#prop:shell-schur-weyl-self-duality)).*

*Each physical correction is therefore a named stratum of the
Schur–Weyl sum, with its scaling exponent determined by the Weyl
dimension formula applied to the corresponding Young diagram.*

**Relation to the GB residue spectral sum.**
*The Schur–Weyl sum above is the **descended** ($E^0$) term of the
residue spectral sum
([GB residue spectral sum](#prop:gb-residue-spectral-sum)):
both sums are over the partitions of $3A$, but the residue sum
adds the Mittag-Leffler contributions from strata $\lambda$ whose
weight $w_\lambda(q)$ has a pole at some $\zeta_\ell$.  The two
propositions together give the full mass:*

$$
  \mathfrak{m}(\mathcal{A}, q_0)
  =
  \sum_{\lambda \,\vdash\, 3A} w_\lambda(q_0)\,\mathrm{tr}_\lambda
  +
  \sum_\ell \frac{\operatorname{Res}_{q=\zeta_\ell}[w_\lambda \mathrm{tr}_\lambda]}
                  {q_0 - \zeta_\ell},
$$

*where the first sum is over regular partitions (analytic at
$q_0$) and the second is over filtration strata with root-of-unity
poles.*

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: schur-weyl-mass-decomposition.md -->

<!-- FILE_START: gb-residue-spectral-sum.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
substrate parameter $q_0$ and Hecke algebra $H_n(R, q)$ filtered by the
confinement filtration $J^\bullet(q)$
([confinement level](#def:confinement-level)).  Let
$\Phi_q(z) = \prod_{k\geq 1}(1 - q^{-k} z)^{-1}$ be the non-perturbative
quantum dilogarithm and let $\zeta_\ell$ denote the root of unity at
which the $\ell$-th knot-operator energy degenerates,
$E_\ell(\zeta_\ell) = 0$.

This proposition is the **symbolic feeding lemma** that produces the
cyclotomic coefficients $a_m$ of the Habiro-completion proposition
([Habiro completion](#prop:full-pole-structure-mass-trace)) from
filtration-stratum residues. It is a formal identity in the
Grothendieck group of the filtered differential algebra
$(H_n(R,q), J^\bullet, d)$, **not** a complex-analytic identity on
or near $S^1$.

**Proposition (residue spectral sum, symbolic form).**
*For a knot $\mathcal{K}$ represented by the closed braid with Hecke
normal form $T_w \in A = H_n(R, q)$
([Hecke normal form](#def:hecke-normal-form)), the categorical mass
admits the symbolic decomposition*

$$
  \mathfrak{m}_{q_0, \mathcal{K}}
  \;=\;
  \underbrace{\bigl|\int_A T_w(q_0)\bigr|}_{\text{descended part } E^0}
  \;+\;
  \sum_{\ell = 1}^{\ell(\mathcal{K}, q_0)}
    r_\ell(T_w; q_0),
  \qquad
  r_\ell(T_w; q_0)
    \;=\;
    \frac{\operatorname*{Res}_{q = \zeta_\ell}\!
      \bigl[\Phi_q \cdot \mathrm{tr}_{M,\ell}(T_w)\bigr]}
    {q_0 - \zeta_\ell},
$$

*where $\mathrm{tr}_{M,\ell}$ is the induced Markov trace on the
graded piece $J^\ell(q)/J^{\ell+1}(q)$ and $\ell(\mathcal{K}, q_0)$ is the
confinement level of $\mathcal{K}$ at $q_0$. The numerators
$\operatorname{Res}_{q = \zeta_\ell}[\Phi_q \cdot \mathrm{tr}_{M,\ell}]$
are the **stratum residues** that feed the cyclotomic coefficients
$a_m$ of the Habiro expansion via*

$$
  \sum_{\ell \geq 1} r_\ell(T_w; q_0)
  \;\equiv\;
  \sum_{m \geq 1} a_m(T_w)\,(q_0; q_0)_m
  \pmod{\widehat{\mathbb{Z}[q]}\text{-equivalence}},
$$

*the equivalence being modulo the cyclotomic completion ideal of
([Habiro ring](#def:habiro-ring)).*

**Cohomological interpretation.**
*The filtration $J^\bullet(q)$ together with the rewriting
differential $d$ induced by the three Gröbner–Shirshov rules
(Hecke, far commutativity, Yang–Baxter) makes $H_n(R, q)$ a
filtered differential algebra. The associated spectral sequence
has*

$$
  E_1^{\ell,*} \;=\; H^*\bigl(J^\ell/J^{\ell+1},\,d\bigr),
  \qquad
  E_\infty^{\ell,*}
    \;\Longrightarrow\;
    \mathrm{gr}^\ell\,H_n(R, q).
$$

*The functional $\int_A$ is closed for $d$ (cyclicity) and so
descends to $E_\infty$. The residue $r_\ell(T_w; q_0)$ is the
pairing of $\int_A$ with the level-$\ell$ stratum: structurally,
the stratum residue is a Hochschild-cohomology class on
$J^\ell/J^{\ell+1}$ evaluated at the substrate parameter, and the
total mass is the sum of these classes — in agreement with the
[mass endomorphism conjecture](#conj:mass-endomorphism).*

**Caveat: this is a symbolic, not analytic, identity.**
*The Cauchy-kernel factor $1/(q_0 - \zeta_\ell)$ is a formal symbol
attached to each stratum, not a function on $\mathbb{C}$ analytic
at $q_0$. Because the primitive roots of unity are dense in $S^1$,
$\mathrm{tr}_M$ is **not** meromorphic on any neighbourhood of
$S^1$, and the sum $\sum_\ell r_\ell$ has no convergent
complex-analytic meaning across $S^1$. The convergent statement
is the Habiro expansion
([Habiro completion](#prop:full-pole-structure-mass-trace)); the
Cauchy-kernel form here is its $q$-adic shadow at fixed cyclotomic
truncation.*

**Reduction in the level-zero case.**
*When $T_w \in J^0(q_0) \setminus J^1(q_0)$, all higher stratum
residues vanish and the formula reduces to
$\mathfrak{m} = |\int_A T_w|$ — the pure descended case
([categorical mass as Markov trace](#prop:categorical-mass-markov)).*

**Convergent archimedean counterpart: PL thimble periods on $\mathcal{E}_q$.**
*Strict archimedean split: this proposition is intrinsically an
$R$-side statement — the residues live in the categorical base ring
$R$, and the Cauchy-kernel form $1/(q_0 - \zeta_\ell)$ is symbolic.
A **convergent** archimedean realisation does exist: under the
fibre functor $\tau \colon R \hookrightarrow \mathbb{C}$, the
filtration stratum $J^p/J^{p+1}$ maps to the geometric jet bundle
$J^p\mathcal{S}$ on $\mathcal{E}_q(\mathbb{C})$ via
(jet-GB-PL correspondence),
and the residues at $\zeta_\ell \in S^1$ are replaced by
Picard–Lefschetz residues at the discriminant locus
$\{z \in \mathbb{C} : \Delta(z) = 0\}$ of the color-tube cubic
(Picard–Lefschetz thimble).
Because the discriminant points lie strictly off $S^1$, the
$\mathbb{C}$-side residues converge unconditionally and the sum
$\sum_p n_p \cdot \Pi^{(p)}$ is a bona fide complex-analytic
quantity — the **archimedean realisation** of the symbolic
$R$-side spectral sum.  The agreement
$\tau(\sum_\ell r_\ell) = \sum_p n_p \cdot \Pi^{(p)}$ is the
content of
(SW-period thimble equivalence);
the $R$-side and $\mathbb{C}$-side sums must not be conflated.*
<!-- FILE_END: gb-residue-spectral-sum.md -->

<!-- FILE_START: categorical-mass-positivity.md -->
**Remark (no exhaustive positivity proof needed).**
*The categorical mass scalars produced by the
[mass identity](#def:mass-identity) are values of the observation
functor $\tau$ on graded projective KLR modules
\cite{khovanovlauda2009, brundankleshchev2009}.  By construction
$\tau$ takes the graded Euler characteristic, so each coefficient
of the resulting polynomial is the dimension of a $\mathrm{Hom}$-space
between graded projectives:*

$$
  [\tau(\mathfrak{M}_K)]_d \;=\;
  \dim_R \mathrm{Hom}_{\mathcal{K}_n}\bigl(P_d, \mathfrak{M}_K\bigr)
  \;\in\; \mathbb{Z}_{\geq 0}.
$$

*Consequently the categorical mass and action coefficients are
**structurally** non-negative integers; an explicit positivity
argument per coefficient is unnecessary.  Coefficients that vanish
correspond to summands that lie in the
[:refterm[cemetery group]{#cemetery-group}](#def:cemetery-group), which the engine drops
during traversal — see
[cemetery-group emergence](#conj:cemetery-group-emergence).*

*The polynomial $\tau(\mathfrak{M}_K) = P_K(q)$ is therefore the
**mass-spectrum generating function** of $K$: each term $c_d q^d$ is
a mass component indexed by **graded Hecke energy** $d$ with
**microstate degeneracy** $c_d$. The relation to the macroscopic
scalar is a functorial composition (decategorification, then
evaluation at the substrate $q_0$, then dimensional anchor), not an
identity — see [mass-spectrum generating
function](#rem:mass-spectrum-generating-function) for the full
$\mathfrak{M}_K \to P_K(q) \to \mathfrak{m}_{\mathcal{K}} \approx m_0 \cdot |P_K(q_0)|$
pipeline.*
<!-- FILE_END: categorical-mass-positivity.md -->

<!-- FILE_START: mass-spectrum-generating-function.md -->
**Remark (the confined Laurent polynomial as mass-spectrum generating
function — functorial equivalence, not identity).**
*The relation "confined Laurent polynomial $=$ mass" is not a literal
equality. The polynomial $P_K(q) \in \mathbb{Z}[q^{\pm 1/2}]$ is a
graded Euler characteristic; the macroscopic mass is a scalar.
The two are linked by a functorial composition: a categorical
generating function whose evaluation at the substrate parameter
$q_0$ collapses to the observed scalar.*

## The polynomial as generating function, not a number

Let $\mathfrak{M}_K$ denote the stable highest-weight KLR module
\cite{khovanovlauda2009, brundankleshchev2009} associated to the
braid closure $\hat{\beta}_K$. The
[Observation Frame](#def:observation) $\tau$ takes the graded
Euler characteristic,

$$
  P_K(q)
  \;=\;
  \sum_{d \in \mathbb{Z}}
    \dim_R \mathrm{Hom}_{\mathcal{K}_n}(P_d, \mathfrak{M}_K) \, q^d
  \;\in\; \mathbb{Z}_{\geq 0}[q^{\pm 1/2}],
$$

where the sum is finite — confinement is the homological boundedness
of $\mathfrak{M}_K$ under the jet/filtration order ([confinement
level](#def:confinement-level)). The word "confined" is not
decorative: an unbounded module would yield an infinite power series
(formally an infinite mass tower); the bound truncates this to a
genuine Laurent polynomial.

## Interpretation of the polynomial: spectrum, not a single value

Each term $c_d q^d$ of $P_K(q)$ has an independent physical reading:

- **Exponent $d$** — the **graded Hecke energy**: a $\mathbb{Z}$-grading
  shift counting topological complexity (crystal-operator depth in
  $\mathfrak{M}_K$). Higher $d$ = higher internal topological tension.
- **Coefficient $c_d$** — the **microstate degeneracy**: the number
  of orthogonal Hom-channels carrying that energy. Coefficients are
  structurally non-negative integers
  ([structural positivity](#rem:categorical-mass-positivity)).

Read this way, $P_K(q)$ is the **mass spectrum** of $K$ — a partition
function over its internal homological slices. The terms are *mass
components*; their sum (after evaluation) is the macroscopic mass.

## Functorial equivalence via substrate evaluation

The macroscopic, measurable mass is the **evaluation** of $P_K(q)$ at
the substrate value $q_0 = 1.109978595554181\ldots$ (50 dps; symbolic
in $q$ above this paragraph):

$$
  \boxed{\;\;
    \mathfrak{m}_{\mathcal{K}}
    \;\approx\;
    m_0 \cdot \bigl|P_K(q_0)\bigr|
  \;\;}
$$

(see [two-tier scaling](#rem:two-tier-scaling-pq) for the
factorisation into the Tier-1 quantum-dimension normalisation and the
Tier-2 base-mass anchor $m_0$). The composition

$$
  \mathfrak{M}_K
  \;\xrightarrow{\;\tau\;}\;
  P_K(q)
  \;\xrightarrow{\;\mathrm{ev}_{q_0}\;}\;
  P_K(q_0)
  \;\xrightarrow{\;m_0\,|\cdot|\;}\;
  \mathfrak{m}_{\mathcal{K}} \in \mathbb{R}_{\geq 0}
$$

is the **functorial equivalence** linking the categorical state, its
generating function, and the physical observable. None of the three
arrows is an identity: $\tau$ is decategorification (loses
isomorphism information), $\mathrm{ev}_{q_0}$ is specialisation
(loses generic-$q$ structure — see the open issue in the
unified knot-mass formula), and
$m_0\,|\cdot|$ is unit conversion.

## Significance of the distinction

Conflating the polynomial with the mass produces three failure modes:

1. **A polynomial cannot equal a scalar.** Any agent or formalisation
   that writes "$P_K(q) = \mathfrak{m}_{\mathcal{K}}$" type-checks as
   nonsense. The correct statement is
   $\mathfrak{m}_{\mathcal{K}} \approx m_0 \cdot |P_K(q_0)|$.
2. **The microstate spectrum is invisible.** Treating $P_K$ as a
   single number erases the degeneracy structure carried by
   coefficients $c_d$ and the energy structure carried by exponents
   $d$ — exactly the data needed to compute branching ratios and
   resonance widths.
3. **The substrate dependence is hidden.** A single electron has a
   single mass on a scale because the substrate $q_0$ is fixed by
   the ambient vacuum, not because the spectrum has only one term.
   The polynomial is the topological engine; the scalar is its
   output at the operating point of our universe.

## Authoring guidance

When stating mass results in `.md` or `.lean`:

- **Do** write "$P_K(q)$ is the mass-spectrum generating function of
  $K$, and $\mathfrak{m}_{\mathcal{K}} \approx m_0 \cdot |P_K(q_0)|$".
- **Do not** write "$P_K(q)$ is the mass of $K$" or
  "$P_K = \mathfrak{m}_{\mathcal{K}}$".
- The Lean side carries this via the [mass identity](#def:mass-identity)
  definition (categorical state $\to$ polynomial) and the calibration
  blocks ([three calibration inputs](#prop:three-calibration-inputs))
  for the Tier-2 conversion.
<!-- FILE_END: mass-spectrum-generating-function.md -->

<!-- FILE_START: graded-markov-trace-from-gs-filtration.md -->
The Lean formalisation of the GB-residue spectral sum
([`prop:gb-spectral-sequence`](#prop:gb-spectral-sequence))
currently relies on two `noncomputable opaque` declarations,
`gradedMarkovTrace` and `residueAtRoot`, axiomatised in
[`content/.../gb-residue-spectral-sum.lean`](gb-residue-spectral-sum.lean).
This block gives the **narrative replacement** for the first of
the two — defining the graded Markov trace
$\mathrm{tr}_{M, \ell}$ as the induced trace on the
associated-graded piece $J^\ell / J^{\ell+1}$ of the
Gröbner–Shirshov filtration $J^\bullet$, with no analytic input.
The second opaque (`residueAtRoot`) is replaced by the companion
block
[`prop:residue-at-root`](#prop:residue-at-root).

## Setup

Let $H_n(q)$ be the Iwahori–Hecke algebra over $\mathbb{Q}(q)$
([AGENTS.md §7a](../../../AGENTS.md)). The Gröbner–Shirshov
filtration on the underlying braid-group algebra
$\mathbb{Q}(q)\langle \sigma_i \rangle / I_{\mathrm{Hecke}}$
([`prop:gb-spectral-sequence`](#prop:gb-spectral-sequence)) is the
two-sided ideal filtration

$$
  J^0 \;=\; H_n(q)
  \;\supset\; J^1
  \;\supset\; J^2
  \;\supset\; \cdots
  \;\supset\; J^{\ell(K, q)}
  \;\supset\; J^{\ell(K, q) + 1} \;=\; 0,
$$

where $J^\ell$ is generated by Hecke-normal-form representatives of
weight $\geq \ell$ in the GS leading-monomial order
\cite{geckpfeiffer2000, mathas1999}, and the cutoff $\ell(K, q)$
is the **confinement level** of the closed braid $K$
([`prop:confinement-level-exists`](#prop:confinement-level-exists)).
The associated-graded algebra is

$$
  \mathrm{gr}^\bullet H_n(q) \;=\; \bigoplus_{\ell \geq 0} J^\ell / J^{\ell+1}.
$$

The full Markov trace
$\mathrm{tr}_M : H_n(q) \to \mathbb{Q}(q)$
([`thm:jones-markov-trace`](#thm:jones-markov-trace)) is
filtration-respecting: $\mathrm{tr}_M(J^\ell) \subset
(\mathrm{tr}_M H_n(q))_\ell$, where the right-hand grading is the
$q$-degree filtration on $\mathbb{Q}(q)$ induced by the GS
leading-monomial filtration on $H_n(q)$.

## Statement

**Proposition (graded Markov trace from GS filtration).**
*For each $\ell \in \mathbb{N}$ there is a uniquely determined
$\mathbb{Q}(q)$-linear trace*

$$
  \mathrm{tr}_{M, \ell}
  \;:\;
  J^\ell / J^{\ell+1}
  \;\longrightarrow\;
  \mathbb{Q}(q)
$$

*characterised by either of the equivalent properties:*

1. ***Quotient compatibility.** The diagram*

   $$
     \begin{array}{ccc}
       J^\ell                    & \xrightarrow{\mathrm{tr}_M\restriction_{J^\ell}} & \mathbb{Q}(q) \\
       \downarrow_{\pi_\ell}     &                                                  & \downarrow_{=} \\
       J^\ell / J^{\ell+1}       & \xrightarrow{\mathrm{tr}_{M, \ell}}              & \mathbb{Q}(q)
     \end{array}
   $$

   *commutes — i.e. $\mathrm{tr}_{M, \ell} \circ \pi_\ell$ equals
   the restriction of $\mathrm{tr}_M$ to $J^\ell$.*

2. ***Vanishing on lower strata.** For all $T \in J^{\ell+1}$,
   $\mathrm{tr}_{M, \ell}(\pi_\ell(T)) = 0$.*

*This trace is well-defined because $\mathrm{tr}_M$ is filtration-
respecting: $\mathrm{tr}_M(J^{\ell+1}) \subset
(\mathrm{tr}_M H_n(q))_{\ell+1}$, so the induced map on the
quotient lands in $\mathbb{Q}(q)$.  Uniqueness follows from the
universal property of the quotient: any two maps that agree on
$J^\ell$ and vanish on $J^{\ell+1}$ agree on $J^\ell / J^{\ell+1}$.*

## Replacement of the Lean `opaque`

The Lean declaration

```lean
noncomputable opaque gradedMarkovTrace (ℓ : ℕ) (q : ℝ) : ℝ
```

in [`gb-residue-spectral-sum.lean`](gb-residue-spectral-sum.lean)
treats $\mathrm{tr}_{M, \ell}$ as an unspecified function of $\ell$
and $q$ — a black box whose values are produced at proof time.
The proposition above gives it a **constructive algebraic
definition** as the :refterm[descent]{#descent} of $\mathrm{tr}_M$ along the GS-
filtration quotient. Three things become immediate:

1. **Existence and uniqueness** are properties of the quotient,
   not assumptions.
2. **Compatibility with the spectral sequence** of
   [`prop:gb-spectral-sequence`](#prop:gb-spectral-sequence) is
   automatic: the $E_2$-page is precisely
   $\bigoplus_\ell H^\bullet(J^\ell / J^{\ell+1}, \mathrm{tr}_{M, \ell})$.
3. **Vanishing above the confinement level** is structural
   — $J^{\ell(K, q) + 1} = 0$ implies
   $\mathrm{tr}_{M, \ell}(K) = 0$ for $\ell > \ell(K, q)$ — and
   replaces the opaque-axiom version of `spectral_sum_finite`
   ([`gb-residue-spectral-sum.lean` line 86](gb-residue-spectral-sum.lean)).
<!-- FILE_END: graded-markov-trace-from-gs-filtration.md -->

<!-- FILE_START: residue-at-root.md -->
The Lean formalisation of the GB-residue spectral sum
([`prop:gb-spectral-sequence`](#prop:gb-spectral-sequence))
relies on a second `noncomputable opaque` declaration,
`residueAtRoot`, axiomatised in
[`content/.../gb-residue-spectral-sum.lean`](gb-residue-spectral-sum.lean)
alongside `gradedMarkovTrace`. This block gives the **narrative
replacement** for `residueAtRoot` — defining the cyclotomic
residue $\mathrm{Res}_{q \to \zeta_\ell}(\Phi_q \cdot
\mathrm{tr}_{M, \ell})$ purely algebraically as a quotient in the
**Habiro completion** of $\mathbb{Z}[q^{\pm 1}]$, with no
analytic continuation in $\mathbb{C}$.

The companion graded-trace block is
[`prop:graded-markov-trace-from-gs-filtration`](#prop:graded-markov-trace-from-gs-filtration).

## Setup

Let $\Phi_q(z) = \prod_{k = 1}^{\infty} (1 - q^{-k} z)^{-1}$ be the
quantum dilogarithm and let
$\mathrm{tr}_{M, \ell} : J^\ell / J^{\ell+1} \to \mathbb{Q}(q)$ be
the graded Markov trace
([`prop:graded-markov-trace-from-gs-filtration`](#prop:graded-markov-trace-from-gs-filtration)).
Fix a closed braid $K$ with Hecke normal form
$T_w \in H_n(q)$ and confinement level $\ell(K, q)$
([`prop:confinement-level-exists`](#prop:confinement-level-exists)).

For each $\ell \in \{1, \dots, \ell(K, q)\}$ the
GB-filtration index $\ell$ determines a **distinguished
cyclotomic order** $n_\ell \in \mathbb{N}_{\geq 2}$ — the order of
the primitive root of unity $\zeta_\ell$ at which the $\ell$-th
graded contribution is supported. Concretely $n_\ell$ is the
smallest integer such that the $q$-Pochhammer factor
$(q;q)_{n_\ell}$ divides the leading coefficient of every
representative of $J^\ell / J^{\ell+1}$ — a property that is
combinatorial in the GS leading-monomial order, not analytic
\cite{habiro2002}.

The **Habiro ring** is the cyclotomic completion

$$
  \widehat{\mathbb{Z}[q]}
  \;=\;
  \varprojlim_n \mathbb{Z}[q] / ((q; q)_n),
$$

with cyclotomic-projection maps
$\pi_n : \widehat{\mathbb{Z}[q]} \to \mathbb{Z}[q] / \Phi_n(q)$,
where $\Phi_n(q)$ is the $n$-th cyclotomic polynomial.

## Statement

**Proposition (algebraic cyclotomic residue).**
*Let $T_w \in J^\ell / J^{\ell+1}$ have $\mathrm{tr}_{M, \ell}(T_w)
\in \mathbb{Q}(q)$.  The cyclotomic residue*

$$
  \mathrm{Res}_{q \to \zeta_\ell}(\Phi_q \cdot \mathrm{tr}_{M, \ell})(T_w)
$$

*is well-defined as the image of $\Phi_q \cdot \mathrm{tr}_{M, \ell}(T_w)$
under the cyclotomic projection*

$$
  \pi_{n_\ell}
  \;:\;
  \widehat{\mathbb{Z}[q]}
  \longrightarrow
  \mathbb{Z}[q] / \Phi_{n_\ell}(q),
$$

*viewed as an element of the residue field $\mathbb{Q}(\zeta_\ell)$
via the natural isomorphism*

$$
  \mathbb{Z}[q] / \Phi_{n_\ell}(q)
  \;\cong\;
  \mathbb{Z}[\zeta_\ell].
$$

*Equivalently, in the standard $q$-series language:*

$$
  \mathrm{Res}_{q \to \zeta_\ell}(\Phi_q \cdot \mathrm{tr}_{M, \ell})(T_w)
  \;=\;
  \frac{(\Phi_q \cdot \mathrm{tr}_{M, \ell}(T_w))}{\Phi_{n_\ell}(q)}
  \pmod{\Phi_{n_\ell}(q)}.
$$

## Replacement of the class field representation

The Lean formulation in
[`gb-residue-spectral-sum.lean`](gb-residue-spectral-sum.lean)
treats the residue as an abstract class field:

```lean
residue : Fin levelBound → ℝ
```

This effectively treats the residue as an unspecified function returning a real number — which forces the formalisation to live over $\mathbb{R}$ and implicitly relies on complex analysis to compute residues at unit-circle roots.

The proposition above replaces this by a constructive algebraic
definition entirely inside $\widehat{\mathbb{Z}[q]}$: cyclotomic
projection plus the Habiro-ring isomorphism. (A full Lean 
formalisation of this constructive approach is a deferred 
multi-week effort for the `QOU.AlgebraicSubstrate` layer.) Three things become
immediate:

1. **No analytic continuation.** The residue is a quotient by a
   cyclotomic polynomial, not a complex-analytic limit.
2. **Algebraic-side stays in $\mathbb{Q}(\zeta_\ell)$.** The
   Lean type changes from `ℝ` to `LaurentPolynomial ℚ` (or, more
   precisely, an element of the cyclotomic ring
   $\mathbb{Z}[\zeta_\ell]$), aligning with the three-calibration
   discipline
   ([`prop:three-calibration-discipline`](../observations/three-calibration-discipline.md))
   that the algebraic side lives in $\mathbb{Q}$-coefficients.
3. **Compatibility with the spectral sequence** of
   [`prop:gb-spectral-sequence`](#prop:gb-spectral-sequence) is
   automatic — the $E_\infty$ page reads off the cyclotomic
   projections of the graded trace.
<!-- FILE_END: residue-at-root.md -->

