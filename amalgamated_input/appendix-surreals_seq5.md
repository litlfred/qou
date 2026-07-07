<!-- FILE_START: surreal-construction-grading-intro.md -->
Conway's construction grades the surreals by birthday. This section connects the grading to the brane-tower level filtration.
<!-- FILE_END: surreal-construction-grading-intro.md -->

<!-- FILE_START: birthday-grading.md -->
The birthday grading provides a coarse "how transfinite" depth gauge for morphisms in surreal-enriched categories. It stratifies formal parameters into nested levels of infinitesimal and transfinite resolution. Statements with all hom-coefficients of birthday $< \omega$ involve only dyadic rationals. Birthday-$\leq \omega$ statements include limit reals and first-order infinitesimals. Birthday $> \omega$ statements use named infinities like $\omega$ itself or transseries terms like $\log \omega$.

Let $K$ be a real-closed field extending $\mathbb{R}$ (typically $K = \mathbf{No}$, Conway's surreal numbers). Every element $x \in \mathbf{No}$ has a canonical **birthday** $b(x) \in \mathrm{Ord}$. This is the least ordinal stage at which $x$ is constructed in Conway's recursive $\{L \mid R\}$ presentation [@conway1976]. Equivalently, $b(x)$ is the length of the sign-sequence representation for $x$ [@gonshor1986]:

$$
  b(0) = 0, \qquad
  b(n) = n \text{ for } n \in \mathbb{N}, \qquad
  b(\omega) = \omega, \qquad
  b(1/2) = 2, \qquad
  b(\pi) = \omega, \qquad
  b(\varepsilon) = \omega.
$$

The birthday function refines the archimedean norm. Distinct reals $x, y \in \mathbb{R} \subset \mathbf{No}$ have $b(x), b(y) \leq \omega$. The elements $\varepsilon$, $\omega$, and $\omega^2$ have progressively larger birthdays.

## Example: Substrate Parameter at $q = 1 + \varepsilon$

Consider $q = 1 + \varepsilon$ for an infinitesimal $\varepsilon \in \mathbf{No}$ with $b(\varepsilon) = \omega$. Its sign sequence $(+, -, -, -, \ldots)$ has length $1 + \omega = \omega$. The associated parameters resolve as follows:

- $c_q = 1/(q - 1) = 1/\varepsilon = \omega$ has birthday $\omega$.
- $\hbar_q = (q-1)/q = \varepsilon(1 + \varepsilon)^{-1}$ has birthday $\omega$.
- $d_H(q) = (2q-1)^2/q^3 = (1 + 2\varepsilon)^2(1 + \varepsilon)^{-3}$ has birthday $\omega$.

Expressions rational in $q$ evaluated at $q = 1 + \varepsilon$ remain in the birthday-$\leq \omega$ stratum. They embed into the Laurent-series field $\mathbb{R}(\!(\varepsilon)\!)$. The standard-part map determines the distinction between finite and infinitesimal within this stratum. The birthday alone does not distinguish them, as limit reals like $\pi$ also have birthday $\omega$.

## Definition

Let $\mathbf{C}$ be a $K$-linear category (enriched over $K$-modules). A **birthday grading** on $\mathbf{C}$ is an ordinal-indexed filtration of each hom-space:

$$
  \mathrm{Hom}_{\mathbf{C}}(X, Y)_{\leq \alpha}
  \;=\; \bigl\{ f \in \mathrm{Hom}_{\mathbf{C}}(X, Y) :
         \text{every coefficient of } f \text{ has birthday} \leq \alpha \bigr\}.
$$

This filtration satisfies three properties:

1. **Exhaustiveness**: $\bigcup_\alpha \mathrm{Hom}_{\mathbf{C}}(X, Y)_{\leq \alpha} = \mathrm{Hom}_{\mathbf{C}}(X, Y)$.
2. **Composition**: If $f \in \mathrm{Hom}(X,Y)_{\leq \alpha}$ and $g \in \mathrm{Hom}(Y,Z)_{\leq \beta}$, then $g \circ f \in \mathrm{Hom}(X,Z)_{\leq \alpha \oplus \beta}$ (where $\oplus$ is the natural sum of ordinals).
3. **Monoidality**: If $\mathbf{C}$ is monoidal, $f \otimes g \in \mathrm{Hom}(X \otimes X', Y \otimes Y')_{\leq \alpha \oplus \beta}$.

## Archimedean Sub-category

The sub-category defined by $b(f) \leq \omega$ forms the **archimedean-coefficient sub-category**. Its morphisms have coefficients that are real numbers or bounded infinitesimals. For $\mathbf{C} = \mathrm{Rep}_{\mathbf{No}}(\mathrm{SU}_q(2))$ with $q \in \mathbb{R} \subset \mathbf{No}$, this recovers $\mathrm{Rep}_{\mathbb{R}}(\mathrm{SU}_q(2))$. The arithmetic of $\mathbf{No}$ restricted to birthday $\leq \omega$ coincides with $\mathbb{R}$ exactly on the archimedean part.

The relaxed axioms in this appendix ([infinitesimal Frobenius](#conj:infinitesimal-frobenius)) allow corrections of the form $\mathrm{id} + O(\varepsilon)$. These corrections live at birthday $\leq \omega$ but are distinguished from the classical $\mathrm{id}$ by having a non-zero standard part for the $\varepsilon$-coefficient.
<!-- FILE_END: birthday-grading.md -->

<!-- FILE_START: hoefsmit-is-surreal-construction.md -->
The Hoefsmit seminormal form
([Hoefsmit seminormal form](#prop:hoefsmit-seminormal-form))
diagonalises the Iwahori--Hecke algebra $H_n(q)$ acting on
$V^{\otimes n}$ along a tower of Young--Jucys--Murphy elements
indexed by standard tableaux. At each step, a Hecke generator $\sigma_i$
splits a tableau-vector into two eigencomponents:

- the **symmetric** ($q$-eigen) component, corresponding to the
  tableau where boxes $i$ and $i+1$ lie in the same row;
- the **antisymmetric** ($-q^{-1}$-eigen) component, corresponding
  to the tableau where they lie in the same column.

This is structurally identical to Conway's recursive surreal
construction.

## Statement

Let $\mathrm{Tab}(\lambda)$ denote the set of standard tableaux of
shape $\lambda$, viewed as the vertex set of a tree $\mathcal{T}_n$
whose edges record the Young--Jucys--Murphy ordering. Let
$\mathbf{No}_{= n}^{\mathrm{dy}}$ denote the set of dyadic surreals
of birthday *exactly* $n$ (equivalently, sign sequences of length
$n$).

**Cardinality note.** The number of two-rowed standard tableaux of
size $n$ is $\binom{n}{\lfloor n/2 \rfloor}$; the number of
dyadic surreals of birthday exactly $n$ is $2^n$.  These counts do
not match (e.g., $n = 3$ gives $3$ tableaux versus $8$ surreals), so
the map below is an **injective embedding**, not a bijection of
forests.

There is a canonical injective embedding

$$
  \Phi : \bigsqcup_{\lambda \vdash n,\, \ell(\lambda) \leq 2}
    \mathrm{Tab}(\lambda)
   \hookrightarrow
  \mathbf{No}_{\leq n}^{\mathrm{dy}}
$$

(taking values in dyadic surreals of birthday $\leq n$) such that:

1. The empty tableau at $n = 0$ and the singleton tableau at
   $n = 1$ both map to the surreal $0$ (the singleton's sign
   sequence is empty, of length $n - 1 = 0$).  For $n \geq 2$ the
   one-row tableau $(n)$ maps to a non-zero value determined by
   its sign sequence (see item 2).
2. Each YJM-edge $t \to t'$ in the tableau forest corresponds to a
   unique sign-sequence extension $s \to s\!\cdot\! +$ (symmetric
   channel: new box in the top row) or $s \to s\!\cdot\! -$
   (antisymmetric channel: new box in the bottom row).  The sign
   sequence of a size-$n$ tableau has length $n - 1$ (no choice at
   the first box placement).
3. The birthday $b(\Phi(t))$ is bounded by the length of the
   sign sequence, i.e., by $n - 1$.  Surreals in the image are
   therefore of birthday $\leq n - 1$; the complement of the image
   in $\mathbf{No}_{\leq n}^{\mathrm{dy}}$ consists of
   "non-tableau" dyadic rationals not reachable by YJM-extension
   from a two-rowed shape.
## Corollaries

This identification has several immediate consequences:

1. **Sign-sequence braid invariant** is well-defined and lives
   in $\mathbf{No}_{\leq c(\beta)}^{\mathrm{dy}}$ for braid $\beta$
   of crossing number $c(\beta)$.

2. **Birthday refines crossing number**:
   $b(\mathrm{surr}(\beta, t)) \leq c(\beta)$, with equality for
   reduced braids.

3. **Hoefsmit factorisation = Conway construction**: the closed
   formula for $\rho_\lambda(\sigma_i)$ as a $2 \times 2$ matrix
   in YJM coordinates is *exactly* the recursive surreal recipe
   $x = \{x^- \mid x^+\}$ with the eigenvalue ratio
   $q : -q^{-1}$ determining the position of $x$ between $x^-$
   and $x^+$.

4. **The Jones polynomial $J_K(q)$** can be re-expressed as a
   weighted sum over surreal sign sequences (rather than over
   tableaux), exposing a previously-hidden combinatorial
   structure
   ([Jones polynomial birthday refinement](#conj:jones-birthday)).

5. **Knot complexity** acquires an honest ordinal-valued
   refinement: knots of unbounded crossing number live at
   birthdays approaching $\omega$.

## Significance

This is the central observation of the appendix. The QOU paper
already uses the Hoefsmit seminormal form as its
algebraic-combinatorial backbone (it powers the mass formula,
the $\mathcal{Q}$-value derivations, the spectral decomposition
on $\Sigma_g$). What this proposition shows is that the same
backbone, viewed differently, is a literal instance of Conway's
surreal-number construction.

The surreal lift of QOU is therefore not a *new* structure
imposed on the paper; it is a different *language* for what
Hoefsmit already provides.
<!-- FILE_END: hoefsmit-is-surreal-construction.md -->

<!-- FILE_START: sign-sequence-of-braid.md -->
A surreal number $x \in \mathbf{No}$ admits a canonical
**sign-sequence presentation** [@gonshor1986]: a function

$$
  s_x : \alpha \to \{+, -\}
$$

for some ordinal $\alpha = b(x)$ (its birthday). The sequence
encodes Conway's $\{L \mid R\}$ construction step-by-step: at each
ordinal stage $\beta < \alpha$, the sign $s_x(\beta) = +$ means
"$x$ is the rightmost option among those constructed so far",
and $s_x(\beta) = -$ means "leftmost option".

Hecke generators have two eigenvalues, $q$ (symmetric channel)
and $-q^{-1}$ (antisymmetric channel) — see
[Hoefsmit seminormal form](#prop:hoefsmit-seminormal-form). This
**binary choice at each level** is exactly the sign-sequence
data, and it gives a canonical functor from braid words to
surreals.

## Construction

Let $V$ be the fundamental representation of $\mathrm{SU}_q(2)$ and
let $\beta = \sigma_{i_1}^{\epsilon_1} \cdots \sigma_{i_k}^{\epsilon_k}$
be a braid word in $B_n$ (with $\epsilon_j \in \{+1, -1\}$). The
Hecke representation $\rho_n : B_n \to H_n(q)$ sends each
$\sigma_i^{\pm 1}$ to $\sigma_i^{\pm 1}$.

Choose a **standard tableau** $t$ of shape $\lambda \vdash n$ with
$\ell(\lambda) \leq 2$ (the partitions appearing in the
$q$-Schur--Weyl decomposition). The Hoefsmit seminormal vector
$v_t \in S_\lambda$ at $t$ is an eigenvector of every
Young--Jucys--Murphy element. The braid $\beta$ acts on $v_t$
by:

1. successively decomposing $\rho(\sigma_{i_j}^{\epsilon_j})\, v_{t_j}$
   as $a_j \cdot q^{\epsilon_j}\, v_{t_j^+} + b_j \cdot
   (-q^{-\epsilon_j})\, v_{t_j^-}$ (sum of the two eigencomponents
   in the relevant pair of standard tableaux);
2. recording $s_j = +$ if the symmetric ($q$-eigen) component is
   chosen, $s_j = -$ if the antisymmetric ($-q^{-1}$-eigen)
   component is chosen.

The resulting sign sequence $s = (s_1, s_2, \ldots, s_k) \in
\{+, -\}^k$ defines a finite-birthday surreal

$$
  \mathrm{surr}(\beta, t)
   := \mathrm{Gonshor}(s) \in \mathbf{No}
$$

where $\mathrm{Gonshor}: \{+, -\}^* \to \mathbf{No}$ is the
canonical sign-sequence-to-surreal map [@gonshor1986]: e.g.
$+ \mapsto 1$, $- \mapsto -1$, $++ \mapsto 2$, $+- \mapsto 1/2$,
$-+ \mapsto -1/2$, $-- \mapsto -2$, etc.

## Functoriality

For each fixed standard tableau $t$, the assignment

$$
  \mathrm{surr}(-, t) : B_n \to \mathbf{No}
$$

is a **multiplicative monoid map** in the following sense: writing
$\beta_1 \beta_2$ for the product braid,
$\mathrm{surr}(\beta_1 \beta_2, t)$ is computed by first applying
$\beta_2$'s sign sequence at $t$ to obtain a new tableau $t'$,
then concatenating with $\beta_1$'s sign sequence at $t'$. This
is the sign-sequence concatenation rule, which corresponds under
$\mathrm{Gonshor}$ to a canonical operation on $\mathbf{No}$ (the
*concatenation product* of Gonshor [@gonshor1986]).

The dependence on $t$ is mild: changing tableau permutes the
sign sequence by a Young--Jucys--Murphy permutation, which is a
well-defined ordinal action on $\mathbf{No}$. We can quotient by
this action to obtain a tableau-independent functor

$$
  \widetilde{\mathrm{surr}} : B_n \longrightarrow \mathbf{No} / \sim,
$$

at the price of a quotient on the target.

## Birthday and crossing number

The sign sequence has length equal to the number of crossings in
$\beta$, so $b(\mathrm{surr}(\beta, t)) \leq c(\beta)$ where
$c(\beta)$ is the crossing number. Equality holds when the
braid is reduced (no Markov-trivial crossings). This gives a
**clean refinement of the crossing-number invariant** by an
ordinal-valued (and hence in particular surreal-valued)
quantity:

$$
  c(\beta)  \leadsto  \mathrm{surr}(\beta, t) \in \mathbf{No},
  \qquad b(\mathrm{surr}(\beta, t)) \leq c(\beta).
$$

## Significance

The sign sequence carries strictly more information than the
crossing number: it records *which* eigenchannel is chosen at
each crossing, so distinct braids with the same crossing number
generally give distinct surreals. Surrealisation is therefore a
candidate **stronger braid invariant** valued in
$\mathbf{No} / \sim$.

Bridge to existing structure:

- It is the precise sense in which "Hoefsmit seminormal form is the
  surreal $\{L \mid R\}$ construction"
  ([Hoefsmit is surreal](#prop:hoefsmit-is-surreal-construction)).
- It refines the Jones polynomial: $J_K(q)$ is the Markov trace
  averaged over tableau choices, while $\mathrm{surr}(\beta, t)$ is
  the un-averaged trajectory through the Hoefsmit eigenspace tree
  ([Jones polynomial birthday refinement](#conj:jones-birthday)).
- It places knot complexity on a transfinite scale: knots with
  arbitrarily long sign sequences live at higher birthdays than
  any classical real-valued invariant can reach.
<!-- FILE_END: sign-sequence-of-braid.md -->

<!-- FILE_START: jones-birthday.md -->
The Jones polynomial $J_K(q) \in \mathbb{Z}[q^{\pm 1/2}]$ is the
Markov trace $\mathrm{tr}_M(\rho_n(\beta))$ of the Hecke
representation of any braid word $\beta$ whose closure is the
oriented link $K$. The Markov trace is computed by summing
contributions from every standard tableau $t$ of every two-rowed
shape $\lambda \vdash n$.

By [Hoefsmit-is-surreal-construction](#prop:hoefsmit-is-surreal-construction),
each tableau $t$ corresponds to a finite-dyadic surreal
$\Phi(t) \in \mathbf{No}$ of birthday $\leq n$. This suggests
that the Jones polynomial admits a **birthday refinement**: a
finer invariant that records contributions stratified by the
birthday of the underlying surreal sign sequence.

## Conjecture

There exists a refinement

$$
  \widetilde{J}_K \in \mathbb{Z}[q^{\pm 1/2}]^{\mathrm{Ord}}
$$

— a function from ordinals to Laurent polynomials in $q^{1/2}$ —
satisfying:

1. **Recovery of Jones**: the sum
   $\sum_\alpha \widetilde{J}_K(\alpha) = J_K(q)$ converges to the
   classical Jones polynomial when summed over all birthdays.

2. **Birthday locality**: $\widetilde{J}_K(\alpha)$ depends only on
   tableau contributions of YJM depth $\leq \alpha$.

3. **Strict refinement**: there exist knots $K_1, K_2$ with the
   same Jones polynomial $J_{K_1}(q) = J_{K_2}(q)$ but distinct
   birthday refinements
   $\widetilde{J}_{K_1} \neq \widetilde{J}_{K_2}$.

If (3) holds, $\widetilde{J}_K$ is a **strictly stronger invariant
than the Jones polynomial**, contradicting the classical view
that all braid-word information is collapsed by the Markov
trace.

## Plausibility

The Jones polynomial loses information for two reasons:

1. **Markov-trace averaging**: contributions from distinct tableaux
   $t, t'$ of the same shape $\lambda$ are added; the trace cannot
   distinguish them.
2. **Tableau-shape averaging**: contributions from distinct shapes
   are weighted by quantum dimensions $\dim_q(\lambda)$.

The birthday refinement preserves the first averaging (still trace-
typed) but stratifies by *YJM depth*, which is a finer invariant
than the shape. So contributions from "early" symmetric channels
($q$-eigen choices at low YJM steps) are separated from
contributions from "late" symmetric channels.

There is a precedent: the **Khovanov homology** and other
categorifications of the Jones polynomial are strictly stronger
invariants. The birthday refinement is *not* a categorification
(it produces numbers, not chain complexes), but it factors
similarly: both refinements expose previously hidden tableau-level
data.

## Criteria for proof or disproof

- **Proof**: produce two knots with identical Jones polynomials
  and distinct birthday refinements, computed via Hoefsmit's
  matrix entries at each YJM step.
- **Disproof**: show that the YJM-depth filtration of any tableau
  contributes only via its endpoint (the shape $\lambda$), not its
  trajectory. This would collapse the refinement to the Jones
  polynomial.

The Conway--Kinoshita pair $(11n34, 11n42)$ is a classical
example of two knots distinguished by Khovanov homology but not by
the Jones polynomial. The birthday refinement could be tested
against this pair.

## Open problem

The conjecture is open. The Hoefsmit eigenchannel data is
explicit (Hoefsmit gives closed formulas), so the refinement is
computable; the question is whether it is non-trivial.

## Proof strategy

A direct attack (computational, no new theory):

1. **Compute** $\widetilde{J}_K$ for the smallest pair of knots
   sharing a Jones polynomial — Conway's $11n34, 11n42$
   (Khovanov-distinguishable, $J$-indistinguishable). Both are
   eleven-crossing knots, so the YJM tableau trees have depth
   $\leq 11$.

2. **Sum over tableau trajectories**: for each YJM-extension path
   $\pi$ of length 11 in either knot, compute the Hoefsmit matrix
   product along $\pi$ and convert to a sign sequence via
   `signSequenceOfBraid`. Compute the Gonshor surreal of each path.

3. **Aggregate by birthday**: group contributions by
   $b(\mathrm{Gonshor}(\pi))$ and sum coefficients. The result is
   $\widetilde{J}_K$.

4. **Compare**: if $\widetilde{J}_{11n34} \neq \widetilde{J}_{11n42}$
   the conjecture (existence of a strict refinement) is established
   by a single example.

**Required infrastructure**:
- Hoefsmit matrix entries for $H_{11}(q)$ (closed-form, known).
- `gonshor` map for finite sign sequences (provided by
  `QOU.AppendixSurreals.gonshor`).
- A Python/Lean script computing matrix products along YJM paths.

**Falsification path**: prove that the Hoefsmit-trajectory sum
factors through the YJM endpoint (= shape $\lambda$), so the
birthday refinement equals the partition-summed Markov trace,
which is the Jones polynomial. This would reduce
$\widetilde{J}_K$ to $J_K$ identically.

**Provability assessment**: computational verification feasible
in days, not months. Lean formalisation requires only the
already-built `gonshor` plus a Hoefsmit-matrix module.
<!-- FILE_END: jones-birthday.md -->

