**Proof.**

*A single-witness existence claim plus an explicit family showing
the gap is unbounded.*

**Step 1: Reduce to the centre.**

For a semisimple Frobenius algebra $A = \bigoplus_\lambda A_\lambda$
with central idempotents $\{p_\lambda\}$, the canonical creation
morphism associated with the Wedderburn decomposition is

$$
  C \;=\; \sum_\lambda \frac{p_\lambda}{d_q(\lambda) \,
  \tau(p_\lambda)}.
$$

Since the $p_\lambda$ are mutually orthogonal idempotents and the
trace splits across blocks,

$$
  \tau(C) \;=\; \sum_\lambda \frac{\tau(p_\lambda)}{d_q(\lambda) \,
  \tau(p_\lambda)} \;=\; \sum_\lambda \frac{1}{d_q(\lambda)},
$$

and

$$
  \|C\|^2 \;=\; \tau(C^\dagger C) \;=\; \sum_\lambda
  \frac{\tau(p_\lambda)}{d_q(\lambda)^2 \, \tau(p_\lambda)^2}
  \;=\; \sum_\lambda \frac{1}{d_q(\lambda)^2 \, \tau(p_\lambda)}.
$$

The L${}^2$-Cauchy--Schwarz inequality applied to the inner
product $\langle f, g \rangle = \tau(f^\dagger g)$ gives

$$
  |\tau(f^\dagger C)|^2 \;\leq\; \tau(f^\dagger f) \cdot \|C\|^2,
$$

so under the unit-creation normalisation $\tau(f^\dagger C) = 1$
the strongest bound CS can deliver is $\tau(f^\dagger f) \geq
1/\|C\|^2$.

**Step 2: Balanced-family witness.**

Specialise to the balanced family $d_q(\lambda) = \tau(p_\lambda)
= 1$ for every $\lambda$ in a finite indexing set $\Lambda$ with
$|\Lambda| = n \geq 2$.  Then

$$
  \tau(C_{\dim_q}) \;=\; \sum_\lambda 1 \;=\; n,
  \qquad
  \|C\|^2 \;=\; \sum_\lambda 1 \;=\; n,
  \qquad
  \frac{1}{\|C\|^2} \;=\; \frac{1}{n}.
$$

The CS-to-Landauer ratio $1/n^2$ tends to $0$ as $n \to \infty$,
so the gap is unbounded:

| $n$ | CS bound $1/n$ | Landauer bound $n$ | ratio $1/n^2$ |
|---|---|---|---|
| 2 | $0.500$ | $2$ | $0.25$ |
| 3 | $0.333$ | $3$ | $0.111$ |
| 5 | $0.200$ | $5$ | $0.04$ |
| 10 | $0.100$ | $10$ | $0.01$ |
| 20 | $0.050$ | $20$ | $0.0025$ |

**Step 3: Independent computational validation.**

The script
[`tau_codim_conjectures_validate.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/tau_codim_conjectures_validate.py)
recomputes both bounds from scratch on the balanced family at
$n \in \{2, 3, 5, 10, 20\}$ and records them in
[`tau-codim-conjectures-validation.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/tau-codim-conjectures-validation.witness.json).
In every case `cs_strictly_weaker = true`.

**Step 4: Honest scope.**

The same validation script also samples $50$ random Frobenius
algebras with $n \in [2, 20]$ blocks and $d_q, \tau_p \in
[0.5, 3]$.  Result:

- $\sim 30\%$ of trials have $1/\|C\|^2 < \tau(C_{\dim_q})$
  (CS strictly weaker), as in the balanced family;
- $\sim 70\%$ of trials have $1/\|C\|^2 > \tau(C_{\dim_q})$
  (CS strictly stronger);
- ratio range observed: $4 \times 10^{-3}$ to $4.9$.

So Cauchy--Schwarz and the Landauer bound are **incomparable in
general**.  The proposition is correctly scoped to "there exists a
witness" — the balanced family delivers it.

**Step 5: Conclusion.**

Any proof of [`conj:tau-codim-landauer`](#conj:tau-codim-landauer)
that holds on the balanced family must use categorical or
trace-positivity input beyond Cauchy--Schwarz, since CS bounds
$\tau(f^\dagger f)$ from below by $1/n$ on that family while the
conjecture demands $\tau(f^\dagger f) \geq n$.  The gap $n - 1/n$
is unbounded in $n$, so no improvement of the CS constant can
close it.  $\square$

**Lean handle.**  The Lean theorem
`QOU.BraidKnot.landauer_cauchy_schwarz_insufficient` proves
$1/n < n$ for every $n \geq 2$ from scratch (one `linarith`
after rewriting $1/n \leq 1 < n$).  This is the entire content
of Step 2 of the proof; Steps 1, 3, and 4 are establishing the
correct *interpretation* of the inequality (as the gap between
the two bounds on the balanced family) and the computational
validation, which live in the proof markdown and the witness
JSON respectively.
