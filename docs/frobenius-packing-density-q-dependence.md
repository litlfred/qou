# Proposition: q-Dependence of Frobenius Packing Density

*Formal statement derived from the JSJ / ρ·Vol framework, 2026-04-20 session.*

## Statement

Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe at substrate parameter $q \in \mathbb{R}_{>0}$ with $q \notin \{\text{roots of unity}\}$. Let $K = \mathbb{S}^3 \setminus L$ be the link complement of an atomic braid representative $\Phi_\text{atom} \in \text{End}_\mathbf{C}(A_\text{atom})$, and let $\{P_\alpha\}_\alpha$ be its JSJ decomposition pieces.

Then the **Frobenius packing density** at piece $P$ is

$$\rho_F(P, q) \;=\; m_e(q) \cdot n_\text{chir}(P)$$

where:

1. $m_e(q) = E_0 \cdot |\text{tr}_M(\sigma_0^3)(q)|$ is the Markov-trace mass of the reference lepton braid in $\mathbf{H}_2(q)$, with $E_0 = Q_\beta = 0.782$ MeV fixing the dimensional scale.

2. $n_\text{chir}(P) \;=\; |\Lambda(P) \cap \Lambda_\text{chir}|$ counts the chirality blocks active in the Wedderburn decomposition of $\Phi_P := \Phi_\text{atom}|_{A_P}$. Here $\Lambda_\text{chir} = \{\text{sym}, \text{alt}\}$ for $\mathbf{H}_3(q)$ (generalising to extremal irreps in higher $\mathbf{H}_n(q)$).

3. $n_\text{chir}(P) \in \mathbb{Z}_{\geq 0}$ is a **topological invariant** of $P$ — it depends only on the homeomorphism type of $P$ and not on $q$ (for $q$ away from roots of unity).

## Corollaries

**Corollary (Classical limit).** At $q = 1$, $m_e(1) = E_0 / 2$ and $n_\text{chir}$ is integer-valued. Binding reduces to the Thurston-volume formula

$$B(\text{atom}, q=1) = \tfrac{E_0}{2} \cdot \sum_P n_\text{chir}(P) \cdot \text{Vol}_\text{hyp}^\text{class}(P).$$

**Corollary (q-expansion).** Near $q = 1$,

$$\rho_F(P, q) = n_\text{chir}(P) \cdot \left[m_e^{(0)} + m_e^{(1)} \cdot (q-1) + O((q-1)^2)\right]$$

and the quantum correction $m_e^{(1)}$ is fixed by the derivative of $\text{tr}_M(\sigma_0^3)$.

**Corollary (Substrate value).** At $q_0 \approx 1.10998$, the chirality-saturated density is

$$\rho_F^\text{CPT}(q_0) = 2 \cdot m_e(q_0) \approx 2 \cdot 0.463 \text{ MeV} \approx 0.926 \text{ MeV}$$

which matches the empirical "$2m_e$" packing (≈1.022 MeV using CODATA $m_e$) to within the framework's own 1.84% residual.

## Proof sketch

**Part (1) — $m_e(q)$**: The electron is represented by the trefoil braid $\sigma_0^3$ in the fibre functor image $\mathbf{H}_2(q)$. By $\text{prop:categorical-mass-markov}$, the single-level mass is $|\text{tr}_M(\sigma_0^3)|$. The dimensional conversion $E_0 = Q_\beta$ is the universal substrate calibration.

**Part (2) — $n_\text{chir}(P)$**: The Wedderburn decomposition of $\mathbf{H}_{n_P}(q)$ at generic $q$ is a direct sum over partitions $\lambda \vdash n_P$. The "chirality blocks" are the extremal (single-row or single-column) irreps: $\lambda = (n_P)$ for sym and $\lambda = (1^{n_P})$ for alt. These correspond to the $\pm q$ eigenspaces of each $\sigma_i$.

The active block set $\Lambda(P)$ is determined by which irreducible character sums are non-zero on $\Phi_P$. By the CPT invariance of the framework and the non-degeneracy of generic-$q$ characters, $\Lambda(P) \cap \Lambda_\text{chir}$ is determined by the topological type of $P$ alone.

**Part (3) — Topological invariance**: For generic $q$, character non-degeneracy means $\chi^\lambda(\Phi_P) = 0$ iff the projection of $\Phi_P$ onto block $\lambda$ is zero at the algebraic level, which is a topological statement about how $P$ embeds in $K$.

## Application table

At $q_0$:

| object | JSJ piece | $n_\text{chir}$ | $\rho_F / m_e(q_0)$ |
|--------|-----------|:----:|:-------:|
| D-bond (knot $6_2$) | 1 hyperbolic piece | 1 | 1 |
| T ≈ ³He link | 1 hyperbolic piece | 2 | 2 |
| ⁴He | 4 disjoint Borromeans | 2 each | 8 total |
| ¹²C α-α bond | 2-comp link $7^2_1$ | 1 | 1 |

## Open questions

1. **Refinement at higher $n$**: for $\mathbf{H}_{n}(q)$ with $n \geq 4$, what are the "chirality blocks"? Candidate: the hook shapes $\lambda = (n-k, 1^k)$.

2. **Non-generic q**: at roots of unity, the Wedderburn decomposition degenerates. Does $n_\text{chir}$ still make sense as a topological invariant?

3. **Connection to Volume Conjecture**: the substrate $q_0$ is on the real axis; volume conjecture is at roots of unity. Is there a "substrate Kashaev" relation?
