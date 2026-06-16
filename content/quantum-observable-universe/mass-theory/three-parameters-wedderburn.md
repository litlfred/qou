The number of calibration inputs
([calibration inputs](#rem:calibration-inputs)) is not ad hoc:
it equals the number of **irreducible representations** of
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

The physics endomorphism $\Phi \in \mathrm{End}_{\mathbf{C}}(A)$
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

## Physical identification

| Parameter | Irrep | Observable | What it fixes |
|:---:|:---:|:---:|:---|
| $\alpha_1$ | $(3)$ symmetric | $m_\mu/m_e$ | Substrate $q_0$ (all crossings $+q$) |
| $\alpha_2$ | $(2,1)$ standard | $m_e$ | Mass scale (mixed eigenvalues) |
| $\alpha_3$ | $(1{,}1{,}1)$ alternating | $\mathfrak{Q}_\beta(n)$ | Interaction scale (all crossings $-q^{-1}$) |

The symmetric sector sees only $+q$ eigenvalues — it controls
the **shape** of the universe (how far $q$ is from $1$).
The alternating sector sees only $-q^{-1}$ eigenvalues — it
controls the **interaction strength** (the antisymmetric
channel that drives beta decay).  The standard sector mixes
both eigenvalues — it controls the **mass scale** (the
conversion between Hecke algebra units and MeV).

## Why three suffices for all $A$

Nuclear computations at Level 0 use $H_A(R, q)$ (one strand per
nucleon), which for $A > 3$ has more than three irreps.
However, the typed crossing operators
([typed crossing operator](#def:typed-crossing-operator))
$C(\mathfrak{p}, \mathfrak{p})$, $C(\mathfrak{p}, \mathfrak{n})$,
$C(\mathfrak{n}, \mathfrak{n})$ are determined entirely by the
three $H_3(R, q)$ parameters:

$$
  C(\mathfrak{p}, \mathfrak{p}) = \sigma \quad (d = 0),
  \qquad
  C(\mathfrak{n}, \mathfrak{n}) = \sigma - h \quad (d = -h),
  \qquad
  C(\mathfrak{p}, \mathfrak{n}) = \sigma - h/2 \quad (d = -h/2).
$$

These three crossing types span all possible nucleon-nucleon
interactions.  The coefficients $(0, -h, -h/2)$ are fixed by
$q$ alone (via $h = q - q^{-1}$), and the energy scale $E_0$
converts NF differences to MeV.  No additional parameters
appear at higher $A$ because the $H_A(R, q)$ computation
factorizes through these three crossing types.

## Cross-check: leptonic sector

For $H_2(R, q)$ (two strands, leptonic physics):
- Partitions of $2$: $(2)$ and $(1{,}1)$
- $H_2(R, q) \cong k \oplus k$, $\dim = 1^2 + 1^2 = 2$
- Two irreps $\to$ two parameters ($q$ and $m_e$)
- No standard representation $\to$ no interaction scale needed

This is consistent: leptonic physics (electron, muon, tau)
requires only two inputs.  The third input ($\mathfrak{Q}_\beta$) is
needed only when the alternating sector participates — i.e.,
when matter and antimatter crossings coexist within a
composite (hadrons).
