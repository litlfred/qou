<!-- FILE_START: alpha-k-procedure-atom-knot-mass-intro.md -->
Continuation of the preceding sub-section.

The arc proceeds through the atom-knot mass derivation (with tables and a proof block), the joint-tower SDP confinement assembly with table data, and the $y_\lambda$ closed-form Wenzl-bridge identification.  The output is the per-atom-knot mass coefficient table consumed by the next sub-section's Wenzl-bridge specialisation.
<!-- FILE_END: alpha-k-procedure-atom-knot-mass-intro.md -->

<!-- FILE_START: joint-tower-sdp-confinement.md -->
**Statement (design specification).** Let $\mathcal{U}$ be a quantum
observable universe at substrate parameter $q_0$. The **joint
mass-tower confinement SDP** at $q_0$ is the semidefinite program

$$
\boxed{\quad
\begin{aligned}
& \text{find} && \big( c_{\mathfrak{H}, w}(q_0) \big)_{\mathfrak{H} \in \mathcal{R}, \, w \in S_{n_0(\mathfrak{H})}} \in \mathbb{Q}, \\
& \text{such that} && \forall \, \mathfrak{H} \in \mathcal{R}: \\
& && \quad T_w(\mathfrak{H}) := \sum_{w \in S_{n_0(\mathfrak{H})}} c_{\mathfrak{H}, w}(q_0) \cdot T_w \;\in\; H_{n_0(\mathfrak{H})}(q_0) \\
& && \quad \rho_\lambda(T_w(\mathfrak{H})) \succeq 0 \text{ for all Wedderburn blocks } \lambda \vdash n_0(\mathfrak{H}) \\
& && \quad \text{(GB-filtration grading: } c_{\mathfrak{H}, w} \neq 0 \Rightarrow \ell(w) \in \mathrm{Filt}(\mathfrak{H})\text{)} \\
& && \quad \text{(jet-order ordering: SDP variable indexing respects jet order)} \\
& \text{cross-level constraints:} && \forall \, \mathfrak{H} \to \mathfrak{H}' \text{ in tower:} \\
& && \quad \pi_{\mathfrak{H} \to \mathfrak{H}'} \big( T_w(\mathfrak{H}) \big) \;=\; T_w(\mathfrak{H}')
\end{aligned}
\quad}
$$

where $\mathcal{R}$ is the registry of confined particles
([def:confined-particle](#def:confined-particle)), $\rho_\lambda$ is
the Wedderburn block $\lambda$-projection, and
$\pi_{\mathfrak{H} \to \mathfrak{H}'}$ is the canonical embedding
$H_{n_0(\mathfrak{H}')} \hookrightarrow H_{n_0(\mathfrak{H})}$
induced by the recursive structure of $\mathcal{R}$ (e.g.\ ${}^2$H = ${}^4$He
embeds via the strand-augmentation $H_{12} \hookrightarrow H_{18}$).

A solution $(c_{\mathfrak{H}, w}(q_0))$ is a **structured certificate**
of the canonical Hecke elements $\{T_w(\mathfrak{H})\}_{\mathfrak{H} \in \mathcal{R}}$
together with the **GB-filtration certificate** and **jet-order log**
([gb-filtration-jet-order.witness.json](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/gb-filtration-jet-order.witness.json))
on each. Existence is asserted by [prop:confinement-sdp](#prop:confinement-sdp);
this proposition refines that with the joint-tower / GB-filtration /
jet-order structure required by the categorical mass derivation
([prop:atom-knot-mass-derivation](#prop:atom-knot-mass-derivation)).

## SDP variables

For each particle $\mathfrak{H} \in \mathcal{R}$ with strand count
$n_0 = n_0(\mathfrak{H})$, the variables are
$c_{\mathfrak{H}, w}(q_0) \in \mathbb{Q}$ for every $w \in S_{n_0}$.
These index the basis $\{T_w\}_{w \in S_{n_0}}$ of $H_{n_0}(q_0)$ in
GB-NF. Total variable count is $\sum_{\mathfrak{H}} |S_{n_0(\mathfrak{H})}|
= \sum_{\mathfrak{H}} n_0(\mathfrak{H})!$, which for $\mathcal{R}$
covering up to ${}^{40}$Ca ($n_0 = 120$) is astronomically large. In practice
the **filtration cuts the problem down**: only $w$ with $\ell(w) \leq L$
for some cutoff $L = O(n_0)$ contribute non-by definition (most $T_w$ are
zero for atomic braids of finite GB-NF length), so the effective
variable count is $\sum_{\mathfrak{H}} \binom{n_0}{L}$ which is
polynomial in $n_0$ for fixed $L$.

## SDP constraints

### (1) Per-particle Wedderburn positivity

For each $\mathfrak{H}$ and each Wedderburn block $\lambda \vdash n_0$,
the block image
$\rho_\lambda(T_w(\mathfrak{H})) \in M_{d_\lambda}(\mathbb{Q})$
must be positive semidefinite. This is the standard confinement SDP
constraint ([prop:confinement-sdp](#prop:confinement-sdp)), expressed
per Wedderburn block via the explicit Hoefsmit seminormal form
([prop:hoefsmit-seminormal-form](#prop:hoefsmit-seminormal-form)).

### (2) GB-filtration grading

The certificate variables $c_{\mathfrak{H}, w}(q_0)$ must support a
filtration: there is a graded structure $\mathrm{Filt}(\mathfrak{H}) =
\{\ell_0(\mathfrak{H}), \ell_1(\mathfrak{H}), \ldots\} \subseteq \mathbb{Z}_{\geq 0}$
such that $c_{\mathfrak{H}, w} = 0$ for $\ell(w) \notin \mathrm{Filt}(\mathfrak{H})$.
This is encoded as a **structural sparsity pattern** on the SDP
variables: the support of the certificate per Wedderburn block lives
in a fixed Coxeter-length-graded subspace. The GB spectral sequence
collapse at $E_2$
([prop:spectral-sequence-collapse](#prop:spectral-sequence-collapse))
implies the filtration is *finite* (at most polynomial-degree cutoff
in $n_0$); the SDP need not enumerate all of $S_{n_0}$.

### (3) Jet-order ordering (variable indexing)

The SDP variables are indexed by *jet order* — i.e.\ the temporal
sequence of GB reductions. Concretely: at each Wedderburn block
$\lambda$, the variables $\{c_{\mathfrak{H}, w}\}_{\ell(w) \leq L}$
are ordered by an admissible jet sequence as in
[gb-filtration-jet-order.witness.json](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/gb-filtration-jet-order.witness.json).
Two effects:

- The SDP is decomposed into a **chain of sub-problems** along the
 jet order, each refining the previous. Solutions extend accordingly
 one jet step at a time.
- The jet-order log emitted with the certificate makes the SDP
 output reproducible: re-running with the same jet ordering yields
 the same coefficients $c_{\mathfrak{H}, w}(q_0)$.

### (4) Cross-level consistency

For each tower-edge $\mathfrak{H} \to \mathfrak{H}'$ where
$\mathfrak{H}'$ is a constituent of $\mathfrak{H}$ (e.g.\ ${}^{4}$He is a
constituent of ${}^{8}$Be in the α-cluster decomposition), the canonical
embedding
$\pi_{\mathfrak{H} \to \mathfrak{H}'} : H_{n_0(\mathfrak{H}')}(q_0) \hookrightarrow H_{n_0(\mathfrak{H})}(q_0)$
must send $T_w(\mathfrak{H}')$ to $T_w(\mathfrak{H})$ inside the
relevant cosets. This is the constraint that **per-atom SDPs alone
cannot enforce**: only the joint formulation guarantees the
filtration grading and jet ordering are consistent across confinement
levels.

The set of tower edges is determined by the recursive structure of
$\mathcal{R}$ ([def:confined-particle](#def:confined-particle)). At
$\ell \leq 2$ the explicit edges are:

See [Table 1](#tbl:joint-tower-sdp-confinement-table1-data).

For ${}^{6}$Li, ${}^{7}$Li the embedding is open: $\mathfrak{H} \to \{\alpha, p, n\}$
or $\mathfrak{H} \to \{\alpha, p, 2n\}$ respectively, with explicit
embeddings $H_{18} \hookleftarrow H_{12} \otimes H_3 \otimes H_3$ and
$H_{21} \hookleftarrow H_{12} \otimes H_3 \otimes H_3 \otimes H_3$.

## Existence

By [prop:confinement-sdp](#prop:confinement-sdp), the per-atom SDP is
feasible at $q_0$ for every $\mathfrak{H} \in \mathcal{R}$. The joint
SDP is feasible iff the cross-level constraints (4) are simultaneously
satisfiable, which holds because the embeddings $\pi_{\mathfrak{H} \to \mathfrak{H}'}$
preserve Wedderburn-block positivity (the canonical embedding of
$H_m(q_0) \hookrightarrow H_n(q_0)$ for $m \leq n$ sends each Wedderburn
block of $H_m$ into a sum of compatible blocks of $H_n$). Combined
with the GB filtration sparsity (2) and jet-order indexing (3), the
SDP is well-posed and admits at least one structured solution.

## Output

A solution to the joint-tower SDP is a structured certificate

$$
\Phi(q_0) \;:=\; \big\{ \big( T_w(\mathfrak{H}), \mathrm{Filt}(\mathfrak{H}), \mathrm{JetLog}(\mathfrak{H}) \big) \big\}_{\mathfrak{H} \in \mathcal{R}}
$$

— one canonical Hecke element per atom, with its filtration grading
and jet-order log. Combined with the structural prefactor
$\rho(\mathfrak{H}) \in \mathbb{Z}_{>0}$ read off from the Wedderburn
multiplicity of $T_w(\mathfrak{H})$, this gives the categorical mass
invariant
$M(\mathfrak{H}) = \rho(\mathfrak{H}) \cdot \mathrm{tr}_M(T_w(\mathfrak{H}))$
for the atom-knot mass derivation
([prop:atom-knot-mass-derivation](#prop:atom-knot-mass-derivation)).
## Refs

- Confinement SDP: [prop:confinement-sdp](#prop:confinement-sdp).
- GB filtration / jet-order certificate format:
 [gb-filtration-jet-order.witness.json](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/gb-filtration-jet-order.witness.json) +
 the canonical formalism.
- GB spectral-sequence collapse:
 [prop:gb-spectral-sequence](#prop:gb-spectral-sequence),
 [prop:spectral-sequence-collapse](#prop:spectral-sequence-collapse).
- Wedderburn block decomposition:
 [prop:wedderburn-trace-identity](#prop:wedderburn-trace-identity).
- Hoefsmit seminormal form for explicit block matrices:
 [prop:hoefsmit-seminormal-form](#prop:hoefsmit-seminormal-form).
- Mass identity that consumes this output:
 [prop:atom-knot-mass-derivation](#prop:atom-knot-mass-derivation).
<!-- FILE_END: joint-tower-sdp-confinement.md -->

<!-- FILE_START: y-lambda-closed-form-wenzl-bridge.md -->
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

## Applicability in QOU

The QOU axioms force the Wenzl-bridge formula to apply: the
Schur--Weyl + Tannaka--Krein + 1-dim Markov-trace family chain
selects a unique Markov trace on $H_n(R, q)$, and the closed form
below is its only realisation.  The full four-step derivation
(Schur--Weyl setup, fibre-functor trace = Markov trace,
1-parameter family, Wenzl-bridge supplies the closed form) is
proven in
([Wenzl-bridge applicability in QOU](#prop:wenzl-bridge-applicability-qou)).

## Convention bridge

The Hecke algebra of type $A_{n-1}$ has two standard
parameterizations:

See [Table 1](#tbl:y-lambda-closed-form-wenzl-bridge-table1-data).

The map $g_i := q \, \sigma_i$ realises an algebra isomorphism with
$Q = q^2$, and the Markov parameters are related by
$z_{\mathrm{GL}} = q \cdot z$.  This is the affine convention
shift; the $\sigma$-convention $z$ does NOT correspond to the same
Wenzl level $r$ as the substitution $q_W \mapsto q$ would suggest
([explicit $\alpha_k$ at $H_3$](#prop:explicit-alpha-k-h3); 10
candidates in the formal derivation).
## Significance

This resolves the convention mismatch between this paper's
symmetric Hecke convention and the standard Wenzl-Orellana
literature formulas.  The bridge is:

1. Substitute $Q = q^2$ (not $Q = q$).
2. Substitute $z_{\mathrm{GL}} = q \cdot z$ (not $z_{\mathrm{GL}} = z$).
3. Apply Wenzl's $s_{\lambda, r}(Q)$ formula at the resulting $r$.

A 10-candidate identification harness without the factor of $q$ in
the Markov-parameter shift
([the formal derivation](#)) fails to recover the closed
form, since it tests $Q = q$ or $Q = q^2$ with $z_{\mathrm{GL}} = z$
— missing the required factor of $q$.

**Implications**:

- $y_\lambda$ at every $n$ has a closed q-rational form in
  $\mathbb{Q}(q^{1/2})$ — no Rust kernel or PSLQ needed for
  symbolic extraction.  Apply the Schur principal-specialization
  formula at $Q = q^2$ with $r$ from the bridge equation.

- The $y_\lambda$ values for $n = 5, \ldots, 12$ (otherwise only
  available canonical via MPFR witness) derive symbolically via
  sympy's principal-specialization implementation — orders of
  magnitude faster than the linear-system solve.

- The depth-stratum decomposition Σ_{depth(λ)=k} $y_\lambda$ is
  gauge-invariant under this convention shift (verified to
  $10^{-16}$ in [GB filtration gauge invariance witness](#)), as
  expected since the GB filtration is partition-combinatorial.

## Witness

[the formal derivation](#)
implements the Wenzl-bridge formula and verifies per-partition
agreement at $n = 3, \ldots, 9$.  Output:
`gb-filtration-gauge-invariance.witness.json`.

[the formal derivation](#)
extends symbolic $y_\lambda$ to **all 270 partitions across $n = 2, \ldots, 12$
in $45$ seconds total** via direct sympy substitution into the
principal-specialization formula:

See [Table 3](#tbl:y-lambda-closed-form-wenzl-bridge-table3-data).

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
the larger ones, but they evaluate correctly via canonical
substitution and match the MPFR witness exactly to machine precision
at $n \in \{3, 4, 5, 6, 9, 12\}$ sample points).

## Lean formalisation

[`y-lambda-closed-form-wenzl-bridge.lean`](#) defines:

- `jonesMarkovZ q := 1 / (Real.sqrt q + 1 / Real.sqrt q)`
- `wenzlQ q := q^2`,  `wenzlZ q := q * jonesMarkovZ q`
- `wenzlX q := wenzlZ q / (1 - wenzlQ q + wenzlZ q)` — the
  explicit `Q^r` substitution, avoiding fractional exponents
- `wenzlSchurElement λ Q X` — the principal-specialization Schur
  element (axiomatic axiomatised full Mathlib partition machinery)
- `wenzlNormalization parts Q X := Σ_µ d_µ * s_{µ,r}(Q)`
- `yLambdaWenzlBridge parts λ q := s_λ / Z`

The main theorem `y_lambda_closed_form_wenzl_bridge` asserts that
this equals the Jones-Markov coefficient `jonesMarkovCoefficient q λ`
defined directly from the trace.  The proof composes:

1. [Wenzl 1988] — `s_{µ, r}(Q)` is the Markov-trace weight at
   parameter `z_GL = Q^r(1-Q)/(1-Q^r)` in the `g`-Hecke convention.
2. The convention isomorphism $G = q\sigma$ sends $\sigma$-Hecke
   (eigenvalues $q, -q^{-1}$, parameter $z$) to $g$-Hecke
   (eigenvalues $Q = q^{2}$, $-1$, parameter $z_{\mathrm{GL}} = q \cdot z$).
3. [Chlouveraki HDR Theorem 6.20] — the type-A Markov-trace family
   is 1-parameter, so the trace is uniquely determined by its
   `z`-value.

The uniqueness of the convention shift
$(Q, z_{\mathrm{GL}}) = (q^2, q \cdot z)$ is recorded at two layers:

1. **`wenzl_bridge_unique_definitional q`** — `rfl`-discharge of the
   convention iso definitions: `wenzlQ q = q^2` and `wenzlZ q = q
   \cdot \mathrm{jonesMarkovZ}\,q` are forced by the eigenvalue
   transport `(q, -q^{-1}) \mapsto (q^2, -1)` and the Markov-axiom
   transport `\mathrm{tr}(x \cdot \sigma_n) = z \cdot \mathrm{tr}(x)
   \mapsto \mathrm{tr}(x \cdot g_n) = (q \cdot z) \cdot \mathrm{tr}(x)`.
   Definitions admit no degrees of freedom.

2. **`wenzl_bridge_unique_categorical q`** — conditional theorem
   under `[MarkovTraceFamilyOneDim ℝ q (jonesMarkovZ q)]`. Once
   Chlouveraki HDR Theorem 6.20 is taken as a class instance
   (1-dimensionality of the type-A Markov-trace family), the
   definitional layer (1) maps trace-uniqueness onto parameter-pair
   uniqueness. Per AGENTS.md §3b-cond, this is a *rigorous
   conditional result* — fully verified by Lean modulo the named
   class axiomatising the cited theorem.

The deprecated `wenzl_bridge_unique q` is retained as an alias for
the definitional layer; the original quantification "for all
$(Q', z')$ reproducing the canonical $y_\lambda$ values, $(Q', z')
= (q^2, q \cdot z)$" was structurally vacuous on the ansatz
Schur-element model.
<!-- FILE_END: y-lambda-closed-form-wenzl-bridge.md -->

