This registry records the full derivation of [prop:recursive-atom-knot-atlas](#prop:recursive-atom-knot-atlas): the methodology classification, notation legend, braid-closure gallery, the per-level atlas, and the per-element AME 2020 cross-reference. It carries no logical content beyond the proposition it supports.

This atlas identifies the specific knot or link for each confined braid at the substrate value $q_0$, verifying whether its invariant reproduces the measured mass or binding energy. A single $q_0$-indexed registry enables recursive construction of composite entries from nucleon and $\alpha$-cluster constituents, ensuring uniform comparison against the AME 2020 reference. Where a free-nucleon entry lists an absolute mass in MeV, that figure is the dimensionless ratio $\mathfrak{m}/m_e$ rendered against the $m_e$ scale (CAL-1, set by fiat), not an independent absolute-mass prediction; the framework's predictive content is the ratio, the binding energy, and the mass splitting. The identification mechanics are detailed below; a layered extension then applies this machinery to every isotope.

## Methodology classification (STRICT)

Every entry carries a **methodology tag** recording its derivation method.

| Tag | Definition | Examples |
|---|---|---|
| `principled-derivation` | Knot is the closure of an explicit $\sigma$-braid word in $H_{n_0}(q_0)$ from [def:confined-particle](#def:confined-particle); $\mathrm{Vol}_{\mathrm{hyp}}$ computed at $\geq 50$ decimal digits via `hp_volume_of_link_closure(braid_word, digits=50)`. | electron $\sigma_1^3$ $\to$ $3_1$, proton/neutron $(\sigma_1 \sigma_2^{-1})^3$ $\to$ $\mathcal{B}_3$. |
| `principled-gb-nf` | Trivial-NF entries: a single strand (unknot $0_1$) or the pure identity $\mathbf{1}$. | neutrino ($0_1$), quark; the bare photon (identity $\mathbf{1}$, not the unknot). |
| `manual-historical-volume-match` | Knot was identified in earlier work via volume-match against AME; the GB-NF derivation in $H_{n_0}(q_0)$ has not been computed. **⚠ This tier is AME-inverted**: the producer states it outright — *"that IS a form of AME-driven fitting ([selecting] the knot whose volume is closest to $B_\mathrm{AME}/\rho$)"* ([`mass_table_ppb.py` L18–21](../../../computations/mass_table_ppb.py)) — so binding figures quoted from these volumes are **circular, not predictions**. | ${}^2$H = $6_2$, ${}^{3}$H = $8_{11}$, ${}^{3}$He = $L_{6a4}$. |
| `magic-A-formula` | Algebraic shell-closure formula $A \cdot 8G$ for double-magic light nuclei; no single hyperbolic knot. | ${}^{4}$He. |
| `recursive-on-⁴He` | Built from $n \cdot {}^{4}\mathrm{He} + n_{\alpha\alpha} \cdot c_{\alpha\alpha}$ recursion; principled given ${}^{4}$He. | ${}^{8}$Be–${}^{40}$Ca. |

The principled pipeline computes $\mathrm{Vol}_{\mathrm{hyp}}$ from the $\sigma$-braid word at $\geq 50$ decimal digits via SnapPy's `Link(braid_closure=...).exterior.high_precision` and `mpmath.workdps(50)`. The Wenzl bridge ([`y_lambda_wenzl_bridge_extended.py`](../../../computations/y_lambda_wenzl_bridge_extended.py)) supplies symbolic-in-$q$ Markov-trace coefficients $y_\lambda$.

For atoms $A \geq 5$, the combinatorics of $\mathcal{H}_{3A}$ explode and `SnapPea` limits fail. Computing the exact symbolic trace restricted to active block-partitions sidesteps this bottleneck, yielding the exact trace $B_{sym} = -\alpha \ln |\mathrm{tr}_M|$ alongside the rigorous Q-CLT finite-sum approximation $B_{qCLT} = -\alpha \sum \ln |\hat{V}_i|$.

## Notation legend (auto-included)

| Symbol | Meaning |
|---|---|
| $\sigma_i$ ($i = 1, \ldots, n-1$) | Standard generators of the braid group $B_n$: half-twist between strands $i$ and $i + 1$. Hecke relation $(\sigma_i - q)(\sigma_i + q^{-1}) = 0$. |
| $\sigma_i^{-1}$ | Inverse half-twist (negative crossing). |
| $\mathbf{1}_{B_n}$ | Identity element of $B_n$ (no crossings); Markov closure $= n$ disjoint unknots. |
| $\widehat{\beta}$ | Markov closure (braid $\to$ knot/link in $S^3$). |
| $T_{p, q}$ | Torus knot/link with braid word $(\sigma_1 \sigma_2 \cdots \sigma_{p-1})^q$ in $B_p$. |
| $0_1$ | Unknot (Rolfsen). $T_{1, 0}$ in torus form. |
| $3_1$ | Trefoil. $= T_{2, 3}$. Braid word $\sigma_1^3$ in $B_2$. |
| $4_1$ | Figure-eight. Amphichiral. Braid $(\sigma_1 \sigma_2^{-1})^2$ in $B_3$. |
| $5_1, 5_2$ | Pretzel/torus knots, 5 crossings. |
| $6_1, 6_2, 6_3$ | 6-crossing prime knots. |
| $\mathcal{B}_3$ | Borromean rings = $\widehat{(\sigma_1 \sigma_2^{-1})^3}$ in $B_3$. |
| $L_H$ | Hopf link $= \widehat{\sigma_1^2}$ in $B_2$. |
| $K_{n_a m}$, $L_{n_a m}$ | Knots / links from SnapPy HT-tables (e.g.\ $K11a259$ = 11-crossing alternating knot, position 259). |
| $B_3(\mathrm{flav})$ | Borromean baryon: 3-strand Borromean with flavor labels (uud, udd, etc.) on crossings. |
| $\oplus$ | Binding operator: $H = K \oplus L$ decorates knot $K$ with link $L$. |
| $[K_1, \ldots, K_n]_p$ | Composite hadron of valence $n$ with constituents $K_1, \ldots, K_n$ bound at link $p$. |
| $\nu(\mathfrak{H})$ | Valence (number of constituent knots in a hadron). |

## Braid-closure visualisations (gallery before table)

The following closures appear in the atlas, providing the braid word and its closed knot/link form.

### $\widehat{\sigma_1^3}$ in $B_2$ — the **trefoil $3_1 = T_{2, 3}$**

Word: $\sigma_1^3$. Closure: the **trefoil knot** ($T_{2, 3}$, left-handed, or simplest nontrivial prime knot). Used for: the **electron** ($e^-$), and as the nucleon binding factor in $H_3$. Hyperbolic volume: $0$ (torus knot).

### $\widehat{(\sigma_1 \sigma_2^{-1})^3}$ in $B_3$ — **Borromean rings $\mathcal{B}_3$**

Word: $(\sigma_1 \sigma_2^{-1})^3$. Closure: three pairwise-unlinked circles that are jointly linked. Hyperbolic volume: $\mathrm{Vol}(\mathcal{B}_3) = 8 G \approx 7.328$. Used for: the **proton** $B_3(\mathrm{uud})$ and **neutron** $B_3(\mathrm{udd})$, where flavor labels colour the crossings.

### $\widehat{(\sigma_1 \sigma_2^{-1})^2}$ in $B_3$ — **figure-eight $4_1$**

Word: $(\sigma_1 \sigma_2^{-1})^2$. Closure: the amphichiral **figure-eight knot**. Hyperbolic volume: $\mathrm{Vol}(4_1) = {{ qou.computations.q-pinning-50-digit.calibration_inputs.Vol_4_1_str | precision: 6 }}$ (smallest hyperbolic volume). Used for: the **Higgs field** (mass mechanism).

### $\widehat{\sigma_1^2}$ in $B_2$ — **Hopf link $L_H$**

Word: $\sigma_1^2$. Closure: two circles linked once. Hyperbolic volume: $0$ (torus link). Used for: the **gluon** (lowest force carrier) and the binding link in deuteron $D = [\mathfrak{p}, \mathfrak{n}]_{L_H}$.

### $\widehat{\mathbf{1}_{B_4}}$ — **photon ($\gamma$)**

Word: $\mathbf{1}_{B_4}$ (identity, no crossings). Closure: 4 disjoint unknots. The 4 strands carry polarisation $\times$ chirality components on the exceptional divisor $\mathcal{S}_p$. Used for: the **photon** (vacuum-flux carrier).

### Hyperbolic atom-knots inventory

This inventory lists hyperbolic-knot identifications and their methodology tags.

| Knot / link | Source | Crossings | $\mathrm{Vol}_{\mathrm{hyp}}$ | Used for | Methodology |
|---|---|---|---|---|---|
| $6_2$ | Rolfsen | 6 | 4.4008 | Deuteron $^2$H | `manual-historical-volume-match` |
| $8_{11}$ | Rolfsen | 8 | 8.2863 | Tritium $^3$H | `manual-historical-volume-match` |
| $L_{6a4}$ | Thistlethwaite link | 6 | 7.3277 | $^3$He | `manual-historical-volume-match` |
| $\mathcal{B}_3$ | Borromean | 6 | 7.3277$\ldots$ (hp50) | Proton/neutron $B_3$ | `principled-derivation` (closure of $(\sigma_1 \sigma_2^{-1})^3$) |

## Atlas

| Particle / atom | Confinement level $\ell$ | $n_0$ |
|:--:|:--:|:--:|

### $\ell = 0$ — quark / lepton level

**Neutrino $\nu$** (vacuum-drag particle, no mass)

| Row | Content |
|--:|---|
| Braid (NF) | $T_w = \mathbf{1} \in H_1(q_0)$. Closure $\widehat{T_w} = 0_1$ (unknot). |
| Prediction | $m_\nu \approx 0$ MeV (CODATA upper bound $\lesssim 1$ eV). Confinement at $q_0$: by definition Frobenius-PSD ($\Phi^* = \mathbf{1}$). |

**Photon $\gamma$** (4 polarisation $\times$ chirality components)

| Row | Content |
|--:|---|
| Braid (NF) | $T_w = \mathbf{1}_{B_4} \in H_4(q_0)$. Closure $\widehat{T_w} = 4 \cdot 0_1$ (4 disjoint unknots). |
| Prediction | $m_\gamma = 0$ MeV (massless, gauge boson). 4 components encode the $\sigma_0/\sigma_1$ polarisation $\times$ $(+q, -q^{-1})$ chirality on $\mathcal{S}_p$. |

**Quark $\mathfrak{q}$** (single-strand H_1 unit)

| Row | Content |
|--:|---|
| Braid (NF) | $T_w = \sigma_0 \in H_1(q_0)$. Confined within Borromean baryon. |
| Prediction | Free-quark not observed (confinement); appears only inside hadrons. |

### $\ell = 1$ — single-nucleon / lepton

**Electron $e^-$** (trefoil)

| Row | Content |
|--:|---|
| Braid (NF) | $T_w = \sigma_1^3 \in H_2(q_0)$. Closure $\widehat{T_w} = T_{2, 3} = 3_1$ (trefoil). |
| Prediction | $m_e = 0.51099895$ MeV (calibration anchor; CODATA exact). |

**Proton $\mathfrak{p}$**

| Row | Content |
|--:|---|
| Braid (NF) | $T_w = (\sigma_1 \sigma_2^{-1})^3$ with flavor coloring $\mathrm{uud}$. $\widehat{T_w} = \mathcal{B}_3(\mathrm{uud})$. |
| Prediction | Ratio $m_\mathfrak{p}/m_e$; rendered against the $m_e$ scale, $m_\mathfrak{p} = 938.27208816$ MeV (CODATA exact), model derives via $\mathrm{Vol}(\mathcal{B}_3) = 8 G$ at $q_0$. The MeV figure is a rendering of the ratio, not an absolute-mass claim. |

**Neutron $\mathfrak{n}$**

| Row | Content |
|--:|---|
| Braid (NF) | $T_w = (\sigma_1 \sigma_2^{-1})^3$ with flavor coloring $\mathrm{udd}$. $\widehat{T_w} = \mathcal{B}_3(\mathrm{udd})$. |
| Prediction | Ratio $m_\mathfrak{n}/m_e$; rendered against the $m_e$ scale, $m_\mathfrak{n} = 939.56542052$ MeV. The predictive content is the mass splitting $m_\mathfrak{n} - m_\mathfrak{p}$ (derived from flavor-flip cost, open); the absolute MeV figure is a rendering of the ratio, not an absolute-mass claim. |

### $\ell = 2$ — light atoms (recursive: ref to nucleon entries above)

**Deuterium ${}^2$H = D = $[\mathfrak{p}, \mathfrak{n}]_{L_H}$**

| Row | Content |
|--:|---|
| Braid (NF) | $T_w = (\mathfrak{p}\text{-braid}) \oplus (\mathfrak{n}\text{-braid}) \oplus L_H$ in $H_6(q_0)$. Closure recorded as $\widehat{T_w} = K_{6_2}$ (hyperbolic, $\mathrm{Vol} = 4.4008$) — **asserted, not computed**; see Provenance. |
| Prediction | $B_\mathrm{pred} = 1 \cdot m_e \cdot \mathrm{Vol}(K_{6_2}) = 2.249$ MeV vs $B_\mathrm{AME} = 2.225$, **err = +1.09%** — **not a prediction**; the knot was selected by matching this quantity (see Provenance). |
| **Provenance ⚠** | **$6_2$ is AME-inverted and the deuteron assignment is UNDETERMINED.** (i) The producer states the inversion outright — *"that IS a form of AME-driven fitting ([selecting] the knot whose volume is closest to $B_\mathrm{AME}/\rho$)"* ([`mass_table_ppb.py` L18–21](../../../computations/mass_table_ppb.py)) — so the $+1.09\%$ agreement is circular and inadmissible as a derivation. (ii) The closure claim is not a computation: the canonical mass word is **not a braid word** (five of its letters are averaged crossings, $\mathbb{C}$-linear combinations in $H_6(q)$), and every live construction of it closes to a **3-component link**, whereas $6_2$ is a knot — an arity mismatch fixed by the underlying permutation, so no crossing convention resolves it. Adjudication: [`2026-08-21-deuteron-knot-assignment-adjudication.md`](../../../docs/audits/2026-08-21-deuteron-knot-assignment-adjudication.md) (verdict **UNDETERMINED** — all three candidates $6_2$ / trefoil / Hopf inadmissible). **This row flags the entry; it does not retarget it** — no alternative assignment is established either. |

**Tritium ${}^{3}$H = T = $[\mathfrak{p}, \mathfrak{n}, \mathfrak{n}]_{L_H \oplus T_{2, 3}}$**

| Row | Content |
|--:|---|
| Braid (NF) | $T_w \in H_9(q_0)$. Closure $\widehat{T_w} = K_{8_{11}}$ (hyperbolic, $\mathrm{Vol} = 8.2863$). |
| Prediction | $B_\mathrm{pred} = 2 \cdot m_e \cdot \mathrm{Vol}(K_{8_{11}}) = 8.469$ MeV vs $B_\mathrm{AME} = 8.482$. **err = −0.16%** — **best per-isotope**. |

**Helium-3 ${}^{3}$He = $[\mathfrak{p}, \mathfrak{p}, \mathfrak{n}]_{L_{6a4}}$**

| Row | Content |
|--:|---|
| Braid (NF) | $T_w \in H_9(q_0)$. Closure $\widehat{T_w} = L_{6a4}$ (link, $\mathrm{Vol} = 7.3277$). |
| Prediction | $B_\mathrm{pred} = 2 \cdot m_e \cdot 7.3277 = 7.489$ MeV vs $B_\mathrm{AME} = 7.718$. **err = −2.97%**. |

**Helium-4 ${}^{4}$He = $[\mathfrak{p}, \mathfrak{p}, \mathfrak{n}, \mathfrak{n}]_{4 \cdot 8 G}$**

| Row | Content |
|--:|---|
| Braid (NF) | $T_w \in H_{12}(q_0)$. Magic A-rule formula: $B = A \cdot 8 G \cdot m_e$. |
| Prediction | $B_\mathrm{pred} = 2 \cdot m_e \cdot 4 \cdot 8 G = 29.956$ MeV vs $B_\mathrm{AME} = 28.296$. **err = +5.87%**. |

### $\ell = 2$ — α-cluster atoms (recursive: ref to ${}^{4}$He)

**Beryllium-8 ${}^{8}$Be = $2 \cdot {}^4\mathrm{He} + 1 \cdot c_{\alpha\alpha}$**

| Row | Content |
|--:|---|
| Braid (NF) | Two $^4$He cluster braids fused, plus one α–α pair-energy correction. |
| Prediction | $B_\mathrm{pred} = 2 B(^4\mathrm{He}_\mathrm{derived}) + c_{\alpha\alpha} = 62.34$ MeV vs $B_\mathrm{AME} = 56.50$. **err = +10.34%**. |

**Carbon-12 ${}^{12}$C = $3 \cdot {}^4\mathrm{He} + 3 \cdot c_{\alpha\alpha}$**

| Row | Content |
|--:|---|
| Braid (NF) | Three α-cluster fused (Hoyle state), three α–α pairs. |
| Prediction | $B_\mathrm{pred} = 97.15$ MeV vs $B_\mathrm{AME} = 92.16$. **err = +5.41%**. |

**Oxygen-16 ${}^{16}$O = $4 \cdot {}^4\mathrm{He} + 6 \cdot c_{\alpha\alpha}$**

| Row | Content |
|--:|---|
| Braid (NF) | Four α-cluster fused, six α–α pairs. |
| Prediction | $B_\mathrm{pred} = 134.38$ MeV vs $B_\mathrm{AME} = 127.62$. **err = +5.30%**. |

## Statistical summary

Principled entry summary:

- Tritium $^3$H: $\sim 1.6 \times 10^{-3}$ error (`manual-historical`).
- Deuteron $^2$H: $\sim 1.1 \times 10^{-2}$ error (`manual-historical`).
- $\alpha$-cluster atoms ${}^{8}$Be–${}^{40}$Ca: mean $|\mathrm{err}| \sim 8$% (`recursive-on-⁴He`).

The atlas covers $\ell \leq 2$ at $q_0$. The all-isotopes extension below covers $\ell = 3$ molecules and heavier nuclei.

## All-atoms / all-isotopes extension

A layered framework extends the atlas to all isotopes under a single registry:

| Layer | Coverage | Pipeline |
|---|---|---|
| **Layer 1** | Light isotopes ($A \leq 7$) | Canonical $\sum_\lambda y_\lambda \cdot \chi^\lambda(\beta_{\text{atom}})$ via Rust `hecke-canonical-chi` + mpmath $y_\lambda$ |
| **Layer 2** | $\alpha$-cluster magic nuclei ($A = 4 n_\alpha$) | Recursive on $^4$He + $\alpha$–$\alpha$ coupling $c_{\alpha\alpha}$ |
| **Layer 3** | Non-$\alpha$ intermediate ($5 \leq A \leq 40$) | Hybrid: nearest-$\alpha$-cluster + valence-nucleon via canonical interface |
| **Layer 4** | Heavy nuclei ($A > 40$) | Brane-tower asymptotic + LP-active-set ansatz |
| **Layer 5** | Theoretical / hypothetical isotopes | Same Layer-1/3 machinery; flagged `prediction-only` |

Per-isotope records follow the [`IsotopeRecord`](https://github.com/litlfred/qou/blob/main/computations/isotope_record_schema.py) schema with an explicit knot-operator catalogue. The Layer-1 pipeline is implemented in [`canonical_mass_table_extended.py`](https://github.com/litlfred/qou/blob/main/computations/canonical_mass_table_extended.py).

### Knot-operator catalogue — per-step primitives

Each per-isotope record lists the knot operators used to build its canonical braid:

**Intra-nucleon operators** (acting on the 3 strands at base $3k$):

| Operator | Formula | Closure |
|---|---|---|
| `proton intra` | $\sigma_0\,\sigma_0\,\sigma_0$ in $H_3$ | trefoil $3_1 = T(2,3)$ |
| `neutron intra` | $\sigma_0^{-1}\,\sigma_0^{-1}\,\sigma_0^{-1}$ in $H_3$ | mirror trefoil |
| `vortex` $\varrho$ | $\mathbf{1}_{B_1}$ (single-strand identity) | unknot $0_1$ |

**Inter-nucleon interfaces** (single-strand crossing at generator $3k+2$):

| Channel | Formula | Crossing kind |
|---|---|---|
| `pp` | $\sigma$ (positive crossing) | positive crossing |
| `nn` | $\sigma + (-h)\cdot\mathbf{1}$ | inverse crossing ($\sigma^{-1}$) |
| `pn` | $\sigma + \bigl(-h(1/2 - \delta/4)\bigr)\cdot\mathbf{1}$ (colour-tube-weighted average) | weighted-average crossing |

where $h = q_0 - q_0^{-1}$ and $\delta$ is the substrate flavour split of
[prop:flavor-split-substrate](#prop:flavor-split-substrate).

The $\delta = 0$ form $\sigma + (-h/2)\cdot\mathbf{1}$ (the unweighted
average) is **not** the `pn` interface: the unweighted average is the
intra-nucleon quark crossing, and it never appears at $3k+2$. Verified against the producer for
$\mathrm{D}$, ${}^{3}\mathrm{He}$ and ${}^{4}\mathrm{He}$ — every generator
$3k+2$ carries the positive crossing (p-p), the inverse crossing (n-n), or the weighted-average crossing (p-n), and
never the unweighted average. The two forms differ by $h\delta/4 \approx 7.190 \times
10^{-5}$ at the substrate anchor.

**Closure topology operators** (Markov closure $\widehat{\beta}$):

| Closure | Braid word | Application |
|---|---|---|
| Hopf link $L_H$ | $\sigma_1^2$ | photon polarisation pair |
| Borromean baryon $\mathcal{B}_3$ | $(\sigma_1 \sigma_2^{-1})^3$ | proton / neutron |
| Trefoil $3_1$ | $\sigma_1^3$ | electron |
| Figure-eight $4_1$ | $(\sigma_1 \sigma_2^{-1})^2$ | (notation, not currently used for matter) |
| Connected sum $K \mathbin{\#} K'$ | concatenation | composite atoms (recursive) |

**Fusion operators** (Layer 2 $\alpha$-cluster recursion):

| Fusion | Description |
|---|---|
| $c_{\alpha\alpha}$ | $\alpha$–$\alpha$ pair-energy correction (${}^{8}$Be, ${}^{12}$C, $\ldots$, ${}^{40}$Ca) |
| $\alpha$–N attachment | Layer 3: $^4$He cluster + valence nucleon (for non-magic $A$) |

For an atom with mass number $A$, the canonical braid word in $B_{3A}$ is built sequentially per nucleon. At each $k \in \{0, \dots, A-1\}$, the intra-nucleon block acts at base $3k$ and $3k+1$. For $k < A-1$, the inter-nucleon interface then acts at $3k+2$ between nucleons $k$ and $k+1$. The [`build_knot_operator_catalogue(Z, N)`](https://github.com/litlfred/qou/blob/main/computations/isotope_record_schema.py) function enumerates this sequence.

### Layer-1 canonical $|\mathrm{tr}_M(q_0)|$ table

**The binding column is census-assigned, not derived.** Each atom's knot is
selected so its volume reproduces $B_\mathrm{AME}/m_e$, and the $^4$He row is
$4\times$ the $^3$He row using the same $8G$. The `± 0.0000 %` is the AME
*experimental* uncertainty, not an error bar on a prediction. This column is
not a binding prediction.

<!-- AUTO:canonical-tr-m-table BEGIN -->

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_{\text{AME}}$ (MeV) | Binding Error | $M_{\text{atom}}$ (MeV) | $M_{\text{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| $\mathfrak{p}$ | 1 | 0 | — | — | — | 938.2721 | -0.00 $\pm$ 0.01 ppb |
| $\mathfrak{n}$ | 1 | 1 | — | — | — | 939.5659 | +501.43 $\pm$ 0.47 ppb |
| D | 2 | 1 | 2.2488 | 2.2246 | +1.09 $\pm$ 0.0000 % | — | — |
| T | 3 | 2 | 8.4686 | 8.4818 | -0.16 $\pm$ 0.0000 % | — | — |
| ${}^3$He | 3 | 1 | 7.4889 | 7.7180 | -2.97 $\pm$ 0.0000 % | — | — |
| ${}^4$He | 4 | 2 | 29.9557 | 28.2957 | +5.87 $\pm$ 0.0000 % | — | — |
| ${}^5$Li | 5 | 2 | — | 26.3280 | — | — | — |
| ${}^6$Li | 6 | 3 | — | 31.9940 | — | — | — |
| ${}^7$Li | 7 | 4 | — | 39.2452 | — | — | — |

_Computed via [`canonical_mass_table_extended.py`](https://github.com/litlfred/qou/blob/main/computations/canonical_mass_table_extended.py) (method=`auto`). Witness: [`canonical-mass-table-extended.witness.json`](https://github.com/litlfred/qou/blob/main/computations/canonical-mass-table-extended.witness.json). Nucleon masses (m_p, m_n) via [`canonical_mass.nucleon_mass_mev()`](https://github.com/litlfred/qou/blob/main/computations/canonical_mass.py). Paper hard floor (CAL-2 propagation): ~780 ppb._

<!-- AUTO:canonical-tr-m-table END -->

## Per-element stability summary ($Z = 1$ to $92$)

_This table summarizes element stability: predicted neutron count $N_{\mathrm{pred}}$, closed $\alpha$ sub-links $k_\alpha$, and the mass $M_q$ (the framework's dimensionless mass ratio rendered against the $m_e$ scale) versus observed AME2020 mass $M_o$. The subsequent per-Z sections provide full isotope chains and layer attributions. See [knot-periodic-table intro](#prose:knot-periodic-table) for derivations and conventions._

<!-- AUTO:stability-summary BEGIN -->
| $\#$ | Element | $Z$ | $N$ | $N_{\mathrm{pred}}$ | $\Delta$ | $k_\alpha$ | $M_q$ (MeV) | $M_o$ (MeV) | $B/A$ |
|---:|------|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Hydrogen | 1 | 0 | 1 | 1 | 0 | $938.7831$ | $938.7831$ | $0.0000$ |
| 2 | Helium$^{\diamond\star}$ | 2 | 2 | 2 | 0 | 1 | $3728.4013$ | $3728.4013$ | $7.0739$ |
| 3 | Lithium | 3 | 4 | 3 | 1 | 1 | — | — | — |
| 4 | Beryllium | 4 | 5 | 4 | 1 | 2 | — | — | — |
| 5 | Boron | 5 | 6 | 5 | 1 | 2 | — | — | — |
| 6 | Carbon | 6 | 6 | 6 | 0 | 3 | $11172.9431$ | $11177.9292$ | $7.6801$ |
| 7 | Nitrogen | 7 | 7 | 8 | 1 | 3 | — | — | — |
| 8 | Oxygen$^{\diamond\star}$ | 8 | 8 | 9 | 1 | 4 | $14892.4034$ | $14899.1687$ | $7.9762$ |
| 9 | Fluorine | 9 | 10 | 10 | 0 | 4 | — | — | — |
| 10 | Neon | 10 | 10 | 11 | 1 | 5 | $18609.4368$ | $18622.8401$ | $8.0322$ |
| 11 | Sodium | 11 | 12 | 12 | 0 | 5 | — | — | — |
| 12 | Magnesium | 12 | 12 | 14 | 2 | 6 | $22324.0432$ | $22341.9249$ | $8.2607$ |
| 13 | Aluminium | 13 | 14 | 15 | 1 | 6 | — | — | — |
| 14 | Silicon | 14 | 14 | 16 | 2 | 7 | — | — | — |
| 15 | Phosphorus | 15 | 16 | 17 | 1 | 7 | — | — | — |
| 16 | Sulfur | 16 | 16 | 19 | 3 | 8 | — | — | — |
| 17 | Chlorine | 17 | 18 | 20 | 2 | 8 | — | — | — |
| 18 | Argon | 18 | 22 | 21 | 1 | 9 | — | — | — |
| 19 | Potassium$^{\star}$ | 19 | 20 | 22 | 2 | 9 | — | — | — |
| 20 | Calcium$^{\diamond\star}$ | 20 | 20 | 24 | 4 | 10 | $37158.1989$ | $37224.9177$ | $8.5513$ |
| 21 | Scandium | 21 | 24 | 25 | 1 | 10 | $42171.2343$ | $41876.1623$ | $8.6189$ |
| 22 | Titanium | 22 | 26 | 26 | 0 | 11 | $44982.6333$ | $44663.2240$ | $8.7230$ |
| 23 | Vanadium$^{\star}$ | 23 | 28 | 28 | 0 | 11 | $47794.2284$ | $47453.9962$ | $8.7421$ |
| 24 | Chromium$^{\star}$ | 24 | 28 | 29 | 1 | 12 | $48738.4096$ | $48382.2739$ | $8.7760$ |
| 25 | Manganese | 25 | 30 | 30 | 0 | 12 | $51550.4085$ | $51174.4632$ | $8.7650$ |
| 26 | Iron | 26 | 30 | 32 | 2 | 13 | $52495.0803$ | $52103.0626$ | $8.7904$ |
| 27 | Cobalt | 27 | 32 | 33 | 1 | 13 | $55307.4715$ | $54895.9223$ | $8.7680$ |
| 28 | Nickel$^{\diamond}$ | 28 | 30 | 35 | 5 | 14 | $54385.2522$ | $53966.4291$ | $8.7321$ |
| 29 | Copper | 29 | 34 | 36 | 2 | 14 | $59065.3941$ | $58618.5487$ | $8.7521$ |
| 30 | Zinc | 30 | 34 | 37 | 3 | 15 | $60011.0085$ | $59549.6186$ | $8.7359$ |
| 31 | Gallium | 31 | 38 | 39 | 1 | 15 | $64691.4783$ | $64203.7653$ | $8.7246$ |
| 32 | Germanium | 32 | 42 | 40 | 2 | 16 | $69372.1434$ | $68857.1412$ | $8.7252$ |
| 33 | Arsenic | 33 | 42 | 42 | 0 | 16 | $70318.2658$ | $69789.0236$ | $8.7009$ |
| 34 | Selenium | 34 | 46 | 43 | 3 | 17 | $74999.2422$ | $74441.7688$ | $8.7108$ |
| 35 | Bromine | 35 | 44 | 45 | 1 | 17 | $74078.4829$ | $73511.9661$ | $8.6876$ |
| 36 | Krypton | 36 | 48 | 46 | 2 | 18 | $78759.7340$ | $78163.0654$ | $8.7174$ |
| 37 | Rubidium | 37 | 48 | 48 | 0 | 18 | $79706.6673$ | $79094.8315$ | $8.6974$ |
| 38 | Strontium$^{\star}$ | 38 | 50 | 49 | 1 | 19 | $82521.0089$ | $81883.5595$ | $8.7326$ |
| 39 | Yttrium$^{\star}$ | 39 | 50 | 51 | 1 | 19 | $83468.3675$ | $82815.2640$ | $8.7140$ |
| 40 | Zirconium$^{\star}$ | 40 | 50 | 52 | 2 | 20 | $84415.9672$ | $83745.6968$ | $8.7100$ |
| 41 | Niobium | 41 | 52 | 54 | 2 | 20 | $87230.8284$ | $86541.7388$ | $8.6642$ |
| 42 | Molybdenum | 42 | 56 | 55 | 1 | 21 | $91912.9047$ | $91198.3062$ | $8.6352$ |
| 43 | Technetium | 43 | 55 | 57 | 2 | 21 | $91927.5281$ | $91199.9900$ | $8.6100$ |
| 44 | Ruthenium | 44 | 58 | 58 | 0 | 22 | $95676.3692$ | $94923.2921$ | $8.6074$ |
| 45 | Rhodium | 45 | 58 | 60 | 2 | 22 | $96624.8996$ | $95855.8610$ | $8.5842$ |
| 46 | Palladium | 46 | 60 | 62 | 2 | 23 | $99440.5647$ | $98648.4675$ | $8.5800$ |
| 47 | Silver | 47 | 60 | 63 | 3 | 23 | $100389.4934$ | $99581.4624$ | $8.5539$ |
| 48 | Cadmium | 48 | 66 | 65 | 1 | 24 | $106939.2762$ | $106100.3129$ | $8.5315$ |
| 49 | Indium | 49 | 66 | 66 | 0 | 24 | $107888.4812$ | $107032.2856$ | $8.5165$ |
| 50 | Tin$^{\diamond}$ | 50 | 70 | 68 | 2 | 25 | $112571.6460$ | $111688.1947$ | $8.5045$ |
| 51 | Antimony | 51 | 70 | 70 | 0 | 25 | $113521.1822$ | $112621.1874$ | $8.4821$ |
| 52 | Tellurium | 52 | 78 | 71 | 7 | 26 | $121938.4477$ | $121006.8805$ | $8.4303$ |
| 53 | Iodine | 53 | 74 | 73 | 1 | 26 | $119154.4790$ | $118210.7680$ | $8.4455$ |
| 54 | Xenon | 54 | 78 | 75 | 3 | 27 | $123838.1762$ | $122867.9427$ | $8.4276$ |
| 55 | Caesium | 55 | 78 | 76 | 2 | 27 | $124788.3639$ | $123800.6449$ | $8.4100$ |
| 56 | Barium$^{\star}$ | 56 | 82 | 78 | 4 | 28 | $129472.3214$ | $128457.9245$ | $8.3934$ |
| 57 | Lanthanum$^{\star}$ | 57 | 82 | 80 | 2 | 28 | $130422.8295$ | $129390.4580$ | $8.3780$ |
| 58 | Cerium$^{\star}$ | 58 | 82 | 81 | 1 | 29 | $131373.5491$ | $130321.1003$ | $8.3763$ |
| 59 | Praseodymium$^{\star}$ | 59 | 82 | 83 | 1 | 29 | $132324.4791$ | $131254.6541$ | $8.3540$ |
| 60 | Neodymium$^{\star}$ | 60 | 82 | 85 | 3 | 30 | $133275.6185$ | $132186.2127$ | $8.3460$ |
| 61 | Promethium | 61 | 84 | 86 | 2 | 30 | $136093.5362$ | $134985.3775$ | $8.3027$ |
| 62 | Samarium | 62 | 90 | 88 | 2 | 31 | $142644.8213$ | $141512.3408$ | $8.2441$ |
| 63 | Europium | 63 | 90 | 90 | 0 | 31 | $143596.3724$ | $142445.2304$ | $8.2287$ |
| 64 | Gadolinium | 64 | 94 | 92 | 2 | 32 | $148281.2974$ | $147105.3784$ | $8.2018$ |
| 65 | Terbium | 65 | 94 | 93 | 1 | 32 | $149233.1547$ | $148038.0299$ | $8.1888$ |
| 66 | Dysprosium | 66 | 98 | 95 | 3 | 33 | $153918.3255$ | $152699.0654$ | $8.1587$ |
| 67 | Holmium | 67 | 98 | 97 | 1 | 33 | $154870.4862$ | $153631.6291$ | $8.1470$ |
| 68 | Erbium | 68 | 98 | 99 | 1 | 34 | $155822.8473$ | $154563.0971$ | $8.1419$ |
| 69 | Thulium | 69 | 100 | 101 | 1 | 34 | $158641.8669$ | $157361.2289$ | $8.1145$ |
| 70 | Ytterbium | 70 | 104 | 102 | 2 | 35 | $163327.5013$ | $162023.0295$ | $8.0838$ |
| 71 | Lutetium | 71 | 104 | 104 | 0 | 35 | $164280.3093$ | $162956.3025$ | $8.0691$ |
| 72 | Hafnium | 72 | 108 | 106 | 2 | 36 | $168966.1821$ | $167619.1592$ | $8.0349$ |
| 73 | Tantalum | 73 | 108 | 108 | 0 | 36 | $169919.2850$ | $168551.9937$ | $8.0234$ |
| 74 | Tungsten | 74 | 110 | 110 | 0 | 37 | $172738.9713$ | $171349.2096$ | $8.0051$ |
| 75 | Rhenium | 75 | 112 | 112 | 0 | 37 | $175558.7890$ | $174148.1808$ | $7.9780$ |
| 76 | Osmium | 76 | 116 | 114 | 2 | 38 | $180245.1310$ | $178810.9856$ | $7.9485$ |
| 77 | Iridium | 77 | 116 | 115 | 1 | 38 | $181198.8166$ | $179743.8257$ | $7.9381$ |
| 78 | Platinum | 78 | 117 | 117 | 0 | 39 | $183085.8551$ | $181608.5563$ | $7.9266$ |
| 79 | Gold | 79 | 118 | 119 | 1 | 39 | $184973.0451$ | $183473.1987$ | $7.9157$ |
| 80 | Mercury | 80 | 122 | 121 | 1 | 40 | $189659.8296$ | $188134.4636$ | $7.8969$ |
| 81 | Thallium | 81 | 124 | 123 | 1 | 40 | $192480.4242$ | $190932.4705$ | $7.8784$ |
| 82 | Lead$^{\diamond\star}$ | 82 | 126 | 125 | 1 | 41 | $195301.1464$ | $193729.0251$ | $7.8675$ |
| 83 | Bismuth$^{\star}$ | 83 | 126 | 127 | 1 | 41 | $196255.7342$ | $194664.0091$ | $7.8480$ |
| 84 | Polonium | 84 | 125 | 129 | 4 | 42 | $196277.4123$ | $194665.9017$ | $7.8352$ |
| 85 | Astatine | 85 | 125 | 131 | 6 | 42 | $197232.3949$ | $195601.7897$ | $7.8117$ |
| 86 | Radon | 86 | 136 | 133 | 3 | 43 | $208451.5494$ | $206808.0630$ | $7.6945$ |
| 87 | Francium | 87 | 136 | 135 | 1 | 43 | $209406.6527$ | $207741.5675$ | $7.6837$ |
| 88 | Radium | 88 | 138 | 137 | 1 | 44 | $212228.1296$ | $210541.3350$ | $7.6620$ |
| 89 | Actinium | 89 | 138 | 139 | 1 | 44 | $213183.5542$ | $211475.0111$ | $7.6507$ |
| 90 | Thorium | 90 | 142 | 141 | 1 | 45 | $217871.4553$ | $216142.0788$ | $7.6150$ |
| 91 | Protactinium | 91 | 140 | 143 | 3 | 45 | $216961.0363$ | $215208.5623$ | $7.6184$ |
| 92 | Uranium | 92 | 146 | 145 | 1 | 46 | $223515.2737$ | $221742.9044$ | $7.5701$ |
<!-- AUTO:stability-summary END -->

<!-- AUTO:per-z-sections BEGIN -->

## Per-element coverage (AME 2020 cross-reference)

_Auto-rendered from per-Z shards `canonical-isotope-witness-Z<NN>.witness.json` (emitted by [`canonical_isotope_witness.py`](https://github.com/litlfred/qou/blob/main/computations/canonical_isotope_witness.py)). Each row carries the framework value, the AME 2020 reference, and the residual. For free nucleons (p, n) the entry is the $m_e$-scaled rendering of the mass ratio conditional on the Borromean baryon mass formula conjecture. For D and up, the prediction is the binding energy; the AME 2020 reference is the total binding energy. $M_{\mathrm{atom}}$ is the composite atomic mass $N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$. The **CAL-3 Bound (ppb)** column represents the theoretical error floor propagated strictly from the empirical observation uncertainty of the neutron beta-decay $Q_\beta$ value (the CAL-3 anchor, $± 0.61$ eV). Because the theoretical neutron mass ratio $m_n/m_e$ is conditionally anchored on $Q_\beta$, each of the $N$ neutrons adds an unavoidable $± 0.61$ eV of experimental uncertainty to the rendered total atomic mass.

### neutron (Z = 0)

_0 of 1 isotopes with a framework prediction; 1 of 1 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| $\mathfrak{n}$ | 1 | 1 | — | — | 939.5654 | 939.5654 | +1.04 ± 0.47 | ±0.65 |

### Hydrogen (Z = 1)

_2 of 7 isotopes with a framework prediction; 3 of 7 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| $\mathfrak{p}$ | 1 | 0 | — | — | 938.7831 | 938.7831 | +14.47 ± 0.01 | ±0.00 |
| ${}^{2}$H | 2 | 1 | 2.2488 | +10903.07 ± 0.1798 | 1876.0997 | 1876.1239 | -12920.26 ± 0.01 | ±0.33 |
| ${}^{3}$H | 3 | 2 | 8.4686 | -1556.02 ± 0.1061 | 2809.4453 | 2809.4321 | +4703.24 ± 0.03 | ±0.43 |
| ${}^{4}$H | 4 | 3 | — | — | — | 3750.5975 | — | ±0.49 |
| ${}^{5}$H | 5 | 4 | — | — | — | 4690.3630 | — | ±0.52 |
| ${}^{6}$H | 6 | 5 | — | — | — | 5630.8403 | — | ±0.54 |
| ${}^{7}$H | 7 | 6 | — | — | — | 6569.5941 | — | ±0.56 |

### Helium (Z = 2)

_2 of 8 isotopes with a framework prediction; 2 of 8 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{3}$He | 3 | 1 | 7.4889 | -29686.55 ± 0.0583 | 2809.6427 | 2809.4135 | +81565.12 ± 0.02 | ±0.22 |
| ${}^{4}$He | 4 | 2 | 28.2957 | -0.08 ± 0.0283 | 3728.4014 | 3728.4013 | +8.46 ± 0.04 | ±0.33 |
| ${}^{5}$He | 5 | 3 | — | — | — | 4668.7018 | — | ±0.39 |
| ${}^{6}$He | 6 | 4 | — | — | — | 5606.5567 | — | ±0.44 |
| ${}^{7}$He | 7 | 5 | — | — | — | 6546.5319 | — | ±0.47 |
| ${}^{8}$He | 8 | 6 | — | — | — | 7483.5625 | — | ±0.49 |
| ${}^{9}$He | 9 | 7 | — | — | — | 8424.3828 | — | ±0.51 |
| ${}^{10}$He | 10 | 8 | — | — | — | 9364.1382 | — | ±0.52 |

### Lithium (Z = 3)

_2 of 11 isotopes with a framework prediction; 0 of 11 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{3}$Li | 3 | 0 | — | — | — | 2823.1490 | — | ±0.00 |
| ${}^{4}$Li | 4 | 1 | — | — | — | 3751.2996 | — | ±0.16 |
| ${}^{5}$Li | 5 | 2 | — | — | — | 4669.1494 | — | ±0.26 |
| ${}^{6}$Li | 6 | 3 | 43.6570 | +364537.17 ± 0.0563 | — | 5603.0515 | — | ±0.33 |
| ${}^{7}$Li | 7 | 4 | 51.3376 | +308129.48 ± 0.1070 | — | 6535.3658 | — | ±0.37 |
| ${}^{8}$Li | 8 | 5 | — | — | — | 7472.8986 | — | ±0.41 |
| ${}^{9}$Li | 9 | 6 | — | — | — | 8408.4018 | — | ±0.44 |
| ${}^{10}$Li | 10 | 7 | — | — | — | 9347.9937 | — | ±0.46 |
| ${}^{11}$Li | 11 | 8 | — | — | — | 10287.1634 | — | ±0.47 |
| ${}^{12}$Li | 12 | 9 | — | — | — | 11226.9388 | — | ±0.49 |
| ${}^{13}$Li | 13 | 10 | — | — | — | 12166.4042 | — | ±0.50 |

### Beryllium (Z = 4)

_3 of 12 isotopes with a framework prediction; 1 of 12 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{5}$Be | 5 | 1 | — | — | — | 4694.6092 | — | ±0.13 |
| ${}^{6}$Be | 6 | 2 | — | — | — | 5607.3397 | — | ±0.22 |
| ${}^{7}$Be | 7 | 3 | — | — | — | 6536.2277 | — | ±0.28 |
| ${}^{8}$Be | 8 | 4 | 62.3383 | +103343.58 ± 0.6230 | 7451.0557 | 7456.8945 | -783006.99 ± 4.62 | ±0.33 |
| ${}^{9}$Be | 9 | 5 | 67.3057 | +157170.96 ± 1.3152 | — | 8394.7954 | — | ±0.36 |
| ${}^{10}$Be | 10 | 6 | 75.5931 | +163395.30 ± 1.2466 | — | 9327.5485 | — | ±0.39 |
| ${}^{11}$Be | 11 | 7 | — | — | — | 10266.6123 | — | ±0.42 |
| ${}^{12}$Be | 12 | 8 | — | — | — | 11203.0070 | — | ±0.44 |
| ${}^{13}$Be | 13 | 9 | — | — | — | 12143.0824 | — | ±0.45 |
| ${}^{14}$Be | 14 | 10 | — | — | — | 13080.8720 | — | ±0.47 |
| ${}^{15}$Be | 15 | 11 | — | — | — | 14022.2374 | — | ±0.48 |
| ${}^{16}$Be | 16 | 12 | — | — | — | 14961.3528 | — | ±0.49 |

### Boron (Z = 5)

_2 of 16 isotopes with a framework prediction; 0 of 16 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{6}$B | 6 | 1 | — | — | — | 5636.2845 | — | ±0.11 |
| ${}^{7}$B | 7 | 2 | — | — | — | 6548.1353 | — | ±0.19 |
| ${}^{8}$B | 8 | 3 | — | — | — | 7474.8744 | — | ±0.24 |
| ${}^{9}$B | 9 | 4 | — | — | — | 8395.8634 | — | ±0.29 |
| ${}^{10}$B | 10 | 5 | 75.5931 | +167446.40 ± 0.2317 | — | 9326.9916 | — | ±0.33 |
| ${}^{11}$B | 11 | 6 | 83.8805 | +100721.45 ± 0.1588 | — | 10255.1028 | — | ±0.36 |
| ${}^{12}$B | 12 | 7 | — | — | — | 11191.2986 | — | ±0.38 |
| ${}^{13}$B | 13 | 8 | — | — | — | 12125.9853 | — | ±0.40 |
| ${}^{14}$B | 14 | 9 | — | — | — | 13064.5811 | — | ±0.42 |
| ${}^{15}$B | 15 | 10 | — | — | — | 14001.3689 | — | ±0.44 |
| ${}^{16}$B | 16 | 11 | — | — | — | 14941.0174 | — | ±0.45 |
| ${}^{17}$B | 17 | 12 | — | — | — | 15879.1161 | — | ±0.46 |
| ${}^{18}$B | 18 | 13 | — | — | — | 16818.6865 | — | ±0.47 |
| ${}^{19}$B | 19 | 14 | — | — | — | 17758.1582 | — | ±0.48 |
| ${}^{20}$B | 20 | 15 | — | — | — | 18699.2836 | — | ±0.49 |
| ${}^{21}$B | 21 | 16 | — | — | — | 19639.7591 | — | ±0.50 |

### Carbon (Z = 6)

_2 of 16 isotopes with a framework prediction; 1 of 16 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{8}$C | 8 | 2 | — | — | — | 7487.0171 | — | ±0.16 |
| ${}^{9}$C | 9 | 3 | — | — | — | 8412.3579 | — | ±0.22 |
| ${}^{10}$C | 10 | 4 | — | — | — | 9330.6397 | — | ±0.26 |
| ${}^{11}$C | 11 | 5 | — | — | — | 10257.0845 | — | ±0.30 |
| ${}^{12}$C | 12 | 6 | 97.1480 | +54103.42 ± 0.0260 | 11172.9431 | 11177.9292 | -446073.51 ± 0.00 | ±0.33 |
| ${}^{13}$C | 13 | 7 | 101.0621 | +40718.17 ± 0.0268 | — | 12112.5484 | — | ±0.35 |
| ${}^{14}$C | 14 | 8 | — | — | — | 13043.9373 | — | ±0.37 |
| ${}^{15}$C | 15 | 9 | — | — | — | 13982.2847 | — | ±0.39 |
| ${}^{16}$C | 16 | 10 | — | — | — | 14917.5998 | — | ±0.41 |
| ${}^{17}$C | 17 | 11 | — | — | — | 15856.4316 | — | ±0.42 |
| ${}^{18}$C | 18 | 12 | — | — | — | 16791.8131 | — | ±0.44 |
| ${}^{19}$C | 19 | 13 | — | — | — | 17730.8017 | — | ±0.45 |
| ${}^{20}$C | 20 | 14 | — | — | — | 18667.3856 | — | ±0.46 |
| ${}^{21}$C | 21 | 15 | — | — | — | 19607.0194 | — | ±0.47 |
| ${}^{22}$C | 22 | 16 | — | — | — | 20546.4815 | — | ±0.48 |
| ${}^{23}$C | 23 | 17 | — | — | — | 21488.5350 | — | ±0.48 |

### Nitrogen (Z = 7)

_2 of 16 isotopes with a framework prediction; 0 of 16 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{10}$N | 10 | 3 | — | — | — | 9353.7411 | — | ±0.20 |
| ${}^{11}$N | 11 | 4 | — | — | — | 10270.8008 | — | ±0.24 |
| ${}^{12}$N | 12 | 5 | — | — | — | 11195.2673 | — | ±0.27 |
| ${}^{13}$N | 13 | 6 | — | — | — | 12114.7688 | — | ±0.30 |
| ${}^{14}$N | 14 | 7 | 109.9563 | +50618.44 ± 0.0268 | — | 13043.7809 | — | ±0.33 |
| ${}^{15}$N | 15 | 8 | 118.8504 | +29080.09 ± 0.0260 | — | 13972.5130 | — | ±0.35 |
| ${}^{16}$N | 16 | 9 | — | — | — | 14909.5896 | — | ±0.37 |
| ${}^{17}$N | 17 | 10 | — | — | — | 15843.2698 | — | ±0.39 |
| ${}^{18}$N | 18 | 11 | — | — | — | 16780.0070 | — | ±0.40 |
| ${}^{19}$N | 19 | 12 | — | — | — | 17714.2442 | — | ±0.41 |
| ${}^{20}$N | 20 | 13 | — | — | — | 18651.6486 | — | ±0.43 |
| ${}^{21}$N | 21 | 14 | — | — | — | 19586.6081 | — | ±0.44 |
| ${}^{22}$N | 22 | 15 | — | — | — | 20524.6351 | — | ±0.45 |
| ${}^{23}$N | 23 | 16 | — | — | — | 21461.0848 | — | ±0.45 |
| ${}^{24}$N | 24 | 17 | — | — | — | 22402.7965 | — | ±0.46 |
| ${}^{25}$N | 25 | 18 | — | — | — | 23343.3354 | — | ±0.47 |

### Oxygen (Z = 8)

_3 of 18 isotopes with a framework prediction; 1 of 18 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{11}$O | 11 | 3 | — | — | — | 10294.1741 | — | ±0.18 |
| ${}^{12}$O | 12 | 4 | — | — | — | 11209.9426 | — | ±0.22 |
| ${}^{13}$O | 13 | 5 | — | — | — | 12132.5388 | — | ±0.25 |
| ${}^{14}$O | 14 | 6 | — | — | — | 13048.9252 | — | ±0.28 |
| ${}^{15}$O | 15 | 7 | — | — | — | 13975.2672 | — | ±0.31 |
| ${}^{16}$O | 16 | 8 | 134.3846 | +53011.81 ± 0.0251 | 14892.4034 | 14899.1687 | -454066.57 ± 0.02 | ±0.33 |
| ${}^{17}$O | 17 | 9 | 137.2455 | +41613.44 ± 0.0258 | — | 15834.5910 | — | ±0.35 |
| ${}^{18}$O | 18 | 10 | 146.7464 | +49629.72 ± 0.0257 | — | 16766.1111 | — | ±0.36 |
| ${}^{19}$O | 19 | 11 | — | — | — | 17701.7208 | — | ±0.38 |
| ${}^{20}$O | 20 | 12 | — | — | — | 18633.6782 | — | ±0.39 |
| ${}^{21}$O | 21 | 13 | — | — | — | 19569.4382 | — | ±0.41 |
| ${}^{22}$O | 22 | 14 | — | — | — | 20502.1533 | — | ±0.42 |
| ${}^{23}$O | 23 | 15 | — | — | — | 21438.9858 | — | ±0.43 |
| ${}^{24}$O | 24 | 16 | — | — | — | 22374.3589 | — | ±0.44 |
| ${}^{25}$O | 25 | 17 | — | — | — | 23314.6816 | — | ±0.44 |
| ${}^{26}$O | 26 | 18 | — | — | — | 24253.5077 | — | ±0.45 |
| ${}^{27}$O | 27 | 19 | — | — | — | 25195.0106 | — | ±0.46 |
| ${}^{28}$O | 28 | 20 | — | — | — | 26133.9147 | — | ±0.47 |

### Fluorine (Z = 9)

_1 of 19 isotopes with a framework prediction; 0 of 19 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{13}$F | 13 | 4 | — | — | — | 12151.4533 | — | ±0.20 |
| ${}^{14}$F | 14 | 5 | — | — | — | 13072.8819 | — | ±0.23 |
| ${}^{15}$F | 15 | 6 | — | — | — | 13988.9783 | — | ±0.26 |
| ${}^{16}$F | 16 | 7 | — | — | — | 14914.5808 | — | ±0.29 |
| ${}^{17}$F | 17 | 8 | — | — | — | 15837.3515 | — | ±0.31 |
| ${}^{18}$F | 18 | 9 | — | — | — | 16767.7670 | — | ±0.33 |
| ${}^{19}$F | 19 | 10 | 156.2473 | +57143.76 ± 0.0257 | — | 17696.9005 | — | ±0.34 |
| ${}^{20}$F | 20 | 11 | — | — | — | 18629.8646 | — | ±0.36 |
| ${}^{21}$F | 21 | 12 | — | — | — | 19561.3286 | — | ±0.37 |
| ${}^{22}$F | 22 | 13 | — | — | — | 20495.6637 | — | ±0.39 |
| ${}^{23}$F | 23 | 14 | — | — | — | 21427.6496 | — | ±0.40 |
| ${}^{24}$F | 24 | 15 | — | — | — | 22363.4030 | — | ±0.41 |
| ${}^{25}$F | 25 | 16 | — | — | — | 23298.6868 | — | ±0.42 |
| ${}^{26}$F | 26 | 17 | — | — | — | 24237.5214 | — | ±0.43 |
| ${}^{27}$F | 27 | 18 | — | — | — | 25175.4743 | — | ±0.44 |
| ${}^{28}$F | 28 | 19 | — | — | — | 26115.2387 | — | ±0.44 |
| ${}^{29}$F | 29 | 20 | — | — | — | 27053.4792 | — | ±0.45 |
| ${}^{30}$F | 30 | 21 | — | — | — | 27993.7834 | — | ±0.46 |
| ${}^{31}$F | 31 | 22 | — | — | — | 28933.1598 | — | ±0.46 |

### Neon (Z = 10)

_3 of 20 isotopes with a framework prediction; 1 of 20 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{15}$Ne | 15 | 5 | — | — | — | 14012.6269 | — | ±0.22 |
| ${}^{16}$Ne | 16 | 6 | — | — | — | 14927.8924 | — | ±0.25 |
| ${}^{17}$Ne | 17 | 7 | — | — | — | 15851.9002 | — | ±0.27 |
| ${}^{18}$Ne | 18 | 8 | — | — | — | 16772.2115 | — | ±0.29 |
| ${}^{19}$Ne | 19 | 9 | — | — | — | 17700.1400 | — | ±0.31 |
| ${}^{20}$Ne | 20 | 10 | 174.0483 | +83435.35 ± 0.0249 | 18609.4368 | 18622.8401 | -719724.39 ± 0.08 | ±0.33 |
| ${}^{21}$Ne | 21 | 11 | 175.8558 | +50475.26 ± 0.2258 | — | 19555.6444 | — | ±0.34 |
| ${}^{22}$Ne | 22 | 12 | 185.9635 | +46089.02 ± 0.0990 | — | 20484.8456 | — | ±0.36 |
| ${}^{23}$Ne | 23 | 13 | — | — | — | 21419.2103 | — | ±0.37 |
| ${}^{24}$Ne | 24 | 14 | — | — | — | 22349.9068 | — | ±0.38 |
| ${}^{25}$Ne | 25 | 15 | — | — | — | 23285.3171 | — | ±0.39 |
| ${}^{26}$Ne | 26 | 16 | — | — | — | 24219.3278 | — | ±0.40 |
| ${}^{27}$Ne | 27 | 17 | — | — | — | 25157.3917 | — | ±0.41 |
| ${}^{28}$Ne | 28 | 18 | — | — | — | 26093.1346 | — | ±0.42 |
| ${}^{29}$Ne | 29 | 19 | — | — | — | 27031.7288 | — | ±0.43 |
| ${}^{30}$Ne | 30 | 20 | — | — | — | 27968.1032 | — | ±0.44 |
| ${}^{31}$Ne | 31 | 21 | — | — | — | 28907.4988 | — | ±0.44 |
| ${}^{32}$Ne | 32 | 22 | — | — | — | 29844.8103 | — | ±0.45 |
| ${}^{33}$Ne | 33 | 23 | — | — | — | 30785.4358 | — | ±0.46 |
| ${}^{34}$Ne | 34 | 24 | — | — | — | 31723.6413 | — | ±0.46 |

### Fermium (Z = 100)

_20 of 20 isotopes with a framework prediction; 20 of 20 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{241}$Fm | 241 | 141 | -146.6045 | -1081554.81 ± 134.0662 | 226503.6379 | 224559.2993 | +8658464.28 ± 1335.69 | ±0.38 |
| ${}^{242}$Fm | 242 | 142 | -139.9027 | -1077442.80 ± 267.9169 | 227436.5016 | 225489.9727 | +8632441.03 ± 1776.32 | ±0.38 |
| ${}^{243}$Fm | 243 | 143 | -133.2092 | -1073444.00 ± 133.9764 | 228369.3735 | 226422.3834 | +8598929.43 ± 575.96 | ±0.39 |
| ${}^{244}$Fm | 244 | 144 | -126.5238 | -1069434.96 ± 133.9047 | 229302.2535 | 227353.5254 | +8571356.59 ± 884.98 | ±0.39 |
| ${}^{245}$Fm | 245 | 145 | -119.8465 | -1065528.39 ± 133.9585 | 230235.1416 | 228286.2472 | +8537064.56 ± 856.88 | ±0.39 |
| ${}^{246}$Fm | 246 | 146 | -113.1772 | -1061605.82 ± 7.4451 | 231168.0377 | 229217.7407 | +8508490.81 ± 59.64 | ±0.39 |
| ${}^{247}$Fm | 247 | 147 | -106.5158 | -1057775.71 ± 133.9764 | 232100.9418 | 230150.7165 | +8473687.51 ± 785.18 | ±0.39 |
| ${}^{248}$Fm | 248 | 148 | -99.8622 | -1053934.25 ± 4.5942 | 233033.8536 | 231082.4355 | +8444683.76 ± 36.77 | ±0.39 |
| ${}^{249}$Fm | 249 | 149 | -93.2164 | -1050170.17 ± 3.3370 | 233966.7732 | 232015.5510 | +8409877.05 ± 26.77 | ±0.39 |
| ${}^{250}$Fm | 250 | 150 | -86.5783 | -1046409.67 ± 4.2347 | 234899.7005 | 232947.5981 | +8380006.66 ± 33.86 | ±0.39 |
| ${}^{251}$Fm | 251 | 151 | -79.9478 | -1042713.85 ± 7.6304 | 235832.6355 | 233880.9788 | +8344657.45 ± 61.10 | ±0.39 |
| ${}^{252}$Fm | 252 | 152 | -73.3249 | -1039025.01 ± 2.7763 | 236765.5780 | 234813.3307 | +8314039.26 ± 22.23 | ±0.39 |
| ${}^{253}$Fm | 253 | 153 | -66.7095 | -1035399.72 ± 0.8190 | 237698.5280 | 235747.3538 | +8276547.64 ± 6.57 | ±0.40 |
| ${}^{254}$Fm | 254 | 154 | -60.1015 | -1031783.28 ± 0.9806 | 238631.4854 | 236680.4049 | +8243523.77 ± 7.78 | ±0.40 |
| ${}^{255}$Fm | 255 | 155 | -53.5008 | -1028215.48 ± 2.0710 | 239564.4502 | 237614.7969 | +8205100.40 ± 16.55 | ±0.40 |
| ${}^{256}$Fm | 256 | 156 | -46.9074 | -1024655.20 ± 1.5878 | 240497.4222 | 238547.9753 | +8172137.65 ± 12.66 | ±0.40 |
| ${}^{257}$Fm | 257 | 157 | -40.3213 | -1021138.26 ± 2.2770 | 241430.4015 | 239482.5748 | +8133479.98 ± 18.16 | ±0.40 |
| ${}^{258}$Fm | 258 | 158 | -33.7423 | -1017630.66 ± 134.8072 | 242363.3880 | 240415.9054 | +8100472.99 ± 833.02 | ±0.40 |
| ${}^{259}$Fm | 259 | 159 | -27.1704 | -1014162.98 ± 135.0074 | 243296.3815 | 241350.6774 | +8061730.23 ± 1173.29 | ±0.40 |
| ${}^{260}$Fm | 260 | 160 | -20.6056 | -1010706.87 ± 270.1972 | 244229.3821 | 242284.2329 | +8028376.82 ± 1795.44 | ±0.40 |

### Mendelevium (Z = 101)

_19 of 19 isotopes with a framework prediction; 19 of 19 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{244}$Md | 244 | 143 | -151.8827 | -1083687.83 ± 268.8895 | 229326.8301 | 227360.1586 | +8650026.97 ± 1646.99 | ±0.38 |
| ${}^{245}$Md | 245 | 144 | -145.1750 | -1079633.28 ± 134.3905 | 230259.6878 | 228291.3798 | +8621911.61 ± 1138.40 | ±0.38 |
| ${}^{246}$Md | 246 | 145 | -138.4755 | -1075649.61 ± 134.3905 | 231192.5538 | 229223.6647 | +8589379.64 ± 1133.77 | ±0.39 |
| ${}^{247}$Md | 247 | 146 | -131.7841 | -1071673.69 ± 134.3364 | 232125.4278 | 230154.9790 | +8561399.63 ± 902.54 | ±0.39 |
| ${}^{248}$Md | 248 | 147 | -125.1007 | -1067782.62 ± 134.3725 | 233058.3098 | 231087.4857 | +8528476.16 ± 798.12 | ±0.39 |
| ${}^{249}$Md | 249 | 148 | -118.4252 | -1063890.67 ± 88.7021 | 233991.1997 | 232019.2128 | +8499239.75 ± 708.66 | ±0.39 |
| ${}^{250}$Md | 250 | 149 | -111.7576 | -1060071.36 ± 48.8735 | 234924.0975 | 232951.9251 | +8466006.04 ± 390.29 | ±0.39 |
| ${}^{251}$Md | 251 | 150 | -105.0977 | -1056264.65 ± 10.1318 | 235857.0030 | 233883.9868 | +8435875.76 ± 80.89 | ±0.39 |
| ${}^{252}$Md | 252 | 151 | -98.4455 | -1052518.63 ± 48.6930 | 236789.9163 | 234816.9813 | +8402011.83 ± 388.76 | ±0.39 |
| ${}^{253}$Md | 253 | 152 | -91.8010 | -1048783.27 ± 0.0000 | 237722.8372 | 235749.1814 | +8371845.79 ± 134.34 | ±0.39 |
| ${}^{254}$Md | 254 | 153 | -85.1641 | -1045114.60 ± 0.0000 | 238655.7657 | 236682.9549 | +8335246.65 ± 421.11 | ±0.39 |
| ${}^{255}$Md | 255 | 154 | -78.5347 | -1041457.82 ± 2.9346 | 239588.7017 | 237615.8385 | +8302742.75 ± 23.43 | ±0.40 |
| ${}^{256}$Md | 256 | 155 | -71.9127 | -1037853.23 ± 0.0000 | 240521.6451 | 238549.9467 | +8265348.53 ± 519.34 | ±0.40 |
| ${}^{257}$Md | 257 | 156 | -65.2980 | -1034253.46 ± 0.8224 | 241454.5959 | 239482.9771 | +8232813.92 ± 6.55 | ±0.40 |
| ${}^{258}$Md | 258 | 157 | -58.6907 | -1030700.91 ± 1.8219 | 242387.5540 | 240417.1691 | +8195691.31 ± 14.45 | ±0.40 |
| ${}^{259}$Md | 259 | 158 | -52.0906 | -1027160.31 ± 0.0000 | 243320.5194 | 241350.5368 | +8162329.31 ± 416.83 | ±0.40 |
| ${}^{260}$Md | 260 | 159 | -45.4977 | -1023660.25 ± 135.2082 | 244253.4919 | 242285.0163 | +8124627.60 ± 1303.33 | ±0.40 |
| ${}^{261}$Md | 261 | 160 | -38.9119 | -1020171.53 ± 270.5994 | 245186.4715 | 243218.5392 | +8091209.91 ± 2091.11 | ±0.40 |
| ${}^{262}$Md | 262 | 161 | -32.3332 | -1016717.56 ± 270.9293 | 246119.4582 | 244153.1222 | +8053699.95 ± 1835.11 | ±0.40 |

### Nobelium (Z = 102)

_17 of 17 isotopes with a framework prediction; 17 of 17 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{248}$No | 248 | 146 | -150.5659 | -1081778.11 ± 134.6983 | 233082.9927 | 231091.2265 | +8618960.42 ± 971.43 | ±0.39 |
| ${}^{249}$No | 249 | 147 | -143.8604 | -1077843.27 ± 134.7346 | 234015.8526 | 232023.8189 | +8585470.85 ± 1204.39 | ±0.39 |
| ${}^{250}$No | 250 | 148 | -137.1630 | -1073882.56 ± 134.6620 | 234948.7205 | 232955.0922 | +8557994.24 ± 859.70 | ±0.39 |
| ${}^{251}$No | 251 | 149 | -130.4734 | -1070027.54 ± 134.7164 | 235881.5964 | 233887.8690 | +8524287.54 ± 772.63 | ±0.39 |
| ${}^{252}$No | 252 | 150 | -123.7917 | -1066152.76 ± 4.9692 | 236814.4802 | 234819.3855 | +8496294.57 ± 39.57 | ±0.39 |
| ${}^{253}$No | 253 | 151 | -117.1179 | -1062366.89 ± 3.6780 | 237747.3717 | 235752.3669 | +8462289.52 ± 29.32 | ±0.39 |
| ${}^{254}$No | 254 | 152 | -110.4517 | -1058576.67 ± 5.1188 | 238680.2710 | 236684.2257 | +8433368.65 ± 40.80 | ±0.39 |
| ${}^{255}$No | 255 | 153 | -103.7932 | -1054871.32 ± 7.4279 | 239613.1779 | 237617.8084 | +8397390.48 ± 59.11 | ±0.39 |
| ${}^{256}$No | 256 | 154 | -97.1423 | -1051164.28 ± 3.9776 | 240546.0924 | 238550.3136 | +8366280.39 ± 31.64 | ±0.39 |
| ${}^{257}$No | 257 | 155 | -90.4989 | -1047523.88 ± 3.2525 | 241479.0144 | 239484.2317 | +8329494.99 ± 25.87 | ±0.39 |
| ${}^{258}$No | 258 | 156 | -83.8629 | -1043884.18 ± 0.0000 | 242411.9439 | 240416.9561 | +8298032.69 ± 414.57 | ±0.40 |
| ${}^{259}$No | 259 | 157 | -77.2344 | -1040297.75 ± 3.3243 | 243344.8808 | 241351.0522 | +8261113.81 ± 26.36 | ±0.40 |
| ${}^{260}$No | 260 | 158 | -70.6131 | -1036716.09 ± 135.1899 | 244277.8249 | 242284.0765 | +8228970.32 ± 826.60 | ±0.40 |
| ${}^{261}$No | 261 | 159 | -63.9991 | -1033189.95 ± 135.3546 | 245210.7764 | 243218.4163 | +8191649.77 ± 823.42 | ±0.40 |
| ${}^{262}$No | 262 | 160 | -57.3923 | -1029662.10 ± 135.4096 | 246143.7350 | 244151.5563 | +8159598.39 ± 1476.49 | ±0.40 |
| ${}^{263}$No | 263 | 161 | -50.7926 | -1026183.28 ± 271.1497 | 247076.7007 | 245086.0787 | +8122134.12 ± 1999.16 | ±0.40 |
| ${}^{264}$No | 264 | 162 | -44.2000 | -1022713.92 ± 271.3336 | 248009.6735 | 246019.4544 | +8089681.75 ± 2400.49 | ±0.40 |

### Lawrencium (Z = 103)

_16 of 16 isotopes with a framework prediction; 16 of 16 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{251}$Lr | 251 | 148 | -156.0750 | -1084028.75 ± 135.1351 | 235906.4157 | 233892.8497 | +8608924.97 ± 856.25 | ±0.39 |
| ${}^{252}$Lr | 252 | 149 | -149.3635 | -1080096.26 ± 135.1351 | 236839.2696 | 234825.0508 | +8577529.57 ± 785.42 | ±0.39 |
| ${}^{253}$Lr | 253 | 150 | -142.6600 | -1076169.07 ± 87.8437 | 237772.1315 | 235756.5317 | +8549497.05 ± 697.90 | ±0.39 |
| ${}^{254}$Lr | 254 | 151 | -135.9643 | -1072325.78 ± 48.5737 | 238705.0012 | 236689.1482 | +8516879.72 ± 385.78 | ±0.39 |
| ${}^{255}$Lr | 255 | 152 | -129.2764 | -1068485.13 ± 9.3751 | 239637.8788 | 237620.9438 | +8488035.67 ± 74.48 | ±0.39 |
| ${}^{256}$Lr | 256 | 153 | -122.5963 | -1064731.20 ± 43.7676 | 240570.7641 | 238554.2372 | +8453117.27 ± 347.52 | ±0.39 |
| ${}^{257}$Lr | 257 | 154 | -115.9238 | -1060979.53 ± 0.0000 | 241503.6571 | 239486.6497 | +8422212.14 ± 182.81 | ±0.39 |
| ${}^{258}$Lr | 258 | 155 | -109.2590 | -1057289.56 ± 0.0000 | 242436.5576 | 240420.2611 | +8386550.00 ± 422.31 | ±0.39 |
| ${}^{259}$Lr | 259 | 156 | -102.6017 | -1053605.60 ± 0.0000 | 243369.4657 | 241352.8236 | +8355577.00 ± 293.32 | ±0.39 |
| ${}^{260}$Lr | 260 | 157 | -95.9518 | -1049985.82 ± 0.0000 | 244302.3813 | 242286.7433 | +8319225.04 ± 515.18 | ±0.40 |
| ${}^{261}$Lr | 261 | 158 | -89.3093 | -1046359.75 ± 135.4830 | 245235.3042 | 243219.5182 | +8287928.54 ± 823.42 | ±0.40 |
| ${}^{262}$Lr | 262 | 159 | -82.6742 | -1042792.28 ± 135.6116 | 246168.2345 | 244153.5609 | +8251665.85 ± 820.27 | ±0.40 |
| ${}^{263}$Lr | 263 | 160 | -76.0463 | -1039227.98 ± 135.6668 | 247101.1721 | 245086.6181 | +8219763.37 ± 912.16 | ±0.40 |
| ${}^{264}$Lr | 264 | 161 | -69.4256 | -1035715.87 ± 271.6284 | 248034.1168 | 246020.8181 | +8183448.40 ± 1771.96 | ±0.40 |
| ${}^{265}$Lr | 265 | 162 | -62.8121 | -1032209.12 ± 271.7761 | 248967.0687 | 246954.1706 | +8150897.53 ± 2214.12 | ±0.40 |
| ${}^{266}$Lr | 266 | 163 | -56.2057 | -1028752.15 ± 272.1459 | 249900.0277 | 247889.0935 | +8112233.42 ± 2175.71 | ±0.40 |

### Rutherfordium (Z = 104)

_16 of 16 isotopes with a framework prediction; 16 of 16 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{253}$Rf | 253 | 149 | -168.4273 | -1090206.05 ± 271.0027 | 237797.1165 | 235761.6495 | +8633579.88 ± 1738.44 | ±0.39 |
| ${}^{254}$Rf | 254 | 150 | -161.7019 | -1086216.35 ± 135.4280 | 238729.9565 | 236692.7030 | +8607166.41 ± 1196.38 | ±0.39 |
| ${}^{255}$Rf | 255 | 151 | -154.9844 | -1082332.94 ± 135.4646 | 239662.8044 | 237625.3261 | +8574331.52 ± 760.48 | ±0.39 |
| ${}^{256}$Rf | 256 | 152 | -148.2747 | -1078424.38 ± 9.4375 | 240595.6602 | 238556.7125 | +8547014.34 ± 74.81 | ±0.39 |
| ${}^{257}$Rf | 257 | 153 | -141.5729 | -1074626.04 ± 5.7033 | 241528.5238 | 239489.8510 | +8512564.32 ± 45.16 | ±0.39 |
| ${}^{258}$Rf | 258 | 154 | -134.8789 | -1070814.02 ± 8.4524 | 242461.3952 | 240421.8231 | +8483306.75 ± 66.98 | ±0.39 |
| ${}^{259}$Rf | 259 | 155 | -128.1925 | -1067093.90 ± 0.0000 | 243394.2742 | 241355.3396 | +8447853.89 ± 301.04 | ±0.39 |
| ${}^{260}$Rf | 260 | 156 | -121.5137 | -1063353.73 ± 135.5565 | 244327.1609 | 242287.6152 | +8417870.10 ± 826.58 | ±0.39 |
| ${}^{261}$Rf | 261 | 157 | -114.8425 | -1059691.57 ± 34.1320 | 245260.0551 | 243221.2793 | +8382390.60 ± 269.97 | ±0.39 |
| ${}^{262}$Rf | 262 | 158 | -108.1788 | -1056023.88 ± 135.6852 | 246192.9567 | 244153.8478 | +8351737.89 ± 915.65 | ±0.39 |
| ${}^{263}$Rf | 263 | 159 | -101.5224 | -1052419.45 ± 135.7958 | 247125.8658 | 245087.7060 | +8316042.56 ± 623.31 | ±0.40 |
| ${}^{264}$Rf | 264 | 160 | -94.8734 | -1048820.68 ± 135.8511 | 248058.7823 | 246020.5182 | +8284935.23 ± 1465.28 | ±0.40 |
| ${}^{265}$Rf | 265 | 161 | -88.2317 | -1045274.67 ± 135.9804 | 248991.7060 | 246954.6270 | +8248798.55 ± 1459.73 | ±0.40 |
| ${}^{266}$Rf | 266 | 162 | -81.5972 | -1041729.91 ± 272.0718 | 249924.6369 | 247887.5677 | +8217714.23 ± 1664.67 | ±0.40 |
| ${}^{267}$Rf | 267 | 163 | -74.9699 | -1038243.83 ± 272.4053 | 250857.5750 | 248822.3696 | +8179350.80 ± 2309.81 | ±0.40 |
| ${}^{268}$Rf | 268 | 164 | -68.3497 | -1034760.27 ± 272.5910 | 251790.5202 | 249755.8953 | +8146454.14 ± 2651.76 | ±0.40 |

### Dubnium (Z = 105)

_16 of 16 isotopes with a framework prediction; 16 of 16 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{255}$Db | 255 | 150 | -180.9170 | -1096409.61 ± 135.8880 | 239687.9547 | 237630.5909 | +8657823.83 ± 1191.66 | ±0.39 |
| ${}^{256}$Db | 256 | 151 | -174.1776 | -1092455.65 ± 135.8880 | 240620.7807 | 238562.7882 | +8626628.01 ± 784.83 | ±0.39 |
| ${}^{257}$Db | 257 | 152 | -167.4461 | -1088500.87 ± 87.0147 | 241553.6147 | 239494.1389 | +8599274.03 ± 687.42 | ±0.39 |
| ${}^{258}$Db | 258 | 153 | -160.7226 | -1084646.71 ± 48.3730 | 242486.4566 | 240426.9865 | +8565885.74 ± 382.06 | ±0.39 |
| ${}^{259}$Db | 259 | 154 | -154.0069 | -1080786.94 ± 29.7404 | 243419.3063 | 241358.9639 | +8536423.74 ± 234.86 | ±0.39 |
| ${}^{260}$Db | 260 | 155 | -147.2989 | -1077006.17 ± 0.0000 | 244352.1637 | 242292.1395 | +8502233.23 ± 384.45 | ±0.39 |
| ${}^{261}$Db | 261 | 156 | -140.5987 | -1073221.73 ± 0.0000 | 245285.0289 | 243224.2688 | +8472674.51 ± 451.91 | ±0.39 |
| ${}^{262}$Db | 262 | 157 | -133.9060 | -1069517.38 ± 136.0174 | 246217.9017 | 244157.7079 | +8437963.33 ± 587.53 | ±0.39 |
| ${}^{263}$Db | 263 | 158 | -127.2210 | -1065795.69 ± 136.0174 | 247150.7820 | 245090.0590 | +8408023.80 ± 684.11 | ±0.39 |
| ${}^{264}$Db | 264 | 159 | -120.5434 | -1062156.78 ± 136.1285 | 248083.6699 | 246023.7048 | +8373034.74 ± 957.91 | ±0.39 |
| ${}^{265}$Db | 265 | 160 | -113.8732 | -1058503.77 ± 136.1470 | 249016.5651 | 246956.3195 | +8342550.60 ± 905.26 | ±0.40 |
| ${}^{266}$Db | 266 | 161 | -107.2104 | -1054918.47 ± 136.2583 | 249949.4677 | 247890.1722 | +8307290.06 ± 1142.34 | ±0.40 |
| ${}^{267}$Db | 267 | 162 | -100.5549 | -1051330.26 ± 136.2955 | 250882.3777 | 248822.9396 | +8276720.89 ± 1504.93 | ±0.40 |
| ${}^{268}$Db | 268 | 163 | -93.9066 | -1047816.30 ± 272.9258 | 251815.2948 | 249757.4797 | +8239253.08 ± 2118.41 | ±0.40 |
| ${}^{269}$Db | 269 | 164 | -87.2655 | -1044299.76 ± 273.1121 | 252748.2191 | 250691.0622 | +8205944.30 ± 2485.81 | ±0.40 |
| ${}^{270}$Db | 270 | 165 | -80.6315 | -1040830.64 ± 273.4482 | 253681.1506 | 251625.8054 | +8168260.68 ± 2284.07 | ±0.40 |

### Seaborgium (Z = 106)

_16 of 16 isotopes with a framework prediction; 16 of 16 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{258}$Sg | 258 | 152 | -186.7901 | -1098609.76 ± 272.4053 | 242511.7418 | 240430.7749 | +8655160.41 ± 1716.30 | ±0.39 |
| ${}^{259}$Sg | 259 | 153 | -180.0448 | -1094707.60 ± 136.2398 | 243444.5619 | 241363.4920 | +8622140.22 ± 748.70 | ±0.39 |
| ${}^{260}$Sg | 260 | 154 | -173.3074 | -1090781.24 ± 10.7592 | 244377.3899 | 242295.0145 | +8594380.02 ± 84.75 | ±0.39 |
| ${}^{261}$Sg | 261 | 155 | -166.5778 | -1086954.93 ± 9.6597 | 245310.2257 | 243227.9661 | +8560938.54 ± 76.03 | ±0.39 |
| ${}^{262}$Sg | 262 | 156 | -159.8560 | -1083111.72 ± 11.5240 | 246243.0694 | 244159.8242 | +8532301.02 ± 90.79 | ±0.39 |
| ${}^{263}$Sg | 263 | 157 | -153.1419 | -1079363.33 ± 0.0000 | 247175.9207 | 245093.1441 | +8497898.19 ± 383.86 | ±0.39 |
| ${}^{264}$Sg | 264 | 158 | -146.4355 | -1075590.06 ± 136.2769 | 248108.7796 | 246025.2260 | +8468861.91 ± 1151.00 | ±0.39 |
| ${}^{265}$Sg | 265 | 159 | -139.7366 | -1071908.88 ± 136.3698 | 249041.6462 | 246958.7312 | +8434263.41 ± 562.01 | ±0.39 |
| ${}^{266}$Sg | 266 | 160 | -133.0452 | -1068217.38 ± 136.3884 | 249974.5202 | 247891.0487 | +8404787.03 ± 988.27 | ±0.39 |
| ${}^{267}$Sg | 267 | 161 | -126.3612 | -1064591.65 ± 136.4815 | 250907.4017 | 248824.7318 | +8370027.39 ± 1051.94 | ±0.39 |
| ${}^{268}$Sg | 268 | 162 | -119.6846 | -1060958.84 ± 273.0003 | 251840.2905 | 249757.2189 | +8340385.88 ± 1879.72 | ±0.40 |
| ${}^{269}$Sg | 269 | 163 | -113.0154 | -1057410.69 ± 136.6494 | 252773.1866 | 250691.6062 | +8303351.03 ± 1467.70 | ±0.40 |
| ${}^{270}$Sg | 270 | 164 | -106.3533 | -1053855.79 ± 273.4482 | 253706.0900 | 251624.8394 | +8271244.63 ± 1821.34 | ±0.40 |
| ${}^{271}$Sg | 271 | 165 | -99.6985 | -1050361.55 ± 273.7851 | 254639.0006 | 252559.5193 | +8233628.96 ± 2338.33 | ±0.40 |
| ${}^{272}$Sg | 272 | 166 | -93.0508 | -1046856.39 ± 410.9026 | 255571.9183 | 253492.9164 | +8201420.25 ± 2730.25 | ±0.40 |
| ${}^{273}$Sg | 273 | 167 | -86.4101 | -1043406.56 ± 137.1366 | 256504.8431 | 254427.8105 | +8163544.12 ± 1570.63 | ±0.40 |

### Bohrium (Z = 107)

_19 of 19 isotopes with a framework prediction; 19 of 19 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{260}$Bh | 260 | 153 | -199.5392 | -1104930.05 ± 136.7241 | 244402.8393 | 242301.5904 | +8672039.26 ± 811.16 | ±0.39 |
| ${}^{261}$Bh | 261 | 154 | -192.7800 | -1100941.27 ± 94.1463 | 245335.6456 | 243233.0405 | +8644405.72 ± 739.22 | ±0.39 |
| ${}^{262}$Bh | 262 | 155 | -186.0288 | -1097055.68 ± 48.5529 | 246268.4597 | 244165.7073 | +8611989.26 ± 381.19 | ±0.39 |
| ${}^{263}$Bh | 263 | 156 | -179.2854 | -1093152.96 ± 136.6494 | 247201.2818 | 245097.4448 | +8583675.61 ± 1246.57 | ±0.39 |
| ${}^{264}$Bh | 264 | 157 | -172.5497 | -1089350.31 ± 136.7054 | 248134.1116 | 246030.4014 | +8550610.83 ± 719.36 | ±0.39 |
| ${}^{265}$Bh | 265 | 158 | -165.8218 | -1085530.72 ± 136.6867 | 249066.9491 | 246962.3323 | +8522015.22 ± 969.35 | ±0.39 |
| ${}^{266}$Bh | 266 | 159 | -159.1016 | -1081789.44 ± 136.7428 | 249999.7942 | 247895.5357 | +8488488.97 ± 657.58 | ±0.39 |
| ${}^{267}$Bh | 267 | 160 | -152.3889 | -1078045.25 ± 136.7428 | 250932.6470 | 248827.6903 | +8459495.52 ± 1055.68 | ±0.39 |
| ${}^{268}$Bh | 268 | 161 | -145.6837 | -1074373.51 ± 136.8176 | 251865.5072 | 249761.1265 | +8425573.45 ± 1529.11 | ±0.39 |
| ${}^{269}$Bh | 269 | 162 | -138.9860 | -1070690.47 ± 136.8176 | 252798.3750 | 250693.3910 | +8396647.26 ± 1493.70 | ±0.39 |
| ${}^{270}$Bh | 270 | 163 | -132.2957 | -1067111.90 ± 136.9675 | 253731.2500 | 251627.6376 | +8360021.26 ± 1184.60 | ±0.40 |
| ${}^{271}$Bh | 271 | 164 | -125.6127 | -1063512.66 ± 137.0238 | 254664.1325 | 252560.7609 | +8328180.21 ± 1519.54 | ±0.40 |
| ${}^{272}$Bh | 272 | 165 | -118.9369 | -1059981.91 ± 274.3484 | 255597.0221 | 253495.1837 | +8291433.62 ± 2098.20 | ±0.40 |
| ${}^{273}$Bh | 273 | 166 | -112.2684 | -1056442.43 ± 274.4990 | 256529.9190 | 254428.5733 | +8259078.96 ± 2573.77 | ±0.40 |
| ${}^{274}$Bh | 274 | 167 | -105.6070 | -1052957.81 ± 274.8008 | 257462.8230 | 255363.1460 | +8222318.05 ± 2261.59 | ±0.40 |
| ${}^{275}$Bh | 275 | 168 | -98.9527 | -1049474.48 ± 274.9897 | 258395.7341 | 256296.6587 | +8190022.71 ± 2340.58 | ±0.40 |
| ${}^{276}$Bh | 276 | 169 | -92.3054 | -1046034.38 ± 275.2925 | 259328.6523 | 257231.3227 | +8153476.72 ± 2332.07 | ±0.40 |
| ${}^{277}$Bh | 277 | 170 | -85.6650 | -1042597.80 ± 275.4821 | 260261.5774 | 258164.9667 | +8121205.30 ± 2323.64 | ±0.40 |
| ${}^{278}$Bh | 278 | 171 | -79.0316 | -1039206.50 ± 137.9120 | 261194.5094 | 259099.7312 | +8084833.20 ± 1542.31 | ±0.40 |

### Hassium (Z = 108)

_18 of 18 isotopes with a framework prediction; 18 of 18 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{263}$Hs | 263 | 155 | -205.6512 | -1107189.00 ± 137.0802 | 247226.8653 | 245102.6267 | +8666731.17 ± 805.69 | ±0.39 |
| ${}^{264}$Hs | 264 | 156 | -198.8862 | -1103222.51 ± 14.9896 | 248159.6657 | 246034.0065 | +8639696.37 ± 117.39 | ±0.39 |
| ${}^{265}$Hs | 265 | 157 | -192.1290 | -1099368.20 ± 12.3899 | 249092.4739 | 246966.8377 | +8606970.00 ± 97.01 | ±0.39 |
| ${}^{266}$Hs | 266 | 158 | -185.3796 | -1095490.65 ± 13.9622 | 250025.2899 | 247898.5713 | +8578987.14 ± 109.34 | ±0.39 |
| ${}^{267}$Hs | 267 | 159 | -178.6379 | -1091714.30 ± 0.0000 | 250958.1137 | 248831.5830 | +8546064.24 ± 381.83 | ±0.39 |
| ${}^{268}$Hs | 268 | 160 | -171.9039 | -1087903.58 ± 137.0426 | 251890.9451 | 249763.3873 | +8518293.37 ± 1200.90 | ±0.39 |
| ${}^{269}$Hs | 269 | 161 | -165.1775 | -1084184.62 ± 0.0000 | 252823.7841 | 250696.4072 | +8485869.16 ± 523.90 | ±0.39 |
| ${}^{270}$Hs | 270 | 162 | -158.4586 | -1080450.11 ± 137.0802 | 253756.6306 | 251628.5198 | +8457351.41 ± 984.70 | ±0.39 |
| ${}^{271}$Hs | 271 | 163 | -151.7471 | -1076832.12 ± 137.2119 | 254689.4846 | 252562.5932 | +8421244.67 ± 1091.70 | ±0.39 |
| ${}^{272}$Hs | 272 | 164 | -145.0431 | -1073187.84 ± 274.4990 | 255622.3460 | 253495.4007 | +8390468.86 ± 2010.01 | ±0.39 |
| ${}^{273}$Hs | 273 | 165 | -138.3464 | -1069619.91 ± 137.3815 | 256555.2147 | 254429.6576 | +8354203.25 ± 1468.10 | ±0.40 |
| ${}^{274}$Hs | 274 | 166 | -131.6570 | -1066039.01 ± 274.8763 | 257488.0907 | 255362.7902 | +8322670.92 ± 1838.46 | ±0.40 |
| ${}^{275}$Hs | 275 | 167 | -124.9747 | -1062528.01 ± 275.1789 | 258420.9739 | 256297.3704 | +8285701.61 ± 2315.13 | ±0.40 |
| ${}^{276}$Hs | 276 | 168 | -118.2997 | -1058998.22 ± 412.9387 | 259353.8643 | 257230.5579 | +8254487.17 ± 2799.22 | ±0.40 |
| ${}^{277}$Hs | 277 | 169 | -111.6317 | -1055540.60 ± 275.6340 | 260286.7617 | 258165.2415 | +8217683.57 ± 1731.90 | ±0.40 |
| ${}^{278}$Hs | 278 | 170 | -104.9708 | -1052067.40 ± 137.8930 | 261219.6662 | 259098.5808 | +8186402.87 ± 1157.63 | ±0.40 |
| ${}^{279}$Hs | 279 | 171 | -98.3169 | -1048652.51 ± 276.1287 | 262152.5777 | 260033.3547 | +8149811.97 ± 2306.94 | ±0.40 |
| ${}^{280}$Hs | 280 | 172 | -91.6698 | -1045226.17 ± 276.2813 | 263085.4961 | 260966.7687 | +8118763.32 ± 2298.69 | ±0.40 |

### Meitnerium (Z = 109)

_18 of 18 isotopes with a framework prediction; 18 of 18 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{265}$Mt | 265 | 156 | -218.6580 | -1113465.97 ± 275.0275 | 249118.2206 | 246972.5620 | +8687841.97 ± 1776.45 | ±0.39 |
| ${}^{266}$Mt | 266 | 157 | -211.8792 | -1109553.66 ± 49.8847 | 250051.0072 | 247905.1043 | +8656146.63 ± 389.15 | ±0.39 |
| ${}^{267}$Mt | 267 | 158 | -205.1083 | -1105622.95 ± 274.9897 | 250983.8017 | 248836.7164 | +8628490.52 ± 2021.43 | ±0.39 |
| ${}^{268}$Mt | 268 | 159 | -198.3451 | -1101787.06 ± 137.5327 | 251916.6040 | 249769.5705 | +8596056.92 ± 932.35 | ±0.39 |
| ${}^{269}$Mt | 269 | 160 | -191.5897 | -1097914.41 ± 137.4759 | 252849.4140 | 250701.2137 | +8568767.13 ± 1244.71 | ±0.39 |
| ${}^{270}$Mt | 270 | 161 | -184.8420 | -1094154.85 ± 137.5327 | 253782.2317 | 251634.1171 | +8536658.59 ± 758.86 | ±0.39 |
| ${}^{271}$Mt | 271 | 162 | -178.1018 | -1090361.93 ± 137.4948 | 254715.0570 | 252566.0015 | +8508886.48 ± 1305.60 | ±0.39 |
| ${}^{272}$Mt | 272 | 163 | -171.3692 | -1086697.94 ± 275.2167 | 255647.8898 | 253499.8775 | +8473425.50 ± 1914.43 | ±0.39 |
| ${}^{273}$Mt | 273 | 164 | -164.6441 | -1083013.35 ± 275.2925 | 256580.7301 | 254432.6729 | +8442536.88 ± 1665.78 | ±0.39 |
| ${}^{274}$Mt | 274 | 165 | -157.9264 | -1079401.26 ± 137.7600 | 257513.5778 | 255366.6336 | +8407301.31 ± 1473.66 | ±0.39 |
| ${}^{275}$Mt | 275 | 166 | -151.2160 | -1075771.87 ± 137.7980 | 258446.4328 | 256299.6451 | +8376085.68 ± 1511.91 | ±0.40 |
| ${}^{276}$Mt | 276 | 167 | -144.5130 | -1072220.37 ± 275.8621 | 259379.2952 | 257233.6849 | +8341093.65 ± 2067.70 | ±0.40 |
| ${}^{277}$Mt | 277 | 168 | -137.8171 | -1068653.89 ± 275.9763 | 260312.1648 | 258166.8744 | +8309704.39 ± 2565.37 | ±0.40 |
| ${}^{278}$Mt | 278 | 169 | -131.1284 | -1065149.87 ± 276.2431 | 261245.0415 | 259101.1276 | +8274429.31 ± 2232.56 | ±0.40 |
| ${}^{279}$Mt | 279 | 170 | -124.4469 | -1061634.12 ± 276.3576 | 262177.9254 | 260034.4399 | +8243082.87 ± 2579.18 | ±0.40 |
| ${}^{280}$Mt | 280 | 171 | -117.7723 | -1058184.47 ± 276.6634 | 263110.8163 | 260968.8589 | +8207712.42 ± 2298.67 | ±0.40 |
| ${}^{281}$Mt | 281 | 172 | -111.1048 | -1054725.37 ± 276.8166 | 264043.7142 | 261902.2430 | +8176604.79 ± 2290.48 | ±0.40 |
| ${}^{282}$Mt | 282 | 173 | -104.4442 | -1051311.94 ± 277.0851 | 264976.6190 | 262836.7924 | +8141274.83 ± 1701.12 | ±0.40 |

### Sodium (Z = 11)

_0 of 23 isotopes with a framework prediction; 0 of 23 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{17}$Na | 17 | 6 | — | — | — | 15870.1193 | — | ±0.23 |
| ${}^{18}$Na | 18 | 7 | — | — | — | 16791.9319 | — | ±0.25 |
| ${}^{19}$Na | 19 | 8 | — | — | — | 17711.3174 | — | ±0.28 |
| ${}^{20}$Na | 20 | 9 | — | — | — | 18636.7326 | — | ±0.29 |
| ${}^{21}$Na | 21 | 10 | — | — | — | 19559.1913 | — | ±0.31 |
| ${}^{22}$Na | 22 | 11 | — | — | — | 20487.6889 | — | ±0.33 |
| ${}^{23}$Na | 23 | 12 | — | — | — | 21414.8345 | — | ±0.34 |
| ${}^{24}$Na | 24 | 13 | — | — | — | 22347.4406 | — | ±0.35 |
| ${}^{25}$Na | 25 | 14 | — | — | — | 23277.9948 | — | ±0.37 |
| ${}^{26}$Na | 26 | 15 | — | — | — | 24211.9859 | — | ±0.38 |
| ${}^{27}$Na | 27 | 16 | — | — | — | 25144.8230 | — | ±0.39 |
| ${}^{28}$Na | 28 | 17 | — | — | — | 26080.8466 | — | ±0.40 |
| ${}^{29}$Na | 29 | 18 | — | — | — | 27016.0090 | — | ±0.41 |
| ${}^{30}$Na | 30 | 19 | — | — | — | 27953.2978 | — | ±0.41 |
| ${}^{31}$Na | 31 | 20 | — | — | — | 28888.5632 | — | ±0.42 |
| ${}^{32}$Na | 32 | 21 | — | — | — | 29826.4515 | — | ±0.43 |
| ${}^{33}$Na | 33 | 22 | — | — | — | 30763.0855 | — | ±0.44 |
| ${}^{34}$Na | 34 | 23 | — | — | — | 31702.4796 | — | ±0.44 |
| ${}^{35}$Na | 35 | 24 | — | — | — | 32640.1253 | — | ±0.45 |
| ${}^{36}$Na | 36 | 25 | — | — | — | 33579.6908 | — | ±0.45 |
| ${}^{37}$Na | 37 | 26 | — | — | — | 34518.4161 | — | ±0.46 |
| ${}^{38}$Na | 38 | 27 | — | — | — | 35458.6812 | — | ±0.46 |
| ${}^{39}$Na | 39 | 28 | — | — | — | 36398.2467 | — | ±0.47 |

### Darmstadtium (Z = 110)

_18 of 18 isotopes with a framework prediction; 18 of 18 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{267}$Ds | 267 | 157 | -231.8000 | -1119779.89 ± 137.9691 | 251009.7110 | 248842.8056 | +8707928.80 ± 819.78 | ±0.38 |
| ${}^{268}$Ds | 268 | 158 | -225.0074 | -1115772.19 ± 137.8930 | 251942.4839 | 249774.0678 | +8681510.38 ± 1208.31 | ±0.39 |
| ${}^{269}$Ds | 269 | 159 | -218.2228 | -1111892.37 ± 16.0962 | 252875.2647 | 250706.7486 | +8649612.14 ± 125.26 | ±0.39 |
| ${}^{270}$Ds | 270 | 160 | -211.4459 | -1107962.31 ± 20.0586 | 253808.0533 | 251638.0896 | +8623351.49 ± 156.08 | ±0.39 |
| ${}^{271}$Ds | 271 | 161 | -204.6768 | -1104145.75 ± 0.0000 | 254740.8496 | 252570.8546 | +8591628.69 ± 383.56 | ±0.39 |
| ${}^{272}$Ds | 272 | 162 | -197.9154 | -1100293.61 ± 275.6720 | 255673.6536 | 253502.4791 | +8564707.12 ± 1675.57 | ±0.39 |
| ${}^{273}$Ds | 273 | 163 | -191.1616 | -1096582.84 ± 137.9310 | 256606.4652 | 254436.1753 | +8529801.01 ± 556.47 | ±0.39 |
| ${}^{274}$Ds | 274 | 164 | -184.4153 | -1092847.10 ± 137.9501 | 257539.2844 | 255368.5813 | +8500274.62 ± 1524.72 | ±0.39 |
| ${}^{275}$Ds | 275 | 165 | -177.6765 | -1089202.89 ± 138.0643 | 258472.1110 | 256302.5448 | +8464864.15 ± 1330.17 | ±0.39 |
| ${}^{276}$Ds | 276 | 166 | -170.9452 | -1085512.45 ± 276.1287 | 259404.9451 | 257234.9117 | +8435998.70 ± 2129.25 | ±0.39 |
| ${}^{277}$Ds | 277 | 167 | -164.2212 | -1081920.18 ± 138.1788 | 260337.7865 | 258168.9590 | +8400806.56 ± 1519.00 | ±0.39 |
| ${}^{278}$Ds | 278 | 168 | -157.5045 | -1078297.82 ± 276.3958 | 261270.6353 | 259101.6119 | +8371323.20 ± 1970.11 | ±0.40 |
| ${}^{279}$Ds | 279 | 169 | -150.7951 | -1074766.10 ± 276.6634 | 262203.4912 | 260035.8791 | +8335819.49 ± 2324.83 | ±0.40 |
| ${}^{280}$Ds | 280 | 170 | -144.0928 | -1071207.58 ± 415.1100 | 263136.3544 | 260968.6689 | +8306305.51 ± 2866.21 | ±0.40 |
| ${}^{281}$Ds | 281 | 171 | -137.3977 | -1067722.94 ± 277.0083 | 264069.2247 | 261903.1158 | +8270649.33 ± 1881.46 | ±0.40 |
| ${}^{282}$Ds | 282 | 172 | -130.7096 | -1064224.63 ± 138.5617 | 265002.1020 | 262836.1274 | +8240779.85 ± 1141.17 | ±0.40 |
| ${}^{283}$Ds | 283 | 173 | -124.0285 | -1060785.47 ± 277.3925 | 265934.9864 | 263770.6609 | +8205330.48 ± 1896.39 | ±0.40 |
| ${}^{284}$Ds | 284 | 174 | -117.3544 | -1057335.87 ± 277.5080 | 266867.8777 | 264703.7851 | +8175525.41 ± 1889.71 | ±0.40 |

### Roentgenium (Z = 111)

_15 of 15 isotopes with a framework prediction; 15 of 15 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{272}$Rg | 272 | 161 | -224.6816 | -1114298.48 ± 138.3700 | 255699.6374 | 253509.1691 | +8640588.17 ± 922.27 | ±0.39 |
| ${}^{273}$Rg | 273 | 162 | -217.8988 | -1110396.14 ± 138.3126 | 256632.4201 | 254440.7750 | +8613576.61 ± 1570.55 | ±0.39 |
| ${}^{274}$Rg | 274 | 163 | -211.1237 | -1106617.48 ± 138.3700 | 257565.2104 | 255373.9961 | +8580413.03 ± 820.70 | ±0.39 |
| ${}^{275}$Rg | 275 | 164 | -204.3563 | -1102824.65 ± 276.7400 | 258498.0084 | 256306.2736 | +8551233.72 ± 1740.83 | ±0.39 |
| ${}^{276}$Rg | 276 | 165 | -197.5964 | -1099117.95 ± 276.8933 | 259430.8140 | 257239.7592 | +8517558.68 ± 2444.25 | ±0.39 |
| ${}^{277}$Rg | 277 | 166 | -190.8440 | -1095398.44 ± 276.9316 | 260363.6270 | 258172.2742 | +8487947.67 ± 1818.45 | ±0.39 |
| ${}^{278}$Rg | 278 | 167 | -184.0990 | -1091746.57 ± 138.5425 | 261296.4475 | 259105.8810 | +8454329.48 ± 1499.13 | ±0.39 |
| ${}^{279}$Rg | 279 | 168 | -177.3615 | -1088096.47 ± 277.1619 | 262229.2753 | 260038.5767 | +8424513.87 ± 1622.71 | ±0.39 |
| ${}^{280}$Rg | 280 | 169 | -170.6312 | -1084497.66 ± 277.3156 | 263162.1104 | 260972.2356 | +8391217.74 ± 2038.08 | ±0.40 |
| ${}^{281}$Rg | 281 | 170 | -163.9082 | -1080913.18 ± 416.1465 | 264094.9529 | 261905.1763 | +8360951.77 ± 2955.54 | ±0.40 |
| ${}^{282}$Rg | 282 | 171 | -157.1924 | -1077376.41 ± 277.6235 | 265027.8025 | 262839.0793 | +8327236.59 ± 2236.25 | ±0.40 |
| ${}^{283}$Rg | 283 | 172 | -150.4837 | -1073843.13 ± 277.7392 | 265960.6592 | 263772.2109 | +8296735.49 ± 2570.88 | ±0.40 |
| ${}^{284}$Rg | 284 | 173 | -143.7821 | -1070364.81 ± 277.9708 | 266893.5230 | 264706.2955 | +8262846.51 ± 1889.69 | ±0.40 |
| ${}^{285}$Rg | 285 | 174 | -137.0875 | -1066881.07 ± 278.0868 | 267826.3938 | 265639.5492 | +8232375.91 ± 2258.26 | ±0.40 |
| ${}^{286}$Rg | 286 | 175 | -130.3998 | -1063457.69 ± 278.3577 | 268759.2716 | 266573.8238 | +8198283.61 ± 1719.21 | ±0.40 |

### Copernicium (Z = 112)

_13 of 13 isotopes with a framework prediction; 13 of 13 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{276}$Cn | 276 | 164 | -224.4665 | -1112815.17 ± 277.4310 | 259456.9018 | 257242.7325 | +8607315.01 ± 1944.51 | ±0.39 |
| ${}^{277}$Cn | 277 | 165 | -217.6855 | -1109072.62 ± 138.7925 | 260389.6861 | 258176.1986 | +8573553.80 ± 595.32 | ±0.39 |
| ${}^{278}$Cn | 278 | 166 | -210.9120 | -1105283.97 ± 277.5465 | 261322.4781 | 259108.2032 | +8545753.78 ± 1689.65 | ±0.39 |
| ${}^{279}$Cn | 279 | 167 | -204.1460 | -1101597.64 ± 138.8503 | 262255.2775 | 260041.8760 | +8511711.74 ± 1518.81 | ±0.39 |
| ${}^{280}$Cn | 280 | 168 | -197.3875 | -1097883.28 ± 277.7006 | 263188.0844 | 260974.0036 | +8483913.47 ± 2234.38 | ±0.39 |
| ${}^{281}$Cn | 281 | 169 | -190.6364 | -1094264.45 ± 138.9468 | 264120.8987 | 261907.7901 | +8449953.45 ± 1518.66 | ±0.39 |
| ${}^{282}$Cn | 282 | 170 | -183.8926 | -1090607.37 ± 277.8936 | 265053.7203 | 262840.1635 | +8421684.03 ± 2083.85 | ±0.39 |
| ${}^{283}$Cn | 283 | 171 | -177.1560 | -1087040.17 ± 278.0868 | 265986.5492 | 263774.1680 | +8387406.60 ± 2330.73 | ±0.40 |
| ${}^{284}$Cn | 284 | 172 | -170.4267 | -1083450.68 ± 417.1882 | 266919.3853 | 264706.7408 | +8358852.12 ± 2882.03 | ±0.40 |
| ${}^{285}$Cn | 285 | 173 | -163.7045 | -1079944.55 ± 278.3577 | 267852.2285 | 265640.9055 | +8324482.36 ± 1907.59 | ±0.40 |
| ${}^{286}$Cn | 286 | 174 | -156.9894 | -1076418.46 ± 278.4352 | 268785.0788 | 266573.7633 | +8295323.25 ± 2624.23 | ±0.40 |
| ${}^{287}$Cn | 287 | 175 | -150.2813 | -1072969.36 ± 278.7068 | 269717.9362 | 267508.1776 | +8260527.10 ± 2615.07 | ±0.40 |
| ${}^{288}$Cn | 288 | 176 | -143.5802 | -1069492.94 ± 278.7845 | 270650.8005 | 268441.2320 | +8231107.07 ± 2605.98 | ±0.40 |

### Nihonium (Z = 113)

_13 of 13 isotopes with a framework prediction; 13 of 13 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{278}$Nh | 278 | 165 | -237.9434 | -1119191.14 ± 139.2564 | 261348.7272 | 259114.3902 | +8622975.36 ± 862.78 | ±0.39 |
| ${}^{279}$Nh | 279 | 166 | -231.1488 | -1115340.43 ± 278.4352 | 262281.4980 | 260046.3146 | +8595327.92 ± 2306.83 | ±0.39 |
| ${}^{280}$Nh | 280 | 167 | -224.3618 | -1111600.56 ± 139.2758 | 263214.2764 | 260979.5888 | +8562690.88 ± 1531.20 | ±0.39 |
| ${}^{281}$Nh | 281 | 168 | -217.5822 | -1107828.16 ± 139.2564 | 264147.0623 | 261911.6530 | +8534974.46 ± 1145.20 | ±0.39 |
| ${}^{282}$Nh | 282 | 169 | -210.8102 | -1104159.65 ± 139.3340 | 265079.8556 | 262845.0660 | +8502307.77 ± 1523.87 | ±0.39 |
| ${}^{283}$Nh | 283 | 170 | -204.0455 | -1100461.04 ± 278.6680 | 266012.6564 | 263777.3947 | +8474045.64 ± 1656.21 | ±0.39 |
| ${}^{284}$Nh | 284 | 171 | -197.2882 | -1096846.05 ± 278.8234 | 266945.4645 | 264710.9167 | +8441464.50 ± 2016.34 | ±0.39 |
| ${}^{285}$Nh | 285 | 172 | -190.5381 | -1093217.35 ± 418.2934 | 267878.2798 | 265643.5872 | +8412371.70 ± 2917.45 | ±0.39 |
| ${}^{286}$Nh | 286 | 173 | -183.7953 | -1089654.14 ± 279.0179 | 268811.1024 | 266577.2704 | +8379679.43 ± 2215.37 | ±0.40 |
| ${}^{287}$Nh | 287 | 174 | -177.0596 | -1086091.61 ± 279.0957 | 269743.9322 | 267510.2623 | +8349847.41 ± 2642.90 | ±0.40 |
| ${}^{288}$Nh | 288 | 175 | -170.3311 | -1082601.57 ± 279.3296 | 270676.7690 | 268444.2714 | +8316428.49 ± 2605.95 | ±0.40 |
| ${}^{289}$Nh | 289 | 176 | -163.6095 | -1079089.54 ± 279.4077 | 271609.6129 | 269377.3463 | +8286764.52 ± 1856.92 | ±0.40 |
| ${}^{290}$Nh | 290 | 177 | -156.8950 | -1075645.59 ± 279.6421 | 272542.4638 | 270311.6051 | +8252915.18 ± 1733.34 | ±0.40 |

### Flerovium (Z = 114)

_8 of 8 isotopes with a framework prediction; 8 of 8 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{284}$Fl | 284 | 170 | -224.3666 | -1110292.25 ± 279.2126 | 266971.7606 | 264713.1047 | +8532467.05 ± 2477.29 | ±0.39 |
| ${}^{285}$Fl | 285 | 171 | -217.5885 | -1106644.55 ± 139.6843 | 267904.5478 | 265646.7515 | +8499243.11 ± 1518.32 | ±0.39 |
| ${}^{286}$Fl | 286 | 172 | -210.8177 | -1102964.76 ± 279.3686 | 268837.3425 | 266578.9191 | +8471875.30 ± 2061.61 | ±0.39 |
| ${}^{287}$Fl | 287 | 173 | -204.0541 | -1099369.68 ± 279.5248 | 269770.1444 | 267512.7363 | +8438506.67 ± 2308.60 | ±0.39 |
| ${}^{288}$Fl | 288 | 174 | -197.2979 | -1095759.29 ± 419.3458 | 270702.9535 | 268445.2188 | +8410411.38 ± 2841.90 | ±0.40 |
| ${}^{289}$Fl | 289 | 175 | -190.5487 | -1092228.03 ± 279.7594 | 271635.7698 | 269379.2614 | +8376696.65 ± 1894.94 | ±0.40 |
| ${}^{290}$Fl | 290 | 176 | -183.8067 | -1088682.85 ± 279.8377 | 272568.5932 | 270312.0205 | +8348029.44 ± 2591.39 | ±0.40 |
| ${}^{291}$Fl | 291 | 177 | -177.0718 | -1085211.33 ± 280.0728 | 273501.4237 | 271246.2839 | +8313993.16 ± 2579.03 | ±0.40 |

### Moscovium (Z = 115)

_6 of 6 isotopes with a framework prediction; 6 of 6 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{287}$Mc | 287 | 172 | -231.2648 | -1112873.07 ± 280.1513 | 269796.5727 | 267516.5555 | +8522901.51 ± 1653.95 | ±0.39 |
| ${}^{288}$Mc | 288 | 173 | -224.4806 | -1109242.68 ± 280.3083 | 270729.3539 | 268449.9675 | +8490916.91 ± 1995.19 | ±0.39 |
| ${}^{289}$Mc | 289 | 174 | -217.7036 | -1105578.10 ± 420.4625 | 271662.1424 | 269382.4788 | +8462553.13 ± 2883.88 | ±0.39 |
| ${}^{290}$Mc | 290 | 175 | -210.9339 | -1101999.49 ± 280.4656 | 272594.9381 | 270316.0818 | +8430339.12 ± 2188.17 | ±0.39 |
| ${}^{291}$Mc | 291 | 176 | -204.1714 | -1098417.71 ± 420.8164 | 273527.7410 | 271248.9639 | +8401053.66 ± 2709.50 | ±0.40 |
| ${}^{292}$Mc | 292 | 177 | -197.4160 | -1094902.04 ± 280.7412 | 274460.5510 | 272182.8780 | +8368171.47 ± 2570.15 | ±0.40 |

### Livermorium (Z = 116)

_5 of 5 isotopes with a framework prediction; 5 of 5 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{289}$Lv | 289 | 173 | -245.0742 | -1119118.93 ± 280.9383 | 271688.7306 | 269386.2532 | +8547122.76 ± 1867.23 | ±0.39 |
| ${}^{290}$Lv | 290 | 174 | -238.2765 | -1115399.34 ± 280.8989 | 272621.4984 | 270318.3174 | +8520254.83 ± 2043.43 | ±0.39 |
| ${}^{291}$Lv | 291 | 175 | -231.4862 | -1111788.25 ± 281.0568 | 273554.2734 | 271252.0275 | +8487478.98 ± 2297.38 | ±0.39 |
| ${}^{292}$Lv | 292 | 176 | -224.7031 | -1108140.96 ± 421.5852 | 274487.0557 | 272184.4112 | +8459869.20 ± 2802.86 | ±0.39 |
| ${}^{293}$Lv | 293 | 177 | -217.9272 | -1104595.52 ± 281.2544 | 275419.8452 | 273118.3402 | +8426768.40 ± 1886.06 | ±0.40 |

### Tennessine (Z = 117)

_4 of 4 isotopes with a framework prediction; 4 of 4 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{291}$Ts | 291 | 174 | -259.0162 | -1125400.11 ± 281.7695 | 273581.0211 | 271256.4372 | +8569691.05 ± 2197.76 | ±0.39 |
| ${}^{292}$Ts | 292 | 175 | -252.2051 | -1121735.90 ± 281.8887 | 274513.7755 | 272189.8996 | +8537700.64 ± 2457.15 | ±0.39 |
| ${}^{293}$Ts | 293 | 176 | -245.4014 | -1118047.56 ± 422.8330 | 275446.5372 | 273122.2004 | +8510244.82 ± 2847.80 | ±0.39 |
| ${}^{294}$Ts | 294 | 177 | -238.6049 | -1114436.18 ± 282.0079 | 276379.3061 | 274055.6627 | +8478727.91 ± 2165.11 | ±0.39 |

### Oganesson (Z = 118)

_3 of 3 isotopes with a framework prediction; 3 of 3 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{293}$Og | 293 | 175 | -273.0904 | -1131682.54 ± 282.5657 | 275473.4438 | 273126.5747 | +8592606.29 ± 2595.38 | ±0.39 |
| ${}^{294}$Og | 294 | 176 | -266.2660 | -1127937.07 ± 282.5258 | 276406.1848 | 274058.5867 | +8566044.79 ± 2018.94 | ±0.39 |
| ${}^{295}$Og | 295 | 177 | -259.4489 | -1124291.66 ± 282.6456 | 277338.9331 | 274992.1291 | +8534077.06 ± 2381.31 | ±0.39 |

### Magnesium (Z = 12)

_2 of 23 isotopes with a framework prediction; 2 of 23 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{19}$Mg | 19 | 7 | — | — | — | 17730.2264 | — | ±0.24 |
| ${}^{20}$Mg | 20 | 8 | — | — | — | 18647.3598 | — | ±0.26 |
| ${}^{21}$Mg | 21 | 9 | — | — | — | 19572.2800 | — | ±0.28 |
| ${}^{22}$Mg | 22 | 10 | — | — | — | 20492.4703 | — | ±0.30 |
| ${}^{23}$Mg | 23 | 11 | — | — | — | 21418.8907 | — | ±0.31 |
| ${}^{24}$Mg | 24 | 12 | 216.1389 | +90195.33 ± 0.0726 | 22324.0432 | 22341.9249 | -800364.49 ± 0.54 | ±0.33 |
| ${}^{25}$Mg | 25 | 13 | — | — | — | 23274.1598 | — | ±0.34 |
| ${}^{26}$Mg | 26 | 14 | — | — | — | 24202.6322 | — | ±0.35 |
| ${}^{27}$Mg | 27 | 15 | — | — | — | 25135.7542 | — | ±0.36 |
| ${}^{28}$Mg | 28 | 16 | — | — | — | 26066.8150 | — | ±0.37 |
| ${}^{29}$Mg | 29 | 17 | — | — | — | 27002.7166 | — | ±0.38 |
| ${}^{30}$Mg | 30 | 18 | — | — | — | 27935.9417 | — | ±0.39 |
| ${}^{31}$Mg | 31 | 19 | — | — | — | 28873.1951 | — | ±0.40 |
| ${}^{32}$Mg | 32 | 20 | — | — | — | 29806.9824 | — | ±0.41 |
| ${}^{33}$Mg | 33 | 21 | — | — | — | 30744.2683 | — | ±0.42 |
| ${}^{34}$Mg | 34 | 22 | — | — | — | 31679.1229 | — | ±0.42 |
| ${}^{35}$Mg | 35 | 23 | — | — | — | 32617.9334 | — | ±0.43 |
| ${}^{36}$Mg | 36 | 24 | — | — | — | 33554.1679 | — | ±0.44 |
| ${}^{37}$Mg | 37 | 25 | — | — | — | 34493.4933 | — | ±0.44 |
| ${}^{38}$Mg | 38 | 26 | — | — | — | 35430.8500 | — | ±0.45 |
| ${}^{39}$Mg | 39 | 27 | — | — | — | 36371.0452 | — | ±0.45 |
| ${}^{40}$Mg | 40 | 28 | — | — | — | 37309.3140 | — | ±0.46 |
| ${}^{41}$Mg | 41 | 29 | 150.3903 | -429096.35 ± 1867.7043 | 38362.4040 | 38249.3583 | +2955492.50 ± 13077.67 | ±0.46 |

### Aluminium (Z = 13)

_3 of 23 isotopes with a framework prediction; 3 of 23 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{21}$Al | 21 | 8 | — | — | — | 19588.4659 | — | ±0.25 |
| ${}^{22}$Al | 22 | 9 | — | — | — | 20511.0717 | — | ±0.27 |
| ${}^{23}$Al | 23 | 10 | — | — | — | 21431.1125 | — | ±0.28 |
| ${}^{24}$Al | 24 | 11 | — | — | — | 22355.8097 | — | ±0.30 |
| ${}^{25}$Al | 25 | 12 | — | — | — | 23278.4366 | — | ±0.31 |
| ${}^{26}$Al | 26 | 13 | — | — | — | 24206.6366 | — | ±0.33 |
| ${}^{27}$Al | 27 | 14 | — | — | — | 25133.1439 | — | ±0.34 |
| ${}^{28}$Al | 28 | 15 | — | — | — | 26064.9842 | — | ±0.35 |
| ${}^{29}$Al | 29 | 16 | — | — | — | 26995.1212 | — | ±0.36 |
| ${}^{30}$Al | 30 | 17 | — | — | — | 27928.9590 | — | ±0.37 |
| ${}^{31}$Al | 31 | 18 | — | — | — | 28861.3665 | — | ±0.38 |
| ${}^{32}$Al | 32 | 19 | — | — | — | 29796.7120 | — | ±0.39 |
| ${}^{33}$Al | 33 | 20 | — | — | — | 30730.8080 | — | ±0.40 |
| ${}^{34}$Al | 34 | 21 | — | — | — | 31667.8019 | — | ±0.40 |
| ${}^{35}$Al | 35 | 22 | — | — | — | 32602.0699 | — | ±0.41 |
| ${}^{36}$Al | 36 | 23 | — | — | — | 33539.7381 | — | ±0.42 |
| ${}^{37}$Al | 37 | 24 | — | — | — | 34475.0914 | — | ±0.42 |
| ${}^{38}$Al | 38 | 25 | — | — | — | 35413.2457 | — | ±0.43 |
| ${}^{39}$Al | 39 | 26 | — | — | — | 36349.7596 | — | ±0.44 |
| ${}^{40}$Al | 40 | 27 | — | — | — | 37288.5846 | — | ±0.44 |
| ${}^{41}$Al | 41 | 28 | 143.0450 | -500157.14 ± 1432.6648 | 38368.9670 | 38225.8484 | +3744026.86 ± 10453.95 | ±0.45 |
| ${}^{42}$Al | 42 | 29 | 148.4366 | -482471.17 ± 1757.2119 | 39303.1408 | 39164.7422 | +3533754.34 ± 12772.01 | ±0.45 |
| ${}^{43}$Al | 43 | 30 | 153.8222 | -467035.16 ± 2085.8164 | 40237.3207 | 40102.5165 | +3361488.96 ± 14958.72 | ±0.46 |

### Silicon (Z = 14)

_5 of 24 isotopes with a framework prediction; 5 of 24 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{22}$Si | 22 | 8 | — | — | — | 20526.5103 | — | ±0.24 |
| ${}^{23}$Si | 23 | 9 | — | — | — | 21448.3140 | — | ±0.26 |
| ${}^{24}$Si | 24 | 10 | — | — | — | 22366.6037 | — | ±0.27 |
| ${}^{25}$Si | 25 | 11 | — | — | — | 23291.1799 | — | ±0.29 |
| ${}^{26}$Si | 26 | 12 | — | — | — | 24211.7057 | — | ±0.30 |
| ${}^{27}$Si | 27 | 13 | — | — | — | 25137.9563 | — | ±0.32 |
| ${}^{28}$Si | 28 | 14 | — | — | — | 26060.3421 | — | ±0.33 |
| ${}^{29}$Si | 29 | 15 | — | — | — | 26991.4339 | — | ±0.34 |
| ${}^{30}$Si | 30 | 16 | — | — | — | 27920.3901 | — | ±0.35 |
| ${}^{31}$Si | 31 | 17 | — | — | — | 28853.3682 | — | ±0.36 |
| ${}^{32}$Si | 32 | 18 | — | — | — | 29783.7336 | — | ±0.37 |
| ${}^{33}$Si | 33 | 19 | — | — | — | 30718.7911 | — | ±0.38 |
| ${}^{34}$Si | 34 | 20 | — | — | — | 31650.8078 | — | ±0.39 |
| ${}^{35}$Si | 35 | 21 | — | — | — | 32587.9021 | — | ±0.39 |
| ${}^{36}$Si | 36 | 22 | — | — | — | 33521.3516 | — | ±0.40 |
| ${}^{37}$Si | 37 | 23 | — | — | — | 34458.7103 | — | ±0.41 |
| ${}^{38}$Si | 38 | 24 | — | — | — | 35392.6056 | — | ±0.41 |
| ${}^{39}$Si | 39 | 25 | — | — | — | 36330.5904 | — | ±0.42 |
| ${}^{40}$Si | 40 | 26 | — | — | — | 37265.4310 | — | ±0.43 |
| ${}^{41}$Si | 41 | 27 | 135.2970 | -558951.21 ± 935.5787 | 38375.9326 | 38204.4585 | +4488329.24 ± 7850.94 | ±0.43 |
| ${}^{42}$Si | 42 | 28 | 140.7259 | -547824.99 ± 944.6694 | 39310.0692 | 39139.5919 | +4355621.85 ± 7663.37 | ±0.44 |
| ${}^{43}$Si | 43 | 29 | 146.1478 | -531266.67 ± 1241.2081 | 40244.2127 | 40078.5762 | +4132795.80 ± 9970.69 | ±0.44 |
| ${}^{44}$Si | 44 | 30 | 151.5629 | -518639.97 ± 1537.1716 | 41178.3630 | 41015.0510 | +3981758.26 ± 12195.82 | ±0.45 |
| ${}^{45}$Si | 45 | 31 | 156.9717 | -501961.60 ± 1856.0822 | 42112.5196 | 41954.3249 | +3770641.09 ± 14298.46 | ±0.45 |

### Phosphorus (Z = 15)

_7 of 24 isotopes with a framework prediction; 7 of 24 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{24}$P | 24 | 9 | — | — | — | 22389.8785 | — | ±0.25 |
| ${}^{25}$P | 25 | 10 | — | — | — | 23307.5427 | — | ±0.26 |
| ${}^{26}$P | 26 | 11 | — | — | — | 24229.8197 | — | ±0.28 |
| ${}^{27}$P | 27 | 12 | — | — | — | 25149.6818 | — | ±0.29 |
| ${}^{28}$P | 28 | 13 | — | — | — | 26074.6870 | — | ±0.30 |
| ${}^{29}$P | 29 | 14 | — | — | — | 26996.3762 | — | ±0.32 |
| ${}^{30}$P | 30 | 15 | — | — | — | 27924.6223 | — | ±0.33 |
| ${}^{31}$P | 31 | 16 | — | — | — | 28851.8767 | — | ±0.34 |
| ${}^{32}$P | 32 | 17 | — | — | — | 29783.5064 | — | ±0.35 |
| ${}^{33}$P | 33 | 18 | — | — | — | 30712.9681 | — | ±0.36 |
| ${}^{34}$P | 34 | 19 | — | — | — | 31646.2508 | — | ±0.37 |
| ${}^{35}$P | 35 | 20 | — | — | — | 32577.4358 | — | ±0.37 |
| ${}^{36}$P | 36 | 21 | — | — | — | 33513.5367 | — | ±0.38 |
| ${}^{37}$P | 37 | 22 | — | — | — | 34446.2858 | — | ±0.39 |
| ${}^{38}$P | 38 | 23 | — | — | — | 35382.1544 | — | ±0.40 |
| ${}^{39}$P | 39 | 24 | — | — | — | 36315.4954 | — | ±0.40 |
| ${}^{40}$P | 40 | 25 | — | — | — | 37251.6250 | — | ±0.41 |
| ${}^{41}$P | 41 | 26 | 127.1462 | -607777.46 ± 370.6799 | 38383.3011 | 38186.2785 | +5159512.94 ± 3146.75 | ±0.42 |
| ${}^{42}$P | 42 | 27 | 132.6155 | -593414.02 ± 291.2858 | 39317.3973 | 39123.8442 | +4947189.73 ± 2428.41 | ±0.42 |
| ${}^{43}$P | 43 | 28 | 138.0765 | -581944.89 ± 911.3397 | 40251.5017 | 40059.2868 | +4798260.48 ± 7487.43 | ±0.43 |
| ${}^{44}$P | 44 | 29 | 143.5297 | -568056.23 ± 1191.7373 | 41185.6139 | 40996.8505 | +4604338.06 ± 9747.36 | ±0.43 |
| ${}^{45}$P | 45 | 30 | 148.9755 | -555986.10 ± 1475.3219 | 42119.7335 | 41933.1949 | +4448470.46 ± 11928.79 | ±0.44 |
| ${}^{46}$P | 46 | 31 | 154.4143 | -541416.40 ± 1502.7322 | 43053.8602 | 42871.5690 | +4252028.98 ± 11667.69 | ±0.44 |
| ${}^{47}$P | 47 | 32 | 159.8462 | -528230.84 ± 1803.3014 | 43987.9936 | 43809.0331 | +4085014.99 ± 13693.12 | ±0.45 |

### Sulfur (Z = 16)

_9 of 24 isotopes with a framework prediction; 9 of 24 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{26}$S | 26 | 10 | — | — | — | 24246.5270 | — | ±0.25 |
| ${}^{27}$S | 27 | 11 | — | — | — | 25167.8315 | — | ±0.27 |
| ${}^{28}$S | 28 | 12 | — | — | — | 26085.9081 | — | ±0.28 |
| ${}^{29}$S | 29 | 13 | — | — | — | 27010.2346 | — | ±0.29 |
| ${}^{30}$S | 30 | 14 | — | — | — | 27930.7639 | — | ±0.31 |
| ${}^{31}$S | 31 | 15 | — | — | — | 28857.2747 | — | ±0.32 |
| ${}^{32}$S | 32 | 16 | — | — | — | 29781.7958 | — | ±0.33 |
| ${}^{33}$S | 33 | 17 | — | — | — | 30712.7196 | — | ±0.34 |
| ${}^{34}$S | 34 | 18 | — | — | — | 31640.8678 | — | ±0.35 |
| ${}^{35}$S | 35 | 19 | — | — | — | 32573.4474 | — | ±0.36 |
| ${}^{36}$S | 36 | 20 | — | — | — | 33503.1236 | — | ±0.36 |
| ${}^{37}$S | 37 | 21 | — | — | — | 34438.3854 | — | ±0.37 |
| ${}^{38}$S | 38 | 22 | — | — | — | 35369.9147 | — | ±0.38 |
| ${}^{39}$S | 39 | 23 | — | — | — | 36305.1074 | — | ±0.39 |
| ${}^{40}$S | 40 | 24 | — | — | — | 37236.9263 | — | ±0.39 |
| ${}^{41}$S | 41 | 25 | 118.5927 | -648525.75 ± 12.1512 | 38391.0723 | 38172.2497 | +5732504.79 ± 107.37 | ±0.40 |
| ${}^{42}$S | 42 | 26 | 124.1053 | -639350.07 ± 8.1165 | 39325.1252 | 39105.1146 | +5626132.22 ± 71.46 | ±0.41 |
| ${}^{43}$S | 43 | 27 | 129.6084 | -626213.77 ± 14.3356 | 40259.1875 | 40042.0510 | +5422711.14 ± 124.11 | ±0.41 |
| ${}^{44}$S | 44 | 28 | 135.1025 | -615994.90 ± 14.8324 | 41193.2588 | 40976.5363 | +5288940.31 ± 127.30 | ±0.42 |
| ${}^{45}$S | 45 | 29 | 140.5880 | -602875.50 ± 889.7928 | 42127.3386 | 41913.8943 | +5092447.72 ± 7156.13 | ±0.42 |
| ${}^{46}$S | 46 | 30 | 146.0654 | -592121.33 ± 1156.0694 | 43061.4267 | 42849.3687 | +4948916.75 ± 9325.95 | ±0.43 |
| ${}^{47}$S | 47 | 31 | 151.5350 | -578652.64 ± 1176.1631 | 43995.5225 | 43787.4233 | +4752486.70 ± 9126.16 | ±0.43 |
| ${}^{48}$S | 48 | 32 | 156.9972 | -566899.41 ± 1324.1525 | 44929.6257 | 44724.1068 | +4595260.70 ± 11184.40 | ±0.44 |
| ${}^{49}$S | 49 | 33 | 162.4523 | -551979.30 ± 1621.6216 | 45863.7361 | 45663.6024 | +4382782.56 ± 12769.81 | ±0.44 |

### Chlorine (Z = 17)

_12 of 25 isotopes with a framework prediction; 12 of 25 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{28}$Cl | 28 | 11 | — | — | — | 26110.1048 | — | ±0.26 |
| ${}^{29}$Cl | 29 | 12 | — | — | — | 27027.3508 | — | ±0.27 |
| ${}^{30}$Cl | 30 | 13 | — | — | — | 27949.4977 | — | ±0.28 |
| ${}^{31}$Cl | 31 | 14 | — | — | — | 28869.2827 | — | ±0.30 |
| ${}^{32}$Cl | 32 | 15 | — | — | — | 29794.4766 | — | ±0.31 |
| ${}^{33}$Cl | 33 | 16 | — | — | — | 30718.3021 | — | ±0.32 |
| ${}^{34}$Cl | 34 | 17 | — | — | — | 31646.3594 | — | ±0.33 |
| ${}^{35}$Cl | 35 | 18 | — | — | — | 32573.2801 | — | ±0.34 |
| ${}^{36}$Cl | 36 | 19 | — | — | — | 33504.2657 | — | ±0.35 |
| ${}^{37}$Cl | 37 | 20 | — | — | — | 34433.5203 | — | ±0.35 |
| ${}^{38}$Cl | 38 | 21 | — | — | — | 35366.9778 | — | ±0.36 |
| ${}^{39}$Cl | 39 | 22 | — | — | — | 36298.4698 | — | ±0.37 |
| ${}^{40}$Cl | 40 | 23 | — | — | — | 37232.2063 | — | ±0.38 |
| ${}^{41}$Cl | 41 | 24 | 109.6364 | -682150.00 ± 199.2402 | 38399.2462 | 38163.9511 | +6165377.46 ± 1800.73 | ±0.38 |
| ${}^{42}$Cl | 42 | 25 | 115.1953 | -671365.69 ± 170.0718 | 39333.2528 | 39097.9206 | +6019046.70 ± 1524.78 | ±0.39 |
| ${}^{43}$Cl | 43 | 26 | 120.7433 | -662658.63 ± 172.8283 | 40267.2702 | 40030.0869 | +5925123.30 ± 1545.28 | ±0.40 |
| ${}^{44}$Cl | 44 | 27 | 126.2812 | -651462.30 ± 236.1655 | 41201.2978 | 40965.2616 | +5761861.70 ± 2088.75 | ±0.40 |
| ${}^{45}$Cl | 45 | 28 | 131.8092 | -641990.11 ± 369.8421 | 42135.3351 | 41898.9721 | +5641260.48 ± 3249.79 | ±0.41 |
| ${}^{46}$Cl | 46 | 29 | 137.3279 | -630556.51 ± 261.6209 | 43069.3818 | 42834.9938 | +5471881.33 ± 2270.29 | ±0.41 |
| ${}^{47}$Cl | 47 | 30 | 142.8378 | -619731.99 ± 500.5005 | 44003.4374 | 43770.6425 | +5318517.68 ± 4575.47 | ±0.42 |
| ${}^{48}$Cl | 48 | 31 | 148.3392 | -607966.61 ± 1268.5526 | 44937.5014 | 44707.4368 | +5146004.75 ± 11188.57 | ±0.42 |
| ${}^{49}$Cl | 49 | 32 | 153.8324 | -596732.53 ± 1027.6172 | 45871.5736 | 45643.9507 | +4986924.07 ± 8754.96 | ±0.43 |
| ${}^{50}$Cl | 50 | 33 | 159.3179 | -583536.97 ± 1045.6150 | 46805.6535 | 46582.4049 | +4792552.17 ± 8578.58 | ±0.43 |
| ${}^{51}$Cl | 51 | 34 | 164.7960 | -570877.25 ± 1859.2297 | 47739.7409 | 47520.4893 | +4613831.39 ± 14721.06 | ±0.44 |
| ${}^{52}$Cl | 52 | 35 | 170.2670 | -556679.55 ± 1760.0867 | 48673.8353 | 48460.0530 | +4411517.05 ± 14435.64 | ±0.44 |

### Argon (Z = 18)

_14 of 26 isotopes with a framework prediction; 14 of 26 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{29}$Ar | 29 | 11 | — | — | — | 27051.2976 | — | ±0.25 |
| ${}^{30}$Ar | 30 | 12 | — | — | — | 27966.8939 | — | ±0.26 |
| ${}^{31}$Ar | 31 | 13 | — | — | — | 28887.6423 | — | ±0.27 |
| ${}^{32}$Ar | 32 | 14 | — | — | — | 29805.6110 | — | ±0.29 |
| ${}^{33}$Ar | 33 | 15 | — | — | — | 30729.9211 | — | ±0.30 |
| ${}^{34}$Ar | 34 | 16 | — | — | — | 31652.4212 | — | ±0.31 |
| ${}^{35}$Ar | 35 | 17 | — | — | — | 32579.2463 | — | ±0.32 |
| ${}^{36}$Ar | 36 | 18 | — | — | — | 33503.5562 | — | ±0.33 |
| ${}^{37}$Ar | 37 | 19 | — | — | — | 34434.3342 | — | ±0.34 |
| ${}^{38}$Ar | 38 | 20 | — | — | — | 35362.0611 | — | ±0.35 |
| ${}^{39}$Ar | 39 | 21 | — | — | — | 36295.0278 | — | ±0.35 |
| ${}^{40}$Ar | 40 | 22 | — | — | — | 37224.7242 | — | ±0.36 |
| ${}^{41}$Ar | 41 | 23 | 100.2774 | -713418.91 ± 0.9960 | 38407.8229 | 38158.1907 | +6542034.04 ± 9.08 | ±0.37 |
| ${}^{42}$Ar | 42 | 24 | 105.8855 | -705329.85 ± 16.0713 | 39341.7802 | 39088.3297 | +6484045.97 ± 147.75 | ±0.37 |
| ${}^{43}$Ar | 43 | 25 | 111.4815 | -694566.50 ± 14.5495 | 40275.7497 | 40022.2366 | +6334304.75 ± 132.66 | ±0.38 |
| ${}^{44}$Ar | 44 | 26 | 117.0658 | -686762.90 ± 4.2384 | 41209.7308 | 40953.0673 | +6267259.20 ± 38.67 | ±0.39 |
| ${}^{45}$Ar | 45 | 27 | 122.6391 | -676326.87 ± 1.3539 | 42143.7229 | 41887.4639 | +6117798.90 ± 12.23 | ±0.39 |
| ${}^{46}$Ar | 46 | 28 | 128.2018 | -668703.23 ± 6.0149 | 43077.7256 | 42818.9575 | +6043307.36 ± 54.39 | ±0.40 |
| ${}^{47}$Ar | 47 | 29 | 133.7545 | -657599.05 ± 3.1042 | 44011.7384 | 43754.8556 | +5870954.79 ± 27.68 | ±0.40 |
| ${}^{48}$Ar | 48 | 30 | 139.2976 | -647968.21 ± 42.3719 | 44945.7607 | 44689.3621 | +5737353.55 ± 375.19 | ±0.41 |
| ${}^{49}$Ar | 49 | 31 | 144.8315 | -636529.26 ± 983.7678 | 45879.7922 | 45626.1508 | +5559124.88 ± 8758.38 | ±0.41 |
| ${}^{50}$Ar | 50 | 32 | 150.3566 | -626628.78 ± 1241.6191 | 46813.8325 | 46561.4752 | +5419874.56 ± 10743.05 | ±0.42 |
| ${}^{51}$Ar | 51 | 33 | 155.8733 | -614195.97 ± 1009.8460 | 47747.8812 | 47499.7096 | +5224698.35 ± 8412.91 | ±0.42 |
| ${}^{52}$Ar | 52 | 34 | 161.3820 | -603487.94 ± 1533.1545 | 48681.9380 | 48436.3139 | +5071073.73 ± 12384.97 | ±0.43 |
| ${}^{53}$Ar | 53 | 35 | 166.8830 | -589848.25 ± 1693.3698 | 49616.0024 | 49375.9781 | +4861156.26 ± 14149.00 | ±0.43 |
| ${}^{54}$Ar | 54 | 36 | 172.3765 | -578759.90 ± 1979.4141 | 50550.0743 | 50313.2419 | +4707159.21 ± 15903.44 | ±0.44 |

### Potassium (Z = 19)

_19 of 29 isotopes with a framework prediction; 19 of 29 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{31}$K | 31 | 12 | — | — | — | 28910.5776 | — | ±0.25 |
| ${}^{32}$K | 32 | 13 | — | — | — | 29829.8011 | — | ±0.27 |
| ${}^{33}$K | 33 | 14 | — | — | — | 30746.8459 | — | ±0.28 |
| ${}^{34}$K | 34 | 15 | — | — | — | 31669.5793 | — | ±0.29 |
| ${}^{35}$K | 35 | 16 | — | — | — | 32591.1207 | — | ±0.30 |
| ${}^{36}$K | 36 | 17 | — | — | — | 33516.3706 | — | ±0.31 |
| ${}^{37}$K | 37 | 18 | — | — | — | 34440.4816 | — | ±0.32 |
| ${}^{38}$K | 38 | 19 | — | — | — | 35367.9752 | — | ±0.33 |
| ${}^{39}$K | 39 | 20 | — | — | — | 36294.4628 | — | ±0.34 |
| ${}^{40}$K | 40 | 21 | — | — | — | 37226.2287 | — | ±0.34 |
| ${}^{41}$K | 41 | 22 | 90.5156 | -742574.78 ± 0.0350 | 38416.8024 | 38155.6987 | +6843110.88 ± 0.10 | ±0.35 |
| ${}^{42}$K | 42 | 23 | 96.1760 | -732214.19 ± 0.2924 | 39350.7074 | 39087.7303 | +6727867.09 ± 2.69 | ±0.36 |
| ${}^{43}$K | 43 | 24 | 101.8227 | -723891.15 ± 1.1077 | 40284.6261 | 40017.6711 | +6670928.83 ± 10.24 | ±0.37 |
| ${}^{44}$K | 44 | 25 | 107.4564 | -714253.49 ± 1.1115 | 41218.5579 | 40949.9591 | +6559195.97 ± 10.24 | ±0.37 |
| ${}^{45}$K | 45 | 26 | 113.0776 | -706261.69 ± 1.3560 | 42152.5021 | 41880.6190 | +6491858.29 ± 12.46 | ±0.38 |
| ${}^{46}$K | 46 | 27 | 118.6870 | -697095.67 ± 1.8549 | 43086.4581 | 42813.3148 | +6379867.13 ± 16.97 | ±0.38 |
| ${}^{47}$K | 47 | 28 | 124.2851 | -689442.04 ± 3.4880 | 44020.4254 | 43744.5109 | +6307409.34 ± 31.94 | ±0.39 |
| ${}^{48}$K | 48 | 29 | 129.8724 | -679203.18 ± 1.9089 | 44954.4035 | 44679.4325 | +6154309.25 ± 17.30 | ±0.40 |
| ${}^{49}$K | 49 | 30 | 135.4494 | -669830.07 ± 1.9588 | 45888.3920 | 45613.5996 | +6024351.83 ± 17.56 | ±0.40 |
| ${}^{50}$K | 50 | 31 | 141.0166 | -659733.04 ± 18.6522 | 46822.3902 | 46548.9773 | +5873660.73 ± 166.09 | ±0.41 |
| ${}^{51}$K | 51 | 32 | 146.5743 | -650421.11 ± 31.1020 | 47756.3979 | 47483.6838 | +5743322.54 ± 274.64 | ±0.41 |
| ${}^{52}$K | 52 | 33 | 152.1229 | -639503.38 ± 79.4698 | 48690.4147 | 48420.5558 | +5573230.79 ± 692.55 | ±0.42 |
| ${}^{53}$K | 53 | 34 | 157.6629 | -629212.46 ± 262.8742 | 49624.4401 | 49356.8918 | +5420688.67 ± 2264.71 | ±0.42 |
| ${}^{54}$K | 54 | 35 | 163.1946 | -617016.53 ± 887.0866 | 50558.4739 | 50295.5314 | +5227949.32 ± 7945.26 | ±0.42 |
| ${}^{55}$K | 55 | 36 | 168.7183 | -606313.44 ± 1155.0308 | 51492.5156 | 51232.6461 | +5072341.51 ± 9763.55 | ±0.43 |
| ${}^{56}$K | 56 | 37 | 174.2343 | -593980.51 ± 1435.4691 | 52426.5650 | 52171.6499 | +4886084.15 ± 11498.24 | ±0.43 |
| ${}^{57}$K | 57 | 38 | 179.7430 | -583050.98 ± 1454.4493 | 53360.6218 | 53109.2937 | +4732279.60 ± 11295.24 | ±0.44 |
| ${}^{58}$K | 58 | 39 | 185.2445 | -570543.12 ± 1613.5539 | 54294.6857 | 54048.5882 | +4553263.75 ± 12943.02 | ±0.44 |
| ${}^{59}$K | 59 | 40 | 190.7392 | -559074.20 ± 1909.4381 | 55228.7564 | 54986.9018 | +4398404.35 ± 14551.71 | ±0.44 |

### Calcium (Z = 20)

_22 of 29 isotopes with a framework prediction; 22 of 29 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{33}$Ca | 33 | 13 | — | — | — | 30770.3354 | — | ±0.26 |
| ${}^{34}$Ca | 34 | 14 | — | — | — | 31685.6895 | — | ±0.27 |
| ${}^{35}$Ca | 35 | 15 | — | — | — | 32607.4839 | — | ±0.28 |
| ${}^{36}$Ca | 36 | 16 | — | — | — | 33527.3366 | — | ±0.29 |
| ${}^{37}$Ca | 37 | 17 | — | — | — | 34452.1458 | — | ±0.30 |
| ${}^{38}$Ca | 38 | 18 | — | — | — | 35374.7174 | — | ±0.31 |
| ${}^{39}$Ca | 39 | 19 | — | — | — | 36300.9873 | — | ±0.32 |
| ${}^{40}$Ca | 40 | 20 | 408.7713 | +195055.37 ± 0.0702 | 37158.1989 | 37224.9177 | -1792316.22 ± 0.55 | ±0.33 |
| ${}^{41}$Ca | 41 | 21 | 80.3511 | -770697.45 ± 0.3978 | 38426.1846 | 38156.1203 | +7077874.89 ± 3.59 | ±0.34 |
| ${}^{42}$Ca | 42 | 22 | 86.0667 | -762178.04 ± 0.4062 | 39360.0343 | 39084.2051 | +7057307.63 ± 3.79 | ±0.34 |
| ${}^{43}$Ca | 43 | 23 | 91.7671 | -751865.83 ± 0.6162 | 40293.8994 | 40015.8376 | +6948793.43 ± 5.68 | ±0.35 |
| ${}^{44}$Ca | 44 | 24 | 97.4529 | -744191.08 ± 0.8547 | 41227.7790 | 40944.2718 | +6924220.60 ± 7.92 | ±0.36 |
| ${}^{45}$Ca | 45 | 25 | 103.1248 | -734470.70 ± 0.9385 | 42161.6725 | 41876.4224 | +6811710.49 ± 8.72 | ±0.36 |
| ${}^{46}$Ca | 46 | 26 | 108.7835 | -727204.55 ± 5.6062 | 43095.5792 | 42805.5892 | +6774583.95 ± 52.18 | ±0.37 |
| ${}^{47}$Ca | 47 | 27 | 114.4296 | -718188.08 ± 5.4749 | 44029.4985 | 43737.8782 | +6667454.96 ± 50.77 | ±0.38 |
| ${}^{48}$Ca | 48 | 28 | 120.0637 | -711386.16 ± 0.0462 | 44963.4299 | 44667.4921 | +6625350.53 ± 0.38 | ±0.38 |
| ${}^{49}$Ca | 49 | 29 | 125.6863 | -701562.48 ± 0.4189 | 45897.3728 | 45601.9111 | +6479151.43 ± 3.88 | ±0.39 |
| ${}^{50}$Ca | 50 | 30 | 131.2978 | -692876.49 ± 3.7075 | 46831.3266 | 46535.1160 | +6365315.09 ± 34.03 | ±0.39 |
| ${}^{51}$Ca | 51 | 31 | 136.8988 | -683340.98 ± 1.2033 | 47765.2910 | 47469.8670 | +6223401.62 ± 10.99 | ±0.40 |
| ${}^{52}$Ca | 52 | 32 | 142.4898 | -674924.20 ± 1.5304 | 48699.2655 | 48403.4271 | +6111930.66 ± 13.86 | ±0.40 |
| ${}^{53}$Ca | 53 | 33 | 148.0710 | -664633.90 ± 99.1528 | 49633.2497 | 49339.7998 | +5947528.79 ± 887.32 | ±0.41 |
| ${}^{54}$Ca | 54 | 34 | 153.6430 | -655017.58 ± 108.7603 | 50567.2431 | 50275.5210 | +5802467.85 ± 963.44 | ±0.41 |
| ${}^{55}$Ca | 55 | 35 | 159.2061 | -643775.19 ± 358.4822 | 51501.2455 | 51213.5253 | +5618049.66 ± 3128.41 | ±0.42 |
| ${}^{56}$Ca | 56 | 36 | 164.7606 | -633749.12 ± 554.9369 | 52435.2564 | 52150.1594 | +5466847.20 ± 4786.95 | ±0.42 |
| ${}^{57}$Ca | 57 | 37 | 170.3069 | -622366.00 ± 884.7321 | 53369.2755 | 53088.6043 | +5286844.32 ± 7527.25 | ±0.43 |
| ${}^{58}$Ca | 58 | 38 | 175.8452 | -612696.14 ± 1149.7190 | 54303.3026 | 54025.1276 | +5148993.18 ± 9258.88 | ±0.43 |
| ${}^{59}$Ca | 59 | 39 | 181.3760 | -601171.63 ± 1297.3534 | 55237.3373 | 54963.9618 | +4973721.34 ± 10914.10 | ±0.43 |
| ${}^{60}$Ca | 60 | 40 | 186.8994 | -591583.93 ± 1573.3578 | 56171.3793 | 55900.6462 | +4843111.83 ± 12514.20 | ±0.44 |
| ${}^{61}$Ca | 61 | 41 | 192.4157 | -579587.49 ± 1732.6403 | 57105.4284 | 56840.1503 | +4667091.49 ± 14077.26 | ±0.44 |

### Scandium (Z = 21)

_23 of 29 isotopes with a framework prediction; 23 of 29 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{35}$Sc | 35 | 14 | — | — | — | 32629.3936 | — | ±0.26 |
| ${}^{36}$Sc | 36 | 15 | — | — | — | 33549.9380 | — | ±0.27 |
| ${}^{37}$Sc | 37 | 16 | — | — | — | 34469.0618 | — | ±0.28 |
| ${}^{38}$Sc | 38 | 17 | — | — | — | 35392.5265 | — | ±0.29 |
| ${}^{39}$Sc | 39 | 18 | — | — | — | 36314.0973 | — | ±0.30 |
| ${}^{40}$Sc | 40 | 19 | — | — | — | 37239.2408 | — | ±0.31 |
| ${}^{41}$Sc | 41 | 20 | 69.7838 | -796630.11 ± 0.2270 | 38435.9696 | 38162.6159 | +7162864.86 ± 2.03 | ±0.32 |
| ${}^{42}$Sc | 42 | 21 | 75.5577 | -786973.61 ± 0.4381 | 39369.7610 | 39090.6314 | +7140577.33 ± 3.93 | ±0.33 |
| ${}^{43}$Sc | 43 | 22 | 81.3146 | -778328.85 ± 5.0757 | 40303.5695 | 40018.0583 | +7134559.26 ± 46.53 | ±0.34 |
| ${}^{44}$Sc | 44 | 23 | 87.0554 | -768792.37 ± 4.6626 | 41237.3942 | 40947.9245 | +7069214.41 ± 42.86 | ±0.34 |
| ${}^{45}$Sc | 45 | 24 | 92.7808 | -760783.32 ± 1.7055 | 42171.2343 | 41876.1623 | +7046297.69 ± 15.84 | ±0.35 |
| ${}^{46}$Sc | 46 | 25 | 98.4914 | -751668.66 ± 1.6933 | 43105.0890 | 42806.9671 | +6964330.37 ± 15.67 | ±0.36 |
| ${}^{47}$Sc | 47 | 26 | 104.1881 | -744172.63 ± 4.7432 | 44038.9577 | 43735.8860 | +6929588.37 ± 44.13 | ±0.36 |
| ${}^{48}$Sc | 48 | 27 | 109.8715 | -735566.85 ± 11.9105 | 44972.8398 | 44667.2129 | +6842309.92 ± 110.80 | ±0.37 |
| ${}^{49}$Sc | 49 | 28 | 115.5420 | -728537.36 ± 5.3302 | 45906.7347 | 45596.6486 | +6800632.00 ± 49.72 | ±0.37 |
| ${}^{50}$Sc | 50 | 29 | 121.2004 | -719231.49 ± 5.8262 | 46840.6417 | 46530.1681 | +6672523.91 ± 54.05 | ±0.38 |
| ${}^{51}$Sc | 51 | 30 | 126.8471 | -710697.53 ± 5.7344 | 47774.5605 | 47462.9489 | +6565363.98 ± 52.99 | ±0.39 |
| ${}^{52}$Sc | 52 | 31 | 132.4825 | -701483.31 ± 6.9247 | 48708.4904 | 48397.1698 | +6432619.54 ± 63.51 | ±0.39 |
| ${}^{53}$Sc | 53 | 32 | 138.1073 | -693176.79 ± 39.3155 | 49642.4311 | 49330.4179 | +6324964.51 ± 358.77 | ±0.40 |
| ${}^{54}$Sc | 54 | 33 | 143.7218 | -683334.49 ± 30.7919 | 50576.3821 | 50266.2437 | +6169913.73 ± 277.97 | ±0.40 |
| ${}^{55}$Sc | 55 | 34 | 149.3263 | -674198.53 ± 136.1634 | 51510.3429 | 51201.3336 | +6035180.92 ± 1218.92 | ±0.41 |
| ${}^{56}$Sc | 56 | 35 | 154.9214 | -664003.50 ± 563.1695 | 52444.3133 | 52138.1540 | +5872077.90 ± 4980.31 | ±0.41 |
| ${}^{57}$Sc | 57 | 36 | 160.5073 | -654834.45 ± 386.6065 | 53378.2927 | 53073.7843 | +5737455.71 ± 3387.33 | ±0.41 |
| ${}^{58}$Sc | 58 | 37 | 166.0845 | -644500.86 ± 406.7440 | 54312.2810 | 54011.1784 | +5574819.49 ± 3518.25 | ±0.42 |
| ${}^{59}$Sc | 59 | 38 | 171.6532 | -635252.35 ± 530.4644 | 55246.2777 | 54947.3226 | +5440759.68 ± 4543.27 | ±0.42 |
| ${}^{60}$Sc | 60 | 39 | 177.2137 | -624849.23 ± 1016.1311 | 56180.2826 | 55885.0959 | +5282029.92 ± 8950.73 | ±0.43 |
| ${}^{61}$Sc | 61 | 40 | 182.7664 | -615579.84 ± 1283.0382 | 57114.2954 | 56821.6405 | +5150411.20 ± 10557.28 | ±0.43 |
| ${}^{62}$Sc | 62 | 41 | 188.3115 | -604932.00 ± 1300.7284 | 58048.3157 | 57759.9448 | +4992575.08 ± 10385.78 | ±0.43 |
| ${}^{63}$Sc | 63 | 42 | 193.8493 | -595294.79 ± 1446.7973 | 58982.3433 | 58697.1983 | +4857896.97 ± 11917.98 | ±0.44 |

### Titanium (Z = 22)

_25 of 29 isotopes with a framework prediction; 25 of 29 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{37}$Ti | 37 | 15 | — | — | — | 34490.4517 | — | ±0.27 |
| ${}^{38}$Ti | 38 | 16 | — | — | — | 35408.1458 | — | ±0.28 |
| ${}^{39}$Ti | 39 | 17 | — | — | — | 36330.7702 | — | ±0.29 |
| ${}^{40}$Ti | 40 | 18 | — | — | — | 37250.7707 | — | ±0.29 |
| ${}^{41}$Ti | 41 | 19 | 58.8137 | -821457.40 ± 84.8353 | 38446.1573 | 38175.5607 | +7088214.30 ± 732.01 | ±0.30 |
| ${}^{42}$Ti | 42 | 20 | 64.6489 | -813631.83 ± 0.7749 | 39379.8875 | 39097.6480 | +7218835.77 ± 6.89 | ±0.31 |
| ${}^{43}$Ti | 43 | 21 | 70.4653 | -803811.09 ± 15.9228 | 40313.6365 | 40024.9309 | +7213145.72 ± 142.87 | ±0.32 |
| ${}^{44}$Ti | 44 | 22 | 76.2638 | -796887.04 ± 1.8632 | 41247.4034 | 40948.1920 | +7307073.35 ± 17.08 | ±0.33 |
| ${}^{45}$Ti | 45 | 23 | 82.0454 | -786899.58 ± 2.1740 | 42181.1873 | 41878.2244 | +7234378.22 ± 19.95 | ±0.34 |
| ${}^{46}$Ti | 46 | 24 | 87.8107 | -779479.45 ± 0.2310 | 43114.9874 | 42804.6005 | +7251251.21 ± 2.11 | ±0.34 |
| ${}^{47}$Ti | 47 | 25 | 93.5606 | -770165.50 ± 0.1963 | 44048.8030 | 43735.2853 | +7168529.85 ± 1.81 | ±0.35 |
| ${}^{48}$Ti | 48 | 26 | 99.2957 | -762850.27 ± 0.1834 | 44982.6333 | 44663.2240 | +7151504.12 ± 1.65 | ±0.36 |
| ${}^{49}$Ti | 49 | 27 | 105.0167 | -753971.04 ± 0.1837 | 45916.4776 | 45594.6471 | +7058516.68 ± 1.72 | ±0.36 |
| ${}^{50}$Ti | 50 | 28 | 110.7243 | -747081.37 ± 0.1942 | 46850.3355 | 46523.2733 | +7030077.02 ± 1.76 | ±0.37 |
| ${}^{51}$Ti | 51 | 29 | 116.4189 | -737888.81 ± 1.0908 | 47784.2063 | 47456.4663 | +6906117.96 ± 10.19 | ±0.37 |
| ${}^{52}$Ti | 52 | 30 | 122.1012 | -729849.36 ± 6.0747 | 48718.0894 | 48388.2157 | +6817232.25 ± 56.75 | ±0.38 |
| ${}^{53}$Ti | 53 | 31 | 127.7717 | -720686.90 ± 6.3144 | 49651.9844 | 49322.3061 | +6684162.37 ± 58.55 | ±0.38 |
| ${}^{54}$Ti | 54 | 32 | 133.4308 | -712671.06 ± 34.0942 | 50585.8907 | 50254.9378 | +6585480.41 ± 315.10 | ±0.39 |
| ${}^{55}$Ti | 55 | 33 | 139.0790 | -703167.35 ± 61.6272 | 51519.8079 | 51190.3432 | +6436071.35 ± 564.10 | ±0.39 |
| ${}^{56}$Ti | 56 | 34 | 144.7167 | -694822.69 ± 211.3026 | 52453.7357 | 52124.2468 | +6321220.32 ± 1922.33 | ±0.40 |
| ${}^{57}$Ti | 57 | 35 | 150.3443 | -684981.46 ± 431.3798 | 53387.6735 | 53060.7621 | +6161076.19 ± 3880.06 | ±0.40 |
| ${}^{58}$Ti | 58 | 36 | 155.9622 | -676321.18 ± 380.4936 | 54321.6210 | 53995.7403 | +6035302.18 ± 3395.44 | ±0.41 |
| ${}^{59}$Ti | 59 | 37 | 161.5708 | -666769.51 ± 608.4205 | 55255.5778 | 54932.2724 | +5885526.89 ± 5460.20 | ±0.41 |
| ${}^{60}$Ti | 60 | 38 | 167.1704 | -658255.04 ± 491.2922 | 56189.5436 | 55867.5465 | +5763580.08 ± 4301.70 | ±0.41 |
| ${}^{61}$Ti | 61 | 39 | 172.7613 | -648529.02 ± 620.5014 | 57123.5181 | 56804.7702 | +5611286.46 ± 5280.21 | ±0.42 |
| ${}^{62}$Ti | 62 | 40 | 178.3439 | -639985.61 ± 750.9387 | 58057.5009 | 57740.4347 | +5491234.65 ± 6920.82 | ±0.42 |
| ${}^{63}$Ti | 63 | 41 | 183.9184 | -630041.77 ± 1013.8132 | 58991.4918 | 58678.2685 | +5337978.34 ± 8524.66 | ±0.43 |
| ${}^{64}$Ti | 64 | 42 | 189.4852 | -621683.37 ± 1150.0128 | 59925.4905 | 59614.1425 | +5222720.86 ± 10062.75 | ±0.43 |
| ${}^{65}$Ti | 65 | 43 | 195.0444 | -611612.35 ± 1423.7639 | 60859.4967 | 60552.3266 | +5072804.90 ± 11552.85 | ±0.43 |

### Vanadium (Z = 23)

_27 of 29 isotopes with a framework prediction; 27 of 29 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{39}$V | 39 | 16 | — | — | — | 36350.8401 | — | ±0.27 |
| ${}^{40}$V | 40 | 17 | — | — | — | 37272.2341 | — | ±0.28 |
| ${}^{41}$V | 41 | 18 | 47.4409 | -848249.81 ± 655.7377 | 38456.7477 | 38191.5684 | +6943399.05 ± 5243.86 | ±0.29 |
| ${}^{42}$V | 42 | 19 | 53.3403 | -837677.96 ± 639.0593 | 39390.4137 | 39115.1327 | +7037711.21 ± 5000.97 | ±0.30 |
| ${}^{43}$V | 43 | 20 | 59.2191 | -829334.43 ± 123.4895 | 40324.1004 | 40036.3301 | +7187729.25 ± 1070.25 | ±0.30 |
| ${}^{44}$V | 44 | 21 | 65.0782 | -819704.03 ± 20.1257 | 41257.8067 | 40961.9325 | +7223150.87 ± 177.35 | ±0.31 |
| ${}^{45}$V | 45 | 22 | 70.9186 | -811937.66 ± 2.2912 | 42191.5317 | 41885.3482 | +7310037.53 ± 20.59 | ±0.32 |
| ${}^{46}$V | 46 | 23 | 76.7413 | -803410.27 ± 0.3417 | 43125.2745 | 42811.6529 | +7325613.32 ± 3.11 | ±0.33 |
| ${}^{47}$V | 47 | 24 | 82.5469 | -795354.31 ± 0.2796 | 44059.0343 | 43738.2158 | +7334969.05 ± 2.51 | ±0.33 |
| ${}^{48}$V | 48 | 25 | 88.3364 | -786579.37 ± 2.3426 | 44992.8102 | 44667.2390 | +7288815.75 ± 21.75 | ±0.34 |
| ${}^{49}$V | 49 | 26 | 94.1103 | -778804.83 ± 1.9348 | 45926.6017 | 45595.2489 | +7267265.81 ± 18.06 | ±0.35 |
| ${}^{50}$V | 50 | 27 | 99.8695 | -770306.89 ± 0.2185 | 46860.4080 | 46525.4819 | +7198765.85 ± 1.98 | ±0.35 |
| ${}^{51}$V | 51 | 28 | 105.6144 | -763114.75 ± 0.2173 | 47794.2284 | 47453.9962 | +7169728.38 ± 2.04 | ±0.36 |
| ${}^{52}$V | 52 | 29 | 111.3458 | -754288.97 ± 0.3557 | 48728.0625 | 48386.2504 | +7064240.57 ± 3.27 | ±0.37 |
| ${}^{53}$V | 53 | 30 | 117.0642 | -746415.34 ± 6.7163 | 49661.9095 | 49317.3358 | +6986867.50 ± 62.92 | ±0.37 |
| ${}^{54}$V | 54 | 31 | 122.7701 | -737533.58 ± 23.8971 | 50595.7690 | 50250.7833 | +6865280.11 ± 222.46 | ±0.38 |
| ${}^{55}$V | 55 | 32 | 128.4640 | -729579.98 ± 56.8694 | 51529.6405 | 51183.0506 | +6771577.17 ± 527.78 | ±0.38 |
| ${}^{56}$V | 56 | 33 | 134.1464 | -720634.94 ± 366.2868 | 52463.5236 | 52117.4864 | +6639559.68 ± 3374.76 | ±0.39 |
| ${}^{57}$V | 57 | 34 | 139.8177 | -712608.51 ± 174.2315 | 53397.4177 | 53050.7288 | +6535043.34 ± 1597.83 | ±0.39 |
| ${}^{58}$V | 58 | 35 | 145.4784 | -703452.06 ± 195.3144 | 54331.3224 | 53986.2274 | +6392277.94 ± 1774.81 | ±0.40 |
| ${}^{59}$V | 59 | 36 | 151.1289 | -695196.81 ± 277.1126 | 55265.2374 | 54920.5415 | +6276265.39 ± 2501.80 | ±0.40 |
| ${}^{60}$V | 60 | 37 | 156.7694 | -686067.19 ± 364.3452 | 56199.1623 | 55856.5588 | +6133629.56 ± 3257.38 | ±0.40 |
| ${}^{61}$V | 61 | 38 | 162.4005 | -678117.63 ± 465.6125 | 57133.0966 | 56790.9632 | +6024434.52 ± 4136.56 | ±0.41 |
| ${}^{62}$V | 62 | 39 | 168.0223 | -669013.44 ± 520.6188 | 58067.0402 | 57727.4213 | +5883147.56 ± 4578.18 | ±0.41 |
| ${}^{63}$V | 63 | 40 | 173.6353 | -661026.87 ± 663.7493 | 59000.9926 | 58662.3884 | +5772083.85 ± 5795.80 | ±0.42 |
| ${}^{64}$V | 64 | 41 | 179.2398 | -651880.47 ± 745.8048 | 59934.9536 | 59599.3029 | +5631789.37 ± 6704.96 | ±0.42 |
| ${}^{65}$V | 65 | 42 | 184.8360 | -643699.97 ± 1002.3807 | 60868.9228 | 60535.0064 | +5516087.88 ± 8263.19 | ±0.42 |
| ${}^{66}$V | 66 | 43 | 190.4242 | -634505.28 ± 1013.4279 | 61802.9000 | 61472.3112 | +5377849.72 ± 8137.20 | ±0.43 |
| ${}^{67}$V | 67 | 44 | 196.0047 | -626332.42 ± 1149.5721 | 62736.8849 | 62408.3612 | +5264097.95 ± 9612.21 | ±0.43 |

### Chromium (Z = 24)

_30 of 30 isotopes with a framework prediction; 30 of 30 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{41}$Cr | 41 | 17 | 35.6653 | -877756.26 ± 1405.2839 | 38467.7410 | 38211.6682 | +6701428.04 ± 10457.83 | ±0.27 |
| ${}^{42}$Cr | 42 | 18 | 41.6320 | -867055.04 ± 938.8412 | 39401.3397 | 39129.8122 | +6939149.06 ± 7665.28 | ±0.28 |
| ${}^{43}$Cr | 43 | 19 | 47.5760 | -855935.05 ± 651.0417 | 40334.9611 | 40052.2763 | +7057895.87 ± 5000.25 | ±0.29 |
| ${}^{44}$Cr | 44 | 20 | 53.4985 | -847052.45 ± 146.4723 | 41268.6040 | 40972.3187 | +7231354.78 ± 1250.41 | ±0.30 |
| ${}^{45}$Cr | 45 | 21 | 59.4006 | -836788.09 ± 97.2585 | 42202.2674 | 41897.7199 | +7268832.75 ± 844.84 | ±0.31 |
| ${}^{46}$Cr | 46 | 22 | 65.2832 | -829090.76 ± 29.9862 | 43135.9502 | 42819.2572 | +7396041.82 ± 267.47 | ±0.31 |
| ${}^{47}$Cr | 47 | 23 | 71.1472 | -819943.71 ± 13.1554 | 44069.6516 | 43745.6598 | +7406262.76 ± 118.77 | ±0.32 |
| ${}^{48}$Cr | 48 | 24 | 76.9935 | -812881.11 ± 17.7666 | 45003.3708 | 44668.8957 | +7487875.25 ± 163.66 | ±0.33 |
| ${}^{49}$Cr | 49 | 25 | 82.8228 | -803760.95 ± 5.2129 | 45937.1069 | 45597.8787 | +7439559.87 ± 48.27 | ±0.33 |
| ${}^{50}$Cr | 50 | 26 | 88.6359 | -796263.08 ± 0.2184 | 46870.8592 | 46524.4438 | +7445878.45 ± 2.00 | ±0.34 |
| ${}^{51}$Cr | 51 | 27 | 94.4336 | -787460.97 ± 0.3788 | 47804.6270 | 47454.7486 | +7372885.01 ± 3.49 | ±0.35 |
| ${}^{52}$Cr | 52 | 28 | 100.2163 | -780396.74 ± 0.2507 | 48738.4096 | 48382.2739 | +7360872.48 ± 2.31 | ±0.35 |
| ${}^{53}$Cr | 53 | 29 | 105.9849 | -771727.60 ± 0.2511 | 49672.2065 | 49313.8999 | +7265834.72 ± 2.34 | ±0.36 |
| ${}^{54}$Cr | 54 | 30 | 111.7397 | -764267.26 ± 0.2848 | 50606.0171 | 50243.7462 | +7210267.54 ± 2.63 | ±0.36 |
| ${}^{55}$Cr | 55 | 31 | 117.4815 | -755377.60 ± 0.4810 | 51539.8407 | 51177.0654 | +7088631.38 ± 4.46 | ±0.37 |
| ${}^{56}$Cr | 56 | 32 | 123.2107 | -747778.90 ± 1.1808 | 52473.6770 | 52108.3847 | +7010240.44 ± 11.08 | ±0.37 |
| ${}^{57}$Cr | 57 | 33 | 128.9277 | -738914.29 ± 3.7745 | 53407.5253 | 53042.6389 | +6879115.14 ± 35.12 | ±0.38 |
| ${}^{58}$Cr | 58 | 34 | 134.6331 | -731459.81 ± 5.9463 | 54341.3854 | 53974.6662 | +6794282.84 ± 55.23 | ±0.38 |
| ${}^{59}$Cr | 59 | 35 | 140.3273 | -722424.94 ± 1.3304 | 55275.2566 | 54910.0362 | +6651250.18 ± 12.21 | ±0.39 |
| ${}^{60}$Cr | 60 | 36 | 146.0107 | -715051.64 ± 2.1779 | 56209.1386 | 55842.7377 | +6561298.53 ± 20.02 | ±0.39 |
| ${}^{61}$Cr | 61 | 37 | 151.6837 | -706079.46 ± 3.6051 | 57143.0310 | 56778.6438 | +6417680.55 ± 32.81 | ±0.40 |
| ${}^{62}$Cr | 62 | 38 | 157.3467 | -698856.84 ± 6.5975 | 58076.9335 | 57711.7818 | +6327159.80 ± 59.72 | ±0.40 |
| ${}^{63}$Cr | 63 | 39 | 163.0000 | -690052.24 ± 138.1605 | 59010.8456 | 58647.9502 | +6187691.04 ± 1238.86 | ±0.41 |
| ${}^{64}$Cr | 64 | 40 | 168.6439 | -682658.98 ± 564.4083 | 59944.7671 | 59581.9827 | +6088828.36 ± 5034.09 | ±0.41 |
| ${}^{65}$Cr | 65 | 41 | 174.2788 | -673739.06 ± 365.0523 | 60878.6976 | 60518.8068 | +5946760.94 ± 3309.24 | ±0.41 |
| ${}^{66}$Cr | 66 | 42 | 179.9050 | -666279.02 ± 612.1450 | 61812.6369 | 61453.4708 | +5844521.77 ± 4880.78 | ±0.42 |
| ${}^{67}$Cr | 67 | 43 | 185.5227 | -657260.09 ± 742.6662 | 62746.5846 | 62390.8351 | +5701950.52 ± 6404.96 | ±0.42 |
| ${}^{68}$Cr | 68 | 44 | 191.1323 | -649792.06 ± 872.1655 | 63680.5404 | 63325.9090 | +5600100.70 ± 7899.02 | ±0.42 |
| ${}^{69}$Cr | 69 | 45 | 196.7340 | -640859.44 ± 881.7231 | 64614.5042 | 64263.4634 | +5462525.52 ± 7783.77 | ±0.43 |
| ${}^{70}$Cr | 70 | 46 | 202.3280 | -633384.08 ± 1141.5525 | 65548.4756 | 65198.9471 | +5360953.29 ± 9200.80 | ±0.43 |

### Manganese (Z = 25)

_31 of 31 isotopes with a framework prediction; 31 of 31 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{43}$Mn | 43 | 18 | 35.5361 | -885426.30 ± 1247.7471 | 40346.2188 | 40071.6160 | +6852798.86 ± 9972.42 | ±0.27 |
| ${}^{44}$Mn | 44 | 19 | 41.5248 | -873441.61 ± 938.7153 | 41279.7954 | 40993.2009 | +6991269.69 ± 7316.85 | ±0.28 |
| ${}^{45}$Mn | 45 | 20 | 47.4913 | -863771.57 ± 903.5756 | 42213.3944 | 41912.2549 | +7184998.54 ± 7156.41 | ±0.29 |
| ${}^{46}$Mn | 46 | 21 | 53.4365 | -853252.78 ± 237.8955 | 43147.0146 | 42836.3110 | +7253275.76 ± 2022.33 | ±0.30 |
| ${}^{47}$Mn | 47 | 22 | 59.3614 | -844749.71 ± 82.8241 | 44080.6551 | 43757.6565 | +7381532.54 ± 723.78 | ±0.31 |
| ${}^{48}$Mn | 48 | 23 | 65.2671 | -835666.06 ± 16.8717 | 45014.3149 | 44682.4203 | +7427854.72 ± 149.91 | ±0.31 |
| ${}^{49}$Mn | 49 | 24 | 71.1542 | -827945.29 ± 5.3555 | 45947.9931 | 45605.5912 | +7507894.56 ± 48.55 | ±0.32 |
| ${}^{50}$Mn | 50 | 25 | 77.0237 | -819461.86 ± 0.2696 | 46881.6890 | 46532.0783 | +7513327.65 ± 2.46 | ±0.33 |
| ${}^{51}$Mn | 51 | 26 | 82.8763 | -811782.35 ± 0.6949 | 47815.4019 | 47457.9561 | +7531841.61 ± 6.40 | ±0.33 |
| ${}^{52}$Mn | 52 | 27 | 88.7127 | -803237.15 ± 0.2883 | 48749.1309 | 48386.9820 | +7484427.81 ± 2.66 | ±0.34 |
| ${}^{53}$Mn | 53 | 28 | 94.5336 | -795784.64 ± 0.7442 | 49682.8754 | 49314.4971 | +7469978.96 ± 7.01 | ±0.35 |
| ${}^{54}$Mn | 54 | 29 | 100.3397 | -787348.73 ± 2.1286 | 50616.6348 | 50245.1234 | +7393980.32 ± 20.02 | ±0.35 |
| ${}^{55}$Mn | 55 | 30 | 106.1314 | -779845.26 ± 0.5362 | 51550.4085 | 51174.4632 | +7346346.46 ± 5.08 | ±0.36 |
| ${}^{56}$Mn | 56 | 31 | 111.9094 | -771308.61 ± 0.5951 | 52484.1959 | 52106.7581 | +7243547.36 ± 5.61 | ±0.36 |
| ${}^{57}$Mn | 57 | 32 | 117.6742 | -763702.94 ± 3.0217 | 53417.9965 | 53037.6776 | +7170730.38 ± 28.36 | ±0.37 |
| ${}^{58}$Mn | 58 | 33 | 123.4263 | -755303.26 ± 5.3584 | 54351.8098 | 53970.8304 | +7058986.60 ± 50.05 | ±0.37 |
| ${}^{59}$Mn | 59 | 34 | 129.1663 | -747808.07 ± 4.5502 | 55285.6353 | 54902.6268 | +6976142.31 ± 42.42 | ±0.38 |
| ${}^{60}$Mn | 60 | 35 | 134.8944 | -739429.33 ± 4.4969 | 56219.4726 | 55836.6783 | +6855607.12 ± 41.71 | ±0.38 |
| ${}^{61}$Mn | 61 | 36 | 140.6112 | -731931.11 ± 4.4424 | 57153.3212 | 56769.3982 | +6762851.78 ± 41.02 | ±0.39 |
| ${}^{62}$Mn | 62 | 37 | 146.3171 | -723610.37 ± 12.3558 | 58087.1808 | 57704.1105 | +6638527.18 ± 113.37 | ±0.39 |
| ${}^{63}$Mn | 63 | 38 | 152.0124 | -716300.25 ± 6.9488 | 59021.0509 | 58637.2415 | +6545488.62 ± 63.54 | ±0.40 |
| ${}^{64}$Mn | 64 | 39 | 157.6975 | -707964.65 ± 6.5541 | 59954.9312 | 59572.6336 | +6417335.13 ± 59.42 | ±0.40 |
| ${}^{65}$Mn | 65 | 40 | 163.3729 | -700806.62 ± 6.8209 | 60888.8213 | 60506.1494 | +6324512.07 ± 61.58 | ±0.40 |
| ${}^{66}$Mn | 66 | 41 | 169.0387 | -692600.39 ± 20.3317 | 61822.7209 | 61441.8605 | +6198712.67 ± 181.93 | ±0.41 |
| ${}^{67}$Mn | 67 | 42 | 174.6953 | -685135.62 ± 362.2751 | 62756.6297 | 62376.5246 | +6093720.69 ± 3210.68 | ±0.41 |
| ${}^{68}$Mn | 68 | 43 | 180.3430 | -676927.44 ± 487.2701 | 63690.5474 | 63312.6790 | +5968290.37 ± 4737.46 | ±0.41 |
| ${}^{69}$Mn | 69 | 44 | 185.9821 | -669479.74 ± 735.7449 | 64624.4737 | 64247.7332 | +5863871.99 ± 6219.85 | ±0.42 |
| ${}^{70}$Mn | 70 | 45 | 191.6129 | -661389.54 ± 865.9080 | 65558.4083 | 65184.1372 | +5741751.37 ± 7673.84 | ±0.42 |
| ${}^{71}$Mn | 71 | 46 | 197.2356 | -654051.52 ± 871.7310 | 66492.3511 | 66119.4616 | +5639631.60 ± 7565.28 | ±0.42 |
| ${}^{72}$Mn | 72 | 47 | 202.8505 | -645836.82 ± 1005.6568 | 67426.3016 | 67056.4059 | +5516186.67 ± 8945.93 | ±0.43 |
| ${}^{73}$Mn | 73 | 48 | 208.4578 | -638304.42 ± 1013.2996 | 68360.2597 | 67992.3693 | +5410759.27 ± 8822.79 | ±0.43 |

### Iron (Z = 26)

_32 of 32 isotopes with a framework prediction; 32 of 32 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{45}$Fe | 45 | 19 | 35.1906 | -892860.15 ± 822.0304 | 42224.9127 | 41931.6421 | +6994017.13 ± 6753.23 | ±0.28 |
| ${}^{46}$Fe | 46 | 20 | 41.2011 | -882194.33 ± 920.6892 | 43158.4676 | 42849.9388 | +7200216.88 ± 6999.80 | ±0.28 |
| ${}^{47}$Fe | 47 | 21 | 47.1896 | -871112.40 ± 1412.0668 | 44092.0446 | 43773.0932 | +7286470.23 ± 11427.39 | ±0.29 |
| ${}^{48}$Fe | 48 | 22 | 53.1571 | -861962.13 ± 239.4697 | 45025.6425 | 44693.7084 | +7426863.65 ± 2063.33 | ±0.30 |
| ${}^{49}$Fe | 49 | 23 | 59.1046 | -852203.24 ± 60.5662 | 45959.2605 | 45618.4604 | +7470662.23 ± 530.90 | ±0.31 |
| ${}^{50}$Fe | 50 | 24 | 65.0328 | -844307.84 ± 20.0742 | 46892.8976 | 46540.2287 | +7577721.51 ± 180.13 | ±0.31 |
| ${}^{51}$Fe | 51 | 25 | 70.9427 | -835584.84 ± 3.2386 | 47826.5531 | 47466.0101 | +7595814.84 ± 29.46 | ±0.32 |
| ${}^{52}$Fe | 52 | 26 | 76.8351 | -828378.06 ± 0.4065 | 48760.2262 | 48389.3613 | +7664182.91 ± 3.70 | ±0.33 |
| ${}^{53}$Fe | 53 | 27 | 82.7106 | -819561.44 ± 3.6421 | 49693.9161 | 49318.2400 | +7617387.26 ± 33.85 | ±0.33 |
| ${}^{54}$Fe | 54 | 28 | 88.5699 | -812258.35 ± 0.7326 | 50627.6222 | 50244.4270 | +7626622.03 ± 6.82 | ±0.34 |
| ${}^{55}$Fe | 55 | 29 | 94.4137 | -803739.35 ± 0.6402 | 51561.3438 | 51174.6943 | +7555483.54 ± 6.01 | ±0.35 |
| ${}^{56}$Fe | 56 | 30 | 100.2426 | -796362.40 ± 0.5461 | 52495.0803 | 52103.0626 | +7523889.83 ± 5.13 | ±0.35 |
| ${}^{57}$Fe | 57 | 31 | 106.0572 | -787845.71 ± 0.5359 | 53428.8312 | 53034.9819 | +7426216.96 ± 5.04 | ±0.36 |
| ${}^{58}$Fe | 58 | 32 | 111.8580 | -780649.30 ± 0.6256 | 54362.5958 | 53964.5027 | +7376942.60 ± 5.85 | ±0.36 |
| ${}^{59}$Fe | 59 | 33 | 117.6456 | -772239.35 ± 0.6397 | 55296.3737 | 54897.4872 | +7266024.57 ± 6.01 | ±0.37 |
| ${}^{60}$Fe | 60 | 34 | 123.4204 | -765070.74 ± 6.4871 | 56230.1643 | 55828.2330 | +7199426.22 ± 61.00 | ±0.37 |
| ${}^{61}$Fe | 61 | 35 | 129.1829 | -756685.67 ± 4.9174 | 57163.9672 | 56762.2198 | +7077725.67 ± 45.95 | ±0.38 |
| ${}^{62}$Fe | 62 | 36 | 134.9335 | -749640.48 ± 5.1882 | 58097.7821 | 57693.7564 | +7002936.11 ± 48.44 | ±0.38 |
| ${}^{63}$Fe | 63 | 37 | 140.6726 | -741309.67 ± 7.9128 | 59031.6083 | 58628.4929 | +6875759.72 ± 73.37 | ±0.38 |
| ${}^{64}$Fe | 64 | 38 | 146.4007 | -734392.97 ± 9.1032 | 59965.4457 | 59560.6531 | +6796308.53 ± 84.23 | ±0.39 |
| ${}^{65}$Fe | 65 | 39 | 152.1181 | -726166.18 ± 9.1969 | 60899.2937 | 60495.8988 | +6668135.04 ± 84.49 | ±0.39 |
| ${}^{66}$Fe | 66 | 40 | 157.8252 | -719388.80 ± 7.2873 | 61833.1520 | 61428.5430 | +6586660.92 ± 66.72 | ±0.40 |
| ${}^{67}$Fe | 67 | 41 | 163.5224 | -711165.60 ± 6.7456 | 62767.0203 | 62364.3965 | +6455987.16 ± 61.24 | ±0.40 |
| ${}^{68}$Fe | 68 | 42 | 169.2098 | -704397.73 ± 356.3792 | 63700.8982 | 63297.7024 | +6369833.54 ± 3046.23 | ±0.40 |
| ${}^{69}$Fe | 69 | 43 | 174.8880 | -696272.22 ± 359.4967 | 64634.7855 | 64233.8940 | +6241120.63 ± 3117.84 | ±0.41 |
| ${}^{70}$Fe | 70 | 44 | 180.5571 | -689529.76 ± 481.4636 | 65568.6818 | 65167.6973 | +6153117.92 ± 4602.60 | ±0.41 |
| ${}^{71}$Fe | 71 | 45 | 186.2174 | -681508.13 ± 728.5974 | 66502.5869 | 66104.1516 | +6027386.88 ± 6045.17 | ±0.42 |
| ${}^{72}$Fe | 72 | 46 | 191.8693 | -674819.89 ± 854.1794 | 67436.5005 | 67038.3256 | +5939510.66 ± 7461.59 | ±0.42 |
| ${}^{73}$Fe | 73 | 47 | 197.5129 | -666832.14 ± 861.9628 | 68370.4223 | 67975.0799 | +5815990.10 ± 7358.76 | ±0.42 |
| ${}^{74}$Fe | 74 | 48 | 203.1486 | -660072.96 ± 866.7657 | 69304.3520 | 68909.9041 | +5724111.41 ± 7258.93 | ±0.42 |
| ${}^{75}$Fe | 75 | 49 | 208.7765 | -651865.16 ± 1000.5003 | 70238.2895 | 69847.3579 | +5596942.96 ± 8588.47 | ±0.43 |
| ${}^{76}$Fe | 76 | 50 | 214.3969 | -644843.09 ± 1007.1761 | 71172.2346 | 70782.9617 | +5499527.57 ± 8474.95 | ±0.43 |

### Cobalt (Z = 27)

_32 of 32 isotopes with a framework prediction; 32 of 32 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{47}$Co | 47 | 20 | 34.6317 | -900372.48 ± 1757.7069 | 44103.8201 | 43790.8428 | +7147094.21 ± 13698.80 | ±0.28 |
| ${}^{48}$Co | 48 | 21 | 40.6636 | -888458.36 ± 1316.6557 | 45037.3536 | 44713.4468 | +7244059.79 ± 11187.07 | ±0.29 |
| ${}^{49}$Co | 49 | 22 | 46.6738 | -878504.26 ± 1275.5102 | 45970.9089 | 45633.4313 | +7395401.76 ± 10961.53 | ±0.29 |
| ${}^{50}$Co | 50 | 23 | 52.6632 | -868352.44 ± 314.3499 | 46904.4849 | 46557.1158 | +7461138.73 ± 2701.02 | ±0.30 |
| ${}^{51}$Co | 51 | 24 | 58.6328 | -859681.84 ± 115.9246 | 47838.0807 | 47478.8571 | +7565969.87 ± 1020.20 | ±0.31 |
| ${}^{52}$Co | 52 | 25 | 64.5833 | -850822.42 ± 12.2034 | 48771.6956 | 48403.3494 | +7609932.45 ± 109.10 | ±0.32 |
| ${}^{53}$Co | 53 | 26 | 70.5156 | -843060.02 ± 3.8454 | 49705.3288 | 49326.5281 | +7679450.57 ± 35.01 | ±0.32 |
| ${}^{54}$Co | 54 | 27 | 76.4304 | -834829.96 ± 0.7702 | 50638.9794 | 50252.6715 | +7687309.38 ± 7.04 | ±0.33 |
| ${}^{55}$Co | 55 | 28 | 82.3285 | -827341.80 ± 0.8536 | 51572.6468 | 51178.1457 | +7708389.05 ± 7.90 | ±0.33 |
| ${}^{56}$Co | 56 | 29 | 88.2104 | -818836.79 ± 0.9776 | 52506.3303 | 52107.6293 | +7651489.96 ± 9.12 | ±0.34 |
| ${}^{57}$Co | 57 | 30 | 94.0767 | -811199.83 ± 1.0295 | 53440.0293 | 53035.8183 | +7621473.16 ± 9.71 | ±0.35 |
| ${}^{58}$Co | 58 | 31 | 99.9282 | -802848.59 ± 2.2772 | 54373.7433 | 53966.8107 | +7540422.14 ± 21.35 | ±0.35 |
| ${}^{59}$Co | 59 | 32 | 105.7654 | -795549.09 ± 0.7641 | 55307.4715 | 54895.9223 | +7496900.47 ± 7.23 | ±0.36 |
| ${}^{60}$Co | 60 | 33 | 111.5887 | -787371.62 ± 0.7660 | 56241.2137 | 55827.9958 | +7401624.69 ± 7.22 | ±0.36 |
| ${}^{61}$Co | 61 | 34 | 117.3987 | -780203.84 ± 1.5760 | 57174.9691 | 56758.2421 | +7342139.64 ± 14.79 | ±0.37 |
| ${}^{62}$Co | 62 | 35 | 123.1958 | -772164.53 ± 34.3525 | 58108.7374 | 57691.2100 | +7237278.08 ± 321.96 | ±0.37 |
| ${}^{63}$Co | 63 | 36 | 128.9806 | -765157.33 ± 33.8159 | 59042.5180 | 58622.2770 | +7168623.69 ± 316.86 | ±0.37 |
| ${}^{64}$Co | 64 | 37 | 134.7534 | -757303.20 ± 36.0324 | 59976.3107 | 59555.8302 | +7060273.59 ± 335.90 | ±0.38 |
| ${}^{65}$Co | 65 | 38 | 140.5146 | -750283.91 ± 3.6965 | 60910.1148 | 60487.9315 | +6979628.52 ± 34.42 | ±0.38 |
| ${}^{66}$Co | 66 | 39 | 146.2647 | -742488.16 ± 24.5993 | 61843.9302 | 61422.2023 | +6866049.23 ± 227.48 | ±0.39 |
| ${}^{67}$Co | 67 | 40 | 152.0040 | -735634.53 ± 11.2098 | 62777.7563 | 62354.7832 | +6783331.05 ± 103.33 | ±0.39 |
| ${}^{68}$Co | 68 | 41 | 157.7328 | -727750.56 ± 6.6548 | 63711.5929 | 63289.9565 | +6661979.82 ± 60.96 | ±0.40 |
| ${}^{69}$Co | 69 | 42 | 163.4516 | -721159.46 ± 146.1967 | 64645.4395 | 64222.7077 | +6582279.94 ± 1334.38 | ±0.40 |
| ${}^{70}$Co | 70 | 43 | 169.1606 | -713478.46 ± 18.6147 | 65579.2960 | 65158.0623 | +6464797.97 ± 168.69 | ±0.40 |
| ${}^{71}$Co | 71 | 44 | 174.8601 | -706763.24 ± 779.8437 | 66513.1619 | 66091.7114 | +6376752.74 ± 7036.13 | ±0.41 |
| ${}^{72}$Co | 72 | 45 | 180.5504 | -699251.15 ± 479.7314 | 67447.0370 | 67027.2753 | +6262551.15 ± 4474.91 | ±0.41 |
| ${}^{73}$Co | 73 | 46 | 186.2318 | -692710.16 ± 481.8116 | 68380.9211 | 67961.1000 | +6177372.77 ± 4413.42 | ±0.41 |
| ${}^{74}$Co | 74 | 47 | 191.9046 | -685240.34 ± 606.8698 | 69314.8137 | 68897.0234 | +6063982.33 ± 5800.12 | ±0.42 |
| ${}^{75}$Co | 75 | 48 | 197.5690 | -678632.08 ± 609.9793 | 70248.7147 | 69831.4973 | +5974630.53 ± 5722.50 | ±0.42 |
| ${}^{76}$Co | 76 | 49 | 203.2252 | -671133.15 ± 860.9027 | 71182.6239 | 70767.8920 | +5860452.17 ± 7068.35 | ±0.42 |
| ${}^{77}$Co | 77 | 50 | 208.8736 | -664359.75 ± 989.8540 | 72116.5409 | 71703.1363 | +5765502.12 ± 8366.19 | ±0.43 |
| ${}^{78}$Co | 78 | 51 | 214.5143 | -656098.05 ± 1125.4220 | 73050.4656 | 72641.2198 | +5633795.75 ± 9630.24 | ±0.43 |

### Nickel (Z = 28)

_35 of 35 isotopes with a framework prediction; 35 of 35 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{48}$Ni | 48 | 20 | 27.7866 | -919999.03 ± 1243.7811 | 45049.4484 | 44729.8951 | +7144064.73 ± 9475.31 | ±0.27 |
| ${}^{49}$Ni | 49 | 21 | 33.8620 | -907240.22 ± 1610.7383 | 45982.9384 | 45651.7408 | +7254873.87 ± 13140.40 | ±0.28 |
| ${}^{50}$Ni | 50 | 22 | 39.9149 | -896351.77 ± 1298.3641 | 46916.4508 | 46571.2456 | +7412411.26 ± 10740.80 | ±0.29 |
| ${}^{51}$Ni | 51 | 23 | 45.9465 | -885525.89 ± 1270.6480 | 47849.9847 | 47494.5491 | +7483714.24 ± 10531.99 | ±0.30 |
| ${}^{52}$Ni | 52 | 24 | 51.9575 | -876398.44 ± 197.2192 | 48783.5391 | 48415.1335 | +7609306.75 ± 1712.34 | ±0.30 |
| ${}^{53}$Ni | 53 | 25 | 57.9488 | -866938.80 ± 57.7456 | 49717.1132 | 49339.5567 | +7652208.20 ± 509.74 | ±0.31 |
| ${}^{54}$Ni | 54 | 26 | 63.9213 | -858963.10 ± 10.2704 | 50650.7062 | 50261.4033 | +7745563.74 ± 92.66 | ±0.32 |
| ${}^{55}$Ni | 55 | 27 | 69.8756 | -850486.33 ± 1.5064 | 51584.3173 | 51186.8397 | +7765228.86 ± 13.78 | ±0.32 |
| ${}^{56}$Ni | 56 | 28 | 75.8126 | -843361.09 ± 0.8215 | 52517.9457 | 52109.7622 | +7833150.07 ± 7.65 | ±0.33 |
| ${}^{57}$Ni | 57 | 29 | 81.7328 | -834630.49 ± 1.1417 | 53451.5909 | 53039.0800 | +7777491.58 ± 10.68 | ±0.33 |
| ${}^{58}$Ni | 58 | 30 | 87.6369 | -826961.68 ± 0.6871 | 54385.2522 | 53966.4291 | +7760807.99 ± 6.46 | ±0.34 |
| ${}^{59}$Ni | 59 | 31 | 93.5256 | -818558.62 ± 0.6868 | 55318.9290 | 54896.9953 | +7685916.58 ± 6.38 | ±0.34 |
| ${}^{60}$Ni | 60 | 32 | 99.3993 | -811331.60 ± 0.6719 | 56252.6207 | 55825.1730 | +7656899.13 ± 6.31 | ±0.35 |
| ${}^{61}$Ni | 61 | 33 | 105.2587 | -803132.17 ± 0.6617 | 57186.3268 | 56756.9183 | +7565746.49 ± 6.25 | ±0.35 |
| ${}^{62}$Ni | 62 | 34 | 111.1042 | -796237.23 ± 0.7846 | 58120.0467 | 57685.8880 | +7526254.48 ± 7.35 | ±0.36 |
| ${}^{63}$Ni | 63 | 35 | 116.9363 | -788197.28 ± 0.7759 | 59053.7799 | 58618.6156 | +7423653.64 ± 7.26 | ±0.36 |
| ${}^{64}$Ni | 64 | 36 | 122.7556 | -781479.49 ± 0.8203 | 59987.5261 | 59548.5236 | +7372181.41 ± 7.77 | ±0.37 |
| ${}^{65}$Ni | 65 | 37 | 128.5624 | -773600.34 ± 0.8470 | 60921.2848 | 60481.9909 | +7263216.94 ± 7.98 | ±0.37 |
| ${}^{66}$Ni | 66 | 38 | 134.3571 | -767067.74 ± 2.4258 | 61855.0555 | 61412.6046 | +7204561.71 ± 22.75 | ±0.38 |
| ${}^{67}$Ni | 67 | 39 | 140.1402 | -759463.60 ± 4.9564 | 62788.8378 | 62346.3623 | +7097054.30 ± 46.32 | ±0.38 |
| ${}^{68}$Ni | 68 | 40 | 145.9120 | -752862.29 ± 5.0446 | 63722.6314 | 63278.1352 | +7024482.25 ± 47.11 | ±0.39 |
| ${}^{69}$Ni | 69 | 41 | 151.6730 | -745084.85 ± 6.2622 | 64656.4359 | 64213.1145 | +6903906.73 ± 58.03 | ±0.39 |
| ${}^{70}$Ni | 70 | 42 | 157.4233 | -738629.87 ± 3.5564 | 65590.2509 | 65145.3734 | +6828996.06 ± 32.90 | ±0.39 |
| ${}^{71}$Ni | 71 | 43 | 163.1635 | -731003.68 ± 3.6872 | 66524.0761 | 66080.6751 | +6709995.25 ± 33.85 | ±0.40 |
| ${}^{72}$Ni | 72 | 44 | 168.8938 | -724684.44 ± 3.6501 | 67457.9113 | 67013.3494 | +6633930.49 ± 33.37 | ±0.40 |
| ${}^{73}$Ni | 73 | 45 | 174.6144 | -717181.74 ± 3.9254 | 68391.7561 | 67948.9614 | +6516577.09 ± 35.66 | ±0.40 |
| ${}^{74}$Ni | 74 | 46 | 180.3258 | -711035.80 ± 355.7453 | 69325.6101 | 68881.8633 | +6442143.14 ± 2907.46 | ±0.41 |
| ${}^{75}$Ni | 75 | 47 | 186.0281 | -703623.50 ± 358.4658 | 70259.4732 | 69817.8174 | +6325832.58 ± 2868.48 | ±0.41 |
| ${}^{76}$Ni | 76 | 48 | 191.7217 | -697450.99 ± 479.7314 | 71193.3451 | 70751.3617 | +6246994.50 ± 4239.37 | ±0.41 |
| ${}^{77}$Ni | 77 | 49 | 197.4067 | -690072.09 ± 604.4487 | 72127.2255 | 71687.6959 | +6131172.06 ± 5574.33 | ±0.42 |
| ${}^{78}$Ni | 78 | 50 | 203.0835 | -683948.21 ± 606.9434 | 73061.1141 | 72621.6603 | +6051277.47 ± 5502.64 | ±0.42 |
| ${}^{79}$Ni | 79 | 51 | 208.7522 | -675775.03 ± 736.1963 | 73995.0108 | 73559.8742 | +5915406.99 ± 6800.07 | ±0.42 |
| ${}^{80}$Ni | 80 | 52 | 214.4132 | -668624.53 ± 865.4797 | 74928.9153 | 74496.2885 | +5807360.81 ± 8052.51 | ±0.43 |
| ${}^{81}$Ni | 81 | 53 | 220.0665 | -660391.17 ± 1125.0000 | 75862.8274 | 75434.9327 | +5672367.42 ± 9273.58 | ±0.43 |
| ${}^{82}$Ni | 82 | 54 | 225.7125 | -653107.60 ± 1260.2394 | 76796.7468 | 76371.7969 | +5564226.21 ± 10477.08 | ±0.43 |

### Copper (Z = 29)

_33 of 33 isotopes with a framework prediction; 33 of 33 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{52}$Cu | 52 | 23 | 38.9576 | -902335.58 ± 1564.3332 | 48795.7567 | 48435.8136 | +7431341.96 ± 12385.10 | ±0.29 |
| ${}^{53}$Cu | 53 | 24 | 45.0101 | -892377.66 ± 1140.5399 | 49729.2696 | 49356.0478 | +7561823.62 ± 10134.77 | ±0.30 |
| ${}^{54}$Cu | 54 | 25 | 51.0424 | -882507.15 ± 870.1057 | 50662.8027 | 50279.4417 | +7624608.16 ± 7947.80 | ±0.30 |
| ${}^{55}$Cu | 55 | 26 | 57.0552 | -874014.12 ± 343.5027 | 51596.3553 | 51200.5403 | +7730681.08 ± 3038.24 | ±0.31 |
| ${}^{56}$Cu | 56 | 27 | 63.0493 | -865260.76 ± 13.6668 | 52529.9267 | 52125.0401 | +7767603.30 ± 122.66 | ±0.32 |
| ${}^{57}$Cu | 57 | 28 | 69.0253 | -857587.54 ± 1.0349 | 53463.5161 | 53047.8549 | +7835588.58 ± 9.43 | ±0.32 |
| ${}^{58}$Cu | 58 | 29 | 74.9841 | -849161.84 ± 1.1317 | 54397.1227 | 53974.9902 | +7820891.87 ± 10.42 | ±0.33 |
| ${}^{59}$Cu | 59 | 30 | 80.9262 | -841283.26 ± 1.0414 | 55330.7460 | 54901.7937 | +7813085.07 ± 9.60 | ±0.33 |
| ${}^{60}$Cu | 60 | 31 | 86.8523 | -832955.96 ± 3.1042 | 56264.3854 | 55831.3010 | +7757018.85 ± 28.88 | ±0.34 |
| ${}^{61}$Cu | 61 | 32 | 92.7629 | -825517.77 ± 1.7899 | 57198.0402 | 56759.1563 | +7732390.76 ± 16.74 | ±0.34 |
| ${}^{62}$Cu | 62 | 33 | 98.6585 | -817475.17 ± 1.1815 | 58131.7100 | 57689.8469 | +7659286.83 ± 11.03 | ±0.35 |
| ${}^{63}$Cu | 63 | 34 | 104.5399 | -810404.92 ± 0.7770 | 59065.3941 | 58618.5487 | +7622935.54 ± 7.26 | ±0.35 |
| ${}^{64}$Cu | 64 | 35 | 110.4073 | -802597.64 ± 0.7667 | 59999.0921 | 59550.1982 | +7538074.96 ± 7.16 | ±0.36 |
| ${}^{65}$Cu | 65 | 36 | 116.2613 | -795750.18 ± 1.1305 | 60932.8035 | 60479.8531 | +7489277.66 ± 10.63 | ±0.36 |
| ${}^{66}$Cu | 66 | 37 | 122.1024 | -788118.69 ± 1.1224 | 61866.5278 | 61412.3526 | +7395503.61 ± 10.56 | ±0.37 |
| ${}^{67}$Cu | 67 | 38 | 127.9309 | -781467.75 ± 1.5222 | 62800.2647 | 62342.7854 | +7338127.59 ± 14.30 | ±0.37 |
| ${}^{68}$Cu | 68 | 39 | 133.7474 | -773971.80 ± 2.6776 | 63734.0137 | 63276.0320 | +7237838.35 ± 25.03 | ±0.38 |
| ${}^{69}$Cu | 69 | 40 | 139.5521 | -767401.26 ± 2.3346 | 64667.7744 | 64207.3569 | +7170790.08 ± 21.76 | ±0.38 |
| ${}^{70}$Cu | 70 | 41 | 145.3454 | -759871.00 ± 1.7926 | 65601.5465 | 65141.6109 | +7060549.92 ± 16.60 | ±0.38 |
| ${}^{71}$Cu | 71 | 42 | 151.1278 | -753496.85 ± 2.4320 | 66535.3295 | 66073.3702 | +6991610.97 ± 22.56 | ±0.39 |
| ${}^{72}$Cu | 72 | 43 | 156.8995 | -746211.69 ± 2.2594 | 67469.1232 | 67007.7925 | +6884733.19 ± 20.85 | ±0.39 |
| ${}^{73}$Cu | 73 | 44 | 162.6609 | -739952.93 ± 3.1044 | 68402.9273 | 67940.0821 | +6812549.00 ± 28.57 | ±0.40 |
| ${}^{74}$Cu | 74 | 45 | 168.4123 | -732931.44 ± 9.7517 | 69336.7413 | 68874.5575 | +6710516.39 ± 89.26 | ±0.40 |
| ${}^{75}$Cu | 75 | 46 | 174.1539 | -726659.13 ± 1.1301 | 70270.5651 | 69807.5876 | +6632194.64 ± 10.27 | ±0.40 |
| ${}^{76}$Cu | 76 | 47 | 179.8862 | -719678.47 ± 1.4212 | 71204.3983 | 70742.5703 | +6528289.82 ± 12.90 | ±0.41 |
| ${}^{77}$Cu | 77 | 48 | 185.6093 | -713418.36 ± 1.8665 | 72138.2406 | 71676.1832 | +6446457.11 ± 16.89 | ±0.41 |
| ${}^{78}$Cu | 78 | 49 | 191.3234 | -706407.94 ± 20.4556 | 73072.0918 | 72611.7506 | +6339762.03 ± 183.60 | ±0.41 |
| ${}^{79}$Cu | 79 | 50 | 197.0290 | -700269.63 ± 159.7056 | 74005.9517 | 73545.6262 | +6259047.35 ± 1427.40 | ±0.41 |
| ${}^{80}$Cu | 80 | 51 | 202.7261 | -692690.19 ± 485.0837 | 74939.8200 | 74482.8489 | +6135253.14 ± 4026.98 | ±0.42 |
| ${}^{81}$Cu | 81 | 52 | 208.4151 | -685641.28 ± 488.6988 | 75873.6964 | 75419.1122 | +6027440.61 ± 3976.99 | ±0.42 |
| ${}^{82}$Cu | 82 | 53 | 214.0962 | -677981.16 ± 616.6749 | 76807.5808 | 76356.7868 | +5903784.79 ± 5233.47 | ±0.42 |
| ${}^{83}$Cu | 83 | 54 | 219.7695 | -670832.31 ± 745.8976 | 77741.4729 | 77293.6202 | +5794174.47 ± 6471.59 | ±0.43 |
| ${}^{84}$Cu | 84 | 55 | 225.4353 | -663056.74 ± 753.2957 | 78675.3726 | 78231.7847 | +5670173.88 ± 6393.98 | ±0.43 |

### Zinc (Z = 30)

_33 of 33 isotopes with a framework prediction; 33 of 33 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{54}$Zn | 54 | 24 | 37.7939 | -909598.76 ± 516.6624 | 50675.2689 | 50294.9799 | +7561172.27 ± 4296.78 | ±0.29 |
| ${}^{55}$Zn | 55 | 25 | 43.8672 | -899090.89 ± 885.6275 | 51608.7610 | 51217.9061 | +7631215.20 ± 7802.17 | ±0.30 |
| ${}^{56}$Zn | 56 | 26 | 49.9205 | -890027.53 ± 863.5579 | 52542.2732 | 52138.2801 | +7748493.17 ± 7664.44 | ±0.30 |
| ${}^{57}$Zn | 57 | 27 | 55.9544 | -880736.70 ± 485.9677 | 53475.8047 | 53062.6138 | +7786855.03 ± 3774.24 | ±0.31 |
| ${}^{58}$Zn | 58 | 28 | 61.9698 | -872742.85 ± 102.6805 | 54409.3547 | 53984.3591 | +7872568.72 ± 926.21 | ±0.32 |
| ${}^{59}$Zn | 59 | 29 | 67.9673 | -864052.72 ± 1.5223 | 55342.9227 | 54910.9364 | +7867034.22 ± 13.81 | ±0.32 |
| ${}^{60}$Zn | 60 | 30 | 73.9475 | -856407.87 ± 1.0602 | 56276.5078 | 55835.4718 | +7898850.69 ± 9.81 | ±0.33 |
| ${}^{61}$Zn | 61 | 31 | 79.9112 | -847854.51 ± 30.2660 | 57210.1095 | 56764.7914 | +7844970.74 ± 280.08 | ±0.33 |
| ${}^{62}$Zn | 62 | 32 | 85.8589 | -840446.38 ± 1.1406 | 58143.7273 | 57691.4663 | +7839304.00 ± 10.66 | ±0.34 |
| ${}^{63}$Zn | 63 | 33 | 91.7912 | -832264.07 ± 2.8551 | 59077.3605 | 58621.9151 | +7769199.38 ± 26.60 | ±0.34 |
| ${}^{64}$Zn | 64 | 34 | 97.7085 | -825239.01 ± 1.1561 | 60011.0085 | 59549.6186 | +7747990.74 ± 10.79 | ±0.35 |
| ${}^{65}$Zn | 65 | 35 | 103.6115 | -817288.60 ± 1.1348 | 60944.6710 | 60481.2047 | +7662979.71 ± 10.67 | ±0.35 |
| ${}^{66}$Zn | 66 | 36 | 109.5006 | -810597.16 ± 1.2900 | 61878.3473 | 61409.7116 | +7631296.07 ± 12.10 | ±0.36 |
| ${}^{67}$Zn | 67 | 37 | 115.3762 | -802839.18 ± 1.2938 | 62812.0371 | 62342.2246 | +7536024.29 ± 12.10 | ±0.36 |
| ${}^{68}$Zn | 68 | 38 | 121.2388 | -796369.47 ± 1.3134 | 63745.7399 | 63271.5919 | +7493852.45 ± 12.29 | ±0.37 |
| ${}^{69}$Zn | 69 | 39 | 127.0889 | -788842.71 ± 1.3184 | 64679.4552 | 64204.6753 | +7394788.28 ± 12.38 | ±0.37 |
| ${}^{70}$Zn | 70 | 40 | 132.9268 | -782474.70 ± 3.1387 | 65613.1828 | 65135.0225 | +7341062.21 ± 29.43 | ±0.37 |
| ${}^{71}$Zn | 71 | 41 | 138.7529 | -775088.42 ± 4.3043 | 66546.9221 | 66068.7526 | +7237453.34 ± 40.17 | ±0.38 |
| ${}^{72}$Zn | 72 | 42 | 144.5676 | -768991.28 ± 3.4285 | 67480.6728 | 66999.4300 | +7182790.56 ± 31.98 | ±0.38 |
| ${}^{73}$Zn | 73 | 43 | 150.3712 | -761818.17 ± 2.9485 | 68414.4347 | 67933.4762 | +7079845.54 ± 27.42 | ±0.39 |
| ${}^{74}$Zn | 74 | 44 | 156.1640 | -755827.35 ± 3.9339 | 69348.2073 | 68864.8070 | +7019554.99 ± 36.52 | ±0.39 |
| ${}^{75}$Zn | 75 | 45 | 161.9464 | -748701.06 ± 3.0375 | 70281.9903 | 69799.4989 | +6912533.71 ± 28.03 | ±0.39 |
| ${}^{76}$Zn | 76 | 46 | 167.7187 | -742862.37 ± 2.2372 | 71215.7834 | 70731.2489 | +6850359.84 ± 20.57 | ±0.40 |
| ${}^{77}$Zn | 77 | 47 | 173.4812 | -735873.17 ± 3.0012 | 72149.5863 | 71666.2568 | +6744171.38 ± 27.52 | ±0.40 |
| ${}^{78}$Zn | 78 | 48 | 179.2342 | -729896.40 ± 2.9269 | 73083.3988 | 72599.0568 | +6671463.09 ± 26.76 | ±0.40 |
| ${}^{79}$Zn | 79 | 49 | 184.9778 | -722919.49 ± 3.3370 | 74017.2205 | 73534.6019 | +6563150.08 ± 30.25 | ±0.41 |
| ${}^{80}$Zn | 80 | 50 | 190.7125 | -716994.89 ± 3.8345 | 74951.0513 | 74467.8797 | +6488322.19 ± 34.70 | ±0.41 |
| ${}^{81}$Zn | 81 | 51 | 196.4384 | -709627.97 ± 7.4354 | 75884.8908 | 75404.8227 | +6366543.14 ± 66.71 | ±0.41 |
| ${}^{82}$Zn | 82 | 52 | 202.1558 | -703014.11 ± 4.5175 | 76818.7388 | 76340.2025 | +6268470.13 ± 40.27 | ±0.42 |
| ${}^{83}$Zn | 83 | 53 | 207.8649 | -695551.12 ± 486.2631 | 77752.5951 | 77277.7205 | +6145039.16 ± 3881.34 | ±0.42 |
| ${}^{84}$Zn | 84 | 54 | 213.5659 | -688844.49 ± 611.9202 | 78686.4595 | 78213.6746 | +6044785.87 ± 5109.22 | ±0.42 |
| ${}^{85}$Zn | 85 | 55 | 219.2591 | -681147.22 ± 741.6564 | 79620.3318 | 79151.8988 | +5918152.61 ± 6319.65 | ±0.42 |
| ${}^{86}$Zn | 86 | 56 | 224.9446 | -674348.20 ± 747.0120 | 80554.2117 | 80088.4313 | +5815825.75 ± 6245.75 | ±0.43 |

### Gallium (Z = 31)

_33 of 33 isotopes with a framework prediction; 33 of 33 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{56}$Ga | 56 | 25 | 36.4261 | -915600.50 ± 1167.7696 | 52554.9852 | 52159.8302 | +7575848.51 ± 9589.99 | ±0.29 |
| ${}^{57}$Ga | 57 | 26 | 42.5200 | -905764.96 ± 884.2850 | 53488.4567 | 53079.7542 | +7699782.15 ± 7528.50 | ±0.30 |
| ${}^{58}$Ga | 58 | 27 | 48.5939 | -896038.42 ± 620.4244 | 54421.9482 | 54003.1182 | +7755663.16 ± 5554.14 | ±0.30 |
| ${}^{59}$Ga | 59 | 28 | 54.6487 | -887481.79 ± 364.4315 | 55355.4588 | 54924.3920 | +7848368.29 ± 3103.60 | ±0.31 |
| ${}^{60}$Ga | 60 | 29 | 60.6851 | -878537.44 ± 360.2738 | 56288.9879 | 55850.0559 | +7859115.09 ± 3585.87 | ±0.32 |
| ${}^{61}$Ga | 61 | 30 | 66.7037 | -870536.57 ± 73.7353 | 57222.5347 | 56774.0057 | +7900253.11 ± 669.19 | ±0.32 |
| ${}^{62}$Ga | 62 | 31 | 72.7052 | -862341.35 ± 1.2091 | 58156.0986 | 57700.6474 | +7893346.35 ± 11.04 | ±0.33 |
| ${}^{63}$Ga | 63 | 32 | 78.6902 | -854489.54 ± 2.4115 | 59089.6790 | 58627.5814 | +7881914.97 ± 22.24 | ±0.33 |
| ${}^{64}$Ga | 64 | 33 | 84.6593 | -846393.70 ± 2.5895 | 60023.2754 | 59556.7898 | +7832618.63 ± 23.98 | ±0.34 |
| ${}^{65}$Ga | 65 | 34 | 90.6129 | -839065.02 ± 1.4084 | 60956.8872 | 60484.4593 | +7810733.02 ± 13.08 | ±0.34 |
| ${}^{66}$Ga | 66 | 35 | 96.5517 | -831255.90 ± 1.9148 | 61890.5139 | 61414.8871 | +7744486.50 ± 17.78 | ±0.35 |
| ${}^{67}$Ga | 67 | 36 | 102.4760 | -824348.29 ± 2.0212 | 62824.1549 | 62343.2258 | +7714216.38 ± 18.86 | ±0.35 |
| ${}^{68}$Ga | 68 | 37 | 108.3865 | -816816.59 ± 2.4135 | 63757.8099 | 63274.5130 | +7638097.30 ± 22.60 | ±0.36 |
| ${}^{69}$Ga | 69 | 38 | 114.2835 | -810159.04 ± 1.9944 | 64691.4783 | 64203.7653 | +7596329.66 ± 18.64 | ±0.36 |
| ${}^{70}$Ga | 70 | 39 | 120.1675 | -802890.94 ± 1.9749 | 65625.1598 | 65135.6771 | +7514816.28 ± 18.43 | ±0.37 |
| ${}^{71}$Ga | 71 | 40 | 126.0388 | -796366.70 ± 1.3077 | 66558.8538 | 66065.9422 | +7460903.11 ± 12.27 | ±0.37 |
| ${}^{72}$Ga | 72 | 41 | 131.8979 | -789122.03 ± 1.3123 | 67492.5601 | 66998.9872 | +7366871.86 ± 12.21 | ±0.37 |
| ${}^{73}$Ga | 73 | 42 | 137.7452 | -782959.76 ± 2.6455 | 68426.2783 | 67929.3702 | +7315069.61 ± 24.68 | ±0.38 |
| ${}^{74}$Ga | 74 | 43 | 143.5810 | -776030.74 ± 4.6750 | 69360.0080 | 68862.5140 | +7224451.75 ± 43.48 | ±0.38 |
| ${}^{75}$Ga | 75 | 44 | 149.4056 | -769988.43 ± 1.0276 | 70293.7488 | 69793.5971 | +7166153.56 ± 9.61 | ±0.38 |
| ${}^{76}$Ga | 76 | 45 | 155.2193 | -763191.67 ± 2.9799 | 71227.5004 | 70727.2552 | +7072877.07 ± 27.66 | ±0.39 |
| ${}^{77}$Ga | 77 | 46 | 161.0226 | -757214.91 ± 3.6571 | 72161.2626 | 71659.0536 | +7008311.02 ± 33.80 | ±0.39 |
| ${}^{78}$Ga | 78 | 47 | 166.8157 | -750654.48 ± 1.5740 | 73095.0349 | 72592.8360 | +6918023.26 ± 14.46 | ±0.39 |
| ${}^{79}$Ga | 79 | 48 | 172.5988 | -744649.76 ± 1.7882 | 74028.8172 | 73525.4858 | +6845672.23 ± 16.42 | ±0.40 |
| ${}^{80}$Ga | 80 | 49 | 178.3723 | -737948.42 ± 4.2428 | 74962.6091 | 74460.3046 | +6745936.92 ± 38.82 | ±0.40 |
| ${}^{81}$Ga | 81 | 50 | 184.1364 | -732029.53 ± 4.7505 | 75896.4104 | 75393.3944 | +6671884.27 ± 43.28 | ±0.40 |
| ${}^{82}$Ga | 82 | 51 | 189.8914 | -725004.67 ± 3.5150 | 76830.2209 | 76329.5858 | +6558860.19 ± 31.78 | ±0.41 |
| ${}^{83}$Ga | 83 | 52 | 195.6376 | -718476.21 ± 3.7623 | 77764.0402 | 77264.7535 | +6462023.74 ± 33.80 | ±0.41 |
| ${}^{84}$Ga | 84 | 53 | 201.3751 | -711427.62 ± 42.7203 | 78697.8681 | 78201.4106 | +6348446.88 ± 381.17 | ±0.41 |
| ${}^{85}$Ga | 85 | 54 | 207.1042 | -704792.00 ± 53.1164 | 79631.7044 | 79137.2548 | +6248001.08 ± 470.82 | ±0.42 |
| ${}^{86}$Ga | 86 | 55 | 212.8251 | -697542.16 ± 611.0975 | 80565.5489 | 80074.7328 | +6129475.98 ± 4990.48 | ±0.42 |
| ${}^{87}$Ga | 87 | 56 | 218.5380 | -690801.22 ± 738.5524 | 81499.4014 | 81011.1172 | +6027372.73 ± 6174.61 | ±0.42 |
| ${}^{88}$Ga | 88 | 57 | 224.2431 | -683451.24 ± 745.3416 | 82433.2617 | 81949.0908 | +5908191.11 ± 6103.94 | ±0.42 |

### Germanium (Z = 32)

_33 of 33 isotopes with a framework prediction; 33 of 33 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{58}$Ge | 58 | 26 | 34.8566 | -922654.36 ± 1158.3012 | 54434.9032 | 54019.0784 | +7697739.31 ± 9259.92 | ±0.29 |
| ${}^{59}$Ge | 59 | 27 | 40.9707 | -912365.23 ± 883.3922 | 55368.3546 | 54941.7820 | +7764082.76 ± 7273.35 | ±0.30 |
| ${}^{60}$Ge | 60 | 28 | 47.0650 | -903313.53 ± 616.2948 | 56301.8256 | 55862.1159 | +7871340.02 ± 5369.31 | ±0.31 |
| ${}^{61}$Ge | 61 | 29 | 53.1405 | -893955.57 ± 608.6427 | 57235.3156 | 56787.3504 | +7888469.00 ± 5281.83 | ±0.31 |
| ${}^{62}$Ge | 62 | 30 | 59.1976 | -885611.63 ± 239.6070 | 58168.8239 | 57710.4946 | +7941871.96 ± 2421.12 | ±0.32 |
| ${}^{63}$Ge | 63 | 31 | 65.2371 | -876999.18 ± 70.2482 | 59102.3499 | 58637.2073 | +7932549.55 ± 635.43 | ±0.32 |
| ${}^{64}$Ge | 64 | 32 | 71.2595 | -869450.93 ± 6.8239 | 60035.8928 | 59561.3071 | +7968020.20 ± 62.56 | ±0.33 |
| ${}^{65}$Ge | 65 | 33 | 77.2655 | -861052.91 ± 3.8924 | 60969.4522 | 60490.6385 | +7915501.31 ± 35.77 | ±0.33 |
| ${}^{66}$Ge | 66 | 34 | 83.2557 | -853752.44 ± 4.2201 | 61903.0275 | 61417.0038 | +7913504.65 ± 39.08 | ±0.34 |
| ${}^{67}$Ge | 67 | 35 | 89.2304 | -845733.40 ± 7.4713 | 62836.6182 | 62347.4312 | +7846144.96 ± 69.26 | ±0.34 |
| ${}^{68}$Ge | 68 | 36 | 95.1903 | -838877.14 ± 3.1767 | 63770.2237 | 63274.6203 | +7832579.32 ± 29.65 | ±0.35 |
| ${}^{69}$Ge | 69 | 37 | 101.1358 | -831155.07 ± 2.2002 | 64703.8436 | 64205.9925 | +7753967.08 ± 20.51 | ±0.35 |
| ${}^{70}$Ge | 70 | 38 | 107.0674 | -824628.87 ± 1.3415 | 65637.4775 | 65134.0252 | +7729481.26 ± 12.59 | ±0.36 |
| ${}^{71}$Ge | 71 | 39 | 112.9856 | -817156.27 ± 1.3213 | 66571.1247 | 66066.1747 | +7643094.88 ± 12.32 | ±0.36 |
| ${}^{72}$Ge | 72 | 40 | 118.8906 | -810890.19 ± 0.1260 | 67504.7851 | 66994.9896 | +7609457.85 ± 1.13 | ±0.36 |
| ${}^{73}$Ge | 73 | 41 | 124.7830 | -803636.21 ± 0.0919 | 68438.4581 | 67927.7720 | +7518075.04 ± 0.84 | ±0.37 |
| ${}^{74}$Ge | 74 | 42 | 130.6632 | -797630.07 ± 0.0344 | 69372.1434 | 68857.1412 | +7479285.26 ± 0.18 | ±0.37 |
| ${}^{75}$Ge | 75 | 43 | 136.5314 | -790650.87 ± 0.0805 | 70305.8406 | 69790.2008 | +7388427.38 ± 0.73 | ±0.38 |
| ${}^{76}$Ge | 76 | 44 | 142.3880 | -784781.65 ± 0.0345 | 71239.5494 | 70720.3390 | +7341741.16 ± 0.25 | ±0.38 |
| ${}^{77}$Ge | 77 | 45 | 148.2334 | -777983.72 ± 0.0807 | 72173.2694 | 71653.8331 | +7249246.36 ± 0.73 | ±0.38 |
| ${}^{78}$Ge | 78 | 46 | 154.0680 | -772220.13 ± 5.2239 | 73107.0003 | 72584.6780 | +7196040.36 ± 48.70 | ±0.39 |
| ${}^{79}$Ge | 79 | 47 | 159.8919 | -765597.77 ± 54.4791 | 74040.7418 | 73518.5070 | +7103446.53 ± 505.45 | ±0.39 |
| ${}^{80}$Ge | 80 | 48 | 165.7055 | -759918.61 ± 2.9788 | 74974.4936 | 74449.9930 | +7045005.41 ± 27.59 | ±0.39 |
| ${}^{81}$Ge | 81 | 49 | 171.5092 | -753236.08 ± 2.9601 | 75908.2554 | 75384.7307 | +6944704.52 ± 27.25 | ±0.40 |
| ${}^{82}$Ge | 82 | 50 | 177.3030 | -747513.58 ± 3.1879 | 76842.0269 | 76317.1014 | +6878215.80 ± 29.35 | ±0.40 |
| ${}^{83}$Ge | 83 | 51 | 183.0875 | -740618.16 ± 3.4335 | 77775.8079 | 77253.0342 | +6767032.14 ± 31.40 | ±0.40 |
| ${}^{84}$Ge | 84 | 52 | 188.8626 | -734409.26 ± 4.4534 | 78709.5982 | 78187.3563 | +6679364.93 ± 40.54 | ±0.41 |
| ${}^{85}$Ge | 85 | 53 | 194.6289 | -727467.94 ± 5.2251 | 79643.3974 | 79123.8754 | +6565931.93 ± 47.13 | ±0.41 |
| ${}^{86}$Ge | 86 | 54 | 200.3863 | -721103.90 ± 609.3268 | 80577.2053 | 80059.0930 | +6471623.71 ± 5468.49 | ±0.41 |
| ${}^{87}$Ge | 87 | 55 | 206.1353 | -714016.75 ± 362.1002 | 81511.0218 | 80996.3968 | +6353677.16 ± 3703.14 | ±0.41 |
| ${}^{88}$Ge | 88 | 56 | 211.8760 | -707663.75 ± 607.0908 | 82444.8465 | 81931.9616 | +6259889.02 ± 4877.35 | ±0.42 |
| ${}^{89}$Ge | 89 | 57 | 217.6085 | -700399.50 ± 490.1360 | 83378.6794 | 82869.9351 | +6139069.13 ± 4822.15 | ±0.42 |
| ${}^{90}$Ge | 90 | 58 | 223.3332 | -693984.44 ± 739.9186 | 84312.5201 | 83805.9991 | +6043970.48 ± 5968.69 | ±0.42 |

### Arsenic (Z = 33)

_33 of 33 isotopes with a framework prediction; 33 of 33 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{60}$As | 60 | 27 | 33.0873 | -928706.56 ± 904.9774 | 56315.0210 | 55884.0060 | +7712672.21 ± 7150.72 | ±0.29 |
| ${}^{61}$As | 61 | 28 | 39.2213 | -918918.92 ± 630.5170 | 57248.4524 | 56803.9403 | +7825374.70 ± 5280.29 | ±0.30 |
| ${}^{62}$As | 62 | 29 | 45.3359 | -909153.37 ± 621.1952 | 58181.9033 | 57728.2144 | +7859049.17 ± 5195.75 | ±0.31 |
| ${}^{63}$As | 63 | 30 | 51.4317 | -900356.89 ± 366.1662 | 59115.3729 | 58650.6283 | +7923949.75 ± 3414.65 | ±0.31 |
| ${}^{64}$As | 64 | 31 | 57.5093 | -891554.08 ± 362.0565 | 60048.8607 | 59576.0900 | +7935577.64 ± 3408.51 | ±0.32 |
| ${}^{65}$As | 65 | 32 | 63.5694 | -883520.33 ± 155.3196 | 60982.3660 | 60500.1797 | +7969998.85 ± 1401.09 | ±0.32 |
| ${}^{66}$As | 66 | 33 | 69.6126 | -875450.47 ± 10.1672 | 61915.8883 | 61426.5858 | +7965647.90 ± 92.50 | ±0.33 |
| ${}^{67}$As | 67 | 34 | 75.6393 | -867658.84 ± 0.7737 | 62849.4270 | 62353.5177 | +7953187.82 ± 7.10 | ±0.33 |
| ${}^{68}$As | 68 | 35 | 81.6503 | -859689.74 ± 3.1667 | 63782.9814 | 63282.7045 | +7905428.59 ± 29.16 | ±0.34 |
| ${}^{69}$As | 69 | 36 | 87.6459 | -852501.51 ± 53.8562 | 64716.5512 | 64209.9810 | +7889275.77 ± 498.34 | ±0.34 |
| ${}^{70}$As | 70 | 37 | 93.6267 | -844862.72 ± 2.3198 | 65650.1358 | 65140.2533 | +7827457.47 ± 21.45 | ±0.35 |
| ${}^{71}$As | 71 | 38 | 99.5931 | -838096.63 ± 6.7637 | 66583.7348 | 66068.1881 | +7803252.22 ± 63.01 | ±0.35 |
| ${}^{72}$As | 72 | 39 | 105.5456 | -830733.52 ± 6.5471 | 67517.3478 | 66999.3457 | +7731450.07 ± 60.94 | ±0.36 |
| ${}^{73}$As | 73 | 40 | 111.4847 | -824251.35 ± 6.0762 | 68450.9742 | 67928.1168 | +7697215.39 ± 56.72 | ±0.36 |
| ${}^{74}$As | 74 | 41 | 117.4106 | -817208.60 ± 2.6382 | 69384.6137 | 68859.7036 | +7622891.37 ± 24.58 | ±0.36 |
| ${}^{75}$As | 75 | 42 | 123.3238 | -811016.95 ± 1.3562 | 70318.2658 | 69789.0236 | +7583459.88 ± 12.65 | ±0.37 |
| ${}^{76}$As | 76 | 43 | 129.2248 | -804173.50 ± 1.3475 | 71251.9303 | 70721.2605 | +7503681.91 ± 12.53 | ±0.37 |
| ${}^{77}$As | 77 | 44 | 135.1137 | -798214.38 ± 2.5299 | 72185.6068 | 71651.1297 | +7459437.96 ± 23.61 | ±0.37 |
| ${}^{78}$As | 78 | 45 | 140.9910 | -791606.71 ± 14.4572 | 73119.2949 | 72583.7231 | +7378675.97 ± 134.72 | ±0.38 |
| ${}^{79}$As | 79 | 46 | 146.8571 | -785751.69 ± 7.7680 | 74052.9943 | 73514.3981 | +7326403.63 ± 72.43 | ±0.38 |
| ${}^{80}$As | 80 | 47 | 152.7122 | -779350.38 ± 4.8201 | 74986.7046 | 74447.3137 | +7245270.35 ± 44.77 | ±0.39 |
| ${}^{81}$As | 81 | 48 | 158.5566 | -773649.88 ± 3.7696 | 75920.4256 | 75378.4891 | +7189538.31 ± 35.07 | ±0.39 |
| ${}^{82}$As | 82 | 49 | 164.3906 | -767196.96 ± 5.2837 | 76854.1570 | 76312.4111 | +7099054.06 ± 48.86 | ±0.39 |
| ${}^{83}$As | 83 | 50 | 170.2146 | -761527.86 ± 3.9188 | 77787.8985 | 77244.3413 | +7036854.79 ± 36.23 | ±0.39 |
| ${}^{84}$As | 84 | 51 | 176.0287 | -754843.87 ± 4.4104 | 78721.6498 | 78179.6511 | +6932733.07 ± 40.55 | ±0.40 |
| ${}^{85}$As | 85 | 52 | 181.8332 | -748652.54 ± 4.2533 | 79655.4107 | 79113.8097 | +6845846.59 ± 38.90 | ±0.40 |
| ${}^{86}$As | 86 | 53 | 187.6285 | -742012.74 ± 4.7418 | 80589.1809 | 80049.5308 | +6741452.18 ± 43.09 | ±0.40 |
| ${}^{87}$As | 87 | 54 | 193.4146 | -735774.21 ± 4.0766 | 81522.9601 | 80984.3691 | +6650555.05 ± 36.85 | ±0.41 |
| ${}^{88}$As | 88 | 55 | 199.1920 | -728949.24 ± 239.4923 | 82456.7482 | 81921.0314 | +6539429.50 ± 2444.69 | ±0.41 |
| ${}^{89}$As | 89 | 56 | 204.9607 | -722672.36 ± 361.2717 | 83390.5449 | 82856.4452 | +6446085.12 ± 3620.01 | ±0.41 |
| ${}^{90}$As | 90 | 57 | 210.7210 | -715856.32 ± 485.4369 | 84324.3501 | 83793.4789 | +6335470.61 ± 4769.00 | ±0.41 |
| ${}^{91}$As | 91 | 58 | 216.4731 | -709509.73 ± 488.4601 | 85258.1634 | 84729.4638 | +6239855.44 ± 4716.32 | ±0.42 |
| ${}^{92}$As | 92 | 59 | 222.2172 | -702573.08 ± 615.6877 | 86191.9847 | 85667.0778 | +6127288.47 ± 5839.03 | ±0.42 |

### Selenium (Z = 34)

_33 of 33 isotopes with a framework prediction; 33 of 33 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{63}$Se | 63 | 29 | 37.2741 | -925268.15 ± 1010.4838 | 59128.7482 | 58667.2787 | +7865874.40 ± 8526.26 | ±0.30 |
| ${}^{64}$Se | 64 | 30 | 43.4086 | -916005.02 ± 990.7121 | 60062.1791 | 59588.7630 | +7944720.64 ± 8394.41 | ±0.31 |
| ${}^{65}$Se | 65 | 31 | 49.5245 | -906742.33 ± 611.9951 | 60995.6286 | 60514.0971 | +7957343.94 ± 4956.55 | ±0.31 |
| ${}^{66}$Se | 66 | 32 | 55.6224 | -898462.29 ± 361.4458 | 61929.0962 | 61436.9507 | +8010577.82 ± 3259.78 | ±0.32 |
| ${}^{67}$Se | 67 | 33 | 61.7028 | -889965.51 ± 119.6004 | 62862.5811 | 62363.5247 | +8002377.91 ± 1075.43 | ±0.32 |
| ${}^{68}$Se | 68 | 34 | 67.7664 | -882439.62 ± 0.8611 | 63796.0830 | 63287.4096 | +8037512.64 ± 7.83 | ±0.33 |
| ${}^{69}$Se | 69 | 35 | 73.8137 | -874200.26 ± 2.5401 | 64729.6011 | 64216.6584 | +7987687.87 ± 23.19 | ±0.33 |
| ${}^{70}$Se | 70 | 36 | 79.8453 | -866996.00 ± 2.6353 | 65663.1349 | 65142.6574 | +7989812.06 ± 24.31 | ±0.34 |
| ${}^{71}$Se | 71 | 37 | 85.8615 | -859153.41 ± 4.5888 | 66596.6841 | 66072.9348 | +7926835.18 ± 42.29 | ±0.34 |
| ${}^{72}$Se | 72 | 38 | 91.8630 | -852406.01 ± 3.1465 | 67530.2481 | 66999.7073 | +7918554.04 ± 29.20 | ±0.35 |
| ${}^{73}$Se | 73 | 39 | 97.8501 | -844887.69 ± 11.7687 | 68463.8264 | 67930.8422 | +7845982.90 ± 109.27 | ±0.35 |
| ${}^{74}$Se | 74 | 40 | 103.8233 | -838505.62 ± 0.0345 | 69397.4186 | 68858.3505 | +7828653.61 ± 0.20 | ±0.35 |
| ${}^{75}$Se | 75 | 41 | 109.7830 | -831341.47 ± 0.1152 | 70331.0244 | 69789.8883 | +7753789.26 ± 1.04 | ±0.36 |
| ${}^{76}$Se | 76 | 42 | 115.7295 | -825201.06 ± 0.0344 | 71264.6432 | 70718.2999 | +7725628.23 ± 0.22 | ±0.36 |
| ${}^{77}$Se | 77 | 43 | 121.6634 | -818274.82 ± 0.0920 | 72198.2748 | 71650.4465 | +7645846.14 ± 0.87 | ±0.37 |
| ${}^{78}$Se | 78 | 44 | 127.5849 | -812372.09 ± 0.2638 | 73131.9187 | 72579.5141 | +7611025.86 ± 2.45 | ±0.37 |
| ${}^{79}$Se | 79 | 45 | 133.4944 | -805671.36 ± 0.3220 | 74065.5746 | 73512.1167 | +7528798.22 ± 3.02 | ±0.37 |
| ${}^{80}$Se | 80 | 46 | 139.3922 | -799972.43 ± 1.3546 | 74999.2422 | 74441.7688 | +7488717.85 ± 12.71 | ±0.38 |
| ${}^{81}$Se | 81 | 47 | 145.2787 | -793510.87 ± 1.3930 | 75932.9211 | 75374.6334 | +7406838.91 ± 12.96 | ±0.38 |
| ${}^{82}$Se | 82 | 48 | 151.1542 | -787955.62 ± 0.6557 | 76866.6111 | 76304.9226 | +7361104.52 ± 6.10 | ±0.38 |
| ${}^{83}$Se | 83 | 49 | 157.0189 | -781511.62 ± 4.2270 | 77800.3118 | 77238.6701 | +7271510.00 ± 39.30 | ±0.39 |
| ${}^{84}$Se | 84 | 50 | 162.8732 | -776069.70 ± 2.6909 | 78734.0230 | 78169.5570 | +7221046.43 ± 25.08 | ±0.39 |
| ${}^{85}$Se | 85 | 51 | 168.7173 | -769472.85 ± 3.5655 | 79667.7443 | 79104.5852 | +7119171.86 ± 33.02 | ±0.39 |
| ${}^{86}$Se | 86 | 52 | 174.5514 | -763492.19 ± 3.4142 | 80601.4755 | 80037.9897 | +7040229.24 ± 31.48 | ±0.40 |
| ${}^{87}$Se | 87 | 53 | 180.3760 | -756915.83 ± 3.0249 | 81535.2164 | 80973.5609 | +6936282.98 ± 27.67 | ±0.40 |
| ${}^{88}$Se | 88 | 54 | 186.1911 | -750935.00 ± 4.4968 | 82468.9667 | 81907.5969 | +6853696.18 ± 40.99 | ±0.40 |
| ${}^{89}$Se | 89 | 55 | 191.9971 | -744256.17 ± 4.9672 | 83402.7262 | 82843.9828 | +6744525.15 ± 45.01 | ±0.40 |
| ${}^{90}$Se | 90 | 56 | 197.7941 | -738235.64 ± 436.3985 | 84336.4945 | 83778.6691 | +6658322.91 ± 3935.95 | ±0.41 |
| ${}^{91}$Se | 91 | 57 | 203.5825 | -731588.09 ± 571.0729 | 85270.2716 | 84715.3833 | +6550030.40 ± 5112.94 | ±0.41 |
| ${}^{92}$Se | 92 | 58 | 209.3623 | -725491.32 ± 482.5090 | 86204.0572 | 85650.7338 | +6460230.11 ± 4665.59 | ±0.41 |
| ${}^{93}$Se | 93 | 59 | 215.1338 | -718751.77 ± 486.3222 | 87137.8511 | 86588.0917 | +6349135.05 ± 4615.08 | ±0.42 |
| ${}^{94}$Se | 94 | 60 | 220.8972 | -712717.54 ± 611.2469 | 88071.6531 | 87523.6424 | +6261287.87 ± 5715.17 | ±0.42 |
| ${}^{95}$Se | 95 | 61 | 226.6528 | -705890.22 ± 616.3708 | 89005.4630 | 88461.4800 | +6149377.56 ± 5654.58 | ±0.42 |

### Bromine (Z = 35)

_34 of 34 isotopes with a framework prediction; 34 of 34 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{65}$Br | 65 | 30 | 35.1308 | -931620.20 ± 1012.1457 | 61009.2400 | 60530.6265 | +7906963.73 ± 8263.79 | ±0.30 |
| ${}^{66}$Br | 66 | 31 | 41.2851 | -921945.19 ± 748.6898 | 61942.6511 | 61455.0413 | +7934416.39 ± 6502.49 | ±0.31 |
| ${}^{67}$Br | 67 | 32 | 47.4208 | -913135.30 ± 490.9180 | 62876.0808 | 62377.5753 | +7991741.86 ± 4808.48 | ±0.31 |
| ${}^{68}$Br | 68 | 33 | 53.5387 | -904438.15 ± 485.4958 | 63809.5283 | 63302.8079 | +8004706.78 ± 4090.74 | ±0.32 |
| ${}^{69}$Br | 69 | 34 | 59.6393 | -896423.27 ± 72.9427 | 64742.9932 | 64226.8337 | +8036508.39 ± 653.96 | ±0.32 |
| ${}^{70}$Br | 70 | 35 | 65.7231 | -888422.50 ± 25.3007 | 65676.4748 | 65153.1616 | +8032044.91 ± 228.75 | ±0.33 |
| ${}^{71}$Br | 71 | 36 | 71.7908 | -880782.67 ± 8.9725 | 66609.9726 | 66079.5789 | +8026589.04 ± 81.75 | ±0.33 |
| ${}^{72}$Br | 72 | 37 | 77.8426 | -872975.19 ± 1.6684 | 67543.4861 | 67008.5137 | +7983647.76 ± 15.29 | ±0.34 |
| ${}^{73}$Br | 73 | 38 | 83.8793 | -865893.92 ± 10.7725 | 68477.0148 | 67935.4238 | +7972145.23 ± 99.23 | ±0.34 |
| ${}^{74}$Br | 74 | 39 | 89.9012 | -858464.23 ± 9.1920 | 69410.5584 | 68865.2755 | +7918110.65 ± 84.73 | ±0.35 |
| ${}^{75}$Br | 75 | 40 | 95.9088 | -851780.80 ± 6.6183 | 70344.1163 | 69792.9508 | +7897151.35 ± 61.39 | ±0.35 |
| ${}^{76}$Br | 76 | 41 | 101.9024 | -844738.40 ± 14.2082 | 71277.6880 | 70723.2628 | +7839361.58 ± 131.80 | ±0.35 |
| ${}^{77}$Br | 77 | 42 | 107.8825 | -838340.49 ± 4.2115 | 72211.2733 | 71651.8112 | +7808067.09 ± 39.22 | ±0.36 |
| ${}^{78}$Br | 78 | 43 | 113.8496 | -831491.98 ± 5.2990 | 73144.8717 | 72583.0879 | +7739871.81 ± 49.31 | ±0.36 |
| ${}^{79}$Br | 79 | 44 | 119.8038 | -825440.29 ± 1.4619 | 74078.4829 | 73511.9661 | +7706456.07 ± 13.61 | ±0.37 |
| ${}^{80}$Br | 80 | 45 | 125.7457 | -818865.61 ± 1.4290 | 75012.1064 | 74443.6393 | +7636208.12 ± 13.33 | ±0.37 |
| ${}^{81}$Br | 81 | 46 | 131.6756 | -813059.53 ± 1.3915 | 75945.7420 | 75373.0454 | +7598162.13 ± 12.96 | ±0.37 |
| ${}^{82}$Br | 82 | 47 | 137.5937 | -806740.81 ± 1.3591 | 76879.3893 | 76305.0178 | +7527308.76 ± 12.72 | ±0.38 |
| ${}^{83}$Br | 83 | 48 | 143.5004 | -801122.23 ± 5.2569 | 77813.0479 | 77234.9969 | +7484315.11 ± 49.12 | ±0.38 |
| ${}^{84}$Br | 84 | 49 | 149.3961 | -794895.93 ± 35.3233 | 78746.7177 | 78167.7216 | +7407099.59 ± 329.16 | ±0.38 |
| ${}^{85}$Br | 85 | 50 | 155.2809 | -789379.71 ± 4.1736 | 79680.3983 | 79098.4233 | +7357604.95 ± 38.91 | ±0.39 |
| ${}^{86}$Br | 86 | 51 | 161.1553 | -782921.78 ± 4.1472 | 80614.0894 | 80032.8607 | +7262375.89 ± 38.45 | ±0.39 |
| ${}^{87}$Br | 87 | 52 | 167.0194 | -776925.07 ± 4.2297 | 81547.7907 | 80966.0953 | +7184431.55 ± 39.16 | ±0.39 |
| ${}^{88}$Br | 88 | 53 | 172.8735 | -770606.12 ± 4.2038 | 82481.5020 | 81900.7652 | +7090737.90 ± 38.72 | ±0.39 |
| ${}^{89}$Br | 89 | 54 | 178.7179 | -764609.35 ± 4.3021 | 83415.2231 | 82834.7010 | +7008199.39 ± 39.40 | ±0.40 |
| ${}^{90}$Br | 90 | 55 | 184.5528 | -758133.86 ± 4.3995 | 84348.9536 | 83770.4690 | +6905590.53 ± 40.08 | ±0.40 |
| ${}^{91}$Br | 91 | 56 | 190.3784 | -752180.86 ± 4.6080 | 85282.6934 | 84704.8561 | +6821772.10 ± 41.83 | ±0.40 |
| ${}^{92}$Br | 92 | 57 | 196.1950 | -745667.62 ± 8.6942 | 86216.4422 | 85641.2247 | +6716595.13 ± 78.33 | ±0.41 |
| ${}^{93}$Br | 93 | 58 | 202.0028 | -739734.23 ± 555.0710 | 87150.1998 | 86576.0614 | +6631606.32 ± 4976.16 | ±0.41 |
| ${}^{94}$Br | 94 | 59 | 207.8021 | -733237.56 ± 241.3419 | 88083.9660 | 87512.7961 | +6526701.13 ± 2288.48 | ±0.41 |
| ${}^{95}$Br | 95 | 60 | 213.5929 | -727307.90 ± 363.8569 | 89017.7406 | 88448.0898 | +6440509.77 ± 3391.15 | ±0.41 |
| ${}^{96}$Br | 96 | 61 | 219.3755 | -720776.89 ± 366.5689 | 89951.5233 | 89385.2241 | +6335490.82 ± 3355.60 | ±0.42 |
| ${}^{97}$Br | 97 | 62 | 225.1502 | -714848.17 ± 491.4005 | 90885.3141 | 90320.9276 | +6248679.46 ± 4424.35 | ±0.42 |
| ${}^{98}$Br | 98 | 63 | 230.9170 | -708307.01 ± 495.1721 | 91819.1127 | 91258.3721 | +6144539.12 ± 4378.90 | ±0.42 |

### Krypton (Z = 36)

_35 of 35 isotopes with a framework prediction; 35 of 35 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{67}$Kr | 67 | 31 | 32.7934 | -937910.23 ± 761.1315 | 62889.9259 | 62394.5537 | +7939350.57 ± 6792.74 | ±0.30 |
| ${}^{68}$Kr | 68 | 32 | 38.9672 | -928672.31 ± 871.2970 | 63823.3175 | 63315.9727 | +8012904.14 ± 7900.26 | ±0.31 |
| ${}^{69}$Kr | 69 | 33 | 45.1226 | -919553.34 ± 492.0654 | 64756.7275 | 64240.9529 | +8028751.38 ± 4669.00 | ±0.31 |
| ${}^{70}$Kr | 70 | 34 | 51.2603 | -911302.09 ± 363.3721 | 65690.1553 | 65163.4869 | +8082261.07 ± 3073.37 | ±0.32 |
| ${}^{71}$Kr | 71 | 35 | 57.3808 | -902946.15 ± 217.7941 | 66623.6002 | 66089.7542 | +8077591.48 ± 1948.38 | ±0.32 |
| ${}^{72}$Kr | 72 | 36 | 63.4846 | -895397.13 ± 13.2039 | 67557.0618 | 67013.6349 | +8109198.79 ± 119.54 | ±0.33 |
| ${}^{73}$Kr | 73 | 37 | 69.5723 | -887349.33 ± 10.6499 | 68490.5395 | 67942.5178 | +8065960.88 ± 96.81 | ±0.33 |
| ${}^{74}$Kr | 74 | 38 | 75.6444 | -880204.34 ± 3.1876 | 69424.0329 | 68868.2318 | +8070499.95 ± 29.23 | ±0.34 |
| ${}^{75}$Kr | 75 | 39 | 81.7012 | -872641.96 ± 12.6382 | 70357.5415 | 69797.7341 | +8020422.60 ± 116.11 | ±0.34 |
| ${}^{76}$Kr | 76 | 40 | 87.7433 | -865891.17 ± 6.1333 | 71291.0648 | 70724.5382 | +8010326.10 ± 56.74 | ±0.35 |
| ${}^{77}$Kr | 77 | 41 | 93.7711 | -858671.30 ± 2.9477 | 72224.6024 | 71654.8765 | +7950971.59 ± 27.30 | ±0.35 |
| ${}^{78}$Kr | 78 | 42 | 99.7850 | -852296.57 ± 0.4503 | 73158.1540 | 72582.3618 | +7932948.63 ± 4.22 | ±0.35 |
| ${}^{79}$Kr | 79 | 43 | 105.7854 | -845323.11 ± 5.0941 | 74091.7190 | 73513.5919 | +7864220.37 ± 47.34 | ±0.36 |
| ${}^{80}$Kr | 80 | 44 | 111.7726 | -839276.53 ± 1.0008 | 75025.2972 | 74441.6348 | +7840535.94 ± 9.32 | ±0.36 |
| ${}^{81}$Kr | 81 | 45 | 117.7471 | -832581.11 ± 1.5318 | 75958.8881 | 75373.3262 | +7768821.00 ± 14.24 | ±0.36 |
| ${}^{82}$Kr | 82 | 46 | 123.7092 | -826804.60 ± 0.0344 | 76892.4914 | 76301.9247 | +7739866.47 ± 0.07 | ±0.37 |
| ${}^{83}$Kr | 83 | 47 | 129.6592 | -820353.28 ± 0.0345 | 77826.1068 | 77234.0200 | +7666140.76 ± 0.11 | ±0.37 |
| ${}^{84}$Kr | 84 | 48 | 135.5975 | -814824.73 ± 0.0344 | 78759.7340 | 78163.0654 | +7633639.12 ± 0.05 | ±0.37 |
| ${}^{85}$Kr | 85 | 49 | 141.5243 | -808590.04 ± 2.7016 | 79693.3726 | 79095.5185 | +7558634.76 ± 25.28 | ±0.38 |
| ${}^{86}$Kr | 86 | 50 | 147.4400 | -803212.54 ± 0.0344 | 80627.0224 | 80025.2272 | +7520067.59 ± 0.05 | ±0.38 |
| ${}^{87}$Kr | 87 | 51 | 153.3448 | -796826.98 ± 0.3228 | 81560.6830 | 80959.2775 | +7428493.61 ± 3.04 | ±0.38 |
| ${}^{88}$Kr | 88 | 52 | 159.2390 | -790970.82 ± 3.4193 | 82494.3542 | 81891.7898 | +7358055.31 ± 31.85 | ±0.39 |
| ${}^{89}$Kr | 89 | 53 | 165.1229 | -784636.83 ± 2.7975 | 83428.0356 | 82826.4394 | +7263335.35 ± 25.87 | ±0.39 |
| ${}^{90}$Kr | 90 | 54 | 170.9968 | -778849.11 ± 2.4094 | 84361.7272 | 83759.5101 | +7189835.63 ± 22.24 | ±0.39 |
| ${}^{91}$Kr | 91 | 55 | 176.8609 | -772467.47 ± 2.8800 | 85295.4285 | 84694.9895 | +7089428.41 ± 26.40 | ±0.40 |
| ${}^{92}$Kr | 92 | 56 | 182.7154 | -766696.46 ± 3.4537 | 86229.1394 | 85628.6882 | +7012266.98 ± 31.55 | ±0.40 |
| ${}^{93}$Kr | 93 | 57 | 188.5606 | -760285.24 ± 3.1922 | 87162.8597 | 86564.8156 | +6908627.08 ± 29.05 | ±0.40 |
| ${}^{94}$Kr | 94 | 58 | 194.3967 | -754514.67 ± 15.2890 | 88096.5890 | 87499.0980 | +6828539.49 ± 138.39 | ±0.40 |
| ${}^{95}$Kr | 95 | 59 | 200.2239 | -748073.07 ± 23.4401 | 89030.3272 | 88435.7809 | +6722915.86 ± 210.66 | ±0.41 |
| ${}^{96}$Kr | 96 | 60 | 206.0424 | -742370.93 ± 24.1031 | 89964.0742 | 89370.3523 | +6643387.55 ± 215.70 | ±0.41 |
| ${}^{97}$Kr | 97 | 61 | 211.8524 | -735903.10 ± 162.5661 | 90897.8296 | 90307.5046 | +6536832.06 ± 1444.06 | ±0.41 |
| ${}^{98}$Kr | 98 | 62 | 217.6542 | -730269.51 ± 364.3430 | 91831.5932 | 91242.3019 | +6458531.51 ± 3287.30 | ±0.41 |
| ${}^{99}$Kr | 99 | 63 | 223.4478 | -723908.42 ± 489.2966 | 92765.3650 | 92179.5164 | +6355518.74 ± 4335.14 | ±0.42 |
| ${}^{100}$Kr | 100 | 64 | 229.2336 | -718178.56 ± 491.7630 | 93699.1447 | 93114.9404 | +6274011.94 ± 4291.59 | ±0.42 |
| ${}^{101}$Kr | 101 | 65 | 235.0116 | -711845.55 ± 619.1950 | 94632.9321 | 94052.3244 | +6173241.63 ± 5318.45 | ±0.42 |

### Rubidium (Z = 37)

_34 of 34 isotopes with a framework prediction; 34 of 34 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{71}$Rb | 71 | 34 | 42.6317 | -926035.25 ± 739.0983 | 66637.5670 | 66103.7911 | +8074814.78 ± 6045.21 | ±0.31 |
| ${}^{72}$Rb | 72 | 35 | 48.7889 | -917383.07 ± 853.4504 | 67570.9751 | 67029.2454 | +8081990.42 ± 7462.60 | ±0.32 |
| ${}^{73}$Rb | 73 | 36 | 54.9291 | -909398.40 ± 67.2841 | 68504.4004 | 67953.0580 | +8113577.54 ± 600.32 | ±0.32 |
| ${}^{74}$Rb | 74 | 37 | 61.0528 | -901566.99 ± 4.8797 | 69437.8422 | 68878.6477 | +8118546.46 ± 43.94 | ±0.33 |
| ${}^{75}$Rb | 75 | 38 | 67.1603 | -894005.50 ± 1.8584 | 70371.3000 | 69804.8391 | +8114923.80 ± 16.89 | ±0.33 |
| ${}^{76}$Rb | 76 | 39 | 73.2523 | -886422.21 ± 1.4494 | 71304.7735 | 70733.0728 | +8082508.98 ± 13.25 | ±0.34 |
| ${}^{77}$Rb | 77 | 40 | 79.3291 | -879324.48 ± 1.9795 | 72238.2621 | 71660.2155 | +8066492.75 ± 18.20 | ±0.34 |
| ${}^{78}$Rb | 78 | 41 | 85.3912 | -872082.96 ± 4.8491 | 73171.7654 | 72589.6047 | +8019891.38 ± 44.59 | ±0.34 |
| ${}^{79}$Rb | 79 | 42 | 91.4390 | -865429.94 ± 2.8601 | 74105.2830 | 73517.2314 | +7998826.67 ± 26.42 | ±0.35 |
| ${}^{80}$Rb | 80 | 43 | 97.4730 | -858516.28 ± 2.7056 | 75038.8145 | 74447.3528 | +7944697.18 ± 25.02 | ±0.35 |
| ${}^{81}$Rb | 81 | 44 | 103.4934 | -852212.82 ± 6.9978 | 75972.3595 | 75375.5657 | +7917602.76 ± 65.07 | ±0.36 |
| ${}^{82}$Rb | 82 | 45 | 109.5007 | -845575.55 ± 4.2440 | 76905.9176 | 76306.3287 | +7857656.41 ± 39.43 | ±0.36 |
| ${}^{83}$Rb | 83 | 46 | 115.4952 | -839599.60 ± 3.2391 | 77839.4885 | 77234.9400 | +7827396.96 ± 30.15 | ±0.36 |
| ${}^{84}$Rb | 84 | 47 | 121.4773 | -833319.39 ± 3.0082 | 78773.0718 | 78165.7457 | +7769721.78 ± 28.06 | ±0.37 |
| ${}^{85}$Rb | 85 | 48 | 127.4473 | -827606.79 ± 0.0345 | 79706.6673 | 79094.8315 | +7735471.27 ± 0.06 | ±0.37 |
| ${}^{86}$Rb | 86 | 49 | 133.4055 | -821634.56 ± 0.2645 | 80640.2745 | 80025.7459 | +7679135.92 ± 2.49 | ±0.37 |
| ${}^{87}$Rb | 87 | 50 | 139.3522 | -816123.02 ± 0.0344 | 81573.8932 | 80955.3892 | +7640059.40 ± 0.07 | ±0.38 |
| ${}^{88}$Rb | 88 | 51 | 145.2877 | -809817.42 ± 0.2073 | 82507.5231 | 81888.8721 | +7554762.49 ± 1.93 | ±0.38 |
| ${}^{89}$Rb | 89 | 52 | 151.2123 | -803903.74 ± 7.0405 | 83441.1639 | 82821.2628 | +7484805.86 ± 65.51 | ±0.38 |
| ${}^{90}$Rb | 90 | 53 | 157.1263 | -797735.87 ± 8.3068 | 84374.8153 | 83755.1038 | +7399090.35 ± 77.03 | ±0.39 |
| ${}^{91}$Rb | 91 | 54 | 163.0300 | -791864.65 ± 9.9564 | 85308.4771 | 84688.2184 | +7324026.53 ± 92.12 | ±0.39 |
| ${}^{92}$Rb | 92 | 55 | 168.9235 | -785735.33 ± 7.7718 | 86242.1491 | 85622.6851 | +7234811.39 ± 71.51 | ±0.39 |
| ${}^{93}$Rb | 93 | 56 | 174.8071 | -779924.66 ± 9.8584 | 87175.8309 | 86556.3317 | +7157178.48 ± 90.46 | ±0.39 |
| ${}^{94}$Rb | 94 | 57 | 180.6811 | -773673.32 ± 2.5433 | 88109.5223 | 87491.8830 | +7059390.04 ± 23.18 | ±0.40 |
| ${}^{95}$Rb | 95 | 58 | 186.5457 | -767896.80 ± 25.1885 | 89043.2231 | 88426.0495 | +6979544.73 ± 228.94 | ±0.40 |
| ${}^{96}$Rb | 96 | 59 | 192.4011 | -761659.80 ± 4.1504 | 89976.9331 | 89362.0796 | +6880474.62 ± 37.52 | ±0.40 |
| ${}^{97}$Rb | 97 | 60 | 198.2475 | -756000.09 ± 2.3519 | 90910.6521 | 90296.4089 | +6802520.72 ± 21.17 | ±0.41 |
| ${}^{98}$Rb | 98 | 61 | 204.0852 | -750021.64 ± 19.6982 | 91844.3799 | 91232.0530 | +6711751.20 ± 176.28 | ±0.41 |
| ${}^{99}$Rb | 99 | 62 | 209.9143 | -744391.83 ± 4.9064 | 92778.1162 | 92166.7951 | +6632768.81 ± 43.73 | ±0.41 |
| ${}^{100}$Rb | 100 | 63 | 215.7351 | -738328.77 ± 15.9136 | 93711.8608 | 93103.1445 | +6538085.85 ± 140.96 | ±0.41 |
| ${}^{101}$Rb | 101 | 64 | 221.5476 | -732696.32 ± 24.7253 | 94645.6137 | 94038.3371 | +6457756.05 ± 217.92 | ±0.42 |
| ${}^{102}$Rb | 102 | 65 | 227.3522 | -726602.11 ± 99.6965 | 95579.3746 | 94975.1463 | +6361962.21 ± 872.89 | ±0.42 |
| ${}^{103}$Rb | 103 | 66 | 233.1489 | -720958.85 ± 493.0966 | 96513.1432 | 95910.7324 | +6280953.18 ± 4166.49 | ±0.42 |
| ${}^{104}$Rb | 104 | 67 | 238.9380 | -714846.61 ± 620.5784 | 97446.9196 | 96847.9366 | +6184778.11 ± 5164.93 | ±0.42 |

### Strontium (Z = 38)

_35 of 35 isotopes with a framework prediction; 35 of 35 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{73}$Sr | 73 | 35 | 39.9497 | -932454.15 ± 617.1316 | 68518.5974 | 67967.1193 | +8113895.59 ± 5893.18 | ±0.31 |
| ${}^{74}$Sr | 74 | 36 | 46.1264 | -924178.37 ± 121.6397 | 69451.9862 | 68889.7363 | +8161591.70 ± 1446.80 | ±0.32 |
| ${}^{75}$Sr | 75 | 37 | 52.2861 | -915970.98 ± 353.5703 | 70385.3919 | 69815.4391 | +8163707.80 ± 3151.21 | ±0.32 |
| ${}^{76}$Sr | 76 | 38 | 58.4293 | -908409.23 ± 54.0271 | 71318.8141 | 70739.3042 | +8192191.02 ± 487.22 | ±0.33 |
| ${}^{77}$Sr | 77 | 39 | 64.5565 | -900615.89 ± 12.1860 | 72252.2523 | 71667.2425 | +8162861.74 ± 110.48 | ±0.33 |
| ${}^{78}$Sr | 78 | 40 | 70.6682 | -893412.69 ± 11.2352 | 73185.7061 | 72593.3661 | +8159697.86 ± 102.65 | ±0.34 |
| ${}^{79}$Sr | 79 | 41 | 76.7648 | -886001.58 ± 11.0161 | 74119.1749 | 73522.5545 | +8114793.93 ± 100.94 | ±0.34 |
| ${}^{80}$Sr | 80 | 42 | 82.8467 | -879282.84 ± 5.0474 | 75052.6584 | 74449.2168 | +8105412.10 ± 46.52 | ±0.34 |
| ${}^{81}$Sr | 81 | 43 | 88.9144 | -872171.56 ± 4.4950 | 75986.1562 | 75379.4943 | +8048102.71 ± 41.50 | ±0.35 |
| ${}^{82}$Sr | 82 | 44 | 94.9681 | -865888.63 ± 8.4648 | 76919.6678 | 76306.5064 | +8035505.80 ± 78.52 | ±0.35 |
| ${}^{83}$Sr | 83 | 45 | 101.0084 | -859121.13 ± 9.5272 | 77853.1930 | 77237.2130 | +7975170.70 ± 88.47 | ±0.36 |
| ${}^{84}$Sr | 84 | 46 | 107.0356 | -853156.87 ± 1.7056 | 78786.7312 | 78164.8551 | +7955955.23 ± 15.90 | ±0.36 |
| ${}^{85}$Sr | 85 | 47 | 113.0500 | -846698.65 ± 3.8152 | 79720.2823 | 79095.8955 | +7894047.40 ± 35.57 | ±0.36 |
| ${}^{86}$Sr | 86 | 48 | 119.0519 | -841036.81 ± 0.0344 | 80653.8458 | 80023.9698 | +7871091.16 ± 0.07 | ±0.37 |
| ${}^{87}$Sr | 87 | 49 | 125.0417 | -834897.02 ± 0.0345 | 81587.4214 | 80955.1069 | +7810680.45 ± 0.06 | ±0.37 |
| ${}^{88}$Sr | 88 | 50 | 131.0196 | -829505.52 ± 0.0344 | 82521.0089 | 81883.5595 | +7784827.38 ± 0.07 | ±0.37 |
| ${}^{89}$Sr | 89 | 51 | 136.9861 | -823204.35 ± 0.1264 | 83454.6078 | 82816.7662 | +7701841.96 ± 1.10 | ±0.38 |
| ${}^{90}$Sr | 90 | 52 | 142.9413 | -817360.20 ± 1.8514 | 84388.2181 | 83748.5184 | +7638340.10 ± 17.30 | ±0.38 |
| ${}^{91}$Sr | 91 | 53 | 148.8855 | -811157.85 ± 6.9138 | 85321.8392 | 84682.3115 | +7552081.62 ± 64.38 | ±0.38 |
| ${}^{92}$Sr | 92 | 54 | 154.8191 | -805430.14 ± 4.3011 | 86255.4711 | 85614.5902 | +7485650.39 ± 39.98 | ±0.38 |
| ${}^{93}$Sr | 93 | 55 | 160.7423 | -799320.30 ± 9.4278 | 87189.1133 | 86548.8658 | +7397526.52 ± 87.27 | ±0.39 |
| ${}^{94}$Sr | 94 | 56 | 166.6553 | -793697.65 ± 2.0596 | 88122.7658 | 87481.6000 | +7329149.77 ± 19.01 | ±0.39 |
| ${}^{95}$Sr | 95 | 57 | 172.5583 | -787532.51 ± 7.1587 | 89056.4282 | 88416.8226 | +7233980.69 ± 65.71 | ±0.39 |
| ${}^{96}$Sr | 96 | 58 | 178.4516 | -781853.45 ± 10.3506 | 89990.1002 | 89350.5157 | +7158151.47 ± 94.75 | ±0.40 |
| ${}^{97}$Sr | 97 | 59 | 184.3355 | -775684.61 ± 4.1195 | 90923.7818 | 90286.3474 | +7060141.64 ± 37.48 | ±0.40 |
| ${}^{98}$Sr | 98 | 60 | 190.2101 | -770189.46 ± 3.8955 | 91857.4726 | 91219.9998 | +6988301.04 ± 35.36 | ±0.40 |
| ${}^{99}$Sr | 99 | 61 | 196.0757 | -764289.55 ± 5.7007 | 92791.1724 | 92155.3977 | +6898941.60 ± 51.40 | ±0.40 |
| ${}^{100}$Sr | 100 | 62 | 201.9324 | -758806.05 ± 8.2654 | 93724.8811 | 93089.5929 | +6824482.25 ± 74.31 | ±0.41 |
| ${}^{101}$Sr | 101 | 63 | 207.7805 | -752877.26 ± 10.0904 | 94658.5985 | 94025.5796 | +6732411.73 ± 90.18 | ±0.41 |
| ${}^{102}$Sr | 102 | 64 | 213.6202 | -747405.70 ± 79.3007 | 95592.3243 | 94960.2393 | +6656312.14 ± 706.27 | ±0.41 |
| ${}^{103}$Sr | 103 | 65 | 219.4515 | -741495.11 ± 242.6595 | 96526.0583 | 95896.6128 | +6563792.58 ± 2088.41 | ±0.41 |
| ${}^{104}$Sr | 104 | 66 | 225.2748 | -736034.13 ± 365.5862 | 97459.8004 | 96831.6271 | +6487274.98 ± 3097.55 | ±0.42 |
| ${}^{105}$Sr | 105 | 67 | 231.0902 | -730022.21 ± 613.3464 | 98393.5505 | 97768.6906 | +6391206.93 ± 5116.28 | ±0.42 |
| ${}^{106}$Sr | 106 | 68 | 236.8978 | -724564.32 ± 739.4627 | 99327.3083 | 98704.0746 | +6314163.84 ± 6077.58 | ±0.42 |
| ${}^{107}$Sr | 107 | 69 | 242.6979 | -718480.27 ± 868.8097 | 100261.0737 | 99641.6187 | +6216829.04 ± 7020.68 | ±0.42 |

### Yttrium (Z = 39)

_35 of 35 isotopes with a framework prediction; 35 of 35 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{75}$Y | 75 | 36 | 37.0785 | -938882.41 ± 494.4987 | 70399.8172 | 69830.2379 | +8156627.15 ± 4295.29 | ±0.31 |
| ${}^{76}$Y | 76 | 37 | 43.2744 | -930331.62 ± 489.4164 | 71333.1867 | 70755.3019 | +8167370.58 ± 4239.13 | ±0.32 |
| ${}^{77}$Y | 77 | 38 | 49.4534 | -922414.65 ± 362.4064 | 72266.5731 | 71678.6073 | +8202808.13 ± 2833.00 | ±0.32 |
| ${}^{78}$Y | 78 | 39 | 55.6160 | -914597.52 ± 479.0993 | 73199.9760 | 72604.3671 | +8203485.23 ± 4105.51 | ±0.33 |
| ${}^{79}$Y | 79 | 40 | 61.7627 | -907113.42 ± 120.4736 | 74133.3947 | 73530.2313 | +8202931.34 ± 1089.46 | ±0.33 |
| ${}^{80}$Y | 80 | 41 | 67.8939 | -899616.08 ± 9.2261 | 75066.8289 | 74458.3801 | +8171662.79 ± 83.83 | ±0.34 |
| ${}^{81}$Y | 81 | 42 | 74.0100 | -892579.99 ± 7.8416 | 76000.2782 | 75385.3095 | +8157672.73 ± 71.69 | ±0.34 |
| ${}^{82}$Y | 82 | 43 | 80.1116 | -885456.82 ± 7.8670 | 76933.7421 | 76314.4524 | +8114972.02 ± 72.04 | ±0.34 |
| ${}^{83}$Y | 83 | 44 | 86.1989 | -878868.42 ± 26.1849 | 77867.2202 | 77241.8049 | +8096849.12 ± 241.19 | ±0.35 |
| ${}^{84}$Y | 84 | 45 | 92.2723 | -872088.03 ± 5.9620 | 78800.7122 | 78171.6103 | +8047702.73 ± 54.99 | ±0.35 |
| ${}^{85}$Y | 85 | 46 | 98.3323 | -865921.37 ± 25.8572 | 79734.2176 | 79099.1567 | +8028668.82 ± 239.77 | ±0.35 |
| ${}^{86}$Y | 86 | 47 | 104.3791 | -859498.71 ± 19.0312 | 80667.7362 | 80029.2098 | +7978666.76 ± 176.71 | ±0.36 |
| ${}^{87}$Y | 87 | 48 | 110.4131 | -853701.54 ± 1.4986 | 81601.2676 | 80956.9686 | +7958536.27 ± 13.92 | ±0.36 |
| ${}^{88}$Y | 88 | 49 | 116.4347 | -847611.23 ± 1.9580 | 82534.8115 | 81887.1821 | +7908800.27 ± 18.31 | ±0.37 |
| ${}^{89}$Y | 89 | 50 | 122.4441 | -842119.03 ± 0.4361 | 83468.3675 | 82815.2640 | +7886268.95 ± 4.08 | ±0.37 |
| ${}^{90}$Y | 90 | 51 | 128.4417 | -835837.14 ± 0.4486 | 84401.9353 | 83747.9724 | +7808701.37 ± 4.22 | ±0.37 |
| ${}^{91}$Y | 91 | 52 | 134.4277 | -829909.35 ± 2.3374 | 85335.5147 | 84679.6121 | +7745697.02 ± 21.76 | ±0.37 |
| ${}^{92}$Y | 92 | 53 | 140.4024 | -823806.76 ± 11.4529 | 86269.1054 | 85612.6410 | +7667843.88 ± 106.61 | ±0.38 |
| ${}^{93}$Y | 93 | 54 | 146.3662 | -818031.31 ± 13.0421 | 87202.7071 | 86544.7245 | +7602804.20 ± 121.18 | ±0.38 |
| ${}^{94}$Y | 94 | 55 | 152.3192 | -812077.77 ± 7.8745 | 88136.3195 | 87478.0943 | +7524457.62 ± 72.93 | ±0.38 |
| ${}^{95}$Y | 95 | 56 | 158.2618 | -806400.92 ± 8.2975 | 89069.9424 | 88410.7319 | +7456226.66 ± 76.67 | ±0.39 |
| ${}^{96}$Y | 96 | 57 | 164.1941 | -800412.00 ± 7.3867 | 90003.5755 | 89345.1040 | +7369978.70 ± 67.99 | ±0.39 |
| ${}^{97}$Y | 97 | 58 | 170.1164 | -794674.82 ± 8.1017 | 90937.2186 | 90278.8126 | +7293028.82 ± 74.30 | ±0.39 |
| ${}^{98}$Y | 98 | 59 | 176.0289 | -788621.47 ± 9.5085 | 91870.8715 | 91214.1334 | +7199959.18 ± 86.81 | ±0.39 |
| ${}^{99}$Y | 99 | 60 | 181.9320 | -783205.98 ± 7.8804 | 92804.5339 | 92147.2725 | +7132726.82 ± 71.78 | ±0.40 |
| ${}^{100}$Y | 100 | 61 | 187.8256 | -777442.34 ± 13.2474 | 93738.2056 | 93082.0891 | +7048793.86 ± 120.09 | ±0.40 |
| ${}^{101}$Y | 101 | 62 | 193.7102 | -772037.60 ± 8.3320 | 94671.8864 | 94015.8497 | +6977937.71 ± 75.31 | ±0.40 |
| ${}^{102}$Y | 102 | 63 | 199.5859 | -766275.23 ± 4.7779 | 95605.5762 | 94951.2259 | +6891435.52 ± 42.98 | ±0.40 |
| ${}^{103}$Y | 103 | 64 | 205.4528 | -760904.30 ± 13.0414 | 96539.2747 | 95885.4356 | +6818960.65 ± 116.86 | ±0.41 |
| ${}^{104}$Y | 104 | 65 | 211.3113 | -755141.11 ± 241.0219 | 97472.9817 | 96821.3070 | +6730694.39 ± 2068.46 | ±0.41 |
| ${}^{105}$Y | 105 | 66 | 217.1613 | -749672.81 ± 484.1443 | 98406.6970 | 97756.3110 | +6653135.67 ± 4087.83 | ±0.41 |
| ${}^{106}$Y | 106 | 67 | 223.0033 | -743906.96 ± 608.6427 | 99340.4205 | 98692.5846 | +6564180.20 ± 5068.39 | ±0.41 |
| ${}^{107}$Y | 107 | 68 | 228.8372 | -738485.55 ± 611.3964 | 100274.1520 | 99627.8988 | +6486669.49 ± 5020.81 | ±0.42 |
| ${}^{108}$Y | 108 | 69 | 234.6633 | -732709.06 ± 738.0982 | 101207.8913 | 100564.5832 | +6396965.71 ± 5965.14 | ±0.42 |
| ${}^{109}$Y | 109 | 70 | 240.4817 | -727252.55 ± 741.7481 | 102141.6383 | 101500.3770 | +6317821.85 ± 6892.11 | ±0.42 |

### Zirconium (Z = 40)

_37 of 37 isotopes with a framework prediction; 37 of 37 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{77}$Zr | 77 | 37 | 34.0197 | -945286.22 ± 619.1950 | 72281.2245 | 71693.4460 | +8198497.48 ± 5573.88 | ±0.31 |
| ${}^{78}$Zr | 78 | 38 | 40.2345 | -937048.15 ± 610.2026 | 73214.5751 | 72615.6903 | +8247318.29 ± 5503.09 | ±0.32 |
| ${}^{79}$Zr | 79 | 39 | 46.4327 | -928903.46 ± 483.8515 | 74147.9424 | 73541.2639 | +8249497.84 ± 4078.54 | ±0.32 |
| ${}^{80}$Zr | 80 | 40 | 52.6145 | -921377.08 ± 478.1829 | 75081.3260 | 74464.7686 | +8279854.25 ± 4027.96 | ±0.33 |
| ${}^{81}$Zr | 81 | 41 | 58.7804 | -913559.13 ± 135.6140 | 76014.7254 | 75393.4980 | +8239801.54 ± 1223.15 | ±0.33 |
| ${}^{82}$Zr | 82 | 42 | 64.9310 | -906462.19 ± 2.2799 | 76948.1403 | 76318.9024 | +8244849.62 ± 20.75 | ±0.34 |
| ${}^{83}$Zr | 83 | 43 | 71.0665 | -899130.19 ± 9.1301 | 77881.5702 | 77248.0989 | +8200476.65 ± 83.23 | ±0.34 |
| ${}^{84}$Zr | 84 | 44 | 77.1875 | -892514.26 ± 7.6617 | 78815.0146 | 78174.0830 | +8198773.73 ± 70.34 | ±0.34 |
| ${}^{85}$Zr | 85 | 45 | 83.2943 | -885575.91 ± 8.8276 | 79748.4733 | 79103.8236 | +8149412.42 ± 81.28 | ±0.35 |
| ${}^{86}$Zr | 86 | 46 | 89.3872 | -879338.34 ± 4.8177 | 80681.9458 | 80030.5239 | +8139668.12 ± 44.54 | ±0.35 |
| ${}^{87}$Zr | 87 | 47 | 95.4666 | -872754.92 ± 5.5313 | 81615.4318 | 80960.6399 | +8087780.65 ± 51.20 | ±0.35 |
| ${}^{88}$Zr | 88 | 48 | 101.5330 | -866861.41 ± 7.0851 | 82548.9309 | 81887.8523 | +8072975.49 ± 65.98 | ±0.36 |
| ${}^{89}$Zr | 89 | 49 | 107.5865 | -860626.90 ± 3.5972 | 83482.4428 | 82818.0973 | +8021743.37 ± 33.55 | ±0.36 |
| ${}^{90}$Zr | 90 | 50 | 113.6275 | -855047.96 ± 0.1493 | 84415.9672 | 83745.6968 | +8003639.56 ± 1.40 | ±0.36 |
| ${}^{91}$Zr | 91 | 51 | 119.6564 | -848745.23 ± 0.1265 | 85349.5037 | 84678.0678 | +7929277.05 ± 1.11 | ±0.37 |
| ${}^{92}$Zr | 92 | 52 | 125.6734 | -842854.51 ± 0.1265 | 86283.0521 | 85608.9985 | +7873630.31 ± 1.10 | ±0.37 |
| ${}^{93}$Zr | 93 | 53 | 131.6788 | -836720.11 ± 0.5651 | 87216.6121 | 86541.8296 | +7797183.25 ± 5.26 | ±0.37 |
| ${}^{94}$Zr | 94 | 54 | 137.6729 | -831009.66 ± 0.2077 | 88150.1834 | 87473.1764 | +7739595.56 ± 1.86 | ±0.38 |
| ${}^{95}$Zr | 95 | 55 | 143.6560 | -825053.22 ± 1.0644 | 89083.7658 | 88406.2799 | +7663322.67 ± 9.83 | ±0.38 |
| ${}^{96}$Zr | 96 | 56 | 149.6283 | -819505.59 ± 0.1390 | 90017.3589 | 89337.9951 | +7604421.58 ± 1.27 | ±0.38 |
| ${}^{97}$Zr | 97 | 57 | 155.5901 | -813566.43 ± 0.1511 | 90950.9625 | 90271.9914 | +7521393.22 ± 1.34 | ±0.39 |
| ${}^{98}$Zr | 98 | 58 | 161.5416 | -807911.97 ± 10.0450 | 91884.5764 | 91205.1404 | +7449536.51 ± 92.58 | ±0.39 |
| ${}^{99}$Zr | 99 | 59 | 167.4831 | -801885.03 ± 12.4250 | 92818.2004 | 92140.2996 | +7357267.13 ± 113.94 | ±0.39 |
| ${}^{100}$Zr | 100 | 60 | 173.4147 | -796511.91 ± 9.5516 | 93751.8342 | 93073.0376 | +7293159.89 ± 87.49 | ±0.39 |
| ${}^{101}$Zr | 101 | 61 | 179.3368 | -790756.05 ± 9.7221 | 94685.4776 | 94007.7435 | +7209343.10 ± 88.62 | ±0.40 |
| ${}^{102}$Zr | 102 | 62 | 185.2494 | -785482.21 ± 10.1461 | 95619.1303 | 94940.8172 | +7144589.71 ± 92.24 | ±0.40 |
| ${}^{103}$Zr | 103 | 63 | 191.1529 | -779742.49 ± 10.6221 | 96552.7923 | 95876.0837 | +7058158.57 ± 96.18 | ±0.40 |
| ${}^{104}$Zr | 104 | 64 | 197.0474 | -774504.29 ± 10.6637 | 97486.4632 | 96809.6691 | +6990976.26 ± 96.22 | ±0.40 |
| ${}^{105}$Zr | 105 | 65 | 202.9331 | -768777.51 ± 13.7942 | 98420.1429 | 97745.4226 | +6902833.02 ± 123.89 | ±0.41 |
| ${}^{106}$Zr | 106 | 66 | 208.8102 | -763516.54 ± 240.0960 | 99353.8313 | 98679.6257 | +6832267.58 ± 2029.51 | ±0.41 |
| ${}^{107}$Zr | 107 | 67 | 214.6789 | -757804.88 ± 362.1439 | 100287.5280 | 99615.8490 | +6742692.61 ± 3010.98 | ±0.41 |
| ${}^{108}$Zr | 108 | 68 | 220.5393 | -752571.13 ± 484.6722 | 101221.2330 | 100550.4133 | +6671476.52 ± 3974.23 | ±0.41 |
| ${}^{109}$Zr | 109 | 69 | 226.3917 | -746832.31 ± 609.4588 | 102154.9460 | 101487.1275 | +6580327.89 ± 4928.83 | ±0.41 |
| ${}^{110}$Zr | 110 | 70 | 232.2361 | -741618.22 ± 611.9202 | 103088.6670 | 102422.1314 | +6507729.81 ± 4883.83 | ±0.42 |
| ${}^{111}$Zr | 111 | 71 | 238.0729 | -735796.93 ± 615.9153 | 104022.3957 | 103359.3654 | +6414806.07 ± 5803.85 | ±0.42 |
| ${}^{112}$Zr | 112 | 72 | 243.9020 | -730516.47 ± 742.4824 | 104956.1320 | 104294.9199 | +6339830.20 ± 6707.44 | ±0.42 |
| ${}^{113}$Zr | 113 | 73 | 249.7237 | -724686.15 ± 373.7386 | 105889.8757 | 105232.4939 | +6246947.21 ± 2850.27 | ±0.42 |

### Niobium (Z = 41)

_38 of 38 isotopes with a framework prediction; 38 of 38 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{79}$Nb | 79 | 38 | 30.7748 | -951704.21 ± 743.8631 | 74162.8179 | 73556.3839 | +8244478.79 ± 6800.39 | ±0.32 |
| ${}^{80}$Nb | 80 | 39 | 37.0085 | -943245.50 ± 613.4217 | 75096.1496 | 74481.1079 | +8257687.95 ± 5365.27 | ±0.32 |
| ${}^{81}$Nb | 81 | 40 | 43.2255 | -935299.66 ± 606.2076 | 76029.4980 | 75404.6619 | +8286438.23 ± 5299.55 | ±0.32 |
| ${}^{82}$Nb | 82 | 41 | 49.4264 | -927483.10 ± 481.2320 | 76962.8626 | 76330.7068 | +8281801.97 ± 3929.49 | ±0.33 |
| ${}^{83}$Nb | 83 | 42 | 55.6114 | -920036.05 ± 233.0591 | 77896.2430 | 77256.3977 | +8282100.67 ± 2097.95 | ±0.33 |
| ${}^{84}$Nb | 84 | 43 | 61.7811 | -912628.48 ± 0.5702 | 78829.6387 | 78184.3109 | +8253929.66 ± 5.12 | ±0.34 |
| ${}^{85}$Nb | 85 | 44 | 67.9359 | -905679.37 ± 5.6882 | 79763.0493 | 79110.7191 | +8245787.70 ± 51.81 | ±0.34 |
| ${}^{86}$Nb | 86 | 45 | 74.0761 | -898691.18 ± 7.5157 | 80696.4745 | 80039.3589 | +8209906.78 ± 68.70 | ±0.34 |
| ${}^{87}$Nb | 87 | 46 | 80.2022 | -892201.83 ± 9.1443 | 81629.9139 | 80966.1125 | +8198508.79 ± 84.01 | ±0.35 |
| ${}^{88}$Nb | 88 | 47 | 86.3144 | -885581.04 ± 76.6296 | 82563.3671 | 81895.3096 | +8157457.87 ± 705.87 | ±0.35 |
| ${}^{89}$Nb | 89 | 48 | 92.4132 | -879497.29 ± 30.8118 | 83496.8338 | 82822.3495 | +8143747.36 ± 285.30 | ±0.35 |
| ${}^{90}$Nb | 90 | 49 | 98.4988 | -873232.57 ± 4.2741 | 84430.3135 | 83751.8078 | +8101386.23 ± 39.61 | ±0.36 |
| ${}^{91}$Nb | 91 | 50 | 104.5716 | -867471.77 ± 3.7136 | 85363.8061 | 84679.3254 | +8083209.37 ± 34.54 | ±0.36 |
| ${}^{92}$Nb | 92 | 51 | 110.6320 | -861178.73 ± 2.2396 | 86297.3112 | 85611.0043 | +8016573.89 ± 20.84 | ±0.36 |
| ${}^{93}$Nb | 93 | 52 | 116.6802 | -855194.06 ± 1.8467 | 87230.8284 | 86541.7388 | +7962512.03 ± 17.21 | ±0.37 |
| ${}^{94}$Nb | 94 | 53 | 122.7164 | -849056.65 ± 1.8384 | 88164.3576 | 87474.0767 | +7891262.43 ± 17.04 | ±0.37 |
| ${}^{95}$Nb | 95 | 54 | 128.7411 | -843282.49 ± 0.6245 | 89097.8983 | 88405.1536 | +7836022.19 ± 5.74 | ±0.37 |
| ${}^{96}$Nb | 96 | 55 | 134.7545 | -837326.37 ± 0.1738 | 90031.4504 | 89337.8311 | +7764004.03 ± 1.64 | ±0.38 |
| ${}^{97}$Nb | 97 | 56 | 140.7567 | -831720.15 ± 5.0794 | 90965.0136 | 90269.3253 | +7706807.29 ± 47.01 | ±0.38 |
| ${}^{98}$Nb | 98 | 57 | 146.7482 | -825805.25 ± 5.9328 | 91898.5875 | 91202.8976 | +7627937.15 ± 54.84 | ±0.38 |
| ${}^{99}$Nb | 99 | 58 | 152.7291 | -820174.78 ± 14.1392 | 92832.1721 | 92135.5809 | +7560500.78 ± 130.28 | ±0.38 |
| ${}^{100}$Nb | 100 | 59 | 158.6996 | -814353.12 ± 9.3350 | 93765.7669 | 93069.6191 | +7479860.76 ± 85.69 | ±0.39 |
| ${}^{101}$Nb | 101 | 60 | 164.6601 | -808983.06 ± 4.3469 | 94699.3719 | 94002.0130 | +7418552.73 ± 39.88 | ±0.39 |
| ${}^{102}$Nb | 102 | 61 | 170.6107 | -803329.81 ± 2.8925 | 95632.9867 | 94936.1003 | +7340583.77 ± 26.44 | ±0.39 |
| ${}^{103}$Nb | 103 | 62 | 176.5516 | -798064.74 ± 4.5003 | 96566.6112 | 95868.8640 | +7278141.79 ± 41.04 | ±0.39 |
| ${}^{104}$Nb | 104 | 63 | 182.4831 | -792432.76 ± 2.0347 | 97500.2451 | 96803.5758 | +7196731.55 ± 18.43 | ±0.40 |
| ${}^{105}$Nb | 105 | 64 | 188.4054 | -787191.39 ± 4.5542 | 98433.8883 | 97736.9653 | +7130597.64 ± 41.21 | ±0.40 |
| ${}^{106}$Nb | 106 | 65 | 194.3186 | -781587.52 ± 1.5965 | 99367.5405 | 98672.1723 | +7047257.71 ± 14.35 | ±0.40 |
| ${}^{107}$Nb | 107 | 66 | 200.2229 | -776356.88 ± 8.9637 | 100301.2016 | 99606.1453 | +6978046.66 ± 80.54 | ±0.40 |
| ${}^{108}$Nb | 108 | 67 | 206.1186 | -770768.29 ± 9.1644 | 101234.8714 | 100541.8180 | +6893185.16 ± 81.94 | ±0.41 |
| ${}^{109}$Nb | 109 | 68 | 212.0058 | -765580.77 ± 476.3574 | 102168.5496 | 101476.1675 | +6823100.62 ± 4245.49 | ±0.41 |
| ${}^{110}$Nb | 110 | 69 | 217.8846 | -760059.74 ± 923.2052 | 103102.2362 | 102412.0415 | +6739389.75 ± 8186.00 | ±0.41 |
| ${}^{111}$Nb | 111 | 70 | 223.7554 | -754856.61 ± 364.8304 | 104035.9309 | 103346.8853 | +6667308.83 ± 2902.28 | ±0.41 |
| ${}^{112}$Nb | 112 | 71 | 229.6181 | -749307.69 ± 366.8379 | 104969.6335 | 104283.2697 | +6581725.21 ± 2876.21 | ±0.42 |
| ${}^{113}$Nb | 113 | 72 | 235.4730 | -744095.26 ± 491.2195 | 105903.3440 | 105218.6239 | +6507594.15 ± 3797.91 | ±0.42 |
| ${}^{114}$Nb | 114 | 73 | 241.3203 | -738564.30 ± 494.0101 | 106837.0622 | 106155.3679 | +6421665.39 ± 4712.08 | ±0.42 |
| ${}^{115}$Nb | 115 | 74 | 247.1601 | -733380.72 ± 496.2164 | 107770.7878 | 107090.9420 | +6348304.15 ± 4670.91 | ±0.42 |
| ${}^{116}$Nb | 116 | 75 | 252.9925 | -727787.13 ± 374.4383 | 108704.5209 | 108028.0856 | +6261661.34 ± 2776.51 | ±0.42 |

### Molybdenum (Z = 42)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{81}$Mo | 81 | 39 | 27.3453 | -958083.36 ± 744.9714 | 76044.5959 | 75419.5621 | +8287422.23 ± 6632.40 | ±0.32 |
| ${}^{82}$Mo | 82 | 40 | 33.5977 | -949806.67 ± 612.5199 | 76977.9089 | 76342.1465 | +8327803.97 ± 5234.47 | ±0.32 |
| ${}^{83}$Mo | 83 | 41 | 39.8335 | -941714.60 ± 607.2383 | 77911.2385 | 77267.6706 | +8329070.56 ± 5183.83 | ±0.32 |
| ${}^{84}$Mo | 84 | 42 | 46.0532 | -934143.84 ± 480.4805 | 78844.5843 | 78191.3346 | +8354501.88 ± 3812.16 | ±0.33 |
| ${}^{85}$Mo | 85 | 43 | 52.2572 | -926472.17 ± 22.2811 | 79777.9457 | 79119.4891 | +8322306.48 ± 200.15 | ±0.33 |
| ${}^{86}$Mo | 86 | 44 | 58.4459 | -919427.83 ± 4.0428 | 80711.3224 | 80044.3820 | +8332132.84 ± 36.62 | ±0.34 |
| ${}^{87}$Mo | 87 | 45 | 64.6197 | -912229.03 ± 3.8760 | 81644.7140 | 80973.1022 | +8294258.33 ± 35.28 | ±0.34 |
| ${}^{88}$Mo | 88 | 46 | 70.7790 | -905641.08 ± 5.0916 | 82578.1202 | 81898.7946 | +8294695.80 ± 46.63 | ±0.34 |
| ${}^{89}$Mo | 89 | 47 | 76.9241 | -898851.05 ± 5.1492 | 83511.5404 | 82827.9603 | +8253011.94 ± 47.23 | ±0.35 |
| ${}^{90}$Mo | 90 | 48 | 83.0555 | -892656.05 ± 4.4783 | 84444.9745 | 83754.2968 | +8246474.48 ± 41.34 | ±0.35 |
| ${}^{91}$Mo | 91 | 49 | 89.1734 | -886235.19 ± 7.9641 | 85378.4220 | 84683.7546 | +8203077.42 ± 73.65 | ±0.35 |
| ${}^{92}$Mo | 92 | 50 | 95.2782 | -880380.57 ± 0.1964 | 86311.8826 | 85610.6490 | +8190963.11 ± 1.83 | ±0.36 |
| ${}^{93}$Mo | 93 | 51 | 101.3702 | -874008.69 ± 0.2312 | 87245.3560 | 86542.1446 | +8125653.48 ± 2.08 | ±0.36 |
| ${}^{94}$Mo | 94 | 52 | 107.4497 | -868039.92 ± 0.1732 | 88178.8420 | 87472.0317 | +8080414.68 ± 1.61 | ±0.36 |
| ${}^{95}$Mo | 95 | 53 | 113.5171 | -861838.96 ± 0.1503 | 89112.3401 | 88404.2280 | +8009934.62 ± 1.39 | ±0.37 |
| ${}^{96}$Mo | 96 | 54 | 119.5725 | -856072.55 ± 0.1502 | 90045.8501 | 89334.6391 | +7961200.95 ± 1.33 | ±0.37 |
| ${}^{97}$Mo | 97 | 55 | 125.6162 | -850029.08 ± 0.1969 | 90979.3717 | 90267.3834 | +7887548.52 ± 1.82 | ±0.37 |
| ${}^{98}$Mo | 98 | 56 | 131.6487 | -844432.27 ± 0.2084 | 91912.9047 | 91198.3062 | +7835655.92 ± 1.90 | ±0.37 |
| ${}^{99}$Mo | 99 | 57 | 137.6700 | -838448.15 ± 0.2672 | 92846.4488 | 92131.9462 | +7755210.96 ± 2.48 | ±0.38 |
| ${}^{100}$Mo | 100 | 58 | 143.6804 | -833020.26 ± 0.3486 | 93780.0038 | 93063.2173 | +7702145.67 ± 3.22 | ±0.38 |
| ${}^{101}$Mo | 101 | 59 | 149.6803 | -827131.97 ± 0.3616 | 94713.5694 | 93997.3845 | +7619199.69 ± 3.28 | ±0.38 |
| ${}^{102}$Mo | 102 | 60 | 155.6698 | -821883.39 ± 9.5000 | 95647.1453 | 94928.8377 | +7566800.68 ± 87.49 | ±0.39 |
| ${}^{103}$Mo | 103 | 61 | 161.6491 | -816191.18 ± 10.4822 | 96580.7314 | 95862.9384 | +7487701.22 ± 96.20 | ±0.39 |
| ${}^{104}$Mo | 104 | 62 | 167.6185 | -811006.77 ± 10.0494 | 97514.3274 | 96795.0430 | +7431004.09 ± 92.06 | ±0.39 |
| ${}^{105}$Mo | 105 | 63 | 173.5782 | -805396.98 ± 10.1473 | 98447.9331 | 97729.5501 | +7350724.68 ± 92.65 | ±0.39 |
| ${}^{106}$Mo | 106 | 64 | 179.5284 | -800264.12 ± 10.1539 | 99381.5483 | 98662.2470 | +7290542.94 ± 92.53 | ±0.40 |
| ${}^{107}$Mo | 107 | 65 | 185.4693 | -794679.78 ± 10.2106 | 100315.1729 | 99597.3241 | +7207510.30 ± 92.60 | ±0.40 |
| ${}^{108}$Mo | 108 | 66 | 191.4011 | -789575.00 ± 10.1399 | 101248.8065 | 100530.6139 | +7144018.72 ± 91.74 | ±0.40 |
| ${}^{109}$Mo | 109 | 67 | 197.3240 | -784008.83 ± 12.2414 | 102182.4490 | 101466.1980 | +7059011.08 ± 110.16 | ±0.40 |
| ${}^{110}$Mo | 110 | 68 | 203.2381 | -778974.19 ± 26.3419 | 103116.1003 | 102399.8156 | +6994980.59 ± 236.51 | ±0.41 |
| ${}^{111}$Mo | 111 | 69 | 209.1437 | -773408.14 ± 13.6255 | 104049.7602 | 103335.9057 | +6908096.92 ± 121.72 | ±0.41 |
| ${}^{112}$Mo | 112 | 70 | 215.0409 | -768422.58 ± 241.2254 | 104983.4284 | 104269.8599 | +6843477.66 ± 1920.70 | ±0.41 |
| ${}^{113}$Mo | 113 | 71 | 220.9299 | -762899.33 ± 363.8128 | 105917.1048 | 105206.1838 | +6757406.83 ± 2850.98 | ±0.41 |
| ${}^{114}$Mo | 114 | 72 | 226.8109 | -757930.52 ± 365.0079 | 106850.7893 | 106140.6475 | +6690573.07 ± 2825.88 | ±0.41 |
| ${}^{115}$Mo | 115 | 73 | 232.6839 | -752436.25 ± 367.0623 | 107784.4816 | 107077.2723 | +6604663.54 ± 3731.99 | ±0.42 |
| ${}^{116}$Mo | 116 | 74 | 238.5492 | -747456.84 ± 491.2195 | 108718.1818 | 108012.1058 | +6537007.58 ± 4631.08 | ±0.42 |
| ${}^{117}$Mo | 117 | 75 | 244.4070 | -741977.71 ± 494.0711 | 109651.8895 | 108949.1209 | +6450429.11 ± 4591.25 | ±0.42 |
| ${}^{118}$Mo | 118 | 76 | 250.2573 | -737098.77 ± 495.8473 | 110585.6046 | 109883.9339 | +6385562.25 ± 4552.19 | ±0.42 |
| ${}^{119}$Mo | 119 | 77 | 256.1002 | -731624.53 ± 374.1115 | 111519.3270 | 110821.2182 | +6299415.19 ± 2706.53 | ±0.42 |

### Technetium (Z = 43)

_40 of 40 isotopes with a framework prediction; 40 of 40 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{83}$Tc | 83 | 40 | 23.7329 | -964448.84 ± 745.9903 | 77926.5569 | 77282.6910 | +8331307.66 ± 6472.50 | ±0.32 |
| ${}^{84}$Tc | 84 | 41 | 30.0037 | -956011.40 ± 615.7635 | 78859.8514 | 78207.8044 | +8337365.36 ± 5109.60 | ±0.32 |
| ${}^{85}$Tc | 85 | 42 | 36.2582 | -948074.67 ± 608.6427 | 79793.1624 | 79131.1488 | +8366030.26 ± 5049.98 | ±0.32 |
| ${}^{86}$Tc | 86 | 43 | 42.4965 | -940320.57 ± 362.3188 | 80726.4894 | 80056.9226 | +8363634.47 ± 3746.60 | ±0.33 |
| ${}^{87}$Tc | 87 | 44 | 48.7193 | -932917.01 ± 5.7740 | 81659.8321 | 80982.2970 | +8366460.10 ± 51.76 | ±0.33 |
| ${}^{88}$Tc | 88 | 45 | 54.9268 | -925604.24 ± 5.5543 | 82593.1900 | 81909.8108 | +8343069.05 ± 50.04 | ±0.34 |
| ${}^{89}$Tc | 89 | 46 | 61.1195 | -918735.05 ± 5.0766 | 83526.5628 | 82835.5804 | +8341613.62 ± 46.10 | ±0.34 |
| ${}^{90}$Tc | 90 | 47 | 67.2977 | -911856.63 ± 1.3438 | 84459.9500 | 83763.7446 | +8311535.74 ± 12.23 | ±0.34 |
| ${}^{91}$Tc | 91 | 48 | 73.4618 | -905434.61 ± 3.0457 | 85393.3513 | 84689.9768 | +8305286.73 ± 27.89 | ±0.35 |
| ${}^{92}$Tc | 92 | 49 | 79.6121 | -898949.67 ± 3.9353 | 86326.7664 | 85618.5318 | +8271977.53 ± 36.23 | ±0.35 |
| ${}^{93}$Tc | 93 | 50 | 85.7490 | -892893.77 ± 1.2662 | 87260.1949 | 86545.3455 | +8259824.91 ± 11.69 | ±0.35 |
| ${}^{94}$Tc | 94 | 51 | 91.8728 | -886467.64 ± 5.0298 | 88193.6366 | 87476.2874 | +8200498.23 ± 46.53 | ±0.36 |
| ${}^{95}$Tc | 95 | 52 | 97.9838 | -880384.39 ± 6.2046 | 89127.0910 | 88405.9185 | +8157513.60 ± 57.46 | ±0.36 |
| ${}^{96}$Tc | 96 | 53 | 104.0823 | -874148.88 ± 6.2218 | 90060.5579 | 89337.6123 | +8092286.89 ± 57.60 | ±0.36 |
| ${}^{97}$Tc | 97 | 54 | 110.1686 | -868298.35 ± 4.9283 | 90994.0370 | 90267.7036 | +8046437.03 ± 45.61 | ±0.36 |
| ${}^{98}$Tc | 98 | 55 | 116.2430 | -862235.50 ± 4.0070 | 91927.5281 | 91199.9900 | +7977392.42 ± 37.06 | ±0.37 |
| ${}^{99}$Tc | 99 | 56 | 122.3057 | -856574.50 ± 1.0681 | 92861.0307 | 92130.5884 | +7928336.98 ± 9.85 | ±0.37 |
| ${}^{100}$Tc | 100 | 57 | 128.3571 | -850662.82 ± 1.5707 | 93794.5448 | 93063.3894 | +7856531.02 ± 14.51 | ±0.37 |
| ${}^{101}$Tc | 101 | 58 | 134.3973 | -845147.79 ± 27.6616 | 94728.0700 | 93994.5599 | +7803751.12 ± 255.36 | ±0.38 |
| ${}^{102}$Tc | 102 | 59 | 140.4266 | -839366.76 ± 10.4893 | 95661.6061 | 94927.8257 | +7729877.54 ± 96.56 | ±0.38 |
| ${}^{103}$Tc | 103 | 60 | 146.4453 | -834020.35 ± 11.1136 | 96595.1529 | 95859.2888 | +7676502.81 ± 102.33 | ±0.38 |
| ${}^{104}$Tc | 104 | 61 | 152.4536 | -828371.22 ± 28.0174 | 97528.7100 | 96792.8878 | +7602027.49 ± 257.10 | ±0.38 |
| ${}^{105}$Tc | 105 | 62 | 158.4517 | -823183.03 ± 39.3457 | 98462.2773 | 97724.5946 | +7548588.62 ± 360.84 | ±0.39 |
| ${}^{106}$Tc | 106 | 63 | 164.4398 | -817632.60 ± 13.5895 | 99395.8547 | 98658.5987 | +7472799.39 ± 124.16 | ±0.39 |
| ${}^{107}$Tc | 107 | 64 | 170.4181 | -812467.68 ± 9.5492 | 100329.4417 | 99591.1191 | +7413538.49 ± 87.08 | ±0.39 |
| ${}^{108}$Tc | 108 | 65 | 176.3869 | -807013.16 ± 9.5949 | 101263.0383 | 100525.4404 | +7337425.98 ± 87.22 | ±0.39 |
| ${}^{109}$Tc | 109 | 66 | 182.3464 | -801886.91 ± 10.5043 | 102196.6443 | 101458.5745 | +7274593.16 ± 95.30 | ±0.40 |
| ${}^{110}$Tc | 110 | 67 | 188.2967 | -796488.55 ± 10.2601 | 103130.2595 | 102393.3168 | +7197175.06 ± 92.75 | ±0.40 |
| ${}^{111}$Tc | 111 | 68 | 194.2380 | -791433.54 ± 11.3586 | 104063.8836 | 103326.8208 | +7133314.93 ± 102.40 | ±0.40 |
| ${}^{112}$Tc | 112 | 69 | 200.1705 | -786052.52 ± 5.8897 | 104997.5165 | 104262.0807 | +7053722.85 ± 52.89 | ±0.40 |
| ${}^{113}$Tc | 113 | 70 | 206.0944 | -781037.10 ± 3.5657 | 105931.1580 | 105196.0222 | +6988247.75 ± 31.88 | ±0.41 |
| ${}^{114}$Tc | 114 | 71 | 212.0098 | -775672.28 ± 458.3089 | 106864.8080 | 106131.7275 | +6907269.89 ± 4081.20 | ±0.41 |
| ${}^{115}$Tc | 115 | 72 | 217.9170 | -770700.61 ± 242.0136 | 107798.4663 | 107066.0254 | +6841020.21 ± 1827.04 | ±0.41 |
| ${}^{116}$Tc | 116 | 73 | 223.8160 | -765359.56 ± 364.8304 | 108732.1327 | 108002.1025 | +6759406.98 ± 2759.93 | ±0.41 |
| ${}^{117}$Tc | 117 | 74 | 229.7071 | -760426.05 ± 366.0769 | 109665.8070 | 108936.6705 | +6693214.19 ± 3668.29 | ±0.41 |
| ${}^{118}$Tc | 118 | 75 | 235.5904 | -755117.31 ± 367.9627 | 110599.4891 | 109873.0140 | +6611952.52 ± 3637.03 | ±0.42 |
| ${}^{119}$Tc | 119 | 76 | 241.4660 | -750292.15 ± 492.2471 | 111533.1789 | 110807.6286 | +6547837.50 ± 4514.24 | ±0.42 |
| ${}^{120}$Tc | 120 | 77 | 247.3341 | -745005.88 ± 494.8658 | 112466.8763 | 111744.2925 | +6466404.24 ± 4476.40 | ±0.42 |
| ${}^{121}$Tc | 121 | 78 | 253.1948 | -740188.82 ± 496.6476 | 113400.5809 | 112679.2462 | +6401664.98 ± 4439.26 | ±0.42 |
| ${}^{122}$Tc | 122 | 79 | 259.0483 | -734946.08 ± 249.6567 | 114334.2929 | 113615.9753 | +6322329.29 ± 2639.96 | ±0.42 |

### Ruthenium (Z = 44)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{85}$Ru | 85 | 41 | 19.9388 | -970776.90 ± 747.4773 | 79808.6994 | 79146.3685 | +8368431.33 ± 6320.09 | ±0.32 |
| ${}^{86}$Ru | 86 | 42 | 26.2280 | -962501.30 ± 614.7793 | 80741.9756 | 80068.7228 | +8408437.52 ± 4990.85 | ±0.32 |
| ${}^{87}$Ru | 87 | 43 | 32.5009 | -954447.85 ± 609.6817 | 81675.2682 | 80994.2572 | +8408139.52 ± 4933.82 | ±0.32 |
| ${}^{88}$Ru | 88 | 44 | 38.7578 | -946923.46 ± 361.5329 | 82608.5767 | 81917.1415 | +8440666.08 ± 3661.52 | ±0.33 |
| ${}^{89}$Ru | 89 | 45 | 44.9991 | -939378.28 ± 32.6244 | 83541.9008 | 82844.6058 | +8416902.88 ± 292.34 | ±0.33 |
| ${}^{90}$Ru | 90 | 46 | 51.2253 | -932320.40 ± 4.9228 | 84475.2401 | 83769.5855 | +8423755.69 ± 44.52 | ±0.33 |
| ${}^{91}$Ru | 91 | 47 | 57.4367 | -925242.51 ± 2.8900 | 85408.5941 | 84697.7236 | +8393029.45 ± 26.22 | ±0.34 |
| ${}^{92}$Ru | 92 | 48 | 63.6336 | -918672.76 ± 3.4686 | 86341.9626 | 85623.1563 | +8394998.02 ± 31.73 | ±0.34 |
| ${}^{93}$Ru | 93 | 49 | 69.8165 | -912006.28 ± 2.6021 | 87275.3451 | 86551.7349 | +8360435.27 ± 23.85 | ±0.35 |
| ${}^{94}$Ru | 94 | 50 | 75.9856 | -905825.98 ± 3.8911 | 88208.7414 | 87477.8621 | +8355019.36 ± 35.93 | ±0.35 |
| ${}^{95}$Ru | 95 | 51 | 82.1414 | -899313.06 ± 11.6449 | 89142.1511 | 88408.4821 | +8298626.52 ± 107.47 | ±0.35 |
| ${}^{96}$Ru | 96 | 52 | 88.2840 | -893183.75 ± 0.2091 | 90075.5739 | 89337.3536 | +8263288.01 ± 1.90 | ±0.36 |
| ${}^{97}$Ru | 97 | 53 | 94.4139 | -886877.37 ± 3.3123 | 91009.0094 | 90268.8075 | +8199974.66 ± 30.60 | ±0.36 |
| ${}^{98}$Ru | 98 | 54 | 100.5312 | -880998.68 ± 7.6447 | 91942.4575 | 91198.1973 | +8160909.23 ± 70.85 | ±0.36 |
| ${}^{99}$Ru | 99 | 55 | 106.6364 | -874878.52 ± 0.4066 | 92875.9178 | 92130.2909 | +8093178.63 ± 3.72 | ±0.36 |
| ${}^{100}$Ru | 100 | 56 | 112.7296 | -869213.52 ± 0.3945 | 93809.3900 | 93060.1830 | +8050779.55 ± 3.67 | ±0.37 |
| ${}^{101}$Ru | 101 | 57 | 118.8111 | -863237.12 ± 0.4767 | 94742.8739 | 93992.9464 | +7978551.01 ± 4.39 | ±0.37 |
| ${}^{102}$Ru | 102 | 58 | 124.8812 | -857759.37 ± 0.4763 | 95676.3692 | 94923.2921 | +7933532.51 ± 4.38 | ±0.37 |
| ${}^{103}$Ru | 103 | 59 | 130.9402 | -851909.35 ± 0.5009 | 96609.8756 | 95856.6255 | +7858091.13 ± 4.60 | ±0.38 |
| ${}^{104}$Ru | 104 | 60 | 136.9883 | -846613.06 ± 2.7948 | 97543.3930 | 96787.2910 | +7811996.20 ± 25.81 | ±0.38 |
| ${}^{105}$Ru | 105 | 61 | 143.0257 | -840905.76 ± 2.7798 | 98476.9210 | 97720.9463 | +7736055.48 ± 25.57 | ±0.38 |
| ${}^{106}$Ru | 106 | 62 | 149.0526 | -835747.41 ± 5.9456 | 99410.4595 | 98652.0517 | +7687703.83 ± 54.64 | ±0.38 |
| ${}^{107}$Ru | 107 | 63 | 155.0693 | -830167.18 ± 9.5039 | 100344.0082 | 99586.0065 | +7611528.05 ± 87.08 | ±0.39 |
| ${}^{108}$Ru | 108 | 64 | 161.0760 | -825096.19 ± 9.4286 | 101277.5669 | 100517.7018 | +7559515.73 ± 86.35 | ±0.39 |
| ${}^{109}$Ru | 109 | 65 | 167.0729 | -819593.03 ± 9.6631 | 102211.1355 | 101452.1188 | +7481525.68 ± 88.25 | ±0.39 |
| ${}^{110}$Ru | 110 | 66 | 173.0602 | -814610.38 ± 9.5566 | 103144.7136 | 102384.2788 | +7427261.81 ± 87.16 | ±0.39 |
| ${}^{111}$Ru | 111 | 67 | 179.0380 | -809184.51 ± 10.3159 | 104078.3012 | 103319.0602 | +7348508.44 ± 93.71 | ±0.40 |
| ${}^{112}$Ru | 112 | 68 | 185.0067 | -804266.15 ± 10.1549 | 105011.8979 | 104251.7087 | +7291863.18 ± 92.08 | ±0.40 |
| ${}^{113}$Ru | 113 | 69 | 190.9663 | -798877.70 ± 40.3204 | 105945.5037 | 105186.9659 | +7211329.16 ± 363.94 | ±0.40 |
| ${}^{114}$Ru | 114 | 70 | 196.9171 | -794004.31 ± 3.7208 | 106879.1184 | 106120.1066 | +7152384.25 ± 33.50 | ±0.40 |
| ${}^{115}$Ru | 115 | 71 | 202.8592 | -788662.73 ± 26.2136 | 107812.7417 | 107055.7166 | +7071318.67 ± 235.07 | ±0.40 |
| ${}^{116}$Ru | 116 | 72 | 208.7928 | -783840.19 ± 3.8550 | 108746.3736 | 107989.2471 | +7011128.08 ± 34.50 | ±0.41 |
| ${}^{117}$Ru | 117 | 73 | 214.7180 | -778506.69 ± 446.8134 | 109680.0137 | 108925.3203 | +6928540.31 ± 3976.53 | ±0.41 |
| ${}^{118}$Ru | 118 | 74 | 220.6351 | -773715.51 ± 242.0428 | 110613.6621 | 109859.3043 | +6866581.34 ± 1822.98 | ±0.41 |
| ${}^{119}$Ru | 119 | 75 | 226.5441 | -768402.44 ± 364.9635 | 111547.3185 | 110795.7185 | +6783655.48 ± 2707.15 | ±0.41 |
| ${}^{120}$Ru | 120 | 76 | 232.4453 | -763746.33 ± 365.8983 | 112480.9828 | 111729.5721 | +6725262.21 ± 3576.59 | ±0.41 |
| ${}^{121}$Ru | 121 | 77 | 238.3387 | -758491.75 ± 367.8274 | 113414.6547 | 112666.1661 | +6643419.69 ± 3546.86 | ±0.42 |
| ${}^{122}$Ru | 122 | 78 | 244.2245 | -753831.71 ± 491.8839 | 114348.3343 | 113600.5003 | +6583016.52 ± 4403.26 | ±0.42 |
| ${}^{123}$Ru | 123 | 79 | 250.1030 | -748626.86 ± 494.4987 | 115282.0213 | 114537.2248 | +6502659.25 ± 4367.25 | ±0.42 |
| ${}^{124}$Ru | 124 | 80 | 255.9740 | -744041.31 ± 619.9628 | 116215.7157 | 115471.6792 | +6443454.20 ± 5195.06 | ±0.42 |
| ${}^{125}$Ru | 125 | 81 | 261.8380 | -738912.65 ± 249.2833 | 117149.4172 | 116408.3934 | +6365724.63 ± 2576.63 | ±0.42 |

### Rhodium (Z = 45)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{88}$Rh | 88 | 43 | 22.2719 | -968715.70 ± 618.0470 | 82624.2802 | 81934.6210 | +8417189.89 ± 4877.19 | ±0.32 |
| ${}^{89}$Rh | 89 | 44 | 28.5631 | -960809.22 ± 488.4601 | 83557.5545 | 82857.3246 | +8451032.57 ± 4350.71 | ±0.32 |
| ${}^{90}$Rh | 90 | 45 | 34.8383 | -953102.43 ± 242.3068 | 84490.8447 | 83782.8357 | +8450525.50 ± 2390.36 | ±0.33 |
| ${}^{91}$Rh | 91 | 46 | 41.0981 | -945769.99 ± 360.2305 | 85424.1503 | 84707.3939 | +8461556.91 ± 3518.91 | ±0.33 |
| ${}^{92}$Rh | 92 | 47 | 47.3428 | -938544.18 ± 5.6847 | 86357.4711 | 85634.4584 | +8443010.35 ± 51.12 | ±0.33 |
| ${}^{93}$Rh | 93 | 48 | 53.5727 | -931705.67 ± 3.3551 | 87290.8066 | 86559.9398 | +8443475.32 ± 30.36 | ±0.34 |
| ${}^{94}$Rh | 94 | 49 | 59.7883 | -924927.39 ± 4.2373 | 88224.1564 | 87487.5381 | +8419693.95 ± 38.62 | ±0.34 |
| ${}^{95}$Rh | 95 | 50 | 65.9898 | -918522.10 ± 4.7974 | 89157.5203 | 88413.5992 | +8414102.60 ± 43.94 | ±0.34 |
| ${}^{96}$Rh | 96 | 51 | 72.1776 | -911906.43 ± 12.2090 | 90090.8980 | 89343.7462 | +8362663.99 ± 111.94 | ±0.35 |
| ${}^{97}$Rh | 97 | 52 | 78.3520 | -905635.23 ± 42.7108 | 91024.2890 | 90272.3305 | +8329888.75 ± 392.84 | ±0.35 |
| ${}^{98}$Rh | 98 | 53 | 84.5133 | -899264.04 ± 14.1926 | 91957.6931 | 91203.2469 | +8272140.99 ± 130.55 | ±0.35 |
| ${}^{99}$Rh | 99 | 54 | 90.6619 | -893268.59 ± 22.9016 | 92891.1099 | 92132.3317 | +8235742.89 ± 211.12 | ±0.36 |
| ${}^{100}$Rh | 100 | 55 | 96.7979 | -887118.42 ± 21.1424 | 93824.5393 | 93063.8192 | +8174176.38 ± 194.76 | ±0.36 |
| ${}^{101}$Rh | 101 | 56 | 102.9217 | -881345.90 ± 6.7302 | 94757.9809 | 93993.4920 | +8133423.27 ± 62.14 | ±0.36 |
| ${}^{102}$Rh | 102 | 57 | 109.0336 | -875369.06 ± 7.3219 | 95691.4344 | 94925.6153 | +8067571.32 ± 67.51 | ±0.37 |
| ${}^{103}$Rh | 103 | 58 | 115.1339 | -869783.40 ± 2.5978 | 96624.8996 | 95855.8610 | +8022865.38 ± 24.00 | ±0.37 |
| ${}^{104}$Rh | 104 | 59 | 121.2226 | -863973.73 ± 2.5791 | 97558.3763 | 96788.4274 | +7954967.97 ± 23.78 | ±0.37 |
| ${}^{105}$Rh | 105 | 60 | 127.3002 | -858576.35 ± 2.7763 | 98491.8641 | 97719.0296 | +7908740.84 ± 25.59 | ±0.37 |
| ${}^{106}$Rh | 106 | 61 | 133.3669 | -852912.27 ± 5.9388 | 99425.3629 | 98652.0123 | +7839176.35 ± 54.63 | ±0.38 |
| ${}^{107}$Rh | 107 | 62 | 139.4229 | -847673.42 ± 13.1633 | 100358.8723 | 99583.0054 | +7791158.12 ± 121.01 | ±0.38 |
| ${}^{108}$Rh | 108 | 63 | 145.4683 | -842144.41 ± 15.1887 | 101292.3923 | 100516.3320 | +7720737.70 ± 139.25 | ±0.38 |
| ${}^{109}$Rh | 109 | 64 | 151.5035 | -837017.14 ± 4.3503 | 102225.9225 | 101447.8581 | +7669599.54 ± 39.81 | ±0.38 |
| ${}^{110}$Rh | 110 | 65 | 157.5287 | -831604.42 ± 19.0375 | 103159.4628 | 102381.5227 | +7598441.95 ± 173.90 | ±0.39 |
| ${}^{111}$Rh | 111 | 66 | 163.5440 | -826573.22 ± 7.2626 | 104093.0129 | 103313.5416 | +7544715.27 ± 66.32 | ±0.39 |
| ${}^{112}$Rh | 112 | 67 | 169.5496 | -821246.92 ± 46.4761 | 105026.5727 | 104247.6086 | +7472249.16 ± 422.89 | ±0.39 |
| ${}^{113}$Rh | 113 | 68 | 175.5458 | -816301.69 ± 7.4614 | 105960.1419 | 105180.0668 | +7416568.05 ± 67.80 | ±0.39 |
| ${}^{114}$Rh | 114 | 69 | 181.5328 | -811028.37 ± 74.4901 | 106893.7204 | 106114.6175 | +7342087.90 ± 674.38 | ±0.40 |
| ${}^{115}$Rh | 115 | 70 | 187.5106 | -806135.54 ± 7.5618 | 107827.3080 | 107047.5927 | +7283818.93 ± 68.37 | ±0.40 |
| ${}^{116}$Rh | 116 | 71 | 193.4795 | -800906.65 ± 75.9763 | 108760.9045 | 107982.5803 | +7207867.98 ± 683.73 | ±0.40 |
| ${}^{117}$Rh | 117 | 72 | 199.4397 | -796081.28 ± 9.0917 | 109694.5097 | 108915.9134 | +7148600.20 ± 81.66 | ±0.40 |
| ${}^{118}$Rh | 118 | 73 | 205.3914 | -790864.44 ± 24.6790 | 110628.1235 | 109851.4174 | +7070514.95 ± 220.62 | ±0.41 |
| ${}^{119}$Rh | 119 | 74 | 211.3346 | -786121.13 ± 9.4299 | 111561.7457 | 110784.9755 | +7011511.61 ± 84.08 | ±0.41 |
| ${}^{120}$Rh | 120 | 75 | 217.2696 | -780960.60 ± 241.9550 | 112495.3761 | 111720.6726 | +6934289.89 ± 1792.61 | ±0.41 |
| ${}^{121}$Rh | 121 | 76 | 223.1965 | -776283.18 ± 620.8916 | 113429.0146 | 112654.5364 | +6874807.34 ± 5498.61 | ±0.41 |
| ${}^{122}$Rh | 122 | 77 | 229.1154 | -771199.42 ± 243.6647 | 114362.6611 | 113590.4011 | +6798638.08 ± 2640.55 | ±0.41 |
| ${}^{123}$Rh | 123 | 78 | 235.0266 | -766550.37 ± 366.5241 | 115296.3154 | 114524.5844 | +6738561.53 ± 3489.30 | ±0.42 |
| ${}^{124}$Rh | 124 | 79 | 240.9301 | -761538.46 ± 368.1885 | 116229.9773 | 115460.5590 | +6663905.69 ± 3461.02 | ±0.42 |
| ${}^{125}$Rh | 125 | 80 | 246.8261 | -756941.31 ± 492.3683 | 117163.6467 | 116394.9333 | +6604354.58 ± 4297.54 | ±0.42 |
| ${}^{126}$Rh | 126 | 81 | 252.7147 | -751988.08 ± 494.6210 | 118097.3235 | 117331.0569 | +6530807.73 ± 4263.26 | ±0.42 |
| ${}^{127}$Rh | 127 | 82 | 258.5961 | -747370.98 ± 620.3474 | 119031.0075 | 118266.0208 | +6468355.70 ± 5072.31 | ±0.42 |
| ${}^{128}$Rh | 128 | 83 | 264.4704 | -742050.57 ± 249.6879 | 119964.6987 | 119203.9050 | +6382288.28 ± 2516.20 | ±0.42 |

### Palladium (Z = 46)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{90}$Pd | 90 | 44 | 18.1368 | -975160.83 ± 493.0359 | 84506.7639 | 83794.7597 | +8497000.43 ± 4768.93 | ±0.32 |
| ${}^{91}$Pd | 91 | 45 | 24.4461 | -967171.16 ± 611.0229 | 85440.0200 | 84719.7939 | +8501272.55 ± 4991.73 | ±0.32 |
| ${}^{92}$Pd | 92 | 46 | 30.7396 | -959625.03 ± 453.1773 | 86373.2919 | 85642.6784 | +8530950.90 ± 4028.68 | ±0.33 |
| ${}^{93}$Pd | 93 | 47 | 37.0176 | -952150.48 ± 478.2797 | 87306.5793 | 86569.9698 | +8508833.39 ± 4274.10 | ±0.33 |
| ${}^{94}$Pd | 94 | 48 | 43.2807 | -945132.26 ± 5.4340 | 88239.8817 | 87494.3435 | +8520987.60 ± 48.99 | ±0.33 |
| ${}^{95}$Pd | 95 | 49 | 49.5290 | -938146.97 ± 3.7846 | 89173.1988 | 88421.9739 | +8495906.57 ± 34.27 | ±0.34 |
| ${}^{96}$Pd | 96 | 50 | 55.7630 | -931582.65 ± 5.1472 | 90106.5302 | 89347.2505 | +8498075.23 ± 46.94 | ±0.34 |
| ${}^{97}$Pd | 97 | 51 | 61.9830 | -924845.02 ± 5.8689 | 91039.8756 | 90277.1222 | +8449022.30 ± 53.65 | ±0.34 |
| ${}^{98}$Pd | 98 | 52 | 68.1893 | -918465.26 ± 5.6715 | 91973.2347 | 91205.1012 | +8422046.05 ± 51.99 | ±0.35 |
| ${}^{99}$Pd | 99 | 53 | 74.3822 | -912000.27 ± 6.0436 | 92906.6072 | 92135.7334 | +8366719.30 ± 55.42 | ±0.35 |
| ${}^{100}$Pd | 100 | 54 | 80.5621 | -905924.56 ± 20.5989 | 93839.9928 | 93064.1977 | +8336128.14 ± 189.51 | ±0.35 |
| ${}^{101}$Pd | 101 | 55 | 86.7292 | -899694.11 ± 5.3032 | 94773.3911 | 93995.4723 | +8276130.27 ± 48.81 | ±0.36 |
| ${}^{102}$Pd | 102 | 56 | 92.8838 | -893870.04 ± 0.4778 | 95706.8019 | 94924.4956 | +8241353.31 ± 4.41 | ±0.36 |
| ${}^{103}$Pd | 103 | 57 | 99.0262 | -887829.01 ± 0.9917 | 96640.2250 | 95856.4357 | +8176699.35 ± 9.15 | ±0.36 |
| ${}^{104}$Pd | 104 | 58 | 105.1566 | -882220.22 ± 1.5026 | 97573.6599 | 96785.9917 | +8138246.72 ± 13.80 | ±0.37 |
| ${}^{105}$Pd | 105 | 59 | 111.2754 | -876349.46 ± 1.2601 | 98507.1066 | 97718.4630 | +8070569.40 ± 11.65 | ±0.37 |
| ${}^{106}$Pd | 106 | 60 | 117.3827 | -870934.18 ± 1.2121 | 99440.5647 | 98648.4675 | +8029494.15 ± 11.20 | ±0.37 |
| ${}^{107}$Pd | 107 | 61 | 123.4788 | -865200.14 ± 1.3083 | 100374.0341 | 99581.4964 | +7958683.59 ± 12.06 | ±0.37 |
| ${}^{108}$Pd | 108 | 62 | 129.5639 | -859967.01 ± 1.2023 | 101307.5144 | 100511.8390 | +7916235.30 ± 11.02 | ±0.38 |
| ${}^{109}$Pd | 109 | 63 | 135.6383 | -854370.35 ± 1.1937 | 102241.0054 | 101445.2508 | +7844177.53 ± 10.97 | ±0.38 |
| ${}^{110}$Pd | 110 | 64 | 141.7022 | -849283.11 ± 0.6552 | 103174.5069 | 102376.0205 | +7799545.35 ± 5.98 | ±0.38 |
| ${}^{111}$Pd | 111 | 65 | 147.7558 | -843795.79 ± 0.7745 | 104108.0188 | 103309.8596 | +7725875.72 ± 7.08 | ±0.38 |
| ${}^{112}$Pd | 112 | 66 | 153.7993 | -838839.01 ± 6.8539 | 105041.5407 | 104241.0186 | +7679530.87 ± 62.79 | ±0.39 |
| ${}^{113}$Pd | 113 | 67 | 159.8329 | -833448.70 ± 7.2416 | 105975.0725 | 105175.2432 | +7604729.75 ± 66.05 | ±0.39 |
| ${}^{114}$Pd | 114 | 68 | 165.8568 | -828595.31 ± 7.1866 | 106908.6140 | 106106.8375 | +7556313.82 ± 65.48 | ±0.39 |
| ${}^{115}$Pd | 115 | 69 | 171.8712 | -823294.05 ± 13.9281 | 107842.1651 | 107041.3961 | +7480927.78 ± 126.56 | ±0.39 |
| ${}^{116}$Pd | 116 | 70 | 177.8763 | -818515.08 ± 7.2787 | 108775.7254 | 107973.4850 | +7429975.89 ± 66.07 | ±0.40 |
| ${}^{117}$Pd | 117 | 71 | 183.8722 | -813286.02 ± 7.3661 | 109709.2949 | 108908.3862 | +7353966.47 ± 66.61 | ±0.40 |
| ${}^{118}$Pd | 118 | 72 | 189.8592 | -808574.15 ± 2.5103 | 110642.8733 | 109840.9159 | +7301080.92 ± 22.70 | ±0.40 |
| ${}^{119}$Pd | 119 | 73 | 195.8374 | -803357.57 ± 8.2806 | 111576.4605 | 110776.3911 | +7222382.34 ± 74.45 | ±0.40 |
| ${}^{120}$Pd | 120 | 74 | 201.8070 | -798766.48 ± 2.2855 | 112510.0564 | 111709.0128 | +7170804.69 ± 20.55 | ±0.40 |
| ${}^{121}$Pd | 121 | 75 | 207.7681 | -793640.06 ± 3.3290 | 113443.6607 | 112644.6042 | +7093606.03 ± 29.77 | ±0.41 |
| ${}^{122}$Pd | 122 | 76 | 213.7209 | -789090.28 ± 19.2994 | 114377.2733 | 113577.6645 | +7040193.84 ± 172.23 | ±0.41 |
| ${}^{123}$Pd | 123 | 77 | 219.6656 | -784051.71 ± 776.0792 | 115310.8940 | 114513.3450 | +6964681.73 ± 6893.88 | ±0.41 |
| ${}^{124}$Pd | 124 | 78 | 225.6023 | -779523.36 ± 242.3655 | 116244.5228 | 115446.8688 | +6909272.92 ± 2598.09 | ±0.41 |
| ${}^{125}$Pd | 125 | 79 | 231.5311 | -774528.45 ± 365.1856 | 117178.1594 | 116382.8034 | +6833964.92 ± 3433.59 | ±0.41 |
| ${}^{126}$Pd | 126 | 80 | 237.4522 | -770093.78 ± 365.9876 | 118111.8037 | 117316.4669 | +6779412.83 ± 3406.26 | ±0.42 |
| ${}^{127}$Pd | 127 | 81 | 243.3657 | -765163.53 ± 490.1961 | 119045.4556 | 118252.5309 | +6705350.27 ± 4230.03 | ±0.42 |
| ${}^{128}$Pd | 128 | 82 | 249.2718 | -760669.03 ± 491.5817 | 119979.1149 | 119186.8549 | +6647209.47 ± 4196.88 | ±0.42 |
| ${}^{129}$Pd | 129 | 83 | 255.1706 | -755371.43 ± 618.3527 | 120912.7816 | 120124.8592 | +6559194.51 ± 4993.82 | ±0.42 |
| ${}^{130}$Pd | 130 | 84 | 261.0622 | -750413.78 ± 248.5707 | 121846.4554 | 121061.5036 | +6483909.27 ± 2477.59 | ±0.42 |
| ${}^{131}$Pd | 131 | 85 | 266.9467 | -745056.75 ± 250.2189 | 122780.1363 | 121999.9876 | +6394661.70 ± 2458.53 | ±0.43 |

### Silver (Z = 47)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{92}$Ag | 92 | 45 | 13.8240 | -981403.33 ± 495.0495 | 86389.4252 | 85659.9276 | +8516205.09 ± 4665.09 | ±0.32 |
| ${}^{93}$Ag | 93 | 46 | 20.1513 | -973494.73 ± 489.2966 | 87322.6633 | 86582.5521 | +8548041.42 ± 4626.13 | ±0.32 |
| ${}^{94}$Ag | 94 | 47 | 26.4629 | -965826.69 ± 485.5547 | 88255.9172 | 87508.0436 | +8546340.67 ± 4566.56 | ±0.33 |
| ${}^{95}$Ag | 95 | 48 | 32.7591 | -958528.89 ± 481.0583 | 89189.1864 | 88432.0336 | +8561974.04 ± 4518.85 | ±0.33 |
| ${}^{96}$Ag | 96 | 49 | 39.0403 | -951356.99 ± 112.2449 | 90122.4706 | 89358.9223 | +8544734.49 ± 1008.10 | ±0.33 |
| ${}^{97}$Ag | 97 | 50 | 45.3069 | -944548.32 ± 14.7094 | 91055.7694 | 90284.0240 | +8547972.71 ± 133.09 | ±0.34 |
| ${}^{98}$Ag | 98 | 51 | 51.5592 | -937676.66 ± 39.7788 | 91989.0825 | 91213.3557 | +8504530.82 ± 360.77 | ±0.34 |
| ${}^{99}$Ag | 99 | 52 | 57.7975 | -931111.65 ± 7.4692 | 92922.4096 | 92141.2038 | +8478355.12 ± 67.99 | ±0.34 |
| ${}^{100}$Ag | 100 | 53 | 64.0222 | -924546.59 ± 5.8928 | 93855.7504 | 93071.2724 | +8428787.55 ± 53.72 | ±0.35 |
| ${}^{101}$Ag | 101 | 54 | 70.2335 | -918311.03 ± 5.6270 | 94789.1045 | 93999.5701 | +8399340.46 ± 51.46 | ±0.35 |
| ${}^{102}$Ag | 102 | 55 | 76.4318 | -912021.07 ± 9.4045 | 95722.4716 | 94930.1519 | +8346344.56 ± 86.06 | ±0.35 |
| ${}^{103}$Ag | 103 | 56 | 82.6173 | -906050.34 ± 4.6617 | 96655.8516 | 95859.0900 | +8311799.86 ± 42.76 | ±0.36 |
| ${}^{104}$Ag | 104 | 57 | 88.7903 | -899984.26 ± 4.7562 | 97589.2440 | 96790.2703 | +8254689.59 ± 43.57 | ±0.36 |
| ${}^{105}$Ag | 105 | 58 | 94.9511 | -894238.95 ± 5.0641 | 98522.6486 | 97719.8100 | +8215719.32 ± 46.49 | ±0.36 |
| ${}^{106}$Ag | 106 | 59 | 101.0999 | -888377.61 ± 3.3354 | 99456.0651 | 98651.4326 | +8156319.01 ± 30.56 | ±0.36 |
| ${}^{107}$Ag | 107 | 60 | 107.2371 | -882835.24 ± 2.6070 | 100389.4934 | 99581.4624 | +8114271.58 ± 23.91 | ±0.37 |
| ${}^{108}$Ag | 108 | 61 | 113.3628 | -877118.69 ± 2.5872 | 101322.9332 | 100513.7564 | +8050408.06 ± 23.75 | ±0.37 |
| ${}^{109}$Ag | 109 | 62 | 119.4772 | -871767.39 ± 1.3805 | 102256.3841 | 101444.1379 | +8006832.75 ± 12.68 | ±0.37 |
| ${}^{110}$Ag | 110 | 63 | 125.5807 | -866194.52 ± 1.3713 | 103189.8461 | 102376.8941 | +7940775.77 ± 12.56 | ±0.38 |
| ${}^{111}$Ag | 111 | 64 | 131.6734 | -861010.34 ± 1.5349 | 104123.3188 | 103307.6301 | +7895725.63 ± 14.11 | ±0.38 |
| ${}^{112}$Ag | 112 | 65 | 137.7556 | -855571.96 ± 2.5364 | 105056.8020 | 104240.7559 | +7828474.82 ± 23.23 | ±0.38 |
| ${}^{113}$Ag | 113 | 66 | 143.8275 | -850540.22 ± 17.2967 | 105990.2956 | 105171.8069 | +7782396.57 ± 158.24 | ±0.38 |
| ${}^{114}$Ag | 114 | 67 | 149.8892 | -845202.32 ± 4.7093 | 106923.7993 | 106105.3970 | +7713107.21 ± 43.02 | ±0.39 |
| ${}^{115}$Ag | 115 | 68 | 155.9409 | -840292.16 ± 18.7149 | 107857.3130 | 107036.8393 | +7665338.59 ± 170.67 | ±0.39 |
| ${}^{116}$Ag | 116 | 69 | 161.9830 | -835055.47 ± 3.3192 | 108790.8363 | 107970.7734 | +7595230.98 ± 30.20 | ±0.39 |
| ${}^{117}$Ag | 117 | 70 | 168.0155 | -830245.50 ± 13.7125 | 109724.3692 | 108902.6282 | +7545649.21 ± 124.62 | ±0.39 |
| ${}^{118}$Ag | 118 | 71 | 174.0386 | -825121.77 ± 2.5255 | 110657.9115 | 109836.7504 | +7476196.14 ± 22.90 | ±0.39 |
| ${}^{119}$Ag | 119 | 72 | 180.0526 | -820371.73 ± 14.6737 | 111591.4630 | 110769.1526 | +7423640.82 ± 132.72 | ±0.40 |
| ${}^{120}$Ag | 120 | 73 | 186.0576 | -815316.37 ± 4.4429 | 112525.0235 | 111703.6409 | +7353229.63 ± 40.03 | ±0.40 |
| ${}^{121}$Ag | 121 | 74 | 192.0537 | -810646.88 ± 11.9418 | 113458.5928 | 112636.3837 | +7299675.46 ± 107.51 | ±0.40 |
| ${}^{122}$Ag | 122 | 75 | 198.0411 | -805658.49 ± 37.4726 | 114392.1707 | 113571.1745 | +7228913.63 ± 336.28 | ±0.40 |
| ${}^{123}$Ag | 123 | 76 | 204.0200 | -801066.76 ± 31.7943 | 115325.7572 | 114504.2062 | +7174854.93 ± 284.73 | ±0.40 |
| ${}^{124}$Ag | 124 | 77 | 209.9906 | -796185.60 ± 244.1119 | 116259.3521 | 115439.0389 | +7106029.27 ± 2178.67 | ±0.41 |
| ${}^{125}$Ag | 125 | 78 | 215.9530 | -791684.78 ± 417.8305 | 117192.9552 | 116372.2430 | +7052473.29 ± 3722.06 | ±0.41 |
| ${}^{126}$Ag | 126 | 79 | 221.9073 | -786809.25 ± 242.1014 | 118126.5663 | 117307.5367 | +6981900.83 ± 1707.23 | ±0.41 |
| ${}^{127}$Ag | 127 | 80 | 227.8537 | -782372.23 ± 242.6007 | 119060.1853 | 118241.1015 | +6927234.24 ± 1693.75 | ±0.41 |
| ${}^{128}$Ag | 128 | 81 | 233.7923 | -777554.24 ± 243.5757 | 119993.8121 | 119176.5349 | +6857702.50 ± 2516.78 | ±0.41 |
| ${}^{129}$Ag | 129 | 82 | 239.7233 | -773043.50 ± 366.3898 | 120927.4466 | 120110.8691 | +6798530.73 ± 3327.02 | ±0.42 |
| ${}^{130}$Ag | 130 | 83 | 245.6467 | -767920.63 ± 368.4598 | 121861.0885 | 121048.3360 | +6714280.95 ± 3501.33 | ±0.42 |
| ${}^{131}$Ag | 131 | 84 | 251.5628 | -762981.12 ± 493.7053 | 122794.7378 | 121984.9775 | +6638197.02 ± 4100.61 | ±0.42 |
| ${}^{132}$Ag | 132 | 85 | 257.4717 | -757786.77 ± 496.7093 | 123728.3944 | 122922.8216 | +6553484.27 ± 4069.32 | ±0.42 |
| ${}^{133}$Ag | 133 | 86 | 263.3734 | -752870.16 ± 499.1888 | 124662.0581 | 123859.6355 | +6478483.42 ± 4038.54 | ±0.42 |

### Cadmium (Z = 48)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{94}$Cd | 94 | 46 | 9.3348 | -987742.96 ± 617.1316 | 88272.2629 | 87520.0059 | +8595257.78 ± 5715.41 | ±0.32 |
| ${}^{95}$Cd | 95 | 47 | 15.6799 | -979800.26 ± 734.3042 | 89205.4832 | 88444.8836 | +8599701.54 ± 6392.87 | ±0.32 |
| ${}^{96}$Cd | 96 | 48 | 22.0094 | -972240.59 ± 484.3201 | 90138.7191 | 89367.8620 | +8625664.01 ± 4586.18 | ±0.33 |
| ${}^{97}$Cd | 97 | 49 | 28.3236 | -964863.32 ± 521.2446 | 91071.9703 | 90294.1940 | +8613801.65 ± 4653.36 | ±0.33 |
| ${}^{98}$Cd | 98 | 50 | 34.6229 | -957832.08 ± 63.0797 | 92005.2364 | 91218.7857 | +8621587.10 ± 567.82 | ±0.33 |
| ${}^{99}$Cd | 99 | 51 | 40.9076 | -950798.99 ± 1.9051 | 92938.5172 | 92147.9851 | +8578939.92 ± 17.18 | ±0.34 |
| ${}^{100}$Cd | 100 | 52 | 47.1781 | -944086.80 ± 1.9911 | 93871.8121 | 93075.2158 | +8558630.27 ± 18.01 | ±0.34 |
| ${}^{101}$Cd | 101 | 53 | 53.4346 | -937392.59 ± 1.7514 | 94805.1210 | 94005.0680 | +8510743.60 ± 15.85 | ±0.34 |
| ${}^{102}$Cd | 102 | 54 | 59.6775 | -931039.08 ± 1.9212 | 95738.4436 | 94932.7389 | +8487110.99 ± 17.50 | ±0.35 |
| ${}^{103}$Cd | 103 | 55 | 65.9071 | -924629.80 ± 2.0731 | 96671.7794 | 95863.2411 | +8434289.91 ± 18.88 | ±0.35 |
| ${}^{104}$Cd | 104 | 56 | 72.1236 | -918581.02 ± 1.8902 | 97605.1283 | 96791.4184 | +8406839.48 ± 17.27 | ±0.35 |
| ${}^{105}$Cd | 105 | 57 | 78.3274 | -912411.89 ± 1.5616 | 98538.4900 | 97722.5470 | +8349587.05 ± 14.24 | ±0.36 |
| ${}^{106}$Cd | 106 | 58 | 84.5187 | -906623.55 ± 1.2179 | 99471.8641 | 98651.2428 | +8318407.47 ± 11.18 | ±0.36 |
| ${}^{107}$Cd | 107 | 59 | 90.6978 | -900667.09 ± 1.8164 | 100405.2504 | 99582.8788 | +8258162.98 ± 16.67 | ±0.36 |
| ${}^{108}$Cd | 108 | 60 | 96.8649 | -895099.99 ± 1.2164 | 101338.6487 | 100512.1108 | +8223267.12 ± 11.17 | ±0.36 |
| ${}^{109}$Cd | 109 | 61 | 103.0203 | -889311.81 ± 1.6513 | 102272.0587 | 101444.3530 | +8159209.71 ± 15.14 | ±0.37 |
| ${}^{110}$Cd | 110 | 62 | 109.1643 | -883946.87 ± 0.4093 | 103205.4802 | 102374.0034 | +8121952.21 ± 3.70 | ±0.37 |
| ${}^{111}$Cd | 111 | 63 | 115.2970 | -878329.44 ± 0.3748 | 104138.9129 | 103306.5933 | +8056791.20 ± 3.45 | ±0.37 |
| ${}^{112}$Cd | 112 | 64 | 121.4187 | -873127.05 ± 0.2575 | 105072.3566 | 104236.7648 | +8016287.55 ± 2.39 | ±0.37 |
| ${}^{113}$Cd | 113 | 65 | 127.5296 | -867646.07 ± 0.2580 | 106005.8111 | 105169.7904 | +7949247.68 ± 2.32 | ±0.38 |
| ${}^{114}$Cd | 114 | 66 | 133.6299 | -862604.42 ± 0.2813 | 106939.2762 | 106100.3129 | +7907265.44 ± 2.60 | ±0.38 |
| ${}^{115}$Cd | 115 | 67 | 139.7199 | -857244.17 ± 0.6697 | 107872.7517 | 107033.7374 | +7838782.82 ± 6.08 | ±0.38 |
| ${}^{116}$Cd | 116 | 68 | 145.7997 | -852344.66 ± 0.1645 | 108806.2373 | 107964.6035 | +7795459.84 ± 1.48 | ±0.38 |
| ${}^{117}$Cd | 117 | 69 | 151.8696 | -847092.18 ± 1.0249 | 109739.7328 | 108898.3917 | +7725927.70 ± 9.30 | ±0.39 |
| ${}^{118}$Cd | 118 | 70 | 157.9297 | -842317.04 ± 19.9698 | 110673.2382 | 109829.6026 | +7681313.29 ± 182.10 | ±0.39 |
| ${}^{119}$Cd | 119 | 71 | 163.9802 | -837145.35 ± 37.4404 | 111606.7531 | 110763.8214 | +7610171.66 ± 340.32 | ±0.39 |
| ${}^{120}$Cd | 120 | 72 | 170.0213 | -832485.24 ± 3.6770 | 112540.2774 | 111695.3351 | +7564705.74 ± 33.36 | ±0.39 |
| ${}^{121}$Cd | 121 | 73 | 176.0531 | -827424.38 ± 1.9096 | 113473.8110 | 112629.7127 | +7494454.54 ± 17.24 | ±0.40 |
| ${}^{122}$Cd | 122 | 74 | 182.0759 | -822842.05 ± 2.2316 | 114407.3536 | 113561.6683 | +7446925.75 ± 20.24 | ±0.40 |
| ${}^{123}$Cd | 123 | 75 | 188.0899 | -817854.21 ± 2.6086 | 115340.9051 | 114496.3606 | +7376168.96 ± 23.54 | ±0.40 |
| ${}^{124}$Cd | 124 | 76 | 194.0951 | -813368.36 ± 2.5039 | 116274.4653 | 115428.5694 | +7328305.93 ± 22.60 | ±0.40 |
| ${}^{125}$Cd | 125 | 77 | 200.0917 | -808471.56 ± 2.7639 | 117208.0341 | 116363.4149 | +7258460.10 ± 24.82 | ±0.40 |
| ${}^{126}$Cd | 126 | 78 | 206.0799 | -804048.62 ± 2.1925 | 118141.6113 | 117296.0013 | +7209196.59 ± 19.64 | ±0.41 |
| ${}^{127}$Cd | 127 | 79 | 212.0599 | -799232.45 ± 5.8676 | 119075.1967 | 118231.0100 | +7140146.71 ± 52.44 | ±0.41 |
| ${}^{128}$Cd | 128 | 80 | 218.0318 | -794854.32 ± 6.0579 | 120008.7903 | 119164.0070 | +7089248.60 ± 53.98 | ±0.41 |
| ${}^{129}$Cd | 129 | 81 | 223.9956 | -790024.33 ± 4.9821 | 120942.3918 | 120099.6172 | +7017296.32 ± 44.21 | ±0.41 |
| ${}^{130}$Cd | 130 | 82 | 229.9517 | -785660.03 ± 20.8419 | 121876.0012 | 121033.1159 | +6964088.47 ± 184.71 | ±0.41 |
| ${}^{131}$Cd | 131 | 83 | 235.9001 | -780558.45 ± 17.9013 | 122809.6183 | 121970.5158 | +6879551.56 ± 157.73 | ±0.42 |
| ${}^{132}$Cd | 132 | 84 | 241.8408 | -775725.82 ± 55.7096 | 123743.2429 | 122906.7563 | +6805863.83 ± 488.72 | ±0.42 |
| ${}^{133}$Cd | 133 | 85 | 247.7742 | -770599.19 ± 246.2751 | 124676.8750 | 123844.5760 | +6720511.97 ± 1617.12 | ±0.42 |
| ${}^{134}$Cd | 134 | 86 | 253.7003 | -765856.35 ± 247.3411 | 125610.5143 | 124780.7499 | +6649778.88 ± 2403.74 | ±0.42 |
| ${}^{135}$Cd | 135 | 87 | 259.6191 | -760688.82 ± 373.3201 | 126544.1609 | 125718.8837 | +6564464.54 ± 3178.61 | ±0.42 |

### Indium (Z = 49)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{96}$In | 96 | 47 | 4.6704 | -993970.71 ± 619.6555 | 90155.2758 | 89385.3442 | +8613621.63 ± 5596.13 | ±0.32 |
| ${}^{97}$In | 97 | 48 | 11.0333 | -986069.17 ± 489.8959 | 91088.4783 | 90307.5383 | +8647562.03 ± 4435.32 | ±0.32 |
| ${}^{98}$In | 98 | 49 | 17.3806 | -978450.45 ± 364.5200 | 92021.6965 | 91232.5157 | +8650214.22 ± 3338.71 | ±0.33 |
| ${}^{99}$In | 99 | 50 | 23.7126 | -971155.86 ± 361.2717 | 92954.9298 | 92156.5401 | +8663407.91 ± 3234.48 | ±0.33 |
| ${}^{100}$In | 100 | 51 | 30.0299 | -963948.66 ± 2.6892 | 93888.1780 | 93085.2322 | +8625920.43 ± 24.02 | ±0.33 |
| ${}^{101}$In | 101 | 52 | 36.3325 | -957023.92 ± 13.7986 | 94821.4408 | 94012.3596 | +8606115.24 ± 124.04 | ±0.34 |
| ${}^{102}$In | 102 | 53 | 42.6210 | -950187.82 ± 5.3406 | 95754.7177 | 94941.7037 | +8563297.40 ± 48.16 | ±0.34 |
| ${}^{103}$In | 103 | 54 | 48.8956 | -943645.52 ± 10.3517 | 96688.0086 | 95869.2603 | +8540258.78 ± 93.67 | ±0.34 |
| ${}^{104}$In | 104 | 55 | 55.1566 | -937126.66 ± 6.5795 | 97621.3130 | 96799.2041 | +8492930.47 ± 59.66 | ±0.35 |
| ${}^{105}$In | 105 | 56 | 61.4042 | -930912.85 ± 11.5302 | 98554.6308 | 97727.2403 | +8466323.77 ± 104.85 | ±0.35 |
| ${}^{106}$In | 106 | 57 | 67.6389 | -924664.26 ± 13.6126 | 99487.9615 | 98657.7668 | +8414894.32 ± 123.92 | ±0.35 |
| ${}^{107}$In | 107 | 58 | 73.8608 | -918732.69 ± 10.6192 | 100421.3050 | 99586.3024 | +8384713.33 ± 96.93 | ±0.36 |
| ${}^{108}$In | 108 | 59 | 80.0703 | -912728.73 ± 9.4170 | 101354.6610 | 100517.2434 | +8331084.31 ± 85.96 | ±0.36 |
| ${}^{109}$In | 109 | 60 | 86.2675 | -907032.13 ± 4.2758 | 102288.0292 | 101446.3678 | +8296614.55 ± 39.13 | ±0.36 |
| ${}^{110}$In | 110 | 61 | 92.4528 | -901223.55 ± 12.3400 | 103221.4093 | 102377.8814 | +8239356.87 ± 112.84 | ±0.36 |
| ${}^{111}$In | 111 | 62 | 98.6263 | -895740.89 ± 3.6141 | 104154.8012 | 103307.4535 | +8202193.70 ± 33.14 | ±0.37 |
| ${}^{112}$In | 112 | 63 | 104.7884 | -890117.75 ± 4.4629 | 105088.2046 | 104239.3495 | +8143326.57 ± 40.78 | ±0.37 |
| ${}^{113}$In | 113 | 64 | 110.9392 | -884809.19 ± 0.1995 | 106021.6192 | 105169.4666 | +8102661.18 ± 1.79 | ±0.37 |
| ${}^{114}$In | 114 | 65 | 117.0790 | -879345.37 ± 0.3172 | 106955.0448 | 106101.7580 | +8042154.73 ± 2.84 | ±0.37 |
| ${}^{115}$In | 115 | 66 | 123.2080 | -874200.87 ± 0.0352 | 107888.4812 | 107032.2856 | +7999414.62 ± 0.10 | ±0.38 |
| ${}^{116}$In | 116 | 67 | 129.3264 | -868862.25 ± 0.2235 | 108821.9282 | 107965.0663 | +7936474.11 ± 2.04 | ±0.38 |
| ${}^{117}$In | 117 | 68 | 135.4344 | -863878.45 ± 4.9037 | 109755.3856 | 108895.8671 | +7893031.79 ± 44.81 | ±0.38 |
| ${}^{118}$In | 118 | 69 | 141.5323 | -858652.73 ± 7.7425 | 110688.8532 | 109829.0761 | +7828320.29 ± 70.58 | ±0.38 |
| ${}^{119}$In | 119 | 70 | 147.6201 | -853819.87 ± 7.2353 | 111622.3308 | 110760.0997 | +7784673.07 ± 65.99 | ±0.39 |
| ${}^{120}$In | 120 | 71 | 153.6981 | -848715.04 ± 39.3799 | 112555.8183 | 111693.5647 | +7719814.06 ± 358.22 | ±0.39 |
| ${}^{121}$In | 121 | 72 | 159.7665 | -843997.71 ± 26.7726 | 113489.3153 | 112624.9520 | +7674705.44 ± 243.45 | ±0.39 |
| ${}^{122}$In | 122 | 73 | 165.8254 | -838994.61 ± 48.6016 | 114422.8218 | 113558.7093 | +7609389.66 ± 440.82 | ±0.39 |
| ${}^{123}$In | 123 | 74 | 171.8751 | -834395.69 ± 19.1042 | 115356.3375 | 114490.3457 | +7563884.75 ± 173.22 | ±0.39 |
| ${}^{124}$In | 124 | 75 | 177.9157 | -829480.78 ± 29.2953 | 116289.8623 | 115424.4011 | +7498078.86 ± 264.77 | ±0.40 |
| ${}^{125}$In | 125 | 76 | 183.9473 | -824977.42 ± 1.6889 | 117223.3961 | 116356.3507 | +7451638.49 ± 15.21 | ±0.40 |
| ${}^{126}$In | 126 | 77 | 189.9702 | -820182.36 ± 3.9716 | 118156.9387 | 117290.4477 | +7387566.42 ± 35.74 | ±0.40 |
| ${}^{127}$In | 127 | 78 | 195.9845 | -815735.18 ± 9.4092 | 119090.4898 | 118222.8713 | +7338838.42 ± 84.59 | ±0.40 |
| ${}^{128}$In | 128 | 79 | 201.9903 | -811044.59 ± 1.2333 | 120024.0494 | 119157.0552 | +7276063.41 ± 11.09 | ±0.40 |
| ${}^{129}$In | 129 | 80 | 207.9878 | -806648.89 ± 1.8348 | 120957.6174 | 120089.9045 | +7225527.37 ± 16.41 | ±0.41 |
| ${}^{130}$In | 130 | 81 | 213.9771 | -802027.57 ± 1.6598 | 121891.1935 | 121024.3270 | +7162746.14 ± 14.79 | ±0.41 |
| ${}^{131}$In | 131 | 82 | 219.9584 | -797652.34 ± 2.0246 | 122824.7776 | 121957.7032 | +7109632.04 ± 18.08 | ±0.41 |
| ${}^{132}$In | 132 | 83 | 225.9318 | -792626.20 ± 55.1025 | 123758.3696 | 122894.8101 | +7026818.20 ± 488.48 | ±0.41 |
| ${}^{133}$In | 133 | 84 | 231.8975 | -787807.00 ± 243.3978 | 124691.9694 | 123831.0256 | +6952569.56 ± 1617.29 | ±0.41 |
| ${}^{134}$In | 134 | 85 | 237.8555 | -782816.47 ± 122.3541 | 125625.5768 | 124768.2400 | +6871434.55 ± 1605.15 | ±0.42 |
| ${}^{135}$In | 135 | 86 | 243.8060 | -778027.21 ± 245.8210 | 126559.1917 | 125704.5937 | +6798462.48 ± 2386.08 | ±0.42 |
| ${}^{136}$In | 136 | 87 | 249.7492 | -773032.84 ± 247.1882 | 127492.8139 | 126642.2282 | +6716446.05 ± 2368.41 | ±0.42 |
| ${}^{137}$In | 137 | 88 | 255.6852 | -768246.00 ± 372.5320 | 128426.4434 | 127578.8623 | +6643585.59 ± 3132.27 | ±0.42 |

### Tin (Z = 50)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{99}$Sn | 99 | 49 | 6.2125 | -992310.64 ± 735.2040 | 92971.6476 | 92169.9397 | +8698149.74 ± 6316.42 | ±0.32 |
| ${}^{100}$Sn | 100 | 50 | 12.5775 | -984757.57 ± 290.8639 | 93904.8481 | 93092.2622 | +8728822.66 ± 2578.19 | ±0.33 |
| ${}^{101}$Sn | 101 | 51 | 18.9273 | -977370.29 ± 358.6841 | 94838.0637 | 94020.5989 | +8694529.14 ± 3190.84 | ±0.33 |
| ${}^{102}$Sn | 102 | 52 | 25.2623 | -970247.87 ± 117.8939 | 95771.2941 | 94947.4637 | +8676697.56 ± 1054.31 | ±0.33 |
| ${}^{103}$Sn | 103 | 53 | 31.5828 | -963247.12 ± 119.8610 | 96704.5390 | 95876.8000 | +8633361.30 ± 1049.28 | ±0.34 |
| ${}^{104}$Sn | 104 | 54 | 37.8892 | -956545.47 ± 6.5840 | 97637.7981 | 96803.7597 | +8615764.02 ± 59.34 | ±0.34 |
| ${}^{105}$Sn | 105 | 55 | 44.1817 | -949890.88 ± 4.5015 | 98571.0710 | 97733.5429 | +8569505.34 ± 40.63 | ±0.34 |
| ${}^{106}$Sn | 106 | 56 | 50.4606 | -943543.50 ± 5.6926 | 99504.3575 | 98661.0213 | +8547815.44 ± 51.60 | ±0.35 |
| ${}^{107}$Sn | 107 | 57 | 56.7263 | -937182.03 ± 5.8771 | 100437.6573 | 99591.3569 | +8497729.44 ± 53.31 | ±0.35 |
| ${}^{108}$Sn | 108 | 58 | 62.9789 | -931144.62 ± 5.8803 | 101370.9700 | 100519.2933 | +8472769.24 ± 53.54 | ±0.35 |
| ${}^{109}$Sn | 109 | 59 | 69.2188 | -925029.94 ± 8.6063 | 102304.2955 | 101450.2271 | +8418595.19 ± 78.35 | ±0.35 |
| ${}^{110}$Sn | 110 | 60 | 75.4463 | -919271.60 ± 14.7362 | 103237.6335 | 102378.5094 | +8391644.52 ± 134.57 | ±0.36 |
| ${}^{111}$Sn | 111 | 61 | 81.6616 | -913378.26 ± 5.6634 | 104170.9836 | 103309.9069 | +8334889.97 ± 51.65 | ±0.36 |
| ${}^{112}$Sn | 112 | 62 | 87.8649 | -907852.61 ± 0.3054 | 105104.3458 | 104238.6846 | +8304605.94 ± 2.81 | ±0.36 |
| ${}^{113}$Sn | 113 | 63 | 94.0564 | -902153.96 ± 1.6340 | 106037.7196 | 105170.5056 | +8245791.14 ± 14.97 | ±0.37 |
| ${}^{114}$Sn | 114 | 64 | 100.2365 | -896830.64 ± 0.0469 | 106971.1050 | 106099.7681 | +8212429.47 ± 0.27 | ±0.37 |
| ${}^{115}$Sn | 115 | 65 | 106.4053 | -891325.31 ± 0.0352 | 107904.5015 | 107031.7881 | +8153778.27 ± 0.14 | ±0.37 |
| ${}^{116}$Sn | 116 | 66 | 112.5631 | -886148.24 ± 0.1056 | 108837.9092 | 107961.7901 | +8115085.30 ± 0.89 | ±0.37 |
| ${}^{117}$Sn | 117 | 67 | 118.7101 | -880768.22 ± 0.4818 | 109771.3277 | 108894.4124 | +8052894.94 ± 4.43 | ±0.38 |
| ${}^{118}$Sn | 118 | 68 | 124.8464 | -875768.64 ± 0.4932 | 110704.7567 | 109824.6514 | +8013732.19 ± 4.55 | ±0.38 |
| ${}^{119}$Sn | 119 | 69 | 130.9724 | -870508.32 ± 0.7177 | 111638.1962 | 110757.7334 | +7949448.36 ± 6.54 | ±0.38 |
| ${}^{120}$Sn | 120 | 70 | 137.0881 | -865670.87 ± 0.9054 | 112571.6460 | 111688.1947 | +7909978.80 ± 8.23 | ±0.38 |
| ${}^{121}$Sn | 121 | 71 | 143.1937 | -860531.30 ± 0.9546 | 113505.1057 | 112621.5899 | +7844994.72 ± 8.68 | ±0.38 |
| ${}^{122}$Sn | 122 | 72 | 149.2896 | -855831.78 ± 2.3681 | 114438.5753 | 113552.3407 | +7804635.12 ± 21.55 | ±0.39 |
| ${}^{123}$Sn | 123 | 73 | 155.3758 | -850811.03 ± 2.3857 | 115372.0545 | 114485.9601 | +7739765.24 ± 21.65 | ±0.39 |
| ${}^{124}$Sn | 124 | 74 | 161.4525 | -846229.55 ± 1.2519 | 116305.5433 | 115417.0374 | +7698221.05 ± 11.38 | ±0.39 |
| ${}^{125}$Sn | 125 | 75 | 167.5198 | -841317.36 ± 1.2551 | 117239.0413 | 116350.8693 | +7633565.45 ± 11.42 | ±0.39 |
| ${}^{126}$Sn | 126 | 76 | 173.5781 | -836844.88 ± 10.0432 | 118172.5485 | 117282.2419 | +7591145.14 ± 91.12 | ±0.40 |
| ${}^{127}$Sn | 127 | 77 | 179.6274 | -832031.28 ± 8.6218 | 119106.0646 | 118216.2816 | +7526738.24 ± 78.04 | ±0.40 |
| ${}^{128}$Sn | 128 | 78 | 185.6678 | -827666.12 ± 16.4073 | 120039.5896 | 119147.8838 | +7484024.82 ± 148.40 | ±0.40 |
| ${}^{129}$Sn | 129 | 79 | 191.6996 | -822938.62 ± 15.9541 | 120973.1232 | 120082.1488 | +7419707.40 ± 143.82 | ±0.40 |
| ${}^{130}$Sn | 130 | 80 | 197.7229 | -818650.45 ± 1.7170 | 121906.6653 | 121014.1013 | +7375702.92 ± 15.47 | ±0.40 |
| ${}^{131}$Sn | 131 | 81 | 203.7378 | -814021.25 ± 3.3004 | 122840.2158 | 121948.4630 | +7312538.38 ± 29.69 | ±0.41 |
| ${}^{132}$Sn | 132 | 82 | 209.7445 | -809814.71 ± 1.7954 | 123773.7745 | 122880.6751 | +7268021.61 ± 16.08 | ±0.41 |
| ${}^{133}$Sn | 133 | 83 | 215.7432 | -804800.03 ± 1.7208 | 124707.3413 | 123817.8419 | +7183935.80 ± 15.37 | ±0.41 |
| ${}^{134}$Sn | 134 | 84 | 221.7339 | -800036.74 ± 2.8519 | 125640.9161 | 124753.7761 | +7111126.82 ± 25.39 | ±0.41 |
| ${}^{135}$Sn | 135 | 85 | 227.7168 | -795060.77 ± 2.7701 | 126574.4986 | 125691.0717 | +7028556.91 ± 24.46 | ±0.41 |
| ${}^{136}$Sn | 136 | 86 | 233.6920 | -790371.69 ± 121.9959 | 127508.0888 | 126627.0281 | +6957920.01 ± 1581.58 | ±0.41 |
| ${}^{137}$Sn | 137 | 87 | 239.6596 | -785409.67 ± 245.3386 | 128441.6866 | 127564.5424 | +6876081.13 ± 2351.29 | ±0.42 |
| ${}^{138}$Sn | 138 | 88 | 245.6199 | -780752.14 ± 369.5492 | 129375.2918 | 128500.6763 | +6806310.09 ± 3109.80 | ±0.42 |
| ${}^{139}$Sn | 139 | 89 | 251.5728 | -775811.19 ± 371.6091 | 130308.9042 | 129438.3704 | +6725469.45 ± 3087.27 | ±0.42 |
| ${}^{140}$Sn | 140 | 90 | 257.5186 | -771159.70 ± 248.8181 | 131242.5239 | 130374.6841 | +6656505.62 ± 2300.61 | ±0.42 |

### Antimony (Z = 51)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{102}$Sb | 102 | 51 | 7.6014 | -990890.71 ± 488.9378 | 95788.1727 | 94961.2987 | +8707484.52 ± 4208.15 | ±0.33 |
| ${}^{103}$Sb | 103 | 52 | 13.9688 | -983529.38 ± 364.3430 | 96721.3707 | 95887.2224 | +8699264.20 ± 3128.06 | ±0.33 |
| ${}^{104}$Sb | 104 | 53 | 20.3214 | -976338.30 ± 121.0947 | 97654.5835 | 96816.0916 | +8660666.58 ± 1048.72 | ±0.33 |
| ${}^{105}$Sb | 105 | 54 | 26.6597 | -969413.11 ± 25.0452 | 98587.8107 | 97742.8654 | +8644572.43 ± 223.30 | ±0.34 |
| ${}^{106}$Sb | 106 | 55 | 32.9838 | -962609.09 ± 8.4475 | 99521.0520 | 98671.9017 | +8605796.42 ± 75.52 | ±0.34 |
| ${}^{107}$Sb | 107 | 56 | 39.2941 | -956065.82 ± 4.6419 | 100454.3071 | 99599.2158 | +8585321.38 ± 41.64 | ±0.34 |
| ${}^{108}$Sb | 108 | 57 | 45.5908 | -949581.52 ± 6.0793 | 101387.5758 | 100528.9179 | +8541402.33 ± 54.67 | ±0.35 |
| ${}^{109}$Sb | 109 | 58 | 51.8743 | -943376.37 ± 5.7467 | 102320.8577 | 101456.6063 | +8518433.88 ± 51.89 | ±0.35 |
| ${}^{110}$Sb | 110 | 59 | 58.1448 | -937167.54 ± 6.4427 | 103254.1526 | 102386.9017 | +8470330.94 ± 58.23 | ±0.35 |
| ${}^{111}$Sb | 111 | 60 | 64.4027 | -931256.41 ± 9.4430 | 104187.4602 | 103315.0088 | +8444576.03 ± 85.65 | ±0.35 |
| ${}^{112}$Sb | 112 | 61 | 70.6480 | -925294.49 ± 18.8544 | 105120.7803 | 104245.7406 | +8394008.47 ± 171.03 | ±0.36 |
| ${}^{113}$Sb | 113 | 62 | 76.8812 | -919628.80 ± 17.9675 | 106054.1125 | 105174.4168 | +8364161.27 ± 163.47 | ±0.36 |
| ${}^{114}$Sb | 114 | 63 | 83.1024 | -913859.19 ± 20.4904 | 106987.4568 | 106105.8312 | +8308926.54 ± 186.34 | ±0.36 |
| ${}^{115}$Sb | 115 | 64 | 89.3118 | -908426.78 ± 16.4369 | 107920.8127 | 107034.8185 | +8277626.02 ± 149.71 | ±0.36 |
| ${}^{116}$Sb | 116 | 65 | 95.5098 | -902857.72 ± 5.2384 | 108854.1802 | 107966.4940 | +8221866.96 ± 47.74 | ±0.37 |
| ${}^{117}$Sb | 117 | 66 | 101.6965 | -897595.25 ± 8.4944 | 109787.5589 | 108896.1706 | +8185671.75 ± 77.47 | ±0.37 |
| ${}^{118}$Sb | 118 | 67 | 107.8722 | -892183.03 ± 3.0193 | 110720.9487 | 109828.3080 | +8127600.55 ± 27.45 | ±0.37 |
| ${}^{119}$Sb | 119 | 68 | 114.0370 | -887099.10 ± 6.9275 | 111654.3493 | 110758.3228 | +8089924.47 ± 63.18 | ±0.37 |
| ${}^{120}$Sb | 120 | 69 | 120.1912 | -881826.73 ± 7.0791 | 112587.7605 | 111690.8753 | +8030067.00 ± 64.45 | ±0.38 |
| ${}^{121}$Sb | 121 | 70 | 126.3349 | -876906.05 ± 2.4404 | 113521.1822 | 112621.1874 | +7991345.57 ± 22.25 | ±0.38 |
| ${}^{122}$Sb | 122 | 71 | 132.4684 | -871780.24 ± 2.4208 | 114454.6142 | 113553.9464 | +7931628.42 ± 22.04 | ±0.38 |
| ${}^{123}$Sb | 123 | 72 | 138.5918 | -867006.60 ± 1.2983 | 115388.0562 | 114484.5519 | +7891931.88 ± 11.85 | ±0.38 |
| ${}^{124}$Sb | 124 | 73 | 144.7054 | -861996.49 ± 1.3008 | 116321.5080 | 115417.6498 | +7831195.88 ± 11.76 | ±0.39 |
| ${}^{125}$Sb | 125 | 74 | 150.8092 | -857359.80 ± 2.3764 | 117254.9696 | 116348.5079 | +7790918.14 ± 21.62 | ±0.39 |
| ${}^{126}$Sb | 126 | 75 | 156.9036 | -852462.06 ± 29.9515 | 118188.4406 | 117281.8639 | +7729896.84 ± 271.54 | ±0.39 |
| ${}^{127}$Sb | 127 | 76 | 162.9886 | -847937.99 ± 4.7394 | 119121.9211 | 118213.0529 | +7688391.07 ± 43.00 | ±0.39 |
| ${}^{128}$Sb | 128 | 77 | 169.0644 | -843147.92 ± 17.4331 | 120055.4107 | 119146.6154 | +7627537.11 ± 157.68 | ±0.39 |
| ${}^{129}$Sb | 129 | 78 | 175.1312 | -838726.93 ± 19.5413 | 120988.9093 | 120078.1100 | +7585056.70 ± 176.76 | ±0.40 |
| ${}^{130}$Sb | 130 | 79 | 181.1892 | -834023.77 ± 13.0160 | 121922.4167 | 121011.9478 | +7523793.81 ± 117.44 | ±0.40 |
| ${}^{131}$Sb | 131 | 80 | 187.2384 | -829694.14 ± 1.8945 | 122855.9329 | 121943.7462 | +7480389.70 ± 17.08 | ±0.40 |
| ${}^{132}$Sb | 132 | 81 | 193.2791 | -825110.46 ± 2.2335 | 123789.4577 | 122877.5864 | +7420972.93 ± 20.07 | ±0.40 |
| ${}^{133}$Sb | 133 | 82 | 199.3114 | -820845.17 ± 2.8094 | 124722.9908 | 123809.7923 | +7375818.15 ± 25.26 | ±0.40 |
| ${}^{134}$Sb | 134 | 83 | 205.3354 | -815954.27 ± 2.7504 | 125656.5322 | 124746.1909 | +7297547.95 ± 24.64 | ±0.41 |
| ${}^{135}$Sb | 135 | 84 | 211.3513 | -811195.48 ± 2.3637 | 126590.0817 | 125682.0137 | +7225123.50 ± 21.00 | ±0.41 |
| ${}^{136}$Sb | 136 | 85 | 217.3592 | -806328.14 ± 5.1986 | 127523.6393 | 126618.6912 | +7147033.67 ± 46.04 | ±0.41 |
| ${}^{137}$Sb | 137 | 86 | 223.3592 | -801622.69 ± 46.3346 | 128457.2046 | 127554.6318 | +7075970.66 ± 408.95 | ±0.41 |
| ${}^{138}$Sb | 138 | 87 | 229.3515 | -796775.79 ± 244.5586 | 129390.7778 | 128491.5365 | +6998447.52 ± 2334.33 | ±0.41 |
| ${}^{139}$Sb | 139 | 88 | 235.3362 | -792108.74 ± 368.3694 | 130324.3585 | 129427.6303 | +6928413.69 ± 3087.52 | ±0.41 |
| ${}^{140}$Sb | 140 | 89 | 241.3135 | -787280.31 ± 493.6443 | 131257.9467 | 130364.7842 | +6851255.89 ± 4601.57 | ±0.42 |
| ${}^{141}$Sb | 141 | 90 | 247.2833 | -782651.80 ± 495.7244 | 132191.5422 | 131301.1286 | +6781462.26 ± 3809.66 | ±0.42 |
| ${}^{142}$Sb | 142 | 91 | 253.2460 | -777822.05 ± 249.1591 | 133125.1450 | 132238.5526 | +6704492.92 ± 2268.18 | ±0.42 |

### Tellurium (Z = 52)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{104}$Te | 104 | 52 | 2.4533 | -997108.15 ± 374.3752 | 97671.6692 | 96825.7600 | +8736407.43 ± 3280.21 | ±0.33 |
| ${}^{105}$Te | 105 | 53 | 8.8382 | -989718.43 ± 349.0115 | 98604.8498 | 97754.0694 | +8703273.47 ± 3069.12 | ±0.33 |
| ${}^{106}$Te | 106 | 54 | 15.2084 | -982581.08 ± 115.1544 | 99538.0450 | 98680.1552 | +8693640.27 ± 1018.85 | ±0.33 |
| ${}^{107}$Te | 107 | 55 | 21.5642 | -975595.19 ± 121.0947 | 100471.2546 | 99609.2121 | +8654245.22 ± 1009.96 | ±0.34 |
| ${}^{108}$Te | 108 | 56 | 27.9060 | -968882.79 ± 6.0334 | 101404.4783 | 100535.5815 | +8642679.12 ± 53.81 | ±0.34 |
| ${}^{109}$Te | 109 | 57 | 34.2339 | -962247.84 ± 4.8321 | 102337.7158 | 101465.1419 | +8599740.19 ± 43.18 | ±0.34 |
| ${}^{110}$Te | 110 | 58 | 40.5484 | -955896.56 ± 7.1547 | 103270.9667 | 102392.1216 | +8583132.49 ± 64.21 | ±0.35 |
| ${}^{111}$Te | 111 | 59 | 46.8496 | -949560.17 ± 6.9194 | 104204.2309 | 103322.2580 | +8536136.53 ± 62.21 | ±0.35 |
| ${}^{112}$Te | 112 | 60 | 53.1379 | -943522.79 ± 8.9160 | 105137.5081 | 104249.7721 | +8515471.65 ± 80.42 | ±0.35 |
| ${}^{113}$Te | 113 | 61 | 59.4135 | -937441.33 ± 29.4242 | 106070.7979 | 105180.4867 | +8464604.68 ± 265.68 | ±0.35 |
| ${}^{114}$Te | 114 | 62 | 65.6766 | -931682.09 ± 25.4127 | 107004.1002 | 106108.4381 | +8441006.95 ± 230.21 | ±0.36 |
| ${}^{115}$Te | 115 | 63 | 71.9275 | -925815.96 ± 28.8217 | 107937.4147 | 107039.7592 | +8386187.94 ± 261.07 | ±0.36 |
| ${}^{116}$Te | 116 | 64 | 78.1665 | -920307.75 ± 24.6817 | 108870.7411 | 107968.0522 | +8360703.79 ± 224.19 | ±0.36 |
| ${}^{117}$Te | 117 | 65 | 84.3938 | -914646.67 ± 13.6080 | 109804.0793 | 108899.7146 | +8304564.27 ± 123.55 | ±0.36 |
| ${}^{118}$Te | 118 | 66 | 90.6095 | -909338.29 ± 18.3123 | 110737.4290 | 109828.6135 | +8274851.84 ± 166.68 | ±0.37 |
| ${}^{119}$Te | 119 | 67 | 96.8140 | -903857.80 ± 7.2323 | 111670.7899 | 110760.6158 | +8217488.94 ± 65.71 | ±0.37 |
| ${}^{120}$Te | 120 | 68 | 103.0074 | -898738.19 ± 1.7223 | 112604.1620 | 111689.9303 | +8185444.03 ± 15.68 | ±0.37 |
| ${}^{121}$Te | 121 | 69 | 109.1899 | -893420.27 ± 25.2159 | 113537.5448 | 112622.2434 | +8127181.38 ± 229.39 | ±0.37 |
| ${}^{122}$Te | 122 | 70 | 115.3618 | -888467.33 ± 1.3093 | 114470.9384 | 113551.9674 | +8092955.37 ± 11.94 | ±0.38 |
| ${}^{123}$Te | 123 | 71 | 121.5232 | -883292.24 ± 1.2994 | 115404.3424 | 114484.6038 | +8033731.72 ± 11.83 | ±0.38 |
| ${}^{124}$Te | 124 | 72 | 127.6744 | -878484.67 ± 1.2864 | 116337.7566 | 115414.7447 | +7997348.34 ± 11.71 | ±0.38 |
| ${}^{125}$Te | 125 | 73 | 133.8155 | -873431.16 ± 1.2769 | 117271.1810 | 116347.7412 | +7936895.06 ± 11.62 | ±0.38 |
| ${}^{126}$Te | 126 | 74 | 139.9467 | -868763.29 ± 1.2643 | 118204.6152 | 117278.1929 | +7899357.11 ± 11.54 | ±0.38 |
| ${}^{127}$Te | 127 | 75 | 146.0681 | -863825.75 ± 1.2787 | 119138.0592 | 118211.4707 | +7838397.71 ± 11.54 | ±0.39 |
| ${}^{128}$Te | 128 | 76 | 152.1800 | -859280.27 ± 0.6510 | 120071.5127 | 119142.2515 | +7799594.34 ± 5.93 | ±0.39 |
| ${}^{129}$Te | 129 | 77 | 158.2825 | -854455.90 ± 0.6524 | 121004.9756 | 120075.7345 | +7738791.84 ± 5.92 | ±0.39 |
| ${}^{130}$Te | 130 | 78 | 164.3758 | -850014.14 ± 0.0356 | 121938.4477 | 121006.8805 | +7698464.72 ± 0.08 | ±0.39 |
| ${}^{131}$Te | 131 | 79 | 170.4601 | -845299.49 ± 0.0594 | 122871.9289 | 121940.5166 | +7638251.46 ± 0.50 | ±0.40 |
| ${}^{132}$Te | 132 | 80 | 176.5355 | -840947.61 ± 3.1397 | 123805.4190 | 122872.0335 | +7596402.89 ± 28.37 | ±0.40 |
| ${}^{133}$Te | 133 | 81 | 182.6021 | -836340.01 ± 1.8477 | 124738.9178 | 123805.7787 | +7537120.88 ± 16.69 | ±0.40 |
| ${}^{134}$Te | 134 | 82 | 188.6601 | -832064.57 ± 2.4452 | 125672.4252 | 124737.6761 | +7493718.67 ± 22.01 | ±0.40 |
| ${}^{135}$Te | 135 | 83 | 194.7096 | -827182.04 ± 1.5337 | 126605.9411 | 125673.9752 | +7415742.65 ± 13.70 | ±0.40 |
| ${}^{136}$Te | 136 | 84 | 200.7509 | -822570.87 ± 2.0194 | 127539.4653 | 126608.7728 | +7350931.57 ± 18.01 | ±0.40 |
| ${}^{137}$Te | 137 | 85 | 206.7839 | -817713.92 ± 1.8478 | 128472.9976 | 127545.3884 | +7272776.96 ± 16.46 | ±0.41 |
| ${}^{138}$Te | 138 | 86 | 212.8089 | -813137.94 ± 3.3202 | 129406.5380 | 128480.4903 | +7207691.10 ± 29.47 | ±0.41 |
| ${}^{139}$Te | 139 | 87 | 218.8261 | -808288.84 ± 3.1053 | 130340.0863 | 129417.4753 | +7128952.02 ± 27.35 | ±0.41 |
| ${}^{140}$Te | 140 | 88 | 224.8354 | -803752.02 ± 12.5499 | 131273.6424 | 130352.8071 | +7064177.14 ± 110.29 | ±0.41 |
| ${}^{141}$Te | 141 | 89 | 230.8371 | -798926.24 ± 368.4598 | 132207.2061 | 131289.9991 | +6986115.18 ± 3043.73 | ±0.41 |
| ${}^{142}$Te | 142 | 90 | 236.8313 | -794425.52 ± 493.0359 | 133140.7774 | 132225.6132 | +6921232.55 ± 3783.02 | ±0.42 |
| ${}^{143}$Te | 143 | 91 | 242.8180 | -789587.61 ± 371.7472 | 134074.3561 | 133163.1266 | +6842956.44 ± 3756.39 | ±0.42 |
| ${}^{144}$Te | 144 | 92 | 248.7975 | -785104.46 ± 248.7562 | 135007.9420 | 134098.9307 | +6778661.92 ± 2236.72 | ±0.42 |
| ${}^{145}$Te | 145 | 93 | 254.7697 | -780316.00 ± 250.0625 | 135941.5352 | 135036.6351 | +6701145.10 ± 2221.18 | ±0.42 |

### Iodine (Z = 53)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{106}$I | 106 | 53 | -2.8655 | -1003341.89 ± 494.4987 | 99555.3365 | 98695.0754 | +8716353.04 ± 4048.95 | ±0.33 |
| ${}^{107}$I | 107 | 54 | 3.5368 | -995942.29 ± 368.2789 | 100488.4997 | 99620.4394 | +8713677.29 ± 3010.84 | ±0.33 |
| ${}^{108}$I | 108 | 55 | 9.9244 | -988760.69 ± 122.3092 | 101421.6775 | 100548.5922 | +8683217.94 ± 1009.79 | ±0.33 |
| ${}^{109}$I | 109 | 56 | 16.2977 | -981810.26 ± 7.5061 | 102354.8697 | 101475.1848 | +8668965.55 ± 66.30 | ±0.34 |
| ${}^{110}$I | 110 | 57 | 22.6569 | -975015.76 ± 68.3036 | 103288.0759 | 102403.8836 | +8634362.91 ± 604.85 | ±0.34 |
| ${}^{111}$I | 111 | 58 | 29.0024 | -968455.25 ± 5.1673 | 104221.2958 | 103330.8917 | +8617017.15 ± 46.00 | ±0.34 |
| ${}^{112}$I | 112 | 59 | 35.3345 | -961989.07 ± 11.0243 | 105154.5292 | 104260.2763 | +8577119.98 ± 98.28 | ±0.35 |
| ${}^{113}$I | 113 | 60 | 41.6533 | -955768.65 ± 8.5076 | 106087.7758 | 105187.7142 | +8556717.59 ± 76.16 | ±0.35 |
| ${}^{114}$I | 114 | 61 | 47.9592 | -949585.90 ± 21.0551 | 107021.0353 | 106117.6889 | +8512684.48 ± 188.73 | ±0.35 |
| ${}^{115}$I | 115 | 62 | 54.2524 | -943667.52 ± 29.9836 | 107954.3075 | 107045.4841 | +8490067.40 ± 269.76 | ±0.35 |
| ${}^{116}$I | 116 | 63 | 60.5332 | -937737.74 ± 77.1839 | 108887.5921 | 107975.8954 | +8443521.15 ± 694.94 | ±0.36 |
| ${}^{117}$I | 117 | 64 | 66.8018 | -932064.95 ± 25.9863 | 109820.8890 | 108904.3716 | +8415799.84 ± 234.68 | ±0.36 |
| ${}^{118}$I | 118 | 65 | 73.0584 | -926346.62 ± 19.9260 | 110754.1977 | 109835.3332 | +8365837.58 ± 179.90 | ±0.36 |
| ${}^{119}$I | 119 | 66 | 79.3033 | -920918.11 ± 21.6450 | 111687.5182 | 110764.0206 | +8337523.61 ± 195.96 | ±0.36 |
| ${}^{120}$I | 120 | 67 | 85.5367 | -915380.60 ± 14.9341 | 112620.8503 | 111695.5453 | +8284170.80 ± 135.20 | ±0.37 |
| ${}^{121}$I | 121 | 68 | 91.7589 | -910164.57 ± 4.6201 | 113554.1936 | 112624.5409 | +8254441.27 ± 41.93 | ±0.37 |
| ${}^{122}$I | 122 | 69 | 97.9699 | -904820.34 ± 5.0373 | 114487.5479 | 113556.2014 | +8201635.45 ± 45.62 | ±0.37 |
| ${}^{123}$I | 123 | 70 | 104.1701 | -899764.20 ± 3.5506 | 115420.9132 | 114485.8322 | +8167657.10 ± 32.19 | ±0.37 |
| ${}^{124}$I | 124 | 71 | 110.3596 | -894568.66 ± 2.1916 | 116354.2891 | 115417.9043 | +8112994.37 ± 19.91 | ±0.38 |
| ${}^{125}$I | 125 | 72 | 116.5386 | -889671.39 ± 1.2781 | 117287.6755 | 116347.9269 | +8077054.77 ± 11.62 | ±0.38 |
| ${}^{126}$I | 126 | 73 | 122.7073 | -884611.98 ± 3.5545 | 118221.0722 | 117280.3466 | +8021170.37 ± 32.21 | ±0.38 |
| ${}^{127}$I | 127 | 74 | 128.8660 | -879853.80 ± 3.3746 | 119154.4790 | 118210.7680 | +7983291.84 ± 30.63 | ±0.38 |
| ${}^{128}$I | 128 | 75 | 135.0147 | -874917.22 ± 3.3559 | 120087.8957 | 119143.5072 | +7926478.89 ± 30.39 | ±0.38 |
| ${}^{129}$I | 129 | 76 | 141.1536 | -870292.19 ± 2.8924 | 121021.3222 | 120074.2322 | +7887537.55 ± 26.26 | ±0.39 |
| ${}^{130}$I | 130 | 77 | 147.2830 | -865463.46 ± 2.8856 | 121954.7583 | 121007.2973 | +7829783.85 ± 26.06 | ±0.39 |
| ${}^{131}$I | 131 | 78 | 153.4029 | -860962.58 ± 0.5462 | 122888.2038 | 121938.2849 | +7790161.16 ± 4.96 | ±0.39 |
| ${}^{132}$I | 132 | 79 | 159.5136 | -856249.12 ± 3.6638 | 123821.6585 | 122871.5182 | +7732795.19 ± 33.08 | ±0.39 |
| ${}^{133}$I | 133 | 80 | 165.6152 | -851848.61 ± 5.2825 | 124755.1223 | 123802.8585 | +7691775.53 ± 47.66 | ±0.39 |
| ${}^{134}$I | 134 | 81 | 171.7079 | -847253.42 ± 4.3151 | 125688.5950 | 124736.1665 | +7635544.81 ± 38.93 | ±0.40 |
| ${}^{135}$I | 135 | 82 | 177.7918 | -842932.19 ± 1.8247 | 126622.0766 | 125667.9248 | +7592643.62 ± 16.39 | ±0.40 |
| ${}^{136}$I | 136 | 83 | 183.8670 | -838113.91 ± 12.4890 | 127555.5668 | 126603.6529 | +7518850.13 ± 112.06 | ±0.40 |
| ${}^{137}$I | 137 | 84 | 189.9337 | -833488.21 ± 7.3505 | 128489.0655 | 127538.3359 | +7454460.69 ± 65.73 | ±0.40 |
| ${}^{138}$I | 138 | 85 | 195.9921 | -828731.72 ± 5.2096 | 129422.5725 | 128474.2064 | +7381762.56 ± 46.40 | ±0.40 |
| ${}^{139}$I | 139 | 86 | 202.0423 | -824145.86 ± 3.4843 | 130356.0877 | 129409.2095 | +7316931.28 ± 30.95 | ±0.41 |
| ${}^{140}$I | 140 | 87 | 208.0844 | -819391.01 ± 10.5110 | 131289.6111 | 130345.5683 | +7242615.17 ± 92.90 | ±0.41 |
| ${}^{141}$I | 141 | 88 | 214.1185 | -814859.36 ± 13.6914 | 132223.1424 | 131280.7420 | +7178512.34 ± 120.62 | ±0.41 |
| ${}^{142}$I | 142 | 89 | 220.1448 | -810132.55 ± 4.2620 | 133156.6815 | 132217.3598 | +7104375.34 ± 37.34 | ±0.41 |
| ${}^{143}$I | 143 | 90 | 226.1634 | -805633.25 ± 122.8954 | 134090.2283 | 133152.8671 | +7039737.40 ± 1504.07 | ±0.41 |
| ${}^{144}$I | 144 | 91 | 232.1744 | -800898.70 ± 370.4618 | 135023.7827 | 134089.8207 | +6965197.13 ± 2980.17 | ±0.41 |
| ${}^{145}$I | 145 | 92 | 238.1780 | -796429.96 ± 371.7933 | 135957.3446 | 135025.5149 | +6901137.85 ± 3704.58 | ±0.42 |
| ${}^{146}$I | 146 | 93 | 244.1742 | -791753.72 ± 249.0350 | 136890.9138 | 135962.5989 | +6827722.57 ± 2206.06 | ±0.42 |
| ${}^{147}$I | 147 | 94 | 250.1632 | -787302.81 ± 249.9688 | 137824.4903 | 136898.4329 | +6764558.18 ± 2190.98 | ±0.42 |

### Xenon (Z = 54)

_43 of 43 isotopes with a framework prediction; 43 of 43 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{108}$Xe | 108 | 54 | -8.3539 | -1009579.21 ± 435.1639 | 101439.1735 | 100558.7308 | +8755507.01 ± 3773.88 | ±0.33 |
| ${}^{109}$Xe | 109 | 55 | -1.9344 | -1002189.03 ± 339.6072 | 102372.3195 | 101486.6878 | +8726580.02 ± 2957.11 | ±0.33 |
| ${}^{110}$Xe | 110 | 56 | 4.4705 | -995019.10 ± 112.5222 | 103305.4800 | 102412.4288 | +8720144.81 ± 986.09 | ±0.33 |
| ${}^{111}$Xe | 111 | 57 | 10.8611 | -988041.11 ± 122.2195 | 104238.6548 | 103341.3252 | +8683163.46 ± 1117.71 | ±0.34 |
| ${}^{112}$Xe | 112 | 58 | 17.2377 | -981299.27 ± 8.9914 | 105171.8436 | 104267.3133 | +8675108.97 ± 79.43 | ±0.34 |
| ${}^{113}$Xe | 113 | 59 | 23.6006 | -974677.85 ± 7.3352 | 106105.0461 | 105196.6301 | +8635409.51 ± 65.01 | ±0.34 |
| ${}^{114}$Xe | 114 | 60 | 29.9501 | -968305.72 ± 11.8347 | 107038.2620 | 106123.2419 | +8622240.21 ± 105.33 | ±0.34 |
| ${}^{115}$Xe | 115 | 61 | 36.2864 | -961988.26 ± 12.6853 | 107971.4911 | 107053.1652 | +8578223.20 ± 113.12 | ±0.35 |
| ${}^{116}$Xe | 116 | 62 | 42.6098 | -955939.37 ± 13.4583 | 108904.7331 | 107980.2692 | +8561415.79 ± 120.55 | ±0.35 |
| ${}^{117}$Xe | 117 | 63 | 48.9206 | -949890.96 ± 10.6300 | 109837.9878 | 108910.6248 | +8514899.53 ± 95.29 | ±0.35 |
| ${}^{118}$Xe | 118 | 64 | 55.2189 | -944124.43 ± 10.5075 | 110771.2549 | 109838.2252 | +8494581.39 ± 94.48 | ±0.36 |
| ${}^{119}$Xe | 119 | 65 | 61.5051 | -938312.01 ± 10.4077 | 111704.5342 | 110769.0039 | +8445777.34 ± 93.69 | ±0.36 |
| ${}^{120}$Xe | 120 | 66 | 67.7792 | -932790.94 ± 11.7206 | 112637.8254 | 111697.1200 | +8421930.80 ± 105.79 | ±0.36 |
| ${}^{121}$Xe | 121 | 67 | 74.0417 | -927186.20 ± 10.0787 | 113571.1284 | 112628.3056 | +8371100.19 ± 90.93 | ±0.36 |
| ${}^{122}$Xe | 122 | 68 | 80.2927 | -921879.78 ± 10.8135 | 114504.4428 | 113556.9257 | +8343984.09 ± 97.84 | ±0.37 |
| ${}^{123}$Xe | 123 | 69 | 86.5323 | -916456.32 ± 9.2033 | 115437.7686 | 114488.5265 | +8291154.88 ± 83.27 | ±0.37 |
| ${}^{124}$Xe | 124 | 70 | 92.7609 | -911340.82 ± 1.3037 | 116371.1054 | 115417.6015 | +8261339.52 ± 11.76 | ±0.37 |
| ${}^{125}$Xe | 125 | 71 | 98.9786 | -906080.58 ± 1.3403 | 117304.4532 | 116349.5636 | +8207074.83 ± 12.15 | ±0.37 |
| ${}^{126}$Xe | 126 | 72 | 105.1856 | -901130.72 ± 0.0355 | 118237.8116 | 117279.1107 | +8174524.09 ± 0.05 | ±0.37 |
| ${}^{127}$Xe | 127 | 73 | 111.3821 | -896014.53 ± 3.8178 | 119171.1805 | 118211.4303 | +8118929.13 ± 34.58 | ±0.38 |
| ${}^{128}$Xe | 128 | 74 | 117.5683 | -891215.24 ± 0.0355 | 120104.5597 | 119141.3847 | +8084302.54 ± 0.04 | ±0.38 |
| ${}^{129}$Xe | 129 | 75 | 123.7444 | -886227.69 ± 0.0356 | 121037.9491 | 120074.0433 | +8027594.97 ± 0.04 | ±0.38 |
| ${}^{130}$Xe | 130 | 76 | 129.9105 | -881566.33 ± 0.0356 | 121971.3484 | 121004.3530 | +7991409.98 ± 0.08 | ±0.38 |
| ${}^{131}$Xe | 131 | 77 | 136.0668 | -876696.27 ± 0.0356 | 122904.7575 | 121937.3140 | +7933941.17 ± 0.04 | ±0.39 |
| ${}^{132}$Xe | 132 | 78 | 142.2136 | -872161.40 ± 0.0356 | 123838.1762 | 122867.9427 | +7896554.99 ± 0.04 | ±0.39 |
| ${}^{133}$Xe | 133 | 79 | 148.3508 | -867411.55 ± 2.1396 | 124771.6043 | 123801.0722 | +7839448.35 ± 19.38 | ±0.39 |
| ${}^{134}$Xe | 134 | 80 | 154.4788 | -862982.12 ± 0.0357 | 125705.0417 | 124732.0841 | +7800380.24 ± 0.04 | ±0.39 |
| ${}^{135}$Xe | 135 | 81 | 160.5977 | -858353.78 ± 3.2387 | 126638.4883 | 125665.2906 | +7744363.28 ± 29.19 | ±0.39 |
| ${}^{136}$Xe | 136 | 82 | 166.7076 | -854006.23 ± 0.0357 | 127571.9438 | 126596.7689 | +7702999.84 ± 0.05 | ±0.40 |
| ${}^{137}$Xe | 137 | 83 | 172.8087 | -849194.88 ± 0.0956 | 128505.4082 | 127532.3088 | +7630218.52 ± 0.81 | ±0.40 |
| ${}^{138}$Xe | 138 | 84 | 178.9011 | -844645.59 ± 2.4327 | 129438.8812 | 128466.2141 | +7571384.83 ± 21.83 | ±0.40 |
| ${}^{139}$Xe | 139 | 85 | 184.9849 | -839883.02 ± 1.8528 | 130372.3628 | 129402.0358 | +7498544.73 ± 16.56 | ±0.40 |
| ${}^{140}$Xe | 140 | 86 | 191.0604 | -835395.55 ± 2.0022 | 131305.8528 | 130336.1881 | +7439719.61 ± 17.87 | ±0.40 |
| ${}^{141}$Xe | 141 | 87 | 197.1276 | -830647.35 ± 2.4832 | 132239.3510 | 131272.4713 | +7365441.21 ± 22.00 | ±0.40 |
| ${}^{142}$Xe | 142 | 88 | 203.1866 | -826204.02 ± 2.3077 | 133172.8573 | 132206.9331 | +7306154.42 ± 20.43 | ±0.41 |
| ${}^{143}$Xe | 143 | 89 | 209.2377 | -821493.10 ± 3.9771 | 134106.3717 | 133143.4539 | +7232182.53 ± 34.98 | ±0.41 |
| ${}^{144}$Xe | 144 | 90 | 215.2809 | -817077.30 ± 4.5149 | 135039.8939 | 134078.2786 | +7172043.99 ± 39.60 | ±0.41 |
| ${}^{145}$Xe | 145 | 91 | 221.3163 | -812378.25 ± 9.4775 | 135973.4239 | 135015.1517 | +7097516.24 ± 82.79 | ±0.41 |
| ${}^{146}$Xe | 146 | 92 | 227.3441 | -808005.95 ± 20.4552 | 136906.9615 | 135950.1842 | +7037705.49 ± 178.15 | ±0.41 |
| ${}^{147}$Xe | 147 | 93 | 233.3644 | -803330.89 ± 123.8850 | 137840.5067 | 136887.2335 | +6963930.47 ± 1463.04 | ±0.41 |
| ${}^{148}$Xe | 148 | 94 | 239.3773 | -799004.06 ± 248.5398 | 138774.0592 | 137822.4778 | +6904399.15 ± 2176.29 | ±0.42 |
| ${}^{149}$Xe | 149 | 95 | 245.3829 | -794373.16 ± 249.7191 | 139707.6190 | 138759.6214 | +6831941.28 ± 2161.59 | ±0.42 |
| ${}^{150}$Xe | 150 | 96 | 251.3814 | -790069.41 ± 250.5324 | 140641.1860 | 139695.1256 | +6772322.00 ± 2147.11 | ±0.42 |

### Caesium (Z = 55)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{111}$Cs | 111 | 56 | -7.5744 | -1008455.73 ± 247.8315 | 104256.3079 | 103352.9456 | +8740557.56 ± 1937.74 | ±0.33 |
| ${}^{112}$Cs | 112 | 57 | -1.1523 | -1001269.87 ± 123.4263 | 105189.4513 | 104280.9251 | +8712294.56 ± 1107.64 | ±0.33 |
| ${}^{113}$Cs | 113 | 58 | 5.2555 | -994292.38 ± 9.3145 | 106122.6088 | 105207.0692 | +8702263.68 ± 81.52 | ±0.34 |
| ${}^{114}$Cs | 114 | 59 | 11.6494 | -987497.74 ± 91.2942 | 107055.7804 | 106135.6419 | +8669457.75 ± 801.49 | ±0.34 |
| ${}^{115}$Cs | 115 | 60 | 18.0297 | -980917.75 ± 121.7137 | 107988.9656 | 107062.1225 | +8657058.71 ± 957.06 | ±0.34 |
| ${}^{116}$Cs | 116 | 61 | 24.3965 | -974460.88 ± 121.4329 | 108922.1641 | 107991.2739 | +8620050.91 ± 931.57 | ±0.34 |
| ${}^{117}$Cs | 117 | 62 | 30.7502 | -968226.98 ± 64.4836 | 109855.3759 | 108918.3170 | +8603317.38 ± 573.00 | ±0.35 |
| ${}^{118}$Cs | 118 | 63 | 37.0910 | -962066.74 ± 13.0455 | 110788.6005 | 109847.8949 | +8563711.22 ± 116.09 | ±0.35 |
| ${}^{119}$Cs | 119 | 64 | 43.4191 | -956131.78 ± 14.0790 | 111721.8378 | 110775.4933 | +8542904.89 ± 125.84 | ±0.35 |
| ${}^{120}$Cs | 120 | 65 | 49.7349 | -950236.14 ± 9.9778 | 112655.0875 | 111705.4038 | +8501680.59 ± 89.24 | ±0.35 |
| ${}^{121}$Cs | 121 | 66 | 56.0385 | -944554.96 ± 14.1388 | 113588.3493 | 112633.6842 | +8475840.13 ± 126.86 | ±0.36 |
| ${}^{122}$Cs | 122 | 67 | 62.3301 | -938881.08 ± 33.0297 | 114521.6231 | 113564.1359 | +8431246.43 ± 296.63 | ±0.36 |
| ${}^{123}$Cs | 123 | 68 | 68.6100 | -933439.19 ± 11.7536 | 115454.9086 | 114492.7311 | +8403830.59 ± 105.77 | ±0.36 |
| ${}^{124}$Cs | 124 | 69 | 74.8784 | -927970.75 ± 8.8030 | 116388.2056 | 115423.5278 | +8357722.71 ± 79.27 | ±0.36 |
| ${}^{125}$Cs | 125 | 70 | 81.1355 | -922726.29 ± 7.3692 | 117321.5140 | 116352.6732 | +8326759.61 ± 66.48 | ±0.37 |
| ${}^{126}$Cs | 126 | 71 | 87.3815 | -917432.80 ± 9.7866 | 118254.8334 | 117283.9064 | +8278433.29 ± 88.32 | ±0.37 |
| ${}^{127}$Cs | 127 | 72 | 93.6166 | -912366.02 ± 5.2190 | 119188.1637 | 118213.5111 | +8244849.00 ± 47.18 | ±0.37 |
| ${}^{128}$Cs | 128 | 73 | 99.8410 | -907213.66 ± 4.9961 | 120121.5047 | 119145.3135 | +8193282.46 ± 45.12 | ±0.37 |
| ${}^{129}$Cs | 129 | 74 | 106.0549 | -902313.87 ± 4.1944 | 121054.8562 | 120075.2403 | +8158350.61 ± 37.92 | ±0.38 |
| ${}^{130}$Cs | 130 | 75 | 112.2585 | -897306.60 ± 7.6468 | 121988.2181 | 121007.3337 | +8105991.09 ± 69.06 | ±0.38 |
| ${}^{131}$Cs | 131 | 76 | 118.4519 | -892547.90 ± 0.1664 | 122921.5901 | 121937.6720 | +8069024.76 ± 1.45 | ±0.38 |
| ${}^{132}$Cs | 132 | 77 | 124.6353 | -887669.13 ± 0.9399 | 123854.9721 | 122870.0690 | +8015809.71 ± 8.43 | ±0.38 |
| ${}^{133}$Cs | 133 | 78 | 130.8090 | -883052.50 ± 0.0357 | 124788.3639 | 123800.6449 | +7978302.76 ± 0.06 | ±0.38 |
| ${}^{134}$Cs | 134 | 79 | 136.9730 | -878291.56 ± 0.0357 | 125721.7653 | 124733.3187 | +7924479.03 ± 0.13 | ±0.39 |
| ${}^{135}$Cs | 135 | 80 | 143.1275 | -873805.41 ± 0.3214 | 126655.1762 | 125664.1220 | +7886532.28 ± 2.89 | ±0.39 |
| ${}^{136}$Cs | 136 | 81 | 149.2727 | -869174.84 ± 1.6449 | 127588.5964 | 126596.8593 | +7833821.24 ± 14.79 | ±0.39 |
| ${}^{137}$Cs | 137 | 82 | 155.4087 | -864778.16 ± 0.2622 | 128522.0258 | 127528.1464 | +7793411.74 ± 2.37 | ±0.39 |
| ${}^{138}$Cs | 138 | 83 | 161.5358 | -859984.57 ± 7.9424 | 129455.4642 | 128463.2993 | +7723333.41 ± 71.29 | ±0.39 |
| ${}^{139}$Cs | 139 | 84 | 167.6540 | -855419.03 ± 2.6971 | 130388.9114 | 129396.9793 | +7665805.65 ± 24.22 | ±0.40 |
| ${}^{140}$Cs | 140 | 85 | 173.7634 | -850719.39 ± 7.0481 | 131322.3674 | 130332.1248 | +7597839.81 ± 62.90 | ±0.40 |
| ${}^{141}$Cs | 141 | 86 | 179.8643 | -846204.65 ± 7.8608 | 132255.8319 | 131266.1913 | +7539189.23 ± 70.05 | ±0.40 |
| ${}^{142}$Cs | 142 | 87 | 185.9567 | -841551.87 ± 6.0255 | 133189.3049 | 132201.6482 | +7470835.28 ± 53.45 | ±0.40 |
| ${}^{143}$Cs | 143 | 88 | 192.0409 | -837094.03 ± 6.4292 | 134122.7862 | 133135.9813 | +7412007.41 ± 56.88 | ±0.40 |
| ${}^{144}$Cs | 144 | 89 | 198.1168 | -832461.05 ± 17.0241 | 135056.2757 | 134071.8796 | +7342300.86 ± 150.15 | ±0.40 |
| ${}^{145}$Cs | 145 | 90 | 204.1848 | -828035.60 ± 7.6324 | 135989.7732 | 135006.5906 | +7282478.08 ± 67.15 | ±0.41 |
| ${}^{146}$Cs | 146 | 91 | 210.2448 | -823426.67 ± 2.4278 | 136923.2786 | 135942.8288 | +7212221.62 ± 21.28 | ±0.41 |
| ${}^{147}$Cs | 147 | 92 | 216.2970 | -819055.10 ± 7.0095 | 137856.7918 | 136877.7132 | +7152943.97 ± 61.25 | ±0.41 |
| ${}^{148}$Cs | 148 | 93 | 222.3415 | -814473.76 ± 10.8798 | 138790.3127 | 137814.2164 | +7082696.57 ± 94.63 | ±0.41 |
| ${}^{149}$Cs | 149 | 94 | 228.3785 | -810139.80 ± 371.6091 | 139723.8411 | 138749.3219 | +7023596.45 ± 2880.09 | ±0.41 |
| ${}^{150}$Cs | 150 | 95 | 234.4080 | -805607.66 ± 373.1807 | 140657.3770 | 139685.9457 | +6954395.37 ± 2860.78 | ±0.41 |
| ${}^{151}$Cs | 151 | 96 | 240.4302 | -801291.28 ± 374.3916 | 141590.9202 | 140621.3297 | +6895045.69 ± 3557.16 | ±0.42 |
| ${}^{152}$Cs | 152 | 97 | 246.4452 | -796823.32 ± 375.9398 | 142524.4707 | 141557.9741 | +6827567.35 ± 3533.62 | ±0.42 |

### Barium (Z = 56)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{113}$Ba | 113 | 57 | -13.3820 | -1014738.64 ± 373.3665 | 106140.4641 | 105219.1241 | +8756392.39 ± 2850.63 | ±0.33 |
| ${}^{114}$Ba | 114 | 58 | -6.9429 | -1007528.40 ± 111.3393 | 107073.5903 | 106144.4224 | +8753808.58 ± 967.32 | ±0.33 |
| ${}^{115}$Ba | 115 | 59 | -0.5179 | -1000554.90 ± 246.4268 | 108006.7308 | 107072.9017 | +8721432.47 ± 1870.42 | ±0.34 |
| ${}^{116}$Ba | 116 | 60 | 5.8931 | -993775.67 ± 245.0380 | 108939.8852 | 107998.9363 | +8712574.96 ± 1854.38 | ±0.34 |
| ${}^{117}$Ba | 117 | 61 | 12.2906 | -987170.46 ± 261.3107 | 109873.0532 | 108927.3522 | +8681941.81 ± 2298.21 | ±0.34 |
| ${}^{118}$Ba | 118 | 62 | 18.6746 | -980763.39 ± 243.1020 | 110806.2345 | 109854.1047 | +8667221.68 ± 1823.07 | ±0.34 |
| ${}^{119}$Ba | 119 | 63 | 25.0456 | -974476.25 ± 204.0886 | 111739.4290 | 110783.2082 | +8631459.41 ± 1807.75 | ±0.35 |
| ${}^{120}$Ba | 120 | 64 | 31.4036 | -968395.20 ± 302.0907 | 112672.6364 | 111710.4038 | +8613634.29 ± 2687.00 | ±0.35 |
| ${}^{121}$Ba | 121 | 65 | 37.7491 | -962384.93 ± 141.3929 | 113605.8563 | 112640.0417 | +8574345.49 ± 1259.74 | ±0.35 |
| ${}^{122}$Ba | 122 | 66 | 44.0822 | -956590.62 ± 27.5236 | 114539.0887 | 113567.6717 | +8553640.17 ± 246.06 | ±0.35 |
| ${}^{123}$Ba | 123 | 67 | 50.4030 | -950807.85 ± 11.8244 | 115472.3332 | 114498.1198 | +8508553.97 ± 105.76 | ±0.36 |
| ${}^{124}$Ba | 124 | 68 | 56.7120 | -945265.11 ± 12.0634 | 116405.5897 | 115426.1791 | +8485168.79 ± 108.27 | ±0.36 |
| ${}^{125}$Ba | 125 | 69 | 63.0092 | -939690.93 ± 10.5166 | 117338.8579 | 116357.0940 | +8437507.75 ± 94.46 | ±0.36 |
| ${}^{126}$Ba | 126 | 70 | 69.2950 | -934370.09 ± 11.8381 | 118272.1376 | 117285.5872 | +8411522.94 ± 106.55 | ±0.36 |
| ${}^{127}$Ba | 127 | 71 | 75.5694 | -928980.38 ± 10.6702 | 119205.4286 | 118216.9332 | +8361706.83 ± 96.07 | ±0.37 |
| ${}^{128}$Ba | 128 | 72 | 81.8327 | -923854.31 ± 1.5007 | 120138.7306 | 119145.8761 | +8333100.25 ± 13.51 | ±0.37 |
| ${}^{129}$Ba | 129 | 73 | 88.0852 | -918624.23 ± 9.7008 | 121072.0436 | 120077.6785 | +8281015.66 ± 87.47 | ±0.37 |
| ${}^{130}$Ba | 130 | 74 | 94.3269 | -913676.74 ± 0.2617 | 122005.3674 | 121006.9767 | +8250686.73 ± 2.37 | ±0.37 |
| ${}^{131}$Ba | 131 | 75 | 100.5580 | -908601.06 ± 0.3810 | 122938.7016 | 121939.0486 | +8197972.59 ± 3.40 | ±0.38 |
| ${}^{132}$Ba | 132 | 76 | 106.7789 | -903806.05 ± 0.9513 | 123872.0462 | 122868.7868 | +8165291.08 ± 8.57 | ±0.38 |
| ${}^{133}$Ba | 133 | 77 | 112.9895 | -898866.11 ± 0.8928 | 124805.4010 | 123801.1623 | +8111706.33 ± 8.01 | ±0.38 |
| ${}^{134}$Ba | 134 | 78 | 119.1902 | -894212.55 ± 0.2260 | 125738.7657 | 124731.2599 | +8077412.31 ± 2.01 | ±0.38 |
| ${}^{135}$Ba | 135 | 79 | 125.3811 | -889402.23 ± 0.2143 | 126672.1403 | 125663.8533 | +8023683.17 ± 1.95 | ±0.38 |
| ${}^{136}$Ba | 136 | 80 | 131.5622 | -884874.76 ± 0.2142 | 127605.5245 | 126594.3110 | +7987827.44 ± 1.93 | ±0.39 |
| ${}^{137}$Ba | 137 | 81 | 137.7339 | -880198.10 ± 0.2145 | 128538.9183 | 127526.9708 | +7935164.38 ± 1.94 | ±0.39 |
| ${}^{138}$Ba | 138 | 82 | 143.8962 | -875768.63 ± 0.2145 | 129472.3214 | 128457.9245 | +7896724.74 ± 1.94 | ±0.39 |
| ${}^{139}$Ba | 139 | 83 | 150.0494 | -870982.50 ± 0.2151 | 130405.7337 | 129392.7665 | +7828622.82 ± 1.95 | ±0.39 |
| ${}^{140}$Ba | 140 | 84 | 156.1935 | -866437.49 ± 6.7519 | 131339.1550 | 130325.9066 | +7774727.24 ± 60.61 | ±0.39 |
| ${}^{141}$Ba | 141 | 85 | 162.3287 | -861727.55 ± 4.5279 | 132272.5852 | 131260.9361 | +7707160.35 ± 40.51 | ±0.40 |
| ${}^{142}$Ba | 142 | 86 | 168.4551 | -857260.54 ± 5.0175 | 133206.0242 | 132194.3205 | +7653155.73 ± 44.78 | ±0.40 |
| ${}^{143}$Ba | 143 | 87 | 174.5729 | -852597.00 ± 5.6991 | 134139.4718 | 133129.7196 | +7584723.83 ± 50.75 | ±0.40 |
| ${}^{144}$Ba | 144 | 88 | 180.6823 | -848194.90 ± 6.0009 | 135072.9279 | 134063.3838 | +7530348.83 ± 53.23 | ±0.40 |
| ${}^{145}$Ba | 145 | 89 | 186.7833 | -843571.08 ± 7.1040 | 136006.3923 | 134999.1289 | +7461258.57 ± 62.79 | ±0.40 |
| ${}^{146}$Ba | 146 | 90 | 192.8761 | -839198.52 ± 1.4728 | 136939.8649 | 135933.2729 | +7405045.09 ± 13.02 | ±0.40 |
| ${}^{147}$Ba | 147 | 91 | 198.9608 | -834604.03 ± 16.4116 | 137873.3456 | 136869.3692 | +7335289.09 ± 144.28 | ±0.41 |
| ${}^{148}$Ba | 148 | 92 | 205.0376 | -830307.45 ± 1.2371 | 138806.8343 | 137803.5824 | +7280303.01 ± 10.82 | ±0.41 |
| ${}^{149}$Ba | 149 | 93 | 211.1065 | -825768.79 ± 2.0782 | 139740.3308 | 138739.7908 | +7211629.39 ± 18.13 | ±0.41 |
| ${}^{150}$Ba | 150 | 94 | 217.1677 | -821522.08 ± 4.6722 | 140673.8350 | 139674.2258 | +7156719.55 ± 40.68 | ±0.41 |
| ${}^{151}$Ba | 151 | 95 | 223.2213 | -817021.11 ± 371.3331 | 141607.3469 | 140610.6697 | +7088204.12 ± 2841.97 | ±0.41 |
| ${}^{152}$Ba | 152 | 96 | 229.2674 | -812791.63 ± 372.3470 | 142540.8662 | 141545.4939 | +7032172.00 ± 2823.20 | ±0.41 |
| ${}^{153}$Ba | 153 | 97 | 235.3061 | -808307.59 ± 373.9250 | 143474.3929 | 142482.1280 | +6964135.70 ± 2804.64 | ±0.42 |
| ${}^{154}$Ba | 154 | 98 | 241.3375 | -804133.64 ± 374.9531 | 144407.9269 | 143417.1720 | +6908202.17 ± 3487.81 | ±0.42 |

### Lanthanum (Z = 57)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{116}$La | 116 | 59 | -12.9002 | -1013845.71 ± 373.5060 | 108957.8962 | 108013.2664 | +8745497.51 ± 2975.24 | ±0.33 |
| ${}^{117}$La | 117 | 60 | -6.4582 | -1006826.45 ± 247.3411 | 109891.0197 | 108938.5391 | +8743283.71 ± 1838.39 | ±0.34 |
| ${}^{118}$La | 118 | 61 | -0.0301 | -1000031.48 ± 369.7313 | 110824.1570 | 109866.6845 | +8714857.40 ± 2730.05 | ±0.34 |
| ${}^{119}$La | 119 | 62 | 6.3844 | -993424.42 ± 367.6921 | 111757.3079 | 110792.7787 | +8705704.28 ± 2707.23 | ±0.34 |
| ${}^{120}$La | 120 | 63 | 12.7855 | -986973.20 ± 244.5287 | 112690.4721 | 111721.7224 | +8671095.68 ± 2684.72 | ±0.34 |
| ${}^{121}$La | 121 | 64 | 19.1736 | -980715.62 ± 243.3978 | 113623.6495 | 112648.5963 | +8655706.51 ± 2662.63 | ±0.35 |
| ${}^{122}$La | 122 | 65 | 25.5489 | -974569.89 ± 242.8658 | 114556.8396 | 113577.7374 | +8620546.96 ± 2624.44 | ±0.35 |
| ${}^{123}$La | 123 | 66 | 31.9115 | -968617.01 ± 241.9257 | 115490.0424 | 114505.1236 | +8601525.93 ± 1708.34 | ±0.35 |
| ${}^{124}$La | 124 | 67 | 38.2618 | -962726.29 ± 55.2046 | 116423.2576 | 115435.0102 | +8561071.27 ± 490.91 | ±0.35 |
| ${}^{125}$La | 125 | 68 | 44.5999 | -957036.20 ± 25.0462 | 117356.4849 | 116363.0035 | +8537777.48 ± 223.41 | ±0.36 |
| ${}^{126}$La | 126 | 69 | 50.9261 | -951377.00 ± 86.4128 | 118289.7241 | 117293.2836 | +8495290.76 ± 771.63 | ±0.36 |
| ${}^{127}$La | 127 | 70 | 57.2405 | -945915.80 ± 24.5634 | 119222.9751 | 118221.8551 | +8468146.95 ± 219.92 | ±0.36 |
| ${}^{128}$La | 128 | 71 | 63.5435 | -940455.53 ± 51.0244 | 120156.2376 | 119152.6198 | +8422959.77 ± 456.96 | ±0.36 |
| ${}^{129}$La | 129 | 72 | 69.8351 | -935213.64 ± 19.8060 | 121089.5113 | 120081.4158 | +8395099.95 ± 177.74 | ±0.37 |
| ${}^{130}$La | 130 | 73 | 76.1157 | -929931.56 ± 23.8865 | 122022.7962 | 121012.6061 | +8347808.75 ± 214.41 | ±0.37 |
| ${}^{131}$La | 131 | 74 | 82.3853 | -924866.42 ± 25.4828 | 122956.0920 | 121941.9583 | +8316527.63 ± 229.16 | ±0.37 |
| ${}^{132}$La | 132 | 75 | 88.6442 | -919745.83 ± 32.9120 | 123889.3985 | 122873.4981 | +8267855.99 ± 295.90 | ±0.37 |
| ${}^{133}$La | 133 | 76 | 94.8926 | -914847.62 ± 25.0751 | 124822.7156 | 123803.2214 | +8234795.02 ± 225.72 | ±0.37 |
| ${}^{134}$La | 134 | 77 | 101.1306 | -909880.34 ± 17.7563 | 125756.0430 | 124734.9912 | +8185768.25 ± 159.77 | ±0.38 |
| ${}^{135}$La | 135 | 78 | 107.3584 | -905133.37 ± 8.3385 | 126689.3806 | 125665.0605 | +8151191.94 ± 75.06 | ±0.38 |
| ${}^{136}$La | 136 | 79 | 113.5762 | -900296.76 ± 46.6807 | 127622.7282 | 126597.1606 | +8101031.42 ± 420.00 | ±0.38 |
| ${}^{137}$La | 137 | 80 | 119.7842 | -895687.23 ± 1.4317 | 128556.0857 | 127527.5513 | +8065193.03 ± 12.86 | ±0.38 |
| ${}^{138}$La | 138 | 81 | 125.9825 | -890996.14 ± 0.3582 | 129489.4528 | 128459.6729 | +8016367.25 ± 3.23 | ±0.38 |
| ${}^{139}$La | 139 | 82 | 132.1712 | -886503.69 ± 0.5252 | 130422.8295 | 129390.4580 | +7978729.54 ± 4.69 | ±0.39 |
| ${}^{140}$La | 140 | 83 | 138.3506 | -881721.61 ± 0.5147 | 131356.2156 | 130324.8625 | +7913709.51 ± 4.65 | ±0.39 |
| ${}^{141}$La | 141 | 84 | 144.5207 | -877149.18 ± 3.5118 | 132289.6108 | 131257.7388 | +7861418.87 ± 31.44 | ±0.39 |
| ${}^{142}$La | 142 | 85 | 150.6818 | -872471.89 ± 5.3240 | 133223.0152 | 132192.1388 | +7798318.64 ± 47.55 | ±0.39 |
| ${}^{143}$La | 143 | 86 | 156.8339 | -867960.04 ± 6.1762 | 134156.4285 | 133125.4854 | +7744145.41 ± 55.05 | ±0.39 |
| ${}^{144}$La | 144 | 87 | 162.9773 | -863334.37 ± 10.8435 | 135089.8506 | 134060.3013 | +7679747.59 ± 96.50 | ±0.40 |
| ${}^{145}$La | 145 | 88 | 169.1120 | -858906.71 ± 10.2346 | 136023.2813 | 134993.8097 | +7626064.92 ± 90.88 | ±0.40 |
| ${}^{146}$La | 146 | 89 | 175.2382 | -854337.19 ± 1.3956 | 136956.7205 | 135928.9180 | +7561323.59 ± 12.31 | ±0.40 |
| ${}^{147}$La | 147 | 90 | 181.3560 | -849941.49 ± 8.8669 | 137890.1681 | 136862.9548 | +7505414.96 ± 78.27 | ±0.40 |
| ${}^{148}$La | 148 | 91 | 187.4655 | -845410.94 ± 16.0489 | 138823.6240 | 137798.4186 | +7439892.18 ± 141.28 | ±0.40 |
| ${}^{149}$La | 149 | 92 | 193.5670 | -841110.98 ± 164.3797 | 139757.0880 | 138732.4015 | +7386064.36 ± 1443.51 | ±0.40 |
| ${}^{150}$La | 150 | 93 | 199.6604 | -836667.28 ± 2.0615 | 140690.5600 | 139667.8044 | +7322772.56 ± 18.01 | ±0.41 |
| ${}^{151}$La | 151 | 94 | 205.7459 | -832384.24 ± 354.7650 | 141624.0399 | 140602.2993 | +7266883.52 ± 3097.20 | ±0.41 |
| ${}^{152}$La | 152 | 95 | 211.8237 | -827995.93 ± 246.8526 | 142557.5275 | 141537.8138 | +7204532.23 ± 2119.16 | ±0.41 |
| ${}^{153}$La | 153 | 96 | 217.8938 | -823766.52 ± 247.4941 | 143491.0228 | 142472.5383 | +7148637.32 ± 2105.26 | ±0.41 |
| ${}^{154}$La | 154 | 97 | 223.9564 | -819368.70 ± 248.4163 | 144424.5256 | 143408.5622 | +7084398.25 ± 2091.51 | ±0.41 |
| ${}^{155}$La | 155 | 98 | 230.0116 | -815153.72 ± 373.6921 | 145358.0359 | 144343.6556 | +7027535.86 ± 2768.47 | ±0.41 |
| ${}^{156}$La | 156 | 99 | 236.0595 | -810778.82 ± 375.1407 | 146291.5534 | 145280.0298 | +6962578.24 ± 2750.63 | ±0.42 |
| ${}^{157}$La | 157 | 100 | 242.1001 | -806568.11 ± 250.8781 | 147225.0782 | 146215.5042 | +6904698.44 ± 2051.36 | ±0.42 |

### Cerium (Z = 58)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{119}$Ce | 119 | 61 | -12.5645 | -1013102.98 ± 496.4011 | 111775.4744 | 110803.9781 | +8767702.55 ± 4514.39 | ±0.34 |
| ${}^{120}$Ce | 120 | 62 | -6.1194 | -1006289.49 ± 493.3399 | 112708.5948 | 111729.5628 | +8762515.20 ± 4476.99 | ±0.34 |
| ${}^{121}$Ce | 121 | 63 | 0.3121 | -999682.85 ± 368.9129 | 113641.7287 | 112658.0966 | +8731126.67 ± 3555.38 | ±0.34 |
| ${}^{122}$Ce | 122 | 64 | 6.7302 | -993251.05 ± 367.0174 | 114574.8759 | 113584.4069 | +8720114.31 ± 3526.39 | ±0.34 |
| ${}^{123}$Ce | 123 | 65 | 13.1354 | -986965.50 ± 244.1108 | 115508.0362 | 114513.4885 | +8684983.67 ± 2603.00 | ±0.35 |
| ${}^{124}$Ce | 124 | 66 | 19.5277 | -980862.65 ± 243.0429 | 116441.2094 | 115440.3530 | +8669900.00 ± 2582.10 | ±0.35 |
| ${}^{125}$Ce | 125 | 67 | 25.9074 | -974853.29 ± 242.6595 | 117374.3951 | 116370.1052 | +8630135.80 ± 1680.96 | ±0.35 |
| ${}^{126}$Ce | 126 | 68 | 32.2748 | -969038.94 ± 26.8093 | 118307.5931 | 117297.4365 | +8611924.07 ± 238.24 | ±0.35 |
| ${}^{127}$Ce | 127 | 69 | 38.6300 | -963267.64 ± 27.4611 | 119240.8033 | 118227.7718 | +8568473.17 ± 244.24 | ±0.36 |
| ${}^{128}$Ce | 128 | 70 | 44.9733 | -957703.52 ± 26.2793 | 120174.0254 | 119155.7114 | +8546078.72 ± 234.52 | ±0.36 |
| ${}^{129}$Ce | 129 | 71 | 51.3049 | -952145.95 ± 26.0620 | 121107.2593 | 120086.4519 | +8500604.19 ± 232.71 | ±0.36 |
| ${}^{130}$Ce | 130 | 72 | 57.6250 | -946806.99 ± 25.8004 | 122040.5046 | 121014.8106 | +8475772.78 ± 230.92 | ±0.36 |
| ${}^{131}$Ce | 131 | 73 | 63.9337 | -941435.19 ± 30.0478 | 122973.7613 | 121946.0191 | +8427844.71 ± 268.98 | ±0.37 |
| ${}^{132}$Ce | 132 | 74 | 70.2314 | -936298.42 ± 18.5098 | 123907.0290 | 122874.7530 | +8401042.33 ± 166.07 | ±0.37 |
| ${}^{133}$Ce | 133 | 75 | 76.5182 | -931097.46 ± 14.7308 | 124840.3077 | 123806.2976 | +8351837.72 ± 132.10 | ±0.37 |
| ${}^{134}$Ce | 134 | 76 | 82.7942 | -926143.46 ± 18.1812 | 125773.5971 | 124735.3770 | +8323381.14 ± 163.44 | ±0.37 |
| ${}^{135}$Ce | 135 | 77 | 89.0596 | -921107.14 ± 9.0887 | 126706.8970 | 125667.0877 | +8274317.25 ± 81.69 | ±0.37 |
| ${}^{136}$Ce | 136 | 78 | 95.3147 | -916304.82 ± 0.2866 | 127640.2074 | 126596.6896 | +8242852.41 ± 2.56 | ±0.38 |
| ${}^{137}$Ce | 137 | 79 | 101.5596 | -911403.27 ± 0.3107 | 128573.5279 | 127528.7734 | +8192304.00 ± 2.82 | ±0.38 |
| ${}^{138}$Ce | 138 | 80 | 107.7944 | -906754.76 ± 0.4297 | 129506.8585 | 128458.6204 | +8160122.31 ± 3.89 | ±0.38 |
| ${}^{139}$Ce | 139 | 81 | 114.0194 | -902002.64 ± 1.7920 | 130440.1989 | 129390.7227 | +8110908.20 ± 16.14 | ±0.38 |
| ${}^{140}$Ce | 140 | 82 | 120.2347 | -897470.40 ± 1.1222 | 131373.5491 | 130321.1003 | +8075812.82 ± 10.07 | ±0.38 |
| ${}^{141}$Ce | 141 | 83 | 126.4404 | -892675.29 ± 1.1131 | 132306.9088 | 131255.2376 | +8012413.60 ± 10.01 | ±0.39 |
| ${}^{142}$Ce | 142 | 84 | 132.6367 | -888097.10 ± 2.0606 | 133240.2779 | 132187.6298 | +7963287.45 ± 18.48 | ±0.39 |
| ${}^{143}$Ce | 143 | 85 | 138.8238 | -883383.38 ± 2.0541 | 134173.6563 | 133122.0505 | +7899561.56 ± 18.34 | ±0.39 |
| ${}^{144}$Ce | 144 | 86 | 145.0017 | -878895.32 ± 2.3693 | 135107.0437 | 134054.7190 | +7849964.27 ± 21.13 | ±0.39 |
| ${}^{145}$Ce | 145 | 87 | 151.1707 | -874237.35 ± 28.2031 | 136040.4402 | 134989.5780 | +7784765.36 ± 251.13 | ±0.39 |
| ${}^{146}$Ce | 146 | 88 | 157.3309 | -869830.53 ± 12.1278 | 136973.8454 | 135922.5133 | +7734790.31 ± 107.89 | ±0.39 |
| ${}^{147}$Ce | 147 | 89 | 163.4824 | -865238.22 ± 7.0766 | 137907.2593 | 136857.6193 | +7669576.59 ± 62.69 | ±0.40 |
| ${}^{148}$Ce | 148 | 90 | 169.6254 | -860914.64 ± 9.1743 | 138840.6818 | 137790.7289 | +7619909.52 ± 81.24 | ±0.40 |
| ${}^{149}$Ce | 149 | 91 | 175.7599 | -856395.95 ± 8.3757 | 139774.1127 | 138725.9515 | +7555624.30 ± 73.86 | ±0.40 |
| ${}^{150}$Ce | 150 | 92 | 181.8861 | -852145.34 ± 9.5109 | 140707.5519 | 139659.2687 | +7506005.16 ± 83.75 | ±0.40 |
| ${}^{151}$Ce | 151 | 93 | 188.0042 | -847722.76 ± 14.3342 | 141640.9992 | 140594.3846 | +7444213.60 ± 125.88 | ±0.40 |
| ${}^{152}$Ce | 152 | 94 | 194.1142 | -843515.82 ± 122.5340 | 142574.4546 | 141528.1234 | +7393097.39 ± 1415.06 | ±0.41 |
| ${}^{153}$Ce | 153 | 95 | 200.2164 | -839119.30 ± 122.9407 | 143507.9179 | 142463.6882 | +7329796.05 ± 1405.77 | ±0.41 |
| ${}^{154}$Ce | 154 | 96 | 206.3107 | -834933.51 ± 123.2134 | 144441.3890 | 143397.8724 | +7277071.95 ± 1396.61 | ±0.41 |
| ${}^{155}$Ce | 155 | 97 | 212.3973 | -830554.59 ± 247.3105 | 145374.8679 | 144333.8060 | +7212875.93 ± 2078.11 | ±0.41 |
| ${}^{156}$Ce | 156 | 98 | 218.4763 | -826414.32 ± 247.8929 | 146308.3542 | 145268.2604 | +7159814.69 ± 2064.74 | ±0.41 |
| ${}^{157}$Ce | 157 | 99 | 224.5479 | -822042.88 ± 373.2736 | 147241.8481 | 146204.6439 | +7094194.34 ± 2733.23 | ±0.41 |
| ${}^{158}$Ce | 158 | 100 | 230.6121 | -817895.16 ± 374.2982 | 148175.3493 | 147139.5287 | +7039716.87 ± 2715.86 | ±0.41 |
| ${}^{159}$Ce | 159 | 101 | 236.6691 | -813543.19 ± 375.7986 | 149108.8578 | 148076.2224 | +6973674.52 ± 3378.07 | ±0.42 |

### Praseodymium (Z = 59)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{121}$Pr | 121 | 62 | -18.8356 | -1019378.34 ± 497.9460 | 113660.0940 | 112669.2354 | +8794402.80 ± 4439.65 | ±0.34 |
| ${}^{122}$Pr | 122 | 63 | -12.3737 | -1012583.62 ± 496.2779 | 114593.1976 | 113597.5009 | +8765128.01 ± 4403.37 | ±0.34 |
| ${}^{123}$Pr | 123 | 64 | -5.9254 | -1005944.44 ± 370.1876 | 115526.3146 | 114523.5449 | +8756014.05 ± 3489.33 | ±0.34 |
| ${}^{124}$Pr | 124 | 65 | 0.5097 | -999494.26 ± 369.0945 | 116459.4450 | 115452.1178 | +8725064.41 ± 3469.34 | ±0.34 |
| ${}^{125}$Pr | 125 | 66 | 6.9318 | -993209.96 ± 244.8880 | 117392.5883 | 116378.6927 | +8712038.46 ± 2577.29 | ±0.35 |
| ${}^{126}$Pr | 126 | 67 | 13.3410 | -987062.40 ± 244.3793 | 118325.7445 | 117307.9335 | +8676403.69 ± 1667.52 | ±0.35 |
| ${}^{127}$Pr | 127 | 68 | 19.7377 | -981083.83 ± 243.4275 | 119258.9132 | 118235.2079 | +8658210.15 ± 1654.45 | ±0.35 |
| ${}^{128}$Pr | 128 | 69 | 26.1221 | -975199.78 ± 28.3026 | 120192.0943 | 119164.9145 | +8619817.19 ± 250.14 | ±0.35 |
| ${}^{129}$Pr | 129 | 70 | 32.4943 | -969483.60 ± 27.9973 | 121125.2875 | 120092.9658 | +8596021.10 ± 248.21 | ±0.36 |
| ${}^{130}$Pr | 130 | 71 | 38.8546 | -963832.20 ± 59.8275 | 122058.4926 | 121023.0580 | +8555680.08 ± 531.08 | ±0.36 |
| ${}^{131}$Pr | 131 | 72 | 45.2033 | -958356.62 ± 43.2891 | 122991.7094 | 121951.4269 | +8530301.76 ± 385.36 | ±0.36 |
| ${}^{132}$Pr | 132 | 73 | 51.5404 | -952908.93 ± 26.3884 | 123924.9377 | 122881.9942 | +8487358.01 ± 234.99 | ±0.36 |
| ${}^{133}$Pr | 133 | 74 | 57.8662 | -947644.95 ± 11.3113 | 124858.1773 | 123810.7782 | +8459676.41 ± 100.94 | ±0.36 |
| ${}^{134}$Pr | 134 | 75 | 64.1809 | -942383.19 ± 18.2368 | 125791.4281 | 124741.6819 | +8415359.95 ± 162.86 | ±0.37 |
| ${}^{135}$Pr | 135 | 76 | 70.4846 | -937313.85 ± 10.5056 | 126724.6897 | 125670.7681 | +8386370.15 ± 94.03 | ±0.37 |
| ${}^{136}$Pr | 136 | 77 | 76.7777 | -932227.97 ± 10.1080 | 127657.9621 | 126601.8577 | +8341934.65 ± 90.47 | ±0.37 |
| ${}^{137}$Pr | 137 | 78 | 83.0601 | -927319.65 ± 7.1208 | 128591.2451 | 127531.4904 | +8309749.00 ± 63.79 | ±0.37 |
| ${}^{138}$Pr | 138 | 79 | 89.3322 | -922374.66 ± 8.7059 | 129524.5384 | 128463.0574 | +8262927.86 ± 77.93 | ±0.38 |
| ${}^{139}$Pr | 139 | 80 | 95.5940 | -917632.77 ± 3.1499 | 130457.8420 | 129392.8518 | +8230672.83 ± 28.20 | ±0.38 |
| ${}^{140}$Pr | 140 | 81 | 101.8458 | -912841.45 ± 5.2597 | 131391.1556 | 130324.4883 | +8184703.72 ± 47.12 | ±0.38 |
| ${}^{141}$Pr | 141 | 82 | 108.0877 | -908237.83 ± 1.2689 | 132324.4791 | 131254.6541 | +8150758.91 ± 11.40 | ±0.38 |
| ${}^{142}$Pr | 142 | 83 | 114.3199 | -903426.03 ± 1.2715 | 133257.8124 | 132188.3764 | +8090242.46 ± 11.32 | ±0.38 |
| ${}^{143}$Pr | 143 | 84 | 120.5425 | -898798.00 ± 1.5247 | 134191.1552 | 133120.5886 | +8042081.07 ± 13.64 | ±0.38 |
| ${}^{144}$Pr | 144 | 85 | 126.7557 | -894093.29 ± 2.2619 | 135124.5074 | 134054.4003 | +7982633.12 ± 20.20 | ±0.39 |
| ${}^{145}$Pr | 145 | 86 | 132.9596 | -889550.88 ± 5.9382 | 136057.8690 | 134987.0190 | +7932984.41 ± 52.96 | ±0.39 |
| ${}^{146}$Pr | 146 | 87 | 139.1544 | -884894.35 ± 28.4168 | 136991.2396 | 135921.4657 | +7870529.92 ± 252.76 | ±0.39 |
| ${}^{147}$Pr | 147 | 88 | 145.3402 | -880454.17 ± 13.0463 | 137924.6193 | 136854.1892 | +7821683.16 ± 115.85 | ±0.39 |
| ${}^{148}$Pr | 148 | 89 | 151.5171 | -875900.47 ± 12.3158 | 138858.0078 | 137788.5919 | +7761280.09 ± 109.16 | ±0.39 |
| ${}^{149}$Pr | 149 | 90 | 157.6853 | -871540.23 ± 8.0478 | 139791.4050 | 138721.5821 | +7712014.69 ± 71.18 | ±0.40 |
| ${}^{150}$Pr | 150 | 91 | 163.8449 | -867099.57 ± 7.3124 | 140724.8108 | 139655.8150 | +7654501.90 ± 64.54 | ±0.40 |
| ${}^{151}$Pr | 151 | 92 | 169.9961 | -862838.91 ± 9.4056 | 141658.2250 | 140588.8300 | +7606543.24 ± 82.86 | ±0.40 |
| ${}^{152}$Pr | 152 | 93 | 176.1390 | -858459.24 ± 14.9015 | 142591.6476 | 141523.3457 | +7548591.09 ± 130.98 | ±0.40 |
| ${}^{153}$Pr | 153 | 94 | 182.2736 | -854218.62 ± 9.5080 | 143525.0783 | 142457.0294 | +7497341.18 ± 83.40 | ±0.40 |
| ${}^{154}$Pr | 154 | 95 | 188.4002 | -849842.53 ± 79.7074 | 144458.5172 | 143392.2324 | +7436140.68 ± 697.42 | ±0.40 |
| ${}^{155}$Pr | 155 | 96 | 194.5188 | -845658.11 ± 13.6514 | 145391.9640 | 144326.1707 | +7384615.32 ± 119.16 | ±0.41 |
| ${}^{156}$Pr | 156 | 97 | 200.6296 | -841326.35 ± 0.8143 | 146325.4186 | 145261.6309 | +7323253.69 ± 7.05 | ±0.41 |
| ${}^{157}$Pr | 157 | 98 | 206.7326 | -837150.87 ± 2.4982 | 147258.8810 | 146196.1395 | +7269286.03 ± 21.66 | ±0.41 |
| ${}^{158}$Pr | 158 | 99 | 212.8280 | -832856.08 ± 248.1697 | 148192.3510 | 147131.9184 | +7207359.81 ± 2038.59 | ±0.41 |
| ${}^{159}$Pr | 159 | 100 | 218.9159 | -828688.59 ± 373.2736 | 149125.8285 | 148066.7929 | +7152418.66 ± 2698.86 | ±0.41 |
| ${}^{160}$Pr | 160 | 101 | 224.9964 | -824419.05 ± 249.7191 | 150059.3135 | 149002.8569 | +7090176.76 ± 2681.90 | ±0.41 |
| ${}^{161}$Pr | 161 | 102 | 231.0697 | -820283.58 ± 375.6574 | 150992.8057 | 149938.0611 | +7034535.13 ± 3336.13 | ±0.41 |

### Neodymium (Z = 60)

_40 of 40 isotopes with a framework prediction; 40 of 40 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{124}$Nd | 124 | 64 | -18.7921 | -1018816.62 ± 496.6476 | 116477.9644 | 115460.4388 | +8812764.04 ± 4332.33 | ±0.34 |
| ${}^{125}$Nd | 125 | 65 | -12.3270 | -1012204.91 ± 371.2871 | 117411.0647 | 116388.6932 | +8784113.83 ± 3433.42 | ±0.34 |
| ${}^{126}$Nd | 126 | 66 | -5.8751 | -1005740.89 ± 246.2448 | 118344.1783 | 117314.8769 | +8773835.28 ± 2556.72 | ±0.34 |
| ${}^{127}$Nd | 127 | 67 | 0.5638 | -999454.74 ± 245.6399 | 119277.3048 | 118243.8410 | +8740106.59 ± 2536.63 | ±0.35 |
| ${}^{128}$Nd | 128 | 68 | 6.9899 | -993321.65 ± 244.5885 | 120210.4441 | 119170.7149 | +8724703.77 ± 1680.54 | ±0.35 |
| ${}^{129}$Nd | 129 | 69 | 13.4035 | -987314.96 ± 244.1704 | 121143.5960 | 120100.3647 | +8686329.07 ± 1683.04 | ±0.35 |
| ${}^{130}$Nd | 130 | 70 | 19.8048 | -981472.29 ± 26.1477 | 122076.7601 | 121027.6372 | +8668457.18 ± 230.90 | ±0.35 |
| ${}^{131}$Nd | 131 | 71 | 26.1939 | -975705.22 ± 25.5276 | 123009.9364 | 121957.9595 | +8625733.62 ± 225.63 | ±0.36 |
| ${}^{132}$Nd | 132 | 72 | 32.5711 | -970115.45 ± 22.2120 | 123943.1246 | 122885.7959 | +8604157.40 ± 196.97 | ±0.36 |
| ${}^{133}$Nd | 133 | 73 | 38.9367 | -964566.84 ± 42.3856 | 124876.3245 | 123816.3834 | +8560588.24 ± 376.16 | ±0.36 |
| ${}^{134}$Nd | 134 | 74 | 45.2907 | -959207.19 ± 10.6451 | 125809.5359 | 124744.5635 | +8537225.10 ± 94.73 | ±0.36 |
| ${}^{135}$Nd | 135 | 75 | 51.6334 | -953853.41 ± 17.0967 | 126742.7586 | 125675.4904 | +8492253.95 ± 152.20 | ±0.36 |
| ${}^{136}$Nd | 136 | 76 | 57.9651 | -948701.56 ± 10.4592 | 127675.9924 | 126603.9988 | +8467296.19 ± 93.34 | ±0.37 |
| ${}^{137}$Nd | 137 | 77 | 64.2858 | -943530.41 ± 10.3014 | 128609.2371 | 127535.1082 | +8422220.94 ± 91.93 | ±0.37 |
| ${}^{138}$Nd | 138 | 78 | 70.5957 | -938554.64 ± 10.1015 | 129542.4926 | 128464.1691 | +8393962.76 ± 90.32 | ±0.37 |
| ${}^{139}$Nd | 139 | 79 | 76.8951 | -933538.66 ± 23.7876 | 130475.7586 | 129395.6635 | +8347228.37 ± 212.69 | ±0.37 |
| ${}^{140}$Nd | 140 | 80 | 83.1840 | -928738.15 ± 2.7945 | 131409.0351 | 130324.9173 | +8318576.73 ± 25.02 | ±0.37 |
| ${}^{141}$Nd | 141 | 81 | 89.4628 | -923881.34 ± 2.7113 | 132342.3218 | 131256.4771 | +8272694.11 ± 24.25 | ±0.38 |
| ${}^{142}$Nd | 142 | 82 | 95.7314 | -919223.29 ± 1.0544 | 133275.6185 | 132186.2127 | +8241448.60 ± 9.50 | ±0.38 |
| ${}^{143}$Nd | 143 | 83 | 101.9902 | -914384.62 ± 1.0564 | 134208.9252 | 133119.6545 | +8182643.66 ± 9.43 | ±0.38 |
| ${}^{144}$Nd | 144 | 84 | 108.2392 | -909731.25 ± 1.0448 | 135142.2416 | 134051.4029 | +8137465.98 ± 9.35 | ±0.38 |
| ${}^{145}$Nd | 145 | 85 | 114.4786 | -904983.80 ± 1.0591 | 136075.5677 | 134985.2130 | +8077585.65 ± 9.41 | ±0.38 |
| ${}^{146}$Nd | 146 | 86 | 120.7085 | -900438.15 ± 1.0477 | 137008.9031 | 135917.2132 | +8032020.87 ± 9.36 | ±0.39 |
| ${}^{147}$Nd | 147 | 87 | 126.9292 | -895762.28 ± 1.0503 | 137942.2479 | 136851.4865 | +7970402.52 ± 9.31 | ±0.39 |
| ${}^{148}$Nd | 148 | 88 | 133.1407 | -891315.70 ± 1.6793 | 138875.6018 | 137783.7193 | +7924612.06 ± 14.89 | ±0.39 |
| ${}^{149}$Nd | 149 | 89 | 139.3432 | -886718.49 ± 1.6716 | 139808.9647 | 138718.2459 | +7862836.08 ± 14.81 | ±0.39 |
| ${}^{150}$Nd | 150 | 90 | 145.5368 | -882388.52 ± 0.9091 | 140742.3366 | 139650.4356 | +7818815.30 ± 8.08 | ±0.39 |
| ${}^{151}$Nd | 151 | 91 | 151.7216 | -877916.69 ± 0.9113 | 141675.7171 | 140584.6665 | +7760808.38 ± 8.05 | ±0.39 |
| ${}^{152}$Nd | 152 | 92 | 157.8979 | -873686.66 ± 19.5768 | 142609.1063 | 141516.9541 | +7717465.52 ± 172.95 | ±0.40 |
| ${}^{153}$Nd | 153 | 93 | 164.0656 | -869301.78 ± 2.1939 | 143542.5040 | 142451.2675 | +7660419.68 ± 19.28 | ±0.40 |
| ${}^{154}$Nd | 154 | 94 | 170.2250 | -865074.43 ± 0.8178 | 144475.9100 | 143384.5124 | +7611684.28 ± 7.15 | ±0.40 |
| ${}^{155}$Nd | 155 | 95 | 176.3762 | -860726.02 ± 7.2335 | 145409.3243 | 144319.3023 | +7552849.65 ± 63.42 | ±0.40 |
| ${}^{156}$Nd | 156 | 96 | 182.5192 | -856553.67 ± 1.0299 | 146342.7467 | 145252.8780 | +7503249.61 ± 8.98 | ±0.40 |
| ${}^{157}$Nd | 157 | 97 | 188.6543 | -852238.69 ± 1.6724 | 147276.1770 | 146188.0802 | +7443129.84 ± 14.62 | ±0.40 |
| ${}^{158}$Nd | 158 | 98 | 194.7814 | -848083.66 ± 1.0228 | 148209.6153 | 147122.2333 | +7391010.87 ± 8.86 | ±0.41 |
| ${}^{159}$Nd | 159 | 99 | 200.9008 | -843793.42 ± 23.1801 | 149143.0613 | 148057.8385 | +7329722.25 ± 201.33 | ±0.41 |
| ${}^{160}$Nd | 160 | 100 | 207.0126 | -839673.61 ± 36.0720 | 150076.5150 | 148992.3321 | +7276769.95 ± 312.60 | ±0.41 |
| ${}^{161}$Nd | 161 | 101 | 213.1168 | -835400.82 ± 248.6944 | 151009.9762 | 149928.3205 | +7214485.94 ± 2665.35 | ±0.41 |
| ${}^{162}$Nd | 162 | 102 | 219.2135 | -831317.66 ± 249.3144 | 151943.4449 | 150863.0348 | +7161530.08 ± 2648.83 | ±0.41 |
| ${}^{163}$Nd | 163 | 103 | 225.3029 | -827048.75 ± 375.3754 | 152876.9209 | 151799.4593 | +7097928.30 ± 3295.22 | ±0.41 |

### Promethium (Z = 61)

_40 of 40 isotopes with a framework prediction; 40 of 40 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{126}$Pm | 126 | 65 | -25.3736 | -1025147.05 ± 499.5005 | 118362.8944 | 117328.5074 | +8816161.14 ± 4263.35 | ±0.34 |
| ${}^{127}$Pm | 127 | 66 | -18.8918 | -1018474.19 ± 372.5782 | 119295.9781 | 118254.4414 | +8807590.00 ± 3379.25 | ±0.34 |
| ${}^{128}$Pm | 128 | 67 | -12.4232 | -1012019.34 ± 247.6780 | 120229.0749 | 119183.0256 | +8776831.65 ± 2516.64 | ±0.34 |
| ${}^{129}$Pm | 129 | 68 | -5.9676 | -1005701.28 ± 246.4876 | 121162.1847 | 120109.5595 | +8763875.75 ± 2497.23 | ±0.35 |
| ${}^{130}$Pm | 130 | 69 | 0.4753 | -999550.34 ± 245.9722 | 122095.3073 | 121038.7639 | +8728966.47 ± 1654.60 | ±0.35 |
| ${}^{131}$Pm | 131 | 70 | 6.9057 | -993542.21 ± 245.0080 | 123028.4423 | 121965.9573 | +8711324.14 ± 1642.03 | ±0.35 |
| ${}^{132}$Pm | 132 | 71 | 13.3237 | -987655.97 ± 122.2942 | 123961.5897 | 122895.5940 | +8673994.15 ± 1212.73 | ±0.35 |
| ${}^{133}$Pm | 133 | 72 | 19.7296 | -981918.81 ± 46.0979 | 124894.7492 | 123823.3081 | +8652983.47 ± 406.23 | ±0.35 |
| ${}^{134}$Pm | 134 | 73 | 26.1237 | -976264.07 ± 38.0840 | 125827.9205 | 124753.4460 | +8612784.60 ± 336.00 | ±0.36 |
| ${}^{135}$Pm | 135 | 74 | 32.5061 | -970767.06 ± 74.5557 | 126761.1036 | 125681.6417 | +8588859.26 ± 659.63 | ±0.36 |
| ${}^{136}$Pm | 136 | 75 | 38.8769 | -965323.93 ± 61.6105 | 127694.2982 | 126612.0282 | +8547923.84 ± 545.54 | ±0.36 |
| ${}^{137}$Pm | 137 | 76 | 45.2365 | -960042.66 ± 11.5203 | 128627.5040 | 127540.6194 | +8521870.65 ± 102.25 | ±0.36 |
| ${}^{138}$Pm | 138 | 77 | 51.5850 | -954791.00 ± 10.1713 | 129560.7210 | 128471.2719 | +8480098.50 ± 90.31 | ±0.37 |
| ${}^{139}$Pm | 139 | 78 | 57.9225 | -949706.58 ± 11.8037 | 130493.9489 | 129400.1794 | +8452611.92 ± 105.01 | ±0.37 |
| ${}^{140}$Pm | 140 | 79 | 64.2492 | -944635.32 ± 20.8708 | 131427.1875 | 130330.9625 | +8411087.08 ± 185.83 | ±0.37 |
| ${}^{141}$Pm | 141 | 80 | 70.5654 | -939731.75 ± 11.9341 | 132360.4368 | 131260.1457 | +8382522.30 ± 106.45 | ±0.37 |
| ${}^{142}$Pm | 142 | 81 | 76.8712 | -934829.82 ± 20.0080 | 133293.6964 | 132191.0212 | +8341529.13 ± 178.49 | ±0.37 |
| ${}^{143}$Pm | 143 | 82 | 83.1667 | -930078.87 ± 2.4766 | 134226.9663 | 133120.6962 | +8310279.39 ± 22.11 | ±0.38 |
| ${}^{144}$Pm | 144 | 83 | 89.4522 | -925204.90 ± 2.4322 | 135160.2463 | 134053.7348 | +8254238.58 ± 21.72 | ±0.38 |
| ${}^{145}$Pm | 145 | 84 | 95.7277 | -920484.41 ± 2.3246 | 136093.5362 | 134985.3775 | +8209472.20 ± 20.78 | ±0.38 |
| ${}^{146}$Pm | 146 | 85 | 101.9934 | -915717.93 ± 3.5350 | 137026.8359 | 135918.6848 | +8153044.85 ± 31.45 | ±0.38 |
| ${}^{147}$Pm | 147 | 86 | 108.2495 | -911110.77 ± 1.0622 | 137960.1452 | 136850.5913 | +8107776.07 ± 9.41 | ±0.38 |
| ${}^{148}$Pm | 148 | 87 | 114.4962 | -906434.26 ± 4.6443 | 138893.4640 | 137784.2615 | +8050284.50 ± 41.29 | ±0.39 |
| ${}^{149}$Pm | 149 | 88 | 120.7335 | -901919.82 ± 1.7793 | 139826.7921 | 138716.5570 | +8003622.94 ± 15.74 | ±0.39 |
| ${}^{150}$Pm | 150 | 89 | 126.9617 | -897327.70 ± 16.1940 | 140760.1293 | 139650.5182 | +7945628.37 ± 143.44 | ±0.39 |
| ${}^{151}$Pm | 151 | 90 | 133.1808 | -892978.67 ± 3.7009 | 141693.4757 | 140582.2234 | +7904642.77 ± 32.79 | ±0.39 |
| ${}^{152}$Pm | 152 | 91 | 139.3910 | -888520.36 ± 20.7145 | 142626.8309 | 141515.8493 | +7850580.64 ± 183.05 | ±0.39 |
| ${}^{153}$Pm | 153 | 92 | 145.5924 | -884251.73 ± 7.2009 | 143560.1949 | 142447.9499 | +7808080.20 ± 63.62 | ±0.39 |
| ${}^{154}$Pm | 154 | 93 | 151.7852 | -879871.78 ± 19.8057 | 144493.5675 | 143381.8254 | +7753717.42 ± 174.51 | ±0.40 |
| ${}^{155}$Pm | 155 | 94 | 157.9694 | -875641.16 ± 3.7094 | 145426.9487 | 144314.6461 | +7707482.57 ± 32.69 | ±0.40 |
| ${}^{156}$Pm | 156 | 95 | 164.1453 | -871316.04 ± 0.9295 | 146360.3382 | 145248.9133 | +7651863.87 ± 8.18 | ±0.40 |
| ${}^{157}$Pm | 157 | 96 | 170.3129 | -867126.87 ± 5.4629 | 147293.7361 | 146182.2772 | +7603239.76 ± 47.92 | ±0.40 |
| ${}^{158}$Pm | 158 | 97 | 176.4724 | -862843.68 ± 0.6877 | 148227.1420 | 147116.9622 | +7546239.30 ± 6.03 | ±0.40 |
| ${}^{159}$Pm | 159 | 98 | 182.6238 | -858669.02 ± 7.7644 | 149160.5561 | 148051.0081 | +7494362.46 ± 67.81 | ±0.40 |
| ${}^{160}$Pm | 160 | 99 | 188.7673 | -854411.67 ± 1.5795 | 150093.9780 | 148986.1620 | +7435697.49 ± 13.75 | ±0.41 |
| ${}^{161}$Pm | 161 | 100 | 194.9029 | -850287.21 ± 6.9379 | 151027.4077 | 149920.4641 | +7383539.13 ± 60.27 | ±0.41 |
| ${}^{162}$Pm | 162 | 101 | 201.0309 | -846057.35 ± 248.1082 | 151960.8452 | 150856.0048 | +7323807.77 ± 1988.26 | ±0.41 |
| ${}^{163}$Pm | 163 | 102 | 207.1513 | -841971.26 ± 248.6944 | 152894.2902 | 151790.5793 | +7271273.70 ± 2632.65 | ±0.41 |
| ${}^{164}$Pm | 164 | 103 | 213.2643 | -837734.99 ± 249.5633 | 153827.7427 | 152726.6732 | +7209412.13 ± 2616.51 | ±0.41 |
| ${}^{165}$Pm | 165 | 104 | 219.3698 | -833644.41 ± 375.3754 | 154761.2026 | 153661.8569 | +7154317.17 ± 3255.28 | ±0.41 |

### Samarium (Z = 62)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{128}$Sm | 128 | 66 | -32.1173 | -1031372.38 ± 500.1250 | 120247.9867 | 119192.0955 | +8858734.71 ± 4196.69 | ±0.34 |
| ${}^{129}$Sm | 129 | 67 | -25.6189 | -1024753.36 ± 498.5666 | 121181.0537 | 120120.4095 | +8829841.90 ± 4164.26 | ±0.34 |
| ${}^{130}$Sm | 130 | 68 | -19.1337 | -1018249.53 ± 371.9777 | 122114.1339 | 121046.5335 | +8819752.03 ± 3301.30 | ±0.34 |
| ${}^{131}$Sm | 131 | 69 | -12.6615 | -1011954.53 ± 371.0575 | 123047.2271 | 121975.4474 | +8786847.99 ± 3276.16 | ±0.35 |
| ${}^{132}$Sm | 132 | 70 | -6.2019 | -1005784.82 ± 246.2448 | 123980.3330 | 122902.0819 | +8773253.38 ± 2440.49 | ±0.35 |
| ${}^{133}$Sm | 133 | 71 | 0.2451 | -999773.52 ± 245.7908 | 124913.4514 | 123831.4848 | +8737411.16 ± 2407.13 | ±0.35 |
| ${}^{134}$Sm | 134 | 72 | 6.6798 | -993896.22 ± 122.4440 | 125846.5821 | 124758.8338 | +8718808.05 ± 1567.94 | ±0.35 |
| ${}^{135}$Sm | 135 | 73 | 13.1025 | -988131.57 ± 140.0651 | 126779.7248 | 125688.8468 | +8679195.39 ± 1230.24 | ±0.35 |
| ${}^{136}$Sm | 136 | 74 | 19.5133 | -982515.05 ± 11.1992 | 127712.8795 | 126616.3872 | +8659955.48 ± 98.70 | ±0.36 |
| ${}^{137}$Sm | 137 | 75 | 25.9124 | -976972.03 ± 25.4336 | 128646.0458 | 127546.7006 | +8619158.70 ± 224.34 | ±0.36 |
| ${}^{138}$Sm | 138 | 76 | 32.3000 | -971587.77 ± 10.3910 | 129579.2236 | 128474.6885 | +8597297.21 ± 91.98 | ±0.36 |
| ${}^{139}$Sm | 139 | 77 | 38.6763 | -966244.80 ± 9.4989 | 130512.4127 | 129405.3002 | +8555387.97 ± 84.10 | ±0.36 |
| ${}^{140}$Sm | 140 | 78 | 45.0415 | -961068.26 ± 10.8061 | 131445.6130 | 130333.7186 | +8531133.80 ± 95.88 | ±0.37 |
| ${}^{141}$Sm | 141 | 79 | 51.3957 | -955901.81 ± 7.3193 | 132378.8241 | 131264.7347 | +8487347.90 ± 65.02 | ±0.37 |
| ${}^{142}$Sm | 142 | 80 | 57.7392 | -950927.19 ± 1.5810 | 133312.0461 | 132193.1808 | +8463865.21 ± 14.11 | ±0.37 |
| ${}^{143}$Sm | 143 | 81 | 64.0721 | -945940.27 ± 2.3166 | 134245.2786 | 133124.1397 | +8421754.96 ± 20.65 | ±0.37 |
| ${}^{144}$Sm | 144 | 82 | 70.3946 | -941128.32 ± 1.2163 | 135178.5215 | 134053.1853 | +8394699.51 ± 10.88 | ±0.37 |
| ${}^{145}$Sm | 145 | 83 | 76.7069 | -936209.83 ± 1.2300 | 136111.7747 | 134985.9936 | +8339984.41 ± 11.00 | ±0.38 |
| ${}^{146}$Sm | 146 | 84 | 83.0090 | -931448.71 ± 2.5199 | 137045.0380 | 135917.1428 | +8298403.00 ± 22.40 | ±0.38 |
| ${}^{147}$Sm | 147 | 85 | 89.3012 | -926636.61 ± 1.0386 | 137978.3112 | 136850.3672 | +8242170.38 ± 9.22 | ±0.38 |
| ${}^{148}$Sm | 148 | 86 | 95.5836 | -921997.15 ± 1.0145 | 138911.5943 | 137781.7913 | +8199944.04 ± 9.04 | ±0.38 |
| ${}^{149}$Sm | 149 | 87 | 101.8563 | -917274.49 ± 0.9439 | 139844.8869 | 138715.4856 | +8141854.96 ± 8.33 | ±0.38 |
| ${}^{150}$Sm | 150 | 88 | 108.1196 | -912753.54 ± 0.8957 | 140778.1891 | 139647.0642 | +8099882.74 ± 7.96 | ±0.38 |
| ${}^{151}$Sm | 151 | 89 | 114.3735 | -908121.89 ± 0.8976 | 141711.5006 | 140581.0332 | +8041393.32 ± 7.89 | ±0.39 |
| ${}^{152}$Sm | 152 | 90 | 120.6183 | -903743.93 ± 0.8127 | 142644.8213 | 141512.3408 | +8002697.64 ± 7.17 | ±0.39 |
| ${}^{153}$Sm | 153 | 91 | 126.8539 | -899239.62 ± 0.8142 | 143578.1510 | 142446.0378 | +7947663.84 ± 7.19 | ±0.39 |
| ${}^{154}$Sm | 154 | 92 | 133.0806 | -894958.43 ± 1.0332 | 144511.4897 | 143377.6364 | +7908160.28 ± 9.10 | ±0.39 |
| ${}^{155}$Sm | 155 | 93 | 139.2986 | -890552.23 ± 1.0473 | 145444.8372 | 144311.3949 | +7854143.30 ± 9.22 | ±0.39 |
| ${}^{156}$Sm | 156 | 94 | 145.5078 | -886320.34 ± 6.6545 | 146378.1934 | 145243.7194 | +7810829.87 ± 58.67 | ±0.39 |
| ${}^{157}$Sm | 157 | 95 | 151.7085 | -881972.82 ± 3.4445 | 147311.5582 | 146177.8966 | +7755355.31 ± 30.33 | ±0.40 |
| ${}^{158}$Sm | 158 | 96 | 157.9008 | -877787.17 ± 3.7054 | 148244.9313 | 147110.8165 | +7709254.82 ± 32.50 | ±0.40 |
| ${}^{159}$Sm | 159 | 97 | 164.0847 | -873493.12 ± 4.5725 | 149178.3128 | 148045.3546 | +7652777.26 ± 40.08 | ±0.40 |
| ${}^{160}$Sm | 160 | 98 | 170.2605 | -869345.82 ± 1.4979 | 150111.7024 | 148978.8234 | +7604295.42 ± 13.13 | ±0.40 |
| ${}^{161}$Sm | 161 | 99 | 176.4282 | -865079.81 ± 5.2081 | 151045.1001 | 149913.8787 | +7545808.77 ± 45.47 | ±0.40 |
| ${}^{162}$Sm | 162 | 100 | 182.5880 | -860983.54 ± 2.6888 | 151978.5058 | 150847.6657 | +7496569.64 ± 23.35 | ±0.40 |
| ${}^{163}$Sm | 163 | 101 | 188.7399 | -856767.72 ± 5.5788 | 152911.9193 | 151782.9393 | +7438121.81 ± 48.48 | ±0.41 |
| ${}^{164}$Sm | 164 | 102 | 194.8841 | -852708.24 ± 3.0987 | 153845.3405 | 152717.1077 | +7387730.47 ± 26.84 | ±0.41 |
| ${}^{165}$Sm | 165 | 103 | 201.0206 | -848488.14 ± 248.7253 | 154778.7694 | 153653.0170 | +7326588.11 ± 2600.74 | ±0.41 |
| ${}^{166}$Sm | 166 | 104 | 207.1497 | -844460.98 ± 249.2833 | 155712.2058 | 154587.5711 | +7275065.43 ± 2585.01 | ±0.41 |
| ${}^{167}$Sm | 167 | 105 | 213.2713 | -840206.01 ± 375.3754 | 156645.6496 | 155524.1856 | +7210865.43 ± 3216.30 | ±0.41 |
| ${}^{168}$Sm | 168 | 106 | 219.3856 | -836172.81 ± 250.9095 | 157579.1007 | 156459.3694 | +7156690.90 ± 1917.05 | ±0.41 |

### Europium (Z = 63)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{130}$Eu | 130 | 67 | -39.0223 | -1037757.44 ± 503.1447 | 122133.2402 | 121060.7202 | +8859355.98 ± 4447.38 | ±0.34 |
| ${}^{131}$Eu | 131 | 68 | -32.5075 | -1031034.09 ± 375.1876 | 123066.2908 | 121986.2639 | +8853676.13 ± 3275.87 | ±0.34 |
| ${}^{132}$Eu | 132 | 69 | -26.0058 | -1024571.38 ± 374.1581 | 123999.3545 | 122915.0213 | +8821812.05 ± 3251.12 | ±0.34 |
| ${}^{133}$Eu | 133 | 70 | -19.5170 | -1018215.51 ± 248.2622 | 124932.4311 | 123841.4797 | +8809256.83 ± 2406.93 | ±0.34 |
| ${}^{134}$Eu | 134 | 71 | -13.0409 | -1012052.01 ± 247.6780 | 125865.5205 | 124770.4094 | +8777009.17 ± 2403.94 | ±0.35 |
| ${}^{135}$Eu | 135 | 72 | -6.5773 | -1006009.67 ± 123.3502 | 126798.6223 | 125697.5562 | +8759645.35 ± 1556.23 | ±0.35 |
| ${}^{136}$Eu | 136 | 73 | -0.1259 | -1000113.99 ± 123.1224 | 127731.7363 | 126626.9545 | +8724697.32 ± 1544.80 | ±0.35 |
| ${}^{137}$Eu | 137 | 74 | 6.3134 | -994346.05 ± 3.9261 | 128664.8625 | 127554.5463 | +8704638.25 ± 34.32 | ±0.35 |
| ${}^{138}$Eu | 138 | 75 | 12.7408 | -988687.98 ± 24.8112 | 129598.0005 | 128484.4366 | +8666916.33 ± 217.50 | ±0.36 |
| ${}^{139}$Eu | 139 | 76 | 19.1565 | -983166.86 ± 11.5546 | 130531.1502 | 129412.2824 | +8645762.22 ± 101.61 | ±0.36 |
| ${}^{140}$Eu | 140 | 77 | 25.5608 | -977728.37 ± 44.9027 | 131464.3114 | 130342.1886 | +8609052.77 ± 395.40 | ±0.36 |
| ${}^{141}$Eu | 141 | 78 | 31.9537 | -972422.63 ± 10.9033 | 132397.4838 | 131270.7430 | +8583335.62 ± 96.28 | ±0.36 |
| ${}^{142}$Eu | 142 | 79 | 38.3356 | -967182.62 ± 25.7342 | 133330.6674 | 132200.8538 | +8546189.92 ± 227.36 | ±0.36 |
| ${}^{143}$Eu | 143 | 80 | 44.7065 | -962085.91 ± 9.3138 | 134263.8619 | 133129.4155 | +8521380.47 ± 82.51 | ±0.37 |
| ${}^{144}$Eu | 144 | 81 | 51.0666 | -957036.38 ± 9.0742 | 135197.0672 | 134059.5318 | +8485300.75 ± 80.46 | ±0.37 |
| ${}^{145}$Eu | 145 | 82 | 57.4161 | -952115.09 ± 2.5516 | 136130.2831 | 134988.6535 | +8457226.16 ± 22.67 | ±0.37 |
| ${}^{146}$Eu | 146 | 83 | 63.7553 | -947145.55 ± 4.9867 | 137063.5094 | 135921.0215 | +8405527.29 ± 44.21 | ±0.37 |
| ${}^{147}$Eu | 147 | 84 | 70.0841 | -942305.29 ± 2.1177 | 137996.7460 | 136852.0886 | +8364193.41 ± 18.77 | ±0.37 |
| ${}^{148}$Eu | 148 | 85 | 76.4028 | -937454.94 ± 8.1538 | 138929.9927 | 137784.8299 | +8311240.02 ± 72.29 | ±0.38 |
| ${}^{149}$Eu | 149 | 86 | 82.7116 | -932742.74 ± 3.1744 | 139863.2493 | 138716.1801 | +8269180.74 ± 28.14 | ±0.38 |
| ${}^{150}$Eu | 150 | 87 | 89.0106 | -927996.73 ± 5.0356 | 140796.5157 | 139649.3232 | +8214809.31 ± 44.61 | ±0.38 |
| ${}^{151}$Eu | 151 | 88 | 95.2999 | -923400.61 ± 0.9345 | 141729.7918 | 140580.9566 | +8172054.83 ± 8.29 | ±0.38 |
| ${}^{152}$Eu | 152 | 89 | 101.5797 | -918764.87 ± 0.9360 | 142663.0775 | 141514.2153 | +8118351.86 ± 8.24 | ±0.38 |
| ${}^{153}$Eu | 153 | 90 | 107.8502 | -914336.04 ± 0.9357 | 143596.3724 | 142445.2304 | +8081295.73 ± 8.22 | ±0.39 |
| ${}^{154}$Eu | 154 | 91 | 114.1114 | -909824.26 ± 0.9371 | 144529.6766 | 143378.3536 | +8029964.13 ± 8.28 | ±0.39 |
| ${}^{155}$Eu | 155 | 92 | 120.3635 | -905492.34 ± 0.9858 | 145462.9899 | 144309.7677 | +7991296.92 ± 8.67 | ±0.39 |
| ${}^{156}$Eu | 156 | 93 | 126.6067 | -901082.39 ± 2.7545 | 146396.3122 | 145242.9973 | +7940588.43 ± 24.31 | ±0.39 |
| ${}^{157}$Eu | 157 | 94 | 132.8410 | -896811.95 ± 3.2928 | 147329.6433 | 146175.1151 | +7898253.67 ± 28.96 | ±0.39 |
| ${}^{158}$Eu | 158 | 95 | 139.0667 | -892467.38 ± 1.5760 | 148262.9831 | 147108.7979 | +7845792.84 ± 13.81 | ±0.39 |
| ${}^{159}$Eu | 159 | 96 | 145.2837 | -888251.48 ± 3.3265 | 149196.3314 | 148041.5191 | +7800597.75 ± 29.18 | ±0.40 |
| ${}^{160}$Eu | 160 | 97 | 151.4923 | -883968.75 ± 0.6985 | 150129.6883 | 148975.5631 | +7747076.75 ± 6.07 | ±0.40 |
| ${}^{161}$Eu | 161 | 98 | 157.6926 | -879806.20 ± 7.9274 | 151063.0534 | 149908.7591 | +7699979.19 ± 69.37 | ±0.40 |
| ${}^{162}$Eu | 162 | 99 | 163.8846 | -875561.09 ± 0.9964 | 151996.4268 | 150843.3219 | +7644388.38 ± 8.71 | ±0.40 |
| ${}^{163}$Eu | 163 | 100 | 170.0686 | -871443.66 ± 0.6900 | 152929.8083 | 151776.9651 | +7595639.95 ± 5.95 | ±0.40 |
| ${}^{164}$Eu | 164 | 101 | 176.2445 | -867249.80 ± 1.5564 | 153863.1977 | 152711.8009 | +7539671.84 ± 13.54 | ±0.40 |
| ${}^{165}$Eu | 165 | 102 | 182.4126 | -863177.75 ± 3.9109 | 154796.5951 | 153645.7980 | +7489935.11 ± 33.93 | ±0.40 |
| ${}^{166}$Eu | 166 | 103 | 188.5729 | -858989.38 ± 124.1311 | 155730.0002 | 154581.2723 | +7431222.65 ± 644.77 | ±0.41 |
| ${}^{167}$Eu | 167 | 104 | 194.7256 | -854936.37 ± 248.8181 | 156663.4129 | 155515.7453 | +7379751.80 ± 2569.59 | ±0.41 |
| ${}^{168}$Eu | 168 | 105 | 200.8707 | -850766.50 ± 249.6256 | 157596.8333 | 156451.7591 | +7319024.24 ± 2554.21 | ±0.41 |
| ${}^{169}$Eu | 169 | 106 | 207.0083 | -846714.89 ± 375.4224 | 158530.2611 | 157386.8431 | +7265015.92 ± 3178.23 | ±0.41 |
| ${}^{170}$Eu | 170 | 107 | 213.1386 | -842552.24 ± 376.7424 | 159463.6962 | 158323.1372 | +7203994.24 ± 3159.44 | ±0.41 |

### Gadolinium (Z = 64)

_40 of 40 isotopes with a framework prediction; 40 of 40 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{133}$Gd | 133 | 69 | -39.5566 | -1037335.90 ± 502.1341 | 124951.6884 | 123852.6558 | +8873710.35 ± 4038.77 | ±0.34 |
| ${}^{134}$Gd | 134 | 70 | -33.0384 | -1030788.65 ± 374.6254 | 125884.7357 | 124778.6802 | +8864138.68 ± 3202.56 | ±0.34 |
| ${}^{135}$Gd | 135 | 71 | -26.5332 | -1024482.10 ± 373.6921 | 126817.7959 | 125707.4543 | +8832742.49 ± 3178.90 | ±0.34 |
| ${}^{136}$Gd | 136 | 72 | -20.0406 | -1018273.52 ± 248.0159 | 127750.8687 | 126634.1084 | +8818796.00 ± 2353.85 | ±0.35 |
| ${}^{137}$Gd | 137 | 73 | -13.5605 | -1012250.25 ± 247.5248 | 128683.9541 | 127563.4787 | +8783669.11 ± 2336.70 | ±0.35 |
| ${}^{138}$Gd | 138 | 74 | -7.0927 | -1006335.83 ± 123.2742 | 129617.0516 | 128490.5267 | +8767376.87 ± 1558.65 | ±0.35 |
| ${}^{139}$Gd | 139 | 75 | -0.6369 | -1000563.85 ± 123.0618 | 130550.1612 | 129420.0489 | +8732127.45 ± 1511.46 | ±0.35 |
| ${}^{140}$Gd | 140 | 76 | 5.8071 | -994913.65 ± 24.4759 | 131483.2827 | 130347.3922 | +8714332.14 ± 214.39 | ±0.36 |
| ${}^{141}$Gd | 141 | 77 | 12.2394 | -989368.26 ± 17.1594 | 132416.4159 | 131277.4444 | +8676063.60 ± 150.52 | ±0.36 |
| ${}^{142}$Gd | 142 | 78 | 18.6602 | -983955.37 ± 24.0286 | 133349.5605 | 132205.2032 | +8655916.94 ± 211.37 | ±0.36 |
| ${}^{143}$Gd | 143 | 79 | 25.0697 | -978616.05 ± 170.8521 | 134282.7164 | 133135.4255 | +8617472.37 ± 1504.49 | ±0.36 |
| ${}^{144}$Gd | 144 | 80 | 31.4681 | -973421.31 ± 23.6076 | 135215.8834 | 134063.3914 | +8596619.52 ± 208.44 | ±0.36 |
| ${}^{145}$Gd | 145 | 81 | 37.8555 | -968273.86 ± 16.5270 | 136149.0614 | 134993.7184 | +8558494.07 ± 146.04 | ±0.37 |
| ${}^{146}$Gd | 146 | 82 | 44.2322 | -963275.31 ± 3.3820 | 137082.2501 | 135922.0533 | +8535750.69 ± 29.99 | ±0.37 |
| ${}^{147}$Gd | 147 | 83 | 50.5983 | -958244.29 ± 1.5528 | 138015.4494 | 136854.2763 | +8484741.01 ± 13.78 | ±0.37 |
| ${}^{148}$Gd | 148 | 84 | 56.9540 | -953345.24 ± 1.2002 | 138948.6592 | 137784.8579 | +8446510.46 ± 10.59 | ±0.37 |
| ${}^{149}$Gd | 149 | 85 | 63.2994 | -948439.98 ± 2.6943 | 139881.8792 | 138717.4943 | +8393930.01 ± 23.86 | ±0.37 |
| ${}^{150}$Gd | 150 | 86 | 69.6346 | -943679.14 ± 4.9014 | 140815.1094 | 139648.3515 | +8354970.64 ± 43.36 | ±0.38 |
| ${}^{151}$Gd | 151 | 87 | 75.9599 | -938884.33 ± 2.4055 | 141748.3495 | 140581.4207 | +8300732.54 ± 21.28 | ±0.38 |
| ${}^{152}$Gd | 152 | 88 | 82.2754 | -934257.39 ± 0.8016 | 142681.5995 | 141512.3965 | +8262194.93 ± 7.12 | ±0.38 |
| ${}^{153}$Gd | 153 | 89 | 88.5812 | -929570.27 ± 0.8029 | 143614.8591 | 142445.7149 | +8207647.13 ± 7.03 | ±0.38 |
| ${}^{154}$Gd | 154 | 90 | 94.8775 | -925093.93 ± 0.7903 | 144548.1282 | 143376.3856 | +8172493.80 ± 6.93 | ±0.38 |
| ${}^{155}$Gd | 155 | 91 | 101.1644 | -920534.15 ± 0.7671 | 145481.4068 | 144309.5158 | +8120677.22 ± 6.81 | ±0.38 |
| ${}^{156}$Gd | 156 | 92 | 107.4420 | -916165.14 ± 0.7669 | 146414.6946 | 145240.5448 | +8084173.18 ± 6.76 | ±0.39 |
| ${}^{157}$Gd | 157 | 93 | 113.7105 | -911712.06 ± 0.7558 | 147347.9915 | 146173.7504 | +8033187.06 ± 6.68 | ±0.39 |
| ${}^{158}$Gd | 158 | 94 | 119.9700 | -907422.52 ± 0.7559 | 148281.2974 | 147105.3784 | +7993718.18 ± 6.64 | ±0.39 |
| ${}^{159}$Gd | 159 | 95 | 126.2207 | -903043.71 ± 0.7572 | 149214.6121 | 148039.0006 | +7941228.04 ± 6.61 | ±0.39 |
| ${}^{160}$Gd | 160 | 96 | 132.4627 | -898828.06 ± 0.8554 | 150147.9356 | 148971.1145 | +7899659.18 ± 7.54 | ±0.39 |
| ${}^{161}$Gd | 161 | 97 | 138.6960 | -894521.17 ± 1.1387 | 151081.2676 | 149905.0446 | +7846454.33 ± 10.03 | ±0.39 |
| ${}^{162}$Gd | 162 | 98 | 144.9209 | -890357.97 ± 3.0028 | 152014.6082 | 150837.7641 | +7802052.25 ± 26.27 | ±0.40 |
| ${}^{163}$Gd | 163 | 99 | 151.1374 | -886101.09 ± 0.6019 | 152947.9571 | 151772.1503 | +7747184.20 ± 5.25 | ±0.40 |
| ${}^{164}$Gd | 164 | 100 | 157.3456 | -881989.56 ± 0.7503 | 153881.3143 | 152705.3393 | +7700942.04 ± 6.55 | ±0.40 |
| ${}^{165}$Gd | 165 | 101 | 163.5458 | -877788.86 ± 0.9741 | 154814.6796 | 153640.0013 | +7645653.79 ± 8.49 | ±0.40 |
| ${}^{166}$Gd | 166 | 102 | 169.7379 | -873720.05 ± 1.1732 | 155748.0529 | 154573.6503 | +7597689.64 ± 10.24 | ±0.40 |
| ${}^{167}$Gd | 167 | 103 | 175.9221 | -869553.60 ± 3.8635 | 156681.4341 | 155508.7396 | +7541020.27 ± 33.52 | ±0.40 |
| ${}^{168}$Gd | 168 | 104 | 182.0984 | -865518.70 ± 248.1390 | 157614.8232 | 156442.8596 | +7491320.62 ± 1917.26 | ±0.41 |
| ${}^{169}$Gd | 169 | 105 | 188.2671 | -861355.73 ± 248.9110 | 158548.2199 | 157378.6134 | +7431800.95 ± 2539.17 | ±0.41 |
| ${}^{170}$Gd | 170 | 106 | 194.4282 | -857341.22 ± 374.2048 | 159481.6242 | 158313.1479 | +7380791.63 ± 3159.64 | ±0.41 |
| ${}^{171}$Gd | 171 | 107 | 200.5818 | -853192.35 ± 375.4693 | 160415.0361 | 159249.2818 | +7320311.21 ± 3141.06 | ±0.41 |
| ${}^{172}$Gd | 172 | 108 | 206.7280 | -849233.92 ± 250.8781 | 161348.4553 | 160184.0156 | +7269387.47 ± 1872.48 | ±0.41 |

### Terbium (Z = 65)

_40 of 40 isotopes with a framework prediction; 40 of 40 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{135}$Tb | 135 | 70 | -46.7653 | -1043633.96 ± 377.8813 | 126837.2457 | 125718.6509 | +8897604.38 ± 3178.61 | ±0.34 |
| ${}^{136}$Tb | 136 | 71 | -40.2309 | -1037158.08 ± 502.4494 | 127770.2767 | 126647.2983 | +8866974.30 ± 3949.65 | ±0.34 |
| ${}^{137}$Tb | 137 | 72 | -33.7093 | -1030760.52 ± 375.0469 | 128703.3205 | 127573.7251 | +8854451.79 ± 3139.69 | ±0.34 |
| ${}^{138}$Tb | 138 | 73 | -27.2004 | -1024579.64 ± 249.4077 | 129636.3770 | 128502.5859 | +8823099.55 ± 2334.13 | ±0.35 |
| ${}^{139}$Tb | 139 | 74 | -20.7039 | -1018498.34 ± 248.3855 | 130569.4459 | 129429.5501 | +8807075.15 ± 2303.01 | ±0.35 |
| ${}^{140}$Tb | 140 | 75 | -14.2196 | -1012588.00 ± 708.6419 | 131502.5270 | 130358.6922 | +8774518.80 ± 6140.66 | ±0.35 |
| ${}^{141}$Tb | 141 | 76 | -7.7473 | -1006785.54 ± 92.1892 | 132435.6202 | 131286.1278 | +8755627.58 ± 801.75 | ±0.35 |
| ${}^{142}$Tb | 142 | 77 | -1.2870 | -1001117.31 ± 608.2100 | 133368.7252 | 132215.6032 | +8721527.68 ± 5298.60 | ±0.36 |
| ${}^{143}$Tb | 143 | 78 | 5.1618 | -995564.58 ± 44.0268 | 134301.8419 | 133143.2376 | +8701938.67 ± 384.79 | ±0.36 |
| ${}^{144}$Tb | 144 | 79 | 11.5991 | -990118.24 ± 23.8122 | 135234.9701 | 134072.7827 | +8668331.51 ± 208.43 | ±0.36 |
| ${}^{145}$Tb | 145 | 80 | 18.0251 | -984800.38 ± 93.5130 | 136168.1095 | 135000.2453 | +8650829.95 ± 821.45 | ±0.36 |
| ${}^{146}$Tb | 146 | 81 | 24.4399 | -979553.71 ± 37.5344 | 137101.2601 | 135930.3755 | +8613855.12 ± 330.02 | ±0.36 |
| ${}^{147}$Tb | 147 | 82 | 30.8439 | -974432.58 ± 6.7141 | 138034.4215 | 136858.8906 | +8589365.06 ± 59.15 | ±0.37 |
| ${}^{148}$Tb | 148 | 83 | 37.2370 | -969333.04 ± 10.2629 | 138967.5938 | 137790.5904 | +8541972.25 ± 90.44 | ±0.37 |
| ${}^{149}$Tb | 149 | 84 | 43.6196 | -964341.59 ± 2.9721 | 139900.7767 | 138721.1328 | +8503706.88 ± 26.15 | ±0.37 |
| ${}^{150}$Tb | 150 | 85 | 49.9917 | -959387.73 ± 5.9832 | 140833.9700 | 139653.0098 | +8456389.20 ± 52.77 | ±0.37 |
| ${}^{151}$Tb | 151 | 86 | 56.3535 | -954536.73 ± 3.3013 | 141767.1736 | 140583.9861 | +8416232.00 ± 29.12 | ±0.37 |
| ${}^{152}$Tb | 152 | 87 | 62.7052 | -949703.23 ± 32.0897 | 142700.3873 | 141516.3865 | +8366528.12 ± 282.74 | ±0.38 |
| ${}^{153}$Tb | 153 | 88 | 69.0470 | -944998.84 ± 3.1444 | 143633.6110 | 142447.2843 | +8328180.76 ± 27.71 | ±0.38 |
| ${}^{154}$Tb | 154 | 89 | 75.3788 | -940283.92 ± 35.8926 | 144566.8445 | 143379.9353 | +8278070.84 ± 316.01 | ±0.38 |
| ${}^{155}$Tb | 155 | 90 | 81.7010 | -935741.95 ± 7.7290 | 145500.0877 | 144310.3356 | +8244399.87 ± 68.11 | ±0.38 |
| ${}^{156}$Tb | 156 | 91 | 88.0137 | -931151.30 ± 2.9531 | 146433.3405 | 145242.9892 | +8195585.58 ± 25.94 | ±0.38 |
| ${}^{157}$Tb | 157 | 92 | 94.3169 | -926721.82 ± 0.7929 | 147366.6027 | 146173.8104 | +8160095.53 ± 6.96 | ±0.38 |
| ${}^{158}$Tb | 158 | 93 | 100.6109 | -922241.31 ± 0.9769 | 148299.8741 | 147106.5975 | +8111645.93 ± 8.61 | ±0.39 |
| ${}^{159}$Tb | 159 | 94 | 106.8958 | -917900.03 ± 0.8426 | 149233.1547 | 148038.0299 | +8073093.18 ± 7.45 | ±0.39 |
| ${}^{160}$Tb | 160 | 95 | 113.1716 | -913503.48 ± 0.8438 | 150166.4443 | 148971.2201 | +8023188.54 ± 7.45 | ±0.39 |
| ${}^{161}$Tb | 161 | 96 | 119.4386 | -909247.52 ± 0.9297 | 151099.7428 | 149903.0889 | +7982849.87 ± 8.13 | ±0.39 |
| ${}^{162}$Tb | 162 | 97 | 125.6968 | -904960.98 ± 1.5556 | 152033.0500 | 150836.1653 | +7934998.47 ± 13.59 | ±0.39 |
| ${}^{163}$Tb | 163 | 98 | 131.9463 | -900745.07 ± 3.0531 | 152966.3658 | 151768.9432 | +7889774.22 ± 26.75 | ±0.39 |
| ${}^{164}$Tb | 164 | 99 | 138.1874 | -896484.86 ± 1.4005 | 153899.6902 | 152702.9280 | +7837192.10 ± 12.20 | ±0.40 |
| ${}^{165}$Tb | 165 | 100 | 144.4201 | -892344.65 ± 1.1439 | 154833.0230 | 153635.9383 | +7791697.12 ± 10.03 | ±0.40 |
| ${}^{166}$Tb | 166 | 101 | 150.6445 | -888145.97 ± 1.0846 | 155766.3640 | 154570.2124 | +7738564.47 ± 9.46 | ±0.40 |
| ${}^{167}$Tb | 167 | 102 | 156.8607 | -884059.45 ± 1.4318 | 156699.7132 | 155503.6322 | +7691659.23 ± 12.41 | ±0.40 |
| ${}^{168}$Tb | 168 | 103 | 163.0689 | -879911.89 ± 3.0930 | 157633.0704 | 156438.2282 | +7637789.07 ± 26.79 | ±0.40 |
| ${}^{169}$Tb | 169 | 104 | 169.2691 | -875871.58 ± 247.8622 | 158566.4356 | 157372.0231 | +7589738.83 ± 1905.94 | ±0.40 |
| ${}^{170}$Tb | 170 | 105 | 175.4615 | -871737.74 ± 248.5398 | 159499.8086 | 158307.2879 | +7532949.39 ± 1894.68 | ±0.40 |
| ${}^{171}$Tb | 171 | 106 | 181.6462 | -867713.80 ± 249.0660 | 160433.1894 | 159241.7218 | +7482132.41 ± 2509.46 | ±0.41 |
| ${}^{172}$Tb | 172 | 107 | 187.8232 | -863602.89 ± 374.7190 | 161366.5778 | 160177.2958 | +7424785.01 ± 3122.87 | ±0.41 |
| ${}^{173}$Tb | 173 | 108 | 193.9927 | -859621.30 ± 375.5633 | 162299.9737 | 161111.9700 | +7373776.60 ± 3104.75 | ±0.41 |
| ${}^{174}$Tb | 174 | 109 | 200.1548 | -855542.53 ± 376.7424 | 163233.3770 | 162048.0042 | +7314948.54 ± 3086.82 | ±0.41 |

### Dysprosium (Z = 66)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{138}$Dy | 138 | 72 | -47.5823 | -1043370.98 ± 503.1447 | 129655.9766 | 128511.2553 | +8907556.67 ± 3914.11 | ±0.34 |
| ${}^{139}$Dy | 139 | 73 | -41.0445 | -1037044.76 ± 501.8191 | 130589.0041 | 129439.9801 | +8876887.10 ± 3864.43 | ±0.34 |
| ${}^{140}$Dy | 140 | 74 | -34.5192 | -1030789.94 ± 374.6254 | 131522.0443 | 130366.3444 | +8865017.41 ± 3072.44 | ±0.35 |
| ${}^{141}$Dy | 141 | 75 | -28.0064 | -1024744.85 ± 249.1591 | 132455.0969 | 131295.2862 | +8833605.07 ± 2270.29 | ±0.35 |
| ${}^{142}$Dy | 142 | 76 | -21.5058 | -1018787.90 ± 620.2704 | 133388.1618 | 132222.0428 | +8819399.36 ± 5509.13 | ±0.35 |
| ${}^{143}$Dy | 143 | 77 | -15.0172 | -1013004.92 ± 11.2940 | 134321.2386 | 133151.4879 | +8785111.82 ± 97.94 | ±0.35 |
| ${}^{144}$Dy | 144 | 78 | -8.5404 | -1007317.01 ± 6.1439 | 135254.3273 | 134078.5808 | +8769084.56 ± 53.49 | ±0.35 |
| ${}^{145}$Dy | 145 | 79 | -2.0753 | -1001763.32 ± 5.5440 | 136187.4276 | 135008.4024 | +8732975.97 ± 48.30 | ±0.36 |
| ${}^{146}$Dy | 146 | 80 | 4.3783 | -996318.67 ± 5.6346 | 137120.5393 | 135935.5842 | +8717034.07 ± 49.25 | ±0.36 |
| ${}^{147}$Dy | 147 | 81 | 10.8207 | -990975.57 ± 7.3804 | 138053.6624 | 136865.4372 | +8681703.80 ± 64.66 | ±0.36 |
| ${}^{148}$Dy | 148 | 82 | 17.2520 | -985751.37 ± 7.1997 | 138986.7965 | 137793.2680 | +8661733.70 ± 63.31 | ±0.36 |
| ${}^{149}$Dy | 149 | 83 | 23.6723 | -980575.56 ± 7.5314 | 139919.9416 | 138724.9275 | +8614271.44 ± 66.19 | ±0.36 |
| ${}^{150}$Dy | 150 | 84 | 30.0818 | -975510.82 ± 3.5168 | 140853.0975 | 139654.8059 | +8580381.94 ± 30.92 | ±0.37 |
| ${}^{151}$Dy | 151 | 85 | 36.4808 | -970482.10 ± 2.6269 | 141786.2640 | 140586.8573 | +8531428.50 ± 23.10 | ±0.37 |
| ${}^{152}$Dy | 152 | 86 | 42.8693 | -965575.79 ± 3.6861 | 142719.4409 | 141516.9858 | +8496896.07 ± 32.45 | ±0.37 |
| ${}^{153}$Dy | 153 | 87 | 49.2475 | -960678.15 ± 3.2007 | 143652.6281 | 142449.4547 | +8446318.56 ± 28.09 | ±0.37 |
| ${}^{154}$Dy | 154 | 88 | 55.6155 | -955921.64 ± 5.8952 | 144585.8255 | 143379.6980 | +8412122.27 ± 51.82 | ±0.37 |
| ${}^{155}$Dy | 155 | 89 | 61.9736 | -951147.09 ± 7.5999 | 145519.0329 | 144312.4301 | +8361045.02 ± 66.83 | ±0.38 |
| ${}^{156}$Dy | 156 | 90 | 68.3218 | -946540.89 ± 0.7690 | 146452.2501 | 145242.5508 | +8328821.42 ± 6.80 | ±0.38 |
| ${}^{157}$Dy | 157 | 91 | 74.6603 | -941897.97 ± 4.0075 | 147385.4770 | 146175.1496 | +8279980.23 ± 35.25 | ±0.38 |
| ${}^{158}$Dy | 158 | 92 | 80.9893 | -937413.63 ± 1.8071 | 148318.7134 | 147105.6612 | +8246128.53 ± 15.89 | ±0.38 |
| ${}^{159}$Dy | 159 | 93 | 87.3088 | -932884.37 ± 1.1123 | 149251.9593 | 148038.3953 | +8197630.34 ± 9.72 | ±0.38 |
| ${}^{160}$Dy | 160 | 94 | 93.6191 | -928504.95 ± 0.5376 | 150185.2145 | 148969.3842 | +8161612.03 ± 4.70 | ±0.38 |
| ${}^{161}$Dy | 161 | 95 | 99.9202 | -924067.21 ± 0.5261 | 151118.4788 | 149902.4952 | +8111830.39 ± 4.65 | ±0.39 |
| ${}^{162}$Dy | 162 | 96 | 106.2122 | -919785.32 ± 0.5261 | 152051.7522 | 150833.8636 | +8074370.83 ± 4.61 | ±0.39 |
| ${}^{163}$Dy | 163 | 97 | 112.4954 | -915440.57 ± 0.5268 | 152985.0344 | 151767.1580 | +8024637.30 ± 4.57 | ±0.39 |
| ${}^{164}$Dy | 164 | 98 | 118.7698 | -911235.27 ± 0.5148 | 153918.3255 | 152699.0654 | +7984725.53 ± 4.55 | ±0.39 |
| ${}^{165}$Dy | 165 | 99 | 125.0355 | -906949.97 ± 0.5157 | 154851.6252 | 153632.9148 | +7932612.35 ± 4.54 | ±0.39 |
| ${}^{166}$Dy | 166 | 100 | 131.2927 | -902802.91 ± 0.5899 | 155784.9334 | 154565.4367 | +7889840.67 ± 5.19 | ±0.39 |
| ${}^{167}$Dy | 167 | 101 | 137.5415 | -898582.20 ± 2.9553 | 156718.2501 | 155499.6039 | +7836973.00 ± 25.76 | ±0.40 |
| ${}^{168}$Dy | 168 | 102 | 143.7819 | -894503.33 ± 102.7300 | 157651.5750 | 156432.4510 | +7793293.47 ± 895.00 | ±0.40 |
| ${}^{169}$Dy | 169 | 103 | 150.0142 | -890341.61 ± 219.7842 | 158584.9082 | 157366.9075 | +7739877.95 ± 1910.62 | ±0.40 |
| ${}^{170}$Dy | 170 | 104 | 156.2384 | -886312.55 ± 123.7011 | 159518.2494 | 158300.2877 | +7693995.66 ± 1265.13 | ±0.40 |
| ${}^{171}$Dy | 171 | 105 | 162.4546 | -882159.89 ± 124.0387 | 160451.5986 | 159235.4817 | +7637223.32 ± 1257.70 | ±0.40 |
| ${}^{172}$Dy | 172 | 106 | 168.6630 | -878171.38 ± 248.4781 | 161384.9557 | 160169.2263 | +7590280.88 ± 1872.65 | ±0.40 |
| ${}^{173}$Dy | 173 | 107 | 174.8635 | -874062.81 ± 249.1901 | 162318.3205 | 161104.7398 | +7532868.10 ± 2480.44 | ±0.41 |
| ${}^{174}$Dy | 174 | 108 | 181.0565 | -870109.30 ± 374.4851 | 163251.6930 | 162038.8439 | +7484928.16 ± 3086.99 | ±0.41 |
| ${}^{175}$Dy | 175 | 109 | 187.2418 | -866021.38 ± 375.6574 | 164185.0731 | 162974.7384 | +7426517.13 ± 3069.26 | ±0.41 |
| ${}^{176}$Dy | 176 | 110 | 193.4197 | -862093.65 ± 376.4588 | 165118.4606 | 163909.3521 | +7376690.35 ± 3051.76 | ±0.41 |

### Holmium (Z = 67)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{140}$Ho | 140 | 73 | -55.0918 | -1049773.97 ± 505.9449 | 131541.8346 | 130379.8567 | +8912250.36 ± 3836.58 | ±0.34 |
| ${}^{141}$Ho | 141 | 74 | -48.5378 | -1043338.74 ± 377.6910 | 132474.8460 | 131306.3039 | +8899359.87 ± 3050.44 | ±0.34 |
| ${}^{142}$Ho | 142 | 75 | -41.9964 | -1037131.07 ± 376.6478 | 133407.8700 | 132234.9123 | +8870257.37 ± 3029.02 | ±0.35 |
| ${}^{143}$Ho | 143 | 76 | -35.4673 | -1031006.77 ± 250.0313 | 134340.9064 | 133161.6092 | +8856134.91 ± 2238.47 | ±0.35 |
| ${}^{144}$Ho | 144 | 77 | -28.9505 | -1025077.02 ± 7.3468 | 135273.9549 | 134090.5414 | +8825480.98 ± 63.22 | ±0.35 |
| ${}^{145}$Ho | 145 | 78 | -22.4456 | -1019232.88 ± 6.3862 | 136207.0155 | 135017.5249 | +8809897.74 ± 55.19 | ±0.35 |
| ${}^{146}$Ho | 146 | 79 | -15.9526 | -1013550.91 ± 5.5933 | 137140.0879 | 135946.9009 | +8776860.54 ± 48.45 | ±0.35 |
| ${}^{147}$Ho | 147 | 80 | -9.4712 | -1007960.16 ± 4.2006 | 138073.1719 | 136873.8761 | +8762050.27 ± 36.53 | ±0.36 |
| ${}^{148}$Ho | 148 | 81 | -3.0012 | -1002500.76 ± 69.8485 | 139006.2674 | 137803.1362 | +8730797.09 ± 608.36 | ±0.36 |
| ${}^{149}$Ho | 149 | 82 | 3.4574 | -997146.99 ± 9.8853 | 139939.3742 | 138730.9756 | +8710373.08 ± 86.39 | ±0.36 |
| ${}^{150}$Ho | 150 | 83 | 9.9050 | -991882.65 ± 11.6167 | 140872.4920 | 139662.1697 | +8666071.48 ± 101.44 | ±0.36 |
| ${}^{151}$Ho | 151 | 84 | 16.3416 | -986713.85 ± 6.7522 | 141805.6208 | 140591.9869 | +8632311.96 ± 59.02 | ±0.36 |
| ${}^{152}$Ho | 152 | 85 | 22.7675 | -981609.87 ± 10.1167 | 142738.7604 | 141523.4991 | +8586992.62 ± 88.52 | ±0.37 |
| ${}^{153}$Ho | 153 | 86 | 29.1827 | -976607.15 ± 4.0595 | 143671.9105 | 142453.5858 | +8552433.04 ± 35.56 | ±0.37 |
| ${}^{154}$Ho | 154 | 87 | 35.5875 | -971648.04 ± 6.5516 | 144605.0712 | 143385.4526 | +8505873.96 ± 57.30 | ±0.37 |
| ${}^{155}$Ho | 155 | 88 | 41.9820 | -966804.16 ± 13.8126 | 145538.2421 | 144315.5463 | +8472377.84 ± 121.05 | ±0.37 |
| ${}^{156}$Ho | 156 | 89 | 48.3664 | -961983.51 ± 30.2007 | 146471.4232 | 145247.5418 | +8426176.46 ± 264.54 | ±0.37 |
| ${}^{157}$Ho | 157 | 90 | 54.7407 | -957287.64 ± 18.3140 | 147404.6143 | 146177.7414 | +8393021.03 ± 160.54 | ±0.38 |
| ${}^{158}$Ho | 158 | 91 | 61.1052 | -952596.31 ± 21.0334 | 148337.8152 | 147109.8810 | +8347054.73 ± 184.25 | ±0.38 |
| ${}^{159}$Ho | 159 | 92 | 67.4599 | -948037.87 ± 2.3515 | 149271.0259 | 148040.2329 | +8313908.86 ± 20.56 | ±0.38 |
| ${}^{160}$Ho | 160 | 93 | 73.8051 | -943460.64 ± 11.5093 | 150204.2461 | 148972.6742 | +8267099.62 ± 100.79 | ±0.38 |
| ${}^{161}$Ho | 161 | 94 | 80.1409 | -939022.11 ± 1.6415 | 151137.4758 | 149903.3544 | +8232780.24 ± 14.35 | ±0.38 |
| ${}^{162}$Ho | 162 | 95 | 86.4673 | -934552.80 ± 2.3543 | 152070.7148 | 150836.0042 | +8185781.15 ± 20.56 | ±0.38 |
| ${}^{163}$Ho | 163 | 96 | 92.7846 | -930215.41 ± 0.5272 | 153003.9629 | 151767.1609 | +8149338.96 ± 4.57 | ±0.39 |
| ${}^{164}$Ho | 164 | 97 | 99.0928 | -925843.14 ± 1.0432 | 153937.2201 | 152700.0525 | +8101946.33 ± 9.10 | ±0.39 |
| ${}^{165}$Ho | 165 | 98 | 105.3921 | -921597.74 ± 0.5892 | 154870.4862 | 153631.6291 | +8063815.77 ± 5.12 | ±0.39 |
| ${}^{166}$Ho | 166 | 99 | 111.6826 | -917302.28 ± 0.5777 | 155803.7612 | 154564.9509 | +8014820.27 ± 5.09 | ±0.39 |
| ${}^{167}$Ho | 167 | 100 | 117.9644 | -913119.15 ± 3.8252 | 156737.0448 | 155497.2359 | +7973189.49 ± 33.37 | ±0.39 |
| ${}^{168}$Ho | 168 | 101 | 124.2377 | -908891.52 ± 22.0037 | 157670.3370 | 156430.9502 | +7922899.94 ± 191.78 | ±0.39 |
| ${}^{169}$Ho | 169 | 102 | 130.5025 | -904772.72 ± 14.6256 | 158603.6376 | 157363.7075 | +7879390.21 ± 127.40 | ±0.40 |
| ${}^{170}$Ho | 170 | 103 | 136.7589 | -900607.21 ± 36.3489 | 159536.9465 | 158297.7601 | +7828199.25 ± 315.98 | ±0.40 |
| ${}^{171}$Ho | 171 | 104 | 143.0072 | -896543.72 ± 434.0639 | 160470.2637 | 159230.9739 | +7782969.29 ± 3768.12 | ±0.40 |
| ${}^{172}$Ho | 172 | 105 | 149.2473 | -892422.88 ± 123.9772 | 161403.5890 | 160165.5022 | +7730046.72 ± 1221.32 | ±0.40 |
| ${}^{173}$Ho | 173 | 106 | 155.4795 | -888412.55 ± 248.3238 | 162336.9223 | 161099.1294 | +7683423.73 ± 1850.28 | ±0.40 |
| ${}^{174}$Ho | 174 | 107 | 161.7037 | -884325.16 ± 248.9420 | 163270.2634 | 162034.1045 | +7629004.80 ± 1851.10 | ±0.40 |
| ${}^{175}$Ho | 175 | 108 | 167.9202 | -880341.22 ± 249.4077 | 164203.6124 | 162968.1686 | +7580890.52 ± 2452.08 | ±0.40 |
| ${}^{176}$Ho | 176 | 109 | 174.1289 | -876282.51 ± 375.1407 | 165136.9691 | 163903.5722 | +7525137.59 ± 3051.87 | ±0.41 |
| ${}^{177}$Ho | 177 | 110 | 180.3301 | -872329.08 ± 375.9398 | 166070.3334 | 164838.1765 | +7474948.24 ± 3034.57 | ±0.41 |
| ${}^{178}$Ho | 178 | 111 | 186.5237 | -868306.39 ± 377.0265 | 167003.7051 | 165773.8204 | +7419052.59 ± 3017.44 | ±0.41 |

### Erbium (Z = 68)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{142}$Er | 142 | 74 | -62.7586 | -1055994.21 ± 506.7782 | 133427.8499 | 132244.2328 | +8950236.25 ± 3782.49 | ±0.34 |
| ${}^{143}$Er | 143 | 75 | -56.1885 | -1049630.76 ± 378.9314 | 134360.8452 | 133172.4965 | +8923379.70 ± 3000.70 | ±0.34 |
| ${}^{144}$Er | 144 | 76 | -49.6310 | -1043320.71 ± 125.6913 | 135293.8531 | 134098.5432 | +8913668.03 ± 1458.73 | ±0.35 |
| ${}^{145}$Er | 145 | 77 | -43.0858 | -1037259.36 ± 125.3918 | 136226.8734 | 135027.4049 | +8883148.12 ± 1483.19 | ±0.35 |
| ${}^{146}$Er | 146 | 78 | -36.5528 | -1031254.12 ± 5.7300 | 137159.9058 | 135953.8171 | +8871311.41 ± 49.31 | ±0.35 |
| ${}^{147}$Er | 147 | 79 | -30.0318 | -1025452.98 ± 32.3679 | 138092.9502 | 136883.0254 | +8839114.54 ± 279.01 | ±0.35 |
| ${}^{148}$Er | 148 | 80 | -23.5225 | -1019719.87 ± 8.5859 | 139026.0064 | 137809.6484 | +8826363.30 ± 74.35 | ±0.35 |
| ${}^{149}$Er | 149 | 81 | -17.0249 | -1014150.09 ± 23.2199 | 139959.0742 | 138738.8798 | +8794898.49 ± 201.42 | ±0.36 |
| ${}^{150}$Er | 150 | 82 | -10.5388 | -1008671.55 ± 14.1443 | 140892.1535 | 139666.2842 | +8777130.68 ± 123.10 | ±0.36 |
| ${}^{151}$Er | 151 | 83 | -4.0639 | -1003320.62 ± 13.4610 | 141825.2440 | 140597.3434 | +8733455.40 ± 117.14 | ±0.36 |
| ${}^{152}$Er | 152 | 84 | 2.3999 | -998055.42 ± 7.1557 | 142758.3456 | 141526.6035 | +8703254.77 ± 62.38 | ±0.36 |
| ${}^{153}$Er | 153 | 85 | 8.8527 | -992873.22 ± 7.4765 | 143691.4582 | 142458.1312 | +8657470.14 ± 65.17 | ±0.36 |
| ${}^{154}$Er | 154 | 86 | 15.2948 | -987787.48 ± 3.9595 | 144624.5815 | 143387.4870 | +8627632.54 ± 34.59 | ±0.37 |
| ${}^{155}$Er | 155 | 87 | 21.7263 | -982757.79 ± 4.8220 | 145557.7155 | 144319.3769 | +8580542.87 ± 42.08 | ±0.37 |
| ${}^{156}$Er | 156 | 88 | 28.1473 | -977839.18 ± 19.3935 | 146490.8599 | 145248.8685 | +8550782.08 ± 169.56 | ±0.37 |
| ${}^{157}$Er | 157 | 89 | 34.5580 | -972946.85 ± 20.7463 | 147424.0146 | 146181.1606 | +8502148.97 ± 181.31 | ±0.37 |
| ${}^{158}$Er | 158 | 90 | 40.9585 | -968184.39 ± 19.5878 | 148357.1795 | 147110.7646 | +8472629.11 ± 171.43 | ±0.37 |
| ${}^{159}$Er | 159 | 91 | 47.3491 | -963428.57 ± 2.8123 | 149290.3544 | 148043.0014 | +8425613.00 ± 24.60 | ±0.37 |
| ${}^{160}$Er | 160 | 92 | 53.7297 | -958804.92 ± 18.5850 | 150223.5392 | 148972.9924 | +8394452.76 ± 162.75 | ±0.38 |
| ${}^{161}$Er | 161 | 93 | 60.1007 | -954173.53 ± 6.6905 | 151156.7337 | 149905.3494 | +8347829.19 ± 58.53 | ±0.38 |
| ${}^{162}$Er | 162 | 94 | 66.4620 | -949676.22 ± 0.5765 | 152089.9377 | 150835.7106 | +8315186.97 ± 5.01 | ±0.38 |
| ${}^{163}$Er | 163 | 95 | 72.8139 | -945153.42 ± 3.4869 | 153023.1513 | 151768.3715 | +8267729.00 ± 30.49 | ±0.38 |
| ${}^{164}$Er | 164 | 96 | 79.1565 | -940770.61 ± 0.5277 | 153956.3741 | 152699.0904 | +8233733.91 ± 4.61 | ±0.38 |
| ${}^{165}$Er | 165 | 97 | 85.4899 | -936348.35 ± 0.6880 | 154889.6062 | 153632.0058 | +8185796.96 ± 5.97 | ±0.39 |
| ${}^{166}$Er | 166 | 98 | 91.8142 | -932068.18 ± 0.2456 | 155822.8473 | 154563.0971 | +8150394.48 ± 2.16 | ±0.39 |
| ${}^{167}$Er | 167 | 99 | 98.1295 | -927739.67 ± 0.2091 | 156756.0973 | 155496.2261 | +8102262.78 ± 1.83 | ±0.39 |
| ${}^{168}$Er | 168 | 100 | 104.4361 | -923533.27 ± 0.1968 | 157689.3562 | 156428.0202 | +8063363.84 ± 1.67 | ±0.39 |
| ${}^{169}$Er | 169 | 101 | 110.7339 | -919276.89 ± 0.2218 | 158622.6238 | 157361.5824 | +8013655.17 ± 1.93 | ±0.39 |
| ${}^{170}$Er | 170 | 102 | 117.0231 | -915141.10 ± 1.0109 | 159555.9000 | 158293.8901 | +7972574.80 ± 8.76 | ±0.39 |
| ${}^{171}$Er | 171 | 103 | 123.3039 | -910953.49 ± 1.0126 | 160489.1846 | 159227.7739 | +7922052.16 ± 8.84 | ±0.39 |
| ${}^{172}$Er | 172 | 104 | 129.5763 | -906883.43 ± 2.8429 | 161422.4776 | 160160.5033 | +7879435.69 ± 24.74 | ±0.40 |
| ${}^{173}$Er | 173 | 105 | 135.8405 | -902748.92 ± 123.8543 | 162355.7789 | 161094.8259 | +7827396.12 ± 1214.28 | ±0.40 |
| ${}^{174}$Er | 174 | 106 | 142.0965 | -898729.32 ± 248.0159 | 163289.0883 | 162028.0246 | +7782997.23 ± 1839.67 | ±0.40 |
| ${}^{175}$Er | 175 | 107 | 148.3445 | -894632.31 ± 248.6016 | 164222.4057 | 162962.8162 | +7729306.15 ± 2457.88 | ±0.40 |
| ${}^{176}$Er | 176 | 108 | 154.5846 | -890674.43 ± 248.9420 | 165155.7311 | 163896.3317 | +7684121.97 ± 2443.88 | ±0.40 |
| ${}^{177}$Er | 177 | 109 | 160.8169 | -886613.03 ± 374.3916 | 166089.0642 | 164831.5983 | +7628791.68 ± 3051.64 | ±0.40 |
| ${}^{178}$Er | 178 | 110 | 167.0414 | -882681.00 ± 375.0469 | 167022.4051 | 165765.6904 | +7581272.00 ± 3596.38 | ±0.40 |
| ${}^{179}$Er | 179 | 111 | 173.2583 | -878645.53 ± 376.1284 | 167955.7537 | 166701.3650 | +7524765.41 ± 3000.65 | ±0.41 |
| ${}^{180}$Er | 180 | 112 | 179.4676 | -874743.42 ± 376.8844 | 168889.1097 | 167635.7588 | +7476631.99 ± 2983.92 | ±0.41 |

### Thulium (Z = 69)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{144}$Tm | 144 | 75 | -70.5820 | -1062439.83 ± 382.1656 | 135314.0218 | 134112.9916 | +8955360.36 ± 2979.66 | ±0.34 |
| ${}^{145}$Tm | 145 | 76 | -63.9959 | -1055945.09 ± 126.7588 | 136247.0011 | 135039.0626 | +8945104.49 ± 1448.57 | ±0.34 |
| ${}^{146}$Tm | 146 | 77 | -57.4223 | -1049697.16 ± 126.3584 | 137179.9929 | 135967.0841 | +8920606.64 ± 1472.94 | ±0.35 |
| ${}^{147}$Tm | 147 | 78 | -50.8610 | -1043527.67 ± 5.8499 | 138112.9971 | 136893.6588 | +8907193.31 ± 49.95 | ±0.35 |
| ${}^{148}$Tm | 148 | 79 | -44.3120 | -1037573.59 ± 8.6842 | 139046.0135 | 137822.3623 | +8878465.92 ± 74.35 | ±0.35 |
| ${}^{149}$Tm | 149 | 80 | -37.7749 | -1031674.48 ± 124.9375 | 139979.0418 | 138748.6810 | +8867549.22 ± 1443.41 | ±0.35 |
| ${}^{150}$Tm | 150 | 81 | -31.2495 | -1025973.09 ± 124.6727 | 140912.0819 | 139677.6247 | +8837902.16 ± 1400.47 | ±0.35 |
| ${}^{151}$Tm | 151 | 82 | -24.7358 | -1020349.33 ± 15.9378 | 141845.1336 | 140604.8380 | +8821144.01 ± 137.79 | ±0.36 |
| ${}^{152}$Tm | 152 | 83 | -18.2335 | -1014889.63 ± 44.1138 | 142778.1967 | 141535.3835 | +8780936.56 ± 381.72 | ±0.36 |
| ${}^{153}$Tm | 153 | 84 | -11.7425 | -1009508.85 ± 9.7011 | 143711.2711 | 142464.6253 | +8750564.21 ± 84.08 | ±0.36 |
| ${}^{154}$Tm | 154 | 85 | -5.2626 | -1004232.31 ± 11.5925 | 144644.3566 | 143395.6648 | +8708016.22 ± 100.50 | ±0.36 |
| ${}^{155}$Tm | 155 | 86 | 1.2064 | -999037.71 ± 7.9126 | 145577.4530 | 144324.9602 | +8678283.21 ± 68.74 | ±0.36 |
| ${}^{156}$Tm | 156 | 87 | 7.6646 | -993926.48 ± 11.3108 | 146510.5602 | 145256.2458 | +8635184.42 ± 98.29 | ±0.37 |
| ${}^{157}$Tm | 157 | 88 | 14.1123 | -988904.80 ± 21.9714 | 147443.6780 | 146185.8650 | +8604204.27 ± 191.16 | ±0.37 |
| ${}^{158}$Tm | 158 | 89 | 20.5494 | -983945.65 ± 19.7008 | 148376.8063 | 147117.3652 | +8560791.83 ± 171.42 | ±0.37 |
| ${}^{159}$Tm | 159 | 90 | 26.9762 | -979087.02 ± 21.6696 | 149309.9449 | 148046.9921 | +8530756.40 ± 188.76 | ±0.37 |
| ${}^{160}$Tm | 160 | 91 | 33.3929 | -974268.22 ± 25.1886 | 150243.0937 | 148978.7556 | +8486700.69 ± 219.40 | ±0.37 |
| ${}^{161}$Tm | 161 | 92 | 39.7996 | -969558.22 ± 21.3780 | 151176.2524 | 149908.6520 | +8455819.16 ± 186.41 | ±0.37 |
| ${}^{162}$Tm | 162 | 93 | 46.1963 | -964871.02 ± 19.8212 | 152109.4211 | 150840.5673 | +8411886.72 ± 172.75 | ±0.38 |
| ${}^{163}$Tm | 163 | 94 | 52.5834 | -960295.60 ± 4.1600 | 153042.5995 | 151770.8105 | +8379667.85 ± 36.33 | ±0.38 |
| ${}^{164}$Tm | 164 | 95 | 58.9608 | -955722.61 ± 18.7816 | 153975.7875 | 152703.1241 | +8334232.90 ± 163.76 | ±0.38 |
| ${}^{165}$Tm | 165 | 96 | 65.3288 | -951273.22 ± 1.2430 | 154908.9849 | 153633.5971 | +8301490.47 ± 10.79 | ±0.38 |
| ${}^{166}$Tm | 166 | 97 | 71.6874 | -946809.33 ± 8.5726 | 155842.1917 | 154566.1347 | +8255734.66 ± 74.73 | ±0.38 |
| ${}^{167}$Tm | 167 | 98 | 78.0368 | -942470.75 ± 0.9234 | 156775.4078 | 155496.9722 | +8221610.54 ± 8.09 | ±0.38 |
| ${}^{168}$Tm | 168 | 99 | 84.3771 | -938108.73 ± 1.2323 | 157708.6329 | 156429.6970 | +8175786.51 ± 10.72 | ±0.39 |
| ${}^{169}$Tm | 169 | 100 | 90.7085 | -933854.41 ± 0.5422 | 158641.8669 | 157361.2289 | +8138205.67 ± 4.69 | ±0.39 |
| ${}^{170}$Tm | 170 | 101 | 97.0310 | -929582.46 ± 0.5305 | 159575.1098 | 158294.2023 | +8091942.04 ± 4.62 | ±0.39 |
| ${}^{171}$Tm | 171 | 102 | 103.3448 | -925405.67 ± 0.7035 | 160508.3615 | 159226.2815 | +8051937.07 ± 6.10 | ±0.39 |
| ${}^{172}$Tm | 172 | 103 | 109.6499 | -921209.15 ± 3.9426 | 161441.6217 | 160159.6123 | +8004573.70 ± 34.22 | ±0.39 |
| ${}^{173}$Tm | 173 | 104 | 115.9466 | -917098.80 ± 3.1418 | 162374.8904 | 161092.2239 | +7962312.13 ± 27.31 | ±0.39 |
| ${}^{174}$Tm | 174 | 105 | 122.2349 | -912956.19 ± 31.8438 | 163308.1676 | 162026.1095 | +7912663.23 ± 276.01 | ±0.40 |
| ${}^{175}$Tm | 175 | 106 | 128.5150 | -908906.93 ± 35.4389 | 164241.4530 | 162959.1576 | +7868814.40 ± 306.82 | ±0.40 |
| ${}^{176}$Tm | 176 | 107 | 134.7868 | -904807.63 ± 70.6267 | 165174.7465 | 163893.5909 | +7816996.27 ± 610.15 | ±0.40 |
| ${}^{177}$Tm | 177 | 108 | 141.0506 | -900821.89 ± 124.4555 | 166108.0481 | 164826.8868 | +7772769.05 ± 1215.04 | ±0.40 |
| ${}^{178}$Tm | 178 | 109 | 147.3065 | -896773.81 ± 249.4699 | 167041.3577 | 165761.7101 | +7719802.34 ± 1809.47 | ±0.40 |
| ${}^{179}$Tm | 179 | 110 | 153.5545 | -892822.83 ± 249.8751 | 167974.6752 | 166695.5441 | +7673456.78 ± 2397.25 | ±0.40 |
| ${}^{180}$Tm | 180 | 111 | 159.7947 | -888795.16 ± 250.5324 | 168908.0003 | 167630.7688 | +7619314.23 ± 2383.88 | ±0.40 |
| ${}^{181}$Tm | 181 | 112 | 166.0273 | -884894.25 ± 376.4588 | 169841.3332 | 168564.9931 | +7571797.74 ± 2967.47 | ±0.41 |
| ${}^{182}$Tm | 182 | 113 | 172.2523 | -880920.85 ± 377.4534 | 170774.6736 | 169500.4368 | +7517601.87 ± 2951.10 | ±0.41 |

### Ytterbium (Z = 70)

_38 of 38 isotopes with a framework prediction; 38 of 38 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{148}$Yb | 148 | 78 | -65.3695 | -1055867.17 ± 379.4586 | 139066.2887 | 137830.8976 | +8963092.55 ± 2899.28 | ±0.35 |
| ${}^{149}$Yb | 149 | 79 | -58.7923 | -1049776.61 ± 252.3023 | 139999.2769 | 138759.2917 | +8936231.95 ± 2161.59 | ±0.35 |
| ${}^{150}$Yb | 150 | 80 | -52.2272 | -1043713.93 ± 251.0986 | 140932.2772 | 139685.2853 | +8927153.14 ± 2147.26 | ±0.35 |
| ${}^{151}$Yb | 151 | 81 | -45.6741 | -1037886.61 ± 249.2561 | 141865.2895 | 140614.0673 | +8898272.00 ± 2137.00 | ±0.35 |
| ${}^{152}$Yb | 152 | 82 | -39.1327 | -1032119.56 ± 122.8754 | 142798.3136 | 141540.8334 | +8884222.25 ± 1057.70 | ±0.35 |
| ${}^{153}$Yb | 153 | 83 | -32.6030 | -1026563.38 ± 124.6572 | 143731.3493 | 142471.4382 | +8843253.75 ± 1405.69 | ±0.36 |
| ${}^{154}$Yb | 154 | 84 | -26.0847 | -1021067.43 ± 13.9553 | 144664.3964 | 143400.1599 | +8816144.12 ± 120.50 | ±0.36 |
| ${}^{155}$Yb | 155 | 85 | -19.5776 | -1015702.36 ± 13.3146 | 145597.4547 | 144331.0835 | +8774071.46 ± 115.01 | ±0.36 |
| ${}^{156}$Yb | 156 | 86 | -13.0816 | -1010401.81 ± 7.4054 | 146530.5241 | 145259.8146 | +8747839.16 ± 64.07 | ±0.36 |
| ${}^{157}$Yb | 157 | 87 | -6.5965 | -1005211.14 ± 8.6199 | 147463.6045 | 146191.1544 | +8704015.89 ± 74.59 | ±0.36 |
| ${}^{158}$Yb | 158 | 88 | -0.1222 | -1000095.77 ± 6.2506 | 148396.6956 | 147120.0588 | +8677517.40 ± 54.19 | ±0.36 |
| ${}^{159}$Yb | 159 | 89 | 6.3414 | -995062.77 ± 13.6914 | 149329.7974 | 148051.7290 | +8632580.13 ± 118.75 | ±0.37 |
| ${}^{160}$Yb | 160 | 90 | 12.7946 | -990118.52 ± 4.2385 | 150262.9096 | 148980.8934 | +8605239.28 ± 36.89 | ±0.37 |
| ${}^{161}$Yb | 161 | 91 | 19.2375 | -985230.90 ± 11.5940 | 151196.0321 | 149912.7165 | +8560419.11 ± 100.73 | ±0.37 |
| ${}^{162}$Yb | 162 | 92 | 25.6702 | -980443.36 ± 11.5026 | 152129.1648 | 150842.2236 | +8531703.96 ± 100.12 | ±0.37 |
| ${}^{163}$Yb | 163 | 93 | 32.0929 | -975690.01 ± 11.4457 | 153062.3076 | 151774.2450 | +8486700.33 ± 99.52 | ±0.37 |
| ${}^{164}$Yb | 164 | 94 | 38.5057 | -971047.09 ± 11.3572 | 153995.4602 | 152704.0208 | +8457140.37 ± 98.92 | ±0.38 |
| ${}^{165}$Yb | 165 | 95 | 44.9088 | -966418.27 ± 19.8400 | 154928.6225 | 153636.2317 | +8412018.47 ± 172.73 | ±0.38 |
| ${}^{166}$Yb | 166 | 96 | 51.3022 | -961904.32 ± 5.2019 | 155861.7945 | 154566.4275 | +8380649.25 ± 45.29 | ±0.38 |
| ${}^{167}$Yb | 167 | 97 | 57.6862 | -957387.40 ± 2.9237 | 156794.9760 | 155498.9254 | +8334787.96 ± 25.47 | ±0.38 |
| ${}^{168}$Yb | 168 | 98 | 64.0608 | -952993.14 ± 0.0740 | 157728.1668 | 156429.4296 | +8302384.39 ± 0.60 | ±0.38 |
| ${}^{169}$Yb | 169 | 99 | 70.4262 | -948581.42 ± 0.1357 | 158661.3669 | 157362.1280 | +8256363.07 ± 1.13 | ±0.38 |
| ${}^{170}$Yb | 170 | 100 | 76.7824 | -944284.79 ± 0.0370 | 159594.5760 | 158293.2337 | +8221086.16 ± 0.06 | ±0.39 |
| ${}^{171}$Yb | 171 | 101 | 83.1297 | -939967.17 ± 0.0370 | 160527.7942 | 159226.1849 | +8174592.87 ± 0.08 | ±0.39 |
| ${}^{172}$Yb | 172 | 102 | 89.4682 | -935761.87 ± 0.0370 | 161461.0212 | 160157.7304 | +8137545.20 ± 0.08 | ±0.39 |
| ${}^{173}$Yb | 173 | 103 | 95.7978 | -931530.18 ± 0.0371 | 162394.2569 | 161090.9287 | +8090636.76 ± 0.07 | ±0.39 |
| ${}^{174}$Yb | 174 | 104 | 102.1189 | -927399.66 ± 0.0371 | 163327.5013 | 162023.0295 | +8051150.21 ± 0.06 | ±0.39 |
| ${}^{175}$Yb | 175 | 105 | 108.4314 | -923229.61 ± 0.0620 | 164260.7542 | 162956.7726 | +8002009.09 ± 0.43 | ±0.39 |
| ${}^{176}$Yb | 176 | 106 | 114.7355 | -919159.29 ± 0.0372 | 165194.0155 | 163889.4709 | +7959904.51 ± 0.09 | ±0.39 |
| ${}^{177}$Yb | 177 | 107 | 121.0314 | -915056.50 ± 0.1615 | 166127.2851 | 164823.4700 | +7910372.93 ± 1.33 | ±0.40 |
| ${}^{178}$Yb | 178 | 108 | 127.3190 | -911065.72 ± 4.6004 | 167060.5629 | 165756.2733 | +7868719.00 ± 39.74 | ±0.40 |
| ${}^{179}$Yb | 179 | 109 | 133.5985 | -907007.16 ± 124.5951 | 167993.8487 | 166690.8047 | +7817132.35 ± 1201.45 | ±0.40 |
| ${}^{180}$Yb | 180 | 110 | 139.8701 | -903061.87 ± 249.5010 | 168927.1426 | 167624.2186 | +7772886.53 ± 1789.37 | ±0.40 |
| ${}^{181}$Yb | 181 | 111 | 146.1338 | -899028.40 ± 250.1251 | 169860.4443 | 168559.3446 | +7718941.84 ± 1768.39 | ±0.40 |
| ${}^{182}$Yb | 182 | 112 | 152.3897 | -895127.02 ± 250.5010 | 170793.7539 | 169493.0268 | +7674222.04 ± 2357.68 | ±0.40 |
| ${}^{183}$Yb | 183 | 113 | 158.6379 | -891137.31 ± 251.1616 | 171727.0711 | 170428.4210 | +7619914.91 ± 2344.74 | ±0.40 |
| ${}^{184}$Yb | 184 | 114 | 164.8785 | -887299.87 ± 377.3110 | 172660.3959 | 171362.3147 | +7575068.31 ± 2935.34 | ±0.41 |
| ${}^{185}$Yb | 185 | 115 | 171.1116 | -883348.77 ± 378.3579 | 173593.7282 | 172297.9288 | +7520690.76 ± 2903.18 | ±0.41 |

### Lutetium (Z = 71)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{150}$Lu | 150 | 79 | -73.4719 | -1062269.57 ± 254.2588 | 140952.7395 | 139699.3443 | +8972090.83 ± 2147.05 | ±0.34 |
| ${}^{151}$Lu | 151 | 80 | -66.8788 | -1056035.65 ± 253.0364 | 141885.7119 | 140625.3091 | +8962844.48 ± 2132.91 | ±0.35 |
| ${}^{152}$Lu | 152 | 81 | -60.2978 | -1050049.96 ± 126.1670 | 142818.6963 | 141553.6818 | +8936641.78 ± 1381.91 | ±0.35 |
| ${}^{153}$Lu | 153 | 82 | -53.7287 | -1044121.66 ± 123.1925 | 143751.6927 | 142480.2224 | +8923836.91 ± 1052.90 | ±0.35 |
| ${}^{154}$Lu | 154 | 83 | -47.1714 | -1038442.27 ± 125.5020 | 144684.7008 | 143410.4252 | +8885515.61 ± 1402.99 | ±0.35 |
| ${}^{155}$Lu | 155 | 84 | -40.6257 | -1032814.21 ± 15.5494 | 145617.7205 | 144339.0410 | +8858860.92 ± 133.33 | ±0.35 |
| ${}^{156}$Lu | 156 | 85 | -34.0914 | -1027332.65 ± 43.3876 | 146550.7516 | 145269.3806 | +8820654.40 ± 372.56 | ±0.36 |
| ${}^{157}$Lu | 157 | 86 | -27.5684 | -1021912.87 ± 9.5965 | 147483.7940 | 146198.1345 | +8793953.09 ± 82.58 | ±0.36 |
| ${}^{158}$Lu | 158 | 87 | -21.0564 | -1016619.97 ± 11.9348 | 148416.8475 | 147128.8562 | +8754171.70 ± 102.79 | ±0.36 |
| ${}^{159}$Lu | 159 | 88 | -14.5554 | -1011393.61 ± 29.4850 | 149349.9118 | 148057.8539 | +8726709.99 ± 254.38 | ±0.36 |
| ${}^{160}$Lu | 160 | 89 | -8.0651 | -1006270.79 ± 44.1758 | 150282.9870 | 148988.7867 | +8686561.97 ± 381.38 | ±0.36 |
| ${}^{161}$Lu | 161 | 90 | -1.5854 | -1001222.85 ± 21.5578 | 151216.0727 | 149917.9883 | +8658630.03 ± 186.40 | ±0.37 |
| ${}^{162}$Lu | 162 | 91 | 4.8838 | -996257.18 ± 57.5078 | 152149.1690 | 150849.2130 | +8617585.10 ± 497.42 | ±0.37 |
| ${}^{163}$Lu | 163 | 92 | 11.3426 | -991373.56 ± 21.2479 | 153082.2755 | 151778.7475 | +8588343.58 ± 184.12 | ±0.37 |
| ${}^{164}$Lu | 164 | 93 | 17.7913 | -986550.16 ± 21.1262 | 154015.3922 | 152710.3906 | +8545598.02 ± 182.99 | ±0.37 |
| ${}^{165}$Lu | 165 | 94 | 24.2300 | -981818.35 ± 19.9090 | 154948.5190 | 153640.0849 | +8516228.95 ± 172.73 | ±0.37 |
| ${}^{166}$Lu | 166 | 95 | 30.6588 | -977125.66 ± 22.2438 | 155881.6557 | 154572.0002 | +8472785.66 ± 192.84 | ±0.37 |
| ${}^{167}$Lu | 167 | 96 | 37.0778 | -972532.73 ± 27.6006 | 156814.8021 | 155501.9890 | +8442419.55 ± 239.61 | ±0.38 |
| ${}^{168}$Lu | 168 | 97 | 43.4872 | -967965.43 ± 27.9689 | 157747.9581 | 156433.9366 | +8399849.48 ± 242.74 | ±0.38 |
| ${}^{169}$Lu | 169 | 98 | 49.8871 | -963495.19 ± 2.2012 | 158681.1237 | 157364.4210 | +8367219.50 ± 19.10 | ±0.38 |
| ${}^{170}$Lu | 170 | 99 | 56.2776 | -959037.60 ± 12.2623 | 159614.2986 | 158296.6914 | +8323655.74 ± 106.40 | ±0.38 |
| ${}^{171}$Lu | 171 | 100 | 62.6588 | -954676.41 ± 1.3482 | 160547.4827 | 159227.6633 | +8288882.83 ± 11.69 | ±0.38 |
| ${}^{172}$Lu | 172 | 101 | 69.0310 | -950317.98 ± 1.6835 | 161480.6760 | 160160.2498 | +8244406.62 ± 14.58 | ±0.38 |
| ${}^{173}$Lu | 173 | 102 | 75.3941 | -946057.36 ± 1.1264 | 162413.8783 | 161091.5989 | +8208245.13 ± 9.73 | ±0.39 |
| ${}^{174}$Lu | 174 | 103 | 81.7484 | -941792.59 ± 1.1150 | 163347.0894 | 162024.4038 | +8163496.55 ± 9.67 | ±0.39 |
| ${}^{175}$Lu | 175 | 104 | 88.0939 | -937614.95 ± 0.8551 | 164280.3093 | 162956.3025 | +8124919.66 ± 7.40 | ±0.39 |
| ${}^{176}$Lu | 176 | 105 | 94.4308 | -933423.88 ± 0.8562 | 165213.5379 | 163889.5799 | +8078353.67 ± 7.39 | ±0.39 |
| ${}^{177}$Lu | 177 | 106 | 100.7591 | -929314.73 ± 0.8568 | 166146.7750 | 164822.0725 | +8037167.28 ± 7.40 | ±0.39 |
| ${}^{178}$Lu | 178 | 107 | 107.0789 | -925197.34 ± 1.5792 | 167080.0206 | 165755.6126 | +7990124.52 ± 13.58 | ±0.39 |
| ${}^{179}$Lu | 179 | 108 | 113.3905 | -921162.34 ± 3.5843 | 168013.2744 | 166688.3856 | +7948297.50 ± 30.89 | ±0.40 |
| ${}^{180}$Lu | 180 | 109 | 119.6938 | -917107.64 ± 48.9776 | 168946.5365 | 167622.2622 | +7900348.69 ± 421.93 | ±0.40 |
| ${}^{181}$Lu | 181 | 110 | 125.9891 | -913120.53 ± 86.7207 | 169879.8067 | 168555.6354 | +7855989.77 ± 746.05 | ±0.40 |
| ${}^{182}$Lu | 182 | 111 | 132.2763 | -909105.45 ± 125.0625 | 170813.0849 | 169490.1568 | +7805338.76 ± 1181.61 | ±0.40 |
| ${}^{183}$Lu | 183 | 112 | 138.5556 | -905178.18 ± 54.8291 | 171746.3710 | 170423.7049 | +7761045.67 ± 470.05 | ±0.40 |
| ${}^{184}$Lu | 184 | 113 | 144.8271 | -901204.49 ± 125.5178 | 172679.6649 | 171358.6148 | +7709272.11 ± 1168.73 | ±0.40 |
| ${}^{185}$Lu | 185 | 114 | 151.0909 | -897334.07 ± 251.4142 | 173612.9666 | 172292.4488 | +7664397.49 ± 1740.88 | ±0.40 |
| ${}^{186}$Lu | 186 | 115 | 157.3470 | -893403.24 ± 252.0161 | 174546.2758 | 173227.5832 | +7612486.80 ± 2306.86 | ±0.40 |
| ${}^{187}$Lu | 187 | 116 | 163.5957 | -889581.82 ± 252.4296 | 175479.5926 | 174161.6277 | +7567481.76 ± 2294.48 | ±0.41 |
| ${}^{188}$Lu | 188 | 117 | 169.8369 | -885690.54 ± 253.0685 | 176412.9169 | 175097.0713 | +7514948.79 ± 2282.23 | ±0.41 |

### Hafnium (Z = 72)

_38 of 38 isotopes with a framework prediction; 38 of 38 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{153}$Hf | 153 | 81 | -75.1197 | -1062291.12 ± 253.7427 | 143772.3013 | 142491.2976 | +8990048.60 ± 2104.98 | ±0.35 |
| ${}^{154}$Hf | 154 | 82 | -68.5229 | -1056195.24 ± 252.5890 | 144705.2699 | 143417.3621 | +8980139.18 ± 2091.39 | ±0.35 |
| ${}^{155}$Hf | 155 | 83 | -61.9380 | -1050397.28 ± 252.2386 | 145638.2505 | 144347.2764 | +8943529.35 ± 2077.91 | ±0.35 |
| ${}^{156}$Hf | 156 | 84 | -55.3648 | -1044626.89 ± 120.7016 | 146571.2427 | 145275.2607 | +8920872.32 ± 1030.73 | ±0.35 |
| ${}^{157}$Hf | 157 | 85 | -48.8032 | -1039051.35 ± 125.6281 | 147504.2465 | 146205.7198 | +8881504.41 ± 1369.79 | ±0.35 |
| ${}^{158}$Hf | 158 | 86 | -42.2531 | -1033506.47 ± 13.8700 | 148437.2618 | 147133.9660 | +8857885.28 ± 118.89 | ±0.36 |
| ${}^{159}$Hf | 159 | 87 | -35.7141 | -1028124.37 ± 13.2347 | 149370.2883 | 148064.7099 | +8817620.13 ± 113.55 | ±0.36 |
| ${}^{160}$Hf | 160 | 88 | -29.1862 | -1022783.58 ± 7.4441 | 150303.3258 | 148993.1178 | +8793748.14 ± 64.03 | ±0.36 |
| ${}^{161}$Hf | 161 | 89 | -22.6693 | -1017580.32 ± 18.1918 | 151236.3743 | 149924.2349 | +8752016.57 ± 156.41 | ±0.36 |
| ${}^{162}$Hf | 162 | 90 | -16.1631 | -1012429.39 ± 6.8891 | 152169.4335 | 150852.8764 | +8727424.76 ± 59.34 | ±0.36 |
| ${}^{163}$Hf | 163 | 91 | -9.6675 | -1007387.88 ± 19.6313 | 153102.5034 | 151784.2696 | +8684916.91 ± 169.27 | ±0.37 |
| ${}^{164}$Hf | 164 | 92 | -3.1824 | -1002412.41 ± 11.9844 | 154035.5837 | 152713.2147 | +8659165.63 ± 103.54 | ±0.37 |
| ${}^{165}$Hf | 165 | 93 | 3.2924 | -997519.08 ± 21.0621 | 154968.6743 | 153644.8916 | +8615858.94 ± 181.88 | ±0.37 |
| ${}^{166}$Hf | 166 | 94 | 9.7570 | -992704.35 ± 20.8901 | 155901.7751 | 154574.1622 | +8588841.02 ± 180.79 | ±0.37 |
| ${}^{167}$Hf | 167 | 95 | 16.2115 | -987947.25 ± 20.7718 | 156834.8860 | 155506.0476 | +8545252.45 ± 179.70 | ±0.37 |
| ${}^{168}$Hf | 168 | 96 | 22.6562 | -983279.72 ± 20.6185 | 157768.0068 | 156435.6489 | +8516971.04 ± 178.63 | ±0.37 |
| ${}^{169}$Hf | 169 | 97 | 29.0911 | -978647.82 ± 20.5166 | 158701.1373 | 157367.7866 | +8472830.98 ± 177.58 | ±0.38 |
| ${}^{170}$Hf | 170 | 98 | 35.5163 | -974114.39 ± 20.3695 | 159634.2775 | 158297.7438 | +8443163.24 ± 176.53 | ±0.38 |
| ${}^{171}$Hf | 171 | 99 | 41.9321 | -969598.97 ± 20.9396 | 160567.4271 | 159230.0604 | +8398959.07 ± 181.35 | ±0.38 |
| ${}^{172}$Hf | 172 | 100 | 48.3384 | -965182.57 ± 17.5922 | 161500.5862 | 160160.5836 | +8366619.12 ± 152.52 | ±0.38 |
| ${}^{173}$Hf | 173 | 101 | 54.7355 | -960774.89 ± 20.0223 | 162433.7545 | 161093.0682 | +8322433.69 ± 173.47 | ±0.38 |
| ${}^{174}$Hf | 174 | 102 | 61.1235 | -956462.42 ± 1.6112 | 163366.9320 | 162024.1295 | +8287670.05 ± 13.94 | ±0.38 |
| ${}^{175}$Hf | 175 | 103 | 67.5024 | -952147.43 ± 1.6128 | 164300.1185 | 162956.9864 | +8242249.13 ± 14.00 | ±0.39 |
| ${}^{176}$Hf | 176 | 104 | 73.8725 | -947933.10 ± 1.0420 | 165233.3138 | 163888.3858 | +8206365.62 ± 9.04 | ±0.39 |
| ${}^{177}$Hf | 177 | 105 | 80.2338 | -943702.53 ± 0.9936 | 166166.5180 | 164821.5756 | +8159989.89 ± 8.56 | ±0.39 |
| ${}^{178}$Hf | 178 | 106 | 86.5863 | -939568.48 ± 0.9939 | 167099.7308 | 165753.5151 | +8121793.00 ± 8.54 | ±0.39 |
| ${}^{179}$Hf | 179 | 107 | 92.9304 | -935415.68 ± 0.9828 | 168032.9522 | 166686.9815 | +8074839.96 ± 8.49 | ±0.39 |
| ${}^{180}$Hf | 180 | 108 | 99.2659 | -931365.01 ± 0.9832 | 168966.1821 | 167619.1592 | +8036210.70 ± 8.47 | ±0.39 |
| ${}^{181}$Hf | 181 | 109 | 105.5932 | -927276.55 ± 0.9848 | 169899.4203 | 168553.0298 | +7987933.83 ± 8.44 | ±0.39 |
| ${}^{182}$Hf | 182 | 110 | 111.9122 | -923279.54 ± 4.2297 | 170832.6667 | 169485.8772 | +7946322.59 ± 36.38 | ±0.40 |
| ${}^{183}$Hf | 183 | 111 | 118.2230 | -919246.88 ± 20.5249 | 171765.9213 | 170420.1374 | +7896859.20 ± 176.28 | ±0.40 |
| ${}^{184}$Hf | 184 | 112 | 124.5258 | -915305.42 ± 27.0063 | 172699.1839 | 171353.4156 | +7853757.86 ± 231.71 | ±0.40 |
| ${}^{185}$Hf | 185 | 113 | 130.8207 | -911319.08 ± 43.5667 | 173632.4544 | 172288.0894 | +7803006.15 ± 373.06 | ±0.40 |
| ${}^{186}$Hf | 186 | 114 | 137.1078 | -907444.69 ± 34.5793 | 174565.7328 | 173221.4791 | +7760317.67 ± 295.76 | ±0.40 |
| ${}^{187}$Hf | 187 | 115 | 143.3871 | -903513.80 ± 125.8336 | 175499.0189 | 174156.3974 | +7709286.41 ± 1149.95 | ±0.40 |
| ${}^{188}$Hf | 188 | 116 | 149.6587 | -899690.39 ± 252.0161 | 176432.3127 | 175090.0618 | +7666059.49 ± 1713.07 | ±0.40 |
| ${}^{189}$Hf | 189 | 117 | 155.9228 | -895795.31 ± 252.6209 | 177365.6140 | 176025.2353 | +7614695.96 ± 1703.97 | ±0.41 |
| ${}^{190}$Hf | 190 | 118 | 162.1795 | -892020.73 ± 253.0044 | 178298.9228 | 176959.0796 | +7571485.87 ± 2258.21 | ±0.41 |

### Tantalum (Z = 73)

_40 of 40 isotopes with a framework prediction; 40 of 40 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{155}$Ta | 155 | 82 | -83.5144 | -1068567.41 ± 254.5177 | 145659.0445 | 144357.5982 | +9015433.32 ± 2077.76 | ±0.35 |
| ${}^{156}$Ta | 156 | 83 | -76.9019 | -1062622.03 ± 254.0650 | 146591.9974 | 145287.0794 | +8981652.13 ± 2064.47 | ±0.35 |
| ${}^{157}$Ta | 157 | 84 | -70.3012 | -1056709.06 ± 121.0350 | 147524.9621 | 146214.9783 | +8959299.64 ± 1026.24 | ±0.35 |
| ${}^{158}$Ta | 158 | 85 | -63.7122 | -1050998.09 ± 126.4702 | 148457.9386 | 147144.9500 | +8923096.90 ± 1361.05 | ±0.35 |
| ${}^{159}$Ta | 159 | 86 | -57.1348 | -1045321.10 ± 15.6141 | 149390.9266 | 148073.1233 | +8899679.26 ± 132.97 | ±0.35 |
| ${}^{160}$Ta | 160 | 87 | -50.5688 | -1039814.11 ± 42.7675 | 150323.9261 | 149003.2329 | +8863520.19 ± 364.53 | ±0.36 |
| ${}^{161}$Ta | 161 | 88 | -44.0141 | -1034355.13 ± 19.0262 | 151256.9367 | 149931.7721 | +8838450.74 ± 162.61 | ±0.36 |
| ${}^{162}$Ta | 162 | 89 | -37.4703 | -1029041.75 ± 49.0813 | 152189.9584 | 150862.2634 | +8800709.99 ± 419.73 | ±0.36 |
| ${}^{163}$Ta | 163 | 90 | -30.9376 | -1023778.95 ± 29.2537 | 153122.9911 | 151791.0043 | +8775136.54 ± 250.75 | ±0.36 |
| ${}^{164}$Ta | 164 | 91 | -24.4155 | -1018639.70 ± 21.3347 | 154056.0345 | 152721.7502 | +8736700.91 ± 182.98 | ±0.36 |
| ${}^{165}$Ta | 165 | 92 | -17.9041 | -1013558.55 ± 10.2836 | 154989.0885 | 153650.6792 | +8710727.71 ± 88.34 | ±0.37 |
| ${}^{166}$Ta | 166 | 93 | -11.4032 | -1008581.40 ± 21.0244 | 155922.1530 | 154581.9234 | +8670027.41 ± 180.78 | ±0.37 |
| ${}^{167}$Ta | 167 | 94 | -4.9126 | -1003668.42 ± 20.8633 | 156855.2278 | 155511.1643 | +8642874.65 ± 179.70 | ±0.37 |
| ${}^{168}$Ta | 168 | 95 | 1.5679 | -998836.26 ± 20.7371 | 157788.3127 | 156442.6155 | +8601858.44 ± 178.63 | ±0.37 |
| ${}^{169}$Ta | 169 | 96 | 8.0383 | -994077.46 ± 20.5953 | 158721.4078 | 157372.2131 | +8573271.34 ± 177.57 | ±0.37 |
| ${}^{170}$Ta | 170 | 97 | 14.4987 | -989379.39 ± 20.4725 | 159654.5127 | 158303.8600 | +8532026.71 ± 176.53 | ±0.37 |
| ${}^{171}$Ta | 171 | 98 | 20.9494 | -984761.88 ± 20.3239 | 160587.6274 | 159233.7715 | +8502316.92 ± 175.50 | ±0.38 |
| ${}^{172}$Ta | 172 | 99 | 27.3905 | -980187.50 ± 20.2172 | 161520.7518 | 160165.6559 | +8460590.09 ± 174.47 | ±0.38 |
| ${}^{173}$Ta | 173 | 100 | 33.8220 | -975695.99 ± 20.0769 | 162453.8857 | 161096.0834 | +8428524.64 ± 173.47 | ±0.38 |
| ${}^{174}$Ta | 174 | 101 | 40.2442 | -971234.42 ± 19.9740 | 163387.0290 | 162028.2333 | +8386166.36 ± 172.47 | ±0.38 |
| ${}^{175}$Ta | 175 | 102 | 46.6570 | -966857.69 ± 19.8522 | 164320.1816 | 162959.0595 | +8352539.96 ± 171.48 | ±0.38 |
| ${}^{176}$Ta | 176 | 103 | 53.0607 | -962496.11 ± 21.7324 | 165253.3433 | 163891.5969 | +8308823.73 ± 187.56 | ±0.38 |
| ${}^{177}$Ta | 177 | 104 | 59.4554 | -958224.92 ± 2.3256 | 166186.5140 | 164822.7416 | +8274176.14 ± 20.11 | ±0.38 |
| ${}^{178}$Ta | 178 | 105 | 65.8412 | -953964.63 ± 0.0000 | 167119.6937 | 165755.3517 | +8231058.32 ± 314.70 | ±0.39 |
| ${}^{179}$Ta | 179 | 106 | 72.2181 | -949779.19 ± 1.0207 | 168052.8821 | 166687.0871 | +8193766.21 ± 8.80 | ±0.39 |
| ${}^{180}$Ta | 180 | 107 | 78.5864 | -945602.13 ± 1.4329 | 168986.0793 | 167620.0050 | +8149828.23 ± 12.33 | ±0.39 |
| ${}^{181}$Ta | 181 | 108 | 84.9461 | -941506.70 ± 1.0843 | 169919.2850 | 168551.9937 | +8111985.41 ± 9.35 | ±0.39 |
| ${}^{182}$Ta | 182 | 109 | 91.2973 | -937394.67 ± 1.0858 | 170852.4992 | 169485.4962 | +8065604.84 ± 9.30 | ±0.39 |
| ${}^{183}$Ta | 183 | 110 | 97.6401 | -933362.05 ± 1.0866 | 171785.7218 | 170418.1274 | +8024934.87 ± 9.33 | ±0.39 |
| ${}^{184}$Ta | 184 | 111 | 103.9747 | -929309.80 ± 17.6888 | 172718.9526 | 171352.0756 | +7977008.79 ± 151.79 | ±0.40 |
| ${}^{185}$Ta | 185 | 112 | 110.3012 | -925344.92 ± 9.5788 | 173652.1916 | 172285.0148 | +7935552.77 ± 82.19 | ±0.40 |
| ${}^{186}$Ta | 186 | 113 | 116.6195 | -921349.77 ± 40.4675 | 174585.4387 | 173219.2957 | +7886783.10 ± 346.45 | ±0.40 |
| ${}^{187}$Ta | 187 | 114 | 122.9299 | -917447.98 ± 37.5351 | 175518.6937 | 174152.5018 | +7844801.90 ± 320.92 | ±0.40 |
| ${}^{188}$Ta | 188 | 115 | 129.2325 | -913511.99 ± 125.8178 | 176451.9566 | 175086.9814 | +7795983.51 ± 1143.84 | ±0.40 |
| ${}^{189}$Ta | 189 | 116 | 135.5272 | -909665.49 ± 125.9763 | 177385.2273 | 176020.4260 | +7753652.52 ± 1137.77 | ±0.40 |
| ${}^{190}$Ta | 190 | 117 | 141.8143 | -905782.48 ± 126.2307 | 178318.5056 | 176955.1599 | +7704469.93 ± 1131.76 | ±0.40 |
| ${}^{191}$Ta | 191 | 118 | 148.0938 | -901989.58 ± 252.8125 | 179251.7915 | 177888.8542 | +7661735.37 ± 1686.12 | ±0.40 |
| ${}^{192}$Ta | 192 | 119 | 154.3659 | -898151.91 ± 253.3570 | 180185.0849 | 178823.7678 | +7612618.44 ± 2234.66 | ±0.41 |
| ${}^{193}$Ta | 193 | 120 | 160.6305 | -894420.62 ± 253.7105 | 181118.3857 | 179757.5524 | +7570381.62 ± 2223.06 | ±0.41 |
| ${}^{194}$Ta | 194 | 121 | 166.8878 | -890623.49 ± 381.4367 | 182051.6938 | 180692.7259 | +7520877.68 ± 2768.30 | ±0.41 |

### Tungsten (Z = 74)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{157}$W | 157 | 83 | -92.0621 | -1074908.42 ± 383.2397 | 147545.9408 | 146224.8844 | +9034415.86 ± 2732.85 | ±0.35 |
| ${}^{158}$W | 158 | 84 | -85.4339 | -1068837.79 ± 254.6149 | 148478.8779 | 147152.3758 | +9014479.75 ± 2038.30 | ±0.35 |
| ${}^{159}$W | 159 | 85 | -78.8175 | -1063011.02 ± 254.2265 | 149411.8270 | 148082.1290 | +8979463.15 ± 2025.51 | ±0.35 |
| ${}^{160}$W | 160 | 86 | -72.2129 | -1057182.62 ± 118.6273 | 150344.7878 | 149009.7275 | +8959550.87 ± 1005.37 | ±0.35 |
| ${}^{161}$W | 161 | 87 | -65.6197 | -1051585.37 ± 126.5663 | 151277.7601 | 149940.0433 | +8921677.57 ± 1335.68 | ±0.35 |
| ${}^{162}$W | 162 | 88 | -59.0380 | -1045991.96 ± 13.7560 | 152210.7437 | 150868.0456 | +8899818.03 ± 117.03 | ±0.36 |
| ${}^{163}$W | 163 | 89 | -52.4675 | -1040589.40 ± 45.1937 | 153143.7386 | 151798.6305 | +8861135.09 ± 384.89 | ±0.36 |
| ${}^{164}$W | 164 | 90 | -45.9080 | -1035204.50 ± 7.4200 | 154076.7446 | 152726.7975 | +8838967.16 ± 63.33 | ±0.36 |
| ${}^{165}$W | 165 | 91 | -39.3595 | -1029982.79 ± 19.6205 | 155009.7615 | 153657.6658 | +8799402.70 ± 167.61 | ±0.36 |
| ${}^{166}$W | 166 | 92 | -32.8217 | -1024792.92 ± 7.1474 | 155942.7891 | 154586.1337 | +8776048.23 ± 61.22 | ±0.36 |
| ${}^{167}$W | 167 | 93 | -26.2945 | -1019738.99 ± 14.0409 | 156875.8274 | 155517.4221 | +8734746.44 ± 120.26 | ±0.36 |
| ${}^{168}$W | 168 | 94 | -19.7778 | -1014726.79 ± 9.8700 | 157808.8761 | 156446.1165 | +8710728.06 ± 84.74 | ±0.37 |
| ${}^{169}$W | 169 | 95 | -13.2714 | -1009822.84 ± 11.4203 | 158741.9351 | 157377.5857 | +8669274.25 ± 98.08 | ±0.37 |
| ${}^{170}$W | 170 | 96 | -6.7752 | -1004976.21 ± 9.6892 | 159675.0043 | 158306.7068 | +8643332.55 ± 83.35 | ±0.37 |
| ${}^{171}$W | 171 | 97 | -0.2891 | -1000211.09 ± 20.4043 | 160608.0836 | 159238.4056 | +8601429.86 ± 175.49 | ±0.37 |
| ${}^{172}$W | 172 | 98 | 6.1872 | -995514.83 ± 20.2614 | 161541.1728 | 160167.8886 | +8574029.27 ± 174.47 | ±0.37 |
| ${}^{173}$W | 173 | 99 | 12.6536 | -990878.13 ± 20.1413 | 162474.2718 | 161099.7526 | +8532100.25 ± 173.46 | ±0.37 |
| ${}^{174}$W | 174 | 100 | 19.1104 | -986317.89 ± 20.0068 | 163407.3804 | 162029.7470 | +8502349.14 ± 172.47 | ±0.38 |
| ${}^{175}$W | 175 | 101 | 25.5576 | -981799.40 ± 19.9025 | 164340.4986 | 162961.8354 | +8460037.58 ± 171.48 | ±0.38 |
| ${}^{176}$W | 176 | 102 | 31.9955 | -977361.15 ± 19.7756 | 165273.6262 | 163892.3206 | +8428128.46 ± 170.51 | ±0.38 |
| ${}^{177}$W | 177 | 103 | 38.4240 | -972949.03 ± 19.6759 | 166206.7630 | 164824.7546 | +8384713.90 ± 169.54 | ±0.38 |
| ${}^{178}$W | 178 | 104 | 44.8434 | -968623.57 ± 10.6361 | 167139.9091 | 165755.5434 | +8351851.42 ± 91.69 | ±0.38 |
| ${}^{179}$W | 179 | 105 | 51.2538 | -964312.11 ± 10.1455 | 168073.0641 | 166688.1493 | +8308418.02 ± 87.42 | ±0.38 |
| ${}^{180}$W | 180 | 106 | 57.6552 | -960088.60 ± 0.9968 | 169006.2281 | 167619.3024 | +8274260.20 ± 8.59 | ±0.39 |
| ${}^{181}$W | 181 | 107 | 64.0478 | -955867.12 ± 0.9978 | 169939.4010 | 168552.1988 | +8230104.14 ± 8.59 | ±0.39 |
| ${}^{182}$W | 182 | 108 | 70.4317 | -951737.05 ± 0.5113 | 170872.5825 | 169483.6807 | +8194899.82 ± 4.39 | ±0.39 |
| ${}^{183}$W | 183 | 109 | 76.8070 | -947590.75 ± 0.5120 | 171805.7727 | 170417.0553 | +8148934.01 ± 4.36 | ±0.39 |
| ${}^{184}$W | 184 | 110 | 83.1738 | -943531.93 ± 0.4997 | 172738.9713 | 171349.2096 | +8110697.79 ± 4.31 | ±0.39 |
| ${}^{185}$W | 185 | 111 | 89.5322 | -939451.62 ± 0.5004 | 173672.1783 | 172283.0213 | +8063226.31 ± 4.29 | ±0.39 |
| ${}^{186}$W | 186 | 112 | 95.8823 | -935471.05 ± 0.8137 | 174605.3936 | 173215.3947 | +8024684.66 ± 7.00 | ±0.39 |
| ${}^{187}$W | 187 | 113 | 102.2242 | -931455.10 ± 0.8150 | 175538.6171 | 174149.4934 | +7976616.64 ± 6.96 | ±0.40 |
| ${}^{188}$W | 188 | 114 | 108.5581 | -927540.13 ± 2.0580 | 176471.8487 | 175082.2236 | +7936985.38 ± 17.64 | ±0.40 |
| ${}^{189}$W | 189 | 115 | 114.8839 | -923579.14 ± 125.7229 | 177405.0882 | 176016.5762 | +7888530.05 ± 1137.80 | ±0.40 |
| ${}^{190}$W | 190 | 116 | 121.2019 | -919735.19 ± 23.4413 | 178338.3357 | 176949.5109 | +7848706.62 ± 200.00 | ±0.40 |
| ${}^{191}$W | 191 | 117 | 127.5121 | -915828.28 ± 27.6747 | 179271.5909 | 177884.1976 | +7799418.35 ± 235.64 | ±0.40 |
| ${}^{192}$W | 192 | 118 | 133.8146 | -912045.57 ± 126.1989 | 180204.8539 | 178817.2483 | +7759909.07 ± 1119.98 | ±0.40 |
| ${}^{193}$W | 193 | 119 | 140.1094 | -908188.23 ± 126.4702 | 181138.1244 | 179752.1721 | +7710350.63 ± 1114.15 | ±0.40 |
| ${}^{194}$W | 194 | 120 | 146.3968 | -904466.05 ± 253.1966 | 182071.4025 | 180685.4463 | +7670546.71 ± 1660.02 | ±0.41 |
| ${}^{195}$W | 195 | 121 | 152.6767 | -900652.52 ± 253.7749 | 183004.6880 | 181620.6105 | +7620707.06 ± 1651.47 | ±0.41 |
| ${}^{196}$W | 196 | 122 | 158.9493 | -896980.97 ± 254.0650 | 183937.9808 | 182554.1045 | +7580636.43 ± 2189.00 | ±0.41 |
| ${}^{197}$W | 197 | 123 | 165.2146 | -893206.06 ± 254.6797 | 184871.2809 | 183489.4681 | +7530747.60 ± 2177.84 | ±0.41 |

### Rhenium (Z = 75)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{159}$Re | 159 | 84 | -100.7622 | -1081298.84 ± 256.5747 | 149432.9893 | 148092.7573 | +9049949.68 ± 2056.81 | ±0.35 |
| ${}^{160}$Re | 160 | 85 | -94.1183 | -1075318.77 ± 256.0819 | 150365.9109 | 149022.1779 | +9016999.95 ± 2012.73 | ±0.35 |
| ${}^{161}$Re | 161 | 86 | -87.4863 | -1069342.85 ± 118.8184 | 151298.8443 | 149949.7079 | +8997259.55 ± 999.70 | ±0.35 |
| ${}^{162}$Re | 162 | 87 | -80.8660 | -1063605.13 ± 127.4210 | 152231.7894 | 150879.5921 | +8962095.88 ± 1327.36 | ±0.35 |
| ${}^{163}$Re | 163 | 88 | -74.2573 | -1057880.04 ± 14.4457 | 153164.7461 | 151807.5367 | +8940329.74 ± 122.09 | ±0.35 |
| ${}^{164}$Re | 164 | 89 | -67.6598 | -1052348.35 ± 42.2025 | 154097.7141 | 152737.5606 | +8905167.34 ± 357.17 | ±0.36 |
| ${}^{165}$Re | 165 | 90 | -61.0737 | -1046844.58 ± 18.0978 | 155030.6933 | 153665.8678 | +8881774.40 ± 153.53 | ±0.36 |
| ${}^{166}$Re | 166 | 91 | -54.4985 | -1041506.86 ± 67.2091 | 155963.6836 | 154596.1839 | +8845624.11 ± 570.79 | ±0.36 |
| ${}^{167}$Re | 167 | 92 | -47.9343 | -1036200.23 ± 0.0000 | 156896.6848 | 155524.6812 | +8821774.27 ± 257.54 | ±0.36 |
| ${}^{168}$Re | 168 | 93 | -41.3808 | -1031041.02 ± 23.1250 | 157829.6967 | 156455.2145 | +8785147.94 ± 196.99 | ±0.36 |
| ${}^{169}$Re | 169 | 94 | -34.8379 | -1025925.20 ± 8.4639 | 158762.7193 | 157384.0943 | +8759620.97 ± 72.23 | ±0.36 |
| ${}^{170}$Re | 170 | 95 | -28.3055 | -1020930.59 ± 8.4475 | 159695.7523 | 158315.0936 | +8720954.18 ± 72.18 | ±0.37 |
| ${}^{171}$Re | 171 | 96 | -21.7834 | -1015984.69 ± 20.5034 | 160628.7957 | 159244.2415 | +8694532.35 ± 175.48 | ±0.37 |
| ${}^{172}$Re | 172 | 97 | -15.2716 | -1011137.71 ± 25.9413 | 161561.8492 | 160175.4190 | +8655698.89 ± 222.05 | ±0.37 |
| ${}^{173}$Re | 173 | 98 | -8.7697 | -1006349.28 ± 20.2282 | 162494.9128 | 161104.9261 | +8627834.97 ± 173.46 | ±0.37 |
| ${}^{174}$Re | 174 | 99 | -2.2778 | -1001639.42 ± 20.1125 | 163427.9863 | 162036.3009 | +8588725.79 ± 172.46 | ±0.37 |
| ${}^{175}$Re | 175 | 100 | 4.2043 | -996994.99 ± 19.9754 | 164361.0696 | 162966.1798 | +8559381.91 ± 171.48 | ±0.37 |
| ${}^{176}$Re | 176 | 101 | 10.6767 | -992411.37 ± 19.8650 | 165294.1626 | 163897.8994 | +8519103.81 ± 170.50 | ±0.38 |
| ${}^{177}$Re | 177 | 102 | 17.1397 | -987897.57 ± 19.7345 | 166227.2651 | 164828.1872 | +8488098.65 ± 169.54 | ±0.38 |
| ${}^{178}$Re | 178 | 103 | 23.5931 | -983427.96 ± 19.6295 | 167160.3770 | 165760.2970 | +8446413.58 ± 168.59 | ±0.38 |
| ${}^{179}$Re | 179 | 104 | 30.0373 | -979034.08 ± 17.1919 | 168093.4983 | 166690.8603 | +8414606.54 ± 147.81 | ±0.38 |
| ${}^{180}$Re | 180 | 105 | 36.4724 | -974671.95 ± 14.8500 | 169026.6287 | 167623.1013 | +8373114.13 ± 127.62 | ±0.38 |
| ${}^{181}$Re | 181 | 106 | 42.8983 | -970389.43 ± 8.6580 | 169959.7681 | 168553.9154 | +8340671.11 ± 74.45 | ±0.38 |
| ${}^{182}$Re | 182 | 107 | 49.3153 | -966123.78 ± 70.0495 | 170892.9166 | 169486.4807 | +8298218.32 ± 601.72 | ±0.39 |
| ${}^{183}$Re | 183 | 108 | 55.7235 | -961942.32 ± 5.4868 | 171826.0738 | 170417.6113 | +8264770.76 ± 47.14 | ±0.39 |
| ${}^{184}$Re | 184 | 109 | 62.1229 | -957758.66 ± 2.9026 | 172759.2398 | 171350.6953 | +8220244.01 ± 24.95 | ±0.39 |
| ${}^{185}$Re | 185 | 110 | 68.5137 | -953654.85 ± 0.5506 | 173692.4144 | 172282.5901 | +8183207.89 ± 4.75 | ±0.39 |
| ${}^{186}$Re | 186 | 111 | 74.8961 | -949548.52 ± 0.5513 | 174625.5975 | 173215.9760 | +8137941.82 ± 4.73 | ±0.39 |
| ${}^{187}$Re | 187 | 112 | 81.2700 | -945525.03 ± 0.4888 | 175558.7890 | 174148.1808 | +8100045.45 ± 4.23 | ±0.39 |
| ${}^{188}$Re | 188 | 113 | 87.6355 | -941488.48 ± 0.4895 | 176491.9889 | 175081.8746 | +8054027.52 ± 4.21 | ±0.39 |
| ${}^{189}$Re | 189 | 114 | 93.9929 | -937537.18 ± 5.4385 | 177425.1969 | 176014.4065 | +8015198.35 ± 46.53 | ±0.40 |
| ${}^{190}$Re | 190 | 115 | 100.3422 | -933568.32 ± 3.2202 | 178358.4130 | 176948.2967 | +7969086.79 ± 27.52 | ±0.40 |
| ${}^{191}$Re | 191 | 116 | 106.6835 | -929688.41 ± 6.7599 | 179291.6372 | 177881.0234 | +7930097.00 ± 57.70 | ±0.40 |
| ${}^{192}$Re | 192 | 117 | 113.0169 | -925774.06 ± 46.4929 | 180224.8692 | 178815.2791 | +7882940.18 ± 395.90 | ±0.40 |
| ${}^{193}$Re | 193 | 118 | 119.3424 | -921963.75 ± 25.5807 | 181158.1091 | 179748.1304 | +7844191.39 ± 217.65 | ±0.40 |
| ${}^{194}$Re | 194 | 119 | 125.6602 | -918101.77 ± 126.4382 | 182091.3567 | 180682.5959 | +7796881.41 ± 1108.41 | ±0.40 |
| ${}^{195}$Re | 195 | 120 | 131.9704 | -914343.59 ± 253.1325 | 183024.6120 | 181615.7900 | +7757155.56 ± 1651.51 | ±0.40 |
| ${}^{196}$Re | 196 | 121 | 138.2730 | -910540.88 ± 253.6140 | 183957.8748 | 182550.4847 | +7709593.37 ± 1643.06 | ±0.40 |
| ${}^{197}$Re | 197 | 122 | 144.5682 | -906836.52 ± 253.9038 | 184891.1450 | 183483.9881 | +7669099.27 ± 1634.70 | ±0.41 |
| ${}^{198}$Re | 198 | 123 | 150.8560 | -903078.61 ± 254.4206 | 185824.4226 | 184418.8421 | +7621675.32 ± 2166.87 | ±0.41 |
| ${}^{199}$Re | 199 | 124 | 157.1365 | -899410.09 ± 254.7771 | 186757.7075 | 185352.5969 | +7580744.10 ± 2155.95 | ±0.41 |

### Osmium (Z = 76)

_43 of 43 isotopes with a framework prediction; 43 of 43 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{161}$Os | 161 | 85 | -109.6138 | -1087679.50 ± 257.5660 | 151320.1895 | 149960.3546 | +9067962.90 ± 2664.78 | ±0.35 |
| ${}^{162}$Os | 162 | 86 | -102.9545 | -1081539.82 ± 256.6076 | 152253.0955 | 150887.5452 | +9050119.84 ± 1987.85 | ±0.35 |
| ${}^{163}$Os | 163 | 87 | -96.3069 | -1075680.79 ± 256.1804 | 153186.0134 | 151817.2024 | +9016178.84 ± 1975.67 | ±0.35 |
| ${}^{164}$Os | 164 | 88 | -89.6710 | -1069801.25 ± 116.6812 | 154118.9430 | 152744.6083 | +8997598.63 ± 981.39 | ±0.35 |
| ${}^{165}$Os | 165 | 89 | -83.0467 | -1064173.57 ± 127.5022 | 155051.8840 | 153674.7805 | +8961155.34 ± 1303.21 | ±0.35 |
| ${}^{166}$Os | 166 | 90 | -76.4337 | -1058533.46 ± 13.7548 | 155984.8365 | 154602.5897 | +8940644.32 ± 116.21 | ±0.36 |
| ${}^{167}$Os | 167 | 91 | -69.8319 | -1053106.10 ± 61.5193 | 156917.8001 | 155533.0165 | +8903470.48 ± 520.09 | ±0.36 |
| ${}^{168}$Os | 168 | 92 | -63.2411 | -1047674.54 ± 7.4595 | 157850.7748 | 156461.0144 | +8882470.36 ± 63.29 | ±0.36 |
| ${}^{169}$Os | 169 | 93 | -56.6613 | -1042432.83 ± 19.4272 | 158783.7603 | 157391.7805 | +8844043.66 ± 164.81 | ±0.36 |
| ${}^{170}$Os | 170 | 94 | -50.0922 | -1037199.25 ± 7.2464 | 159716.7566 | 158320.0719 | +8821905.44 ± 61.64 | ±0.36 |
| ${}^{171}$Os | 171 | 95 | -43.5337 | -1032127.37 ± 13.4651 | 160649.7636 | 159251.1945 | +8782157.52 ± 114.58 | ±0.36 |
| ${}^{172}$Os | 172 | 96 | -36.9857 | -1027074.86 ± 9.3425 | 161582.7810 | 160179.7422 | +8759152.37 ± 79.69 | ±0.37 |
| ${}^{173}$Os | 173 | 97 | -30.4480 | -1022154.97 ± 10.8887 | 162515.8087 | 161111.0417 | +8719247.19 ± 92.85 | ±0.37 |
| ${}^{174}$Os | 174 | 98 | -23.9205 | -1017271.76 ± 7.4000 | 163448.8466 | 162039.9787 | +8694570.03 ± 63.28 | ±0.37 |
| ${}^{175}$Os | 175 | 99 | -17.4030 | -1012492.04 ± 8.4540 | 164381.8946 | 162971.3628 | +8655089.85 ± 72.25 | ±0.37 |
| ${}^{176}$Os | 176 | 100 | -10.8955 | -1007764.60 ± 7.8015 | 165314.9525 | 163900.8311 | +8627908.72 ± 66.80 | ±0.37 |
| ${}^{177}$Os | 177 | 101 | -4.3978 | -1003116.50 ± 10.3607 | 166248.0202 | 164832.4999 | +8587628.47 ± 88.65 | ±0.37 |
| ${}^{178}$Os | 178 | 102 | 2.0903 | -998528.78 ± 9.5967 | 167181.0976 | 165762.4062 | +8558583.14 ± 82.24 | ±0.38 |
| ${}^{179}$Os | 179 | 103 | 8.5688 | -994000.83 ± 10.8528 | 168114.1845 | 166694.4244 | +8517141.79 ± 93.01 | ±0.38 |
| ${}^{180}$Os | 180 | 104 | 15.0379 | -989540.59 ± 10.9297 | 169047.2808 | 167624.5825 | +8487408.80 ± 93.79 | ±0.38 |
| ${}^{181}$Os | 181 | 105 | 21.4976 | -985122.76 ± 17.5363 | 169980.3865 | 168556.8828 | +8445242.09 ± 150.32 | ±0.38 |
| ${}^{182}$Os | 182 | 106 | 27.9482 | -980780.14 ± 14.9567 | 170913.5013 | 169487.3178 | +8414691.96 ± 128.30 | ±0.38 |
| ${}^{183}$Os | 183 | 107 | 34.3897 | -976465.68 ± 34.0638 | 171846.6253 | 170419.7572 | +8372667.98 ± 292.03 | ±0.38 |
| ${}^{184}$Os | 184 | 108 | 40.8222 | -972228.21 ± 0.5633 | 172779.7582 | 171350.6625 | +8340181.57 ± 4.84 | ±0.38 |
| ${}^{185}$Os | 185 | 109 | 47.2459 | -968002.32 ± 0.5638 | 173712.8999 | 172283.6033 | +8296184.86 ± 4.83 | ±0.39 |
| ${}^{186}$Os | 186 | 110 | 53.6608 | -963860.06 ± 0.5136 | 174646.0504 | 173214.9033 | +8262263.24 ± 4.39 | ±0.39 |
| ${}^{187}$Os | 187 | 111 | 60.0671 | -959716.15 ± 0.4891 | 175579.2095 | 174148.1784 | +8217318.97 ± 4.23 | ±0.39 |
| ${}^{188}$Os | 188 | 112 | 66.4649 | -955663.07 ± 0.4891 | 176512.3772 | 175079.7542 | +8182687.79 ± 4.19 | ±0.39 |
| ${}^{189}$Os | 189 | 113 | 72.8542 | -951592.11 ± 0.4395 | 177445.5532 | 176013.3988 | +8136621.73 ± 3.78 | ±0.39 |
| ${}^{190}$Os | 190 | 114 | 79.2353 | -947623.44 ± 0.4270 | 178378.7377 | 176945.1719 | +8101751.28 ± 3.67 | ±0.39 |
| ${}^{191}$Os | 191 | 115 | 85.6080 | -943625.46 ± 0.4402 | 179311.9303 | 177878.9786 | +8055767.63 ± 3.70 | ±0.39 |
| ${}^{192}$Os | 192 | 116 | 91.9727 | -939734.17 ± 1.5223 | 180245.1310 | 178810.9856 | +8020454.86 ± 12.94 | ±0.40 |
| ${}^{193}$Os | 193 | 117 | 98.3293 | -935803.81 ± 1.5120 | 181178.3398 | 179744.9676 | +7974477.65 ± 12.90 | ±0.40 |
| ${}^{194}$Os | 194 | 118 | 104.6780 | -931974.80 ± 1.5633 | 182111.5566 | 180677.4209 | +7937547.59 ± 13.30 | ±0.40 |
| ${}^{195}$Os | 195 | 119 | 111.0189 | -928094.73 ± 36.1972 | 183044.7811 | 181611.8386 | +7890138.25 ± 307.74 | ±0.40 |
| ${}^{196}$Os | 196 | 120 | 117.3520 | -924327.96 ± 25.8334 | 183978.0135 | 182544.5672 | +7852582.44 ± 219.42 | ±0.40 |
| ${}^{197}$Os | 197 | 121 | 123.6774 | -920500.93 ± 126.6304 | 184911.2535 | 183479.2589 | +7804667.27 ± 1091.52 | ±0.40 |
| ${}^{198}$Os | 198 | 122 | 129.9953 | -916788.11 ± 126.7427 | 185844.5010 | 184412.2322 | +7766669.22 ± 1086.00 | ±0.40 |
| ${}^{199}$Os | 199 | 123 | 136.3057 | -913010.78 ± 127.0003 | 186777.7561 | 185347.0564 | +7719030.90 ± 1080.52 | ±0.40 |
| ${}^{200}$Os | 200 | 124 | 142.6086 | -909362.75 ± 127.1133 | 187711.0185 | 186280.2710 | +7680617.58 ± 1610.16 | ±0.41 |
| ${}^{201}$Os | 201 | 125 | 148.9043 | -905616.32 ± 127.4048 | 188644.2883 | 187215.4752 | +7631917.36 ± 1602.12 | ±0.41 |
| ${}^{202}$Os | 202 | 126 | 155.1927 | -901992.48 ± 255.1346 | 189577.5652 | 188149.2785 | +7591242.22 ± 2123.90 | ±0.41 |
| ${}^{203}$Os | 203 | 127 | 161.4740 | -898203.41 ± 255.9509 | 190510.8494 | 189086.0327 | +7535282.29 ± 2113.38 | ±0.41 |

### Iridium (Z = 77)

_43 of 43 isotopes with a framework prediction; 43 of 43 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{163}$Ir | 163 | 86 | -118.6164 | -1094092.09 ± 258.5984 | 153207.5406 | 151828.2285 | +9084688.40 ± 2631.99 | ±0.35 |
| ${}^{164}$Ir | 164 | 87 | -111.9416 | -1088073.64 ± 258.0645 | 154140.4312 | 152757.5494 | +9052788.56 ± 2067.17 | ±0.35 |
| ${}^{165}$Ir | 165 | 88 | -105.2786 | -1082054.01 ± 128.6008 | 155073.3336 | 153684.9319 | +9034078.30 ± 1030.38 | ±0.35 |
| ${}^{166}$Ir | 166 | 89 | -98.6272 | -1076279.35 ± 128.3862 | 156006.2476 | 154614.7158 | +8999996.41 ± 1295.29 | ±0.35 |
| ${}^{167}$Ir | 167 | 90 | -91.9873 | -1070502.34 ± 14.0666 | 156939.1732 | 155542.4429 | +8979737.65 ± 117.94 | ±0.35 |
| ${}^{168}$Ir | 168 | 91 | -85.3588 | -1064940.95 ± 42.0126 | 157872.1101 | 156472.3432 | +8945778.43 ± 352.88 | ±0.35 |
| ${}^{169}$Ir | 169 | 92 | -78.7415 | -1059386.96 ± 17.5767 | 158805.0582 | 157400.4101 | +8924043.38 ± 148.07 | ±0.36 |
| ${}^{170}$Ir | 170 | 93 | -72.1352 | -1054033.46 ± 127.3399 | 159738.0173 | 158330.8155 | +8887731.61 ± 641.27 | ±0.36 |
| ${}^{171}$Ir | 171 | 94 | -65.5398 | -1048679.02 ± 28.5642 | 160670.9874 | 159259.0797 | +8865476.64 ± 241.53 | ±0.36 |
| ${}^{172}$Ir | 172 | 95 | -58.9552 | -1043496.33 ± 23.9078 | 161603.9681 | 160189.6065 | +8829297.30 ± 202.27 | ±0.36 |
| ${}^{173}$Ir | 173 | 96 | -52.3811 | -1038336.08 ± 7.7107 | 162536.9595 | 161118.2115 | +8805634.08 ± 65.42 | ±0.36 |
| ${}^{174}$Ir | 174 | 97 | -45.8175 | -1033322.94 ± 8.1625 | 163469.9613 | 162049.1881 | +8767543.03 ± 69.24 | ±0.37 |
| ${}^{175}$Ir | 175 | 98 | -39.2643 | -1028336.67 ± 8.9418 | 164402.9735 | 162978.0736 | +8742893.05 ± 75.99 | ±0.37 |
| ${}^{176}$Ir | 176 | 99 | -32.7212 | -1023469.64 ± 5.7943 | 165335.9959 | 163909.0803 | +8705530.73 ± 49.32 | ±0.37 |
| ${}^{177}$Ir | 177 | 100 | -26.1882 | -1018646.86 ± 14.0649 | 166269.0283 | 164838.4089 | +8678919.94 ± 119.87 | ±0.37 |
| ${}^{178}$Ir | 178 | 101 | -19.6651 | -1013920.17 ± 13.3181 | 167202.0706 | 165769.6961 | +8640749.95 ± 113.53 | ±0.37 |
| ${}^{179}$Ir | 179 | 102 | -13.1519 | -1009244.91 ± 6.8701 | 168135.1228 | 166699.3628 | +8612870.09 ± 58.61 | ±0.37 |
| ${}^{180}$Ir | 180 | 103 | -6.6483 | -1004647.29 ± 15.1743 | 169068.1846 | 167630.9611 | +8573735.38 ± 129.48 | ±0.37 |
| ${}^{181}$Ir | 181 | 104 | -0.1543 | -1000107.12 ± 3.6448 | 170001.2560 | 168560.9697 | +8544601.41 ± 31.12 | ±0.38 |
| ${}^{182}$Ir | 182 | 105 | 6.3303 | -995627.60 ± 14.4816 | 170934.3369 | 169492.8752 | +8504556.18 ± 123.70 | ±0.38 |
| ${}^{183}$Ir | 183 | 106 | 12.8056 | -991211.06 ± 16.9308 | 171867.4270 | 170423.2188 | +8474245.44 ± 144.77 | ±0.38 |
| ${}^{184}$Ir | 184 | 107 | 19.2717 | -986840.73 ± 19.0848 | 172800.5264 | 171355.3042 | +8434067.23 ± 163.08 | ±0.38 |
| ${}^{185}$Ir | 185 | 108 | 25.7286 | -982536.60 ± 18.9735 | 173733.6348 | 172286.0736 | +8402079.00 ± 162.20 | ±0.38 |
| ${}^{186}$Ir | 186 | 109 | 32.1766 | -978261.92 ± 11.1585 | 174666.7523 | 173218.7309 | +8359496.15 ± 95.40 | ±0.38 |
| ${}^{187}$Ir | 187 | 110 | 38.6158 | -974059.79 ± 18.7673 | 175599.8785 | 174149.8480 | +8326338.18 ± 160.46 | ±0.39 |
| ${}^{188}$Ir | 188 | 111 | 45.0461 | -969879.12 ± 6.2980 | 176533.0136 | 175082.5465 | +8284475.43 ± 53.82 | ±0.39 |
| ${}^{189}$Ir | 189 | 112 | 51.4679 | -965772.25 ± 8.3584 | 177466.1573 | 176013.9360 | +8250604.39 ± 71.44 | ±0.39 |
| ${}^{190}$Ir | 190 | 113 | 57.8810 | -961669.80 ± 0.9059 | 178399.3096 | 176947.1261 | +8206877.93 ± 7.74 | ±0.39 |
| ${}^{191}$Ir | 191 | 114 | 64.2857 | -957653.53 ± 0.8681 | 179332.4703 | 177878.6650 | +8173016.54 ± 7.36 | ±0.39 |
| ${}^{192}$Ir | 192 | 115 | 70.6821 | -953629.42 ± 0.8565 | 180265.6393 | 178812.0323 | +8129246.10 ± 7.35 | ±0.39 |
| ${}^{193}$Ir | 193 | 116 | 77.0703 | -949695.01 ± 0.8692 | 181198.8166 | 179743.8257 | +8094803.10 ± 7.38 | ±0.39 |
| ${}^{194}$Ir | 194 | 117 | 83.4502 | -945745.54 ± 0.8703 | 182132.0020 | 180677.3243 | +8051246.55 ± 7.37 | ±0.40 |
| ${}^{195}$Ir | 195 | 118 | 89.8222 | -941876.16 ± 0.8581 | 183065.1955 | 181609.6579 | +8014648.73 ± 7.34 | ±0.40 |
| ${}^{196}$Ir | 196 | 119 | 96.1861 | -937991.36 ± 24.7658 | 183998.3970 | 182543.4088 | +7970642.02 ± 210.44 | ±0.40 |
| ${}^{197}$Ir | 197 | 120 | 102.5422 | -934186.50 ± 12.9093 | 184931.6063 | 183476.0743 | +7933088.75 ± 109.60 | ±0.40 |
| ${}^{198}$Ir | 198 | 121 | 108.8906 | -930359.32 ± 126.6304 | 185864.8234 | 184410.1224 | +7888401.11 ± 1086.01 | ±0.40 |
| ${}^{199}$Ir | 199 | 122 | 115.2312 | -926620.68 ± 26.1430 | 186798.0482 | 185342.9281 | +7850960.75 ± 221.50 | ±0.40 |
| ${}^{200}$Ir | 200 | 123 | 121.5643 | -922845.73 ± 126.9358 | 187731.2805 | 186277.2511 | +7805727.53 ± 1050.12 | ±0.40 |
| ${}^{201}$Ir | 201 | 124 | 127.8898 | -919152.77 ± 127.0648 | 188664.5204 | 187210.4750 | +7766902.28 ± 1069.77 | ±0.40 |
| ${}^{202}$Ir | 202 | 125 | 134.2079 | -915417.49 ± 127.3074 | 189597.7677 | 188145.1687 | +7720628.70 ± 1594.20 | ±0.41 |
| ${}^{203}$Ir | 203 | 126 | 140.5187 | -911764.14 ± 254.9395 | 190531.0224 | 189078.9329 | +7679805.81 ± 2113.46 | ±0.41 |
| ${}^{204}$Ir | 204 | 127 | 146.8222 | -907999.91 ± 255.6564 | 191464.2843 | 190015.2270 | +7626006.24 ± 2103.05 | ±0.41 |
| ${}^{205}$Ir | 205 | 128 | 153.1185 | -904302.41 ± 256.2460 | 192397.5534 | 190950.6911 | +7577151.23 ± 2619.59 | ±0.41 |

### Platinum (Z = 78)

_44 of 44 isotopes with a framework prediction; 44 of 44 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{165}$Pt | 165 | 87 | -127.7693 | -1100526.99 ± 259.6391 | 155095.0420 | 153696.2085 | +9101287.87 ± 2600.01 | ±0.35 |
| ${}^{166}$Pt | 166 | 88 | -121.0791 | -1094322.00 ± 258.6318 | 156027.9172 | 154623.2389 | +9084522.19 ± 1939.82 | ±0.35 |
| ${}^{167}$Pt | 167 | 89 | -114.4006 | -1088437.10 ± 258.1978 | 156960.8042 | 155552.7620 | +9051862.26 ± 1970.15 | ±0.35 |
| ${}^{168}$Pt | 168 | 90 | -107.7339 | -1082493.46 ± 114.8113 | 157893.7028 | 156479.9993 | +9034403.51 ± 958.16 | ±0.35 |
| ${}^{169}$Pt | 169 | 91 | -101.0786 | -1076836.84 ± 128.4687 | 158826.6129 | 157410.0392 | +8999259.04 ± 1272.29 | ±0.35 |
| ${}^{170}$Pt | 170 | 92 | -94.4346 | -1071142.52 ± 13.7419 | 159759.5344 | 158337.6984 | +8979768.95 ± 115.24 | ±0.35 |
| ${}^{171}$Pt | 171 | 93 | -87.8018 | -1065688.50 ± 60.5634 | 160692.4670 | 159268.0252 | +8943677.43 ± 508.27 | ±0.36 |
| ${}^{172}$Pt | 172 | 94 | -81.1800 | -1060206.93 ± 7.6921 | 161625.4107 | 160195.8792 | +8923647.16 ± 64.77 | ±0.36 |
| ${}^{173}$Pt | 173 | 95 | -74.5692 | -1054941.29 ± 46.7409 | 162558.3652 | 161126.5432 | +8886320.06 ± 393.67 | ±0.36 |
| ${}^{174}$Pt | 174 | 96 | -67.9690 | -1049659.41 ± 7.5514 | 163491.3305 | 162054.6564 | +8865367.39 ± 63.79 | ±0.36 |
| ${}^{175}$Pt | 175 | 97 | -61.3795 | -1044569.41 ± 13.5205 | 164424.3064 | 162985.7595 | +8826212.38 ± 114.20 | ±0.36 |
| ${}^{176}$Pt | 176 | 98 | -54.8004 | -1039468.41 ± 9.1520 | 165357.2927 | 163914.0283 | +8805008.48 ± 77.55 | ±0.36 |
| ${}^{177}$Pt | 177 | 99 | -48.2317 | -1034525.90 ± 10.7317 | 166290.2894 | 164845.0859 | +8767040.24 ± 90.92 | ±0.37 |
| ${}^{178}$Pt | 178 | 100 | -41.6731 | -1029604.35 ± 7.1950 | 167223.2963 | 165773.9530 | +8742889.30 ± 61.12 | ±0.37 |
| ${}^{179}$Pt | 179 | 101 | -35.1246 | -1024805.34 ± 5.6380 | 168156.3132 | 166705.1764 | +8704809.45 ± 47.85 | ±0.37 |
| ${}^{180}$Pt | 180 | 102 | -28.5861 | -1020042.92 ± 7.0423 | 169089.3401 | 167634.5088 | +8678590.84 ± 59.96 | ±0.37 |
| ${}^{181}$Pt | 181 | 103 | -22.0574 | -1015378.83 ± 9.5405 | 170022.3768 | 168566.0513 | +8639494.74 ± 81.20 | ±0.37 |
| ${}^{182}$Pt | 182 | 104 | -15.5383 | -1010759.66 ± 9.0614 | 170955.4232 | 169495.7585 | +8611806.66 ± 77.25 | ±0.37 |
| ${}^{183}$Pt | 183 | 105 | -9.0288 | -1006219.04 ± 9.7941 | 171888.4791 | 170427.6478 | +8571562.94 ± 83.41 | ±0.38 |
| ${}^{184}$Pt | 184 | 106 | -2.5288 | -1001730.34 ± 10.0849 | 172821.5445 | 171357.5826 | +8543315.42 ± 86.04 | ±0.38 |
| ${}^{185}$Pt | 185 | 107 | 3.9619 | -997302.71 ± 17.5824 | 173754.6192 | 172289.7210 | +8502527.80 ± 149.93 | ±0.38 |
| ${}^{186}$Pt | 186 | 108 | 10.4434 | -992934.58 ± 14.7103 | 174687.7031 | 173220.0388 | +8472831.89 ± 125.53 | ±0.38 |
| ${}^{187}$Pt | 187 | 109 | 16.9158 | -988608.86 ± 16.2067 | 175620.7961 | 174152.7120 | +8429866.46 ± 138.19 | ±0.38 |
| ${}^{188}$Pt | 188 | 110 | 23.3792 | -984353.40 ± 3.5481 | 176553.8982 | 175083.0705 | +8400741.56 ± 30.29 | ±0.38 |
| ${}^{189}$Pt | 189 | 111 | 29.8338 | -980123.09 ± 6.7243 | 177487.0091 | 176015.9162 | +8357726.34 ± 57.32 | ±0.38 |
| ${}^{190}$Pt | 190 | 112 | 36.2795 | -975971.19 ± 0.4404 | 178420.1287 | 176946.5732 | +8327686.15 ± 3.71 | ±0.39 |
| ${}^{191}$Pt | 191 | 113 | 42.7166 | -971828.35 ± 2.7208 | 179353.2571 | 177879.6755 | +8284148.24 ± 23.20 | ±0.39 |
| ${}^{192}$Pt | 192 | 114 | 49.1451 | -967772.82 ± 1.6871 | 180286.3940 | 178810.5794 | +8253508.26 ± 14.37 | ±0.39 |
| ${}^{193}$Pt | 193 | 115 | 55.5652 | -963711.86 ± 0.8823 | 181219.5394 | 179743.8823 | +8209776.02 ± 7.56 | ±0.39 |
| ${}^{194}$Pt | 194 | 116 | 61.9768 | -959744.13 ± 0.3276 | 182152.6931 | 180675.0960 | +8178200.01 ± 2.74 | ±0.39 |
| ${}^{195}$Pt | 195 | 117 | 68.3803 | -955760.34 ± 0.3280 | 183085.8551 | 181608.5563 | +8134521.73 ± 2.77 | ±0.39 |
| ${}^{196}$Pt | 196 | 118 | 74.7755 | -951869.51 ± 0.3280 | 184019.0253 | 182540.1998 | +8101368.78 ± 2.79 | ±0.39 |
| ${}^{197}$Pt | 197 | 119 | 81.1627 | -947954.16 ± 0.3411 | 184952.2035 | 183473.9187 | +8057193.44 ± 2.92 | ±0.40 |
| ${}^{198}$Pt | 198 | 120 | 87.5419 | -944134.15 ± 1.3394 | 185885.3897 | 184405.9285 | +8022850.62 ± 11.39 | ±0.40 |
| ${}^{199}$Pt | 199 | 121 | 93.9132 | -940279.98 ± 1.3793 | 186818.5838 | 185339.9379 | +7978020.96 ± 11.64 | ±0.40 |
| ${}^{200}$Pt | 200 | 122 | 100.2767 | -936527.29 ± 12.7355 | 187751.7858 | 186272.2216 | +7943021.15 ± 107.96 | ±0.40 |
| ${}^{201}$Pt | 201 | 123 | 106.6325 | -932726.20 ± 31.6137 | 188684.9954 | 187206.5741 | +7897272.02 ± 267.64 | ±0.40 |
| ${}^{202}$Pt | 202 | 124 | 112.9807 | -929035.59 ± 15.7964 | 189618.2126 | 188139.1168 | +7861713.32 ± 133.68 | ±0.40 |
| ${}^{203}$Pt | 203 | 125 | 119.3213 | -925284.12 ± 127.1133 | 190551.4374 | 189073.7929 | +7815173.47 ± 1059.22 | ±0.40 |
| ${}^{204}$Pt | 204 | 126 | 125.6545 | -921624.43 ± 127.2427 | 191484.6696 | 190007.1770 | +7775983.18 ± 1054.02 | ±0.40 |
| ${}^{205}$Pt | 205 | 127 | 131.9804 | -917839.89 ± 127.6161 | 192417.9092 | 190943.4711 | +7721856.67 ± 1570.84 | ±0.41 |
| ${}^{206}$Pt | 206 | 128 | 138.2989 | -914149.12 ± 127.8772 | 193351.1561 | 191878.5449 | +7674704.64 ± 1563.18 | ±0.41 |
| ${}^{207}$Pt | 207 | 129 | 144.6102 | -910401.41 ± 256.5089 | 194284.4102 | 192815.1399 | +7620098.09 ± 2072.51 | ±0.41 |
| ${}^{208}$Pt | 208 | 130 | 150.9145 | -906741.61 ± 257.0694 | 195217.6714 | 193750.2734 | +7573656.60 ± 2062.51 | ±0.41 |

### Gold (Z = 79)

_43 of 43 isotopes with a framework prediction; 43 of 43 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{168}$Au | 168 | 89 | -130.3662 | -1100935.16 ± 260.1457 | 157915.5528 | 156493.5394 | +9086723.21 ± 2553.53 | ±0.35 |
| ${}^{169}$Au | 169 | 90 | -123.6725 | -1094840.56 ± 259.2017 | 158848.4245 | 157420.7151 | +9069387.32 ± 1893.51 | ±0.35 |
| ${}^{170}$Au | 170 | 91 | -116.9903 | -1089026.96 ± 129.3661 | 159781.3078 | 158350.2940 | +9037013.65 ± 1270.62 | ±0.35 |
| ${}^{171}$Au | 171 | 92 | -110.3197 | -1083200.32 ± 15.6175 | 160714.2025 | 159277.9294 | +9017401.89 ± 130.04 | ±0.35 |
| ${}^{172}$Au | 172 | 93 | -103.6603 | -1077602.87 ± 42.0414 | 161647.1086 | 160207.6678 | +8984843.21 ± 350.53 | ±0.35 |
| ${}^{173}$Au | 173 | 94 | -97.0121 | -1072001.39 ± 16.9101 | 162580.0258 | 161135.6479 | +8963739.16 ± 141.39 | ±0.36 |
| ${}^{174}$Au | 174 | 95 | -90.3750 | -1066614.89 ± 128.2545 | 163512.9541 | 162065.9159 | +8928701.37 ± 626.49 | ±0.36 |
| ${}^{175}$Au | 175 | 96 | -83.7487 | -1061216.26 ± 28.1928 | 164445.8932 | 162994.0645 | +8907249.36 ± 236.59 | ±0.36 |
| ${}^{176}$Au | 176 | 97 | -77.1331 | -1056004.46 ± 24.0883 | 165378.8431 | 163924.4413 | +8872391.54 ± 202.44 | ±0.36 |
| ${}^{177}$Au | 177 | 98 | -70.5282 | -1050799.49 ± 7.1776 | 166311.8036 | 164852.9106 | +8849664.57 ± 60.46 | ±0.36 |
| ${}^{178}$Au | 178 | 99 | -63.9337 | -1045758.68 ± 7.3381 | 167244.7745 | 165783.6474 | +8813457.20 ± 61.81 | ±0.36 |
| ${}^{179}$Au | 179 | 100 | -57.3495 | -1040732.66 ± 8.3019 | 168177.7558 | 166712.4560 | +8789383.89 ± 70.15 | ±0.37 |
| ${}^{180}$Au | 180 | 101 | -50.7755 | -1035841.79 ± 3.3544 | 169110.7472 | 167643.3130 | +8753311.85 ± 28.38 | ±0.37 |
| ${}^{181}$Au | 181 | 102 | -44.2116 | -1030982.78 ± 14.0033 | 170043.7487 | 168572.5616 | +8727322.46 ± 118.50 | ±0.37 |
| ${}^{182}$Au | 182 | 103 | -37.6577 | -1026233.53 ± 13.0717 | 170976.7602 | 169503.6229 | +8690889.72 ± 110.69 | ±0.37 |
| ${}^{183}$Au | 183 | 104 | -31.1135 | -1021525.33 ± 6.5202 | 171909.7815 | 170433.2295 | +8663521.64 ± 55.29 | ±0.37 |
| ${}^{184}$Au | 184 | 105 | -24.5791 | -1016908.68 ± 15.3287 | 172842.8124 | 171364.5964 | +8626146.18 ± 129.98 | ±0.37 |
| ${}^{185}$Au | 185 | 106 | -18.0542 | -1012338.43 ± 1.7827 | 173775.8530 | 172294.5510 | +8597497.24 ± 15.14 | ±0.38 |
| ${}^{186}$Au | 186 | 107 | -11.5387 | -1007843.21 ± 14.2486 | 174708.9030 | 173226.1884 | +8559413.18 ± 121.04 | ±0.38 |
| ${}^{187}$Au | 187 | 108 | -5.0326 | -1003399.15 ± 15.1943 | 175641.9623 | 174156.3686 | +8530228.80 ± 129.18 | ±0.38 |
| ${}^{188}$Au | 188 | 109 | 1.4642 | -999015.96 ± 1.8194 | 176575.0308 | 175088.5202 | +8490052.08 ± 15.43 | ±0.38 |
| ${}^{189}$Au | 189 | 110 | 7.9520 | -994688.96 ± 13.4183 | 177508.1085 | 176018.8036 | +8461055.48 ± 114.09 | ±0.38 |
| ${}^{190}$Au | 190 | 111 | 14.4307 | -990408.79 ± 2.2857 | 178441.1952 | 176951.0462 | +8421250.09 ± 19.48 | ±0.38 |
| ${}^{191}$Au | 191 | 112 | 20.9006 | -986191.60 ± 3.2557 | 179374.2907 | 177881.5759 | +8391621.44 ± 27.69 | ±0.38 |
| ${}^{192}$Au | 192 | 113 | 27.3617 | -982006.72 ± 10.4039 | 180307.3951 | 178814.0957 | +8351127.82 ± 88.51 | ±0.39 |
| ${}^{193}$Au | 193 | 114 | 33.8140 | -977890.13 ± 5.6662 | 181240.5081 | 179744.9572 | +8320405.62 ± 48.25 | ±0.39 |
| ${}^{194}$Au | 194 | 115 | 40.2578 | -973794.60 ± 1.3765 | 182173.6298 | 180677.6442 | +8279859.95 ± 11.72 | ±0.39 |
| ${}^{195}$Au | 195 | 116 | 46.6932 | -969771.41 ± 0.7196 | 183106.7599 | 181608.7832 | +8248371.44 ± 6.16 | ±0.39 |
| ${}^{196}$Au | 196 | 117 | 53.1201 | -965757.95 ± 1.9078 | 184039.8983 | 182541.7056 | +8207399.68 ± 16.22 | ±0.39 |
| ${}^{197}$Au | 197 | 118 | 59.5388 | -961819.06 ± 0.3537 | 184973.0451 | 183473.1987 | +8174744.03 ± 2.95 | ±0.39 |
| ${}^{198}$Au | 198 | 119 | 65.9492 | -957884.05 ± 0.3414 | 185906.2001 | 184406.2517 | +8133934.27 ± 2.92 | ±0.39 |
| ${}^{199}$Au | 199 | 120 | 72.3516 | -954018.13 ± 0.3415 | 186839.3631 | 185338.2329 | +8099409.46 ± 2.92 | ±0.39 |
| ${}^{200}$Au | 200 | 121 | 78.7460 | -950151.27 ± 16.9146 | 187772.5342 | 186271.5807 | +8057877.22 ± 143.43 | ±0.40 |
| ${}^{201}$Au | 201 | 122 | 85.1324 | -946354.02 ± 2.0266 | 188705.7131 | 187203.9141 | +8022262.80 ± 17.19 | ±0.40 |
| ${}^{202}$Au | 202 | 123 | 91.5111 | -942552.60 ± 14.6210 | 189638.8999 | 188137.4560 | +7980569.01 ± 123.78 | ±0.40 |
| ${}^{203}$Au | 203 | 124 | 97.8820 | -938816.72 ± 1.9287 | 190572.0944 | 189070.1596 | +7943796.24 ± 16.30 | ±0.40 |
| ${}^{204}$Au | 204 | 125 | 104.2452 | -935052.61 ± 127.0971 | 191505.2966 | 190004.4068 | +7899236.99 ± 1054.03 | ±0.40 |
| ${}^{205}$Au | 205 | 126 | 110.6009 | -931359.19 ± 127.2265 | 192438.5063 | 190937.7210 | +7860077.65 ± 1048.88 | ±0.40 |
| ${}^{206}$Au | 206 | 127 | 116.9492 | -927587.45 ± 127.5510 | 193371.7235 | 191873.5950 | +7807893.09 ± 1563.22 | ±0.40 |
| ${}^{207}$Au | 207 | 128 | 123.2900 | -923874.76 ± 127.8119 | 194304.9481 | 192808.6390 | +7760591.43 ± 1555.64 | ±0.40 |
| ${}^{208}$Au | 208 | 129 | 129.6235 | -920134.55 ± 128.1558 | 195238.1800 | 193744.8632 | +7707645.57 ± 1548.12 | ±0.41 |
| ${}^{209}$Au | 209 | 130 | 135.9498 | -916455.47 ± 256.8713 | 196171.4191 | 194680.0377 | +7660679.76 ± 2052.66 | ±0.41 |
| ${}^{210}$Au | 210 | 131 | 142.2690 | -912741.97 ± 257.5992 | 197104.6654 | 195616.4417 | +7607866.09 ± 2042.83 | ±0.41 |

### Mercury (Z = 80)

_47 of 47 isotopes with a framework prediction; 47 of 47 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{170}$Hg | 170 | 90 | -139.8024 | -1107204.69 ± 260.7222 | 159803.3375 | 158359.4133 | +9118019.38 ± 1905.82 | ±0.35 |
| ${}^{171}$Hg | 171 | 91 | -133.0934 | -1101265.14 ± 260.2134 | 160736.1939 | 159288.8311 | +9086404.71 ± 1923.94 | ±0.35 |
| ${}^{172}$Hg | 172 | 92 | -126.3960 | -1095268.05 ± 113.1118 | 161669.0619 | 160215.9245 | +9069869.00 ± 936.62 | ±0.35 |
| ${}^{173}$Hg | 173 | 93 | -119.7100 | -1089574.79 ± 129.4498 | 162601.9414 | 161145.8187 | +9036056.44 ± 1242.80 | ±0.35 |
| ${}^{174}$Hg | 174 | 94 | -113.0353 | -1083825.33 ± 14.2456 | 163534.8321 | 162073.3330 | +9017517.43 ± 118.53 | ±0.35 |
| ${}^{175}$Hg | 175 | 95 | -106.3718 | -1078337.70 ± 59.7097 | 164467.7340 | 163003.4987 | +8982846.09 ± 497.44 | ±0.36 |
| ${}^{176}$Hg | 176 | 96 | -99.7193 | -1072801.17 ± 8.1206 | 165400.6470 | 163931.1776 | +8963940.73 ± 67.82 | ±0.36 |
| ${}^{177}$Hg | 177 | 97 | -93.0777 | -1067505.75 ± 61.4514 | 166333.5708 | 164861.6805 | +8928031.25 ± 513.89 | ±0.36 |
| ${}^{178}$Hg | 178 | 98 | -86.4468 | -1062173.05 ± 7.7323 | 167266.5053 | 165789.6351 | +8908097.17 ± 64.88 | ±0.36 |
| ${}^{179}$Hg | 179 | 99 | -79.8265 | -1057055.15 ± 20.0991 | 168199.4504 | 166720.5116 | +8870766.74 ± 168.67 | ±0.36 |
| ${}^{180}$Hg | 180 | 100 | -73.2166 | -1051908.29 ± 8.9585 | 169132.4060 | 167648.6882 | +8850160.69 ± 75.42 | ±0.36 |
| ${}^{181}$Hg | 181 | 101 | -66.6171 | -1046947.12 ± 10.8423 | 170065.3719 | 168579.7716 | +8812446.62 ± 91.24 | ±0.37 |
| ${}^{182}$Hg | 182 | 102 | -60.0278 | -1041978.38 ± 6.8474 | 170998.3480 | 169508.3500 | +8790115.58 ± 57.76 | ±0.37 |
| ${}^{183}$Hg | 183 | 103 | -53.4485 | -1037161.73 ± 4.9240 | 171931.3341 | 170439.6163 | +8752177.74 ± 41.56 | ±0.37 |
| ${}^{184}$Hg | 184 | 104 | -46.8792 | -1032355.49 ± 6.5783 | 172864.3302 | 171368.5703 | +8728321.32 ± 55.63 | ±0.37 |
| ${}^{185}$Hg | 185 | 105 | -40.3197 | -1027677.09 ± 9.3593 | 173797.3362 | 172300.2255 | +8688965.00 ± 79.15 | ±0.37 |
| ${}^{186}$Hg | 186 | 106 | -33.7699 | -1023016.31 ± 7.9358 | 174730.3518 | 173229.3642 | +8664740.88 ± 67.25 | ±0.37 |
| ${}^{187}$Hg | 187 | 107 | -27.2297 | -1018462.46 ± 8.7232 | 175663.3770 | 174161.2789 | +8624753.50 ± 73.86 | ±0.37 |
| ${}^{188}$Hg | 188 | 108 | -20.6989 | -1013938.49 ± 4.5702 | 176596.4116 | 175090.6931 | +8599648.97 ± 38.76 | ±0.38 |
| ${}^{189}$Hg | 189 | 109 | -14.1775 | -1009499.05 ± 21.1348 | 177529.4557 | 176022.7592 | +8559668.30 ± 179.25 | ±0.38 |
| ${}^{190}$Hg | 190 | 110 | -7.6653 | -1005102.28 ± 10.5855 | 178462.5089 | 176952.5091 | +8533362.01 ± 89.89 | ±0.38 |
| ${}^{191}$Hg | 191 | 111 | -1.1623 | -1000769.91 ± 14.7650 | 179395.5713 | 177884.7820 | +8493077.88 ± 125.25 | ±0.38 |
| ${}^{192}$Hg | 192 | 112 | 5.3318 | -996490.22 ± 10.2249 | 180328.6427 | 178814.8564 | +8465662.46 ± 86.89 | ±0.38 |
| ${}^{193}$Hg | 193 | 113 | 11.8169 | -992257.50 ± 10.1543 | 181261.7229 | 179747.2999 | +8425289.79 ± 86.26 | ±0.38 |
| ${}^{194}$Hg | 194 | 114 | 18.2932 | -988085.94 ± 1.8826 | 182194.8120 | 180677.6722 | +8396941.63 ± 15.98 | ±0.38 |
| ${}^{195}$Hg | 195 | 115 | 24.7609 | -983945.84 ± 15.0075 | 183127.9098 | 181610.3369 | +8356203.57 ± 127.42 | ±0.39 |
| ${}^{196}$Hg | 196 | 116 | 31.2199 | -979873.93 ± 1.8953 | 184061.0162 | 182541.0184 | +8326883.72 ± 16.14 | ±0.39 |
| ${}^{197}$Hg | 197 | 117 | 37.6704 | -975821.32 ± 2.0610 | 184994.1311 | 183473.7982 | +8286376.15 ± 17.47 | ±0.39 |
| ${}^{198}$Hg | 198 | 118 | 44.1126 | -971839.82 ± 0.2907 | 185927.2544 | 184404.8782 | +8255617.68 ± 2.48 | ±0.39 |
| ${}^{199}$Hg | 199 | 119 | 50.5464 | -967869.32 ± 0.3415 | 186860.3860 | 185337.7806 | +8215299.68 ± 2.83 | ±0.39 |
| ${}^{200}$Hg | 200 | 120 | 56.9720 | -963968.65 ± 0.3415 | 187793.5258 | 186269.3175 | +8182820.03 ± 2.84 | ±0.39 |
| ${}^{201}$Hg | 201 | 121 | 63.3895 | -960067.31 ± 0.4558 | 188726.6737 | 187202.6523 | +8141024.45 ± 3.80 | ±0.39 |
| ${}^{202}$Hg | 202 | 122 | 69.7990 | -956243.35 ± 0.4432 | 189659.8296 | 188134.4636 | +8107849.81 ± 3.75 | ±0.40 |
| ${}^{203}$Hg | 203 | 123 | 76.2006 | -952409.10 ± 1.0143 | 190592.9935 | 189068.0339 | +8065666.07 ± 8.62 | ±0.40 |
| ${}^{204}$Hg | 204 | 124 | 82.5943 | -948656.17 ± 0.3170 | 191526.1652 | 190000.1070 | +8031880.58 ± 2.62 | ±0.40 |
| ${}^{205}$Hg | 205 | 125 | 88.9803 | -944880.65 ± 2.2604 | 192459.3446 | 190934.0035 | +7988839.41 ± 19.14 | ±0.40 |
| ${}^{206}$Hg | 206 | 126 | 95.3586 | -941174.79 ± 12.6062 | 193392.5318 | 191866.8396 | +7951828.07 ± 106.53 | ±0.40 |
| ${}^{207}$Hg | 207 | 127 | 101.7293 | -937384.35 ± 18.3472 | 194325.7265 | 192802.7920 | +7898923.16 ± 154.60 | ±0.40 |
| ${}^{208}$Hg | 208 | 128 | 108.0925 | -933665.71 ± 18.8660 | 195258.9287 | 193737.5082 | +7852999.23 ± 158.66 | ±0.40 |
| ${}^{209}$Hg | 209 | 129 | 114.4483 | -929911.74 ± 127.9918 | 196192.1383 | 194673.6579 | +7800132.94 ± 770.37 | ±0.40 |
| ${}^{210}$Hg | 210 | 130 | 120.7968 | -926244.03 ± 128.2216 | 197125.3552 | 195608.4616 | +7754744.61 ± 1023.84 | ±0.41 |
| ${}^{211}$Hg | 211 | 131 | 127.1380 | -922521.57 ± 128.5843 | 198058.5795 | 196544.8656 | +7701619.99 ± 1018.96 | ±0.41 |
| ${}^{212}$Hg | 212 | 132 | 133.4720 | -918888.81 ± 128.8328 | 198991.8108 | 197479.7699 | +7656687.83 ± 1518.84 | ±0.41 |
| ${}^{213}$Hg | 213 | 133 | 139.7990 | -915191.47 ± 129.2157 | 199925.0493 | 198416.4440 | +7603227.15 ± 1511.67 | ±0.41 |
| ${}^{214}$Hg | 214 | 134 | 146.1189 | -911600.40 ± 258.9332 | 200858.2948 | 199351.5086 | +7558439.34 ± 2004.55 | ±0.41 |
| ${}^{215}$Hg | 215 | 135 | 152.4318 | -907935.94 ± 259.7065 | 201791.5473 | 200288.3420 | +7505206.25 ± 1995.18 | ±0.41 |
| ${}^{216}$Hg | 216 | 136 | 158.7379 | -904372.44 ± 260.2472 | 202724.8066 | 201223.6468 | +7460156.04 ± 1985.90 | ±0.41 |

### Thallium (Z = 81)

_43 of 43 isotopes with a framework prediction; 43 of 43 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{176}$Tl | 176 | 95 | -122.5590 | -1090342.96 ± 61.2226 | 165422.7043 | 163943.5470 | +9022357.83 ± 506.62 | ±0.35 |
| ${}^{177}$Tl | 177 | 96 | -115.8802 | -1084671.06 ± 15.8041 | 166355.5910 | 164871.1163 | +9003849.56 ± 131.18 | ±0.36 |
| ${}^{178}$Tl | 178 | 97 | -109.2125 | -1079260.20 ± 129.1823 | 167288.4886 | 165801.3368 | +8969480.57 ± 617.99 | ±0.36 |
| ${}^{179}$Tl | 179 | 98 | -102.5556 | -1073798.75 ± 27.8096 | 168221.3972 | 166729.1749 | +8949976.67 ± 231.83 | ±0.36 |
| ${}^{180}$Tl | 180 | 99 | -95.9094 | -1068562.65 ± 49.9779 | 169154.3164 | 167659.5482 | +8915496.83 ± 417.01 | ±0.36 |
| ${}^{181}$Tl | 181 | 100 | -89.2738 | -1063299.61 ± 6.4554 | 170087.2462 | 168587.6340 | +8895149.49 ± 53.99 | ±0.36 |
| ${}^{182}$Tl | 182 | 101 | -82.6487 | -1058246.88 ± 8.4398 | 171020.1865 | 169518.5997 | +8857947.46 ± 70.64 | ±0.36 |
| ${}^{183}$Tl | 183 | 102 | -76.0338 | -1053160.54 ± 6.5253 | 171953.1371 | 170446.8337 | +8837379.77 ± 54.74 | ±0.37 |
| ${}^{184}$Tl | 184 | 103 | -69.4292 | -1048260.46 ± 6.9577 | 172886.0979 | 171378.0317 | +8799647.05 ± 58.41 | ±0.37 |
| ${}^{185}$Tl | 185 | 104 | -62.8347 | -1043346.76 ± 14.2683 | 173819.0688 | 172306.6514 | +8777475.13 ± 119.98 | ±0.37 |
| ${}^{186}$Tl | 186 | 105 | -56.2501 | -1038586.16 ± 14.2392 | 174752.0496 | 173238.0204 | +8739589.89 ± 119.78 | ±0.37 |
| ${}^{187}$Tl | 187 | 106 | -49.6753 | -1033829.27 ± 5.4760 | 175685.0402 | 174166.9528 | +8716277.18 ± 46.21 | ±0.37 |
| ${}^{188}$Tl | 188 | 107 | -43.1102 | -1029200.04 ± 20.2596 | 176618.0406 | 175098.5551 | +8677887.04 ± 170.78 | ±0.37 |
| ${}^{189}$Tl | 189 | 108 | -36.5547 | -1024587.39 ± 5.6316 | 177551.0505 | 176027.7695 | +8653640.32 ± 47.54 | ±0.37 |
| ${}^{190}$Tl | 190 | 109 | -30.0087 | -1020078.77 ± 4.8563 | 178484.0699 | 176959.5135 | +8615283.77 ± 40.97 | ±0.38 |
| ${}^{191}$Tl | 191 | 110 | -23.4720 | -1015600.82 ± 4.8876 | 179417.0986 | 177889.0909 | +8589665.48 ± 41.31 | ±0.38 |
| ${}^{192}$Tl | 192 | 111 | -16.9446 | -1011205.27 ± 20.9497 | 180350.1366 | 178820.9957 | +8551238.43 ± 177.11 | ±0.38 |
| ${}^{193}$Tl | 193 | 112 | -10.4263 | -1006850.94 ± 4.4133 | 181283.1838 | 179750.8848 | +8524569.80 ± 37.31 | ±0.38 |
| ${}^{194}$Tl | 194 | 113 | -3.9170 | -1002561.12 ± 9.1330 | 182216.2399 | 180682.9186 | +8486254.84 ± 77.33 | ±0.38 |
| ${}^{195}$Tl | 195 | 114 | 2.5834 | -998321.07 ± 7.2363 | 183149.3050 | 181613.1949 | +8458141.26 ± 61.26 | ±0.38 |
| ${}^{196}$Tl | 196 | 115 | 9.0749 | -994130.48 ± 7.8344 | 184082.3789 | 182545.3477 | +8419996.28 ± 66.34 | ±0.38 |
| ${}^{197}$Tl | 197 | 116 | 15.5577 | -989995.25 ± 8.7286 | 185015.4615 | 183475.9842 | +8390620.04 ± 73.99 | ±0.39 |
| ${}^{198}$Tl | 198 | 117 | 22.0319 | -985897.58 ± 4.8287 | 185948.5527 | 184408.3038 | +8352383.71 ± 40.92 | ±0.39 |
| ${}^{199}$Tl | 199 | 118 | 28.4976 | -981858.84 ± 17.7859 | 186881.6524 | 185339.2672 | +8321955.75 ± 150.78 | ±0.39 |
| ${}^{200}$Tl | 200 | 119 | 34.9549 | -977847.77 ± 3.6503 | 187814.7606 | 186271.7735 | +8283525.85 ± 30.91 | ±0.39 |
| ${}^{201}$Tl | 201 | 120 | 41.4039 | -973896.56 ± 8.9466 | 188747.8770 | 187203.1341 | +8251693.91 ± 75.77 | ±0.39 |
| ${}^{202}$Tl | 202 | 121 | 47.8446 | -969966.04 ± 1.1539 | 189681.0017 | 188135.8285 | +8213072.42 ± 9.76 | ±0.39 |
| ${}^{203}$Tl | 203 | 122 | 54.2772 | -966095.16 ± 0.7355 | 190614.1345 | 189067.5417 | +8180107.36 ± 6.19 | ±0.39 |
| ${}^{204}$Tl | 204 | 123 | 60.7018 | -962238.99 ± 0.7233 | 191547.2754 | 190000.4511 | +8141161.23 ± 6.07 | ±0.39 |
| ${}^{205}$Tl | 205 | 124 | 67.1184 | -958442.46 ± 0.7616 | 192480.4242 | 190932.4705 | +8107336.29 ± 6.49 | ±0.40 |
| ${}^{206}$Tl | 206 | 125 | 73.5271 | -954656.96 ± 0.7876 | 193413.5809 | 191865.5321 | +8068404.93 ± 6.70 | ±0.40 |
| ${}^{207}$Tl | 207 | 126 | 79.9281 | -950916.99 ± 3.3432 | 194346.7453 | 192798.2450 | +8031713.63 ± 28.21 | ±0.40 |
| ${}^{208}$Tl | 208 | 127 | 86.3214 | -947113.93 ± 1.1342 | 195279.9175 | 193734.0235 | +7979465.77 ± 9.56 | ±0.40 |
| ${}^{209}$Tl | 209 | 128 | 92.7071 | -943373.94 ± 3.7276 | 196213.0972 | 194668.6229 | +7933863.69 ± 31.38 | ±0.40 |
| ${}^{210}$Tl | 210 | 129 | 99.0852 | -939613.61 ± 7.0774 | 197146.2845 | 195604.5148 | +7882076.14 ± 59.32 | ±0.40 |
| ${}^{211}$Tl | 211 | 130 | 105.4560 | -935922.49 ± 25.4750 | 198079.4792 | 196539.1779 | +7837120.81 ± 213.28 | ±0.40 |
| ${}^{212}$Tl | 212 | 131 | 111.8193 | -932204.42 ± 128.5347 | 199012.6812 | 197475.1991 | +7785697.57 ± 1014.16 | ±0.40 |
| ${}^{213}$Tl | 213 | 132 | 118.1754 | -928553.35 ± 16.3288 | 199945.8906 | 198410.0279 | +7740852.02 ± 136.15 | ±0.41 |
| ${}^{214}$Tl | 214 | 133 | 124.5243 | -924869.06 ± 129.1156 | 200879.1071 | 199346.2028 | +7689659.13 ± 981.28 | ±0.41 |
| ${}^{215}$Tl | 215 | 134 | 130.8660 | -921257.54 ± 129.3661 | 201812.3308 | 200281.2626 | +7644590.07 ± 1497.60 | ±0.41 |
| ${}^{216}$Tl | 216 | 135 | 137.2007 | -917604.28 ± 129.7185 | 202745.5615 | 201217.5968 | +7593593.93 ± 1490.63 | ±0.41 |
| ${}^{217}$Tl | 217 | 136 | 143.5285 | -914022.94 ± 259.9766 | 203678.7992 | 202152.8802 | +7548341.59 ± 1976.78 | ±0.41 |
| ${}^{218}$Tl | 218 | 137 | 149.8493 | -910403.79 ± 260.6882 | 204612.0438 | 203089.4249 | +7497283.14 ± 1967.66 | ±0.41 |

### Lead (Z = 82)

_43 of 43 isotopes with a framework prediction; 43 of 43 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{178}$Pb | 178 | 96 | -132.2307 | -1096591.48 ± 16.9292 | 167310.7245 | 165809.5238 | +9053766.53 ± 139.82 | ±0.35 |
| ${}^{179}$Pb | 179 | 97 | -125.5368 | -1091063.56 ± 58.9239 | 168243.5960 | 166739.4962 | +9020657.21 ± 487.16 | ±0.35 |
| ${}^{180}$Pb | 180 | 98 | -118.8538 | -1085467.84 ± 8.9183 | 169176.4785 | 167666.9976 | +9002850.22 ± 73.92 | ±0.36 |
| ${}^{181}$Pb | 181 | 99 | -112.1817 | -1080137.40 ± 60.7442 | 170109.3718 | 168597.3221 | +8968408.36 ± 504.37 | ±0.36 |
| ${}^{182}$Pb | 182 | 100 | -105.5203 | -1074749.50 ± 8.5608 | 171042.2758 | 169525.1023 | +8949550.58 ± 71.29 | ±0.36 |
| ${}^{183}$Pb | 183 | 101 | -98.8695 | -1069602.91 ± 20.4066 | 171975.1904 | 170455.8410 | +8913448.92 ± 170.01 | ±0.36 |
| ${}^{184}$Pb | 184 | 102 | -92.2291 | -1064404.82 ± 8.9429 | 172908.1155 | 171383.8635 | +8893789.25 ± 74.70 | ±0.36 |
| ${}^{185}$Pb | 185 | 103 | -85.5990 | -1059419.74 ± 11.2239 | 173841.0508 | 172314.8680 | +8856942.41 ± 93.87 | ±0.36 |
| ${}^{186}$Pb | 186 | 104 | -78.9792 | -1054401.12 ± 7.5845 | 174773.9964 | 173243.2224 | +8835982.11 ± 63.52 | ±0.37 |
| ${}^{187}$Pb | 187 | 105 | -72.3694 | -1049562.28 ± 3.4834 | 175706.9520 | 174174.4104 | +8798890.74 ± 29.24 | ±0.37 |
| ${}^{188}$Pb | 188 | 106 | -65.7696 | -1044708.77 ± 6.8883 | 176639.9176 | 175103.0805 | +8776756.84 ± 57.81 | ±0.37 |
| ${}^{189}$Pb | 189 | 107 | -59.1796 | -1040008.61 ± 9.5064 | 177572.8930 | 176034.5416 | +8738918.21 ± 79.88 | ±0.37 |
| ${}^{190}$Pb | 190 | 108 | -52.5993 | -1035305.91 ± 8.4044 | 178505.8782 | 176963.4631 | +8716008.58 ± 70.71 | ±0.37 |
| ${}^{191}$Pb | 191 | 109 | -46.0285 | -1030731.58 ± 4.4123 | 179438.8729 | 177895.0826 | +8678094.31 ± 37.17 | ±0.37 |
| ${}^{192}$Pb | 192 | 110 | -39.4673 | -1026170.35 ± 3.7939 | 180371.8771 | 178824.3161 | +8654085.87 ± 32.02 | ±0.38 |
| ${}^{193}$Pb | 193 | 111 | -32.9154 | -1021714.30 ± 6.7863 | 181304.8906 | 179756.1328 | +8615883.17 ± 57.23 | ±0.38 |
| ${}^{194}$Pb | 194 | 112 | -26.3728 | -1017283.54 ± 11.4298 | 182237.9134 | 180685.6483 | +8590970.90 ± 96.49 | ±0.38 |
| ${}^{195}$Pb | 195 | 113 | -19.8393 | -1012937.35 ± 3.3189 | 183170.9453 | 181617.6122 | +8552767.23 ± 28.01 | ±0.38 |
| ${}^{196}$Pb | 196 | 114 | -13.3149 | -1008628.25 ± 4.9915 | 184103.9863 | 182547.4961 | +8526494.57 ± 42.24 | ±0.38 |
| ${}^{197}$Pb | 197 | 115 | -6.7994 | -1004384.88 ± 3.0999 | 185037.0362 | 183479.5930 | +8488372.83 ± 26.18 | ±0.38 |
| ${}^{198}$Pb | 198 | 116 | -0.2927 | -1000187.62 ± 5.6099 | 185970.0950 | 184409.7651 | +8461210.76 ± 47.45 | ±0.38 |
| ${}^{199}$Pb | 199 | 117 | 6.2053 | -996040.72 ± 4.3551 | 186903.1624 | 185342.0949 | +8422628.14 ± 36.80 | ±0.39 |
| ${}^{200}$Pb | 200 | 118 | 12.6946 | -991946.91 ± 6.3437 | 187836.2385 | 186272.5699 | +8394519.16 ± 53.73 | ±0.39 |
| ${}^{201}$Pb | 201 | 119 | 19.1754 | -987890.15 ± 8.6825 | 188769.3232 | 187205.0438 | +8355967.97 ± 73.43 | ±0.39 |
| ${}^{202}$Pb | 202 | 120 | 25.6478 | -983891.56 ± 2.3851 | 189702.4162 | 188135.8683 | +8326683.73 ± 20.18 | ±0.39 |
| ${}^{203}$Pb | 203 | 121 | 32.1118 | -979918.98 ± 4.1003 | 190635.5176 | 189068.5166 | +8288006.19 ± 34.66 | ±0.39 |
| ${}^{204}$Pb | 204 | 122 | 38.5676 | -976007.82 ± 0.7107 | 191568.6272 | 189999.6873 | +8257591.98 ± 6.04 | ±0.39 |
| ${}^{205}$Pb | 205 | 123 | 45.0152 | -972113.63 ± 0.7112 | 192501.7450 | 190932.5211 | +8218735.66 ± 5.99 | ±0.39 |
| ${}^{206}$Pb | 206 | 124 | 51.4548 | -968283.28 ± 0.7111 | 193434.8709 | 191863.9999 | +8187419.22 ± 5.96 | ±0.39 |
| ${}^{207}$Pb | 207 | 125 | 57.8864 | -964466.42 ± 0.6989 | 194368.0047 | 192796.8275 | +8149393.27 ± 5.95 | ±0.40 |
| ${}^{208}$Pb | 208 | 126 | 64.3102 | -960700.95 ± 0.6991 | 195301.1464 | 193729.0251 | +8115053.01 ± 5.92 | ±0.40 |
| ${}^{209}$Pb | 209 | 127 | 70.7261 | -956884.00 ± 1.0702 | 196234.2958 | 194664.6531 | +8063316.68 ± 8.97 | ±0.40 |
| ${}^{210}$Pb | 210 | 128 | 77.1343 | -953125.59 ± 0.8806 | 197167.4530 | 195599.0334 | +8018545.22 ± 7.40 | ±0.40 |
| ${}^{211}$Pb | 211 | 129 | 83.5349 | -949354.01 ± 1.3688 | 198100.6179 | 196534.7629 | +7967318.22 ± 11.50 | ±0.40 |
| ${}^{212}$Pb | 212 | 130 | 89.9280 | -945646.96 ± 1.1148 | 199033.7902 | 197469.2011 | +7923206.10 ± 9.32 | ±0.40 |
| ${}^{213}$Pb | 213 | 131 | 96.3136 | -941918.27 ± 4.1874 | 199966.9701 | 198405.0405 | +7872428.89 ± 35.05 | ±0.40 |
| ${}^{214}$Pb | 214 | 132 | 102.6918 | -938259.95 ± 1.1837 | 200900.1573 | 199339.5552 | +7828863.17 ± 9.88 | ±0.40 |
| ${}^{215}$Pb | 215 | 133 | 109.0627 | -934569.15 ± 31.6017 | 201833.3518 | 200275.5745 | +7778168.93 ± 263.06 | ±0.41 |
| ${}^{216}$Pb | 216 | 134 | 115.4264 | -930958.49 ± 129.1990 | 202766.5535 | 201210.2361 | +7734782.58 ± 995.33 | ±0.41 |
| ${}^{217}$Pb | 217 | 135 | 121.7829 | -927294.79 ± 129.5505 | 203699.7624 | 202146.4808 | +7683940.82 ± 1483.78 | ±0.41 |
| ${}^{218}$Pb | 218 | 136 | 128.1323 | -923716.67 ± 129.7859 | 204632.9784 | 203081.3442 | +7640456.83 ± 1476.95 | ±0.41 |
| ${}^{219}$Pb | 219 | 137 | 134.4748 | -920088.47 ± 260.2811 | 205566.2014 | 204017.8283 | +7589400.91 ± 1958.71 | ±0.41 |
| ${}^{220}$Pb | 220 | 138 | 140.8103 | -916551.89 ± 260.7562 | 206499.4313 | 204952.8332 | +7546117.10 ± 1949.77 | ±0.41 |

### Bismuth (Z = 83)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{184}$Bi | 184 | 101 | -115.2788 | -1081239.03 ± 129.6680 | 172930.3829 | 171396.1698 | +8951268.03 ± 711.95 | ±0.36 |
| ${}^{185}$Bi | 185 | 102 | -108.6129 | -1075930.74 ± 0.0000 | 173863.2823 | 172324.1736 | +8931473.01 ± 470.28 | ±0.36 |
| ${}^{186}$Bi | 186 | 103 | -101.9573 | -1070829.48 ± 11.7714 | 174796.1922 | 173254.7578 | +8896923.96 ± 97.85 | ±0.36 |
| ${}^{187}$Bi | 187 | 104 | -95.3121 | -1065696.92 ± 6.8959 | 175729.1124 | 174183.0141 | +8876286.23 ± 57.44 | ±0.36 |
| ${}^{188}$Bi | 188 | 105 | -88.6771 | -1060751.55 ± 7.6634 | 176662.0428 | 175113.6967 | +8841947.51 ± 63.84 | ±0.37 |
| ${}^{189}$Bi | 189 | 106 | -82.0521 | -1055794.67 ± 14.1756 | 177594.9833 | 176042.3209 | +8819824.33 ± 118.44 | ±0.37 |
| ${}^{190}$Bi | 190 | 107 | -75.4371 | -1050998.20 ± 14.1805 | 178527.9337 | 176973.2838 | +8784658.73 ± 118.51 | ±0.37 |
| ${}^{191}$Bi | 191 | 108 | -68.8320 | -1046198.23 ± 5.0252 | 179460.8939 | 177902.1345 | +8761893.14 ± 42.08 | ±0.37 |
| ${}^{192}$Bi | 192 | 109 | -62.2365 | -1041538.27 ± 20.0933 | 180393.8639 | 178833.3334 | +8726172.58 ± 168.38 | ±0.37 |
| ${}^{193}$Bi | 193 | 110 | -55.6506 | -1036886.13 ± 5.0274 | 181326.8435 | 179762.4775 | +8702405.69 ± 42.14 | ±0.37 |
| ${}^{194}$Bi | 194 | 111 | -49.0742 | -1032351.15 ± 3.4658 | 182259.8325 | 180693.8331 | +8666590.14 ± 29.06 | ±0.37 |
| ${}^{195}$Bi | 195 | 112 | -42.5072 | -1027837.12 ± 3.4607 | 183192.8309 | 181623.3247 | +8641545.59 ± 29.11 | ±0.38 |
| ${}^{196}$Bi | 196 | 113 | -35.9495 | -1023419.04 ± 15.9093 | 184125.8386 | 182554.8353 | +8605651.37 ± 133.81 | ±0.38 |
| ${}^{197}$Bi | 197 | 114 | -29.4009 | -1019032.12 ± 5.3943 | 185058.8554 | 183484.6512 | +8579486.82 ± 45.42 | ±0.38 |
| ${}^{198}$Bi | 198 | 115 | -22.8613 | -1014724.90 ± 17.7524 | 185991.8812 | 184416.4587 | +8542743.83 ± 149.50 | ±0.38 |
| ${}^{199}$Bi | 199 | 116 | -16.3307 | -1010454.61 ± 6.7902 | 186924.9161 | 185346.5290 | +8515870.48 ± 57.27 | ±0.38 |
| ${}^{200}$Bi | 200 | 117 | -9.8089 | -1006248.91 ± 14.4614 | 187857.9597 | 186278.4502 | +8479292.88 ± 121.86 | ±0.38 |
| ${}^{201}$Bi | 201 | 118 | -3.2959 | -1002087.54 ± 7.7150 | 188791.0121 | 187208.8858 | +8451127.97 ± 65.04 | ±0.38 |
| ${}^{202}$Bi | 202 | 119 | 3.2085 | -997977.26 ± 8.8251 | 189724.0731 | 188141.0581 | +8413979.60 ± 74.42 | ±0.39 |
| ${}^{203}$Bi | 203 | 120 | 9.7044 | -993916.01 ± 8.0051 | 190657.1427 | 189071.7782 | +8384987.68 ± 67.58 | ±0.39 |
| ${}^{204}$Bi | 204 | 121 | 16.1918 | -989894.41 ± 5.7294 | 191590.2207 | 190004.1512 | +8347551.70 ± 48.31 | ±0.39 |
| ${}^{205}$Bi | 205 | 122 | 22.6708 | -985925.30 ± 2.9908 | 192523.3071 | 190935.2257 | +8317382.91 ± 25.18 | ±0.39 |
| ${}^{206}$Bi | 206 | 123 | 29.1416 | -981986.71 ± 4.7241 | 193456.4017 | 191867.7572 | +8279893.19 ± 39.78 | ±0.39 |
| ${}^{207}$Bi | 207 | 124 | 35.6043 | -978101.58 ± 1.4769 | 194389.5045 | 192799.2249 | +8248371.23 ± 12.43 | ±0.39 |
| ${}^{208}$Bi | 208 | 125 | 42.0588 | -974240.81 ± 1.4140 | 195322.6154 | 193731.9034 | +8210893.08 ± 11.90 | ±0.39 |
| ${}^{209}$Bi | 209 | 126 | 48.5054 | -970427.68 ± 0.8282 | 196255.7342 | 194664.0091 | +8176781.86 ± 7.01 | ±0.39 |
| ${}^{210}$Bi | 210 | 127 | 54.9440 | -966596.00 ± 0.8299 | 197188.8610 | 195598.9699 | +8128320.47 ± 6.97 | ±0.40 |
| ${}^{211}$Bi | 211 | 128 | 61.3749 | -962802.48 ± 3.2993 | 198121.9956 | 196533.3968 | +8083098.45 ± 27.69 | ±0.40 |
| ${}^{212}$Bi | 212 | 129 | 67.7980 | -959017.17 ± 1.1149 | 199055.1379 | 197468.6320 | +8034216.92 ± 9.38 | ±0.40 |
| ${}^{213}$Bi | 213 | 130 | 74.2135 | -955279.29 ± 3.0676 | 199988.2878 | 198403.0124 | +7990178.09 ± 25.61 | ±0.40 |
| ${}^{214}$Bi | 214 | 131 | 80.6214 | -951535.91 ± 6.7409 | 200921.4453 | 199338.5374 | +7940802.35 ± 56.23 | ±0.40 |
| ${}^{215}$Bi | 215 | 132 | 87.0218 | -947852.71 ± 3.3755 | 201854.6103 | 200272.8616 | +7897968.61 ± 28.08 | ±0.40 |
| ${}^{216}$Bi | 216 | 133 | 93.4148 | -944149.80 ± 6.6895 | 202787.7828 | 201208.6004 | +7848483.41 ± 55.55 | ±0.40 |
| ${}^{217}$Bi | 217 | 134 | 99.8005 | -940517.45 ± 10.5537 | 203720.9625 | 202142.9505 | +7806416.27 ± 87.55 | ±0.40 |
| ${}^{218}$Bi | 218 | 135 | 106.1789 | -936850.75 ± 16.0641 | 204654.1495 | 203078.9306 | +7756682.67 ± 133.02 | ±0.41 |
| ${}^{219}$Bi | 219 | 136 | 112.5502 | -933256.12 ± 129.8701 | 205587.3436 | 204013.5285 | +7714268.51 ± 981.66 | ±0.41 |
| ${}^{220}$Bi | 220 | 137 | 118.9144 | -929628.97 ± 130.1914 | 206520.5449 | 204949.6624 | +7664723.62 ± 1463.49 | ±0.41 |
| ${}^{221}$Bi | 221 | 138 | 125.2715 | -926077.28 ± 130.4121 | 207453.7532 | 205884.3971 | +7622510.74 ± 1456.84 | ±0.41 |
| ${}^{222}$Bi | 222 | 139 | 131.6217 | -922477.70 ± 130.7531 | 208386.9684 | 206820.6409 | +7573361.45 ± 1450.25 | ±0.41 |
| ${}^{223}$Bi | 223 | 140 | 137.9650 | -918978.89 ± 261.9172 | 209320.1905 | 207755.4251 | +7531766.94 ± 1923.47 | ±0.41 |
| ${}^{224}$Bi | 224 | 141 | 144.3015 | -915414.50 ± 262.6050 | 210253.4194 | 208691.7490 | +7483144.26 ± 1914.84 | ±0.41 |

### Polonium (Z = 84)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{186}$Po | 186 | 102 | -125.1844 | -1087453.10 ± 12.7730 | 174818.6370 | 173262.0048 | +8984267.26 ± 105.49 | ±0.36 |
| ${}^{187}$Po | 187 | 103 | -118.5034 | -1082248.56 ± 22.6483 | 175751.5213 | 174192.2212 | +8951605.95 ± 187.32 | ±0.36 |
| ${}^{188}$Po | 188 | 104 | -111.8327 | -1077007.32 ± 13.7482 | 176684.4161 | 175120.3471 | +8931395.02 ± 114.03 | ±0.36 |
| ${}^{189}$Po | 189 | 105 | -105.1724 | -1071977.53 ± 15.0948 | 177617.3212 | 176050.9636 | +8897182.85 ± 125.30 | ±0.36 |
| ${}^{190}$Po | 190 | 106 | -98.5223 | -1066912.90 ± 8.9426 | 178550.2365 | 176979.3170 | +8876288.74 ± 74.38 | ±0.37 |
| ${}^{191}$Po | 191 | 107 | -91.8822 | -1062041.78 ± 4.7977 | 179483.1619 | 177910.3051 | +8840729.05 ± 39.92 | ±0.37 |
| ${}^{192}$Po | 192 | 108 | -85.2521 | -1057137.86 ± 7.1290 | 180416.0972 | 178838.8014 | +8819650.72 ± 59.46 | ±0.37 |
| ${}^{193}$Po | 193 | 109 | -78.6318 | -1052408.20 ± 9.6862 | 181349.0423 | 179770.0367 | +8783474.98 ± 80.83 | ±0.37 |
| ${}^{194}$Po | 194 | 110 | -72.0213 | -1047660.75 ± 8.5502 | 182281.9972 | 180698.8515 | +8761238.24 ± 71.45 | ±0.37 |
| ${}^{195}$Po | 195 | 111 | -65.4203 | -1043059.31 ± 3.9788 | 183214.9616 | 181630.2336 | +8725023.62 ± 33.26 | ±0.37 |
| ${}^{196}$Po | 196 | 112 | -58.8288 | -1038457.00 ± 3.5235 | 184147.9356 | 182559.3756 | +8701607.30 ± 29.48 | ±0.37 |
| ${}^{197}$Po | 197 | 113 | -52.2467 | -1033976.62 ± 6.4184 | 185080.9189 | 183490.9454 | +8665133.61 ± 53.73 | ±0.38 |
| ${}^{198}$Po | 198 | 114 | -45.6739 | -1029507.43 ± 11.2567 | 186013.9115 | 184420.3593 | +8640869.42 ± 94.48 | ±0.38 |
| ${}^{199}$Po | 199 | 115 | -39.1102 | -1025139.72 ± 3.4921 | 186946.9133 | 185352.0878 | +8604302.53 ± 29.29 | ±0.38 |
| ${}^{200}$Po | 200 | 116 | -32.5556 | -1020795.81 ± 4.8419 | 187879.9241 | 186281.8791 | +8578639.02 ± 40.68 | ±0.38 |
| ${}^{201}$Po | 201 | 117 | -26.0099 | -1016533.78 ± 3.1431 | 188812.9438 | 187213.7937 | +8541839.27 ± 26.40 | ±0.38 |
| ${}^{202}$Po | 202 | 118 | -19.4731 | -1012304.27 ± 5.4756 | 189745.9724 | 188143.8674 | +8515318.98 ± 46.08 | ±0.38 |
| ${}^{203}$Po | 203 | 119 | -12.9451 | -1008141.18 ± 2.9236 | 190679.0098 | 189075.9922 | +8478165.49 ± 24.54 | ±0.38 |
| ${}^{204}$Po | 204 | 120 | -6.4256 | -1004018.11 ± 6.3018 | 191612.0558 | 190006.4561 | +8450237.55 ± 53.00 | ±0.39 |
| ${}^{205}$Po | 205 | 121 | 0.0852 | -999946.96 ± 6.2658 | 192545.1104 | 190938.7699 | +8412856.71 ± 52.68 | ±0.39 |
| ${}^{206}$Po | 206 | 122 | 6.5876 | -995921.41 ± 2.4871 | 193478.1734 | 191869.5967 | +8383697.76 ± 20.90 | ±0.39 |
| ${}^{207}$Po | 207 | 123 | 13.0816 | -991935.84 ± 4.1089 | 194411.2448 | 192802.1338 | +8345919.23 ± 34.53 | ±0.39 |
| ${}^{208}$Po | 208 | 124 | 19.5674 | -987999.80 ± 1.0205 | 195344.3245 | 193733.3044 | +8315659.09 ± 8.63 | ±0.39 |
| ${}^{209}$Po | 209 | 125 | 26.0449 | -984095.23 ± 1.0848 | 196277.4123 | 194665.9017 | +8278340.79 ± 9.13 | ±0.39 |
| ${}^{210}$Po | 210 | 126 | 32.5144 | -980236.96 ± 0.7020 | 197210.5083 | 195597.8087 | +8244977.68 ± 5.86 | ±0.39 |
| ${}^{211}$Po | 211 | 127 | 38.9759 | -976374.87 ± 0.7674 | 198143.6122 | 196532.8234 | +8196029.68 ± 6.38 | ±0.39 |
| ${}^{212}$Po | 212 | 128 | 45.4294 | -972563.00 ± 0.6914 | 199076.7241 | 197466.3806 | +8155026.39 ± 5.84 | ±0.40 |
| ${}^{213}$Po | 213 | 129 | 51.8751 | -968752.32 ± 1.8347 | 200009.8438 | 198401.5906 | +8106050.25 ± 15.39 | ±0.40 |
| ${}^{214}$Po | 214 | 130 | 58.3131 | -964998.46 ± 0.8735 | 200942.9713 | 199335.2682 | +8065321.76 ± 7.27 | ±0.40 |
| ${}^{215}$Po | 215 | 131 | 64.7434 | -961235.18 ± 1.2744 | 201876.1064 | 200270.6905 | +8016229.91 ± 10.59 | ±0.40 |
| ${}^{216}$Po | 216 | 132 | 71.1661 | -957535.74 ± 1.0826 | 202809.2491 | 201204.5087 | +7975668.22 ± 9.02 | ±0.40 |
| ${}^{217}$Po | 217 | 133 | 77.5813 | -953817.24 ± 3.9011 | 203742.3994 | 202140.1040 | +7926657.68 ± 32.37 | ±0.40 |
| ${}^{218}$Po | 218 | 134 | 83.9891 | -950168.87 ± 1.1641 | 204675.5570 | 203074.0713 | +7886214.83 ± 9.69 | ±0.40 |
| ${}^{219}$Po | 219 | 135 | 90.3895 | -946490.41 ± 9.3734 | 205608.7220 | 204009.8901 | +7837031.51 ± 77.62 | ±0.40 |
| ${}^{220}$Po | 220 | 136 | 96.7826 | -942891.31 ± 10.4372 | 206541.8943 | 204943.9663 | +7796901.91 ± 86.36 | ±0.40 |
| ${}^{221}$Po | 221 | 137 | 103.1686 | -939250.78 ± 11.5167 | 207475.0737 | 205879.9707 | +7747733.13 ± 95.01 | ±0.41 |
| ${}^{222}$Po | 222 | 138 | 109.5474 | -935697.61 ± 23.5079 | 208408.2603 | 206814.1773 | +7707803.52 ± 193.67 | ±0.41 |
| ${}^{223}$Po | 223 | 139 | 115.9192 | -932094.43 ± 130.6336 | 209341.4540 | 207750.2637 | +7659149.42 ± 941.58 | ±0.41 |
| ${}^{224}$Po | 224 | 140 | 122.2840 | -928583.10 ± 130.8216 | 210274.6546 | 208684.5895 | +7619465.74 ± 937.37 | ±0.41 |
| ${}^{225}$Po | 225 | 141 | 128.6419 | -925027.29 ± 131.1303 | 211207.8621 | 209620.7532 | +7571334.86 ± 1430.88 | ±0.41 |
| ${}^{226}$Po | 226 | 142 | 134.9930 | -921550.55 ± 262.6740 | 212141.0765 | 210555.2160 | +7531803.41 ± 1902.32 | ±0.41 |
| ${}^{227}$Po | 227 | 143 | 141.3373 | -918031.69 ± 263.2965 | 213074.2976 | 211491.4421 | +7484253.29 ± 1893.89 | ±0.41 |

### Astatine (Z = 85)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{191}$At | 191 | 106 | -115.1793 | -1078286.28 ± 10.9439 | 179505.6767 | 177919.2377 | +8916623.98 ± 90.51 | ±0.36 |
| ${}^{192}$At | 192 | 107 | -108.5142 | -1073307.12 ± 18.8333 | 180438.5769 | 178849.7937 | +8883338.51 ± 155.84 | ±0.36 |
| ${}^{193}$At | 193 | 108 | -101.8591 | -1068300.72 ± 14.5074 | 181371.4872 | 179778.2947 | +8861984.92 ± 120.32 | ±0.37 |
| ${}^{194}$At | 194 | 109 | -95.2139 | -1063473.71 ± 15.6617 | 182304.4075 | 180709.1396 | +8827820.60 ± 130.05 | ±0.37 |
| ${}^{195}$At | 195 | 110 | -88.5786 | -1058627.23 ± 6.3370 | 183237.3376 | 181637.8799 | +8805749.48 ± 52.70 | ±0.37 |
| ${}^{196}$At | 196 | 111 | -81.9530 | -1053938.00 ± 19.9045 | 184170.2774 | 182568.9312 | +8771187.09 ± 165.61 | ±0.37 |
| ${}^{197}$At | 197 | 112 | -75.3370 | -1049242.89 ± 5.2150 | 185103.2268 | 183497.9832 | +8748017.93 ± 43.50 | ±0.37 |
| ${}^{198}$At | 198 | 113 | -68.7304 | -1044678.61 ± 3.1920 | 186036.1857 | 184429.1238 | +8713710.24 ± 26.59 | ±0.37 |
| ${}^{199}$At | 199 | 114 | -62.1333 | -1040124.42 ± 3.4826 | 186969.1540 | 185358.5033 | +8689381.58 ± 29.05 | ±0.38 |
| ${}^{200}$At | 200 | 115 | -55.5455 | -1035680.35 ± 15.7122 | 187902.1316 | 186289.8328 | +8654786.57 ± 131.33 | ±0.38 |
| ${}^{201}$At | 201 | 116 | -48.9668 | -1031256.22 ± 5.2219 | 188835.1183 | 187219.5254 | +8629404.02 ± 43.71 | ±0.38 |
| ${}^{202}$At | 202 | 117 | -42.3972 | -1026927.35 ± 17.5250 | 189768.1141 | 188151.2138 | +8593621.35 ± 146.70 | ±0.38 |
| ${}^{203}$At | 203 | 118 | -35.8365 | -1022622.04 ± 6.7020 | 190701.1189 | 189081.1404 | +8567636.35 ± 56.18 | ±0.38 |
| ${}^{204}$At | 204 | 119 | -29.2847 | -1018395.79 ± 14.2371 | 191634.1325 | 190012.9219 | +8532107.20 ± 119.30 | ±0.38 |
| ${}^{205}$At | 205 | 120 | -22.7417 | -1014203.73 ± 7.5285 | 192567.1549 | 190943.3067 | +8504347.19 ± 63.13 | ±0.38 |
| ${}^{206}$At | 206 | 121 | -16.2073 | -1010075.21 ± 8.4135 | 193500.1860 | 191875.3460 | +8468206.20 ± 70.50 | ±0.38 |
| ${}^{207}$At | 207 | 122 | -9.6815 | -1005985.51 ± 7.6658 | 194433.2256 | 192806.0520 | +8439432.23 ± 64.34 | ±0.39 |
| ${}^{208}$At | 208 | 123 | -3.1642 | -1001947.42 ± 5.4919 | 195366.2737 | 193738.3037 | +8402933.20 ± 46.05 | ±0.39 |
| ${}^{209}$At | 209 | 124 | 3.3448 | -997952.13 ± 2.9048 | 196299.3302 | 194669.3839 | +8372894.81 ± 24.37 | ±0.39 |
| ${}^{210}$At | 210 | 125 | 9.8454 | -993998.35 ± 4.6853 | 197232.3949 | 195601.7897 | +8336351.47 ± 39.34 | ±0.39 |
| ${}^{211}$At | 211 | 126 | 16.3379 | -990087.43 ± 1.6514 | 198165.4679 | 196533.6087 | +8303206.96 ± 13.88 | ±0.39 |
| ${}^{212}$At | 212 | 127 | 22.8222 | -986195.54 ± 1.4490 | 199098.5490 | 197468.1218 | +8256660.10 ± 12.07 | ±0.39 |
| ${}^{213}$At | 213 | 128 | 29.2985 | -982342.53 ± 2.9525 | 200031.6381 | 198401.6646 | +8215523.50 ± 24.69 | ±0.39 |
| ${}^{214}$At | 214 | 129 | 35.7669 | -978507.30 ± 2.3919 | 200964.7352 | 199336.3590 | +8168986.91 ± 19.97 | ±0.39 |
| ${}^{215}$At | 215 | 130 | 42.2274 | -974715.49 ± 3.9651 | 201897.8400 | 200269.9757 | +8128349.37 ± 33.10 | ±0.40 |
| ${}^{216}$At | 216 | 131 | 48.6802 | -970931.11 ± 2.1411 | 202830.9527 | 201204.9831 | +8081159.85 ± 17.76 | ±0.40 |
| ${}^{217}$At | 217 | 132 | 55.1253 | -967198.71 ± 2.9698 | 203764.0731 | 202138.6151 | +8041303.54 ± 24.74 | ±0.40 |
| ${}^{218}$At | 218 | 133 | 61.5627 | -963463.13 ± 6.8313 | 204697.2010 | 203073.8148 | +7994069.53 ± 56.64 | ±0.40 |
| ${}^{219}$At | 219 | 134 | 67.9927 | -959784.87 ± 1.9170 | 205630.3365 | 204007.6047 | +7954271.00 ± 15.86 | ±0.40 |
| ${}^{220}$At | 220 | 135 | 74.4151 | -956092.46 ± 8.2428 | 206563.4794 | 204943.0786 | +7906589.91 ± 68.18 | ±0.40 |
| ${}^{221}$At | 221 | 136 | 80.8303 | -952466.18 ± 8.2137 | 207496.6297 | 205876.9797 | +7867077.22 ± 67.87 | ±0.40 |
| ${}^{222}$At | 222 | 137 | 87.2381 | -948815.36 ± 9.2870 | 208429.7873 | 206812.6441 | +7819363.75 ± 76.57 | ±0.40 |
| ${}^{223}$At | 223 | 138 | 93.6387 | -945239.78 ± 8.1768 | 209362.9522 | 207746.6131 | +7780338.75 ± 67.26 | ±0.41 |
| ${}^{224}$At | 224 | 139 | 100.0322 | -941630.17 ± 13.0445 | 210296.1241 | 208682.3903 | +7732966.22 ± 107.13 | ±0.41 |
| ${}^{225}$At | 225 | 140 | 106.4185 | -938100.87 ± 130.8729 | 211229.3032 | 209616.4730 | +7694195.79 ± 1430.90 | ±0.41 |
| ${}^{226}$At | 226 | 141 | 112.7979 | -934534.91 ± 131.1647 | 212162.4892 | 210552.3274 | +7647323.64 ± 1424.54 | ±0.41 |
| ${}^{227}$At | 227 | 142 | 119.1704 | -931041.68 ± 131.3543 | 213095.6822 | 211486.5918 | +7608474.72 ± 1418.25 | ±0.41 |
| ${}^{228}$At | 228 | 143 | 125.5360 | -927514.95 ± 263.2965 | 214028.8820 | 212422.5356 | +7562033.64 ± 1881.21 | ±0.41 |
| ${}^{229}$At | 229 | 144 | 131.8948 | -924065.95 ± 263.6783 | 214962.0886 | 213357.0394 | +7522832.24 ± 1872.97 | ±0.41 |

### Radon (Z = 86)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{193}$Rn | 193 | 107 | -125.3323 | -1084601.70 ± 16.9493 | 181394.1781 | 179787.4049 | +8937073.24 ± 139.67 | ±0.36 |
| ${}^{194}$Rn | 194 | 108 | -118.6521 | -1079481.39 ± 11.1631 | 182327.0634 | 180715.5807 | +8917231.45 ± 92.18 | ±0.36 |
| ${}^{195}$Rn | 195 | 109 | -111.9821 | -1074576.40 ± 34.4269 | 183259.9587 | 181646.4005 | +8882962.83 ± 284.54 | ±0.37 |
| ${}^{196}$Rn | 196 | 110 | -105.3219 | -1069624.13 ± 9.2900 | 184192.8640 | 182574.8195 | +8862364.03 ± 76.97 | ±0.37 |
| ${}^{197}$Rn | 197 | 111 | -98.6716 | -1064861.86 ± 10.6447 | 185125.7791 | 183505.8488 | +8827676.78 ± 88.24 | ±0.37 |
| ${}^{198}$Rn | 198 | 112 | -92.0310 | -1060069.73 ± 8.7623 | 186058.7039 | 184434.6022 | +8805840.74 ± 72.76 | ±0.37 |
| ${}^{199}$Rn | 199 | 113 | -85.4000 | -1055437.62 ± 4.7410 | 186991.6384 | 185365.7668 | +8771153.49 ± 39.36 | ±0.37 |
| ${}^{200}$Rn | 200 | 114 | -78.7785 | -1050792.67 ± 3.7396 | 187924.5823 | 186294.8203 | +8748294.92 ± 31.09 | ±0.37 |
| ${}^{201}$Rn | 201 | 115 | -72.1664 | -1046285.43 ± 6.4973 | 188857.5356 | 187226.2074 | +8713140.26 ± 54.06 | ±0.37 |
| ${}^{202}$Rn | 202 | 116 | -65.5636 | -1041776.25 ± 11.1593 | 189790.4982 | 188155.5344 | +8689427.38 ± 93.11 | ±0.38 |
| ${}^{203}$Rn | 203 | 117 | -58.9700 | -1037384.76 ± 3.6807 | 190723.4700 | 189087.1190 | +8653952.85 ± 30.75 | ±0.38 |
| ${}^{204}$Rn | 204 | 118 | -52.3854 | -1033004.14 ± 4.6912 | 191656.4509 | 190016.8270 | +8628834.92 ± 39.17 | ±0.38 |
| ${}^{205}$Rn | 205 | 119 | -45.8098 | -1028720.01 ± 3.1874 | 192589.4407 | 190948.5815 | +8593199.23 ± 26.60 | ±0.38 |
| ${}^{206}$Rn | 206 | 120 | -39.2431 | -1024457.48 ± 5.3537 | 193522.4394 | 191878.6524 | +8566804.76 ± 44.77 | ±0.38 |
| ${}^{207}$Rn | 207 | 121 | -32.6851 | -1020274.67 ± 2.9404 | 194455.4469 | 192810.6447 | +8530660.46 ± 24.59 | ±0.38 |
| ${}^{208}$Rn | 208 | 122 | -26.1358 | -1016121.22 ± 6.2738 | 195388.4630 | 193741.1182 | +8502814.75 ± 52.45 | ±0.38 |
| ${}^{209}$Rn | 209 | 123 | -19.5952 | -1012032.16 ± 6.1215 | 196321.4878 | 194673.3266 | +8466291.46 ± 51.16 | ±0.39 |
| ${}^{210}$Rn | 210 | 124 | -13.0629 | -1007978.35 ± 2.7832 | 197254.5210 | 195604.1570 | +8437264.21 ± 23.30 | ±0.39 |
| ${}^{211}$Rn | 211 | 125 | -6.5391 | -1003976.32 ± 4.1442 | 198187.5626 | 196536.5006 | +8400790.82 ± 34.67 | ±0.39 |
| ${}^{212}$Rn | 212 | 126 | -0.0236 | -1000014.30 ± 1.8859 | 199120.6125 | 197468.0908 | +8368550.72 ± 15.75 | ±0.39 |
| ${}^{213}$Rn | 213 | 127 | 6.4837 | -996088.54 ± 2.0303 | 200053.6706 | 198402.5481 | +8322083.11 ± 16.99 | ±0.39 |
| ${}^{214}$Rn | 214 | 128 | 12.9828 | -992199.23 ± 5.5162 | 200986.7369 | 199335.4185 | +8284119.20 ± 46.09 | ±0.39 |
| ${}^{215}$Rn | 215 | 129 | 19.4739 | -988333.51 ± 3.6451 | 201919.8112 | 200270.0633 | +8237616.07 ± 30.41 | ±0.39 |
| ${}^{216}$Rn | 216 | 130 | 25.9571 | -984511.26 ± 3.4413 | 202852.8935 | 201202.9797 | +8200245.06 ± 28.67 | ±0.39 |
| ${}^{217}$Rn | 217 | 131 | 32.4324 | -980701.15 ± 2.4921 | 203785.9836 | 202137.8791 | +8153367.98 ± 20.76 | ±0.40 |
| ${}^{218}$Rn | 218 | 132 | 38.8999 | -976942.03 ± 1.3697 | 204719.0815 | 203070.9320 | +8116127.01 ± 11.40 | ±0.40 |
| ${}^{219}$Rn | 219 | 133 | 45.3597 | -973183.86 ± 1.2429 | 205652.1871 | 204006.0381 | +8069119.35 ± 10.29 | ±0.40 |
| ${}^{220}$Rn | 220 | 134 | 51.8119 | -969482.86 ± 1.0626 | 206585.3004 | 204939.3148 | +8031575.39 ± 8.85 | ±0.40 |
| ${}^{221}$Rn | 221 | 135 | 58.2565 | -965771.90 ± 3.3630 | 207518.4212 | 205874.6683 | +7984240.60 ± 27.75 | ±0.40 |
| ${}^{222}$Rn | 222 | 136 | 64.6937 | -962127.11 ± 1.1437 | 208451.5494 | 206808.0630 | +7946916.67 ± 9.40 | ±0.40 |
| ${}^{223}$Rn | 223 | 137 | 71.1234 | -958461.57 ± 4.5714 | 209384.6851 | 207743.5749 | +7899691.78 ± 37.65 | ±0.40 |
| ${}^{224}$Rn | 224 | 138 | 77.5459 | -954869.22 ± 5.7100 | 210317.8280 | 208677.1243 | +7862403.32 ± 47.03 | ±0.40 |
| ${}^{225}$Rn | 225 | 139 | 83.9611 | -951248.63 ± 6.4669 | 211250.9783 | 209612.7075 | +7815703.53 ± 53.14 | ±0.40 |
| ${}^{226}$Rn | 226 | 140 | 90.3692 | -947705.73 ± 6.0682 | 212184.1356 | 210546.4146 | +7778432.15 ± 49.76 | ±0.41 |
| ${}^{227}$Rn | 227 | 141 | 96.7701 | -944128.81 ± 8.1389 | 213117.3001 | 211482.0474 | +7732347.74 ± 66.63 | ±0.41 |
| ${}^{228}$Rn | 228 | 142 | 103.1640 | -940633.06 ± 10.1684 | 214050.4716 | 212415.8991 | +7695151.34 ± 83.22 | ±0.41 |
| ${}^{229}$Rn | 229 | 143 | 109.5510 | -937100.66 ± 7.4813 | 214983.6501 | 213351.5122 | +7649994.54 ± 61.12 | ±0.41 |
| ${}^{230}$Rn | 230 | 144 | 115.9311 | -933634.20 ± 131.6656 | 215916.8354 | 214285.8135 | +7611431.83 ± 934.60 | ±0.41 |
| ${}^{231}$Rn | 231 | 145 | 122.3044 | -930141.69 ± 131.9435 | 216850.0275 | 215221.6875 | +7565873.31 ± 1393.64 | ±0.41 |

### Francium (Z = 87)

_37 of 37 isotopes with a framework prediction; 37 of 37 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{197}$Fr | 197 | 110 | -122.2506 | -1080867.94 ± 37.3350 | 185148.5758 | 183514.5924 | +8903833.64 ± 307.52 | ±0.37 |
| ${}^{198}$Fr | 198 | 111 | -115.5755 | -1076012.58 ± 20.4709 | 186081.4661 | 184445.4102 | +8870136.22 ± 168.77 | ±0.37 |
| ${}^{199}$Fr | 199 | 112 | -108.9103 | -1071120.13 ± 8.9666 | 187014.3663 | 185374.0980 | +8848422.29 ± 74.04 | ±0.37 |
| ${}^{200}$Fr | 200 | 113 | -102.2548 | -1066396.36 ± 19.8173 | 187947.2762 | 186304.9543 | +8815234.76 ± 163.84 | ±0.37 |
| ${}^{201}$Fr | 201 | 114 | -95.6089 | -1061656.00 ± 5.8588 | 188880.1957 | 187233.9034 | +8792704.16 ± 48.49 | ±0.37 |
| ${}^{202}$Fr | 202 | 115 | -88.9724 | -1057061.40 ± 3.8736 | 189813.1248 | 188164.9105 | +8759413.54 ± 32.06 | ±0.37 |
| ${}^{203}$Fr | 203 | 116 | -82.3454 | -1052464.79 ± 3.9707 | 190746.0632 | 189094.1795 | +8735772.29 ± 32.95 | ±0.37 |
| ${}^{204}$Fr | 204 | 117 | -75.7277 | -1047993.40 ± 15.5792 | 191679.0109 | 190025.4045 | +8702027.98 ± 129.36 | ±0.38 |
| ${}^{205}$Fr | 205 | 118 | -69.1192 | -1043529.59 ± 4.9318 | 192611.9677 | 190954.9814 | +8677366.11 ± 40.97 | ±0.38 |
| ${}^{206}$Fr | 206 | 119 | -62.5197 | -1039175.83 ± 17.4262 | 193544.9337 | 191886.5385 | +8642582.20 ± 144.93 | ±0.38 |
| ${}^{207}$Fr | 207 | 120 | -55.9292 | -1034834.97 ± 10.9331 | 194477.9086 | 192816.4304 | +8616891.08 ± 91.05 | ±0.38 |
| ${}^{208}$Fr | 208 | 121 | -49.3476 | -1030585.43 ± 7.2194 | 195410.8925 | 193748.1086 | +8582193.74 ± 60.16 | ±0.38 |
| ${}^{209}$Fr | 209 | 122 | -42.7748 | -1026361.50 ± 7.0842 | 196343.8851 | 194678.4855 | +8554615.16 ± 59.09 | ±0.38 |
| ${}^{210}$Fr | 210 | 123 | -36.2107 | -1022211.64 ± 8.2312 | 197276.8864 | 195610.4183 | +8519321.68 ± 68.61 | ±0.38 |
| ${}^{211}$Fr | 211 | 124 | -29.6551 | -1018092.06 ± 7.3117 | 198209.8962 | 196541.1156 | +8490745.89 ± 61.01 | ±0.38 |
| ${}^{212}$Fr | 212 | 125 | -23.1081 | -1014034.07 ± 5.3303 | 199142.9146 | 197473.2340 | +8455225.06 ± 44.43 | ±0.39 |
| ${}^{213}$Fr | 213 | 126 | -16.5695 | -1010013.69 ± 2.8448 | 200075.9414 | 198404.6899 | +8423447.72 ± 23.72 | ±0.39 |
| ${}^{214}$Fr | 214 | 127 | -10.0392 | -1006047.12 ± 5.1304 | 201008.9765 | 199338.7799 | +8378684.14 ± 42.73 | ±0.39 |
| ${}^{215}$Fr | 215 | 128 | -3.5171 | -1002109.89 ± 4.2434 | 201942.0199 | 200271.5504 | +8341022.22 ± 35.28 | ±0.39 |
| ${}^{216}$Fr | 216 | 129 | 2.9968 | -998208.02 ± 2.4928 | 202875.0714 | 201205.6974 | +8296852.29 ± 20.74 | ±0.39 |
| ${}^{217}$Fr | 217 | 130 | 9.5027 | -994340.57 ± 3.8900 | 203808.1309 | 202138.5352 | +8259660.89 ± 32.31 | ±0.39 |
| ${}^{218}$Fr | 218 | 131 | 16.0006 | -990500.83 ± 2.5108 | 204741.1984 | 203072.7741 | +8215894.02 ± 20.85 | ±0.39 |
| ${}^{219}$Fr | 219 | 132 | 22.4906 | -986699.30 ± 4.0667 | 205674.2738 | 204005.8257 | +8178434.06 ± 33.70 | ±0.39 |
| ${}^{220}$Fr | 220 | 133 | 28.9729 | -982918.39 ± 2.3736 | 206607.3571 | 204940.1851 | +8134919.50 ± 19.65 | ±0.40 |
| ${}^{221}$Fr | 221 | 134 | 35.4473 | -979178.26 ± 2.8689 | 207540.4480 | 205873.4742 | +8097079.17 ± 23.73 | ±0.40 |
| ${}^{222}$Fr | 222 | 135 | 41.9142 | -975451.31 ± 4.3688 | 208473.5466 | 206808.0691 | +8053251.75 ± 36.03 | ±0.40 |
| ${}^{223}$Fr | 223 | 136 | 48.3735 | -971768.50 ± 1.1323 | 209406.6527 | 207741.5675 | +8015176.17 ± 9.30 | ±0.40 |
| ${}^{224}$Fr | 224 | 137 | 54.8253 | -968090.76 ± 6.5056 | 210339.7664 | 208676.4278 | +7970897.93 ± 53.57 | ±0.40 |
| ${}^{225}$Fr | 225 | 138 | 61.2696 | -964464.11 ± 6.9425 | 211272.8874 | 209609.9939 | +7933273.75 ± 57.09 | ±0.40 |
| ${}^{226}$Fr | 226 | 139 | 67.7067 | -960829.99 ± 3.6086 | 212206.0158 | 210545.1880 | +7888224.95 ± 29.59 | ±0.40 |
| ${}^{227}$Fr | 227 | 140 | 74.1364 | -957256.33 ± 3.4028 | 213139.1514 | 211478.8440 | +7850938.70 ± 27.89 | ±0.40 |
| ${}^{228}$Fr | 228 | 141 | 80.5590 | -953670.07 ± 3.8682 | 214072.2943 | 212414.0399 | +7806708.05 ± 31.69 | ±0.40 |
| ${}^{229}$Fr | 229 | 142 | 86.9745 | -950146.43 ± 2.8615 | 215005.4442 | 213347.8180 | +7769595.33 ± 23.44 | ±0.41 |
| ${}^{230}$Fr | 230 | 143 | 93.3829 | -946603.30 ± 3.7350 | 215938.6012 | 214283.1306 | +7725622.56 ± 30.52 | ±0.41 |
| ${}^{231}$Fr | 231 | 144 | 99.7844 | -943121.08 ± 4.4111 | 216871.7652 | 215217.2185 | +7687798.70 ± 35.92 | ±0.41 |
| ${}^{232}$Fr | 232 | 145 | 106.1789 | -939616.47 ± 7.9426 | 217804.9361 | 216152.7049 | +7643814.45 ± 64.64 | ±0.41 |
| ${}^{233}$Fr | 233 | 146 | 112.5666 | -936173.44 ± 11.0975 | 218738.1138 | 217087.0462 | +7605555.45 ± 90.11 | ±0.41 |

### Radium (Z = 88)

_35 of 35 isotopes with a framework prediction; 35 of 35 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{201}$Ra | 201 | 113 | -119.2941 | -1077385.73 ± 13.1692 | 188903.0986 | 187242.2517 | +8870043.80 ± 108.42 | ±0.37 |
| ${}^{202}$Ra | 202 | 114 | -112.6237 | -1072544.15 ± 9.6675 | 189835.9937 | 188170.8839 | +8848923.82 ± 79.81 | ±0.37 |
| ${}^{203}$Ra | 203 | 115 | -105.9629 | -1067880.14 ± 6.2030 | 190768.8983 | 189101.9044 | +8815320.66 ± 51.23 | ±0.37 |
| ${}^{204}$Ra | 204 | 116 | -99.3116 | -1063189.76 ± 5.6723 | 191701.8125 | 190030.8583 | +8793067.69 ± 46.96 | ±0.37 |
| ${}^{205}$Ra | 205 | 117 | -92.6698 | -1058652.87 ± 14.4151 | 192634.7360 | 190962.0951 | +8759020.40 ± 119.25 | ±0.37 |
| ${}^{206}$Ra | 206 | 118 | -86.0372 | -1054101.93 ± 11.3215 | 193567.6688 | 191891.3510 | +8735765.59 ± 93.84 | ±0.38 |
| ${}^{207}$Ra | 207 | 119 | -79.4138 | -1049683.23 ± 36.4684 | 194500.6109 | 192822.7935 | +8701343.77 ± 302.27 | ±0.38 |
| ${}^{208}$Ra | 208 | 120 | -72.7995 | -1045266.00 ± 5.6130 | 195433.5620 | 193752.5015 | +8676329.17 ± 46.57 | ±0.38 |
| ${}^{209}$Ra | 209 | 121 | -66.1942 | -1040956.65 ± 3.5562 | 196366.5221 | 194684.1259 | +8641671.06 ± 29.52 | ±0.38 |
| ${}^{210}$Ra | 210 | 122 | -59.5977 | -1036660.02 ± 5.6579 | 197299.4911 | 195614.2046 | +8615358.35 ± 46.99 | ±0.38 |
| ${}^{211}$Ra | 211 | 123 | -53.0101 | -1032454.44 ± 3.0357 | 198232.4689 | 196546.0878 | +8580079.86 ± 25.27 | ±0.38 |
| ${}^{212}$Ra | 212 | 124 | -46.4312 | -1028269.09 ± 6.2472 | 199165.4554 | 197476.5512 | +8552428.82 ± 51.92 | ±0.38 |
| ${}^{213}$Ra | 213 | 125 | -39.8608 | -1024158.11 ± 5.9511 | 200098.4505 | 198408.5896 | +8517074.91 ± 49.48 | ±0.38 |
| ${}^{214}$Ra | 214 | 126 | -33.2990 | -1020079.95 ± 3.1616 | 201031.4541 | 199339.8309 | +8486127.11 ± 26.34 | ±0.39 |
| ${}^{215}$Ra | 215 | 127 | -26.7456 | -1016073.54 ± 4.3285 | 201964.4661 | 200273.7643 | +8441953.55 ± 35.95 | ±0.39 |
| ${}^{216}$Ra | 216 | 128 | -20.2006 | -1012086.99 ± 4.7949 | 202897.4865 | 201206.0179 | +8406650.17 ± 39.78 | ±0.39 |
| ${}^{217}$Ra | 217 | 129 | -13.6638 | -1008149.01 ± 4.2061 | 203830.5151 | 202140.1100 | +8362541.40 ± 34.86 | ±0.39 |
| ${}^{218}$Ra | 218 | 130 | -7.1351 | -1004236.86 ± 5.8252 | 204763.5518 | 203072.3602 | +8328024.94 ± 48.29 | ±0.39 |
| ${}^{219}$Ra | 219 | 131 | -0.6145 | -1000363.76 ± 4.0316 | 205696.5967 | 204006.6026 | +8284016.77 ± 33.40 | ±0.39 |
| ${}^{220}$Ra | 220 | 132 | 5.8981 | -996523.53 ± 4.4737 | 206629.6495 | 204938.9749 | +8249648.96 ± 37.06 | ±0.39 |
| ${}^{221}$Ra | 221 | 133 | 12.4028 | -992712.62 ± 2.7269 | 207562.7102 | 205873.1608 | +8206749.41 ± 22.49 | ±0.39 |
| ${}^{222}$Ra | 222 | 134 | 18.8996 | -988938.95 ± 2.6115 | 208495.7788 | 206806.0112 | +8170785.52 ± 21.53 | ±0.40 |
| ${}^{223}$Ra | 223 | 135 | 25.3888 | -985185.90 ± 1.2231 | 209428.8551 | 207740.4184 | +8127627.39 ± 10.06 | ±0.40 |
| ${}^{224}$Ra | 224 | 136 | 31.8702 | -981474.06 ± 1.0547 | 210361.9390 | 208673.5051 | +8091271.48 ± 8.68 | ±0.40 |
| ${}^{225}$Ra | 225 | 137 | 38.3441 | -977774.20 ± 1.4998 | 211295.0306 | 209608.1664 | +8047702.71 ± 12.38 | ±0.40 |
| ${}^{226}$Ra | 226 | 138 | 44.8105 | -974121.98 ± 1.1094 | 212228.1296 | 210541.3350 | +8011702.89 ± 9.15 | ±0.40 |
| ${}^{227}$Ra | 227 | 139 | 51.2694 | -970469.73 ± 1.1244 | 213161.2361 | 211476.3390 | +7967307.94 ± 9.20 | ±0.40 |
| ${}^{228}$Ra | 228 | 140 | 57.7210 | -966874.11 ± 1.1515 | 214094.3500 | 212409.5958 | +7931629.04 ± 9.39 | ±0.40 |
| ${}^{229}$Ra | 229 | 141 | 64.1653 | -963269.54 ± 8.8353 | 215027.4711 | 213344.7117 | +7887513.85 ± 72.37 | ±0.40 |
| ${}^{230}$Ra | 230 | 142 | 70.6024 | -959725.74 ± 5.8778 | 215960.5994 | 214278.1602 | +7851659.98 ± 48.05 | ±0.40 |
| ${}^{231}$Ra | 231 | 143 | 77.0323 | -956167.15 ± 6.4670 | 216893.7349 | 215213.3544 | +7807974.76 ± 52.83 | ±0.41 |
| ${}^{232}$Ra | 232 | 144 | 83.4552 | -952668.37 ± 5.1842 | 217826.8774 | 216147.1290 | +7771319.54 ± 42.33 | ±0.41 |
| ${}^{233}$Ra | 233 | 145 | 89.8711 | -949151.71 ± 4.8645 | 218760.0270 | 217082.4602 | +7727785.71 ± 39.63 | ±0.41 |
| ${}^{234}$Ra | 234 | 146 | 96.2801 | -945693.80 ± 4.7251 | 219693.1834 | 218016.5509 | +7690391.03 ± 38.45 | ±0.41 |
| ${}^{235}$Ra | 235 | 147 | 102.6822 | -942210.63 ± 132.2576 | 220626.3468 | 218952.2441 | +7645971.74 ± 1369.89 | ±0.41 |

### Actinium (Z = 89)

_33 of 33 isotopes with a framework prediction; 33 of 33 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{205}$Ac | 205 | 116 | -116.4616 | -1074137.60 ± 37.7666 | 192657.7455 | 190970.3980 | +8835649.83 ± 310.62 | ±0.37 |
| ${}^{206}$Ac | 206 | 117 | -109.7955 | -1069509.41 ± 41.2110 | 193590.6449 | 191901.2701 | +8803353.58 ± 339.17 | ±0.37 |
| ${}^{207}$Ac | 207 | 118 | -103.1388 | -1064867.70 ± 35.3725 | 194523.5536 | 192830.4257 | +8780398.05 ± 291.69 | ±0.37 |
| ${}^{208}$Ac | 208 | 119 | -96.4915 | -1060365.85 ± 40.3392 | 195456.4716 | 193761.5344 | +8747542.21 ± 332.79 | ±0.37 |
| ${}^{209}$Ac | 209 | 120 | -89.8533 | -1055863.90 ± 34.7200 | 196389.3989 | 194691.1126 | +8722978.04 ± 286.84 | ±0.38 |
| ${}^{210}$Ac | 210 | 121 | -83.2242 | -1051481.51 ± 38.4774 | 197322.3352 | 195622.5259 | +8689231.08 ± 318.00 | ±0.38 |
| ${}^{211}$Ac | 211 | 122 | -76.6041 | -1047103.99 ± 33.0588 | 198255.2805 | 196552.3994 | +8663751.52 ± 273.48 | ±0.38 |
| ${}^{212}$Ac | 212 | 123 | -69.9929 | -1042830.29 ± 13.3879 | 199188.2347 | 197484.0496 | +8629482.53 ± 110.81 | ±0.38 |
| ${}^{213}$Ac | 213 | 124 | -63.3905 | -1038572.28 ± 7.1025 | 200121.1978 | 198414.3851 | +8602262.64 ± 58.79 | ±0.38 |
| ${}^{214}$Ac | 214 | 125 | -56.7968 | -1034397.29 ± 8.2039 | 201054.1695 | 199346.1715 | +8568000.24 ± 67.97 | ±0.38 |
| ${}^{215}$Ac | 215 | 126 | -50.2117 | -1030253.97 ± 7.4747 | 201987.1499 | 200277.2628 | +8537599.29 ± 61.94 | ±0.38 |
| ${}^{216}$Ac | 216 | 127 | -43.6352 | -1026197.47 ± 5.5374 | 202920.1387 | 201210.8761 | +8494881.79 ± 45.87 | ±0.39 |
| ${}^{217}$Ac | 217 | 128 | -37.0671 | -1022154.14 ± 6.7053 | 203853.1361 | 202142.9228 | +8460416.07 ± 55.52 | ±0.39 |
| ${}^{218}$Ac | 218 | 129 | -30.5073 | -1018169.20 ± 34.3151 | 204786.1417 | 203076.5655 | +8418382.80 ± 283.71 | ±0.39 |
| ${}^{219}$Ac | 219 | 130 | -23.9558 | -1014205.13 ± 30.5303 | 205719.1556 | 204008.7783 | +8383842.03 ± 252.33 | ±0.39 |
| ${}^{220}$Ac | 220 | 131 | -17.4125 | -1010289.13 ± 3.6270 | 206652.1777 | 204942.4466 | +8342494.11 ± 29.90 | ±0.39 |
| ${}^{221}$Ac | 221 | 132 | -10.8772 | -1006399.87 ± 33.4829 | 207585.2079 | 205874.7280 | +8308353.09 ± 276.39 | ±0.39 |
| ${}^{222}$Ac | 222 | 133 | -4.3500 | -1002550.44 ± 2.7594 | 208518.2461 | 206808.3128 | +8268203.71 ± 22.72 | ±0.39 |
| ${}^{223}$Ac | 223 | 134 | 2.1693 | -998733.20 ± 4.0630 | 209451.2922 | 207741.0102 | +8232760.58 ± 33.44 | ±0.39 |
| ${}^{224}$Ac | 224 | 135 | 8.6808 | -994947.47 ± 2.3859 | 210384.3461 | 208674.9134 | +8191845.94 ± 19.59 | ±0.39 |
| ${}^{225}$Ac | 225 | 136 | 15.1845 | -991196.25 ± 2.7525 | 211317.4078 | 209607.8106 | +8156171.16 ± 22.70 | ±0.40 |
| ${}^{226}$Ac | 226 | 137 | 21.6806 | -987469.17 ± 1.7895 | 212250.4772 | 210541.9766 | +8114774.02 ± 14.72 | ±0.40 |
| ${}^{227}$Ac | 227 | 138 | 28.1690 | -983780.25 ± 1.1110 | 213183.5542 | 211475.0111 | +8079172.66 ± 9.11 | ±0.40 |
| ${}^{228}$Ac | 228 | 139 | 34.6499 | -980106.10 ± 1.2043 | 214116.6387 | 212409.5503 | +8036777.97 ± 9.85 | ±0.40 |
| ${}^{229}$Ac | 229 | 140 | 41.1234 | -976474.20 ± 6.9302 | 215049.7307 | 213342.8397 | +8000694.89 ± 56.76 | ±0.40 |
| ${}^{230}$Ac | 230 | 141 | 47.5895 | -972851.56 ± 9.0403 | 215982.8300 | 214277.4822 | +7958595.24 ± 73.90 | ±0.40 |
| ${}^{231}$Ac | 231 | 142 | 54.0483 | -969274.75 ± 7.4195 | 216915.9366 | 215210.9008 | +7922627.59 ± 60.60 | ±0.40 |
| ${}^{232}$Ac | 232 | 143 | 60.4998 | -965698.43 ± 7.3924 | 217849.0505 | 216145.7865 | +7880162.94 ± 60.33 | ±0.40 |
| ${}^{233}$Ac | 233 | 144 | 66.9442 | -962171.58 ± 7.3731 | 218782.1715 | 217079.4342 | +7843844.51 ± 60.07 | ±0.40 |
| ${}^{234}$Ac | 234 | 145 | 73.3815 | -958640.09 ± 7.8738 | 219715.2997 | 218014.4615 | +7801492.51 ± 64.09 | ±0.41 |
| ${}^{235}$Ac | 235 | 146 | 79.8118 | -955156.21 ± 7.8563 | 220648.4348 | 218948.4715 | +7764216.14 ± 63.82 | ±0.41 |
| ${}^{236}$Ac | 236 | 147 | 86.2351 | -951661.41 ± 21.4043 | 221581.5769 | 219883.8295 | +7721110.78 ± 173.69 | ±0.41 |
| ${}^{237}$Ac | 237 | 148 | 92.6516 | -948220.54 ± 264.9007 | 222514.7259 | 220818.1227 | +7683260.40 ± 1809.68 | ±0.41 |

### Thorium (Z = 90)

_32 of 32 isotopes with a framework prediction; 32 of 32 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{208}$Th | 208 | 118 | -120.4235 | -1075655.52 ± 20.0194 | 195479.6214 | 193767.4616 | +8836157.25 ± 164.45 | ±0.37 |
| ${}^{209}$Th | 209 | 119 | -113.7521 | -1071090.44 ± 0.0000 | 196412.5154 | 194698.6629 | +8802589.77 ± 531.06 | ±0.37 |
| ${}^{210}$Th | 210 | 120 | -107.0900 | -1066494.61 ± 11.7354 | 197345.4187 | 195627.8213 | +8779923.73 ± 96.65 | ±0.37 |
| ${}^{211}$Th | 211 | 121 | -100.4370 | -1062045.64 ± 53.1684 | 198278.3311 | 196559.1323 | +8746471.57 ± 437.88 | ±0.38 |
| ${}^{212}$Th | 212 | 122 | -93.7932 | -1057591.40 ± 6.2093 | 199211.2527 | 197488.8609 | +8721463.35 ± 51.19 | ±0.38 |
| ${}^{213}$Th | 213 | 123 | -87.1584 | -1053253.83 ± 5.6352 | 200144.1833 | 198420.3642 | +8687712.79 ± 46.45 | ±0.38 |
| ${}^{214}$Th | 214 | 124 | -80.5325 | -1048921.53 ± 6.4740 | 201077.1228 | 199350.4331 | +8661579.95 ± 53.48 | ±0.38 |
| ${}^{215}$Th | 215 | 125 | -73.9154 | -1044688.83 ± 3.8346 | 202010.0712 | 200282.1537 | +8627415.84 ± 31.63 | ±0.38 |
| ${}^{216}$Th | 216 | 126 | -67.3070 | -1040480.65 ± 6.6774 | 202943.0282 | 201213.0249 | +8597869.13 ± 55.18 | ±0.38 |
| ${}^{217}$Th | 217 | 127 | -60.7072 | -1036376.48 ± 6.3584 | 203875.9939 | 202146.4263 | +8556013.60 ± 52.50 | ±0.38 |
| ${}^{218}$Th | 218 | 128 | -54.1160 | -1032273.96 ± 6.2666 | 204808.9681 | 203078.0814 | +8523257.11 ± 51.78 | ±0.38 |
| ${}^{219}$Th | 219 | 129 | -47.5332 | -1028247.43 ± 33.5513 | 205741.9507 | 204011.6715 | +8481275.59 ± 276.74 | ±0.39 |
| ${}^{220}$Th | 220 | 130 | -40.9588 | -1024227.53 ± 8.0942 | 206674.9417 | 204943.3924 | +8448915.25 ± 66.78 | ±0.39 |
| ${}^{221}$Th | 221 | 131 | -34.3926 | -1020273.78 ± 4.7160 | 207607.9410 | 205877.1368 | +8406975.94 ± 38.83 | ±0.39 |
| ${}^{222}$Th | 222 | 132 | -27.8347 | -1016332.82 ± 5.9922 | 208540.9484 | 206808.8941 | +8375144.54 ± 49.39 | ±0.39 |
| ${}^{223}$Th | 223 | 133 | -21.2848 | -1012446.48 ± 4.6423 | 209473.9640 | 207742.5705 | +8334321.99 ± 38.23 | ±0.39 |
| ${}^{224}$Th | 224 | 134 | -14.7430 | -1008583.63 ± 5.5949 | 210406.9876 | 208674.6748 | +8301499.80 ± 46.02 | ±0.39 |
| ${}^{225}$Th | 225 | 135 | -8.2091 | -1004763.51 ± 2.9507 | 211340.0191 | 209608.4835 | +8260808.64 ± 24.30 | ±0.39 |
| ${}^{226}$Th | 226 | 136 | -1.6830 | -1000972.56 ± 2.5858 | 212273.0585 | 210540.8651 | +8227349.99 ± 21.28 | ±0.39 |
| ${}^{227}$Th | 227 | 137 | 4.8353 | -997214.67 ± 1.2030 | 213206.1056 | 211474.9663 | +8186024.80 ± 9.87 | ±0.40 |
| ${}^{228}$Th | 228 | 138 | 11.3458 | -993490.93 ± 1.0333 | 214139.1605 | 212407.4265 | +8152887.82 ± 8.50 | ±0.40 |
| ${}^{229}$Th | 229 | 139 | 17.8488 | -989790.98 ± 1.3753 | 215072.2229 | 213341.7353 | +8111341.48 ± 11.27 | ±0.40 |
| ${}^{230}$Th | 230 | 140 | 24.3442 | -986129.69 ± 0.6945 | 216005.2929 | 214274.5064 | +8077426.52 ± 5.64 | ±0.40 |
| ${}^{231}$Th | 231 | 141 | 30.8321 | -982484.20 ± 0.6955 | 216938.3704 | 215208.9538 | +8035988.41 ± 5.65 | ±0.40 |
| ${}^{232}$Th | 232 | 142 | 37.3127 | -978879.87 ± 0.8010 | 217871.4553 | 216142.0788 | +8001109.92 ± 6.57 | ±0.40 |
| ${}^{233}$Th | 233 | 143 | 43.7859 | -975282.79 ± 0.8023 | 218804.5475 | 217076.8578 | +7958884.75 ± 6.56 | ±0.40 |
| ${}^{234}$Th | 234 | 144 | 50.2519 | -971731.51 ± 1.4611 | 219737.6470 | 218010.2332 | +7923544.23 ± 11.87 | ±0.40 |
| ${}^{235}$Th | 235 | 145 | 56.7107 | -968181.73 ± 7.3177 | 220670.7536 | 218945.1321 | +7881524.64 ± 59.56 | ±0.40 |
| ${}^{236}$Th | 236 | 146 | 63.1624 | -964677.55 ± 7.8132 | 221603.8673 | 219878.8637 | +7845245.39 ± 63.55 | ±0.41 |
| ${}^{237}$Th | 237 | 147 | 69.6070 | -961168.42 ± 8.8320 | 222536.9881 | 220814.0577 | +7802630.14 ± 71.71 | ±0.41 |
| ${}^{238}$Th | 238 | 148 | 76.0447 | -957708.09 ± 132.3627 | 223470.1159 | 221748.1218 | +7765540.77 ± 1277.01 | ±0.41 |
| ${}^{239}$Th | 239 | 149 | 82.4754 | -954232.69 ± 265.2520 | 224403.2505 | 222683.5906 | +7722436.78 ± 1794.52 | ±0.41 |

### Protactinium (Z = 91)

_31 of 31 isotopes with a framework prediction; 31 of 31 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{211}$Pa | 211 | 120 | -124.5090 | -1077344.27 ± 43.1620 | 198301.6208 | 196567.3081 | +8822996.39 ± 353.42 | ±0.37 |
| ${}^{212}$Pa | 212 | 121 | -117.8322 | -1072810.99 ± 54.1289 | 199234.5094 | 197498.3465 | +8790771.53 ± 443.57 | ±0.37 |
| ${}^{213}$Pa | 213 | 122 | -111.1645 | -1068268.50 ± 35.1088 | 200167.4072 | 198427.8983 | +8766453.12 ± 288.11 | ±0.38 |
| ${}^{214}$Pa | 214 | 123 | -104.5060 | -1063855.23 ± 49.6227 | 201100.3141 | 199359.1981 | +8733562.29 ± 407.34 | ±0.38 |
| ${}^{215}$Pa | 215 | 124 | -97.8565 | -1059439.00 ± 50.0824 | 202033.2300 | 200289.0368 | +8708380.53 ± 411.65 | ±0.38 |
| ${}^{216}$Pa | 216 | 125 | -91.2159 | -1055135.78 ± 14.8971 | 202966.1548 | 201220.5502 | +8675081.24 ± 122.48 | ±0.38 |
| ${}^{217}$Pa | 217 | 126 | -84.5842 | -1050855.43 ± 7.5150 | 203899.0885 | 202151.2753 | +8646065.78 ± 61.82 | ±0.38 |
| ${}^{218}$Pa | 218 | 127 | -77.9611 | -1046691.58 ± 10.6930 | 204832.0309 | 203084.3642 | +8605619.11 ± 87.87 | ±0.38 |
| ${}^{219}$Pa | 219 | 128 | -71.3467 | -1042522.92 ± 41.5460 | 205764.9819 | 204015.7919 | +8573796.82 ± 341.66 | ±0.38 |
| ${}^{220}$Pa | 220 | 129 | -64.7409 | -1038439.72 ± 8.6996 | 206697.9415 | 204948.9812 | +8533637.14 ± 71.50 | ±0.38 |
| ${}^{221}$Pa | 221 | 130 | -58.1435 | -1034359.84 ± 35.0922 | 207630.9095 | 205880.5719 | +8501713.41 ± 288.41 | ±0.39 |
| ${}^{222}$Pa | 222 | 131 | -51.5544 | -1030351.59 ± 50.9852 | 208563.8859 | 206813.7554 | +8462350.51 ± 418.76 | ±0.39 |
| ${}^{223}$Pa | 223 | 132 | -44.9737 | -1026356.32 ± 44.3289 | 209496.8706 | 207745.5227 | +8430255.37 ± 364.06 | ±0.39 |
| ${}^{224}$Pa | 224 | 133 | -38.4012 | -1022418.55 ± 4.4331 | 210429.8634 | 208678.5416 | +8392438.60 ± 36.36 | ±0.39 |
| ${}^{225}$Pa | 225 | 134 | -31.8367 | -1018504.39 ± 47.5895 | 211362.8644 | 209610.5300 | +8359954.29 ± 390.56 | ±0.39 |
| ${}^{226}$Pa | 226 | 135 | -25.2803 | -1014639.22 ± 6.4912 | 212295.8735 | 210543.7010 | +8322131.71 ± 53.25 | ±0.39 |
| ${}^{227}$Pa | 227 | 136 | -18.7319 | -1010801.68 ± 4.1888 | 213228.8904 | 211475.9919 | +8288877.14 ± 34.34 | ±0.39 |
| ${}^{228}$Pa | 228 | 137 | -12.1913 | -1007005.93 ± 2.4895 | 214161.9153 | 212409.5792 | +8249797.58 ± 20.43 | ±0.39 |
| ${}^{229}$Pa | 229 | 138 | -5.6585 | -1003238.55 ± 1.8742 | 215094.9479 | 213342.0466 | +8216389.35 ± 15.37 | ±0.39 |
| ${}^{230}$Pa | 230 | 139 | 0.8665 | -999505.70 ± 1.7319 | 216027.9883 | 214275.8174 | +8177175.10 ± 14.18 | ±0.40 |
| ${}^{231}$Pa | 231 | 140 | 7.3840 | -995804.23 ± 1.0107 | 216961.0363 | 215208.5623 | +8143142.42 ± 8.23 | ±0.40 |
| ${}^{232}$Pa | 232 | 141 | 13.8938 | -992129.95 ± 4.3367 | 217894.0918 | 216142.5786 | +8103508.46 ± 35.36 | ±0.40 |
| ${}^{233}$Pa | 233 | 142 | 20.3962 | -988489.30 ± 0.7495 | 218827.1549 | 217075.6156 | +8068798.00 ± 6.15 | ±0.40 |
| ${}^{234}$Pa | 234 | 143 | 26.8912 | -984868.42 ± 2.3042 | 219760.2253 | 218009.9591 | +8028377.21 ± 18.78 | ±0.40 |
| ${}^{235}$Pa | 235 | 144 | 33.3788 | -981282.33 ± 7.8409 | 220693.3031 | 218943.4033 | +7992475.79 ± 63.82 | ±0.40 |
| ${}^{236}$Pa | 236 | 145 | 39.8591 | -977711.20 ± 7.8125 | 221626.3882 | 219877.9424 | +7951892.50 ± 63.55 | ±0.40 |
| ${}^{237}$Pa | 237 | 146 | 46.3323 | -974176.35 ± 7.2652 | 222559.4805 | 220811.6302 | +7915571.55 ± 59.06 | ±0.40 |
| ${}^{238}$Pa | 238 | 147 | 52.7983 | -970649.43 ± 8.7982 | 223492.5799 | 221746.4907 | +7874258.25 ± 71.41 | ±0.40 |
| ${}^{239}$Pa | 239 | 148 | 59.2573 | -967160.47 ± 132.4503 | 224425.6863 | 222680.4281 | +7837501.46 ± 878.45 | ±0.41 |
| ${}^{240}$Pa | 240 | 149 | 65.7093 | -963674.06 ± 132.6788 | 225358.7998 | 223615.5951 | +7795541.49 ± 895.60 | ±0.41 |
| ${}^{241}$Pa | 241 | 150 | 72.1543 | -960229.09 ± 132.8374 | 226291.9202 | 224549.8194 | +7758192.46 ± 1335.74 | ±0.41 |

### Uranium (Z = 92)

_29 of 29 isotopes with a framework prediction; 29 of 29 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{215}$U | 215 | 123 | -122.0352 | -1074481.29 ± 63.5630 | 202056.6263 | 200296.1216 | +8789509.85 ± 519.91 | ±0.37 |
| ${}^{216}$U | 216 | 124 | -115.3621 | -1069985.87 ± 17.0482 | 202989.5186 | 201225.7928 | +8764909.13 ± 139.60 | ±0.38 |
| ${}^{217}$U | 217 | 125 | -108.6979 | -1065615.95 ± 0.0000 | 203922.4199 | 202157.1912 | +8731961.28 ± 396.27 | ±0.38 |
| ${}^{218}$U | 218 | 126 | -102.0427 | -1061262.03 ± 8.2322 | 204855.3301 | 203087.6093 | +8704228.06 ± 67.52 | ±0.38 |
| ${}^{219}$U | 219 | 127 | -95.3964 | -1057043.41 ± 7.9751 | 205788.2492 | 204020.5047 | +8664543.37 ± 65.38 | ±0.38 |
| ${}^{220}$U | 220 | 128 | -88.7587 | -1052807.42 ± 0.0000 | 206721.1770 | 204951.7163 | +8633548.83 ± 490.85 | ±0.38 |
| ${}^{221}$U | 221 | 129 | -82.1297 | -1048676.23 ± 42.7523 | 207654.1134 | 205884.7169 | +8594112.76 ± 350.37 | ±0.38 |
| ${}^{222}$U | 222 | 130 | -75.5093 | -1044532.91 ± 30.6634 | 208587.0584 | 206815.9639 | +8563625.76 ± 251.40 | ±0.38 |
| ${}^{223}$U | 223 | 131 | -68.8973 | -1040483.00 ± 34.6971 | 209520.0118 | 207749.2304 | +8523648.53 ± 284.25 | ±0.38 |
| ${}^{224}$U | 224 | 132 | -62.2937 | -1036423.61 ± 8.9194 | 210452.9737 | 208680.4219 | +8494096.97 ± 73.13 | ±0.39 |
| ${}^{225}$U | 225 | 133 | -55.6984 | -1032445.09 ± 5.7931 | 211385.9438 | 209613.5453 | +8455553.07 ± 47.39 | ±0.39 |
| ${}^{226}$U | 226 | 134 | -49.1114 | -1028473.44 ± 6.4204 | 212318.9221 | 210544.9962 | +8425400.42 ± 52.58 | ±0.39 |
| ${}^{227}$U | 227 | 135 | -42.5324 | -1024568.61 ± 4.9172 | 213251.9086 | 211478.2066 | +8387162.25 ± 40.24 | ±0.39 |
| ${}^{228}$U | 228 | 136 | -35.9615 | -1020678.65 ± 7.7483 | 214184.9031 | 212409.8756 | +8356614.65 ± 63.43 | ±0.39 |
| ${}^{229}$U | 229 | 137 | -29.3986 | -1016845.91 ± 3.3986 | 215117.9056 | 213343.3604 | +8317789.86 ± 27.83 | ±0.39 |
| ${}^{230}$U | 230 | 138 | -22.8435 | -1013032.49 ± 2.5719 | 216050.9160 | 214275.2589 | +8286804.18 ± 21.04 | ±0.39 |
| ${}^{231}$U | 231 | 139 | -16.2963 | -1009266.12 ± 1.5236 | 216983.9342 | 215208.9439 | +8247753.17 ± 12.40 | ±0.39 |
| ${}^{232}$U | 232 | 140 | -9.7568 | -1005524.90 ± 1.0247 | 217916.9601 | 216141.2415 | +8215547.15 ± 8.37 | ±0.40 |
| ${}^{233}$U | 233 | 141 | -3.2249 | -1001820.20 ± 1.2757 | 218849.9936 | 217075.0453 | +8176657.77 ± 10.38 | ±0.40 |
| ${}^{234}$U | 234 | 142 | 3.2994 | -998144.92 ± 0.6315 | 219783.0348 | 218007.7652 | +8143148.22 ± 5.18 | ±0.40 |
| ${}^{235}$U | 235 | 143 | 9.8162 | -994497.25 ± 0.6323 | 220716.0834 | 218942.0332 | +8102830.88 ± 5.10 | ±0.40 |
| ${}^{236}$U | 236 | 144 | 16.3255 | -990881.70 ± 0.6195 | 221649.1395 | 219875.0531 | +8068611.78 ± 5.05 | ±0.40 |
| ${}^{237}$U | 237 | 145 | 22.8275 | -987286.53 ± 0.6732 | 222582.2029 | 220809.4927 | +8028233.78 ± 5.44 | ±0.40 |
| ${}^{238}$U | 238 | 146 | 29.3222 | -983725.18 ± 0.8322 | 223515.2737 | 221742.9044 | +7992901.77 ± 6.73 | ±0.40 |
| ${}^{239}$U | 239 | 147 | 35.8097 | -980177.29 ± 0.8335 | 224448.3516 | 222677.6635 | +7951799.63 ± 6.74 | ±0.40 |
| ${}^{240}$U | 240 | 148 | 42.2900 | -976666.63 ± 1.4036 | 225381.4367 | 223611.3004 | +7916130.90 ± 11.41 | ±0.40 |
| ${}^{241}$U | 241 | 149 | 48.7632 | -973161.29 ± 132.6436 | 226314.5289 | 224546.2760 | +7874781.48 ± 871.15 | ±0.40 |
| ${}^{242}$U | 242 | 150 | 55.2295 | -969699.83 ± 132.7669 | 227247.6281 | 225480.1930 | +7838538.30 ± 888.20 | ±0.41 |
| ${}^{243}$U | 243 | 151 | 61.6887 | -966232.62 ± 133.0141 | 228180.7342 | 226415.5472 | +7796227.23 ± 1324.74 | ±0.41 |

### Neptunium (Z = 93)

_27 of 27 isotopes with a framework prediction; 27 of 27 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{219}$Np | 219 | 126 | -119.6821 | -1071862.87 ± 55.2160 | 205811.7526 | 204026.6457 | +8749381.32 ± 450.77 | ±0.38 |
| ${}^{220}$Np | 220 | 127 | -113.0123 | -1067572.65 ± 18.3634 | 206744.6482 | 204959.1778 | +8711346.39 ± 149.87 | ±0.38 |
| ${}^{221}$Np | 221 | 128 | -106.3514 | -1063261.20 ± 131.4579 | 207677.5527 | 205890.1072 | +8681551.26 ± 972.71 | ±0.38 |
| ${}^{222}$Np | 222 | 129 | -99.6992 | -1059070.51 ± 22.5446 | 208610.4659 | 206822.9657 | +8642658.59 ± 183.98 | ±0.38 |
| ${}^{223}$Np | 223 | 130 | -93.0557 | -1054851.97 ± 48.8461 | 209543.3878 | 207753.8437 | +8613771.41 ± 398.85 | ±0.38 |
| ${}^{224}$Np | 224 | 131 | -86.4207 | -1050740.64 ± 16.9790 | 210476.3183 | 208686.7115 | +8575566.64 ± 138.60 | ±0.38 |
| ${}^{225}$Np | 225 | 132 | -79.7942 | -1046617.73 ± 53.5267 | 211409.2572 | 209617.7914 | +8546344.10 ± 437.07 | ±0.38 |
| ${}^{226}$Np | 226 | 133 | -73.1761 | -1042580.31 ± 59.3885 | 212342.2045 | 210550.4843 | +8509694.10 ± 484.74 | ±0.39 |
| ${}^{227}$Np | 227 | 134 | -66.5663 | -1038547.77 ± 44.5889 | 213275.1602 | 211481.7406 | +8480257.42 ± 364.05 | ±0.39 |
| ${}^{228}$Np | 228 | 135 | -59.9647 | -1034587.48 ± 0.0000 | 214208.1240 | 212414.4810 | +8444071.29 ± 473.61 | ±0.39 |
| ${}^{229}$Np | 229 | 136 | -53.3713 | -1030641.95 ± 58.0858 | 215141.0960 | 213345.9511 | +8414243.95 ± 474.24 | ±0.39 |
| ${}^{230}$Np | 230 | 137 | -46.7859 | -1026759.15 ± 31.4663 | 216074.0761 | 214278.8805 | +8377846.61 ± 256.70 | ±0.39 |
| ${}^{231}$Np | 231 | 138 | -40.2085 | -1022896.59 ± 29.1234 | 217007.0641 | 215210.7616 | +8346712.96 ± 237.69 | ±0.39 |
| ${}^{232}$Np | 232 | 139 | -33.6391 | -1019085.94 ± 0.0000 | 217940.0600 | 216143.9915 | +8309592.71 ± 461.13 | ±0.39 |
| ${}^{233}$Np | 233 | 140 | -27.0774 | -1015298.73 ± 28.8039 | 218873.0638 | 217076.0747 | +8278153.63 ± 234.85 | ±0.39 |
| ${}^{234}$Np | 234 | 141 | -20.5235 | -1011556.17 ± 4.7301 | 219806.0753 | 218009.5751 | +8240464.77 ± 38.51 | ±0.39 |
| ${}^{235}$Np | 235 | 142 | -13.9772 | -1007839.34 ± 0.7776 | 220739.0945 | 218942.1574 | +8207359.77 ± 6.34 | ±0.40 |
| ${}^{236}$Np | 236 | 143 | -7.4386 | -1004158.66 ± 28.1823 | 221672.1212 | 219875.9866 | +8168853.28 ± 229.31 | ±0.40 |
| ${}^{237}$Np | 237 | 144 | -0.9074 | -1000505.46 ± 0.6205 | 222605.1555 | 220808.9742 | +8134548.72 ± 5.07 | ±0.40 |
| ${}^{238}$Np | 238 | 145 | 5.6162 | -996881.19 ± 0.6344 | 223538.1973 | 221743.0513 | +8095613.31 ± 5.12 | ±0.40 |
| ${}^{239}$Np | 239 | 146 | 12.1325 | -993285.72 ± 0.7275 | 224471.2464 | 222676.4018 | +8060326.97 ± 5.88 | ±0.40 |
| ${}^{240}$Np | 240 | 147 | 18.6415 | -989712.41 ± 9.4038 | 225404.3028 | 223610.9011 | +8020189.08 ± 76.17 | ±0.40 |
| ${}^{241}$Np | 241 | 148 | 25.1433 | -986170.67 ± 55.0103 | 226337.3665 | 224544.3941 | +7984934.96 ± 445.37 | ±0.40 |
| ${}^{242}$Np | 242 | 149 | 31.6379 | -982645.95 ± 109.7114 | 227270.4373 | 225478.9900 | +7945074.40 ± 887.01 | ±0.40 |
| ${}^{243}$Np | 243 | 150 | 38.1254 | -979153.00 ± 0.0000 | 228203.5153 | 226412.8729 | +7908748.24 ± 139.88 | ±0.40 |
| ${}^{244}$Np | 244 | 151 | 44.6058 | -975670.65 ± 0.0000 | 229136.6002 | 227347.8014 | +7868115.92 ± 438.40 | ±0.41 |
| ${}^{245}$Np | 245 | 152 | 51.0793 | -972223.96 ± 133.2268 | 230069.6922 | 228281.9055 | +7831486.42 ± 877.30 | ±0.41 |

### Plutonium (Z = 94)

_27 of 27 isotopes with a framework prediction; 27 of 27 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{221}$Pu | 221 | 127 | -130.8085 | -1078127.44 ± 131.9958 | 207701.2275 | 205896.1265 | +8767046.67 ± 1456.76 | ±0.38 |
| ${}^{222}$Pu | 222 | 128 | -124.1242 | -1073742.79 ± 131.8913 | 208634.1086 | 206826.7506 | +8738511.74 ± 1450.20 | ±0.38 |
| ${}^{223}$Pu | 223 | 129 | -117.4487 | -1069482.30 ± 131.9261 | 209566.9986 | 207759.3057 | +8700899.71 ± 1443.70 | ±0.38 |
| ${}^{224}$Pu | 224 | 130 | -110.7820 | -1065194.12 ± 131.8218 | 210499.8973 | 208689.9596 | +8672854.76 ± 1437.26 | ±0.38 |
| ${}^{225}$Pu | 225 | 131 | -104.1240 | -1061027.73 ± 131.8739 | 211432.8047 | 209622.4737 | +8636149.44 ± 1430.86 | ±0.38 |
| ${}^{226}$Pu | 226 | 132 | -97.4745 | -1056840.17 ± 131.7870 | 212365.7206 | 210553.2971 | +8607908.63 ± 951.17 | ±0.38 |
| ${}^{227}$Pu | 227 | 133 | -90.8335 | -1052755.15 ± 0.0000 | 213298.6451 | 211485.9313 | +8571320.70 ± 471.28 | ±0.38 |
| ${}^{228}$Pu | 228 | 134 | -84.2010 | -1048653.87 ± 13.4907 | 214231.5779 | 212416.7635 | +8543650.00 ± 109.93 | ±0.38 |
| ${}^{229}$Pu | 229 | 135 | -77.5767 | -1044651.14 ± 34.9023 | 215164.5191 | 213349.5447 | +8507046.22 ± 284.19 | ±0.39 |
| ${}^{230}$Pu | 230 | 136 | -70.9607 | -1040643.50 ± 8.2730 | 216097.4685 | 214280.5760 | +8479034.96 ± 67.44 | ±0.39 |
| ${}^{231}$Pu | 231 | 137 | -64.3529 | -1036717.98 ± 12.5871 | 217030.4261 | 215213.4465 | +8442685.98 ± 102.51 | ±0.39 |
| ${}^{232}$Pu | 232 | 138 | -57.7531 | -1032802.24 ± 9.5929 | 217963.3917 | 216144.9930 | +8412865.45 ± 78.12 | ±0.39 |
| ${}^{233}$Pu | 233 | 139 | -51.1613 | -1028953.35 ± 30.6575 | 218896.3654 | 217078.1780 | +8375726.04 ± 249.58 | ±0.39 |
| ${}^{234}$Pu | 234 | 140 | -44.5774 | -1025116.89 ± 3.8367 | 219829.3469 | 218009.9703 | +8345382.72 ± 31.18 | ±0.39 |
| ${}^{235}$Pu | 235 | 141 | -38.0014 | -1021336.65 ± 11.5189 | 220762.3363 | 218943.2967 | +8308267.87 ± 93.73 | ±0.39 |
| ${}^{236}$Pu | 236 | 142 | -31.4331 | -1017576.20 ± 1.0161 | 221695.3334 | 219875.5100 | +8276608.14 ± 8.23 | ±0.39 |
| ${}^{237}$Pu | 237 | 143 | -24.8725 | -1013862.18 ± 0.9510 | 222628.3383 | 220809.1942 | +8238533.78 ± 7.68 | ±0.40 |
| ${}^{238}$Pu | 238 | 144 | -18.3195 | -1010170.33 ± 0.6342 | 223561.3507 | 221741.7598 | +8205900.68 ± 5.13 | ±0.40 |
| ${}^{239}$Pu | 239 | 145 | -11.7741 | -1006516.11 ± 0.6217 | 224494.3707 | 222675.6790 | +8167446.36 ± 4.99 | ±0.40 |
| ${}^{240}$Pu | 240 | 146 | -5.2361 | -1002887.36 ± 0.6088 | 225427.3981 | 223608.7102 | +8133350.02 ± 4.94 | ±0.40 |
| ${}^{241}$Pu | 241 | 147 | 1.2945 | -999288.23 ± 0.6096 | 226360.4330 | 224543.0341 | +8093766.33 ± 4.92 | ±0.40 |
| ${}^{242}$Pu | 242 | 148 | 7.8178 | -995716.30 ± 0.6895 | 227293.4751 | 225476.2900 | +8059318.12 ± 5.52 | ±0.40 |
| ${}^{243}$Pu | 243 | 149 | 14.3338 | -992167.50 ± 1.3942 | 228226.5245 | 226410.8218 | +8019505.29 ± 11.22 | ±0.40 |
| ${}^{244}$Pu | 244 | 150 | 20.8426 | -988648.18 ± 1.2758 | 229159.5812 | 227344.3673 | +7984424.03 ± 10.32 | ±0.40 |
| ${}^{245}$Pu | 245 | 151 | 27.3443 | -985145.08 ± 7.4002 | 230092.6449 | 228279.2336 | +7943829.47 ± 59.66 | ±0.40 |
| ${}^{246}$Pu | 246 | 152 | 33.8389 | -981675.11 ± 8.1129 | 231025.7157 | 229212.9443 | +7908678.05 ± 65.38 | ±0.40 |
| ${}^{247}$Pu | 247 | 153 | 40.3266 | -978210.94 ± 133.4579 | 231958.7934 | 230148.2536 | +7866841.39 ± 870.18 | ±0.41 |

### Americium (Z = 95)

_27 of 27 isotopes with a framework prediction; 27 of 27 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{223}$Am | 223 | 128 | -142.0765 | -1084419.55 ± 132.5030 | 209590.8440 | 207765.8848 | +8783728.84 ± 1443.65 | ±0.38 |
| ${}^{224}$Am | 224 | 129 | -135.3777 | -1080090.76 ± 265.0411 | 210523.7107 | 208697.9397 | +8748390.09 ± 1914.78 | ±0.38 |
| ${}^{225}$Am | 225 | 130 | -128.6878 | -1075724.33 ± 264.7954 | 211456.5862 | 209628.5638 | +8720292.56 ± 1906.28 | ±0.38 |
| ${}^{226}$Am | 226 | 131 | -122.0067 | -1071484.70 ± 132.4153 | 212389.4704 | 210560.6373 | +8685541.61 ± 1424.49 | ±0.38 |
| ${}^{227}$Am | 227 | 132 | -115.3342 | -1067224.14 ± 132.3101 | 213322.3634 | 211491.3415 | +8657668.47 ± 946.95 | ±0.38 |
| ${}^{228}$Am | 228 | 133 | -108.6703 | -1063070.53 ± 132.3276 | 214255.2649 | 212423.5053 | +8623149.26 ± 942.79 | ±0.38 |
| ${}^{229}$Am | 229 | 134 | -102.0149 | -1058905.88 ± 61.4077 | 215188.1749 | 213354.3302 | +8595301.32 ± 498.46 | ±0.38 |
| ${}^{230}$Am | 230 | 135 | -95.3679 | -1054832.45 ± 132.2401 | 216121.0934 | 214286.5159 | +8561329.56 ± 665.08 | ±0.38 |
| ${}^{231}$Am | 231 | 136 | -88.7292 | -1050767.80 ± 132.1702 | 217054.0201 | 215217.5480 | +8533096.77 ± 1393.66 | ±0.39 |
| ${}^{232}$Am | 232 | 137 | -82.0988 | -1046784.00 ± 132.2052 | 217986.9551 | 216150.0518 | +8498278.47 ± 1387.65 | ±0.39 |
| ${}^{233}$Am | 233 | 138 | -75.4766 | -1042808.74 ± 0.0000 | 218919.8983 | 217081.4108 | +8469115.17 ± 527.79 | ±0.39 |
| ${}^{234}$Am | 234 | 139 | -68.8624 | -1038905.84 ± 132.2052 | 219852.8496 | 218014.0814 | +8434171.49 ± 734.89 | ±0.39 |
| ${}^{235}$Am | 235 | 140 | -62.2563 | -1035018.46 ± 29.6887 | 220785.8088 | 218945.7390 | +8404227.77 ± 241.06 | ±0.39 |
| ${}^{236}$Am | 236 | 141 | -55.6580 | -1031191.52 ± 132.2576 | 221718.7760 | 219878.6494 | +8368827.99 ± 538.02 | ±0.39 |
| ${}^{237}$Am | 237 | 142 | -49.0677 | -1027382.16 ± 0.0000 | 222651.7511 | 220810.6726 | +8337814.60 ± 269.99 | ±0.39 |
| ${}^{238}$Am | 238 | 143 | -42.4851 | -1023626.05 ± 32.7572 | 223584.7339 | 221744.0181 | +8301084.35 ± 265.67 | ±0.39 |
| ${}^{239}$Am | 239 | 144 | -35.9102 | -1019891.17 ± 1.0988 | 224517.7244 | 222676.4811 | +8268692.20 ± 8.90 | ±0.39 |
| ${}^{240}$Am | 240 | 145 | -29.3429 | -1016200.05 ± 7.6322 | 225450.7226 | 223610.0950 | +8231415.41 ± 61.86 | ±0.40 |
| ${}^{241}$Am | 241 | 146 | -22.7832 | -1012532.48 ± 0.6098 | 226383.7283 | 224543.0133 | +8197605.14 ± 4.96 | ±0.40 |
| ${}^{242}$Am | 242 | 147 | -16.2309 | -1008901.14 ± 0.6105 | 227316.7415 | 225477.0411 | +8159147.20 ± 4.95 | ±0.40 |
| ${}^{243}$Am | 243 | 148 | -9.6861 | -1005293.45 ± 0.7570 | 228249.7621 | 226410.2422 | +8124720.23 ± 6.13 | ±0.40 |
| ${}^{244}$Am | 244 | 149 | -3.1486 | -1001715.69 ± 0.8110 | 229182.7900 | 227344.4404 | +8086186.68 ± 6.56 | ±0.40 |
| ${}^{245}$Am | 245 | 150 | 3.3816 | -998163.44 ± 1.0246 | 230115.8252 | 228277.9558 | +8051015.75 ± 8.26 | ±0.40 |
| ${}^{246}$Am | 246 | 151 | 9.9046 | -994635.25 ± 0.0000 | 231048.8677 | 229212.5436 | +8011446.74 ± 77.21 | ±0.40 |
| ${}^{247}$Am | 247 | 152 | 16.4204 | -991134.89 ± 0.0000 | 231981.9172 | 230146.1969 | +7976322.72 ± 433.07 | ±0.40 |
| ${}^{248}$Am | 248 | 153 | 22.9292 | -987651.06 ± 133.5648 | 232914.9739 | 231081.1003 | +7936060.53 ± 866.67 | ±0.40 |
| ${}^{249}$Am | 249 | 154 | 29.4310 | -984196.18 ± 133.7077 | 233848.0375 | 232015.1355 | +7899924.35 ± 1284.74 | ±0.40 |

### Curium (Z = 96)

_22 of 22 isotopes with a framework prediction; 22 of 22 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{231}$Cm | 231 | 135 | -113.3376 | -1065054.25 ± 132.5908 | 217077.8462 | 215222.4076 | +8621029.11 ± 1393.63 | ±0.38 |
| ${}^{232}$Cm | 232 | 136 | -106.6763 | -1060918.33 ± 132.4854 | 218010.7503 | 216152.9646 | +8594773.06 ± 930.83 | ±0.38 |
| ${}^{233}$Cm | 233 | 137 | -100.0233 | -1056888.98 ± 46.1171 | 218943.6627 | 217085.4195 | +8559962.96 ± 373.56 | ±0.38 |
| ${}^{234}$Cm | 234 | 138 | -93.3785 | -1052849.94 ± 9.6680 | 219876.5833 | 218016.3427 | +8532574.25 ± 78.33 | ±0.39 |
| ${}^{235}$Cm | 235 | 139 | -86.7419 | -1048908.77 ± 0.0000 | 220809.5121 | 218949.1282 | +8496877.44 ± 467.98 | ±0.39 |
| ${}^{236}$Cm | 236 | 140 | -80.1134 | -1044960.22 ± 9.8936 | 221742.4491 | 219880.4613 | +8468182.07 ± 80.20 | ±0.39 |
| ${}^{237}$Cm | 237 | 141 | -73.4929 | -1041090.79 ± 41.5948 | 222675.3940 | 220813.3497 | +8432661.78 ± 336.93 | ±0.39 |
| ${}^{238}$Cm | 238 | 142 | -66.8804 | -1037229.76 ± 6.8098 | 223608.3469 | 221745.0419 | +8402916.32 ± 55.17 | ±0.39 |
| ${}^{239}$Cm | 239 | 143 | -60.2757 | -1033434.65 ± 83.2420 | 224541.3077 | 222678.2378 | +8366645.73 ± 673.93 | ±0.39 |
| ${}^{240}$Cm | 240 | 144 | -53.6789 | -1029652.13 ± 1.0473 | 225474.2762 | 223610.3091 | +8335783.43 ± 8.52 | ±0.39 |
| ${}^{241}$Cm | 241 | 145 | -47.0897 | -1025925.02 ± 0.8890 | 226407.2525 | 224543.7808 | +8298923.78 ± 7.16 | ±0.39 |
| ${}^{242}$Cm | 242 | 146 | -40.5082 | -1022216.35 ± 0.6238 | 227340.2364 | 225476.3768 | +8266318.72 ± 5.06 | ±0.39 |
| ${}^{243}$Cm | 243 | 147 | -33.9342 | -1018553.00 ± 0.8237 | 228273.2279 | 226410.2491 | +8228332.14 ± 6.60 | ±0.40 |
| ${}^{244}$Cm | 244 | 148 | -27.3678 | -1014907.47 ± 0.5981 | 229206.2268 | 227343.0131 | +8195605.73 ± 4.86 | ±0.40 |
| ${}^{245}$Cm | 245 | 149 | -20.8088 | -1011300.74 ± 0.6254 | 230139.2332 | 228277.0599 | +8157513.99 ± 5.03 | ±0.40 |
| ${}^{246}$Cm | 246 | 150 | -14.2571 | -1007715.63 ± 0.8254 | 231072.2470 | 229210.1664 | +8123900.48 ± 6.65 | ±0.40 |
| ${}^{247}$Cm | 247 | 151 | -7.7127 | -1004162.35 ± 2.0528 | 232005.2681 | 230144.5767 | +8084880.22 ± 16.50 | ±0.40 |
| ${}^{248}$Cm | 248 | 152 | -1.1756 | -1000632.31 ± 1.2672 | 232938.2963 | 231077.9305 | +8050815.85 ± 10.20 | ±0.40 |
| ${}^{249}$Cm | 249 | 153 | 5.3544 | -997127.32 ± 1.2691 | 233871.3318 | 232012.7825 | +8010546.76 ± 10.22 | ±0.40 |
| ${}^{250}$Cm | 250 | 154 | 11.8773 | -993647.60 ± 5.4954 | 234804.3743 | 232946.5155 | +7975473.53 ± 44.10 | ±0.40 |
| ${}^{251}$Cm | 251 | 155 | 18.3932 | -990185.84 ± 12.1071 | 235737.4238 | 233881.6680 | +7934592.88 ± 97.05 | ±0.40 |
| ${}^{252}$Cm | 252 | 156 | 24.9021 | -986753.64 ± 134.0483 | 236670.4803 | 234815.5700 | +7899434.86 ± 1269.41 | ±0.41 |

### Berkelium (Z = 97)

_22 of 22 isotopes with a framework prediction; 22 of 22 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{233}$Bk | 233 | 136 | -124.8013 | -1071236.61 ± 132.9964 | 218967.6584 | 217090.8972 | +8645048.03 ± 1072.70 | ±0.38 |
| ${}^{234}$Bk | 234 | 137 | -118.1256 | -1067137.97 ± 132.9964 | 219900.5481 | 218023.0154 | +8611626.41 ± 700.68 | ±0.38 |
| ${}^{235}$Bk | 235 | 138 | -111.4583 | -1063037.03 ± 265.8161 | 220833.4462 | 218953.8844 | +8584281.43 ± 1829.35 | ±0.38 |
| ${}^{236}$Bk | 236 | 139 | -104.7992 | -1059027.58 ± 265.8514 | 221766.3526 | 219886.1498 | +8550801.09 ± 1639.43 | ±0.39 |
| ${}^{237}$Bk | 237 | 140 | -98.1483 | -1055019.00 ± 132.8551 | 222699.2671 | 220817.3123 | +8522677.65 ± 1041.94 | ±0.39 |
| ${}^{238}$Bk | 238 | 141 | -91.5056 | -1051093.30 ± 132.8904 | 223632.1897 | 221749.8134 | +8488739.35 ± 1155.18 | ±0.39 |
| ${}^{239}$Bk | 239 | 142 | -84.8708 | -1047177.89 ± 132.8551 | 224565.1204 | 222681.3401 | +8459533.86 ± 928.64 | ±0.39 |
| ${}^{240}$Bk | 240 | 143 | -78.2440 | -1043336.00 ± 132.9257 | 225498.0590 | 223614.2491 | +8424373.36 ± 670.67 | ±0.39 |
| ${}^{241}$Bk | 241 | 144 | -71.6251 | -1039500.21 ± 132.9080 | 226431.0055 | 224546.0599 | +8394472.03 ± 738.41 | ±0.39 |
| ${}^{242}$Bk | 242 | 145 | -65.0140 | -1035729.86 ± 132.9964 | 227363.9599 | 225479.3248 | +8358349.75 ± 594.89 | ±0.39 |
| ${}^{243}$Bk | 243 | 146 | -58.4106 | -1031975.10 ± 2.4742 | 228296.9219 | 226411.7568 | +8326268.46 ± 19.98 | ±0.39 |
| ${}^{244}$Bk | 244 | 147 | -51.8149 | -1028270.89 ± 7.8546 | 229229.8916 | 227345.2751 | +8289666.31 ± 63.33 | ±0.39 |
| ${}^{245}$Bk | 245 | 148 | -45.2267 | -1024582.81 ± 0.9721 | 230162.8689 | 228277.8692 | +8257478.95 ± 7.85 | ±0.40 |
| ${}^{246}$Bk | 246 | 149 | -38.6461 | -1020938.58 ± 32.5212 | 231095.8537 | 229211.5164 | +8220953.67 ± 261.85 | ±0.40 |
| ${}^{247}$Bk | 247 | 150 | -32.0729 | -1017315.77 ± 2.8004 | 232028.8459 | 230144.5331 | +8187519.21 ± 22.54 | ±0.40 |
| ${}^{248}$Bk | 248 | 151 | -25.5071 | -1013730.73 ± 26.9404 | 232961.8455 | 231078.6688 | +8149505.01 ± 216.63 | ±0.40 |
| ${}^{249}$Bk | 249 | 152 | -18.9486 | -1010165.45 ± 0.6679 | 233894.8525 | 232011.8782 | +8115853.05 ± 5.38 | ±0.40 |
| ${}^{250}$Bk | 250 | 153 | -12.3974 | -1006633.20 ± 1.5516 | 234827.8666 | 232946.4779 | +8076484.84 ± 12.44 | ±0.40 |
| ${}^{251}$Bk | 251 | 154 | -5.8533 | -1003122.11 ± 5.7301 | 235760.8880 | 233880.2480 | +8041037.98 ± 45.89 | ±0.40 |
| ${}^{252}$Bk | 252 | 155 | 0.6837 | -999636.27 ± 134.0662 | 236693.9164 | 234815.0484 | +8001480.42 ± 852.89 | ±0.40 |
| ${}^{253}$Bk | 253 | 156 | 7.2136 | -996173.36 ± 134.2102 | 237626.9519 | 235748.9364 | +7966167.26 ± 1521.22 | ±0.40 |
| ${}^{254}$Bk | 254 | 157 | 13.7366 | -992731.05 ± 134.4086 | 238559.9944 | 236683.8957 | +7926600.42 ± 1259.39 | ±0.40 |

### Californium (Z = 98)

_20 of 20 isotopes with a framework prediction; 20 of 20 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{237}$Cf | 237 | 139 | -123.0338 | -1069186.44 ± 54.7355 | 222723.3703 | 220822.0408 | +8610233.96 ± 440.84 | ±0.38 |
| ${}^{238}$Cf | 238 | 140 | -116.3605 | -1065109.83 ± 133.1735 | 223656.2624 | 221752.8743 | +8583375.08 ± 1344.19 | ±0.39 |
| ${}^{239}$Cf | 239 | 141 | -109.6954 | -1061139.79 ± 133.2090 | 224589.1626 | 222685.2924 | +8549600.24 ± 539.61 | ±0.39 |
| ${}^{240}$Cf | 240 | 142 | -103.0383 | -1057165.47 ± 9.9997 | 225522.0710 | 223616.5736 | +8521270.99 ± 80.65 | ±0.39 |
| ${}^{241}$Cf | 241 | 143 | -96.3894 | -1053277.72 ± 133.2090 | 226454.9875 | 224549.4059 | +8486246.55 ± 746.69 | ±0.39 |
| ${}^{242}$Cf | 242 | 144 | -89.7483 | -1049388.21 ± 7.0981 | 227387.9119 | 225480.9601 | +8457263.10 ± 57.18 | ±0.39 |
| ${}^{243}$Cf | 243 | 145 | -83.1152 | -1045574.68 ± 133.2445 | 228320.8442 | 226414.0568 | +8421682.97 ± 798.14 | ±0.39 |
| ${}^{244}$Cf | 244 | 146 | -76.4899 | -1041769.16 ± 1.4257 | 229253.7843 | 227346.0394 | +8391370.73 ± 11.51 | ±0.39 |
| ${}^{245}$Cf | 245 | 147 | -69.8724 | -1038027.48 ± 1.3201 | 230186.7322 | 228279.4406 | +8355073.94 ± 10.63 | ±0.39 |
| ${}^{246}$Cf | 246 | 148 | -63.2625 | -1034292.62 ± 0.8268 | 231119.6877 | 229211.6397 | +8324393.82 ± 6.60 | ±0.39 |
| ${}^{247}$Cf | 247 | 149 | -56.6602 | -1030613.29 ± 7.7403 | 232052.6508 | 230145.1530 | +8288238.07 ± 62.25 | ±0.39 |
| ${}^{248}$Cf | 248 | 150 | -50.0654 | -1026949.07 ± 2.7633 | 232985.6215 | 231077.7757 | +8256292.99 ± 22.16 | ±0.40 |
| ${}^{249}$Cf | 249 | 151 | -43.4781 | -1023333.11 ± 0.6414 | 233918.5996 | 232011.7546 | +8218743.31 ± 5.09 | ±0.40 |
| ${}^{250}$Cf | 250 | 152 | -36.8982 | -1019731.77 ± 0.8289 | 234851.5851 | 232944.6963 | +8186015.35 ± 6.60 | ±0.40 |
| ${}^{251}$Cf | 251 | 153 | -30.3256 | -1016172.84 ± 2.0748 | 235784.5780 | 233879.1550 | +8147040.50 ± 16.68 | ±0.40 |
| ${}^{252}$Cf | 252 | 154 | -23.7603 | -1012629.93 ± 1.2592 | 236717.5781 | 234812.5487 | +8112979.12 ± 10.04 | ±0.40 |
| ${}^{253}$Cf | 253 | 155 | -17.2021 | -1009120.62 ± 2.2536 | 237650.5853 | 235747.3098 | +8073371.17 ± 18.06 | ±0.40 |
| ${}^{254}$Cf | 254 | 156 | -10.6511 | -1005629.25 ± 6.0543 | 238583.5997 | 236680.8437 | +8039332.52 ± 48.42 | ±0.40 |
| ${}^{255}$Cf | 255 | 157 | -4.1072 | -1002165.44 ± 134.4447 | 239516.6212 | 237615.8053 | +7999535.01 ± 842.84 | ±0.40 |
| ${}^{256}$Cf | 256 | 158 | 2.4298 | -998722.91 ± 134.5533 | 240449.6497 | 238549.5312 | +7965299.47 ± 1319.83 | ±0.40 |

### Einsteinium (Z = 99)

_20 of 20 isotopes with a framework prediction; 20 of 20 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppm) | Mass $M_q$ (MeV) | Mass $M_o$ (MeV) | Mass Error (ppb) | CAL-3 Bound (ppb) |
|---|---|---|---|---|---|---|---|---|
| ${}^{239}$Es | 239 | 140 | -134.7494 | -1075364.93 ± 133.6720 | 224613.4343 | 222690.7212 | +8634006.76 ± 1346.90 | ±0.38 |
| ${}^{240}$Es | 240 | 141 | -128.0618 | -1071326.16 ± 267.3439 | 225546.3122 | 223622.8105 | +8601545.24 ± 1637.03 | ±0.38 |
| ${}^{241}$Es | 241 | 142 | -121.3825 | -1067289.48 ± 133.6005 | 226479.1983 | 224553.9720 | +8573556.78 ± 1028.75 | ±0.39 |
| ${}^{242}$Es | 242 | 143 | -114.7113 | -1063345.38 ± 133.6362 | 227412.0925 | 225486.3744 | +8540285.96 ± 1140.17 | ±0.39 |
| ${}^{243}$Es | 243 | 144 | -108.0481 | -1059396.52 ± 133.5827 | 228344.9947 | 226417.8135 | +8511614.85 ± 913.32 | ±0.39 |
| ${}^{244}$Es | 244 | 145 | -101.3929 | -1055531.83 ± 133.6362 | 229277.9050 | 227350.5865 | +8477296.85 ± 798.95 | ±0.39 |
| ${}^{245}$Es | 245 | 146 | -94.7456 | -1051665.57 ± 133.6005 | 230210.8231 | 228282.3703 | +8447663.94 ± 726.32 | ±0.39 |
| ${}^{246}$Es | 246 | 147 | -88.1062 | -1047876.67 ± 48.8585 | 231143.7491 | 229215.3683 | +8412964.41 ± 392.31 | ±0.39 |
| ${}^{247}$Es | 247 | 148 | -81.4745 | -1044097.82 ± 10.5212 | 232076.6828 | 230147.6220 | +8381840.94 ± 84.47 | ±0.39 |
| ${}^{248}$Es | 248 | 149 | -74.8504 | -1040371.36 ± 0.0000 | 233009.6242 | 231080.8367 | +8346808.66 ± 225.74 | ±0.39 |
| ${}^{249}$Es | 249 | 150 | -68.2340 | -1036664.74 ± 0.0000 | 233942.5732 | 232013.2064 | +8315763.01 ± 128.47 | ±0.39 |
| ${}^{250}$Es | 250 | 151 | -61.6252 | -1033003.17 ± 0.0000 | 234875.5298 | 232946.7516 | +8279910.05 ± 427.87 | ±0.40 |
| ${}^{251}$Es | 251 | 152 | -55.0238 | -1029362.67 ± 2.8262 | 235808.4938 | 233879.5316 | +8247674.38 ± 22.61 | ±0.40 |
| ${}^{252}$Es | 252 | 153 | -48.4298 | -1025771.16 ± 26.6318 | 236741.4652 | 234813.8087 | +8209297.87 ± 213.17 | ±0.40 |
| ${}^{253}$Es | 253 | 154 | -41.8432 | -1022191.14 ± 0.6575 | 237674.4440 | 235747.0187 | +8175820.48 ± 5.30 | ±0.40 |
| ${}^{254}$Es | 254 | 155 | -35.2638 | -1018651.51 ± 1.5584 | 238607.4301 | 236681.4965 | +8137237.68 ± 12.41 | ±0.40 |
| ${}^{255}$Es | 255 | 156 | -28.6917 | -1015127.58 ± 5.7006 | 239540.4234 | 237615.0857 | +8102758.55 ± 45.52 | ±0.40 |
| ${}^{256}$Es | 256 | 157 | -22.1266 | -1011635.99 ± 0.0000 | 240473.4238 | 238549.6756 | +8064350.32 ± 417.82 | ±0.40 |
| ${}^{257}$Es | 257 | 158 | -15.5687 | -1008162.03 ± 269.4691 | 241406.4312 | 239483.3885 | +8029962.85 ± 1715.31 | ±0.40 |
| ${}^{258}$Es | 258 | 159 | -9.0178 | -1004715.68 ± 269.8327 | 242339.4457 | 240418.1811 | +7991345.25 ± 1666.02 | ±0.40 |

<!-- AUTO:per-z-sections END -->
