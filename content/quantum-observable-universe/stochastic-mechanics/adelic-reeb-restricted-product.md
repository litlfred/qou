**Proposition (restricted-product structure of the Reeb $\omega$-order).**
*Let $\mathbb{A} = \mathbb{R} \times \prod_p' \mathbb{Q}_p$ be the rational
adele ring and, for each place $v$ of $\mathbb{Q}$, let
$\varepsilon_v \in \mathrm{Der}(A_v)$ be the local Reeb infinitesimal
([Reeb infinitesimal](#def:reeb-epsilon)) on the substrate's local completion
$A_v$. Suppose every local $\omega$-order $\ordw_v$ takes values in one common
linearly ordered value group $\Gamma$ — the $\omega$-grade of $\mathbf{No}$ —
and that, for any adelic observable $f = (f_v)_v$, the set of $v$ with
$\ordw_v(f_v) \neq 0$ is finite (restricted-product condition). Then the global
$\omega$-order is the finite sum of the local orders,*

$$
  \ordw_{\mathbb{A}}(f) \;=\; \sum_{v} \ordw_v(f_v)
  \qquad (\text{finite sum}),
$$

*and this assignment is*

1. **additive over places** — $\ordw_{\mathbb{A}}(fg) = \ordw_{\mathbb{A}}(f) +
   \ordw_{\mathbb{A}}(g)$ (Tate factorisation), and
2. **squeeze-coherent** — if $\ordw_v(g_v) \le \ordw_v(f_v)$ at every place and
   the inequality is *strict* at some place $v_0$, then
   $\ordw_{\mathbb{A}}(g) < \ordw_{\mathbb{A}}(f)$.

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
place $v = \infty$ simultaneously. Without it the sum $\sum_v \ordw_v(f_v)$ does
not even typecheck. This shared $\Gamma$ is the genuine additional structure the
adelic lift exposes (formalised in Lean as a linearly ordered abelian group —
`AddCommGroup` $+$ `LinearOrder` $+$ `IsOrderedCancelAddMonoid`): it is what makes the two dual archimedean reductions of
[adelic–Tate surreal squeeze](#rem:adelic-tate-squeeze) — the fibre functor
$\tau_{\mathrm{arch}} = \pi_\infty$ across places, and the standard part
$\mathrm{St} : \mathbf{No} \to \mathbb{R}$ along the filtration — land in the
same ordered target, and it is the natural place to look for further exploitable
rigidity (e.g. the automorphic generalisation flagged in the outlook of
[adelic–Tate surreal squeeze](#rem:adelic-tate-squeeze)).

**Downstream.** This proposition supplies the local–global skeleton consumed by
[adelic–Tate surreal squeeze](#rem:adelic-tate-squeeze) and, through it, the
leading-coefficient reduction of [BSD surreal bound](#rem:bsd-surreal-bound).
The squeeze content is purely structural — it takes the per-place inequalities
as hypotheses and is therefore independent of the q-NS conjecture cone behind
[surreal squeeze](#lem:surreal-squeeze).
