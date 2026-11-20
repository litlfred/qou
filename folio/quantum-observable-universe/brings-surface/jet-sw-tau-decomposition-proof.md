By [Abelianisation of the MI integral on exceptional divisors](#prop:mi-sw-abelianisation), for each vertical
degree $n\geq 0$ the Killing-norm projection of the surface-ordered
multiplicative integral onto the $n$-jet component equals the prolonged
Seiberg--Witten period, $\lVert\mathrm{MI}\!\int_{\mathcal{S}_c}\rVert_{J^n} =
\lvert a_D^{(n)}\rvert$. The jet prolongation tower $\{J^n E\}_{n\geq 0}$ is
exhaustive — every vertical component of the connection lives at some finite jet
degree — so the surface-ordered integral is the (convergent) sum of its jet
components.

The Archimedean realisation $\tau$ is additive on the graded pieces of the jet
filtration (it is exact on the associated graded of the prolongation tower), so
it commutes with the degree sum:

$$
\tau\!\left(\mathrm{MI}\!\!\int_{\mathcal{S}_c}\bigl(\nabla_A q,\,L\wedge F^+\bigr)\right)
= \sum_{n\geq 0}\tau\bigl(\text{$n$-jet component}\bigr)
= \sum_{n\geq 0} a_D^{(n)}.
$$

Rewriting each period as its residue sum
([The Seiberg–Witten period is an algebraic residue sum](#prop:sw-period-residue-sum)) gives the second
equality. The Lean witness
[`QOU.Brings.jet_sw_tau_decomposition`](#prop:jet-sw-tau-decomposition) packages
the exhaustiveness and additivity as the structure hypothesis and extracts the
graded-sum identity. $\qquad\blacksquare$
