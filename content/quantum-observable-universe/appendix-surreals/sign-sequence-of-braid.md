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
$|t\rangle \in S_\lambda$ at $t$ is an eigenvector of every
Young--Jucys--Murphy element. The braid $\beta$ acts on $|t\rangle$
by:

1. successively decomposing $\rho(\sigma_{i_j}^{\epsilon_j}) |t_j\rangle$
   as $a_j \cdot q^{\epsilon_j} |t_j^+\rangle + b_j \cdot
   (-q^{-\epsilon_j}) |t_j^-\rangle$ (sum of the two eigencomponents
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

## Why this is interesting

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
