The six Gröbner-Shirshov normal-form basis elements of $H_3(q)$
act on the Bring surface $\Sigma_4$ (genus $4$, $\chi = -6$) via
the Hecke representation. This remark makes the action explicit
and identifies the $\mathrm{SO}(3)$ structure that the current
pipeline exploits only partially.

## The six basis operators

The Hecke algebra $H_3(q)$ has dimension $3! = 6$. In the
Gröbner-Shirshov normal form, the basis elements are:

| $k$ | Name | Word | Permutation | $\operatorname{tr}_M$ at $q_0$ |
|---|---|---|---|---|
| 0 | $\gamma$ (identity) | $$ | $e$ | $1.000$ |
| 1 | $\sigma_0$ | $(0)$ | $(1\;2)$ | $0.499$ |
| 2 | $\sigma_1$ | $(1)$ | $(2\;3)$ | $0.499$ |
| 3 | $L_+$ | $(0, 1)$ | $(1\;2\;3)$ | $0.249$ |
| 4 | $L_-$ | $(1, 0)$ | $(1\;3\;2)$ | $0.249$ |
| 5 | $e^-$ | $(0, 1, 0)$ | $(1\;3)$ | $0.551$ |

The Gram matrix $G_{ij} = \operatorname{tr}_M(b_i \cdot b_j)$
encodes the inner-product structure: $G$ is a $6 \times 6$
symmetric positive-definite matrix whose inverse $G^{-1}$ defines
the Frobenius dual basis.

## Action on the Bring surface

Bring's surface $\Sigma_4$ has the structure of a degree-5
algebraic curve with $S_5$ symmetry. The three quark strands of a
baryon braid thread through the color-tube cubic
$\Delta(z) = z^3 + p z + r = 0$ on $\Sigma_4$, with the three
roots $z_1, z_2, z_3$ representing the quark positions on the
surface.

Each basis operator $b_k \in H_3(q)$ acts on the root triple
$(z_1, z_2, z_3)$ by permuting and $q$-deforming the roots:

| Operator | Action on roots | Geometric interpretation |
|---|---|---|
| $\gamma$ | $(z_1, z_2, z_3) \mapsto (z_1, z_2, z_3)$ | Identity — no crossing |
| $\sigma_0$ | $(z_1, z_2, z_3) \mapsto (q z_2, q^{-1} z_1, z_3)$ | Strands 1–2 cross; $q$-deformation shifts the roots along the color tube |
| $\sigma_1$ | $(z_1, z_2, z_3) \mapsto (z_1, q z_3, q^{-1} z_2)$ | Strands 2–3 cross |
| $L_+$ | $\sigma_0 \sigma_1$ | Full 3-cycle: $(1 \to 2 \to 3 \to 1)$ |
| $L_-$ | $\sigma_1 \sigma_0$ | Reverse 3-cycle: $(1 \to 3 \to 2 \to 1)$ |
| $e^-$ | $\sigma_0 \sigma_1 \sigma_0$ | Transposition $(1\;3)$ via braid relation |

The $q$-deformation factors distinguish this from the classical
$S_3$ permutation action: at $q = 1$, the action is pure
permutation; at $q = q_0 \neq 1$, each crossing
shifts the root positions along the color-tube fibre by a factor
of $q$ or $q^{-1}$.

## The $S_3 \subset \mathrm{SO}(3)$ gap

The six basis operators generate the **discrete** group
$S_3 \cong \mathrm{Dih}_3$ — the group of permutations of three
objects. This is a **subgroup** of $\mathrm{SO}(3)$:

$$
  S_3 \;\hookrightarrow\; \mathrm{SO}(3)
$$

embedded as the symmetry group of the equilateral triangle (the
three quark positions at $120°$ intervals on the color-tube
cross-section).

The **full** $\mathrm{SO}(3)$ acts by rotating the color-tube
cross-section continuously. This gives a continuous family of
crossing conventions parameterised by
$\mathrm{SO}(3) / S_3$ — a 3-dimensional manifold minus the
discrete quotient.

**Pipeline inputs:** only the $S_3$ subgroup — the six
discrete basis operators. The averaged crossing
$I = \sigma - (h/2) \cdot 1$ averages over the $S_3$ orbit.

**Pipeline exclusions:** the continuous
$\mathrm{SO}(3) / S_3$ rotations. These would give:

1. **Continuous families of Gram matrices** $G(\theta)$
   parameterised by rotation angle $\theta$. The LP shadow prices
   $y^*(\theta)$ would vary continuously, potentially identifying
   optimal orientations for the binding-energy prediction.

2. **Angular-momentum quantum numbers** from the
   $\mathrm{SO}(3)$ representation theory. The irreps of
   $\mathrm{SO}(3)$ are labelled by angular momentum $\ell$;
   restricting to $S_3$ gives the branching rule
   $V_\ell|_{S_3} = \bigoplus_\lambda n_{\ell,\lambda} V_\lambda$
   where the multiplicity $n_{\ell,\lambda}$ counts how many times
   each $S_3$ irrep appears in the $\ell$-th angular-momentum
   channel. These multiplicities are computable from character
   theory and may give the missing per-partition $\Delta_\lambda$
   values.

3. **Spherical harmonics on the Bring surface.** The Bring
   surface's genus-4 topology carries a natural Laplacian whose
   eigenfunctions are generalised spherical harmonics. The
   $\mathrm{SO}(3)$ action decomposes these into angular-momentum
   channels. The Markov trace, viewed as a function on the Bring
   surface, expands in these harmonics — giving a spectral
   decomposition of the mass formula in angular-momentum space.

## The Gram inverse on the Bring surface

The Gram inverse $G^{-1}$ defines the Frobenius dual basis:
$b_k^\vee = \sum_j (G^{-1})_{kj} b_j$. On the Bring surface,
$G^{-1}$ is the **metric inverse** — it converts between the
"crossing basis" (knot operators $b_k$) and the "demand basis"
(Frobenius duals $b_k^\vee$).

The LP/SDP operator-selection framework minimises
$\sum t_k x_k$ subject to Gram constraints. In the Bring-surface
interpretation, this is a **minimum-action principle on
$\Sigma_4$**: the optimal knot operator is the one that minimises
the action functional (Markov trace) over the moduli space of
braid embeddings in the Bring surface.

The $\mathrm{SO}(3)$ extension would make this a minimum-action
principle on $\Sigma_4 \times \mathrm{SO}(3) / S_3$ — optimising
over both the knot type AND the orientation. If the minimum over
orientations is unique (which would follow from the Bring
surface's rigidity as a hyperbolic 3-manifold complement), this
would derive the averaged-crossing convention from a variational
principle — closing
[`conj:canonical-knot-id-sdp`](#conj:canonical-knot-id-sdp).
