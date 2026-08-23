The number of calibration inputs
([calibration inputs](#rem:calibration-inputs))
equals the number of **irreducible representations** of
$H_3(R, q)$, which is the number of partitions of $3$.

## Wedderburn-Artin decomposition

The Iwahori--Hecke algebra $H_3(R, q)$ is semisimple for generic
$q$ and decomposes via the Wedderburn theorem as:

$$
  H_3(R, q)
  \;\cong\;
  \underbrace{M_1(k)}_{\lambda = (3)}
  \;\oplus\;
  \underbrace{M_2(k)}_{\lambda = (2,1)}
  \;\oplus\;
  \underbrace{M_1(k)}_{\lambda = (1{,}1{,}1)}
$$

with dimensions $1^2 + 2^2 + 1^2 = 1 + 4 + 1 = 6 = \dim H_3(R, q)$.

Each simple component corresponds to an irreducible
representation labelled by a partition $\lambda \vdash 3$:

| Partition | Irrep | $\dim V_\lambda$ | Eigenvalue of $\sigma_i$ | Physical sector |
|:---:|:---:|:---:|:---:|:---|
| $(3)$ | Symmetric | $1$ | $+q$ | Shape (deformation) |
| $(2,1)$ | Standard | $2$ | $+q$ and $-q^{-1}$ mixed | Scale (mass ruler) |
| $(1{,}1{,}1)$ | Alternating | $1$ | $-q^{-1}$ | Interaction (hadronic) |

## On-shell projection

The Lagrangian endomorphism $\Phi \in \mathrm{End}_{\mathbf{C}}(A)$
([categorical action](#def:categorical-action)) decomposes
over the three irreps via the central idempotents $e_\lambda$:

$$
  \Phi
  =
  \alpha_1 \cdot e_{(3)}
  +
  \alpha_2 \cdot e_{(2,1)}
  +
  \alpha_3 \cdot e_{(1{,}1{,}1)}
$$

The on-shell condition $\star_q F = F$, observability
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$, and gauge
invariance reduce each component to one real scalar:

| Component | Raw dim | $-$ Ad | $-$ $\star$ | $-$ gauge | Surviving |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $M_1$ (symmetric) | $1$ | $0$ | $0$ | $0$ | **$1$** |
| $M_2$ (standard) | $4$ | $1$ | $1$ | $1$ | **$1$** |
| $M_1$ (alternating) | $1$ | $0$ | $0$ | $0$ | **$1$** |
| **Total** | $6$ | | | | **$3$** |

Three irreps, three surviving parameters, three calibration
inputs.

The physical identification of the three parameters, the sufficiency
argument for all $A$, and the leptonic-sector cross-check are collected in
[the three-parameter context](#rem:three-parameters-wedderburn-context).
