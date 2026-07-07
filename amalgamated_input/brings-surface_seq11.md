<!-- FILE_START: archimedean-condition-genus-completeness-genus-ideal-characterisation-intro.md -->
Continuation of the preceding sub-section.

This sub-section pins the *genus ideal* — the set of categorical
genus invariants that the archimedean condition isolates — as a
finitely generated ideal characterised by the Yekutieli leading
coefficient.  The proof proceeds in two layers: the leading
coefficient identification fixes the generator set; the genus
filtration interprets the ideal as a structured cover of the
torus-embeddable subspace.  The closing blocks complete the arc by
showing that every torus-embeddable categorical knot lies in the
generation closure of the genus ideal, which makes the Descartes
condition equivalent to a finite combinatorial classification.
<!-- FILE_END: archimedean-condition-genus-completeness-genus-ideal-characterisation-intro.md -->

<!-- FILE_START: genus-ideal-characterisation.md -->
**Lemma.**
*At genus $g = 4$, the kernel of the truncation
$\pi_4 \colon \mathbb{Z}[u] \to \mathbb{Z}[u]/(u^5)$ is the
genus-filtration ideal $\mathfrak{I}_4 = (u^5)$, consisting of
those terms in the Chebyshev expansion of $a_p$ whose Seifert
cycles have no target in $H_1(\Sigma_4)$.*
<!-- FILE_END: genus-ideal-characterisation.md -->

<!-- FILE_START: yekutieli-leading-coefficient.md -->
**Lemma.**
*For $T_{2,p}$ at level $n = g + 1 = 5$, the Yekutieli obstruction
$\kappa(T_{2,p}) \in H^2(\mathcal{S}, \mathcal{B})$ equals the
leading Chebyshev coefficient $c_{(p-1)/2} = 1$.  In particular
$\kappa(T_{2,p}) \neq 0$ for $q \neq 1$.*
<!-- FILE_END: yekutieli-leading-coefficient.md -->

<!-- FILE_START: genus-filtration-ideal.md -->
The genus of the moduli surface is not assumed --- it is
**determined by the Iwahori--Hecke algebra**.  The QOU axioms force
$g = 4$ through a completeness condition on the irreducible
representations of $H_2(q) \oplus H_3(q)$, and the
genus-filtration ideal $\mathfrak{I}_4 = (u^5)$ is the
algebraic obstruction that kills $T_{2,p}$ for all primes
$p \geq 11$.

## Part 0: the genus is determined by the algebra

**Proposition (Genus from Hecke completeness).**
*Let $(\mathbf{C}, A, \tau)$ be a QOU with
$G = \mathrm{SU}_q(2)$.  The braiding on $V_1^{\otimes n}$
gives the Iwahori--Hecke algebra $H_n(q)$.  The relevant strand
counts are $n = 2$ and $n = 3$:*

- *$H_2(q)$ has $2$ irreducible representations
  (partitions of $2$: $(2)$ trivial, $(1,1)$ sign).*
- *$H_3(q)$ has $3$ irreducible representations
  (partitions of $3$: $(3)$, $(1,1,1)$, $(2,1)$).*
- *Total: $5$ irreps.*

*At genus $g$, the embeddable torus knots $T_{r,s}$ with
$(r-1)(s-1) \leq 2g$ and $\gcd(r,s) = 1$ are the ones whose
Jones polynomials can be evaluated on $\Sigma_g$.  Completeness
([cohomological embedding](#prop:cohomological-embedding))
requires that these evaluations **span all $5$ irrep
characters**: the evaluation matrix
$M_{ij} = \chi_{\lambda_j}(\sigma_i)$ must have rank $5$.*

*The strand counts $m \geq 4$ contribute no new knots: at genus
$g$, the constraint $(m-1)(s-1) \leq 2g$ with $m \geq 4$ and
$m < s$, $\gcd(m,s) = 1$, gives $s \leq 2g/(m-1) + 1$, which
for $m = 4$ yields $T_{4,3} = T_{3,4}$ (already counted) and
for $m \geq 5$ yields no valid $(m, s)$ pairs with $m < s$.
Therefore $H_2(q) \oplus H_3(q)$ is the complete Hecke
algebra of the QOU.*

**The genus scan.**

See [Table 1](#tbl:genus-filtration-ideal-table1-data).

*At $g = 3$: only $4$ knots are available, but $5$ irreps
must be spanned.  Rank $\leq 4 < 5$ --- incomplete.
Observability
($\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$) would be
violated: there would exist knot observables not determined
by the generators.*

*At $g = 4$: the two additional knots $T_{2,9}$ (Chebyshev
degree $4$, saturates) and $T_{3,5}$ (genus $4$, saturates)
bring the total to $6$ knots spanning $5$ irreps.
Rank $= 5$ --- complete.*

*At $g \geq 5$: $T_{2,11}$ and further knots embed, but they
add no new irreps (rank stays $5$).  These extra knots predict
**unobserved particles** --- the redundancy violates
minimality.*

*Therefore $g = 4$ is the **unique minimal genus** where the
Hecke completeness condition holds.*

## Part I: Chebyshev degree = Seifert genus

**Origin of the Chebyshev structure.**
The Iwahori--Hecke algebra $H_2(q)$ is $2$-dimensional with basis
$\{1, T\}$ and the single relation $T^2 = sT + 1$ where
$s = q - q^{-1}$.  The generator $T$ has two eigenvalues:
$q$ (symmetric channel) and $-q^{-1}$ (antisymmetric channel).
Computing $T^p$ --- the $p$-th power of the braid generator
--- reduces it via the relation:

$$
  T^p =  a_p \cdot T +  a_{p-1} \cdot \mathbf{1}
$$

The coefficients $a_n$ satisfy the recurrence
$a_{n+1} = s \cdot a_n + a_{n-1}$ with $a_0 = 0$, $a_1 = 1$.
This is the **Chebyshev recurrence**: powers of a matrix with
two eigenvalues are always Chebyshev polynomials.  Precisely,
$a_p = U_{p-1}(s/2)$, the Chebyshev polynomial of the second
kind evaluated at $s/2$, where
$U_n(\cos\varTheta) = \sin((n+1)\varTheta)/\sin\varTheta$.

For odd $p$, only even powers of $s$ appear, so writing
$u = s^2 = (q - q^{-1})^2$:

$$
  a_p(u)
  = 
  U_{p-1}\!\left(\tfrac{s}{2}\right)
  = 
  \sum_{j=0}^{(p-1)/2} c_j u^j
$$

with leading coefficient $c_{(p-1)/2} = 1$.

**The degree--genus identity.**
The algebraic complexity of the Hecke coefficient (the
polynomial degree $\deg_u a_p$) equals the topological
complexity of the knot (the Seifert genus $g(T_{2,p})$):

$$
  \deg_u a_p =  \frac{p-1}{2} =  g(T_{2,p}).
$$

Each monomial $u^k$ in $a_p$ represents the $k$-th independent
$1$-cycle of the Seifert surface $F_p$.  To realise $T_{2,p}$
as a localized knot on $\Sigma_g$, each cycle needs a target
class in $H^1(\Sigma_g)$.  When $\deg_u a_p > g$, the
polynomial encodes more topology than the surface can hold ---
the surplus monomials have no geometric home.  This is the
**Chebyshev overflow**: the Iwahori--Hecke algebra knows the knot
doesn't fit, before any surface is chosen.

## The Chebyshev table

The Hecke recurrence $a_{n+1} = s \cdot a_n + a_{n-1}$ with
$a_0 = 0$, $a_1 = 1$ gives, for odd $p$, the following
polynomials in $u = s^2 = (q - q^{-1})^2$:

See [Table 2](#tbl:genus-filtration-ideal-table2-data).

($*$: $9 = 3^2$ is not prime but $T_{2,9}$ is the degree-$2$
tower of the trefoil.)

The saturation at $a_9$ (degree $4$) and the overflow at
$a_{11}$ (degree $5$) are not coincidences --- they are the
Chebyshev reflection of the Hecke completeness condition.
The completeness scan (Part 0) shows that $g = 4$ is the
minimum genus where all $5$ irreps are spanned.  The
Chebyshev degree at the boundary is $\deg_u a_9 = 4 = g$,
and $\deg_u a_{11} = 5 = g + 1$ is the first overflow.

## Part II: the genus-filtration ideal

*Define the genus-$g$ filtration ideal
$\mathfrak{I}_g \subset \mathbb{Z}[u]$ by*

$$
  \mathfrak{I}_g
  = 
  \bigl\{ f(u) \in \mathbb{Z}[u] : \deg f > g \bigr\}
  = 
  (u^{g+1}).
$$

*A torus knot $T_{2,p}$ admits a localized knot structure on
$\Sigma_g$ if and only if $a_p \notin \mathfrak{I}_g$, i.e.,
$\deg_u a_p \leq g$.*

For $g = 4$ (as determined by Hecke completeness):
$\mathfrak{I}_4 = (u^5)$.  Every $T_{2,p}$ with $p \geq 11$
has $a_p \in \mathfrak{I}_4$ because $\deg_u a_p \geq 5$.
The ideal $(u^5)$ catches all of them simultaneously: $u^k = u^{k-5} \cdot u^5 \in (u^5)$ for all $k \geq 5$.

## Part III: Yekutieli obstruction = leading coefficient

*The Yekutieli obstruction class
$\kappa(T_{2,p}) \in H^2(\Sigma_g, \mathbb{Z})$ is
the image of the leading monomial of $a_p$ under the
projection $\pi_g \colon \mathbb{Z}[u] \to \mathbb{Z}[u]/(u^{g+1})$:*

$$
  \kappa(T_{2,p})
  = 
  \begin{cases}
    0 & \text{if } (p-1)/2 \leq g \quad
      (\text{lifts: } a_p \text{ fits in } H^1(\Sigma_g)), \\[6pt]
    c_{(p-1)/2} \cdot [u^{(p-1)/2}] \neq 0 &
      \text{if } (p-1)/2 > g \quad
      (\text{obstructed: overflow}).
  \end{cases}
$$

*Since $c_{(p-1)/2} = 1$ for all odd $p$, the obstruction is
nonzero for every prime $p \geq 2g + 3 = 11$.*

<!-- FILE_END: genus-filtration-ideal.md -->

<!-- FILE_START: genus-filtration-interpretation.md -->
## Formal coordinates: unwinding $d_q^2 \neq 0$

The non-nilpotence $d_q^2 \alpha = q^{-1}(1-q^{-1}) \omega_V \wedge_q [\xi, \alpha]$
([categorical $d_q^2$](#prop:categorical-dq-squared)) provides
the differential-geometric mechanism.

Associate to $T_{2,p}$ the form
$\alpha_p = a_p(u) \cdot \omega_T \in \Omega^1(A)$, where
$\omega_T$ is the Hecke $1$-form (the $T$-component of the
Maurer--Cartan form on $H_2(q)$) and $u = s^2$ acts as a
grading parameter.

The weight decomposition assigns degree $k$ in $u$ to the
$k$-th Seifert cycle: $\alpha_p = \sum_{k=0}^{g_p} c_k  u^k \omega_T$, with $[\xi, u^k \omega_T] = k \cdot u^k \omega_T$
(the Lie derivative counts Seifert cycles).

Applying $d_q^2$ iteratively:

1. **At genus level $k \leq g$:** The component $c_k u^k \omega_T$
   maps under $\iota_*$ to a class in $H^1(\Sigma_g)$.
   The obstruction $d_q^2(c_k u^k \omega_T) \propto k \cdot \omega_V \wedge c_k u^k \omega_T$ is absorbed by
   the available $H^2(\Sigma_g)$ pairing --- it vanishes on the
   horizontal subcomplex ($\xi$-invariant forms project the
   surplus away).

2. **At genus level $k = g + 1$:** The component
   $c_{g+1} u^{g+1} \omega_T$ has no target in $H^1(\Sigma_g)$.
   The obstruction

   $$
     d_q^2(c_{g+1} u^{g+1} \omega_T)
     = 
     q^{-1}(1-q^{-1})(g+1) c_{g+1} u^{g+1}
     \omega_V \wedge_q \omega_T
   $$

   is a **nonzero class in $\Omega^2(A)$** that does not pair
   to zero against $H_2(\Sigma_g)$.  The coefficient
   $(g+1) \cdot c_{g+1} \cdot q^{-1}(1-q^{-1})$ is nonzero
   for all $q > 1$, and $c_{g+1} = 1$ (the leading Chebyshev
   coefficient is always $1$).

3. **The obstruction class.** The $d_q^2$-obstruction at level
   $g + 1$ descends to the Yekutieli class:

   $$
     \kappa(T_{2,p})
     = 
     (g+1) \cdot q^{-1}(1-q^{-1}) \cdot [\omega_V \wedge_q \omega_T]
      \in  H^2(\Sigma_g, \mathbb{Z})
   $$

   which is nonzero for $q \neq 1$.  At $q = 1$ (the classical
   limit), $d_q^2 = 0$ and all obstructions vanish ---
   consistent with classical de Rham cohomology having no
   genus constraint on embeddings.
<!-- FILE_END: genus-filtration-interpretation.md -->

<!-- FILE_START: genus-filtration-derivation-chain.md -->
## The derivation chain

The full argument is **non-circular**:

1. **QOU axioms** give $G = \mathrm{SU}_q(2)$ with braiding
   on $V_1^{\otimes n}$, producing $H_n(q)$.

2. **Strand count closure**: for any genus $g$, the constraint
   $(m-1)(s-1) \leq 2g$ with $m \geq 4$ contributes no new
   torus knots beyond those from $m \in \{2, 3\}$.  The
   relevant Iwahori--Hecke algebra is $H_2(q) \oplus H_3(q)$, with
   $5$ irreps.

3. **Hecke completeness**: the evaluation matrix of embeddable
   torus knots must have rank $5$.  Scanning from $g = 1$
   upward, the first genus where this holds is $g = 4$
   (with $6$ embeddable knots).

4. **Chebyshev overflow**: the polynomial $a_p(u)$ has degree
   $(p-1)/2$ in $u = s^2$.  At $g = 4$, the last fitting
   polynomial is $a_9$ (degree $4$); the first overflowing
   one is $a_{11}$ (degree $5$).

5. **Ideal**: the genus-filtration ideal $\mathfrak{I}_4 = (u^5)$
   is generated by the overflow.  Every $T_{2,p}$ with
   $p \geq 11$ has $a_p \in (u^5)$.

6. **Yekutieli**: the leading Chebyshev coefficient $c_{g+1} = 1$
   gives a nonzero obstruction $\kappa(T_{2,p}) \in H^2(\Sigma_4)$
   via $d_q^2 \neq 0$.

7. **Bring surface**: $\Sigma_4$ is the unique genus-$4$ curve
   with maximal symmetry ($S_5$), determined by the Descartes
   condition $\chi = 2 - 2g = -6$.

The Bring surface is a **consequence** of the Iwahori--Hecke algebra,
not an input.  The genus $g = 4$ emerges from representation
completeness; the surface $\Sigma_4$ is then identified by its
symmetry.
<!-- FILE_END: genus-filtration-derivation-chain.md -->

<!-- FILE_START: torus-embeddable-complete.md -->
The generator set $\mathcal{G}$
([finiteness of generators](#prop:torus-knot-generators)) is not only
a convenient choice — it is the *complete* list of torus knots
embeddable in the genus-$4$ fiber of the Bring's surface.

**Proposition.**
Let $T_{m,n}$ be a torus knot with $\gcd(m,n) = 1$ and $1 < m < n$.
Then $T_{m,n}$ embeds in the Seifert genus-$4$ surface $\Sigma_4$ of
the Bring's surface if and only if $(m,n)$ belongs to the set

$$
  \{(2,3),(2,5),(2,7),(2,9),(3,4),(3,5)\}.
$$

Together with the unknot $T_{1,0}$, these are the only torus knots
that can appear as localized knots in the Descartes universe.
<!-- FILE_END: torus-embeddable-complete.md -->

<!-- FILE_START: torus-embeddable-completeness-remark.md -->
**Remark.**
The completeness is purely number-theoretic: it depends only on the
Diophantine constraint $(m-1)(n-1) \leq 2g$ with a coprimality
condition. For any QOU with fiber genus $g'$, an analogous finite
enumeration determines the torus knot generator set. The Descartes
value $g = 4$ is the *smallest* genus that accommodates all three
lepton generations (requiring genera $1, 2, 3$) plus a non-trivial
quark sector (requiring $m = 3$ generators).
<!-- FILE_END: torus-embeddable-completeness-remark.md -->

<!-- FILE_START: bring-trefoil-cinquefoil-channel.md -->
*Lean sibling: $\mathbb{N}$ genus combinatorics and $\mathbb{C}$ for $\zeta_5$ (AGENTS.md §7c — the Gauss sum is the archimedean specialisation; the embedding combinatorics stay over $\mathbb{N}$).*

**Proposition (trefoil $+$ cinquefoil channel).** *In Bring's genus-$4$ Seifert
fibre $\Sigma_4$ — whose automorphism group is $\mathrm{Aut}(B) = S_5$, permuting
the five roots the Bring radical resolves — the chiral channel and the $\zeta_5$
symmetry are carried by two **distinct** torus knots, linked by the ambient $S_5$:*

- *the **chiral channel** is the **trefoil** $T_{2,3}$, of Seifert genus
  $g(T_{2,3}) = :val[bring_g_trefoil]{precision=0, witness=computations/bring-trefoil-cinquefoil-channel.witness.json}$
  — the colour-tube cubic's three sheets $(r,g,b)$ with $B_3 \twoheadrightarrow H_3$
  branch monodromy, i.e. the signed-content-zero block $V_{(2,1)}$
  ($c_\lambda = 0$, the $q$-Dirac kernel);*
- *the **$\zeta_5$ carrier** is the **cinquefoil** $T_{2,5}$, of Seifert genus
  $g(T_{2,5}) = :val[bring_g_cinquefoil]{precision=0, witness=computations/bring-trefoil-cinquefoil-channel.witness.json}$
  — the hyperelliptic quintic $\mathcal{X}_5 \colon y^2 = x^5 - 1$
  ([`def:hyperelliptic-quintic`](#def:hyperelliptic-quintic)) **embedded** (not
  covered) by the first Lagrange resolvent $w_1$ of the cyclic
  $\mathbb{Z}_5 \subset S_5$, its five branch points one $\mathbb{Z}_5$-orbit
  $\{1, \zeta_5, \dots, \zeta_5^4\}$ ([`prop:x5-z5-automorphism`](#prop:x5-z5-automorphism)).*

*Both embed in $\Sigma_4$ — genus $1$ and $2$ are $\le g(\Sigma_4) =
:val[bring_sigma4_genus]{precision=0, witness=computations/bring-trefoil-cinquefoil-channel.witness.json}$, within the complete embeddable
list $\{(2,3),(2,5),(2,7),(2,9),(3,4),(3,5)\}$ of
[`prop:torus-embeddable-complete`](#prop:torus-embeddable-complete) — and they
are distinct. The quadratic Gauss sum over the cinquefoil's $\mathbb{Z}_5$-orbit,*

$$
  g \;=\; \sum_{k=0}^{4} \zeta_5^{\,k^2},
  \qquad g^2 = 5,
  \qquad g = +\sqrt5,
$$

*is the unique source of $\zeta_5$'s irrationality over $\mathbb{Q}$, carried by
the resolvent $w_1$ (numerically $g \approx :val[bring_gauss_sum_sqrt5]{precision=5, witness=computations/bring-trefoil-cinquefoil-channel.witness.json}$).
The chiral residue's only available irrational scale on this configuration is
therefore $\sqrt5$, and its Bring constant is
$1/\sqrt5 \approx :val[bring_inv_sqrt5]{precision=5, witness=computations/bring-trefoil-cinquefoil-channel.witness.json}$.*

## Two torus knots, not one fibre

The phrasing "the chiral channel lives on the Bring chiral fibre with $\zeta_5$
symmetry" conflates two distinct structures. The colour-tube cubic
([`rem:color-tube-cubic`](#rem:color-tube-cubic)) is a **$3$-fold** datum — three
sheets, $B_3 \twoheadrightarrow H_3$, the trefoil. The $\zeta_5$ is a **$5$-fold**
datum — a cyclic subgroup of $S_5$, realised by the cinquefoil. They are not the
same knot, and the $5$-fold is *not* a covering of the $3$-fold: it is a second
torus knot embedded in the *same* $\Sigma_4$, and the ambient $S_5$ relates the
two. The $\sqrt5$ does not come from the cubic fibre; it comes from the
$\mathbb{Z}_5$-orbit Gauss sum carried by the resolvent $w_1$ that embeds the
quintic.

| structure | torus knot | Seifert genus | carried by |
|---|---|---|---|
| chiral channel ($3$-fold) | trefoil $T_{2,3}$ | $1$ | colour-tube cubic, $B_3 \twoheadrightarrow H_3$ |
| $\zeta_5$ symmetry ($5$-fold) | cinquefoil $T_{2,5}$ | $2$ | quintic $\mathcal{X}_5$ via the $w_1$ resolvent |

Both rows sit inside the single genus-$4$ fibre $\Sigma_4$; the third
column is exactly the descending chain
$g(T_{2,3}) = 1 < g(T_{2,5}) = 2 < g(\Sigma_4) = 4$.

## Relation to the H$_2$S residual

This proposition is the **provable geometric scaffold** beneath the H$_2$S
bond-angle conjecture ([`conj:h2s-angle-s3-braid-holonomy`](../molecular-construction/h2s-angle-s3-braid-holonomy.md)),
which observes the residual opening $\Delta\theta_{\mathrm{H_2S}}$ takes the Bring
$1/\sqrt5$ residual-mixing form. The scaffold fixes *which* $\sqrt5$ is available
(the quintic Gauss sum of the cinquefoil, $g^2 = 5$) and *why* the chiral channel
can see it (it is the trefoil sharing $\Sigma_4$ with the cinquefoil, $S_5$-linked).
What remains conjectural is only the **exact normalisation** — that the
$\zeta_5$-residue of the chiral $3p_z$ braid returns *precisely* the coefficient
$1/\sqrt5$ (equivalently, that the archimedean root of $g^2 = 5$ enters with the
observed weight). That monodromy/Reshetikhin–Turaev evaluation at $\zeta_5$ is the
conjecture's open content; the discrete scaffold here is established.

## Lean structure

`QOU.BringChiralCinquefoil` (sibling `bring-trefoil-cinquefoil-channel.lean`):

- `bring_trefoil_cinquefoil_channel` — the genera $g(T_{2,3}) = 1$,
  $g(T_{2,5}) = 2$, both $\le 4$, and $g(T_{2,3}) \ne g(T_{2,5})$ (two distinct
  knots in $\Sigma_4$). **Sorry-free** (`decide`).
- `zeta5_pow_five` — $\zeta_5^5 = 1$, the $5$-fold symmetry. **Sorry-free**
  (matching [`prop:x5-z5-automorphism`](#prop:x5-z5-automorphism)).
- `quintic_gauss_sum_sq_eq_five` — $\bigl(\sum_k \zeta_5^{k^2}\bigr)^2 = 5$.
  **Sorry-free** — proved from $\zeta_5$ primitivity
  (`Complex.isPrimitiveRoot_exp`) and the cyclotomic relation
  $1+\zeta_5+\zeta_5^2+\zeta_5^3+\zeta_5^4 = 0$ (`geom_sum_eq_zero`), reducing
  $\zeta_5^9 \mapsto \zeta_5^4$, $\zeta_5^{16} \mapsto \zeta_5$ and closing
  $g^2 - 5 = (4\zeta_5^3+8)(\zeta_5^5-1) + 4(1+\zeta_5+\zeta_5^2+\zeta_5^3+\zeta_5^4)$
  by `linear_combination` (\cite{washington1997} is the classical reference for
  the value). The archimedean *sign* $g = +\sqrt5$ — not the value $g^2 = 5$ — is
  the only deferred part, and it is the conjecture's open normalisation content.
<!-- FILE_END: bring-trefoil-cinquefoil-channel.md -->

<!-- FILE_START: generation-completeness.md -->
The embeddability closure
([embeddability closure](#thm:embeddability-closure)) shows that the
generation scheme does not produce knots *outside* genus $4$.  The
converse question is whether it produces *all* knots inside genus $4$.
The answer is yes: every knot embeddable in the Bring's surface is
reachable from $\mathcal{G}$ by Skein operations alone.

**Theorem (Generation completeness).**
Let $K$ be any knot with Seifert genus $g(K) \leq 4$.  Then $K$ is
reachable from the generator set $\mathcal{G}$
([finiteness of generators](#prop:torus-knot-generators)) by a finite
sequence of Skein crossing changes.  In particular, the generation
scheme
([knot-particle generation](#def:knot-particle-generation)) applied to
$\mathcal{G}$ produces every knot type that admits a localized knot
structure in the Descartes universe.
<!-- FILE_END: generation-completeness.md -->

<!-- FILE_START: generation-completeness-interpretation.md -->
This remark interprets the
[generation completeness theorem](#thm:generation-completeness).

**Physical content of the spectral filter.**
The physical content of the Skein resolution is the projection onto the
submodule spanned by knots with $g(K) \leq 4$.

**Physical interpretation.**
The completeness theorem means the Descartes universe does not
arbitrarily select which knots become particles.  Every topologically
admissible knot type is physically realizable — the $7$ generators
and the Skein algebra are sufficient to span the entire embeddable
spectrum.  The particle dictionary
([knot formula table](#rem:knot-formula-table)) names only the
phenomenologically prominent knots (trefoil, figure-eight, etc.),
but the theorem guarantees that the thousands of higher-crossing
embeddable knots also populate the spectrum, appearing as massive,
short-lived resonances in the Skein decomposition of hadronic
processes.
<!-- FILE_END: generation-completeness-interpretation.md -->

