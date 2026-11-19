The hexagon axioms and naturality of the braiding in a :refterm[braided monoidal category]{#braided-monoidal-category} guarantee that
$c_{V,V}$ satisfies the Yang--Baxter equation

$$
  (c \otimes \mathrm{id})
  \circ (\mathrm{id} \otimes c)
  \circ (c \otimes \mathrm{id})
  = 
  (\mathrm{id} \otimes c)
  \circ (c \otimes \mathrm{id})
  \circ (\mathrm{id} \otimes c)
$$

on $V^{\otimes 3}$. This identity is the braid relation for adjacent
generators $\rho_n(\sigma_i)\rho_n(\sigma_{i+1})\rho_n(\sigma_i) = \rho_n(\sigma_{i+1})\rho_n(\sigma_i)\rho_n(\sigma_{i+1})$, and the two equations are algebraically identical at every adjacent triple $(i, i+1, i+2)$. The far-commutativity relation
$\rho_n(\sigma_i)\rho_n(\sigma_j) = \rho_n(\sigma_j)\rho_n(\sigma_i)$ ($\lvert i-j\rvert \geq 2$) follows
from the bifunctoriality (interchange law) of the monoidal tensor product $\otimes$ and the coherence of the associator isomorphisms, since $\rho_n(\sigma_i)$ and $\rho_n(\sigma_j)$ act on disjoint tensor-factor pairs. Because $c_{V,V}$ is an isomorphism with inverse $c_{V,V}^{-1}$, each $\rho_n(\sigma_i)$ is an automorphism of $V^{\otimes n}$, and together these relations verify the Artin presentation of $B_n$.
