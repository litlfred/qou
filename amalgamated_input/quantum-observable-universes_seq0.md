<!-- FILE_START: qou-definition-intro.md -->
This chapter opens by adding four conditions to the
quantum universe of Chapter 1 — non-degenerate integration,
observability, measurability via vanishing categorical Chern
classes, and the categorical volume constraint — and naming the
resulting structure. Definition: Quantum Observable Universe
collects the four axioms on the triple $(\mathbf{C}, A, \tau)$;
the rest of the chapter takes this triple as fixed input.

The structural backbone is Proposition: Existence of quantum observable universes, proved axiom-by-axiom across four lemmas —
Lemma: Haar non-degeneracy, Lemma: adjoint observability,
Lemma: vanishing categorical Chern classes, and
Lemma: quantum-determinant volume invariance — each with its
own proof block. Proposition: Braiding-induced ordering records
that the non-symmetric braiding $c_{V,V}$ supplies a canonical
admissible well-ordering $\prec_c$ on the Hecke monomial basis,
identifying the categorical arrow of time with positive crossings.
Remark: Frobenius integration reads the non-degeneracy axiom
as a categorical Haar measure, Remark: categorical Stokes
reads the measurability axiom through the nonabelian Stokes
theorem, and Remark: fibre-functor rigidity collects the
cohomological consequence that $\tau$ admits no non-trivial
deformations.

We close on Example: QOU on $\mathrm{SU}(2)$ — the running
$\mathcal{O}(\mathrm{SU}(2))$ realisation that will be exercised
throughout the chapter — and Remark: base-field independence,
which records that the axioms are stated over an arbitrary
commutative ring. The next section, **Emergence from
observability**, takes this triple as given and derives
$G \cong \mathrm{SU}(2)$ from the volume constraint alone.

_(draft.)_
<!-- FILE_END: qou-definition-intro.md -->

<!-- FILE_START: quantum-observable-universe.md -->
A quantum universe $(\mathbf{C}, A, \tau)$ over $R$
([quantum universe](#def:quantum-universe)) is a
**quantum observable universe** — is *observable* — if the
forgetful functor $\tau$
([Example](#ex:rigid-monoidal-vect)) is faithful and the following
conditions hold:

1. *(non-degenerate integration)* the Frobenius form
 $\int_A \colon A \to \mathbf{1}$ induces a
 non-degenerate pairing
 $(a, b) \mapsto \int_A ab$
 ([Frobenius pairing](#def:frobenius-pairing)), giving an
 isomorphism $A \xrightarrow{ \sim } A^{\vee}$;

2. *(observability)* there are no hidden global symmetries:
 $\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A)) = 0$, where $\mathrm{Ad}(A)$ is the adjoint object
 ($A$ acted on by conjugation). The
 formal statement is that every morphism
 $\mathbf{1} \to \mathrm{Ad}(A)$ is zero:

 ```tex
   \[
   \begin{tikzcd}[column sep=2.5em]
     \mathbf{1} \ar[r, "0"] & \mathrm{Ad}(A)
   \end{tikzcd}
   \qquad\text{(observability)}
   \]
   ```

3. *(measurability / anomaly-free)* the primary Chern classes of the
 adjoint object vanish. Precisely, define the *Chern classes of a
 categorical object* $X$ by pulling back through the fibre functor:

 $$
   c_i(X)  :=  c_i\!\bigl(\tau(X)\bigr)
      \in  H^{2i}_{\mathrm{dR}}\!\bigl(\mathrm{Spec}R\bigr),
   $$

 where the right-hand side is the classical Chern class of the
 realised $R$-module (or, in the archimedean setting, of the
 associated vector bundle $\tau(X) \times_G M$). This definition is
 intrinsic to the pair $(\mathbf{C}, \tau)$ — the fibre functor
 $\tau$ is part of the QOU datum — and reduces to the standard
 topological Chern classes in every geometric realisation. The
 measurability axiom requires:

 $$
     c_1(\mathrm{Ad}(A)) = 0
     \qquad\text{and}\qquad
     c_2(\mathrm{Ad}(A)) = 0.
   $$


4. *(categorical volume constraint)*
 let $V$ denote the fundamental object of $\mathbf{C}$
 ([Remark](#sec:fundamental-object-explication)); there exists a
 non-degenerate epimorphism $\epsilon$ preserved by the rigid
 dualities, making the following diagram commute for every
 $g \in \mathrm{Aut}^{\otimes}(\tau)$:

 ```tex
   \begin{equation}\label{eq:categorical-volume-constraint}
   \begin{tikzcd}[row sep=2.5em, column sep=3em]
     \Lambda^2 V \ar[r, "\Lambda^2 g_V"]
                 \ar[d, "\epsilon"', two heads]
     & \Lambda^2 V \ar[d, "\epsilon", two heads]
     \\
     \mathbf{1} \ar[r, "g_{\mathbf{1}} = \mathrm{id}"']
     & \mathbf{1}
   \end{tikzcd}
   \qquad\text{(volume constraint)}
   \end{equation}
   ```

The braiding $c_{V,V}$ on $\mathbf{C}$ (which is non-symmetric:
$c_{V,V}^2 \neq \mathrm{id}$, since $\mathbf{C}$ is braided
monoidal but not symmetric monoidal) induces a canonical
admissible well-ordering on the Hecke basis. See
[braiding-induced ordering](#prop:braiding-induced-ordering).
<!-- FILE_END: quantum-observable-universe.md -->

<!-- FILE_START: qou-axioms-physical-reading.md -->
The observability axiom (2) has a direct physical reading: there are
no hidden global symmetries, so every internal degree of freedom is
accessible to measurement — no gauge transformation acts as the
identity on all observables.

The measurability axiom (3) is likewise an anomaly-freedom condition.
The first vanishing $c_1(\mathrm{Ad}(A)) = 0$ ensures the adjoint
bundle is orientable, precluding global anomalies; the second
$c_2(\mathrm{Ad}(A)) = 0$ ensures the volume form acquires no
topological phases (see
[Remark](#rem:yekutieli-stokes) for the connection to
categorical flatness via Yekutieli's nonabelian Stokes theorem).
For many applications, axioms (1), (2), and (3) suffice — axiom
(3) is needed only when global topology of $M$ matters.
<!-- FILE_END: qou-axioms-physical-reading.md -->

<!-- FILE_START: quantum-observable-universe-exists.md -->
**Proposition.**
*Let $G$ be a compact, connected, semisimple Lie group with complexified
Lie algebra $\mathfrak{g}$. Let $M$ be a compact oriented manifold
admitting a principal $G$-bundle $P \to M$ whose adjoint bundle
$\mathrm{Ad}(P) = P \times_{G} \mathfrak{g}$ satisfies the measurability
condition*

$$
  c_{1}\!\bigl(\mathrm{Ad}(P)\bigr) = 0
  \qquad\text{and}\qquad
  c_{2}\!\bigl(\mathrm{Ad}(P)\bigr) = 0.
$$

*Then there exists a
[quantum observable universe](#def:quantum-observable-universe)
$(\mathbf{C}, A, \tau)$ satisfying the four QOU axioms ---
non-degenerate integration, observability, measurability, and the
categorical volume constraint --- whose archimedean realisation has
state bundle $\mathcal{S} = P \times_{G} V_{\mathrm{std}}$.*

*Explicitly, one may take*

$$
  \mathbf{C} = \mathbf{Rep}\bigl(U_{q}(\mathfrak{g})\bigr),
  \qquad
  A = \mathcal{O}_{q}(G),
  \qquad
  \tau = \mathrm{forget},
$$

*where $q \in \mathbb{C}^{\times}$ is the substrate parameter
([substrate parameter](#def:substrate-parameter)), $U_{q}(\mathfrak{g})$
is the Drinfeld--Jimbo quantum group, $\mathcal{O}_{q}(G)$ is its
restricted dual Hopf algebra, and the Frobenius form $\int_{A}$ is the
Haar state on $\mathcal{O}_{q}(G)$
([$\mathrm{SU}(2)$-QOU](#ex:qou-su2)).*

The measurability hypothesis on $P$ is not vacuous but admits common
realisations: for $G = \mathrm{SU}(2)$ and $M$ a contact CR 3-manifold,
$c_{1}(\mathrm{Ad}(P)) = 0$ is automatic ($G$ is connected)
while $c_{2}(\mathrm{Ad}(P)) = 0$ selects the topologically trivial
sector. Non-vanishing $c_{2}$ is also admissible with $q = e^{\pi i/(k +
h^{\vee})}$ a root of unity, replacing $\mathbf{C}$ by the modular
tensor category $\mathbf{Rep}_{k}(\widehat{\mathfrak{g}})$ at level
$k = \langle c_{2}, [M] \rangle$ (Reshetikhin--Turaev). Both regimes
establish existence. No universal-property uniqueness holds: a QOU is
a *structure*, not a universal object.

The proof is constructive: we exhibit $(\mathbf{C}, A, \tau)$ and
verify the four axioms in
[proof of QOU existence](#prf:quantum-observable-universe-exists).

\cite{woronowicz1987, woronowicz1988, reshetikhin1991, kassel1995, chari1994}
<!-- FILE_END: quantum-observable-universe-exists.md -->

<!-- FILE_START: qou-exists-axiom-1.md -->
**Lemma.**
*The Haar state $h = \int_{A}$ on $A = \mathcal{O}_{q}(G)$ is faithful;
equivalently, the pairing $(a, b) \mapsto h(ab)$ is non-degenerate
and induces an isomorphism $A \xrightarrow{\sim} A^{\vee}$, verifying
axiom~(1) of [quantum observable universe](#def:quantum-observable-universe).*
<!-- FILE_END: qou-exists-axiom-1.md -->

<!-- FILE_START: qou-exists-axiom-2.md -->
**Lemma.**
*For $\mathbf{C} = \mathbf{Rep}(U_{q}(\mathfrak{g}))$ at generic $q$
and $A = \mathcal{O}_{q}(G)$,
$\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A)) = 0$
modulo the unit, verifying axiom~(2) of
[quantum observable universe](#def:quantum-observable-universe).*
<!-- FILE_END: qou-exists-axiom-2.md -->

<!-- FILE_START: qou-exists-axiom-3.md -->
**Lemma.**
*Under the proposition's hypothesis $c_{1}(\mathrm{Ad}(P)) = c_{2}(\mathrm{Ad}(P)) = 0$,
the categorical Chern classes
$c_{i}(\mathrm{Ad}(A)) := c_{i}(\tau(\mathrm{Ad}(A)))$ vanish, verifying
axiom~(3) of
[quantum observable universe](#def:quantum-observable-universe).
For $c_{2}(\mathrm{Ad}(P)) \neq 0$ the construction is replaced by
the modular tensor category $\mathbf{Rep}_{k}(\widehat{\mathfrak{g}})$
at level $k = \langle c_{2}, [M] \rangle$, with the level absorbed
into the ribbon twist.*
<!-- FILE_END: qou-exists-axiom-3.md -->

<!-- FILE_START: qou-exists-axiom-4.md -->
**Lemma.**
*Let $V \in \mathbf{C}$ be the standard representation of dimension
$n$.  The quantum determinant $\epsilon \colon \Lambda^{n} V \to \mathbf{1}$
is invariant under all tensor automorphisms of the fibre functor:*

$$
  \epsilon \circ \Lambda^{n}(g_{V}) = \epsilon
  \quad \text{for all } g \in \mathrm{Aut}^{\otimes}(\tau).
$$

*This verifies axiom~(4) of
[quantum observable universe](#def:quantum-observable-universe).*
<!-- FILE_END: qou-exists-axiom-4.md -->

<!-- FILE_START: braiding-induced-ordering.md -->
**Proposition.**
*Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe
([QOU](#def:quantum-observable-universe)) whose braiding
$c_{V,V} \colon V \otimes V \to V \otimes V$ is non-symmetric
($c_{V,V}^2 \neq \mathrm{id}$).  Then $c_{V,V}$ determines
a canonical admissible well-ordering $\prec_c$ on the monomial
basis $B$ of the Iwahori--Hecke algebra $H_n(q)$ of $A$.*

**Construction.**  The monomial basis $B$ of $H_n(q)$ consists
of reduced positive braid monomials
$w = \sigma_{i_1}\sigma_{i_2}\cdots\sigma_{i_k}$ —
the images of the braiding $c_{V,V}$ under
$\rho_n(\sigma_i) = \mathrm{id}^{\otimes(i-1)} \otimes c_{V,V} \otimes \mathrm{id}^{\otimes(n-i-1)}$
([braid action on tensor powers](#prop:braid-action-tensor)).
The braiding $c_{V,V}$ (as opposed to its inverse
$c_{V,V}^{-1}$) defines "positive crossing" — forward time.

*Definition.* A **well-ordering** on a set $S$ is a total
order $\prec$ such that every non-empty subset of $S$ has a
least element.  Equivalently: there are no infinite strictly
descending chains $s_1 \succ s_2 \succ s_3 \succ \cdots$.

*Definition.* The **degree-lexicographic ordering** $\prec_c$
on $B$ is: $w \prec_c w'$ if and only if

$$
  \ell(w) < \ell(w'),
  \quad\text{or}\quad
  \ell(w) = \ell(w')  \text{and}
  (i_1, \ldots, i_k) <_{\mathrm{lex}} (i_1', \ldots, i_k')
$$

where $\ell(w) = k$ is the word length (number of crossings)
and $<_{\mathrm{lex}}$ is lexicographic order on the generator
indices $i_j \in \{1, \ldots, n-1\}$.
<!-- FILE_END: braiding-induced-ordering.md -->

<!-- FILE_START: frobenius-integration.md -->
The Frobenius form $\int_A \colon A \to \mathbf{1}$ extends to a
pairing on products:

$$
  \int_A ab  :=  \int_A \!\circ \mu(a \otimes b).
$$

The non-degeneracy condition (i) of
[quantum observable universe](#def:quantum-observable-universe) then
reads: the pairing $(a, b) \mapsto \int_A ab$ induces an isomorphism
$A \xrightarrow{ \sim } A^{\vee}$.

Readers familiar with TQFT will recognise $\int_A$ as a categorical
Haar measure: the unique (up to scalar) $G$-invariant functional on $A$.
The existence of the volume $\epsilon$
([categorical volume constraint](#eq:categorical-volume-constraint))
may then be read as the normalisation condition
$\int_A \mathbf{1}$ is a well-defined topological constant.
<!-- FILE_END: frobenius-integration.md -->

<!-- FILE_START: yekutieli-stokes-remark.md -->
The measurability condition
$c_1(\mathrm{Ad}(A)) = 0$, $c_2(\mathrm{Ad}(A)) = 0$ can be
understood through the nonabelian Stokes theorem
\cite{yekutieli2015}. The core of that theorem is: for a nonabelian
integral to be well-defined over a surface or volume, the curvature of
the connection must vanish (or be highly constrained).

In the QOU setting, the vanishing of $c_1(\mathrm{Ad}(A))$ is a
*necessary condition* for the adjoint representation to admit a flat
structure --- it removes the primary topological obstruction to
flatness.  Combined with the categorical rigidity of the
Frobenius--Hopf algebra (which constrains the connection to the
instanton locus), this necessary condition becomes sufficient:
the categorical volume $\epsilon$
([categorical volume constraint](#eq:categorical-volume-constraint))
is well-defined precisely because the instanton connection on
$\mathrm{Ad}(A)$ is flat.  The existence of $\epsilon$ can therefore
be viewed as a categorical realisation of the nonabelian Stokes
theorem.

The additional condition $c_2(\mathrm{Ad}(A)) = 0$ ensures that
$\epsilon$ is canonically unique and does not acquire topological
phases under transport around non-contractible cycles. Together, the
two vanishing conditions make $\mathrm{Ad}(A)$ *anomaly-free*: the
adjoint bundle carries no hidden topological obstructions to
integration.
<!-- FILE_END: yekutieli-stokes-remark.md -->

<!-- FILE_START: fibre-functor-rigidity.md -->
*(For the category-theorist reader.)*
The fibre functor $\tau$ plays a deliberately passive role in this paper.
The reason is cohomological: the observability axiom

$$
  \mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A)) = 0
$$

is equivalent to the vanishing of zeroth adjoint cohomology,
$H^0_G(\mathrm{Ad}(A)) = 0$. Since the Lie algebra of
$\mathrm{Aut}^{\otimes}(\tau)$ is precisely
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A))$, this vanishing
kills all infinitesimal automorphisms of $\tau$. Combined with the
measurability conditions $c_1(\mathrm{Ad}(A)) = c_2(\mathrm{Ad}(A)) = 0$,
the fibre functor becomes *rigid* in the deformation-theoretic sense:
it admits no non-trivial first-order deformations, and Tannaka--Krein
reconstruction pins it uniquely (up to monoidal natural isomorphism).
There is, consequently, nothing geometrically or algebraically interesting
happening at the level of $\tau$ itself — the entire content of the
theory lives in $(\mathbf{C}, A)$.

If we relax the observability axiom — allowing
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) \neq 0$ — the situation
changes qualitatively. Non-trivial $G$-invariant sections of the
adjoint bundle reappear, the automorphism group
$\mathrm{Aut}^{\otimes}(\tau)$ acquires a non-trivial centre, and
the deformation theory of $\tau$ becomes obstructed. In this regime,
Yekutieli's obstruction classes $\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$
\cite{yekutieli2010} interact with the newly non-vanishing adjoint
cohomology to produce additional obstructions to lifting Frobenius--Hopf
objects through the brane tower — obstructions that are invisible under
the assumptions of the present paper. The twisted deformation quantization
framework from \cite{yekutieli2008} is the setting for analysing
these: the hidden symmetries generate a non-trivial MC element
in the pronilpotent DG Lie algebra governing deformations of $\tau$
\cite{yekutieli2009}, and the resulting obstruction tower is the
content of Yekutieli's theory of central extensions of gerbes.
<!-- FILE_END: fibre-functor-rigidity.md -->

<!-- FILE_START: qou-su2.md -->
Continuing [Examples](#ex:rigid-monoidal-vect)
and [quantum universe on $\mathrm{SU}(2)$](#ex:quantum-universe-su2), write
$V = V_{1/2} \cong \mathbb{C}^2$:

1. *Non-degeneracy.* The Haar integral $\int_A = \int_G$ on
   $\mathcal{O}(\mathrm{SU}(2))$ is faithful: if
   $\int_A(f^* f) = 0$ then $f = 0$.

2. *Observability.* The adjoint representation
   $\mathrm{Ad} \cong V_1$ (spin-$1$, dimension $3$)
   is irreducible, so it contains no copy of the
   trivial representation: $\mathrm{Hom}(\mathbf{1}, V_1) = 0$.

3. *Volume constraint.* For $v, w \in V = \mathbb{C}^2$,
   the determinant
   $\epsilon(v \wedge w) = v_1 w_2 - v_2 w_1$
   defines a non-degenerate map
   $\epsilon \colon \Lambda^2 V \to \mathbb{C}$.
<!-- FILE_END: qou-su2.md -->

<!-- FILE_START: base-field-independence.md -->
[quantum universe](#def:quantum-universe) and [quantum observable universe](#def:quantum-observable-universe)
are formulated over an arbitrary commutative ring $R$. The Frobenius--Hopf axioms
replace the analytic vanishing conditions of the archimedean realisation
([$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe)) with a single algebraic
non-degeneracy condition on the Frobenius form. Concrete realisations
include:

- $R = K$ an archimedean field (a field with an archimedean absolute
  value, e.g. $\mathbb{Q}$, $\mathbb{R}$, or $\mathbb{C}$): the
  setting of CR geometry and contact manifolds
  ([$\mathbb{C}$-quantum universe](#ex:c-quantum-universe));
- $R = \mathbb{Q}_\pp$ (the $\pp$-adic field): the gauge datum becomes
  an $F$-isocrystal with Frobenius lift
  ([$p$-adic realisation](#ex:p-adic-realisation),
  [Chapter](#chap:brings-surface));
- $R = \mathbb{F}_\pp$ (a finite field): representations of a quantum
  group over $\mathbb{F}_\pp$
  ([finite field realisation](#ex:finite-field-realisation));
- $R = \mathbb{Z}[q, q^{-1}]$: the universal (Lusztig) integral form.

The fibre functor $\tau$ ensures that $G = \mathrm{Aut}^{\otimes}(\tau)$
is well-defined over any $R$.
<!-- FILE_END: base-field-independence.md -->

