The Skein binding Lagrangian
([Skein binding Lagrangian](#def:skein-binding-lagrangian))
derives the smooth (liquid-drop) nuclear binding energy from
the categorical action.  This accounts for the trend — neutron
excess growing with $p$ — but misses the **shell structure**:
the stability pairs $\{2, 8, 20, 28, 50, 82, 126\}$ at which
nuclei have anomalously high binding.  The shell corrections
should arise from a discrete term in the binding energy that
the smooth formula does not capture.

**The gap in the derivation.**

The chain from R-matrix to nuclear binding is:

$$
  \mathcal{R} \xrightarrow{\text{Yang--Baxter}}
  \check{R} \xrightarrow{\text{crossing asymmetry}}
  \mathfrak{E}_{\mathrm{cross}} \xrightarrow{\text{Skein binding}}
  \mathcal{L}_{\mathrm{bind}} \xrightarrow{\partial/\partial p}
  p^*(A)
$$

The last step (beta-stability) gives the smooth curve.  The
missing step is a **discrete correction**
$\delta E_{\mathrm{shell}}(p, n)$ that is nonzero only when
the multi-nucleon link $\mathcal{N}(Z, N)$
([stable nucleus](#def:stable-nucleus)) has special topological
structure.

**Conjecture: shell correction from closed sub-links.**

*For the multi-nucleon link
$\mathcal{N}(Z, N) = Z\mathfrak{p} \oplus N\mathfrak{n}$,
the Skein polynomial $J_{\mathcal{N}}(q)$ factors into a
product of Skein polynomials of closed sub-links at specific
values of $(p, n)$.  The shell correction is:*

$$
  \delta E_{\mathrm{shell}}(p, n)
  = 
  -\lambda_{\mathrm{shell}} \cdot
  \sum_{\text{closed sub-links } L_i \subset \mathcal{N}}
  \frac{|J_{L_i}(q)|}{|J_{\mathcal{N}}(q)|}
$$

*where the sum runs over maximal closed (unlinked) sub-links
$L_i$ of $\mathcal{N}$, and $\lambda_{\mathrm{shell}}$ is the
shell energy scale.*

**Closed sub-links of $\mathcal{N}(Z, N)$.**

A **closed sub-link** of $\mathcal{N}(Z, N)$ is a subset
$S \subset \{1, \ldots, p+n\}$ of nucleons such that:

1. The restriction $\mathcal{N}|_S$ of the Hopf link to $S$
   is a **split link** — it can be isotoped into a ball
   disjoint from the remaining nucleons.

2. The Skein polynomial of $\mathcal{N}|_S$ divides
   $J_{\mathcal{N}}$: $J_{\mathcal{N}} = J_{\mathcal{N}|_S} \cdot J_{\mathcal{N}|_{S^c}} \cdot (\text{linking factor})$.

When this occurs, the link "factorizes" and the nucleons in
$S$ form an internally bound cluster that contributes extra
binding energy beyond the liquid-drop prediction.

**Predicted factorizations.**

For the Descartes universe ($\chi = -6$), the following
factorizations are expected:

See [Table](#tbl:skein-shell-correction-table-data).

The pattern: the $\alpha$ particle $\mathcal{N}(2,2)$ is the
fundamental closed sub-link (Skein polynomial factorizes
completely).  Stability pair nuclei are those where the maximal
number of $\alpha$ clusters can be formed, saturating the
available Hopf junctions.

**The $\alpha$-cluster hypothesis.**

The closed sub-link structure predicts that the shell correction
is largest when $(p, n)$ admits the factorization

$$
  \mathcal{N}(Z, N) = 
  k \times \mathcal{N}(2, 2)  \oplus 
  (p - 2k)\mathfrak{p}  \oplus 
  (n - 2k)\mathfrak{n}
$$

for $k = \min(\lfloor p/2 \rfloor, \lfloor n/2 \rfloor)$.
The shell energy is then

$$
  \delta E_{\mathrm{shell}}
  = 
  -\lambda_{\mathrm{shell}} \cdot k
  = 
  -\lambda_{\mathrm{shell}} \cdot
  \min\!\left(\left\lfloor \frac{p}{2} \right\rfloor,
  \left\lfloor \frac{n}{2} \right\rfloor\right).
$$

This is **maximised** when both $p$ and $n$ are even (even-even
nuclei have the most $\alpha$ clusters), explaining the
even-even dominance.  It is **locally maximised** at the
stability pairs, where the factorization is "complete" in a
sense to be made precise.

**Remaining obligations.**

1. **Skein factorization**: prove that the Skein polynomial
   $J_{\mathcal{N}(Z, N)}(q)$ factors when $(p, n)$ admits
   $\alpha$-cluster decomposition.  This is a computation in
   the Skein algebra of the Hopf link.

2. **Shell energy scale**: derive $\lambda_{\mathrm{shell}}$
   from the categorical action.  It should be expressible in
   terms of $q$, $a_V$, and the Skein polynomial of
   $\mathcal{N}(2,2)$.

3. **Corrected stability formula**: show that the total
   binding energy $\mathcal{L}_{\mathrm{bind}} + \delta E_{\mathrm{shell}}$ reproduces the observed stable
   isotopes to $|\Delta n| \leq 1$ for all $p \leq 103$.

4. **Genus lift**: show that including
   $\delta E_{\mathrm{shell}}$ lifts the stability cubic from
   genus $0$ to genus $1$, connecting to the
   [elliptic stability conjecture](#rem:elliptic-stability-locus).
