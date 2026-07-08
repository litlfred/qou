This atlas identifies the specific knot or link for each confined braid at the substrate value $q_0$, verifying whether its invariant reproduces the measured mass or binding energy. A single $q_0$-indexed registry enables recursive construction of composite entries from nucleon and $\alpha$-cluster constituents, ensuring uniform comparison against the AME 2020 reference. We detail the precise identification mechanics below; a layered extension then applies this machinery to every isotope.

**Atlas (recursive, $q_0$-indexed).**
*The [confinement source of truth](#def:confined-particle) determines each entry. A particle or atom is identified by the Markov-equivalence class $[K]_M$ of its canonical Hecke element $T_w \in H_{n_0}(q_0)$, expressed in $\sigma_*$ generators of the braid group $B_{n_0}$. The [confinement SDP](#prop:confinement-sdp) verifies confinement at $q_0$.*

*Each entry occupies **two rows**: the first gives the braid word in normal form (NF, shortlex Gröbner–Shirshov); the second gives the prediction and AME residual. Composite entries reference earlier entries.*

## Methodology classification (STRICT)

Every entry carries a **methodology tag** recording its derivation method.

| Tag | Definition | Examples |
|---|---|---|
| `principled-derivation` | Knot is the closure of an explicit $\sigma$-braid word in $H_{n_0}(q_0)$ from [`def:confined-particle`](#def:confined-particle); $\mathrm{Vol}_{\mathrm{hyp}}$ computed at $\geq 50$ decimal digits via `hp_volume_of_link_closure(braid_word, digits=50)`. | electron $\sigma_1^3$ $\to$ $3_1$, proton/neutron $(\sigma_1 \sigma_2^{-1})^3$ $\to$ $\mathcal{B}_3$. |
| `principled-gb-nf` | Trivial-NF entries: a single strand (unknot $0_1$) or the pure identity $\mathbf{1}$. | neutrino ($0_1$), quark; the bare photon (identity $\mathbf{1}$, not the unknot). |
| `manual-historical-volume-match` | Knot was identified in earlier work via volume-match against AME; well-established but the GB-NF derivation in $H_{n_0}(q_0)$ has not been computed yet. | ${}^2$H = $6_2$, ${}^{3}$H = $8_{11}$, ${}^{3}$He = $L_{6a4}$. |
| `magic-A-formula` | Algebraic shell-closure formula $A \cdot 8G$ for double-magic light nuclei; no single hyperbolic knot. | ${}^{4}$He. |
| `recursive-on-⁴He` | Built from $n \cdot {}^{4}\mathrm{He} + n_{\alpha\alpha} \cdot c_{\alpha\alpha}$ recursion; principled given ${}^{4}$He. | ${}^{8}$Be–${}^{40}$Ca. |

The principled pipeline computes $\mathrm{Vol}_{\mathrm{hyp}}$ from the $\sigma$-braid word at $\geq 50$ decimal digits via SnapPy's `Link(braid_closure=...).exterior.high_precision` and `mpmath.workdps(50)`. The Wenzl bridge ([`y_lambda_wenzl_bridge_extended.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/y_lambda_wenzl_bridge_extended.py)) supplies symbolic-in-$q$ Markov-trace coefficients $y_\lambda$.

For atoms $A \geq 5$, the combinatorics of $\mathcal{H}_{3A}$ explode and `SnapPea` limits fail. We sidestep this by computing the exact symbolic trace restricted to active block-partitions (`closed_form_tau_M`). We show this exact trace $B_{sym} = -\alpha \ln |\tau_M|$ alongside the rigorous Q-CLT finite-sum approximation $B_{qCLT} = -\alpha \sum \ln |\hat{V}_i|$.

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

Word: $(\sigma_1 \sigma_2^{-1})^2$. Closure: the amphichiral **figure-eight knot**. Hyperbolic volume: $\mathrm{Vol}(4_1) = :val[Vol_4_1]{precision=6} \cdot \pi$ (smallest hyperbolic volume). Used for: the **Higgs field** (mass mechanism).

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
| Prediction | $m_\mathfrak{p} = 938.27208816$ MeV (CODATA exact); model derives via $\mathrm{Vol}(\mathcal{B}_3) = 8 G$ at $q_0$. |

**Neutron $\mathfrak{n}$**

| Row | Content |
|--:|---|
| Braid (NF) | $T_w = (\sigma_1 \sigma_2^{-1})^3$ with flavor coloring $\mathrm{udd}$. $\widehat{T_w} = \mathcal{B}_3(\mathrm{udd})$. |
| Prediction | $m_\mathfrak{n} = 939.56542052$ MeV; $m_\mathfrak{n} - m_\mathfrak{p}$ derived from flavor-flip cost (open). |

### $\ell = 2$ — light atoms (recursive: ref to nucleon entries above)

**Deuterium ${}^2$H = D = $[\mathfrak{p}, \mathfrak{n}]_{L_H}$**

| Row | Content |
|--:|---|
| Braid (NF) | $T_w = (\mathfrak{p}\text{-braid}) \oplus (\mathfrak{n}\text{-braid}) \oplus L_H$ in $H_6(q_0)$. Closure $\widehat{T_w} = K_{6_2}$ (hyperbolic, $\mathrm{Vol} = 4.4008$). |
| Prediction | $B_\mathrm{pred} = 1 \cdot m_e \cdot \mathrm{Vol}(K_{6_2}) = 2.249$ MeV vs $B_\mathrm{AME} = 2.225$. **err = +1.09%**. |

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

| Channel | Formula | Wire-format `ctype` |
|---|---|---|
| `pp` | $\sigma$ (positive crossing) | `sigma` |
| `nn` | $\sigma + (-h)\cdot\mathbf{1}$ | `sigma_inv` (underscore, matches `canonical_braid_crossings.atom_canonical_crossings`) |
| `pn` | $\sigma + (-h/2)\cdot\mathbf{1}$ (averaged half-shift) | `averaged` |

where $h = q_0 - q_0^{-1}$.

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

For an atom with mass number $A$, we build the canonical braid word in $B_{3A}$ sequentially per nucleon. At each $k \in \{0, \dots, A-1\}$, we apply the intra block at base $3k$ and $3k+1$. For $k < A-1$, we then apply the inter-nucleon interface at $3k+2$ between nucleon $k$ and $k+1$. The [`build_knot_operator_catalogue(Z, N)`](https://github.com/litlfred/qou/blob/main/computations/isotope_record_schema.py) function enumerates this sequence.

### Layer-1 canonical $|\mathrm{tr}_M(q_0)|$ table

<!-- AUTO:canonical-tr-m-table BEGIN -->

| Atom | $A$ | $n$ | $\|\mathrm{tr}_M(\beta_{\text{atom}}, q_0)\|$ | Predicting | Prediction (MeV) | Reference (MeV) | Error |
|---|---|---|---|---|---|---|---|
| D | 2 | 6 | $0.3882864715593036$ | B (binding) | 2.2488 | 2.2246 | +1.09 % |
| T | 3 | 9 | $0.1040710693020871$ | B (binding) | 8.4686 | 8.4818 | -0.16 % |
| ${}^3$He | 3 | 9 | $0.2065784750874029$ | B (binding) | 7.4889 | 7.7180 | -2.97 % |
| ${}^4$He | 4 | 12 | $0.0553584262667831$ | B (binding) | 29.9557 | 28.2957 | +5.87 % |
| ${}^5$Li | 5 | 15 | $0.0294467557534109$ | B (binding) | — | 26.3280 | — |
| ${}^6$Li | 6 | 18 | $0.0078910741135128$ | B (binding) | — | 31.9940 | — |
| ${}^7$Li | 7 | 21 | $0.0021146319542430$ | B (binding) | — | 39.2452 | — |

_Computed via [`canonical_mass_table_extended.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/canonical_mass_table_extended.py) (method=`branching`). Witness: [`canonical-mass-table-extended.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/canonical-mass-table-extended.witness.json). Nucleon masses (m_p, m_n) via [`m-p-borromean-verification-50dps.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/m-p-borromean-verification-50dps.witness.json). Paper hard floor (CAL-2 propagation): ~780 ppb._

<!-- AUTO:canonical-tr-m-table END -->

## Per-element stability summary ($Z = 1$ to $92$)

_This table summarizes element stability: predicted neutron count $N_{\mathrm{pred}}$, closed $\alpha$ sub-links $k_\alpha$, and predicted mass $M_q$ versus observed AME2020 mass $M_o$. The subsequent per-Z sections provide full isotope chains and layer attributions. See [knot-periodic-table intro](#prose:knot-periodic-table) for derivations and conventions._

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

_Auto-rendered from per-Z shards `canonical-isotope-witness-Z<NN>.witness.json` (emitted by [`canonical_isotope_witness.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/canonical_isotope_witness.py)). Each row carries the framework prediction, the AME 2020 reference, and the residual. For free nucleons (p, n) the prediction is the mass conditional on `conj:borromean-baryon-mass-formula`. For D and up, the prediction is the binding energy; the AME 2020 reference is the total binding energy. $M_{\mathrm{atom}}$ is the composite atomic mass $N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$.

### neutron (Z = 0)

_0 of 1 isotopes with a framework prediction; 1 of 1 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| $\mathfrak{n}$ | 1 | 1 | — | — | — | 939.5654 | +0.00 ppm |

### Hydrogen (Z = 1)

_2 of 7 isotopes with a framework prediction; 3 of 7 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| $\mathfrak{p}$ | 1 | 0 | — | — | — | 938.7831 | +0.01 ppm |
| ${}^{2}$H | 2 | 1 | 2.2488 | 2.2246 | +1.09 % | 1876.0997 | -12.92 ppm |
| ${}^{3}$H | 3 | 2 | 8.4686 | 8.4818 | -0.16 % | 2809.4453 | +4.70 ppm |
| ${}^{4}$H | 4 | 3 | — | 6.8818 | — | — | — |
| ${}^{5}$H | 5 | 4 | — | 6.6818 | — | — | — |
| ${}^{6}$H | 6 | 5 | — | 5.7698 | — | — | — |
| ${}^{7}$H | 7 | 6 | — | 6.5800 | — | — | — |

### Helium (Z = 2)

_2 of 8 isotopes with a framework prediction; 2 of 8 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{3}$He | 3 | 1 | 7.4889 | 7.7180 | -2.97 % | 2809.6427 | +81.57 ppm |
| ${}^{4}$He | 4 | 2 | 28.2957 | 28.2957 | +0.00 % | 3728.4013 | +0.00 ppm |
| ${}^{5}$He | 5 | 3 | — | 27.5607 | — | — | — |
| ${}^{6}$He | 6 | 4 | — | 29.2711 | — | — | — |
| ${}^{7}$He | 7 | 5 | — | 28.8614 | — | — | — |
| ${}^{8}$He | 8 | 6 | — | 31.3962 | — | — | — |
| ${}^{9}$He | 9 | 7 | — | 30.1413 | — | — | — |
| ${}^{10}$He | 10 | 8 | — | 29.9513 | — | — | — |

### Lithium (Z = 3)

_2 of 11 isotopes with a framework prediction; 0 of 11 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{3}$Li | 3 | 0 | — | -6.8010 | — | — | — |
| ${}^{4}$Li | 4 | 1 | — | 4.6150 | — | — | — |
| ${}^{5}$Li | 5 | 2 | — | 26.3307 | — | — | — |
| ${}^{6}$Li | 6 | 3 | 43.6570 | 31.9940 | +36.45 % | — | — |
| ${}^{7}$Li | 7 | 4 | 51.3377 | 39.2451 | +30.81 % | — | — |
| ${}^{8}$Li | 8 | 5 | — | 41.2777 | — | — | — |
| ${}^{9}$Li | 9 | 6 | — | 45.3399 | — | — | — |
| ${}^{10}$Li | 10 | 7 | — | 45.3135 | — | — | — |
| ${}^{11}$Li | 11 | 8 | — | 45.7092 | — | — | — |
| ${}^{12}$Li | 12 | 9 | — | 45.4992 | — | — | — |
| ${}^{13}$Li | 13 | 10 | — | 45.5992 | — | — | — |

### Beryllium (Z = 4)

_3 of 12 isotopes with a framework prediction; 1 of 12 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{5}$Be | 5 | 1 | — | 0.0900 | — | — | — |
| ${}^{6}$Be | 6 | 2 | — | 26.9235 | — | — | — |
| ${}^{7}$Be | 7 | 3 | — | 37.6008 | — | — | — |
| ${}^{8}$Be | 8 | 4 | 62.3383 | 56.4995 | +10.33 % | 7451.0557 | -783.01 ppm |
| ${}^{9}$Be | 9 | 5 | 67.3058 | 58.1640 | +15.72 % | — | — |
| ${}^{10}$Be | 10 | 6 | 75.5932 | 64.9763 | +16.34 % | — | — |
| ${}^{11}$Be | 11 | 7 | — | 65.4779 | — | — | — |
| ${}^{12}$Be | 12 | 8 | — | 68.6487 | — | — | — |
| ${}^{13}$Be | 13 | 9 | — | 68.1387 | — | — | — |
| ${}^{14}$Be | 14 | 10 | — | 69.9146 | — | — | — |
| ${}^{15}$Be | 15 | 11 | — | 68.1146 | — | — | — |
| ${}^{16}$Be | 16 | 12 | — | 68.5646 | — | — | — |

### Boron (Z = 5)

_2 of 16 isotopes with a framework prediction; 0 of 16 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{6}$B | 6 | 1 | — | -2.8020 | — | — | — |
| ${}^{7}$B | 7 | 2 | — | 24.9109 | — | — | — |
| ${}^{8}$B | 8 | 3 | — | 37.7372 | — | — | — |
| ${}^{9}$B | 9 | 4 | — | 56.3136 | — | — | — |
| ${}^{10}$B | 10 | 5 | 75.5932 | 64.7508 | +16.74 % | — | — |
| ${}^{11}$B | 11 | 6 | 83.8806 | 76.2051 | +10.07 % | — | — |
| ${}^{12}$B | 12 | 7 | — | 79.5747 | — | — | — |
| ${}^{13}$B | 13 | 8 | — | 84.4535 | — | — | — |
| ${}^{14}$B | 14 | 9 | — | 85.4230 | — | — | — |
| ${}^{15}$B | 15 | 10 | — | 88.2007 | — | — | — |
| ${}^{16}$B | 16 | 11 | — | 88.1177 | — | — | — |
| ${}^{17}$B | 17 | 12 | — | 89.5844 | — | — | — |
| ${}^{18}$B | 18 | 13 | — | 89.5794 | — | — | — |
| ${}^{19}$B | 19 | 14 | — | 89.6731 | — | — | — |
| ${}^{20}$B | 20 | 15 | — | 88.1131 | — | — | — |
| ${}^{21}$B | 21 | 16 | — | 87.2031 | — | — | — |

### Carbon (Z = 6)

_2 of 16 isotopes with a framework prediction; 1 of 16 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{8}$C | 8 | 2 | — | 24.8122 | — | — | — |
| ${}^{9}$C | 9 | 3 | — | 39.0368 | — | — | — |
| ${}^{10}$C | 10 | 4 | — | 60.3204 | — | — | — |
| ${}^{11}$C | 11 | 5 | — | 73.4410 | — | — | — |
| ${}^{12}$C | 12 | 6 | 97.1480 | 92.1617 | +5.41 % | 11172.9431 | -446.07 ppm |
| ${}^{13}$C | 13 | 7 | 101.0622 | 97.1080 | +4.07 % | — | — |
| ${}^{14}$C | 14 | 8 | — | 105.2845 | — | — | — |
| ${}^{15}$C | 15 | 9 | — | 106.5025 | — | — | — |
| ${}^{16}$C | 16 | 10 | — | 110.7529 | — | — | — |
| ${}^{17}$C | 17 | 11 | — | 111.4864 | — | — | — |
| ${}^{18}$C | 18 | 12 | — | 115.6704 | — | — | — |
| ${}^{19}$C | 19 | 13 | — | 116.2472 | — | — | — |
| ${}^{20}$C | 20 | 14 | — | 119.2287 | — | — | — |
| ${}^{21}$C | 21 | 15 | — | 119.1540 | — | — | — |
| ${}^{22}$C | 22 | 16 | — | 119.2637 | — | — | — |
| ${}^{23}$C | 23 | 17 | — | 116.7710 | — | — | — |

### Nitrogen (Z = 7)

_2 of 16 isotopes with a framework prediction; 0 of 16 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{10}$N | 10 | 3 | — | 36.4367 | — | — | — |
| ${}^{11}$N | 11 | 4 | — | 58.9424 | — | — | — |
| ${}^{12}$N | 12 | 5 | — | 74.0413 | — | — | — |
| ${}^{13}$N | 13 | 6 | — | 94.1052 | — | — | — |
| ${}^{14}$N | 14 | 7 | 109.9563 | 104.6586 | +5.06 % | — | — |
| ${}^{15}$N | 15 | 8 | 118.8505 | 115.4919 | +2.91 % | — | — |
| ${}^{16}$N | 16 | 9 | — | 117.9808 | — | — | — |
| ${}^{17}$N | 17 | 10 | — | 123.8659 | — | — | — |
| ${}^{18}$N | 18 | 11 | — | 126.6941 | — | — | — |
| ${}^{19}$N | 19 | 12 | — | 132.0224 | — | — | — |
| ${}^{20}$N | 20 | 13 | — | 134.1834 | — | — | — |
| ${}^{21}$N | 21 | 14 | — | 138.7893 | — | — | — |
| ${}^{22}$N | 22 | 15 | — | 140.3278 | — | — | — |
| ${}^{23}$N | 23 | 16 | — | 143.4435 | — | — | — |
| ${}^{24}$N | 24 | 17 | — | 141.2880 | — | — | — |
| ${}^{25}$N | 25 | 18 | — | 140.3250 | — | — | — |

### Oxygen (Z = 8)

_3 of 18 isotopes with a framework prediction; 1 of 18 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{11}$O | 11 | 3 | — | 34.7868 | — | — | — |
| ${}^{12}$O | 12 | 4 | — | 58.5837 | — | — | — |
| ${}^{13}$O | 13 | 5 | — | 75.5529 | — | — | — |
| ${}^{14}$O | 14 | 6 | — | 98.7319 | — | — | — |
| ${}^{15}$O | 15 | 7 | — | 111.9554 | — | — | — |
| ${}^{16}$O | 16 | 8 | 134.3846 | 127.6193 | +5.30 % | 14892.4034 | -454.07 ppm |
| ${}^{17}$O | 17 | 9 | 137.2455 | 131.7624 | +4.16 % | — | — |
| ${}^{18}$O | 18 | 10 | 146.7464 | 139.8078 | +4.96 % | — | — |
| ${}^{19}$O | 19 | 11 | — | 143.7634 | — | — | — |
| ${}^{20}$O | 20 | 12 | — | 151.3714 | — | — | — |
| ${}^{21}$O | 21 | 13 | — | 155.1769 | — | — | — |
| ${}^{22}$O | 22 | 14 | — | 162.0272 | — | — | — |
| ${}^{23}$O | 23 | 15 | — | 164.7602 | — | — | — |
| ${}^{24}$O | 24 | 16 | — | 168.9525 | — | — | — |
| ${}^{25}$O | 25 | 17 | — | 168.1951 | — | — | — |
| ${}^{26}$O | 26 | 18 | — | 168.9345 | — | — | — |
| ${}^{27}$O | 27 | 19 | — | 166.9950 | — | — | — |
| ${}^{28}$O | 28 | 20 | — | 167.6640 | — | — | — |

### Fluorine (Z = 9)

_1 of 19 isotopes with a framework prediction; 0 of 19 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{13}$F | 13 | 4 | — | 55.8610 | — | — | — |
| ${}^{14}$F | 14 | 5 | — | 73.9929 | — | — | — |
| ${}^{15}$F | 15 | 6 | — | 97.4619 | — | — | — |
| ${}^{16}$F | 16 | 7 | — | 111.4248 | — | — | — |
| ${}^{17}$F | 17 | 8 | — | 128.2196 | — | — | — |
| ${}^{18}$F | 18 | 9 | — | 137.3695 | — | — | — |
| ${}^{19}$F | 19 | 10 | 156.2474 | 147.8014 | +5.71 % | — | — |
| ${}^{20}$F | 20 | 11 | — | 154.4027 | — | — | — |
| ${}^{21}$F | 21 | 12 | — | 162.5042 | — | — | — |
| ${}^{22}$F | 22 | 13 | — | 167.7345 | — | — | — |
| ${}^{23}$F | 23 | 14 | — | 175.3139 | — | — | — |
| ${}^{24}$F | 24 | 15 | — | 179.1260 | — | — | — |
| ${}^{25}$F | 25 | 16 | — | 183.4077 | — | — | — |
| ${}^{26}$F | 26 | 17 | — | 184.1385 | — | — | — |
| ${}^{27}$F | 27 | 18 | — | 185.7510 | — | — | — |
| ${}^{28}$F | 28 | 19 | — | 185.5520 | — | — | — |
| ${}^{29}$F | 29 | 20 | — | 186.8769 | — | — | — |
| ${}^{30}$F | 30 | 21 | — | 186.1500 | — | — | — |
| ${}^{31}$F | 31 | 22 | — | 186.3410 | — | — | — |

### Neon (Z = 10)

_3 of 20 isotopes with a framework prediction; 1 of 20 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{15}$Ne | 15 | 5 | — | 73.0309 | — | — | — |
| ${}^{16}$Ne | 16 | 6 | — | 97.3308 | — | — | — |
| ${}^{17}$Ne | 17 | 7 | — | 112.8885 | — | — | — |
| ${}^{18}$Ne | 18 | 8 | — | 132.1426 | — | — | — |
| ${}^{19}$Ne | 19 | 9 | — | 143.7795 | — | — | — |
| ${}^{20}$Ne | 20 | 10 | 174.0483 | 160.6448 | +8.34 % | 18609.4368 | -719.72 ppm |
| ${}^{21}$Ne | 21 | 11 | 175.8559 | 167.4060 | +5.05 % | — | — |
| ${}^{22}$Ne | 22 | 12 | 185.9636 | 177.7702 | +4.61 % | — | — |
| ${}^{23}$Ne | 23 | 13 | — | 182.9709 | — | — | — |
| ${}^{24}$Ne | 24 | 14 | — | 191.8398 | — | — | — |
| ${}^{25}$Ne | 25 | 15 | — | 195.9950 | — | — | — |
| ${}^{26}$Ne | 26 | 16 | — | 201.5497 | — | — | — |
| ${}^{27}$Ne | 27 | 17 | — | 203.0512 | — | — | — |
| ${}^{28}$Ne | 28 | 18 | — | 206.8737 | — | — | — |
| ${}^{29}$Ne | 29 | 19 | — | 207.8450 | — | — | — |
| ${}^{30}$Ne | 30 | 20 | — | 211.0360 | — | — | — |
| ${}^{31}$Ne | 31 | 21 | — | 211.2058 | — | — | — |
| ${}^{32}$Ne | 32 | 22 | — | 213.4720 | — | — | — |
| ${}^{33}$Ne | 33 | 23 | — | 212.3880 | — | — | — |
| ${}^{34}$Ne | 34 | 24 | — | 213.7580 | — | — | — |

### Fermium (Z = 100)

_20 of 20 isotopes with a framework prediction; 20 of 20 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{241}$Fm | 241 | 141 | -146.6045 | 1797.6190 | -108.16 % | 226503.6379 | +8658.46 ppm |
| ${}^{242}$Fm | 242 | 142 | -139.9027 | 1806.5300 | -107.74 % | 227436.5016 | +8632.44 ppm |
| ${}^{243}$Fm | 243 | 143 | -133.2092 | 1813.7520 | -107.34 % | 228369.3735 | +8598.93 ppm |
| ${}^{244}$Fm | 244 | 144 | -126.5238 | 1822.1920 | -106.94 % | 229302.2535 | +8571.36 ppm |
| ${}^{245}$Fm | 245 | 145 | -119.8465 | 1828.9250 | -106.55 % | 230235.1416 | +8537.06 ppm |
| ${}^{246}$Fm | 246 | 146 | -113.1772 | 1837.1184 | -106.16 % | 231168.0377 | +8508.49 ppm |
| ${}^{247}$Fm | 247 | 147 | -106.5158 | 1843.6080 | -105.78 % | 232100.9418 | +8473.69 ppm |
| ${}^{248}$Fm | 248 | 148 | -99.8622 | 1851.5544 | -105.39 % | 233033.8536 | +8444.68 ppm |
| ${}^{249}$Fm | 249 | 149 | -93.2164 | 1858.0044 | -105.02 % | 233966.7732 | +8409.88 ppm |
| ${}^{250}$Fm | 250 | 150 | -86.5783 | 1865.5226 | -104.64 % | 234899.7005 | +8380.01 ppm |
| ${}^{251}$Fm | 251 | 151 | -79.9478 | 1871.7073 | -104.27 % | 235832.6355 | +8344.66 ppm |
| ${}^{252}$Fm | 252 | 152 | -73.3249 | 1878.9208 | -103.90 % | 236765.5780 | +8314.04 ppm |
| ${}^{253}$Fm | 253 | 153 | -66.7095 | 1884.4632 | -103.54 % | 237698.5280 | +8276.55 ppm |
| ${}^{254}$Fm | 254 | 154 | -60.1015 | 1890.9776 | -103.18 % | 238631.4854 | +8243.52 ppm |
| ${}^{255}$Fm | 255 | 155 | -53.5008 | 1896.1509 | -102.82 % | 239564.4502 | +8205.10 ppm |
| ${}^{256}$Fm | 256 | 156 | -46.9074 | 1902.5379 | -102.47 % | 240497.4222 | +8172.14 ppm |
| ${}^{257}$Fm | 257 | 157 | -40.3213 | 1907.5039 | -102.11 % | 241430.4015 | +8133.48 ppm |
| ${}^{258}$Fm | 258 | 158 | -33.7423 | 1913.8440 | -101.76 % | 242363.3880 | +8100.47 ppm |
| ${}^{259}$Fm | 259 | 159 | -27.1704 | 1918.4130 | -101.42 % | 243296.3815 | +8061.73 ppm |
| ${}^{260}$Fm | 260 | 160 | -20.6056 | 1924.5200 | -101.07 % | 244229.3821 | +8028.38 ppm |

### Mendelevium (Z = 101)

_19 of 19 isotopes with a framework prediction; 19 of 19 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{244}$Md | 244 | 143 | -151.8827 | 1814.8720 | -108.37 % | 229326.8301 | +8650.03 ppm |
| ${}^{245}$Md | 245 | 144 | -145.1750 | 1823.0450 | -107.96 % | 230259.6878 | +8621.91 ppm |
| ${}^{246}$Md | 246 | 145 | -138.4755 | 1830.4860 | -107.56 % | 231192.5538 | +8589.38 ppm |
| ${}^{247}$Md | 247 | 146 | -131.7841 | 1838.6680 | -107.17 % | 232125.4278 | +8561.40 ppm |
| ${}^{248}$Md | 248 | 147 | -125.1007 | 1845.6160 | -106.78 % | 233058.3098 | +8528.48 ppm |
| ${}^{249}$Md | 249 | 148 | -118.4252 | 1853.5602 | -106.39 % | 233991.1997 | +8499.24 ppm |
| ${}^{250}$Md | 250 | 149 | -111.7576 | 1860.4133 | -106.01 % | 234924.0975 | +8466.01 ppm |
| ${}^{251}$Md | 251 | 150 | -105.0977 | 1867.9170 | -105.63 % | 235857.0030 | +8435.88 ppm |
| ${}^{252}$Md | 252 | 151 | -98.4455 | 1874.4880 | -105.25 % | 236789.9163 | +8402.01 ppm |
| ${}^{253}$Md | 253 | 152 | -91.8010 | 1881.8140 | -104.88 % | 237722.8372 | +8371.85 ppm |
| ${}^{254}$Md | 254 | 153 | -85.1641 | 1887.7280 | -104.51 % | 238655.7657 | +8335.25 ppm |
| ${}^{255}$Md | 255 | 154 | -78.5347 | 1894.3270 | -104.15 % | 239588.7017 | +8302.74 ppm |
| ${}^{256}$Md | 256 | 155 | -71.9127 | 1899.7760 | -103.79 % | 240521.6451 | +8265.35 ppm |
| ${}^{257}$Md | 257 | 156 | -65.2980 | 1906.3192 | -103.43 % | 241454.5959 | +8232.81 ppm |
| ${}^{258}$Md | 258 | 157 | -58.6907 | 1911.6927 | -103.07 % | 242387.5540 | +8195.69 ppm |
| ${}^{259}$Md | 259 | 158 | -52.0906 | 1917.8950 | -102.72 % | 243320.5194 | +8162.33 ppm |
| ${}^{260}$Md | 260 | 159 | -45.4977 | 1922.9600 | -102.37 % | 244253.4919 | +8124.63 ppm |
| ${}^{261}$Md | 261 | 160 | -38.9119 | 1929.0510 | -102.02 % | 245186.4715 | +8091.21 ppm |
| ${}^{262}$Md | 262 | 161 | -32.3332 | 1934.0840 | -101.67 % | 246119.4582 | +8053.70 ppm |

### Nobelium (Z = 102)

_17 of 17 isotopes with a framework prediction; 17 of 17 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{248}$No | 248 | 146 | -150.5659 | 1841.1520 | -108.18 % | 233082.9927 | +8618.96 ppm |
| ${}^{249}$No | 249 | 147 | -143.8604 | 1848.0780 | -107.78 % | 234015.8526 | +8585.47 ppm |
| ${}^{250}$No | 250 | 148 | -137.1630 | 1856.5000 | -107.39 % | 234948.7205 | +8557.99 ppm |
| ${}^{251}$No | 251 | 149 | -130.4734 | 1863.1730 | -107.00 % | 235881.5964 | +8524.29 ppm |
| ${}^{252}$No | 252 | 150 | -123.7917 | 1871.3014 | -106.62 % | 236814.4802 | +8496.29 ppm |
| ${}^{253}$No | 253 | 151 | -117.1179 | 1877.8854 | -106.24 % | 237747.3717 | +8462.29 ppm |
| ${}^{254}$No | 254 | 152 | -110.4517 | 1885.5921 | -105.86 % | 238680.2710 | +8433.37 ppm |
| ${}^{255}$No | 255 | 153 | -103.7932 | 1891.5748 | -105.49 % | 239613.1779 | +8397.39 ppm |
| ${}^{256}$No | 256 | 154 | -97.1423 | 1898.6350 | -105.12 % | 240546.0924 | +8366.28 ppm |
| ${}^{257}$No | 257 | 155 | -90.4989 | 1904.2823 | -104.75 % | 241479.0144 | +8329.49 ppm |
| ${}^{258}$No | 258 | 156 | -83.8629 | 1911.0060 | -104.39 % | 242411.9439 | +8298.03 ppm |
| ${}^{259}$No | 259 | 157 | -77.2344 | 1916.5926 | -104.03 % | 243344.8808 | +8261.11 ppm |
| ${}^{260}$No | 260 | 158 | -70.6131 | 1923.2200 | -103.67 % | 244277.8249 | +8228.97 ppm |
| ${}^{261}$No | 261 | 159 | -63.9991 | 1928.2680 | -103.32 % | 245210.7764 | +8191.65 ppm |
| ${}^{262}$No | 262 | 160 | -57.3923 | 1934.8700 | -102.97 % | 246143.7350 | +8159.60 ppm |
| ${}^{263}$No | 263 | 161 | -50.7926 | 1939.8880 | -102.62 % | 247076.7007 | +8122.13 ppm |
| ${}^{264}$No | 264 | 162 | -44.2000 | 1945.9440 | -102.27 % | 248009.6735 | +8089.68 ppm |

### Lawrencium (Z = 103)

_16 of 16 isotopes with a framework prediction; 16 of 16 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{251}$Lr | 251 | 148 | -156.0750 | 1857.4000 | -108.40 % | 235906.4157 | +8608.92 ppm |
| ${}^{252}$Lr | 252 | 149 | -149.3635 | 1864.8000 | -108.01 % | 236839.2696 | +8577.53 ppm |
| ${}^{253}$Lr | 253 | 150 | -142.6600 | 1872.9383 | -107.62 % | 237772.1315 | +8549.50 ppm |
| ${}^{254}$Lr | 254 | 151 | -135.9643 | 1879.8872 | -107.23 % | 238705.0012 | +8516.88 ppm |
| ${}^{255}$Lr | 255 | 152 | -129.2764 | 1887.6571 | -106.85 % | 239637.8788 | +8488.04 ppm |
| ${}^{256}$Lr | 256 | 153 | -122.5963 | 1893.9291 | -106.47 % | 240570.7641 | +8453.12 ppm |
| ${}^{257}$Lr | 257 | 154 | -115.9238 | 1901.0290 | -106.10 % | 241503.6571 | +8422.21 ppm |
| ${}^{258}$Lr | 258 | 155 | -109.2590 | 1907.1360 | -105.73 % | 242436.5576 | +8386.55 ppm |
| ${}^{259}$Lr | 259 | 156 | -102.6017 | 1914.0100 | -105.36 % | 243369.4657 | +8355.58 ppm |
| ${}^{260}$Lr | 260 | 157 | -95.9518 | 1919.5800 | -105.00 % | 244302.3813 | +8319.23 ppm |
| ${}^{261}$Lr | 261 | 158 | -89.3093 | 1926.4410 | -104.64 % | 245235.3042 | +8287.93 ppm |
| ${}^{262}$Lr | 262 | 159 | -82.6742 | 1931.9880 | -104.28 % | 246168.2345 | +8251.67 ppm |
| ${}^{263}$Lr | 263 | 160 | -76.0463 | 1938.5730 | -103.92 % | 247101.1721 | +8219.76 ppm |
| ${}^{264}$Lr | 264 | 161 | -69.4256 | 1943.8320 | -103.57 % | 248034.1168 | +8183.45 ppm |
| ${}^{265}$Lr | 265 | 162 | -62.8121 | 1950.1350 | -103.22 % | 248967.0687 | +8150.90 ppm |
| ${}^{266}$Lr | 266 | 163 | -56.2057 | 1954.8340 | -102.88 % | 249900.0277 | +8112.23 ppm |

### Rutherfordium (Z = 104)

_16 of 16 isotopes with a framework prediction; 16 of 16 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{253}$Rf | 253 | 149 | -168.4273 | 1867.1400 | -109.02 % | 237797.1165 | +8633.58 ppm |
| ${}^{254}$Rf | 254 | 150 | -161.7019 | 1875.5360 | -108.62 % | 238729.9565 | +8607.17 ppm |
| ${}^{255}$Rf | 255 | 151 | -154.9844 | 1882.4100 | -108.23 % | 239662.8044 | +8574.33 ppm |
| ${}^{256}$Rf | 256 | 152 | -148.2747 | 1890.6713 | -107.84 % | 240595.6602 | +8547.01 ppm |
| ${}^{257}$Rf | 257 | 153 | -141.5729 | 1897.0983 | -107.46 % | 241528.5238 | +8512.56 ppm |
| ${}^{258}$Rf | 258 | 154 | -134.8789 | 1904.6916 | -107.08 % | 242461.3952 | +8483.31 ppm |
| ${}^{259}$Rf | 259 | 155 | -128.1925 | 1910.6430 | -106.71 % | 243394.2742 | +8447.85 ppm |
| ${}^{260}$Rf | 260 | 156 | -121.5137 | 1918.0200 | -106.34 % | 244327.1609 | +8417.87 ppm |
| ${}^{261}$Rf | 261 | 157 | -114.8425 | 1923.9317 | -105.97 % | 245260.0551 | +8382.39 ppm |
| ${}^{262}$Rf | 262 | 158 | -108.1788 | 1930.9400 | -105.60 % | 246192.9567 | +8351.74 ppm |
| ${}^{263}$Rf | 263 | 159 | -101.5224 | 1936.7320 | -105.24 % | 247125.8658 | +8316.04 ppm |
| ${}^{264}$Rf | 264 | 160 | -94.8734 | 1943.3040 | -104.88 % | 248058.7823 | +8284.94 ppm |
| ${}^{265}$Rf | 265 | 161 | -88.2317 | 1948.8100 | -104.53 % | 248991.7060 | +8248.80 ppm |
| ${}^{266}$Rf | 266 | 162 | -81.5972 | 1955.3660 | -104.17 % | 249924.6369 | +8217.71 ppm |
| ${}^{267}$Rf | 267 | 163 | -74.9699 | 1960.3140 | -103.82 % | 250857.5750 | +8179.35 ppm |
| ${}^{268}$Rf | 268 | 164 | -68.3497 | 1966.3160 | -103.48 % | 251790.5202 | +8146.45 ppm |

### Dubnium (Z = 105)

_16 of 16 isotopes with a framework prediction; 16 of 16 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{255}$Db | 255 | 150 | -180.9170 | 1876.5450 | -109.64 % | 239687.9547 | +8657.82 ppm |
| ${}^{256}$Db | 256 | 151 | -174.1776 | 1883.9040 | -109.25 % | 240620.7807 | +8626.63 ppm |
| ${}^{257}$Db | 257 | 152 | -167.4461 | 1892.0280 | -108.85 % | 241553.6147 | +8599.27 ppm |
| ${}^{258}$Db | 258 | 153 | -160.7226 | 1898.7459 | -108.46 % | 242486.4566 | +8565.89 ppm |
| ${}^{259}$Db | 259 | 154 | -154.0069 | 1906.3339 | -108.08 % | 243419.3063 | +8536.42 ppm |
| ${}^{260}$Db | 260 | 155 | -147.2989 | 1912.8200 | -107.70 % | 244352.1637 | +8502.23 ppm |
| ${}^{261}$Db | 261 | 156 | -140.5987 | 1920.1770 | -107.32 % | 245285.0289 | +8472.67 ppm |
| ${}^{262}$Db | 262 | 157 | -133.9060 | 1926.2240 | -106.95 % | 246217.9017 | +8437.96 ppm |
| ${}^{263}$Db | 263 | 158 | -127.2210 | 1933.5760 | -106.58 % | 247150.7820 | +8408.02 ppm |
| ${}^{264}$Db | 264 | 159 | -120.5434 | 1939.3440 | -106.22 % | 248083.6699 | +8373.03 ppm |
| ${}^{265}$Db | 265 | 160 | -113.8732 | 1946.4250 | -105.85 % | 249016.5651 | +8342.55 ppm |
| ${}^{266}$Db | 266 | 161 | -107.2104 | 1952.1740 | -105.49 % | 249949.4677 | +8307.29 ppm |
| ${}^{267}$Db | 267 | 162 | -100.5549 | 1958.9790 | -105.13 % | 250882.3777 | +8276.72 ppm |
| ${}^{268}$Db | 268 | 163 | -93.9066 | 1963.9040 | -104.78 % | 251815.2948 | +8239.25 ppm |
| ${}^{269}$Db | 269 | 164 | -87.2655 | 1969.8870 | -104.43 % | 252748.2191 | +8205.94 ppm |
| ${}^{270}$Db | 270 | 165 | -80.6315 | 1974.7800 | -104.08 % | 253681.1506 | +8168.26 ppm |

### Seaborgium (Z = 106)

_16 of 16 isotopes with a framework prediction; 16 of 16 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{258}$Sg | 258 | 152 | -186.7901 | 1894.2360 | -109.86 % | 242511.7418 | +8655.16 ppm |
| ${}^{259}$Sg | 259 | 153 | -180.0448 | 1901.0600 | -109.47 % | 243444.5619 | +8622.14 ppm |
| ${}^{260}$Sg | 260 | 154 | -173.3074 | 1909.0664 | -109.08 % | 244377.3899 | +8594.38 ppm |
| ${}^{261}$Sg | 261 | 155 | -166.5778 | 1915.6802 | -108.70 % | 245310.2257 | +8560.94 ppm |
| ${}^{262}$Sg | 262 | 156 | -159.8560 | 1923.3875 | -108.31 % | 246243.0694 | +8532.30 ppm |
| ${}^{263}$Sg | 263 | 157 | -153.1419 | 1929.6310 | -107.94 % | 247175.9207 | +8497.90 ppm |
| ${}^{264}$Sg | 264 | 158 | -146.4355 | 1937.2320 | -107.56 % | 248108.7796 | +8468.86 ppm |
| ${}^{265}$Sg | 265 | 159 | -139.7366 | 1943.2450 | -107.19 % | 249041.6462 | +8434.26 ppm |
| ${}^{266}$Sg | 266 | 160 | -133.0452 | 1950.3120 | -106.82 % | 249974.5202 | +8404.79 ppm |
| ${}^{267}$Sg | 267 | 161 | -126.3612 | 1956.3090 | -106.46 % | 250907.4017 | +8370.03 ppm |
| ${}^{268}$Sg | 268 | 162 | -119.6846 | 1963.3680 | -106.10 % | 251840.2905 | +8340.39 ppm |
| ${}^{269}$Sg | 269 | 163 | -113.0154 | 1968.5420 | -105.74 % | 252773.1866 | +8303.35 ppm |
| ${}^{270}$Sg | 270 | 164 | -106.3533 | 1974.7800 | -105.39 % | 253706.0900 | +8271.24 ppm |
| ${}^{271}$Sg | 271 | 165 | -99.6985 | 1979.6550 | -105.04 % | 254639.0006 | +8233.63 ppm |
| ${}^{272}$Sg | 272 | 166 | -93.0508 | 1985.8720 | -104.69 % | 255571.9183 | +8201.42 ppm |
| ${}^{273}$Sg | 273 | 167 | -86.4101 | 1990.7160 | -104.34 % | 256504.8431 | +8163.54 ppm |

### Bohrium (Z = 107)

_19 of 19 isotopes with a framework prediction; 19 of 19 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{260}$Bh | 260 | 153 | -199.5392 | 1901.6400 | -110.49 % | 244402.8393 | +8672.04 ppm |
| ${}^{261}$Bh | 261 | 154 | -192.7800 | 1909.8235 | -110.09 % | 245335.6456 | +8644.41 ppm |
| ${}^{262}$Bh | 262 | 155 | -186.0288 | 1916.7221 | -109.71 % | 246268.4597 | +8611.99 ppm |
| ${}^{263}$Bh | 263 | 156 | -179.2854 | 1924.6340 | -109.32 % | 247201.2818 | +8583.68 ppm |
| ${}^{264}$Bh | 264 | 157 | -172.5497 | 1931.1600 | -108.94 % | 248134.1116 | +8550.61 ppm |
| ${}^{265}$Bh | 265 | 158 | -165.8218 | 1938.7400 | -108.55 % | 249066.9491 | +8522.02 ppm |
| ${}^{266}$Bh | 266 | 159 | -159.1016 | 1945.2580 | -108.18 % | 249999.7942 | +8488.49 ppm |
| ${}^{267}$Bh | 267 | 160 | -152.3889 | 1952.5710 | -107.80 % | 250932.6470 | +8459.50 ppm |
| ${}^{268}$Bh | 268 | 161 | -145.6837 | 1958.8120 | -107.44 % | 251865.5072 | +8425.57 ppm |
| ${}^{269}$Bh | 269 | 162 | -138.9860 | 1966.1210 | -107.07 % | 252798.3750 | +8396.65 ppm |
| ${}^{270}$Bh | 270 | 163 | -132.2957 | 1971.2700 | -106.71 % | 253731.2500 | +8360.02 ppm |
| ${}^{271}$Bh | 271 | 164 | -125.6127 | 1977.7580 | -106.35 % | 254664.1325 | +8328.18 ppm |
| ${}^{272}$Bh | 272 | 165 | -118.9369 | 1982.8800 | -106.00 % | 255597.0221 | +8291.43 ppm |
| ${}^{273}$Bh | 273 | 166 | -112.2684 | 1989.0780 | -105.64 % | 256529.9190 | +8259.08 ppm |
| ${}^{274}$Bh | 274 | 167 | -105.6070 | 1994.1720 | -105.30 % | 257462.8230 | +8222.32 ppm |
| ${}^{275}$Bh | 275 | 168 | -98.9527 | 2000.0750 | -104.95 % | 258395.7341 | +8190.02 ppm |
| ${}^{276}$Bh | 276 | 169 | -92.3054 | 2005.1400 | -104.60 % | 259328.6523 | +8153.48 ppm |
| ${}^{277}$Bh | 277 | 170 | -85.6650 | 2011.0200 | -104.26 % | 260261.5774 | +8121.21 ppm |
| ${}^{278}$Bh | 278 | 171 | -79.0316 | 2015.7780 | -103.92 % | 261194.5094 | +8084.83 ppm |

### Hassium (Z = 108)

_18 of 18 isotopes with a framework prediction; 18 of 18 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{263}$Hs | 263 | 155 | -205.6512 | 1918.5850 | -110.72 % | 247226.8653 | +8666.73 ppm |
| ${}^{264}$Hs | 264 | 156 | -198.8862 | 1926.7713 | -110.32 % | 248159.6657 | +8639.70 ppm |
| ${}^{265}$Hs | 265 | 157 | -192.1290 | 1933.5056 | -109.94 % | 249092.4739 | +8606.97 ppm |
| ${}^{266}$Hs | 266 | 158 | -185.3796 | 1941.3375 | -109.55 % | 250025.2899 | +8578.99 ppm |
| ${}^{267}$Hs | 267 | 159 | -178.6379 | 1947.7650 | -109.17 % | 250958.1137 | +8546.06 ppm |
| ${}^{268}$Hs | 268 | 160 | -171.9039 | 1955.5960 | -108.79 % | 251890.9451 | +8518.29 ppm |
| ${}^{269}$Hs | 269 | 161 | -165.1775 | 1962.0860 | -108.42 % | 252823.7841 | +8485.87 ppm |
| ${}^{270}$Hs | 270 | 162 | -158.4586 | 1969.6500 | -108.05 % | 253756.6306 | +8457.35 ppm |
| ${}^{271}$Hs | 271 | 163 | -151.7471 | 1975.0480 | -107.68 % | 254689.4846 | +8421.24 ppm |
| ${}^{272}$Hs | 272 | 164 | -145.0431 | 1981.7920 | -107.32 % | 255622.3460 | +8390.47 ppm |
| ${}^{273}$Hs | 273 | 165 | -138.3464 | 1987.1670 | -106.96 % | 256555.2147 | +8354.20 ppm |
| ${}^{274}$Hs | 274 | 166 | -131.6570 | 1993.6240 | -106.60 % | 257488.0907 | +8322.67 ppm |
| ${}^{275}$Hs | 275 | 167 | -124.9747 | 1998.7000 | -106.25 % | 258420.9739 | +8285.70 ppm |
| ${}^{276}$Hs | 276 | 168 | -118.2997 | 2005.1400 | -105.90 % | 259353.8643 | +8254.49 ppm |
| ${}^{277}$Hs | 277 | 169 | -111.6317 | 2009.9120 | -105.55 % | 260286.7617 | +8217.68 ppm |
| ${}^{278}$Hs | 278 | 170 | -104.9708 | 2016.0560 | -105.21 % | 261219.6662 | +8186.40 ppm |
| ${}^{279}$Hs | 279 | 171 | -98.3169 | 2020.7970 | -104.87 % | 262152.5777 | +8149.81 ppm |
| ${}^{280}$Hs | 280 | 172 | -91.6698 | 2026.9200 | -104.52 % | 263085.4961 | +8118.76 ppm |

### Meitnerium (Z = 109)

_18 of 18 isotopes with a framework prediction; 18 of 18 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{265}$Mt | 265 | 156 | -218.6580 | 1927.0800 | -111.35 % | 249118.2206 | +8687.84 ppm |
| ${}^{266}$Mt | 266 | 157 | -211.8792 | 1934.0221 | -110.96 % | 250051.0072 | +8656.15 ppm |
| ${}^{267}$Mt | 267 | 158 | -205.1083 | 1941.8910 | -110.56 % | 250983.8017 | +8628.49 ppm |
| ${}^{268}$Mt | 268 | 159 | -198.3451 | 1948.6280 | -110.18 % | 251916.6040 | +8596.06 ppm |
| ${}^{269}$Mt | 269 | 160 | -191.5897 | 1956.7060 | -109.79 % | 252849.4140 | +8568.77 ppm |
| ${}^{270}$Mt | 270 | 161 | -184.8420 | 1963.1700 | -109.42 % | 253782.2317 | +8536.66 ppm |
| ${}^{271}$Mt | 271 | 162 | -178.1018 | 1970.9830 | -109.04 % | 254715.0570 | +8508.89 ppm |
| ${}^{272}$Mt | 272 | 163 | -171.3692 | 1976.6240 | -108.67 % | 255647.8898 | +8473.43 ppm |
| ${}^{273}$Mt | 273 | 164 | -164.6441 | 1983.3450 | -108.30 % | 256580.7301 | +8442.54 ppm |
| ${}^{274}$Mt | 274 | 165 | -157.9264 | 1988.9660 | -107.94 % | 257513.5778 | +8407.30 ppm |
| ${}^{275}$Mt | 275 | 166 | -151.2160 | 1995.6750 | -107.58 % | 258446.4328 | +8376.09 ppm |
| ${}^{276}$Mt | 276 | 167 | -144.5130 | 2001.0000 | -107.22 % | 259379.2952 | +8341.09 ppm |
| ${}^{277}$Mt | 277 | 168 | -137.8171 | 2007.4190 | -106.87 % | 260312.1648 | +8309.70 ppm |
| ${}^{278}$Mt | 278 | 169 | -131.1284 | 2012.7200 | -106.51 % | 261245.0415 | +8274.43 ppm |
| ${}^{279}$Mt | 279 | 170 | -124.4469 | 2019.1230 | -106.16 % | 262177.9254 | +8243.08 ppm |
| ${}^{280}$Mt | 280 | 171 | -117.7723 | 2024.1200 | -105.82 % | 263110.8163 | +8207.71 ppm |
| ${}^{281}$Mt | 281 | 172 | -111.1048 | 2030.2250 | -105.47 % | 264043.7142 | +8176.60 ppm |
| ${}^{282}$Mt | 282 | 173 | -104.4442 | 2035.4760 | -105.13 % | 264976.6190 | +8141.27 ppm |

### Sodium (Z = 11)

_0 of 23 isotopes with a framework prediction; 0 of 23 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{17}$Na | 17 | 6 | — | 93.8870 | — | — | — |
| ${}^{18}$Na | 18 | 7 | — | 111.6399 | — | — | — |
| ${}^{19}$Na | 19 | 8 | — | 131.8198 | — | — | — |
| ${}^{20}$Na | 20 | 9 | — | 145.9701 | — | — | — |
| ${}^{21}$Na | 21 | 10 | — | 163.0767 | — | — | — |
| ${}^{22}$Na | 22 | 11 | — | 174.1446 | — | — | — |
| ${}^{23}$Na | 23 | 12 | — | 186.5644 | — | — | — |
| ${}^{24}$Na | 24 | 13 | — | 193.5237 | — | — | — |
| ${}^{25}$Na | 25 | 14 | — | 202.5349 | — | — | — |
| ${}^{26}$Na | 26 | 15 | — | 208.1092 | — | — | — |
| ${}^{27}$Na | 27 | 16 | — | 214.8376 | — | — | — |
| ${}^{28}$Na | 28 | 17 | — | 218.3794 | — | — | — |
| ${}^{29}$Na | 29 | 18 | — | 222.7824 | — | — | — |
| ${}^{30}$Na | 30 | 19 | — | 225.0591 | — | — | — |
| ${}^{31}$Na | 31 | 20 | — | 229.3590 | — | — | — |
| ${}^{32}$Na | 32 | 21 | — | 231.0362 | — | — | — |
| ${}^{33}$Na | 33 | 22 | — | 233.9676 | — | — | — |
| ${}^{34}$Na | 34 | 23 | — | 234.1389 | — | — | — |
| ${}^{35}$Na | 35 | 24 | — | 236.0750 | — | — | — |
| ${}^{36}$Na | 36 | 25 | — | 236.0520 | — | — | — |
| ${}^{37}$Na | 37 | 26 | — | 236.9110 | — | — | — |
| ${}^{38}$Na | 38 | 27 | — | 236.2080 | — | — | — |
| ${}^{39}$Na | 39 | 28 | — | 236.1840 | — | — | — |

### Darmstadtium (Z = 110)

_18 of 18 isotopes with a framework prediction; 18 of 18 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{267}$Ds | 267 | 157 | -231.8000 | 1935.2160 | -111.98 % | 251009.7110 | +8707.93 ppm |
| ${}^{268}$Ds | 268 | 158 | -225.0074 | 1943.5360 | -111.58 % | 251942.4839 | +8681.51 ppm |
| ${}^{269}$Ds | 269 | 159 | -218.2228 | 1950.2917 | -111.19 % | 252875.2647 | +8649.61 ppm |
| ${}^{270}$Ds | 270 | 160 | -211.4459 | 1958.5161 | -110.80 % | 253808.0533 | +8623.35 ppm |
| ${}^{271}$Ds | 271 | 161 | -204.6768 | 1965.2920 | -110.41 % | 254740.8496 | +8591.63 ppm |
| ${}^{272}$Ds | 272 | 162 | -197.9154 | 1973.3600 | -110.03 % | 255673.6536 | +8564.71 ppm |
| ${}^{273}$Ds | 273 | 163 | -191.1616 | 1979.2500 | -109.66 % | 256606.4652 | +8529.80 ppm |
| ${}^{274}$Ds | 274 | 164 | -184.4153 | 1986.2260 | -109.28 % | 257539.2844 | +8500.27 ppm |
| ${}^{275}$Ds | 275 | 165 | -177.6765 | 1991.8250 | -108.92 % | 258472.1110 | +8464.86 ppm |
| ${}^{276}$Ds | 276 | 166 | -170.9452 | 1999.0680 | -108.55 % | 259404.9451 | +8436.00 ppm |
| ${}^{277}$Ds | 277 | 167 | -164.2212 | 2004.6490 | -108.19 % | 260337.7865 | +8400.81 ppm |
| ${}^{278}$Ds | 278 | 168 | -157.5045 | 2011.6080 | -107.83 % | 261270.6353 | +8371.32 ppm |
| ${}^{279}$Ds | 279 | 169 | -150.7951 | 2016.8910 | -107.48 % | 262203.4912 | +8335.82 ppm |
| ${}^{280}$Ds | 280 | 170 | -144.0928 | 2023.5600 | -107.12 % | 263136.3544 | +8306.31 ppm |
| ${}^{281}$Ds | 281 | 171 | -137.3977 | 2028.8200 | -106.77 % | 264069.2247 | +8270.65 ppm |
| ${}^{282}$Ds | 282 | 172 | -130.7096 | 2035.1940 | -106.42 % | 265002.1020 | +8240.78 ppm |
| ${}^{283}$Ds | 283 | 173 | -124.0285 | 2040.4300 | -106.08 % | 265934.9864 | +8205.33 ppm |
| ${}^{284}$Ds | 284 | 174 | -117.3544 | 2046.7880 | -105.73 % | 266867.8777 | +8175.53 ppm |

### Roentgenium (Z = 111)

_15 of 15 isotopes with a framework prediction; 15 of 15 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{272}$Rg | 272 | 161 | -224.6816 | 1965.7440 | -111.43 % | 255699.6374 | +8640.59 ppm |
| ${}^{273}$Rg | 273 | 162 | -217.8988 | 1973.7900 | -111.04 % | 256632.4201 | +8613.58 ppm |
| ${}^{274}$Rg | 274 | 163 | -211.1237 | 1980.1980 | -110.66 % | 257565.2104 | +8580.41 ppm |
| ${}^{275}$Rg | 275 | 164 | -204.3563 | 1987.4250 | -110.28 % | 258498.0084 | +8551.23 ppm |
| ${}^{276}$Rg | 276 | 165 | -197.5964 | 1993.5480 | -109.91 % | 259430.8140 | +8517.56 ppm |
| ${}^{277}$Rg | 277 | 166 | -190.8440 | 2000.4940 | -109.54 % | 260363.6270 | +8487.95 ppm |
| ${}^{278}$Rg | 278 | 167 | -184.0990 | 2006.6040 | -109.17 % | 261296.4475 | +8454.33 ppm |
| ${}^{279}$Rg | 279 | 168 | -177.3615 | 2013.2640 | -108.81 % | 262229.2753 | +8424.51 ppm |
| ${}^{280}$Rg | 280 | 169 | -170.6312 | 2019.3600 | -108.45 % | 263162.1104 | +8391.22 ppm |
| ${}^{281}$Rg | 281 | 170 | -163.9082 | 2025.7290 | -108.09 % | 264094.9529 | +8360.95 ppm |
| ${}^{282}$Rg | 282 | 171 | -157.1924 | 2031.5280 | -107.74 % | 265027.8025 | +8327.24 ppm |
| ${}^{283}$Rg | 283 | 172 | -150.4837 | 2037.8830 | -107.38 % | 265960.6592 | +8296.74 ppm |
| ${}^{284}$Rg | 284 | 173 | -143.7821 | 2043.3800 | -107.04 % | 266893.5230 | +8262.85 ppm |
| ${}^{285}$Rg | 285 | 174 | -137.0875 | 2049.7200 | -106.69 % | 267826.3938 | +8232.38 ppm |
| ${}^{286}$Rg | 286 | 175 | -130.3998 | 2054.9100 | -106.35 % | 268759.2716 | +8198.28 ppm |

### Copernicium (Z = 112)

_13 of 13 isotopes with a framework prediction; 13 of 13 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{276}$Cn | 276 | 164 | -224.4665 | 1989.6840 | -111.28 % | 259456.9018 | +8607.32 ppm |
| ${}^{277}$Cn | 277 | 165 | -217.6855 | 1995.7850 | -110.91 % | 260389.6861 | +8573.55 ppm |
| ${}^{278}$Cn | 278 | 166 | -210.9120 | 2003.2680 | -110.53 % | 261322.4781 | +8545.75 ppm |
| ${}^{279}$Cn | 279 | 167 | -204.1460 | 2009.3580 | -110.16 % | 262255.2775 | +8511.71 ppm |
| ${}^{280}$Cn | 280 | 168 | -197.3875 | 2016.5600 | -109.79 % | 263188.0844 | +8483.91 ppm |
| ${}^{281}$Cn | 281 | 169 | -190.6364 | 2022.3570 | -109.43 % | 264120.8987 | +8449.95 ppm |
| ${}^{282}$Cn | 282 | 170 | -183.8926 | 2029.5540 | -109.06 % | 265053.7203 | +8421.68 ppm |
| ${}^{283}$Cn | 283 | 171 | -177.1560 | 2035.3360 | -108.70 % | 265986.5492 | +8387.41 ppm |
| ${}^{284}$Cn | 284 | 172 | -170.4267 | 2042.2440 | -108.35 % | 266919.3853 | +8358.85 ppm |
| ${}^{285}$Cn | 285 | 173 | -163.7045 | 2047.7250 | -107.99 % | 267852.2285 | +8324.48 ppm |
| ${}^{286}$Cn | 286 | 174 | -156.9894 | 2054.3380 | -107.64 % | 268785.0788 | +8295.32 ppm |
| ${}^{287}$Cn | 287 | 175 | -150.2813 | 2059.5120 | -107.30 % | 269717.9362 | +8260.53 ppm |
| ${}^{288}$Cn | 288 | 176 | -143.5802 | 2066.1120 | -106.95 % | 270650.8005 | +8231.11 ppm |

### Nihonium (Z = 113)

_13 of 13 isotopes with a framework prediction; 13 of 13 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{278}$Nh | 278 | 165 | -237.9434 | 1996.3180 | -111.92 % | 261348.7272 | +8622.98 ppm |
| ${}^{279}$Nh | 279 | 166 | -231.1488 | 2004.0570 | -111.53 % | 262281.4980 | +8595.33 ppm |
| ${}^{280}$Nh | 280 | 167 | -224.3618 | 2010.4000 | -111.16 % | 263214.2764 | +8562.69 ppm |
| ${}^{281}$Nh | 281 | 168 | -217.5822 | 2017.8610 | -110.78 % | 264147.0623 | +8534.97 ppm |
| ${}^{282}$Nh | 282 | 169 | -210.8102 | 2023.9140 | -110.42 % | 265079.8556 | +8502.31 ppm |
| ${}^{283}$Nh | 283 | 170 | -204.0455 | 2031.0910 | -110.05 % | 266012.6564 | +8474.05 ppm |
| ${}^{284}$Nh | 284 | 171 | -197.2882 | 2037.1320 | -109.68 % | 266945.4645 | +8441.46 ppm |
| ${}^{285}$Nh | 285 | 172 | -190.5381 | 2044.0200 | -109.32 % | 267878.2798 | +8412.37 ppm |
| ${}^{286}$Nh | 286 | 173 | -183.7953 | 2050.0480 | -108.97 % | 268811.1024 | +8379.68 ppm |
| ${}^{287}$Nh | 287 | 174 | -177.0596 | 2056.6420 | -108.61 % | 269743.9322 | +8349.85 ppm |
| ${}^{288}$Nh | 288 | 175 | -170.3311 | 2062.0800 | -108.26 % | 270676.7690 | +8316.43 ppm |
| ${}^{289}$Nh | 289 | 176 | -163.6095 | 2068.6620 | -107.91 % | 271609.6129 | +8286.76 ppm |
| ${}^{290}$Nh | 290 | 177 | -156.8950 | 2074.0800 | -107.56 % | 272542.4638 | +8252.92 ppm |

### Flerovium (Z = 114)

_8 of 8 isotopes with a framework prediction; 8 of 8 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{284}$Fl | 284 | 170 | -224.3666 | 2034.2920 | -111.03 % | 266971.7606 | +8532.47 ppm |
| ${}^{285}$Fl | 285 | 171 | -217.5885 | 2040.3150 | -110.66 % | 267904.5478 | +8499.24 ppm |
| ${}^{286}$Fl | 286 | 172 | -210.8177 | 2047.4740 | -110.30 % | 268837.3425 | +8471.88 ppm |
| ${}^{287}$Fl | 287 | 173 | -204.0541 | 2053.4850 | -109.94 % | 269770.1444 | +8438.51 ppm |
| ${}^{288}$Fl | 288 | 174 | -197.2979 | 2060.3520 | -109.58 % | 270702.9535 | +8410.41 ppm |
| ${}^{289}$Fl | 289 | 175 | -190.5487 | 2066.0610 | -109.22 % | 271635.7698 | +8376.70 ppm |
| ${}^{290}$Fl | 290 | 176 | -183.8067 | 2072.6300 | -108.87 % | 272568.5932 | +8348.03 ppm |
| ${}^{291}$Fl | 291 | 177 | -177.0718 | 2078.0310 | -108.52 % | 273501.4237 | +8313.99 ppm |

### Moscovium (Z = 115)

_6 of 6 isotopes with a framework prediction; 6 of 6 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{287}$Mc | 287 | 172 | -231.2648 | 2048.8930 | -111.29 % | 269796.5727 | +8522.90 ppm |
| ${}^{288}$Mc | 288 | 173 | -224.4806 | 2054.8800 | -110.92 % | 270729.3539 | +8490.92 ppm |
| ${}^{289}$Mc | 289 | 174 | -217.7036 | 2062.0150 | -110.56 % | 271662.1424 | +8462.55 ppm |
| ${}^{290}$Mc | 290 | 175 | -210.9339 | 2067.9900 | -110.20 % | 272594.9381 | +8430.34 ppm |
| ${}^{291}$Mc | 291 | 176 | -204.1714 | 2074.5390 | -109.84 % | 273527.7410 | +8401.05 ppm |
| ${}^{292}$Mc | 292 | 177 | -197.4160 | 2080.2080 | -109.49 % | 274460.5510 | +8368.17 ppm |

### Livermorium (Z = 116)

_5 of 5 isotopes with a framework prediction; 5 of 5 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{289}$Lv | 289 | 173 | -245.0742 | 2057.3910 | -111.91 % | 271688.7306 | +8547.12 ppm |
| ${}^{290}$Lv | 290 | 174 | -238.2765 | 2064.8000 | -111.54 % | 272621.4984 | +8520.25 ppm |
| ${}^{291}$Lv | 291 | 175 | -231.4862 | 2070.7560 | -111.18 % | 273554.2734 | +8487.48 ppm |
| ${}^{292}$Lv | 292 | 176 | -224.7031 | 2077.8720 | -110.81 % | 274487.0557 | +8459.87 ppm |
| ${}^{293}$Lv | 293 | 177 | -217.9272 | 2083.5230 | -110.46 % | 275419.8452 | +8426.77 ppm |

### Tennessine (Z = 117)

_4 of 4 isotopes with a framework prediction; 4 of 4 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{291}$Ts | 291 | 174 | -259.0162 | 2065.5180 | -112.54 % | 273581.0211 | +8569.69 ppm |
| ${}^{292}$Ts | 292 | 175 | -252.2051 | 2071.7400 | -112.17 % | 274513.7755 | +8537.70 ppm |
| ${}^{293}$Ts | 293 | 176 | -245.4014 | 2078.8350 | -111.80 % | 275446.5372 | +8510.24 ppm |
| ${}^{294}$Ts | 294 | 177 | -238.6049 | 2085.0480 | -111.44 % | 276379.3061 | +8478.73 ppm |

### Oganesson (Z = 118)

_3 of 3 isotopes with a framework prediction; 3 of 3 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{293}$Og | 293 | 175 | -273.0904 | 2073.8540 | -113.17 % | 275473.4438 | +8592.61 ppm |
| ${}^{294}$Og | 294 | 176 | -266.2660 | 2081.2260 | -112.79 % | 276406.1848 | +8566.04 ppm |
| ${}^{295}$Og | 295 | 177 | -259.4489 | 2087.4200 | -112.43 % | 277338.9331 | +8534.08 ppm |

### Magnesium (Z = 12)

_2 of 23 isotopes with a framework prediction; 2 of 23 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{19}$Mg | 19 | 7 | — | 112.1285 | — | — | — |
| ${}^{20}$Mg | 20 | 8 | — | 134.5605 | — | — | — |
| ${}^{21}$Mg | 21 | 9 | — | 149.2057 | — | — | — |
| ${}^{22}$Mg | 22 | 10 | — | 168.5808 | — | — | — |
| ${}^{23}$Mg | 23 | 11 | — | 181.7258 | — | — | — |
| ${}^{24}$Mg | 24 | 12 | 216.1389 | 198.2570 | +9.02 % | 22324.0432 | -800.36 ppm |
| ${}^{25}$Mg | 25 | 13 | — | 205.5876 | — | — | — |
| ${}^{26}$Mg | 26 | 14 | — | 216.6806 | — | — | — |
| ${}^{27}$Mg | 27 | 15 | — | 223.1240 | — | — | — |
| ${}^{28}$Mg | 28 | 16 | — | 231.6287 | — | — | — |
| ${}^{29}$Mg | 29 | 17 | — | 235.2924 | — | — | — |
| ${}^{30}$Mg | 30 | 18 | — | 241.6327 | — | — | — |
| ${}^{31}$Mg | 31 | 19 | — | 243.9448 | — | — | — |
| ${}^{32}$Mg | 32 | 20 | — | 249.7229 | — | — | — |
| ${}^{33}$Mg | 33 | 21 | — | 252.0025 | — | — | — |
| ${}^{34}$Mg | 34 | 22 | — | 256.7133 | — | — | — |
| ${}^{35}$Mg | 35 | 23 | — | 257.4682 | — | — | — |
| ${}^{36}$Mg | 36 | 24 | — | 260.7991 | — | — | — |
| ${}^{37}$Mg | 37 | 25 | — | 261.0391 | — | — | — |
| ${}^{38}$Mg | 38 | 26 | — | 263.2640 | — | — | — |
| ${}^{39}$Mg | 39 | 27 | — | 262.6260 | — | — | — |
| ${}^{40}$Mg | 40 | 28 | — | 263.9200 | — | — | — |
| ${}^{41}$Mg | 41 | 29 | 150.3903 | 263.4250 | -42.91 % | 38362.4040 | +2955.49 ppm |

### Aluminium (Z = 13)

_3 of 23 isotopes with a framework prediction; 3 of 23 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{21}$Al | 21 | 8 | — | 132.2370 | — | — | — |
| ${}^{22}$Al | 22 | 9 | — | 149.2040 | — | — | — |
| ${}^{23}$Al | 23 | 10 | — | 168.7217 | — | — | — |
| ${}^{24}$Al | 24 | 11 | — | 183.5899 | — | — | — |
| ${}^{25}$Al | 25 | 12 | — | 200.5284 | — | — | — |
| ${}^{26}$Al | 26 | 13 | — | 211.8939 | — | — | — |
| ${}^{27}$Al | 27 | 14 | — | 224.9519 | — | — | — |
| ${}^{28}$Al | 28 | 15 | — | 232.6771 | — | — | — |
| ${}^{29}$Al | 29 | 16 | — | 242.1055 | — | — | — |
| ${}^{30}$Al | 30 | 17 | — | 247.8331 | — | — | — |
| ${}^{31}$Al | 31 | 18 | — | 254.9911 | — | — | — |
| ${}^{32}$Al | 32 | 19 | — | 259.2110 | — | — | — |
| ${}^{33}$Al | 33 | 20 | — | 264.6804 | — | — | — |
| ${}^{34}$Al | 34 | 21 | — | 267.2519 | — | — | — |
| ${}^{35}$Al | 35 | 22 | — | 272.5494 | — | — | — |
| ${}^{36}$Al | 36 | 23 | — | 274.4466 | — | — | — |
| ${}^{37}$Al | 37 | 24 | — | 278.6587 | — | — | — |
| ${}^{38}$Al | 38 | 25 | — | 280.0600 | — | — | — |
| ${}^{39}$Al | 39 | 26 | — | 283.1400 | — | — | — |
| ${}^{40}$Al | 40 | 27 | — | 283.8800 | — | — | — |
| ${}^{41}$Al | 41 | 28 | 143.0450 | 286.1800 | -50.02 % | 38368.9670 | +3744.03 ppm |
| ${}^{42}$Al | 42 | 29 | 148.4366 | 286.8180 | -48.25 % | 39303.1408 | +3533.75 ppm |
| ${}^{43}$Al | 43 | 30 | 153.8222 | 288.6160 | -46.70 % | 40237.3207 | +3361.49 ppm |

### Silicon (Z = 14)

_5 of 24 isotopes with a framework prediction; 5 of 24 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{22}$Si | 22 | 8 | — | 132.9680 | — | — | — |
| ${}^{23}$Si | 23 | 9 | — | 150.7420 | — | — | — |
| ${}^{24}$Si | 24 | 10 | — | 172.0136 | — | — | — |
| ${}^{25}$Si | 25 | 11 | — | 187.0028 | — | — | — |
| ${}^{26}$Si | 26 | 12 | — | 206.0424 | — | — | — |
| ${}^{27}$Si | 27 | 13 | — | 219.3572 | — | — | — |
| ${}^{28}$Si | 28 | 14 | — | 236.5368 | — | — | — |
| ${}^{29}$Si | 29 | 15 | — | 245.0104 | — | — | — |
| ${}^{30}$Si | 30 | 16 | — | 255.6196 | — | — | — |
| ${}^{31}$Si | 31 | 17 | — | 262.2070 | — | — | — |
| ${}^{32}$Si | 32 | 18 | — | 271.4070 | — | — | — |
| ${}^{33}$Si | 33 | 19 | — | 275.9150 | — | — | — |
| ${}^{34}$Si | 34 | 20 | — | 283.4636 | — | — | — |
| ${}^{35}$Si | 35 | 21 | — | 285.9348 | — | — | — |
| ${}^{36}$Si | 36 | 22 | — | 292.0507 | — | — | — |
| ${}^{37}$Si | 37 | 23 | — | 294.2574 | — | — | — |
| ${}^{38}$Si | 38 | 24 | — | 299.9275 | — | — | — |
| ${}^{39}$Si | 39 | 25 | — | 301.5082 | — | — | — |
| ${}^{40}$Si | 40 | 26 | — | 306.2330 | — | — | — |
| ${}^{41}$Si | 41 | 27 | 135.2970 | 306.7620 | -55.90 % | 38375.9326 | +4488.33 ppm |
| ${}^{42}$Si | 42 | 28 | 140.7259 | 311.2200 | -54.78 % | 39310.0692 | +4355.62 ppm |
| ${}^{43}$Si | 43 | 29 | 146.1478 | 311.7930 | -53.13 % | 40244.2127 | +4132.80 ppm |
| ${}^{44}$Si | 44 | 30 | 151.5629 | 314.8640 | -51.86 % | 41178.3630 | +3981.76 ppm |
| ${}^{45}$Si | 45 | 31 | 156.9717 | 315.1800 | -50.20 % | 42112.5196 | +3770.64 ppm |

### Phosphorus (Z = 15)

_7 of 24 isotopes with a framework prediction; 7 of 24 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{24}$P | 24 | 9 | — | 147.9600 | — | — | — |
| ${}^{25}$P | 25 | 10 | — | 169.8500 | — | — | — |
| ${}^{26}$P | 26 | 11 | — | 187.1480 | — | — | — |
| ${}^{27}$P | 27 | 12 | — | 206.8494 | — | — | — |
| ${}^{28}$P | 28 | 13 | — | 221.4096 | — | — | — |
| ${}^{29}$P | 29 | 14 | — | 239.2859 | — | — | — |
| ${}^{30}$P | 30 | 15 | — | 250.6052 | — | — | — |
| ${}^{31}$P | 31 | 16 | — | 262.9162 | — | — | — |
| ${}^{32}$P | 32 | 17 | — | 270.8518 | — | — | — |
| ${}^{33}$P | 33 | 18 | — | 280.9556 | — | — | — |
| ${}^{34}$P | 34 | 19 | — | 287.2383 | — | — | — |
| ${}^{35}$P | 35 | 20 | — | 295.6187 | — | — | — |
| ${}^{36}$P | 36 | 21 | — | 299.0833 | — | — | — |
| ${}^{37}$P | 37 | 22 | — | 305.8996 | — | — | — |
| ${}^{38}$P | 38 | 23 | — | 309.5964 | — | — | — |
| ${}^{39}$P | 39 | 24 | — | 315.8208 | — | — | — |
| ${}^{40}$P | 40 | 25 | — | 319.2567 | — | — | — |
| ${}^{41}$P | 41 | 26 | 127.1462 | 324.1686 | -60.78 % | 38383.3011 | +5159.51 ppm |
| ${}^{42}$P | 42 | 27 | 132.6155 | 326.1683 | -59.34 % | 39317.3973 | +4947.19 ppm |
| ${}^{43}$P | 43 | 28 | 138.0765 | 330.2830 | -58.19 % | 40251.5017 | +4798.26 ppm |
| ${}^{44}$P | 44 | 29 | 143.5297 | 332.2880 | -56.81 % | 41185.6139 | +4604.34 ppm |
| ${}^{45}$P | 45 | 30 | 148.9755 | 335.5200 | -55.60 % | 42119.7335 | +4448.47 ppm |
| ${}^{46}$P | 46 | 31 | 154.4143 | 336.7200 | -54.14 % | 43053.8602 | +4252.03 ppm |
| ${}^{47}$P | 47 | 32 | 159.8462 | 338.8230 | -52.82 % | 43987.9936 | +4085.01 ppm |

### Sulfur (Z = 16)

_9 of 24 isotopes with a framework prediction; 9 of 24 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{26}$S | 26 | 10 | — | 169.6500 | — | — | — |
| ${}^{27}$S | 27 | 11 | — | 187.9200 | — | — | — |
| ${}^{28}$S | 28 | 12 | — | 209.4062 | — | — | — |
| ${}^{29}$S | 29 | 13 | — | 224.6451 | — | — | — |
| ${}^{30}$S | 30 | 14 | — | 243.6812 | — | — | — |
| ${}^{31}$S | 31 | 15 | — | 256.7358 | — | — | — |
| ${}^{32}$S | 32 | 16 | — | 271.7802 | — | — | — |
| ${}^{33}$S | 33 | 17 | — | 280.4218 | — | — | — |
| ${}^{34}$S | 34 | 18 | — | 291.8390 | — | — | — |
| ${}^{35}$S | 35 | 19 | — | 298.8248 | — | — | — |
| ${}^{36}$S | 36 | 20 | — | 308.7140 | — | — | — |
| ${}^{37}$S | 37 | 21 | — | 313.0176 | — | — | — |
| ${}^{38}$S | 38 | 22 | — | 321.0538 | — | — | — |
| ${}^{39}$S | 39 | 23 | — | 325.4265 | — | — | — |
| ${}^{40}$S | 40 | 24 | — | 333.1730 | — | — | — |
| ${}^{41}$S | 41 | 25 | 118.5927 | 337.4151 | -64.85 % | 38391.0723 | +5732.50 ppm |
| ${}^{42}$S | 42 | 26 | 124.1053 | 344.1156 | -63.94 % | 39325.1252 | +5626.13 ppm |
| ${}^{43}$S | 43 | 27 | 129.6084 | 346.7446 | -62.62 % | 40259.1875 | +5422.71 ppm |
| ${}^{44}$S | 44 | 28 | 135.1025 | 351.8247 | -61.60 % | 41193.2588 | +5288.94 ppm |
| ${}^{45}$S | 45 | 29 | 140.5880 | 354.0150 | -60.29 % | 42127.3386 | +5092.45 ppm |
| ${}^{46}$S | 46 | 30 | 146.0654 | 358.1100 | -59.21 % | 43061.4267 | +4948.92 ppm |
| ${}^{47}$S | 47 | 31 | 151.5350 | 359.6440 | -57.87 % | 43995.5225 | +4752.49 ppm |
| ${}^{48}$S | 48 | 32 | 156.9972 | 362.4960 | -56.69 % | 44929.6257 | +4595.26 ppm |
| ${}^{49}$S | 49 | 33 | 162.4523 | 362.6000 | -55.20 % | 45863.7361 | +4382.78 ppm |

### Chlorine (Z = 17)

_12 of 25 isotopes with a framework prediction; 12 of 25 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{28}$Cl | 28 | 11 | — | 184.4360 | — | — | — |
| ${}^{29}$Cl | 29 | 12 | — | 206.7410 | — | — | — |
| ${}^{30}$Cl | 30 | 13 | — | 224.1651 | — | — | — |
| ${}^{31}$Cl | 31 | 14 | — | 243.9455 | — | — | — |
| ${}^{32}$Cl | 32 | 15 | — | 258.3170 | — | — | — |
| ${}^{33}$Cl | 33 | 16 | — | 274.0569 | — | — | — |
| ${}^{34}$Cl | 34 | 17 | — | 285.5650 | — | — | — |
| ${}^{35}$Cl | 35 | 18 | — | 298.2098 | — | — | — |
| ${}^{36}$Cl | 36 | 19 | — | 306.7896 | — | — | — |
| ${}^{37}$Cl | 37 | 20 | — | 317.1004 | — | — | — |
| ${}^{38}$Cl | 38 | 21 | — | 323.2083 | — | — | — |
| ${}^{39}$Cl | 39 | 22 | — | 331.2817 | — | — | — |
| ${}^{40}$Cl | 40 | 23 | — | 337.1106 | — | — | — |
| ${}^{41}$Cl | 41 | 24 | 109.6364 | 344.9313 | -68.21 % | 38399.2462 | +6165.38 ppm |
| ${}^{42}$Cl | 42 | 25 | 115.1953 | 350.5272 | -67.14 % | 39333.2528 | +6019.05 ppm |
| ${}^{43}$Cl | 43 | 26 | 120.7433 | 357.9263 | -66.27 % | 40267.2702 | +5925.12 ppm |
| ${}^{44}$Cl | 44 | 27 | 126.2812 | 362.3171 | -65.15 % | 41201.2978 | +5761.86 ppm |
| ${}^{45}$Cl | 45 | 28 | 131.8092 | 368.1720 | -64.20 % | 42135.3351 | +5641.26 ppm |
| ${}^{46}$Cl | 46 | 29 | 137.3279 | 371.7157 | -63.06 % | 43069.3818 | +5471.88 ppm |
| ${}^{47}$Cl | 47 | 30 | 142.8378 | 375.6240 | -61.97 % | 44003.4374 | +5318.52 ppm |
| ${}^{48}$Cl | 48 | 31 | 148.3392 | 378.3840 | -60.80 % | 44937.5014 | +5146.00 ppm |
| ${}^{49}$Cl | 49 | 32 | 153.8324 | 381.4650 | -59.67 % | 45871.5736 | +4986.92 ppm |
| ${}^{50}$Cl | 50 | 33 | 159.3179 | 382.5500 | -58.35 % | 46805.6535 | +4792.55 ppm |
| ${}^{51}$Cl | 51 | 34 | 164.7960 | 384.0300 | -57.09 % | 47739.7409 | +4613.83 ppm |
| ${}^{52}$Cl | 52 | 35 | 170.2670 | 384.0720 | -55.67 % | 48673.8353 | +4411.52 ppm |

### Argon (Z = 18)

_14 of 26 isotopes with a framework prediction; 14 of 26 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{29}$Ar | 29 | 11 | — | 182.0040 | — | — | — |
| ${}^{30}$Ar | 30 | 12 | — | 205.9800 | — | — | — |
| ${}^{31}$Ar | 31 | 13 | — | 224.8120 | — | — | — |
| ${}^{32}$Ar | 32 | 14 | — | 246.4003 | — | — | — |
| ${}^{33}$Ar | 33 | 15 | — | 261.6555 | — | — | — |
| ${}^{34}$Ar | 34 | 16 | — | 278.7209 | — | — | — |
| ${}^{35}$Ar | 35 | 17 | — | 291.4612 | — | — | — |
| ${}^{36}$Ar | 36 | 18 | — | 306.7167 | — | — | — |
| ${}^{37}$Ar | 37 | 19 | — | 315.5042 | — | — | — |
| ${}^{38}$Ar | 38 | 20 | — | 327.3427 | — | — | — |
| ${}^{39}$Ar | 39 | 21 | — | 333.9414 | — | — | — |
| ${}^{40}$Ar | 40 | 22 | — | 343.8104 | — | — | — |
| ${}^{41}$Ar | 41 | 23 | 100.2774 | 349.9093 | -71.34 % | 38407.8229 | +6542.03 ppm |
| ${}^{42}$Ar | 42 | 24 | 105.8855 | 359.3358 | -70.53 % | 39341.7802 | +6484.05 ppm |
| ${}^{43}$Ar | 43 | 25 | 111.4815 | 364.9942 | -69.46 % | 40275.7497 | +6334.30 ppm |
| ${}^{44}$Ar | 44 | 26 | 117.0658 | 373.7290 | -68.68 % | 41209.7308 | +6267.26 ppm |
| ${}^{45}$Ar | 45 | 27 | 122.6391 | 378.8979 | -67.63 % | 42143.7229 | +6117.80 ppm |
| ${}^{46}$Ar | 46 | 28 | 128.2018 | 386.9696 | -66.87 % | 43077.7256 | +6043.31 ppm |
| ${}^{47}$Ar | 47 | 29 | 133.7545 | 390.6370 | -65.76 % | 44011.7384 | +5870.95 ppm |
| ${}^{48}$Ar | 48 | 30 | 139.2976 | 395.6959 | -64.80 % | 44945.7607 | +5737.35 ppm |
| ${}^{49}$Ar | 49 | 31 | 144.8315 | 398.4680 | -63.65 % | 45879.7922 | +5559.12 ppm |
| ${}^{50}$Ar | 50 | 32 | 150.3566 | 402.7000 | -62.66 % | 46813.8325 | +5419.87 ppm |
| ${}^{51}$Ar | 51 | 33 | 155.8733 | 404.0220 | -61.42 % | 47747.8812 | +5224.70 ppm |
| ${}^{52}$Ar | 52 | 34 | 161.3820 | 407.0040 | -60.35 % | 48681.9380 | +5071.07 ppm |
| ${}^{53}$Ar | 53 | 35 | 166.8830 | 406.8810 | -58.98 % | 49616.0024 | +4861.16 ppm |
| ${}^{54}$Ar | 54 | 36 | 172.3765 | 409.2120 | -57.88 % | 50550.0743 | +4707.16 ppm |

### Potassium (Z = 19)

_19 of 29 isotopes with a framework prediction; 19 of 29 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{31}$K | 31 | 12 | — | 201.0970 | — | — | — |
| ${}^{32}$K | 32 | 13 | — | 221.4400 | — | — | — |
| ${}^{33}$K | 33 | 14 | — | 243.9360 | — | — | — |
| ${}^{34}$K | 34 | 15 | — | 260.7800 | — | — | — |
| ${}^{35}$K | 35 | 16 | — | 278.8044 | — | — | — |
| ${}^{36}$K | 36 | 17 | — | 293.1200 | — | — | — |
| ${}^{37}$K | 37 | 18 | — | 308.5744 | — | — | — |
| ${}^{38}$K | 38 | 19 | — | 320.6463 | — | — | — |
| ${}^{39}$K | 39 | 20 | — | 333.7240 | — | — | — |
| ${}^{40}$K | 40 | 21 | — | 341.5236 | — | — | — |
| ${}^{41}$K | 41 | 22 | 90.5156 | 351.6190 | -74.26 % | 38416.8024 | +6843.11 ppm |
| ${}^{42}$K | 42 | 23 | 96.1760 | 359.1528 | -73.22 % | 39350.7074 | +6727.87 ppm |
| ${}^{43}$K | 43 | 24 | 101.8227 | 368.7775 | -72.39 % | 40284.6261 | +6670.93 ppm |
| ${}^{44}$K | 44 | 25 | 107.4564 | 376.0549 | -71.43 % | 41218.5579 | +6559.20 ppm |
| ${}^{45}$K | 45 | 26 | 113.0776 | 384.9604 | -70.63 % | 42152.5021 | +6491.86 ppm |
| ${}^{46}$K | 46 | 27 | 118.6870 | 391.8300 | -69.71 % | 43086.4581 | +6379.87 ppm |
| ${}^{47}$K | 47 | 28 | 124.2851 | 400.1993 | -68.94 % | 44020.4254 | +6307.41 ppm |
| ${}^{48}$K | 48 | 29 | 129.8724 | 404.8432 | -67.92 % | 44954.4035 | +6154.31 ppm |
| ${}^{49}$K | 49 | 30 | 135.4494 | 410.2415 | -66.98 % | 45888.3920 | +6024.35 ppm |
| ${}^{50}$K | 50 | 31 | 141.0166 | 414.4292 | -65.97 % | 46822.3902 | +5873.66 ppm |
| ${}^{51}$K | 51 | 32 | 146.5743 | 419.2881 | -65.04 % | 47756.3979 | +5743.32 ppm |
| ${}^{52}$K | 52 | 33 | 152.1229 | 421.9816 | -63.95 % | 48690.4147 | +5573.23 ppm |
| ${}^{53}$K | 53 | 34 | 157.6629 | 425.2110 | -62.92 % | 49624.4401 | +5420.69 ppm |
| ${}^{54}$K | 54 | 35 | 163.1946 | 426.1140 | -61.70 % | 50558.4739 | +5227.95 ppm |
| ${}^{55}$K | 55 | 36 | 168.7183 | 428.5600 | -60.63 % | 51492.5156 | +5072.34 ppm |
| ${}^{56}$K | 56 | 37 | 174.2343 | 429.1280 | -59.40 % | 52426.5650 | +4886.08 ppm |
| ${}^{57}$K | 57 | 38 | 179.7430 | 431.0910 | -58.31 % | 53360.6218 | +4732.28 ppm |
| ${}^{58}$K | 58 | 39 | 185.2445 | 431.3460 | -57.05 % | 54294.6857 | +4553.26 ppm |
| ${}^{59}$K | 59 | 40 | 190.7392 | 432.5880 | -55.91 % | 55228.7564 | +4398.40 ppm |

### Calcium (Z = 20)

_22 of 29 isotopes with a framework prediction; 22 of 29 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{33}$Ca | 33 | 13 | — | 219.6810 | — | — | — |
| ${}^{34}$Ca | 34 | 14 | — | 243.8820 | — | — | — |
| ${}^{35}$Ca | 35 | 15 | — | 261.6600 | — | — | — |
| ${}^{36}$Ca | 36 | 16 | — | 281.3717 | — | — | — |
| ${}^{37}$Ca | 37 | 17 | — | 296.1279 | — | — | — |
| ${}^{38}$Ca | 38 | 18 | — | 313.1216 | — | — | — |
| ${}^{39}$Ca | 39 | 19 | — | 326.4172 | — | — | — |
| ${}^{40}$Ca | 40 | 20 | 408.7713 | 342.0522 | +19.51 % | 37158.1989 | -1792.32 ppm |
| ${}^{41}$Ca | 41 | 21 | 80.3511 | 350.4150 | -77.07 % | 38426.1846 | +7077.87 ppm |
| ${}^{42}$Ca | 42 | 22 | 86.0667 | 361.8957 | -76.22 % | 39360.0343 | +7057.31 ppm |
| ${}^{43}$Ca | 43 | 23 | 91.7671 | 369.8286 | -75.19 % | 40293.8994 | +6948.79 ppm |
| ${}^{44}$Ca | 44 | 24 | 97.4529 | 380.9598 | -74.42 % | 41227.7790 | +6924.22 ppm |
| ${}^{45}$Ca | 45 | 25 | 103.1248 | 388.3746 | -73.45 % | 42161.6725 | +6811.71 ppm |
| ${}^{46}$Ca | 46 | 26 | 108.7835 | 398.7733 | -72.72 % | 43095.5792 | +6774.58 ppm |
| ${}^{47}$Ca | 47 | 27 | 114.4296 | 406.0497 | -71.82 % | 44029.4985 | +6667.45 ppm |
| ${}^{48}$Ca | 48 | 28 | 120.0637 | 416.0012 | -71.14 % | 44963.4299 | +6625.35 ppm |
| ${}^{49}$Ca | 49 | 29 | 125.6863 | 421.1476 | -70.16 % | 45897.3728 | +6479.15 ppm |
| ${}^{50}$Ca | 50 | 30 | 131.2978 | 427.5082 | -69.29 % | 46831.3266 | +6365.32 ppm |
| ${}^{51}$Ca | 51 | 31 | 136.8988 | 432.3226 | -68.33 % | 47765.2910 | +6223.40 ppm |
| ${}^{52}$Ca | 52 | 32 | 142.4898 | 438.3279 | -67.49 % | 48699.2655 | +6111.93 ppm |
| ${}^{53}$Ca | 53 | 33 | 148.0710 | 441.5206 | -66.46 % | 49633.2497 | +5947.53 ppm |
| ${}^{54}$Ca | 54 | 34 | 153.6430 | 445.3648 | -65.50 % | 50567.2431 | +5802.47 ppm |
| ${}^{55}$Ca | 55 | 35 | 159.2061 | 446.9259 | -64.38 % | 51501.2455 | +5618.05 ppm |
| ${}^{56}$Ca | 56 | 36 | 164.7606 | 449.8573 | -63.37 % | 52435.2564 | +5466.85 ppm |
| ${}^{57}$Ca | 57 | 37 | 170.3069 | 450.9840 | -62.24 % | 53369.2755 | +5286.84 ppm |
| ${}^{58}$Ca | 58 | 38 | 175.8452 | 454.0240 | -61.27 % | 54303.3026 | +5148.99 ppm |
| ${}^{59}$Ca | 59 | 39 | 181.3760 | 454.7720 | -60.12 % | 55237.3373 | +4973.72 ppm |
| ${}^{60}$Ca | 60 | 40 | 186.8994 | 457.6200 | -59.16 % | 56171.3793 | +4843.11 ppm |
| ${}^{61}$Ca | 61 | 41 | 192.4157 | 457.6830 | -57.96 % | 57105.4284 | +4667.09 ppm |

### Scandium (Z = 21)

_23 of 29 isotopes with a framework prediction; 23 of 29 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{35}$Sc | 35 | 14 | — | 238.9800 | — | — | — |
| ${}^{36}$Sc | 36 | 15 | — | 257.9760 | — | — | — |
| ${}^{37}$Sc | 37 | 16 | — | 278.4250 | — | — | — |
| ${}^{38}$Sc | 38 | 17 | — | 294.5380 | — | — | — |
| ${}^{39}$Sc | 39 | 18 | — | 312.5248 | — | — | — |
| ${}^{40}$Sc | 40 | 19 | — | 326.9468 | — | — | — |
| ${}^{41}$Sc | 41 | 20 | 69.7838 | 343.1371 | -79.66 % | 38435.9696 | +7162.86 ppm |
| ${}^{42}$Sc | 42 | 21 | 75.5577 | 354.6871 | -78.70 % | 39369.7610 | +7140.58 ppm |
| ${}^{43}$Sc | 43 | 22 | 81.3146 | 366.8255 | -77.83 % | 40303.5695 | +7134.56 ppm |
| ${}^{44}$Sc | 44 | 23 | 87.0554 | 376.5247 | -76.88 % | 41237.3942 | +7069.21 ppm |
| ${}^{45}$Sc | 45 | 24 | 92.7808 | 387.8523 | -76.08 % | 42171.2343 | +7046.30 ppm |
| ${}^{46}$Sc | 46 | 25 | 98.4914 | 396.6130 | -75.17 % | 43105.0890 | +6964.33 ppm |
| ${}^{47}$Sc | 47 | 26 | 104.1881 | 407.2595 | -74.42 % | 44038.9577 | +6929.59 ppm |
| ${}^{48}$Sc | 48 | 27 | 109.8715 | 415.4981 | -73.56 % | 44972.8398 | +6842.31 ppm |
| ${}^{49}$Sc | 49 | 28 | 115.5420 | 425.6277 | -72.85 % | 45906.7347 | +6800.63 ppm |
| ${}^{50}$Sc | 50 | 29 | 121.2004 | 431.6737 | -71.92 % | 46840.6417 | +6672.52 ppm |
| ${}^{51}$Sc | 51 | 30 | 126.8471 | 438.4583 | -71.07 % | 47774.5605 | +6565.36 ppm |
| ${}^{52}$Sc | 52 | 31 | 132.4825 | 443.8028 | -70.15 % | 48708.4904 | +6432.62 ppm |
| ${}^{53}$Sc | 53 | 32 | 138.1073 | 450.1201 | -69.32 % | 49642.4311 | +6324.96 ppm |
| ${}^{54}$Sc | 54 | 33 | 143.7218 | 453.8598 | -68.33 % | 50576.3821 | +6169.91 ppm |
| ${}^{55}$Sc | 55 | 34 | 149.3263 | 458.3353 | -67.42 % | 51510.3429 | +6035.18 ppm |
| ${}^{56}$Sc | 56 | 35 | 154.9214 | 461.0804 | -66.40 % | 52444.3133 | +5872.08 ppm |
| ${}^{57}$Sc | 57 | 36 | 160.5073 | 465.0155 | -65.48 % | 53378.2927 | +5737.46 ppm |
| ${}^{58}$Sc | 58 | 37 | 166.0845 | 467.1867 | -64.45 % | 54312.2810 | +5574.82 ppm |
| ${}^{59}$Sc | 59 | 38 | 171.6532 | 470.6080 | -63.53 % | 55246.2777 | +5440.76 ppm |
| ${}^{60}$Sc | 60 | 39 | 177.2137 | 472.3800 | -62.48 % | 56180.2826 | +5282.03 ppm |
| ${}^{61}$Sc | 61 | 40 | 182.7664 | 475.4340 | -61.56 % | 57114.2954 | +5150.41 ppm |
| ${}^{62}$Sc | 62 | 41 | 188.3115 | 476.6560 | -60.49 % | 58048.3157 | +4992.58 ppm |
| ${}^{63}$Sc | 63 | 42 | 193.8493 | 478.9890 | -59.53 % | 58982.3433 | +4857.90 ppm |

### Titanium (Z = 22)

_25 of 29 isotopes with a framework prediction; 25 of 29 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{37}$Ti | 37 | 15 | — | 256.2620 | — | — | — |
| ${}^{38}$Ti | 38 | 16 | — | 278.1220 | — | — | — |
| ${}^{39}$Ti | 39 | 17 | — | 295.0740 | — | — | — |
| ${}^{40}$Ti | 40 | 18 | — | 314.6345 | — | — | — |
| ${}^{41}$Ti | 41 | 19 | 58.8137 | 329.4099 | -82.15 % | 38446.1573 | +7088.21 ppm |
| ${}^{42}$Ti | 42 | 20 | 64.6489 | 346.8881 | -81.36 % | 39379.8875 | +7218.84 ppm |
| ${}^{43}$Ti | 43 | 21 | 70.4653 | 359.1706 | -80.38 % | 40313.6365 | +7213.15 ppm |
| ${}^{44}$Ti | 44 | 22 | 76.2638 | 375.4749 | -79.69 % | 41247.4034 | +7307.07 ppm |
| ${}^{45}$Ti | 45 | 23 | 82.0454 | 385.0079 | -78.69 % | 42181.1873 | +7234.38 ppm |
| ${}^{46}$Ti | 46 | 24 | 87.8107 | 398.1973 | -77.95 % | 43114.9874 | +7251.25 ppm |
| ${}^{47}$Ti | 47 | 25 | 93.5606 | 407.0779 | -77.02 % | 44048.8030 | +7168.53 ppm |
| ${}^{48}$Ti | 48 | 26 | 99.2957 | 418.7046 | -76.29 % | 44982.6333 | +7151.50 ppm |
| ${}^{49}$Ti | 49 | 27 | 105.0167 | 426.8470 | -75.40 % | 45916.4776 | +7058.52 ppm |
| ${}^{50}$Ti | 50 | 28 | 110.7243 | 437.7861 | -74.71 % | 46850.3355 | +7030.08 ppm |
| ${}^{51}$Ti | 51 | 29 | 116.4189 | 444.1586 | -73.79 % | 47784.2063 | +6906.12 ppm |
| ${}^{52}$Ti | 52 | 30 | 122.1012 | 451.9746 | -72.98 % | 48718.0894 | +6817.23 ppm |
| ${}^{53}$Ti | 53 | 31 | 127.7717 | 457.4497 | -72.07 % | 49651.9844 | +6684.16 ppm |
| ${}^{54}$Ti | 54 | 32 | 133.4308 | 464.3834 | -71.27 % | 50585.8907 | +6585.48 ppm |
| ${}^{55}$Ti | 55 | 33 | 139.0790 | 468.5433 | -70.32 % | 51519.8079 | +6436.07 ppm |
| ${}^{56}$Ti | 56 | 34 | 144.7167 | 474.2052 | -69.48 % | 52453.7357 | +6321.22 ppm |
| ${}^{57}$Ti | 57 | 35 | 150.3443 | 477.2553 | -68.50 % | 53387.6735 | +6161.08 ppm |
| ${}^{58}$Ti | 58 | 36 | 155.9622 | 481.8425 | -67.63 % | 54321.6210 | +6035.30 ppm |
| ${}^{59}$Ti | 59 | 37 | 161.5708 | 484.8620 | -66.68 % | 55255.5778 | +5885.53 ppm |
| ${}^{60}$Ti | 60 | 38 | 167.1704 | 489.1671 | -65.83 % | 56189.5436 | +5763.58 ppm |
| ${}^{61}$Ti | 61 | 39 | 172.7613 | 491.5380 | -64.85 % | 57123.5181 | +5611.29 ppm |
| ${}^{62}$Ti | 62 | 40 | 178.3439 | 495.3800 | -64.00 % | 58057.5009 | +5491.23 ppm |
| ${}^{63}$Ti | 63 | 41 | 183.9184 | 497.1330 | -63.00 % | 58991.4918 | +5337.98 ppm |
| ${}^{64}$Ti | 64 | 42 | 189.4852 | 500.8640 | -62.17 % | 59925.4905 | +5222.72 ppm |
| ${}^{65}$Ti | 65 | 43 | 195.0444 | 502.1900 | -61.16 % | 60859.4967 | +5072.80 ppm |

### Vanadium (Z = 23)

_27 of 29 isotopes with a framework prediction; 27 of 29 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{39}$V | 39 | 16 | — | 274.2090 | — | — | — |
| ${}^{40}$V | 40 | 17 | — | 292.4000 | — | — | — |
| ${}^{41}$V | 41 | 18 | 47.4409 | 312.6250 | -84.82 % | 38456.7477 | +6943.40 ppm |
| ${}^{42}$V | 42 | 19 | 53.3403 | 328.6080 | -83.77 % | 39390.4137 | +7037.71 ppm |
| ${}^{43}$V | 43 | 20 | 59.2191 | 346.9891 | -82.93 % | 40324.1004 | +7187.73 ppm |
| ${}^{44}$V | 44 | 21 | 65.0782 | 360.9521 | -81.97 % | 41257.8067 | +7223.15 ppm |
| ${}^{45}$V | 45 | 22 | 70.9186 | 377.1018 | -81.19 % | 42191.5317 | +7310.04 ppm |
| ${}^{46}$V | 46 | 23 | 76.7413 | 390.3625 | -80.34 % | 43125.2745 | +7325.61 ppm |
| ${}^{47}$V | 47 | 24 | 82.5469 | 403.3650 | -79.54 % | 44059.0343 | +7334.97 ppm |
| ${}^{48}$V | 48 | 25 | 88.3364 | 413.9073 | -78.66 % | 44992.8102 | +7288.82 ppm |
| ${}^{49}$V | 49 | 26 | 94.1103 | 425.4628 | -77.88 % | 45926.6017 | +7267.27 ppm |
| ${}^{50}$V | 50 | 27 | 99.8695 | 434.7952 | -77.03 % | 46860.4080 | +7198.77 ppm |
| ${}^{51}$V | 51 | 28 | 105.6144 | 445.8463 | -76.31 % | 47794.2284 | +7169.73 ppm |
| ${}^{52}$V | 52 | 29 | 111.3458 | 453.1576 | -75.43 % | 48728.0625 | +7064.24 ppm |
| ${}^{53}$V | 53 | 30 | 117.0642 | 461.6376 | -74.64 % | 49661.9095 | +6986.87 ppm |
| ${}^{54}$V | 54 | 31 | 122.7701 | 467.7555 | -73.75 % | 50595.7690 | +6865.28 ppm |
| ${}^{55}$V | 55 | 32 | 128.4640 | 475.0537 | -72.96 % | 51529.6405 | +6771.58 ppm |
| ${}^{56}$V | 56 | 33 | 134.1464 | 480.1832 | -72.06 % | 52463.5236 | +6639.56 ppm |
| ${}^{57}$V | 57 | 34 | 139.8177 | 486.5062 | -71.26 % | 53397.4177 | +6535.04 ppm |
| ${}^{58}$V | 58 | 35 | 145.4784 | 490.5730 | -70.35 % | 54331.3224 | +6392.28 ppm |
| ${}^{59}$V | 59 | 36 | 151.1289 | 495.8244 | -69.52 % | 55265.2374 | +6276.27 ppm |
| ${}^{60}$V | 60 | 37 | 156.7694 | 499.3725 | -68.61 % | 56199.1623 | +6133.63 ppm |
| ${}^{61}$V | 61 | 38 | 162.4005 | 504.5335 | -67.81 % | 57133.0966 | +6024.43 ppm |
| ${}^{62}$V | 62 | 39 | 168.0223 | 507.6409 | -66.90 % | 58067.0402 | +5883.15 ppm |
| ${}^{63}$V | 63 | 40 | 173.6353 | 512.2392 | -66.10 % | 59000.9926 | +5772.08 ppm |
| ${}^{64}$V | 64 | 41 | 179.2398 | 514.8800 | -65.19 % | 59934.9536 | +5631.79 ppm |
| ${}^{65}$V | 65 | 42 | 184.8360 | 518.7650 | -64.37 % | 60868.9228 | +5516.09 ppm |
| ${}^{66}$V | 66 | 43 | 190.4242 | 521.0040 | -63.45 % | 61802.9000 | +5377.85 ppm |
| ${}^{67}$V | 67 | 44 | 196.0047 | 524.5430 | -62.63 % | 62736.8849 | +5264.10 ppm |

### Chromium (Z = 24)

_30 of 30 isotopes with a framework prediction; 30 of 30 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{41}$Cr | 41 | 17 | 35.6653 | 291.7560 | -87.78 % | 38467.7410 | +6701.43 ppm |
| ${}^{42}$Cr | 42 | 18 | 41.6320 | 313.1520 | -86.71 % | 39401.3397 | +6939.15 ppm |
| ${}^{43}$Cr | 43 | 19 | 47.5760 | 330.2400 | -85.59 % | 40334.9611 | +7057.90 ppm |
| ${}^{44}$Cr | 44 | 20 | 53.4985 | 349.7836 | -84.71 % | 41268.6040 | +7231.35 ppm |
| ${}^{45}$Cr | 45 | 21 | 59.4006 | 363.9478 | -83.68 % | 42202.2674 | +7268.83 ppm |
| ${}^{46}$Cr | 46 | 22 | 65.2832 | 381.9759 | -82.91 % | 43135.9502 | +7396.04 ppm |
| ${}^{47}$Cr | 47 | 23 | 71.1472 | 395.1387 | -81.99 % | 44069.6516 | +7406.26 ppm |
| ${}^{48}$Cr | 48 | 24 | 76.9935 | 411.4683 | -81.29 % | 45003.3708 | +7487.88 ppm |
| ${}^{49}$Cr | 49 | 25 | 82.8228 | 422.0506 | -80.38 % | 45937.1069 | +7439.56 ppm |
| ${}^{50}$Cr | 50 | 26 | 88.6359 | 435.0509 | -79.63 % | 46870.8592 | +7445.88 ppm |
| ${}^{51}$Cr | 51 | 27 | 94.4336 | 444.3116 | -78.75 % | 47804.6270 | +7372.89 ppm |
| ${}^{52}$Cr | 52 | 28 | 100.2163 | 456.3517 | -78.04 % | 48738.4096 | +7360.87 ppm |
| ${}^{53}$Cr | 53 | 29 | 105.9849 | 464.2911 | -77.17 % | 49672.2065 | +7265.83 ppm |
| ${}^{54}$Cr | 54 | 30 | 111.7397 | 474.0102 | -76.43 % | 50606.0171 | +7210.27 ppm |
| ${}^{55}$Cr | 55 | 31 | 117.4815 | 480.2565 | -75.54 % | 51539.8407 | +7088.63 ppm |
| ${}^{56}$Cr | 56 | 32 | 123.2107 | 488.5026 | -74.78 % | 52473.6770 | +7010.24 ppm |
| ${}^{57}$Cr | 57 | 33 | 128.9277 | 493.8138 | -73.89 % | 53407.5253 | +6879.12 ppm |
| ${}^{58}$Cr | 58 | 34 | 134.6331 | 501.3519 | -73.15 % | 54341.3854 | +6794.28 ppm |
| ${}^{59}$Cr | 59 | 35 | 140.3273 | 505.5474 | -72.24 % | 55275.2566 | +6651.25 ppm |
| ${}^{60}$Cr | 60 | 36 | 146.0107 | 512.4113 | -71.51 % | 56209.1386 | +6561.30 ppm |
| ${}^{61}$Cr | 61 | 37 | 151.6837 | 516.0706 | -70.61 % | 57143.0310 | +6417.68 ppm |
| ${}^{62}$Cr | 62 | 38 | 157.3467 | 522.4980 | -69.89 % | 58076.9335 | +6327.16 ppm |
| ${}^{63}$Cr | 63 | 39 | 163.0000 | 525.8950 | -69.01 % | 59010.8456 | +6187.69 ppm |
| ${}^{64}$Cr | 64 | 40 | 168.6439 | 531.4280 | -68.27 % | 59944.7671 | +6088.83 ppm |
| ${}^{65}$Cr | 65 | 41 | 174.2788 | 534.1700 | -67.37 % | 60878.6976 | +5946.76 ppm |
| ${}^{66}$Cr | 66 | 42 | 179.9050 | 539.0880 | -66.63 % | 61812.6369 | +5844.52 ppm |
| ${}^{67}$Cr | 67 | 43 | 185.5227 | 541.2930 | -65.73 % | 62746.5846 | +5701.95 ppm |
| ${}^{68}$Cr | 68 | 44 | 191.1323 | 545.7680 | -64.98 % | 63680.5404 | +5600.10 ppm |
| ${}^{69}$Cr | 69 | 45 | 196.7340 | 547.7910 | -64.09 % | 64614.5042 | +5462.53 ppm |
| ${}^{70}$Cr | 70 | 46 | 202.3280 | 551.8800 | -63.34 % | 65548.4756 | +5360.95 ppm |

### Manganese (Z = 25)

_31 of 31 isotopes with a framework prediction; 31 of 31 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{43}$Mn | 43 | 18 | 35.5361 | 310.1590 | -88.54 % | 40346.2188 | +6852.80 ppm |
| ${}^{44}$Mn | 44 | 19 | 41.5248 | 328.1080 | -87.34 % | 41279.7954 | +6991.27 ppm |
| ${}^{45}$Mn | 45 | 20 | 47.4913 | 348.6150 | -86.38 % | 42213.3944 | +7185.00 ppm |
| ${}^{46}$Mn | 46 | 21 | 53.4365 | 364.1397 | -85.33 % | 43147.0146 | +7253.28 ppm |
| ${}^{47}$Mn | 47 | 22 | 59.3614 | 382.3596 | -84.47 % | 44080.6551 | +7381.53 ppm |
| ${}^{48}$Mn | 48 | 23 | 65.2671 | 397.1612 | -83.57 % | 45014.3149 | +7427.85 ppm |
| ${}^{49}$Mn | 49 | 24 | 71.1542 | 413.5558 | -82.79 % | 45947.9931 | +7507.89 ppm |
| ${}^{50}$Mn | 50 | 25 | 77.0237 | 426.6341 | -81.95 % | 46881.6890 | +7513.33 ppm |
| ${}^{51}$Mn | 51 | 26 | 82.8763 | 440.3218 | -81.18 % | 47815.4019 | +7531.84 ppm |
| ${}^{52}$Mn | 52 | 27 | 88.7127 | 450.8613 | -80.32 % | 48749.1309 | +7484.43 ppm |
| ${}^{53}$Mn | 53 | 28 | 94.5336 | 462.9115 | -79.58 % | 49682.8754 | +7469.98 ppm |
| ${}^{54}$Mn | 54 | 29 | 100.3397 | 471.8507 | -78.73 % | 50616.6348 | +7393.98 ppm |
| ${}^{55}$Mn | 55 | 30 | 106.1314 | 482.0764 | -77.98 % | 51550.4085 | +7346.35 ppm |
| ${}^{56}$Mn | 56 | 31 | 111.9094 | 489.3468 | -77.13 % | 52484.1959 | +7243.55 ppm |
| ${}^{57}$Mn | 57 | 32 | 117.6742 | 497.9927 | -76.37 % | 53417.9965 | +7170.73 ppm |
| ${}^{58}$Mn | 58 | 33 | 123.4263 | 504.4053 | -75.53 % | 54351.8098 | +7058.99 ppm |
| ${}^{59}$Mn | 59 | 34 | 129.1663 | 512.1744 | -74.78 % | 55285.6353 | +6976.14 ppm |
| ${}^{60}$Mn | 60 | 35 | 134.8944 | 517.6884 | -73.94 % | 56219.4726 | +6855.61 ppm |
| ${}^{61}$Mn | 61 | 36 | 140.6112 | 524.5339 | -73.19 % | 57153.3212 | +6762.85 ppm |
| ${}^{62}$Mn | 62 | 37 | 146.3171 | 529.3870 | -72.36 % | 58087.1808 | +6638.53 ppm |
| ${}^{63}$Mn | 63 | 38 | 152.0124 | 535.8214 | -71.63 % | 59021.0509 | +6545.49 ppm |
| ${}^{64}$Mn | 64 | 39 | 157.6975 | 539.9947 | -70.80 % | 59954.9312 | +6417.34 ppm |
| ${}^{65}$Mn | 65 | 40 | 163.3729 | 546.0443 | -70.08 % | 60888.8213 | +6324.51 ppm |
| ${}^{66}$Mn | 66 | 41 | 169.0387 | 549.8987 | -69.26 % | 61822.7209 | +6198.71 ppm |
| ${}^{67}$Mn | 67 | 42 | 174.6953 | 554.8270 | -68.51 % | 62756.6297 | +6093.72 ppm |
| ${}^{68}$Mn | 68 | 43 | 180.3430 | 558.2120 | -67.69 % | 63690.5474 | +5968.29 ppm |
| ${}^{69}$Mn | 69 | 44 | 185.9821 | 562.6950 | -66.95 % | 64624.4737 | +5863.87 ppm |
| ${}^{70}$Mn | 70 | 45 | 191.6129 | 565.8800 | -66.14 % | 65558.4083 | +5741.75 ppm |
| ${}^{71}$Mn | 71 | 46 | 197.2356 | 570.1300 | -65.41 % | 66492.3511 | +5639.63 ppm |
| ${}^{72}$Mn | 72 | 47 | 202.8505 | 572.7600 | -64.58 % | 67426.3016 | +5516.19 ppm |
| ${}^{73}$Mn | 73 | 48 | 208.4578 | 576.3350 | -63.83 % | 68360.2597 | +5410.76 ppm |

### Iron (Z = 26)

_32 of 32 isotopes with a framework prediction; 32 of 32 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{45}$Fe | 45 | 19 | 35.1906 | 328.4550 | -89.29 % | 42224.9127 | +6994.02 ppm |
| ${}^{46}$Fe | 46 | 20 | 41.2011 | 349.7380 | -88.22 % | 43158.4676 | +7200.22 ppm |
| ${}^{47}$Fe | 47 | 21 | 47.1896 | 366.1300 | -87.11 % | 44092.0446 | +7286.47 ppm |
| ${}^{48}$Fe | 48 | 22 | 53.1571 | 385.0908 | -86.20 % | 45025.6425 | +7426.86 ppm |
| ${}^{49}$Fe | 49 | 23 | 59.1046 | 399.9043 | -85.22 % | 45959.2605 | +7470.66 ppm |
| ${}^{50}$Fe | 50 | 24 | 65.0328 | 417.7013 | -84.43 % | 46892.8976 | +7577.72 ppm |
| ${}^{51}$Fe | 51 | 25 | 70.9427 | 431.4854 | -83.56 % | 47826.5531 | +7595.81 ppm |
| ${}^{52}$Fe | 52 | 26 | 76.8351 | 447.6996 | -82.84 % | 48760.2262 | +7664.18 ppm |
| ${}^{53}$Fe | 53 | 27 | 82.7106 | 458.3863 | -81.96 % | 49693.9161 | +7617.39 ppm |
| ${}^{54}$Fe | 54 | 28 | 88.5699 | 471.7648 | -81.23 % | 50627.6222 | +7626.62 ppm |
| ${}^{55}$Fe | 55 | 29 | 94.4137 | 481.0629 | -80.37 % | 51561.3438 | +7555.48 ppm |
| ${}^{56}$Fe | 56 | 30 | 100.2426 | 492.2600 | -79.64 % | 52495.0803 | +7523.89 ppm |
| ${}^{57}$Fe | 57 | 31 | 106.0572 | 499.9061 | -78.78 % | 53428.8312 | +7426.22 ppm |
| ${}^{58}$Fe | 58 | 32 | 111.8580 | 509.9507 | -78.06 % | 54362.5958 | +7376.94 ppm |
| ${}^{59}$Fe | 59 | 33 | 117.6456 | 516.5317 | -77.22 % | 55296.3737 | +7266.02 ppm |
| ${}^{60}$Fe | 60 | 34 | 123.4204 | 525.3512 | -76.51 % | 56230.1643 | +7199.43 ppm |
| ${}^{61}$Fe | 61 | 35 | 129.1829 | 530.9299 | -75.67 % | 57163.9672 | +7077.73 ppm |
| ${}^{62}$Fe | 62 | 36 | 134.9335 | 538.9588 | -74.96 % | 58097.7821 | +7002.94 ppm |
| ${}^{63}$Fe | 63 | 37 | 140.6726 | 543.7876 | -74.13 % | 59031.6083 | +6875.76 ppm |
| ${}^{64}$Fe | 64 | 38 | 146.4007 | 551.1929 | -73.44 % | 59965.4457 | +6796.31 ppm |
| ${}^{65}$Fe | 65 | 39 | 152.1181 | 555.5126 | -72.62 % | 60899.2937 | +6668.14 ppm |
| ${}^{66}$Fe | 66 | 40 | 157.8252 | 562.4338 | -71.94 % | 61833.1520 | +6586.66 ppm |
| ${}^{67}$Fe | 67 | 41 | 163.5224 | 566.1457 | -71.12 % | 62767.0203 | +6455.99 ppm |
| ${}^{68}$Fe | 68 | 42 | 169.2098 | 572.4240 | -70.44 % | 63700.8982 | +6369.83 ppm |
| ${}^{69}$Fe | 69 | 43 | 174.8880 | 575.8050 | -69.63 % | 64634.7855 | +6241.12 ppm |
| ${}^{70}$Fe | 70 | 44 | 180.5571 | 581.5600 | -68.95 % | 65568.6818 | +6153.12 ppm |
| ${}^{71}$Fe | 71 | 45 | 186.2174 | 584.6850 | -68.15 % | 66502.5869 | +6027.39 ppm |
| ${}^{72}$Fe | 72 | 46 | 191.8693 | 590.0400 | -67.48 % | 67436.5005 | +5939.51 ppm |
| ${}^{73}$Fe | 73 | 47 | 197.5129 | 592.8330 | -66.68 % | 68370.4223 | +5815.99 ppm |
| ${}^{74}$Fe | 74 | 48 | 203.1486 | 597.6240 | -66.01 % | 69304.3520 | +5724.11 ppm |
| ${}^{75}$Fe | 75 | 49 | 208.7765 | 599.7000 | -65.19 % | 70238.2895 | +5596.94 ppm |
| ${}^{76}$Fe | 76 | 50 | 214.3969 | 603.6680 | -64.48 % | 71172.2346 | +5499.53 ppm |

### Cobalt (Z = 27)

_32 of 32 isotopes with a framework prediction; 32 of 32 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{47}$Co | 47 | 20 | 34.6317 | 347.6120 | -90.04 % | 44103.8201 | +7147.09 ppm |
| ${}^{48}$Co | 48 | 21 | 40.6636 | 364.5600 | -88.85 % | 45037.3536 | +7244.06 ppm |
| ${}^{49}$Co | 49 | 22 | 46.6738 | 384.1600 | -87.85 % | 45970.9089 | +7395.40 ppm |
| ${}^{50}$Co | 50 | 23 | 52.6632 | 400.0319 | -86.84 % | 46904.4849 | +7461.14 ppm |
| ${}^{51}$Co | 51 | 24 | 58.6328 | 417.8560 | -85.97 % | 47838.0807 | +7565.97 ppm |
| ${}^{52}$Co | 52 | 25 | 64.5833 | 432.9292 | -85.08 % | 48771.6956 | +7609.93 ppm |
| ${}^{53}$Co | 53 | 26 | 70.5156 | 449.3159 | -84.31 % | 49705.3288 | +7679.45 ppm |
| ${}^{54}$Co | 54 | 27 | 76.4304 | 462.7379 | -83.48 % | 50638.9794 | +7687.31 ppm |
| ${}^{55}$Co | 55 | 28 | 82.3285 | 476.8291 | -82.73 % | 51572.6468 | +7708.39 ppm |
| ${}^{56}$Co | 56 | 29 | 88.2104 | 486.9110 | -81.88 % | 52506.3303 | +7651.49 ppm |
| ${}^{57}$Co | 57 | 30 | 94.0767 | 498.2874 | -81.12 % | 53440.0293 | +7621.47 ppm |
| ${}^{58}$Co | 58 | 31 | 99.9282 | 506.8604 | -80.28 % | 54373.7433 | +7540.42 ppm |
| ${}^{59}$Co | 59 | 32 | 105.7654 | 517.3142 | -79.55 % | 55307.4715 | +7496.90 ppm |
| ${}^{60}$Co | 60 | 33 | 111.5887 | 524.8062 | -78.74 % | 56241.2137 | +7401.62 ppm |
| ${}^{61}$Co | 61 | 34 | 117.3987 | 534.1252 | -78.02 % | 57174.9691 | +7342.14 ppm |
| ${}^{62}$Co | 62 | 35 | 123.1958 | 540.7228 | -77.22 % | 58108.7374 | +7237.28 ppm |
| ${}^{63}$Co | 63 | 36 | 128.9806 | 549.2212 | -76.52 % | 59042.5180 | +7168.62 ppm |
| ${}^{64}$Co | 64 | 37 | 134.7534 | 555.2334 | -75.73 % | 59976.3107 | +7060.27 ppm |
| ${}^{65}$Co | 65 | 38 | 140.5146 | 562.6975 | -75.03 % | 60910.1148 | +6979.63 ppm |
| ${}^{66}$Co | 66 | 39 | 146.2647 | 567.9922 | -74.25 % | 61843.9302 | +6866.05 ppm |
| ${}^{67}$Co | 67 | 40 | 152.0040 | 574.9767 | -73.56 % | 62777.7563 | +6783.33 ppm |
| ${}^{68}$Co | 68 | 41 | 157.7328 | 579.3688 | -72.78 % | 63711.5929 | +6661.98 ppm |
| ${}^{69}$Co | 69 | 42 | 163.4516 | 586.1830 | -72.12 % | 64645.4395 | +6582.28 ppm |
| ${}^{70}$Co | 70 | 43 | 169.1606 | 590.3939 | -71.35 % | 65579.2960 | +6464.80 ppm |
| ${}^{71}$Co | 71 | 44 | 174.8601 | 596.3101 | -70.68 % | 66513.1619 | +6376.75 ppm |
| ${}^{72}$Co | 72 | 45 | 180.5504 | 600.3360 | -69.93 % | 67447.0370 | +6262.55 ppm |
| ${}^{73}$Co | 73 | 46 | 186.2318 | 606.0460 | -69.27 % | 68380.9211 | +6177.37 ppm |
| ${}^{74}$Co | 74 | 47 | 191.9046 | 609.6860 | -68.52 % | 69314.8137 | +6063.98 ppm |
| ${}^{75}$Co | 75 | 48 | 197.5690 | 614.7750 | -67.86 % | 70248.7147 | +5974.63 ppm |
| ${}^{76}$Co | 76 | 49 | 203.2252 | 617.9560 | -67.11 % | 71182.6239 | +5860.45 ppm |
| ${}^{77}$Co | 77 | 50 | 208.8736 | 622.3140 | -66.44 % | 72116.5409 | +5765.50 ppm |
| ${}^{78}$Co | 78 | 51 | 214.5143 | 623.7660 | -65.61 % | 73050.4656 | +5633.80 ppm |

### Nickel (Z = 28)

_35 of 35 isotopes with a framework prediction; 35 of 35 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{48}$Ni | 48 | 20 | 27.7866 | 347.3280 | -92.00 % | 45049.4484 | +7144.06 ppm |
| ${}^{49}$Ni | 49 | 21 | 33.8620 | 365.0500 | -90.72 % | 45982.9384 | +7254.87 ppm |
| ${}^{50}$Ni | 50 | 22 | 39.9149 | 385.1000 | -89.64 % | 46916.4508 | +7412.41 ppm |
| ${}^{51}$Ni | 51 | 23 | 45.9465 | 401.3700 | -88.55 % | 47849.9847 | +7483.71 ppm |
| ${}^{52}$Ni | 52 | 24 | 51.9575 | 420.3627 | -87.64 % | 48783.5391 | +7609.31 ppm |
| ${}^{53}$Ni | 53 | 25 | 57.9488 | 435.5050 | -86.69 % | 49717.1132 | +7652.21 ppm |
| ${}^{54}$Ni | 54 | 26 | 63.9213 | 453.2238 | -85.90 % | 50650.7062 | +7745.56 ppm |
| ${}^{55}$Ni | 55 | 27 | 69.8756 | 467.3527 | -85.05 % | 51584.3173 | +7765.23 ppm |
| ${}^{56}$Ni | 56 | 28 | 75.8126 | 483.9957 | -84.34 % | 52517.9457 | +7833.15 ppm |
| ${}^{57}$Ni | 57 | 29 | 81.7328 | 494.2434 | -83.46 % | 53451.5909 | +7777.49 ppm |
| ${}^{58}$Ni | 58 | 30 | 87.6369 | 506.4596 | -82.70 % | 54385.2522 | +7760.81 ppm |
| ${}^{59}$Ni | 59 | 31 | 93.5256 | 515.4589 | -81.86 % | 55318.9290 | +7685.92 ppm |
| ${}^{60}$Ni | 60 | 32 | 99.3993 | 526.8466 | -81.13 % | 56252.6207 | +7656.90 ppm |
| ${}^{61}$Ni | 61 | 33 | 105.2587 | 534.6667 | -80.31 % | 57186.3268 | +7565.75 ppm |
| ${}^{62}$Ni | 62 | 34 | 111.1042 | 545.2624 | -79.62 % | 58120.0467 | +7526.25 ppm |
| ${}^{63}$Ni | 63 | 35 | 116.9363 | 552.1002 | -78.82 % | 59053.7799 | +7423.65 ppm |
| ${}^{64}$Ni | 64 | 36 | 122.7556 | 561.7577 | -78.15 % | 59987.5261 | +7372.18 ppm |
| ${}^{65}$Ni | 65 | 37 | 128.5624 | 567.8558 | -77.36 % | 60921.2848 | +7263.22 ppm |
| ${}^{66}$Ni | 66 | 38 | 134.3571 | 576.8076 | -76.71 % | 61855.0555 | +7204.56 ppm |
| ${}^{67}$Ni | 67 | 39 | 140.1402 | 582.6153 | -75.95 % | 62788.8378 | +7097.05 ppm |
| ${}^{68}$Ni | 68 | 40 | 145.9120 | 590.4077 | -75.29 % | 63722.6314 | +7024.48 ppm |
| ${}^{69}$Ni | 69 | 41 | 151.6730 | 594.9939 | -74.51 % | 64656.4359 | +6903.91 ppm |
| ${}^{70}$Ni | 70 | 42 | 157.4233 | 602.3004 | -73.86 % | 65590.2509 | +6829.00 ppm |
| ${}^{71}$Ni | 71 | 43 | 163.1635 | 606.5641 | -73.10 % | 66524.0761 | +6710.00 ppm |
| ${}^{72}$Ni | 72 | 44 | 168.8938 | 613.4552 | -72.47 % | 67457.9113 | +6633.93 ppm |
| ${}^{73}$Ni | 73 | 45 | 174.6144 | 617.4087 | -71.72 % | 68391.7561 | +6516.58 ppm |
| ${}^{74}$Ni | 74 | 46 | 180.3258 | 624.0420 | -71.10 % | 69325.6101 | +6442.14 ppm |
| ${}^{75}$Ni | 75 | 47 | 186.0281 | 627.6750 | -70.36 % | 70259.4732 | +6325.83 ppm |
| ${}^{76}$Ni | 76 | 48 | 191.7217 | 633.6880 | -69.75 % | 71193.3451 | +6246.99 ppm |
| ${}^{77}$Ni | 77 | 49 | 197.4067 | 636.9440 | -69.01 % | 72127.2255 | +6131.17 ppm |
| ${}^{78}$Ni | 78 | 50 | 203.0835 | 642.5640 | -68.39 % | 73061.1141 | +6051.28 ppm |
| ${}^{79}$Ni | 79 | 51 | 208.7522 | 643.8500 | -67.58 % | 73995.0108 | +5915.41 ppm |
| ${}^{80}$Ni | 80 | 52 | 214.4132 | 647.0400 | -66.86 % | 74928.9153 | +5807.36 ppm |
| ${}^{81}$Ni | 81 | 53 | 220.0665 | 648.0000 | -66.04 % | 75862.8274 | +5672.37 ppm |
| ${}^{82}$Ni | 82 | 54 | 225.7125 | 650.6700 | -65.31 % | 76796.7468 | +5564.23 ppm |

### Copper (Z = 29)

_33 of 33 isotopes with a framework prediction; 33 of 33 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{52}$Cu | 52 | 23 | 38.9576 | 398.8920 | -90.23 % | 48795.7567 | +7431.34 ppm |
| ${}^{53}$Cu | 53 | 24 | 45.0101 | 418.2230 | -89.24 % | 49729.2696 | +7561.82 ppm |
| ${}^{54}$Cu | 54 | 25 | 51.0424 | 434.4300 | -88.25 % | 50662.8027 | +7624.61 ppm |
| ${}^{55}$Cu | 55 | 26 | 57.0552 | 452.8698 | -87.40 % | 51596.3553 | +7730.68 ppm |
| ${}^{56}$Cu | 56 | 27 | 63.0493 | 467.9355 | -86.53 % | 52529.9267 | +7767.60 ppm |
| ${}^{57}$Cu | 57 | 28 | 69.0253 | 484.6861 | -85.76 % | 53463.5161 | +7835.59 ppm |
| ${}^{58}$Cu | 58 | 29 | 74.9841 | 497.1162 | -84.92 % | 54397.1227 | +7820.89 ppm |
| ${}^{59}$Cu | 59 | 30 | 80.9262 | 509.8782 | -84.13 % | 55330.7460 | +7813.09 ppm |
| ${}^{60}$Cu | 60 | 31 | 86.8523 | 519.9363 | -83.30 % | 56264.3854 | +7757.02 ppm |
| ${}^{61}$Cu | 61 | 32 | 92.7629 | 531.6464 | -82.55 % | 57198.0402 | +7732.39 ppm |
| ${}^{62}$Cu | 62 | 33 | 98.6585 | 540.5212 | -81.75 % | 58131.7100 | +7659.29 ppm |
| ${}^{63}$Cu | 63 | 34 | 104.5399 | 551.3848 | -81.04 % | 59065.3941 | +7622.94 ppm |
| ${}^{64}$Cu | 64 | 35 | 110.4073 | 559.3007 | -80.26 % | 59999.0921 | +7538.07 ppm |
| ${}^{65}$Cu | 65 | 36 | 116.2613 | 569.2113 | -79.58 % | 60932.8035 | +7489.28 ppm |
| ${}^{66}$Cu | 66 | 37 | 122.1024 | 576.2772 | -78.81 % | 61866.5278 | +7395.50 ppm |
| ${}^{67}$Cu | 67 | 38 | 127.9309 | 585.4098 | -78.15 % | 62800.2647 | +7338.13 ppm |
| ${}^{68}$Cu | 68 | 39 | 133.7474 | 591.7286 | -77.40 % | 63734.0137 | +7237.84 ppm |
| ${}^{69}$Cu | 69 | 40 | 139.5521 | 599.9691 | -76.74 % | 64667.7744 | +7170.79 ppm |
| ${}^{70}$Cu | 70 | 41 | 145.3454 | 605.2806 | -75.99 % | 65601.5465 | +7060.55 ppm |
| ${}^{71}$Cu | 71 | 42 | 151.1278 | 613.0867 | -75.35 % | 66535.3295 | +6991.61 ppm |
| ${}^{72}$Cu | 72 | 43 | 156.8995 | 618.2298 | -74.62 % | 67469.1232 | +6884.73 ppm |
| ${}^{73}$Cu | 73 | 44 | 162.6609 | 625.5056 | -74.00 % | 68402.9273 | +6812.55 ppm |
| ${}^{74}$Cu | 74 | 45 | 168.4123 | 630.5957 | -73.29 % | 69336.7413 | +6710.52 ppm |
| ${}^{75}$Cu | 75 | 46 | 174.1539 | 637.1310 | -72.67 % | 70270.5651 | +6632.19 ppm |
| ${}^{76}$Cu | 76 | 47 | 179.8862 | 641.7137 | -71.97 % | 71204.3983 | +6528.29 ppm |
| ${}^{77}$Cu | 77 | 48 | 185.6093 | 647.6663 | -71.34 % | 72138.2406 | +6446.46 ppm |
| ${}^{78}$Cu | 78 | 49 | 191.3234 | 651.6642 | -70.64 % | 73072.0918 | +6339.76 ppm |
| ${}^{79}$Cu | 79 | 50 | 197.0290 | 657.3541 | -70.03 % | 74005.9517 | +6259.05 ppm |
| ${}^{80}$Cu | 80 | 51 | 202.7261 | 659.6800 | -69.27 % | 74939.8200 | +6135.25 ppm |
| ${}^{81}$Cu | 81 | 52 | 208.4151 | 662.9850 | -68.56 % | 75873.6964 | +6027.44 ppm |
| ${}^{82}$Cu | 82 | 53 | 214.0962 | 664.8560 | -67.80 % | 76807.5808 | +5903.78 ppm |
| ${}^{83}$Cu | 83 | 54 | 219.7695 | 667.6520 | -67.08 % | 77741.4729 | +5794.17 ppm |
| ${}^{84}$Cu | 84 | 55 | 225.4353 | 669.0600 | -66.31 % | 78675.3726 | +5670.17 ppm |

### Zinc (Z = 30)

_33 of 33 isotopes with a framework prediction; 33 of 33 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{54}$Zn | 54 | 24 | 37.7939 | 418.0680 | -90.96 % | 50675.2689 | +7561.17 ppm |
| ${}^{55}$Zn | 55 | 25 | 43.8672 | 434.7200 | -89.91 % | 51608.7610 | +7631.22 ppm |
| ${}^{56}$Zn | 56 | 26 | 49.9205 | 453.9360 | -89.00 % | 52542.2732 | +7748.49 ppm |
| ${}^{57}$Zn | 57 | 27 | 55.9544 | 469.1670 | -88.07 % | 53475.8047 | +7786.86 ppm |
| ${}^{58}$Zn | 58 | 28 | 61.9698 | 486.9649 | -87.27 % | 54409.3547 | +7872.57 ppm |
| ${}^{59}$Zn | 59 | 29 | 67.9673 | 499.9530 | -86.41 % | 55342.9227 | +7867.03 ppm |
| ${}^{60}$Zn | 60 | 30 | 73.9475 | 514.9831 | -85.64 % | 56276.5078 | +7898.85 ppm |
| ${}^{61}$Zn | 61 | 31 | 79.9112 | 525.2289 | -84.79 % | 57210.1095 | +7844.97 ppm |
| ${}^{62}$Zn | 62 | 32 | 85.8589 | 538.1194 | -84.04 % | 58143.7273 | +7839.30 ppm |
| ${}^{63}$Zn | 63 | 33 | 91.7912 | 547.2361 | -83.23 % | 59077.3605 | +7769.20 ppm |
| ${}^{64}$Zn | 64 | 34 | 97.7085 | 559.0980 | -82.52 % | 60011.0085 | +7747.99 ppm |
| ${}^{65}$Zn | 65 | 35 | 103.6115 | 567.0773 | -81.73 % | 60944.6710 | +7662.98 ppm |
| ${}^{66}$Zn | 66 | 36 | 109.5006 | 578.1358 | -81.06 % | 61878.3473 | +7631.30 ppm |
| ${}^{67}$Zn | 67 | 37 | 115.3762 | 585.1883 | -80.28 % | 62812.0371 | +7536.02 ppm |
| ${}^{68}$Zn | 68 | 38 | 121.2388 | 595.3864 | -79.64 % | 63745.7399 | +7493.85 ppm |
| ${}^{69}$Zn | 69 | 39 | 127.0889 | 601.8684 | -78.88 % | 64679.4552 | +7394.79 ppm |
| ${}^{70}$Zn | 70 | 40 | 132.9268 | 611.0866 | -78.25 % | 65613.1828 | +7341.06 ppm |
| ${}^{71}$Zn | 71 | 41 | 138.7529 | 616.9220 | -77.51 % | 66546.9221 | +7237.45 ppm |
| ${}^{72}$Zn | 72 | 42 | 144.5676 | 625.8100 | -76.90 % | 67480.6728 | +7182.79 ppm |
| ${}^{73}$Zn | 73 | 43 | 150.3712 | 631.3292 | -76.18 % | 68414.4347 | +7079.85 ppm |
| ${}^{74}$Zn | 74 | 44 | 156.1640 | 639.5638 | -75.58 % | 69348.2073 | +7019.55 ppm |
| ${}^{75}$Zn | 75 | 45 | 161.9464 | 644.4374 | -74.87 % | 70281.9903 | +6912.53 ppm |
| ${}^{76}$Zn | 76 | 46 | 167.7187 | 652.2528 | -74.29 % | 71215.7834 | +6850.36 ppm |
| ${}^{77}$Zn | 77 | 47 | 173.4812 | 656.8103 | -73.59 % | 72149.5863 | +6744.17 ppm |
| ${}^{78}$Zn | 78 | 48 | 179.2342 | 663.5756 | -72.99 % | 73083.3988 | +6671.46 ppm |
| ${}^{79}$Zn | 79 | 49 | 184.9778 | 667.5960 | -72.29 % | 74017.2205 | +6563.15 ppm |
| ${}^{80}$Zn | 80 | 50 | 190.7125 | 673.8837 | -71.70 % | 74951.0513 | +6488.32 ppm |
| ${}^{81}$Zn | 81 | 51 | 196.4384 | 676.5060 | -70.96 % | 75884.8908 | +6366.54 ppm |
| ${}^{82}$Zn | 82 | 52 | 202.1558 | 680.6916 | -70.30 % | 76818.7388 | +6268.47 ppm |
| ${}^{83}$Zn | 83 | 53 | 207.8649 | 682.7580 | -69.56 % | 77752.5951 | +6145.04 ppm |
| ${}^{84}$Zn | 84 | 54 | 213.5659 | 686.3640 | -68.88 % | 78686.4595 | +6044.79 ppm |
| ${}^{85}$Zn | 85 | 55 | 219.2591 | 687.6500 | -68.11 % | 79620.3318 | +5918.15 ppm |
| ${}^{86}$Zn | 86 | 56 | 224.9446 | 690.7520 | -67.43 % | 80554.2117 | +5815.83 ppm |

### Gallium (Z = 31)

_33 of 33 isotopes with a framework prediction; 33 of 33 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{56}$Ga | 56 | 25 | 36.4261 | 431.5920 | -91.56 % | 52554.9852 | +7575.85 ppm |
| ${}^{57}$Ga | 57 | 26 | 42.5200 | 451.2120 | -90.58 % | 53488.4567 | +7699.78 ppm |
| ${}^{58}$Ga | 58 | 27 | 48.5939 | 467.4220 | -89.60 % | 54421.9482 | +7755.66 ppm |
| ${}^{59}$Ga | 59 | 28 | 54.6487 | 485.6880 | -88.75 % | 55355.4588 | +7848.37 ppm |
| ${}^{60}$Ga | 60 | 29 | 60.6851 | 499.6200 | -87.85 % | 56288.9879 | +7859.12 ppm |
| ${}^{61}$Ga | 61 | 30 | 66.7037 | 515.2323 | -87.05 % | 57222.5347 | +7900.25 ppm |
| ${}^{62}$Ga | 62 | 31 | 72.7052 | 528.1560 | -86.23 % | 58156.0986 | +7893.35 ppm |
| ${}^{63}$Ga | 63 | 32 | 78.6902 | 540.7874 | -85.45 % | 59089.6790 | +7881.91 ppm |
| ${}^{64}$Ga | 64 | 33 | 84.6593 | 551.1444 | -84.64 % | 60023.2754 | +7832.62 ppm |
| ${}^{65}$Ga | 65 | 34 | 90.6129 | 563.0404 | -83.91 % | 60956.8872 | +7810.73 ppm |
| ${}^{66}$Ga | 66 | 35 | 96.5517 | 572.1780 | -83.13 % | 61890.5139 | +7744.49 ppm |
| ${}^{67}$Ga | 67 | 36 | 102.4760 | 583.4047 | -82.43 % | 62824.1549 | +7714.22 ppm |
| ${}^{68}$Ga | 68 | 37 | 108.3865 | 591.6829 | -81.68 % | 63757.8099 | +7638.10 ppm |
| ${}^{69}$Ga | 69 | 38 | 114.2835 | 601.9960 | -81.02 % | 64691.4783 | +7596.33 ppm |
| ${}^{70}$Ga | 70 | 39 | 120.1675 | 609.6497 | -80.29 % | 65625.1598 | +7514.82 ppm |
| ${}^{71}$Ga | 71 | 40 | 126.0388 | 618.9500 | -79.64 % | 66558.8538 | +7460.90 ppm |
| ${}^{72}$Ga | 72 | 41 | 131.8979 | 625.4704 | -78.91 % | 67492.5601 | +7366.87 ppm |
| ${}^{73}$Ga | 73 | 42 | 137.7452 | 634.6528 | -78.30 % | 68426.2783 | +7315.07 ppm |
| ${}^{74}$Ga | 74 | 43 | 143.5810 | 641.0744 | -77.60 % | 69360.0080 | +7224.45 ppm |
| ${}^{75}$Ga | 75 | 44 | 149.4056 | 649.5567 | -77.00 % | 70293.7488 | +7166.15 ppm |
| ${}^{76}$Ga | 76 | 45 | 155.2193 | 655.4641 | -76.32 % | 71227.5004 | +7072.88 ppm |
| ${}^{77}$Ga | 77 | 46 | 161.0226 | 663.2311 | -75.72 % | 72161.2626 | +7008.31 ppm |
| ${}^{78}$Ga | 78 | 47 | 166.8157 | 669.0141 | -75.07 % | 73095.0349 | +6918.02 ppm |
| ${}^{79}$Ga | 79 | 48 | 172.5988 | 675.9297 | -74.46 % | 74028.8172 | +6845.67 ppm |
| ${}^{80}$Ga | 80 | 49 | 178.3723 | 680.6764 | -73.79 % | 74962.6091 | +6745.94 ppm |
| ${}^{81}$Ga | 81 | 50 | 184.1364 | 687.1520 | -73.20 % | 75896.4104 | +6671.88 ppm |
| ${}^{82}$Ga | 82 | 51 | 189.8914 | 690.5261 | -72.50 % | 76830.2209 | +6558.86 ppm |
| ${}^{83}$Ga | 83 | 52 | 195.6376 | 694.9238 | -71.85 % | 77764.0402 | +6462.02 ppm |
| ${}^{84}$Ga | 84 | 53 | 201.3751 | 697.8321 | -71.14 % | 78697.8681 | +6348.45 ppm |
| ${}^{85}$Ga | 85 | 54 | 207.1042 | 701.5533 | -70.48 % | 79631.7044 | +6248.00 ppm |
| ${}^{86}$Ga | 86 | 55 | 212.8251 | 703.6520 | -69.75 % | 80565.5489 | +6129.48 ppm |
| ${}^{87}$Ga | 87 | 56 | 218.5380 | 706.7880 | -69.08 % | 81499.4014 | +6027.37 ppm |
| ${}^{88}$Ga | 88 | 57 | 224.2431 | 708.4000 | -68.35 % | 82433.2617 | +5908.19 ppm |

### Germanium (Z = 32)

_33 of 33 isotopes with a framework prediction; 33 of 33 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{58}$Ge | 58 | 26 | 34.8566 | 450.6600 | -92.27 % | 54434.9032 | +7697.74 ppm |
| ${}^{59}$Ge | 59 | 27 | 40.9707 | 467.5160 | -91.24 % | 55368.3546 | +7764.08 ppm |
| ${}^{60}$Ge | 60 | 28 | 47.0650 | 486.7800 | -90.33 % | 56301.8256 | +7871.34 ppm |
| ${}^{61}$Ge | 61 | 29 | 53.1405 | 501.1150 | -89.40 % | 57235.3156 | +7888.47 ppm |
| ${}^{62}$Ge | 62 | 30 | 59.1976 | 517.5140 | -88.56 % | 58168.8239 | +7941.87 ppm |
| ${}^{63}$Ge | 63 | 31 | 65.2371 | 530.3792 | -87.70 % | 59102.3499 | +7932.55 ppm |
| ${}^{64}$Ge | 64 | 32 | 71.2595 | 545.8448 | -86.95 % | 60035.8928 | +7968.02 ppm |
| ${}^{65}$Ge | 65 | 33 | 77.2655 | 556.0788 | -86.11 % | 60969.4522 | +7915.50 ppm |
| ${}^{66}$Ge | 66 | 34 | 83.2557 | 569.2789 | -85.38 % | 61903.0275 | +7913.50 ppm |
| ${}^{67}$Ge | 67 | 35 | 89.2304 | 578.4169 | -84.57 % | 62836.6182 | +7846.14 ppm |
| ${}^{68}$Ge | 68 | 36 | 95.1903 | 590.7933 | -83.89 % | 63770.2237 | +7832.58 ppm |
| ${}^{69}$Ge | 69 | 37 | 101.1358 | 598.9865 | -83.12 % | 64703.8436 | +7753.97 ppm |
| ${}^{70}$Ge | 70 | 38 | 107.0674 | 610.5192 | -82.46 % | 65637.4775 | +7729.48 ppm |
| ${}^{71}$Ge | 71 | 39 | 112.9856 | 617.9351 | -81.72 % | 66571.1247 | +7643.09 ppm |
| ${}^{72}$Ge | 72 | 40 | 118.8906 | 628.6857 | -81.09 % | 67504.7851 | +7609.46 ppm |
| ${}^{73}$Ge | 73 | 41 | 124.7830 | 635.4686 | -80.36 % | 68438.4581 | +7518.08 ppm |
| ${}^{74}$Ge | 74 | 42 | 130.6632 | 645.6649 | -79.76 % | 69372.1434 | +7479.29 ppm |
| ${}^{75}$Ge | 75 | 43 | 136.5314 | 652.1707 | -79.07 % | 70305.8406 | +7388.43 ppm |
| ${}^{76}$Ge | 76 | 44 | 142.3880 | 661.5980 | -78.48 % | 71239.5494 | +7341.74 ppm |
| ${}^{77}$Ge | 77 | 45 | 148.2334 | 667.6693 | -77.80 % | 72173.2694 | +7249.25 ppm |
| ${}^{78}$Ge | 78 | 46 | 154.0680 | 676.3898 | -77.22 % | 73107.0003 | +7196.04 ppm |
| ${}^{79}$Ge | 79 | 47 | 159.8919 | 682.1262 | -76.56 % | 74040.7418 | +7103.45 ppm |
| ${}^{80}$Ge | 80 | 48 | 165.7055 | 690.2057 | -75.99 % | 74974.4936 | +7045.01 ppm |
| ${}^{81}$Ge | 81 | 49 | 171.5092 | 695.0334 | -75.32 % | 75908.2554 | +6944.70 ppm |
| ${}^{82}$Ge | 82 | 50 | 177.3030 | 702.2280 | -74.75 % | 76842.0269 | +6878.22 ppm |
| ${}^{83}$Ge | 83 | 51 | 183.0875 | 705.8607 | -74.06 % | 77775.8079 | +6767.03 ppm |
| ${}^{84}$Ge | 84 | 52 | 188.8626 | 711.1040 | -73.44 % | 78709.5982 | +6679.36 ppm |
| ${}^{85}$Ge | 85 | 53 | 194.6289 | 714.1504 | -72.75 % | 79643.3974 | +6565.93 ppm |
| ${}^{86}$Ge | 86 | 54 | 200.3863 | 718.4982 | -72.11 % | 80577.2053 | +6471.62 ppm |
| ${}^{87}$Ge | 87 | 55 | 206.1353 | 720.7950 | -71.40 % | 81511.0218 | +6353.68 ppm |
| ${}^{88}$Ge | 88 | 56 | 211.8760 | 724.7680 | -70.77 % | 82444.8465 | +6259.89 ppm |
| ${}^{89}$Ge | 89 | 57 | 217.6085 | 726.3290 | -70.04 % | 83378.6794 | +6139.07 ppm |
| ${}^{90}$Ge | 90 | 58 | 223.3332 | 729.8100 | -69.40 % | 84312.5201 | +6043.97 ppm |

### Arsenic (Z = 33)

_33 of 33 isotopes with a framework prediction; 33 of 33 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{60}$As | 60 | 27 | 33.0873 | 464.1000 | -92.87 % | 56315.0210 | +7712.67 ppm |
| ${}^{61}$As | 61 | 28 | 39.2213 | 483.7300 | -91.89 % | 57248.4524 | +7825.37 ppm |
| ${}^{62}$As | 62 | 29 | 45.3359 | 499.0380 | -90.92 % | 58181.9033 | +7859.05 ppm |
| ${}^{63}$As | 63 | 30 | 51.4317 | 516.1590 | -90.04 % | 59115.3729 | +7923.95 ppm |
| ${}^{64}$As | 64 | 31 | 57.5093 | 530.3040 | -89.16 % | 60048.8607 | +7935.58 ppm |
| ${}^{65}$As | 65 | 32 | 63.5694 | 545.7553 | -88.35 % | 60982.3660 | +7970.00 ppm |
| ${}^{66}$As | 66 | 33 | 69.6126 | 558.9146 | -87.55 % | 61915.8883 | +7965.65 ppm |
| ${}^{67}$As | 67 | 34 | 75.6393 | 571.5481 | -86.77 % | 62849.4270 | +7953.19 ppm |
| ${}^{68}$As | 68 | 35 | 81.6503 | 581.9267 | -85.97 % | 63782.9814 | +7905.43 ppm |
| ${}^{69}$As | 69 | 36 | 87.6459 | 594.2157 | -85.25 % | 64716.5512 | +7889.28 ppm |
| ${}^{70}$As | 70 | 37 | 93.6267 | 603.5088 | -84.49 % | 65650.1358 | +7827.46 ppm |
| ${}^{71}$As | 71 | 38 | 99.5931 | 615.1394 | -83.81 % | 66583.7348 | +7803.25 ppm |
| ${}^{72}$As | 72 | 39 | 105.5456 | 623.5473 | -83.07 % | 67517.3478 | +7731.45 ppm |
| ${}^{73}$As | 73 | 40 | 111.4847 | 634.3415 | -82.43 % | 68450.9742 | +7697.22 ppm |
| ${}^{74}$As | 74 | 41 | 117.4106 | 642.3201 | -81.72 % | 69384.6137 | +7622.89 ppm |
| ${}^{75}$As | 75 | 42 | 123.3238 | 652.5656 | -81.10 % | 70318.2658 | +7583.46 ppm |
| ${}^{76}$As | 76 | 43 | 129.2248 | 659.8941 | -80.42 % | 71251.9303 | +7503.68 ppm |
| ${}^{77}$As | 77 | 44 | 135.1137 | 669.5904 | -79.82 % | 72185.6068 | +7459.44 ppm |
| ${}^{78}$As | 78 | 45 | 140.9910 | 676.5623 | -79.16 % | 73119.2949 | +7378.68 ppm |
| ${}^{79}$As | 79 | 46 | 146.8571 | 685.4528 | -78.58 % | 74052.9943 | +7326.40 ppm |
| ${}^{80}$As | 80 | 47 | 152.7122 | 692.1026 | -77.94 % | 74986.7046 | +7245.27 ppm |
| ${}^{81}$As | 81 | 48 | 158.5566 | 700.4926 | -77.36 % | 75920.4256 | +7189.54 ppm |
| ${}^{82}$As | 82 | 49 | 164.3906 | 706.1361 | -76.72 % | 76854.1570 | +7099.05 ppm |
| ${}^{83}$As | 83 | 50 | 170.2146 | 713.7713 | -76.15 % | 77787.8985 | +7036.85 ppm |
| ${}^{84}$As | 84 | 51 | 176.0287 | 718.0268 | -75.48 % | 78721.6498 | +6932.73 ppm |
| ${}^{85}$As | 85 | 52 | 181.8332 | 723.4337 | -74.87 % | 79655.4107 | +6845.85 ppm |
| ${}^{86}$As | 86 | 53 | 187.6285 | 727.2780 | -74.20 % | 80589.1809 | +6741.45 ppm |
| ${}^{87}$As | 87 | 54 | 193.4146 | 732.0051 | -73.58 % | 81522.9601 | +6650.56 ppm |
| ${}^{88}$As | 88 | 55 | 199.1920 | 734.8880 | -72.89 % | 82456.7482 | +6539.43 ppm |
| ${}^{89}$As | 89 | 56 | 204.9607 | 739.0560 | -72.27 % | 83390.5449 | +6446.09 ppm |
| ${}^{90}$As | 90 | 57 | 210.7210 | 741.6000 | -71.59 % | 84324.3501 | +6335.47 ppm |
| ${}^{91}$As | 91 | 58 | 216.4731 | 745.1990 | -70.95 % | 85258.1634 | +6239.86 ppm |
| ${}^{92}$As | 92 | 59 | 222.2172 | 747.1320 | -70.26 % | 86191.9847 | +6127.29 ppm |

### Selenium (Z = 34)

_33 of 33 isotopes with a framework prediction; 33 of 33 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{63}$Se | 63 | 29 | 37.2741 | 498.7710 | -92.53 % | 59128.7482 | +7865.87 ppm |
| ${}^{64}$Se | 64 | 30 | 43.4086 | 516.8000 | -91.60 % | 60062.1791 | +7944.72 ppm |
| ${}^{65}$Se | 65 | 31 | 49.5245 | 531.0500 | -90.67 % | 60995.6286 | +7957.34 ppm |
| ${}^{66}$Se | 66 | 32 | 55.6224 | 547.8000 | -89.85 % | 61929.0962 | +8010.58 ppm |
| ${}^{67}$Se | 67 | 33 | 61.7028 | 560.7588 | -89.00 % | 62862.5811 | +8002.38 ppm |
| ${}^{68}$Se | 68 | 34 | 67.7664 | 576.4393 | -88.24 % | 63796.0830 | +8037.51 ppm |
| ${}^{69}$Se | 69 | 35 | 73.8137 | 586.7559 | -87.42 % | 64729.6011 | +7987.69 ppm |
| ${}^{70}$Se | 70 | 36 | 79.8453 | 600.3224 | -86.70 % | 65663.1349 | +7989.81 ppm |
| ${}^{71}$Se | 71 | 37 | 85.8615 | 609.6103 | -85.92 % | 66596.6841 | +7926.84 ppm |
| ${}^{72}$Se | 72 | 38 | 91.8630 | 622.4033 | -85.24 % | 67530.2481 | +7918.55 ppm |
| ${}^{73}$Se | 73 | 39 | 97.8501 | 630.8338 | -84.49 % | 68463.8264 | +7845.98 ppm |
| ${}^{74}$Se | 74 | 40 | 103.8233 | 642.8909 | -83.85 % | 69397.4186 | +7828.65 ppm |
| ${}^{75}$Se | 75 | 41 | 109.7830 | 650.9185 | -83.13 % | 70331.0244 | +7753.79 ppm |
| ${}^{76}$Se | 76 | 42 | 115.7295 | 662.0723 | -82.52 % | 71264.6432 | +7725.63 ppm |
| ${}^{77}$Se | 77 | 43 | 121.6634 | 669.4912 | -81.83 % | 72198.2748 | +7645.85 ppm |
| ${}^{78}$Se | 78 | 44 | 127.5849 | 679.9890 | -81.24 % | 73131.9187 | +7611.03 ppm |
| ${}^{79}$Se | 79 | 45 | 133.4944 | 686.9518 | -80.57 % | 74065.5746 | +7528.80 ppm |
| ${}^{80}$Se | 80 | 46 | 139.3922 | 696.8651 | -80.00 % | 74999.2422 | +7488.72 ppm |
| ${}^{81}$Se | 81 | 47 | 145.2787 | 703.5660 | -79.35 % | 75932.9211 | +7406.84 ppm |
| ${}^{82}$Se | 82 | 48 | 151.1542 | 712.8422 | -78.80 % | 76866.6111 | +7361.10 ppm |
| ${}^{83}$Se | 83 | 49 | 157.0189 | 718.6601 | -78.15 % | 77800.3118 | +7271.51 ppm |
| ${}^{84}$Se | 84 | 50 | 162.8732 | 727.3387 | -77.61 % | 78734.0230 | +7221.05 ppm |
| ${}^{85}$Se | 85 | 51 | 168.7173 | 731.8759 | -76.95 % | 79667.7443 | +7119.17 ppm |
| ${}^{86}$Se | 86 | 52 | 174.5514 | 738.0367 | -76.35 % | 80601.4755 | +7040.23 ppm |
| ${}^{87}$Se | 87 | 53 | 180.3760 | 742.0310 | -75.69 % | 81535.2164 | +6936.28 ppm |
| ${}^{88}$Se | 88 | 54 | 186.1911 | 747.5604 | -75.09 % | 82468.9667 | +6853.70 ppm |
| ${}^{89}$Se | 89 | 55 | 191.9971 | 750.7399 | -74.43 % | 83402.7262 | +6744.53 ppm |
| ${}^{90}$Se | 90 | 56 | 197.7941 | 755.6190 | -73.82 % | 84336.4945 | +6658.32 ppm |
| ${}^{91}$Se | 91 | 57 | 203.5825 | 758.4703 | -73.16 % | 85270.2716 | +6550.03 ppm |
| ${}^{92}$Se | 92 | 58 | 209.3623 | 762.6800 | -72.55 % | 86204.0572 | +6460.23 ppm |
| ${}^{93}$Se | 93 | 59 | 215.1338 | 764.9250 | -71.88 % | 87137.8511 | +6349.14 ppm |
| ${}^{94}$Se | 94 | 60 | 220.8972 | 768.9200 | -71.27 % | 88071.6531 | +6261.29 ppm |
| ${}^{95}$Se | 95 | 61 | 226.6528 | 770.6400 | -70.59 % | 89005.4630 | +6149.38 ppm |

### Bromine (Z = 35)

_34 of 34 isotopes with a framework prediction; 34 of 34 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{65}$Br | 65 | 30 | 35.1308 | 513.7600 | -93.16 % | 61009.2400 | +7906.96 ppm |
| ${}^{66}$Br | 66 | 31 | 41.2851 | 528.9240 | -92.19 % | 61942.6511 | +7934.42 ppm |
| ${}^{67}$Br | 67 | 32 | 47.4208 | 545.9160 | -91.31 % | 62876.0808 | +7991.74 ppm |
| ${}^{68}$Br | 68 | 33 | 53.5387 | 560.2520 | -90.44 % | 63809.5283 | +8004.71 ppm |
| ${}^{69}$Br | 69 | 34 | 59.6393 | 575.7983 | -89.64 % | 64742.9932 | +8036.51 ppm |
| ${}^{70}$Br | 70 | 35 | 65.7231 | 589.0357 | -88.84 % | 65676.4748 | +8032.04 ppm |
| ${}^{71}$Br | 71 | 36 | 71.7908 | 602.1839 | -88.08 % | 66609.9726 | +8026.59 ppm |
| ${}^{72}$Br | 72 | 37 | 77.8426 | 612.8145 | -87.30 % | 67543.4861 | +7983.65 ppm |
| ${}^{73}$Br | 73 | 38 | 83.8793 | 625.4699 | -86.59 % | 68477.0148 | +7972.15 ppm |
| ${}^{74}$Br | 74 | 39 | 89.9012 | 635.1836 | -85.85 % | 69410.5584 | +7918.11 ppm |
| ${}^{75}$Br | 75 | 40 | 95.9088 | 647.0737 | -85.18 % | 70344.1163 | +7897.15 ppm |
| ${}^{76}$Br | 76 | 41 | 101.9024 | 656.3271 | -84.47 % | 71277.6880 | +7839.36 ppm |
| ${}^{77}$Br | 77 | 42 | 107.8825 | 667.3442 | -83.83 % | 72211.2733 | +7808.07 ppm |
| ${}^{78}$Br | 78 | 43 | 113.8496 | 675.6328 | -83.15 % | 73144.8717 | +7739.87 ppm |
| ${}^{79}$Br | 79 | 44 | 119.8038 | 686.3201 | -82.54 % | 74078.4829 | +7706.46 ppm |
| ${}^{80}$Br | 80 | 45 | 125.7457 | 694.2123 | -81.89 % | 75012.1064 | +7636.21 ppm |
| ${}^{81}$Br | 81 | 46 | 131.6756 | 704.3717 | -81.31 % | 75945.7420 | +7598.16 ppm |
| ${}^{82}$Br | 82 | 47 | 137.5937 | 711.9646 | -80.67 % | 76879.3893 | +7527.31 ppm |
| ${}^{83}$Br | 83 | 48 | 143.5004 | 721.5510 | -80.11 % | 77813.0479 | +7484.32 ppm |
| ${}^{84}$Br | 84 | 49 | 149.3961 | 728.3917 | -79.49 % | 78746.7177 | +7407.10 ppm |
| ${}^{85}$Br | 85 | 50 | 155.2809 | 737.2554 | -78.94 % | 79680.3983 | +7357.60 ppm |
| ${}^{86}$Br | 86 | 51 | 161.1553 | 742.3835 | -78.29 % | 80614.0894 | +7262.38 ppm |
| ${}^{87}$Br | 87 | 52 | 167.0194 | 748.7142 | -77.69 % | 81547.7907 | +7184.43 ppm |
| ${}^{88}$Br | 88 | 53 | 172.8735 | 753.6098 | -77.06 % | 82481.5020 | +7090.74 ppm |
| ${}^{89}$Br | 89 | 54 | 178.7179 | 759.2394 | -76.46 % | 83415.2231 | +7008.20 ppm |
| ${}^{90}$Br | 90 | 55 | 184.5528 | 763.0368 | -75.81 % | 84348.9536 | +6905.59 ppm |
| ${}^{91}$Br | 91 | 56 | 190.3784 | 768.2151 | -75.22 % | 85282.6934 | +6821.77 ppm |
| ${}^{92}$Br | 92 | 57 | 196.1950 | 771.4119 | -74.57 % | 86216.4422 | +6716.60 ppm |
| ${}^{93}$Br | 93 | 58 | 202.0028 | 776.1407 | -73.97 % | 87150.1998 | +6631.61 ppm |
| ${}^{94}$Br | 94 | 59 | 207.8021 | 778.9780 | -73.32 % | 88083.9660 | +6526.70 ppm |
| ${}^{95}$Br | 95 | 60 | 213.5929 | 783.2750 | -72.73 % | 89017.7406 | +6440.51 ppm |
| ${}^{96}$Br | 96 | 61 | 219.3755 | 785.6640 | -72.08 % | 89951.5233 | +6335.49 ppm |
| ${}^{97}$Br | 97 | 62 | 225.1502 | 789.5800 | -71.48 % | 90885.3141 | +6248.68 ppm |
| ${}^{98}$Br | 98 | 63 | 230.9170 | 791.6440 | -70.83 % | 91819.1127 | +6144.54 ppm |

### Krypton (Z = 36)

_35 of 35 isotopes with a framework prediction; 35 of 35 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{67}$Kr | 67 | 31 | 32.7934 | 528.1610 | -93.79 % | 62889.9259 | +7939.35 ppm |
| ${}^{68}$Kr | 68 | 32 | 38.9672 | 546.3120 | -92.87 % | 63823.3175 | +8012.90 ppm |
| ${}^{69}$Kr | 69 | 33 | 45.1226 | 560.9010 | -91.96 % | 64756.7275 | +8028.75 ppm |
| ${}^{70}$Kr | 70 | 34 | 51.2603 | 577.9200 | -91.13 % | 65690.1553 | +8082.26 ppm |
| ${}^{71}$Kr | 71 | 35 | 57.3808 | 591.2263 | -90.29 % | 66623.6002 | +8077.59 ppm |
| ${}^{72}$Kr | 72 | 36 | 63.4846 | 606.9110 | -89.54 % | 67557.0618 | +8109.20 ppm |
| ${}^{73}$Kr | 73 | 37 | 69.5723 | 617.5935 | -88.73 % | 68490.5395 | +8065.96 ppm |
| ${}^{74}$Kr | 74 | 38 | 75.6444 | 631.4449 | -88.02 % | 69424.0329 | +8070.50 ppm |
| ${}^{75}$Kr | 75 | 39 | 81.7012 | 641.5080 | -87.26 % | 70357.5415 | +8020.42 ppm |
| ${}^{76}$Kr | 76 | 40 | 87.7433 | 654.2694 | -86.59 % | 71291.0648 | +8010.33 ppm |
| ${}^{77}$Kr | 77 | 41 | 93.7711 | 663.4964 | -85.87 % | 72224.6024 | +7950.97 ppm |
| ${}^{78}$Kr | 78 | 42 | 99.7850 | 675.5766 | -85.23 % | 73158.1540 | +7932.95 ppm |
| ${}^{79}$Kr | 79 | 43 | 105.7854 | 683.9119 | -84.53 % | 74091.7190 | +7864.22 ppm |
| ${}^{80}$Kr | 80 | 44 | 111.7726 | 695.4344 | -83.93 % | 75025.2972 | +7840.54 ppm |
| ${}^{81}$Kr | 81 | 45 | 117.7471 | 703.3085 | -83.26 % | 75958.8881 | +7768.82 ppm |
| ${}^{82}$Kr | 82 | 46 | 123.7092 | 714.2754 | -82.68 % | 76892.4914 | +7739.87 ppm |
| ${}^{83}$Kr | 83 | 47 | 129.6592 | 721.7455 | -82.04 % | 77826.1068 | +7666.14 ppm |
| ${}^{84}$Kr | 84 | 48 | 135.5975 | 732.2656 | -81.48 % | 78759.7340 | +7633.64 ppm |
| ${}^{85}$Kr | 85 | 49 | 141.5243 | 739.3779 | -80.86 % | 79693.3726 | +7558.63 ppm |
| ${}^{86}$Kr | 86 | 50 | 147.4400 | 749.2345 | -80.32 % | 80627.0224 | +7520.07 ppm |
| ${}^{87}$Kr | 87 | 51 | 153.3448 | 754.7497 | -79.68 % | 81560.6830 | +7428.49 ppm |
| ${}^{88}$Kr | 88 | 52 | 159.2390 | 761.8028 | -79.10 % | 82494.3542 | +7358.06 ppm |
| ${}^{89}$Kr | 89 | 53 | 165.1229 | 766.7186 | -78.46 % | 83428.0356 | +7263.34 ppm |
| ${}^{90}$Kr | 90 | 54 | 170.9968 | 773.2134 | -77.88 % | 84361.7272 | +7189.84 ppm |
| ${}^{91}$Kr | 91 | 55 | 176.8609 | 777.2994 | -77.25 % | 85295.4285 | +7089.43 ppm |
| ${}^{92}$Kr | 92 | 56 | 182.7154 | 783.1661 | -76.67 % | 86229.1394 | +7012.27 ppm |
| ${}^{93}$Kr | 93 | 57 | 188.5606 | 786.6041 | -76.03 % | 87162.8597 | +6908.63 ppm |
| ${}^{94}$Kr | 94 | 58 | 194.3967 | 791.8872 | -75.45 % | 88096.5890 | +6828.54 ppm |
| ${}^{95}$Kr | 95 | 59 | 200.2239 | 794.7696 | -74.81 % | 89030.3272 | +6722.92 ppm |
| ${}^{96}$Kr | 96 | 60 | 206.0424 | 799.7637 | -74.24 % | 89964.0742 | +6643.39 ppm |
| ${}^{97}$Kr | 97 | 61 | 211.8524 | 802.1769 | -73.59 % | 90897.8296 | +6536.83 ppm |
| ${}^{98}$Kr | 98 | 62 | 217.6542 | 806.9320 | -73.03 % | 91831.5932 | +6458.53 ppm |
| ${}^{99}$Kr | 99 | 63 | 223.4478 | 809.3250 | -72.39 % | 92765.3650 | +6355.52 ppm |
| ${}^{100}$Kr | 100 | 64 | 229.2336 | 813.4000 | -71.82 % | 93699.1447 | +6274.01 ppm |
| ${}^{101}$Kr | 101 | 65 | 235.0116 | 815.5750 | -71.18 % | 94632.9321 | +6173.24 ppm |

### Rubidium (Z = 37)

_34 of 34 isotopes with a framework prediction; 34 of 34 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{71}$Rb | 71 | 34 | 42.6317 | 576.3780 | -92.60 % | 66637.5670 | +8074.81 ppm |
| ${}^{72}$Rb | 72 | 35 | 48.7889 | 590.5440 | -91.74 % | 67570.9751 | +8081.99 ppm |
| ${}^{73}$Rb | 73 | 36 | 54.9291 | 606.2710 | -90.94 % | 68504.4004 | +8113.58 ppm |
| ${}^{74}$Rb | 74 | 37 | 61.0528 | 620.2467 | -90.16 % | 69437.8422 | +8118.55 ppm |
| ${}^{75}$Rb | 75 | 38 | 67.1603 | 633.6207 | -89.40 % | 70371.3000 | +8114.92 ppm |
| ${}^{76}$Rb | 76 | 39 | 73.2523 | 644.9524 | -88.64 % | 71304.7735 | +8082.51 ppm |
| ${}^{77}$Rb | 77 | 40 | 79.3291 | 657.3751 | -87.93 % | 72238.2621 | +8066.49 ppm |
| ${}^{78}$Rb | 78 | 41 | 85.3912 | 667.5514 | -87.21 % | 73171.7654 | +8019.89 ppm |
| ${}^{79}$Rb | 79 | 42 | 91.4390 | 679.4901 | -86.54 % | 74105.2830 | +7998.83 ppm |
| ${}^{80}$Rb | 80 | 43 | 97.4730 | 688.9341 | -85.85 % | 75038.8145 | +7944.70 ppm |
| ${}^{81}$Rb | 81 | 44 | 103.4934 | 700.2866 | -85.22 % | 75972.3595 | +7917.60 ppm |
| ${}^{82}$Rb | 82 | 45 | 109.5007 | 709.0891 | -84.56 % | 76905.9176 | +7857.66 ppm |
| ${}^{83}$Rb | 83 | 46 | 115.4952 | 720.0432 | -83.96 % | 77839.4885 | +7827.40 ppm |
| ${}^{84}$Rb | 84 | 47 | 121.4773 | 728.8028 | -83.33 % | 78773.0718 | +7769.72 ppm |
| ${}^{85}$Rb | 85 | 48 | 127.4473 | 739.2825 | -82.76 % | 79706.6673 | +7735.47 ppm |
| ${}^{86}$Rb | 86 | 49 | 133.4055 | 747.9335 | -82.16 % | 80640.2745 | +7679.14 ppm |
| ${}^{87}$Rb | 87 | 50 | 139.3522 | 757.8556 | -81.61 % | 81573.8932 | +7640.06 ppm |
| ${}^{88}$Rb | 88 | 51 | 145.2877 | 763.9382 | -80.98 % | 82507.5231 | +7554.76 ppm |
| ${}^{89}$Rb | 89 | 52 | 151.2123 | 771.1129 | -80.39 % | 83441.1639 | +7484.81 ppm |
| ${}^{90}$Rb | 90 | 53 | 157.1263 | 776.8374 | -79.77 % | 84374.8153 | +7399.09 ppm |
| ${}^{91}$Rb | 91 | 54 | 163.0300 | 783.2882 | -79.19 % | 85308.4771 | +7324.03 ppm |
| ${}^{92}$Rb | 92 | 55 | 168.9235 | 788.3869 | -78.57 % | 86242.1491 | +7234.81 ppm |
| ${}^{93}$Rb | 93 | 56 | 174.8071 | 794.3056 | -77.99 % | 87175.8309 | +7157.18 ppm |
| ${}^{94}$Rb | 94 | 57 | 180.6811 | 798.3199 | -77.37 % | 88109.5223 | +7059.39 ppm |
| ${}^{95}$Rb | 95 | 58 | 186.5457 | 803.7187 | -76.79 % | 89043.2231 | +6979.54 ppm |
| ${}^{96}$Rb | 96 | 59 | 192.4011 | 807.2540 | -76.17 % | 89976.9331 | +6880.47 ppm |
| ${}^{97}$Rb | 97 | 60 | 198.2475 | 812.4902 | -75.60 % | 90910.6521 | +6802.52 ppm |
| ${}^{98}$Rb | 98 | 61 | 204.0852 | 816.4115 | -75.00 % | 91844.3799 | +6711.75 ppm |
| ${}^{99}$Rb | 99 | 62 | 209.9143 | 821.2348 | -74.44 % | 92778.1162 | +6632.77 ppm |
| ${}^{100}$Rb | 100 | 63 | 215.7351 | 824.4508 | -73.83 % | 93711.8608 | +6538.09 ppm |
| ${}^{101}$Rb | 101 | 64 | 221.5476 | 828.8237 | -73.27 % | 94645.6137 | +6457.76 ppm |
| ${}^{102}$Rb | 102 | 65 | 227.3522 | 831.5799 | -72.66 % | 95579.3746 | +6361.96 ppm |
| ${}^{103}$Rb | 103 | 66 | 233.1489 | 835.5360 | -72.10 % | 96513.1432 | +6280.95 ppm |
| ${}^{104}$Rb | 104 | 67 | 238.9380 | 837.9280 | -71.48 % | 97446.9196 | +6184.78 ppm |

### Strontium (Z = 38)

_35 of 35 isotopes with a framework prediction; 35 of 35 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{73}$Sr | 73 | 35 | 39.9497 | 591.4460 | -93.25 % | 68518.5974 | +8113.90 ppm |
| ${}^{74}$Sr | 74 | 36 | 46.1264 | 608.3540 | -92.42 % | 69451.9862 | +8161.59 ppm |
| ${}^{75}$Sr | 75 | 37 | 52.2861 | 622.2384 | -91.60 % | 70385.3919 | +8163.71 ppm |
| ${}^{76}$Sr | 76 | 38 | 58.4293 | 637.9386 | -90.84 % | 71318.8141 | +8192.19 ppm |
| ${}^{77}$Sr | 77 | 39 | 64.5565 | 649.5657 | -90.06 % | 72252.2523 | +8162.86 ppm |
| ${}^{78}$Sr | 78 | 40 | 70.6682 | 663.0076 | -89.34 % | 73185.7061 | +8159.70 ppm |
| ${}^{79}$Sr | 79 | 41 | 76.7648 | 673.3846 | -88.60 % | 74119.1749 | +8114.79 ppm |
| ${}^{80}$Sr | 80 | 42 | 82.8467 | 686.2877 | -87.93 % | 75052.6584 | +8105.41 ppm |
| ${}^{81}$Sr | 81 | 43 | 88.9144 | 695.5757 | -87.22 % | 75986.1562 | +8048.10 ppm |
| ${}^{82}$Sr | 82 | 44 | 94.9681 | 708.1290 | -86.59 % | 76919.6678 | +8035.51 ppm |
| ${}^{83}$Sr | 83 | 45 | 101.0084 | 716.9878 | -85.91 % | 77853.1930 | +7975.17 ppm |
| ${}^{84}$Sr | 84 | 46 | 107.0356 | 728.9111 | -85.32 % | 78786.7312 | +7955.96 ppm |
| ${}^{85}$Sr | 85 | 47 | 113.0500 | 737.4361 | -84.67 % | 79720.2823 | +7894.05 ppm |
| ${}^{86}$Sr | 86 | 48 | 119.0519 | 748.9273 | -84.10 % | 80653.8458 | +7871.09 ppm |
| ${}^{87}$Sr | 87 | 49 | 125.0417 | 757.3556 | -83.49 % | 81587.4214 | +7810.68 ppm |
| ${}^{88}$Sr | 88 | 50 | 131.0196 | 768.4684 | -82.95 % | 82521.0089 | +7784.83 ppm |
| ${}^{89}$Sr | 89 | 51 | 136.9861 | 774.8271 | -82.32 % | 83454.6078 | +7701.84 ppm |
| ${}^{90}$Sr | 90 | 52 | 142.9413 | 782.6404 | -81.74 % | 84388.2181 | +7638.34 ppm |
| ${}^{91}$Sr | 91 | 53 | 148.8855 | 788.4127 | -81.12 % | 85321.8392 | +7552.08 ppm |
| ${}^{92}$Sr | 92 | 54 | 154.8191 | 795.6994 | -80.54 % | 86255.4711 | +7485.65 ppm |
| ${}^{93}$Sr | 93 | 55 | 160.7423 | 800.9892 | -79.93 % | 87189.1133 | +7397.53 ppm |
| ${}^{94}$Sr | 94 | 56 | 166.6553 | 807.8204 | -79.37 % | 88122.7658 | +7329.15 ppm |
| ${}^{95}$Sr | 95 | 57 | 172.5583 | 812.1633 | -78.75 % | 89056.4282 | +7233.98 ppm |
| ${}^{96}$Sr | 96 | 58 | 178.4516 | 818.0356 | -78.19 % | 89990.1002 | +7158.15 ppm |
| ${}^{97}$Sr | 97 | 59 | 184.3355 | 821.7693 | -77.57 % | 90923.7818 | +7060.14 ppm |
| ${}^{98}$Sr | 98 | 60 | 190.2101 | 827.6824 | -77.02 % | 91857.4726 | +6988.30 ppm |
| ${}^{99}$Sr | 99 | 61 | 196.0757 | 831.8498 | -76.43 % | 92791.1724 | +6898.94 ppm |
| ${}^{100}$Sr | 100 | 62 | 201.9324 | 837.2201 | -75.88 % | 93724.8811 | +6824.48 ppm |
| ${}^{101}$Sr | 101 | 63 | 207.7805 | 840.7989 | -75.29 % | 94658.5985 | +6732.41 ppm |
| ${}^{102}$Sr | 102 | 64 | 213.6202 | 845.7046 | -74.74 % | 95592.3243 | +6656.31 ppm |
| ${}^{103}$Sr | 103 | 65 | 219.4515 | 848.9260 | -74.15 % | 96526.0583 | +6563.79 ppm |
| ${}^{104}$Sr | 104 | 66 | 225.2748 | 853.4240 | -73.60 % | 97459.8004 | +6487.27 ppm |
| ${}^{105}$Sr | 105 | 67 | 231.0902 | 855.9600 | -73.00 % | 98393.5505 | +6391.21 ppm |
| ${}^{106}$Sr | 106 | 68 | 236.8978 | 860.0840 | -72.46 % | 99327.3083 | +6314.16 ppm |
| ${}^{107}$Sr | 107 | 69 | 242.6979 | 862.0990 | -71.85 % | 100261.0737 | +6216.83 ppm |

### Yttrium (Z = 39)

_35 of 35 isotopes with a framework prediction; 35 of 35 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{75}$Y | 75 | 36 | 37.0785 | 606.6750 | -93.89 % | 70399.8172 | +8156.63 ppm |
| ${}^{76}$Y | 76 | 37 | 43.2744 | 621.1480 | -93.03 % | 71333.1867 | +8167.37 ppm |
| ${}^{77}$Y | 77 | 38 | 49.4534 | 637.4060 | -92.24 % | 72266.5731 | +8202.81 ppm |
| ${}^{78}$Y | 78 | 39 | 55.6160 | 651.2220 | -91.46 % | 73199.9760 | +8203.49 ppm |
| ${}^{79}$Y | 79 | 40 | 61.7627 | 664.9255 | -90.71 % | 74133.3947 | +8202.93 ppm |
| ${}^{80}$Y | 80 | 41 | 67.8939 | 676.3421 | -89.96 % | 75066.8289 | +8171.66 ppm |
| ${}^{81}$Y | 81 | 42 | 74.0100 | 688.9782 | -89.26 % | 76000.2782 | +8157.67 ppm |
| ${}^{82}$Y | 82 | 43 | 80.1116 | 699.4006 | -88.55 % | 76933.7421 | +8114.97 ppm |
| ${}^{83}$Y | 83 | 44 | 86.1989 | 711.6135 | -87.89 % | 77867.2202 | +8096.85 ppm |
| ${}^{84}$Y | 84 | 45 | 92.2723 | 721.3736 | -87.21 % | 78800.7122 | +8047.70 ppm |
| ${}^{85}$Y | 85 | 46 | 98.3323 | 733.3926 | -86.59 % | 79734.2176 | +8028.67 ppm |
| ${}^{86}$Y | 86 | 47 | 104.3791 | 742.9049 | -85.95 % | 80667.7362 | +7978.67 ppm |
| ${}^{87}$Y | 87 | 48 | 110.4131 | 754.7115 | -85.37 % | 81601.2676 | +7958.54 ppm |
| ${}^{88}$Y | 88 | 49 | 116.4347 | 764.0635 | -84.76 % | 82534.8115 | +7908.80 ppm |
| ${}^{89}$Y | 89 | 50 | 122.4441 | 775.5470 | -84.21 % | 83468.3675 | +7886.27 ppm |
| ${}^{90}$Y | 90 | 51 | 128.4417 | 782.4040 | -83.58 % | 84401.9353 | +7808.70 ppm |
| ${}^{91}$Y | 91 | 52 | 134.4277 | 790.3297 | -82.99 % | 85335.5147 | +7745.70 ppm |
| ${}^{92}$Y | 92 | 53 | 140.4024 | 796.8662 | -82.38 % | 86269.1054 | +7667.84 ppm |
| ${}^{93}$Y | 93 | 54 | 146.3662 | 804.3482 | -81.80 % | 87202.7071 | +7602.80 ppm |
| ${}^{94}$Y | 94 | 55 | 152.3192 | 810.5438 | -81.21 % | 88136.3195 | +7524.46 ppm |
| ${}^{95}$Y | 95 | 56 | 158.2618 | 817.4716 | -80.64 % | 89069.9424 | +7456.23 ppm |
| ${}^{96}$Y | 96 | 57 | 164.1941 | 822.6650 | -80.04 % | 90003.5755 | +7369.98 ppm |
| ${}^{97}$Y | 97 | 58 | 170.1164 | 828.5218 | -79.47 % | 90937.2186 | +7293.03 ppm |
| ${}^{98}$Y | 98 | 59 | 176.0289 | 832.7664 | -78.86 % | 91870.8715 | +7199.96 ppm |
| ${}^{99}$Y | 99 | 60 | 181.9320 | 839.1927 | -78.32 % | 92804.5339 | +7132.73 ppm |
| ${}^{100}$Y | 100 | 61 | 187.8256 | 843.9415 | -77.74 % | 93738.2056 | +7048.79 ppm |
| ${}^{101}$Y | 101 | 62 | 193.7102 | 849.7464 | -77.20 % | 94671.8864 | +6977.94 ppm |
| ${}^{102}$Y | 102 | 63 | 199.5859 | 853.9356 | -76.63 % | 95605.5762 | +6891.44 ppm |
| ${}^{103}$Y | 103 | 64 | 205.4528 | 859.2913 | -76.09 % | 96539.2747 | +6818.96 ppm |
| ${}^{104}$Y | 104 | 65 | 211.3113 | 862.9920 | -75.51 % | 97472.9817 | +6730.69 ppm |
| ${}^{105}$Y | 105 | 66 | 217.1613 | 867.5100 | -74.97 % | 98406.6970 | +6653.14 ppm |
| ${}^{106}$Y | 106 | 67 | 223.0033 | 870.7900 | -74.39 % | 99340.4205 | +6564.18 ppm |
| ${}^{107}$Y | 107 | 68 | 228.8372 | 875.0460 | -73.85 % | 100274.1520 | +6486.67 ppm |
| ${}^{108}$Y | 108 | 69 | 234.6633 | 877.9320 | -73.27 % | 101207.8913 | +6396.97 ppm |
| ${}^{109}$Y | 109 | 70 | 240.4817 | 881.7010 | -72.73 % | 102141.6383 | +6317.82 ppm |

### Zirconium (Z = 40)

_37 of 37 isotopes with a framework prediction; 37 of 37 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{77}$Zr | 77 | 37 | 34.0197 | 621.7750 | -94.53 % | 72281.2245 | +8198.50 ppm |
| ${}^{78}$Zr | 78 | 38 | 40.2345 | 639.1320 | -93.70 % | 73214.5751 | +8247.32 ppm |
| ${}^{79}$Zr | 79 | 39 | 46.4327 | 653.0930 | -92.89 % | 74147.9424 | +8249.50 ppm |
| ${}^{80}$Zr | 80 | 40 | 52.6145 | 669.2000 | -92.14 % | 75081.3260 | +8279.85 ppm |
| ${}^{81}$Zr | 81 | 41 | 58.7804 | 680.0073 | -91.36 % | 76014.7254 | +8239.80 ppm |
| ${}^{82}$Zr | 82 | 42 | 64.9310 | 694.1683 | -90.65 % | 76948.1403 | +8244.85 ppm |
| ${}^{83}$Zr | 83 | 43 | 71.0665 | 704.5372 | -89.91 % | 77881.5702 | +8200.48 ppm |
| ${}^{84}$Zr | 84 | 44 | 77.1875 | 718.1185 | -89.25 % | 78815.0146 | +8198.77 ppm |
| ${}^{85}$Zr | 85 | 45 | 83.2943 | 727.9433 | -88.56 % | 79748.4733 | +8149.41 ppm |
| ${}^{86}$Zr | 86 | 46 | 89.3872 | 740.8085 | -87.93 % | 80681.9458 | +8139.67 ppm |
| ${}^{87}$Zr | 87 | 47 | 95.4666 | 750.2579 | -87.28 % | 81615.4318 | +8087.78 ppm |
| ${}^{88}$Zr | 88 | 48 | 101.5330 | 762.6110 | -86.69 % | 82548.9309 | +8072.98 ppm |
| ${}^{89}$Zr | 89 | 49 | 107.5865 | 771.9314 | -86.06 % | 83482.4428 | +8021.74 ppm |
| ${}^{90}$Zr | 90 | 50 | 113.6275 | 783.8973 | -85.50 % | 84415.9672 | +8003.64 ppm |
| ${}^{91}$Zr | 91 | 51 | 119.6564 | 791.0917 | -84.87 % | 85349.5037 | +7929.28 ppm |
| ${}^{92}$Zr | 92 | 52 | 125.6734 | 799.7264 | -84.29 % | 86283.0521 | +7873.63 ppm |
| ${}^{93}$Zr | 93 | 53 | 131.6788 | 806.4607 | -83.67 % | 87216.6121 | +7797.18 ppm |
| ${}^{94}$Zr | 94 | 54 | 137.6729 | 814.6794 | -83.10 % | 88150.1834 | +7739.60 ppm |
| ${}^{95}$Zr | 95 | 55 | 143.6560 | 821.1413 | -82.51 % | 89083.7658 | +7663.32 ppm |
| ${}^{96}$Zr | 96 | 56 | 149.6283 | 828.9915 | -81.95 % | 90017.3589 | +7604.42 ppm |
| ${}^{97}$Zr | 97 | 57 | 155.5901 | 834.5607 | -81.36 % | 90950.9625 | +7521.39 ppm |
| ${}^{98}$Zr | 98 | 58 | 161.5416 | 840.9770 | -80.79 % | 91884.5764 | +7449.54 ppm |
| ${}^{99}$Zr | 99 | 59 | 167.4831 | 845.3833 | -80.19 % | 92818.2004 | +7357.27 ppm |
| ${}^{100}$Zr | 100 | 60 | 173.4147 | 852.2107 | -79.65 % | 93751.8342 | +7293.16 ppm |
| ${}^{101}$Zr | 101 | 61 | 179.3368 | 857.0702 | -79.08 % | 94685.4776 | +7209.34 ppm |
| ${}^{102}$Zr | 102 | 62 | 185.2494 | 863.5620 | -78.55 % | 95619.1303 | +7144.59 ppm |
| ${}^{103}$Zr | 103 | 63 | 191.1529 | 867.8609 | -77.97 % | 96552.7923 | +7058.16 ppm |
| ${}^{104}$Zr | 104 | 64 | 197.0474 | 873.8409 | -77.45 % | 97486.4632 | +6990.98 ppm |
| ${}^{105}$Zr | 105 | 65 | 202.9331 | 877.6528 | -76.88 % | 98420.1429 | +6902.83 ppm |
| ${}^{106}$Zr | 106 | 66 | 208.8102 | 882.9800 | -76.35 % | 99353.8313 | +6832.27 ppm |
| ${}^{107}$Zr | 107 | 67 | 214.6789 | 886.3880 | -75.78 % | 100287.5280 | +6742.69 ppm |
| ${}^{108}$Zr | 108 | 68 | 220.5393 | 891.3240 | -75.26 % | 101221.2330 | +6671.48 ppm |
| ${}^{109}$Zr | 109 | 69 | 226.3917 | 894.2360 | -74.68 % | 102154.9460 | +6580.33 ppm |
| ${}^{110}$Zr | 110 | 70 | 232.2361 | 898.8100 | -74.16 % | 103088.6670 | +6507.73 ppm |
| ${}^{111}$Zr | 111 | 71 | 238.0729 | 901.0980 | -73.58 % | 104022.3957 | +6414.81 ppm |
| ${}^{112}$Zr | 112 | 72 | 243.9020 | 905.0720 | -73.05 % | 104956.1320 | +6339.83 ppm |
| ${}^{113}$Zr | 113 | 73 | 249.7237 | 907.0510 | -72.47 % | 105889.8757 | +6246.95 ppm |

### Niobium (Z = 41)

_38 of 38 isotopes with a framework prediction; 38 of 38 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{79}$Nb | 79 | 38 | 30.7748 | 637.2140 | -95.17 % | 74162.8179 | +8244.48 ppm |
| ${}^{80}$Nb | 80 | 39 | 37.0085 | 652.0800 | -94.32 % | 75096.1496 | +8257.69 ppm |
| ${}^{81}$Nb | 81 | 40 | 43.2255 | 668.0880 | -93.53 % | 76029.4980 | +8286.44 ppm |
| ${}^{82}$Nb | 82 | 41 | 49.4264 | 681.5840 | -92.75 % | 76962.8626 | +8281.80 ppm |
| ${}^{83}$Nb | 83 | 42 | 55.6114 | 695.4561 | -92.00 % | 77896.2430 | +8282.10 ppm |
| ${}^{84}$Nb | 84 | 43 | 61.7811 | 707.1083 | -91.26 % | 78829.6387 | +8253.93 ppm |
| ${}^{85}$Nb | 85 | 44 | 67.9359 | 720.2655 | -90.57 % | 79763.0493 | +8245.79 ppm |
| ${}^{86}$Nb | 86 | 45 | 74.0761 | 731.1912 | -89.87 % | 80696.4745 | +8209.91 ppm |
| ${}^{87}$Nb | 87 | 46 | 80.2022 | 744.0029 | -89.22 % | 81629.9139 | +8198.51 ppm |
| ${}^{88}$Nb | 88 | 47 | 86.3144 | 754.3713 | -88.56 % | 82563.3671 | +8157.46 ppm |
| ${}^{89}$Nb | 89 | 48 | 92.4132 | 766.8968 | -87.95 % | 83496.8338 | +8143.75 ppm |
| ${}^{90}$Nb | 90 | 49 | 98.4988 | 777.0039 | -87.32 % | 84430.3135 | +8101.39 ppm |
| ${}^{91}$Nb | 91 | 50 | 104.5716 | 789.0517 | -86.75 % | 85363.8061 | +8083.21 ppm |
| ${}^{92}$Nb | 92 | 51 | 110.6320 | 796.9383 | -86.12 % | 86297.3112 | +8016.57 ppm |
| ${}^{93}$Nb | 93 | 52 | 116.6802 | 805.7692 | -85.52 % | 87230.8284 | +7962.51 ppm |
| ${}^{94}$Nb | 94 | 53 | 122.7164 | 812.9967 | -84.91 % | 88164.3576 | +7891.26 ppm |
| ${}^{95}$Nb | 95 | 54 | 128.7411 | 821.4853 | -84.33 % | 89097.8983 | +7836.02 ppm |
| ${}^{96}$Nb | 96 | 55 | 134.7545 | 828.3731 | -83.73 % | 90031.4504 | +7764.00 ppm |
| ${}^{97}$Nb | 97 | 56 | 140.7567 | 836.4444 | -83.17 % | 90965.0136 | +7706.81 ppm |
| ${}^{98}$Nb | 98 | 57 | 146.7482 | 842.4376 | -82.58 % | 91898.5875 | +7627.94 ppm |
| ${}^{99}$Nb | 99 | 58 | 152.7291 | 849.3196 | -82.02 % | 92832.1721 | +7560.50 ppm |
| ${}^{100}$Nb | 100 | 59 | 158.6996 | 854.8468 | -81.44 % | 93765.7669 | +7479.86 ppm |
| ${}^{101}$Nb | 101 | 60 | 164.6601 | 862.0184 | -80.90 % | 94699.3719 | +7418.55 ppm |
| ${}^{102}$Nb | 102 | 61 | 170.6107 | 867.4965 | -80.33 % | 95632.9867 | +7340.58 ppm |
| ${}^{103}$Nb | 103 | 62 | 176.5516 | 874.2982 | -79.81 % | 96566.6112 | +7278.14 ppm |
| ${}^{104}$Nb | 104 | 63 | 182.4831 | 879.1519 | -79.24 % | 97500.2451 | +7196.73 ppm |
| ${}^{105}$Nb | 105 | 64 | 188.4054 | 885.3277 | -78.72 % | 98433.8883 | +7130.60 ppm |
| ${}^{106}$Nb | 106 | 65 | 194.3186 | 889.6862 | -78.16 % | 99367.5405 | +7047.26 ppm |
| ${}^{107}$Nb | 107 | 66 | 200.2229 | 895.2786 | -77.64 % | 100301.2016 | +6978.05 ppm |
| ${}^{108}$Nb | 108 | 67 | 206.1186 | 899.1713 | -77.08 % | 101234.8714 | +6893.19 ppm |
| ${}^{109}$Nb | 109 | 68 | 212.0058 | 904.3872 | -76.56 % | 102168.5496 | +6823.10 ppm |
| ${}^{110}$Nb | 110 | 69 | 217.8846 | 908.0787 | -76.01 % | 103102.2362 | +6739.39 ppm |
| ${}^{111}$Nb | 111 | 70 | 223.7554 | 912.7530 | -75.49 % | 104035.9309 | +6667.31 ppm |
| ${}^{112}$Nb | 112 | 71 | 229.6181 | 915.9360 | -74.93 % | 104969.6335 | +6581.73 ppm |
| ${}^{113}$Nb | 113 | 72 | 235.4730 | 920.1590 | -74.41 % | 105903.3440 | +6507.59 ppm |
| ${}^{114}$Nb | 114 | 73 | 241.3203 | 923.0580 | -73.86 % | 106837.0622 | +6421.67 ppm |
| ${}^{115}$Nb | 115 | 74 | 247.1601 | 927.0150 | -73.34 % | 107770.7878 | +6348.30 ppm |
| ${}^{116}$Nb | 116 | 75 | 252.9925 | 929.3920 | -72.78 % | 108704.5209 | +6261.66 ppm |

### Molybdenum (Z = 42)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{81}$Mo | 81 | 39 | 27.3453 | 652.3740 | -95.81 % | 76044.5959 | +8287.42 ppm |
| ${}^{82}$Mo | 82 | 40 | 33.5977 | 669.3660 | -94.98 % | 76977.9089 | +8327.80 ppm |
| ${}^{83}$Mo | 83 | 41 | 39.8335 | 683.4220 | -94.17 % | 77911.2385 | +8329.07 ppm |
| ${}^{84}$Mo | 84 | 42 | 46.0532 | 699.3000 | -93.41 % | 78844.5843 | +8354.50 ppm |
| ${}^{85}$Mo | 85 | 43 | 52.2572 | 710.7132 | -92.65 % | 79777.9457 | +8322.31 ppm |
| ${}^{86}$Mo | 86 | 44 | 58.4459 | 725.3857 | -91.94 % | 80711.3224 | +8332.13 ppm |
| ${}^{87}$Mo | 87 | 45 | 64.6197 | 736.2309 | -91.22 % | 81644.7140 | +8294.26 ppm |
| ${}^{88}$Mo | 88 | 46 | 70.7790 | 750.1040 | -90.56 % | 82578.1202 | +8294.70 ppm |
| ${}^{89}$Mo | 89 | 47 | 76.9241 | 760.5037 | -89.89 % | 83511.5404 | +8253.01 ppm |
| ${}^{90}$Mo | 90 | 48 | 83.0555 | 773.7326 | -89.27 % | 84444.9745 | +8246.47 ppm |
| ${}^{91}$Mo | 91 | 49 | 89.1734 | 783.8402 | -88.62 % | 85378.4220 | +8203.08 ppm |
| ${}^{92}$Mo | 92 | 50 | 95.2782 | 796.5113 | -88.04 % | 86311.8826 | +8190.96 ppm |
| ${}^{93}$Mo | 93 | 51 | 101.3702 | 804.5811 | -87.40 % | 87245.3560 | +8125.65 ppm |
| ${}^{94}$Mo | 94 | 52 | 107.4497 | 814.2594 | -86.80 % | 88178.8420 | +8080.41 ppm |
| ${}^{95}$Mo | 95 | 53 | 113.5171 | 821.6285 | -86.18 % | 89112.3401 | +8009.93 ppm |
| ${}^{96}$Mo | 96 | 54 | 119.5725 | 830.7828 | -85.61 % | 90045.8501 | +7961.20 ppm |
| ${}^{97}$Mo | 97 | 55 | 125.6162 | 837.6040 | -85.00 % | 90979.3717 | +7887.55 ppm |
| ${}^{98}$Mo | 98 | 56 | 131.6487 | 846.2466 | -84.44 % | 91912.9047 | +7835.66 ppm |
| ${}^{99}$Mo | 99 | 57 | 137.6700 | 852.1720 | -83.84 % | 92846.4488 | +7755.21 ppm |
| ${}^{100}$Mo | 100 | 58 | 143.6804 | 860.4663 | -83.30 % | 93780.0038 | +7702.15 ppm |
| ${}^{101}$Mo | 101 | 59 | 149.6803 | 865.8645 | -82.71 % | 94713.5694 | +7619.20 ppm |
| ${}^{102}$Mo | 102 | 60 | 155.6698 | 873.9767 | -82.19 % | 95647.1453 | +7566.80 ppm |
| ${}^{103}$Mo | 103 | 61 | 161.6491 | 879.4415 | -81.62 % | 96580.7314 | +7487.70 ppm |
| ${}^{104}$Mo | 104 | 62 | 167.6185 | 886.9023 | -81.10 % | 97514.3274 | +7431.00 ppm |
| ${}^{105}$Mo | 105 | 63 | 173.5782 | 891.9606 | -80.54 % | 98447.9331 | +7350.72 ppm |
| ${}^{106}$Mo | 106 | 64 | 179.5284 | 898.8291 | -80.03 % | 99381.5483 | +7290.54 ppm |
| ${}^{107}$Mo | 107 | 65 | 185.4693 | 903.3174 | -79.47 % | 100315.1729 | +7207.51 ppm |
| ${}^{108}$Mo | 108 | 66 | 191.4011 | 909.5931 | -78.96 % | 101248.8065 | +7144.02 ppm |
| ${}^{109}$Mo | 109 | 67 | 197.3240 | 913.5744 | -78.40 % | 102182.4490 | +7059.01 ppm |
| ${}^{110}$Mo | 110 | 68 | 203.2381 | 919.5222 | -77.90 % | 103116.1003 | +6994.98 ppm |
| ${}^{111}$Mo | 111 | 69 | 209.1437 | 922.9975 | -77.34 % | 104049.7602 | +6908.10 ppm |
| ${}^{112}$Mo | 112 | 70 | 215.0409 | 928.5920 | -76.84 % | 104983.4284 | +6843.48 ppm |
| ${}^{113}$Mo | 113 | 71 | 220.9299 | 931.7980 | -76.29 % | 105917.1048 | +6757.41 ppm |
| ${}^{114}$Mo | 114 | 72 | 226.8109 | 936.9660 | -75.79 % | 106850.7893 | +6690.57 ppm |
| ${}^{115}$Mo | 115 | 73 | 232.6839 | 939.8950 | -75.24 % | 107784.4816 | +6604.66 ppm |
| ${}^{116}$Mo | 116 | 74 | 238.5492 | 944.5880 | -74.75 % | 108718.1818 | +6537.01 ppm |
| ${}^{117}$Mo | 117 | 75 | 244.4070 | 947.2320 | -74.20 % | 109651.8895 | +6450.43 ppm |
| ${}^{118}$Mo | 118 | 76 | 250.2573 | 951.9060 | -73.71 % | 110585.6046 | +6385.56 ppm |
| ${}^{119}$Mo | 119 | 77 | 256.1002 | 954.2610 | -73.16 % | 111519.3270 | +6299.42 ppm |

### Technetium (Z = 43)

_40 of 40 isotopes with a framework prediction; 40 of 40 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{83}$Tc | 83 | 40 | 23.7329 | 667.5690 | -96.44 % | 77926.5569 | +8331.31 ppm |
| ${}^{84}$Tc | 84 | 41 | 30.0037 | 682.0800 | -95.60 % | 78859.8514 | +8337.37 ppm |
| ${}^{85}$Tc | 85 | 42 | 36.2582 | 698.2750 | -94.81 % | 79793.1624 | +8366.03 ppm |
| ${}^{86}$Tc | 86 | 43 | 42.4965 | 712.0800 | -94.03 % | 80726.4894 | +8363.63 ppm |
| ${}^{87}$Tc | 87 | 44 | 48.7193 | 726.2538 | -93.29 % | 81659.8321 | +8366.46 ppm |
| ${}^{88}$Tc | 88 | 45 | 54.9268 | 738.3054 | -92.56 % | 82593.1900 | +8343.07 ppm |
| ${}^{89}$Tc | 89 | 46 | 61.1195 | 752.1012 | -91.87 % | 83526.5628 | +8341.61 ppm |
| ${}^{90}$Tc | 90 | 47 | 67.2977 | 763.5024 | -91.19 % | 84459.9500 | +8311.54 ppm |
| ${}^{91}$Tc | 91 | 48 | 73.4618 | 776.8357 | -90.54 % | 85393.3513 | +8305.29 ppm |
| ${}^{92}$Tc | 92 | 49 | 79.6121 | 787.8460 | -89.89 % | 86326.7664 | +8271.98 ppm |
| ${}^{93}$Tc | 93 | 50 | 85.7490 | 800.5978 | -89.29 % | 87260.1949 | +8259.82 ppm |
| ${}^{94}$Tc | 94 | 51 | 91.8728 | 809.2213 | -88.65 % | 88193.6366 | +8200.50 ppm |
| ${}^{95}$Tc | 95 | 52 | 97.9838 | 819.1557 | -88.04 % | 89127.0910 | +8157.51 ppm |
| ${}^{96}$Tc | 96 | 53 | 104.0823 | 827.0273 | -87.41 % | 90060.5579 | +8092.29 ppm |
| ${}^{97}$Tc | 97 | 54 | 110.1686 | 836.5014 | -86.83 % | 90994.0370 | +8046.44 ppm |
| ${}^{98}$Tc | 98 | 55 | 116.2430 | 843.7805 | -86.22 % | 91927.5281 | +7977.39 ppm |
| ${}^{99}$Tc | 99 | 56 | 122.3057 | 852.7474 | -85.66 % | 92861.0307 | +7928.34 ppm |
| ${}^{100}$Tc | 100 | 57 | 128.3571 | 859.5118 | -85.07 % | 93794.5448 | +7856.53 ppm |
| ${}^{101}$Tc | 101 | 58 | 134.3973 | 867.9068 | -84.51 % | 94728.0700 | +7803.75 ppm |
| ${}^{102}$Tc | 102 | 59 | 140.4266 | 874.2064 | -83.94 % | 95661.6061 | +7729.88 ppm |
| ${}^{103}$Tc | 103 | 60 | 146.4453 | 882.3088 | -83.40 % | 96595.1529 | +7676.50 ppm |
| ${}^{104}$Tc | 104 | 61 | 152.4536 | 888.2751 | -82.84 % | 97528.7100 | +7602.03 ppm |
| ${}^{105}$Tc | 105 | 62 | 158.4517 | 896.1338 | -82.32 % | 98462.2773 | +7548.59 ppm |
| ${}^{106}$Tc | 106 | 63 | 164.4398 | 901.6950 | -81.76 % | 99395.8547 | +7472.80 ppm |
| ${}^{107}$Tc | 107 | 64 | 170.4181 | 908.7401 | -81.25 % | 100329.4417 | +7413.54 ppm |
| ${}^{108}$Tc | 108 | 65 | 176.3869 | 913.9843 | -80.70 % | 101263.0383 | +7337.43 ppm |
| ${}^{109}$Tc | 109 | 66 | 182.3464 | 920.4156 | -80.19 % | 102196.6443 | +7274.59 ppm |
| ${}^{110}$Tc | 110 | 67 | 188.2967 | 925.2386 | -79.65 % | 103130.2595 | +7197.18 ppm |
| ${}^{111}$Tc | 111 | 68 | 194.2380 | 931.3001 | -79.14 % | 104063.8836 | +7133.31 ppm |
| ${}^{112}$Tc | 112 | 69 | 200.1705 | 935.6056 | -78.61 % | 104997.5165 | +7053.72 ppm |
| ${}^{113}$Tc | 113 | 70 | 206.0944 | 941.2296 | -78.10 % | 105931.1580 | +6988.25 ppm |
| ${}^{114}$Tc | 114 | 71 | 212.0098 | 945.0896 | -77.57 % | 106864.8080 | +6907.27 ppm |
| ${}^{115}$Tc | 115 | 72 | 217.9170 | 950.3600 | -77.07 % | 107798.4663 | +6841.02 ppm |
| ${}^{116}$Tc | 116 | 73 | 223.8160 | 953.8680 | -76.54 % | 108732.1327 | +6759.41 ppm |
| ${}^{117}$Tc | 117 | 74 | 229.7071 | 958.8150 | -76.04 % | 109665.8070 | +6693.21 ppm |
| ${}^{118}$Tc | 118 | 75 | 235.5904 | 962.0540 | -75.51 % | 110599.4891 | +6611.95 ppm |
| ${}^{119}$Tc | 119 | 76 | 241.4660 | 966.9940 | -75.03 % | 111533.1789 | +6547.84 ppm |
| ${}^{120}$Tc | 120 | 77 | 247.3341 | 969.9600 | -74.50 % | 112466.8763 | +6466.40 ppm |
| ${}^{121}$Tc | 121 | 78 | 253.1948 | 974.5340 | -74.02 % | 113400.5809 | +6401.66 ppm |
| ${}^{122}$Tc | 122 | 79 | 259.0483 | 977.3420 | -73.49 % | 114334.2929 | +6322.33 ppm |

### Ruthenium (Z = 44)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{85}$Ru | 85 | 41 | 19.9388 | 682.2950 | -97.08 % | 79808.6994 | +8368.43 ppm |
| ${}^{86}$Ru | 86 | 42 | 26.2280 | 699.4380 | -96.25 % | 80741.9756 | +8408.44 ppm |
| ${}^{87}$Ru | 87 | 43 | 32.5009 | 713.4870 | -95.44 % | 81675.2682 | +8408.14 ppm |
| ${}^{88}$Ru | 88 | 44 | 38.7578 | 730.2240 | -94.69 % | 82608.5767 | +8440.67 ppm |
| ${}^{89}$Ru | 89 | 45 | 44.9991 | 742.2935 | -93.94 % | 83541.9008 | +8416.90 ppm |
| ${}^{90}$Ru | 90 | 46 | 51.2253 | 756.8792 | -93.23 % | 84475.2401 | +8423.76 ppm |
| ${}^{91}$Ru | 91 | 47 | 57.4367 | 768.3065 | -92.52 % | 85408.5941 | +8393.03 ppm |
| ${}^{92}$Ru | 92 | 48 | 63.6336 | 782.4392 | -91.87 % | 86341.9626 | +8395.00 ppm |
| ${}^{93}$Ru | 93 | 49 | 69.8165 | 793.4260 | -91.20 % | 87275.3451 | +8360.44 ppm |
| ${}^{94}$Ru | 94 | 50 | 75.9856 | 806.8642 | -90.58 % | 88208.7414 | +8355.02 ppm |
| ${}^{95}$Ru | 95 | 51 | 82.1414 | 815.8097 | -89.93 % | 89142.1511 | +8298.63 ppm |
| ${}^{96}$Ru | 96 | 52 | 88.2840 | 826.5036 | -89.32 % | 90075.5739 | +8263.29 ppm |
| ${}^{97}$Ru | 97 | 53 | 94.4139 | 834.6152 | -88.69 % | 91009.0094 | +8199.97 ppm |
| ${}^{98}$Ru | 98 | 54 | 100.5312 | 844.7908 | -88.10 % | 91942.4575 | +8160.91 ppm |
| ${}^{99}$Ru | 99 | 55 | 106.6364 | 852.2626 | -87.49 % | 92875.9178 | +8093.18 ppm |
| ${}^{100}$Ru | 100 | 56 | 112.7296 | 861.9359 | -86.92 % | 93809.3900 | +8050.78 ppm |
| ${}^{101}$Ru | 101 | 57 | 118.8111 | 868.7380 | -86.32 % | 94742.8739 | +7978.55 ppm |
| ${}^{102}$Ru | 102 | 58 | 124.8812 | 877.9576 | -85.78 % | 95676.3692 | +7933.53 ppm |
| ${}^{103}$Ru | 103 | 59 | 130.9402 | 884.1897 | -85.19 % | 96609.8756 | +7858.09 ppm |
| ${}^{104}$Ru | 104 | 60 | 136.9883 | 893.0896 | -84.66 % | 97543.3930 | +7812.00 ppm |
| ${}^{105}$Ru | 105 | 61 | 143.0257 | 898.9997 | -84.09 % | 98476.9210 | +7736.06 ppm |
| ${}^{106}$Ru | 106 | 62 | 149.0526 | 907.4597 | -83.57 % | 99410.4595 | +7687.70 ppm |
| ${}^{107}$Ru | 107 | 63 | 155.0693 | 913.0703 | -83.02 % | 100344.0082 | +7611.53 ppm |
| ${}^{108}$Ru | 108 | 64 | 161.0760 | 920.9405 | -82.51 % | 101277.5669 | +7559.52 ppm |
| ${}^{109}$Ru | 109 | 65 | 167.0729 | 926.0889 | -81.96 % | 102211.1355 | +7481.53 ppm |
| ${}^{110}$Ru | 110 | 66 | 173.0602 | 933.4944 | -81.46 % | 103144.7136 | +7427.26 ppm |
| ${}^{111}$Ru | 111 | 67 | 179.0380 | 938.2784 | -80.92 % | 104078.3012 | +7348.51 ppm |
| ${}^{112}$Ru | 112 | 68 | 185.0067 | 945.1952 | -80.43 % | 105011.8979 | +7291.86 ppm |
| ${}^{113}$Ru | 113 | 69 | 190.9663 | 949.5035 | -79.89 % | 105945.5037 | +7211.33 ppm |
| ${}^{114}$Ru | 114 | 70 | 196.9171 | 955.9282 | -79.40 % | 106879.1184 | +7152.38 ppm |
| ${}^{115}$Ru | 115 | 71 | 202.8592 | 959.8836 | -78.87 % | 107812.7417 | +7071.32 ppm |
| ${}^{116}$Ru | 116 | 72 | 208.7928 | 965.9185 | -78.38 % | 108746.3736 | +7011.13 ppm |
| ${}^{117}$Ru | 117 | 73 | 214.7180 | 969.4108 | -77.85 % | 109680.0137 | +6928.54 ppm |
| ${}^{118}$Ru | 118 | 74 | 220.6351 | 975.0340 | -77.37 % | 110613.6621 | +6866.58 ppm |
| ${}^{119}$Ru | 119 | 75 | 226.5441 | 978.1800 | -76.84 % | 111547.3185 | +6783.66 ppm |
| ${}^{120}$Ru | 120 | 76 | 232.4453 | 983.8800 | -76.37 % | 112480.9828 | +6725.26 ppm |
| ${}^{121}$Ru | 121 | 77 | 238.3387 | 986.8760 | -75.85 % | 113414.6547 | +6643.42 ppm |
| ${}^{122}$Ru | 122 | 78 | 244.2245 | 992.1040 | -75.38 % | 114348.3343 | +6583.02 ppm |
| ${}^{123}$Ru | 123 | 79 | 250.1030 | 994.9470 | -74.86 % | 115282.0213 | +6502.66 ppm |
| ${}^{124}$Ru | 124 | 80 | 255.9740 | 1000.0600 | -74.40 % | 116215.7157 | +6443.45 ppm |
| ${}^{125}$Ru | 125 | 81 | 261.8380 | 1002.8750 | -73.89 % | 117149.4172 | +6365.72 ppm |

### Rhodium (Z = 45)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{88}$Rh | 88 | 43 | 22.2719 | 711.9200 | -96.87 % | 82624.2802 | +8417.19 ppm |
| ${}^{89}$Rh | 89 | 44 | 28.5631 | 728.8210 | -96.08 % | 83557.5545 | +8451.03 ppm |
| ${}^{90}$Rh | 90 | 45 | 34.8383 | 742.8600 | -95.31 % | 84490.8447 | +8450.53 ppm |
| ${}^{91}$Rh | 91 | 46 | 41.0981 | 757.8480 | -94.58 % | 85424.1503 | +8461.56 ppm |
| ${}^{92}$Rh | 92 | 47 | 47.3428 | 770.3547 | -93.85 % | 86357.4711 | +8443.01 ppm |
| ${}^{93}$Rh | 93 | 48 | 53.5727 | 784.4388 | -93.17 % | 87290.8066 | +8443.48 ppm |
| ${}^{94}$Rh | 94 | 49 | 59.7883 | 796.4059 | -92.49 % | 88224.1564 | +8419.69 ppm |
| ${}^{95}$Rh | 95 | 50 | 65.9898 | 809.9102 | -91.85 % | 89157.5203 | +8414.10 ppm |
| ${}^{96}$Rh | 96 | 51 | 72.1776 | 819.3287 | -91.19 % | 90090.8980 | +8362.66 ppm |
| ${}^{97}$Rh | 97 | 52 | 78.3520 | 830.3098 | -90.56 % | 91024.2890 | +8329.89 ppm |
| ${}^{98}$Rh | 98 | 53 | 84.5133 | 838.9588 | -89.93 % | 91957.6931 | +8272.14 ppm |
| ${}^{99}$Rh | 99 | 54 | 90.6619 | 849.4394 | -89.33 % | 92891.1099 | +8235.74 ppm |
| ${}^{100}$Rh | 100 | 55 | 96.7979 | 857.5173 | -88.71 % | 93824.5393 | +8174.18 ppm |
| ${}^{101}$Rh | 101 | 56 | 102.9217 | 867.4099 | -88.13 % | 94757.9809 | +8133.42 ppm |
| ${}^{102}$Rh | 102 | 57 | 109.0336 | 874.8521 | -87.54 % | 95691.4344 | +8067.57 ppm |
| ${}^{103}$Rh | 103 | 58 | 115.1339 | 884.1718 | -86.98 % | 96624.8996 | +8022.87 ppm |
| ${}^{104}$Rh | 104 | 59 | 121.2226 | 891.1708 | -86.40 % | 97558.3763 | +7954.97 ppm |
| ${}^{105}$Rh | 105 | 60 | 127.3002 | 900.1341 | -85.86 % | 98491.8641 | +7908.74 ppm |
| ${}^{106}$Rh | 106 | 61 | 133.3669 | 906.7168 | -85.29 % | 99425.3629 | +7839.18 ppm |
| ${}^{107}$Rh | 107 | 62 | 139.4229 | 915.2891 | -84.77 % | 100358.8723 | +7791.16 ppm |
| ${}^{108}$Rh | 108 | 63 | 145.4683 | 921.5279 | -84.21 % | 101292.3923 | +7720.74 ppm |
| ${}^{109}$Rh | 109 | 64 | 151.5035 | 929.5673 | -83.70 % | 102225.9225 | +7669.60 ppm |
| ${}^{110}$Rh | 110 | 65 | 157.5287 | 935.4681 | -83.16 % | 103159.4628 | +7598.44 ppm |
| ${}^{111}$Rh | 111 | 66 | 163.5440 | 943.0146 | -82.66 % | 104093.0129 | +7544.72 ppm |
| ${}^{112}$Rh | 112 | 67 | 169.5496 | 948.5131 | -82.12 % | 105026.5727 | +7472.25 ppm |
| ${}^{113}$Rh | 113 | 68 | 175.5458 | 955.6203 | -81.63 % | 105960.1419 | +7416.57 ppm |
| ${}^{114}$Rh | 114 | 69 | 181.5328 | 960.6349 | -81.10 % | 106893.7204 | +7342.09 ppm |
| ${}^{115}$Rh | 115 | 70 | 187.5106 | 967.2252 | -80.61 % | 107827.3080 | +7283.82 ppm |
| ${}^{116}$Rh | 116 | 71 | 193.4795 | 971.8030 | -80.09 % | 108760.9045 | +7207.87 ppm |
| ${}^{117}$Rh | 117 | 72 | 199.4397 | 978.0354 | -79.61 % | 109694.5097 | +7148.60 ppm |
| ${}^{118}$Rh | 118 | 73 | 205.3914 | 982.0968 | -79.09 % | 110628.1235 | +7070.51 ppm |
| ${}^{119}$Rh | 119 | 74 | 211.3346 | 988.1040 | -78.61 % | 111561.7457 | +7011.51 ppm |
| ${}^{120}$Rh | 120 | 75 | 217.2696 | 991.9200 | -78.10 % | 112495.3761 | +6934.29 ppm |
| ${}^{121}$Rh | 121 | 76 | 223.1965 | 997.6740 | -77.63 % | 113429.0146 | +6874.81 ppm |
| ${}^{122}$Rh | 122 | 77 | 229.1154 | 1001.3760 | -77.12 % | 114362.6611 | +6798.64 ppm |
| ${}^{123}$Rh | 123 | 78 | 235.0266 | 1006.7550 | -76.66 % | 115296.3154 | +6738.56 ppm |
| ${}^{124}$Rh | 124 | 79 | 240.9301 | 1010.3520 | -76.15 % | 116229.9773 | +6663.91 ppm |
| ${}^{125}$Rh | 125 | 80 | 246.8261 | 1015.5000 | -75.69 % | 117163.6467 | +6604.35 ppm |
| ${}^{126}$Rh | 126 | 81 | 252.7147 | 1018.9620 | -75.20 % | 118097.3235 | +6530.81 ppm |
| ${}^{127}$Rh | 127 | 82 | 258.5961 | 1023.6200 | -74.74 % | 119031.0075 | +6468.36 ppm |
| ${}^{128}$Rh | 128 | 83 | 264.4704 | 1025.2800 | -74.21 % | 119964.6987 | +6382.29 ppm |

### Palladium (Z = 46)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{90}$Pd | 90 | 44 | 18.1368 | 730.1700 | -97.52 % | 84506.7639 | +8497.00 ppm |
| ${}^{91}$Pd | 91 | 45 | 24.4461 | 744.6530 | -96.72 % | 85440.0200 | +8501.27 ppm |
| ${}^{92}$Pd | 92 | 46 | 30.7396 | 761.3524 | -95.96 % | 86373.2919 | +8530.95 ppm |
| ${}^{93}$Pd | 93 | 47 | 37.0176 | 773.6264 | -95.22 % | 87306.5793 | +8508.83 ppm |
| ${}^{94}$Pd | 94 | 48 | 43.2807 | 788.8182 | -94.51 % | 88239.8817 | +8520.99 ppm |
| ${}^{95}$Pd | 95 | 49 | 49.5290 | 800.7532 | -93.81 % | 89173.1988 | +8495.91 ppm |
| ${}^{96}$Pd | 96 | 50 | 55.7630 | 815.0420 | -93.16 % | 90106.5302 | +8498.08 ppm |
| ${}^{97}$Pd | 97 | 51 | 61.9830 | 824.7357 | -92.48 % | 91039.8756 | +8449.02 ppm |
| ${}^{98}$Pd | 98 | 52 | 68.1893 | 836.3222 | -91.85 % | 91973.2347 | +8422.05 ppm |
| ${}^{99}$Pd | 99 | 53 | 74.3822 | 845.2554 | -91.20 % | 92906.6072 | +8366.72 ppm |
| ${}^{100}$Pd | 100 | 54 | 80.5621 | 856.3565 | -90.59 % | 93839.9928 | +8336.13 ppm |
| ${}^{101}$Pd | 101 | 55 | 86.7292 | 864.6473 | -89.97 % | 94773.3911 | +8276.13 ppm |
| ${}^{102}$Pd | 102 | 56 | 92.8838 | 875.1894 | -89.39 % | 95706.8019 | +8241.35 ppm |
| ${}^{103}$Pd | 103 | 57 | 99.0262 | 882.8148 | -88.78 % | 96640.2250 | +8176.70 ppm |
| ${}^{104}$Pd | 104 | 58 | 105.1566 | 892.8242 | -88.22 % | 97573.6599 | +8138.25 ppm |
| ${}^{105}$Pd | 105 | 59 | 111.2754 | 899.9183 | -87.63 % | 98507.1066 | +8070.57 ppm |
| ${}^{106}$Pd | 106 | 60 | 117.3827 | 909.4793 | -87.09 % | 99440.5647 | +8029.49 ppm |
| ${}^{107}$Pd | 107 | 61 | 123.4788 | 916.0157 | -86.52 % | 100374.0341 | +7958.68 ppm |
| ${}^{108}$Pd | 108 | 62 | 129.5639 | 925.2386 | -86.00 % | 101307.5144 | +7916.24 ppm |
| ${}^{109}$Pd | 109 | 63 | 135.6383 | 931.3922 | -85.44 % | 102241.0054 | +7844.18 ppm |
| ${}^{110}$Pd | 110 | 64 | 141.7022 | 940.1879 | -84.93 % | 103174.5069 | +7799.55 ppm |
| ${}^{111}$Pd | 111 | 65 | 147.7558 | 945.9142 | -84.38 % | 104108.0188 | +7725.88 ppm |
| ${}^{112}$Pd | 112 | 66 | 153.7993 | 954.3207 | -83.88 % | 105041.5407 | +7679.53 ppm |
| ${}^{113}$Pd | 113 | 67 | 159.8329 | 959.6615 | -83.34 % | 105975.0725 | +7604.73 ppm |
| ${}^{114}$Pd | 114 | 68 | 165.8568 | 967.6326 | -82.86 % | 106908.6140 | +7556.31 ppm |
| ${}^{115}$Pd | 115 | 69 | 171.8712 | 972.6394 | -82.33 % | 107842.1651 | +7480.93 ppm |
| ${}^{116}$Pd | 116 | 70 | 177.8763 | 980.1160 | -81.85 % | 108775.7254 | +7429.98 ppm |
| ${}^{117}$Pd | 117 | 71 | 183.8722 | 984.7801 | -81.33 % | 109709.2949 | +7353.97 ppm |
| ${}^{118}$Pd | 118 | 72 | 189.8592 | 991.8159 | -80.86 % | 110642.8733 | +7301.08 ppm |
| ${}^{119}$Pd | 119 | 73 | 195.8374 | 995.9062 | -80.34 % | 111576.4605 | +7222.38 ppm |
| ${}^{120}$Pd | 120 | 74 | 201.8070 | 1002.8498 | -79.88 % | 112510.0564 | +7170.80 ppm |
| ${}^{121}$Pd | 121 | 75 | 207.7681 | 1006.8239 | -79.36 % | 113443.6607 | +7093.61 ppm |
| ${}^{122}$Pd | 122 | 76 | 213.7209 | 1013.3290 | -78.91 % | 114377.2733 | +7040.19 ppm |
| ${}^{123}$Pd | 123 | 77 | 219.6656 | 1017.2139 | -78.41 % | 115310.8940 | +6964.68 ppm |
| ${}^{124}$Pd | 124 | 78 | 225.6023 | 1023.2480 | -77.95 % | 116244.5228 | +6909.27 ppm |
| ${}^{125}$Pd | 125 | 79 | 231.5311 | 1026.8750 | -77.45 % | 117178.1594 | +6833.96 ppm |
| ${}^{126}$Pd | 126 | 80 | 237.4522 | 1032.8220 | -77.01 % | 118111.8037 | +6779.41 ppm |
| ${}^{127}$Pd | 127 | 81 | 243.3657 | 1036.3200 | -76.52 % | 119045.4556 | +6705.35 ppm |
| ${}^{128}$Pd | 128 | 82 | 249.2718 | 1041.5360 | -76.07 % | 119979.1149 | +6647.21 ppm |
| ${}^{129}$Pd | 129 | 83 | 255.1706 | 1043.0940 | -75.54 % | 120912.7816 | +6559.19 ppm |
| ${}^{130}$Pd | 130 | 84 | 261.0622 | 1045.9800 | -75.04 % | 121846.4554 | +6483.91 ppm |
| ${}^{131}$Pd | 131 | 85 | 266.9467 | 1047.0830 | -74.51 % | 122780.1363 | +6394.66 ppm |

### Silver (Z = 47)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{92}$Ag | 92 | 45 | 13.8240 | 743.3600 | -98.14 % | 86389.4252 | +8516.21 ppm |
| ${}^{93}$Ag | 93 | 46 | 20.1513 | 760.2750 | -97.35 % | 87322.6633 | +8548.04 ppm |
| ${}^{94}$Ag | 94 | 47 | 26.4629 | 774.3720 | -96.58 % | 88255.9172 | +8546.34 ppm |
| ${}^{95}$Ag | 95 | 48 | 32.7591 | 789.9250 | -95.85 % | 89189.1864 | +8561.97 ppm |
| ${}^{96}$Ag | 96 | 49 | 39.0403 | 802.5879 | -95.14 % | 90122.4706 | +8544.73 ppm |
| ${}^{97}$Ag | 97 | 50 | 45.3069 | 817.0516 | -94.45 % | 91055.7694 | +8547.97 ppm |
| ${}^{98}$Ag | 98 | 51 | 51.5592 | 827.2853 | -93.77 % | 91989.0825 | +8504.53 ppm |
| ${}^{99}$Ag | 99 | 52 | 57.7975 | 839.0027 | -93.11 % | 92922.4096 | +8478.36 ppm |
| ${}^{100}$Ag | 100 | 53 | 64.0222 | 848.4995 | -92.45 % | 93855.7504 | +8428.79 ppm |
| ${}^{101}$Ag | 101 | 54 | 70.2335 | 859.7672 | -91.83 % | 94789.1045 | +8399.34 ppm |
| ${}^{102}$Ag | 102 | 55 | 76.4318 | 868.7508 | -91.20 % | 95722.4716 | +8346.34 ppm |
| ${}^{103}$Ag | 103 | 56 | 82.6173 | 879.3782 | -90.61 % | 96655.8516 | +8311.80 ppm |
| ${}^{104}$Ag | 104 | 57 | 88.7903 | 887.7632 | -90.00 % | 97589.2440 | +8254.69 ppm |
| ${}^{105}$Ag | 105 | 58 | 94.9511 | 897.7889 | -89.42 % | 98522.6486 | +8215.72 ppm |
| ${}^{106}$Ag | 106 | 59 | 101.0999 | 905.7318 | -88.84 % | 99456.0651 | +8156.32 ppm |
| ${}^{107}$Ag | 107 | 60 | 107.2371 | 915.2674 | -88.28 % | 100389.4934 | +8114.27 ppm |
| ${}^{108}$Ag | 108 | 61 | 113.3628 | 922.5388 | -87.71 % | 101322.9332 | +8050.41 ppm |
| ${}^{109}$Ag | 109 | 62 | 119.4772 | 931.7228 | -87.18 % | 102256.3841 | +8006.83 ppm |
| ${}^{110}$Ag | 110 | 63 | 125.5807 | 938.5320 | -86.62 % | 103189.8461 | +7940.78 ppm |
| ${}^{111}$Ag | 111 | 64 | 131.6734 | 947.3614 | -86.10 % | 104123.3188 | +7895.73 ppm |
| ${}^{112}$Ag | 112 | 65 | 137.7556 | 953.8010 | -85.56 % | 105056.8020 | +7828.47 ppm |
| ${}^{113}$Ag | 113 | 66 | 143.8275 | 962.3155 | -85.05 % | 105990.2956 | +7782.40 ppm |
| ${}^{114}$Ag | 114 | 67 | 149.8892 | 968.2908 | -84.52 % | 106923.7993 | +7713.11 ppm |
| ${}^{115}$Ag | 115 | 68 | 155.9409 | 976.4139 | -84.03 % | 107857.3130 | +7665.34 ppm |
| ${}^{116}$Ag | 116 | 69 | 161.9830 | 982.0452 | -83.51 % | 108790.8363 | +7595.23 ppm |
| ${}^{117}$Ag | 117 | 70 | 168.0155 | 989.7558 | -83.02 % | 109724.3692 | +7545.65 ppm |
| ${}^{118}$Ag | 118 | 71 | 174.0386 | 995.1990 | -82.51 % | 110657.9115 | +7476.20 ppm |
| ${}^{119}$Ag | 119 | 72 | 180.0526 | 1002.3623 | -82.04 % | 111591.4630 | +7423.64 ppm |
| ${}^{120}$Ag | 120 | 73 | 186.0576 | 1007.4394 | -81.53 % | 112525.0235 | +7353.23 ppm |
| ${}^{121}$Ag | 121 | 74 | 192.0537 | 1014.2620 | -81.06 % | 113458.5928 | +7299.68 ppm |
| ${}^{122}$Ag | 122 | 75 | 198.0411 | 1019.0366 | -80.57 % | 114392.1707 | +7228.91 ppm |
| ${}^{123}$Ag | 123 | 76 | 204.0200 | 1025.5704 | -80.11 % | 115325.7572 | +7174.85 ppm |
| ${}^{124}$Ag | 124 | 77 | 209.9906 | 1030.3031 | -79.62 % | 116259.3521 | +7106.03 ppm |
| ${}^{125}$Ag | 125 | 78 | 215.9530 | 1036.6644 | -79.17 % | 117192.9552 | +7052.47 ppm |
| ${}^{126}$Ag | 126 | 79 | 221.9073 | 1040.8860 | -78.68 % | 118126.5663 | +6981.90 ppm |
| ${}^{127}$Ag | 127 | 80 | 227.8537 | 1046.9880 | -78.24 % | 119060.1853 | +6927.23 ppm |
| ${}^{128}$Ag | 128 | 81 | 233.7923 | 1051.0080 | -77.76 % | 119993.8121 | +6857.70 ppm |
| ${}^{129}$Ag | 129 | 82 | 239.7233 | 1056.2520 | -77.30 % | 120927.4466 | +6798.53 ppm |
| ${}^{130}$Ag | 130 | 83 | 245.6467 | 1058.4600 | -76.79 % | 121861.0885 | +6714.28 ppm |
| ${}^{131}$Ag | 131 | 84 | 251.5628 | 1061.3620 | -76.30 % | 122794.7378 | +6638.20 ppm |
| ${}^{132}$Ag | 132 | 85 | 257.4717 | 1062.9960 | -75.78 % | 123728.3944 | +6553.48 ppm |
| ${}^{133}$Ag | 133 | 86 | 263.3734 | 1065.7290 | -75.29 % | 124662.0581 | +6478.48 ppm |

### Cadmium (Z = 48)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{94}$Cd | 94 | 46 | 9.3348 | 761.5880 | -98.77 % | 88272.2629 | +8595.26 ppm |
| ${}^{95}$Cd | 95 | 47 | 15.6799 | 776.2450 | -97.98 % | 89205.4832 | +8599.70 ppm |
| ${}^{96}$Cd | 96 | 48 | 22.0094 | 792.8640 | -97.22 % | 90138.7191 | +8625.66 ppm |
| ${}^{97}$Cd | 97 | 49 | 28.3236 | 806.0992 | -96.49 % | 91071.9703 | +8613.80 ppm |
| ${}^{98}$Cd | 98 | 50 | 34.6229 | 821.0729 | -95.78 % | 92005.2364 | +8621.59 ppm |
| ${}^{99}$Cd | 99 | 51 | 40.9076 | 831.4390 | -95.08 % | 92938.5172 | +8578.94 ppm |
| ${}^{100}$Cd | 100 | 52 | 47.1781 | 843.7737 | -94.41 % | 93871.8121 | +8558.63 ppm |
| ${}^{101}$Cd | 101 | 53 | 53.4346 | 853.4869 | -93.74 % | 94805.1210 | +8510.74 ppm |
| ${}^{102}$Cd | 102 | 54 | 59.6775 | 865.3815 | -93.10 % | 95738.4436 | +8487.11 ppm |
| ${}^{103}$Cd | 103 | 55 | 65.9071 | 874.4447 | -92.46 % | 96671.7794 | +8434.29 ppm |
| ${}^{104}$Cd | 104 | 56 | 72.1236 | 885.8328 | -91.86 % | 97605.1283 | +8406.84 ppm |
| ${}^{105}$Cd | 105 | 57 | 78.3274 | 894.2696 | -91.24 % | 98538.4900 | +8349.59 ppm |
| ${}^{106}$Cd | 106 | 58 | 84.5187 | 905.1392 | -90.66 % | 99471.8641 | +8318.41 ppm |
| ${}^{107}$Cd | 107 | 59 | 90.6978 | 913.0687 | -90.07 % | 100405.2504 | +8258.16 ppm |
| ${}^{108}$Cd | 108 | 60 | 96.8649 | 923.4021 | -89.51 % | 101338.6487 | +8223.27 ppm |
| ${}^{109}$Cd | 109 | 61 | 103.0203 | 930.7253 | -88.93 % | 102272.0587 | +8159.21 ppm |
| ${}^{110}$Cd | 110 | 62 | 109.1643 | 940.6403 | -88.39 % | 103205.4802 | +8121.95 ppm |
| ${}^{111}$Cd | 111 | 63 | 115.2970 | 947.6159 | -87.83 % | 104138.9129 | +8056.79 ppm |
| ${}^{112}$Cd | 112 | 64 | 121.4187 | 957.0098 | -87.31 % | 105072.3566 | +8016.29 ppm |
| ${}^{113}$Cd | 113 | 65 | 127.5296 | 963.5496 | -86.76 % | 106005.8111 | +7949.25 ppm |
| ${}^{114}$Cd | 114 | 66 | 133.6299 | 972.5925 | -86.26 % | 106939.2762 | +7907.27 ppm |
| ${}^{115}$Cd | 115 | 67 | 139.7199 | 978.7334 | -85.72 % | 107872.7517 | +7838.78 ppm |
| ${}^{116}$Cd | 116 | 68 | 145.7997 | 987.4327 | -85.23 % | 108806.2373 | +7795.46 ppm |
| ${}^{117}$Cd | 117 | 69 | 151.8696 | 993.2100 | -84.71 % | 109739.7328 | +7725.93 ppm |
| ${}^{118}$Cd | 118 | 70 | 157.9297 | 1001.5645 | -84.23 % | 110673.2382 | +7681.31 ppm |
| ${}^{119}$Cd | 119 | 71 | 163.9802 | 1006.9111 | -83.71 % | 111606.7531 | +7610.17 ppm |
| ${}^{120}$Cd | 120 | 72 | 170.0213 | 1014.9629 | -83.25 % | 112540.2774 | +7564.71 ppm |
| ${}^{121}$Cd | 121 | 73 | 176.0531 | 1020.1507 | -82.74 % | 113473.8110 | +7494.45 ppm |
| ${}^{122}$Cd | 122 | 74 | 182.0759 | 1027.7605 | -82.28 % | 114407.3536 | +7446.93 ppm |
| ${}^{123}$Cd | 123 | 75 | 188.0899 | 1032.6336 | -81.79 % | 115340.9051 | +7376.17 ppm |
| ${}^{124}$Cd | 124 | 76 | 194.0951 | 1039.9902 | -81.34 % | 116274.4653 | +7328.31 ppm |
| ${}^{125}$Cd | 125 | 77 | 200.0917 | 1044.7102 | -80.85 % | 117208.0341 | +7258.46 ppm |
| ${}^{126}$Cd | 126 | 78 | 206.0799 | 1051.6892 | -80.40 % | 118141.6113 | +7209.20 ppm |
| ${}^{127}$Cd | 127 | 79 | 212.0599 | 1056.2459 | -79.92 % | 119075.1967 | +7140.15 ppm |
| ${}^{128}$Cd | 128 | 80 | 218.0318 | 1062.8143 | -79.49 % | 120008.7903 | +7089.25 ppm |
| ${}^{129}$Cd | 129 | 81 | 223.9956 | 1066.7695 | -79.00 % | 120942.3918 | +7017.30 ppm |
| ${}^{130}$Cd | 130 | 82 | 229.9517 | 1072.8363 | -78.57 % | 121876.0012 | +6964.09 ppm |
| ${}^{131}$Cd | 131 | 83 | 235.9001 | 1075.0018 | -78.06 % | 122809.6183 | +6879.55 ppm |
| ${}^{132}$Cd | 132 | 84 | 241.8408 | 1078.3268 | -77.57 % | 123743.2429 | +6805.86 ppm |
| ${}^{133}$Cd | 133 | 85 | 247.7742 | 1080.0930 | -77.06 % | 124676.8750 | +6720.51 ppm |
| ${}^{134}$Cd | 134 | 86 | 253.7003 | 1083.5240 | -76.59 % | 125610.5143 | +6649.78 ppm |
| ${}^{135}$Cd | 135 | 87 | 259.6191 | 1084.8600 | -76.07 % | 126544.1609 | +6564.46 ppm |

### Indium (Z = 49)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{96}$In | 96 | 47 | 4.6704 | 774.6240 | -99.40 % | 90155.2758 | +8613.62 ppm |
| ${}^{97}$In | 97 | 48 | 11.0333 | 792.0050 | -98.61 % | 91088.4783 | +8647.56 ppm |
| ${}^{98}$In | 98 | 49 | 17.3806 | 806.5400 | -97.85 % | 92021.6965 | +8650.21 ppm |
| ${}^{99}$In | 99 | 50 | 23.7126 | 822.0960 | -97.12 % | 92954.9298 | +8663.41 ppm |
| ${}^{100}$In | 100 | 51 | 30.0299 | 832.9749 | -96.39 % | 93888.1780 | +8625.92 ppm |
| ${}^{101}$In | 101 | 52 | 36.3325 | 845.4130 | -95.70 % | 94821.4408 | +8606.12 ppm |
| ${}^{102}$In | 102 | 53 | 42.6210 | 855.6343 | -95.02 % | 95754.7177 | +8563.30 ppm |
| ${}^{103}$In | 103 | 54 | 48.8956 | 867.6431 | -94.36 % | 96688.0086 | +8540.26 ppm |
| ${}^{104}$In | 104 | 55 | 55.1566 | 877.2648 | -93.71 % | 97621.3130 | +8492.93 ppm |
| ${}^{105}$In | 105 | 56 | 61.4042 | 888.7940 | -93.09 % | 98554.6308 | +8466.32 ppm |
| ${}^{106}$In | 106 | 57 | 67.6389 | 897.8329 | -92.47 % | 99487.9615 | +8414.89 ppm |
| ${}^{107}$In | 107 | 58 | 73.8608 | 908.8627 | -91.87 % | 100421.3050 | +8384.71 ppm |
| ${}^{108}$In | 108 | 59 | 80.0703 | 917.4872 | -91.27 % | 101354.6610 | +8331.08 ppm |
| ${}^{109}$In | 109 | 60 | 86.2675 | 927.9282 | -90.70 % | 102288.0292 | +8296.61 ppm |
| ${}^{110}$In | 110 | 61 | 92.4528 | 935.9800 | -90.12 % | 103221.4093 | +8239.36 ppm |
| ${}^{111}$In | 111 | 62 | 98.6263 | 945.9733 | -89.57 % | 104154.8012 | +8202.19 ppm |
| ${}^{112}$In | 112 | 63 | 104.7884 | 953.6427 | -89.01 % | 105088.2046 | +8143.33 ppm |
| ${}^{113}$In | 113 | 64 | 110.9392 | 963.0911 | -88.48 % | 106021.6192 | +8102.66 ppm |
| ${}^{114}$In | 114 | 65 | 117.0790 | 970.3651 | -87.93 % | 106955.0448 | +8042.15 ppm |
| ${}^{115}$In | 115 | 66 | 123.2080 | 979.4029 | -87.42 % | 107888.4812 | +7999.41 ppm |
| ${}^{116}$In | 116 | 67 | 129.3264 | 986.1877 | -86.89 % | 108821.9282 | +7936.47 ppm |
| ${}^{117}$In | 117 | 68 | 135.4344 | 994.9522 | -86.39 % | 109755.3856 | +7893.03 ppm |
| ${}^{118}$In | 118 | 69 | 141.5323 | 1001.3087 | -85.87 % | 110688.8532 | +7828.32 ppm |
| ${}^{119}$In | 119 | 70 | 147.6201 | 1009.8505 | -85.38 % | 111622.3308 | +7784.67 ppm |
| ${}^{120}$In | 120 | 71 | 153.6981 | 1015.9509 | -84.87 % | 112555.8183 | +7719.81 ppm |
| ${}^{121}$In | 121 | 72 | 159.7665 | 1024.1291 | -84.40 % | 113489.3153 | +7674.71 ppm |
| ${}^{122}$In | 122 | 73 | 165.8254 | 1029.9372 | -83.90 % | 114422.8218 | +7609.39 ppm |
| ${}^{123}$In | 123 | 74 | 171.8751 | 1037.8662 | -83.44 % | 115356.3375 | +7563.88 ppm |
| ${}^{124}$In | 124 | 75 | 177.9157 | 1043.3762 | -82.95 % | 116289.8623 | +7498.08 ppm |
| ${}^{125}$In | 125 | 76 | 183.9473 | 1050.9921 | -82.50 % | 117223.3961 | +7451.64 ppm |
| ${}^{126}$In | 126 | 77 | 189.9702 | 1056.4604 | -82.02 % | 118156.9387 | +7387.57 ppm |
| ${}^{127}$In | 127 | 78 | 195.9845 | 1063.6023 | -81.57 % | 119090.4898 | +7338.84 ppm |
| ${}^{128}$In | 128 | 79 | 201.9903 | 1068.9838 | -81.10 % | 120024.0494 | +7276.06 ppm |
| ${}^{129}$In | 129 | 80 | 207.9878 | 1075.6999 | -80.66 % | 120957.6174 | +7225.53 ppm |
| ${}^{130}$In | 130 | 81 | 213.9771 | 1080.8429 | -80.20 % | 121891.1935 | +7162.75 ppm |
| ${}^{131}$In | 131 | 82 | 219.9584 | 1087.0320 | -79.77 % | 122824.7776 | +7109.63 ppm |
| ${}^{132}$In | 132 | 83 | 225.9318 | 1089.4905 | -79.26 % | 123758.3696 | +7026.82 ppm |
| ${}^{133}$In | 133 | 84 | 231.8975 | 1092.8610 | -78.78 % | 124691.9694 | +6952.57 ppm |
| ${}^{134}$In | 134 | 85 | 237.8555 | 1095.1820 | -78.28 % | 125625.5768 | +6871.43 ppm |
| ${}^{135}$In | 135 | 86 | 243.8060 | 1098.3600 | -77.80 % | 126559.1917 | +6798.46 ppm |
| ${}^{136}$In | 136 | 87 | 249.7492 | 1100.3760 | -77.30 % | 127492.8139 | +6716.45 ppm |
| ${}^{137}$In | 137 | 88 | 255.6852 | 1103.2610 | -76.82 % | 128426.4434 | +6643.59 ppm |

### Tin (Z = 50)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{99}$Sn | 99 | 49 | 6.2125 | 807.9390 | -99.23 % | 92971.6476 | +8698.15 ppm |
| ${}^{100}$Sn | 100 | 50 | 12.5775 | 825.1626 | -98.48 % | 93904.8481 | +8728.82 ppm |
| ${}^{101}$Sn | 101 | 51 | 18.9273 | 836.3914 | -97.74 % | 94838.0637 | +8694.53 ppm |
| ${}^{102}$Sn | 102 | 52 | 25.2623 | 849.0920 | -97.02 % | 95771.2941 | +8676.70 ppm |
| ${}^{103}$Sn | 103 | 53 | 31.5828 | 859.3290 | -96.32 % | 96704.5390 | +8633.36 ppm |
| ${}^{104}$Sn | 104 | 54 | 37.8892 | 871.9268 | -95.65 % | 97637.7981 | +8615.76 ppm |
| ${}^{105}$Sn | 105 | 55 | 44.1817 | 881.7090 | -94.99 % | 98571.0710 | +8569.51 ppm |
| ${}^{106}$Sn | 106 | 56 | 50.4606 | 893.7961 | -94.35 % | 99504.3575 | +8547.82 ppm |
| ${}^{107}$Sn | 107 | 57 | 56.7263 | 903.0259 | -93.72 % | 100437.6573 | +8497.73 ppm |
| ${}^{108}$Sn | 108 | 58 | 62.9789 | 914.6549 | -93.11 % | 101370.9700 | +8472.77 ppm |
| ${}^{109}$Sn | 109 | 59 | 69.2188 | 923.2865 | -92.50 % | 102304.2955 | +8418.60 ppm |
| ${}^{110}$Sn | 110 | 60 | 75.4463 | 934.5696 | -91.93 % | 103237.6335 | +8391.64 ppm |
| ${}^{111}$Sn | 111 | 61 | 81.6616 | 942.7375 | -91.34 % | 104170.9836 | +8334.89 ppm |
| ${}^{112}$Sn | 112 | 62 | 87.8649 | 953.5253 | -90.79 % | 105104.3458 | +8304.61 ppm |
| ${}^{113}$Sn | 113 | 63 | 94.0564 | 961.2697 | -90.22 % | 106037.7196 | +8245.79 ppm |
| ${}^{114}$Sn | 114 | 64 | 100.2365 | 971.5726 | -89.68 % | 106971.1050 | +8212.43 ppm |
| ${}^{115}$Sn | 115 | 65 | 106.4053 | 979.1181 | -89.13 % | 107904.5015 | +8153.78 ppm |
| ${}^{116}$Sn | 116 | 66 | 112.5631 | 988.6815 | -88.61 % | 108837.9092 | +8115.09 ppm |
| ${}^{117}$Sn | 117 | 67 | 118.7101 | 995.6246 | -88.08 % | 109771.3277 | +8052.89 ppm |
| ${}^{118}$Sn | 118 | 68 | 124.8464 | 1004.9510 | -87.58 % | 110704.7567 | +8013.73 ppm |
| ${}^{119}$Sn | 119 | 69 | 130.9724 | 1011.4345 | -87.05 % | 111638.1962 | +7949.45 ppm |
| ${}^{120}$Sn | 120 | 70 | 137.0881 | 1020.5386 | -86.57 % | 112571.6460 | +7909.98 ppm |
| ${}^{121}$Sn | 121 | 71 | 143.1937 | 1026.7088 | -86.05 % | 113505.1057 | +7844.99 ppm |
| ${}^{122}$Sn | 122 | 72 | 149.2896 | 1035.5234 | -85.58 % | 114438.5753 | +7804.64 ppm |
| ${}^{123}$Sn | 123 | 73 | 155.3758 | 1041.4694 | -85.08 % | 115372.0545 | +7739.77 ppm |
| ${}^{124}$Sn | 124 | 74 | 161.4525 | 1049.9576 | -84.62 % | 116305.5433 | +7698.22 ppm |
| ${}^{125}$Sn | 125 | 75 | 167.5198 | 1055.6911 | -84.13 % | 117239.0413 | +7633.57 ppm |
| ${}^{126}$Sn | 126 | 76 | 173.5781 | 1063.8839 | -83.68 % | 118172.5485 | +7591.15 ppm |
| ${}^{127}$Sn | 127 | 77 | 179.6274 | 1069.4096 | -83.20 % | 119106.0646 | +7526.74 ppm |
| ${}^{128}$Sn | 128 | 78 | 185.6678 | 1077.3728 | -82.77 % | 120039.5896 | +7484.02 ppm |
| ${}^{129}$Sn | 129 | 79 | 191.6996 | 1082.6733 | -82.29 % | 120973.1232 | +7419.71 ppm |
| ${}^{130}$Sn | 130 | 80 | 197.7229 | 1090.2862 | -81.87 % | 121906.6653 | +7375.70 ppm |
| ${}^{131}$Sn | 131 | 81 | 203.7378 | 1095.4899 | -81.40 % | 122840.2158 | +7312.54 ppm |
| ${}^{132}$Sn | 132 | 82 | 209.7445 | 1102.8432 | -80.98 % | 123773.7745 | +7268.02 ppm |
| ${}^{133}$Sn | 133 | 83 | 215.7432 | 1105.2418 | -80.48 % | 124707.3413 | +7183.94 ppm |
| ${}^{134}$Sn | 134 | 84 | 221.7339 | 1108.8730 | -80.00 % | 125640.9161 | +7111.13 ppm |
| ${}^{135}$Sn | 135 | 85 | 227.7168 | 1111.1428 | -79.51 % | 126574.4986 | +7028.56 ppm |
| ${}^{136}$Sn | 136 | 86 | 233.6920 | 1114.7920 | -79.04 % | 127508.0888 | +6957.92 ppm |
| ${}^{137}$Sn | 137 | 87 | 239.6596 | 1116.8240 | -78.54 % | 128441.6866 | +6876.08 ppm |
| ${}^{138}$Sn | 138 | 88 | 245.6199 | 1120.2840 | -78.08 % | 129375.2918 | +6806.31 ppm |
| ${}^{139}$Sn | 139 | 89 | 251.5728 | 1122.1470 | -77.58 % | 130308.9042 | +6725.47 ppm |
| ${}^{140}$Sn | 140 | 90 | 257.5186 | 1125.3200 | -77.12 % | 131242.5239 | +6656.51 ppm |

### Antimony (Z = 51)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{102}$Sb | 102 | 51 | 7.6014 | 834.4620 | -99.09 % | 95788.1727 | +8707.48 ppm |
| ${}^{103}$Sb | 103 | 52 | 13.9688 | 848.1020 | -98.35 % | 96721.3707 | +8699.26 ppm |
| ${}^{104}$Sb | 104 | 53 | 20.3214 | 858.8320 | -97.63 % | 97654.5835 | +8660.67 ppm |
| ${}^{105}$Sb | 105 | 54 | 26.6597 | 871.6042 | -96.94 % | 98587.8107 | +8644.57 ppm |
| ${}^{106}$Sb | 106 | 55 | 32.9838 | 882.1333 | -96.26 % | 99521.0520 | +8605.80 ppm |
| ${}^{107}$Sb | 107 | 56 | 39.2941 | 894.3846 | -95.61 % | 100454.3071 | +8585.32 ppm |
| ${}^{108}$Sb | 108 | 57 | 45.5908 | 904.2480 | -94.96 % | 101387.5758 | +8541.40 ppm |
| ${}^{109}$Sb | 109 | 58 | 51.8743 | 916.1250 | -94.34 % | 102320.8577 | +8518.43 ppm |
| ${}^{110}$Sb | 110 | 59 | 58.1448 | 925.3950 | -93.72 % | 103254.1526 | +8470.33 ppm |
| ${}^{111}$Sb | 111 | 60 | 64.4027 | 936.8534 | -93.13 % | 104187.4602 | +8444.58 ppm |
| ${}^{112}$Sb | 112 | 61 | 70.6480 | 945.6869 | -92.53 % | 105120.7803 | +8394.01 ppm |
| ${}^{113}$Sb | 113 | 62 | 76.8812 | 956.5762 | -91.96 % | 106054.1125 | +8364.16 ppm |
| ${}^{114}$Sb | 114 | 63 | 83.1024 | 964.7272 | -91.39 % | 106987.4568 | +8308.93 ppm |
| ${}^{115}$Sb | 115 | 64 | 89.3118 | 975.3053 | -90.84 % | 107920.8127 | +8277.63 ppm |
| ${}^{116}$Sb | 116 | 65 | 95.5098 | 983.1952 | -90.29 % | 108854.1802 | +8221.87 ppm |
| ${}^{117}$Sb | 117 | 66 | 101.6965 | 993.0841 | -89.76 % | 109787.5589 | +8185.67 ppm |
| ${}^{118}$Sb | 118 | 67 | 107.8722 | 1000.5120 | -89.22 % | 110720.9487 | +8127.60 ppm |
| ${}^{119}$Sb | 119 | 68 | 114.0370 | 1010.0627 | -88.71 % | 111654.3493 | +8089.92 ppm |
| ${}^{120}$Sb | 120 | 69 | 120.1912 | 1017.0756 | -88.18 % | 112587.7605 | +8030.07 ppm |
| ${}^{121}$Sb | 121 | 70 | 126.3349 | 1026.3289 | -87.69 % | 113521.1822 | +7991.35 ppm |
| ${}^{122}$Sb | 122 | 71 | 132.4684 | 1033.1353 | -87.18 % | 114454.6142 | +7931.63 ppm |
| ${}^{123}$Sb | 123 | 72 | 138.5918 | 1042.0953 | -86.70 % | 115388.0562 | +7891.93 ppm |
| ${}^{124}$Sb | 124 | 73 | 144.7054 | 1048.5628 | -86.20 % | 116321.5080 | +7831.20 ppm |
| ${}^{125}$Sb | 125 | 74 | 150.8092 | 1057.2702 | -85.74 % | 117254.9696 | +7790.92 ppm |
| ${}^{126}$Sb | 126 | 75 | 156.9036 | 1063.4795 | -85.25 % | 118188.4406 | +7729.90 ppm |
| ${}^{127}$Sb | 127 | 76 | 162.9886 | 1071.8560 | -84.79 % | 119121.9211 | +7688.39 ppm |
| ${}^{128}$Sb | 128 | 77 | 169.0644 | 1077.8589 | -84.31 % | 120055.4107 | +7627.54 ppm |
| ${}^{129}$Sb | 129 | 78 | 175.1312 | 1085.9297 | -83.87 % | 120988.9093 | +7585.06 ppm |
| ${}^{130}$Sb | 130 | 79 | 181.1892 | 1091.6573 | -83.40 % | 121922.4167 | +7523.79 ppm |
| ${}^{131}$Sb | 131 | 80 | 187.2384 | 1099.4244 | -82.97 % | 122855.9329 | +7480.39 ppm |
| ${}^{132}$Sb | 132 | 81 | 193.2791 | 1105.1496 | -82.51 % | 123789.4577 | +7420.97 ppm |
| ${}^{133}$Sb | 133 | 82 | 199.3114 | 1112.5091 | -82.08 % | 124722.9908 | +7375.82 ppm |
| ${}^{134}$Sb | 134 | 83 | 205.3354 | 1115.6759 | -81.60 % | 125656.5322 | +7297.55 ppm |
| ${}^{135}$Sb | 135 | 84 | 211.3513 | 1119.4186 | -81.12 % | 126590.0817 | +7225.12 ppm |
| ${}^{136}$Sb | 136 | 85 | 217.3592 | 1122.3064 | -80.63 % | 127523.6393 | +7147.03 ppm |
| ${}^{137}$Sb | 137 | 86 | 223.3592 | 1125.9313 | -80.16 % | 128457.2046 | +7075.97 ppm |
| ${}^{138}$Sb | 138 | 87 | 229.3515 | 1128.5640 | -79.68 % | 129390.7778 | +6998.45 ppm |
| ${}^{139}$Sb | 139 | 88 | 235.3362 | 1132.0160 | -79.21 % | 130324.3585 | +6928.41 ppm |
| ${}^{140}$Sb | 140 | 89 | 241.3135 | 1134.4200 | -78.73 % | 131257.9467 | +6851.26 ppm |
| ${}^{141}$Sb | 141 | 90 | 247.2833 | 1137.7290 | -78.27 % | 132191.5422 | +6781.46 ppm |
| ${}^{142}$Sb | 142 | 91 | 253.2460 | 1139.8340 | -77.78 % | 133125.1450 | +6704.49 ppm |

### Tellurium (Z = 52)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{104}$Te | 104 | 52 | 2.4533 | 848.3619 | -99.71 % | 97671.6692 | +8736.41 ppm |
| ${}^{105}$Te | 105 | 53 | 8.8382 | 859.6179 | -98.97 % | 98604.8498 | +8703.27 ppm |
| ${}^{106}$Te | 106 | 54 | 15.2084 | 873.0974 | -98.26 % | 99538.0450 | +8693.64 ppm |
| ${}^{107}$Te | 107 | 55 | 21.5642 | 883.6060 | -97.56 % | 100471.2546 | +8654.25 ppm |
| ${}^{108}$Te | 108 | 56 | 27.9060 | 896.8020 | -96.89 % | 101404.4783 | +8642.68 ppm |
| ${}^{109}$Te | 109 | 57 | 34.2339 | 906.8070 | -96.22 % | 102337.7158 | +8599.74 ppm |
| ${}^{110}$Te | 110 | 58 | 40.5484 | 919.3928 | -95.59 % | 103270.9667 | +8583.13 ppm |
| ${}^{111}$Te | 111 | 59 | 46.8496 | 928.8217 | -94.96 % | 104204.2309 | +8536.14 ppm |
| ${}^{112}$Te | 112 | 60 | 53.1379 | 940.8731 | -94.35 % | 105137.5081 | +8515.47 ppm |
| ${}^{113}$Te | 113 | 61 | 59.4135 | 949.7239 | -93.74 % | 106070.7979 | +8464.60 ppm |
| ${}^{114}$Te | 114 | 62 | 65.6766 | 961.3379 | -93.17 % | 107004.1002 | +8441.01 ppm |
| ${}^{115}$Te | 115 | 63 | 71.9275 | 969.5823 | -92.58 % | 107937.4147 | +8386.19 ppm |
| ${}^{116}$Te | 116 | 64 | 78.1665 | 980.8546 | -92.03 % | 108870.7411 | +8360.70 ppm |
| ${}^{117}$Te | 117 | 65 | 84.3938 | 988.7577 | -91.46 % | 109804.0793 | +8304.56 ppm |
| ${}^{118}$Te | 118 | 66 | 90.6095 | 999.4242 | -90.93 % | 110737.4290 | +8274.85 ppm |
| ${}^{119}$Te | 119 | 67 | 96.8140 | 1006.9873 | -90.39 % | 111670.7899 | +8217.49 ppm |
| ${}^{120}$Te | 120 | 68 | 103.0074 | 1017.2383 | -89.87 % | 112604.1620 | +8185.44 ppm |
| ${}^{121}$Te | 121 | 69 | 109.1899 | 1024.4906 | -89.34 % | 113537.5448 | +8127.18 ppm |
| ${}^{122}$Te | 122 | 70 | 115.3618 | 1034.3320 | -88.85 % | 114470.9384 | +8092.96 ppm |
| ${}^{123}$Te | 123 | 71 | 121.5232 | 1041.2611 | -88.33 % | 115404.3424 | +8033.73 ppm |
| ${}^{124}$Te | 124 | 72 | 127.6744 | 1050.6855 | -87.85 % | 116337.7566 | +7997.35 ppm |
| ${}^{125}$Te | 125 | 73 | 133.8155 | 1057.2545 | -87.34 % | 117271.1810 | +7936.90 ppm |
| ${}^{126}$Te | 126 | 74 | 139.9467 | 1066.3682 | -86.88 % | 118204.6152 | +7899.36 ppm |
| ${}^{127}$Te | 127 | 75 | 146.0681 | 1072.6558 | -86.38 % | 119138.0592 | +7838.40 ppm |
| ${}^{128}$Te | 128 | 76 | 152.1800 | 1081.4405 | -85.93 % | 120071.5127 | +7799.59 ppm |
| ${}^{129}$Te | 129 | 77 | 158.2825 | 1087.5229 | -85.45 % | 121004.9756 | +7738.79 ppm |
| ${}^{130}$Te | 130 | 78 | 164.3758 | 1095.9423 | -85.00 % | 121938.4477 | +7698.46 ppm |
| ${}^{131}$Te | 131 | 79 | 170.4601 | 1101.8716 | -84.53 % | 122871.9289 | +7638.25 ppm |
| ${}^{132}$Te | 132 | 80 | 176.5355 | 1109.9201 | -84.09 % | 123805.4190 | +7596.40 ppm |
| ${}^{133}$Te | 133 | 81 | 182.6021 | 1115.7404 | -83.63 % | 124738.9178 | +7537.12 ppm |
| ${}^{134}$Te | 134 | 82 | 188.6601 | 1123.4083 | -83.21 % | 125672.4252 | +7493.72 ppm |
| ${}^{135}$Te | 135 | 83 | 194.7096 | 1126.6747 | -82.72 % | 126605.9411 | +7415.74 ppm |
| ${}^{136}$Te | 136 | 84 | 200.7509 | 1131.4425 | -82.26 % | 127539.4653 | +7350.93 ppm |
| ${}^{137}$Te | 137 | 85 | 206.7839 | 1134.3923 | -81.77 % | 128472.9976 | +7272.78 ppm |
| ${}^{138}$Te | 138 | 86 | 212.8089 | 1138.8558 | -81.31 % | 129406.5380 | +7207.69 ppm |
| ${}^{139}$Te | 139 | 87 | 218.8261 | 1141.4363 | -80.83 % | 130340.0863 | +7128.95 ppm |
| ${}^{140}$Te | 140 | 88 | 224.8354 | 1145.6699 | -80.38 % | 131273.6424 | +7064.18 ppm |
| ${}^{141}$Te | 141 | 89 | 230.8371 | 1148.0220 | -79.89 % | 132207.2061 | +6986.12 ppm |
| ${}^{142}$Te | 142 | 90 | 236.8313 | 1152.0460 | -79.44 % | 133140.7774 | +6921.23 ppm |
| ${}^{143}$Te | 143 | 91 | 242.8180 | 1154.0100 | -78.96 % | 134074.3561 | +6842.96 ppm |
| ${}^{144}$Te | 144 | 92 | 248.7975 | 1157.7600 | -78.51 % | 135007.9420 | +6778.66 ppm |
| ${}^{145}$Te | 145 | 93 | 254.7697 | 1159.7100 | -78.03 % | 135941.5352 | +6701.15 ppm |

### Iodine (Z = 53)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{106}$I | 106 | 53 | -2.8655 | 857.4340 | -100.33 % | 99555.3365 | +8716.35 ppm |
| ${}^{107}$I | 107 | 54 | 3.5368 | 871.6220 | -99.59 % | 100488.4997 | +8713.68 ppm |
| ${}^{108}$I | 108 | 55 | 9.9244 | 883.0080 | -98.88 % | 101421.6775 | +8683.22 ppm |
| ${}^{109}$I | 109 | 56 | 16.2977 | 895.9818 | -98.18 % | 102354.8697 | +8668.97 ppm |
| ${}^{110}$I | 110 | 57 | 22.6569 | 906.8484 | -97.50 % | 103288.0759 | +8634.36 ppm |
| ${}^{111}$I | 111 | 58 | 29.0024 | 919.4057 | -96.85 % | 104221.2958 | +8617.02 ppm |
| ${}^{112}$I | 112 | 59 | 35.3345 | 929.5866 | -96.20 % | 105154.5292 | +8577.12 ppm |
| ${}^{113}$I | 113 | 60 | 41.6533 | 941.7141 | -95.58 % | 106087.7758 | +8556.72 ppm |
| ${}^{114}$I | 114 | 61 | 47.9592 | 951.3048 | -94.96 % | 107021.0353 | +8512.68 ppm |
| ${}^{115}$I | 115 | 62 | 54.2524 | 963.0750 | -94.37 % | 107954.3075 | +8490.07 ppm |
| ${}^{116}$I | 116 | 63 | 60.5332 | 972.2292 | -93.77 % | 108887.5921 | +8443.52 ppm |
| ${}^{117}$I | 117 | 64 | 66.8018 | 983.3184 | -93.21 % | 109820.8890 | +8415.80 ppm |
| ${}^{118}$I | 118 | 65 | 73.0584 | 991.9222 | -92.63 % | 110754.1977 | +8365.84 ppm |
| ${}^{119}$I | 119 | 66 | 79.3033 | 1002.8002 | -92.09 % | 111687.5182 | +8337.52 ppm |
| ${}^{120}$I | 120 | 67 | 85.5367 | 1010.8409 | -91.54 % | 112620.8503 | +8284.17 ppm |
| ${}^{121}$I | 121 | 68 | 91.7589 | 1021.4107 | -91.02 % | 113554.1936 | +8254.44 ppm |
| ${}^{122}$I | 122 | 69 | 97.9699 | 1029.3157 | -90.48 % | 114487.5479 | +8201.64 ppm |
| ${}^{123}$I | 123 | 70 | 104.1701 | 1039.2503 | -89.98 % | 115420.9132 | +8167.66 ppm |
| ${}^{124}$I | 124 | 71 | 110.3596 | 1046.7436 | -89.46 % | 116354.2891 | +8112.99 ppm |
| ${}^{125}$I | 125 | 72 | 116.5386 | 1056.2864 | -88.97 % | 117287.6755 | +8077.05 ppm |
| ${}^{126}$I | 126 | 73 | 122.7073 | 1063.4322 | -88.46 % | 118221.0722 | +8021.17 ppm |
| ${}^{127}$I | 127 | 74 | 128.8660 | 1072.5762 | -87.99 % | 119154.4790 | +7983.29 ppm |
| ${}^{128}$I | 128 | 75 | 135.0147 | 1079.4024 | -87.49 % | 120087.8957 | +7926.48 ppm |
| ${}^{129}$I | 129 | 76 | 141.1536 | 1088.2428 | -87.03 % | 121021.3222 | +7887.54 ppm |
| ${}^{130}$I | 130 | 77 | 147.2830 | 1094.7431 | -86.55 % | 121954.7583 | +7829.78 ppm |
| ${}^{131}$I | 131 | 78 | 153.4029 | 1103.3210 | -86.10 % | 122888.2038 | +7790.16 ppm |
| ${}^{132}$I | 132 | 79 | 159.5136 | 1109.6531 | -85.62 % | 123821.6585 | +7732.80 ppm |
| ${}^{133}$I | 133 | 80 | 165.6152 | 1117.8782 | -85.18 % | 124755.1223 | +7691.78 ppm |
| ${}^{134}$I | 134 | 81 | 171.7079 | 1124.1357 | -84.73 % | 125688.5950 | +7635.54 ppm |
| ${}^{135}$I | 135 | 82 | 177.7918 | 1131.9427 | -84.29 % | 126622.0766 | +7592.64 ppm |
| ${}^{136}$I | 136 | 83 | 183.8670 | 1135.7801 | -83.81 % | 127555.5668 | +7518.85 ppm |
| ${}^{137}$I | 137 | 84 | 189.9337 | 1140.6625 | -83.35 % | 128489.0655 | +7454.46 ppm |
| ${}^{138}$I | 138 | 85 | 195.9921 | 1144.3574 | -82.87 % | 129422.5725 | +7381.76 ppm |
| ${}^{139}$I | 139 | 86 | 202.0423 | 1148.9198 | -82.41 % | 130356.0877 | +7316.93 ppm |
| ${}^{140}$I | 140 | 87 | 208.0844 | 1152.1264 | -81.94 % | 131289.6111 | +7242.62 ppm |
| ${}^{141}$I | 141 | 88 | 214.1185 | 1156.5181 | -81.49 % | 132223.1424 | +7178.51 ppm |
| ${}^{142}$I | 142 | 89 | 220.1448 | 1159.4657 | -81.01 % | 133156.6815 | +7104.38 ppm |
| ${}^{143}$I | 143 | 90 | 226.1634 | 1163.5910 | -80.56 % | 134090.2283 | +7039.74 ppm |
| ${}^{144}$I | 144 | 91 | 232.1744 | 1166.1120 | -80.09 % | 135023.7827 | +6965.20 ppm |
| ${}^{145}$I | 145 | 92 | 238.1780 | 1170.0050 | -79.64 % | 135957.3446 | +6901.14 ppm |
| ${}^{146}$I | 146 | 93 | 244.1742 | 1172.5260 | -79.18 % | 136890.9138 | +6827.72 ppm |
| ${}^{147}$I | 147 | 94 | 250.1632 | 1176.1470 | -78.73 % | 137824.4903 | +6764.56 ppm |

### Xenon (Z = 54)

_43 of 43 isotopes with a framework prediction; 43 of 43 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{108}$Xe | 108 | 54 | -8.3539 | 872.0880 | -100.96 % | 101439.1735 | +8755.51 ppm |
| ${}^{109}$Xe | 109 | 55 | -1.9344 | 883.6965 | -100.22 % | 102372.3195 | +8726.58 ppm |
| ${}^{110}$Xe | 110 | 56 | 4.4705 | 897.5209 | -99.50 % | 103305.4800 | +8720.14 ppm |
| ${}^{111}$Xe | 111 | 57 | 10.8611 | 908.2020 | -98.80 % | 104238.6548 | +8683.16 ppm |
| ${}^{112}$Xe | 112 | 58 | 17.2377 | 921.7672 | -98.13 % | 105171.8436 | +8675.11 ppm |
| ${}^{113}$Xe | 113 | 59 | 23.6006 | 932.0158 | -97.47 % | 106105.0461 | +8635.41 ppm |
| ${}^{114}$Xe | 114 | 60 | 29.9501 | 944.9694 | -96.83 % | 107038.2620 | +8622.24 ppm |
| ${}^{115}$Xe | 115 | 61 | 36.2864 | 954.6116 | -96.20 % | 107971.4911 | +8578.22 ppm |
| ${}^{116}$Xe | 116 | 62 | 42.6098 | 967.0730 | -95.59 % | 108904.7331 | +8561.42 ppm |
| ${}^{117}$Xe | 117 | 63 | 48.9206 | 976.2828 | -94.99 % | 109837.9878 | +8514.90 ppm |
| ${}^{118}$Xe | 118 | 64 | 55.2189 | 988.2479 | -94.41 % | 110771.2549 | +8494.58 ppm |
| ${}^{119}$Xe | 119 | 65 | 61.5051 | 997.0346 | -93.83 % | 111704.5342 | +8445.78 ppm |
| ${}^{120}$Xe | 120 | 66 | 67.7792 | 1008.4839 | -93.28 % | 112637.8254 | +8421.93 ppm |
| ${}^{121}$Xe | 121 | 67 | 74.0417 | 1016.8637 | -92.72 % | 113571.1284 | +8371.10 ppm |
| ${}^{122}$Xe | 122 | 68 | 80.2927 | 1027.8091 | -92.19 % | 114504.4428 | +8343.98 ppm |
| ${}^{123}$Xe | 123 | 69 | 86.5323 | 1035.7736 | -91.65 % | 115437.7686 | +8291.15 ppm |
| ${}^{124}$Xe | 124 | 70 | 92.7609 | 1046.2641 | -91.13 % | 116371.1054 | +8261.34 ppm |
| ${}^{125}$Xe | 125 | 71 | 98.9786 | 1053.8674 | -90.61 % | 117304.4532 | +8207.07 ppm |
| ${}^{126}$Xe | 126 | 72 | 105.1856 | 1063.8857 | -90.11 % | 118237.8116 | +8174.52 ppm |
| ${}^{127}$Xe | 127 | 73 | 111.3821 | 1071.1315 | -89.60 % | 119171.1805 | +8118.93 ppm |
| ${}^{128}$Xe | 128 | 74 | 117.5683 | 1080.7425 | -89.12 % | 120104.5597 | +8084.30 ppm |
| ${}^{129}$Xe | 129 | 75 | 123.7444 | 1087.6494 | -88.62 % | 121037.9491 | +8027.59 ppm |
| ${}^{130}$Xe | 130 | 76 | 129.9105 | 1096.9051 | -88.16 % | 121971.3484 | +7991.41 ppm |
| ${}^{131}$Xe | 131 | 77 | 136.0668 | 1103.5095 | -87.67 % | 122904.7575 | +7933.94 ppm |
| ${}^{132}$Xe | 132 | 78 | 142.2136 | 1112.4462 | -87.22 % | 123838.1762 | +7896.55 ppm |
| ${}^{133}$Xe | 133 | 79 | 148.3508 | 1118.8821 | -86.74 % | 124771.6043 | +7839.45 ppm |
| ${}^{134}$Xe | 134 | 80 | 154.4788 | 1127.4357 | -86.30 % | 125705.0417 | +7800.38 ppm |
| ${}^{135}$Xe | 135 | 81 | 160.5977 | 1133.7946 | -85.84 % | 126638.4883 | +7744.36 ppm |
| ${}^{136}$Xe | 136 | 82 | 166.7076 | 1141.8817 | -85.40 % | 127571.9438 | +7703.00 ppm |
| ${}^{137}$Xe | 137 | 83 | 172.8087 | 1145.9073 | -84.92 % | 128505.4082 | +7630.22 ppm |
| ${}^{138}$Xe | 138 | 84 | 178.9011 | 1151.5674 | -84.46 % | 129438.8812 | +7571.38 ppm |
| ${}^{139}$Xe | 139 | 85 | 184.9849 | 1155.3111 | -83.99 % | 130372.3628 | +7498.54 ppm |
| ${}^{140}$Xe | 140 | 86 | 191.0604 | 1160.7242 | -83.54 % | 131305.8528 | +7439.72 ppm |
| ${}^{141}$Xe | 141 | 87 | 197.1276 | 1164.0064 | -83.06 % | 132239.3510 | +7365.44 ppm |
| ${}^{142}$Xe | 142 | 88 | 203.1866 | 1169.1101 | -82.62 % | 133172.8573 | +7306.15 ppm |
| ${}^{143}$Xe | 143 | 89 | 209.2377 | 1172.1546 | -82.15 % | 134106.3717 | +7232.18 ppm |
| ${}^{144}$Xe | 144 | 90 | 215.2809 | 1176.8954 | -81.71 % | 135039.8939 | +7172.04 ppm |
| ${}^{145}$Xe | 145 | 91 | 221.3163 | 1179.5877 | -81.24 % | 135973.4239 | +7097.52 ppm |
| ${}^{146}$Xe | 146 | 92 | 227.3441 | 1184.1206 | -80.80 % | 136906.9615 | +7037.71 ppm |
| ${}^{147}$Xe | 147 | 93 | 233.3644 | 1186.5840 | -80.33 % | 137840.5067 | +6963.93 ppm |
| ${}^{148}$Xe | 148 | 94 | 239.3773 | 1190.9560 | -79.90 % | 138774.0592 | +6904.40 ppm |
| ${}^{149}$Xe | 149 | 95 | 245.3829 | 1193.3410 | -79.44 % | 139707.6190 | +6831.94 ppm |
| ${}^{150}$Xe | 150 | 96 | 251.3814 | 1197.4500 | -79.01 % | 140641.1860 | +6772.32 ppm |

### Caesium (Z = 55)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{111}$Cs | 111 | 56 | -7.5744 | 895.7700 | -100.85 % | 104256.3079 | +8740.56 ppm |
| ${}^{112}$Cs | 112 | 57 | -1.1523 | 907.4240 | -100.13 % | 105189.4513 | +8712.29 ppm |
| ${}^{113}$Cs | 113 | 58 | 5.2555 | 920.7944 | -99.43 % | 106122.6088 | +8702.26 ppm |
| ${}^{114}$Cs | 114 | 59 | 11.6494 | 931.7871 | -98.75 % | 107055.7804 | +8669.46 ppm |
| ${}^{115}$Cs | 115 | 60 | 18.0297 | 944.8400 | -98.09 % | 107988.9656 | +8657.06 ppm |
| ${}^{116}$Cs | 116 | 61 | 24.3965 | 955.2600 | -97.45 % | 108922.1641 | +8620.05 ppm |
| ${}^{117}$Cs | 117 | 62 | 30.7502 | 967.8082 | -96.82 % | 109855.3759 | +8603.32 ppm |
| ${}^{118}$Cs | 118 | 63 | 37.0910 | 977.7958 | -96.21 % | 110788.6005 | +8563.71 ppm |
| ${}^{119}$Cs | 119 | 64 | 43.4191 | 989.7628 | -95.61 % | 111721.8378 | +8542.90 ppm |
| ${}^{120}$Cs | 120 | 65 | 49.7349 | 999.4177 | -95.02 % | 112655.0875 | +8501.68 ppm |
| ${}^{121}$Cs | 121 | 66 | 56.0385 | 1010.7027 | -94.46 % | 113588.3493 | +8475.84 ppm |
| ${}^{122}$Cs | 122 | 67 | 62.3301 | 1019.8165 | -93.89 % | 114521.6231 | +8431.25 ppm |
| ${}^{123}$Cs | 123 | 68 | 68.6100 | 1030.7867 | -93.34 % | 115454.9086 | +8403.83 ppm |
| ${}^{124}$Cs | 124 | 69 | 74.8784 | 1039.5554 | -92.80 % | 116388.2056 | +8357.72 ppm |
| ${}^{125}$Cs | 125 | 70 | 81.1355 | 1049.9754 | -92.27 % | 117321.5140 | +8326.76 ppm |
| ${}^{126}$Cs | 126 | 71 | 87.3815 | 1058.3077 | -91.74 % | 118254.8334 | +8278.43 ppm |
| ${}^{127}$Cs | 127 | 72 | 93.6166 | 1068.2683 | -91.24 % | 119188.1637 | +8244.85 ppm |
| ${}^{128}$Cs | 128 | 73 | 99.8410 | 1076.0314 | -90.72 % | 120121.5047 | +8193.28 ppm |
| ${}^{129}$Cs | 129 | 74 | 106.0549 | 1085.6700 | -90.23 % | 121054.8562 | +8158.35 ppm |
| ${}^{130}$Cs | 130 | 75 | 112.2585 | 1093.1420 | -89.73 % | 121988.2181 | +8105.99 ppm |
| ${}^{131}$Cs | 131 | 76 | 118.4519 | 1102.3692 | -89.25 % | 122921.5901 | +8069.02 ppm |
| ${}^{132}$Cs | 132 | 77 | 124.6353 | 1109.5376 | -88.77 % | 123854.9721 | +8015.81 ppm |
| ${}^{133}$Cs | 133 | 78 | 130.8090 | 1118.5272 | -88.31 % | 124788.3639 | +7978.30 ppm |
| ${}^{134}$Cs | 134 | 79 | 136.9730 | 1125.4187 | -87.83 % | 125721.7653 | +7924.48 ppm |
| ${}^{135}$Cs | 135 | 80 | 143.1275 | 1134.1808 | -87.38 % | 126655.1762 | +7886.53 ppm |
| ${}^{136}$Cs | 136 | 81 | 149.2727 | 1141.0090 | -86.92 % | 127588.5964 | +7833.82 ppm |
| ${}^{137}$Cs | 137 | 82 | 155.4087 | 1149.2873 | -86.48 % | 128522.0258 | +7793.41 ppm |
| ${}^{138}$Cs | 138 | 83 | 161.5358 | 1153.6998 | -86.00 % | 129455.4642 | +7723.33 ppm |
| ${}^{139}$Cs | 139 | 84 | 167.6540 | 1159.5852 | -85.54 % | 130388.9114 | +7665.81 ppm |
| ${}^{140}$Cs | 140 | 85 | 173.7634 | 1164.0052 | -85.07 % | 131322.3674 | +7597.84 ppm |
| ${}^{141}$Cs | 141 | 86 | 179.8643 | 1169.5041 | -84.62 % | 132255.8319 | +7539.19 ppm |
| ${}^{142}$Cs | 142 | 87 | 185.9567 | 1173.6126 | -84.16 % | 133189.3049 | +7470.84 ppm |
| ${}^{143}$Cs | 143 | 88 | 192.0409 | 1178.8449 | -83.71 % | 134122.7862 | +7412.01 ppm |
| ${}^{144}$Cs | 144 | 89 | 198.1168 | 1182.5121 | -83.25 % | 135056.2757 | +7342.30 ppm |
| ${}^{145}$Cs | 145 | 90 | 204.1848 | 1187.3665 | -82.80 % | 135989.7732 | +7282.48 ppm |
| ${}^{146}$Cs | 146 | 91 | 210.2448 | 1190.6937 | -82.34 % | 136923.2786 | +7212.22 ppm |
| ${}^{147}$Cs | 147 | 92 | 216.2970 | 1195.3747 | -81.91 % | 137856.7918 | +7152.94 ppm |
| ${}^{148}$Cs | 148 | 93 | 222.3415 | 1198.4369 | -81.45 % | 138790.3127 | +7082.70 ppm |
| ${}^{149}$Cs | 149 | 94 | 228.3785 | 1202.8770 | -81.01 % | 139723.8411 | +7023.60 ppm |
| ${}^{150}$Cs | 150 | 95 | 234.4080 | 1205.8500 | -80.56 % | 140657.3770 | +6954.40 ppm |
| ${}^{151}$Cs | 151 | 96 | 240.4302 | 1209.9630 | -80.13 % | 141590.9202 | +6895.05 ppm |
| ${}^{152}$Cs | 152 | 97 | 246.4452 | 1212.9600 | -79.68 % | 142524.4707 | +6827.57 ppm |

### Barium (Z = 56)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{113}$Ba | 113 | 57 | -13.3820 | 907.9550 | -101.47 % | 106140.4641 | +8756.39 ppm |
| ${}^{114}$Ba | 114 | 58 | -6.9429 | 922.2243 | -100.75 % | 107073.5903 | +8753.81 ppm |
| ${}^{115}$Ba | 115 | 59 | -0.5179 | 933.3400 | -100.06 % | 108006.7308 | +8721.43 ppm |
| ${}^{116}$Ba | 116 | 60 | 5.8931 | 946.7920 | -99.38 % | 108939.8852 | +8712.57 ppm |
| ${}^{117}$Ba | 117 | 61 | 12.2906 | 957.9907 | -98.72 % | 109873.0532 | +8681.94 ppm |
| ${}^{118}$Ba | 118 | 62 | 18.6746 | 970.7860 | -98.08 % | 110806.2345 | +8667.22 ppm |
| ${}^{119}$Ba | 119 | 63 | 25.0456 | 981.2655 | -97.45 % | 111739.4290 | +8631.46 ppm |
| ${}^{120}$Ba | 120 | 64 | 31.4036 | 993.6354 | -96.84 % | 112672.6364 | +8613.63 ppm |
| ${}^{121}$Ba | 121 | 65 | 37.7491 | 1003.5629 | -96.24 % | 113605.8563 | +8574.35 ppm |
| ${}^{122}$Ba | 122 | 66 | 44.0822 | 1015.4983 | -95.66 % | 114539.0887 | +8553.64 ppm |
| ${}^{123}$Ba | 123 | 67 | 50.4030 | 1024.6157 | -95.08 % | 115472.3332 | +8508.55 ppm |
| ${}^{124}$Ba | 124 | 68 | 56.7120 | 1036.1218 | -94.53 % | 116405.5897 | +8485.17 ppm |
| ${}^{125}$Ba | 125 | 69 | 63.0092 | 1044.7723 | -93.97 % | 117338.8579 | +8437.51 ppm |
| ${}^{126}$Ba | 126 | 70 | 69.2950 | 1055.8446 | -93.44 % | 118272.1376 | +8411.52 ppm |
| ${}^{127}$Ba | 127 | 71 | 75.5694 | 1064.0639 | -92.90 % | 119205.4286 | +8361.71 ppm |
| ${}^{128}$Ba | 128 | 72 | 81.8327 | 1074.6864 | -92.39 % | 120138.7306 | +8333.10 ppm |
| ${}^{129}$Ba | 129 | 73 | 88.0852 | 1082.4495 | -91.86 % | 121072.0436 | +8281.02 ppm |
| ${}^{130}$Ba | 130 | 74 | 94.3269 | 1092.7167 | -91.37 % | 122005.3674 | +8250.69 ppm |
| ${}^{131}$Ba | 131 | 75 | 100.5580 | 1100.2102 | -90.86 % | 122938.7016 | +8197.97 ppm |
| ${}^{132}$Ba | 132 | 76 | 106.7789 | 1110.0375 | -90.38 % | 123872.0462 | +8165.29 ppm |
| ${}^{133}$Ba | 133 | 77 | 112.9895 | 1117.2274 | -89.89 % | 124805.4010 | +8111.71 ppm |
| ${}^{134}$Ba | 134 | 78 | 119.1902 | 1126.6952 | -89.42 % | 125738.7657 | +8077.41 ppm |
| ${}^{135}$Ba | 135 | 79 | 125.3811 | 1133.6672 | -88.94 % | 126672.1403 | +8023.68 ppm |
| ${}^{136}$Ba | 136 | 80 | 131.5622 | 1142.7749 | -88.49 % | 127605.5245 | +7987.83 ppm |
| ${}^{137}$Ba | 137 | 81 | 137.7339 | 1149.6805 | -88.02 % | 128538.9183 | +7935.16 ppm |
| ${}^{138}$Ba | 138 | 82 | 143.8962 | 1158.2923 | -87.58 % | 129472.3214 | +7896.72 ppm |
| ${}^{139}$Ba | 139 | 83 | 150.0494 | 1163.0157 | -87.10 % | 130405.7337 | +7828.62 ppm |
| ${}^{140}$Ba | 140 | 84 | 156.1935 | 1169.4410 | -86.64 % | 131339.1550 | +7774.73 ppm |
| ${}^{141}$Ba | 141 | 85 | 162.3287 | 1173.9769 | -86.17 % | 132272.5852 | +7707.16 ppm |
| ${}^{142}$Ba | 142 | 86 | 168.4551 | 1180.1580 | -85.73 % | 133206.0242 | +7653.16 ppm |
| ${}^{143}$Ba | 143 | 87 | 174.5729 | 1184.3243 | -85.26 % | 134139.4718 | +7584.72 ppm |
| ${}^{144}$Ba | 144 | 88 | 180.6823 | 1190.2255 | -84.82 % | 135072.9279 | +7530.35 ppm |
| ${}^{145}$Ba | 145 | 89 | 186.7833 | 1194.0459 | -84.36 % | 136006.3923 | +7461.26 ppm |
| ${}^{146}$Ba | 146 | 90 | 192.8761 | 1199.4673 | -83.92 % | 136939.8649 | +7405.05 ppm |
| ${}^{147}$Ba | 147 | 91 | 198.9608 | 1202.9364 | -83.46 % | 137873.3456 | +7335.29 ppm |
| ${}^{148}$Ba | 148 | 92 | 205.0376 | 1208.2885 | -83.03 % | 138806.8343 | +7280.30 ppm |
| ${}^{149}$Ba | 149 | 93 | 211.1065 | 1211.6456 | -82.58 % | 139740.3308 | +7211.63 ppm |
| ${}^{150}$Ba | 150 | 94 | 217.1677 | 1216.7761 | -82.15 % | 140673.8350 | +7156.72 ppm |
| ${}^{151}$Ba | 151 | 95 | 223.2213 | 1219.9290 | -81.70 % | 141607.3469 | +7088.20 ppm |
| ${}^{152}$Ba | 152 | 96 | 229.2674 | 1224.6640 | -81.28 % | 142540.8662 | +7032.17 ppm |
| ${}^{153}$Ba | 153 | 97 | 235.3061 | 1227.5190 | -80.83 % | 143474.3929 | +6964.14 ppm |
| ${}^{154}$Ba | 154 | 98 | 241.3375 | 1232.1540 | -80.41 % | 144407.9269 | +6908.20 ppm |

### Lanthanum (Z = 57)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{116}$La | 116 | 59 | -12.9002 | 931.7120 | -101.38 % | 108957.8962 | +8745.50 ppm |
| ${}^{117}$La | 117 | 60 | -6.4582 | 946.0620 | -100.68 % | 109891.0197 | +8743.28 ppm |
| ${}^{118}$La | 118 | 61 | -0.0301 | 957.4520 | -100.00 % | 110824.1570 | +8714.86 ppm |
| ${}^{119}$La | 119 | 62 | 6.3844 | 970.9210 | -99.34 % | 111757.3079 | +8705.70 ppm |
| ${}^{120}$La | 120 | 63 | 12.7855 | 981.4800 | -98.70 % | 112690.4721 | +8671.10 ppm |
| ${}^{121}$La | 121 | 64 | 19.1736 | 994.2570 | -98.07 % | 113623.6495 | +8655.71 ppm |
| ${}^{122}$La | 122 | 65 | 25.5489 | 1004.6700 | -97.46 % | 114556.8396 | +8620.55 ppm |
| ${}^{123}$La | 123 | 66 | 31.9115 | 1016.8410 | -96.86 % | 115490.0424 | +8601.53 ppm |
| ${}^{124}$La | 124 | 67 | 38.2618 | 1026.5083 | -96.27 % | 116423.2576 | +8561.07 ppm |
| ${}^{125}$La | 125 | 68 | 44.5999 | 1038.0805 | -95.70 % | 117356.4849 | +8537.78 ppm |
| ${}^{126}$La | 126 | 69 | 50.9261 | 1047.3658 | -95.14 % | 118289.7241 | +8495.29 ppm |
| ${}^{127}$La | 127 | 70 | 57.2405 | 1058.3597 | -94.59 % | 119222.9751 | +8468.15 ppm |
| ${}^{128}$La | 128 | 71 | 63.5435 | 1067.1604 | -94.05 % | 120156.2376 | +8422.96 ppm |
| ${}^{129}$La | 129 | 72 | 69.8351 | 1077.9298 | -93.52 % | 121089.5113 | +8395.10 ppm |
| ${}^{130}$La | 130 | 73 | 76.1157 | 1086.3049 | -92.99 % | 122022.7962 | +8347.81 ppm |
| ${}^{131}$La | 131 | 74 | 82.3853 | 1096.5182 | -92.49 % | 122956.0920 | +8316.53 ppm |
| ${}^{132}$La | 132 | 75 | 88.6442 | 1104.5438 | -91.97 % | 123889.3985 | +8267.86 ppm |
| ${}^{133}$La | 133 | 76 | 94.8926 | 1114.3859 | -91.48 % | 124822.7156 | +8234.80 ppm |
| ${}^{134}$La | 134 | 77 | 101.1306 | 1122.1815 | -90.99 % | 125756.0430 | +8185.77 ppm |
| ${}^{135}$La | 135 | 78 | 107.3584 | 1131.6776 | -90.51 % | 126689.3806 | +8151.19 ppm |
| ${}^{136}$La | 136 | 79 | 113.5762 | 1139.1430 | -90.03 % | 127622.7282 | +8101.03 ppm |
| ${}^{137}$La | 137 | 80 | 119.7842 | 1148.3177 | -89.57 % | 128556.0857 | +8065.19 ppm |
| ${}^{138}$La | 138 | 81 | 125.9825 | 1155.7615 | -89.10 % | 129489.4528 | +8016.37 ppm |
| ${}^{139}$La | 139 | 82 | 132.1712 | 1164.5418 | -88.65 % | 130422.8295 | +7978.73 ppm |
| ${}^{140}$La | 140 | 83 | 138.3506 | 1169.7028 | -88.17 % | 131356.2156 | +7913.71 ppm |
| ${}^{141}$La | 141 | 84 | 144.5207 | 1176.3919 | -87.71 % | 132289.6108 | +7861.42 ppm |
| ${}^{142}$La | 142 | 85 | 150.6818 | 1181.5573 | -87.25 % | 133223.0152 | +7798.32 ppm |
| ${}^{143}$La | 143 | 86 | 156.8339 | 1187.7762 | -86.80 % | 134156.4285 | +7744.15 ppm |
| ${}^{144}$La | 144 | 87 | 162.9773 | 1192.5257 | -86.33 % | 135089.8506 | +7679.75 ppm |
| ${}^{145}$La | 145 | 88 | 169.1120 | 1198.5827 | -85.89 % | 136023.2813 | +7626.06 ppm |
| ${}^{146}$La | 146 | 89 | 175.2382 | 1203.0398 | -85.43 % | 136956.7205 | +7561.32 ppm |
| ${}^{147}$La | 147 | 90 | 181.3560 | 1208.5684 | -84.99 % | 137890.1681 | +7505.41 ppm |
| ${}^{148}$La | 148 | 91 | 187.4655 | 1212.6700 | -84.54 % | 138823.6240 | +7439.89 ppm |
| ${}^{149}$La | 149 | 92 | 193.5670 | 1218.2525 | -84.11 % | 139757.0880 | +7386.06 ppm |
| ${}^{150}$La | 150 | 93 | 199.6604 | 1222.4151 | -83.67 % | 140690.5600 | +7322.77 ppm |
| ${}^{151}$La | 151 | 94 | 205.7459 | 1227.4856 | -83.24 % | 141624.0399 | +7266.88 ppm |
| ${}^{152}$La | 152 | 95 | 211.8237 | 1231.5040 | -82.80 % | 142557.5275 | +7204.53 ppm |
| ${}^{153}$La | 153 | 96 | 217.8938 | 1236.3930 | -82.38 % | 143491.0228 | +7148.64 ppm |
| ${}^{154}$La | 154 | 97 | 223.9564 | 1239.8540 | -81.94 % | 144424.5256 | +7084.40 ppm |
| ${}^{155}$La | 155 | 98 | 230.0116 | 1244.3400 | -81.52 % | 145358.0359 | +7027.54 ppm |
| ${}^{156}$La | 156 | 99 | 236.0595 | 1247.5320 | -81.08 % | 146291.5534 | +6962.58 ppm |
| ${}^{157}$La | 157 | 100 | 242.1001 | 1251.6040 | -80.66 % | 147225.0782 | +6904.70 ppm |

### Cerium (Z = 58)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{119}$Ce | 119 | 61 | -12.5645 | 958.9020 | -101.31 % | 111775.4744 | +8767.70 ppm |
| ${}^{120}$Ce | 120 | 62 | -6.1194 | 972.9600 | -100.63 % | 112708.5948 | +8762.52 ppm |
| ${}^{121}$Ce | 121 | 63 | 0.3121 | 983.9720 | -99.97 % | 113641.7287 | +8731.13 ppm |
| ${}^{122}$Ce | 122 | 64 | 6.7302 | 997.2280 | -99.33 % | 114574.8759 | +8720.11 ppm |
| ${}^{123}$Ce | 123 | 65 | 13.1354 | 1007.7390 | -98.70 % | 115508.0362 | +8684.98 ppm |
| ${}^{124}$Ce | 124 | 66 | 19.5277 | 1020.3960 | -98.09 % | 116441.2094 | +8669.90 ppm |
| ${}^{125}$Ce | 125 | 67 | 25.9074 | 1030.2500 | -97.49 % | 117374.3951 | +8630.14 ppm |
| ${}^{126}$Ce | 126 | 68 | 32.2748 | 1042.4305 | -96.90 % | 118307.5931 | +8611.92 ppm |
| ${}^{127}$Ce | 127 | 69 | 38.6300 | 1051.6606 | -96.33 % | 119240.8033 | +8568.47 ppm |
| ${}^{128}$Ce | 128 | 70 | 44.9733 | 1063.2865 | -95.77 % | 120174.0254 | +8546.08 ppm |
| ${}^{129}$Ce | 129 | 71 | 51.3049 | 1072.1114 | -95.21 % | 121107.2593 | +8500.60 ppm |
| ${}^{130}$Ce | 130 | 72 | 57.6250 | 1083.3181 | -94.68 % | 122040.5046 | +8475.77 ppm |
| ${}^{131}$Ce | 131 | 73 | 63.9337 | 1091.6750 | -94.14 % | 122973.7613 | +8427.84 ppm |
| ${}^{132}$Ce | 132 | 74 | 70.2314 | 1102.5065 | -93.63 % | 123907.0290 | +8401.04 ppm |
| ${}^{133}$Ce | 133 | 75 | 76.5182 | 1110.5274 | -93.11 % | 124840.3077 | +8351.84 ppm |
| ${}^{134}$Ce | 134 | 76 | 82.7942 | 1121.0134 | -92.61 % | 125773.5971 | +8323.38 ppm |
| ${}^{135}$Ce | 135 | 77 | 89.0596 | 1128.8681 | -92.11 % | 126706.8970 | +8274.32 ppm |
| ${}^{136}$Ce | 136 | 78 | 95.3147 | 1138.8317 | -91.63 % | 127640.2074 | +8242.85 ppm |
| ${}^{137}$Ce | 137 | 79 | 101.5596 | 1146.3132 | -91.14 % | 128573.5279 | +8192.30 ppm |
| ${}^{138}$Ce | 138 | 80 | 107.7944 | 1156.0316 | -90.68 % | 129506.8585 | +8160.12 ppm |
| ${}^{139}$Ce | 139 | 81 | 114.0194 | 1163.4948 | -90.20 % | 130440.1989 | +8110.91 ppm |
| ${}^{140}$Ce | 140 | 82 | 120.2347 | 1172.6826 | -89.75 % | 131373.5491 | +8075.81 ppm |
| ${}^{141}$Ce | 141 | 83 | 126.4404 | 1178.1108 | -89.27 % | 132306.9088 | +8012.41 ppm |
| ${}^{142}$Ce | 142 | 84 | 132.6367 | 1185.2839 | -88.81 % | 133240.2779 | +7963.29 ppm |
| ${}^{143}$Ce | 143 | 85 | 138.8238 | 1190.4287 | -88.34 % | 134173.6563 | +7899.56 ppm |
| ${}^{144}$Ce | 144 | 86 | 145.0017 | 1197.3256 | -87.89 % | 135107.0437 | +7849.96 ppm |
| ${}^{145}$Ce | 145 | 87 | 151.1707 | 1202.0320 | -87.42 % | 136040.4402 | +7784.77 ppm |
| ${}^{146}$Ce | 146 | 88 | 157.3309 | 1208.6622 | -86.98 % | 136973.8454 | +7734.79 ppm |
| ${}^{147}$Ce | 147 | 89 | 163.4824 | 1213.1215 | -86.52 % | 137907.2593 | +7669.58 ppm |
| ${}^{148}$Ce | 148 | 90 | 169.6254 | 1219.5774 | -86.09 % | 138840.6818 | +7619.91 ppm |
| ${}^{149}$Ce | 149 | 91 | 175.7599 | 1223.9202 | -85.64 % | 139774.1127 | +7555.62 ppm |
| ${}^{150}$Ce | 150 | 92 | 181.8861 | 1230.1684 | -85.21 % | 140707.5519 | +7506.01 ppm |
| ${}^{151}$Ce | 151 | 93 | 188.0042 | 1234.6180 | -84.77 % | 141640.9992 | +7444.21 ppm |
| ${}^{152}$Ce | 152 | 94 | 194.1142 | 1240.4720 | -84.35 % | 142574.4546 | +7393.10 ppm |
| ${}^{153}$Ce | 153 | 95 | 200.2164 | 1244.5020 | -83.91 % | 143507.9179 | +7329.80 ppm |
| ${}^{154}$Ce | 154 | 96 | 206.3107 | 1249.8640 | -83.49 % | 144441.3890 | +7277.07 ppm |
| ${}^{155}$Ce | 155 | 97 | 212.3973 | 1253.4850 | -83.06 % | 145374.8679 | +7212.88 ppm |
| ${}^{156}$Ce | 156 | 98 | 218.4763 | 1258.6080 | -82.64 % | 146308.3542 | +7159.81 ppm |
| ${}^{157}$Ce | 157 | 99 | 224.5479 | 1261.8090 | -82.20 % | 147241.8481 | +7094.19 ppm |
| ${}^{158}$Ce | 158 | 100 | 230.6121 | 1266.3700 | -81.79 % | 148175.3493 | +7039.72 ppm |
| ${}^{159}$Ce | 159 | 101 | 236.6691 | 1269.2970 | -81.35 % | 149108.8578 | +6973.67 ppm |

### Praseodymium (Z = 59)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{121}$Pr | 121 | 62 | -18.8356 | 971.9930 | -101.94 % | 113660.0940 | +8794.40 ppm |
| ${}^{122}$Pr | 122 | 63 | -12.3737 | 983.3200 | -101.26 % | 114593.1976 | +8765.13 ppm |
| ${}^{123}$Pr | 123 | 64 | -5.9254 | 996.7920 | -100.59 % | 115526.3146 | +8756.01 ppm |
| ${}^{124}$Pr | 124 | 65 | 0.5097 | 1007.8720 | -99.95 % | 116459.4450 | +8725.06 ppm |
| ${}^{125}$Pr | 125 | 66 | 6.9318 | 1020.8750 | -99.32 % | 117392.5883 | +8712.04 ppm |
| ${}^{126}$Pr | 126 | 67 | 13.3410 | 1031.1840 | -98.71 % | 118325.7445 | +8676.40 ppm |
| ${}^{127}$Pr | 127 | 68 | 19.7377 | 1043.4320 | -98.11 % | 119258.9132 | +8658.21 ppm |
| ${}^{128}$Pr | 128 | 69 | 26.1221 | 1053.3010 | -97.52 % | 120192.0943 | +8619.82 ppm |
| ${}^{129}$Pr | 129 | 70 | 32.4943 | 1064.8151 | -96.95 % | 121125.2875 | +8596.02 ppm |
| ${}^{130}$Pr | 130 | 71 | 38.8546 | 1074.2883 | -96.38 % | 122058.4926 | +8555.68 ppm |
| ${}^{131}$Pr | 131 | 72 | 45.2033 | 1085.4849 | -95.84 % | 122991.7094 | +8530.30 ppm |
| ${}^{132}$Pr | 132 | 73 | 51.5404 | 1094.4830 | -95.29 % | 123924.9377 | +8487.36 ppm |
| ${}^{133}$Pr | 133 | 74 | 57.8662 | 1105.2644 | -94.76 % | 124858.1773 | +8459.68 ppm |
| ${}^{134}$Pr | 134 | 75 | 64.1809 | 1113.9261 | -94.24 % | 125791.4281 | +8415.36 ppm |
| ${}^{135}$Pr | 135 | 76 | 70.4846 | 1124.4053 | -93.73 % | 126724.6897 | +8386.37 ppm |
| ${}^{136}$Pr | 136 | 77 | 76.7777 | 1132.8812 | -93.22 % | 127657.9621 | +8341.93 ppm |
| ${}^{137}$Pr | 137 | 78 | 83.0601 | 1142.8139 | -92.73 % | 128591.2451 | +8309.75 ppm |
| ${}^{138}$Pr | 138 | 79 | 89.3322 | 1150.8123 | -92.24 % | 129524.5384 | +8262.93 ppm |
| ${}^{139}$Pr | 139 | 80 | 95.5940 | 1160.5834 | -91.76 % | 130457.8420 | +8230.67 ppm |
| ${}^{140}$Pr | 140 | 81 | 101.8458 | 1168.5123 | -91.28 % | 131391.1556 | +8184.70 ppm |
| ${}^{141}$Pr | 141 | 82 | 108.0877 | 1177.9119 | -90.82 % | 132324.4791 | +8150.76 ppm |
| ${}^{142}$Pr | 142 | 83 | 114.3199 | 1183.7551 | -90.34 % | 133257.8124 | +8090.24 ppm |
| ${}^{143}$Pr | 143 | 84 | 120.5425 | 1191.1082 | -89.88 % | 134191.1552 | +8042.08 ppm |
| ${}^{144}$Pr | 144 | 85 | 126.7557 | 1196.8619 | -89.41 % | 135124.5074 | +7982.63 ppm |
| ${}^{145}$Pr | 145 | 86 | 132.9596 | 1203.8086 | -88.96 % | 136057.8690 | +7932.98 ppm |
| ${}^{146}$Pr | 146 | 87 | 139.1544 | 1208.9275 | -88.49 % | 136991.2396 | +7870.53 ppm |
| ${}^{147}$Pr | 147 | 88 | 145.3402 | 1215.7694 | -88.05 % | 137924.6193 | +7821.68 ppm |
| ${}^{148}$Pr | 148 | 89 | 151.5171 | 1220.9321 | -87.59 % | 138858.0078 | +7761.28 ppm |
| ${}^{149}$Pr | 149 | 90 | 157.6853 | 1227.5073 | -87.15 % | 139791.4050 | +7712.01 ppm |
| ${}^{150}$Pr | 150 | 91 | 163.8449 | 1232.8397 | -86.71 % | 140724.8108 | +7654.50 ppm |
| ${}^{151}$Pr | 151 | 92 | 169.9961 | 1239.3902 | -86.28 % | 141658.2250 | +7606.54 ppm |
| ${}^{152}$Pr | 152 | 93 | 176.1390 | 1244.4399 | -85.85 % | 142591.6476 | +7548.59 ppm |
| ${}^{153}$Pr | 153 | 94 | 182.2736 | 1250.3217 | -85.42 % | 143525.0783 | +7497.34 ppm |
| ${}^{154}$Pr | 154 | 95 | 188.4002 | 1254.6841 | -84.98 % | 144458.5172 | +7436.14 ppm |
| ${}^{155}$Pr | 155 | 96 | 194.5188 | 1260.3112 | -84.57 % | 145391.9640 | +7384.62 ppm |
| ${}^{156}$Pr | 156 | 97 | 200.6296 | 1264.4165 | -84.13 % | 146325.4186 | +7323.25 ppm |
| ${}^{157}$Pr | 157 | 98 | 206.7326 | 1269.4733 | -83.72 % | 147258.8810 | +7269.29 ppm |
| ${}^{158}$Pr | 158 | 99 | 212.8280 | 1273.3220 | -83.29 % | 148192.3510 | +7207.36 ppm |
| ${}^{159}$Pr | 159 | 100 | 218.9159 | 1277.8830 | -82.87 % | 149125.8285 | +7152.42 ppm |
| ${}^{160}$Pr | 160 | 101 | 224.9964 | 1281.4400 | -82.44 % | 150059.3135 | +7090.18 ppm |
| ${}^{161}$Pr | 161 | 102 | 231.0697 | 1285.7460 | -82.03 % | 150992.8057 | +7034.54 ppm |

### Neodymium (Z = 60)

_40 of 40 isotopes with a framework prediction; 40 of 40 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{124}$Nd | 124 | 64 | -18.7921 | 998.6960 | -101.88 % | 116477.9644 | +8812.76 ppm |
| ${}^{125}$Nd | 125 | 65 | -12.3270 | 1010.0000 | -101.22 % | 117411.0647 | +8784.11 ppm |
| ${}^{126}$Nd | 126 | 66 | -5.8751 | 1023.3720 | -100.57 % | 118344.1783 | +8773.84 ppm |
| ${}^{127}$Nd | 127 | 67 | 0.5638 | 1034.0340 | -99.95 % | 119277.3048 | +8740.11 ppm |
| ${}^{128}$Nd | 128 | 68 | 6.9899 | 1046.6560 | -99.33 % | 120210.4441 | +8724.70 ppm |
| ${}^{129}$Nd | 129 | 69 | 13.4035 | 1056.6390 | -98.73 % | 121143.5960 | +8686.33 ppm |
| ${}^{130}$Nd | 130 | 70 | 19.8048 | 1068.9268 | -98.15 % | 122076.7601 | +8668.46 ppm |
| ${}^{131}$Nd | 131 | 71 | 26.1939 | 1078.1699 | -97.57 % | 123009.9364 | +8625.73 ppm |
| ${}^{132}$Nd | 132 | 72 | 32.5711 | 1089.8990 | -97.01 % | 123943.1246 | +8604.16 ppm |
| ${}^{133}$Nd | 133 | 73 | 38.9367 | 1098.8769 | -96.46 % | 124876.3245 | +8560.59 ppm |
| ${}^{134}$Nd | 134 | 74 | 45.2907 | 1110.2622 | -95.92 % | 125809.5359 | +8537.23 ppm |
| ${}^{135}$Nd | 135 | 75 | 51.6334 | 1118.9007 | -95.39 % | 126742.7586 | +8492.25 ppm |
| ${}^{136}$Nd | 136 | 76 | 57.9651 | 1129.9577 | -94.87 % | 127675.9924 | +8467.30 ppm |
| ${}^{137}$Nd | 137 | 77 | 64.2858 | 1138.4137 | -94.35 % | 128609.2371 | +8422.22 ppm |
| ${}^{138}$Nd | 138 | 78 | 70.5957 | 1148.9183 | -93.86 % | 129542.4926 | +8393.96 ppm |
| ${}^{139}$Nd | 139 | 79 | 76.8951 | 1156.9893 | -93.35 % | 130475.7586 | +8347.23 ppm |
| ${}^{140}$Nd | 140 | 80 | 83.1840 | 1167.3010 | -92.87 % | 131409.0351 | +8318.58 ppm |
| ${}^{141}$Nd | 141 | 81 | 89.4628 | 1175.3065 | -92.39 % | 132342.3218 | +8272.69 ppm |
| ${}^{142}$Nd | 142 | 82 | 95.7314 | 1185.1364 | -91.92 % | 133275.6185 | +8241.45 ppm |
| ${}^{143}$Nd | 143 | 83 | 101.9902 | 1191.2600 | -91.44 % | 134208.9252 | +8182.64 ppm |
| ${}^{144}$Nd | 144 | 84 | 108.2392 | 1199.0770 | -90.97 % | 135142.2416 | +8137.47 ppm |
| ${}^{145}$Nd | 145 | 85 | 114.4786 | 1204.8323 | -90.50 % | 136075.5677 | +8077.59 ppm |
| ${}^{146}$Nd | 146 | 86 | 120.7085 | 1212.3975 | -90.04 % | 137008.9031 | +8032.02 ppm |
| ${}^{147}$Nd | 147 | 87 | 126.9292 | 1217.6897 | -89.58 % | 137942.2479 | +7970.40 ppm |
| ${}^{148}$Nd | 148 | 88 | 133.1407 | 1225.0223 | -89.13 % | 138875.6018 | +7924.61 ppm |
| ${}^{149}$Nd | 149 | 89 | 139.3432 | 1230.0611 | -88.67 % | 139808.9647 | +7862.84 ppm |
| ${}^{150}$Nd | 150 | 90 | 145.5368 | 1237.4368 | -88.24 % | 140742.3366 | +7818.82 ppm |
| ${}^{151}$Nd | 151 | 91 | 151.7216 | 1242.7714 | -87.79 % | 141675.7171 | +7760.81 ppm |
| ${}^{152}$Nd | 152 | 92 | 157.8979 | 1250.0492 | -87.37 % | 142609.1063 | +7717.47 ppm |
| ${}^{153}$Nd | 153 | 93 | 164.0656 | 1255.3012 | -86.93 % | 143542.5040 | +7660.42 ppm |
| ${}^{154}$Nd | 154 | 94 | 170.2250 | 1261.6218 | -86.51 % | 144475.9100 | +7611.68 ppm |
| ${}^{155}$Nd | 155 | 95 | 176.3762 | 1266.3973 | -86.07 % | 145409.3243 | +7552.85 ppm |
| ${}^{156}$Nd | 156 | 96 | 182.5192 | 1272.3869 | -85.66 % | 146342.7467 | +7503.25 ppm |
| ${}^{157}$Nd | 157 | 97 | 188.6543 | 1276.7502 | -85.22 % | 147276.1770 | +7443.13 ppm |
| ${}^{158}$Nd | 158 | 98 | 194.7814 | 1282.1626 | -84.81 % | 148209.6153 | +7391.01 ppm |
| ${}^{159}$Nd | 159 | 99 | 200.9008 | 1286.1228 | -84.38 % | 149143.0613 | +7329.72 ppm |
| ${}^{160}$Nd | 160 | 100 | 207.0126 | 1291.1946 | -83.97 % | 150076.5150 | +7276.77 ppm |
| ${}^{161}$Nd | 161 | 101 | 213.1168 | 1294.7620 | -83.54 % | 151009.9762 | +7214.49 ppm |
| ${}^{162}$Nd | 162 | 102 | 219.2135 | 1299.5640 | -83.13 % | 151943.4449 | +7161.53 ppm |
| ${}^{163}$Nd | 163 | 103 | 225.3029 | 1302.6960 | -82.70 % | 152876.9209 | +7097.93 ppm |

### Promethium (Z = 61)

_40 of 40 isotopes with a framework prediction; 40 of 40 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{126}$Pm | 126 | 65 | -25.3736 | 1009.0080 | -102.51 % | 118362.8944 | +8816.16 ppm |
| ${}^{127}$Pm | 127 | 66 | -18.8918 | 1022.6040 | -101.85 % | 119295.9781 | +8807.59 ppm |
| ${}^{128}$Pm | 128 | 67 | -12.4232 | 1033.6000 | -101.20 % | 120229.0749 | +8776.83 ppm |
| ${}^{129}$Pm | 129 | 68 | -5.9676 | 1046.7060 | -100.57 % | 121162.1847 | +8763.88 ppm |
| ${}^{130}$Pm | 130 | 69 | 0.4753 | 1057.0300 | -99.96 % | 122095.3073 | +8728.97 ppm |
| ${}^{131}$Pm | 131 | 70 | 6.9057 | 1069.3530 | -99.35 % | 123028.4423 | +8711.32 ppm |
| ${}^{132}$Pm | 132 | 71 | 13.3237 | 1079.3640 | -98.77 % | 123961.5897 | +8673.99 ppm |
| ${}^{133}$Pm | 133 | 72 | 19.7296 | 1091.1698 | -98.19 % | 124894.7492 | +8652.98 ppm |
| ${}^{134}$Pm | 134 | 73 | 26.1237 | 1100.5974 | -97.63 % | 125827.9205 | +8612.78 ppm |
| ${}^{135}$Pm | 135 | 74 | 32.5061 | 1111.9671 | -97.08 % | 126761.1036 | +8588.86 ppm |
| ${}^{136}$Pm | 136 | 75 | 38.8769 | 1121.1460 | -96.53 % | 127694.2982 | +8547.92 ppm |
| ${}^{137}$Pm | 137 | 76 | 45.2365 | 1132.1203 | -96.00 % | 128627.5040 | +8521.87 ppm |
| ${}^{138}$Pm | 138 | 77 | 51.5850 | 1141.0331 | -95.48 % | 129560.7210 | +8480.10 ppm |
| ${}^{139}$Pm | 139 | 78 | 57.9225 | 1151.6911 | -94.97 % | 130493.9489 | +8452.61 ppm |
| ${}^{140}$Pm | 140 | 79 | 64.2492 | 1160.4734 | -94.46 % | 131427.1875 | +8411.09 ppm |
| ${}^{141}$Pm | 141 | 80 | 70.5654 | 1170.8556 | -93.97 % | 132360.4368 | +8382.52 ppm |
| ${}^{142}$Pm | 142 | 81 | 76.8712 | 1179.5455 | -93.48 % | 133293.6964 | +8341.53 ppm |
| ${}^{143}$Pm | 143 | 82 | 83.1667 | 1189.4360 | -93.01 % | 134226.9663 | +8310.28 ppm |
| ${}^{144}$Pm | 144 | 83 | 89.4522 | 1195.9628 | -92.52 % | 135160.2463 | +8254.24 ppm |
| ${}^{145}$Pm | 145 | 84 | 95.7277 | 1203.8855 | -92.05 % | 136093.5362 | +8209.47 ppm |
| ${}^{146}$Pm | 146 | 85 | 101.9934 | 1210.1436 | -91.57 % | 137026.8359 | +8153.04 ppm |
| ${}^{147}$Pm | 147 | 86 | 108.2495 | 1217.8026 | -91.11 % | 137960.1452 | +8107.78 ppm |
| ${}^{148}$Pm | 148 | 87 | 114.4962 | 1223.6978 | -90.64 % | 138893.4640 | +8050.28 ppm |
| ${}^{149}$Pm | 149 | 88 | 120.7335 | 1230.9676 | -90.19 % | 139826.7921 | +8003.62 ppm |
| ${}^{150}$Pm | 150 | 89 | 126.9617 | 1236.5719 | -89.73 % | 140760.1293 | +7945.63 ppm |
| ${}^{151}$Pm | 151 | 90 | 133.1808 | 1244.4321 | -89.30 % | 141693.4757 | +7904.64 ppm |
| ${}^{152}$Pm | 152 | 91 | 139.3910 | 1250.3717 | -88.85 % | 142626.8309 | +7850.58 ppm |
| ${}^{153}$Pm | 153 | 92 | 145.5924 | 1257.8365 | -88.43 % | 143560.1949 | +7808.08 ppm |
| ${}^{154}$Pm | 154 | 93 | 151.7852 | 1263.5264 | -87.99 % | 144493.5675 | +7753.72 ppm |
| ${}^{155}$Pm | 155 | 94 | 157.9694 | 1270.2711 | -87.56 % | 145426.9487 | +7707.48 ppm |
| ${}^{156}$Pm | 156 | 95 | 164.1453 | 1275.5693 | -87.13 % | 146360.3382 | +7651.86 ppm |
| ${}^{157}$Pm | 157 | 96 | 170.3129 | 1281.7709 | -86.71 % | 147293.7361 | +7603.24 ppm |
| ${}^{158}$Pm | 158 | 97 | 176.4724 | 1286.6512 | -86.28 % | 148227.1420 | +7546.24 ppm |
| ${}^{159}$Pm | 159 | 98 | 182.6238 | 1292.1708 | -85.87 % | 149160.5561 | +7494.36 ppm |
| ${}^{160}$Pm | 160 | 99 | 188.7673 | 1296.5824 | -85.44 % | 150093.9780 | +7435.70 ppm |
| ${}^{161}$Pm | 161 | 100 | 194.9029 | 1301.8456 | -85.03 % | 151027.4077 | +7383.54 ppm |
| ${}^{162}$Pm | 162 | 101 | 201.0309 | 1305.8820 | -84.61 % | 151960.8452 | +7323.81 ppm |
| ${}^{163}$Pm | 163 | 102 | 207.1513 | 1310.8460 | -84.20 % | 152894.2902 | +7271.27 ppm |
| ${}^{164}$Pm | 164 | 103 | 213.2643 | 1314.2960 | -83.77 % | 153827.7427 | +7209.41 ppm |
| ${}^{165}$Pm | 165 | 104 | 219.3698 | 1318.6800 | -83.36 % | 154761.2026 | +7154.32 ppm |

### Samarium (Z = 62)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{128}$Sm | 128 | 66 | -32.1173 | 1023.7440 | -103.14 % | 120247.9867 | +8858.73 ppm |
| ${}^{129}$Sm | 129 | 67 | -25.6189 | 1034.9670 | -102.48 % | 121181.0537 | +8829.84 ppm |
| ${}^{130}$Sm | 130 | 68 | -19.1337 | 1048.4500 | -101.82 % | 122114.1339 | +8819.75 ppm |
| ${}^{131}$Sm | 131 | 69 | -12.6615 | 1059.1350 | -101.20 % | 123047.2271 | +8786.85 ppm |
| ${}^{132}$Sm | 132 | 70 | -6.2019 | 1072.1040 | -100.58 % | 123980.3330 | +8773.25 ppm |
| ${}^{133}$Sm | 133 | 71 | 0.2451 | 1082.2210 | -99.98 % | 124913.4514 | +8737.41 ppm |
| ${}^{134}$Sm | 134 | 72 | 6.6798 | 1094.3780 | -99.39 % | 125846.5821 | +8718.81 ppm |
| ${}^{135}$Sm | 135 | 73 | 13.1025 | 1103.9796 | -98.81 % | 126779.7248 | +8679.20 ppm |
| ${}^{136}$Sm | 136 | 74 | 19.5133 | 1116.0046 | -98.25 % | 127712.8795 | +8659.96 ppm |
| ${}^{137}$Sm | 137 | 75 | 25.9124 | 1125.2567 | -97.70 % | 128646.0458 | +8619.16 ppm |
| ${}^{138}$Sm | 138 | 76 | 32.3000 | 1136.8341 | -97.16 % | 129579.2236 | +8597.30 ppm |
| ${}^{139}$Sm | 139 | 77 | 38.6763 | 1145.7879 | -96.62 % | 130512.4127 | +8555.39 ppm |
| ${}^{140}$Sm | 140 | 78 | 45.0415 | 1156.9350 | -96.11 % | 131445.6130 | +8531.13 ppm |
| ${}^{141}$Sm | 141 | 79 | 51.3957 | 1165.4843 | -95.59 % | 132378.8241 | +8487.35 ppm |
| ${}^{142}$Sm | 142 | 80 | 57.7392 | 1176.6036 | -95.09 % | 133312.0461 | +8463.87 ppm |
| ${}^{143}$Sm | 143 | 81 | 64.0721 | 1185.2101 | -94.59 % | 134245.2786 | +8421.75 ppm |
| ${}^{144}$Sm | 144 | 82 | 70.3946 | 1195.7299 | -94.11 % | 135178.5215 | +8394.70 ppm |
| ${}^{145}$Sm | 145 | 83 | 76.7069 | 1202.4870 | -93.62 % | 136111.7747 | +8339.98 ppm |
| ${}^{146}$Sm | 146 | 84 | 83.0090 | 1210.9033 | -93.14 % | 137045.0380 | +8298.40 ppm |
| ${}^{147}$Sm | 147 | 85 | 89.3012 | 1217.2443 | -92.66 % | 137978.3112 | +8242.17 ppm |
| ${}^{148}$Sm | 148 | 86 | 95.5836 | 1225.3856 | -92.20 % | 138911.5943 | +8199.94 ppm |
| ${}^{149}$Sm | 149 | 87 | 101.8563 | 1231.2568 | -91.73 % | 139844.8869 | +8141.85 ppm |
| ${}^{150}$Sm | 150 | 88 | 108.1196 | 1239.2435 | -91.28 % | 140778.1891 | +8099.88 ppm |
| ${}^{151}$Sm | 151 | 89 | 114.3735 | 1244.8400 | -90.81 % | 141711.5006 | +8041.39 ppm |
| ${}^{152}$Sm | 152 | 90 | 120.6183 | 1253.0978 | -90.37 % | 142644.8213 | +8002.70 ppm |
| ${}^{153}$Sm | 153 | 91 | 126.8539 | 1258.9662 | -89.92 % | 143578.1510 | +7947.66 ppm |
| ${}^{154}$Sm | 154 | 92 | 133.0806 | 1266.9330 | -89.50 % | 144511.4897 | +7908.16 ppm |
| ${}^{155}$Sm | 155 | 93 | 139.2986 | 1272.7400 | -89.06 % | 145444.8372 | +7854.14 ppm |
| ${}^{156}$Sm | 156 | 94 | 145.5078 | 1279.9808 | -88.63 % | 146378.1934 | +7810.83 ppm |
| ${}^{157}$Sm | 157 | 95 | 151.7085 | 1285.3691 | -88.20 % | 147311.5582 | +7755.36 ppm |
| ${}^{158}$Sm | 158 | 96 | 157.9008 | 1292.0146 | -87.78 % | 148244.9313 | +7709.25 ppm |
| ${}^{159}$Sm | 159 | 97 | 164.0847 | 1297.0419 | -87.35 % | 149178.3128 | +7652.78 ppm |
| ${}^{160}$Sm | 160 | 98 | 170.2605 | 1303.1385 | -86.93 % | 150111.7024 | +7604.30 ppm |
| ${}^{161}$Sm | 161 | 99 | 176.4282 | 1307.6487 | -86.51 % | 151045.1001 | +7545.81 ppm |
| ${}^{162}$Sm | 162 | 100 | 182.5880 | 1313.4271 | -86.10 % | 151978.5058 | +7496.57 ppm |
| ${}^{163}$Sm | 163 | 101 | 188.7399 | 1317.7189 | -85.68 % | 152911.9193 | +7438.12 ppm |
| ${}^{164}$Sm | 164 | 102 | 194.8841 | 1323.1160 | -85.27 % | 153845.3405 | +7387.73 ppm |
| ${}^{165}$Sm | 165 | 103 | 201.0206 | 1326.7650 | -84.85 % | 154778.7694 | +7326.59 ppm |
| ${}^{166}$Sm | 166 | 104 | 207.1497 | 1331.8180 | -84.45 % | 155712.2058 | +7275.07 ppm |
| ${}^{167}$Sm | 167 | 105 | 213.2713 | 1334.6640 | -84.02 % | 156645.6496 | +7210.87 ppm |
| ${}^{168}$Sm | 168 | 106 | 219.3856 | 1339.1280 | -83.62 % | 157579.1007 | +7156.69 ppm |

### Europium (Z = 63)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{130}$Eu | 130 | 67 | -39.0223 | 1033.5000 | -103.78 % | 122133.2402 | +8859.36 ppm |
| ${}^{131}$Eu | 131 | 68 | -32.5075 | 1047.4760 | -103.10 % | 123066.2908 | +8853.68 ppm |
| ${}^{132}$Eu | 132 | 69 | -26.0058 | 1058.3760 | -102.46 % | 123999.3545 | +8821.81 ppm |
| ${}^{133}$Eu | 133 | 70 | -19.5170 | 1071.4480 | -101.82 % | 124932.4311 | +8809.26 ppm |
| ${}^{134}$Eu | 134 | 71 | -13.0409 | 1082.0500 | -101.21 % | 125865.5205 | +8777.01 ppm |
| ${}^{135}$Eu | 135 | 72 | -6.5773 | 1094.4450 | -100.60 % | 126798.6223 | +8759.65 ppm |
| ${}^{136}$Eu | 136 | 73 | -0.1259 | 1104.5920 | -100.01 % | 127731.7363 | +8724.70 ppm |
| ${}^{137}$Eu | 137 | 74 | 6.3134 | 1116.6286 | -99.43 % | 128664.8625 | +8704.64 ppm |
| ${}^{138}$Eu | 138 | 75 | 12.7408 | 1126.3037 | -98.87 % | 129598.0005 | +8666.92 ppm |
| ${}^{139}$Eu | 139 | 76 | 19.1565 | 1138.0234 | -98.32 % | 130531.1502 | +8645.76 ppm |
| ${}^{140}$Eu | 140 | 77 | 25.5608 | 1147.6826 | -97.77 % | 131464.3114 | +8609.05 ppm |
| ${}^{141}$Eu | 141 | 78 | 31.9537 | 1158.6936 | -97.24 % | 132397.4838 | +8583.34 ppm |
| ${}^{142}$Eu | 142 | 79 | 38.3356 | 1168.1482 | -96.72 % | 133330.6674 | +8546.19 ppm |
| ${}^{143}$Eu | 143 | 80 | 44.7065 | 1179.1519 | -96.21 % | 134263.8619 | +8521.38 ppm |
| ${}^{144}$Eu | 144 | 81 | 51.0666 | 1188.6011 | -95.70 % | 135197.0672 | +8485.30 ppm |
| ${}^{145}$Eu | 145 | 82 | 57.4161 | 1199.0448 | -95.21 % | 136130.2831 | +8457.23 ppm |
| ${}^{146}$Eu | 146 | 83 | 63.7553 | 1206.2422 | -94.71 % | 137063.5094 | +8405.53 ppm |
| ${}^{147}$Eu | 147 | 84 | 70.0841 | 1214.7405 | -94.23 % | 137996.7460 | +8364.19 ppm |
| ${}^{148}$Eu | 148 | 85 | 76.4028 | 1221.5647 | -93.75 % | 138929.9927 | +8311.24 ppm |
| ${}^{149}$Eu | 149 | 86 | 82.7116 | 1229.7798 | -93.27 % | 139863.2493 | +8269.18 ppm |
| ${}^{150}$Eu | 150 | 87 | 89.0106 | 1236.2022 | -92.80 % | 140796.5157 | +8214.81 ppm |
| ${}^{151}$Eu | 151 | 88 | 95.2999 | 1244.1343 | -92.34 % | 141729.7918 | +8172.05 ppm |
| ${}^{152}$Eu | 152 | 89 | 101.5797 | 1250.4410 | -91.88 % | 142663.0775 | +8118.35 ppm |
| ${}^{153}$Eu | 153 | 90 | 107.8502 | 1258.9913 | -91.43 % | 143596.3724 | +8081.30 ppm |
| ${}^{154}$Eu | 154 | 91 | 114.1114 | 1265.4335 | -90.98 % | 144529.6766 | +8029.96 ppm |
| ${}^{155}$Eu | 155 | 92 | 120.3635 | 1273.5848 | -90.55 % | 145462.9899 | +7991.30 ppm |
| ${}^{156}$Eu | 156 | 93 | 126.6067 | 1279.9206 | -90.11 % | 146396.3122 | +7940.59 ppm |
| ${}^{157}$Eu | 157 | 94 | 132.8410 | 1287.3682 | -89.68 % | 147329.6433 | +7898.25 ppm |
| ${}^{158}$Eu | 158 | 95 | 139.0667 | 1293.2509 | -89.25 % | 148262.9831 | +7845.79 ppm |
| ${}^{159}$Eu | 159 | 96 | 145.2837 | 1300.0951 | -88.83 % | 149196.3314 | +7800.60 ppm |
| ${}^{160}$Eu | 160 | 97 | 151.4923 | 1305.6165 | -88.40 % | 150129.6883 | +7747.08 ppm |
| ${}^{161}$Eu | 161 | 98 | 157.6926 | 1311.9859 | -87.98 % | 151063.0534 | +7699.98 ppm |
| ${}^{162}$Eu | 162 | 99 | 163.8846 | 1316.9886 | -87.56 % | 151996.4268 | +7644.39 ppm |
| ${}^{163}$Eu | 163 | 100 | 170.0686 | 1322.9108 | -87.14 % | 152929.8083 | +7595.64 ppm |
| ${}^{164}$Eu | 164 | 101 | 176.2445 | 1327.6405 | -86.72 % | 153863.1977 | +7539.67 ppm |
| ${}^{165}$Eu | 165 | 102 | 182.4126 | 1333.2087 | -86.32 % | 154796.5951 | +7489.94 ppm |
| ${}^{166}$Eu | 166 | 103 | 188.5729 | 1337.2960 | -85.90 % | 155730.0002 | +7431.22 ppm |
| ${}^{167}$Eu | 167 | 104 | 194.7256 | 1342.3460 | -85.49 % | 156663.4129 | +7379.75 ppm |
| ${}^{168}$Eu | 168 | 105 | 200.8707 | 1346.0160 | -85.08 % | 157596.8333 | +7319.02 ppm |
| ${}^{169}$Eu | 169 | 106 | 207.0083 | 1350.4790 | -84.67 % | 158530.2611 | +7265.02 ppm |
| ${}^{170}$Eu | 170 | 107 | 213.1386 | 1353.7100 | -84.26 % | 159463.6962 | +7203.99 ppm |

### Gadolinium (Z = 64)

_40 of 40 isotopes with a framework prediction; 40 of 40 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{133}$Gd | 133 | 69 | -39.5566 | 1059.4780 | -103.73 % | 124951.6884 | +8873.71 ppm |
| ${}^{134}$Gd | 134 | 70 | -33.0384 | 1073.0720 | -103.08 % | 125884.7357 | +8864.14 ppm |
| ${}^{135}$Gd | 135 | 71 | -26.5332 | 1083.7800 | -102.45 % | 126817.7959 | +8832.74 ppm |
| ${}^{136}$Gd | 136 | 72 | -20.0406 | 1096.7040 | -101.83 % | 127750.8687 | +8818.80 ppm |
| ${}^{137}$Gd | 137 | 73 | -13.5605 | 1106.9600 | -101.23 % | 128683.9541 | +8783.67 ppm |
| ${}^{138}$Gd | 138 | 74 | -7.0927 | 1119.4560 | -100.63 % | 129617.0516 | +8767.38 ppm |
| ${}^{139}$Gd | 139 | 75 | -0.6369 | 1129.5140 | -100.06 % | 130550.1612 | +8732.13 ppm |
| ${}^{140}$Gd | 140 | 76 | 5.8071 | 1141.6966 | -99.49 % | 131483.2827 | +8714.33 ppm |
| ${}^{141}$Gd | 141 | 77 | 12.2394 | 1151.2099 | -98.94 % | 132416.4159 | +8676.06 ppm |
| ${}^{142}$Gd | 142 | 78 | 18.6602 | 1163.0165 | -98.40 % | 133349.5605 | +8655.92 ppm |
| ${}^{143}$Gd | 143 | 79 | 25.0697 | 1172.3596 | -97.86 % | 134282.7164 | +8617.47 ppm |
| ${}^{144}$Gd | 144 | 80 | 31.4681 | 1183.9591 | -97.34 % | 135215.8834 | +8596.62 ppm |
| ${}^{145}$Gd | 145 | 81 | 37.8555 | 1193.1975 | -96.83 % | 136149.0614 | +8558.49 ppm |
| ${}^{146}$Gd | 146 | 82 | 44.2322 | 1204.4281 | -96.33 % | 137082.2501 | +8535.75 ppm |
| ${}^{147}$Gd | 147 | 83 | 50.5983 | 1211.7705 | -95.82 % | 138015.4494 | +8484.74 ppm |
| ${}^{148}$Gd | 148 | 84 | 56.9540 | 1220.7543 | -95.33 % | 138948.6592 | +8446.51 ppm |
| ${}^{149}$Gd | 149 | 85 | 63.2994 | 1227.6834 | -94.84 % | 139881.8792 | +8393.93 ppm |
| ${}^{150}$Gd | 150 | 86 | 69.6346 | 1236.3915 | -94.37 % | 140815.1094 | +8354.97 ppm |
| ${}^{151}$Gd | 151 | 87 | 75.9599 | 1242.8877 | -93.89 % | 141748.3495 | +8300.73 ppm |
| ${}^{152}$Gd | 152 | 88 | 82.2754 | 1251.4774 | -93.43 % | 142681.5995 | +8262.19 ppm |
| ${}^{153}$Gd | 153 | 89 | 88.5812 | 1257.7244 | -92.96 % | 143614.8591 | +8207.65 ppm |
| ${}^{154}$Gd | 154 | 90 | 94.8775 | 1266.6191 | -92.51 % | 144548.1282 | +8172.49 ppm |
| ${}^{155}$Gd | 155 | 91 | 101.1644 | 1273.0544 | -92.05 % | 145481.4068 | +8120.68 ppm |
| ${}^{156}$Gd | 156 | 92 | 107.4420 | 1281.5907 | -91.62 % | 146414.6946 | +8084.17 ppm |
| ${}^{157}$Gd | 157 | 93 | 113.7105 | 1287.9506 | -91.17 % | 147347.9915 | +8033.19 ppm |
| ${}^{158}$Gd | 158 | 94 | 119.9700 | 1295.8880 | -90.74 % | 148281.2974 | +7993.72 ppm |
| ${}^{159}$Gd | 159 | 95 | 126.2207 | 1301.8312 | -90.30 % | 149214.6121 | +7941.23 ppm |
| ${}^{160}$Gd | 160 | 96 | 132.4627 | 1309.2827 | -89.88 % | 150147.9356 | +7899.66 ppm |
| ${}^{161}$Gd | 161 | 97 | 138.6960 | 1314.9181 | -89.45 % | 151081.2676 | +7846.45 ppm |
| ${}^{162}$Gd | 162 | 98 | 144.9209 | 1321.7640 | -89.04 % | 152014.6082 | +7802.05 ppm |
| ${}^{163}$Gd | 163 | 99 | 151.1374 | 1326.9432 | -88.61 % | 152947.9571 | +7747.18 ppm |
| ${}^{164}$Gd | 164 | 100 | 157.3456 | 1333.3196 | -88.20 % | 153881.3143 | +7700.94 ppm |
| ${}^{165}$Gd | 165 | 101 | 163.5458 | 1338.2231 | -87.78 % | 154814.6796 | +7645.65 ppm |
| ${}^{166}$Gd | 166 | 102 | 169.7379 | 1344.1395 | -87.37 % | 155748.0529 | +7597.69 ppm |
| ${}^{167}$Gd | 167 | 103 | 175.9221 | 1348.6156 | -86.96 % | 156681.4341 | +7541.02 ppm |
| ${}^{168}$Gd | 168 | 104 | 182.0984 | 1354.0800 | -86.55 % | 157614.8232 | +7491.32 ppm |
| ${}^{169}$Gd | 169 | 105 | 188.2671 | 1357.9150 | -86.14 % | 158548.2199 | +7431.80 ppm |
| ${}^{170}$Gd | 170 | 106 | 194.4282 | 1362.8900 | -85.73 % | 159481.6242 | +7380.79 ppm |
| ${}^{171}$Gd | 171 | 107 | 200.5818 | 1366.2900 | -85.32 % | 160415.0361 | +7320.31 ppm |
| ${}^{172}$Gd | 172 | 108 | 206.7280 | 1371.1840 | -84.92 % | 161348.4553 | +7269.39 ppm |

### Terbium (Z = 65)

_40 of 40 isotopes with a framework prediction; 40 of 40 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{135}$Tb | 135 | 70 | -46.7653 | 1071.7650 | -104.36 % | 126837.2457 | +8897.60 ppm |
| ${}^{136}$Tb | 136 | 71 | -40.2309 | 1082.6960 | -103.72 % | 127770.2767 | +8866.97 ppm |
| ${}^{137}$Tb | 137 | 72 | -33.7093 | 1095.8630 | -103.08 % | 128703.3205 | +8854.45 ppm |
| ${}^{138}$Tb | 138 | 73 | -27.2004 | 1106.6220 | -102.46 % | 129636.3770 | +8823.10 ppm |
| ${}^{139}$Tb | 139 | 74 | -20.7039 | 1119.2280 | -101.85 % | 130569.4459 | +8807.08 ppm |
| ${}^{140}$Tb | 140 | 75 | -14.2196 | 1129.6142 | -101.26 % | 131502.5270 | +8774.52 ppm |
| ${}^{141}$Tb | 141 | 76 | -7.7473 | 1141.7441 | -100.68 % | 132435.6202 | +8755.63 ppm |
| ${}^{142}$Tb | 142 | 77 | -1.2870 | 1151.8341 | -100.11 % | 133368.7252 | +8721.53 ppm |
| ${}^{143}$Tb | 143 | 78 | 5.1618 | 1163.7651 | -99.56 % | 134301.8419 | +8701.94 ppm |
| ${}^{144}$Tb | 144 | 79 | 11.5991 | 1173.7854 | -99.01 % | 135234.9701 | +8668.33 ppm |
| ${}^{145}$Tb | 145 | 80 | 18.0251 | 1185.8883 | -98.48 % | 136168.1095 | +8650.83 ppm |
| ${}^{146}$Tb | 146 | 81 | 24.4399 | 1195.3235 | -97.96 % | 137101.2601 | +8613.86 ppm |
| ${}^{147}$Tb | 147 | 82 | 30.8439 | 1206.3739 | -97.44 % | 138034.4215 | +8589.37 ppm |
| ${}^{148}$Tb | 148 | 83 | 37.2370 | 1214.2395 | -96.93 % | 138967.5938 | +8541.97 ppm |
| ${}^{149}$Tb | 149 | 84 | 43.6196 | 1223.2625 | -96.43 % | 139900.7767 | +8503.71 ppm |
| ${}^{150}$Tb | 150 | 85 | 49.9917 | 1230.9509 | -95.94 % | 140833.9700 | +8456.39 ppm |
| ${}^{151}$Tb | 151 | 86 | 56.3535 | 1239.5400 | -95.45 % | 141767.1736 | +8416.23 ppm |
| ${}^{152}$Tb | 152 | 87 | 62.7052 | 1246.7051 | -94.97 % | 142700.3873 | +8366.53 ppm |
| ${}^{153}$Tb | 153 | 88 | 69.0470 | 1255.3727 | -94.50 % | 143633.6110 | +8328.18 ppm |
| ${}^{154}$Tb | 154 | 89 | 75.3788 | 1262.2871 | -94.03 % | 144566.8445 | +8278.07 ppm |
| ${}^{155}$Tb | 155 | 90 | 81.7010 | 1271.4522 | -93.57 % | 145500.0877 | +8244.40 ppm |
| ${}^{156}$Tb | 156 | 91 | 88.0137 | 1278.3641 | -93.12 % | 146433.3405 | +8195.59 ppm |
| ${}^{157}$Tb | 157 | 92 | 94.3169 | 1287.1082 | -92.67 % | 147366.6027 | +8160.10 ppm |
| ${}^{158}$Tb | 158 | 93 | 100.6109 | 1293.8866 | -92.22 % | 148299.8741 | +8111.65 ppm |
| ${}^{159}$Tb | 159 | 94 | 106.8958 | 1302.0196 | -91.79 % | 149233.1547 | +8073.09 ppm |
| ${}^{160}$Tb | 160 | 95 | 113.1716 | 1308.3948 | -91.35 % | 150166.4443 | +8023.19 ppm |
| ${}^{161}$Tb | 161 | 96 | 119.4386 | 1316.0914 | -90.92 % | 151099.7428 | +7982.85 ppm |
| ${}^{162}$Tb | 162 | 97 | 125.6968 | 1322.5805 | -90.50 % | 152033.0500 | +7935.00 ppm |
| ${}^{163}$Tb | 163 | 98 | 131.9463 | 1329.3680 | -90.07 % | 152966.3658 | +7889.77 ppm |
| ${}^{164}$Tb | 164 | 99 | 138.1874 | 1334.9486 | -89.65 % | 153899.6902 | +7837.19 ppm |
| ${}^{165}$Tb | 165 | 100 | 144.4201 | 1341.5038 | -89.23 % | 154833.0230 | +7791.70 ppm |
| ${}^{166}$Tb | 166 | 101 | 150.6445 | 1346.7950 | -88.81 % | 155766.3640 | +7738.56 ppm |
| ${}^{167}$Tb | 167 | 102 | 156.8607 | 1352.9406 | -88.41 % | 156699.7132 | +7691.66 ppm |
| ${}^{168}$Tb | 168 | 103 | 163.0689 | 1357.9101 | -87.99 % | 157633.0704 | +7637.79 ppm |
| ${}^{169}$Tb | 169 | 104 | 169.2691 | 1363.6610 | -87.59 % | 158566.4356 | +7589.74 ppm |
| ${}^{170}$Tb | 170 | 105 | 175.4615 | 1367.9900 | -87.17 % | 159499.8086 | +7532.95 ppm |
| ${}^{171}$Tb | 171 | 106 | 181.6462 | 1373.1300 | -86.77 % | 160433.1894 | +7482.13 ppm |
| ${}^{172}$Tb | 172 | 107 | 187.8232 | 1377.0320 | -86.36 % | 161366.5778 | +7424.79 ppm |
| ${}^{173}$Tb | 173 | 108 | 193.9927 | 1381.9240 | -85.96 % | 162299.9737 | +7373.78 ppm |
| ${}^{174}$Tb | 174 | 109 | 200.1548 | 1385.5620 | -85.55 % | 163233.3770 | +7314.95 ppm |

### Dysprosium (Z = 66)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{138}$Dy | 138 | 72 | -47.5823 | 1097.1000 | -104.34 % | 129655.9766 | +8907.56 ppm |
| ${}^{139}$Dy | 139 | 73 | -41.0445 | 1107.9690 | -103.70 % | 130589.0041 | +8876.89 ppm |
| ${}^{140}$Dy | 140 | 74 | -34.5192 | 1121.1200 | -103.08 % | 131522.0443 | +8865.02 ppm |
| ${}^{141}$Dy | 141 | 75 | -28.0064 | 1131.8070 | -102.47 % | 132455.0969 | +8833.61 ppm |
| ${}^{142}$Dy | 142 | 76 | -21.5058 | 1144.6620 | -101.88 % | 133388.1618 | +8819.40 ppm |
| ${}^{143}$Dy | 143 | 77 | -15.0172 | 1154.7325 | -101.30 % | 134321.2386 | +8785.11 ppm |
| ${}^{144}$Dy | 144 | 78 | -8.5404 | 1167.2050 | -100.73 % | 135254.3273 | +8769.08 ppm |
| ${}^{145}$Dy | 145 | 79 | -2.0753 | 1176.9488 | -100.18 % | 136187.4276 | +8732.98 ppm |
| ${}^{146}$Dy | 146 | 80 | 4.3783 | 1189.3325 | -99.63 % | 137120.5393 | +8717.03 ppm |
| ${}^{147}$Dy | 147 | 81 | 10.8207 | 1199.0449 | -99.10 % | 138053.6624 | +8681.70 ppm |
| ${}^{148}$Dy | 148 | 82 | 17.2520 | 1210.7796 | -98.58 % | 138986.7965 | +8661.73 ppm |
| ${}^{149}$Dy | 149 | 83 | 23.6723 | 1218.6855 | -98.06 % | 139919.9416 | +8614.27 ppm |
| ${}^{150}$Dy | 150 | 84 | 30.0818 | 1228.3724 | -97.55 % | 140853.0975 | +8580.38 ppm |
| ${}^{151}$Dy | 151 | 85 | 36.4808 | 1235.8865 | -97.05 % | 141786.2640 | +8531.43 ppm |
| ${}^{152}$Dy | 152 | 86 | 42.8693 | 1245.3234 | -96.56 % | 142719.4409 | +8496.90 ppm |
| ${}^{153}$Dy | 153 | 87 | 49.2475 | 1252.4200 | -96.07 % | 143652.6281 | +8446.32 ppm |
| ${}^{154}$Dy | 154 | 88 | 55.6155 | 1261.7421 | -95.59 % | 144585.8255 | +8412.12 ppm |
| ${}^{155}$Dy | 155 | 89 | 61.9736 | 1268.5753 | -95.11 % | 145519.0329 | +8361.05 ppm |
| ${}^{156}$Dy | 156 | 90 | 68.3218 | 1278.0201 | -94.65 % | 146452.2501 | +8328.82 ppm |
| ${}^{157}$Dy | 157 | 91 | 74.6603 | 1284.9867 | -94.19 % | 147385.4770 | +8279.98 ppm |
| ${}^{158}$Dy | 158 | 92 | 80.9893 | 1294.0405 | -93.74 % | 148318.7134 | +8246.13 ppm |
| ${}^{159}$Dy | 159 | 93 | 87.3088 | 1300.8719 | -93.29 % | 149251.9593 | +8197.63 ppm |
| ${}^{160}$Dy | 160 | 94 | 93.6191 | 1309.4484 | -92.85 % | 150185.2145 | +8161.61 ppm |
| ${}^{161}$Dy | 161 | 95 | 99.9202 | 1315.9028 | -92.41 % | 151118.4788 | +8111.83 ppm |
| ${}^{162}$Dy | 162 | 96 | 106.2122 | 1324.0998 | -91.98 % | 152051.7522 | +8074.37 ppm |
| ${}^{163}$Dy | 163 | 97 | 112.4954 | 1330.3708 | -91.54 % | 152985.0344 | +8024.64 ppm |
| ${}^{164}$Dy | 164 | 98 | 118.7698 | 1338.0289 | -91.12 % | 153918.3255 | +7984.73 ppm |
| ${}^{165}$Dy | 165 | 99 | 125.0355 | 1343.7449 | -90.69 % | 154851.6252 | +7932.61 ppm |
| ${}^{166}$Dy | 166 | 100 | 131.2927 | 1350.7884 | -90.28 % | 155784.9334 | +7889.84 ppm |
| ${}^{167}$Dy | 167 | 101 | 137.5415 | 1356.1867 | -89.86 % | 156718.2501 | +7836.97 ppm |
| ${}^{168}$Dy | 168 | 102 | 143.7819 | 1362.9049 | -89.45 % | 157651.5750 | +7793.29 ppm |
| ${}^{169}$Dy | 169 | 103 | 150.0142 | 1368.0139 | -89.03 % | 158584.9082 | +7739.88 ppm |
| ${}^{170}$Dy | 170 | 104 | 156.2384 | 1374.2800 | -88.63 % | 159518.2494 | +7694.00 ppm |
| ${}^{171}$Dy | 171 | 105 | 162.4546 | 1378.6020 | -88.22 % | 160451.5986 | +7637.22 ppm |
| ${}^{172}$Dy | 172 | 106 | 168.6630 | 1384.4280 | -87.82 % | 161384.9557 | +7590.28 ppm |
| ${}^{173}$Dy | 173 | 107 | 174.8635 | 1388.4980 | -87.41 % | 162318.3205 | +7532.87 ppm |
| ${}^{174}$Dy | 174 | 108 | 181.0565 | 1393.9140 | -87.01 % | 163251.6930 | +7484.93 ppm |
| ${}^{175}$Dy | 175 | 109 | 187.2418 | 1397.5500 | -86.60 % | 164185.0731 | +7426.52 ppm |
| ${}^{176}$Dy | 176 | 110 | 193.4197 | 1402.5440 | -86.21 % | 165118.4606 | +7376.69 ppm |

### Holmium (Z = 67)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{140}$Ho | 140 | 73 | -55.0918 | 1106.8400 | -104.98 % | 131541.8346 | +8912.25 ppm |
| ${}^{141}$Ho | 141 | 74 | -48.5378 | 1119.9630 | -104.33 % | 132474.8460 | +8899.36 ppm |
| ${}^{142}$Ho | 142 | 75 | -41.9964 | 1131.0300 | -103.71 % | 133407.8700 | +8870.26 ppm |
| ${}^{143}$Ho | 143 | 76 | -35.4673 | 1143.8570 | -103.10 % | 134340.9064 | +8856.13 ppm |
| ${}^{144}$Ho | 144 | 77 | -28.9505 | 1154.4621 | -102.51 % | 135273.9549 | +8825.48 ppm |
| ${}^{145}$Ho | 145 | 78 | -22.4456 | 1167.0440 | -101.92 % | 136207.0155 | +8809.90 ppm |
| ${}^{146}$Ho | 146 | 79 | -15.9526 | 1177.2334 | -101.36 % | 137140.0879 | +8776.86 ppm |
| ${}^{147}$Ho | 147 | 80 | -9.4712 | 1189.8236 | -100.80 % | 138073.1719 | +8762.05 ppm |
| ${}^{148}$Ho | 148 | 81 | -3.0012 | 1200.1290 | -100.25 % | 139006.2674 | +8730.80 ppm |
| ${}^{149}$Ho | 149 | 82 | 3.4574 | 1211.8550 | -99.71 % | 139939.3742 | +8710.37 ppm |
| ${}^{150}$Ho | 150 | 83 | 9.9050 | 1220.2263 | -99.19 % | 140872.4920 | +8666.07 ppm |
| ${}^{151}$Ho | 151 | 84 | 16.3416 | 1229.9745 | -98.67 % | 141805.6208 | +8632.31 ppm |
| ${}^{152}$Ho | 152 | 85 | 22.7675 | 1238.0277 | -98.16 % | 142738.7604 | +8586.99 ppm |
| ${}^{153}$Ho | 153 | 86 | 29.1827 | 1247.5065 | -97.66 % | 143671.9105 | +8552.43 ppm |
| ${}^{154}$Ho | 154 | 87 | 35.5875 | 1255.2051 | -97.16 % | 144605.0712 | +8505.87 ppm |
| ${}^{155}$Ho | 155 | 88 | 41.9820 | 1264.6769 | -96.68 % | 145538.2421 | +8472.38 ppm |
| ${}^{156}$Ho | 156 | 89 | 48.3664 | 1272.2468 | -96.20 % | 146471.4232 | +8426.18 ppm |
| ${}^{157}$Ho | 157 | 90 | 54.7407 | 1281.6126 | -95.73 % | 147404.6143 | +8393.02 ppm |
| ${}^{158}$Ho | 158 | 91 | 61.1052 | 1289.0384 | -95.26 % | 148337.8152 | +8347.05 ppm |
| ${}^{159}$Ho | 159 | 92 | 67.4599 | 1298.2519 | -94.80 % | 149271.0259 | +8313.91 ppm |
| ${}^{160}$Ho | 160 | 93 | 73.8051 | 1305.3761 | -94.35 % | 150204.2461 | +8267.10 ppm |
| ${}^{161}$Ho | 161 | 94 | 80.1409 | 1314.2613 | -93.90 % | 151137.4758 | +8232.78 ppm |
| ${}^{162}$Ho | 162 | 95 | 86.4673 | 1321.1768 | -93.46 % | 152070.7148 | +8185.78 ppm |
| ${}^{163}$Ho | 163 | 96 | 92.7846 | 1329.5856 | -93.02 % | 153003.9629 | +8149.34 ppm |
| ${}^{164}$Ho | 164 | 97 | 99.0928 | 1336.2594 | -92.58 % | 153937.2201 | +8101.95 ppm |
| ${}^{165}$Ho | 165 | 98 | 105.3921 | 1344.2483 | -92.16 % | 154870.4862 | +8063.82 ppm |
| ${}^{166}$Ho | 166 | 99 | 111.6826 | 1350.4919 | -91.73 % | 155803.7612 | +8014.82 ppm |
| ${}^{167}$Ho | 167 | 100 | 117.9644 | 1357.7723 | -91.31 % | 156737.0448 | +7973.19 ppm |
| ${}^{168}$Ho | 168 | 101 | 124.2377 | 1363.6234 | -90.89 % | 157670.3370 | +7922.90 ppm |
| ${}^{169}$Ho | 169 | 102 | 130.5025 | 1370.4315 | -90.48 % | 158603.6376 | +7879.39 ppm |
| ${}^{170}$Ho | 170 | 103 | 136.7589 | 1375.9443 | -90.06 % | 159536.9465 | +7828.20 ppm |
| ${}^{171}$Ho | 171 | 104 | 143.0072 | 1382.2960 | -89.65 % | 160470.2637 | +7782.97 ppm |
| ${}^{172}$Ho | 172 | 105 | 149.2473 | 1387.3520 | -89.24 % | 161403.5890 | +7730.05 ppm |
| ${}^{173}$Ho | 173 | 106 | 155.4795 | 1393.3420 | -88.84 % | 162336.9223 | +7683.42 ppm |
| ${}^{174}$Ho | 174 | 107 | 161.7037 | 1397.9160 | -88.43 % | 163270.2634 | +7629.00 ppm |
| ${}^{175}$Ho | 175 | 108 | 167.9202 | 1403.3250 | -88.03 % | 164203.6124 | +7580.89 ppm |
| ${}^{176}$Ho | 176 | 109 | 174.1289 | 1407.4720 | -87.63 % | 165136.9691 | +7525.14 ppm |
| ${}^{177}$Ho | 177 | 110 | 180.3301 | 1412.4600 | -87.23 % | 166070.3334 | +7474.95 ppm |
| ${}^{178}$Ho | 178 | 111 | 186.5237 | 1416.3460 | -86.83 % | 167003.7051 | +7419.05 ppm |

### Erbium (Z = 68)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{142}$Er | 142 | 74 | -62.7586 | 1120.8060 | -105.60 % | 133427.8499 | +8950.24 ppm |
| ${}^{143}$Er | 143 | 75 | -56.1885 | 1132.1310 | -104.96 % | 134360.8452 | +8923.38 ppm |
| ${}^{144}$Er | 144 | 76 | -49.6310 | 1145.6640 | -104.33 % | 135293.8531 | +8913.67 ppm |
| ${}^{145}$Er | 145 | 77 | -43.0858 | 1156.3750 | -103.73 % | 136226.8734 | +8883.15 ppm |
| ${}^{146}$Er | 146 | 78 | -36.5528 | 1169.5349 | -103.13 % | 137159.9058 | +8871.31 ppm |
| ${}^{147}$Er | 147 | 79 | -30.0318 | 1179.8920 | -102.55 % | 138092.9502 | +8839.11 ppm |
| ${}^{148}$Er | 148 | 80 | -23.5225 | 1192.8345 | -101.97 % | 139026.0064 | +8826.36 ppm |
| ${}^{149}$Er | 149 | 81 | -17.0249 | 1203.1684 | -101.42 % | 139959.0742 | +8794.90 ppm |
| ${}^{150}$Er | 150 | 82 | -10.5388 | 1215.3294 | -100.87 % | 140892.1535 | +8777.13 ppm |
| ${}^{151}$Er | 151 | 83 | -4.0639 | 1223.8357 | -100.33 % | 141825.2440 | +8733.46 ppm |
| ${}^{152}$Er | 152 | 84 | 2.3999 | 1234.1410 | -99.81 % | 142758.3456 | +8703.25 ppm |
| ${}^{153}$Er | 153 | 85 | 8.8527 | 1242.1788 | -99.29 % | 143691.4582 | +8657.47 ppm |
| ${}^{154}$Er | 154 | 86 | 15.2948 | 1252.3884 | -98.78 % | 144624.5815 | +8627.63 ppm |
| ${}^{155}$Er | 155 | 87 | 21.7263 | 1260.0639 | -98.28 % | 145557.7155 | +8580.54 ppm |
| ${}^{156}$Er | 156 | 88 | 28.1473 | 1270.1377 | -97.78 % | 146490.8599 | +8550.78 ppm |
| ${}^{157}$Er | 157 | 89 | 34.5580 | 1277.4110 | -97.29 % | 147424.0146 | +8502.15 ppm |
| ${}^{158}$Er | 158 | 90 | 40.9585 | 1287.3725 | -96.82 % | 148357.1795 | +8472.63 ppm |
| ${}^{159}$Er | 159 | 91 | 47.3491 | 1294.7011 | -96.34 % | 149290.3544 | +8425.61 ppm |
| ${}^{160}$Er | 160 | 92 | 53.7297 | 1304.2755 | -95.88 % | 150223.5392 | +8394.45 ppm |
| ${}^{161}$Er | 161 | 93 | 60.1007 | 1311.4839 | -95.42 % | 151156.7337 | +8347.83 ppm |
| ${}^{162}$Er | 162 | 94 | 66.4620 | 1320.6881 | -94.97 % | 152089.9377 | +8315.19 ppm |
| ${}^{163}$Er | 163 | 95 | 72.8139 | 1327.5927 | -94.52 % | 153023.1513 | +8267.73 ppm |
| ${}^{164}$Er | 164 | 96 | 79.1565 | 1336.4391 | -94.08 % | 153956.3741 | +8233.73 ppm |
| ${}^{165}$Er | 165 | 97 | 85.4899 | 1343.0892 | -93.63 % | 154889.6062 | +8185.80 ppm |
| ${}^{166}$Er | 166 | 98 | 91.8142 | 1351.5634 | -93.21 % | 155822.8473 | +8150.39 ppm |
| ${}^{167}$Er | 167 | 99 | 98.1295 | 1357.9998 | -92.77 % | 156756.0973 | +8102.26 ppm |
| ${}^{168}$Er | 168 | 100 | 104.4361 | 1365.7711 | -92.35 % | 157689.3562 | +8063.36 ppm |
| ${}^{169}$Er | 169 | 101 | 110.7339 | 1371.7743 | -91.93 % | 158622.6238 | +8013.66 ppm |
| ${}^{170}$Er | 170 | 102 | 117.0231 | 1379.0320 | -91.51 % | 159555.9000 | +7972.57 ppm |
| ${}^{171}$Er | 171 | 103 | 123.3039 | 1384.7136 | -91.10 % | 160489.1846 | +7922.05 ppm |
| ${}^{172}$Er | 172 | 104 | 129.5763 | 1391.5497 | -90.69 % | 161422.4776 | +7879.44 ppm |
| ${}^{173}$Er | 173 | 105 | 135.8405 | 1396.8020 | -90.27 % | 162355.7789 | +7827.40 ppm |
| ${}^{174}$Er | 174 | 106 | 142.0965 | 1403.1360 | -89.87 % | 163289.0883 | +7783.00 ppm |
| ${}^{175}$Er | 175 | 107 | 148.3445 | 1407.8750 | -89.46 % | 164222.4057 | +7729.31 ppm |
| ${}^{176}$Er | 176 | 108 | 154.5846 | 1413.9840 | -89.07 % | 165155.7311 | +7684.12 ppm |
| ${}^{177}$Er | 177 | 109 | 160.8169 | 1418.3010 | -88.66 % | 166089.0642 | +7628.79 ppm |
| ${}^{178}$Er | 178 | 110 | 167.0414 | 1423.8220 | -88.27 % | 167022.4051 | +7581.27 ppm |
| ${}^{179}$Er | 179 | 111 | 173.2583 | 1427.7040 | -87.86 % | 167955.7537 | +7524.77 ppm |
| ${}^{180}$Er | 180 | 112 | 179.4676 | 1432.8000 | -87.47 % | 168889.1097 | +7476.63 ppm |

### Thulium (Z = 69)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{144}$Tm | 144 | 75 | -70.5820 | 1130.4000 | -106.24 % | 135314.0218 | +8955.36 ppm |
| ${}^{145}$Tm | 145 | 76 | -63.9959 | 1143.9050 | -105.59 % | 136247.0011 | +8945.10 ppm |
| ${}^{146}$Tm | 146 | 77 | -57.4223 | 1155.4440 | -104.97 % | 137179.9929 | +8920.61 ppm |
| ${}^{147}$Tm | 147 | 78 | -50.8610 | 1168.4762 | -104.35 % | 138112.9971 | +8907.19 ppm |
| ${}^{148}$Tm | 148 | 79 | -44.3120 | 1179.3382 | -103.76 % | 139046.0135 | +8878.47 ppm |
| ${}^{149}$Tm | 149 | 80 | -37.7749 | 1192.5960 | -103.17 % | 139979.0418 | +8867.55 ppm |
| ${}^{150}$Tm | 150 | 81 | -31.2495 | 1203.1500 | -102.60 % | 140912.0819 | +8837.90 ppm |
| ${}^{151}$Tm | 151 | 82 | -24.7358 | 1215.5587 | -102.03 % | 141845.1336 | +8821.14 ppm |
| ${}^{152}$Tm | 152 | 83 | -18.2335 | 1224.5787 | -101.49 % | 142778.1967 | +8780.94 ppm |
| ${}^{153}$Tm | 153 | 84 | -11.7425 | 1234.9023 | -100.95 % | 143711.2711 | +8750.56 ppm |
| ${}^{154}$Tm | 154 | 85 | -5.2626 | 1243.4282 | -100.42 % | 144644.3566 | +8708.02 ppm |
| ${}^{155}$Tm | 155 | 86 | 1.2064 | 1253.6983 | -99.90 % | 145577.4530 | +8678.28 ppm |
| ${}^{156}$Tm | 156 | 87 | 7.6646 | 1261.9781 | -99.39 % | 146510.5602 | +8635.18 ppm |
| ${}^{157}$Tm | 157 | 88 | 14.1123 | 1271.9243 | -98.89 % | 147443.6780 | +8604.20 ppm |
| ${}^{158}$Tm | 158 | 89 | 20.5494 | 1279.9895 | -98.39 % | 148376.8063 | +8560.79 ppm |
| ${}^{159}$Tm | 159 | 90 | 26.9762 | 1289.9280 | -97.91 % | 149309.9449 | +8530.76 ppm |
| ${}^{160}$Tm | 160 | 91 | 33.3929 | 1297.7300 | -97.43 % | 150243.0937 | +8486.70 ppm |
| ${}^{161}$Tm | 161 | 92 | 39.7996 | 1307.3990 | -96.96 % | 151176.2524 | +8455.82 ppm |
| ${}^{162}$Tm | 162 | 93 | 46.1963 | 1315.0491 | -96.49 % | 152109.4211 | +8411.89 ppm |
| ${}^{163}$Tm | 163 | 94 | 52.5834 | 1324.3713 | -96.03 % | 153042.5995 | +8379.67 ppm |
| ${}^{164}$Tm | 164 | 95 | 58.9608 | 1331.6232 | -95.57 % | 153975.7875 | +8334.23 ppm |
| ${}^{165}$Tm | 165 | 96 | 65.3288 | 1340.7156 | -95.13 % | 154908.9849 | +8301.49 ppm |
| ${}^{166}$Tm | 166 | 97 | 71.6874 | 1347.7433 | -94.68 % | 155842.1917 | +8255.73 ppm |
| ${}^{167}$Tm | 167 | 98 | 78.0368 | 1356.4713 | -94.25 % | 156775.4078 | +8221.61 ppm |
| ${}^{168}$Tm | 168 | 99 | 84.3771 | 1363.3119 | -93.81 % | 157708.6329 | +8175.79 ppm |
| ${}^{169}$Tm | 169 | 100 | 90.7085 | 1371.3455 | -93.39 % | 158641.8669 | +8138.21 ppm |
| ${}^{170}$Tm | 170 | 101 | 97.0310 | 1377.9374 | -92.96 % | 159575.1098 | +8091.94 ppm |
| ${}^{171}$Tm | 171 | 102 | 103.3448 | 1385.4237 | -92.54 % | 160508.3615 | +8051.94 ppm |
| ${}^{172}$Tm | 172 | 103 | 109.6499 | 1391.6583 | -92.12 % | 161441.6217 | +8004.57 ppm |
| ${}^{173}$Tm | 173 | 104 | 115.9466 | 1398.6122 | -91.71 % | 162374.8904 | +7962.31 ppm |
| ${}^{174}$Tm | 174 | 105 | 122.2349 | 1404.2919 | -91.30 % | 163308.1676 | +7912.66 ppm |
| ${}^{175}$Tm | 175 | 106 | 128.5150 | 1410.8093 | -90.89 % | 164241.4530 | +7868.81 ppm |
| ${}^{176}$Tm | 176 | 107 | 134.7868 | 1415.9414 | -90.48 % | 165174.7465 | +7817.00 ppm |
| ${}^{177}$Tm | 177 | 108 | 141.0506 | 1422.1950 | -90.08 % | 166108.0481 | +7772.77 ppm |
| ${}^{178}$Tm | 178 | 109 | 147.3065 | 1427.0260 | -89.68 % | 167041.3577 | +7719.80 ppm |
| ${}^{179}$Tm | 179 | 110 | 153.5545 | 1432.7160 | -89.28 % | 167974.6752 | +7673.46 ppm |
| ${}^{180}$Tm | 180 | 111 | 159.7947 | 1436.9400 | -88.88 % | 168908.0003 | +7619.31 ppm |
| ${}^{181}$Tm | 181 | 112 | 166.0273 | 1442.3890 | -88.49 % | 169841.3332 | +7571.80 ppm |
| ${}^{182}$Tm | 182 | 113 | 172.2523 | 1446.5360 | -88.09 % | 170774.6736 | +7517.60 ppm |

### Ytterbium (Z = 70)

_38 of 38 isotopes with a framework prediction; 38 of 38 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{148}$Yb | 148 | 78 | -65.3695 | 1170.0880 | -105.59 % | 139066.2887 | +8963.09 ppm |
| ${}^{149}$Yb | 149 | 79 | -58.7923 | 1181.1230 | -104.98 % | 139999.2769 | +8936.23 ppm |
| ${}^{150}$Yb | 150 | 80 | -52.2272 | 1194.7500 | -104.37 % | 140932.2772 | +8927.15 ppm |
| ${}^{151}$Yb | 151 | 81 | -45.6741 | 1205.5471 | -103.79 % | 141865.2895 | +8898.27 ppm |
| ${}^{152}$Yb | 152 | 82 | -39.1327 | 1218.3464 | -103.21 % | 142798.3136 | +8884.22 ppm |
| ${}^{153}$Yb | 153 | 83 | -32.6030 | 1227.3660 | -102.66 % | 143731.3493 | +8843.25 ppm |
| ${}^{154}$Yb | 154 | 84 | -26.0847 | 1238.1508 | -102.11 % | 144664.3964 | +8816.14 ppm |
| ${}^{155}$Yb | 155 | 85 | -19.5776 | 1246.7926 | -101.57 % | 145597.4547 | +8774.07 ppm |
| ${}^{156}$Yb | 156 | 86 | -13.0816 | 1257.6269 | -101.04 % | 146530.5241 | +8747.84 ppm |
| ${}^{157}$Yb | 157 | 87 | -6.5965 | 1265.8526 | -100.52 % | 147463.6045 | +8704.02 ppm |
| ${}^{158}$Yb | 158 | 88 | -0.1222 | 1276.5136 | -100.01 % | 148396.6956 | +8677.52 ppm |
| ${}^{159}$Yb | 159 | 89 | 6.3414 | 1284.4088 | -99.51 % | 149329.7974 | +8632.58 ppm |
| ${}^{160}$Yb | 160 | 90 | 12.7946 | 1294.8098 | -99.01 % | 150262.9096 | +8605.24 ppm |
| ${}^{161}$Yb | 161 | 91 | 19.2375 | 1302.5522 | -98.52 % | 151196.0321 | +8560.42 ppm |
| ${}^{162}$Yb | 162 | 92 | 25.6702 | 1312.6104 | -98.04 % | 152129.1648 | +8531.70 ppm |
| ${}^{163}$Yb | 163 | 93 | 32.0929 | 1320.1544 | -97.57 % | 153062.3076 | +8486.70 ppm |
| ${}^{164}$Yb | 164 | 94 | 38.5057 | 1329.9440 | -97.10 % | 153995.4602 | +8457.14 ppm |
| ${}^{165}$Yb | 165 | 95 | 44.9088 | 1337.2986 | -96.64 % | 154928.6225 | +8412.02 ppm |
| ${}^{166}$Yb | 166 | 96 | 51.3022 | 1346.6682 | -96.19 % | 155861.7945 | +8380.65 ppm |
| ${}^{167}$Yb | 167 | 97 | 57.6862 | 1353.7357 | -95.74 % | 156794.9760 | +8334.79 ppm |
| ${}^{168}$Yb | 168 | 98 | 64.0608 | 1362.7970 | -95.30 % | 157728.1668 | +8302.38 ppm |
| ${}^{169}$Yb | 169 | 99 | 70.4262 | 1369.6640 | -94.86 % | 158661.3669 | +8256.36 ppm |
| ${}^{170}$Yb | 170 | 100 | 76.7824 | 1378.1237 | -94.43 % | 159594.5760 | +8221.09 ppm |
| ${}^{171}$Yb | 171 | 101 | 83.1297 | 1384.7379 | -94.00 % | 160527.7942 | +8174.59 ppm |
| ${}^{172}$Yb | 172 | 102 | 89.4682 | 1392.7579 | -93.58 % | 161461.0212 | +8137.55 ppm |
| ${}^{173}$Yb | 173 | 103 | 95.7978 | 1399.1250 | -93.15 % | 162394.2569 | +8090.64 ppm |
| ${}^{174}$Yb | 174 | 104 | 102.1189 | 1406.5896 | -92.74 % | 163327.5013 | +8051.15 ppm |
| ${}^{175}$Yb | 175 | 105 | 108.4314 | 1412.4119 | -92.32 % | 164260.7542 | +8002.01 ppm |
| ${}^{176}$Yb | 176 | 106 | 114.7355 | 1419.2790 | -91.92 % | 165194.0155 | +7959.90 ppm |
| ${}^{177}$Yb | 177 | 107 | 121.0314 | 1424.8454 | -91.51 % | 166127.2851 | +7910.37 ppm |
| ${}^{178}$Yb | 178 | 108 | 127.3190 | 1431.6075 | -91.11 % | 167060.5629 | +7868.72 ppm |
| ${}^{179}$Yb | 179 | 109 | 133.5985 | 1436.6540 | -90.70 % | 167993.8487 | +7817.13 ppm |
| ${}^{180}$Yb | 180 | 110 | 139.8701 | 1442.8800 | -90.31 % | 168927.1426 | +7772.89 ppm |
| ${}^{181}$Yb | 181 | 111 | 146.1338 | 1447.2760 | -89.90 % | 169860.4443 | +7718.94 ppm |
| ${}^{182}$Yb | 182 | 112 | 152.3897 | 1453.0880 | -89.51 % | 170793.7539 | +7674.22 ppm |
| ${}^{183}$Yb | 183 | 113 | 158.6379 | 1457.2290 | -89.11 % | 171727.0711 | +7619.91 ppm |
| ${}^{184}$Yb | 184 | 114 | 164.8785 | 1462.9840 | -88.73 % | 172660.3959 | +7575.07 ppm |
| ${}^{185}$Yb | 185 | 115 | 171.1116 | 1466.8650 | -88.33 % | 173593.7282 | +7520.69 ppm |

### Lutetium (Z = 71)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{150}$Lu | 150 | 79 | -73.4719 | 1179.9000 | -106.23 % | 140952.7395 | +8972.09 ppm |
| ${}^{151}$Lu | 151 | 80 | -66.8788 | 1193.5040 | -105.60 % | 141885.7119 | +8962.84 ppm |
| ${}^{152}$Lu | 152 | 81 | -60.2978 | 1204.7520 | -105.00 % | 142818.6963 | +8936.64 ppm |
| ${}^{153}$Lu | 153 | 82 | -53.7287 | 1217.7405 | -104.41 % | 143751.6927 | +8923.84 ppm |
| ${}^{154}$Lu | 154 | 83 | -47.1714 | 1227.0720 | -103.84 % | 144684.7008 | +8885.52 ppm |
| ${}^{155}$Lu | 155 | 84 | -40.6257 | 1238.0527 | -103.28 % | 145617.7205 | +8858.86 ppm |
| ${}^{156}$Lu | 156 | 85 | -34.0914 | 1247.2785 | -102.73 % | 146550.7516 | +8820.65 ppm |
| ${}^{157}$Lu | 157 | 86 | -27.5684 | 1258.0901 | -102.19 % | 147483.7940 | +8793.95 ppm |
| ${}^{158}$Lu | 158 | 87 | -21.0564 | 1266.9338 | -101.66 % | 148416.8475 | +8754.17 ppm |
| ${}^{159}$Lu | 159 | 88 | -14.5554 | 1277.5015 | -101.14 % | 149349.9118 | +8726.71 ppm |
| ${}^{160}$Lu | 160 | 89 | -8.0651 | 1286.1342 | -100.63 % | 150282.9870 | +8686.56 ppm |
| ${}^{161}$Lu | 161 | 90 | -1.5854 | 1296.4979 | -100.12 % | 151216.0727 | +8658.63 ppm |
| ${}^{162}$Lu | 162 | 91 | 4.8838 | 1304.8387 | -99.63 % | 152149.1690 | +8617.59 ppm |
| ${}^{163}$Lu | 163 | 92 | 11.3426 | 1314.8696 | -99.14 % | 153082.2755 | +8588.34 ppm |
| ${}^{164}$Lu | 164 | 93 | 17.7913 | 1322.7919 | -98.66 % | 154015.3922 | +8545.60 ppm |
| ${}^{165}$Lu | 165 | 94 | 24.2300 | 1332.6631 | -98.18 % | 154948.5190 | +8516.23 ppm |
| ${}^{166}$Lu | 166 | 95 | 30.6588 | 1340.3131 | -97.71 % | 155881.6557 | +8472.79 ppm |
| ${}^{167}$Lu | 167 | 96 | 37.0778 | 1349.8898 | -97.25 % | 156814.8021 | +8442.42 ppm |
| ${}^{168}$Lu | 168 | 97 | 43.4872 | 1357.5076 | -96.80 % | 157747.9581 | +8399.85 ppm |
| ${}^{169}$Lu | 169 | 98 | 49.8871 | 1366.5886 | -96.35 % | 158681.1237 | +8367.22 ppm |
| ${}^{170}$Lu | 170 | 99 | 56.2776 | 1373.8837 | -95.90 % | 159614.2986 | +8323.66 ppm |
| ${}^{171}$Lu | 171 | 100 | 62.6588 | 1382.4772 | -95.47 % | 160547.4827 | +8288.88 ppm |
| ${}^{172}$Lu | 172 | 101 | 69.0310 | 1389.4561 | -95.03 % | 161480.6760 | +8244.41 ppm |
| ${}^{173}$Lu | 173 | 102 | 75.3941 | 1397.6724 | -94.61 % | 162413.8783 | +8208.25 ppm |
| ${}^{174}$Lu | 174 | 103 | 81.7484 | 1404.4330 | -94.18 % | 163347.0894 | +8163.50 ppm |
| ${}^{175}$Lu | 175 | 104 | 88.0939 | 1412.0997 | -93.76 % | 164280.3093 | +8124.92 ppm |
| ${}^{176}$Lu | 176 | 105 | 94.4308 | 1418.3877 | -93.34 % | 165213.5379 | +8078.35 ppm |
| ${}^{177}$Lu | 177 | 106 | 100.7591 | 1425.4606 | -92.93 % | 166146.7750 | +8037.17 ppm |
| ${}^{178}$Lu | 178 | 107 | 107.0789 | 1431.4859 | -92.52 % | 167080.0206 | +7990.12 ppm |
| ${}^{179}$Lu | 179 | 108 | 113.3905 | 1438.2783 | -92.12 % | 168013.2744 | +7948.30 ppm |
| ${}^{180}$Lu | 180 | 109 | 119.6938 | 1443.9671 | -91.71 % | 168946.5365 | +7900.35 ppm |
| ${}^{181}$Lu | 181 | 110 | 125.9891 | 1450.1593 | -91.31 % | 169879.8067 | +7855.99 ppm |
| ${}^{182}$Lu | 182 | 111 | 132.2763 | 1455.2720 | -90.91 % | 170813.0849 | +7805.34 ppm |
| ${}^{183}$Lu | 183 | 112 | 138.5556 | 1461.2207 | -90.52 % | 171746.3710 | +7761.05 ppm |
| ${}^{184}$Lu | 184 | 113 | 144.8271 | 1465.9280 | -90.12 % | 172679.6649 | +7709.27 ppm |
| ${}^{185}$Lu | 185 | 114 | 151.0909 | 1471.6750 | -89.73 % | 173612.9666 | +7664.40 ppm |
| ${}^{186}$Lu | 186 | 115 | 157.3470 | 1476.0960 | -89.34 % | 174546.2758 | +7612.49 ppm |
| ${}^{187}$Lu | 187 | 116 | 163.5957 | 1481.6010 | -88.96 % | 175479.5926 | +7567.48 ppm |
| ${}^{188}$Lu | 188 | 117 | 169.8369 | 1485.7640 | -88.57 % | 176412.9169 | +7514.95 ppm |

### Hafnium (Z = 72)

_38 of 38 isotopes with a framework prediction; 38 of 38 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{153}$Hf | 153 | 81 | -75.1197 | 1205.9460 | -106.23 % | 143772.3013 | +8990.05 ppm |
| ${}^{154}$Hf | 154 | 82 | -68.5229 | 1219.3720 | -105.62 % | 144705.2699 | +8980.14 ppm |
| ${}^{155}$Hf | 155 | 83 | -61.9380 | 1228.9950 | -105.04 % | 145638.2505 | +8943.53 ppm |
| ${}^{156}$Hf | 156 | 84 | -55.3648 | 1240.6161 | -104.46 % | 146571.2427 | +8920.87 ppm |
| ${}^{157}$Hf | 157 | 85 | -48.8032 | 1249.7200 | -103.91 % | 147504.2465 | +8881.50 ppm |
| ${}^{158}$Hf | 158 | 86 | -42.2531 | 1261.0417 | -103.35 % | 148437.2618 | +8857.89 ppm |
| ${}^{159}$Hf | 159 | 87 | -35.7141 | 1269.8632 | -102.81 % | 149370.2883 | +8817.62 ppm |
| ${}^{160}$Hf | 160 | 88 | -29.1862 | 1281.0207 | -102.28 % | 150303.3258 | +8793.75 ppm |
| ${}^{161}$Hf | 161 | 89 | -22.6693 | 1289.4690 | -101.76 % | 151236.3743 | +8752.02 ppm |
| ${}^{162}$Hf | 162 | 90 | -16.1631 | 1300.3930 | -101.24 % | 152169.4335 | +8727.42 ppm |
| ${}^{163}$Hf | 163 | 91 | -9.6675 | 1308.5652 | -100.74 % | 153102.5034 | +8684.92 ppm |
| ${}^{164}$Hf | 164 | 92 | -3.1824 | 1319.1855 | -100.24 % | 154035.5837 | +8659.17 ppm |
| ${}^{165}$Hf | 165 | 93 | 3.2924 | 1327.0740 | -99.75 % | 154968.6743 | +8615.86 ppm |
| ${}^{166}$Hf | 166 | 94 | 9.7570 | 1337.3688 | -99.27 % | 155901.7751 | +8588.84 ppm |
| ${}^{167}$Hf | 167 | 95 | 16.2115 | 1345.0489 | -98.79 % | 156834.8860 | +8545.25 ppm |
| ${}^{168}$Hf | 168 | 96 | 22.6562 | 1355.0130 | -98.33 % | 157768.0068 | +8516.97 ppm |
| ${}^{169}$Hf | 169 | 97 | 29.0911 | 1362.4407 | -97.86 % | 158701.1373 | +8472.83 ppm |
| ${}^{170}$Hf | 170 | 98 | 35.5163 | 1372.0490 | -97.41 % | 159634.2775 | +8443.16 ppm |
| ${}^{171}$Hf | 171 | 99 | 41.9321 | 1379.2977 | -96.96 % | 160567.4271 | +8398.96 ppm |
| ${}^{172}$Hf | 172 | 100 | 48.3384 | 1388.3400 | -96.52 % | 161500.5862 | +8366.62 ppm |
| ${}^{173}$Hf | 173 | 101 | 54.7355 | 1395.4208 | -96.08 % | 162433.7545 | +8322.43 ppm |
| ${}^{174}$Hf | 174 | 102 | 61.1235 | 1403.9249 | -95.65 % | 163366.9320 | +8287.67 ppm |
| ${}^{175}$Hf | 175 | 103 | 67.5024 | 1410.6334 | -95.21 % | 164300.1185 | +8242.25 ppm |
| ${}^{176}$Hf | 176 | 104 | 73.8725 | 1418.7994 | -94.79 % | 165233.3138 | +8206.37 ppm |
| ${}^{177}$Hf | 177 | 105 | 80.2338 | 1425.1751 | -94.37 % | 166166.5180 | +8159.99 ppm |
| ${}^{178}$Hf | 178 | 106 | 86.5863 | 1432.8010 | -93.96 % | 167099.7308 | +8121.79 ppm |
| ${}^{179}$Hf | 179 | 107 | 92.9304 | 1438.9000 | -93.54 % | 168032.9522 | +8074.84 ppm |
| ${}^{180}$Hf | 180 | 108 | 99.2659 | 1446.2877 | -93.14 % | 168966.1821 | +8036.21 ppm |
| ${}^{181}$Hf | 181 | 109 | 105.5932 | 1451.9825 | -92.73 % | 169899.4203 | +7987.93 ppm |
| ${}^{182}$Hf | 182 | 110 | 111.9122 | 1458.7005 | -92.33 % | 170832.6667 | +7946.32 ppm |
| ${}^{183}$Hf | 183 | 111 | 118.2230 | 1464.0058 | -91.92 % | 171765.9213 | +7896.86 ppm |
| ${}^{184}$Hf | 184 | 112 | 124.5258 | 1470.2930 | -91.53 % | 172699.1839 | +7853.76 ppm |
| ${}^{185}$Hf | 185 | 113 | 130.8207 | 1475.1847 | -91.13 % | 173632.4544 | +7803.01 ppm |
| ${}^{186}$Hf | 186 | 114 | 137.1078 | 1481.3604 | -90.74 % | 174565.7328 | +7760.32 ppm |
| ${}^{187}$Hf | 187 | 115 | 143.3871 | 1486.0890 | -90.35 % | 175499.0189 | +7709.29 ppm |
| ${}^{188}$Hf | 188 | 116 | 149.6587 | 1491.9680 | -89.97 % | 176432.3127 | +7666.06 ppm |
| ${}^{189}$Hf | 189 | 117 | 155.9228 | 1496.3130 | -89.58 % | 177365.6140 | +7614.70 ppm |
| ${}^{190}$Hf | 190 | 118 | 162.1795 | 1501.9500 | -89.20 % | 178298.9228 | +7571.49 ppm |

### Tantalum (Z = 73)

_40 of 40 isotopes with a framework prediction; 40 of 40 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{155}$Ta | 155 | 82 | -83.5144 | 1217.9900 | -106.86 % | 145659.0445 | +9015.43 ppm |
| ${}^{156}$Ta | 156 | 83 | -76.9019 | 1228.0320 | -106.26 % | 146591.9974 | +8981.65 ppm |
| ${}^{157}$Ta | 157 | 84 | -70.3012 | 1239.6815 | -105.67 % | 147524.9621 | +8959.30 ppm |
| ${}^{158}$Ta | 158 | 85 | -63.7122 | 1249.3060 | -105.10 % | 148457.9386 | +8923.10 ppm |
| ${}^{159}$Ta | 159 | 86 | -57.1348 | 1260.6674 | -104.53 % | 149390.9266 | +8899.68 ppm |
| ${}^{160}$Ta | 160 | 87 | -50.5688 | 1270.1233 | -103.98 % | 150323.9261 | +8863.52 ppm |
| ${}^{161}$Ta | 161 | 88 | -44.0141 | 1281.1494 | -103.44 % | 151256.9367 | +8838.45 ppm |
| ${}^{162}$Ta | 162 | 89 | -37.4703 | 1290.2236 | -102.90 % | 152189.9584 | +8800.71 ppm |
| ${}^{163}$Ta | 163 | 90 | -30.9376 | 1301.0482 | -102.38 % | 153122.9911 | +8775.14 ppm |
| ${}^{164}$Ta | 164 | 91 | -24.4155 | 1309.8676 | -101.86 % | 154056.0345 | +8736.70 ppm |
| ${}^{165}$Ta | 165 | 92 | -17.9041 | 1320.5040 | -101.36 % | 154989.0885 | +8710.73 ppm |
| ${}^{166}$Ta | 166 | 93 | -11.4032 | 1328.8253 | -100.86 % | 155922.1530 | +8670.03 ppm |
| ${}^{167}$Ta | 167 | 94 | -4.9126 | 1339.1499 | -100.37 % | 156855.2278 | +8642.87 ppm |
| ${}^{168}$Ta | 168 | 95 | 1.5679 | 1347.2640 | -99.88 % | 157788.3127 | +8601.86 ppm |
| ${}^{169}$Ta | 169 | 96 | 8.0383 | 1357.2319 | -99.41 % | 158721.4078 | +8573.27 ppm |
| ${}^{170}$Ta | 170 | 97 | 14.4987 | 1365.1504 | -98.94 % | 159654.5127 | +8532.03 ppm |
| ${}^{171}$Ta | 171 | 98 | 20.9494 | 1374.8043 | -98.48 % | 160587.6274 | +8502.32 ppm |
| ${}^{172}$Ta | 172 | 99 | 27.3905 | 1382.4854 | -98.02 % | 161520.7518 | +8460.59 ppm |
| ${}^{173}$Ta | 173 | 100 | 33.8220 | 1391.6232 | -97.57 % | 162453.8857 | +8428.52 ppm |
| ${}^{174}$Ta | 174 | 101 | 40.2442 | 1399.0388 | -97.12 % | 163387.0290 | +8386.17 ppm |
| ${}^{175}$Ta | 175 | 102 | 46.6570 | 1407.7780 | -96.69 % | 164320.1816 | +8352.54 ppm |
| ${}^{176}$Ta | 176 | 103 | 53.0607 | 1414.8060 | -96.25 % | 165253.3433 | +8308.82 ppm |
| ${}^{177}$Ta | 177 | 104 | 59.4554 | 1423.2267 | -95.82 % | 166186.5140 | +8274.18 ppm |
| ${}^{178}$Ta | 178 | 105 | 65.8412 | 1430.2300 | -95.40 % | 167119.6937 | +8231.06 ppm |
| ${}^{179}$Ta | 179 | 106 | 72.2181 | 1438.0121 | -94.98 % | 168052.8821 | +8193.77 ppm |
| ${}^{180}$Ta | 180 | 107 | 78.5864 | 1444.6596 | -94.56 % | 168986.0793 | +8149.83 ppm |
| ${}^{181}$Ta | 181 | 108 | 84.9461 | 1452.2363 | -94.15 % | 169919.2850 | +8111.99 ppm |
| ${}^{182}$Ta | 182 | 109 | 91.2973 | 1458.2992 | -93.74 % | 170852.4992 | +8065.60 ppm |
| ${}^{183}$Ta | 183 | 110 | 97.6401 | 1465.2334 | -93.34 % | 171785.7218 | +8024.93 ppm |
| ${}^{184}$Ta | 184 | 111 | 103.9747 | 1470.8506 | -92.93 % | 172718.9526 | +7977.01 ppm |
| ${}^{185}$Ta | 185 | 112 | 110.3012 | 1477.4769 | -92.53 % | 173652.1916 | +7935.55 ppm |
| ${}^{186}$Ta | 186 | 113 | 116.6195 | 1482.7614 | -92.13 % | 174585.4387 | +7886.78 ppm |
| ${}^{187}$Ta | 187 | 114 | 122.9299 | 1489.1207 | -91.74 % | 175518.6937 | +7844.80 ppm |
| ${}^{188}$Ta | 188 | 115 | 129.2325 | 1494.2240 | -91.35 % | 176451.9566 | +7795.98 ppm |
| ${}^{189}$Ta | 189 | 116 | 135.5272 | 1500.2820 | -90.97 % | 177385.2273 | +7753.65 ppm |
| ${}^{190}$Ta | 190 | 117 | 141.8143 | 1505.1800 | -90.58 % | 178318.5056 | +7704.47 ppm |
| ${}^{191}$Ta | 191 | 118 | 148.0938 | 1511.0010 | -90.20 % | 179251.7915 | +7661.74 ppm |
| ${}^{192}$Ta | 192 | 119 | 154.3659 | 1515.6480 | -89.82 % | 180185.0849 | +7612.62 ppm |
| ${}^{193}$Ta | 193 | 120 | 160.6305 | 1521.4190 | -89.44 % | 181118.3857 | +7570.38 ppm |
| ${}^{194}$Ta | 194 | 121 | 166.8878 | 1525.8100 | -89.06 % | 182051.6938 | +7520.88 ppm |

### Tungsten (Z = 74)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{157}$W | 157 | 83 | -92.0621 | 1228.9960 | -107.49 % | 147545.9408 | +9034.42 ppm |
| ${}^{158}$W | 158 | 84 | -85.4339 | 1241.0900 | -106.88 % | 148478.8779 | +9014.48 ppm |
| ${}^{159}$W | 159 | 85 | -78.8175 | 1250.8530 | -106.30 % | 149411.8270 | +8979.46 ppm |
| ${}^{160}$W | 160 | 86 | -72.2129 | 1262.8463 | -105.72 % | 150344.7878 | +8959.55 ppm |
| ${}^{161}$W | 161 | 87 | -65.6197 | 1272.0610 | -105.16 % | 151277.7601 | +8921.68 ppm |
| ${}^{162}$W | 162 | 88 | -59.0380 | 1283.6591 | -104.60 % | 152210.7437 | +8899.82 ppm |
| ${}^{163}$W | 163 | 89 | -52.4675 | 1292.6396 | -104.06 % | 153143.7386 | +8861.14 ppm |
| ${}^{164}$W | 164 | 90 | -45.9080 | 1304.0380 | -103.52 % | 154076.7446 | +8838.97 ppm |
| ${}^{165}$W | 165 | 91 | -39.3595 | 1312.7351 | -103.00 % | 155009.7615 | +8799.40 ppm |
| ${}^{166}$W | 166 | 92 | -32.8217 | 1323.8326 | -102.48 % | 155942.7891 | +8776.05 ppm |
| ${}^{167}$W | 167 | 93 | -26.2945 | 1332.1097 | -101.97 % | 156875.8274 | +8734.75 ppm |
| ${}^{168}$W | 168 | 94 | -19.7778 | 1342.9807 | -101.47 % | 157808.8761 | +8710.73 ppm |
| ${}^{169}$W | 169 | 95 | -13.2714 | 1351.0769 | -100.98 % | 158741.9351 | +8669.27 ppm |
| ${}^{170}$W | 170 | 96 | -6.7752 | 1361.5212 | -100.50 % | 159675.0043 | +8643.33 ppm |
| ${}^{171}$W | 171 | 97 | -0.2891 | 1369.3878 | -100.02 % | 160608.0836 | +8601.43 ppm |
| ${}^{172}$W | 172 | 98 | 6.1872 | 1379.4702 | -99.55 % | 161541.1728 | +8574.03 ppm |
| ${}^{173}$W | 173 | 99 | 12.6536 | 1387.1717 | -99.09 % | 162474.2718 | +8532.10 ppm |
| ${}^{174}$W | 174 | 100 | 19.1104 | 1396.7428 | -98.63 % | 163407.3804 | +8502.35 ppm |
| ${}^{175}$W | 175 | 101 | 25.5576 | 1404.2198 | -98.18 % | 164340.4986 | +8460.04 ppm |
| ${}^{176}$W | 176 | 102 | 31.9955 | 1413.2999 | -97.74 % | 165273.6262 | +8428.13 ppm |
| ${}^{177}$W | 177 | 103 | 38.4240 | 1420.4314 | -97.29 % | 166206.7630 | +8384.71 ppm |
| ${}^{178}$W | 178 | 104 | 44.8434 | 1429.2080 | -96.86 % | 167139.9091 | +8351.85 ppm |
| ${}^{179}$W | 179 | 105 | 51.2538 | 1436.1675 | -96.43 % | 168073.0641 | +8308.42 ppm |
| ${}^{180}$W | 180 | 106 | 57.6552 | 1444.5798 | -96.01 % | 169006.2281 | +8274.26 ppm |
| ${}^{181}$W | 181 | 107 | 64.0478 | 1451.2488 | -95.59 % | 169939.4010 | +8230.10 ppm |
| ${}^{182}$W | 182 | 108 | 70.4317 | 1459.3323 | -95.17 % | 170872.5825 | +8194.90 ppm |
| ${}^{183}$W | 183 | 109 | 76.8070 | 1465.5232 | -94.76 % | 171805.7727 | +8148.93 ppm |
| ${}^{184}$W | 184 | 110 | 83.1738 | 1472.9343 | -94.35 % | 172738.9713 | +8110.70 ppm |
| ${}^{185}$W | 185 | 111 | 89.5322 | 1478.6880 | -93.95 % | 173672.1783 | +8063.23 ppm |
| ${}^{186}$W | 186 | 112 | 95.8823 | 1485.8801 | -93.55 % | 174605.3936 | +8024.68 ppm |
| ${}^{187}$W | 187 | 113 | 102.2242 | 1491.3468 | -93.15 % | 175538.6171 | +7976.62 ppm |
| ${}^{188}$W | 188 | 114 | 108.5581 | 1498.1820 | -92.75 % | 176471.8487 | +7936.99 ppm |
| ${}^{189}$W | 189 | 115 | 114.8839 | 1503.3060 | -92.36 % | 177405.0882 | +7888.53 ppm |
| ${}^{190}$W | 190 | 116 | 121.2019 | 1510.0256 | -91.97 % | 178338.3357 | +7848.71 ppm |
| ${}^{191}$W | 191 | 117 | 127.5121 | 1514.9043 | -91.58 % | 179271.5909 | +7799.42 ppm |
| ${}^{192}$W | 192 | 118 | 133.8146 | 1521.4080 | -91.20 % | 180204.8539 | +7759.91 ppm |
| ${}^{193}$W | 193 | 119 | 140.1094 | 1526.0510 | -90.82 % | 181138.1244 | +7710.35 ppm |
| ${}^{194}$W | 194 | 120 | 146.3968 | 1532.4060 | -90.45 % | 182071.4025 | +7670.55 ppm |
| ${}^{195}$W | 195 | 121 | 152.6767 | 1536.7950 | -90.07 % | 183004.6880 | +7620.71 ppm |
| ${}^{196}$W | 196 | 122 | 158.9493 | 1542.9120 | -89.70 % | 183937.9808 | +7580.64 ppm |
| ${}^{197}$W | 197 | 123 | 165.2146 | 1547.0410 | -89.32 % | 184871.2809 | +7530.75 ppm |

### Rhenium (Z = 75)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{159}$Re | 159 | 84 | -100.7622 | 1239.4050 | -108.13 % | 149432.9893 | +9049.95 ppm |
| ${}^{160}$Re | 160 | 85 | -94.1183 | 1249.6000 | -107.53 % | 150365.9109 | +9017.00 ppm |
| ${}^{161}$Re | 161 | 86 | -87.4863 | 1261.6490 | -106.93 % | 151298.8443 | +8997.26 ppm |
| ${}^{162}$Re | 162 | 87 | -80.8660 | 1271.3760 | -106.36 % | 152231.7894 | +8962.10 ppm |
| ${}^{163}$Re | 163 | 88 | -74.2573 | 1282.9511 | -105.79 % | 153164.7461 | +8940.33 ppm |
| ${}^{164}$Re | 164 | 89 | -67.6598 | 1292.4926 | -105.23 % | 154097.7141 | +8905.17 ppm |
| ${}^{165}$Re | 165 | 90 | -61.0737 | 1303.7508 | -104.68 % | 155030.6933 | +8881.77 ppm |
| ${}^{166}$Re | 166 | 91 | -54.4985 | 1313.0001 | -104.15 % | 155963.6836 | +8845.62 ppm |
| ${}^{167}$Re | 167 | 92 | -47.9343 | 1324.1430 | -103.62 % | 156896.6848 | +8821.77 ppm |
| ${}^{168}$Re | 168 | 93 | -41.3808 | 1333.1003 | -103.10 % | 157829.6967 | +8785.15 ppm |
| ${}^{169}$Re | 169 | 94 | -34.8379 | 1343.7860 | -102.59 % | 158762.7193 | +8759.62 ppm |
| ${}^{170}$Re | 170 | 95 | -28.3055 | 1352.3520 | -102.09 % | 159695.7523 | +8720.95 ppm |
| ${}^{171}$Re | 171 | 96 | -21.7834 | 1362.7696 | -101.60 % | 160628.7957 | +8694.53 ppm |
| ${}^{172}$Re | 172 | 97 | -15.2716 | 1371.1575 | -101.11 % | 161561.8492 | +8655.70 ppm |
| ${}^{173}$Re | 173 | 98 | -8.7697 | 1381.2159 | -100.63 % | 162494.9128 | +8627.83 ppm |
| ${}^{174}$Re | 174 | 99 | -2.2778 | 1389.4064 | -100.16 % | 163427.9863 | +8588.73 ppm |
| ${}^{175}$Re | 175 | 100 | 4.2043 | 1399.0929 | -99.70 % | 164361.0696 | +8559.38 ppm |
| ${}^{176}$Re | 176 | 101 | 10.6767 | 1406.9388 | -99.24 % | 165294.1626 | +8519.10 ppm |
| ${}^{177}$Re | 177 | 102 | 17.1397 | 1416.2165 | -98.79 % | 166227.2651 | +8488.10 ppm |
| ${}^{178}$Re | 178 | 103 | 23.5931 | 1423.6721 | -98.34 % | 167160.3770 | +8446.41 ppm |
| ${}^{179}$Re | 179 | 104 | 30.0373 | 1432.6742 | -97.90 % | 168093.4983 | +8414.61 ppm |
| ${}^{180}$Re | 180 | 105 | 36.4724 | 1439.9986 | -97.47 % | 169026.6287 | +8373.11 ppm |
| ${}^{181}$Re | 181 | 106 | 42.8983 | 1448.7500 | -97.04 % | 169959.7681 | +8340.67 ppm |
| ${}^{182}$Re | 182 | 107 | 49.3153 | 1455.7500 | -96.61 % | 170892.9166 | +8298.22 ppm |
| ${}^{183}$Re | 183 | 108 | 55.7235 | 1464.1848 | -96.19 % | 171826.0738 | +8264.77 ppm |
| ${}^{184}$Re | 184 | 109 | 62.1229 | 1470.6663 | -95.78 % | 172759.2398 | +8220.24 ppm |
| ${}^{185}$Re | 185 | 110 | 68.5137 | 1478.3369 | -95.37 % | 173692.4144 | +8183.21 ppm |
| ${}^{186}$Re | 186 | 111 | 74.8961 | 1484.5165 | -94.95 % | 174625.5975 | +8137.94 ppm |
| ${}^{187}$Re | 187 | 112 | 81.2700 | 1491.8770 | -94.55 % | 175558.7890 | +8100.05 ppm |
| ${}^{188}$Re | 188 | 113 | 87.6355 | 1497.7486 | -94.15 % | 176491.9889 | +8054.03 ppm |
| ${}^{189}$Re | 189 | 114 | 93.9929 | 1504.7822 | -93.75 % | 177425.1969 | +8015.20 ppm |
| ${}^{190}$Re | 190 | 115 | 100.3422 | 1510.4574 | -93.36 % | 178358.4130 | +7969.09 ppm |
| ${}^{191}$Re | 191 | 116 | 106.6835 | 1517.2961 | -92.97 % | 179291.6372 | +7930.10 ppm |
| ${}^{192}$Re | 192 | 117 | 113.0169 | 1522.6059 | -92.58 % | 180224.8692 | +7882.94 ppm |
| ${}^{193}$Re | 193 | 118 | 119.3424 | 1529.3200 | -92.20 % | 181158.1091 | +7844.19 ppm |
| ${}^{194}$Re | 194 | 119 | 125.6602 | 1534.3460 | -91.81 % | 182091.3567 | +7796.88 ppm |
| ${}^{195}$Re | 195 | 120 | 131.9704 | 1540.6950 | -91.43 % | 183024.6120 | +7757.16 ppm |
| ${}^{196}$Re | 196 | 121 | 138.2730 | 1545.6560 | -91.05 % | 183957.8748 | +7709.59 ppm |
| ${}^{197}$Re | 197 | 122 | 144.5682 | 1551.7690 | -90.68 % | 184891.1450 | +7669.10 ppm |
| ${}^{198}$Re | 198 | 123 | 150.8560 | 1556.4780 | -90.31 % | 185824.4226 | +7621.68 ppm |
| ${}^{199}$Re | 199 | 124 | 157.1365 | 1562.1500 | -89.94 % | 186757.7075 | +7580.74 ppm |

### Osmium (Z = 76)

_43 of 43 isotopes with a framework prediction; 43 of 43 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{161}$Os | 161 | 85 | -109.6138 | 1250.1650 | -108.77 % | 151320.1895 | +9067.96 ppm |
| ${}^{162}$Os | 162 | 86 | -102.9545 | 1262.6280 | -108.15 % | 152253.0955 | +9050.12 ppm |
| ${}^{163}$Os | 163 | 87 | -96.3069 | 1272.5410 | -107.57 % | 153186.0134 | +9016.18 ppm |
| ${}^{164}$Os | 164 | 88 | -89.6710 | 1284.6625 | -106.98 % | 154118.9430 | +8997.60 ppm |
| ${}^{165}$Os | 165 | 89 | -83.0467 | 1294.0950 | -106.42 % | 155051.8840 | +8961.16 ppm |
| ${}^{166}$Os | 166 | 90 | -76.4337 | 1305.8120 | -105.85 % | 155984.8365 | +8940.64 ppm |
| ${}^{167}$Os | 167 | 91 | -69.8319 | 1314.9506 | -105.31 % | 156917.8001 | +8903.47 ppm |
| ${}^{168}$Os | 168 | 92 | -63.2411 | 1326.5181 | -104.77 % | 157850.7748 | +8882.47 ppm |
| ${}^{169}$Os | 169 | 93 | -56.6613 | 1335.3174 | -104.24 % | 158783.7603 | +8844.04 ppm |
| ${}^{170}$Os | 170 | 94 | -50.0922 | 1346.5914 | -103.72 % | 159716.7566 | +8821.91 ppm |
| ${}^{171}$Os | 171 | 95 | -43.5337 | 1355.0342 | -103.21 % | 160649.7636 | +8782.16 ppm |
| ${}^{172}$Os | 172 | 96 | -36.9857 | 1366.0520 | -102.71 % | 161582.7810 | +8759.15 ppm |
| ${}^{173}$Os | 173 | 97 | -30.4480 | 1374.3179 | -102.22 % | 162515.8087 | +8719.25 ppm |
| ${}^{174}$Os | 174 | 98 | -23.9205 | 1384.9464 | -101.73 % | 163448.8466 | +8694.57 ppm |
| ${}^{175}$Os | 175 | 99 | -17.4030 | 1393.1276 | -101.25 % | 164381.8946 | +8655.09 ppm |
| ${}^{176}$Os | 176 | 100 | -10.8955 | 1403.2248 | -100.78 % | 165314.9525 | +8627.91 ppm |
| ${}^{177}$Os | 177 | 101 | -4.3978 | 1411.1214 | -100.31 % | 166248.0202 | +8587.63 ppm |
| ${}^{178}$Os | 178 | 102 | 2.0903 | 1420.7805 | -99.85 % | 167181.0976 | +8558.58 ppm |
| ${}^{179}$Os | 179 | 103 | 8.5688 | 1428.3277 | -99.40 % | 168114.1845 | +8517.14 ppm |
| ${}^{180}$Os | 180 | 104 | 15.0379 | 1437.7351 | -98.95 % | 169047.2808 | +8487.41 ppm |
| ${}^{181}$Os | 181 | 105 | 21.4976 | 1445.0002 | -98.51 % | 169980.3865 | +8445.24 ppm |
| ${}^{182}$Os | 182 | 106 | 27.9482 | 1454.1306 | -98.08 % | 170913.5013 | +8414.69 ppm |
| ${}^{183}$Os | 183 | 107 | 34.3897 | 1461.2566 | -97.65 % | 171846.6253 | +8372.67 ppm |
| ${}^{184}$Os | 184 | 108 | 40.8222 | 1469.9167 | -97.22 % | 172779.7582 | +8340.18 ppm |
| ${}^{185}$Os | 185 | 109 | 47.2459 | 1476.5414 | -96.80 % | 173712.8999 | +8296.18 ppm |
| ${}^{186}$Os | 186 | 110 | 53.6608 | 1484.8068 | -96.39 % | 174646.0504 | +8262.26 ppm |
| ${}^{187}$Os | 187 | 111 | 60.0671 | 1491.0971 | -95.97 % | 175579.2095 | +8217.32 ppm |
| ${}^{188}$Os | 188 | 112 | 66.4649 | 1499.0867 | -95.57 % | 176512.3772 | +8182.69 ppm |
| ${}^{189}$Os | 189 | 113 | 72.8542 | 1505.0075 | -95.16 % | 177445.5532 | +8136.62 ppm |
| ${}^{190}$Os | 190 | 114 | 79.2353 | 1512.7999 | -94.76 % | 178378.7377 | +8101.75 ppm |
| ${}^{191}$Os | 191 | 115 | 85.6080 | 1518.5586 | -94.36 % | 179311.9303 | +8055.77 ppm |
| ${}^{192}$Os | 192 | 116 | 91.9727 | 1526.1170 | -93.97 % | 180245.1310 | +8020.45 ppm |
| ${}^{193}$Os | 193 | 117 | 98.3293 | 1531.7004 | -93.58 % | 181178.3398 | +7974.48 ppm |
| ${}^{194}$Os | 194 | 118 | 104.6780 | 1538.8125 | -93.20 % | 182111.5566 | +7937.55 ppm |
| ${}^{195}$Os | 195 | 119 | 111.0189 | 1543.9603 | -92.81 % | 183044.7811 | +7890.14 ppm |
| ${}^{196}$Os | 196 | 120 | 117.3520 | 1550.7971 | -92.43 % | 183978.0135 | +7852.58 ppm |
| ${}^{197}$Os | 197 | 121 | 123.6774 | 1555.7090 | -92.05 % | 184911.2535 | +7804.67 ppm |
| ${}^{198}$Os | 198 | 122 | 129.9953 | 1562.2200 | -91.68 % | 185844.5010 | +7766.67 ppm |
| ${}^{199}$Os | 199 | 123 | 136.3057 | 1566.9260 | -91.30 % | 186777.7561 | +7719.03 ppm |
| ${}^{200}$Os | 200 | 124 | 142.6086 | 1573.4000 | -90.94 % | 187711.0185 | +7680.62 ppm |
| ${}^{201}$Os | 201 | 125 | 148.9043 | 1577.6490 | -90.56 % | 188644.2883 | +7631.92 ppm |
| ${}^{202}$Os | 202 | 126 | 155.1927 | 1583.4780 | -90.20 % | 189577.5652 | +7591.24 ppm |
| ${}^{203}$Os | 203 | 127 | 161.4740 | 1586.2420 | -89.82 % | 190510.8494 | +7535.28 ppm |

### Iridium (Z = 77)

_43 of 43 isotopes with a framework prediction; 43 of 43 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{163}$Ir | 163 | 86 | -118.6164 | 1260.6420 | -109.41 % | 153207.5406 | +9084.69 ppm |
| ${}^{164}$Ir | 164 | 87 | -111.9416 | 1271.0000 | -108.81 % | 154140.4312 | +9052.79 ppm |
| ${}^{165}$Ir | 165 | 88 | -105.2786 | 1283.0400 | -108.21 % | 155073.3336 | +9034.08 ppm |
| ${}^{166}$Ir | 166 | 89 | -98.6272 | 1292.9740 | -107.63 % | 156006.2476 | +9000.00 ppm |
| ${}^{167}$Ir | 167 | 90 | -91.9873 | 1304.7418 | -107.05 % | 156939.1732 | +8979.74 ppm |
| ${}^{168}$Ir | 168 | 91 | -85.3588 | 1314.4070 | -106.49 % | 157872.1101 | +8945.78 ppm |
| ${}^{169}$Ir | 169 | 92 | -78.7415 | 1325.9055 | -105.94 % | 158805.0582 | +8924.04 ppm |
| ${}^{170}$Ir | 170 | 93 | -72.1352 | 1335.0100 | -105.40 % | 159738.0173 | +8887.73 ppm |
| ${}^{171}$Ir | 171 | 94 | -65.5398 | 1346.3667 | -104.87 % | 160670.9874 | +8865.48 ppm |
| ${}^{172}$Ir | 172 | 95 | -58.9552 | 1355.4054 | -104.35 % | 161603.9681 | +8829.30 ppm |
| ${}^{173}$Ir | 173 | 96 | -52.3811 | 1366.3658 | -103.83 % | 162536.9595 | +8805.63 ppm |
| ${}^{174}$Ir | 174 | 97 | -45.8175 | 1374.9546 | -103.33 % | 163469.9613 | +8767.54 ppm |
| ${}^{175}$Ir | 175 | 98 | -39.2643 | 1385.6345 | -102.83 % | 164402.9735 | +8742.89 ppm |
| ${}^{176}$Ir | 176 | 99 | -32.7212 | 1394.1932 | -102.35 % | 165335.9959 | +8705.53 ppm |
| ${}^{177}$Ir | 177 | 100 | -26.1882 | 1404.4300 | -101.86 % | 166269.0283 | +8678.92 ppm |
| ${}^{178}$Ir | 178 | 101 | -19.6651 | 1412.7082 | -101.39 % | 167202.0706 | +8640.75 ppm |
| ${}^{179}$Ir | 179 | 102 | -13.1519 | 1422.6069 | -100.92 % | 168135.1228 | +8612.87 ppm |
| ${}^{180}$Ir | 180 | 103 | -6.6483 | 1430.5741 | -100.46 % | 169068.1846 | +8573.74 ppm |
| ${}^{181}$Ir | 181 | 104 | -0.1543 | 1440.1309 | -100.01 % | 170001.2560 | +8544.60 ppm |
| ${}^{182}$Ir | 182 | 105 | 6.3303 | 1447.7909 | -99.56 % | 170934.3369 | +8504.56 ppm |
| ${}^{183}$Ir | 183 | 106 | 12.8056 | 1457.0126 | -99.12 % | 171867.4270 | +8474.25 ppm |
| ${}^{184}$Ir | 184 | 107 | 19.2717 | 1464.4927 | -98.68 % | 172800.5264 | +8434.07 ppm |
| ${}^{185}$Ir | 185 | 108 | 25.7286 | 1473.2887 | -98.25 % | 173733.6348 | +8402.08 ppm |
| ${}^{186}$Ir | 186 | 109 | 32.1766 | 1480.1968 | -97.83 % | 174666.7523 | +8359.50 ppm |
| ${}^{187}$Ir | 187 | 110 | 38.6158 | 1488.6451 | -97.41 % | 175599.8785 | +8326.34 ppm |
| ${}^{188}$Ir | 188 | 111 | 45.0461 | 1495.5120 | -96.99 % | 176533.0136 | +8284.48 ppm |
| ${}^{189}$Ir | 189 | 112 | 51.4679 | 1503.6880 | -96.58 % | 177466.1573 | +8250.60 ppm |
| ${}^{190}$Ir | 190 | 113 | 57.8810 | 1510.0633 | -96.17 % | 178399.3096 | +8206.88 ppm |
| ${}^{191}$Ir | 191 | 114 | 64.2857 | 1518.0899 | -95.77 % | 179332.4703 | +8173.02 ppm |
| ${}^{192}$Ir | 192 | 115 | 70.6821 | 1524.2880 | -95.36 % | 180265.6393 | +8129.25 ppm |
| ${}^{193}$Ir | 193 | 116 | 77.0703 | 1532.0600 | -94.97 % | 181198.8166 | +8094.80 ppm |
| ${}^{194}$Ir | 194 | 117 | 83.4502 | 1538.1268 | -94.57 % | 182132.0020 | +8051.25 ppm |
| ${}^{195}$Ir | 195 | 118 | 89.8222 | 1545.3586 | -94.19 % | 183065.1955 | +8014.65 ppm |
| ${}^{196}$Ir | 196 | 119 | 96.1861 | 1551.1731 | -93.80 % | 183998.3970 | +7970.64 ppm |
| ${}^{197}$Ir | 197 | 120 | 102.5422 | 1558.0731 | -93.42 % | 184931.6063 | +7933.09 ppm |
| ${}^{198}$Ir | 198 | 121 | 108.8906 | 1563.6060 | -93.04 % | 185864.8234 | +7888.40 ppm |
| ${}^{199}$Ir | 199 | 122 | 115.2312 | 1570.3501 | -92.66 % | 186798.0482 | +7850.96 ppm |
| ${}^{200}$Ir | 200 | 123 | 121.5643 | 1575.6000 | -92.28 % | 187731.2805 | +7805.73 ppm |
| ${}^{201}$Ir | 201 | 124 | 127.8898 | 1581.8700 | -91.92 % | 188664.5204 | +7766.90 ppm |
| ${}^{202}$Ir | 202 | 125 | 134.2079 | 1586.7100 | -91.54 % | 189597.7677 | +7720.63 ppm |
| ${}^{203}$Ir | 203 | 126 | 140.5187 | 1592.5350 | -91.18 % | 190531.0224 | +7679.81 ppm |
| ${}^{204}$Ir | 204 | 127 | 146.8222 | 1595.8920 | -90.80 % | 191464.2843 | +7626.01 ppm |
| ${}^{205}$Ir | 205 | 128 | 153.1185 | 1600.0250 | -90.43 % | 192397.5534 | +7577.15 ppm |

### Platinum (Z = 78)

_44 of 44 isotopes with a framework prediction; 44 of 44 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{165}$Pt | 165 | 87 | -127.7693 | 1270.9950 | -110.05 % | 155095.0420 | +9101.29 ppm |
| ${}^{166}$Pt | 166 | 88 | -121.0791 | 1283.6780 | -109.43 % | 156027.9172 | +9084.52 ppm |
| ${}^{167}$Pt | 167 | 89 | -114.4006 | 1293.5820 | -108.84 % | 156960.8042 | +9051.86 ppm |
| ${}^{168}$Pt | 168 | 90 | -107.7339 | 1305.9684 | -108.25 % | 157893.7028 | +9034.40 ppm |
| ${}^{169}$Pt | 169 | 91 | -101.0786 | 1315.4960 | -107.68 % | 158826.6129 | +8999.26 ppm |
| ${}^{170}$Pt | 170 | 92 | -94.4346 | 1327.4002 | -107.11 % | 159759.5344 | +8979.77 ppm |
| ${}^{171}$Pt | 171 | 93 | -87.8018 | 1336.6389 | -106.57 % | 160692.4670 | +8943.68 ppm |
| ${}^{172}$Pt | 172 | 94 | -81.1800 | 1348.3503 | -106.02 % | 161625.4107 | +8923.65 ppm |
| ${}^{173}$Pt | 173 | 95 | -74.5692 | 1357.2517 | -105.49 % | 162558.3652 | +8886.32 ppm |
| ${}^{174}$Pt | 174 | 96 | -67.9690 | 1368.7039 | -104.97 % | 163491.3305 | +8865.37 ppm |
| ${}^{175}$Pt | 175 | 97 | -61.3795 | 1377.1663 | -104.46 % | 164424.3064 | +8826.21 ppm |
| ${}^{176}$Pt | 176 | 98 | -54.8004 | 1388.4628 | -103.95 % | 165357.2927 | +8805.01 ppm |
| ${}^{177}$Pt | 177 | 99 | -48.2317 | 1396.9707 | -103.45 % | 166290.2894 | +8767.04 ppm |
| ${}^{178}$Pt | 178 | 100 | -41.6731 | 1407.6690 | -102.96 % | 167223.2963 | +8742.89 ppm |
| ${}^{179}$Pt | 179 | 101 | -35.1246 | 1416.0110 | -102.48 % | 168156.3132 | +8704.81 ppm |
| ${}^{180}$Pt | 180 | 102 | -28.5861 | 1426.2441 | -102.00 % | 169089.3401 | +8678.59 ppm |
| ${}^{181}$Pt | 181 | 103 | -22.0574 | 1434.2670 | -101.54 % | 170022.3768 | +8639.49 ppm |
| ${}^{182}$Pt | 182 | 104 | -15.5383 | 1444.1252 | -101.08 % | 170955.4232 | +8611.81 ppm |
| ${}^{183}$Pt | 183 | 105 | -9.0288 | 1451.8013 | -100.62 % | 171888.4791 | +8571.56 ppm |
| ${}^{184}$Pt | 184 | 106 | -2.5288 | 1461.4319 | -100.17 % | 172821.5445 | +8543.32 ppm |
| ${}^{185}$Pt | 185 | 107 | 3.9619 | 1468.8589 | -99.73 % | 173754.6192 | +8502.53 ppm |
| ${}^{186}$Pt | 186 | 108 | 10.4434 | 1478.1065 | -99.29 % | 174687.7031 | +8472.83 ppm |
| ${}^{187}$Pt | 187 | 109 | 16.9158 | 1484.9988 | -98.86 % | 175620.7961 | +8429.87 ppm |
| ${}^{188}$Pt | 188 | 110 | 23.3792 | 1494.2057 | -98.44 % | 176553.8982 | +8400.74 ppm |
| ${}^{189}$Pt | 189 | 111 | 29.8338 | 1500.9255 | -98.01 % | 177487.0091 | +8357.73 ppm |
| ${}^{190}$Pt | 190 | 112 | 36.2795 | 1509.8339 | -97.60 % | 178420.1287 | +8327.69 ppm |
| ${}^{191}$Pt | 191 | 113 | 42.7166 | 1516.2970 | -97.18 % | 179353.2571 | +8284.15 ppm |
| ${}^{192}$Pt | 192 | 114 | 49.1451 | 1524.9585 | -96.78 % | 180286.3940 | +8253.51 ppm |
| ${}^{193}$Pt | 193 | 115 | 55.5652 | 1531.2210 | -96.37 % | 181219.5394 | +8209.78 ppm |
| ${}^{194}$Pt | 194 | 116 | 61.9768 | 1539.5727 | -95.97 % | 182152.6931 | +8178.20 ppm |
| ${}^{195}$Pt | 195 | 117 | 68.3803 | 1545.6778 | -95.58 % | 183085.8551 | +8134.52 ppm |
| ${}^{196}$Pt | 196 | 118 | 74.7755 | 1553.5998 | -95.19 % | 184019.0253 | +8101.37 ppm |
| ${}^{197}$Pt | 197 | 119 | 81.1627 | 1559.4464 | -94.80 % | 184952.2035 | +8057.19 ppm |
| ${}^{198}$Pt | 198 | 120 | 87.5419 | 1567.0019 | -94.41 % | 185885.3897 | +8022.85 ppm |
| ${}^{199}$Pt | 199 | 121 | 93.9132 | 1572.5579 | -94.03 % | 186818.5838 | +7978.02 ppm |
| ${}^{200}$Pt | 200 | 122 | 100.2767 | 1579.8397 | -93.65 % | 187751.7858 | +7943.02 ppm |
| ${}^{201}$Pt | 201 | 123 | 106.6325 | 1585.0526 | -93.27 % | 188684.9954 | +7897.27 ppm |
| ${}^{202}$Pt | 202 | 124 | 112.9807 | 1592.0753 | -92.90 % | 189618.2126 | +7861.71 ppm |
| ${}^{203}$Pt | 203 | 125 | 119.3213 | 1597.0010 | -92.53 % | 190551.4374 | +7815.17 ppm |
| ${}^{204}$Pt | 204 | 126 | 125.6545 | 1603.2360 | -92.16 % | 191484.6696 | +7775.98 ppm |
| ${}^{205}$Pt | 205 | 127 | 131.9804 | 1606.3800 | -91.78 % | 192417.9092 | +7721.86 ppm |
| ${}^{206}$Pt | 206 | 128 | 138.2989 | 1610.9200 | -91.41 % | 193351.1561 | +7674.70 ppm |
| ${}^{207}$Pt | 207 | 129 | 144.6102 | 1613.9790 | -91.04 % | 194284.4102 | +7620.10 ppm |
| ${}^{208}$Pt | 208 | 130 | 150.9145 | 1618.2400 | -90.67 % | 195217.6714 | +7573.66 ppm |

### Gold (Z = 79)

_43 of 43 isotopes with a framework prediction; 43 of 43 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{168}$Au | 168 | 89 | -130.3662 | 1291.5840 | -110.09 % | 157915.5528 | +9086.72 ppm |
| ${}^{169}$Au | 169 | 90 | -123.6725 | 1304.0040 | -109.48 % | 158848.4245 | +9069.39 ppm |
| ${}^{170}$Au | 170 | 91 | -116.9903 | 1314.1000 | -108.90 % | 159781.3078 | +9037.01 ppm |
| ${}^{171}$Au | 171 | 92 | -110.3197 | 1325.9523 | -108.32 % | 160714.2025 | +9017.40 ppm |
| ${}^{172}$Au | 172 | 93 | -103.6603 | 1335.7793 | -107.76 % | 161647.1086 | +8984.84 ppm |
| ${}^{173}$Au | 173 | 94 | -97.0121 | 1347.3646 | -107.20 % | 162580.0258 | +8963.74 ppm |
| ${}^{174}$Au | 174 | 95 | -90.3750 | 1356.6780 | -106.66 % | 163512.9541 | +8928.70 ppm |
| ${}^{175}$Au | 175 | 96 | -83.7487 | 1368.0789 | -106.12 % | 164445.8932 | +8907.25 ppm |
| ${}^{176}$Au | 176 | 97 | -77.1331 | 1377.2675 | -105.60 % | 165378.8431 | +8872.39 ppm |
| ${}^{177}$Au | 177 | 98 | -70.5282 | 1388.3636 | -105.08 % | 166311.8036 | +8849.66 ppm |
| ${}^{178}$Au | 178 | 99 | -63.9337 | 1397.1922 | -104.58 % | 167244.7745 | +8813.46 ppm |
| ${}^{179}$Au | 179 | 100 | -57.3495 | 1407.9491 | -104.07 % | 168177.7558 | +8789.38 ppm |
| ${}^{180}$Au | 180 | 101 | -50.7755 | 1416.6575 | -103.58 % | 169110.7472 | +8753.31 ppm |
| ${}^{181}$Au | 181 | 102 | -44.2116 | 1426.9743 | -103.10 % | 170043.7487 | +8727.32 ppm |
| ${}^{182}$Au | 182 | 103 | -37.6577 | 1435.4784 | -102.62 % | 170976.7602 | +8690.89 ppm |
| ${}^{183}$Au | 183 | 104 | -31.1135 | 1445.4373 | -102.15 % | 171909.7815 | +8663.52 ppm |
| ${}^{184}$Au | 184 | 105 | -24.5791 | 1453.6358 | -101.69 % | 172842.8124 | +8626.15 ppm |
| ${}^{185}$Au | 185 | 106 | -18.0542 | 1463.2466 | -101.23 % | 173775.8530 | +8597.50 ppm |
| ${}^{186}$Au | 186 | 107 | -11.5387 | 1471.1746 | -100.78 % | 174708.9030 | +8559.41 ppm |
| ${}^{187}$Au | 187 | 108 | -5.0326 | 1480.5598 | -100.34 % | 175641.9623 | +8530.23 ppm |
| ${}^{188}$Au | 188 | 109 | 1.4642 | 1487.9737 | -99.90 % | 176575.0308 | +8490.05 ppm |
| ${}^{189}$Au | 189 | 110 | 7.9520 | 1497.2557 | -99.47 % | 177508.1085 | +8461.06 ppm |
| ${}^{190}$Au | 190 | 111 | 14.4307 | 1504.5786 | -99.04 % | 178441.1952 | +8421.25 ppm |
| ${}^{191}$Au | 191 | 112 | 20.9006 | 1513.6142 | -98.62 % | 179374.2907 | +8391.62 ppm |
| ${}^{192}$Au | 192 | 113 | 27.3617 | 1520.6598 | -98.20 % | 180307.3951 | +8351.13 ppm |
| ${}^{193}$Au | 193 | 114 | 33.8140 | 1529.3638 | -97.79 % | 181240.5081 | +8320.41 ppm |
| ${}^{194}$Au | 194 | 115 | 40.2578 | 1536.2422 | -97.38 % | 182173.6298 | +8279.86 ppm |
| ${}^{195}$Au | 195 | 116 | 46.6932 | 1544.6687 | -96.98 % | 183106.7599 | +8248.37 ppm |
| ${}^{196}$Au | 196 | 117 | 53.1201 | 1551.3116 | -96.58 % | 184039.8983 | +8207.40 ppm |
| ${}^{197}$Au | 197 | 118 | 59.5388 | 1559.3840 | -96.18 % | 184973.0451 | +8174.74 ppm |
| ${}^{198}$Au | 198 | 119 | 65.9492 | 1565.8964 | -95.79 % | 185906.2001 | +8133.93 ppm |
| ${}^{199}$Au | 199 | 120 | 72.3516 | 1573.4806 | -95.40 % | 186839.3631 | +8099.41 ppm |
| ${}^{200}$Au | 200 | 121 | 78.7460 | 1579.6983 | -95.02 % | 187772.5342 | +8057.88 ppm |
| ${}^{201}$Au | 201 | 122 | 85.1324 | 1586.9302 | -94.64 % | 188705.7131 | +8022.26 ppm |
| ${}^{202}$Au | 202 | 123 | 91.5111 | 1592.9538 | -94.26 % | 189638.8999 | +7980.57 ppm |
| ${}^{203}$Au | 203 | 124 | 97.8820 | 1599.8156 | -93.88 % | 190572.0944 | +7943.80 ppm |
| ${}^{204}$Au | 204 | 125 | 104.2452 | 1605.0720 | -93.51 % | 191505.2966 | +7899.24 ppm |
| ${}^{205}$Au | 205 | 126 | 110.6009 | 1611.3000 | -93.14 % | 192438.5063 | +7860.08 ppm |
| ${}^{206}$Au | 206 | 127 | 116.9492 | 1615.0400 | -92.76 % | 193371.7235 | +7807.89 ppm |
| ${}^{207}$Au | 207 | 128 | 123.2900 | 1619.5680 | -92.39 % | 194304.9481 | +7760.59 ppm |
| ${}^{208}$Au | 208 | 129 | 129.6235 | 1623.0240 | -92.01 % | 195238.1800 | +7707.65 ppm |
| ${}^{209}$Au | 209 | 130 | 135.9498 | 1627.2740 | -91.65 % | 196171.4191 | +7660.68 ppm |
| ${}^{210}$Au | 210 | 131 | 142.2690 | 1630.4400 | -91.27 % | 197104.6654 | +7607.87 ppm |

### Mercury (Z = 80)

_47 of 47 isotopes with a framework prediction; 47 of 47 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{170}$Hg | 170 | 90 | -139.8024 | 1304.0700 | -110.72 % | 159803.3375 | +9118.02 ppm |
| ${}^{171}$Hg | 171 | 91 | -133.0934 | 1314.3060 | -110.13 % | 160736.1939 | +9086.40 ppm |
| ${}^{172}$Hg | 172 | 92 | -126.3960 | 1326.7403 | -109.53 % | 161669.0619 | +9069.87 ppm |
| ${}^{173}$Hg | 173 | 93 | -119.7100 | 1336.4250 | -108.96 % | 162601.9414 | +9036.06 ppm |
| ${}^{174}$Hg | 174 | 94 | -113.0353 | 1348.4626 | -108.38 % | 163534.8321 | +9017.52 ppm |
| ${}^{175}$Hg | 175 | 95 | -106.3718 | 1357.8623 | -107.83 % | 164467.7340 | +8982.85 ppm |
| ${}^{176}$Hg | 176 | 96 | -99.7193 | 1369.7489 | -107.28 % | 165400.6470 | +8963.94 ppm |
| ${}^{177}$Hg | 177 | 97 | -93.0777 | 1378.8114 | -106.75 % | 166333.5708 | +8928.03 ppm |
| ${}^{178}$Hg | 178 | 98 | -86.4468 | 1390.4222 | -106.22 % | 167266.5053 | +8908.10 ppm |
| ${}^{179}$Hg | 179 | 99 | -79.8265 | 1399.1111 | -105.71 % | 168199.4504 | +8870.77 ppm |
| ${}^{180}$Hg | 180 | 100 | -73.2166 | 1410.5000 | -105.19 % | 169132.4060 | +8850.16 ppm |
| ${}^{181}$Hg | 181 | 101 | -66.6171 | 1418.9819 | -104.69 % | 170065.3719 | +8812.45 ppm |
| ${}^{182}$Hg | 182 | 102 | -60.0278 | 1429.9690 | -104.20 % | 170998.3480 | +8790.12 ppm |
| ${}^{183}$Hg | 183 | 103 | -53.4485 | 1438.2681 | -103.72 % | 171931.3341 | +8752.18 ppm |
| ${}^{184}$Hg | 184 | 104 | -46.8792 | 1448.8796 | -103.24 % | 172864.3302 | +8728.32 ppm |
| ${}^{185}$Hg | 185 | 105 | -40.3197 | 1456.7897 | -102.77 % | 173797.3362 | +8688.96 ppm |
| ${}^{186}$Hg | 186 | 106 | -33.7699 | 1467.2165 | -102.30 % | 174730.3518 | +8664.74 ppm |
| ${}^{187}$Hg | 187 | 107 | -27.2297 | 1474.8672 | -101.85 % | 175663.3770 | +8624.75 ppm |
| ${}^{188}$Hg | 188 | 108 | -20.6989 | 1485.0184 | -101.39 % | 176596.4116 | +8599.65 ppm |
| ${}^{189}$Hg | 189 | 109 | -14.1775 | 1492.5177 | -100.95 % | 177529.4557 | +8559.67 ppm |
| ${}^{190}$Hg | 190 | 110 | -7.6653 | 1502.3333 | -100.51 % | 178462.5089 | +8533.36 ppm |
| ${}^{191}$Hg | 191 | 111 | -1.1623 | 1509.6258 | -100.08 % | 179395.5713 | +8493.08 ppm |
| ${}^{192}$Hg | 192 | 112 | 5.3318 | 1519.1168 | -99.65 % | 180328.6427 | +8465.66 ppm |
| ${}^{193}$Hg | 193 | 113 | 11.8169 | 1526.2388 | -99.23 % | 181261.7229 | +8425.29 ppm |
| ${}^{194}$Hg | 194 | 114 | 18.2932 | 1535.4319 | -98.81 % | 182194.8120 | +8396.94 ppm |
| ${}^{195}$Hg | 195 | 115 | 24.7609 | 1542.3326 | -98.39 % | 183127.9098 | +8356.20 ppm |
| ${}^{196}$Hg | 196 | 116 | 31.2199 | 1551.2165 | -97.99 % | 184061.0162 | +8326.88 ppm |
| ${}^{197}$Hg | 197 | 117 | 37.6704 | 1558.0021 | -97.58 % | 184994.1311 | +8286.38 ppm |
| ${}^{198}$Hg | 198 | 118 | 44.1126 | 1566.4875 | -97.18 % | 185927.2544 | +8255.62 ppm |
| ${}^{199}$Hg | 199 | 119 | 50.5464 | 1573.1506 | -96.79 % | 186860.3860 | +8215.30 ppm |
| ${}^{200}$Hg | 200 | 120 | 56.9720 | 1581.1791 | -96.40 % | 187793.5258 | +8182.82 ppm |
| ${}^{201}$Hg | 201 | 121 | 63.3895 | 1587.4097 | -96.01 % | 188726.6737 | +8141.02 ppm |
| ${}^{202}$Hg | 202 | 122 | 69.7990 | 1595.1638 | -95.62 % | 189659.8296 | +8107.85 ppm |
| ${}^{203}$Hg | 203 | 123 | 76.2006 | 1601.1590 | -95.24 % | 190592.9935 | +8065.67 ppm |
| ${}^{204}$Hg | 204 | 124 | 82.5943 | 1608.6513 | -94.87 % | 191526.1652 | +8031.88 ppm |
| ${}^{205}$Hg | 205 | 125 | 88.9803 | 1614.3202 | -94.49 % | 192459.3446 | +7988.84 ppm |
| ${}^{206}$Hg | 206 | 126 | 95.3586 | 1621.0495 | -94.12 % | 193392.5318 | +7951.83 ppm |
| ${}^{207}$Hg | 207 | 127 | 101.7293 | 1624.6625 | -93.74 % | 194325.7265 | +7898.92 ppm |
| ${}^{208}$Hg | 208 | 128 | 108.0925 | 1629.5118 | -93.37 % | 195258.9287 | +7853.00 ppm |
| ${}^{209}$Hg | 209 | 129 | 114.4483 | 1632.9170 | -92.99 % | 196192.1383 | +7800.13 ppm |
| ${}^{210}$Hg | 210 | 130 | 120.7968 | 1637.7900 | -92.62 % | 197125.3552 | +7754.74 ppm |
| ${}^{211}$Hg | 211 | 131 | 127.1380 | 1640.9470 | -92.25 % | 198058.5795 | +7701.62 ppm |
| ${}^{212}$Hg | 212 | 132 | 133.4720 | 1645.5440 | -91.89 % | 198991.8108 | +7656.69 ppm |
| ${}^{213}$Hg | 213 | 133 | 139.7990 | 1648.4070 | -91.52 % | 199925.0493 | +7603.23 ppm |
| ${}^{214}$Hg | 214 | 134 | 146.1189 | 1652.9360 | -91.16 % | 200858.2948 | +7558.44 ppm |
| ${}^{215}$Hg | 215 | 135 | 152.4318 | 1655.7150 | -90.79 % | 201791.5473 | +7505.21 ppm |
| ${}^{216}$Hg | 216 | 136 | 158.7379 | 1659.9600 | -90.44 % | 202724.8066 | +7460.16 ppm |

### Thallium (Z = 81)

_43 of 43 isotopes with a framework prediction; 43 of 43 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{176}$Tl | 176 | 95 | -122.5590 | 1356.5971 | -109.03 % | 165422.7043 | +9022.36 ppm |
| ${}^{177}$Tl | 177 | 96 | -115.8802 | 1368.5933 | -108.47 % | 166355.5910 | +9003.85 ppm |
| ${}^{178}$Tl | 178 | 97 | -109.2125 | 1377.8980 | -107.93 % | 167288.4886 | +8969.48 ppm |
| ${}^{179}$Tl | 179 | 98 | -102.5556 | 1389.6655 | -107.38 % | 168221.3972 | +8949.98 ppm |
| ${}^{180}$Tl | 180 | 99 | -95.9094 | 1398.8576 | -106.86 % | 169154.3164 | +8915.50 ppm |
| ${}^{181}$Tl | 181 | 100 | -89.2738 | 1410.3372 | -106.33 % | 170087.2462 | +8895.15 ppm |
| ${}^{182}$Tl | 182 | 101 | -82.6487 | 1418.9370 | -105.82 % | 171020.1865 | +8857.95 ppm |
| ${}^{183}$Tl | 183 | 102 | -76.0338 | 1430.2684 | -105.32 % | 171953.1371 | +8837.38 ppm |
| ${}^{184}$Tl | 184 | 103 | -69.4292 | 1438.6358 | -104.83 % | 172886.0979 | +8799.65 ppm |
| ${}^{185}$Tl | 185 | 104 | -62.8347 | 1449.5815 | -104.33 % | 173819.0688 | +8777.48 ppm |
| ${}^{186}$Tl | 186 | 105 | -56.2501 | 1457.7780 | -103.86 % | 174752.0496 | +8739.59 ppm |
| ${}^{187}$Tl | 187 | 106 | -49.6753 | 1468.4110 | -103.38 % | 175685.0402 | +8716.28 ppm |
| ${}^{188}$Tl | 188 | 107 | -43.1102 | 1476.3741 | -102.92 % | 176618.0406 | +8677.89 ppm |
| ${}^{189}$Tl | 189 | 108 | -36.5547 | 1486.7251 | -102.46 % | 177551.0505 | +8653.64 ppm |
| ${}^{190}$Tl | 190 | 109 | -30.0087 | 1494.5466 | -102.01 % | 178484.0699 | +8615.28 ppm |
| ${}^{191}$Tl | 191 | 110 | -23.4720 | 1504.5346 | -101.56 % | 179417.0986 | +8589.67 ppm |
| ${}^{192}$Tl | 192 | 111 | -16.9446 | 1512.1952 | -101.12 % | 180350.1366 | +8551.24 ppm |
| ${}^{193}$Tl | 193 | 112 | -10.4263 | 1521.8715 | -100.69 % | 181283.1838 | +8524.57 ppm |
| ${}^{194}$Tl | 194 | 113 | -3.9170 | 1529.4031 | -100.26 % | 182216.2399 | +8486.25 ppm |
| ${}^{195}$Tl | 195 | 114 | 2.5834 | 1538.6922 | -99.83 % | 183149.3050 | +8458.14 ppm |
| ${}^{196}$Tl | 196 | 115 | 9.0749 | 1546.1048 | -99.41 % | 184082.3789 | +8420.00 ppm |
| ${}^{197}$Tl | 197 | 116 | 15.5577 | 1555.0338 | -99.00 % | 185015.4615 | +8390.62 ppm |
| ${}^{198}$Tl | 198 | 117 | 22.0319 | 1562.2796 | -98.59 % | 185948.5527 | +8352.38 ppm |
| ${}^{199}$Tl | 199 | 118 | 28.4976 | 1570.8816 | -98.19 % | 186881.6524 | +8321.96 ppm |
| ${}^{200}$Tl | 200 | 119 | 34.9549 | 1577.9407 | -97.78 % | 187814.7606 | +8283.53 ppm |
| ${}^{201}$Tl | 201 | 120 | 41.4039 | 1586.1456 | -97.39 % | 188747.8770 | +8251.69 ppm |
| ${}^{202}$Tl | 202 | 121 | 47.8446 | 1593.0166 | -97.00 % | 189681.0017 | +8213.07 ppm |
| ${}^{203}$Tl | 203 | 122 | 54.2772 | 1600.8688 | -96.61 % | 190614.1345 | +8180.11 ppm |
| ${}^{204}$Tl | 204 | 123 | 60.7018 | 1607.5249 | -96.22 % | 191547.2754 | +8141.16 ppm |
| ${}^{205}$Tl | 205 | 124 | 67.1184 | 1615.0709 | -95.84 % | 192480.4242 | +8107.34 ppm |
| ${}^{206}$Tl | 206 | 125 | 73.5271 | 1621.5747 | -95.47 % | 193413.5809 | +8068.40 ppm |
| ${}^{207}$Tl | 207 | 126 | 79.9281 | 1628.4272 | -95.09 % | 194346.7453 | +8031.71 ppm |
| ${}^{208}$Tl | 208 | 127 | 86.3214 | 1632.2142 | -94.71 % | 195279.9175 | +7979.47 ppm |
| ${}^{209}$Tl | 209 | 128 | 92.7071 | 1637.1802 | -94.34 % | 196213.0972 | +7933.86 ppm |
| ${}^{210}$Tl | 210 | 129 | 99.0852 | 1640.8537 | -93.96 % | 197146.2845 | +7882.08 ppm |
| ${}^{211}$Tl | 211 | 130 | 105.4560 | 1645.7560 | -93.59 % | 198079.4792 | +7837.12 ppm |
| ${}^{212}$Tl | 212 | 131 | 111.8193 | 1649.3600 | -93.22 % | 199012.6812 | +7785.70 ppm |
| ${}^{213}$Tl | 213 | 132 | 118.1754 | 1654.0368 | -92.86 % | 199945.8906 | +7740.85 ppm |
| ${}^{214}$Tl | 214 | 133 | 124.5243 | 1657.4300 | -92.49 % | 200879.1071 | +7689.66 ppm |
| ${}^{215}$Tl | 215 | 134 | 130.8660 | 1661.9500 | -92.13 % | 201812.3308 | +7644.59 ppm |
| ${}^{216}$Tl | 216 | 135 | 137.2007 | 1665.1440 | -91.76 % | 202745.5615 | +7593.59 ppm |
| ${}^{217}$Tl | 217 | 136 | 143.5285 | 1669.3810 | -91.40 % | 203678.7992 | +7548.34 ppm |
| ${}^{218}$Tl | 218 | 137 | 149.8493 | 1672.4960 | -91.04 % | 204612.0438 | +7497.28 ppm |

### Lead (Z = 82)

_43 of 43 isotopes with a framework prediction; 43 of 43 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{178}$Pb | 178 | 96 | -132.2307 | 1368.9688 | -109.66 % | 167310.7245 | +9053.77 ppm |
| ${}^{179}$Pb | 179 | 97 | -125.5368 | 1378.5619 | -109.11 % | 168243.5960 | +9020.66 ppm |
| ${}^{180}$Pb | 180 | 98 | -118.8538 | 1390.6259 | -108.55 % | 169176.4785 | +9002.85 ppm |
| ${}^{181}$Pb | 181 | 99 | -112.1817 | 1399.8667 | -108.01 % | 170109.3718 | +8968.41 ppm |
| ${}^{182}$Pb | 182 | 100 | -105.5203 | 1411.6520 | -107.47 % | 171042.2758 | +8949.55 ppm |
| ${}^{183}$Pb | 183 | 101 | -98.8695 | 1420.4788 | -106.96 % | 171975.1904 | +8913.45 ppm |
| ${}^{184}$Pb | 184 | 102 | -92.2291 | 1432.0217 | -106.44 % | 172908.1155 | +8893.79 ppm |
| ${}^{185}$Pb | 185 | 103 | -85.5990 | 1440.5826 | -105.94 % | 173841.0508 | +8856.94 ppm |
| ${}^{186}$Pb | 186 | 104 | -78.9792 | 1451.7936 | -105.44 % | 174773.9964 | +8835.98 ppm |
| ${}^{187}$Pb | 187 | 105 | -72.3694 | 1460.1710 | -104.96 % | 175706.9520 | +8798.89 ppm |
| ${}^{188}$Pb | 188 | 106 | -65.7696 | 1471.0664 | -104.47 % | 176639.9176 | +8776.76 ppm |
| ${}^{189}$Pb | 189 | 107 | -59.1796 | 1479.1707 | -104.00 % | 177572.8930 | +8738.92 ppm |
| ${}^{190}$Pb | 190 | 108 | -52.5993 | 1489.8146 | -103.53 % | 178505.8782 | +8716.01 ppm |
| ${}^{191}$Pb | 191 | 109 | -46.0285 | 1497.7605 | -103.07 % | 179438.8729 | +8678.09 ppm |
| ${}^{192}$Pb | 192 | 110 | -39.4673 | 1508.0925 | -102.62 % | 180371.8771 | +8654.09 ppm |
| ${}^{193}$Pb | 193 | 111 | -32.9154 | 1515.8412 | -102.17 % | 181304.8906 | +8615.88 ppm |
| ${}^{194}$Pb | 194 | 112 | -26.3728 | 1525.8911 | -101.73 % | 182237.9134 | +8590.97 ppm |
| ${}^{195}$Pb | 195 | 113 | -19.8393 | 1533.4926 | -101.29 % | 183170.9453 | +8552.77 ppm |
| ${}^{196}$Pb | 196 | 114 | -13.3149 | 1543.1741 | -100.86 % | 184103.9863 | +8526.49 ppm |
| ${}^{197}$Pb | 197 | 115 | -6.7994 | 1550.6426 | -100.44 % | 185037.0362 | +8488.37 ppm |
| ${}^{198}$Pb | 198 | 116 | -0.2927 | 1560.0360 | -100.02 % | 185970.0950 | +8461.21 ppm |
| ${}^{199}$Pb | 199 | 117 | 6.2053 | 1567.2716 | -99.60 % | 186903.1624 | +8422.63 ppm |
| ${}^{200}$Pb | 200 | 118 | 12.6946 | 1576.3620 | -99.19 % | 187836.2385 | +8394.52 ppm |
| ${}^{201}$Pb | 201 | 119 | 19.1754 | 1583.4535 | -98.79 % | 188769.3232 | +8355.97 ppm |
| ${}^{202}$Pb | 202 | 120 | 25.6478 | 1592.1944 | -98.39 % | 189702.4162 | +8326.68 ppm |
| ${}^{203}$Pb | 203 | 121 | 32.1118 | 1599.1116 | -97.99 % | 190635.5176 | +8288.01 ppm |
| ${}^{204}$Pb | 204 | 122 | 38.5676 | 1607.5063 | -97.60 % | 191568.6272 | +8257.59 ppm |
| ${}^{205}$Pb | 205 | 123 | 45.0152 | 1614.2379 | -97.21 % | 192501.7450 | +8218.74 ppm |
| ${}^{206}$Pb | 206 | 124 | 51.4548 | 1622.3246 | -96.83 % | 193434.8709 | +8187.42 ppm |
| ${}^{207}$Pb | 207 | 125 | 57.8864 | 1629.0623 | -96.45 % | 194368.0047 | +8149.39 ppm |
| ${}^{208}$Pb | 208 | 126 | 64.3102 | 1636.4302 | -96.07 % | 195301.1464 | +8115.05 ppm |
| ${}^{209}$Pb | 209 | 127 | 70.7261 | 1640.3676 | -95.69 % | 196234.2958 | +8063.32 ppm |
| ${}^{210}$Pb | 210 | 128 | 77.1343 | 1645.5528 | -95.31 % | 197167.4530 | +8018.55 ppm |
| ${}^{211}$Pb | 211 | 129 | 83.5349 | 1649.3887 | -94.94 % | 198100.6179 | +7967.32 ppm |
| ${}^{212}$Pb | 212 | 130 | 89.9280 | 1654.5159 | -94.56 % | 199033.7902 | +7923.21 ppm |
| ${}^{213}$Pb | 213 | 131 | 96.3136 | 1658.2419 | -94.19 % | 199966.9701 | +7872.43 ppm |
| ${}^{214}$Pb | 214 | 132 | 102.6918 | 1663.2926 | -93.83 % | 200900.1573 | +7828.86 ppm |
| ${}^{215}$Pb | 215 | 133 | 109.0627 | 1666.8387 | -93.46 % | 201833.3518 | +7778.17 ppm |
| ${}^{216}$Pb | 216 | 134 | 115.4264 | 1671.8400 | -93.10 % | 202766.5535 | +7734.78 ppm |
| ${}^{217}$Pb | 217 | 135 | 121.7829 | 1675.0230 | -92.73 % | 203699.7624 | +7683.94 ppm |
| ${}^{218}$Pb | 218 | 136 | 128.1323 | 1679.6900 | -92.37 % | 204632.9784 | +7640.46 ppm |
| ${}^{219}$Pb | 219 | 137 | 134.4748 | 1682.7960 | -92.01 % | 205566.2014 | +7589.40 ppm |
| ${}^{220}$Pb | 220 | 138 | 140.8103 | 1687.4000 | -91.66 % | 206499.4313 | +7546.12 ppm |

### Bismuth (Z = 83)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{184}$Bi | 184 | 101 | -115.2788 | 1419.0080 | -108.12 % | 172930.3829 | +8951.27 ppm |
| ${}^{185}$Bi | 185 | 102 | -108.6129 | 1430.4200 | -107.59 % | 173863.2823 | +8931.47 ppm |
| ${}^{186}$Bi | 186 | 103 | -101.9573 | 1439.4759 | -107.08 % | 174796.1922 | +8896.92 ppm |
| ${}^{187}$Bi | 187 | 104 | -95.3121 | 1450.7850 | -106.57 % | 175729.1124 | +8876.29 ppm |
| ${}^{188}$Bi | 188 | 105 | -88.6771 | 1459.6678 | -106.08 % | 176662.0428 | +8841.95 ppm |
| ${}^{189}$Bi | 189 | 106 | -82.0521 | 1470.6090 | -105.58 % | 177594.9833 | +8819.82 ppm |
| ${}^{190}$Bi | 190 | 107 | -75.4371 | 1479.2115 | -105.10 % | 178527.9337 | +8784.66 ppm |
| ${}^{191}$Bi | 191 | 108 | -68.8320 | 1489.9263 | -104.62 % | 179460.8939 | +8761.89 ppm |
| ${}^{192}$Bi | 192 | 109 | -62.2365 | 1498.2928 | -104.15 % | 180393.8639 | +8726.17 ppm |
| ${}^{193}$Bi | 193 | 110 | -55.6506 | 1508.7142 | -103.69 % | 181326.8435 | +8702.41 ppm |
| ${}^{194}$Bi | 194 | 111 | -49.0742 | 1516.9239 | -103.24 % | 182259.8325 | +8666.59 ppm |
| ${}^{195}$Bi | 195 | 112 | -42.5072 | 1526.9978 | -102.78 % | 183192.8309 | +8641.55 ppm |
| ${}^{196}$Bi | 196 | 113 | -35.9495 | 1535.0526 | -102.34 % | 184125.8386 | +8605.65 ppm |
| ${}^{197}$Bi | 197 | 114 | -29.4009 | 1544.8021 | -101.90 % | 185058.8554 | +8579.49 ppm |
| ${}^{198}$Bi | 198 | 115 | -22.8613 | 1552.5600 | -101.47 % | 185991.8812 | +8542.74 ppm |
| ${}^{199}$Bi | 199 | 116 | -16.3307 | 1562.0551 | -101.05 % | 186924.9161 | +8515.87 ppm |
| ${}^{200}$Bi | 200 | 117 | -9.8089 | 1569.6994 | -100.62 % | 187857.9597 | +8479.29 ppm |
| ${}^{201}$Bi | 201 | 118 | -3.2959 | 1578.8291 | -100.21 % | 188791.0121 | +8451.13 ppm |
| ${}^{202}$Bi | 202 | 119 | 3.2085 | 1586.2223 | -99.80 % | 189724.0731 | +8413.98 ppm |
| ${}^{203}$Bi | 203 | 120 | 9.7044 | 1595.0677 | -99.39 % | 190657.1427 | +8384.99 ppm |
| ${}^{204}$Bi | 204 | 121 | 16.1918 | 1602.2600 | -98.99 % | 191590.2207 | +8347.55 ppm |
| ${}^{205}$Bi | 205 | 122 | 22.6708 | 1610.7510 | -98.59 % | 192523.3071 | +8317.38 ppm |
| ${}^{206}$Bi | 206 | 123 | 29.1416 | 1617.7849 | -98.20 % | 193456.4017 | +8279.89 ppm |
| ${}^{207}$Bi | 207 | 124 | 35.6043 | 1625.8826 | -97.81 % | 194389.5045 | +8248.37 ppm |
| ${}^{208}$Bi | 208 | 125 | 42.0588 | 1632.7695 | -97.42 % | 195322.6154 | +8210.89 ppm |
| ${}^{209}$Bi | 209 | 126 | 48.5054 | 1640.2293 | -97.04 % | 196255.7342 | +8176.78 ppm |
| ${}^{210}$Bi | 210 | 127 | 54.9440 | 1644.8339 | -96.66 % | 197188.8610 | +8128.32 ppm |
| ${}^{211}$Bi | 211 | 128 | 61.3749 | 1649.9724 | -96.28 % | 198121.9956 | +8083.10 ppm |
| ${}^{212}$Bi | 212 | 129 | 67.7980 | 1654.3026 | -95.90 % | 199055.1379 | +8034.22 ppm |
| ${}^{213}$Bi | 213 | 130 | 74.2135 | 1659.4876 | -95.53 % | 199988.2878 | +7990.18 ppm |
| ${}^{214}$Bi | 214 | 131 | 80.6214 | 1663.5280 | -95.15 % | 200921.4453 | +7940.80 ppm |
| ${}^{215}$Bi | 215 | 132 | 87.0218 | 1668.7693 | -94.79 % | 201854.6103 | +7897.97 ppm |
| ${}^{216}$Bi | 216 | 133 | 93.4148 | 1672.5959 | -94.41 % | 202787.7828 | +7848.48 ppm |
| ${}^{217}$Bi | 217 | 134 | 99.8005 | 1677.8113 | -94.05 % | 203720.9625 | +7806.42 ppm |
| ${}^{218}$Bi | 218 | 135 | 106.1789 | 1681.3965 | -93.69 % | 204654.1495 | +7756.68 ppm |
| ${}^{219}$Bi | 219 | 136 | 112.5502 | 1686.3000 | -93.33 % | 205587.3436 | +7714.27 ppm |
| ${}^{220}$Bi | 220 | 137 | 118.9144 | 1689.8200 | -92.96 % | 206520.5449 | +7664.72 ppm |
| ${}^{221}$Bi | 221 | 138 | 125.2715 | 1694.6280 | -92.61 % | 207453.7532 | +7622.51 ppm |
| ${}^{222}$Bi | 222 | 139 | 131.6217 | 1697.8560 | -92.25 % | 208386.9684 | +7573.36 ppm |
| ${}^{223}$Bi | 223 | 140 | 137.9650 | 1702.8280 | -91.90 % | 209320.1905 | +7531.77 ppm |
| ${}^{224}$Bi | 224 | 141 | 144.3015 | 1705.9840 | -91.54 % | 210253.4194 | +7483.14 ppm |

### Polonium (Z = 84)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{186}$Po | 186 | 102 | -125.1844 | 1431.4465 | -108.75 % | 174818.6370 | +8984.27 ppm |
| ${}^{187}$Po | 187 | 103 | -118.5034 | 1440.7955 | -108.22 % | 175751.5213 | +8951.61 ppm |
| ${}^{188}$Po | 188 | 104 | -111.8327 | 1452.2350 | -107.70 % | 176684.4161 | +8931.40 ppm |
| ${}^{189}$Po | 189 | 105 | -105.1724 | 1461.1840 | -107.20 % | 177617.3212 | +8897.18 ppm |
| ${}^{190}$Po | 190 | 106 | -98.5223 | 1472.3960 | -106.69 % | 178550.2365 | +8876.29 ppm |
| ${}^{191}$Po | 191 | 107 | -91.8822 | 1480.9733 | -106.20 % | 179483.1619 | +8840.73 ppm |
| ${}^{192}$Po | 192 | 108 | -85.2521 | 1492.0424 | -105.71 % | 180416.0972 | +8819.65 ppm |
| ${}^{193}$Po | 193 | 109 | -78.6318 | 1500.3725 | -105.24 % | 181349.0423 | +8783.47 ppm |
| ${}^{194}$Po | 194 | 110 | -72.0213 | 1511.1232 | -104.77 % | 182281.9972 | +8761.24 ppm |
| ${}^{195}$Po | 195 | 111 | -65.4203 | 1519.3065 | -104.31 % | 183214.9616 | +8725.02 ppm |
| ${}^{196}$Po | 196 | 112 | -58.8288 | 1529.7299 | -103.85 % | 184147.9356 | +8701.61 ppm |
| ${}^{197}$Po | 197 | 113 | -52.2467 | 1537.7256 | -103.40 % | 185080.9189 | +8665.13 ppm |
| ${}^{198}$Po | 198 | 114 | -45.6739 | 1547.8771 | -102.95 % | 186013.9115 | +8640.87 ppm |
| ${}^{199}$Po | 199 | 115 | -39.1102 | 1555.7140 | -102.51 % | 186946.9133 | +8604.30 ppm |
| ${}^{200}$Po | 200 | 116 | -32.5556 | 1565.4881 | -102.08 % | 187879.9241 | +8578.64 ppm |
| ${}^{201}$Po | 201 | 117 | -26.0099 | 1573.1389 | -101.65 % | 188812.9438 | +8541.84 ppm |
| ${}^{202}$Po | 202 | 118 | -19.4731 | 1582.6307 | -101.23 % | 189745.9724 | +8515.32 ppm |
| ${}^{203}$Po | 203 | 119 | -12.9451 | 1590.0712 | -100.81 % | 190679.0098 | +8478.17 ppm |
| ${}^{204}$Po | 204 | 120 | -6.4256 | 1599.1728 | -100.40 % | 191612.0558 | +8450.24 ppm |
| ${}^{205}$Po | 205 | 121 | 0.0852 | 1606.4244 | -99.99 % | 192545.1104 | +8412.86 ppm |
| ${}^{206}$Po | 206 | 122 | 6.5876 | 1615.1630 | -99.59 % | 193478.1734 | +8383.70 ppm |
| ${}^{207}$Po | 207 | 123 | 13.0816 | 1622.1914 | -99.19 % | 194411.2448 | +8345.92 ppm |
| ${}^{208}$Po | 208 | 124 | 19.5674 | 1630.5862 | -98.80 % | 195344.3245 | +8315.66 ppm |
| ${}^{209}$Po | 209 | 125 | 26.0449 | 1637.5543 | -98.41 % | 196277.4123 | +8278.34 ppm |
| ${}^{210}$Po | 210 | 126 | 32.5144 | 1645.2127 | -98.02 % | 197210.5083 | +8244.98 ppm |
| ${}^{211}$Po | 211 | 127 | 38.9759 | 1649.7635 | -97.64 % | 198143.6122 | +8196.03 ppm |
| ${}^{212}$Po | 212 | 128 | 45.4294 | 1655.7717 | -97.26 % | 199076.7241 | +8155.03 ppm |
| ${}^{213}$Po | 213 | 129 | 51.8751 | 1660.1271 | -96.88 % | 200009.8438 | +8106.05 ppm |
| ${}^{214}$Po | 214 | 130 | 58.3131 | 1666.0149 | -96.50 % | 200942.9713 | +8065.32 ppm |
| ${}^{215}$Po | 215 | 131 | 64.7434 | 1670.1580 | -96.12 % | 201876.1064 | +8016.23 ppm |
| ${}^{216}$Po | 216 | 132 | 71.1661 | 1675.9052 | -95.75 % | 202809.2491 | +7975.67 ppm |
| ${}^{217}$Po | 217 | 133 | 77.5813 | 1679.8754 | -95.38 % | 203742.3994 | +7926.66 ppm |
| ${}^{218}$Po | 218 | 134 | 83.9891 | 1685.4735 | -95.02 % | 204675.5570 | +7886.21 ppm |
| ${}^{219}$Po | 219 | 135 | 90.3895 | 1689.2201 | -94.65 % | 205608.7220 | +7837.03 ppm |
| ${}^{220}$Po | 220 | 136 | 96.7826 | 1694.7094 | -94.29 % | 206541.8943 | +7796.90 ppm |
| ${}^{221}$Po | 221 | 137 | 103.1686 | 1698.2704 | -93.93 % | 207475.0737 | +7747.73 ppm |
| ${}^{222}$Po | 222 | 138 | 109.5474 | 1703.6292 | -93.57 % | 208408.2603 | +7707.80 ppm |
| ${}^{223}$Po | 223 | 139 | 115.9192 | 1707.0650 | -93.21 % | 209341.4540 | +7659.15 ppm |
| ${}^{224}$Po | 224 | 140 | 122.2840 | 1712.2560 | -92.86 % | 210274.6546 | +7619.47 ppm |
| ${}^{225}$Po | 225 | 141 | 128.6419 | 1715.8500 | -92.50 % | 211207.8621 | +7571.33 ppm |
| ${}^{226}$Po | 226 | 142 | 134.9930 | 1720.7640 | -92.16 % | 212141.0765 | +7531.80 ppm |
| ${}^{227}$Po | 227 | 143 | 141.3373 | 1724.2920 | -91.80 % | 213074.2976 | +7484.25 ppm |

### Astatine (Z = 85)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{191}$At | 191 | 106 | -115.1793 | 1471.2584 | -107.83 % | 179505.6767 | +8916.62 ppm |
| ${}^{192}$At | 192 | 107 | -108.5142 | 1480.2678 | -107.33 % | 180438.5769 | +8883.34 ppm |
| ${}^{193}$At | 193 | 108 | -101.8591 | 1491.3322 | -106.83 % | 181371.4872 | +8861.98 ppm |
| ${}^{194}$At | 194 | 109 | -95.2139 | 1500.0527 | -106.35 % | 182304.4075 | +8827.82 ppm |
| ${}^{195}$At | 195 | 110 | -88.5786 | 1510.8778 | -105.86 % | 183237.3376 | +8805.75 ppm |
| ${}^{196}$At | 196 | 111 | -81.9530 | 1519.3920 | -105.39 % | 184170.2774 | +8771.19 ppm |
| ${}^{197}$At | 197 | 112 | -75.3370 | 1529.9054 | -104.92 % | 185103.2268 | +8748.02 ppm |
| ${}^{198}$At | 198 | 113 | -68.7304 | 1538.3302 | -104.47 % | 186036.1857 | +8713.71 ppm |
| ${}^{199}$At | 199 | 114 | -62.1333 | 1548.5162 | -104.01 % | 186969.1540 | +8689.38 ppm |
| ${}^{200}$At | 200 | 115 | -55.5455 | 1556.7520 | -103.57 % | 187902.1316 | +8654.79 ppm |
| ${}^{201}$At | 201 | 116 | -48.9668 | 1566.6249 | -103.13 % | 188835.1183 | +8629.40 ppm |
| ${}^{202}$At | 202 | 117 | -42.3972 | 1574.5019 | -102.69 % | 189768.1141 | +8593.62 ppm |
| ${}^{203}$At | 203 | 118 | -35.8365 | 1584.1407 | -102.26 % | 190701.1189 | +8567.64 ppm |
| ${}^{204}$At | 204 | 119 | -29.2847 | 1591.9246 | -101.84 % | 191634.1325 | +8532.11 ppm |
| ${}^{205}$At | 205 | 120 | -22.7417 | 1601.1052 | -101.42 % | 192567.1549 | +8504.35 ppm |
| ${}^{206}$At | 206 | 121 | -16.2073 | 1608.6314 | -101.01 % | 193500.1860 | +8468.21 ppm |
| ${}^{207}$At | 207 | 122 | -9.6815 | 1617.4908 | -100.60 % | 194433.2256 | +8439.43 ppm |
| ${}^{208}$At | 208 | 123 | -3.1642 | 1624.8046 | -100.19 % | 195366.2737 | +8402.93 ppm |
| ${}^{209}$At | 209 | 124 | 3.3448 | 1633.2898 | -99.80 % | 196299.3302 | +8372.89 ppm |
| ${}^{210}$At | 210 | 125 | 9.8454 | 1640.4494 | -99.40 % | 197232.3949 | +8336.35 ppm |
| ${}^{211}$At | 211 | 126 | 16.3379 | 1648.1958 | -99.01 % | 198165.4679 | +8303.21 ppm |
| ${}^{212}$At | 212 | 127 | 22.8222 | 1653.2481 | -98.62 % | 199098.5490 | +8256.66 ppm |
| ${}^{213}$At | 213 | 128 | 29.2985 | 1659.2708 | -98.23 % | 200031.6381 | +8215.52 ppm |
| ${}^{214}$At | 214 | 129 | 35.7669 | 1664.1417 | -97.85 % | 200964.7352 | +8168.99 ppm |
| ${}^{215}$At | 215 | 130 | 42.2274 | 1670.0905 | -97.47 % | 201897.8400 | +8128.35 ppm |
| ${}^{216}$At | 216 | 131 | 48.6802 | 1674.6485 | -97.09 % | 202830.9527 | +8081.16 ppm |
| ${}^{217}$At | 217 | 132 | 55.1253 | 1680.5819 | -96.72 % | 203764.0731 | +8041.30 ppm |
| ${}^{218}$At | 218 | 133 | 61.5627 | 1684.9476 | -96.35 % | 204697.2010 | +7994.07 ppm |
| ${}^{219}$At | 219 | 134 | 67.9927 | 1690.7231 | -95.98 % | 205630.3365 | +7954.27 ppm |
| ${}^{220}$At | 220 | 135 | 74.4151 | 1694.8147 | -95.61 % | 206563.4794 | +7906.59 ppm |
| ${}^{221}$At | 221 | 136 | 80.8303 | 1700.4791 | -95.25 % | 207496.6297 | +7867.08 ppm |
| ${}^{222}$At | 222 | 137 | 87.2381 | 1704.3801 | -94.88 % | 208429.7873 | +7819.36 ppm |
| ${}^{223}$At | 223 | 138 | 93.6387 | 1709.9764 | -94.52 % | 209362.9522 | +7780.34 ppm |
| ${}^{224}$At | 224 | 139 | 100.0322 | 1713.7647 | -94.16 % | 210296.1241 | +7732.97 ppm |
| ${}^{225}$At | 225 | 140 | 106.4185 | 1719.2250 | -93.81 % | 211229.3032 | +7694.20 ppm |
| ${}^{226}$At | 226 | 141 | 112.7979 | 1723.0240 | -93.45 % | 212162.4892 | +7647.32 ppm |
| ${}^{227}$At | 227 | 142 | 119.1704 | 1728.1510 | -93.10 % | 213095.6822 | +7608.47 ppm |
| ${}^{228}$At | 228 | 143 | 125.5360 | 1731.8880 | -92.75 % | 214028.8820 | +7562.03 ppm |
| ${}^{229}$At | 229 | 144 | 131.8948 | 1736.9650 | -92.41 % | 214962.0886 | +7522.83 ppm |

### Radon (Z = 86)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{193}$Rn | 193 | 107 | -125.3323 | 1481.4396 | -108.46 % | 181394.1781 | +8937.07 ppm |
| ${}^{194}$Rn | 194 | 108 | -118.6521 | 1492.8292 | -107.95 % | 182327.0634 | +8917.23 ppm |
| ${}^{195}$Rn | 195 | 109 | -111.9821 | 1501.5749 | -107.46 % | 183259.9587 | +8882.96 ppm |
| ${}^{196}$Rn | 196 | 110 | -105.3219 | 1512.7213 | -106.96 % | 184192.8640 | +8862.36 ppm |
| ${}^{197}$Rn | 197 | 111 | -98.6716 | 1521.2574 | -106.49 % | 185125.7791 | +8827.68 ppm |
| ${}^{198}$Rn | 198 | 112 | -92.0310 | 1532.0695 | -106.01 % | 186058.7039 | +8805.84 ppm |
| ${}^{199}$Rn | 199 | 113 | -85.4000 | 1540.4703 | -105.54 % | 186991.6384 | +8771.15 ppm |
| ${}^{200}$Rn | 200 | 114 | -78.7785 | 1550.9822 | -105.08 % | 187924.5823 | +8748.29 ppm |
| ${}^{201}$Rn | 201 | 115 | -72.1664 | 1559.1605 | -104.63 % | 188857.5356 | +8713.14 ppm |
| ${}^{202}$Rn | 202 | 116 | -65.5636 | 1569.3990 | -104.18 % | 189790.4982 | +8689.43 ppm |
| ${}^{203}$Rn | 203 | 117 | -58.9700 | 1577.3798 | -103.74 % | 190723.4700 | +8653.95 ppm |
| ${}^{204}$Rn | 204 | 118 | -52.3854 | 1587.2372 | -103.30 % | 191656.4509 | +8628.83 ppm |
| ${}^{205}$Rn | 205 | 119 | -45.8098 | 1595.0481 | -102.87 % | 192589.4407 | +8593.20 ppm |
| ${}^{206}$Rn | 206 | 120 | -39.2431 | 1604.5426 | -102.45 % | 193522.4394 | +8566.80 ppm |
| ${}^{207}$Rn | 207 | 121 | -32.6851 | 1612.1157 | -102.03 % | 194455.4469 | +8530.66 ppm |
| ${}^{208}$Rn | 208 | 122 | -26.1358 | 1621.2077 | -101.61 % | 195388.4630 | +8502.81 ppm |
| ${}^{209}$Rn | 209 | 123 | -19.5952 | 1628.5647 | -101.20 % | 196321.4878 | +8466.29 ppm |
| ${}^{210}$Rn | 210 | 124 | -13.0629 | 1637.2997 | -100.80 % | 197254.5210 | +8437.26 ppm |
| ${}^{211}$Rn | 211 | 125 | -6.5391 | 1644.5216 | -100.40 % | 198187.5626 | +8400.79 ppm |
| ${}^{212}$Rn | 212 | 126 | -0.0236 | 1652.4968 | -100.00 % | 199120.6125 | +8368.55 ppm |
| ${}^{213}$Rn | 213 | 127 | 6.4837 | 1657.6049 | -99.61 % | 200053.6706 | +8322.08 ppm |
| ${}^{214}$Rn | 214 | 128 | 12.9828 | 1664.2999 | -99.22 % | 200986.7369 | +8284.12 ppm |
| ${}^{215}$Rn | 215 | 129 | 19.4739 | 1669.2205 | -98.83 % | 201919.8112 | +8237.62 ppm |
| ${}^{216}$Rn | 216 | 130 | 25.9571 | 1675.8695 | -98.45 % | 202852.8935 | +8200.25 ppm |
| ${}^{217}$Rn | 217 | 131 | 32.4324 | 1680.5356 | -98.07 % | 203785.9836 | +8153.37 ppm |
| ${}^{218}$Rn | 218 | 132 | 38.8999 | 1687.0481 | -97.69 % | 204719.0815 | +8116.13 ppm |
| ${}^{219}$Rn | 219 | 133 | 45.3597 | 1691.5075 | -97.32 % | 205652.1871 | +8069.12 ppm |
| ${}^{220}$Rn | 220 | 134 | 51.8119 | 1697.7961 | -96.95 % | 206585.3004 | +8031.58 ppm |
| ${}^{221}$Rn | 221 | 135 | 58.2565 | 1702.0081 | -96.58 % | 207518.4212 | +7984.24 ppm |
| ${}^{222}$Rn | 222 | 136 | 64.6937 | 1708.1788 | -96.21 % | 208451.5494 | +7946.92 ppm |
| ${}^{223}$Rn | 223 | 137 | 71.1234 | 1712.2324 | -95.85 % | 209384.6851 | +7899.69 ppm |
| ${}^{224}$Rn | 224 | 138 | 77.5459 | 1718.2483 | -95.49 % | 210317.8280 | +7862.40 ppm |
| ${}^{225}$Rn | 225 | 139 | 83.9611 | 1722.2306 | -95.12 % | 211250.9783 | +7815.70 ppm |
| ${}^{226}$Rn | 226 | 140 | 90.3692 | 1728.0888 | -94.77 % | 212184.1356 | +7778.43 ppm |
| ${}^{227}$Rn | 227 | 141 | 96.7701 | 1732.0215 | -94.41 % | 213117.3001 | +7732.35 ppm |
| ${}^{228}$Rn | 228 | 142 | 103.1640 | 1737.7352 | -94.06 % | 214050.4716 | +7695.15 ppm |
| ${}^{229}$Rn | 229 | 143 | 109.5510 | 1741.6876 | -93.71 % | 214983.6501 | +7649.99 ppm |
| ${}^{230}$Rn | 230 | 144 | 115.9311 | 1746.8500 | -93.36 % | 215916.8354 | +7611.43 ppm |
| ${}^{231}$Rn | 231 | 145 | 122.3044 | 1750.7490 | -93.01 % | 216850.0275 | +7565.87 ppm |

### Francium (Z = 87)

_37 of 37 isotopes with a framework prediction; 37 of 37 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{197}$Fr | 197 | 110 | -122.2506 | 1511.7315 | -108.09 % | 185148.5758 | +8903.83 ppm |
| ${}^{198}$Fr | 198 | 111 | -115.5755 | 1520.4791 | -107.60 % | 186081.4661 | +8870.14 ppm |
| ${}^{199}$Fr | 199 | 112 | -108.9103 | 1531.3567 | -107.11 % | 187014.3663 | +8848.42 ppm |
| ${}^{200}$Fr | 200 | 113 | -102.2548 | 1540.0658 | -106.64 % | 187947.2762 | +8815.23 ppm |
| ${}^{201}$Fr | 201 | 114 | -95.6089 | 1550.6822 | -106.17 % | 188880.1957 | +8792.70 ppm |
| ${}^{202}$Fr | 202 | 115 | -88.9724 | 1559.2405 | -105.71 % | 189813.1248 | +8759.41 ppm |
| ${}^{203}$Fr | 203 | 116 | -82.3454 | 1569.5370 | -105.25 % | 190746.0632 | +8735.77 ppm |
| ${}^{204}$Fr | 204 | 117 | -75.7277 | 1577.8774 | -104.80 % | 191679.0109 | +8702.03 ppm |
| ${}^{205}$Fr | 205 | 118 | -69.1192 | 1587.8658 | -104.35 % | 192611.9677 | +8677.37 ppm |
| ${}^{206}$Fr | 206 | 119 | -62.5197 | 1595.8742 | -103.92 % | 193544.9337 | +8642.58 ppm |
| ${}^{207}$Fr | 207 | 120 | -55.9292 | 1605.5477 | -103.48 % | 194477.9086 | +8616.89 ppm |
| ${}^{208}$Fr | 208 | 121 | -49.3476 | 1613.4349 | -103.06 % | 195410.8925 | +8582.19 ppm |
| ${}^{209}$Fr | 209 | 122 | -42.7748 | 1622.6234 | -102.64 % | 196343.8851 | +8554.62 ppm |
| ${}^{210}$Fr | 210 | 123 | -36.2107 | 1630.2561 | -102.22 % | 197276.8864 | +8519.32 ppm |
| ${}^{211}$Fr | 211 | 124 | -29.6551 | 1639.1242 | -101.81 % | 198209.8962 | +8490.75 ppm |
| ${}^{212}$Fr | 212 | 125 | -23.1081 | 1646.5712 | -101.40 % | 199142.9146 | +8455.23 ppm |
| ${}^{213}$Fr | 213 | 126 | -16.5695 | 1654.6808 | -101.00 % | 200075.9414 | +8423.45 ppm |
| ${}^{214}$Fr | 214 | 127 | -10.0392 | 1660.1562 | -100.60 % | 201008.9765 | +8378.68 ppm |
| ${}^{215}$Fr | 215 | 128 | -3.5171 | 1666.9511 | -100.21 % | 201942.0199 | +8341.02 ppm |
| ${}^{216}$Fr | 216 | 129 | 2.9968 | 1672.3695 | -99.82 % | 202875.0714 | +8296.85 ppm |
| ${}^{217}$Fr | 217 | 130 | 9.5027 | 1679.0972 | -99.43 % | 203808.1309 | +8259.66 ppm |
| ${}^{218}$Fr | 218 | 131 | 16.0006 | 1684.4237 | -99.05 % | 204741.1984 | +8215.89 ppm |
| ${}^{219}$Fr | 219 | 132 | 22.4906 | 1690.9375 | -98.67 % | 205674.2738 | +8178.43 ppm |
| ${}^{220}$Fr | 220 | 133 | 28.9729 | 1696.1435 | -98.29 % | 206607.3571 | +8134.92 ppm |
| ${}^{221}$Fr | 221 | 134 | 35.4473 | 1702.4198 | -97.92 % | 207540.4480 | +8097.08 ppm |
| ${}^{222}$Fr | 222 | 135 | 41.9142 | 1707.3903 | -97.55 % | 208473.5466 | +8053.25 ppm |
| ${}^{223}$Fr | 223 | 136 | 48.3735 | 1713.4574 | -97.18 % | 209406.6527 | +8015.18 ppm |
| ${}^{224}$Fr | 224 | 137 | 54.8253 | 1718.1624 | -96.81 % | 210339.7664 | +7970.90 ppm |
| ${}^{225}$Fr | 225 | 138 | 61.2696 | 1724.1618 | -96.45 % | 211272.8874 | +7933.27 ppm |
| ${}^{226}$Fr | 226 | 139 | 67.7067 | 1728.5332 | -96.08 % | 212206.0158 | +7888.22 ppm |
| ${}^{227}$Fr | 227 | 140 | 74.1364 | 1734.4426 | -95.73 % | 213139.1514 | +7850.94 ppm |
| ${}^{228}$Fr | 228 | 141 | 80.5590 | 1738.8121 | -95.37 % | 214072.2943 | +7806.71 ppm |
| ${}^{229}$Fr | 229 | 142 | 86.9745 | 1744.5994 | -95.01 % | 215005.4442 | +7769.60 ppm |
| ${}^{230}$Fr | 230 | 143 | 93.3829 | 1748.8522 | -94.66 % | 215938.6012 | +7725.62 ppm |
| ${}^{231}$Fr | 231 | 144 | 99.7844 | 1754.3297 | -94.31 % | 216871.7652 | +7687.80 ppm |
| ${}^{232}$Fr | 232 | 145 | 106.1789 | 1758.4088 | -93.96 % | 217804.9361 | +7643.81 ppm |
| ${}^{233}$Fr | 233 | 146 | 112.5666 | 1763.6329 | -93.62 % | 218738.1138 | +7605.56 ppm |

### Radium (Z = 88)

_35 of 35 isotopes with a framework prediction; 35 of 35 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{201}$Ra | 201 | 113 | -119.2941 | 1541.5516 | -107.74 % | 188903.0986 | +8870.04 ppm |
| ${}^{202}$Ra | 202 | 114 | -112.6237 | 1552.4848 | -107.25 % | 189835.9937 | +8848.92 ppm |
| ${}^{203}$Ra | 203 | 115 | -105.9629 | 1561.0297 | -106.79 % | 190768.8983 | +8815.32 ppm |
| ${}^{204}$Ra | 204 | 116 | -99.3116 | 1571.6413 | -106.32 % | 191701.8125 | +8793.07 ppm |
| ${}^{205}$Ra | 205 | 117 | -92.6698 | 1579.9698 | -105.87 % | 192634.7360 | +8759.02 ppm |
| ${}^{206}$Ra | 206 | 118 | -86.0372 | 1590.2794 | -105.41 % | 193567.6688 | +8735.77 ppm |
| ${}^{207}$Ra | 207 | 119 | -79.4138 | 1598.4023 | -104.97 % | 194500.6109 | +8701.34 ppm |
| ${}^{208}$Ra | 208 | 120 | -72.7995 | 1608.2597 | -104.53 % | 195433.5620 | +8676.33 ppm |
| ${}^{209}$Ra | 209 | 121 | -66.1942 | 1616.2007 | -104.10 % | 196366.5221 | +8641.67 ppm |
| ${}^{210}$Ra | 210 | 122 | -59.5977 | 1625.6874 | -103.67 % | 197299.4911 | +8615.36 ppm |
| ${}^{211}$Ra | 211 | 123 | -53.0101 | 1633.3697 | -103.25 % | 198232.4689 | +8580.08 ppm |
| ${}^{212}$Ra | 212 | 124 | -46.4312 | 1642.4717 | -102.83 % | 199165.4554 | +8552.43 ppm |
| ${}^{213}$Ra | 213 | 125 | -39.8608 | 1649.9987 | -102.42 % | 200098.4505 | +8517.07 ppm |
| ${}^{214}$Ra | 214 | 126 | -33.2990 | 1658.3228 | -102.01 % | 201031.4541 | +8486.13 ppm |
| ${}^{215}$Ra | 215 | 127 | -26.7456 | 1663.9549 | -101.61 % | 201964.4661 | +8441.95 ppm |
| ${}^{216}$Ra | 216 | 128 | -20.2006 | 1671.2667 | -101.21 % | 202897.4865 | +8406.65 ppm |
| ${}^{217}$Ra | 217 | 129 | -13.6638 | 1676.7399 | -100.81 % | 203830.5151 | +8362.54 ppm |
| ${}^{218}$Ra | 218 | 130 | -7.1351 | 1684.0553 | -100.42 % | 204763.5518 | +8328.02 ppm |
| ${}^{219}$Ra | 219 | 131 | -0.6145 | 1689.3783 | -100.04 % | 205696.5967 | +8284.02 ppm |
| ${}^{220}$Ra | 220 | 132 | 5.8981 | 1696.5713 | -99.65 % | 206629.6495 | +8249.65 ppm |
| ${}^{221}$Ra | 221 | 133 | 12.4028 | 1701.9509 | -99.27 % | 207562.7102 | +8206.75 ppm |
| ${}^{222}$Ra | 222 | 134 | 18.8996 | 1708.6659 | -98.89 % | 208495.7788 | +8170.79 ppm |
| ${}^{223}$Ra | 223 | 135 | 25.3888 | 1713.8242 | -98.52 % | 209428.8551 | +8127.63 ppm |
| ${}^{224}$Ra | 224 | 136 | 31.8702 | 1720.3029 | -98.15 % | 210361.9390 | +8091.27 ppm |
| ${}^{225}$Ra | 225 | 137 | 38.3441 | 1725.2070 | -97.78 % | 211295.0306 | +8047.70 ppm |
| ${}^{226}$Ra | 226 | 138 | 44.8105 | 1731.6038 | -97.41 % | 212228.1296 | +8011.70 ppm |
| ${}^{227}$Ra | 227 | 139 | 51.2694 | 1736.1652 | -97.05 % | 213161.2361 | +7967.31 ppm |
| ${}^{228}$Ra | 228 | 140 | 57.7210 | 1742.4738 | -96.69 % | 214094.3500 | +7931.63 ppm |
| ${}^{229}$Ra | 229 | 141 | 64.1653 | 1746.9233 | -96.33 % | 215027.4711 | +7887.51 ppm |
| ${}^{230}$Ra | 230 | 142 | 70.6024 | 1753.0403 | -95.97 % | 215960.5994 | +7851.66 ppm |
| ${}^{231}$Ra | 231 | 143 | 77.0323 | 1757.4115 | -95.62 % | 216893.7349 | +7807.97 ppm |
| ${}^{232}$Ra | 232 | 144 | 83.4552 | 1763.2023 | -95.27 % | 217826.8774 | +7771.32 ppm |
| ${}^{233}$Ra | 233 | 145 | 89.8711 | 1767.4365 | -94.92 % | 218760.0270 | +7727.79 ppm |
| ${}^{234}$Ra | 234 | 146 | 96.2801 | 1772.9113 | -94.57 % | 219693.1834 | +7690.39 ppm |
| ${}^{235}$Ra | 235 | 147 | 102.6822 | 1776.8350 | -94.22 % | 220626.3468 | +7645.97 ppm |

### Actinium (Z = 89)

_33 of 33 isotopes with a framework prediction; 33 of 33 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{205}$Ac | 205 | 116 | -116.4616 | 1570.8846 | -107.41 % | 192657.7455 | +8835.65 ppm |
| ${}^{206}$Ac | 206 | 117 | -109.7955 | 1579.5779 | -106.95 % | 193590.6449 | +8803.35 ppm |
| ${}^{207}$Ac | 207 | 118 | -103.1388 | 1589.9877 | -106.49 % | 194523.5536 | +8780.40 ppm |
| ${}^{208}$Ac | 208 | 119 | -96.4915 | 1598.4444 | -106.04 % | 195456.4716 | +8747.54 ppm |
| ${}^{209}$Ac | 209 | 120 | -89.8533 | 1608.4317 | -105.59 % | 196389.3989 | +8722.98 ppm |
| ${}^{210}$Ac | 210 | 121 | -83.2242 | 1616.5838 | -105.15 % | 197322.3352 | +8689.23 ppm |
| ${}^{211}$Ac | 211 | 122 | -76.6041 | 1626.2757 | -104.71 % | 198255.2805 | +8663.75 ppm |
| ${}^{212}$Ac | 212 | 123 | -69.9929 | 1634.1910 | -104.28 % | 199188.2347 | +8629.48 ppm |
| ${}^{213}$Ac | 213 | 124 | -63.3905 | 1643.4208 | -103.86 % | 200121.1978 | +8602.26 ppm |
| ${}^{214}$Ac | 214 | 125 | -56.7968 | 1651.1999 | -103.44 % | 201054.1695 | +8568.00 ppm |
| ${}^{215}$Ac | 215 | 126 | -50.2117 | 1659.6739 | -103.03 % | 201987.1499 | +8537.60 ppm |
| ${}^{216}$Ac | 216 | 127 | -43.6352 | 1665.6261 | -102.62 % | 202920.1387 | +8494.88 ppm |
| ${}^{217}$Ac | 217 | 128 | -37.0671 | 1673.1448 | -102.22 % | 203853.1361 | +8460.42 ppm |
| ${}^{218}$Ac | 218 | 129 | -30.5073 | 1679.0676 | -101.82 % | 204786.1417 | +8418.38 ppm |
| ${}^{219}$Ac | 219 | 130 | -23.9558 | 1686.4202 | -101.42 % | 205719.1556 | +8383.84 ppm |
| ${}^{220}$Ac | 220 | 131 | -17.4125 | 1692.3173 | -101.03 % | 206652.1777 | +8342.49 ppm |
| ${}^{221}$Ac | 221 | 132 | -10.8772 | 1699.6014 | -100.64 % | 207585.2079 | +8308.35 ppm |
| ${}^{222}$Ac | 222 | 133 | -4.3500 | 1705.5819 | -100.26 % | 208518.2461 | +8268.20 ppm |
| ${}^{223}$Ac | 223 | 134 | 2.1693 | 1712.4500 | -99.87 % | 209451.2922 | +8232.76 ppm |
| ${}^{224}$Ac | 224 | 135 | 8.6808 | 1718.1122 | -99.49 % | 210384.3461 | +8191.85 ppm |
| ${}^{225}$Ac | 225 | 136 | 15.1845 | 1724.7804 | -99.12 % | 211317.4078 | +8156.17 ppm |
| ${}^{226}$Ac | 226 | 137 | 21.6806 | 1730.1798 | -98.75 % | 212250.4772 | +8114.77 ppm |
| ${}^{227}$Ac | 227 | 138 | 28.1690 | 1736.7108 | -98.38 % | 213183.5542 | +8079.17 ppm |
| ${}^{228}$Ac | 228 | 139 | 34.6499 | 1741.7370 | -98.01 % | 214116.6387 | +8036.78 ppm |
| ${}^{229}$Ac | 229 | 140 | 41.1234 | 1748.0130 | -97.65 % | 215049.7307 | +8000.69 ppm |
| ${}^{230}$Ac | 230 | 141 | 47.5895 | 1752.9359 | -97.29 % | 215982.8300 | +7958.60 ppm |
| ${}^{231}$Ac | 231 | 142 | 54.0483 | 1759.0827 | -96.93 % | 216915.9366 | +7922.63 ppm |
| ${}^{232}$Ac | 232 | 143 | 60.4998 | 1763.7625 | -96.57 % | 217849.0505 | +7880.16 ppm |
| ${}^{233}$Ac | 233 | 144 | 66.9442 | 1769.6802 | -96.22 % | 218782.1715 | +7843.84 ppm |
| ${}^{234}$Ac | 234 | 145 | 73.3815 | 1774.2183 | -95.86 % | 219715.2997 | +7801.49 ppm |
| ${}^{235}$Ac | 235 | 146 | 79.8118 | 1779.7737 | -95.52 % | 220648.4348 | +7764.22 ppm |
| ${}^{236}$Ac | 236 | 147 | 86.2351 | 1783.9812 | -95.17 % | 221581.5769 | +7721.11 ppm |
| ${}^{237}$Ac | 237 | 148 | 92.6516 | 1789.3500 | -94.82 % | 222514.7259 | +7683.26 ppm |

### Thorium (Z = 90)

_32 of 32 isotopes with a framework prediction; 32 of 32 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{208}$Th | 208 | 118 | -120.4235 | 1591.7349 | -107.57 % | 195479.6214 | +8836.16 ppm |
| ${}^{209}$Th | 209 | 119 | -113.7521 | 1600.1040 | -107.11 % | 196412.5154 | +8802.59 ppm |
| ${}^{210}$Th | 210 | 120 | -107.0900 | 1610.5060 | -106.65 % | 197345.4187 | +8779.92 ppm |
| ${}^{211}$Th | 211 | 121 | -100.4370 | 1618.7605 | -106.20 % | 198278.3311 | +8746.47 ppm |
| ${}^{212}$Th | 212 | 122 | -93.7932 | 1628.5973 | -105.76 % | 199211.2527 | +8721.46 ppm |
| ${}^{213}$Th | 213 | 123 | -87.1584 | 1636.6594 | -105.33 % | 200144.1833 | +8687.71 ppm |
| ${}^{214}$Th | 214 | 124 | -80.5325 | 1646.1559 | -104.89 % | 201077.1228 | +8661.58 ppm |
| ${}^{215}$Th | 215 | 125 | -73.9154 | 1654.0007 | -104.47 % | 202010.0712 | +8627.42 ppm |
| ${}^{216}$Th | 216 | 126 | -67.3070 | 1662.6949 | -104.05 % | 202943.0282 | +8597.87 ppm |
| ${}^{217}$Th | 217 | 127 | -60.7072 | 1668.8590 | -103.64 % | 203875.9939 | +8556.01 ppm |
| ${}^{218}$Th | 218 | 128 | -54.1160 | 1676.7694 | -103.23 % | 204808.9681 | +8523.26 ppm |
| ${}^{219}$Th | 219 | 129 | -47.5332 | 1682.7446 | -102.82 % | 205741.9507 | +8481.28 ppm |
| ${}^{220}$Th | 220 | 130 | -40.9588 | 1690.5892 | -102.42 % | 206674.9417 | +8448.92 ppm |
| ${}^{221}$Th | 221 | 131 | -34.3926 | 1696.4101 | -102.03 % | 207607.9410 | +8406.98 ppm |
| ${}^{222}$Th | 222 | 132 | -27.8347 | 1704.2183 | -101.63 % | 208540.9484 | +8375.14 ppm |
| ${}^{223}$Th | 223 | 133 | -21.2848 | 1710.1073 | -101.24 % | 209473.9640 | +8334.32 ppm |
| ${}^{224}$Th | 224 | 134 | -14.7430 | 1717.5684 | -100.86 % | 210406.9876 | +8301.50 ppm |
| ${}^{225}$Th | 225 | 135 | -8.2091 | 1723.3252 | -100.48 % | 211340.0191 | +8260.81 ppm |
| ${}^{226}$Th | 226 | 136 | -1.6830 | 1730.5090 | -100.10 % | 212273.0585 | +8227.35 ppm |
| ${}^{227}$Th | 227 | 137 | 4.8353 | 1735.9732 | -99.72 % | 213206.1056 | +8186.02 ppm |
| ${}^{228}$Th | 228 | 138 | 11.3458 | 1743.0784 | -99.35 % | 214139.1605 | +8152.89 ppm |
| ${}^{229}$Th | 229 | 139 | 17.8488 | 1748.3351 | -98.98 % | 215072.2229 | +8111.34 ppm |
| ${}^{230}$Th | 230 | 140 | 24.3442 | 1755.1294 | -98.61 % | 216005.2929 | +8077.43 ppm |
| ${}^{231}$Th | 231 | 141 | 30.8321 | 1760.2474 | -98.25 % | 216938.3704 | +8035.99 ppm |
| ${}^{232}$Th | 232 | 142 | 37.3127 | 1766.6878 | -97.89 % | 217871.4553 | +8001.11 ppm |
| ${}^{233}$Th | 233 | 143 | 43.7859 | 1771.4742 | -97.53 % | 218804.5475 | +7958.88 ppm |
| ${}^{234}$Th | 234 | 144 | 50.2519 | 1777.6642 | -97.17 % | 219737.6470 | +7923.54 ppm |
| ${}^{235}$Th | 235 | 145 | 56.7107 | 1782.3308 | -96.82 % | 220670.7536 | +7881.52 ppm |
| ${}^{236}$Th | 236 | 146 | 63.1624 | 1788.1646 | -96.47 % | 221603.8673 | +7845.25 ppm |
| ${}^{237}$Th | 237 | 147 | 69.6070 | 1792.5361 | -96.12 % | 222536.9881 | +7802.63 ppm |
| ${}^{238}$Th | 238 | 148 | 76.0447 | 1798.0900 | -95.77 % | 223470.1159 | +7765.54 ppm |
| ${}^{239}$Th | 239 | 149 | 82.4754 | 1802.0600 | -95.42 % | 224403.2505 | +7722.44 ppm |

### Protactinium (Z = 91)

_31 of 31 isotopes with a framework prediction; 31 of 31 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{211}$Pa | 211 | 120 | -124.5090 | 1609.8023 | -107.73 % | 198301.6208 | +8823.00 ppm |
| ${}^{212}$Pa | 212 | 121 | -117.8322 | 1618.3293 | -107.28 % | 199234.5094 | +8790.77 ppm |
| ${}^{213}$Pa | 213 | 122 | -111.1645 | 1628.3430 | -106.83 % | 200167.4072 | +8766.45 ppm |
| ${}^{214}$Pa | 214 | 123 | -104.5060 | 1636.6086 | -106.39 % | 201100.3141 | +8733.56 ppm |
| ${}^{215}$Pa | 215 | 124 | -97.8565 | 1646.3353 | -105.94 % | 202033.2300 | +8708.38 ppm |
| ${}^{216}$Pa | 216 | 125 | -91.2159 | 1654.3873 | -105.51 % | 202966.1548 | +8675.08 ppm |
| ${}^{217}$Pa | 217 | 126 | -84.5842 | 1663.2277 | -105.09 % | 203899.0885 | +8646.07 ppm |
| ${}^{218}$Pa | 218 | 127 | -77.9611 | 1669.7042 | -104.67 % | 204832.0309 | +8605.62 ppm |
| ${}^{219}$Pa | 219 | 128 | -71.3467 | 1677.8418 | -104.25 % | 205764.9819 | +8573.80 ppm |
| ${}^{220}$Pa | 220 | 129 | -64.7409 | 1684.2180 | -103.84 % | 206697.9415 | +8533.64 ppm |
| ${}^{221}$Pa | 221 | 130 | -58.1435 | 1692.1928 | -103.44 % | 207630.9095 | +8501.71 ppm |
| ${}^{222}$Pa | 222 | 131 | -51.5544 | 1698.5747 | -103.04 % | 208563.8859 | +8462.35 ppm |
| ${}^{223}$Pa | 223 | 132 | -44.9737 | 1706.3727 | -102.64 % | 209496.8706 | +8430.26 ppm |
| ${}^{224}$Pa | 224 | 133 | -38.4012 | 1712.9193 | -102.24 % | 210429.8634 | +8392.44 ppm |
| ${}^{225}$Pa | 225 | 134 | -31.8367 | 1720.4963 | -101.85 % | 211362.8644 | +8359.95 ppm |
| ${}^{226}$Pa | 226 | 135 | -25.2803 | 1726.8907 | -101.46 % | 212295.8735 | +8322.13 ppm |
| ${}^{227}$Pa | 227 | 136 | -18.7319 | 1734.1653 | -101.08 % | 213228.8904 | +8288.88 ppm |
| ${}^{228}$Pa | 228 | 137 | -12.1913 | 1740.1433 | -100.70 % | 214161.9153 | +8249.80 ppm |
| ${}^{229}$Pa | 229 | 138 | -5.6585 | 1747.2414 | -100.32 % | 215094.9479 | +8216.39 ppm |
| ${}^{230}$Pa | 230 | 139 | 0.8665 | 1753.0360 | -99.95 % | 216027.9883 | +8177.18 ppm |
| ${}^{231}$Pa | 231 | 140 | 7.3840 | 1759.8566 | -99.58 % | 216961.0363 | +8143.14 ppm |
| ${}^{232}$Pa | 232 | 141 | 13.8938 | 1765.4057 | -99.21 % | 217894.0918 | +8103.51 ppm |
| ${}^{233}$Pa | 233 | 142 | 20.3962 | 1771.9341 | -98.85 % | 218827.1549 | +8068.80 ppm |
| ${}^{234}$Pa | 234 | 143 | 26.8912 | 1777.1560 | -98.49 % | 219760.2253 | +8028.38 ppm |
| ${}^{235}$Pa | 235 | 144 | 33.3788 | 1783.2773 | -98.13 % | 220693.3031 | +7992.48 ppm |
| ${}^{236}$Pa | 236 | 145 | 39.8591 | 1788.3035 | -97.77 % | 221626.3882 | +7951.89 ppm |
| ${}^{237}$Pa | 237 | 146 | 46.3323 | 1794.1812 | -97.42 % | 222559.4805 | +7915.57 ppm |
| ${}^{238}$Pa | 238 | 147 | 52.7983 | 1798.8861 | -97.06 % | 223492.5799 | +7874.26 ppm |
| ${}^{239}$Pa | 239 | 148 | 59.2573 | 1804.4500 | -96.72 % | 224425.6863 | +7837.50 ppm |
| ${}^{240}$Pa | 240 | 149 | 65.7093 | 1808.8800 | -96.37 % | 225358.7998 | +7795.54 ppm |
| ${}^{241}$Pa | 241 | 150 | 72.1543 | 1814.2480 | -96.02 % | 226291.9202 | +7758.19 ppm |

### Uranium (Z = 92)

_29 of 29 isotopes with a framework prediction; 29 of 29 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{215}$U | 215 | 123 | -122.0352 | 1638.4682 | -107.45 % | 202056.6263 | +8789.51 ppm |
| ${}^{216}$U | 216 | 124 | -115.3621 | 1648.3624 | -107.00 % | 202989.5186 | +8764.91 ppm |
| ${}^{217}$U | 217 | 125 | -108.6979 | 1656.5780 | -106.56 % | 203922.4199 | +8731.96 ppm |
| ${}^{218}$U | 218 | 126 | -102.0427 | 1665.6768 | -106.13 % | 204855.3301 | +8704.23 ppm |
| ${}^{219}$U | 219 | 127 | -95.3964 | 1672.3468 | -105.70 % | 205788.2492 | +8664.54 ppm |
| ${}^{220}$U | 220 | 128 | -88.7587 | 1680.8000 | -105.28 % | 206721.1770 | +8633.55 ppm |
| ${}^{221}$U | 221 | 129 | -82.1297 | 1687.2654 | -104.87 % | 207654.1134 | +8594.11 ppm |
| ${}^{222}$U | 222 | 130 | -75.5093 | 1695.5839 | -104.45 % | 208587.0584 | +8563.63 ppm |
| ${}^{223}$U | 223 | 131 | -68.8973 | 1701.8827 | -104.05 % | 209520.0118 | +8523.65 ppm |
| ${}^{224}$U | 224 | 132 | -62.2937 | 1710.2566 | -103.64 % | 210452.9737 | +8494.10 ppm |
| ${}^{225}$U | 225 | 133 | -55.6984 | 1716.6986 | -103.24 % | 211385.9438 | +8455.55 ppm |
| ${}^{226}$U | 226 | 134 | -49.1114 | 1724.8132 | -102.85 % | 212318.9221 | +8425.40 ppm |
| ${}^{227}$U | 227 | 135 | -42.5324 | 1731.1682 | -102.46 % | 213251.9086 | +8387.16 ppm |
| ${}^{228}$U | 228 | 136 | -35.9615 | 1739.0646 | -102.07 % | 214184.9031 | +8356.61 ppm |
| ${}^{229}$U | 229 | 137 | -29.3986 | 1745.1453 | -101.68 % | 215117.9056 | +8317.79 ppm |
| ${}^{230}$U | 230 | 138 | -22.8435 | 1752.8122 | -101.30 % | 216050.9160 | +8286.80 ppm |
| ${}^{231}$U | 231 | 139 | -16.2963 | 1758.6926 | -100.93 % | 216983.9342 | +8247.75 ppm |
| ${}^{232}$U | 232 | 140 | -9.7568 | 1765.9604 | -100.55 % | 217916.9601 | +8215.55 ppm |
| ${}^{233}$U | 233 | 141 | -3.2249 | 1771.7221 | -100.18 % | 218849.9936 | +8176.66 ppm |
| ${}^{234}$U | 234 | 142 | 3.2994 | 1778.5675 | -99.81 % | 219783.0348 | +8143.15 ppm |
| ${}^{235}$U | 235 | 143 | 9.8162 | 1783.8650 | -99.45 % | 220716.0834 | +8102.83 ppm |
| ${}^{236}$U | 236 | 144 | 16.3255 | 1790.4106 | -99.09 % | 221649.1395 | +8068.61 ppm |
| ${}^{237}$U | 237 | 145 | 22.8275 | 1795.5363 | -98.73 % | 222582.2029 | +8028.23 ppm |
| ${}^{238}$U | 238 | 146 | 29.3222 | 1801.6900 | -98.37 % | 223515.2737 | +7992.90 ppm |
| ${}^{239}$U | 239 | 147 | 35.8097 | 1806.4964 | -98.02 % | 224448.3516 | +7951.80 ppm |
| ${}^{240}$U | 240 | 148 | 42.2900 | 1812.4249 | -97.67 % | 225381.4367 | +7916.13 ppm |
| ${}^{241}$U | 241 | 149 | 48.7632 | 1816.8990 | -97.32 % | 226314.5289 | +7874.78 ppm |
| ${}^{242}$U | 242 | 150 | 55.2295 | 1822.7440 | -96.97 % | 227247.6281 | +7838.54 ppm |
| ${}^{243}$U | 243 | 151 | 61.6887 | 1826.8740 | -96.62 % | 228180.7342 | +7796.23 ppm |

### Neptunium (Z = 93)

_27 of 27 isotopes with a framework prediction; 27 of 27 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{219}$Np | 219 | 126 | -119.6821 | 1665.4234 | -107.19 % | 205811.7526 | +8749.38 ppm |
| ${}^{220}$Np | 220 | 127 | -113.0123 | 1672.4567 | -106.76 % | 206744.6482 | +8711.35 ppm |
| ${}^{221}$Np | 221 | 128 | -106.3514 | 1681.1470 | -106.33 % | 207677.5527 | +8681.55 ppm |
| ${}^{222}$Np | 222 | 129 | -99.6992 | 1687.7997 | -105.91 % | 208610.4659 | +8642.66 ppm |
| ${}^{223}$Np | 223 | 130 | -93.0557 | 1696.4871 | -105.49 % | 209543.3878 | +8613.77 ppm |
| ${}^{224}$Np | 224 | 131 | -86.4207 | 1703.1847 | -105.07 % | 210476.3183 | +8575.57 ppm |
| ${}^{225}$Np | 225 | 132 | -79.7942 | 1711.6702 | -104.66 % | 211409.2572 | +8546.34 ppm |
| ${}^{226}$Np | 226 | 133 | -73.1761 | 1718.5427 | -104.26 % | 212342.2045 | +8509.69 ppm |
| ${}^{227}$Np | 227 | 134 | -66.5663 | 1726.8519 | -103.85 % | 213275.1602 | +8480.26 ppm |
| ${}^{228}$Np | 228 | 135 | -59.9647 | 1733.7120 | -103.46 % | 214208.1240 | +8444.07 ppm |
| ${}^{229}$Np | 229 | 136 | -53.3713 | 1741.7722 | -103.06 % | 215141.0960 | +8414.24 ppm |
| ${}^{230}$Np | 230 | 137 | -46.7859 | 1748.4083 | -102.68 % | 216074.0761 | +8377.85 ppm |
| ${}^{231}$Np | 231 | 138 | -40.2085 | 1756.0925 | -102.29 % | 217007.0641 | +8346.71 ppm |
| ${}^{232}$Np | 232 | 139 | -33.6391 | 1762.5040 | -101.91 % | 217940.0600 | +8309.59 ppm |
| ${}^{233}$Np | 233 | 140 | -27.0774 | 1769.9103 | -101.53 % | 218873.0638 | +8278.15 ppm |
| ${}^{234}$Np | 234 | 141 | -20.5235 | 1775.9753 | -101.16 % | 219806.0753 | +8240.46 ppm |
| ${}^{235}$Np | 235 | 142 | -13.9772 | 1782.9584 | -100.78 % | 220739.0945 | +8207.36 ppm |
| ${}^{236}$Np | 236 | 143 | -7.4386 | 1788.6947 | -100.42 % | 221672.1212 | +8168.85 ppm |
| ${}^{237}$Np | 237 | 144 | -0.9074 | 1795.2725 | -100.05 % | 222605.1555 | +8134.55 ppm |
| ${}^{238}$Np | 238 | 145 | 5.6162 | 1800.7608 | -99.69 % | 223538.1973 | +8095.61 ppm |
| ${}^{239}$Np | 239 | 146 | 12.1325 | 1806.9758 | -99.33 % | 224471.2464 | +8060.33 ppm |
| ${}^{240}$Np | 240 | 147 | 18.6415 | 1812.0418 | -98.97 % | 225404.3028 | +8020.19 ppm |
| ${}^{241}$Np | 241 | 148 | 25.1433 | 1818.1143 | -98.62 % | 226337.3665 | +7984.93 ppm |
| ${}^{242}$Np | 242 | 149 | 31.6379 | 1823.0838 | -98.26 % | 227270.4373 | +7945.07 ppm |
| ${}^{243}$Np | 243 | 150 | 38.1254 | 1828.8180 | -97.92 % | 228203.5153 | +7908.75 ppm |
| ${}^{244}$Np | 244 | 151 | 44.6058 | 1833.4160 | -97.57 % | 229136.6002 | +7868.12 ppm |
| ${}^{245}$Np | 245 | 152 | 51.0793 | 1838.9700 | -97.22 % | 230069.6922 | +7831.49 ppm |

### Plutonium (Z = 94)

_27 of 27 isotopes with a framework prediction; 27 of 27 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{221}$Pu | 221 | 127 | -130.8085 | 1674.2960 | -107.81 % | 207701.2275 | +8767.05 ppm |
| ${}^{222}$Pu | 222 | 128 | -124.1242 | 1683.2040 | -107.37 % | 208634.1086 | +8738.51 ppm |
| ${}^{223}$Pu | 223 | 129 | -117.4487 | 1690.3400 | -106.95 % | 209566.9986 | +8700.90 ppm |
| ${}^{224}$Pu | 224 | 130 | -110.7820 | 1699.2640 | -106.52 % | 210499.8973 | +8672.85 ppm |
| ${}^{225}$Pu | 225 | 131 | -104.1240 | 1706.1750 | -106.10 % | 211432.8047 | +8636.15 ppm |
| ${}^{226}$Pu | 226 | 132 | -97.4745 | 1714.8880 | -105.68 % | 212365.7206 | +8607.91 ppm |
| ${}^{227}$Pu | 227 | 133 | -90.8335 | 1721.7950 | -105.28 % | 213298.6451 | +8571.32 ppm |
| ${}^{228}$Pu | 228 | 134 | -84.2010 | 1730.6121 | -104.87 % | 214231.5779 | +8543.65 ppm |
| ${}^{229}$Pu | 229 | 135 | -77.5767 | 1737.3963 | -104.47 % | 215164.5191 | +8507.05 ppm |
| ${}^{230}$Pu | 230 | 136 | -70.9607 | 1745.9304 | -104.06 % | 216097.4685 | +8479.03 ppm |
| ${}^{231}$Pu | 231 | 137 | -64.3529 | 1752.6253 | -103.67 % | 217030.4261 | +8442.69 ppm |
| ${}^{232}$Pu | 232 | 138 | -57.7531 | 1760.6443 | -103.28 % | 217963.3917 | +8412.87 ppm |
| ${}^{233}$Pu | 233 | 139 | -51.1613 | 1767.0247 | -102.90 % | 218896.3654 | +8375.73 ppm |
| ${}^{234}$Pu | 234 | 140 | -44.5774 | 1774.7978 | -102.51 % | 219829.3469 | +8345.38 ppm |
| ${}^{235}$Pu | 235 | 141 | -38.0014 | 1781.0368 | -102.13 % | 220762.3363 | +8308.27 ppm |
| ${}^{236}$Pu | 236 | 142 | -31.4331 | 1788.3889 | -101.76 % | 221695.3334 | +8276.61 ppm |
| ${}^{237}$Pu | 237 | 143 | -24.8725 | 1794.2701 | -101.39 % | 222628.3383 | +8238.53 ppm |
| ${}^{238}$Pu | 238 | 144 | -18.3195 | 1801.2699 | -101.02 % | 223561.3507 | +8205.90 ppm |
| ${}^{239}$Pu | 239 | 145 | -11.7741 | 1806.9162 | -100.65 % | 224494.3707 | +8167.45 ppm |
| ${}^{240}$Pu | 240 | 146 | -5.2361 | 1813.4504 | -100.29 % | 225427.3981 | +8133.35 ppm |
| ${}^{241}$Pu | 241 | 147 | 1.2945 | 1818.6919 | -99.93 % | 226360.4330 | +8093.77 ppm |
| ${}^{242}$Pu | 242 | 148 | 7.8178 | 1825.0015 | -99.57 % | 227293.4751 | +8059.32 ppm |
| ${}^{243}$Pu | 243 | 149 | 14.3338 | 1830.0351 | -99.22 % | 228226.5245 | +8019.51 ppm |
| ${}^{244}$Pu | 244 | 150 | 20.8426 | 1836.0550 | -98.86 % | 229159.5812 | +7984.42 ppm |
| ${}^{245}$Pu | 245 | 151 | 27.3443 | 1840.7541 | -98.51 % | 230092.6449 | +7943.83 ppm |
| ${}^{246}$Pu | 246 | 152 | 33.8389 | 1846.6089 | -98.17 % | 231025.7157 | +7908.68 ppm |
| ${}^{247}$Pu | 247 | 153 | 40.3266 | 1850.7710 | -97.82 % | 231958.7934 | +7866.84 ppm |

### Americium (Z = 95)

_27 of 27 isotopes with a framework prediction; 27 of 27 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{223}$Am | 223 | 128 | -142.0765 | 1682.9810 | -108.44 % | 209590.8440 | +8783.73 ppm |
| ${}^{224}$Am | 224 | 129 | -135.3777 | 1690.3040 | -108.01 % | 210523.7107 | +8748.39 ppm |
| ${}^{225}$Am | 225 | 130 | -128.6878 | 1699.4250 | -107.57 % | 211456.5862 | +8720.29 ppm |
| ${}^{226}$Am | 226 | 131 | -122.0067 | 1706.7520 | -107.15 % | 212389.4704 | +8685.54 ppm |
| ${}^{227}$Am | 227 | 132 | -115.3342 | 1715.6660 | -106.72 % | 213322.3634 | +8657.67 ppm |
| ${}^{228}$Am | 228 | 133 | -108.6703 | 1722.9960 | -106.31 % | 214255.2649 | +8623.15 ppm |
| ${}^{229}$Am | 229 | 134 | -102.0149 | 1731.8285 | -105.89 % | 215188.1749 | +8595.30 ppm |
| ${}^{230}$Am | 230 | 135 | -95.3679 | 1739.2600 | -105.48 % | 216121.0934 | +8561.33 ppm |
| ${}^{231}$Am | 231 | 136 | -88.7292 | 1747.7460 | -105.08 % | 217054.0201 | +8533.10 ppm |
| ${}^{232}$Am | 232 | 137 | -82.0988 | 1754.8480 | -104.68 % | 217986.9551 | +8498.28 ppm |
| ${}^{233}$Am | 233 | 138 | -75.4766 | 1763.1110 | -104.28 % | 218919.8983 | +8469.12 ppm |
| ${}^{234}$Am | 234 | 139 | -68.8624 | 1769.9760 | -103.89 % | 219852.8496 | +8434.17 ppm |
| ${}^{235}$Am | 235 | 140 | -62.2563 | 1777.8122 | -103.50 % | 220785.8088 | +8404.23 ppm |
| ${}^{236}$Am | 236 | 141 | -55.6580 | 1784.3960 | -103.12 % | 221718.7760 | +8368.83 ppm |
| ${}^{237}$Am | 237 | 142 | -49.0677 | 1791.9570 | -102.74 % | 222651.7511 | +8337.81 ppm |
| ${}^{238}$Am | 238 | 143 | -42.4851 | 1798.2293 | -102.36 % | 223584.7339 | +8301.08 ppm |
| ${}^{239}$Am | 239 | 144 | -35.9102 | 1805.3317 | -101.99 % | 224517.7244 | +8268.69 ppm |
| ${}^{240}$Am | 240 | 145 | -29.3429 | 1811.2833 | -101.62 % | 225450.7226 | +8231.42 ppm |
| ${}^{241}$Am | 241 | 146 | -22.7832 | 1817.9304 | -101.25 % | 226383.7283 | +8197.61 ppm |
| ${}^{242}$Am | 242 | 147 | -16.2309 | 1823.4680 | -100.89 % | 227316.7415 | +8159.15 ppm |
| ${}^{243}$Am | 243 | 148 | -9.6861 | 1829.8323 | -100.53 % | 228249.7621 | +8124.72 ppm |
| ${}^{244}$Am | 244 | 149 | -3.1486 | 1835.1995 | -100.17 % | 229182.7900 | +8086.19 ppm |
| ${}^{245}$Am | 245 | 150 | 3.3816 | 1841.2496 | -99.82 % | 230115.8252 | +8051.02 ppm |
| ${}^{246}$Am | 246 | 151 | 9.9046 | 1846.2300 | -99.46 % | 231048.8677 | +8011.45 ppm |
| ${}^{247}$Am | 247 | 152 | 16.4204 | 1852.2530 | -99.11 % | 231981.9172 | +7976.32 ppm |
| ${}^{248}$Am | 248 | 153 | 22.9292 | 1856.7760 | -98.77 % | 232914.9739 | +7936.06 ppm |
| ${}^{249}$Am | 249 | 154 | 29.4310 | 1862.2710 | -98.42 % | 233848.0375 | +7899.92 ppm |

### Curium (Z = 96)

_22 of 22 isotopes with a framework prediction; 22 of 22 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{231}$Cm | 231 | 135 | -113.3376 | 1742.2020 | -106.51 % | 217077.8462 | +8621.03 ppm |
| ${}^{232}$Cm | 232 | 136 | -106.6763 | 1751.1360 | -106.09 % | 218010.7503 | +8594.77 ppm |
| ${}^{233}$Cm | 233 | 137 | -100.0233 | 1758.2185 | -105.69 % | 218943.6627 | +8559.96 ppm |
| ${}^{234}$Cm | 234 | 138 | -93.3785 | 1766.8607 | -105.28 % | 219876.5833 | +8532.57 ppm |
| ${}^{235}$Cm | 235 | 139 | -86.7419 | 1773.5450 | -104.89 % | 220809.5121 | +8496.88 ppm |
| ${}^{236}$Cm | 236 | 140 | -80.1134 | 1781.8729 | -104.50 % | 221742.4491 | +8468.18 ppm |
| ${}^{237}$Cm | 237 | 141 | -73.4929 | 1788.5499 | -104.11 % | 222675.3940 | +8432.66 ppm |
| ${}^{238}$Cm | 238 | 142 | -66.8804 | 1796.4232 | -103.72 % | 223608.3469 | +8402.92 ppm |
| ${}^{239}$Cm | 239 | 143 | -60.2757 | 1802.7928 | -103.34 % | 224541.3077 | +8366.65 ppm |
| ${}^{240}$Cm | 240 | 144 | -53.6789 | 1810.2868 | -102.97 % | 225474.2762 | +8335.78 ppm |
| ${}^{241}$Cm | 241 | 145 | -47.0897 | 1816.3806 | -102.59 % | 226407.2525 | +8298.92 ppm |
| ${}^{242}$Cm | 242 | 146 | -40.5082 | 1823.3500 | -102.22 % | 227340.2364 | +8266.32 ppm |
| ${}^{243}$Cm | 243 | 147 | -33.9342 | 1829.0430 | -101.86 % | 228273.2279 | +8228.33 ppm |
| ${}^{244}$Cm | 244 | 148 | -27.3678 | 1835.8445 | -101.49 % | 229206.2268 | +8195.61 ppm |
| ${}^{245}$Cm | 245 | 149 | -20.8088 | 1841.3631 | -101.13 % | 230139.2332 | +8157.51 ppm |
| ${}^{246}$Cm | 246 | 150 | -14.2571 | 1847.8220 | -100.77 % | 231072.2470 | +8123.90 ppm |
| ${}^{247}$Cm | 247 | 151 | -7.7127 | 1852.9772 | -100.42 % | 232005.2681 | +8084.88 ppm |
| ${}^{248}$Cm | 248 | 152 | -1.1756 | 1859.1888 | -100.06 % | 232938.2963 | +8050.82 ppm |
| ${}^{249}$Cm | 249 | 153 | 5.3544 | 1863.9022 | -99.71 % | 233871.3318 | +8010.55 ppm |
| ${}^{250}$Cm | 250 | 154 | 11.8773 | 1869.7346 | -99.36 % | 234804.3743 | +7975.47 ppm |
| ${}^{251}$Cm | 251 | 155 | 18.3932 | 1874.1475 | -99.02 % | 235737.4238 | +7934.59 ppm |
| ${}^{252}$Cm | 252 | 156 | 24.9021 | 1879.9200 | -98.68 % | 236670.4803 | +7899.43 ppm |

### Berkelium (Z = 97)

_22 of 22 isotopes with a framework prediction; 22 of 22 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{233}$Bk | 233 | 136 | -124.8013 | 1751.9270 | -107.12 % | 218967.6584 | +8645.05 ppm |
| ${}^{234}$Bk | 234 | 137 | -118.1256 | 1759.4460 | -106.71 % | 219900.5481 | +8611.63 ppm |
| ${}^{235}$Bk | 235 | 138 | -111.4583 | 1768.1400 | -106.30 % | 220833.4462 | +8584.28 ppm |
| ${}^{236}$Bk | 236 | 139 | -104.7992 | 1775.4280 | -105.90 % | 221766.3526 | +8550.80 ppm |
| ${}^{237}$Bk | 237 | 140 | -98.1483 | 1783.8990 | -105.50 % | 222699.2671 | +8522.68 ppm |
| ${}^{238}$Bk | 238 | 141 | -91.5056 | 1790.9500 | -105.11 % | 223632.1897 | +8488.74 ppm |
| ${}^{239}$Bk | 239 | 142 | -84.8708 | 1798.9530 | -104.72 % | 224565.1204 | +8459.53 ppm |
| ${}^{240}$Bk | 240 | 143 | -78.2440 | 1805.5200 | -104.33 % | 225498.0590 | +8424.37 ppm |
| ${}^{241}$Bk | 241 | 144 | -71.6251 | 1813.2840 | -103.95 % | 226431.0055 | +8394.47 ppm |
| ${}^{242}$Bk | 242 | 145 | -65.0140 | 1819.5980 | -103.57 % | 227363.9599 | +8358.35 ppm |
| ${}^{243}$Bk | 243 | 146 | -58.4106 | 1826.7530 | -103.20 % | 228296.9219 | +8326.27 ppm |
| ${}^{244}$Bk | 244 | 147 | -51.8149 | 1832.8001 | -102.83 % | 229229.8916 | +8289.67 ppm |
| ${}^{245}$Bk | 245 | 148 | -45.2267 | 1839.7715 | -102.46 % | 230162.8689 | +8257.48 ppm |
| ${}^{246}$Bk | 246 | 149 | -38.6461 | 1845.6897 | -102.09 % | 231095.8537 | +8220.95 ppm |
| ${}^{247}$Bk | 247 | 150 | -32.0729 | 1852.2384 | -101.73 % | 232028.8459 | +8187.52 ppm |
| ${}^{248}$Bk | 248 | 151 | -25.5071 | 1857.6682 | -101.37 % | 232961.8455 | +8149.51 ppm |
| ${}^{249}$Bk | 249 | 152 | -18.9486 | 1864.0242 | -101.02 % | 233894.8525 | +8115.85 ppm |
| ${}^{250}$Bk | 250 | 153 | -12.3974 | 1868.9898 | -100.66 % | 234827.8666 | +8076.48 ppm |
| ${}^{251}$Bk | 251 | 154 | -5.8533 | 1874.7852 | -100.31 % | 235760.8880 | +8041.04 ppm |
| ${}^{252}$Bk | 252 | 155 | 0.6837 | 1879.6680 | -99.96 % | 236693.9164 | +8001.48 ppm |
| ${}^{253}$Bk | 253 | 156 | 7.2136 | 1885.1030 | -99.62 % | 237626.9519 | +7966.17 ppm |
| ${}^{254}$Bk | 254 | 157 | 13.7366 | 1889.7600 | -99.27 % | 238559.9944 | +7926.60 ppm |

### Californium (Z = 98)

_20 of 20 isotopes with a framework prediction; 20 of 20 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{237}$Cf | 237 | 139 | -123.0338 | 1778.2941 | -106.92 % | 222723.3703 | +8610.23 ppm |
| ${}^{238}$Cf | 238 | 140 | -116.3605 | 1787.1420 | -106.51 % | 223656.2624 | +8583.38 ppm |
| ${}^{239}$Cf | 239 | 141 | -109.6954 | 1794.1730 | -106.11 % | 224589.1626 | +8549.60 ppm |
| ${}^{240}$Cf | 240 | 142 | -103.0383 | 1802.4576 | -105.72 % | 225522.0710 | +8521.27 ppm |
| ${}^{241}$Cf | 241 | 143 | -96.3894 | 1809.1870 | -105.33 % | 226454.9875 | +8486.25 ppm |
| ${}^{242}$Cf | 242 | 144 | -89.7483 | 1817.2020 | -104.94 % | 227387.9119 | +8457.26 ppm |
| ${}^{243}$Cf | 243 | 145 | -83.1152 | 1823.7150 | -104.56 % | 228320.8442 | +8421.68 ppm |
| ${}^{244}$Cf | 244 | 146 | -76.4899 | 1831.2535 | -104.18 % | 229253.7843 | +8391.37 ppm |
| ${}^{245}$Cf | 245 | 147 | -69.8724 | 1837.4178 | -103.80 % | 230186.7322 | +8355.07 ppm |
| ${}^{246}$Cf | 246 | 148 | -63.2625 | 1844.7840 | -103.43 % | 231119.6877 | +8324.39 ppm |
| ${}^{247}$Cf | 247 | 149 | -56.6602 | 1850.8362 | -103.06 % | 232052.6508 | +8288.24 ppm |
| ${}^{248}$Cf | 248 | 150 | -50.0654 | 1857.7789 | -102.69 % | 232985.6215 | +8256.29 ppm |
| ${}^{249}$Cf | 249 | 151 | -43.4781 | 1863.3655 | -102.33 % | 233918.5996 | +8218.74 ppm |
| ${}^{250}$Cf | 250 | 152 | -36.8982 | 1869.9892 | -101.97 % | 234851.5851 | +8186.02 ppm |
| ${}^{251}$Cf | 251 | 153 | -30.3256 | 1875.0959 | -101.62 % | 235784.5780 | +8147.04 ppm |
| ${}^{252}$Cf | 252 | 154 | -23.7603 | 1881.2675 | -101.26 % | 236717.5781 | +8112.98 ppm |
| ${}^{253}$Cf | 253 | 155 | -17.2021 | 1886.0719 | -100.91 % | 237650.5853 | +8073.37 ppm |
| ${}^{254}$Cf | 254 | 156 | -10.6511 | 1892.1034 | -100.56 % | 238583.5997 | +8039.33 ppm |
| ${}^{255}$Cf | 255 | 157 | -4.1072 | 1896.6900 | -100.22 % | 239516.6212 | +7999.54 ppm |
| ${}^{256}$Cf | 256 | 158 | 2.4298 | 1902.5920 | -99.87 % | 240449.6497 | +7965.30 ppm |

### Einsteinium (Z = 99)

_20 of 20 isotopes with a framework prediction; 20 of 20 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Prediction (MeV) | Reference (MeV) | Error | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error |
|---|---|---|---|---|---|---|---|
| ${}^{239}$Es | 239 | 140 | -134.7494 | 1787.9590 | -107.54 % | 224613.4343 | +8634.01 ppm |
| ${}^{240}$Es | 240 | 141 | -128.0618 | 1795.4400 | -107.13 % | 225546.3122 | +8601.55 ppm |
| ${}^{241}$Es | 241 | 142 | -121.3825 | 1803.8850 | -106.73 % | 226479.1983 | +8573.56 ppm |
| ${}^{242}$Es | 242 | 143 | -114.7113 | 1810.8860 | -106.33 % | 227412.0925 | +8540.29 ppm |
| ${}^{243}$Es | 243 | 144 | -108.0481 | 1819.0980 | -105.94 % | 228344.9947 | +8511.61 ppm |
| ${}^{244}$Es | 244 | 145 | -101.3929 | 1825.8520 | -105.55 % | 229277.9050 | +8477.30 ppm |
| ${}^{245}$Es | 245 | 146 | -94.7456 | 1833.8250 | -105.17 % | 230210.8231 | +8447.66 ppm |
| ${}^{246}$Es | 246 | 147 | -88.1062 | 1840.2731 | -104.79 % | 231143.7491 | +8412.96 ppm |
| ${}^{247}$Es | 247 | 148 | -81.4745 | 1847.5848 | -104.41 % | 232076.6828 | +8381.84 ppm |
| ${}^{248}$Es | 248 | 149 | -74.8504 | 1854.0480 | -104.04 % | 233009.6242 | +8346.81 ppm |
| ${}^{249}$Es | 249 | 150 | -68.2340 | 1861.0260 | -103.67 % | 233942.5732 | +8315.76 ppm |
| ${}^{250}$Es | 250 | 151 | -61.6252 | 1867.2500 | -103.30 % | 234875.5298 | +8279.91 ppm |
| ${}^{251}$Es | 251 | 152 | -55.0238 | 1873.9369 | -102.94 % | 235808.4938 | +8247.67 ppm |
| ${}^{252}$Es | 252 | 153 | -48.4298 | 1879.2252 | -102.58 % | 236741.4652 | +8209.30 ppm |
| ${}^{253}$Es | 253 | 154 | -41.8432 | 1885.5806 | -102.22 % | 237674.4440 | +8175.82 ppm |
| ${}^{254}$Es | 254 | 155 | -35.2638 | 1890.6683 | -101.87 % | 238607.4301 | +8137.24 ppm |
| ${}^{255}$Es | 255 | 156 | -28.6917 | 1896.6445 | -101.51 % | 239540.4234 | +8102.76 ppm |
| ${}^{256}$Es | 256 | 157 | -22.1266 | 1901.5680 | -101.16 % | 240473.4238 | +8064.35 ppm |
| ${}^{257}$Es | 257 | 158 | -15.5687 | 1907.4540 | -100.82 % | 241406.4312 | +8029.96 ppm |
| ${}^{258}$Es | 258 | 159 | -9.0178 | 1912.2960 | -100.47 % | 242339.4457 | +7991.35 ppm |

<!-- AUTO:per-z-sections END -->
