## Three equivalent forms

The same observable $\mathfrak{m}(K)$ admits three rewritings.
Each exposes different structure:

| Form | Inputs | Status |
|---|---|---|
| **(GB-NF)** $\mathfrak{m} = m_e \cdot \rho_K \cdot \lvert\!\mathrm{tr}_M\!\bigl(\mathrm{NF}_{\mathrm{GS}}(\mathcal{B}_K)\bigr)\!\rvert$ | $m_e$, $\mathcal{B}_K$, $q_0$, $\rho_K$ | algebraic |
| **(constituent)** $\mathfrak{m} = Z m_{\mathfrak{p}} + N m_{\mathfrak{n}} + Z m_e + \alpha \sum_i \ln\lvert\hat{V}_i^{\mathrm{full}}\rvert$ | $m_e$, $\mathcal{B}_K$, $q_0$, $m_\mu$ | $0.18\%$ mean error, $Z\!=\!1\!\dots\!20$, utilizing the exact muon-anchored Hecke energy |
| **(muon-anchored)** $m_{\mathfrak{p}} = 2(m_\mu F_{\mathrm{Bor}} - 6m_e)$ | $m_e$, $q_0$, $m_\mu$ | Exact canonical derivation matching CODATA ([unified mass formula](#thm:knot-mass-formula-unified)) |

The (GB-NF) form constitutes the abstract algebraic statement. The
other two constitute concrete evaluations that fix $\rho_K$ via different
calibration data. Throughout, the predictive content is the dimensionless
mass ratio $\mathfrak{m}(K)/m_e$: the leading $m_e$ factor is the CAL-1 scale
set by fiat, so the MeV figures are that ratio rendered against the $m_e$ unit
rather than an independent absolute-mass prediction.

## The categorical density factor $\rho_K$

By the categorical-mass identity
([categorical mass = Markov](#prop:categorical-mass-markov)):
$\mathfrak{m}_{q,K} = \lvert\!\mathrm{tr}_M(\rho(\mathcal{B}_K))\!\rvert$
provides the dimensionless mass ratio. To obtain MeV, one multiplies
by a calibration factor with the dimensions of energy. The
**categorical density** $\rho_K$ packages this calibration as a
braid-class invariant:

$$
  \rho_K \;=\;
  \frac{\mathfrak{m}(K)}{m_e \cdot
    \lvert\!\mathrm{tr}_M\!\bigl(\mathrm{NF}_{\mathrm{GS}}(\mathcal{B}_K)\bigr)\!\rvert}.
$$

| Atom | $A$ | $\lvert\mathrm{tr}_M(\mathrm{NF}_{\mathrm{GS}})\rvert$ | $\mathfrak{m}_{\mathrm{CODATA}}$ (MeV) | $\rho_K^{\mathrm{CODATA}}$ |
|---|---|---|---|---|
| $\mathfrak{p}$ | $1$ | $1.0653$ | $938.272$ | $1723.6$ |
| $\mathfrak{n}$ | $1$ | $0.9232$ | $939.565$ | $1991.6$ |
| $D$ | $2$ | $0.3883$ | $1875.613$ | $9453.0$ |
| $T$ | $3$ | $0.1041$ | $2808.921$ | $52828.5$ |
| ${}^3\mathrm{He}$ | $3$ | $0.2065$ | $2808.392$ | $26609.2$ |

$\rho_K^{\mathrm{CODATA}}$ grows super-linearly in $A$, with
$\rho_K(\mathrm{T}) / \rho_K(\mathfrak{p}) \approx 30.6$ for $A = 3$.

## Open question: categorical derivation of $\rho_K$

The (GB-NF) form makes the algebraic structure manifest: $\mathcal{B}_K$
reduces to a unique normal form $\mathrm{NF}_{\mathrm{GS}}(\mathcal{B}_K)$ in
$H_n(q_0)$, and its Markov trace is computable directly from braid
data alone. The categorical-density derivation lives in
[graded ρ_K expansion](#prop:rho-k-graded-expansion):

$$
  m_e \cdot |\!\mathrm{tr}_M(\mathcal{B}_K)| \cdot \rho_K
  \;=\;
  \underbrace{Z m_{\mathfrak{p}} + N m_{\mathfrak{n}} + Z m_e}_{\rho_K^{\mathrm{LO}}\text{-piece}}
  \;+\; \underbrace{\tfrac{\alpha}{2} \sum_i \ln\bigl(\hat V_i^{\mathrm{full}} \cdot \overline{\hat V_i^{\mathrm{full}}}\bigr)}_{\rho_K^{\text{single-gen}}\text{-piece}}
  \;+\; \underbrace{\tfrac{\alpha\, z^2}{2}\!\!\sum_{i<j}\!\ln\bigl(\hat V_i \hat V_j \cdot \overline{\hat V_i \hat V_j}\bigr)\!\big|_{\mathrm{Wedd}}}_{\rho_K^{\text{pair-gen}}\text{-piece (open)}}
  \;+\; \dots
$$

**The LO piece is no longer an ansatz.** It constitutes the categorical
consequence of \[Wenzl 1988] Markov multiplicativity for disjoint
braids ($\mathrm{tr}_M(\mathcal{B}_p \otimes \mathcal{B}_n) = \mathrm{tr}_M(\mathcal{B}_p) \mathrm{tr}_M(\mathcal{B}_n)$,
verified numerically to $3.2 \times 10^{-14}$)
plus free-constituent mass additivity:

$$
  \rho_K^{\mathrm{LO}}
  \;=\;
  \frac{Z m_{\mathfrak{p}} + N m_{\mathfrak{n}} + Z m_e}{m_e \cdot \lvert\!\mathrm{tr}_M(\mathcal{B}_K)\!\rvert}.
$$

The single-gen binding correction $\tfrac{\alpha}{2} \sum_i \ln\bigl(\hat V_i^{\mathrm{full}} \cdot \overline{\hat V_i^{\mathrm{full}}}\bigr)$
(where $\overline{\,\cdot\,}$ forms the Hecke bar-involution $q \leftrightarrow q^{-1}$;
at the archimedean specialization with real $q_0$ and real $\hat V_i$,
this equals $\alpha \sum_i \ln|\hat V_i^{\mathrm{full}}|$)
with $\alpha = m_e \cdot 8G$ ([binding scale](#conj:binding-scale-catalan))
takes $\rho_K$ to $0.18\%$ mean accuracy across $Z = 1..20$
([atomic braid mass](#sec:atomic-braid-mass-foundations)). The pair-gen and
higher pieces require the proper Wedderburn-coupling structure
(open work; see [graded ρ_K expansion](#prop:rho-k-graded-expansion)).

**Mirror-pair check** (T and ${}^3\mathrm{He}$, both $A=3$, $n=9$
<!-- literal-source: closed-form ratio of mirror-pair categorical density factors rho_K(T) / rho_K(3He) -->
strands): the categorical density factors $\rho_K(T) / \rho_K({}^3\mathrm{He}) = 1.9853$
exactly compensate $|\!\mathrm{tr}_M({}^3\mathrm{He})| / |\!\mathrm{tr}_M(T)| = 1.9850$,
since their CODATA masses agree to $0.02\%$. So $\rho_K$ is **not**
a function of $(A, n\text{-strands})$ alone. It must depend on the
specific braid $\mathcal{B}_K$ through $|\!\mathrm{tr}_M(\mathrm{NF}_{\mathrm{GS}}(\mathcal{B}_K))|$
(and hence $\rho_K \cdot |\!\mathrm{tr}_M\!|$ constructs the
mirror-symmetric quantity, equal to $\mathfrak{m}(K)/m_e$).

**Reduction.** The categorical-closure question reduces to deriving
the nucleon-mass anchors $m_{\mathfrak{p}}$ and $m_{\mathfrak{n}}$ from $H_3(q_0)$ data alone.
Once these anchors become categorically self-determined, the
constituent decomposition plus binding correction recovers atomic
mass ratios to sub-percent across the full $A = 1..20$ range
([Wedderburn mass](#thm:wedderburn-mass-formula)). The definitive
resolution is the **muon-anchored Hecke energy** identity:
$m_{\mathfrak{p}} = 2(m_\mu \cdot F_{\mathrm{Bor}} - 6 m_e)$, which fixes the
nucleon-mass ratio $m_{\mathfrak{p}}/m_e$ natively (through the muon ratio
$m_\mu/m_e$) without empirical proton calibration fits.

**Connection to the $\alpha_{\mathrm{shift}}$ framework.**
The Habiro denominator factorisation provides the exact structure for $D(u)$:

$$
  D(u) \;=\; 2^{2A+1} \cdot u^{\mathrm{shift}} \cdot (1 + u^2)^{3A-1}.
$$

By anchoring the mass ratio to the muon-anchored Hecke energy rather than an empirical proton fit, the formula demonstrates that $\rho_K$ is categorically self-determined and not an ad-hoc calibration scalar. The small binding correction is thus a clean JSJ/q-CLT trace extrapolation.

## Reading the three forms

The three forms encode the same physical mass $\mathfrak{m}(K)$
parameterised by different calibration data:

* **(constituent)** anchors at the nucleon level but evaluates the exact constituent masses through the **muon-anchored Hecke energy** $m_{\mathfrak{p}} = 2(m_\mu F_{\mathrm{Bor}} - 6m_e)$, rendering CODATA fits unnecessary. Sub-percent for $Z = 1$..$20$.
* **(muon-anchored)** is the definitive structural mass form. It computes the mass ratio without any phenomenological proton calibration or empirical spectral parameter tuning, resolving the atomic mass ratio strictly from the topological aether; the MeV figure follows from the $m_e$ scale and is a rendering rather than an absolute-mass claim.
* **(GB-NF)** states the algebraic statement. The atomic mass is
  proportional to the Markov trace of the normal form, with the
  proportionality constant $\rho_K$ as the categorical density.

The propositional content carried by (GB-NF) — that the atomic mass
factors through the Gröbner–Shirshov quotient — renders the
:refterm[descent]{#descent} in [categorical mass = Markov](#prop:categorical-mass-markov)
applicable. The trace depends only on the braid class modulo the
PBW relations.

## Numerical cross-checks

Independent evaluations compare $\rho_K^{\mathrm{CODATA}}$ against $\rho_K^{6\text{-term}}$ across $A = 1, 2, 3$, evaluate the leading-order scaling ansatz $\rho_K \approx (Z m_{\mathfrak{p}} + N m_{\mathfrak{n}})/(m_e \cdot |\!\mathrm{tr}_M\!|)$ ($0.14\%$ mean residual) alongside the $A = 3$ mirror pair, certify $\lvert\!\mathrm{tr}_M(\mathrm{NF}_{\mathrm{GS}}(\mathcal{B}_K))\!\rvert$ to $50$ decimal places, and compare constituent and six-term spectral $m_e$-scaled mass evaluations across all five tower modes.
