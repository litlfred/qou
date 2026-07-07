<!-- FILE_START: substrate-parameter-intro.md -->
This section promotes the substrate parameter $q$ from an
algebraic device to a structural ingredient of the categorical
deformation, and records the elementary identities the parameter
must satisfy.  The arc proceeds from the quantum-universe
explication (substrate-flow on the QU axioms), through the
existence-uniqueness $\mathbb{G}_m$-family of differentials, to
the substrate categorical action that records the parameter's
behaviour under the fibre functor.

The middle blocks exhibit the deformation of $\mathrm{SU}(2)$ to
$\mathrm{SU}_q(2)$ and the categorical dimension formula
$\dim_q V = [2]_q = q + q^{-1}$ that the chapter cycle relies on
throughout.  The closing blocks specialise the substrate
parameter to its substrate-numerical value
$q_0 \approx 1.1097$ (delayed until the physical-observation
chapter) and tabulate the substrate-parametrised analogues of
classical objects: $c_q$, $\hbar_q$, $d_H(q)$.

A note on scope: the substrate parameter is the single
deformation knob that controls every chapter that follows.
Readers focused on substrate-level statements need only the
algebraic identities here; the archimedean numerical
specialisation is deferred to Chapter 7.
<!-- FILE_END: substrate-parameter-intro.md -->

<!-- FILE_START: quantum-universe-explication.md -->
The substrate parameter $q \in \mathrm{End}(\mathbf{1})$ is not part
of the categorical definition of a quantum universe or observable
universe; it parametrises the $\mathbb{G}_m$-family of interpolations
between the full differential $d$ and the vertical projection
$\pi_V \circ d$ ([substrate parameter](#def:substrate-parameter)).
The triple $(\mathbf{C}, A, \tau)$ carries both endomorphisms
canonically; $q$ records *where one sits* in the
$\mathbb{G}_m$-family they span.  Once a substrate parameter is
fixed, the categorical dimension of the fundamental object $V$
deforms from $2$ to $[2]_q = q + q^{-1}$, and the gauge group
$G = \mathrm{Aut}^{\otimes}(\tau)$
([$\mathrm{SU}(2)$ emergence](#thm:su2-emergence)) deforms from $\mathrm{SU}(2)$
to $\mathrm{SU}_q(2)$.

The section proceeds in three layers.  We first promote the
substrate parameter from an algebraic device to a structural
ingredient: existence and uniqueness of the $\mathbb{G}_m$-family,
the substrate categorical action that records the parameter's
behaviour under the fibre functor, and the gauge-group deformation
$\mathrm{SU}(2) \to \mathrm{SU}_q(2)$.  We then exhibit the
substrate parameter's elementary identities — the
$q$-commutators, the deformation of the Reeb derivation, and the
classical-limit obstruction that controls $q \to 1$.  Finally we
introduce the *algebraic substrate* (Reeb action on the universal
enveloping algebra of $\mathfrak{su}_q(2)$), which is the home for
the substrate-level computations in the next section.

The output of this section is the substrate parameter $q$ as an
explicit endomorphism of $\mathbf{1}$ in $\mathbf{C}$, together
with its action on every categorical structure introduced so far.
Every chapter that follows is parametrised by $q$ — the
substrate-numerical value $q_0 \approx 1.1097$ is fixed only in
the physical-observation chapter.
<!-- FILE_END: quantum-universe-explication.md -->

<!-- FILE_START: braiding-eigenvalue-extraction.md -->
Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)) with
fundamental object $V$ of rank $2$ and braiding
$c_{V,V} \colon V \otimes V \to V \otimes V$.  Then:

1. **Spectral decomposition.** The tensor square decomposes
   as $V \otimes V = S^2 V \oplus \Lambda^2 V$, where $S^2 V$
   (symmetric) and $\Lambda^2 V$ (antisymmetric) are the eigenspaces
   of $c_{V,V}$.  This decomposition is *intrinsic* to $\mathbf{C}$
   — it depends only on the braiding, not on any external parameter.

2. **Eigenvalue definition of $q$.** Since $\Lambda^2 V \cong \mathbf{1}$
   ([volume constraint](#eq:categorical-volume-constraint)) is simple,
   $c_{V,V}$ acts on it by a scalar
   $\lambda_- \in \mathrm{End}(\mathbf{1}) \cong k$.  Similarly,
   $c_{V,V}$ acts on the $3$-dimensional $S^2 V$ by a scalar
   $\lambda_+$.  Define

   $$
     q  :=  \lambda_+,
     \qquad
     \lambda_- =  -q^{-1}.
   $$

   This is a *categorical invariant*: it is determined by the
   braiding endomorphism of $\mathbf{C}$ alone.

3. **Hecke relation.** The eigenvalue pair $(\lambda_+, \lambda_-) = (q, -q^{-1})$ is equivalent to the Hecke relation on
   $T = \tau(c_{V,V})$:

   $$
     (T - q)(T + q^{-1}) =  0,
   $$

   and the product $\lambda_+ \cdot \lambda_- = -1$ (which follows
   from $\det(c_{V,V}) = -1$ on a rank-$2$ object with trivial
   determinant).  The Hecke relation is intrinsic: it is a
   polynomial identity on the braiding morphism in $\mathbf{C}$.

4. **Classical vs.\ quantum.** When $c_{V,V}^2 = \mathrm{id}$,
   the eigenvalues are $+1$ and $-1$, giving $q = 1$ (symmetric
   monoidal, classical). When $c_{V,V}^2 \neq \mathrm{id}$,
   $q \neq 1$ and the category is genuinely braided — this is
   the quantum regime.

5. **Connection to the substrate parameter.** The categorical
   $q$ extracted here coincides with the
   ([substrate parameter](#def:substrate-parameter)): the
   one-parameter family $d_q = q^{-1} d + (1 - q^{-1}) \pi_V \circ d$
   is parametrised by the *same* $q \in \mathrm{End}(\mathbf{1})$
   that appears as the braiding eigenvalue.  The braiding determines
   the differential geometry.
<!-- FILE_END: braiding-eigenvalue-extraction.md -->

<!-- FILE_START: braiding-eigenvalue-extraction-novelty.md -->
The deformation parameter $q$ is not imposed externally.
It is the eigenvalue of the braiding $c_{V,V}$ on the symmetric
summand of $V \otimes V$ — a purely categorical datum, extracted from
the monoidal structure of $\mathbf{C}$ via the Hecke relation.
The Tannaka--Krein reconstruction
([reconstruction](#prop:tannaka-krein-reconstruction)) then recovers the
quantum group $\mathrm{SU}_q(2)$ as $\mathrm{End}^{\otimes}(\tau)$,
with $q$ already determined by the category.

While using the Hecke relation and determinant constraint to relate braiding eigenvalues is standard algebraic manipulation (e.g., following Kassel), the mathematical novelty here is treating this extraction not as a definition of $q$, but as a rigorous proof that the macroscopic substrate parameter governing the fluid PDE is precisely and completely constrained by the microscopic categorical braiding of the observable universe.
<!-- FILE_END: braiding-eigenvalue-extraction-novelty.md -->

<!-- FILE_START: spectral-chart-correspondence.md -->
Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)).  The
Hecke spectral decomposition

$$
  V \otimes V  =  S^2 V \oplus \Lambda^2 V,
  \qquad
  c_{V,V}|_{S^2 V} = \lambda_+ = q,
  \quad
  c_{V,V}|_{\Lambda^2 V} = \lambda_- = -q^{-1},
$$

of ([braiding eigenvalue extraction](#prop:braiding-eigenvalue-extraction))
realises geometrically as the chart-glue datum of the quantum projective
line ([projective line object](#def:projective-line-object)).  On the two
affine charts $U_0, U_1$ of
([contact affine chart](#def:contact-affine-chart)) the chart-transition
coefficient $\kappa$ in $z\,w = \kappa$ is fixed by the spectral data:

$$
  \kappa  =  \lambda_+^{-1}  =  -\lambda_-  =  q^{-1}.
$$

Two readings of the same equality:

1. *Glue from the antisymmetric line.*  The Hecke determinant constraint
   $\lambda_+ \lambda_- = -1$ from
   ([braiding eigenvalue extraction](#prop:braiding-eigenvalue-extraction))
   is an eigenvalue identity on $\Lambda^2 V \cong \mathbf{1}$.  Because
   $\Lambda^2 V$ is the unit summand, that scalar identity is precisely
   the chart-glue datum on $\mathbb{P}_q(V)$ — no extra freedom remains.

2. *Classical degeneration.*  At $q = 1$ the eigenvalues collapse to
   $(+1, -1)$, the chart transition becomes the classical inversion
   $z\,w = 1$, and the projective line is the symmetric-monoidal
   $\mathbb{P}(V)$ of ([commutative QOU](#def:commutative-qou)).

The spectral and the geometric extractions of $q$ are therefore the same
datum read twice: eigenvalues of $c_{V,V}$ on $V \otimes V$, and
chart-transition data on $\mathbb{P}_q(V)$.  The explicit
$z\,w = q^{-1}$ presentation in coordinates $z = y x^{-1}$, $w = x y^{-1}$
on the quantum plane is worked out in
([affine-chart origin of $i$ and $q$](#rem:affine-chart-origin-of-i-and-q)).
<!-- FILE_END: spectral-chart-correspondence.md -->

<!-- FILE_START: tannaka-krein-reconstruction.md -->
Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)) with
fibre functor $\tau \colon \mathbf{C} \to R\text{-}\mathrm{Mod}$.
Then the coend

$$
  H =  \mathrm{End}^{\otimes}(\tau)
  =  \int^{X \in \mathbf{C}}
  \tau(X)^{\vee} \otimes_R \tau(X)
$$

carries a canonical Hopf algebra structure
$(\mu, \eta, \Delta, \varepsilon, S)$ such that:

1. **Reconstruction.** There is a monoidal equivalence
   $\mathbf{C} \simeq \mathrm{Rep}(H)$ under which $\tau$
   corresponds to the forgetful functor
   $U \colon \mathrm{Rep}(H) \to R\text{-}\mathrm{Mod}$.

2. **Universal property.** $H$ is the *universal* Hopf algebra
   through which $\tau$ factors: for every Hopf algebra $H'$ and
   monoidal natural transformation
   $\alpha \colon \tau \Rightarrow U \circ F$ (where
   $F \colon \mathbf{C} \to \mathrm{Rep}(H')$), there exists
   a unique Hopf map $\phi \colon H \to H'$ with
   $\alpha = U(\phi) \circ \mathrm{can}$.

3. **Naturality in $\tau$.** The group of monoidal natural
   automorphisms of $\tau$ is
   $\mathrm{Aut}^{\otimes}(\tau) \cong G(H)$, the group-like
   elements (characters) of $H$.

In the classical case ($\mathbf{C}$ symmetric), this is Tannaka's
theorem \cite{tannaka1939} as algebraised by Deligne \cite{deligne1990}:
The sheaf $H = \mathcal{O}(G)$ is the coordinate ring of a compact group $G$,
and $\mathrm{Aut}^{\otimes}(\tau) \cong G$.

In the quantum case ($\mathbf{C}$ braided but not symmetric), the
reconstruction is due to Woronowicz \cite{woronowicz1988}: $H$ is
a compact quantum group algebra $\mathcal{O}_q(G)$, and the braiding
$c_{V,W}$ on $\mathbf{C}$ encodes the universal $R$-matrix of $H$.
The deformation parameter $q$ is *not* an external input — it is
determined by the braiding, as shown in
([braiding eigenvalue extraction](#prop:braiding-eigenvalue-extraction)).
<!-- FILE_END: tannaka-krein-reconstruction.md -->

<!-- FILE_START: substrate-parameter.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe
([quantum observable universe](#def:quantum-observable-universe)) with
weight decomposition $\pi_H, \pi_V$
([weight decomposition](#def:weight-decomposition)) and Reeb derivation
$\xi$ ([categorical Reeb](#def:categorical-reeb)).  The non-commutative
de Rham complex $(\Omega^\bullet(A), d)$ carries two canonical
endomorphisms:

1. the full differential $d \colon \Omega^k(A) \to \Omega^{k+1}(A)$;
2. the vertical differential $\pi_V \circ d$, which retains only the
   component along the Reeb direction.

These span a one-parameter family of first-order operators
parametrised by $q \in \mathrm{End}(\mathbf{1}) \cong k^{\times}$:

$$
  d_q =  q^{-1}d +  (1 - q^{-1})\pi_V \circ d.
$$

```tex
\begin{equation}\label{eq:substrate-family-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \Omega^k(A) \ar[r, "d"] \ar[d, "\pi_V \circ d"'] \ar[dr, "d_q"]
  & \Omega^{k+1}(A) \\
  \Omega^{k+1}(A)
  & {} \ar[u, phantom, "q{=}1"' near start]
    \ar[l, phantom, "q{\to}\infty" near start]
\end{tikzcd}
\qquad\text{(substrate family)}
\end{equation}
```

The **substrate parameter** is the unique element
$q \in \mathrm{End}(\mathbf{1}) \cong k$ such that $d_q$
acts as $q^{-1}d$ on horizontal forms and as $d$ on vertical forms.
Geometrically, $q$ is the fibre coordinate on the
$\mathbb{G}_m$-family of interpolations.
<!-- FILE_END: substrate-parameter.md -->

<!-- FILE_START: substrate-parameter-limits-and-lusztig.md -->
At $q = 1$ the operator $d_q$ recovers $d$ (classicality: horizontal
and vertical differentiation are treated equally).  As
$q \to \infty$, $d_q$ projects onto $\pi_V \circ d$ (deep-quantum
regime: only the Reeb direction contributes).  The substrate
parameter is *not* intrinsic to the triple $(\mathbf{C}, A, \tau)$;
it records where one sits in the $\mathbb{G}_m$-family
that $q$ parametrises.

When the quantum universe is fibred over a space $M$ (as in the
archimedean realisation,
[$\mathbb{C}$-quantum universe](#ex:c-quantum-universe)), the categorical
substrate parameter specialises to a *substrate field*
$q \colon M \to k^{\times}$, encoding the local value of the
$\mathrm{End}(\mathbf{1})$-element at each point.

*Algebraic perspective.*  The Lusztig integral form
$\mathcal{U}^{\mathbb{Z}}_q(\mathfrak{su}(2))$ \cite{lusztig1993}
is the universal $\mathbb{Z}[q, q^{-1}]$-algebra generated by
$K^{\pm 1}$ and the divided powers $E^{(n)}, F^{(n)}$.  A ring
homomorphism $\iota \colon \mathbb{Z}[q, q^{-1}] \to k$,
$q \mapsto q_0$, base-changes this to the quantised enveloping algebra
at $q_0$.  The categorical and algebraic viewpoints agree: the
interpolation parameter $q$ in $d_q$ and the specialisation target
$q_0 = \iota(q)$ determine the same deformation.
<!-- FILE_END: substrate-parameter-limits-and-lusztig.md -->

<!-- FILE_START: substrate-parameter-exists.md -->
Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)) with
[weight decomposition](#def:weight-decomposition) $(\pi_H, \pi_V)$
and [categorical Reeb derivation](#def:categorical-reeb)
$(\xi, \varTheta_A)$. Then there exists a
[substrate parameter](#def:substrate-parameter)
$q \in \mathrm{End}(\mathbf{1}) \cong k$, with $q \notin \mu_\infty(k)$
(not a root of unity).  In the archimedean realisation this specialises
to a substrate field $q \colon M \to \mathbb{R}_{>0}$ with
$q(p) \ge 1$, such that the $q$-deformed differential

$$d_q = q^{-1} d + (1 - q^{-1}) \pi_V \circ d$$

interpolates between the full differential $d$ (at $q = 1$) and the
vertical projection $\pi_V \circ d$ (as $q \to \infty$).

```tex
\begin{equation}\label{eq:substrate-parameter-exists-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  d \ar[r, phantom, "\xleftarrow{q=1}"]
  & d_q \ar[r, phantom, "\xrightarrow{q \to \infty}"]
  & \pi_V \circ d
\end{tikzcd}
\qquad\text{(substrate interpolation)}
\end{equation}
```
<!-- FILE_END: substrate-parameter-exists.md -->

<!-- FILE_START: substrate-parameter-unique.md -->
Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)).
The [substrate parameter](#def:substrate-parameter)
$q \in \mathrm{End}(\mathbf{1})$ provided by
[existence](#thm:substrate-parameter-exists) is unique: if
$q, q' \in \mathrm{End}(\mathbf{1})$ both satisfy the substrate-parameter
axioms with respect to the same QOU structure, then $q = q'$.
<!-- FILE_END: substrate-parameter-unique.md -->

<!-- FILE_START: substrate-parameter-su2.md -->
Continuing the [quantum universe for $\mathrm{SU}(2)$](#ex:quantum-universe-su2),
we specify the [substrate parameter](#def:substrate-parameter) that
controls the deformation from classical $\mathrm{SU}(2)$ to quantum
$\mathrm{SU}_q(2)$.

**The specialisation map.** The categorical substrate parameter
$q \in \mathrm{End}(\mathbf{1})$ is realised via a ring
homomorphism $\iota \colon \mathbb{Z}[q, q^{-1}] \to \mathbb{C}$
determined by its value on the generator:
$\iota(q) = q_0 \in \mathbb{C}^\times$. All algebraic structures
(multiplication, comultiplication, antipode, $R$-matrix) are defined
over $\mathbb{Z}[q, q^{-1}]$ and specialise to concrete $\mathbb{C}$-algebras
via $\iota$.

**Classical case.** Setting $q_0 = 1$ recovers the undeformed coordinate
ring $\mathcal{O}(\mathrm{SU}(2))$ with its commutative multiplication:

$$
  \iota_{q_0 = 1} \colon
  \mathcal{O}_q(\mathrm{SU}(2))
   \longrightarrow 
  \mathcal{O}(\mathrm{SU}(2)),
  \qquad
  \begin{pmatrix} a & b \\ c & d \end{pmatrix}
  \mapsto
  \begin{pmatrix} a & b \\ c & d \end{pmatrix},
$$

where $ab = ba$, $ac = ca$, etc. This is the setting of the classical
[brane tower](#ex:recursive-brane-tower-su2).

**Quantum case.** For $q_0 = e^{\pi i / \kappa}$ with $\kappa \in \mathbb{Z}_{\geq 2}$ the Chern--Simons level, the specialisation
produces $\mathcal{O}_{q_0}(\mathrm{SU}(2))$ with non-commutative
relations:

$$
  ab = q_0 ba, \quad ac = q_0 ca, \quad
  bc = cb, \quad ad - da = (q_0 - q_0^{-1}) bc.
$$

The representation category
$\mathrm{Rep}(\mathrm{SU}_{q_0}(2))$ is a modular tensor category
with finitely many simple objects $V_0, V_{1/2}, \ldots, V_{(\kappa - 2)/2}$
when $q_0$ is a root of unity.

**Root-of-unity truncation.** At $q_0 = e^{\pi i / \kappa}$, the
spin-$j$ representations with $2j \geq \kappa - 1$ become reducible
or zero, leaving a finite semisimple category. The quantum dimension
of $V_j$ is

$$
  \dim_q(V_j) = \frac{q_0^{2j+1} - q_0^{-(2j+1)}}{q_0 - q_0^{-1}}
  = [2j + 1]_{q_0},
$$

the quantum integer. For $q_0 = 1$ this reduces to the classical
dimension $2j + 1$.

**Physical interpretation.** The substrate parameter $q_0$ interpolates
between the classical gauge theory ($q_0 = 1$, infinite-dimensional
representation category) and the topological quantum field theory
($q_0$ a root of unity, finite modular category). The Chern--Simons
level $\kappa$ controls the "granularity" of the quantum geometry.
<!-- FILE_END: substrate-parameter-su2.md -->

<!-- FILE_START: substrate-parameter-brings.md -->
Continuing the [Bring's surface example](#ex:brings-surface-concrete),
we extract the [substrate parameter](#def:substrate-parameter)
constructively — replacing "there exists $q$" with an explicit
algorithm.

**Step 1: the fundamental object.** Bring's QOU has
$\mathbf{C} = \mathrm{Rep}(\mathrm{SU}_q(2))$ with fundamental
object $V = V_{1/2} \cong \mathbb{C}^2$.

**Step 2: braiding eigenvalues.** The braiding
$c_{V,V} \colon V \otimes V \to V \otimes V$ is the $R$-matrix of
$\mathrm{SU}_q(2)$, acting on the $4$-dimensional space
$V \otimes V$. This space decomposes as
$V_{1/2} \otimes V_{1/2} \cong V_1 \oplus V_0$
(spin-$1$ $\oplus$ spin-$0$). The $R$-matrix has eigenvalue $+q$ on
the symmetric summand $S^2 V \cong V_1$ and eigenvalue $-q^{-1}$ on
the antisymmetric summand $\Lambda^2 V \cong V_0$. In matrix form
on the standard basis $\{e_+ \otimes e_+,\, e_+ \otimes e_-,\,
e_- \otimes e_+,\, e_- \otimes e_-\}$:

$$
  R = \begin{pmatrix}
    q & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 1 & q - q^{-1} & 0 \\
    0 & 0 & 0 & q
  \end{pmatrix}.
$$

**Step 3: read off $q$.** Define $q := \lambda_+$, the eigenvalue of
$c_{V,V}$ on $S^2 V$. This is a concrete number, not an existential
assertion. The Hecke relation $(T - q)(T + q^{-1}) = 0$ is then
*verified* (not postulated) by checking that $R$ satisfies
$R^2 - (q - q^{-1})R - I = 0$.

**Step 4: non-degeneracy.** The QOU axiom $c_{V,V}^2 \neq \mathrm{id}$
forces $q \neq \pm 1$. The dagger structure
$c_{V,V}^{\dagger} = c_{V,V}^{-1}$ forces $|q| = 1$ or
$q \in \mathbb{R} \setminus \{0\}$.

**Bring's surface specialisation.** The Euler characteristic
$\chi(A) = -6$ constrains $q$ further. The quantum dimension of
$A = \mathcal{O}_q(\mathrm{SU}(2))$ satisfies
$\mathrm{tr}(\mathrm{id}_A) = [N]_q [N-1]_q / [1]_q$ at $N = 2$, giving
$\chi(A) = [2]_q [1]_q / [1]_q = [2]_q = q + q^{-1}$.
The Descartes condition $\chi(A) = 2 - 2g = -6$ requires
$q + q^{-1} = -6$, i.e. $q^2 + 6q + 1 = 0$, so
$q = -3 \pm 2\sqrt{2}$. The two roots are both negative
(consistent with $q + q^{-1} < 0$). Choosing the root closer to
zero:

$$
  q_{\mathrm{Bring}} = -3 + 2\sqrt{2} \approx -0.172.
$$

(The other root $q = -3 - 2\sqrt{2} \approx -5.83$ is its
reciprocal.) This *categorical* parameter lives in the Laurent
polynomial ring $\mathbb{Z}[q, q^{-1}]$; the *physical* substrate
parameter $q_0 = 1.109978595554181\ldots$ (50 dps) arises from the archimedean
realisation via the muon/electron mass ratio
([skein mass relation](#rem:skein-mass-relation)). The two are
related by the specialisation map
$\iota \colon \mathbb{Z}[q, q^{-1}] \to \mathbb{C}$.

**Summary.** The substrate parameter is not only "known to exist" —
it is extracted by a three-step algorithm: (1) form $V \otimes V$,
(2) diagonalise $c_{V,V}$, (3) read off the symmetric eigenvalue.
On Bring's surface, the Descartes condition pins $q$ to a specific
algebraic number.
<!-- FILE_END: substrate-parameter-brings.md -->

<!-- FILE_START: quantum-gauge-group.md -->
Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)) with
substrate parameter $q \in \mathrm{End}(\mathbf{1})$
([substrate parameter](#def:substrate-parameter)), where $q$ is the
braiding eigenvalue on the symmetric summand of $V \otimes V$
([braiding eigenvalue extraction](#prop:braiding-eigenvalue-extraction)).
The **quantum gauge group** is the Hopf algebra
$H = \mathrm{End}^{\otimes}(\tau)$ reconstructed via Tannaka--Krein
duality ([reconstruction](#prop:tannaka-krein-reconstruction)).
By the universal property, $H \cong \mathcal{O}_q(\mathrm{SU}(2))$
— the coordinate ring of $\mathrm{SU}_q(2)$ at the categorically
determined $q$:

$$
  G_q =  \mathrm{SU}_q(2),
  \qquad
  q = \text{eigenvalue of } c_{V,V} \text{ on } S^2 V.
$$

The classical gauge group
$G = \mathrm{Aut}^{\otimes}(\tau) \cong \mathrm{SU}(2)$
([$\mathrm{SU}(2)$ emergence](#thm:su2-emergence)) is the $q = 1$ case
(symmetric braiding).
In the archimedean realisation, where the substrate parameter specialises
to a substrate field over $M$, this yields a field of quantum groups
$\{G_{q(p)}\}_{p \in M}$.
<!-- FILE_END: quantum-gauge-group.md -->

<!-- FILE_START: quantum-planck-constant.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
substrate parameter $q \in \mathrm{End}(\mathbf{1}) \cong k$
([substrate parameter](#def:substrate-parameter)).  The
**quantum Planck constant** is the element
$\hbar_q = 1 - q^{-1} \in k$.  When the categorical substrate parameter
specialises to a substrate field over a space $M$, this defines a field
$\hbar_q \colon M \to k$ by $\hbar_q(p) = 1 - q(p)^{-1}$.
<!-- FILE_END: quantum-planck-constant.md -->

<!-- FILE_START: planck-limits.md -->
Like $q$ itself, $\hbar_q$ is not a universal constant but a field on $M$.
As $q(p) \to 1$ (classicality), $\hbar_q(p) \to 0$ and quantum effects
vanish; as $q(p) \to \infty$ (deep-quantum regime), $\hbar_q(p) \to 1$.
<!-- FILE_END: planck-limits.md -->

<!-- FILE_START: q-hodge-star.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
categorical Hodge star $\star$
([categorical hodge star](#def:categorical-hodge-star)) and substrate
parameter $q$ ([substrate parameter](#def:substrate-parameter)).  The
**$q$-Hodge star** is the $q$-deformed involution
$\star_q \colon \Omega^k(A) \to \Omega^{n-k}(A)$ defined by

$$
  \alpha \wedge_q \star_q \beta
  =  q \cdot \int_A\!\bigl(\alpha^* \cdot \beta\bigr) \mathrm{vol}.
$$

```tex
\begin{equation}\label{eq:q-hodge-star-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \Omega^k(A) \ar[r, "\star_q"] \ar[d, "\star"']
  & \Omega^{n-k}(A) \\
  \Omega^{n-k}(A) \ar[ur, "q \cdot \mathrm{id}"']
\end{tikzcd}
\qquad\text{($q$-Hodge star)}
\end{equation}
```

At $q = 1$ this recovers the categorical Hodge star:
$\star_1 = \star$.  The factor of $q$ rescales the inner product on
forms, coupling the Hodge duality to the local deformation strength.
<!-- FILE_END: q-hodge-star.md -->

<!-- FILE_START: exceptional-divisor.md -->
Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be a QOU and let $p \in M$ be a brane point
with outward normal $N(p) = p/\lvert p\rvert$ and positively-oriented
tangent frame $(T_1, T_2)$.  Set $R = R_{\mathbb{P}^1(\mathbb{C})}$ and

$$
  O(p) =  p + RN(p).
$$

The **exceptional divisor** at $p$ is the fibre of the state bundle
$\mathcal{S}$ at $p$ --- the $\mathbb{P}^1(\mathbb{C})$ fibre

$$
  \mathcal{S}_p =  \pi^{-1}(p)
  = 
  \bigl\{
    O(p) + R\bigl(\sin\phi (\cos\psi T_1 + \sin\psi T_2) - \cos\phi N\bigr)
     : 
    \phi \in [0,\pi], \psi \in [0,2\pi)
  \bigr\},
$$

where $\pi\colon \widetilde{M} \to M$ is the blow-up map that replaces $p$
with $\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$.
<!-- FILE_END: exceptional-divisor.md -->

<!-- FILE_START: commutative-qou.md -->
Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be a QOU with Frobenius--Hopf
object $A$.  The QOU is **strictly commutative** when the multiplication
$\mu \colon A \otimes A \to A$ satisfies
$\mu \circ c_{A,A} = \mu$ and, dually, the comultiplication
$\Delta$ is cocommutative, $c_{A,A} \circ \Delta = \Delta$.

By the self-duality of the Frobenius--Hopf structure, the two
conditions are equivalent, and by
[$q$-parameter tracking](#rem:hopf-non-cocommutativity) they are
equivalent to the classical limit $q \to 1$.  In this limit the
quantum gauge group $\mathcal{O}_q(\mathrm{SU}(2))$ reduces to
$\mathcal{O}(\mathrm{SU}(2))$, the ambient braiding
$c$ becomes symmetric ($c \circ c = \mathrm{id}$), and
$\mathrm{Rep}(\mathbf{C})$ degrades to a classical (symmetric)
Tannakian category.

**Scope.**  The strictly commutative QOU is the single-parameter
specialisation $q = 1$ inside the full deformation family. It is the
natural home for the hyperelliptic quintic $\mathcal{X}_5$ (Definition
[def:hyperelliptic-quintic](#def:hyperelliptic-quintic)) and the
$\mathrm{U}(1)$-equivariant reduction of the exceptional divisor
(Proposition [prop:u1-equivariant-reduction](#prop:u1-equivariant-reduction)).

Anyonic structure --- which requires $c \circ c \neq \mathrm{id}$ ---
does **not** live here; it belongs to the root-of-unity specialisation
$q = e^{2\pi i/N}$ treated in Chapter 7 (Fluid Dynamics).
<!-- FILE_END: commutative-qou.md -->

<!-- FILE_START: u1-equivariant-reduction.md -->
**Proposition.**
Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be a commutative-limit QOU
([def:commutative-qou](#def:commutative-qou)) and let
$\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$ be the exceptional
divisor at a brane point $p$
([def:exceptional-divisor](#def:exceptional-divisor)).  Fix the
action of the maximal torus $\mathrm{U}(1) \subset \mathrm{SU}(2)$
by rotation about the polar axis.  The space of
$\mathrm{U}(1)$-equivariant observables on $\mathcal{S}_p$,

$$
  \mathrm{Obs}_{\mathrm{U}(1)}(\mathcal{S}_p)
    = 
   \bigl(\mathrm{Obs}(\mathcal{S}_p)\bigr)^{\mathrm{U}(1)},
$$

is supported on the orbit space
$\mathcal{S}_p / \mathrm{U}(1) \cong [0, \pi]$, and over the interior
of the interval restricts to a free $\mathrm{U}(1)$-bundle whose
section space is parametrised by a single phase coordinate
$\varphi \in S^1$.
<!-- FILE_END: u1-equivariant-reduction.md -->

