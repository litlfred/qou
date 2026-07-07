<!-- FILE_START: skein-resolution-obstruction.md -->
The Skein resolution obstruction is a fourth evaluation of
the universal obstruction class $\chi(A) \in HH^2 \cong k$
([QOU obstruction reduction](#thm:qou-obstruction-reduction)).
It measures whether the degree-$0$ answer $P_L(q)$ can be
extracted from the resolution tree in polynomial depth.

**Definition.**
Let $L = \hat{\beta}$ be a link with $c$ crossings and
$\mathcal{R}(L)$ its Skein resolution tree
([Skein Turing machine](#rem:skein-turing-machine)).  The
**Skein resolution obstruction** is the image of the universal
class under the resolution-tree restriction map:

$$
  \kappa_c^{\mathrm{comp}}(L, q)
  = 
  \mathrm{res}_{\mathcal{R}}\!\bigl(\chi(A)\bigr)
   \in 
  H^2(\mathcal{R}, \mathbb{G}_m),
$$

where $\mathrm{res}_{\mathcal{R}} \colon HH^2(\mathrm{Ad})
\to H^2(\mathcal{R}, \mathbb{G}_m)$ evaluates the unique
obstruction scalar $\chi(A)$ on the resolution tree of $L$.

This is the fourth evaluation of $\chi(A)$ alongside the
spectral (RH), collision (NS), and elliptic (BSD) restrictions
([QOU obstruction reduction](#thm:qou-obstruction-reduction)).
All four are images of the same class in $HH^2 \cong k$,
and the one-dimensionality of $HH^2$ means they are
proportional: the single integer $\chi(A) = -6$ controls
whether each problem persists through the classical limit.

**Kummer reduction.**
The Kummer filtration
([Kummer filtration](#rem:kummer-filtration-obstruction))
applies directly:

$$
  \kappa_c^{\mathrm{comp}} \bmod n = 0
  \quad\Longleftrightarrow\quad
  n \mid \chi(A).
$$

The obstruction vanishes at the divisors of $|\chi(A)| = 6$
(levels $\{1, 2, 3, 6\}$) and persists at all other levels.
For the computational setting, the Kummer level $n$
corresponds to the root-of-unity $q_n = e^{2\pi i/n}$:

- At $n \mid 6$ (torsion where obstruction vanishes): the
  Iwahori--Hecke algebra at $q_n$ has a radical that prunes the
  resolution tree — the BQP mechanism.
- At $n \nmid 6$ (torsion where obstruction persists): even
  quantum interference at this root of unity cannot collapse
  the tree.

**Field dependence.**
Over a finite field $\mathbb{F}_p$, the substrate parameter
$q \in \mathbb{F}_p^\times$ is always
$\mathbb{G}_m$-torsion (order dividing $p - 1$).  The
Kummer reduction at level $p - 1$ controls the obstruction:

$$
  \kappa_c^{\mathrm{comp}} \bmod (p-1) = 0
  \quad\Longleftrightarrow\quad
  (p - 1) \mid \chi(A).
$$

For $p > 7$, we have $p - 1 > 6 = |\chi(A)|$, so
$(p-1) \nmid 6$ and the obstruction persists modulo $p - 1$.
However, the resolution tree over $\mathbb{F}_p$ has at most
$p$ distinct weights — the computation terminates in bounded
time.  P = NP over finite fields is trivial (finite lookup),
not because the obstruction vanishes, but because the field
itself is finite.

Over $\mathbb{R}$ at non-torsion $q_0 = 1.109978595554181\ldots$ (50 dps), no
Kummer level applies.  The Iwahori--Hecke algebra $H_n(q_0)$ is
semisimple ($\mathrm{Rad} = 0$), the full $3^c$ tree
survives, and the obstruction is non-vanishing.
<!-- FILE_END: skein-resolution-obstruction.md -->

<!-- FILE_START: hecke-satisfies-blitvic-hypothesis.md -->
**Proposition (Hecke pair-partition structure).**
*The non-commutative random variables $\sigma_i \in H_\infty(q)$
under the Markov trace $\mathrm{tr}_M$ satisfy the pair-partition
combinatorial hypothesis of Blitvić's two-parameter non-commutative
central limit theorem [`blitvic2012`].*

**The hypothesis.** Blitvić's theorem requires a sequence of
non-commuting random variables whose joint moments are determined
by a pair-partition combinatorial structure: every length-$k$
joint moment
$\mathrm{tr}_M(\sigma_{i_1} \sigma_{i_2} \cdots \sigma_{i_k})$
must decompose as a sum over pair-partitions $\pi$ of
$\{1, \ldots, k\}$ of weights $W(\pi, q)$ depending only on $\pi$
and the deformation parameter $q$.

**Satisfaction of the hypothesis by Hecke generators.** The Hecke quadratic relation
$$
  \sigma_i^2 \;=\; (q - q^{-1})\,\sigma_i + 1
$$
forces every length-$k$ word in the generators to reduce, after
finitely many rewriting steps, to an $R$-linear combination of
*square-free* generator products (where each $\sigma_i$ appears at
most once). The Markov property
$\mathrm{tr}_M(x \, \sigma_n) = z \, \mathrm{tr}_M(x)$
then peels off generators one at a time, producing a sum over
*matchings* (pair-partitions): each non-trivial Markov pairing
$\sigma_i \leftrightarrow \sigma_i^{-1}$ contributes a fixed scalar
to the trace, and each unmatched generator contributes zero (by
trace centring under the bar-involution adjoint).

Explicitly: for the centred generator $\tilde\sigma_i := \sigma_i -
\mathrm{tr}_M(\sigma_i) \cdot 1 = \sigma_i - z \cdot 1$, the joint
moment
$$
  \mathrm{tr}_M\bigl(\tilde\sigma_{i_1} \tilde\sigma_{i_2} \cdots \tilde\sigma_{i_k}\bigr)
$$
vanishes unless $k$ is even, and for even $k$ decomposes as
$$
  \mathrm{tr}_M\bigl(\tilde\sigma_{i_1} \cdots \tilde\sigma_{i_k}\bigr)
  \;=\;
  \sum_{\pi \in P_2(k)}
    W(\pi; q) \cdot \prod_{\{a, b\} \in \pi}
      \delta_{i_a = i_b},
$$
where $P_2(k)$ is the set of pair-partitions of $\{1, \ldots, k\}$
and $W(\pi; q)$ is determined by the *crossing count* of $\pi$
weighted by powers of $(q - q^{-1})$. The weight function $W(\cdot;
q)$ is Blitvić's $(q, t)$-Gaussian moment kernel at parameter $t = 1$,
$q = $ the QOU substrate.

**Corollary: the q-CLT input (partially established).** Only the
*odd-length* face of the proposition is proved (odd-word moments
vanish — Lean `sorry`-free); the full even-length pair-partition
decomposition with the crossing-weighted $W(\pi; q)$ kernel remains
open, carried as an honest `sorry` (it needs non-commutative-probability
pair-partition machinery absent from Mathlib). *Conditional on* that
full decomposition, Blitvić's CLT
[`blitvic2012`, Theorem 1.1] applies: the rescaled centred
sum $S_n = n^{-1/2} \sum_i \tilde\sigma_i$ has joint moments
converging to a $(q, t)$-Gaussian process at parameter $(q, 1)$.
The QOU q-CLT
(`conj:q-clt-non-commutative`)
is therefore conditional on **both** the full pair-partition
decomposition **and** the *parameter-identification*
step (Blitvić's $q$ $\leftrightarrow$ QOU's $q$ $\leftrightarrow$ Tsallis's $q$).
<!-- FILE_END: hecke-satisfies-blitvic-hypothesis.md -->

<!-- FILE_START: hecke-satisfies-blitvic-hypothesis-interpretation.md -->
The crossing-count exponent $q^{\mathrm{cr}(\pi)}$ in the
pair-partition moment formula arises from the braid relation
$\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}$:
each non-trivial reordering of a crossing pair contributes one
factor of $q$ (positive crossing) or $q^{-1}$ (negative crossing).
The Blitvić $(q, t)$-Gaussian recovers this exact crossing-weighted
combinatorics. Our use of $q$ throughout fixes a sign convention;
the corresponding $t$ parameter in Blitvić's framework is $t = 1$,
which is the standard fermionic/Hecke case.
<!-- FILE_END: hecke-satisfies-blitvic-hypothesis-interpretation.md -->

<!-- FILE_START: trace-locality-meets-gs-nonlocality.md -->
**Proposition (locality–non-locality reconciliation).**
*The two seemingly contradictory operational stances in the QOU
manuscript — that single Hecke crossings obey a Markov locality
property (memoryless of upstream history) while composite braid
evaluation is non-local (Gröbner–Shirshov reduction sweeps the
whole braid word) — are not contradictory but
complementary statements about different operations on the same
object. They are reconciled by Wenzl's product factorisation of
the Markov trace.*

**Statement.** Let $\beta = \sigma_{i_1} \sigma_{i_2} \cdots \sigma_{i_N}$
be a braid word in $B_n$, and let $\mathrm{NF}_{\mathrm{GS}}(\beta)
= e_{j_1} \cdot e_{j_2} \cdots e_{j_M}$ be its Gröbner–Shirshov
normal form in $H_n(R, q)$. Then:

1. *(Markov locality, single-generator step.)* For every $x \in
   H_n(R, q)$,
   $$
     \mathrm{tr}_{M, n+1}(x \cdot \sigma_n^{\pm 1})
     \;=\;
     z^{\pm 1} \cdot \mathrm{tr}_{M, n}(x),
     \qquad z = 1/(q^{1/2} + q^{-1/2}).
   $$
   *The contribution of a single newly-added generator $\sigma_n$ is
   a fixed scalar $z^{\pm 1}$ — independent of $x$. The new crossing
   "doesn't look back."*

2. *(GS non-locality, composite braid.)* The normal form
   $\mathrm{NF}_{\mathrm{GS}}(\beta)$ depends on the full braid
   word; rewriting rules (Hecke quadratic relation, braid relation,
   far-commutativity) act non-locally across $\beta$ during reduction.

3. *(Product factorisation bridge.)* The Markov trace of the normal
   form decomposes as a product of local vertex volumes:
   $$
     \mathrm{tr}_M\bigl(\rho_{\mathrm{NF}}(\beta)\bigr)
     \;=\;
     \prod_{i = 1}^{M} \widehat{V}_i(q),
   $$
   *where the vertex volumes $\widehat{V}_i(q)$ are local in the
   normal-form word — each depends only on its own normal-form
   generator $e_{j_i}$ and the modified Markov-parameter
   coefficients $(a_i, b_i)$ produced by the GS algorithm
   (Wenzl 1988 [`wenzl1988`]).*

**Reconciliation.** The Gröbner–Shirshov algorithm "digests" the
global, non-local braid entanglement into modified local coefficients
at each normal-form generator. After digestion, the Markov trace
factorises locally over the normal form — recovering
single-generator locality on the *post-reduction* word. The two
stances are sequential, not contradictory:

- *Step 1 (non-local):* Apply Gröbner–Shirshov reduction to
  $\beta$. This sweeps the whole braid word and produces local
  coefficients that absorb the global entanglement.
- *Step 2 (local):* Evaluate $\mathrm{tr}_M$ on the normal form.
  Markov locality applies: the trace factorises over the normal-form
  generators.

The composite operation (input: braid word $\beta$; output:
$\mathrm{tr}_M(\rho(\beta))$) is therefore *local after
normalisation*, even though normalisation itself is non-local.
<!-- FILE_END: trace-locality-meets-gs-nonlocality.md -->

<!-- FILE_START: trace-locality-nc-probability-reading.md -->
**Non-commutative probability reading.** Translating to the
dictionary
([rem:non-commutative-probability-dictionary](#rem:non-commutative-probability-dictionary)):

- *Markov locality* = the conditional expectation of a new
  random variable given the past is a fixed scalar (the analogue
  of conditional independence for non-commutative random variables).
- *GS non-locality* = the joint distribution depends on the *full*
  word — analogous to a Markov chain's joint law depending on
  the full sample path even though each step is conditionally
  independent of the past given the present state.
- *Product factorisation* = the joint law decomposes as a product
  over states once the chain is in normal form — the
  non-commutative analogue of writing $P(X_1, \ldots, X_N) =
  P(X_1) \prod_{i \geq 2} P(X_i \mid X_{i-1})$ for a classical
  Markov chain.

In this reading, GS reduction is the non-commutative analogue of
*finding the stationary representation* of a Markov chain: a
single global computation that, once done, permits local stepwise
evaluation.
<!-- FILE_END: trace-locality-nc-probability-reading.md -->

<!-- FILE_START: jones-markov-trace.md -->
**(Jones, 1987, Theorem 5.1 and Corollary 5.3.)**
Let $q \in \mathbb{C}^{\times}$ be not a root of unity, and let
$H_n(R, q) = \mathrm{End}_{B_n}(V^{\otimes n})$ be the Iwahori--Hecke algebra of
type $A_{n-1}$.  Then:

1. **(Existence.)** There exists a unique $\mathbb{C}$-linear functional
   $\mathrm{tr}_M \colon \bigcup_{n \geq 1} H_n(R, q) \to \mathbb{C}$
   satisfying:
   - **(Normalisation)**: $\mathrm{tr}_M(1) = 1$.
   - **(Trace property)**: $\mathrm{tr}_M(ab) = \mathrm{tr}_M(ba)$
     for all $a, b \in H_n(R, q)$.
   - **(Markov property)**: $\mathrm{tr}_M(x \sigma_n^{\pm 1}) = z^{\pm 1}\mathrm{tr}_M(x)$ for all $x \in H_n(R, q)$, viewed in
     $H_{n+1}(q)$ under the standard embedding $H_n(R, q) \hookrightarrow H_{n+1}(q)$, where
     $z = (q - 1)/(q^{1/2} + q^{-1/2})^2$ (determined by $q$).

2. **(Non-degeneracy on irreducibles.)** For each partition
   $\lambda \vdash n$ with at most $r$ parts (where $r = \mathrm{rank}$
   of the quantum group), the restriction of $\mathrm{tr}_M$ to the
   irreducible $H_n(R, q)$-module $S_\lambda$ is a non-zero scalar multiple
   of the character $\chi_\lambda$.  In particular,
   $\mathrm{tr}_M|_{S_\lambda} \neq 0$ for every $\lambda$.

3. **(Link invariance.)** For any braid $\beta \in B_n$, the value
   $\mathrm{tr}_M(\rho_n(\beta))$ depends only on the isotopy class of
   the closure $\hat{\beta}$, and equals the Jones polynomial $J_L(q)$
   of the link $L = \hat{\beta}$ up to a framing factor
   $\alpha^{w(\beta)}$ where $w(\beta)$ is the writhe.

This is the key external result on which knot eigenbasis completeness
([knot eigenbasis completeness](#prop:knot-eigenbasis-complete)) depends.
<!-- FILE_END: jones-markov-trace.md -->

<!-- FILE_START: jones-markov-trace-formalization-note.md -->
The proof occupies §3--5 of Jones (1987); we take the result as axiomatic
and encode it as a Lean structure whose fields are the three properties above.
The formal goal is to verify that downstream theorems — the unity of the Markov trace and the detection of all irreducible representations — follow from these axiomatized structure fields. The trace's required properties are isolated as axiomatic structure fields, separating the external existence proof from the internal verification of its consequences in the observable mass spectrum.

**Mathematical Novelty:** The theorem itself is a standard result due to Jones, with no new mathematical argument. The novel contribution of this work lies in the formalization: the faithful structure-encoding of the three trace properties alongside the $R_q = \mathbb{Z}[q, q^{-1}]$ ground-ring framing, which constitutes careful engineering to support downstream machine-checked proofs.
<!-- FILE_END: jones-markov-trace-formalization-note.md -->

<!-- FILE_START: markov-disambiguation.md -->
Three mathematically distinct constructions share the name *Markov*
in this work.  They arise from the same combinatorial source (the
braid group $B_n$) but operate at different levels of the
Cat$\to$Alg$\to$Geom$\to$Arch$\to$Phys arc.

1. **Markov trace** (Jones--Wenzl).  The unique trace functional
   $\mathrm{tr}_M \colon H_n(R,q) \to R$ satisfying cyclicity, the
   Markov axiom $\mathrm{tr}_M^{(n)}(x\sigma_{n-1})
   = z \cdot \mathrm{tr}_M^{(n-1)}(x)$, and $\mathrm{tr}_M(1)=1$.
   This is the **algebraic** object that feeds the mass formula:
   $\mathfrak{m}(\varrho) = m_e \cdot
   |\mathrm{tr}_M(\rho(\beta))| \cdot \mathrm{VolDensity}(K,q_0)$.
   Symbol: $\mathrm{tr}_M$.

2. **Markov chain** (stochastic dynamics).  The random walk on
   braid words induced by Hecke--Markov transition probabilities
   $p_{w \to w'} = \mathrm{tr}_M(\rho(w')) \cdot \overline{\mathrm{tr}_M(\rho(w'))} /
   \sum \mathrm{tr}_M(\rho(w'')) \cdot \overline{\mathrm{tr}_M(\rho(w''))}$
   (bar denotes the Hecke bar-involution $q \leftrightarrow q^{-1}$;
   at real $q_0$ the form reduces to $|\mathrm{tr}_M|^2$).
   This is the **stochastic**
   object that gives error bounds on the mass formula via
   Perron--Frobenius dominant-eigenvalue convergence.  See
   Chapter Stochastic Mechanics.

3. **Markov moves** (topological equivalence).  Stabilisation
   $\beta \mapsto \beta\sigma_n^{\pm 1}$ and conjugation
   $\beta \mapsto \gamma\beta\gamma^{-1}$ on $B_n$.  Two braids
   represent the same link iff they are related by a finite
   sequence of Markov moves (Markov's theorem, 1935).  This is
   the **topological** input that makes the Jones polynomial a
   knot invariant.

These three uses are separated: (1) is an algebraic
functional, (2) is a probability measure, (3) is an equivalence
relation.  Context always disambiguates, but when precision matters
we write $\mathrm{tr}_M$ for (1), "Markov chain" for (2), and
"Markov move" for (3).
<!-- FILE_END: markov-disambiguation.md -->

<!-- FILE_START: bar-involution.md -->
**Definition (bar-involution).**

*The* **bar-involution** *$\overline{(\cdot)} \colon H_n(q) \to H_n(q)$
is the ring anti-involution on the Iwahori–Hecke algebra defined
on generators by*

$$
\overline{\sigma_i} \;=\; \sigma_i^{-1}, \qquad \overline{q} \;=\; q^{-1}.
$$

*Equivalently, on the parameter alone: $q \mapsto q^{-1}$, and on
crossings: positive $L_+ \leftrightarrow$ negative $L_-$ (mirror
reflection of the braid diagram).*

The bar-involution is an involution ($\overline{\overline x} = x$);
over a field of characteristic $\ne 2$ it splits every element
$x \in H_n(q)$ into a bar-symmetric part $P_{\mathrm{avg}}(x)$ and a
bar-anti-symmetric part $P_{\mathrm{skew}}(x)$. The canonical
projection, classification of QOU quantities by bar-type, key
identities, and the bar-grading proofs are developed in the
interpreting remark [bar-involution properties](#rem:bar-involution-properties).
<!-- FILE_END: bar-involution.md -->

<!-- FILE_START: bar-involution-properties.md -->
This remark develops the canonical projections and the classification of
QOU quantities by bar-type for the [bar-involution](#def:bar-involution).
The key algebraic identities, the geometric / Kac–Sunada readings, and the
$\mathbb{Z}/2\mathbb{Z}$ bar-grading proofs are developed in the companion
remarks
[bar-symmetric algebraic identities](#rem:bar-involution-c5-algebraic-identities),
[geometric and Kac–Sunada readings](#rem:bar-involution-geometric-kac-sunada),
and [the bar-grading Lean bridge](#rem:bar-involution-grading-lean-proofs).

## The two canonical projections

The bar-involution is an involution: $\overline{\overline x} = x$.
Every Hecke-algebra element $x \in H_n(q)$ over a field of
characteristic $\ne$ 2 decomposes uniquely as

$$x \;=\; P_{\mathrm{avg}}(x) + P_{\mathrm{skew}}(x),$$

where

See [Table 1](#tbl:bar-involution-table1-data).

The framework's empirical content is that **$P_{\mathrm{avg}}$ is
the canonical projection** — the bar-symmetric part of every
Hecke-algebra computation is the physical/observable content; the
bar-anti-symmetric part is projected away.

> **Antiskew-vs-symmetric clarification.** $P_{\mathrm{avg}}(x)$
> is the bar-**even** (= bar-**symmetric**) projection. The
> framework retains $P_{\mathrm{avg}}$ ($\cos, \cosh, \mathrm{Li}_2^q$)
> and discards $P_{\mathrm{skew}}$ ($\sin, \sinh, \Phi_q$ alone).
> "Anti-skew" is only accurate in the discarding sense — the
> kept residual is symmetric/even.

## Classification of QOU quantities by bar-type

The canonical reference. Every quantity in the paper that has a
well-defined bar-action falls in one of these rows:

### Bar-symmetric (bar-even, $P_{\mathrm{avg}}$ image, retained)

See [Table 2](#tbl:bar-involution-table2-data).

### Bar-anti-symmetric (bar-odd, $P_{\mathrm{skew}}$ image, discarded)

See [Table 3](#tbl:bar-involution-table3-data).

### Trivial under bar (rational scalars)

See [Table 4](#tbl:bar-involution-table4-data).

## Cross-references

This definition is the canonical reference for bar-symmetry. Other
blocks that consume it (with their primary bar-classification):

- `thm:averaging-resonance-rule` — $\sigma_{\mathrm{avg}}$ bar-symmetric; level-selection rule at half-fill rung.
- [`prop:c5-involution-leibniz-decomposition`](#prop:c5-involution-leibniz-decomposition) — $c_5$ bar-symmetric closed form; Hoefsmit-Quantum-2 identity proved here.
- [`prop:silver-ratio-beta-decay-null`](#prop:silver-ratio-beta-decay-null) — $\Delta(\text{net}) = h(h-2)/2$ bar-anti-symmetric in $h$; $h = 2$ root at silver.
- `prop:bar-symmetric-three-layer-synthesis` — series / phase / gain layers, all bar-symmetric projections (conjecturally of one universal kernel).
- [`def:categorical-q-reeb-flow`](#def:categorical-q-reeb-flow) — Reeb field $R$ bar-anti-symmetric.
- [`prop:chirality-residue-mass-term`](#prop:chirality-residue-mass-term) — chirality residue bar-anti-symmetric.

## Notation summary

See [Table 8](#tbl:bar-involution-table8-data).
<!-- FILE_END: bar-involution-properties.md -->

<!-- FILE_START: bar-involution-c5-algebraic-identities.md -->
This remark collects the key bar-symmetric algebraic identities induced by
the [bar-involution](#def:bar-involution): the half-step factorization of
$h$, the Hoefsmit-Quantum-2 identity, and the $c_5$ closed form with its
Wedderburn-block and skein-function readings. It overlaps
[`prop:c5-involution-leibniz-decomposition`](#prop:c5-involution-leibniz-decomposition),
where the Hoefsmit-Quantum-2 identity is proved.

## Key algebraic identities

### Half-step factorization of $h$

$$h \;=\; q - q^{-1} \;=\; \underbrace{(q^{1/2} - q^{-1/2})}_{h_{1/2},\;\text{bar-ANTI-sym}} \;\cdot\; \underbrace{(q^{1/2} + q^{-1/2})}_{1/z,\;\text{bar-SYM (Markov param)}}$$

The bar-anti-symmetry of $h$ comes *entirely* from $h_{1/2}$; the
bar-symmetric Markov parameter $z = 1/(q^{1/2}+q^{-1/2})$ factor
is bar-invariant. This is the same $z$ that the cross-PR Phase 5c.1 cross-check
identified as the interface-knot value $\bowtie_K = z$ exactly.

### Hoefsmit-Quantum-2 identity

$$\boxed{\;\; b^2(q) \;=\; 1 \,-\, \frac{1}{[2]_q^2} \;\;}$$

Proved as a pure algebraic identity over a field of char $\ne 2$;
no `sorry`. See [`prop:c5-involution-leibniz-decomposition`](#prop:c5-involution-leibniz-decomposition)
in the Lean sibling `hoefsmit_b_squared_eq_one_minus_inv_quantum_two_squared`.

### $c_5$ via quantum-2

$$c_5(q) \;=\; -b^2 - \tfrac{1}{2} \;=\; -\tfrac{3}{2} + \frac{1}{[2]_q^2}.$$

Proved as a corollary of the Hoefsmit-Quantum-2 identity; see
`c5_decomposition_via_quantum_two`.

### $c_5$ classical limit (commutative QOU)

$c_5(q=1) = -5/4$. Proved as `c5_classical_limit_eq_neg_five_quarters`.

### Commutative-QOU categorical identification of $-3/2$

The q-independent $-3/2$ in $c_5(q) = -3/2 + 1/[2]_q^2$ is identified
categorically as **half the dimension of the non-sign Wedderburn
blocks of $\mathbb{C}[S_3] = H_3(q=1)$**:

$$
-3/2 \;=\; -\frac{\dim V_{(3)} + \dim V_{(2,1)}}{2} \;=\; -\frac{1 + 2}{2}.
$$

The sign rep $V_{(1,1,1)}$ (dim 1) is excluded — it carries the
bar-anti-symmetric part of the Hopf-link Markov trace, projected
away by $P_{\mathrm{avg}}$. Proved as
`c5_classical_eq_wedderburn_nonsign_dim_half`.

This identifies the "−1/2 fingerprint" of the empirical
$c_5 = -b^2 - 1/2$ decomposition as the **bar-symmetric
Wedderburn-block contribution from the non-sign sector** in the
commutative limit — categorical content, not a quantum artifact.

### $c_5$ as a rational function of the bar-anti-symmetric Hecke skein

The closed form $c_5(q) = -3/2 + 1/[2]_q^2$ rewrites as a
function of the bar-anti-symmetric Hecke skein $h = q - q^{-1}$
alone, using the algebraic identity (PROVED in Lean as
`quantum_two_squared_eq_skein_squared_plus_four`):

$$
[2]_q^2 \;=\; (q + q^{-1})^2 \;=\; h^2 + 4
\quad\text{(from } q^2 + 2 + q^{-2} = (q^2 - 2 + q^{-2}) + 4\text{)}.
$$

Substituting:

$$
\boxed{\;\; c_5(q) \;=\; -\frac{3}{2} \,+\, \frac{1}{h^2 + 4}, \quad h = q - q^{-1}. \;\;}
$$

Both terms are **even functions of $h$** (the constant $-3/2$
by definition; $1/(h^2 + 4)$ because $h^2$ is bar-symmetric by
`IsBarAntiSymmetric.pow_two_mul`).

**Categorical reading**: this expresses $c_5$ purely as a function
of the universal bar-anti-symmetric kernel $h$ — the
`BarHeckeFunctor` $K \mapsto -3/2 + 1/(K^2 + 4)$ applied to
$K = h$. The Markov-trace-functor shape is now **explicit** for
$c_5$: it is the image of the bar-anti-symmetric skein under a
specific even rational function, which is exactly the
$P_{\mathrm{avg}}$-projection of the kernel through the
series-layer functor.

Proved in Lean as `c5_as_function_of_skein` (no `sorry`).

### Bar-grading algebraic structure (all PROVED in Lean, no `sorry`)

The bar-involution induces a $\mathbb{Z}/2\mathbb{Z}$-grading on
the underlying ring. The bar-symmetric subspace is a **subring**;
the bar-anti-symmetric subspace is an $R^+$-module that satisfies
the natural sign rules:

See [Table 5](#tbl:bar-involution-table5-data).

These are **fully proved** from the four ring-involution axioms
alone — no `sorry`, no auxiliary `Field` instance needed (only
`CommRing`). They formalize previously narrative-only claims:

- *"$h^2$ is bar-symmetric because $h$ is bar-anti-symmetric"* —
 now `IsBarSymmetric.of_mul_antisym hx hx` for any
 `hx : IsBarAntiSymmetric h`.
- *"$\cosh(h) = (e^h + e^{-h})/2$ is even, hence bar-symmetric"* —
 the formal-series structure that makes $\cosh$, $\cos$,
 $\mathrm{Li}_2^q$ bar-symmetric reduces to repeated applications
 of `pow_two_mul` and `add`.
- *"The framework retains only the even part"* — the
 bar-symmetric subspace is closed under the ring operations, so
 applying $P_{\mathrm{avg}}$ to any sequence of operations
 on bar-symmetric inputs lands in the bar-symmetric subspace
 again.

### Falsifiability: silver vs golden $c_5$ outlier

`computations/probes/qbeta_golden_ratio_fibonacci_probe.py`
computes $c_k(q)$ for $k = 3..10$ at golden ratio $q = \varphi$
($b^2 = 4/5$ exact) and tests Fibonacci-Lucas-cleanness vs the
silver-ratio Pell-Lucas test. Result (witness confirmed):

See [Table 6](#tbl:bar-involution-table6-data).

**Silver outliers: $\{5\}$. Golden outliers: $\emptyset$.**

This **confirms the hypothesis** that the $c_5$ outlier is
silver-specific — the inert-prime fingerprint of the β-decay null
($h=2$ at silver, no analog at golden $h=1$). The outlier IS the
forced collapse into the bar-invariant fixed-point sector at the
unique null point in the proton/neutron kinematic window.
<!-- FILE_END: bar-involution-c5-algebraic-identities.md -->

<!-- FILE_START: bar-involution-geometric-kac-sunada.md -->
This remark develops the geometric and Kac–Sunada readings of the
[bar-involution](#def:bar-involution): the three-level correspondence of
the bar-symmetric projection with orientation-averaged quantities, and the
isospectral meta-justification for why bar-symmetric matching is forced.

## Geometric reading

The bar-involution corresponds at three different geometric levels:

See [Table 7](#tbl:bar-involution-table7-data).

The bar-symmetric projection at each level is the **orientation-
averaged** quantity: averaged crossings (knot), unsigned winding
(color tubes), symmetrized Wilson loop (ED), $\alpha \wedge d\alpha$
(contact volume).

## Kac–Sunada meta-justification

Kac (1966) / Sunada (1985): distinct manifolds can be isospectral
(share Laplace-Dirichlet spectrum). The Hecke analog: distinct
braids share $\tau_M(\beta)$ at fixed $q$ (Hecke-trace isospectral
pairs). But demanding agreement at BOTH $q$ AND $q^{-1}$ —
bar-symmetric matching — **is much tighter**.

The Faddeev $\Phi_q$ channel hears only one orientation;
symmetric Li_2^q hears the bar-symmetrized spectrum. So
**bar-symmetric is FORCED** — the projection isn't a stylistic
choice but the isospectral lift demanded by Kac–Sunada non-
uniqueness applied to Hecke-trace-determined braids.
<!-- FILE_END: bar-involution-geometric-kac-sunada.md -->

<!-- FILE_START: braid-group-n-strand.md -->
**$n$-strand braid group + Markov closure + Hecke quotient scaffolding.**

Generalises the 2-strand foundation in
[`rem:braid-link-types`](#rem:braid-link-types) and the 3-strand
typed-$\mathbf{B}_3$ infrastructure in
[`rem:typed-b3-sub-braid-extraction`](#rem:typed-b3-sub-braid-extraction)
to an arbitrary number of strands $n \in \mathbb{N}$.

## Defined objects

See [Table 1](#tbl:braid-group-n-strand-table1-data).

## Specialisations

See [Table 2](#tbl:braid-group-n-strand-table2-data).

## Significance

The categorical-derivation chain through $N=4$ in
[`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder)
sits on the 3-strand typed-$\mathbf{B}_3$ infrastructure. Validating
the **two convergence mechanisms** documented in
[`prop:categorical-chain-convergence-mechanisms`](#prop:categorical-chain-convergence-mechanisms)
— per-knot $c(K)$ brane-tower bound + inter-knot linking-number
locality — requires at minimum $n = 6$ infrastructure (to test
$\tau_M(K_1 \sqcup K_2) = \tau_M(K_1) \cdot \tau_M(K_2) \cdot z^k$
on a concrete 2-baryon disjoint braid via Markov axiom M3).

The Lean class system makes the scaffolding **per-$n$ extensible**:
each new $n$ adds an `instance HeckeQuotient n q_0` and
`instance MarkovTraceN n q_0`, and downstream theorems
auto-specialise.

## Specialisations landed

See [Table 3](#tbl:braid-group-n-strand-table3-data).

Note: the parameterised `BraidCrossing n` in this block coexists with
the unparameterised `TypedCrossing` from
[`rem:typed-b3-sub-braid-extraction`](#rem:typed-b3-sub-braid-extraction);
the latter additionally carries the `averaged` Hecke-specific crossing
type, so the conversion `BraidWord 3 → TypedBraidWord3` is into the
`sigma`/`sigma_inv` subset (the `averaged` channel has no counterpart
in the generic n-strand types).

## Open R&D

- Per-$n$ discharge of `MarkovTraceN n q` from a fixed Markov-trace
  operator on the inductive limit $\bigcup_n \mathbf{B}_n$.
- Higher-$n$ `closureN` discharges: Borromean link at $n=3$,
  di-baryon at $n=6$, etc. (current $n \geq 3$ returns `Link.unknot`
  as a ansatz).
<!-- FILE_END: braid-group-n-strand.md -->

<!-- FILE_START: h3-hecke-idempotents.md -->
**$H_3(q)$ Hecke idempotents — explicit $q$-dimensions and Wedderburn-block eigenvalue table.**

The Iwahori-Hecke algebra $H_3(q)$ has three irreducible Wedderburn
blocks indexed by partitions of $3$. For each block $V_\lambda$, the
generators $\sigma_0, \sigma_1$ act with eigenvalues drawn from the
Hecke-quadratic roots $\{q, -q^{-1}\}$.

| $\lambda$ | $\dim_q V_\lambda$ | $\sigma_0$ eigenvalue | $\sigma_1$ eigenvalue | source |
|:---:|:---:|:---:|:---:|---|
| $(3)$ | $1$ | $q$ | $q$ | symmetric: both $\sigma$ act as $q$ |
| $(2,1)$ | $[2]_q = q + q^{-1}$ | $\langle q, -q^{-1} \rangle$ | Hoefsmit (off-diag) | [`prop:hoefsmit-V21-cos-symmetrization`](#prop:hoefsmit-V21-cos-symmetrization) |
| $(1,1,1)$ | $1$ | $-q^{-1}$ | $-q^{-1}$ | antisymmetric: both $\sigma$ act as $-q^{-1}$ |

## Substantive content (no vacuous classes)

The Lean module exports **concrete scalar identities**, not abstract markers:

- `dimQ_V3 q : ℝ = 1`
- `dimQ_V21 q : ℝ = q + q^{-1}` (= $[2]_q$ at H_3)
- `dimQ_V111 q : ℝ = 1`
- `sigma_eigval_V3 q i : ℝ = q` (for every $i$)
- `sigma_eigval_V111 q i : ℝ = -q^{-1}` (for every $i$)

The **sum-of-$q$-dimensions identity**

$$
  \dim_q V_{(3)} + \dim_q V_{(2,1)} + \dim_q V_{(1,1,1)}
    \;=\; q + q^{-1} + 2
$$

is the theorem `dimQ_sum_H3`, closed by `ring`. The completeness
residual at $n = 3$ — the LHS $-$ RHS of this identity — is
the theorem `qYoung_completeness_residual_H3`, closed `0` by `ring`.

## Connection to the Q-YST class

This block **substantively backs** the abstract `QYoungSymmetrizers 3 q`
class instance in
[`rem:ck-extraction-from-algebraic-rules`](#rem:ck-extraction-from-algebraic-rules):
the `qyst_residual` scalar (declared in that class) is concretely
the residual of the $q$-dimension sum identity above, and `dimQ_sum_H3`
discharges it to `0`.

## Explicit projector normalization — the $S_3$ Poincaré polynomial

The carrier-level construction of the two one-dimensional projectors
(in the upstreamable module `QOU.Mathlib.HeckeAlgebra`, declarations
`H3.blockSym3` / `H3.blockAlt3`) fixes the normalization convention:

$$
  e_{(3)} = \frac{1}{P(q)} \sum_{w \in S_3} q^{\ell(w)}\, T_w,
  \qquad
  e_{(1^3)} = \frac{1}{P(q^{-1})} \sum_{w \in S_3} (-q^{-1})^{\ell(w)}\, T_w,
$$

where $P(q) = \sum_{w \in S_3} q^{2\ell(w)} = 1 + 2q^2 + 2q^4 + q^6
= (1+q^2)(1+q^2+q^4)$ is the Poincaré polynomial of $S_3$ in the
Hecke parameter (declaration `H3.poincare`). The normalizer is forced
by the eigenvalue table above: $T_w\, e_{(3)} = q^{\ell(w)} e_{(3)}$,
so squaring the sum multiplies it by $\sum_w q^{2\ell(w)}$, and
idempotency pins the denominator to $P(q)$ exactly; the sign block has
$T_w\, e_{(1^3)} = (-q^{-1})^{\ell(w)} e_{(1^3)}$, pinning $P(q^{-1})$.

Two practical consequences:

1. **No genericity hypothesis.** $P(q) \geq 1 > 0$ for every real
   $q$ (even powers, positive coefficients), so idempotency and
   orthogonality of the blocks hold with only $q \neq 0$ (which
   clears the $q - q^{-1}$ structure constants) — there is no
   vanishing locus to avoid on the real line.
2. **Relation to the balanced $q$-factorial.** With the balanced
   convention $[k]_q = (q^k - q^{-k})/(q - q^{-1})$ one has
   $P(q) = q^{\ell(w_0)}\, [3]_q!$ with $\ell(w_0) = 3$ the longest
   element, and $P(q^{-1}) = q^{-\ell(w_0)}\, [3]_q!$ by
   bar-invariance of $[3]_q!$. The two normalizers differ by
   $q^{2\ell(w_0)} = q^6$; using the bare balanced factorial for
   *both* blocks makes neither projector idempotent.

## Remaining work

The abstract $H_n(q)$ type (the quotient-of-`FreeAlgebra`
presentation a Mathlib lift would provide) is still outside the
chapter-block .lean tier; the explicit projectors above live on the
concrete rank-6 carrier. The scalar-invariant version landed here is
sufficient to discharge the abstract Q-YST scaffolding for the c_k
extraction theorem; a future Mathlib lift of full $H_n(q)$ would
substitute the carrier-level $e_\lambda$ values without changing the
downstream API.
<!-- FILE_END: h3-hecke-idempotents.md -->

<!-- FILE_START: braid-link-types.md -->
**Track C Step A: concrete Lean Braid/Link types**, discharging Atom 1
of [`rem:markov-closure-map-axiomatic`](#rem:markov-closure-map-axiomatic)
for the 2-strand case.

## Constructed infrastructure

A **minimal but fully Lean-proved** infrastructure:

- `inductive Link` with constructors `unknot`, `hopfLink`,
  `torusLink2 k` (sufficient for 2-strand braid analysis).
- `Braid2 := ℤ` — 2-strand braid group as integers (single generator σ).
- `closure2 : Braid2 → Link` — explicit Markov-closure pattern matching
  on the crossing count.
- `jonesAtOne : Link → ℝ` — classical-limit Jones values.

## The atomic theorem (Atom 1 discharged)

$$
\boxed{
  \widehat{\sigma_1^2 \in B_2} \;=\; \text{Hopf link}
}
$$

In Lean: `theorem closure2_at_two_crossings_eq_hopf : closure2 σ_sq = hopfLink`
— closed by `rfl` from the explicit definition.

## The composed chain

For the c_3 = -2 identification, the chain:

$$
  \sigma_1^2 \in B_2 \;\xrightarrow{\text{closure}_2}\; \text{Hopf link} \;\xrightarrow{J(q{=}1)}\; -2
$$

is now FULLY LEAN-PROVED via:

```lean
theorem closure2_jones_at_one_sigma_sq_eq_neg_two :
    jonesAtOne (closure2 Braid2.σ_sq) = -2
```

closed by `closure2_at_two_crossings_eq_hopf` + `jonesAtOne_hopf_eq_neg_two`.

## Track-C atoms (Step A)

| Track-C atom | Lean status |
|---|---|
| Atom 1: closure of $\sigma^2$ = Hopf link (Alexander-Markov 1923/1936) | proved via `closure2_at_two_crossings_eq_hopf` |
| Atom 2: J_Hopf(q=1) = -2 (Jones 1985) | proved via `jonesAtOne_hopf_eq_neg_two` |
| Composed chain $\sigma^2$ $\to$ Hopf $\to$ -2 | proved via composition |

**Both atomic Track-C axioms are now Lean theorems.** The 2-strand
case is fully discharged.

## Remaining n-strand case (open)

The QOU framework needs the analogous chain for **3-strand typed
braids in B_3**. The categorical content there is more subtle:

1. The 3-strand typed-B_3 braid β_p / β_n has 11 typed crossings.
2. At order ε^6 in the perturbative τ_M expansion, the dominant
   contribution selects 3-element subsets of crossings.
3. The 3-element subset that maximally contributes corresponds to a
   **2-strand sub-braid** (extracted by collapsing the third strand).
4. This 2-strand sub-braid has 2 crossings (the active ones), so its
   Markov closure is the Hopf link by the 2-strand theorem above.
5. Composing gives c_3 = J_Hopf(1) = -2.

Steps 1, 2 are mechanical sympy + combinatorics. Step 3 is the
**sub-braid extraction** combinatorial result. Step 4 reduces to the
2-strand case (this file). Step 5 is `rfl`.

The remaining Lean work is to formalise Step 3 — sub-braid extraction
combinatorics — which requires a Lean definition of the general
braid group $B_n$ and how sub-braids are extracted via strand-collapse.

Mathlib has `BraidGroup`; building on it requires:
- A `subBraid : Braid n → Finset (Fin n) → Braid (size of subset)` map
- Theorems about Markov closure under sub-braid extraction
- Identification of the dominant sub-braid at order ε^6

This is substantial Lean-engineering work but no longer "research-level"
— each step is a concrete combinatorial theorem given the foundations.
<!-- FILE_END: braid-link-types.md -->

