<!-- FILE_START: categorical-braiding-intro.md -->
The braid group is conventionally introduced through the topology of configuration spaces or knot complements. In our framework, however, braiding has a categorical origin. This algebraic structure precedes any geometric realisation and extends seamlessly to non-archimedean settings where knot complements are unavailable.

We first promote the abstract braiding $c_{X,Y} : X \otimes Y \xrightarrow{\sim} Y \otimes X$ from the rigid monoidal structure to a substrate-parametrised family indexed by $q \in \mathrm{End}(\mathbf{1})$. We prove the existence and uniqueness of this family and verify the hexagon coherence conditions under the substrate flow. We then specialise the categorical braiding to the Reshetikhin–Turaev framework to extract the categorical $R$-matrix. Finally, we tie the categorical $R$-matrix to the Hecke-skein relation, which drives subsequent normal-form computations. 

This establishes the foundational categorical braiding apparatus: the substrate-parametrised $R$-matrix, hexagon coherence, and the Hecke-skein relation.
<!-- FILE_END: categorical-braiding-intro.md -->

<!-- FILE_START: braid-action-tensor.md -->
Let $(\mathbf{C}, A, \tau)$ be a [quantum observable universe](#def:quantum-observable-universe) whose ambient category $\mathbf{C}$ is braided monoidal with braiding $c_{X,Y}\colon X\otimes Y \xrightarrow{ \sim } Y\otimes X$. For each object $V$ in $\mathbf{C}$ and each $n \geq 2$, there is a group homomorphism

$$
  \rho_n\colon B_n  \longrightarrow  \mathrm{Aut}_{\mathbf{C}}(V^{\otimes n})
$$

given on the Artin generators by

```tex
\begin{equation}\label{eq:categorical-braid-rep}
  \rho_n(\sigma_i)
  = 
  \mathrm{id}^{\otimes(i-1)}
  \otimes c_{V,V}
  \otimes \mathrm{id}^{\otimes(n-i-1)},
  \qquad 1 \leq i \leq n-1.
\end{equation}
```

The braid relation $\rho_n(\sigma_i)\rho_n(\sigma_{i+1})\rho_n(\sigma_i) = \rho_n(\sigma_{i+1})\rho_n(\sigma_i)\rho_n(\sigma_{i+1})$ is mathematically equivalent to the Yang--Baxter equation for the braiding $c_{V,V}$.

**Mathematical Novelty:** The braid-group action is standard (e.g., Kassel Thm XIII.1.3). However, its complete categorical Lean formalization in a generic braided monoidal category, achieved via an explicit hexagon and naturality chase, represents a non-trivial engineering contribution to formal verification.
<!-- FILE_END: braid-action-tensor.md -->

<!-- FILE_START: why-b3.md -->
The Descartes condition $\chi(A) = -6$ forces the gauge group to be a quantum form of $\mathrm{SU}(2)$, which has rank $2$. Consequently, the fundamental representation $V$ is $2$-dimensional. On $V^{\otimes 2}$, the braiding provides a single operator $c_{V,V}$. The first non-trivial braid group action occurs on $V^{\otimes 3}$, where the two generators $\sigma_1, \sigma_2$ of $B_3$ act via the categorical braid representation.
<!-- FILE_END: why-b3.md -->

<!-- FILE_START: categorical-boson-fermion.md -->
The Schur--Weyl decomposition $V^{\otimes 3} \cong V_{\frac{3}{2}} \oplus V_{\frac{1}{2}}^{\oplus 2}$ separates the symmetric (spin-$\frac{3}{2}$) and mixed-symmetry (spin-$\frac{1}{2}$) sectors. The $B_3$-action preserves this decomposition. On the symmetric sector, the generators act as scalars, producing bosonic exchange. On the mixed-symmetry sector, they act non-trivially, producing fermionic exchange. This categorical distinction between bosons and fermions requires no topological input.
<!-- FILE_END: categorical-boson-fermion.md -->

<!-- FILE_START: symmetric-quotient-colour.md -->
The quotient $B_3 \twoheadrightarrow S_3$ obtained by imposing $\sigma_i^2 = \mathrm{id}$ corresponds to passing from a :refterm[braided monoidal category]{#braided-monoidal-category} to a symmetric monoidal one, requiring $c_{V,V}^2 = \mathrm{id}$. In the Descartes universe, the three copies of $S_3$ inside $S_5 = \mathrm{Aut}(\Sigma_4)$ are images of three such quotients. Each quotient corresponds to a colour sector $\mathfrak{r}, \mathfrak{g}, \mathfrak{b}$. Lifting these three $S_3$ subgroups back to $B_3$ via the braiding of $\mathrm{Rep}(\mathrm{SU}_q(2))$ recovers the non-trivial exchange phases that distinguish quarks from leptons.
<!-- FILE_END: symmetric-quotient-colour.md -->

<!-- FILE_START: braid-base-field.md -->
The result [braid action on tensor products](#prop:braid-action-tensor) uses only the braided monoidal structure of $\mathbf{C}$. In particular:

1. For the archimedean realisation ([$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe)), the braiding is computed by the $R$-matrix of $\mathcal{U}_q(\mathfrak{su}(2))$. The $B_n$-action recovers standard skein relations as traces on braid-group representations.
2. For the $\mathfrak{p}$-adic realisation ([$p$-adic realisation](#ex:p-adic-realisation)), the same braiding exists on $\mathrm{Rep}(\mathrm{SU}_{q(p)}(2))$ over $\mathbb{Q}_\mathfrak{p}$. The Yang--Baxter equation holds generically over any base ring.
3. For the finite-field realisation ([finite field realisation](#ex:finite-field-realisation)), the braiding persists on the fusion category $\mathrm{Rep}_{\mathbb{F}_\mathfrak{p}}(\mathrm{SU}_q(2))$.

The skein relations, knot invariants, and hyperbolic volumes that appear in the archimedean setting are therefore consequences of the categorical braiding evaluated via a specific fibre functor. They are not the source of the braid-group structure.
<!-- FILE_END: braid-base-field.md -->

<!-- FILE_START: braid-lifting-compatibility.md -->
The [jet prolongation](#prop:jet-prolongation) preserves the braided monoidal structure. If $\mathbf{C}$ is braided, the jet object $J^1(A) = A \otimes \Omega^1(A)$ inherits a braiding from the tensor product of the braidings on $A$ and $\Omega^1(A)$. Consequently, the braid-group representations $\rho_n$ at each level of the brane tower are compatible with the transition maps. The direct-limit algebra $\mathcal{A}_\infty = \varinjlim\Gamma(J^1 \mathcal{S}_n, \mathrm{SU}_{q_n}(2))$ thus carries a well-defined $B_n$-action for every $n$.
<!-- FILE_END: braid-lifting-compatibility.md -->

