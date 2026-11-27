One computes the [quantum characteristic classes](#def:quantum-characteristic-classes) for $G = \mathrm{SU}(2)$ from the [brane tower for SU(2)](#ex:recursive-brane-tower-su2), separating the holomorphic/smooth unit band $\mathcal{O}^{\times}_{\mathbb{CP}^1}$ from the discrete and Kummer bands $\mathbb{Z}$ and $\mu_n$.

**1. Unit-sheaf band $\mathcal{B} = \mathcal{O}^{\times}_{\mathbb{CP}^1}$.** When the level transitions $A_n \hookrightarrow A_{n+1}$ of the brane tower on $\mathcal{S} = \mathbb{CP}^1 \cong \mathrm{SU}(2)/\mathrm{U}(1)$ are banded by $\mathcal{O}^{\times}_{\mathbb{CP}^1}$, the obstruction classes lie in $H^2(\mathbb{CP}^1, \mathcal{O}^{\times})$. Because $\mathbb{CP}^1$ has complex dimension $1$ and real dimension $2$, both $H^2(\mathbb{CP}^1, \mathcal{O}) = 0$ and $H^3(\mathbb{CP}^1, \mathbb{Z}) = 0$ in the exponential sequence, giving

$$
  H^2(\mathbb{CP}^1, \mathcal{O}^{\times}) = 0.
$$

Consequently every $\mathcal{O}^{\times}$-banded gerbe obstruction $\kappa_n \in H^2(\mathbb{CP}^1, \mathcal{O}^{\times})$ vanishes identically for all $n \geq 0$. The non-trivial first Chern class $c_1(\text{Hopf}) = 1$ of the principal $\mathrm{U}(1)$-bundle $\pi \colon \mathrm{SU}(2) \to \mathbb{CP}^1$ sits one cohomological degree lower, in $\mathrm{Pic}(\mathbb{CP}^1) = H^1(\mathbb{CP}^1, \mathcal{O}^{\times}) \cong H^2(\mathbb{CP}^1, \mathbb{Z}) \cong \mathbb{Z}$, and does not obstruct $\mathcal{O}^{\times}$-gerbe lifts.

**2. Discrete band $\mathbb{Z}$ (Reeb bundle Euler class).** Lifting the Reeb unit tangent $\mathrm{U}(1)$-bundle $\xi$ of $\mathbb{CP}^1 \cong S^2$ (total space $\mathrm{SO}(3) \cong \mathbb{RP}^3$) along the central extension $0 \to \underline{\mathbb{Z}} \to \underline{\mathbb{R}} \to \underline{\mathrm{U}(1)} \to 0$ yields the non-torsion Euler class

$$
  \kappa_0 = c_1(\xi) = e(\xi) = \chi(\mathbb{CP}^1) = 2
   \in  H^2(\mathbb{CP}^1, \mathbb{Z})  \cong  \mathbb{Z}.
$$

Meanwhile, the jet-correction group $H^2(\mathbb{CP}^1, \mathcal{O}) = 0$ vanishes on the curve, so no additive higher-jet classes arise in $H^2(\mathbb{CP}^1, \mathcal{O})$.

**3. Kummer bands $\mu_n$ ($n$-th root persistence).** Reducing $\kappa_0 = 2$ modulo $n$ along $1 \to \mu_n \to \mathrm{U}(1) \xrightarrow{(\cdot)^n} \mathrm{U}(1) \to 1$ gives the Kummer obstruction

$$
  \kappa_0 \bmod n \;=\; 2 \bmod n \;\in\; H^2(\mathbb{CP}^1, \mu_n) \;\cong\; \mathbb{Z}/n.
$$

This class vanishes for $n \mid 2$ ($n \in \{1, 2\}$, where the Hopf bundle $\mathrm{SU}(2) \to \mathbb{CP}^1$ with $c_1 = \pm 1$ supplies the spin square root of $\xi$) and is non-zero for every $n \geq 3$.

**Conclusion.** For $\mathrm{SU}(2)$ over $\mathcal{S} = \mathbb{CP}^1$, the $\mathcal{O}^{\times}$-banded gerbe tower has $\kappa_n = 0$ at every level, whereas the Reeb $\mathrm{U}(1)$-bundle carries Euler class $\chi(\mathbb{CP}^1) = 2 \in H^2(\mathbb{CP}^1, \mathbb{Z})$ whose Kummer $n$-th-root obstruction vanishes at $n \in \{1, 2\}$ and persists for all $n \geq 3$.
