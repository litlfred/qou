<!-- FILE_START: intro-wenzl-bridge-cyclotomic.md -->
The Wenzl bridge is the categorical morphism that converts a
$q$-deformed Hecke trace into a Jones-polynomial evaluation at a
cyclotomic root of unity, packaged so that the resulting
$\alpha$-coefficients are *explicit* polynomials in the
substrate parameter rather than implicit series.  This section
records the bridge construction, exhibits the resulting
cyclotomic factorisation of the categorical $y_\lambda$
sequence, and extracts the explicit small-$\lambda$
$\alpha_k$ values that the six-term mass formula needs.

The arc moves in three movements.  The first blocks construct
the Wenzl bridge and prove it preserves the Hecke trace under
the cyclotomic specialisation; the middle blocks exhibit the
cyclotomic factorisation $y_\lambda = \prod_\zeta y_\lambda(\zeta)$
and extract the explicit polynomial factors; the closing blocks
tabulate the $\alpha_k$ values for $k \leq 6$ and connect them
to the six-term mass formula coefficients via the substrate-
flow normalisation.

The output is the explicit $\alpha_k$ table that drives the
six-term mass formula's evaluation against CODATA.  This is the
chapter's most concrete canonical content and is the natural
exit point for readers who want the substrate-level predictions
without the full categorical apparatus.
<!-- FILE_END: intro-wenzl-bridge-cyclotomic.md -->

<!-- FILE_START: y-lambda-cyclotomic-factorization.md -->
**Proposition (cyclotomic factorisation of $y_\lambda$ at small $n$).**
*Let $\sigma_i$ be the symmetric Hecke generators of $H_n(R, q)$ with
Markov parameter $z = 1/(q^{1/2} + q^{-1/2})$, and write $\check{q} = q^{1/2}$.
Then for every $\lambda \,\vdash\, n$ at $n \in \{2, 3, 4\}$, the
Jones-Markov central coefficient $y_\lambda$ admits the closed form*

$$
  y_\lambda(\check{q}) \;=\; \frac{P_\lambda(\check{q})}{D_n(\check{q})}, \qquad
  D_n(\check{q}) \;=\; \prod_{d} \Phi_d(\check{q})^{e_{n, d}},
$$

*where $P_\lambda(\check{q}) \in \mathbb{Z}[\check{q}]$ is a polynomial in $\check{q}$ and
$D_n(\check{q})$ is a **pure product of cyclotomic polynomials** $\Phi_d(\check{q})$.*

## Per-$n$ denominators (over $\mathbb{Q}$ in $\check{q} = q^{1/2}$)

| $n$ | $D_n(\check{q})$ |
|--:|--|
| $2$ | $\Phi_4(\check{q}) \cdot \Phi_8(\check{q}) = (\check{q}^2 + 1)(\check{q}^4 + 1)$ |
| $3$ | $\Phi_4(\check{q})^2 \cdot \Phi_8(\check{q}) \cdot \Phi_3(\check{q}) \cdot \Phi_6(\check{q}) \cdot \Phi_{12}(\check{q})$ |
| $4$ | $\Phi_4(\check{q})^3 \cdot \Phi_8(\check{q})^2 \cdot \Phi_{16}(\check{q})$ (for hook-shape rows) |

where $\Phi_3(\check{q}) = \check{q}^2 + \check{q} + 1$, $\Phi_4(\check{q}) = \check{q}^2 + 1$,
$\Phi_6(\check{q}) = \check{q}^2 - \check{q} + 1$, $\Phi_8(\check{q}) = \check{q}^4 + 1$,
$\Phi_{12}(\check{q}) = \check{q}^4 - \check{q}^2 + 1$, $\Phi_{16}(\check{q}) = \check{q}^8 + 1$.

## Numerators (small $n$)

### $n = 2$

$$
  y_{(2)}(\check{q}) = \frac{\check{q}^3 + \check{q}^2 + 1}{\Phi_4(\check{q}) \, \Phi_8(\check{q})}, \qquad
  y_{(1, 1)}(\check{q}) = \frac{\check{q}^3 \, (\check{q}^3 + \check{q} - 1)}{\Phi_4(\check{q}) \, \Phi_8(\check{q})}.
$$

The numerators $P_{(2)} = \check{q}^3 + \check{q}^2 + 1$ and $P_{(1,1)} = \check{q}^3(\check{q}^3+\check{q}-1)$
are **not** cyclotomic — they encode the specific $X$ substitution
from the Wenzl-bridge.

### $n = 3$

$$
\begin{aligned}
  y_{(3)}(\check{q}) &= \frac{(\check{q} + 1)(\check{q}^3 + \check{q}^2 + 1)(\check{q}^6 - \check{q}^5 + \check{q}^4 - \check{q}^3 + 2\check{q}^2 - \check{q} + 1)}{D_3(\check{q})}, \\
  y_{(2, 1)}(\check{q}) &= \frac{\check{q}^3 (\check{q}^3 + \check{q} - 1)(\check{q}^3 + \check{q}^2 + 1)}{\Phi_4(\check{q})^2 \, \Phi_3(\check{q}) \, \Phi_6(\check{q}) \, \Phi_{12}(\check{q})}, \\
  y_{(1^3)}(\check{q}) &= \frac{\check{q}^6 (\check{q} - 1)(\check{q}^3 + \check{q} - 1)(\check{q}^6 + \check{q}^5 + 2\check{q}^4 + \check{q}^3 + \check{q}^2 + \check{q} + 1)}{D_3(\check{q})}.
\end{aligned}
$$

### $n = 4$

$$
\begin{aligned}
  y_{(4)} &= \frac{(\check{q} + 1)(\check{q}^3 + \check{q}^2 + 1)(\check{q}^{11} + \check{q}^7 + \check{q}^3 + \check{q}^2 + 1)(\ldots)}{\Phi_4^3 \, \Phi_8^2 \, \Phi_{16} \, \Phi_3 \, \Phi_6 \, \Phi_{12}}, \\
  y_{(2,2)} &= \frac{\check{q}^7 (\check{q}^3 + \check{q} - 1)(\check{q}^3 + \check{q}^2 + 1)}{\Phi_4^2 \, \Phi_8^2 \, \Phi_3 \, \Phi_6 \, \Phi_{12}}, \\
  y_{(1^4)} &= \frac{\check{q}^9 (\check{q} - 1)(\check{q}^3 + \check{q} - 1)(\check{q}^{11} + \check{q}^9 - \check{q}^8 - \check{q}^4 - 1)(\ldots)}{D_4(\check{q})}.
\end{aligned}
$$

(Mid-shapes $(3,1), (2,1,1)$ are bigger; see witness file for full
expressions.)
## Significance

This is the **cleanest possible closed form** for $y_\lambda$ in
$\mathbb{Q}(\check{q})$: the denominator structure is fully determined by
combinatorial hook-length data via cyclotomic polynomials, and the
numerator is a finite-degree polynomial in $\check{q}$ that can be
explicitly tabulated.

For Lean formalisation, this gives a concrete mathematical
statement:

$$
  y_\lambda(\check{q}) \cdot D_n(\check{q}) \;=\; P_\lambda(\check{q})
  \in \mathbb{Z}[\check{q}]
$$

where $D_n(\check{q}) = \prod_d \Phi_d(\check{q})^{e_{n,d}}$ with explicit
$e_{n, d}$ exponents derivable from the hook-length data of all
partitions of $n$.

## Witness

the canonical formalism
factors the Wenzl-bridge $y_\lambda$ over $\mathbb{Q}(\check{q})$ via sympy.
Output: `y-lambda-cyclotomic-factor.witness.json` with explicit
factored numerators and denominators for $n = 2, 3, 4$.
<!-- FILE_END: y-lambda-cyclotomic-factorization.md -->

<!-- FILE_START: y-lambda-recipe-from-partition.md -->
**Proposition (recipe: $\lambda \mapsto y_\lambda(q)$ as q-rational).**
*Given a partition $\lambda \,\vdash\, n$, the Jones-Markov central
coefficient $y_\lambda(q)$ is determined by the following algorithm,
yielding a rational function in $\sqrt q$ with cyclotomic
denominator.*

## Step 1: Compute partition data

For each cell $(i, j) \in \lambda$ (1-indexed, $i$ = row, $j$ = column):

- **Content** $c(i, j) := j - i$
- **Hook length** $h(i, j) := \mathrm{arm}(i, j) + \mathrm{leg}(i, j) + 1$
  where $\mathrm{arm}(i, j) := \lambda_i - j$ (cells right of $(i, j)$
  in row $i$) and $\mathrm{leg}(i, j) := |\{r > i : \lambda_r > j\}|$
  (cells below $(i, j)$ in column $j$).

Define $n(\lambda) := \sum_i (i - 1) \lambda_i$.

## Step 2: Compute the universal $X$ substitution

Let $z := 1/(\sqrt q + 1/\sqrt q)$ (Markov parameter). Then

$$
  z \;=\; \frac{\sqrt q}{q + 1},
  \qquad
  q \cdot z \;=\; \frac{q^{3/2}}{q + 1},
$$

and the Wenzl-bridge level $r$ satisfies $q \cdot z = Q^r (1 - Q) /
(1 - Q^r)$ with $Q := q^2$. Solving:

$$
  \boxed{\;
    X \;:=\; Q^r \;=\; \frac{q^{3/2}}{1 + q - q^2 - q^3 + q^{3/2}}.
  \;}
$$

canonical at $q_0 \approx 1.110$: $X \approx 1.7203$.

## Step 3: Compute the Schur principal-specialisation

For partition $\lambda$, define

$$
  \boxed{\;
    s_{\lambda, r}(Q) \;=\; Q^{n(\lambda)} \cdot
    \prod_{(i, j) \in \lambda}
    \frac{1 - X \cdot Q^{c(i, j)}}{1 - Q^{h(i, j)}}
  \;}
$$

with $Q = q^2$ and $X$ from Step 2.  Each cell contributes one
factor of the form $(1 - X \cdot q^{2 c}) / (1 - q^{2 h})$ — both
polynomial in $\sqrt q$ after substitution.

## Step 4: Normalise

Compute the **partition-function denominator**

$$
  Z_n \;:=\; \sum_{\mu \,\vdash\, n} d_\mu \cdot s_{\mu, r}(Q),
$$

where $d_\mu = f^\mu$ is the classical $S_n$-irrep dimension via
hook-length formula

$$
  f^\mu \;=\; \frac{n!}{\prod_{(i, j) \in \mu} h(i, j)}.
$$

Then

$$
  \boxed{\;
    y_\lambda(q) \;=\; \frac{s_{\lambda, r}(Q)}{Z_n}.
  \;}
$$

## Step 5: Factor over $\mathbb{Q}$ in $\sqrt q$

Substitute $X = q^{3/2} / (1 + q - q^2 - q^3 + q^{3/2})$ explicitly
and reduce via cancellation. The denominator factors as a pure
product of cyclotomic polynomials in $\sqrt q$:

$$
  D_n(\sqrt q) \;=\; \prod_d \Phi_d(\sqrt q)^{e_{n, d}}
$$

where the exponents $e_{n, d}$ are determined by the hook-length
data of all partitions of $n$ via

$$
  1 - q^k \;=\; \prod_{d \mid 2k} \Phi_d(\sqrt q)
$$

(since $q^k = (\sqrt q)^{2k}$).  The numerator $P_\lambda(\sqrt q)$
is a polynomial encoding the $X$ substitution; it is generally
**not** cyclotomic.

## Worked example: $\lambda = (2)$ at $H_2$

**Step 1**: Cells $(1, 1), (1, 2)$.
- $c(1, 1) = 0$, $c(1, 2) = 1$.
- $h(1, 1) = 2$, $h(1, 2) = 1$.
- $n((2)) = 0$.

**Step 2**: $X = q^{3/2} / (1 + q - q^2 - q^3 + q^{3/2})$.

**Step 3**: $Q^0 = 1$, so

$$
  s_{(2), r}(Q) \;=\; \frac{(1 - X)(1 - X \cdot Q)}{(1 - Q^2)(1 - Q)}.
$$

**Step 4**: Other partition is $(1, 1)$ with $n = 1$, contents $0, -1$, hooks $2, 1$:

$$
  s_{(1, 1), r}(Q) \;=\; \frac{Q (1 - X)(1 - X / Q)}{(1 - Q^2)(1 - Q)}.
$$

$d_{(2)} = d_{(1, 1)} = 1$, so

$$
\begin{aligned}
  Z_2 &= s_{(2)} + s_{(1, 1)}
       = \frac{(1 - X)\bigl[(1 - XQ) + Q(1 - X/Q)\bigr]}{(1 - Q^2)(1 - Q)} \\
      &= \frac{(1 - X)(1 + Q)(1 - X)}{(1 - Q^2)(1 - Q)}
       = \frac{(1 - X)^2}{(1 - Q)^2}.
\end{aligned}
$$

**Step 5**: $y_{(2)}(q) = s_{(2)} / Z_2 = (1 - X q^2) / ((1 - X)(1 + q^2))$.

After substituting $X$ and factoring over $\mathbb{Q}$ in $\sqrt q$:

$$
  \boxed{\;
    y_{(2)}(q) \;=\;
    \frac{(\sqrt q)^3 + (\sqrt q)^2 + 1}
         {\Phi_4(\sqrt q) \, \Phi_8(\sqrt q)}
    \;=\;
    \frac{q^{3/2} + q + 1}{(q + 1)(q^2 + 1)}.
  \;}
$$

(Using $\Phi_4(\sqrt q) = q + 1$ and $\Phi_8(\sqrt q) = q^2 + 1$.)

## canonical sanity at $q_0 \approx 1.110$

$y_{(2)}(q_0) = (1.1097 + 1.110 + 1) / ((1.110 + 1)(1.232 + 1))
             = 3.220 / (2.110 \cdot 2.232) = 3.220 / 4.708 = 0.6839$ ?

Re-evaluating exactly: $q^{3/2} \approx 1.169$, so the numerator
is $1.169 + 1.110 + 1 = 3.279$ and the denominator is
$2.110 \cdot 2.232 = 4.710$, giving $y_{(2)} \approx 0.6963$, in
agreement with the witness value $0.69632542$.

## Algorithm summary (pseudocode)

```
function y_lambda(λ):
    # Step 1
    cells   = [(i, j) for i in 1..len(λ), j in 1..λ[i]]
    content = j - i for each cell
    hook    = arm + leg + 1 for each cell
    n_lam   = Σ (i-1) λ_i

    # Step 2 (universal)
    X = q^(3/2) / (1 + q - q² - q³ + q^(3/2))

    # Step 3
    s_λ = q^(2 n_lam) · ∏ (1 - X·q^(2c)) / (1 - q^(2h))

    # Step 4
    Z_n = Σ_µ (n! / ∏ h_µ) · s_µ
    y_λ = s_λ / Z_n

    # Step 5 (optional cleanup)
    return factor_over_Q_in_sqrt_q(y_λ)
```

This is **fully mechanical**: any partition $\lambda$ at any $n$
yields its $y_\lambda(q)$ in closed q-rational form via this recipe
in $O(p(n) \cdot \max \text{hooks})$ time.

## Code

the canonical formalism
implements the full recipe end-to-end; takes a partition as input
and returns $(P_\lambda, D_n)$ in $\sqrt q$ with cyclotomic
denominator.
<!-- FILE_END: y-lambda-recipe-from-partition.md -->

<!-- FILE_START: graded-hecke-energy-truncation-bound.md -->
**Proposition (graded Hecke energy truncation bound).**
*Let $\hat{\beta}_K$ be the closure of a braid $\mathcal{B}_K \in B_n$, let
$\mathfrak{M}_K$ be the stable highest-weight KLR module
\cite{khovanovlauda2009, brundankleshchev2009} associated to
$\hat{\beta}_K$, and let*

$$
  P_K(q) \;=\; \sum_{d \in \mathbb{Z}}
    \dim_R \mathrm{Hom}_{\mathcal{K}_n}(P_d, \mathfrak{M}_K) \, q^d
  \;\in\; \mathbb{Z}_{\geq 0}[q^{\pm 1/2}]
$$

*be the mass-spectrum generating function of $K$
([mass-spectrum generating function](#rem:mass-spectrum-generating-function)).
Then $P_K(q)$ has at most $\ell(K, q_0) + 1$ nonzero terms, where
$\ell(K, q_0)$ is the
[confinement level](#def:confinement-level)
of $K$ at the substrate value $q_0$.*

## Computational consequence

For canonical evaluation of $\mathrm{tr}_M(T_w(\mathcal{B}_K), q_0) =
P_K(q_0)$, only the grades $d \in \{0, 1, \ldots, \ell(K, q_0)\}$
need to be enumerated. The naive enumeration over all $p(n)$
partitions of the $n$ strands of $\mathcal{B}_K$ overcounts:
many partitions contribute zero or negligibly to the relevant
grades. **The truncation reduces the effective work from $p(n)$
partitions to at most $\ell(K, q_0) + 1$ effective grades.**

Empirically at $q_0 \approx 1.110$:

See [Table](#tbl:graded-hecke-energy-truncation-bound-table-data).

Speedups assume $\ell(K, q_0) + 1$ effective grades vs $p(n)$
partitions; conservative since the per-grade cost is comparable.

## Stratified-cache compatibility

The result also enables **resumable** canonical evaluation: a
partial cache `chi-{atom}-h{n}.witness.json` can be made
graded-stratified, so partial completion at grade $\ell^\star$
exposes $\mathrm{tr}_{M, \leq \ell^\star}(\mathcal{B}_K)$ immediately.
Resuming becomes a matter of picking up at grade $\ell^\star + 1$
rather than partition $i+1$ — a structural property the partition-
indexed cache does not have.

## Empirical witness

the canonical formalism
demonstrates the stratification on the proton/neutron/deuteron
braids at the canonical $q_0$, emitting per-grade $c_d$ values
and confirming the truncation bound holds. Output:
`graded-hecke-energy-canonical evaluation.witness.json`.
<!-- FILE_END: graded-hecke-energy-truncation-bound.md -->

<!-- FILE_START: descent-rate-probe-sim.md -->

<!-- FILE_END: descent-rate-probe-sim.md -->

<!-- FILE_START: multi-level-jet-sum-sim.md -->

<!-- FILE_END: multi-level-jet-sum-sim.md -->

<!-- FILE_START: macdonald-hook-telescope.md -->
**Proposition (Macdonald hook-content telescope, conditional on `StanleyHookTelescope`).**
*Let $Q = q^2$ and $X = q\,z\,/\,(1 - Q + q\,z)$ be the Wenzl-bridge
substitution of
[`prop:y-lambda-closed-form-wenzl-bridge`](#prop:y-lambda-closed-form-wenzl-bridge),
let $f_\lambda$ be the number of standard Young tableaux of shape
$\lambda$, and let*

$$
  s_{\lambda, X}(Q) \;=\; Q^{n(\lambda)} \prod_{x \in \lambda}
    \frac{1 - X \cdot Q^{c(x)}}{1 - Q^{h(x)}}
$$

*be the principal-specialisation Schur element. Then the
Wenzl-bridge normalisation $Z_n := \sum_{\lambda \vdash n}
f_\lambda \cdot s_{\lambda, X}(Q)$ telescopes to the single
geometric ratio*

$$
  \boxed{\;
    Z_n \;=\; \left(\frac{1 - X}{1 - Q}\right)^n,
  \;}
$$

*and consequently every Jones–Markov central coefficient
$y_\lambda$ admits the **single-product hook-content closed
form***

$$
  \boxed{\;
    y_\lambda \;=\; Q^{n(\lambda)}
      \cdot \frac{(1 - Q)^n}{(1 - X)^n}
      \cdot \prod_{x \in \lambda}
        \frac{1 - X \cdot Q^{c(x)}}{1 - Q^{h(x)}}.
  \;}
$$

## Conditional-class formalisation

The Lean module axiomatises the principal-specialisation identity as
the class `StanleyHookTelescope`; the proposition's theorem
`macdonald_hook_telescope` carries this class as an explicit
`[Instance]` hypothesis and is discharged by `telescope_holds`.
This follows AGENTS.md §3b-cond (conditional-on-class). The
`wenzlNormalizationOfShape` value is kept `opaque` so the class
field captures substantive (non-tautological) mathematical content.

The substantive content of the identity is Stanley's
principal-specialisation result (Stanley 1999 Cor. 7.12.5;
Macdonald 1995 I.3 ex. 1). It is backed empirically by symbolic
verification at $n = 0, \ldots, 8$ in
the formal derivation (every partition closes via
`sympy.cancel` to 0) and 191-sample canonical cross-check to
$\approx 10^{-51}$ against the MPFR Hoefsmit-matrix witness. A
future Mathlib lift of Schur / principal-specialisation
infrastructure would supply a constructive instance, with the
downstream API unchanged.

## Justification of the shortcut

The classical principal-specialisation identity (Stanley,
*Enumerative Combinatorics II* Cor. 7.12.5; Macdonald, *Symmetric
Functions* I.3 ex. 1) states

$$
  \sum_{\lambda \vdash n} f_\lambda \cdot s_\lambda
    \;=\; p_1^{\,n}
$$

as symmetric functions, where $p_1 = \sum x_i$. Equivalently, the
regular representation of $S_n$ has Frobenius image $p_1^n$. Under
the *principal specialisation in $r$ variables* — the substitution
$x_i \mapsto q^{i-1}$ for $i = 1, \ldots, r$ — we have
$p_1 \mapsto 1 + q + \cdots + q^{r-1} = (1 - q^r)/(1 - q)$. Sending
$q \mapsto Q$ and identifying the Wenzl level $X = Q^r$ gives

$$
  Z_n \;=\; \sum_{\lambda \vdash n} f_\lambda \cdot s_{\lambda, X}(Q)
    \;=\; \left(\frac{1 - X}{1 - Q}\right)^n.
$$

The fractional/non-integer $r$ used by the Wenzl bridge does not
break the identity: $X = Q^r$ enters the formula only through the
factor $(1 - X)$, and the right-hand side of the principal-
specialisation identity is a polynomial identity in $X$ that
extends analytically.

## Comparison with the previous "open structural project"

The earlier hand-derivation in
[`y-lambda-clean-closed-forms.md`](https://github.com/litlfred/qou/blob/main/computations/y-lambda-clean-closed-forms.md)
recorded the $n = 2$ collapse $Z_2 = (1 - X)^2 / (1 - Q)^2$,
flagged the $n \geq 3$ unsimplified sympy expressions as
"degree $\sim 25$ polynomials", and listed the general identity as
an *open structural project* — pending a Macdonald-hook formula
that would let `sympy.factor` collapse the sum at every $n$.
This proposition closes that project: the identity is the
classical regular-representation Frobenius identity, evaluated
at the principal specialisation.

## Computational consequences

Per-partition, the closed form requires only the cells of $\lambda$:

- $O(n)$ cell scans for $n(\lambda)$, contents $c(x)$, hooks $h(x)$.
- One product of $n$ factors $(1 - X \cdot Q^c)$ in the numerator.
- One product of $n$ factors $(1 - Q^h)$ in the denominator.
- One global $(1 - Q)^n / (1 - X)^n$ from the telescope.

No `sympy.simplify` and no `sympy.cancel` are required: the
expression is already in canonical hook-content form. This
eliminates the sympy `RecursionError` previously observed for
$n \geq 5$ and the "degree $\sim 80$ in $q^{1/2}$" denominator
explosion at $n = 12$. The compute path is now O($p(n) \cdot n$)
work for the entire table.

## canonical structural verification

The companion formalism
the canonical formalism

1. Verifies $Z_n = ((1-X)/(1-Q))^n$ symbolically for $n = 0, \ldots, 6$
   (the difference reduces to $0$ via `sympy.cancel`).
2. Verifies the closed-form collapse
   $y_\lambda = s_{\lambda, X}(Q) / Z_n$ partition-by-partition for
   $n = 0, \ldots, 6$ (all 30 partitions).
3. Emits closed forms for all 30 partitions across $n = 0, \ldots, 6$
   — the closed-form formula itself is $O(n)$ per partition for any
   $n$; only sympy serialisation costs grow at larger $n$.
4. Cross-checks against the MPFR Hoefsmit-matrix witness
   (`y-lambda-mpfr-witness.json`): max
   $|y_\lambda^{\text{telescope}} - y_\lambda^{\text{MPFR}}|
     \approx 2.5 \times 10^{-51}$ across 191 samples (limited only
   by the witness's exact representation precision).

Output: [`y-lambda-macdonald-telescope.witness.json`](https://github.com/litlfred/qou/blob/main/computations/y-lambda-macdonald-telescope.witness.json).

## Crystal-basis interpretation

The identity $\sum_\lambda f_\lambda \cdot s_\lambda = p_1^n$ is
the *Frobenius character* of the regular $S_n$-representation,
which is the **Kostka decomposition** of $p_1^n$ into Schur
functions. Categorified, $p_1^n$ is the $n$-fold tensor product of
the natural module of the KLR algebra $R_\alpha$ (in type $A$);
the multiplicity $f_\lambda$ is the dimension of the corresponding
KLR canonical-basis component. The telescope is thus the
**decategorified Kashiwara crystal count** for the regular
representation — exactly the symmetric-crystal shortcut flagged in
the project's authoring guidance (AGENTS.md §7b, item 2: "decategorifying
KLR canonical basis to KL basis of $S_n$"). The previous
hand-rolled sympy approach reinvented this combinatorial count
without naming the crystal structure; naming it removes the
manual algebra.

## Lean formalisation

[`macdonald-hook-telescope.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/macdonald-hook-telescope.lean)
states `macdonald_hook_telescope`: $Z_n = ((1-X)/(1-Q))^n$ as
an algebraic identity over $\mathbb{Q}(X, Q)$. The proof reduces
to the principal-specialisation case of the regular-representation
Frobenius identity — currently a single `sorry` with a citation to
[stanley1999] Cor. 7.12.5, plus an empirical witness link to
`y-lambda-macdonald-telescope.witness.json` recording symbolic
verification through $n = 8$.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: macdonald-hook-telescope.md -->

<!-- FILE_START: demazure-fiber-markov-trace.md -->
**Proposition (Demazure-fiber Markov-trace functional).**
*Let $V_\lambda$ be the irreducible $S_n$-module indexed by
$\lambda \vdash n$, with Kashiwara crystal $\mathrm{Cryst}(V_\lambda)$
in type $A_{n-1}$
([`conj:crystal-graph-realization`](#conj:crystal-graph-realization)).
For each Weyl element $w \in S_n$, let*

$$
  D_w(\lambda) \;=\; \pi_w \bigl(x^{\lambda}\bigr)
  \;=\; \pi_{i_1} \cdots \pi_{i_k}\!\bigl(x_1^{\lambda_1}\cdots x_n^{\lambda_n}\bigr)
$$

*be the Demazure character, where $\pi_i(f) = (x_i f - x_{i+1}\,s_i f)/(x_i - x_{i+1})$
is the Demazure isobaric divided-difference operator and
$w = s_{i_1} \cdots s_{i_k}$ is any reduced word.  At the longest
element $w_0$, $D_{w_0}(\lambda) = s_\lambda(x_1, \ldots, x_n)$
recovers the Schur polynomial; at intermediate $w$, the Demazure
character $D_w(\lambda)$ is the character of a sub-crystal of
$\mathrm{Cryst}(V_\lambda)$ — an "incomplete topological state" in
the sense of AGENTS.md §7b item 3. Define the Demazure-fiber
Markov-trace functional*

$$
  \boxed{\;
    T^{\mathrm{Dem}}(\lambda;\, w)
    \;:=\;
    y_\lambda
    \cdot
    \frac{D_w(\lambda)}{D_{w_0}(\lambda)},
  \;}
$$

*where $y_\lambda$ is the Jones–Markov central coefficient
([`prop:macdonald-hook-telescope`](#prop:macdonald-hook-telescope)),
and the ratio $D_w(\lambda) / D_{w_0}(\lambda)$ is taken under the
principal specialisation $x_i \mapsto q^{i-1}$.  Then:*

1. *$T^{\mathrm{Dem}}(\lambda;\, w_0) = y_\lambda$ — the standard
   Jones–Markov coefficient is the saturated case.*
2. *For $w < w_0$ (Bruhat order), $T^{\mathrm{Dem}}(\lambda;\, w)$
   is the **structural resonance width** of the $\lambda$-block
   under the Demazure filtration: the fraction of $V_\lambda$
   accessible from the Demazure sub-crystal cut by $w$.*
3. *Plancherel completeness:
   $\sum_{\lambda \vdash n} f_\lambda \cdot T^{\mathrm{Dem}}(\lambda;\, w_0) = 1$
   reduces to the Macdonald hook-content telescope
   ([`prop:macdonald-hook-telescope`](#prop:macdonald-hook-telescope)).*

## Replacing the manual Hecke-energy LP cost

The LP / SDP cost vector
$c_\lambda = \tilde w_\lambda(q) = \dim_q(V_\lambda)^2 / [n]_q!$ used
in
[`sdp-dual-without-demand.md`](https://github.com/litlfred/qou/blob/main/computations/sdp-dual-without-demand.md)
is the q-deformed Wedderburn-block weight (the classical Plancherel
measure is the bare-symbol $w_\lambda = (\dim V_\lambda)^2/n!$; see
[`prop:plancherel-weight-boundedness`](#prop:plancherel-weight-boundedness)). It is
computed by-hand via Hoefsmit matrices or the hook-content
formula, with no structural reason for the chosen functional
beyond the trace constraint.

The Demazure-fiber functional $T^{\mathrm{Dem}}$ subsumes this in
two senses:

| | manual Hecke-energy | Demazure-fiber |
|---|---|---|
| Cost at full block | $w_\lambda(q)$ | $T^{\mathrm{Dem}}(\lambda;\, w_0) = y_\lambda$ |
| Sub-block (resonance) | not represented | $T^{\mathrm{Dem}}(\lambda;\, w)$ for $w < w_0$ |
| Computation | Hoefsmit matmul / sympy | Demazure operator recursion |
| Per-partition complexity | $O(\dim V_\lambda^3)$ | $O(\ell(w_0)) = O(n^2)$ |
| Crystal interpretation | none — empirical | sub-crystal projection |

For the LP/SDP solvers in the QOU pipeline, the cost
vector at $w = w_0$ is unchanged, but the dual variables and
shadow prices acquire a structural interpretation: the active set
$\{\lambda \mid u_\lambda^* > 0\}$ corresponds to the Demazure
fiber that the bound state actually occupies, and inactive blocks
have $T^{\mathrm{Dem}}(\lambda;\, w) = 0$ for some "decay-time"
Weyl element $w$.

## Worked example: $n = 3$, the alt block

Take $\lambda = (1, 1, 1)$ — the alt / antiparticle block at $n = 3$.
Then $V_\lambda$ is the sign representation, $\dim V_\lambda = 1$,
and $\mathrm{Cryst}(V_\lambda)$ is a single vertex. Demazure
characters at $x_i = q^{i-1}$:

| $w$ | reduced word | $D_w(1,1,1)$ at p.s. | $D_w / D_{w_0}$ |
|---|---|---|---|
| $\mathrm{id}$ | $\emptyset$ | $1$ | $1/q^3$ |
| $s_1$ | $(1)$ | $1 + q$ | $(1 + q)/q^3$ |
| $s_1 s_2$ | $(1, 2)$ | $1 + q + q^2$ | $(1+q+q^2)/q^3$ |
| $s_1 s_2 s_1 = w_0$ | $(1, 2, 1)$ | $q^3$ | $1$ |

Each prefix of $w_0$ corresponds to a Demazure sub-crystal of
increasing size; the ratio sweeps from "almost-empty fiber" to
"saturated block". Multiplied by the telescope-form $y_{(1,1,1)}$,
this gives the Demazure-fiber resonance width of the alt block at
each filtration depth — the exact analogue of a resonance width
without phenomenological cutoffs.

## Structural justification of the Demazure operator

By Kashiwara's refined Demazure character formula
\cite{kashiwara1991}, $D_w(\lambda)$ is the character of the
Demazure sub-crystal $B_w(\lambda) \subseteq \mathrm{Cryst}(V_\lambda)$
generated from the highest-weight vertex by the chains
$\tilde f_{i_1}, \ldots, \tilde f_{i_k}$. Hence
$D_w / D_{w_0}$ is the fraction of $V_\lambda$ reachable from
the highest weight along the chosen Bruhat-prefix path — exactly
the structural notion of "incomplete topological state" that the
crystal-basis literature uses for resonances and virtual
intermediates \cite{lecouvey2007}.

For the QOU pipeline, the Demazure-filtered Markov trace is the
natural setting in which W/Z resonances, hadronic decays, and
virtual particles all become *structural objects* rather than
heuristic LP cutoffs. They are sub-crystals of completed Wedderburn
blocks, indexed by Bruhat-comparable Weyl elements.

## Crystal-basis shortcut

This is shortcut #3 from AGENTS.md §7b: replace the manual
Hecke-energy LP functional with Kashiwara weight-lattice
projection. Resonance widths become structural Demazure
multiplicities, not heuristic cutoffs. The shadow-price ordering
discussed in
[`sdp-dual-without-demand.md`](https://github.com/litlfred/qou/blob/main/computations/sdp-dual-without-demand.md)
acquires a Bruhat-order interpretation: more-active LP blocks
correspond to longer Bruhat-prefix Demazure sub-crystals.

## canonical structural verification

The companion formalism
the canonical formalism

1. Implements the Demazure operator $\pi_i$ recursively on
   $\mathbb{Q}[x_1, \ldots, x_n]$ via sympy.
2. Verifies $D_{w_0}(\lambda) = s_\lambda$ at principal
   specialisation against the Macdonald hook-content formula for
   $n = 2, 3$ (all 5 partitions: differences reduce to $0$ via
   `sympy.cancel`).
3. Tabulates $D_w(\lambda)$, $D_w(\lambda)/D_{w_0}(\lambda)$, and
   $T^{\mathrm{Dem}}(\lambda; w)$ for every $(\lambda, w) \in
   \mathrm{Part}(n) \times S_n$ at $n \in \{2, 3\}$ —
   $4 + 18 = 22$ non-trivial Demazure characters in total
   ($p(n) \cdot n!$ for $n \in \{2, 3\}$).  Extension to $n = 4$
   adds $5 \cdot 24 = 120$ further evaluations and is deferred to
   a follow-up witness.

Output: [`demazure-markov-trace.witness.json`](https://github.com/litlfred/qou/blob/main/computations/demazure-markov-trace.witness.json).

## Lean formalisation

[`demazure-fiber-markov-trace.lean`](demazure-fiber-markov-trace.lean)
defines the abstract Demazure operator `demazureOp`, the Demazure
character `demazureCharacter`, the principal-specialisation ratio
`demazureRatio`, and the Demazure-fiber Markov-trace functional
`demazureFiberMarkovTrace`. The two main theorems are:

- `demazure_at_w0_equals_y_lambda` —
  $T^{\mathrm{Dem}}(\lambda;\, w_0) = y_\lambda$, reducing to
  `prop:macdonald-hook-telescope`.
- `demazure_principal_specialization_eq_schur` — at
  $x_i = q^{i-1}$, $D_{w_0}(\lambda)$ equals the Macdonald
  hook-content principal specialisation; deferred to a single
  `sorry` citing Kashiwara's refined character formula.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: demazure-fiber-markov-trace.md -->

<!-- FILE_START: wenzl-bridge-applicability-qou.md -->
**Proposition (applicability of the Wenzl-bridge formula in QOU).**
*Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be a QOU substrate
satisfying the [archimedean axioms](#def:rigid-monoidal-category)
with self-dual fundamental object $A \in \mathbf{C}$ and fibre
functor $\tau \colon \mathbf{C} \to R\text{-mod}$
([fibre functor](#prop:fibre-functor-atlas)).  Let
$H := \mathrm{Aut}^\otimes(\tau)$ be the Tannaka--Krein Hopf algebra
([Tannaka--Krein](#prop:tannaka-krein-reconstruction)) and
$V := \tau(A)$.  Then the Markov trace
$\mathrm{tr}_M$ on the Iwahori--Hecke algebra $H_n(R, q)$
([Jones--Markov trace](#thm:jones-markov-trace)) is uniquely
determined by $(\mathbf{C}, A, \tau)$ up to the normalisation
$\mathrm{tr}_M(1) = 1$, and equals the closed form
([Wenzl-bridge $y_\lambda$](#prop:y-lambda-closed-form-wenzl-bridge)).*
## Corollaries

1. **No fitting.**  The Wenzl-bridge formula is *the* closed form
   for $y_\lambda$ in QOU; no parameter is chosen to fit observables.

2. **Unique extension to $n \ge 5$.**  The
   ([procedure](#prop:alpha-k-derivation-procedure))
   linear-system characterisation gives $y_\lambda$ at finite $n$;
   the Wenzl bridge gives the same $y_\lambda$ in closed form at
   every $n$, and the two characterisations agree by uniqueness
   ([cross-check witness](https://github.com/litlfred/qou/blob/main/computations/y-lambda-wenzl-vs-mpfr-cross-check.json)).

3. **Fractional rank $r$.**  The QOU substrate value $q_0 \approx
   1.1097$ has $X(q_0, z_0) = q^{2 r_0}$ with $r_0 \approx 2.5995$
   non-integer.  Wenzl 1988 specialises to integer-$N$
   $\mathrm{SU}_q(N)$ centralisers; the QOU case is the analytic
   continuation in the rank parameter, which is well-defined
   because the principal Schur specialisation is a rational
   function of $X$ (no integrality assumption).

## Empirical verification

The closed form has been verified against the linear-system
witness at $n = 3, \ldots, 11$ (193 partitions) to MPFR exact representation
precision (max per-partition $|\Delta| \le 4 \times 10^{-51}$):
[`y-lambda-wenzl-vs-mpfr-cross-check.json`](https://github.com/litlfred/qou/blob/main/computations/y-lambda-wenzl-vs-mpfr-cross-check.json).  Two independent
computational paths (closed-form principal Schur specialisation;
Hoefsmit linear-system inverse via the Rust `pyhecke_native`
kernel) agree at the precision floor.

## Lean formalisation

`wenzl-bridge-applicability-qou.lean` axiomatises the four-step
chain:

1. `schurWeylSetup`: from the QOU substrate axioms, produces the
   centraliser identity $H_n(R, q) = \mathrm{End}_H(V^{\otimes n})$.
2. `fibreFunctorMarkovTrace`: the fibre-functor trace restricted to
   the $H_n$-summand satisfies the Markov property at parameter
   $z$ fixed by $z \cdot \dim_q V = 1$.
3. `markovTraceFamilyOneDim`: the Chlouveraki HDR uniqueness — the
   type-$A$ Markov-trace family is one-parameter, normalisation pins
   the scale.
4. `wenzlBridgeYLambdaApplies`: combining the three, the unique
   Markov trace satisfies the Wenzl-bridge closed form.

Each step is a `sorry` with `-- Ref:` to the canonical source
(Chlouveraki HDR Thm 6.20, Wenzl 1988, Tannaka--Krein
reconstruction); the chain itself is a verified composition.
<!-- FILE_END: wenzl-bridge-applicability-qou.md -->

