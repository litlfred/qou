<!-- FILE_START: markov-trace-factorization.md -->
The Markov trace of the nuclear braid word factors exactly as
a product of **Markov-traced generator volumes** — one per braid
generator $\sigma_i$.  This factorization is an exact algebraic
identity in $H_A(q)$, and the result is a **polynomial in $q$**:
the Skein polynomial of the nuclear link.

**Theorem.**
Let $\mathcal{N}(Z, N)$ be the Gröbner--Shirshov-reduced
nuclear braid word in $H_A(q)$
([nuclear Gröbner--Shirshov reduction](#prop:nuclear-groebner-reduction)).
At each generator $\sigma_i$, let $(a_i, b_i)$ be the
transfer-matrix-reduced chain coefficients
([generator volume decomposition](#prop:generator-volume-decomposition)).
Let $z = 1/(q^{1/2} + q^{-1/2})$ be the Markov trace parameter.
Then the Markov trace factors exactly:

$$
  \mathrm{tr}_{\mathrm{Markov}}\!\bigl(
    \mathcal{N}(Z, N)
  \bigr)
  = 
  \prod_{i=0}^{A-2}
  \bigl(z \cdot a_i + b_i\bigr).
$$

Each $\hat{V}_i = z \cdot a_i + b_i$ is a **polynomial in
$q$** (since $a_i, b_i$ are polynomials in $q$ from the
transfer matrix product, and $z$ is rational in $q^{1/2}$).
The full trace is therefore a **product of polynomials** — the
factored form of the nuclear Skein polynomial.

## The transfer matrix IS the polynomial

At each crossing between nucleons $i$ and $j$, the transfer
matrix

$$
  T_j = 
  \begin{pmatrix}
    c_j(q - q^{-1}) + d_j & c_j \\
    c_j & d_j
  \end{pmatrix}
$$

has entries that are polynomials in $q$.  The crossing types
determine the coefficients:

| Pair type | $c_j$ | $d_j$ | $\det(T_j)$ |
|-----------|-------|-------|:-----------:|
| $\mathfrak{p}$-$\mathfrak{p}$ | $1$ | $0$ | $-1$ |
| $\mathfrak{n}$-$\mathfrak{n}$ | $1$ | $-(q - q^{-1})$ | $-1$ |
| mixed | $1$ | $-\frac{1}{2}(q - q^{-1})$ | $-1 - \frac{1}{4}(q - q^{-1})^2$ |

The product of $k_i$ transfer matrices at generator $\sigma_i$
gives $M_i \in \mathrm{GL}_2(\mathbb{Q}(q))$, whose entries are
polynomials in $q$ of degree $\leq 2k_i$.  Then:

$$
  \hat{V}_i(q) =  z \cdot (M_i)_{11} + (M_i)_{21}
$$

is a polynomial in $q^{1/2}$.  The nuclear Skein polynomial is:

$$
  P_{\mathcal{N}}(q) =  \prod_{i=0}^{A-2} \hat{V}_i(q)
$$

**This product IS the Skein polynomial of the nuclear link
$\mathcal{N}(Z, N)$**, written in factored form.  Evaluating at
the substrate $q$ gives the physical categorical action.

## $q$ as the polynomial variable

The substrate parameter $q$ is simultaneously:

1. **The deformation parameter** of the Iwahori--Hecke algebra $H_A(q)$,
   controlling the deviation from the symmetric group.
2. **The variable** of the Skein polynomial, in which each
   transfer matrix entry is polynomial.
3. **The physical parameter** the substrate $q$, determined by the
   Descartes condition $\chi(A) = -6$.

The entire nuclear physics is encoded in the polynomial
$P_{\mathcal{N}}(q)$.  Computing the polynomial requires
exactly $\binom{A}{2}$ transfer matrix multiplications.
Evaluating the polynomial at the substrate parameter $q$ gives the energy.
Taking the ratio $P_{\mathrm{par}}(q) / P_{\mathrm{dau}}(q)$
gives the matrix element for beta decay.
## Consequence: the chain of invariant-preserving maps

$$
  \mathbb{Z}[B_A]
  \xrightarrow{\text{Hecke quotient}}
  H_A(q)
  \xrightarrow{\text{transfer matrices}}
  \prod_{i} (a_i(q) \sigma_i + b_i(q))
  \xrightarrow{\text{Markov trace}}
  \prod_{i} \hat{V}_i(q)
  = 
  P_{\mathcal{N}}(q)
$$

Each step preserves the link invariant.  The polynomial
$P_{\mathcal{N}}(q)$ is a well-defined invariant of the nuclear
link $\mathcal{N}(Z, N)$ — it does not depend on the braid
representative or the reduction path.  Evaluating at
the substrate $q$ projects the polynomial invariant to the physical
energy.

## The polynomial degree

The degree of $P_{\mathcal{N}}(q)$ as a polynomial in $q^{1/2}$
is bounded by:

$$
  \deg P_{\mathcal{N}}  \leq 
  \sum_{i=0}^{A-2} (2k_i + 1)
  = 
  A(A-1) + (A-1)
  = 
  (A-1)(A+1)
  = 
  A^2 - 1
$$

For ${}^{14}\mathrm{C}$: $\deg \leq 195$.  For
${}^{210}\mathrm{Bi}$: $\deg \leq 44{,}099$.  The transfer
matrix product evaluates this polynomial at the substrate parameter $q$
without ever expanding it.

## Asymptotic behaviour

For heavy nuclei ($A \gg 1$), the ratio of $L_0^{-}$ and parent
traces converges:

$$
  \frac{\mathrm{tr}(L_0^{-})}{\mathrm{tr}(\mathcal{N})}
   \longrightarrow 
  \frac{1}{\hbar_q}
  = 
  \frac{1}{1 - q^{-1}}
   \approx  10.09
  \quad\text{as } A \to \infty.
$$

The sub-leading correction is $O(1/A)$ and carries the
nucleus-specific information (shell structure, pairing).
<!-- FILE_END: markov-trace-factorization.md -->

<!-- FILE_START: ks-multiplicativity-via-markov.md -->
Kontsevich--Soibelman's Theorem 8 \cite{kontsevich-soibelman-2008}
states that the Donaldson--Thomas counting map
$\Phi \colon H(\mathbf{C}) \to R_\Gamma$ is a homomorphism of
$\Gamma$-graded algebras — *disjoint union maps to product*. Their
proof routes through the **motivic Hall algebra** (their Propositions
10--12): a stack-level integration whose foundations
(ind-constructibility, orientation data, the motivic quantum torus)
occupy most of the paper.

In the QOU setting the same multiplicativity is **two lines** — the
same reduction by which the Gröbner--Shirshov / Diamond-Lemma proof
of Poincaré--Birkhoff--Witt \cite{bergman1978} replaces the
analytic Lie-theoretic argument (the unital Gröbner-bases route to
PBW).

**Setup (two definitions).**

1. *The disjoint-union monoid of links.* Links form a commutative
   monoid $(\mathcal{L}, \sqcup)$ under split union; on braids this is
   the block inclusion
   $H_m(q) \otimes H_n(q) \hookrightarrow H_{m+n}(q)$.
2. *The Markov trace*
   $\mathrm{tr}_M \colon \mathcal{L} \to \mathbb{Z}[q^{\pm 1/2}]$.

**Two-line proof.** A split braid $\beta \sqcup \beta'$ has no
generator $\sigma_i$ linking the two blocks, so the right-to-left
Markov peel ([Markov-trace
factorization](#thm:markov-trace-factorization)) processes the two
blocks independently — peeling $\beta'$ never meets a generator of
$\beta$. Hence

$$
  \mathrm{tr}_M(\beta \sqcup \beta')
  \;=\;
  \mathrm{tr}_M(\beta)\,\mathrm{tr}_M(\beta'),
$$

i.e. $\mathrm{tr}_M$ is a **monoid homomorphism**
$(\mathcal{L}, \sqcup) \to (\mathbb{Z}[q^{\pm 1/2}], \cdot)$.
$\square$

This is the QOU avatar of KS Theorem 8 — the invariant is
multiplicative — with no Hall algebra, motivic measure, or
ind-constructibility: a known result given a prior heavy/motivic
proof, recovered here by an elementary algebraic one.

**Precision (what is and is not claimed).** The multiplicativity is
for the **monoidal** structure $\sqcup = \otimes$, *not* the internal
product:
$\mathrm{tr}_M(ab) \neq \mathrm{tr}_M(a)\,\mathrm{tr}_M(b)$ in
general (only the trace property
$\mathrm{tr}_M(ab) = \mathrm{tr}_M(ba)$ holds). KS Theorem 8 is
likewise a statement about the counting/integration map on the
*disjoint-union* grading, not the internal multiplication. The
shortcut applies to that statement only — not to the wall-crossing
apparatus (KS Theorems 3--4), which is the archimedean locus the QOU
framework deliberately does not enter.
<!-- FILE_END: ks-multiplicativity-via-markov.md -->

<!-- FILE_START: markov-trace-ratio-exact.md -->
**Proposition (normalization-independence of Markov-trace ratios).**
*For braids $\beta_1, \beta_2 \in B_n$ with $\operatorname{tr}_M(\beta_2) \neq 0$,
and for the Jones normalisation factor
$C(n, q) = (-q^{1/2} - q^{-1/2})^{n-1}$:*

$$
  \frac{J_{K_1}(q)}{J_{K_2}(q)}
  \;=\;
  \frac{C(n, q) \cdot \operatorname{tr}_M(\beta_1)}{C(n, q) \cdot \operatorname{tr}_M(\beta_2)}
  \;=\;
  \frac{\operatorname{tr}_M(\beta_1)}{\operatorname{tr}_M(\beta_2)}.
$$

*In particular, the Gram matrix $G_{ij} = \operatorname{tr}_M(b_i \cdot b_j)$,
the LP cost vectors $t_k = \operatorname{tr}_M(b_k)$, and the shadow
prices $y^*$ from the operator-selection LP are all exact up to a global
scalar that cancels in every ratio, inner product, and optimality
condition.*

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: markov-trace-ratio-exact.md -->

<!-- FILE_START: vassiliev-filtration-mass-tower.md -->
The Markov trace $\operatorname{tr}_M(\beta)(q)$ of a braid word
$\beta$ is a rational function of $q$. Expanding about $q = 1$
(the classical limit) in the Hecke deformation parameter
$h = q - q^{-1}$:

$$
  \operatorname{tr}_M(\beta)(q)
  \;=\;
  \underbrace{c_0(\beta)}_{\text{type 0}}
  \;+\;
  \underbrace{c_1(\beta) \cdot h}_{\text{type 1}}
  \;+\;
  \underbrace{c_2(\beta) \cdot h^2}_{\text{type 2}}
  \;+\;
  \cdots
$$

Each coefficient $c_k(\beta)$ is a **Vassiliev invariant of type
$k$** (also called a finite-type invariant of order $k$). This is
a theorem of Birman-Lin (1993) \cite{birmanlin1993}: the coefficients of
the power series expansion of any quantum knot invariant at $q = 1$ are
finite-type invariants, with the order matching the power of the
deformation parameter.

## Content of the Vassiliev grading

The graded decomposition
$V_0 \subset V_1 \subset V_2 \subset \cdots$ of knot invariants
by type gives a **canonical filtration by complexity**:

| Type | Detects | Mass-formula role | Example |
|---|---|---|---|
| 0 | Number of components | Baryon vs meson | $c_0 = 1$ for all knots |
| 1 | Linking number | — (vanishes for knots) | $c_1 = 0$ for any knot |
| 2 | Framing / writhe | Leading mass correction | $c_2 \propto$ the $h^2$ term in $\lambda_{\mathrm{scale}}$ |
| 3 | Crossing-change sensitivity | Sub-leading mass | $c_3$ distinguishes trefoil from unknot |
| $k$ | $k$-fold crossing relations | Order-$k$ mass correction | $c_k$ gives the $h^k$ mass term |

**For the mass formula**, the Vassiliev filtration means:

1. **The leading term** $c_0 = \operatorname{tr}_M(\beta)(q=1)$
   is the classical Markov trace — it gives the
   "all-knots-are-equivalent" baseline (all knots have the same
   $c_0$; mass differences arise at $k \geq 2$).

2. **The $h^2$ correction** $c_2 \cdot h^2$ is the first
   mass-discriminating term. This is exactly the term that the
   CAL-4 $\lambda_{\mathrm{scale}}$ investigation (PRs #888–#969)
   was trying to derive — it is a **type-2 Vassiliev invariant**.
   (In the canonical production formula this $h^2$ term is absorbed
   into the per-block density $\varrho(K)$; $\lambda_{\mathrm{scale}}$
   survives only as the acknowledged-CAL-4 near-form of
   [`conj:borromean-baryon-mass-formula`](#conj:borromean-baryon-mass-formula),
   not as a standalone derived factor.)

3. **Higher corrections** $c_k \cdot h^k$ for $k \geq 3$
   give the precision refinements. The mass tower's convergence
   rate is controlled by $|h|^k = |q - q^{-1}|^k \approx
   (0.209)^k$ at substrate $q_0 \approx 1.110$ — each order
   suppresses by a factor of $\sim 0.209$, giving roughly one
   additional decimal digit of precision per Vassiliev order.

## Connection to the Archimedean-image table

In the Archimedean-image table
([`rem:archimedean-image-table`](#rem:archimedean-image-table)),
each row's $\tau$-image can be decomposed via the Vassiliev
filtration:

- **Row 3 (Markov trace)**: $\operatorname{tr}_M = c_0 + c_2 h^2
  + c_3 h^3 + \cdots$ — the full Vassiliev expansion.
- **Row 4 (Jones polynomial)**: proportional to row 3; same
  Vassiliev coefficients up to normalisation.
- **Row 5 (HOMFLYPT)**: the two-variable expansion
  $P(K; v, z) = \sum_{i,j} a_{ij} v^i z^j$ gives a
  **two-dimensional** Vassiliev-like grading — the $z$-degree
  controls the Vassiliev type, while the $v$-degree controls
  the SU($N$) channel. This is strictly richer than the one-
  variable Jones expansion.
- **Row 7 (Wedderburn $\dim_q V_\lambda$)**: the quantum dimension
  is a type-0 invariant (it depends only on the partition, not on
  the braid). The per-partition contribution
  $y_\lambda \cdot \chi_\lambda(\beta)$ has Vassiliev type
  controlled by the partition's content statistics.

## Connection to optimisation

For the LP/SDP operator-selection framework — concretely the
[knot operator energy](#def:knot-operator-energy)
$E(\lambda, q) = |w_\lambda/d_\lambda - 1/[k]_q!|$ — the
Vassiliev filtration provides a **canonical cost-vector basis**
at each type:

$$
  t_k^{(\mathrm{type}\,m)}
  \;=\;
  c_m(b_k)
  \quad\text{(type-$m$ Vassiliev invariant of basis element $b_k$)}
$$

The LP at type $m$ finds the optimal operator for the type-$m$
mass correction, independent of higher-order terms. This
decomposes the mass-formula optimisation into a **graded hierarchy**
of independent LPs — one per Vassiliev type — whose solutions
can be composed to give the full mass prediction.

This decomposition follows directly from the Vassiliev
filtration's compatibility with the Markov trace.
<!-- FILE_END: vassiliev-filtration-mass-tower.md -->

<!-- FILE_START: hecke-quandle.md -->
## The quandle axioms as Reidemeister moves

A **quandle** $(Q, \triangleright)$ is a set $Q$ with a binary
operation $\triangleright : Q \times Q \to Q$ satisfying three
axioms that encode the three Reidemeister moves algebraically
\cite{joyce1982}, \cite{matveev1982}:

| Axiom | Formula | Reidemeister move |
|---|---|---|
| **Idempotency** | $a \triangleright a = a$ | R1: a strand crossing itself can be removed |
| **Right-invertibility** | $\forall\, a, b \in Q,\;\exists!\, c : c \triangleright a = b$ | R2: two opposite crossings cancel |
| **Self-distributivity** | $(a \triangleright b) \triangleright c = (a \triangleright c) \triangleright (b \triangleright c)$ | R3: a strand can slide past a crossing |

The **knot quandle** $Q(K)$ of an oriented knot $K$ is the set of
arcs of a knot diagram with the crossing rule: at each crossing,
the under-arc $a$ acts on the over-arc $b$ to produce the outgoing
arc $a \triangleright b$. Joyce's theorem (1982, proved
rigorously): $Q(K) \cong Q(K')$ if and only if $K$ and $K'$ are
ambient isotopic as oriented knots. The knot quandle is therefore
a **complete invariant** of oriented prime knots — strictly more
powerful than any polynomial invariant (HOMFLYPT, Jones, Alexander).

## The Hecke quandle $Q_H(q)$

The Hecke algebra's quadratic relation
$\sigma_i^2 = h \sigma_i + 1$ (with $h = q - q^{-1}$) defines a natural quandle
structure on the set of Hecke elements:

$$
  a \triangleright_H b
  \;:=\;
  h \cdot b + \sigma_i^{-1} a \sigma_i
$$

where $\sigma_i$ is the Hecke generator at the crossing where $a$
and $b$ meet. This satisfies the quandle axioms because the Hecke
relation encodes the braid relations (which ARE the Reidemeister
moves for braids).

**The Hecke quandle $Q_H(q)$** is the quandle $(H_n(q), \triangleright_H)$.
It deforms the **permutation quandle** $Q_H(1) = (S_n, \text{conjugation})$
at $q = 1$ and recovers the **dihedral quandle** $R_n$ at
$q = -1$ (roots of unity).

## Flavour-parameterised quandle

The QOU mass formula uses **averaged crossings**
$I = \sigma - (h/2) \cdot 1$ whose coefficient $h/2$ depends on
the quark flavour at the crossing
([`rem:operator-valued-magnitude-budget`](#rem:operator-valued-magnitude-budget)).
In the quandle language, this means the crossing operation
$\triangleright$ is not fixed — it varies per crossing depending
on the strand labels:

$$
  a \triangleright_f b
  \;=\;
  h_f \cdot b + \sigma_i^{-1} a \sigma_i
$$

where $h_f$ is a flavour-dependent crossing coefficient. The proton uses
$h_f = h_0$ for $u$-$u$ crossings and $h_f' = h_0 - h/2$ for $u$-$d$
crossings. The neutron uses the
complementary assignment.

This is a **parameterised quandle** — the crossing rule varies
over a parameter space (the flavour group). Parameterised quandles
are studied in the literature as
**biquandles** (Fenn-Rourke-Sanderson 1995) and
**virtual quandles** (Kauffman 1999); the QOU's flavour
parameterisation is a specific instance where the parameter space
is the $\mathrm{SU}(3)_{\mathrm{flavour}}$ representation.

## Relevance of quandles to the mass formula

### 1. Completeness beyond polynomials

The knot quandle is a **complete invariant** (Joyce's theorem) —
it distinguishes knots that share the same HOMFLYPT, Jones, and
Alexander polynomials. For the mass formula, this means:

- If two baryon braids have the same HOMFLYPT (as shown for
  proton/neutron via amphicheirality), the quandle CAN still
  distinguish them — because the flavour-parameterised quandle
  encodes the operator-valued crossing structure that the
  polynomial misses.
- The quandle IS the complete algebraic object encoding "which
  crossing rule applies where" — exactly the data the mass
  formula needs beyond the topological polynomial.

### 2. Coloring count as a state-counting invariant

The **quandle coloring number** $\mathrm{Col}_Q(K) = |\mathrm{Hom}(Q(K), Q)|$
counts the number of quandle homomorphisms from the knot quandle
to a fixed quandle $Q$. For the Hecke quandle $Q_H(q)$:

$$
  \mathrm{Col}_{Q_H(q)}(K)
  \;=\;
  \text{number of distinct Hecke representations of } K
$$

This counts the **number of physically distinct baryonic states**
within the topological class $K$. For the Borromean link with the
flavour-parameterised quandle, $\mathrm{Col}_{Q_f}(\mathcal{B}_3)$
counts the number of distinct $(u, d, s)$ flavour assignments
that give topologically inequivalent braid closures — this IS the
baryon multiplet.

### 3. Quandle cocycle invariants for the Gram matrix

The **quandle cocycle invariant** (Carter-Jelsovsky-Kamada-Langford-
Saito 2003) assigns weights from a 2-cocycle $\phi : Q \times Q \to A$
(values in an abelian group $A$) to each crossing:

$$
  \Phi_\phi(K) \;=\; \sum_{\text{colorings}} \prod_{\text{crossings}} \phi(a_i, b_i)
$$

For the Hecke quandle, the natural 2-cocycle is the **Markov trace
weight**: $\phi(a, b) = y_\lambda \cdot \chi_\lambda(\sigma_i)$ at
the crossing where arcs $a, b$ meet. This makes
$\Phi_\phi(K) = \operatorname{tr}_M(K)$ — the Markov trace IS a
quandle cocycle invariant.

This connection means the Gram matrix
$G_{ij} = \operatorname{tr}_M(b_i \cdot b_j)$ is a
**quandle-cocycle Gram matrix**, and the LP/SDP optimisation over
it is an optimisation over quandle-cocycle invariants. The quandle
framework gives the Gram matrix a REPRESENTATION-THEORETIC
interpretation beyond the Hecke-algebra computation.

## Directions opened by the quandle framework

1. **Non-polynomial invariants for the mass formula.** The quandle
   coloring number and cocycle invariants are strictly finer than
   HOMFLYPT — they can distinguish proton from neutron even when
   the HOMFLYPT cannot (because the flavour-parameterised quandle
   IS different for proton vs neutron, while the braid topology
   is amphicheiral).

2. **State-counting optimisation.** The coloring number
   $\mathrm{Col}_{Q_f}(K)$ provides a discrete invariant (an
   integer) that counts physical states. Integer-valued invariants
   are natural for LP constraint counts — each coloring is a
   feasible point in the LP, and the optimal coloring gives the
   ground-state mass.

3. **Canonical crossing rules from quandle axioms.** The three
   quandle axioms (idempotency, invertibility, self-distributivity)
   constrain the averaged-crossing coefficients. If the
   flavour-parameterised Hecke quandle must satisfy these axioms
   for ALL knot diagrams (not just the specific braid words used
   in the mass formula), this gives **algebraic constraints on
   the crossing coefficients** — potentially deriving them from
   first principles rather than fitting to CODATA. This is the
   quandle route to closing
   [`conj:canonical-knot-id-sdp`](#conj:canonical-knot-id-sdp).
<!-- FILE_END: hecke-quandle.md -->

<!-- FILE_START: knot-operator-bring-action.md -->
The six Gröbner-Shirshov normal-form basis elements of $H_3(q)$
act on the Bring surface $\Sigma_4$ (genus $4$, $\chi = -6$) via
the Hecke representation. This remark makes the action explicit
and identifies the $\mathrm{SO}(3)$ structure that the current
pipeline exploits only partially.

## The six basis operators

The Hecke algebra $H_3(q)$ has dimension $3! = 6$. In the
Gröbner-Shirshov normal form, the basis elements are:

| $k$ | Name | Word | Permutation | $\operatorname{tr}_M$ at $q_0$ |
|---|---|---|---|---|
| 0 | $\gamma$ (identity) | $$ | $e$ | $1.000$ |
| 1 | $\sigma_0$ | $(0)$ | $(1\;2)$ | $0.499$ |
| 2 | $\sigma_1$ | $(1)$ | $(2\;3)$ | $0.499$ |
| 3 | $L_+$ | $(0, 1)$ | $(1\;2\;3)$ | $0.249$ |
| 4 | $L_-$ | $(1, 0)$ | $(1\;3\;2)$ | $0.249$ |
| 5 | $e^-$ | $(0, 1, 0)$ | $(1\;3)$ | $0.551$ |

The Gram matrix $G_{ij} = \operatorname{tr}_M(b_i \cdot b_j)$
encodes the inner-product structure: $G$ is a $6 \times 6$
symmetric positive-definite matrix whose inverse $G^{-1}$ defines
the Frobenius dual basis.

## Action on the Bring surface

Bring's surface $\Sigma_4$ has the structure of a degree-5
algebraic curve with $S_5$ symmetry. The three quark strands of a
baryon braid thread through the color-tube cubic
$\Delta(z) = z^3 + p z + r = 0$ on $\Sigma_4$, with the three
roots $z_1, z_2, z_3$ representing the quark positions on the
surface.

Each basis operator $b_k \in H_3(q)$ acts on the root triple
$(z_1, z_2, z_3)$ by permuting and $q$-deforming the roots:

| Operator | Action on roots | Geometric interpretation |
|---|---|---|
| $\gamma$ | $(z_1, z_2, z_3) \mapsto (z_1, z_2, z_3)$ | Identity — no crossing |
| $\sigma_0$ | $(z_1, z_2, z_3) \mapsto (q z_2, q^{-1} z_1, z_3)$ | Strands 1–2 cross; $q$-deformation shifts the roots along the color tube |
| $\sigma_1$ | $(z_1, z_2, z_3) \mapsto (z_1, q z_3, q^{-1} z_2)$ | Strands 2–3 cross |
| $L_+$ | $\sigma_0 \sigma_1$ | Full 3-cycle: $(1 \to 2 \to 3 \to 1)$ |
| $L_-$ | $\sigma_1 \sigma_0$ | Reverse 3-cycle: $(1 \to 3 \to 2 \to 1)$ |
| $e^-$ | $\sigma_0 \sigma_1 \sigma_0$ | Transposition $(1\;3)$ via braid relation |

The $q$-deformation factors distinguish this from the classical
$S_3$ permutation action: at $q = 1$, the action is pure
permutation; at $q = q_0 \neq 1$, each crossing
shifts the root positions along the color-tube fibre by a factor
of $q$ or $q^{-1}$.

## The $S_3 \subset \mathrm{SO}(3)$ gap

The six basis operators generate the **discrete** group
$S_3 \cong \mathrm{Dih}_3$ — the group of permutations of three
objects. This is a **subgroup** of $\mathrm{SO}(3)$:

$$
  S_3 \;\hookrightarrow\; \mathrm{SO}(3)
$$

embedded as the symmetry group of the equilateral triangle (the
three quark positions at $120°$ intervals on the color-tube
cross-section).

The **full** $\mathrm{SO}(3)$ acts by rotating the color-tube
cross-section continuously. This gives a continuous family of
crossing conventions parameterised by
$\mathrm{SO}(3) / S_3$ — a 3-dimensional manifold minus the
discrete quotient.

**Pipeline inputs:** only the $S_3$ subgroup — the six
discrete basis operators. The averaged crossing
$I = \sigma - (h/2) \cdot 1$ averages over the $S_3$ orbit.

**Pipeline exclusions:** the continuous
$\mathrm{SO}(3) / S_3$ rotations. These would give:

1. **Continuous families of Gram matrices** $G(\theta)$
   parameterised by rotation angle $\theta$. The LP shadow prices
   $y^*(\theta)$ would vary continuously, potentially identifying
   optimal orientations for the binding-energy prediction.

2. **Angular-momentum quantum numbers** from the
   $\mathrm{SO}(3)$ representation theory. The irreps of
   $\mathrm{SO}(3)$ are labelled by angular momentum $\ell$;
   restricting to $S_3$ gives the branching rule
   $V_\ell|_{S_3} = \bigoplus_\lambda n_{\ell,\lambda} V_\lambda$
   where the multiplicity $n_{\ell,\lambda}$ counts how many times
   each $S_3$ irrep appears in the $\ell$-th angular-momentum
   channel. These multiplicities are computable from character
   theory and may give the missing per-partition $\Delta_\lambda$
   values.

3. **Spherical harmonics on the Bring surface.** The Bring
   surface's genus-4 topology carries a natural Laplacian whose
   eigenfunctions are generalised spherical harmonics. The
   $\mathrm{SO}(3)$ action decomposes these into angular-momentum
   channels. The Markov trace, viewed as a function on the Bring
   surface, expands in these harmonics — giving a spectral
   decomposition of the mass formula in angular-momentum space.

## The Gram inverse on the Bring surface

The Gram inverse $G^{-1}$ defines the Frobenius dual basis:
$b_k^\vee = \sum_j (G^{-1})_{kj} b_j$. On the Bring surface,
$G^{-1}$ is the **metric inverse** — it converts between the
"crossing basis" (knot operators $b_k$) and the "demand basis"
(Frobenius duals $b_k^\vee$).

The LP/SDP operator-selection framework minimises
$\sum t_k x_k$ subject to Gram constraints. In the Bring-surface
interpretation, this is a **minimum-action principle on
$\Sigma_4$**: the optimal knot operator is the one that minimises
the action functional (Markov trace) over the moduli space of
braid embeddings in the Bring surface.

The $\mathrm{SO}(3)$ extension would make this a minimum-action
principle on $\Sigma_4 \times \mathrm{SO}(3) / S_3$ — optimising
over both the knot type AND the orientation. If the minimum over
orientations is unique (which would follow from the Bring
surface's rigidity as a hyperbolic 3-manifold complement), this
would derive the averaged-crossing convention from a variational
principle — closing
[`conj:canonical-knot-id-sdp`](#conj:canonical-knot-id-sdp).
<!-- FILE_END: knot-operator-bring-action.md -->

<!-- FILE_START: phi-q-resums-trace-series.md -->
**Audit note for the reader who wonders whether Terms 2 and 3 of
([six-term mass formula](#thm:six-term-mass-formula-complete)) are
genuinely outside the algebraic Markov-trace framework.**

The closed-form quantum dilogarithm

$$
  \Phi_q(z) \;=\; \prod_{k \geq 1}(1 - q^{-k} z)^{-1}
$$

makes Terms 2 and 3 *look* like a non-trace species —
transcendental functions of per-generator volumes.  They are not.
Two equivalent expansions both factor $\Phi_q$ through Markov
traces of the same per-generator subwords already used by Term 1.

## Series expansion

Using the standard identity
$\Phi_q(z) = \exp\!\bigl[\sum_{k \geq 1} z^k / (k(1 - q^k))\bigr]$,
each Term-2 contribution unwinds as

$$
  \Phi_q\!\bigl(\hat{V}_i^{\mathrm{full}}\bigr)
  \;=\;
  \exp\!\left[\sum_{k \geq 1}
    \frac{\bigl(\hat V_i^{\mathrm{full}}\bigr)^{k}}{k\,(1 - q^k)}\right],
$$

and each $\bigl(\hat V_i^{\mathrm{full}}\bigr)^k$ is the
Plancherel-weighted Markov trace of $W_i^k$, where $W_i$ is the
length-$\ell_i$ subword of crossings at generator $i$.  Term 3 is
the same with $\hat V_i \hat V_j$ in place of $\hat V_i$.  Both
terms therefore reduce to (a series of) Markov traces of powers of
per-generator (or pair) sub-braids — the same algebraic species
that supplies Terms 1, 4, 5, 6.

## Kähler-lift expansion

The same fact is visible from
([topological mass](#thm:topological-mass)).  The transient summands
$\hbar_q^{2n} \cdot \mathrm{tower}^{(n)}$ are the $n$-th Kähler
differentials of $\mathrm{tr}_M$ in the substrate parameter $q$, so
the entire tower is generated by symbolic differentiation of the
descended trace.  Resumming via $\Phi_q$ collapses the tower into a
single transcendental factor; the underlying algebra remains
Markov-trace arithmetic.

## Practical consequence

Both routes confirm that the six-term formula is, end-to-end, a
construction over Markov traces:

See [Table](#tbl:phi-q-resums-trace-series-table-data).

The $\Phi_q$ resummation in Terms 2--3 is a computational
convenience — exact and faster than series truncation — but it
*conceals* the fact that nothing structurally new appears beyond
Markov-trace arithmetic and its Kähler / dilogarithm transforms.
A reader scanning the formula for a single algebraic engine will
find it: the canonical Jones--Markov trace, applied to atomic
braids and their derivatives.

The recursive-ascent compute path
([Markov-axiom recursive ascent](https://github.com/litlfred/qou/issues/508))
is the production engine for the trace-form of every term it
covers (1, 4, 5, 6); Terms 2 and 3 retain $\Phi_q$ for performance
but are reachable from the same engine via series or differentiation
on demand.
<!-- FILE_END: phi-q-resums-trace-series.md -->

<!-- FILE_START: markov-axiom-recursive-ascent.md -->
**Definition** (:defterm[Markov-axiom recursive ascent]{#markov-axiom-recursive-ascent}).
Given a braid $\beta \in B_n$ with Hecke representative
$T_w \in H_n(q)$ in Gröbner–Shirshov normal form, the *recursive
ascent* algorithm evaluates the canonical Jones–Markov trace
$\mathrm{tr}_M^{(n)}(T_w) \in \mathbb{Z}[q^{1/2}, q^{-1/2}]$ by

1. **Eliminate inverse generators.** Whenever an
   $\sigma_i^{-1}$ factor appears, expand
   $\sigma_i^{-1} = \sigma_i - (q - q^{-1})$
   (the Hecke-relation identity for the inverse), so that the
   reduced word contains only positive generators.
2. **Peel the top generator.** Express
   $T_w = T_{w'} \cdot \sigma_{n-1}$ with
   $T_{w'} \in H_{n-1}(q)$ via Garside / Gröbner–Shirshov
   normalisation; the
   ([Markov pair identity](#prop:markov-pair-z2))
   gives
   $\mathrm{tr}_M^{(n)}(T_w) = z \cdot \mathrm{tr}_M^{(n-1)}(T_{w'})$
   where $z = 1 / (q^{1/2} + q^{-1/2})$.  (No inverse factor
   is ever peeled; inverses were eliminated in step 1.)
3. **Branch on the Hecke quadratic.** Whenever a $\sigma_i^2$
   factor appears, expand
   $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$
   into two recursive sub-traces and combine.
4. **Recurse** on $T_{w'}$ at level $n - 1$ until the chain
   $H_n \supset H_{n-1} \supset \cdots \supset H_1$ terminates
   at the base case $\mathrm{tr}_M^{(1)}(\mathbf{1}) = 1$.

**Significance.** The naive Hoefsmit per-Wedderburn-block path
materialises symbolic matrices of dimension up to $\dim_\lambda \leq 462$
for every partition $\lambda \vdash 3A$ and multiplies along the
braid word — for $A \geq 4$ this is computationally infeasible
(${\sim} 30$ minutes per atom).  Recursive ascent never
materialises a matrix representation: the cost is bounded by the
braid length and the depth of the Hecke-quadratic branching tree.

The production implementation
(the formal derivation) completes
$\mathfrak{m}({}^{4}\mathrm{He})$ end-to-end in ~60 s and
$\mathfrak{m}({}^{6}\mathrm{Li})$ within minutes, with all
$A \leq 3$ atoms cross-checked against the Hoefsmit + Wenzl
bridge witness (`atomic-tr-m-mpfr-50dps.witness.json`) to within
$\sim 4 \cdot 10^{-16}$.  The witness file
`markov-peel-atomic-tr-m.witness.json` records the production
results from $\mathfrak{p}, \mathfrak{n}$ through ${}^{6}\mathrm{Li}$.

**Lean status.**  The Lean module `QOU.Interactions.MarkovPeel`
declares the abstract `MarkovTrace` typeclass encoding the three
defining axioms (M1 cyclicity, M2 Markov peel, M3 unit), states
the reference identity
([Markov pair identity](#prop:markov-pair-z2)), and stubs the
recursive evaluator as a `noncomputable` declaration.  The body
of `markov_peel` and the proof of `markov_pair_z2` are open
work items
([#508](https://github.com/litlfred/qou/issues/508) Phase 6);
the Python production path supplies the computational witness in
the meantime.

**Scope of this definition.**  The recursive-ascent algorithm
covers Term 1 of the
([six-term mass formula](#thm:six-term-mass-formula-complete))
directly, and reaches Terms 4, 5, 6 via specialised inputs
(the Frobenius co-Casimir element, braid-mirror products, and
residues at primitive roots of unity respectively).  Terms 2, 3
are reachable through the
([$\Phi_q$ trace-series remark](#rem:phi-q-resums-trace-series))
via Kähler-lift differentiation or series truncation; the closed
$\Phi_q$ form remains the production fast path for those terms.
<!-- FILE_END: markov-axiom-recursive-ascent.md -->

<!-- FILE_START: per-braid-mass-tower.md -->
**Proposition (per-braid mass tower — full jet-level form).**
*Let $W \in B_{3A}$ be the atomic braid of a nucleus $(Z, N)$,
$\mathrm{tr}_M$ the Markov trace on $H_{3A}(q)$
([Jones–Markov trace](#thm:jones-markov-trace)), $\Phi_q$ the
quantum dilogarithm, $z = 1/(q^{1/2} + q^{-1/2})$ the Markov
weight, and $\mathcal{S}^{(n)}_\ell$ the depth-$\ell$ stratum of
$W$ at jet level $n$ in the recursive brane tower
$A_{n+1} = A_n \otimes \Omega^1(A_n)$
([recursive brane tower](#def:recursive-brane-tower)). The mass
functional decomposes as*

$$
  \mathfrak{m}(W)
  \;=\;
  \underbrace{\bigl|\mathrm{tr}_M(W)\bigr|}_{\substack{\text{descended} \\ \text{(level 0 only)}}}
  +\,
  \sum_{n=0}^{N}\!
    \left(\,
      \underbrace{\sum_{\xi \in \mathcal{S}^{(n)}_1}\!\!
        \Phi_q\!\bigl(|\mathrm{tr}_M(\xi)|\bigr)}_{\text{singletons at jet level } n}
      +\,
      z^{2}\!\!\!\underbrace{\sum_{(\xi,\xi') \in \mathcal{S}^{(n)}_2}\!\!\!\!
        \Phi_q\!\bigl(|\mathrm{tr}_M(\xi\,\xi')|\bigr)}_{\text{pairs at jet level } n}
    \right)
  +\, R_N
$$

*where $R_N$ is the geometric-series tail bound from
([brane-tower tail bound](#prop:jet-tower-convergence)):
$|R_N| \leq \Delta_{\max}\,\hbar_q^{2(N+1)}/(1 - \hbar_q^{2})$,
per the [jet-tower remark](#rem:mass-endomorphism-jet-tower).
Triple-or-higher interactions at level $n$ ascend via the
pentagon identity to pairs/singletons at level $n+1$
([pentagon UV commutation](#prop:pentagon-uv-commutation)) and
are already captured by the level-$(n+1)$ sum.*

**Three structural features:**

* The **descended** term appears **only at $n = 0$** —
  $\mathcal{A}^{\mathrm{desc}}_n = \mathrm{im}\,\hat\tau_n$ is the
  image of the :refterm[descent]{#descent} involution; including a separate descended
  product at every jet level would double-count
  ([:refterm[descent]{#descent} eigenspaces](#prop:descent-eigenspaces)).
* Each level $n$ contributes **only singletons and pairs**
  (quadratic closure per level via the pentagon identity).
* $\mathcal{S}^{(n)}_2 = \{(\xi, \xi') : \xi \neq \xi'\}$ is
  the **full set of unordered pairs** at every jet level (per
  `thm:markov-trace-factorization` lifted to all $n$).

*For an atom built from $A$ nucleons at level $n = 0$:*

| Level $\ell$ | Stratum $\mathcal{S}_\ell$              |    Cardinality | Identification                                                                 |
| -----------: | --------------------------------------- | -------------: | ------------------------------------------------------------------------------ |
|          $0$ | $\{W\}$                                 |            $1$ | The full atomic braid                                                          |
|          $1$ | $\{\beta_N : N \in \text{nucleons}\}$   |            $A$ | Per-nucleon sub-braids (3-strand $H_3$ each)                                   |
|          $2$ | $\{(\beta_N, \beta_{N'}) : N \neq N'\}$ | $\binom{A}{2}$ | Per-nucleon-pair sub-braids (6-strand $H_6$ each, with inter-nucleon coupling) |

*All sub-braid Markov traces are computed via the proper $H_{3A}$
Schur–Weyl path ([prop:schur-weyl-mass-decomposition](#prop:schur-weyl-mass-decomposition)),
ensuring $|\mathrm{tr}_M(\xi)| < q$ at $q = q_0$ (the $\Phi_q$
convergence radius).*

## Supersession of the per-generator form

The earlier statement
([mass-endomorphism-tower](#prop:mass-endomorphism-tower)) summed
over **per-generator** terms $\hat V_i^{\text{full}}$ — one per
braid letter $\sigma_i$:

$$
  \mathfrak{m}_{\text{per-gen}}
  \;=\;
  \Bigl|\prod_{i=0}^{n-2} \hat V_i^{\text{full}}\Bigr|
  + \sum_{i=0}^{n-2} \Phi_q(|\hat V_i^{\text{full}}|)
  + z^2\!\!\sum_{(i,j)\in\mathcal{P}_n}\!\!\Phi_q(|\hat V_i^{\text{full}}\hat V_j^{\text{full}}|).
$$

The per-generator $\hat V_i^{\text{full}} = w_{\text{sym}}V_{\text{sym},i}
+ w_{\text{std}}V_{\text{std},i} + w_{\text{alt}}V_{\text{alt},i}$
mixes three Wedderburn channels — but **at the $H_3$ weights
$w_{\text{sym}/\text{std}/\text{alt}} = \dim_q(\lambda)^2/[3]_q!$
for $\lambda \vdash 3$**. Applying these weights per-generator at
$H_{3A}$ is a structural mismatch
([H_3-at-H_{3A} weight derivation](../../../docs/audits/-h3-at-h3a-weight-derivation.md)):
the actual $H_{3A}$ Wedderburn decomposition is indexed by
partitions $\lambda \vdash 3A$, not by $H_3$-channels, and the
per-generator product compounds $\hat V_i$ values past the
$\Phi_q$ convergence radius $|z| < q$.

The **per-braid** form replaces this with three structural
improvements:

1. **Sub-braid traces, not generator products.** Each level-1
   contribution is $\mathrm{tr}_M(\xi)$ for a complete sub-braid,
   computed via the proper $H_{3A}$ Schur–Weyl decomposition.
   $\mathrm{tr}_M$ is bounded by Plancherel measure, so
   $|\mathrm{tr}_M(\xi)| < q$ holds automatically — the $\Phi_q$
   tower converges.

2. **Stratification matches algebraic JSJ.** $\mathcal{S}_\ell$
   coincides with the depth-$\ell$ summands of the
   $J^\bullet$-graded stratification of $H_{3A}(q)$
   ([gb-spectral-sequence](#prop:gb-spectral-sequence),
   [graded-trace-residue-split](#prop:graded-trace-residue-split)).
   The per-braid tower is the explicit content of the algebraic
   JSJ at the level of mass.

3. **Cardinality reduction.** Per-generator gives $3A-1$ singles
   and $\binom{3A-1}{2}$ pairs (e.g., 11 + 55 = 66 terms at
   ${}^4\mathrm{He}$). Per-braid gives $A$ singles and
   $\binom{A}{2}$ pairs (4 + 6 = 10 terms at ${}^4\mathrm{He}$).
   Each per-braid term is a self-contained physical entity (a
   nucleon, a nucleon-pair) — direct match to the :refterm[descent]{#descent} /
   brane-tower picture.

## Compatibility with `prop:mass-endomorphism-tower`

The per-generator form is an **expansion** of the per-braid form
in the limit where each sub-braid is replaced by its
contributing generators. Specifically, the per-generator
$\hat V_i^{\text{full}}$ at H\_3 weights coincides with the
**single-letter Markov trace** $\mathrm{tr}_M(\sigma_i)$ on a
fictitious 2-strand sub-braid — the smallest possible sub-braid
through the generator. The per-generator form thus arises as the
**finest-grained** stratification ($\mathcal{S}_\ell^{\text{gen}} =
\{\sigma_i\}$, $|S_1^{\text{gen}}| = 3A-1$), where the stratification
has been refined past the natural sub-braid scale and the H\_3
weights are inherited from the smallest enclosing Hecke subalgebra
($H_2 \subset H_3$).

The per-generator form **converges** when each
$\hat V_i^{\text{full}} = \mathrm{tr}_M(\sigma_i)|_{H_2}$ alone is
small — but the per-generator product across many generators
escapes the convergence radius. The per-braid form fixes this by
keeping the natural sub-braid scale.

## canonical structural verification

The per-braid tower has been computed for D, ${}^{3}$He, ${}^{3}$H, ${}^{4}$He via
the canonical formalism,
with witness
[`docs/audits/-per-braid-tower.witness.json`](https://github.com/litlfred/qou/blob/claude/audit-math-framework-FXlp2/docs/audits/-per-braid-tower.witness.json).

Per-braid tower values (at $q_0 \approx 1.11$):

| Atom | descended $|\mathrm{tr}_M(W)|$ | single $\sum\Phi_q$ | pair $z^2\sum\Phi_q$ | total | max sub-trace | $\Phi_q$ conv |
|------|------------------------------:|--------------------:|---------------------:|------:|--------------:|:-------------:|
| D    | $1.56 \times 10^{-2}$ | $3.70 \times 10^{3}$ | $2.87 \times 10^{-1}$ | $3.70 \times 10^{3}$ | $0.67$ | yes |
| ${}^{3}$He  | $8.83 \times 10^{-4}$ | $5.55 \times 10^{3}$ | $8.62 \times 10^{-1}$ | $5.55 \times 10^{3}$ | $0.67$ | yes |
| ${}^{3}$H   | $8.83 \times 10^{-4}$ | $5.55 \times 10^{3}$ | $8.62 \times 10^{-1}$ | $5.55 \times 10^{3}$ | $0.67$ | yes |
| ${}^{4}$He  | $4.43 \times 10^{-6}$ | $7.40 \times 10^{3}$ | $1.72$               | $7.40 \times 10^{3}$ | $0.67$ | yes |

For comparison, the per-generator H\_3 tower at the same atoms
gives totals $\sim 10^{6}$ — reflecting the H\_3-at-H\_{3A}
divergence. The per-braid form is convergent because every
sub-braid trace stays well below $q_0 = 1.11$ (max $0.67 \approx 0.6\,q_0$).

## Strict τ-wall compliance

Both sides of the per-braid tower live in $\mathbb{Q}(q_0)$:

* $\mathrm{tr}_M(\xi)$ is the Markov trace of an $H_n(q)$ element
  — algebraic.
* $\Phi_q(z) = \prod_{k\geq 1}(1 - q^{-k}z)^{-1}$ is the
  $q$-Pochhammer; convergent in $\mathbb{Q}(q)$ for $|z| < q$.
* The Markov weight $z = 1/(q^{1/2} + q^{-1/2})$ is in
  $\mathbb{Q}(q^{1/2})$.

No τ-image quantities (hyperbolic volumes, Mostow rigidity, etc.)
appear in the per-braid mass formula. The strict wall is
preserved in proofs as well as in the statement.

## Open: explicit closed form

Conjectural per `conj:mass-endomorphism`: there exists a single
closed-form $\Phi_{\text{mass}}(W) \in H_{3A}(q)$ such that
$\mathfrak{m}(W) = |\mathrm{tr}_M(\Phi_{\text{mass}}(W))|$. The
per-braid tower is the **expansion** of this conjectural element
along the $\mathcal{S}_\bullet$ stratification; the descended
term gives the level-0 part, the single tower the level-1
correction, the pair tower the level-2 correction. Higher-level
corrections (triples, $\ldots$) are absorbed by pentagon-ascension
([pentagon-uv-commutation](#prop:pentagon-uv-commutation),
[mass-endomorphism-jet-tower](#rem:mass-endomorphism-jet-tower)).

The conjecture is open; the per-braid tower up to level 2 is
empirically validated by the witness above.

$\square$

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: per-braid-mass-tower.md -->

