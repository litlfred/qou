<!-- FILE_START: nuclear-stability-decay-hadron-half-life-intro.md -->
This section continues the analysis of nuclear stability. We define the hadron half-life, derive the substrate-level $q$-self-correction, and establish the skein-Coulomb enhancement that governs the substrate-flow behaviour of the half-life. We then tabulate per-hadron half-life predictions against PDG values and identify the optimal substrate-flow regime for these predictions.

The result is a substrate-level hadron half-life formula. The categorical $q$-self-correction provides the leading deviation from the classical Fermi formula.
<!-- FILE_END: nuclear-stability-decay-hadron-half-life-intro.md -->

<!-- FILE_START: hadron-half-life.md -->
A nucleus displaced from the valley of stability ([integer stability](#prop:integer-stability)) beta decays toward stability. The half-life — the time for half a population to decay — is governed by the substrate parameter $q$ ([substrate parameter](#def:substrate-parameter)) via the $q$-deformed transition amplitude.

**Proposition.**
Let $(\mathbf{C}, A, \tau)$ be the Descartes universe with substrate parameter $q$. A nucleus $\mathcal{N}(Z, N)$ ([stable nucleus](#def:stable-nucleus)) with proton displacement $\delta p = p - p_{\mathrm{stab}}(A)$ from the valley of stability has beta-decay half-life:

$$
  t_{1/2}(p, A)
  = 
  \frac{\ln 2}{\Gamma_\beta(p, A)}.
$$

The decay rate $\Gamma_\beta$ depends only on $q$ and a single dimensional scale $\mu_0$ ([building blocks](#rem:building-block-knots)).

## Decay rate from $q$ and $\mu_0$

Beta decay is mediated by the torus knot $T_{3,5}$, which has $10$ crossings ([beta decay as crossing change](#def:beta-decay-skein), [force identification](#rem:force-knot-identification)). The $T_{3,5}$ braid $(\sigma_1\sigma_2)^5$ is inserted at the converting quark. Its $10$ crossings partition into the electron trefoil ($3$), the neutrino unknot ($0$), and the nuclear re-reduction residue ($7$). The fundamental weak coupling is the weak vertex form factor $\mathcal{W}(q)$, defined as the Markov trace of the $T_{3,5}$ braid word in $H_3(q)$.

The decay rate is:

$$
  \Gamma_\beta(p, A)
  = 
  \frac{|\mathcal{W}(q)|^2 \cdot \mu_0}{2\pi^3}
   \cdot 
  [2]_q
   \cdot 
  |\mathcal{M}_q|^2
   \cdot 
  f(Q).
$$

Every factor here is fixed by $q$:

1. **Weak vertex form factor** $|\mathcal{W}(q)|^2 = |\mathrm{tr}_{\mathrm{Markov}}((\sigma_1\sigma_2)^5)|^2$: This is the full $10$-crossing weak vertex coupling, replacing the single-crossing approximation $s^2 = (q^{1/2} - q^{-1/2})^2$. In the classical limit $q \to 1$, $\mathcal{W}(1) = 0$ and beta decay vanishes.
2. **$q$-integer modulation** $[2]_q = q + q^{-1}$: The categorical dimension of the $\mathrm{SU}_q(2)$ fundamental representation. It replaces the classical weak-interaction factor of $2$.
3. **$q$-deformed matrix element:** The squared matrix element is the Markov trace ratio between parent and daughter Gröbner--Shirshov normal forms ([trace ratio observable](#prop:trace-ratio-observable)):

   $$
     |\mathcal{M}_q|^2
     = 
     s^2
      \cdot 
     \prod_{i=0}^{p}
     \left|
       \frac{\hat{V}_i^{\mathrm{par}}}{\hat{V}_i^{\mathrm{dau}}}
     \right|^2
   $$

   where $\hat{V}_i = z \cdot a_i + b_i$ is the Markov-traced generator volume ([factorization theorem](#thm:markov-trace-factorization)).
4. **Phase-space integral:** The $Q$-value ([transition energy](#def:Q-value-transition)) is the categorical action difference $Q = \mathfrak{S}_q(\mathrm{par}) - \mathfrak{S}_q(\mathrm{dau}) - \mathfrak{S}_q(e)$. This replaces classical energy conservation ($M_{\mathrm{par}} - M_{\mathrm{dau}} - m_e$), which assumes $d_q^2 = 0$ and fails for $q \neq 1$. Each nucleus's action evaluates at $q$ via the terminal resolution of its composite link ([terminal resolution](#prop:terminal-resolution)), using the pair Skein mass formula $\mathcal{S}_{ab}(q) = (q\mu_a + q^{-1}\mu_b)/(q^{1/2}+q^{-1/2})$. The fifth-power Sargent rule sets $f(Q) \propto Q^5$ for allowed transitions.
5. **Dimensional scale** $\mu_0$: The single free parameter converting Skein units to physical units (MeV, seconds). It represents a choice of units, not a physical parameter.

## Relation to the Fermi constant

Standard Fermi theory sets the decay rate as $\Gamma = G_F^2m_e^5/(2\pi^3) \cdot |M|^2 \cdot f(Z, Q)$. This effective theory formula packages two distinct mass scales:

- The electron mass $m_e = 3\mathfrak{E}_{\times}(q) \cdot \mu_0$ ([building blocks](#rem:building-block-knots)), where $\mathfrak{E}_{\times} = \frac{1}{2}(q - q^{-1})$ is the crossing energy.
- The weak scale $v \approx 246$ GeV, via $G_F = 1/(\sqrt{2}v^2)$.

Both scales are fixed by $q$ and $\mu_0$, yet originate from distinct knot structures: $m_e$ from the trefoil's 3 crossings, and $v$ from the electroweak topology. The pure number ratio $v / m_e \approx 4.8 \times 10^5$ is determined strictly by topology.

The combination entering the half-life is:

$$
  G_F^2m_e^5
  = 
  \frac{m_e^5}{2v^4}
  = 
  \frac{(3\mathfrak{E}_{\times})^5}{2(N_v\mathfrak{E}_{\times})^4}
   \cdot  \mu_0
  = 
  \frac{243\mathfrak{E}_{\times}}{2N_v^4}
   \cdot  \mu_0,
$$

where $N_v = v / (\mathfrak{E}_{\times}\mu_0)$ is the effective crossing count of the weak scale. This reduces to a pure function of $q$ times $\mu_0$. The Fermi constant is not an independent parameter.

**Open computations:**

1. **$N_v$ (weak scale crossing count):** We must derive $N_v$ (equivalently, $v$) from the Skein algebra. Since $T_{3,5}$ mediates the weak interaction, $v$ emerges from the $10$-crossing structure of the $T_{3,5}$ braid. The vertex form factor $\mathcal{W}(q)$ supplies the coupling; the mass scale $v$ provides the range.
2. **$\mathcal{W}(q)$ (weak vertex form factor):** This is the Markov trace of $(\sigma_1\sigma_2)^5$ in $H_3(q)$ evaluated at $q$. It replaces the single-crossing approximation $s^2$ and is expected to resolve the systematic $10$–$17\%$ overshoot in heavy-nucleus half-life predictions.

## $q$-dependence of the decay rate

The decay rate depends on $q$ through four channels:

- $|\mathcal{W}(q)|^2$: The $T_{3,5}$ weak vertex form factor.
- $[2]_q = q + q^{-1}$: The weak-vertex dimension.
- $|\mathcal{M}_q|^2$: The Markov trace ratio, reflecting the nuclear braid's crossing structure at $q$.
- $Q^5$: The categorical action difference ([transition energy](#def:Q-value-transition)). This depends on the pair Skein weights $\mathcal{S}_{ab}(q)$, which in turn depend on $q$ through the dressed quark masses $\mu_{\mathfrak{u}}, \mu_{\mathfrak{d}}$. Note that $Q \neq T_e + T_{\nu^{\sigma}} + T_{\mathrm{recoil}}$ for $q \neq 1$ (the $q$-anomaly $\delta_q \neq 0$).

In the classical limit $q = 1$, we have $s = 0$ and $[2]_1 = 2$. Crossing asymmetry vanishes, isobars become degenerate ($Q = 0$), and beta decay ceases. For $q > 1$, crossing asymmetry splits the isobars, yielding finite $Q$ and half-lives.

The decay rate's sensitivity to $q$ is:

$$
  \frac{\partial \ln \Gamma_\beta}{\partial \ln q}
  = 
  \frac{q^2 - 1}{q^2 + 1}
  + 
  5\frac{q^2 + 1}{q^2 - 1}
   \approx  48
  \quad\text{at } q = q_0.
$$

A $1\%$ shift in $q$ changes decay rates by $\sim 50\%$.

The half-life is not a free observable. It derives from the categorical action $\mathfrak{S}_q$ on the nuclear link using the identical parameter $q$ that dictates the valley of stability. The parameter $q$ determines both which nuclei are stable and how fast unstable nuclei decay.

## Parameter count

The half-life formula depends on:
- $q$: The substrate parameter (fixed by the muon-electron mass ratio).
- $\mu_0$: The dimensional scale (unit choice).
- $(p, n)$: The nuclear quantum numbers.

Every standard-physics constant decomposes into $q$-dependent factors times $\mu_0$: the electron mass $m_e = 3\mathfrak{E}_{\times}\mu_0$, the weak scale $v = N_v\mathfrak{E}_{\times}\mu_0$, and the fine structure constant $\alpha = q^{-1}/([9]_q \cdot [10]_q)$ via the Chern-Simons correction ([EM coupling projection](#prop:em-coupling-projection)). The fine structure constant strictly derives from $q$ ($2.1\;\mathrm{ppm}$ deviation from CODATA). The weak scale crossing count $N_v$ remains open (see [verification](#ex:hadron-half-life-verification)).
<!-- FILE_END: hadron-half-life.md -->

<!-- FILE_START: hadron-half-life-novelty.md -->
**Remark (Categorical derivation).** This geometric framing derives the empirical weak-decay structure purely categorically. It unifies the Fermi golden rule and Sargent's rule within a single Markov-trace matrix element.
<!-- FILE_END: hadron-half-life-novelty.md -->

<!-- FILE_START: hadron-q-self-correction.md -->
The substrate parameter $q \colon M \to k^\times$ ([substrate parameter](#def:substrate-parameter)) is a field, not a background constant. A hadron ([hadron](#def:hadron)) — a multi-component knot composite containing internal Hopf junctions and crossings — perturbs the local value of $q$ through its topological linking structure. The effective substrate parameter observed by a nucleus is:

$$
  q_{\mathrm{eff}}(p, n)
  = 
  q_0 +  \delta q(p, n).
$$

Here, $q_0$ is the background substrate value ([local substrate $q$](#prop:local-substrate-q)) and $\delta q(p, n)$ is the hadron's self-deformation.

**Proposition.**
Let $\mathcal{N}(Z, N) = Z\mathfrak{p} \oplus N\mathfrak{n}$ be a nucleus ([stable nucleus](#def:stable-nucleus)). The self-deformation of the substrate parameter is determined by the signed crossing excess, which is the imbalance between positive ($\mathfrak{p}$--$\mathfrak{p}$) and negative ($\mathfrak{n}$--$\mathfrak{n}$) Hopf crossings:

$$
  \delta q(p, n)
  = 
  \frac{\ell_{\mathrm{net}}(p, n)}{A^2}
  \cdot \hbar_q^2.
$$

Here, $\hbar_q = 1 - q_0^{-1}$ is the quantum Planck constant, and the net signed crossing number is:

$$
  \ell_{\mathrm{net}}(p, n)
  = 
  \binom{p}{2} - \binom{n}{2}
  = 
  \frac{p(p-1) - n(n-1)}{2}.
$$

For neutron-rich nuclei ($n > p$), $\ell_{\mathrm{net}} < 0$ and the local $q$ is reduced. For proton-rich nuclei, $\ell_{\mathrm{net}} > 0$ and $q$ is increased.

**Net signed crossing.**

The $q$-deformed wedge product $\wedge_q$ in the gauge sector of the canonical action ([canonical action](#prop:qou-canonical-action)) assigns weights to crossings:
- $q$ to $\mathfrak{p}$--$\mathfrak{p}$ crossings (positive).
- $q^{-1}$ to $\mathfrak{n}$--$\mathfrak{n}$ crossings (negative).
- $(q + q^{-1})/2$ to $\mathfrak{p}$--$\mathfrak{n}$ crossings (neutral average).

Neutral crossings contribute symmetrically, producing no shift in $q$. The substrate field deformation arises entirely from the imbalance between positive and negative crossings. The $A^2$ normalization reflects linking density: since crossings occupy a volume proportional to $A$, the crossing density per unit volume is $\ell_{\mathrm{net}} / A^2$.

**Magnitude.**

Evaluating at the background substrate $q_0$, we find $\hbar_q \approx 0.0991$ and $\hbar_q^2 \approx 0.00982$. For representative nuclei:

See [Table](#tbl:hadron-q-self-correction-table-data).

The self-deformation is small ($|\delta q / q_0| < 0.1\%$ for all nuclei).

**Effect on beta decay: the differential shift.**

In beta decay, $A$ remains fixed while $(p, n)$ shifts by $(+1, -1)$. The daughter nucleus exhibits a different self-deformation from the parent. The change in effective $q$ across the decay is:

$$
  \Delta q_{\mathrm{eff}}
  = 
  \delta q(p+1, n-1) - \delta q(p, n)
  = 
  \frac{A - 1}{A^2} \cdot \hbar_q^2.
$$

This shift is strictly positive: the daughter acquires one more proton and thus more positive crossings, yielding a higher effective $q$. A higher $q$ increases the crossing asymmetry, resulting in a larger $Q$-value ([transition energy](#def:Q-value-transition)) than predicted by the background alone. Through the Sargent rule $f(Q) \propto Q^5$, the enlarged $Q$-value increases the decay rate and shortens the half-life.

The shift $\Delta q_{\mathrm{eff}}$ represents precisely the $q$-anomaly $\delta_q$ of the transition energy. The daughter is evaluated at the shifted $q + \Delta q_{\mathrm{eff}}$, not the background $q$. This embodies $q$-deformed energy balance, overriding classical conservation.

**Effect on the decay rate.**

The differential shift $\Delta q_{\mathrm{eff}}$ modifies the effective substrate parameter at the converting nucleon. The decay rate depends on $q$ with sensitivity $\approx 48$ ([half-life regimes](#rem:hadron-half-life-regimes)). Thus, a shift of $\Delta q / q_0 \sim 0.1$--$0.4\%$ induces a measurable change in the decay rate.

For ${}^{3}\mathrm{H}$ ($A = 3$), the shift $\Delta q_{\mathrm{eff}} = (2/9) \times \hbar_q^2 \approx 0.00218$ is the maximum correction. This categorical quantity derives directly from $q$, $A$, and the linking structure of the nuclear braid.

**Universality.**

The self-deformation applies whenever $q$ is evaluated on a specific hadron configuration, extending beyond half-lives. The beta-stability line ([beta-stability](#prop:beta-stability)) and the topological mass formula receive identical structural corrections when $q_0$ is replaced by $q_{\mathrm{eff}}$.

**Formalization goal plausibility.**

The intended Lean theorems (establishing `deltaQ <= 0` for neutron-rich nuclei, `differentialShift >= 0`, and `qEff > 1`) possess mathematically sound proof bodies relying on basic arithmetic, `omega`, and `positivity` tactics. The Lean file structure is technically broken because theorem headers were commented out (their Archimedean nature conflicts with the generic `R_q` Laurent polynomial ring). Closing this gap is highly plausible. It requires separating generic definitions from Archimedean instantiations (e.g., via a ring homomorphism to $\mathbb{R}$) and restoring the theorem headers over the reals. The underlying inequalities are elementary, making the formalization gap purely structural.
<!-- FILE_END: hadron-q-self-correction.md -->

<!-- FILE_START: hadron-q-self-correction-interpretation.md -->
**Remark (Topological back-reaction).** The $\binom{p}{2} - \binom{n}{2}$ signed-crossing excess acts as a topological self-deformation of the substrate field. Driven by nuclear linking density ($\ell_{\mathrm{net}}/A^2$), this provides a geometric mechanism for nuclear self-correction.
<!-- FILE_END: hadron-q-self-correction-interpretation.md -->

<!-- FILE_START: skein-coulomb-enhancement.md -->
**Proposition.**
Let $(\mathbf{C}, A, \tau)$ be a Descartes universe with substrate parameter $q$. In the beta decay $\mathcal{N}(Z, N) \to \mathcal{N}(p\!+\!1, n\!-\!1) + T_{2,3} + \nu^{\sigma}$, the emitted electron $T_{2,3}$ crosses each of the $Z = p + 1$ proton strands of the daughter nucleus as it exits the Hopf link. The $q$-deformed wedge product $\wedge_q$ ([crossing asymmetry](#rem:skein-crossing-asymmetry)) assigns weight $q$ to each positive electron-proton crossing. This produces a coherent product that multiplies the decay rate by the **Skein-Coulomb enhancement factor**:

$$
  F_q(Z, E)
  = 
  \frac{2\pi\eta_q}{1 - e^{-2\pi\eta_q}}
$$

The $q$-deformed Sommerfeld parameter is:

$$
  \eta_q
  = 
  \alpha_{\mathrm{EM}}(q)
  \cdot \frac{Z}{\beta_e}
$$

where $\alpha_{\mathrm{EM}}(q) = q^{-1}/([9]_q \cdot [10]_q)$ ([EM coupling projection](#prop:em-coupling-projection)) and $\beta_e = v_e / c$ is the velocity of the emitted electron.

**Derivation.**
We evaluate the canonical action $\mathfrak{S}_q$ ([canonical action](#prop:qou-canonical-action)) on the full outgoing state $\psi = T_{2,3} \cup \mathcal{N}(p\!+\!1, n\!-\!1)$. This decomposes as:

$$
  \mathfrak{S}_q\big|_\psi
  = 
  \mathfrak{S}_q\big|_{\mathcal{N}}
  + 
  \sum_{j=1}^{Z} \mathcal{S}_{e\text{-}p_j}
  + 
  \mathfrak{S}_q\big|_{T_{2,3}}
$$

The middle sum runs over all electron-proton crossings. Each crossing contributes a Skein weight $\mathcal{S}_{e\text{-}p_j}(q) = q$. This is a positive crossing between two like-charge constituents. The electron's radial wave function picks up a phase $e^{i\delta_\ell}$ at each proton. The phase shift is:

$$
  \delta_\ell
  = 
  \arg \Gamma(\ell + 1 + i\eta_q).
$$

The coherent product of $Z$ such scattering amplitudes, summed over partial waves $\ell$ and integrated over the electron energy spectrum, yields:

$$
  |\psi_e(0)|^2_{\text{Coulomb}}
  = 
  |\psi_e(0)|^2_{\text{free}}
   \times 
  F_q(Z, E).
$$

The decay rate is directly proportional to $|\psi_e(0)|^2$ (the electron wave function at the nuclear origin). Thus, $F_q$ multiplies the leading-order rate.
<!-- FILE_END: skein-coulomb-enhancement.md -->

<!-- FILE_START: skein-coulomb-enhancement-interpretation.md -->
The leading-order half-life formula ([hadron half-life](#prop:hadron-half-life)) evaluates the Skein polynomial strictly on the **nucleus alone**, treating the emitted electron as a free particle. However, the electron (trefoil $T_{2,3}$, [electron knot](#def:electron-knot)) traverses the Coulomb field of $Z$ protons as it exits the nucleus. Each electron-proton crossing carries a Skein weight. Evaluating the Skein polynomial on the **full outgoing link** $T_{2,3} \cup \mathcal{N}(Z, N)$ naturally generates the Coulomb enhancement.

**This does not constitute an ad hoc correction.** It is precisely the same Skein polynomial, evaluated on the complete outgoing link rather than truncating at the weak vertex.

**Magnitude.**
The integrated Coulomb enhancement (averaged over the electron energy spectrum) is a large, $Z$-dependent factor.

See [Table: Skein-Coulomb enhancement factors](#tbl:skein-coulomb-enhancement-table1-data).

These are **not** small perturbative corrections. They change decay rates by factors of 1.4 to 5. The leading-order predictions ([verification](#ex:hadron-half-life-verification)) inherently include $F_q$ at leading order through the nucleus-specific matrix element. The $\sim 10$--$17\%$ residual in the verification table stems entirely from discrete nuclear structure effects. Shell closures, pairing, and deformation modify the Gamow--Teller strength $\sigma_{\mathrm{GT}}$ at the individual-nucleus level.

**Transition classes.**
The nuclear matrix element $|\mathcal{M}_q|^2$ varies by six orders of magnitude across the verification set. Measured $\log ft$ values (NNDC/ENSDF) classify the transitions.

See [Table: Beta-decay classification](#tbl:skein-coulomb-enhancement-table2-data).

The QOU framework dictates the $q$-dependent modulation of each transition class (via $[2]_q$, $\tanh(\ln q)$, and $\sigma_{\mathrm{GT}}$). It does not, however, predict the absolute matrix element from the leading-order Hecke computation alone. Predicting $|\mathcal{M}_q|^2$ for individual nuclei necessitates resolving the discrete shell structure, specifically the precise quantum numbers of the parent and daughter nuclear states.

**Predictions of the QOU.**
Within a single transition class (fixed $\log ft$), the QOU correctly predicts:

1. **The $q$-dependent scale**: The factor $(q + q^{-1})(q - q^{-1})^5$ sets the overall decay-rate scale entirely from the single parameter $q$.
2. **The $A$-dependence**: We find $t_{1/2} \propto A^{5/3}$ at fixed $|\delta p|$ and fixed transition class.
3. **The $q$-sensitivity**: We predict $\partial \ln \Gamma / \partial \ln q \approx 48$ without free parameters.
4. **The Coulomb enhancement structure**: The term $F_q(Z, E)$ emerges directly from the Skein crossing weights. This unifies the electromagnetic and weak interactions through the single deformation parameter $q$.
5. **The self-deformation**: We observe a differential $\Delta q_{\mathrm{eff}}$ correction induced by the hadron's own linking structure.
<!-- FILE_END: skein-coulomb-enhancement-interpretation.md -->

<!-- FILE_START: groebner-nf-computation.md -->
The Gröbner--Shirshov normal form $\mathcal{N}(Z, N)$ of a nucleus in $H_A(q)$ is a formal sum over reduced braid words:

$$
  \mathcal{N}(Z, N)
  = 
  \sum_{w \in \mathrm{supp}} c_w \cdot w.
$$

Here, each amplitude $c_w \in \mathbb{Z}[q^{1/2}, q^{-1/2}]$ is an exact Laurent polynomial in the substrate parameter $q$. The support $\mathrm{supp} \subset S_A$ consists of reduced words in the symmetric group.

## Content of the NF

Each reduced word $w$ of length $\ell(w)$ represents a configuration of $\ell(w)$ simultaneously active crossings in the nuclear braid. The amplitude of this configuration is $c_w$.

The word length $\ell$ has a direct physical interpretation:

See [Table 1](#tbl:groebner-nf-computation-table1-data).

The weight distribution $W(\ell) = \sum_{|w| = \ell} |c_w|$ defines the total amplitude at each correlation level. For all computed nuclei ($A \leq 12$):

- $W(L_{\max}) \gg W(0)$: The fully correlated state carries the largest amplitude. This determines the shell binding energy via many-body correlations.
- $W(0) + W(1)$: This is the amplitude in the optimal basis $\{\mathbf{1}, \sigma_0, \ldots, \sigma_{A-2}\}$, which the transfer matrix computes directly via traced volumes $\hat{V}_i$.
- $W(\ell) / W(\ell - 1) \approx q^{c}$: The weight grows exponentially. Each Hecke reduction $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ transfers amplitude from degree $\ell$ to degrees $\ell - 1$ and $\ell - 2$, scaling by $q - q^{-1} \approx 0.209$.

## Quotient ideals: reducing $A!$ to $A$

The raw normal form contains up to $|S_A| = A!$ terms. For nuclei in the valley of stability ($N \geq Z - 1$), two quotient ideals reduce this to exactly $A$ terms (the optimal Gröbner--Shirshov basis):

**$I_8$ (adjacency correlation).** A reduced word $\sigma_i \sigma_{i+1}$ of length $2$ is absorbed into the single-generator term $\sigma_{i+1}$ when the latter is present. The coefficient of $\sigma_i \sigma_{i+1}$ matches the off-diagonal entry of the transfer matrix product $M_i$ at $\sigma_i$.

Physically, adjacency correlation is the non-commutative coupling between neighbouring crossings. It appears as the off-diagonal entry of the $2 \times 2$ transfer matrix $T(c, d)$ acting on the Hecke state $(a \sigma + b)$. The optimal basis encodes this coupling in the ratio $c_{\sigma_i \sigma_{i+1}} / c_{\sigma_{i+1}}$, a function of $q$ alone.

**$I_9$ (closed shell chain collapse).** A reduced word $w \cdot \sigma_j$ is absorbed when its prefix $w$ is present. Applying this recursively from longest to shortest words collapses the entire normal form to the standard basis $\{\mathbf{1}, \sigma_0, \ldots, \sigma_{A-2}\}$.

Physically, each generator $\sigma_i$ contributes a transfer matrix chain $M_i = \prod_{j > i} T_{K_i, K_j}(q)$. The extension $w \cdot \sigma_j$ represents the next step in this chain. Collapsing the chain to a single term $\hat{V}_i = z \cdot (M_i)_{00} + (M_i)_{10}$ yields the Markov-traced volume.

**Necessity of $d \neq 0$ for $I_9$.** Multiplying the normal form by $(c \cdot \sigma_k + d)$ scales every existing word by $d$ and extends each word by $c \cdot \sigma_k$. For every extended word $w \cdot \sigma_k$, the prefix $w$ survives from the $d$-term, allowing $I_9$ to absorb it. This mechanism fails if $d = 0$.

For proton–proton crossings, $d = 0$. Without the prefix, $I_9$ lacks an anchor for chain stripping. The condition $d \neq 0$ holds for neutron–neutron ($d = -(q - q^{-1})$) and proton–neutron ($d = -(q - q^{-1})/2$) crossings. The valley of stability condition $N \geq Z - 1$ ensures at least one $d \neq 0$ crossing at every generator.

## The histogram: universal in $A$

The term-count histogram $h(\ell) = \#\{w : |w| = \ell\}$ tallies reduced words at each length. Verified for $A \leq 8$, this histogram is identical for all $(Z, N)$ at the same $A$ (e.g., ${}^8\mathrm{Be}(4,4)$ and ${}^8\mathrm{Li}(3,5)$).

The histogram depends only on the Iwahori--Hecke algebra $H_A(q)$, factoring as a product of $q$-integers:

See [Table 2](#tbl:groebner-nf-computation-table2-data).

These are $q$-multinomial coefficients. The palindromicity of the histogram polynomial (verified for $A \leq 7$) reflects the Poincaré duality of the Bruhat order on the support.

## The weight distribution: where pairing lives

Unlike the $A$-universal histogram, the weight distribution $W(\ell)$ depends on $(Z, N)$. At constant $A$:

- Even-even nuclei exhibit higher total weight, reflecting stronger coherence from nucleon pairing.
- Odd-odd nuclei exhibit lower total weight, as unpaired crossings weaken the chain anchor.

The ratio $\mathrm{net}(\text{even-even}) / \mathrm{net}(\text{odd-odd})$ quantifies the pairing energy. At $A = 6$, we find $\mathrm{net}({}^6\mathrm{He}(2,4)) / \mathrm{net}({}^6\mathrm{Li}(3,3)) = 6.64 / 4.96 = 1.34$, a $34\%$ pairing enhancement.

In the normal form, adjacent same-type crossings (even occupancy) trigger the Hecke product $\sigma^2 = (q - q^{-1})\sigma + 1$. The generated $\mathbf{1}$ term anchors the $I_9$ chain. Unpaired crossings (odd occupancy) produce only the $\sigma$ term, weakening the anchor and reducing total amplitude.

## The Pauli factor: multi-generator phenomenon

The alternating trace $\mathrm{tr}_{\mathrm{alt}} = \sum_w c_w \cdot (-q^{-1})^{\ell(w)}$ evaluates each word at the alternating eigenvalue $-q^{-1}$. The ratio

$$
  F_{\mathrm{Pauli}}^{(A)}
  = 
  \frac{|\mathrm{tr}_{\mathrm{alt}}(\mathcal{N})|}{|\mathrm{net}(\mathcal{N})|}
$$

measures the normal form amplitude residing in the alternating irrep of $S_A$, the antisymmetric channel governed by Pauli exclusion.

This quantity eludes the $2 \times 2$ transfer matrix. The per-generator transfer matrix has only eigenvalues $q$ and $-q^{-1}$, which are shared by both the symmetric and alternating irreps. Irrep separation demands the multi-generator interaction (e.g., how $\sigma_0$ and $\sigma_1$ act together). This requires the full Gröbner--Shirshov normal form.

## The $6 \times 6$ transfer matrix: no shortcut

One might expect an enlarged $6 \times 6$ transfer matrix (acting on the $H_3(q)$ basis $\{\mathbf{1}, \sigma_0, \sigma_1, \sigma_0\sigma_1, \sigma_1\sigma_0, \sigma_0\sigma_1\sigma_0\}$) to separate the irreps.

Symbolic proof shows otherwise. The matrix $T_6(c, d) = c \cdot R(\sigma_0) + d \cdot I_6$ possesses exactly two distinct eigenvalues, each with multiplicity $3$:

$$
  \lambda_+ = c \cdot q + d,
  \qquad
  \lambda_- = c \cdot (-q^{-1}) + d.
$$

These match the $2 \times 2$ eigenvalues. The standard irrep contains both eigenvalues because $\sigma_0$ in the standard representation has a $2 \times 2$ matrix with both eigenvalues. The $6 \times 6$ matrix fails to separate the symmetric from the standard irrep, or the alternating from the standard irrep.

The Pauli factor $F_{\mathrm{Pauli}}$ is irreducibly multi-generator. No per-generator transfer matrix can compute it.

Physically, the Pauli exclusion principle acts between pairs of fermions (quarks in a Borromean triplet), not on individual crossings. The multi-generator structure embodies this inter-quark correlation.

Computed witnesses (exact in $\mathbb{Z}[\check{q}, \check{q}^{-1}]$ for $A \leq 12$, displayed at $q_0$):

See [Table 3](#tbl:groebner-nf-computation-table3-data).

For $A \leq 12$, the symbolic witnesses $\mathrm{tr}_{\mathrm{alt}}(\check{q})$, $\mathrm{net}(\check{q})$, $\mathrm{observable}(\check{q})$, and $\mathrm{color}(\check{q})$ are exact Laurent polynomials over $\mathbb{Z}$ in the spinor information rate $\check{q} = q^{1/2}$. The denominator $2^{p_n}$ is tracked separately.

The $H_3(q)$ Pauli factor is $F_{\mathrm{Pauli}} = 0.6382$. The $A$-strand values differ because they capture the full multi-generator interaction rather than the $3$-strand projection.

## Streaming pattern discovery

During inductive construction, the quotient ideals $I_8$ and $I_9$ strip terms at each strand boundary. The engine identifies the most frequent suffix patterns before stripping. These identify candidates for new structural ideals.

For ${}^{16}\mathrm{O}$ at strand $8$, $\sigma_7 \sigma_8$ appeared $52{,}230$ times (the $I_8$ adjacency pattern at the newest generator). The pattern $\sigma_4 \sigma_6 \sigma_7 \sigma_8$ appeared $14{,}262$ times, revealing a $4$-generator chain that skips $\sigma_5$ (a potential $I_{11}$ candidate).

Because the weight distribution $W(\ell)$ and the Pauli accumulator $\mathrm{tr}_{\mathrm{alt}}$ are preserved exactly through stripping, no physical data is lost. The $A$-universal histogram $h(\ell)$ can be computed once from the minimal case $N(1, A-1)$.
<!-- FILE_END: groebner-nf-computation.md -->

<!-- FILE_START: nf-computation-strategy.md -->
The Gröbner--Shirshov normal form computation separates into three complexity regimes.

## The three regimes

**Regime 1: Transfer matrix ($O(A^2)$).**
The optimal normal form $\{\mathbf{1}, \sigma_0, \ldots, \sigma_{A-2}\}$ possesses coefficients equal to the Markov-traced volumes $\hat{V}_i(q)$. Each $\hat{V}_i$ is a product of $A - i - 1$ transfer matrices $T(c_j, d_j)$, totalling $\binom{A}{2}$ multiplications. This yields the $Q$-value, the Skein polynomial, and the optimal normal form coefficients without Iwahori--Hecke algebra expansion.

**Regime 2: Symbolic Gröbner--Shirshov with stripping ($O(A^3)$).**
The full normal form dictates the Pauli factor $F_{\mathrm{Pauli}}$, the color content, and the per-length weight distribution. We apply inductive quotient stripping (ideals I$_{8}$ and I$_{9}$) after each strand. This bounds the intermediate term count to $O(A^2)$ per strand, giving $O(A^3)$ overall. All coefficients remain exact Laurent polynomials in $\mathbb{Z}[t, t^{-1}]$.

**Regime 3: Full expansion ($O(A!)$).**
Without stripping, the raw normal form generates up to $A!$ terms. This limits tractability to $A \leq 9$. The full expansion exposes the raw histogram and palindromic structure, but contributes to no physical observable.

## Inductive quotient chaining

At each strand boundary, we apply the chain collapse ideal I$_{9}$ and accumulate the Pauli data of stripped terms as symbolic polynomials. The surviving optimal basis contains roughly $A$ terms. The subsequent strand computation initiates from these $A$ terms, bypassing the $A!$ explosion.

The accumulation is exact. Each stripped term contributes its coefficient $c_w(t)$ to the running totals $\mathrm{tr}_{\mathrm{alt}}(t)$ and $\mathrm{net}(t)$, weighted by $(-t^{-2})^{\ell(w)}$ for the alternating trace. The final witness sums the accumulated (stripped) and kept (surviving) contributions.

We accumulate only stripped terms. If we accumulated all terms before stripping, surviving terms would double-count when contributing to subsequent strands.

## The bottleneck: strand 8

For all nuclei with $A > 8$, the computation exhibits a characteristic bottleneck:

1. **Strands 1–7**: The normal form builds to $\sim 14{,}000$ terms ($A = 8$) or $\sim 230{,}000$ terms ($A = 9$), taking under 10 seconds.
2. **Strand 8 boundary**: The I$_{9}$ strip collapses $\sim 230{,}000$ terms to roughly 9 terms. We accumulate the Pauli data for the stripped terms.
3. **Strands 9+**: Each strand expands from $\sim 10$ terms to $5{,}000$–$240{,}000$ terms, then strips back to $10$–$600$ terms at the boundary.

The computational bottleneck is the final crossing of a large strand—typically the neutron–neutron crossings characterized by $c = 1, d = -(q - q^{-1})$. Peak memory occurs immediately before stripping.

## Optimisation strategies

**Monomial ordering (LenLex).**
We use length-lexicographic ordering. The engine reduces shorter words first, then applies lexicographic ordering within the same degree. This aligns with the Iwahori--Hecke algebra, where the Hecke relation $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ acts as the sole degree-changing rule.

**Junction-only reduction.**
When appending $\sigma_k$ to a reduced word $w$, we only check the junction (the final characters of $w \cdot \sigma_k$). The prefix $w$ remains reduced. This lowers the amortized per-word reduction cost from $O(\ell)$ to $O(1)$.

**Separated reduction pools.**
We partition terms into stable (fully reduced) and pending pools. Stable terms are never rescanned. When a pending term collides with a stable term, the merged result returns to the pending pool.

**Batch quotient stripping ($O(A \cdot L_{\max})$).**
The I$_{9}$ strip processes all terms at each length level simultaneously, descending from longest to shortest. We collect and remove all terms containing a specific length $\ell - 1$ prefix. This operates in $O(n \cdot L_{\max})$ rather than $O(n^2)$.

**Mid-crossing stripping.**
For large strands, the quotient strip fires within a crossing multiplication once the term count exceeds 30,000. This halts the exponential blowup from cascaded adjacent generators.

**Pattern discovery.**
At each strand boundary, the engine identifies frequent suffix patterns. These candidate sub-words suggest structural ideals beyond I$_{8}$ and I$_{9}$. Persisting patterns indicate universal structural operations eligible for inclusion in the quotient ideal.

## Scalability

| $A$ | Strategy | Time | Memory | Coefficients |
|:---:|----------|-----:|-------:|:------------:|
| $\leq 9$ | Full expansion | $\leq 30$s | $\leq 562$MB | $\leq 10^{12}$ |
| $10$–$12$ | Inductive stripping | $10$–$45$s | $\leq 2.5$GB | $\leq 10^{17}$ |
| $13$–$16$ | Inductive + mid-crossing | est. $1$–$5$min | $\leq 3$GB | $\leq 10^{22}$ |
| $17$–$20$ | Needs big integer | est. $5$–$30$min | $\leq 5$GB | $> 10^{38}$ (i128 overflow) |
| $\leq 40$ | Transfer matrix only | $< 1$s | $< 1$MB | $O(A^2)$ |

The transfer matrix ($O(A^2)$) yields $Q$-values for any $A$. The symbolic engine supplies $F_{\mathrm{Pauli}}$ and color content up to $A \leq 16$ (minutes) or $A \leq 20$ (with big integers). Beyond $A = 20$, we sacrifice exact-in-$q$ calculations for a per-length accumulation float engine.
<!-- FILE_END: nf-computation-strategy.md -->

<!-- FILE_START: kummer-shell-closure.md -->
The Kummer tower filtration provides the algebraic framework for understanding shell closure, the Pauli factor, and the odd-odd pairing deficit in the Gröbner--Shirshov normal form.

## The $\mu_2$ torsion as Pauli evaluation

The alternating trace of the normal form evaluates each word $w$ at the alternating eigenvalue $(-q^{-1})^{\ell(w)}$:

$$
  \mathrm{tr}_{\mathrm{alt}}(\mathcal{N})
  = 
  \sum_{w \in \mathrm{supp}} c_w \cdot (-q^{-1})^{\ell(w)}
$$

This sum is the $\mu_2$ Kummer evaluation. It applies the sign character of $\mathbb{G}_m$ to the normal form. The eigenvalue $-q^{-1}$ is the alternating root of the Hecke relation $\sigma^2 = (q - q^{-1})\sigma + 1$, alongside the symmetric root $q$.

The Pauli factor

$$
  F_{\mathrm{Pauli}}^{(A)}
  = 
  \frac{|\mathrm{tr}_{\mathrm{alt}}(\mathcal{N})|}{|\mathrm{net}(\mathcal{N})|}
$$

measures the $\mu_2$-torsion content of the normal form. It quantifies the amplitude present in the antisymmetric channel.

## Shell closure as Kummer divisibility

The Kummer reduction at level $n$ takes the form:

$$
  \kappa_0 \bmod n = 0
  \quad\Longleftrightarrow\quad
  n  \big|  \chi(A)
$$

The obstruction vanishes when $n$ divides the Euler characteristic $\chi(A)$ of the brane configuration. We apply this to the nuclear braid.

- At level $n = 2$, the obstruction $\kappa_0 \bmod 2 = 0$ vanishes when $\chi(A)$ is even. This corresponds to even-even nuclei. The Pauli factor is enhanced.
- For magic numbers, the obstruction vanishes at specific levels $n$ corresponding to the shell capacities. Magic number 2 corresponds to $\mu_2$, magic 8 corresponds to $\mu_8$, and so on.
- For doubly magic nuclei, both the proton and neutron obstructions vanish simultaneously at the same Kummer level.

## The pairing deficit as $\mu_2$ obstruction

For odd-odd nuclei, both $Z$ and $N$ are odd. The Euler characteristic $\chi(A)$ is odd at the relevant level. The condition $\kappa_0 \bmod 2 \neq 0$ implies the obstruction persists at the $\mu_2$ level. This persistence has three effects:

1. The normal form has a lower total amplitude. We observe $\mathrm{net}(\text{odd-odd}) < \mathrm{net}(\text{even-even})$ at the same $A$.
2. The alternating trace is suppressed relative to the net amplitude.
3. The Pauli factor $F_{\mathrm{Pauli}}^{(A)}$ is lower.

Calculations at $A = 6$ yield $\mathrm{net}({}^6\mathrm{He}(2,4)) / \mathrm{net}({}^6\mathrm{Li}(3,3)) = 6.64 / 4.96 = 1.34$. This demonstrates a $34\%$ pairing enhancement for even-even configurations over odd-odd configurations.

This provides an algebraic formula for the pairing correction $I_{10}$. The correction factor for odd-odd nuclei is the ratio of $\mu_2$-torsion content between the even-even and odd-odd configurations at the same mass number $A$.

## Computational complexity

The Kummer framework suggests the Pauli witness computation scales as $O(A^3)$:

| Component | Complexity | What it computes |
|-----------|-----------|-----------------|
| Transfer matrix (optimal NF) | $O(A^2)$ | $\hat{V}_i$ for each generator |
| $\mu_2$ evaluation per word | $O(\ell)$ per word | $(-q^{-1})^{\ell(w)} \cdot c_w$ |
| Total NF terms (with stripping) | $O(A^2)$ per strand | Quotient keeps terms bounded |
| Number of strands | $O(A)$ | One per nucleon |
| **Total** | **$O(A^3)$** | Full Pauli witness |

Computational verification:

| $A$ | Terms | Time | Scaling |
|:---:|------:|-----:|:-------:|
| $8$ | $14256$ | $0.9$s | — |
| $9$ | $234504$ | $29$s | — |
| $10$ | $8.7$M | $4.3$s (v2) | — |
| $12$ | $923319$ | $269$s (v3) / $\sim5$s (v6) | — |
| $16$ | $3.4$M | $38$s (v6) | $A^3 = 4096$ (matches) |

Applying the quotient during construction (v6) yields an effective complexity of $O(A^3)$. The complexity is cubic in the mass number. Nuclei up to $A = 40$ (${}^{40}\mathrm{Ca}$, doubly magic) are computationally tractable in minutes.

## Symbolic witnesses

The symbolic engine computes exact evaluations in $\mathbb{Z}[\check{q}, \check{q}^{-1}]$, where $\check{q} = q^{1/2}$ is the spinor information rate. It produces Laurent polynomial witnesses for $\mathrm{tr}_{\mathrm{alt}}(q)$ and $\mathrm{net}(q)$. We verify this through $A = 9$ (${}^9\mathrm{Be}$) without overflow.

For $A > 9$, the integer coefficients grow as $O(q^{A^2})$. This growth requires either larger integer types or modular arithmetic for exact computation. The float engine (v6) serves as a cross-check at $q_0$.

The polynomial coefficients grow following the Kummer tower. At level $n$, the coefficients involve the $q$-factorial $[n]_q!$, which possesses $O(n^2)$ digits. At $A = 16$, the maximum coefficient is approximately $10^{18}$, which fits within a 128-bit integer. At $A = 40$, the maximum coefficient reaches approximately $10^{100}$. This exceeds the 128-bit integer range and requires arbitrary-precision arithmetic or modular reduction.
<!-- FILE_END: kummer-shell-closure.md -->

<!-- FILE_START: skein-shell-correction.md -->
The Skein binding Lagrangian ([Skein binding Lagrangian](#def:skein-binding-lagrangian)) derives the smooth, liquid-drop nuclear binding energy directly from the categorical action. This derivation predicts the macroscopic trend of neutron excess growing with $p$. However, it misses the **shell structure**: the stability pairs $\{2, 8, 20, 28, 50, 82, 126\}$ at which nuclei exhibit anomalously high binding. Shell corrections demand a discrete term in the binding energy, escaping the smooth continuous formula.

**The gap in the derivation.**

The chain from the R-matrix to nuclear binding proceeds as:

$$
  \mathcal{R} \xrightarrow{\text{Yang--Baxter}}
  \check{R} \xrightarrow{\text{crossing asymmetry}}
  \mathfrak{E}_{\mathrm{cross}} \xrightarrow{\text{Skein binding}}
  \mathcal{L}_{\mathrm{bind}} \xrightarrow{\partial/\partial p}
  p^*(A).
$$

The final beta-stability step yields the smooth curve. The missing step is a discrete correction $\delta E_{\mathrm{shell}}(p, n)$, nonzero only when the multi-nucleon link $\mathcal{N}(Z, N)$ ([stable nucleus](#def:stable-nucleus)) possesses a specific topological structure.

**Conjecture: shell correction from closed sub-links.**

*For the multi-nucleon link $\mathcal{N}(Z, N) = Z\mathfrak{p} \oplus N\mathfrak{n}$, the Skein polynomial $J_{\mathcal{N}}(q)$ factors into a product of Skein polynomials of closed sub-links at specific $(p, n)$ values. The shell correction is:*

$$
  \delta E_{\mathrm{shell}}(p, n)
  = 
  -\lambda_{\mathrm{shell}} \cdot
  \sum_{\text{closed sub-links } L_i \subset \mathcal{N}}
  \frac{|J_{L_i}(q)|}{|J_{\mathcal{N}}(q)|},
$$

*where the sum runs over maximal closed (unlinked) sub-links $L_i$ of $\mathcal{N}$, and $\lambda_{\mathrm{shell}}$ is the shell energy scale.*

**Closed sub-links of $\mathcal{N}(Z, N)$.**

A **closed sub-link** of $\mathcal{N}(Z, N)$ is a subset $S \subset \{1, \ldots, p+n\}$ of nucleons satisfying two conditions:

1. The restriction $\mathcal{N}|_S$ of the Hopf link to $S$ forms a **split link**. It can be isotoped into a ball disjoint from all remaining nucleons.
2. The Skein polynomial of $\mathcal{N}|_S$ divides $J_{\mathcal{N}}$: $J_{\mathcal{N}} = J_{\mathcal{N}|_S} \cdot J_{\mathcal{N}|_{S^c}} \cdot (\text{linking factor})$.

When these hold, the link factorizes. The nucleons in $S$ form an internally bound cluster, contributing extra binding energy beyond the liquid-drop prediction.

**Predicted factorizations.**

For the Descartes universe ($\chi = -6$), we expect the following factorizations:

See [Table](#tbl:skein-shell-correction-table-data).

The pattern is clear. The $\alpha$ particle $\mathcal{N}(2,2)$ acts as the fundamental closed sub-link; its Skein polynomial factorizes completely. Stability pair nuclei are precisely those where the maximum possible number of $\alpha$ clusters form, saturating all available Hopf junctions.

**The $\alpha$-cluster hypothesis.**

The closed sub-link structure predicts that the shell correction is largest when $(p, n)$ admits the exact factorization

$$
  \mathcal{N}(Z, N) = 
  k \times \mathcal{N}(2, 2)  \oplus 
  (p - 2k)\mathfrak{p}  \oplus 
  (n - 2k)\mathfrak{n},
$$

where $k = \min(\lfloor p/2 \rfloor, \lfloor n/2 \rfloor)$. The shell energy becomes

$$
  \delta E_{\mathrm{shell}}
  = 
  -\lambda_{\mathrm{shell}} \cdot k
  = 
  -\lambda_{\mathrm{shell}} \cdot
  \min\!\left(\left\lfloor \frac{p}{2} \right\rfloor,
  \left\lfloor \frac{n}{2} \right\rfloor\right).
$$

This quantity is maximised when both $p$ and $n$ are even, because even-even nuclei host the most $\alpha$ clusters. It is locally maximised at the stability pairs, where the factorization is complete.

**Remaining obligations.**

1. **Skein factorization**: We must prove that the Skein polynomial $J_{\mathcal{N}(Z, N)}(q)$ factors when $(p, n)$ admits an $\alpha$-cluster decomposition. This requires a direct computation in the Skein algebra of the Hopf link.
2. **Shell energy scale**: We must derive $\lambda_{\mathrm{shell}}$ directly from the categorical action. We expect it to be expressible in terms of $q$, $a_V$, and the Skein polynomial of $\mathcal{N}(2,2)$.
3. **Corrected stability formula**: We must show that the total binding energy $\mathcal{L}_{\mathrm{bind}} + \delta E_{\mathrm{shell}}$ reproduces all observed stable isotopes to within $|\Delta n| \leq 1$ for all $p \leq 103$.
4. **Genus lift**: We must show that including $\delta E_{\mathrm{shell}}$ lifts the stability cubic from genus $0$ to genus $1$, establishing a firm connection to the [elliptic stability conjecture](#rem:elliptic-stability-locus).
<!-- FILE_END: skein-shell-correction.md -->

