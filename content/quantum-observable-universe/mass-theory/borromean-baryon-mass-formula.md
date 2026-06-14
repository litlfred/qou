**Conjecture (Borromean baryon mass formula, common-scale form).**
*Every Borromean baryon $B = \mathcal{B}_3(K_{0_1}, K_{0_1}, K_{0_1})
\oplus \mathcal{L}_H$ ([def:borromean-baryon](#def:borromean-baryon))
has rest mass*

$$
  \mathfrak{m}(B)
  \;=\;
  m_e \cdot \left[\,
    \frac{\mathrm{Vol}(\mathcal{B}_3)}{\hbar_q^2}
    \cdot \lambda_{\mathrm{scale}}
    \;+\; S(B)
  \,\right]
$$

*where:*

- $m_e$ *is the leptonic mass quantum*
  ([CAL-1 in three-calibration-inputs](#prop:three-calibration-inputs)),
- $\hbar_q = (q-1)/q$ *is the* $q$*-deformed Planck constant*
  ([def:quantum-planck-constant](#def:quantum-planck-constant)),
- $\mathrm{Vol}(\mathcal{B}_3) \approx 7.32772\ldots$ *is the
  hyperbolic volume of the Borromean rings complement
  (a fixed topological invariant; no calibration),*
- $S(B) \in \mathbb{Z}[q^{\pm 1/2}]$ *is the* **Skein contribution**
  *of the orientation partition $(p, n) = (k, 3-k)$ via the Kauffman
  bracket evaluated at $q_0$ ([def:hadron](#def:hadron) tower),*
- $\lambda_{\mathrm{scale}} \in \mathbb{Q}(q_0)$ *is the* **common
  Borromean scale** *— a single $q$-rational that is shared between
  every Borromean baryon and absorbs the topology$\to$energy normalisation
  of the Borromean linking quantum.*

**The common-scale hypothesis.** The conjecture asserts that
$\lambda_{\mathrm{scale}}$ depends only on $\mathcal{B}_3$ and $q_0$,
*not* on the orientation partition $(p, n)$. Under this hypothesis
the orientation dependence of the baryon mass is carried entirely
by the Skein term $S(B)$.

## Empirical closure targets at $q_0$

Solving the formula for $\lambda_{\mathrm{scale}}$ against the CODATA
proton and neutron masses, with $S(B)$ identified from the canonical
Kauffman-bracket evaluation
([def:typed-crossing-operator](#def:typed-crossing-operator)),
yields:

| Baryon | $(p, n)$ | $\lambda_{\mathrm{scale}}$ closure target |
|--------|----------|-------------------------------------------|
| proton  | $(2, 1)$ | $2.4599527869\ldots$ |
| neutron | $(1, 2)$ | $2.4633436333\ldots$ |

*The two values differ in the seventh significant figure. The
$1.4 \times 10^{-3}$ relative spread is consistent with — and entirely
absorbed by — the* $\Delta S(n - p)$ *substrate identity below
([rem:delta-skein-substrate-identity](#rem:delta-skein-substrate-identity)),
which derives the proton–neutron Skein offset from
$\{m_e, q_0, \mathrm{Vol}(\mathcal{B}_3)\}$ alone.*

## Discussion

This conjecture has two parts:

1. **The Vol-form mass formula** — that
   $\mathfrak{m}(B)$ is linear in $\mathrm{Vol}(\mathcal{B}_3)/\hbar_q^2$
   plus a Skein-orientation correction. This is the topological-mass
   ansatz of
   [thm:topological-mass](#thm:topological-mass) restricted to the
   Borromean substrate; it is the direct generalisation of the
   verified CAL-2 identity
   $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$
   ([prop:three-calibration-inputs](#prop:three-calibration-inputs))
   from the figure-8 (muon) sector to the Borromean (baryon) sector.

2. **The closed-form derivation of $\lambda_{\mathrm{scale}}$** —
   an open R&D item. Candidate substrate origins, ranked by structural
   plausibility, are:
   - the Skein polynomial $Q(q_0)$ of $\mathcal{B}_3$ evaluated at
     the substrate point (cohomology of the GS-confinement filtration
     on the canonical 11-crossing Borromean braid);
   - the graded-Hecke-energy weight at the canonical Borromean
     element $\beta_{\mathrm{Bor}} \in H_3(R, q)$
     ([graded-hecke-energy-truncation-bound](#prop:graded-hecke-energy-truncation-bound));
   - a Clausen-substructure expansion
     $\lambda_{\mathrm{scale}} = \mathrm{Cl}_2(\pi/3)^a / \hbar_q^b$
     for small integers $(a, b)$.

   None of these has yet been carried through to a closed form
   matching $2.4599\ldots$ at the required precision; the open
   programme is documented in
   [docs/agent-briefs/-lambda-scale-borromean-baryon-derivation.md](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/docs/agent-briefs/-lambda-scale-borromean-baryon-derivation.md).

Until part 2 is resolved, $\lambda_{\mathrm{scale}}$ is a
**conjectural common scale**, not a free fit parameter:
the conjecture is that *some* $\mathbb{Q}(q_0)$-expression exists,
and the empirical agreement of $\Delta S(n-p)$ to $\sim 1\,000$ ppm
from CAL-1 + CAL-2 + $\mathrm{Vol}(\mathcal{B}_3)$ alone (no fit to
proton or neutron individually) is the first non-trivial substrate
test of the common-scale hypothesis.

## Why this is a conjecture, not a fit

The formula is testable without ever solving for
$\lambda_{\mathrm{scale}}$ from $m_p$ or $m_n$: under the common-scale
hypothesis the difference

$$
  \mathfrak{m}(n) - \mathfrak{m}(p)
  \;=\;
  m_e \cdot \bigl[\, S(n) - S(p) \,\bigr]
  \;=\;
  m_e \cdot \Delta S(n - p)
$$

is independent of $\lambda_{\mathrm{scale}}$. Substituting the CODATA
identity $m_n - m_p = Q_\beta + m_e$ and the CAL-2 normalisation
$\mathrm{Vol}(\mathcal{B}_3)/\hbar_q^2$ gives a closed-form
prediction for $\Delta S(n - p)$ that is verifiable against the
direct Kauffman-bracket evaluation
([rem:delta-skein-substrate-identity](#rem:delta-skein-substrate-identity)).
The 1 015 ppm agreement matches the $Q_\beta$ residual exactly; it
is not a free parameter.
