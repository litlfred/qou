# Formal equivalence proof — $y_\lambda(q)$ and $\mathrm{tr}_M$

> **Notation note (added 2026-06-04, PR #1794).** This audit uses
> the symbol $r$ for the spinor information rate $q^{1/2}$. As of
> 2026-06-04 the canonical symbol is **$\check{q}$** (q-háček) —
> read $r \mapsto \check{q}$ throughout. The audit's content is
> unchanged; only the name of the symbol was updated.

**Branch.** `claude/hoefsmit-2x2-fix` (PR #546 round-3).
**Witness.** [`y_lambda_equivalence_proof.witness.json`](../../computations/y_lambda_equivalence_proof.witness.json)
**Script.** [`y_lambda_equivalence_proof.py`](../../computations/y_lambda_equivalence_proof.py)

## Setup — base ring

Throughout, fix the **integer Laurent ring**
$$
R \;=\; \mathbb{Z}\big[r,\,r^{-1}\big],\qquad r = q^{1/2},\quad r^2 = q,
$$
where $r$ is the **spinor information rate** — the eigenvalue of
the elementary half-twist on the spin-½ fundamental rep of
$\mathrm{SU}_q(2)$ (see [`notation-register.md`](../../content/quantum-observable-universe/notation/notation-register.md) Ch 4
and [`notation-collisions.md`](../../content/quantum-observable-universe/notation/notation-collisions.md)).
The Markov parameter is $z = 1/(r + r^{-1})$.

The seminormal Hoefsmit matrices live in $\mathrm{Frac}(R)$ since the
2×2 blocks invert factors $(1 - q^{2\rho})$. The Wedderburn weights
$y_\lambda(q)$ also live in $\mathrm{Frac}(R)$ (they are explicit
quotients of integer Laurent polynomials in $r$).

**Important:** all polynomial identities below hold in $R$ itself,
not just in $\mathrm{Frac}(R)$. By base-change they descend to
$R \otimes_\mathbb{Z} S$ for **any** commutative ring $S$ — in
particular to $\mathbb{F}_p[r,r^{-1}]$ for any prime $p$ where the
relevant denominators do not vanish.

## Statement

Let $H_n(q)$ be the Iwahori-Hecke algebra over $\mathrm{Frac}(R)$
with Markov parameter $z = 1/(r + r^{-1})$. Let $y_\lambda(q)$
denote the Wedderburn weight in the decomposition
$\mathrm{tr}_M = \sum_{\lambda \vdash n} y_\lambda(q) \cdot \chi^\lambda$.

**Theorem (equivalence of derivations).** Two derivations of
$y_\lambda(q)$ are equivalent as elements of $\mathrm{Frac}(R)$:

- **Path A (linear system on the ladder).** Solve $A \cdot y = b$
  where $A_{ij} = \chi^{\lambda_j}(\sigma_1 \cdots \sigma_{i-1})$
  for $i = 0, 1, \ldots, n-1$ and $b_i = z^i$.
- **Path B (Wenzl Schur principal specialization).** Set
  $$
  y_\lambda(q) = \frac{1}{Z}\, s_\lambda(1, Q, Q^2, \ldots, Q^{r-1}),
  \qquad Q = q^2,\ \ Q^r = \frac{z_W}{1 - Q + z_W},\ \ z_W = q z,
  $$
  with $s_\lambda$ the Schur principal specialisation
  $Q^{n(\lambda)} \prod_{x \in \lambda} (1 - Q^{r + c(x)})/(1 - Q^{h(x)})$
  and $Z = \sum_\mu f^\mu \cdot s_\mu$ enforcing $\mathrm{tr}_M(1) = 1$.

Both paths produce the same rational functions $y_\lambda(q)$.

## Proof

### Mathematical proof (uniqueness)

The Ocneanu Markov trace on $H_n(q)$ is the unique linear functional
satisfying

$$
\mathrm{tr}_M(1) = 1, \qquad
\mathrm{tr}_M(x \sigma_n) = z \cdot \mathrm{tr}_M(x) \ \forall x \in H_n,
\qquad
\mathrm{tr}_M(xy) = \mathrm{tr}_M(yx).
$$

Existence + uniqueness: Ocneanu (1985); Jones (1987); Wenzl (1988).
Therefore any linear functional satisfying these axioms is *the*
Markov trace, so all decompositions
$\mathrm{tr}_M = \sum_\lambda y_\lambda \chi^\lambda$ must agree on
$y_\lambda$ (since the $\chi^\lambda$ are linearly independent as
class functions on $H_n$).

- **Path A produces a Markov trace.** By construction the linear
  system encodes $\mathrm{tr}_M(1) = 1$, $\mathrm{tr}_M(\sigma_i) = z$,
  $\mathrm{tr}_M(\sigma_1 \sigma_2) = z^2$, … on a basis that spans
  the class-function dual; the resulting linear extension is a
  trace satisfying the Markov property by induction on word length.

- **Path B produces a Markov trace.** Wenzl (1988, Theorem 5.1)
  derives the Schur principal specialisation as the explicit form
  of the Markov trace under the substitution $Q = q^2$, $z_W = q z$,
  $Q^r = z_W / (1 - Q + z_W)$.

By uniqueness, $y_\lambda^A = y_\lambda^B$ for every $\lambda \vdash n$.
$\square$

### Computational verification (polynomial identity in $R$)

For $n = 3$ ($\lambda \in \{(3), (2,1), (1,1,1)\}$), write
$y_\lambda^A = P_\lambda^A / Q_\lambda^A$ and
$y_\lambda^B = P_\lambda^B / Q_\lambda^B$ as **integer** Laurent
polynomials $P, Q \in R = \mathbb{Z}[r, r^{-1}]$. Then sympy's
`sp.expand` reduces the cleared-denominator form

$$
\Delta_\lambda \;:=\; P^A_\lambda \cdot Q^B_\lambda \;-\; P^B_\lambda \cdot Q^A_\lambda
$$

to **exactly** $0$ as a Laurent polynomial in $R$:

| $\lambda$ | $\Delta_\lambda \in R$ | integer coeffs? |
|---|---|---|
| $(3)$ | $0$ ✓ | ✓ |
| $(2,1)$ | $0$ ✓ | ✓ |
| $(1,1,1)$ | $0$ ✓ | ✓ |

This is a **polynomial identity** in $\mathbb{Z}[r, r^{-1}]$, hence
holds **in any commutative ring** by base-change:

$$
\Delta_\lambda \;=\; 0 \;\;\text{in}\;\; S[r, r^{-1}] \;\;\text{for all commutative}\; S,
$$

including $S = \mathbb{F}_p$ for every prime $p$. Therefore
$y_\lambda^A = y_\lambda^B$ in $\mathrm{Frac}(\mathbb{F}_p[t, t^{-1}])$
whenever $Q_\lambda^A, Q_\lambda^B \neq 0$ in that field — i.e. for
all primes $p$ where the explicit cyclotomic-factor denominators
do not vanish.

This is a strictly stronger statement than numerical agreement at
any specific $q_0$, and is also stronger than rational-function
equality over $\mathbb{Q}(t)$: it is a universal polynomial
identity over $\mathbb{Z}$.

(For $n \geq 4$ the linear system is rank-deficient on the ladder
basis alone — there are more partitions than ladder elements — so
Path A must be augmented with extra basis elements drawn from
non-ladder Markov-cyclic identities. The Wenzl Schur formula gives
the closed form for any $n$, with the linear-system identification
re-imposable as a uniqueness argument once the basis is completed.)

## Corollary — equivalence of $\mathrm{tr}_M$ algorithms

Two algorithms for computing the Markov trace on a braid word $\beta$
exist in this codebase:

- **Wedderburn assembly.**
  $\mathrm{tr}_M(\beta) = \sum_\lambda y_\lambda(q) \cdot \chi^\lambda(\beta)$
  using closed-form $y_\lambda$ (either path A or B above) and
  symbolic seminormal Hoefsmit $\chi^\lambda$
  ([`hoefsmit_symbolic.chi_lambda_symbolic`](../../computations/hoefsmit_symbolic.py)).

- **Markov-peel recursive ascent.**
  [`markov_peel.tr_M_element`](../../computations/markov/markov_peel.py)
  recursively reduces $\beta$ via $\mathrm{tr}_M(x \sigma_n) = z \mathrm{tr}_M(x)$
  until reaching the constant term $\mathrm{tr}_M(1) = 1$.

**Corollary.** Both algorithms compute the same rational function in
$q$ for every braid word $\beta \in B_n$, $n \geq 1$.

**Proof.** Both satisfy the Markov axioms by construction (Wedderburn
trivially; markov_peel by recursive application). By the uniqueness
theorem, they agree as linear functionals on $H_n$, hence on every
braid-word input. $\square$

### Numerical confirmation

| atom | Wedderburn at $q_0$ | markov_peel at $q_0$ | Δ |
|---|---|---|---:|
| proton (A=1) | $1.06530622859239$ | $1.06530622859239$ | $\le 6\!\times\!10^{-15}$ |
| neutron (A=1) | $0.92323329716958$ | $0.92323329716958$ | $\le 6\!\times\!10^{-15}$ |
| deuteron (A=2) | $0.38828647154771$ | $0.38828647154771$ | $\le 4\!\times\!10^{-16}$ |

The residual is the float-precision floor of $q_0$ itself — the
underlying rational-function identity holds exactly.

## Lean formalisation (open)

The uniqueness argument above is a candidate for Lean formalisation:

```lean
-- Sketch (not committed):
theorem markov_trace_unique
    (T₁ T₂ : H q n →ₗ[R] R)
    (h₁_unit  : T₁ 1 = 1)  (h₂_unit  : T₂ 1 = 1)
    (h₁_markov : ∀ x, T₁ (x * σ n) = z * T₁ x)
    (h₂_markov : ∀ x, T₂ (x * σ n) = z * T₂ x)
    (h₁_trace  : ∀ x y, T₁ (x * y) = T₁ (y * x))
    (h₂_trace  : ∀ x y, T₂ (x * y) = T₂ (y * x)) :
  T₁ = T₂ := by
  sorry  -- standard, but not yet formalised here
```

Once committed, the Lean proof would axiomatise the trace-axiom
constraints and derive uniqueness via a basis argument (e.g. via the
canonical basis of reduced braid words $\sigma_{i_1} \cdots \sigma_{i_k}$).

## Files

- [`computations/markov/markov_weights_symbolic.py`](../../computations/markov/markov_weights_symbolic.py)
  — both paths.
- [`computations/y_lambda_equivalence_proof.py`](../../computations/y_lambda_equivalence_proof.py)
  — equivalence verification script.
- [`computations/y_lambda_equivalence_proof.witness.json`](../../computations/y_lambda_equivalence_proof.witness.json)
  — sympy-symbolic identity witness.
