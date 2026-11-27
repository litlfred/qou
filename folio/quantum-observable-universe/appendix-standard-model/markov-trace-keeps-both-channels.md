**Proposition.** In $H_2(q) = \operatorname{span}\{1, \sigma\}$ with
$\sigma^2 = (q - q^{-1})\sigma + 1$, let
$p_+ = (\sigma + q^{-1})/(q + q^{-1})$ and $p_- = (q - \sigma)/(q + q^{-1})$ be the idempotents
of the $q$ and $-q^{-1}$ channels of
[`prop:hecke-sign-channel-is-fermi`](hecke-sign-channel-is-fermi.md). Let $\mathrm{tr}_z$ be
the Markov trace with $\mathrm{tr}_z 1 = 1$ and $\mathrm{tr}_z \sigma = z$. Assume $q \neq 0$
and $q^2 + 1 \neq 0$. Then

1. $\mathrm{tr}_z p_- + \mathrm{tr}_z p_+ = 1$ for every $z$;
2. $\mathrm{tr}_z p_- = 0$ if and only if $z = q$, and $\mathrm{tr}_z p_+ = 0$ if and only if
   $z = -q^{-1}$;
3. at $z_D = q^3/(q^2 + 1)$,
   $$\mathrm{tr}_{z_D} p_- = \frac{q^2}{(q^2 + 1)^2}, \qquad
     \mathrm{tr}_{z_D} p_+ = \frac{q^4 + q^2 + 1}{(q^2 + 1)^2},$$
   and both are nonzero when $q^4 + q^2 + 1 \neq 0$.

**Proof.** $\mathrm{tr}_z p_- = (q - z)/(q + q^{-1})$ and
$\mathrm{tr}_z p_+ = (q^{-1} + z)/(q + q^{-1})$; items 1 and 2 follow, and item 3 is the
substitution $z = z_D$. $\square$

**Scope.** Convention D gives both channels nonzero weight, so it does not choose the
channel a matter strand pair occupies. This is a negative about the Markov trace at $z_D$
only. The one trace that removes a channel, the augmentation $z = q$, removes the
$-q^{-1}$ (Fermi) channel.
