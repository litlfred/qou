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

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| $\mathfrak{n}$ | 1 | 1 | — | — | — | 939.5654 | +0.0010 ppm | 0.0005 ppm |

### Hydrogen (Z = 1)

_2 of 7 isotopes with a framework prediction; 3 of 7 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| $\mathfrak{p}$ | 1 | 0 | — | — | — | 938.7831 | +0.0145 ppm | 0.0000 ppm |
| ${}^{2}$H | 2 | 1 | 2.2488 | 2.2246 | +10903.0672 ppm | 1876.0997 | -12.9203 ppm | 0.0000 ppm |
| ${}^{3}$H | 3 | 2 | 8.4686 | 8.4818 | -1556.0163 ppm | 2809.4453 | +4.7032 ppm | 0.0000 ppm |
| ${}^{4}$H | 4 | 3 | — | 6.8818 | — | — | — | 26.6623 ppm |
| ${}^{5}$H | 5 | 4 | — | 6.6818 | — | — | — | 19.0693 ppm |
| ${}^{6}$H | 6 | 5 | — | 5.7698 | — | — | — | 45.1312 ppm |
| ${}^{7}$H | 7 | 6 | — | 6.5800 | — | — | — | 152.8482 ppm |

### Helium (Z = 2)

_2 of 8 isotopes with a framework prediction; 2 of 8 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{3}$He | 3 | 1 | 7.4889 | 7.7180 | -29686.5488 ppm | 2809.6427 | +81.5651 ppm | 0.0000 ppm |
| ${}^{4}$He | 4 | 2 | 28.2957 | 28.2957 | +0.4100 ppm | 3728.4013 | +0.0047 ppm | 0.0000 ppm |
| ${}^{5}$He | 5 | 3 | — | 27.5607 | — | — | — | 4.2837 ppm |
| ${}^{6}$He | 6 | 4 | — | 29.2711 | — | — | — | 0.0095 ppm |
| ${}^{7}$He | 7 | 5 | — | 28.8614 | — | — | — | 1.1547 ppm |
| ${}^{8}$He | 8 | 6 | — | 31.3962 | — | — | — | 0.0118 ppm |
| ${}^{9}$He | 9 | 7 | — | 30.1413 | — | — | — | 5.5572 ppm |
| ${}^{10}$He | 10 | 8 | — | 29.9513 | — | — | — | 9.9152 ppm |

### Lithium (Z = 3)

_2 of 11 isotopes with a framework prediction; 0 of 11 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{3}$Li | 3 | 0 | — | -6.8010 | — | — | — | 708.3997 ppm |
| ${}^{4}$Li | 4 | 1 | — | 4.6150 | — | — | — | 56.5489 ppm |
| ${}^{5}$Li | 5 | 2 | — | 26.3307 | — | — | — | 10.7085 ppm |
| ${}^{6}$Li | 6 | 3 | 43.6570 | 31.9940 | +364537.8264 ppm | — | — | 0.0003 ppm |
| ${}^{7}$Li | 7 | 4 | 51.3377 | 39.2451 | +308130.1073 ppm | — | — | 0.0006 ppm |
| ${}^{8}$Li | 8 | 5 | — | 41.2777 | — | — | — | 0.0062 ppm |
| ${}^{9}$Li | 9 | 6 | — | 45.3399 | — | — | — | 0.0222 ppm |
| ${}^{10}$Li | 10 | 7 | — | 45.3135 | — | — | — | 1.3608 ppm |
| ${}^{11}$Li | 11 | 8 | — | 45.7092 | — | — | — | 0.0598 ppm |
| ${}^{12}$Li | 12 | 9 | — | 45.4992 | — | — | — | 2.6727 ppm |
| ${}^{13}$Li | 13 | 10 | — | 45.5992 | — | — | — | 5.7537 ppm |

### Beryllium (Z = 4)

_3 of 12 isotopes with a framework prediction; 1 of 12 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{5}$Be | 5 | 1 | — | 0.0900 | — | — | — | 426.5983 ppm |
| ${}^{6}$Be | 6 | 2 | — | 26.9235 | — | — | — | 0.9715 ppm |
| ${}^{7}$Be | 7 | 3 | — | 37.6008 | — | — | — | 0.0108 ppm |
| ${}^{8}$Be | 8 | 4 | 62.3383 | 56.4995 | +103343.5842 ppm | 7451.0557 | -783.0070 ppm | 0.0046 ppm |
| ${}^{9}$Be | 9 | 5 | 67.3058 | 58.1640 | +157171.5035 ppm | — | — | 0.0091 ppm |
| ${}^{10}$Be | 10 | 6 | 75.5932 | 64.9763 | +163395.8386 ppm | — | — | 0.0086 ppm |
| ${}^{11}$Be | 11 | 7 | — | 65.4779 | — | — | — | 0.0231 ppm |
| ${}^{12}$Be | 12 | 8 | — | 68.6487 | — | — | — | 0.1703 ppm |
| ${}^{13}$Be | 13 | 9 | — | 68.1387 | — | — | — | 0.8384 ppm |
| ${}^{14}$Be | 14 | 10 | — | 69.9146 | — | — | — | 10.1097 ppm |
| ${}^{15}$Be | 15 | 11 | — | 68.1146 | — | — | — | 11.8238 ppm |
| ${}^{16}$Be | 16 | 12 | — | 68.5646 | — | — | — | 11.0817 ppm |

### Boron (Z = 5)

_2 of 16 isotopes with a framework prediction; 0 of 16 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{6}$B | 6 | 1 | — | -2.8020 | — | — | — | 355.3249 ppm |
| ${}^{7}$B | 7 | 2 | — | 24.9109 | — | — | — | 3.8408 ppm |
| ${}^{8}$B | 8 | 3 | — | 37.7372 | — | — | — | 0.1337 ppm |
| ${}^{9}$B | 9 | 4 | — | 56.3136 | — | — | — | 0.1075 ppm |
| ${}^{10}$B | 10 | 5 | 75.5932 | 64.7508 | +167446.9373 ppm | — | — | 0.0016 ppm |
| ${}^{11}$B | 11 | 6 | 83.8806 | 76.2051 | +100721.9525 ppm | — | — | 0.0012 ppm |
| ${}^{12}$B | 12 | 7 | — | 79.5747 | — | — | — | 0.1180 ppm |
| ${}^{13}$B | 13 | 8 | — | 84.4535 | — | — | — | 0.0824 ppm |
| ${}^{14}$B | 14 | 9 | — | 85.4230 | — | — | — | 1.6237 ppm |
| ${}^{15}$B | 15 | 10 | — | 88.2007 | — | — | — | 1.5019 ppm |
| ${}^{16}$B | 16 | 11 | — | 88.1177 | — | — | — | 1.6442 ppm |
| ${}^{17}$B | 17 | 12 | — | 89.5844 | — | — | — | 12.8536 ppm |
| ${}^{18}$B | 18 | 13 | — | 89.5794 | — | — | — | 12.1392 ppm |
| ${}^{19}$B | 19 | 14 | — | 89.6731 | — | — | — | 29.5843 ppm |
| ${}^{20}$B | 20 | 15 | — | 88.1131 | — | — | — | 29.2181 ppm |
| ${}^{21}$B | 21 | 16 | — | 87.2031 | — | — | — | 28.4455 ppm |

### Carbon (Z = 6)

_2 of 16 isotopes with a framework prediction; 1 of 16 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{8}$C | 8 | 2 | — | 24.8122 | — | — | — | 2.4365 ppm |
| ${}^{9}$C | 9 | 3 | — | 39.0368 | — | — | — | 0.2539 ppm |
| ${}^{10}$C | 10 | 4 | — | 60.3204 | — | — | — | 0.0075 ppm |
| ${}^{11}$C | 11 | 5 | — | 73.4410 | — | — | — | 0.0058 ppm |
| ${}^{12}$C | 12 | 6 | 97.1480 | 92.1617 | +54103.4210 ppm | 11172.9431 | -446.0735 ppm | 0.0000 ppm |
| ${}^{13}$C | 13 | 7 | 101.0622 | 97.1080 | +40718.6418 ppm | — | — | 0.0000 ppm |
| ${}^{14}$C | 14 | 8 | — | 105.2845 | — | — | — | 0.0003 ppm |
| ${}^{15}$C | 15 | 9 | — | 106.5025 | — | — | — | 0.0572 ppm |
| ${}^{16}$C | 16 | 10 | — | 110.7529 | — | — | — | 0.2398 ppm |
| ${}^{17}$C | 17 | 11 | — | 111.4864 | — | — | — | 1.0951 ppm |
| ${}^{18}$C | 18 | 12 | — | 115.6704 | — | — | — | 1.7866 ppm |
| ${}^{19}$C | 19 | 13 | — | 116.2472 | — | — | — | 5.5490 ppm |
| ${}^{20}$C | 20 | 14 | — | 119.2287 | — | — | — | 12.3544 ppm |
| ${}^{21}$C | 21 | 15 | — | 119.1540 | — | — | — | 30.4052 ppm |
| ${}^{22}$C | 22 | 16 | — | 119.2637 | — | — | — | 11.2667 ppm |
| ${}^{23}$C | 23 | 17 | — | 116.7710 | — | — | — | 46.3828 ppm |

### Nitrogen (Z = 7)

_2 of 16 isotopes with a framework prediction; 0 of 16 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{10}$N | 10 | 3 | — | 36.4367 | — | — | — | 42.7636 ppm |
| ${}^{11}$N | 11 | 4 | — | 58.9424 | — | — | — | 0.4868 ppm |
| ${}^{12}$N | 12 | 5 | — | 74.0413 | — | — | — | 0.0893 ppm |
| ${}^{13}$N | 13 | 6 | — | 94.1052 | — | — | — | 0.0222 ppm |
| ${}^{14}$N | 14 | 7 | 109.9563 | 104.6586 | +50618.9095 ppm | — | — | 0.0000 ppm |
| ${}^{15}$N | 15 | 8 | 118.8505 | 115.4919 | +29080.5482 ppm | — | — | 0.0000 ppm |
| ${}^{16}$N | 16 | 9 | — | 117.9808 | — | — | — | 0.1543 ppm |
| ${}^{17}$N | 17 | 10 | — | 123.8659 | — | — | — | 0.9468 ppm |
| ${}^{18}$N | 18 | 11 | — | 126.6941 | — | — | — | 1.1066 ppm |
| ${}^{19}$N | 19 | 12 | — | 132.0224 | — | — | — | 0.9260 ppm |
| ${}^{20}$N | 20 | 13 | — | 134.1834 | — | — | — | 4.2299 ppm |
| ${}^{21}$N | 21 | 14 | — | 138.7893 | — | — | — | 6.8438 ppm |
| ${}^{22}$N | 22 | 15 | — | 140.3278 | — | — | — | 10.1234 ppm |
| ${}^{23}$N | 23 | 16 | — | 143.4435 | — | — | — | 19.5968 ppm |
| ${}^{24}$N | 24 | 17 | — | 141.2880 | — | — | — | 17.8791 ppm |
| ${}^{25}$N | 25 | 18 | — | 140.3250 | — | — | — | 21.5482 ppm |

### Oxygen (Z = 8)

_3 of 18 isotopes with a framework prediction; 1 of 18 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{11}$O | 11 | 3 | — | 34.7868 | — | — | — | 5.8322 ppm |
| ${}^{12}$O | 12 | 4 | — | 58.5837 | — | — | — | 1.0704 ppm |
| ${}^{13}$O | 13 | 5 | — | 75.5529 | — | — | — | 0.7851 ppm |
| ${}^{14}$O | 14 | 6 | — | 98.7319 | — | — | — | 0.0019 ppm |
| ${}^{15}$O | 15 | 7 | — | 111.9554 | — | — | — | 0.0351 ppm |
| ${}^{16}$O | 16 | 8 | 134.3846 | 127.6193 | +53011.8106 ppm | 14892.4034 | -454.0666 ppm | 0.0000 ppm |
| ${}^{17}$O | 17 | 9 | 137.2455 | 131.7624 | +41613.8940 ppm | — | — | 0.0000 ppm |
| ${}^{18}$O | 18 | 10 | 146.7464 | 139.8078 | +49630.1703 ppm | — | — | 0.0000 ppm |
| ${}^{19}$O | 19 | 11 | — | 143.7634 | — | — | — | 0.1489 ppm |
| ${}^{20}$O | 20 | 12 | — | 151.3714 | — | — | — | 0.0475 ppm |
| ${}^{21}$O | 21 | 13 | — | 155.1769 | — | — | — | 0.6132 ppm |
| ${}^{22}$O | 22 | 14 | — | 162.0272 | — | — | — | 2.7763 ppm |
| ${}^{23}$O | 23 | 15 | — | 164.7602 | — | — | — | 5.6771 ppm |
| ${}^{24}$O | 24 | 16 | — | 168.9525 | — | — | — | 7.3689 ppm |
| ${}^{25}$O | 25 | 17 | — | 168.1951 | — | — | — | 7.0807 ppm |
| ${}^{26}$O | 26 | 18 | — | 168.9345 | — | — | — | 6.8011 ppm |
| ${}^{27}$O | 27 | 19 | — | 166.9950 | — | — | — | 19.8536 ppm |
| ${}^{28}$O | 28 | 20 | — | 167.6640 | — | — | — | 26.7323 ppm |

### Fluorine (Z = 9)

_1 of 19 isotopes with a framework prediction; 0 of 19 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{13}$F | 13 | 4 | — | 55.8610 | — | — | — | 41.1648 ppm |
| ${}^{14}$F | 14 | 5 | — | 73.9929 | — | — | — | 3.1453 ppm |
| ${}^{15}$F | 15 | 6 | — | 97.4619 | — | — | — | 1.0007 ppm |
| ${}^{16}$F | 16 | 7 | — | 111.4248 | — | — | — | 0.3596 ppm |
| ${}^{17}$F | 17 | 8 | — | 128.2196 | — | — | — | 0.0156 ppm |
| ${}^{18}$F | 18 | 9 | — | 137.3695 | — | — | — | 0.0276 ppm |
| ${}^{19}$F | 19 | 10 | 156.2474 | 147.8014 | +57144.2100 ppm | — | — | 0.0000 ppm |
| ${}^{20}$F | 20 | 11 | — | 154.4027 | — | — | — | 0.0016 ppm |
| ${}^{21}$F | 21 | 12 | — | 162.5042 | — | — | — | 0.0920 ppm |
| ${}^{22}$F | 22 | 13 | — | 167.7345 | — | — | — | 0.6049 ppm |
| ${}^{23}$F | 23 | 14 | — | 175.3139 | — | — | — | 1.5550 ppm |
| ${}^{24}$F | 24 | 15 | — | 179.1260 | — | — | — | 4.3674 ppm |
| ${}^{25}$F | 25 | 16 | — | 183.4077 | — | — | — | 4.1394 ppm |
| ${}^{26}$F | 26 | 17 | — | 184.1385 | — | — | — | 4.4157 ppm |
| ${}^{27}$F | 27 | 18 | — | 185.7510 | — | — | — | 4.7744 ppm |
| ${}^{28}$F | 28 | 19 | — | 185.5520 | — | — | — | 4.6083 ppm |
| ${}^{29}$F | 29 | 20 | — | 186.8769 | — | — | — | 19.4194 ppm |
| ${}^{30}$F | 30 | 21 | — | 186.1500 | — | — | — | 17.8687 ppm |
| ${}^{31}$F | 31 | 22 | — | 186.3410 | — | — | — | 18.4798 ppm |

### Neon (Z = 10)

_3 of 20 isotopes with a framework prediction; 1 of 20 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{15}$Ne | 15 | 5 | — | 73.0309 | — | — | — | 4.7588 ppm |
| ${}^{16}$Ne | 16 | 6 | — | 97.3308 | — | — | — | 1.3719 ppm |
| ${}^{17}$Ne | 17 | 7 | — | 112.8885 | — | — | — | 0.0223 ppm |
| ${}^{18}$Ne | 18 | 8 | — | 132.1426 | — | — | — | 0.0217 ppm |
| ${}^{19}$Ne | 19 | 9 | — | 143.7795 | — | — | — | 0.0090 ppm |
| ${}^{20}$Ne | 20 | 10 | 174.0483 | 160.6448 | +83435.3522 ppm | 18609.4368 | -719.7244 ppm | 0.0001 ppm |
| ${}^{21}$Ne | 21 | 11 | 175.8559 | 167.4060 | +50475.7030 ppm | — | — | 0.0020 ppm |
| ${}^{22}$Ne | 22 | 12 | 185.9636 | 177.7702 | +46089.4492 ppm | — | — | 0.0008 ppm |
| ${}^{23}$Ne | 23 | 13 | — | 182.9709 | — | — | — | 0.0049 ppm |
| ${}^{24}$Ne | 24 | 14 | — | 191.8398 | — | — | — | 0.0229 ppm |
| ${}^{25}$Ne | 25 | 15 | — | 195.9950 | — | — | — | 1.2473 ppm |
| ${}^{26}$Ne | 26 | 16 | — | 201.5497 | — | — | — | 0.7609 ppm |
| ${}^{27}$Ne | 27 | 17 | — | 203.0512 | — | — | — | 3.6081 ppm |
| ${}^{28}$Ne | 28 | 18 | — | 206.8737 | — | — | — | 4.8314 ppm |
| ${}^{29}$Ne | 29 | 19 | — | 207.8450 | — | — | — | 5.5307 ppm |
| ${}^{30}$Ne | 30 | 20 | — | 211.0360 | — | — | — | 9.0550 ppm |
| ${}^{31}$Ne | 31 | 21 | — | 211.2058 | — | — | — | 9.2085 ppm |
| ${}^{32}$Ne | 32 | 22 | — | 213.4720 | — | — | — | 16.8541 ppm |
| ${}^{33}$Ne | 33 | 23 | — | 212.3880 | — | — | — | 19.4859 ppm |
| ${}^{34}$Ne | 34 | 24 | — | 213.7580 | — | — | — | 16.1789 ppm |

### Fermium (Z = 100)

_20 of 20 isotopes with a framework prediction; 20 of 20 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{241}$Fm | 241 | 141 | -146.6045 | 1797.6190 | -1081554.8112 ppm | 226503.6379 | +8658.4643 ppm | 1.3357 ppm |
| ${}^{242}$Fm | 242 | 142 | -139.9027 | 1806.5300 | -1077442.7961 ppm | 227436.5016 | +8632.4410 ppm | 1.7763 ppm |
| ${}^{243}$Fm | 243 | 143 | -133.2092 | 1813.7520 | -1073444.0044 ppm | 228369.3735 | +8598.9294 ppm | 0.5760 ppm |
| ${}^{244}$Fm | 244 | 144 | -126.5238 | 1822.1920 | -1069434.9590 ppm | 229302.2535 | +8571.3566 ppm | 0.8850 ppm |
| ${}^{245}$Fm | 245 | 145 | -119.8465 | 1828.9250 | -1065528.3891 ppm | 230235.1416 | +8537.0646 ppm | 0.8569 ppm |
| ${}^{246}$Fm | 246 | 146 | -113.1772 | 1837.1184 | -1061605.8190 ppm | 231168.0377 | +8508.4908 ppm | 0.0596 ppm |
| ${}^{247}$Fm | 247 | 147 | -106.5158 | 1843.6080 | -1057775.7139 ppm | 232100.9418 | +8473.6875 ppm | 0.7852 ppm |
| ${}^{248}$Fm | 248 | 148 | -99.8622 | 1851.5544 | -1053934.2504 ppm | 233033.8536 | +8444.6838 ppm | 0.0368 ppm |
| ${}^{249}$Fm | 249 | 149 | -93.2164 | 1858.0044 | -1050170.1711 ppm | 233966.7732 | +8409.8771 ppm | 0.0268 ppm |
| ${}^{250}$Fm | 250 | 150 | -86.5783 | 1865.5226 | -1046409.6723 ppm | 234899.7005 | +8380.0067 ppm | 0.0339 ppm |
| ${}^{251}$Fm | 251 | 151 | -79.9478 | 1871.7073 | -1042713.8459 ppm | 235832.6355 | +8344.6574 ppm | 0.0611 ppm |
| ${}^{252}$Fm | 252 | 152 | -73.3249 | 1878.9208 | -1039025.0079 ppm | 236765.5780 | +8314.0393 ppm | 0.0222 ppm |
| ${}^{253}$Fm | 253 | 153 | -66.7095 | 1884.4632 | -1035399.7213 ppm | 237698.5280 | +8276.5476 ppm | 0.0066 ppm |
| ${}^{254}$Fm | 254 | 154 | -60.1015 | 1890.9776 | -1031783.2779 ppm | 238631.4854 | +8243.5238 ppm | 0.0078 ppm |
| ${}^{255}$Fm | 255 | 155 | -53.5008 | 1896.1509 | -1028215.4825 ppm | 239564.4502 | +8205.1004 ppm | 0.0166 ppm |
| ${}^{256}$Fm | 256 | 156 | -46.9074 | 1902.5379 | -1024655.1980 ppm | 240497.4222 | +8172.1376 ppm | 0.0127 ppm |
| ${}^{257}$Fm | 257 | 157 | -40.3213 | 1907.5039 | -1021138.2574 ppm | 241430.4015 | +8133.4800 ppm | 0.0182 ppm |
| ${}^{258}$Fm | 258 | 158 | -33.7423 | 1913.8440 | -1017630.6567 ppm | 242363.3880 | +8100.4730 ppm | 0.8330 ppm |
| ${}^{259}$Fm | 259 | 159 | -27.1704 | 1918.4130 | -1014162.9772 ppm | 243296.3815 | +8061.7302 ppm | 1.1733 ppm |
| ${}^{260}$Fm | 260 | 160 | -20.6056 | 1924.5200 | -1010706.8698 ppm | 244229.3821 | +8028.3768 ppm | 1.7954 ppm |

### Mendelevium (Z = 101)

_19 of 19 isotopes with a framework prediction; 19 of 19 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{244}$Md | 244 | 143 | -151.8827 | 1814.8720 | -1083687.8282 ppm | 229326.8301 | +8650.0270 ppm | 1.6470 ppm |
| ${}^{245}$Md | 245 | 144 | -145.1750 | 1823.0450 | -1079633.2753 ppm | 230259.6878 | +8621.9116 ppm | 1.1384 ppm |
| ${}^{246}$Md | 246 | 145 | -138.4755 | 1830.4860 | -1075649.6058 ppm | 231192.5538 | +8589.3796 ppm | 1.1338 ppm |
| ${}^{247}$Md | 247 | 146 | -131.7841 | 1838.6680 | -1071673.6898 ppm | 232125.4278 | +8561.3996 ppm | 0.9025 ppm |
| ${}^{248}$Md | 248 | 147 | -125.1007 | 1845.6160 | -1067782.6244 ppm | 233058.3098 | +8528.4762 ppm | 0.7981 ppm |
| ${}^{249}$Md | 249 | 148 | -118.4252 | 1853.5602 | -1063890.6677 ppm | 233991.1997 | +8499.2398 ppm | 0.7087 ppm |
| ${}^{250}$Md | 250 | 149 | -111.7576 | 1860.4133 | -1060071.3589 ppm | 234924.0975 | +8466.0060 ppm | 0.3903 ppm |
| ${}^{251}$Md | 251 | 150 | -105.0977 | 1867.9170 | -1056264.6489 ppm | 235857.0030 | +8435.8758 ppm | 0.0809 ppm |
| ${}^{252}$Md | 252 | 151 | -98.4455 | 1874.4880 | -1052518.6324 ppm | 236789.9163 | +8402.0118 ppm | 0.3888 ppm |
| ${}^{253}$Md | 253 | 152 | -91.8010 | 1881.8140 | -1048783.2680 ppm | 237722.8372 | +8371.8458 ppm | 0.1343 ppm |
| ${}^{254}$Md | 254 | 153 | -85.1641 | 1887.7280 | -1045114.6030 ppm | 238655.7657 | +8335.2466 ppm | 0.4211 ppm |
| ${}^{255}$Md | 255 | 154 | -78.5347 | 1894.3270 | -1041457.8188 ppm | 239588.7017 | +8302.7427 ppm | 0.0234 ppm |
| ${}^{256}$Md | 256 | 155 | -71.9127 | 1899.7760 | -1037853.2349 ppm | 240521.6451 | +8265.3485 ppm | 0.5193 ppm |
| ${}^{257}$Md | 257 | 156 | -65.2980 | 1906.3192 | -1034253.4649 ppm | 241454.5959 | +8232.8139 ppm | 0.0065 ppm |
| ${}^{258}$Md | 258 | 157 | -58.6907 | 1911.6927 | -1030700.9146 ppm | 242387.5540 | +8195.6913 ppm | 0.0144 ppm |
| ${}^{259}$Md | 259 | 158 | -52.0906 | 1917.8950 | -1027160.3123 ppm | 243320.5194 | +8162.3293 ppm | 0.4168 ppm |
| ${}^{260}$Md | 260 | 159 | -45.4977 | 1922.9600 | -1023660.2507 ppm | 244253.4919 | +8124.6276 ppm | 1.3033 ppm |
| ${}^{261}$Md | 261 | 160 | -38.9119 | 1929.0510 | -1020171.5328 ppm | 245186.4715 | +8091.2099 ppm | 2.0911 ppm |
| ${}^{262}$Md | 262 | 161 | -32.3332 | 1934.0840 | -1016717.5596 ppm | 246119.4582 | +8053.7000 ppm | 1.8351 ppm |

### Nobelium (Z = 102)

_17 of 17 isotopes with a framework prediction; 17 of 17 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{248}$No | 248 | 146 | -150.5659 | 1841.1520 | -1081778.1113 ppm | 233082.9927 | +8618.9604 ppm | 0.9714 ppm |
| ${}^{249}$No | 249 | 147 | -143.8604 | 1848.0780 | -1077843.2746 ppm | 234015.8526 | +8585.4708 ppm | 1.2044 ppm |
| ${}^{250}$No | 250 | 148 | -137.1630 | 1856.5000 | -1073882.5557 ppm | 234948.7205 | +8557.9942 ppm | 0.8597 ppm |
| ${}^{251}$No | 251 | 149 | -130.4734 | 1863.1730 | -1070027.5412 ppm | 235881.5964 | +8524.2875 ppm | 0.7726 ppm |
| ${}^{252}$No | 252 | 150 | -123.7917 | 1871.3014 | -1066152.7582 ppm | 236814.4802 | +8496.2946 ppm | 0.0396 ppm |
| ${}^{253}$No | 253 | 151 | -117.1179 | 1877.8854 | -1062366.8880 ppm | 237747.3717 | +8462.2895 ppm | 0.0293 ppm |
| ${}^{254}$No | 254 | 152 | -110.4517 | 1885.5921 | -1058576.6725 ppm | 238680.2710 | +8433.3687 ppm | 0.0408 ppm |
| ${}^{255}$No | 255 | 153 | -103.7932 | 1891.5748 | -1054871.3207 ppm | 239613.1779 | +8397.3905 ppm | 0.0591 ppm |
| ${}^{256}$No | 256 | 154 | -97.1423 | 1898.6350 | -1051164.2776 ppm | 240546.0924 | +8366.2804 ppm | 0.0316 ppm |
| ${}^{257}$No | 257 | 155 | -90.4989 | 1904.2823 | -1047523.8814 ppm | 241479.0144 | +8329.4950 ppm | 0.0259 ppm |
| ${}^{258}$No | 258 | 156 | -83.8629 | 1911.0060 | -1043884.1812 ppm | 242411.9439 | +8298.0327 ppm | 0.4146 ppm |
| ${}^{259}$No | 259 | 157 | -77.2344 | 1916.5926 | -1040297.7482 ppm | 243344.8808 | +8261.1138 ppm | 0.0264 ppm |
| ${}^{260}$No | 260 | 158 | -70.6131 | 1923.2200 | -1036716.0888 ppm | 244277.8249 | +8228.9703 ppm | 0.8266 ppm |
| ${}^{261}$No | 261 | 159 | -63.9991 | 1928.2680 | -1033189.9512 ppm | 245210.7764 | +8191.6498 ppm | 0.8234 ppm |
| ${}^{262}$No | 262 | 160 | -57.3923 | 1934.8700 | -1029662.1043 ppm | 246143.7350 | +8159.5984 ppm | 1.4765 ppm |
| ${}^{263}$No | 263 | 161 | -50.7926 | 1939.8880 | -1026183.2838 ppm | 247076.7007 | +8122.1341 ppm | 1.9992 ppm |
| ${}^{264}$No | 264 | 162 | -44.2000 | 1945.9440 | -1022713.9247 ppm | 248009.6735 | +8089.6817 ppm | 2.4005 ppm |

### Lawrencium (Z = 103)

_16 of 16 isotopes with a framework prediction; 16 of 16 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{251}$Lr | 251 | 148 | -156.0750 | 1857.4000 | -1084028.7518 ppm | 235906.4157 | +8608.9250 ppm | 0.8563 ppm |
| ${}^{252}$Lr | 252 | 149 | -149.3635 | 1864.8000 | -1080096.2626 ppm | 236839.2696 | +8577.5296 ppm | 0.7854 ppm |
| ${}^{253}$Lr | 253 | 150 | -142.6600 | 1872.9383 | -1076169.0707 ppm | 237772.1315 | +8549.4970 ppm | 0.6979 ppm |
| ${}^{254}$Lr | 254 | 151 | -135.9643 | 1879.8872 | -1072325.7760 ppm | 238705.0012 | +8516.8797 ppm | 0.3858 ppm |
| ${}^{255}$Lr | 255 | 152 | -129.2764 | 1887.6571 | -1068485.1287 ppm | 239637.8788 | +8488.0357 ppm | 0.0745 ppm |
| ${}^{256}$Lr | 256 | 153 | -122.5963 | 1893.9291 | -1064731.2039 ppm | 240570.7641 | +8453.1173 ppm | 0.3475 ppm |
| ${}^{257}$Lr | 257 | 154 | -115.9238 | 1901.0290 | -1060979.5273 ppm | 241503.6571 | +8422.2121 ppm | 0.1828 ppm |
| ${}^{258}$Lr | 258 | 155 | -109.2590 | 1907.1360 | -1057289.5626 ppm | 242436.5576 | +8386.5500 ppm | 0.4223 ppm |
| ${}^{259}$Lr | 259 | 156 | -102.6017 | 1914.0100 | -1053605.6004 ppm | 243369.4657 | +8355.5770 ppm | 0.2933 ppm |
| ${}^{260}$Lr | 260 | 157 | -95.9518 | 1919.5800 | -1049985.8235 ppm | 244302.3813 | +8319.2250 ppm | 0.5152 ppm |
| ${}^{261}$Lr | 261 | 158 | -89.3093 | 1926.4410 | -1046359.7467 ppm | 245235.3042 | +8287.9285 ppm | 0.8234 ppm |
| ${}^{262}$Lr | 262 | 159 | -82.6742 | 1931.9880 | -1042792.2841 ppm | 246168.2345 | +8251.6659 ppm | 0.8203 ppm |
| ${}^{263}$Lr | 263 | 160 | -76.0463 | 1938.5730 | -1039227.9841 ppm | 247101.1721 | +8219.7634 ppm | 0.9122 ppm |
| ${}^{264}$Lr | 264 | 161 | -69.4256 | 1943.8320 | -1035715.8683 ppm | 248034.1168 | +8183.4484 ppm | 1.7720 ppm |
| ${}^{265}$Lr | 265 | 162 | -62.8121 | 1950.1350 | -1032209.1176 ppm | 248967.0687 | +8150.8975 ppm | 2.2141 ppm |
| ${}^{266}$Lr | 266 | 163 | -56.2057 | 1954.8340 | -1028752.1542 ppm | 249900.0277 | +8112.2334 ppm | 2.1757 ppm |

### Rutherfordium (Z = 104)

_16 of 16 isotopes with a framework prediction; 16 of 16 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{253}$Rf | 253 | 149 | -168.4273 | 1867.1400 | -1090206.0540 ppm | 237797.1165 | +8633.5799 ppm | 1.7384 ppm |
| ${}^{254}$Rf | 254 | 150 | -161.7019 | 1875.5360 | -1086216.3480 ppm | 238729.9565 | +8607.1664 ppm | 1.1964 ppm |
| ${}^{255}$Rf | 255 | 151 | -154.9844 | 1882.4100 | -1082332.9434 ppm | 239662.8044 | +8574.3315 ppm | 0.7605 ppm |
| ${}^{256}$Rf | 256 | 152 | -148.2747 | 1890.6713 | -1078424.3843 ppm | 240595.6602 | +8547.0143 ppm | 0.0748 ppm |
| ${}^{257}$Rf | 257 | 153 | -141.5729 | 1897.0983 | -1074626.0402 ppm | 241528.5238 | +8512.5643 ppm | 0.0452 ppm |
| ${}^{258}$Rf | 258 | 154 | -134.8789 | 1904.6916 | -1070814.0217 ppm | 242461.3952 | +8483.3067 ppm | 0.0670 ppm |
| ${}^{259}$Rf | 259 | 155 | -128.1925 | 1910.6430 | -1067093.9029 ppm | 243394.2742 | +8447.8539 ppm | 0.3010 ppm |
| ${}^{260}$Rf | 260 | 156 | -121.5137 | 1918.0200 | -1063353.7335 ppm | 244327.1609 | +8417.8701 ppm | 0.8266 ppm |
| ${}^{261}$Rf | 261 | 157 | -114.8425 | 1923.9317 | -1059691.5699 ppm | 245260.0551 | +8382.3906 ppm | 0.2700 ppm |
| ${}^{262}$Rf | 262 | 158 | -108.1788 | 1930.9400 | -1056023.8824 ppm | 246192.9567 | +8351.7379 ppm | 0.9156 ppm |
| ${}^{263}$Rf | 263 | 159 | -101.5224 | 1936.7320 | -1052419.4465 ppm | 247125.8658 | +8316.0426 ppm | 0.6233 ppm |
| ${}^{264}$Rf | 264 | 160 | -94.8734 | 1943.3040 | -1048820.6839 ppm | 248058.7823 | +8284.9352 ppm | 1.4653 ppm |
| ${}^{265}$Rf | 265 | 161 | -88.2317 | 1948.8100 | -1045274.6674 ppm | 248991.7060 | +8248.7985 ppm | 1.4597 ppm |
| ${}^{266}$Rf | 266 | 162 | -81.5972 | 1955.3660 | -1041729.9058 ppm | 249924.6369 | +8217.7142 ppm | 1.6647 ppm |
| ${}^{267}$Rf | 267 | 163 | -74.9699 | 1960.3140 | -1038243.8280 ppm | 250857.5750 | +8179.3508 ppm | 2.3098 ppm |
| ${}^{268}$Rf | 268 | 164 | -68.3497 | 1966.3160 | -1034760.2727 ppm | 251790.5202 | +8146.4541 ppm | 2.6518 ppm |

### Dubnium (Z = 105)

_16 of 16 isotopes with a framework prediction; 16 of 16 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{255}$Db | 255 | 150 | -180.9170 | 1876.5450 | -1096409.6064 ppm | 239687.9547 | +8657.8238 ppm | 1.1917 ppm |
| ${}^{256}$Db | 256 | 151 | -174.1776 | 1883.9040 | -1092455.6469 ppm | 240620.7807 | +8626.6280 ppm | 0.7848 ppm |
| ${}^{257}$Db | 257 | 152 | -167.4461 | 1892.0280 | -1088500.8726 ppm | 241553.6147 | +8599.2740 ppm | 0.6874 ppm |
| ${}^{258}$Db | 258 | 153 | -160.7226 | 1898.7459 | -1084646.7100 ppm | 242486.4566 | +8565.8857 ppm | 0.3821 ppm |
| ${}^{259}$Db | 259 | 154 | -154.0069 | 1906.3339 | -1080786.9422 ppm | 243419.3063 | +8536.4237 ppm | 0.2349 ppm |
| ${}^{260}$Db | 260 | 155 | -147.2989 | 1912.8200 | -1077006.1683 ppm | 244352.1637 | +8502.2332 ppm | 0.3845 ppm |
| ${}^{261}$Db | 261 | 156 | -140.5987 | 1920.1770 | -1073221.7291 ppm | 245285.0289 | +8472.6745 ppm | 0.4519 ppm |
| ${}^{262}$Db | 262 | 157 | -133.9060 | 1926.2240 | -1069517.3790 ppm | 246217.9017 | +8437.9633 ppm | 0.5875 ppm |
| ${}^{263}$Db | 263 | 158 | -127.2210 | 1933.5760 | -1065795.6882 ppm | 247150.7820 | +8408.0238 ppm | 0.6841 ppm |
| ${}^{264}$Db | 264 | 159 | -120.5434 | 1939.3440 | -1062156.7773 ppm | 248083.6699 | +8373.0347 ppm | 0.9579 ppm |
| ${}^{265}$Db | 265 | 160 | -113.8732 | 1946.4250 | -1058503.7737 ppm | 249016.5651 | +8342.5506 ppm | 0.9053 ppm |
| ${}^{266}$Db | 266 | 161 | -107.2104 | 1952.1740 | -1054918.4668 ppm | 249949.4677 | +8307.2901 ppm | 1.1423 ppm |
| ${}^{267}$Db | 267 | 162 | -100.5549 | 1958.9790 | -1051330.2570 ppm | 250882.3777 | +8276.7209 ppm | 1.5049 ppm |
| ${}^{268}$Db | 268 | 163 | -93.9066 | 1963.9040 | -1047816.2999 ppm | 251815.2948 | +8239.2531 ppm | 2.1184 ppm |
| ${}^{269}$Db | 269 | 164 | -87.2655 | 1969.8870 | -1044299.7606 ppm | 252748.2191 | +8205.9443 ppm | 2.4858 ppm |
| ${}^{270}$Db | 270 | 165 | -80.6315 | 1974.7800 | -1040830.6413 ppm | 253681.1506 | +8168.2607 ppm | 2.2841 ppm |

### Seaborgium (Z = 106)

_16 of 16 isotopes with a framework prediction; 16 of 16 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{258}$Sg | 258 | 152 | -186.7901 | 1894.2360 | -1098609.7555 ppm | 242511.7418 | +8655.1604 ppm | 1.7163 ppm |
| ${}^{259}$Sg | 259 | 153 | -180.0448 | 1901.0600 | -1094707.6002 ppm | 243444.5619 | +8622.1402 ppm | 0.7487 ppm |
| ${}^{260}$Sg | 260 | 154 | -173.3074 | 1909.0664 | -1090781.2410 ppm | 244377.3899 | +8594.3800 ppm | 0.0848 ppm |
| ${}^{261}$Sg | 261 | 155 | -166.5778 | 1915.6802 | -1086954.9338 ppm | 245310.2257 | +8560.9385 ppm | 0.0760 ppm |
| ${}^{262}$Sg | 262 | 156 | -159.8560 | 1923.3875 | -1083111.7215 ppm | 246243.0694 | +8532.3010 ppm | 0.0908 ppm |
| ${}^{263}$Sg | 263 | 157 | -153.1419 | 1929.6310 | -1079363.3308 ppm | 247175.9207 | +8497.8982 ppm | 0.3839 ppm |
| ${}^{264}$Sg | 264 | 158 | -146.4355 | 1937.2320 | -1075590.0565 ppm | 248108.7796 | +8468.8619 ppm | 1.1510 ppm |
| ${}^{265}$Sg | 265 | 159 | -139.7366 | 1943.2450 | -1071908.8830 ppm | 249041.6462 | +8434.2634 ppm | 0.5620 ppm |
| ${}^{266}$Sg | 266 | 160 | -133.0452 | 1950.3120 | -1068217.3830 ppm | 249974.5202 | +8404.7870 ppm | 0.9883 ppm |
| ${}^{267}$Sg | 267 | 161 | -126.3612 | 1956.3090 | -1064591.6479 ppm | 250907.4017 | +8370.0274 ppm | 1.0519 ppm |
| ${}^{268}$Sg | 268 | 162 | -119.6846 | 1963.3680 | -1060958.8408 ppm | 251840.2905 | +8340.3859 ppm | 1.8797 ppm |
| ${}^{269}$Sg | 269 | 163 | -113.0154 | 1968.5420 | -1057410.6947 ppm | 252773.1866 | +8303.3510 ppm | 1.4677 ppm |
| ${}^{270}$Sg | 270 | 164 | -106.3533 | 1974.7800 | -1053855.7908 ppm | 253706.0900 | +8271.2446 ppm | 1.8213 ppm |
| ${}^{271}$Sg | 271 | 165 | -99.6985 | 1979.6550 | -1050361.5530 ppm | 254639.0006 | +8233.6290 ppm | 2.3383 ppm |
| ${}^{272}$Sg | 272 | 166 | -93.0508 | 1985.8720 | -1046856.3877 ppm | 255571.9183 | +8201.4202 ppm | 2.7303 ppm |
| ${}^{273}$Sg | 273 | 167 | -86.4101 | 1990.7160 | -1043406.5645 ppm | 256504.8431 | +8163.5441 ppm | 1.5706 ppm |

### Bohrium (Z = 107)

_19 of 19 isotopes with a framework prediction; 19 of 19 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{260}$Bh | 260 | 153 | -199.5392 | 1901.6400 | -1104930.0451 ppm | 244402.8393 | +8672.0393 ppm | 0.8112 ppm |
| ${}^{261}$Bh | 261 | 154 | -192.7800 | 1909.8235 | -1100941.2696 ppm | 245335.6456 | +8644.4057 ppm | 0.7392 ppm |
| ${}^{262}$Bh | 262 | 155 | -186.0288 | 1916.7221 | -1097055.6769 ppm | 246268.4597 | +8611.9893 ppm | 0.3812 ppm |
| ${}^{263}$Bh | 263 | 156 | -179.2854 | 1924.6340 | -1093152.9626 ppm | 247201.2818 | +8583.6756 ppm | 1.2466 ppm |
| ${}^{264}$Bh | 264 | 157 | -172.5497 | 1931.1600 | -1089350.3075 ppm | 248134.1116 | +8550.6108 ppm | 0.7194 ppm |
| ${}^{265}$Bh | 265 | 158 | -165.8218 | 1938.7400 | -1085530.7226 ppm | 249066.9491 | +8522.0152 ppm | 0.9694 ppm |
| ${}^{266}$Bh | 266 | 159 | -159.1016 | 1945.2580 | -1081789.4450 ppm | 249999.7942 | +8488.4890 ppm | 0.6576 ppm |
| ${}^{267}$Bh | 267 | 160 | -152.3889 | 1952.5710 | -1078045.2496 ppm | 250932.6470 | +8459.4955 ppm | 1.0557 ppm |
| ${}^{268}$Bh | 268 | 161 | -145.6837 | 1958.8120 | -1074373.5103 ppm | 251865.5072 | +8425.5735 ppm | 1.5291 ppm |
| ${}^{269}$Bh | 269 | 162 | -138.9860 | 1966.1210 | -1070690.4654 ppm | 252798.3750 | +8396.6473 ppm | 1.4937 ppm |
| ${}^{270}$Bh | 270 | 163 | -132.2957 | 1971.2700 | -1067111.9022 ppm | 253731.2500 | +8360.0213 ppm | 1.1846 ppm |
| ${}^{271}$Bh | 271 | 164 | -125.6127 | 1977.7580 | -1063512.6616 ppm | 254664.1325 | +8328.1802 ppm | 1.5195 ppm |
| ${}^{272}$Bh | 272 | 165 | -118.9369 | 1982.8800 | -1059981.9110 ppm | 255597.0221 | +8291.4336 ppm | 2.0982 ppm |
| ${}^{273}$Bh | 273 | 166 | -112.2684 | 1989.0780 | -1056442.4271 ppm | 256529.9190 | +8259.0790 ppm | 2.5738 ppm |
| ${}^{274}$Bh | 274 | 167 | -105.6070 | 1994.1720 | -1052957.8134 ppm | 257462.8230 | +8222.3181 ppm | 2.2616 ppm |
| ${}^{275}$Bh | 275 | 168 | -98.9527 | 2000.0750 | -1049474.4787 ppm | 258395.7341 | +8190.0227 ppm | 2.3406 ppm |
| ${}^{276}$Bh | 276 | 169 | -92.3054 | 2005.1400 | -1046034.3761 ppm | 259328.6523 | +8153.4767 ppm | 2.3321 ppm |
| ${}^{277}$Bh | 277 | 170 | -85.6650 | 2011.0200 | -1042597.8027 ppm | 260261.5774 | +8121.2053 ppm | 2.3236 ppm |
| ${}^{278}$Bh | 278 | 171 | -79.0316 | 2015.7780 | -1039206.5014 ppm | 261194.5094 | +8084.8332 ppm | 1.5423 ppm |

### Hassium (Z = 108)

_18 of 18 isotopes with a framework prediction; 18 of 18 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{263}$Hs | 263 | 155 | -205.6512 | 1918.5850 | -1107189.0014 ppm | 247226.8653 | +8666.7312 ppm | 0.8057 ppm |
| ${}^{264}$Hs | 264 | 156 | -198.8862 | 1926.7713 | -1103222.5059 ppm | 248159.6657 | +8639.6964 ppm | 0.1174 ppm |
| ${}^{265}$Hs | 265 | 157 | -192.1290 | 1933.5056 | -1099368.2041 ppm | 249092.4739 | +8606.9700 ppm | 0.0970 ppm |
| ${}^{266}$Hs | 266 | 158 | -185.3796 | 1941.3375 | -1095490.6510 ppm | 250025.2899 | +8578.9871 ppm | 0.1093 ppm |
| ${}^{267}$Hs | 267 | 159 | -178.6379 | 1947.7650 | -1091714.2993 ppm | 250958.1137 | +8546.0642 ppm | 0.3818 ppm |
| ${}^{268}$Hs | 268 | 160 | -171.9039 | 1955.5960 | -1087903.5772 ppm | 251890.9451 | +8518.2934 ppm | 1.2009 ppm |
| ${}^{269}$Hs | 269 | 161 | -165.1775 | 1962.0860 | -1084184.6163 ppm | 252823.7841 | +8485.8692 ppm | 0.5239 ppm |
| ${}^{270}$Hs | 270 | 162 | -158.4586 | 1969.6500 | -1080450.1088 ppm | 253756.6306 | +8457.3514 ppm | 0.9847 ppm |
| ${}^{271}$Hs | 271 | 163 | -151.7471 | 1975.0480 | -1076832.1170 ppm | 254689.4846 | +8421.2447 ppm | 1.0917 ppm |
| ${}^{272}$Hs | 272 | 164 | -145.0431 | 1981.7920 | -1073187.8425 ppm | 255622.3460 | +8390.4689 ppm | 2.0100 ppm |
| ${}^{273}$Hs | 273 | 165 | -138.3464 | 1987.1670 | -1069619.9059 ppm | 256555.2147 | +8354.2032 ppm | 1.4681 ppm |
| ${}^{274}$Hs | 274 | 166 | -131.6570 | 1993.6240 | -1066039.0093 ppm | 257488.0907 | +8322.6709 ppm | 1.8385 ppm |
| ${}^{275}$Hs | 275 | 167 | -124.9747 | 1998.7000 | -1062528.0145 ppm | 258420.9739 | +8285.7016 ppm | 2.3151 ppm |
| ${}^{276}$Hs | 276 | 168 | -118.2997 | 2005.1400 | -1058998.2175 ppm | 259353.8643 | +8254.4872 ppm | 2.7992 ppm |
| ${}^{277}$Hs | 277 | 169 | -111.6317 | 2009.9120 | -1055540.6027 ppm | 260286.7617 | +8217.6836 ppm | 1.7319 ppm |
| ${}^{278}$Hs | 278 | 170 | -104.9708 | 2016.0560 | -1052067.4019 ppm | 261219.6662 | +8186.4029 ppm | 1.1576 ppm |
| ${}^{279}$Hs | 279 | 171 | -98.3169 | 2020.7970 | -1048652.5119 ppm | 262152.5777 | +8149.8120 ppm | 2.3069 ppm |
| ${}^{280}$Hs | 280 | 172 | -91.6698 | 2026.9200 | -1045226.1673 ppm | 263085.4961 | +8118.7633 ppm | 2.2987 ppm |

### Meitnerium (Z = 109)

_18 of 18 isotopes with a framework prediction; 18 of 18 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{265}$Mt | 265 | 156 | -218.6580 | 1927.0800 | -1113465.9711 ppm | 249118.2206 | +8687.8420 ppm | 1.7764 ppm |
| ${}^{266}$Mt | 266 | 157 | -211.8792 | 1934.0221 | -1109553.6577 ppm | 250051.0072 | +8656.1466 ppm | 0.3892 ppm |
| ${}^{267}$Mt | 267 | 158 | -205.1083 | 1941.8910 | -1105622.9499 ppm | 250983.8017 | +8628.4905 ppm | 2.0214 ppm |
| ${}^{268}$Mt | 268 | 159 | -198.3451 | 1948.6280 | -1101787.0604 ppm | 251916.6040 | +8596.0569 ppm | 0.9324 ppm |
| ${}^{269}$Mt | 269 | 160 | -191.5897 | 1956.7060 | -1097914.4079 ppm | 252849.4140 | +8568.7671 ppm | 1.2447 ppm |
| ${}^{270}$Mt | 270 | 161 | -184.8420 | 1963.1700 | -1094154.8467 ppm | 253782.2317 | +8536.6586 ppm | 0.7589 ppm |
| ${}^{271}$Mt | 271 | 162 | -178.1018 | 1970.9830 | -1090361.9330 ppm | 254715.0570 | +8508.8865 ppm | 1.3056 ppm |
| ${}^{272}$Mt | 272 | 163 | -171.3692 | 1976.6240 | -1086697.9432 ppm | 255647.8898 | +8473.4255 ppm | 1.9144 ppm |
| ${}^{273}$Mt | 273 | 164 | -164.6441 | 1983.3450 | -1083013.3493 ppm | 256580.7301 | +8442.5369 ppm | 1.6658 ppm |
| ${}^{274}$Mt | 274 | 165 | -157.9264 | 1988.9660 | -1079401.2562 ppm | 257513.5778 | +8407.3013 ppm | 1.4737 ppm |
| ${}^{275}$Mt | 275 | 166 | -151.2160 | 1995.6750 | -1075771.8748 ppm | 258446.4328 | +8376.0857 ppm | 1.5119 ppm |
| ${}^{276}$Mt | 276 | 167 | -144.5130 | 2001.0000 | -1072220.3707 ppm | 259379.2952 | +8341.0937 ppm | 2.0677 ppm |
| ${}^{277}$Mt | 277 | 168 | -137.8171 | 2007.4190 | -1068653.8860 ppm | 260312.1648 | +8309.7044 ppm | 2.5654 ppm |
| ${}^{278}$Mt | 278 | 169 | -131.1284 | 2012.7200 | -1065149.8650 ppm | 261245.0415 | +8274.4293 ppm | 2.2326 ppm |
| ${}^{279}$Mt | 279 | 170 | -124.4469 | 2019.1230 | -1061634.1185 ppm | 262177.9254 | +8243.0829 ppm | 2.5792 ppm |
| ${}^{280}$Mt | 280 | 171 | -117.7723 | 2024.1200 | -1058184.4686 ppm | 263110.8163 | +8207.7124 ppm | 2.2987 ppm |
| ${}^{281}$Mt | 281 | 172 | -111.1048 | 2030.2250 | -1054725.3725 ppm | 264043.7142 | +8176.6048 ppm | 2.2905 ppm |
| ${}^{282}$Mt | 282 | 173 | -104.4442 | 2035.4760 | -1051311.9425 ppm | 264976.6190 | +8141.2748 ppm | 1.7011 ppm |

### Sodium (Z = 11)

_0 of 23 isotopes with a framework prediction; 0 of 23 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{17}$Na | 17 | 6 | — | 93.8870 | — | — | — | 3.7565 ppm |
| ${}^{18}$Na | 18 | 7 | — | 111.6399 | — | — | — | 5.5908 ppm |
| ${}^{19}$Na | 19 | 8 | — | 131.8198 | — | — | — | 0.5948 ppm |
| ${}^{20}$Na | 20 | 9 | — | 145.9701 | — | — | — | 0.0595 ppm |
| ${}^{21}$Na | 21 | 10 | — | 163.0767 | — | — | — | 0.0021 ppm |
| ${}^{22}$Na | 22 | 11 | — | 174.1446 | — | — | — | 0.0064 ppm |
| ${}^{23}$Na | 23 | 12 | — | 186.5644 | — | — | — | 0.0001 ppm |
| ${}^{24}$Na | 24 | 13 | — | 193.5237 | — | — | — | 0.0007 ppm |
| ${}^{25}$Na | 25 | 14 | — | 202.5349 | — | — | — | 0.0515 ppm |
| ${}^{26}$Na | 26 | 15 | — | 208.1092 | — | — | — | 0.1446 ppm |
| ${}^{27}$Na | 27 | 16 | — | 214.8376 | — | — | — | 0.1482 ppm |
| ${}^{28}$Na | 28 | 17 | — | 218.3794 | — | — | — | 0.3929 ppm |
| ${}^{29}$Na | 29 | 18 | — | 222.7824 | — | — | — | 0.2716 ppm |
| ${}^{30}$Na | 30 | 19 | — | 225.0591 | — | — | — | 0.1691 ppm |
| ${}^{31}$Na | 31 | 20 | — | 229.3590 | — | — | — | 0.4837 ppm |
| ${}^{32}$Na | 32 | 21 | — | 231.0362 | — | — | — | 1.2492 ppm |
| ${}^{33}$Na | 33 | 22 | — | 233.9676 | — | — | — | 14.6250 ppm |
| ${}^{34}$Na | 34 | 23 | — | 234.1389 | — | — | — | 18.9076 ppm |
| ${}^{35}$Na | 35 | 24 | — | 236.0750 | — | — | — | 20.5476 ppm |
| ${}^{36}$Na | 36 | 25 | — | 236.0520 | — | — | — | 20.4442 ppm |
| ${}^{37}$Na | 37 | 26 | — | 236.9110 | — | — | — | 19.8883 ppm |
| ${}^{38}$Na | 38 | 27 | — | 236.2080 | — | — | — | 20.1752 ppm |
| ${}^{39}$Na | 39 | 28 | — | 236.1840 | — | — | — | 20.3966 ppm |

### Darmstadtium (Z = 110)

_18 of 18 isotopes with a framework prediction; 18 of 18 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{267}$Ds | 267 | 157 | -231.8000 | 1935.2160 | -1119779.8859 ppm | 251009.7110 | +8707.9288 ppm | 0.8198 ppm |
| ${}^{268}$Ds | 268 | 158 | -225.0074 | 1943.5360 | -1115772.1905 ppm | 251942.4839 | +8681.5104 ppm | 1.2083 ppm |
| ${}^{269}$Ds | 269 | 159 | -218.2228 | 1950.2917 | -1111892.3712 ppm | 252875.2647 | +8649.6121 ppm | 0.1253 ppm |
| ${}^{270}$Ds | 270 | 160 | -211.4459 | 1958.5161 | -1107962.3080 ppm | 253808.0533 | +8623.3515 ppm | 0.1561 ppm |
| ${}^{271}$Ds | 271 | 161 | -204.6768 | 1965.2920 | -1104145.7549 ppm | 254740.8496 | +8591.6287 ppm | 0.3836 ppm |
| ${}^{272}$Ds | 272 | 162 | -197.9154 | 1973.3600 | -1100293.6086 ppm | 255673.6536 | +8564.7071 ppm | 1.6756 ppm |
| ${}^{273}$Ds | 273 | 163 | -191.1616 | 1979.2500 | -1096582.8394 ppm | 256606.4652 | +8529.8010 ppm | 0.5565 ppm |
| ${}^{274}$Ds | 274 | 164 | -184.4153 | 1986.2260 | -1092847.0998 ppm | 257539.2844 | +8500.2746 ppm | 1.5247 ppm |
| ${}^{275}$Ds | 275 | 165 | -177.6765 | 1991.8250 | -1089202.8911 ppm | 258472.1110 | +8464.8641 ppm | 1.3302 ppm |
| ${}^{276}$Ds | 276 | 166 | -170.9452 | 1999.0680 | -1085512.4472 ppm | 259404.9451 | +8435.9987 ppm | 2.1293 ppm |
| ${}^{277}$Ds | 277 | 167 | -164.2212 | 2004.6490 | -1081920.1800 ppm | 260337.7865 | +8400.8066 ppm | 1.5190 ppm |
| ${}^{278}$Ds | 278 | 168 | -157.5045 | 2011.6080 | -1078297.8185 ppm | 261270.6353 | +8371.3232 ppm | 1.9701 ppm |
| ${}^{279}$Ds | 279 | 169 | -150.7951 | 2016.8910 | -1074766.0977 ppm | 262203.4912 | +8335.8195 ppm | 2.3248 ppm |
| ${}^{280}$Ds | 280 | 170 | -144.0928 | 2023.5600 | -1071207.5759 ppm | 263136.3544 | +8306.3055 ppm | 2.8662 ppm |
| ${}^{281}$Ds | 281 | 171 | -137.3977 | 2028.8200 | -1067722.9411 ppm | 264069.2247 | +8270.6493 ppm | 1.8815 ppm |
| ${}^{282}$Ds | 282 | 172 | -130.7096 | 2035.1940 | -1064224.6274 ppm | 265002.1020 | +8240.7799 ppm | 1.1412 ppm |
| ${}^{283}$Ds | 283 | 173 | -124.0285 | 2040.4300 | -1060785.4727 ppm | 265934.9864 | +8205.3305 ppm | 1.8964 ppm |
| ${}^{284}$Ds | 284 | 174 | -117.3544 | 2046.7880 | -1057335.8733 ppm | 266867.8777 | +8175.5254 ppm | 1.8897 ppm |

### Roentgenium (Z = 111)

_15 of 15 isotopes with a framework prediction; 15 of 15 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{272}$Rg | 272 | 161 | -224.6816 | 1965.7440 | -1114298.4849 ppm | 255699.6374 | +8640.5882 ppm | 0.9223 ppm |
| ${}^{273}$Rg | 273 | 162 | -217.8988 | 1973.7900 | -1110396.1418 ppm | 256632.4201 | +8613.5766 ppm | 1.5705 ppm |
| ${}^{274}$Rg | 274 | 163 | -211.1237 | 1980.1980 | -1106617.4839 ppm | 257565.2104 | +8580.4130 ppm | 0.8207 ppm |
| ${}^{275}$Rg | 275 | 164 | -204.3563 | 1987.4250 | -1102824.6498 ppm | 258498.0084 | +8551.2337 ppm | 1.7408 ppm |
| ${}^{276}$Rg | 276 | 165 | -197.5964 | 1993.5480 | -1099117.9500 ppm | 259430.8140 | +8517.5587 ppm | 2.4443 ppm |
| ${}^{277}$Rg | 277 | 166 | -190.8440 | 2000.4940 | -1095398.4363 ppm | 260363.6270 | +8487.9477 ppm | 1.8184 ppm |
| ${}^{278}$Rg | 278 | 167 | -184.0990 | 2006.6040 | -1091746.5743 ppm | 261296.4475 | +8454.3295 ppm | 1.4991 ppm |
| ${}^{279}$Rg | 279 | 168 | -177.3615 | 2013.2640 | -1088096.4743 ppm | 262229.2753 | +8424.5139 ppm | 1.6227 ppm |
| ${}^{280}$Rg | 280 | 169 | -170.6312 | 2019.3600 | -1084497.6580 ppm | 263162.1104 | +8391.2177 ppm | 2.0381 ppm |
| ${}^{281}$Rg | 281 | 170 | -163.9082 | 2025.7290 | -1080913.1794 ppm | 264094.9529 | +8360.9518 ppm | 2.9555 ppm |
| ${}^{282}$Rg | 282 | 171 | -157.1924 | 2031.5280 | -1077376.4140 ppm | 265027.8025 | +8327.2366 ppm | 2.2362 ppm |
| ${}^{283}$Rg | 283 | 172 | -150.4837 | 2037.8830 | -1073843.1325 ppm | 265960.6592 | +8296.7355 ppm | 2.5709 ppm |
| ${}^{284}$Rg | 284 | 173 | -143.7821 | 2043.3800 | -1070364.8145 ppm | 266893.5230 | +8262.8465 ppm | 1.8897 ppm |
| ${}^{285}$Rg | 285 | 174 | -137.0875 | 2049.7200 | -1066881.0694 ppm | 267826.3938 | +8232.3759 ppm | 2.2583 ppm |
| ${}^{286}$Rg | 286 | 175 | -130.3998 | 2054.9100 | -1063457.6891 ppm | 268759.2716 | +8198.2836 ppm | 1.7192 ppm |

### Copernicium (Z = 112)

_13 of 13 isotopes with a framework prediction; 13 of 13 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{276}$Cn | 276 | 164 | -224.4665 | 1989.6840 | -1112815.1727 ppm | 259456.9018 | +8607.3150 ppm | 1.9445 ppm |
| ${}^{277}$Cn | 277 | 165 | -217.6855 | 1995.7850 | -1109072.6167 ppm | 260389.6861 | +8573.5538 ppm | 0.5953 ppm |
| ${}^{278}$Cn | 278 | 166 | -210.9120 | 2003.2680 | -1105283.9716 ppm | 261322.4781 | +8545.7538 ppm | 1.6897 ppm |
| ${}^{279}$Cn | 279 | 167 | -204.1460 | 2009.3580 | -1101597.6436 ppm | 262255.2775 | +8511.7117 ppm | 1.5188 ppm |
| ${}^{280}$Cn | 280 | 168 | -197.3875 | 2016.5600 | -1097883.2820 ppm | 263188.0844 | +8483.9135 ppm | 2.2344 ppm |
| ${}^{281}$Cn | 281 | 169 | -190.6364 | 2022.3570 | -1094264.4496 ppm | 264120.8987 | +8449.9535 ppm | 1.5187 ppm |
| ${}^{282}$Cn | 282 | 170 | -183.8926 | 2029.5540 | -1090607.3713 ppm | 265053.7203 | +8421.6840 ppm | 2.0838 ppm |
| ${}^{283}$Cn | 283 | 171 | -177.1560 | 2035.3360 | -1087040.1750 ppm | 265986.5492 | +8387.4066 ppm | 2.3307 ppm |
| ${}^{284}$Cn | 284 | 172 | -170.4267 | 2042.2440 | -1083450.6830 ppm | 266919.3853 | +8358.8521 ppm | 2.8820 ppm |
| ${}^{285}$Cn | 285 | 173 | -163.7045 | 2047.7250 | -1079944.5532 ppm | 267852.2285 | +8324.4824 ppm | 1.9076 ppm |
| ${}^{286}$Cn | 286 | 174 | -156.9894 | 2054.3380 | -1076418.4638 ppm | 268785.0788 | +8295.3233 ppm | 2.6242 ppm |
| ${}^{287}$Cn | 287 | 175 | -150.2813 | 2059.5120 | -1072969.3646 ppm | 269717.9362 | +8260.5271 ppm | 2.6151 ppm |
| ${}^{288}$Cn | 288 | 176 | -143.5802 | 2066.1120 | -1069492.9351 ppm | 270650.8005 | +8231.1071 ppm | 2.6060 ppm |

### Nihonium (Z = 113)

_13 of 13 isotopes with a framework prediction; 13 of 13 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{278}$Nh | 278 | 165 | -237.9434 | 1996.3180 | -1119191.1423 ppm | 261348.7272 | +8622.9754 ppm | 0.8628 ppm |
| ${}^{279}$Nh | 279 | 166 | -231.1488 | 2004.0570 | -1115340.4334 ppm | 262281.4980 | +8595.3279 ppm | 2.3068 ppm |
| ${}^{280}$Nh | 280 | 167 | -224.3618 | 2010.4000 | -1111600.5591 ppm | 263214.2764 | +8562.6909 ppm | 1.5312 ppm |
| ${}^{281}$Nh | 281 | 168 | -217.5822 | 2017.8610 | -1107828.1624 ppm | 264147.0623 | +8534.9745 ppm | 1.1452 ppm |
| ${}^{282}$Nh | 282 | 169 | -210.8102 | 2023.9140 | -1104159.6532 ppm | 265079.8556 | +8502.3078 ppm | 1.5239 ppm |
| ${}^{283}$Nh | 283 | 170 | -204.0455 | 2031.0910 | -1100461.0397 ppm | 266012.6564 | +8474.0456 ppm | 1.6562 ppm |
| ${}^{284}$Nh | 284 | 171 | -197.2882 | 2037.1320 | -1096846.0480 ppm | 266945.4645 | +8441.4645 ppm | 2.0163 ppm |
| ${}^{285}$Nh | 285 | 172 | -190.5381 | 2044.0200 | -1093217.3513 ppm | 267878.2798 | +8412.3717 ppm | 2.9175 ppm |
| ${}^{286}$Nh | 286 | 173 | -183.7953 | 2050.0480 | -1089654.1428 ppm | 268811.1024 | +8379.6794 ppm | 2.2154 ppm |
| ${}^{287}$Nh | 287 | 174 | -177.0596 | 2056.6420 | -1086091.6108 ppm | 269743.9322 | +8349.8474 ppm | 2.6429 ppm |
| ${}^{288}$Nh | 288 | 175 | -170.3311 | 2062.0800 | -1082601.5734 ppm | 270676.7690 | +8316.4285 ppm | 2.6059 ppm |
| ${}^{289}$Nh | 289 | 176 | -163.6095 | 2068.6620 | -1079089.5415 ppm | 271609.6129 | +8286.7645 ppm | 1.8569 ppm |
| ${}^{290}$Nh | 290 | 177 | -156.8950 | 2074.0800 | -1075645.5858 ppm | 272542.4638 | +8252.9152 ppm | 1.7333 ppm |

### Flerovium (Z = 114)

_8 of 8 isotopes with a framework prediction; 8 of 8 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{284}$Fl | 284 | 170 | -224.3666 | 2034.2920 | -1110292.2466 ppm | 266971.7606 | +8532.4670 ppm | 2.4773 ppm |
| ${}^{285}$Fl | 285 | 171 | -217.5885 | 2040.3150 | -1106644.5508 ppm | 267904.5478 | +8499.2431 ppm | 1.5183 ppm |
| ${}^{286}$Fl | 286 | 172 | -210.8177 | 2047.4740 | -1102964.7586 ppm | 268837.3425 | +8471.8753 ppm | 2.0616 ppm |
| ${}^{287}$Fl | 287 | 173 | -204.0541 | 2053.4850 | -1099369.6785 ppm | 269770.1444 | +8438.5067 ppm | 2.3086 ppm |
| ${}^{288}$Fl | 288 | 174 | -197.2979 | 2060.3520 | -1095759.2941 ppm | 270702.9535 | +8410.4114 ppm | 2.8419 ppm |
| ${}^{289}$Fl | 289 | 175 | -190.5487 | 2066.0610 | -1092228.0295 ppm | 271635.7698 | +8376.6966 ppm | 1.8949 ppm |
| ${}^{290}$Fl | 290 | 176 | -183.8067 | 2072.6300 | -1088682.8485 ppm | 272568.5932 | +8348.0294 ppm | 2.5914 ppm |
| ${}^{291}$Fl | 291 | 177 | -177.0718 | 2078.0310 | -1085211.3320 ppm | 273501.4237 | +8313.9932 ppm | 2.5790 ppm |

### Moscovium (Z = 115)

_6 of 6 isotopes with a framework prediction; 6 of 6 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{287}$Mc | 287 | 172 | -231.2648 | 2048.8930 | -1112873.0721 ppm | 269796.5727 | +8522.9015 ppm | 1.6540 ppm |
| ${}^{288}$Mc | 288 | 173 | -224.4806 | 2054.8800 | -1109242.6757 ppm | 270729.3539 | +8490.9169 ppm | 1.9952 ppm |
| ${}^{289}$Mc | 289 | 174 | -217.7036 | 2062.0150 | -1105578.1028 ppm | 271662.1424 | +8462.5531 ppm | 2.8839 ppm |
| ${}^{290}$Mc | 290 | 175 | -210.9339 | 2067.9900 | -1101999.4854 ppm | 272594.9381 | +8430.3391 ppm | 2.1882 ppm |
| ${}^{291}$Mc | 291 | 176 | -204.1714 | 2074.5390 | -1098417.7135 ppm | 273527.7410 | +8401.0537 ppm | 2.7095 ppm |
| ${}^{292}$Mc | 292 | 177 | -197.4160 | 2080.2080 | -1094902.0396 ppm | 274460.5510 | +8368.1715 ppm | 2.5702 ppm |

### Livermorium (Z = 116)

_5 of 5 isotopes with a framework prediction; 5 of 5 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{289}$Lv | 289 | 173 | -245.0742 | 2057.3910 | -1119118.9324 ppm | 271688.7306 | +8547.1228 ppm | 1.8672 ppm |
| ${}^{290}$Lv | 290 | 174 | -238.2765 | 2064.8000 | -1115399.3351 ppm | 272621.4984 | +8520.2548 ppm | 2.0434 ppm |
| ${}^{291}$Lv | 291 | 175 | -231.4862 | 2070.7560 | -1111788.2482 ppm | 273554.2734 | +8487.4790 ppm | 2.2974 ppm |
| ${}^{292}$Lv | 292 | 176 | -224.7031 | 2077.8720 | -1108140.9623 ppm | 274487.0557 | +8459.8692 ppm | 2.8029 ppm |
| ${}^{293}$Lv | 293 | 177 | -217.9272 | 2083.5230 | -1104595.5172 ppm | 275419.8452 | +8426.7684 ppm | 1.8861 ppm |

### Tennessine (Z = 117)

_4 of 4 isotopes with a framework prediction; 4 of 4 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{291}$Ts | 291 | 174 | -259.0162 | 2065.5180 | -1125400.1136 ppm | 273581.0211 | +8569.6910 ppm | 2.1978 ppm |
| ${}^{292}$Ts | 292 | 175 | -252.2051 | 2071.7400 | -1121735.9019 ppm | 274513.7755 | +8537.7006 ppm | 2.4572 ppm |
| ${}^{293}$Ts | 293 | 176 | -245.4014 | 2078.8350 | -1118047.5626 ppm | 275446.5372 | +8510.2448 ppm | 2.8478 ppm |
| ${}^{294}$Ts | 294 | 177 | -238.6049 | 2085.0480 | -1114436.1839 ppm | 276379.3061 | +8478.7279 ppm | 2.1651 ppm |

### Oganesson (Z = 118)

_3 of 3 isotopes with a framework prediction; 3 of 3 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{293}$Og | 293 | 175 | -273.0904 | 2073.8540 | -1131682.5427 ppm | 275473.4438 | +8592.6063 ppm | 2.5954 ppm |
| ${}^{294}$Og | 294 | 176 | -266.2660 | 2081.2260 | -1127937.0736 ppm | 276406.1848 | +8566.0448 ppm | 2.0189 ppm |
| ${}^{295}$Og | 295 | 177 | -259.4489 | 2087.4200 | -1124291.6576 ppm | 277338.9331 | +8534.0771 ppm | 2.3813 ppm |

### Magnesium (Z = 12)

_2 of 23 isotopes with a framework prediction; 2 of 23 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{19}$Mg | 19 | 7 | — | 112.1285 | — | — | — | 3.3841 ppm |
| ${}^{20}$Mg | 20 | 8 | — | 134.5605 | — | — | — | 0.0999 ppm |
| ${}^{21}$Mg | 21 | 9 | — | 149.2057 | — | — | — | 0.0385 ppm |
| ${}^{22}$Mg | 22 | 10 | — | 168.5808 | — | — | — | 0.0077 ppm |
| ${}^{23}$Mg | 23 | 11 | — | 181.7258 | — | — | — | 0.0015 ppm |
| ${}^{24}$Mg | 24 | 12 | 216.1389 | 198.2570 | +90195.3264 ppm | 22324.0432 | -800.3645 ppm | 0.0005 ppm |
| ${}^{25}$Mg | 25 | 13 | — | 205.5876 | — | — | — | 0.0020 ppm |
| ${}^{26}$Mg | 26 | 14 | — | 216.6806 | — | — | — | 0.0012 ppm |
| ${}^{27}$Mg | 27 | 15 | — | 223.1240 | — | — | — | 0.0019 ppm |
| ${}^{28}$Mg | 28 | 16 | — | 231.6287 | — | — | — | 0.0100 ppm |
| ${}^{29}$Mg | 29 | 17 | — | 235.2924 | — | — | — | 0.0127 ppm |
| ${}^{30}$Mg | 30 | 18 | — | 241.6327 | — | — | — | 0.0463 ppm |
| ${}^{31}$Mg | 31 | 19 | — | 243.9448 | — | — | — | 0.1065 ppm |
| ${}^{32}$Mg | 32 | 20 | — | 249.7229 | — | — | — | 0.1094 ppm |
| ${}^{33}$Mg | 33 | 21 | — | 252.0025 | — | — | — | 0.0866 ppm |
| ${}^{34}$Mg | 34 | 22 | — | 256.7133 | — | — | — | 0.2176 ppm |
| ${}^{35}$Mg | 35 | 23 | — | 257.4682 | — | — | — | 8.2675 ppm |
| ${}^{36}$Mg | 36 | 24 | — | 260.7991 | — | — | — | 20.5708 ppm |
| ${}^{37}$Mg | 37 | 25 | — | 261.0391 | — | — | — | 20.2631 ppm |
| ${}^{38}$Mg | 38 | 26 | — | 263.2640 | — | — | — | 14.1969 ppm |
| ${}^{39}$Mg | 39 | 27 | — | 262.6260 | — | — | — | 14.1116 ppm |
| ${}^{40}$Mg | 40 | 28 | — | 263.9200 | — | — | — | 13.4072 ppm |
| ${}^{41}$Mg | 41 | 29 | 150.3903 | 263.4250 | -429096.3464 ppm | 38362.4040 | +2955.4925 ppm | 13.0777 ppm |

### Aluminium (Z = 13)

_3 of 23 isotopes with a framework prediction; 3 of 23 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{21}$Al | 21 | 8 | — | 132.2370 | — | — | — | 30.6243 ppm |
| ${}^{22}$Al | 22 | 9 | — | 149.2040 | — | — | — | 19.5281 ppm |
| ${}^{23}$Al | 23 | 10 | — | 168.7217 | — | — | — | 0.0161 ppm |
| ${}^{24}$Al | 24 | 11 | — | 183.5899 | — | — | — | 0.0102 ppm |
| ${}^{25}$Al | 25 | 12 | — | 200.5284 | — | — | — | 0.0028 ppm |
| ${}^{26}$Al | 26 | 13 | — | 211.8939 | — | — | — | 0.0027 ppm |
| ${}^{27}$Al | 27 | 14 | — | 224.9519 | — | — | — | 0.0019 ppm |
| ${}^{28}$Al | 28 | 15 | — | 232.6771 | — | — | — | 0.0019 ppm |
| ${}^{29}$Al | 29 | 16 | — | 242.1055 | — | — | — | 0.0128 ppm |
| ${}^{30}$Al | 30 | 17 | — | 247.8331 | — | — | — | 0.0693 ppm |
| ${}^{31}$Al | 31 | 18 | — | 254.9911 | — | — | — | 0.0775 ppm |
| ${}^{32}$Al | 32 | 19 | — | 259.2110 | — | — | — | 0.2407 ppm |
| ${}^{33}$Al | 33 | 20 | — | 264.6804 | — | — | — | 0.2273 ppm |
| ${}^{34}$Al | 34 | 21 | — | 267.2519 | — | — | — | 0.0664 ppm |
| ${}^{35}$Al | 35 | 22 | — | 272.5494 | — | — | — | 0.2257 ppm |
| ${}^{36}$Al | 36 | 23 | — | 274.4466 | — | — | — | 4.4575 ppm |
| ${}^{37}$Al | 37 | 24 | — | 278.6587 | — | — | — | 5.2282 ppm |
| ${}^{38}$Al | 38 | 25 | — | 280.0600 | — | — | — | 4.2349 ppm |
| ${}^{39}$Al | 39 | 26 | — | 283.1400 | — | — | — | 8.2515 ppm |
| ${}^{40}$Al | 40 | 27 | — | 283.8800 | — | — | — | 8.0438 ppm |
| ${}^{41}$Al | 41 | 28 | 143.0450 | 286.1800 | -500157.1436 ppm | 38368.9670 | +3744.0269 ppm | 10.4539 ppm |
| ${}^{42}$Al | 42 | 29 | 148.4366 | 286.8180 | -482471.1706 ppm | 39303.1408 | +3533.7543 ppm | 12.7720 ppm |
| ${}^{43}$Al | 43 | 30 | 153.8222 | 288.6160 | -467035.1572 ppm | 40237.3207 | +3361.4890 ppm | 14.9587 ppm |

### Silicon (Z = 14)

_5 of 24 isotopes with a framework prediction; 5 of 24 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{22}$Si | 22 | 8 | — | 132.9680 | — | — | — | 24.3691 ppm |
| ${}^{23}$Si | 23 | 9 | — | 150.7420 | — | — | — | 23.3218 ppm |
| ${}^{24}$Si | 24 | 10 | — | 172.0136 | — | — | — | 0.8706 ppm |
| ${}^{25}$Si | 25 | 11 | — | 187.0028 | — | — | — | 0.4293 ppm |
| ${}^{26}$Si | 26 | 12 | — | 206.0424 | — | — | — | 0.0044 ppm |
| ${}^{27}$Si | 27 | 13 | — | 219.3572 | — | — | — | 0.0043 ppm |
| ${}^{28}$Si | 28 | 14 | — | 236.5368 | — | — | — | 0.0000 ppm |
| ${}^{29}$Si | 29 | 15 | — | 245.0104 | — | — | — | 0.0000 ppm |
| ${}^{30}$Si | 30 | 16 | — | 255.6196 | — | — | — | 0.0008 ppm |
| ${}^{31}$Si | 31 | 17 | — | 262.2070 | — | — | — | 0.0015 ppm |
| ${}^{32}$Si | 32 | 18 | — | 271.4070 | — | — | — | 0.0100 ppm |
| ${}^{33}$Si | 33 | 19 | — | 275.9150 | — | — | — | 0.0227 ppm |
| ${}^{34}$Si | 34 | 20 | — | 283.4636 | — | — | — | 0.0253 ppm |
| ${}^{35}$Si | 35 | 21 | — | 285.9348 | — | — | — | 1.1003 ppm |
| ${}^{36}$Si | 36 | 22 | — | 292.0507 | — | — | — | 2.1418 ppm |
| ${}^{37}$Si | 37 | 23 | — | 294.2574 | — | — | — | 3.3028 ppm |
| ${}^{38}$Si | 38 | 24 | — | 299.9275 | — | — | — | 2.9609 ppm |
| ${}^{39}$Si | 39 | 25 | — | 301.5082 | — | — | — | 3.7305 ppm |
| ${}^{40}$Si | 40 | 26 | — | 306.2330 | — | — | — | 3.2736 ppm |
| ${}^{41}$Si | 41 | 27 | 135.2970 | 306.7620 | -558951.2115 ppm | 38375.9326 | +4488.3292 ppm | 7.8509 ppm |
| ${}^{42}$Si | 42 | 28 | 140.7259 | 311.2200 | -547824.9913 ppm | 39310.0692 | +4355.6219 ppm | 7.6634 ppm |
| ${}^{43}$Si | 43 | 29 | 146.1478 | 311.7930 | -531266.6675 ppm | 40244.2127 | +4132.7958 ppm | 9.9707 ppm |
| ${}^{44}$Si | 44 | 30 | 151.5629 | 314.8640 | -518639.9681 ppm | 41178.3630 | +3981.7583 ppm | 12.1958 ppm |
| ${}^{45}$Si | 45 | 31 | 156.9717 | 315.1800 | -501961.6026 ppm | 42112.5196 | +3770.6411 ppm | 14.2985 ppm |

### Phosphorus (Z = 15)

_7 of 24 isotopes with a framework prediction; 7 of 24 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{24}$P | 24 | 9 | — | 147.9600 | — | — | — | 22.3410 ppm |
| ${}^{25}$P | 25 | 10 | — | 169.8500 | — | — | — | 17.1451 ppm |
| ${}^{26}$P | 26 | 11 | — | 187.1480 | — | — | — | 8.0733 ppm |
| ${}^{27}$P | 27 | 12 | — | 206.8494 | — | — | — | 0.3579 ppm |
| ${}^{28}$P | 28 | 13 | — | 221.4096 | — | — | — | 0.0440 ppm |
| ${}^{29}$P | 29 | 14 | — | 239.2859 | — | — | — | 0.0133 ppm |
| ${}^{30}$P | 30 | 15 | — | 250.6052 | — | — | — | 0.0023 ppm |
| ${}^{31}$P | 31 | 16 | — | 262.9162 | — | — | — | 0.0000 ppm |
| ${}^{32}$P | 32 | 17 | — | 270.8518 | — | — | — | 0.0013 ppm |
| ${}^{33}$P | 33 | 18 | — | 280.9556 | — | — | — | 0.0355 ppm |
| ${}^{34}$P | 34 | 19 | — | 287.2383 | — | — | — | 0.0256 ppm |
| ${}^{35}$P | 35 | 20 | — | 295.6187 | — | — | — | 0.0573 ppm |
| ${}^{36}$P | 36 | 21 | — | 299.0833 | — | — | — | 0.3913 ppm |
| ${}^{37}$P | 37 | 22 | — | 305.8996 | — | — | — | 1.1016 ppm |
| ${}^{38}$P | 38 | 23 | — | 309.5964 | — | — | — | 2.0513 ppm |
| ${}^{39}$P | 39 | 24 | — | 315.8208 | — | — | — | 3.1018 ppm |
| ${}^{40}$P | 40 | 25 | — | 319.2567 | — | — | — | 2.2444 ppm |
| ${}^{41}$P | 41 | 26 | 127.1462 | 324.1686 | -607777.4556 ppm | 38383.3011 | +5159.5129 ppm | 3.1468 ppm |
| ${}^{42}$P | 42 | 27 | 132.6155 | 326.1683 | -593414.0221 ppm | 39317.3973 | +4947.1897 ppm | 2.4284 ppm |
| ${}^{43}$P | 43 | 28 | 138.0765 | 330.2830 | -581944.8896 ppm | 40251.5017 | +4798.2605 ppm | 7.4874 ppm |
| ${}^{44}$P | 44 | 29 | 143.5297 | 332.2880 | -568056.2259 ppm | 41185.6139 | +4604.3381 ppm | 9.7474 ppm |
| ${}^{45}$P | 45 | 30 | 148.9755 | 335.5200 | -555986.1032 ppm | 42119.7335 | +4448.4705 ppm | 11.9288 ppm |
| ${}^{46}$P | 46 | 31 | 154.4143 | 336.7200 | -541416.3960 ppm | 43053.8602 | +4252.0290 ppm | 11.6677 ppm |
| ${}^{47}$P | 47 | 32 | 159.8462 | 338.8230 | -528230.8425 ppm | 43987.9936 | +4085.0150 ppm | 13.6931 ppm |

### Sulfur (Z = 16)

_9 of 24 isotopes with a framework prediction; 9 of 24 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{26}$S | 26 | 10 | — | 169.6500 | — | — | — | 24.7410 ppm |
| ${}^{27}$S | 27 | 11 | — | 187.9200 | — | — | — | 15.9149 ppm |
| ${}^{28}$S | 28 | 12 | — | 209.4062 | — | — | — | 6.1336 ppm |
| ${}^{29}$S | 29 | 13 | — | 224.6451 | — | — | — | 0.4828 ppm |
| ${}^{30}$S | 30 | 14 | — | 243.6812 | — | — | — | 0.0074 ppm |
| ${}^{31}$S | 31 | 15 | — | 256.7358 | — | — | — | 0.0079 ppm |
| ${}^{32}$S | 32 | 16 | — | 271.7802 | — | — | — | 0.0000 ppm |
| ${}^{33}$S | 33 | 17 | — | 280.4218 | — | — | — | 0.0000 ppm |
| ${}^{34}$S | 34 | 18 | — | 291.8390 | — | — | — | 0.0014 ppm |
| ${}^{35}$S | 35 | 19 | — | 298.8248 | — | — | — | 0.0012 ppm |
| ${}^{36}$S | 36 | 20 | — | 308.7140 | — | — | — | 0.0056 ppm |
| ${}^{37}$S | 37 | 21 | — | 313.0176 | — | — | — | 0.0057 ppm |
| ${}^{38}$S | 38 | 22 | — | 321.0538 | — | — | — | 0.2028 ppm |
| ${}^{39}$S | 39 | 23 | — | 325.4265 | — | — | — | 1.3772 ppm |
| ${}^{40}$S | 40 | 24 | — | 333.1730 | — | — | — | 0.1069 ppm |
| ${}^{41}$S | 41 | 25 | 118.5927 | 337.4151 | -648525.7542 ppm | 38391.0723 | +5732.5048 ppm | 0.1074 ppm |
| ${}^{42}$S | 42 | 26 | 124.1053 | 344.1156 | -639350.0666 ppm | 39325.1252 | +5626.1322 ppm | 0.0715 ppm |
| ${}^{43}$S | 43 | 27 | 129.6084 | 346.7446 | -626213.7657 ppm | 40259.1875 | +5422.7111 ppm | 0.1241 ppm |
| ${}^{44}$S | 44 | 28 | 135.1025 | 351.8247 | -615994.9021 ppm | 41193.2588 | +5288.9403 ppm | 0.1273 ppm |
| ${}^{45}$S | 45 | 29 | 140.5880 | 354.0150 | -602875.5020 ppm | 42127.3386 | +5092.4477 ppm | 7.1561 ppm |
| ${}^{46}$S | 46 | 30 | 146.0654 | 358.1100 | -592121.3288 ppm | 43061.4267 | +4948.9167 ppm | 9.3259 ppm |
| ${}^{47}$S | 47 | 31 | 151.5350 | 359.6440 | -578652.6444 ppm | 43995.5225 | +4752.4867 ppm | 9.1262 ppm |
| ${}^{48}$S | 48 | 32 | 156.9972 | 362.4960 | -566899.4122 ppm | 44929.6257 | +4595.2607 ppm | 11.1844 ppm |
| ${}^{49}$S | 49 | 33 | 162.4523 | 362.6000 | -551979.3018 ppm | 45863.7361 | +4382.7826 ppm | 12.7698 ppm |

### Chlorine (Z = 17)

_12 of 25 isotopes with a framework prediction; 12 of 25 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{28}$Cl | 28 | 11 | — | 184.4360 | — | — | — | 19.1578 ppm |
| ${}^{29}$Cl | 29 | 12 | — | 206.7410 | — | — | — | 6.9964 ppm |
| ${}^{30}$Cl | 30 | 13 | — | 224.1651 | — | — | — | 0.8542 ppm |
| ${}^{31}$Cl | 31 | 14 | — | 243.9455 | — | — | — | 0.1194 ppm |
| ${}^{32}$Cl | 32 | 15 | — | 258.3170 | — | — | — | 0.0189 ppm |
| ${}^{33}$Cl | 33 | 16 | — | 274.0569 | — | — | — | 0.0127 ppm |
| ${}^{34}$Cl | 34 | 17 | — | 285.5650 | — | — | — | 0.0015 ppm |
| ${}^{35}$Cl | 35 | 18 | — | 298.2098 | — | — | — | 0.0011 ppm |
| ${}^{36}$Cl | 36 | 19 | — | 306.7896 | — | — | — | 0.0011 ppm |
| ${}^{37}$Cl | 37 | 20 | — | 317.1004 | — | — | — | 0.0015 ppm |
| ${}^{38}$Cl | 38 | 21 | — | 323.2083 | — | — | — | 0.0028 ppm |
| ${}^{39}$Cl | 39 | 22 | — | 331.2817 | — | — | — | 0.0477 ppm |
| ${}^{40}$Cl | 40 | 23 | — | 337.1106 | — | — | — | 0.8612 ppm |
| ${}^{41}$Cl | 41 | 24 | 109.6364 | 344.9313 | -682149.9971 ppm | 38399.2462 | +6165.3775 ppm | 1.8007 ppm |
| ${}^{42}$Cl | 42 | 25 | 115.1953 | 350.5272 | -671365.6860 ppm | 39333.2528 | +6019.0467 ppm | 1.5248 ppm |
| ${}^{43}$Cl | 43 | 26 | 120.7433 | 357.9263 | -662658.6328 ppm | 40267.2702 | +5925.1233 ppm | 1.5453 ppm |
| ${}^{44}$Cl | 44 | 27 | 126.2812 | 362.3171 | -651462.3036 ppm | 41201.2978 | +5761.8617 ppm | 2.0887 ppm |
| ${}^{45}$Cl | 45 | 28 | 131.8092 | 368.1720 | -641990.1130 ppm | 42135.3351 | +5641.2605 ppm | 3.2498 ppm |
| ${}^{46}$Cl | 46 | 29 | 137.3279 | 371.7157 | -630556.5129 ppm | 43069.3818 | +5471.8813 ppm | 2.2703 ppm |
| ${}^{47}$Cl | 47 | 30 | 142.8378 | 375.6240 | -619731.9879 ppm | 44003.4374 | +5318.5177 ppm | 4.5755 ppm |
| ${}^{48}$Cl | 48 | 31 | 148.3392 | 378.3840 | -607966.6079 ppm | 44937.5014 | +5146.0047 ppm | 11.1886 ppm |
| ${}^{49}$Cl | 49 | 32 | 153.8324 | 381.4650 | -596732.5286 ppm | 45871.5736 | +4986.9241 ppm | 8.7550 ppm |
| ${}^{50}$Cl | 50 | 33 | 159.3179 | 382.5500 | -583536.9711 ppm | 46805.6535 | +4792.5522 ppm | 8.5786 ppm |
| ${}^{51}$Cl | 51 | 34 | 164.7960 | 384.0300 | -570877.2489 ppm | 47739.7409 | +4613.8314 ppm | 14.7211 ppm |
| ${}^{52}$Cl | 52 | 35 | 170.2670 | 384.0720 | -556679.5518 ppm | 48673.8353 | +4411.5171 ppm | 14.4356 ppm |

### Argon (Z = 18)

_14 of 26 isotopes with a framework prediction; 14 of 26 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{29}$Ar | 29 | 11 | — | 182.0040 | — | — | — | 16.2186 ppm |
| ${}^{30}$Ar | 30 | 12 | — | 205.9800 | — | — | — | 6.3949 ppm |
| ${}^{31}$Ar | 31 | 13 | — | 224.8120 | — | — | — | 6.9328 ppm |
| ${}^{32}$Ar | 32 | 14 | — | 246.4003 | — | — | — | 0.0594 ppm |
| ${}^{33}$Ar | 33 | 15 | — | 261.6555 | — | — | — | 0.0130 ppm |
| ${}^{34}$Ar | 34 | 16 | — | 278.7209 | — | — | — | 0.0024 ppm |
| ${}^{35}$Ar | 35 | 17 | — | 291.4612 | — | — | — | 0.0209 ppm |
| ${}^{36}$Ar | 36 | 18 | — | 306.7167 | — | — | — | 0.0008 ppm |
| ${}^{37}$Ar | 37 | 19 | — | 315.5042 | — | — | — | 0.0060 ppm |
| ${}^{38}$Ar | 38 | 20 | — | 327.3427 | — | — | — | 0.0055 ppm |
| ${}^{39}$Ar | 39 | 21 | — | 333.9414 | — | — | — | 0.1377 ppm |
| ${}^{40}$Ar | 40 | 22 | — | 343.8104 | — | — | — | 0.0001 ppm |
| ${}^{41}$Ar | 41 | 23 | 100.2774 | 349.9093 | -713418.9133 ppm | 38407.8229 | +6542.0340 ppm | 0.0091 ppm |
| ${}^{42}$Ar | 42 | 24 | 105.8855 | 359.3358 | -705329.8483 ppm | 39341.7802 | +6484.0460 ppm | 0.1477 ppm |
| ${}^{43}$Ar | 43 | 25 | 111.4815 | 364.9942 | -694566.5038 ppm | 40275.7497 | +6334.3047 ppm | 0.1327 ppm |
| ${}^{44}$Ar | 44 | 26 | 117.0658 | 373.7290 | -686762.8981 ppm | 41209.7308 | +6267.2592 ppm | 0.0387 ppm |
| ${}^{45}$Ar | 45 | 27 | 122.6391 | 378.8979 | -676326.8663 ppm | 42143.7229 | +6117.7989 ppm | 0.0122 ppm |
| ${}^{46}$Ar | 46 | 28 | 128.2018 | 386.9696 | -668703.2309 ppm | 43077.7256 | +6043.3074 ppm | 0.0544 ppm |
| ${}^{47}$Ar | 47 | 29 | 133.7545 | 390.6370 | -657599.0496 ppm | 44011.7384 | +5870.9548 ppm | 0.0277 ppm |
| ${}^{48}$Ar | 48 | 30 | 139.2976 | 395.6959 | -647968.2120 ppm | 44945.7607 | +5737.3535 ppm | 0.3752 ppm |
| ${}^{49}$Ar | 49 | 31 | 144.8315 | 398.4680 | -636529.2597 ppm | 45879.7922 | +5559.1249 ppm | 8.7584 ppm |
| ${}^{50}$Ar | 50 | 32 | 150.3566 | 402.7000 | -626628.7822 ppm | 46813.8325 | +5419.8746 ppm | 10.7431 ppm |
| ${}^{51}$Ar | 51 | 33 | 155.8733 | 404.0220 | -614195.9652 ppm | 47747.8812 | +5224.6983 ppm | 8.4129 ppm |
| ${}^{52}$Ar | 52 | 34 | 161.3820 | 407.0040 | -603487.9377 ppm | 48681.9380 | +5071.0737 ppm | 12.3850 ppm |
| ${}^{53}$Ar | 53 | 35 | 166.8830 | 406.8810 | -589848.2523 ppm | 49616.0024 | +4861.1563 ppm | 14.1490 ppm |
| ${}^{54}$Ar | 54 | 36 | 172.3765 | 409.2120 | -578759.9020 ppm | 50550.0743 | +4707.1592 ppm | 15.9034 ppm |

### Potassium (Z = 19)

_19 of 29 isotopes with a framework prediction; 19 of 29 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{31}$K | 31 | 12 | — | 201.0970 | — | — | — | 10.3748 ppm |
| ${}^{32}$K | 32 | 13 | — | 221.4400 | — | — | — | 13.3964 ppm |
| ${}^{33}$K | 33 | 14 | — | 243.9360 | — | — | — | 6.5136 ppm |
| ${}^{34}$K | 34 | 15 | — | 260.7800 | — | — | — | 6.1767 ppm |
| ${}^{35}$K | 35 | 16 | — | 278.8044 | — | — | — | 0.0157 ppm |
| ${}^{36}$K | 36 | 17 | — | 293.1200 | — | — | — | 0.0097 ppm |
| ${}^{37}$K | 37 | 18 | — | 308.5744 | — | — | — | 0.0027 ppm |
| ${}^{38}$K | 38 | 19 | — | 320.6463 | — | — | — | 0.0055 ppm |
| ${}^{39}$K | 39 | 20 | — | 333.7240 | — | — | — | 0.0001 ppm |
| ${}^{40}$K | 40 | 21 | — | 341.5236 | — | — | — | 0.0015 ppm |
| ${}^{41}$K | 41 | 22 | 90.5156 | 351.6190 | -742574.7751 ppm | 38416.8024 | +6843.1109 ppm | 0.0001 ppm |
| ${}^{42}$K | 42 | 23 | 96.1760 | 359.1528 | -732214.1896 ppm | 39350.7074 | +6727.8671 ppm | 0.0027 ppm |
| ${}^{43}$K | 43 | 24 | 101.8227 | 368.7775 | -723891.1515 ppm | 40284.6261 | +6670.9288 ppm | 0.0102 ppm |
| ${}^{44}$K | 44 | 25 | 107.4564 | 376.0549 | -714253.4883 ppm | 41218.5579 | +6559.1960 ppm | 0.0102 ppm |
| ${}^{45}$K | 45 | 26 | 113.0776 | 384.9604 | -706261.6945 ppm | 42152.5021 | +6491.8583 ppm | 0.0125 ppm |
| ${}^{46}$K | 46 | 27 | 118.6870 | 391.8300 | -697095.6733 ppm | 43086.4581 | +6379.8671 ppm | 0.0170 ppm |
| ${}^{47}$K | 47 | 28 | 124.2851 | 400.1993 | -689442.0449 ppm | 44020.4254 | +6307.4093 ppm | 0.0319 ppm |
| ${}^{48}$K | 48 | 29 | 129.8724 | 404.8432 | -679203.1754 ppm | 44954.4035 | +6154.3093 ppm | 0.0173 ppm |
| ${}^{49}$K | 49 | 30 | 135.4494 | 410.2415 | -669830.0697 ppm | 45888.3920 | +6024.3518 ppm | 0.0176 ppm |
| ${}^{50}$K | 50 | 31 | 141.0166 | 414.4292 | -659733.0403 ppm | 46822.3902 | +5873.6607 ppm | 0.1661 ppm |
| ${}^{51}$K | 51 | 32 | 146.5743 | 419.2881 | -650421.1105 ppm | 47756.3979 | +5743.3225 ppm | 0.2746 ppm |
| ${}^{52}$K | 52 | 33 | 152.1229 | 421.9816 | -639503.3766 ppm | 48690.4147 | +5573.2308 ppm | 0.6926 ppm |
| ${}^{53}$K | 53 | 34 | 157.6629 | 425.2110 | -629212.4635 ppm | 49624.4401 | +5420.6887 ppm | 2.2647 ppm |
| ${}^{54}$K | 54 | 35 | 163.1946 | 426.1140 | -617016.5336 ppm | 50558.4739 | +5227.9493 ppm | 7.9453 ppm |
| ${}^{55}$K | 55 | 36 | 168.7183 | 428.5600 | -606313.4407 ppm | 51492.5156 | +5072.3415 ppm | 9.7635 ppm |
| ${}^{56}$K | 56 | 37 | 174.2343 | 429.1280 | -593980.5107 ppm | 52426.5650 | +4886.0842 ppm | 11.4982 ppm |
| ${}^{57}$K | 57 | 38 | 179.7430 | 431.0910 | -583050.9787 ppm | 53360.6218 | +4732.2796 ppm | 11.2952 ppm |
| ${}^{58}$K | 58 | 39 | 185.2445 | 431.3460 | -570543.1180 ppm | 54294.6857 | +4553.2638 ppm | 12.9430 ppm |
| ${}^{59}$K | 59 | 40 | 190.7392 | 432.5880 | -559074.2031 ppm | 55228.7564 | +4398.4043 ppm | 14.5517 ppm |

### Calcium (Z = 20)

_22 of 29 isotopes with a framework prediction; 22 of 29 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{33}$Ca | 33 | 13 | — | 219.6810 | — | — | — | 12.9869 ppm |
| ${}^{34}$Ca | 34 | 14 | — | 243.8820 | — | — | — | 9.4661 ppm |
| ${}^{35}$Ca | 35 | 15 | — | 261.6600 | — | — | — | 6.1419 ppm |
| ${}^{36}$Ca | 36 | 16 | — | 281.3717 | — | — | — | 1.1930 ppm |
| ${}^{37}$Ca | 37 | 17 | — | 296.1279 | — | — | — | 0.0184 ppm |
| ${}^{38}$Ca | 38 | 18 | — | 313.1216 | — | — | — | 0.0055 ppm |
| ${}^{39}$Ca | 39 | 19 | — | 326.4172 | — | — | — | 0.0164 ppm |
| ${}^{40}$Ca | 40 | 20 | 408.7713 | 342.0522 | +195055.3738 ppm | 37158.1989 | -1792.3162 ppm | 0.0006 ppm |
| ${}^{41}$Ca | 41 | 21 | 80.3511 | 350.4150 | -770697.4466 ppm | 38426.1846 | +7077.8749 ppm | 0.0036 ppm |
| ${}^{42}$Ca | 42 | 22 | 86.0667 | 361.8957 | -762178.0410 ppm | 39360.0343 | +7057.3076 ppm | 0.0038 ppm |
| ${}^{43}$Ca | 43 | 23 | 91.7671 | 369.8286 | -751865.8297 ppm | 40293.8994 | +6948.7934 ppm | 0.0057 ppm |
| ${}^{44}$Ca | 44 | 24 | 97.4529 | 380.9598 | -744191.0815 ppm | 41227.7790 | +6924.2206 ppm | 0.0079 ppm |
| ${}^{45}$Ca | 45 | 25 | 103.1248 | 388.3746 | -734470.7040 ppm | 42161.6725 | +6811.7105 ppm | 0.0087 ppm |
| ${}^{46}$Ca | 46 | 26 | 108.7835 | 398.7733 | -727204.5526 ppm | 43095.5792 | +6774.5840 ppm | 0.0522 ppm |
| ${}^{47}$Ca | 47 | 27 | 114.4296 | 406.0497 | -718188.0770 ppm | 44029.4985 | +6667.4550 ppm | 0.0508 ppm |
| ${}^{48}$Ca | 48 | 28 | 120.0637 | 416.0012 | -711386.1623 ppm | 44963.4299 | +6625.3505 ppm | 0.0004 ppm |
| ${}^{49}$Ca | 49 | 29 | 125.6863 | 421.1476 | -701562.4773 ppm | 45897.3728 | +6479.1514 ppm | 0.0039 ppm |
| ${}^{50}$Ca | 50 | 30 | 131.2978 | 427.5082 | -692876.4854 ppm | 46831.3266 | +6365.3151 ppm | 0.0340 ppm |
| ${}^{51}$Ca | 51 | 31 | 136.8988 | 432.3226 | -683340.9820 ppm | 47765.2910 | +6223.4016 ppm | 0.0110 ppm |
| ${}^{52}$Ca | 52 | 32 | 142.4898 | 438.3279 | -674924.1963 ppm | 48699.2655 | +6111.9307 ppm | 0.0139 ppm |
| ${}^{53}$Ca | 53 | 33 | 148.0710 | 441.5206 | -664633.9001 ppm | 49633.2497 | +5947.5288 ppm | 0.8873 ppm |
| ${}^{54}$Ca | 54 | 34 | 153.6430 | 445.3648 | -655017.5809 ppm | 50567.2431 | +5802.4678 ppm | 0.9634 ppm |
| ${}^{55}$Ca | 55 | 35 | 159.2061 | 446.9259 | -643775.1862 ppm | 51501.2455 | +5618.0497 ppm | 3.1284 ppm |
| ${}^{56}$Ca | 56 | 36 | 164.7606 | 449.8573 | -633749.1248 ppm | 52435.2564 | +5466.8472 ppm | 4.7870 ppm |
| ${}^{57}$Ca | 57 | 37 | 170.3069 | 450.9840 | -622365.9978 ppm | 53369.2755 | +5286.8443 ppm | 7.5272 ppm |
| ${}^{58}$Ca | 58 | 38 | 175.8452 | 454.0240 | -612696.1388 ppm | 54303.3026 | +5148.9932 ppm | 9.2589 ppm |
| ${}^{59}$Ca | 59 | 39 | 181.3760 | 454.7720 | -601171.6259 ppm | 55237.3373 | +4973.7213 ppm | 10.9141 ppm |
| ${}^{60}$Ca | 60 | 40 | 186.8994 | 457.6200 | -591583.9349 ppm | 56171.3793 | +4843.1118 ppm | 12.5142 ppm |
| ${}^{61}$Ca | 61 | 41 | 192.4157 | 457.6830 | -579587.4863 ppm | 57105.4284 | +4667.0915 ppm | 14.0773 ppm |

### Scandium (Z = 21)

_23 of 29 isotopes with a framework prediction; 23 of 29 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{35}$Sc | 35 | 14 | — | 238.9800 | — | — | — | 12.2470 ppm |
| ${}^{36}$Sc | 36 | 15 | — | 257.9760 | — | — | — | 8.9401 ppm |
| ${}^{37}$Sc | 37 | 16 | — | 278.4250 | — | — | — | 8.7017 ppm |
| ${}^{38}$Sc | 38 | 17 | — | 294.5380 | — | — | — | 5.6586 ppm |
| ${}^{39}$Sc | 39 | 18 | — | 312.5248 | — | — | — | 0.6609 ppm |
| ${}^{40}$Sc | 40 | 19 | — | 326.9468 | — | — | — | 0.0759 ppm |
| ${}^{41}$Sc | 41 | 20 | 69.7838 | 343.1371 | -796630.1055 ppm | 38435.9696 | +7162.8649 ppm | 0.0020 ppm |
| ${}^{42}$Sc | 42 | 21 | 75.5577 | 354.6871 | -786973.6133 ppm | 39369.7610 | +7140.5773 ppm | 0.0039 ppm |
| ${}^{43}$Sc | 43 | 22 | 81.3146 | 366.8255 | -778328.8528 ppm | 40303.5695 | +7134.5593 ppm | 0.0465 ppm |
| ${}^{44}$Sc | 44 | 23 | 87.0554 | 376.5247 | -768792.3692 ppm | 41237.3942 | +7069.2144 ppm | 0.0429 ppm |
| ${}^{45}$Sc | 45 | 24 | 92.7808 | 387.8523 | -760783.3190 ppm | 42171.2343 | +7046.2977 ppm | 0.0158 ppm |
| ${}^{46}$Sc | 46 | 25 | 98.4914 | 396.6130 | -751668.6569 ppm | 43105.0890 | +6964.3304 ppm | 0.0157 ppm |
| ${}^{47}$Sc | 47 | 26 | 104.1881 | 407.2595 | -744172.6273 ppm | 44038.9577 | +6929.5884 ppm | 0.0441 ppm |
| ${}^{48}$Sc | 48 | 27 | 109.8715 | 415.4981 | -735566.8505 ppm | 44972.8398 | +6842.3099 ppm | 0.1108 ppm |
| ${}^{49}$Sc | 49 | 28 | 115.5420 | 425.6277 | -728537.3609 ppm | 45906.7347 | +6800.6320 ppm | 0.0497 ppm |
| ${}^{50}$Sc | 50 | 29 | 121.2004 | 431.6737 | -719231.4895 ppm | 46840.6417 | +6672.5239 ppm | 0.0541 ppm |
| ${}^{51}$Sc | 51 | 30 | 126.8471 | 438.4583 | -710697.5252 ppm | 47774.5605 | +6565.3640 ppm | 0.0530 ppm |
| ${}^{52}$Sc | 52 | 31 | 132.4825 | 443.8028 | -701483.3053 ppm | 48708.4904 | +6432.6195 ppm | 0.0635 ppm |
| ${}^{53}$Sc | 53 | 32 | 138.1073 | 450.1201 | -693176.7933 ppm | 49642.4311 | +6324.9645 ppm | 0.3588 ppm |
| ${}^{54}$Sc | 54 | 33 | 143.7218 | 453.8598 | -683334.4863 ppm | 50576.3821 | +6169.9137 ppm | 0.2780 ppm |
| ${}^{55}$Sc | 55 | 34 | 149.3263 | 458.3353 | -674198.5265 ppm | 51510.3429 | +6035.1809 ppm | 1.2189 ppm |
| ${}^{56}$Sc | 56 | 35 | 154.9214 | 461.0804 | -664003.5002 ppm | 52444.3133 | +5872.0779 ppm | 4.9803 ppm |
| ${}^{57}$Sc | 57 | 36 | 160.5073 | 465.0155 | -654834.4500 ppm | 53378.2927 | +5737.4557 ppm | 3.3873 ppm |
| ${}^{58}$Sc | 58 | 37 | 166.0845 | 467.1867 | -644500.8577 ppm | 54312.2810 | +5574.8195 ppm | 3.5182 ppm |
| ${}^{59}$Sc | 59 | 38 | 171.6532 | 470.6080 | -635252.3463 ppm | 55246.2777 | +5440.7597 ppm | 4.5433 ppm |
| ${}^{60}$Sc | 60 | 39 | 177.2137 | 472.3800 | -624849.2298 ppm | 56180.2826 | +5282.0299 ppm | 8.9507 ppm |
| ${}^{61}$Sc | 61 | 40 | 182.7664 | 475.4340 | -615579.8422 ppm | 57114.2954 | +5150.4112 ppm | 10.5573 ppm |
| ${}^{62}$Sc | 62 | 41 | 188.3115 | 476.6560 | -604932.0017 ppm | 58048.3157 | +4992.5751 ppm | 10.3858 ppm |
| ${}^{63}$Sc | 63 | 42 | 193.8493 | 478.9890 | -595294.7944 ppm | 58982.3433 | +4857.8970 ppm | 11.9180 ppm |

### Titanium (Z = 22)

_25 of 29 isotopes with a framework prediction; 25 of 29 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{37}$Ti | 37 | 15 | — | 256.2620 | — | — | — | 11.5861 ppm |
| ${}^{38}$Ti | 38 | 16 | — | 278.1220 | — | — | — | 8.4710 ppm |
| ${}^{39}$Ti | 39 | 17 | — | 295.0740 | — | — | — | 5.5124 ppm |
| ${}^{40}$Ti | 40 | 18 | — | 314.6345 | — | — | — | 1.8320 ppm |
| ${}^{41}$Ti | 41 | 19 | 58.8137 | 329.4099 | -821457.4018 ppm | 38446.1573 | +7088.2143 ppm | 0.7320 ppm |
| ${}^{42}$Ti | 42 | 20 | 64.6489 | 346.8881 | -813631.8286 ppm | 39379.8875 | +7218.8358 ppm | 0.0069 ppm |
| ${}^{43}$Ti | 43 | 21 | 70.4653 | 359.1706 | -803811.0902 ppm | 40313.6365 | +7213.1457 ppm | 0.1429 ppm |
| ${}^{44}$Ti | 44 | 22 | 76.2638 | 375.4749 | -796887.0443 ppm | 41247.4034 | +7307.0734 ppm | 0.0171 ppm |
| ${}^{45}$Ti | 45 | 23 | 82.0454 | 385.0079 | -786899.5848 ppm | 42181.1873 | +7234.3782 ppm | 0.0200 ppm |
| ${}^{46}$Ti | 46 | 24 | 87.8107 | 398.1973 | -779479.4538 ppm | 43114.9874 | +7251.2512 ppm | 0.0021 ppm |
| ${}^{47}$Ti | 47 | 25 | 93.5606 | 407.0779 | -770165.4960 ppm | 44048.8030 | +7168.5298 ppm | 0.0018 ppm |
| ${}^{48}$Ti | 48 | 26 | 99.2957 | 418.7046 | -762850.2705 ppm | 44982.6333 | +7151.5041 ppm | 0.0016 ppm |
| ${}^{49}$Ti | 49 | 27 | 105.0167 | 426.8470 | -753971.0444 ppm | 45916.4776 | +7058.5167 ppm | 0.0017 ppm |
| ${}^{50}$Ti | 50 | 28 | 110.7243 | 437.7861 | -747081.3718 ppm | 46850.3355 | +7030.0770 ppm | 0.0018 ppm |
| ${}^{51}$Ti | 51 | 29 | 116.4189 | 444.1586 | -737888.8108 ppm | 47784.2063 | +6906.1180 ppm | 0.0102 ppm |
| ${}^{52}$Ti | 52 | 30 | 122.1012 | 451.9746 | -729849.3622 ppm | 48718.0894 | +6817.2323 ppm | 0.0568 ppm |
| ${}^{53}$Ti | 53 | 31 | 127.7717 | 457.4497 | -720686.8956 ppm | 49651.9844 | +6684.1624 ppm | 0.0585 ppm |
| ${}^{54}$Ti | 54 | 32 | 133.4308 | 464.3834 | -712671.0603 ppm | 50585.8907 | +6585.4804 ppm | 0.3151 ppm |
| ${}^{55}$Ti | 55 | 33 | 139.0790 | 468.5433 | -703167.3490 ppm | 51519.8079 | +6436.0713 ppm | 0.5641 ppm |
| ${}^{56}$Ti | 56 | 34 | 144.7167 | 474.2052 | -694822.6914 ppm | 52453.7357 | +6321.2203 ppm | 1.9223 ppm |
| ${}^{57}$Ti | 57 | 35 | 150.3443 | 477.2553 | -684981.4637 ppm | 53387.6735 | +6161.0762 ppm | 3.8801 ppm |
| ${}^{58}$Ti | 58 | 36 | 155.9622 | 481.8425 | -676321.1768 ppm | 54321.6210 | +6035.3022 ppm | 3.3954 ppm |
| ${}^{59}$Ti | 59 | 37 | 161.5708 | 484.8620 | -666769.5106 ppm | 55255.5778 | +5885.5269 ppm | 5.4602 ppm |
| ${}^{60}$Ti | 60 | 38 | 167.1704 | 489.1671 | -658255.0441 ppm | 56189.5436 | +5763.5801 ppm | 4.3017 ppm |
| ${}^{61}$Ti | 61 | 39 | 172.7613 | 491.5380 | -648529.0164 ppm | 57123.5181 | +5611.2865 ppm | 5.2802 ppm |
| ${}^{62}$Ti | 62 | 40 | 178.3439 | 495.3800 | -639985.6132 ppm | 58057.5009 | +5491.2347 ppm | 6.9208 ppm |
| ${}^{63}$Ti | 63 | 41 | 183.9184 | 497.1330 | -630041.7670 ppm | 58991.4918 | +5337.9783 ppm | 8.5247 ppm |
| ${}^{64}$Ti | 64 | 42 | 189.4852 | 500.8640 | -621683.3691 ppm | 59925.4905 | +5222.7209 ppm | 10.0627 ppm |
| ${}^{65}$Ti | 65 | 43 | 195.0444 | 502.1900 | -611612.3457 ppm | 60859.4967 | +5072.8049 ppm | 11.5529 ppm |

### Vanadium (Z = 23)

_27 of 29 isotopes with a framework prediction; 27 of 29 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{39}$V | 39 | 16 | — | 274.2090 | — | — | — | 10.9932 ppm |
| ${}^{40}$V | 40 | 17 | — | 292.4000 | — | — | — | 8.0473 ppm |
| ${}^{41}$V | 41 | 18 | 47.4409 | 312.6250 | -848249.8125 ppm | 38456.7477 | +6943.3991 ppm | 5.2439 ppm |
| ${}^{42}$V | 42 | 19 | 53.3403 | 328.6080 | -837677.9553 ppm | 39390.4137 | +7037.7112 ppm | 5.0010 ppm |
| ${}^{43}$V | 43 | 20 | 59.2191 | 346.9891 | -829334.4305 ppm | 40324.1004 | +7187.7293 ppm | 1.0702 ppm |
| ${}^{44}$V | 44 | 21 | 65.0782 | 360.9521 | -819704.0305 ppm | 41257.8067 | +7223.1509 ppm | 0.1774 ppm |
| ${}^{45}$V | 45 | 22 | 70.9186 | 377.1018 | -811937.6626 ppm | 42191.5317 | +7310.0375 ppm | 0.0206 ppm |
| ${}^{46}$V | 46 | 23 | 76.7413 | 390.3625 | -803410.2688 ppm | 43125.2745 | +7325.6133 ppm | 0.0031 ppm |
| ${}^{47}$V | 47 | 24 | 82.5469 | 403.3650 | -795354.3130 ppm | 44059.0343 | +7334.9690 ppm | 0.0025 ppm |
| ${}^{48}$V | 48 | 25 | 88.3364 | 413.9073 | -786579.3745 ppm | 44992.8102 | +7288.8158 ppm | 0.0218 ppm |
| ${}^{49}$V | 49 | 26 | 94.1103 | 425.4628 | -778804.8340 ppm | 45926.6017 | +7267.2658 ppm | 0.0181 ppm |
| ${}^{50}$V | 50 | 27 | 99.8695 | 434.7952 | -770306.8942 ppm | 46860.4080 | +7198.7659 ppm | 0.0020 ppm |
| ${}^{51}$V | 51 | 28 | 105.6144 | 445.8463 | -763114.7508 ppm | 47794.2284 | +7169.7284 ppm | 0.0020 ppm |
| ${}^{52}$V | 52 | 29 | 111.3458 | 453.1576 | -754288.9666 ppm | 48728.0625 | +7064.2406 ppm | 0.0033 ppm |
| ${}^{53}$V | 53 | 30 | 117.0642 | 461.6376 | -746415.3383 ppm | 49661.9095 | +6986.8675 ppm | 0.0629 ppm |
| ${}^{54}$V | 54 | 31 | 122.7701 | 467.7555 | -737533.5799 ppm | 50595.7690 | +6865.2801 ppm | 0.2225 ppm |
| ${}^{55}$V | 55 | 32 | 128.4640 | 475.0537 | -729579.9839 ppm | 51529.6405 | +6771.5772 ppm | 0.5278 ppm |
| ${}^{56}$V | 56 | 33 | 134.1464 | 480.1832 | -720634.9449 ppm | 52463.5236 | +6639.5597 ppm | 3.3748 ppm |
| ${}^{57}$V | 57 | 34 | 139.8177 | 486.5062 | -712608.5089 ppm | 53397.4177 | +6535.0433 ppm | 1.5978 ppm |
| ${}^{58}$V | 58 | 35 | 145.4784 | 490.5730 | -703452.0600 ppm | 54331.3224 | +6392.2779 ppm | 1.7748 ppm |
| ${}^{59}$V | 59 | 36 | 151.1289 | 495.8244 | -695196.8139 ppm | 55265.2374 | +6276.2654 ppm | 2.5018 ppm |
| ${}^{60}$V | 60 | 37 | 156.7694 | 499.3725 | -686067.1912 ppm | 56199.1623 | +6133.6296 ppm | 3.2574 ppm |
| ${}^{61}$V | 61 | 38 | 162.4005 | 504.5335 | -678117.6284 ppm | 57133.0966 | +6024.4345 ppm | 4.1366 ppm |
| ${}^{62}$V | 62 | 39 | 168.0223 | 507.6409 | -669013.4391 ppm | 58067.0402 | +5883.1476 ppm | 4.5782 ppm |
| ${}^{63}$V | 63 | 40 | 173.6353 | 512.2392 | -661026.8678 ppm | 59000.9926 | +5772.0839 ppm | 5.7958 ppm |
| ${}^{64}$V | 64 | 41 | 179.2398 | 514.8800 | -651880.4681 ppm | 59934.9536 | +5631.7894 ppm | 6.7050 ppm |
| ${}^{65}$V | 65 | 42 | 184.8360 | 518.7650 | -643699.9663 ppm | 60868.9228 | +5516.0879 ppm | 8.2632 ppm |
| ${}^{66}$V | 66 | 43 | 190.4242 | 521.0040 | -634505.2833 ppm | 61802.9000 | +5377.8497 ppm | 8.1372 ppm |
| ${}^{67}$V | 67 | 44 | 196.0047 | 524.5430 | -626332.4153 ppm | 62736.8849 | +5264.0979 ppm | 9.6122 ppm |

### Chromium (Z = 24)

_30 of 30 isotopes with a framework prediction; 30 of 30 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{41}$Cr | 41 | 17 | 35.6653 | 291.7560 | -877756.2641 ppm | 38467.7410 | +6701.4280 ppm | 10.4578 ppm |
| ${}^{42}$Cr | 42 | 18 | 41.6320 | 313.1520 | -867055.0357 ppm | 39401.3397 | +6939.1491 ppm | 7.6653 ppm |
| ${}^{43}$Cr | 43 | 19 | 47.5760 | 330.2400 | -855935.0543 ppm | 40334.9611 | +7057.8959 ppm | 5.0002 ppm |
| ${}^{44}$Cr | 44 | 20 | 53.4985 | 349.7836 | -847052.4515 ppm | 41268.6040 | +7231.3548 ppm | 1.2504 ppm |
| ${}^{45}$Cr | 45 | 21 | 59.4006 | 363.9478 | -836788.0862 ppm | 42202.2674 | +7268.8328 ppm | 0.8448 ppm |
| ${}^{46}$Cr | 46 | 22 | 65.2832 | 381.9759 | -829090.7639 ppm | 43135.9502 | +7396.0418 ppm | 0.2675 ppm |
| ${}^{47}$Cr | 47 | 23 | 71.1472 | 395.1387 | -819943.7066 ppm | 44069.6516 | +7406.2628 ppm | 0.1188 ppm |
| ${}^{48}$Cr | 48 | 24 | 76.9935 | 411.4683 | -812881.1067 ppm | 45003.3708 | +7487.8753 ppm | 0.1637 ppm |
| ${}^{49}$Cr | 49 | 25 | 82.8228 | 422.0506 | -803760.9456 ppm | 45937.1069 | +7439.5599 ppm | 0.0483 ppm |
| ${}^{50}$Cr | 50 | 26 | 88.6359 | 435.0509 | -796263.0825 ppm | 46870.8592 | +7445.8784 ppm | 0.0020 ppm |
| ${}^{51}$Cr | 51 | 27 | 94.4336 | 444.3116 | -787460.9726 ppm | 47804.6270 | +7372.8850 ppm | 0.0035 ppm |
| ${}^{52}$Cr | 52 | 28 | 100.2163 | 456.3517 | -780396.7415 ppm | 48738.4096 | +7360.8725 ppm | 0.0023 ppm |
| ${}^{53}$Cr | 53 | 29 | 105.9849 | 464.2911 | -771727.5963 ppm | 49672.2065 | +7265.8347 ppm | 0.0023 ppm |
| ${}^{54}$Cr | 54 | 30 | 111.7397 | 474.0102 | -764267.2591 ppm | 50606.0171 | +7210.2675 ppm | 0.0026 ppm |
| ${}^{55}$Cr | 55 | 31 | 117.4815 | 480.2565 | -755377.6018 ppm | 51539.8407 | +7088.6314 ppm | 0.0045 ppm |
| ${}^{56}$Cr | 56 | 32 | 123.2107 | 488.5026 | -747778.9039 ppm | 52473.6770 | +7010.2404 ppm | 0.0111 ppm |
| ${}^{57}$Cr | 57 | 33 | 128.9277 | 493.8138 | -738914.2868 ppm | 53407.5253 | +6879.1151 ppm | 0.0351 ppm |
| ${}^{58}$Cr | 58 | 34 | 134.6331 | 501.3519 | -731459.8139 ppm | 54341.3854 | +6794.2828 ppm | 0.0552 ppm |
| ${}^{59}$Cr | 59 | 35 | 140.3273 | 505.5474 | -722424.9405 ppm | 55275.2566 | +6651.2502 ppm | 0.0122 ppm |
| ${}^{60}$Cr | 60 | 36 | 146.0107 | 512.4113 | -715051.6440 ppm | 56209.1386 | +6561.2985 ppm | 0.0200 ppm |
| ${}^{61}$Cr | 61 | 37 | 151.6837 | 516.0706 | -706079.4634 ppm | 57143.0310 | +6417.6806 ppm | 0.0328 ppm |
| ${}^{62}$Cr | 62 | 38 | 157.3467 | 522.4980 | -698856.8358 ppm | 58076.9335 | +6327.1598 ppm | 0.0597 ppm |
| ${}^{63}$Cr | 63 | 39 | 163.0000 | 525.8950 | -690052.2435 ppm | 59010.8456 | +6187.6910 ppm | 1.2389 ppm |
| ${}^{64}$Cr | 64 | 40 | 168.6439 | 531.4280 | -682658.9790 ppm | 59944.7671 | +6088.8284 ppm | 5.0341 ppm |
| ${}^{65}$Cr | 65 | 41 | 174.2788 | 534.1700 | -673739.0622 ppm | 60878.6976 | +5946.7609 ppm | 3.3092 ppm |
| ${}^{66}$Cr | 66 | 42 | 179.9050 | 539.0880 | -666279.0151 ppm | 61812.6369 | +5844.5218 ppm | 4.8808 ppm |
| ${}^{67}$Cr | 67 | 43 | 185.5227 | 541.2930 | -657260.0892 ppm | 62746.5846 | +5701.9505 ppm | 6.4050 ppm |
| ${}^{68}$Cr | 68 | 44 | 191.1323 | 545.7680 | -649792.0555 ppm | 63680.5404 | +5600.1007 ppm | 7.8990 ppm |
| ${}^{69}$Cr | 69 | 45 | 196.7340 | 547.7910 | -640859.4411 ppm | 64614.5042 | +5462.5255 ppm | 7.7838 ppm |
| ${}^{70}$Cr | 70 | 46 | 202.3280 | 551.8800 | -633384.0786 ppm | 65548.4756 | +5360.9533 ppm | 9.2008 ppm |

### Manganese (Z = 25)

_31 of 31 isotopes with a framework prediction; 31 of 31 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{43}$Mn | 43 | 18 | 35.5361 | 310.1590 | -885426.3009 ppm | 40346.2188 | +6852.7989 ppm | 9.9724 ppm |
| ${}^{44}$Mn | 44 | 19 | 41.5248 | 328.1080 | -873441.6129 ppm | 41279.7954 | +6991.2697 ppm | 7.3168 ppm |
| ${}^{45}$Mn | 45 | 20 | 47.4913 | 348.6150 | -863771.5682 ppm | 42213.3944 | +7184.9985 ppm | 7.1564 ppm |
| ${}^{46}$Mn | 46 | 21 | 53.4365 | 364.1397 | -853252.7830 ppm | 43147.0146 | +7253.2758 ppm | 2.0223 ppm |
| ${}^{47}$Mn | 47 | 22 | 59.3614 | 382.3596 | -844749.7106 ppm | 44080.6551 | +7381.5325 ppm | 0.7238 ppm |
| ${}^{48}$Mn | 48 | 23 | 65.2671 | 397.1612 | -835666.0554 ppm | 45014.3149 | +7427.8547 ppm | 0.1499 ppm |
| ${}^{49}$Mn | 49 | 24 | 71.1542 | 413.5558 | -827945.2878 ppm | 45947.9931 | +7507.8946 ppm | 0.0486 ppm |
| ${}^{50}$Mn | 50 | 25 | 77.0237 | 426.6341 | -819461.8610 ppm | 46881.6890 | +7513.3276 ppm | 0.0025 ppm |
| ${}^{51}$Mn | 51 | 26 | 82.8763 | 440.3218 | -811782.3497 ppm | 47815.4019 | +7531.8416 ppm | 0.0064 ppm |
| ${}^{52}$Mn | 52 | 27 | 88.7127 | 450.8613 | -803237.1535 ppm | 48749.1309 | +7484.4278 ppm | 0.0027 ppm |
| ${}^{53}$Mn | 53 | 28 | 94.5336 | 462.9115 | -795784.6420 ppm | 49682.8754 | +7469.9790 ppm | 0.0070 ppm |
| ${}^{54}$Mn | 54 | 29 | 100.3397 | 471.8507 | -787348.7269 ppm | 50616.6348 | +7393.9803 ppm | 0.0200 ppm |
| ${}^{55}$Mn | 55 | 30 | 106.1314 | 482.0764 | -779845.2619 ppm | 51550.4085 | +7346.3465 ppm | 0.0051 ppm |
| ${}^{56}$Mn | 56 | 31 | 111.9094 | 489.3468 | -771308.6058 ppm | 52484.1959 | +7243.5474 ppm | 0.0056 ppm |
| ${}^{57}$Mn | 57 | 32 | 117.6742 | 497.9927 | -763702.9390 ppm | 53417.9965 | +7170.7304 ppm | 0.0284 ppm |
| ${}^{58}$Mn | 58 | 33 | 123.4263 | 504.4053 | -755303.2558 ppm | 54351.8098 | +7058.9866 ppm | 0.0501 ppm |
| ${}^{59}$Mn | 59 | 34 | 129.1663 | 512.1744 | -747808.0721 ppm | 55285.6353 | +6976.1423 ppm | 0.0424 ppm |
| ${}^{60}$Mn | 60 | 35 | 134.8944 | 517.6884 | -739429.3315 ppm | 56219.4726 | +6855.6071 ppm | 0.0417 ppm |
| ${}^{61}$Mn | 61 | 36 | 140.6112 | 524.5339 | -731931.1143 ppm | 57153.3212 | +6762.8518 ppm | 0.0410 ppm |
| ${}^{62}$Mn | 62 | 37 | 146.3171 | 529.3870 | -723610.3707 ppm | 58087.1808 | +6638.5272 ppm | 0.1134 ppm |
| ${}^{63}$Mn | 63 | 38 | 152.0124 | 535.8214 | -716300.2500 ppm | 59021.0509 | +6545.4886 ppm | 0.0635 ppm |
| ${}^{64}$Mn | 64 | 39 | 157.6975 | 539.9947 | -707964.6528 ppm | 59954.9312 | +6417.3351 ppm | 0.0594 ppm |
| ${}^{65}$Mn | 65 | 40 | 163.3729 | 546.0443 | -700806.6236 ppm | 60888.8213 | +6324.5121 ppm | 0.0616 ppm |
| ${}^{66}$Mn | 66 | 41 | 169.0387 | 549.8987 | -692600.3857 ppm | 61822.7209 | +6198.7127 ppm | 0.1819 ppm |
| ${}^{67}$Mn | 67 | 42 | 174.6953 | 554.8270 | -685135.6178 ppm | 62756.6297 | +6093.7207 ppm | 3.2107 ppm |
| ${}^{68}$Mn | 68 | 43 | 180.3430 | 558.2120 | -676927.4380 ppm | 63690.5474 | +5968.2904 ppm | 4.7375 ppm |
| ${}^{69}$Mn | 69 | 44 | 185.9821 | 562.6950 | -669479.7391 ppm | 64624.4737 | +5863.8720 ppm | 6.2198 ppm |
| ${}^{70}$Mn | 70 | 45 | 191.6129 | 565.8800 | -661389.5423 ppm | 65558.4083 | +5741.7514 ppm | 7.6738 ppm |
| ${}^{71}$Mn | 71 | 46 | 197.2356 | 570.1300 | -654051.5237 ppm | 66492.3511 | +5639.6316 ppm | 7.5653 ppm |
| ${}^{72}$Mn | 72 | 47 | 202.8505 | 572.7600 | -645836.8166 ppm | 67426.3016 | +5516.1867 ppm | 8.9459 ppm |
| ${}^{73}$Mn | 73 | 48 | 208.4578 | 576.3350 | -638304.4154 ppm | 68360.2597 | +5410.7593 ppm | 8.8228 ppm |

### Iron (Z = 26)

_32 of 32 isotopes with a framework prediction; 32 of 32 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{45}$Fe | 45 | 19 | 35.1906 | 328.4550 | -892860.1465 ppm | 42224.9127 | +6994.0171 ppm | 6.7532 ppm |
| ${}^{46}$Fe | 46 | 20 | 41.2011 | 349.7380 | -882194.3322 ppm | 43158.4676 | +7200.2169 ppm | 6.9998 ppm |
| ${}^{47}$Fe | 47 | 21 | 47.1896 | 366.1300 | -871112.4014 ppm | 44092.0446 | +7286.4702 ppm | 11.4274 ppm |
| ${}^{48}$Fe | 48 | 22 | 53.1571 | 385.0908 | -861962.1275 ppm | 45025.6425 | +7426.8636 ppm | 2.0633 ppm |
| ${}^{49}$Fe | 49 | 23 | 59.1046 | 399.9043 | -852203.2359 ppm | 45959.2605 | +7470.6622 ppm | 0.5309 ppm |
| ${}^{50}$Fe | 50 | 24 | 65.0328 | 417.7013 | -844307.8357 ppm | 46892.8976 | +7577.7215 ppm | 0.1801 ppm |
| ${}^{51}$Fe | 51 | 25 | 70.9427 | 431.4854 | -835584.8386 ppm | 47826.5531 | +7595.8148 ppm | 0.0295 ppm |
| ${}^{52}$Fe | 52 | 26 | 76.8351 | 447.6996 | -828378.0600 ppm | 48760.2262 | +7664.1829 ppm | 0.0037 ppm |
| ${}^{53}$Fe | 53 | 27 | 82.7106 | 458.3863 | -819561.4434 ppm | 49693.9161 | +7617.3873 ppm | 0.0338 ppm |
| ${}^{54}$Fe | 54 | 28 | 88.5699 | 471.7648 | -812258.3485 ppm | 50627.6222 | +7626.6220 ppm | 0.0068 ppm |
| ${}^{55}$Fe | 55 | 29 | 94.4137 | 481.0629 | -803739.3524 ppm | 51561.3438 | +7555.4835 ppm | 0.0060 ppm |
| ${}^{56}$Fe | 56 | 30 | 100.2426 | 492.2600 | -796362.4044 ppm | 52495.0803 | +7523.8898 ppm | 0.0051 ppm |
| ${}^{57}$Fe | 57 | 31 | 106.0572 | 499.9061 | -787845.7138 ppm | 53428.8312 | +7426.2170 ppm | 0.0050 ppm |
| ${}^{58}$Fe | 58 | 32 | 111.8580 | 509.9507 | -780649.2988 ppm | 54362.5958 | +7376.9426 ppm | 0.0059 ppm |
| ${}^{59}$Fe | 59 | 33 | 117.6456 | 516.5317 | -772239.3481 ppm | 55296.3737 | +7266.0246 ppm | 0.0060 ppm |
| ${}^{60}$Fe | 60 | 34 | 123.4204 | 525.3512 | -765070.7367 ppm | 56230.1643 | +7199.4262 ppm | 0.0610 ppm |
| ${}^{61}$Fe | 61 | 35 | 129.1829 | 530.9299 | -756685.6671 ppm | 57163.9672 | +7077.7257 ppm | 0.0459 ppm |
| ${}^{62}$Fe | 62 | 36 | 134.9335 | 538.9588 | -749640.4812 ppm | 58097.7821 | +7002.9361 ppm | 0.0484 ppm |
| ${}^{63}$Fe | 63 | 37 | 140.6726 | 543.7876 | -741309.6689 ppm | 59031.6083 | +6875.7597 ppm | 0.0734 ppm |
| ${}^{64}$Fe | 64 | 38 | 146.4007 | 551.1929 | -734392.9732 ppm | 59965.4457 | +6796.3085 ppm | 0.0842 ppm |
| ${}^{65}$Fe | 65 | 39 | 152.1181 | 555.5126 | -726166.1829 ppm | 60899.2937 | +6668.1350 ppm | 0.0845 ppm |
| ${}^{66}$Fe | 66 | 40 | 157.8252 | 562.4338 | -719388.8035 ppm | 61833.1520 | +6586.6609 ppm | 0.0667 ppm |
| ${}^{67}$Fe | 67 | 41 | 163.5224 | 566.1457 | -711165.6018 ppm | 62767.0203 | +6455.9872 ppm | 0.0612 ppm |
| ${}^{68}$Fe | 68 | 42 | 169.2098 | 572.4240 | -704397.7316 ppm | 63700.8982 | +6369.8335 ppm | 3.0462 ppm |
| ${}^{69}$Fe | 69 | 43 | 174.8880 | 575.8050 | -696272.2209 ppm | 64634.7855 | +6241.1206 ppm | 3.1178 ppm |
| ${}^{70}$Fe | 70 | 44 | 180.5571 | 581.5600 | -689529.7579 ppm | 65568.6818 | +6153.1179 ppm | 4.6026 ppm |
| ${}^{71}$Fe | 71 | 45 | 186.2174 | 584.6850 | -681508.1335 ppm | 66502.5869 | +6027.3869 ppm | 6.0452 ppm |
| ${}^{72}$Fe | 72 | 46 | 191.8693 | 590.0400 | -674819.8871 ppm | 67436.5005 | +5939.5107 ppm | 7.4616 ppm |
| ${}^{73}$Fe | 73 | 47 | 197.5129 | 592.8330 | -666832.1369 ppm | 68370.4223 | +5815.9901 ppm | 7.3588 ppm |
| ${}^{74}$Fe | 74 | 48 | 203.1486 | 597.6240 | -660072.9641 ppm | 69304.3520 | +5724.1114 ppm | 7.2589 ppm |
| ${}^{75}$Fe | 75 | 49 | 208.7765 | 599.7000 | -651865.1583 ppm | 70238.2895 | +5596.9430 ppm | 8.5885 ppm |
| ${}^{76}$Fe | 76 | 50 | 214.3969 | 603.6680 | -644843.0922 ppm | 71172.2346 | +5499.5276 ppm | 8.4750 ppm |

### Cobalt (Z = 27)

_32 of 32 isotopes with a framework prediction; 32 of 32 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{47}$Co | 47 | 20 | 34.6317 | 347.6120 | -900372.4756 ppm | 44103.8201 | +7147.0942 ppm | 13.6988 ppm |
| ${}^{48}$Co | 48 | 21 | 40.6636 | 364.5600 | -888458.3626 ppm | 45037.3536 | +7244.0598 ppm | 11.1871 ppm |
| ${}^{49}$Co | 49 | 22 | 46.6738 | 384.1600 | -878504.2617 ppm | 45970.9089 | +7395.4018 ppm | 10.9615 ppm |
| ${}^{50}$Co | 50 | 23 | 52.6632 | 400.0319 | -868352.4429 ppm | 46904.4849 | +7461.1387 ppm | 2.7010 ppm |
| ${}^{51}$Co | 51 | 24 | 58.6328 | 417.8560 | -859681.8366 ppm | 47838.0807 | +7565.9699 ppm | 1.0202 ppm |
| ${}^{52}$Co | 52 | 25 | 64.5833 | 432.9292 | -850822.4235 ppm | 48771.6956 | +7609.9324 ppm | 0.1091 ppm |
| ${}^{53}$Co | 53 | 26 | 70.5156 | 449.3159 | -843060.0196 ppm | 49705.3288 | +7679.4506 ppm | 0.0350 ppm |
| ${}^{54}$Co | 54 | 27 | 76.4304 | 462.7379 | -834829.9577 ppm | 50638.9794 | +7687.3094 ppm | 0.0070 ppm |
| ${}^{55}$Co | 55 | 28 | 82.3285 | 476.8291 | -827341.8009 ppm | 51572.6468 | +7708.3891 ppm | 0.0079 ppm |
| ${}^{56}$Co | 56 | 29 | 88.2104 | 486.9110 | -818836.7870 ppm | 52506.3303 | +7651.4900 ppm | 0.0091 ppm |
| ${}^{57}$Co | 57 | 30 | 94.0767 | 498.2874 | -811199.8287 ppm | 53440.0293 | +7621.4732 ppm | 0.0097 ppm |
| ${}^{58}$Co | 58 | 31 | 99.9282 | 506.8604 | -802848.5942 ppm | 54373.7433 | +7540.4221 ppm | 0.0214 ppm |
| ${}^{59}$Co | 59 | 32 | 105.7654 | 517.3142 | -795549.0864 ppm | 55307.4715 | +7496.9005 ppm | 0.0072 ppm |
| ${}^{60}$Co | 60 | 33 | 111.5887 | 524.8062 | -787371.6231 ppm | 56241.2137 | +7401.6247 ppm | 0.0072 ppm |
| ${}^{61}$Co | 61 | 34 | 117.3987 | 534.1252 | -780203.8353 ppm | 57174.9691 | +7342.1396 ppm | 0.0148 ppm |
| ${}^{62}$Co | 62 | 35 | 123.1958 | 540.7228 | -772164.5300 ppm | 58108.7374 | +7237.2781 ppm | 0.3220 ppm |
| ${}^{63}$Co | 63 | 36 | 128.9806 | 549.2212 | -765157.3261 ppm | 59042.5180 | +7168.6237 ppm | 0.3169 ppm |
| ${}^{64}$Co | 64 | 37 | 134.7534 | 555.2334 | -757303.1961 ppm | 59976.3107 | +7060.2736 ppm | 0.3359 ppm |
| ${}^{65}$Co | 65 | 38 | 140.5146 | 562.6975 | -750283.9085 ppm | 60910.1148 | +6979.6285 ppm | 0.0344 ppm |
| ${}^{66}$Co | 66 | 39 | 146.2647 | 567.9922 | -742488.1637 ppm | 61843.9302 | +6866.0492 ppm | 0.2275 ppm |
| ${}^{67}$Co | 67 | 40 | 152.0040 | 574.9767 | -735634.5261 ppm | 62777.7563 | +6783.3310 ppm | 0.1033 ppm |
| ${}^{68}$Co | 68 | 41 | 157.7328 | 579.3688 | -727750.5583 ppm | 63711.5929 | +6661.9798 ppm | 0.0610 ppm |
| ${}^{69}$Co | 69 | 42 | 163.4516 | 586.1830 | -721159.4589 ppm | 64645.4395 | +6582.2799 ppm | 1.3344 ppm |
| ${}^{70}$Co | 70 | 43 | 169.1606 | 590.3939 | -713478.4578 ppm | 65579.2960 | +6464.7980 ppm | 0.1687 ppm |
| ${}^{71}$Co | 71 | 44 | 174.8601 | 596.3101 | -706763.2438 ppm | 66513.1619 | +6376.7527 ppm | 7.0361 ppm |
| ${}^{72}$Co | 72 | 45 | 180.5504 | 600.3360 | -699251.1462 ppm | 67447.0370 | +6262.5511 ppm | 4.4749 ppm |
| ${}^{73}$Co | 73 | 46 | 186.2318 | 606.0460 | -692710.1639 ppm | 68380.9211 | +6177.3728 ppm | 4.4134 ppm |
| ${}^{74}$Co | 74 | 47 | 191.9046 | 609.6860 | -685240.3423 ppm | 69314.8137 | +6063.9823 ppm | 5.8001 ppm |
| ${}^{75}$Co | 75 | 48 | 197.5690 | 614.7750 | -678632.0804 ppm | 70248.7147 | +5974.6305 ppm | 5.7225 ppm |
| ${}^{76}$Co | 76 | 49 | 203.2252 | 617.9560 | -671133.1541 ppm | 71182.6239 | +5860.4522 ppm | 7.0684 ppm |
| ${}^{77}$Co | 77 | 50 | 208.8736 | 622.3140 | -664359.7507 ppm | 72116.5409 | +5765.5021 ppm | 8.3662 ppm |
| ${}^{78}$Co | 78 | 51 | 214.5143 | 623.7660 | -656098.0472 ppm | 73050.4656 | +5633.7957 ppm | 9.6302 ppm |

### Nickel (Z = 28)

_35 of 35 isotopes with a framework prediction; 35 of 35 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{48}$Ni | 48 | 20 | 27.7866 | 347.3280 | -919999.0262 ppm | 45049.4484 | +7144.0647 ppm | 9.4753 ppm |
| ${}^{49}$Ni | 49 | 21 | 33.8620 | 365.0500 | -907240.2208 ppm | 45982.9384 | +7254.8739 ppm | 13.1404 ppm |
| ${}^{50}$Ni | 50 | 22 | 39.9149 | 385.1000 | -896351.7704 ppm | 46916.4508 | +7412.4113 ppm | 10.7408 ppm |
| ${}^{51}$Ni | 51 | 23 | 45.9465 | 401.3700 | -885525.8941 ppm | 47849.9847 | +7483.7142 ppm | 10.5320 ppm |
| ${}^{52}$Ni | 52 | 24 | 51.9575 | 420.3627 | -876398.4450 ppm | 48783.5391 | +7609.3067 ppm | 1.7123 ppm |
| ${}^{53}$Ni | 53 | 25 | 57.9488 | 435.5050 | -866938.7995 ppm | 49717.1132 | +7652.2082 ppm | 0.5097 ppm |
| ${}^{54}$Ni | 54 | 26 | 63.9213 | 453.2238 | -858963.1019 ppm | 50650.7062 | +7745.5637 ppm | 0.0927 ppm |
| ${}^{55}$Ni | 55 | 27 | 69.8756 | 467.3527 | -850486.3349 ppm | 51584.3173 | +7765.2289 ppm | 0.0138 ppm |
| ${}^{56}$Ni | 56 | 28 | 75.8126 | 483.9957 | -843361.0883 ppm | 52517.9457 | +7833.1501 ppm | 0.0077 ppm |
| ${}^{57}$Ni | 57 | 29 | 81.7328 | 494.2434 | -834630.4867 ppm | 53451.5909 | +7777.4916 ppm | 0.0107 ppm |
| ${}^{58}$Ni | 58 | 30 | 87.6369 | 506.4596 | -826961.6790 ppm | 54385.2522 | +7760.8080 ppm | 0.0065 ppm |
| ${}^{59}$Ni | 59 | 31 | 93.5256 | 515.4589 | -818558.6246 ppm | 55318.9290 | +7685.9166 ppm | 0.0064 ppm |
| ${}^{60}$Ni | 60 | 32 | 99.3993 | 526.8466 | -811331.6039 ppm | 56252.6207 | +7656.8991 ppm | 0.0063 ppm |
| ${}^{61}$Ni | 61 | 33 | 105.2587 | 534.6667 | -803132.1748 ppm | 57186.3268 | +7565.7465 ppm | 0.0063 ppm |
| ${}^{62}$Ni | 62 | 34 | 111.1042 | 545.2624 | -796237.2302 ppm | 58120.0467 | +7526.2545 ppm | 0.0073 ppm |
| ${}^{63}$Ni | 63 | 35 | 116.9363 | 552.1002 | -788197.2757 ppm | 59053.7799 | +7423.6536 ppm | 0.0073 ppm |
| ${}^{64}$Ni | 64 | 36 | 122.7556 | 561.7577 | -781479.4948 ppm | 59987.5261 | +7372.1814 ppm | 0.0078 ppm |
| ${}^{65}$Ni | 65 | 37 | 128.5624 | 567.8558 | -773600.3388 ppm | 60921.2848 | +7263.2169 ppm | 0.0080 ppm |
| ${}^{66}$Ni | 66 | 38 | 134.3571 | 576.8076 | -767067.7438 ppm | 61855.0555 | +7204.5617 ppm | 0.0228 ppm |
| ${}^{67}$Ni | 67 | 39 | 140.1402 | 582.6153 | -759463.5992 ppm | 62788.8378 | +7097.0543 ppm | 0.0463 ppm |
| ${}^{68}$Ni | 68 | 40 | 145.9120 | 590.4077 | -752862.2867 ppm | 63722.6314 | +7024.4822 ppm | 0.0471 ppm |
| ${}^{69}$Ni | 69 | 41 | 151.6730 | 594.9939 | -745084.8516 ppm | 64656.4359 | +6903.9067 ppm | 0.0580 ppm |
| ${}^{70}$Ni | 70 | 42 | 157.4233 | 602.3004 | -738629.8653 ppm | 65590.2509 | +6828.9961 ppm | 0.0329 ppm |
| ${}^{71}$Ni | 71 | 43 | 163.1635 | 606.5641 | -731003.6840 ppm | 66524.0761 | +6709.9952 ppm | 0.0338 ppm |
| ${}^{72}$Ni | 72 | 44 | 168.8938 | 613.4552 | -724684.4406 ppm | 67457.9113 | +6633.9305 ppm | 0.0334 ppm |
| ${}^{73}$Ni | 73 | 45 | 174.6144 | 617.4087 | -717181.7432 ppm | 68391.7561 | +6516.5771 ppm | 0.0357 ppm |
| ${}^{74}$Ni | 74 | 46 | 180.3258 | 624.0420 | -711035.7989 ppm | 69325.6101 | +6442.1431 ppm | 2.9075 ppm |
| ${}^{75}$Ni | 75 | 47 | 186.0281 | 627.6750 | -703623.4960 ppm | 70259.4732 | +6325.8326 ppm | 2.8685 ppm |
| ${}^{76}$Ni | 76 | 48 | 191.7217 | 633.6880 | -697450.9859 ppm | 71193.3451 | +6246.9945 ppm | 4.2394 ppm |
| ${}^{77}$Ni | 77 | 49 | 197.4067 | 636.9440 | -690072.0864 ppm | 72127.2255 | +6131.1721 ppm | 5.5743 ppm |
| ${}^{78}$Ni | 78 | 50 | 203.0835 | 642.5640 | -683948.2100 ppm | 73061.1141 | +6051.2775 ppm | 5.5026 ppm |
| ${}^{79}$Ni | 79 | 51 | 208.7522 | 643.8500 | -675775.0313 ppm | 73995.0108 | +5915.4070 ppm | 6.8001 ppm |
| ${}^{80}$Ni | 80 | 52 | 214.4132 | 647.0400 | -668624.5349 ppm | 74928.9153 | +5807.3608 ppm | 8.0525 ppm |
| ${}^{81}$Ni | 81 | 53 | 220.0665 | 648.0000 | -660391.1684 ppm | 75862.8274 | +5672.3674 ppm | 9.2736 ppm |
| ${}^{82}$Ni | 82 | 54 | 225.7125 | 650.6700 | -653107.5978 ppm | 76796.7468 | +5564.2262 ppm | 10.4771 ppm |

### Copper (Z = 29)

_33 of 33 isotopes with a framework prediction; 33 of 33 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{52}$Cu | 52 | 23 | 38.9576 | 398.8920 | -902335.5849 ppm | 48795.7567 | +7431.3420 ppm | 12.3851 ppm |
| ${}^{53}$Cu | 53 | 24 | 45.0101 | 418.2230 | -892377.6553 ppm | 49729.2696 | +7561.8236 ppm | 10.1348 ppm |
| ${}^{54}$Cu | 54 | 25 | 51.0424 | 434.4300 | -882507.1510 ppm | 50662.8027 | +7624.6082 ppm | 7.9478 ppm |
| ${}^{55}$Cu | 55 | 26 | 57.0552 | 452.8698 | -874014.1194 ppm | 51596.3553 | +7730.6811 ppm | 3.0382 ppm |
| ${}^{56}$Cu | 56 | 27 | 63.0493 | 467.9355 | -865260.7637 ppm | 52529.9267 | +7767.6033 ppm | 0.1227 ppm |
| ${}^{57}$Cu | 57 | 28 | 69.0253 | 484.6861 | -857587.5398 ppm | 53463.5161 | +7835.5886 ppm | 0.0094 ppm |
| ${}^{58}$Cu | 58 | 29 | 74.9841 | 497.1162 | -849161.8433 ppm | 54397.1227 | +7820.8919 ppm | 0.0104 ppm |
| ${}^{59}$Cu | 59 | 30 | 80.9262 | 509.8782 | -841283.2638 ppm | 55330.7460 | +7813.0851 ppm | 0.0096 ppm |
| ${}^{60}$Cu | 60 | 31 | 86.8523 | 519.9363 | -832955.9650 ppm | 56264.3854 | +7757.0189 ppm | 0.0289 ppm |
| ${}^{61}$Cu | 61 | 32 | 92.7629 | 531.6464 | -825517.7664 ppm | 57198.0402 | +7732.3908 ppm | 0.0167 ppm |
| ${}^{62}$Cu | 62 | 33 | 98.6585 | 540.5212 | -817475.1655 ppm | 58131.7100 | +7659.2868 ppm | 0.0110 ppm |
| ${}^{63}$Cu | 63 | 34 | 104.5399 | 551.3848 | -810404.9210 ppm | 59065.3941 | +7622.9355 ppm | 0.0073 ppm |
| ${}^{64}$Cu | 64 | 35 | 110.4073 | 559.3007 | -802597.6359 ppm | 59999.0921 | +7538.0750 ppm | 0.0072 ppm |
| ${}^{65}$Cu | 65 | 36 | 116.2613 | 569.2113 | -795750.1751 ppm | 60932.8035 | +7489.2777 ppm | 0.0106 ppm |
| ${}^{66}$Cu | 66 | 37 | 122.1024 | 576.2772 | -788118.6862 ppm | 61866.5278 | +7395.5036 ppm | 0.0106 ppm |
| ${}^{67}$Cu | 67 | 38 | 127.9309 | 585.4098 | -781467.7528 ppm | 62800.2647 | +7338.1276 ppm | 0.0143 ppm |
| ${}^{68}$Cu | 68 | 39 | 133.7474 | 591.7286 | -773971.8026 ppm | 63734.0137 | +7237.8383 ppm | 0.0250 ppm |
| ${}^{69}$Cu | 69 | 40 | 139.5521 | 599.9691 | -767401.2555 ppm | 64667.7744 | +7170.7901 ppm | 0.0218 ppm |
| ${}^{70}$Cu | 70 | 41 | 145.3454 | 605.2806 | -759871.0008 ppm | 65601.5465 | +7060.5499 ppm | 0.0166 ppm |
| ${}^{71}$Cu | 71 | 42 | 151.1278 | 613.0867 | -753496.8525 ppm | 66535.3295 | +6991.6110 ppm | 0.0226 ppm |
| ${}^{72}$Cu | 72 | 43 | 156.8995 | 618.2298 | -746211.6890 ppm | 67469.1232 | +6884.7332 ppm | 0.0209 ppm |
| ${}^{73}$Cu | 73 | 44 | 162.6609 | 625.5056 | -739952.9286 ppm | 68402.9273 | +6812.5490 ppm | 0.0286 ppm |
| ${}^{74}$Cu | 74 | 45 | 168.4123 | 630.5957 | -732931.4438 ppm | 69336.7413 | +6710.5164 ppm | 0.0893 ppm |
| ${}^{75}$Cu | 75 | 46 | 174.1539 | 637.1310 | -726659.1319 ppm | 70270.5651 | +6632.1946 ppm | 0.0103 ppm |
| ${}^{76}$Cu | 76 | 47 | 179.8862 | 641.7137 | -719678.4688 ppm | 71204.3983 | +6528.2898 ppm | 0.0129 ppm |
| ${}^{77}$Cu | 77 | 48 | 185.6093 | 647.6663 | -713418.3626 ppm | 72138.2406 | +6446.4571 ppm | 0.0169 ppm |
| ${}^{78}$Cu | 78 | 49 | 191.3234 | 651.6642 | -706407.9364 ppm | 73072.0918 | +6339.7620 ppm | 0.1836 ppm |
| ${}^{79}$Cu | 79 | 50 | 197.0290 | 657.3541 | -700269.6276 ppm | 74005.9517 | +6259.0473 ppm | 1.4274 ppm |
| ${}^{80}$Cu | 80 | 51 | 202.7261 | 659.6800 | -692690.1867 ppm | 74939.8200 | +6135.2531 ppm | 4.0270 ppm |
| ${}^{81}$Cu | 81 | 52 | 208.4151 | 662.9850 | -685641.2750 ppm | 75873.6964 | +6027.4406 ppm | 3.9770 ppm |
| ${}^{82}$Cu | 82 | 53 | 214.0962 | 664.8560 | -677981.1597 ppm | 76807.5808 | +5903.7848 ppm | 5.2335 ppm |
| ${}^{83}$Cu | 83 | 54 | 219.7695 | 667.6520 | -670832.3071 ppm | 77741.4729 | +5794.1745 ppm | 6.4716 ppm |
| ${}^{84}$Cu | 84 | 55 | 225.4353 | 669.0600 | -663056.7407 ppm | 78675.3726 | +5670.1739 ppm | 6.3940 ppm |

### Zinc (Z = 30)

_33 of 33 isotopes with a framework prediction; 33 of 33 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{54}$Zn | 54 | 24 | 37.7939 | 418.0680 | -909598.7618 ppm | 50675.2689 | +7561.1723 ppm | 4.2968 ppm |
| ${}^{55}$Zn | 55 | 25 | 43.8672 | 434.7200 | -899090.8853 ppm | 51608.7610 | +7631.2152 ppm | 7.8022 ppm |
| ${}^{56}$Zn | 56 | 26 | 49.9205 | 453.9360 | -890027.5306 ppm | 52542.2732 | +7748.4932 ppm | 7.6644 ppm |
| ${}^{57}$Zn | 57 | 27 | 55.9544 | 469.1670 | -880736.7041 ppm | 53475.8047 | +7786.8550 ppm | 3.7742 ppm |
| ${}^{58}$Zn | 58 | 28 | 61.9698 | 486.9649 | -872742.8477 ppm | 54409.3547 | +7872.5687 ppm | 0.9262 ppm |
| ${}^{59}$Zn | 59 | 29 | 67.9673 | 499.9530 | -864052.7191 ppm | 55342.9227 | +7867.0342 ppm | 0.0138 ppm |
| ${}^{60}$Zn | 60 | 30 | 73.9475 | 514.9831 | -856407.8695 ppm | 56276.5078 | +7898.8507 ppm | 0.0098 ppm |
| ${}^{61}$Zn | 61 | 31 | 79.9112 | 525.2289 | -847854.5088 ppm | 57210.1095 | +7844.9707 ppm | 0.2801 ppm |
| ${}^{62}$Zn | 62 | 32 | 85.8589 | 538.1194 | -840446.3845 ppm | 58143.7273 | +7839.3040 ppm | 0.0107 ppm |
| ${}^{63}$Zn | 63 | 33 | 91.7912 | 547.2361 | -832264.0664 ppm | 59077.3605 | +7769.1994 ppm | 0.0266 ppm |
| ${}^{64}$Zn | 64 | 34 | 97.7085 | 559.0980 | -825239.0143 ppm | 60011.0085 | +7747.9907 ppm | 0.0108 ppm |
| ${}^{65}$Zn | 65 | 35 | 103.6115 | 567.0773 | -817288.5970 ppm | 60944.6710 | +7662.9797 ppm | 0.0107 ppm |
| ${}^{66}$Zn | 66 | 36 | 109.5006 | 578.1358 | -810597.1617 ppm | 61878.3473 | +7631.2961 ppm | 0.0121 ppm |
| ${}^{67}$Zn | 67 | 37 | 115.3762 | 585.1883 | -802839.1773 ppm | 62812.0371 | +7536.0243 ppm | 0.0121 ppm |
| ${}^{68}$Zn | 68 | 38 | 121.2388 | 595.3864 | -796369.4688 ppm | 63745.7399 | +7493.8525 ppm | 0.0123 ppm |
| ${}^{69}$Zn | 69 | 39 | 127.0889 | 601.8684 | -788842.7118 ppm | 64679.4552 | +7394.7883 ppm | 0.0124 ppm |
| ${}^{70}$Zn | 70 | 40 | 132.9268 | 611.0866 | -782474.6980 ppm | 65613.1828 | +7341.0622 ppm | 0.0294 ppm |
| ${}^{71}$Zn | 71 | 41 | 138.7529 | 616.9220 | -775088.4195 ppm | 66546.9221 | +7237.4533 ppm | 0.0402 ppm |
| ${}^{72}$Zn | 72 | 42 | 144.5676 | 625.8100 | -768991.2823 ppm | 67480.6728 | +7182.7906 ppm | 0.0320 ppm |
| ${}^{73}$Zn | 73 | 43 | 150.3712 | 631.3292 | -761818.1658 ppm | 68414.4347 | +7079.8455 ppm | 0.0274 ppm |
| ${}^{74}$Zn | 74 | 44 | 156.1640 | 639.5638 | -755827.3501 ppm | 69348.2073 | +7019.5550 ppm | 0.0365 ppm |
| ${}^{75}$Zn | 75 | 45 | 161.9464 | 644.4374 | -748701.0607 ppm | 70281.9903 | +6912.5337 ppm | 0.0280 ppm |
| ${}^{76}$Zn | 76 | 46 | 167.7187 | 652.2528 | -742862.3731 ppm | 71215.7834 | +6850.3598 ppm | 0.0206 ppm |
| ${}^{77}$Zn | 77 | 47 | 173.4812 | 656.8103 | -735873.1663 ppm | 72149.5863 | +6744.1714 ppm | 0.0275 ppm |
| ${}^{78}$Zn | 78 | 48 | 179.2342 | 663.5756 | -729896.4012 ppm | 73083.3988 | +6671.4631 ppm | 0.0268 ppm |
| ${}^{79}$Zn | 79 | 49 | 184.9778 | 667.5960 | -722919.4873 ppm | 74017.2205 | +6563.1501 ppm | 0.0302 ppm |
| ${}^{80}$Zn | 80 | 50 | 190.7125 | 673.8837 | -716994.8940 ppm | 74951.0513 | +6488.3222 ppm | 0.0347 ppm |
| ${}^{81}$Zn | 81 | 51 | 196.4384 | 676.5060 | -709627.9744 ppm | 75884.8908 | +6366.5431 ppm | 0.0667 ppm |
| ${}^{82}$Zn | 82 | 52 | 202.1558 | 680.6916 | -703014.1089 ppm | 76818.7388 | +6268.4701 ppm | 0.0403 ppm |
| ${}^{83}$Zn | 83 | 53 | 207.8649 | 682.7580 | -695551.1187 ppm | 77752.5951 | +6145.0392 ppm | 3.8813 ppm |
| ${}^{84}$Zn | 84 | 54 | 213.5659 | 686.3640 | -688844.4937 ppm | 78686.4595 | +6044.7859 ppm | 5.1092 ppm |
| ${}^{85}$Zn | 85 | 55 | 219.2591 | 687.6500 | -681147.2247 ppm | 79620.3318 | +5918.1526 ppm | 6.3197 ppm |
| ${}^{86}$Zn | 86 | 56 | 224.9446 | 690.7520 | -674348.1983 ppm | 80554.2117 | +5815.8258 ppm | 6.2458 ppm |

### Gallium (Z = 31)

_33 of 33 isotopes with a framework prediction; 33 of 33 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{56}$Ga | 56 | 25 | 36.4261 | 431.5920 | -915600.5033 ppm | 52554.9852 | +7575.8485 ppm | 9.5900 ppm |
| ${}^{57}$Ga | 57 | 26 | 42.5200 | 451.2120 | -905764.9567 ppm | 53488.4567 | +7699.7822 ppm | 7.5285 ppm |
| ${}^{58}$Ga | 58 | 27 | 48.5939 | 467.4220 | -896038.4163 ppm | 54421.9482 | +7755.6632 ppm | 5.5541 ppm |
| ${}^{59}$Ga | 59 | 28 | 54.6487 | 485.6880 | -887481.7946 ppm | 55355.4588 | +7848.3683 ppm | 3.1036 ppm |
| ${}^{60}$Ga | 60 | 29 | 60.6851 | 499.6200 | -878537.4433 ppm | 56288.9879 | +7859.1151 ppm | 3.5859 ppm |
| ${}^{61}$Ga | 61 | 30 | 66.7037 | 515.2323 | -870536.5667 ppm | 57222.5347 | +7900.2531 ppm | 0.6692 ppm |
| ${}^{62}$Ga | 62 | 31 | 72.7052 | 528.1560 | -862341.3453 ppm | 58156.0986 | +7893.3464 ppm | 0.0110 ppm |
| ${}^{63}$Ga | 63 | 32 | 78.6902 | 540.7874 | -854489.5371 ppm | 59089.6790 | +7881.9150 ppm | 0.0222 ppm |
| ${}^{64}$Ga | 64 | 33 | 84.6593 | 551.1444 | -846393.6965 ppm | 60023.2754 | +7832.6186 ppm | 0.0240 ppm |
| ${}^{65}$Ga | 65 | 34 | 90.6129 | 563.0404 | -839065.0201 ppm | 60956.8872 | +7810.7330 ppm | 0.0131 ppm |
| ${}^{66}$Ga | 66 | 35 | 96.5517 | 572.1780 | -831255.8988 ppm | 61890.5139 | +7744.4865 ppm | 0.0178 ppm |
| ${}^{67}$Ga | 67 | 36 | 102.4760 | 583.4047 | -824348.2938 ppm | 62824.1549 | +7714.2164 ppm | 0.0189 ppm |
| ${}^{68}$Ga | 68 | 37 | 108.3865 | 591.6829 | -816816.5871 ppm | 63757.8099 | +7638.0973 ppm | 0.0226 ppm |
| ${}^{69}$Ga | 69 | 38 | 114.2835 | 601.9960 | -810159.0382 ppm | 64691.4783 | +7596.3297 ppm | 0.0186 ppm |
| ${}^{70}$Ga | 70 | 39 | 120.1675 | 609.6497 | -802890.9389 ppm | 65625.1598 | +7514.8163 ppm | 0.0184 ppm |
| ${}^{71}$Ga | 71 | 40 | 126.0388 | 618.9500 | -796366.7042 ppm | 66558.8538 | +7460.9031 ppm | 0.0123 ppm |
| ${}^{72}$Ga | 72 | 41 | 131.8979 | 625.4704 | -789122.0271 ppm | 67492.5601 | +7366.8719 ppm | 0.0122 ppm |
| ${}^{73}$Ga | 73 | 42 | 137.7452 | 634.6528 | -782959.7592 ppm | 68426.2783 | +7315.0696 ppm | 0.0247 ppm |
| ${}^{74}$Ga | 74 | 43 | 143.5810 | 641.0744 | -776030.7398 ppm | 69360.0080 | +7224.4517 ppm | 0.0435 ppm |
| ${}^{75}$Ga | 75 | 44 | 149.4056 | 649.5567 | -769988.4266 ppm | 70293.7488 | +7166.1536 ppm | 0.0096 ppm |
| ${}^{76}$Ga | 76 | 45 | 155.2193 | 655.4641 | -763191.6742 ppm | 71227.5004 | +7072.8771 ppm | 0.0277 ppm |
| ${}^{77}$Ga | 77 | 46 | 161.0226 | 663.2311 | -757214.9109 ppm | 72161.2626 | +7008.3110 ppm | 0.0338 ppm |
| ${}^{78}$Ga | 78 | 47 | 166.8157 | 669.0141 | -750654.4799 ppm | 73095.0349 | +6918.0233 ppm | 0.0145 ppm |
| ${}^{79}$Ga | 79 | 48 | 172.5988 | 675.9297 | -744649.7615 ppm | 74028.8172 | +6845.6722 ppm | 0.0164 ppm |
| ${}^{80}$Ga | 80 | 49 | 178.3723 | 680.6764 | -737948.4215 ppm | 74962.6091 | +6745.9369 ppm | 0.0388 ppm |
| ${}^{81}$Ga | 81 | 50 | 184.1364 | 687.1520 | -732029.5275 ppm | 75896.4104 | +6671.8843 ppm | 0.0433 ppm |
| ${}^{82}$Ga | 82 | 51 | 189.8914 | 690.5261 | -725004.6680 ppm | 76830.2209 | +6558.8602 ppm | 0.0318 ppm |
| ${}^{83}$Ga | 83 | 52 | 195.6376 | 694.9238 | -718476.2138 ppm | 77764.0402 | +6462.0237 ppm | 0.0338 ppm |
| ${}^{84}$Ga | 84 | 53 | 201.3751 | 697.8321 | -711427.6215 ppm | 78697.8681 | +6348.4469 ppm | 0.3812 ppm |
| ${}^{85}$Ga | 85 | 54 | 207.1042 | 701.5533 | -704791.9992 ppm | 79631.7044 | +6248.0011 ppm | 0.4708 ppm |
| ${}^{86}$Ga | 86 | 55 | 212.8251 | 703.6520 | -697542.1635 ppm | 80565.5489 | +6129.4760 ppm | 4.9905 ppm |
| ${}^{87}$Ga | 87 | 56 | 218.5380 | 706.7880 | -690801.2181 ppm | 81499.4014 | +6027.3727 ppm | 6.1746 ppm |
| ${}^{88}$Ga | 88 | 57 | 224.2431 | 708.4000 | -683451.2367 ppm | 82433.2617 | +5908.1911 ppm | 6.1039 ppm |

### Germanium (Z = 32)

_33 of 33 isotopes with a framework prediction; 33 of 33 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{58}$Ge | 58 | 26 | 34.8566 | 450.6600 | -922654.3553 ppm | 54434.9032 | +7697.7393 ppm | 9.2599 ppm |
| ${}^{59}$Ge | 59 | 27 | 40.9707 | 467.5160 | -912365.2284 ppm | 55368.3546 | +7764.0828 ppm | 7.2734 ppm |
| ${}^{60}$Ge | 60 | 28 | 47.0650 | 486.7800 | -903313.5260 ppm | 56301.8256 | +7871.3400 ppm | 5.3693 ppm |
| ${}^{61}$Ge | 61 | 29 | 53.1405 | 501.1150 | -893955.5650 ppm | 57235.3156 | +7888.4690 ppm | 5.2818 ppm |
| ${}^{62}$Ge | 62 | 30 | 59.1976 | 517.5140 | -885611.6282 ppm | 58168.8239 | +7941.8720 ppm | 2.4211 ppm |
| ${}^{63}$Ge | 63 | 31 | 65.2371 | 530.3792 | -876999.1849 ppm | 59102.3499 | +7932.5495 ppm | 0.6354 ppm |
| ${}^{64}$Ge | 64 | 32 | 71.2595 | 545.8448 | -869450.9336 ppm | 60035.8928 | +7968.0202 ppm | 0.0626 ppm |
| ${}^{65}$Ge | 65 | 33 | 77.2655 | 556.0788 | -861052.9056 ppm | 60969.4522 | +7915.5013 ppm | 0.0358 ppm |
| ${}^{66}$Ge | 66 | 34 | 83.2557 | 569.2789 | -853752.4427 ppm | 61903.0275 | +7913.5047 ppm | 0.0391 ppm |
| ${}^{67}$Ge | 67 | 35 | 89.2304 | 578.4169 | -845733.4020 ppm | 62836.6182 | +7846.1450 ppm | 0.0693 ppm |
| ${}^{68}$Ge | 68 | 36 | 95.1903 | 590.7933 | -838877.1366 ppm | 63770.2237 | +7832.5793 ppm | 0.0296 ppm |
| ${}^{69}$Ge | 69 | 37 | 101.1358 | 598.9865 | -831155.0706 ppm | 64703.8436 | +7753.9671 ppm | 0.0205 ppm |
| ${}^{70}$Ge | 70 | 38 | 107.0674 | 610.5192 | -824628.8687 ppm | 65637.4775 | +7729.4813 ppm | 0.0126 ppm |
| ${}^{71}$Ge | 71 | 39 | 112.9856 | 617.9351 | -817156.2659 ppm | 66571.1247 | +7643.0949 ppm | 0.0123 ppm |
| ${}^{72}$Ge | 72 | 40 | 118.8906 | 628.6857 | -810890.1929 ppm | 67504.7851 | +7609.4578 ppm | 0.0011 ppm |
| ${}^{73}$Ge | 73 | 41 | 124.7830 | 635.4686 | -803636.2058 ppm | 68438.4581 | +7518.0750 ppm | 0.0008 ppm |
| ${}^{74}$Ge | 74 | 42 | 130.6632 | 645.6649 | -797630.0662 ppm | 69372.1434 | +7479.2853 ppm | 0.0002 ppm |
| ${}^{75}$Ge | 75 | 43 | 136.5314 | 652.1707 | -790650.8725 ppm | 70305.8406 | +7388.4274 ppm | 0.0007 ppm |
| ${}^{76}$Ge | 76 | 44 | 142.3880 | 661.5980 | -784781.6513 ppm | 71239.5494 | +7341.7412 ppm | 0.0003 ppm |
| ${}^{77}$Ge | 77 | 45 | 148.2334 | 667.6693 | -777983.7156 ppm | 72173.2694 | +7249.2464 ppm | 0.0007 ppm |
| ${}^{78}$Ge | 78 | 46 | 154.0680 | 676.3898 | -772220.1317 ppm | 73107.0003 | +7196.0404 ppm | 0.0487 ppm |
| ${}^{79}$Ge | 79 | 47 | 159.8919 | 682.1262 | -765597.7734 ppm | 74040.7418 | +7103.4465 ppm | 0.5055 ppm |
| ${}^{80}$Ge | 80 | 48 | 165.7055 | 690.2057 | -759918.6076 ppm | 74974.4936 | +7045.0054 ppm | 0.0276 ppm |
| ${}^{81}$Ge | 81 | 49 | 171.5092 | 695.0334 | -753236.0757 ppm | 75908.2554 | +6944.7045 ppm | 0.0272 ppm |
| ${}^{82}$Ge | 82 | 50 | 177.3030 | 702.2280 | -747513.5826 ppm | 76842.0269 | +6878.2158 ppm | 0.0294 ppm |
| ${}^{83}$Ge | 83 | 51 | 183.0875 | 705.8607 | -740618.1585 ppm | 77775.8079 | +6767.0321 ppm | 0.0314 ppm |
| ${}^{84}$Ge | 84 | 52 | 188.8626 | 711.1040 | -734409.2613 ppm | 78709.5982 | +6679.3649 ppm | 0.0405 ppm |
| ${}^{85}$Ge | 85 | 53 | 194.6289 | 714.1504 | -727467.9426 ppm | 79643.3974 | +6565.9319 ppm | 0.0471 ppm |
| ${}^{86}$Ge | 86 | 54 | 200.3863 | 718.4982 | -721103.9001 ppm | 80577.2053 | +6471.6237 ppm | 5.4685 ppm |
| ${}^{87}$Ge | 87 | 55 | 206.1353 | 720.7950 | -714016.7476 ppm | 81511.0218 | +6353.6772 ppm | 3.7031 ppm |
| ${}^{88}$Ge | 88 | 56 | 211.8760 | 724.7680 | -707663.7514 ppm | 82444.8465 | +6259.8890 ppm | 4.8774 ppm |
| ${}^{89}$Ge | 89 | 57 | 217.6085 | 726.3290 | -700399.5028 ppm | 83378.6794 | +6139.0691 ppm | 4.8221 ppm |
| ${}^{90}$Ge | 90 | 58 | 223.3332 | 729.8100 | -693984.4420 ppm | 84312.5201 | +6043.9705 ppm | 5.9687 ppm |

### Arsenic (Z = 33)

_33 of 33 isotopes with a framework prediction; 33 of 33 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{60}$As | 60 | 27 | 33.0873 | 464.1000 | -928706.5622 ppm | 56315.0210 | +7712.6722 ppm | 7.1507 ppm |
| ${}^{61}$As | 61 | 28 | 39.2213 | 483.7300 | -918918.9247 ppm | 57248.4524 | +7825.3747 ppm | 5.2803 ppm |
| ${}^{62}$As | 62 | 29 | 45.3359 | 499.0380 | -909153.3709 ppm | 58181.9033 | +7859.0492 ppm | 5.1957 ppm |
| ${}^{63}$As | 63 | 30 | 51.4317 | 516.1590 | -900356.8904 ppm | 59115.3729 | +7923.9497 ppm | 3.4146 ppm |
| ${}^{64}$As | 64 | 31 | 57.5093 | 530.3040 | -891554.0785 ppm | 60048.8607 | +7935.5776 ppm | 3.4085 ppm |
| ${}^{65}$As | 65 | 32 | 63.5694 | 545.7553 | -883520.3269 ppm | 60982.3660 | +7969.9989 ppm | 1.4011 ppm |
| ${}^{66}$As | 66 | 33 | 69.6126 | 558.9146 | -875450.4727 ppm | 61915.8883 | +7965.6479 ppm | 0.0925 ppm |
| ${}^{67}$As | 67 | 34 | 75.6393 | 571.5481 | -867658.8414 ppm | 62849.4270 | +7953.1878 ppm | 0.0071 ppm |
| ${}^{68}$As | 68 | 35 | 81.6503 | 581.9267 | -859689.7424 ppm | 63782.9814 | +7905.4286 ppm | 0.0292 ppm |
| ${}^{69}$As | 69 | 36 | 87.6459 | 594.2157 | -852501.5110 ppm | 64716.5512 | +7889.2758 ppm | 0.4983 ppm |
| ${}^{70}$As | 70 | 37 | 93.6267 | 603.5088 | -844862.7229 ppm | 65650.1358 | +7827.4575 ppm | 0.0214 ppm |
| ${}^{71}$As | 71 | 38 | 99.5931 | 615.1394 | -838096.6297 ppm | 66583.7348 | +7803.2522 ppm | 0.0630 ppm |
| ${}^{72}$As | 72 | 39 | 105.5456 | 623.5473 | -830733.5200 ppm | 67517.3478 | +7731.4501 ppm | 0.0609 ppm |
| ${}^{73}$As | 73 | 40 | 111.4847 | 634.3415 | -824251.3494 ppm | 68450.9742 | +7697.2154 ppm | 0.0567 ppm |
| ${}^{74}$As | 74 | 41 | 117.4106 | 642.3201 | -817208.6007 ppm | 69384.6137 | +7622.8914 ppm | 0.0246 ppm |
| ${}^{75}$As | 75 | 42 | 123.3238 | 652.5656 | -811016.9545 ppm | 70318.2658 | +7583.4599 ppm | 0.0127 ppm |
| ${}^{76}$As | 76 | 43 | 129.2248 | 659.8941 | -804173.4993 ppm | 71251.9303 | +7503.6819 ppm | 0.0125 ppm |
| ${}^{77}$As | 77 | 44 | 135.1137 | 669.5904 | -798214.3789 ppm | 72185.6068 | +7459.4380 ppm | 0.0236 ppm |
| ${}^{78}$As | 78 | 45 | 140.9910 | 676.5623 | -791606.7124 ppm | 73119.2949 | +7378.6760 ppm | 0.1347 ppm |
| ${}^{79}$As | 79 | 46 | 146.8571 | 685.4528 | -785751.6861 ppm | 74052.9943 | +7326.4036 ppm | 0.0724 ppm |
| ${}^{80}$As | 80 | 47 | 152.7122 | 692.1026 | -779350.3764 ppm | 74986.7046 | +7245.2703 ppm | 0.0448 ppm |
| ${}^{81}$As | 81 | 48 | 158.5566 | 700.4926 | -773649.8831 ppm | 75920.4256 | +7189.5383 ppm | 0.0351 ppm |
| ${}^{82}$As | 82 | 49 | 164.3906 | 706.1361 | -767196.9556 ppm | 76854.1570 | +7099.0541 ppm | 0.0489 ppm |
| ${}^{83}$As | 83 | 50 | 170.2146 | 713.7713 | -761527.8610 ppm | 77787.8985 | +7036.8548 ppm | 0.0362 ppm |
| ${}^{84}$As | 84 | 51 | 176.0287 | 718.0268 | -754843.8687 ppm | 78721.6498 | +6932.7331 ppm | 0.0405 ppm |
| ${}^{85}$As | 85 | 52 | 181.8332 | 723.4337 | -748652.5386 ppm | 79655.4107 | +6845.8466 ppm | 0.0389 ppm |
| ${}^{86}$As | 86 | 53 | 187.6285 | 727.2780 | -742012.7427 ppm | 80589.1809 | +6741.4522 ppm | 0.0431 ppm |
| ${}^{87}$As | 87 | 54 | 193.4146 | 732.0051 | -735774.2136 ppm | 81522.9601 | +6650.5550 ppm | 0.0369 ppm |
| ${}^{88}$As | 88 | 55 | 199.1920 | 734.8880 | -728949.2378 ppm | 82456.7482 | +6539.4295 ppm | 2.4447 ppm |
| ${}^{89}$As | 89 | 56 | 204.9607 | 739.0560 | -722672.3622 ppm | 83390.5449 | +6446.0851 ppm | 3.6200 ppm |
| ${}^{90}$As | 90 | 57 | 210.7210 | 741.6000 | -715856.3189 ppm | 84324.3501 | +6335.4706 ppm | 4.7690 ppm |
| ${}^{91}$As | 91 | 58 | 216.4731 | 745.1990 | -709509.7308 ppm | 85258.1634 | +6239.8554 ppm | 4.7163 ppm |
| ${}^{92}$As | 92 | 59 | 222.2172 | 747.1320 | -702573.0822 ppm | 86191.9847 | +6127.2885 ppm | 5.8390 ppm |

### Selenium (Z = 34)

_33 of 33 isotopes with a framework prediction; 33 of 33 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{63}$Se | 63 | 29 | 37.2741 | 498.7710 | -925268.1457 ppm | 59128.7482 | +7865.8744 ppm | 8.5263 ppm |
| ${}^{64}$Se | 64 | 30 | 43.4086 | 516.8000 | -916005.0181 ppm | 60062.1791 | +7944.7206 ppm | 8.3944 ppm |
| ${}^{65}$Se | 65 | 31 | 49.5245 | 531.0500 | -906742.3259 ppm | 60995.6286 | +7957.3439 ppm | 4.9565 ppm |
| ${}^{66}$Se | 66 | 32 | 55.6224 | 547.8000 | -898462.2939 ppm | 61929.0962 | +8010.5778 ppm | 3.2598 ppm |
| ${}^{67}$Se | 67 | 33 | 61.7028 | 560.7588 | -889965.5098 ppm | 62862.5811 | +8002.3779 ppm | 1.0754 ppm |
| ${}^{68}$Se | 68 | 34 | 67.7664 | 576.4393 | -882439.6191 ppm | 63796.0830 | +8037.5126 ppm | 0.0078 ppm |
| ${}^{69}$Se | 69 | 35 | 73.8137 | 586.7559 | -874200.2586 ppm | 64729.6011 | +7987.6879 ppm | 0.0232 ppm |
| ${}^{70}$Se | 70 | 36 | 79.8453 | 600.3224 | -866996.0018 ppm | 65663.1349 | +7989.8121 ppm | 0.0243 ppm |
| ${}^{71}$Se | 71 | 37 | 85.8615 | 609.6103 | -859153.4074 ppm | 66596.6841 | +7926.8352 ppm | 0.0423 ppm |
| ${}^{72}$Se | 72 | 38 | 91.8630 | 622.4033 | -852406.0060 ppm | 67530.2481 | +7918.5540 ppm | 0.0292 ppm |
| ${}^{73}$Se | 73 | 39 | 97.8501 | 630.8338 | -844887.6883 ppm | 68463.8264 | +7845.9829 ppm | 0.1093 ppm |
| ${}^{74}$Se | 74 | 40 | 103.8233 | 642.8909 | -838505.6159 ppm | 69397.4186 | +7828.6536 ppm | 0.0002 ppm |
| ${}^{75}$Se | 75 | 41 | 109.7830 | 650.9185 | -831341.4729 ppm | 70331.0244 | +7753.7893 ppm | 0.0010 ppm |
| ${}^{76}$Se | 76 | 42 | 115.7295 | 662.0723 | -825201.0569 ppm | 71264.6432 | +7725.6282 ppm | 0.0002 ppm |
| ${}^{77}$Se | 77 | 43 | 121.6634 | 669.4912 | -818274.8238 ppm | 72198.2748 | +7645.8461 ppm | 0.0009 ppm |
| ${}^{78}$Se | 78 | 44 | 127.5849 | 679.9890 | -812372.0880 ppm | 73131.9187 | +7611.0259 ppm | 0.0025 ppm |
| ${}^{79}$Se | 79 | 45 | 133.4944 | 686.9518 | -805671.3588 ppm | 74065.5746 | +7528.7982 ppm | 0.0030 ppm |
| ${}^{80}$Se | 80 | 46 | 139.3922 | 696.8651 | -799972.4308 ppm | 74999.2422 | +7488.7178 ppm | 0.0127 ppm |
| ${}^{81}$Se | 81 | 47 | 145.2787 | 703.5660 | -793510.8737 ppm | 75932.9211 | +7406.8389 ppm | 0.0130 ppm |
| ${}^{82}$Se | 82 | 48 | 151.1542 | 712.8422 | -787955.6209 ppm | 76866.6111 | +7361.1045 ppm | 0.0061 ppm |
| ${}^{83}$Se | 83 | 49 | 157.0189 | 718.6601 | -781511.6170 ppm | 77800.3118 | +7271.5100 ppm | 0.0393 ppm |
| ${}^{84}$Se | 84 | 50 | 162.8732 | 727.3387 | -776069.7016 ppm | 78734.0230 | +7221.0464 ppm | 0.0251 ppm |
| ${}^{85}$Se | 85 | 51 | 168.7173 | 731.8759 | -769472.8544 ppm | 79667.7443 | +7119.1719 ppm | 0.0330 ppm |
| ${}^{86}$Se | 86 | 52 | 174.5514 | 738.0367 | -763492.1919 ppm | 80601.4755 | +7040.2292 ppm | 0.0315 ppm |
| ${}^{87}$Se | 87 | 53 | 180.3760 | 742.0310 | -756915.8322 ppm | 81535.2164 | +6936.2830 ppm | 0.0277 ppm |
| ${}^{88}$Se | 88 | 54 | 186.1911 | 747.5604 | -750935.0044 ppm | 82468.9667 | +6853.6962 ppm | 0.0410 ppm |
| ${}^{89}$Se | 89 | 55 | 191.9971 | 750.7399 | -744256.1714 ppm | 83402.7262 | +6744.5251 ppm | 0.0450 ppm |
| ${}^{90}$Se | 90 | 56 | 197.7941 | 755.6190 | -738235.6411 ppm | 84336.4945 | +6658.3229 ppm | 3.9360 ppm |
| ${}^{91}$Se | 91 | 57 | 203.5825 | 758.4703 | -731588.0873 ppm | 85270.2716 | +6550.0304 ppm | 5.1129 ppm |
| ${}^{92}$Se | 92 | 58 | 209.3623 | 762.6800 | -725491.3226 ppm | 86204.0572 | +6460.2301 ppm | 4.6656 ppm |
| ${}^{93}$Se | 93 | 59 | 215.1338 | 764.9250 | -718751.7686 ppm | 87137.8511 | +6349.1350 ppm | 4.6151 ppm |
| ${}^{94}$Se | 94 | 60 | 220.8972 | 768.9200 | -712717.5359 ppm | 88071.6531 | +6261.2879 ppm | 5.7152 ppm |
| ${}^{95}$Se | 95 | 61 | 226.6528 | 770.6400 | -705890.2250 ppm | 89005.4630 | +6149.3776 ppm | 5.6546 ppm |

### Bromine (Z = 35)

_34 of 34 isotopes with a framework prediction; 34 of 34 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{65}$Br | 65 | 30 | 35.1308 | 513.7600 | -931620.1997 ppm | 61009.2400 | +7906.9637 ppm | 8.2638 ppm |
| ${}^{66}$Br | 66 | 31 | 41.2851 | 528.9240 | -921945.1908 ppm | 61942.6511 | +7934.4164 ppm | 6.5025 ppm |
| ${}^{67}$Br | 67 | 32 | 47.4208 | 545.9160 | -913135.3001 ppm | 62876.0808 | +7991.7419 ppm | 4.8085 ppm |
| ${}^{68}$Br | 68 | 33 | 53.5387 | 560.2520 | -904438.1524 ppm | 63809.5283 | +8004.7068 ppm | 4.0907 ppm |
| ${}^{69}$Br | 69 | 34 | 59.6393 | 575.7983 | -896423.2730 ppm | 64742.9932 | +8036.5084 ppm | 0.6540 ppm |
| ${}^{70}$Br | 70 | 35 | 65.7231 | 589.0357 | -888422.4987 ppm | 65676.4748 | +8032.0449 ppm | 0.2288 ppm |
| ${}^{71}$Br | 71 | 36 | 71.7908 | 602.1839 | -880782.6726 ppm | 66609.9726 | +8026.5890 ppm | 0.0817 ppm |
| ${}^{72}$Br | 72 | 37 | 77.8426 | 612.8145 | -872975.1876 ppm | 67543.4861 | +7983.6478 ppm | 0.0153 ppm |
| ${}^{73}$Br | 73 | 38 | 83.8793 | 625.4699 | -865893.9236 ppm | 68477.0148 | +7972.1452 ppm | 0.0992 ppm |
| ${}^{74}$Br | 74 | 39 | 89.9012 | 635.1836 | -858464.2252 ppm | 69410.5584 | +7918.1107 ppm | 0.0847 ppm |
| ${}^{75}$Br | 75 | 40 | 95.9088 | 647.0737 | -851780.8003 ppm | 70344.1163 | +7897.1513 ppm | 0.0614 ppm |
| ${}^{76}$Br | 76 | 41 | 101.9024 | 656.3271 | -844738.4047 ppm | 71277.6880 | +7839.3616 ppm | 0.1318 ppm |
| ${}^{77}$Br | 77 | 42 | 107.8825 | 667.3442 | -838340.4868 ppm | 72211.2733 | +7808.0671 ppm | 0.0392 ppm |
| ${}^{78}$Br | 78 | 43 | 113.8496 | 675.6328 | -831491.9751 ppm | 73144.8717 | +7739.8718 ppm | 0.0493 ppm |
| ${}^{79}$Br | 79 | 44 | 119.8038 | 686.3201 | -825440.2861 ppm | 74078.4829 | +7706.4561 ppm | 0.0136 ppm |
| ${}^{80}$Br | 80 | 45 | 125.7457 | 694.2123 | -818865.6149 ppm | 75012.1064 | +7636.2081 ppm | 0.0133 ppm |
| ${}^{81}$Br | 81 | 46 | 131.6756 | 704.3717 | -813059.5288 ppm | 75945.7420 | +7598.1621 ppm | 0.0130 ppm |
| ${}^{82}$Br | 82 | 47 | 137.5937 | 711.9646 | -806740.8080 ppm | 76879.3893 | +7527.3088 ppm | 0.0127 ppm |
| ${}^{83}$Br | 83 | 48 | 143.5004 | 721.5510 | -801122.2344 ppm | 77813.0479 | +7484.3151 ppm | 0.0491 ppm |
| ${}^{84}$Br | 84 | 49 | 149.3961 | 728.3917 | -794895.9343 ppm | 78746.7177 | +7407.0996 ppm | 0.3292 ppm |
| ${}^{85}$Br | 85 | 50 | 155.2809 | 737.2554 | -789379.7058 ppm | 79680.3983 | +7357.6050 ppm | 0.0389 ppm |
| ${}^{86}$Br | 86 | 51 | 161.1553 | 742.3835 | -782921.7846 ppm | 80614.0894 | +7262.3759 ppm | 0.0385 ppm |
| ${}^{87}$Br | 87 | 52 | 167.0194 | 748.7142 | -776925.0708 ppm | 81547.7907 | +7184.4315 ppm | 0.0392 ppm |
| ${}^{88}$Br | 88 | 53 | 172.8735 | 753.6098 | -770606.1182 ppm | 82481.5020 | +7090.7379 ppm | 0.0387 ppm |
| ${}^{89}$Br | 89 | 54 | 178.7179 | 759.2394 | -764609.3524 ppm | 83415.2231 | +7008.1994 ppm | 0.0394 ppm |
| ${}^{90}$Br | 90 | 55 | 184.5528 | 763.0368 | -758133.8627 ppm | 84348.9536 | +6905.5905 ppm | 0.0401 ppm |
| ${}^{91}$Br | 91 | 56 | 190.3784 | 768.2151 | -752180.8596 ppm | 85282.6934 | +6821.7721 ppm | 0.0418 ppm |
| ${}^{92}$Br | 92 | 57 | 196.1950 | 771.4119 | -745667.6245 ppm | 86216.4422 | +6716.5951 ppm | 0.0783 ppm |
| ${}^{93}$Br | 93 | 58 | 202.0028 | 776.1407 | -739734.2330 ppm | 87150.1998 | +6631.6063 ppm | 4.9762 ppm |
| ${}^{94}$Br | 94 | 59 | 207.8021 | 778.9780 | -733237.5618 ppm | 88083.9660 | +6526.7011 ppm | 2.2885 ppm |
| ${}^{95}$Br | 95 | 60 | 213.5929 | 783.2750 | -727307.9000 ppm | 89017.7406 | +6440.5098 ppm | 3.3912 ppm |
| ${}^{96}$Br | 96 | 61 | 219.3755 | 785.6640 | -720776.8893 ppm | 89951.5233 | +6335.4908 ppm | 3.3556 ppm |
| ${}^{97}$Br | 97 | 62 | 225.1502 | 789.5800 | -714848.1656 ppm | 90885.3141 | +6248.6795 ppm | 4.4243 ppm |
| ${}^{98}$Br | 98 | 63 | 230.9170 | 791.6440 | -708307.0078 ppm | 91819.1127 | +6144.5391 ppm | 4.3789 ppm |

### Krypton (Z = 36)

_35 of 35 isotopes with a framework prediction; 35 of 35 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{67}$Kr | 67 | 31 | 32.7934 | 528.1610 | -937910.2259 ppm | 62889.9259 | +7939.3506 ppm | 6.7927 ppm |
| ${}^{68}$Kr | 68 | 32 | 38.9672 | 546.3120 | -928672.3122 ppm | 63823.3175 | +8012.9041 ppm | 7.9003 ppm |
| ${}^{69}$Kr | 69 | 33 | 45.1226 | 560.9010 | -919553.3446 ppm | 64756.7275 | +8028.7514 ppm | 4.6690 ppm |
| ${}^{70}$Kr | 70 | 34 | 51.2603 | 577.9200 | -911302.0901 ppm | 65690.1553 | +8082.2611 ppm | 3.0734 ppm |
| ${}^{71}$Kr | 71 | 35 | 57.3808 | 591.2263 | -902946.1462 ppm | 66623.6002 | +8077.5915 ppm | 1.9484 ppm |
| ${}^{72}$Kr | 72 | 36 | 63.4846 | 606.9110 | -895397.1344 ppm | 67557.0618 | +8109.1988 ppm | 0.1195 ppm |
| ${}^{73}$Kr | 73 | 37 | 69.5723 | 617.5935 | -887349.3292 ppm | 68490.5395 | +8065.9609 ppm | 0.0968 ppm |
| ${}^{74}$Kr | 74 | 38 | 75.6444 | 631.4449 | -880204.3443 ppm | 69424.0329 | +8070.5000 ppm | 0.0292 ppm |
| ${}^{75}$Kr | 75 | 39 | 81.7012 | 641.5080 | -872641.9630 ppm | 70357.5415 | +8020.4226 ppm | 0.1161 ppm |
| ${}^{76}$Kr | 76 | 40 | 87.7433 | 654.2694 | -865891.1701 ppm | 71291.0648 | +8010.3261 ppm | 0.0567 ppm |
| ${}^{77}$Kr | 77 | 41 | 93.7711 | 663.4964 | -858671.2967 ppm | 72224.6024 | +7950.9716 ppm | 0.0273 ppm |
| ${}^{78}$Kr | 78 | 42 | 99.7850 | 675.5766 | -852296.5669 ppm | 73158.1540 | +7932.9486 ppm | 0.0042 ppm |
| ${}^{79}$Kr | 79 | 43 | 105.7854 | 683.9119 | -845323.1112 ppm | 74091.7190 | +7864.2204 ppm | 0.0473 ppm |
| ${}^{80}$Kr | 80 | 44 | 111.7726 | 695.4344 | -839276.5341 ppm | 75025.2972 | +7840.5359 ppm | 0.0093 ppm |
| ${}^{81}$Kr | 81 | 45 | 117.7471 | 703.3085 | -832581.1067 ppm | 75958.8881 | +7768.8210 ppm | 0.0142 ppm |
| ${}^{82}$Kr | 82 | 46 | 123.7092 | 714.2754 | -826804.6007 ppm | 76892.4914 | +7739.8665 ppm | 0.0001 ppm |
| ${}^{83}$Kr | 83 | 47 | 129.6592 | 721.7455 | -820353.2826 ppm | 77826.1068 | +7666.1408 ppm | 0.0001 ppm |
| ${}^{84}$Kr | 84 | 48 | 135.5975 | 732.2656 | -814824.7317 ppm | 78759.7340 | +7633.6391 ppm | 0.0000 ppm |
| ${}^{85}$Kr | 85 | 49 | 141.5243 | 739.3779 | -808590.0442 ppm | 79693.3726 | +7558.6348 ppm | 0.0253 ppm |
| ${}^{86}$Kr | 86 | 50 | 147.4400 | 749.2345 | -803212.5442 ppm | 80627.0224 | +7520.0676 ppm | 0.0000 ppm |
| ${}^{87}$Kr | 87 | 51 | 153.3448 | 754.7497 | -796826.9834 ppm | 81560.6830 | +7428.4936 ppm | 0.0030 ppm |
| ${}^{88}$Kr | 88 | 52 | 159.2390 | 761.8028 | -790970.8172 ppm | 82494.3542 | +7358.0553 ppm | 0.0318 ppm |
| ${}^{89}$Kr | 89 | 53 | 165.1229 | 766.7186 | -784636.8346 ppm | 83428.0356 | +7263.3354 ppm | 0.0259 ppm |
| ${}^{90}$Kr | 90 | 54 | 170.9968 | 773.2134 | -778849.1144 ppm | 84361.7272 | +7189.8356 ppm | 0.0222 ppm |
| ${}^{91}$Kr | 91 | 55 | 176.8609 | 777.2994 | -772467.4699 ppm | 85295.4285 | +7089.4284 ppm | 0.0264 ppm |
| ${}^{92}$Kr | 92 | 56 | 182.7154 | 783.1661 | -766696.4636 ppm | 86229.1394 | +7012.2670 ppm | 0.0315 ppm |
| ${}^{93}$Kr | 93 | 57 | 188.5606 | 786.6041 | -760285.2446 ppm | 87162.8597 | +6908.6271 ppm | 0.0291 ppm |
| ${}^{94}$Kr | 94 | 58 | 194.3967 | 791.8872 | -754514.6707 ppm | 88096.5890 | +6828.5395 ppm | 0.1384 ppm |
| ${}^{95}$Kr | 95 | 59 | 200.2239 | 794.7696 | -748073.0698 ppm | 89030.3272 | +6722.9159 ppm | 0.2107 ppm |
| ${}^{96}$Kr | 96 | 60 | 206.0424 | 799.7637 | -742370.9258 ppm | 89964.0742 | +6643.3875 ppm | 0.2157 ppm |
| ${}^{97}$Kr | 97 | 61 | 211.8524 | 802.1769 | -735903.1041 ppm | 90897.8296 | +6536.8321 ppm | 1.4441 ppm |
| ${}^{98}$Kr | 98 | 62 | 217.6542 | 806.9320 | -730269.5088 ppm | 91831.5932 | +6458.5315 ppm | 3.2873 ppm |
| ${}^{99}$Kr | 99 | 63 | 223.4478 | 809.3250 | -723908.4212 ppm | 92765.3650 | +6355.5187 ppm | 4.3351 ppm |
| ${}^{100}$Kr | 100 | 64 | 229.2336 | 813.4000 | -718178.5621 ppm | 93699.1447 | +6274.0119 ppm | 4.2916 ppm |
| ${}^{101}$Kr | 101 | 65 | 235.0116 | 815.5750 | -711845.5526 ppm | 94632.9321 | +6173.2416 ppm | 5.3184 ppm |

### Rubidium (Z = 37)

_34 of 34 isotopes with a framework prediction; 34 of 34 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{71}$Rb | 71 | 34 | 42.6317 | 576.3780 | -926035.2517 ppm | 66637.5670 | +8074.8148 ppm | 6.0452 ppm |
| ${}^{72}$Rb | 72 | 35 | 48.7889 | 590.5440 | -917383.0726 ppm | 67570.9751 | +8081.9904 ppm | 7.4626 ppm |
| ${}^{73}$Rb | 73 | 36 | 54.9291 | 606.2710 | -909398.3961 ppm | 68504.4004 | +8113.5775 ppm | 0.6003 ppm |
| ${}^{74}$Rb | 74 | 37 | 61.0528 | 620.2467 | -901566.9881 ppm | 69437.8422 | +8118.5465 ppm | 0.0439 ppm |
| ${}^{75}$Rb | 75 | 38 | 67.1603 | 633.6207 | -894005.5040 ppm | 70371.3000 | +8114.9238 ppm | 0.0169 ppm |
| ${}^{76}$Rb | 76 | 39 | 73.2523 | 644.9524 | -886422.2143 ppm | 71304.7735 | +8082.5090 ppm | 0.0132 ppm |
| ${}^{77}$Rb | 77 | 40 | 79.3291 | 657.3751 | -879324.4833 ppm | 72238.2621 | +8066.4927 ppm | 0.0182 ppm |
| ${}^{78}$Rb | 78 | 41 | 85.3912 | 667.5514 | -872082.9622 ppm | 73171.7654 | +8019.8914 ppm | 0.0446 ppm |
| ${}^{79}$Rb | 79 | 42 | 91.4390 | 679.4901 | -865429.9396 ppm | 74105.2830 | +7998.8267 ppm | 0.0264 ppm |
| ${}^{80}$Rb | 80 | 43 | 97.4730 | 688.9341 | -858516.2825 ppm | 75038.8145 | +7944.6972 ppm | 0.0250 ppm |
| ${}^{81}$Rb | 81 | 44 | 103.4934 | 700.2866 | -852212.8167 ppm | 75972.3595 | +7917.6028 ppm | 0.0651 ppm |
| ${}^{82}$Rb | 82 | 45 | 109.5007 | 709.0891 | -845575.5474 ppm | 76905.9176 | +7857.6564 ppm | 0.0394 ppm |
| ${}^{83}$Rb | 83 | 46 | 115.4952 | 720.0432 | -839599.6047 ppm | 77839.4885 | +7827.3970 ppm | 0.0302 ppm |
| ${}^{84}$Rb | 84 | 47 | 121.4773 | 728.8028 | -833319.3878 ppm | 78773.0718 | +7769.7218 ppm | 0.0281 ppm |
| ${}^{85}$Rb | 85 | 48 | 127.4473 | 739.2825 | -827606.7879 ppm | 79706.6673 | +7735.4713 ppm | 0.0001 ppm |
| ${}^{86}$Rb | 86 | 49 | 133.4055 | 747.9335 | -821634.5635 ppm | 80640.2745 | +7679.1359 ppm | 0.0025 ppm |
| ${}^{87}$Rb | 87 | 50 | 139.3522 | 757.8556 | -816123.0223 ppm | 81573.8932 | +7640.0594 ppm | 0.0001 ppm |
| ${}^{88}$Rb | 88 | 51 | 145.2877 | 763.9382 | -809817.4205 ppm | 82507.5231 | +7554.7625 ppm | 0.0019 ppm |
| ${}^{89}$Rb | 89 | 52 | 151.2123 | 771.1129 | -803903.7408 ppm | 83441.1639 | +7484.8059 ppm | 0.0655 ppm |
| ${}^{90}$Rb | 90 | 53 | 157.1263 | 776.8374 | -797735.8668 ppm | 84374.8153 | +7399.0904 ppm | 0.0770 ppm |
| ${}^{91}$Rb | 91 | 54 | 163.0300 | 783.2882 | -791864.6522 ppm | 85308.4771 | +7324.0265 ppm | 0.0921 ppm |
| ${}^{92}$Rb | 92 | 55 | 168.9235 | 788.3869 | -785735.3291 ppm | 86242.1491 | +7234.8114 ppm | 0.0715 ppm |
| ${}^{93}$Rb | 93 | 56 | 174.8071 | 794.3056 | -779924.6600 ppm | 87175.8309 | +7157.1785 ppm | 0.0905 ppm |
| ${}^{94}$Rb | 94 | 57 | 180.6811 | 798.3199 | -773673.3192 ppm | 88109.5223 | +7059.3900 ppm | 0.0232 ppm |
| ${}^{95}$Rb | 95 | 58 | 186.5457 | 803.7187 | -767896.8033 ppm | 89043.2231 | +6979.5447 ppm | 0.2289 ppm |
| ${}^{96}$Rb | 96 | 59 | 192.4011 | 807.2540 | -761659.8047 ppm | 89976.9331 | +6880.4746 ppm | 0.0375 ppm |
| ${}^{97}$Rb | 97 | 60 | 198.2475 | 812.4902 | -756000.0876 ppm | 90910.6521 | +6802.5207 ppm | 0.0212 ppm |
| ${}^{98}$Rb | 98 | 61 | 204.0852 | 816.4115 | -750021.6373 ppm | 91844.3799 | +6711.7512 ppm | 0.1763 ppm |
| ${}^{99}$Rb | 99 | 62 | 209.9143 | 821.2348 | -744391.8346 ppm | 92778.1162 | +6632.7688 ppm | 0.0437 ppm |
| ${}^{100}$Rb | 100 | 63 | 215.7351 | 824.4508 | -738328.7727 ppm | 93711.8608 | +6538.0858 ppm | 0.1410 ppm |
| ${}^{101}$Rb | 101 | 64 | 221.5476 | 828.8237 | -732696.3170 ppm | 94645.6137 | +6457.7560 ppm | 0.2179 ppm |
| ${}^{102}$Rb | 102 | 65 | 227.3522 | 831.5799 | -726602.1146 ppm | 95579.3746 | +6361.9622 ppm | 0.8729 ppm |
| ${}^{103}$Rb | 103 | 66 | 233.1489 | 835.5360 | -720958.8475 ppm | 96513.1432 | +6280.9532 ppm | 4.1665 ppm |
| ${}^{104}$Rb | 104 | 67 | 238.9380 | 837.9280 | -714846.6094 ppm | 97446.9196 | +6184.7781 ppm | 5.1649 ppm |

### Strontium (Z = 38)

_35 of 35 isotopes with a framework prediction; 35 of 35 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{73}$Sr | 73 | 35 | 39.9497 | 591.4460 | -932454.1517 ppm | 68518.5974 | +8113.8956 ppm | 5.8932 ppm |
| ${}^{74}$Sr | 74 | 36 | 46.1264 | 608.3540 | -924178.3746 ppm | 69451.9862 | +8161.5917 ppm | 1.4468 ppm |
| ${}^{75}$Sr | 75 | 37 | 52.2861 | 622.2384 | -915970.9820 ppm | 70385.3919 | +8163.7078 ppm | 3.1512 ppm |
| ${}^{76}$Sr | 76 | 38 | 58.4293 | 637.9386 | -908409.2260 ppm | 71318.8141 | +8192.1910 ppm | 0.4872 ppm |
| ${}^{77}$Sr | 77 | 39 | 64.5565 | 649.5657 | -900615.8934 ppm | 72252.2523 | +8162.8617 ppm | 0.1105 ppm |
| ${}^{78}$Sr | 78 | 40 | 70.6682 | 663.0076 | -893412.6893 ppm | 73185.7061 | +8159.6979 ppm | 0.1027 ppm |
| ${}^{79}$Sr | 79 | 41 | 76.7648 | 673.3846 | -886001.5772 ppm | 74119.1749 | +8114.7939 ppm | 0.1009 ppm |
| ${}^{80}$Sr | 80 | 42 | 82.8467 | 686.2877 | -879282.8445 ppm | 75052.6584 | +8105.4121 ppm | 0.0465 ppm |
| ${}^{81}$Sr | 81 | 43 | 88.9144 | 695.5757 | -872171.5597 ppm | 75986.1562 | +8048.1027 ppm | 0.0415 ppm |
| ${}^{82}$Sr | 82 | 44 | 94.9681 | 708.1290 | -865888.6320 ppm | 76919.6678 | +8035.5058 ppm | 0.0785 ppm |
| ${}^{83}$Sr | 83 | 45 | 101.0084 | 716.9878 | -859121.1348 ppm | 77853.1930 | +7975.1707 ppm | 0.0885 ppm |
| ${}^{84}$Sr | 84 | 46 | 107.0356 | 728.9111 | -853156.8733 ppm | 78786.7312 | +7955.9552 ppm | 0.0159 ppm |
| ${}^{85}$Sr | 85 | 47 | 113.0500 | 737.4361 | -846698.6526 ppm | 79720.2823 | +7894.0474 ppm | 0.0356 ppm |
| ${}^{86}$Sr | 86 | 48 | 119.0519 | 748.9273 | -841036.8071 ppm | 80653.8458 | +7871.0912 ppm | 0.0001 ppm |
| ${}^{87}$Sr | 87 | 49 | 125.0417 | 757.3556 | -834897.0249 ppm | 81587.4214 | +7810.6804 ppm | 0.0001 ppm |
| ${}^{88}$Sr | 88 | 50 | 131.0196 | 768.4684 | -829505.5233 ppm | 82521.0089 | +7784.8274 ppm | 0.0001 ppm |
| ${}^{89}$Sr | 89 | 51 | 136.9861 | 774.8271 | -823204.3488 ppm | 83454.6078 | +7701.8420 ppm | 0.0011 ppm |
| ${}^{90}$Sr | 90 | 52 | 142.9413 | 782.6404 | -817360.1974 ppm | 84388.2181 | +7638.3401 ppm | 0.0173 ppm |
| ${}^{91}$Sr | 91 | 53 | 148.8855 | 788.4127 | -811157.8528 ppm | 85321.8392 | +7552.0816 ppm | 0.0644 ppm |
| ${}^{92}$Sr | 92 | 54 | 154.8191 | 795.6994 | -805430.1437 ppm | 86255.4711 | +7485.6504 ppm | 0.0400 ppm |
| ${}^{93}$Sr | 93 | 55 | 160.7423 | 800.9892 | -799320.3010 ppm | 87189.1133 | +7397.5265 ppm | 0.0873 ppm |
| ${}^{94}$Sr | 94 | 56 | 166.6553 | 807.8204 | -793697.6467 ppm | 88122.7658 | +7329.1498 ppm | 0.0190 ppm |
| ${}^{95}$Sr | 95 | 57 | 172.5583 | 812.1633 | -787532.5100 ppm | 89056.4282 | +7233.9807 ppm | 0.0657 ppm |
| ${}^{96}$Sr | 96 | 58 | 178.4516 | 818.0356 | -781853.4475 ppm | 89990.1002 | +7158.1515 ppm | 0.0948 ppm |
| ${}^{97}$Sr | 97 | 59 | 184.3355 | 821.7693 | -775684.6052 ppm | 90923.7818 | +7060.1416 ppm | 0.0375 ppm |
| ${}^{98}$Sr | 98 | 60 | 190.2101 | 827.6824 | -770189.4648 ppm | 91857.4726 | +6988.3010 ppm | 0.0354 ppm |
| ${}^{99}$Sr | 99 | 61 | 196.0757 | 831.8498 | -764289.5475 ppm | 92791.1724 | +6898.9416 ppm | 0.0514 ppm |
| ${}^{100}$Sr | 100 | 62 | 201.9324 | 837.2201 | -758806.0486 ppm | 93724.8811 | +6824.4822 ppm | 0.0743 ppm |
| ${}^{101}$Sr | 101 | 63 | 207.7805 | 840.7989 | -752877.2591 ppm | 94658.5985 | +6732.4117 ppm | 0.0902 ppm |
| ${}^{102}$Sr | 102 | 64 | 213.6202 | 845.7046 | -747405.7010 ppm | 95592.3243 | +6656.3121 ppm | 0.7063 ppm |
| ${}^{103}$Sr | 103 | 65 | 219.4515 | 848.9260 | -741495.1061 ppm | 96526.0583 | +6563.7926 ppm | 2.0884 ppm |
| ${}^{104}$Sr | 104 | 66 | 225.2748 | 853.4240 | -736034.1260 ppm | 97459.8004 | +6487.2750 ppm | 3.0976 ppm |
| ${}^{105}$Sr | 105 | 67 | 231.0902 | 855.9600 | -730022.2121 ppm | 98393.5505 | +6391.2069 ppm | 5.1163 ppm |
| ${}^{106}$Sr | 106 | 68 | 236.8978 | 860.0840 | -724564.3211 ppm | 99327.3083 | +6314.1638 ppm | 6.0776 ppm |
| ${}^{107}$Sr | 107 | 69 | 242.6979 | 862.0990 | -718480.2732 ppm | 100261.0737 | +6216.8290 ppm | 7.0207 ppm |

### Yttrium (Z = 39)

_35 of 35 isotopes with a framework prediction; 35 of 35 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{75}$Y | 75 | 36 | 37.0785 | 606.6750 | -938882.4144 ppm | 70399.8172 | +8156.6271 ppm | 4.2953 ppm |
| ${}^{76}$Y | 76 | 37 | 43.2744 | 621.1480 | -930331.6167 ppm | 71333.1867 | +8167.3706 ppm | 4.2391 ppm |
| ${}^{77}$Y | 77 | 38 | 49.4534 | 637.4060 | -922414.6465 ppm | 72266.5731 | +8202.8081 ppm | 2.8330 ppm |
| ${}^{78}$Y | 78 | 39 | 55.6160 | 651.2220 | -914597.5172 ppm | 73199.9760 | +8203.4852 ppm | 4.1055 ppm |
| ${}^{79}$Y | 79 | 40 | 61.7627 | 664.9255 | -907113.4164 ppm | 74133.3947 | +8202.9313 ppm | 1.0895 ppm |
| ${}^{80}$Y | 80 | 41 | 67.8939 | 676.3421 | -899616.0759 ppm | 75066.8289 | +8171.6628 ppm | 0.0838 ppm |
| ${}^{81}$Y | 81 | 42 | 74.0100 | 688.9782 | -892579.9931 ppm | 76000.2782 | +8157.6727 ppm | 0.0717 ppm |
| ${}^{82}$Y | 82 | 43 | 80.1116 | 699.4006 | -885456.8228 ppm | 76933.7421 | +8114.9720 ppm | 0.0720 ppm |
| ${}^{83}$Y | 83 | 44 | 86.1989 | 711.6135 | -878868.4207 ppm | 77867.2202 | +8096.8491 ppm | 0.2412 ppm |
| ${}^{84}$Y | 84 | 45 | 92.2723 | 721.3736 | -872088.0348 ppm | 78800.7122 | +8047.7027 ppm | 0.0550 ppm |
| ${}^{85}$Y | 85 | 46 | 98.3323 | 733.3926 | -865921.3742 ppm | 79734.2176 | +8028.6688 ppm | 0.2398 ppm |
| ${}^{86}$Y | 86 | 47 | 104.3791 | 742.9049 | -859498.7081 ppm | 80667.7362 | +7978.6668 ppm | 0.1767 ppm |
| ${}^{87}$Y | 87 | 48 | 110.4131 | 754.7115 | -853701.5422 ppm | 81601.2676 | +7958.5363 ppm | 0.0139 ppm |
| ${}^{88}$Y | 88 | 49 | 116.4347 | 764.0635 | -847611.2272 ppm | 82534.8115 | +7908.8003 ppm | 0.0183 ppm |
| ${}^{89}$Y | 89 | 50 | 122.4441 | 775.5470 | -842119.0278 ppm | 83468.3675 | +7886.2690 ppm | 0.0041 ppm |
| ${}^{90}$Y | 90 | 51 | 128.4417 | 782.4040 | -835837.1395 ppm | 84401.9353 | +7808.7014 ppm | 0.0042 ppm |
| ${}^{91}$Y | 91 | 52 | 134.4277 | 790.3297 | -829909.3540 ppm | 85335.5147 | +7745.6970 ppm | 0.0218 ppm |
| ${}^{92}$Y | 92 | 53 | 140.4024 | 796.8662 | -823806.7618 ppm | 86269.1054 | +7667.8439 ppm | 0.1066 ppm |
| ${}^{93}$Y | 93 | 54 | 146.3662 | 804.3482 | -818031.3075 ppm | 87202.7071 | +7602.8042 ppm | 0.1212 ppm |
| ${}^{94}$Y | 94 | 55 | 152.3192 | 810.5438 | -812077.7662 ppm | 88136.3195 | +7524.4576 ppm | 0.0729 ppm |
| ${}^{95}$Y | 95 | 56 | 158.2618 | 817.4716 | -806400.9237 ppm | 89069.9424 | +7456.2267 ppm | 0.0767 ppm |
| ${}^{96}$Y | 96 | 57 | 164.1941 | 822.6650 | -800411.9971 ppm | 90003.5755 | +7369.9787 ppm | 0.0680 ppm |
| ${}^{97}$Y | 97 | 58 | 170.1164 | 828.5218 | -794674.8240 ppm | 90937.2186 | +7293.0288 ppm | 0.0743 ppm |
| ${}^{98}$Y | 98 | 59 | 176.0289 | 832.7664 | -788621.4688 ppm | 91870.8715 | +7199.9592 ppm | 0.0868 ppm |
| ${}^{99}$Y | 99 | 60 | 181.9320 | 839.1927 | -783205.9832 ppm | 92804.5339 | +7132.7268 ppm | 0.0718 ppm |
| ${}^{100}$Y | 100 | 61 | 187.8256 | 843.9415 | -777442.3405 ppm | 93738.2056 | +7048.7939 ppm | 0.1201 ppm |
| ${}^{101}$Y | 101 | 62 | 193.7102 | 849.7464 | -772037.5975 ppm | 94671.8864 | +6977.9377 ppm | 0.0753 ppm |
| ${}^{102}$Y | 102 | 63 | 199.5859 | 853.9356 | -766275.2279 ppm | 95605.5762 | +6891.4355 ppm | 0.0430 ppm |
| ${}^{103}$Y | 103 | 64 | 205.4528 | 859.2913 | -760904.3038 ppm | 96539.2747 | +6818.9606 ppm | 0.1169 ppm |
| ${}^{104}$Y | 104 | 65 | 211.3113 | 862.9920 | -755141.1088 ppm | 97472.9817 | +6730.6944 ppm | 2.0685 ppm |
| ${}^{105}$Y | 105 | 66 | 217.1613 | 867.5100 | -749672.8077 ppm | 98406.6970 | +6653.1357 ppm | 4.0878 ppm |
| ${}^{106}$Y | 106 | 67 | 223.0033 | 870.7900 | -743906.9632 ppm | 99340.4205 | +6564.1802 ppm | 5.0684 ppm |
| ${}^{107}$Y | 107 | 68 | 228.8372 | 875.0460 | -738485.5474 ppm | 100274.1520 | +6486.6695 ppm | 5.0208 ppm |
| ${}^{108}$Y | 108 | 69 | 234.6633 | 877.9320 | -732709.0586 ppm | 101207.8913 | +6396.9657 ppm | 5.9651 ppm |
| ${}^{109}$Y | 109 | 70 | 240.4817 | 881.7010 | -727252.5457 ppm | 102141.6383 | +6317.8218 ppm | 6.8921 ppm |

### Zirconium (Z = 40)

_37 of 37 isotopes with a framework prediction; 37 of 37 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{77}$Zr | 77 | 37 | 34.0197 | 621.7750 | -945286.2194 ppm | 72281.2245 | +8198.4975 ppm | 5.5739 ppm |
| ${}^{78}$Zr | 78 | 38 | 40.2345 | 639.1320 | -937048.1511 ppm | 73214.5751 | +8247.3183 ppm | 5.5031 ppm |
| ${}^{79}$Zr | 79 | 39 | 46.4327 | 653.0930 | -928903.4627 ppm | 74147.9424 | +8249.4978 ppm | 4.0785 ppm |
| ${}^{80}$Zr | 80 | 40 | 52.6145 | 669.2000 | -921377.0752 ppm | 75081.3260 | +8279.8543 ppm | 4.0280 ppm |
| ${}^{81}$Zr | 81 | 41 | 58.7804 | 680.0073 | -913559.1270 ppm | 76014.7254 | +8239.8015 ppm | 1.2232 ppm |
| ${}^{82}$Zr | 82 | 42 | 64.9310 | 694.1683 | -906462.1934 ppm | 76948.1403 | +8244.8496 ppm | 0.0207 ppm |
| ${}^{83}$Zr | 83 | 43 | 71.0665 | 704.5372 | -899130.1858 ppm | 77881.5702 | +8200.4766 ppm | 0.0832 ppm |
| ${}^{84}$Zr | 84 | 44 | 77.1875 | 718.1185 | -892514.2637 ppm | 78815.0146 | +8198.7737 ppm | 0.0703 ppm |
| ${}^{85}$Zr | 85 | 45 | 83.2943 | 727.9433 | -885575.9068 ppm | 79748.4733 | +8149.4124 ppm | 0.0813 ppm |
| ${}^{86}$Zr | 86 | 46 | 89.3872 | 740.8085 | -879338.3407 ppm | 80681.9458 | +8139.6681 ppm | 0.0445 ppm |
| ${}^{87}$Zr | 87 | 47 | 95.4666 | 750.2579 | -872754.9199 ppm | 81615.4318 | +8087.7807 ppm | 0.0512 ppm |
| ${}^{88}$Zr | 88 | 48 | 101.5330 | 762.6110 | -866861.4106 ppm | 82548.9309 | +8072.9755 ppm | 0.0660 ppm |
| ${}^{89}$Zr | 89 | 49 | 107.5865 | 771.9314 | -860626.9009 ppm | 83482.4428 | +8021.7434 ppm | 0.0336 ppm |
| ${}^{90}$Zr | 90 | 50 | 113.6275 | 783.8973 | -855047.9560 ppm | 84415.9672 | +8003.6396 ppm | 0.0014 ppm |
| ${}^{91}$Zr | 91 | 51 | 119.6564 | 791.0917 | -848745.2257 ppm | 85349.5037 | +7929.2771 ppm | 0.0011 ppm |
| ${}^{92}$Zr | 92 | 52 | 125.6734 | 799.7264 | -842854.5126 ppm | 86283.0521 | +7873.6303 ppm | 0.0011 ppm |
| ${}^{93}$Zr | 93 | 53 | 131.6788 | 806.4607 | -836720.1089 ppm | 87216.6121 | +7797.1832 ppm | 0.0053 ppm |
| ${}^{94}$Zr | 94 | 54 | 137.6729 | 814.6794 | -831009.6608 ppm | 88150.1834 | +7739.5956 ppm | 0.0019 ppm |
| ${}^{95}$Zr | 95 | 55 | 143.6560 | 821.1413 | -825053.2167 ppm | 89083.7658 | +7663.3227 ppm | 0.0098 ppm |
| ${}^{96}$Zr | 96 | 56 | 149.6283 | 828.9915 | -819505.5890 ppm | 90017.3589 | +7604.4216 ppm | 0.0013 ppm |
| ${}^{97}$Zr | 97 | 57 | 155.5901 | 834.5607 | -813566.4333 ppm | 90950.9625 | +7521.3932 ppm | 0.0013 ppm |
| ${}^{98}$Zr | 98 | 58 | 161.5416 | 840.9770 | -807911.9674 ppm | 91884.5764 | +7449.5365 ppm | 0.0926 ppm |
| ${}^{99}$Zr | 99 | 59 | 167.4831 | 845.3833 | -801885.0289 ppm | 92818.2004 | +7357.2671 ppm | 0.1139 ppm |
| ${}^{100}$Zr | 100 | 60 | 173.4147 | 852.2107 | -796511.9086 ppm | 93751.8342 | +7293.1599 ppm | 0.0875 ppm |
| ${}^{101}$Zr | 101 | 61 | 179.3368 | 857.0702 | -790756.0534 ppm | 94685.4776 | +7209.3431 ppm | 0.0886 ppm |
| ${}^{102}$Zr | 102 | 62 | 185.2494 | 863.5620 | -785482.2105 ppm | 95619.1303 | +7144.5897 ppm | 0.0922 ppm |
| ${}^{103}$Zr | 103 | 63 | 191.1529 | 867.8609 | -779742.4855 ppm | 96552.7923 | +7058.1586 ppm | 0.0962 ppm |
| ${}^{104}$Zr | 104 | 64 | 197.0474 | 873.8409 | -774504.2864 ppm | 97486.4632 | +6990.9763 ppm | 0.0962 ppm |
| ${}^{105}$Zr | 105 | 65 | 202.9331 | 877.6528 | -768777.5051 ppm | 98420.1429 | +6902.8330 ppm | 0.1239 ppm |
| ${}^{106}$Zr | 106 | 66 | 208.8102 | 882.9800 | -763516.5364 ppm | 99353.8313 | +6832.2676 ppm | 2.0295 ppm |
| ${}^{107}$Zr | 107 | 67 | 214.6789 | 886.3880 | -757804.8758 ppm | 100287.5280 | +6742.6926 ppm | 3.0110 ppm |
| ${}^{108}$Zr | 108 | 68 | 220.5393 | 891.3240 | -752571.1264 ppm | 101221.2330 | +6671.4765 ppm | 3.9742 ppm |
| ${}^{109}$Zr | 109 | 69 | 226.3917 | 894.2360 | -746832.3074 ppm | 102154.9460 | +6580.3279 ppm | 4.9288 ppm |
| ${}^{110}$Zr | 110 | 70 | 232.2361 | 898.8100 | -741618.2150 ppm | 103088.6670 | +6507.7298 ppm | 4.8838 ppm |
| ${}^{111}$Zr | 111 | 71 | 238.0729 | 901.0980 | -735796.9311 ppm | 104022.3957 | +6414.8061 ppm | 5.8038 ppm |
| ${}^{112}$Zr | 112 | 72 | 243.9020 | 905.0720 | -730516.4717 ppm | 104956.1320 | +6339.8302 ppm | 6.7074 ppm |
| ${}^{113}$Zr | 113 | 73 | 249.7237 | 907.0510 | -724686.1521 ppm | 105889.8757 | +6246.9472 ppm | 2.8503 ppm |

### Niobium (Z = 41)

_38 of 38 isotopes with a framework prediction; 38 of 38 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{79}$Nb | 79 | 38 | 30.7748 | 637.2140 | -951704.2083 ppm | 74162.8179 | +8244.4788 ppm | 6.8004 ppm |
| ${}^{80}$Nb | 80 | 39 | 37.0085 | 652.0800 | -943245.5027 ppm | 75096.1496 | +8257.6879 ppm | 5.3653 ppm |
| ${}^{81}$Nb | 81 | 40 | 43.2255 | 668.0880 | -935299.6603 ppm | 76029.4980 | +8286.4382 ppm | 5.2996 ppm |
| ${}^{82}$Nb | 82 | 41 | 49.4264 | 681.5840 | -927483.1043 ppm | 76962.8626 | +8281.8020 ppm | 3.9295 ppm |
| ${}^{83}$Nb | 83 | 42 | 55.6114 | 695.4561 | -920036.0457 ppm | 77896.2430 | +8282.1007 ppm | 2.0979 ppm |
| ${}^{84}$Nb | 84 | 43 | 61.7811 | 707.1083 | -912628.4793 ppm | 78829.6387 | +8253.9297 ppm | 0.0051 ppm |
| ${}^{85}$Nb | 85 | 44 | 67.9359 | 720.2655 | -905679.3656 ppm | 79763.0493 | +8245.7877 ppm | 0.0518 ppm |
| ${}^{86}$Nb | 86 | 45 | 74.0761 | 731.1912 | -898691.1823 ppm | 80696.4745 | +8209.9068 ppm | 0.0687 ppm |
| ${}^{87}$Nb | 87 | 46 | 80.2022 | 744.0029 | -892201.8294 ppm | 81629.9139 | +8198.5088 ppm | 0.0840 ppm |
| ${}^{88}$Nb | 88 | 47 | 86.3144 | 754.3713 | -885581.0359 ppm | 82563.3671 | +8157.4579 ppm | 0.7059 ppm |
| ${}^{89}$Nb | 89 | 48 | 92.4132 | 766.8968 | -879497.2853 ppm | 83496.8338 | +8143.7474 ppm | 0.2853 ppm |
| ${}^{90}$Nb | 90 | 49 | 98.4988 | 777.0039 | -873232.5685 ppm | 84430.3135 | +8101.3862 ppm | 0.0396 ppm |
| ${}^{91}$Nb | 91 | 50 | 104.5716 | 789.0517 | -867471.7657 ppm | 85363.8061 | +8083.2094 ppm | 0.0345 ppm |
| ${}^{92}$Nb | 92 | 51 | 110.6320 | 796.9383 | -861178.7292 ppm | 86297.3112 | +8016.5739 ppm | 0.0208 ppm |
| ${}^{93}$Nb | 93 | 52 | 116.6802 | 805.7692 | -855194.0609 ppm | 87230.8284 | +7962.5120 ppm | 0.0172 ppm |
| ${}^{94}$Nb | 94 | 53 | 122.7164 | 812.9967 | -849056.6513 ppm | 88164.3576 | +7891.2624 ppm | 0.0170 ppm |
| ${}^{95}$Nb | 95 | 54 | 128.7411 | 821.4853 | -843282.4889 ppm | 89097.8983 | +7836.0222 ppm | 0.0057 ppm |
| ${}^{96}$Nb | 96 | 55 | 134.7545 | 828.3731 | -837326.3651 ppm | 90031.4504 | +7764.0040 ppm | 0.0016 ppm |
| ${}^{97}$Nb | 97 | 56 | 140.7567 | 836.4444 | -831720.1516 ppm | 90965.0136 | +7706.8073 ppm | 0.0470 ppm |
| ${}^{98}$Nb | 98 | 57 | 146.7482 | 842.4376 | -825805.2511 ppm | 91898.5875 | +7627.9371 ppm | 0.0548 ppm |
| ${}^{99}$Nb | 99 | 58 | 152.7291 | 849.3196 | -820174.7756 ppm | 92832.1721 | +7560.5008 ppm | 0.1303 ppm |
| ${}^{100}$Nb | 100 | 59 | 158.6996 | 854.8468 | -814353.1174 ppm | 93765.7669 | +7479.8608 ppm | 0.0857 ppm |
| ${}^{101}$Nb | 101 | 60 | 164.6601 | 862.0184 | -808983.0623 ppm | 94699.3719 | +7418.5527 ppm | 0.0399 ppm |
| ${}^{102}$Nb | 102 | 61 | 170.6107 | 867.4965 | -803329.8065 ppm | 95632.9867 | +7340.5838 ppm | 0.0264 ppm |
| ${}^{103}$Nb | 103 | 62 | 176.5516 | 874.2982 | -798064.7393 ppm | 96566.6112 | +7278.1418 ppm | 0.0410 ppm |
| ${}^{104}$Nb | 104 | 63 | 182.4831 | 879.1519 | -792432.7641 ppm | 97500.2451 | +7196.7315 ppm | 0.0184 ppm |
| ${}^{105}$Nb | 105 | 64 | 188.4054 | 885.3277 | -787191.3867 ppm | 98433.8883 | +7130.5976 ppm | 0.0412 ppm |
| ${}^{106}$Nb | 106 | 65 | 194.3186 | 889.6862 | -781587.5217 ppm | 99367.5405 | +7047.2577 ppm | 0.0143 ppm |
| ${}^{107}$Nb | 107 | 66 | 200.2229 | 895.2786 | -776356.8781 ppm | 100301.2016 | +6978.0467 ppm | 0.0805 ppm |
| ${}^{108}$Nb | 108 | 67 | 206.1186 | 899.1713 | -770768.2927 ppm | 101234.8714 | +6893.1852 ppm | 0.0819 ppm |
| ${}^{109}$Nb | 109 | 68 | 212.0058 | 904.3872 | -765580.7680 ppm | 102168.5496 | +6823.1006 ppm | 4.2455 ppm |
| ${}^{110}$Nb | 110 | 69 | 217.8846 | 908.0787 | -760059.7371 ppm | 103102.2362 | +6739.3898 ppm | 8.1860 ppm |
| ${}^{111}$Nb | 111 | 70 | 223.7554 | 912.7530 | -754856.6091 ppm | 104035.9309 | +6667.3088 ppm | 2.9023 ppm |
| ${}^{112}$Nb | 112 | 71 | 229.6181 | 915.9360 | -749307.6857 ppm | 104969.6335 | +6581.7252 ppm | 2.8762 ppm |
| ${}^{113}$Nb | 113 | 72 | 235.4730 | 920.1590 | -744095.2631 ppm | 105903.3440 | +6507.5941 ppm | 3.7979 ppm |
| ${}^{114}$Nb | 114 | 73 | 241.3203 | 923.0580 | -738564.2996 ppm | 106837.0622 | +6421.6654 ppm | 4.7121 ppm |
| ${}^{115}$Nb | 115 | 74 | 247.1601 | 927.0150 | -733380.7214 ppm | 107770.7878 | +6348.3041 ppm | 4.6709 ppm |
| ${}^{116}$Nb | 116 | 75 | 252.9925 | 929.3920 | -727787.1329 ppm | 108704.5209 | +6261.6613 ppm | 2.7765 ppm |

### Molybdenum (Z = 42)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{81}$Mo | 81 | 39 | 27.3453 | 652.3740 | -958083.3628 ppm | 76044.5959 | +8287.4222 ppm | 6.6324 ppm |
| ${}^{82}$Mo | 82 | 40 | 33.5977 | 669.3660 | -949806.6677 ppm | 76977.9089 | +8327.8040 ppm | 5.2345 ppm |
| ${}^{83}$Mo | 83 | 41 | 39.8335 | 683.4220 | -941714.6004 ppm | 77911.2385 | +8329.0706 ppm | 5.1838 ppm |
| ${}^{84}$Mo | 84 | 42 | 46.0532 | 699.3000 | -934143.8419 ppm | 78844.5843 | +8354.5019 ppm | 3.8122 ppm |
| ${}^{85}$Mo | 85 | 43 | 52.2572 | 710.7132 | -926472.1733 ppm | 79777.9457 | +8322.3065 ppm | 0.2001 ppm |
| ${}^{86}$Mo | 86 | 44 | 58.4459 | 725.3857 | -919427.8346 ppm | 80711.3224 | +8332.1328 ppm | 0.0366 ppm |
| ${}^{87}$Mo | 87 | 45 | 64.6197 | 736.2309 | -912229.0280 ppm | 81644.7140 | +8294.2583 ppm | 0.0353 ppm |
| ${}^{88}$Mo | 88 | 46 | 70.7790 | 750.1040 | -905641.0828 ppm | 82578.1202 | +8294.6958 ppm | 0.0466 ppm |
| ${}^{89}$Mo | 89 | 47 | 76.9241 | 760.5037 | -898851.0479 ppm | 83511.5404 | +8253.0119 ppm | 0.0472 ppm |
| ${}^{90}$Mo | 90 | 48 | 83.0555 | 773.7326 | -892656.0463 ppm | 84444.9745 | +8246.4745 ppm | 0.0413 ppm |
| ${}^{91}$Mo | 91 | 49 | 89.1734 | 783.8402 | -886235.1940 ppm | 85378.4220 | +8203.0774 ppm | 0.0737 ppm |
| ${}^{92}$Mo | 92 | 50 | 95.2782 | 796.5113 | -880380.5658 ppm | 86311.8826 | +8190.9631 ppm | 0.0018 ppm |
| ${}^{93}$Mo | 93 | 51 | 101.3702 | 804.5811 | -874008.6861 ppm | 87245.3560 | +8125.6535 ppm | 0.0021 ppm |
| ${}^{94}$Mo | 94 | 52 | 107.4497 | 814.2594 | -868039.9191 ppm | 88178.8420 | +8080.4147 ppm | 0.0016 ppm |
| ${}^{95}$Mo | 95 | 53 | 113.5171 | 821.6285 | -861838.9575 ppm | 89112.3401 | +8009.9346 ppm | 0.0014 ppm |
| ${}^{96}$Mo | 96 | 54 | 119.5725 | 830.7828 | -856072.5462 ppm | 90045.8501 | +7961.2010 ppm | 0.0013 ppm |
| ${}^{97}$Mo | 97 | 55 | 125.6162 | 837.6040 | -850029.0821 ppm | 90979.3717 | +7887.5485 ppm | 0.0018 ppm |
| ${}^{98}$Mo | 98 | 56 | 131.6487 | 846.2466 | -844432.2742 ppm | 91912.9047 | +7835.6559 ppm | 0.0019 ppm |
| ${}^{99}$Mo | 99 | 57 | 137.6700 | 852.1720 | -838448.1471 ppm | 92846.4488 | +7755.2110 ppm | 0.0025 ppm |
| ${}^{100}$Mo | 100 | 58 | 143.6804 | 860.4663 | -833020.2596 ppm | 93780.0038 | +7702.1457 ppm | 0.0032 ppm |
| ${}^{101}$Mo | 101 | 59 | 149.6803 | 865.8645 | -827131.9736 ppm | 94713.5694 | +7619.1997 ppm | 0.0033 ppm |
| ${}^{102}$Mo | 102 | 60 | 155.6698 | 873.9767 | -821883.3931 ppm | 95647.1453 | +7566.8007 ppm | 0.0875 ppm |
| ${}^{103}$Mo | 103 | 61 | 161.6491 | 879.4415 | -816191.1788 ppm | 96580.7314 | +7487.7012 ppm | 0.0962 ppm |
| ${}^{104}$Mo | 104 | 62 | 167.6185 | 886.9023 | -811006.7681 ppm | 97514.3274 | +7431.0041 ppm | 0.0921 ppm |
| ${}^{105}$Mo | 105 | 63 | 173.5782 | 891.9606 | -805396.9818 ppm | 98447.9331 | +7350.7247 ppm | 0.0927 ppm |
| ${}^{106}$Mo | 106 | 64 | 179.5284 | 898.8291 | -800264.1201 ppm | 99381.5483 | +7290.5429 ppm | 0.0925 ppm |
| ${}^{107}$Mo | 107 | 65 | 185.4693 | 903.3174 | -794679.7850 ppm | 100315.1729 | +7207.5103 ppm | 0.0926 ppm |
| ${}^{108}$Mo | 108 | 66 | 191.4011 | 909.5931 | -789574.9993 ppm | 101248.8065 | +7144.0187 ppm | 0.0917 ppm |
| ${}^{109}$Mo | 109 | 67 | 197.3240 | 913.5744 | -784008.8281 ppm | 102182.4490 | +7059.0111 ppm | 0.1102 ppm |
| ${}^{110}$Mo | 110 | 68 | 203.2381 | 919.5222 | -778974.1921 ppm | 103116.1003 | +6994.9806 ppm | 0.2365 ppm |
| ${}^{111}$Mo | 111 | 69 | 209.1437 | 922.9975 | -773408.1381 ppm | 104049.7602 | +6908.0969 ppm | 0.1217 ppm |
| ${}^{112}$Mo | 112 | 70 | 215.0409 | 928.5920 | -768422.5806 ppm | 104983.4284 | +6843.4777 ppm | 1.9207 ppm |
| ${}^{113}$Mo | 113 | 71 | 220.9299 | 931.7980 | -762899.3278 ppm | 105917.1048 | +6757.4068 ppm | 2.8510 ppm |
| ${}^{114}$Mo | 114 | 72 | 226.8109 | 936.9660 | -757930.5172 ppm | 106850.7893 | +6690.5731 ppm | 2.8259 ppm |
| ${}^{115}$Mo | 115 | 73 | 232.6839 | 939.8950 | -752436.2547 ppm | 107784.4816 | +6604.6635 ppm | 3.7320 ppm |
| ${}^{116}$Mo | 116 | 74 | 238.5492 | 944.5880 | -747456.8375 ppm | 108718.1818 | +6537.0076 ppm | 4.6311 ppm |
| ${}^{117}$Mo | 117 | 75 | 244.4070 | 947.2320 | -741977.7118 ppm | 109651.8895 | +6450.4291 ppm | 4.5912 ppm |
| ${}^{118}$Mo | 118 | 76 | 250.2573 | 951.9060 | -737098.7742 ppm | 110585.6046 | +6385.5623 ppm | 4.5522 ppm |
| ${}^{119}$Mo | 119 | 77 | 256.1002 | 954.2610 | -731624.5332 ppm | 111519.3270 | +6299.4152 ppm | 2.7065 ppm |

### Technetium (Z = 43)

_40 of 40 isotopes with a framework prediction; 40 of 40 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{83}$Tc | 83 | 40 | 23.7329 | 667.5690 | -964448.8393 ppm | 77926.5569 | +8331.3077 ppm | 6.4725 ppm |
| ${}^{84}$Tc | 84 | 41 | 30.0037 | 682.0800 | -956011.4023 ppm | 78859.8514 | +8337.3654 ppm | 5.1096 ppm |
| ${}^{85}$Tc | 85 | 42 | 36.2582 | 698.2750 | -948074.6728 ppm | 79793.1624 | +8366.0303 ppm | 5.0500 ppm |
| ${}^{86}$Tc | 86 | 43 | 42.4965 | 712.0800 | -940320.5683 ppm | 80726.4894 | +8363.6345 ppm | 3.7466 ppm |
| ${}^{87}$Tc | 87 | 44 | 48.7193 | 726.2538 | -932917.0136 ppm | 81659.8321 | +8366.4601 ppm | 0.0518 ppm |
| ${}^{88}$Tc | 88 | 45 | 54.9268 | 738.3054 | -925604.2371 ppm | 82593.1900 | +8343.0691 ppm | 0.0500 ppm |
| ${}^{89}$Tc | 89 | 46 | 61.1195 | 752.1012 | -918735.0531 ppm | 83526.5628 | +8341.6136 ppm | 0.0461 ppm |
| ${}^{90}$Tc | 90 | 47 | 67.2977 | 763.5024 | -911856.6294 ppm | 84459.9500 | +8311.5357 ppm | 0.0122 ppm |
| ${}^{91}$Tc | 91 | 48 | 73.4618 | 776.8357 | -905434.6060 ppm | 85393.3513 | +8305.2867 ppm | 0.0279 ppm |
| ${}^{92}$Tc | 92 | 49 | 79.6121 | 787.8460 | -898949.6680 ppm | 86326.7664 | +8271.9775 ppm | 0.0362 ppm |
| ${}^{93}$Tc | 93 | 50 | 85.7490 | 800.5978 | -892893.7718 ppm | 87260.1949 | +8259.8249 ppm | 0.0117 ppm |
| ${}^{94}$Tc | 94 | 51 | 91.8728 | 809.2213 | -886467.6415 ppm | 88193.6366 | +8200.4982 ppm | 0.0465 ppm |
| ${}^{95}$Tc | 95 | 52 | 97.9838 | 819.1557 | -880384.3894 ppm | 89127.0910 | +8157.5136 ppm | 0.0575 ppm |
| ${}^{96}$Tc | 96 | 53 | 104.0823 | 827.0273 | -874148.8768 ppm | 90060.5579 | +8092.2869 ppm | 0.0576 ppm |
| ${}^{97}$Tc | 97 | 54 | 110.1686 | 836.5014 | -868298.3468 ppm | 90994.0370 | +8046.4370 ppm | 0.0456 ppm |
| ${}^{98}$Tc | 98 | 55 | 116.2430 | 843.7805 | -862235.4996 ppm | 91927.5281 | +7977.3924 ppm | 0.0371 ppm |
| ${}^{99}$Tc | 99 | 56 | 122.3057 | 852.7474 | -856574.5029 ppm | 92861.0307 | +7928.3370 ppm | 0.0098 ppm |
| ${}^{100}$Tc | 100 | 57 | 128.3571 | 859.5118 | -850662.8235 ppm | 93794.5448 | +7856.5310 ppm | 0.0145 ppm |
| ${}^{101}$Tc | 101 | 58 | 134.3973 | 867.9068 | -845147.7889 ppm | 94728.0700 | +7803.7511 ppm | 0.2554 ppm |
| ${}^{102}$Tc | 102 | 59 | 140.4266 | 874.2064 | -839366.7551 ppm | 95661.6061 | +7729.8775 ppm | 0.0966 ppm |
| ${}^{103}$Tc | 103 | 60 | 146.4453 | 882.3088 | -834020.3450 ppm | 96595.1529 | +7676.5028 ppm | 0.1023 ppm |
| ${}^{104}$Tc | 104 | 61 | 152.4536 | 888.2751 | -828371.2188 ppm | 97528.7100 | +7602.0275 ppm | 0.2571 ppm |
| ${}^{105}$Tc | 105 | 62 | 158.4517 | 896.1338 | -823183.0261 ppm | 98462.2773 | +7548.5886 ppm | 0.3608 ppm |
| ${}^{106}$Tc | 106 | 63 | 164.4398 | 901.6950 | -817632.6039 ppm | 99395.8547 | +7472.7994 ppm | 0.1242 ppm |
| ${}^{107}$Tc | 107 | 64 | 170.4181 | 908.7401 | -812467.6835 ppm | 100329.4417 | +7413.5385 ppm | 0.0871 ppm |
| ${}^{108}$Tc | 108 | 65 | 176.3869 | 913.9843 | -807013.1629 ppm | 101263.0383 | +7337.4260 ppm | 0.0872 ppm |
| ${}^{109}$Tc | 109 | 66 | 182.3464 | 920.4156 | -801886.9096 ppm | 102196.6443 | +7274.5932 ppm | 0.0953 ppm |
| ${}^{110}$Tc | 110 | 67 | 188.2967 | 925.2386 | -796488.5518 ppm | 103130.2595 | +7197.1751 ppm | 0.0927 ppm |
| ${}^{111}$Tc | 111 | 68 | 194.2380 | 931.3001 | -791433.5384 ppm | 104063.8836 | +7133.3149 ppm | 0.1024 ppm |
| ${}^{112}$Tc | 112 | 69 | 200.1705 | 935.6056 | -786052.5206 ppm | 104997.5165 | +7053.7228 ppm | 0.0529 ppm |
| ${}^{113}$Tc | 113 | 70 | 206.0944 | 941.2296 | -781037.0986 ppm | 105931.1580 | +6988.2478 ppm | 0.0319 ppm |
| ${}^{114}$Tc | 114 | 71 | 212.0098 | 945.0896 | -775672.2806 ppm | 106864.8080 | +6907.2699 ppm | 4.0812 ppm |
| ${}^{115}$Tc | 115 | 72 | 217.9170 | 950.3600 | -770700.6135 ppm | 107798.4663 | +6841.0202 ppm | 1.8270 ppm |
| ${}^{116}$Tc | 116 | 73 | 223.8160 | 953.8680 | -765359.5561 ppm | 108732.1327 | +6759.4070 ppm | 2.7599 ppm |
| ${}^{117}$Tc | 117 | 74 | 229.7071 | 958.8150 | -760426.0507 ppm | 109665.8070 | +6693.2142 ppm | 3.6683 ppm |
| ${}^{118}$Tc | 118 | 75 | 235.5904 | 962.0540 | -755117.3073 ppm | 110599.4891 | +6611.9525 ppm | 3.6370 ppm |
| ${}^{119}$Tc | 119 | 76 | 241.4660 | 966.9940 | -750292.1493 ppm | 111533.1789 | +6547.8375 ppm | 4.5142 ppm |
| ${}^{120}$Tc | 120 | 77 | 247.3341 | 969.9600 | -745005.8774 ppm | 112466.8763 | +6466.4042 ppm | 4.4764 ppm |
| ${}^{121}$Tc | 121 | 78 | 253.1948 | 974.5340 | -740188.8161 ppm | 113400.5809 | +6401.6650 ppm | 4.4393 ppm |
| ${}^{122}$Tc | 122 | 79 | 259.0483 | 977.3420 | -734946.0782 ppm | 114334.2929 | +6322.3293 ppm | 2.6400 ppm |

### Ruthenium (Z = 44)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{85}$Ru | 85 | 41 | 19.9388 | 682.2950 | -970776.8979 ppm | 79808.6994 | +8368.4313 ppm | 6.3201 ppm |
| ${}^{86}$Ru | 86 | 42 | 26.2280 | 699.4380 | -962501.3041 ppm | 80741.9756 | +8408.4375 ppm | 4.9908 ppm |
| ${}^{87}$Ru | 87 | 43 | 32.5009 | 713.4870 | -954447.8467 ppm | 81675.2682 | +8408.1395 ppm | 4.9338 ppm |
| ${}^{88}$Ru | 88 | 44 | 38.7578 | 730.2240 | -946923.4575 ppm | 82608.5767 | +8440.6661 ppm | 3.6615 ppm |
| ${}^{89}$Ru | 89 | 45 | 44.9991 | 742.2935 | -939378.2816 ppm | 83541.9008 | +8416.9029 ppm | 0.2923 ppm |
| ${}^{90}$Ru | 90 | 46 | 51.2253 | 756.8792 | -932320.3984 ppm | 84475.2401 | +8423.7557 ppm | 0.0445 ppm |
| ${}^{91}$Ru | 91 | 47 | 57.4367 | 768.3065 | -925242.5123 ppm | 85408.5941 | +8393.0294 ppm | 0.0262 ppm |
| ${}^{92}$Ru | 92 | 48 | 63.6336 | 782.4392 | -918672.7581 ppm | 86341.9626 | +8394.9980 ppm | 0.0317 ppm |
| ${}^{93}$Ru | 93 | 49 | 69.8165 | 793.4260 | -912006.2843 ppm | 87275.3451 | +8360.4353 ppm | 0.0238 ppm |
| ${}^{94}$Ru | 94 | 50 | 75.9856 | 806.8642 | -905825.9794 ppm | 88208.7414 | +8355.0194 ppm | 0.0359 ppm |
| ${}^{95}$Ru | 95 | 51 | 82.1414 | 815.8097 | -899313.0626 ppm | 89142.1511 | +8298.6265 ppm | 0.1075 ppm |
| ${}^{96}$Ru | 96 | 52 | 88.2840 | 826.5036 | -893183.7529 ppm | 90075.5739 | +8263.2880 ppm | 0.0019 ppm |
| ${}^{97}$Ru | 97 | 53 | 94.4139 | 834.6152 | -886877.3657 ppm | 91009.0094 | +8199.9747 ppm | 0.0306 ppm |
| ${}^{98}$Ru | 98 | 54 | 100.5312 | 844.7908 | -880998.6815 ppm | 91942.4575 | +8160.9092 ppm | 0.0709 ppm |
| ${}^{99}$Ru | 99 | 55 | 106.6364 | 852.2626 | -874878.5218 ppm | 92875.9178 | +8093.1786 ppm | 0.0037 ppm |
| ${}^{100}$Ru | 100 | 56 | 112.7296 | 861.9359 | -869213.5214 ppm | 93809.3900 | +8050.7796 ppm | 0.0037 ppm |
| ${}^{101}$Ru | 101 | 57 | 118.8111 | 868.7380 | -863237.1194 ppm | 94742.8739 | +7978.5510 ppm | 0.0044 ppm |
| ${}^{102}$Ru | 102 | 58 | 124.8812 | 877.9576 | -857759.3722 ppm | 95676.3692 | +7933.5325 ppm | 0.0044 ppm |
| ${}^{103}$Ru | 103 | 59 | 130.9402 | 884.1897 | -851909.3529 ppm | 96609.8756 | +7858.0911 ppm | 0.0046 ppm |
| ${}^{104}$Ru | 104 | 60 | 136.9883 | 893.0896 | -846613.0551 ppm | 97543.3930 | +7811.9962 ppm | 0.0258 ppm |
| ${}^{105}$Ru | 105 | 61 | 143.0257 | 898.9997 | -840905.7617 ppm | 98476.9210 | +7736.0555 ppm | 0.0256 ppm |
| ${}^{106}$Ru | 106 | 62 | 149.0526 | 907.4597 | -835747.4146 ppm | 99410.4595 | +7687.7038 ppm | 0.0546 ppm |
| ${}^{107}$Ru | 107 | 63 | 155.0693 | 913.0703 | -830167.1811 ppm | 100344.0082 | +7611.5281 ppm | 0.0871 ppm |
| ${}^{108}$Ru | 108 | 64 | 161.0760 | 920.9405 | -825096.1891 ppm | 101277.5669 | +7559.5157 ppm | 0.0863 ppm |
| ${}^{109}$Ru | 109 | 65 | 167.0729 | 926.0889 | -819593.0277 ppm | 102211.1355 | +7481.5257 ppm | 0.0883 ppm |
| ${}^{110}$Ru | 110 | 66 | 173.0602 | 933.4944 | -814610.3757 ppm | 103144.7136 | +7427.2618 ppm | 0.0872 ppm |
| ${}^{111}$Ru | 111 | 67 | 179.0380 | 938.2784 | -809184.5142 ppm | 104078.3012 | +7348.5084 ppm | 0.0937 ppm |
| ${}^{112}$Ru | 112 | 68 | 185.0067 | 945.1952 | -804266.1535 ppm | 105011.8979 | +7291.8632 ppm | 0.0921 ppm |
| ${}^{113}$Ru | 113 | 69 | 190.9663 | 949.5035 | -798877.7033 ppm | 105945.5037 | +7211.3292 ppm | 0.3639 ppm |
| ${}^{114}$Ru | 114 | 70 | 196.9171 | 955.9282 | -794004.3065 ppm | 106879.1184 | +7152.3843 ppm | 0.0335 ppm |
| ${}^{115}$Ru | 115 | 71 | 202.8592 | 959.8836 | -788662.7252 ppm | 107812.7417 | +7071.3187 ppm | 0.2351 ppm |
| ${}^{116}$Ru | 116 | 72 | 208.7928 | 965.9185 | -783840.1874 ppm | 108746.3736 | +7011.1281 ppm | 0.0345 ppm |
| ${}^{117}$Ru | 117 | 73 | 214.7180 | 969.4108 | -778506.6859 ppm | 109680.0137 | +6928.5403 ppm | 3.9765 ppm |
| ${}^{118}$Ru | 118 | 74 | 220.6351 | 975.0340 | -773715.5084 ppm | 110613.6621 | +6866.5813 ppm | 1.8230 ppm |
| ${}^{119}$Ru | 119 | 75 | 226.5441 | 978.1800 | -768402.4351 ppm | 111547.3185 | +6783.6555 ppm | 2.7072 ppm |
| ${}^{120}$Ru | 120 | 76 | 232.4453 | 983.8800 | -763746.3264 ppm | 112480.9828 | +6725.2622 ppm | 3.5766 ppm |
| ${}^{121}$Ru | 121 | 77 | 238.3387 | 986.8760 | -758491.7498 ppm | 113414.6547 | +6643.4197 ppm | 3.5469 ppm |
| ${}^{122}$Ru | 122 | 78 | 244.2245 | 992.1040 | -753831.7106 ppm | 114348.3343 | +6583.0165 ppm | 4.4033 ppm |
| ${}^{123}$Ru | 123 | 79 | 250.1030 | 994.9470 | -748626.8611 ppm | 115282.0213 | +6502.6593 ppm | 4.3672 ppm |
| ${}^{124}$Ru | 124 | 80 | 255.9740 | 1000.0600 | -744041.3077 ppm | 116215.7157 | +6443.4542 ppm | 5.1951 ppm |
| ${}^{125}$Ru | 125 | 81 | 261.8380 | 1002.8750 | -738912.6506 ppm | 117149.4172 | +6365.7246 ppm | 2.5766 ppm |

### Rhodium (Z = 45)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{88}$Rh | 88 | 43 | 22.2719 | 711.9200 | -968715.7003 ppm | 82624.2802 | +8417.1899 ppm | 4.8772 ppm |
| ${}^{89}$Rh | 89 | 44 | 28.5631 | 728.8210 | -960809.2219 ppm | 83557.5545 | +8451.0326 ppm | 4.3507 ppm |
| ${}^{90}$Rh | 90 | 45 | 34.8383 | 742.8600 | -953102.4328 ppm | 84490.8447 | +8450.5255 ppm | 2.3904 ppm |
| ${}^{91}$Rh | 91 | 46 | 41.0981 | 757.8480 | -945769.9874 ppm | 85424.1503 | +8461.5569 ppm | 3.5189 ppm |
| ${}^{92}$Rh | 92 | 47 | 47.3428 | 770.3547 | -938544.1810 ppm | 86357.4711 | +8443.0104 ppm | 0.0511 ppm |
| ${}^{93}$Rh | 93 | 48 | 53.5727 | 784.4388 | -931705.6722 ppm | 87290.8066 | +8443.4753 ppm | 0.0304 ppm |
| ${}^{94}$Rh | 94 | 49 | 59.7883 | 796.4059 | -924927.3880 ppm | 88224.1564 | +8419.6939 ppm | 0.0386 ppm |
| ${}^{95}$Rh | 95 | 50 | 65.9898 | 809.9102 | -918522.1000 ppm | 89157.5203 | +8414.1026 ppm | 0.0439 ppm |
| ${}^{96}$Rh | 96 | 51 | 72.1776 | 819.3287 | -911906.4323 ppm | 90090.8980 | +8362.6640 ppm | 0.1119 ppm |
| ${}^{97}$Rh | 97 | 52 | 78.3520 | 830.3098 | -905635.2300 ppm | 91024.2890 | +8329.8888 ppm | 0.3928 ppm |
| ${}^{98}$Rh | 98 | 53 | 84.5133 | 838.9588 | -899264.0358 ppm | 91957.6931 | +8272.1410 ppm | 0.1305 ppm |
| ${}^{99}$Rh | 99 | 54 | 90.6619 | 849.4394 | -893268.5897 ppm | 92891.1099 | +8235.7429 ppm | 0.2111 ppm |
| ${}^{100}$Rh | 100 | 55 | 96.7979 | 857.5173 | -887118.4154 ppm | 93824.5393 | +8174.1764 ppm | 0.1948 ppm |
| ${}^{101}$Rh | 101 | 56 | 102.9217 | 867.4099 | -881345.8958 ppm | 94757.9809 | +8133.4233 ppm | 0.0621 ppm |
| ${}^{102}$Rh | 102 | 57 | 109.0336 | 874.8521 | -875369.0646 ppm | 95691.4344 | +8067.5713 ppm | 0.0675 ppm |
| ${}^{103}$Rh | 103 | 58 | 115.1339 | 884.1718 | -869783.3996 ppm | 96624.8996 | +8022.8654 ppm | 0.0240 ppm |
| ${}^{104}$Rh | 104 | 59 | 121.2226 | 891.1708 | -863973.7347 ppm | 97558.3763 | +7954.9680 ppm | 0.0238 ppm |
| ${}^{105}$Rh | 105 | 60 | 127.3002 | 900.1341 | -858576.3519 ppm | 98491.8641 | +7908.7408 ppm | 0.0256 ppm |
| ${}^{106}$Rh | 106 | 61 | 133.3669 | 906.7168 | -852912.2743 ppm | 99425.3629 | +7839.1764 ppm | 0.0546 ppm |
| ${}^{107}$Rh | 107 | 62 | 139.4229 | 915.2891 | -847673.4218 ppm | 100358.8723 | +7791.1581 ppm | 0.1210 ppm |
| ${}^{108}$Rh | 108 | 63 | 145.4683 | 921.5279 | -842144.4084 ppm | 101292.3923 | +7720.7377 ppm | 0.1392 ppm |
| ${}^{109}$Rh | 109 | 64 | 151.5035 | 929.5673 | -837017.1430 ppm | 102225.9225 | +7669.5995 ppm | 0.0398 ppm |
| ${}^{110}$Rh | 110 | 65 | 157.5287 | 935.4681 | -831604.4232 ppm | 103159.4628 | +7598.4419 ppm | 0.1739 ppm |
| ${}^{111}$Rh | 111 | 66 | 163.5440 | 943.0146 | -826573.2159 ppm | 104093.0129 | +7544.7153 ppm | 0.0663 ppm |
| ${}^{112}$Rh | 112 | 67 | 169.5496 | 948.5131 | -821246.9182 ppm | 105026.5727 | +7472.2492 ppm | 0.4229 ppm |
| ${}^{113}$Rh | 113 | 68 | 175.5458 | 955.6203 | -816301.6922 ppm | 105960.1419 | +7416.5681 ppm | 0.0678 ppm |
| ${}^{114}$Rh | 114 | 69 | 181.5328 | 960.6349 | -811028.3660 ppm | 106893.7204 | +7342.0879 ppm | 0.6744 ppm |
| ${}^{115}$Rh | 115 | 70 | 187.5106 | 967.2252 | -806135.5384 ppm | 107827.3080 | +7283.8189 ppm | 0.0684 ppm |
| ${}^{116}$Rh | 116 | 71 | 193.4795 | 971.8030 | -800906.6477 ppm | 108760.9045 | +7207.8680 ppm | 0.6837 ppm |
| ${}^{117}$Rh | 117 | 72 | 199.4397 | 978.0354 | -796081.2791 ppm | 109694.5097 | +7148.6002 ppm | 0.0817 ppm |
| ${}^{118}$Rh | 118 | 73 | 205.3914 | 982.0968 | -790864.4449 ppm | 110628.1235 | +7070.5149 ppm | 0.2206 ppm |
| ${}^{119}$Rh | 119 | 74 | 211.3346 | 988.1040 | -786121.1266 ppm | 111561.7457 | +7011.5116 ppm | 0.0841 ppm |
| ${}^{120}$Rh | 120 | 75 | 217.2696 | 991.9200 | -780960.5987 ppm | 112495.3761 | +6934.2899 ppm | 1.7926 ppm |
| ${}^{121}$Rh | 121 | 76 | 223.1965 | 997.6740 | -776283.1780 ppm | 113429.0146 | +6874.8073 ppm | 5.4986 ppm |
| ${}^{122}$Rh | 122 | 77 | 229.1154 | 1001.3760 | -771199.4162 ppm | 114362.6611 | +6798.6381 ppm | 2.6405 ppm |
| ${}^{123}$Rh | 123 | 78 | 235.0266 | 1006.7550 | -766550.3749 ppm | 115296.3154 | +6738.5615 ppm | 3.4893 ppm |
| ${}^{124}$Rh | 124 | 79 | 240.9301 | 1010.3520 | -761538.4618 ppm | 116229.9773 | +6663.9057 ppm | 3.4610 ppm |
| ${}^{125}$Rh | 125 | 80 | 246.8261 | 1015.5000 | -756941.3129 ppm | 117163.6467 | +6604.3546 ppm | 4.2975 ppm |
| ${}^{126}$Rh | 126 | 81 | 252.7147 | 1018.9620 | -751988.0754 ppm | 118097.3235 | +6530.8077 ppm | 4.2633 ppm |
| ${}^{127}$Rh | 127 | 82 | 258.5961 | 1023.6200 | -747370.9832 ppm | 119031.0075 | +6468.3557 ppm | 5.0723 ppm |
| ${}^{128}$Rh | 128 | 83 | 264.4704 | 1025.2800 | -742050.5738 ppm | 119964.6987 | +6382.2883 ppm | 2.5162 ppm |

### Palladium (Z = 46)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{90}$Pd | 90 | 44 | 18.1368 | 730.1700 | -975160.8309 ppm | 84506.7639 | +8497.0004 ppm | 4.7689 ppm |
| ${}^{91}$Pd | 91 | 45 | 24.4461 | 744.6530 | -967171.1551 ppm | 85440.0200 | +8501.2726 ppm | 4.9917 ppm |
| ${}^{92}$Pd | 92 | 46 | 30.7396 | 761.3524 | -959625.0286 ppm | 86373.2919 | +8530.9509 ppm | 4.0287 ppm |
| ${}^{93}$Pd | 93 | 47 | 37.0176 | 773.6264 | -952150.4844 ppm | 87306.5793 | +8508.8334 ppm | 4.2741 ppm |
| ${}^{94}$Pd | 94 | 48 | 43.2807 | 788.8182 | -945132.2589 ppm | 88239.8817 | +8520.9876 ppm | 0.0490 ppm |
| ${}^{95}$Pd | 95 | 49 | 49.5290 | 800.7532 | -938146.9672 ppm | 89173.1988 | +8495.9066 ppm | 0.0343 ppm |
| ${}^{96}$Pd | 96 | 50 | 55.7630 | 815.0420 | -931582.6544 ppm | 90106.5302 | +8498.0752 ppm | 0.0469 ppm |
| ${}^{97}$Pd | 97 | 51 | 61.9830 | 824.7357 | -924845.0168 ppm | 91039.8756 | +8449.0223 ppm | 0.0537 ppm |
| ${}^{98}$Pd | 98 | 52 | 68.1893 | 836.3222 | -918465.2639 ppm | 91973.2347 | +8422.0460 ppm | 0.0520 ppm |
| ${}^{99}$Pd | 99 | 53 | 74.3822 | 845.2554 | -912000.2683 ppm | 92906.6072 | +8366.7193 ppm | 0.0554 ppm |
| ${}^{100}$Pd | 100 | 54 | 80.5621 | 856.3565 | -905924.5584 ppm | 93839.9928 | +8336.1281 ppm | 0.1895 ppm |
| ${}^{101}$Pd | 101 | 55 | 86.7292 | 864.6473 | -899694.1145 ppm | 94773.3911 | +8276.1303 ppm | 0.0488 ppm |
| ${}^{102}$Pd | 102 | 56 | 92.8838 | 875.1894 | -893870.0436 ppm | 95706.8019 | +8241.3533 ppm | 0.0044 ppm |
| ${}^{103}$Pd | 103 | 57 | 99.0262 | 882.8148 | -887829.0129 ppm | 96640.2250 | +8176.6993 ppm | 0.0092 ppm |
| ${}^{104}$Pd | 104 | 58 | 105.1566 | 892.8242 | -882220.2206 ppm | 97573.6599 | +8138.2467 ppm | 0.0138 ppm |
| ${}^{105}$Pd | 105 | 59 | 111.2754 | 899.9183 | -876349.4629 ppm | 98507.1066 | +8070.5694 ppm | 0.0116 ppm |
| ${}^{106}$Pd | 106 | 60 | 117.3827 | 909.4793 | -870934.1842 ppm | 99440.5647 | +8029.4942 ppm | 0.0112 ppm |
| ${}^{107}$Pd | 107 | 61 | 123.4788 | 916.0157 | -865200.1428 ppm | 100374.0341 | +7958.6836 ppm | 0.0121 ppm |
| ${}^{108}$Pd | 108 | 62 | 129.5639 | 925.2386 | -859967.0147 ppm | 101307.5144 | +7916.2353 ppm | 0.0110 ppm |
| ${}^{109}$Pd | 109 | 63 | 135.6383 | 931.3922 | -854370.3474 ppm | 102241.0054 | +7844.1775 ppm | 0.0110 ppm |
| ${}^{110}$Pd | 110 | 64 | 141.7022 | 940.1879 | -849283.1076 ppm | 103174.5069 | +7799.5454 ppm | 0.0060 ppm |
| ${}^{111}$Pd | 111 | 65 | 147.7558 | 945.9142 | -843795.7913 ppm | 104108.0188 | +7725.8757 ppm | 0.0071 ppm |
| ${}^{112}$Pd | 112 | 66 | 153.7993 | 954.3207 | -838839.0067 ppm | 105041.5407 | +7679.5309 ppm | 0.0628 ppm |
| ${}^{113}$Pd | 113 | 67 | 159.8329 | 959.6615 | -833448.6985 ppm | 105975.0725 | +7604.7297 ppm | 0.0661 ppm |
| ${}^{114}$Pd | 114 | 68 | 165.8568 | 967.6326 | -828595.3085 ppm | 106908.6140 | +7556.3138 ppm | 0.0655 ppm |
| ${}^{115}$Pd | 115 | 69 | 171.8712 | 972.6394 | -823294.0482 ppm | 107842.1651 | +7480.9278 ppm | 0.1266 ppm |
| ${}^{116}$Pd | 116 | 70 | 177.8763 | 980.1160 | -818515.0825 ppm | 108775.7254 | +7429.9759 ppm | 0.0661 ppm |
| ${}^{117}$Pd | 117 | 71 | 183.8722 | 984.7801 | -813286.0244 ppm | 109709.2949 | +7353.9665 ppm | 0.0666 ppm |
| ${}^{118}$Pd | 118 | 72 | 189.8592 | 991.8159 | -808574.1482 ppm | 110642.8733 | +7301.0809 ppm | 0.0227 ppm |
| ${}^{119}$Pd | 119 | 73 | 195.8374 | 995.9062 | -803357.5666 ppm | 111576.4605 | +7222.3823 ppm | 0.0745 ppm |
| ${}^{120}$Pd | 120 | 74 | 201.8070 | 1002.8498 | -798766.4814 ppm | 112510.0564 | +7170.8047 ppm | 0.0205 ppm |
| ${}^{121}$Pd | 121 | 75 | 207.7681 | 1006.8239 | -793640.0558 ppm | 113443.6607 | +7093.6060 ppm | 0.0298 ppm |
| ${}^{122}$Pd | 122 | 76 | 213.7209 | 1013.3290 | -789090.2815 ppm | 114377.2733 | +7040.1938 ppm | 0.1722 ppm |
| ${}^{123}$Pd | 123 | 77 | 219.6656 | 1017.2139 | -784051.7078 ppm | 115310.8940 | +6964.6817 ppm | 6.8939 ppm |
| ${}^{124}$Pd | 124 | 78 | 225.6023 | 1023.2480 | -779523.3632 ppm | 116244.5228 | +6909.2729 ppm | 2.5981 ppm |
| ${}^{125}$Pd | 125 | 79 | 231.5311 | 1026.8750 | -774528.4538 ppm | 117178.1594 | +6833.9649 ppm | 3.4336 ppm |
| ${}^{126}$Pd | 126 | 80 | 237.4522 | 1032.8220 | -770093.7840 ppm | 118111.8037 | +6779.4128 ppm | 3.4063 ppm |
| ${}^{127}$Pd | 127 | 81 | 243.3657 | 1036.3200 | -765163.5333 ppm | 119045.4556 | +6705.3503 ppm | 4.2300 ppm |
| ${}^{128}$Pd | 128 | 82 | 249.2718 | 1041.5360 | -760669.0344 ppm | 119979.1149 | +6647.2095 ppm | 4.1969 ppm |
| ${}^{129}$Pd | 129 | 83 | 255.1706 | 1043.0940 | -755371.4265 ppm | 120912.7816 | +6559.1945 ppm | 4.9938 ppm |
| ${}^{130}$Pd | 130 | 84 | 261.0622 | 1045.9800 | -750413.7774 ppm | 121846.4554 | +6483.9093 ppm | 2.4776 ppm |
| ${}^{131}$Pd | 131 | 85 | 266.9467 | 1047.0830 | -745056.7521 ppm | 122780.1363 | +6394.6617 ppm | 2.4585 ppm |

### Silver (Z = 47)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{92}$Ag | 92 | 45 | 13.8240 | 743.3600 | -981403.3288 ppm | 86389.4252 | +8516.2051 ppm | 4.6651 ppm |
| ${}^{93}$Ag | 93 | 46 | 20.1513 | 760.2750 | -973494.7253 ppm | 87322.6633 | +8548.0414 ppm | 4.6261 ppm |
| ${}^{94}$Ag | 94 | 47 | 26.4629 | 774.3720 | -965826.6900 ppm | 88255.9172 | +8546.3407 ppm | 4.5666 ppm |
| ${}^{95}$Ag | 95 | 48 | 32.7591 | 789.9250 | -958528.8913 ppm | 89189.1864 | +8561.9740 ppm | 4.5188 ppm |
| ${}^{96}$Ag | 96 | 49 | 39.0403 | 802.5879 | -951356.9864 ppm | 90122.4706 | +8544.7345 ppm | 1.0081 ppm |
| ${}^{97}$Ag | 97 | 50 | 45.3069 | 817.0516 | -944548.3169 ppm | 91055.7694 | +8547.9727 ppm | 0.1331 ppm |
| ${}^{98}$Ag | 98 | 51 | 51.5592 | 827.2853 | -937676.6622 ppm | 91989.0825 | +8504.5308 ppm | 0.3608 ppm |
| ${}^{99}$Ag | 99 | 52 | 57.7975 | 839.0027 | -931111.6544 ppm | 92922.4096 | +8478.3551 ppm | 0.0680 ppm |
| ${}^{100}$Ag | 100 | 53 | 64.0222 | 848.4995 | -924546.5919 ppm | 93855.7504 | +8428.7875 ppm | 0.0537 ppm |
| ${}^{101}$Ag | 101 | 54 | 70.2335 | 859.7672 | -918311.0261 ppm | 94789.1045 | +8399.3405 ppm | 0.0515 ppm |
| ${}^{102}$Ag | 102 | 55 | 76.4318 | 868.7508 | -912021.0664 ppm | 95722.4716 | +8346.3446 ppm | 0.0861 ppm |
| ${}^{103}$Ag | 103 | 56 | 82.6173 | 879.3782 | -906050.3405 ppm | 96655.8516 | +8311.7999 ppm | 0.0428 ppm |
| ${}^{104}$Ag | 104 | 57 | 88.7903 | 887.7632 | -899984.2588 ppm | 97589.2440 | +8254.6896 ppm | 0.0436 ppm |
| ${}^{105}$Ag | 105 | 58 | 94.9511 | 897.7889 | -894238.9491 ppm | 98522.6486 | +8215.7193 ppm | 0.0465 ppm |
| ${}^{106}$Ag | 106 | 59 | 101.0999 | 905.7318 | -888377.6115 ppm | 99456.0651 | +8156.3190 ppm | 0.0306 ppm |
| ${}^{107}$Ag | 107 | 60 | 107.2371 | 915.2674 | -882835.2368 ppm | 100389.4934 | +8114.2716 ppm | 0.0239 ppm |
| ${}^{108}$Ag | 108 | 61 | 113.3628 | 922.5388 | -877118.6921 ppm | 101322.9332 | +8050.4081 ppm | 0.0238 ppm |
| ${}^{109}$Ag | 109 | 62 | 119.4772 | 931.7228 | -871767.3896 ppm | 102256.3841 | +8006.8327 ppm | 0.0127 ppm |
| ${}^{110}$Ag | 110 | 63 | 125.5807 | 938.5320 | -866194.5163 ppm | 103189.8461 | +7940.7758 ppm | 0.0126 ppm |
| ${}^{111}$Ag | 111 | 64 | 131.6734 | 947.3614 | -861010.3432 ppm | 104123.3188 | +7895.7256 ppm | 0.0141 ppm |
| ${}^{112}$Ag | 112 | 65 | 137.7556 | 953.8010 | -855571.9606 ppm | 105056.8020 | +7828.4748 ppm | 0.0232 ppm |
| ${}^{113}$Ag | 113 | 66 | 143.8275 | 962.3155 | -850540.2245 ppm | 105990.2956 | +7782.3966 ppm | 0.1582 ppm |
| ${}^{114}$Ag | 114 | 67 | 149.8892 | 968.2908 | -845202.3203 ppm | 106923.7993 | +7713.1072 ppm | 0.0430 ppm |
| ${}^{115}$Ag | 115 | 68 | 155.9409 | 976.4139 | -840292.1625 ppm | 107857.3130 | +7665.3386 ppm | 0.1707 ppm |
| ${}^{116}$Ag | 116 | 69 | 161.9830 | 982.0452 | -835055.4661 ppm | 108790.8363 | +7595.2310 ppm | 0.0302 ppm |
| ${}^{117}$Ag | 117 | 70 | 168.0155 | 989.7558 | -830245.5049 ppm | 109724.3692 | +7545.6492 ppm | 0.1246 ppm |
| ${}^{118}$Ag | 118 | 71 | 174.0386 | 995.1990 | -825121.7686 ppm | 110657.9115 | +7476.1961 ppm | 0.0229 ppm |
| ${}^{119}$Ag | 119 | 72 | 180.0526 | 1002.3623 | -820371.7294 ppm | 111591.4630 | +7423.6408 ppm | 0.1327 ppm |
| ${}^{120}$Ag | 120 | 73 | 186.0576 | 1007.4394 | -815316.3704 ppm | 112525.0235 | +7353.2296 ppm | 0.0400 ppm |
| ${}^{121}$Ag | 121 | 74 | 192.0537 | 1014.2620 | -810646.8806 ppm | 113458.5928 | +7299.6755 ppm | 0.1075 ppm |
| ${}^{122}$Ag | 122 | 75 | 198.0411 | 1019.0366 | -805658.4898 ppm | 114392.1707 | +7228.9136 ppm | 0.3363 ppm |
| ${}^{123}$Ag | 123 | 76 | 204.0200 | 1025.5704 | -801066.7625 ppm | 115325.7572 | +7174.8549 ppm | 0.2847 ppm |
| ${}^{124}$Ag | 124 | 77 | 209.9906 | 1030.3031 | -796185.5976 ppm | 116259.3521 | +7106.0293 ppm | 2.1787 ppm |
| ${}^{125}$Ag | 125 | 78 | 215.9530 | 1036.6644 | -791684.7825 ppm | 117192.9552 | +7052.4733 ppm | 3.7221 ppm |
| ${}^{126}$Ag | 126 | 79 | 221.9073 | 1040.8860 | -786809.2470 ppm | 118126.5663 | +6981.9008 ppm | 1.7072 ppm |
| ${}^{127}$Ag | 127 | 80 | 227.8537 | 1046.9880 | -782372.2342 ppm | 119060.1853 | +6927.2342 ppm | 1.6938 ppm |
| ${}^{128}$Ag | 128 | 81 | 233.7923 | 1051.0080 | -777554.2383 ppm | 119993.8121 | +6857.7025 ppm | 2.5168 ppm |
| ${}^{129}$Ag | 129 | 82 | 239.7233 | 1056.2520 | -773043.5021 ppm | 120927.4466 | +6798.5307 ppm | 3.3270 ppm |
| ${}^{130}$Ag | 130 | 83 | 245.6467 | 1058.4600 | -767920.6280 ppm | 121861.0885 | +6714.2810 ppm | 3.5013 ppm |
| ${}^{131}$Ag | 131 | 84 | 251.5628 | 1061.3620 | -762981.1157 ppm | 122794.7378 | +6638.1970 ppm | 4.1006 ppm |
| ${}^{132}$Ag | 132 | 85 | 257.4717 | 1062.9960 | -757786.7677 ppm | 123728.3944 | +6553.4843 ppm | 4.0693 ppm |
| ${}^{133}$Ag | 133 | 86 | 263.3734 | 1065.7290 | -752870.1611 ppm | 124662.0581 | +6478.4834 ppm | 4.0385 ppm |

### Cadmium (Z = 48)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{94}$Cd | 94 | 46 | 9.3348 | 761.5880 | -987742.9615 ppm | 88272.2629 | +8595.2578 ppm | 5.7154 ppm |
| ${}^{95}$Cd | 95 | 47 | 15.6799 | 776.2450 | -979800.2631 ppm | 89205.4832 | +8599.7015 ppm | 6.3929 ppm |
| ${}^{96}$Cd | 96 | 48 | 22.0094 | 792.8640 | -972240.5932 ppm | 90138.7191 | +8625.6640 ppm | 4.5862 ppm |
| ${}^{97}$Cd | 97 | 49 | 28.3236 | 806.0992 | -964863.3248 ppm | 91071.9703 | +8613.8017 ppm | 4.6534 ppm |
| ${}^{98}$Cd | 98 | 50 | 34.6229 | 821.0729 | -957832.0841 ppm | 92005.2364 | +8621.5871 ppm | 0.5678 ppm |
| ${}^{99}$Cd | 99 | 51 | 40.9076 | 831.4390 | -950798.9870 ppm | 92938.5172 | +8578.9399 ppm | 0.0172 ppm |
| ${}^{100}$Cd | 100 | 52 | 47.1781 | 843.7737 | -944086.7994 ppm | 93871.8121 | +8558.6303 ppm | 0.0180 ppm |
| ${}^{101}$Cd | 101 | 53 | 53.4346 | 853.4869 | -937392.5874 ppm | 94805.1210 | +8510.7436 ppm | 0.0159 ppm |
| ${}^{102}$Cd | 102 | 54 | 59.6775 | 865.3815 | -931039.0814 ppm | 95738.4436 | +8487.1110 ppm | 0.0175 ppm |
| ${}^{103}$Cd | 103 | 55 | 65.9071 | 874.4447 | -924629.8043 ppm | 96671.7794 | +8434.2899 ppm | 0.0189 ppm |
| ${}^{104}$Cd | 104 | 56 | 72.1236 | 885.8328 | -918581.0192 ppm | 97605.1283 | +8406.8395 ppm | 0.0173 ppm |
| ${}^{105}$Cd | 105 | 57 | 78.3274 | 894.2696 | -912411.8870 ppm | 98538.4900 | +8349.5871 ppm | 0.0142 ppm |
| ${}^{106}$Cd | 106 | 58 | 84.5187 | 905.1392 | -906623.5510 ppm | 99471.8641 | +8318.4075 ppm | 0.0112 ppm |
| ${}^{107}$Cd | 107 | 59 | 90.6978 | 913.0687 | -900667.0922 ppm | 100405.2504 | +8258.1630 ppm | 0.0167 ppm |
| ${}^{108}$Cd | 108 | 60 | 96.8649 | 923.4021 | -895099.9872 ppm | 101338.6487 | +8223.2671 ppm | 0.0112 ppm |
| ${}^{109}$Cd | 109 | 61 | 103.0203 | 930.7253 | -889311.8061 ppm | 102272.0587 | +8159.2097 ppm | 0.0151 ppm |
| ${}^{110}$Cd | 110 | 62 | 109.1643 | 940.6403 | -883946.8709 ppm | 103205.4802 | +8121.9522 ppm | 0.0037 ppm |
| ${}^{111}$Cd | 111 | 63 | 115.2970 | 947.6159 | -878329.4366 ppm | 104138.9129 | +8056.7912 ppm | 0.0035 ppm |
| ${}^{112}$Cd | 112 | 64 | 121.4187 | 957.0098 | -873127.0495 ppm | 105072.3566 | +8016.2875 ppm | 0.0024 ppm |
| ${}^{113}$Cd | 113 | 65 | 127.5296 | 963.5496 | -867646.0680 ppm | 106005.8111 | +7949.2477 ppm | 0.0023 ppm |
| ${}^{114}$Cd | 114 | 66 | 133.6299 | 972.5925 | -862604.4179 ppm | 106939.2762 | +7907.2654 ppm | 0.0026 ppm |
| ${}^{115}$Cd | 115 | 67 | 139.7199 | 978.7334 | -857244.1707 ppm | 107872.7517 | +7838.7828 ppm | 0.0061 ppm |
| ${}^{116}$Cd | 116 | 68 | 145.7997 | 987.4327 | -852344.6574 ppm | 108806.2373 | +7795.4598 ppm | 0.0015 ppm |
| ${}^{117}$Cd | 117 | 69 | 151.8696 | 993.2100 | -847092.1750 ppm | 109739.7328 | +7725.9277 ppm | 0.0093 ppm |
| ${}^{118}$Cd | 118 | 70 | 157.9297 | 1001.5645 | -842317.0398 ppm | 110673.2382 | +7681.3133 ppm | 0.1821 ppm |
| ${}^{119}$Cd | 119 | 71 | 163.9802 | 1006.9111 | -837145.3496 ppm | 111606.7531 | +7610.1717 ppm | 0.3403 ppm |
| ${}^{120}$Cd | 120 | 72 | 170.0213 | 1014.9629 | -832485.2449 ppm | 112540.2774 | +7564.7057 ppm | 0.0334 ppm |
| ${}^{121}$Cd | 121 | 73 | 176.0531 | 1020.1507 | -827424.3836 ppm | 113473.8110 | +7494.4545 ppm | 0.0172 ppm |
| ${}^{122}$Cd | 122 | 74 | 182.0759 | 1027.7605 | -822842.0544 ppm | 114407.3536 | +7446.9258 ppm | 0.0202 ppm |
| ${}^{123}$Cd | 123 | 75 | 188.0899 | 1032.6336 | -817854.2073 ppm | 115340.9051 | +7376.1690 ppm | 0.0235 ppm |
| ${}^{124}$Cd | 124 | 76 | 194.0951 | 1039.9902 | -813368.3619 ppm | 116274.4653 | +7328.3059 ppm | 0.0226 ppm |
| ${}^{125}$Cd | 125 | 77 | 200.0917 | 1044.7102 | -808471.5560 ppm | 117208.0341 | +7258.4601 ppm | 0.0248 ppm |
| ${}^{126}$Cd | 126 | 78 | 206.0799 | 1051.6892 | -804048.6169 ppm | 118141.6113 | +7209.1966 ppm | 0.0196 ppm |
| ${}^{127}$Cd | 127 | 79 | 212.0599 | 1056.2459 | -799232.4476 ppm | 119075.1967 | +7140.1467 ppm | 0.0524 ppm |
| ${}^{128}$Cd | 128 | 80 | 218.0318 | 1062.8143 | -794854.3186 ppm | 120008.7903 | +7089.2486 ppm | 0.0540 ppm |
| ${}^{129}$Cd | 129 | 81 | 223.9956 | 1066.7695 | -790024.3277 ppm | 120942.3918 | +7017.2963 ppm | 0.0442 ppm |
| ${}^{130}$Cd | 130 | 82 | 229.9517 | 1072.8363 | -785660.0305 ppm | 121876.0012 | +6964.0885 ppm | 0.1847 ppm |
| ${}^{131}$Cd | 131 | 83 | 235.9001 | 1075.0018 | -780558.4528 ppm | 122809.6183 | +6879.5516 ppm | 0.1577 ppm |
| ${}^{132}$Cd | 132 | 84 | 241.8408 | 1078.3268 | -775725.8235 ppm | 123743.2429 | +6805.8638 ppm | 0.4887 ppm |
| ${}^{133}$Cd | 133 | 85 | 247.7742 | 1080.0930 | -770599.1930 ppm | 124676.8750 | +6720.5120 ppm | 1.6171 ppm |
| ${}^{134}$Cd | 134 | 86 | 253.7003 | 1083.5240 | -765856.3545 ppm | 125610.5143 | +6649.7789 ppm | 2.4037 ppm |
| ${}^{135}$Cd | 135 | 87 | 259.6191 | 1084.8600 | -760688.8175 ppm | 126544.1609 | +6564.4645 ppm | 3.1786 ppm |

### Indium (Z = 49)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{96}$In | 96 | 47 | 4.6704 | 774.6240 | -993970.7079 ppm | 90155.2758 | +8613.6216 ppm | 5.5961 ppm |
| ${}^{97}$In | 97 | 48 | 11.0333 | 792.0050 | -986069.1714 ppm | 91088.4783 | +8647.5620 ppm | 4.4353 ppm |
| ${}^{98}$In | 98 | 49 | 17.3806 | 806.5400 | -978450.4524 ppm | 92021.6965 | +8650.2142 ppm | 3.3387 ppm |
| ${}^{99}$In | 99 | 50 | 23.7126 | 822.0960 | -971155.8641 ppm | 92954.9298 | +8663.4079 ppm | 3.2345 ppm |
| ${}^{100}$In | 100 | 51 | 30.0299 | 832.9749 | -963948.6637 ppm | 93888.1780 | +8625.9204 ppm | 0.0240 ppm |
| ${}^{101}$In | 101 | 52 | 36.3325 | 845.4130 | -957023.9181 ppm | 94821.4408 | +8606.1152 ppm | 0.1240 ppm |
| ${}^{102}$In | 102 | 53 | 42.6210 | 855.6343 | -950187.8223 ppm | 95754.7177 | +8563.2974 ppm | 0.0482 ppm |
| ${}^{103}$In | 103 | 54 | 48.8956 | 867.6431 | -943645.5153 ppm | 96688.0086 | +8540.2588 ppm | 0.0937 ppm |
| ${}^{104}$In | 104 | 55 | 55.1566 | 877.2648 | -937126.6639 ppm | 97621.3130 | +8492.9305 ppm | 0.0597 ppm |
| ${}^{105}$In | 105 | 56 | 61.4042 | 888.7940 | -930912.8530 ppm | 98554.6308 | +8466.3238 ppm | 0.1048 ppm |
| ${}^{106}$In | 106 | 57 | 67.6389 | 897.8329 | -924664.2611 ppm | 99487.9615 | +8414.8943 ppm | 0.1239 ppm |
| ${}^{107}$In | 107 | 58 | 73.8608 | 908.8627 | -918732.6938 ppm | 100421.3050 | +8384.7133 ppm | 0.0969 ppm |
| ${}^{108}$In | 108 | 59 | 80.0703 | 917.4872 | -912728.7293 ppm | 101354.6610 | +8331.0843 ppm | 0.0860 ppm |
| ${}^{109}$In | 109 | 60 | 86.2675 | 927.9282 | -907032.1317 ppm | 102288.0292 | +8296.6146 ppm | 0.0391 ppm |
| ${}^{110}$In | 110 | 61 | 92.4528 | 935.9800 | -901223.5482 ppm | 103221.4093 | +8239.3569 ppm | 0.1128 ppm |
| ${}^{111}$In | 111 | 62 | 98.6263 | 945.9733 | -895740.8945 ppm | 104154.8012 | +8202.1937 ppm | 0.0331 ppm |
| ${}^{112}$In | 112 | 63 | 104.7884 | 953.6427 | -890117.7501 ppm | 105088.2046 | +8143.3266 ppm | 0.0408 ppm |
| ${}^{113}$In | 113 | 64 | 110.9392 | 963.0911 | -884809.1915 ppm | 106021.6192 | +8102.6612 ppm | 0.0018 ppm |
| ${}^{114}$In | 114 | 65 | 117.0790 | 970.3651 | -879345.3683 ppm | 106955.0448 | +8042.1547 ppm | 0.0028 ppm |
| ${}^{115}$In | 115 | 66 | 123.2080 | 979.4029 | -874200.8738 ppm | 107888.4812 | +7999.4146 ppm | 0.0001 ppm |
| ${}^{116}$In | 116 | 67 | 129.3264 | 986.1877 | -868862.2497 ppm | 108821.9282 | +7936.4741 ppm | 0.0020 ppm |
| ${}^{117}$In | 117 | 68 | 135.4344 | 994.9522 | -863878.4536 ppm | 109755.3856 | +7893.0318 ppm | 0.0448 ppm |
| ${}^{118}$In | 118 | 69 | 141.5323 | 1001.3087 | -858652.7276 ppm | 110688.8532 | +7828.3203 ppm | 0.0706 ppm |
| ${}^{119}$In | 119 | 70 | 147.6201 | 1009.8505 | -853819.8726 ppm | 111622.3308 | +7784.6731 ppm | 0.0660 ppm |
| ${}^{120}$In | 120 | 71 | 153.6981 | 1015.9509 | -848715.0412 ppm | 112555.8183 | +7719.8141 ppm | 0.3582 ppm |
| ${}^{121}$In | 121 | 72 | 159.7665 | 1024.1291 | -843997.7097 ppm | 113489.3153 | +7674.7054 ppm | 0.2434 ppm |
| ${}^{122}$In | 122 | 73 | 165.8254 | 1029.9372 | -838994.6134 ppm | 114422.8218 | +7609.3897 ppm | 0.4408 ppm |
| ${}^{123}$In | 123 | 74 | 171.8751 | 1037.8662 | -834395.6866 ppm | 115356.3375 | +7563.8848 ppm | 0.1732 ppm |
| ${}^{124}$In | 124 | 75 | 177.9157 | 1043.3762 | -829480.7844 ppm | 116289.8623 | +7498.0789 ppm | 0.2648 ppm |
| ${}^{125}$In | 125 | 76 | 183.9473 | 1050.9921 | -824977.4202 ppm | 117223.3961 | +7451.6385 ppm | 0.0152 ppm |
| ${}^{126}$In | 126 | 77 | 189.9702 | 1056.4604 | -820182.3647 ppm | 118156.9387 | +7387.5664 ppm | 0.0357 ppm |
| ${}^{127}$In | 127 | 78 | 195.9845 | 1063.6023 | -815735.1838 ppm | 119090.4898 | +7338.8384 ppm | 0.0846 ppm |
| ${}^{128}$In | 128 | 79 | 201.9903 | 1068.9838 | -811044.5852 ppm | 120024.0494 | +7276.0634 ppm | 0.0111 ppm |
| ${}^{129}$In | 129 | 80 | 207.9878 | 1075.6999 | -806648.8925 ppm | 120957.6174 | +7225.5274 ppm | 0.0164 ppm |
| ${}^{130}$In | 130 | 81 | 213.9771 | 1080.8429 | -802027.5712 ppm | 121891.1935 | +7162.7461 ppm | 0.0148 ppm |
| ${}^{131}$In | 131 | 82 | 219.9584 | 1087.0320 | -797652.3408 ppm | 122824.7776 | +7109.6320 ppm | 0.0181 ppm |
| ${}^{132}$In | 132 | 83 | 225.9318 | 1089.4905 | -792626.1979 ppm | 123758.3696 | +7026.8182 ppm | 0.4885 ppm |
| ${}^{133}$In | 133 | 84 | 231.8975 | 1092.8610 | -787807.0011 ppm | 124691.9694 | +6952.5696 ppm | 1.6173 ppm |
| ${}^{134}$In | 134 | 85 | 237.8555 | 1095.1820 | -782816.4720 ppm | 125625.5768 | +6871.4346 ppm | 1.6051 ppm |
| ${}^{135}$In | 135 | 86 | 243.8060 | 1098.3600 | -778027.2071 ppm | 126559.1917 | +6798.4625 ppm | 2.3861 ppm |
| ${}^{136}$In | 136 | 87 | 249.7492 | 1100.3760 | -773032.8388 ppm | 127492.8139 | +6716.4460 ppm | 2.3684 ppm |
| ${}^{137}$In | 137 | 88 | 255.6852 | 1103.2610 | -768245.9965 ppm | 128426.4434 | +6643.5856 ppm | 3.1323 ppm |

### Tin (Z = 50)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{99}$Sn | 99 | 49 | 6.2125 | 807.9390 | -992310.6404 ppm | 92971.6476 | +8698.1497 ppm | 6.3164 ppm |
| ${}^{100}$Sn | 100 | 50 | 12.5775 | 825.1626 | -984757.5686 ppm | 93904.8481 | +8728.8227 ppm | 2.5782 ppm |
| ${}^{101}$Sn | 101 | 51 | 18.9273 | 836.3914 | -977370.2931 ppm | 94838.0637 | +8694.5291 ppm | 3.1908 ppm |
| ${}^{102}$Sn | 102 | 52 | 25.2623 | 849.0920 | -970247.8720 ppm | 95771.2941 | +8676.6976 ppm | 1.0543 ppm |
| ${}^{103}$Sn | 103 | 53 | 31.5828 | 859.3290 | -963247.1219 ppm | 96704.5390 | +8633.3613 ppm | 1.0493 ppm |
| ${}^{104}$Sn | 104 | 54 | 37.8892 | 871.9268 | -956545.4697 ppm | 97637.7981 | +8615.7640 ppm | 0.0593 ppm |
| ${}^{105}$Sn | 105 | 55 | 44.1817 | 881.7090 | -949890.8803 ppm | 98571.0710 | +8569.5053 ppm | 0.0406 ppm |
| ${}^{106}$Sn | 106 | 56 | 50.4606 | 893.7961 | -943543.5015 ppm | 99504.3575 | +8547.8154 ppm | 0.0516 ppm |
| ${}^{107}$Sn | 107 | 57 | 56.7263 | 903.0259 | -937182.0338 ppm | 100437.6573 | +8497.7294 ppm | 0.0533 ppm |
| ${}^{108}$Sn | 108 | 58 | 62.9789 | 914.6549 | -931144.6237 ppm | 101370.9700 | +8472.7692 ppm | 0.0535 ppm |
| ${}^{109}$Sn | 109 | 59 | 69.2188 | 923.2865 | -925029.9413 ppm | 102304.2955 | +8418.5952 ppm | 0.0783 ppm |
| ${}^{110}$Sn | 110 | 60 | 75.4463 | 934.5696 | -919271.6000 ppm | 103237.6335 | +8391.6445 ppm | 0.1346 ppm |
| ${}^{111}$Sn | 111 | 61 | 81.6616 | 942.7375 | -913378.2572 ppm | 104170.9836 | +8334.8900 ppm | 0.0516 ppm |
| ${}^{112}$Sn | 112 | 62 | 87.8649 | 953.5253 | -907852.6145 ppm | 105104.3458 | +8304.6059 ppm | 0.0028 ppm |
| ${}^{113}$Sn | 113 | 63 | 94.0564 | 961.2697 | -902153.9561 ppm | 106037.7196 | +8245.7911 ppm | 0.0150 ppm |
| ${}^{114}$Sn | 114 | 64 | 100.2365 | 971.5726 | -896830.6431 ppm | 106971.1050 | +8212.4295 ppm | 0.0003 ppm |
| ${}^{115}$Sn | 115 | 65 | 106.4053 | 979.1181 | -891325.3133 ppm | 107904.5015 | +8153.7783 ppm | 0.0001 ppm |
| ${}^{116}$Sn | 116 | 66 | 112.5631 | 988.6815 | -886148.2386 ppm | 108837.9092 | +8115.0853 ppm | 0.0009 ppm |
| ${}^{117}$Sn | 117 | 67 | 118.7101 | 995.6246 | -880768.2240 ppm | 109771.3277 | +8052.8949 ppm | 0.0044 ppm |
| ${}^{118}$Sn | 118 | 68 | 124.8464 | 1004.9510 | -875768.6443 ppm | 110704.7567 | +8013.7322 ppm | 0.0045 ppm |
| ${}^{119}$Sn | 119 | 69 | 130.9724 | 1011.4345 | -870508.3191 ppm | 111638.1962 | +7949.4484 ppm | 0.0065 ppm |
| ${}^{120}$Sn | 120 | 70 | 137.0881 | 1020.5386 | -865670.8718 ppm | 112571.6460 | +7909.9788 ppm | 0.0082 ppm |
| ${}^{121}$Sn | 121 | 71 | 143.1937 | 1026.7088 | -860531.3036 ppm | 113505.1057 | +7844.9947 ppm | 0.0087 ppm |
| ${}^{122}$Sn | 122 | 72 | 149.2896 | 1035.5234 | -855831.7756 ppm | 114438.5753 | +7804.6351 ppm | 0.0215 ppm |
| ${}^{123}$Sn | 123 | 73 | 155.3758 | 1041.4694 | -850811.0325 ppm | 115372.0545 | +7739.7652 ppm | 0.0217 ppm |
| ${}^{124}$Sn | 124 | 74 | 161.4525 | 1049.9576 | -846229.5453 ppm | 116305.5433 | +7698.2211 ppm | 0.0114 ppm |
| ${}^{125}$Sn | 125 | 75 | 167.5198 | 1055.6911 | -841317.3612 ppm | 117239.0413 | +7633.5654 ppm | 0.0114 ppm |
| ${}^{126}$Sn | 126 | 76 | 173.5781 | 1063.8839 | -836844.8834 ppm | 118172.5485 | +7591.1451 ppm | 0.0911 ppm |
| ${}^{127}$Sn | 127 | 77 | 179.6274 | 1069.4096 | -832031.2751 ppm | 119106.0646 | +7526.7382 ppm | 0.0780 ppm |
| ${}^{128}$Sn | 128 | 78 | 185.6678 | 1077.3728 | -827666.1235 ppm | 120039.5896 | +7484.0248 ppm | 0.1484 ppm |
| ${}^{129}$Sn | 129 | 79 | 191.6996 | 1082.6733 | -822938.6187 ppm | 120973.1232 | +7419.7074 ppm | 0.1438 ppm |
| ${}^{130}$Sn | 130 | 80 | 197.7229 | 1090.2862 | -818650.4503 ppm | 121906.6653 | +7375.7029 ppm | 0.0155 ppm |
| ${}^{131}$Sn | 131 | 81 | 203.7378 | 1095.4899 | -814021.2527 ppm | 122840.2158 | +7312.5384 ppm | 0.0297 ppm |
| ${}^{132}$Sn | 132 | 82 | 209.7445 | 1102.8432 | -809814.7137 ppm | 123773.7745 | +7268.0216 ppm | 0.0161 ppm |
| ${}^{133}$Sn | 133 | 83 | 215.7432 | 1105.2418 | -804800.0264 ppm | 124707.3413 | +7183.9358 ppm | 0.0154 ppm |
| ${}^{134}$Sn | 134 | 84 | 221.7339 | 1108.8730 | -800036.7386 ppm | 125640.9161 | +7111.1268 ppm | 0.0254 ppm |
| ${}^{135}$Sn | 135 | 85 | 227.7168 | 1111.1428 | -795060.7738 ppm | 126574.4986 | +7028.5569 ppm | 0.0245 ppm |
| ${}^{136}$Sn | 136 | 86 | 233.6920 | 1114.7920 | -790371.6891 ppm | 127508.0888 | +6957.9200 ppm | 1.5816 ppm |
| ${}^{137}$Sn | 137 | 87 | 239.6596 | 1116.8240 | -785409.6737 ppm | 128441.6866 | +6876.0811 ppm | 2.3513 ppm |
| ${}^{138}$Sn | 138 | 88 | 245.6199 | 1120.2840 | -780752.1428 ppm | 129375.2918 | +6806.3101 ppm | 3.1098 ppm |
| ${}^{139}$Sn | 139 | 89 | 251.5728 | 1122.1470 | -775811.1860 ppm | 130308.9042 | +6725.4694 ppm | 3.0873 ppm |
| ${}^{140}$Sn | 140 | 90 | 257.5186 | 1125.3200 | -771159.7045 ppm | 131242.5239 | +6656.5056 ppm | 2.3006 ppm |

### Antimony (Z = 51)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{102}$Sb | 102 | 51 | 7.6014 | 834.4620 | -990890.7121 ppm | 95788.1727 | +8707.4845 ppm | 4.2081 ppm |
| ${}^{103}$Sb | 103 | 52 | 13.9688 | 848.1020 | -983529.3810 ppm | 96721.3707 | +8699.2642 ppm | 3.1281 ppm |
| ${}^{104}$Sb | 104 | 53 | 20.3214 | 858.8320 | -976338.2982 ppm | 97654.5835 | +8660.6666 ppm | 1.0487 ppm |
| ${}^{105}$Sb | 105 | 54 | 26.6597 | 871.6042 | -969413.1138 ppm | 98587.8107 | +8644.5724 ppm | 0.2233 ppm |
| ${}^{106}$Sb | 106 | 55 | 32.9838 | 882.1333 | -962609.0891 ppm | 99521.0520 | +8605.7964 ppm | 0.0755 ppm |
| ${}^{107}$Sb | 107 | 56 | 39.2941 | 894.3846 | -956065.8169 ppm | 100454.3071 | +8585.3214 ppm | 0.0416 ppm |
| ${}^{108}$Sb | 108 | 57 | 45.5908 | 904.2480 | -949581.5176 ppm | 101387.5758 | +8541.4023 ppm | 0.0547 ppm |
| ${}^{109}$Sb | 109 | 58 | 51.8743 | 916.1250 | -943376.3741 ppm | 102320.8577 | +8518.4339 ppm | 0.0519 ppm |
| ${}^{110}$Sb | 110 | 59 | 58.1448 | 925.3950 | -937167.5415 ppm | 103254.1526 | +8470.3309 ppm | 0.0582 ppm |
| ${}^{111}$Sb | 111 | 60 | 64.4027 | 936.8534 | -931256.4119 ppm | 104187.4602 | +8444.5760 ppm | 0.0857 ppm |
| ${}^{112}$Sb | 112 | 61 | 70.6480 | 945.6869 | -925294.4888 ppm | 105120.7803 | +8394.0085 ppm | 0.1710 ppm |
| ${}^{113}$Sb | 113 | 62 | 76.8812 | 956.5762 | -919628.7969 ppm | 106054.1125 | +8364.1613 ppm | 0.1635 ppm |
| ${}^{114}$Sb | 114 | 63 | 83.1024 | 964.7272 | -913859.1928 ppm | 106987.4568 | +8308.9265 ppm | 0.1863 ppm |
| ${}^{115}$Sb | 115 | 64 | 89.3118 | 975.3053 | -908426.7764 ppm | 107920.8127 | +8277.6260 ppm | 0.1497 ppm |
| ${}^{116}$Sb | 116 | 65 | 95.5098 | 983.1952 | -902857.7181 ppm | 108854.1802 | +8221.8670 ppm | 0.0477 ppm |
| ${}^{117}$Sb | 117 | 66 | 101.6965 | 993.0841 | -897595.2455 ppm | 109787.5589 | +8185.6718 ppm | 0.0775 ppm |
| ${}^{118}$Sb | 118 | 67 | 107.8722 | 1000.5120 | -892183.0259 ppm | 110720.9487 | +8127.6006 ppm | 0.0275 ppm |
| ${}^{119}$Sb | 119 | 68 | 114.0370 | 1010.0627 | -887099.1008 ppm | 111654.3493 | +8089.9245 ppm | 0.0632 ppm |
| ${}^{120}$Sb | 120 | 69 | 120.1912 | 1017.0756 | -881826.7261 ppm | 112587.7605 | +8030.0670 ppm | 0.0645 ppm |
| ${}^{121}$Sb | 121 | 70 | 126.3349 | 1026.3289 | -876906.0522 ppm | 113521.1822 | +7991.3456 ppm | 0.0222 ppm |
| ${}^{122}$Sb | 122 | 71 | 132.4684 | 1033.1353 | -871780.2358 ppm | 114454.6142 | +7931.6284 ppm | 0.0220 ppm |
| ${}^{123}$Sb | 123 | 72 | 138.5918 | 1042.0953 | -867006.6036 ppm | 115388.0562 | +7891.9319 ppm | 0.0118 ppm |
| ${}^{124}$Sb | 124 | 73 | 144.7054 | 1048.5628 | -861996.4852 ppm | 116321.5080 | +7831.1959 ppm | 0.0118 ppm |
| ${}^{125}$Sb | 125 | 74 | 150.8092 | 1057.2702 | -857359.8043 ppm | 117254.9696 | +7790.9181 ppm | 0.0216 ppm |
| ${}^{126}$Sb | 126 | 75 | 156.9036 | 1063.4795 | -852462.0635 ppm | 118188.4406 | +7729.8968 ppm | 0.2715 ppm |
| ${}^{127}$Sb | 127 | 76 | 162.9886 | 1071.8560 | -847937.9882 ppm | 119121.9211 | +7688.3911 ppm | 0.0430 ppm |
| ${}^{128}$Sb | 128 | 77 | 169.0644 | 1077.8589 | -843147.9191 ppm | 120055.4107 | +7627.5371 ppm | 0.1577 ppm |
| ${}^{129}$Sb | 129 | 78 | 175.1312 | 1085.9297 | -838726.9328 ppm | 120988.9093 | +7585.0567 ppm | 0.1768 ppm |
| ${}^{130}$Sb | 130 | 79 | 181.1892 | 1091.6573 | -834023.7725 ppm | 121922.4167 | +7523.7938 ppm | 0.1174 ppm |
| ${}^{131}$Sb | 131 | 80 | 187.2384 | 1099.4244 | -829694.1436 ppm | 122855.9329 | +7480.3897 ppm | 0.0171 ppm |
| ${}^{132}$Sb | 132 | 81 | 193.2791 | 1105.1496 | -825110.4601 ppm | 123789.4577 | +7420.9729 ppm | 0.0201 ppm |
| ${}^{133}$Sb | 133 | 82 | 199.3114 | 1112.5091 | -820845.1723 ppm | 124722.9908 | +7375.8182 ppm | 0.0253 ppm |
| ${}^{134}$Sb | 134 | 83 | 205.3354 | 1115.6759 | -815954.2687 ppm | 125656.5322 | +7297.5480 ppm | 0.0246 ppm |
| ${}^{135}$Sb | 135 | 84 | 211.3513 | 1119.4186 | -811195.4848 ppm | 126590.0817 | +7225.1235 ppm | 0.0210 ppm |
| ${}^{136}$Sb | 136 | 85 | 217.3592 | 1122.3064 | -806328.1405 ppm | 127523.6393 | +7147.0337 ppm | 0.0460 ppm |
| ${}^{137}$Sb | 137 | 86 | 223.3592 | 1125.9313 | -801622.6900 ppm | 128457.2046 | +7075.9707 ppm | 0.4090 ppm |
| ${}^{138}$Sb | 138 | 87 | 229.3515 | 1128.5640 | -796775.7903 ppm | 129390.7778 | +6998.4475 ppm | 2.3343 ppm |
| ${}^{139}$Sb | 139 | 88 | 235.3362 | 1132.0160 | -792108.7362 ppm | 130324.3585 | +6928.4137 ppm | 3.0875 ppm |
| ${}^{140}$Sb | 140 | 89 | 241.3135 | 1134.4200 | -787280.3114 ppm | 131257.9467 | +6851.2559 ppm | 4.6016 ppm |
| ${}^{141}$Sb | 141 | 90 | 247.2833 | 1137.7290 | -782651.8048 ppm | 132191.5422 | +6781.4623 ppm | 3.8097 ppm |
| ${}^{142}$Sb | 142 | 91 | 253.2460 | 1139.8340 | -777822.0496 ppm | 133125.1450 | +6704.4929 ppm | 2.2682 ppm |

### Tellurium (Z = 52)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{104}$Te | 104 | 52 | 2.4533 | 848.3619 | -997108.1505 ppm | 97671.6692 | +8736.4074 ppm | 3.2802 ppm |
| ${}^{105}$Te | 105 | 53 | 8.8382 | 859.6179 | -989718.4288 ppm | 98604.8498 | +8703.2735 ppm | 3.0691 ppm |
| ${}^{106}$Te | 106 | 54 | 15.2084 | 873.0974 | -982581.0751 ppm | 99538.0450 | +8693.6403 ppm | 1.0188 ppm |
| ${}^{107}$Te | 107 | 55 | 21.5642 | 883.6060 | -975595.1915 ppm | 100471.2546 | +8654.2452 ppm | 1.0100 ppm |
| ${}^{108}$Te | 108 | 56 | 27.9060 | 896.8020 | -968882.7918 ppm | 101404.4783 | +8642.6791 ppm | 0.0538 ppm |
| ${}^{109}$Te | 109 | 57 | 34.2339 | 906.8070 | -962247.8351 ppm | 102337.7158 | +8599.7402 ppm | 0.0432 ppm |
| ${}^{110}$Te | 110 | 58 | 40.5484 | 919.3928 | -955896.5613 ppm | 103270.9667 | +8583.1325 ppm | 0.0642 ppm |
| ${}^{111}$Te | 111 | 59 | 46.8496 | 928.8217 | -949560.1693 ppm | 104204.2309 | +8536.1365 ppm | 0.0622 ppm |
| ${}^{112}$Te | 112 | 60 | 53.1379 | 940.8731 | -943522.7931 ppm | 105137.5081 | +8515.4716 ppm | 0.0804 ppm |
| ${}^{113}$Te | 113 | 61 | 59.4135 | 949.7239 | -937441.3345 ppm | 106070.7979 | +8464.6047 ppm | 0.2657 ppm |
| ${}^{114}$Te | 114 | 62 | 65.6766 | 961.3379 | -931682.0894 ppm | 107004.1002 | +8441.0070 ppm | 0.2302 ppm |
| ${}^{115}$Te | 115 | 63 | 71.9275 | 969.5823 | -925815.9594 ppm | 107937.4147 | +8386.1879 ppm | 0.2611 ppm |
| ${}^{116}$Te | 116 | 64 | 78.1665 | 980.8546 | -920307.7534 ppm | 108870.7411 | +8360.7038 ppm | 0.2242 ppm |
| ${}^{117}$Te | 117 | 65 | 84.3938 | 988.7577 | -914646.6683 ppm | 109804.0793 | +8304.5643 ppm | 0.1235 ppm |
| ${}^{118}$Te | 118 | 66 | 90.6095 | 999.4242 | -909338.2885 ppm | 110737.4290 | +8274.8518 ppm | 0.1667 ppm |
| ${}^{119}$Te | 119 | 67 | 96.8140 | 1006.9873 | -903857.7959 ppm | 111670.7899 | +8217.4889 ppm | 0.0657 ppm |
| ${}^{120}$Te | 120 | 68 | 103.0074 | 1017.2383 | -898738.1947 ppm | 112604.1620 | +8185.4440 ppm | 0.0157 ppm |
| ${}^{121}$Te | 121 | 69 | 109.1899 | 1024.4906 | -893420.2687 ppm | 113537.5448 | +8127.1814 ppm | 0.2294 ppm |
| ${}^{122}$Te | 122 | 70 | 115.3618 | 1034.3320 | -888467.3302 ppm | 114470.9384 | +8092.9554 ppm | 0.0119 ppm |
| ${}^{123}$Te | 123 | 71 | 121.5232 | 1041.2611 | -883292.2444 ppm | 115404.3424 | +8033.7317 ppm | 0.0118 ppm |
| ${}^{124}$Te | 124 | 72 | 127.6744 | 1050.6855 | -878484.6721 ppm | 116337.7566 | +7997.3483 ppm | 0.0117 ppm |
| ${}^{125}$Te | 125 | 73 | 133.8155 | 1057.2545 | -873431.1624 ppm | 117271.1810 | +7936.8951 ppm | 0.0116 ppm |
| ${}^{126}$Te | 126 | 74 | 139.9467 | 1066.3682 | -868763.2924 ppm | 118204.6152 | +7899.3571 ppm | 0.0115 ppm |
| ${}^{127}$Te | 127 | 75 | 146.0681 | 1072.6558 | -863825.7479 ppm | 119138.0592 | +7838.3977 ppm | 0.0115 ppm |
| ${}^{128}$Te | 128 | 76 | 152.1800 | 1081.4405 | -859280.2666 ppm | 120071.5127 | +7799.5943 ppm | 0.0059 ppm |
| ${}^{129}$Te | 129 | 77 | 158.2825 | 1087.5229 | -854455.8980 ppm | 121004.9756 | +7738.7918 ppm | 0.0059 ppm |
| ${}^{130}$Te | 130 | 78 | 164.3758 | 1095.9423 | -850014.1355 ppm | 121938.4477 | +7698.4647 ppm | 0.0001 ppm |
| ${}^{131}$Te | 131 | 79 | 170.4601 | 1101.8716 | -845299.4939 ppm | 122871.9289 | +7638.2515 ppm | 0.0005 ppm |
| ${}^{132}$Te | 132 | 80 | 176.5355 | 1109.9201 | -840947.6078 ppm | 123805.4190 | +7596.4029 ppm | 0.0284 ppm |
| ${}^{133}$Te | 133 | 81 | 182.6021 | 1115.7404 | -836340.0128 ppm | 124738.9178 | +7537.1209 ppm | 0.0167 ppm |
| ${}^{134}$Te | 134 | 82 | 188.6601 | 1123.4083 | -832064.5660 ppm | 125672.4252 | +7493.7187 ppm | 0.0220 ppm |
| ${}^{135}$Te | 135 | 83 | 194.7096 | 1126.6747 | -827182.0437 ppm | 126605.9411 | +7415.7426 ppm | 0.0137 ppm |
| ${}^{136}$Te | 136 | 84 | 200.7509 | 1131.4425 | -822570.8711 ppm | 127539.4653 | +7350.9316 ppm | 0.0180 ppm |
| ${}^{137}$Te | 137 | 85 | 206.7839 | 1134.3923 | -817713.9220 ppm | 128472.9976 | +7272.7770 ppm | 0.0165 ppm |
| ${}^{138}$Te | 138 | 86 | 212.8089 | 1138.8558 | -813137.9413 ppm | 129406.5380 | +7207.6911 ppm | 0.0295 ppm |
| ${}^{139}$Te | 139 | 87 | 218.8261 | 1141.4363 | -808288.8406 ppm | 130340.0863 | +7128.9520 ppm | 0.0274 ppm |
| ${}^{140}$Te | 140 | 88 | 224.8354 | 1145.6699 | -803752.0229 ppm | 131273.6424 | +7064.1771 ppm | 0.1103 ppm |
| ${}^{141}$Te | 141 | 89 | 230.8371 | 1148.0220 | -798926.2440 ppm | 132207.2061 | +6986.1152 ppm | 3.0437 ppm |
| ${}^{142}$Te | 142 | 90 | 236.8313 | 1152.0460 | -794425.5237 ppm | 133140.7774 | +6921.2326 ppm | 3.7830 ppm |
| ${}^{143}$Te | 143 | 91 | 242.8180 | 1154.0100 | -789587.6112 ppm | 134074.3561 | +6842.9564 ppm | 3.7564 ppm |
| ${}^{144}$Te | 144 | 92 | 248.7975 | 1157.7600 | -785104.4640 ppm | 135007.9420 | +6778.6619 ppm | 2.2367 ppm |
| ${}^{145}$Te | 145 | 93 | 254.7697 | 1159.7100 | -780315.9989 ppm | 135941.5352 | +6701.1451 ppm | 2.2212 ppm |

### Iodine (Z = 53)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{106}$I | 106 | 53 | -2.8655 | 857.4340 | -1003341.8934 ppm | 99555.3365 | +8716.3530 ppm | 4.0489 ppm |
| ${}^{107}$I | 107 | 54 | 3.5368 | 871.6220 | -995942.2895 ppm | 100488.4997 | +8713.6773 ppm | 3.0108 ppm |
| ${}^{108}$I | 108 | 55 | 9.9244 | 883.0080 | -988760.6926 ppm | 101421.6775 | +8683.2179 ppm | 1.0098 ppm |
| ${}^{109}$I | 109 | 56 | 16.2977 | 895.9818 | -981810.2581 ppm | 102354.8697 | +8668.9656 ppm | 0.0663 ppm |
| ${}^{110}$I | 110 | 57 | 22.6569 | 906.8484 | -975015.7560 ppm | 103288.0759 | +8634.3629 ppm | 0.6048 ppm |
| ${}^{111}$I | 111 | 58 | 29.0024 | 919.4057 | -968455.2526 ppm | 104221.2958 | +8617.0172 ppm | 0.0460 ppm |
| ${}^{112}$I | 112 | 59 | 35.3345 | 929.5866 | -961989.0695 ppm | 105154.5292 | +8577.1200 ppm | 0.0983 ppm |
| ${}^{113}$I | 113 | 60 | 41.6533 | 941.7141 | -955768.6519 ppm | 106087.7758 | +8556.7176 ppm | 0.0762 ppm |
| ${}^{114}$I | 114 | 61 | 47.9592 | 951.3048 | -949585.8955 ppm | 107021.0353 | +8512.6845 ppm | 0.1887 ppm |
| ${}^{115}$I | 115 | 62 | 54.2524 | 963.0750 | -943667.5248 ppm | 107954.3075 | +8490.0674 ppm | 0.2698 ppm |
| ${}^{116}$I | 116 | 63 | 60.5332 | 972.2292 | -937737.7398 ppm | 108887.5921 | +8443.5212 ppm | 0.6949 ppm |
| ${}^{117}$I | 117 | 64 | 66.8018 | 983.3184 | -932064.9526 ppm | 109820.8890 | +8415.7998 ppm | 0.2347 ppm |
| ${}^{118}$I | 118 | 65 | 73.0584 | 991.9222 | -926346.6187 ppm | 110754.1977 | +8365.8376 ppm | 0.1799 ppm |
| ${}^{119}$I | 119 | 66 | 79.3033 | 1002.8002 | -920918.1057 ppm | 111687.5182 | +8337.5236 ppm | 0.1960 ppm |
| ${}^{120}$I | 120 | 67 | 85.5367 | 1010.8409 | -915380.6038 ppm | 112620.8503 | +8284.1708 ppm | 0.1352 ppm |
| ${}^{121}$I | 121 | 68 | 91.7589 | 1021.4107 | -910164.5708 ppm | 113554.1936 | +8254.4413 ppm | 0.0419 ppm |
| ${}^{122}$I | 122 | 69 | 97.9699 | 1029.3157 | -904820.3408 ppm | 114487.5479 | +8201.6354 ppm | 0.0456 ppm |
| ${}^{123}$I | 123 | 70 | 104.1701 | 1039.2503 | -899764.1988 ppm | 115420.9132 | +8167.6571 ppm | 0.0322 ppm |
| ${}^{124}$I | 124 | 71 | 110.3596 | 1046.7436 | -894568.6552 ppm | 116354.2891 | +8112.9944 ppm | 0.0199 ppm |
| ${}^{125}$I | 125 | 72 | 116.5386 | 1056.2864 | -889671.3943 ppm | 117287.6755 | +8077.0548 ppm | 0.0116 ppm |
| ${}^{126}$I | 126 | 73 | 122.7073 | 1063.4322 | -884611.9808 ppm | 118221.0722 | +8021.1704 ppm | 0.0322 ppm |
| ${}^{127}$I | 127 | 74 | 128.8660 | 1072.5762 | -879853.8019 ppm | 119154.4790 | +7983.2918 ppm | 0.0306 ppm |
| ${}^{128}$I | 128 | 75 | 135.0147 | 1079.4024 | -874917.2175 ppm | 120087.8957 | +7926.4789 ppm | 0.0304 ppm |
| ${}^{129}$I | 129 | 76 | 141.1536 | 1088.2428 | -870292.1875 ppm | 121021.3222 | +7887.5376 ppm | 0.0263 ppm |
| ${}^{130}$I | 130 | 77 | 147.2830 | 1094.7431 | -865463.4560 ppm | 121954.7583 | +7829.7839 ppm | 0.0261 ppm |
| ${}^{131}$I | 131 | 78 | 153.4029 | 1103.3210 | -860962.5759 ppm | 122888.2038 | +7790.1612 ppm | 0.0050 ppm |
| ${}^{132}$I | 132 | 79 | 159.5136 | 1109.6531 | -856249.1196 ppm | 123821.6585 | +7732.7952 ppm | 0.0331 ppm |
| ${}^{133}$I | 133 | 80 | 165.6152 | 1117.8782 | -851848.6061 ppm | 124755.1223 | +7691.7755 ppm | 0.0477 ppm |
| ${}^{134}$I | 134 | 81 | 171.7079 | 1124.1357 | -847253.4180 ppm | 125688.5950 | +7635.5448 ppm | 0.0389 ppm |
| ${}^{135}$I | 135 | 82 | 177.7918 | 1131.9427 | -842932.1922 ppm | 126622.0766 | +7592.6436 ppm | 0.0164 ppm |
| ${}^{136}$I | 136 | 83 | 183.8670 | 1135.7801 | -838113.9073 ppm | 127555.5668 | +7518.8501 ppm | 0.1121 ppm |
| ${}^{137}$I | 137 | 84 | 189.9337 | 1140.6625 | -833488.2126 ppm | 128489.0655 | +7454.4607 ppm | 0.0657 ppm |
| ${}^{138}$I | 138 | 85 | 195.9921 | 1144.3574 | -828731.7161 ppm | 129422.5725 | +7381.7626 ppm | 0.0464 ppm |
| ${}^{139}$I | 139 | 86 | 202.0423 | 1148.9198 | -824145.8646 ppm | 130356.0877 | +7316.9313 ppm | 0.0310 ppm |
| ${}^{140}$I | 140 | 87 | 208.0844 | 1152.1264 | -819391.0109 ppm | 131289.6111 | +7242.6152 ppm | 0.0929 ppm |
| ${}^{141}$I | 141 | 88 | 214.1185 | 1156.5181 | -814859.3621 ppm | 132223.1424 | +7178.5123 ppm | 0.1206 ppm |
| ${}^{142}$I | 142 | 89 | 220.1448 | 1159.4657 | -810132.5515 ppm | 133156.6815 | +7104.3753 ppm | 0.0373 ppm |
| ${}^{143}$I | 143 | 90 | 226.1634 | 1163.5910 | -805633.2523 ppm | 134090.2283 | +7039.7374 ppm | 1.5041 ppm |
| ${}^{144}$I | 144 | 91 | 232.1744 | 1166.1120 | -800898.7008 ppm | 135023.7827 | +6965.1971 ppm | 2.9802 ppm |
| ${}^{145}$I | 145 | 92 | 238.1780 | 1170.0050 | -796429.9564 ppm | 135957.3446 | +6901.1379 ppm | 3.7046 ppm |
| ${}^{146}$I | 146 | 93 | 244.1742 | 1172.5260 | -791753.7191 ppm | 136890.9138 | +6827.7226 ppm | 2.2061 ppm |
| ${}^{147}$I | 147 | 94 | 250.1632 | 1176.1470 | -787302.8133 ppm | 137824.4903 | +6764.5582 ppm | 2.1910 ppm |

### Xenon (Z = 54)

_43 of 43 isotopes with a framework prediction; 43 of 43 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{108}$Xe | 108 | 54 | -8.3539 | 872.0880 | -1009579.2122 ppm | 101439.1735 | +8755.5070 ppm | 3.7739 ppm |
| ${}^{109}$Xe | 109 | 55 | -1.9344 | 883.6965 | -1002189.0276 ppm | 102372.3195 | +8726.5800 ppm | 2.9571 ppm |
| ${}^{110}$Xe | 110 | 56 | 4.4705 | 897.5209 | -995019.0953 ppm | 103305.4800 | +8720.1448 ppm | 0.9861 ppm |
| ${}^{111}$Xe | 111 | 57 | 10.8611 | 908.2020 | -988041.1096 ppm | 104238.6548 | +8683.1635 ppm | 1.1177 ppm |
| ${}^{112}$Xe | 112 | 58 | 17.2377 | 921.7672 | -981299.2701 ppm | 105171.8436 | +8675.1090 ppm | 0.0794 ppm |
| ${}^{113}$Xe | 113 | 59 | 23.6006 | 932.0158 | -974677.8518 ppm | 106105.0461 | +8635.4095 ppm | 0.0650 ppm |
| ${}^{114}$Xe | 114 | 60 | 29.9501 | 944.9694 | -968305.7153 ppm | 107038.2620 | +8622.2402 ppm | 0.1053 ppm |
| ${}^{115}$Xe | 115 | 61 | 36.2864 | 954.6116 | -961988.2621 ppm | 107971.4911 | +8578.2232 ppm | 0.1131 ppm |
| ${}^{116}$Xe | 116 | 62 | 42.6098 | 967.0730 | -955939.3680 ppm | 108904.7331 | +8561.4158 ppm | 0.1205 ppm |
| ${}^{117}$Xe | 117 | 63 | 48.9206 | 976.2828 | -949890.9645 ppm | 109837.9878 | +8514.8995 ppm | 0.0953 ppm |
| ${}^{118}$Xe | 118 | 64 | 55.2189 | 988.2479 | -944124.4290 ppm | 110771.2549 | +8494.5814 ppm | 0.0945 ppm |
| ${}^{119}$Xe | 119 | 65 | 61.5051 | 997.0346 | -938312.0143 ppm | 111704.5342 | +8445.7773 ppm | 0.0937 ppm |
| ${}^{120}$Xe | 120 | 66 | 67.7792 | 1008.4839 | -932790.9443 ppm | 112637.8254 | +8421.9308 ppm | 0.1058 ppm |
| ${}^{121}$Xe | 121 | 67 | 74.0417 | 1016.8637 | -927186.1986 ppm | 113571.1284 | +8371.1002 ppm | 0.0909 ppm |
| ${}^{122}$Xe | 122 | 68 | 80.2927 | 1027.8091 | -921879.7755 ppm | 114504.4428 | +8343.9841 ppm | 0.0978 ppm |
| ${}^{123}$Xe | 123 | 69 | 86.5323 | 1035.7736 | -916456.3221 ppm | 115437.7686 | +8291.1549 ppm | 0.0833 ppm |
| ${}^{124}$Xe | 124 | 70 | 92.7609 | 1046.2641 | -911340.8208 ppm | 116371.1054 | +8261.3395 ppm | 0.0118 ppm |
| ${}^{125}$Xe | 125 | 71 | 98.9786 | 1053.8674 | -906080.5825 ppm | 117304.4532 | +8207.0748 ppm | 0.0122 ppm |
| ${}^{126}$Xe | 126 | 72 | 105.1856 | 1063.8857 | -901130.7216 ppm | 118237.8116 | +8174.5241 ppm | 0.0000 ppm |
| ${}^{127}$Xe | 127 | 73 | 111.3821 | 1071.1315 | -896014.5262 ppm | 119171.1805 | +8118.9291 ppm | 0.0346 ppm |
| ${}^{128}$Xe | 128 | 74 | 117.5683 | 1080.7425 | -891215.2374 ppm | 120104.5597 | +8084.3025 ppm | 0.0000 ppm |
| ${}^{129}$Xe | 129 | 75 | 123.7444 | 1087.6494 | -886227.6868 ppm | 121037.9491 | +8027.5950 ppm | 0.0000 ppm |
| ${}^{130}$Xe | 130 | 76 | 129.9105 | 1096.9051 | -881566.3252 ppm | 121971.3484 | +7991.4100 ppm | 0.0001 ppm |
| ${}^{131}$Xe | 131 | 77 | 136.0668 | 1103.5095 | -876696.2709 ppm | 122904.7575 | +7933.9412 ppm | 0.0000 ppm |
| ${}^{132}$Xe | 132 | 78 | 142.2136 | 1112.4462 | -872161.4020 ppm | 123838.1762 | +7896.5550 ppm | 0.0000 ppm |
| ${}^{133}$Xe | 133 | 79 | 148.3508 | 1118.8821 | -867411.5508 ppm | 124771.6043 | +7839.4483 ppm | 0.0194 ppm |
| ${}^{134}$Xe | 134 | 80 | 154.4788 | 1127.4357 | -862982.1249 ppm | 125705.0417 | +7800.3802 ppm | 0.0000 ppm |
| ${}^{135}$Xe | 135 | 81 | 160.5977 | 1133.7946 | -858353.7784 ppm | 126638.4883 | +7744.3633 ppm | 0.0292 ppm |
| ${}^{136}$Xe | 136 | 82 | 166.7076 | 1141.8817 | -854006.2304 ppm | 127571.9438 | +7702.9998 ppm | 0.0001 ppm |
| ${}^{137}$Xe | 137 | 83 | 172.8087 | 1145.9073 | -849194.8785 ppm | 128505.4082 | +7630.2185 ppm | 0.0008 ppm |
| ${}^{138}$Xe | 138 | 84 | 178.9011 | 1151.5674 | -844645.5918 ppm | 129438.8812 | +7571.3848 ppm | 0.0218 ppm |
| ${}^{139}$Xe | 139 | 85 | 184.9849 | 1155.3111 | -839883.0155 ppm | 130372.3628 | +7498.5447 ppm | 0.0166 ppm |
| ${}^{140}$Xe | 140 | 86 | 191.0604 | 1160.7242 | -835395.5494 ppm | 131305.8528 | +7439.7196 ppm | 0.0179 ppm |
| ${}^{141}$Xe | 141 | 87 | 197.1276 | 1164.0064 | -830647.3536 ppm | 132239.3510 | +7365.4412 ppm | 0.0220 ppm |
| ${}^{142}$Xe | 142 | 88 | 203.1866 | 1169.1101 | -826204.0214 ppm | 133172.8573 | +7306.1544 ppm | 0.0204 ppm |
| ${}^{143}$Xe | 143 | 89 | 209.2377 | 1172.1546 | -821493.1002 ppm | 134106.3717 | +7232.1825 ppm | 0.0350 ppm |
| ${}^{144}$Xe | 144 | 90 | 215.2809 | 1176.8954 | -817077.3032 ppm | 135039.8939 | +7172.0440 ppm | 0.0396 ppm |
| ${}^{145}$Xe | 145 | 91 | 221.3163 | 1179.5877 | -812378.2509 ppm | 135973.4239 | +7097.5162 ppm | 0.0828 ppm |
| ${}^{146}$Xe | 146 | 92 | 227.3441 | 1184.1206 | -808005.9510 ppm | 136906.9615 | +7037.7055 ppm | 0.1781 ppm |
| ${}^{147}$Xe | 147 | 93 | 233.3644 | 1186.5840 | -803330.8940 ppm | 137840.5067 | +6963.9305 ppm | 1.4630 ppm |
| ${}^{148}$Xe | 148 | 94 | 239.3773 | 1190.9560 | -799004.0637 ppm | 138774.0592 | +6904.3992 ppm | 2.1763 ppm |
| ${}^{149}$Xe | 149 | 95 | 245.3829 | 1193.3410 | -794373.1618 ppm | 139707.6190 | +6831.9413 ppm | 2.1616 ppm |
| ${}^{150}$Xe | 150 | 96 | 251.3814 | 1197.4500 | -790069.4088 ppm | 140641.1860 | +6772.3220 ppm | 2.1471 ppm |

### Caesium (Z = 55)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{111}$Cs | 111 | 56 | -7.5744 | 895.7700 | -1008455.7264 ppm | 104256.3079 | +8740.5576 ppm | 1.9377 ppm |
| ${}^{112}$Cs | 112 | 57 | -1.1523 | 907.4240 | -1001269.8655 ppm | 105189.4513 | +8712.2946 ppm | 1.1076 ppm |
| ${}^{113}$Cs | 113 | 58 | 5.2555 | 920.7944 | -994292.3819 ppm | 106122.6088 | +8702.2637 ppm | 0.0815 ppm |
| ${}^{114}$Cs | 114 | 59 | 11.6494 | 931.7871 | -987497.7394 ppm | 107055.7804 | +8669.4577 ppm | 0.8015 ppm |
| ${}^{115}$Cs | 115 | 60 | 18.0297 | 944.8400 | -980917.7465 ppm | 107988.9656 | +8657.0587 ppm | 0.9571 ppm |
| ${}^{116}$Cs | 116 | 61 | 24.3965 | 955.2600 | -974460.8755 ppm | 108922.1641 | +8620.0509 ppm | 0.9316 ppm |
| ${}^{117}$Cs | 117 | 62 | 30.7502 | 967.8082 | -968226.9817 ppm | 109855.3759 | +8603.3174 ppm | 0.5730 ppm |
| ${}^{118}$Cs | 118 | 63 | 37.0910 | 977.7958 | -962066.7403 ppm | 110788.6005 | +8563.7112 ppm | 0.1161 ppm |
| ${}^{119}$Cs | 119 | 64 | 43.4191 | 989.7628 | -956131.7800 ppm | 111721.8378 | +8542.9049 ppm | 0.1258 ppm |
| ${}^{120}$Cs | 120 | 65 | 49.7349 | 999.4177 | -950236.1443 ppm | 112655.0875 | +8501.6806 ppm | 0.0892 ppm |
| ${}^{121}$Cs | 121 | 66 | 56.0385 | 1010.7027 | -944554.9590 ppm | 113588.3493 | +8475.8401 ppm | 0.1269 ppm |
| ${}^{122}$Cs | 122 | 67 | 62.3301 | 1019.8165 | -938881.0765 ppm | 114521.6231 | +8431.2464 ppm | 0.2966 ppm |
| ${}^{123}$Cs | 123 | 68 | 68.6100 | 1030.7867 | -933439.1941 ppm | 115454.9086 | +8403.8306 ppm | 0.1058 ppm |
| ${}^{124}$Cs | 124 | 69 | 74.8784 | 1039.5554 | -927970.7548 ppm | 116388.2056 | +8357.7227 ppm | 0.0793 ppm |
| ${}^{125}$Cs | 125 | 70 | 81.1355 | 1049.9754 | -922726.2936 ppm | 117321.5140 | +8326.7596 ppm | 0.0665 ppm |
| ${}^{126}$Cs | 126 | 71 | 87.3815 | 1058.3077 | -917432.8047 ppm | 118254.8334 | +8278.4333 ppm | 0.0883 ppm |
| ${}^{127}$Cs | 127 | 72 | 93.6166 | 1068.2683 | -912366.0201 ppm | 119188.1637 | +8244.8490 ppm | 0.0472 ppm |
| ${}^{128}$Cs | 128 | 73 | 99.8410 | 1076.0314 | -907213.6623 ppm | 120121.5047 | +8193.2825 ppm | 0.0451 ppm |
| ${}^{129}$Cs | 129 | 74 | 106.0549 | 1085.6700 | -902313.8651 ppm | 121054.8562 | +8158.3506 ppm | 0.0379 ppm |
| ${}^{130}$Cs | 130 | 75 | 112.2585 | 1093.1420 | -897306.6011 ppm | 121988.2181 | +8105.9911 ppm | 0.0691 ppm |
| ${}^{131}$Cs | 131 | 76 | 118.4519 | 1102.3692 | -892547.8966 ppm | 122921.5901 | +8069.0248 ppm | 0.0015 ppm |
| ${}^{132}$Cs | 132 | 77 | 124.6353 | 1109.5376 | -887669.1292 ppm | 123854.9721 | +8015.8097 ppm | 0.0084 ppm |
| ${}^{133}$Cs | 133 | 78 | 130.8090 | 1118.5272 | -883052.4955 ppm | 124788.3639 | +7978.3028 ppm | 0.0001 ppm |
| ${}^{134}$Cs | 134 | 79 | 136.9730 | 1125.4187 | -878291.5567 ppm | 125721.7653 | +7924.4790 ppm | 0.0001 ppm |
| ${}^{135}$Cs | 135 | 80 | 143.1275 | 1134.1808 | -873805.4100 ppm | 126655.1762 | +7886.5323 ppm | 0.0029 ppm |
| ${}^{136}$Cs | 136 | 81 | 149.2727 | 1141.0090 | -869174.8396 ppm | 127588.5964 | +7833.8212 ppm | 0.0148 ppm |
| ${}^{137}$Cs | 137 | 82 | 155.4087 | 1149.2873 | -864778.1609 ppm | 128522.0258 | +7793.4117 ppm | 0.0024 ppm |
| ${}^{138}$Cs | 138 | 83 | 161.5358 | 1153.6998 | -859984.5729 ppm | 129455.4642 | +7723.3334 ppm | 0.0713 ppm |
| ${}^{139}$Cs | 139 | 84 | 167.6540 | 1159.5852 | -855419.0346 ppm | 130388.9114 | +7665.8056 ppm | 0.0242 ppm |
| ${}^{140}$Cs | 140 | 85 | 173.7634 | 1164.0052 | -850719.3853 ppm | 131322.3674 | +7597.8398 ppm | 0.0629 ppm |
| ${}^{141}$Cs | 141 | 86 | 179.8643 | 1169.5041 | -846204.6534 ppm | 132255.8319 | +7539.1892 ppm | 0.0700 ppm |
| ${}^{142}$Cs | 142 | 87 | 185.9567 | 1173.6126 | -841551.8651 ppm | 133189.3049 | +7470.8353 ppm | 0.0535 ppm |
| ${}^{143}$Cs | 143 | 88 | 192.0409 | 1178.8449 | -837094.0320 ppm | 134122.7862 | +7412.0074 ppm | 0.0569 ppm |
| ${}^{144}$Cs | 144 | 89 | 198.1168 | 1182.5121 | -832461.0452 ppm | 135056.2757 | +7342.3009 ppm | 0.1502 ppm |
| ${}^{145}$Cs | 145 | 90 | 204.1848 | 1187.3665 | -828035.6021 ppm | 135989.7732 | +7282.4781 ppm | 0.0672 ppm |
| ${}^{146}$Cs | 146 | 91 | 210.2448 | 1190.6937 | -823426.6664 ppm | 136923.2786 | +7212.2216 ppm | 0.0213 ppm |
| ${}^{147}$Cs | 147 | 92 | 216.2970 | 1195.3747 | -819055.0965 ppm | 137856.7918 | +7152.9440 ppm | 0.0612 ppm |
| ${}^{148}$Cs | 148 | 93 | 222.3415 | 1198.4369 | -814473.7597 ppm | 138790.3127 | +7082.6966 ppm | 0.0946 ppm |
| ${}^{149}$Cs | 149 | 94 | 228.3785 | 1202.8770 | -810139.7951 ppm | 139723.8411 | +7023.5965 ppm | 2.8801 ppm |
| ${}^{150}$Cs | 150 | 95 | 234.4080 | 1205.8500 | -805607.6589 ppm | 140657.3770 | +6954.3954 ppm | 2.8608 ppm |
| ${}^{151}$Cs | 151 | 96 | 240.4302 | 1209.9630 | -801291.2751 ppm | 141590.9202 | +6895.0457 ppm | 3.5572 ppm |
| ${}^{152}$Cs | 152 | 97 | 246.4452 | 1212.9600 | -796823.3207 ppm | 142524.4707 | +6827.5674 ppm | 3.5336 ppm |

### Barium (Z = 56)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{113}$Ba | 113 | 57 | -13.3820 | 907.9550 | -1014738.6355 ppm | 106140.4641 | +8756.3924 ppm | 2.8506 ppm |
| ${}^{114}$Ba | 114 | 58 | -6.9429 | 922.2243 | -1007528.4003 ppm | 107073.5903 | +8753.8086 ppm | 0.9673 ppm |
| ${}^{115}$Ba | 115 | 59 | -0.5179 | 933.3400 | -1000554.8999 ppm | 108006.7308 | +8721.4325 ppm | 1.8704 ppm |
| ${}^{116}$Ba | 116 | 60 | 5.8931 | 946.7920 | -993775.6662 ppm | 108939.8852 | +8712.5750 ppm | 1.8544 ppm |
| ${}^{117}$Ba | 117 | 61 | 12.2906 | 957.9907 | -987170.4643 ppm | 109873.0532 | +8681.9418 ppm | 2.2982 ppm |
| ${}^{118}$Ba | 118 | 62 | 18.6746 | 970.7860 | -980763.3904 ppm | 110806.2345 | +8667.2217 ppm | 1.8231 ppm |
| ${}^{119}$Ba | 119 | 63 | 25.0456 | 981.2655 | -974476.2544 ppm | 111739.4290 | +8631.4594 ppm | 1.8078 ppm |
| ${}^{120}$Ba | 120 | 64 | 31.4036 | 993.6354 | -968395.2031 ppm | 112672.6364 | +8613.6343 ppm | 2.6870 ppm |
| ${}^{121}$Ba | 121 | 65 | 37.7491 | 1003.5629 | -962384.9261 ppm | 113605.8563 | +8574.3455 ppm | 1.2597 ppm |
| ${}^{122}$Ba | 122 | 66 | 44.0822 | 1015.4983 | -956590.6211 ppm | 114539.0887 | +8553.6402 ppm | 0.2461 ppm |
| ${}^{123}$Ba | 123 | 67 | 50.4030 | 1024.6157 | -950807.8481 ppm | 115472.3332 | +8508.5540 ppm | 0.1058 ppm |
| ${}^{124}$Ba | 124 | 68 | 56.7120 | 1036.1218 | -945265.1128 ppm | 116405.5897 | +8485.1688 ppm | 0.1083 ppm |
| ${}^{125}$Ba | 125 | 69 | 63.0092 | 1044.7723 | -939690.9264 ppm | 117338.8579 | +8437.5077 ppm | 0.0945 ppm |
| ${}^{126}$Ba | 126 | 70 | 69.2950 | 1055.8446 | -934370.0919 ppm | 118272.1376 | +8411.5229 ppm | 0.1066 ppm |
| ${}^{127}$Ba | 127 | 71 | 75.5694 | 1064.0639 | -928980.3839 ppm | 119205.4286 | +8361.7068 ppm | 0.0961 ppm |
| ${}^{128}$Ba | 128 | 72 | 81.8327 | 1074.6864 | -923854.3117 ppm | 120138.7306 | +8333.1002 ppm | 0.0135 ppm |
| ${}^{129}$Ba | 129 | 73 | 88.0852 | 1082.4495 | -918624.2275 ppm | 121072.0436 | +8281.0157 ppm | 0.0875 ppm |
| ${}^{130}$Ba | 130 | 74 | 94.3269 | 1092.7167 | -913676.7377 ppm | 122005.3674 | +8250.6867 ppm | 0.0024 ppm |
| ${}^{131}$Ba | 131 | 75 | 100.5580 | 1100.2102 | -908601.0563 ppm | 122938.7016 | +8197.9726 ppm | 0.0034 ppm |
| ${}^{132}$Ba | 132 | 76 | 106.7789 | 1110.0375 | -903806.0542 ppm | 123872.0462 | +8165.2911 ppm | 0.0086 ppm |
| ${}^{133}$Ba | 133 | 77 | 112.9895 | 1117.2274 | -898866.1134 ppm | 124805.4010 | +8111.7063 ppm | 0.0080 ppm |
| ${}^{134}$Ba | 134 | 78 | 119.1902 | 1126.6952 | -894212.5464 ppm | 125738.7657 | +8077.4123 ppm | 0.0020 ppm |
| ${}^{135}$Ba | 135 | 79 | 125.3811 | 1133.6672 | -889402.2332 ppm | 126672.1403 | +8023.6832 ppm | 0.0019 ppm |
| ${}^{136}$Ba | 136 | 80 | 131.5622 | 1142.7749 | -884874.7610 ppm | 127605.5245 | +7987.8274 ppm | 0.0019 ppm |
| ${}^{137}$Ba | 137 | 81 | 137.7339 | 1149.6805 | -880198.1049 ppm | 128538.9183 | +7935.1644 ppm | 0.0019 ppm |
| ${}^{138}$Ba | 138 | 82 | 143.8962 | 1158.2923 | -875768.6274 ppm | 129472.3214 | +7896.7247 ppm | 0.0019 ppm |
| ${}^{139}$Ba | 139 | 83 | 150.0494 | 1163.0157 | -870982.5020 ppm | 130405.7337 | +7828.6228 ppm | 0.0020 ppm |
| ${}^{140}$Ba | 140 | 84 | 156.1935 | 1169.4410 | -866437.4942 ppm | 131339.1550 | +7774.7272 ppm | 0.0606 ppm |
| ${}^{141}$Ba | 141 | 85 | 162.3287 | 1173.9769 | -861727.5456 ppm | 132272.5852 | +7707.1604 ppm | 0.0405 ppm |
| ${}^{142}$Ba | 142 | 86 | 168.4551 | 1180.1580 | -857260.5402 ppm | 133206.0242 | +7653.1557 ppm | 0.0448 ppm |
| ${}^{143}$Ba | 143 | 87 | 174.5729 | 1184.3243 | -852597.0014 ppm | 134139.4718 | +7584.7238 ppm | 0.0507 ppm |
| ${}^{144}$Ba | 144 | 88 | 180.6823 | 1190.2255 | -848194.9007 ppm | 135072.9279 | +7530.3488 ppm | 0.0532 ppm |
| ${}^{145}$Ba | 145 | 89 | 186.7833 | 1194.0459 | -843571.0751 ppm | 136006.3923 | +7461.2586 ppm | 0.0628 ppm |
| ${}^{146}$Ba | 146 | 90 | 192.8761 | 1199.4673 | -839198.5241 ppm | 136939.8649 | +7405.0451 ppm | 0.0130 ppm |
| ${}^{147}$Ba | 147 | 91 | 198.9608 | 1202.9364 | -834604.0347 ppm | 137873.3456 | +7335.2891 ppm | 0.1443 ppm |
| ${}^{148}$Ba | 148 | 92 | 205.0376 | 1208.2885 | -830307.4465 ppm | 138806.8343 | +7280.3030 ppm | 0.0108 ppm |
| ${}^{149}$Ba | 149 | 93 | 211.1065 | 1211.6456 | -825768.7867 ppm | 139740.3308 | +7211.6294 ppm | 0.0181 ppm |
| ${}^{150}$Ba | 150 | 94 | 217.1677 | 1216.7761 | -821522.0755 ppm | 140673.8350 | +7156.7195 ppm | 0.0407 ppm |
| ${}^{151}$Ba | 151 | 95 | 223.2213 | 1219.9290 | -817021.1097 ppm | 141607.3469 | +7088.2041 ppm | 2.8420 ppm |
| ${}^{152}$Ba | 152 | 96 | 229.2674 | 1224.6640 | -812791.6298 ppm | 142540.8662 | +7032.1720 ppm | 2.8232 ppm |
| ${}^{153}$Ba | 153 | 97 | 235.3061 | 1227.5190 | -808307.5938 ppm | 143474.3929 | +6964.1357 ppm | 2.8046 ppm |
| ${}^{154}$Ba | 154 | 98 | 241.3375 | 1232.1540 | -804133.6376 ppm | 144407.9269 | +6908.2022 ppm | 3.4878 ppm |

### Lanthanum (Z = 57)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{116}$La | 116 | 59 | -12.9002 | 931.7120 | -1013845.7106 ppm | 108957.8962 | +8745.4975 ppm | 2.9752 ppm |
| ${}^{117}$La | 117 | 60 | -6.4582 | 946.0620 | -1006826.4531 ppm | 109891.0197 | +8743.2837 ppm | 1.8384 ppm |
| ${}^{118}$La | 118 | 61 | -0.0301 | 957.4520 | -1000031.4807 ppm | 110824.1570 | +8714.8574 ppm | 2.7300 ppm |
| ${}^{119}$La | 119 | 62 | 6.3844 | 970.9210 | -993424.4190 ppm | 111757.3079 | +8705.7043 ppm | 2.7072 ppm |
| ${}^{120}$La | 120 | 63 | 12.7855 | 981.4800 | -986973.2009 ppm | 112690.4721 | +8671.0957 ppm | 2.6847 ppm |
| ${}^{121}$La | 121 | 64 | 19.1736 | 994.2570 | -980715.6212 ppm | 113623.6495 | +8655.7065 ppm | 2.6626 ppm |
| ${}^{122}$La | 122 | 65 | 25.5489 | 1004.6700 | -974569.8875 ppm | 114556.8396 | +8620.5470 ppm | 2.6244 ppm |
| ${}^{123}$La | 123 | 66 | 31.9115 | 1016.8410 | -968617.0130 ppm | 115490.0424 | +8601.5259 ppm | 1.7083 ppm |
| ${}^{124}$La | 124 | 67 | 38.2618 | 1026.5083 | -962726.2917 ppm | 116423.2576 | +8561.0713 ppm | 0.4909 ppm |
| ${}^{125}$La | 125 | 68 | 44.5999 | 1038.0805 | -957036.1986 ppm | 117356.4849 | +8537.7775 ppm | 0.2234 ppm |
| ${}^{126}$La | 126 | 69 | 50.9261 | 1047.3658 | -951376.9994 ppm | 118289.7241 | +8495.2908 ppm | 0.7716 ppm |
| ${}^{127}$La | 127 | 70 | 57.2405 | 1058.3597 | -945915.8049 ppm | 119222.9751 | +8468.1470 ppm | 0.2199 ppm |
| ${}^{128}$La | 128 | 71 | 63.5435 | 1067.1604 | -940455.5343 ppm | 120156.2376 | +8422.9598 ppm | 0.4570 ppm |
| ${}^{129}$La | 129 | 72 | 69.8351 | 1077.9298 | -935213.6382 ppm | 121089.5113 | +8395.1000 ppm | 0.1777 ppm |
| ${}^{130}$La | 130 | 73 | 76.1157 | 1086.3049 | -929931.5550 ppm | 122022.7962 | +8347.8088 ppm | 0.2144 ppm |
| ${}^{131}$La | 131 | 74 | 82.3853 | 1096.5182 | -924866.4206 ppm | 122956.0920 | +8316.5276 ppm | 0.2292 ppm |
| ${}^{132}$La | 132 | 75 | 88.6442 | 1104.5438 | -919745.8299 ppm | 123889.3985 | +8267.8560 ppm | 0.2959 ppm |
| ${}^{133}$La | 133 | 76 | 94.8926 | 1114.3859 | -914847.6200 ppm | 124822.7156 | +8234.7950 ppm | 0.2257 ppm |
| ${}^{134}$La | 134 | 77 | 101.1306 | 1122.1815 | -909880.3355 ppm | 125756.0430 | +8185.7683 ppm | 0.1598 ppm |
| ${}^{135}$La | 135 | 78 | 107.3584 | 1131.6776 | -905133.3722 ppm | 126689.3806 | +8151.1919 ppm | 0.0751 ppm |
| ${}^{136}$La | 136 | 79 | 113.5762 | 1139.1430 | -900296.7614 ppm | 127622.7282 | +8101.0314 ppm | 0.4200 ppm |
| ${}^{137}$La | 137 | 80 | 119.7842 | 1148.3177 | -895687.2298 ppm | 128556.0857 | +8065.1930 ppm | 0.0129 ppm |
| ${}^{138}$La | 138 | 81 | 125.9825 | 1155.7615 | -890996.1450 ppm | 129489.4528 | +8016.3673 ppm | 0.0032 ppm |
| ${}^{139}$La | 139 | 82 | 132.1712 | 1164.5418 | -886503.6904 ppm | 130422.8295 | +7978.7295 ppm | 0.0047 ppm |
| ${}^{140}$La | 140 | 83 | 138.3506 | 1169.7028 | -881721.6122 ppm | 131356.2156 | +7913.7095 ppm | 0.0047 ppm |
| ${}^{141}$La | 141 | 84 | 144.5207 | 1176.3919 | -877149.1840 ppm | 132289.6108 | +7861.4189 ppm | 0.0314 ppm |
| ${}^{142}$La | 142 | 85 | 150.6818 | 1181.5573 | -872471.8894 ppm | 133223.0152 | +7798.3186 ppm | 0.0475 ppm |
| ${}^{143}$La | 143 | 86 | 156.8339 | 1187.7762 | -867960.0435 ppm | 134156.4285 | +7744.1454 ppm | 0.0551 ppm |
| ${}^{144}$La | 144 | 87 | 162.9773 | 1192.5257 | -863334.3745 ppm | 135089.8506 | +7679.7476 ppm | 0.0965 ppm |
| ${}^{145}$La | 145 | 88 | 169.1120 | 1198.5827 | -858906.7098 ppm | 136023.2813 | +7626.0649 ppm | 0.0909 ppm |
| ${}^{146}$La | 146 | 89 | 175.2382 | 1203.0398 | -854337.1909 ppm | 136956.7205 | +7561.3236 ppm | 0.0123 ppm |
| ${}^{147}$La | 147 | 90 | 181.3560 | 1208.5684 | -849941.4918 ppm | 137890.1681 | +7505.4150 ppm | 0.0783 ppm |
| ${}^{148}$La | 148 | 91 | 187.4655 | 1212.6700 | -845410.9390 ppm | 138823.6240 | +7439.8922 ppm | 0.1413 ppm |
| ${}^{149}$La | 149 | 92 | 193.5670 | 1218.2525 | -841110.9793 ppm | 139757.0880 | +7386.0644 ppm | 1.4435 ppm |
| ${}^{150}$La | 150 | 93 | 199.6604 | 1222.4151 | -836667.2820 ppm | 140690.5600 | +7322.7726 ppm | 0.0180 ppm |
| ${}^{151}$La | 151 | 94 | 205.7459 | 1227.4856 | -832384.2449 ppm | 141624.0399 | +7266.8835 ppm | 3.0972 ppm |
| ${}^{152}$La | 152 | 95 | 211.8237 | 1231.5040 | -827995.9265 ppm | 142557.5275 | +7204.5322 ppm | 2.1192 ppm |
| ${}^{153}$La | 153 | 96 | 217.8938 | 1236.3930 | -823766.5220 ppm | 143491.0228 | +7148.6373 ppm | 2.1053 ppm |
| ${}^{154}$La | 154 | 97 | 223.9564 | 1239.8540 | -819368.7009 ppm | 144424.5256 | +7084.3982 ppm | 2.0915 ppm |
| ${}^{155}$La | 155 | 98 | 230.0116 | 1244.3400 | -815153.7234 ppm | 145358.0359 | +7027.5359 ppm | 2.7685 ppm |
| ${}^{156}$La | 156 | 99 | 236.0595 | 1247.5320 | -810778.8188 ppm | 146291.5534 | +6962.5782 ppm | 2.7506 ppm |
| ${}^{157}$La | 157 | 100 | 242.1001 | 1251.6040 | -806568.1050 ppm | 147225.0782 | +6904.6984 ppm | 2.0514 ppm |

### Cerium (Z = 58)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{119}$Ce | 119 | 61 | -12.5645 | 958.9020 | -1013102.9777 ppm | 111775.4744 | +8767.7025 ppm | 4.5144 ppm |
| ${}^{120}$Ce | 120 | 62 | -6.1194 | 972.9600 | -1006289.4937 ppm | 112708.5948 | +8762.5152 ppm | 4.4770 ppm |
| ${}^{121}$Ce | 121 | 63 | 0.3121 | 983.9720 | -999682.8546 ppm | 113641.7287 | +8731.1267 ppm | 3.5554 ppm |
| ${}^{122}$Ce | 122 | 64 | 6.7302 | 997.2280 | -993251.0466 ppm | 114574.8759 | +8720.1143 ppm | 3.5264 ppm |
| ${}^{123}$Ce | 123 | 65 | 13.1354 | 1007.7390 | -986965.5045 ppm | 115508.0362 | +8684.9837 ppm | 2.6030 ppm |
| ${}^{124}$Ce | 124 | 66 | 19.5277 | 1020.3960 | -980862.6511 ppm | 116441.2094 | +8669.9000 ppm | 2.5821 ppm |
| ${}^{125}$Ce | 125 | 67 | 25.9074 | 1030.2500 | -974853.2945 ppm | 117374.3951 | +8630.1358 ppm | 1.6810 ppm |
| ${}^{126}$Ce | 126 | 68 | 32.2748 | 1042.4305 | -969038.9401 ppm | 118307.5931 | +8611.9241 ppm | 0.2382 ppm |
| ${}^{127}$Ce | 127 | 69 | 38.6300 | 1051.6606 | -963267.6390 ppm | 119240.8033 | +8568.4732 ppm | 0.2442 ppm |
| ${}^{128}$Ce | 128 | 70 | 44.9733 | 1063.2865 | -957703.5176 ppm | 120174.0254 | +8546.0787 ppm | 0.2345 ppm |
| ${}^{129}$Ce | 129 | 71 | 51.3049 | 1072.1114 | -952145.9516 ppm | 121107.2593 | +8500.6042 ppm | 0.2327 ppm |
| ${}^{130}$Ce | 130 | 72 | 57.6250 | 1083.3181 | -946806.9858 ppm | 122040.5046 | +8475.7728 ppm | 0.2309 ppm |
| ${}^{131}$Ce | 131 | 73 | 63.9337 | 1091.6750 | -941435.1915 ppm | 122973.7613 | +8427.8447 ppm | 0.2690 ppm |
| ${}^{132}$Ce | 132 | 74 | 70.2314 | 1102.5065 | -936298.4218 ppm | 123907.0290 | +8401.0423 ppm | 0.1661 ppm |
| ${}^{133}$Ce | 133 | 75 | 76.5182 | 1110.5274 | -931097.4623 ppm | 124840.3077 | +8351.8377 ppm | 0.1321 ppm |
| ${}^{134}$Ce | 134 | 76 | 82.7942 | 1121.0134 | -926143.4593 ppm | 125773.5971 | +8323.3811 ppm | 0.1634 ppm |
| ${}^{135}$Ce | 135 | 77 | 89.0596 | 1128.8681 | -921107.1415 ppm | 126706.8970 | +8274.3172 ppm | 0.0817 ppm |
| ${}^{136}$Ce | 136 | 78 | 95.3147 | 1138.8317 | -916304.8241 ppm | 127640.2074 | +8242.8524 ppm | 0.0026 ppm |
| ${}^{137}$Ce | 137 | 79 | 101.5596 | 1146.3132 | -911403.2719 ppm | 128573.5279 | +8192.3040 ppm | 0.0028 ppm |
| ${}^{138}$Ce | 138 | 80 | 107.7944 | 1156.0316 | -906754.7610 ppm | 129506.8585 | +8160.1223 ppm | 0.0039 ppm |
| ${}^{139}$Ce | 139 | 81 | 114.0194 | 1163.4948 | -902002.6405 ppm | 130440.1989 | +8110.9082 ppm | 0.0161 ppm |
| ${}^{140}$Ce | 140 | 82 | 120.2347 | 1172.6826 | -897470.3954 ppm | 131373.5491 | +8075.8128 ppm | 0.0101 ppm |
| ${}^{141}$Ce | 141 | 83 | 126.4404 | 1178.1108 | -892675.2891 ppm | 132306.9088 | +8012.4136 ppm | 0.0100 ppm |
| ${}^{142}$Ce | 142 | 84 | 132.6367 | 1185.2839 | -888097.0987 ppm | 133240.2779 | +7963.2875 ppm | 0.0185 ppm |
| ${}^{143}$Ce | 143 | 85 | 138.8238 | 1190.4287 | -883383.3807 ppm | 134173.6563 | +7899.5616 ppm | 0.0183 ppm |
| ${}^{144}$Ce | 144 | 86 | 145.0017 | 1197.3256 | -878895.3198 ppm | 135107.0437 | +7849.9643 ppm | 0.0211 ppm |
| ${}^{145}$Ce | 145 | 87 | 151.1707 | 1202.0320 | -874237.3500 ppm | 136040.4402 | +7784.7654 ppm | 0.2511 ppm |
| ${}^{146}$Ce | 146 | 88 | 157.3309 | 1208.6622 | -869830.5294 ppm | 136973.8454 | +7734.7903 ppm | 0.1079 ppm |
| ${}^{147}$Ce | 147 | 89 | 163.4824 | 1213.1215 | -865238.2219 ppm | 137907.2593 | +7669.5766 ppm | 0.0627 ppm |
| ${}^{148}$Ce | 148 | 90 | 169.6254 | 1219.5774 | -860914.6351 ppm | 138840.6818 | +7619.9095 ppm | 0.0812 ppm |
| ${}^{149}$Ce | 149 | 91 | 175.7599 | 1223.9202 | -856395.9511 ppm | 139774.1127 | +7555.6243 ppm | 0.0739 ppm |
| ${}^{150}$Ce | 150 | 92 | 181.8861 | 1230.1684 | -852145.3432 ppm | 140707.5519 | +7506.0052 ppm | 0.0837 ppm |
| ${}^{151}$Ce | 151 | 93 | 188.0042 | 1234.6180 | -847722.7648 ppm | 141640.9992 | +7444.2136 ppm | 0.1259 ppm |
| ${}^{152}$Ce | 152 | 94 | 194.1142 | 1240.4720 | -843515.8199 ppm | 142574.4546 | +7393.0974 ppm | 1.4151 ppm |
| ${}^{153}$Ce | 153 | 95 | 200.2164 | 1244.5020 | -839119.2977 ppm | 143507.9179 | +7329.7960 ppm | 1.4058 ppm |
| ${}^{154}$Ce | 154 | 96 | 206.3107 | 1249.8640 | -834933.5103 ppm | 144441.3890 | +7277.0719 ppm | 1.3966 ppm |
| ${}^{155}$Ce | 155 | 97 | 212.3973 | 1253.4850 | -830554.5891 ppm | 145374.8679 | +7212.8759 ppm | 2.0781 ppm |
| ${}^{156}$Ce | 156 | 98 | 218.4763 | 1258.6080 | -826414.3231 ppm | 146308.3542 | +7159.8147 ppm | 2.0647 ppm |
| ${}^{157}$Ce | 157 | 99 | 224.5479 | 1261.8090 | -822042.8800 ppm | 147241.8481 | +7094.1943 ppm | 2.7332 ppm |
| ${}^{158}$Ce | 158 | 100 | 230.6121 | 1266.3700 | -817895.1563 ppm | 148175.3493 | +7039.7169 ppm | 2.7159 ppm |
| ${}^{159}$Ce | 159 | 101 | 236.6691 | 1269.2970 | -813543.1872 ppm | 149108.8578 | +6973.6745 ppm | 3.3781 ppm |

### Praseodymium (Z = 59)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{121}$Pr | 121 | 62 | -18.8356 | 971.9930 | -1019378.3353 ppm | 113660.0940 | +8794.4028 ppm | 4.4397 ppm |
| ${}^{122}$Pr | 122 | 63 | -12.3737 | 983.3200 | -1012583.6211 ppm | 114593.1976 | +8765.1280 ppm | 4.4034 ppm |
| ${}^{123}$Pr | 123 | 64 | -5.9254 | 996.7920 | -1005944.4362 ppm | 115526.3146 | +8756.0141 ppm | 3.4893 ppm |
| ${}^{124}$Pr | 124 | 65 | 0.5097 | 1007.8720 | -999494.2596 ppm | 116459.4450 | +8725.0644 ppm | 3.4693 ppm |
| ${}^{125}$Pr | 125 | 66 | 6.9318 | 1020.8750 | -993209.9628 ppm | 117392.5883 | +8712.0385 ppm | 2.5773 ppm |
| ${}^{126}$Pr | 126 | 67 | 13.3410 | 1031.1840 | -987062.4040 ppm | 118325.7445 | +8676.4037 ppm | 1.6675 ppm |
| ${}^{127}$Pr | 127 | 68 | 19.7377 | 1043.4320 | -981083.8279 ppm | 119258.9132 | +8658.2101 ppm | 1.6544 ppm |
| ${}^{128}$Pr | 128 | 69 | 26.1221 | 1053.3010 | -975199.7821 ppm | 120192.0943 | +8619.8172 ppm | 0.2501 ppm |
| ${}^{129}$Pr | 129 | 70 | 32.4943 | 1064.8151 | -969483.5990 ppm | 121125.2875 | +8596.0211 ppm | 0.2482 ppm |
| ${}^{130}$Pr | 130 | 71 | 38.8546 | 1074.2883 | -963832.2014 ppm | 122058.4926 | +8555.6801 ppm | 0.5311 ppm |
| ${}^{131}$Pr | 131 | 72 | 45.2033 | 1085.4849 | -958356.6193 ppm | 122991.7094 | +8530.3018 ppm | 0.3854 ppm |
| ${}^{132}$Pr | 132 | 73 | 51.5404 | 1094.4830 | -952908.9335 ppm | 123924.9377 | +8487.3580 ppm | 0.2350 ppm |
| ${}^{133}$Pr | 133 | 74 | 57.8662 | 1105.2644 | -947644.9476 ppm | 124858.1773 | +8459.6764 ppm | 0.1009 ppm |
| ${}^{134}$Pr | 134 | 75 | 64.1809 | 1113.9261 | -942383.1918 ppm | 125791.4281 | +8415.3599 ppm | 0.1629 ppm |
| ${}^{135}$Pr | 135 | 76 | 70.4846 | 1124.4053 | -937313.8549 ppm | 126724.6897 | +8386.3701 ppm | 0.0940 ppm |
| ${}^{136}$Pr | 136 | 77 | 76.7777 | 1132.8812 | -932227.9695 ppm | 127657.9621 | +8341.9346 ppm | 0.0905 ppm |
| ${}^{137}$Pr | 137 | 78 | 83.0601 | 1142.8139 | -927319.6458 ppm | 128591.2451 | +8309.7490 ppm | 0.0638 ppm |
| ${}^{138}$Pr | 138 | 79 | 89.3322 | 1150.8123 | -922374.6642 ppm | 129524.5384 | +8262.9279 ppm | 0.0779 ppm |
| ${}^{139}$Pr | 139 | 80 | 95.5940 | 1160.5834 | -917632.7676 ppm | 130457.8420 | +8230.6728 ppm | 0.0282 ppm |
| ${}^{140}$Pr | 140 | 81 | 101.8458 | 1168.5123 | -912841.4461 ppm | 131391.1556 | +8184.7037 ppm | 0.0471 ppm |
| ${}^{141}$Pr | 141 | 82 | 108.0877 | 1177.9119 | -908237.8333 ppm | 132324.4791 | +8150.7589 ppm | 0.0114 ppm |
| ${}^{142}$Pr | 142 | 83 | 114.3199 | 1183.7551 | -903426.0285 ppm | 133257.8124 | +8090.2425 ppm | 0.0113 ppm |
| ${}^{143}$Pr | 143 | 84 | 120.5425 | 1191.1082 | -898798.0035 ppm | 134191.1552 | +8042.0811 ppm | 0.0136 ppm |
| ${}^{144}$Pr | 144 | 85 | 126.7557 | 1196.8619 | -894093.2921 ppm | 135124.5074 | +7982.6331 ppm | 0.0202 ppm |
| ${}^{145}$Pr | 145 | 86 | 132.9596 | 1203.8086 | -889550.8778 ppm | 136057.8690 | +7932.9844 ppm | 0.0530 ppm |
| ${}^{146}$Pr | 146 | 87 | 139.1544 | 1208.9275 | -884894.3525 ppm | 136991.2396 | +7870.5299 ppm | 0.2528 ppm |
| ${}^{147}$Pr | 147 | 88 | 145.3402 | 1215.7694 | -880454.1716 ppm | 137924.6193 | +7821.6832 ppm | 0.1158 ppm |
| ${}^{148}$Pr | 148 | 89 | 151.5171 | 1220.9321 | -875900.4750 ppm | 138858.0078 | +7761.2801 ppm | 0.1092 ppm |
| ${}^{149}$Pr | 149 | 90 | 157.6853 | 1227.5073 | -871540.2316 ppm | 139791.4050 | +7712.0147 ppm | 0.0712 ppm |
| ${}^{150}$Pr | 150 | 91 | 163.8449 | 1232.8397 | -867099.5668 ppm | 140724.8108 | +7654.5019 ppm | 0.0645 ppm |
| ${}^{151}$Pr | 151 | 92 | 169.9961 | 1239.3902 | -862838.9109 ppm | 141658.2250 | +7606.5432 ppm | 0.0829 ppm |
| ${}^{152}$Pr | 152 | 93 | 176.1390 | 1244.4399 | -858459.2448 ppm | 142591.6476 | +7548.5911 ppm | 0.1310 ppm |
| ${}^{153}$Pr | 153 | 94 | 182.2736 | 1250.3217 | -854218.6178 ppm | 143525.0783 | +7497.3412 ppm | 0.0834 ppm |
| ${}^{154}$Pr | 154 | 95 | 188.4002 | 1254.6841 | -849842.5271 ppm | 144458.5172 | +7436.1407 ppm | 0.6974 ppm |
| ${}^{155}$Pr | 155 | 96 | 194.5188 | 1260.3112 | -845658.1108 ppm | 145391.9640 | +7384.6153 ppm | 0.1192 ppm |
| ${}^{156}$Pr | 156 | 97 | 200.6296 | 1264.4165 | -841326.3499 ppm | 146325.4186 | +7323.2537 ppm | 0.0071 ppm |
| ${}^{157}$Pr | 157 | 98 | 206.7326 | 1269.4733 | -837150.8743 ppm | 147258.8810 | +7269.2860 ppm | 0.0217 ppm |
| ${}^{158}$Pr | 158 | 99 | 212.8280 | 1273.3220 | -832856.0795 ppm | 148192.3510 | +7207.3598 ppm | 2.0386 ppm |
| ${}^{159}$Pr | 159 | 100 | 218.9159 | 1277.8830 | -828688.5878 ppm | 149125.8285 | +7152.4187 ppm | 2.6989 ppm |
| ${}^{160}$Pr | 160 | 101 | 224.9964 | 1281.4400 | -824419.0521 ppm | 150059.3135 | +7090.1768 ppm | 2.6819 ppm |
| ${}^{161}$Pr | 161 | 102 | 231.0697 | 1285.7460 | -820283.5850 ppm | 150992.8057 | +7034.5351 ppm | 3.3361 ppm |

### Neodymium (Z = 60)

_40 of 40 isotopes with a framework prediction; 40 of 40 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{124}$Nd | 124 | 64 | -18.7921 | 998.6960 | -1018816.6248 ppm | 116477.9644 | +8812.7640 ppm | 4.3323 ppm |
| ${}^{125}$Nd | 125 | 65 | -12.3270 | 1010.0000 | -1012204.9097 ppm | 117411.0647 | +8784.1138 ppm | 3.4334 ppm |
| ${}^{126}$Nd | 126 | 66 | -5.8751 | 1023.3720 | -1005740.8922 ppm | 118344.1783 | +8773.8353 ppm | 2.5567 ppm |
| ${}^{127}$Nd | 127 | 67 | 0.5638 | 1034.0340 | -999454.7370 ppm | 119277.3048 | +8740.1066 ppm | 2.5366 ppm |
| ${}^{128}$Nd | 128 | 68 | 6.9899 | 1046.6560 | -993321.6462 ppm | 120210.4441 | +8724.7038 ppm | 1.6805 ppm |
| ${}^{129}$Nd | 129 | 69 | 13.4035 | 1056.6390 | -987314.9554 ppm | 121143.5960 | +8686.3291 ppm | 1.6830 ppm |
| ${}^{130}$Nd | 130 | 70 | 19.8048 | 1068.9268 | -981472.2934 ppm | 122076.7601 | +8668.4572 ppm | 0.2309 ppm |
| ${}^{131}$Nd | 131 | 71 | 26.1939 | 1078.1699 | -975705.2206 ppm | 123009.9364 | +8625.7336 ppm | 0.2256 ppm |
| ${}^{132}$Nd | 132 | 72 | 32.5711 | 1089.8990 | -970115.4541 ppm | 123943.1246 | +8604.1574 ppm | 0.1970 ppm |
| ${}^{133}$Nd | 133 | 73 | 38.9367 | 1098.8769 | -964566.8447 ppm | 124876.3245 | +8560.5882 ppm | 0.3762 ppm |
| ${}^{134}$Nd | 134 | 74 | 45.2907 | 1110.2622 | -959207.1926 ppm | 125809.5359 | +8537.2251 ppm | 0.0947 ppm |
| ${}^{135}$Nd | 135 | 75 | 51.6334 | 1118.9007 | -953853.4146 ppm | 126742.7586 | +8492.2539 ppm | 0.1522 ppm |
| ${}^{136}$Nd | 136 | 76 | 57.9651 | 1129.9577 | -948701.5608 ppm | 127675.9924 | +8467.2962 ppm | 0.0933 ppm |
| ${}^{137}$Nd | 137 | 77 | 64.2858 | 1138.4137 | -943530.4094 ppm | 128609.2371 | +8422.2209 ppm | 0.0919 ppm |
| ${}^{138}$Nd | 138 | 78 | 70.5957 | 1148.9183 | -938554.6400 ppm | 129542.4926 | +8393.9628 ppm | 0.0903 ppm |
| ${}^{139}$Nd | 139 | 79 | 76.8951 | 1156.9893 | -933538.6595 ppm | 130475.7586 | +8347.2284 ppm | 0.2127 ppm |
| ${}^{140}$Nd | 140 | 80 | 83.1840 | 1167.3010 | -928738.1502 ppm | 131409.0351 | +8318.5767 ppm | 0.0250 ppm |
| ${}^{141}$Nd | 141 | 81 | 89.4628 | 1175.3065 | -923881.3418 ppm | 132342.3218 | +8272.6941 ppm | 0.0242 ppm |
| ${}^{142}$Nd | 142 | 82 | 95.7314 | 1185.1364 | -919223.2899 ppm | 133275.6185 | +8241.4486 ppm | 0.0095 ppm |
| ${}^{143}$Nd | 143 | 83 | 101.9902 | 1191.2600 | -914384.6207 ppm | 134208.9252 | +8182.6437 ppm | 0.0094 ppm |
| ${}^{144}$Nd | 144 | 84 | 108.2392 | 1199.0770 | -909731.2546 ppm | 135142.2416 | +8137.4660 ppm | 0.0094 ppm |
| ${}^{145}$Nd | 145 | 85 | 114.4786 | 1204.8323 | -904983.8031 ppm | 136075.5677 | +8077.5857 ppm | 0.0094 ppm |
| ${}^{146}$Nd | 146 | 86 | 120.7085 | 1212.3975 | -900438.1499 ppm | 137008.9031 | +8032.0209 ppm | 0.0094 ppm |
| ${}^{147}$Nd | 147 | 87 | 126.9292 | 1217.6897 | -895762.2819 ppm | 137942.2479 | +7970.4025 ppm | 0.0093 ppm |
| ${}^{148}$Nd | 148 | 88 | 133.1407 | 1225.0223 | -891315.6954 ppm | 138875.6018 | +7924.6121 ppm | 0.0149 ppm |
| ${}^{149}$Nd | 149 | 89 | 139.3432 | 1230.0611 | -886718.4895 ppm | 139808.9647 | +7862.8361 ppm | 0.0148 ppm |
| ${}^{150}$Nd | 150 | 90 | 145.5368 | 1237.4368 | -882388.5156 ppm | 140742.3366 | +7818.8153 ppm | 0.0081 ppm |
| ${}^{151}$Nd | 151 | 91 | 151.7216 | 1242.7714 | -877916.6942 ppm | 141675.7171 | +7760.8084 ppm | 0.0081 ppm |
| ${}^{152}$Nd | 152 | 92 | 157.8979 | 1250.0492 | -873686.6649 ppm | 142609.1063 | +7717.4655 ppm | 0.1730 ppm |
| ${}^{153}$Nd | 153 | 93 | 164.0656 | 1255.3012 | -869301.7786 ppm | 143542.5040 | +7660.4197 ppm | 0.0193 ppm |
| ${}^{154}$Nd | 154 | 94 | 170.2250 | 1261.6218 | -865074.4308 ppm | 144475.9100 | +7611.6843 ppm | 0.0071 ppm |
| ${}^{155}$Nd | 155 | 95 | 176.3762 | 1266.3973 | -860726.0160 ppm | 145409.3243 | +7552.8496 ppm | 0.0634 ppm |
| ${}^{156}$Nd | 156 | 96 | 182.5192 | 1272.3869 | -856553.6691 ppm | 146342.7467 | +7503.2496 ppm | 0.0090 ppm |
| ${}^{157}$Nd | 157 | 97 | 188.6543 | 1276.7502 | -852238.6938 ppm | 147276.1770 | +7443.1298 ppm | 0.0146 ppm |
| ${}^{158}$Nd | 158 | 98 | 194.7814 | 1282.1626 | -848083.6584 ppm | 148209.6153 | +7391.0109 ppm | 0.0089 ppm |
| ${}^{159}$Nd | 159 | 99 | 200.9008 | 1286.1228 | -843793.4194 ppm | 149143.0613 | +7329.7223 ppm | 0.2013 ppm |
| ${}^{160}$Nd | 160 | 100 | 207.0126 | 1291.1946 | -839673.6050 ppm | 150076.5150 | +7276.7700 ppm | 0.3126 ppm |
| ${}^{161}$Nd | 161 | 101 | 213.1168 | 1294.7620 | -835400.8227 ppm | 151009.9762 | +7214.4859 ppm | 2.6653 ppm |
| ${}^{162}$Nd | 162 | 102 | 219.2135 | 1299.5640 | -831317.6552 ppm | 151943.4449 | +7161.5301 ppm | 2.6488 ppm |
| ${}^{163}$Nd | 163 | 103 | 225.3029 | 1302.6960 | -827048.7459 ppm | 152876.9209 | +7097.9283 ppm | 3.2952 ppm |

### Promethium (Z = 61)

_40 of 40 isotopes with a framework prediction; 40 of 40 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{126}$Pm | 126 | 65 | -25.3736 | 1009.0080 | -1025147.0528 ppm | 118362.8944 | +8816.1611 ppm | 4.2633 ppm |
| ${}^{127}$Pm | 127 | 66 | -18.8918 | 1022.6040 | -1018474.1886 ppm | 119295.9781 | +8807.5900 ppm | 3.3792 ppm |
| ${}^{128}$Pm | 128 | 67 | -12.4232 | 1033.6000 | -1012019.3368 ppm | 120229.0749 | +8776.8316 ppm | 2.5166 ppm |
| ${}^{129}$Pm | 129 | 68 | -5.9676 | 1046.7060 | -1005701.2824 ppm | 121162.1847 | +8763.8758 ppm | 2.4972 ppm |
| ${}^{130}$Pm | 130 | 69 | 0.4753 | 1057.0300 | -999550.3362 ppm | 122095.3073 | +8728.9665 ppm | 1.6546 ppm |
| ${}^{131}$Pm | 131 | 70 | 6.9057 | 1069.3530 | -993542.2082 ppm | 123028.4423 | +8711.3241 ppm | 1.6420 ppm |
| ${}^{132}$Pm | 132 | 71 | 13.3237 | 1079.3640 | -987655.9692 ppm | 123961.5897 | +8673.9941 ppm | 1.2127 ppm |
| ${}^{133}$Pm | 133 | 72 | 19.7296 | 1091.1698 | -981918.8091 ppm | 124894.7492 | +8652.9835 ppm | 0.4062 ppm |
| ${}^{134}$Pm | 134 | 73 | 26.1237 | 1100.5974 | -976264.0672 ppm | 125827.9205 | +8612.7846 ppm | 0.3360 ppm |
| ${}^{135}$Pm | 135 | 74 | 32.5061 | 1111.9671 | -970767.0573 ppm | 126761.1036 | +8588.8593 ppm | 0.6596 ppm |
| ${}^{136}$Pm | 136 | 75 | 38.8769 | 1121.1460 | -965323.9265 ppm | 127694.2982 | +8547.9238 ppm | 0.5455 ppm |
| ${}^{137}$Pm | 137 | 76 | 45.2365 | 1132.1203 | -960042.6642 ppm | 128627.5040 | +8521.8707 ppm | 0.1022 ppm |
| ${}^{138}$Pm | 138 | 77 | 51.5850 | 1141.0331 | -954791.0034 ppm | 129560.7210 | +8480.0985 ppm | 0.0903 ppm |
| ${}^{139}$Pm | 139 | 78 | 57.9225 | 1151.6911 | -949706.5830 ppm | 130493.9489 | +8452.6119 ppm | 0.1050 ppm |
| ${}^{140}$Pm | 140 | 79 | 64.2492 | 1160.4734 | -944635.3179 ppm | 131427.1875 | +8411.0871 ppm | 0.1858 ppm |
| ${}^{141}$Pm | 141 | 80 | 70.5654 | 1170.8556 | -939731.7473 ppm | 132360.4368 | +8382.5223 ppm | 0.1064 ppm |
| ${}^{142}$Pm | 142 | 81 | 76.8712 | 1179.5455 | -934829.8241 ppm | 133293.6964 | +8341.5291 ppm | 0.1785 ppm |
| ${}^{143}$Pm | 143 | 82 | 83.1667 | 1189.4360 | -930078.8658 ppm | 134226.9663 | +8310.2794 ppm | 0.0221 ppm |
| ${}^{144}$Pm | 144 | 83 | 89.4522 | 1195.9628 | -925204.9018 ppm | 135160.2463 | +8254.2386 ppm | 0.0217 ppm |
| ${}^{145}$Pm | 145 | 84 | 95.7277 | 1203.8855 | -920484.4069 ppm | 136093.5362 | +8209.4722 ppm | 0.0208 ppm |
| ${}^{146}$Pm | 146 | 85 | 101.9934 | 1210.1436 | -915717.9297 ppm | 137026.8359 | +8153.0448 ppm | 0.0314 ppm |
| ${}^{147}$Pm | 147 | 86 | 108.2495 | 1217.8026 | -911110.7661 ppm | 137960.1452 | +8107.7761 ppm | 0.0094 ppm |
| ${}^{148}$Pm | 148 | 87 | 114.4962 | 1223.6978 | -906434.2559 ppm | 138893.4640 | +8050.2845 ppm | 0.0413 ppm |
| ${}^{149}$Pm | 149 | 88 | 120.7335 | 1230.9676 | -901919.8199 ppm | 139826.7921 | +8003.6229 ppm | 0.0157 ppm |
| ${}^{150}$Pm | 150 | 89 | 126.9617 | 1236.5719 | -897327.7018 ppm | 140760.1293 | +7945.6284 ppm | 0.1434 ppm |
| ${}^{151}$Pm | 151 | 90 | 133.1808 | 1244.4321 | -892978.6685 ppm | 141693.4757 | +7904.6428 ppm | 0.0328 ppm |
| ${}^{152}$Pm | 152 | 91 | 139.3910 | 1250.3717 | -888520.3613 ppm | 142626.8309 | +7850.5806 ppm | 0.1830 ppm |
| ${}^{153}$Pm | 153 | 92 | 145.5924 | 1257.8365 | -884251.7266 ppm | 143560.1949 | +7808.0802 ppm | 0.0636 ppm |
| ${}^{154}$Pm | 154 | 93 | 151.7852 | 1263.5264 | -879871.7786 ppm | 144493.5675 | +7753.7174 ppm | 0.1745 ppm |
| ${}^{155}$Pm | 155 | 94 | 157.9694 | 1270.2711 | -875641.1632 ppm | 145426.9487 | +7707.4826 ppm | 0.0327 ppm |
| ${}^{156}$Pm | 156 | 95 | 164.1453 | 1275.5693 | -871316.0395 ppm | 146360.3382 | +7651.8639 ppm | 0.0082 ppm |
| ${}^{157}$Pm | 157 | 96 | 170.3129 | 1281.7709 | -867126.8725 ppm | 147293.7361 | +7603.2398 ppm | 0.0479 ppm |
| ${}^{158}$Pm | 158 | 97 | 176.4724 | 1286.6512 | -862843.6755 ppm | 148227.1420 | +7546.2393 ppm | 0.0060 ppm |
| ${}^{159}$Pm | 159 | 98 | 182.6238 | 1292.1708 | -858669.0151 ppm | 149160.5561 | +7494.3625 ppm | 0.0678 ppm |
| ${}^{160}$Pm | 160 | 99 | 188.7673 | 1296.5824 | -854411.6723 ppm | 150093.9780 | +7435.6975 ppm | 0.0138 ppm |
| ${}^{161}$Pm | 161 | 100 | 194.9029 | 1301.8456 | -850287.2071 ppm | 151027.4077 | +7383.5391 ppm | 0.0603 ppm |
| ${}^{162}$Pm | 162 | 101 | 201.0309 | 1305.8820 | -846057.3505 ppm | 151960.8452 | +7323.8078 ppm | 1.9883 ppm |
| ${}^{163}$Pm | 163 | 102 | 207.1513 | 1310.8460 | -841971.2643 ppm | 152894.2902 | +7271.2737 ppm | 2.6326 ppm |
| ${}^{164}$Pm | 164 | 103 | 213.2643 | 1314.2960 | -837734.9894 ppm | 153827.7427 | +7209.4121 ppm | 2.6165 ppm |
| ${}^{165}$Pm | 165 | 104 | 219.3698 | 1318.6800 | -833644.4070 ppm | 154761.2026 | +7154.3172 ppm | 3.2553 ppm |

### Samarium (Z = 62)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{128}$Sm | 128 | 66 | -32.1173 | 1023.7440 | -1031372.3767 ppm | 120247.9867 | +8858.7347 ppm | 4.1967 ppm |
| ${}^{129}$Sm | 129 | 67 | -25.6189 | 1034.9670 | -1024753.3621 ppm | 121181.0537 | +8829.8419 ppm | 4.1643 ppm |
| ${}^{130}$Sm | 130 | 68 | -19.1337 | 1048.4500 | -1018249.5264 ppm | 122114.1339 | +8819.7520 ppm | 3.3013 ppm |
| ${}^{131}$Sm | 131 | 69 | -12.6615 | 1059.1350 | -1011954.5314 ppm | 123047.2271 | +8786.8480 ppm | 3.2762 ppm |
| ${}^{132}$Sm | 132 | 70 | -6.2019 | 1072.1040 | -1005784.8208 ppm | 123980.3330 | +8773.2534 ppm | 2.4405 ppm |
| ${}^{133}$Sm | 133 | 71 | 0.2451 | 1082.2210 | -999773.5200 ppm | 124913.4514 | +8737.4112 ppm | 2.4071 ppm |
| ${}^{134}$Sm | 134 | 72 | 6.6798 | 1094.3780 | -993896.2198 ppm | 125846.5821 | +8718.8080 ppm | 1.5679 ppm |
| ${}^{135}$Sm | 135 | 73 | 13.1025 | 1103.9796 | -988131.5729 ppm | 126779.7248 | +8679.1954 ppm | 1.2302 ppm |
| ${}^{136}$Sm | 136 | 74 | 19.5133 | 1116.0046 | -982515.0535 ppm | 127712.8795 | +8659.9555 ppm | 0.0987 ppm |
| ${}^{137}$Sm | 137 | 75 | 25.9124 | 1125.2567 | -976972.0289 ppm | 128646.0458 | +8619.1587 ppm | 0.2243 ppm |
| ${}^{138}$Sm | 138 | 76 | 32.3000 | 1136.8341 | -971587.7747 ppm | 129579.2236 | +8597.2972 ppm | 0.0920 ppm |
| ${}^{139}$Sm | 139 | 77 | 38.6763 | 1145.7879 | -966244.8038 ppm | 130512.4127 | +8555.3880 ppm | 0.0841 ppm |
| ${}^{140}$Sm | 140 | 78 | 45.0415 | 1156.9350 | -961068.2623 ppm | 131445.6130 | +8531.1338 ppm | 0.0959 ppm |
| ${}^{141}$Sm | 141 | 79 | 51.3957 | 1165.4843 | -955901.8133 ppm | 132378.8241 | +8487.3479 ppm | 0.0650 ppm |
| ${}^{142}$Sm | 142 | 80 | 57.7392 | 1176.6036 | -950927.1948 ppm | 133312.0461 | +8463.8652 ppm | 0.0141 ppm |
| ${}^{143}$Sm | 143 | 81 | 64.0721 | 1185.2101 | -945940.2652 ppm | 134245.2786 | +8421.7550 ppm | 0.0206 ppm |
| ${}^{144}$Sm | 144 | 82 | 70.3946 | 1195.7299 | -941128.3214 ppm | 135178.5215 | +8394.6995 ppm | 0.0109 ppm |
| ${}^{145}$Sm | 145 | 83 | 76.7069 | 1202.4870 | -936209.8275 ppm | 136111.7747 | +8339.9844 ppm | 0.0110 ppm |
| ${}^{146}$Sm | 146 | 84 | 83.0090 | 1210.9033 | -931448.7086 ppm | 137045.0380 | +8298.4030 ppm | 0.0224 ppm |
| ${}^{147}$Sm | 147 | 85 | 89.3012 | 1217.2443 | -926636.6055 ppm | 137978.3112 | +8242.1704 ppm | 0.0092 ppm |
| ${}^{148}$Sm | 148 | 86 | 95.5836 | 1225.3856 | -921997.1466 ppm | 138911.5943 | +8199.9440 ppm | 0.0090 ppm |
| ${}^{149}$Sm | 149 | 87 | 101.8563 | 1231.2568 | -917274.4935 ppm | 139844.8869 | +8141.8550 ppm | 0.0083 ppm |
| ${}^{150}$Sm | 150 | 88 | 108.1196 | 1239.2435 | -912753.5361 ppm | 140778.1891 | +8099.8827 ppm | 0.0080 ppm |
| ${}^{151}$Sm | 151 | 89 | 114.3735 | 1244.8400 | -908121.8923 ppm | 141711.5006 | +8041.3933 ppm | 0.0079 ppm |
| ${}^{152}$Sm | 152 | 90 | 120.6183 | 1253.0978 | -903743.9339 ppm | 142644.8213 | +8002.6976 ppm | 0.0072 ppm |
| ${}^{153}$Sm | 153 | 91 | 126.8539 | 1258.9662 | -899239.6167 ppm | 143578.1510 | +7947.6638 ppm | 0.0072 ppm |
| ${}^{154}$Sm | 154 | 92 | 133.0806 | 1266.9330 | -894958.4297 ppm | 144511.4897 | +7908.1603 ppm | 0.0091 ppm |
| ${}^{155}$Sm | 155 | 93 | 139.2986 | 1272.7400 | -890552.2330 ppm | 145444.8372 | +7854.1433 ppm | 0.0092 ppm |
| ${}^{156}$Sm | 156 | 94 | 145.5078 | 1279.9808 | -886320.3359 ppm | 146378.1934 | +7810.8299 ppm | 0.0587 ppm |
| ${}^{157}$Sm | 157 | 95 | 151.7085 | 1285.3691 | -881972.8215 ppm | 147311.5582 | +7755.3553 ppm | 0.0303 ppm |
| ${}^{158}$Sm | 158 | 96 | 157.9008 | 1292.0146 | -877787.1728 ppm | 148244.9313 | +7709.2548 ppm | 0.0325 ppm |
| ${}^{159}$Sm | 159 | 97 | 164.0847 | 1297.0419 | -873493.1230 ppm | 149178.3128 | +7652.7773 ppm | 0.0401 ppm |
| ${}^{160}$Sm | 160 | 98 | 170.2605 | 1303.1385 | -869345.8156 ppm | 150111.7024 | +7604.2954 ppm | 0.0131 ppm |
| ${}^{161}$Sm | 161 | 99 | 176.4282 | 1307.6487 | -865079.8083 ppm | 151045.1001 | +7545.8088 ppm | 0.0455 ppm |
| ${}^{162}$Sm | 162 | 100 | 182.5880 | 1313.4271 | -860983.5439 ppm | 151978.5058 | +7496.5696 ppm | 0.0234 ppm |
| ${}^{163}$Sm | 163 | 101 | 188.7399 | 1317.7189 | -856767.7168 ppm | 152911.9193 | +7438.1218 ppm | 0.0485 ppm |
| ${}^{164}$Sm | 164 | 102 | 194.8841 | 1323.1160 | -852708.2431 ppm | 153845.3405 | +7387.7305 ppm | 0.0268 ppm |
| ${}^{165}$Sm | 165 | 103 | 201.0206 | 1326.7650 | -848488.1406 ppm | 154778.7694 | +7326.5881 ppm | 2.6007 ppm |
| ${}^{166}$Sm | 166 | 104 | 207.1497 | 1331.8180 | -844460.9795 ppm | 155712.2058 | +7275.0654 ppm | 2.5850 ppm |
| ${}^{167}$Sm | 167 | 105 | 213.2713 | 1334.6640 | -840206.0115 ppm | 156645.6496 | +7210.8654 ppm | 3.2163 ppm |
| ${}^{168}$Sm | 168 | 106 | 219.3856 | 1339.1280 | -836172.8056 ppm | 157579.1007 | +7156.6909 ppm | 1.9171 ppm |

### Europium (Z = 63)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{130}$Eu | 130 | 67 | -39.0223 | 1033.5000 | -1037757.4365 ppm | 122133.2402 | +8859.3560 ppm | 4.4474 ppm |
| ${}^{131}$Eu | 131 | 68 | -32.5075 | 1047.4760 | -1031034.0910 ppm | 123066.2908 | +8853.6761 ppm | 3.2759 ppm |
| ${}^{132}$Eu | 132 | 69 | -26.0058 | 1058.3760 | -1024571.3811 ppm | 123999.3545 | +8821.8121 ppm | 3.2511 ppm |
| ${}^{133}$Eu | 133 | 70 | -19.5170 | 1071.4480 | -1018215.5074 ppm | 124932.4311 | +8809.2568 ppm | 2.4069 ppm |
| ${}^{134}$Eu | 134 | 71 | -13.0409 | 1082.0500 | -1012052.0057 ppm | 125865.5205 | +8777.0092 ppm | 2.4039 ppm |
| ${}^{135}$Eu | 135 | 72 | -6.5773 | 1094.4450 | -1006009.6733 ppm | 126798.6223 | +8759.6453 ppm | 1.5562 ppm |
| ${}^{136}$Eu | 136 | 73 | -0.1259 | 1104.5920 | -1000113.9900 ppm | 127731.7363 | +8724.6973 ppm | 1.5448 ppm |
| ${}^{137}$Eu | 137 | 74 | 6.3134 | 1116.6286 | -994346.0476 ppm | 128664.8625 | +8704.6382 ppm | 0.0343 ppm |
| ${}^{138}$Eu | 138 | 75 | 12.7408 | 1126.3037 | -988687.9758 ppm | 129598.0005 | +8666.9163 ppm | 0.2175 ppm |
| ${}^{139}$Eu | 139 | 76 | 19.1565 | 1138.0234 | -983166.8561 ppm | 130531.1502 | +8645.7622 ppm | 0.1016 ppm |
| ${}^{140}$Eu | 140 | 77 | 25.5608 | 1147.6826 | -977728.3674 ppm | 131464.3114 | +8609.0528 ppm | 0.3954 ppm |
| ${}^{141}$Eu | 141 | 78 | 31.9537 | 1158.6936 | -972422.6302 ppm | 132397.4838 | +8583.3356 ppm | 0.0963 ppm |
| ${}^{142}$Eu | 142 | 79 | 38.3356 | 1168.1482 | -967182.6203 ppm | 133330.6674 | +8546.1899 ppm | 0.2274 ppm |
| ${}^{143}$Eu | 143 | 80 | 44.7065 | 1179.1519 | -962085.9144 ppm | 134263.8619 | +8521.3805 ppm | 0.0825 ppm |
| ${}^{144}$Eu | 144 | 81 | 51.0666 | 1188.6011 | -957036.3809 ppm | 135197.0672 | +8485.3007 ppm | 0.0805 ppm |
| ${}^{145}$Eu | 145 | 82 | 57.4161 | 1199.0448 | -952115.0929 ppm | 136130.2831 | +8457.2262 ppm | 0.0227 ppm |
| ${}^{146}$Eu | 146 | 83 | 63.7553 | 1206.2422 | -947145.5545 ppm | 137063.5094 | +8405.5273 ppm | 0.0442 ppm |
| ${}^{147}$Eu | 147 | 84 | 70.0841 | 1214.7405 | -942305.2861 ppm | 137996.7460 | +8364.1934 ppm | 0.0188 ppm |
| ${}^{148}$Eu | 148 | 85 | 76.4028 | 1221.5647 | -937454.9361 ppm | 138929.9927 | +8311.2400 ppm | 0.0723 ppm |
| ${}^{149}$Eu | 149 | 86 | 82.7116 | 1229.7798 | -932742.7400 ppm | 139863.2493 | +8269.1807 ppm | 0.0281 ppm |
| ${}^{150}$Eu | 150 | 87 | 89.0106 | 1236.2022 | -927996.7312 ppm | 140796.5157 | +8214.8093 ppm | 0.0446 ppm |
| ${}^{151}$Eu | 151 | 88 | 95.2999 | 1244.1343 | -923400.6123 ppm | 141729.7918 | +8172.0548 ppm | 0.0083 ppm |
| ${}^{152}$Eu | 152 | 89 | 101.5797 | 1250.4410 | -918764.8695 ppm | 142663.0775 | +8118.3519 ppm | 0.0082 ppm |
| ${}^{153}$Eu | 153 | 90 | 107.8502 | 1258.9913 | -914336.0370 ppm | 143596.3724 | +8081.2957 ppm | 0.0082 ppm |
| ${}^{154}$Eu | 154 | 91 | 114.1114 | 1265.4335 | -909824.2631 ppm | 144529.6766 | +8029.9641 ppm | 0.0083 ppm |
| ${}^{155}$Eu | 155 | 92 | 120.3635 | 1273.5848 | -905492.3372 ppm | 145462.9899 | +7991.2969 ppm | 0.0087 ppm |
| ${}^{156}$Eu | 156 | 93 | 126.6067 | 1279.9206 | -901082.3914 ppm | 146396.3122 | +7940.5884 ppm | 0.0243 ppm |
| ${}^{157}$Eu | 157 | 94 | 132.8410 | 1287.3682 | -896811.9472 ppm | 147329.6433 | +7898.2537 ppm | 0.0290 ppm |
| ${}^{158}$Eu | 158 | 95 | 139.0667 | 1293.2509 | -892467.3814 ppm | 148262.9831 | +7845.7928 ppm | 0.0138 ppm |
| ${}^{159}$Eu | 159 | 96 | 145.2837 | 1300.0951 | -888251.4766 ppm | 149196.3314 | +7800.5978 ppm | 0.0292 ppm |
| ${}^{160}$Eu | 160 | 97 | 151.4923 | 1305.6165 | -883968.7527 ppm | 150129.6883 | +7747.0767 ppm | 0.0061 ppm |
| ${}^{161}$Eu | 161 | 98 | 157.6926 | 1311.9859 | -879806.1996 ppm | 151063.0534 | +7699.9792 ppm | 0.0694 ppm |
| ${}^{162}$Eu | 162 | 99 | 163.8846 | 1316.9886 | -875561.0894 ppm | 151996.4268 | +7644.3884 ppm | 0.0087 ppm |
| ${}^{163}$Eu | 163 | 100 | 170.0686 | 1322.9108 | -871443.6553 ppm | 152929.8083 | +7595.6400 ppm | 0.0060 ppm |
| ${}^{164}$Eu | 164 | 101 | 176.2445 | 1327.6405 | -867249.7974 ppm | 153863.1977 | +7539.6718 ppm | 0.0135 ppm |
| ${}^{165}$Eu | 165 | 102 | 182.4126 | 1333.2087 | -863177.7465 ppm | 154796.5951 | +7489.9351 ppm | 0.0339 ppm |
| ${}^{166}$Eu | 166 | 103 | 188.5729 | 1337.2960 | -858989.3805 ppm | 155730.0002 | +7431.2227 ppm | 0.6448 ppm |
| ${}^{167}$Eu | 167 | 104 | 194.7256 | 1342.3460 | -854936.3656 ppm | 156663.4129 | +7379.7518 ppm | 2.5696 ppm |
| ${}^{168}$Eu | 168 | 105 | 200.8707 | 1346.0160 | -850766.4969 ppm | 157596.8333 | +7319.0242 ppm | 2.5542 ppm |
| ${}^{169}$Eu | 169 | 106 | 207.0083 | 1350.4790 | -846714.8914 ppm | 158530.2611 | +7265.0159 ppm | 3.1782 ppm |
| ${}^{170}$Eu | 170 | 107 | 213.1386 | 1353.7100 | -842552.2440 ppm | 159463.6962 | +7203.9942 ppm | 3.1594 ppm |

### Gadolinium (Z = 64)

_40 of 40 isotopes with a framework prediction; 40 of 40 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{133}$Gd | 133 | 69 | -39.5566 | 1059.4780 | -1037335.8976 ppm | 124951.6884 | +8873.7104 ppm | 4.0388 ppm |
| ${}^{134}$Gd | 134 | 70 | -33.0384 | 1073.0720 | -1030788.6531 ppm | 125884.7357 | +8864.1387 ppm | 3.2026 ppm |
| ${}^{135}$Gd | 135 | 71 | -26.5332 | 1083.7800 | -1024482.0963 ppm | 126817.7959 | +8832.7425 ppm | 3.1789 ppm |
| ${}^{136}$Gd | 136 | 72 | -20.0406 | 1096.7040 | -1018273.5180 ppm | 127750.8687 | +8818.7960 ppm | 2.3539 ppm |
| ${}^{137}$Gd | 137 | 73 | -13.5605 | 1106.9600 | -1012250.2464 ppm | 128683.9541 | +8783.6691 ppm | 2.3367 ppm |
| ${}^{138}$Gd | 138 | 74 | -7.0927 | 1119.4560 | -1006335.8254 ppm | 129617.0516 | +8767.3769 ppm | 1.5586 ppm |
| ${}^{139}$Gd | 139 | 75 | -0.6369 | 1129.5140 | -1000563.8481 ppm | 130550.1612 | +8732.1274 ppm | 1.5115 ppm |
| ${}^{140}$Gd | 140 | 76 | 5.8071 | 1141.6966 | -994913.6453 ppm | 131483.2827 | +8714.3321 ppm | 0.2144 ppm |
| ${}^{141}$Gd | 141 | 77 | 12.2394 | 1151.2099 | -989368.2646 ppm | 132416.4159 | +8676.0636 ppm | 0.1505 ppm |
| ${}^{142}$Gd | 142 | 78 | 18.6602 | 1163.0165 | -983955.3713 ppm | 133349.5605 | +8655.9169 ppm | 0.2114 ppm |
| ${}^{143}$Gd | 143 | 79 | 25.0697 | 1172.3596 | -978616.0460 ppm | 134282.7164 | +8617.4724 ppm | 1.5045 ppm |
| ${}^{144}$Gd | 144 | 80 | 31.4681 | 1183.9591 | -973421.3071 ppm | 135215.8834 | +8596.6195 ppm | 0.2084 ppm |
| ${}^{145}$Gd | 145 | 81 | 37.8555 | 1193.1975 | -968273.8631 ppm | 136149.0614 | +8558.4941 ppm | 0.1460 ppm |
| ${}^{146}$Gd | 146 | 82 | 44.2322 | 1204.4281 | -963275.3131 ppm | 137082.2501 | +8535.7507 ppm | 0.0300 ppm |
| ${}^{147}$Gd | 147 | 83 | 50.5983 | 1211.7705 | -958244.2897 ppm | 138015.4494 | +8484.7410 ppm | 0.0138 ppm |
| ${}^{148}$Gd | 148 | 84 | 56.9540 | 1220.7543 | -953345.2438 ppm | 138948.6592 | +8446.5105 ppm | 0.0106 ppm |
| ${}^{149}$Gd | 149 | 85 | 63.2994 | 1227.6834 | -948439.9843 ppm | 139881.8792 | +8393.9300 ppm | 0.0239 ppm |
| ${}^{150}$Gd | 150 | 86 | 69.6346 | 1236.3915 | -943679.1431 ppm | 140815.1094 | +8354.9706 ppm | 0.0434 ppm |
| ${}^{151}$Gd | 151 | 87 | 75.9599 | 1242.8877 | -938884.3260 ppm | 141748.3495 | +8300.7325 ppm | 0.0213 ppm |
| ${}^{152}$Gd | 152 | 88 | 82.2754 | 1251.4774 | -934257.3894 ppm | 142681.5995 | +8262.1949 ppm | 0.0071 ppm |
| ${}^{153}$Gd | 153 | 89 | 88.5812 | 1257.7244 | -929570.2662 ppm | 143614.8591 | +8207.6471 ppm | 0.0070 ppm |
| ${}^{154}$Gd | 154 | 90 | 94.8775 | 1266.6191 | -925093.9258 ppm | 144548.1282 | +8172.4938 ppm | 0.0069 ppm |
| ${}^{155}$Gd | 155 | 91 | 101.1644 | 1273.0544 | -920534.1475 ppm | 145481.4068 | +8120.6772 ppm | 0.0068 ppm |
| ${}^{156}$Gd | 156 | 92 | 107.4420 | 1281.5907 | -916165.1355 ppm | 146414.6946 | +8084.1732 ppm | 0.0068 ppm |
| ${}^{157}$Gd | 157 | 93 | 113.7105 | 1287.9506 | -911712.0618 ppm | 147347.9915 | +8033.1871 ppm | 0.0067 ppm |
| ${}^{158}$Gd | 158 | 94 | 119.9700 | 1295.8880 | -907422.5247 ppm | 148281.2974 | +7993.7182 ppm | 0.0066 ppm |
| ${}^{159}$Gd | 159 | 95 | 126.2207 | 1301.8312 | -903043.7124 ppm | 149214.6121 | +7941.2280 ppm | 0.0066 ppm |
| ${}^{160}$Gd | 160 | 96 | 132.4627 | 1309.2827 | -898828.0603 ppm | 150147.9356 | +7899.6592 ppm | 0.0075 ppm |
| ${}^{161}$Gd | 161 | 97 | 138.6960 | 1314.9181 | -894521.1733 ppm | 151081.2676 | +7846.4543 ppm | 0.0100 ppm |
| ${}^{162}$Gd | 162 | 98 | 144.9209 | 1321.7640 | -890357.9738 ppm | 152014.6082 | +7802.0523 ppm | 0.0263 ppm |
| ${}^{163}$Gd | 163 | 99 | 151.1374 | 1326.9432 | -886101.0885 ppm | 152947.9571 | +7747.1842 ppm | 0.0052 ppm |
| ${}^{164}$Gd | 164 | 100 | 157.3456 | 1333.3196 | -881989.5552 ppm | 153881.3143 | +7700.9420 ppm | 0.0065 ppm |
| ${}^{165}$Gd | 165 | 101 | 163.5458 | 1338.2231 | -877788.8608 ppm | 154814.6796 | +7645.6538 ppm | 0.0085 ppm |
| ${}^{166}$Gd | 166 | 102 | 169.7379 | 1344.1395 | -873720.0541 ppm | 155748.0529 | +7597.6896 ppm | 0.0102 ppm |
| ${}^{167}$Gd | 167 | 103 | 175.9221 | 1348.6156 | -869553.6012 ppm | 156681.4341 | +7541.0203 ppm | 0.0335 ppm |
| ${}^{168}$Gd | 168 | 104 | 182.0984 | 1354.0800 | -865518.6987 ppm | 157614.8232 | +7491.3206 ppm | 1.9173 ppm |
| ${}^{169}$Gd | 169 | 105 | 188.2671 | 1357.9150 | -861355.7339 ppm | 158548.2199 | +7431.8009 ppm | 2.5392 ppm |
| ${}^{170}$Gd | 170 | 106 | 194.4282 | 1362.8900 | -857341.2216 ppm | 159481.6242 | +7380.7916 ppm | 3.1596 ppm |
| ${}^{171}$Gd | 171 | 107 | 200.5818 | 1366.2900 | -853192.3503 ppm | 160415.0361 | +7320.3112 ppm | 3.1411 ppm |
| ${}^{172}$Gd | 172 | 108 | 206.7280 | 1371.1840 | -849233.9234 ppm | 161348.4553 | +7269.3875 ppm | 1.8725 ppm |

### Terbium (Z = 65)

_40 of 40 isotopes with a framework prediction; 40 of 40 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{135}$Tb | 135 | 70 | -46.7653 | 1071.7650 | -1043633.9553 ppm | 126837.2457 | +8897.6044 ppm | 3.1786 ppm |
| ${}^{136}$Tb | 136 | 71 | -40.2309 | 1082.6960 | -1037158.0777 ppm | 127770.2767 | +8866.9743 ppm | 3.9496 ppm |
| ${}^{137}$Tb | 137 | 72 | -33.7093 | 1095.8630 | -1030760.5186 ppm | 128703.3205 | +8854.4518 ppm | 3.1397 ppm |
| ${}^{138}$Tb | 138 | 73 | -27.2004 | 1106.6220 | -1024579.6395 ppm | 129636.3770 | +8823.0995 ppm | 2.3341 ppm |
| ${}^{139}$Tb | 139 | 74 | -20.7039 | 1119.2280 | -1018498.3414 ppm | 130569.4459 | +8807.0751 ppm | 2.3030 ppm |
| ${}^{140}$Tb | 140 | 75 | -14.2196 | 1129.6142 | -1012588.0026 ppm | 131502.5270 | +8774.5188 ppm | 6.1407 ppm |
| ${}^{141}$Tb | 141 | 76 | -7.7473 | 1141.7441 | -1006785.5378 ppm | 132435.6202 | +8755.6276 ppm | 0.8018 ppm |
| ${}^{142}$Tb | 142 | 77 | -1.2870 | 1151.8341 | -1001117.3060 ppm | 133368.7252 | +8721.5277 ppm | 5.2986 ppm |
| ${}^{143}$Tb | 143 | 78 | 5.1618 | 1163.7651 | -995564.5755 ppm | 134301.8419 | +8701.9387 ppm | 0.3848 ppm |
| ${}^{144}$Tb | 144 | 79 | 11.5991 | 1173.7854 | -990118.2389 ppm | 135234.9701 | +8668.3315 ppm | 0.2084 ppm |
| ${}^{145}$Tb | 145 | 80 | 18.0251 | 1185.8883 | -984800.3773 ppm | 136168.1095 | +8650.8299 ppm | 0.8214 ppm |
| ${}^{146}$Tb | 146 | 81 | 24.4399 | 1195.3235 | -979553.7118 ppm | 137101.2601 | +8613.8551 ppm | 0.3300 ppm |
| ${}^{147}$Tb | 147 | 82 | 30.8439 | 1206.3739 | -974432.5819 ppm | 138034.4215 | +8589.3651 ppm | 0.0592 ppm |
| ${}^{148}$Tb | 148 | 83 | 37.2370 | 1214.2395 | -969333.0417 ppm | 138967.5938 | +8541.9723 ppm | 0.0904 ppm |
| ${}^{149}$Tb | 149 | 84 | 43.6196 | 1223.2625 | -964341.5929 ppm | 139900.7767 | +8503.7069 ppm | 0.0262 ppm |
| ${}^{150}$Tb | 150 | 85 | 49.9917 | 1230.9509 | -959387.7332 ppm | 140833.9700 | +8456.3892 ppm | 0.0528 ppm |
| ${}^{151}$Tb | 151 | 86 | 56.3535 | 1239.5400 | -954536.7332 ppm | 141767.1736 | +8416.2320 ppm | 0.0291 ppm |
| ${}^{152}$Tb | 152 | 87 | 62.7052 | 1246.7051 | -949703.2312 ppm | 142700.3873 | +8366.5281 ppm | 0.2827 ppm |
| ${}^{153}$Tb | 153 | 88 | 69.0470 | 1255.3727 | -944998.8386 ppm | 143633.6110 | +8328.1808 ppm | 0.0277 ppm |
| ${}^{154}$Tb | 154 | 89 | 75.3788 | 1262.2871 | -940283.9163 ppm | 144566.8445 | +8278.0708 ppm | 0.3160 ppm |
| ${}^{155}$Tb | 155 | 90 | 81.7010 | 1271.4522 | -935741.9452 ppm | 145500.0877 | +8244.3999 ppm | 0.0681 ppm |
| ${}^{156}$Tb | 156 | 91 | 88.0137 | 1278.3641 | -931151.3047 ppm | 146433.3405 | +8195.5856 ppm | 0.0259 ppm |
| ${}^{157}$Tb | 157 | 92 | 94.3169 | 1287.1082 | -926721.8214 ppm | 147366.6027 | +8160.0955 ppm | 0.0070 ppm |
| ${}^{158}$Tb | 158 | 93 | 100.6109 | 1293.8866 | -922241.3109 ppm | 148299.8741 | +8111.6459 ppm | 0.0086 ppm |
| ${}^{159}$Tb | 159 | 94 | 106.8958 | 1302.0196 | -917900.0334 ppm | 149233.1547 | +8073.0932 ppm | 0.0075 ppm |
| ${}^{160}$Tb | 160 | 95 | 113.1716 | 1308.3948 | -913503.4790 ppm | 150166.4443 | +8023.1885 ppm | 0.0074 ppm |
| ${}^{161}$Tb | 161 | 96 | 119.4386 | 1316.0914 | -909247.5241 ppm | 151099.7428 | +7982.8499 ppm | 0.0081 ppm |
| ${}^{162}$Tb | 162 | 97 | 125.6968 | 1322.5805 | -904960.9795 ppm | 152033.0500 | +7934.9985 ppm | 0.0136 ppm |
| ${}^{163}$Tb | 163 | 98 | 131.9463 | 1329.3680 | -900745.0728 ppm | 152966.3658 | +7889.7742 ppm | 0.0267 ppm |
| ${}^{164}$Tb | 164 | 99 | 138.1874 | 1334.9486 | -896484.8597 ppm | 153899.6902 | +7837.1921 ppm | 0.0122 ppm |
| ${}^{165}$Tb | 165 | 100 | 144.4201 | 1341.5038 | -892344.6494 ppm | 154833.0230 | +7791.6971 ppm | 0.0100 ppm |
| ${}^{166}$Tb | 166 | 101 | 150.6445 | 1346.7950 | -888145.9694 ppm | 155766.3640 | +7738.5645 ppm | 0.0095 ppm |
| ${}^{167}$Tb | 167 | 102 | 156.8607 | 1352.9406 | -884059.4522 ppm | 156699.7132 | +7691.6592 ppm | 0.0124 ppm |
| ${}^{168}$Tb | 168 | 103 | 163.0689 | 1357.9101 | -879911.8878 ppm | 157633.0704 | +7637.7891 ppm | 0.0268 ppm |
| ${}^{169}$Tb | 169 | 104 | 169.2691 | 1363.6610 | -875871.5771 ppm | 158566.4356 | +7589.7388 ppm | 1.9059 ppm |
| ${}^{170}$Tb | 170 | 105 | 175.4615 | 1367.9900 | -871737.7422 ppm | 159499.8086 | +7532.9494 ppm | 1.8947 ppm |
| ${}^{171}$Tb | 171 | 106 | 181.6462 | 1373.1300 | -867713.7990 ppm | 160433.1894 | +7482.1324 ppm | 2.5095 ppm |
| ${}^{172}$Tb | 172 | 107 | 187.8232 | 1377.0320 | -863602.8882 ppm | 161366.5778 | +7424.7850 ppm | 3.1229 ppm |
| ${}^{173}$Tb | 173 | 108 | 193.9927 | 1381.9240 | -859621.2988 ppm | 162299.9737 | +7373.7766 ppm | 3.1047 ppm |
| ${}^{174}$Tb | 174 | 109 | 200.1548 | 1385.5620 | -855542.5336 ppm | 163233.3770 | +7314.9485 ppm | 3.0868 ppm |

### Dysprosium (Z = 66)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{138}$Dy | 138 | 72 | -47.5823 | 1097.1000 | -1043370.9793 ppm | 129655.9766 | +8907.5567 ppm | 3.9141 ppm |
| ${}^{139}$Dy | 139 | 73 | -41.0445 | 1107.9690 | -1037044.7643 ppm | 130589.0041 | +8876.8871 ppm | 3.8644 ppm |
| ${}^{140}$Dy | 140 | 74 | -34.5192 | 1121.1200 | -1030789.9397 ppm | 131522.0443 | +8865.0174 ppm | 3.0724 ppm |
| ${}^{141}$Dy | 141 | 75 | -28.0064 | 1131.8070 | -1024744.8528 ppm | 132455.0969 | +8833.6051 ppm | 2.2703 ppm |
| ${}^{142}$Dy | 142 | 76 | -21.5058 | 1144.6620 | -1018787.8975 ppm | 133388.1618 | +8819.3994 ppm | 5.5091 ppm |
| ${}^{143}$Dy | 143 | 77 | -15.0172 | 1154.7325 | -1013004.9217 ppm | 134321.2386 | +8785.1118 ppm | 0.0979 ppm |
| ${}^{144}$Dy | 144 | 78 | -8.5404 | 1167.2050 | -1007317.0086 ppm | 135254.3273 | +8769.0846 ppm | 0.0535 ppm |
| ${}^{145}$Dy | 145 | 79 | -2.0753 | 1176.9488 | -1001763.3175 ppm | 136187.4276 | +8732.9760 ppm | 0.0483 ppm |
| ${}^{146}$Dy | 146 | 80 | 4.3783 | 1189.3325 | -996318.6748 ppm | 137120.5393 | +8717.0341 ppm | 0.0492 ppm |
| ${}^{147}$Dy | 147 | 81 | 10.8207 | 1199.0449 | -990975.5748 ppm | 138053.6624 | +8681.7038 ppm | 0.0647 ppm |
| ${}^{148}$Dy | 148 | 82 | 17.2520 | 1210.7796 | -985751.3670 ppm | 138986.7965 | +8661.7337 ppm | 0.0633 ppm |
| ${}^{149}$Dy | 149 | 83 | 23.6723 | 1218.6855 | -980575.5641 ppm | 139919.9416 | +8614.2714 ppm | 0.0662 ppm |
| ${}^{150}$Dy | 150 | 84 | 30.0818 | 1228.3724 | -975510.8223 ppm | 140853.0975 | +8580.3819 ppm | 0.0309 ppm |
| ${}^{151}$Dy | 151 | 85 | 36.4808 | 1235.8865 | -970482.1003 ppm | 141786.2640 | +8531.4285 ppm | 0.0231 ppm |
| ${}^{152}$Dy | 152 | 86 | 42.8693 | 1245.3234 | -965575.7947 ppm | 142719.4409 | +8496.8961 ppm | 0.0325 ppm |
| ${}^{153}$Dy | 153 | 87 | 49.2475 | 1252.4200 | -960678.1509 ppm | 143652.6281 | +8446.3186 ppm | 0.0281 ppm |
| ${}^{154}$Dy | 154 | 88 | 55.6155 | 1261.7421 | -955921.6350 ppm | 144585.8255 | +8412.1223 ppm | 0.0518 ppm |
| ${}^{155}$Dy | 155 | 89 | 61.9736 | 1268.5753 | -951147.0897 ppm | 145519.0329 | +8361.0450 ppm | 0.0668 ppm |
| ${}^{156}$Dy | 156 | 90 | 68.3218 | 1278.0201 | -946540.8878 ppm | 146452.2501 | +8328.8214 ppm | 0.0068 ppm |
| ${}^{157}$Dy | 157 | 91 | 74.6603 | 1284.9867 | -941897.9654 ppm | 147385.4770 | +8279.9802 ppm | 0.0353 ppm |
| ${}^{158}$Dy | 158 | 92 | 80.9893 | 1294.0405 | -937413.6267 ppm | 148318.7134 | +8246.1285 ppm | 0.0159 ppm |
| ${}^{159}$Dy | 159 | 93 | 87.3088 | 1300.8719 | -932884.3682 ppm | 149251.9593 | +8197.6303 ppm | 0.0097 ppm |
| ${}^{160}$Dy | 160 | 94 | 93.6191 | 1309.4484 | -928504.9457 ppm | 150185.2145 | +8161.6120 ppm | 0.0047 ppm |
| ${}^{161}$Dy | 161 | 95 | 99.9202 | 1315.9028 | -924067.2067 ppm | 151118.4788 | +8111.8304 ppm | 0.0046 ppm |
| ${}^{162}$Dy | 162 | 96 | 106.2122 | 1324.0998 | -919785.3234 ppm | 152051.7522 | +8074.3708 ppm | 0.0046 ppm |
| ${}^{163}$Dy | 163 | 97 | 112.4954 | 1330.3708 | -915440.5698 ppm | 152985.0344 | +8024.6373 ppm | 0.0046 ppm |
| ${}^{164}$Dy | 164 | 98 | 118.7698 | 1338.0289 | -911235.2678 ppm | 153918.3255 | +7984.7255 ppm | 0.0046 ppm |
| ${}^{165}$Dy | 165 | 99 | 125.0355 | 1343.7449 | -906949.9667 ppm | 154851.6252 | +7932.6123 ppm | 0.0045 ppm |
| ${}^{166}$Dy | 166 | 100 | 131.2927 | 1350.7884 | -902802.9126 ppm | 155784.9334 | +7889.8407 ppm | 0.0052 ppm |
| ${}^{167}$Dy | 167 | 101 | 137.5415 | 1356.1867 | -898582.2019 ppm | 156718.2501 | +7836.9730 ppm | 0.0258 ppm |
| ${}^{168}$Dy | 168 | 102 | 143.7819 | 1362.9049 | -894503.3307 ppm | 157651.5750 | +7793.2935 ppm | 0.8950 ppm |
| ${}^{169}$Dy | 169 | 103 | 150.0142 | 1368.0139 | -890341.6068 ppm | 158584.9082 | +7739.8779 ppm | 1.9106 ppm |
| ${}^{170}$Dy | 170 | 104 | 156.2384 | 1374.2800 | -886312.5474 ppm | 159518.2494 | +7693.9957 ppm | 1.2651 ppm |
| ${}^{171}$Dy | 171 | 105 | 162.4546 | 1378.6020 | -882159.8922 ppm | 160451.5986 | +7637.2233 ppm | 1.2577 ppm |
| ${}^{172}$Dy | 172 | 106 | 168.6630 | 1384.4280 | -878171.3777 ppm | 161384.9557 | +7590.2809 ppm | 1.8727 ppm |
| ${}^{173}$Dy | 173 | 107 | 174.8635 | 1388.4980 | -874062.8079 ppm | 162318.3205 | +7532.8681 ppm | 2.4804 ppm |
| ${}^{174}$Dy | 174 | 108 | 181.0565 | 1393.9140 | -870109.3030 ppm | 163251.6930 | +7484.9282 ppm | 3.0870 ppm |
| ${}^{175}$Dy | 175 | 109 | 187.2418 | 1397.5500 | -866021.3798 ppm | 164185.0731 | +7426.5171 ppm | 3.0693 ppm |
| ${}^{176}$Dy | 176 | 110 | 193.4197 | 1402.5440 | -862093.6548 ppm | 165118.4606 | +7376.6903 ppm | 3.0518 ppm |

### Holmium (Z = 67)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{140}$Ho | 140 | 73 | -55.0918 | 1106.8400 | -1049773.9660 ppm | 131541.8346 | +8912.2504 ppm | 3.8366 ppm |
| ${}^{141}$Ho | 141 | 74 | -48.5378 | 1119.9630 | -1043338.7443 ppm | 132474.8460 | +8899.3599 ppm | 3.0504 ppm |
| ${}^{142}$Ho | 142 | 75 | -41.9964 | 1131.0300 | -1037131.0714 ppm | 133407.8700 | +8870.2574 ppm | 3.0290 ppm |
| ${}^{143}$Ho | 143 | 76 | -35.4673 | 1143.8570 | -1031006.7711 ppm | 134340.9064 | +8856.1349 ppm | 2.2385 ppm |
| ${}^{144}$Ho | 144 | 77 | -28.9505 | 1154.4621 | -1025077.0156 ppm | 135273.9549 | +8825.4810 ppm | 0.0632 ppm |
| ${}^{145}$Ho | 145 | 78 | -22.4456 | 1167.0440 | -1019232.8801 ppm | 136207.0155 | +8809.8977 ppm | 0.0552 ppm |
| ${}^{146}$Ho | 146 | 79 | -15.9526 | 1177.2334 | -1013550.9114 ppm | 137140.0879 | +8776.8605 ppm | 0.0484 ppm |
| ${}^{147}$Ho | 147 | 80 | -9.4712 | 1189.8236 | -1007960.1598 ppm | 138073.1719 | +8762.0503 ppm | 0.0365 ppm |
| ${}^{148}$Ho | 148 | 81 | -3.0012 | 1200.1290 | -1002500.7631 ppm | 139006.2674 | +8730.7971 ppm | 0.6084 ppm |
| ${}^{149}$Ho | 149 | 82 | 3.4574 | 1211.8550 | -997146.9913 ppm | 139939.3742 | +8710.3731 ppm | 0.0864 ppm |
| ${}^{150}$Ho | 150 | 83 | 9.9050 | 1220.2263 | -991882.6543 ppm | 140872.4920 | +8666.0715 ppm | 0.1014 ppm |
| ${}^{151}$Ho | 151 | 84 | 16.3416 | 1229.9745 | -986713.8482 ppm | 141805.6208 | +8632.3120 ppm | 0.0590 ppm |
| ${}^{152}$Ho | 152 | 85 | 22.7675 | 1238.0277 | -981609.8748 ppm | 142738.7604 | +8586.9926 ppm | 0.0885 ppm |
| ${}^{153}$Ho | 153 | 86 | 29.1827 | 1247.5065 | -976607.1518 ppm | 143671.9105 | +8552.4330 ppm | 0.0356 ppm |
| ${}^{154}$Ho | 154 | 87 | 35.5875 | 1255.2051 | -971648.0434 ppm | 144605.0712 | +8505.8740 ppm | 0.0573 ppm |
| ${}^{155}$Ho | 155 | 88 | 41.9820 | 1264.6769 | -966804.1595 ppm | 145538.2421 | +8472.3778 ppm | 0.1210 ppm |
| ${}^{156}$Ho | 156 | 89 | 48.3664 | 1272.2468 | -961983.5135 ppm | 146471.4232 | +8426.1765 ppm | 0.2645 ppm |
| ${}^{157}$Ho | 157 | 90 | 54.7407 | 1281.6126 | -957287.6442 ppm | 147404.6143 | +8393.0210 ppm | 0.1605 ppm |
| ${}^{158}$Ho | 158 | 91 | 61.1052 | 1289.0384 | -952596.3122 ppm | 148337.8152 | +8347.0547 ppm | 0.1843 ppm |
| ${}^{159}$Ho | 159 | 92 | 67.4599 | 1298.2519 | -948037.8665 ppm | 149271.0259 | +8313.9089 ppm | 0.0206 ppm |
| ${}^{160}$Ho | 160 | 93 | 73.8051 | 1305.3761 | -943460.6365 ppm | 150204.2461 | +8267.0996 ppm | 0.1008 ppm |
| ${}^{161}$Ho | 161 | 94 | 80.1409 | 1314.2613 | -939022.1073 ppm | 151137.4758 | +8232.7802 ppm | 0.0143 ppm |
| ${}^{162}$Ho | 162 | 95 | 86.4673 | 1321.1768 | -934552.8001 ppm | 152070.7148 | +8185.7811 ppm | 0.0206 ppm |
| ${}^{163}$Ho | 163 | 96 | 92.7846 | 1329.5856 | -930215.4073 ppm | 153003.9629 | +8149.3390 ppm | 0.0046 ppm |
| ${}^{164}$Ho | 164 | 97 | 99.0928 | 1336.2594 | -925843.1367 ppm | 153937.2201 | +8101.9463 ppm | 0.0091 ppm |
| ${}^{165}$Ho | 165 | 98 | 105.3921 | 1344.2483 | -921597.7389 ppm | 154870.4862 | +8063.8158 ppm | 0.0051 ppm |
| ${}^{166}$Ho | 166 | 99 | 111.6826 | 1350.4919 | -917302.2830 ppm | 155803.7612 | +8014.8203 ppm | 0.0051 ppm |
| ${}^{167}$Ho | 167 | 100 | 117.9644 | 1357.7723 | -913119.1529 ppm | 156737.0448 | +7973.1895 ppm | 0.0334 ppm |
| ${}^{168}$Ho | 168 | 101 | 124.2377 | 1363.6234 | -908891.5170 ppm | 157670.3370 | +7922.8999 ppm | 0.1918 ppm |
| ${}^{169}$Ho | 169 | 102 | 130.5025 | 1370.4315 | -904772.7182 ppm | 158603.6376 | +7879.3902 ppm | 0.1274 ppm |
| ${}^{170}$Ho | 170 | 103 | 136.7589 | 1375.9443 | -900607.2133 ppm | 159536.9465 | +7828.1992 ppm | 0.3160 ppm |
| ${}^{171}$Ho | 171 | 104 | 143.0072 | 1382.2960 | -896543.7221 ppm | 160470.2637 | +7782.9693 ppm | 3.7681 ppm |
| ${}^{172}$Ho | 172 | 105 | 149.2473 | 1387.3520 | -892422.8770 ppm | 161403.5890 | +7730.0467 ppm | 1.2213 ppm |
| ${}^{173}$Ho | 173 | 106 | 155.4795 | 1393.3420 | -888412.5544 ppm | 162336.9223 | +7683.4237 ppm | 1.8503 ppm |
| ${}^{174}$Ho | 174 | 107 | 161.7037 | 1397.9160 | -884325.1571 ppm | 163270.2634 | +7629.0048 ppm | 1.8511 ppm |
| ${}^{175}$Ho | 175 | 108 | 167.9202 | 1403.3250 | -880341.2201 ppm | 164203.6124 | +7580.8905 ppm | 2.4521 ppm |
| ${}^{176}$Ho | 176 | 109 | 174.1289 | 1407.4720 | -876282.5073 ppm | 165136.9691 | +7525.1376 ppm | 3.0519 ppm |
| ${}^{177}$Ho | 177 | 110 | 180.3301 | 1412.4600 | -872329.0842 ppm | 166070.3334 | +7474.9482 ppm | 3.0346 ppm |
| ${}^{178}$Ho | 178 | 111 | 186.5237 | 1416.3460 | -868306.3886 ppm | 167003.7051 | +7419.0526 ppm | 3.0174 ppm |

### Erbium (Z = 68)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{142}$Er | 142 | 74 | -62.7586 | 1120.8060 | -1055994.2054 ppm | 133427.8499 | +8950.2363 ppm | 3.7825 ppm |
| ${}^{143}$Er | 143 | 75 | -56.1885 | 1132.1310 | -1049630.7631 ppm | 134360.8452 | +8923.3797 ppm | 3.0007 ppm |
| ${}^{144}$Er | 144 | 76 | -49.6310 | 1145.6640 | -1043320.7080 ppm | 135293.8531 | +8913.6680 ppm | 1.4587 ppm |
| ${}^{145}$Er | 145 | 77 | -43.0858 | 1156.3750 | -1037259.3612 ppm | 136226.8734 | +8883.1481 ppm | 1.4832 ppm |
| ${}^{146}$Er | 146 | 78 | -36.5528 | 1169.5349 | -1031254.1235 ppm | 137159.9058 | +8871.3114 ppm | 0.0493 ppm |
| ${}^{147}$Er | 147 | 79 | -30.0318 | 1179.8920 | -1025452.9789 ppm | 138092.9502 | +8839.1145 ppm | 0.2790 ppm |
| ${}^{148}$Er | 148 | 80 | -23.5225 | 1192.8345 | -1019719.8735 ppm | 139026.0064 | +8826.3633 ppm | 0.0744 ppm |
| ${}^{149}$Er | 149 | 81 | -17.0249 | 1203.1684 | -1014150.0924 ppm | 139959.0742 | +8794.8985 ppm | 0.2014 ppm |
| ${}^{150}$Er | 150 | 82 | -10.5388 | 1215.3294 | -1008671.5473 ppm | 140892.1535 | +8777.1307 ppm | 0.1231 ppm |
| ${}^{151}$Er | 151 | 83 | -4.0639 | 1223.8357 | -1003320.6245 ppm | 141825.2440 | +8733.4554 ppm | 0.1171 ppm |
| ${}^{152}$Er | 152 | 84 | 2.3999 | 1234.1410 | -998055.4181 ppm | 142758.3456 | +8703.2548 ppm | 0.0624 ppm |
| ${}^{153}$Er | 153 | 85 | 8.8527 | 1242.1788 | -992873.2153 ppm | 143691.4582 | +8657.4701 ppm | 0.0652 ppm |
| ${}^{154}$Er | 154 | 86 | 15.2948 | 1252.3884 | -987787.4781 ppm | 144624.5815 | +8627.6325 ppm | 0.0346 ppm |
| ${}^{155}$Er | 155 | 87 | 21.7263 | 1260.0639 | -982757.7899 ppm | 145557.7155 | +8580.5429 ppm | 0.0421 ppm |
| ${}^{156}$Er | 156 | 88 | 28.1473 | 1270.1377 | -977839.1796 ppm | 146490.8599 | +8550.7821 ppm | 0.1696 ppm |
| ${}^{157}$Er | 157 | 89 | 34.5580 | 1277.4110 | -972946.8468 ppm | 147424.0146 | +8502.1490 ppm | 0.1813 ppm |
| ${}^{158}$Er | 158 | 90 | 40.9585 | 1287.3725 | -968184.3906 ppm | 148357.1795 | +8472.6291 ppm | 0.1714 ppm |
| ${}^{159}$Er | 159 | 91 | 47.3491 | 1294.7011 | -963428.5682 ppm | 149290.3544 | +8425.6130 ppm | 0.0246 ppm |
| ${}^{160}$Er | 160 | 92 | 53.7297 | 1304.2755 | -958804.9155 ppm | 150223.5392 | +8394.4528 ppm | 0.1628 ppm |
| ${}^{161}$Er | 161 | 93 | 60.1007 | 1311.4839 | -954173.5318 ppm | 151156.7337 | +8347.8292 ppm | 0.0585 ppm |
| ${}^{162}$Er | 162 | 94 | 66.4620 | 1320.6881 | -949676.2174 ppm | 152089.9377 | +8315.1870 ppm | 0.0050 ppm |
| ${}^{163}$Er | 163 | 95 | 72.8139 | 1327.5927 | -945153.4230 ppm | 153023.1513 | +8267.7290 ppm | 0.0305 ppm |
| ${}^{164}$Er | 164 | 96 | 79.1565 | 1336.4391 | -940770.6059 ppm | 153956.3741 | +8233.7339 ppm | 0.0046 ppm |
| ${}^{165}$Er | 165 | 97 | 85.4899 | 1343.0892 | -936348.3460 ppm | 154889.6062 | +8185.7970 ppm | 0.0060 ppm |
| ${}^{166}$Er | 166 | 98 | 91.8142 | 1351.5634 | -932068.1823 ppm | 155822.8473 | +8150.3945 ppm | 0.0022 ppm |
| ${}^{167}$Er | 167 | 99 | 98.1295 | 1357.9998 | -927739.6683 ppm | 156756.0973 | +8102.2628 ppm | 0.0018 ppm |
| ${}^{168}$Er | 168 | 100 | 104.4361 | 1365.7711 | -923533.2673 ppm | 157689.3562 | +8063.3638 ppm | 0.0017 ppm |
| ${}^{169}$Er | 169 | 101 | 110.7339 | 1371.7743 | -919276.8927 ppm | 158622.6238 | +8013.6552 ppm | 0.0019 ppm |
| ${}^{170}$Er | 170 | 102 | 117.0231 | 1379.0320 | -915141.1031 ppm | 159555.9000 | +7972.5748 ppm | 0.0088 ppm |
| ${}^{171}$Er | 171 | 103 | 123.3039 | 1384.7136 | -910953.4922 ppm | 160489.1846 | +7922.0522 ppm | 0.0088 ppm |
| ${}^{172}$Er | 172 | 104 | 129.5763 | 1391.5497 | -906883.4330 ppm | 161422.4776 | +7879.4357 ppm | 0.0247 ppm |
| ${}^{173}$Er | 173 | 105 | 135.8405 | 1396.8020 | -902748.9208 ppm | 162355.7789 | +7827.3961 ppm | 1.2143 ppm |
| ${}^{174}$Er | 174 | 106 | 142.0965 | 1403.1360 | -898729.3218 ppm | 163289.0883 | +7782.9972 ppm | 1.8397 ppm |
| ${}^{175}$Er | 175 | 107 | 148.3445 | 1407.8750 | -894632.3118 ppm | 164222.4057 | +7729.3061 ppm | 2.4579 ppm |
| ${}^{176}$Er | 176 | 108 | 154.5846 | 1413.9840 | -890674.4309 ppm | 165155.7311 | +7684.1220 ppm | 2.4439 ppm |
| ${}^{177}$Er | 177 | 109 | 160.8169 | 1418.3010 | -886613.0312 ppm | 166089.0642 | +7628.7917 ppm | 3.0516 ppm |
| ${}^{178}$Er | 178 | 110 | 167.0414 | 1423.8220 | -882681.0009 ppm | 167022.4051 | +7581.2720 ppm | 3.5964 ppm |
| ${}^{179}$Er | 179 | 111 | 173.2583 | 1427.7040 | -878645.5271 ppm | 167955.7537 | +7524.7654 ppm | 3.0006 ppm |
| ${}^{180}$Er | 180 | 112 | 179.4676 | 1432.8000 | -874743.4174 ppm | 168889.1097 | +7476.6320 ppm | 2.9839 ppm |

### Thulium (Z = 69)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{144}$Tm | 144 | 75 | -70.5820 | 1130.4000 | -1062439.8319 ppm | 135314.0218 | +8955.3604 ppm | 2.9797 ppm |
| ${}^{145}$Tm | 145 | 76 | -63.9959 | 1143.9050 | -1055945.0870 ppm | 136247.0011 | +8945.1045 ppm | 1.4486 ppm |
| ${}^{146}$Tm | 146 | 77 | -57.4223 | 1155.4440 | -1049697.1585 ppm | 137179.9929 | +8920.6066 ppm | 1.4729 ppm |
| ${}^{147}$Tm | 147 | 78 | -50.8610 | 1168.4762 | -1043527.6703 ppm | 138112.9971 | +8907.1933 ppm | 0.0500 ppm |
| ${}^{148}$Tm | 148 | 79 | -44.3120 | 1179.3382 | -1037573.5879 ppm | 139046.0135 | +8878.4659 ppm | 0.0743 ppm |
| ${}^{149}$Tm | 149 | 80 | -37.7749 | 1192.5960 | -1031674.4758 ppm | 139979.0418 | +8867.5492 ppm | 1.4434 ppm |
| ${}^{150}$Tm | 150 | 81 | -31.2495 | 1203.1500 | -1025973.0927 ppm | 140912.0819 | +8837.9022 ppm | 1.4005 ppm |
| ${}^{151}$Tm | 151 | 82 | -24.7358 | 1215.5587 | -1020349.3321 ppm | 141845.1336 | +8821.1440 ppm | 0.1378 ppm |
| ${}^{152}$Tm | 152 | 83 | -18.2335 | 1224.5787 | -1014889.6290 ppm | 142778.1967 | +8780.9366 ppm | 0.3817 ppm |
| ${}^{153}$Tm | 153 | 84 | -11.7425 | 1234.9023 | -1009508.8488 ppm | 143711.2711 | +8750.5642 ppm | 0.0841 ppm |
| ${}^{154}$Tm | 154 | 85 | -5.2626 | 1243.4282 | -1004232.3093 ppm | 144644.3566 | +8708.0162 ppm | 0.1005 ppm |
| ${}^{155}$Tm | 155 | 86 | 1.2064 | 1253.6983 | -999037.7093 ppm | 145577.4530 | +8678.2832 ppm | 0.0687 ppm |
| ${}^{156}$Tm | 156 | 87 | 7.6646 | 1261.9781 | -993926.4833 ppm | 146510.5602 | +8635.1844 ppm | 0.0983 ppm |
| ${}^{157}$Tm | 157 | 88 | 14.1123 | 1271.9243 | -988904.8011 ppm | 147443.6780 | +8604.2043 ppm | 0.1912 ppm |
| ${}^{158}$Tm | 158 | 89 | 20.5494 | 1279.9895 | -983945.6504 ppm | 148376.8063 | +8560.7918 ppm | 0.1714 ppm |
| ${}^{159}$Tm | 159 | 90 | 26.9762 | 1289.9280 | -979087.0240 ppm | 149309.9449 | +8530.7564 ppm | 0.1888 ppm |
| ${}^{160}$Tm | 160 | 91 | 33.3929 | 1297.7300 | -974268.2181 ppm | 150243.0937 | +8486.7007 ppm | 0.2194 ppm |
| ${}^{161}$Tm | 161 | 92 | 39.7996 | 1307.3990 | -969558.2168 ppm | 151176.2524 | +8455.8192 ppm | 0.1864 ppm |
| ${}^{162}$Tm | 162 | 93 | 46.1963 | 1315.0491 | -964871.0218 ppm | 152109.4211 | +8411.8867 ppm | 0.1727 ppm |
| ${}^{163}$Tm | 163 | 94 | 52.5834 | 1324.3713 | -960295.6037 ppm | 153042.5995 | +8379.6679 ppm | 0.0363 ppm |
| ${}^{164}$Tm | 164 | 95 | 58.9608 | 1331.6232 | -955722.6132 ppm | 153975.7875 | +8334.2329 ppm | 0.1638 ppm |
| ${}^{165}$Tm | 165 | 96 | 65.3288 | 1340.7156 | -951273.2197 ppm | 154908.9849 | +8301.4905 ppm | 0.0108 ppm |
| ${}^{166}$Tm | 166 | 97 | 71.6874 | 1347.7433 | -946809.3288 ppm | 155842.1917 | +8255.7347 ppm | 0.0747 ppm |
| ${}^{167}$Tm | 167 | 98 | 78.0368 | 1356.4713 | -942470.7479 ppm | 156775.4078 | +8221.6105 ppm | 0.0081 ppm |
| ${}^{168}$Tm | 168 | 99 | 84.3771 | 1363.3119 | -938108.7328 ppm | 157708.6329 | +8175.7865 ppm | 0.0107 ppm |
| ${}^{169}$Tm | 169 | 100 | 90.7085 | 1371.3455 | -933854.4095 ppm | 158641.8669 | +8138.2057 ppm | 0.0047 ppm |
| ${}^{170}$Tm | 170 | 101 | 97.0310 | 1377.9374 | -929582.4576 ppm | 159575.1098 | +8091.9420 ppm | 0.0046 ppm |
| ${}^{171}$Tm | 171 | 102 | 103.3448 | 1385.4237 | -925405.6680 ppm | 160508.3615 | +8051.9371 ppm | 0.0061 ppm |
| ${}^{172}$Tm | 172 | 103 | 109.6499 | 1391.6583 | -921209.1534 ppm | 161441.6217 | +8004.5737 ppm | 0.0342 ppm |
| ${}^{173}$Tm | 173 | 104 | 115.9466 | 1398.6122 | -917098.8031 ppm | 162374.8904 | +7962.3121 ppm | 0.0273 ppm |
| ${}^{174}$Tm | 174 | 105 | 122.2349 | 1404.2919 | -912956.1871 ppm | 163308.1676 | +7912.6632 ppm | 0.2760 ppm |
| ${}^{175}$Tm | 175 | 106 | 128.5150 | 1410.8093 | -908906.9281 ppm | 164241.4530 | +7868.8144 ppm | 0.3068 ppm |
| ${}^{176}$Tm | 176 | 107 | 134.7868 | 1415.9414 | -904807.6310 ppm | 165174.7465 | +7816.9963 ppm | 0.6101 ppm |
| ${}^{177}$Tm | 177 | 108 | 141.0506 | 1422.1950 | -900821.8880 ppm | 166108.0481 | +7772.7690 ppm | 1.2150 ppm |
| ${}^{178}$Tm | 178 | 109 | 147.3065 | 1427.0260 | -896773.8077 ppm | 167041.3577 | +7719.8023 ppm | 1.8095 ppm |
| ${}^{179}$Tm | 179 | 110 | 153.5545 | 1432.7160 | -892822.8270 ppm | 167974.6752 | +7673.4568 ppm | 2.3973 ppm |
| ${}^{180}$Tm | 180 | 111 | 159.7947 | 1436.9400 | -888795.1577 ppm | 168908.0003 | +7619.3142 ppm | 2.3839 ppm |
| ${}^{181}$Tm | 181 | 112 | 166.0273 | 1442.3890 | -884894.2520 ppm | 169841.3332 | +7571.7977 ppm | 2.9675 ppm |
| ${}^{182}$Tm | 182 | 113 | 172.2523 | 1446.5360 | -880920.8461 ppm | 170774.6736 | +7517.6019 ppm | 2.9511 ppm |

### Ytterbium (Z = 70)

_38 of 38 isotopes with a framework prediction; 38 of 38 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{148}$Yb | 148 | 78 | -65.3695 | 1170.0880 | -1055867.1673 ppm | 139066.2887 | +8963.0926 ppm | 2.8993 ppm |
| ${}^{149}$Yb | 149 | 79 | -58.7923 | 1181.1230 | -1049776.6058 ppm | 139999.2769 | +8936.2319 ppm | 2.1616 ppm |
| ${}^{150}$Yb | 150 | 80 | -52.2272 | 1194.7500 | -1043713.9321 ppm | 140932.2772 | +8927.1531 ppm | 2.1473 ppm |
| ${}^{151}$Yb | 151 | 81 | -45.6741 | 1205.5471 | -1037886.6142 ppm | 141865.2895 | +8898.2720 ppm | 2.1370 ppm |
| ${}^{152}$Yb | 152 | 82 | -39.1327 | 1218.3464 | -1032119.5557 ppm | 142798.3136 | +8884.2222 ppm | 1.0577 ppm |
| ${}^{153}$Yb | 153 | 83 | -32.6030 | 1227.3660 | -1026563.3808 ppm | 143731.3493 | +8843.2538 ppm | 1.4057 ppm |
| ${}^{154}$Yb | 154 | 84 | -26.0847 | 1238.1508 | -1021067.4324 ppm | 144664.3964 | +8816.1441 ppm | 0.1205 ppm |
| ${}^{155}$Yb | 155 | 85 | -19.5776 | 1246.7926 | -1015702.3553 ppm | 145597.4547 | +8774.0715 ppm | 0.1150 ppm |
| ${}^{156}$Yb | 156 | 86 | -13.0816 | 1257.6269 | -1010401.8083 ppm | 146530.5241 | +8747.8392 ppm | 0.0641 ppm |
| ${}^{157}$Yb | 157 | 87 | -6.5965 | 1265.8526 | -1005211.1403 ppm | 147463.6045 | +8704.0159 ppm | 0.0746 ppm |
| ${}^{158}$Yb | 158 | 88 | -0.1222 | 1276.5136 | -1000095.7668 ppm | 148396.6956 | +8677.5174 ppm | 0.0542 ppm |
| ${}^{159}$Yb | 159 | 89 | 6.3414 | 1284.4088 | -995062.7680 ppm | 149329.7974 | +8632.5801 ppm | 0.1187 ppm |
| ${}^{160}$Yb | 160 | 90 | 12.7946 | 1294.8098 | -990118.5242 ppm | 150262.9096 | +8605.2393 ppm | 0.0369 ppm |
| ${}^{161}$Yb | 161 | 91 | 19.2375 | 1302.5522 | -985230.8992 ppm | 151196.0321 | +8560.4191 ppm | 0.1007 ppm |
| ${}^{162}$Yb | 162 | 92 | 25.6702 | 1312.6104 | -980443.3620 ppm | 152129.1648 | +8531.7040 ppm | 0.1001 ppm |
| ${}^{163}$Yb | 163 | 93 | 32.0929 | 1320.1544 | -975690.0097 ppm | 153062.3076 | +8486.7003 ppm | 0.0995 ppm |
| ${}^{164}$Yb | 164 | 94 | 38.5057 | 1329.9440 | -971047.0911 ppm | 153995.4602 | +8457.1404 ppm | 0.0989 ppm |
| ${}^{165}$Yb | 165 | 95 | 44.9088 | 1337.2986 | -966418.2656 ppm | 154928.6225 | +8412.0185 ppm | 0.1727 ppm |
| ${}^{166}$Yb | 166 | 96 | 51.3022 | 1346.6682 | -961904.3159 ppm | 155861.7945 | +8380.6492 ppm | 0.0453 ppm |
| ${}^{167}$Yb | 167 | 97 | 57.6862 | 1353.7357 | -957387.3970 ppm | 156794.9760 | +8334.7880 ppm | 0.0255 ppm |
| ${}^{168}$Yb | 168 | 98 | 64.0608 | 1362.7970 | -952993.1427 ppm | 157728.1668 | +8302.3844 ppm | 0.0006 ppm |
| ${}^{169}$Yb | 169 | 99 | 70.4262 | 1369.6640 | -948581.4194 ppm | 158661.3669 | +8256.3631 ppm | 0.0011 ppm |
| ${}^{170}$Yb | 170 | 100 | 76.7824 | 1378.1237 | -944284.7943 ppm | 159594.5760 | +8221.0862 ppm | 0.0001 ppm |
| ${}^{171}$Yb | 171 | 101 | 83.1297 | 1384.7379 | -939967.1729 ppm | 160527.7942 | +8174.5929 ppm | 0.0001 ppm |
| ${}^{172}$Yb | 172 | 102 | 89.4682 | 1392.7579 | -935761.8743 ppm | 161461.0212 | +8137.5452 ppm | 0.0001 ppm |
| ${}^{173}$Yb | 173 | 103 | 95.7978 | 1399.1250 | -931530.1818 ppm | 162394.2569 | +8090.6368 ppm | 0.0001 ppm |
| ${}^{174}$Yb | 174 | 104 | 102.1189 | 1406.5896 | -927399.6613 ppm | 163327.5013 | +8051.1502 ppm | 0.0001 ppm |
| ${}^{175}$Yb | 175 | 105 | 108.4314 | 1412.4119 | -923229.6147 ppm | 164260.7542 | +8002.0091 ppm | 0.0004 ppm |
| ${}^{176}$Yb | 176 | 106 | 114.7355 | 1419.2790 | -919159.2855 ppm | 165194.0155 | +7959.9045 ppm | 0.0001 ppm |
| ${}^{177}$Yb | 177 | 107 | 121.0314 | 1424.8454 | -915056.5027 ppm | 166127.2851 | +7910.3729 ppm | 0.0013 ppm |
| ${}^{178}$Yb | 178 | 108 | 127.3190 | 1431.6075 | -911065.7166 ppm | 167060.5629 | +7868.7190 ppm | 0.0397 ppm |
| ${}^{179}$Yb | 179 | 109 | 133.5985 | 1436.6540 | -907007.1643 ppm | 167993.8487 | +7817.1324 ppm | 1.2015 ppm |
| ${}^{180}$Yb | 180 | 110 | 139.8701 | 1442.8800 | -903061.8691 ppm | 168927.1426 | +7772.8865 ppm | 1.7894 ppm |
| ${}^{181}$Yb | 181 | 111 | 146.1338 | 1447.2760 | -899028.4035 ppm | 169860.4443 | +7718.9418 ppm | 1.7684 ppm |
| ${}^{182}$Yb | 182 | 112 | 152.3897 | 1453.0880 | -895127.0243 ppm | 170793.7539 | +7674.2220 ppm | 2.3577 ppm |
| ${}^{183}$Yb | 183 | 113 | 158.6379 | 1457.2290 | -891137.3089 ppm | 171727.0711 | +7619.9149 ppm | 2.3447 ppm |
| ${}^{184}$Yb | 184 | 114 | 164.8785 | 1462.9840 | -887299.8695 ppm | 172660.3959 | +7575.0683 ppm | 2.9353 ppm |
| ${}^{185}$Yb | 185 | 115 | 171.1116 | 1466.8650 | -883348.7687 ppm | 173593.7282 | +7520.6908 ppm | 2.9032 ppm |

### Lutetium (Z = 71)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{150}$Lu | 150 | 79 | -73.4719 | 1179.9000 | -1062269.5724 ppm | 140952.7395 | +8972.0908 ppm | 2.1470 ppm |
| ${}^{151}$Lu | 151 | 80 | -66.8788 | 1193.5040 | -1056035.6474 ppm | 141885.7119 | +8962.8445 ppm | 2.1329 ppm |
| ${}^{152}$Lu | 152 | 81 | -60.2978 | 1204.7520 | -1050049.9555 ppm | 142818.6963 | +8936.6418 ppm | 1.3819 ppm |
| ${}^{153}$Lu | 153 | 82 | -53.7287 | 1217.7405 | -1044121.6599 ppm | 143751.6927 | +8923.8369 ppm | 1.0529 ppm |
| ${}^{154}$Lu | 154 | 83 | -47.1714 | 1227.0720 | -1038442.2723 ppm | 144684.7008 | +8885.5156 ppm | 1.4030 ppm |
| ${}^{155}$Lu | 155 | 84 | -40.6257 | 1238.0527 | -1032814.2106 ppm | 145617.7205 | +8858.8609 ppm | 0.1333 ppm |
| ${}^{156}$Lu | 156 | 85 | -34.0914 | 1247.2785 | -1027332.6460 ppm | 146550.7516 | +8820.6544 ppm | 0.3726 ppm |
| ${}^{157}$Lu | 157 | 86 | -27.5684 | 1258.0901 | -1021912.8734 ppm | 147483.7940 | +8793.9531 ppm | 0.0826 ppm |
| ${}^{158}$Lu | 158 | 87 | -21.0564 | 1266.9338 | -1016619.9686 ppm | 148416.8475 | +8754.1717 ppm | 0.1028 ppm |
| ${}^{159}$Lu | 159 | 88 | -14.5554 | 1277.5015 | -1011393.6114 ppm | 149349.9118 | +8726.7100 ppm | 0.2544 ppm |
| ${}^{160}$Lu | 160 | 89 | -8.0651 | 1286.1342 | -1006270.7926 ppm | 150282.9870 | +8686.5620 ppm | 0.3814 ppm |
| ${}^{161}$Lu | 161 | 90 | -1.5854 | 1296.4979 | -1001222.8491 ppm | 151216.0727 | +8658.6300 ppm | 0.1864 ppm |
| ${}^{162}$Lu | 162 | 91 | 4.8838 | 1304.8387 | -996257.1831 ppm | 152149.1690 | +8617.5851 ppm | 0.4974 ppm |
| ${}^{163}$Lu | 163 | 92 | 11.3426 | 1314.8696 | -991373.5580 ppm | 153082.2755 | +8588.3436 ppm | 0.1841 ppm |
| ${}^{164}$Lu | 164 | 93 | 17.7913 | 1322.7919 | -986550.1554 ppm | 154015.3922 | +8545.5980 ppm | 0.1830 ppm |
| ${}^{165}$Lu | 165 | 94 | 24.2300 | 1332.6631 | -981818.3526 ppm | 154948.5190 | +8516.2289 ppm | 0.1727 ppm |
| ${}^{166}$Lu | 166 | 95 | 30.6588 | 1340.3131 | -977125.6595 ppm | 155881.6557 | +8472.7857 ppm | 0.1928 ppm |
| ${}^{167}$Lu | 167 | 96 | 37.0778 | 1349.8898 | -972532.7290 ppm | 156814.8021 | +8442.4196 ppm | 0.2396 ppm |
| ${}^{168}$Lu | 168 | 97 | 43.4872 | 1357.5076 | -967965.4335 ppm | 157747.9581 | +8399.8495 ppm | 0.2427 ppm |
| ${}^{169}$Lu | 169 | 98 | 49.8871 | 1366.5886 | -963495.1944 ppm | 158681.1237 | +8367.2195 ppm | 0.0191 ppm |
| ${}^{170}$Lu | 170 | 99 | 56.2776 | 1373.8837 | -959037.6038 ppm | 159614.2986 | +8323.6557 ppm | 0.1064 ppm |
| ${}^{171}$Lu | 171 | 100 | 62.6588 | 1382.4772 | -954676.4051 ppm | 160547.4827 | +8288.8828 ppm | 0.0117 ppm |
| ${}^{172}$Lu | 172 | 101 | 69.0310 | 1389.4561 | -950317.9807 ppm | 161480.6760 | +8244.4066 ppm | 0.0146 ppm |
| ${}^{173}$Lu | 173 | 102 | 75.3941 | 1397.6724 | -946057.3620 ppm | 162413.8783 | +8208.2451 ppm | 0.0097 ppm |
| ${}^{174}$Lu | 174 | 103 | 81.7484 | 1404.4330 | -941792.5927 ppm | 163347.0894 | +8163.4966 ppm | 0.0097 ppm |
| ${}^{175}$Lu | 175 | 104 | 88.0939 | 1412.0997 | -937614.9543 ppm | 164280.3093 | +8124.9197 ppm | 0.0074 ppm |
| ${}^{176}$Lu | 176 | 105 | 94.4308 | 1418.3877 | -933423.8754 ppm | 165213.5379 | +8078.3537 ppm | 0.0074 ppm |
| ${}^{177}$Lu | 177 | 106 | 100.7591 | 1425.4606 | -929314.7300 ppm | 166146.7750 | +8037.1673 ppm | 0.0074 ppm |
| ${}^{178}$Lu | 178 | 107 | 107.0789 | 1431.4859 | -925197.3438 ppm | 167080.0206 | +7990.1245 ppm | 0.0136 ppm |
| ${}^{179}$Lu | 179 | 108 | 113.3905 | 1438.2783 | -921162.3361 ppm | 168013.2744 | +7948.2975 ppm | 0.0309 ppm |
| ${}^{180}$Lu | 180 | 109 | 119.6938 | 1443.9671 | -917107.6372 ppm | 168946.5365 | +7900.3487 ppm | 0.4219 ppm |
| ${}^{181}$Lu | 181 | 110 | 125.9891 | 1450.1593 | -913120.5316 ppm | 169879.8067 | +7855.9898 ppm | 0.7461 ppm |
| ${}^{182}$Lu | 182 | 111 | 132.2763 | 1455.2720 | -909105.4509 ppm | 170813.0849 | +7805.3388 ppm | 1.1816 ppm |
| ${}^{183}$Lu | 183 | 112 | 138.5556 | 1461.2207 | -905178.1826 ppm | 171746.3710 | +7761.0457 ppm | 0.4701 ppm |
| ${}^{184}$Lu | 184 | 113 | 144.8271 | 1465.9280 | -901204.4939 ppm | 172679.6649 | +7709.2721 ppm | 1.1687 ppm |
| ${}^{185}$Lu | 185 | 114 | 151.0909 | 1471.6750 | -897334.0709 ppm | 173612.9666 | +7664.3975 ppm | 1.7409 ppm |
| ${}^{186}$Lu | 186 | 115 | 157.3470 | 1476.0960 | -893403.2448 ppm | 174546.2758 | +7612.4868 ppm | 2.3069 ppm |
| ${}^{187}$Lu | 187 | 116 | 163.5957 | 1481.6010 | -889581.8237 ppm | 175479.5926 | +7567.4818 ppm | 2.2945 ppm |
| ${}^{188}$Lu | 188 | 117 | 169.8369 | 1485.7640 | -885690.5390 ppm | 176412.9169 | +7514.9488 ppm | 2.2822 ppm |

### Hafnium (Z = 72)

_38 of 38 isotopes with a framework prediction; 38 of 38 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{153}$Hf | 153 | 81 | -75.1197 | 1205.9460 | -1062291.1176 ppm | 143772.3013 | +8990.0486 ppm | 2.1050 ppm |
| ${}^{154}$Hf | 154 | 82 | -68.5229 | 1219.3720 | -1056195.2434 ppm | 144705.2699 | +8980.1392 ppm | 2.0914 ppm |
| ${}^{155}$Hf | 155 | 83 | -61.9380 | 1228.9950 | -1050397.2788 ppm | 145638.2505 | +8943.5293 ppm | 2.0779 ppm |
| ${}^{156}$Hf | 156 | 84 | -55.3648 | 1240.6161 | -1044626.8910 ppm | 146571.2427 | +8920.8723 ppm | 1.0307 ppm |
| ${}^{157}$Hf | 157 | 85 | -48.8032 | 1249.7200 | -1039051.3468 ppm | 147504.2465 | +8881.5044 ppm | 1.3698 ppm |
| ${}^{158}$Hf | 158 | 86 | -42.2531 | 1261.0417 | -1033506.4733 ppm | 148437.2618 | +8857.8853 ppm | 0.1189 ppm |
| ${}^{159}$Hf | 159 | 87 | -35.7141 | 1269.8632 | -1028124.3738 ppm | 149370.2883 | +8817.6201 ppm | 0.1135 ppm |
| ${}^{160}$Hf | 160 | 88 | -29.1862 | 1281.0207 | -1022783.5774 ppm | 150303.3258 | +8793.7481 ppm | 0.0640 ppm |
| ${}^{161}$Hf | 161 | 89 | -22.6693 | 1289.4690 | -1017580.3210 ppm | 151236.3743 | +8752.0166 ppm | 0.1564 ppm |
| ${}^{162}$Hf | 162 | 90 | -16.1631 | 1300.3930 | -1012429.3909 ppm | 152169.4335 | +8727.4248 ppm | 0.0593 ppm |
| ${}^{163}$Hf | 163 | 91 | -9.6675 | 1308.5652 | -1007387.8785 ppm | 153102.5034 | +8684.9169 ppm | 0.1693 ppm |
| ${}^{164}$Hf | 164 | 92 | -3.1824 | 1319.1855 | -1002412.4095 ppm | 154035.5837 | +8659.1656 ppm | 0.1035 ppm |
| ${}^{165}$Hf | 165 | 93 | 3.2924 | 1327.0740 | -997519.0782 ppm | 154968.6743 | +8615.8589 ppm | 0.1819 ppm |
| ${}^{166}$Hf | 166 | 94 | 9.7570 | 1337.3688 | -992704.3538 ppm | 155901.7751 | +8588.8410 ppm | 0.1808 ppm |
| ${}^{167}$Hf | 167 | 95 | 16.2115 | 1345.0489 | -987947.2545 ppm | 156834.8860 | +8545.2525 ppm | 0.1797 ppm |
| ${}^{168}$Hf | 168 | 96 | 22.6562 | 1355.0130 | -983279.7246 ppm | 157768.0068 | +8516.9710 ppm | 0.1786 ppm |
| ${}^{169}$Hf | 169 | 97 | 29.0911 | 1362.4407 | -978647.8191 ppm | 158701.1373 | +8472.8310 ppm | 0.1776 ppm |
| ${}^{170}$Hf | 170 | 98 | 35.5163 | 1372.0490 | -974114.3854 ppm | 159634.2775 | +8443.1632 ppm | 0.1765 ppm |
| ${}^{171}$Hf | 171 | 99 | 41.9321 | 1379.2977 | -969598.9701 ppm | 160567.4271 | +8398.9591 ppm | 0.1813 ppm |
| ${}^{172}$Hf | 172 | 100 | 48.3384 | 1388.3400 | -965182.5685 ppm | 161500.5862 | +8366.6191 ppm | 0.1525 ppm |
| ${}^{173}$Hf | 173 | 101 | 54.7355 | 1395.4208 | -960774.8930 ppm | 162433.7545 | +8322.4337 ppm | 0.1735 ppm |
| ${}^{174}$Hf | 174 | 102 | 61.1235 | 1403.9249 | -956462.4190 ppm | 163366.9320 | +8287.6701 ppm | 0.0139 ppm |
| ${}^{175}$Hf | 175 | 103 | 67.5024 | 1410.6334 | -952147.4252 ppm | 164300.1185 | +8242.2491 ppm | 0.0140 ppm |
| ${}^{176}$Hf | 176 | 104 | 73.8725 | 1418.7994 | -947933.0994 ppm | 165233.3138 | +8206.3656 ppm | 0.0090 ppm |
| ${}^{177}$Hf | 177 | 105 | 80.2338 | 1425.1751 | -943702.5296 ppm | 166166.5180 | +8159.9899 ppm | 0.0086 ppm |
| ${}^{178}$Hf | 178 | 106 | 86.5863 | 1432.8010 | -939568.4808 ppm | 167099.7308 | +8121.7930 ppm | 0.0085 ppm |
| ${}^{179}$Hf | 179 | 107 | 92.9304 | 1438.9000 | -935415.6848 ppm | 168032.9522 | +8074.8400 ppm | 0.0085 ppm |
| ${}^{180}$Hf | 180 | 108 | 99.2659 | 1446.2877 | -931365.0081 ppm | 168966.1821 | +8036.2107 ppm | 0.0085 ppm |
| ${}^{181}$Hf | 181 | 109 | 105.5932 | 1451.9825 | -927276.5501 ppm | 169899.4203 | +7987.9338 ppm | 0.0084 ppm |
| ${}^{182}$Hf | 182 | 110 | 111.9122 | 1458.7005 | -923279.5427 ppm | 170832.6667 | +7946.3226 ppm | 0.0364 ppm |
| ${}^{183}$Hf | 183 | 111 | 118.2230 | 1464.0058 | -919246.8839 ppm | 171765.9213 | +7896.8592 ppm | 0.1763 ppm |
| ${}^{184}$Hf | 184 | 112 | 124.5258 | 1470.2930 | -915305.4203 ppm | 172699.1839 | +7853.7579 ppm | 0.2317 ppm |
| ${}^{185}$Hf | 185 | 113 | 130.8207 | 1475.1847 | -911319.0809 ppm | 173632.4544 | +7803.0061 ppm | 0.3731 ppm |
| ${}^{186}$Hf | 186 | 114 | 137.1078 | 1481.3604 | -907444.6862 ppm | 174565.7328 | +7760.3177 ppm | 0.2958 ppm |
| ${}^{187}$Hf | 187 | 115 | 143.3871 | 1486.0890 | -903513.8008 ppm | 175499.0189 | +7709.2864 ppm | 1.1500 ppm |
| ${}^{188}$Hf | 188 | 116 | 149.6587 | 1491.9680 | -899690.3858 ppm | 176432.3127 | +7666.0595 ppm | 1.7131 ppm |
| ${}^{189}$Hf | 189 | 117 | 155.9228 | 1496.3130 | -895795.3087 ppm | 177365.6140 | +7614.6960 ppm | 1.7040 ppm |
| ${}^{190}$Hf | 190 | 118 | 162.1795 | 1501.9500 | -892020.7264 ppm | 178298.9228 | +7571.4859 ppm | 2.2582 ppm |

### Tantalum (Z = 73)

_40 of 40 isotopes with a framework prediction; 40 of 40 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{155}$Ta | 155 | 82 | -83.5144 | 1217.9900 | -1068567.4132 ppm | 145659.0445 | +9015.4333 ppm | 2.0778 ppm |
| ${}^{156}$Ta | 156 | 83 | -76.9019 | 1228.0320 | -1062622.0251 ppm | 146591.9974 | +8981.6521 ppm | 2.0645 ppm |
| ${}^{157}$Ta | 157 | 84 | -70.3012 | 1239.6815 | -1056709.0598 ppm | 147524.9621 | +8959.2996 ppm | 1.0262 ppm |
| ${}^{158}$Ta | 158 | 85 | -63.7122 | 1249.3060 | -1050998.0932 ppm | 148457.9386 | +8923.0969 ppm | 1.3610 ppm |
| ${}^{159}$Ta | 159 | 86 | -57.1348 | 1260.6674 | -1045321.0966 ppm | 149390.9266 | +8899.6793 ppm | 0.1330 ppm |
| ${}^{160}$Ta | 160 | 87 | -50.5688 | 1270.1233 | -1039814.1086 ppm | 150323.9261 | +8863.5202 ppm | 0.3645 ppm |
| ${}^{161}$Ta | 161 | 88 | -44.0141 | 1281.1494 | -1034355.1264 ppm | 151256.9367 | +8838.4507 ppm | 0.1626 ppm |
| ${}^{162}$Ta | 162 | 89 | -37.4703 | 1290.2236 | -1029041.7474 ppm | 152189.9584 | +8800.7100 ppm | 0.4197 ppm |
| ${}^{163}$Ta | 163 | 90 | -30.9376 | 1301.0482 | -1023778.9508 ppm | 153122.9911 | +8775.1365 ppm | 0.2507 ppm |
| ${}^{164}$Ta | 164 | 91 | -24.4155 | 1309.8676 | -1018639.6966 ppm | 154056.0345 | +8736.7009 ppm | 0.1830 ppm |
| ${}^{165}$Ta | 165 | 92 | -17.9041 | 1320.5040 | -1013558.5538 ppm | 154989.0885 | +8710.7277 ppm | 0.0883 ppm |
| ${}^{166}$Ta | 166 | 93 | -11.4032 | 1328.8253 | -1008581.4009 ppm | 155922.1530 | +8670.0274 ppm | 0.1808 ppm |
| ${}^{167}$Ta | 167 | 94 | -4.9126 | 1339.1499 | -1003668.4199 ppm | 156855.2278 | +8642.8746 ppm | 0.1797 ppm |
| ${}^{168}$Ta | 168 | 95 | 1.5679 | 1347.2640 | -998836.2560 ppm | 157788.3127 | +8601.8584 ppm | 0.1786 ppm |
| ${}^{169}$Ta | 169 | 96 | 8.0383 | 1357.2319 | -994077.4608 ppm | 158721.4078 | +8573.2713 ppm | 0.1776 ppm |
| ${}^{170}$Ta | 170 | 97 | 14.4987 | 1365.1504 | -989379.3852 ppm | 159654.5127 | +8532.0267 ppm | 0.1765 ppm |
| ${}^{171}$Ta | 171 | 98 | 20.9494 | 1374.8043 | -984761.8779 ppm | 160587.6274 | +8502.3169 ppm | 0.1755 ppm |
| ${}^{172}$Ta | 172 | 99 | 27.3905 | 1382.4854 | -980187.5024 ppm | 161520.7518 | +8460.5901 ppm | 0.1745 ppm |
| ${}^{173}$Ta | 173 | 100 | 33.8220 | 1391.6232 | -975695.9943 ppm | 162453.8857 | +8428.5246 ppm | 0.1735 ppm |
| ${}^{174}$Ta | 174 | 101 | 40.2442 | 1399.0388 | -971234.4248 ppm | 163387.0290 | +8386.1664 ppm | 0.1725 ppm |
| ${}^{175}$Ta | 175 | 102 | 46.6570 | 1407.7780 | -966857.6863 ppm | 164320.1816 | +8352.5400 ppm | 0.1715 ppm |
| ${}^{176}$Ta | 176 | 103 | 53.0607 | 1414.8060 | -962496.1084 ppm | 165253.3433 | +8308.8237 ppm | 0.1876 ppm |
| ${}^{177}$Ta | 177 | 104 | 59.4554 | 1423.2267 | -958224.9192 ppm | 166186.5140 | +8274.1761 ppm | 0.0201 ppm |
| ${}^{178}$Ta | 178 | 105 | 65.8412 | 1430.2300 | -953964.6259 ppm | 167119.6937 | +8231.0583 ppm | 0.3147 ppm |
| ${}^{179}$Ta | 179 | 106 | 72.2181 | 1438.0121 | -949779.1885 ppm | 168052.8821 | +8193.7662 ppm | 0.0088 ppm |
| ${}^{180}$Ta | 180 | 107 | 78.5864 | 1444.6596 | -945602.1314 ppm | 168986.0793 | +8149.8282 ppm | 0.0123 ppm |
| ${}^{181}$Ta | 181 | 108 | 84.9461 | 1452.2363 | -941506.7042 ppm | 169919.2850 | +8111.9854 ppm | 0.0094 ppm |
| ${}^{182}$Ta | 182 | 109 | 91.2973 | 1458.2992 | -937394.6723 ppm | 170852.4992 | +8065.6048 ppm | 0.0093 ppm |
| ${}^{183}$Ta | 183 | 110 | 97.6401 | 1465.2334 | -933362.0515 ppm | 171785.7218 | +8024.9349 ppm | 0.0093 ppm |
| ${}^{184}$Ta | 184 | 111 | 103.9747 | 1470.8506 | -929309.7950 ppm | 172718.9526 | +7977.0088 ppm | 0.1518 ppm |
| ${}^{185}$Ta | 185 | 112 | 110.3012 | 1477.4769 | -925344.9180 ppm | 173652.1916 | +7935.5528 ppm | 0.0822 ppm |
| ${}^{186}$Ta | 186 | 113 | 116.6195 | 1482.7614 | -921349.7747 ppm | 174585.4387 | +7886.7831 ppm | 0.3464 ppm |
| ${}^{187}$Ta | 187 | 114 | 122.9299 | 1489.1207 | -917447.9785 ppm | 175518.6937 | +7844.8019 ppm | 0.3209 ppm |
| ${}^{188}$Ta | 188 | 115 | 129.2325 | 1494.2240 | -913511.9884 ppm | 176451.9566 | +7795.9835 ppm | 1.1438 ppm |
| ${}^{189}$Ta | 189 | 116 | 135.5272 | 1500.2820 | -909665.4947 ppm | 177385.2273 | +7753.6525 ppm | 1.1378 ppm |
| ${}^{190}$Ta | 190 | 117 | 141.8143 | 1505.1800 | -905782.4800 ppm | 178318.5056 | +7704.4699 ppm | 1.1318 ppm |
| ${}^{191}$Ta | 191 | 118 | 148.0938 | 1511.0010 | -901989.5829 ppm | 179251.7915 | +7661.7354 ppm | 1.6861 ppm |
| ${}^{192}$Ta | 192 | 119 | 154.3659 | 1515.6480 | -898151.9079 ppm | 180185.0849 | +7612.6184 ppm | 2.2347 ppm |
| ${}^{193}$Ta | 193 | 120 | 160.6305 | 1521.4190 | -894420.6215 ppm | 181118.3857 | +7570.3816 ppm | 2.2231 ppm |
| ${}^{194}$Ta | 194 | 121 | 166.8878 | 1525.8100 | -890623.4907 ppm | 182051.6938 | +7520.8777 ppm | 2.7683 ppm |

### Tungsten (Z = 74)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{157}$W | 157 | 83 | -92.0621 | 1228.9960 | -1074908.4183 ppm | 147545.9408 | +9034.4159 ppm | 2.7329 ppm |
| ${}^{158}$W | 158 | 84 | -85.4339 | 1241.0900 | -1068837.7916 ppm | 148478.8779 | +9014.4797 ppm | 2.0383 ppm |
| ${}^{159}$W | 159 | 85 | -78.8175 | 1250.8530 | -1063011.0186 ppm | 149411.8270 | +8979.4631 ppm | 2.0255 ppm |
| ${}^{160}$W | 160 | 86 | -72.2129 | 1262.8463 | -1057182.6185 ppm | 150344.7878 | +8959.5509 ppm | 1.0054 ppm |
| ${}^{161}$W | 161 | 87 | -65.6197 | 1272.0610 | -1051585.3688 ppm | 151277.7601 | +8921.6776 ppm | 1.3357 ppm |
| ${}^{162}$W | 162 | 88 | -59.0380 | 1283.6591 | -1045991.9580 ppm | 152210.7437 | +8899.8180 ppm | 0.1170 ppm |
| ${}^{163}$W | 163 | 89 | -52.4675 | 1292.6396 | -1040589.4047 ppm | 153143.7386 | +8861.1351 ppm | 0.3849 ppm |
| ${}^{164}$W | 164 | 90 | -45.9080 | 1304.0380 | -1035204.5046 ppm | 154076.7446 | +8838.9672 ppm | 0.0633 ppm |
| ${}^{165}$W | 165 | 91 | -39.3595 | 1312.7351 | -1029982.7928 ppm | 155009.7615 | +8799.4027 ppm | 0.1676 ppm |
| ${}^{166}$W | 166 | 92 | -32.8217 | 1323.8326 | -1024792.9207 ppm | 155942.7891 | +8776.0482 ppm | 0.0612 ppm |
| ${}^{167}$W | 167 | 93 | -26.2945 | 1332.1097 | -1019738.9907 ppm | 156875.8274 | +8734.7464 ppm | 0.1203 ppm |
| ${}^{168}$W | 168 | 94 | -19.7778 | 1342.9807 | -1014726.7878 ppm | 157808.8761 | +8710.7281 ppm | 0.0847 ppm |
| ${}^{169}$W | 169 | 95 | -13.2714 | 1351.0769 | -1009822.8376 ppm | 158741.9351 | +8669.2742 ppm | 0.0981 ppm |
| ${}^{170}$W | 170 | 96 | -6.7752 | 1361.5212 | -1004976.2092 ppm | 159675.0043 | +8643.3326 ppm | 0.0833 ppm |
| ${}^{171}$W | 171 | 97 | -0.2891 | 1369.3878 | -1000211.0943 ppm | 160608.0836 | +8601.4299 ppm | 0.1755 ppm |
| ${}^{172}$W | 172 | 98 | 6.1872 | 1379.4702 | -995514.8307 ppm | 161541.1728 | +8574.0293 ppm | 0.1745 ppm |
| ${}^{173}$W | 173 | 99 | 12.6536 | 1387.1717 | -990878.1309 ppm | 162474.2718 | +8532.1003 ppm | 0.1735 ppm |
| ${}^{174}$W | 174 | 100 | 19.1104 | 1396.7428 | -986317.8934 ppm | 163407.3804 | +8502.3491 ppm | 0.1725 ppm |
| ${}^{175}$W | 175 | 101 | 25.5576 | 1404.2198 | -981799.4040 ppm | 164340.4986 | +8460.0376 ppm | 0.1715 ppm |
| ${}^{176}$W | 176 | 102 | 31.9955 | 1413.2999 | -977361.1506 ppm | 165273.6262 | +8428.1285 ppm | 0.1705 ppm |
| ${}^{177}$W | 177 | 103 | 38.4240 | 1420.4314 | -972949.0304 ppm | 166206.7630 | +8384.7139 ppm | 0.1695 ppm |
| ${}^{178}$W | 178 | 104 | 44.8434 | 1429.2080 | -968623.5723 ppm | 167139.9091 | +8351.8514 ppm | 0.0917 ppm |
| ${}^{179}$W | 179 | 105 | 51.2538 | 1436.1675 | -964312.1091 ppm | 168073.0641 | +8308.4180 ppm | 0.0874 ppm |
| ${}^{180}$W | 180 | 106 | 57.6552 | 1444.5798 | -960088.5997 ppm | 169006.2281 | +8274.2602 ppm | 0.0086 ppm |
| ${}^{181}$W | 181 | 107 | 64.0478 | 1451.2488 | -955867.1157 ppm | 169939.4010 | +8230.1041 ppm | 0.0086 ppm |
| ${}^{182}$W | 182 | 108 | 70.4317 | 1459.3323 | -951737.0515 ppm | 170872.5825 | +8194.8998 ppm | 0.0044 ppm |
| ${}^{183}$W | 183 | 109 | 76.8070 | 1465.5232 | -947590.7531 ppm | 171805.7727 | +8148.9340 ppm | 0.0044 ppm |
| ${}^{184}$W | 184 | 110 | 83.1738 | 1472.9343 | -943531.9296 ppm | 172738.9713 | +8110.6978 ppm | 0.0043 ppm |
| ${}^{185}$W | 185 | 111 | 89.5322 | 1478.6880 | -939451.6229 ppm | 173672.1783 | +8063.2263 ppm | 0.0043 ppm |
| ${}^{186}$W | 186 | 112 | 95.8823 | 1485.8801 | -935471.0515 ppm | 174605.3936 | +8024.6847 ppm | 0.0070 ppm |
| ${}^{187}$W | 187 | 113 | 102.2242 | 1491.3468 | -931455.1036 ppm | 175538.6171 | +7976.6166 ppm | 0.0070 ppm |
| ${}^{188}$W | 188 | 114 | 108.5581 | 1498.1820 | -927540.1343 ppm | 176471.8487 | +7936.9854 ppm | 0.0176 ppm |
| ${}^{189}$W | 189 | 115 | 114.8839 | 1503.3060 | -923579.1429 ppm | 177405.0882 | +7888.5300 ppm | 1.1378 ppm |
| ${}^{190}$W | 190 | 116 | 121.2019 | 1510.0256 | -919735.1944 ppm | 178338.3357 | +7848.7066 ppm | 0.2000 ppm |
| ${}^{191}$W | 191 | 117 | 127.5121 | 1514.9043 | -915828.2825 ppm | 179271.5909 | +7799.4184 ppm | 0.2356 ppm |
| ${}^{192}$W | 192 | 118 | 133.8146 | 1521.4080 | -912045.5693 ppm | 180204.8539 | +7759.9091 ppm | 1.1200 ppm |
| ${}^{193}$W | 193 | 119 | 140.1094 | 1526.0510 | -908188.2283 ppm | 181138.1244 | +7710.3506 ppm | 1.1142 ppm |
| ${}^{194}$W | 194 | 120 | 146.3968 | 1532.4060 | -904466.0506 ppm | 182071.4025 | +7670.5467 ppm | 1.6600 ppm |
| ${}^{195}$W | 195 | 121 | 152.6767 | 1536.7950 | -900652.5158 ppm | 183004.6880 | +7620.7071 ppm | 1.6515 ppm |
| ${}^{196}$W | 196 | 122 | 158.9493 | 1542.9120 | -896980.9736 ppm | 183937.9808 | +7580.6364 ppm | 2.1890 ppm |
| ${}^{197}$W | 197 | 123 | 165.2146 | 1547.0410 | -893206.0574 ppm | 184871.2809 | +7530.7476 ppm | 2.1778 ppm |

### Rhenium (Z = 75)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{159}$Re | 159 | 84 | -100.7622 | 1239.4050 | -1081298.8369 ppm | 149432.9893 | +9049.9497 ppm | 2.0568 ppm |
| ${}^{160}$Re | 160 | 85 | -94.1183 | 1249.6000 | -1075318.7653 ppm | 150365.9109 | +9016.9999 ppm | 2.0127 ppm |
| ${}^{161}$Re | 161 | 86 | -87.4863 | 1261.6490 | -1069342.8469 ppm | 151298.8443 | +8997.2595 ppm | 0.9997 ppm |
| ${}^{162}$Re | 162 | 87 | -80.8660 | 1271.3760 | -1063605.1259 ppm | 152231.7894 | +8962.0959 ppm | 1.3274 ppm |
| ${}^{163}$Re | 163 | 88 | -74.2573 | 1282.9511 | -1057880.0373 ppm | 153164.7461 | +8940.3297 ppm | 0.1221 ppm |
| ${}^{164}$Re | 164 | 89 | -67.6598 | 1292.4926 | -1052348.3467 ppm | 154097.7141 | +8905.1673 ppm | 0.3572 ppm |
| ${}^{165}$Re | 165 | 90 | -61.0737 | 1303.7508 | -1046844.5752 ppm | 155030.6933 | +8881.7744 ppm | 0.1535 ppm |
| ${}^{166}$Re | 166 | 91 | -54.4985 | 1313.0001 | -1041506.8608 ppm | 155963.6836 | +8845.6241 ppm | 0.5708 ppm |
| ${}^{167}$Re | 167 | 92 | -47.9343 | 1324.1430 | -1036200.2264 ppm | 156896.6848 | +8821.7743 ppm | 0.2575 ppm |
| ${}^{168}$Re | 168 | 93 | -41.3808 | 1333.1003 | -1031041.0222 ppm | 157829.6967 | +8785.1479 ppm | 0.1970 ppm |
| ${}^{169}$Re | 169 | 94 | -34.8379 | 1343.7860 | -1025925.2039 ppm | 158762.7193 | +8759.6210 ppm | 0.0722 ppm |
| ${}^{170}$Re | 170 | 95 | -28.3055 | 1352.3520 | -1020930.5872 ppm | 159695.7523 | +8720.9542 ppm | 0.0722 ppm |
| ${}^{171}$Re | 171 | 96 | -21.7834 | 1362.7696 | -1015984.6872 ppm | 160628.7957 | +8694.5324 ppm | 0.1755 ppm |
| ${}^{172}$Re | 172 | 97 | -15.2716 | 1371.1575 | -1011137.7142 ppm | 161561.8492 | +8655.6989 ppm | 0.2221 ppm |
| ${}^{173}$Re | 173 | 98 | -8.7697 | 1381.2159 | -1006349.2822 ppm | 162494.9128 | +8627.8350 ppm | 0.1735 ppm |
| ${}^{174}$Re | 174 | 99 | -2.2778 | 1389.4064 | -1001639.4203 ppm | 163427.9863 | +8588.7258 ppm | 0.1725 ppm |
| ${}^{175}$Re | 175 | 100 | 4.2043 | 1399.0929 | -996994.9856 ppm | 164361.0696 | +8559.3819 ppm | 0.1715 ppm |
| ${}^{176}$Re | 176 | 101 | 10.6767 | 1406.9388 | -992411.3657 ppm | 165294.1626 | +8519.1038 ppm | 0.1705 ppm |
| ${}^{177}$Re | 177 | 102 | 17.1397 | 1416.2165 | -987897.5747 ppm | 166227.2651 | +8488.0987 ppm | 0.1695 ppm |
| ${}^{178}$Re | 178 | 103 | 23.5931 | 1423.6721 | -983427.9633 ppm | 167160.3770 | +8446.4136 ppm | 0.1686 ppm |
| ${}^{179}$Re | 179 | 104 | 30.0373 | 1432.6742 | -979034.0752 ppm | 168093.4983 | +8414.6065 ppm | 0.1478 ppm |
| ${}^{180}$Re | 180 | 105 | 36.4724 | 1439.9986 | -974671.9507 ppm | 169026.6287 | +8373.1141 ppm | 0.1276 ppm |
| ${}^{181}$Re | 181 | 106 | 42.8983 | 1448.7500 | -970389.4327 ppm | 169959.7681 | +8340.6711 ppm | 0.0744 ppm |
| ${}^{182}$Re | 182 | 107 | 49.3153 | 1455.7500 | -966123.7769 ppm | 170892.9166 | +8298.2183 ppm | 0.6017 ppm |
| ${}^{183}$Re | 183 | 108 | 55.7235 | 1464.1848 | -961942.3196 ppm | 171826.0738 | +8264.7708 ppm | 0.0471 ppm |
| ${}^{184}$Re | 184 | 109 | 62.1229 | 1470.6663 | -957758.6575 ppm | 172759.2398 | +8220.2440 ppm | 0.0250 ppm |
| ${}^{185}$Re | 185 | 110 | 68.5137 | 1478.3369 | -953654.8519 ppm | 173692.4144 | +8183.2079 ppm | 0.0048 ppm |
| ${}^{186}$Re | 186 | 111 | 74.8961 | 1484.5165 | -949548.5216 ppm | 174625.5975 | +8137.9418 ppm | 0.0047 ppm |
| ${}^{187}$Re | 187 | 112 | 81.2700 | 1491.8770 | -945525.0326 ppm | 175558.7890 | +8100.0455 ppm | 0.0042 ppm |
| ${}^{188}$Re | 188 | 113 | 87.6355 | 1497.7486 | -941488.4822 ppm | 176491.9889 | +8054.0275 ppm | 0.0042 ppm |
| ${}^{189}$Re | 189 | 114 | 93.9929 | 1504.7822 | -937537.1814 ppm | 177425.1969 | +8015.1984 ppm | 0.0465 ppm |
| ${}^{190}$Re | 190 | 115 | 100.3422 | 1510.4574 | -933568.3222 ppm | 178358.4130 | +7969.0868 ppm | 0.0275 ppm |
| ${}^{191}$Re | 191 | 116 | 106.6835 | 1517.2961 | -929688.4149 ppm | 179291.6372 | +7930.0970 ppm | 0.0577 ppm |
| ${}^{192}$Re | 192 | 117 | 113.0169 | 1522.6059 | -925774.0559 ppm | 180224.8692 | +7882.9402 ppm | 0.3959 ppm |
| ${}^{193}$Re | 193 | 118 | 119.3424 | 1529.3200 | -921963.7476 ppm | 181158.1091 | +7844.1914 ppm | 0.2177 ppm |
| ${}^{194}$Re | 194 | 119 | 125.6602 | 1534.3460 | -918101.7729 ppm | 182091.3567 | +7796.8814 ppm | 1.1084 ppm |
| ${}^{195}$Re | 195 | 120 | 131.9704 | 1540.6950 | -914343.5934 ppm | 183024.6120 | +7757.1556 ppm | 1.6515 ppm |
| ${}^{196}$Re | 196 | 121 | 138.2730 | 1545.6560 | -910540.8766 ppm | 183957.8748 | +7709.5934 ppm | 1.6431 ppm |
| ${}^{197}$Re | 197 | 122 | 144.5682 | 1551.7690 | -906836.5166 ppm | 184891.1450 | +7669.0993 ppm | 1.6347 ppm |
| ${}^{198}$Re | 198 | 123 | 150.8560 | 1556.4780 | -903078.6124 ppm | 185824.4226 | +7621.6753 ppm | 2.1669 ppm |
| ${}^{199}$Re | 199 | 124 | 157.1365 | 1562.1500 | -899410.0936 ppm | 186757.7075 | +7580.7441 ppm | 2.1560 ppm |

### Osmium (Z = 76)

_43 of 43 isotopes with a framework prediction; 43 of 43 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{161}$Os | 161 | 85 | -109.6138 | 1250.1650 | -1087679.5017 ppm | 151320.1895 | +9067.9629 ppm | 2.6648 ppm |
| ${}^{162}$Os | 162 | 86 | -102.9545 | 1262.6280 | -1081539.8183 ppm | 152253.0955 | +9050.1198 ppm | 1.9878 ppm |
| ${}^{163}$Os | 163 | 87 | -96.3069 | 1272.5410 | -1075680.7936 ppm | 153186.0134 | +9016.1788 ppm | 1.9757 ppm |
| ${}^{164}$Os | 164 | 88 | -89.6710 | 1284.6625 | -1069801.2460 ppm | 154118.9430 | +8997.5986 ppm | 0.9814 ppm |
| ${}^{165}$Os | 165 | 89 | -83.0467 | 1294.0950 | -1064173.5651 ppm | 155051.8840 | +8961.1553 ppm | 1.3032 ppm |
| ${}^{166}$Os | 166 | 90 | -76.4337 | 1305.8120 | -1058533.4593 ppm | 155984.8365 | +8940.6443 ppm | 0.1162 ppm |
| ${}^{167}$Os | 167 | 91 | -69.8319 | 1314.9506 | -1053106.0958 ppm | 156917.8001 | +8903.4705 ppm | 0.5201 ppm |
| ${}^{168}$Os | 168 | 92 | -63.2411 | 1326.5181 | -1047674.5429 ppm | 157850.7748 | +8882.4704 ppm | 0.0633 ppm |
| ${}^{169}$Os | 169 | 93 | -56.6613 | 1335.3174 | -1042432.8257 ppm | 158783.7603 | +8844.0437 ppm | 0.1648 ppm |
| ${}^{170}$Os | 170 | 94 | -50.0922 | 1346.5914 | -1037199.2485 ppm | 159716.7566 | +8821.9054 ppm | 0.0616 ppm |
| ${}^{171}$Os | 171 | 95 | -43.5337 | 1355.0342 | -1032127.3750 ppm | 160649.7636 | +8782.1575 ppm | 0.1146 ppm |
| ${}^{172}$Os | 172 | 96 | -36.9857 | 1366.0520 | -1027074.8599 ppm | 161582.7810 | +8759.1524 ppm | 0.0797 ppm |
| ${}^{173}$Os | 173 | 97 | -30.4480 | 1374.3179 | -1022154.9655 ppm | 162515.8087 | +8719.2472 ppm | 0.0928 ppm |
| ${}^{174}$Os | 174 | 98 | -23.9205 | 1384.9464 | -1017271.7575 ppm | 163448.8466 | +8694.5700 ppm | 0.0633 ppm |
| ${}^{175}$Os | 175 | 99 | -17.4030 | 1393.1276 | -1012492.0412 ppm | 164381.8946 | +8655.0899 ppm | 0.0722 ppm |
| ${}^{176}$Os | 176 | 100 | -10.8955 | 1403.2248 | -1007764.6050 ppm | 165314.9525 | +8627.9087 ppm | 0.0668 ppm |
| ${}^{177}$Os | 177 | 101 | -4.3978 | 1411.1214 | -1003116.5027 ppm | 166248.0202 | +8587.6285 ppm | 0.0886 ppm |
| ${}^{178}$Os | 178 | 102 | 2.0903 | 1420.7805 | -998528.7765 ppm | 167181.0976 | +8558.5831 ppm | 0.0822 ppm |
| ${}^{179}$Os | 179 | 103 | 8.5688 | 1428.3277 | -994000.8267 ppm | 168114.1845 | +8517.1418 ppm | 0.0930 ppm |
| ${}^{180}$Os | 180 | 104 | 15.0379 | 1437.7351 | -989540.5923 ppm | 169047.2808 | +8487.4088 ppm | 0.0938 ppm |
| ${}^{181}$Os | 181 | 105 | 21.4976 | 1445.0002 | -985122.7557 ppm | 169980.3865 | +8445.2421 ppm | 0.1503 ppm |
| ${}^{182}$Os | 182 | 106 | 27.9482 | 1454.1306 | -980780.1365 ppm | 170913.5013 | +8414.6920 ppm | 0.1283 ppm |
| ${}^{183}$Os | 183 | 107 | 34.3897 | 1461.2566 | -976465.6752 ppm | 171846.6253 | +8372.6680 ppm | 0.2920 ppm |
| ${}^{184}$Os | 184 | 108 | 40.8222 | 1469.9167 | -972228.2096 ppm | 172779.7582 | +8340.1816 ppm | 0.0048 ppm |
| ${}^{185}$Os | 185 | 109 | 47.2459 | 1476.5414 | -968002.3201 ppm | 173712.8999 | +8296.1849 ppm | 0.0048 ppm |
| ${}^{186}$Os | 186 | 110 | 53.6608 | 1484.8068 | -963860.0571 ppm | 174646.0504 | +8262.2632 ppm | 0.0044 ppm |
| ${}^{187}$Os | 187 | 111 | 60.0671 | 1491.0971 | -959716.1496 ppm | 175579.2095 | +8217.3190 ppm | 0.0042 ppm |
| ${}^{188}$Os | 188 | 112 | 66.4649 | 1499.0867 | -955663.0711 ppm | 176512.3772 | +8182.6878 ppm | 0.0042 ppm |
| ${}^{189}$Os | 189 | 113 | 72.8542 | 1505.0075 | -951592.1080 ppm | 177445.5532 | +8136.6217 ppm | 0.0038 ppm |
| ${}^{190}$Os | 190 | 114 | 79.2353 | 1512.7999 | -947623.4377 ppm | 178378.7377 | +8101.7513 ppm | 0.0037 ppm |
| ${}^{191}$Os | 191 | 115 | 85.6080 | 1518.5586 | -943625.4580 ppm | 179311.9303 | +8055.7676 ppm | 0.0037 ppm |
| ${}^{192}$Os | 192 | 116 | 91.9727 | 1526.1170 | -939734.1695 ppm | 180245.1310 | +8020.4549 ppm | 0.0129 ppm |
| ${}^{193}$Os | 193 | 117 | 98.3293 | 1531.7004 | -935803.8056 ppm | 181178.3398 | +7974.4776 ppm | 0.0129 ppm |
| ${}^{194}$Os | 194 | 118 | 104.6780 | 1538.8125 | -931974.7980 ppm | 182111.5566 | +7937.5476 ppm | 0.0133 ppm |
| ${}^{195}$Os | 195 | 119 | 111.0189 | 1543.9603 | -928094.7283 ppm | 183044.7811 | +7890.1383 ppm | 0.3077 ppm |
| ${}^{196}$Os | 196 | 120 | 117.3520 | 1550.7971 | -924327.9597 ppm | 183978.0135 | +7852.5824 ppm | 0.2194 ppm |
| ${}^{197}$Os | 197 | 121 | 123.6774 | 1555.7090 | -920500.9301 ppm | 184911.2535 | +7804.6673 ppm | 1.0915 ppm |
| ${}^{198}$Os | 198 | 122 | 129.9953 | 1562.2200 | -916788.1066 ppm | 185844.5010 | +7766.6692 ppm | 1.0860 ppm |
| ${}^{199}$Os | 199 | 123 | 136.3057 | 1566.9260 | -913010.7839 ppm | 186777.7561 | +7719.0309 ppm | 1.0805 ppm |
| ${}^{200}$Os | 200 | 124 | 142.6086 | 1573.4000 | -909362.7523 ppm | 187711.0185 | +7680.6176 ppm | 1.6102 ppm |
| ${}^{201}$Os | 201 | 125 | 148.9043 | 1577.6490 | -905616.3243 ppm | 188644.2883 | +7631.9174 ppm | 1.6021 ppm |
| ${}^{202}$Os | 202 | 126 | 155.1927 | 1583.4780 | -901992.4837 ppm | 189577.5652 | +7591.2422 ppm | 2.1239 ppm |
| ${}^{203}$Os | 203 | 127 | 161.4740 | 1586.2420 | -898203.4078 ppm | 190510.8494 | +7535.2823 ppm | 2.1134 ppm |

### Iridium (Z = 77)

_43 of 43 isotopes with a framework prediction; 43 of 43 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{163}$Ir | 163 | 86 | -118.6164 | 1260.6420 | -1094092.0910 ppm | 153207.5406 | +9084.6884 ppm | 2.6320 ppm |
| ${}^{164}$Ir | 164 | 87 | -111.9416 | 1271.0000 | -1088073.6403 ppm | 154140.4312 | +9052.7886 ppm | 2.0672 ppm |
| ${}^{165}$Ir | 165 | 88 | -105.2786 | 1283.0400 | -1082054.0080 ppm | 155073.3336 | +9034.0783 ppm | 1.0304 ppm |
| ${}^{166}$Ir | 166 | 89 | -98.6272 | 1292.9740 | -1076279.3466 ppm | 156006.2476 | +8999.9964 ppm | 1.2953 ppm |
| ${}^{167}$Ir | 167 | 90 | -91.9873 | 1304.7418 | -1070502.3371 ppm | 156939.1732 | +8979.7377 ppm | 0.1179 ppm |
| ${}^{168}$Ir | 168 | 91 | -85.3588 | 1314.4070 | -1064940.9453 ppm | 157872.1101 | +8945.7784 ppm | 0.3529 ppm |
| ${}^{169}$Ir | 169 | 92 | -78.7415 | 1325.9055 | -1059386.9647 ppm | 158805.0582 | +8924.0434 ppm | 0.1481 ppm |
| ${}^{170}$Ir | 170 | 93 | -72.1352 | 1335.0100 | -1054033.4604 ppm | 159738.0173 | +8887.7316 ppm | 0.6413 ppm |
| ${}^{171}$Ir | 171 | 94 | -65.5398 | 1346.3667 | -1048679.0194 ppm | 160670.9874 | +8865.4766 ppm | 0.2415 ppm |
| ${}^{172}$Ir | 172 | 95 | -58.9552 | 1355.4054 | -1043496.3297 ppm | 161603.9681 | +8829.2973 ppm | 0.2023 ppm |
| ${}^{173}$Ir | 173 | 96 | -52.3811 | 1366.3658 | -1038336.0819 ppm | 162536.9595 | +8805.6341 ppm | 0.0654 ppm |
| ${}^{174}$Ir | 174 | 97 | -45.8175 | 1374.9546 | -1033322.9384 ppm | 163469.9613 | +8767.5430 ppm | 0.0692 ppm |
| ${}^{175}$Ir | 175 | 98 | -39.2643 | 1385.6345 | -1028336.6727 ppm | 164402.9735 | +8742.8930 ppm | 0.0760 ppm |
| ${}^{176}$Ir | 176 | 99 | -32.7212 | 1394.1932 | -1023469.6368 ppm | 165335.9959 | +8705.5307 ppm | 0.0493 ppm |
| ${}^{177}$Ir | 177 | 100 | -26.1882 | 1404.4300 | -1018646.8580 ppm | 166269.0283 | +8678.9199 ppm | 0.1199 ppm |
| ${}^{178}$Ir | 178 | 101 | -19.6651 | 1412.7082 | -1013920.1698 ppm | 167202.0706 | +8640.7500 ppm | 0.1135 ppm |
| ${}^{179}$Ir | 179 | 102 | -13.1519 | 1422.6069 | -1009244.9110 ppm | 168135.1228 | +8612.8701 ppm | 0.0586 ppm |
| ${}^{180}$Ir | 180 | 103 | -6.6483 | 1430.5741 | -1004647.2890 ppm | 169068.1846 | +8573.7354 ppm | 0.1295 ppm |
| ${}^{181}$Ir | 181 | 104 | -0.1543 | 1440.1309 | -1000107.1192 ppm | 170001.2560 | +8544.6014 ppm | 0.0311 ppm |
| ${}^{182}$Ir | 182 | 105 | 6.3303 | 1447.7909 | -995627.5989 ppm | 170934.3369 | +8504.5562 ppm | 0.1237 ppm |
| ${}^{183}$Ir | 183 | 106 | 12.8056 | 1457.0126 | -991211.0638 ppm | 171867.4270 | +8474.2454 ppm | 0.1448 ppm |
| ${}^{184}$Ir | 184 | 107 | 19.2717 | 1464.4927 | -986840.7287 ppm | 172800.5264 | +8434.0672 ppm | 0.1631 ppm |
| ${}^{185}$Ir | 185 | 108 | 25.7286 | 1473.2887 | -982536.5983 ppm | 173733.6348 | +8402.0790 ppm | 0.1622 ppm |
| ${}^{186}$Ir | 186 | 109 | 32.1766 | 1480.1968 | -978261.9240 ppm | 174666.7523 | +8359.4962 ppm | 0.0954 ppm |
| ${}^{187}$Ir | 187 | 110 | 38.6158 | 1488.6451 | -974059.7940 ppm | 175599.8785 | +8326.3382 ppm | 0.1605 ppm |
| ${}^{188}$Ir | 188 | 111 | 45.0461 | 1495.5120 | -969879.1233 ppm | 176533.0136 | +8284.4754 ppm | 0.0538 ppm |
| ${}^{189}$Ir | 189 | 112 | 51.4679 | 1503.6880 | -965772.2544 ppm | 177466.1573 | +8250.6044 ppm | 0.0714 ppm |
| ${}^{190}$Ir | 190 | 113 | 57.8810 | 1510.0633 | -961669.8049 ppm | 178399.3096 | +8206.8779 ppm | 0.0077 ppm |
| ${}^{191}$Ir | 191 | 114 | 64.2857 | 1518.0899 | -957653.5305 ppm | 179332.4703 | +8173.0165 ppm | 0.0074 ppm |
| ${}^{192}$Ir | 192 | 115 | 70.6821 | 1524.2880 | -953629.4160 ppm | 180265.6393 | +8129.2461 ppm | 0.0073 ppm |
| ${}^{193}$Ir | 193 | 116 | 77.0703 | 1532.0600 | -949695.0138 ppm | 181198.8166 | +8094.8031 ppm | 0.0074 ppm |
| ${}^{194}$Ir | 194 | 117 | 83.4502 | 1538.1268 | -945745.5385 ppm | 182132.0020 | +8051.2465 ppm | 0.0074 ppm |
| ${}^{195}$Ir | 195 | 118 | 89.8222 | 1545.3586 | -941876.1646 ppm | 183065.1955 | +8014.6487 ppm | 0.0073 ppm |
| ${}^{196}$Ir | 196 | 119 | 96.1861 | 1551.1731 | -937991.3570 ppm | 183998.3970 | +7970.6420 ppm | 0.2104 ppm |
| ${}^{197}$Ir | 197 | 120 | 102.5422 | 1558.0731 | -934186.4961 ppm | 184931.6063 | +7933.0887 ppm | 0.1096 ppm |
| ${}^{198}$Ir | 198 | 121 | 108.8906 | 1563.6060 | -930359.3246 ppm | 185864.8234 | +7888.4011 ppm | 1.0860 ppm |
| ${}^{199}$Ir | 199 | 122 | 115.2312 | 1570.3501 | -926620.6803 ppm | 186798.0482 | +7850.9607 ppm | 0.2215 ppm |
| ${}^{200}$Ir | 200 | 123 | 121.5643 | 1575.6000 | -922845.7280 ppm | 187731.2805 | +7805.7275 ppm | 1.0501 ppm |
| ${}^{201}$Ir | 201 | 124 | 127.8898 | 1581.8700 | -919152.7698 ppm | 188664.5204 | +7766.9023 ppm | 1.0698 ppm |
| ${}^{202}$Ir | 202 | 125 | 134.2079 | 1586.7100 | -915417.4865 ppm | 189597.7677 | +7720.6287 ppm | 1.5942 ppm |
| ${}^{203}$Ir | 203 | 126 | 140.5187 | 1592.5350 | -911764.1431 ppm | 190531.0224 | +7679.8058 ppm | 2.1135 ppm |
| ${}^{204}$Ir | 204 | 127 | 146.8222 | 1595.8920 | -907999.9136 ppm | 191464.2843 | +7626.0062 ppm | 2.1030 ppm |
| ${}^{205}$Ir | 205 | 128 | 153.1185 | 1600.0250 | -904302.4105 ppm | 192397.5534 | +7577.1512 ppm | 2.6196 ppm |

### Platinum (Z = 78)

_44 of 44 isotopes with a framework prediction; 44 of 44 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{165}$Pt | 165 | 87 | -127.7693 | 1270.9950 | -1100526.9945 ppm | 155095.0420 | +9101.2879 ppm | 2.6000 ppm |
| ${}^{166}$Pt | 166 | 88 | -121.0791 | 1283.6780 | -1094321.9988 ppm | 156027.9172 | +9084.5222 ppm | 1.9398 ppm |
| ${}^{167}$Pt | 167 | 89 | -114.4006 | 1293.5820 | -1088437.1040 ppm | 156960.8042 | +9051.8623 ppm | 1.9701 ppm |
| ${}^{168}$Pt | 168 | 90 | -107.7339 | 1305.9684 | -1082493.4632 ppm | 157893.7028 | +9034.4035 ppm | 0.9582 ppm |
| ${}^{169}$Pt | 169 | 91 | -101.0786 | 1315.4960 | -1076836.8428 ppm | 158826.6129 | +8999.2590 ppm | 1.2723 ppm |
| ${}^{170}$Pt | 170 | 92 | -94.4346 | 1327.4002 | -1071142.5154 ppm | 159759.5344 | +8979.7689 ppm | 0.1152 ppm |
| ${}^{171}$Pt | 171 | 93 | -87.8018 | 1336.6389 | -1065688.4962 ppm | 160692.4670 | +8943.6774 ppm | 0.5083 ppm |
| ${}^{172}$Pt | 172 | 94 | -81.1800 | 1348.3503 | -1060206.9339 ppm | 161625.4107 | +8923.6472 ppm | 0.0648 ppm |
| ${}^{173}$Pt | 173 | 95 | -74.5692 | 1357.2517 | -1054941.2916 ppm | 162558.3652 | +8886.3201 ppm | 0.3937 ppm |
| ${}^{174}$Pt | 174 | 96 | -67.9690 | 1368.7039 | -1049659.4095 ppm | 163491.3305 | +8865.3674 ppm | 0.0638 ppm |
| ${}^{175}$Pt | 175 | 97 | -61.3795 | 1377.1663 | -1044569.4127 ppm | 164424.3064 | +8826.2124 ppm | 0.1142 ppm |
| ${}^{176}$Pt | 176 | 98 | -54.8004 | 1388.4628 | -1039468.4100 ppm | 165357.2927 | +8805.0085 ppm | 0.0776 ppm |
| ${}^{177}$Pt | 177 | 99 | -48.2317 | 1396.9707 | -1034525.9048 ppm | 166290.2894 | +8767.0402 ppm | 0.0909 ppm |
| ${}^{178}$Pt | 178 | 100 | -41.6731 | 1407.6690 | -1029604.3495 ppm | 167223.2963 | +8742.8893 ppm | 0.0611 ppm |
| ${}^{179}$Pt | 179 | 101 | -35.1246 | 1416.0110 | -1024805.3443 ppm | 168156.3132 | +8704.8094 ppm | 0.0478 ppm |
| ${}^{180}$Pt | 180 | 102 | -28.5861 | 1426.2441 | -1020042.9161 ppm | 169089.3401 | +8678.5908 ppm | 0.0600 ppm |
| ${}^{181}$Pt | 181 | 103 | -22.0574 | 1434.2670 | -1015378.8313 ppm | 170022.3768 | +8639.4947 ppm | 0.0812 ppm |
| ${}^{182}$Pt | 182 | 104 | -15.5383 | 1444.1252 | -1010759.6605 ppm | 170955.4232 | +8611.8067 ppm | 0.0773 ppm |
| ${}^{183}$Pt | 183 | 105 | -9.0288 | 1451.8013 | -1006219.0395 ppm | 171888.4791 | +8571.5629 ppm | 0.0834 ppm |
| ${}^{184}$Pt | 184 | 106 | -2.5288 | 1461.4319 | -1001730.3364 ppm | 172821.5445 | +8543.3154 ppm | 0.0860 ppm |
| ${}^{185}$Pt | 185 | 107 | 3.9619 | 1468.8589 | -997302.7070 ppm | 173754.6192 | +8502.5278 ppm | 0.1499 ppm |
| ${}^{186}$Pt | 186 | 108 | 10.4434 | 1478.1065 | -992934.5824 ppm | 174687.7031 | +8472.8319 ppm | 0.1255 ppm |
| ${}^{187}$Pt | 187 | 109 | 16.9158 | 1484.9988 | -988608.8556 ppm | 175620.7961 | +8429.8665 ppm | 0.1382 ppm |
| ${}^{188}$Pt | 188 | 110 | 23.3792 | 1494.2057 | -984353.3991 ppm | 176553.8982 | +8400.7416 ppm | 0.0303 ppm |
| ${}^{189}$Pt | 189 | 111 | 29.8338 | 1500.9255 | -980123.0876 ppm | 177487.0091 | +8357.7263 ppm | 0.0573 ppm |
| ${}^{190}$Pt | 190 | 112 | 36.2795 | 1509.8339 | -975971.1893 ppm | 178420.1287 | +8327.6862 ppm | 0.0037 ppm |
| ${}^{191}$Pt | 191 | 113 | 42.7166 | 1516.2970 | -971828.3481 ppm | 179353.2571 | +8284.1482 ppm | 0.0232 ppm |
| ${}^{192}$Pt | 192 | 114 | 49.1451 | 1524.9585 | -967772.8244 ppm | 180286.3940 | +8253.5083 ppm | 0.0144 ppm |
| ${}^{193}$Pt | 193 | 115 | 55.5652 | 1531.2210 | -963711.8636 ppm | 181219.5394 | +8209.7760 ppm | 0.0076 ppm |
| ${}^{194}$Pt | 194 | 116 | 61.9768 | 1539.5727 | -959744.1289 ppm | 182152.6931 | +8178.2000 ppm | 0.0027 ppm |
| ${}^{195}$Pt | 195 | 117 | 68.3803 | 1545.6778 | -955760.3396 ppm | 183085.8551 | +8134.5217 ppm | 0.0028 ppm |
| ${}^{196}$Pt | 196 | 118 | 74.7755 | 1553.5998 | -951869.5143 ppm | 184019.0253 | +8101.3688 ppm | 0.0028 ppm |
| ${}^{197}$Pt | 197 | 119 | 81.1627 | 1559.4464 | -947954.1628 ppm | 184952.2035 | +8057.1934 ppm | 0.0029 ppm |
| ${}^{198}$Pt | 198 | 120 | 87.5419 | 1567.0019 | -944134.1539 ppm | 185885.3897 | +8022.8506 ppm | 0.0114 ppm |
| ${}^{199}$Pt | 199 | 121 | 93.9132 | 1572.5579 | -940279.9751 ppm | 186818.5838 | +7978.0210 ppm | 0.0116 ppm |
| ${}^{200}$Pt | 200 | 122 | 100.2767 | 1579.8397 | -936527.2895 ppm | 187751.7858 | +7943.0212 ppm | 0.1080 ppm |
| ${}^{201}$Pt | 201 | 123 | 106.6325 | 1585.0526 | -932726.1991 ppm | 188684.9954 | +7897.2720 ppm | 0.2676 ppm |
| ${}^{202}$Pt | 202 | 124 | 112.9807 | 1592.0753 | -929035.5852 ppm | 189618.2126 | +7861.7133 ppm | 0.1337 ppm |
| ${}^{203}$Pt | 203 | 125 | 119.3213 | 1597.0010 | -925284.1185 ppm | 190551.4374 | +7815.1735 ppm | 1.0592 ppm |
| ${}^{204}$Pt | 204 | 126 | 125.6545 | 1603.2360 | -921624.4318 ppm | 191484.6696 | +7775.9832 ppm | 1.0540 ppm |
| ${}^{205}$Pt | 205 | 127 | 131.9804 | 1606.3800 | -917839.8884 ppm | 192417.9092 | +7721.8567 ppm | 1.5708 ppm |
| ${}^{206}$Pt | 206 | 128 | 138.2989 | 1610.9200 | -914149.1181 ppm | 193351.1561 | +7674.7046 ppm | 1.5632 ppm |
| ${}^{207}$Pt | 207 | 129 | 144.6102 | 1613.9790 | -910401.4111 ppm | 194284.4102 | +7620.0981 ppm | 2.0725 ppm |
| ${}^{208}$Pt | 208 | 130 | 150.9145 | 1618.2400 | -906741.6118 ppm | 195217.6714 | +7573.6566 ppm | 2.0625 ppm |

### Gold (Z = 79)

_43 of 43 isotopes with a framework prediction; 43 of 43 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{168}$Au | 168 | 89 | -130.3662 | 1291.5840 | -1100935.1556 ppm | 157915.5528 | +9086.7232 ppm | 2.5535 ppm |
| ${}^{169}$Au | 169 | 90 | -123.6725 | 1304.0040 | -1094840.5573 ppm | 158848.4245 | +9069.3873 ppm | 1.8935 ppm |
| ${}^{170}$Au | 170 | 91 | -116.9903 | 1314.1000 | -1089026.9585 ppm | 159781.3078 | +9037.0136 ppm | 1.2706 ppm |
| ${}^{171}$Au | 171 | 92 | -110.3197 | 1325.9523 | -1083200.3222 ppm | 160714.2025 | +9017.4019 ppm | 0.1300 ppm |
| ${}^{172}$Au | 172 | 93 | -103.6603 | 1335.7793 | -1077602.8687 ppm | 161647.1086 | +8984.8432 ppm | 0.3505 ppm |
| ${}^{173}$Au | 173 | 94 | -97.0121 | 1347.3646 | -1072001.3874 ppm | 162580.0258 | +8963.7392 ppm | 0.1414 ppm |
| ${}^{174}$Au | 174 | 95 | -90.3750 | 1356.6780 | -1066614.8929 ppm | 163512.9541 | +8928.7014 ppm | 0.6265 ppm |
| ${}^{175}$Au | 175 | 96 | -83.7487 | 1368.0789 | -1061216.2591 ppm | 164445.8932 | +8907.2494 ppm | 0.2366 ppm |
| ${}^{176}$Au | 176 | 97 | -77.1331 | 1377.2675 | -1056004.4601 ppm | 165378.8431 | +8872.3915 ppm | 0.2024 ppm |
| ${}^{177}$Au | 177 | 98 | -70.5282 | 1388.3636 | -1050799.4949 ppm | 166311.8036 | +8849.6646 ppm | 0.0605 ppm |
| ${}^{178}$Au | 178 | 99 | -63.9337 | 1397.1922 | -1045758.6838 ppm | 167244.7745 | +8813.4572 ppm | 0.0618 ppm |
| ${}^{179}$Au | 179 | 100 | -57.3495 | 1407.9491 | -1040732.6595 ppm | 168177.7558 | +8789.3839 ppm | 0.0702 ppm |
| ${}^{180}$Au | 180 | 101 | -50.7755 | 1416.6575 | -1035841.7893 ppm | 169110.7472 | +8753.3118 ppm | 0.0284 ppm |
| ${}^{181}$Au | 181 | 102 | -44.2116 | 1426.9743 | -1030982.7819 ppm | 170043.7487 | +8727.3225 ppm | 0.1185 ppm |
| ${}^{182}$Au | 182 | 103 | -37.6577 | 1435.4784 | -1026233.5300 ppm | 170976.7602 | +8690.8897 ppm | 0.1107 ppm |
| ${}^{183}$Au | 183 | 104 | -31.1135 | 1445.4373 | -1021525.3304 ppm | 171909.7815 | +8663.5216 ppm | 0.0553 ppm |
| ${}^{184}$Au | 184 | 105 | -24.5791 | 1453.6358 | -1016908.6752 ppm | 172842.8124 | +8626.1462 ppm | 0.1300 ppm |
| ${}^{185}$Au | 185 | 106 | -18.0542 | 1463.2466 | -1012338.4327 ppm | 173775.8530 | +8597.4972 ppm | 0.0151 ppm |
| ${}^{186}$Au | 186 | 107 | -11.5387 | 1471.1746 | -1007843.2143 ppm | 174708.9030 | +8559.4132 ppm | 0.1210 ppm |
| ${}^{187}$Au | 187 | 108 | -5.0326 | 1480.5598 | -1003399.1498 ppm | 175641.9623 | +8530.2288 ppm | 0.1292 ppm |
| ${}^{188}$Au | 188 | 109 | 1.4642 | 1487.9737 | -999015.9615 ppm | 176575.0308 | +8490.0521 ppm | 0.0154 ppm |
| ${}^{189}$Au | 189 | 110 | 7.9520 | 1497.2557 | -994688.9643 ppm | 177508.1085 | +8461.0555 ppm | 0.1141 ppm |
| ${}^{190}$Au | 190 | 111 | 14.4307 | 1504.5786 | -990408.7892 ppm | 178441.1952 | +8421.2501 ppm | 0.0195 ppm |
| ${}^{191}$Au | 191 | 112 | 20.9006 | 1513.6142 | -986191.6028 ppm | 179374.2907 | +8391.6214 ppm | 0.0277 ppm |
| ${}^{192}$Au | 192 | 113 | 27.3617 | 1520.6598 | -982006.7225 ppm | 180307.3951 | +8351.1278 ppm | 0.0885 ppm |
| ${}^{193}$Au | 193 | 114 | 33.8140 | 1529.3638 | -977890.1283 ppm | 181240.5081 | +8320.4056 ppm | 0.0483 ppm |
| ${}^{194}$Au | 194 | 115 | 40.2578 | 1536.2422 | -973794.6023 ppm | 182173.6298 | +8279.8599 ppm | 0.0117 ppm |
| ${}^{195}$Au | 195 | 116 | 46.6932 | 1544.6687 | -969771.4080 ppm | 183106.7599 | +8248.3714 ppm | 0.0062 ppm |
| ${}^{196}$Au | 196 | 117 | 53.1201 | 1551.3116 | -965757.9457 ppm | 184039.8983 | +8207.3997 ppm | 0.0162 ppm |
| ${}^{197}$Au | 197 | 118 | 59.5388 | 1559.3840 | -961819.0569 ppm | 184973.0451 | +8174.7440 ppm | 0.0029 ppm |
| ${}^{198}$Au | 198 | 119 | 65.9492 | 1565.8964 | -957884.0472 ppm | 185906.2001 | +8133.9343 ppm | 0.0029 ppm |
| ${}^{199}$Au | 199 | 120 | 72.3516 | 1573.4806 | -954018.1255 ppm | 186839.3631 | +8099.4095 ppm | 0.0029 ppm |
| ${}^{200}$Au | 200 | 121 | 78.7460 | 1579.6983 | -950151.2661 ppm | 187772.5342 | +8057.8772 ppm | 0.1434 ppm |
| ${}^{201}$Au | 201 | 122 | 85.1324 | 1586.9302 | -946354.0234 ppm | 188705.7131 | +8022.2628 ppm | 0.0172 ppm |
| ${}^{202}$Au | 202 | 123 | 91.5111 | 1592.9538 | -942552.5957 ppm | 189638.8999 | +7980.5690 ppm | 0.1238 ppm |
| ${}^{203}$Au | 203 | 124 | 97.8820 | 1599.8156 | -938816.7163 ppm | 190572.0944 | +7943.7962 ppm | 0.0163 ppm |
| ${}^{204}$Au | 204 | 125 | 104.2452 | 1605.0720 | -935052.6107 ppm | 191505.2966 | +7899.2370 ppm | 1.0540 ppm |
| ${}^{205}$Au | 205 | 126 | 110.6009 | 1611.3000 | -931359.1873 ppm | 192438.5063 | +7860.0776 ppm | 1.0489 ppm |
| ${}^{206}$Au | 206 | 127 | 116.9492 | 1615.0400 | -927587.4455 ppm | 193371.7235 | +7807.8931 ppm | 1.5632 ppm |
| ${}^{207}$Au | 207 | 128 | 123.2900 | 1619.5680 | -923874.7553 ppm | 194304.9481 | +7760.5914 ppm | 1.5556 ppm |
| ${}^{208}$Au | 208 | 129 | 129.6235 | 1623.0240 | -920134.5525 ppm | 195238.1800 | +7707.6456 ppm | 1.5481 ppm |
| ${}^{209}$Au | 209 | 130 | 135.9498 | 1627.2740 | -916455.4737 ppm | 196171.4191 | +7660.6798 ppm | 2.0527 ppm |
| ${}^{210}$Au | 210 | 131 | 142.2690 | 1630.4400 | -912741.9705 ppm | 197104.6654 | +7607.8661 ppm | 2.0428 ppm |

### Mercury (Z = 80)

_47 of 47 isotopes with a framework prediction; 47 of 47 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{170}$Hg | 170 | 90 | -139.8024 | 1304.0700 | -1107204.6900 ppm | 159803.3375 | +9118.0194 ppm | 1.9058 ppm |
| ${}^{171}$Hg | 171 | 91 | -133.0934 | 1314.3060 | -1101265.1434 ppm | 160736.1939 | +9086.4047 ppm | 1.9239 ppm |
| ${}^{172}$Hg | 172 | 92 | -126.3960 | 1326.7403 | -1095268.0490 ppm | 161669.0619 | +9069.8690 ppm | 0.9366 ppm |
| ${}^{173}$Hg | 173 | 93 | -119.7100 | 1336.4250 | -1089574.7909 ppm | 162601.9414 | +9036.0564 ppm | 1.2428 ppm |
| ${}^{174}$Hg | 174 | 94 | -113.0353 | 1348.4626 | -1083825.3312 ppm | 163534.8321 | +9017.5174 ppm | 0.1185 ppm |
| ${}^{175}$Hg | 175 | 95 | -106.3718 | 1357.8623 | -1078337.7024 ppm | 164467.7340 | +8982.8461 ppm | 0.4974 ppm |
| ${}^{176}$Hg | 176 | 96 | -99.7193 | 1369.7489 | -1072801.1697 ppm | 165400.6470 | +8963.9407 ppm | 0.0678 ppm |
| ${}^{177}$Hg | 177 | 97 | -93.0777 | 1378.8114 | -1067505.7477 ppm | 166333.5708 | +8928.0312 ppm | 0.5139 ppm |
| ${}^{178}$Hg | 178 | 98 | -86.4468 | 1390.4222 | -1062173.0533 ppm | 167266.5053 | +8908.0972 ppm | 0.0649 ppm |
| ${}^{179}$Hg | 179 | 99 | -79.8265 | 1399.1111 | -1057055.1459 ppm | 168199.4504 | +8870.7667 ppm | 0.1687 ppm |
| ${}^{180}$Hg | 180 | 100 | -73.2166 | 1410.5000 | -1051908.2872 ppm | 169132.4060 | +8850.1607 ppm | 0.0754 ppm |
| ${}^{181}$Hg | 181 | 101 | -66.6171 | 1418.9819 | -1046947.1200 ppm | 170065.3719 | +8812.4466 ppm | 0.0912 ppm |
| ${}^{182}$Hg | 182 | 102 | -60.0278 | 1429.9690 | -1041978.3826 ppm | 170998.3480 | +8790.1156 ppm | 0.0578 ppm |
| ${}^{183}$Hg | 183 | 103 | -53.4485 | 1438.2681 | -1037161.7261 ppm | 171931.3341 | +8752.1777 ppm | 0.0416 ppm |
| ${}^{184}$Hg | 184 | 104 | -46.8792 | 1448.8796 | -1032355.4884 ppm | 172864.3302 | +8728.3213 ppm | 0.0556 ppm |
| ${}^{185}$Hg | 185 | 105 | -40.3197 | 1456.7897 | -1027677.0931 ppm | 173797.3362 | +8688.9650 ppm | 0.0792 ppm |
| ${}^{186}$Hg | 186 | 106 | -33.7699 | 1467.2165 | -1023016.3058 ppm | 174730.3518 | +8664.7409 ppm | 0.0673 ppm |
| ${}^{187}$Hg | 187 | 107 | -27.2297 | 1474.8672 | -1018462.4614 ppm | 175663.3770 | +8624.7535 ppm | 0.0739 ppm |
| ${}^{188}$Hg | 188 | 108 | -20.6989 | 1485.0184 | -1013938.4927 ppm | 176596.4116 | +8599.6490 ppm | 0.0388 ppm |
| ${}^{189}$Hg | 189 | 109 | -14.1775 | 1492.5177 | -1009499.0526 ppm | 177529.4557 | +8559.6683 ppm | 0.1793 ppm |
| ${}^{190}$Hg | 190 | 110 | -7.6653 | 1502.3333 | -1005102.2803 ppm | 178462.5089 | +8533.3620 ppm | 0.0899 ppm |
| ${}^{191}$Hg | 191 | 111 | -1.1623 | 1509.6258 | -1000769.9066 ppm | 179395.5713 | +8493.0779 ppm | 0.1252 ppm |
| ${}^{192}$Hg | 192 | 112 | 5.3318 | 1519.1168 | -996490.2179 ppm | 180328.6427 | +8465.6625 ppm | 0.0869 ppm |
| ${}^{193}$Hg | 193 | 113 | 11.8169 | 1526.2388 | -992257.5021 ppm | 181261.7229 | +8425.2898 ppm | 0.0863 ppm |
| ${}^{194}$Hg | 194 | 114 | 18.2932 | 1535.4319 | -988085.9387 ppm | 182194.8120 | +8396.9416 ppm | 0.0160 ppm |
| ${}^{195}$Hg | 195 | 115 | 24.7609 | 1542.3326 | -983945.8367 ppm | 183127.9098 | +8356.2036 ppm | 0.1274 ppm |
| ${}^{196}$Hg | 196 | 116 | 31.2199 | 1551.2165 | -979873.9302 ppm | 184061.0162 | +8326.8837 ppm | 0.0161 ppm |
| ${}^{197}$Hg | 197 | 117 | 37.6704 | 1558.0021 | -975821.3249 ppm | 184994.1311 | +8286.3761 ppm | 0.0175 ppm |
| ${}^{198}$Hg | 198 | 118 | 44.1126 | 1566.4875 | -971839.8250 ppm | 185927.2544 | +8255.6177 ppm | 0.0025 ppm |
| ${}^{199}$Hg | 199 | 119 | 50.5464 | 1573.1506 | -967869.3209 ppm | 186860.3860 | +8215.2997 ppm | 0.0028 ppm |
| ${}^{200}$Hg | 200 | 120 | 56.9720 | 1581.1791 | -963968.6463 ppm | 187793.5258 | +8182.8200 ppm | 0.0028 ppm |
| ${}^{201}$Hg | 201 | 121 | 63.3895 | 1587.4097 | -960067.3110 ppm | 188726.6737 | +8141.0244 ppm | 0.0038 ppm |
| ${}^{202}$Hg | 202 | 122 | 69.7990 | 1595.1638 | -956243.3461 ppm | 189659.8296 | +8107.8498 ppm | 0.0037 ppm |
| ${}^{203}$Hg | 203 | 123 | 76.2006 | 1601.1590 | -952409.1037 ppm | 190592.9935 | +8065.6661 ppm | 0.0086 ppm |
| ${}^{204}$Hg | 204 | 124 | 82.5943 | 1608.6513 | -948656.1731 ppm | 191526.1652 | +8031.8806 ppm | 0.0026 ppm |
| ${}^{205}$Hg | 205 | 125 | 88.9803 | 1614.3202 | -944880.6488 ppm | 192459.3446 | +7988.8394 ppm | 0.0191 ppm |
| ${}^{206}$Hg | 206 | 126 | 95.3586 | 1621.0495 | -941174.7883 ppm | 193392.5318 | +7951.8281 ppm | 0.1065 ppm |
| ${}^{207}$Hg | 207 | 127 | 101.7293 | 1624.6625 | -937384.3515 ppm | 194325.7265 | +7898.9232 ppm | 0.1546 ppm |
| ${}^{208}$Hg | 208 | 128 | 108.0925 | 1629.5118 | -933665.7057 ppm | 195258.9287 | +7852.9992 ppm | 0.1587 ppm |
| ${}^{209}$Hg | 209 | 129 | 114.4483 | 1632.9170 | -929911.7355 ppm | 196192.1383 | +7800.1329 ppm | 0.7704 ppm |
| ${}^{210}$Hg | 210 | 130 | 120.7968 | 1637.7900 | -926244.0326 ppm | 197125.3552 | +7754.7446 ppm | 1.0238 ppm |
| ${}^{211}$Hg | 211 | 131 | 127.1380 | 1640.9470 | -922521.5697 ppm | 198058.5795 | +7701.6200 ppm | 1.0190 ppm |
| ${}^{212}$Hg | 212 | 132 | 133.4720 | 1645.5440 | -918888.8097 ppm | 198991.8108 | +7656.6878 ppm | 1.5188 ppm |
| ${}^{213}$Hg | 213 | 133 | 139.7990 | 1648.4070 | -915191.4740 ppm | 199925.0493 | +7603.2272 ppm | 1.5117 ppm |
| ${}^{214}$Hg | 214 | 134 | 146.1189 | 1652.9360 | -911600.4009 ppm | 200858.2948 | +7558.4393 ppm | 2.0046 ppm |
| ${}^{215}$Hg | 215 | 135 | 152.4318 | 1655.7150 | -907935.9413 ppm | 201791.5473 | +7505.2063 ppm | 1.9952 ppm |
| ${}^{216}$Hg | 216 | 136 | 158.7379 | 1659.9600 | -904372.4357 ppm | 202724.8066 | +7460.1560 ppm | 1.9859 ppm |

### Thallium (Z = 81)

_43 of 43 isotopes with a framework prediction; 43 of 43 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{176}$Tl | 176 | 95 | -122.5590 | 1356.5971 | -1090342.9633 ppm | 165422.7043 | +9022.3578 ppm | 0.5066 ppm |
| ${}^{177}$Tl | 177 | 96 | -115.8802 | 1368.5933 | -1084671.0555 ppm | 166355.5910 | +9003.8496 ppm | 0.1312 ppm |
| ${}^{178}$Tl | 178 | 97 | -109.2125 | 1377.8980 | -1079260.2019 ppm | 167288.4886 | +8969.4806 ppm | 0.6180 ppm |
| ${}^{179}$Tl | 179 | 98 | -102.5556 | 1389.6655 | -1073798.7470 ppm | 168221.3972 | +8949.9767 ppm | 0.2318 ppm |
| ${}^{180}$Tl | 180 | 99 | -95.9094 | 1398.8576 | -1068562.6545 ppm | 169154.3164 | +8915.4968 ppm | 0.4170 ppm |
| ${}^{181}$Tl | 181 | 100 | -89.2738 | 1410.3372 | -1063299.6099 ppm | 170087.2462 | +8895.1495 ppm | 0.0540 ppm |
| ${}^{182}$Tl | 182 | 101 | -82.6487 | 1418.9370 | -1058246.8822 ppm | 171020.1865 | +8857.9475 ppm | 0.0706 ppm |
| ${}^{183}$Tl | 183 | 102 | -76.0338 | 1430.2684 | -1053160.5406 ppm | 171953.1371 | +8837.3798 ppm | 0.0547 ppm |
| ${}^{184}$Tl | 184 | 103 | -69.4292 | 1438.6358 | -1048260.4552 ppm | 172886.0979 | +8799.6471 ppm | 0.0584 ppm |
| ${}^{185}$Tl | 185 | 104 | -62.8347 | 1449.5815 | -1043346.7621 ppm | 173819.0688 | +8777.4751 ppm | 0.1200 ppm |
| ${}^{186}$Tl | 186 | 105 | -56.2501 | 1457.7780 | -1038586.1597 ppm | 174752.0496 | +8739.5899 ppm | 0.1198 ppm |
| ${}^{187}$Tl | 187 | 106 | -49.6753 | 1468.4110 | -1033829.2680 ppm | 175685.0402 | +8716.2772 ppm | 0.0462 ppm |
| ${}^{188}$Tl | 188 | 107 | -43.1102 | 1476.3741 | -1029200.0406 ppm | 176618.0406 | +8677.8870 ppm | 0.1708 ppm |
| ${}^{189}$Tl | 189 | 108 | -36.5547 | 1486.7251 | -1024587.3862 ppm | 177551.0505 | +8653.6403 ppm | 0.0475 ppm |
| ${}^{190}$Tl | 190 | 109 | -30.0087 | 1494.5466 | -1020078.7686 ppm | 178484.0699 | +8615.2838 ppm | 0.0410 ppm |
| ${}^{191}$Tl | 191 | 110 | -23.4720 | 1504.5346 | -1015600.8246 ppm | 179417.0986 | +8589.6655 ppm | 0.0413 ppm |
| ${}^{192}$Tl | 192 | 111 | -16.9446 | 1512.1952 | -1011205.2666 ppm | 180350.1366 | +8551.2384 ppm | 0.1771 ppm |
| ${}^{193}$Tl | 193 | 112 | -10.4263 | 1521.8715 | -1006850.9429 ppm | 181283.1838 | +8524.5698 ppm | 0.0373 ppm |
| ${}^{194}$Tl | 194 | 113 | -3.9170 | 1529.4031 | -1002561.1202 ppm | 182216.2399 | +8486.2548 ppm | 0.0773 ppm |
| ${}^{195}$Tl | 195 | 114 | 2.5834 | 1538.6922 | -998321.0650 ppm | 183149.3050 | +8458.1413 ppm | 0.0613 ppm |
| ${}^{196}$Tl | 196 | 115 | 9.0749 | 1546.1048 | -994130.4771 ppm | 184082.3789 | +8419.9963 ppm | 0.0663 ppm |
| ${}^{197}$Tl | 197 | 116 | 15.5577 | 1555.0338 | -989995.2540 ppm | 185015.4615 | +8390.6200 ppm | 0.0740 ppm |
| ${}^{198}$Tl | 198 | 117 | 22.0319 | 1562.2796 | -985897.5782 ppm | 185948.5527 | +8352.3837 ppm | 0.0409 ppm |
| ${}^{199}$Tl | 199 | 118 | 28.4976 | 1570.8816 | -981858.8355 ppm | 186881.6524 | +8321.9557 ppm | 0.1508 ppm |
| ${}^{200}$Tl | 200 | 119 | 34.9549 | 1577.9407 | -977847.7734 ppm | 187814.7606 | +8283.5258 ppm | 0.0309 ppm |
| ${}^{201}$Tl | 201 | 120 | 41.4039 | 1586.1456 | -973896.5573 ppm | 188747.8770 | +8251.6939 ppm | 0.0758 ppm |
| ${}^{202}$Tl | 202 | 121 | 47.8446 | 1593.0166 | -969966.0394 ppm | 189681.0017 | +8213.0724 ppm | 0.0098 ppm |
| ${}^{203}$Tl | 203 | 122 | 54.2772 | 1600.8688 | -966095.1594 ppm | 190614.1345 | +8180.1074 ppm | 0.0062 ppm |
| ${}^{204}$Tl | 204 | 123 | 60.7018 | 1607.5249 | -962238.9895 ppm | 191547.2754 | +8141.1612 ppm | 0.0061 ppm |
| ${}^{205}$Tl | 205 | 124 | 67.1184 | 1615.0709 | -958442.4587 ppm | 192480.4242 | +8107.3363 ppm | 0.0065 ppm |
| ${}^{206}$Tl | 206 | 125 | 73.5271 | 1621.5747 | -954656.9607 ppm | 193413.5809 | +8068.4049 ppm | 0.0067 ppm |
| ${}^{207}$Tl | 207 | 126 | 79.9281 | 1628.4272 | -950916.9933 ppm | 194346.7453 | +8031.7136 ppm | 0.0282 ppm |
| ${}^{208}$Tl | 208 | 127 | 86.3214 | 1632.2142 | -947113.9329 ppm | 195279.9175 | +7979.4658 ppm | 0.0096 ppm |
| ${}^{209}$Tl | 209 | 128 | 92.7071 | 1637.1802 | -943373.9352 ppm | 196213.0972 | +7933.8637 ppm | 0.0314 ppm |
| ${}^{210}$Tl | 210 | 129 | 99.0852 | 1640.8537 | -939613.6104 ppm | 197146.2845 | +7882.0761 ppm | 0.0593 ppm |
| ${}^{211}$Tl | 211 | 130 | 105.4560 | 1645.7560 | -935922.4876 ppm | 198079.4792 | +7837.1208 ppm | 0.2133 ppm |
| ${}^{212}$Tl | 212 | 131 | 111.8193 | 1649.3600 | -932204.4233 ppm | 199012.6812 | +7785.6976 ppm | 1.0142 ppm |
| ${}^{213}$Tl | 213 | 132 | 118.1754 | 1654.0368 | -928553.3477 ppm | 199945.8906 | +7740.8520 ppm | 0.1361 ppm |
| ${}^{214}$Tl | 214 | 133 | 124.5243 | 1657.4300 | -924869.0602 ppm | 200879.1071 | +7689.6591 ppm | 0.9813 ppm |
| ${}^{215}$Tl | 215 | 134 | 130.8660 | 1661.9500 | -921257.5418 ppm | 201812.3308 | +7644.5901 ppm | 1.4976 ppm |
| ${}^{216}$Tl | 216 | 135 | 137.2007 | 1665.1440 | -917604.2829 ppm | 202745.5615 | +7593.5939 ppm | 1.4906 ppm |
| ${}^{217}$Tl | 217 | 136 | 143.5285 | 1669.3810 | -914022.9433 ppm | 203678.7992 | +7548.3416 ppm | 1.9768 ppm |
| ${}^{218}$Tl | 218 | 137 | 149.8493 | 1672.4960 | -910403.7949 ppm | 204612.0438 | +7497.2831 ppm | 1.9677 ppm |

### Lead (Z = 82)

_43 of 43 isotopes with a framework prediction; 43 of 43 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{178}$Pb | 178 | 96 | -132.2307 | 1368.9688 | -1096591.4771 ppm | 167310.7245 | +9053.7665 ppm | 0.1398 ppm |
| ${}^{179}$Pb | 179 | 97 | -125.5368 | 1378.5619 | -1091063.5638 ppm | 168243.5960 | +9020.6572 ppm | 0.4872 ppm |
| ${}^{180}$Pb | 180 | 98 | -118.8538 | 1390.6259 | -1085467.8398 ppm | 169176.4785 | +9002.8502 ppm | 0.0739 ppm |
| ${}^{181}$Pb | 181 | 99 | -112.1817 | 1399.8667 | -1080137.3950 ppm | 170109.3718 | +8968.4084 ppm | 0.5044 ppm |
| ${}^{182}$Pb | 182 | 100 | -105.5203 | 1411.6520 | -1074749.4963 ppm | 171042.2758 | +8949.5506 ppm | 0.0713 ppm |
| ${}^{183}$Pb | 183 | 101 | -98.8695 | 1420.4788 | -1069602.9121 ppm | 171975.1904 | +8913.4489 ppm | 0.1700 ppm |
| ${}^{184}$Pb | 184 | 102 | -92.2291 | 1432.0217 | -1064404.8161 ppm | 172908.1155 | +8893.7893 ppm | 0.0747 ppm |
| ${}^{185}$Pb | 185 | 103 | -85.5990 | 1440.5826 | -1059419.7413 ppm | 173841.0508 | +8856.9424 ppm | 0.0939 ppm |
| ${}^{186}$Pb | 186 | 104 | -78.9792 | 1451.7936 | -1054401.1167 ppm | 174773.9964 | +8835.9821 ppm | 0.0635 ppm |
| ${}^{187}$Pb | 187 | 105 | -72.3694 | 1460.1710 | -1049562.2849 ppm | 175706.9520 | +8798.8907 ppm | 0.0292 ppm |
| ${}^{188}$Pb | 188 | 106 | -65.7696 | 1471.0664 | -1044708.7737 ppm | 176639.9176 | +8776.7568 ppm | 0.0578 ppm |
| ${}^{189}$Pb | 189 | 107 | -59.1796 | 1479.1707 | -1040008.6090 ppm | 177572.8930 | +8738.9182 ppm | 0.0799 ppm |
| ${}^{190}$Pb | 190 | 108 | -52.5993 | 1489.8146 | -1035305.9079 ppm | 178505.8782 | +8716.0086 ppm | 0.0707 ppm |
| ${}^{191}$Pb | 191 | 109 | -46.0285 | 1497.7605 | -1030731.5763 ppm | 179438.8729 | +8678.0943 ppm | 0.0372 ppm |
| ${}^{192}$Pb | 192 | 110 | -39.4673 | 1508.0925 | -1026170.3475 ppm | 180371.8771 | +8654.0859 ppm | 0.0320 ppm |
| ${}^{193}$Pb | 193 | 111 | -32.9154 | 1515.8412 | -1021714.2988 ppm | 181304.8906 | +8615.8832 ppm | 0.0572 ppm |
| ${}^{194}$Pb | 194 | 112 | -26.3728 | 1525.8911 | -1017283.5438 ppm | 182237.9134 | +8590.9709 ppm | 0.0965 ppm |
| ${}^{195}$Pb | 195 | 113 | -19.8393 | 1533.4926 | -1012937.3477 ppm | 183170.9453 | +8552.7672 ppm | 0.0280 ppm |
| ${}^{196}$Pb | 196 | 114 | -13.3149 | 1543.1741 | -1008628.2456 ppm | 184103.9863 | +8526.4946 ppm | 0.0422 ppm |
| ${}^{197}$Pb | 197 | 115 | -6.7994 | 1550.6426 | -1004384.8759 ppm | 185037.0362 | +8488.3728 ppm | 0.0262 ppm |
| ${}^{198}$Pb | 198 | 116 | -0.2927 | 1560.0360 | -1000187.6198 ppm | 185970.0950 | +8461.2108 ppm | 0.0474 ppm |
| ${}^{199}$Pb | 199 | 117 | 6.2053 | 1567.2716 | -996040.7234 ppm | 186903.1624 | +8422.6281 ppm | 0.0368 ppm |
| ${}^{200}$Pb | 200 | 118 | 12.6946 | 1576.3620 | -991946.9067 ppm | 187836.2385 | +8394.5192 ppm | 0.0537 ppm |
| ${}^{201}$Pb | 201 | 119 | 19.1754 | 1583.4535 | -987890.1458 ppm | 188769.3232 | +8355.9680 ppm | 0.0734 ppm |
| ${}^{202}$Pb | 202 | 120 | 25.6478 | 1592.1944 | -983891.5645 ppm | 189702.4162 | +8326.6837 ppm | 0.0202 ppm |
| ${}^{203}$Pb | 203 | 121 | 32.1118 | 1599.1116 | -979918.9783 ppm | 190635.5176 | +8288.0062 ppm | 0.0347 ppm |
| ${}^{204}$Pb | 204 | 122 | 38.5676 | 1607.5063 | -976007.8157 ppm | 191568.6272 | +8257.5920 ppm | 0.0060 ppm |
| ${}^{205}$Pb | 205 | 123 | 45.0152 | 1614.2379 | -972113.6350 ppm | 192501.7450 | +8218.7357 ppm | 0.0060 ppm |
| ${}^{206}$Pb | 206 | 124 | 51.4548 | 1622.3246 | -968283.2824 ppm | 193434.8709 | +8187.4192 ppm | 0.0060 ppm |
| ${}^{207}$Pb | 207 | 125 | 57.8864 | 1629.0623 | -964466.4164 ppm | 194368.0047 | +8149.3933 ppm | 0.0059 ppm |
| ${}^{208}$Pb | 208 | 126 | 64.3102 | 1636.4302 | -960700.9496 ppm | 195301.1464 | +8115.0530 ppm | 0.0059 ppm |
| ${}^{209}$Pb | 209 | 127 | 70.7261 | 1640.3676 | -956884.0000 ppm | 196234.2958 | +8063.3167 ppm | 0.0090 ppm |
| ${}^{210}$Pb | 210 | 128 | 77.1343 | 1645.5528 | -953125.5905 ppm | 197167.4530 | +8018.5452 ppm | 0.0074 ppm |
| ${}^{211}$Pb | 211 | 129 | 83.5349 | 1649.3887 | -949354.0150 ppm | 198100.6179 | +7967.3182 ppm | 0.0115 ppm |
| ${}^{212}$Pb | 212 | 130 | 89.9280 | 1654.5159 | -945646.9600 ppm | 199033.7902 | +7923.2061 ppm | 0.0093 ppm |
| ${}^{213}$Pb | 213 | 131 | 96.3136 | 1658.2419 | -941918.2676 ppm | 199966.9701 | +7872.4289 ppm | 0.0350 ppm |
| ${}^{214}$Pb | 214 | 132 | 102.6918 | 1663.2926 | -938259.9490 ppm | 200900.1573 | +7828.8632 ppm | 0.0099 ppm |
| ${}^{215}$Pb | 215 | 133 | 109.0627 | 1666.8387 | -934569.1459 ppm | 201833.3518 | +7778.1689 ppm | 0.2631 ppm |
| ${}^{216}$Pb | 216 | 134 | 115.4264 | 1671.8400 | -930958.4888 ppm | 202766.5535 | +7734.7826 ppm | 0.9953 ppm |
| ${}^{217}$Pb | 217 | 135 | 121.7829 | 1675.0230 | -927294.7945 ppm | 203699.7624 | +7683.9408 ppm | 1.4838 ppm |
| ${}^{218}$Pb | 218 | 136 | 128.1323 | 1679.6900 | -923716.6688 ppm | 204632.9784 | +7640.4568 ppm | 1.4770 ppm |
| ${}^{219}$Pb | 219 | 137 | 134.4748 | 1682.7960 | -920088.4685 ppm | 205566.2014 | +7589.4009 ppm | 1.9587 ppm |
| ${}^{220}$Pb | 220 | 138 | 140.8103 | 1687.4000 | -916551.8930 ppm | 206499.4313 | +7546.1171 ppm | 1.9498 ppm |

### Bismuth (Z = 83)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{184}$Bi | 184 | 101 | -115.2788 | 1419.0080 | -1081239.0260 ppm | 172930.3829 | +8951.2680 ppm | 0.7120 ppm |
| ${}^{185}$Bi | 185 | 102 | -108.6129 | 1430.4200 | -1075930.7411 ppm | 173863.2823 | +8931.4730 ppm | 0.4703 ppm |
| ${}^{186}$Bi | 186 | 103 | -101.9573 | 1439.4759 | -1070829.4756 ppm | 174796.1922 | +8896.9240 ppm | 0.0979 ppm |
| ${}^{187}$Bi | 187 | 104 | -95.3121 | 1450.7850 | -1065696.9230 ppm | 175729.1124 | +8876.2862 ppm | 0.0574 ppm |
| ${}^{188}$Bi | 188 | 105 | -88.6771 | 1459.6678 | -1060751.5542 ppm | 176662.0428 | +8841.9475 ppm | 0.0638 ppm |
| ${}^{189}$Bi | 189 | 106 | -82.0521 | 1470.6090 | -1055794.6653 ppm | 177594.9833 | +8819.8243 ppm | 0.1184 ppm |
| ${}^{190}$Bi | 190 | 107 | -75.4371 | 1479.2115 | -1050998.2040 ppm | 178527.9337 | +8784.6587 ppm | 0.1185 ppm |
| ${}^{191}$Bi | 191 | 108 | -68.8320 | 1489.9263 | -1046198.2284 ppm | 179460.8939 | +8761.8931 ppm | 0.0421 ppm |
| ${}^{192}$Bi | 192 | 109 | -62.2365 | 1498.2928 | -1041538.2694 ppm | 180393.8639 | +8726.1726 ppm | 0.1684 ppm |
| ${}^{193}$Bi | 193 | 110 | -55.6506 | 1508.7142 | -1036886.1260 ppm | 181326.8435 | +8702.4057 ppm | 0.0421 ppm |
| ${}^{194}$Bi | 194 | 111 | -49.0742 | 1516.9239 | -1032351.1492 ppm | 182259.8325 | +8666.5901 ppm | 0.0291 ppm |
| ${}^{195}$Bi | 195 | 112 | -42.5072 | 1526.9978 | -1027837.1159 ppm | 183192.8309 | +8641.5456 ppm | 0.0291 ppm |
| ${}^{196}$Bi | 196 | 113 | -35.9495 | 1535.0526 | -1023419.0398 ppm | 184125.8386 | +8605.6514 ppm | 0.1338 ppm |
| ${}^{197}$Bi | 197 | 114 | -29.4009 | 1544.8021 | -1019032.1169 ppm | 185058.8554 | +8579.4868 ppm | 0.0454 ppm |
| ${}^{198}$Bi | 198 | 115 | -22.8613 | 1552.5600 | -1014724.9031 ppm | 185991.8812 | +8542.7438 ppm | 0.1495 ppm |
| ${}^{199}$Bi | 199 | 116 | -16.3307 | 1562.0551 | -1010454.6129 ppm | 186924.9161 | +8515.8705 ppm | 0.0573 ppm |
| ${}^{200}$Bi | 200 | 117 | -9.8089 | 1569.6994 | -1006248.9081 ppm | 187857.9597 | +8479.2929 ppm | 0.1219 ppm |
| ${}^{201}$Bi | 201 | 118 | -3.2959 | 1578.8291 | -1002087.5419 ppm | 188791.0121 | +8451.1280 ppm | 0.0650 ppm |
| ${}^{202}$Bi | 202 | 119 | 3.2085 | 1586.2223 | -997977.2551 ppm | 189724.0731 | +8413.9796 ppm | 0.0744 ppm |
| ${}^{203}$Bi | 203 | 120 | 9.7044 | 1595.0677 | -993916.0099 ppm | 190657.1427 | +8384.9877 ppm | 0.0676 ppm |
| ${}^{204}$Bi | 204 | 121 | 16.1918 | 1602.2600 | -989894.4101 ppm | 191590.2207 | +8347.5517 ppm | 0.0483 ppm |
| ${}^{205}$Bi | 205 | 122 | 22.6708 | 1610.7510 | -985925.2997 ppm | 192523.3071 | +8317.3829 ppm | 0.0252 ppm |
| ${}^{206}$Bi | 206 | 123 | 29.1416 | 1617.7849 | -981986.7074 ppm | 193456.4017 | +8279.8932 ppm | 0.0398 ppm |
| ${}^{207}$Bi | 207 | 124 | 35.6043 | 1625.8826 | -978101.5787 ppm | 194389.5045 | +8248.3712 ppm | 0.0124 ppm |
| ${}^{208}$Bi | 208 | 125 | 42.0588 | 1632.7695 | -974240.8138 ppm | 195322.6154 | +8210.8931 ppm | 0.0119 ppm |
| ${}^{209}$Bi | 209 | 126 | 48.5054 | 1640.2293 | -970427.6846 ppm | 196255.7342 | +8176.7819 ppm | 0.0070 ppm |
| ${}^{210}$Bi | 210 | 127 | 54.9440 | 1644.8339 | -966595.9954 ppm | 197188.8610 | +8128.3205 ppm | 0.0070 ppm |
| ${}^{211}$Bi | 211 | 128 | 61.3749 | 1649.9724 | -962802.4775 ppm | 198121.9956 | +8083.0985 ppm | 0.0277 ppm |
| ${}^{212}$Bi | 212 | 129 | 67.7980 | 1654.3026 | -959017.1689 ppm | 199055.1379 | +8034.2169 ppm | 0.0094 ppm |
| ${}^{213}$Bi | 213 | 130 | 74.2135 | 1659.4876 | -955279.2857 ppm | 199988.2878 | +7990.1781 ppm | 0.0256 ppm |
| ${}^{214}$Bi | 214 | 131 | 80.6214 | 1663.5280 | -951535.9080 ppm | 200921.4453 | +7940.8023 ppm | 0.0562 ppm |
| ${}^{215}$Bi | 215 | 132 | 87.0218 | 1668.7693 | -947852.7109 ppm | 201854.6103 | +7897.9686 ppm | 0.0281 ppm |
| ${}^{216}$Bi | 216 | 133 | 93.4148 | 1672.5959 | -944149.8038 ppm | 202787.7828 | +7848.4834 ppm | 0.0556 ppm |
| ${}^{217}$Bi | 217 | 134 | 99.8005 | 1677.8113 | -940517.4464 ppm | 203720.9625 | +7806.4163 ppm | 0.0876 ppm |
| ${}^{218}$Bi | 218 | 135 | 106.1789 | 1681.3965 | -936850.7450 ppm | 204654.1495 | +7756.6827 ppm | 0.1330 ppm |
| ${}^{219}$Bi | 219 | 136 | 112.5502 | 1686.3000 | -933256.1218 ppm | 205587.3436 | +7714.2685 ppm | 0.9817 ppm |
| ${}^{220}$Bi | 220 | 137 | 118.9144 | 1689.8200 | -929628.9733 ppm | 206520.5449 | +7664.7236 ppm | 1.4635 ppm |
| ${}^{221}$Bi | 221 | 138 | 125.2715 | 1694.6280 | -926077.2805 ppm | 207453.7532 | +7622.5107 ppm | 1.4568 ppm |
| ${}^{222}$Bi | 222 | 139 | 131.6217 | 1697.8560 | -922477.7013 ppm | 208386.9684 | +7573.3614 ppm | 1.4502 ppm |
| ${}^{223}$Bi | 223 | 140 | 137.9650 | 1702.8280 | -918978.8932 ppm | 209320.1905 | +7531.7669 ppm | 1.9235 ppm |
| ${}^{224}$Bi | 224 | 141 | 144.3015 | 1705.9840 | -915414.5007 ppm | 210253.4194 | +7483.1443 ppm | 1.9148 ppm |

### Polonium (Z = 84)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{186}$Po | 186 | 102 | -125.1844 | 1431.4465 | -1087453.1010 ppm | 174818.6370 | +8984.2673 ppm | 0.1055 ppm |
| ${}^{187}$Po | 187 | 103 | -118.5034 | 1440.7955 | -1082248.5609 ppm | 175751.5213 | +8951.6059 ppm | 0.1873 ppm |
| ${}^{188}$Po | 188 | 104 | -111.8327 | 1452.2350 | -1077007.3185 ppm | 176684.4161 | +8931.3950 ppm | 0.1140 ppm |
| ${}^{189}$Po | 189 | 105 | -105.1724 | 1461.1840 | -1071977.5263 ppm | 177617.3212 | +8897.1828 ppm | 0.1253 ppm |
| ${}^{190}$Po | 190 | 106 | -98.5223 | 1472.3960 | -1066912.8962 ppm | 178550.2365 | +8876.2887 ppm | 0.0744 ppm |
| ${}^{191}$Po | 191 | 107 | -91.8822 | 1480.9733 | -1062041.7799 ppm | 179483.1619 | +8840.7290 ppm | 0.0399 ppm |
| ${}^{192}$Po | 192 | 108 | -85.2521 | 1492.0424 | -1057137.8608 ppm | 180416.0972 | +8819.6507 ppm | 0.0595 ppm |
| ${}^{193}$Po | 193 | 109 | -78.6318 | 1500.3725 | -1052408.2044 ppm | 181349.0423 | +8783.4750 ppm | 0.0808 ppm |
| ${}^{194}$Po | 194 | 110 | -72.0213 | 1511.1232 | -1047660.7505 ppm | 182281.9972 | +8761.2382 ppm | 0.0714 ppm |
| ${}^{195}$Po | 195 | 111 | -65.4203 | 1519.3065 | -1043059.3147 ppm | 183214.9616 | +8725.0236 ppm | 0.0333 ppm |
| ${}^{196}$Po | 196 | 112 | -58.8288 | 1529.7299 | -1038456.9964 ppm | 184147.9356 | +8701.6073 ppm | 0.0295 ppm |
| ${}^{197}$Po | 197 | 113 | -52.2467 | 1537.7256 | -1033976.6186 ppm | 185080.9189 | +8665.1336 ppm | 0.0537 ppm |
| ${}^{198}$Po | 198 | 114 | -45.6739 | 1547.8771 | -1029507.4339 ppm | 186013.9115 | +8640.8694 ppm | 0.0945 ppm |
| ${}^{199}$Po | 199 | 115 | -39.1102 | 1555.7140 | -1025139.7164 ppm | 186946.9133 | +8604.3025 ppm | 0.0293 ppm |
| ${}^{200}$Po | 200 | 116 | -32.5556 | 1565.4881 | -1020795.8087 ppm | 187879.9241 | +8578.6390 ppm | 0.0407 ppm |
| ${}^{201}$Po | 201 | 117 | -26.0099 | 1573.1389 | -1016533.7770 ppm | 188812.9438 | +8541.8393 ppm | 0.0264 ppm |
| ${}^{202}$Po | 202 | 118 | -19.4731 | 1582.6307 | -1012304.2709 ppm | 189745.9724 | +8515.3190 ppm | 0.0461 ppm |
| ${}^{203}$Po | 203 | 119 | -12.9451 | 1590.0712 | -1008141.1798 ppm | 190679.0098 | +8478.1655 ppm | 0.0245 ppm |
| ${}^{204}$Po | 204 | 120 | -6.4256 | 1599.1728 | -1004018.1074 ppm | 191612.0558 | +8450.2376 ppm | 0.0530 ppm |
| ${}^{205}$Po | 205 | 121 | 0.0852 | 1606.4244 | -999946.9607 ppm | 192545.1104 | +8412.8567 ppm | 0.0527 ppm |
| ${}^{206}$Po | 206 | 122 | 6.5876 | 1615.1630 | -995921.4059 ppm | 193478.1734 | +8383.6978 ppm | 0.0209 ppm |
| ${}^{207}$Po | 207 | 123 | 13.0816 | 1622.1914 | -991935.8354 ppm | 194411.2448 | +8345.9192 ppm | 0.0345 ppm |
| ${}^{208}$Po | 208 | 124 | 19.5674 | 1630.5862 | -987999.7958 ppm | 195344.3245 | +8315.6591 ppm | 0.0086 ppm |
| ${}^{209}$Po | 209 | 125 | 26.0449 | 1637.5543 | -984095.2252 ppm | 196277.4123 | +8278.3408 ppm | 0.0091 ppm |
| ${}^{210}$Po | 210 | 126 | 32.5144 | 1645.2127 | -980236.9603 ppm | 197210.5083 | +8244.9777 ppm | 0.0059 ppm |
| ${}^{211}$Po | 211 | 127 | 38.9759 | 1649.7635 | -976374.8748 ppm | 198143.6122 | +8196.0297 ppm | 0.0064 ppm |
| ${}^{212}$Po | 212 | 128 | 45.4294 | 1655.7717 | -972562.9966 ppm | 199076.7241 | +8155.0264 ppm | 0.0058 ppm |
| ${}^{213}$Po | 213 | 129 | 51.8751 | 1660.1271 | -968752.3181 ppm | 200009.8438 | +8106.0503 ppm | 0.0154 ppm |
| ${}^{214}$Po | 214 | 130 | 58.3131 | 1666.0149 | -964998.4615 ppm | 200942.9713 | +8065.3218 ppm | 0.0073 ppm |
| ${}^{215}$Po | 215 | 131 | 64.7434 | 1670.1580 | -961235.1786 ppm | 201876.1064 | +8016.2299 ppm | 0.0106 ppm |
| ${}^{216}$Po | 216 | 132 | 71.1661 | 1675.9052 | -957535.7350 ppm | 202809.2491 | +7975.6682 ppm | 0.0090 ppm |
| ${}^{217}$Po | 217 | 133 | 77.5813 | 1679.8754 | -953817.2394 ppm | 203742.3994 | +7926.6577 ppm | 0.0324 ppm |
| ${}^{218}$Po | 218 | 134 | 83.9891 | 1685.4735 | -950168.8655 ppm | 204675.5570 | +7886.2148 ppm | 0.0097 ppm |
| ${}^{219}$Po | 219 | 135 | 90.3895 | 1689.2201 | -946490.4061 ppm | 205608.7220 | +7837.0315 ppm | 0.0776 ppm |
| ${}^{220}$Po | 220 | 136 | 96.7826 | 1694.7094 | -942891.3070 ppm | 206541.8943 | +7796.9019 ppm | 0.0864 ppm |
| ${}^{221}$Po | 221 | 137 | 103.1686 | 1698.2704 | -939250.7847 ppm | 207475.0737 | +7747.7331 ppm | 0.0950 ppm |
| ${}^{222}$Po | 222 | 138 | 109.5474 | 1703.6292 | -935697.6108 ppm | 208408.2603 | +7707.8035 ppm | 0.1937 ppm |
| ${}^{223}$Po | 223 | 139 | 115.9192 | 1707.0650 | -932094.4350 ppm | 209341.4540 | +7659.1494 ppm | 0.9416 ppm |
| ${}^{224}$Po | 224 | 140 | 122.2840 | 1712.2560 | -928583.0961 ppm | 210274.6546 | +7619.4657 ppm | 0.9374 ppm |
| ${}^{225}$Po | 225 | 141 | 128.6419 | 1715.8500 | -925027.2892 ppm | 211207.8621 | +7571.3349 ppm | 1.4309 ppm |
| ${}^{226}$Po | 226 | 142 | 134.9930 | 1720.7640 | -921550.5472 ppm | 212141.0765 | +7531.8034 ppm | 1.9023 ppm |
| ${}^{227}$Po | 227 | 143 | 141.3373 | 1724.2920 | -918031.6927 ppm | 213074.2976 | +7484.2533 ppm | 1.8939 ppm |

### Astatine (Z = 85)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{191}$At | 191 | 106 | -115.1793 | 1471.2584 | -1078286.2776 ppm | 179505.6767 | +8916.6240 ppm | 0.0905 ppm |
| ${}^{192}$At | 192 | 107 | -108.5142 | 1480.2678 | -1073307.1161 ppm | 180438.5769 | +8883.3385 ppm | 0.1558 ppm |
| ${}^{193}$At | 193 | 108 | -101.8591 | 1491.3322 | -1068300.7174 ppm | 181371.4872 | +8861.9849 ppm | 0.1203 ppm |
| ${}^{194}$At | 194 | 109 | -95.2139 | 1500.0527 | -1063473.7050 ppm | 182304.4075 | +8827.8206 ppm | 0.1301 ppm |
| ${}^{195}$At | 195 | 110 | -88.5786 | 1510.8778 | -1058627.2268 ppm | 183237.3376 | +8805.7495 ppm | 0.0527 ppm |
| ${}^{196}$At | 196 | 111 | -81.9530 | 1519.3920 | -1053938.0007 ppm | 184170.2774 | +8771.1871 ppm | 0.1656 ppm |
| ${}^{197}$At | 197 | 112 | -75.3370 | 1529.9054 | -1049242.8884 ppm | 185103.2268 | +8748.0179 ppm | 0.0435 ppm |
| ${}^{198}$At | 198 | 113 | -68.7304 | 1538.3302 | -1044678.6052 ppm | 186036.1857 | +8713.7102 ppm | 0.0266 ppm |
| ${}^{199}$At | 199 | 114 | -62.1333 | 1548.5162 | -1040124.4236 ppm | 186969.1540 | +8689.3816 ppm | 0.0290 ppm |
| ${}^{200}$At | 200 | 115 | -55.5455 | 1556.7520 | -1035680.3544 ppm | 187902.1316 | +8654.7866 ppm | 0.1313 ppm |
| ${}^{201}$At | 201 | 116 | -48.9668 | 1566.6249 | -1031256.2242 ppm | 188835.1183 | +8629.4040 ppm | 0.0437 ppm |
| ${}^{202}$At | 202 | 117 | -42.3972 | 1574.5019 | -1026927.3469 ppm | 189768.1141 | +8593.6214 ppm | 0.1467 ppm |
| ${}^{203}$At | 203 | 118 | -35.8365 | 1584.1407 | -1022622.0442 ppm | 190701.1189 | +8567.6363 ppm | 0.0562 ppm |
| ${}^{204}$At | 204 | 119 | -29.2847 | 1591.9246 | -1018395.7861 ppm | 191634.1325 | +8532.1072 ppm | 0.1193 ppm |
| ${}^{205}$At | 205 | 120 | -22.7417 | 1601.1052 | -1014203.7341 ppm | 192567.1549 | +8504.3472 ppm | 0.0631 ppm |
| ${}^{206}$At | 206 | 121 | -16.2073 | 1608.6314 | -1010075.2140 ppm | 193500.1860 | +8468.2062 ppm | 0.0705 ppm |
| ${}^{207}$At | 207 | 122 | -9.6815 | 1617.4908 | -1005985.5103 ppm | 194433.2256 | +8439.4322 ppm | 0.0643 ppm |
| ${}^{208}$At | 208 | 123 | -3.1642 | 1624.8046 | -1001947.4248 ppm | 195366.2737 | +8402.9332 ppm | 0.0460 ppm |
| ${}^{209}$At | 209 | 124 | 3.3448 | 1633.2898 | -997952.1350 ppm | 196299.3302 | +8372.8948 ppm | 0.0244 ppm |
| ${}^{210}$At | 210 | 125 | 9.8454 | 1640.4494 | -993998.3467 ppm | 197232.3949 | +8336.3515 ppm | 0.0393 ppm |
| ${}^{211}$At | 211 | 126 | 16.3379 | 1648.1958 | -990087.4275 ppm | 198165.4679 | +8303.2070 ppm | 0.0139 ppm |
| ${}^{212}$At | 212 | 127 | 22.8222 | 1653.2481 | -986195.5376 ppm | 199098.5490 | +8256.6601 ppm | 0.0121 ppm |
| ${}^{213}$At | 213 | 128 | 29.2985 | 1659.2708 | -982342.5335 ppm | 200031.6381 | +8215.5235 ppm | 0.0247 ppm |
| ${}^{214}$At | 214 | 129 | 35.7669 | 1664.1417 | -978507.3008 ppm | 200964.7352 | +8168.9869 ppm | 0.0200 ppm |
| ${}^{215}$At | 215 | 130 | 42.2274 | 1670.0905 | -974715.4873 ppm | 201897.8400 | +8128.3494 ppm | 0.0331 ppm |
| ${}^{216}$At | 216 | 131 | 48.6802 | 1674.6485 | -970931.1054 ppm | 202830.9527 | +8081.1599 ppm | 0.0178 ppm |
| ${}^{217}$At | 217 | 132 | 55.1253 | 1680.5819 | -967198.7124 ppm | 203764.0731 | +8041.3035 ppm | 0.0247 ppm |
| ${}^{218}$At | 218 | 133 | 61.5627 | 1684.9476 | -963463.1282 ppm | 204697.2010 | +7994.0695 ppm | 0.0566 ppm |
| ${}^{219}$At | 219 | 134 | 67.9927 | 1690.7231 | -959784.8692 ppm | 205630.3365 | +7954.2710 ppm | 0.0159 ppm |
| ${}^{220}$At | 220 | 135 | 74.4151 | 1694.8147 | -956092.4621 ppm | 206563.4794 | +7906.5899 ppm | 0.0682 ppm |
| ${}^{221}$At | 221 | 136 | 80.8303 | 1700.4791 | -952466.1830 ppm | 207496.6297 | +7867.0772 ppm | 0.0679 ppm |
| ${}^{222}$At | 222 | 137 | 87.2381 | 1704.3801 | -948815.3577 ppm | 208429.7873 | +7819.3637 ppm | 0.0766 ppm |
| ${}^{223}$At | 223 | 138 | 93.6387 | 1709.9764 | -945239.7767 ppm | 209362.9522 | +7780.3388 ppm | 0.0673 ppm |
| ${}^{224}$At | 224 | 139 | 100.0322 | 1713.7647 | -941630.1729 ppm | 210296.1241 | +7732.9662 ppm | 0.1071 ppm |
| ${}^{225}$At | 225 | 140 | 106.4185 | 1719.2250 | -938100.8657 ppm | 211229.3032 | +7694.1958 ppm | 1.4309 ppm |
| ${}^{226}$At | 226 | 141 | 112.7979 | 1723.0240 | -934534.9067 ppm | 212162.4892 | +7647.3236 ppm | 1.4245 ppm |
| ${}^{227}$At | 227 | 142 | 119.1704 | 1728.1510 | -931041.6826 ppm | 213095.6822 | +7608.4747 ppm | 1.4183 ppm |
| ${}^{228}$At | 228 | 143 | 125.5360 | 1731.8880 | -927514.9527 ppm | 214028.8820 | +7562.0336 ppm | 1.8812 ppm |
| ${}^{229}$At | 229 | 144 | 131.8948 | 1736.9650 | -924065.9476 ppm | 214962.0886 | +7522.8322 ppm | 1.8730 ppm |

### Radon (Z = 86)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{193}$Rn | 193 | 107 | -125.3323 | 1481.4396 | -1084601.6974 ppm | 181394.1781 | +8937.0732 ppm | 0.1397 ppm |
| ${}^{194}$Rn | 194 | 108 | -118.6521 | 1492.8292 | -1079481.3920 ppm | 182327.0634 | +8917.2314 ppm | 0.0922 ppm |
| ${}^{195}$Rn | 195 | 109 | -111.9821 | 1501.5749 | -1074576.4010 ppm | 183259.9587 | +8882.9628 ppm | 0.2845 ppm |
| ${}^{196}$Rn | 196 | 110 | -105.3219 | 1512.7213 | -1069624.1295 ppm | 184192.8640 | +8862.3640 ppm | 0.0770 ppm |
| ${}^{197}$Rn | 197 | 111 | -98.6716 | 1521.2574 | -1064861.8640 ppm | 185125.7791 | +8827.6768 ppm | 0.0882 ppm |
| ${}^{198}$Rn | 198 | 112 | -92.0310 | 1532.0695 | -1060069.7309 ppm | 186058.7039 | +8805.8407 ppm | 0.0728 ppm |
| ${}^{199}$Rn | 199 | 113 | -85.4000 | 1540.4703 | -1055437.6236 ppm | 186991.6384 | +8771.1535 ppm | 0.0394 ppm |
| ${}^{200}$Rn | 200 | 114 | -78.7785 | 1550.9822 | -1050792.6667 ppm | 187924.5823 | +8748.2949 ppm | 0.0311 ppm |
| ${}^{201}$Rn | 201 | 115 | -72.1664 | 1559.1605 | -1046285.4347 ppm | 188857.5356 | +8713.1403 ppm | 0.0541 ppm |
| ${}^{202}$Rn | 202 | 116 | -65.5636 | 1569.3990 | -1041776.2488 ppm | 189790.4982 | +8689.4274 ppm | 0.0931 ppm |
| ${}^{203}$Rn | 203 | 117 | -58.9700 | 1577.3798 | -1037384.7566 ppm | 190723.4700 | +8653.9529 ppm | 0.0307 ppm |
| ${}^{204}$Rn | 204 | 118 | -52.3854 | 1587.2372 | -1033004.1351 ppm | 191656.4509 | +8628.8349 ppm | 0.0392 ppm |
| ${}^{205}$Rn | 205 | 119 | -45.8098 | 1595.0481 | -1028720.0064 ppm | 192589.4407 | +8593.1992 ppm | 0.0266 ppm |
| ${}^{206}$Rn | 206 | 120 | -39.2431 | 1604.5426 | -1024457.4797 ppm | 193522.4394 | +8566.8048 ppm | 0.0448 ppm |
| ${}^{207}$Rn | 207 | 121 | -32.6851 | 1612.1157 | -1020274.6715 ppm | 194455.4469 | +8530.6605 ppm | 0.0246 ppm |
| ${}^{208}$Rn | 208 | 122 | -26.1358 | 1621.2077 | -1016121.2181 ppm | 195388.4630 | +8502.8147 ppm | 0.0525 ppm |
| ${}^{209}$Rn | 209 | 123 | -19.5952 | 1628.5647 | -1012032.1600 ppm | 196321.4878 | +8466.2915 ppm | 0.0512 ppm |
| ${}^{210}$Rn | 210 | 124 | -13.0629 | 1637.2997 | -1007978.3478 ppm | 197254.5210 | +8437.2642 ppm | 0.0233 ppm |
| ${}^{211}$Rn | 211 | 125 | -6.5391 | 1644.5216 | -1003976.3163 ppm | 198187.5626 | +8400.7908 ppm | 0.0347 ppm |
| ${}^{212}$Rn | 212 | 126 | -0.0236 | 1652.4968 | -1000014.3022 ppm | 199120.6125 | +8368.5507 ppm | 0.0157 ppm |
| ${}^{213}$Rn | 213 | 127 | 6.4837 | 1657.6049 | -996088.5406 ppm | 200053.6706 | +8322.0831 ppm | 0.0170 ppm |
| ${}^{214}$Rn | 214 | 128 | 12.9828 | 1664.2999 | -992199.2331 ppm | 200986.7369 | +8284.1192 ppm | 0.0461 ppm |
| ${}^{215}$Rn | 215 | 129 | 19.4739 | 1669.2205 | -988333.5148 ppm | 201919.8112 | +8237.6161 ppm | 0.0304 ppm |
| ${}^{216}$Rn | 216 | 130 | 25.9571 | 1675.8695 | -984511.2630 ppm | 202852.8935 | +8200.2451 ppm | 0.0287 ppm |
| ${}^{217}$Rn | 217 | 131 | 32.4324 | 1680.5356 | -980701.1539 ppm | 203785.9836 | +8153.3680 ppm | 0.0208 ppm |
| ${}^{218}$Rn | 218 | 132 | 38.8999 | 1687.0481 | -976942.0292 ppm | 204719.0815 | +8116.1270 ppm | 0.0114 ppm |
| ${}^{219}$Rn | 219 | 133 | 45.3597 | 1691.5075 | -973183.8566 ppm | 205652.1871 | +8069.1194 ppm | 0.0103 ppm |
| ${}^{220}$Rn | 220 | 134 | 51.8119 | 1697.7961 | -969482.8601 ppm | 206585.3004 | +8031.5754 ppm | 0.0088 ppm |
| ${}^{221}$Rn | 221 | 135 | 58.2565 | 1702.0081 | -965771.8951 ppm | 207518.4212 | +7984.2406 ppm | 0.0278 ppm |
| ${}^{222}$Rn | 222 | 136 | 64.6937 | 1708.1788 | -962127.1074 ppm | 208451.5494 | +7946.9167 ppm | 0.0094 ppm |
| ${}^{223}$Rn | 223 | 137 | 71.1234 | 1712.2324 | -958461.5714 ppm | 209384.6851 | +7899.6918 ppm | 0.0377 ppm |
| ${}^{224}$Rn | 224 | 138 | 77.5459 | 1718.2483 | -954869.2153 ppm | 210317.8280 | +7862.4033 ppm | 0.0470 ppm |
| ${}^{225}$Rn | 225 | 139 | 83.9611 | 1722.2306 | -951248.6258 ppm | 211250.9783 | +7815.7035 ppm | 0.0531 ppm |
| ${}^{226}$Rn | 226 | 140 | 90.3692 | 1728.0888 | -947705.7257 ppm | 212184.1356 | +7778.4322 ppm | 0.0498 ppm |
| ${}^{227}$Rn | 227 | 141 | 96.7701 | 1732.0215 | -944128.8113 ppm | 213117.3001 | +7732.3477 ppm | 0.0666 ppm |
| ${}^{228}$Rn | 228 | 142 | 103.1640 | 1737.7352 | -940633.0567 ppm | 214050.4716 | +7695.1513 ppm | 0.0832 ppm |
| ${}^{229}$Rn | 229 | 143 | 109.5510 | 1741.6876 | -937100.6593 ppm | 214983.6501 | +7649.9945 ppm | 0.0611 ppm |
| ${}^{230}$Rn | 230 | 144 | 115.9311 | 1746.8500 | -933634.2035 ppm | 215916.8354 | +7611.4318 ppm | 0.9346 ppm |
| ${}^{231}$Rn | 231 | 145 | 122.3044 | 1750.7490 | -930141.6900 ppm | 216850.0275 | +7565.8733 ppm | 1.3936 ppm |

### Francium (Z = 87)

_37 of 37 isotopes with a framework prediction; 37 of 37 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{197}$Fr | 197 | 110 | -122.2506 | 1511.7315 | -1080867.9374 ppm | 185148.5758 | +8903.8336 ppm | 0.3075 ppm |
| ${}^{198}$Fr | 198 | 111 | -115.5755 | 1520.4791 | -1076012.5766 ppm | 186081.4661 | +8870.1362 ppm | 0.1688 ppm |
| ${}^{199}$Fr | 199 | 112 | -108.9103 | 1531.3567 | -1071120.1310 ppm | 187014.3663 | +8848.4223 ppm | 0.0740 ppm |
| ${}^{200}$Fr | 200 | 113 | -102.2548 | 1540.0658 | -1066396.3621 ppm | 187947.2762 | +8815.2348 ppm | 0.1638 ppm |
| ${}^{201}$Fr | 201 | 114 | -95.6089 | 1550.6822 | -1061655.9983 ppm | 188880.1957 | +8792.7042 ppm | 0.0485 ppm |
| ${}^{202}$Fr | 202 | 115 | -88.9724 | 1559.2405 | -1057061.3999 ppm | 189813.1248 | +8759.4135 ppm | 0.0321 ppm |
| ${}^{203}$Fr | 203 | 116 | -82.3454 | 1569.5370 | -1052464.7916 ppm | 190746.0632 | +8735.7723 ppm | 0.0330 ppm |
| ${}^{204}$Fr | 204 | 117 | -75.7277 | 1577.8774 | -1047993.3999 ppm | 191679.0109 | +8702.0280 ppm | 0.1294 ppm |
| ${}^{205}$Fr | 205 | 118 | -69.1192 | 1587.8658 | -1043529.5940 ppm | 192611.9677 | +8677.3661 ppm | 0.0410 ppm |
| ${}^{206}$Fr | 206 | 119 | -62.5197 | 1595.8742 | -1039175.8270 ppm | 193544.9337 | +8642.5822 ppm | 0.1449 ppm |
| ${}^{207}$Fr | 207 | 120 | -55.9292 | 1605.5477 | -1034834.9723 ppm | 194477.9086 | +8616.8911 ppm | 0.0910 ppm |
| ${}^{208}$Fr | 208 | 121 | -49.3476 | 1613.4349 | -1030585.4345 ppm | 195410.8925 | +8582.1937 ppm | 0.0602 ppm |
| ${}^{209}$Fr | 209 | 122 | -42.7748 | 1622.6234 | -1026361.5016 ppm | 196343.8851 | +8554.6152 ppm | 0.0591 ppm |
| ${}^{210}$Fr | 210 | 123 | -36.2107 | 1630.2561 | -1022211.6400 ppm | 197276.8864 | +8519.3217 ppm | 0.0686 ppm |
| ${}^{211}$Fr | 211 | 124 | -29.6551 | 1639.1242 | -1018092.0556 ppm | 198209.8962 | +8490.7459 ppm | 0.0610 ppm |
| ${}^{212}$Fr | 212 | 125 | -23.1081 | 1646.5712 | -1014034.0679 ppm | 199142.9146 | +8455.2251 ppm | 0.0444 ppm |
| ${}^{213}$Fr | 213 | 126 | -16.5695 | 1654.6808 | -1010013.6945 ppm | 200075.9414 | +8423.4477 ppm | 0.0237 ppm |
| ${}^{214}$Fr | 214 | 127 | -10.0392 | 1660.1562 | -1006047.1187 ppm | 201008.9765 | +8378.6841 ppm | 0.0427 ppm |
| ${}^{215}$Fr | 215 | 128 | -3.5171 | 1666.9511 | -1002109.8913 ppm | 201942.0199 | +8341.0222 ppm | 0.0353 ppm |
| ${}^{216}$Fr | 216 | 129 | 2.9968 | 1672.3695 | -998208.0229 ppm | 202875.0714 | +8296.8523 ppm | 0.0207 ppm |
| ${}^{217}$Fr | 217 | 130 | 9.5027 | 1679.0972 | -994340.5748 ppm | 203808.1309 | +8259.6609 ppm | 0.0323 ppm |
| ${}^{218}$Fr | 218 | 131 | 16.0006 | 1684.4237 | -990500.8282 ppm | 204741.1984 | +8215.8940 ppm | 0.0209 ppm |
| ${}^{219}$Fr | 219 | 132 | 22.4906 | 1690.9375 | -986699.3030 ppm | 205674.2738 | +8178.4341 ppm | 0.0337 ppm |
| ${}^{220}$Fr | 220 | 133 | 28.9729 | 1696.1435 | -982918.3911 ppm | 206607.3571 | +8134.9195 ppm | 0.0197 ppm |
| ${}^{221}$Fr | 221 | 134 | 35.4473 | 1702.4198 | -979178.2582 ppm | 207540.4480 | +8097.0792 ppm | 0.0237 ppm |
| ${}^{222}$Fr | 222 | 135 | 41.9142 | 1707.3903 | -975451.3141 ppm | 208473.5466 | +8053.2518 ppm | 0.0360 ppm |
| ${}^{223}$Fr | 223 | 136 | 48.3735 | 1713.4574 | -971768.5043 ppm | 209406.6527 | +8015.1762 ppm | 0.0093 ppm |
| ${}^{224}$Fr | 224 | 137 | 54.8253 | 1718.1624 | -968090.7623 ppm | 210339.7664 | +7970.8979 ppm | 0.0536 ppm |
| ${}^{225}$Fr | 225 | 138 | 61.2696 | 1724.1618 | -964464.1061 ppm | 211272.8874 | +7933.2737 ppm | 0.0571 ppm |
| ${}^{226}$Fr | 226 | 139 | 67.7067 | 1728.5332 | -960829.9851 ppm | 212206.0158 | +7888.2249 ppm | 0.0296 ppm |
| ${}^{227}$Fr | 227 | 140 | 74.1364 | 1734.4426 | -957256.3267 ppm | 213139.1514 | +7850.9387 ppm | 0.0279 ppm |
| ${}^{228}$Fr | 228 | 141 | 80.5590 | 1738.8121 | -953670.0748 ppm | 214072.2943 | +7806.7081 ppm | 0.0317 ppm |
| ${}^{229}$Fr | 229 | 142 | 86.9745 | 1744.5994 | -950146.4313 ppm | 215005.4442 | +7769.5953 ppm | 0.0234 ppm |
| ${}^{230}$Fr | 230 | 143 | 93.3829 | 1748.8522 | -946603.3027 ppm | 215938.6012 | +7725.6226 ppm | 0.0305 ppm |
| ${}^{231}$Fr | 231 | 144 | 99.7844 | 1754.3297 | -943121.0792 ppm | 216871.7652 | +7687.7987 ppm | 0.0359 ppm |
| ${}^{232}$Fr | 232 | 145 | 106.1789 | 1758.4088 | -939616.4728 ppm | 217804.9361 | +7643.8145 ppm | 0.0646 ppm |
| ${}^{233}$Fr | 233 | 146 | 112.5666 | 1763.6329 | -936173.4358 ppm | 218738.1138 | +7605.5554 ppm | 0.0901 ppm |

### Radium (Z = 88)

_35 of 35 isotopes with a framework prediction; 35 of 35 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{201}$Ra | 201 | 113 | -119.2941 | 1541.5516 | -1077385.7259 ppm | 188903.0986 | +8870.0438 ppm | 0.1084 ppm |
| ${}^{202}$Ra | 202 | 114 | -112.6237 | 1552.4848 | -1072544.1520 ppm | 189835.9937 | +8848.9238 ppm | 0.0798 ppm |
| ${}^{203}$Ra | 203 | 115 | -105.9629 | 1561.0297 | -1067880.1396 ppm | 190768.8983 | +8815.3207 ppm | 0.0512 ppm |
| ${}^{204}$Ra | 204 | 116 | -99.3116 | 1571.6413 | -1063189.7630 ppm | 191701.8125 | +8793.0677 ppm | 0.0470 ppm |
| ${}^{205}$Ra | 205 | 117 | -92.6698 | 1579.9698 | -1058652.8681 ppm | 192634.7360 | +8759.0204 ppm | 0.1192 ppm |
| ${}^{206}$Ra | 206 | 118 | -86.0372 | 1590.2794 | -1054101.9256 ppm | 193567.6688 | +8735.7656 ppm | 0.0938 ppm |
| ${}^{207}$Ra | 207 | 119 | -79.4138 | 1598.4023 | -1049683.2255 ppm | 194500.6109 | +8701.3438 ppm | 0.3023 ppm |
| ${}^{208}$Ra | 208 | 120 | -72.7995 | 1608.2597 | -1045265.9967 ppm | 195433.5620 | +8676.3292 ppm | 0.0466 ppm |
| ${}^{209}$Ra | 209 | 121 | -66.1942 | 1616.2007 | -1040956.6471 ppm | 196366.5221 | +8641.6711 ppm | 0.0295 ppm |
| ${}^{210}$Ra | 210 | 122 | -59.5977 | 1625.6874 | -1036660.0219 ppm | 197299.4911 | +8615.3584 ppm | 0.0470 ppm |
| ${}^{211}$Ra | 211 | 123 | -53.0101 | 1633.3697 | -1032454.4440 ppm | 198232.4689 | +8580.0799 ppm | 0.0253 ppm |
| ${}^{212}$Ra | 212 | 124 | -46.4312 | 1642.4717 | -1028269.0870 ppm | 199165.4554 | +8552.4288 ppm | 0.0519 ppm |
| ${}^{213}$Ra | 213 | 125 | -39.8608 | 1649.9987 | -1024158.1090 ppm | 200098.4505 | +8517.0749 ppm | 0.0495 ppm |
| ${}^{214}$Ra | 214 | 126 | -33.2990 | 1658.3228 | -1020079.9471 ppm | 201031.4541 | +8486.1271 ppm | 0.0263 ppm |
| ${}^{215}$Ra | 215 | 127 | -26.7456 | 1663.9549 | -1016073.5384 ppm | 201964.4661 | +8441.9536 ppm | 0.0360 ppm |
| ${}^{216}$Ra | 216 | 128 | -20.2006 | 1671.2667 | -1012086.9896 ppm | 202897.4865 | +8406.6502 ppm | 0.0398 ppm |
| ${}^{217}$Ra | 217 | 129 | -13.6638 | 1676.7399 | -1008149.0086 ppm | 203830.5151 | +8362.5414 ppm | 0.0349 ppm |
| ${}^{218}$Ra | 218 | 130 | -7.1351 | 1684.0553 | -1004236.8628 ppm | 204763.5518 | +8328.0249 ppm | 0.0483 ppm |
| ${}^{219}$Ra | 219 | 131 | -0.6145 | 1689.3783 | -1000363.7585 ppm | 205696.5967 | +8284.0168 ppm | 0.0334 ppm |
| ${}^{220}$Ra | 220 | 132 | 5.8981 | 1696.5713 | -996523.5343 ppm | 206629.6495 | +8249.6490 ppm | 0.0371 ppm |
| ${}^{221}$Ra | 221 | 133 | 12.4028 | 1701.9509 | -992712.6187 ppm | 207562.7102 | +8206.7494 ppm | 0.0225 ppm |
| ${}^{222}$Ra | 222 | 134 | 18.8996 | 1708.6659 | -988938.9521 ppm | 208495.7788 | +8170.7855 ppm | 0.0215 ppm |
| ${}^{223}$Ra | 223 | 135 | 25.3888 | 1713.8242 | -985185.8999 ppm | 209428.8551 | +8127.6274 ppm | 0.0101 ppm |
| ${}^{224}$Ra | 224 | 136 | 31.8702 | 1720.3029 | -981474.0605 ppm | 210361.9390 | +8091.2715 ppm | 0.0087 ppm |
| ${}^{225}$Ra | 225 | 137 | 38.3441 | 1725.2070 | -977774.1990 ppm | 211295.0306 | +8047.7027 ppm | 0.0124 ppm |
| ${}^{226}$Ra | 226 | 138 | 44.8105 | 1731.6038 | -974121.9787 ppm | 212228.1296 | +8011.7029 ppm | 0.0091 ppm |
| ${}^{227}$Ra | 227 | 139 | 51.2694 | 1736.1652 | -970469.7339 ppm | 213161.2361 | +7967.3079 ppm | 0.0092 ppm |
| ${}^{228}$Ra | 228 | 140 | 57.7210 | 1742.4738 | -966874.1050 ppm | 214094.3500 | +7931.6290 ppm | 0.0094 ppm |
| ${}^{229}$Ra | 229 | 141 | 64.1653 | 1746.9233 | -963269.5362 ppm | 215027.4711 | +7887.5138 ppm | 0.0724 ppm |
| ${}^{230}$Ra | 230 | 142 | 70.6024 | 1753.0403 | -959725.7436 ppm | 215960.5994 | +7851.6600 ppm | 0.0480 ppm |
| ${}^{231}$Ra | 231 | 143 | 77.0323 | 1757.4115 | -956167.1533 ppm | 216893.7349 | +7807.9748 ppm | 0.0528 ppm |
| ${}^{232}$Ra | 232 | 144 | 83.4552 | 1763.2023 | -952668.3743 ppm | 217826.8774 | +7771.3195 ppm | 0.0423 ppm |
| ${}^{233}$Ra | 233 | 145 | 89.8711 | 1767.4365 | -949151.7139 ppm | 218760.0270 | +7727.7857 ppm | 0.0396 ppm |
| ${}^{234}$Ra | 234 | 146 | 96.2801 | 1772.9113 | -945693.8003 ppm | 219693.1834 | +7690.3910 ppm | 0.0385 ppm |
| ${}^{235}$Ra | 235 | 147 | 102.6822 | 1776.8350 | -942210.6338 ppm | 220626.3468 | +7645.9717 ppm | 1.3699 ppm |

### Actinium (Z = 89)

_33 of 33 isotopes with a framework prediction; 33 of 33 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{205}$Ac | 205 | 116 | -116.4616 | 1570.8846 | -1074137.5951 ppm | 192657.7455 | +8835.6498 ppm | 0.3106 ppm |
| ${}^{206}$Ac | 206 | 117 | -109.7955 | 1579.5779 | -1069509.4078 ppm | 193590.6449 | +8803.3536 ppm | 0.3392 ppm |
| ${}^{207}$Ac | 207 | 118 | -103.1388 | 1589.9877 | -1064867.6955 ppm | 194523.5536 | +8780.3980 ppm | 0.2917 ppm |
| ${}^{208}$Ac | 208 | 119 | -96.4915 | 1598.4444 | -1060365.8489 ppm | 195456.4716 | +8747.5422 ppm | 0.3328 ppm |
| ${}^{209}$Ac | 209 | 120 | -89.8533 | 1608.4317 | -1055863.8979 ppm | 196389.3989 | +8722.9780 ppm | 0.2868 ppm |
| ${}^{210}$Ac | 210 | 121 | -83.2242 | 1616.5838 | -1051481.5071 ppm | 197322.3352 | +8689.2311 ppm | 0.3180 ppm |
| ${}^{211}$Ac | 211 | 122 | -76.6041 | 1626.2757 | -1047103.9892 ppm | 198255.2805 | +8663.7515 ppm | 0.2735 ppm |
| ${}^{212}$Ac | 212 | 123 | -69.9929 | 1634.1910 | -1042830.2937 ppm | 199188.2347 | +8629.4825 ppm | 0.1108 ppm |
| ${}^{213}$Ac | 213 | 124 | -63.3905 | 1643.4208 | -1038572.2779 ppm | 200121.1978 | +8602.2626 ppm | 0.0588 ppm |
| ${}^{214}$Ac | 214 | 125 | -56.7968 | 1651.1999 | -1034397.2897 ppm | 201054.1695 | +8568.0002 ppm | 0.0680 ppm |
| ${}^{215}$Ac | 215 | 126 | -50.2117 | 1659.6739 | -1030253.9747 ppm | 201987.1499 | +8537.5993 ppm | 0.0619 ppm |
| ${}^{216}$Ac | 216 | 127 | -43.6352 | 1665.6261 | -1026197.4704 ppm | 202920.1387 | +8494.8818 ppm | 0.0459 ppm |
| ${}^{217}$Ac | 217 | 128 | -37.0671 | 1673.1448 | -1022154.1381 ppm | 203853.1361 | +8460.4161 ppm | 0.0555 ppm |
| ${}^{218}$Ac | 218 | 129 | -30.5073 | 1679.0676 | -1018169.2017 ppm | 204786.1417 | +8418.3828 ppm | 0.2837 ppm |
| ${}^{219}$Ac | 219 | 130 | -23.9558 | 1686.4202 | -1014205.1267 ppm | 205719.1556 | +8383.8420 ppm | 0.2523 ppm |
| ${}^{220}$Ac | 220 | 131 | -17.4125 | 1692.3173 | -1010289.1337 ppm | 206652.1777 | +8342.4941 ppm | 0.0299 ppm |
| ${}^{221}$Ac | 221 | 132 | -10.8772 | 1699.6014 | -1006399.8729 ppm | 207585.2079 | +8308.3531 ppm | 0.2764 ppm |
| ${}^{222}$Ac | 222 | 133 | -4.3500 | 1705.5819 | -1002550.4429 ppm | 208518.2461 | +8268.2037 ppm | 0.0227 ppm |
| ${}^{223}$Ac | 223 | 134 | 2.1693 | 1712.4500 | -998733.1991 ppm | 209451.2922 | +8232.7606 ppm | 0.0334 ppm |
| ${}^{224}$Ac | 224 | 135 | 8.6808 | 1718.1122 | -994947.4686 ppm | 210384.3461 | +8191.8459 ppm | 0.0196 ppm |
| ${}^{225}$Ac | 225 | 136 | 15.1845 | 1724.7804 | -991196.2477 ppm | 211317.4078 | +8156.1712 ppm | 0.0227 ppm |
| ${}^{226}$Ac | 226 | 137 | 21.6806 | 1730.1798 | -987469.1741 ppm | 212250.4772 | +8114.7740 ppm | 0.0147 ppm |
| ${}^{227}$Ac | 227 | 138 | 28.1690 | 1736.7108 | -983780.2464 ppm | 213183.5542 | +8079.1727 ppm | 0.0091 ppm |
| ${}^{228}$Ac | 228 | 139 | 34.6499 | 1741.7370 | -980106.1039 ppm | 214116.6387 | +8036.7780 ppm | 0.0099 ppm |
| ${}^{229}$Ac | 229 | 140 | 41.1234 | 1748.0130 | -976474.2044 ppm | 215049.7307 | +8000.6949 ppm | 0.0568 ppm |
| ${}^{230}$Ac | 230 | 141 | 47.5895 | 1752.9359 | -972851.5555 ppm | 215982.8300 | +7958.5952 ppm | 0.0739 ppm |
| ${}^{231}$Ac | 231 | 142 | 54.0483 | 1759.0827 | -969274.7451 ppm | 216915.9366 | +7922.6276 ppm | 0.0606 ppm |
| ${}^{232}$Ac | 232 | 143 | 60.4998 | 1763.7625 | -965698.4327 ppm | 217849.0505 | +7880.1629 ppm | 0.0603 ppm |
| ${}^{233}$Ac | 233 | 144 | 66.9442 | 1769.6802 | -962171.5771 ppm | 218782.1715 | +7843.8445 ppm | 0.0601 ppm |
| ${}^{234}$Ac | 234 | 145 | 73.3815 | 1774.2183 | -958640.0886 ppm | 219715.2997 | +7801.4925 ppm | 0.0641 ppm |
| ${}^{235}$Ac | 235 | 146 | 79.8118 | 1779.7737 | -955156.2104 ppm | 220648.4348 | +7764.2161 ppm | 0.0638 ppm |
| ${}^{236}$Ac | 236 | 147 | 86.2351 | 1783.9812 | -951661.4130 ppm | 221581.5769 | +7721.1108 ppm | 0.1737 ppm |
| ${}^{237}$Ac | 237 | 148 | 92.6516 | 1789.3500 | -948220.5395 ppm | 222514.7259 | +7683.2604 ppm | 1.8097 ppm |

### Thorium (Z = 90)

_32 of 32 isotopes with a framework prediction; 32 of 32 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{208}$Th | 208 | 118 | -120.4235 | 1591.7349 | -1075655.5233 ppm | 195479.6214 | +8836.1573 ppm | 0.1644 ppm |
| ${}^{209}$Th | 209 | 119 | -113.7521 | 1600.1040 | -1071090.4414 ppm | 196412.5154 | +8802.5898 ppm | 0.5311 ppm |
| ${}^{210}$Th | 210 | 120 | -107.0900 | 1610.5060 | -1066494.6069 ppm | 197345.4187 | +8779.9237 ppm | 0.0967 ppm |
| ${}^{211}$Th | 211 | 121 | -100.4370 | 1618.7605 | -1062045.6432 ppm | 198278.3311 | +8746.4716 ppm | 0.4379 ppm |
| ${}^{212}$Th | 212 | 122 | -93.7932 | 1628.5973 | -1057591.4041 ppm | 199211.2527 | +8721.4634 ppm | 0.0512 ppm |
| ${}^{213}$Th | 213 | 123 | -87.1584 | 1636.6594 | -1053253.8295 ppm | 200144.1833 | +8687.7128 ppm | 0.0465 ppm |
| ${}^{214}$Th | 214 | 124 | -80.5325 | 1646.1559 | -1048921.5292 ppm | 201077.1228 | +8661.5799 ppm | 0.0535 ppm |
| ${}^{215}$Th | 215 | 125 | -73.9154 | 1654.0007 | -1044688.8315 ppm | 202010.0712 | +8627.4158 ppm | 0.0316 ppm |
| ${}^{216}$Th | 216 | 126 | -67.3070 | 1662.6949 | -1040480.6513 ppm | 202943.0282 | +8597.8691 ppm | 0.0552 ppm |
| ${}^{217}$Th | 217 | 127 | -60.7072 | 1668.8590 | -1036376.4789 ppm | 203875.9939 | +8556.0136 ppm | 0.0525 ppm |
| ${}^{218}$Th | 218 | 128 | -54.1160 | 1676.7694 | -1032273.9620 ppm | 204808.9681 | +8523.2571 ppm | 0.0518 ppm |
| ${}^{219}$Th | 219 | 129 | -47.5332 | 1682.7446 | -1028247.4312 ppm | 205741.9507 | +8481.2756 ppm | 0.2767 ppm |
| ${}^{220}$Th | 220 | 130 | -40.9588 | 1690.5892 | -1024227.5263 ppm | 206674.9417 | +8448.9152 ppm | 0.0668 ppm |
| ${}^{221}$Th | 221 | 131 | -34.3926 | 1696.4101 | -1020273.7802 ppm | 207607.9410 | +8406.9759 ppm | 0.0388 ppm |
| ${}^{222}$Th | 222 | 132 | -27.8347 | 1704.2183 | -1016332.8157 ppm | 208540.9484 | +8375.1445 ppm | 0.0494 ppm |
| ${}^{223}$Th | 223 | 133 | -21.2848 | 1710.1073 | -1012446.4840 ppm | 209473.9640 | +8334.3220 ppm | 0.0382 ppm |
| ${}^{224}$Th | 224 | 134 | -14.7430 | 1717.5684 | -1008583.6349 ppm | 210406.9876 | +8301.4998 ppm | 0.0460 ppm |
| ${}^{225}$Th | 225 | 135 | -8.2091 | 1723.3252 | -1004763.5085 ppm | 211340.0191 | +8260.8086 ppm | 0.0243 ppm |
| ${}^{226}$Th | 226 | 136 | -1.6830 | 1730.5090 | -1000972.5597 ppm | 212273.0585 | +8227.3500 ppm | 0.0213 ppm |
| ${}^{227}$Th | 227 | 137 | 4.8353 | 1735.9732 | -997214.6742 ppm | 213206.1056 | +8186.0248 ppm | 0.0099 ppm |
| ${}^{228}$Th | 228 | 138 | 11.3458 | 1743.0784 | -993490.9253 ppm | 214139.1605 | +8152.8878 ppm | 0.0085 ppm |
| ${}^{229}$Th | 229 | 139 | 17.8488 | 1748.3351 | -989790.9826 ppm | 215072.2229 | +8111.3415 ppm | 0.0113 ppm |
| ${}^{230}$Th | 230 | 140 | 24.3442 | 1755.1294 | -986129.6867 ppm | 216005.2929 | +8077.4265 ppm | 0.0056 ppm |
| ${}^{231}$Th | 231 | 141 | 30.8321 | 1760.2474 | -982484.2033 ppm | 216938.3704 | +8035.9884 ppm | 0.0057 ppm |
| ${}^{232}$Th | 232 | 142 | 37.3127 | 1766.6878 | -978879.8667 ppm | 217871.4553 | +8001.1099 ppm | 0.0066 ppm |
| ${}^{233}$Th | 233 | 143 | 43.7859 | 1771.4742 | -975282.7867 ppm | 218804.5475 | +7958.8848 ppm | 0.0066 ppm |
| ${}^{234}$Th | 234 | 144 | 50.2519 | 1777.6642 | -971731.5123 ppm | 219737.6470 | +7923.5442 ppm | 0.0119 ppm |
| ${}^{235}$Th | 235 | 145 | 56.7107 | 1782.3308 | -968181.7348 ppm | 220670.7536 | +7881.5246 ppm | 0.0596 ppm |
| ${}^{236}$Th | 236 | 146 | 63.1624 | 1788.1646 | -964677.5499 ppm | 221603.8673 | +7845.2454 ppm | 0.0635 ppm |
| ${}^{237}$Th | 237 | 147 | 69.6070 | 1792.5361 | -961168.4249 ppm | 222536.9881 | +7802.6301 ppm | 0.0717 ppm |
| ${}^{238}$Th | 238 | 148 | 76.0447 | 1798.0900 | -957708.0856 ppm | 223470.1159 | +7765.5408 ppm | 1.2770 ppm |
| ${}^{239}$Th | 239 | 149 | 82.4754 | 1802.0600 | -954232.6936 ppm | 224403.2505 | +7722.4368 ppm | 1.7945 ppm |

### Protactinium (Z = 91)

_31 of 31 isotopes with a framework prediction; 31 of 31 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{211}$Pa | 211 | 120 | -124.5090 | 1609.8023 | -1077344.2707 ppm | 198301.6208 | +8822.9964 ppm | 0.3534 ppm |
| ${}^{212}$Pa | 212 | 121 | -117.8322 | 1618.3293 | -1072810.9875 ppm | 199234.5094 | +8790.7715 ppm | 0.4436 ppm |
| ${}^{213}$Pa | 213 | 122 | -111.1645 | 1628.3430 | -1068268.5016 ppm | 200167.4072 | +8766.4531 ppm | 0.2881 ppm |
| ${}^{214}$Pa | 214 | 123 | -104.5060 | 1636.6086 | -1063855.2323 ppm | 201100.3141 | +8733.5623 ppm | 0.4073 ppm |
| ${}^{215}$Pa | 215 | 124 | -97.8565 | 1646.3353 | -1059438.9990 ppm | 202033.2300 | +8708.3805 ppm | 0.4117 ppm |
| ${}^{216}$Pa | 216 | 125 | -91.2159 | 1654.3873 | -1055135.7783 ppm | 202966.1548 | +8675.0812 ppm | 0.1225 ppm |
| ${}^{217}$Pa | 217 | 126 | -84.5842 | 1663.2277 | -1050855.4343 ppm | 203899.0885 | +8646.0658 ppm | 0.0618 ppm |
| ${}^{218}$Pa | 218 | 127 | -77.9611 | 1669.7042 | -1046691.5819 ppm | 204832.0309 | +8605.6191 ppm | 0.0879 ppm |
| ${}^{219}$Pa | 219 | 128 | -71.3467 | 1677.8418 | -1042522.9163 ppm | 205764.9819 | +8573.7968 ppm | 0.3417 ppm |
| ${}^{220}$Pa | 220 | 129 | -64.7409 | 1684.2180 | -1038439.7230 ppm | 206697.9415 | +8533.6371 ppm | 0.0715 ppm |
| ${}^{221}$Pa | 221 | 130 | -58.1435 | 1692.1928 | -1034359.8420 ppm | 207630.9095 | +8501.7134 ppm | 0.2884 ppm |
| ${}^{222}$Pa | 222 | 131 | -51.5544 | 1698.5747 | -1030351.5941 ppm | 208563.8859 | +8462.3505 ppm | 0.4188 ppm |
| ${}^{223}$Pa | 223 | 132 | -44.9737 | 1706.3727 | -1026356.3200 ppm | 209496.8706 | +8430.2554 ppm | 0.3641 ppm |
| ${}^{224}$Pa | 224 | 133 | -38.4012 | 1712.9193 | -1022418.5468 ppm | 210429.8634 | +8392.4386 ppm | 0.0364 ppm |
| ${}^{225}$Pa | 225 | 134 | -31.8367 | 1720.4963 | -1018504.3884 ppm | 211362.8644 | +8359.9543 ppm | 0.3906 ppm |
| ${}^{226}$Pa | 226 | 135 | -25.2803 | 1726.8907 | -1014639.2219 ppm | 212295.8735 | +8322.1317 ppm | 0.0533 ppm |
| ${}^{227}$Pa | 227 | 136 | -18.7319 | 1734.1653 | -1010801.6760 ppm | 213228.8904 | +8288.8771 ppm | 0.0343 ppm |
| ${}^{228}$Pa | 228 | 137 | -12.1913 | 1740.1433 | -1007005.9272 ppm | 214161.9153 | +8249.7976 ppm | 0.0204 ppm |
| ${}^{229}$Pa | 229 | 138 | -5.6585 | 1747.2414 | -1003238.5543 ppm | 215094.9479 | +8216.3894 ppm | 0.0154 ppm |
| ${}^{230}$Pa | 230 | 139 | 0.8665 | 1753.0360 | -999505.6973 ppm | 216027.9883 | +8177.1751 ppm | 0.0142 ppm |
| ${}^{231}$Pa | 231 | 140 | 7.3840 | 1759.8566 | -995804.2265 ppm | 216961.0363 | +8143.1424 ppm | 0.0082 ppm |
| ${}^{232}$Pa | 232 | 141 | 13.8938 | 1765.4057 | -992129.9526 ppm | 217894.0918 | +8103.5085 ppm | 0.0354 ppm |
| ${}^{233}$Pa | 233 | 142 | 20.3962 | 1771.9341 | -988489.2980 ppm | 218827.1549 | +8068.7980 ppm | 0.0061 ppm |
| ${}^{234}$Pa | 234 | 143 | 26.8912 | 1777.1560 | -984868.4239 ppm | 219760.2253 | +8028.3772 ppm | 0.0188 ppm |
| ${}^{235}$Pa | 235 | 144 | 33.3788 | 1783.2773 | -981282.3304 ppm | 220693.3031 | +7992.4758 ppm | 0.0638 ppm |
| ${}^{236}$Pa | 236 | 145 | 39.8591 | 1788.3035 | -977711.1950 ppm | 221626.3882 | +7951.8925 ppm | 0.0635 ppm |
| ${}^{237}$Pa | 237 | 146 | 46.3323 | 1794.1812 | -974176.3522 ppm | 222559.4805 | +7915.5716 ppm | 0.0591 ppm |
| ${}^{238}$Pa | 238 | 147 | 52.7983 | 1798.8861 | -970649.4328 ppm | 223492.5799 | +7874.2582 ppm | 0.0714 ppm |
| ${}^{239}$Pa | 239 | 148 | 59.2573 | 1804.4500 | -967160.4701 ppm | 224425.6863 | +7837.5015 ppm | 0.8785 ppm |
| ${}^{240}$Pa | 240 | 149 | 65.7093 | 1808.8800 | -963674.0642 ppm | 225358.7998 | +7795.5415 ppm | 0.8956 ppm |
| ${}^{241}$Pa | 241 | 150 | 72.1543 | 1814.2480 | -960229.0863 ppm | 226291.9202 | +7758.1925 ppm | 1.3357 ppm |

### Uranium (Z = 92)

_29 of 29 isotopes with a framework prediction; 29 of 29 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{215}$U | 215 | 123 | -122.0352 | 1638.4682 | -1074481.2859 ppm | 202056.6263 | +8789.5099 ppm | 0.5199 ppm |
| ${}^{216}$U | 216 | 124 | -115.3621 | 1648.3624 | -1069985.8671 ppm | 202989.5186 | +8764.9091 ppm | 0.1396 ppm |
| ${}^{217}$U | 217 | 125 | -108.6979 | 1656.5780 | -1065615.9506 ppm | 203922.4199 | +8731.9613 ppm | 0.3963 ppm |
| ${}^{218}$U | 218 | 126 | -102.0427 | 1665.6768 | -1061262.0266 ppm | 204855.3301 | +8704.2281 ppm | 0.0675 ppm |
| ${}^{219}$U | 219 | 127 | -95.3964 | 1672.3468 | -1057043.4062 ppm | 205788.2492 | +8664.5434 ppm | 0.0654 ppm |
| ${}^{220}$U | 220 | 128 | -88.7587 | 1680.8000 | -1052807.4231 ppm | 206721.1770 | +8633.5488 ppm | 0.4909 ppm |
| ${}^{221}$U | 221 | 129 | -82.1297 | 1687.2654 | -1048676.2334 ppm | 207654.1134 | +8594.1128 ppm | 0.3504 ppm |
| ${}^{222}$U | 222 | 130 | -75.5093 | 1695.5839 | -1044532.9111 ppm | 208587.0584 | +8563.6258 ppm | 0.2514 ppm |
| ${}^{223}$U | 223 | 131 | -68.8973 | 1701.8827 | -1040482.9984 ppm | 209520.0118 | +8523.6485 ppm | 0.2843 ppm |
| ${}^{224}$U | 224 | 132 | -62.2937 | 1710.2566 | -1036423.6146 ppm | 210452.9737 | +8494.0970 ppm | 0.0731 ppm |
| ${}^{225}$U | 225 | 133 | -55.6984 | 1716.6986 | -1032445.0870 ppm | 211385.9438 | +8455.5531 ppm | 0.0474 ppm |
| ${}^{226}$U | 226 | 134 | -49.1114 | 1724.8132 | -1028473.4358 ppm | 212318.9221 | +8425.4004 ppm | 0.0526 ppm |
| ${}^{227}$U | 227 | 135 | -42.5324 | 1731.1682 | -1024568.6145 ppm | 213251.9086 | +8387.1623 ppm | 0.0402 ppm |
| ${}^{228}$U | 228 | 136 | -35.9615 | 1739.0646 | -1020678.6456 ppm | 214184.9031 | +8356.6147 ppm | 0.0634 ppm |
| ${}^{229}$U | 229 | 137 | -29.3986 | 1745.1453 | -1016845.9108 ppm | 215117.9056 | +8317.7899 ppm | 0.0278 ppm |
| ${}^{230}$U | 230 | 138 | -22.8435 | 1752.8122 | -1013032.4910 ppm | 216050.9160 | +8286.8042 ppm | 0.0210 ppm |
| ${}^{231}$U | 231 | 139 | -16.2963 | 1758.6926 | -1009266.1248 ppm | 216983.9342 | +8247.7532 ppm | 0.0124 ppm |
| ${}^{232}$U | 232 | 140 | -9.7568 | 1765.9604 | -1005524.8981 ppm | 217916.9601 | +8215.5472 ppm | 0.0084 ppm |
| ${}^{233}$U | 233 | 141 | -3.2249 | 1771.7221 | -1001820.2020 ppm | 218849.9936 | +8176.6578 ppm | 0.0104 ppm |
| ${}^{234}$U | 234 | 142 | 3.2994 | 1778.5675 | -998144.9183 ppm | 219783.0348 | +8143.1482 ppm | 0.0052 ppm |
| ${}^{235}$U | 235 | 143 | 9.8162 | 1783.8650 | -994497.2501 ppm | 220716.0834 | +8102.8309 ppm | 0.0051 ppm |
| ${}^{236}$U | 236 | 144 | 16.3255 | 1790.4106 | -990881.6967 ppm | 221649.1395 | +8068.6118 ppm | 0.0051 ppm |
| ${}^{237}$U | 237 | 145 | 22.8275 | 1795.5363 | -987286.5342 ppm | 222582.2029 | +8028.2338 ppm | 0.0054 ppm |
| ${}^{238}$U | 238 | 146 | 29.3222 | 1801.6900 | -983725.1783 ppm | 223515.2737 | +7992.9018 ppm | 0.0067 ppm |
| ${}^{239}$U | 239 | 147 | 35.8097 | 1806.4964 | -980177.2872 ppm | 224448.3516 | +7951.7996 ppm | 0.0067 ppm |
| ${}^{240}$U | 240 | 148 | 42.2900 | 1812.4249 | -976666.6275 ppm | 225381.4367 | +7916.1309 ppm | 0.0114 ppm |
| ${}^{241}$U | 241 | 149 | 48.7632 | 1816.8990 | -973161.2873 ppm | 226314.5289 | +7874.7815 ppm | 0.8712 ppm |
| ${}^{242}$U | 242 | 150 | 55.2295 | 1822.7440 | -969699.8257 ppm | 227247.6281 | +7838.5383 ppm | 0.8882 ppm |
| ${}^{243}$U | 243 | 151 | 61.6887 | 1826.8740 | -966232.6227 ppm | 228180.7342 | +7796.2272 ppm | 1.3247 ppm |

### Neptunium (Z = 93)

_27 of 27 isotopes with a framework prediction; 27 of 27 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{219}$Np | 219 | 126 | -119.6821 | 1665.4234 | -1071862.8653 ppm | 205811.7526 | +8749.3813 ppm | 0.4508 ppm |
| ${}^{220}$Np | 220 | 127 | -113.0123 | 1672.4567 | -1067572.6466 ppm | 206744.6482 | +8711.3464 ppm | 0.1499 ppm |
| ${}^{221}$Np | 221 | 128 | -106.3514 | 1681.1470 | -1063261.2050 ppm | 207677.5527 | +8681.5513 ppm | 0.9727 ppm |
| ${}^{222}$Np | 222 | 129 | -99.6992 | 1687.7997 | -1059070.5115 ppm | 208610.4659 | +8642.6586 ppm | 0.1840 ppm |
| ${}^{223}$Np | 223 | 130 | -93.0557 | 1696.4871 | -1054851.9661 ppm | 209543.3878 | +8613.7714 ppm | 0.3988 ppm |
| ${}^{224}$Np | 224 | 131 | -86.4207 | 1703.1847 | -1050740.6381 ppm | 210476.3183 | +8575.5666 ppm | 0.1386 ppm |
| ${}^{225}$Np | 225 | 132 | -79.7942 | 1711.6702 | -1046617.7338 ppm | 211409.2572 | +8546.3441 ppm | 0.4371 ppm |
| ${}^{226}$Np | 226 | 133 | -73.1761 | 1718.5427 | -1042580.3111 ppm | 212342.2045 | +8509.6941 ppm | 0.4847 ppm |
| ${}^{227}$Np | 227 | 134 | -66.5663 | 1726.8519 | -1038547.7706 ppm | 213275.1602 | +8480.2574 ppm | 0.3640 ppm |
| ${}^{228}$Np | 228 | 135 | -59.9647 | 1733.7120 | -1034587.4755 ppm | 214208.1240 | +8444.0713 ppm | 0.4736 ppm |
| ${}^{229}$Np | 229 | 136 | -53.3713 | 1741.7722 | -1030641.9483 ppm | 215141.0960 | +8414.2440 ppm | 0.4742 ppm |
| ${}^{230}$Np | 230 | 137 | -46.7859 | 1748.4083 | -1026759.1536 ppm | 216074.0761 | +8377.8466 ppm | 0.2567 ppm |
| ${}^{231}$Np | 231 | 138 | -40.2085 | 1756.0925 | -1022896.5942 ppm | 217007.0641 | +8346.7130 ppm | 0.2377 ppm |
| ${}^{232}$Np | 232 | 139 | -33.6391 | 1762.5040 | -1019085.9429 ppm | 217940.0600 | +8309.5927 ppm | 0.4611 ppm |
| ${}^{233}$Np | 233 | 140 | -27.0774 | 1769.9103 | -1015298.7338 ppm | 218873.0638 | +8278.1536 ppm | 0.2348 ppm |
| ${}^{234}$Np | 234 | 141 | -20.5235 | 1775.9753 | -1011556.1678 ppm | 219806.0753 | +8240.4648 ppm | 0.0385 ppm |
| ${}^{235}$Np | 235 | 142 | -13.9772 | 1782.9584 | -1007839.3425 ppm | 220739.0945 | +8207.3598 ppm | 0.0063 ppm |
| ${}^{236}$Np | 236 | 143 | -7.4386 | 1788.6947 | -1004158.6583 ppm | 221672.1212 | +8168.8533 ppm | 0.2293 ppm |
| ${}^{237}$Np | 237 | 144 | -0.9074 | 1795.2725 | -1000505.4612 ppm | 222605.1555 | +8134.5487 ppm | 0.0051 ppm |
| ${}^{238}$Np | 238 | 145 | 5.6162 | 1800.7608 | -996881.1852 ppm | 223538.1973 | +8095.6133 ppm | 0.0051 ppm |
| ${}^{239}$Np | 239 | 146 | 12.1325 | 1806.9758 | -993285.7196 ppm | 224471.2464 | +8060.3270 ppm | 0.0059 ppm |
| ${}^{240}$Np | 240 | 147 | 18.6415 | 1812.0418 | -989712.4135 ppm | 225404.3028 | +8020.1891 ppm | 0.0762 ppm |
| ${}^{241}$Np | 241 | 148 | 25.1433 | 1818.1143 | -986170.6740 ppm | 226337.3665 | +7984.9350 ppm | 0.4454 ppm |
| ${}^{242}$Np | 242 | 149 | 31.6379 | 1823.0838 | -982645.9521 ppm | 227270.4373 | +7945.0744 ppm | 0.8870 ppm |
| ${}^{243}$Np | 243 | 150 | 38.1254 | 1828.8180 | -979152.9982 ppm | 228203.5153 | +7908.7482 ppm | 0.1399 ppm |
| ${}^{244}$Np | 244 | 151 | 44.6058 | 1833.4160 | -975670.6462 ppm | 229136.6002 | +7868.1159 ppm | 0.4384 ppm |
| ${}^{245}$Np | 245 | 152 | 51.0793 | 1838.9700 | -972223.9553 ppm | 230069.6922 | +7831.4864 ppm | 0.8773 ppm |

### Plutonium (Z = 94)

_27 of 27 isotopes with a framework prediction; 27 of 27 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{221}$Pu | 221 | 127 | -130.8085 | 1674.2960 | -1078127.4419 ppm | 207701.2275 | +8767.0467 ppm | 1.4568 ppm |
| ${}^{222}$Pu | 222 | 128 | -124.1242 | 1683.2040 | -1073742.7950 ppm | 208634.1086 | +8738.5117 ppm | 1.4502 ppm |
| ${}^{223}$Pu | 223 | 129 | -117.4487 | 1690.3400 | -1069482.3025 ppm | 209566.9986 | +8700.8997 ppm | 1.4437 ppm |
| ${}^{224}$Pu | 224 | 130 | -110.7820 | 1699.2640 | -1065194.1169 ppm | 210499.8973 | +8672.8548 ppm | 1.4373 ppm |
| ${}^{225}$Pu | 225 | 131 | -104.1240 | 1706.1750 | -1061027.7258 ppm | 211432.8047 | +8636.1494 ppm | 1.4309 ppm |
| ${}^{226}$Pu | 226 | 132 | -97.4745 | 1714.8880 | -1056840.1667 ppm | 212365.7206 | +8607.9086 ppm | 0.9512 ppm |
| ${}^{227}$Pu | 227 | 133 | -90.8335 | 1721.7950 | -1052755.1471 ppm | 213298.6451 | +8571.3207 ppm | 0.4713 ppm |
| ${}^{228}$Pu | 228 | 134 | -84.2010 | 1730.6121 | -1048653.8727 ppm | 214231.5779 | +8543.6500 ppm | 0.1099 ppm |
| ${}^{229}$Pu | 229 | 135 | -77.5767 | 1737.3963 | -1044651.1432 ppm | 215164.5191 | +8507.0462 ppm | 0.2842 ppm |
| ${}^{230}$Pu | 230 | 136 | -70.9607 | 1745.9304 | -1040643.4980 ppm | 216097.4685 | +8479.0350 ppm | 0.0674 ppm |
| ${}^{231}$Pu | 231 | 137 | -64.3529 | 1752.6253 | -1036717.9789 ppm | 217030.4261 | +8442.6860 ppm | 0.1025 ppm |
| ${}^{232}$Pu | 232 | 138 | -57.7531 | 1760.6443 | -1032802.2375 ppm | 217963.3917 | +8412.8654 ppm | 0.0781 ppm |
| ${}^{233}$Pu | 233 | 139 | -51.1613 | 1767.0247 | -1028953.3472 ppm | 218896.3654 | +8375.7260 ppm | 0.2496 ppm |
| ${}^{234}$Pu | 234 | 140 | -44.5774 | 1774.7978 | -1025116.8892 ppm | 219829.3469 | +8345.3827 ppm | 0.0312 ppm |
| ${}^{235}$Pu | 235 | 141 | -38.0014 | 1781.0368 | -1021336.6509 ppm | 220762.3363 | +8308.2679 ppm | 0.0937 ppm |
| ${}^{236}$Pu | 236 | 142 | -31.4331 | 1788.3889 | -1017576.1996 ppm | 221695.3334 | +8276.6081 ppm | 0.0082 ppm |
| ${}^{237}$Pu | 237 | 143 | -24.8725 | 1794.2701 | -1013862.1759 ppm | 222628.3383 | +8238.5338 ppm | 0.0077 ppm |
| ${}^{238}$Pu | 238 | 144 | -18.3195 | 1801.2699 | -1010170.3281 ppm | 223561.3507 | +8205.9007 ppm | 0.0051 ppm |
| ${}^{239}$Pu | 239 | 145 | -11.7741 | 1806.9162 | -1006516.1095 ppm | 224494.3707 | +8167.4464 ppm | 0.0050 ppm |
| ${}^{240}$Pu | 240 | 146 | -5.2361 | 1813.4504 | -1002887.3616 ppm | 225427.3981 | +8133.3500 ppm | 0.0049 ppm |
| ${}^{241}$Pu | 241 | 147 | 1.2945 | 1818.6919 | -999288.2279 ppm | 226360.4330 | +8093.7663 ppm | 0.0049 ppm |
| ${}^{242}$Pu | 242 | 148 | 7.8178 | 1825.0015 | -995716.3045 ppm | 227293.4751 | +8059.3181 ppm | 0.0055 ppm |
| ${}^{243}$Pu | 243 | 149 | 14.3338 | 1830.0351 | -992167.4992 ppm | 228226.5245 | +8019.5053 ppm | 0.0112 ppm |
| ${}^{244}$Pu | 244 | 150 | 20.8426 | 1836.0550 | -988648.1802 ppm | 229159.5812 | +7984.4240 ppm | 0.0103 ppm |
| ${}^{245}$Pu | 245 | 151 | 27.3443 | 1840.7541 | -985145.0781 ppm | 230092.6449 | +7943.8295 ppm | 0.0597 ppm |
| ${}^{246}$Pu | 246 | 152 | 33.8389 | 1846.6089 | -981675.1126 ppm | 231025.7157 | +7908.6780 ppm | 0.0654 ppm |
| ${}^{247}$Pu | 247 | 153 | 40.3266 | 1850.7710 | -978210.9442 ppm | 231958.7934 | +7866.8414 ppm | 0.8702 ppm |

### Americium (Z = 95)

_27 of 27 isotopes with a framework prediction; 27 of 27 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{223}$Am | 223 | 128 | -142.0765 | 1682.9810 | -1084419.5537 ppm | 209590.8440 | +8783.7288 ppm | 1.4436 ppm |
| ${}^{224}$Am | 224 | 129 | -135.3777 | 1690.3040 | -1080090.7631 ppm | 210523.7107 | +8748.3901 ppm | 1.9148 ppm |
| ${}^{225}$Am | 225 | 130 | -128.6878 | 1699.4250 | -1075724.3302 ppm | 211456.5862 | +8720.2926 ppm | 1.9063 ppm |
| ${}^{226}$Am | 226 | 131 | -122.0067 | 1706.7520 | -1071484.7048 ppm | 212389.4704 | +8685.5416 ppm | 1.4245 ppm |
| ${}^{227}$Am | 227 | 132 | -115.3342 | 1715.6660 | -1067224.1437 ppm | 213322.3634 | +8657.6685 ppm | 0.9469 ppm |
| ${}^{228}$Am | 228 | 133 | -108.6703 | 1722.9960 | -1063070.5335 ppm | 214255.2649 | +8623.1493 ppm | 0.9428 ppm |
| ${}^{229}$Am | 229 | 134 | -102.0149 | 1731.8285 | -1058905.8771 ppm | 215188.1749 | +8595.3013 ppm | 0.4985 ppm |
| ${}^{230}$Am | 230 | 135 | -95.3679 | 1739.2600 | -1054832.4490 ppm | 216121.0934 | +8561.3296 ppm | 0.6651 ppm |
| ${}^{231}$Am | 231 | 136 | -88.7292 | 1747.7460 | -1050767.8037 ppm | 217054.0201 | +8533.0968 ppm | 1.3937 ppm |
| ${}^{232}$Am | 232 | 137 | -82.0988 | 1754.8480 | -1046784.0027 ppm | 217986.9551 | +8498.2785 ppm | 1.3877 ppm |
| ${}^{233}$Am | 233 | 138 | -75.4766 | 1763.1110 | -1042808.7438 ppm | 218919.8983 | +8469.1152 ppm | 0.5278 ppm |
| ${}^{234}$Am | 234 | 139 | -68.8624 | 1769.9760 | -1038905.8417 ppm | 219852.8496 | +8434.1715 ppm | 0.7349 ppm |
| ${}^{235}$Am | 235 | 140 | -62.2563 | 1777.8122 | -1035018.4641 ppm | 220785.8088 | +8404.2278 ppm | 0.2411 ppm |
| ${}^{236}$Am | 236 | 141 | -55.6580 | 1784.3960 | -1031191.5214 ppm | 221718.7760 | +8368.8280 ppm | 0.5380 ppm |
| ${}^{237}$Am | 237 | 142 | -49.0677 | 1791.9570 | -1027382.1593 ppm | 222651.7511 | +8337.8146 ppm | 0.2700 ppm |
| ${}^{238}$Am | 238 | 143 | -42.4851 | 1798.2293 | -1023626.0491 ppm | 223584.7339 | +8301.0844 ppm | 0.2657 ppm |
| ${}^{239}$Am | 239 | 144 | -35.9102 | 1805.3317 | -1019891.1684 ppm | 224517.7244 | +8268.6922 ppm | 0.0089 ppm |
| ${}^{240}$Am | 240 | 145 | -29.3429 | 1811.2833 | -1016200.0541 ppm | 225450.7226 | +8231.4154 ppm | 0.0619 ppm |
| ${}^{241}$Am | 241 | 146 | -22.7832 | 1817.9304 | -1012532.4777 ppm | 226383.7283 | +8197.6051 ppm | 0.0050 ppm |
| ${}^{242}$Am | 242 | 147 | -16.2309 | 1823.4680 | -1008901.1374 ppm | 227316.7415 | +8159.1472 ppm | 0.0050 ppm |
| ${}^{243}$Am | 243 | 148 | -9.6861 | 1829.8323 | -1005293.4460 ppm | 228249.7621 | +8124.7202 ppm | 0.0061 ppm |
| ${}^{244}$Am | 244 | 149 | -3.1486 | 1835.1995 | -1001715.6937 ppm | 229182.7900 | +8086.1867 ppm | 0.0066 ppm |
| ${}^{245}$Am | 245 | 150 | 3.3816 | 1841.2496 | -998163.4403 ppm | 230115.8252 | +8051.0158 ppm | 0.0083 ppm |
| ${}^{246}$Am | 246 | 151 | 9.9046 | 1846.2300 | -994635.2488 ppm | 231048.8677 | +8011.4467 ppm | 0.0772 ppm |
| ${}^{247}$Am | 247 | 152 | 16.4204 | 1852.2530 | -991134.8902 ppm | 231981.9172 | +7976.3227 ppm | 0.4331 ppm |
| ${}^{248}$Am | 248 | 153 | 22.9292 | 1856.7760 | -987651.0598 ppm | 232914.9739 | +7936.0605 ppm | 0.8667 ppm |
| ${}^{249}$Am | 249 | 154 | 29.4310 | 1862.2710 | -984196.1783 ppm | 233848.0375 | +7899.9244 ppm | 1.2847 ppm |

### Curium (Z = 96)

_22 of 22 isotopes with a framework prediction; 22 of 22 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{231}$Cm | 231 | 135 | -113.3376 | 1742.2020 | -1065054.2483 ppm | 217077.8462 | +8621.0291 ppm | 1.3936 ppm |
| ${}^{232}$Cm | 232 | 136 | -106.6763 | 1751.1360 | -1060918.3279 ppm | 218010.7503 | +8594.7731 ppm | 0.9308 ppm |
| ${}^{233}$Cm | 233 | 137 | -100.0233 | 1758.2185 | -1056888.9785 ppm | 218943.6627 | +8559.9630 ppm | 0.3736 ppm |
| ${}^{234}$Cm | 234 | 138 | -93.3785 | 1766.8607 | -1052849.9420 ppm | 219876.5833 | +8532.5742 ppm | 0.0783 ppm |
| ${}^{235}$Cm | 235 | 139 | -86.7419 | 1773.5450 | -1048908.7658 ppm | 220809.5121 | +8496.8774 ppm | 0.4680 ppm |
| ${}^{236}$Cm | 236 | 140 | -80.1134 | 1781.8729 | -1044960.2239 ppm | 221742.4491 | +8468.1821 ppm | 0.0802 ppm |
| ${}^{237}$Cm | 237 | 141 | -73.4929 | 1788.5499 | -1041090.7925 ppm | 222675.3940 | +8432.6618 ppm | 0.3369 ppm |
| ${}^{238}$Cm | 238 | 142 | -66.8804 | 1796.4232 | -1037229.7592 ppm | 223608.3469 | +8402.9163 ppm | 0.0552 ppm |
| ${}^{239}$Cm | 239 | 143 | -60.2757 | 1802.7928 | -1033434.6461 ppm | 224541.3077 | +8366.6457 ppm | 0.6739 ppm |
| ${}^{240}$Cm | 240 | 144 | -53.6789 | 1810.2868 | -1029652.1313 ppm | 225474.2762 | +8335.7834 ppm | 0.0085 ppm |
| ${}^{241}$Cm | 241 | 145 | -47.0897 | 1816.3806 | -1025925.0201 ppm | 226407.2525 | +8298.9238 ppm | 0.0072 ppm |
| ${}^{242}$Cm | 242 | 146 | -40.5082 | 1823.3500 | -1022216.3523 ppm | 227340.2364 | +8266.3187 ppm | 0.0051 ppm |
| ${}^{243}$Cm | 243 | 147 | -33.9342 | 1829.0430 | -1018553.0014 ppm | 228273.2279 | +8228.3321 ppm | 0.0066 ppm |
| ${}^{244}$Cm | 244 | 148 | -27.3678 | 1835.8445 | -1014907.4664 ppm | 229206.2268 | +8195.6057 ppm | 0.0049 ppm |
| ${}^{245}$Cm | 245 | 149 | -20.8088 | 1841.3631 | -1011300.7422 ppm | 230139.2332 | +8157.5140 ppm | 0.0050 ppm |
| ${}^{246}$Cm | 246 | 150 | -14.2571 | 1847.8220 | -1007715.6286 ppm | 231072.2470 | +8123.9005 ppm | 0.0067 ppm |
| ${}^{247}$Cm | 247 | 151 | -7.7127 | 1852.9772 | -1004162.3490 ppm | 232005.2681 | +8084.8802 ppm | 0.0165 ppm |
| ${}^{248}$Cm | 248 | 152 | -1.1756 | 1859.1888 | -1000632.3133 ppm | 232938.2963 | +8050.8158 ppm | 0.0102 ppm |
| ${}^{249}$Cm | 249 | 153 | 5.3544 | 1863.9022 | -997127.3160 ppm | 233871.3318 | +8010.5468 ppm | 0.0102 ppm |
| ${}^{250}$Cm | 250 | 154 | 11.8773 | 1869.7346 | -993647.5993 ppm | 234804.3743 | +7975.4735 ppm | 0.0441 ppm |
| ${}^{251}$Cm | 251 | 155 | 18.3932 | 1874.1475 | -990185.8422 ppm | 235737.4238 | +7934.5929 ppm | 0.0970 ppm |
| ${}^{252}$Cm | 252 | 156 | 24.9021 | 1879.9200 | -986753.6413 ppm | 236670.4803 | +7899.4349 ppm | 1.2694 ppm |

### Berkelium (Z = 97)

_22 of 22 isotopes with a framework prediction; 22 of 22 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{233}$Bk | 233 | 136 | -124.8013 | 1751.9270 | -1071236.6070 ppm | 218967.6584 | +8645.0480 ppm | 1.0727 ppm |
| ${}^{234}$Bk | 234 | 137 | -118.1256 | 1759.4460 | -1067137.9744 ppm | 219900.5481 | +8611.6264 ppm | 0.7007 ppm |
| ${}^{235}$Bk | 235 | 138 | -111.4583 | 1768.1400 | -1063037.0309 ppm | 220833.4462 | +8584.2814 ppm | 1.8293 ppm |
| ${}^{236}$Bk | 236 | 139 | -104.7992 | 1775.4280 | -1059027.5807 ppm | 221766.3526 | +8550.8011 ppm | 1.6394 ppm |
| ${}^{237}$Bk | 237 | 140 | -98.1483 | 1783.8990 | -1055018.9959 ppm | 222699.2671 | +8522.6776 ppm | 1.0419 ppm |
| ${}^{238}$Bk | 238 | 141 | -91.5056 | 1790.9500 | -1051093.3042 ppm | 223632.1897 | +8488.7394 ppm | 1.1552 ppm |
| ${}^{239}$Bk | 239 | 142 | -84.8708 | 1798.9530 | -1047177.8896 ppm | 224565.1204 | +8459.5339 ppm | 0.9286 ppm |
| ${}^{240}$Bk | 240 | 143 | -78.2440 | 1805.5200 | -1043335.9991 ppm | 225498.0590 | +8424.3734 ppm | 0.6707 ppm |
| ${}^{241}$Bk | 241 | 144 | -71.6251 | 1813.2840 | -1039500.2100 ppm | 226431.0055 | +8394.4720 ppm | 0.7384 ppm |
| ${}^{242}$Bk | 242 | 145 | -65.0140 | 1819.5980 | -1035729.8634 ppm | 227363.9599 | +8358.3498 ppm | 0.5949 ppm |
| ${}^{243}$Bk | 243 | 146 | -58.4106 | 1826.7530 | -1031975.0983 ppm | 228296.9219 | +8326.2685 ppm | 0.0200 ppm |
| ${}^{244}$Bk | 244 | 147 | -51.8149 | 1832.8001 | -1028270.8859 ppm | 229229.8916 | +8289.6663 ppm | 0.0633 ppm |
| ${}^{245}$Bk | 245 | 148 | -45.2267 | 1839.7715 | -1024582.8052 ppm | 230162.8689 | +8257.4789 ppm | 0.0078 ppm |
| ${}^{246}$Bk | 246 | 149 | -38.6461 | 1845.6897 | -1020938.5794 ppm | 231095.8537 | +8220.9537 ppm | 0.2618 ppm |
| ${}^{247}$Bk | 247 | 150 | -32.0729 | 1852.2384 | -1017315.7729 ppm | 232028.8459 | +8187.5192 ppm | 0.0225 ppm |
| ${}^{248}$Bk | 248 | 151 | -25.5071 | 1857.6682 | -1013730.7266 ppm | 232961.8455 | +8149.5050 ppm | 0.2166 ppm |
| ${}^{249}$Bk | 249 | 152 | -18.9486 | 1864.0242 | -1010165.4451 ppm | 233894.8525 | +8115.8531 ppm | 0.0054 ppm |
| ${}^{250}$Bk | 250 | 153 | -12.3974 | 1868.9898 | -1006633.1969 ppm | 234827.8666 | +8076.4848 ppm | 0.0124 ppm |
| ${}^{251}$Bk | 251 | 154 | -5.8533 | 1874.7852 | -1003122.1140 ppm | 235760.8880 | +8041.0380 ppm | 0.0459 ppm |
| ${}^{252}$Bk | 252 | 155 | 0.6837 | 1879.6680 | -999636.2744 ppm | 236693.9164 | +8001.4804 ppm | 0.8529 ppm |
| ${}^{253}$Bk | 253 | 156 | 7.2136 | 1885.1030 | -996173.3569 ppm | 237626.9519 | +7966.1673 ppm | 1.5212 ppm |
| ${}^{254}$Bk | 254 | 157 | 13.7366 | 1889.7600 | -992731.0506 ppm | 238559.9944 | +7926.6004 ppm | 1.2594 ppm |

### Californium (Z = 98)

_20 of 20 isotopes with a framework prediction; 20 of 20 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{237}$Cf | 237 | 139 | -123.0338 | 1778.2941 | -1069186.4446 ppm | 222723.3703 | +8610.2340 ppm | 0.4408 ppm |
| ${}^{238}$Cf | 238 | 140 | -116.3605 | 1787.1420 | -1065109.8263 ppm | 223656.2624 | +8583.3751 ppm | 1.3442 ppm |
| ${}^{239}$Cf | 239 | 141 | -109.6954 | 1794.1730 | -1061139.7910 ppm | 224589.1626 | +8549.6002 ppm | 0.5396 ppm |
| ${}^{240}$Cf | 240 | 142 | -103.0383 | 1802.4576 | -1057165.4721 ppm | 225522.0710 | +8521.2710 ppm | 0.0806 ppm |
| ${}^{241}$Cf | 241 | 143 | -96.3894 | 1809.1870 | -1053277.7209 ppm | 226454.9875 | +8486.2465 ppm | 0.7467 ppm |
| ${}^{242}$Cf | 242 | 144 | -89.7483 | 1817.2020 | -1049388.2066 ppm | 227387.9119 | +8457.2631 ppm | 0.0572 ppm |
| ${}^{243}$Cf | 243 | 145 | -83.1152 | 1823.7150 | -1045574.6787 ppm | 228320.8442 | +8421.6830 ppm | 0.7981 ppm |
| ${}^{244}$Cf | 244 | 146 | -76.4899 | 1831.2535 | -1041769.1599 ppm | 229253.7843 | +8391.3707 ppm | 0.0115 ppm |
| ${}^{245}$Cf | 245 | 147 | -69.8724 | 1837.4178 | -1038027.4752 ppm | 230186.7322 | +8355.0739 ppm | 0.0106 ppm |
| ${}^{246}$Cf | 246 | 148 | -63.2625 | 1844.7840 | -1034292.6154 ppm | 231119.6877 | +8324.3938 ppm | 0.0066 ppm |
| ${}^{247}$Cf | 247 | 149 | -56.6602 | 1850.8362 | -1030613.2867 ppm | 232052.6508 | +8288.2381 ppm | 0.0622 ppm |
| ${}^{248}$Cf | 248 | 150 | -50.0654 | 1857.7789 | -1026949.0714 ppm | 232985.6215 | +8256.2930 ppm | 0.0222 ppm |
| ${}^{249}$Cf | 249 | 151 | -43.4781 | 1863.3655 | -1023333.1120 ppm | 233918.5996 | +8218.7433 ppm | 0.0051 ppm |
| ${}^{250}$Cf | 250 | 152 | -36.8982 | 1869.9892 | -1019731.7743 ppm | 234851.5851 | +8186.0154 ppm | 0.0066 ppm |
| ${}^{251}$Cf | 251 | 153 | -30.3256 | 1875.0959 | -1016172.8357 ppm | 235784.5780 | +8147.0405 ppm | 0.0167 ppm |
| ${}^{252}$Cf | 252 | 154 | -23.7603 | 1881.2675 | -1012629.9347 ppm | 236717.5781 | +8112.9791 ppm | 0.0100 ppm |
| ${}^{253}$Cf | 253 | 155 | -17.2021 | 1886.0719 | -1009120.6205 ppm | 237650.5853 | +8073.3712 ppm | 0.0181 ppm |
| ${}^{254}$Cf | 254 | 156 | -10.6511 | 1892.1034 | -1005629.2544 ppm | 238583.5997 | +8039.3325 ppm | 0.0484 ppm |
| ${}^{255}$Cf | 255 | 157 | -4.1072 | 1896.6900 | -1002165.4449 ppm | 239516.6212 | +7999.5350 ppm | 0.8428 ppm |
| ${}^{256}$Cf | 256 | 158 | 2.4298 | 1902.5920 | -998722.9115 ppm | 240449.6497 | +7965.2995 ppm | 1.3198 ppm |

### Einsteinium (Z = 99)

_20 of 20 isotopes with a framework prediction; 20 of 20 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding $B_o$ (MeV) | Binding Error (ppm) | $M_{\mathrm{atom}}$ (MeV) | $M_{\mathrm{atom}}$ Error (pred) | $M_{\mathrm{atom}}$ Error (exp) |
|---|---|---|---|---|---|---|---|---|
| ${}^{239}$Es | 239 | 140 | -134.7494 | 1787.9590 | -1075364.9306 ppm | 224613.4343 | +8634.0068 ppm | 1.3469 ppm |
| ${}^{240}$Es | 240 | 141 | -128.0618 | 1795.4400 | -1071326.1605 ppm | 225546.3122 | +8601.5452 ppm | 1.6370 ppm |
| ${}^{241}$Es | 241 | 142 | -121.3825 | 1803.8850 | -1067289.4816 ppm | 226479.1983 | +8573.5568 ppm | 1.0288 ppm |
| ${}^{242}$Es | 242 | 143 | -114.7113 | 1810.8860 | -1063345.3804 ppm | 227412.0925 | +8540.2860 ppm | 1.1402 ppm |
| ${}^{243}$Es | 243 | 144 | -108.0481 | 1819.0980 | -1059396.5212 ppm | 228344.9947 | +8511.6149 ppm | 0.9133 ppm |
| ${}^{244}$Es | 244 | 145 | -101.3929 | 1825.8520 | -1055531.8293 ppm | 229277.9050 | +8477.2968 ppm | 0.7989 ppm |
| ${}^{245}$Es | 245 | 146 | -94.7456 | 1833.8250 | -1051665.5700 ppm | 230210.8231 | +8447.6639 ppm | 0.7263 ppm |
| ${}^{246}$Es | 246 | 147 | -88.1062 | 1840.2731 | -1047876.6747 ppm | 231143.7491 | +8412.9644 ppm | 0.3923 ppm |
| ${}^{247}$Es | 247 | 148 | -81.4745 | 1847.5848 | -1044097.8154 ppm | 232076.6828 | +8381.8409 ppm | 0.0845 ppm |
| ${}^{248}$Es | 248 | 149 | -74.8504 | 1854.0480 | -1040371.3593 ppm | 233009.6242 | +8346.8087 ppm | 0.2257 ppm |
| ${}^{249}$Es | 249 | 150 | -68.2340 | 1861.0260 | -1036664.7404 ppm | 233942.5732 | +8315.7630 ppm | 0.1285 ppm |
| ${}^{250}$Es | 250 | 151 | -61.6252 | 1867.2500 | -1033003.1738 ppm | 234875.5298 | +8279.9101 ppm | 0.4279 ppm |
| ${}^{251}$Es | 251 | 152 | -55.0238 | 1873.9369 | -1029362.6702 ppm | 235808.4938 | +8247.6744 ppm | 0.0226 ppm |
| ${}^{252}$Es | 252 | 153 | -48.4298 | 1879.2252 | -1025771.1608 ppm | 236741.4652 | +8209.2979 ppm | 0.2132 ppm |
| ${}^{253}$Es | 253 | 154 | -41.8432 | 1885.5806 | -1022191.1357 ppm | 237674.4440 | +8175.8205 ppm | 0.0053 ppm |
| ${}^{254}$Es | 254 | 155 | -35.2638 | 1890.6683 | -1018651.5055 ppm | 238607.4301 | +8137.2377 ppm | 0.0124 ppm |
| ${}^{255}$Es | 255 | 156 | -28.6917 | 1896.6445 | -1015127.5850 ppm | 239540.4234 | +8102.7585 ppm | 0.0455 ppm |
| ${}^{256}$Es | 256 | 157 | -22.1266 | 1901.5680 | -1011635.9943 ppm | 240473.4238 | +8064.3503 ppm | 0.4178 ppm |
| ${}^{257}$Es | 257 | 158 | -15.5687 | 1907.4540 | -1008162.0297 ppm | 241406.4312 | +8029.9629 ppm | 1.7153 ppm |
| ${}^{258}$Es | 258 | 159 | -9.0178 | 1912.2960 | -1004715.6785 ppm | 242339.4457 | +7991.3453 ppm | 1.6660 ppm |

<!-- AUTO:per-z-sections END -->
