**Proof.** Both parts hold over the abstract linearly ordered abelian value group
$\Gamma$.
The restricted-product condition is encoded by an explicit finite set $S$ of
*active* places (those with $\ordw_v \neq 0$); off $S$ the local order is the
tame archimedean reference $0$, so the sum is finite and well-defined.
Additivity follows from pointwise addition of local orders
summed over $S$ ($\sum_S (a+b) = \sum_S a + \sum_S b$). The squeeze
follows because a finite sum of
weak inequalities with one strict term is strict in any linearly ordered cancellative abelian monoid. $\square$

**Tate's thesis.** This is the surreal-register form of Tate's adelic
factorisation \cite{tate1967}: where Tate writes the global zeta integral as a
restricted product of local zeta integrals $\zeta_v(f_v, s)$ — one per place —
the substrate writes the global Reeb infinitesimal $\varepsilon$ as the
restricted product of local $\varepsilon_v$, and the global valuation as the
sum of local valuations. Part 1 is the valuation-theoretic shadow of the Euler
product; part 2 promotes the single global $\varepsilon$-squeeze of
[surreal squeeze](#lem:surreal-squeeze) to a *separate squeeze at each prime*,
which is the local–global content used by
[adelic–Tate surreal squeeze](#rem:adelic-tate-squeeze).

**Extra structure — consistency across places.** The hypothesis that *all*
local orders $\ordw_v$ land in one common value group $\Gamma$ is not free: it
is the requirement that the per-place surreal orders be **commensurable** — a
single coherent birthday filtration spanning every prime and the archimedean
place $v = \infty$ simultaneously. Without it the sum $\sum_v \ordw_v(f_v)$ is
not even defined. This shared linearly ordered abelian group $\Gamma$ is the genuine additional structure the
adelic lift exposes: it is what makes the two dual archimedean reductions of
[adelic–Tate surreal squeeze](#rem:adelic-tate-squeeze) — the fibre functor
$\tau_{\mathrm{arch}} = \pi_\infty$ across places, and the standard part
$\mathrm{St} : \mathbf{No} \to \mathbb{R}$ along the filtration — land in the
same ordered target, and it is the natural place to look for further exploitable
rigidity (e.g. the automorphic generalisation flagged in the outlook of
[adelic–Tate surreal squeeze](#rem:adelic-tate-squeeze)).

**Downstream.** This proposition supplies the local–global skeleton consumed by
[adelic–Tate surreal squeeze](#rem:adelic-tate-squeeze) and, through it, the
leading-coefficient reduction of [BSD surreal bound](#rem:bsd-surreal-bound).
The squeeze content is purely structural: it takes the per-place inequalities
as hypotheses and is therefore independent of the q-NS conjecture cone behind
[surreal squeeze](#lem:surreal-squeeze).
