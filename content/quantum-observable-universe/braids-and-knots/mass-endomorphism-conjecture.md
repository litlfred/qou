In the unified six-term formula
([unified knot mass](#thm:knot-mass-formula-unified)),
$|\mathrm{tr}_M(\rho(\beta))|$ is **Term 1** ($E_\infty^{0,*}$,
vortex-specific) and the brane tower $\sum \Phi_q(z_i)$ supplies
**Terms 2–3** ($E_\infty^{1,*}$ and $E_\infty^{2,*}$).  In the
archimedean realisation these three terms together evaluate to
$\mathrm{Vol}(K)/\hbar_q^2$
([topological decomposition](#thm:topological-mass)).
Terms 4–6 (Frobenius co-Casimir, chirality, jet prefix) are
separate structural pieces handled elsewhere; this conjecture
concerns only the tower piece.

The **Hecke mass element**
$\Phi_{\mathrm{mass}}(\beta) \in H_n(R, q)$
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
closed-form NF decomposition in $H_n(R, q)$ expressible in terms
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

## Tower convergence

The electron mass $\mathrm{Li}_2(q^{-2})/\hbar_q^2$ can be
decomposed as a sum over brane levels
$n = 1, 2, \ldots$, with level $n$ contributing
$q^{-2n}/n^2$ to $\mathrm{Li}_2$:

| Levels | Fraction of $\mathrm{Li}_2(q^{-2})$ |
|:---:|:---:|
| $N = 1$ | $73.9\%$ |
| $N = 3$ | $94.3\%$ |
| $N = 10$ | $99.75\%$ |
| $N = 20$ | $99.99\%$ |

The tower effectively converges in $\sim 20$ terms,
consistent with $t_P = 1/\hbar_q \approx 10$ Reeb
operations per Planck time.  The first brane level alone
provides $74\%$ of the electron mass; the remaining
$26\%$ comes from higher jet prolongations.

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

**Step 3 (Markov trace $\neq$ Vol, the gap).**
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

The **Habiro ring** ([Habiro ring](#def:habiro-ring)) partially
closes this gap: the colored Jones polynomials for all $N$
coexist as a single element of $\widehat{\mathbb{Z}[q]}$.
The algebraic quantum volume
([algebraic quantum volume](#def:algebraic-quantum-volume))
$\mathrm{Vol}_q(\beta) = \prod \hat{V}_i$ embeds into
$\widehat{\mathbb{Z}[q^{1/2}]}$, and its evaluations at
roots of unity collectively encode the hyperbolic volume via
the Volume Conjecture.  The mass at $q_0$ is a **different**
specialisation of the same Habiro element — not through roots
of unity, but through direct evaluation at the substrate
parameter.

## What $\Phi_{\mathrm{mass}}$ would need to encode

The brane tower $\{A_n\}$ provides the categorical version of
$N \to \infty$: each brane level $n$ contributes a transient
trace $\Phi_q(z_n)$, and the full mass sums over all levels.
A mass endomorphism $\Phi_{\mathrm{mass}}$ would need to
encode this sum as a **single** element of $H_n(R, q)$.

The quantum dilogarithm $\Phi_q(z) = \prod_{k=1}^{\infty}(1 - q^{-k}z)^{-1}$
is an **infinite product** — it is not a finite element of
$H_n(R, q)$ for any $n$.  However, the brane tower truncates at
finite $N$ (determined by the knot crossing number), so the
relevant sum is finite.  The question is whether this finite
sum has a closed-form expression in $H_n(R, q)$.

**Habiro-ring home for the tower limit.**  *Even when the brane
tower does not truncate finitely, the partial sums*

$$
  \Phi_{\mathrm{mass}}^{(N)}(\beta)
  \;:=\;
  \sum_{i=1}^{N} \Phi_q(z_i)
$$

*form a Cauchy sequence in the $(q;q)_n$-adic topology on
$\widehat{\mathbb{Z}[q]}$ ([Habiro ring](#def:habiro-ring)): each
factor $\Phi_q(z_i)$ has cyclotomic-denominator structure (the
$[k]_q$ in $\Phi_q$ are cyclotomic), so successive partial sums
agree modulo $((q;q)_n)$ for $n$ growing with $N$. Therefore the
limit*

$$
  \Phi_{\mathrm{mass}}^{(\infty)}(\beta)
  \;\in\;\widehat{\mathbb{Z}[q]}
$$

*exists as an element of the Habiro completion — well-defined
purely algebraically, with no analytic convergence required. This
limit object **is** the motive of the mass:* it carries the
combinatorial data needed to map to $\mathrm{Vol}(K)/\hbar_q^2$
**only** when the archimedean realization
[$\rho_\infty$](#def:archimedean-realization-functor) of
the [motivic substrate](#def:motivic-substrate) is applied at
$q_0 \in \mathbb{R}$. The non-archimedean realizations
$\{\rho_p\}$ recover the colored-Jones data via cyclotomic
projection $\widehat{\mathbb{Z}[q]} \to \mathbb{Z}[q]/\Phi_N(q)$
without any complex-analytic limit.

The conjecture's "closed-form expression in $H_n(R, q)$" is a
question at the level of the **finite-rank Hecke algebra**; the
$N \to \infty$ tower limit is then a question at the level of the
**Habiro completion** $\widehat{\mathbb{Z}[q]}$. Both senses are
algebraic.

**Two distinct convergence problems (clarification, 2026-04-28f).**
*The Habiro completion above resolves the* $N \to \infty$ *tower-limit
problem (number of summands) in the* $((q;q)_n)$*-adic topology on* $q$.
*This is well-defined and at* $q_0 \approx 1.11$ *(real,* $|q| > 1$,
*outside the natural boundary* $S^1$*) the Habiro evaluation
agrees with the analytic infinite product.*

*A separate convergence problem affects the brane tower numerically:
for the per-generator volumes* $|\hat{V}_i|$ *of low isotopes, all values
sit at* $|\hat{V}_i| \in [0.85, 1.0]$ *— at the boundary of the
* $z$*-radius of convergence of* $\Phi_q(z) = \prod (1 - q^{-k} z)^{-1}$.
*Numerically* $\Phi_q(0.989) \approx 6.7 \times 10^5$ *and* $\Phi_q(1) \approx 9 \times 10^5$.
*The Habiro framework above is about completion in* $q$*, not in* $z$;
*it does not regularize the* $|\hat{V}|\approx 1$ *behaviour.*

*Two partial mitigations are documented but neither universally
closes the gap:*

1. *Yekutieli finite-slice truncation
   ([atom-knot-mass-derivation §Architecture](#prop:atom-knot-mass-derivation)).
   The non-abelian Stokes theorem at finite slice depth gives a
   finite multiplicative integral; per-atom max slice depth equals
   the GB filtration* $\mathrm{max\_grade}$ *recorded in
   `joint-tower-sdp-h6-h9.witness.json`. Truncating the* $\Phi_q$
   *product at this depth reduces* $\Phi_q(0.989)$ *from* $6.7 \times 10^5$
   *to* $46.5$ *for* $\mathrm{max\_grade}=2$ *(D's filtration depth).*
   *Empirical test in*
   [`probe_phiq_yekutieli_truncation.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/probe_phiq_yekutieli_truncation.py):
   *the free-minus-atom subtraction* $E_0 \cdot (\mathrm{tower}^{\mathrm{free}}_{\leq k_{\max}} - \mathrm{tower}^{\mathrm{atom}}_{\leq k_{\max}})$
   *gives* $B(D) \approx +1.74 \mathrm{MeV}$ *(error* $-22\%$*) but
   fails for* $T$ *(deeper filtration* $k_{\max}=9$ *gives* $B(T) \approx 1449 \mathrm{MeV}$, *grossly off).*

2. *A "z-Habiro" completion — analogous to the* $q$*-Habiro one
   above but in the* $z$*-variable — is conjecturally what would
   regularize* $\Phi_q$ *at* $|z|=1$. *The construction would replace
   the analytic product with a cyclotomic series in* $z$ *whose
   evaluation at any specific* $|z|<\infty$ *is finite. This
   construction is OPEN; it would require identifying a cyclotomic
   denominator structure in* $z$ *parallel to the* $(q; q)_n$ *ideal
   in* $q$.*

*Until either (1) extended uniformly across atoms (which requires
understanding why Yekutieli depth differs by* $A$*) or (2) the* $z$*-
Habiro completion is constructed, the brane tower contribution to the
multi-term mass formula is not computable in closed form for*
$|\hat{V}|\approx 1$. *Empirically the descended Markov trace plus
Frobenius co-Casimir alone reproduces the binding within* $\sim 30\%$
*for low isotopes; closing the residual to AME requires the brane
tower in some regularized form.*

## Descended vs transient mass (computed)

The Hecke mass element splits as
$\Phi_{\mathrm{mass}} = \Phi^{\mathrm{desc}} + \Phi^{\mathrm{trans}}$
([Hecke mass element](#def:hecke-mass-element)).  At $q_0$,
the transient (tower) component dominates overwhelmingly:

| Particle | $\mathrm{tr}_M(\Phi^{\mathrm{desc}})$ | $\mathrm{tr}_M(\Phi^{\mathrm{trans}})$ | Ratio trans/desc |
|:---:|:---:|:---:|:---:|
| $e^-$ (trefoil) | $0.551$ | $111.86$ | $203\times$ |
| $4_1$ (figure-eight) | $0.182$ | $207.40$ | $1137\times$ |

The single-level (descended) Markov trace contributes **less
than $0.5\%$** of the total mass.  The mass is almost entirely
a brane tower effect — the accumulated quantum dilogarithm
across exceptional divisors.

## Computational verification (single-level)

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
in $H_3(R, q)$.

**(b) Tower-accumulated operator.**
The mass endomorphism may be the product
$\Phi_{\mathrm{mass}} = \prod_{n=0}^{N} (1 + \Phi_q(z_n))$
of Hecke elements at each brane level, composed via the
comultiplication.  This would be an element of $H_n(R, q)$
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
showed that interactions decompose over irreps of $H_n(R, q)$
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
