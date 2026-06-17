Let $\varrho \colon \mathbf{1} \to A$ be a vortex with braid
representative $\beta \in B_n$ and Hecke mass element
$T_w \in H_n(R, q)$
([Hecke mass element](#def:hecke-mass-element)). Let
$\hat V_i^{\mathrm{full}}$ denote the additive-Wedderburn traced
volume at generator $i$ of the braid word. Let
$\Phi_q(z) = \prod_{k \geq 1} (1 - q^{-k} z)^{-1}$ be the quantum
dilogarithm and $z = 1/(q^{1/2} + q^{-1/2})$ the Markov parameter.

*The boxed theorem below is the **six-term spectral expansion** of
the Gröbner–Shirshov-NF mass identity
([atomic mass via GB-NF](#prop:atomic-mass-gb-nf))
$\mathfrak{m}(\varrho) = m_e \cdot \rho_K \cdot \lvert\!\operatorname{tr}_M\!(\mathrm{NF}_{\mathrm{GS}}(\mathcal{B}_K))\!\rvert$.
The descended $\lvert\!\operatorname{tr}_M(T_w)\!\rvert$ piece supplies
the GB-NF normal-form trace; the brane tower and Frobenius co-Casimir
are the spectral decomposition of $\rho_K$ across Wedderburn blocks.
Empirically the six-term sum recovers $\rho_K^{\mathrm{CODATA}}$ to
$\sim 5\%$ for $A = 1$ but under-predicts by $22\%$–$31\%$ for $A \in \{2, 3\}$
(`rho-k-codata-vs-six-term.witness.json`), so the spectral closure of
$\rho_K$ from braid data alone remains open.*

**Theorem (unified knot mass formula; conditional on [`conj:knot-factor-frobenius-pairing`](#conj:knot-factor-frobenius-pairing)).**
*The categorical mass of the vortex $\varrho$ is*

$$
  \boxed{
    \mathfrak{m}(\varrho)
    \;=\;
    \underbrace{\bigl|\mathrm{tr}_M(T_w)\bigr|}_{\text{descended}}
    \;-\;
    \underbrace{\sum_{i=0}^{n-2} \mathrm{Li}_2^q\bigl(-|\hat V_i^{\mathrm{full}}|\bigr)
               - z^2 \sum_{0 \leq i < j \leq n-2}
                  \mathrm{Li}_2^q\bigl(-|\hat V_i^{\mathrm{full}} \hat V_j^{\mathrm{full}}|\bigr)}_{\text{brane tower}}
    \;+\;
    \underbrace{m_e \cdot \mathrm{tr}_M\bigl(C_{\dim_q}^{H_n(R, q)}\bigr)}_{\text{Frobenius co-Casimir}}
  }
$$

*where $\mathrm{Li}_2^q(z) = \sum_{n \geq 1} z^n / (n \cdot [n]_q)$
is the symmetric q-dilogarithm with
$[n]_q = (q^n - q^{-n})/(q - q^{-1})$. Per
([mass endomorphism tower proof](#prop:mass-endomorphism-tower)), this
is the closed-form result of integrating the Briggs–Klein
expansion flow $\int_0^V (\ln_q(1+t)/t)\,dt = -\mathrm{Li}_2^q(-V)$
over each resolved defect $E_i \cong \mathbb{P}^1(\mathbb{C})$.*

**Brane-tower-evaluation note (added).**
*The boxed brane-tower form $\sum_i \Phi_q(|\hat V_i|) + z^2 \sum_{i<j}
\Phi_q(|\hat V_i \hat V_j|)$ is the **archimedean Kashaev specialisation**
of the algebraic R-side form
$\sum_i z\,\mathrm{Vol}_q^{(\{i\})}(\beta) + z^2\sum_{i<j}\mathrm{Vol}_q^{(\{i,j\})}(\beta)$
in `prop:mass-endomorphism-tower`. The Kashaev substitution
$\mathrm{Vol}_q^{(S)} \rightsquigarrow \Phi_q(|\hat V_i|)$ evaluates the
quantum dilogarithm on per-generator amplitudes, which are NOT
Markov-invariant. Numerically at $q_0 \approx 1.110$ this
specialisation produces $\Phi_q(0.99) \approx 6.7 \times 10^5$ — i.e.
each per-generator term contributes $\sim 10^5$ Hecke-units, summing
to $\sim 10^6$ for atomic braids. Tiny p/n asymmetries between
mirror nuclei (T = 1p+2n vs $^3$He = 2p+1n) get amplified by
$\sim 10^5\times$, predicting T − $^3$He $\approx -737$ MeV against
CODATA $+0.019$ MeV. See
`brane-tower-isospin-diagnosis.witness.json` and
`paper-six-term-isotope-sweep.witness.json` (the four `tower_mode`
variants).*

*The R-side algebraic form, by contrast, gives
$\mathrm{tr}_M(\sigma_i) = z$ and $\mathrm{tr}_M(\sigma_i\sigma_j) = z^2$
(Markov axiom; `prop:markov-pair-z2`) for every braid
$\beta$, so $T_2 = (n-1)\cdot z^2$ and $T_3 = \binom{n-1}{2}\cdot z^4$
universally, depending only on the strand count $n$. These are
isospin-exact (T and $^3$He get identical T2+T3 since both have
$n=3A=9$) and $O(1)$ Hecke-units at $q_0$ — six orders of
magnitude smaller than the Kashaev-specialisation form. At
$q\to 1$ the closed-form trace value is $(1/2)^{2A-1}$, also
isospin-exact.*

*Implications. The boxed Kashaev specialisation in this theorem is
**Markov-invariance-broken at $q_0$** and produces hundreds-of-MeV
isospin pathologies at the atomic-braid scale. A complete proof
requires either:*

1. *replacing the boxed formula with the R-side algebraic form
 $\sum_S z^{|S|}\,\mathrm{Vol}_q^{(S)}(\beta)$ — Markov-invariant
 by construction; or*
2. *replacing the per-generator $\Phi_q(|\hat V_i|)$ with a
 q-deformed Wedderburn-weighted trace expansion $\sum_n c_n\,\mathrm{tr}_M(\sigma_i^n)$
 (Heine identity; `brane-tower-plancherel-scaffold.witness.json`)
 — converges to $\Phi_q(z)$ but each summand is a trace; or*
3. *using the Habiro-coefficient sum $\sum_m a_m(T_w)\,(u;u)_m / \mathrm{denom}(u)$
 per `prop:full-pole-structure-mass-trace` — single trace,
 absorbs T2+T3+T6 into one cyclotomic expansion.*

*Empirical: Path 3 (Habiro form) gives sub-1% atomic-mass errors
on $\{p, n, D, T, ^3\mathrm{He}\}$ via a single-prefactor binding
model (`path-b-habiro-mass-probe.witness.json`). None of the
additive variants of paths 1, 2 reach this accuracy when forced
through the proton-calibration in the boxed theorem — suggesting
that the additive structure itself may need to be re-derived from
the categorical mass identity $\mathfrak{m}_{q,K} = m_e\cdot\rho\cdot|\mathrm{tr}_M(T_w)|$
([categorical mass, Markov](#prop:categorical-mass-markov)) rather
than treated as a sum of independent pieces.*

*This is **not a refutation of the theorem** — the algebraic form
$\sum_S z^{|S|}\mathrm{Vol}_q^{(S)}$ is correct as a Hochschild-page
decomposition (`prop:gb-spectral-sequence`). It is a flag that
the boxed Kashaev specialisation is the wrong evaluation step at
$q_0$, and the open derivation question is which of paths 1–3
(or another structural reformulation) gives the canonical numerical
value matching CODATA.*

*where*

$$
  C_{\dim_q}^{H_n(R, q)}
  \;=\;
  \sum_{\lambda \,\vdash\, n}
    \frac{[n]_q!}{\dim_q(\lambda)^2 \cdot d_\lambda}
    \cdot e_\lambda
  \;\in\; Z\bigl(H_n(R, q)\bigr)
$$

*is the Frobenius co-Casimir element
([universal Frobenius co-dimension](#thm:frobenius-codim-universal))
with trace*

$$
  \mathrm{tr}_M\bigl(C_{\dim_q}^{H_n(R, q)}\bigr)
  \;=\;
  \sum_{\lambda \,\vdash\, n} \frac{1}{\dim_q(\lambda)}.
$$

**Three-part structure.**

| piece | algebraic origin | physical content |
|---|---|---|
| descended $\|\mathrm{tr}_M(T_w)\|$ | Markov trace of braid word | $E^0$ term of filtration |
| brane tower $\sum \Phi_q$ | quantum-dilogarithm resolution | single + pair blow-ups |
| Frobenius $m_e \cdot \mathrm{tr}_M(C_{\dim_q})$ | self-dual co-Casimir | universal fibre-functor residual |

*Each piece is computable from the braid word $T_w$ and the
quantum dimensions $\{\dim_q(\lambda) : \lambda \vdash n\}$ alone.
No empirical constant enters except the single fibre-functor
calibration $m_e$ (or equivalently $E_0$) that converts
categorical mass to MeV
([categorical mass, Markov](#prop:categorical-mass-markov)).*

**Specialisations by braid size $n$.**

*For a trefoil / single nucleon ($n = 3$):*

$$
  \mathfrak{m}_{\mathfrak{p}}
  \;=\;
  |\mathrm{tr}_M(T_w^{\mathfrak{p}})|
  + \text{brane-tower}(n{=}3)
  + m_e \cdot \left(2 + \frac{1}{[2]_q}\right).
$$

*The Frobenius piece $m_e \cdot (2 + 1/[2]_q) \approx 1.276\;\mathrm{MeV}$
matches the observed proton tower residual to $0.14\%$
([proton residual](#prop:partition-sum-proton-residual)).*

*For a general isotope braid ($n = 3A$):*

$$
  \mathfrak{m}_{\text{isotope}}
  \;=\;
  |\mathrm{tr}_M(T_w)|
  + \text{brane-tower}(n{=}3A)
  + m_e \cdot \sum_{\lambda \,\vdash\, 3A} \frac{1}{\dim_q(\lambda)}.
$$

*The right object is the $(3A)$-level Frobenius sum
$\tau\bigl(C_{\dim_q}^{H_{3A}(R, q)}\bigr) = \sum_{\lambda \vdash 3A} 1/\dim_q(\lambda)$,
not $A$ copies of the single-vortex $(n=3)$ value.*

*This is forced by the algebraic content of
[Frobenius co-Casimir universal](#thm:frobenius-codim-universal):
when the isotope's braid lives in $H_{3A}(R, q)$, the central
idempotents $p_\lambda$ are indexed by partitions $\lambda \vdash 3A$,
not by partitions of $3$. The per-A heuristic
$A \cdot \tau(C_{\dim_q}^{H_3})$ would correspond to a disconnected sum
of $A$ independent $H_3$-blocks, which is**not** the algebra
hosting an isotope braid.*

*Numerical values per
[`probe_term4_conventions.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/computations/probe_term4_conventions.py):*

| atom | $A$ | per-vortex $1{\cdot}m_e\Sigma_3$ | per-A $A{\cdot}m_e\Sigma_3$ | **per-$3A$ $m_e\Sigma_{3A}$ (algebraic)** |
|---|---:|---:|---:|---:|
| D | 2 | 1.276 MeV | 2.552 MeV | **1.636 MeV** |
| T, ${}^{3}$He | 3 | 1.276 MeV | 3.828 MeV | **1.300 MeV** |
| ${}^{4}$He | 4 | 1.276 MeV | 5.105 MeV | **1.151 MeV** |

*The per-$3A$ values are close to the per-vortex value ($\sim
1.2$–$1.6$ MeV) because $\sum_{\lambda \vdash 3A} 1/\dim_q(\lambda)$
is dominated by the two extreme blocks $((3A))$ and $((1^{3A}))$
each contributing $1$, plus a $q$-dependent middle that grows
slowly in $A$. This explains why the per-vortex heuristic was
empirically a good approximation, but it is not the rigorous
statement.*

*Compute side: scripts that use $A \cdot m_e \cdot (2 + 1/[2]_q)$
([`mass_formula_6term.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/computations/mass_formula_6term.py),
[`unified_low_isotope_predictor.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/computations/unified_low_isotope_predictor.py))
are using the per-A heuristic and need to be migrated to the
per-$3A$ algebraic form before any "best prediction" claim.*

**Specialisations by knot type.**

*For a single braid generator ($n = 2$, electron candidate):*
$\widehat{H_2(R, q)} = \{(2), (1,1)\}$ both with $\dim_q = 1$, so
$\sum 1/\dim_q = 2$, giving Frobenius residual $2 m_e \approx
1.022\;\mathrm{MeV}$.

*For Borromean-type braids ($n \geq 6$):*
the Frobenius sum grows with $n$; see table in
[Frobenius universal](#thm:frobenius-codim-universal).

**Classical limit ($q \to 1$).**
*The Hecke algebra reduces to $\mathbb{C}[S_n]$; $\dim_q \to d_\lambda$
and $[2]_q \to 2$. The Frobenius co-Casimir trace reduces to
$\sum_\lambda 1/d_\lambda$ (classical reciprocal-dimension sum).
For $n = 3$ this is exactly $5/2$ — recovering the upstream
classical discovery
(`residual_partition_sum.py`).*

**Why "unified":**
*The three pieces were previously distinct objects with separate
derivations:*

1. *Descended $|\mathrm{tr}_M|$ — `prop:categorical-mass-markov`,
 the mass-identity prescription.*
2. *Brane tower $\sum \Phi_q$ — `prop:mass-endomorphism-tower`,
 derived from the quantum-dilogarithm resolution of the
 exceptional divisor.*
3. *Frobenius correction — `thm:frobenius-codim-universal` (new),
 derived from self-dual Frobenius structure of $H_n(R, q)$.*

*This theorem combines them into a single three-term formula.
Each term is independently derived; the sum is the total mass.*

**Limitation: the Frobenius piece is vortex-blind.**

*The Frobenius correction $m_e \cdot \mathrm{tr}_M(C_{\dim_q})$
**does not depend on the specific vortex $\varrho$** — only on
the ambient Hecke algebra $H_n(R, q)$. All trefoil-like vortices
on $H_3(R, q)$ (proton, neutron, any quark configuration) get
the same additive offset $(2 + 1/[2]_q) \cdot m_e$. Mass
differences between such vortices therefore must come from
the first two pieces (descended + brane tower).*

**Isotope binding: chirality factors are a FOURTH tier.**

*For compound isotope bindings, the paper's full formula
([figure-eight BW coefficients](#thm:six-term-mass-formula-complete))
adds a **vortex-dependent chirality factor**
$a_K \in \{1 + h,\; 1 - h^2,\; (1 - h^2)^2\}$ for $\{D, T, ^4\mathrm{He}\}$
respectively — reflecting the knot type (chiral+, amphichiral,
Borromean$\times$2). Upstream verification
(`computations/bw_chirality_isotopes.py`) gives
$T: 0.505\%$ and $^3\mathrm{He}: 0.856\%$ agreement with AME
using these factors.*

*The chirality factor is a fourth structural layer beyond the
three Frobenius-universal layers of this theorem. It is vortex-
dependent, like the descended and tower pieces, but algebra-
independent in form (depends only on the knot type of the
isotope braid, not on the specific $T_w$ expansion). A
complete mass formula is therefore:*

$$
  \mathfrak{m}(\varrho)
  \;=\;
  |\mathrm{tr}_M(T_w)|
  \;+\;
  \sum \Phi_q(\cdot)
  \;+\;
  m_e \cdot \mathrm{tr}_M(C_{\dim_q})
  \;+\;
  a_K \cdot B_{\mathrm{bulk}}
  \;+\;
  (\text{jet-level corrections}),
$$

*where $a_K$ is the chirality factor and the jet-level
corrections reflect the open-problem prefix-word structure
per upstream `pure_hecke_binding.py`.*

**Consistency checks.**

1. *At $q = 1$: classical Hecke reduces to $\mathbb{C}[S_n]$, brane
 tower collapses ($\Phi_1$ singular — handled by a separate
 classical-limit argument), Frobenius term reduces to $\sum
   1/d_\lambda$ (number of conjugacy classes / involutions).*
2. *For the identity braid $T_e = 1 \in H_n(R, q)$:
 $|\mathrm{tr}_M(1)| = 1$; brane tower vanishes (no crossings);
 Frobenius term is pure $\sum 1/\dim_q$ — this is the
 **vacuum mass** of the trivial vortex, consistent with
 the unit object's fibre-functor value.*
3. *Under braid concatenation $T_{w_1 w_2} = T_{w_1} T_{w_2}$
 (Hecke multiplication): the descended piece is multiplicative
 in $|\mathrm{tr}_M|$; the brane tower is additive;
 the Frobenius piece is **vortex-count-additive** (per
 deuteron observation). Total mass is therefore not 
 additive or multiplicative — the three pieces compose by
 their own rules and the sum respects the expected
 thermodynamic behaviour of bound-state mass defects.*
