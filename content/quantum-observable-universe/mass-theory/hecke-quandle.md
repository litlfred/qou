## The Hecke quandle and its relevance to the mass formula

### The quandle axioms as Reidemeister moves

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

### The Hecke quandle $Q_H(q)$

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

### Flavour-parameterised quandle

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

### Relevance of quandles to the mass formula

#### 1. Completeness beyond polynomials

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

#### 2. Coloring count as a state-counting invariant

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

#### 3. Quandle cocycle invariants for the Gram matrix

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

### Directions opened by the quandle framework

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
