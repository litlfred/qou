**Definition.**
Let $\mathcal{A}_1$ and $\mathcal{A}_2$ be atoms with residual sub-links $R_1$ and $R_2$. A **covalent bond** of order $k$ is a shared sub-Hopf link

$$
  B_k(R_1, R_2)
  = 
  \underbrace{T_{2,3} \oplus \cdots \oplus T_{2,3}}_{k \text{ shared trefoils}}
$$

where each shared trefoil is simultaneously Hopf-linked to one open site in $R_1$ and one open site in $R_2$. The integer $k$ is the **bond order**:

| Bond order $k$ | Chemical name | Shared trefoils | Linking sites consumed |
|:-:|---|:-:|:-:|
| 1 | Single bond | 1 | 1 per atom |
| 2 | Double bond | 2 | 2 per atom |
| 3 | Triple bond | 3 | 3 per atom |

The crossing energy of the bond is

$$
  E_{\mathrm{bond}}(k)
  = 
  k \cdot \mathfrak{E}_{\mathrm{cross}}(T(2,2))
  + 
  \binom{k}{2}  \Delta E_{\mathrm{inter}},
$$

where $T(2,2)$ is the Hopf link. The first term accounts for $k$ individual Hopf links, and the second for inter-link interactions within the shared sub-link. Higher bond order increases both binding strength and rigidity: a triple bond is stronger and stiffer than a single bond because the three shared trefoils form a closed sub-link that resists Reidemeister moves.
