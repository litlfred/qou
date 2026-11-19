The Skein binding Lagrangian ([Skein binding Lagrangian](#def:skein-binding-lagrangian)) derives the smooth, liquid-drop nuclear binding energy directly from the categorical action. This derivation predicts that neutron excess grows with $p$. However, it misses the shell structure. Nuclei exhibit anomalously high binding at the stability pairs $\{2, 8, 20, 28, 50, 82, 126\}$. Shell corrections demand a discrete term in the binding energy. This escapes the smooth continuous formula.

**The gap in the derivation.**

The chain from the R-matrix to nuclear binding proceeds as:

$$
  \mathcal{R} \xrightarrow{\text{Yang--Baxter}}
  \check{R} \xrightarrow{\text{crossing asymmetry}}
  \mathfrak{E}_{\mathrm{cross}} \xrightarrow{\text{Skein binding}}
  \mathcal{L}_{\mathrm{bind}} \xrightarrow{\partial/\partial p}
  p^*(A).
$$

The final beta-stability step yields the smooth curve. The missing step is a discrete correction $\delta E_{\mathrm{shell}}(p, n)$. This is nonzero only when the multi-nucleon link $\mathcal{N}(Z, N)$ ([stable nucleus](#def:stable-nucleus)) possesses a specific topological structure.

**Conjecture: shell correction from closed sub-links.**

*Let $\mathcal{N}(Z, N) = Z\mathfrak{p} \oplus N\mathfrak{n}$ be a multi-nucleon link. The Skein polynomial $J_{\mathcal{N}}(q)$ factors into a product of Skein polynomials of closed sub-links at specific $(p, n)$ values. The shell correction is:*

$$
  \delta E_{\mathrm{shell}}(p, n)
  = 
  -\lambda_{\mathrm{shell}} \cdot
  \sum_{\text{closed sub-links } L_i \subset \mathcal{N}}
  \frac{|J_{L_i}(q)|}{|J_{\mathcal{N}}(q)|}.
$$

*The sum runs over maximal closed unlinked sub-links $L_i$ of $\mathcal{N}$. The shell energy scale is $\lambda_{\mathrm{shell}}$.*

**Closed sub-links of $\mathcal{N}(Z, N)$.**

A closed sub-link of $\mathcal{N}(Z, N)$ is a subset $S \subset \{1, \ldots, p+n\}$ of nucleons satisfying two conditions:

1. The restriction $\mathcal{N}|_S$ of the Hopf link to $S$ forms a split link, isotopic into a ball disjoint from all remaining nucleons.
2. The Skein polynomial of $\mathcal{N}|_S$ divides $J_{\mathcal{N}}$, yielding $J_{\mathcal{N}} = J_{\mathcal{N}|_S} \cdot J_{\mathcal{N}|_{S^c}} \cdot (\text{linking factor})$.

When these hold, the link factorizes. The nucleons in $S$ form an internally bound cluster. They contribute extra binding energy beyond the liquid-drop prediction.

**Predicted factorizations.**

For the Descartes universe ($\chi = -6$), this structure predicts the following factorizations:

See [Table](#tbl:skein-shell-correction-table-data).

The $\alpha$ particle $\mathcal{N}(2,2)$ acts as the fundamental closed sub-link. Its Skein polynomial factorizes completely. Stability pair nuclei are precisely those where the maximum possible number of $\alpha$ clusters form. They saturate all available Hopf junctions.

**The $\alpha$-cluster hypothesis.**

The closed sub-link structure predicts the shell correction is largest when $(p, n)$ admits the exact factorization:

$$
  \mathcal{N}(Z, N) = 
  k \times \mathcal{N}(2, 2)  \oplus 
  (p - 2k)\mathfrak{p}  \oplus 
  (n - 2k)\mathfrak{n},
$$

where $k = \min(\lfloor p/2 \rfloor, \lfloor n/2 \rfloor)$. The shell energy becomes:

$$
  \delta E_{\mathrm{shell}}
  = 
  -\lambda_{\mathrm{shell}} \cdot k
  = 
  -\lambda_{\mathrm{shell}} \cdot
  \min\!\left(\left\lfloor \frac{p}{2} \right\rfloor,
  \left\lfloor \frac{n}{2} \right\rfloor\right).
$$

This quantity is maximised when both $p$ and $n$ are even. Even-even nuclei host the most $\alpha$ clusters. It is locally maximised at the stability pairs, where the factorization is complete.

**Remaining obligations.**

1. **Skein factorization**: Prove that the Skein polynomial $J_{\mathcal{N}(Z, N)}(q)$ factors whenever $(p, n)$ admits an $\alpha$-cluster decomposition, via direct computation in the Skein algebra of the Hopf link.
2. **Shell energy scale**: Derive $\lambda_{\mathrm{shell}}$ directly from the categorical action in terms of $q$, $a_V$, and the Skein polynomial of $\mathcal{N}(2,2)$.
3. **Corrected stability formula**: Show that the total binding energy $\mathcal{L}_{\mathrm{bind}} + \delta E_{\mathrm{shell}}$ reproduces all observed stable isotopes to within $|\Delta n| \leq 1$ for all $p \leq 103$.
4. **Genus lift**: Show that including $\delta E_{\mathrm{shell}}$ lifts the stability cubic from genus $0$ to genus $1$, establishing a connection to the [elliptic stability conjecture](#rem:elliptic-stability-locus).
