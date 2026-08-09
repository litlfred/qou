Let $H_n(R, q)$ be the Iwahori--Hecke algebra with Markov trace
$\mathrm{tr}_M$ normalised by $\mathrm{tr}_M(1_k) = 1$ for all $k$
and Markov axiom $\mathrm{tr}_M(x\sigma_{k-1}) = z\,\mathrm{tr}_M(x)$
for $x \in H_{k-1}(q)$, where
$z = q^{3}/(q^{2}+1)$ (**convention D**, [Jones--Markov trace](#thm:jones-markov-trace)).

**Proposition.** For every pair of braid generators
$\sigma_i, \sigma_j$ with $0 \le i < j$, embedded in any
$H_n(R, q)$ with $n > j$,

$$
  \mathrm{tr}_M(\sigma_i\sigma_j) \;=\; z^2.
$$

The identity holds whether $(i,j)$ are adjacent ($j = i+1$)
or non-adjacent ($j \ge i+2$).
## Operator interpretation

The value $z^2$ is the **Jones polynomial of the Hopf link**
(unknotted two-component linking) evaluated at the substrate
parameter:
$J_{\mathrm{Hopf}}(q) = -(q^{1/2} + q^{-1/2})\cdot z^2
= -(q + q^{-1})/(q^{1/2} + q^{-1/2})$. Multiplying by the
Markov normalization recovers the pair contribution to the
categorical mass — the pair blow-up centre at coordinate
$\hat V_i\hat V_j$ carries the same weight $z^2$ regardless
of its position in the braid, matching the empirically-verified
all-pairs set on atoms $A \ge 6$(cf. `adjacent-vs-full-canonical evaluation.witness.json`,
[jet-tower remark](#rem:mass-endomorphism-jet-tower)).

> **The proposition is convention-independent; the Hopf-link normalisation above
> is not, and has NOT been re-derived.** Flagged 2026-08-09, not fixed.
>
> $\mathrm{tr}_M(\sigma_i\sigma_j) = z^2$ follows from the Markov axiom alone and
> holds for any Markov parameter, so switching $z$ to **convention D**
> ($z = q^3/(q^2+1)$, as the cited theorem now states) leaves the proposition
> untouched.
>
> The normalisation $J_{\mathrm{Hopf}}(q) = -(q^{1/2}+q^{-1/2})\cdot z^2$ is a
> different matter. Its prefactor is the loop parameter at **half argument**,
> $[2]_{\sqrt q} = q^{1/2}+q^{-1/2} = 2.0027\ldots$ at $q_0$, whereas the
> Temperley–Lieb loop value of the production trace is
> $\delta = [2]_q = q + q^{-1} = 2.010896866707122\ldots$ — a $0.4\%$ difference,
> and the two are conflated across the corpus (the reciprocal $1/\delta =
> 0.497290545604915556$ against $z_C = 0.499320334183694452$ is the same
> confusion). The identity was derived when $z$ was $z_C$, and under convention D
> — which *is* the Jones/Temperley–Lieb trace — both the prefactor and $z^2$
> change, so the displayed second equality
> $-(q+q^{-1})/(q^{1/2}+q^{-1/2})$ cannot be assumed to survive.
>
> Deliberately left as-is rather than patched: getting the Jones normalisation
> right under D is a derivation, not a substitution, and quietly editing the
> prefactor would produce a formula nobody has checked. Bean `qou-98g5`
> (δ vs $z_C$ conflation) and `qou-emyt`.
