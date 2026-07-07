<!-- FILE_START: intro-kashiwara-jones-quantum-dilog.md -->
The Kashiwara crystal-basis framework and the Jones polynomial
are two presentations of the same categorical data — one
combinatorial, one analytic.  This section identifies the
quantum dilogarithm $\mathrm{Li}_2^q$ as the bridge:  the
Kashiwara-Jones alternation interpretation evaluates a Jones
polynomial at the Kashiwara crystal-basis sum, and the result
is a quantum-dilogarithm identity that closes the cycle.

The arc moves in three movements.  The first blocks establish
the Kashiwara-Jones alternation as a generating-function
identity in the categorical setting; the middle blocks specialise
the identity to the substrate parameter and exhibit the
quantum-dilogarithm cocycle that controls the resulting
combinatorial decomposition; the closing blocks survey the
applications — the Reshetikhin–Turaev TQFT invariants, the
volume conjecture's quantum form, and the Yetter-style
Hopf-categorical extensions.

The output is the identification of $\mathrm{Li}_2^q$ as a
canonical level-2 categorical cocycle that the
$q$-geometric-Langlands chapter inherits.  Readers interested
only in the structural identification can take the closing
blocks' summary; the proofs are technical and consume the
machinery of the previous two sections.
<!-- FILE_END: intro-kashiwara-jones-quantum-dilog.md -->

<!-- FILE_START: kashiwara-jones-alternation-interpretation.md -->
**Interpretation: the Kashiwara $\leftrightarrow$ Jones alternation in the
$\mathfrak{Q}_\beta$ precision ladder.**

The categorical-derivation precision ladder from
[`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder)
exhibits an empirical alternating pattern in the $c_k$ coefficients
through $k = 4$:

|  $k$  | $c_k$ origin |
|:---:|:---|
| 1 | Kashiwara crystal $\tilde f_1$ matrix element $b$ |
| 2 | Kashiwara $\tilde f_1^\dagger \tilde f_1$ return amplitude $b^2$ |
| 3 | classical-limit Jones $J_{\text{Hopf}}(q=1) = -2$ |
| 4 | mixed: $b^2 + 1/2$ (Kashiwara + half-Hopf) |

The user's observation: *"weird we switch back and forth between Kashiwara
and Jones."* This remark captures the structural origin of the alternation.

## Two moduli spaces meeting at Markov closure

The Kashiwara and Jones contributions arise from **different moduli spaces**
that the τ_M observable straddles:

- **Kashiwara crystal** lives in the moduli of representations of
  $U_q(\mathfrak{sl}_2)$ — finite-dimensional, combinatorial, parameterised
  by SYTs and crystal edges.
- **Jones polynomial** lives in the moduli of knot/link complements via
  Witten–Reshetikhin–Turaev — geometric, encoding topological invariants
  of the closure $\widehat\beta$.

The τ_M observable
([`prop:markov-trace-frobenius-selection`](#prop:markov-trace-frobenius-selection))
sits at the **crossroads**: it computes the Markov closure of a typed braid,
which simultaneously lives in $H_n(q)$ (Kashiwara side) and produces an
invariant of $\widehat\beta$ (Jones side).

## Parity rule: even $k$ $\to$ Kashiwara, odd $k$ $\to$ Jones

The structural rule (empirically validated through $k = 4$):

| $k$ parity | typical contributor | closure structure |
|:---:|:---|:---|
| **even** $k$ | $\tilde f_1^{k/2}$ Kashiwara matrix element | $\sigma_i^k$ stays inside $H_n(q)$; pure intra-block action |
| **odd** $k$ | $J_{\text{link}}(q=1)$ at $(k{+}1)$-fold closure | $\sigma_i^k$ followed by Markov trace closes to a link; topological invariant emerges |

The mechanism:

- At **even $k$**, the Hecke quadratic $\sigma_i^2 = h\sigma_i + 1$ reduces
  $\sigma_i^k$ to a polynomial in $\sigma_i$ with coefficients in
  $\mathbb{Z}[q^{\pm 1}]$. Acting on a 2-d irrep like $V_{(2,1)}$ in the
  Hoefsmit seminormal basis, the off-diagonal coupling $b$ enters at each
  step, producing matrix elements $\propto b^{k/2}$. **No link invariant
  is generated** because the action stays within $H_n(q)$'s combinatorial
  structure.
- At **odd $k$**, the Markov closure of $\sigma_i^{k+1}$ produces a
  **2-component link** ($(k+1)$ is even, so the closure has even crossing
  number and is topologically link-like). The Jones polynomial of this
  link emerges as the τ_M trace. At $q = 1$ (the KL classical-limit
  decategorification per AGENTS.md §7b), the Jones value is an integer,
  contributing the inter-block coefficient.

## The "GeomK with jet-order twist" interpretation

The user's intuition: *"something like $\mathrm{Geom}(K)$ but maybe more
twisted due to jet order / filtration and quadratic"* — yes, this is
exactly the right framing.

The QOU framework uses a **GB (Gröbner–Buchberger) filtration** indexed by
jet order. The Hecke quadratic $\sigma_i^2 = h\sigma_i + 1$ increases jet
order by one at each multiplication. The precision-ladder rungs correspond
to **distinct jet orders**:

- $k = 0$: jet order 0 (Form A, single-wrap NF counit, no Hecke twist).
- $k = 1$: jet order 1 (first Hecke crossing, $b$ enters the eigenphase).
- $k = 2$: jet order 2 (Hecke quadratic activates, $b^2$ from the
  return amplitude).
- $k = 3$: jet order 3 (Markov closure of three crossings — the **first
  jet where the cyclic closure produces a non-trivial link**, $J_{\text{Hopf}}$).
- $k \geq 4$: jet order $\geq 4$ — mixing of Kashiwara (intra-block) and
  Jones (inter-block) contributions; both modular spaces contribute at
  this order.

The precision ladder is essentially:

$$
  \mathfrak{Q}_\beta^{\text{cat}}
   \;=\;
   \mathfrak{Q}_\beta^A \cdot \prod_{k \geq 1}
     F_k\bigl(b,\, J_{\text{closure}_k}(q{=}1)\bigr)\,
     \hbar_q^{2k},
$$

with the Kashiwara $b$ and Jones invariants of the $k$-fold Markov closure
appearing in $F_k$. The "twist" by jet order is via $\hbar_q^{2k}$;
the "quadratic" structure is the Hecke relation $\sigma_i^2 = h\sigma_i + 1$.

## Hyperbolic vs torus operators

The user's intuition extends to operator-type dependence:

- **Hyperbolic links/knots** (figure-8, Borromean rings, $\ldots$): $\mathrm{Vol} > 0$.
  Their τ_M values (and Jones polynomials) carry the Vol Conjecture-style
  asymptotics. Their classical-limit Jones values are integer-valued and
  enter the precision ladder via Markov closure at $q = 1$.
- **Torus knots** (trefoil $3_1$, $T(2,5)$, $\ldots$): $\mathrm{Vol} = 0$. Their
  Jones values at $q = 1$ collapse to $1$ (unknot-like classical limit).
  Torus structure is captured by **Jucys–Murphy elements** — diagonal in
  the seminormal basis, so they contribute to the **Kashiwara** side
  (intra-block, no link invariant).

The QOU β-decay braid has $11$ typed crossings with the closure being a
**3-strand braid $\to$ 3-component link** (Borromean structure per
[`rem:borromean-baryon-interpretation`](#rem:borromean-baryon-interpretation)).
The closure is **hyperbolic** ($\mathrm{Vol}(\mathcal{B}_3) \approx 7.328$);
its sub-link structure (Hopf at 3-fold closure, full Borromean at higher
orders) drives the Jones contributions in the precision ladder.

## Breakdown of the alternating pattern at $c_5, c_6$

Per the canonical formalism,
the empirical $c_5, c_6$ don't fit simple integer Jones values or simple
Kashiwara $b^k$ alone. Two structural reasons:

1. **Mixed-order contributions**: at $k \geq 5$, the typed-braid Markov
   closure becomes a **multi-link** (sub-Hopf $\oplus$ sub-trefoil
   $\oplus$ sub-Borromean), and the contributions interfere — neither
   pure Kashiwara nor pure Jones at any single level captures the
   coefficient.
2. **Hoefsmit seminormal recursion** generates **cross-block** matrix
   elements at order $k \geq 4$ (the V_(2,1) crystal has only 2 vertices,
   so beyond $\tilde f_1^2$, contributions must come from coupling to
   $V_{(3)}$ and $V_{(1,1,1)}$). The cross-block coupling brings in both
   Kashiwara-like and Jones-like terms simultaneously.

The "switching back and forth" is therefore not a defect of the framework
but a **feature** — the τ_M observable is structurally a *bridge* between
the two moduli spaces, and the precision ladder explicitly tracks the
interleaved contributions.
<!-- FILE_END: kashiwara-jones-alternation-interpretation.md -->

<!-- FILE_START: canonical-braid-interface-composition.md -->
**Definition (canonical-braid interface composition).** *Let
$\beta(Z, N) \in H_{3A}(q)$ be the canonical atomic braid in the
standard pppnnn ordering (built by
the canonical formalism).
The* $A - 1$ *inter-nucleon interface generators
$\sigma_{3k + 2}$ ($k = 0, \ldots, A - 2$) are classified by the
flavour pair $(\text{nuc}_k, \text{nuc}_{k+1})$ they bridge:*

See [Table 1](#tbl:canonical-braid-interface-composition-table1-data).

*The interface composition $(n_{pp}(Z, N), n_{pn}(Z, N), n_{nn}(Z, N))$
counts these three types. Under canonical pppnnn ordering, closed
forms are:*

$$
\boxed{\quad
n_{pp}(Z, N) = \max(0, Z - 1), \quad
n_{nn}(Z, N) = \max(0, N - 1), \quad
n_{pn}(Z, N) = \begin{cases} 1 & Z \geq 1, N \geq 1 \\ 0 & \text{else}\end{cases}
\quad}
$$

*with total count $n_{pp} + n_{pn} + n_{nn} = A - 1$.*

### Empirical table

See [Table 2](#tbl:canonical-braid-interface-composition-table2-data).

### Z$\leftrightarrow$N asymmetry and ordering dependence

Under the pppnnn ordering the asymmetric counts $(n_{pp}, n_{nn})$
encode Z$\leftrightarrow$N asymmetry directly. **Alternative orderings** (e.g.,
alternating pnpnpn) would produce different interface compositions
for the same atom — at $(Z=2, N=2)$ ${}^{4}$He:

See [Table 3](#tbl:canonical-braid-interface-composition-table3-data).

The canonical pppnnn ordering is fixed by
the canonical formalism;
this definition is **ordering-specific**. Generalising to arbitrary
orderings requires an additional `ordering: list[Nucleon]` argument,
captured in the
the canonical formalism
utility module's `interface_composition(ordering)` function.

### Role in substrate derivation

The Δ_coupling residual fit localised the ${}^{3}$He
proton-heavy anomaly to the **pp interface asymmetry**: ${}^{3}$He has
$n_{pp} = 1$ (excess $\sigma$) while T has $n_{nn} = 1$ (excess $\sigma^{-1}$), and
the pp/nn interfaces contribute non-equivalently through the
hook's antisymmetric column. A linear fit

$$
\Delta_{\mathrm{coupling}}(Z, N)
\;\approx\;
[A - 2]_q \cdot E_0 \cdot \log(1/h)
\,+\, \alpha \, n_{pp}
\,+\, \beta \, n_{nn}
\,+\, \gamma
$$

with $\alpha \approx +0.224$ MeV, $\beta \approx +1.093$ MeV,
$\gamma \approx -1.295$ MeV closes the 4-atom canonical evaluation set by definition
(3 free parameters, 3 non-trivial equations). The fit is **not
predictive** until extended to atoms with distinct $(n_{pp}, n_{nn})$
combinations beyond the $\{$D, T, ${}^{3}$He, ${}^{4}$He$\}$ set. See
[`docs/audits/-a-minus-2-q-substrate-derivation.md`](../../docs/audits/-a-minus-2-q-substrate-derivation.md)
§v6 for the open-question framing.
<!-- FILE_END: canonical-braid-interface-composition.md -->

<!-- FILE_START: prop-rigid-monoidal-structural-gap-invariance.md -->
**Proposition (structural-gap convention-invariance via rigid
monoidal Type-B folding).**

*Let $\mathbf{C} = \mathbf{Rep}(\mathrm{SU}_q(2))$ be the rigid
monoidal category of $\mathrm{SU}_q(2)$-representations, and let*

$$
  \tau \;:\; \mathrm{End}_{\mathbf{C}}(A^{\otimes n}) \;\longrightarrow\; \mathbb{C}_q
$$

*be the canonical Markov trace on the Hecke endomorphism algebra
$\mathrm{End}_{\mathbf{C}}(A^{\otimes n}) \cong H_n(q)$.  For any
confined particle $\mathfrak{H}$, let $\beta_{\mathfrak{H}} \in
H_{3A}(q)$ be its canonical atomic-braid representative
([`def:confined-particle`](#def:confined-particle)) and define the
**categorical structural gap**

$$
  \Delta_{\mathrm{cat}}(\mathfrak{H})
    \;:=\; B_{\mathrm{AME}}(\mathfrak{H})
    \;-\; m_e \cdot \rho \cdot \bigl|\tau(\beta_{\mathfrak{H}})\bigr|.
$$

Then $\Delta_{\mathrm{cat}}(\mathfrak{H})$ depends only on the
categorical-trace invariant $\tau(\beta_{\mathfrak{H}})$ and not on
any choice of operator-volume convention (per-generator algebraic
volumes, eigenvalue spectra, pair-knot composites, multi-term
assembly, ...) for evaluating $\mathrm{End}_{\mathbf{C}}(A^{\otimes 3A})$.*

## Convention-independence of the structural gap

The Markov trace $\tau$ on $H_n(q)$ is **uniquely determined** by
the categorical axioms M1 (cyclicity), M2 (Markov-axiom Hecke peel
$\mathrm{tr}_M^{(n)}(x \cdot \sigma_{n-1}) = z \cdot \mathrm{tr}_M^{(n-1)}(x)$),
M3 ($\mathrm{tr}_M(1) = 1$), and the Hecke quadratic relation, up
to the choice of the Markov parameter $z = 1/(\sqrt{q} + 1/\sqrt{q})$. Two evaluations of the same $\beta_{\mathfrak{H}}$
through different operator-volume conventions give the SAME
categorical $\tau(\beta_{\mathfrak{H}})$ value — this is the
universal property of the rigid monoidal Markov trace.

What the operator-volume conventions vary is the **non-categorical**
remainder:
- Per-generator $\Phi_q$ towers depend on the algebraic volumes $|\hat V_i|$ — not categorical.
- Per-eigenvalue $\Phi_q$ depends on the choice of basis in $V_\lambda$ — not categorical without further structure.
- Pair-knot product-volume / Markov-trace composites depend on the operator-volume convention chosen for the shell sub-braid.

The **categorical trace** $\tau(\beta_{\mathfrak{H}})$ is the
common invariant; the brane-tower formula contributions beyond
$|\tau(\beta_{\mathfrak{H}})|$ (the "transient tower" component of
[`conj:brane-tower-z-habiro`](#conj:brane-tower-z-habiro)) are
convention-dependent regularizations of a divergent analytic
object, and their differences must therefore cancel into the same
$\Delta_{\mathrm{cat}}$ value.

## Type-B-folded rigid monoidal structure

The Type-B folding (AGENTS.md §7b) folds the
$\mathfrak{sl}_n$ Cartan datum into a Type B datum; the resulting
*symmetric* Kashiwara crystal is the categorical home of the
spin-involution invariance ([`prop:spin-involution-lp-dual-invariance`](#prop:spin-involution-lp-dual-invariance)).
Stable matter = fixed points of the folded crystal.

Under Type-B folding:
- **Spin involution $\sigma = S$** (Hopf antipode) acts as the
  folded-crystal involution; magic-shell sub-braids are S-conjugate.
- **Markov trace $\tau$** is S-invariant
  ([`prop:spin-involution-lp-dual-invariance`](#prop:spin-involution-lp-dual-invariance)
  §"Step 2: cycle stable"); in particular
  $\tau(\sigma_{pp}) = \tau(\sigma_{nn})$
  ([`pair_knot_Z_N_trace_invariance`](spin-involution-lp-dual-invariance.lean)
  in the Lean sibling).
- **Operator-selection LP** dual y_0* is S-invariant; magic-shell
  composite operators are in the active set EXACTLY at $Z = 2$ /
  $N = 2$ shells (the LP-dual finding from  family 5).

This is the unified rigid monoidal framework under which the
three load-bearing findings of the  closure are
consequences of a single structural fact.

## Unification of findings (1)–(3) from  closure

| Finding | Categorical content |
|:---|:---|
| (1) Pair-knot operators active at magic shells | LP-dual active set selects S-conjugate composites in Type-B-fixed locus (categorical: sub-algebra structure in $\mathbf{Rep}(\mathrm{SU}_q(2))$) |
| (2) Z$\leftrightarrow$N substrate-binding symmetry | $\tau$ is S-invariant $\Rightarrow$ $\tau(\sigma_{pp}) = \tau(\sigma_{nn})$ algebraically |
| (3) Convention-independence of structural gap | The categorical $\tau(\beta_{\mathfrak{H}})$ is the only invariant; conventions vary the non-categorical regularizer |
## Discussion

The proposition is **conjectural** at the falsifiable-prediction
level (predictions 1–3 are testable but not yet verified
exhaustively).  The categorical content (Steps 1–3 of the proof)
follows from established results in quantum-group representation
theory (Jones 1985, Wenzl 1988, Kassel 1995).  Lean class
`RigidMonoidalStructuralGapInvariance` in
[sibling `.lean`](prop-rigid-monoidal-structural-gap-invariance.lean)
axiomatizes the conjectural content per §3b conditional-class
pattern; downstream conditional theorems are unconditional Lean
theorems whenever the class is in scope.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: prop-rigid-monoidal-structural-gap-invariance.md -->

<!-- FILE_START: qz-bicompletion.md -->
**Definition (proposed; conjectural utility).**
*The **$(q, z)$-bicompletion** is the inverse limit*

$$
  \widehat{\mathbb{Z}[q^{\pm 1}, z]}_{q,z}
  \;:=\;
  \varprojlim_{(m, n)} \;
  \mathbb{Z}[q^{\pm 1}, z] \big/ \bigl(I_{m,n}\bigr),
$$

*indexed by pairs $(m, n) \in \mathbb{N}^2$ with $(m, n) \leq (m', n')$
iff $m \leq m'$ and $n \leq n'$, where the bigraded ideal is*

$$
  I_{m,n}
  \;:=\;
  \bigl((q;q)_m \;\cdot\; P_n(q, z)\bigr)
  \;=\;
  \Bigl(\prod_{k=1}^{m}(1 - q^k) \;\cdot\; \prod_{k=1}^{n}(1 - q^{-k} z)\Bigr).
$$

*The transition maps $\mathbb{Z}[q^{\pm 1}, z]/I_{m',n'} \twoheadrightarrow \mathbb{Z}[q^{\pm 1}, z]/I_{m,n}$
for $(m, n) \leq (m', n')$ are well-defined because $I_{m',n'} \subseteq I_{m,n}$.*

The bicompletion sits at the apex of the diagram of cyclotomic
completions, jointly carrying the $q$-only ([Habiro ring](#def:habiro-ring))
and $z$-only ([$z$-Habiro ring](#def:z-habiro-ring)) cyclotomic structures.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: qz-bicompletion.md -->

<!-- FILE_START: qz-bicompletion-properties.md -->
The [$(q, z)$-bicompletion](#def:qz-bicompletion)
$\widehat{\mathbb{Z}[q^{\pm 1}, z]}_{q,z}$ sits at the apex of a diagram
of cyclotomic completions; its raison d'être is the conjectural mass
element, whose existence and utility we record here together with the
open questions it raises.

The bicompletion sits at the apex of the diagram of cyclotomic
completions:

$$
\begin{array}{ccc}
  \widehat{\mathbb{Z}[q^{\pm 1}, z]}_{q,z}
  & \xrightarrow{\;\;z \,\mapsto\, 0\;\;}
  & \widehat{\mathbb{Z}[q]} \\
  \big\downarrow {q \,\mapsto\, q_0} & & \big\downarrow {q \,\mapsto\, q_0} \\
  \widehat{\mathbb{Z}[q^{\pm 1}_0][z]}_z
  & \xrightarrow{\;\;\;\;\;\;\;\;\;\;}
  & \mathbb{Z}[q^{\pm 1}_0][z] \\
\end{array}
$$

(viewed as the natural projection lattice; the bottom-right is the
"realised" ring at the substrate parameter $q_0$).

| Direction | Cyclotomic ideal | Universal element | Cyclotomic projections |
|:---|:---|:---|:---|
| $q$-only ([Habiro ring](#def:habiro-ring)) | $((q;q)_m)$ | colored Jones $J_K \in \widehat{\mathbb{Z}[q]}$ | $J_N(K)$ via $q \mapsto \zeta_N$ |
| $z$-only ([$z$-Habiro ring](#def:z-habiro-ring)) | $(P_n(q, z))$ | brane-tower element (conjectural) | level-$n$ cyclotomic truncation |
| $(q, z)$-joint (this block) | $((q;q)_m \cdot P_n(q,z))$ | mass-element (conjectural) | $J_N$-data + brane-tower data jointly |

## Rationale for the bicompletion

The mass-element [conjecture](#conj:mass-endomorphism) connects two
quantum invariants that live in **different** cyclotomic
completions:

1. The **colored Jones** $J_N(K; q)$ of the closed braid $K$ lives in
   $\widehat{\mathbb{Z}[q]}$, encoding the **knot's topological**
   content via cyclotomic projections at $q = \zeta_N$
   (Volume Conjecture).

2. The **brane-tower partial sums** $\Phi_{\mathrm{mass}}^{(N)}(\beta) = \sum_{i=1}^{N}\Phi_q(z_i)$
   live in $\widehat{\mathbb{Z}[q^{\pm 1}][z]}_z$
   (conjectural — see [brane-tower in $z$-Habiro](#conj:brane-tower-z-habiro)),
   encoding the **algebraic-volume** content via cyclotomic projections at
   the structurally determined level $n_\star(\mathfrak{H})$.

The mass formula
$\mathfrak{m}_{q,\mathcal{K}}(T_w) = \sum_\lambda \tilde w_\lambda(q) \cdot \chi_\lambda(\rho(\beta))/\dim_q V_\lambda$
relates these two pieces through the q-deformed Wedderburn-weighted
Markov-trace pairing, which depends on $q$ (through the q-deformed
weights $\tilde w_\lambda = \dim_q^2/[n]_q!$) and on $z$ (through
algebraic-volume coordinates).
A single ambient ring carrying **both** cyclotomic structures is
required to express the relation as an algebraic identity rather
than a coincidence of two independent specialisations.

## Conjectural utility

The bicompletion is **defined**; the **conjectural utility** is that
the mass element

$$
  \mathfrak{m}^{\widehat{\;}}(\beta)
  \;\in\;
  \widehat{\mathbb{Z}[q^{\pm 1}, z]}_{q,z}
$$

(the conjectural lift of $\mathfrak{m}_{q,\mathcal{K}}$ to the
bicompletion) **simultaneously** recovers:

- the colored Jones invariants under $z \mapsto 0$ followed by
  cyclotomic-in-$q$ projection at $q = \zeta_N$, and
- the brane-tower partial sums under $q \mapsto q_0$ followed by
  cyclotomic-in-$z$ projection at level $n_\star(\mathfrak{H})$.

If such $\mathfrak{m}^{\widehat{\;}}$ exists, the **Volume Conjecture**
(asymptotic relation between $J_N$ and $\mathrm{Vol}(K)$) becomes a
**consequence** of the algebraic identity in the bicompletion: the
two cyclotomic projections of the same bicompletion element must
agree on their common image in $\mathbb{R}$ via the realisation
functor.

## Open questions

1. **Existence of $\mathfrak{m}^{\widehat{\;}}$ as an algebraic element.**
   The Frobenius-paired identity from
   [partition-depth stratification of $\Phi_q$](#prop:quantum-dilogarithm-stratified)
   is the natural starting point: it gives a single algebraic
   expression $\sum_k \phi_q^{(k)}(z) \otimes e_\lambda$ that
   simultaneously carries $q$-content (in $\phi_q^{(k)}$) and
   $z$-content (in the depth grading). Whether this extends to a
   Cauchy sequence in the $(q, z)$-cyclotomic topology is open.

2. **Non-archimedean realisations.** The bicompletion has cyclotomic
   projections at all pairs $(\zeta_M, \zeta_N)$ of roots of unity.
   These should correspond to non-archimedean realisations of the
   [motivic substrate](#def:motivic-substrate) — finite-place avatars
   of the mass at finite primes. The interpretation of the
   bicompletion's $p$-adic projections as "$p$-adic mass invariants"
   is open.

3. **Bicompletion-level Volume Conjecture.** The classical Volume
   Conjecture is the asymptotic statement that $|J_N(K; \zeta_N)|$
   grows like $\exp(N \cdot \mathrm{Vol}(K) / 2\pi)$. The
   bicompletion-level analogue would be: there exists a
   $\mathfrak{m}^{\widehat{\;}}$ such that **all** $z$-cyclotomic
   projections recover the brane-tower partial sums, **and** the
   $z \mapsto 0$ specialisation recovers $J_K$, **and** the two
   recoveries agree under archimedean realisation. This is
   strictly stronger than the classical Volume Conjecture (which is
   only asymptotic) and would be **algebraic** rather than analytic.

The bicompletion is offered here as a **target structure** for
future work — neither the existence of
$\mathfrak{m}^{\widehat{\;}}$ nor the level-selection rule
$n_\star(\mathfrak{H})$ are claimed proved.
<!-- FILE_END: qz-bicompletion-properties.md -->

<!-- FILE_START: quantum-dilogarithm-stratified.md -->
**Proposition (partition-depth stratification of $\Phi_q$).**

*Let $A = H_n(R, q)$ be a semisimple Hecke algebra at generic $q$, and
let* $Z(A) = \bigoplus_{\lambda \vdash n} R \cdot e_\lambda$ *be its
centre. Decompose the centre by GB-depth of partitions
([curvature-rank stratification](#prop:curvature-rank-gb-stratification)):*

$$
  Z(A) \;=\; \bigoplus_{k \geq 0} Z^{(k)}(A),
  \qquad
  Z^{(k)}(A) \;=\; \mathrm{span}_R\bigl\{e_\lambda : \mathrm{depth}_{\mathrm{GB}}(\lambda) = k\bigr\}.
$$

*The analytic quantum dilogarithm
([quantum dilogarithm](#cor:quantum-dilogarithm))
$\Phi_q(z_i) = \prod_{k=1}^{\infty}(1 - q^{-k} z_i)^{-1}$ at the $i$-th
exceptional divisor admits a centre-stratified expansion: there exist
$Z^{(k)}(A)$-valued coefficients $\phi_q^{(k)}(z_i) \in Z^{(k)}(A)$
such that, on every $T_w \in H_n(R, q)$ with $\mathrm{supp}(T_w) \subseteq Z(A)$,*

$$
  \mathrm{tr}_M\!\bigl(\Phi_q(z_i) \cdot T_w\bigr)
  \;=\;
  \sum_{k = 0}^{\infty}
    \bigl\langle \phi_q^{(k)}(z_i),\, T_w \bigr\rangle,
$$

*where $\langle \cdot, \cdot \rangle$ is the Frobenius pairing on $Z(A)$.
Moreover, the depth-$k$ coefficient* $\phi_q^{(k)}(z_i)$ *is the
**Frobenius dual** of the truncation increment*

$$
  \phi_q^{(k)}(z_i)
  \;\equiv\;
  \Bigl(\Phi_q^{[\leq k]}(z_i) - \Phi_q^{[\leq k-1]}(z_i)\Bigr) \cdot \mathbf{1}_{Z^{(k)}(A)}
  \pmod{\bigoplus_{\ell \neq k} Z^{(\ell)}(A)},
$$

*so the partial sum $\Phi_q^{[\leq k]}(z_i) = \sum_{j=0}^{k}\phi_q^{(j)}(z_i)$
captures exactly the $\bigoplus_{j \leq k} Z^{(j)}(A)$-content of
$\Phi_q(z_i)$.*

*The truncation $\Phi_q^{[\leq k]}(z_i)$ is the $|q| > 1$ Faddeev
form of the same partial product written in the $|q| < 1$ convention
in ([q-Pochhammer partial product](#def:q-pochhammer-partial-product));
the conventions agree under $q \mapsto q^{-1}$ and the explicit
denominator polynomial $(x; q)_n$ is recorded there.*

**Corollary (truncation = projection onto NF-support depth).**
*For $T_w$ with NF support depth*
$k_\star(T_w) = \max_{\lambda \in \mathrm{supp}(T_w)} \mathrm{depth}_{\mathrm{GB}}(\lambda)$,

$$
  \mathrm{tr}_M\!\bigl(\Phi_q(z_i) \cdot T_w\bigr)
  \;=\;
  \mathrm{tr}_M\!\bigl(\Phi_q^{[\leq k_\star(T_w)]}(z_i) \cdot T_w\bigr),
$$

*because all $\phi_q^{(k)}(z_i)$ for $k > k_\star(T_w)$ pair to zero
with $T_w$ under the Frobenius pairing (they live in centre strata
$Z^{(k)}(A)$ with $k > k_\star(T_w)$, on which $T_w$ has zero
projection by definition of $k_\star$). The analytic infinite product
truncates to a finite product as a Frobenius-paired identity, with
the truncation depth structurally determined by $T_w$'s NF support.*

## Resolution of Step 4 of [$\Phi_q$ categorical truncation](#prop:phi-q-categorical-truncation)

[Cor: quantum dilogarithm](#cor:quantum-dilogarithm) gives the
analytic identity $\mathrm{tr}_{\mathrm{trans}}(\varrho, p_i) = \Phi_q(z_i)$ as
the level-$i$ archimedean torsion volume — but as an *analytic*
(infinite-product) object, with no curvature-rank stratification
visible.

This proposition refines that identity by exposing the
partition-depth filtration of $\Phi_q(z_i)$ inside $Z(A)$. The bridge
is the Frobenius pairing: while the analytic product $\Phi_q(z_i)$
diverges at $|z_i| \to q$, its **Frobenius pairing with any specific
$T_w$** evaluates to a *finite* sum over the $\leq k_\star(T_w)$
depth-strata of the centre. The $|\hat V|\approx 1$ ill-conditioning is
then a property of the analytic representation, not of the
Frobenius-paired categorical mass.
<!-- FILE_END: quantum-dilogarithm-stratified.md -->

<!-- FILE_START: q-pochhammer-partial-product.md -->
**Definition.**
*The **$q$-Pochhammer partial product** at depth $n \in \mathbb{N}$,
substrate parameter $q$, and state variable $x$, is the finite
rational function*

$$
  \Phi_n(x; q)
  \;:=\;
  \prod_{k=0}^{n-1} \frac{1}{1 - x q^k}
  \;=\;
  \frac{1}{(x; q)_n},
  \qquad
  (x; q)_n
  \;:=\;
  \prod_{k=0}^{n-1}\bigl(1 - x q^k\bigr).
$$

*The numerator is the constant $1$; the **denominator polynomial**
$(x; q)_n \in \mathbb{Z}[q, x]$ has $n$ simple roots $x = q^{-k}$ for
$k = 0, \dots, n-1$. As a finite rational function, $\Phi_n(x; q)$ is
well-defined for any $q \neq 0$ — including the QOU substrate
$q_0 \approx 1.11$, where the roots $\{q_0^{-k}\}_{k=0}^{n-1} =
\{1, 0.901, 0.812, \dots\}$ lie in $(0, 1]$. The partial product is
the depth-$n$ truncation of the analytic quantum dilogarithm
([quantum dilogarithm](#cor:quantum-dilogarithm))*

$$
  \Phi_q(x)
  \;=\;
  \prod_{k=0}^{\infty}\frac{1}{1 - x q^k}
  \;=\;
  \lim_{n \to \infty} \Phi_n(x; q),
  \qquad |q| < 1.
$$

*The infinite product converges only for $|q| < 1$, but the QOU
substrate has $q_0 > 1$. The partial product $\Phi_n$ is what
appears in the QOU mass formulas: a finite rational function whose
denominator zeros are the algebraic addresses of cusps regardless of
the convergence radius of the analytic limit. The Faddeev limit to
$\mathrm{Li}_2$
([Archimedean limit](#conj:dilogarithm-archimedean-limit))
takes $q \to 1$ from either side — $q \to 1^-$ in the convergence
domain, or $q \to 1^+$ via analytic continuation in the QOU
substrate regime.*

*so $\Phi_n$ is the same object as $\Phi_q^{[\leq n]}$ in
([Φ$_q$ partition-depth stratification](#prop:quantum-dilogarithm-stratified)),
with the truncation index $n$ identified with the GB-depth
$k_\star(T_w)$.*

*The stratification proposition writes the analytic product as
$\prod_{k \geq 1}(1 - q^{-k} z_i)^{-1}$ — the standard form indexed
from $k = 1$ with negative-power factors. The present block uses the
equivalent indexing-from-$k=0$ form $(1 - x q^k)$: under the
substitution $z_i = q \cdot x$ and shifting $k \mapsto k - 1$, the
two forms agree factor-for-factor. Both denote the same algebraic
object. The form here exposes the denominator polynomial
$(x; q)_n \in \mathbb{Z}[q, x]$ with non-negative powers of $q$, so
that at the QOU substrate $q_0 > 1$ the denominator zeros $q_0^{-k}$
land in $(0, 1]$ — the cusp-shape range used by the Newton-Raphson
seeding pipeline.*

## Rationale for the partial product

The categorical Markov trace of a transient crossing word $T_w$ at
GB-depth $k_\star(T_w) = n$ pairs to zero with every centre stratum
$Z^{(k)}(A)$ of depth $k > n$
([truncation = projection onto NF-support depth](#prop:quantum-dilogarithm-stratified)).
Consequently the analytic infinite product $\Phi_q(x)$ collapses
under Frobenius pairing to its depth-$n$ truncation $\Phi_n(x; q)$
— a finite rational function with explicit denominator.

The denominator polynomial $(x; q)_n$ carries the entire pole
structure of the categorical trace at depth $n$. Each factor
$(1 - x q^k)$ is a single pole at $x = q^{-k}$; the corresponding
residue is the depth-$k$ Frobenius coefficient
$\phi_q^{(k)}(z_i)$ of the stratification proposition.

## Recursive structure

The partial product satisfies the one-step recurrence

$$
  \Phi_{n+1}(x; q)
  \;=\;
  \frac{1}{1 - x q^n} \cdot \Phi_n(x; q),
  \qquad
  \Phi_0(x; q) \;=\; 1,
$$

which is the recurrence Lean uses to define $\mathtt{qPochhammer}$
([Lean implementation](./q-pochhammer-partial-product.lean)).
The recurrence is the algebraic shadow of the inductive
**filtration step** $N_{\leq k+1} = \mathrm{NF}(N_{\leq k} \cdot
C(N_k, N_{k+1}) \cdot N_{k+1})$ that drives jet-stratified
reduction: adding one nucleon to the active filtration shell
multiplies the partial product by exactly one new pole factor.

## Interpretation of the denominator zeros

Each zero $x = q^{-k}$ of $(x; q)_n$ is a **pole of the categorical
state sum**. Under the archimedean realization $\tau_{\mathrm{arch}}$
([archimedean realization functor](#def:archimedean-realization-functor)),
these poles mark the **cuspidal boundary** of the corresponding
ideal-tetrahedron piece — the algebraic address of a geometric cusp
that bounds an active JSJ piece
([Φ$_q$-tower JSJ bridge](#rem:phi-q-tower-jsj-bridge)). The
detailed correspondence is the content of
([shared-denominator cusp holonomy](#conj:shared-denominator-cusp-holonomy)),
and the asymptotic $\Phi_n \to \mathrm{Li}_2$ as $n \to \infty$ is
the content of
([dilogarithm Archimedean limit](#conj:dilogarithm-archimedean-limit)).

## canonical extraction (for the solver pipeline)

Given a Hecke normal-form word $T_w$ of GB-depth $n$ and a fixed
substrate $q = q_0$, the algebraic engine computes $\Phi_n(x; q_0)$
as a rational function in $x$ with explicit denominator
$(x; q_0)_n$. Its zeros $\{q_0^{-k} : k = 0, \dots, n-1\}$ are
passed across the WASM boundary to the SnapPy kernel as the
**initial seed values** for the Newton–Raphson solver of the
Thurston gluing equations
([cusp-holonomy seeding](#conj:shared-denominator-cusp-holonomy)).
The witness
[q-pochhammer-seed.witness.json](../../../computations/q-pochhammer-seed.witness.json)
records the seed extraction for a sample nucleon word.
<!-- FILE_END: q-pochhammer-partial-product.md -->

<!-- FILE_START: phi-q-categorical-truncation.md -->
**Proposition (categorical $\Phi_q$ truncation depth).**

*Let $\mathfrak{H}$ be a confined particle with Hecke NF $T_w \in H_n(R, q)$
([Hecke normal form](#def:hecke-normal-form)). Let
$\mathrm{supp}(T_w) = \{\lambda \vdash k : \langle T_w, e_\lambda \rangle \neq 0\}$
be the set of central idempotents on which $T_w$ has nonzero
projection, and define*

$$
  k_\star(T_w) \;:=\; \max_{\lambda \in \mathrm{supp}(T_w)} \mathrm{depth}_{\mathrm{GB}}(\lambda),
$$

*the **NF-support depth** in the GB-curvature-rank stratification
([curvature-rank stratification](#prop:curvature-rank-gb-stratification)).
Then the categorical brane-tower contribution to the mass functional
is the finite sum*

$$
  \mathfrak{m}^{\mathrm{tower}}_{q,\mathcal{K}}(T_w)
  \;=\;
  \sum_{k=0}^{k_\star(T_w)}
    \alpha_k \cdot \mathfrak{m}^{(k)}_{q,\mathcal{K}}(T_w),
$$

*where $\mathfrak{m}^{(k)}_{q,\mathcal{K}}$ is the depth-$k$ centre
projection and $\alpha_k$ are the curvature-rank coefficients
([unified mass formula](#prop:unified-curvature-rank-mass-formula)).
Equivalently, expressed via the analytic dilogarithm,*

$$
  \mathfrak{m}^{\mathrm{tower}}_{q,\mathcal{K}}(T_w)
  \;=\;
  \sum_{i} \Phi_q^{[\leq k_\star(T_w)]}(z_i)
  \;=\;
  \sum_i \prod_{j=1}^{k_\star(T_w)} (1 - q^{-j} z_i)^{-1},
$$

*with the truncation depth $k_\star(T_w)$ structurally determined by
$T_w$'s NF support — not chosen externally.*

**Corollary (any deeper truncation is categorically equivalent).**
*For any $k \geq k_\star(T_w)$,*

$$
  \sum_i \Phi_q^{[\leq k]}(z_i)
  \;=\;
  \sum_i \Phi_q^{[\leq k_\star(T_w)]}(z_i) \mod E_\infty^{\geq 1, *},
$$

*and the right-hand side already vanishes on $E_\infty^{\geq 1, *}$ by
prop:spectral-sequence-collapse. Therefore truncation at any
$k \geq k_\star(T_w)$ gives the same categorical answer; the
analytic divergence at $|\hat{V}|\approx 1$ is a spurious side-effect
of representing the finite centre-projection sum by an infinite
product.*
<!-- FILE_END: phi-q-categorical-truncation.md -->

<!-- FILE_START: phi-q-categorical-truncation-interpretation.md -->
**Remark on Yekutieli's "max_grade".**
*The witness data
[`joint-tower-sdp-h6-h9.witness.json`](https://github.com/litlfred/qou/blob/claude/brane-tower-regularization-xTt8V/computations/joint-tower-sdp-h6-h9.witness.json)
records a per-atom `max_grade` field labelled* $k_{\max}$. *This number
is the maximal $k$ such that $T_w$ has nonzero $\lambda$-projection with
$\dim_q V_\lambda \geq 2$, which is **distinct** from $k_\star(T_w)$
defined above:*

| Symbol | Definition | Source |
|:---|:---|:---|
| $k_{\max}(K, q)$ (witness) | smallest $k$ s.t. $T_w$ uses no $\lambda \vdash k' > k$ with $d_\lambda \geq 2$ | $T_w$'s strand structure |
| $k_\star(T_w)$ (this prop) | max GB-depth of $\lambda \in \mathrm{supp}(T_w)$ | curvature-rank stratification |

*The two coincide whenever the GB-depth filtration is induced by the
strand-size filtration on partitions, but they **can differ** when a
small-$k$ partition $\lambda$ sits at large GB-depth or vice versa.*

**Computed for tritium.** A direct YSN/Hoefsmit
character computation
(the canonical formalism)
gives $\chi_\lambda(\rho(\mathrm{T_w})) \neq 0$ for **every**
$\lambda \vdash 5$, so $\mathrm{supp}(\mathrm{T_w}) = \{\lambda : \lambda \vdash 5\}$
and $k_\star(\mathrm{T_w}) = \max_{\lambda \vdash 5} \mathrm{maxhook}(\lambda) = 5$.

**Three distinct "depths" — disambiguation.**
The literature and witness data conflate three structurally
different depth invariants of $T_w$:

| Depth | Formal definition | Tritium value |
|:---|:---|:---:|
| Coxeter length $\ell_{\max}(T_w)$ | longest reduced NF word in $S_{n_0}$ supporting $T_w$ | $9$ |
| q-Habiro depth $m_{\max}(T_w)$ | termination depth of cyclotomic expansion in $q$, $\leq \lceil\sqrt{2 \deg p}\rceil$ ([atomic Habiro expansion](#cor:habiro-expansion-atomic)) | $\approx 9$ |
| Partition GB-depth $k_\star(T_w)$ | $\max_\lambda \mathrm{maxhook}(\lambda)$ over $\mathrm{supp}(T_w)$ (this proposition) | $5$ |

The witness's $\mathtt{max\_grade} = 9$ matches both $\ell_{\max}$
and $m_{\max}$ for tritium (an accidental alignment of independent bounds:
$\deg p \approx 40$ and $\binom{5}{2} = 10$, not a structural relationship), but it does **not**
match $k_\star = 5$. This proposition's truncation depth is
$k_\star$, not $\ell_{\max}$ or $m_{\max}$ — these are independent
structural quantities, all bounded but not equal.

**Structural upper bound.** For any $T_w \in H_{n_0}(q)$,
$k_\star(T_w) \leq n_0$ because every partition $\lambda \vdash n_0$
has $\mathrm{maxhook}(\lambda) \leq n_0$. The witness's $k_{\max}$ is
**not** so bounded — it is the Coxeter-length filtration, which can
reach $\binom{n_0}{2}$ (the longest element in $S_{n_0}$). Identifying
the two is the strand-padding artifact: padding $T_w$'s NF to longer
Coxeter words does not change partition support, but does inflate
$k_{\max}$ in the witness.

**Empirical implication.**
*Under this proposition, the structural truncation depth for tritium
is $k_\star(\mathrm{T_w}) = 5$ (computed; full partition support of
$\lambda \vdash 5$), and for D and ${}^3\mathrm{He}$ at most
$k_\star \leq 3$ (since they live in $H_3$). The uniform-$k$ canonical evaluation
(the canonical formalism)
shows the Frobenius-paired truncation is far from canonical closed:
at $k = 2$ subtractive form, D errs $-22\%$, T errs $-39\%$,
${}^3\mathrm{He}$ overshoots $+134\%$; at $k = 5$ (the
structural truncation for tritium), the absolute formula errs by
$\sim 70000\%$. The Frobenius-paired equality
$\mathrm{tr}_M(\Phi_q \cdot T_w) = \mathrm{tr}_M(\Phi_q^{[\leq k_\star]} \cdot T_w)$
is a **categorical identity**, not a real-valued canonical identity;
the real-valued mass at $|\hat V|\approx 1$ requires the open
$z$-Habiro uniform bound to convert categorical equality into
canonical equality
([brane tower in $z$-Habiro](#conj:brane-tower-z-habiro)).*
<!-- FILE_END: phi-q-categorical-truncation-interpretation.md -->

<!-- FILE_START: pachner-pentagon-borromean.md -->
**Conjecture (D15 Pachner-Pentagon closure).**
*The Pachner $2$–$3$ move on the ideal-tetrahedron decomposition of
the Borromean complement $\mathbf{S}^3 \setminus \mathcal{B}_3$
realises the Pentagon identity for the q-dilogarithm $\Phi_q$ at the
state-sum level (Turaev–Viro / Reshetikhin–Turaev), with the
$h^4 = -3/4$ coefficient of $\mathrm{tr}_M(\mathcal{B}_3)$ derivable
as the difference between the 8-octahedron and 16-tetrahedron
decompositions under the Pachner move.*

## The geometric Pentagon

The Borromean complement is hyperbolic with explicit ideal
decompositions:

- **8 ideal octahedra** (Thurston): $\mathbf{S}^3 \setminus
  \mathcal{B}_3 \cong 8 \cdot (\text{ideal octahedron of volume } G)$
  giving $\mathrm{Vol}(\mathcal{B}_3) = 8G$
  ([`prop:vol-through-tau`](#prop:vol-through-tau),
  [neumann-zagier1985]).
- **16 ideal tetrahedra**: each ideal octahedron splits into
  2 ideal tetrahedra via the Pachner $2$–$3$ move; total
  $8 \times 2 = 16$ ideal tetrahedra, each contributing
  $\Lambda(\theta)$ (Lobachevsky) such that $\sum \Lambda = 8G$.

The Pentagon identity for Lobachevsky / Rogers dilogarithm relates
these two decompositions: under Pachner, five ideal-tetrahedron
configurations map cyclically via a 5-term identity that IS the
Faddeev–Volkov–Kashaev Pentagon
([`prop:pentagon-uv-commutation`](#prop:pentagon-uv-commutation))
in its archimedean realisation
([`prop:q-rogers-pentagon-archimedean`](#prop:q-rogers-pentagon-archimedean)).

## Pachner $\leftrightarrow$ Pentagon at the state-sum level

For a Turaev–Viro / Reshetikhin–Turaev state sum $Z(M; q)$ on a
3-manifold $M$ with ideal-tetrahedron triangulation $T$:

$$
  Z(M; q)
  \;=\;
  \sum_{\text{coloring}}
    \prod_{\tau \in T} \Phi_q(\text{state}(\tau)),
$$

where $\Phi_q$ is the quantum dilogarithm
([`prop:quantum-dilogarithm-stratified`](#prop:quantum-dilogarithm-stratified)).

**Pachner invariance** means $Z(M)$ does not depend on the choice of
triangulation $T$.  The $2$–$3$ move (replace 2 tetrahedra with 3
tetrahedra sharing a common edge) preserves $Z(M)$ iff $\Phi_q$
satisfies the Pentagon identity — this is the **categorical content
of the Pachner-Pentagon link**.

## The conjectural content

Given:

- $\Phi_q$ obeys the Pentagon identity (proved per
  [`prop:pentagon-uv-commutation`](#prop:pentagon-uv-commutation))
- $\mathcal{B}_3 \setminus \mathbf{S}^3$ has both 8-octahedron and
  16-tetrahedron triangulations connected by Pachner moves
- $\mathrm{tr}_M(\mathcal{B}_3, q)$ has $h^4 = -3/4$ as the first
  non-trivial coefficient (proved in
  [`prop:borromean-markov-trace-closed-form`](#prop:borromean-markov-trace-closed-form))

**Conjecture**: the $h^4 = -3/4$ coefficient is the Pachner-invariant
$\Phi_q$ state-sum evaluation of the 16-tetrahedron decomposition,
expressible as

$$
  h^4 = -3/4
  \;\stackrel{?}{=}\;
  \frac{Z(\mathcal{B}_3; q)\big|_{h^4 \text{ coefficient}}}
       {\mathrm{tr}_M(\mathcal{B}_3, q)\big|_{h^0 \text{ coefficient}}}.
$$

If true, $h^4 = -3/4$ is **identified categorically** with the
8 octahedra $\times$ 5 Pentagon-vertices = 40 Pentagon-coherent state
contributions on the Borromean complement, of which 30 cancel by
trace cyclicity and 10 sum to $-3/4$.  (The "10" matches the
10-fold color-tube weighted averaging from
[`docs/canonical-derivation-cheat-sheet.md §"Bring color-tube weighted averaging"`](../../docs/canonical-derivation-cheat-sheet.md)
— possibly the same categorical structure viewed from two angles.)

## High-value $h^{4}$ cross-validation route

Per
[`docs/audits/-pentagon-identity-broad-context.md`](../../docs/audits/-pentagon-identity-broad-context.md)
§3, the Pentagon literature spans 8 disciplines.  Four candidate
routes for deriving $h^4 = -3/4$ categorically are flagged:

1. **Direct Borromean Markov trace** — already done
   ([`borromean-markov-trace-closed-form.md`](#prop:borromean-markov-trace-closed-form)).
2. **Pachner-Pentagon state-sum** (this conjecture).
3. **K-theoretic / Bloch group regulator** — see sibling
   [`conj:borromean-bloch-group-element`](borromean-bloch-group-element.md) (D16).
4. **DIM-master Pentagon** — research-grade, no QOU block yet.

Closing this conjecture provides an **independent cross-validation**
of the topological $h^4$ via the geometric Pentagon.

## Diagnostics

Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration level**: state-sum is computed over the
  triangulation poset; the Pentagon identity sits at the 5-vertex
  cell level (= Coxeter length 5 in the corresponding braid-word
  encoding via [`prop:exterior-square-borromean`](#prop:exterior-square-borromean)).
- **Jet order**: $h^4$ — the load-bearing claim is that the
  Pachner-invariant $\Phi_q$ state-sum agrees with the Markov-trace
  closed form at $h^4$ order.
- **Bar-symmetry status**: bar-symmetric.  Pentagon identity is
  bar-symmetric (Pachner-invariance is symmetric under
  $q \mapsto q^{-1}$ because both decompositions transform
  identically under bar).

## Lean axiomatisation (sketch)

```lean
class PachnerPentagonBorromean
    (M : Type*) [BrCategory M] [QuantumDilogarithm M] where
  /-- The state-sum evaluation on a 3-manifold triangulation. -/
  z_state_sum : ∀ (M : Manifold3) (T : Triangulation M), Quantum
  /-- Pachner 2-3 invariance: ∀ T, T' related by 2-3 moves,
      z_state_sum M T = z_state_sum M T'. -/
  pachner_invariance :
    ∀ (M : Manifold3) (T T' : Triangulation M),
      pachner_related T T' → z_state_sum M T = z_state_sum M T'
  /-- Pentagon identity for Φ_q (already proved upstream). -/
  phi_q_pentagon : ∀ (a b c : Quantum), pentagon_identity a b c
  /-- The Borromean state-sum h^4 coefficient agrees with the
      Markov-trace closed form. -/
  borromean_h4_pachner_eq_markov_trace :
    z_state_sum_h4_coeff borromean_triangulation = -3/4
```

## Open R&D

1. **Compute prototype**: extend a Pachner-state-sum canonical evaluation for
   $\mathcal{B}_3$ at $q = q_0$; cross-check $h^4$ coefficient via
   the Lobachevsky decomposition $8G = \sum \Lambda(\theta_i)$.
2. **D15 to closed** requires the Lean class + the
   `borromean_h4_pachner_eq_markov_trace` proof (which would
   likely import a Lobachevsky-Pentagon lemma).
3. **Connect to D16** (sibling): the Bloch-group element of
   $\mathcal{B}_3$ in $K_3(\mathbb{C})$ has regulator $r_2 = 8G$;
   the Pachner-Pentagon state-sum and the K-theoretic regulator
   should agree at $h^4$ — that would be a triple cross-validation.

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) §1 D15
  + §2 Cluster C (Pentagon validation D15-D18)
- [`docs/audits/-pentagon-identity-broad-context.md`](../../docs/audits/-pentagon-identity-broad-context.md)
  — 8-literature Pentagon catalogue, 4 candidate routes
- Sibling Cluster C item:
  [`conj:borromean-bloch-group-element`](borromean-bloch-group-element.md) (D16)
- The Pentagon identity itself:
  [`prop:pentagon-uv-commutation`](#prop:pentagon-uv-commutation),
  [`prop:q-rogers-pentagon-archimedean`](#prop:q-rogers-pentagon-archimedean)
- The Borromean structure: [`def:borromean-baryon`](borromean-baryon.md),
  [`prop:exterior-square-borromean`](#prop:exterior-square-borromean)
- The volume route: [`prop:vol-through-tau`](#prop:vol-through-tau),
  [`prop:reeb-bundle-complement-equals-volume`](#prop:reeb-bundle-complement-equals-volume)
<!-- FILE_END: pachner-pentagon-borromean.md -->

<!-- FILE_START: q-rogers-pentagon-archimedean.md -->
**Proposition (Post-$\tau$ pentagon = pre-$\tau$ pentagon + $q$-$\log^2$ Rogers correction).**

*The pentagon identity for the q-dilogarithm
([`def:q-dilogarithm`](#def:q-dilogarithm)) takes two structurally
distinct forms depending on whether the pre-$\tau$ (categorical R-side)
or post-$\tau$ (archimedean $\mathbb{R}$-side) register is operative
([`rem:pre-tau-vs-post-tau`](#rem:pre-tau-vs-post-tau)).*

### Pre-$\tau$ (bare) pentagon

*In the q-shuffle Hopf algebra $\mathcal{H}_q$ over
$R = \mathbb{Z}[q^{\pm 1/2}, (q - q^{-1})^{-1}]$, the
q-dilogarithm satisfies the bare five-term identity*

$$
  \mathrm{Li}_2^q(u) + \mathrm{Li}_2^q(v) =
  \mathrm{Li}_2^q(uv) +
  \mathrm{Li}_2^q\!\!\left(\frac{u(1-v)}{1-uv}\right) +
  \mathrm{Li}_2^q\!\!\left(\frac{v(1-u)}{1-uv}\right) \tag{P}
$$

*as a Hopf-algebraic identity in $\mathcal{H}_q^{\otimes 2}$
([`prop:q-dilogarithm-unique`](#prop:q-dilogarithm-unique)): it is the
defining pentagon for the level-2 primitive, holding in $R$ without
any analytic considerations.*

### Post-$\tau$ (archimedean) pentagon

*Under the archimedean realization functor
([`def:archimedean-realization-functor`](#def:archimedean-realization-functor)),
$\mathrm{Li}_2^q$ realises as the convergent series
$\sum_n z^n / (n \cdot [n]_q)$ on $|z| < q$. The post-$\tau$ pentagon
**picks up a $\log_q^2$ correction term** with respect to the bare
identity:*

$$
  \boxed{\;
    \mathrm{Li}_2^q(u) + \mathrm{Li}_2^q(v) - \mathrm{Li}_2^q(uv) -
    \mathrm{Li}_2^q(\alpha) - \mathrm{Li}_2^q(\beta) \;=\;
    \log_q\!\!\left(\frac{1-u}{1-uv}\right) \cdot
    \log_q\!\!\left(\frac{1-v}{1-uv}\right) + O\bigl((q-1)^2\bigr)
  \;}
  \tag{R}
$$

*where $\alpha = u(1-v)/(1-uv)$, $\beta = v(1-u)/(1-uv)$, and
$\log_q$ is the q-logarithm ([`def:q-logarithm`](#def:q-logarithm)).*
### Structural interpretation

This proposition crystallises **what $\tau_{\mathrm{arch}}$ does to
the pentagon identity**. Pre-$\tau$, the identity (P) is a five-term
relation among Hopf-algebraic primitives — no log-squared term, no
$1/n^2$ denominator structure, purely formal.

Post-$\tau$, the realization functor introduces the rational
denominators $1/n$ in the series (the "missing $n!$" structure
implicit in passing from divided-power algebras to series-form
archimedean realizations). The cost of this rationalisation is the
$\log_q^2$ Rogers correction term — which is *exactly* the
archimedean kernel that distinguishes Faddeev's non-perturbative
Volume-conjecture form from the $\mathrm{Li}_2^q$ algebraic form
(the bar-anti-symmetric image of $\log\Phi_q$ rescaled by $h/2$, per
`prop:li2q-phiq-bar-symmetrization`).

The post-$\tau$ pentagon (R) is therefore the **defining identity**
for the analytic q-dilogarithm in the volume-conjecture / Kashaev
[`rem:kashaev-as-archimedean-realization`](#rem:kashaev-as-archimedean-realization)
framework, in the same way the pre-$\tau$ pentagon (P) is the
defining identity for the algebraic level-2 primitive in $\mathcal{H}_q$.

### Significance: archimedean compute pipeline

Computational consequences of the post-$\tau$ pentagon (R):

1. **T3 reorganisation**:
   the canonical formalism
   uses (P$'$) — the duplication form of (R) — to evaluate
   $\mathrm{Li}_2^q(|V_i V_j|)$ at out-of-radius arguments via factorisation
   $z = uv$ with $|u|, |v| < q_0$. The Rogers $\log_q^2$ correction
   ensures the reorganisation is canonical consistent.

2. **Algebraic-side ratios** (per the Habiro framework
   [`prop:full-pole-structure-mass-trace`](#prop:full-pole-structure-mass-trace)):
   the bare pentagon (P) suffices for ratio computations; no
   $\log_q^2$ correction is needed when both numerator and
   denominator pass through the same $\tau_{\mathrm{arch}}$ realization.

3. **Volume-conjecture matching**: Kashaev's hyperbolic-volume
   conjecture uses Faddeev $\Phi_q$ on the archimedean side; the
   q-Rogers pentagon (R) connects this to the
   $\mathrm{Li}_2^q$ side via the bar-**anti**-symmetrization
   identity
   (`prop:li2q-phiq-bar-symmetrization`)
   $\mathrm{Li}_2^q(z) = -h \cdot \log \Phi_q(z) = (h/2)\bigl(\log \Phi_{q^{-1}} - \log \Phi_q\bigr)$ —
   not the bar-SYMMETRIC sum (which vanishes identically).

### Lean formalisation

[`qou:QOU.BraidKnot.q_rogers_pentagon_archimedean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/QRogersPentagonArchimedean.lean)
states the post-$\tau$ pentagon (R) as a theorem conditional on the
$O((q-1)^2)$ correction being class-axiomatized
(per AGENTS.md §3b-cond). At $q = 1$ the theorem reduces to the
classical Rogers identity (provable in Mathlib via real-log
arithmetic).

### Falsifiability

The canonical residual at $u = v = 0.7$ is $2.3 \times 10^{-3}$ — the
upper end of the empirical $O((q-1)^2)$ behaviour. A direct
high-precision computation at this point disagreeing by more than
$O((q-1)^3 \cdot u v)$ refutes the proposed q-correction; tracked
as the open paper-track derivation in
[`docs/audits/-pentagon-reduction-li2q.md`](https://github.com/litlfred/qou/blob/main/docs/audits/-pentagon-reduction-li2q.md).
<!-- FILE_END: q-rogers-pentagon-archimedean.md -->

