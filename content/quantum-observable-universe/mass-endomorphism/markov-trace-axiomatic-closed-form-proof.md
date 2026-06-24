**Step 1: Hecke-power recurrence.** Apply the Hecke quadratic
relation iteratively. Set $\sigma_i^k = a_k\sigma_i + b_k$ with
$a_k, b_k \in \mathbb{Z}[h]$. Multiplying by $\sigma_i$:

$$
  \sigma_i^{k+1} = a_k\sigma_i^2 + b_k\sigma_i = a_k(h\sigma_i + 1) + b_k\sigma_i = (h a_k + b_k)\sigma_i + a_k,
$$

so $a_{k+1} = h a_k + b_k$ and $b_{k+1} = a_k$, with $a_0 = 0$,
$b_0 = 1$. Direct enumeration:

See [Table 1](#tbl:markov-trace-axiomatic-closed-form-table1-data).

**Step 2: Expansion of the proton word.** Using the recurrence,

$$
  \sigma_1^7 \sigma_2^4 \;=\; (a_7 \sigma_1 + b_7)(a_4 \sigma_2 + b_4)
   \;=\; a_7 a_4 \,\sigma_1\sigma_2 \;+\; a_7 b_4 \,\sigma_1 \;+\; b_7 a_4 \,\sigma_2 \;+\; b_7 b_4.
$$

Note $a_k, b_k \in \mathbb{Z}[h] \subset \mathbb{Z}[q, q^{-1}]$ are
Laurent polynomial scalars and commute with the basis elements of
$H_3(q)$.

**Step 3: Markov-trace values on the $H_3$ basis.** The axioms +
cyclicity uniquely fix the trace on the canonical reduced-word
basis $\{1, \sigma_1, \sigma_2, \sigma_1\sigma_2, \sigma_2\sigma_1, \sigma_1\sigma_2\sigma_1\}$
of $H_3(q)$:

See [Table 2](#tbl:markov-trace-axiomatic-closed-form-table2-data).

The last entry follows from
$\sigma_1\sigma_2\sigma_1 = \sigma_2\sigma_1\sigma_2$ (braid
relation), which by Markov on $\alpha = \sigma_2\sigma_1 \in H_3$
(after cyclic rotation) gives $\operatorname{tr}_M(\sigma_2\sigma_1\sigma_2) = z\cdot\operatorname{tr}_M(\sigma_2\sigma_1)$
contradicting naive expectations; the correct derivation uses the
Hecke-quadratic identity $\sigma_1\sigma_2\sigma_1 - \sigma_2\sigma_1\sigma_2 = 0$
and the cyclic application $\operatorname{tr}_M(\sigma_2\sigma_1\sigma_2) = \operatorname{tr}_M(\sigma_1\sigma_2\sigma_1)$
combined with $\sigma_1^2 = h\sigma_1 + 1$ on the inner factor to give
$\operatorname{tr}_M(\sigma_1\sigma_2\sigma_1) = h\,\operatorname{tr}_M(\sigma_1\sigma_2) + \operatorname{tr}_M(\sigma_2) = h z^2 + z$.

**Step 4: Linear combination.** Applying $\operatorname{tr}_M$ to the
expansion in Step 2 and reading off basis values:

$$
  \operatorname{tr}_M(\sigma_1^7\sigma_2^4)
   \;=\; a_7 a_4 \cdot z^2 \;+\; a_7 b_4 \cdot z \;+\; b_7 a_4 \cdot z \;+\; b_7 b_4 \cdot 1.
$$

**Step 5: Substitution and simplification.** Substituting $h = q -
q^{-1}$ and $z = 1/(q^{1/2}+q^{-1/2})$ and clearing denominators
gives a rational function in $q^{1/2}$ with denominator
$q^{10}(q+1)^3$ (verified by `sp.cancel` in
`markov_trace_atomic_proton_full.py`).

The methodology of Steps 1-5 is fully axiomatic — only the Hecke
quadratic, Markov axioms, cyclicity, and braid relations are
invoked. No representation theory, no Hoefsmit-Wenzl seminormal
construction, no character tables. $\square$
