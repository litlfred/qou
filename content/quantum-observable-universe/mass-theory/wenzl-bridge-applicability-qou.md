**Proposition (applicability of the Wenzl-bridge formula in QOU).**
*Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be a QOU substrate
satisfying the [archimedean axioms](#def\:rigid-monoidal-category)
with self-dual fundamental object $A \in \mathbf{C}$ and fibre
functor $\tau \colon \mathbf{C} \to R\text{-mod}$
([fibre functor](#prop\:fibre-functor-atlas)).  Let
$H := \mathrm{Aut}^\otimes(\tau)$ be the Tannaka--Krein Hopf algebra
([Tannaka--Krein](#prop\:tannaka-krein-reconstruction)) and
$V := \tau(A)$.  Then the Markov trace
$\mathrm{tr}_M$ on the Iwahori--Hecke algebra $H_n(R, q)$
([Jones--Markov trace](#thm\:jones-markov-trace)) is uniquely
determined by $(\mathbf{C}, A, \tau)$ up to the normalisation
$\mathrm{tr}_M(1) = 1$, and equals the closed form
([Wenzl-bridge $y_\lambda$](#prop\:y-lambda-closed-form-wenzl-bridge)).*

## Why the QOU substrate satisfies the hypotheses

| Hypothesis                                                            | QOU realisation                                                                                                                   |
| --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Rigid :refterm[braided monoidal category]{#braided-monoidal-category} | $\mathbf{C}$ as the [rigid :refterm[braided monoidal category]{#braided-monoidal-category}](#def\:rigid-monoidal-category) of QOU |
| Self-dual fundamental object                                          | $A$ as the [fundamental confined particle](#def\:confined-particle), self-dual via $A^* \cong A$ from the antipode                |
| Fibre functor                                                         | [$\tau \colon \mathbf{C} \to R\text{-mod}$](#prop\:fibre-functor-atlas) realising the state bundle                                |
| Tannaka--Krein Hopf algebra                                           | $H = U_q(\mathfrak{sl}_2)$ in the running QOU example                                                                             |
| $V = \tau(A)$ has $q$-dimension $[2]_q^{\mathrm{symm}}$               | direct from $A$ being the spin-$\tfrac{1}{2}$ representation                                                                      |

## Consequences

1. **No fitting.**  The Wenzl-bridge formula is *the* closed form
   for $y_\lambda$ in QOU; no parameter is chosen to fit observables.

2. **Unique extension to $n \ge 5$.**  The
   ([procedure](#prop\:alpha-k-derivation-procedure))
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
witness at $n = 3, \ldots, 11$ (193 partitions) to MPFR 50-dps
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
