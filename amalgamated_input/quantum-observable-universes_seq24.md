<!-- FILE_START: intro-q-special-functions.md -->
Having developed the $q$-resolvent and the Wick rotation in the
previous section, we now identify the three categorical special
functions that pair with the resolvent under the
$\exp_q$-grouplike pairing: the $q$-exponential
$\exp_q \in G(\mathcal{H}_q)$, its primitive inverse $\log_q$, and the
level-2 iterated primitive $\mathrm{Li}_2^q$.  Each is defined
Hopf-algebraically — as the unique grouplike or primitive solving
a shuffle-coalgebra equation in $\mathcal{H}_q$ — rather than by a power
series, so the definitions extend beyond the archimedean limit.

The section is organised in three parallel arcs.  For each special
function we record (i) the existence and uniqueness of the
Hopf-algebraic characterisation, then (ii) two specialisation
remarks — a finite-field obstruction (the Taylor representation
fails when the Jackson factorial $[n]_q!$ vanishes modulo $p$) and
a $p$-adic refinement (the obstruction selects a canonical
$p$-adic grouplike, distinct from the archimedean one).  The three
functions are introduced bottom-up: $\exp_q$ first (as the
grouplike), then $\log_q$ (the inverse), then $\mathrm{Li}_2^q$
(the iterated primitive).

The output of this section is the trio
$(\exp_q, \log_q, \mathrm{Li}_2^q)$ as morphisms in
$\mathrm{End}_{\mathbf{C}}(A)$.  These three are the substrate-level
seeds of the formal-group law that governs the chapter on
$q$-geometric Langlands: the dilogarithm in particular furnishes
the depth-2 modular cocycle that the Langlands chapter pulls back
along the Tannaka–Krein equivalence.  Readers focused on the
substrate-level statements can take the proofs on first reading;
the archimedean / $p$-adic specialisations are deferred to the
Descartes universe.
<!-- FILE_END: intro-q-special-functions.md -->

<!-- FILE_START: q-exponential.md -->
Let $\mathcal{H}_q$ be the $q$-shuffle Hopf algebra of a quantum observable
universe with coproduct $\Delta_q$, counit $\epsilon$, antipode $S_q$,
and $q$-Jackson derivative $D_q$.  A *grouplike* of $\mathcal{H}_q$ is an
element $g \in \mathcal{H}_q$ satisfying

$$
  \Delta_q(g) = g \otimes g,
  \qquad
  \epsilon(g) = 1.
$$

Grouplikes form a group $G(\mathcal{H}_q) \subseteq \mathcal{H}_q$ under multiplication:
they are the characters of the coalgebra structure.

**$q$-Exponential.**  The *$q$-exponential* is the unique grouplike
$\exp_q \in G(\mathcal{H}_q)$ satisfying the categorical flow equation

$$
  D_q  \exp_q  =  \exp_q,
  \qquad
  \exp_q(0) = 1.
$$

Equivalently, $\exp_q$ is the unique element of $\mathcal{H}_q$ with
$\mathcal{L}_q^{-1}[(1 - s)_q^{-1}] = \exp_q$, where $\mathcal{L}_q$ is
the categorical Laplace transform
([categorical Laplace transform](#def:categorical-laplace)).
<!-- FILE_END: q-exponential.md -->

<!-- FILE_START: q-exponential-realisations.md -->
**Universal property.**  $\exp_q$ is the *free grouplike* on one
primitive generator $x$ (the infinitesimal of the Reeb flow
$\phi_t^q$).  Any :refterm[monoidal functor]{#monoidal-functor}
$\Phi \colon (\mathrm{End}_{\mathbf{C}}(A), \ast_q) \to (\mathrm{End}_{\mathbf{C}}(A), \cdot)$
that intertwines convolution with product is determined by its value
$\Phi(x)$; the diagonal $\Phi(\exp_q) = \Phi(x) \otimes \Phi(x)$ enforces
grouplike-ness functorially.

```tex
\begin{equation}\label{eq:q-exp-universal}
\begin{tikzcd}[row sep=2.5em, column sep=3.5em]
  x
    \ar[r, "D_q"]
    \ar[d, dashed, "!\,\Phi"']
  & \exp_q
    \ar[r, "\Delta_q"]
    \ar[d, dashed, "!\,\Phi"]
  & \exp_q \otimes \exp_q
    \ar[d, dashed, "!\,\Phi \otimes \Phi"]
  \\
  \Phi(x)
    \ar[r, "D_q"']
  & \Phi(\exp_q)
    \ar[r, "\Delta_q"']
  & \Phi(\exp_q) \otimes \Phi(\exp_q)
\end{tikzcd}
\end{equation}
```

**Base-ring independence.**  Because this definition characterises
$\exp_q$ by a purely Hopf-algebraic universal property — *grouplike* +
*flow-invariant* — it makes sense in any base ring $R$ where $\mathcal{H}_q$
admits a grouplike.  In particular $\exp_q$ exists abstractly over
$\mathbb{F}_p$, $\mathbb{Q}_p$, and $\mathbb{Z}[q, q^{-1}]$ as an
element of the formal Hopf algebra, independently of any convergent
power-series representation
([finite-field obstruction for $\exp_q$](#rem:q-exp-finite-field-obstruction)).

**Native algebraic home: the Habiro ring.**  The Taylor coefficients
of $\exp_q$ are rational functions of $q$ whose denominators are
products of $[n]_q$ — i.e. cyclotomic factors. The partial sums are
therefore coherent modulo the Habiro ideal $((q;q)_m)$, and $\exp_q$
acts as a grouplike in the formal-power-series ring
$\widehat{\mathbb{Z}[q]}[\![x]\!]$ over the Habiro ring
([Habiro ring](#def:habiro-ring)). Evaluation at any root of unity
$\zeta_n$ is the cyclotomic-projection
$\widehat{\mathbb{Z}[q]} \to \mathbb{Z}[q]/\Phi_n(q)$ — purely
algebraic, no analytic continuation required.

**Archimedean realisation.**  Over $\mathbb{C}$ (or any field of
characteristic zero where the Jackson factorials $[n]_q!$ are
invertible), $\exp_q$ is represented by a convergent Taylor series
([Taylor series of $\exp_q$](#prop:q-exponential-taylor)).  This is an
*additional* fact about the $\mathbb{C}$-realisation of the abstract
grouplike — not its defining property.

**Physical meaning.**  $\exp_q$ is the *categorical generator of the
Reeb flow*: the unique Hopf-algebra element whose action on the
substrate coordinate $Z$ produces the $q$-deformed rotation
$\mathcal{L}_\xi Z = J\hbar_q Z$
([substrate radial coordinate](#prop:substrate-radial-coordinate)).
The Planck step $t_P(q) = q/(q-1)$ is one full $\exp_q$-orbit.
<!-- FILE_END: q-exponential-realisations.md -->

<!-- FILE_START: q-exponential-exists.md -->
Let $\mathcal{H}_q$ be the $q$-shuffle Hopf algebra
([$q$-exponential](#def:q-exponential)) over a base ring $R$ in which
the Jackson integers $[n]_q = (1 - q^n)/(1 - q)$ are invertible for
all $n \ge 1$.  Then there exists a grouplike
$\exp_q \in G(\mathcal{H}_q)$ satisfying the flow equation

$$
  D_q \exp_q \;=\; \exp_q,
  \qquad
  \epsilon(\exp_q) \;=\; 1.
$$

Uniqueness is ([uniqueness of $\exp_q$](#prop:q-exponential-unique)).
<!-- FILE_END: q-exponential-exists.md -->

<!-- FILE_START: q-exponential-unique.md -->
Any two grouplikes $e_1, e_2 \in G(\mathcal{H}_q)$ satisfying
$D_q e_i = e_i$ and $\epsilon(e_i) = 1$ coincide:

$$
  e_1 \;=\; e_2.
$$
<!-- FILE_END: q-exponential-unique.md -->

<!-- FILE_START: q-exp-finite-field-obstruction.md -->
The categorical $q$-exponential ([$q$-exponential](#def:q-exponential))
is defined purely Hopf-algebraically: $\exp_q$ is the unique grouplike
of $\mathcal{H}_q$ satisfying $D_q \exp_q = \exp_q$.  This characterisation is
base-ring independent.  Its archimedean realisation as the Taylor series

$$
  \exp_q(x) \;=\; \sum_{n \ge 0} \frac{x^n}{[n]_q!}
$$

([Taylor series of $\exp_q$](#prop:q-exponential-taylor)) is,
however, an *archimedean-only* statement.  The series representation
*fails* over a field of characteristic $p$ whenever the Jackson
factorial $[n]_q!$ vanishes modulo $p$.

**Location of the vanishing.**  The Jackson integer
$[n]_q = (1 - q^n)/(1 - q)$ vanishes in $\mathbb{F}_p$ precisely when
$q^n = 1$ in $\mathbb{F}_p^\times$ — i.e.\ when the multiplicative
order $\mathrm{ord}_{\mathbb{F}_p^\times}(q)$ divides $n$.  Thus
$[n]_q! = 0$ for every $n$ at least equal to that order, and the
formal series $\sum x^n / [n]_q!$ has divisions by zero starting at
degree $\mathrm{ord}_{\mathbb{F}_p^\times}(q)$.

**Surviving abstract structure.**  The grouplike $\exp_q$ nonetheless
*exists* in the formal Hopf algebra $\mathcal{H}_q \otimes \mathbb{F}_p$:
one can define $\exp_q$ as a *symbol* (a formal grouplike, adjoined
to the Hopf algebra), characterised by its coproduct
$\Delta_q(\exp_q) = \exp_q \otimes \exp_q$ and the flow equation
$D_q \exp_q = \exp_q$, without attempting to evaluate it at specific
arguments.  This is analogous to the formal group law: the group
$\widehat{\mathbb{G}_a}$ is defined in any characteristic, even
though the exponential $\exp \colon \widehat{\mathbb{G}_a} \to \widehat{\mathbb{G}_m}$
is not realisable as a power series in characteristic $p$.

**Truncated $p$-exponential.**  A partial substitute over
$\mathbb{F}_p$ is the truncated series

$$
  \exp_q^{(p)}(x) \;=\; \sum_{n = 0}^{p - 1} \frac{x^n}{[n]_q!},
$$

well-defined whenever $[n]_q \ne 0$ for $1 \le n \le p - 1$.  This is
a polynomial, not a grouplike of the full Hopf algebra — but it
*becomes* grouplike modulo the relation $x^p = 0$ (or the
$\mathbb{F}_p$-Frobenius twist).  Geometrically: the $p$-truncated
$\exp_q$ lives on the first-order infinitesimal neighbourhood of
the identity in $G(\mathcal{H}_q)$.

**Witt-vector lift.**  The truncated $\mathbb{F}_p$-exponential lifts
uniquely to a convergent grouplike on $\mathbb{Q}_p$ and $\mathbb{C}_p$
when $q$ is $p$-adically close to $1$ — see
[$p$-adic realisations of $\exp_q$](#rem:q-exp-p-adic) for the
convergence radii and the $q$-analogue of the Artin--Hasse
exponential.

**Conclusion.**  $\exp_q$ is archimedean in its *series representation*,
but base-ring independent in its *Hopf-algebraic content*.  The same
applies to $\log_q$ ([$q$-logarithm](#def:q-logarithm)) and
$\mathrm{Li}_2^q$ ([$q$-dilogarithm](#def:q-dilogarithm)): the
categorical structures survive in characteristic $p$; only their
power-series avatars fail.
<!-- FILE_END: q-exp-finite-field-obstruction.md -->

<!-- FILE_START: q-exp-p-adic.md -->
The formal grouplike $\exp_q \in G(\mathcal{H}_q)$
([$q$-exponential](#def:q-exponential)) admits convergent
power-series realisations over the $p$-adic fields $\mathbb{Q}_p$ and
$\mathbb{C}_p$, recovering the archimedean Taylor series
([Taylor series of $\exp_q$](#prop:q-exponential-taylor)) as an
ultrametric series once the divisibility obstruction over
$\mathbb{F}_p$ ([finite-field
obstruction](#rem:q-exp-finite-field-obstruction)) is controlled by
requiring $q$ sufficiently close to $1$ in the $p$-adic metric.

**Setup.**  Let $v_p \colon \mathbb{C}_p^\times \to \mathbb{Q}$ be the
$p$-adic valuation normalised by $v_p(p) = 1$, and write
$|x|_p = p^{-v_p(x)}$.  A formal series
$\sum a_n x^n \in \mathbb{Q}_p[\![x]\!]$ converges at $x \in \mathbb{C}_p$
iff $v_p(a_n x^n) \to \infty$, i.e. iff
$v_p(a_n)/n + v_p(x) \to \infty$.

**Jackson factorial valuation.**  Assume $q \in 1 + p\mathbb{Z}_p$, so
$v_p(q - 1) = e \ge 1$.  Then $q$ has multiplicative order $p^k$ in
$(\mathbb{Z}/p^{k+e}\mathbb{Z})^\times$ for every $k \ge 0$, and

$$
  v_p\bigl([n]_q\bigr)
  \;=\;
  v_p\!\left(\frac{q^n - 1}{q - 1}\right)
  \;=\;
  v_p(n)
  \qquad
  \text{for } q \in 1 + p\mathbb{Z}_p, \; p \ne 2.
$$

(At $p = 2$ the identity $v_2([n]_q) = v_2(n) + O(1)$ holds with a
small correction.)  Consequently the Jackson factorial satisfies

$$
  v_p\bigl([n]_q!\bigr)
  \;=\;
  \sum_{k=1}^{n} v_p([k]_q)
  \;=\;
  v_p(n!)
  \;=\;
  \frac{n - s_p(n)}{p - 1},
$$

where $s_p(n)$ is the sum of base-$p$ digits of $n$ (Legendre's
formula).  The $q$-deformation therefore does **not** change the
$p$-adic growth of denominators relative to the classical exponential:
$v_p([n]_q!) = v_p(n!)$.

**Convergence on $\mathbb{Q}_p$.**  For $q \in 1 + p\mathbb{Z}_p$ and
$x \in \mathbb{Q}_p$ with $v_p(x) \ge 1$ (i.e. $x \in p\mathbb{Z}_p$),
the Taylor series

$$
  \exp_q(x) \;=\; \sum_{n \ge 0} \frac{x^n}{[n]_q!}
$$

converges in $\mathbb{Q}_p$ because
$v_p(x^n/[n]_q!) \ge n - (n - s_p(n))/(p-1) \to \infty$.  The limit is a
grouplike of $\mathcal{H}_q \otimes \mathbb{Q}_p$ and agrees, under the reduction
$\mathbb{Z}_p \twoheadrightarrow \mathbb{F}_p$, with the truncated
exponential $\exp_q^{(p)}$ of the finite-field remark.  Equivalently,
the $p$-adic $\exp_q$ is the **Witt-vector lift** of the
$\mathbb{F}_p$-truncated polynomial: the unique continuous grouplike on
$p\mathbb{Z}_p$ whose reduction mod $p$ is $\exp_q^{(p)}$ modulo
$x^p = 0$.

**Convergence on $\mathbb{C}_p$.**  Over $\mathbb{C}_p$ (the completion
of $\overline{\mathbb{Q}_p}$), the radius of convergence widens to
include fractional valuations but remains strictly smaller than the
naive archimedean disc.  The series converges for all $x \in \mathbb{C}_p$
with

$$
  v_p(x) \;>\; \frac{1}{p - 1},
$$

matching the classical $p$-adic exponential's radius
$|x|_p < p^{-1/(p-1)}$.  Since $v_p([n]_q!) = v_p(n!)$, the radius is
**identical** to the classical $\exp$ radius — the $q$-deformation
does not shrink the disc.  At the boundary $v_p(x) = 1/(p-1)$ the
series diverges (same as classical $\exp$), and the grouplike $\exp_q$
does not extend continuously beyond this disc.

**$q$-deformation of the Dwork/Artin--Hasse exponentials.**  Just as
the classical Artin--Hasse exponential
$E_p(x) = \exp\bigl(\sum_{k \ge 0} x^{p^k}/p^k\bigr)$ extends the $p$-adic
$\exp$ to $x \in \mathbb{Z}_p$ by absorbing denominators through
Frobenius, a $q$-analogue

$$
  E_p^q(x)
  \;=\;
  \exp_q\!\left(\sum_{k \ge 0} \frac{x^{p^k}}{[p^k]_q}\right)
$$

converges on the unit disc $v_p(x) \ge 0$ provided $v_p(q - 1) \ge 1$.
This is the categorical avatar of the Artin--Hasse construction and
plays the role, in the $q$-deformed story, of the Frobenius-stable
formal group law underlying Dwork's theory of exponential sums.  See
the Witt-vector lift remark
([Witt vector lift](#rem:witt-lift-qou)) for the functorial formulation.

**Comparison table.**

See [Table](#tbl:q-exp-p-adic-table-data).

**Moral.**  The grouplike $\exp_q$ is *always* present as a formal
Hopf-algebraic object; what varies between base rings is the domain of
*evaluation*.  The $p$-adic side gives a convergent realisation whenever
$q$ is $p$-adically close to $1$ — matching the heuristic that the
substrate parameter "deforms" the classical exponential without
changing its $p$-adic growth profile.
<!-- FILE_END: q-exp-p-adic.md -->

<!-- FILE_START: q-logarithm.md -->
Dual to the $q$-exponential ([$q$-exponential](#def:q-exponential))
is its categorical inverse.  A *primitive* of the $q$-shuffle Hopf
algebra $\mathcal{H}_q$ is an element $p$ satisfying

$$
  \Delta_q(p) = p \otimes 1 + 1 \otimes p,
  \qquad
  \epsilon(p) = 0.
$$

Primitives form a Lie algebra $\mathrm{Prim}(\mathcal{H}_q) \subseteq \mathcal{H}_q$ under
the $q$-commutator, and they are exactly the *infinitesimal* data of
grouplikes: the Milnor--Moore theorem identifies $\mathrm{Prim}(\mathcal{H}_q)$
with the tangent space at $1 \in G(\mathcal{H}_q)$.

**$q$-Logarithm.**  The **$q$-logarithm** is the unique primitive
$\log_q \in \mathrm{Prim}(\mathcal{H}_q)$ such that

$$
  \log_q \circ \exp_q \;=\; \mathrm{id}
  \qquad\text{(in the formal-power-series PROP).}
$$

Equivalently, $\log_q$ and $\exp_q$ form an *adjoint pair*

$$
  \log_q \;\dashv\; \exp_q
  \qquad
  \bigl(\mathrm{Prim}(\mathcal{H}_q), [\cdot,\cdot]_q\bigr)
  \;\rightleftarrows\;
  \bigl(G(\mathcal{H}_q), \cdot\bigr)
$$

between the Lie algebra of primitives and the group of grouplikes.
This is the Hopf-algebraic shadow of the Lie-theoretic exponential
$\mathfrak{g} \to G$.

```tex
\begin{equation}\label{eq:q-log-adjunction}
\begin{tikzcd}[row sep=2.5em, column sep=4em]
  \mathrm{Prim}(\mathcal{H}_q)
    \ar[r, bend left=15, "\exp_q"]
    \ar[r, phantom, "\dashv"]
  & G(\mathcal{H}_q)
    \ar[l, bend left=15, "\log_q"]
\end{tikzcd}
\end{equation}
```

**Universal property.**  $\log_q$ is the left adjoint of the
functor *grouplike-of* from primitives to grouplikes.  For any
Hopf-algebra morphism $\Phi \colon \mathcal{H}_q \to K$ sending grouplikes to
grouplikes and primitives to primitives,

$$
  \Phi(\log_q g) \;=\; \log_K \Phi(g)
  \qquad\forall  g \in G(\mathcal{H}_q),
$$

so $\log_q$ is *natural* in the Hopf algebra.
<!-- FILE_END: q-logarithm.md -->

<!-- FILE_START: q-logarithm-properties.md -->
This remark collects the base-ring, three-context, Habiro,
archimedean, and physical realisations of the
[$q$-logarithm](#def:q-logarithm).

**Base-ring independence.**  The adjoint pair $(\log_q, \exp_q)$ lives
in the universal setting of Hopf algebras — no convergence is
required.  Over $\mathbb{F}_p$ the $\log_q$ of a grouplike is still
a well-defined primitive, even when the series representation fails
([finite-field obstruction](#rem:q-exp-finite-field-obstruction)).

**Three-context behaviour.**  Mirroring $\exp_q$
([$p$-adic $\exp_q$](#rem:q-exp-p-adic)):

- **$\mathbb{F}_p$.**  The series $\log_q(1 + x) = \sum (-1)^{n-1} x^n / [n]_q$
  has zero denominators whenever $[n]_q$ vanishes in $\mathbb{F}_p$
  (i.e. $n \ge \mathrm{ord}_{\mathbb{F}_p^\times}(q)$).  The truncation
  $\log_q^{(p)}(1+x) = \sum_{n=1}^{p-1} (-1)^{n-1} x^n / [n]_q$ becomes
  primitive modulo $x^p = 0$ and inverts $\exp_q^{(p)}$ on the first
  infinitesimal neighbourhood of $1$.
- **$\mathbb{Q}_p$.**  For $q \in 1 + p\mathbb{Z}_p$ the series
  converges on $1 + p\mathbb{Z}_p$ because $v_p([n]_q) = v_p(n)$ and
  the denominators grow no faster than the classical $p$-adic
  $\log$; the result is a continuous primitive $p\mathbb{Z}_p \to p\mathbb{Z}_p$
  inverting the Witt-vector $\exp_q$.
- **$\mathbb{C}_p$.**  Converges on $v_p(x) > 0$ (the open unit disc
  around $1$, i.e. $|1 + x - 1|_p < 1$), matching the classical $p$-adic
  $\log$ radius.  The logarithm extends by Iwasawa's convention to all
  of $\mathbb{C}_p^\times$ via $\log_q(p) = 0$ if one wants a global
  branch.

**Native algebraic home: the Habiro ring.**  The series
representation $\log_q(1 + x) = \sum_{n \geq 1} (-1)^{n-1} x^n/[n]_q$
has cyclotomic denominators $[n]_q$, so its partial sums are
coherent modulo the Habiro ideal $((q;q)_m)$. Equivalently, the
adjoint pair $(\log_q, \exp_q)$ acts on the formal-power-series
ring $\widehat{\mathbb{Z}[q]}[\![x]\!]$ over the Habiro ring
([Habiro ring](#def:habiro-ring)). Cyclotomic-projection
$\widehat{\mathbb{Z}[q]} \to \mathbb{Z}[q]/\Phi_N(q)$ at the
$N$-th finite place sends $\log_q$ to its level-$N$ truncation,
giving evaluation at any root of unity without invoking
$\mathbb{C}$ or analytic continuation.

**Archimedean realisation.**  Over $\mathbb{C}$ the adjoint pair
$(\log_q, \exp_q)$ is represented by the convergent series

$$
  \log_q(1 + x) \;=\; \sum_{n \ge 1} \frac{(-1)^{n-1}  x^n}{[n]_q}
$$

(a corollary of the Taylor expansion of $\exp_q$; cf.
[Taylor series of $\exp_q$](#prop:q-exponential-taylor)).

**Physical meaning.**  The Reeb-flow holonomy between two substrate
slices $q_1 < q_2$ is a grouplike element; its $q$-logarithm is the
infinitesimal generator of the flow on $\mathrm{Prim}(\mathcal{H}_q)$.  Hence
$\log_q$ measures *cosmological displacement* in Hopf-algebraic
units — the analogue of a "time rapidity" on the substrate side.
<!-- FILE_END: q-logarithm-properties.md -->

<!-- FILE_START: q-logarithm-exists.md -->
Under the hypotheses of ([existence of
$\exp_q$](#prop:q-exponential-exists)) — $\mathcal{H}_q$ the $q$-shuffle
Hopf algebra over a base ring $R$ with invertible Jackson factorials —
there exists a primitive element
$\log_q \in \mathrm{Prim}(\mathcal{H}_q)$ satisfying

$$
  D_q  \exp_q(\log_q) \;=\; \exp_q(\log_q),
  \qquad
  \log_q \circ \exp_q \;=\; \mathrm{id}_{\mathrm{Prim}(\mathcal{H}_q)}.
$$

Uniqueness is ([uniqueness of $\log_q$](#prop:q-logarithm-unique)).
<!-- FILE_END: q-logarithm-exists.md -->

<!-- FILE_START: q-logarithm-unique.md -->
Any two primitives $\ell_1, \ell_2 \in \mathrm{Prim}(\mathcal{H}_q)$
satisfying $\exp_q(\ell_i) = g$ for the same grouplike
$g \in G(\mathcal{H}_q)$ and $\epsilon(\ell_i) = 0$ coincide:

$$
  \ell_1 \;=\; \ell_2.
$$
<!-- FILE_END: q-logarithm-unique.md -->

