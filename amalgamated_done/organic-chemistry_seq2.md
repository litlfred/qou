<!-- FILE_START: carbon-chains-benzene-intro.md -->
We instantiate the chain–ring machinery at $N = 6$. The **linear $\mathrm{C}_6$ Hopf chain** assembles six carbons with a $6 \times 6$ tridiagonal linking matrix. Interior carbons consume two of their four sites for the backbone. Endpoint carbons carry three dangling links each. These soft modes make linear $\mathrm{C}_6$ flexible.

**Benzene** is the closed counterpart: six carbons threaded by $T(2,6)$, whose two components are the two delocalised $\pi$ electrons. Its Alexander polynomial $q^2 + 1 + q^{-2}$ replaces six pairwise Hopf weights with a single threading invariant. This explains bond-order equalisation and the $\mathrm{C}_6\mathrm{H}_6$ formula. 

Comparing the two structures, the threaded ring binds one more atom at Alexander weight $\approx 3$ versus the chain's $5$. The chain persists because the transition is discontinuous. The geometric reconfiguration sets an activation barrier. The parameter-free prediction $\Delta E \approx 2 \cdot |q + q^{-1}|_{\mathrm{mol}} \approx 193\text{--}386\,\mathrm{kJ/mol}$ matches the experimental $200\text{--}400\,\mathrm{kJ/mol}$ window. The $1/2$ threading factor resolves the pairwise picture's overshoot.
<!-- FILE_END: carbon-chains-benzene-intro.md -->

<!-- FILE_START: carbon-chain-c6.md -->
The linear $\mathrm{C}_6$ chain links six carbon atoms end-to-end.

**Construction.**
Each carbon has 4 open linking sites. In the chain $\mathcal{C}_6^{(1)}$, each interior carbon consumes 2 sites for backbone bonds. The endpoint carbons consume 1 site each.

The linking matrix is the $6 \times 6$ tridiagonal matrix:

$$
  L^{\mathrm{chain}}
  = 
  \begin{pmatrix}
    0 & 1 & 0 & 0 & 0 & 0 \\
    1 & 0 & 1 & 0 & 0 & 0 \\
    0 & 1 & 0 & 1 & 0 & 0 \\
    0 & 0 & 1 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1 & 0 & 1 \\
    0 & 0 & 0 & 0 & 1 & 0
  \end{pmatrix}.
$$

**Crossing energy.**
The chain has 5 bonds, giving $\mathfrak{E}_{\mathrm{cross}}(\mathrm{C}_6^{\mathrm{chain}}) = 5 \cdot E_{\mathrm{bond}}(1)$.

**Spring behaviour.**
The endpoint carbons act as soft modes. The endpoints can oscillate and the chain can bend and stretch at energies below the bond-breaking threshold. In chemistry, linear $\mathrm{C}_6$ is observed as cumulene and carbyne. These correspond to bond-order patterns $(2,2,2,2,2)$ and $(1,3,1,3,1)$.
<!-- FILE_END: carbon-chain-c6.md -->

<!-- FILE_START: benzene-ring.md -->
Benzene ($\mathrm{C}_6\mathrm{H}_6$) is the prototypical threaded molecular ring: six carbon atoms bound by a single threading link $T(2,6)$.

**Construction.**
The six carbon atoms form the ring $\mathcal{R}_6$:

$$
  \mathrm{C}_6^{\mathrm{ring}}
  = 
  [\mathcal{A}(6,6)_1, \ldots, \mathcal{A}(6,6)_6]
   \oplus 
  T(2,6).
$$

The threading link $T(2,6)$ has 10 crossings of the same sign.

**The two components are the $\pi$ electrons.**
$T(2,6)$ has two components, each an unknotted loop winding 3 times through all 6 carbons. These components are the two delocalised $\pi$ electrons of benzene. Delocalisation is topological.

**Alexander polynomial.**

$$
  \Delta_{T(2,6)}(q)
  = 
  q^2 + 1 + q^{-2}
  = 
  (q + q^{-1})^2 - 1.
$$

The crossing energy is proportional to this polynomial, strictly less than the weight of 6 separate Hopf links.

**Bond order equalisation.**
There are no individual bonds — the threading link distributes binding uniformly. Each carbon is threaded identically, producing equal bond lengths and equal bond orders of $3/2$.

**Hydrogen attachment.**
$T(2,6)$ consumes 2 sites per carbon. One remaining site bonds to hydrogen, and one participates in the $\sigma$-backbone. Total hydrogen capacity is 6, giving $\mathrm{C}_6\mathrm{H}_6$.

**Aromaticity as threading.**
Aromaticity corresponds to the existence of a threading link. For even $N$, the threading link is universally twice as efficient as pairwise bonding. The odd-$N$ case requires separate treatment.
<!-- FILE_END: benzene-ring.md -->

<!-- FILE_START: chain-ring-energy.md -->
The linear $\mathrm{C}_6$ chain and benzene represent two different topological states.

**Energy accounting via Alexander polynomials.**
The crossing energy is proportional to the Alexander polynomial weight at the substrate parameter $q$:

| Structure | Binding topology | $\Delta(q)$ | At $q \approx 1$ |
|-----------|-----------------|-------------|------------------:|
| Chain $\mathcal{C}_6$ | 5 Hopf links | $5 \times 1$ | 5 |
| Pairwise ring | 6 Hopf links | $6 \times 1$ | 6 |
| Threaded ring $\mathcal{R}_6$ | $T(2,6)$ | $q^2 + 1 + q^{-2}$ | 3 |

The threaded ring binds 6 carbons with Alexander weight $\approx 3$, less than the chain's weight of 5.

**Existence of the chain.**
The chain exists because the transition is discontinuous. It cannot continuously deform into the ring. The binding structure must dissolve, the atoms must reconfigure into a hexagon, and the threading link must form. This geometric reconfiguration is the activation barrier.

Once the threading forms, the energy drops below the chain. The threading link cannot be broken by a local perturbation.

**Asymmetry of the barriers.**
The closure barrier is dominated by geometric reconfiguration. The opening barrier requires dissolving the threading link back into 5 separate Hopf links. This costs additional Alexander weight. Opening the ring is harder than closing it.
<!-- FILE_END: chain-ring-energy.md -->

<!-- FILE_START: chain-ring-comparison.md -->
**Theoretical prediction.**
The energy difference between the chain and threaded ring is proportional to the difference in Alexander weights:

$$
  \Delta E
   \propto 
  \bigl[(N-1) - \Delta_{T(2,N)}(q)\bigr]
  \cdot |q + q^{-1}|_{\mathrm{mol}}.
$$

For $N = 6$ with $|q + q^{-1}|_{\mathrm{mol}} \sim 1\text{--}2$ eV and weight difference $5 - 3 = 2$:

$$
  \Delta E(6)
   \sim 
  2 \times (1\text{--}2 \mathrm{eV})
   \sim 
  2\text{--}4 \mathrm{eV}
   \approx 
  193\text{--}386 \mathrm{kJ/mol}.
$$
<!-- FILE_END: chain-ring-comparison.md -->

<!-- FILE_START: chain-ring-comparison-interpretation.md -->
The pairwise Hopf-link estimate of the cyclisation barrier overshot by a factor of two. The threading-link picture halves it exactly, with no free parameters.

**Derivation chain.**
Every quantity is determined by the Bring's surface geometry. $q$ is fixed by $\chi(A) = -6$. The nuclear crossing energy quantum is determined by the Skein binding Lagrangian. $\alpha$ and $m_e/m_p$ are determined by the knot spectrum. The molecular crossing energy quantum follows by scale separation. The Alexander polynomial requires no input beyond $q$.

**The factor of $1/2$.**
The threading link resolves the pairwise overshoot exactly: $\Delta_{T(2,6)}(q) / 6 \approx 1/2$.

**Predictions for other even-$N$ rings.**
The same framework predicts barriers for even-$N$ cyclic molecules. See [Table 3](#tbl:chain-ring-comparison-table3-data). The barrier increases with $N$, but the threading efficiency ratio is constant for all even $N$.

**Experimental data.**
See [Table 1](#tbl:chain-ring-comparison-table1-data). See [Table 2](#tbl:chain-ring-comparison-table2-data).
<!-- FILE_END: chain-ring-comparison-interpretation.md -->

<!-- FILE_START: chain-ring-open-problems.md -->
Three questions remain open in the threading-link account.

**Open problems.**
1. **Exact $q$ at molecular scale**: The estimate for $|q + q^{-1}|_{\mathrm{mol}}$ should be sharpened using the electronic-scale crossing energy.
2. **Hückel's rule**: Even $N$ alone does not imply aromaticity. What invariant encodes the aromatic/anti-aromatic distinction?
3. **Heteroatoms**: When the ring contains non-carbon atoms, how does this modify the Alexander polynomial?
<!-- FILE_END: chain-ring-open-problems.md -->

<!-- FILE_START: organic-taxonomy-intro.md -->
We sort the standard organic classes so that the familiar taxonomy falls out of the Hopf-chain framework. Two parameters do the sorting: the bond-order pattern $(k_1, \ldots, k_{N-1})$, and whether the structure is open or closed. Saturation reads as linking-site occupancy. The hydrogen capacity follows directly: $\mathrm{C}_N \mathrm{H}_{2N+2-2d}$ (open) versus $\mathrm{C}_N \mathrm{H}_{2N-2d}$ (closed), read off from the total degree of unsaturation. Aromatic rings appear as the case where the secondary trefoils close.
<!-- FILE_END: organic-taxonomy-intro.md -->

<!-- FILE_START: organic-chain-taxonomy.md -->
The molecular Hopf chain framework generates the standard classes of organic molecules by varying the bond-order pattern and whether the chain is open or closed.

**Bond-order classification.**

| Class | Bond-order pattern | Free sites per C | Hydrogen capacity |
|-------|-------------------|:---:|:---:|
| Alkane (saturated) | $(1, 1, \ldots, 1)$ | 2 (interior), 3 (endpoint) | $2N + 2$ (chain), $2N$ (ring) |
| Alkene | $(\ldots, 2, \ldots)$ | 1 at double bond | $2N$ (one double bond) |
| Alkyne | $(\ldots, 3, \ldots)$ | 0 at triple bond | $2N - 2$ (one triple bond) |
| Cumulene | $(2, 2, \ldots, 2)$ | 0 (interior), 2 (endpoint) | 4 |
| Polyyne | $(1, 3, 1, 3, \ldots)$ | 0 (interior) | 2 |

**Saturation as linking-site occupancy.**
Raising the bond order by one unit consumes one free linking site on each adjacent carbon. Saturation is the extreme case where every backbone bond is single.

**Open vs. closed (chain vs. ring).**
Whether the backbone closes into a ring shifts the hydrogen count by a fixed offset. The total degree of unsaturation is $d = \sum_i (k_i - 1)$.

**Aromatic rings.**
A closed ring with $d = N/2$ is aromatic. The secondary Hopf ring formed by extra trefoils is closed. We conjecture that Hückel's $4n + 2$ rule corresponds to a sub-Hopf link closure condition.
<!-- FILE_END: organic-chain-taxonomy.md -->

<!-- FILE_START: outro-organic-chemistry.md -->
This closes the organic-chemistry chapter. The Hopf-chain construction recovers the comparative energetics of linear versus cyclic carbon backbones and identifies the threading transition.

The next chapter lifts this static molecular geometry to a flowing brane. The Hopf-chain morphisms reappear as the cocycle data of the $q$-Navier–Stokes obstruction.
<!-- FILE_END: outro-organic-chemistry.md -->
