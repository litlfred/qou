## The inequality

Both scalars carry the same denominator $q + q^{-1}$, which is positive for $q > 0$,
and the ordering therefore reduces to the numerators: $\mu_- < \mu_+$ is equivalent
to $q - z < z + q^{-1}$, that is to $h < 2z$ with $h = q - q^{-1}$.

Substituting convention D and clearing denominators turns $2z - h$ into a closed form
rather than an estimate:

$$
  2\,\frac{q^{3}}{q^{2}+1} \;-\; \Bigl(q - \frac1q\Bigr)
  \;=\; \frac{2q^{4} - (q^{2}-1)(q^{2}+1)}{q\,(q^{2}+1)}
  \;=\; \frac{q^{4}+1}{q\,(q^{2}+1)} .
$$

The numerator $q^{4}+1$ and the denominator $q(q^{2}+1)$ are both strictly positive
for $q > 0$, so $2z - h > 0$ identically. Dividing by the common positive denominator
restores the inequality on the scalars.

Nothing in the computation is specific to the aether parameter, and nothing is
approximate: the quantity whose sign is at issue has been written as a ratio of
positives, which is the strongest form the claim admits.

## Transport to binding energy

The binding of a channel is $B_T = -\alpha \log \mu_T$ with $\alpha > 0$ the energy
scale. Since $\log$ is strictly increasing on the positive reals and $\mu_- > 0$, the
inequality $\mu_- < \mu_+$ gives $\log \mu_- < \log \mu_+$, and multiplying by
$-\alpha$ reverses it:

$$
  B_+ \;=\; -\alpha\log\mu_+ \;<\; -\alpha\log\mu_- \;=\; B_- .
$$

The transport step is where the argument leaves the algebra and enters the
archimedean sector, since $\log$ is a real-analytic function and the energy scale is
a physical quantity. The inequality it transports, however, was established over an
ordered field with no such input, so the two halves of the proof sit on opposite
sides of the Archimedean boundary and only the second is specialised.
