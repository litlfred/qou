**Proposition (Canonical Wedderburn weight).**
*The mass-formula coefficient associated with each partition
$\lambda \vdash n$ is, up to explicit signed and Hecke-rescaled
factors, a single combinatorial quantity — the canonical
**Wedderburn-block weight***

$$
  w_\lambda
  \;:=\;
  \frac{\dim_q(\lambda)^2}{[n]_q!}
  \;\in\;
  \mathbb{Q}(q),
$$

*where $\dim_q(\lambda)$ is the $q$-Weyl dimension and
$[n]_q! = \prod_{k=1}^{n}[k]_q$ is the $q$-factorial. The three
named coefficient forms used elsewhere in the paper are immediate
scalings of $w_\lambda$:*

| Named form | Identity | Where used |
|------------|----------|------------|
| **BW form** | $\beta_\lambda \;=\; -\tfrac12\,w_\lambda$ | mass coefficient ([hook-weight-derivation](#prop:hook-weight-derivation)) |
| **LP shadow-price** | $C_\lambda \;=\; w_\lambda \cdot h/2$, $h := q - q^{-1}$ | nuclear operator-selection LP dual ([bw-coefficient-shadow-price](#prop:bw-coefficient-shadow-price)) |
| **Wenzl-bridge** | $y_\lambda \;=\; (-1)^{\kappa_\lambda}\,w_\lambda$, $\kappa_\lambda := \sum_{x\in\lambda} c(x)$ | sign-tracked closed form ([y-lambda-closed-form-wenzl-bridge](#prop:y-lambda-closed-form-wenzl-bridge)) |

*For self-conjugate partitions ($\kappa_\lambda = 0$), the
Wenzl-bridge form reduces to $y_\lambda = w_\lambda$. The three
forms are therefore not independent results — each is a
**named scaling** of the same canonical $w_\lambda$, picked for
its naturality in the surrounding context (mass formula / LP /
sign-tracking).*

## Why $w_\lambda$ is canonical

The Wedderburn–Artin decomposition
([Wedderburn mass formula](#thm:wedderburn-mass-formula))
identifies the Hecke algebra $H_n(R, q)$ with a direct sum of
matrix blocks indexed by partitions $\lambda \vdash n$:

$$
  H_n(R, q) \;\cong\; \bigoplus_{\lambda \vdash n} M_{f_\lambda}\bigl(\mathbb{Q}(q)\bigr),
  \qquad
  f_\lambda = \dim_q(\lambda).
$$

Decomposing the Markov trace ([Jones–Markov](#thm:jones-markov-trace))
along the blocks gives

$$
  \mathrm{tr}_M
  \;=\;
  \sum_{\lambda \vdash n} w_\lambda \cdot \chi_\lambda,
  \qquad
  w_\lambda = \frac{\dim_q(\lambda)^2}{[n]_q!},
$$

where $\chi_\lambda$ is the (suitably normalised) character of the
$\lambda$-block. The combinatorial coefficient $w_\lambda$ is the
**Plancherel weight** of the block in the Markov decomposition; it
is determined by the algebra alone, before any choice of mass /
LP / sign convention.

## The three named scalings — derivations

### BW form: $\beta_\lambda = -\tfrac12 w_\lambda$

Mass coefficients in the BW formula carry a sign and a factor of
$\tfrac12$:

- The sign is fixed by the channel structure (sym/std/alt
  alternation in [Wedderburn mass formula](#thm:wedderburn-mass-formula)).
- The $\tfrac12$ comes from the Wigner $T=0$ doubling convention:
  each $\mathfrak{p}\mathfrak{n}$ crossing uses $c=2$ in the hook
  channel, and $\beta$ compensates
  ([hook-weight-derivation](#prop:hook-weight-derivation)).

So $\beta_\lambda = -\tfrac12 w_\lambda$ is the BW-ready mass
coefficient — what one multiplies by $m_e$ to get a MeV-scale
correction.

### LP shadow-price: $C_\lambda = w_\lambda \cdot h/2$

In the nuclear operator-selection LP
([bw-coefficient-shadow-price](#prop:bw-coefficient-shadow-price)),
each partition $\lambda$ contributes a Frobenius-positivity
constraint, and its dual variable (shadow price) is

$$
  C_\lambda
  \;=\;
  w_\lambda \cdot \frac{h}{2},
  \qquad h = q - q^{-1}.
$$

The factor $h$ is the Hecke-generator scalar
$\sigma_i^2 = h\,\sigma_i + 1$; it appears because the LP
constraint involves Hecke-generator action, not pure Markov
trace.

### Wenzl-bridge: $y_\lambda = (-1)^{\kappa_\lambda} w_\lambda$

The Wenzl-bridge closed form
([y-lambda-closed-form-wenzl-bridge](#prop:y-lambda-closed-form-wenzl-bridge))
introduces an explicit sign tracking the **content sum**

$$
  \kappa_\lambda
  \;:=\;
  \sum_{x \in \lambda}\,c(x)
  \;=\;
  \sum_{x = (i,j) \in \lambda}\,(j - i).
$$

For self-conjugate $\lambda$ (those with $\lambda = \lambda'$),
$\kappa_\lambda = 0$ and $y_\lambda = w_\lambda$. For
non-self-conjugate $\lambda$, the sign distinguishes $\lambda$
from its conjugate $\lambda'$ and ensures $y_\lambda + y_{\lambda'} = 0$
on conjugate pairs of equal magnitude.

## Symbolic verification

The three identities above are verified at the level of explicit
$\mathbb{Q}(q)$ rational expressions by the script
[`folio-assistant/computations/bw_wenzl_shadow_equivalence.py`](https://github.com/litlfred/qou/blob/claude/audit-math-framework-FXlp2/folio-assistant/computations/bw_wenzl_shadow_equivalence.py)
for the partitions $\lambda = (2,2) \vdash 4$ (used in BW-8 / BW-11
hook terms) and $\lambda = (3,2,1) \vdash 6$ (Wigner-2 BW-7).
Sympy simplifies the differences to $0$ exactly. Witness:
[`docs/audits/2026-05-01-p1-3a-bw-equivalence.witness.json`](https://github.com/litlfred/qou/blob/claude/audit-math-framework-FXlp2/docs/audits/2026-05-01-p1-3a-bw-equivalence.witness.json).

## Why each context picks a different form

| Context | Form chosen | Reason |
|---------|-------------|--------|
| Mass formula | $\beta_\lambda = -\tfrac12 w_\lambda$ | Already includes the sign and Wigner $\tfrac12$ doubling needed to multiply by $m_e$ and produce a MeV correction. |
| Operator-selection LP | $C_\lambda = w_\lambda h/2$ | LP duality on the Frobenius-positivity constraint involves the Hecke generator $\sigma_i$ with eigenvalue $h$; the dual variable inherits the $h$ factor. |
| Sign-tracked closed form | $y_\lambda = (-1)^{\kappa_\lambda} w_\lambda$ | Conjugate pairs $\lambda \leftrightarrow \lambda'$ contribute with opposite signs; the explicit $\kappa_\lambda$ sign rule produces a closed form valid for all partitions, not just self-conjugate ones. |

Each form is **natural in its context** but they all encode the
same combinatorial fact: $w_\lambda = \dim_q(\lambda)^2/[n]_q!$ is
the Plancherel weight of the $\lambda$-block in the Wedderburn
decomposition of the Markov trace.

## Consequences for downstream use

- Any new mass-formula coefficient at a new partition can be
  derived in three steps: (1) compute $w_\lambda$ from $\dim_q(\lambda)$
  and $[n]_q!$; (2) pick the named form natural in the
  surrounding context; (3) cite this proposition for the
  rationale.
- Cross-checks between mass / LP / Wenzl forms reduce to a
  one-line scaling identity, not a re-derivation.
- The earlier "BW vs Wenzl-bridge vs shadow-price" question of
  *which derivation is correct* dissolves: all three are correct
  views of the same canonical $w_\lambda$.

$\square$
