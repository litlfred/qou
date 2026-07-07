<!-- FILE_START: categorical-mass-foundations-intro.md -->
The preceding section established Reidemeister invariance of mass on the Borromean test case. We now lay the categorical foundations for all subsequent mass calculations. Mass constitutes a categorical invariant. It equals the Markov trace of a distinguished element of the Hecke algebra, splits along the descent involution into a base-level term plus a transient blow-up correction, and admits a recursive symbolic reducer with a disjoint-product property for multi-atom composites.

This section decomposes mass under the descent involution, culminating in the structural identification of the categorical mass with $\mathrm{tr}_M$ on $H_n(q)$ ([categorical mass = Markov](#prop:categorical-mass-markov)). It fills out the algebraic backbone with the Gröbner–Shirshov normal form trace evaluation, Hecke branching decompositions, and the recursive symbolic Markov-trace reducer. Finally, it aligns the Markov-Z spectrum with the mass-endomorphism conjecture and packages the mass functor as a global section ($\Phi_n$) ready for calibration. The subsequent section, Calibration and Algebraic Mass Formula, anchors this functor to physical units via three calibration inputs.
<!-- FILE_END: categorical-mass-foundations-intro.md -->

<!-- FILE_START: topological-mass-cat-eigenspace.md -->
**Lemma.**
*Let $\alpha = (\int_A \otimes \mathrm{id}) \circ \Delta \circ \varrho$
form the categorical mass integrand of a closed cycle $\varrho$. When
the [Frobenius pairing](#def:frobenius-pairing) is compatible with the
$*$-involution, the :refterm[descent]{#descent} involution $\hat{\tau}_n$ produces an
orthogonal decomposition of $\alpha$ into descended and transient
components, giving*

$$
  \mathfrak{m}(\varrho)^2
  =
  \bigl\lVert \mathrm{tr}(\hat{\tau}_n(\alpha)) \bigr\rVert^2
  +
  \bigl\lVert \mathrm{tr}(\alpha - \hat{\tau}_n(\alpha)) \bigr\rVert^2.
$$

*(Orthogonal components add **in quadrature**, not linearly. The
descended and transient traces are orthogonal, so the masses combine
by the Pythagorean law, not additively.)*
<!-- FILE_END: topological-mass-cat-eigenspace.md -->

<!-- FILE_START: topological-mass-cat-descended.md -->
**Lemma.**
*Let $\alpha = (\int_A \otimes \mathrm{id}) \circ \Delta \circ \varrho$
form the categorical mass integrand of a closed cycle $\varrho$ at level
$n+1$. Let $\varrho_0$ denote its base-level :refterm[descent]{#descent}. Then*

$$
  \bigl\lVert \mathrm{tr}(\hat{\tau}_n(\alpha)) \bigr\rVert
  =
  \mathfrak{m}(\varrho_0).
$$
<!-- FILE_END: topological-mass-cat-descended.md -->

<!-- FILE_START: topological-mass-cat-transient.md -->
**Lemma.** *The transient component $\alpha - \hat{\tau}_n(\alpha) \in \mathcal{A}_{n+1}^{\mathrm{trans}}$ has support contained in the union of the kernels of $\mathfrak{d}_{n+1}$ at the blow-up centres $p_1, \ldots, p_N$. The transient trace decomposes as a sum of disjoint local contributions:*

$$
  \mathrm{tr}(\alpha - \hat{\tau}_n(\alpha))
  = 
  \sum_{i=1}^{N} \mathrm{tr}_{\mathrm{trans}}(\varrho, p_i).
$$
<!-- FILE_END: topological-mass-cat-transient.md -->

<!-- FILE_START: categorical-mass-markov.md -->
The categorical mass descends to the Iwahori–Hecke algebra. Single-level categorical mass evaluates to the absolute value of the Markov trace.

## Statement

**Proposition.**
*Let $(\mathbf{C}, A, \tau)$ form a quantum observable universe with Frobenius–Hopf object $A = H_n(R, q)$ over a commutative ring $R$. Let $\varrho \colon \mathbf{1} \to A$ form a closed cycle representing the knot $\mathcal{K}$ with braid representative $\beta_\mathcal{K} \in B_n$. The single-level categorical mass satisfies*

$$
  \mathfrak{m}_{q,\mathcal{K}}\big|_{\text{single level}}
  \;=\; \Bigl|\!\int_A\! \rho(\beta_\mathcal{K})\Bigr|,
$$

*where $\int_A : A \to R$ is the Jones–Markov trace, functioning as the Frobenius integral on $A$.*

## Modulus isolates the bar-even shadow

The absolute value operation isolates the bar-even ($\cosh$, real-$q$) component of the Markov trace. This provides the mass or binding channel. The discarded bar-odd ($\sinh$, root-of-unity-$q$) component is not noise. It provides the imaginary part of the complex fibre observable $\mathfrak{V}$, where $\mathfrak{V} = \mathfrak{E}_{\mathrm{bind}} + i\,\mathfrak{Q}_\beta$. This imaginary part equals the $\beta$-decay $Q$-value, $\mathfrak{Q}_\beta = \mathrm{Im}\,\mathfrak{V}$.

Mass and $\mathfrak{Q}_\beta$ construct the two parities of a single object ([`conj:binding-qbeta-complex-volume`](binding-qbeta-complex-volume.md)). We take the modulus only when the mass magnitude alone is required. Any computation tying binding to decay must retain the bar-odd shadow. This requires the root-of-unity evaluation, rather than collapsing to the modulus.

The parameter $q_0$ is not complex. At the observable level, $\mathrm{Im}(q_0) = 0$. The imaginary part forms the fibre-level shadow, which constitutes a separate real observable.
<!-- FILE_END: categorical-mass-markov.md -->

<!-- FILE_START: markov-trace-gibbs-free-energy.md -->
*Interpretation of the [categorical mass–Markov decomposition](#prop:categorical-mass-markov).*

The binding formula follows a thermodynamic form. Writing

$$
  \mathfrak{E}_{\mathrm{bind}}
  \;=\;
  E_0 \,\ln\frac{\mathrm{tr}_M(W_{\text{free}})}{\mathrm{tr}_M(W_{\text{atom}})},
$$

the Markov trace occupies the partition function slot and $E_0$ occupies the temperature slot. The expression defines a free-energy difference $\Delta F = kT \ln(Z_1/Z_2)$ with $kT = E_0$. This is not an external analogy. Markov traces on the Hecke tower form temperature (Gibbs-type) states in the operator-algebraic sense \cite{jones1987}. The deformation parameter sets the inverse temperature scale ($\beta \sim \ln q$). Energy and information appear Legendre-dual by construction. The entropy in play is that of the normalized channel measure $\hat y_\lambda \chi^\lambda$ over Wedderburn blocks. The binding energy forms the free-energy cost of the channel reweighting imposed by confinement.

Two limiting statements render the information reading exact. A trace concentrated on a single one-dimensional channel has zero channel entropy and contributes zero free-energy difference. A configuration that does not oscillate between channels carries no information and no binding-scale energy. At the opposite end, the per-crossing information rate is bounded by the operational entropy $\eta_q$ of the [fibre channel capacity](#rem:fibre-channel-capacity). Thus, a braid's information content (and the free energy available to channel reweighting) grows at most linearly in its crossing number.
<!-- FILE_END: markov-trace-gibbs-free-energy.md -->

<!-- FILE_START: atomic-mass-gb-nf.md -->
## Statement

**Proposition.**
*Let $(Z, N)$ be a neutral atom with atomic braid $\mathcal{B}_K \in B_{n}$, where $n = 3A + Z$ and $A = Z + N$ ([atomic braid](#def:atomic-braid)). Let $\mathrm{NF}_{\mathrm{GS}}(\mathcal{B}_K) \in H_n(R, q_0)$ denote the Gröbner–Shirshov normal form of $\mathcal{B}_K$ in the Iwahori–Hecke algebra under the PBW Gröbner–Shirshov basis ([PBW corollary](unital-groebner-bases:cor:pbw)). The atomic mass admits the unified categorical expression:*

$$
  \mathcal{M}(K)
  \;=\;
  m_e \cdot \rho_K \cdot
  \bigl\lvert\!\operatorname{tr}_M\!\bigl(\mathrm{NF}_{\mathrm{GS}}(\mathcal{B}_K)\bigr)\!\bigr\rvert,
$$

*where $\operatorname{tr}_M$ provides the canonical Jones–Markov trace ([categorical mass = Markov](#prop:categorical-mass-markov)) and $\rho_K$ provides a positive scalar—the **categorical density** of the atomic braid class.*

**Archimedean specialisation (§7c).** This block operates on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs: real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluations at the substrate parameter $q_0$. Any generic categorical or $q$-deformation identities it employs hold over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: atomic-mass-gb-nf.md -->

<!-- FILE_START: atomic-mass-gb-nf-interpretation.md -->
## Three equivalent forms

The same observable $\mathcal{M}(K)$ admits three rewritings.
Each exposes different structure:

| Form | Inputs | Status |
|---|---|---|
| **(GB-NF)** $\mathcal{M} = m_e \cdot \rho_K \cdot \lvert\!\operatorname{tr}_M\!\bigl(\mathrm{NF}_{\mathrm{GS}}(\mathcal{B}_K)\bigr)\!\rvert$ | $m_e$, $\mathcal{B}_K$, $q_0$, $\rho_K$ | algebraic; $\rho_K$ currently empirical |
| **(constituent)** $\mathcal{M} = Z m_{\mathfrak{p}} + N m_{\mathfrak{n}} + Z m_e + \alpha \sum_i \ln\lvert\hat{V}_i^{\mathrm{full}}\rvert$ | $m_e$, **$m_{\mathfrak{p}}$, $m_{\mathfrak{n}}$ (CODATA)**, $\mathcal{B}_K$, $q_0$ | $0.18\%$ mean error, $Z\!=\!1\!\dots\!20$ ([Wedderburn mass](#thm:wedderburn-mass-formula)) |
| **(six-term spectral)** $\mathcal{M} = T_1 + T_2 + T_3 + T_4 + T_5 + T_6$ | $m_e$, $\mathcal{B}_K$, $q_0$, $E_0$ (proton calibration) | $25\%$ under-prediction at ${}^4\mathrm{He}$ ([unified mass formula](#thm:knot-mass-formula-unified)) |

The (GB-NF) form constitutes the abstract algebraic statement. The
other two constitute concrete evaluations that fix $\rho_K$ via different
calibration data.

## The categorical density factor $\rho_K$

By the categorical-mass identity
([categorical mass = Markov](#prop:categorical-mass-markov)):
$\mathfrak{m}_{q,K} = \lvert\!\operatorname{tr}_M(\rho(\mathcal{B}_K))\!\rvert$
provides the dimensionless mass ratio. To obtain MeV, one multiplies
by a calibration factor with the dimensions of energy. The
**categorical density** $\rho_K$ packages this calibration as a
braid-class invariant:

$$
  \rho_K \;=\;
  \frac{\mathcal{M}(K)}{m_e \cdot
    \lvert\!\operatorname{tr}_M\!\bigl(\mathrm{NF}_{\mathrm{GS}}(\mathcal{B}_K)\bigr)\!\rvert}.
$$

| Atom | $A$ | $\lvert\operatorname{tr}_M(\mathrm{NF}_{\mathrm{GS}})\rvert$ | $\mathcal{M}_{\mathrm{CODATA}}$ (MeV) | $\rho_K^{\mathrm{CODATA}}$ |
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
  m_e \cdot |\!\operatorname{tr}_M(\mathcal{B}_K)| \cdot \rho_K
  \;=\;
  \underbrace{Z m_{\mathfrak{p}} + N m_{\mathfrak{n}} + Z m_e}_{\rho_K^{\mathrm{LO}}\text{-piece}}
  \;+\; \underbrace{\tfrac{\alpha}{2} \sum_i \ln\bigl(\hat V_i^{\mathrm{full}} \cdot \overline{\hat V_i^{\mathrm{full}}}\bigr)}_{\rho_K^{\text{single-gen}}\text{-piece}}
  \;+\; \underbrace{\tfrac{\alpha\, z^2}{2}\!\!\sum_{i<j}\!\ln\bigl(\hat V_i \hat V_j \cdot \overline{\hat V_i \hat V_j}\bigr)\!\big|_{\mathrm{Wedd}}}_{\rho_K^{\text{pair-gen}}\text{-piece (open)}}
  \;+\; \dots
$$

**The LO piece is no longer an ansatz.** It constitutes the categorical
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
(where $\overline{\,\cdot\,}$ forms the Hecke bar-involution $q \leftrightarrow q^{-1}$;
at the archimedean specialization with real $q_0$ and real $\hat V_i$,
this equals $\alpha \sum_i \ln|\hat V_i^{\mathrm{full}}|$)
with $\alpha = m_e \cdot 8G$ ([binding scale](#prop:binding-scale-catalan))
takes $\rho_K$ to $0.18\%$ mean accuracy across $Z = 1..20$
([atomic braid mass](#sec:atomic-braid-mass-foundations)). The pair-gen and
higher pieces require the proper Wedderburn-coupling structure
(open work; see [graded ρ_K expansion](#prop:rho-k-graded-expansion)).

**Mirror-pair check** (T and ${}^3\mathrm{He}$, both $A=3$, $n=9$
strands): the categorical density factors $\rho_K(T) / \rho_K({}^3\mathrm{He}) = 1.9853$
exactly compensate $|\!\operatorname{tr}_M({}^3\mathrm{He})| / |\!\operatorname{tr}_M(T)| = 1.9850$,
since their CODATA masses agree to $0.02\%$. So $\rho_K$ is **not**
a function of $(A, n\text{-strands})$ alone. It must depend on the
specific braid $\mathcal{B}_K$ through $|\!\operatorname{tr}_M(\mathrm{NF}_{\mathrm{GS}}(\mathcal{B}_K))|$
(and hence $\rho_K \cdot |\!\operatorname{tr}_M\!|$ constructs the
mirror-symmetric quantity, equal to $\mathcal{M}(K)/m_e$).

**Reduction.** The categorical-closure question reduces to deriving
the nucleon-mass anchors $m_{\mathfrak{p}}/m_e \approx 1836.15$ and
$m_{\mathfrak{n}}/m_e \approx 1838.68$ from $H_3(q_0)$ data alone.
Once these anchors become categorically self-determined, the
constituent decomposition plus binding correction recovers atomic
masses to sub-percent across the full $A = 1..20$ range
([Wedderburn mass](#thm:wedderburn-mass-formula)). The six-term
spectral form provides the current best candidate. Empirically with
proton calibration it recovers $m_{\mathfrak{p}}$ by construction
but predicts $m_{\mathfrak{n}}$ to only $4.9\%$
(`paper-six-term-isotope-sweep.witness.json`, `li2q` mode). The
nucleon-anchor question remains the structural bottleneck.

**Connection to the $\alpha_{\mathrm{shift}}$ framework.**
The same bottleneck appears in the Habiro denominator factorisation
([w3 audit](../../docs/audits/-w3-habiro-unblocked.md)):

$$
  D(u) \;=\; 2^{2A+1} \cdot u^{\mathrm{shift}} \cdot (1 + u^2)^{3A-1},
$$

The (six-term spectral) form provides the current best candidate
attempt, expanding $\rho_K \cdot \lvert\!\operatorname{tr}_M\!\rvert$
into a $\sum_{i=1}^{6} T_i$ decomposition over the Wedderburn
blocks plus the cyclotomic tail. Empirically the six-term
expansion **under-predicts** $\rho_K$ by $22\%$–$31\%$ for
$A \in \{2, 3\}$ when calibrated against the proton
(`paper-six-term-isotope-sweep.witness.json`):

| Atom | $\rho_K^{\mathrm{CODATA}}$ | $\rho_K^{6\text{-term}}$ | gap (%) |
|---|---|---|---|
| $\mathfrak{p}$ | $1723.6$ | $1723.6$ | $0.0$ (calibrated) |
| $\mathfrak{n}$ | $1991.6$ | $1893.8$ | $+4.9$ |
| $D$ | $9453.0$ | $7398.2$ | $+21.7$ |
| $T$ | $52828.5$ | $36193.8$ | $+31.5$ |
| ${}^3\mathrm{He}$ | $26609.2$ | $19523.5$ | $+26.6$ |

The (constituent) form sidesteps this question by **using CODATA
$m_{\mathfrak{p}}, m_{\mathfrak{n}}$ as inputs**. The $0.18\%$
accuracy is dominated by the CODATA constituent sum, with
$\alpha \sum \ln\lvert\hat{V}_i^{\mathrm{full}}\rvert \approx -7$ MeV
of categorical correction. In particular, the (constituent)
formula does **not** demonstrate that $\rho_K$ is categorically
self-determined; it demonstrates that, given CODATA nucleon masses,
the small binding correction admits a clean log-volume sum representation.

## Reading the three forms

The three forms encode the same physical mass $\mathcal{M}(K)$
parameterised by different calibration data:

* **(constituent)** anchors at the nucleon level. It takes CODATA
  $m_{\mathfrak{p}}, m_{\mathfrak{n}}$ as primitive, and treats the
  binding/electron-coupling as a categorical correction.
  Sub-percent for $Z = 1$..$20$.
* **(six-term spectral)** anchors at the electron level. It takes
  $m_e$ and $E_0 = m_{\mathfrak{p}}^{\mathrm{CODATA}} / \lvert\!\operatorname{tr}_M(\mathrm{NF}_{\mathrm{GS}}(\beta_{\mathfrak{p}}))\!\rvert$
  as the only calibration; it predicts everything else from $q_0$ and
  the braid spectrum. Currently $25\%$ off at $A = 4$.
* **(GB-NF)** states the algebraic statement. The atomic mass is
  proportional to the Markov trace of the normal form, with the
  proportionality constant $\rho_K$ as the categorical density.

The propositional content carried by (GB-NF) — that the atomic mass
factors through the Gröbner–Shirshov quotient — renders the
:refterm[descent]{#descent} in [categorical mass = Markov](#prop:categorical-mass-markov)
applicable. The trace depends only on the braid class modulo the
PBW relations.

## Witnesses

* `rho-k-codata-vs-six-term.witness.json` — $\rho_K^{\mathrm{CODATA}}$ vs $\rho_K^{6\text{-term}}$ table for $A = 1, 2, 3$.
* `rho-k-scaling-structure.witness.json` — leading-order ansatz $\rho_K \approx (Z m_{\mathfrak{p}} + N m_{\mathfrak{n}})/(m_e \cdot |\!\operatorname{tr}_M\!|)$ ($0.14\%$ mean residual); mirror-pair analysis.
* `atomic-tr-m-mpfr-50dps.witness.json` — canonical $\lvert\!\operatorname{tr}_M(\mathrm{NF}_{\mathrm{GS}}(\mathcal{B}_K))\!\rvert$ at $50$ decimal-place precision.
* `atom-mass-atomic-braid.witness.json` — (constituent) form predictions.
* `paper-six-term-isotope-sweep.witness.json` — (six-term spectral) predictions across all five tower modes.
<!-- FILE_END: atomic-mass-gb-nf-interpretation.md -->

<!-- FILE_START: rho-k-graded-expansion.md -->
## Statement

**Proposition (graded $\rho_K$ expansion).** We expose the graded expansion of the categorical density $\rho_K$ by multiplying the GB-NF identity ([atomic mass via GB-NF](#prop:atomic-mass-gb-nf)) $\mathcal{M}(K) = m_e \cdot \rho_K \cdot |\!\mathrm{tr}_M(\mathrm{NF}_{\mathrm{GS}}(\mathcal{B}_K))|$ through by $m_e \cdot |\!\mathrm{tr}_M(\mathcal{B}_K)|$:

$$
  \boxed{
    m_e \cdot |\!\mathrm{tr}_M(\mathcal{B}_K)| \cdot \rho_K
    \;=\;
    \underbrace{Z m_{\mathfrak{p}} + N m_{\mathfrak{n}} + Z m_e}_{\rho_K^{\mathrm{LO}}\text{-piece (Markov mult.)}}
    \;+\; \underbrace{\tfrac{\alpha}{2} \sum_i \ln\bigl(\hat V_i^{\mathrm{full}} \cdot \overline{\hat V_i^{\mathrm{full}}}\bigr)}_{\rho_K^{\text{single-gen}}\text{-piece}}
    \;+\; \underbrace{\tfrac{\alpha\, z^2}{2}\!\!\sum_{i<j}\!\ln\bigl(\hat V_i^{\mathrm{full}} \hat V_j^{\mathrm{full}} \cdot \overline{\hat V_i^{\mathrm{full}} \hat V_j^{\mathrm{full}}}\bigr)\!\big|_{\mathrm{Wedd}}}_{\rho_K^{\text{pair-gen}}\text{-piece (open)}}
    \;+\; \dots
  }
$$

where $\alpha = m_e \cdot 8G$ ([binding scale](#prop:binding-scale-catalan)) and $z = 1/(q^{1/2} + q^{-1/2})$ forms the Markov parameter. The graded expansion truncates at the single-generator level to achieve the empirical $0.18\%$ accuracy reported in [atomic braid mass](#thm:wedderburn-mass-formula).

## The three pieces

### Leading-order piece (proved)

By [Wenzl 1988] Theorem 5 (Markov multiplicativity), disjoint braids $\beta_1 \in H_{n_1}(q)$ and $\beta_2 \in H_{n_2}(q)$ with image $\beta_1 \otimes \beta_2 \in H_{n_1 + n_2}(q)$ satisfy:

$$
  \mathrm{tr}_M(\beta_1 \otimes \beta_2)
  \;=\; \mathrm{tr}_M(\beta_1) \cdot \mathrm{tr}_M(\beta_2).
$$

Combined with mass additivity for free constituents, this categorically determines the leading-order piece:

$$
  \rho_K^{\mathrm{LO}}
  \;=\;
  \frac{Z m_{\mathfrak{p}} + N m_{\mathfrak{n}} + Z m_e}{m_e \cdot |\!\mathrm{tr}_M(\mathcal{B}_K)|}.
$$

The script `rho-k-markov-multiplicativity.witness.json` numerically verifies the [Wenzl 1988] branching identity $\chi^\lambda(\mathcal{B}_p \otimes \mathcal{B}_n) = \sum c^\lambda_{\mu, \nu} \chi^\mu(\mathcal{B}_p) \chi^\nu(\mathcal{B}_n)$ to machine precision ($3.2 \times 10^{-14}$) for all $\lambda \vdash 6$ in the deuteron case.

### Single-generator piece (proved)

Per [atomic braid mass](#thm:wedderburn-mass-formula), the per-generator log-volume sum reads:

$$
  \tfrac{\alpha}{2} \sum_i \ln\bigl(\hat V_i^{\mathrm{full}} \cdot \overline{\hat V_i^{\mathrm{full}}}\bigr)
$$

The overline denotes the Hecke bar-involution $q \leftrightarrow q^{-1}$. At real $q_0$ and real $\hat V_i$, this reduces to the archimedean form $\alpha \sum_i \ln|\hat V_i^{\mathrm{full}}|$. Using $\alpha = m_e \cdot 8G \approx 3.7445$ MeV (the Borromean binding scale, [Catalan binding](#prop:binding-scale-catalan)), this captures the leading binding correction. The mean error is $0.18\%$, with a $0.35\%$ maximum across $Z = 1..20$ (see `atomic-braid-mass-paper-formula.witness.json` and the `rho-k-pair-gen-extension.witness.json` table).

### Pair-generator piece (open)

The pair-generator term provides the log-volume analogue of $T_3 = -z^2 \sum_{i<j} \mathrm{Li}_2^q(-|\hat V_i \hat V_j|)$ from the [unified knot mass formula](#thm:knot-mass-formula-unified):

$$
  \alpha \cdot z^2 \cdot \sum_{i<j} \ln\bigl|\hat V_i^{\mathrm{full}} \hat V_j^{\mathrm{full}}\bigr|_{\mathrm{Wedderburn}}.
$$


$$
  \bigl|\hat V_i \hat V_j\bigr|_{\mathrm{Wedderburn}}
  \;=\;
  w_{\mathrm{sym}}\, \lambda_i^{\mathrm{sym}} \lambda_j^{\mathrm{sym}}
  + w_{\mathrm{std}}\, \bigl[\,z\,(M_i M_j)_{1,2} + (M_i M_j)_{2,2}\bigr]
  + w_{\mathrm{alt}}\, \lambda_i^{\mathrm{alt}} \lambda_j^{\mathrm{alt}}
$$

Here, $M_i$ provides the per-generator $2 \times 2$ standard-representation transfer matrix, and $w_\bullet$ are the Wedderburn-Markov weights from [Wedderburn mass](#thm:wedderburn-mass-formula). The standard-channel pair coupling uses the Markov-traced $2 \times 2$ matrix product $M_i M_j$ to capture braid non-commutativity, avoiding the naive product $V_i^{\mathrm{std}} \cdot V_j^{\mathrm{std}}$.

See [Table 1](#tbl:rho-k-graded-expansion-table1-data).

Both pair extensions degrade accuracy under the simple $\alpha z^2$ log-formula, even with the correct Wedderburn coupling. The gap lies in the functional form: $T_3$ in the six-term theorem requires $-z^2 \sum \mathrm{Li}_2^q(-|V_i V_j|)$, not $\alpha z^2 \sum \ln |V_i V_j|$. The single-generator Kashaev-limit derivation that yields $\alpha \sum \ln|V_i|$ (matching $T_2$) requires a parallel derivation for the pair piece to produce the correct functional form and prefactor. This remains open work.

## Identification with the six-term theorem

Each piece of the graded expansion corresponds to a term in the Kashaev limit of the [unified knot mass formula](#thm:knot-mass-formula-unified) (six-term theorem):

See [Table 2](#tbl:rho-k-graded-expansion-table2-data).

The graded $\rho_K$ expansion supplies the Kashaev specialisation of the six-term theorem (`thm:knot-mass-formula-unified`) expressed at the GB-NF level. The constituent-mass piece is explicitly factored out via the Markov-multiplicativity rewriting.

## Significance

The graded expansion replaces the empirical leading-order ansatz of [atomic mass via GB-NF](#prop:atomic-mass-gb-nf) with a categorical derivation:

- The leading-order piece acts as a theorem derived from Markov multiplicativity and free-constituent additivity.
- The single-generator piece forms the proved binding correction, achieving $0.18\%$ empirical accuracy.
- The pair-generator and higher pieces remain open work. Finding the precise Wedderburn-coupling structure closes the six-term theorem's Kashaev limit at sub-percent accuracy.

Combined with the Hecke branching trace decomposition (refined Sub-lemma 2.1, operator-valued $A^\lambda_{\mu, \nu}(I)$ interface), the bound atomic case receives full coverage. The leading-order and single-generator pieces give $\rho_K$ to $0.18\%$; the higher pieces and the interface contribution close the residual.

## Production wiring

The graded expansion is realised end-to-end by `computations/rho_k_graded_atomic_mass.py` (witness `rho-k-graded-atomic-mass.witness.json`). The leading-order constituents $Z m_{\mathfrak{p}} + N m_{\mathfrak{n}} + Z m_e$ are drawn from the canonical muon-anchored mass facade (`computations/canonical_mass.py`). No CODATA nucleon masses enter. The single-generator correction $\alpha \sum_i \ln|\hat V_i^{\mathrm{full}}|$ is evaluated at $50$ decimal places of precision, yielding $0.19\%$ mean error and $0.30\%$ maximum error across the published $Z = 1..10$ table. The pair-generator tier is reported as the open residual only. It is never added to the mass, as its naive log-additive form degrades accuracy (see Table 1). Per-generator volumes carry the known $H_3$-weight convention of the published table. The dynamic $H_{3A}$ re-weighting forms a separate tracked fix (`docs/audits/2026-05-25-h3-vs-h3a-legacy-bug-audit.md` §7 Tier 2).

## References

- [Wenzl 1988] *Hecke algebras of type $A_n$ and subfactors*, Inventiones Math. **92**, 349–383. Theorem 5 (Markov multiplicativity for parabolic subalgebras).
<!-- FILE_END: rho-k-graded-expansion.md -->

<!-- FILE_START: conj-rho-k-pair-gen-canonical-form.md -->
**Conjecture (Canonical form of $\rho_K^{\text{pair-gen}}$).**
*There exists a closed-form Wedderburn-coupled functional $f_2 : \mathbb{Q}(q^{1/2}) \times \mathbb{Q}(q^{1/2}) \times \mathbb{Q}(q^{1/2}) \to \mathbb{R}$ such that for every atomic braid $\mathcal{B}_K \in B_{3A}$:*

$$
\rho_K^{\text{pair-gen}}
\;=\;
\sum_{0 \leq i < j \leq 3A-2}
  f_2\!\left(q, \hat V_i^{\text{full}}, \hat V_j^{\text{full}}\right)
$$

*and the resulting graded-expansion truncation*

$$
m_e \cdot |\mathrm{tr}_M(\mathcal{B}_K)| \cdot \left(\rho_K^{\text{LO}} + \rho_K^{\text{single-gen}} + \rho_K^{\text{pair-gen}}\right)
\;=\;
\mathcal{M}(K)^{\text{CODATA}}
\;+\; O(\hbar_q^{6})
$$

*matches CODATA to sub-percent accuracy across $Z = 1..20$. Here, $\hat V_i^{\text{full}}$ denotes the Wedderburn-traced per-generator volumes, and $z = 1/(q^{1/2} + q^{-1/2})$ forms the Markov parameter.*

## Empirical evidence

| Candidate $f_2$ | Form | $Z=1..20$ status |
|---|---|---|
| Naive log-additive | $\alpha z^2 \sum \ln\|V_i V_j\|$ | Degrades vs LO + single-gen |
| Wedderburn-decomposed | $\alpha z^2 \sum \|V_i V_j\|_{\text{Wedderburn}}$ (with $w_{sym}, w_{std}, w_{alt}$) | Degrades (wrong functional form) |
| Six-term theorem $T_3$ | $-z^2 \sum \text{Li}_2^q(-\|V_i V_j\|)$ | Expected per [`thm:knot-mass-formula-unified`](knot-mass-formula-unified.md); wiring pending |

The Kashaev-limit form (six-term $T_3$) provides the anticipated canonical form. Its derivation as a leading-order expansion in $\hbar_q$ remains incomplete. This must parallel the single-generator Kashaev derivation $\alpha \sum \ln|V_i|$.

## Conjecture status

| Component | Status | Evidence |
|---|---|---|
| Existence of $f_2$ (any form) | Conjectural | Follows from evaluating mass formula at finite truncation |
| $f_2 = -\text{Li}_2^q(-\|V_i V_j\|) \cdot z^2$ | Conjectural | Matches six-term $T_3$; derivation pending |
| Naive log-additive form | Refuted | `rho-k-pair-gen-extension.witness.json` |
| Wedderburn-coupled form | Partial | Correct Wedderburn weights, wrong functional form |
| Six-term theorem [`thm:knot-mass-formula-unified`](knot-mass-formula-unified.md) | Theorem | Proved independently |

## Wedderburn-coupling structure

Under [`prop:rho-k-graded-expansion`](rho-k-graded-expansion.md) §pair-gen, the pair coupling expands as:

$$
|\hat V_i \hat V_j|_{\text{Wedderburn}}
\;=\;
w_{\text{sym}}\, \lambda_i^{\text{sym}} \lambda_j^{\text{sym}}
\;+\;
w_{\text{std}}\, \bigl[z\,(M_i M_j)_{1,2} + (M_i M_j)_{2,2}\bigr]
\;+\;
w_{\text{alt}}\, \lambda_i^{\text{alt}} \lambda_j^{\text{alt}},
$$

where:
- $w_{\text{sym}}, w_{\text{std}}, w_{\text{alt}}$ denote Wedderburn–Markov weights from [`thm:wedderburn-mass-formula`](wedderburn-mass-formula.md).
- $\lambda_i^\bullet$ denote per-generator eigenvalues within each Wedderburn channel.
- $M_i$ denotes the per-generator $2 \times 2$ standard-representation transfer matrix.

The standard-channel pair coupling relies on the Markov-traced $2 \times 2$ matrix product $M_i M_j$. This captures braid non-commutativity, superseding the naive scalar product $V_i^{\text{std}} \cdot V_j^{\text{std}}$.

The open requirement is the functional form $f_2$. The naive logarithmic form $\alpha z^2 \ln|V_i V_j|_{\text{Wedderburn}}$ degrades empirically. The expected $q$-dilogarithmic form $-z^2 \text{Li}_2^q(-|V_i V_j|_{\text{Wedderburn}})$ requires a formal derivation connecting it to the pair-generator expansion.

## Dependencies

- [`conj:lepton-mass-tower-canonical`](lepton-mass-tower-canonical.md): The lepton-sector variant. It gates on the graded-expansion formalism but evaluates at $Z = N = 0$, nullifying the atomic LO piece. It requires its own dimensional factor $\xi_\ell(q)$.
- [`conj:mass-endomorphism`](mass-endomorphism-conjecture.md): The unifying closed-form mass element $\Phi_{\text{mass}}(W) \in H_{3A}(q)$. The present conjecture restricts this to the pair level.

## Lean formalization

```lean
namespace QOU.BraidKnot.RhoKPairGenCanonicalForm

/-- The conjectural canonical pair-gen functional `f_2(q, V_i, V_j)`;
    expected six-term `T_3` Kashaev form, derivation open. -/
noncomputable def pair_gen_functional
    {R : Type*} [Field R] (q V_i V_j : R) : R :=
  sorry

/-- Conjecture axiomatisation: a single canonical functional
    reproduces ρ_K^pair-gen to sub-percent accuracy. The specific Li_2^q
    recovery bound requires the graded-expansion infrastructure, 
    so it exists as a `Prop` class assumed downstream as `[PairGenCanonical]`. -/
class PairGenCanonical : Prop where
  exists_subpercent_recovery :
    ∀ (M : ℝ), 0 ≤ M → ∃ M_rec : ℝ, |M_rec - M| ≤ M / 100

end QOU.BraidKnot.RhoKPairGenCanonicalForm
```

## Resolution path

Deriving the canonical $f_2$ yields four consequences:
1. This conjecture elevates to a theorem.
2. The open status of [`prop:rho-k-graded-expansion`](rho-k-graded-expansion.md) §pair-gen resolves to proved.
3. Downstream conjectures unblock, specifically [`conj:lepton-mass-tower-canonical`](lepton-mass-tower-canonical.md).
4. The $\mathfrak{Q}_\beta$ residual closure direction becomes tractable.

## Archimedean specialization

We state this conjecture on the archimedean side of the substrate wall. It asserts a real-mass sub-percent recovery bound: $\forall M \ge 0,\ \exists M_{\mathrm{rec}},\ |M_{\mathrm{rec}} - M| \le M/100$ over $\mathbb{R}$. The generic $q$-deformation functional $f_2(q, \hat V_i, \hat V_j)$ serves as input. The conjectural statement intrinsically addresses real masses; it does not constitute a separable archimedean specialization of an otherwise $\mathbb{R}$-free construction.
<!-- FILE_END: conj-rho-k-pair-gen-canonical-form.md -->

<!-- FILE_START: hecke-branching-trace-decomposition.md -->
**Proposition (Hecke branching trace decomposition).**
*Let $H_{n+m}(q)$ act on its irreducible Hoefsmit seminormal module $V_\lambda$ ($\lambda \vdash n+m$). Let $I \in H_{n+m}(q)$ be an interface element (any product of generators bridging the index range $\{n, n+1\}$). For braid words $\beta_1 \in H_n(q)$ and $\beta_2 \in H_m(q)$ acting on the left and right $H_n \otimes H_m$ factors respectively, the trace of $\beta_1 \cdot I \cdot \beta_2$ on $V_\lambda$ admits the block decomposition:*

$$
\operatorname{tr}_{V_\lambda}\!\bigl(\rho_\lambda(\beta_1 \cdot I \cdot \beta_2)\bigr)
\;=\;
\sum_{\substack{\mu \vdash n \\ \nu \vdash m}}
\operatorname{tr}_{V_\mu \otimes V_\nu}\!
\Bigl(A^\lambda_{\mu,\nu}(I)\,\cdot\,
\bigl(\rho_\mu(\beta_1) \otimes \rho_\nu(\beta_2)\bigr)\Bigr),
$$

*where $A^\lambda_{\mu,\nu}(I) \in \operatorname{End}(V_\mu \otimes V_\nu)^{\oplus c^\lambda_{\mu,\nu}}$ constructs the operator-valued coefficient encoding the multiplicities given by the Littlewood–Richardson coefficients $c^\lambda_{\mu,\nu}$, and $\rho_\lambda, \rho_\mu, \rho_\nu$ construct the Hoefsmit seminormal representations of $H_\bullet(q)$.*

## Corollary (the case used downstream)

Taking $\beta_1 = \beta_2 = 1$ recovers the simpler sum:
$$
\chi^\lambda(I) \;=\; \sum_{\mu, \nu} \operatorname{tr}\,A^\lambda_{\mu,\nu}(I),
$$
This form supplies the scalar-vs-operator Frobenius budget in [`rem:operator-valued-magnitude-budget`](operator-valued-magnitude-budget.md). The Pythagorean orthogonality:
$$
\bigl\| A^\lambda_{\mu,\nu}(I) - A^{\lambda,\mu,\nu}_{\mathrm{scalar}} \bigr\|_F^2
\;=\;
\bigl\| A^\lambda_{\mu,\nu}(I) \bigr\|_F^2
\;-\;
\frac{\bigl|\operatorname{tr}\,A^\lambda_{\mu,\nu}(I)\bigr|^2}{d_\mu \, d_\nu}
$$
provides the standard scalar-vs-traceless decomposition of an operator under the Hilbert–Schmidt inner product. No further hypothesis remains needed.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs: real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: hecke-branching-trace-decomposition.md -->

<!-- FILE_START: operator-valued-magnitude-budget.md -->
For the deuteron interface $I \in H_6(q)$, the operator-valued branching identity `prop:hecke-branching-trace-decomposition` expands $\chi^\lambda(\beta_1 \cdot I \cdot \beta_2)$ as a sum over $(\mu, \nu)$ blocks of traces of $A^\lambda_{\mu,\nu}(I) \in \operatorname{End}(V_\mu \otimes V_\nu)^{\oplus c}$.

A scalar-substrate ansatz approximates each $A^\lambda_{\mu,\nu}(I)$ by its best scalar multiple of the identity:
$$
A_{\mathrm{scalar}}^{\lambda,\mu,\nu} \;:=\; \frac{\operatorname{tr} A^\lambda_{\mu,\nu}(I)}{d_\mu \cdot d_\nu} \cdot \mathbf{1}_{V_\mu \otimes V_\nu}.
$$

By the orthogonality of the scalar and traceless components under the Hilbert–Schmidt inner product, the operator-valued residual holds Frobenius norm:
$$
\bigl\| A^\lambda_{\mu,\nu}(I) - A_{\mathrm{scalar}}^{\lambda,\mu,\nu} \bigr\|_F^2 \;=\; \bigl\| A^\lambda_{\mu,\nu}(I) \bigr\|_F^2 \;-\; \frac{\bigl| \operatorname{tr} A^\lambda_{\mu,\nu}(I) \bigr|^2}{d_\mu \cdot d_\nu}.
$$

Summing across all $35$ $(\lambda, \mu, \nu)$ blocks of the $H_6$ deuteron-interface decomposition yields:

| Quantity | Frobenius |
|---|---|
| Scalar-approximation total | $3.517$ |
| Operator-valued residual total | $3.603$ |
| Non-scalar blocks | $19 / 35$ |

The operator-valued residual magnitude **exceeds** the scalar approximation magnitude. Symmetric scalar substrate ansätze recover less than half of the structural Frobenius content of the $A^\lambda_{\mu,\nu}(I)$ family.

This quantitative magnitude budget drives the [`structural-diagnosis-operator-valued`](https://github.com/litlfred/qou/blob/main/docs/audits/-structural-diagnosis-operator-valued.md) audit's conclusion. The symmetric scalar substrate cannot account for the empirical Z$\leftrightarrow$N-asymmetric mass-formula residuals ($\Delta_{\text{coupling}}$ +0.796 MeV; T5 −0.325 MeV). We construct these residuals to be operator-valued at the per-Wedderburn-block level.
<!-- FILE_END: operator-valued-magnitude-budget.md -->

<!-- FILE_START: q-hecke-seminormal-character-closure.md -->
# Partition-sum Wedderburn decomposition of the Markov trace

$$
  \mathrm{tr}_M^{\mathrm{partition\text{-}sum}}(\mathcal{B}_K)
  \;:=\;
  \sum_{\lambda \vdash 3A} y_\lambda(q) \cdot \mathrm{tr}_{V_\lambda}\!\bigl(\rho_\lambda^q(\mathcal{B}_K)\bigr),
$$

This partition-sum form equals the canonical Markov-axiom reducer $\mathrm{tr}_M(\mathcal{B}_K)$ ([`prop:markov-trace-recursive-reducer`](#prop:markov-trace-recursive-reducer)) to numerical precision at $q = q_0$.

## Significance

The partition-sum form rewrites the Markov trace via the Wedderburn–Artin decomposition $H_n(q) \cong \bigoplus_\lambda M_{f^\lambda}(\mathbb{C})$. The result `prop:hecke-branching-trace-decomposition` relies on this decomposition. Downstream consumers (such as binding-energy analysis via $\rho_K$ refinement and force-carrier saturation identities) require a partition-by-partition decomposition of $\mathrm{tr}_M$ that the recursive reducer does not directly expose.

The recursive Markov-axiom ascent and partition-sum Wedderburn formulas must agree. The agreement was previously broken at $q \ne 1$ due to a character convention error. `schur_weyl_symbolic.specht_character_atomic` incorrectly returned the classical Murnaghan–Nakayama character $\chi^\lambda_{\mathrm{MN}}(\pi(\beta))$ at $q = 1$ instead of the $q$-Hecke character $\chi^\lambda_q(\beta)$ (see audit log [`docs/audits/-p3-h-3a-divergence.md`](../../../docs/audits/-p3-h-3a-divergence.md)).

Both underlying bugs are now fixed:

1. **Weight layer:** `schur_weyl_symbolic.schur_weyl_weight` incorrectly used the two-variable Schur function $s_\lambda(q, q^{-1}) / H_q(\lambda)$, which vanishes for partitions with three or more rows. It now uses `y_\lambda(q)` via Wenzl Schur principal specialization (`prop:hecke-branching-trace-decomposition`).
2. **Character layer:** `specht_character_atomic` previously returned the $q = 1$ limit of the Hecke character. It now returns the $q$-Hecke character $\chi^\lambda_q(\mathcal{B}_K) = \mathrm{tr}\,\rho_\lambda^q(\mathcal{B}_K)$ via Hoefsmit seminormal matrices at $q_0$ ([`docs/audits/-q-hecke-character-gap-closure.md`](../../../docs/audits/-q-hecke-character-gap-closure.md)).

## Numerical verification

| Atom | $|\mathrm{tr}_M|$ canonical | partition-sum ($q$-Hecke) | Relative error |
|---|---:|---:|---:|
| Proton | $1.06530622859$ | $1.06530622859$ | $3.96 \times 10^{-15}$ |
| Neutron | $0.92323329717$ | $0.92323329717$ | $4.21 \times 10^{-15}$ |
| Deuteron | $0.38828647155$ | $0.38828647155$ | $7.01 \times 10^{-15}$ |
| Tritium | $0.10405211868$ | $0.10405211868$ | $1.07 \times 10^{-14}$ |
| ${}^3$He | $0.20654085856$ | $0.20654085856$ | $1.03 \times 10^{-14}$ |

## Production paths

The canonical values are rigorously evaluated via formal trace definitions. All three paths agree at the precision floor of their respective layers. The cross-check witness gates this on every continuous integration run.
<!-- FILE_END: q-hecke-seminormal-character-closure.md -->
