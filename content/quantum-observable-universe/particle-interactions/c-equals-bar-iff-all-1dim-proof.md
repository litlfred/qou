*Forward direction.* On a one-dimensional representation
$V_\lambda$ with eigenvalue $\alpha$ (either $q$ or $-q^{-1}$),
$\sigma_i^{-1}$ has eigenvalue $\alpha^{-1}$
(from $\sigma^2 = h\sigma + 1$, so $\sigma^{-1} = \sigma - h$,
giving eigenvalue $\alpha - h$; for $\alpha = q$: $q - h = q^{-1}$;
for $\alpha = -q^{-1}$: $-q^{-1} - h = -q$).

Under bar, $q \mapsto q^{-1}$ sends eigenvalue $q \mapsto q^{-1}$
and $-q^{-1} \mapsto -q$.  These match $C$:

$$
  C\colon q \mapsto q^{-1},\quad -q^{-1} \mapsto -q
  \qquad = \qquad
  \mathrm{bar}\colon q \mapsto q^{-1},\quad -q^{-1} \mapsto -q.
$$

So $\chi^\lambda(C(\beta)) = \chi^\lambda(\mathrm{bar}(\beta))$
for all 1-dim $\lambda$.

*Reverse direction.* At $H_3(q)$, the standard representation
$(2,1)$ has dimension 2.  The Hoefsmit seminormal matrix for
$\sigma_1$ has a $2 \times 2$ block with off-diagonal entry
$b = \sqrt{a_\rho \cdot a_{-\rho} + 1}$ (irrational in $q$).
Under $C$: $\sigma_1 \mapsto \sigma_1 - h \cdot I$, which shifts
the diagonal by $-h$ but does NOT conjugate $b$.  Under bar:
$q \mapsto q^{-1}$ changes both diagonal AND off-diagonal entries
(since $b$ depends on $q$ through $a_\rho = h/(1-q^{-2\rho})$).
These give different matrices, hence different traces.

Explicitly at $q_0$:
$\chi^{(2,1)}(\pi^+, q_0) = -(h^2+1) \approx -1.044$,
$\chi^{(2,1)}(\pi^-, q_0) \approx +1.892$ (charge conjugate),
$\chi^{(2,1)}(\pi^+, q_0^{-1}) = -(h^2+1) \approx -1.044$ (bar).
Since $+1.892 \ne -1.044$, $C \ne \mathrm{bar}$ on $(2,1)$.
$\qquad\blacksquare$
