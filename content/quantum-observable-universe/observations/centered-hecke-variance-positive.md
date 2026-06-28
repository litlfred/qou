**Proposition (positivity of centred Hecke variance).**
*Let $q > 0$ with $q^{1/2} + q^{-1/2} > 2$ (Wenzl positivity regime).
Let $z = 1/(q^{1/2}+q^{-1/2})$ be the Markov parameter and
$\tilde\sigma_i := \sigma_i - z \cdot 1$ the centred Hecke generator.
Then the variance*
$$
  \mathrm{Var}(\sigma_i) \;:=\; \mathrm{tr}_M(\tilde\sigma_i^2)
  \;=\;
  (q - q^{-1}) z + 1 - z^2
$$
*is strictly positive: $\mathrm{Var}(\sigma_i) > 0$. Numerically at
the QOU substrate $q_0 \approx 1.110$, $\mathrm{Var}(\sigma_i) \approx 0.855$.*

**Numerical check at $q_0$.** With $q_0 \approx 1.110$:

See [Table: Centred Hecke variance at $q_0$](#tbl:centered-hecke-variance-positive-table-data).

The variance is well-separated from zero, confirming the q-CLT limit
is non-degenerate at the substrate value.

**Status: provable arithmetic.** The proof in
[`prf:centered-hecke-variance-positive`](#prf:centered-hecke-variance-positive)
is direct algebra plus the inequality
$(q^{1/2}+q^{-1/2})^2 > 4$ ⟹ Wenzl regime ⟹ variance positive.
