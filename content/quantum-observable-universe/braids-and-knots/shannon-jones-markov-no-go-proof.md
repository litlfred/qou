**Proof.**

*A single-witness existence claim: at $n = 4$ and the substrate
parameter $q_0 \approx 1.1097$, the Jones--Markov block weight
$y_{(1,1,1,1)}(q_0)$ is strictly negative.  We do not trust the
prior literature on this point — we re-derive it.*

**Step 1: Independent re-computation of $y_\lambda$ at $n = 4$.**

The Jones--Markov weights $\{y_\lambda^{(n)}\}_{\lambda \vdash n}$
are defined by the central decomposition $\mathrm{tr}_M = \sum_\lambda
y_\lambda \chi_\lambda$ on $H_n(R, q)$
([alpha-k derivation procedure](#prop:alpha-k-derivation-procedure)).
For $n = 4$ the system is a $5 \times 5$ linear equation
$A(q_0)\, y = b(q_0)$ where:

- the rows are indexed by the five conjugacy-class
  representatives $w_\mu$ for $\mu \vdash 4$;
- $A_{\mu\lambda} = \chi_\lambda(w_\mu)$ is computed by tracing the
  product of seminormal-representation matrices;
- $b_\mu = z^{n - \ell(\mu)}$ with $z = 1/(\sqrt{q_0} +
  1/\sqrt{q_0})$.

The script
[`tau_codim_conjectures_validate.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/tau_codim_conjectures_validate.py)
re-runs this solve from scratch using
`y_lambda_jones_markov_witness.solve_jones_markov_weights` and
records the result at
[`tau-codim-conjectures-validation.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/tau-codim-conjectures-validation.witness.json).
The output:

| $\lambda$ | $y_\lambda(q_0)$ |
|---|---|
| $(4)$ | $+2.275 \times 10^{-1}$ |
| $(3,1)$ | $+1.879 \times 10^{-1}$ |
| $(2,2)$ | $+6.947 \times 10^{-2}$ |
| $(2,1,1)$ | $+2.359 \times 10^{-2}$ |
| $(1,1,1,1)$ | $\mathbf{-8.4253 \times 10^{-4}}$ |

with linear-system condition $\sim 3$ and residual $\sim 10^{-16}$.

**Step 2: Cross-check with three independent pathways.**

The validation script also lifts $y_{(1,1,1,1)}(q_0)$ from two
pre-existing witnesses for cross-checking:

| Pathway | $y_{(1,1,1,1)}(q_0)$ |
|---|---|
| Fresh numpy linear solve (this PR) | $-8.42527491154525 \times 10^{-4}$ |
| Pre-existing 50-digit mpfr witness | $-8.42527491154563 \times 10^{-4}$ |
| Sympy symbolic $q$-rational solve | $-8.42527491154563 \times 10^{-4}$ |

Maximum pairwise difference: $3.8 \times 10^{-17}$ (machine
$\epsilon$).  All three pathways agree on both magnitude and sign;
the prior mpfr witness (50-digit precision) and the symbolic
$q$-rational expression evaluated at $q_0$ confirm that the
negativity is not a single-precision artifact and not a numerical
coincidence at $q_0$.

**Step 3: Continuity in $q$ rules out singularity.**

Solving at $q \in \{1.0001, 1.001, 1.01, 1.05, 1.1097\}$ shows
$y_{(1,1,1,1)}(q)$ varies smoothly from $-2.08 \times 10^{-6}$ at
$q = 1.0001$ to $-8.45 \times 10^{-4}$ at $q = 1.1097$ — strictly
negative and monotone decreasing across the whole interval.  In
particular the negative sign is not localised at $q_0$ and is not
a near-zero rounding artifact.

**Step 4: Conclusion.**

The witness $y_{(1,1,1,1)}(q_0) = -8.4253 \times 10^{-4} < 0$
is established by three independent pathways and by smooth $q$-
continuation.  Hence the candidate measure $p_q(\lambda) = y_\lambda
\cdot d_\lambda$ for [`conj:tau-codim-shannon`](#conj:tau-codim-shannon)
takes a strictly negative value at $\lambda = (1,1,1,1) \vdash 4$,
$q = q_0$, and is therefore not a probability measure.  $\square$

**Lean handle.**  The Lean theorem
`QOU.BraidKnot.shannon_jones_markov_no_go` packages this as the
existence statement *"there exists $y < 0$"* with the witness
constant $y_{(1,1,1,1)}(q_0)$ proved negative by `norm_num`.  The
substantive content lives in the computational witness; the Lean
side certifies that the witness implies the no-go.
