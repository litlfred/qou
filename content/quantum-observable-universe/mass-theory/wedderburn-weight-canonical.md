**Proposition (Canonical Wedderburn-block weight; BW and LP
scalings).** *The BW mass coefficient and the LP shadow-price are
both scalings, valid for every $\lambda \vdash n$, of a single
combinatorial quantity — the canonical
**q-deformed Wedderburn-block weight***

$$
  \tilde w_\lambda
  \;:=\;
  \frac{\dim_q(\lambda)^2}{[n]_q!}
  \;\in\;
  \mathbb{Q}(q),
$$

*where $\dim_q(\lambda)$ is the **quantum hook-length dimension**
defined by the $q$-deformed Frame–Robinson–Thrall formula*

$$
  \dim_q(\lambda) \;=\; \frac{[n]_q!}{\displaystyle\prod_{x \in \lambda} [h_x]_q},
  \qquad
  [k]_q \;=\; \frac{q^k - q^{-k}}{q - q^{-1}},
$$

*with $h_x$ the hook length of cell $x$ in $\lambda$, and
$[n]_q! = \prod_{k=1}^{n}[k]_q$ is the $q$-factorial. At $q = 1$,
$\dim_q(\lambda) \to d_\lambda := n! / \prod_x h_x$ (classical
Frame–Robinson–Thrall), recovering the $S_n$-irrep dimension.
The convention is universal across this paper — the same
$\dim_q$ appears in
[`hecke_n6_frobenius_codim`](frobenius-codim-universal.lean),
[`hecke_n7_frobenius_codim`](frobenius-codim-universal.lean), and
[`hecke_n8_frobenius_codim`](frobenius-codim-universal.lean) Lean
closures, in the Wenzl-bridge $y_\lambda$ closed form
([y-lambda-closed-form-wenzl-bridge](#prop:y-lambda-closed-form-wenzl-bridge)),
and in the q-deformed Wedderburn-block weight $\tilde w_\lambda = \dim_q(\lambda)^2 / [n]_q!$
above. Two of the three named coefficient forms below are immediate
scalings of $\tilde w_\lambda$ for **all** $\lambda$; the third (the
Markov coefficient $y_\lambda$) is related to $\tilde w_\lambda$ **only on
self-conjugate $\lambda$** and otherwise has its own Wenzl
hook–content closed form:*

| Named form | Identity | Domain | Where used |
|------------|----------|--------|------------|
| **BW form** | $\beta_\lambda \;=\; -\tfrac12\,\tilde w_\lambda$ | all $\lambda$ (definitional) | mass coefficient ([hook-weight-derivation](#prop:hook-weight-derivation)) |
| **LP shadow-price** | $C_\lambda \;=\; \tilde w_\lambda \cdot h/2$, $h := q - q^{-1}$ | all $\lambda$ (definitional) | nuclear operator-selection LP dual ([mass-coefficient-shadow-price](#prop:mass-coefficient-shadow-price)) |
| **Wenzl-bridge (self-conjugate case)** | $y_\lambda \;=\; \tilde w_\lambda$ when $\kappa_\lambda = 0$, $\kappa_\lambda := \sum_{x\in\lambda} c(x)$ | self-conjugate $\lambda$ only | sign-tracked closed form ([y-lambda-closed-form-wenzl-bridge](#prop:y-lambda-closed-form-wenzl-bridge)) |

*For self-conjugate partitions ($\kappa_\lambda = 0$), the
Wenzl-bridge form reduces to $y_\lambda = \tilde w_\lambda$ — verified
symbolically for $\lambda = (2,2)$ and $\lambda = (3,2,1)$ by the
P1.3a equivalence audit
([witness](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/docs/audits/-p1-3a-bw-equivalence.witness.json)).
The BW and LP forms are scalings of the same canonical $\tilde w_\lambda$
for every $\lambda$; the Wenzl-bridge identification with
$\tilde w_\lambda$ holds **only** on the self-conjugate stratum. For
non-self-conjugate $\lambda$, $y_\lambda$ is given by Wenzl's
hook–content closed form [wenzl1988] and is, in general, distinct
from $(-1)^{\kappa_\lambda} \tilde w_\lambda$ — see the
[non-self-conjugate empirical witness](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/probe-wedderburn-weight-scheme.witness.json),
which records $|y_\lambda / \tilde w_\lambda|$ ratios from $0.14$ to
$2.54$ at $q_0$ for $n \in \{2, 3\}$, confirming the two are
distinct weight families away from self-conjugate $\lambda$.*

## Why $\tilde w_\lambda$ is canonical

The Wedderburn–Artin decomposition
([Wedderburn mass formula](#thm:wedderburn-mass-formula))
identifies the Hecke algebra $H_n(R, q)$ with a direct sum of
matrix blocks indexed by partitions $\lambda \vdash n$:

$$
  H_n(R, q) \;\cong\; \bigoplus_{\lambda \vdash n} M_{f_\lambda}\bigl(\mathbb{Q}(q)\bigr),
  \qquad
  f_\lambda \;=\; \dim V_\lambda \;\in\; \mathbb{Z}_{>0}
$$

(the $\mathbb{Q}(q)$-dimensions $f_\lambda$ are the classical
$S_n$-irrep dimensions; the algebra is a flat deformation of
$\mathbb{Q}S_n$). The combinatorial weight

$$
  \tilde w_\lambda \;=\; \frac{\dim_q(\lambda)^2}{[n]_q!}
$$

is the **q-deformed Wedderburn-block weight** — the
$\mathbb{Q}(q)$-rational analogue of the classical block-size
fraction $f_\lambda^2 / n!$. It is determined by the algebra alone,
before any choice of mass / LP convention, and it specialises to
the classical Plancherel measure
([prop:plancherel-weight-boundedness](#prop:plancherel-weight-boundedness))
at $q = 1$.

The Markov trace on $H_n(R, q)$
([Jones–Markov](#thm:jones-markov-trace))
decomposes along the blocks as

$$
  \mathrm{tr}_M
  \;=\;
  \sum_{\lambda \vdash n} y_\lambda(q) \cdot \chi_\lambda,
$$

where $\chi_\lambda$ is the Hecke-irrep character on the
$\lambda$-block and $y_\lambda(q)$ is the **Markov coefficient**
given by Wenzl's hook–content closed form [wenzl1988]
([y-lambda-closed-form-wenzl-bridge](#prop:y-lambda-closed-form-wenzl-bridge)).
For self-conjugate $\lambda$ the Markov coefficient and the
Wedderburn-block weight coincide, $y_\lambda(q) = \tilde w_\lambda$; for
non-self-conjugate $\lambda$ they are distinct.

## The three named scalings — derivations

### BW form: $\beta_\lambda = -\tfrac12 \tilde w_\lambda$

Mass coefficients in the BW formula carry a sign and a factor of
$\tfrac12$:

- The sign is fixed by the channel structure (sym/std/alt
  alternation in [Wedderburn mass formula](#thm:wedderburn-mass-formula)).
- The $\tfrac12$ comes from the Wigner $T=0$ doubling convention:
  each $\mathfrak{p}\mathfrak{n}$ crossing uses $c=2$ in the hook
  channel, and $\beta$ compensates
  ([hook-weight-derivation](#prop:hook-weight-derivation)).

So $\beta_\lambda = -\tfrac12 \tilde w_\lambda$ is the BW-ready mass
coefficient — what one multiplies by $m_e$ to get a MeV-scale
correction.

### LP shadow-price: $C_\lambda = \tilde w_\lambda \cdot h/2$

In the nuclear operator-selection LP
([mass-coefficient-shadow-price](#prop:mass-coefficient-shadow-price)),
each partition $\lambda$ contributes a Frobenius-positivity
constraint, and its dual variable (shadow price) is

$$
  C_\lambda
  \;=\;
  \tilde w_\lambda \cdot \frac{h}{2},
  \qquad h = q - q^{-1}.
$$

The factor $h$ is the Hecke-generator scalar
$\sigma_i^2 = h\,\sigma_i + 1$; it appears because the LP
constraint involves Hecke-generator action, not pure Markov
trace.

### Wenzl-bridge on the self-conjugate stratum: $y_\lambda = \tilde w_\lambda$ when $\kappa_\lambda = 0$

The Wenzl-bridge closed form
([y-lambda-closed-form-wenzl-bridge](#prop:y-lambda-closed-form-wenzl-bridge))
tracks the **content sum**

$$
  \kappa_\lambda
  \;:=\;
  \sum_{x \in \lambda}\,c(x)
  \;=\;
  \sum_{x = (i,j) \in \lambda}\,(j - i).
$$

For self-conjugate $\lambda$ (those with $\lambda = \lambda'$),
$\kappa_\lambda = 0$ and the Markov coefficient coincides with
the Wedderburn-block weight: $y_\lambda = \tilde w_\lambda$.

For non-self-conjugate $\lambda$, $y_\lambda$ and $\tilde w_\lambda$ are
**distinct**: $y_\lambda$ is given by Wenzl's content-distance
closed form [wenzl1988] and is not, in general, a sign multiple of
$\tilde w_\lambda$. The empirical witness
[`probe-wedderburn-weight-scheme.witness.json`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/probe-wedderburn-weight-scheme.witness.json)
records $|y_\lambda / \tilde w_\lambda|$ ratios ranging from $\approx 0.14$
to $\approx 2.54$ at $q_0$ for $n \in \{2, 3\}$, confirming that
Markov $y_\lambda$ and Wedderburn $\tilde w_\lambda$ are distinct weight
families away from the self-conjugate stratum.

## Symbolic verification (self-conjugate stratum)

The BW and LP scaling identities — and the Wenzl-bridge identity
restricted to the self-conjugate stratum — are verified at the
level of explicit $\mathbb{Q}(q)$ rational expressions for the
partitions $\lambda = (2,2) \vdash 4$ (used in BW-8 / BW-11 hook
terms) and $\lambda = (3,2,1) \vdash 6$ (Wigner-2 BW-7). Sympy
simplifies the differences to $0$ exactly. Both partitions are
self-conjugate, so the witness establishes the BW/LP identities in
general (definitional) and the Wenzl-bridge identity on the
self-conjugate stratum. Witness:
[`docs/audits/-p1-3a-bw-equivalence.witness.json`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/docs/audits/-p1-3a-bw-equivalence.witness.json).

## Why each context picks a different form

| Context | Form chosen | Reason |
|---------|-------------|--------|
| Mass formula | $\beta_\lambda = -\tfrac12 \tilde w_\lambda$ | Already includes the sign and Wigner $\tfrac12$ doubling needed to multiply by $m_e$ and produce a MeV correction. |
| Operator-selection LP | $C_\lambda = \tilde w_\lambda h/2$ | LP duality on the Frobenius-positivity constraint involves the Hecke generator $\sigma_i$ with eigenvalue $h$; the dual variable inherits the $h$ factor. |
| Sign-tracked closed form (self-conjugate) | $y_\lambda = \tilde w_\lambda$ when $\kappa_\lambda = 0$ | On self-conjugate $\lambda$, the Markov coefficient agrees with the Wedderburn-block weight up to the (trivial) content-sum sign. For non-self-conjugate $\lambda$ use Wenzl's hook–content closed form ([y-lambda-closed-form-wenzl-bridge](#prop:y-lambda-closed-form-wenzl-bridge)) directly. |

The BW and LP forms are scalings of $\tilde w_\lambda$ for every
$\lambda$ (definitional). The Wenzl-bridge identification with
$\tilde w_\lambda$ is exact on the self-conjugate stratum; off that
stratum, the Markov coefficient $y_\lambda$ is a distinct weight
family and must be obtained from the Wenzl closed form.

## Consequences for downstream use

- Any new BW mass coefficient or LP shadow-price at a new
  partition can be derived in three steps: (1) compute $\tilde w_\lambda$
  from $\dim_q(\lambda)$ and $[n]_q!$; (2) apply the BW or LP
  scaling identity natural in the surrounding context; (3) cite
  this proposition for the rationale.
- A Markov coefficient $y_\lambda$ at a non-self-conjugate
  $\lambda$ must come from the Wenzl closed form
  ([y-lambda-closed-form-wenzl-bridge](#prop:y-lambda-closed-form-wenzl-bridge)),
  not from a sign of $\tilde w_\lambda$.
- Cross-checks between BW and LP forms reduce to a one-line
  scaling identity. Cross-checks between Markov $y_\lambda$ and
  Wedderburn $\tilde w_\lambda$ are non-trivial off the self-conjugate
  stratum.
- The earlier "BW vs Wenzl-bridge vs shadow-price" question of
  *which derivation is correct* dissolves: all three are correct
  views of the same canonical $\tilde w_\lambda$.

$\square$
