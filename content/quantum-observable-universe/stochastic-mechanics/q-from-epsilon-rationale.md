**Consistency with prior usage.** The existing Frobenius--Hopf substrate $A_q$ ([Frobenius--Hopf substrate](#def:frobenius-hopf-substrate)) emerges as the evaluation of the $\varepsilon$-expansion

$$
A_q = A_1 + \varepsilon \, \phi_1 + \varepsilon^2 \, \phi_2 + \cdots.
$$

The classical algebra $A_1$ and the deformation cocycles $\phi_n \in HH^2(\mathcal{U}_q, \mathrm{Ad})$ match the Drinfeld--Jimbo expansion pinned down by the [classical limit obstruction](#def:classical-limit-obstruction). The existing $q$-theory remains unchanged. Every identity previously written with $q - 1$ is now written with $\varepsilon$. The classical point $\varepsilon = 0$ coincides with $q = 1$.

**Motivation for taking $\varepsilon$ as primitive.** We elevate $\varepsilon$ for two reasons.

1. **Categorical origin:** The substrate parameter $q$ is a scalar attached to the $R$-matrix. The Reeb infinitesimal $\varepsilon$ is the tangent vector of the Reeb flow. This structure is intrinsic to $A$ before any braiding is chosen. Declaring $\varepsilon$ primitive places the deformation direction inside the category.
2. **Exact error bounds:** The infinitesimal $\varepsilon$ lives in an ordered field. The scaling laws $\Delta_q \asymp \varepsilon^3$, $\Omega_q \asymp \varepsilon^{-1}$, and $\mathrm{enstrophy} \asymp \varepsilon^{-4/3}$ become literal arithmetic inequalities rather than asymptotic $O(\cdot)$ statements (see [surreal rate calculus](#prop:surreal-rate-calculus)).

**Notational convention for the remainder of the paper.** We identify $q - 1$ with $\varepsilon$ and $q = 1$ with $\varepsilon = 0$. The two conventions are logically identical. The $\varepsilon$-convention renders the millennium-problem squeeze lemmas ([surreal squeeze](#lem:surreal-squeeze)) literal rather than asymptotic.
