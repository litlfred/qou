**Proposition (closed form for $y_\lambda$ via Wenzl bridge).**
*Let $\sigma_i$ be the symmetric Hecke generators of $H_n(R, q)$
satisfying $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ (eigenvalues
$q, -q^{-1}$), and let $\mathrm{tr}_M$ be the Jones-Markov trace
with parameter $z = 1/(q^{1/2} + q^{-1/2})$. The central
coefficients $y_\lambda$ in the expansion
$\mathrm{tr}_M = \sum_\lambda y_\lambda \chi_\lambda$ admit the
closed form*

$$
  \boxed{\;
    y_\lambda \;=\; \frac{s_\lambda(1, Q, Q^2, \ldots, Q^{r-1})}
                        {\sum_{\mu \,\vdash\, n} d_\mu \cdot s_\mu(1, Q, Q^2, \ldots, Q^{r-1})}
  \;}
$$

*where $Q = q^2$, $d_\mu = f^\mu$ is the classical hook-length
dimension of the $S_n$-irrep, $s_\lambda$ is the principal-
specialization Schur polynomial in $r$ variables, and $r$ is the
unique solution of*

$$
  q \cdot z \;=\; \frac{Q^r (1 - Q)}{1 - Q^r}
  \;=\; \frac{q^{2r}(1 - q^2)}{1 - q^{2r}},
$$

*i.e.*

$$
  r \;=\; \log_{q^2}\!\biggl(\frac{q \, z}{1 - q^2 + q \, z}\biggr)
  \;=\; \log_{Q}\!\biggl(\frac{q \, z}{1 - Q + q \, z}\biggr).
$$

*At the substrate value $q_0 \approx 1.110$, $z_0 \approx 0.499$,
this gives $r_0 \approx 2.5995$ (non-integer; lies between the
$\mathfrak{sl}(2)$ and $\mathfrak{sl}(3)$ Schur-Weyl-duality
levels).*

## Convention bridge

The Hecke algebra of type $A_{n-1}$ has two standard
parameterizations:

| | $\sigma$-convention (this paper) | $g$-convention (Wenzl-Orellana) |
|--|--|--|
| Quadratic | $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ | $g_i^2 = (Q - 1)g_i + Q$ |
| Eigenvalues | $q, -q^{-1}$ | $Q, -1$ |
| Markov param | $z = 1/(q^{1/2} + q^{-1/2})$ | $z_{\mathrm{GL}}$ |

The map $g_i := q \, \sigma_i$ realises an algebra isomorphism with
$Q = q^2$, and the Markov parameters are related by
$z_{\mathrm{GL}} = q \cdot z$.  This is the affine convention
shift; my $z$ does NOT correspond to the same Wenzl level $r$ as
the substitution $q_W \mapsto q_{\mathrm{my}}$ would suggest
([explicit $\alpha_k$ at $H_3$](#prop:explicit-alpha-k-h3); 10
candidates in `schur_element_identify.py`).

## Proof

By [Wenzl 1988] (cited in [Orellana, math/9806163, Theorem on
p.17]), the unique Markov trace on the type-A Iwahori-Hecke
algebra in $g$-convention with parameter $z_{\mathrm{GL}} = Q^r
(1 - Q)/(1 - Q^r)$ has weights $\omega_\lambda(Q) =
s_{\lambda, r}(Q)$ given by the principal-specialization Schur
function.  By [Chlouveraki HDR Theorem 6.20 (=Juyumaya Theorem 12,
$d=1$ case)], the type-A Markov-trace family is 1-dimensional,
parameterised by $z$.

The convention isomorphism $g = q\sigma$ transports $\mathrm{tr}_M$
on $\sigma$-Hecke (with my $z$) to $\mathrm{tr}_{\mathrm{GL}}$ on
$g$-Hecke (with $z_{\mathrm{GL}} = q z$).  Both traces have the
same expansion $\mathrm{tr} = \sum_\lambda y_\lambda \chi_\lambda$
for any choice of irreducible character basis (which is intrinsic
to the algebra, hence convention-independent).  By uniqueness, the
weights agree:

$$
  y_\lambda^{(\sigma)} \;=\; y_\lambda^{(g)} \;=\;
  \omega_\lambda(Q) / Z, \qquad Z := \sum_\mu d_\mu \omega_\mu(Q),
$$

normalised so $\mathrm{tr}_M(1) = \sum_\lambda y_\lambda d_\lambda = 1$.
$\square$

## Numerical verification

Per-partition agreement at H_3, H_4, H_5 (representative entries):

| $n$ | $\lambda$ | $y_\lambda$ (witness) | $y_\lambda$ (Wenzl bridge) | $\Delta$ |
|--|--|--:|--:|--:|
| 3 | $(3)$ | $+0.41539579$ | $+0.41539579$ | $\sim 10^{-16}$ |
| 3 | $(2,1)$ | $+0.28092963$ | $+0.28092963$ | $\sim 10^{-17}$ |
| 3 | $(1^3)$ | $+0.02274495$ | $+0.02274495$ | $\sim 10^{-17}$ |
| 4 | $(4)$ | $+0.22752693$ | $+0.22752693$ | $\sim 10^{-16}$ |
| 4 | $(3,1)$ | $+0.18786886$ | $+0.18786886$ | $\sim 10^{-17}$ |
| 4 | $(2,2)$ | $+0.06947330$ | $+0.06947330$ | $\sim 10^{-17}$ |
| 4 | $(2,1,1)$ | $+0.02358747$ | $+0.02358747$ | $\sim 10^{-17}$ |
| 4 | $(1^4)$ | $-0.00084253$ | $-0.00084253$ | $\sim 10^{-17}$ |
| 5 | $(5)$ | $+0.11814840$ | $+0.11814840$ | $\sim 10^{-16}$ |
| ... | ... | ... | ... | ... |

All differences are at numerical precision (10⁻¹⁶), confirming the
identity exactly.

## Significance

This **closes** the long-standing puzzle of the convention
mismatch between this paper's symmetric Hecke convention and the
standard Wenzl-Orellana literature formulas.  The bridge is:

1. Substitute $Q = q^2$ (not $Q = q$).
2. Substitute $z_{\mathrm{GL}} = q \cdot z$ (not $z_{\mathrm{GL}} = z$).
3. Apply Wenzl's $s_{\lambda, r}(Q)$ formula at the resulting $r$.

The earlier 10-candidate harness
([`schur_element_identify.py`](#)) failed because it tested
$Q = q$ or $Q = q^2$ with $z_{\mathrm{GL}} = z$ — missing the
required factor of $q$ in the Markov-parameter shift.

**Implications**:

- $y_\lambda$ at every $n$ now has a closed q-rational form in
  $\mathbb{Q}(q^{1/2})$ — no Rust kernel or PSLQ needed for
  symbolic extraction.  Just apply the Schur principal
  specialization formula at $Q = q^2$ with $r$ from the bridge
  equation.

- The y_λ values for $n = 5, \ldots, 12$ (currently only available
  numerically via MPFR witness) can now be derived symbolically
  by sympy's principal-specialization implementation — orders of
  magnitude faster than the linear-system solve.

- The depth-stratum decomposition Σ_{depth(λ)=k} $y_\lambda$ is
  gauge-invariant under this convention shift (verified to
  10⁻¹⁶ in [GB filtration gauge invariance witness](#)), as
  expected since the GB filtration is partition-combinatorial.

## Witness

[`folio-assistant/computations/gb_filtration_gauge_invariance_test.py`](#)
implements the Wenzl-bridge formula and verifies per-partition
agreement at $n = 3, \ldots, 9$.  Output:
`gb-filtration-gauge-invariance.witness.json`.

[`folio-assistant/computations/y_lambda_wenzl_bridge_extended.py`](#)
extends symbolic $y_\lambda$ to **all 270 partitions across $n = 2, \ldots, 12$
in $45$ seconds total** via direct sympy substitution into the
principal-specialization formula:

| $n$ | $p(n)$ | symbolic compute time |
|--:|--:|--:|
| 2 | 2 | 0.03 s |
| 3 | 3 | 0.02 s |
| 4 | 5 | 0.05 s |
| 5 | 7 | 0.12 s |
| 6 | 11 | 0.30 s |
| 7 | 15 | 0.63 s |
| 8 | 22 | 1.41 s |
| 9 | 30 | 2.89 s |
| 10 | 42 | 5.82 s |
| 11 | 56 | 11.27 s |
| 12 | 77 | 22.77 s |
| **total** | **270** | **45.31 s** |

Compare to:
- Sympy linear-system $y_\lambda$ solve at $n=4$: $\sim 30$ s,
  RecursionError at $n = 5$.
- MPFR Hoefsmit-matrix path: $\sim 25$ minutes for $n = 11$ alone,
  failed at $n = 12$ on the $462 \times 462$ sparse seminormal
  matmul for partition $(4, 4, 4)$.

The Wenzl bridge gives speedups of $\sim 30\times$ to $\sim 1000\times$
depending on $n$, while producing exact symbolic q-rational closed
forms in $\mathbb{Q}(q^{1/2})$.

Witness: `y-lambda-wenzl-bridge-symbolic-witness.json` (6.7 MB, 270
unsimplified expressions; sympy `simplify` triggers RecursionError on
the larger ones, but they evaluate correctly via numerical
substitution and match the MPFR witness exactly to machine precision
at $n \in \{3, 4, 5, 6, 9, 12\}$ sample points).

## Lean formalisation

[`y-lambda-closed-form-wenzl-bridge.lean`](#) defines:

- `jonesMarkovZ q := 1 / (√q + 1/√q)`
- `wenzlQ q := q²`,  `wenzlZ q := q · jonesMarkovZ q`
- `wenzlX q := wenzlZ q / (1 - wenzlQ q + wenzlZ q)` — the
  explicit `Q^r` substitution, avoiding fractional exponents
- `wenzlSchurElement λ Q X` — the principal-specialization Schur
  element (axiomatic stub pending full Mathlib partition machinery)
- `wenzlNormalization parts Q X := Σ_µ d_µ · s_{µ,r}(Q)`
- `yLambdaWenzlBridge parts λ q := s_λ / Z`

The main theorem `y_lambda_closed_form_wenzl_bridge` asserts that
this equals the Jones-Markov coefficient `jonesMarkovCoefficient q λ`
defined directly from the trace.  The proof composes:

1. [Wenzl 1988] — `s_{µ, r}(Q)` is the Markov-trace weight at
   parameter `z_GL = Q^r(1-Q)/(1-Q^r)` in the `g`-Hecke convention.
2. The convention isomorphism `G = q σ` sends σ-Hecke (eigenvalues
   `q, -q⁻¹`, parameter `z`) to `g`-Hecke (eigenvalues `Q = q²`,
   `-1`, parameter `z_GL = q · z`).
3. [Chlouveraki HDR Theorem 6.20] — the type-A Markov-trace family
   is 1-parameter, so the trace is uniquely determined by its
   `z`-value.

The companion theorem `wenzl_bridge_unique` states that the
substitution `(Q, z_GL) = (q², q · z)` is the unique convention map
realising the Jones-Markov trace via the Wenzl formula — corollary
of the 1-parameter family.

`y_lambda_bridge_numerical_agreement` records the empirical witness
data (machine-precision agreement) as a `True := trivial` placeholder.
