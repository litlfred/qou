The categorical mass at a single brane level is the Markov trace
([categorical mass as Markov trace](#prop:categorical-mass-markov)).
The full topological mass includes a tower sum over all brane
levels
([topological decomposition](#thm:topological-mass)), which
evaluates to $\mathrm{Vol}(K)/\hbar_q^2$ in the archimedean
realisation.

The **Hecke mass element**
$\Phi_{\mathrm{mass}}(\beta) \in H_n(q)$
([Hecke mass element](#def:hecke-mass-element)) is categorically
defined: it is the fibre functor image of the mass integrand
$(\int_A \otimes \mathrm{id}) \circ \Delta \circ \varrho$, and
its Markov trace gives the full categorical mass
([mass via Markov trace](#prop:hecke-mass-trace)).  The **open
problem** is computing $\Phi_{\mathrm{mass}}(\beta)$ explicitly
— expressing its NF decomposition in the basis
$\{\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-\}$ for specific
braid words.

## Statement

**Conjecture (explicit mass endomorphism).**
*The Hecke mass element $\Phi_{\mathrm{mass}}(\beta)$
([Hecke mass element](#def:hecke-mass-element)) admits a
closed-form NF decomposition in $H_n(q)$ expressible in terms
of the braid word $\beta$, the substrate parameter $q$, and
the quantum dilogarithm $\Phi_q$.  Specifically, the
transient component satisfies:*

$$
  \mathrm{tr}_M\!\bigl(\Phi^{\mathrm{trans}}(\beta)\bigr)
  =
  \sum_{i=1}^{N} \Phi_q(z_i)
  =
  \frac{\mathrm{Vol}(K_\beta)}{\hbar_q^2}
  -
  \bigl|\mathrm{tr}_M\!\bigl(\rho(\beta)\bigr)\bigr|,
$$

*where the spectral coordinates $z_i$ of the blow-up centres
are determined by the braid word and the Briggs--Klein chart.*

## What is known

**Step 1 (Categorical → Markov, proved).**
$\mathfrak{m}(\varrho)|_{\text{single level}} = |\mathrm{tr}_M(\rho(\beta))|$.
This is
[categorical mass as Markov trace](#prop:categorical-mass-markov):
the Nakayama automorphism is $S^2 = \mathrm{id}$, so the
mass reduces to the Markov trace of the braid word.

**Step 2 (Tower sum → Vol, archimedean).**
$\mathfrak{m}(\varrho)|_{\text{full tower}} = \mathrm{Vol}(K)/\hbar_q^2$.
This is the
[archimedean mass formula](#prop:topological-mass-formula):
the descended trace gives $\mathrm{Vol}(K)$, each transient
trace gives $\Phi_q(z_i)$, and they sum to
$\mathrm{Vol}(K)/\hbar_q^2$.

**Step 3 (Markov trace ≠ Vol, the gap).**
The Jones--Markov trace $\mathrm{tr}_M(\rho(\beta))$ is
the Jones polynomial $J(K; q)$ — a Laurent polynomial
in $q^{1/2}$.  The hyperbolic volume $\mathrm{Vol}(K)$ is a
transcendental number.  These are **different knot
invariants**: $J(\text{trefoil}; q) = -q^{-4} + q^{-3} + q^{-1}$
while $\mathrm{Vol}(\text{trefoil}) = 0$.

The bridge between them is the **Volume Conjecture**
\cite{kashaev1997, murakami-murakami2001}:

$$
  \lim_{N \to \infty}
  \frac{2\pi}{N}
  \log |J_N(K; e^{2\pi i/N})|
  =
  \mathrm{Vol}(S^3 \setminus K),
$$

where $J_N$ is the $N$-colored Jones polynomial.  This limit
involves:
- evaluating at roots of unity ($q = e^{2\pi i/N}$, not
  generic $q$),
- the $N$-dimensional representation (not the fundamental),
- an asymptotic limit ($N \to \infty$).

Each step moves away from the Hecke algebra at generic $q$.

## What $\Phi_{\mathrm{mass}}$ would need to encode

The brane tower $\{A_n\}$ provides the categorical version of
$N \to \infty$: each brane level $n$ contributes a transient
trace $\Phi_q(z_n)$, and the full mass sums over all levels.
A mass endomorphism $\Phi_{\mathrm{mass}}$ would need to
encode this sum as a **single** element of $H_n(q)$.

The quantum dilogarithm $\Phi_q(z) = \prod_{k=1}^{\infty}(1 - q^{-k}z)^{-1}$
is an **infinite product** — it is not a finite element of
$H_n(q)$ for any $n$.  However, the brane tower truncates at
finite $N$ (determined by the knot crossing number), so the
relevant sum is finite.  The question is whether this finite
sum has a closed-form expression in $H_n(q)$.

## Computational verification

Three single-level approaches were tested for the proton
($uud$) and neutron ($udd$) Borromean braids:

| Method | Proton | Neutron | Ratio $n/p$ | CODATA |
|:---|:---:|:---:|:---:|:---:|
| $\lvert\mathrm{tr}_M(\beta)\rvert$ | $1.165$ | $0.911$ | $0.782$ | $1.001$ |
| $\Phi_q/\hbar_q^2$ | $-89.8$ | $-125.2$ | $1.395$ | $1.001$ |
| GS energy | $0.852$ | $1.184$ | $1.390$ | $1.001$ |

**None of these single-level computations reproduce the
neutron-to-proton mass ratio.**  The quantum dilogarithm
$\Phi_q = \sum \log \lvert\hat{V}_i\rvert$ gives the correct
**binding energy differences** between nuclei (Q-values at
Level 0), but not single-nucleon absolute masses.

The proton mass 938.272 MeV in the paper comes from the
pair Skein formula $m_p = \mathcal{S}_{uu} + 2\mathcal{S}_{ud}$,
which requires the **dressed quark mass** $\mu_\mathfrak{u} \approx 311$ MeV
as input — calibrated from CODATA $m_p$.  The structural
content (pair formula, splitting isolation, binding energy)
is categorically derived; the absolute scale is calibrated.

## Candidate structures

**(a) Figure-eight $4_1$ as Higgs coupling.**
The figure-eight knot $4_1 = (\sigma_0\sigma_1^{-1})^2$ is the
gluon unit squared.  Its NF is
$h^2\gamma + h^3\sigma_0 - h\sigma_1 - h^2 L_+ + L_-$ with
zero electron content.  As a mass operator, the pairing
$\mathrm{tr}_M(e^- \cdot 4_1) = hz^2 + z = \mathrm{tr}_M(e^-)$
does not produce the correct mass ratios.  The figure-eight
encodes the **mass mechanism** (amphichiral, hyperbolic,
$\mathrm{Vol} = 2.0299$) but acts trivially on the trefoil
in $H_3(q)$.

**(b) Tower-accumulated operator.**
The mass endomorphism may be the product
$\Phi_{\mathrm{mass}} = \prod_{n=0}^{N} (1 + \Phi_q(z_n))$
of Hecke elements at each brane level, composed via the
comultiplication.  This would be an element of $H_n(q)$
growing with $N$ — a categorically defined object, but not a
fixed element independent of the knot.

**(c) Spectral decomposition via RJ weights.**
The Rosso--Jones inner product
([RJ canonical inner product](#prop:rj-canonical-inner-product))
decomposes the Markov trace over irreps:
$\mathrm{tr}_M = \sum_\lambda d_\lambda(q) \cdot \mathrm{tr}_\lambda$.
A mass endomorphism could be a **reweighting** of the irreps:
$\Phi_{\mathrm{mass}} = \sum_\lambda w_\lambda(q) \cdot e_\lambda$,
where $w_\lambda$ encodes the volume information.  The Volume
Conjecture would then be the statement that the weights
$w_\lambda$ grow exponentially with $\lambda$, recovering
$\mathrm{Vol}(K)$ in the limit.

## Relation to knot operator selection

The multi-channel decomposition
([knot operator selection](#prop:knot-operator-selection))
showed that interactions decompose over irreps of $H_n(q)$
weighted by quantum dimensions.  The mass endomorphism
conjecture is the statement that **mass is a specific
reweighting of the same decomposition** — the weights that
produce $\mathrm{Vol}(K)$ instead of $J(K; q)$.

If the conjecture holds, then:
- The **operator selection** framework (Frobenius dual,
  Gram matrix, demand/supply) applies to mass, with
  $\Phi_{\mathrm{mass}}$ replacing the identity.
- The **Higgs field** is the dominant contribution to
  $\Phi_{\mathrm{mass}}$ for leptons (it supplies the
  volume that the trefoil lacks).
- The **graviton** would be the residual of
  $\Phi_{\mathrm{mass}}$ after subtracting the Higgs
  contribution.
