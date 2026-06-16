## Statement

**Class-A discipline status.** The three forms below have **different discipline statuses**:

- **(GB-NF)** is the production-target algebraic form. $\rho_K$ admits a
  **graded substrate expansion**
  ([`prop:rho-k-graded-expansion`](rho-k-graded-expansion.md)) —
  LO piece (Markov-multiplicative nucleon sum) **proved** via Wenzl
  1988; single-gen piece $\tfrac{\alpha}{2} \sum_i \ln(\hat V_i^{\mathrm{full}} \cdot \overline{\hat V_i^{\mathrm{full}}})$
  closes empirically to $0.18\%$ mean error; pair-gen piece remains
  open. The H_3-anchor refinement of the per-irrep coefficients is
  the subject of [`prop:rho-k-h3a-refinement`](rho-k-h3a-refinement.md).
- **(constituent)** consumes CODATA $m_{\mathfrak{p}}, m_{\mathfrak{n}}$
  as upstream inputs — a **Class-A opt-out** (acknowledged 4th/5th
  calibration injection) tracked under
  [Workplan 0b](../../../docs/audits/-workplan-0b-script-rewire-handoff.md).
  The substrate-pure replacement is $m_{\mathfrak{n}} = m_{\mathfrak{p}}
  + \mathfrak{Q}_\beta + m_e$ with $m_{\mathfrak{p}}$ from
  [`prop:lambda-scale-substrate-form`](lambda-scale-substrate-form.md)
  ($\lambda_{\mathrm{scale}} \approx 5/2 - h^2 G$, matching CODATA to
  ~5.4 ppm — currently *justification* at this precision per
  [`docs/audits/-lambda-scale-derivation-search.md §13`](../../../docs/audits/-lambda-scale-derivation-search.md))
  and [`prop:flavor-split-substrate`](../observations/flavor-split-substrate.md)
  for the $m_n - m_p$ split. ${}^1\mathrm{H}$ already lifts to
  `derived` once the Borromean tower wiring is on-trunk.
- **(six-term spectral)** consumes a proton-mass calibration to fix
  $E_0$ — also a **Class-A opt-out** until $E_0$ is independently
  derived from CAL-3 ($\mathfrak{Q}_\beta(n)$). Substrate replacement candidate:
  $E_0 = m_e / (q_0(q_0 - 1))$ from
  [`prop:three-calibration-inputs`](three-calibration-inputs.md).

Per the [three-calibration discipline](three-calibration-inputs.md),
the (constituent) and (six-term spectral) forms violate the rule by
admitting additional calibrations beyond CAL-1/2/3; the §Open and
§Negative-result shift-anchor sections below document the empirical
falsifications and the structural barriers to closure. Treat numerical
outputs from those two forms as illustrative until the substrate-pure
replacements land.

**Proposition.**
*Let $(Z, N)$ be a neutral atom with atomic braid
$\mathcal{B}_K \in B_{n}$, where $n = 3A + Z$ and $A = Z + N$
([atomic braid](#def\:atomic-braid)).
Let $\mathrm{NF}_{\mathrm{GS}}(\mathcal{B}_K) \in H_n(R, q_0)$ denote the
Gröbner–Shirshov normal form of $\mathcal{B}_K$ in the Iwahori–Hecke
algebra under the PBW Gröbner–Shirshov basis
([PBW corollary](unital-groebner-bases\:cor\:pbw)).
Then the atomic mass admits the unified categorical expression*

$$
  \mathcal{M}(K)
  \;=\;
  m_e \cdot \rho_K \cdot
  \bigl\lvert\!\operatorname{tr}_M\!\bigl(\mathrm{NF}_{\mathrm{GS}}(\mathcal{B}_K)\bigr)\!\bigr\rvert,
$$

*where $\operatorname{tr}_M$ is the canonical Jones–Markov trace
([categorical mass = Markov](#prop\:categorical-mass-markov))
and $\rho_K$ is a positive scalar — the **categorical density**
of the atomic braid class.*

## Three equivalent forms

The same observable $\mathcal{M}(K)$ admits three rewritings,
each exposing different structure:

| Form                                                                                                                                       | Inputs                                                                       | Status                                                                                                 |
| :----------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------- |
| **(GB-NF)** $\mathcal{M} = m_e \cdot \rho_K \cdot \lvert\!\operatorname{tr}_M\!\bigl(\mathrm{NF}_{\mathrm{GS}}(\mathcal{B}_K)\bigr)\!\rvert$     | $m_e$, $\mathcal{B}_K$, $q_0$, $\rho_K$                                            | algebraic; $\rho_K$ currently empirical                                                                |
| **(constituent)** $\mathcal{M} = Z m_{\mathfrak{p}} + N m_{\mathfrak{n}} + Z m_e + \alpha \sum_i \ln\lvert\hat{V}_i^{\mathrm{full}}\rvert$ | $m_e$, **$m_{\mathfrak{p}}$, $m_{\mathfrak{n}}$ (CODATA)**, $\mathcal{B}_K$, $q_0$ | $0.18\%$ mean error, $Z\!=\!1\!\dots\!20$ ([Wedderburn mass](#thm\:wedderburn-mass-formula))           |
| **(six-term spectral)** $\mathcal{M} = T_1 + T_2 + T_3 + T_4 + T_5 + T_6$                                                                  | $m_e$, $\mathcal{B}_K$, $q_0$, $E_0$ (proton calibration)                          | $25\%$ under-prediction at ${}^4\mathrm{He}$ ([unified mass formula](#thm\:knot-mass-formula-unified)) |

The (GB-NF) form is the **abstract algebraic statement**; the
other two are concrete evaluations that fix $\rho_K$ via different
calibration data.

## The categorical density factor $\rho_K$

By the categorical-mass identity
([categorical mass = Markov](#prop\:categorical-mass-markov)):
$\mathfrak{m}_{q,K} = \lvert\!\operatorname{tr}_M(\rho(\mathcal{B}_K))\!\rvert$
is the **dimensionless** mass ratio. To obtain MeV, one multiplies
by a calibration factor with the dimensions of energy. The
**categorical density** $\rho_K$ packages this calibration as a
braid-class invariant:

$$
  \rho_K \;=\;
  \frac{\mathcal{M}(K)}{m_e \cdot
    \lvert\!\operatorname{tr}_M\!\bigl(\mathrm{NF}_{\mathrm{GS}}(\mathcal{B}_K)\bigr)\!\rvert}.
$$

**Empirical values** (from
`rho-k-codata-vs-six-term.witness.json`, evaluated at $q_0$ via
50-dps Markov trace of `markov_peel.tr_M_atomic`):

|        Atom       | $A$ | $\lvert\operatorname{tr}_M(\mathrm{NF}_{\mathrm{GS}})\rvert$ | $\mathcal{M}_{\mathrm{CODATA}}$ (MeV) | $\rho_K^{\mathrm{CODATA}}$ |
| :---------------: | :-: | :----------------------------------------------------------: | :-----------------------------------: | :------------------------: |
|   $\mathfrak{p}$  |  1  |                           $1.0653$                           |               $938.272$               |          $1723.6$          |
|   $\mathfrak{n}$  |  1  |                           $0.9232$                           |               $939.565$               |          $1991.6$          |
|        $D$        |  2  |                           $0.3883$                           |               $1875.613$              |          $9453.0$          |
|        $T$        |  3  |                           $0.1041$                           |               $2808.921$              |          $52828.5$         |
| ${}^3\mathrm{He}$ |  3  |                           $0.2065$                           |               $2808.392$              |          $26609.2$         |

$\rho_K^{\mathrm{CODATA}}$ grows super-linearly in $A$, with
$\rho_K(\mathrm{T}) / \rho_K(\mathfrak{p}) \approx 30.6$ for $A = 3$.

## Open question: categorical derivation of $\rho_K$

The (GB-NF) form makes the **algebraic** structure manifest: $\mathcal{B}_K$
reduces to a unique normal form $\mathrm{NF}_{\mathrm{GS}}(\mathcal{B}_K)$ in
$H_n(q_0)$, and its Markov trace is computable directly from braid
data alone. The categorical-density derivation lives in
[graded ρ\_K expansion](#prop\:rho-k-graded-expansion):

$$
  m_e \cdot |\!\operatorname{tr}_M(\mathcal{B}_K)| \cdot \rho_K
  \;=\;
  \underbrace{Z m_{\mathfrak{p}} + N m_{\mathfrak{n}} + Z m_e}_{\rho_K^{\mathrm{LO}}\text{-piece}}
  \;+\; \underbrace{\tfrac{\alpha}{2} \sum_i \ln\bigl(\hat V_i^{\mathrm{full}} \cdot \overline{\hat V_i^{\mathrm{full}}}\bigr)}_{\rho_K^{\text{single-gen}}\text{-piece}}
  \;+\; \underbrace{\tfrac{\alpha\, z^2}{2}\!\!\sum_{i<j}\!\ln\bigl(\hat V_i \hat V_j \cdot \overline{\hat V_i \hat V_j}\bigr)\!\big|_{\mathrm{Wedd}}}_{\rho_K^{\text{pair-gen}}\text{-piece (open)}}
  \;+\; \dots
$$

**The LO piece is no longer an "ansatz"** — it is the categorical
consequence of \[Wenzl 1988] Markov multiplicativity for disjoint
braids ($\operatorname{tr}_M(\mathcal{B}_p \otimes \mathcal{B}_n) = \operatorname{tr}_M(\mathcal{B}_p) \operatorname{tr}_M(\mathcal{B}_n)$,
verified to $3.2 \times 10^{-14}$ in `rho-k-markov-multiplicativity.witness.json`)
plus free-constituent mass additivity:

$$
  \rho_K^{\mathrm{LO}}
  \;=\;
  \frac{Z m_{\mathfrak{p}} + N m_{\mathfrak{n}} + Z m_e}{m_e \cdot \lvert\!\operatorname{tr}_M(\mathcal{B}_K)\!\rvert}.
$$

The single-gen binding correction $\tfrac{\alpha}{2} \sum_i \ln\bigl(\hat V_i^{\mathrm{full}} \cdot \overline{\hat V_i^{\mathrm{full}}}\bigr)$
(where $\overline{\,\cdot\,}$ is the Hecke bar-involution $q \leftrightarrow q^{-1}$;
at the archimedean specialization with real $q_0$ and real $\hat V_i$,
this equals $\alpha \sum_i \ln|\hat V_i^{\mathrm{full}}|$)
with $\alpha = m_e \cdot 8G$ ([binding scale](#prop\:binding-scale-catalan))
takes ρ\_K to $0.18\%$ mean accuracy across $Z = 1..20$
([atomic braid mass](#prop\:atomic-braid-mass)). The pair-gen and
higher pieces require the proper Wedderburn-coupling structure
(open work; see [graded ρ\_K expansion](#prop\:rho-k-graded-expansion)).

**Mirror-pair check** (T and ${}^3\mathrm{He}$, both $A=3$, $n=9$
strands): the categorical density factors $\rho_K(T) / \rho_K({}^3\mathrm{He}) = 1.9853$
exactly compensate $|\!\operatorname{tr}_M({}^3\mathrm{He})| / |\!\operatorname{tr}_M(T)| = 1.9850$,
since their CODATA masses agree to $0.02\%$. So $\rho_K$ is **not**
a function of $(A, n\text{-strands})$ alone — it must depend on the
specific braid $\mathcal{B}_K$ through $|\!\operatorname{tr}_M(\mathrm{NF}_{\mathrm{GS}}(\mathcal{B}_K))|$
(and hence $\rho_K \cdot |\!\operatorname{tr}_M\!|$ is the
mirror-symmetric quantity, equal to $\mathcal{M}(K)/m_e$).

**Reduction.** The categorical-closure question reduces to deriving
the nucleon-mass anchors $m_{\mathfrak{p}}/m_e \approx 1836.15$ and
$m_{\mathfrak{n}}/m_e \approx 1838.68$ from $H_3(q_0)$ data alone.
Once these anchors are categorically self-determined, the
constituent decomposition plus binding correction recovers atomic
masses to sub-percent across the full $A = 1..20$ range
([Wedderburn mass](#thm\:wedderburn-mass-formula)). The six-term
spectral form is the current best candidate; empirically with
proton calibration it recovers $m_{\mathfrak{p}}$ by construction
but predicts $m_{\mathfrak{n}}$ to only $4.9\%$
(`paper-six-term-isotope-sweep.witness.json`, `li2q` mode), so the
nucleon-anchor question remains the structural bottleneck.

**Connection to the $\alpha_{\mathrm{shift}}$ framework.**
The same bottleneck appears in the Habiro denominator factorisation
([w3 audit](../../docs/audits/-w3-habiro-unblocked.md)):

$$
  D(u) \;=\; 2^{2A+1} \cdot u^{\mathrm{shift}} \cdot (1 + u^2)^{3A-1},
$$

where the $2^{2A+1}$ and $(1+u^2)^{3A-1}$ factors are proved
categorically but the per-nucleon shift exponents
($\mathrm{shift}_{\mathfrak{p}} = 20$,
$\mathrm{shift}_{\mathfrak{n}} = 16$ for `include_inter=False`) are
characterised only via integer-LP. The clean torus-knot limit
$\alpha_{\mathrm{shift}}(T_{p,k}) = k(p-1)$ on $V_{(1^p)}$ is proved
([torus-knot pole order](#prop\:alpha-shift-torus-knot)) and powers
the multiplicative-chain identity for $\alpha_{EM}^{-1}$
([$\alpha_{EM}$ chain](#prop\:alpha-em-shift-multiplicative-chain)),
but the atomic-braid case carries a strand-context-dependent profile
$(1, 4, 0, 0, 1, 0)$ for the per-crossing shift contributions whose
categorical origin is open. The atomic-shift coefficients
$(18, 21, 1)$ governing
[`prop:per-nucleon-shift-additive-linearity`](per-nucleon-shift-additive-linearity.md)
are now **categorically verified** for the proton and deuteron via
the symbolic Hoefsmit pole-order analysis in
[`per_irrep_pole_atom.py`](../../folio-assistant/computations/per_irrep_pole_atom.py)
(witnesses
[`per-irrep-pole-proton-h3.witness.json`](../../folio-assistant/computations/per-irrep-pole-proton-h3.witness.json)
+
[`per-irrep-pole-deuteron-h6.witness.json`](../../folio-assistant/computations/per-irrep-pole-deuteron-h6.witness.json)),
closing the per-nucleon contribution to $\mathrm{shift}_{\mathrm{NF}}$
that controls the $u$-power in $D(u)$. Closing the strand-context
profile $(1, 4, 0, 0, 1, 0)$ remains open.

**Negative result on the simple shift-anchor ansatz**
(`u-shift-mass-anchor-probe.witness.json`).
No combination of $\mathrm{shift}_{\mathfrak{p}}, \mathrm{shift}_{\mathfrak{n}}$
and the $q_0$-derived constants $(q_0, c_q, \hbar_q, z, [n]_q)$
reproduces both nucleon anchors to better than $11\%$. The closest
single-formula fit, $\mathrm{shift} \cdot q \cdot c_q^2 \approx 1835.4$,
matches $m_{\mathfrak{p}}/m_e$ to $0.04\%$ but fails for the neutron
($20\%$ error). The integer 4-unit shift differential ($20 \to 16$)
is structurally too coarse to encode the $0.14\%$ CODATA
$m_{\mathfrak{n}} - m_{\mathfrak{p}}$ splitting — the splitting
must be encoded in the per-irrep character data, not in the scalar
shift exponent alone.

The (six-term spectral) form is the current best candidate
attempt, expanding $\rho_K \cdot \lvert\!\operatorname{tr}_M\!\rvert$
into a $\sum_{i=1}^{6} T_i$ decomposition over the Wedderburn
blocks plus the cyclotomic tail. Empirically the six-term
expansion **under-predicts** $\rho_K$ by $22\%$–$31\%$ for
$A \in \{2, 3\}$ when calibrated against the proton
(`paper-six-term-isotope-sweep.witness.json`):

|        Atom       | $\rho_K^{\mathrm{CODATA}}$ | $\rho_K^{6\text{-term}}$ |       gap (%)      |
| :---------------: | :------------------------: | :----------------------: | :----------------: |
|   $\mathfrak{p}$  |          $1723.6$          |         $1723.6$         | $0.0$ (calibrated) |
|   $\mathfrak{n}$  |          $1991.6$          |         $1893.8$         |       $+4.9$       |
|        $D$        |          $9453.0$          |         $7398.2$         |       $+21.7$      |
|        $T$        |          $52828.5$         |         $36193.8$        |       $+31.5$      |
| ${}^3\mathrm{He}$ |          $26609.2$         |         $19523.5$        |       $+26.6$      |

The (constituent) form sidesteps this question by **using CODATA
$m_{\mathfrak{p}}, m_{\mathfrak{n}}$ as inputs**: the $0.18\%$
accuracy is dominated by the CODATA constituent sum, with
$\alpha \sum \ln\lvert\hat{V}_i^{\mathrm{full}}\rvert \approx -7$ MeV
of categorical correction. In particular, the (constituent)
formula does **not** demonstrate that $\rho_K$ is categorically
self-determined; it demonstrates that, given CODATA nucleon masses,
the small binding correction is captured by a clean log-volume sum.

## Reading the three forms

The three forms encode the same physical mass $\mathcal{M}(K)$
parameterised by different calibration data:

* **(constituent)** anchors at the *nucleon level*: take CODATA
  $m_{\mathfrak{p}}, m_{\mathfrak{n}}$ as primitive, treat the
  binding/electron-coupling as a categorical correction.
  Sub-percent for $Z = 1$..$20$.
* **(six-term spectral)** anchors at the *electron level*: take
  $m_e$ and $E_0 = m_{\mathfrak{p}}^{\mathrm{CODATA}} / \lvert\!\operatorname{tr}_M(\mathrm{NF}_{\mathrm{GS}}(\beta_{\mathfrak{p}}))\!\rvert$
  as the only calibration; predict everything else from $q_0$ and
  the braid spectrum. Currently $25\%$ off at $A = 4$.
* **(GB-NF)** is the *algebraic statement*: the atomic mass is
  proportional to the Markov trace of the normal form, with the
  proportionality constant $\rho_K$ as the categorical density.

The propositional content carried by (GB-NF) — that the atomic mass
factors through the Gröbner–Shirshov quotient — is what makes the
:refterm[descent]{#descent} in [categorical mass = Markov](#prop\:categorical-mass-markov)
applicable: the trace depends only on the braid class modulo the
PBW relations.

## Witnesses

* `rho-k-codata-vs-six-term.witness.json` — $\rho_K^{\mathrm{CODATA}}$ vs $\rho_K^{6\text{-term}}$ table for $A = 1, 2, 3$.
* `rho-k-scaling-structure.witness.json` — leading-order ansatz $\rho_K \approx (Z m_{\mathfrak{p}} + N m_{\mathfrak{n}})/(m_e \cdot |\!\operatorname{tr}_M\!|)$ ($0.14\%$ mean residual); mirror-pair analysis.
* `atomic-tr-m-mpfr-50dps.witness.json` — canonical $\lvert\!\operatorname{tr}_M(\mathrm{NF}_{\mathrm{GS}}(\mathcal{B}_K))\!\rvert$ at 50 decimal-place precision.
* `atom-mass-atomic-braid.witness.json` — (constituent) form predictions.
* `paper-six-term-isotope-sweep.witness.json` — (six-term spectral) predictions across all five tower modes.
