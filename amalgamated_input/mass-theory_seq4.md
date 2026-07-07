<!-- FILE_START: pentagon-uv-commutation.md -->
The pentagon identity of the quantum dilogarithm
(quantum Bloch group)

$$
  \Phi_q(v)\,\Phi_q(u) \;=\; \Phi_q(u)\,\Phi_q(uv)\,\Phi_q(v)
$$

requires the quantum-torus relation $uv = q\,vu$ on its operator
arguments. This block locates where that relation lives in the
brane-tower formalism and how it drives the jet-tower mass
ascension.

## Within a single jet level — trivial commutation

At a fixed jet level $n$, the traced volumes $\hat V_i^{(n)}
\in \mathbb{Z}[q^{\pm 1/2}, z]$ are **scalar Laurent polynomials**
([def:algebraic-quantum-volume](#def:algebraic-quantum-volume)).
Two scalars commute, so

$$
  \hat V_i^{(n)} \, \hat V_j^{(n)}
  \;=\;
  \hat V_j^{(n)} \, \hat V_i^{(n)}
$$

without any $q$-factor. This is the level-internal lemma
[`lem:vhat-pair-commutation-trace`](#lem:vhat-pair-commutation-trace),
which closes the level-internal half of the audit gap.

## Between adjacent jet levels — the pentagon q-factor

The brane tower
([def:recursive-brane-tower](../lifting-and-descent/recursive-brane-tower.md))
admits a non-commutative quantization in which the level-shift
operator $\hat\tau_n$ supplies the canonical pair $u, v$
satisfying $uv = q\,vu$. Specifically, let $\widehat U_i$ and
$\widehat V_j$ denote level-shift conjugates of $\hat V_i$ and
$\hat V_j$ at adjacent jet levels $n$ and $n+1$. Then

$$
  \widehat U_i \, \widehat V_j
  \;=\;
  q \, \widehat V_j \, \widehat U_i
$$

on the transient summand $\ker \hat\tau_n$ between the two
levels, where the :refterm[descent]{#descent} involution $\hat\tau_n$ separates the
descended part (where the residual $R_q$ lives) from the
transient part (where the pentagon $q$-factor is exact).

**Proposition.** The pentagon identity
$\Phi_q(v)\,\Phi_q(u) = \Phi_q(u)\,\Phi_q(uv)\,\Phi_q(v)$
applies to the operator lift $u = \widehat U_i$, $v = \widehat
V_j$ at adjacent jet levels $n, n+1$, and supplies the
*inter-level ascension rule* for the jet-tower mass formula
([rem:mass-endomorphism-jet-tower](#rem:mass-endomorphism-jet-tower)):

a triple product at jet level $n$ rewrites via pentagon as a
pair plus a singleton at level $n$, leaving a residual
$\Phi_q(uv)$ that ascends to level $n+1$.

## Derivation sketch

The pentagon q-factor is a feature of the brane tower's
$q$-graded jet stratification, not of the scalar $\hat V_i$'s:

1. **Hecke braid relation** at the operator level (before
   :refterm[descent]{#descent} to scalars): $\sigma_s \sigma_{s+1} \sigma_s =
   \sigma_{s+1} \sigma_s \sigma_{s+1}$ in $H_n(R, q)$.
2. **:refterm[Descent]{#descent} involution split**: $\hat\tau_n$ separates
   $H_n(R, q)$ into $\mathrm{im}\,\hat\tau_n$ (descended,
   level-$n$ contribution) and $\ker\,\hat\tau_n$ (transient,
   ascends to level $n+1$).
3. **Eigenvalue specialisation** on the $q$-block of $\sigma_s$
   reduces the descended part to scalar form, where commutation
   is trivial.
4. **Operator lift on the transient part**: the surviving
   non-trivial commutation is between level-$n$ and level-$(n+1)$
   operators, giving the quantum-torus relation $uv = q\,vu$.

The pentagon identity then governs how triple products at level
$n$ reorganise into pair + singleton at level $n$ plus a residual
ascending to level $n+1$ — the algebraic content of the jet-tower
ascension.

## Significance for the mass tower

The mass-tower jet form
([rem:mass-endomorphism-jet-tower](#rem:mass-endomorphism-jet-tower))

$$
  \mathfrak{m} \;=\; |\mathrm{tr}_M(W)|
  + \sum_{n=0}^{N}\!\Bigl(\sum_{\xi \in \mathcal{S}^{(n)}_1}\!\Phi_q(|\mathrm{tr}_M(\xi)|)
  + z^2\!\!\!\sum_{(\xi,\xi') \in \mathcal{S}^{(n)}_2}\!\!\!\Phi_q(|\mathrm{tr}_M(\xi\xi')|)\Bigr)
  + R_N
$$

contains only **singletons** ($\mathcal{S}_1$) and **pairs**
($\mathcal{S}_2$) at each level $n$, plus a tail bound $R_N$.
The pentagon's role is structural: it certifies that **no
triples** appear at any level — every triple at level $n$ is
absorbed into a pair plus singleton at level $n$ plus a
residual that lives at level $n+1$. Iterating gives the jet
ascension; the geometric tail bound from
[`prop:jet-tower-convergence`](#prop:jet-tower-convergence)
controls $R_N$.
<!-- FILE_END: pentagon-uv-commutation.md -->

<!-- FILE_START: transfer-matrix-operator.md -->
Every particle interaction in the Descartes universe is encoded by
a **transfer matrix** $T_{K_1, K_2}(q) \in \mathrm{M}_2(\mathbb{Z}[q^{\pm 1/2}])$
determined by the knot types $K_1, K_2$ of the two interacting
strands.  The transfer matrix acts as an **operator** on the
Gröbner--Shirshov ideal of the Iwahori--Hecke algebra, and its entries are
polynomials in $q$.

## Definition

**Definition.**
Let $K_1, K_2$ be two building block knots
([building blocks](#rem:building-block-knots)) meeting at a
crossing in a braid word $\beta \in B_n$.  The **transfer
matrix** of the crossing is:

$$
  T_{K_1, K_2}(q)
  = 
  \begin{pmatrix}
    c(q - q^{-1}) + d & c \\
    c & d
  \end{pmatrix}
$$

where the **crossing coefficients** $(c, d) \in \mathbb{Z}[q^{\pm 1/2}]^2$
are determined by the knot types:

$$
  c_{K_1, K_2}
  = 
  \frac{J_{K_1}(q) \cdot J_{K_2}(q)}{J_{K_1 \# K_2}(q)},
  \qquad
  d_{K_1, K_2}
  = 
  -c \cdot \frac{q  s}{1 + J_{K_1}(q) \cdot J_{K_2}(q)}
$$

where $J_K(q)$ is the Jones polynomial of knot $K$ and
$s = q^{1/2} - q^{-1/2}$ is the Skein amplitude.

For the three nuclear crossing types (quarks as Borromean
unknot components), this specializes to:

| Crossing | $K_1$ | $K_2$ | $c$ | $d$ | Hecke element |
|----------|-------|-------|-----|-----|---------------|
| $\mathfrak{p}$-$\mathfrak{p}$ | $u$ | $u$ | $1$ | $0$ | $\sigma$ |
| $\mathfrak{n}$-$\mathfrak{n}$ | $d$ | $d$ | $1$ | $-(q - q^{-1})$ | $\sigma^{-1}$ |
| mixed | $u$ | $d$ | $1$ | $-\frac{1}{2}(q - q^{-1})$ | $\frac{1}{2}(\sigma + \sigma^{-1})$ |
<!-- FILE_END: transfer-matrix-operator.md -->

<!-- FILE_START: transfer-matrix-operator-properties.md -->
The [transfer matrix](#def:transfer-matrix-operator)
$T_{K_1, K_2}(q)$ acts on the Gröbner--Shirshov-reduced Hecke chain,
generates a non-commutative operator algebra under composition, and
catalogues every particle interaction together with its $\Delta$
operator and composition rules. These actions, catalogues, and rules
are collected below.

## Action on the Gröbner--Shirshov ideal

The transfer matrix acts on the Iwahori--Hecke algebra element
$a\sigma_i + b$ (the Gröbner--Shirshov-reduced chain at generator
$\sigma_i$) by left multiplication followed by Hecke reduction:

$$
  T_{K_1, K_2}  \cdot  (a\sigma + b)
   := 
  (c\sigma + d)(a\sigma + b)
  \stackrel{T^2 = (q-q^{-1})T + 1}{\longrightarrow}
  a'\sigma + b'
$$

where:

$$
  a' = ac(q - q^{-1}) + ad + bc,
  \qquad
  b' = ac + bd.
$$

In matrix form:

$$
  \begin{pmatrix} a' \\ b' \end{pmatrix}
  = 
  T_{K_1, K_2}(q)
   \cdot 
  \begin{pmatrix} a \\ b \end{pmatrix}
$$

The product of $k$ transfer matrices at generator $\sigma_i$
gives the full chain reduction $M_i = \prod_{j} T_j(q)$, and
the Markov-traced volume is $\hat{V}_i = z \cdot (M_i)_{11} + (M_i)_{21}$.

## The operator algebra

Transfer matrices compose: if strands $K_1$, $K_2$, $K_3$
cross in sequence at generator $\sigma_i$, the combined
operator is:

$$
  T_{K_1 K_3} \circ T_{K_1 K_2}
  = 
  T_{K_1, K_3}(q) \cdot T_{K_1, K_2}(q)
$$

(matrix multiplication).  This is **non-commutative** — the
order of crossings matters.

**The Gröbner--Shirshov ideal is the kernel:**

$$
  I_i =  \ker\!\left(
    \prod_{j} T_j(q) - M_i(q)
  \right)
$$

The ideal $I_i$ at generator $\sigma_i$ absorbs the terms
eliminated by the Hecke relation ($T^2 = (q - q^{-1})T + 1$).
The transfer matrix product $M_i(q)$ is the **quotient** — the
element surviving after modding out $I_i$.

## Interaction catalogue

Every particle interaction corresponds to a transfer matrix.
The **interaction type** is determined by the knot types of
the two strands at the crossing:

### Nuclear interactions (quark-level, Level 1)

| Interaction | $K_1$ | $K_2$ | $T(q)$ | Physical |
|-------------|-------|-------|--------|----------|
| $\mathfrak{u}\mathfrak{u}$ | $T_{2,3}$ | $T_{2,3}$ | $T_{pp}$ | proton-proton repulsion |
| $\mathfrak{d}\mathfrak{d}$ | $T_{2,3}^{\sigma}$ | $T_{2,3}^{\sigma}$ | $T_{nn}$ | neutron-neutron |
| $\mathfrak{u}\mathfrak{d}$ | $T_{2,3}$ | $T_{2,3}^{\sigma}$ | $T_{\mathrm{mix}}$ | proton-neutron binding |

### Electromagnetic interactions (electron-level)

| Interaction | $K_1$ | $K_2$ | Physical |
|-------------|-------|-------|----------|
| $e$-$\mathfrak{p}$ | $T_{2,3}$ | $\mathcal{B}_3$ | Electron-nucleus Coulomb |
| $e$-$e$ | $T_{2,3}$ | $T_{2,3}$ | Electron-electron repulsion |
| $\gamma$-$e$ | $\varnothing$ | $T_{2,3}$ | Photon absorption/emission |

### Photon-electron transfer matrix

The photon ($\varnothing$, empty knot) crossing with the electron
($T_{2,3}$, trefoil) gives:

$$
  T_{\gamma e}(q)
  = 
  T_{\varnothing, T_{2,3}}(q)
$$

Since the empty knot has $J_{\varnothing}(q) = 1$:
$c_{\gamma e} = J_{T_{2,3}}(q) / J_{T_{2,3}}(q) = 1$ and
$d_{\gamma e} = 0$.  Therefore:

$$
  T_{\gamma e}(q) =  T_{pp}(q)
  = 
  \begin{pmatrix}
    q - q^{-1} & 1 \\
    1 & 0
  \end{pmatrix}
$$

**The photon-electron transfer matrix is the same as the
proton-proton matrix.**  This is because $J_{\varnothing}(q) = 1$
(trivial Jones polynomial of the empty knot), so the photon
contributes no deformation — the crossing is purely determined
by the electron.

### Shell transitions as R-I moves

Photon absorption promotes an electron from shell $n$ to
shell $n+1$.  In the transfer matrix language, this is a
**Reidemeister I move** on the electron-nucleus Hopf link:
a curl is added to the electron trefoil, changing its writhe
by $\pm 1$ but preserving its knot type.

The R-I move at the electron-nucleus junction:

$$
  \sigma_i \mapsto \sigma_i \cdot \sigma_n
$$

adds one transfer matrix factor $T_{\gamma e}$ to the chain
at generator $\sigma_i$.  The energy change is:

$$
  \Delta E_n
  = 
  \hat{V}_i^{(n+1)} - \hat{V}_i^{(n)}
  = 
  z \cdot (T_{\gamma e} \cdot M_i^{(n)})_{11}
  + (T_{\gamma e} \cdot M_i^{(n)})_{21}
  - \hat{V}_i^{(n)}
$$

For hydrogen ($A = 1$, single electron-proton junction):
the transfer matrix at shell $n$ is $T_{\gamma e}^n$ (the
$n$-th power).  The energy:

$$
  E_n  \propto  \hat{V}(T_{\gamma e}^n)
  = 
  z \cdot (T_{\gamma e}^n)_{11} + (T_{\gamma e}^n)_{21}
$$

Since $T_{\gamma e}$ has eigenvalues
$\lambda_{\pm} = \frac{1}{2}\bigl[(q - q^{-1}) \pm \sqrt{(q - q^{-1})^2 + 4}\bigr]$, the $n$-th power grows as
$\lambda_+^n$, and the energy scales as:

$$
  E_n  \propto  \lambda_+^n
$$

The **energy difference** between shells:

$$
  \Delta E_{n \to n+1}
  = 
  \hat{V}(T_{\gamma e}^{n+1}) - \hat{V}(T_{\gamma e}^n)
  = 
  \hat{V}(T_{\gamma e}^n) \cdot (\lambda_+ - 1)
$$

This gives the photon energy for shell transitions — a
geometric series in the eigenvalue $\lambda_+$ of the
photon-electron transfer matrix.

## Interaction as Δ operator

Any interaction that changes the crossing type from
$(K_1, K_2) \to (K_1', K_2')$ is encoded by the
**interaction operator**:

$$
  \Delta_{K_1 K_2 \to K_1' K_2'}(q)
  = 
  T_{K_1', K_2'}(q) - T_{K_1, K_2}(q)
$$

This is a 2$\times$2 matrix with polynomial entries in $q$.

| Interaction | $\Delta$ operator | Physical process |
|-------------|-------------------|------------------|
| $\beta^-$ decay | $\Delta_\beta = T_{\mathrm{mix}} - T_{nn}$ | $\mathfrak{d} \to \mathfrak{u}$ crossing change |
| $\beta^+$ decay | $-\Delta_\beta = T_{\mathrm{mix}} - T_{pp}$ | $\mathfrak{u} \to \mathfrak{d}$ crossing change |
| Photon absorption | $\Delta_\gamma = T_{\gamma e}$ (appended) | R-I move adds crossing |
| Pair creation | $\Delta_{\mathrm{pair}} = T_{ee} - T_{\gamma\gamma}$ | $\gamma \to e^+ e^-$ |

For beta decay, $\Delta_\beta$ is **universal**
([beta decay matrix](#prop:beta-decay-transfer-matrix)):
the same matrix for every nucleus.

For photon absorption, the operator is not a difference but
an **extension**: a new transfer matrix factor $T_{\gamma e}$
is appended to the chain, increasing the color degree by $1$.

## Composition rules

**Sequential interactions** (two interactions in sequence at
the same generator):

$$
  \Delta_{\mathrm{total}} = \Delta_2 \cdot T_{\mathrm{between}} \cdot \Delta_1
  + \Delta_1 + \Delta_2
$$

**Parallel interactions** (interactions at different generators):

$$
  \frac{P_{\mathrm{final}}}{P_{\mathrm{initial}}}
  = 
  \prod_{i \in \mathrm{affected}} \frac{\hat{V}_i^{\mathrm{final}}}{\hat{V}_i^{\mathrm{initial}}}
$$

The generators factorize — each affected generator contributes
independently to the Skein polynomial ratio.
<!-- FILE_END: transfer-matrix-operator-properties.md -->

<!-- FILE_START: transfer-matrix-identities.md -->
The three typed transfer matrices satisfy two exact
identities in $\mathrm{M}_2(\mathbb{Z}[q^{\pm 1}])$.

## Statement

**Proposition.**

**(i)** $T_{pp} \cdot T_{nn} = T_{nn} \cdot T_{pp} = I$.

**(ii)** $T_{pn}^2 = \dfrac{[2]_q^2}{4} \cdot I$, where
$[2]_q = q + q^{-1}$.
## Corollaries

**Nuclear binding from mixed crossings only.**
Identity (i) means that adjacent $pp$ and $nn$ crossings
cancel in the transfer matrix chain.  In the interleaved
ground-state ordering, $pp$ crossings (from proton-proton
pairs) and $nn$ crossings (from neutron-neutron pairs)
contribute zero net effect.  All nuclear binding energy
arises from the **mixed** ($pn$) crossings, whose transfer
matrix $T_{pn}$ has trace $0$ and determinant
$-(1 + h^2/4)$.

**Scalar pairing from mixed crossings.**
Identity (ii) means that every pair of mixed crossings
produces a **scalar** (proportional to $I$).  The binding
strength per pair is $[2]_q^2/4 = (q + q^{-1})^2/4$,
which is the square of half the quantum $2$-integer.
At $q_0$: $[2]_q^2/4 \approx 1.011$.
<!-- FILE_END: transfer-matrix-identities.md -->

<!-- FILE_START: skein-polynomial-transfer-matrix.md -->
The substrate parameter $q$ is the variable of the nuclear Skein
polynomial.  The transfer matrix product computes this polynomial
in factored form without expansion.

**Proposition.**
*Let $\mathcal{N}(Z, N)$ be a nucleus with $A = Z + N$ nucleons.
The Markov trace
([factorization theorem](#thm:markov-trace-factorization))*

$$
  P_{\mathcal{N}}(q)
   := 
  \mathrm{tr}_{\mathrm{Markov}}\!\bigl(
    \mathcal{N}(Z, N)
  \bigr)
  = 
  \prod_{i=0}^{A-2} \hat{V}_i(q)
$$

*is a polynomial in $q^{1/2}$ of degree $\leq A^2 - 1$.  Each
factor*

$$
  \hat{V}_i(q) =  z(q) \cdot a_i(q) + b_i(q)
$$

*is a rational function in $q^{1/2}$, where $a_i(q), b_i(q) \in \mathbb{Z}[q^{\pm 1}]$ are the transfer matrix coefficients at
generator $\sigma_i$ and $z(q) = 1/(q^{1/2} + q^{-1/2})$ is the
Markov parameter.  The product $P_{\mathcal{N}}(q)$ is the
**Skein polynomial of the nuclear link** in factored form.
It is computed by exactly $\binom{A}{2}$ transfer matrix
multiplications — one per nucleon pair.*

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: skein-polynomial-transfer-matrix.md -->

<!-- FILE_START: beta-decay-transfer-matrix.md -->
Beta decay is mediated by the $T_{3,5}$ torus knot with $10$
crossings ([beta decay](#def:beta-decay-skein)).  The $T_{3,5}$
insertion at the converting quark produces a **universal** 2$\times$2
matrix-valued polynomial $\Delta_\beta(q)$ that governs every
beta transition in every nucleus.  The transfer matrix captures
the effect of the $10$-crossing weak vertex on each nucleon pair.

## The three crossing transfer matrices

Each nucleon pair $(i, j)$ contributes a transfer matrix
$T(q) \in \mathrm{M}_2(\mathbb{Z}[q^{\pm 1}])$:

$$
  T(c, d) = 
  \begin{pmatrix}
    c(q - q^{-1}) + d & c \\
    c & d
  \end{pmatrix}
$$

with crossing coefficients $(c, d)$ depending on the pair type.
The $(1, -(q - q^{-1}))$ convention for nn crossings is the unique
convention consistent with the Hecke inverse relation
$\sigma^{-1} = \sigma - (q - q^{-1})$:

$$
  T_{pp}(q) =  T(1, 0) = 
  \begin{pmatrix}
    q - q^{-1} & 1 \\
    1 & 0
  \end{pmatrix},
  \quad
  T_{nn}(q) =  T(1, -(q - q^{-1})) = 
  \begin{pmatrix}
    0 & 1 \\
    1 & -(q - q^{-1})
  \end{pmatrix}
$$

$$
  T_{\mathrm{mix}}(q) =  T\!\left(1, -\tfrac{1}{2}(q - q^{-1})\right) = 
  \begin{pmatrix}
    \frac{1}{2}(q - q^{-1}) & 1 \\[4pt]
    1 & -\frac{1}{2}(q - q^{-1})
  \end{pmatrix}
$$

All three matrices live in $\mathrm{M}_2(\mathbb{Z}[q^{\pm 1}])$ —
no fractional powers of $q$ appear.  The pp and nn transfer matrices
are unimodular: $\det T_{pp} = \det T_{nn} = -1$ (forced by the
Hecke eigenvalues $q \cdot (-q^{-1}) = -1$).  The mixed crossing
$\frac{1}{2}(\sigma + \sigma^{-1})$ is an algebraic average, not a
group element, so $\det T_{\mathrm{mix}} \neq -1$.

## The universal beta decay matrix

**Proposition.**
*The two elementary decay matrices $\Delta_\beta^{nn \to \mathrm{mix}}$
and $\Delta_\beta^{\mathrm{mix} \to pp}$ are identical:*

$$
  \Delta_\beta^{nn \to \mathrm{mix}}(q)
  =  T_{\mathrm{mix}}(q) - T_{nn}(q)
  =  T_{pp}(q) - T_{\mathrm{mix}}(q)
  =  \Delta_\beta^{\mathrm{mix} \to pp}(q)
$$

*There is a single universal beta decay matrix:*

$$
  \boxed{
    \Delta_\beta(q)
    = 
    \tfrac{1}{2}(q - q^{-1}) \mathbb{I}
  }
$$

*where $\mathbb{I}$ is the $2 \times 2$ identity.
The decay matrix is a scalar multiple of the identity — beta decay
uniformly scales all channels by $\frac{1}{2}(q - q^{-1})$.*
<!-- FILE_END: beta-decay-transfer-matrix.md -->

<!-- FILE_START: ground-state-ordering.md -->
The nuclear ground state is the nucleon ordering that minimises
the quantum dilogarithm volume $\Phi_q = \sum_i \log|\hat{V}_i|$
of the transfer matrix chain.  The ordering is determined by
the **eigenvalue structure** of the three typed transfer matrices.

## Transfer matrix eigenvalues

The three transfer matrices
([transfer matrix](#prop:beta-decay-transfer-matrix)) have
eigenvalues determined by the typed crossing operators
([typed crossings](#def:typed-crossing-operator)):

See [Table 1](#tbl:ground-state-ordering-table1-data).

where $h = q - q^{-1}$.

**Key symmetry**: $T_{nn}$ is the $q \leftrightarrow q^{-1}$
mirror of $T_{pp}$.  Their eigenvalues are swapped:
$\lambda_\pm(T_{nn}) = \lambda_\mp(T_{pp})$.  The mixed matrix
$T_{pn}$ has **zero trace** and equal-magnitude eigenvalues
$\pm\sqrt{1 + h^2/4} \approx \pm 1.005$.

## Ground-state rule

**Proposition.**
*The nuclear ground state ordering for a nucleus with $Z$ protons
and $N$ neutrons ($A = Z + N$) is determined by:*

**(i) Interleaving.**  *Alternate protons and neutrons in adjacent
positions.  For $Z \leq N$: neutrons at even positions
($0, 2, 4, \ldots$), protons at odd positions
($1, 3, 5, \ldots$).*

**(ii) Tail packing.**  *Place excess neutrons ($N - Z$ of them)
at the highest positions ($2Z, 2Z+1, \ldots, A-1$), forming
$nn$ pairs at the high generators.*

**(iii) Boundary correction.**  *For small $A$ ($A \leq 3$), the
sorted ordering (all protons first) beats interleaving because
the chain is too short for the interleaved eigenvalue
cancellation to dominate.*

*Formally, for $Z \leq N$ and $A \geq 4$:*

$$
  \mathrm{ordering}[k]
  =
  \begin{cases}
    1 \text{ (proton)} & k \text{ odd}, \; k < 2Z \\
    0 \text{ (neutron)} & \text{otherwise}
  \end{cases}
$$

## Minimisation of $\Phi_q$ under interleaving

The vertex volume at generator $i$ is
$\hat{V}_i = z \cdot a_i + b_i$, where $(a_i, b_i)$ is the
chain-reduced transfer matrix state.  The chain at generator $i$
multiplies transfer matrices for all crossings with strands
$j > i$.

Each $T_{pp}$ contributes dominant eigenvalue $+q \approx 1.110$
(growth).  Each $T_{nn}$ contributes $+q^{-1} \approx 0.901$
(decay).  The interleaved arrangement alternates growth and
decay factors, producing destructive interference that drives
$|\hat{V}_i|$ below $1$ at most generators.

In contrast:
- **Sorted** (all protons first): generators $0, \ldots, Z-2$
  see only $T_{pp}$ crossings (pure growth), producing
  $|\hat{V}_i| > 1$ (no binding).  Generators $Z, \ldots, A-2$
  see only $T_{nn}$ (pure decay), but the accumulated growth
  from early generators limits the total binding.

- **Interleaved**: every generator sees a mix of $T_{pp}$, $T_{pn}$,
  $T_{nn}$ crossings.  The alternating $q$ and $q^{-1}$ eigenvalues
  cancel partially at each step, keeping $|\hat{V}_i|$ close to
  (and often below) $1$ throughout the chain.

The $T_{pn}$ matrix has zero trace, meaning its contributions
average to zero over many chain steps.  The interleaved
arrangement maximises the fraction of $T_{pn}$ crossings,
which act as **neutral spacers** between the binding $T_{nn}$
and anti-binding $T_{pp}$ contributions.

## Verified ground states

Exhaustive search over all $\binom{A}{Z}$ orderings confirms
the derived rule for $A \leq 14$:

See [Table 2](#tbl:ground-state-ordering-table2-data).

The sorted ordering (protons first) is optimal only for
$A \leq 3$, where the chain is too short for eigenvalue
cancellation to develop.  For $A \geq 4$, interleaving
dominates by factors of $2\text{--}10\times$ in $|\Phi_q|$.

## Connection to the Gram matrix

The transfer matrix eigenvalues are the Gram matrix entries
in disguise: $\lambda_+(T_{pp}) = q$ and $\lambda_+(T_{nn}) = q^{-1}$
are the braiding eigenvalues from the Hecke relation
$(T - q)(T + q^{-1}) = 0$.  The ground-state ordering maximises
the destructive interference between these eigenvalues,
which is equivalent to minimising the Frobenius norm
$\|\mathrm{NF}(\mathcal{N})\|_F$ of the nuclear configuration
in the Gram matrix inner product.

## Scalability

For $A > 14$, exhaustive search over $\binom{A}{Z}$ orderings is
infeasible.  The derived rule provides an $O(A)$ construction:
interleave protons at odd positions $1, 3, \ldots, 2Z-1$ and
pack excess neutrons at positions $2Z, \ldots, A-1$.  This
matches the exhaustive ground state for all verified cases
($A \leq 14$, except $A \leq 3$ where sorting wins).

For $A \leq 3$: use sorted (protons first).
For $A \geq 4$: use interleaved + tail packing.
<!-- FILE_END: ground-state-ordering.md -->

<!-- FILE_START: skein-generation.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
substrate parameter $q$ and Skein module
$\mathrm{Sk}_q = \mathrm{Sk}_q(\mathbf{C})$.
The Skein module $\mathrm{Sk}_q$ is generated as an
algebra by:

1. The fundamental (mass-zero) knot types $\{K_i\}_{i \in \mathcal{F}}$
   (torus knots), and
2. The Hopf link $\mathcal{L}_{\mathrm{Hopf}}$ (the binding operation).

Every hadron admits a terminal Skein resolution into a finite
polynomial in these generators with coefficients in
$\mathbb{Z}[q^{\pm 1}]$.
<!-- FILE_END: skein-generation.md -->

<!-- FILE_START: skein-mass-from-linking.md -->
**Lemma.**
*Evaluating the mass functional $\mathcal{M}$ on the terminal Skein
resolution of a hadron $H$ gives*

$$
  \mathcal{M}(H)
  = 
  Q(q) \cdot \mathcal{M}(\mathcal{L}_{\mathrm{Hopf}})
  +
  \sum_{i=1}^{n}
  \frac{\mathrm{Vol}(K_i)}{\hbar_q^{2}},
$$

*where the first term is the binding energy from linking and the
second is the constituent mass (zero for torus-knot constituents),
$Q(q) \in \mathbb{Z}[q^{\pm 1}]$ is the Skein polynomial of the
linking configuration, and $\hbar_q = 1 - q^{-1}$.*
<!-- FILE_END: skein-mass-from-linking.md -->

