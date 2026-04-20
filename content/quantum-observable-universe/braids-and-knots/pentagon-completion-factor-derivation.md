The pentagon-completion factor $\rho(\lambda, A)$ in the restated
[tower binding energy](#prop:tower-binding-energy) quantifies how
much the singleton-only log-form captures of the true per-irrep
contribution to $B$.  We derive its value for each kind of irrep
from the pentagon-ascension bound and the single-vortex-to-log-form
reduction.

## Setup

For an atom with $A$ nucleons the single-vortex mass formula
([mass endomorphism tower](#prop:mass-endomorphism-tower)) has
three additive pieces for each irrep $\lambda$ of $H_A(q)$:

$$
  \mathfrak{m}^\lambda
  \;=\;
  \underbrace{\Bigl\lvert\prod_{i=0}^{A-2}\hat{V}_i^\lambda\Bigr\rvert}_{\text{descended}}
  \;+\;
  \underbrace{\sum_{i=0}^{A-2} \Phi_q(\hat{V}_i^\lambda)}_{\text{singletons}}
  \;+\;
  \underbrace{\sum_{0\leq i<j\leq A-2} z^2 \cdot \Phi_q(\hat{V}_i^\lambda \hat{V}_j^\lambda)}_{\text{pair terms}}.
$$

The **log-form** [tower binding energy](#prop:tower-binding-energy)
uses only the singleton sum; the descended and pair terms are
assumed to ascend into the next jet level via
[pentagon ascension bound](#prop:pentagon-ascension-bound).  The
ascension requires the pentagon identity of the quantum Bloch
group ([quantum Bloch group](#def:quantum-bloch-group)) — which
needs **at least $3$ elements** — and a quasi-commutativity bound.

$\rho(\lambda, A)$ measures how completely the pair terms ascend,
given that $\lambda$ has $\dim_q(\lambda) \cdot (A-1)$ effective
matrix elements.

## Derivation by irrep dimension

**Case 1: $\dim_q(\lambda) = 1$ (trivial, sign irreps).**

The Hecke generator $\sigma_i$ acts as a scalar in $\lambda$
(eigenvalue $q$ for sym, $-q^{-1}$ for alt).  The character $\hat{V}_i^\lambda$
is a SINGLE scalar per generator.  The pair term
$\Phi_q(\hat{V}_i \hat{V}_j)$ is then a $\Phi_q$ of a scalar product
$V_i V_j$, which DOES satisfy the pentagon identity trivially
(as commuting scalars): $\Phi_q(V_i V_j) = \Phi_q(V_i) \Phi_q(V_j)$
exactly when $V_i$ and $V_j$ commute (scalars always do).

Thus for $1$-dim irreps the "pair term" reduces exactly to
$z^2 \Phi_q(V_i) \Phi_q(V_j)$ which combines multiplicatively
with the singletons, producing an effective $(1 + z^2 V_i V_j)$
correction per pair — absorbed into the redefinition
$\Phi_q \mapsto \tilde\Phi_q$ of the analytic continuation.
Hence $\rho(\lambda, A) = 1$ **identically** for all $A$ and all
$1$-dim irreps.

**Case 2: $\dim_q(\lambda) \geq 2$, $\lambda$ has $\geq 3$ generators in $H_A$.**

This is the regime where [pentagon ascension bound](#prop:pentagon-ascension-bound)
applies.  The R-factor residual satisfies

$$
  \lvert R(u, v) - 1 \rvert \leq C_1 \hbar_q^2
$$

for each pair $(u, v) = (\hat{V}_i^\lambda, \hat{V}_j^\lambda)$, and
the pair term ascends to the next jet level $\mathbf{A}_{n+1}$
with suppression $\hbar_q^2$.  At level $n=0$, the singleton
sum captures the contribution modulo an $O(\hbar_q^2)$ residual
per pair, which is below numerical precision for light atoms.
Hence $\rho(\lambda, A) \approx 1$ with correction $O(\hbar_q^2)$.

**Case 3: $\dim_q(\lambda) \geq 2$, $\lambda$ has $< 3$ generators in $H_A$.**

Pentagon cannot operate: only pair terms exist, not the $3$-term
products needed for the pentagon closure

$$
  \Phi_q(v) \Phi_q(u) = \Phi_q(u) \Phi_q(u v) \Phi_q(v).
$$

The pair-term contribution

$$
  z^2 \cdot \Phi_q(\hat{V}_i^\lambda \hat{V}_j^\lambda)
$$

sits un-cancelled in the mass.  Under the log form, the singleton
sum $\sum_i \ln|\Phi_q(\hat{V}_i^\lambda)|$ does NOT correctly
represent the pair contribution.  The single-vortex formula would
add the pair, giving

$$
  \mathfrak{m}^\lambda_{\mathrm{sv}}
  \;=\;
  \sum_i \Phi_q(\hat{V}_i^\lambda) + z^2 \Phi_q(\hat{V}_i^\lambda \hat{V}_j^\lambda)
  \quad \text{vs.} \quad
  \mathfrak{m}^\lambda_{\mathrm{log}} = \sum_i \ln|\Phi_q(\hat{V}_i^\lambda)|.
$$

These are different quantities; one must express $\rho$ as the
ratio that the log-form under-captures.

**Case 4: $\lambda$ does not exist in $H_A$.**

If the partition $\lambda \not\vdash A$, then $V_\lambda$ is not a
sub-irrep of $H_A$'s regular representation.  The character is
undefined; $\rho(\lambda, A) = 0$ trivially.  The transfer-chain
formula $\hat{V}^{\mathrm{std}} = z a + b$ extends numerically but
represents no Wedderburn component.  Concretely, at $A = 2$ the
standard irrep $(2, 1)$ does not exist (it requires $A = 3$), and
$\rho(\mathrm{std}, 2) = 0$ by definition.

## Quantitative form at A = 3 (sub-magic, pentagon incomplete)

For $\lambda = (2, 1) = \mathrm{std}$ at $A = 3$, we have $2$
generators and $1$ pair $(\hat{V}_0, \hat{V}_1)$.  The pair term
is

$$
  \Delta \mathfrak{m}^{\mathrm{std}}_{\mathrm{pair}}
  \;=\;
  z^2 \cdot \Phi_q(\hat{V}_0^{\mathrm{std}} \hat{V}_1^{\mathrm{std}}).
$$

Under the log form's implicit assumption that this ascends (valid
for $A \geq 4$), it's absorbed into the next jet level.  At $A = 3$
the ascension fails; instead the pair term **remains un-cancelled
AND SUBTRACTIVE with respect to the singleton sum** under the
log-to-linear conversion.  The resulting $\rho(\mathrm{std}, 3)$ is
approximately:

$$
  \rho(\mathrm{std}, 3)
  \;\approx\;
  1 - \frac{z^2 \cdot \ln|\Phi_q(\hat{V}_0 \hat{V}_1)|}
            {\ln|\Phi_q(\hat{V}_0)| + \ln|\Phi_q(\hat{V}_1)|}
$$

(schematic; the actual reduction uses BCH + pentagon residual).

Empirically: $\rho(\mathrm{std}, 3) = 0.07$ for ${}^3\mathrm{H}$,
$0.25$ for ${}^3\mathrm{He}$.  The isotope-dependence reflects
the different $\hat{V}^\lambda$ values from the proton-neutron
asymmetry.

## Quantitative form at A = 4 (doubly-magic shell enhancement)

For $\lambda = \mathrm{std} = (3, 1)$ at $A = 4$, we have $3$ generators
and $3$ pairs.  Pentagon operates.  But empirically
$\rho(\mathrm{std}, 4) \approx 1.77$ — the std contribution is
**BOOSTED** at ${}^4\mathrm{He}$.

We conjecture this is a **doubly-magic shell-closure enhancement**:
at a doubly-magic atom, the nucleons form a closed shell whose
categorical image in the std irrep has a RESONANT structure that
amplifies the per-generator contribution by a factor $> 1$.
Formally, the shell-closed configuration sits at a zero of some
determinant that the pentagon R-factor would normally suppress;
absent that suppression, the std contribution appears at full
matrix-trace value.

This is the **pentagon-enhancement hypothesis**: at doubly-magic
$(Z_c, N_c) = (2, 2)$, the normal $R = 1 + O(\hbar_q^2)$ bound
is violated because the partition $\lambda = (3, 1)$ has a
resonance with the shell structure.  The empirical $\rho = 1.77$
is the magnitude of this resonance and requires further theoretical
analysis.

## Summary table

| Case | Condition | $\rho(\lambda, A)$ | Mechanism |
|:---:|:---|:---:|:---|
| 1 | $\dim_q(\lambda) = 1$ | $1$ | Scalar commutes, pentagon trivially closed |
| 2 | $\dim_q \geq 2$, $\geq 3$ gens | $1 + O(\hbar_q^2)$ | Pentagon operational |
| 3 | $\dim_q \geq 2$, $< 3$ gens | $\lesssim 1$ | Pair un-cancelled, log over-counts |
| 4 | $\lambda \not\vdash A$ | $0$ | Irrep absent |
| special | doubly-magic $(Z_c, N_c) = (2,2)$ | $> 1$ (resonance) | Shell-closure enhancement |

## Open problems

1. Exact analytic form of $\rho(\mathrm{std}, 3)$ as a function of
   $\hat{V}_0^{\mathrm{std}}, \hat{V}_1^{\mathrm{std}}$ at $q_0$.
2. Derivation of the doubly-magic enhancement $\rho(\mathrm{std}, 4) > 1$
   from shell-closure resonance.
3. General $\rho(\lambda, A)$ for higher-dim irreps at $A \geq 5$
   (e.g., $(2, 2)$, $(2, 1, 1)$ at $A = 4, 5$).
4. Lean formalization of the pentagon-BCH expansion bounding the
   residual at $O(\hbar_q^2)$ for $\geq 3$ gens.
