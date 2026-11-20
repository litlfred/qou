**Proof.** Both parts are proved over the abstract value group
$\Gamma$.
The restricted-product condition is encoded by an explicit finite set $S$ of
*active* places (those with $\ordw_v \neq 0$); off $S$ the local order is the
tame archimedean reference $0$, so the sum is finite and well-defined.
Additivity is pointwise addition of local orders
summed over $S$ ($\sum_S (a+b) = \sum_S a + \sum_S b$). The squeeze
is the strict comparison of finite sums: a finite sum of
weak inequalities with one strict term is strict. $\square$

**Tate's thesis.** This is the surreal-register form of Tate's adelic
factorisation \cite{tate1967}: where Tate writes the global zeta integral as a
restricted product of local zeta integrals $\zeta_v(f_v, s)$ — one per place —
the substrate writes the global Reeb infinitesimal $\varepsilon$ as the
restricted product of local $\varepsilon_v$, and the global valuation as the
sum of local valuations. Part 1 is the valuation-theoretic shadow of the Euler
product; part 2 gives a *separate squeeze at each prime*.

**Extra structure — consistency across places.** The hypothesis that *all*
local orders $\ordw_v$ land in one common value group $\Gamma$ is not free: it
is the requirement that the per-place surreal orders be **commensurable** — a
single coherent birthday filtration spanning every prime and the archimedean
place $v = \infty$ simultaneously. Without it the sum $\sum_v \ordw_v(f_v)$ does
not even typecheck. This shared $\Gamma$ is the genuine additional structure the
adelic lift exposes
(a linearly ordered abelian group).

