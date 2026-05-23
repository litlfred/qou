The archimedean functor $\tau \colon \mathbf{C} \to \mathbf{Arch}$
([def:archimedean-realization-functor](#def:archimedean-realization-functor))
maps each algebraic structure on the categorical side to a concrete
real-valued object at the substrate parameter $q_0$. The table below
catalogues these images systematically, distinguishing structures
that are **implemented** in the current pipeline from those that
remain open infrastructure targets.

The organising principle: every row is a functorial image. Where the
image is a scalar, it enters the mass formula directly. Where the
image is a richer object (polynomial, matrix, family), it carries
structural data beyond what any single scalar evaluation can access.
The HOMFLYPT family (row 5) is the first non-trivial example: it
simultaneously encodes the quantum $\mathrm{SU}(N)$ invariant for
*every* rank $N$, and its polynomial coefficients (integers,
$q$-independent) survive the functor as categorical constants.

| # | Categorical structure | Algebraic home | $\tau$-image at $q_0$ | Duality | Observable / role | Status |
|---|---|---|---|---|---|---|
| 1 | Braid group $B_n$ element $\beta$ | $B_n$ | Hoefsmit matrix $\rho(\beta) \in \mathrm{Mat}(\mathbb{R})$ | $\beta^{-1}$ (group inverse; time-reversal) | Input to mass formula | implemented (PyHecke) |
| 2 | Hecke algebra $H_n(q)$ element $T_w$ | $H_n(q)$ | Seminormal matrix at $q_0$ | $S(T_w) = T_{w^{-1}}$ (Hopf antipode; crossing reversal $\to$ p/n mass split) | Intermediate representation | implemented |
| 3 | Markov trace $\operatorname{tr}_M(\beta)$ | $\mathbb{Q}(q) \to \mathbb{R}$ | $\operatorname{tr}_M(\beta)(q_0) \in \mathbb{R}$ | Ocneanu trace $\tau(\cdot;\, s)$ (specialisation $\leftrightarrow$ generalisation) | Mass ratio $\mathfrak{m}_K / m_e$ | implemented |
| 4 | Jones polynomial $J_K(q)$ | $\mathbb{Z}[q^{\pm 1}]$ | $J_K(q_0) \in \mathbb{R}$ | $J_{\bar K}(q) = J_K(q^{-1})$ (mirror; matter/antimatter CPT) | $= \operatorname{tr}_M$ (SU(2) specialisation) | implemented (= row 3) |
| 5 | **HOMFLYPT** $P(K; a, z)$ | $\mathbb{Z}[a^{\pm 1}, z^{\pm 1}]$ | $\{P(K; q_0^{N-1}, h_q)\}_{N \geq 2} \in \mathbb{R}^\infty$ | $P(\bar K) = P(K;\, a^{-1}, z)$ (mirror symmetry; chirality for all SU($N$)) | **Family of observables indexed by $N$** | **not built** |
| 6 | Colored Jones $J_K^{(V)}(q)$ | per-irrep polynomial | $J_K^{(V)}(q_0) \in \mathbb{R}$ per $V$ | $J_K^{(V^*)}$ (representation dual; particle/antiparticle) | Per-representation channel | not built |
| 7 | Wedderburn decomposition $\{\dim_q V_\lambda\}$ | $\mathbb{R}^{|\mathrm{Part}(n)|}$ | $\{\dim_{q_0} V_\lambda\}$ | $\{\dim_q V_{\lambda'}\}$ (conjugate partition; Young transpose) | Per-partition quantum dimensions | implemented |
| 8 | Frobenius pairing $y_\lambda \chi_\lambda$ | weight decomposition | $y_\lambda(q_0) \cdot \chi_\lambda(\beta)(q_0)$ | dual basis $y^*_\lambda$ (Frobenius self-duality; weight $\leftrightarrow$ character) | Per-partition mass contributions | implemented |
| 9 | LP/SDP shadow prices $y^*$ | dual variables | $y^*(q_0) \in \mathbb{R}^m$ | primal $x$ (LP strong duality; binding-energy shadow prices) | Binding-energy shadow prices | implemented |
| 10 | Kauffman bracket $\langle K \rangle(A)$ | $\mathbb{Z}[A^{\pm 1}]$ | $\langle K \rangle(q_0^{1/4}) \in \mathbb{R}$ | $\langle \bar K \rangle$ (mirror bracket; writhe conjugation) | Unnormalized Jones | partially (hardcoded knots) |
| 11 | Alexander polynomial $\Delta_K(t)$ | $\mathbb{Z}[t^{\pm 1}]$ | $\Delta_K(q_0) \in \mathbb{R}$ | $\Delta_K(t^{-1}) = \Delta_K(t)$ (Fox calculus; fibered $\leftrightarrow$ non-fibered) | HOMFLYPT at $N \to \infty$ | not built explicitly |
| 12 | Khovanov homology $H^{i,j}(K)$ | bigraded $\mathbb{Z}$-module | Euler char $\to$ Jones | $H_{i,j}$ (Poincaré duality; categorified mirror) | Categorified Jones | not built (out of scope) |
| 13 | Knot group $\pi_1(S^3 \setminus K)$ | finitely-presented group | ? | peripheral system (Dehn surgery duality) | Open question | open |

**Reading the table.** Rows 1--4 and 7--9 form the *implemented
derivation chain*: categorical data enters as a braid (row 1), is
represented in the Hecke algebra (row 2), traced via the Markov
trace (row 3 = row 4 at $N = 2$), decomposed through
Wedderburn / Frobenius (rows 7--8), and optimised via LP/SDP
(row 9). Every step is implemented and produces a real observable
at $q_0$.

**The duality column.** Each algebraic structure admits a natural
dual that pairs with it under a specific duality type. The
physically deepest entries are:

- **Row 2 (Hopf antipode).** The Hecke antipode $S(T_w) = T_{w^{-1}}$
  is the algebraic expression of *crossing reversal*. Under $\tau$,
  this is the structural mechanism behind the proton/neutron mass
  split: the proton and neutron braids $\beta_p, \beta_n$ differ by
  crossing signs, and $S$ is the map between them. The
  $\tau$-image of $S$ is the real-valued gap
  $\operatorname{tr}_M(\beta_n) - \operatorname{tr}_M(\beta_p)$,
  which (after calibration) gives $Q_\beta$.

- **Row 5 (HOMFLYPT mirror).** The mirror $P(\bar K) = P(K; a^{-1}, z)$
  simultaneously encodes chirality for *every* SU($N$) channel. This
  is the multi-$N$ generalisation of CPT in row 4 (Jones mirror):
  where row 4 gives matter/antimatter at $N = 2$, row 5 gives
  matter/antimatter at every representation-theoretic rank.

- **Row 9 (LP strong duality).** The primal/dual pair $(x, y^*)$ in
  the operator-selection LP is already central to the mass formula:
  $y^*$ are the binding-energy shadow prices, and strong duality
  guarantees that $\sum t_i x_i^* = n_{\mathrm{target}} \cdot y_0^*$.
  The duality here is *self-contained* — both sides live at the
  same $q_0$ — whereas rows 2 and 5 are dualities that pair
  *different physical states* (proton/neutron, particle/antiparticle).

Row 5 (HOMFLYPT) is the highest-value open infrastructure target:
it gives the **entire** $N$-indexed family in a single computation,
where the current pipeline accesses only the $N = 2$ slice. The
polynomial coefficients are integers ($q$-independent), so they
sit on the *correct axis* for structural derivations that the
reframing in [PR #957](https://github.com/litlfred/qou/pull/957)
identified: constants from substrate, not $q$-dependent
coincidences.

**The HOMFLYPT specialisation family.** For a braid closure
$\hat\beta$ with HOMFLYPT polynomial
$P(\hat\beta; a, z) \in \mathbb{Z}[a^{\pm 1}, z^{\pm 1}]$:

$$
  P(\hat\beta;\, q_0^{N-1},\, q_0 - q_0^{-1})
  \;=\;
  \text{quantum } \mathrm{SU}(N) \text{ invariant of } \hat\beta
  \qquad (N = 2, 3, 4, \ldots)
$$

| $N$ | Specialisation $(a, z)$ | Name | Physical channel |
|---|---|---|---|
| 2 | $(q_0^{-1},\, h_q)$ | Jones polynomial | mass ratio (current pipeline) |
| 3 | $(q_0^2,\, h_q)$ | SU(3) invariant | color structure |
| 4 | $(q_0^3,\, h_q)$ | SU(4) invariant | electroweak channel (speculative) |
| $\infty$ | — | Alexander polynomial | classical / homological |

Each row is a *different functor image* of the same categorical
object $P(K)$, evaluated at a different representation-theoretic
point. The mass tower may use different $N$-slices for different
particles — this is not constrained by the current pipeline, which
accesses only $N = 2$.
