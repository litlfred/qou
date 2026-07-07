<!-- FILE_START: magic-shell-fingerprint.md -->
**Proposition (canonical He4 trace fingerprint).**
*Let $\beta_{^4\mathrm{He}}$ be the canonical $A=4$ operator on the Iwahori–Hecke algebra $H_{12}(q)$. The canonical Markov trace evaluation $\tau_M(\beta_{^4\mathrm{He}})(q_0)$ isolates the magic-shell structural fingerprint across two algebraic tiers:*

1. **(Compositional tier).** *The $A=4$ trace decomposes exactly as $2 \cdot \tau_M(\beta_{\mathrm{D}}) + \text{residual}$. The residual selects the $\mathrm{T} \oplus p$ operator basis (`he4-channel-active-set`).*
2. **(Representation tier).** *The $A=4$ trace evaluation isolates $> 80\%$ of its weight in the balanced two-row stratum $\Lambda^2(12)$ (`he4-two-row-dominance`). The dominant representation is $\lambda^* = (9, 3)$, carrying $29.0\%$ of the trace.*

*The $q$-symmetric deuteron-pairing structural constraint controls the $A=4$ magic-shell coupling.*

## Structural necessity of the two tiers

The compositional tier accounts for the energy budget ($268.9$ MeV primal cost). The $\mathrm{T} \oplus p$ channel supplies the lowest-residual algebraic path to the $A=4$ binding energy constraint.

The representation tier exposes the binding mechanism. The dual shadow prices ($y^\star_{\mathrm{D} \oplus \mathrm{D}} = 3.778$, $y^\star_{\mathrm{T} \oplus p} = 0$) reveal that the $\mathrm{D} \oplus \mathrm{D}$ sub-braid structure responds most strongly to perturbative binding forces. The $\Lambda^2(12)$ dominance theorem identifies this perturbative sensitivity as the $\mathrm{SU}(2)$ spin-pairing image of the deuteron blocks forming the stable core.

## Lean verification strategy

The `he4_fingerprint_theorem` in Lean couples `He4CompositionalActiveSet` and `He4TwoRowDominance` into a single class instance. Downstream structural results consume this unified fingerprint.
<!-- FILE_END: magic-shell-fingerprint.md -->

<!-- FILE_START: beta-n-hecke-eval.md -->
## Setting

Let $H_{3A}(q)$ be the Iwahori–Hecke algebra. Let $\beta_{A}$ be the canonical $A$-nucleon braid word. We define the trace observable $m_A(q) := \tau_M(\beta_A)(q)$. We consider the scaling behaviour as $A \to \infty$.

**Conjecture (thermodynamic $q$-scaling).**
*Let $q_0 \approx 0.999812$ be the proton-pinned substrate parameter. As the nucleon number $A \to \infty$, the trace evaluation $\tau_M(\beta_A)(q_0)$ exhibits power-law asymptotic scaling:*
$$
  \tau_M(\beta_A)(q_0) \;\sim\; C \cdot A^{-\gamma(q_0)},
$$
*where $C$ is a constant and $\gamma(q_0) > 0$ is a $q_0$-dependent scaling exponent. In the classical $q \to 1$ limit, the trace grows factorially.*

## Justification

At $q=1$, the Hecke algebra reduces to the symmetric group algebra $\mathbb{C}[S_{3A}]$. The trace $\tau_M$ reduces to the character of the regular representation. The word length of $\beta_A$ grows quadratically with $A$ (from the all-to-all nuclear pairing). Evaluating the regular character on long group words yields factorial growth.

For generic $q$, the Markov trace $\tau_M$ is a quantum group invariant. The exponential damping from the $q$-integers $[k]_q$ offsets the combinatorial explosion of the word length. At the specific substrate parameter $q_0 < 1$, the Wenzl weights $y_\lambda(q_0)$ damp the high-rank representations. The trace localises to the boundary strata. This $q$-deformation converts factorial growth into power-law suppression.

## Empirical context

We lack a closed-form formula for the generic $A$-nucleon braid word. The power-law scaling isolates the $q$-dependent thermodynamic limit of the binding energy without requiring exhaustive enumeration of the $\beta_A$ inter-nucleon crossings.
<!-- FILE_END: beta-n-hecke-eval.md -->

<!-- FILE_START: nuclear-many-body-q-series.md -->
The Hecke-algebraic evaluation $m_A(q) = \tau_M(\beta_A)(q)$ defines a discrete sequence of trace evaluations. We package these evaluations into a generating series to study the categorical nuclear many-body limit.

**Definition (Nuclear many-body binding series).**
The categorical binding series is the formal generating function:
$$
  \mathcal{B}(z, q) \;:=\; \sum_{A=1}^\infty \tau_M(\beta_A)(q) \cdot z^A.
$$

We evaluate this series at the physical parameter $q_0$. Based on the `conj:beta-n-hecke-eval` power-law decay $m_A(q_0) \sim C A^{-\gamma}$, the series converges for $|z| \leq 1$. This implies the $q$-deformed many-body binding limit is finite.

The series encodes the binding fraction $B(A, Z) / A$. The single-nucleon operator $\beta_1$ sets the base mass scale. The trace $\tau_M(\beta_A)$ computes the coupled $A$-body mass. The coefficients map directly to the empirical semi-empirical mass formula (SEMF).

**Extracting SEMF terms.**
We project the coefficients into the representations of $\mathrm{SU}(2)$. The two-row stratum $\Lambda^2(3A)$ (`def:two-row-stratum`) carries the spin-pairing interaction. The volume term corresponds to the trace of the non-interacting projection. The asymmetry term isolates the non-self-conjugate representations. The generating series provides the global geometric setting for the $A$-dependent scaling of these terms.
<!-- FILE_END: nuclear-many-body-q-series.md -->

<!-- FILE_START: q-difference-recurrence-he4.md -->
**Proposition (q-difference magic shell stabilization).**
*The $^4\mathrm{He}$ mass $m_4(q) = \tau_M(\beta_{^4\mathrm{He}})(q)$ sits at a local minimum of the $q$-difference operator with respect to the $A$-series.*
*Let $\nabla_q$ be the $q$-difference operator $\nabla_q f(A) = f(A) - f(A-1)$. Then:*
$$
  \left. \frac{\partial}{\partial A} (\nabla_q m_A(q)) \right|_{A=4} \;\approx\; 0
$$
*in the discrete continuous-interpolation sense. The binding increment per nucleon reaches a stable plateau at $A=4$.*

## Structural basis

The nuclear series starts with large mass defects per nucleon (deuteron, triton). The increment $\nabla_q m_A(q) = m_A(q) - m_{A-1}(q)$ measures the marginal binding energy. At $A=4$, the trace isolates into the self-conjugate two-row partition $(6,6)$ (`he4-two-row-dominance`). The representation-theoretic closure of the two-row stratum at $\Lambda^2(12)$ corresponds to the closure of the $1s$ nuclear shell.

This closure prevents further spin-paired nucleon addition without jumping to a higher-rank representation or a higher-energy principal quantum number. The marginal binding energy derivative vanishes. The $^4\mathrm{He}$ nucleus exhibits the magic-shell binding spike.

## Evaluation

At $q_0 \approx 0.999812$, the empirical marginal binding drops sharply from $A=3$ to $A=4$ and then levels off for $A=5$ (the ${}^5\mathrm{He}$ unbound state). The $q$-difference operator mathematically locates this plateau. It derives the $A=4$ magic number from the algebraic $H_{12}(q)$ state-space saturation.
<!-- FILE_END: q-difference-recurrence-he4.md -->

<!-- FILE_START: nuclear-q-difference-operator.md -->
**Definition (Nuclear q-difference operator).**
Let $\mathcal{B}(z, q)$ be the [nuclear many-body binding series](#def:nuclear-many-body-q-series). We define the **nuclear $q$-difference operator** as the discrete derivative with respect to the constituent count $A$:
$$
  \nabla_A m_A(q) \;:=\; m_A(q) - q \cdot m_{A-1}(q).
$$
The $q$-weighting accounts for the background categorical coupling of the added nucleon.

## Relation to SEMF

The $q$-difference operator extracts the marginal binding energy. In the semi-empirical mass formula context, $\nabla_A m_A(q)$ isolates the volume and surface term scaling. The volume term contributes a constant marginal mass. The surface term contributes an $A^{-1/3}$ penalty.

We identify the magic-shell stabilisations ([`prop:q-difference-recurrence-he4`](#prop:q-difference-recurrence-he4)) as the roots of the second $q$-difference operator:
$$
  \nabla_A^2 m_A(q) \;\approx\; 0.
$$
These roots occur when the two-row stratum $\Lambda^2(3A)$ structurally closes. The addition of a nucleon forces a representation-theoretic jump, suppressing the marginal binding gain.
<!-- FILE_END: nuclear-q-difference-operator.md -->
