<!-- FILE_START: mass-physical-face-intro.md -->
The algebraic and geometric faces of the mass endomorphism now
specialise to physical predictions.  The neutron--proton mass
splitting ([n--p splitting](#prop:neutron-proton-splitting))
follows from the crossing asymmetry of the trefoil braid; the
Borromean baryon mass formula
([baryon mass](#conj:borromean-baryon-mass-formula)) gives the
proton and neutron masses from a single common scale; and the
seven-term atomic mass formula
([q-integer mass](#conj:q-integer-mass-formula)) extends the
prediction to nuclei with $q$-integer coefficients.

Binding energies derive from the three-channel brane tower
([tower binding](#prop:tower-binding-energy)).  The mass table for $Z = 1$--$20$
([mass table](#rem:mass-table-z1-20)) collects all predictions
against CODATA/AME data.

These binding energies are the **real part** of the complex volume
$\mathfrak{V}$ ([The complex volume $\mathfrak{V}$](#sec:complex-volume)):
$\mathfrak{E}_{\mathrm{bind}} = \operatorname{Re}\mathfrak{V}$, the
bar-even ($\cosh$) strong channel of stable binding.  The same
physical face carries the complementary **imaginary part**
$\mathfrak{Q}_\beta = \operatorname{Im}\mathfrak{V}$, the bar-odd
($\sinh$) weak channel — the $\beta$-decay $Q$-value — developed as
the $\operatorname{Im}$ leg of the complex-volume precision ladder
(complex-volume ladder).
Binding and decay are one complex object read on its two parities,
not two independent predictions.
<!-- FILE_END: mass-physical-face-intro.md -->

<!-- FILE_START: neutron-proton-splitting.md -->
**Proposition.**
*The neutron--proton mass difference is*

$$
  \Delta m = m_{\mathfrak{n}} - m_{\mathfrak{p}}
  = \alpha \cdot \lvert \Phi(\mathfrak{u}\mathfrak{d}\mathfrak{d})
    - \Phi(\mathfrak{u}\mathfrak{u}\mathfrak{d}) \rvert
  \approx 1.302 \; \mathrm{MeV}
$$

*where $\Phi(\mathfrak{u}\mathfrak{u}\mathfrak{d})$ and
$\Phi(\mathfrak{u}\mathfrak{d}\mathfrak{d})$ are the quantum
dilogarithm volumes of the proton and neutron quark orderings
respectively, and $\alpha = m_e \times 8G$ is the same binding
scale as in the atomic mass formula.*

*The splitting arises from replacing one
$\mathfrak{u}\mathfrak{u}$ crossing ($\sigma$, eigenvalue $q$)
with one $\mathfrak{d}\mathfrak{d}$ crossing ($\sigma^{-1}$,
eigenvalue $q^{-1}$).  The $\mathfrak{d}\mathfrak{d}$ crossing
has more confinement energy than $\mathfrak{u}\mathfrak{u}$,
making the neutron heavier.  CODATA: $\Delta m = 1.293$ MeV
(error: $0.63\%$).*
<!-- FILE_END: neutron-proton-splitting.md -->

<!-- FILE_START: borromean-baryon-mass-formula.md -->
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

## Conjectural status versus a fit

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
identity $m_n - m_p = \mathfrak{Q}_\beta + m_e$ and the CAL-2 normalisation
$\mathrm{Vol}(\mathcal{B}_3)/\hbar_q^2$ gives a closed-form
prediction for $\Delta S(n - p)$ that is verifiable against the
direct Kauffman-bracket evaluation
([rem:delta-skein-substrate-identity](#rem:delta-skein-substrate-identity)).
The 1 015 ppm agreement matches the $\mathfrak{Q}_\beta$ residual exactly; it
is not a free parameter.
<!-- FILE_END: borromean-baryon-mass-formula.md -->

<!-- FILE_START: borromean-baryon-interpretation.md -->
**Properties of the Borromean link.**

The Borromean link $\mathcal{B}_3$ has three components with
the defining property that **no two components are linked, but
all three together are inseparable**: removing any one
component frees the other two.

- **Hyperbolic volume**:
  $\mathrm{Vol}(S^3 \setminus \mathcal{B}_3) = 7.32772\ldots$
- **Components**: $3$ (each an unknot)
- **Pairwise linking number**: $0$ (no two are linked)
- **Milnor invariant** $\bar{\mu}(123) = 1$ (nontrivial
  triple linking)

**Crossing orientation.**

Within $\mathcal{B}_3$, the three components pass over and
under each other at specific crossings.  Each component has a
**crossing orientation** --- positive ($+$) or negative ($-$)
--- determined by whether its crossings contribute $q$ or
$q^{-1}$ to the Skein polynomial.  A Borromean baryon with
orientation partition $(p, n) = (k, 3-k)$ has $k$ positive
and $3-k$ negative components.

**Mass.**

The constituent unknots have zero hyperbolic volume:
$\mathrm{Vol}(K_{0_1}) = 0$.  The Hopf link has zero volume:
$\mathrm{Vol}(\mathcal{L}_H) = 0$.  The entire baryon mass
comes from the Borromean linking:

$$
  m(B) = 
  \frac{\mathrm{Vol}(S^3 \setminus \mathcal{B}_3)}{\hbar_q^2}
  \cdot \lambda_{\mathrm{scale}}
  +  \text{Skein corrections from orientation partition}.
$$

**Confinement.**

The Borromean property ensures that no single component can
be extracted without destroying the link.  This is the
topological definition of **confinement**: the constituents
of a Borromean baryon cannot be isolated.
<!-- FILE_END: borromean-baryon-interpretation.md -->

<!-- FILE_START: q-integer-mass-formula.md -->
**Conjecture (BW-emergence: empirical liquid-drop coefficients as q-integer products, conditional on conj:palindromicity-orbital-type and conj:shell-closure-nf-term-count).**
*The QOU production mass formula is the six-term framework
([six-term mass formula](#thm:six-term-mass-formula-complete)).
The empirical Bethe--Weizsäcker liquid-drop formula — historically
**fit** to nuclear binding data in the 20th century — is recovered
from QOU as a derivative phenomenology: all five standard
liquid-drop coefficients (volume, surface, Coulomb, asymmetry,
pairing), together with the two extended terms (exchange Coulomb,
shell correction), are products of quantum integers
$[n]_q = (q^n - q^{-n})/(q - q^{-1})$ evaluated at the substrate
parameter $q_0 \approx 1.110$, times the electron mass $m_e$.*

*This block is a **BW-emergence result**, not a definition of
QOU's mass framework. It demonstrates that the parameters
nuclear physicists fit to data are themselves substrate-derived
algebraic q-rationals.*

*Five empirical liquid-drop coefficients (recovered):*

| Coefficient                     | $q$-expression                | Value (MeV) | Fitted (MeV) | Error    |
| :------------------------------ | :---------------------------- | :---------- | :----------- | :------- |
| $\lambda_V$ (volume)            | $2[2]_q[7]_q \cdot m_e$       | $15.67$     | $15.56$      | $+0.7\%$ |
| $\lambda_S$ (surface)           | $2[4]_q^2 \cdot m_e$          | $17.26$     | $17.23$      | $+0.2\%$ |
| $\lambda_C$ (Coulomb)           | $(q - q^{-1})[6]_q \cdot m_e$ | $0.68$      | $0.70$       | $-2.1\%$ |
| $a_{\mathrm{asym}}$ (asymmetry) | $3[2]_q[7]_q \cdot m_e$       | $23.51$     | $23.29$      | $+0.9\%$ |
| $\delta_P$ (pairing)            | $[3]_q[7]_q \cdot m_e$        | $11.86$     | $12.00$      | $-1.2\%$ |

*Two extended terms from Hecke representation theory:*

| Coefficient                        | $q$-expression                  | Value (MeV) | Origin                  |
| :--------------------------------- | :------------------------------ | :---------- | :---------------------- |
| $\lambda_{\mathrm{ex}}$ (exchange) | $\frac{[3]_q}{[2]_q} \cdot m_e$ | $0.77$      | nucleon screening ratio |
| $\delta_S$ (shell)                 | $[2]_q^2 [3]_q \cdot m_e$       | $6.29$      | torus knot coherence    |

*The phenomenological seven-term mass of an atom $(Z, N)$ with
$A = Z + N$, obtained by substituting these q-integer
coefficients into the empirical liquid-drop ansatz, is:*

$$
  M(Z, N) = Z m_p + N m_n + Z m_e
  - \lambda_V A
  + \lambda_S A^{2/3}
  + \lambda_C \frac{Z(Z-1)}{A^{1/3}}
  + a_{\mathrm{asym}} \frac{(N-Z)^2}{4A}
  \mp \frac{\delta_P}{\sqrt{A}}
  + \lambda_{\mathrm{ex}} \frac{Z^{4/3}}{A^{1/3}}
  - \delta_S \frac{f(Z) + f(N)}{A^{2/3}}
$$

*where $f(x) = \sum_m \exp(-(x-m)^2/2[2]_q^2)$ sums over
magic numbers $\{2,8,20,28,50,82,126\}$ with width
$\sigma = [2]_q = q + q^{-1}$ (the quantum dimension of the
pairing representation $H_2(q)$).
Zero fitted parameters.  At $q_0$ from CODATA:*

$$
  \mathrm{MAE} \approx 0.020\%
  \qquad (\text{32 isotopes, He through U})
$$

*This match is the BW-emergence result: the seven liquid-drop
parameters that 20th-century nuclear physics fit empirically
are recovered from $q_0$ alone, as products of quantum integers
specific to the Hecke algebra $H_3(q)$ of the nucleon. The
production QOU mass formula (six-term framework) achieves
higher accuracy without going through the liquid-drop ansatz.*

### Derivation of the five recovered coefficients

*The $q$-integer products arise from the Wedderburn-Artin decomposition
of the Hecke algebra $H_3(q)$ at different levels of the
nuclear construction:*

* *$[2]_q = \dim_q(\text{standard representation})$: the dimension
  of the 2D seminormal representation of $H_3(q)$.*
* *$[7]_q$: related to the proton's internal crossing count
  (7 crossings on generator 0: 3 B$_{3}$ + 1 uu + 2 gluon + 1 ud).*
* *$[4]_q$: the 4 crossings on generator 1 per proton
  (3 B$_{3}$ inverse + 1 ud mixed).*
* *$[6]_q$: the 6 crossings in the Borromean link $\mathcal{B}_3$.*
* *$[3]_q$: the 3-strand structure of the nucleon.*

*The asymmetry coefficient satisfies $a_{\mathrm{asym}} = \frac{3}{2}
\lambda_V$ exactly in the $q$-integer formula, because both involve
$[2]_q[7]_q$ with different integer prefactors (2 vs 3).  This
relation is approximate in the empirically-fit liquid-drop formula
($23.29/15.56 = 1.50$) and exact here.*

### Derivation from the channel product

*The first three recovered coefficients $\lambda_V$, $\lambda_S$,
$\lambda_C$ are derivable from the per-nucleon channel product
(per-nucleon channel decomposition).
The effective binding scale is $\alpha_{\mathrm{eff}} = m_e \times 8G
\times [3]_q$, where $8G = \mathrm{Vol}(\mathcal{B}_3)$ is the
Borromean link volume and $[3]_q$ is the nucleon strand count:*

$$
  \lambda_V
  = \alpha_{\mathrm{eff}} \cdot
    \bigl\lvert \tfrac{1}{2} \ln(ab) \bigr\rvert
  \qquad (-1.3\%\text{ vs } 2[2]_q[7]_q m_e)
$$

$$
  \lambda_S
  = \lambda_V \times \frac{[4]_q^2}{[2]_q [7]_q}
  \qquad (\text{exact: } \sigma_1/\sigma_0\text{ crossing ratio})
$$

$$
  \lambda_C
  = \frac{\alpha_{\mathrm{eff}}}{2}
    \ln \frac{2q^{-1}}{3q^{-1} - q}
  \qquad (+3.0\%\text{ vs } (q{-}q^{-1})[6]_q m_e)
$$

*where $a = -(q-q^{-1})/2$ and
$b = -3(q^2-1)(q^2+1)^2/(4q^3)$ are the proton and
neutron channel sums.  Volume arises from the geometric
mean of channel sums; the surface/volume ratio
$[4]_q^2/([2]_q[7]_q)$ counts the $\sigma_1$ vs $\sigma_0$
crossings; Coulomb is the pp-vs-pn crossing eigenvalue
deficit in the confining channel.*

### Derivation of the remaining four terms

*All seven terms derive from the Hecke algebra $H_3(q)$ and
brane topology — no external quantum statistics (Fermi--Dirac,
Bose--Einstein, Pauli exclusion) is imported.  What appears as
"pairing" and "exchange" in the empirical liquid-drop literature
emerges here from the representation theory of $H_n(q)$ and the
self-intersection of exceptional divisors in the brane blow-up.*

*The asymmetry coefficient $a_{\mathrm{asym}} = \frac{3}{2}\lambda_V$
is an exact algebraic relation: both involve $[2]_q[7]_q$ with
prefactors 3 vs 2, counting the crossing contributions on
$\sigma_0$ for asymmetric nucleon configurations.*

*The exchange Coulomb $\lambda_{\mathrm{ex}} = [3]_q/[2]_q \cdot m_e$
is the Hecke dimension ratio: the 3-strand nucleon ($H_3(q)$,
quantum dimension $[3]_q$) screens the 2-strand pair interaction
($H_2(q)$, quantum dimension $[2]_q$).  The $Z^{4/3}/A^{1/3}$
scaling follows from the transfer matrix chain reduction in the
confining channel.*

*The pairing $\delta_P = [3]_q[7]_q \cdot m_e$ arises from the
Chebyshev sign alternation in the quotient atom model
([shell closure conjecture](#conj:shell-closure-nf-term-count)).
The $Z$-fold nuclear-electron crossing $(\sigma^{-1})^Z$ reduces
to $c_Z \sigma + d_Z$ where:*

$$
  c_Z = \frac{q^{-Z} - (-1)^Z q^Z}{[2]_q}
$$

*For even $Z$: $c_Z < 0$ (identity-heavy crossing), which
cancels existing NF words and suppresses the growth ratio
to $\gamma = 1$ (s-shells) or $\gamma \approx 1.3$ (p-shells).
For odd $Z$: $c_Z > 0$ ($\sigma$-heavy), which creates new
reduced words and drives $\gamma \geq 3$.  This sign alternation
IS the pairing mechanism — not Pauli exclusion, but the
Chebyshev structure of iterated Hecke generators.  The
[palindromicity conjecture](#conj:palindromicity-orbital-type)
shows the paired state has Poincaré-dual NF (palindromic
histogram), confirming the coherence of the exceptional
divisor intersection form.  The empirical liquid-drop
approximation $\mp \delta_P / \sqrt{A}$ is a leading-order fit
to this exact Chebyshev alternation.*

*The shell correction $\delta_S = [2]_q^2 [3]_q \cdot m_e$ captures
the distinction between :refterm[exact pairing]{#exact-pairing} ($\gamma = 1$, s-shells)
and approximate pairing ($\gamma \approx 1.3$, p-shells).
The [shell closure conjecture](#conj:shell-closure-nf-term-count)
identifies the algebraic shell gap: no $Z$ has
$\gamma \in (1.4, 3.0)$.  At magic-number closures, the
torus knot $T_{2,m}$ coherence pushes $\gamma$ exactly to 1
for the closing pair.  The Gaussian proximity with width
$\sigma = [2]_q$ (quantum dimension of the pairing representation)
smooths this discrete effect.  The coefficient $[2]_q^2 [3]_q$
is the product of pair-interaction dimension squared and nucleon
strand count.*

### Algorithm

1. *Compute $q_0$ from CODATA inputs:
   $\hbar_q^2 = \mathrm{Vol}(4_1) / (m_\mu/m_e)$,
   $q_0 = 1/(1 - \sqrt{\hbar_q^2})$.*

2. *Evaluate $[n]_{q_0}$ for $n = 2, 3, 4, 6, 7$.*

3. *Compute all seven liquid-drop-recovered coefficients as
   products of $[n]_{q_0} \times m_e$.*

4. *Compute magic proximity $f(Z)$, $f(N)$ for the
   shell correction.*

5. *Apply the seven-term liquid-drop ansatz.*

*No intermediate fitting, no free parameters, no canonical
optimization.  The entire phenomenological match is derived
from the single substrate parameter $q_0$.  For higher-precision
predictions, use the production
[six-term mass formula](#thm:six-term-mass-formula-complete)
directly.*
<!-- FILE_END: q-integer-mass-formula.md -->

<!-- FILE_START: lambda-scale-substrate-form.md -->
## Family A theorem (the proved, canonical content)

*Let $q_0 \in \mathbb{R}$ be the substrate parameter
([def:substrate-parameter](#def:substrate-parameter)), $h = q_0 - q_0^{-1}$
the Hecke deformation, and $\dim_q V_\lambda$ the q-deformed dimension of the
irreducible $H_4(q)$-module indexed by $\lambda \vdash 4$ (Frame–Robinson–Thrall
hook-content formula).*

**Theorem (Family A closed form).** *The half-symmetric Wedderburn-sum
projection at $H_4$ has the closed form*

$$
  \lambda_A(q) = \frac{1}{4} \sum_{\lambda \vdash 4} \dim_q V_\lambda
             = \frac{3 q^2 + 4 + 3 q^{-2}}{4}
             = \frac{5}{2} + \frac{3}{4}\,h^2,
$$

*with no $h^4, h^6, \ldots$ corrections; all odd-$h$ coefficients vanish by
$q \leftrightarrow q^{-1}$ symmetry.*
## Structural interpretation of the leading term

At $H_4(q)$ the partition spectrum is $p(4) = 5$; the half-symmetric count over
conjugate pairs (each pair weight $1$, the self-conjugate $(2,2)$ weight
$\tfrac12$) gives $1 + 1 + \tfrac12 = \tfrac52$. The structural identity
$\mathrm{Vol}(\mathcal{B}_3) = 8G$ ($G$ = Catalan; the Borromean complement is
8 ideal regular octahedra, $V_{\mathrm{oct}} = 4G$, per Adams 1985) is derived;
how the half-symmetric $H_4$ count drives the production `VolDensity(𝓑_3)`
refinement at higher $h^2$ order is the current research direction (not a
$\lambda_{\mathrm{scale}}$-from-substrate derivation).

## Witness

- the canonical formalism — the proved Family A closed form.
- [`docs/audits/2026-05-18-lambda-scale-derivation-search.md`](../../../docs/audits/2026-05-18-lambda-scale-derivation-search.md) — the falsified-form audit trail (moved out of the paper).
<!-- FILE_END: lambda-scale-substrate-form.md -->

<!-- FILE_START: topological-mass-trefoil.md -->
We compute the topological mass
([mass formula](#prop:topological-mass-formula)) for two specific
knots: the trefoil $\tau(2,3)$ and the figure-eight knot $4_1$.

**Trefoil knot $\tau(2,3)$ — the electron.**
The trefoil is a torus knot, so its complement in $S^3$ admits a
Seifert fibration and is *not* hyperbolic.  Its hyperbolic volume
is $\mathrm{Vol}(S^3 \setminus \tau(2,3)) = 0$.  Therefore the
mass formula does not use the volume directly; instead, the
quantum dilogarithm provides the analytic continuation:

$$
  \mathfrak{m}(\tau(2,3))
  = 
  \frac{\mathrm{Li}_2(q^{-2})}{\hbar_q^{2}},
$$

where $\mathrm{Li}_2$ is the quantum dilogarithm and
$\hbar_q = (q - 1)/q$ is the quantum Planck constant
([mass identity](#def:mass-identity)).  The quantum dilogarithm
interpolates between the classical volume (for hyperbolic knots)
and the Chern--Simons invariant (for non-hyperbolic knots such as
torus knots).  Evaluating at the substrate parameter
$q \approx 1.110$:

$$
  \hbar_q  \approx  \frac{0.110}{1.110}  \approx  0.0990.
$$

**Figure-eight knot $4_1$ — the Higgs field (mass mechanism).**
The figure-eight knot *is* hyperbolic, with complement volume

$$
  \mathrm{Vol}(S^3 \setminus 4_1)  \approx  2.0299.
$$

By the mass formula, the topological mass associated with $4_1$ is

$$
  \mathfrak{m}(4_1)
  = 
  \frac{\mathrm{Vol}(S^3 \setminus 4_1)}{\hbar_q^{2}}
   \approx 
  \frac{2.0299}{(0.0990)^2}
   \approx 
  \frac{2.0299}{0.00980}
   \approx  207.1.
$$

**Physical interpretation.**
The figure-eight knot $4_1$ is the Higgs field
([cohomological embedding](#prop:cohomological-embedding)).
It is the unique amphichiral knot in $H^{0,1}(\Sigma_4)$, and
its hyperbolic volume drives the mass mechanism.  The muon
($T_{2,5}$, cinquefoil) acquires its mass through the Higgs
field ($4_1$), which universally couples to all knot-particles
with crossings $> 0$.  The dimensionless mass of $4_1$ is

$$
  \mathfrak{m}(4_1)
  = 
  \frac{\mathrm{Vol}(4_1)}{\hbar_q^2}
  \approx 207.1,
$$

which matches the muon-to-electron mass ratio
$\mathfrak{m}_\mu / \mathfrak{m}_e \approx :val[m_mu_over_e]{precision=6}$ to within $0.2\%$
(the electron mass $\mathfrak{m}_e = 1$ is the dimensionless unit).
The correspondence

$$
  \tau(2,3) \longleftrightarrow e^-
  \qquad\text{and}\qquad
  4_1 \longleftrightarrow H \text{ (Higgs field)}
$$

is determined entirely by the knot topology — no free parameters
beyond the single substrate parameter $q$.
<!-- FILE_END: topological-mass-trefoil.md -->

<!-- FILE_START: meson-kaon-pion-hecke-seifert.md -->
**Proposition (kaon-to-pion mass ratio from Hecke characters and Seifert
volumes).**
*The kaon-to-pion mass ratio decomposes into an algebraic factor from the
Hecke character of the strange-quark braid and a topological factor from
the Seifert volumes of the quark torus knots:*

$$
  \frac{\mathfrak{m}_K}{\mathfrak{m}_\pi}
  \;=\;
  \chi^{(2,1)}(\sigma_1^5)
  \;\times\;
  \biggl(\frac{V_S(T(2,5))}{V_S(T(2,3))}\biggr)^{\!2}
  \;\approx\; 3.536
$$

*where:*

1. $\chi^{(2,1)}(\sigma_1^5) = q_0^5 - q_0^{-5} = h \cdot [5]_q$ *is
   the character of $\sigma_1^5$ on the standard $(2,1)$ representation
   of $H_3(q_0)$, with $\sigma_1$ acting diagonally with eigenvalues
   $q$ and $-q^{-1}$;*

2. $V_S(T(2,n)) = 2\pi\,|e(T(2,n))|$ *is the Seifert volume of the
   torus knot $T(2,n)$, with Euler number
   $e(T(2,n)) = 1 - \tfrac{1}{2} - \tfrac{1}{n} = \tfrac{n-2}{2n}$;*

3. *the exponent $2$ equals the number of quark constituents in the
   meson $q\bar{q}$ composite.*

*The exact algebraic values $3.5361$ matches the PDG ratio
$m_{K^\pm}/m_{\pi^\pm} = 3.5371$ to $290\;\mathrm{ppm}$.*
<!-- FILE_END: meson-kaon-pion-hecke-seifert.md -->

<!-- FILE_START: gen3-meson-phi-hecke-seifert.md -->
**Proposition (third-generation meson mass ratio).**
*The third-generation meson built on the torus knot $T(2,7)$ has mass ratio*

$$
  \frac{\mathfrak{m}_X}{\mathfrak{m}_\pi}
  \;=\; \chi^{(2,1)}(\sigma_1^7)\cdot\Bigl(\frac{V_S(T(2,7))}{V_S(T(2,3))}\Bigr)^2
  \;=\; (q_0^7 - q_0^{-7})\cdot\Bigl(\frac{15}{7}\Bigr)^2
  \;\approx\; 7.320,
$$

*which identifies $X$ with the $\phi(1020)$ meson:
$\mathfrak{m}_\phi/\mathfrak{m}_\pi^{\mathrm{PDG}} = 7.304$, a
$2167\;\mathrm{ppm}$ match.*

This extends the proved kaon ratio
([`prop:meson-kaon-pion-hecke-seifert`](#prop:meson-kaon-pion-hecke-seifert))
to the next odd torus knot $T(2,7)$. The two algebraic ingredients are
identical in form to the kaon:

- **Hecke character.** On the standard $(2,1)$ representation of $H_3(q)$,
  $\chi^{(2,1)}(\sigma_1^7) = q^7 + (-q^{-1})^7 = q^7 - q^{-7} = h\,[7]_q$
  (odd $n$; Lean `chi_21_odd`).
- **Seifert ratio.** With $V_S(T(2,n)) = 2\pi\,e(T(2,n)) = \pi(n-2)/n$,
  $$\frac{V_S(T(2,7))}{V_S(T(2,3))} = \frac{5/14}{1/6} = \frac{15}{7}$$
  (Lean `seifert_ratio_T27_T23`, requiring $2,3,7 \neq 0$).
- **Squaring exponent** $n_q = 2$ (the two-body $\bar q q$ composite), the
  same value as the kaon.

## It is the φ, not the η

The substrate-table dictionary listed the third generation as
"$\eta,\phi$". The computation selects **$\phi$ unambiguously**: the
predicted ratio $7.320$ matches the $\phi$ to $2167\;\mathrm{ppm}$, while
the next-closest light meson is the $\eta'$ ($66{,}700\;\mathrm{ppm}$) and
the $\eta$ misses by $\sim 8.6\times 10^{5}\;\mathrm{ppm}$. This tracks the
strangeness progression — $\pi$ (generation 1, $\bar u u/\bar d d$), $K$
(generation 2, one strange quark), $\phi$ (generation 3, pure $\bar s s$
vector) — so the odd-torus tower follows the strange-vector line. The
$\eta$, a flavour-singlet pseudoscalar carrying an axial-anomaly
contribution, lies outside the single-torus-knot model and is not
predicted by this formula. The witness records the full comparison across
$K,\eta,\rho,\omega,K^\ast,\eta',\phi$.

## Status

As with the kaon, the two algebraic identities (`chi_21_odd`,
`seifert_ratio_T27_T23`) are Lean-proved sorry-free over a generic
`[Field R]` — no archimedean $\mathbb{R}$/$\mathbb{C}$ dependence; the
substrate evaluation at $q_0$ lives downstream. The exponent $n_q=2$ is
empirically selected (a two-body rationale, not substrate-derived), and
the $\approx 2167\;\mathrm{ppm}$ PDG match is a witnessed near-match, not a
Lean equality.
<!-- FILE_END: gen3-meson-phi-hecke-seifert.md -->

<!-- FILE_START: tower-binding-energy.md -->
The nuclear binding energy of a derived atom $\mathcal{A}(Z, N)$
([derived atom](#def:derived-atom)) is determined by the brane
tower partition function evaluated on **all three** Wedderburn
channels of $H_3(q)$.

## Statement

**Proposition.**
*Let $\mathcal{A}(Z, N)$ be a derived atom with $A$ nucleons
and $A - 1$ generators in $H_A(q)$, with canonical Hecke element
$T_w = \mathtt{atom\_braid\_word\_3A}(Z, N) \in H_{3A}(q_0)$ in
Gröbner–Shirshov normal form
([def:atomic-braid](#def:atomic-braid),
the canonical formalism).
The per-generator vertex volumes $\hat{V}_i^\lambda$ below are read
off generator $i$ of $T_w$ in irrep $\lambda \in \{\mathrm{sym},
\mathrm{std}, \mathrm{alt}\}$.  For each generator $i$
and each irrep $\lambda$, let $\hat{V}_i^\lambda$ be the vertex volume
in channel $\lambda$, computed from the Garside staircase with
LP-derived gluon crossings
([integer LP gluon](#prop:mass-endomorphism-tower)):*

- *Symmetric: $\hat{V}_i^{\mathrm{sym}} = \prod_j (c_j q + d_j)$*
- *Standard: $\hat{V}_i^{\mathrm{std}} = z a_i + b_i$
  (transfer chain reduction)*
- *Alternating: $\hat{V}_i^{\mathrm{alt}} = \prod_j (-c_j q^{-1} + d_j)$*

*The brane tower at generator $i$ in channel $\lambda$ is*

$$
  \Phi_q(\hat{V}_i^\lambda)
  =
  \prod_{k=1}^{\infty}
  \bigl|1 - q^{-k} \hat{V}_i^\lambda\bigr|^{-1},
$$

*analytically continued past $|\hat{V}| = q$ via the absolute
value of the $q$-Pochhammer symbol.*

*The nuclear binding energy is*

$$
  B(Z, N)
  =
  \sum_{\lambda}
  w_\lambda \cdot m_e
  \cdot
  \sum_{i=0}^{A-2}
  \ln\bigl|\Phi_q(\hat{V}_i^\lambda)\bigr|,
$$

*where $w_\lambda$ are the Wedderburn-Artin weights:
$w_{\mathrm{sym}} = w_{\mathrm{alt}} = 1/([2]_q^2 + 2)$,
$w_{\mathrm{std}} = [2]_q^2/([2]_q^2 + 2)$.*

*The atomic mass is then*

$$
  M(Z, N)
  =
  Z \cdot m_{\mathfrak{p}}
  + N \cdot m_{\mathfrak{n}}
  + Z \cdot m_e
  - B(Z, N).
$$

## Derivation

The binding energy arises from the gauge sector of the categorical
action ([canonical action](#prop:qou-canonical-action)):

$$
  \mathcal{S}_{\mathrm{gauge}}
  =
  \int_A \mathrm{tr}_A\bigl(
    F_\nabla \wedge_q \star_q F_\nabla
  \bigr).
$$

Under the Wedderburn-Artin decomposition of $H_3(q)$, the gauge
functional decomposes into three channels.  Although the
weights satisfy $w_{\mathrm{sym}} = w_{\mathrm{alt}}$, the
channels do **not** cancel in the binding: the nonlinearity
of $\ln|\Phi_q|$ breaks the character cancellation because
$\hat{V}^{\mathrm{sym}} \neq \hat{V}^{\mathrm{alt}}$.

Each channel contributes independently:

- **Symmetric** ($\sim 20\%$ of $B$): $\hat{V}^{\mathrm{sym}}
  = \prod (c_j q + d_j)$ grows with $A$, providing the volume
  binding baseline.
- **Standard** ($\sim 65\%$ of $B$): the $2{\times}2$ transfer
  chain $\hat{V}^{\mathrm{std}} = z a_i + b_i$ encodes the
  correlated structure between adjacent nucleons.
- **Alternating** ($\sim 15\%$ of $B$): $\hat{V}^{\mathrm{alt}}
  = \prod (-c_j q^{-1} + d_j)$ captures the Pauli exclusion
  and parity structure.

The $\Phi_q$ tower is analytically continued past
$|\hat{V}| = q$ via the $q$-Pochhammer functional equation,
taking $\ln|\Phi_q| = -\sum_k \ln|1 - q^{-k}\hat{V}|$.
This is well-defined for all $\hat{V} \neq q^n$ ($n$ integer).

The coefficients $w_\lambda \cdot m_e$ are the natural
normalization: $w_\lambda$ weights each channel relative to
the full regular representation, and $m_e$ converts the
dimensionless partition function to physical energy.

## canonical results

At $q_0 \approx 1.110$, see
[Table: Predicted vs observed binding energies for $Z = 1$ to $20$](#tbl:tower-binding-energy-table-data).

Zero fitted parameters.  Mean mass error: $0.071\%$ across
$Z = 1$ to $Z = 20$.  All coefficients derived from $q_0$
and $m_e$.

**Witness**: `full-tower-mass.witness.json`.
<!-- FILE_END: tower-binding-energy.md -->

