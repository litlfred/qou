**Definition (Hecke curvature 2-cocycle).**
*The Hecke algebra $H_n(R, q)$ has free-algebra generators $\sigma_1,
\ldots, \sigma_{n-1}$ subject to two relations:*

$$
  R_H(i) \;:=\; \sigma_i^{\,2} - (q - q^{-1})\,\sigma_i - \mathbf{1}, \qquad
  R_{YB}(i) \;:=\; \sigma_i \sigma_{i+1} \sigma_i - \sigma_{i+1} \sigma_i \sigma_{i+1}.
$$

*The **Hecke curvature 2-cocycle** is the 2-form-valued bilinear
map $F \in C^2(H_n(R, q), H_n(R, q))$ defined on generator pairs by:*

$$
  F(\sigma_i, \sigma_j) \;=\;
  \begin{cases}
    R_H(i) & \text{if } i = j, \\
    R_{YB}(i) & \text{if } |i - j| = 1, \\
    [\sigma_i, \sigma_j] & \text{if } |i - j| \geq 2,
  \end{cases}
$$

*and extended to general elements by the Leibniz rule
$F(ab, c) = a F(b, c) + F(a, c) b$, $F(a, bc) = F(a, b) c + b F(a, c)$.
$F$ is a $2$-cochain in the Hochschild complex
([GB spectral sequence](#prop:gb-spectral-sequence)), and on the
free algebra $\mathbb{C}\langle \sigma_1, \ldots, \sigma_{n-1}\rangle$,
$F$ measures **failure of commutativity** at each generator pair
in the same way that the curvature $F_A = dA + A \wedge A$ of a
principal connection measures failure of flatness.*

**Definition (curvature-rank).**
*For an element $T_w \in H_n(R, q)$ written as a word in
$\sigma_i^{\pm 1}$ of length $\ell(T_w)$, the **curvature-rank**
$r(T_w)$ is the smallest non-negative integer $r$ such that*

$$
  F^{\,r}(T_w) \;=\; F\bigl(F\bigl(\cdots F(T_w)\cdots\bigr)\bigr)
  \;\in\; J^{\,r}(q) \setminus J^{\,r+1}(q),
$$

*where $F^{\,r}$ is the $r$-fold iterated curvature applied via
Leibniz extension, and $J^\bullet(q)$ is the GB confinement
filtration ([confinement level](#def:confinement-level)).
Equivalently, $r(T_w)$ counts the minimal number of times the
Hecke or Yang–Baxter relations must be applied to express $T_w$
in normal form starting from its free-algebra representative.*

*By construction $r(\mathbf{1}) = 0$, $r(\sigma_i) = 0$,
$r(\sigma_i^{\,2}) = 1$ (one Hecke reduction),
$r(\sigma_i \sigma_{i+1} \sigma_i) = 0$ in normal form but $1$ if
the YB relation must be applied.  In general,
$r(T_w) \leq \ell(T_w)$ with equality only for words requiring
maximal reduction.*

**Proposition (curvature-rank = GB filtration index).**
*The curvature-rank stratifies the GB filtration:*

$$
  \boxed{
    J^{\,r}(q) / J^{\,r+1}(q)
    \;=\;
    \bigl\{T_w \in H_n(R, q)\ \bigm|\ r(T_w) = r\bigr\},
  }
$$

*so the spectral-sequence pages of
[GB spectral sequence](#prop:gb-spectral-sequence) decompose by
curvature-rank:*

$$
  E_r^{\ell, *}(H_n(R, q))
  \;=\;
  \bigl\{ T_w\text{-induced cohomology classes of curvature-rank } \ell\bigr\}.
$$

*Consequence: the **non-abelian Stokes residue** of the Markov
trace at filtration depth $\ell$ equals the contribution from
words of curvature-rank $\ell$.*

**Corollary (six-term mass formula = curvature-rank decomposition).**
*By [unified knot mass](#thm:knot-mass-formula-unified) the
six-term mass decomposes over $E_\infty^{\ell, *}$, and by the
proposition each page corresponds to a curvature-rank stratum:*

See [Table](#tbl:curvature-rank-gb-stratification-table-data).

*Each term is the **non-abelian Stokes residue** at the corresponding
curvature-rank stratum of the GB filtration spectral sequence,
paired with the Markov-trace functional.*

**Geometric reading.**
*Under the archimedean realisation
([topological mass](#prop:topological-mass-formula)), the Markov
trace becomes a holonomy along the boundary of a Seifert surface,
and the curvature 2-cocycle $F$ becomes the curvature 2-form of
the corresponding flat connection on the Frobenius–Hopf bundle.
Non-abelian Stokes:*

$$
  \mathrm{tr}_M(\beta) \;=\; \mathrm{Hol}_{\partial \Sigma}\bigl(A\bigr)
  \;=\; \int_\Sigma F_A
  \;=\; \sum_{r \geq 0} \int_{\Sigma_r} F^{\,r}_A,
$$

*where $\Sigma_r \subset \Sigma$ is the curvature-rank-$r$ stratum
of the Seifert surface (its $r$-fold blow-up locus).
Each integral $\int_{\Sigma_r} F^r_A$ corresponds to the $E_\infty^{r,*}$
contribution and to one of the six mass terms.*

**Witness.**
[`computations/hecke_knot_ideal_tracker.py`](#) and
[`computations/knot_ideals_gb_jet_locations.py`](#)
identify hyperbolic-knot ideals at specific GB positions for the
proton and neutron braids.  The neutron's extra ideal at
(GB depth 3, jet 1, std channel) — the $6_1$ knot — is the
**curvature-rank-3 std-stratum residue** that is structurally
absent from the proton.  This residue is the algebraic origin of
the proton-neutron mass splitting at the Hochschild-cohomology
level.
