The interpolation between the bound and free projections of [`conj:binding-qbeta-complex-volume`](#conj:binding-qbeta-complex-volume) is a *path*, and the bar-odd channel is its *holonomy*. No structure beyond the deformation itself is needed to "rotate between bound and free".

## The two endpoints are two representations

The free projection $\Pi_{\text{free}}$ — the inter-constituent confining crossings dropped, only linking data surviving — is the **abelian** representation of the knot group. The bound object — the full braiding — is the **discrete-faithful** side. These are the two distinguished points of the character variety of $K$.

## The path integral reading

Neumann–Zagier read the complex volume as the integral of a holomorphic 1-form along the path in the character variety joining these two representations \cite{neumann-zagier1985}. Transported to $\mathfrak{V}$:

$$
\mathfrak{V} \;=\; \Phi(\text{bound}) - \Phi(\text{free}),
\qquad
\mathfrak{E}_{\mathrm{bind}} = \mathrm{Re}\mathfrak{V},
\quad
\mathfrak{Q}_\beta = \mathrm{Im}\mathfrak{V},
$$

for a potential $\Phi$ on the deformation path: the endpoint difference of $\Phi$ *is* the projection defect $\mathrm{tr}_M((\Pi_{\text{free}} - \mathbf{1}) \circ \mathcal{M})$, its bar-even part is the volume (binding) channel, and its bar-odd part is the phase picked up along the path — exactly as $\mathrm{CS}$ is the phase companion of the hyperbolic volume, and consistent with the state-integral factorization picture \cite{garoufalidis-zagier-2024}.

## The categorical carrier, and where Askey enters

Pre-$\tau$ (base-ring convention: generic $R$ with bar involution, never $\mathbb{R}$ or $\mathbb{C}$), the path is carried by the deformation parameter $t$ of **one Askey–Wilson tridiagonal family**: at $t = 0$ the family sits at the $q$-Hermite bottom of the scheme — all Askey–Wilson parameters off, orthogonality measure the $q$-Plancherel weight $W_\lambda$, the free side — and at $t = 1$ it is the bound channel data. This is formalized as the conjecture class `AWDeformationPath` (Lean sibling of the conjecture), whose fields carry exactly these inputs: the family, the $q$-Hermite free endpoint, the potential with $\mathfrak{V}$ as endpoint difference, and one three-term ladder recurrence with a **bar-even multiplier**. The two-channel descent — the binding and $\mathfrak{Q}_\beta$ ladders each satisfying the *same* recurrence — is then a derived theorem (`AWDeformationPath.channel_ladders` via `recurrence_invol_descent`), not an assumption.

## Falsifiable consequence, and its current status

The class predicts one decidable numerical signature: the binding and $\mathfrak{Q}_\beta$ channel ladders share **one** bar-even three-term multiplier — equivalently, the multiplier solved from the complex ladder $\mathfrak{V}_A$ has vanishing bar-odd part. This is a probe of the holomorphic tie (not a parity projection, which is already known not to move the binding error). The *mechanism* half is compute-confirmed: the Hopf-power tower $\mathfrak{V}_n = \mathrm{tr}_M((\sigma_1^2)^n)$ rides one three-term recurrence with the bar-even multiplier $q^2 + q^{-2}$ (continuous $q$-ultraspherical class), exercising `recurrence_invol_descent` end-to-end. The *physical* identification — that the measured $c_k$-ladder is an Askey–Wilson instance of this mechanism — remains under-determined and gated on the even-channel $c_3$.
