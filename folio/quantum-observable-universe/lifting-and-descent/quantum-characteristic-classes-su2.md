One computes the [quantum characteristic classes](#def:quantum-characteristic-classes) for $G = \mathrm{SU}(2)$ from the [brane tower for SU(2)](#ex:recursive-brane-tower-su2).

**Setup.** The brane tower $A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots$ produces central extensions of gerbes on $\mathcal{S} = \mathbb{CP}^1 \cong \mathrm{SU}(2)/\mathrm{U}(1)$, banded by $\mathcal{B} = \mathcal{O}^{\times}_{\mathbb{CP}^1}$. The quantum characteristic classes are the obstruction classes $\kappa_n \in H^2(\mathbb{CP}^1, \mathcal{O}^{\times})$ for each transition $A_n \hookrightarrow A_{n+1}$.

**First obstruction.** The Hopf bundle $\pi \colon \mathrm{SU}(2) \to \mathbb{CP}^1$ is a principal $\mathrm{U}(1)$-bundle. Its first Chern class is:
$$
  \kappa_0 =  c_1(\text{Hopf}) =  1
   \in  H^2(\mathbb{CP}^1, \mathbb{Z})  \cong  \mathbb{Z}.
$$
Under the trace map $H^2(\mathcal{S}, \mathcal{B}) \to R$, the obstruction maps to the Euler characteristic: $\kappa_0 \mapsto \mathrm{tr}(\mathrm{id}_A) = \chi(\mathbb{CP}^1) = 2$.

**Non-torsion property.** The group $H^2(\mathbb{CP}^1, \mathbb{Z}) \cong \mathbb{Z}$ is torsion-free. One has $\kappa_0 = 1 \neq 0$. The class $\kappa_0$ is non-torsion.

**Higher obstructions.** At level $n$, the jet prolongation $A_n \hookrightarrow A_{n+1} = J^1(A_n)$ produces an obstruction:
$$
  \kappa_n =  \kappa_0 + \delta_n
   \in  H^2(\mathbb{CP}^1, \mathbb{Z}),
$$
where $\delta_n \in H^2(\mathbb{CP}^1, \mathbb{Z})$ is the correction from the jet structure at level $n$. One has $\kappa_0 = 1$, which generates $H^2(\mathbb{CP}^1, \mathbb{Z}) \cong \mathbb{Z}$. Because $\delta_n \in \mathbb{Z}$ and each prolongation adds non-negative curvature ($\delta_n \geq 0$), one finds $\kappa_n = 1 + \delta_n \geq 1 > 0$ for all $n$.

**Conclusion.** The quantum characteristic classes for $\mathrm{SU}(2)$ never vanish: $\kappa_n \neq 0$ for all $n \geq 0$. The Hopf bundle is non-trivial. The gerbe tower is obstructed at every level.
