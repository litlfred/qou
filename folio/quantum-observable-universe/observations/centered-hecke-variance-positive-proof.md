*Proof.* Apply the Hecke quadratic relation $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ and the Markov property:

$$
  \mathrm{tr}_M(\sigma_i^2)
  = (q - q^{-1}) \mathrm{tr}_M(\sigma_i) + 1
  = (q - q^{-1}) z + 1.
$$

Hence

$$
  \mathrm{tr}_M(\tilde\sigma_i^2)
  =
  \mathrm{tr}_M(\sigma_i^2 - 2 z \sigma_i + z^2)
  =
  (q - q^{-1}) z + 1 - 2 z^2 + z^2
  =
  (q - q^{-1}) z + 1 - z^2.
$$

This is the variance. Both steps are convention-independent: they use only the quadratic relation and $\mathrm{tr}_M(\sigma_i) = z$.

**Closed form.** Substituting the production convention D, $z = q^3/(q^2+1)$, and $q - q^{-1} = (q^2-1)/q$:

$$
  (q - q^{-1})\,z \;=\; \frac{q^2(q^2-1)}{q^2+1},
  \qquad
  z^2 \;=\; \frac{q^6}{(q^2+1)^2}.
$$

Over the common denominator $(q^2+1)^2$,

$$
  \mathrm{Var}(\sigma_i)
  \;=\; \frac{q^2(q^2-1)(q^2+1) + (q^2+1)^2 - q^6}{(q^2+1)^2}
  \;=\; \frac{q^6 - q^2 + q^4 + 2q^2 + 1 - q^6}{(q^2+1)^2}
  \;=\; \frac{q^4 + q^2 + 1}{(q^2+1)^2}.
$$

**Positivity.** Numerator and denominator are both strictly positive for every real $q$, so $\mathrm{Var}(\sigma_i) > 0$ unconditionally — no regime hypothesis is needed. For the sharp bound, set $t = q^2 > 0$ and write $f(t) = (t^2+t+1)/(t+1)^2$. Then

$$
  f'(t) \;=\; \frac{t-1}{(t+1)^3},
$$

which is negative on $(0,1)$, zero at $t = 1$, and positive on $(1,\infty)$. So $f$ attains its global minimum at $t = 1$, i.e. $q = 1$, where $f(1) = 3/4$, and $f(t) \to 1$ as $t \to 0^+$ and as $t \to \infty$. Therefore

$$
  \tfrac{3}{4} \;\leq\; \mathrm{Var}(\sigma_i) \;<\; 1
  \qquad \text{for all } q > 0,
$$

with equality on the left only at $q = 1$. At $q_0$ the value is $0.75270211325196540159$. $\square$

**Identification.** The closed form is not a new quantity. Since $[2]_q = (q^2+1)/q$ and $[4]_q = [2]_q(q^2+q^{-2})$,

$$
  \frac{[4]_q}{[2]_q^3} + \frac{1}{[2]_q^2}
  \;=\; \frac{q^4+1}{(q^2+1)^2} + \frac{q^2}{(q^2+1)^2}
  \;=\; \frac{q^4+q^2+1}{(q^2+1)^2},
$$

so $\mathrm{Var}(\sigma_i) = y_{(3)} + y_{(2,1)} = \mu_+$ identically in $q$ — the centred second moment of a single Hecke generator is exactly the isospin-triplet Wenzl weight.

**Comparison with Convention C.** Unlike the Convention-C identity $(q-q^{-1})z_C = q^{1/2} - q^{-1/2}$ (which lower-bounded the variance by $3/4$ for $q \neq 1$), the rational Convention-D derivation above is unconditional for all $q > 0$ and achieves the sharp lower bound $\mathrm{Var}(\sigma_i) = 1$ at $q = 1$.
