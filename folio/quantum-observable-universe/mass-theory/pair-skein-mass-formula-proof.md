**Proof.**
Write $[2]_q = q + q^{-1}$. The two ingredients of $\mathcal{S}_{ab}$ are computed from the Markov trace at $z = q^3/(q^2+1)$.

*The normaliser.* The Temperley–Lieb generator is $e_i = q - \sigma_i$, so its trace is $q - z$. From $z(q^2+1) = q^3$,

$$
  (q - z)(q + q^{-1}) = \frac{q(q^2+1) - q^3}{q^2+1}\cdot\frac{q^2+1}{q} = 1,
$$

so $q - z = 1/[2]_q$. In particular $[2]_q \neq 0$.

*The skein weights.* A link invariant $X = c^{\,w(\beta)}\,\kappa^{\,n-1}\,\mathrm{tr}(\beta)$, with $w$ the writhe, is unchanged by stabilising with $\sigma_n$ and with $\sigma_n^{-1}$ exactly when $c\,\kappa\,z = 1$ and $c^{-1}\kappa\,\mathrm{tr}(\sigma^{-1}) = 1$. Since $\sigma^{-1} = \sigma - (q - q^{-1})$,

$$
  \mathrm{tr}(\sigma^{-1}) = z - (q - q^{-1}) = q^{-4} z .
$$

Dividing the two conditions gives $c^2 = q^{-4}$, so $c = \pm q^{-2}$. The trace relation $\mathrm{tr}(x\sigma) - \mathrm{tr}(x\sigma^{-1}) = (q - q^{-1})\,\mathrm{tr}(x)$ then reads $c^{-1}X(L_+) - c\,X(L_-) = (q - q^{-1})\,X(L_0)$, with weights $\pm q^{\pm 2}$.

*The mass assignment.* Each crossing pair of the Borromean braid joins strands of species $a$ and $b$. Weight $\mu_a$ by the positive-crossing coefficient $q^{2}$ and $\mu_b$ by the negative-crossing coefficient $q^{-2}$, and normalise by the trace of $e_i$. This gives $\mathcal{S}_{ab} = (q - z)(q^2\mu_a + q^{-2}\mu_b)$. This step is a reading, not a derivation from the braid. It contains two choices, and both are fixed by tests the corpus already applies to this normaliser.

1. *Bar-covariance.* The form above satisfies $\mathcal{S}_{ab}(q^{-1}) = \mathcal{S}_{ba}(q)$ identically. Normalising by $z$ instead multiplies every $\mathcal{S}_{ab}$ by $q^2$ (because $z = q^2(q - z)$), and that form is bar-covariant on $(\mu_a, \mu_b) = (1, 0)$ only if $q^4 = 1$.
2. *Classical limit.* At $q = 1$ the form above gives $\mathcal{S}_{aa} = \mu_a$. The branch $c = -q^{-2}$ negates every $\mathcal{S}_{ab}$ and gives $-\mu_a$.

The total nucleon mass is the sum over the three crossing pairs. $\square$
