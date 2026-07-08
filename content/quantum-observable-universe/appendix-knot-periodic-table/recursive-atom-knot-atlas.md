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

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| $\mathfrak{n}$ | 1 | 1 | — | — | 939.5654 | +1.04 | 0.47 |

### Hydrogen (Z = 1)

_2 of 7 isotopes with a framework prediction; 3 of 7 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| $\mathfrak{p}$ | 1 | 0 | — | — | 938.7831 | +14.47 | 0.01 |
| ${}^{2}$H | 2 | 1 | 2.2488 | +10903067.24 | 1876.0997 | -12920.26 | 0.01 |
| ${}^{3}$H | 3 | 2 | 8.4686 | -1556016.34 | 2809.4453 | +4703.24 | 0.03 |
| ${}^{4}$H | 4 | 3 | — | — | — | — | 26662.32 |
| ${}^{5}$H | 5 | 4 | — | — | — | — | 19069.33 |
| ${}^{6}$H | 6 | 5 | — | — | — | — | 45131.18 |
| ${}^{7}$H | 7 | 6 | — | — | — | — | 152848.20 |

### Helium (Z = 2)

_2 of 8 isotopes with a framework prediction; 2 of 8 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{3}$He | 3 | 1 | 7.4889 | -29686548.79 | 2809.6427 | +81565.12 | 0.02 |
| ${}^{4}$He | 4 | 2 | 28.2957 | +409.96 | 3728.4013 | +4.70 | 0.04 |
| ${}^{5}$He | 5 | 3 | — | — | — | — | 4283.67 |
| ${}^{6}$He | 6 | 4 | — | — | — | — | 9.47 |
| ${}^{7}$He | 7 | 5 | — | — | — | — | 1154.67 |
| ${}^{8}$He | 8 | 6 | — | — | — | — | 11.82 |
| ${}^{9}$He | 9 | 7 | — | — | — | — | 5557.20 |
| ${}^{10}$He | 10 | 8 | — | — | — | — | 9915.23 |

### Lithium (Z = 3)

_2 of 11 isotopes with a framework prediction; 0 of 11 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{3}$Li | 3 | 0 | — | — | — | — | 708399.67 |
| ${}^{4}$Li | 4 | 1 | — | — | — | — | 56548.92 |
| ${}^{5}$Li | 5 | 2 | — | — | — | — | 10708.55 |
| ${}^{6}$Li | 6 | 3 | 43.6570 | +364537826.40 | — | — | 0.26 |
| ${}^{7}$Li | 7 | 4 | 51.3377 | +308130107.32 | — | — | 0.64 |
| ${}^{8}$Li | 8 | 5 | — | — | — | — | 6.23 |
| ${}^{9}$Li | 9 | 6 | — | — | — | — | 22.16 |
| ${}^{10}$Li | 10 | 7 | — | — | — | — | 1360.77 |
| ${}^{11}$Li | 11 | 8 | — | — | — | — | 59.76 |
| ${}^{12}$Li | 12 | 9 | — | — | — | — | 2672.70 |
| ${}^{13}$Li | 13 | 10 | — | — | — | — | 5753.70 |

### Beryllium (Z = 4)

_3 of 12 isotopes with a framework prediction; 1 of 12 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{5}$Be | 5 | 1 | — | — | — | — | 426598.31 |
| ${}^{6}$Be | 6 | 2 | — | — | — | — | 971.47 |
| ${}^{7}$Be | 7 | 3 | — | — | — | — | 10.83 |
| ${}^{8}$Be | 8 | 4 | 62.3383 | +103343584.23 | 7451.0557 | -783006.99 | 4.62 |
| ${}^{9}$Be | 9 | 5 | 67.3058 | +157171503.52 | — | — | 9.10 |
| ${}^{10}$Be | 10 | 6 | 75.5932 | +163395838.59 | — | — | 8.59 |
| ${}^{11}$Be | 11 | 7 | — | — | — | — | 23.14 |
| ${}^{12}$Be | 12 | 8 | — | — | — | — | 170.28 |
| ${}^{13}$Be | 13 | 9 | — | — | — | — | 838.36 |
| ${}^{14}$Be | 14 | 10 | — | — | — | — | 10109.74 |
| ${}^{15}$Be | 15 | 11 | — | — | — | — | 11823.84 |
| ${}^{16}$Be | 16 | 12 | — | — | — | — | 11081.66 |

### Boron (Z = 5)

_2 of 16 isotopes with a framework prediction; 0 of 16 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{6}$B | 6 | 1 | — | — | — | — | 355324.92 |
| ${}^{7}$B | 7 | 2 | — | — | — | — | 3840.84 |
| ${}^{8}$B | 8 | 3 | — | — | — | — | 133.71 |
| ${}^{9}$B | 9 | 4 | — | — | — | — | 107.51 |
| ${}^{10}$B | 10 | 5 | 75.5932 | +167446937.29 | — | — | 1.60 |
| ${}^{11}$B | 11 | 6 | 83.8806 | +100721952.49 | — | — | 1.18 |
| ${}^{12}$B | 12 | 7 | — | — | — | — | 118.03 |
| ${}^{13}$B | 13 | 8 | — | — | — | — | 82.43 |
| ${}^{14}$B | 14 | 9 | — | — | — | — | 1623.70 |
| ${}^{15}$B | 15 | 10 | — | — | — | — | 1501.89 |
| ${}^{16}$B | 16 | 11 | — | — | — | — | 1644.22 |
| ${}^{17}$B | 17 | 12 | — | — | — | — | 12853.57 |
| ${}^{18}$B | 18 | 13 | — | — | — | — | 12139.17 |
| ${}^{19}$B | 19 | 14 | — | — | — | — | 29584.30 |
| ${}^{20}$B | 20 | 15 | — | — | — | — | 29218.05 |
| ${}^{21}$B | 21 | 16 | — | — | — | — | 28445.54 |

### Carbon (Z = 6)

_2 of 16 isotopes with a framework prediction; 1 of 16 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{8}$C | 8 | 2 | — | — | — | — | 2436.54 |
| ${}^{9}$C | 9 | 3 | — | — | — | — | 253.90 |
| ${}^{10}$C | 10 | 4 | — | — | — | — | 7.49 |
| ${}^{11}$C | 11 | 5 | — | — | — | — | 5.81 |
| ${}^{12}$C | 12 | 6 | 97.1480 | +54103421.00 | 11172.9431 | -446073.51 | 0.00 |
| ${}^{13}$C | 13 | 7 | 101.0622 | +40718641.80 | — | — | 0.02 |
| ${}^{14}$C | 14 | 8 | — | — | — | — | 0.29 |
| ${}^{15}$C | 15 | 9 | — | — | — | — | 57.16 |
| ${}^{16}$C | 16 | 10 | — | — | — | — | 239.78 |
| ${}^{17}$C | 17 | 11 | — | — | — | — | 1095.07 |
| ${}^{18}$C | 18 | 12 | — | — | — | — | 1786.57 |
| ${}^{19}$C | 19 | 13 | — | — | — | — | 5549.05 |
| ${}^{20}$C | 20 | 14 | — | — | — | — | 12354.38 |
| ${}^{21}$C | 21 | 15 | — | — | — | — | 30405.24 |
| ${}^{22}$C | 22 | 16 | — | — | — | — | 11266.66 |
| ${}^{23}$C | 23 | 17 | — | — | — | — | 46382.81 |

### Nitrogen (Z = 7)

_2 of 16 isotopes with a framework prediction; 0 of 16 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{10}$N | 10 | 3 | — | — | — | — | 42763.57 |
| ${}^{11}$N | 11 | 4 | — | — | — | — | 486.84 |
| ${}^{12}$N | 12 | 5 | — | — | — | — | 89.28 |
| ${}^{13}$N | 13 | 6 | — | — | — | — | 22.22 |
| ${}^{14}$N | 14 | 7 | 109.9563 | +50618909.51 | — | — | 0.02 |
| ${}^{15}$N | 15 | 8 | 118.8505 | +29080548.19 | — | — | 0.04 |
| ${}^{16}$N | 16 | 9 | — | — | — | — | 154.32 |
| ${}^{17}$N | 17 | 10 | — | — | — | — | 946.76 |
| ${}^{18}$N | 18 | 11 | — | — | — | — | 1106.63 |
| ${}^{19}$N | 19 | 12 | — | — | — | — | 926.01 |
| ${}^{20}$N | 20 | 13 | — | — | — | — | 4229.86 |
| ${}^{21}$N | 21 | 14 | — | — | — | — | 6843.84 |
| ${}^{22}$N | 22 | 15 | — | — | — | — | 10123.40 |
| ${}^{23}$N | 23 | 16 | — | — | — | — | 19596.85 |
| ${}^{24}$N | 24 | 17 | — | — | — | — | 17879.13 |
| ${}^{25}$N | 25 | 18 | — | — | — | — | 21548.20 |

### Oxygen (Z = 8)

_3 of 18 isotopes with a framework prediction; 1 of 18 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{11}$O | 11 | 3 | — | — | — | — | 5832.19 |
| ${}^{12}$O | 12 | 4 | — | — | — | — | 1070.43 |
| ${}^{13}$O | 13 | 5 | — | — | — | — | 785.12 |
| ${}^{14}$O | 14 | 6 | — | — | — | — | 1.93 |
| ${}^{15}$O | 15 | 7 | — | — | — | — | 35.06 |
| ${}^{16}$O | 16 | 8 | 134.3846 | +53011810.55 | 14892.4034 | -454066.57 | 0.02 |
| ${}^{17}$O | 17 | 9 | 137.2455 | +41613894.00 | — | — | 0.04 |
| ${}^{18}$O | 18 | 10 | 146.7464 | +49630170.33 | — | — | 0.04 |
| ${}^{19}$O | 19 | 11 | — | — | — | — | 148.92 |
| ${}^{20}$O | 20 | 12 | — | — | — | — | 47.49 |
| ${}^{21}$O | 21 | 13 | — | — | — | — | 613.18 |
| ${}^{22}$O | 22 | 14 | — | — | — | — | 2776.33 |
| ${}^{23}$O | 23 | 15 | — | — | — | — | 5677.13 |
| ${}^{24}$O | 24 | 16 | — | — | — | — | 7368.90 |
| ${}^{25}$O | 25 | 17 | — | — | — | — | 7080.69 |
| ${}^{26}$O | 26 | 18 | — | — | — | — | 6801.07 |
| ${}^{27}$O | 27 | 19 | — | — | — | — | 19853.63 |
| ${}^{28}$O | 28 | 20 | — | — | — | — | 26732.34 |

### Fluorine (Z = 9)

_1 of 19 isotopes with a framework prediction; 0 of 19 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{13}$F | 13 | 4 | — | — | — | — | 41164.82 |
| ${}^{14}$F | 14 | 5 | — | — | — | — | 3145.29 |
| ${}^{15}$F | 15 | 6 | — | — | — | — | 1000.75 |
| ${}^{16}$F | 16 | 7 | — | — | — | — | 359.62 |
| ${}^{17}$F | 17 | 8 | — | — | — | — | 15.65 |
| ${}^{18}$F | 18 | 9 | — | — | — | — | 27.61 |
| ${}^{19}$F | 19 | 10 | 156.2474 | +57144210.04 | — | — | 0.05 |
| ${}^{20}$F | 20 | 11 | — | — | — | — | 1.55 |
| ${}^{21}$F | 21 | 12 | — | — | — | — | 92.00 |
| ${}^{22}$F | 22 | 13 | — | — | — | — | 604.92 |
| ${}^{23}$F | 23 | 14 | — | — | — | — | 1554.98 |
| ${}^{24}$F | 24 | 15 | — | — | — | — | 4367.40 |
| ${}^{25}$F | 25 | 16 | — | — | — | — | 4139.39 |
| ${}^{26}$F | 26 | 17 | — | — | — | — | 4415.75 |
| ${}^{27}$F | 27 | 18 | — | — | — | — | 4774.38 |
| ${}^{28}$F | 28 | 19 | — | — | — | — | 4608.31 |
| ${}^{29}$F | 29 | 20 | — | — | — | — | 19419.41 |
| ${}^{30}$F | 30 | 21 | — | — | — | — | 17868.69 |
| ${}^{31}$F | 31 | 22 | — | — | — | — | 18479.75 |

### Neon (Z = 10)

_3 of 20 isotopes with a framework prediction; 1 of 20 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{15}$Ne | 15 | 5 | — | — | — | — | 4758.84 |
| ${}^{16}$Ne | 16 | 6 | — | — | — | — | 1371.92 |
| ${}^{17}$Ne | 17 | 7 | — | — | — | — | 22.33 |
| ${}^{18}$Ne | 18 | 8 | — | — | — | — | 21.66 |
| ${}^{19}$Ne | 19 | 9 | — | — | — | — | 9.00 |
| ${}^{20}$Ne | 20 | 10 | 174.0483 | +83435352.19 | 18609.4368 | -719724.39 | 0.08 |
| ${}^{21}$Ne | 21 | 11 | 175.8559 | +50475703.05 | — | — | 1.95 |
| ${}^{22}$Ne | 22 | 12 | 185.9636 | +46089449.22 | — | — | 0.82 |
| ${}^{23}$Ne | 23 | 13 | — | — | — | — | 4.87 |
| ${}^{24}$Ne | 24 | 14 | — | — | — | — | 22.92 |
| ${}^{25}$Ne | 25 | 15 | — | — | — | — | 1247.35 |
| ${}^{26}$Ne | 26 | 16 | — | — | — | — | 760.91 |
| ${}^{27}$Ne | 27 | 17 | — | — | — | — | 3608.06 |
| ${}^{28}$Ne | 28 | 18 | — | — | — | — | 4831.44 |
| ${}^{29}$Ne | 29 | 19 | — | — | — | — | 5530.72 |
| ${}^{30}$Ne | 30 | 20 | — | — | — | — | 9054.96 |
| ${}^{31}$Ne | 31 | 21 | — | — | — | — | 9208.51 |
| ${}^{32}$Ne | 32 | 22 | — | — | — | — | 16854.08 |
| ${}^{33}$Ne | 33 | 23 | — | — | — | — | 19485.91 |
| ${}^{34}$Ne | 34 | 24 | — | — | — | — | 16178.89 |

### Fermium (Z = 100)

_20 of 20 isotopes with a framework prediction; 20 of 20 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{241}$Fm | 241 | 141 | -146.6045 | -1081554811.17 | 226503.6379 | +8658464.28 | 1335.69 |
| ${}^{242}$Fm | 242 | 142 | -139.9027 | -1077442796.12 | 227436.5016 | +8632441.03 | 1776.32 |
| ${}^{243}$Fm | 243 | 143 | -133.2092 | -1073444004.41 | 228369.3735 | +8598929.43 | 575.96 |
| ${}^{244}$Fm | 244 | 144 | -126.5238 | -1069434959.04 | 229302.2535 | +8571356.59 | 884.98 |
| ${}^{245}$Fm | 245 | 145 | -119.8465 | -1065528389.11 | 230235.1416 | +8537064.56 | 856.88 |
| ${}^{246}$Fm | 246 | 146 | -113.1772 | -1061605819.02 | 231168.0377 | +8508490.81 | 59.64 |
| ${}^{247}$Fm | 247 | 147 | -106.5158 | -1057775713.91 | 232100.9418 | +8473687.51 | 785.18 |
| ${}^{248}$Fm | 248 | 148 | -99.8622 | -1053934250.35 | 233033.8536 | +8444683.76 | 36.77 |
| ${}^{249}$Fm | 249 | 149 | -93.2164 | -1050170171.11 | 233966.7732 | +8409877.05 | 26.77 |
| ${}^{250}$Fm | 250 | 150 | -86.5783 | -1046409672.31 | 234899.7005 | +8380006.66 | 33.86 |
| ${}^{251}$Fm | 251 | 151 | -79.9478 | -1042713845.90 | 235832.6355 | +8344657.45 | 61.10 |
| ${}^{252}$Fm | 252 | 152 | -73.3249 | -1039025007.92 | 236765.5780 | +8314039.26 | 22.23 |
| ${}^{253}$Fm | 253 | 153 | -66.7095 | -1035399721.34 | 237698.5280 | +8276547.64 | 6.57 |
| ${}^{254}$Fm | 254 | 154 | -60.1015 | -1031783277.94 | 238631.4854 | +8243523.77 | 7.78 |
| ${}^{255}$Fm | 255 | 155 | -53.5008 | -1028215482.55 | 239564.4502 | +8205100.40 | 16.55 |
| ${}^{256}$Fm | 256 | 156 | -46.9074 | -1024655198.03 | 240497.4222 | +8172137.65 | 12.66 |
| ${}^{257}$Fm | 257 | 157 | -40.3213 | -1021138257.42 | 241430.4015 | +8133479.98 | 18.16 |
| ${}^{258}$Fm | 258 | 158 | -33.7423 | -1017630656.71 | 242363.3880 | +8100472.99 | 833.02 |
| ${}^{259}$Fm | 259 | 159 | -27.1704 | -1014162977.22 | 243296.3815 | +8061730.23 | 1173.29 |
| ${}^{260}$Fm | 260 | 160 | -20.6056 | -1010706869.77 | 244229.3821 | +8028376.82 | 1795.44 |

### Mendelevium (Z = 101)

_19 of 19 isotopes with a framework prediction; 19 of 19 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{244}$Md | 244 | 143 | -151.8827 | -1083687828.19 | 229326.8301 | +8650026.97 | 1646.99 |
| ${}^{245}$Md | 245 | 144 | -145.1750 | -1079633275.33 | 230259.6878 | +8621911.61 | 1138.40 |
| ${}^{246}$Md | 246 | 145 | -138.4755 | -1075649605.79 | 231192.5538 | +8589379.64 | 1133.77 |
| ${}^{247}$Md | 247 | 146 | -131.7841 | -1071673689.77 | 232125.4278 | +8561399.63 | 902.54 |
| ${}^{248}$Md | 248 | 147 | -125.1007 | -1067782624.41 | 233058.3098 | +8528476.16 | 798.12 |
| ${}^{249}$Md | 249 | 148 | -118.4252 | -1063890667.70 | 233991.1997 | +8499239.75 | 708.66 |
| ${}^{250}$Md | 250 | 149 | -111.7576 | -1060071358.86 | 234924.0975 | +8466006.04 | 390.29 |
| ${}^{251}$Md | 251 | 150 | -105.0977 | -1056264648.90 | 235857.0030 | +8435875.76 | 80.89 |
| ${}^{252}$Md | 252 | 151 | -98.4455 | -1052518632.44 | 236789.9163 | +8402011.83 | 388.76 |
| ${}^{253}$Md | 253 | 152 | -91.8010 | -1048783267.98 | 237722.8372 | +8371845.79 | 134.34 |
| ${}^{254}$Md | 254 | 153 | -85.1641 | -1045114602.99 | 238655.7657 | +8335246.65 | 421.11 |
| ${}^{255}$Md | 255 | 154 | -78.5347 | -1041457818.85 | 239588.7017 | +8302742.75 | 23.43 |
| ${}^{256}$Md | 256 | 155 | -71.9127 | -1037853234.89 | 240521.6451 | +8265348.53 | 519.34 |
| ${}^{257}$Md | 257 | 156 | -65.2980 | -1034253464.94 | 241454.5959 | +8232813.92 | 6.55 |
| ${}^{258}$Md | 258 | 157 | -58.6907 | -1030700914.65 | 242387.5540 | +8195691.31 | 14.45 |
| ${}^{259}$Md | 259 | 158 | -52.0906 | -1027160312.29 | 243320.5194 | +8162329.31 | 416.83 |
| ${}^{260}$Md | 260 | 159 | -45.4977 | -1023660250.65 | 244253.4919 | +8124627.60 | 1303.33 |
| ${}^{261}$Md | 261 | 160 | -38.9119 | -1020171532.81 | 245186.4715 | +8091209.91 | 2091.11 |
| ${}^{262}$Md | 262 | 161 | -32.3332 | -1016717559.57 | 246119.4582 | +8053699.95 | 1835.11 |

### Nobelium (Z = 102)

_17 of 17 isotopes with a framework prediction; 17 of 17 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{248}$No | 248 | 146 | -150.5659 | -1081778111.26 | 233082.9927 | +8618960.42 | 971.43 |
| ${}^{249}$No | 249 | 147 | -143.8604 | -1077843274.56 | 234015.8526 | +8585470.85 | 1204.39 |
| ${}^{250}$No | 250 | 148 | -137.1630 | -1073882555.67 | 234948.7205 | +8557994.24 | 859.70 |
| ${}^{251}$No | 251 | 149 | -130.4734 | -1070027541.19 | 235881.5964 | +8524287.54 | 772.63 |
| ${}^{252}$No | 252 | 150 | -123.7917 | -1066152758.20 | 236814.4802 | +8496294.57 | 39.57 |
| ${}^{253}$No | 253 | 151 | -117.1179 | -1062366888.01 | 237747.3717 | +8462289.52 | 29.32 |
| ${}^{254}$No | 254 | 152 | -110.4517 | -1058576672.47 | 238680.2710 | +8433368.65 | 40.80 |
| ${}^{255}$No | 255 | 153 | -103.7932 | -1054871320.75 | 239613.1779 | +8397390.48 | 59.11 |
| ${}^{256}$No | 256 | 154 | -97.1423 | -1051164277.62 | 240546.0924 | +8366280.39 | 31.64 |
| ${}^{257}$No | 257 | 155 | -90.4989 | -1047523881.38 | 241479.0144 | +8329494.99 | 25.87 |
| ${}^{258}$No | 258 | 156 | -83.8629 | -1043884181.24 | 242411.9439 | +8298032.69 | 414.57 |
| ${}^{259}$No | 259 | 157 | -77.2344 | -1040297748.20 | 243344.8808 | +8261113.81 | 26.36 |
| ${}^{260}$No | 260 | 158 | -70.6131 | -1036716088.78 | 244277.8249 | +8228970.32 | 826.60 |
| ${}^{261}$No | 261 | 159 | -63.9991 | -1033189951.21 | 245210.7764 | +8191649.77 | 823.42 |
| ${}^{262}$No | 262 | 160 | -57.3923 | -1029662104.29 | 246143.7350 | +8159598.39 | 1476.49 |
| ${}^{263}$No | 263 | 161 | -50.7926 | -1026183283.77 | 247076.7007 | +8122134.12 | 1999.16 |
| ${}^{264}$No | 264 | 162 | -44.2000 | -1022713924.72 | 248009.6735 | +8089681.75 | 2400.49 |

### Lawrencium (Z = 103)

_16 of 16 isotopes with a framework prediction; 16 of 16 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{251}$Lr | 251 | 148 | -156.0750 | -1084028751.76 | 235906.4157 | +8608924.97 | 856.25 |
| ${}^{252}$Lr | 252 | 149 | -149.3635 | -1080096262.62 | 236839.2696 | +8577529.57 | 785.42 |
| ${}^{253}$Lr | 253 | 150 | -142.6600 | -1076169070.66 | 237772.1315 | +8549497.05 | 697.90 |
| ${}^{254}$Lr | 254 | 151 | -135.9643 | -1072325776.02 | 238705.0012 | +8516879.72 | 385.78 |
| ${}^{255}$Lr | 255 | 152 | -129.2764 | -1068485128.68 | 239637.8788 | +8488035.67 | 74.48 |
| ${}^{256}$Lr | 256 | 153 | -122.5963 | -1064731203.93 | 240570.7641 | +8453117.27 | 347.52 |
| ${}^{257}$Lr | 257 | 154 | -115.9238 | -1060979527.27 | 241503.6571 | +8422212.14 | 182.81 |
| ${}^{258}$Lr | 258 | 155 | -109.2590 | -1057289562.64 | 242436.5576 | +8386550.00 | 422.31 |
| ${}^{259}$Lr | 259 | 156 | -102.6017 | -1053605600.45 | 243369.4657 | +8355577.00 | 293.32 |
| ${}^{260}$Lr | 260 | 157 | -95.9518 | -1049985823.48 | 244302.3813 | +8319225.04 | 515.18 |
| ${}^{261}$Lr | 261 | 158 | -89.3093 | -1046359746.66 | 245235.3042 | +8287928.54 | 823.42 |
| ${}^{262}$Lr | 262 | 159 | -82.6742 | -1042792284.10 | 246168.2345 | +8251665.85 | 820.27 |
| ${}^{263}$Lr | 263 | 160 | -76.0463 | -1039227984.11 | 247101.1721 | +8219763.37 | 912.16 |
| ${}^{264}$Lr | 264 | 161 | -69.4256 | -1035715868.34 | 248034.1168 | +8183448.40 | 1771.96 |
| ${}^{265}$Lr | 265 | 162 | -62.8121 | -1032209117.63 | 248967.0687 | +8150897.53 | 2214.12 |
| ${}^{266}$Lr | 266 | 163 | -56.2057 | -1028752154.16 | 249900.0277 | +8112233.42 | 2175.71 |

### Rutherfordium (Z = 104)

_16 of 16 isotopes with a framework prediction; 16 of 16 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{253}$Rf | 253 | 149 | -168.4273 | -1090206054.04 | 237797.1165 | +8633579.88 | 1738.44 |
| ${}^{254}$Rf | 254 | 150 | -161.7019 | -1086216347.97 | 238729.9565 | +8607166.41 | 1196.38 |
| ${}^{255}$Rf | 255 | 151 | -154.9844 | -1082332943.45 | 239662.8044 | +8574331.52 | 760.48 |
| ${}^{256}$Rf | 256 | 152 | -148.2747 | -1078424384.25 | 240595.6602 | +8547014.34 | 74.81 |
| ${}^{257}$Rf | 257 | 153 | -141.5729 | -1074626040.24 | 241528.5238 | +8512564.32 | 45.16 |
| ${}^{258}$Rf | 258 | 154 | -134.8789 | -1070814021.69 | 242461.3952 | +8483306.75 | 66.98 |
| ${}^{259}$Rf | 259 | 155 | -128.1925 | -1067093902.93 | 243394.2742 | +8447853.89 | 301.04 |
| ${}^{260}$Rf | 260 | 156 | -121.5137 | -1063353733.49 | 244327.1609 | +8417870.10 | 826.58 |
| ${}^{261}$Rf | 261 | 157 | -114.8425 | -1059691569.88 | 245260.0551 | +8382390.60 | 269.97 |
| ${}^{262}$Rf | 262 | 158 | -108.1788 | -1056023882.38 | 246192.9567 | +8351737.89 | 915.65 |
| ${}^{263}$Rf | 263 | 159 | -101.5224 | -1052419446.45 | 247125.8658 | +8316042.56 | 623.31 |
| ${}^{264}$Rf | 264 | 160 | -94.8734 | -1048820683.92 | 248058.7823 | +8284935.23 | 1465.28 |
| ${}^{265}$Rf | 265 | 161 | -88.2317 | -1045274667.38 | 248991.7060 | +8248798.55 | 1459.73 |
| ${}^{266}$Rf | 266 | 162 | -81.5972 | -1041729905.79 | 249924.6369 | +8217714.23 | 1664.67 |
| ${}^{267}$Rf | 267 | 163 | -74.9699 | -1038243827.96 | 250857.5750 | +8179350.80 | 2309.81 |
| ${}^{268}$Rf | 268 | 164 | -68.3497 | -1034760272.66 | 251790.5202 | +8146454.14 | 2651.76 |

### Dubnium (Z = 105)

_16 of 16 isotopes with a framework prediction; 16 of 16 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{255}$Db | 255 | 150 | -180.9170 | -1096409606.40 | 239687.9547 | +8657823.83 | 1191.66 |
| ${}^{256}$Db | 256 | 151 | -174.1776 | -1092455646.86 | 240620.7807 | +8626628.01 | 784.83 |
| ${}^{257}$Db | 257 | 152 | -167.4461 | -1088500872.58 | 241553.6147 | +8599274.03 | 687.42 |
| ${}^{258}$Db | 258 | 153 | -160.7226 | -1084646709.96 | 242486.4566 | +8565885.74 | 382.06 |
| ${}^{259}$Db | 259 | 154 | -154.0069 | -1080786942.20 | 243419.3063 | +8536423.74 | 234.86 |
| ${}^{260}$Db | 260 | 155 | -147.2989 | -1077006168.30 | 244352.1637 | +8502233.23 | 384.45 |
| ${}^{261}$Db | 261 | 156 | -140.5987 | -1073221729.10 | 245285.0289 | +8472674.51 | 451.91 |
| ${}^{262}$Db | 262 | 157 | -133.9060 | -1069517379.04 | 246217.9017 | +8437963.33 | 587.53 |
| ${}^{263}$Db | 263 | 158 | -127.2210 | -1065795688.18 | 247150.7820 | +8408023.80 | 684.11 |
| ${}^{264}$Db | 264 | 159 | -120.5434 | -1062156777.34 | 248083.6699 | +8373034.74 | 957.91 |
| ${}^{265}$Db | 265 | 160 | -113.8732 | -1058503773.72 | 249016.5651 | +8342550.60 | 905.26 |
| ${}^{266}$Db | 266 | 161 | -107.2104 | -1054918466.82 | 249949.4677 | +8307290.06 | 1142.34 |
| ${}^{267}$Db | 267 | 162 | -100.5549 | -1051330257.02 | 250882.3777 | +8276720.89 | 1504.93 |
| ${}^{268}$Db | 268 | 163 | -93.9066 | -1047816299.93 | 251815.2948 | +8239253.08 | 2118.41 |
| ${}^{269}$Db | 269 | 164 | -87.2655 | -1044299760.59 | 252748.2191 | +8205944.30 | 2485.81 |
| ${}^{270}$Db | 270 | 165 | -80.6315 | -1040830641.31 | 253681.1506 | +8168260.68 | 2284.07 |

### Seaborgium (Z = 106)

_16 of 16 isotopes with a framework prediction; 16 of 16 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{258}$Sg | 258 | 152 | -186.7901 | -1098609755.54 | 242511.7418 | +8655160.41 | 1716.30 |
| ${}^{259}$Sg | 259 | 153 | -180.0448 | -1094707600.19 | 243444.5619 | +8622140.22 | 748.70 |
| ${}^{260}$Sg | 260 | 154 | -173.3074 | -1090781241.03 | 244377.3899 | +8594380.02 | 84.75 |
| ${}^{261}$Sg | 261 | 155 | -166.5778 | -1086954933.79 | 245310.2257 | +8560938.54 | 76.03 |
| ${}^{262}$Sg | 262 | 156 | -159.8560 | -1083111721.49 | 246243.0694 | +8532301.02 | 90.79 |
| ${}^{263}$Sg | 263 | 157 | -153.1419 | -1079363330.83 | 247175.9207 | +8497898.19 | 383.86 |
| ${}^{264}$Sg | 264 | 158 | -146.4355 | -1075590056.51 | 248108.7796 | +8468861.91 | 1151.00 |
| ${}^{265}$Sg | 265 | 159 | -139.7366 | -1071908882.97 | 249041.6462 | +8434263.41 | 562.01 |
| ${}^{266}$Sg | 266 | 160 | -133.0452 | -1068217383.05 | 249974.5202 | +8404787.03 | 988.27 |
| ${}^{267}$Sg | 267 | 161 | -126.3612 | -1064591647.90 | 250907.4017 | +8370027.39 | 1051.94 |
| ${}^{268}$Sg | 268 | 162 | -119.6846 | -1060958840.85 | 251840.2905 | +8340385.88 | 1879.72 |
| ${}^{269}$Sg | 269 | 163 | -113.0154 | -1057410694.65 | 252773.1866 | +8303351.03 | 1467.70 |
| ${}^{270}$Sg | 270 | 164 | -106.3533 | -1053855790.76 | 253706.0900 | +8271244.63 | 1821.34 |
| ${}^{271}$Sg | 271 | 165 | -99.6985 | -1050361553.04 | 254639.0006 | +8233628.96 | 2338.33 |
| ${}^{272}$Sg | 272 | 166 | -93.0508 | -1046856387.66 | 255571.9183 | +8201420.25 | 2730.25 |
| ${}^{273}$Sg | 273 | 167 | -86.4101 | -1043406564.45 | 256504.8431 | +8163544.12 | 1570.63 |

### Bohrium (Z = 107)

_19 of 19 isotopes with a framework prediction; 19 of 19 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{260}$Bh | 260 | 153 | -199.5392 | -1104930045.14 | 244402.8393 | +8672039.26 | 811.16 |
| ${}^{261}$Bh | 261 | 154 | -192.7800 | -1100941269.62 | 245335.6456 | +8644405.72 | 739.22 |
| ${}^{262}$Bh | 262 | 155 | -186.0288 | -1097055676.90 | 246268.4597 | +8611989.26 | 381.19 |
| ${}^{263}$Bh | 263 | 156 | -179.2854 | -1093152962.58 | 247201.2818 | +8583675.61 | 1246.57 |
| ${}^{264}$Bh | 264 | 157 | -172.5497 | -1089350307.50 | 248134.1116 | +8550610.83 | 719.36 |
| ${}^{265}$Bh | 265 | 158 | -165.8218 | -1085530722.59 | 249066.9491 | +8522015.22 | 969.35 |
| ${}^{266}$Bh | 266 | 159 | -159.1016 | -1081789444.97 | 249999.7942 | +8488488.97 | 657.58 |
| ${}^{267}$Bh | 267 | 160 | -152.3889 | -1078045249.56 | 250932.6470 | +8459495.52 | 1055.68 |
| ${}^{268}$Bh | 268 | 161 | -145.6837 | -1074373510.35 | 251865.5072 | +8425573.45 | 1529.11 |
| ${}^{269}$Bh | 269 | 162 | -138.9860 | -1070690465.41 | 252798.3750 | +8396647.26 | 1493.70 |
| ${}^{270}$Bh | 270 | 163 | -132.2957 | -1067111902.20 | 253731.2500 | +8360021.26 | 1184.60 |
| ${}^{271}$Bh | 271 | 164 | -125.6127 | -1063512661.57 | 254664.1325 | +8328180.21 | 1519.54 |
| ${}^{272}$Bh | 272 | 165 | -118.9369 | -1059981911.04 | 255597.0221 | +8291433.62 | 2098.20 |
| ${}^{273}$Bh | 273 | 166 | -112.2684 | -1056442427.08 | 256529.9190 | +8259078.96 | 2573.77 |
| ${}^{274}$Bh | 274 | 167 | -105.6070 | -1052957813.38 | 257462.8230 | +8222318.05 | 2261.59 |
| ${}^{275}$Bh | 275 | 168 | -98.9527 | -1049474478.69 | 258395.7341 | +8190022.71 | 2340.58 |
| ${}^{276}$Bh | 276 | 169 | -92.3054 | -1046034376.11 | 259328.6523 | +8153476.72 | 2332.07 |
| ${}^{277}$Bh | 277 | 170 | -85.6650 | -1042597802.66 | 260261.5774 | +8121205.30 | 2323.64 |
| ${}^{278}$Bh | 278 | 171 | -79.0316 | -1039206501.36 | 261194.5094 | +8084833.20 | 1542.31 |

### Hassium (Z = 108)

_18 of 18 isotopes with a framework prediction; 18 of 18 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{263}$Hs | 263 | 155 | -205.6512 | -1107189001.37 | 247226.8653 | +8666731.17 | 805.69 |
| ${}^{264}$Hs | 264 | 156 | -198.8862 | -1103222505.89 | 248159.6657 | +8639696.37 | 117.39 |
| ${}^{265}$Hs | 265 | 157 | -192.1290 | -1099368204.12 | 249092.4739 | +8606970.00 | 97.01 |
| ${}^{266}$Hs | 266 | 158 | -185.3796 | -1095490651.00 | 250025.2899 | +8578987.14 | 109.34 |
| ${}^{267}$Hs | 267 | 159 | -178.6379 | -1091714299.31 | 250958.1137 | +8546064.24 | 381.83 |
| ${}^{268}$Hs | 268 | 160 | -171.9039 | -1087903577.23 | 251890.9451 | +8518293.37 | 1200.90 |
| ${}^{269}$Hs | 269 | 161 | -165.1775 | -1084184616.33 | 252823.7841 | +8485869.16 | 523.90 |
| ${}^{270}$Hs | 270 | 162 | -158.4586 | -1080450108.78 | 253756.6306 | +8457351.41 | 984.70 |
| ${}^{271}$Hs | 271 | 163 | -151.7471 | -1076832117.01 | 254689.4846 | +8421244.67 | 1091.70 |
| ${}^{272}$Hs | 272 | 164 | -145.0431 | -1073187842.51 | 255622.3460 | +8390468.86 | 2010.01 |
| ${}^{273}$Hs | 273 | 165 | -138.3464 | -1069619905.93 | 256555.2147 | +8354203.25 | 1468.10 |
| ${}^{274}$Hs | 274 | 166 | -131.6570 | -1066039009.30 | 257488.0907 | +8322670.92 | 1838.46 |
| ${}^{275}$Hs | 275 | 167 | -124.9747 | -1062528014.54 | 258420.9739 | +8285701.61 | 2315.13 |
| ${}^{276}$Hs | 276 | 168 | -118.2997 | -1058998217.48 | 259353.8643 | +8254487.17 | 2799.22 |
| ${}^{277}$Hs | 277 | 169 | -111.6317 | -1055540602.68 | 260286.7617 | +8217683.57 | 1731.90 |
| ${}^{278}$Hs | 278 | 170 | -104.9708 | -1052067401.88 | 261219.6662 | +8186402.87 | 1157.63 |
| ${}^{279}$Hs | 279 | 171 | -98.3169 | -1048652511.94 | 262152.5777 | +8149811.97 | 2306.94 |
| ${}^{280}$Hs | 280 | 172 | -91.6698 | -1045226167.32 | 263085.4961 | +8118763.32 | 2298.69 |

### Meitnerium (Z = 109)

_18 of 18 isotopes with a framework prediction; 18 of 18 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{265}$Mt | 265 | 156 | -218.6580 | -1113465971.14 | 249118.2206 | +8687841.97 | 1776.45 |
| ${}^{266}$Mt | 266 | 157 | -211.8792 | -1109553657.68 | 250051.0072 | +8656146.63 | 389.15 |
| ${}^{267}$Mt | 267 | 158 | -205.1083 | -1105622949.87 | 250983.8017 | +8628490.52 | 2021.43 |
| ${}^{268}$Mt | 268 | 159 | -198.3451 | -1101787060.36 | 251916.6040 | +8596056.92 | 932.35 |
| ${}^{269}$Mt | 269 | 160 | -191.5897 | -1097914407.88 | 252849.4140 | +8568767.13 | 1244.71 |
| ${}^{270}$Mt | 270 | 161 | -184.8420 | -1094154846.71 | 253782.2317 | +8536658.59 | 758.86 |
| ${}^{271}$Mt | 271 | 162 | -178.1018 | -1090361933.03 | 254715.0570 | +8508886.48 | 1305.60 |
| ${}^{272}$Mt | 272 | 163 | -171.3692 | -1086697943.22 | 255647.8898 | +8473425.50 | 1914.43 |
| ${}^{273}$Mt | 273 | 164 | -164.6441 | -1083013349.30 | 256580.7301 | +8442536.88 | 1665.78 |
| ${}^{274}$Mt | 274 | 165 | -157.9264 | -1079401256.18 | 257513.5778 | +8407301.31 | 1473.66 |
| ${}^{275}$Mt | 275 | 166 | -151.2160 | -1075771874.76 | 258446.4328 | +8376085.68 | 1511.91 |
| ${}^{276}$Mt | 276 | 167 | -144.5130 | -1072220370.69 | 259379.2952 | +8341093.65 | 2067.70 |
| ${}^{277}$Mt | 277 | 168 | -137.8171 | -1068653885.96 | 260312.1648 | +8309704.39 | 2565.37 |
| ${}^{278}$Mt | 278 | 169 | -131.1284 | -1065149865.02 | 261245.0415 | +8274429.31 | 2232.56 |
| ${}^{279}$Mt | 279 | 170 | -124.4469 | -1061634118.52 | 262177.9254 | +8243082.87 | 2579.18 |
| ${}^{280}$Mt | 280 | 171 | -117.7723 | -1058184468.58 | 263110.8163 | +8207712.42 | 2298.67 |
| ${}^{281}$Mt | 281 | 172 | -111.1048 | -1054725372.45 | 264043.7142 | +8176604.79 | 2290.48 |
| ${}^{282}$Mt | 282 | 173 | -104.4442 | -1051311942.49 | 264976.6190 | +8141274.83 | 1701.12 |

### Sodium (Z = 11)

_0 of 23 isotopes with a framework prediction; 0 of 23 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{17}$Na | 17 | 6 | — | — | — | — | 3756.47 |
| ${}^{18}$Na | 18 | 7 | — | — | — | — | 5590.82 |
| ${}^{19}$Na | 19 | 8 | — | — | — | — | 594.78 |
| ${}^{20}$Na | 20 | 9 | — | — | — | — | 59.48 |
| ${}^{21}$Na | 21 | 10 | — | — | — | — | 2.14 |
| ${}^{22}$Na | 22 | 11 | — | — | — | — | 6.41 |
| ${}^{23}$Na | 23 | 12 | — | — | — | — | 0.08 |
| ${}^{24}$Na | 24 | 13 | — | — | — | — | 0.71 |
| ${}^{25}$Na | 25 | 14 | — | — | — | — | 51.54 |
| ${}^{26}$Na | 26 | 15 | — | — | — | — | 144.62 |
| ${}^{27}$Na | 27 | 16 | — | — | — | — | 148.18 |
| ${}^{28}$Na | 28 | 17 | — | — | — | — | 392.87 |
| ${}^{29}$Na | 29 | 18 | — | — | — | — | 271.56 |
| ${}^{30}$Na | 30 | 19 | — | — | — | — | 169.08 |
| ${}^{31}$Na | 31 | 20 | — | — | — | — | 483.67 |
| ${}^{32}$Na | 32 | 21 | — | — | — | — | 1249.22 |
| ${}^{33}$Na | 33 | 22 | — | — | — | — | 14625.05 |
| ${}^{34}$Na | 34 | 23 | — | — | — | — | 18907.56 |
| ${}^{35}$Na | 35 | 24 | — | — | — | — | 20547.59 |
| ${}^{36}$Na | 36 | 25 | — | — | — | — | 20444.24 |
| ${}^{37}$Na | 37 | 26 | — | — | — | — | 19888.26 |
| ${}^{38}$Na | 38 | 27 | — | — | — | — | 20175.24 |
| ${}^{39}$Na | 39 | 28 | — | — | — | — | 20396.61 |

### Darmstadtium (Z = 110)

_18 of 18 isotopes with a framework prediction; 18 of 18 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{267}$Ds | 267 | 157 | -231.8000 | -1119779885.88 | 251009.7110 | +8707928.80 | 819.78 |
| ${}^{268}$Ds | 268 | 158 | -225.0074 | -1115772190.50 | 251942.4839 | +8681510.38 | 1208.31 |
| ${}^{269}$Ds | 269 | 159 | -218.2228 | -1111892371.23 | 252875.2647 | +8649612.14 | 125.26 |
| ${}^{270}$Ds | 270 | 160 | -211.4459 | -1107962308.04 | 253808.0533 | +8623351.49 | 156.08 |
| ${}^{271}$Ds | 271 | 161 | -204.6768 | -1104145754.91 | 254740.8496 | +8591628.69 | 383.56 |
| ${}^{272}$Ds | 272 | 162 | -197.9154 | -1100293608.55 | 255673.6536 | +8564707.12 | 1675.57 |
| ${}^{273}$Ds | 273 | 163 | -191.1616 | -1096582839.43 | 256606.4652 | +8529801.01 | 556.47 |
| ${}^{274}$Ds | 274 | 164 | -184.4153 | -1092847099.84 | 257539.2844 | +8500274.62 | 1524.72 |
| ${}^{275}$Ds | 275 | 165 | -177.6765 | -1089202891.06 | 258472.1110 | +8464864.15 | 1330.17 |
| ${}^{276}$Ds | 276 | 166 | -170.9452 | -1085512447.20 | 259404.9451 | +8435998.70 | 2129.25 |
| ${}^{277}$Ds | 277 | 167 | -164.2212 | -1081920180.02 | 260337.7865 | +8400806.56 | 1519.00 |
| ${}^{278}$Ds | 278 | 168 | -157.5045 | -1078297818.45 | 261270.6353 | +8371323.20 | 1970.11 |
| ${}^{279}$Ds | 279 | 169 | -150.7951 | -1074766097.74 | 262203.4912 | +8335819.49 | 2324.83 |
| ${}^{280}$Ds | 280 | 170 | -144.0928 | -1071207575.94 | 263136.3544 | +8306305.51 | 2866.21 |
| ${}^{281}$Ds | 281 | 171 | -137.3977 | -1067722941.09 | 264069.2247 | +8270649.33 | 1881.46 |
| ${}^{282}$Ds | 282 | 172 | -130.7096 | -1064224627.43 | 265002.1020 | +8240779.85 | 1141.17 |
| ${}^{283}$Ds | 283 | 173 | -124.0285 | -1060785472.69 | 265934.9864 | +8205330.48 | 1896.39 |
| ${}^{284}$Ds | 284 | 174 | -117.3544 | -1057335873.32 | 266867.8777 | +8175525.41 | 1889.71 |

### Roentgenium (Z = 111)

_15 of 15 isotopes with a framework prediction; 15 of 15 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{272}$Rg | 272 | 161 | -224.6816 | -1114298484.93 | 255699.6374 | +8640588.17 | 922.27 |
| ${}^{273}$Rg | 273 | 162 | -217.8988 | -1110396141.77 | 256632.4201 | +8613576.61 | 1570.55 |
| ${}^{274}$Rg | 274 | 163 | -211.1237 | -1106617483.88 | 257565.2104 | +8580413.03 | 820.70 |
| ${}^{275}$Rg | 275 | 164 | -204.3563 | -1102824649.79 | 258498.0084 | +8551233.72 | 1740.83 |
| ${}^{276}$Rg | 276 | 165 | -197.5964 | -1099117949.96 | 259430.8140 | +8517558.68 | 2444.25 |
| ${}^{277}$Rg | 277 | 166 | -190.8440 | -1095398436.28 | 260363.6270 | +8487947.67 | 1818.45 |
| ${}^{278}$Rg | 278 | 167 | -184.0990 | -1091746574.28 | 261296.4475 | +8454329.48 | 1499.13 |
| ${}^{279}$Rg | 279 | 168 | -177.3615 | -1088096474.29 | 262229.2753 | +8424513.87 | 1622.71 |
| ${}^{280}$Rg | 280 | 169 | -170.6312 | -1084497657.96 | 263162.1104 | +8391217.74 | 2038.08 |
| ${}^{281}$Rg | 281 | 170 | -163.9082 | -1080913179.45 | 264094.9529 | +8360951.77 | 2955.54 |
| ${}^{282}$Rg | 282 | 171 | -157.1924 | -1077376413.98 | 265027.8025 | +8327236.59 | 2236.25 |
| ${}^{283}$Rg | 283 | 172 | -150.4837 | -1073843132.49 | 265960.6592 | +8296735.49 | 2570.88 |
| ${}^{284}$Rg | 284 | 173 | -143.7821 | -1070364814.55 | 266893.5230 | +8262846.51 | 1889.69 |
| ${}^{285}$Rg | 285 | 174 | -137.0875 | -1066881069.35 | 267826.3938 | +8232375.91 | 2258.26 |
| ${}^{286}$Rg | 286 | 175 | -130.3998 | -1063457689.14 | 268759.2716 | +8198283.61 | 1719.21 |

### Copernicium (Z = 112)

_13 of 13 isotopes with a framework prediction; 13 of 13 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{276}$Cn | 276 | 164 | -224.4665 | -1112815172.71 | 259456.9018 | +8607315.01 | 1944.51 |
| ${}^{277}$Cn | 277 | 165 | -217.6855 | -1109072616.73 | 260389.6861 | +8573553.80 | 595.32 |
| ${}^{278}$Cn | 278 | 166 | -210.9120 | -1105283971.58 | 261322.4781 | +8545753.78 | 1689.65 |
| ${}^{279}$Cn | 279 | 167 | -204.1460 | -1101597643.63 | 262255.2775 | +8511711.74 | 1518.81 |
| ${}^{280}$Cn | 280 | 168 | -197.3875 | -1097883281.99 | 263188.0844 | +8483913.47 | 2234.38 |
| ${}^{281}$Cn | 281 | 169 | -190.6364 | -1094264449.61 | 264120.8987 | +8449953.45 | 1518.66 |
| ${}^{282}$Cn | 282 | 170 | -183.8926 | -1090607371.31 | 265053.7203 | +8421684.03 | 2083.85 |
| ${}^{283}$Cn | 283 | 171 | -177.1560 | -1087040174.98 | 265986.5492 | +8387406.60 | 2330.73 |
| ${}^{284}$Cn | 284 | 172 | -170.4267 | -1083450683.05 | 266919.3853 | +8358852.12 | 2882.03 |
| ${}^{285}$Cn | 285 | 173 | -163.7045 | -1079944553.16 | 267852.2285 | +8324482.36 | 1907.59 |
| ${}^{286}$Cn | 286 | 174 | -156.9894 | -1076418463.84 | 268785.0788 | +8295323.25 | 2624.23 |
| ${}^{287}$Cn | 287 | 175 | -150.2813 | -1072969364.56 | 269717.9362 | +8260527.10 | 2615.07 |
| ${}^{288}$Cn | 288 | 176 | -143.5802 | -1069492935.15 | 270650.8005 | +8231107.07 | 2605.98 |

### Nihonium (Z = 113)

_13 of 13 isotopes with a framework prediction; 13 of 13 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{278}$Nh | 278 | 165 | -237.9434 | -1119191142.25 | 261348.7272 | +8622975.36 | 862.78 |
| ${}^{279}$Nh | 279 | 166 | -231.1488 | -1115340433.44 | 262281.4980 | +8595327.92 | 2306.83 |
| ${}^{280}$Nh | 280 | 167 | -224.3618 | -1111600559.11 | 263214.2764 | +8562690.88 | 1531.20 |
| ${}^{281}$Nh | 281 | 168 | -217.5822 | -1107828162.41 | 264147.0623 | +8534974.46 | 1145.20 |
| ${}^{282}$Nh | 282 | 169 | -210.8102 | -1104159653.22 | 265079.8556 | +8502307.77 | 1523.87 |
| ${}^{283}$Nh | 283 | 170 | -204.0455 | -1100461039.74 | 266012.6564 | +8474045.64 | 1656.21 |
| ${}^{284}$Nh | 284 | 171 | -197.2882 | -1096846048.01 | 266945.4645 | +8441464.50 | 2016.34 |
| ${}^{285}$Nh | 285 | 172 | -190.5381 | -1093217351.35 | 267878.2798 | +8412371.70 | 2917.45 |
| ${}^{286}$Nh | 286 | 173 | -183.7953 | -1089654142.82 | 268811.1024 | +8379679.43 | 2215.37 |
| ${}^{287}$Nh | 287 | 174 | -177.0596 | -1086091610.78 | 269743.9322 | +8349847.41 | 2642.90 |
| ${}^{288}$Nh | 288 | 175 | -170.3311 | -1082601573.36 | 270676.7690 | +8316428.49 | 2605.95 |
| ${}^{289}$Nh | 289 | 176 | -163.6095 | -1079089541.48 | 271609.6129 | +8286764.52 | 1856.92 |
| ${}^{290}$Nh | 290 | 177 | -156.8950 | -1075645585.79 | 272542.4638 | +8252915.18 | 1733.34 |

### Flerovium (Z = 114)

_8 of 8 isotopes with a framework prediction; 8 of 8 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{284}$Fl | 284 | 170 | -224.3666 | -1110292246.59 | 266971.7606 | +8532467.05 | 2477.29 |
| ${}^{285}$Fl | 285 | 171 | -217.5885 | -1106644550.77 | 267904.5478 | +8499243.11 | 1518.32 |
| ${}^{286}$Fl | 286 | 172 | -210.8177 | -1102964758.56 | 268837.3425 | +8471875.30 | 2061.61 |
| ${}^{287}$Fl | 287 | 173 | -204.0541 | -1099369678.54 | 269770.1444 | +8438506.67 | 2308.60 |
| ${}^{288}$Fl | 288 | 174 | -197.2979 | -1095759294.10 | 270702.9535 | +8410411.38 | 2841.90 |
| ${}^{289}$Fl | 289 | 175 | -190.5487 | -1092228029.46 | 271635.7698 | +8376696.65 | 1894.94 |
| ${}^{290}$Fl | 290 | 176 | -183.8067 | -1088682848.54 | 272568.5932 | +8348029.44 | 2591.39 |
| ${}^{291}$Fl | 291 | 177 | -177.0718 | -1085211332.04 | 273501.4237 | +8313993.16 | 2579.03 |

### Moscovium (Z = 115)

_6 of 6 isotopes with a framework prediction; 6 of 6 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{287}$Mc | 287 | 172 | -231.2648 | -1112873072.06 | 269796.5727 | +8522901.51 | 1653.95 |
| ${}^{288}$Mc | 288 | 173 | -224.4806 | -1109242675.67 | 270729.3539 | +8490916.91 | 1995.19 |
| ${}^{289}$Mc | 289 | 174 | -217.7036 | -1105578102.76 | 271662.1424 | +8462553.13 | 2883.88 |
| ${}^{290}$Mc | 290 | 175 | -210.9339 | -1101999485.42 | 272594.9381 | +8430339.12 | 2188.17 |
| ${}^{291}$Mc | 291 | 176 | -204.1714 | -1098417713.47 | 273527.7410 | +8401053.66 | 2709.50 |
| ${}^{292}$Mc | 292 | 177 | -197.4160 | -1094902039.59 | 274460.5510 | +8368171.47 | 2570.15 |

### Livermorium (Z = 116)

_5 of 5 isotopes with a framework prediction; 5 of 5 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{289}$Lv | 289 | 173 | -245.0742 | -1119118932.39 | 271688.7306 | +8547122.76 | 1867.23 |
| ${}^{290}$Lv | 290 | 174 | -238.2765 | -1115399335.06 | 272621.4984 | +8520254.83 | 2043.43 |
| ${}^{291}$Lv | 291 | 175 | -231.4862 | -1111788248.18 | 273554.2734 | +8487478.98 | 2297.38 |
| ${}^{292}$Lv | 292 | 176 | -224.7031 | -1108140962.29 | 274487.0557 | +8459869.20 | 2802.86 |
| ${}^{293}$Lv | 293 | 177 | -217.9272 | -1104595517.24 | 275419.8452 | +8426768.40 | 1886.06 |

### Tennessine (Z = 117)

_4 of 4 isotopes with a framework prediction; 4 of 4 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{291}$Ts | 291 | 174 | -259.0162 | -1125400113.60 | 273581.0211 | +8569691.05 | 2197.76 |
| ${}^{292}$Ts | 292 | 175 | -252.2051 | -1121735901.93 | 274513.7755 | +8537700.64 | 2457.15 |
| ${}^{293}$Ts | 293 | 176 | -245.4014 | -1118047562.59 | 275446.5372 | +8510244.82 | 2847.80 |
| ${}^{294}$Ts | 294 | 177 | -238.6049 | -1114436183.91 | 276379.3061 | +8478727.91 | 2165.11 |

### Oganesson (Z = 118)

_3 of 3 isotopes with a framework prediction; 3 of 3 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{293}$Og | 293 | 175 | -273.0904 | -1131682542.67 | 275473.4438 | +8592606.29 | 2595.38 |
| ${}^{294}$Og | 294 | 176 | -266.2660 | -1127937073.56 | 276406.1848 | +8566044.79 | 2018.94 |
| ${}^{295}$Og | 295 | 177 | -259.4489 | -1124291657.60 | 277338.9331 | +8534077.06 | 2381.31 |

### Magnesium (Z = 12)

_2 of 23 isotopes with a framework prediction; 2 of 23 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{19}$Mg | 19 | 7 | — | — | — | — | 3384.07 |
| ${}^{20}$Mg | 20 | 8 | — | — | — | — | 99.91 |
| ${}^{21}$Mg | 21 | 9 | — | — | — | — | 38.55 |
| ${}^{22}$Mg | 22 | 10 | — | — | — | — | 7.73 |
| ${}^{23}$Mg | 23 | 11 | — | — | — | — | 1.48 |
| ${}^{24}$Mg | 24 | 12 | 216.1389 | +90195326.40 | 22324.0432 | -800364.49 | 0.54 |
| ${}^{25}$Mg | 25 | 13 | — | — | — | — | 2.00 |
| ${}^{26}$Mg | 26 | 14 | — | — | — | — | 1.19 |
| ${}^{27}$Mg | 27 | 15 | — | — | — | — | 1.85 |
| ${}^{28}$Mg | 28 | 16 | — | — | — | — | 10.01 |
| ${}^{29}$Mg | 29 | 17 | — | — | — | — | 12.73 |
| ${}^{30}$Mg | 30 | 18 | — | — | — | — | 46.35 |
| ${}^{31}$Mg | 31 | 19 | — | — | — | — | 106.46 |
| ${}^{32}$Mg | 32 | 20 | — | — | — | — | 109.38 |
| ${}^{33}$Mg | 33 | 21 | — | — | — | — | 86.62 |
| ${}^{34}$Mg | 34 | 22 | — | — | — | — | 217.59 |
| ${}^{35}$Mg | 35 | 23 | — | — | — | — | 8267.46 |
| ${}^{36}$Mg | 36 | 24 | — | — | — | — | 20570.83 |
| ${}^{37}$Mg | 37 | 25 | — | — | — | — | 20263.14 |
| ${}^{38}$Mg | 38 | 26 | — | — | — | — | 14196.86 |
| ${}^{39}$Mg | 39 | 27 | — | — | — | — | 14111.59 |
| ${}^{40}$Mg | 40 | 28 | — | — | — | — | 13407.17 |
| ${}^{41}$Mg | 41 | 29 | 150.3903 | -429096346.37 | 38362.4040 | +2955492.50 | 13077.67 |

### Aluminium (Z = 13)

_3 of 23 isotopes with a framework prediction; 3 of 23 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{21}$Al | 21 | 8 | — | — | — | — | 30624.26 |
| ${}^{22}$Al | 22 | 9 | — | — | — | — | 19528.11 |
| ${}^{23}$Al | 23 | 10 | — | — | — | — | 16.08 |
| ${}^{24}$Al | 24 | 11 | — | — | — | — | 10.17 |
| ${}^{25}$Al | 25 | 12 | — | — | — | — | 2.76 |
| ${}^{26}$Al | 26 | 13 | — | — | — | — | 2.73 |
| ${}^{27}$Al | 27 | 14 | — | — | — | — | 1.85 |
| ${}^{28}$Al | 28 | 15 | — | — | — | — | 1.86 |
| ${}^{29}$Al | 29 | 16 | — | — | — | — | 12.77 |
| ${}^{30}$Al | 30 | 17 | — | — | — | — | 69.27 |
| ${}^{31}$Al | 31 | 18 | — | — | — | — | 77.46 |
| ${}^{32}$Al | 32 | 19 | — | — | — | — | 240.71 |
| ${}^{33}$Al | 33 | 20 | — | — | — | — | 227.34 |
| ${}^{34}$Al | 34 | 21 | — | — | — | — | 66.45 |
| ${}^{35}$Al | 35 | 22 | — | — | — | — | 225.72 |
| ${}^{36}$Al | 36 | 23 | — | — | — | — | 4457.54 |
| ${}^{37}$Al | 37 | 24 | — | — | — | — | 5228.24 |
| ${}^{38}$Al | 38 | 25 | — | — | — | — | 4234.87 |
| ${}^{39}$Al | 39 | 26 | — | — | — | — | 8251.53 |
| ${}^{40}$Al | 40 | 27 | — | — | — | — | 8043.78 |
| ${}^{41}$Al | 41 | 28 | 143.0450 | -500157143.57 | 38368.9670 | +3744026.86 | 10453.95 |
| ${}^{42}$Al | 42 | 29 | 148.4366 | -482471170.55 | 39303.1408 | +3533754.34 | 12772.01 |
| ${}^{43}$Al | 43 | 30 | 153.8222 | -467035157.15 | 40237.3207 | +3361488.96 | 14958.72 |

### Silicon (Z = 14)

_5 of 24 isotopes with a framework prediction; 5 of 24 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{22}$Si | 22 | 8 | — | — | — | — | 24369.09 |
| ${}^{23}$Si | 23 | 9 | — | — | — | — | 23321.76 |
| ${}^{24}$Si | 24 | 10 | — | — | — | — | 870.58 |
| ${}^{25}$Si | 25 | 11 | — | — | — | — | 429.33 |
| ${}^{26}$Si | 26 | 12 | — | — | — | — | 4.42 |
| ${}^{27}$Si | 27 | 13 | — | — | — | — | 4.26 |
| ${}^{28}$Si | 28 | 14 | — | — | — | — | 0.02 |
| ${}^{29}$Si | 29 | 15 | — | — | — | — | 0.02 |
| ${}^{30}$Si | 30 | 16 | — | — | — | — | 0.77 |
| ${}^{31}$Si | 31 | 17 | — | — | — | — | 1.49 |
| ${}^{32}$Si | 32 | 18 | — | — | — | — | 10.01 |
| ${}^{33}$Si | 33 | 19 | — | — | — | — | 22.74 |
| ${}^{34}$Si | 34 | 20 | — | — | — | — | 25.31 |
| ${}^{35}$Si | 35 | 21 | — | — | — | — | 1100.31 |
| ${}^{36}$Si | 36 | 22 | — | — | — | — | 2141.82 |
| ${}^{37}$Si | 37 | 23 | — | — | — | — | 3302.76 |
| ${}^{38}$Si | 38 | 24 | — | — | — | — | 2960.88 |
| ${}^{39}$Si | 39 | 25 | — | — | — | — | 3730.53 |
| ${}^{40}$Si | 40 | 26 | — | — | — | — | 3273.55 |
| ${}^{41}$Si | 41 | 27 | 135.2970 | -558951211.47 | 38375.9326 | +4488329.24 | 7850.94 |
| ${}^{42}$Si | 42 | 28 | 140.7259 | -547824991.30 | 39310.0692 | +4355621.85 | 7663.37 |
| ${}^{43}$Si | 43 | 29 | 146.1478 | -531266667.46 | 40244.2127 | +4132795.80 | 9970.69 |
| ${}^{44}$Si | 44 | 30 | 151.5629 | -518639968.07 | 41178.3630 | +3981758.26 | 12195.82 |
| ${}^{45}$Si | 45 | 31 | 156.9717 | -501961602.62 | 42112.5196 | +3770641.09 | 14298.46 |

### Phosphorus (Z = 15)

_7 of 24 isotopes with a framework prediction; 7 of 24 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{24}$P | 24 | 9 | — | — | — | — | 22341.00 |
| ${}^{25}$P | 25 | 10 | — | — | — | — | 17145.14 |
| ${}^{26}$P | 26 | 11 | — | — | — | — | 8073.27 |
| ${}^{27}$P | 27 | 12 | — | — | — | — | 357.86 |
| ${}^{28}$P | 28 | 13 | — | — | — | — | 43.98 |
| ${}^{29}$P | 29 | 14 | — | — | — | — | 13.28 |
| ${}^{30}$P | 30 | 15 | — | — | — | — | 2.30 |
| ${}^{31}$P | 31 | 16 | — | — | — | — | 0.03 |
| ${}^{32}$P | 32 | 17 | — | — | — | — | 1.31 |
| ${}^{33}$P | 33 | 18 | — | — | — | — | 35.48 |
| ${}^{34}$P | 34 | 19 | — | — | — | — | 25.61 |
| ${}^{35}$P | 35 | 20 | — | — | — | — | 57.27 |
| ${}^{36}$P | 36 | 21 | — | — | — | — | 391.29 |
| ${}^{37}$P | 37 | 22 | — | — | — | — | 1101.63 |
| ${}^{38}$P | 38 | 23 | — | — | — | — | 2051.32 |
| ${}^{39}$P | 39 | 24 | — | — | — | — | 3101.83 |
| ${}^{40}$P | 40 | 25 | — | — | — | — | 2244.37 |
| ${}^{41}$P | 41 | 26 | 127.1462 | -607777455.58 | 38383.3011 | +5159512.94 | 3146.75 |
| ${}^{42}$P | 42 | 27 | 132.6155 | -593414022.06 | 39317.3973 | +4947189.73 | 2428.41 |
| ${}^{43}$P | 43 | 28 | 138.0765 | -581944889.56 | 40251.5017 | +4798260.48 | 7487.43 |
| ${}^{44}$P | 44 | 29 | 143.5297 | -568056225.94 | 41185.6139 | +4604338.06 | 9747.36 |
| ${}^{45}$P | 45 | 30 | 148.9755 | -555986103.19 | 42119.7335 | +4448470.46 | 11928.79 |
| ${}^{46}$P | 46 | 31 | 154.4143 | -541416395.97 | 43053.8602 | +4252028.98 | 11667.69 |
| ${}^{47}$P | 47 | 32 | 159.8462 | -528230842.53 | 43987.9936 | +4085014.99 | 13693.12 |

### Sulfur (Z = 16)

_9 of 24 isotopes with a framework prediction; 9 of 24 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{26}$S | 26 | 10 | — | — | — | — | 24740.95 |
| ${}^{27}$S | 27 | 11 | — | — | — | — | 15914.86 |
| ${}^{28}$S | 28 | 12 | — | — | — | — | 6133.58 |
| ${}^{29}$S | 29 | 13 | — | — | — | — | 482.81 |
| ${}^{30}$S | 30 | 14 | — | — | — | — | 7.37 |
| ${}^{31}$S | 31 | 15 | — | — | — | — | 7.94 |
| ${}^{32}$S | 32 | 16 | — | — | — | — | 0.04 |
| ${}^{33}$S | 33 | 17 | — | — | — | — | 0.04 |
| ${}^{34}$S | 34 | 18 | — | — | — | — | 1.38 |
| ${}^{35}$S | 35 | 19 | — | — | — | — | 1.23 |
| ${}^{36}$S | 36 | 20 | — | — | — | — | 5.59 |
| ${}^{37}$S | 37 | 21 | — | — | — | — | 5.73 |
| ${}^{38}$S | 38 | 22 | — | — | — | — | 202.76 |
| ${}^{39}$S | 39 | 23 | — | — | — | — | 1377.21 |
| ${}^{40}$S | 40 | 24 | — | — | — | — | 106.92 |
| ${}^{41}$S | 41 | 25 | 118.5927 | -648525754.22 | 38391.0723 | +5732504.79 | 107.37 |
| ${}^{42}$S | 42 | 26 | 124.1053 | -639350066.60 | 39325.1252 | +5626132.22 | 71.46 |
| ${}^{43}$S | 43 | 27 | 129.6084 | -626213765.75 | 40259.1875 | +5422711.14 | 124.11 |
| ${}^{44}$S | 44 | 28 | 135.1025 | -615994902.12 | 41193.2588 | +5288940.31 | 127.30 |
| ${}^{45}$S | 45 | 29 | 140.5880 | -602875501.98 | 42127.3386 | +5092447.72 | 7156.13 |
| ${}^{46}$S | 46 | 30 | 146.0654 | -592121328.77 | 43061.4267 | +4948916.75 | 9325.95 |
| ${}^{47}$S | 47 | 31 | 151.5350 | -578652644.40 | 43995.5225 | +4752486.70 | 9126.16 |
| ${}^{48}$S | 48 | 32 | 156.9972 | -566899412.23 | 44929.6257 | +4595260.70 | 11184.40 |
| ${}^{49}$S | 49 | 33 | 162.4523 | -551979301.84 | 45863.7361 | +4382782.56 | 12769.81 |

### Chlorine (Z = 17)

_12 of 25 isotopes with a framework prediction; 12 of 25 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{28}$Cl | 28 | 11 | — | — | — | — | 19157.81 |
| ${}^{29}$Cl | 29 | 12 | — | — | — | — | 6996.37 |
| ${}^{30}$Cl | 30 | 13 | — | — | — | — | 854.22 |
| ${}^{31}$Cl | 31 | 14 | — | — | — | — | 119.38 |
| ${}^{32}$Cl | 32 | 15 | — | — | — | — | 18.85 |
| ${}^{33}$Cl | 33 | 16 | — | — | — | — | 12.71 |
| ${}^{34}$Cl | 34 | 17 | — | — | — | — | 1.53 |
| ${}^{35}$Cl | 35 | 18 | — | — | — | — | 1.09 |
| ${}^{36}$Cl | 36 | 19 | — | — | — | — | 1.06 |
| ${}^{37}$Cl | 37 | 20 | — | — | — | — | 1.49 |
| ${}^{38}$Cl | 38 | 21 | — | — | — | — | 2.77 |
| ${}^{39}$Cl | 39 | 22 | — | — | — | — | 47.71 |
| ${}^{40}$Cl | 40 | 23 | — | — | — | — | 861.21 |
| ${}^{41}$Cl | 41 | 24 | 109.6364 | -682149997.09 | 38399.2462 | +6165377.46 | 1800.73 |
| ${}^{42}$Cl | 42 | 25 | 115.1953 | -671365686.01 | 39333.2528 | +6019046.70 | 1524.78 |
| ${}^{43}$Cl | 43 | 26 | 120.7433 | -662658632.85 | 40267.2702 | +5925123.30 | 1545.28 |
| ${}^{44}$Cl | 44 | 27 | 126.2812 | -651462303.55 | 41201.2978 | +5761861.70 | 2088.75 |
| ${}^{45}$Cl | 45 | 28 | 131.8092 | -641990113.03 | 42135.3351 | +5641260.48 | 3249.79 |
| ${}^{46}$Cl | 46 | 29 | 137.3279 | -630556512.90 | 43069.3818 | +5471881.33 | 2270.29 |
| ${}^{47}$Cl | 47 | 30 | 142.8378 | -619731987.88 | 44003.4374 | +5318517.68 | 4575.47 |
| ${}^{48}$Cl | 48 | 31 | 148.3392 | -607966607.90 | 44937.5014 | +5146004.75 | 11188.57 |
| ${}^{49}$Cl | 49 | 32 | 153.8324 | -596732528.64 | 45871.5736 | +4986924.07 | 8754.96 |
| ${}^{50}$Cl | 50 | 33 | 159.3179 | -583536971.07 | 46805.6535 | +4792552.17 | 8578.58 |
| ${}^{51}$Cl | 51 | 34 | 164.7960 | -570877248.91 | 47739.7409 | +4613831.39 | 14721.06 |
| ${}^{52}$Cl | 52 | 35 | 170.2670 | -556679551.79 | 48673.8353 | +4411517.05 | 14435.64 |

### Argon (Z = 18)

_14 of 26 isotopes with a framework prediction; 14 of 26 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{29}$Ar | 29 | 11 | — | — | — | — | 16218.58 |
| ${}^{30}$Ar | 30 | 12 | — | — | — | — | 6394.95 |
| ${}^{31}$Ar | 31 | 13 | — | — | — | — | 6932.76 |
| ${}^{32}$Ar | 32 | 14 | — | — | — | — | 59.38 |
| ${}^{33}$Ar | 33 | 15 | — | — | — | — | 13.03 |
| ${}^{34}$Ar | 34 | 16 | — | — | — | — | 2.44 |
| ${}^{35}$Ar | 35 | 17 | — | — | — | — | 20.87 |
| ${}^{36}$Ar | 36 | 18 | — | — | — | — | 0.78 |
| ${}^{37}$Ar | 37 | 19 | — | — | — | — | 5.98 |
| ${}^{38}$Ar | 38 | 20 | — | — | — | — | 5.51 |
| ${}^{39}$Ar | 39 | 21 | — | — | — | — | 137.74 |
| ${}^{40}$Ar | 40 | 22 | — | — | — | — | 0.06 |
| ${}^{41}$Ar | 41 | 23 | 100.2774 | -713418913.28 | 38407.8229 | +6542034.04 | 9.08 |
| ${}^{42}$Ar | 42 | 24 | 105.8855 | -705329848.27 | 39341.7802 | +6484045.97 | 147.75 |
| ${}^{43}$Ar | 43 | 25 | 111.4815 | -694566503.78 | 40275.7497 | +6334304.75 | 132.66 |
| ${}^{44}$Ar | 44 | 26 | 117.0658 | -686762898.13 | 41209.7308 | +6267259.20 | 38.67 |
| ${}^{45}$Ar | 45 | 27 | 122.6391 | -676326866.25 | 42143.7229 | +6117798.90 | 12.23 |
| ${}^{46}$Ar | 46 | 28 | 128.2018 | -668703230.87 | 43077.7256 | +6043307.36 | 54.39 |
| ${}^{47}$Ar | 47 | 29 | 133.7545 | -657599049.56 | 44011.7384 | +5870954.79 | 27.68 |
| ${}^{48}$Ar | 48 | 30 | 139.2976 | -647968211.99 | 44945.7607 | +5737353.55 | 375.19 |
| ${}^{49}$Ar | 49 | 31 | 144.8315 | -636529259.74 | 45879.7922 | +5559124.88 | 8758.38 |
| ${}^{50}$Ar | 50 | 32 | 150.3566 | -626628782.18 | 46813.8325 | +5419874.56 | 10743.05 |
| ${}^{51}$Ar | 51 | 33 | 155.8733 | -614195965.23 | 47747.8812 | +5224698.35 | 8412.91 |
| ${}^{52}$Ar | 52 | 34 | 161.3820 | -603487937.71 | 48681.9380 | +5071073.73 | 12384.97 |
| ${}^{53}$Ar | 53 | 35 | 166.8830 | -589848252.32 | 49616.0024 | +4861156.26 | 14149.00 |
| ${}^{54}$Ar | 54 | 36 | 172.3765 | -578759902.00 | 50550.0743 | +4707159.21 | 15903.44 |

### Potassium (Z = 19)

_19 of 29 isotopes with a framework prediction; 19 of 29 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{31}$K | 31 | 12 | — | — | — | — | 10374.79 |
| ${}^{32}$K | 32 | 13 | — | — | — | — | 13396.37 |
| ${}^{33}$K | 33 | 14 | — | — | — | — | 6513.55 |
| ${}^{34}$K | 34 | 15 | — | — | — | — | 6176.71 |
| ${}^{35}$K | 35 | 16 | — | — | — | — | 15.72 |
| ${}^{36}$K | 36 | 17 | — | — | — | — | 9.70 |
| ${}^{37}$K | 37 | 18 | — | — | — | — | 2.70 |
| ${}^{38}$K | 38 | 19 | — | — | — | — | 5.50 |
| ${}^{39}$K | 39 | 20 | — | — | — | — | 0.13 |
| ${}^{40}$K | 40 | 21 | — | — | — | — | 1.50 |
| ${}^{41}$K | 41 | 22 | 90.5156 | -742574775.12 | 38416.8024 | +6843110.88 | 0.10 |
| ${}^{42}$K | 42 | 23 | 96.1760 | -732214189.64 | 39350.7074 | +6727867.09 | 2.69 |
| ${}^{43}$K | 43 | 24 | 101.8227 | -723891151.51 | 40284.6261 | +6670928.83 | 10.24 |
| ${}^{44}$K | 44 | 25 | 107.4564 | -714253488.29 | 41218.5579 | +6559195.97 | 10.24 |
| ${}^{45}$K | 45 | 26 | 113.0776 | -706261694.45 | 42152.5021 | +6491858.29 | 12.46 |
| ${}^{46}$K | 46 | 27 | 118.6870 | -697095673.32 | 43086.4581 | +6379867.13 | 16.97 |
| ${}^{47}$K | 47 | 28 | 124.2851 | -689442044.94 | 44020.4254 | +6307409.34 | 31.94 |
| ${}^{48}$K | 48 | 29 | 129.8724 | -679203175.41 | 44954.4035 | +6154309.25 | 17.30 |
| ${}^{49}$K | 49 | 30 | 135.4494 | -669830069.70 | 45888.3920 | +6024351.83 | 17.56 |
| ${}^{50}$K | 50 | 31 | 141.0166 | -659733040.35 | 46822.3902 | +5873660.73 | 166.09 |
| ${}^{51}$K | 51 | 32 | 146.5743 | -650421110.47 | 47756.3979 | +5743322.54 | 274.64 |
| ${}^{52}$K | 52 | 33 | 152.1229 | -639503376.62 | 48690.4147 | +5573230.79 | 692.55 |
| ${}^{53}$K | 53 | 34 | 157.6629 | -629212463.51 | 49624.4401 | +5420688.67 | 2264.71 |
| ${}^{54}$K | 54 | 35 | 163.1946 | -617016533.59 | 50558.4739 | +5227949.32 | 7945.26 |
| ${}^{55}$K | 55 | 36 | 168.7183 | -606313440.73 | 51492.5156 | +5072341.51 | 9763.55 |
| ${}^{56}$K | 56 | 37 | 174.2343 | -593980510.67 | 52426.5650 | +4886084.15 | 11498.24 |
| ${}^{57}$K | 57 | 38 | 179.7430 | -583050978.72 | 53360.6218 | +4732279.60 | 11295.24 |
| ${}^{58}$K | 58 | 39 | 185.2445 | -570543118.01 | 54294.6857 | +4553263.75 | 12943.02 |
| ${}^{59}$K | 59 | 40 | 190.7392 | -559074203.09 | 55228.7564 | +4398404.35 | 14551.71 |

### Calcium (Z = 20)

_22 of 29 isotopes with a framework prediction; 22 of 29 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{33}$Ca | 33 | 13 | — | — | — | — | 12986.89 |
| ${}^{34}$Ca | 34 | 14 | — | — | — | — | 9466.14 |
| ${}^{35}$Ca | 35 | 15 | — | — | — | — | 6141.88 |
| ${}^{36}$Ca | 36 | 16 | — | — | — | — | 1193.04 |
| ${}^{37}$Ca | 37 | 17 | — | — | — | — | 18.39 |
| ${}^{38}$Ca | 38 | 18 | — | — | — | — | 5.48 |
| ${}^{39}$Ca | 39 | 19 | — | — | — | — | 16.42 |
| ${}^{40}$Ca | 40 | 20 | 408.7713 | +195055373.81 | 37158.1989 | -1792316.22 | 0.55 |
| ${}^{41}$Ca | 41 | 21 | 80.3511 | -770697446.64 | 38426.1846 | +7077874.89 | 3.59 |
| ${}^{42}$Ca | 42 | 22 | 86.0667 | -762178041.01 | 39360.0343 | +7057307.63 | 3.79 |
| ${}^{43}$Ca | 43 | 23 | 91.7671 | -751865829.73 | 40293.8994 | +6948793.43 | 5.68 |
| ${}^{44}$Ca | 44 | 24 | 97.4529 | -744191081.48 | 41227.7790 | +6924220.60 | 7.92 |
| ${}^{45}$Ca | 45 | 25 | 103.1248 | -734470703.97 | 42161.6725 | +6811710.49 | 8.72 |
| ${}^{46}$Ca | 46 | 26 | 108.7835 | -727204552.57 | 43095.5792 | +6774583.95 | 52.18 |
| ${}^{47}$Ca | 47 | 27 | 114.4296 | -718188077.01 | 44029.4985 | +6667454.96 | 50.77 |
| ${}^{48}$Ca | 48 | 28 | 120.0637 | -711386162.32 | 44963.4299 | +6625350.53 | 0.38 |
| ${}^{49}$Ca | 49 | 29 | 125.6863 | -701562477.32 | 45897.3728 | +6479151.43 | 3.88 |
| ${}^{50}$Ca | 50 | 30 | 131.2978 | -692876485.41 | 46831.3266 | +6365315.09 | 34.03 |
| ${}^{51}$Ca | 51 | 31 | 136.8988 | -683340981.99 | 47765.2910 | +6223401.62 | 10.99 |
| ${}^{52}$Ca | 52 | 32 | 142.4898 | -674924196.26 | 48699.2655 | +6111930.66 | 13.86 |
| ${}^{53}$Ca | 53 | 33 | 148.0710 | -664633900.07 | 49633.2497 | +5947528.79 | 887.32 |
| ${}^{54}$Ca | 54 | 34 | 153.6430 | -655017580.92 | 50567.2431 | +5802467.85 | 963.44 |
| ${}^{55}$Ca | 55 | 35 | 159.2061 | -643775186.23 | 51501.2455 | +5618049.66 | 3128.41 |
| ${}^{56}$Ca | 56 | 36 | 164.7606 | -633749124.79 | 52435.2564 | +5466847.20 | 4786.95 |
| ${}^{57}$Ca | 57 | 37 | 170.3069 | -622365997.77 | 53369.2755 | +5286844.32 | 7527.25 |
| ${}^{58}$Ca | 58 | 38 | 175.8452 | -612696138.84 | 54303.3026 | +5148993.18 | 9258.88 |
| ${}^{59}$Ca | 59 | 39 | 181.3760 | -601171625.88 | 55237.3373 | +4973721.34 | 10914.10 |
| ${}^{60}$Ca | 60 | 40 | 186.8994 | -591583934.86 | 56171.3793 | +4843111.83 | 12514.20 |
| ${}^{61}$Ca | 61 | 41 | 192.4157 | -579587486.27 | 57105.4284 | +4667091.49 | 14077.26 |

### Scandium (Z = 21)

_23 of 29 isotopes with a framework prediction; 23 of 29 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{35}$Sc | 35 | 14 | — | — | — | — | 12246.96 |
| ${}^{36}$Sc | 36 | 15 | — | — | — | — | 8940.14 |
| ${}^{37}$Sc | 37 | 16 | — | — | — | — | 8701.75 |
| ${}^{38}$Sc | 38 | 17 | — | — | — | — | 5658.57 |
| ${}^{39}$Sc | 39 | 18 | — | — | — | — | 660.90 |
| ${}^{40}$Sc | 40 | 19 | — | — | — | — | 75.94 |
| ${}^{41}$Sc | 41 | 20 | 69.7838 | -796630105.55 | 38435.9696 | +7162864.86 | 2.03 |
| ${}^{42}$Sc | 42 | 21 | 75.5577 | -786973613.32 | 39369.7610 | +7140577.33 | 3.93 |
| ${}^{43}$Sc | 43 | 22 | 81.3146 | -778328852.80 | 40303.5695 | +7134559.26 | 46.53 |
| ${}^{44}$Sc | 44 | 23 | 87.0554 | -768792369.23 | 41237.3942 | +7069214.41 | 42.86 |
| ${}^{45}$Sc | 45 | 24 | 92.7808 | -760783318.95 | 42171.2343 | +7046297.69 | 15.84 |
| ${}^{46}$Sc | 46 | 25 | 98.4914 | -751668656.91 | 43105.0890 | +6964330.37 | 15.67 |
| ${}^{47}$Sc | 47 | 26 | 104.1881 | -744172627.27 | 44038.9577 | +6929588.37 | 44.13 |
| ${}^{48}$Sc | 48 | 27 | 109.8715 | -735566850.54 | 44972.8398 | +6842309.92 | 110.80 |
| ${}^{49}$Sc | 49 | 28 | 115.5420 | -728537360.90 | 45906.7347 | +6800632.00 | 49.72 |
| ${}^{50}$Sc | 50 | 29 | 121.2004 | -719231489.45 | 46840.6417 | +6672523.91 | 54.05 |
| ${}^{51}$Sc | 51 | 30 | 126.8471 | -710697525.24 | 47774.5605 | +6565363.98 | 52.99 |
| ${}^{52}$Sc | 52 | 31 | 132.4825 | -701483305.27 | 48708.4904 | +6432619.54 | 63.51 |
| ${}^{53}$Sc | 53 | 32 | 138.1073 | -693176793.32 | 49642.4311 | +6324964.51 | 358.77 |
| ${}^{54}$Sc | 54 | 33 | 143.7218 | -683334486.30 | 50576.3821 | +6169913.73 | 277.97 |
| ${}^{55}$Sc | 55 | 34 | 149.3263 | -674198526.51 | 51510.3429 | +6035180.92 | 1218.92 |
| ${}^{56}$Sc | 56 | 35 | 154.9214 | -664003500.22 | 52444.3133 | +5872077.90 | 4980.31 |
| ${}^{57}$Sc | 57 | 36 | 160.5073 | -654834450.03 | 53378.2927 | +5737455.71 | 3387.33 |
| ${}^{58}$Sc | 58 | 37 | 166.0845 | -644500857.72 | 54312.2810 | +5574819.49 | 3518.25 |
| ${}^{59}$Sc | 59 | 38 | 171.6532 | -635252346.32 | 55246.2777 | +5440759.68 | 4543.27 |
| ${}^{60}$Sc | 60 | 39 | 177.2137 | -624849229.77 | 56180.2826 | +5282029.92 | 8950.73 |
| ${}^{61}$Sc | 61 | 40 | 182.7664 | -615579842.18 | 57114.2954 | +5150411.20 | 10557.28 |
| ${}^{62}$Sc | 62 | 41 | 188.3115 | -604932001.67 | 58048.3157 | +4992575.08 | 10385.78 |
| ${}^{63}$Sc | 63 | 42 | 193.8493 | -595294794.40 | 58982.3433 | +4857896.97 | 11917.98 |

### Titanium (Z = 22)

_25 of 29 isotopes with a framework prediction; 25 of 29 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{37}$Ti | 37 | 15 | — | — | — | — | 11586.13 |
| ${}^{38}$Ti | 38 | 16 | — | — | — | — | 8470.96 |
| ${}^{39}$Ti | 39 | 17 | — | — | — | — | 5512.44 |
| ${}^{40}$Ti | 40 | 18 | — | — | — | — | 1831.99 |
| ${}^{41}$Ti | 41 | 19 | 58.8137 | -821457401.79 | 38446.1573 | +7088214.30 | 732.01 |
| ${}^{42}$Ti | 42 | 20 | 64.6489 | -813631828.60 | 39379.8875 | +7218835.77 | 6.89 |
| ${}^{43}$Ti | 43 | 21 | 70.4653 | -803811090.15 | 40313.6365 | +7213145.72 | 142.87 |
| ${}^{44}$Ti | 44 | 22 | 76.2638 | -796887044.32 | 41247.4034 | +7307073.35 | 17.08 |
| ${}^{45}$Ti | 45 | 23 | 82.0454 | -786899584.83 | 42181.1873 | +7234378.22 | 19.95 |
| ${}^{46}$Ti | 46 | 24 | 87.8107 | -779479453.78 | 43114.9874 | +7251251.21 | 2.11 |
| ${}^{47}$Ti | 47 | 25 | 93.5606 | -770165496.05 | 44048.8030 | +7168529.85 | 1.81 |
| ${}^{48}$Ti | 48 | 26 | 99.2957 | -762850270.46 | 44982.6333 | +7151504.12 | 1.65 |
| ${}^{49}$Ti | 49 | 27 | 105.0167 | -753971044.36 | 45916.4776 | +7058516.68 | 1.72 |
| ${}^{50}$Ti | 50 | 28 | 110.7243 | -747081371.77 | 46850.3355 | +7030077.02 | 1.76 |
| ${}^{51}$Ti | 51 | 29 | 116.4189 | -737888810.79 | 47784.2063 | +6906117.96 | 10.19 |
| ${}^{52}$Ti | 52 | 30 | 122.1012 | -729849362.20 | 48718.0894 | +6817232.25 | 56.75 |
| ${}^{53}$Ti | 53 | 31 | 127.7717 | -720686895.65 | 49651.9844 | +6684162.37 | 58.55 |
| ${}^{54}$Ti | 54 | 32 | 133.4308 | -712671060.28 | 50585.8907 | +6585480.41 | 315.10 |
| ${}^{55}$Ti | 55 | 33 | 139.0790 | -703167348.95 | 51519.8079 | +6436071.35 | 564.10 |
| ${}^{56}$Ti | 56 | 34 | 144.7167 | -694822691.37 | 52453.7357 | +6321220.32 | 1922.33 |
| ${}^{57}$Ti | 57 | 35 | 150.3443 | -684981463.67 | 53387.6735 | +6161076.19 | 3880.06 |
| ${}^{58}$Ti | 58 | 36 | 155.9622 | -676321176.77 | 54321.6210 | +6035302.18 | 3395.44 |
| ${}^{59}$Ti | 59 | 37 | 161.5708 | -666769510.57 | 55255.5778 | +5885526.89 | 5460.20 |
| ${}^{60}$Ti | 60 | 38 | 167.1704 | -658255044.10 | 56189.5436 | +5763580.08 | 4301.70 |
| ${}^{61}$Ti | 61 | 39 | 172.7613 | -648529016.41 | 57123.5181 | +5611286.46 | 5280.21 |
| ${}^{62}$Ti | 62 | 40 | 178.3439 | -639985613.24 | 58057.5009 | +5491234.65 | 6920.82 |
| ${}^{63}$Ti | 63 | 41 | 183.9184 | -630041766.96 | 58991.4918 | +5337978.34 | 8524.66 |
| ${}^{64}$Ti | 64 | 42 | 189.4852 | -621683369.14 | 59925.4905 | +5222720.86 | 10062.75 |
| ${}^{65}$Ti | 65 | 43 | 195.0444 | -611612345.69 | 60859.4967 | +5072804.90 | 11552.85 |

### Vanadium (Z = 23)

_27 of 29 isotopes with a framework prediction; 27 of 29 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{39}$V | 39 | 16 | — | — | — | — | 10993.17 |
| ${}^{40}$V | 40 | 17 | — | — | — | — | 8047.31 |
| ${}^{41}$V | 41 | 18 | 47.4409 | -848249812.51 | 38456.7477 | +6943399.05 | 5243.86 |
| ${}^{42}$V | 42 | 19 | 53.3403 | -837677955.25 | 39390.4137 | +7037711.21 | 5000.97 |
| ${}^{43}$V | 43 | 20 | 59.2191 | -829334430.54 | 40324.1004 | +7187729.25 | 1070.25 |
| ${}^{44}$V | 44 | 21 | 65.0782 | -819704030.52 | 41257.8067 | +7223150.87 | 177.35 |
| ${}^{45}$V | 45 | 22 | 70.9186 | -811937662.62 | 42191.5317 | +7310037.53 | 20.59 |
| ${}^{46}$V | 46 | 23 | 76.7413 | -803410268.78 | 43125.2745 | +7325613.32 | 3.11 |
| ${}^{47}$V | 47 | 24 | 82.5469 | -795354313.03 | 44059.0343 | +7334969.05 | 2.51 |
| ${}^{48}$V | 48 | 25 | 88.3364 | -786579374.47 | 44992.8102 | +7288815.75 | 21.75 |
| ${}^{49}$V | 49 | 26 | 94.1103 | -778804833.97 | 45926.6017 | +7267265.81 | 18.06 |
| ${}^{50}$V | 50 | 27 | 99.8695 | -770306894.23 | 46860.4080 | +7198765.85 | 1.98 |
| ${}^{51}$V | 51 | 28 | 105.6144 | -763114750.82 | 47794.2284 | +7169728.38 | 2.04 |
| ${}^{52}$V | 52 | 29 | 111.3458 | -754288966.62 | 48728.0625 | +7064240.57 | 3.27 |
| ${}^{53}$V | 53 | 30 | 117.0642 | -746415338.33 | 49661.9095 | +6986867.50 | 62.92 |
| ${}^{54}$V | 54 | 31 | 122.7701 | -737533579.91 | 50595.7690 | +6865280.11 | 222.46 |
| ${}^{55}$V | 55 | 32 | 128.4640 | -729579983.86 | 51529.6405 | +6771577.17 | 527.78 |
| ${}^{56}$V | 56 | 33 | 134.1464 | -720634944.87 | 52463.5236 | +6639559.68 | 3374.76 |
| ${}^{57}$V | 57 | 34 | 139.8177 | -712608508.92 | 53397.4177 | +6535043.34 | 1597.83 |
| ${}^{58}$V | 58 | 35 | 145.4784 | -703452059.98 | 54331.3224 | +6392277.94 | 1774.81 |
| ${}^{59}$V | 59 | 36 | 151.1289 | -695196813.90 | 55265.2374 | +6276265.39 | 2501.80 |
| ${}^{60}$V | 60 | 37 | 156.7694 | -686067191.16 | 56199.1623 | +6133629.56 | 3257.38 |
| ${}^{61}$V | 61 | 38 | 162.4005 | -678117628.44 | 57133.0966 | +6024434.52 | 4136.56 |
| ${}^{62}$V | 62 | 39 | 168.0223 | -669013439.08 | 58067.0402 | +5883147.56 | 4578.18 |
| ${}^{63}$V | 63 | 40 | 173.6353 | -661026867.83 | 59000.9926 | +5772083.85 | 5795.80 |
| ${}^{64}$V | 64 | 41 | 179.2398 | -651880468.06 | 59934.9536 | +5631789.37 | 6704.96 |
| ${}^{65}$V | 65 | 42 | 184.8360 | -643699966.27 | 60868.9228 | +5516087.88 | 8263.19 |
| ${}^{66}$V | 66 | 43 | 190.4242 | -634505283.29 | 61802.9000 | +5377849.72 | 8137.20 |
| ${}^{67}$V | 67 | 44 | 196.0047 | -626332415.28 | 62736.8849 | +5264097.95 | 9612.21 |

### Chromium (Z = 24)

_30 of 30 isotopes with a framework prediction; 30 of 30 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{41}$Cr | 41 | 17 | 35.6653 | -877756264.09 | 38467.7410 | +6701428.04 | 10457.83 |
| ${}^{42}$Cr | 42 | 18 | 41.6320 | -867055035.67 | 39401.3397 | +6939149.06 | 7665.28 |
| ${}^{43}$Cr | 43 | 19 | 47.5760 | -855935054.28 | 40334.9611 | +7057895.87 | 5000.25 |
| ${}^{44}$Cr | 44 | 20 | 53.4985 | -847052451.47 | 41268.6040 | +7231354.78 | 1250.41 |
| ${}^{45}$Cr | 45 | 21 | 59.4006 | -836788086.21 | 42202.2674 | +7268832.75 | 844.84 |
| ${}^{46}$Cr | 46 | 22 | 65.2832 | -829090763.95 | 43135.9502 | +7396041.82 | 267.47 |
| ${}^{47}$Cr | 47 | 23 | 71.1472 | -819943706.57 | 44069.6516 | +7406262.76 | 118.77 |
| ${}^{48}$Cr | 48 | 24 | 76.9935 | -812881106.67 | 45003.3708 | +7487875.25 | 163.66 |
| ${}^{49}$Cr | 49 | 25 | 82.8228 | -803760945.57 | 45937.1069 | +7439559.87 | 48.27 |
| ${}^{50}$Cr | 50 | 26 | 88.6359 | -796263082.48 | 46870.8592 | +7445878.45 | 2.00 |
| ${}^{51}$Cr | 51 | 27 | 94.4336 | -787460972.59 | 47804.6270 | +7372885.01 | 3.49 |
| ${}^{52}$Cr | 52 | 28 | 100.2163 | -780396741.53 | 48738.4096 | +7360872.48 | 2.31 |
| ${}^{53}$Cr | 53 | 29 | 105.9849 | -771727596.29 | 49672.2065 | +7265834.72 | 2.34 |
| ${}^{54}$Cr | 54 | 30 | 111.7397 | -764267259.06 | 50606.0171 | +7210267.54 | 2.63 |
| ${}^{55}$Cr | 55 | 31 | 117.4815 | -755377601.76 | 51539.8407 | +7088631.38 | 4.46 |
| ${}^{56}$Cr | 56 | 32 | 123.2107 | -747778903.91 | 52473.6770 | +7010240.44 | 11.08 |
| ${}^{57}$Cr | 57 | 33 | 128.9277 | -738914286.78 | 53407.5253 | +6879115.14 | 35.12 |
| ${}^{58}$Cr | 58 | 34 | 134.6331 | -731459813.90 | 54341.3854 | +6794282.84 | 55.23 |
| ${}^{59}$Cr | 59 | 35 | 140.3273 | -722424940.47 | 55275.2566 | +6651250.18 | 12.21 |
| ${}^{60}$Cr | 60 | 36 | 146.0107 | -715051644.04 | 56209.1386 | +6561298.53 | 20.02 |
| ${}^{61}$Cr | 61 | 37 | 151.6837 | -706079463.36 | 57143.0310 | +6417680.55 | 32.81 |
| ${}^{62}$Cr | 62 | 38 | 157.3467 | -698856835.80 | 58076.9335 | +6327159.80 | 59.72 |
| ${}^{63}$Cr | 63 | 39 | 163.0000 | -690052243.50 | 59010.8456 | +6187691.04 | 1238.86 |
| ${}^{64}$Cr | 64 | 40 | 168.6439 | -682658979.02 | 59944.7671 | +6088828.36 | 5034.09 |
| ${}^{65}$Cr | 65 | 41 | 174.2788 | -673739062.16 | 60878.6976 | +5946760.94 | 3309.24 |
| ${}^{66}$Cr | 66 | 42 | 179.9050 | -666279015.14 | 61812.6369 | +5844521.77 | 4880.78 |
| ${}^{67}$Cr | 67 | 43 | 185.5227 | -657260089.20 | 62746.5846 | +5701950.52 | 6404.96 |
| ${}^{68}$Cr | 68 | 44 | 191.1323 | -649792055.48 | 63680.5404 | +5600100.70 | 7899.02 |
| ${}^{69}$Cr | 69 | 45 | 196.7340 | -640859441.11 | 64614.5042 | +5462525.52 | 7783.77 |
| ${}^{70}$Cr | 70 | 46 | 202.3280 | -633384078.61 | 65548.4756 | +5360953.29 | 9200.80 |

### Manganese (Z = 25)

_31 of 31 isotopes with a framework prediction; 31 of 31 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{43}$Mn | 43 | 18 | 35.5361 | -885426300.87 | 40346.2188 | +6852798.86 | 9972.42 |
| ${}^{44}$Mn | 44 | 19 | 41.5248 | -873441612.92 | 41279.7954 | +6991269.69 | 7316.85 |
| ${}^{45}$Mn | 45 | 20 | 47.4913 | -863771568.22 | 42213.3944 | +7184998.54 | 7156.41 |
| ${}^{46}$Mn | 46 | 21 | 53.4365 | -853252783.02 | 43147.0146 | +7253275.76 | 2022.33 |
| ${}^{47}$Mn | 47 | 22 | 59.3614 | -844749710.63 | 44080.6551 | +7381532.54 | 723.78 |
| ${}^{48}$Mn | 48 | 23 | 65.2671 | -835666055.41 | 45014.3149 | +7427854.72 | 149.91 |
| ${}^{49}$Mn | 49 | 24 | 71.1542 | -827945287.76 | 45947.9931 | +7507894.56 | 48.55 |
| ${}^{50}$Mn | 50 | 25 | 77.0237 | -819461861.04 | 46881.6890 | +7513327.65 | 2.46 |
| ${}^{51}$Mn | 51 | 26 | 82.8763 | -811782349.70 | 47815.4019 | +7531841.61 | 6.40 |
| ${}^{52}$Mn | 52 | 27 | 88.7127 | -803237153.55 | 48749.1309 | +7484427.81 | 2.66 |
| ${}^{53}$Mn | 53 | 28 | 94.5336 | -795784641.97 | 49682.8754 | +7469978.96 | 7.01 |
| ${}^{54}$Mn | 54 | 29 | 100.3397 | -787348726.89 | 50616.6348 | +7393980.32 | 20.02 |
| ${}^{55}$Mn | 55 | 30 | 106.1314 | -779845261.87 | 51550.4085 | +7346346.46 | 5.08 |
| ${}^{56}$Mn | 56 | 31 | 111.9094 | -771308605.75 | 52484.1959 | +7243547.36 | 5.61 |
| ${}^{57}$Mn | 57 | 32 | 117.6742 | -763702938.98 | 53417.9965 | +7170730.38 | 28.36 |
| ${}^{58}$Mn | 58 | 33 | 123.4263 | -755303255.84 | 54351.8098 | +7058986.60 | 50.05 |
| ${}^{59}$Mn | 59 | 34 | 129.1663 | -747808072.13 | 55285.6353 | +6976142.31 | 42.42 |
| ${}^{60}$Mn | 60 | 35 | 134.8944 | -739429331.51 | 56219.4726 | +6855607.12 | 41.71 |
| ${}^{61}$Mn | 61 | 36 | 140.6112 | -731931114.28 | 57153.3212 | +6762851.78 | 41.02 |
| ${}^{62}$Mn | 62 | 37 | 146.3171 | -723610370.67 | 58087.1808 | +6638527.18 | 113.37 |
| ${}^{63}$Mn | 63 | 38 | 152.0124 | -716300250.03 | 59021.0509 | +6545488.62 | 63.54 |
| ${}^{64}$Mn | 64 | 39 | 157.6975 | -707964652.76 | 59954.9312 | +6417335.13 | 59.42 |
| ${}^{65}$Mn | 65 | 40 | 163.3729 | -700806623.63 | 60888.8213 | +6324512.07 | 61.58 |
| ${}^{66}$Mn | 66 | 41 | 169.0387 | -692600385.73 | 61822.7209 | +6198712.67 | 181.93 |
| ${}^{67}$Mn | 67 | 42 | 174.6953 | -685135617.76 | 62756.6297 | +6093720.69 | 3210.68 |
| ${}^{68}$Mn | 68 | 43 | 180.3430 | -676927438.00 | 63690.5474 | +5968290.37 | 4737.46 |
| ${}^{69}$Mn | 69 | 44 | 185.9821 | -669479739.07 | 64624.4737 | +5863871.99 | 6219.85 |
| ${}^{70}$Mn | 70 | 45 | 191.6129 | -661389542.34 | 65558.4083 | +5741751.37 | 7673.84 |
| ${}^{71}$Mn | 71 | 46 | 197.2356 | -654051523.66 | 66492.3511 | +5639631.60 | 7565.28 |
| ${}^{72}$Mn | 72 | 47 | 202.8505 | -645836816.61 | 67426.3016 | +5516186.67 | 8945.93 |
| ${}^{73}$Mn | 73 | 48 | 208.4578 | -638304415.38 | 68360.2597 | +5410759.27 | 8822.79 |

### Iron (Z = 26)

_32 of 32 isotopes with a framework prediction; 32 of 32 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{45}$Fe | 45 | 19 | 35.1906 | -892860146.47 | 42224.9127 | +6994017.13 | 6753.23 |
| ${}^{46}$Fe | 46 | 20 | 41.2011 | -882194332.16 | 43158.4676 | +7200216.88 | 6999.80 |
| ${}^{47}$Fe | 47 | 21 | 47.1896 | -871112401.36 | 44092.0446 | +7286470.23 | 11427.39 |
| ${}^{48}$Fe | 48 | 22 | 53.1571 | -861962127.52 | 45025.6425 | +7426863.65 | 2063.33 |
| ${}^{49}$Fe | 49 | 23 | 59.1046 | -852203235.92 | 45959.2605 | +7470662.23 | 530.90 |
| ${}^{50}$Fe | 50 | 24 | 65.0328 | -844307835.72 | 46892.8976 | +7577721.51 | 180.13 |
| ${}^{51}$Fe | 51 | 25 | 70.9427 | -835584838.64 | 47826.5531 | +7595814.84 | 29.46 |
| ${}^{52}$Fe | 52 | 26 | 76.8351 | -828378060.04 | 48760.2262 | +7664182.91 | 3.70 |
| ${}^{53}$Fe | 53 | 27 | 82.7106 | -819561443.44 | 49693.9161 | +7617387.26 | 33.85 |
| ${}^{54}$Fe | 54 | 28 | 88.5699 | -812258348.54 | 50627.6222 | +7626622.03 | 6.82 |
| ${}^{55}$Fe | 55 | 29 | 94.4137 | -803739352.35 | 51561.3438 | +7555483.54 | 6.01 |
| ${}^{56}$Fe | 56 | 30 | 100.2426 | -796362404.40 | 52495.0803 | +7523889.83 | 5.13 |
| ${}^{57}$Fe | 57 | 31 | 106.0572 | -787845713.83 | 53428.8312 | +7426216.96 | 5.04 |
| ${}^{58}$Fe | 58 | 32 | 111.8580 | -780649298.83 | 54362.5958 | +7376942.60 | 5.85 |
| ${}^{59}$Fe | 59 | 33 | 117.6456 | -772239348.09 | 55296.3737 | +7266024.57 | 6.01 |
| ${}^{60}$Fe | 60 | 34 | 123.4204 | -765070736.68 | 56230.1643 | +7199426.22 | 61.00 |
| ${}^{61}$Fe | 61 | 35 | 129.1829 | -756685667.11 | 57163.9672 | +7077725.67 | 45.95 |
| ${}^{62}$Fe | 62 | 36 | 134.9335 | -749640481.23 | 58097.7821 | +7002936.11 | 48.44 |
| ${}^{63}$Fe | 63 | 37 | 140.6726 | -741309668.92 | 59031.6083 | +6875759.72 | 73.37 |
| ${}^{64}$Fe | 64 | 38 | 146.4007 | -734392973.18 | 59965.4457 | +6796308.53 | 84.23 |
| ${}^{65}$Fe | 65 | 39 | 152.1181 | -726166182.91 | 60899.2937 | +6668135.04 | 84.49 |
| ${}^{66}$Fe | 66 | 40 | 157.8252 | -719388803.49 | 61833.1520 | +6586660.92 | 66.72 |
| ${}^{67}$Fe | 67 | 41 | 163.5224 | -711165601.78 | 62767.0203 | +6455987.16 | 61.24 |
| ${}^{68}$Fe | 68 | 42 | 169.2098 | -704397731.65 | 63700.8982 | +6369833.54 | 3046.23 |
| ${}^{69}$Fe | 69 | 43 | 174.8880 | -696272220.94 | 64634.7855 | +6241120.63 | 3117.84 |
| ${}^{70}$Fe | 70 | 44 | 180.5571 | -689529757.95 | 65568.6818 | +6153117.92 | 4602.60 |
| ${}^{71}$Fe | 71 | 45 | 186.2174 | -681508133.54 | 66502.5869 | +6027386.88 | 6045.17 |
| ${}^{72}$Fe | 72 | 46 | 191.8693 | -674819887.09 | 67436.5005 | +5939510.66 | 7461.59 |
| ${}^{73}$Fe | 73 | 47 | 197.5129 | -666832136.88 | 68370.4223 | +5815990.10 | 7358.76 |
| ${}^{74}$Fe | 74 | 48 | 203.1486 | -660072964.11 | 69304.3520 | +5724111.41 | 7258.93 |
| ${}^{75}$Fe | 75 | 49 | 208.7765 | -651865158.34 | 70238.2895 | +5596942.96 | 8588.47 |
| ${}^{76}$Fe | 76 | 50 | 214.3969 | -644843092.23 | 71172.2346 | +5499527.57 | 8474.95 |

### Cobalt (Z = 27)

_32 of 32 isotopes with a framework prediction; 32 of 32 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{47}$Co | 47 | 20 | 34.6317 | -900372475.64 | 44103.8201 | +7147094.21 | 13698.80 |
| ${}^{48}$Co | 48 | 21 | 40.6636 | -888458362.62 | 45037.3536 | +7244059.79 | 11187.07 |
| ${}^{49}$Co | 49 | 22 | 46.6738 | -878504261.67 | 45970.9089 | +7395401.76 | 10961.53 |
| ${}^{50}$Co | 50 | 23 | 52.6632 | -868352442.89 | 46904.4849 | +7461138.73 | 2701.02 |
| ${}^{51}$Co | 51 | 24 | 58.6328 | -859681836.64 | 47838.0807 | +7565969.87 | 1020.20 |
| ${}^{52}$Co | 52 | 25 | 64.5833 | -850822423.46 | 48771.6956 | +7609932.45 | 109.10 |
| ${}^{53}$Co | 53 | 26 | 70.5156 | -843060019.57 | 49705.3288 | +7679450.57 | 35.01 |
| ${}^{54}$Co | 54 | 27 | 76.4304 | -834829957.74 | 50638.9794 | +7687309.38 | 7.04 |
| ${}^{55}$Co | 55 | 28 | 82.3285 | -827341800.85 | 51572.6468 | +7708389.05 | 7.90 |
| ${}^{56}$Co | 56 | 29 | 88.2104 | -818836787.00 | 52506.3303 | +7651489.96 | 9.12 |
| ${}^{57}$Co | 57 | 30 | 94.0767 | -811199828.67 | 53440.0293 | +7621473.16 | 9.71 |
| ${}^{58}$Co | 58 | 31 | 99.9282 | -802848594.20 | 54373.7433 | +7540422.14 | 21.35 |
| ${}^{59}$Co | 59 | 32 | 105.7654 | -795549086.35 | 55307.4715 | +7496900.47 | 7.23 |
| ${}^{60}$Co | 60 | 33 | 111.5887 | -787371623.09 | 56241.2137 | +7401624.69 | 7.22 |
| ${}^{61}$Co | 61 | 34 | 117.3987 | -780203835.32 | 57174.9691 | +7342139.64 | 14.79 |
| ${}^{62}$Co | 62 | 35 | 123.1958 | -772164530.00 | 58108.7374 | +7237278.08 | 321.96 |
| ${}^{63}$Co | 63 | 36 | 128.9806 | -765157326.12 | 59042.5180 | +7168623.69 | 316.86 |
| ${}^{64}$Co | 64 | 37 | 134.7534 | -757303196.14 | 59976.3107 | +7060273.59 | 335.90 |
| ${}^{65}$Co | 65 | 38 | 140.5146 | -750283908.45 | 60910.1148 | +6979628.52 | 34.42 |
| ${}^{66}$Co | 66 | 39 | 146.2647 | -742488163.72 | 61843.9302 | +6866049.23 | 227.48 |
| ${}^{67}$Co | 67 | 40 | 152.0040 | -735634526.13 | 62777.7563 | +6783331.05 | 103.33 |
| ${}^{68}$Co | 68 | 41 | 157.7328 | -727750558.26 | 63711.5929 | +6661979.82 | 60.96 |
| ${}^{69}$Co | 69 | 42 | 163.4516 | -721159458.85 | 64645.4395 | +6582279.94 | 1334.38 |
| ${}^{70}$Co | 70 | 43 | 169.1606 | -713478457.84 | 65579.2960 | +6464797.97 | 168.69 |
| ${}^{71}$Co | 71 | 44 | 174.8601 | -706763243.80 | 66513.1619 | +6376752.74 | 7036.13 |
| ${}^{72}$Co | 72 | 45 | 180.5504 | -699251146.16 | 67447.0370 | +6262551.15 | 4474.91 |
| ${}^{73}$Co | 73 | 46 | 186.2318 | -692710163.86 | 68380.9211 | +6177372.77 | 4413.42 |
| ${}^{74}$Co | 74 | 47 | 191.9046 | -685240342.32 | 69314.8137 | +6063982.33 | 5800.12 |
| ${}^{75}$Co | 75 | 48 | 197.5690 | -678632080.38 | 70248.7147 | +5974630.53 | 5722.50 |
| ${}^{76}$Co | 76 | 49 | 203.2252 | -671133154.11 | 71182.6239 | +5860452.17 | 7068.35 |
| ${}^{77}$Co | 77 | 50 | 208.8736 | -664359750.72 | 72116.5409 | +5765502.12 | 8366.19 |
| ${}^{78}$Co | 78 | 51 | 214.5143 | -656098047.25 | 73050.4656 | +5633795.75 | 9630.24 |

### Nickel (Z = 28)

_35 of 35 isotopes with a framework prediction; 35 of 35 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{48}$Ni | 48 | 20 | 27.7866 | -919999026.25 | 45049.4484 | +7144064.73 | 9475.31 |
| ${}^{49}$Ni | 49 | 21 | 33.8620 | -907240220.78 | 45982.9384 | +7254873.87 | 13140.40 |
| ${}^{50}$Ni | 50 | 22 | 39.9149 | -896351770.40 | 46916.4508 | +7412411.26 | 10740.80 |
| ${}^{51}$Ni | 51 | 23 | 45.9465 | -885525894.14 | 47849.9847 | +7483714.24 | 10531.99 |
| ${}^{52}$Ni | 52 | 24 | 51.9575 | -876398444.97 | 48783.5391 | +7609306.75 | 1712.34 |
| ${}^{53}$Ni | 53 | 25 | 57.9488 | -866938799.50 | 49717.1132 | +7652208.20 | 509.74 |
| ${}^{54}$Ni | 54 | 26 | 63.9213 | -858963101.86 | 50650.7062 | +7745563.74 | 92.66 |
| ${}^{55}$Ni | 55 | 27 | 69.8756 | -850486334.89 | 51584.3173 | +7765228.86 | 13.78 |
| ${}^{56}$Ni | 56 | 28 | 75.8126 | -843361088.35 | 52517.9457 | +7833150.07 | 7.65 |
| ${}^{57}$Ni | 57 | 29 | 81.7328 | -834630486.69 | 53451.5909 | +7777491.58 | 10.68 |
| ${}^{58}$Ni | 58 | 30 | 87.6369 | -826961679.03 | 54385.2522 | +7760807.99 | 6.46 |
| ${}^{59}$Ni | 59 | 31 | 93.5256 | -818558624.57 | 55318.9290 | +7685916.58 | 6.38 |
| ${}^{60}$Ni | 60 | 32 | 99.3993 | -811331603.88 | 56252.6207 | +7656899.13 | 6.31 |
| ${}^{61}$Ni | 61 | 33 | 105.2587 | -803132174.78 | 57186.3268 | +7565746.49 | 6.25 |
| ${}^{62}$Ni | 62 | 34 | 111.1042 | -796237230.25 | 58120.0467 | +7526254.48 | 7.35 |
| ${}^{63}$Ni | 63 | 35 | 116.9363 | -788197275.72 | 59053.7799 | +7423653.64 | 7.26 |
| ${}^{64}$Ni | 64 | 36 | 122.7556 | -781479494.76 | 59987.5261 | +7372181.41 | 7.77 |
| ${}^{65}$Ni | 65 | 37 | 128.5624 | -773600338.83 | 60921.2848 | +7263216.94 | 7.98 |
| ${}^{66}$Ni | 66 | 38 | 134.3571 | -767067743.85 | 61855.0555 | +7204561.71 | 22.75 |
| ${}^{67}$Ni | 67 | 39 | 140.1402 | -759463599.21 | 62788.8378 | +7097054.30 | 46.32 |
| ${}^{68}$Ni | 68 | 40 | 145.9120 | -752862286.66 | 63722.6314 | +7024482.25 | 47.11 |
| ${}^{69}$Ni | 69 | 41 | 151.6730 | -745084851.58 | 64656.4359 | +6903906.73 | 58.03 |
| ${}^{70}$Ni | 70 | 42 | 157.4233 | -738629865.34 | 65590.2509 | +6828996.06 | 32.90 |
| ${}^{71}$Ni | 71 | 43 | 163.1635 | -731003683.95 | 66524.0761 | +6709995.25 | 33.85 |
| ${}^{72}$Ni | 72 | 44 | 168.8938 | -724684440.60 | 67457.9113 | +6633930.49 | 33.37 |
| ${}^{73}$Ni | 73 | 45 | 174.6144 | -717181743.15 | 68391.7561 | +6516577.09 | 35.66 |
| ${}^{74}$Ni | 74 | 46 | 180.3258 | -711035798.86 | 69325.6101 | +6442143.14 | 2907.46 |
| ${}^{75}$Ni | 75 | 47 | 186.0281 | -703623495.96 | 70259.4732 | +6325832.58 | 2868.48 |
| ${}^{76}$Ni | 76 | 48 | 191.7217 | -697450985.91 | 71193.3451 | +6246994.50 | 4239.37 |
| ${}^{77}$Ni | 77 | 49 | 197.4067 | -690072086.39 | 72127.2255 | +6131172.06 | 5574.33 |
| ${}^{78}$Ni | 78 | 50 | 203.0835 | -683948209.95 | 73061.1141 | +6051277.47 | 5502.64 |
| ${}^{79}$Ni | 79 | 51 | 208.7522 | -675775031.26 | 73995.0108 | +5915406.99 | 6800.07 |
| ${}^{80}$Ni | 80 | 52 | 214.4132 | -668624534.87 | 74928.9153 | +5807360.81 | 8052.51 |
| ${}^{81}$Ni | 81 | 53 | 220.0665 | -660391168.40 | 75862.8274 | +5672367.42 | 9273.58 |
| ${}^{82}$Ni | 82 | 54 | 225.7125 | -653107597.77 | 76796.7468 | +5564226.21 | 10477.08 |

### Copper (Z = 29)

_33 of 33 isotopes with a framework prediction; 33 of 33 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{52}$Cu | 52 | 23 | 38.9576 | -902335584.89 | 48795.7567 | +7431341.96 | 12385.10 |
| ${}^{53}$Cu | 53 | 24 | 45.0101 | -892377655.32 | 49729.2696 | +7561823.62 | 10134.77 |
| ${}^{54}$Cu | 54 | 25 | 51.0424 | -882507151.05 | 50662.8027 | +7624608.16 | 7947.80 |
| ${}^{55}$Cu | 55 | 26 | 57.0552 | -874014119.39 | 51596.3553 | +7730681.08 | 3038.24 |
| ${}^{56}$Cu | 56 | 27 | 63.0493 | -865260763.75 | 52529.9267 | +7767603.30 | 122.66 |
| ${}^{57}$Cu | 57 | 28 | 69.0253 | -857587539.80 | 53463.5161 | +7835588.58 | 9.43 |
| ${}^{58}$Cu | 58 | 29 | 74.9841 | -849161843.33 | 54397.1227 | +7820891.87 | 10.42 |
| ${}^{59}$Cu | 59 | 30 | 80.9262 | -841283263.76 | 55330.7460 | +7813085.07 | 9.60 |
| ${}^{60}$Cu | 60 | 31 | 86.8523 | -832955964.98 | 56264.3854 | +7757018.85 | 28.88 |
| ${}^{61}$Cu | 61 | 32 | 92.7629 | -825517766.43 | 57198.0402 | +7732390.76 | 16.74 |
| ${}^{62}$Cu | 62 | 33 | 98.6585 | -817475165.52 | 58131.7100 | +7659286.83 | 11.03 |
| ${}^{63}$Cu | 63 | 34 | 104.5399 | -810404921.01 | 59065.3941 | +7622935.54 | 7.26 |
| ${}^{64}$Cu | 64 | 35 | 110.4073 | -802597635.95 | 59999.0921 | +7538074.96 | 7.16 |
| ${}^{65}$Cu | 65 | 36 | 116.2613 | -795750175.13 | 60932.8035 | +7489277.66 | 10.63 |
| ${}^{66}$Cu | 66 | 37 | 122.1024 | -788118686.16 | 61866.5278 | +7395503.61 | 10.56 |
| ${}^{67}$Cu | 67 | 38 | 127.9309 | -781467752.82 | 62800.2647 | +7338127.59 | 14.30 |
| ${}^{68}$Cu | 68 | 39 | 133.7474 | -773971802.62 | 63734.0137 | +7237838.35 | 25.03 |
| ${}^{69}$Cu | 69 | 40 | 139.5521 | -767401255.55 | 64667.7744 | +7170790.08 | 21.76 |
| ${}^{70}$Cu | 70 | 41 | 145.3454 | -759871000.83 | 65601.5465 | +7060549.92 | 16.60 |
| ${}^{71}$Cu | 71 | 42 | 151.1278 | -753496852.48 | 66535.3295 | +6991610.97 | 22.56 |
| ${}^{72}$Cu | 72 | 43 | 156.8995 | -746211689.02 | 67469.1232 | +6884733.19 | 20.85 |
| ${}^{73}$Cu | 73 | 44 | 162.6609 | -739952928.64 | 68402.9273 | +6812549.00 | 28.57 |
| ${}^{74}$Cu | 74 | 45 | 168.4123 | -732931443.76 | 69336.7413 | +6710516.39 | 89.26 |
| ${}^{75}$Cu | 75 | 46 | 174.1539 | -726659131.85 | 70270.5651 | +6632194.64 | 10.27 |
| ${}^{76}$Cu | 76 | 47 | 179.8862 | -719678468.83 | 71204.3983 | +6528289.82 | 12.90 |
| ${}^{77}$Cu | 77 | 48 | 185.6093 | -713418362.63 | 72138.2406 | +6446457.11 | 16.89 |
| ${}^{78}$Cu | 78 | 49 | 191.3234 | -706407936.40 | 73072.0918 | +6339762.03 | 183.60 |
| ${}^{79}$Cu | 79 | 50 | 197.0290 | -700269627.62 | 74005.9517 | +6259047.35 | 1427.40 |
| ${}^{80}$Cu | 80 | 51 | 202.7261 | -692690186.73 | 74939.8200 | +6135253.14 | 4026.98 |
| ${}^{81}$Cu | 81 | 52 | 208.4151 | -685641275.00 | 75873.6964 | +6027440.61 | 3976.99 |
| ${}^{82}$Cu | 82 | 53 | 214.0962 | -677981159.75 | 76807.5808 | +5903784.79 | 5233.47 |
| ${}^{83}$Cu | 83 | 54 | 219.7695 | -670832307.07 | 77741.4729 | +5794174.47 | 6471.59 |
| ${}^{84}$Cu | 84 | 55 | 225.4353 | -663056740.68 | 78675.3726 | +5670173.88 | 6393.98 |

### Zinc (Z = 30)

_33 of 33 isotopes with a framework prediction; 33 of 33 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{54}$Zn | 54 | 24 | 37.7939 | -909598761.78 | 50675.2689 | +7561172.27 | 4296.78 |
| ${}^{55}$Zn | 55 | 25 | 43.8672 | -899090885.28 | 51608.7610 | +7631215.20 | 7802.17 |
| ${}^{56}$Zn | 56 | 26 | 49.9205 | -890027530.60 | 52542.2732 | +7748493.17 | 7664.44 |
| ${}^{57}$Zn | 57 | 27 | 55.9544 | -880736704.13 | 53475.8047 | +7786855.03 | 3774.24 |
| ${}^{58}$Zn | 58 | 28 | 61.9698 | -872742847.66 | 54409.3547 | +7872568.72 | 926.21 |
| ${}^{59}$Zn | 59 | 29 | 67.9673 | -864052719.08 | 55342.9227 | +7867034.22 | 13.81 |
| ${}^{60}$Zn | 60 | 30 | 73.9475 | -856407869.54 | 56276.5078 | +7898850.69 | 9.81 |
| ${}^{61}$Zn | 61 | 31 | 79.9112 | -847854508.76 | 57210.1095 | +7844970.74 | 280.08 |
| ${}^{62}$Zn | 62 | 32 | 85.8589 | -840446384.54 | 58143.7273 | +7839304.00 | 10.66 |
| ${}^{63}$Zn | 63 | 33 | 91.7912 | -832264066.37 | 59077.3605 | +7769199.38 | 26.60 |
| ${}^{64}$Zn | 64 | 34 | 97.7085 | -825239014.26 | 60011.0085 | +7747990.74 | 10.79 |
| ${}^{65}$Zn | 65 | 35 | 103.6115 | -817288596.96 | 60944.6710 | +7662979.71 | 10.67 |
| ${}^{66}$Zn | 66 | 36 | 109.5006 | -810597161.74 | 61878.3473 | +7631296.07 | 12.10 |
| ${}^{67}$Zn | 67 | 37 | 115.3762 | -802839177.33 | 62812.0371 | +7536024.29 | 12.10 |
| ${}^{68}$Zn | 68 | 38 | 121.2388 | -796369468.76 | 63745.7399 | +7493852.45 | 12.29 |
| ${}^{69}$Zn | 69 | 39 | 127.0889 | -788842711.83 | 64679.4552 | +7394788.28 | 12.38 |
| ${}^{70}$Zn | 70 | 40 | 132.9268 | -782474697.98 | 65613.1828 | +7341062.21 | 29.43 |
| ${}^{71}$Zn | 71 | 41 | 138.7529 | -775088419.50 | 66546.9221 | +7237453.34 | 40.17 |
| ${}^{72}$Zn | 72 | 42 | 144.5676 | -768991282.27 | 67480.6728 | +7182790.56 | 31.98 |
| ${}^{73}$Zn | 73 | 43 | 150.3712 | -761818165.84 | 68414.4347 | +7079845.54 | 27.42 |
| ${}^{74}$Zn | 74 | 44 | 156.1640 | -755827350.12 | 69348.2073 | +7019554.99 | 36.52 |
| ${}^{75}$Zn | 75 | 45 | 161.9464 | -748701060.68 | 70281.9903 | +6912533.71 | 28.03 |
| ${}^{76}$Zn | 76 | 46 | 167.7187 | -742862373.14 | 71215.7834 | +6850359.84 | 20.57 |
| ${}^{77}$Zn | 77 | 47 | 173.4812 | -735873166.33 | 72149.5863 | +6744171.38 | 27.52 |
| ${}^{78}$Zn | 78 | 48 | 179.2342 | -729896401.17 | 73083.3988 | +6671463.09 | 26.76 |
| ${}^{79}$Zn | 79 | 49 | 184.9778 | -722919487.34 | 74017.2205 | +6563150.08 | 30.25 |
| ${}^{80}$Zn | 80 | 50 | 190.7125 | -716994894.00 | 74951.0513 | +6488322.19 | 34.70 |
| ${}^{81}$Zn | 81 | 51 | 196.4384 | -709627974.44 | 75884.8908 | +6366543.14 | 66.71 |
| ${}^{82}$Zn | 82 | 52 | 202.1558 | -703014108.89 | 76818.7388 | +6268470.13 | 40.27 |
| ${}^{83}$Zn | 83 | 53 | 207.8649 | -695551118.71 | 77752.5951 | +6145039.16 | 3881.34 |
| ${}^{84}$Zn | 84 | 54 | 213.5659 | -688844493.66 | 78686.4595 | +6044785.87 | 5109.22 |
| ${}^{85}$Zn | 85 | 55 | 219.2591 | -681147224.72 | 79620.3318 | +5918152.61 | 6319.65 |
| ${}^{86}$Zn | 86 | 56 | 224.9446 | -674348198.30 | 80554.2117 | +5815825.75 | 6245.75 |

### Gallium (Z = 31)

_33 of 33 isotopes with a framework prediction; 33 of 33 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{56}$Ga | 56 | 25 | 36.4261 | -915600503.32 | 52554.9852 | +7575848.51 | 9589.99 |
| ${}^{57}$Ga | 57 | 26 | 42.5200 | -905764956.65 | 53488.4567 | +7699782.15 | 7528.50 |
| ${}^{58}$Ga | 58 | 27 | 48.5939 | -896038416.30 | 54421.9482 | +7755663.16 | 5554.14 |
| ${}^{59}$Ga | 59 | 28 | 54.6487 | -887481794.65 | 55355.4588 | +7848368.29 | 3103.60 |
| ${}^{60}$Ga | 60 | 29 | 60.6851 | -878537443.32 | 56288.9879 | +7859115.09 | 3585.87 |
| ${}^{61}$Ga | 61 | 30 | 66.7037 | -870536566.65 | 57222.5347 | +7900253.11 | 669.19 |
| ${}^{62}$Ga | 62 | 31 | 72.7052 | -862341345.32 | 58156.0986 | +7893346.35 | 11.04 |
| ${}^{63}$Ga | 63 | 32 | 78.6902 | -854489537.08 | 59089.6790 | +7881914.97 | 22.24 |
| ${}^{64}$Ga | 64 | 33 | 84.6593 | -846393696.54 | 60023.2754 | +7832618.63 | 23.98 |
| ${}^{65}$Ga | 65 | 34 | 90.6129 | -839065020.12 | 60956.8872 | +7810733.02 | 13.08 |
| ${}^{66}$Ga | 66 | 35 | 96.5517 | -831255898.83 | 61890.5139 | +7744486.50 | 17.78 |
| ${}^{67}$Ga | 67 | 36 | 102.4760 | -824348293.84 | 62824.1549 | +7714216.38 | 18.86 |
| ${}^{68}$Ga | 68 | 37 | 108.3865 | -816816587.09 | 63757.8099 | +7638097.30 | 22.60 |
| ${}^{69}$Ga | 69 | 38 | 114.2835 | -810159038.23 | 64691.4783 | +7596329.66 | 18.64 |
| ${}^{70}$Ga | 70 | 39 | 120.1675 | -802890938.85 | 65625.1598 | +7514816.28 | 18.43 |
| ${}^{71}$Ga | 71 | 40 | 126.0388 | -796366704.25 | 66558.8538 | +7460903.11 | 12.27 |
| ${}^{72}$Ga | 72 | 41 | 131.8979 | -789122027.13 | 67492.5601 | +7366871.86 | 12.21 |
| ${}^{73}$Ga | 73 | 42 | 137.7452 | -782959759.21 | 68426.2783 | +7315069.61 | 24.68 |
| ${}^{74}$Ga | 74 | 43 | 143.5810 | -776030739.84 | 69360.0080 | +7224451.75 | 43.48 |
| ${}^{75}$Ga | 75 | 44 | 149.4056 | -769988426.56 | 70293.7488 | +7166153.56 | 9.61 |
| ${}^{76}$Ga | 76 | 45 | 155.2193 | -763191674.24 | 71227.5004 | +7072877.07 | 27.66 |
| ${}^{77}$Ga | 77 | 46 | 161.0226 | -757214910.86 | 72161.2626 | +7008311.02 | 33.80 |
| ${}^{78}$Ga | 78 | 47 | 166.8157 | -750654479.91 | 73095.0349 | +6918023.26 | 14.46 |
| ${}^{79}$Ga | 79 | 48 | 172.5988 | -744649761.50 | 74028.8172 | +6845672.23 | 16.42 |
| ${}^{80}$Ga | 80 | 49 | 178.3723 | -737948421.49 | 74962.6091 | +6745936.92 | 38.82 |
| ${}^{81}$Ga | 81 | 50 | 184.1364 | -732029527.49 | 75896.4104 | +6671884.27 | 43.28 |
| ${}^{82}$Ga | 82 | 51 | 189.8914 | -725004668.03 | 76830.2209 | +6558860.19 | 31.78 |
| ${}^{83}$Ga | 83 | 52 | 195.6376 | -718476213.82 | 77764.0402 | +6462023.74 | 33.80 |
| ${}^{84}$Ga | 84 | 53 | 201.3751 | -711427621.53 | 78697.8681 | +6348446.88 | 381.17 |
| ${}^{85}$Ga | 85 | 54 | 207.1042 | -704791999.24 | 79631.7044 | +6248001.08 | 470.82 |
| ${}^{86}$Ga | 86 | 55 | 212.8251 | -697542163.52 | 80565.5489 | +6129475.98 | 4990.48 |
| ${}^{87}$Ga | 87 | 56 | 218.5380 | -690801218.08 | 81499.4014 | +6027372.73 | 6174.61 |
| ${}^{88}$Ga | 88 | 57 | 224.2431 | -683451236.71 | 82433.2617 | +5908191.11 | 6103.94 |

### Germanium (Z = 32)

_33 of 33 isotopes with a framework prediction; 33 of 33 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{58}$Ge | 58 | 26 | 34.8566 | -922654355.25 | 54434.9032 | +7697739.31 | 9259.92 |
| ${}^{59}$Ge | 59 | 27 | 40.9707 | -912365228.35 | 55368.3546 | +7764082.76 | 7273.35 |
| ${}^{60}$Ge | 60 | 28 | 47.0650 | -903313526.03 | 56301.8256 | +7871340.02 | 5369.31 |
| ${}^{61}$Ge | 61 | 29 | 53.1405 | -893955565.04 | 57235.3156 | +7888469.00 | 5281.83 |
| ${}^{62}$Ge | 62 | 30 | 59.1976 | -885611628.25 | 58168.8239 | +7941871.96 | 2421.12 |
| ${}^{63}$Ge | 63 | 31 | 65.2371 | -876999184.94 | 59102.3499 | +7932549.55 | 635.43 |
| ${}^{64}$Ge | 64 | 32 | 71.2595 | -869450933.56 | 60035.8928 | +7968020.20 | 62.56 |
| ${}^{65}$Ge | 65 | 33 | 77.2655 | -861052905.56 | 60969.4522 | +7915501.31 | 35.77 |
| ${}^{66}$Ge | 66 | 34 | 83.2557 | -853752442.72 | 61903.0275 | +7913504.65 | 39.08 |
| ${}^{67}$Ge | 67 | 35 | 89.2304 | -845733402.03 | 62836.6182 | +7846144.96 | 69.26 |
| ${}^{68}$Ge | 68 | 36 | 95.1903 | -838877136.65 | 63770.2237 | +7832579.32 | 29.65 |
| ${}^{69}$Ge | 69 | 37 | 101.1358 | -831155070.61 | 64703.8436 | +7753967.08 | 20.51 |
| ${}^{70}$Ge | 70 | 38 | 107.0674 | -824628868.71 | 65637.4775 | +7729481.26 | 12.59 |
| ${}^{71}$Ge | 71 | 39 | 112.9856 | -817156265.88 | 66571.1247 | +7643094.88 | 12.32 |
| ${}^{72}$Ge | 72 | 40 | 118.8906 | -810890192.89 | 67504.7851 | +7609457.85 | 1.13 |
| ${}^{73}$Ge | 73 | 41 | 124.7830 | -803636205.82 | 68438.4581 | +7518075.04 | 0.84 |
| ${}^{74}$Ge | 74 | 42 | 130.6632 | -797630066.15 | 69372.1434 | +7479285.26 | 0.18 |
| ${}^{75}$Ge | 75 | 43 | 136.5314 | -790650872.50 | 70305.8406 | +7388427.38 | 0.73 |
| ${}^{76}$Ge | 76 | 44 | 142.3880 | -784781651.34 | 71239.5494 | +7341741.16 | 0.25 |
| ${}^{77}$Ge | 77 | 45 | 148.2334 | -777983715.59 | 72173.2694 | +7249246.36 | 0.73 |
| ${}^{78}$Ge | 78 | 46 | 154.0680 | -772220131.66 | 73107.0003 | +7196040.36 | 48.70 |
| ${}^{79}$Ge | 79 | 47 | 159.8919 | -765597773.41 | 74040.7418 | +7103446.53 | 505.45 |
| ${}^{80}$Ge | 80 | 48 | 165.7055 | -759918607.64 | 74974.4936 | +7045005.41 | 27.59 |
| ${}^{81}$Ge | 81 | 49 | 171.5092 | -753236075.74 | 75908.2554 | +6944704.52 | 27.25 |
| ${}^{82}$Ge | 82 | 50 | 177.3030 | -747513582.58 | 76842.0269 | +6878215.80 | 29.35 |
| ${}^{83}$Ge | 83 | 51 | 183.0875 | -740618158.46 | 77775.8079 | +6767032.14 | 31.40 |
| ${}^{84}$Ge | 84 | 52 | 188.8626 | -734409261.32 | 78709.5982 | +6679364.93 | 40.54 |
| ${}^{85}$Ge | 85 | 53 | 194.6289 | -727467942.62 | 79643.3974 | +6565931.93 | 47.13 |
| ${}^{86}$Ge | 86 | 54 | 200.3863 | -721103900.15 | 80577.2053 | +6471623.71 | 5468.49 |
| ${}^{87}$Ge | 87 | 55 | 206.1353 | -714016747.65 | 81511.0218 | +6353677.16 | 3703.14 |
| ${}^{88}$Ge | 88 | 56 | 211.8760 | -707663751.37 | 82444.8465 | +6259889.02 | 4877.35 |
| ${}^{89}$Ge | 89 | 57 | 217.6085 | -700399502.83 | 83378.6794 | +6139069.13 | 4822.15 |
| ${}^{90}$Ge | 90 | 58 | 223.3332 | -693984441.95 | 84312.5201 | +6043970.48 | 5968.69 |

### Arsenic (Z = 33)

_33 of 33 isotopes with a framework prediction; 33 of 33 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{60}$As | 60 | 27 | 33.0873 | -928706562.17 | 56315.0210 | +7712672.21 | 7150.72 |
| ${}^{61}$As | 61 | 28 | 39.2213 | -918918924.72 | 57248.4524 | +7825374.70 | 5280.29 |
| ${}^{62}$As | 62 | 29 | 45.3359 | -909153370.88 | 58181.9033 | +7859049.17 | 5195.75 |
| ${}^{63}$As | 63 | 30 | 51.4317 | -900356890.41 | 59115.3729 | +7923949.75 | 3414.65 |
| ${}^{64}$As | 64 | 31 | 57.5093 | -891554078.48 | 60048.8607 | +7935577.64 | 3408.51 |
| ${}^{65}$As | 65 | 32 | 63.5694 | -883520326.93 | 60982.3660 | +7969998.85 | 1401.09 |
| ${}^{66}$As | 66 | 33 | 69.6126 | -875450472.68 | 61915.8883 | +7965647.90 | 92.50 |
| ${}^{67}$As | 67 | 34 | 75.6393 | -867658841.44 | 62849.4270 | +7953187.82 | 7.10 |
| ${}^{68}$As | 68 | 35 | 81.6503 | -859689742.38 | 63782.9814 | +7905428.59 | 29.16 |
| ${}^{69}$As | 69 | 36 | 87.6459 | -852501510.96 | 64716.5512 | +7889275.77 | 498.34 |
| ${}^{70}$As | 70 | 37 | 93.6267 | -844862722.88 | 65650.1358 | +7827457.47 | 21.45 |
| ${}^{71}$As | 71 | 38 | 99.5931 | -838096629.74 | 66583.7348 | +7803252.22 | 63.01 |
| ${}^{72}$As | 72 | 39 | 105.5456 | -830733520.05 | 67517.3478 | +7731450.07 | 60.94 |
| ${}^{73}$As | 73 | 40 | 111.4847 | -824251349.40 | 68450.9742 | +7697215.39 | 56.72 |
| ${}^{74}$As | 74 | 41 | 117.4106 | -817208600.70 | 69384.6137 | +7622891.37 | 24.58 |
| ${}^{75}$As | 75 | 42 | 123.3238 | -811016954.53 | 70318.2658 | +7583459.88 | 12.65 |
| ${}^{76}$As | 76 | 43 | 129.2248 | -804173499.27 | 71251.9303 | +7503681.91 | 12.53 |
| ${}^{77}$As | 77 | 44 | 135.1137 | -798214378.90 | 72185.6068 | +7459437.96 | 23.61 |
| ${}^{78}$As | 78 | 45 | 140.9910 | -791606712.36 | 73119.2949 | +7378675.97 | 134.72 |
| ${}^{79}$As | 79 | 46 | 146.8571 | -785751686.05 | 74052.9943 | +7326403.63 | 72.43 |
| ${}^{80}$As | 80 | 47 | 152.7122 | -779350376.37 | 74986.7046 | +7245270.35 | 44.77 |
| ${}^{81}$As | 81 | 48 | 158.5566 | -773649883.14 | 75920.4256 | +7189538.31 | 35.07 |
| ${}^{82}$As | 82 | 49 | 164.3906 | -767196955.60 | 76854.1570 | +7099054.06 | 48.86 |
| ${}^{83}$As | 83 | 50 | 170.2146 | -761527861.03 | 77787.8985 | +7036854.79 | 36.23 |
| ${}^{84}$As | 84 | 51 | 176.0287 | -754843868.69 | 78721.6498 | +6932733.07 | 40.55 |
| ${}^{85}$As | 85 | 52 | 181.8332 | -748652538.64 | 79655.4107 | +6845846.59 | 38.90 |
| ${}^{86}$As | 86 | 53 | 187.6285 | -742012742.73 | 80589.1809 | +6741452.18 | 43.09 |
| ${}^{87}$As | 87 | 54 | 193.4146 | -735774213.57 | 81522.9601 | +6650555.05 | 36.85 |
| ${}^{88}$As | 88 | 55 | 199.1920 | -728949237.82 | 82456.7482 | +6539429.50 | 2444.69 |
| ${}^{89}$As | 89 | 56 | 204.9607 | -722672362.20 | 83390.5449 | +6446085.12 | 3620.01 |
| ${}^{90}$As | 90 | 57 | 210.7210 | -715856318.88 | 84324.3501 | +6335470.61 | 4769.00 |
| ${}^{91}$As | 91 | 58 | 216.4731 | -709509730.77 | 85258.1634 | +6239855.44 | 4716.32 |
| ${}^{92}$As | 92 | 59 | 222.2172 | -702573082.16 | 86191.9847 | +6127288.47 | 5839.03 |

### Selenium (Z = 34)

_33 of 33 isotopes with a framework prediction; 33 of 33 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{63}$Se | 63 | 29 | 37.2741 | -925268145.66 | 59128.7482 | +7865874.40 | 8526.26 |
| ${}^{64}$Se | 64 | 30 | 43.4086 | -916005018.13 | 60062.1791 | +7944720.64 | 8394.41 |
| ${}^{65}$Se | 65 | 31 | 49.5245 | -906742325.88 | 60995.6286 | +7957343.94 | 4956.55 |
| ${}^{66}$Se | 66 | 32 | 55.6224 | -898462293.95 | 61929.0962 | +8010577.82 | 3259.78 |
| ${}^{67}$Se | 67 | 33 | 61.7028 | -889965509.82 | 62862.5811 | +8002377.91 | 1075.43 |
| ${}^{68}$Se | 68 | 34 | 67.7664 | -882439619.06 | 63796.0830 | +8037512.64 | 7.83 |
| ${}^{69}$Se | 69 | 35 | 73.8137 | -874200258.58 | 64729.6011 | +7987687.87 | 23.19 |
| ${}^{70}$Se | 70 | 36 | 79.8453 | -866996001.81 | 65663.1349 | +7989812.06 | 24.31 |
| ${}^{71}$Se | 71 | 37 | 85.8615 | -859153407.36 | 66596.6841 | +7926835.18 | 42.29 |
| ${}^{72}$Se | 72 | 38 | 91.8630 | -852406005.95 | 67530.2481 | +7918554.04 | 29.20 |
| ${}^{73}$Se | 73 | 39 | 97.8501 | -844887688.25 | 68463.8264 | +7845982.90 | 109.27 |
| ${}^{74}$Se | 74 | 40 | 103.8233 | -838505615.86 | 69397.4186 | +7828653.61 | 0.20 |
| ${}^{75}$Se | 75 | 41 | 109.7830 | -831341472.93 | 70331.0244 | +7753789.26 | 1.04 |
| ${}^{76}$Se | 76 | 42 | 115.7295 | -825201056.88 | 71264.6432 | +7725628.23 | 0.22 |
| ${}^{77}$Se | 77 | 43 | 121.6634 | -818274823.82 | 72198.2748 | +7645846.14 | 0.87 |
| ${}^{78}$Se | 78 | 44 | 127.5849 | -812372088.03 | 73131.9187 | +7611025.86 | 2.45 |
| ${}^{79}$Se | 79 | 45 | 133.4944 | -805671358.80 | 74065.5746 | +7528798.22 | 3.02 |
| ${}^{80}$Se | 80 | 46 | 139.3922 | -799972430.83 | 74999.2422 | +7488717.85 | 12.71 |
| ${}^{81}$Se | 81 | 47 | 145.2787 | -793510873.73 | 75932.9211 | +7406838.91 | 12.96 |
| ${}^{82}$Se | 82 | 48 | 151.1542 | -787955620.86 | 76866.6111 | +7361104.52 | 6.10 |
| ${}^{83}$Se | 83 | 49 | 157.0189 | -781511617.04 | 77800.3118 | +7271510.00 | 39.30 |
| ${}^{84}$Se | 84 | 50 | 162.8732 | -776069701.61 | 78734.0230 | +7221046.43 | 25.08 |
| ${}^{85}$Se | 85 | 51 | 168.7173 | -769472854.42 | 79667.7443 | +7119171.86 | 33.02 |
| ${}^{86}$Se | 86 | 52 | 174.5514 | -763492191.85 | 80601.4755 | +7040229.24 | 31.48 |
| ${}^{87}$Se | 87 | 53 | 180.3760 | -756915832.17 | 81535.2164 | +6936282.98 | 27.67 |
| ${}^{88}$Se | 88 | 54 | 186.1911 | -750935004.43 | 82468.9667 | +6853696.18 | 40.99 |
| ${}^{89}$Se | 89 | 55 | 191.9971 | -744256171.39 | 83402.7262 | +6744525.15 | 45.01 |
| ${}^{90}$Se | 90 | 56 | 197.7941 | -738235641.05 | 84336.4945 | +6658322.91 | 3935.95 |
| ${}^{91}$Se | 91 | 57 | 203.5825 | -731588087.31 | 85270.2716 | +6550030.40 | 5112.94 |
| ${}^{92}$Se | 92 | 58 | 209.3623 | -725491322.56 | 86204.0572 | +6460230.11 | 4665.59 |
| ${}^{93}$Se | 93 | 59 | 215.1338 | -718751768.63 | 87137.8511 | +6349135.05 | 4615.08 |
| ${}^{94}$Se | 94 | 60 | 220.8972 | -712717535.89 | 88071.6531 | +6261287.87 | 5715.17 |
| ${}^{95}$Se | 95 | 61 | 226.6528 | -705890224.95 | 89005.4630 | +6149377.56 | 5654.58 |

### Bromine (Z = 35)

_34 of 34 isotopes with a framework prediction; 34 of 34 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{65}$Br | 65 | 30 | 35.1308 | -931620199.69 | 61009.2400 | +7906963.73 | 8263.79 |
| ${}^{66}$Br | 66 | 31 | 41.2851 | -921945190.82 | 61942.6511 | +7934416.39 | 6502.49 |
| ${}^{67}$Br | 67 | 32 | 47.4208 | -913135300.14 | 62876.0808 | +7991741.86 | 4808.48 |
| ${}^{68}$Br | 68 | 33 | 53.5387 | -904438152.41 | 63809.5283 | +8004706.78 | 4090.74 |
| ${}^{69}$Br | 69 | 34 | 59.6393 | -896423273.01 | 64742.9932 | +8036508.39 | 653.96 |
| ${}^{70}$Br | 70 | 35 | 65.7231 | -888422498.72 | 65676.4748 | +8032044.91 | 228.75 |
| ${}^{71}$Br | 71 | 36 | 71.7908 | -880782672.62 | 66609.9726 | +8026589.04 | 81.75 |
| ${}^{72}$Br | 72 | 37 | 77.8426 | -872975187.61 | 67543.4861 | +7983647.76 | 15.29 |
| ${}^{73}$Br | 73 | 38 | 83.8793 | -865893923.58 | 68477.0148 | +7972145.23 | 99.23 |
| ${}^{74}$Br | 74 | 39 | 89.9012 | -858464225.16 | 69410.5584 | +7918110.65 | 84.73 |
| ${}^{75}$Br | 75 | 40 | 95.9088 | -851780800.28 | 70344.1163 | +7897151.35 | 61.39 |
| ${}^{76}$Br | 76 | 41 | 101.9024 | -844738404.74 | 71277.6880 | +7839361.58 | 131.80 |
| ${}^{77}$Br | 77 | 42 | 107.8825 | -838340486.76 | 72211.2733 | +7808067.09 | 39.22 |
| ${}^{78}$Br | 78 | 43 | 113.8496 | -831491975.11 | 73144.8717 | +7739871.81 | 49.31 |
| ${}^{79}$Br | 79 | 44 | 119.8038 | -825440286.11 | 74078.4829 | +7706456.07 | 13.61 |
| ${}^{80}$Br | 80 | 45 | 125.7457 | -818865614.89 | 75012.1064 | +7636208.12 | 13.33 |
| ${}^{81}$Br | 81 | 46 | 131.6756 | -813059528.80 | 75945.7420 | +7598162.13 | 12.96 |
| ${}^{82}$Br | 82 | 47 | 137.5937 | -806740808.01 | 76879.3893 | +7527308.76 | 12.72 |
| ${}^{83}$Br | 83 | 48 | 143.5004 | -801122234.35 | 77813.0479 | +7484315.11 | 49.12 |
| ${}^{84}$Br | 84 | 49 | 149.3961 | -794895934.26 | 78746.7177 | +7407099.59 | 329.16 |
| ${}^{85}$Br | 85 | 50 | 155.2809 | -789379705.80 | 79680.3983 | +7357604.95 | 38.91 |
| ${}^{86}$Br | 86 | 51 | 161.1553 | -782921784.62 | 80614.0894 | +7262375.89 | 38.45 |
| ${}^{87}$Br | 87 | 52 | 167.0194 | -776925070.85 | 81547.7907 | +7184431.55 | 39.16 |
| ${}^{88}$Br | 88 | 53 | 172.8735 | -770606118.22 | 82481.5020 | +7090737.90 | 38.72 |
| ${}^{89}$Br | 89 | 54 | 178.7179 | -764609352.43 | 83415.2231 | +7008199.39 | 39.40 |
| ${}^{90}$Br | 90 | 55 | 184.5528 | -758133862.72 | 84348.9536 | +6905590.53 | 40.08 |
| ${}^{91}$Br | 91 | 56 | 190.3784 | -752180859.57 | 85282.6934 | +6821772.10 | 41.83 |
| ${}^{92}$Br | 92 | 57 | 196.1950 | -745667624.53 | 86216.4422 | +6716595.13 | 78.33 |
| ${}^{93}$Br | 93 | 58 | 202.0028 | -739734233.01 | 87150.1998 | +6631606.32 | 4976.16 |
| ${}^{94}$Br | 94 | 59 | 207.8021 | -733237561.81 | 88083.9660 | +6526701.13 | 2288.48 |
| ${}^{95}$Br | 95 | 60 | 213.5929 | -727307899.99 | 89017.7406 | +6440509.77 | 3391.15 |
| ${}^{96}$Br | 96 | 61 | 219.3755 | -720776889.28 | 89951.5233 | +6335490.82 | 3355.60 |
| ${}^{97}$Br | 97 | 62 | 225.1502 | -714848165.55 | 90885.3141 | +6248679.46 | 4424.35 |
| ${}^{98}$Br | 98 | 63 | 230.9170 | -708307007.83 | 91819.1127 | +6144539.12 | 4378.90 |

### Krypton (Z = 36)

_35 of 35 isotopes with a framework prediction; 35 of 35 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{67}$Kr | 67 | 31 | 32.7934 | -937910225.86 | 62889.9259 | +7939350.57 | 6792.74 |
| ${}^{68}$Kr | 68 | 32 | 38.9672 | -928672312.21 | 63823.3175 | +8012904.14 | 7900.26 |
| ${}^{69}$Kr | 69 | 33 | 45.1226 | -919553344.61 | 64756.7275 | +8028751.38 | 4669.00 |
| ${}^{70}$Kr | 70 | 34 | 51.2603 | -911302090.14 | 65690.1553 | +8082261.07 | 3073.37 |
| ${}^{71}$Kr | 71 | 35 | 57.3808 | -902946146.18 | 66623.6002 | +8077591.48 | 1948.38 |
| ${}^{72}$Kr | 72 | 36 | 63.4846 | -895397134.39 | 67557.0618 | +8109198.79 | 119.54 |
| ${}^{73}$Kr | 73 | 37 | 69.5723 | -887349329.24 | 68490.5395 | +8065960.88 | 96.81 |
| ${}^{74}$Kr | 74 | 38 | 75.6444 | -880204344.32 | 69424.0329 | +8070499.95 | 29.23 |
| ${}^{75}$Kr | 75 | 39 | 81.7012 | -872641963.04 | 70357.5415 | +8020422.60 | 116.11 |
| ${}^{76}$Kr | 76 | 40 | 87.7433 | -865891170.11 | 71291.0648 | +8010326.10 | 56.74 |
| ${}^{77}$Kr | 77 | 41 | 93.7711 | -858671296.74 | 72224.6024 | +7950971.59 | 27.30 |
| ${}^{78}$Kr | 78 | 42 | 99.7850 | -852296566.94 | 73158.1540 | +7932948.63 | 4.22 |
| ${}^{79}$Kr | 79 | 43 | 105.7854 | -845323111.23 | 74091.7190 | +7864220.37 | 47.34 |
| ${}^{80}$Kr | 80 | 44 | 111.7726 | -839276534.11 | 75025.2972 | +7840535.94 | 9.32 |
| ${}^{81}$Kr | 81 | 45 | 117.7471 | -832581106.69 | 75958.8881 | +7768821.00 | 14.24 |
| ${}^{82}$Kr | 82 | 46 | 123.7092 | -826804600.68 | 76892.4914 | +7739866.47 | 0.07 |
| ${}^{83}$Kr | 83 | 47 | 129.6592 | -820353282.64 | 77826.1068 | +7666140.76 | 0.11 |
| ${}^{84}$Kr | 84 | 48 | 135.5975 | -814824731.70 | 78759.7340 | +7633639.12 | 0.05 |
| ${}^{85}$Kr | 85 | 49 | 141.5243 | -808590044.16 | 79693.3726 | +7558634.76 | 25.28 |
| ${}^{86}$Kr | 86 | 50 | 147.4400 | -803212544.18 | 80627.0224 | +7520067.59 | 0.05 |
| ${}^{87}$Kr | 87 | 51 | 153.3448 | -796826983.43 | 81560.6830 | +7428493.61 | 3.04 |
| ${}^{88}$Kr | 88 | 52 | 159.2390 | -790970817.16 | 82494.3542 | +7358055.31 | 31.85 |
| ${}^{89}$Kr | 89 | 53 | 165.1229 | -784636834.61 | 83428.0356 | +7263335.35 | 25.87 |
| ${}^{90}$Kr | 90 | 54 | 170.9968 | -778849114.41 | 84361.7272 | +7189835.63 | 22.24 |
| ${}^{91}$Kr | 91 | 55 | 176.8609 | -772467469.87 | 85295.4285 | +7089428.41 | 26.40 |
| ${}^{92}$Kr | 92 | 56 | 182.7154 | -766696463.58 | 86229.1394 | +7012266.98 | 31.55 |
| ${}^{93}$Kr | 93 | 57 | 188.5606 | -760285244.64 | 87162.8597 | +6908627.08 | 29.05 |
| ${}^{94}$Kr | 94 | 58 | 194.3967 | -754514670.75 | 88096.5890 | +6828539.49 | 138.39 |
| ${}^{95}$Kr | 95 | 59 | 200.2239 | -748073069.83 | 89030.3272 | +6722915.86 | 210.66 |
| ${}^{96}$Kr | 96 | 60 | 206.0424 | -742370925.78 | 89964.0742 | +6643387.55 | 215.70 |
| ${}^{97}$Kr | 97 | 61 | 211.8524 | -735903104.14 | 90897.8296 | +6536832.06 | 1444.06 |
| ${}^{98}$Kr | 98 | 62 | 217.6542 | -730269508.83 | 91831.5932 | +6458531.51 | 3287.30 |
| ${}^{99}$Kr | 99 | 63 | 223.4478 | -723908421.16 | 92765.3650 | +6355518.74 | 4335.14 |
| ${}^{100}$Kr | 100 | 64 | 229.2336 | -718178562.06 | 93699.1447 | +6274011.94 | 4291.59 |
| ${}^{101}$Kr | 101 | 65 | 235.0116 | -711845552.64 | 94632.9321 | +6173241.63 | 5318.45 |

### Rubidium (Z = 37)

_34 of 34 isotopes with a framework prediction; 34 of 34 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{71}$Rb | 71 | 34 | 42.6317 | -926035251.74 | 66637.5670 | +8074814.78 | 6045.21 |
| ${}^{72}$Rb | 72 | 35 | 48.7889 | -917383072.63 | 67570.9751 | +8081990.42 | 7462.60 |
| ${}^{73}$Rb | 73 | 36 | 54.9291 | -909398396.15 | 68504.4004 | +8113577.54 | 600.32 |
| ${}^{74}$Rb | 74 | 37 | 61.0528 | -901566988.07 | 69437.8422 | +8118546.46 | 43.94 |
| ${}^{75}$Rb | 75 | 38 | 67.1603 | -894005504.00 | 70371.3000 | +8114923.80 | 16.89 |
| ${}^{76}$Rb | 76 | 39 | 73.2523 | -886422214.27 | 71304.7735 | +8082508.98 | 13.25 |
| ${}^{77}$Rb | 77 | 40 | 79.3291 | -879324483.33 | 72238.2621 | +8066492.75 | 18.20 |
| ${}^{78}$Rb | 78 | 41 | 85.3912 | -872082962.15 | 73171.7654 | +8019891.38 | 44.59 |
| ${}^{79}$Rb | 79 | 42 | 91.4390 | -865429939.59 | 74105.2830 | +7998826.67 | 26.42 |
| ${}^{80}$Rb | 80 | 43 | 97.4730 | -858516282.48 | 75038.8145 | +7944697.18 | 25.02 |
| ${}^{81}$Rb | 81 | 44 | 103.4934 | -852212816.68 | 75972.3595 | +7917602.76 | 65.07 |
| ${}^{82}$Rb | 82 | 45 | 109.5007 | -845575547.36 | 76905.9176 | +7857656.41 | 39.43 |
| ${}^{83}$Rb | 83 | 46 | 115.4952 | -839599604.71 | 77839.4885 | +7827396.96 | 30.15 |
| ${}^{84}$Rb | 84 | 47 | 121.4773 | -833319387.83 | 78773.0718 | +7769721.78 | 28.06 |
| ${}^{85}$Rb | 85 | 48 | 127.4473 | -827606787.85 | 79706.6673 | +7735471.27 | 0.06 |
| ${}^{86}$Rb | 86 | 49 | 133.4055 | -821634563.50 | 80640.2745 | +7679135.92 | 2.49 |
| ${}^{87}$Rb | 87 | 50 | 139.3522 | -816123022.33 | 81573.8932 | +7640059.40 | 0.07 |
| ${}^{88}$Rb | 88 | 51 | 145.2877 | -809817420.49 | 82507.5231 | +7554762.49 | 1.93 |
| ${}^{89}$Rb | 89 | 52 | 151.2123 | -803903740.78 | 83441.1639 | +7484805.86 | 65.51 |
| ${}^{90}$Rb | 90 | 53 | 157.1263 | -797735866.82 | 84374.8153 | +7399090.35 | 77.03 |
| ${}^{91}$Rb | 91 | 54 | 163.0300 | -791864652.21 | 85308.4771 | +7324026.53 | 92.12 |
| ${}^{92}$Rb | 92 | 55 | 168.9235 | -785735329.12 | 86242.1491 | +7234811.39 | 71.51 |
| ${}^{93}$Rb | 93 | 56 | 174.8071 | -779924660.02 | 87175.8309 | +7157178.48 | 90.46 |
| ${}^{94}$Rb | 94 | 57 | 180.6811 | -773673319.20 | 88109.5223 | +7059390.04 | 23.18 |
| ${}^{95}$Rb | 95 | 58 | 186.5457 | -767896803.34 | 89043.2231 | +6979544.73 | 228.94 |
| ${}^{96}$Rb | 96 | 59 | 192.4011 | -761659804.69 | 89976.9331 | +6880474.62 | 37.52 |
| ${}^{97}$Rb | 97 | 60 | 198.2475 | -756000087.59 | 90910.6521 | +6802520.72 | 21.17 |
| ${}^{98}$Rb | 98 | 61 | 204.0852 | -750021637.29 | 91844.3799 | +6711751.20 | 176.28 |
| ${}^{99}$Rb | 99 | 62 | 209.9143 | -744391834.64 | 92778.1162 | +6632768.81 | 43.73 |
| ${}^{100}$Rb | 100 | 63 | 215.7351 | -738328772.73 | 93711.8608 | +6538085.85 | 140.96 |
| ${}^{101}$Rb | 101 | 64 | 221.5476 | -732696317.02 | 94645.6137 | +6457756.05 | 217.92 |
| ${}^{102}$Rb | 102 | 65 | 227.3522 | -726602114.58 | 95579.3746 | +6361962.21 | 872.89 |
| ${}^{103}$Rb | 103 | 66 | 233.1489 | -720958847.54 | 96513.1432 | +6280953.18 | 4166.49 |
| ${}^{104}$Rb | 104 | 67 | 238.9380 | -714846609.37 | 97446.9196 | +6184778.11 | 5164.93 |

### Strontium (Z = 38)

_35 of 35 isotopes with a framework prediction; 35 of 35 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{73}$Sr | 73 | 35 | 39.9497 | -932454151.70 | 68518.5974 | +8113895.59 | 5893.18 |
| ${}^{74}$Sr | 74 | 36 | 46.1264 | -924178374.59 | 69451.9862 | +8161591.70 | 1446.80 |
| ${}^{75}$Sr | 75 | 37 | 52.2861 | -915970981.96 | 70385.3919 | +8163707.80 | 3151.21 |
| ${}^{76}$Sr | 76 | 38 | 58.4293 | -908409226.03 | 71318.8141 | +8192191.02 | 487.22 |
| ${}^{77}$Sr | 77 | 39 | 64.5565 | -900615893.45 | 72252.2523 | +8162861.74 | 110.48 |
| ${}^{78}$Sr | 78 | 40 | 70.6682 | -893412689.33 | 73185.7061 | +8159697.86 | 102.65 |
| ${}^{79}$Sr | 79 | 41 | 76.7648 | -886001577.23 | 74119.1749 | +8114793.93 | 100.94 |
| ${}^{80}$Sr | 80 | 42 | 82.8467 | -879282844.48 | 75052.6584 | +8105412.10 | 46.52 |
| ${}^{81}$Sr | 81 | 43 | 88.9144 | -872171559.68 | 75986.1562 | +8048102.71 | 41.50 |
| ${}^{82}$Sr | 82 | 44 | 94.9681 | -865888631.99 | 76919.6678 | +8035505.80 | 78.52 |
| ${}^{83}$Sr | 83 | 45 | 101.0084 | -859121134.77 | 77853.1930 | +7975170.70 | 88.47 |
| ${}^{84}$Sr | 84 | 46 | 107.0356 | -853156873.31 | 78786.7312 | +7955955.23 | 15.90 |
| ${}^{85}$Sr | 85 | 47 | 113.0500 | -846698652.60 | 79720.2823 | +7894047.40 | 35.57 |
| ${}^{86}$Sr | 86 | 48 | 119.0519 | -841036807.09 | 80653.8458 | +7871091.16 | 0.07 |
| ${}^{87}$Sr | 87 | 49 | 125.0417 | -834897024.90 | 81587.4214 | +7810680.45 | 0.06 |
| ${}^{88}$Sr | 88 | 50 | 131.0196 | -829505523.33 | 82521.0089 | +7784827.38 | 0.07 |
| ${}^{89}$Sr | 89 | 51 | 136.9861 | -823204348.79 | 83454.6078 | +7701841.96 | 1.10 |
| ${}^{90}$Sr | 90 | 52 | 142.9413 | -817360197.38 | 84388.2181 | +7638340.10 | 17.30 |
| ${}^{91}$Sr | 91 | 53 | 148.8855 | -811157852.78 | 85321.8392 | +7552081.62 | 64.38 |
| ${}^{92}$Sr | 92 | 54 | 154.8191 | -805430143.66 | 86255.4711 | +7485650.39 | 39.98 |
| ${}^{93}$Sr | 93 | 55 | 160.7423 | -799320300.97 | 87189.1133 | +7397526.52 | 87.27 |
| ${}^{94}$Sr | 94 | 56 | 166.6553 | -793697646.67 | 88122.7658 | +7329149.77 | 19.01 |
| ${}^{95}$Sr | 95 | 57 | 172.5583 | -787532510.00 | 89056.4282 | +7233980.69 | 65.71 |
| ${}^{96}$Sr | 96 | 58 | 178.4516 | -781853447.46 | 89990.1002 | +7158151.47 | 94.75 |
| ${}^{97}$Sr | 97 | 59 | 184.3355 | -775684605.20 | 90923.7818 | +7060141.64 | 37.48 |
| ${}^{98}$Sr | 98 | 60 | 190.2101 | -770189464.83 | 91857.4726 | +6988301.04 | 35.36 |
| ${}^{99}$Sr | 99 | 61 | 196.0757 | -764289547.45 | 92791.1724 | +6898941.60 | 51.40 |
| ${}^{100}$Sr | 100 | 62 | 201.9324 | -758806048.57 | 93724.8811 | +6824482.25 | 74.31 |
| ${}^{101}$Sr | 101 | 63 | 207.7805 | -752877259.09 | 94658.5985 | +6732411.73 | 90.18 |
| ${}^{102}$Sr | 102 | 64 | 213.6202 | -747405701.03 | 95592.3243 | +6656312.14 | 706.27 |
| ${}^{103}$Sr | 103 | 65 | 219.4515 | -741495106.14 | 96526.0583 | +6563792.58 | 2088.41 |
| ${}^{104}$Sr | 104 | 66 | 225.2748 | -736034126.03 | 97459.8004 | +6487274.98 | 3097.55 |
| ${}^{105}$Sr | 105 | 67 | 231.0902 | -730022212.06 | 98393.5505 | +6391206.93 | 5116.28 |
| ${}^{106}$Sr | 106 | 68 | 236.8978 | -724564321.14 | 99327.3083 | +6314163.84 | 6077.58 |
| ${}^{107}$Sr | 107 | 69 | 242.6979 | -718480273.19 | 100261.0737 | +6216829.04 | 7020.68 |

### Yttrium (Z = 39)

_35 of 35 isotopes with a framework prediction; 35 of 35 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{75}$Y | 75 | 36 | 37.0785 | -938882414.42 | 70399.8172 | +8156627.15 | 4295.29 |
| ${}^{76}$Y | 76 | 37 | 43.2744 | -930331616.67 | 71333.1867 | +8167370.58 | 4239.13 |
| ${}^{77}$Y | 77 | 38 | 49.4534 | -922414646.47 | 72266.5731 | +8202808.13 | 2833.00 |
| ${}^{78}$Y | 78 | 39 | 55.6160 | -914597517.20 | 73199.9760 | +8203485.23 | 4105.51 |
| ${}^{79}$Y | 79 | 40 | 61.7627 | -907113416.43 | 74133.3947 | +8202931.34 | 1089.46 |
| ${}^{80}$Y | 80 | 41 | 67.8939 | -899616075.88 | 75066.8289 | +8171662.79 | 83.83 |
| ${}^{81}$Y | 81 | 42 | 74.0100 | -892579993.13 | 76000.2782 | +8157672.73 | 71.69 |
| ${}^{82}$Y | 82 | 43 | 80.1116 | -885456822.78 | 76933.7421 | +8114972.02 | 72.04 |
| ${}^{83}$Y | 83 | 44 | 86.1989 | -878868420.67 | 77867.2202 | +8096849.12 | 241.19 |
| ${}^{84}$Y | 84 | 45 | 92.2723 | -872088034.76 | 78800.7122 | +8047702.73 | 54.99 |
| ${}^{85}$Y | 85 | 46 | 98.3323 | -865921374.18 | 79734.2176 | +8028668.82 | 239.77 |
| ${}^{86}$Y | 86 | 47 | 104.3791 | -859498708.14 | 80667.7362 | +7978666.76 | 176.71 |
| ${}^{87}$Y | 87 | 48 | 110.4131 | -853701542.24 | 81601.2676 | +7958536.27 | 13.92 |
| ${}^{88}$Y | 88 | 49 | 116.4347 | -847611227.24 | 82534.8115 | +7908800.27 | 18.31 |
| ${}^{89}$Y | 89 | 50 | 122.4441 | -842119027.84 | 83468.3675 | +7886268.95 | 4.08 |
| ${}^{90}$Y | 90 | 51 | 128.4417 | -835837139.47 | 84401.9353 | +7808701.37 | 4.22 |
| ${}^{91}$Y | 91 | 52 | 134.4277 | -829909354.01 | 85335.5147 | +7745697.02 | 21.76 |
| ${}^{92}$Y | 92 | 53 | 140.4024 | -823806761.77 | 86269.1054 | +7667843.88 | 106.61 |
| ${}^{93}$Y | 93 | 54 | 146.3662 | -818031307.46 | 87202.7071 | +7602804.20 | 121.18 |
| ${}^{94}$Y | 94 | 55 | 152.3192 | -812077766.18 | 88136.3195 | +7524457.62 | 72.93 |
| ${}^{95}$Y | 95 | 56 | 158.2618 | -806400923.74 | 89069.9424 | +7456226.66 | 76.67 |
| ${}^{96}$Y | 96 | 57 | 164.1941 | -800411997.14 | 90003.5755 | +7369978.70 | 67.99 |
| ${}^{97}$Y | 97 | 58 | 170.1164 | -794674823.97 | 90937.2186 | +7293028.82 | 74.30 |
| ${}^{98}$Y | 98 | 59 | 176.0289 | -788621468.76 | 91870.8715 | +7199959.18 | 86.81 |
| ${}^{99}$Y | 99 | 60 | 181.9320 | -783205983.19 | 92804.5339 | +7132726.82 | 71.78 |
| ${}^{100}$Y | 100 | 61 | 187.8256 | -777442340.45 | 93738.2056 | +7048793.86 | 120.09 |
| ${}^{101}$Y | 101 | 62 | 193.7102 | -772037597.52 | 94671.8864 | +6977937.71 | 75.31 |
| ${}^{102}$Y | 102 | 63 | 199.5859 | -766275227.93 | 95605.5762 | +6891435.52 | 42.98 |
| ${}^{103}$Y | 103 | 64 | 205.4528 | -760904303.83 | 96539.2747 | +6818960.65 | 116.86 |
| ${}^{104}$Y | 104 | 65 | 211.3113 | -755141108.82 | 97472.9817 | +6730694.39 | 2068.46 |
| ${}^{105}$Y | 105 | 66 | 217.1613 | -749672807.69 | 98406.6970 | +6653135.67 | 4087.83 |
| ${}^{106}$Y | 106 | 67 | 223.0033 | -743906963.20 | 99340.4205 | +6564180.20 | 5068.39 |
| ${}^{107}$Y | 107 | 68 | 228.8372 | -738485547.38 | 100274.1520 | +6486669.49 | 5020.81 |
| ${}^{108}$Y | 108 | 69 | 234.6633 | -732709058.63 | 101207.8913 | +6396965.71 | 5965.14 |
| ${}^{109}$Y | 109 | 70 | 240.4817 | -727252545.70 | 102141.6383 | +6317821.85 | 6892.11 |

### Zirconium (Z = 40)

_37 of 37 isotopes with a framework prediction; 37 of 37 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{77}$Zr | 77 | 37 | 34.0197 | -945286219.45 | 72281.2245 | +8198497.48 | 5573.88 |
| ${}^{78}$Zr | 78 | 38 | 40.2345 | -937048151.09 | 73214.5751 | +8247318.29 | 5503.09 |
| ${}^{79}$Zr | 79 | 39 | 46.4327 | -928903462.71 | 74147.9424 | +8249497.84 | 4078.54 |
| ${}^{80}$Zr | 80 | 40 | 52.6145 | -921377075.16 | 75081.3260 | +8279854.25 | 4027.96 |
| ${}^{81}$Zr | 81 | 41 | 58.7804 | -913559127.01 | 76014.7254 | +8239801.54 | 1223.15 |
| ${}^{82}$Zr | 82 | 42 | 64.9310 | -906462193.36 | 76948.1403 | +8244849.62 | 20.75 |
| ${}^{83}$Zr | 83 | 43 | 71.0665 | -899130185.84 | 77881.5702 | +8200476.65 | 83.23 |
| ${}^{84}$Zr | 84 | 44 | 77.1875 | -892514263.73 | 78815.0146 | +8198773.73 | 70.34 |
| ${}^{85}$Zr | 85 | 45 | 83.2943 | -885575906.77 | 79748.4733 | +8149412.42 | 81.28 |
| ${}^{86}$Zr | 86 | 46 | 89.3872 | -879338340.67 | 80681.9458 | +8139668.12 | 44.54 |
| ${}^{87}$Zr | 87 | 47 | 95.4666 | -872754919.89 | 81615.4318 | +8087780.65 | 51.20 |
| ${}^{88}$Zr | 88 | 48 | 101.5330 | -866861410.59 | 82548.9309 | +8072975.49 | 65.98 |
| ${}^{89}$Zr | 89 | 49 | 107.5865 | -860626900.94 | 83482.4428 | +8021743.37 | 33.55 |
| ${}^{90}$Zr | 90 | 50 | 113.6275 | -855047956.00 | 84415.9672 | +8003639.56 | 1.40 |
| ${}^{91}$Zr | 91 | 51 | 119.6564 | -848745225.69 | 85349.5037 | +7929277.05 | 1.11 |
| ${}^{92}$Zr | 92 | 52 | 125.6734 | -842854512.65 | 86283.0521 | +7873630.31 | 1.10 |
| ${}^{93}$Zr | 93 | 53 | 131.6788 | -836720108.92 | 87216.6121 | +7797183.25 | 5.26 |
| ${}^{94}$Zr | 94 | 54 | 137.6729 | -831009660.83 | 88150.1834 | +7739595.56 | 1.86 |
| ${}^{95}$Zr | 95 | 55 | 143.6560 | -825053216.66 | 89083.7658 | +7663322.67 | 9.83 |
| ${}^{96}$Zr | 96 | 56 | 149.6283 | -819505589.05 | 90017.3589 | +7604421.58 | 1.27 |
| ${}^{97}$Zr | 97 | 57 | 155.5901 | -813566433.34 | 90950.9625 | +7521393.22 | 1.34 |
| ${}^{98}$Zr | 98 | 58 | 161.5416 | -807911967.35 | 91884.5764 | +7449536.51 | 92.58 |
| ${}^{99}$Zr | 99 | 59 | 167.4831 | -801885028.91 | 92818.2004 | +7357267.13 | 113.94 |
| ${}^{100}$Zr | 100 | 60 | 173.4147 | -796511908.63 | 93751.8342 | +7293159.89 | 87.49 |
| ${}^{101}$Zr | 101 | 61 | 179.3368 | -790756053.39 | 94685.4776 | +7209343.10 | 88.62 |
| ${}^{102}$Zr | 102 | 62 | 185.2494 | -785482210.46 | 95619.1303 | +7144589.71 | 92.24 |
| ${}^{103}$Zr | 103 | 63 | 191.1529 | -779742485.48 | 96552.7923 | +7058158.57 | 96.18 |
| ${}^{104}$Zr | 104 | 64 | 197.0474 | -774504286.38 | 97486.4632 | +6990976.26 | 96.22 |
| ${}^{105}$Zr | 105 | 65 | 202.9331 | -768777505.12 | 98420.1429 | +6902833.02 | 123.89 |
| ${}^{106}$Zr | 106 | 66 | 208.8102 | -763516536.38 | 99353.8313 | +6832267.58 | 2029.51 |
| ${}^{107}$Zr | 107 | 67 | 214.6789 | -757804875.83 | 100287.5280 | +6742692.61 | 3010.98 |
| ${}^{108}$Zr | 108 | 68 | 220.5393 | -752571126.43 | 101221.2330 | +6671476.52 | 3974.23 |
| ${}^{109}$Zr | 109 | 69 | 226.3917 | -746832307.44 | 102154.9460 | +6580327.89 | 4928.83 |
| ${}^{110}$Zr | 110 | 70 | 232.2361 | -741618215.00 | 103088.6670 | +6507729.81 | 4883.83 |
| ${}^{111}$Zr | 111 | 71 | 238.0729 | -735796931.06 | 104022.3957 | +6414806.07 | 5803.85 |
| ${}^{112}$Zr | 112 | 72 | 243.9020 | -730516471.69 | 104956.1320 | +6339830.20 | 6707.44 |
| ${}^{113}$Zr | 113 | 73 | 249.7237 | -724686152.07 | 105889.8757 | +6246947.21 | 2850.27 |

### Niobium (Z = 41)

_38 of 38 isotopes with a framework prediction; 38 of 38 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{79}$Nb | 79 | 38 | 30.7748 | -951704208.27 | 74162.8179 | +8244478.79 | 6800.39 |
| ${}^{80}$Nb | 80 | 39 | 37.0085 | -943245502.72 | 75096.1496 | +8257687.95 | 5365.27 |
| ${}^{81}$Nb | 81 | 40 | 43.2255 | -935299660.34 | 76029.4980 | +8286438.23 | 5299.55 |
| ${}^{82}$Nb | 82 | 41 | 49.4264 | -927483104.34 | 76962.8626 | +8281801.97 | 3929.49 |
| ${}^{83}$Nb | 83 | 42 | 55.6114 | -920036045.73 | 77896.2430 | +8282100.67 | 2097.95 |
| ${}^{84}$Nb | 84 | 43 | 61.7811 | -912628479.27 | 78829.6387 | +8253929.66 | 5.12 |
| ${}^{85}$Nb | 85 | 44 | 67.9359 | -905679365.56 | 79763.0493 | +8245787.70 | 51.81 |
| ${}^{86}$Nb | 86 | 45 | 74.0761 | -898691182.34 | 80696.4745 | +8209906.78 | 68.70 |
| ${}^{87}$Nb | 87 | 46 | 80.2022 | -892201829.43 | 81629.9139 | +8198508.79 | 84.01 |
| ${}^{88}$Nb | 88 | 47 | 86.3144 | -885581035.94 | 82563.3671 | +8157457.87 | 705.87 |
| ${}^{89}$Nb | 89 | 48 | 92.4132 | -879497285.29 | 83496.8338 | +8143747.36 | 285.30 |
| ${}^{90}$Nb | 90 | 49 | 98.4988 | -873232568.52 | 84430.3135 | +8101386.23 | 39.61 |
| ${}^{91}$Nb | 91 | 50 | 104.5716 | -867471765.72 | 85363.8061 | +8083209.37 | 34.54 |
| ${}^{92}$Nb | 92 | 51 | 110.6320 | -861178729.16 | 86297.3112 | +8016573.89 | 20.84 |
| ${}^{93}$Nb | 93 | 52 | 116.6802 | -855194060.91 | 87230.8284 | +7962512.03 | 17.21 |
| ${}^{94}$Nb | 94 | 53 | 122.7164 | -849056651.32 | 88164.3576 | +7891262.43 | 17.04 |
| ${}^{95}$Nb | 95 | 54 | 128.7411 | -843282488.89 | 89097.8983 | +7836022.19 | 5.74 |
| ${}^{96}$Nb | 96 | 55 | 134.7545 | -837326365.14 | 90031.4504 | +7764004.03 | 1.64 |
| ${}^{97}$Nb | 97 | 56 | 140.7567 | -831720151.59 | 90965.0136 | +7706807.29 | 47.01 |
| ${}^{98}$Nb | 98 | 57 | 146.7482 | -825805251.14 | 91898.5875 | +7627937.15 | 54.84 |
| ${}^{99}$Nb | 99 | 58 | 152.7291 | -820174775.64 | 92832.1721 | +7560500.78 | 130.28 |
| ${}^{100}$Nb | 100 | 59 | 158.6996 | -814353117.36 | 93765.7669 | +7479860.76 | 85.69 |
| ${}^{101}$Nb | 101 | 60 | 164.6601 | -808983062.32 | 94699.3719 | +7418552.73 | 39.88 |
| ${}^{102}$Nb | 102 | 61 | 170.6107 | -803329806.47 | 95632.9867 | +7340583.77 | 26.44 |
| ${}^{103}$Nb | 103 | 62 | 176.5516 | -798064739.30 | 96566.6112 | +7278141.79 | 41.04 |
| ${}^{104}$Nb | 104 | 63 | 182.4831 | -792432764.14 | 97500.2451 | +7196731.55 | 18.43 |
| ${}^{105}$Nb | 105 | 64 | 188.4054 | -787191386.72 | 98433.8883 | +7130597.64 | 41.21 |
| ${}^{106}$Nb | 106 | 65 | 194.3186 | -781587521.75 | 99367.5405 | +7047257.71 | 14.35 |
| ${}^{107}$Nb | 107 | 66 | 200.2229 | -776356878.09 | 100301.2016 | +6978046.66 | 80.54 |
| ${}^{108}$Nb | 108 | 67 | 206.1186 | -770768292.74 | 101234.8714 | +6893185.16 | 81.94 |
| ${}^{109}$Nb | 109 | 68 | 212.0058 | -765580767.96 | 102168.5496 | +6823100.62 | 4245.49 |
| ${}^{110}$Nb | 110 | 69 | 217.8846 | -760059737.12 | 103102.2362 | +6739389.75 | 8186.00 |
| ${}^{111}$Nb | 111 | 70 | 223.7554 | -754856609.10 | 104035.9309 | +6667308.83 | 2902.28 |
| ${}^{112}$Nb | 112 | 71 | 229.6181 | -749307685.74 | 104969.6335 | +6581725.21 | 2876.21 |
| ${}^{113}$Nb | 113 | 72 | 235.4730 | -744095263.09 | 105903.3440 | +6507594.15 | 3797.91 |
| ${}^{114}$Nb | 114 | 73 | 241.3203 | -738564299.59 | 106837.0622 | +6421665.39 | 4712.08 |
| ${}^{115}$Nb | 115 | 74 | 247.1601 | -733380721.43 | 107770.7878 | +6348304.15 | 4670.91 |
| ${}^{116}$Nb | 116 | 75 | 252.9925 | -727787132.86 | 108704.5209 | +6261661.34 | 2776.51 |

### Molybdenum (Z = 42)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{81}$Mo | 81 | 39 | 27.3453 | -958083362.75 | 76044.5959 | +8287422.23 | 6632.40 |
| ${}^{82}$Mo | 82 | 40 | 33.5977 | -949806667.68 | 76977.9089 | +8327803.97 | 5234.47 |
| ${}^{83}$Mo | 83 | 41 | 39.8335 | -941714600.41 | 77911.2385 | +8329070.56 | 5183.83 |
| ${}^{84}$Mo | 84 | 42 | 46.0532 | -934143841.89 | 78844.5843 | +8354501.88 | 3812.16 |
| ${}^{85}$Mo | 85 | 43 | 52.2572 | -926472173.31 | 79777.9457 | +8322306.48 | 200.15 |
| ${}^{86}$Mo | 86 | 44 | 58.4459 | -919427834.63 | 80711.3224 | +8332132.84 | 36.62 |
| ${}^{87}$Mo | 87 | 45 | 64.6197 | -912229027.95 | 81644.7140 | +8294258.33 | 35.28 |
| ${}^{88}$Mo | 88 | 46 | 70.7790 | -905641082.79 | 82578.1202 | +8294695.80 | 46.63 |
| ${}^{89}$Mo | 89 | 47 | 76.9241 | -898851047.88 | 83511.5404 | +8253011.94 | 47.23 |
| ${}^{90}$Mo | 90 | 48 | 83.0555 | -892656046.35 | 84444.9745 | +8246474.48 | 41.34 |
| ${}^{91}$Mo | 91 | 49 | 89.1734 | -886235194.01 | 85378.4220 | +8203077.42 | 73.65 |
| ${}^{92}$Mo | 92 | 50 | 95.2782 | -880380565.77 | 86311.8826 | +8190963.11 | 1.83 |
| ${}^{93}$Mo | 93 | 51 | 101.3702 | -874008686.09 | 87245.3560 | +8125653.48 | 2.08 |
| ${}^{94}$Mo | 94 | 52 | 107.4497 | -868039919.06 | 88178.8420 | +8080414.68 | 1.61 |
| ${}^{95}$Mo | 95 | 53 | 113.5171 | -861838957.46 | 89112.3401 | +8009934.62 | 1.39 |
| ${}^{96}$Mo | 96 | 54 | 119.5725 | -856072546.25 | 90045.8501 | +7961200.95 | 1.33 |
| ${}^{97}$Mo | 97 | 55 | 125.6162 | -850029082.12 | 90979.3717 | +7887548.52 | 1.82 |
| ${}^{98}$Mo | 98 | 56 | 131.6487 | -844432274.24 | 91912.9047 | +7835655.92 | 1.90 |
| ${}^{99}$Mo | 99 | 57 | 137.6700 | -838448147.07 | 92846.4488 | +7755210.96 | 2.48 |
| ${}^{100}$Mo | 100 | 58 | 143.6804 | -833020259.63 | 93780.0038 | +7702145.67 | 3.22 |
| ${}^{101}$Mo | 101 | 59 | 149.6803 | -827131973.58 | 94713.5694 | +7619199.69 | 3.28 |
| ${}^{102}$Mo | 102 | 60 | 155.6698 | -821883393.11 | 95647.1453 | +7566800.68 | 87.49 |
| ${}^{103}$Mo | 103 | 61 | 161.6491 | -816191178.83 | 96580.7314 | +7487701.22 | 96.20 |
| ${}^{104}$Mo | 104 | 62 | 167.6185 | -811006768.13 | 97514.3274 | +7431004.09 | 92.06 |
| ${}^{105}$Mo | 105 | 63 | 173.5782 | -805396981.84 | 98447.9331 | +7350724.68 | 92.65 |
| ${}^{106}$Mo | 106 | 64 | 179.5284 | -800264120.12 | 99381.5483 | +7290542.94 | 92.53 |
| ${}^{107}$Mo | 107 | 65 | 185.4693 | -794679784.99 | 100315.1729 | +7207510.30 | 92.60 |
| ${}^{108}$Mo | 108 | 66 | 191.4011 | -789574999.26 | 101248.8065 | +7144018.72 | 91.74 |
| ${}^{109}$Mo | 109 | 67 | 197.3240 | -784008828.07 | 102182.4490 | +7059011.08 | 110.16 |
| ${}^{110}$Mo | 110 | 68 | 203.2381 | -778974192.08 | 103116.1003 | +6994980.59 | 236.51 |
| ${}^{111}$Mo | 111 | 69 | 209.1437 | -773408138.09 | 104049.7602 | +6908096.92 | 121.72 |
| ${}^{112}$Mo | 112 | 70 | 215.0409 | -768422580.62 | 104983.4284 | +6843477.66 | 1920.70 |
| ${}^{113}$Mo | 113 | 71 | 220.9299 | -762899327.85 | 105917.1048 | +6757406.83 | 2850.98 |
| ${}^{114}$Mo | 114 | 72 | 226.8109 | -757930517.25 | 106850.7893 | +6690573.07 | 2825.88 |
| ${}^{115}$Mo | 115 | 73 | 232.6839 | -752436254.67 | 107784.4816 | +6604663.54 | 3731.99 |
| ${}^{116}$Mo | 116 | 74 | 238.5492 | -747456837.52 | 108718.1818 | +6537007.58 | 4631.08 |
| ${}^{117}$Mo | 117 | 75 | 244.4070 | -741977711.83 | 109651.8895 | +6450429.11 | 4591.25 |
| ${}^{118}$Mo | 118 | 76 | 250.2573 | -737098774.18 | 110585.6046 | +6385562.25 | 4552.19 |
| ${}^{119}$Mo | 119 | 77 | 256.1002 | -731624533.24 | 111519.3270 | +6299415.19 | 2706.53 |

### Technetium (Z = 43)

_40 of 40 isotopes with a framework prediction; 40 of 40 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{83}$Tc | 83 | 40 | 23.7329 | -964448839.35 | 77926.5569 | +8331307.66 | 6472.50 |
| ${}^{84}$Tc | 84 | 41 | 30.0037 | -956011402.29 | 78859.8514 | +8337365.36 | 5109.60 |
| ${}^{85}$Tc | 85 | 42 | 36.2582 | -948074672.84 | 79793.1624 | +8366030.26 | 5049.98 |
| ${}^{86}$Tc | 86 | 43 | 42.4965 | -940320568.27 | 80726.4894 | +8363634.47 | 3746.60 |
| ${}^{87}$Tc | 87 | 44 | 48.7193 | -932917013.62 | 81659.8321 | +8366460.10 | 51.76 |
| ${}^{88}$Tc | 88 | 45 | 54.9268 | -925604237.07 | 82593.1900 | +8343069.05 | 50.04 |
| ${}^{89}$Tc | 89 | 46 | 61.1195 | -918735053.06 | 83526.5628 | +8341613.62 | 46.10 |
| ${}^{90}$Tc | 90 | 47 | 67.2977 | -911856629.36 | 84459.9500 | +8311535.74 | 12.23 |
| ${}^{91}$Tc | 91 | 48 | 73.4618 | -905434606.04 | 85393.3513 | +8305286.73 | 27.89 |
| ${}^{92}$Tc | 92 | 49 | 79.6121 | -898949667.96 | 86326.7664 | +8271977.53 | 36.23 |
| ${}^{93}$Tc | 93 | 50 | 85.7490 | -892893771.83 | 87260.1949 | +8259824.91 | 11.69 |
| ${}^{94}$Tc | 94 | 51 | 91.8728 | -886467641.46 | 88193.6366 | +8200498.23 | 46.53 |
| ${}^{95}$Tc | 95 | 52 | 97.9838 | -880384389.45 | 89127.0910 | +8157513.60 | 57.46 |
| ${}^{96}$Tc | 96 | 53 | 104.0823 | -874148876.77 | 90060.5579 | +8092286.89 | 57.60 |
| ${}^{97}$Tc | 97 | 54 | 110.1686 | -868298346.81 | 90994.0370 | +8046437.03 | 45.61 |
| ${}^{98}$Tc | 98 | 55 | 116.2430 | -862235499.56 | 91927.5281 | +7977392.42 | 37.06 |
| ${}^{99}$Tc | 99 | 56 | 122.3057 | -856574502.89 | 92861.0307 | +7928336.98 | 9.85 |
| ${}^{100}$Tc | 100 | 57 | 128.3571 | -850662823.52 | 93794.5448 | +7856531.02 | 14.51 |
| ${}^{101}$Tc | 101 | 58 | 134.3973 | -845147788.95 | 94728.0700 | +7803751.12 | 255.36 |
| ${}^{102}$Tc | 102 | 59 | 140.4266 | -839366755.06 | 95661.6061 | +7729877.54 | 96.56 |
| ${}^{103}$Tc | 103 | 60 | 146.4453 | -834020345.04 | 96595.1529 | +7676502.81 | 102.33 |
| ${}^{104}$Tc | 104 | 61 | 152.4536 | -828371218.78 | 97528.7100 | +7602027.49 | 257.10 |
| ${}^{105}$Tc | 105 | 62 | 158.4517 | -823183026.14 | 98462.2773 | +7548588.62 | 360.84 |
| ${}^{106}$Tc | 106 | 63 | 164.4398 | -817632603.93 | 99395.8547 | +7472799.39 | 124.16 |
| ${}^{107}$Tc | 107 | 64 | 170.4181 | -812467683.51 | 100329.4417 | +7413538.49 | 87.08 |
| ${}^{108}$Tc | 108 | 65 | 176.3869 | -807013162.93 | 101263.0383 | +7337425.98 | 87.22 |
| ${}^{109}$Tc | 109 | 66 | 182.3464 | -801886909.59 | 102196.6443 | +7274593.16 | 95.30 |
| ${}^{110}$Tc | 110 | 67 | 188.2967 | -796488551.84 | 103130.2595 | +7197175.06 | 92.75 |
| ${}^{111}$Tc | 111 | 68 | 194.2380 | -791433538.36 | 104063.8836 | +7133314.93 | 102.40 |
| ${}^{112}$Tc | 112 | 69 | 200.1705 | -786052520.61 | 104997.5165 | +7053722.85 | 52.89 |
| ${}^{113}$Tc | 113 | 70 | 206.0944 | -781037098.61 | 105931.1580 | +6988247.75 | 31.88 |
| ${}^{114}$Tc | 114 | 71 | 212.0098 | -775672280.61 | 106864.8080 | +6907269.89 | 4081.20 |
| ${}^{115}$Tc | 115 | 72 | 217.9170 | -770700613.47 | 107798.4663 | +6841020.21 | 1827.04 |
| ${}^{116}$Tc | 116 | 73 | 223.8160 | -765359556.14 | 108732.1327 | +6759406.98 | 2759.93 |
| ${}^{117}$Tc | 117 | 74 | 229.7071 | -760426050.67 | 109665.8070 | +6693214.19 | 3668.29 |
| ${}^{118}$Tc | 118 | 75 | 235.5904 | -755117307.26 | 110599.4891 | +6611952.52 | 3637.03 |
| ${}^{119}$Tc | 119 | 76 | 241.4660 | -750292149.26 | 111533.1789 | +6547837.50 | 4514.24 |
| ${}^{120}$Tc | 120 | 77 | 247.3341 | -745005877.41 | 112466.8763 | +6466404.24 | 4476.40 |
| ${}^{121}$Tc | 121 | 78 | 253.1948 | -740188816.12 | 113400.5809 | +6401664.98 | 4439.26 |
| ${}^{122}$Tc | 122 | 79 | 259.0483 | -734946078.17 | 114334.2929 | +6322329.29 | 2639.96 |

### Ruthenium (Z = 44)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{85}$Ru | 85 | 41 | 19.9388 | -970776897.87 | 79808.6994 | +8368431.33 | 6320.09 |
| ${}^{86}$Ru | 86 | 42 | 26.2280 | -962501304.06 | 80741.9756 | +8408437.52 | 4990.85 |
| ${}^{87}$Ru | 87 | 43 | 32.5009 | -954447846.72 | 81675.2682 | +8408139.52 | 4933.82 |
| ${}^{88}$Ru | 88 | 44 | 38.7578 | -946923457.52 | 82608.5767 | +8440666.08 | 3661.52 |
| ${}^{89}$Ru | 89 | 45 | 44.9991 | -939378281.62 | 83541.9008 | +8416902.88 | 292.34 |
| ${}^{90}$Ru | 90 | 46 | 51.2253 | -932320398.38 | 84475.2401 | +8423755.69 | 44.52 |
| ${}^{91}$Ru | 91 | 47 | 57.4367 | -925242512.33 | 85408.5941 | +8393029.45 | 26.22 |
| ${}^{92}$Ru | 92 | 48 | 63.6336 | -918672758.08 | 86341.9626 | +8394998.02 | 31.73 |
| ${}^{93}$Ru | 93 | 49 | 69.8165 | -912006284.29 | 87275.3451 | +8360435.27 | 23.85 |
| ${}^{94}$Ru | 94 | 50 | 75.9856 | -905825979.40 | 88208.7414 | +8355019.36 | 35.93 |
| ${}^{95}$Ru | 95 | 51 | 82.1414 | -899313062.55 | 89142.1511 | +8298626.52 | 107.47 |
| ${}^{96}$Ru | 96 | 52 | 88.2840 | -893183752.92 | 90075.5739 | +8263288.01 | 1.90 |
| ${}^{97}$Ru | 97 | 53 | 94.4139 | -886877365.69 | 91009.0094 | +8199974.66 | 30.60 |
| ${}^{98}$Ru | 98 | 54 | 100.5312 | -880998681.50 | 91942.4575 | +8160909.23 | 70.85 |
| ${}^{99}$Ru | 99 | 55 | 106.6364 | -874878521.77 | 92875.9178 | +8093178.63 | 3.72 |
| ${}^{100}$Ru | 100 | 56 | 112.7296 | -869213521.38 | 93809.3900 | +8050779.55 | 3.67 |
| ${}^{101}$Ru | 101 | 57 | 118.8111 | -863237119.42 | 94742.8739 | +7978551.01 | 4.39 |
| ${}^{102}$Ru | 102 | 58 | 124.8812 | -857759372.21 | 95676.3692 | +7933532.51 | 4.38 |
| ${}^{103}$Ru | 103 | 59 | 130.9402 | -851909352.92 | 96609.8756 | +7858091.13 | 4.60 |
| ${}^{104}$Ru | 104 | 60 | 136.9883 | -846613055.05 | 97543.3930 | +7811996.20 | 25.81 |
| ${}^{105}$Ru | 105 | 61 | 143.0257 | -840905761.72 | 98476.9210 | +7736055.48 | 25.57 |
| ${}^{106}$Ru | 106 | 62 | 149.0526 | -835747414.63 | 99410.4595 | +7687703.83 | 54.64 |
| ${}^{107}$Ru | 107 | 63 | 155.0693 | -830167181.13 | 100344.0082 | +7611528.05 | 87.08 |
| ${}^{108}$Ru | 108 | 64 | 161.0760 | -825096189.05 | 101277.5669 | +7559515.73 | 86.35 |
| ${}^{109}$Ru | 109 | 65 | 167.0729 | -819593027.73 | 102211.1355 | +7481525.68 | 88.25 |
| ${}^{110}$Ru | 110 | 66 | 173.0602 | -814610375.67 | 103144.7136 | +7427261.81 | 87.16 |
| ${}^{111}$Ru | 111 | 67 | 179.0380 | -809184514.19 | 104078.3012 | +7348508.44 | 93.71 |
| ${}^{112}$Ru | 112 | 68 | 185.0067 | -804266153.54 | 105011.8979 | +7291863.18 | 92.08 |
| ${}^{113}$Ru | 113 | 69 | 190.9663 | -798877703.29 | 105945.5037 | +7211329.16 | 363.94 |
| ${}^{114}$Ru | 114 | 70 | 196.9171 | -794004306.47 | 106879.1184 | +7152384.25 | 33.50 |
| ${}^{115}$Ru | 115 | 71 | 202.8592 | -788662725.24 | 107812.7417 | +7071318.67 | 235.07 |
| ${}^{116}$Ru | 116 | 72 | 208.7928 | -783840187.41 | 108746.3736 | +7011128.08 | 34.50 |
| ${}^{117}$Ru | 117 | 73 | 214.7180 | -778506685.94 | 109680.0137 | +6928540.31 | 3976.53 |
| ${}^{118}$Ru | 118 | 74 | 220.6351 | -773715508.36 | 110613.6621 | +6866581.34 | 1822.98 |
| ${}^{119}$Ru | 119 | 75 | 226.5441 | -768402435.14 | 111547.3185 | +6783655.48 | 2707.15 |
| ${}^{120}$Ru | 120 | 76 | 232.4453 | -763746326.41 | 112480.9828 | +6725262.21 | 3576.59 |
| ${}^{121}$Ru | 121 | 77 | 238.3387 | -758491749.77 | 113414.6547 | +6643419.69 | 3546.86 |
| ${}^{122}$Ru | 122 | 78 | 244.2245 | -753831710.57 | 114348.3343 | +6583016.52 | 4403.26 |
| ${}^{123}$Ru | 123 | 79 | 250.1030 | -748626861.10 | 115282.0213 | +6502659.25 | 4367.25 |
| ${}^{124}$Ru | 124 | 80 | 255.9740 | -744041307.74 | 116215.7157 | +6443454.20 | 5195.06 |
| ${}^{125}$Ru | 125 | 81 | 261.8380 | -738912650.62 | 117149.4172 | +6365724.63 | 2576.63 |

### Rhodium (Z = 45)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{88}$Rh | 88 | 43 | 22.2719 | -968715700.31 | 82624.2802 | +8417189.89 | 4877.19 |
| ${}^{89}$Rh | 89 | 44 | 28.5631 | -960809221.88 | 83557.5545 | +8451032.57 | 4350.71 |
| ${}^{90}$Rh | 90 | 45 | 34.8383 | -953102432.80 | 84490.8447 | +8450525.50 | 2390.36 |
| ${}^{91}$Rh | 91 | 46 | 41.0981 | -945769987.43 | 85424.1503 | +8461556.91 | 3518.91 |
| ${}^{92}$Rh | 92 | 47 | 47.3428 | -938544180.98 | 86357.4711 | +8443010.35 | 51.12 |
| ${}^{93}$Rh | 93 | 48 | 53.5727 | -931705672.21 | 87290.8066 | +8443475.32 | 30.36 |
| ${}^{94}$Rh | 94 | 49 | 59.7883 | -924927387.99 | 88224.1564 | +8419693.95 | 38.62 |
| ${}^{95}$Rh | 95 | 50 | 65.9898 | -918522100.00 | 89157.5203 | +8414102.60 | 43.94 |
| ${}^{96}$Rh | 96 | 51 | 72.1776 | -911906432.32 | 90090.8980 | +8362663.99 | 111.94 |
| ${}^{97}$Rh | 97 | 52 | 78.3520 | -905635229.99 | 91024.2890 | +8329888.75 | 392.84 |
| ${}^{98}$Rh | 98 | 53 | 84.5133 | -899264035.78 | 91957.6931 | +8272140.99 | 130.55 |
| ${}^{99}$Rh | 99 | 54 | 90.6619 | -893268589.70 | 92891.1099 | +8235742.89 | 211.12 |
| ${}^{100}$Rh | 100 | 55 | 96.7979 | -887118415.40 | 93824.5393 | +8174176.38 | 194.76 |
| ${}^{101}$Rh | 101 | 56 | 102.9217 | -881345895.82 | 94757.9809 | +8133423.27 | 62.14 |
| ${}^{102}$Rh | 102 | 57 | 109.0336 | -875369064.61 | 95691.4344 | +8067571.32 | 67.51 |
| ${}^{103}$Rh | 103 | 58 | 115.1339 | -869783399.62 | 96624.8996 | +8022865.38 | 24.00 |
| ${}^{104}$Rh | 104 | 59 | 121.2226 | -863973734.70 | 97558.3763 | +7954967.97 | 23.78 |
| ${}^{105}$Rh | 105 | 60 | 127.3002 | -858576351.87 | 98491.8641 | +7908740.84 | 25.59 |
| ${}^{106}$Rh | 106 | 61 | 133.3669 | -852912274.30 | 99425.3629 | +7839176.35 | 54.63 |
| ${}^{107}$Rh | 107 | 62 | 139.4229 | -847673421.84 | 100358.8723 | +7791158.12 | 121.01 |
| ${}^{108}$Rh | 108 | 63 | 145.4683 | -842144408.40 | 101292.3923 | +7720737.70 | 139.25 |
| ${}^{109}$Rh | 109 | 64 | 151.5035 | -837017143.03 | 102225.9225 | +7669599.54 | 39.81 |
| ${}^{110}$Rh | 110 | 65 | 157.5287 | -831604423.17 | 103159.4628 | +7598441.95 | 173.90 |
| ${}^{111}$Rh | 111 | 66 | 163.5440 | -826573215.93 | 104093.0129 | +7544715.27 | 66.32 |
| ${}^{112}$Rh | 112 | 67 | 169.5496 | -821246918.20 | 105026.5727 | +7472249.16 | 422.89 |
| ${}^{113}$Rh | 113 | 68 | 175.5458 | -816301692.19 | 105960.1419 | +7416568.05 | 67.80 |
| ${}^{114}$Rh | 114 | 69 | 181.5328 | -811028365.97 | 106893.7204 | +7342087.90 | 674.38 |
| ${}^{115}$Rh | 115 | 70 | 187.5106 | -806135538.38 | 107827.3080 | +7283818.93 | 68.37 |
| ${}^{116}$Rh | 116 | 71 | 193.4795 | -800906647.68 | 108760.9045 | +7207867.98 | 683.73 |
| ${}^{117}$Rh | 117 | 72 | 199.4397 | -796081279.13 | 109694.5097 | +7148600.20 | 81.66 |
| ${}^{118}$Rh | 118 | 73 | 205.3914 | -790864444.94 | 110628.1235 | +7070514.95 | 220.62 |
| ${}^{119}$Rh | 119 | 74 | 211.3346 | -786121126.61 | 111561.7457 | +7011511.61 | 84.08 |
| ${}^{120}$Rh | 120 | 75 | 217.2696 | -780960598.74 | 112495.3761 | +6934289.89 | 1792.61 |
| ${}^{121}$Rh | 121 | 76 | 223.1965 | -776283178.01 | 113429.0146 | +6874807.34 | 5498.61 |
| ${}^{122}$Rh | 122 | 77 | 229.1154 | -771199416.18 | 114362.6611 | +6798638.08 | 2640.55 |
| ${}^{123}$Rh | 123 | 78 | 235.0266 | -766550374.86 | 115296.3154 | +6738561.53 | 3489.30 |
| ${}^{124}$Rh | 124 | 79 | 240.9301 | -761538461.75 | 116229.9773 | +6663905.69 | 3461.02 |
| ${}^{125}$Rh | 125 | 80 | 246.8261 | -756941312.93 | 117163.6467 | +6604354.58 | 4297.54 |
| ${}^{126}$Rh | 126 | 81 | 252.7147 | -751988075.36 | 118097.3235 | +6530807.73 | 4263.26 |
| ${}^{127}$Rh | 127 | 82 | 258.5961 | -747370983.18 | 119031.0075 | +6468355.70 | 5072.31 |
| ${}^{128}$Rh | 128 | 83 | 264.4704 | -742050573.78 | 119964.6987 | +6382288.28 | 2516.20 |

### Palladium (Z = 46)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{90}$Pd | 90 | 44 | 18.1368 | -975160830.93 | 84506.7639 | +8497000.43 | 4768.93 |
| ${}^{91}$Pd | 91 | 45 | 24.4461 | -967171155.05 | 85440.0200 | +8501272.55 | 4991.73 |
| ${}^{92}$Pd | 92 | 46 | 30.7396 | -959625028.59 | 86373.2919 | +8530950.90 | 4028.68 |
| ${}^{93}$Pd | 93 | 47 | 37.0176 | -952150484.42 | 87306.5793 | +8508833.39 | 4274.10 |
| ${}^{94}$Pd | 94 | 48 | 43.2807 | -945132258.93 | 88239.8817 | +8520987.60 | 48.99 |
| ${}^{95}$Pd | 95 | 49 | 49.5290 | -938146967.24 | 89173.1988 | +8495906.57 | 34.27 |
| ${}^{96}$Pd | 96 | 50 | 55.7630 | -931582654.39 | 90106.5302 | +8498075.23 | 46.94 |
| ${}^{97}$Pd | 97 | 51 | 61.9830 | -924845016.75 | 91039.8756 | +8449022.30 | 53.65 |
| ${}^{98}$Pd | 98 | 52 | 68.1893 | -918465263.88 | 91973.2347 | +8422046.05 | 51.99 |
| ${}^{99}$Pd | 99 | 53 | 74.3822 | -912000268.25 | 92906.6072 | +8366719.30 | 55.42 |
| ${}^{100}$Pd | 100 | 54 | 80.5621 | -905924558.36 | 93839.9928 | +8336128.14 | 189.51 |
| ${}^{101}$Pd | 101 | 55 | 86.7292 | -899694114.51 | 94773.3911 | +8276130.27 | 48.81 |
| ${}^{102}$Pd | 102 | 56 | 92.8838 | -893870043.62 | 95706.8019 | +8241353.31 | 4.41 |
| ${}^{103}$Pd | 103 | 57 | 99.0262 | -887829012.88 | 96640.2250 | +8176699.35 | 9.15 |
| ${}^{104}$Pd | 104 | 58 | 105.1566 | -882220220.58 | 97573.6599 | +8138246.72 | 13.80 |
| ${}^{105}$Pd | 105 | 59 | 111.2754 | -876349462.88 | 98507.1066 | +8070569.40 | 11.65 |
| ${}^{106}$Pd | 106 | 60 | 117.3827 | -870934184.17 | 99440.5647 | +8029494.15 | 11.20 |
| ${}^{107}$Pd | 107 | 61 | 123.4788 | -865200142.80 | 100374.0341 | +7958683.59 | 12.06 |
| ${}^{108}$Pd | 108 | 62 | 129.5639 | -859967014.66 | 101307.5144 | +7916235.30 | 11.02 |
| ${}^{109}$Pd | 109 | 63 | 135.6383 | -854370347.39 | 102241.0054 | +7844177.53 | 10.97 |
| ${}^{110}$Pd | 110 | 64 | 141.7022 | -849283107.61 | 103174.5069 | +7799545.35 | 5.98 |
| ${}^{111}$Pd | 111 | 65 | 147.7558 | -843795791.27 | 104108.0188 | +7725875.72 | 7.08 |
| ${}^{112}$Pd | 112 | 66 | 153.7993 | -838839006.71 | 105041.5407 | +7679530.87 | 62.79 |
| ${}^{113}$Pd | 113 | 67 | 159.8329 | -833448698.46 | 105975.0725 | +7604729.75 | 66.05 |
| ${}^{114}$Pd | 114 | 68 | 165.8568 | -828595308.54 | 106908.6140 | +7556313.82 | 65.48 |
| ${}^{115}$Pd | 115 | 69 | 171.8712 | -823294048.23 | 107842.1651 | +7480927.78 | 126.56 |
| ${}^{116}$Pd | 116 | 70 | 177.8763 | -818515082.53 | 108775.7254 | +7429975.89 | 66.07 |
| ${}^{117}$Pd | 117 | 71 | 183.8722 | -813286024.35 | 109709.2949 | +7353966.47 | 66.61 |
| ${}^{118}$Pd | 118 | 72 | 189.8592 | -808574148.16 | 110642.8733 | +7301080.92 | 22.70 |
| ${}^{119}$Pd | 119 | 73 | 195.8374 | -803357566.55 | 111576.4605 | +7222382.34 | 74.45 |
| ${}^{120}$Pd | 120 | 74 | 201.8070 | -798766481.35 | 112510.0564 | +7170804.69 | 20.55 |
| ${}^{121}$Pd | 121 | 75 | 207.7681 | -793640055.81 | 113443.6607 | +7093606.03 | 29.77 |
| ${}^{122}$Pd | 122 | 76 | 213.7209 | -789090281.48 | 114377.2733 | +7040193.84 | 172.23 |
| ${}^{123}$Pd | 123 | 77 | 219.6656 | -784051707.83 | 115310.8940 | +6964681.73 | 6893.88 |
| ${}^{124}$Pd | 124 | 78 | 225.6023 | -779523363.24 | 116244.5228 | +6909272.92 | 2598.09 |
| ${}^{125}$Pd | 125 | 79 | 231.5311 | -774528453.81 | 117178.1594 | +6833964.92 | 3433.59 |
| ${}^{126}$Pd | 126 | 80 | 237.4522 | -770093784.02 | 118111.8037 | +6779412.83 | 3406.26 |
| ${}^{127}$Pd | 127 | 81 | 243.3657 | -765163533.34 | 119045.4556 | +6705350.27 | 4230.03 |
| ${}^{128}$Pd | 128 | 82 | 249.2718 | -760669034.44 | 119979.1149 | +6647209.47 | 4196.88 |
| ${}^{129}$Pd | 129 | 83 | 255.1706 | -755371426.51 | 120912.7816 | +6559194.51 | 4993.82 |
| ${}^{130}$Pd | 130 | 84 | 261.0622 | -750413777.42 | 121846.4554 | +6483909.27 | 2477.59 |
| ${}^{131}$Pd | 131 | 85 | 266.9467 | -745056752.10 | 122780.1363 | +6394661.70 | 2458.53 |

### Silver (Z = 47)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{92}$Ag | 92 | 45 | 13.8240 | -981403328.78 | 86389.4252 | +8516205.09 | 4665.09 |
| ${}^{93}$Ag | 93 | 46 | 20.1513 | -973494725.29 | 87322.6633 | +8548041.42 | 4626.13 |
| ${}^{94}$Ag | 94 | 47 | 26.4629 | -965826690.02 | 88255.9172 | +8546340.67 | 4566.56 |
| ${}^{95}$Ag | 95 | 48 | 32.7591 | -958528891.28 | 89189.1864 | +8561974.04 | 4518.85 |
| ${}^{96}$Ag | 96 | 49 | 39.0403 | -951356986.40 | 90122.4706 | +8544734.49 | 1008.10 |
| ${}^{97}$Ag | 97 | 50 | 45.3069 | -944548316.89 | 91055.7694 | +8547972.71 | 133.09 |
| ${}^{98}$Ag | 98 | 51 | 51.5592 | -937676662.23 | 91989.0825 | +8504530.82 | 360.77 |
| ${}^{99}$Ag | 99 | 52 | 57.7975 | -931111654.39 | 92922.4096 | +8478355.12 | 67.99 |
| ${}^{100}$Ag | 100 | 53 | 64.0222 | -924546591.85 | 93855.7504 | +8428787.55 | 53.72 |
| ${}^{101}$Ag | 101 | 54 | 70.2335 | -918311026.12 | 94789.1045 | +8399340.46 | 51.46 |
| ${}^{102}$Ag | 102 | 55 | 76.4318 | -912021066.40 | 95722.4716 | +8346344.56 | 86.06 |
| ${}^{103}$Ag | 103 | 56 | 82.6173 | -906050340.45 | 96655.8516 | +8311799.86 | 42.76 |
| ${}^{104}$Ag | 104 | 57 | 88.7903 | -899984258.85 | 97589.2440 | +8254689.59 | 43.57 |
| ${}^{105}$Ag | 105 | 58 | 94.9511 | -894238949.09 | 98522.6486 | +8215719.32 | 46.49 |
| ${}^{106}$Ag | 106 | 59 | 101.0999 | -888377611.52 | 99456.0651 | +8156319.01 | 30.56 |
| ${}^{107}$Ag | 107 | 60 | 107.2371 | -882835236.85 | 100389.4934 | +8114271.58 | 23.91 |
| ${}^{108}$Ag | 108 | 61 | 113.3628 | -877118692.13 | 101322.9332 | +8050408.06 | 23.75 |
| ${}^{109}$Ag | 109 | 62 | 119.4772 | -871767389.57 | 102256.3841 | +8006832.75 | 12.68 |
| ${}^{110}$Ag | 110 | 63 | 125.5807 | -866194516.30 | 103189.8461 | +7940775.77 | 12.56 |
| ${}^{111}$Ag | 111 | 64 | 131.6734 | -861010343.19 | 104123.3188 | +7895725.63 | 14.11 |
| ${}^{112}$Ag | 112 | 65 | 137.7556 | -855571960.61 | 105056.8020 | +7828474.82 | 23.23 |
| ${}^{113}$Ag | 113 | 66 | 143.8275 | -850540224.50 | 105990.2956 | +7782396.57 | 158.24 |
| ${}^{114}$Ag | 114 | 67 | 149.8892 | -845202320.25 | 106923.7993 | +7713107.21 | 43.02 |
| ${}^{115}$Ag | 115 | 68 | 155.9409 | -840292162.51 | 107857.3130 | +7665338.59 | 170.67 |
| ${}^{116}$Ag | 116 | 69 | 161.9830 | -835055466.09 | 108790.8363 | +7595230.98 | 30.20 |
| ${}^{117}$Ag | 117 | 70 | 168.0155 | -830245504.88 | 109724.3692 | +7545649.21 | 124.62 |
| ${}^{118}$Ag | 118 | 71 | 174.0386 | -825121768.59 | 110657.9115 | +7476196.14 | 22.90 |
| ${}^{119}$Ag | 119 | 72 | 180.0526 | -820371729.37 | 111591.4630 | +7423640.82 | 132.72 |
| ${}^{120}$Ag | 120 | 73 | 186.0576 | -815316370.36 | 112525.0235 | +7353229.63 | 40.03 |
| ${}^{121}$Ag | 121 | 74 | 192.0537 | -810646880.56 | 113458.5928 | +7299675.46 | 107.51 |
| ${}^{122}$Ag | 122 | 75 | 198.0411 | -805658489.78 | 114392.1707 | +7228913.63 | 336.28 |
| ${}^{123}$Ag | 123 | 76 | 204.0200 | -801066762.50 | 115325.7572 | +7174854.93 | 284.73 |
| ${}^{124}$Ag | 124 | 77 | 209.9906 | -796185597.63 | 116259.3521 | +7106029.27 | 2178.67 |
| ${}^{125}$Ag | 125 | 78 | 215.9530 | -791684782.54 | 117192.9552 | +7052473.29 | 3722.06 |
| ${}^{126}$Ag | 126 | 79 | 221.9073 | -786809246.95 | 118126.5663 | +6981900.83 | 1707.23 |
| ${}^{127}$Ag | 127 | 80 | 227.8537 | -782372234.24 | 119060.1853 | +6927234.24 | 1693.75 |
| ${}^{128}$Ag | 128 | 81 | 233.7923 | -777554238.34 | 119993.8121 | +6857702.50 | 2516.78 |
| ${}^{129}$Ag | 129 | 82 | 239.7233 | -773043502.12 | 120927.4466 | +6798530.73 | 3327.02 |
| ${}^{130}$Ag | 130 | 83 | 245.6467 | -767920628.04 | 121861.0885 | +6714280.95 | 3501.33 |
| ${}^{131}$Ag | 131 | 84 | 251.5628 | -762981115.67 | 122794.7378 | +6638197.02 | 4100.61 |
| ${}^{132}$Ag | 132 | 85 | 257.4717 | -757786767.67 | 123728.3944 | +6553484.27 | 4069.32 |
| ${}^{133}$Ag | 133 | 86 | 263.3734 | -752870161.15 | 124662.0581 | +6478483.42 | 4038.54 |

### Cadmium (Z = 48)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{94}$Cd | 94 | 46 | 9.3348 | -987742961.51 | 88272.2629 | +8595257.78 | 5715.41 |
| ${}^{95}$Cd | 95 | 47 | 15.6799 | -979800263.09 | 89205.4832 | +8599701.54 | 6392.87 |
| ${}^{96}$Cd | 96 | 48 | 22.0094 | -972240593.23 | 90138.7191 | +8625664.01 | 4586.18 |
| ${}^{97}$Cd | 97 | 49 | 28.3236 | -964863324.78 | 91071.9703 | +8613801.65 | 4653.36 |
| ${}^{98}$Cd | 98 | 50 | 34.6229 | -957832084.06 | 92005.2364 | +8621587.10 | 567.82 |
| ${}^{99}$Cd | 99 | 51 | 40.9076 | -950798987.00 | 92938.5172 | +8578939.92 | 17.18 |
| ${}^{100}$Cd | 100 | 52 | 47.1781 | -944086799.44 | 93871.8121 | +8558630.27 | 18.01 |
| ${}^{101}$Cd | 101 | 53 | 53.4346 | -937392587.43 | 94805.1210 | +8510743.60 | 15.85 |
| ${}^{102}$Cd | 102 | 54 | 59.6775 | -931039081.39 | 95738.4436 | +8487110.99 | 17.50 |
| ${}^{103}$Cd | 103 | 55 | 65.9071 | -924629804.32 | 96671.7794 | +8434289.91 | 18.88 |
| ${}^{104}$Cd | 104 | 56 | 72.1236 | -918581019.20 | 97605.1283 | +8406839.48 | 17.27 |
| ${}^{105}$Cd | 105 | 57 | 78.3274 | -912411886.99 | 98538.4900 | +8349587.05 | 14.24 |
| ${}^{106}$Cd | 106 | 58 | 84.5187 | -906623551.05 | 99471.8641 | +8318407.47 | 11.18 |
| ${}^{107}$Cd | 107 | 59 | 90.6978 | -900667092.20 | 100405.2504 | +8258162.98 | 16.67 |
| ${}^{108}$Cd | 108 | 60 | 96.8649 | -895099987.23 | 101338.6487 | +8223267.12 | 11.17 |
| ${}^{109}$Cd | 109 | 61 | 103.0203 | -889311806.10 | 102272.0587 | +8159209.71 | 15.14 |
| ${}^{110}$Cd | 110 | 62 | 109.1643 | -883946870.89 | 103205.4802 | +8121952.21 | 3.70 |
| ${}^{111}$Cd | 111 | 63 | 115.2970 | -878329436.59 | 104138.9129 | +8056791.20 | 3.45 |
| ${}^{112}$Cd | 112 | 64 | 121.4187 | -873127049.48 | 105072.3566 | +8016287.55 | 2.39 |
| ${}^{113}$Cd | 113 | 65 | 127.5296 | -867646067.99 | 106005.8111 | +7949247.68 | 2.32 |
| ${}^{114}$Cd | 114 | 66 | 133.6299 | -862604417.92 | 106939.2762 | +7907265.44 | 2.60 |
| ${}^{115}$Cd | 115 | 67 | 139.7199 | -857244170.65 | 107872.7517 | +7838782.82 | 6.08 |
| ${}^{116}$Cd | 116 | 68 | 145.7997 | -852344657.42 | 108806.2373 | +7795459.84 | 1.48 |
| ${}^{117}$Cd | 117 | 69 | 151.8696 | -847092175.04 | 109739.7328 | +7725927.70 | 9.30 |
| ${}^{118}$Cd | 118 | 70 | 157.9297 | -842317039.80 | 110673.2382 | +7681313.29 | 182.10 |
| ${}^{119}$Cd | 119 | 71 | 163.9802 | -837145349.57 | 111606.7531 | +7610171.66 | 340.32 |
| ${}^{120}$Cd | 120 | 72 | 170.0213 | -832485244.88 | 112540.2774 | +7564705.74 | 33.36 |
| ${}^{121}$Cd | 121 | 73 | 176.0531 | -827424383.56 | 113473.8110 | +7494454.54 | 17.24 |
| ${}^{122}$Cd | 122 | 74 | 182.0759 | -822842054.40 | 114407.3536 | +7446925.75 | 20.24 |
| ${}^{123}$Cd | 123 | 75 | 188.0899 | -817854207.33 | 115340.9051 | +7376168.96 | 23.54 |
| ${}^{124}$Cd | 124 | 76 | 194.0951 | -813368361.90 | 116274.4653 | +7328305.93 | 22.60 |
| ${}^{125}$Cd | 125 | 77 | 200.0917 | -808471555.95 | 117208.0341 | +7258460.10 | 24.82 |
| ${}^{126}$Cd | 126 | 78 | 206.0799 | -804048616.91 | 118141.6113 | +7209196.59 | 19.64 |
| ${}^{127}$Cd | 127 | 79 | 212.0599 | -799232447.56 | 119075.1967 | +7140146.71 | 52.44 |
| ${}^{128}$Cd | 128 | 80 | 218.0318 | -794854318.58 | 120008.7903 | +7089248.60 | 53.98 |
| ${}^{129}$Cd | 129 | 81 | 223.9956 | -790024327.72 | 120942.3918 | +7017296.32 | 44.21 |
| ${}^{130}$Cd | 130 | 82 | 229.9517 | -785660030.51 | 121876.0012 | +6964088.47 | 184.71 |
| ${}^{131}$Cd | 131 | 83 | 235.9001 | -780558452.79 | 122809.6183 | +6879551.56 | 157.73 |
| ${}^{132}$Cd | 132 | 84 | 241.8408 | -775725823.45 | 123743.2429 | +6805863.83 | 488.72 |
| ${}^{133}$Cd | 133 | 85 | 247.7742 | -770599193.01 | 124676.8750 | +6720511.97 | 1617.12 |
| ${}^{134}$Cd | 134 | 86 | 253.7003 | -765856354.48 | 125610.5143 | +6649778.88 | 2403.74 |
| ${}^{135}$Cd | 135 | 87 | 259.6191 | -760688817.55 | 126544.1609 | +6564464.54 | 3178.61 |

### Indium (Z = 49)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{96}$In | 96 | 47 | 4.6704 | -993970707.93 | 90155.2758 | +8613621.63 | 5596.13 |
| ${}^{97}$In | 97 | 48 | 11.0333 | -986069171.40 | 91088.4783 | +8647562.03 | 4435.32 |
| ${}^{98}$In | 98 | 49 | 17.3806 | -978450452.44 | 92021.6965 | +8650214.22 | 3338.71 |
| ${}^{99}$In | 99 | 50 | 23.7126 | -971155864.14 | 92954.9298 | +8663407.91 | 3234.48 |
| ${}^{100}$In | 100 | 51 | 30.0299 | -963948663.65 | 93888.1780 | +8625920.43 | 24.02 |
| ${}^{101}$In | 101 | 52 | 36.3325 | -957023918.09 | 94821.4408 | +8606115.24 | 124.04 |
| ${}^{102}$In | 102 | 53 | 42.6210 | -950187822.32 | 95754.7177 | +8563297.40 | 48.16 |
| ${}^{103}$In | 103 | 54 | 48.8956 | -943645515.31 | 96688.0086 | +8540258.78 | 93.67 |
| ${}^{104}$In | 104 | 55 | 55.1566 | -937126663.90 | 97621.3130 | +8492930.47 | 59.66 |
| ${}^{105}$In | 105 | 56 | 61.4042 | -930912852.96 | 98554.6308 | +8466323.77 | 104.85 |
| ${}^{106}$In | 106 | 57 | 67.6389 | -924664261.06 | 99487.9615 | +8414894.32 | 123.92 |
| ${}^{107}$In | 107 | 58 | 73.8608 | -918732693.77 | 100421.3050 | +8384713.33 | 96.93 |
| ${}^{108}$In | 108 | 59 | 80.0703 | -912728729.31 | 101354.6610 | +8331084.31 | 85.96 |
| ${}^{109}$In | 109 | 60 | 86.2675 | -907032131.74 | 102288.0292 | +8296614.55 | 39.13 |
| ${}^{110}$In | 110 | 61 | 92.4528 | -901223548.19 | 103221.4093 | +8239356.87 | 112.84 |
| ${}^{111}$In | 111 | 62 | 98.6263 | -895740894.55 | 104154.8012 | +8202193.70 | 33.14 |
| ${}^{112}$In | 112 | 63 | 104.7884 | -890117750.14 | 105088.2046 | +8143326.57 | 40.78 |
| ${}^{113}$In | 113 | 64 | 110.9392 | -884809191.46 | 106021.6192 | +8102661.18 | 1.79 |
| ${}^{114}$In | 114 | 65 | 117.0790 | -879345368.27 | 106955.0448 | +8042154.73 | 2.84 |
| ${}^{115}$In | 115 | 66 | 123.2080 | -874200873.78 | 107888.4812 | +7999414.62 | 0.10 |
| ${}^{116}$In | 116 | 67 | 129.3264 | -868862249.68 | 108821.9282 | +7936474.11 | 2.04 |
| ${}^{117}$In | 117 | 68 | 135.4344 | -863878453.60 | 109755.3856 | +7893031.79 | 44.81 |
| ${}^{118}$In | 118 | 69 | 141.5323 | -858652727.59 | 110688.8532 | +7828320.29 | 70.58 |
| ${}^{119}$In | 119 | 70 | 147.6201 | -853819872.61 | 111622.3308 | +7784673.07 | 65.99 |
| ${}^{120}$In | 120 | 71 | 153.6981 | -848715041.21 | 112555.8183 | +7719814.06 | 358.22 |
| ${}^{121}$In | 121 | 72 | 159.7665 | -843997709.68 | 113489.3153 | +7674705.44 | 243.45 |
| ${}^{122}$In | 122 | 73 | 165.8254 | -838994613.42 | 114422.8218 | +7609389.66 | 440.82 |
| ${}^{123}$In | 123 | 74 | 171.8751 | -834395686.56 | 115356.3375 | +7563884.75 | 173.22 |
| ${}^{124}$In | 124 | 75 | 177.9157 | -829480784.40 | 116289.8623 | +7498078.86 | 264.77 |
| ${}^{125}$In | 125 | 76 | 183.9473 | -824977420.21 | 117223.3961 | +7451638.49 | 15.21 |
| ${}^{126}$In | 126 | 77 | 189.9702 | -820182364.66 | 118156.9387 | +7387566.42 | 35.74 |
| ${}^{127}$In | 127 | 78 | 195.9845 | -815735183.81 | 119090.4898 | +7338838.42 | 84.59 |
| ${}^{128}$In | 128 | 79 | 201.9903 | -811044585.23 | 120024.0494 | +7276063.41 | 11.09 |
| ${}^{129}$In | 129 | 80 | 207.9878 | -806648892.49 | 120957.6174 | +7225527.37 | 16.41 |
| ${}^{130}$In | 130 | 81 | 213.9771 | -802027571.18 | 121891.1935 | +7162746.14 | 14.79 |
| ${}^{131}$In | 131 | 82 | 219.9584 | -797652340.76 | 122824.7776 | +7109632.04 | 18.08 |
| ${}^{132}$In | 132 | 83 | 225.9318 | -792626197.87 | 123758.3696 | +7026818.20 | 488.48 |
| ${}^{133}$In | 133 | 84 | 231.8975 | -787807001.13 | 124691.9694 | +6952569.56 | 1617.29 |
| ${}^{134}$In | 134 | 85 | 237.8555 | -782816471.98 | 125625.5768 | +6871434.55 | 1605.15 |
| ${}^{135}$In | 135 | 86 | 243.8060 | -778027207.12 | 126559.1917 | +6798462.48 | 2386.08 |
| ${}^{136}$In | 136 | 87 | 249.7492 | -773032838.77 | 127492.8139 | +6716446.05 | 2368.41 |
| ${}^{137}$In | 137 | 88 | 255.6852 | -768245996.47 | 128426.4434 | +6643585.59 | 3132.27 |

### Tin (Z = 50)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{99}$Sn | 99 | 49 | 6.2125 | -992310640.37 | 92971.6476 | +8698149.74 | 6316.42 |
| ${}^{100}$Sn | 100 | 50 | 12.5775 | -984757568.56 | 93904.8481 | +8728822.66 | 2578.19 |
| ${}^{101}$Sn | 101 | 51 | 18.9273 | -977370293.10 | 94838.0637 | +8694529.14 | 3190.84 |
| ${}^{102}$Sn | 102 | 52 | 25.2623 | -970247872.02 | 95771.2941 | +8676697.56 | 1054.31 |
| ${}^{103}$Sn | 103 | 53 | 31.5828 | -963247121.89 | 96704.5390 | +8633361.30 | 1049.28 |
| ${}^{104}$Sn | 104 | 54 | 37.8892 | -956545469.74 | 97637.7981 | +8615764.02 | 59.34 |
| ${}^{105}$Sn | 105 | 55 | 44.1817 | -949890880.30 | 98571.0710 | +8569505.34 | 40.63 |
| ${}^{106}$Sn | 106 | 56 | 50.4606 | -943543501.46 | 99504.3575 | +8547815.44 | 51.60 |
| ${}^{107}$Sn | 107 | 57 | 56.7263 | -937182033.77 | 100437.6573 | +8497729.44 | 53.31 |
| ${}^{108}$Sn | 108 | 58 | 62.9789 | -931144623.71 | 101370.9700 | +8472769.24 | 53.54 |
| ${}^{109}$Sn | 109 | 59 | 69.2188 | -925029941.31 | 102304.2955 | +8418595.19 | 78.35 |
| ${}^{110}$Sn | 110 | 60 | 75.4463 | -919271600.04 | 103237.6335 | +8391644.52 | 134.57 |
| ${}^{111}$Sn | 111 | 61 | 81.6616 | -913378257.23 | 104170.9836 | +8334889.97 | 51.65 |
| ${}^{112}$Sn | 112 | 62 | 87.8649 | -907852614.46 | 105104.3458 | +8304605.94 | 2.81 |
| ${}^{113}$Sn | 113 | 63 | 94.0564 | -902153956.14 | 106037.7196 | +8245791.14 | 14.97 |
| ${}^{114}$Sn | 114 | 64 | 100.2365 | -896830643.12 | 106971.1050 | +8212429.47 | 0.27 |
| ${}^{115}$Sn | 115 | 65 | 106.4053 | -891325313.28 | 107904.5015 | +8153778.27 | 0.14 |
| ${}^{116}$Sn | 116 | 66 | 112.5631 | -886148238.56 | 108837.9092 | +8115085.30 | 0.89 |
| ${}^{117}$Sn | 117 | 67 | 118.7101 | -880768223.97 | 109771.3277 | +8052894.94 | 4.43 |
| ${}^{118}$Sn | 118 | 68 | 124.8464 | -875768644.34 | 110704.7567 | +8013732.19 | 4.55 |
| ${}^{119}$Sn | 119 | 69 | 130.9724 | -870508319.11 | 111638.1962 | +7949448.36 | 6.54 |
| ${}^{120}$Sn | 120 | 70 | 137.0881 | -865670871.79 | 112571.6460 | +7909978.80 | 8.23 |
| ${}^{121}$Sn | 121 | 71 | 143.1937 | -860531303.57 | 113505.1057 | +7844994.72 | 8.68 |
| ${}^{122}$Sn | 122 | 72 | 149.2896 | -855831775.59 | 114438.5753 | +7804635.12 | 21.55 |
| ${}^{123}$Sn | 123 | 73 | 155.3758 | -850811032.54 | 115372.0545 | +7739765.24 | 21.65 |
| ${}^{124}$Sn | 124 | 74 | 161.4525 | -846229545.34 | 116305.5433 | +7698221.05 | 11.38 |
| ${}^{125}$Sn | 125 | 75 | 167.5198 | -841317361.16 | 117239.0413 | +7633565.45 | 11.42 |
| ${}^{126}$Sn | 126 | 76 | 173.5781 | -836844883.41 | 118172.5485 | +7591145.14 | 91.12 |
| ${}^{127}$Sn | 127 | 77 | 179.6274 | -832031275.10 | 119106.0646 | +7526738.24 | 78.04 |
| ${}^{128}$Sn | 128 | 78 | 185.6678 | -827666123.47 | 120039.5896 | +7484024.82 | 148.40 |
| ${}^{129}$Sn | 129 | 79 | 191.6996 | -822938618.68 | 120973.1232 | +7419707.40 | 143.82 |
| ${}^{130}$Sn | 130 | 80 | 197.7229 | -818650450.27 | 121906.6653 | +7375702.92 | 15.47 |
| ${}^{131}$Sn | 131 | 81 | 203.7378 | -814021252.74 | 122840.2158 | +7312538.38 | 29.69 |
| ${}^{132}$Sn | 132 | 82 | 209.7445 | -809814713.69 | 123773.7745 | +7268021.61 | 16.08 |
| ${}^{133}$Sn | 133 | 83 | 215.7432 | -804800026.43 | 124707.3413 | +7183935.80 | 15.37 |
| ${}^{134}$Sn | 134 | 84 | 221.7339 | -800036738.62 | 125640.9161 | +7111126.82 | 25.39 |
| ${}^{135}$Sn | 135 | 85 | 227.7168 | -795060773.80 | 126574.4986 | +7028556.91 | 24.46 |
| ${}^{136}$Sn | 136 | 86 | 233.6920 | -790371689.14 | 127508.0888 | +6957920.01 | 1581.58 |
| ${}^{137}$Sn | 137 | 87 | 239.6596 | -785409673.65 | 128441.6866 | +6876081.13 | 2351.29 |
| ${}^{138}$Sn | 138 | 88 | 245.6199 | -780752142.79 | 129375.2918 | +6806310.09 | 3109.80 |
| ${}^{139}$Sn | 139 | 89 | 251.5728 | -775811185.98 | 130308.9042 | +6725469.45 | 3087.27 |
| ${}^{140}$Sn | 140 | 90 | 257.5186 | -771159704.49 | 131242.5239 | +6656505.62 | 2300.61 |

### Antimony (Z = 51)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{102}$Sb | 102 | 51 | 7.6014 | -990890712.08 | 95788.1727 | +8707484.52 | 4208.15 |
| ${}^{103}$Sb | 103 | 52 | 13.9688 | -983529381.01 | 96721.3707 | +8699264.20 | 3128.06 |
| ${}^{104}$Sb | 104 | 53 | 20.3214 | -976338298.24 | 97654.5835 | +8660666.58 | 1048.72 |
| ${}^{105}$Sb | 105 | 54 | 26.6597 | -969413113.82 | 98587.8107 | +8644572.43 | 223.30 |
| ${}^{106}$Sb | 106 | 55 | 32.9838 | -962609089.05 | 99521.0520 | +8605796.42 | 75.52 |
| ${}^{107}$Sb | 107 | 56 | 39.2941 | -956065816.94 | 100454.3071 | +8585321.38 | 41.64 |
| ${}^{108}$Sb | 108 | 57 | 45.5908 | -949581517.55 | 101387.5758 | +8541402.33 | 54.67 |
| ${}^{109}$Sb | 109 | 58 | 51.8743 | -943376374.05 | 102320.8577 | +8518433.88 | 51.89 |
| ${}^{110}$Sb | 110 | 59 | 58.1448 | -937167541.55 | 103254.1526 | +8470330.94 | 58.23 |
| ${}^{111}$Sb | 111 | 60 | 64.4027 | -931256411.87 | 104187.4602 | +8444576.03 | 85.65 |
| ${}^{112}$Sb | 112 | 61 | 70.6480 | -925294488.78 | 105120.7803 | +8394008.47 | 171.03 |
| ${}^{113}$Sb | 113 | 62 | 76.8812 | -919628796.90 | 106054.1125 | +8364161.27 | 163.47 |
| ${}^{114}$Sb | 114 | 63 | 83.1024 | -913859192.81 | 106987.4568 | +8308926.54 | 186.34 |
| ${}^{115}$Sb | 115 | 64 | 89.3118 | -908426776.36 | 107920.8127 | +8277626.02 | 149.71 |
| ${}^{116}$Sb | 116 | 65 | 95.5098 | -902857718.06 | 108854.1802 | +8221866.96 | 47.74 |
| ${}^{117}$Sb | 117 | 66 | 101.6965 | -897595245.45 | 109787.5589 | +8185671.75 | 77.47 |
| ${}^{118}$Sb | 118 | 67 | 107.8722 | -892183025.88 | 110720.9487 | +8127600.55 | 27.45 |
| ${}^{119}$Sb | 119 | 68 | 114.0370 | -887099100.81 | 111654.3493 | +8089924.47 | 63.18 |
| ${}^{120}$Sb | 120 | 69 | 120.1912 | -881826726.14 | 112587.7605 | +8030067.00 | 64.45 |
| ${}^{121}$Sb | 121 | 70 | 126.3349 | -876906052.18 | 113521.1822 | +7991345.57 | 22.25 |
| ${}^{122}$Sb | 122 | 71 | 132.4684 | -871780235.79 | 114454.6142 | +7931628.42 | 22.04 |
| ${}^{123}$Sb | 123 | 72 | 138.5918 | -867006603.60 | 115388.0562 | +7891931.88 | 11.85 |
| ${}^{124}$Sb | 124 | 73 | 144.7054 | -861996485.19 | 116321.5080 | +7831195.88 | 11.76 |
| ${}^{125}$Sb | 125 | 74 | 150.8092 | -857359804.28 | 117254.9696 | +7790918.14 | 21.62 |
| ${}^{126}$Sb | 126 | 75 | 156.9036 | -852462063.52 | 118188.4406 | +7729896.84 | 271.54 |
| ${}^{127}$Sb | 127 | 76 | 162.9886 | -847937988.21 | 119121.9211 | +7688391.07 | 43.00 |
| ${}^{128}$Sb | 128 | 77 | 169.0644 | -843147919.11 | 120055.4107 | +7627537.11 | 157.68 |
| ${}^{129}$Sb | 129 | 78 | 175.1312 | -838726932.79 | 120988.9093 | +7585056.70 | 176.76 |
| ${}^{130}$Sb | 130 | 79 | 181.1892 | -834023772.55 | 121922.4167 | +7523793.81 | 117.44 |
| ${}^{131}$Sb | 131 | 80 | 187.2384 | -829694143.55 | 122855.9329 | +7480389.70 | 17.08 |
| ${}^{132}$Sb | 132 | 81 | 193.2791 | -825110460.12 | 123789.4577 | +7420972.93 | 20.07 |
| ${}^{133}$Sb | 133 | 82 | 199.3114 | -820845172.28 | 124722.9908 | +7375818.15 | 25.26 |
| ${}^{134}$Sb | 134 | 83 | 205.3354 | -815954268.72 | 125656.5322 | +7297547.95 | 24.64 |
| ${}^{135}$Sb | 135 | 84 | 211.3513 | -811195484.80 | 126590.0817 | +7225123.50 | 21.00 |
| ${}^{136}$Sb | 136 | 85 | 217.3592 | -806328140.46 | 127523.6393 | +7147033.67 | 46.04 |
| ${}^{137}$Sb | 137 | 86 | 223.3592 | -801622690.01 | 128457.2046 | +7075970.66 | 408.95 |
| ${}^{138}$Sb | 138 | 87 | 229.3515 | -796775790.27 | 129390.7778 | +6998447.52 | 2334.33 |
| ${}^{139}$Sb | 139 | 88 | 235.3362 | -792108736.21 | 130324.3585 | +6928413.69 | 3087.52 |
| ${}^{140}$Sb | 140 | 89 | 241.3135 | -787280311.37 | 131257.9467 | +6851255.89 | 4601.57 |
| ${}^{141}$Sb | 141 | 90 | 247.2833 | -782651804.76 | 132191.5422 | +6781462.26 | 3809.66 |
| ${}^{142}$Sb | 142 | 91 | 253.2460 | -777822049.61 | 133125.1450 | +6704492.92 | 2268.18 |

### Tellurium (Z = 52)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{104}$Te | 104 | 52 | 2.4533 | -997108150.47 | 97671.6692 | +8736407.43 | 3280.21 |
| ${}^{105}$Te | 105 | 53 | 8.8382 | -989718428.85 | 98604.8498 | +8703273.47 | 3069.12 |
| ${}^{106}$Te | 106 | 54 | 15.2084 | -982581075.09 | 99538.0450 | +8693640.27 | 1018.85 |
| ${}^{107}$Te | 107 | 55 | 21.5642 | -975595191.53 | 100471.2546 | +8654245.22 | 1009.96 |
| ${}^{108}$Te | 108 | 56 | 27.9060 | -968882791.81 | 101404.4783 | +8642679.12 | 53.81 |
| ${}^{109}$Te | 109 | 57 | 34.2339 | -962247835.07 | 102337.7158 | +8599740.19 | 43.18 |
| ${}^{110}$Te | 110 | 58 | 40.5484 | -955896561.32 | 103270.9667 | +8583132.49 | 64.21 |
| ${}^{111}$Te | 111 | 59 | 46.8496 | -949560169.33 | 104204.2309 | +8536136.53 | 62.21 |
| ${}^{112}$Te | 112 | 60 | 53.1379 | -943522793.09 | 105137.5081 | +8515471.65 | 80.42 |
| ${}^{113}$Te | 113 | 61 | 59.4135 | -937441334.52 | 106070.7979 | +8464604.68 | 265.68 |
| ${}^{114}$Te | 114 | 62 | 65.6766 | -931682089.41 | 107004.1002 | +8441006.95 | 230.21 |
| ${}^{115}$Te | 115 | 63 | 71.9275 | -925815959.36 | 107937.4147 | +8386187.94 | 261.07 |
| ${}^{116}$Te | 116 | 64 | 78.1665 | -920307753.39 | 108870.7411 | +8360703.79 | 224.19 |
| ${}^{117}$Te | 117 | 65 | 84.3938 | -914646668.30 | 109804.0793 | +8304564.27 | 123.55 |
| ${}^{118}$Te | 118 | 66 | 90.6095 | -909338288.49 | 110737.4290 | +8274851.84 | 166.68 |
| ${}^{119}$Te | 119 | 67 | 96.8140 | -903857795.89 | 111670.7899 | +8217488.94 | 65.71 |
| ${}^{120}$Te | 120 | 68 | 103.0074 | -898738194.71 | 112604.1620 | +8185444.03 | 15.68 |
| ${}^{121}$Te | 121 | 69 | 109.1899 | -893420268.72 | 113537.5448 | +8127181.38 | 229.39 |
| ${}^{122}$Te | 122 | 70 | 115.3618 | -888467330.17 | 114470.9384 | +8092955.37 | 11.94 |
| ${}^{123}$Te | 123 | 71 | 121.5232 | -883292244.36 | 115404.3424 | +8033731.72 | 11.83 |
| ${}^{124}$Te | 124 | 72 | 127.6744 | -878484672.09 | 116337.7566 | +7997348.34 | 11.71 |
| ${}^{125}$Te | 125 | 73 | 133.8155 | -873431162.39 | 117271.1810 | +7936895.06 | 11.62 |
| ${}^{126}$Te | 126 | 74 | 139.9467 | -868763292.42 | 118204.6152 | +7899357.11 | 11.54 |
| ${}^{127}$Te | 127 | 75 | 146.0681 | -863825747.91 | 119138.0592 | +7838397.71 | 11.54 |
| ${}^{128}$Te | 128 | 76 | 152.1800 | -859280266.65 | 120071.5127 | +7799594.34 | 5.93 |
| ${}^{129}$Te | 129 | 77 | 158.2825 | -854455897.96 | 121004.9756 | +7738791.84 | 5.92 |
| ${}^{130}$Te | 130 | 78 | 164.3758 | -850014135.52 | 121938.4477 | +7698464.72 | 0.08 |
| ${}^{131}$Te | 131 | 79 | 170.4601 | -845299493.91 | 122871.9289 | +7638251.46 | 0.50 |
| ${}^{132}$Te | 132 | 80 | 176.5355 | -840947607.84 | 123805.4190 | +7596402.89 | 28.37 |
| ${}^{133}$Te | 133 | 81 | 182.6021 | -836340012.80 | 124738.9178 | +7537120.88 | 16.69 |
| ${}^{134}$Te | 134 | 82 | 188.6601 | -832064566.05 | 125672.4252 | +7493718.67 | 22.01 |
| ${}^{135}$Te | 135 | 83 | 194.7096 | -827182043.73 | 126605.9411 | +7415742.65 | 13.70 |
| ${}^{136}$Te | 136 | 84 | 200.7509 | -822570871.13 | 127539.4653 | +7350931.57 | 18.01 |
| ${}^{137}$Te | 137 | 85 | 206.7839 | -817713921.99 | 128472.9976 | +7272776.96 | 16.46 |
| ${}^{138}$Te | 138 | 86 | 212.8089 | -813137941.27 | 129406.5380 | +7207691.10 | 29.47 |
| ${}^{139}$Te | 139 | 87 | 218.8261 | -808288840.64 | 130340.0863 | +7128952.02 | 27.35 |
| ${}^{140}$Te | 140 | 88 | 224.8354 | -803752022.86 | 131273.6424 | +7064177.14 | 110.29 |
| ${}^{141}$Te | 141 | 89 | 230.8371 | -798926244.05 | 132207.2061 | +6986115.18 | 3043.73 |
| ${}^{142}$Te | 142 | 90 | 236.8313 | -794425523.73 | 133140.7774 | +6921232.55 | 3783.02 |
| ${}^{143}$Te | 143 | 91 | 242.8180 | -789587611.24 | 134074.3561 | +6842956.44 | 3756.39 |
| ${}^{144}$Te | 144 | 92 | 248.7975 | -785104463.98 | 135007.9420 | +6778661.92 | 2236.72 |
| ${}^{145}$Te | 145 | 93 | 254.7697 | -780315998.95 | 135941.5352 | +6701145.10 | 2221.18 |

### Iodine (Z = 53)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{106}$I | 106 | 53 | -2.8655 | -1003341893.36 | 99555.3365 | +8716353.04 | 4048.95 |
| ${}^{107}$I | 107 | 54 | 3.5368 | -995942289.48 | 100488.4997 | +8713677.29 | 3010.84 |
| ${}^{108}$I | 108 | 55 | 9.9244 | -988760692.58 | 101421.6775 | +8683217.94 | 1009.79 |
| ${}^{109}$I | 109 | 56 | 16.2977 | -981810258.13 | 102354.8697 | +8668965.55 | 66.30 |
| ${}^{110}$I | 110 | 57 | 22.6569 | -975015756.03 | 103288.0759 | +8634362.91 | 604.85 |
| ${}^{111}$I | 111 | 58 | 29.0024 | -968455252.63 | 104221.2958 | +8617017.15 | 46.00 |
| ${}^{112}$I | 112 | 59 | 35.3345 | -961989069.46 | 105154.5292 | +8577119.98 | 98.28 |
| ${}^{113}$I | 113 | 60 | 41.6533 | -955768651.91 | 106087.7758 | +8556717.59 | 76.16 |
| ${}^{114}$I | 114 | 61 | 47.9592 | -949585895.49 | 107021.0353 | +8512684.48 | 188.73 |
| ${}^{115}$I | 115 | 62 | 54.2524 | -943667524.83 | 107954.3075 | +8490067.40 | 269.76 |
| ${}^{116}$I | 116 | 63 | 60.5332 | -937737739.77 | 108887.5921 | +8443521.15 | 694.94 |
| ${}^{117}$I | 117 | 64 | 66.8018 | -932064952.60 | 109820.8890 | +8415799.84 | 234.68 |
| ${}^{118}$I | 118 | 65 | 73.0584 | -926346618.74 | 110754.1977 | +8365837.58 | 179.90 |
| ${}^{119}$I | 119 | 66 | 79.3033 | -920918105.70 | 111687.5182 | +8337523.61 | 195.96 |
| ${}^{120}$I | 120 | 67 | 85.5367 | -915380603.80 | 112620.8503 | +8284170.80 | 135.20 |
| ${}^{121}$I | 121 | 68 | 91.7589 | -910164570.76 | 113554.1936 | +8254441.27 | 41.93 |
| ${}^{122}$I | 122 | 69 | 97.9699 | -904820340.83 | 114487.5479 | +8201635.45 | 45.62 |
| ${}^{123}$I | 123 | 70 | 104.1701 | -899764198.85 | 115420.9132 | +8167657.10 | 32.19 |
| ${}^{124}$I | 124 | 71 | 110.3596 | -894568655.16 | 116354.2891 | +8112994.37 | 19.91 |
| ${}^{125}$I | 125 | 72 | 116.5386 | -889671394.31 | 117287.6755 | +8077054.77 | 11.62 |
| ${}^{126}$I | 126 | 73 | 122.7073 | -884611980.82 | 118221.0722 | +8021170.37 | 32.21 |
| ${}^{127}$I | 127 | 74 | 128.8660 | -879853801.92 | 119154.4790 | +7983291.84 | 30.63 |
| ${}^{128}$I | 128 | 75 | 135.0147 | -874917217.49 | 120087.8957 | +7926478.89 | 30.39 |
| ${}^{129}$I | 129 | 76 | 141.1536 | -870292187.54 | 121021.3222 | +7887537.55 | 26.26 |
| ${}^{130}$I | 130 | 77 | 147.2830 | -865463455.96 | 121954.7583 | +7829783.85 | 26.06 |
| ${}^{131}$I | 131 | 78 | 153.4029 | -860962575.94 | 122888.2038 | +7790161.16 | 4.96 |
| ${}^{132}$I | 132 | 79 | 159.5136 | -856249119.57 | 123821.6585 | +7732795.19 | 33.08 |
| ${}^{133}$I | 133 | 80 | 165.6152 | -851848606.08 | 124755.1223 | +7691775.53 | 47.66 |
| ${}^{134}$I | 134 | 81 | 171.7079 | -847253417.97 | 125688.5950 | +7635544.81 | 38.93 |
| ${}^{135}$I | 135 | 82 | 177.7918 | -842932192.17 | 126622.0766 | +7592643.62 | 16.39 |
| ${}^{136}$I | 136 | 83 | 183.8670 | -838113907.26 | 127555.5668 | +7518850.13 | 112.06 |
| ${}^{137}$I | 137 | 84 | 189.9337 | -833488212.62 | 128489.0655 | +7454460.69 | 65.73 |
| ${}^{138}$I | 138 | 85 | 195.9921 | -828731716.13 | 129422.5725 | +7381762.56 | 46.40 |
| ${}^{139}$I | 139 | 86 | 202.0423 | -824145864.59 | 130356.0877 | +7316931.28 | 30.95 |
| ${}^{140}$I | 140 | 87 | 208.0844 | -819391010.86 | 131289.6111 | +7242615.17 | 92.90 |
| ${}^{141}$I | 141 | 88 | 214.1185 | -814859362.14 | 132223.1424 | +7178512.34 | 120.62 |
| ${}^{142}$I | 142 | 89 | 220.1448 | -810132551.48 | 133156.6815 | +7104375.34 | 37.34 |
| ${}^{143}$I | 143 | 90 | 226.1634 | -805633252.32 | 134090.2283 | +7039737.40 | 1504.07 |
| ${}^{144}$I | 144 | 91 | 232.1744 | -800898700.83 | 135023.7827 | +6965197.13 | 2980.17 |
| ${}^{145}$I | 145 | 92 | 238.1780 | -796429956.43 | 135957.3446 | +6901137.85 | 3704.58 |
| ${}^{146}$I | 146 | 93 | 244.1742 | -791753719.06 | 136890.9138 | +6827722.57 | 2206.06 |
| ${}^{147}$I | 147 | 94 | 250.1632 | -787302813.27 | 137824.4903 | +6764558.18 | 2190.98 |

### Xenon (Z = 54)

_43 of 43 isotopes with a framework prediction; 43 of 43 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{108}$Xe | 108 | 54 | -8.3539 | -1009579212.22 | 101439.1735 | +8755507.01 | 3773.88 |
| ${}^{109}$Xe | 109 | 55 | -1.9344 | -1002189027.59 | 102372.3195 | +8726580.02 | 2957.11 |
| ${}^{110}$Xe | 110 | 56 | 4.4705 | -995019095.34 | 103305.4800 | +8720144.81 | 986.09 |
| ${}^{111}$Xe | 111 | 57 | 10.8611 | -988041109.58 | 104238.6548 | +8683163.46 | 1117.71 |
| ${}^{112}$Xe | 112 | 58 | 17.2377 | -981299270.05 | 105171.8436 | +8675108.97 | 79.43 |
| ${}^{113}$Xe | 113 | 59 | 23.6006 | -974677851.85 | 106105.0461 | +8635409.51 | 65.01 |
| ${}^{114}$Xe | 114 | 60 | 29.9501 | -968305715.32 | 107038.2620 | +8622240.21 | 105.33 |
| ${}^{115}$Xe | 115 | 61 | 36.2864 | -961988262.14 | 107971.4911 | +8578223.20 | 113.12 |
| ${}^{116}$Xe | 116 | 62 | 42.6098 | -955939367.98 | 108904.7331 | +8561415.79 | 120.55 |
| ${}^{117}$Xe | 117 | 63 | 48.9206 | -949890964.48 | 109837.9878 | +8514899.53 | 95.29 |
| ${}^{118}$Xe | 118 | 64 | 55.2189 | -944124428.97 | 110771.2549 | +8494581.39 | 94.48 |
| ${}^{119}$Xe | 119 | 65 | 61.5051 | -938312014.25 | 111704.5342 | +8445777.34 | 93.69 |
| ${}^{120}$Xe | 120 | 66 | 67.7792 | -932790944.25 | 112637.8254 | +8421930.80 | 105.79 |
| ${}^{121}$Xe | 121 | 67 | 74.0417 | -927186198.58 | 113571.1284 | +8371100.19 | 90.93 |
| ${}^{122}$Xe | 122 | 68 | 80.2927 | -921879775.54 | 114504.4428 | +8343984.09 | 97.84 |
| ${}^{123}$Xe | 123 | 69 | 86.5323 | -916456322.07 | 115437.7686 | +8291154.88 | 83.27 |
| ${}^{124}$Xe | 124 | 70 | 92.7609 | -911340820.75 | 116371.1054 | +8261339.52 | 11.76 |
| ${}^{125}$Xe | 125 | 71 | 98.9786 | -906080582.45 | 117304.4532 | +8207074.83 | 12.15 |
| ${}^{126}$Xe | 126 | 72 | 105.1856 | -901130721.63 | 118237.8116 | +8174524.09 | 0.05 |
| ${}^{127}$Xe | 127 | 73 | 111.3821 | -896014526.19 | 119171.1805 | +8118929.13 | 34.58 |
| ${}^{128}$Xe | 128 | 74 | 117.5683 | -891215237.45 | 120104.5597 | +8084302.54 | 0.04 |
| ${}^{129}$Xe | 129 | 75 | 123.7444 | -886227686.81 | 121037.9491 | +8027594.97 | 0.04 |
| ${}^{130}$Xe | 130 | 76 | 129.9105 | -881566325.16 | 121971.3484 | +7991409.98 | 0.08 |
| ${}^{131}$Xe | 131 | 77 | 136.0668 | -876696270.85 | 122904.7575 | +7933941.17 | 0.04 |
| ${}^{132}$Xe | 132 | 78 | 142.2136 | -872161402.04 | 123838.1762 | +7896554.99 | 0.04 |
| ${}^{133}$Xe | 133 | 79 | 148.3508 | -867411550.83 | 124771.6043 | +7839448.35 | 19.38 |
| ${}^{134}$Xe | 134 | 80 | 154.4788 | -862982124.91 | 125705.0417 | +7800380.24 | 0.04 |
| ${}^{135}$Xe | 135 | 81 | 160.5977 | -858353778.38 | 126638.4883 | +7744363.28 | 29.19 |
| ${}^{136}$Xe | 136 | 82 | 166.7076 | -854006230.39 | 127571.9438 | +7702999.84 | 0.05 |
| ${}^{137}$Xe | 137 | 83 | 172.8087 | -849194878.50 | 128505.4082 | +7630218.52 | 0.81 |
| ${}^{138}$Xe | 138 | 84 | 178.9011 | -844645591.75 | 129438.8812 | +7571384.83 | 21.83 |
| ${}^{139}$Xe | 139 | 85 | 184.9849 | -839883015.48 | 130372.3628 | +7498544.73 | 16.56 |
| ${}^{140}$Xe | 140 | 86 | 191.0604 | -835395549.40 | 131305.8528 | +7439719.61 | 17.87 |
| ${}^{141}$Xe | 141 | 87 | 197.1276 | -830647353.61 | 132239.3510 | +7365441.21 | 22.00 |
| ${}^{142}$Xe | 142 | 88 | 203.1866 | -826204021.39 | 133172.8573 | +7306154.42 | 20.43 |
| ${}^{143}$Xe | 143 | 89 | 209.2377 | -821493100.21 | 134106.3717 | +7232182.53 | 34.98 |
| ${}^{144}$Xe | 144 | 90 | 215.2809 | -817077303.24 | 135039.8939 | +7172043.99 | 39.60 |
| ${}^{145}$Xe | 145 | 91 | 221.3163 | -812378250.89 | 135973.4239 | +7097516.24 | 82.79 |
| ${}^{146}$Xe | 146 | 92 | 227.3441 | -808005951.02 | 136906.9615 | +7037705.49 | 178.15 |
| ${}^{147}$Xe | 147 | 93 | 233.3644 | -803330894.05 | 137840.5067 | +6963930.47 | 1463.04 |
| ${}^{148}$Xe | 148 | 94 | 239.3773 | -799004063.69 | 138774.0592 | +6904399.15 | 2176.29 |
| ${}^{149}$Xe | 149 | 95 | 245.3829 | -794373161.80 | 139707.6190 | +6831941.28 | 2161.59 |
| ${}^{150}$Xe | 150 | 96 | 251.3814 | -790069408.83 | 140641.1860 | +6772322.00 | 2147.11 |

### Caesium (Z = 55)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{111}$Cs | 111 | 56 | -7.5744 | -1008455726.35 | 104256.3079 | +8740557.56 | 1937.74 |
| ${}^{112}$Cs | 112 | 57 | -1.1523 | -1001269865.55 | 105189.4513 | +8712294.56 | 1107.64 |
| ${}^{113}$Cs | 113 | 58 | 5.2555 | -994292381.91 | 106122.6088 | +8702263.68 | 81.52 |
| ${}^{114}$Cs | 114 | 59 | 11.6494 | -987497739.39 | 107055.7804 | +8669457.75 | 801.49 |
| ${}^{115}$Cs | 115 | 60 | 18.0297 | -980917746.49 | 107988.9656 | +8657058.71 | 957.06 |
| ${}^{116}$Cs | 116 | 61 | 24.3965 | -974460875.50 | 108922.1641 | +8620050.91 | 931.57 |
| ${}^{117}$Cs | 117 | 62 | 30.7502 | -968226981.72 | 109855.3759 | +8603317.38 | 573.00 |
| ${}^{118}$Cs | 118 | 63 | 37.0910 | -962066740.34 | 110788.6005 | +8563711.22 | 116.09 |
| ${}^{119}$Cs | 119 | 64 | 43.4191 | -956131780.03 | 111721.8378 | +8542904.89 | 125.84 |
| ${}^{120}$Cs | 120 | 65 | 49.7349 | -950236144.32 | 112655.0875 | +8501680.59 | 89.24 |
| ${}^{121}$Cs | 121 | 66 | 56.0385 | -944554958.96 | 113588.3493 | +8475840.13 | 126.86 |
| ${}^{122}$Cs | 122 | 67 | 62.3301 | -938881076.51 | 114521.6231 | +8431246.43 | 296.63 |
| ${}^{123}$Cs | 123 | 68 | 68.6100 | -933439194.06 | 115454.9086 | +8403830.59 | 105.77 |
| ${}^{124}$Cs | 124 | 69 | 74.8784 | -927970754.79 | 116388.2056 | +8357722.71 | 79.27 |
| ${}^{125}$Cs | 125 | 70 | 81.1355 | -922726293.58 | 117321.5140 | +8326759.61 | 66.48 |
| ${}^{126}$Cs | 126 | 71 | 87.3815 | -917432804.71 | 118254.8334 | +8278433.29 | 88.32 |
| ${}^{127}$Cs | 127 | 72 | 93.6166 | -912366020.05 | 119188.1637 | +8244849.00 | 47.18 |
| ${}^{128}$Cs | 128 | 73 | 99.8410 | -907213662.34 | 120121.5047 | +8193282.46 | 45.12 |
| ${}^{129}$Cs | 129 | 74 | 106.0549 | -902313865.07 | 121054.8562 | +8158350.61 | 37.92 |
| ${}^{130}$Cs | 130 | 75 | 112.2585 | -897306601.09 | 121988.2181 | +8105991.09 | 69.06 |
| ${}^{131}$Cs | 131 | 76 | 118.4519 | -892547896.64 | 122921.5901 | +8069024.76 | 1.45 |
| ${}^{132}$Cs | 132 | 77 | 124.6353 | -887669129.17 | 123854.9721 | +8015809.71 | 8.43 |
| ${}^{133}$Cs | 133 | 78 | 130.8090 | -883052495.53 | 124788.3639 | +7978302.76 | 0.06 |
| ${}^{134}$Cs | 134 | 79 | 136.9730 | -878291556.70 | 125721.7653 | +7924479.03 | 0.13 |
| ${}^{135}$Cs | 135 | 80 | 143.1275 | -873805410.04 | 126655.1762 | +7886532.28 | 2.89 |
| ${}^{136}$Cs | 136 | 81 | 149.2727 | -869174839.57 | 127588.5964 | +7833821.24 | 14.79 |
| ${}^{137}$Cs | 137 | 82 | 155.4087 | -864778160.86 | 128522.0258 | +7793411.74 | 2.37 |
| ${}^{138}$Cs | 138 | 83 | 161.5358 | -859984572.87 | 129455.4642 | +7723333.41 | 71.29 |
| ${}^{139}$Cs | 139 | 84 | 167.6540 | -855419034.61 | 130388.9114 | +7665805.65 | 24.22 |
| ${}^{140}$Cs | 140 | 85 | 173.7634 | -850719385.28 | 131322.3674 | +7597839.81 | 62.90 |
| ${}^{141}$Cs | 141 | 86 | 179.8643 | -846204653.45 | 132255.8319 | +7539189.23 | 70.05 |
| ${}^{142}$Cs | 142 | 87 | 185.9567 | -841551865.14 | 133189.3049 | +7470835.28 | 53.45 |
| ${}^{143}$Cs | 143 | 88 | 192.0409 | -837094031.99 | 134122.7862 | +7412007.41 | 56.88 |
| ${}^{144}$Cs | 144 | 89 | 198.1168 | -832461045.23 | 135056.2757 | +7342300.86 | 150.15 |
| ${}^{145}$Cs | 145 | 90 | 204.1848 | -828035602.11 | 135989.7732 | +7282478.08 | 67.15 |
| ${}^{146}$Cs | 146 | 91 | 210.2448 | -823426666.40 | 136923.2786 | +7212221.62 | 21.28 |
| ${}^{147}$Cs | 147 | 92 | 216.2970 | -819055096.54 | 137856.7918 | +7152943.97 | 61.25 |
| ${}^{148}$Cs | 148 | 93 | 222.3415 | -814473759.73 | 138790.3127 | +7082696.57 | 94.63 |
| ${}^{149}$Cs | 149 | 94 | 228.3785 | -810139795.12 | 139723.8411 | +7023596.45 | 2880.09 |
| ${}^{150}$Cs | 150 | 95 | 234.4080 | -805607658.91 | 140657.3770 | +6954395.37 | 2860.78 |
| ${}^{151}$Cs | 151 | 96 | 240.4302 | -801291275.11 | 141590.9202 | +6895045.69 | 3557.16 |
| ${}^{152}$Cs | 152 | 97 | 246.4452 | -796823320.69 | 142524.4707 | +6827567.35 | 3533.62 |

### Barium (Z = 56)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{113}$Ba | 113 | 57 | -13.3820 | -1014738635.53 | 106140.4641 | +8756392.39 | 2850.63 |
| ${}^{114}$Ba | 114 | 58 | -6.9429 | -1007528400.32 | 107073.5903 | +8753808.58 | 967.32 |
| ${}^{115}$Ba | 115 | 59 | -0.5179 | -1000554899.88 | 108006.7308 | +8721432.47 | 1870.42 |
| ${}^{116}$Ba | 116 | 60 | 5.8931 | -993775666.19 | 108939.8852 | +8712574.96 | 1854.38 |
| ${}^{117}$Ba | 117 | 61 | 12.2906 | -987170464.28 | 109873.0532 | +8681941.81 | 2298.21 |
| ${}^{118}$Ba | 118 | 62 | 18.6746 | -980763390.43 | 110806.2345 | +8667221.68 | 1823.07 |
| ${}^{119}$Ba | 119 | 63 | 25.0456 | -974476254.39 | 111739.4290 | +8631459.41 | 1807.75 |
| ${}^{120}$Ba | 120 | 64 | 31.4036 | -968395203.10 | 112672.6364 | +8613634.29 | 2687.00 |
| ${}^{121}$Ba | 121 | 65 | 37.7491 | -962384926.12 | 113605.8563 | +8574345.49 | 1259.74 |
| ${}^{122}$Ba | 122 | 66 | 44.0822 | -956590621.10 | 114539.0887 | +8553640.17 | 246.06 |
| ${}^{123}$Ba | 123 | 67 | 50.4030 | -950807848.10 | 115472.3332 | +8508553.97 | 105.76 |
| ${}^{124}$Ba | 124 | 68 | 56.7120 | -945265112.77 | 116405.5897 | +8485168.79 | 108.27 |
| ${}^{125}$Ba | 125 | 69 | 63.0092 | -939690926.37 | 117338.8579 | +8437507.75 | 94.46 |
| ${}^{126}$Ba | 126 | 70 | 69.2950 | -934370091.91 | 118272.1376 | +8411522.94 | 106.55 |
| ${}^{127}$Ba | 127 | 71 | 75.5694 | -928980383.93 | 119205.4286 | +8361706.83 | 96.07 |
| ${}^{128}$Ba | 128 | 72 | 81.8327 | -923854311.72 | 120138.7306 | +8333100.25 | 13.51 |
| ${}^{129}$Ba | 129 | 73 | 88.0852 | -918624227.46 | 121072.0436 | +8281015.66 | 87.47 |
| ${}^{130}$Ba | 130 | 74 | 94.3269 | -913676737.68 | 122005.3674 | +8250686.73 | 2.37 |
| ${}^{131}$Ba | 131 | 75 | 100.5580 | -908601056.27 | 122938.7016 | +8197972.59 | 3.40 |
| ${}^{132}$Ba | 132 | 76 | 106.7789 | -903806054.21 | 123872.0462 | +8165291.08 | 8.57 |
| ${}^{133}$Ba | 133 | 77 | 112.9895 | -898866113.37 | 124805.4010 | +8111706.33 | 8.01 |
| ${}^{134}$Ba | 134 | 78 | 119.1902 | -894212546.45 | 125738.7657 | +8077412.31 | 2.01 |
| ${}^{135}$Ba | 135 | 79 | 125.3811 | -889402233.18 | 126672.1403 | +8023683.17 | 1.95 |
| ${}^{136}$Ba | 136 | 80 | 131.5622 | -884874761.01 | 127605.5245 | +7987827.44 | 1.93 |
| ${}^{137}$Ba | 137 | 81 | 137.7339 | -880198104.87 | 128538.9183 | +7935164.38 | 1.94 |
| ${}^{138}$Ba | 138 | 82 | 143.8962 | -875768627.42 | 129472.3214 | +7896724.74 | 1.94 |
| ${}^{139}$Ba | 139 | 83 | 150.0494 | -870982502.04 | 130405.7337 | +7828622.82 | 1.95 |
| ${}^{140}$Ba | 140 | 84 | 156.1935 | -866437494.20 | 131339.1550 | +7774727.24 | 60.61 |
| ${}^{141}$Ba | 141 | 85 | 162.3287 | -861727545.59 | 132272.5852 | +7707160.35 | 40.51 |
| ${}^{142}$Ba | 142 | 86 | 168.4551 | -857260540.19 | 133206.0242 | +7653155.73 | 44.78 |
| ${}^{143}$Ba | 143 | 87 | 174.5729 | -852597001.38 | 134139.4718 | +7584723.83 | 50.75 |
| ${}^{144}$Ba | 144 | 88 | 180.6823 | -848194900.70 | 135072.9279 | +7530348.83 | 53.23 |
| ${}^{145}$Ba | 145 | 89 | 186.7833 | -843571075.14 | 136006.3923 | +7461258.57 | 62.79 |
| ${}^{146}$Ba | 146 | 90 | 192.8761 | -839198524.10 | 136939.8649 | +7405045.09 | 13.02 |
| ${}^{147}$Ba | 147 | 91 | 198.9608 | -834604034.67 | 137873.3456 | +7335289.09 | 144.28 |
| ${}^{148}$Ba | 148 | 92 | 205.0376 | -830307446.47 | 138806.8343 | +7280303.01 | 10.82 |
| ${}^{149}$Ba | 149 | 93 | 211.1065 | -825768786.65 | 139740.3308 | +7211629.39 | 18.13 |
| ${}^{150}$Ba | 150 | 94 | 217.1677 | -821522075.48 | 140673.8350 | +7156719.55 | 40.68 |
| ${}^{151}$Ba | 151 | 95 | 223.2213 | -817021109.70 | 141607.3469 | +7088204.12 | 2841.97 |
| ${}^{152}$Ba | 152 | 96 | 229.2674 | -812791629.77 | 142540.8662 | +7032172.00 | 2823.20 |
| ${}^{153}$Ba | 153 | 97 | 235.3061 | -808307593.78 | 143474.3929 | +6964135.70 | 2804.64 |
| ${}^{154}$Ba | 154 | 98 | 241.3375 | -804133637.62 | 144407.9269 | +6908202.17 | 3487.81 |

### Lanthanum (Z = 57)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{116}$La | 116 | 59 | -12.9002 | -1013845710.65 | 108957.8962 | +8745497.51 | 2975.24 |
| ${}^{117}$La | 117 | 60 | -6.4582 | -1006826453.08 | 109891.0197 | +8743283.71 | 1838.39 |
| ${}^{118}$La | 118 | 61 | -0.0301 | -1000031480.74 | 110824.1570 | +8714857.40 | 2730.05 |
| ${}^{119}$La | 119 | 62 | 6.3844 | -993424418.97 | 111757.3079 | +8705704.28 | 2707.23 |
| ${}^{120}$La | 120 | 63 | 12.7855 | -986973200.90 | 112690.4721 | +8671095.68 | 2684.72 |
| ${}^{121}$La | 121 | 64 | 19.1736 | -980715621.23 | 113623.6495 | +8655706.51 | 2662.63 |
| ${}^{122}$La | 122 | 65 | 25.5489 | -974569887.50 | 114556.8396 | +8620546.96 | 2624.44 |
| ${}^{123}$La | 123 | 66 | 31.9115 | -968617012.97 | 115490.0424 | +8601525.93 | 1708.34 |
| ${}^{124}$La | 124 | 67 | 38.2618 | -962726291.73 | 116423.2576 | +8561071.27 | 490.91 |
| ${}^{125}$La | 125 | 68 | 44.5999 | -957036198.56 | 117356.4849 | +8537777.48 | 223.41 |
| ${}^{126}$La | 126 | 69 | 50.9261 | -951376999.39 | 118289.7241 | +8495290.76 | 771.63 |
| ${}^{127}$La | 127 | 70 | 57.2405 | -945915804.90 | 119222.9751 | +8468146.95 | 219.92 |
| ${}^{128}$La | 128 | 71 | 63.5435 | -940455534.30 | 120156.2376 | +8422959.77 | 456.96 |
| ${}^{129}$La | 129 | 72 | 69.8351 | -935213638.21 | 121089.5113 | +8395099.95 | 177.74 |
| ${}^{130}$La | 130 | 73 | 76.1157 | -929931555.03 | 122022.7962 | +8347808.75 | 214.41 |
| ${}^{131}$La | 131 | 74 | 82.3853 | -924866420.60 | 122956.0920 | +8316527.63 | 229.16 |
| ${}^{132}$La | 132 | 75 | 88.6442 | -919745829.89 | 123889.3985 | +8267855.99 | 295.90 |
| ${}^{133}$La | 133 | 76 | 94.8926 | -914847619.95 | 124822.7156 | +8234795.02 | 225.72 |
| ${}^{134}$La | 134 | 77 | 101.1306 | -909880335.54 | 125756.0430 | +8185768.25 | 159.77 |
| ${}^{135}$La | 135 | 78 | 107.3584 | -905133372.22 | 126689.3806 | +8151191.94 | 75.06 |
| ${}^{136}$La | 136 | 79 | 113.5762 | -900296761.36 | 127622.7282 | +8101031.42 | 420.00 |
| ${}^{137}$La | 137 | 80 | 119.7842 | -895687229.83 | 128556.0857 | +8065193.03 | 12.86 |
| ${}^{138}$La | 138 | 81 | 125.9825 | -890996144.99 | 129489.4528 | +8016367.25 | 3.23 |
| ${}^{139}$La | 139 | 82 | 132.1712 | -886503690.42 | 130422.8295 | +7978729.54 | 4.69 |
| ${}^{140}$La | 140 | 83 | 138.3506 | -881721612.25 | 131356.2156 | +7913709.51 | 4.65 |
| ${}^{141}$La | 141 | 84 | 144.5207 | -877149183.98 | 132289.6108 | +7861418.87 | 31.44 |
| ${}^{142}$La | 142 | 85 | 150.6818 | -872471889.40 | 133223.0152 | +7798318.64 | 47.55 |
| ${}^{143}$La | 143 | 86 | 156.8339 | -867960043.46 | 134156.4285 | +7744145.41 | 55.05 |
| ${}^{144}$La | 144 | 87 | 162.9773 | -863334374.54 | 135089.8506 | +7679747.59 | 96.50 |
| ${}^{145}$La | 145 | 88 | 169.1120 | -858906709.83 | 136023.2813 | +7626064.92 | 90.88 |
| ${}^{146}$La | 146 | 89 | 175.2382 | -854337190.87 | 136956.7205 | +7561323.59 | 12.31 |
| ${}^{147}$La | 147 | 90 | 181.3560 | -849941491.77 | 137890.1681 | +7505414.96 | 78.27 |
| ${}^{148}$La | 148 | 91 | 187.4655 | -845410938.95 | 138823.6240 | +7439892.18 | 141.28 |
| ${}^{149}$La | 149 | 92 | 193.5670 | -841110979.30 | 139757.0880 | +7386064.36 | 1443.51 |
| ${}^{150}$La | 150 | 93 | 199.6604 | -836667282.04 | 140690.5600 | +7322772.56 | 18.01 |
| ${}^{151}$La | 151 | 94 | 205.7459 | -832384244.87 | 141624.0399 | +7266883.52 | 3097.20 |
| ${}^{152}$La | 152 | 95 | 211.8237 | -827995926.54 | 142557.5275 | +7204532.23 | 2119.16 |
| ${}^{153}$La | 153 | 96 | 217.8938 | -823766521.98 | 143491.0228 | +7148637.32 | 2105.26 |
| ${}^{154}$La | 154 | 97 | 223.9564 | -819368700.91 | 144424.5256 | +7084398.25 | 2091.51 |
| ${}^{155}$La | 155 | 98 | 230.0116 | -815153723.40 | 145358.0359 | +7027535.86 | 2768.47 |
| ${}^{156}$La | 156 | 99 | 236.0595 | -810778818.81 | 146291.5534 | +6962578.24 | 2750.63 |
| ${}^{157}$La | 157 | 100 | 242.1001 | -806568105.02 | 147225.0782 | +6904698.44 | 2051.36 |

### Cerium (Z = 58)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{119}$Ce | 119 | 61 | -12.5645 | -1013102977.71 | 111775.4744 | +8767702.55 | 4514.39 |
| ${}^{120}$Ce | 120 | 62 | -6.1194 | -1006289493.68 | 112708.5948 | +8762515.20 | 4476.99 |
| ${}^{121}$Ce | 121 | 63 | 0.3121 | -999682854.56 | 113641.7287 | +8731126.67 | 3555.38 |
| ${}^{122}$Ce | 122 | 64 | 6.7302 | -993251046.63 | 114574.8759 | +8720114.31 | 3526.39 |
| ${}^{123}$Ce | 123 | 65 | 13.1354 | -986965504.54 | 115508.0362 | +8684983.67 | 2603.00 |
| ${}^{124}$Ce | 124 | 66 | 19.5277 | -980862651.06 | 116441.2094 | +8669900.00 | 2582.10 |
| ${}^{125}$Ce | 125 | 67 | 25.9074 | -974853294.54 | 117374.3951 | +8630135.80 | 1680.96 |
| ${}^{126}$Ce | 126 | 68 | 32.2748 | -969038940.13 | 118307.5931 | +8611924.07 | 238.24 |
| ${}^{127}$Ce | 127 | 69 | 38.6300 | -963267638.99 | 119240.8033 | +8568473.17 | 244.24 |
| ${}^{128}$Ce | 128 | 70 | 44.9733 | -957703517.58 | 120174.0254 | +8546078.72 | 234.52 |
| ${}^{129}$Ce | 129 | 71 | 51.3049 | -952145951.64 | 121107.2593 | +8500604.19 | 232.71 |
| ${}^{130}$Ce | 130 | 72 | 57.6250 | -946806985.84 | 122040.5046 | +8475772.78 | 230.92 |
| ${}^{131}$Ce | 131 | 73 | 63.9337 | -941435191.47 | 122973.7613 | +8427844.71 | 268.98 |
| ${}^{132}$Ce | 132 | 74 | 70.2314 | -936298421.85 | 123907.0290 | +8401042.33 | 166.07 |
| ${}^{133}$Ce | 133 | 75 | 76.5182 | -931097462.26 | 124840.3077 | +8351837.72 | 132.10 |
| ${}^{134}$Ce | 134 | 76 | 82.7942 | -926143459.32 | 125773.5971 | +8323381.14 | 163.44 |
| ${}^{135}$Ce | 135 | 77 | 89.0596 | -921107141.55 | 126706.8970 | +8274317.25 | 81.69 |
| ${}^{136}$Ce | 136 | 78 | 95.3147 | -916304824.11 | 127640.2074 | +8242852.41 | 2.56 |
| ${}^{137}$Ce | 137 | 79 | 101.5596 | -911403271.92 | 128573.5279 | +8192304.00 | 2.82 |
| ${}^{138}$Ce | 138 | 80 | 107.7944 | -906754760.95 | 129506.8585 | +8160122.31 | 3.89 |
| ${}^{139}$Ce | 139 | 81 | 114.0194 | -902002640.53 | 130440.1989 | +8110908.20 | 16.14 |
| ${}^{140}$Ce | 140 | 82 | 120.2347 | -897470395.35 | 131373.5491 | +8075812.82 | 10.07 |
| ${}^{141}$Ce | 141 | 83 | 126.4404 | -892675289.06 | 132306.9088 | +8012413.60 | 10.01 |
| ${}^{142}$Ce | 142 | 84 | 132.6367 | -888097098.65 | 133240.2779 | +7963287.45 | 18.48 |
| ${}^{143}$Ce | 143 | 85 | 138.8238 | -883383380.67 | 134173.6563 | +7899561.56 | 18.34 |
| ${}^{144}$Ce | 144 | 86 | 145.0017 | -878895319.80 | 135107.0437 | +7849964.27 | 21.13 |
| ${}^{145}$Ce | 145 | 87 | 151.1707 | -874237349.99 | 136040.4402 | +7784765.36 | 251.13 |
| ${}^{146}$Ce | 146 | 88 | 157.3309 | -869830529.36 | 136973.8454 | +7734790.31 | 107.89 |
| ${}^{147}$Ce | 147 | 89 | 163.4824 | -865238221.87 | 137907.2593 | +7669576.59 | 62.69 |
| ${}^{148}$Ce | 148 | 90 | 169.6254 | -860914635.07 | 138840.6818 | +7619909.52 | 81.24 |
| ${}^{149}$Ce | 149 | 91 | 175.7599 | -856395951.14 | 139774.1127 | +7555624.30 | 73.86 |
| ${}^{150}$Ce | 150 | 92 | 181.8861 | -852145343.18 | 140707.5519 | +7506005.16 | 83.75 |
| ${}^{151}$Ce | 151 | 93 | 188.0042 | -847722764.79 | 141640.9992 | +7444213.60 | 125.88 |
| ${}^{152}$Ce | 152 | 94 | 194.1142 | -843515819.92 | 142574.4546 | +7393097.39 | 1415.06 |
| ${}^{153}$Ce | 153 | 95 | 200.2164 | -839119297.74 | 143507.9179 | +7329796.05 | 1405.77 |
| ${}^{154}$Ce | 154 | 96 | 206.3107 | -834933510.32 | 144441.3890 | +7277071.95 | 1396.61 |
| ${}^{155}$Ce | 155 | 97 | 212.3973 | -830554589.14 | 145374.8679 | +7212875.93 | 2078.11 |
| ${}^{156}$Ce | 156 | 98 | 218.4763 | -826414323.11 | 146308.3542 | +7159814.69 | 2064.74 |
| ${}^{157}$Ce | 157 | 99 | 224.5479 | -822042879.98 | 147241.8481 | +7094194.34 | 2733.23 |
| ${}^{158}$Ce | 158 | 100 | 230.6121 | -817895156.31 | 148175.3493 | +7039716.87 | 2715.86 |
| ${}^{159}$Ce | 159 | 101 | 236.6691 | -813543187.22 | 149108.8578 | +6973674.52 | 3378.07 |

### Praseodymium (Z = 59)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{121}$Pr | 121 | 62 | -18.8356 | -1019378335.30 | 113660.0940 | +8794402.80 | 4439.65 |
| ${}^{122}$Pr | 122 | 63 | -12.3737 | -1012583621.13 | 114593.1976 | +8765128.01 | 4403.37 |
| ${}^{123}$Pr | 123 | 64 | -5.9254 | -1005944436.17 | 115526.3146 | +8756014.05 | 3489.33 |
| ${}^{124}$Pr | 124 | 65 | 0.5097 | -999494259.62 | 116459.4450 | +8725064.41 | 3469.34 |
| ${}^{125}$Pr | 125 | 66 | 6.9318 | -993209962.77 | 117392.5883 | +8712038.46 | 2577.29 |
| ${}^{126}$Pr | 126 | 67 | 13.3410 | -987062403.97 | 118325.7445 | +8676403.69 | 1667.52 |
| ${}^{127}$Pr | 127 | 68 | 19.7377 | -981083827.95 | 119258.9132 | +8658210.15 | 1654.45 |
| ${}^{128}$Pr | 128 | 69 | 26.1221 | -975199782.14 | 120192.0943 | +8619817.19 | 250.14 |
| ${}^{129}$Pr | 129 | 70 | 32.4943 | -969483598.96 | 121125.2875 | +8596021.10 | 248.21 |
| ${}^{130}$Pr | 130 | 71 | 38.8546 | -963832201.44 | 122058.4926 | +8555680.08 | 531.08 |
| ${}^{131}$Pr | 131 | 72 | 45.2033 | -958356619.31 | 122991.7094 | +8530301.76 | 385.36 |
| ${}^{132}$Pr | 132 | 73 | 51.5404 | -952908933.53 | 123924.9377 | +8487358.01 | 234.99 |
| ${}^{133}$Pr | 133 | 74 | 57.8662 | -947644947.62 | 124858.1773 | +8459676.41 | 100.94 |
| ${}^{134}$Pr | 134 | 75 | 64.1809 | -942383191.79 | 125791.4281 | +8415359.95 | 162.86 |
| ${}^{135}$Pr | 135 | 76 | 70.4846 | -937313854.85 | 126724.6897 | +8386370.15 | 94.03 |
| ${}^{136}$Pr | 136 | 77 | 76.7777 | -932227969.46 | 127657.9621 | +8341934.65 | 90.47 |
| ${}^{137}$Pr | 137 | 78 | 83.0601 | -927319645.85 | 128591.2451 | +8309749.00 | 63.79 |
| ${}^{138}$Pr | 138 | 79 | 89.3322 | -922374664.24 | 129524.5384 | +8262927.86 | 77.93 |
| ${}^{139}$Pr | 139 | 80 | 95.5940 | -917632767.60 | 130457.8420 | +8230672.83 | 28.20 |
| ${}^{140}$Pr | 140 | 81 | 101.8458 | -912841446.14 | 131391.1556 | +8184703.72 | 47.12 |
| ${}^{141}$Pr | 141 | 82 | 108.0877 | -908237833.27 | 132324.4791 | +8150758.91 | 11.40 |
| ${}^{142}$Pr | 142 | 83 | 114.3199 | -903426028.52 | 133257.8124 | +8090242.46 | 11.32 |
| ${}^{143}$Pr | 143 | 84 | 120.5425 | -898798003.45 | 134191.1552 | +8042081.07 | 13.64 |
| ${}^{144}$Pr | 144 | 85 | 126.7557 | -894093292.14 | 135124.5074 | +7982633.12 | 20.20 |
| ${}^{145}$Pr | 145 | 86 | 132.9596 | -889550877.82 | 136057.8690 | +7932984.41 | 52.96 |
| ${}^{146}$Pr | 146 | 87 | 139.1544 | -884894352.53 | 136991.2396 | +7870529.92 | 252.76 |
| ${}^{147}$Pr | 147 | 88 | 145.3402 | -880454171.56 | 137924.6193 | +7821683.16 | 115.85 |
| ${}^{148}$Pr | 148 | 89 | 151.5171 | -875900474.97 | 138858.0078 | +7761280.09 | 109.16 |
| ${}^{149}$Pr | 149 | 90 | 157.6853 | -871540231.59 | 139791.4050 | +7712014.69 | 71.18 |
| ${}^{150}$Pr | 150 | 91 | 163.8449 | -867099566.76 | 140724.8108 | +7654501.90 | 64.54 |
| ${}^{151}$Pr | 151 | 92 | 169.9961 | -862838910.92 | 141658.2250 | +7606543.24 | 82.86 |
| ${}^{152}$Pr | 152 | 93 | 176.1390 | -858459244.82 | 142591.6476 | +7548591.09 | 130.98 |
| ${}^{153}$Pr | 153 | 94 | 182.2736 | -854218617.78 | 143525.0783 | +7497341.18 | 83.40 |
| ${}^{154}$Pr | 154 | 95 | 188.4002 | -849842527.06 | 144458.5172 | +7436140.68 | 697.42 |
| ${}^{155}$Pr | 155 | 96 | 194.5188 | -845658110.77 | 145391.9640 | +7384615.32 | 119.16 |
| ${}^{156}$Pr | 156 | 97 | 200.6296 | -841326349.92 | 146325.4186 | +7323253.69 | 7.05 |
| ${}^{157}$Pr | 157 | 98 | 206.7326 | -837150874.29 | 147258.8810 | +7269286.03 | 21.66 |
| ${}^{158}$Pr | 158 | 99 | 212.8280 | -832856079.54 | 148192.3510 | +7207359.81 | 2038.59 |
| ${}^{159}$Pr | 159 | 100 | 218.9159 | -828688587.85 | 149125.8285 | +7152418.66 | 2698.86 |
| ${}^{160}$Pr | 160 | 101 | 224.9964 | -824419052.13 | 150059.3135 | +7090176.76 | 2681.90 |
| ${}^{161}$Pr | 161 | 102 | 231.0697 | -820283584.98 | 150992.8057 | +7034535.13 | 3336.13 |

### Neodymium (Z = 60)

_40 of 40 isotopes with a framework prediction; 40 of 40 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{124}$Nd | 124 | 64 | -18.7921 | -1018816624.84 | 116477.9644 | +8812764.04 | 4332.33 |
| ${}^{125}$Nd | 125 | 65 | -12.3270 | -1012204909.65 | 117411.0647 | +8784113.83 | 3433.42 |
| ${}^{126}$Nd | 126 | 66 | -5.8751 | -1005740892.24 | 118344.1783 | +8773835.28 | 2556.72 |
| ${}^{127}$Nd | 127 | 67 | 0.5638 | -999454737.00 | 119277.3048 | +8740106.59 | 2536.63 |
| ${}^{128}$Nd | 128 | 68 | 6.9899 | -993321646.20 | 120210.4441 | +8724703.77 | 1680.54 |
| ${}^{129}$Nd | 129 | 69 | 13.4035 | -987314955.39 | 121143.5960 | +8686329.07 | 1683.04 |
| ${}^{130}$Nd | 130 | 70 | 19.8048 | -981472293.35 | 122076.7601 | +8668457.18 | 230.90 |
| ${}^{131}$Nd | 131 | 71 | 26.1939 | -975705220.65 | 123009.9364 | +8625733.62 | 225.63 |
| ${}^{132}$Nd | 132 | 72 | 32.5711 | -970115454.14 | 123943.1246 | +8604157.40 | 196.97 |
| ${}^{133}$Nd | 133 | 73 | 38.9367 | -964566844.75 | 124876.3245 | +8560588.24 | 376.16 |
| ${}^{134}$Nd | 134 | 74 | 45.2907 | -959207192.56 | 125809.5359 | +8537225.10 | 94.73 |
| ${}^{135}$Nd | 135 | 75 | 51.6334 | -953853414.56 | 126742.7586 | +8492253.95 | 152.20 |
| ${}^{136}$Nd | 136 | 76 | 57.9651 | -948701560.81 | 127675.9924 | +8467296.19 | 93.34 |
| ${}^{137}$Nd | 137 | 77 | 64.2858 | -943530409.44 | 128609.2371 | +8422220.94 | 91.93 |
| ${}^{138}$Nd | 138 | 78 | 70.5957 | -938554639.99 | 129542.4926 | +8393962.76 | 90.32 |
| ${}^{139}$Nd | 139 | 79 | 76.8951 | -933538659.51 | 130475.7586 | +8347228.37 | 212.69 |
| ${}^{140}$Nd | 140 | 80 | 83.1840 | -928738150.17 | 131409.0351 | +8318576.73 | 25.02 |
| ${}^{141}$Nd | 141 | 81 | 89.4628 | -923881341.85 | 132342.3218 | +8272694.11 | 24.25 |
| ${}^{142}$Nd | 142 | 82 | 95.7314 | -919223289.87 | 133275.6185 | +8241448.60 | 9.50 |
| ${}^{143}$Nd | 143 | 83 | 101.9902 | -914384620.71 | 134208.9252 | +8182643.66 | 9.43 |
| ${}^{144}$Nd | 144 | 84 | 108.2392 | -909731254.58 | 135142.2416 | +8137465.98 | 9.35 |
| ${}^{145}$Nd | 145 | 85 | 114.4786 | -904983803.08 | 136075.5677 | +8077585.65 | 9.41 |
| ${}^{146}$Nd | 146 | 86 | 120.7085 | -900438149.91 | 137008.9031 | +8032020.87 | 9.36 |
| ${}^{147}$Nd | 147 | 87 | 126.9292 | -895762281.91 | 137942.2479 | +7970402.52 | 9.31 |
| ${}^{148}$Nd | 148 | 88 | 133.1407 | -891315695.43 | 138875.6018 | +7924612.06 | 14.89 |
| ${}^{149}$Nd | 149 | 89 | 139.3432 | -886718489.52 | 139808.9647 | +7862836.08 | 14.81 |
| ${}^{150}$Nd | 150 | 90 | 145.5368 | -882388515.63 | 140742.3366 | +7818815.30 | 8.08 |
| ${}^{151}$Nd | 151 | 91 | 151.7216 | -877916694.21 | 141675.7171 | +7760808.38 | 8.05 |
| ${}^{152}$Nd | 152 | 92 | 157.8979 | -873686664.90 | 142609.1063 | +7717465.52 | 172.95 |
| ${}^{153}$Nd | 153 | 93 | 164.0656 | -869301778.63 | 143542.5040 | +7660419.68 | 19.28 |
| ${}^{154}$Nd | 154 | 94 | 170.2250 | -865074430.76 | 144475.9100 | +7611684.28 | 7.15 |
| ${}^{155}$Nd | 155 | 95 | 176.3762 | -860726015.97 | 145409.3243 | +7552849.65 | 63.42 |
| ${}^{156}$Nd | 156 | 96 | 182.5192 | -856553669.08 | 146342.7467 | +7503249.61 | 8.98 |
| ${}^{157}$Nd | 157 | 97 | 188.6543 | -852238693.76 | 147276.1770 | +7443129.84 | 14.62 |
| ${}^{158}$Nd | 158 | 98 | 194.7814 | -848083658.38 | 148209.6153 | +7391010.87 | 8.86 |
| ${}^{159}$Nd | 159 | 99 | 200.9008 | -843793419.42 | 149143.0613 | +7329722.25 | 201.33 |
| ${}^{160}$Nd | 160 | 100 | 207.0126 | -839673605.02 | 150076.5150 | +7276769.95 | 312.60 |
| ${}^{161}$Nd | 161 | 101 | 213.1168 | -835400822.71 | 151009.9762 | +7214485.94 | 2665.35 |
| ${}^{162}$Nd | 162 | 102 | 219.2135 | -831317655.16 | 151943.4449 | +7161530.08 | 2648.83 |
| ${}^{163}$Nd | 163 | 103 | 225.3029 | -827048745.88 | 152876.9209 | +7097928.30 | 3295.22 |

### Promethium (Z = 61)

_40 of 40 isotopes with a framework prediction; 40 of 40 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{126}$Pm | 126 | 65 | -25.3736 | -1025147052.79 | 118362.8944 | +8816161.14 | 4263.35 |
| ${}^{127}$Pm | 127 | 66 | -18.8918 | -1018474188.56 | 119295.9781 | +8807590.00 | 3379.25 |
| ${}^{128}$Pm | 128 | 67 | -12.4232 | -1012019336.81 | 120229.0749 | +8776831.65 | 2516.64 |
| ${}^{129}$Pm | 129 | 68 | -5.9676 | -1005701282.45 | 121162.1847 | +8763875.75 | 2497.23 |
| ${}^{130}$Pm | 130 | 69 | 0.4753 | -999550336.22 | 122095.3073 | +8728966.47 | 1654.60 |
| ${}^{131}$Pm | 131 | 70 | 6.9057 | -993542208.17 | 123028.4423 | +8711324.14 | 1642.03 |
| ${}^{132}$Pm | 132 | 71 | 13.3237 | -987655969.19 | 123961.5897 | +8673994.15 | 1212.73 |
| ${}^{133}$Pm | 133 | 72 | 19.7296 | -981918809.11 | 124894.7492 | +8652983.47 | 406.23 |
| ${}^{134}$Pm | 134 | 73 | 26.1237 | -976264067.16 | 125827.9205 | +8612784.60 | 336.00 |
| ${}^{135}$Pm | 135 | 74 | 32.5061 | -970767057.28 | 126761.1036 | +8588859.26 | 659.63 |
| ${}^{136}$Pm | 136 | 75 | 38.8769 | -965323926.52 | 127694.2982 | +8547923.84 | 545.54 |
| ${}^{137}$Pm | 137 | 76 | 45.2365 | -960042664.21 | 128627.5040 | +8521870.65 | 102.25 |
| ${}^{138}$Pm | 138 | 77 | 51.5850 | -954791003.36 | 129560.7210 | +8480098.50 | 90.31 |
| ${}^{139}$Pm | 139 | 78 | 57.9225 | -949706582.97 | 130493.9489 | +8452611.92 | 105.01 |
| ${}^{140}$Pm | 140 | 79 | 64.2492 | -944635317.88 | 131427.1875 | +8411087.08 | 185.83 |
| ${}^{141}$Pm | 141 | 80 | 70.5654 | -939731747.35 | 132360.4368 | +8382522.30 | 106.45 |
| ${}^{142}$Pm | 142 | 81 | 76.8712 | -934829824.07 | 133293.6964 | +8341529.13 | 178.49 |
| ${}^{143}$Pm | 143 | 82 | 83.1667 | -930078865.76 | 134226.9663 | +8310279.39 | 22.11 |
| ${}^{144}$Pm | 144 | 83 | 89.4522 | -925204901.78 | 135160.2463 | +8254238.58 | 21.72 |
| ${}^{145}$Pm | 145 | 84 | 95.7277 | -920484406.87 | 136093.5362 | +8209472.20 | 20.78 |
| ${}^{146}$Pm | 146 | 85 | 101.9934 | -915717929.69 | 137026.8359 | +8153044.85 | 31.45 |
| ${}^{147}$Pm | 147 | 86 | 108.2495 | -911110766.12 | 137960.1452 | +8107776.07 | 9.41 |
| ${}^{148}$Pm | 148 | 87 | 114.4962 | -906434255.90 | 138893.4640 | +8050284.50 | 41.29 |
| ${}^{149}$Pm | 149 | 88 | 120.7335 | -901919819.95 | 139826.7921 | +8003622.94 | 15.74 |
| ${}^{150}$Pm | 150 | 89 | 126.9617 | -897327701.83 | 140760.1293 | +7945628.37 | 143.44 |
| ${}^{151}$Pm | 151 | 90 | 133.1808 | -892978668.47 | 141693.4757 | +7904642.77 | 32.79 |
| ${}^{152}$Pm | 152 | 91 | 139.3910 | -888520361.32 | 142626.8309 | +7850580.64 | 183.05 |
| ${}^{153}$Pm | 153 | 92 | 145.5924 | -884251726.64 | 143560.1949 | +7808080.20 | 63.62 |
| ${}^{154}$Pm | 154 | 93 | 151.7852 | -879871778.63 | 144493.5675 | +7753717.42 | 174.51 |
| ${}^{155}$Pm | 155 | 94 | 157.9694 | -875641163.16 | 145426.9487 | +7707482.57 | 32.69 |
| ${}^{156}$Pm | 156 | 95 | 164.1453 | -871316039.51 | 146360.3382 | +7651863.87 | 8.18 |
| ${}^{157}$Pm | 157 | 96 | 170.3129 | -867126872.46 | 147293.7361 | +7603239.76 | 47.92 |
| ${}^{158}$Pm | 158 | 97 | 176.4724 | -862843675.54 | 148227.1420 | +7546239.30 | 6.03 |
| ${}^{159}$Pm | 159 | 98 | 182.6238 | -858669015.12 | 149160.5561 | +7494362.46 | 67.81 |
| ${}^{160}$Pm | 160 | 99 | 188.7673 | -854411672.26 | 150093.9780 | +7435697.49 | 13.75 |
| ${}^{161}$Pm | 161 | 100 | 194.9029 | -850287207.09 | 151027.4077 | +7383539.13 | 60.27 |
| ${}^{162}$Pm | 162 | 101 | 201.0309 | -846057350.53 | 151960.8452 | +7323807.77 | 1988.26 |
| ${}^{163}$Pm | 163 | 102 | 207.1513 | -841971264.27 | 152894.2902 | +7271273.70 | 2632.65 |
| ${}^{164}$Pm | 164 | 103 | 213.2643 | -837734989.41 | 153827.7427 | +7209412.13 | 2616.51 |
| ${}^{165}$Pm | 165 | 104 | 219.3698 | -833644406.99 | 154761.2026 | +7154317.17 | 3255.28 |

### Samarium (Z = 62)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{128}$Sm | 128 | 66 | -32.1173 | -1031372376.71 | 120247.9867 | +8858734.71 | 4196.69 |
| ${}^{129}$Sm | 129 | 67 | -25.6189 | -1024753362.06 | 121181.0537 | +8829841.90 | 4164.26 |
| ${}^{130}$Sm | 130 | 68 | -19.1337 | -1018249526.41 | 122114.1339 | +8819752.03 | 3301.30 |
| ${}^{131}$Sm | 131 | 69 | -12.6615 | -1011954531.43 | 123047.2271 | +8786847.99 | 3276.16 |
| ${}^{132}$Sm | 132 | 70 | -6.2019 | -1005784820.77 | 123980.3330 | +8773253.38 | 2440.49 |
| ${}^{133}$Sm | 133 | 71 | 0.2451 | -999773519.97 | 124913.4514 | +8737411.16 | 2407.13 |
| ${}^{134}$Sm | 134 | 72 | 6.6798 | -993896219.81 | 125846.5821 | +8718808.05 | 1567.94 |
| ${}^{135}$Sm | 135 | 73 | 13.1025 | -988131572.88 | 126779.7248 | +8679195.39 | 1230.24 |
| ${}^{136}$Sm | 136 | 74 | 19.5133 | -982515053.46 | 127712.8795 | +8659955.48 | 98.70 |
| ${}^{137}$Sm | 137 | 75 | 25.9124 | -976972028.92 | 128646.0458 | +8619158.70 | 224.34 |
| ${}^{138}$Sm | 138 | 76 | 32.3000 | -971587774.66 | 129579.2236 | +8597297.21 | 91.98 |
| ${}^{139}$Sm | 139 | 77 | 38.6763 | -966244803.77 | 130512.4127 | +8555387.97 | 84.10 |
| ${}^{140}$Sm | 140 | 78 | 45.0415 | -961068262.26 | 131445.6130 | +8531133.80 | 95.88 |
| ${}^{141}$Sm | 141 | 79 | 51.3957 | -955901813.31 | 132378.8241 | +8487347.90 | 65.02 |
| ${}^{142}$Sm | 142 | 80 | 57.7392 | -950927194.84 | 133312.0461 | +8463865.21 | 14.11 |
| ${}^{143}$Sm | 143 | 81 | 64.0721 | -945940265.17 | 134245.2786 | +8421754.96 | 20.65 |
| ${}^{144}$Sm | 144 | 82 | 70.3946 | -941128321.35 | 135178.5215 | +8394699.51 | 10.88 |
| ${}^{145}$Sm | 145 | 83 | 76.7069 | -936209827.45 | 136111.7747 | +8339984.41 | 11.00 |
| ${}^{146}$Sm | 146 | 84 | 83.0090 | -931448708.62 | 137045.0380 | +8298403.00 | 22.40 |
| ${}^{147}$Sm | 147 | 85 | 89.3012 | -926636605.52 | 137978.3112 | +8242170.38 | 9.22 |
| ${}^{148}$Sm | 148 | 86 | 95.5836 | -921997146.57 | 138911.5943 | +8199944.04 | 9.04 |
| ${}^{149}$Sm | 149 | 87 | 101.8563 | -917274493.46 | 139844.8869 | +8141854.96 | 8.33 |
| ${}^{150}$Sm | 150 | 88 | 108.1196 | -912753536.15 | 140778.1891 | +8099882.74 | 7.96 |
| ${}^{151}$Sm | 151 | 89 | 114.3735 | -908121892.31 | 141711.5006 | +8041393.32 | 7.89 |
| ${}^{152}$Sm | 152 | 90 | 120.6183 | -903743933.92 | 142644.8213 | +8002697.64 | 7.17 |
| ${}^{153}$Sm | 153 | 91 | 126.8539 | -899239616.67 | 143578.1510 | +7947663.84 | 7.19 |
| ${}^{154}$Sm | 154 | 92 | 133.0806 | -894958429.66 | 144511.4897 | +7908160.28 | 9.10 |
| ${}^{155}$Sm | 155 | 93 | 139.2986 | -890552232.97 | 145444.8372 | +7854143.30 | 9.22 |
| ${}^{156}$Sm | 156 | 94 | 145.5078 | -886320335.92 | 146378.1934 | +7810829.87 | 58.67 |
| ${}^{157}$Sm | 157 | 95 | 151.7085 | -881972821.51 | 147311.5582 | +7755355.31 | 30.33 |
| ${}^{158}$Sm | 158 | 96 | 157.9008 | -877787172.80 | 148244.9313 | +7709254.82 | 32.50 |
| ${}^{159}$Sm | 159 | 97 | 164.0847 | -873493122.97 | 149178.3128 | +7652777.26 | 40.08 |
| ${}^{160}$Sm | 160 | 98 | 170.2605 | -869345815.63 | 150111.7024 | +7604295.42 | 13.13 |
| ${}^{161}$Sm | 161 | 99 | 176.4282 | -865079808.32 | 151045.1001 | +7545808.77 | 45.47 |
| ${}^{162}$Sm | 162 | 100 | 182.5880 | -860983543.86 | 151978.5058 | +7496569.64 | 23.35 |
| ${}^{163}$Sm | 163 | 101 | 188.7399 | -856767716.84 | 152911.9193 | +7438121.81 | 48.48 |
| ${}^{164}$Sm | 164 | 102 | 194.8841 | -852708243.07 | 153845.3405 | +7387730.47 | 26.84 |
| ${}^{165}$Sm | 165 | 103 | 201.0206 | -848488140.60 | 154778.7694 | +7326588.11 | 2600.74 |
| ${}^{166}$Sm | 166 | 104 | 207.1497 | -844460979.50 | 155712.2058 | +7275065.43 | 2585.01 |
| ${}^{167}$Sm | 167 | 105 | 213.2713 | -840206011.47 | 156645.6496 | +7210865.43 | 3216.30 |
| ${}^{168}$Sm | 168 | 106 | 219.3856 | -836172805.57 | 157579.1007 | +7156690.90 | 1917.05 |

### Europium (Z = 63)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{130}$Eu | 130 | 67 | -39.0223 | -1037757436.52 | 122133.2402 | +8859355.98 | 4447.38 |
| ${}^{131}$Eu | 131 | 68 | -32.5075 | -1031034091.04 | 123066.2908 | +8853676.13 | 3275.87 |
| ${}^{132}$Eu | 132 | 69 | -26.0058 | -1024571381.09 | 123999.3545 | +8821812.05 | 3251.12 |
| ${}^{133}$Eu | 133 | 70 | -19.5170 | -1018215507.40 | 124932.4311 | +8809256.83 | 2406.93 |
| ${}^{134}$Eu | 134 | 71 | -13.0409 | -1012052005.66 | 125865.5205 | +8777009.17 | 2403.94 |
| ${}^{135}$Eu | 135 | 72 | -6.5773 | -1006009673.35 | 126798.6223 | +8759645.35 | 1556.23 |
| ${}^{136}$Eu | 136 | 73 | -0.1259 | -1000113989.99 | 127731.7363 | +8724697.32 | 1544.80 |
| ${}^{137}$Eu | 137 | 74 | 6.3134 | -994346047.59 | 128664.8625 | +8704638.25 | 34.32 |
| ${}^{138}$Eu | 138 | 75 | 12.7408 | -988687975.82 | 129598.0005 | +8666916.33 | 217.50 |
| ${}^{139}$Eu | 139 | 76 | 19.1565 | -983166856.10 | 130531.1502 | +8645762.22 | 101.61 |
| ${}^{140}$Eu | 140 | 77 | 25.5608 | -977728367.40 | 131464.3114 | +8609052.77 | 395.40 |
| ${}^{141}$Eu | 141 | 78 | 31.9537 | -972422630.22 | 132397.4838 | +8583335.62 | 96.28 |
| ${}^{142}$Eu | 142 | 79 | 38.3356 | -967182620.33 | 133330.6674 | +8546189.92 | 227.36 |
| ${}^{143}$Eu | 143 | 80 | 44.7065 | -962085914.42 | 134263.8619 | +8521380.47 | 82.51 |
| ${}^{144}$Eu | 144 | 81 | 51.0666 | -957036380.89 | 135197.0672 | +8485300.75 | 80.46 |
| ${}^{145}$Eu | 145 | 82 | 57.4161 | -952115092.86 | 136130.2831 | +8457226.16 | 22.67 |
| ${}^{146}$Eu | 146 | 83 | 63.7553 | -947145554.47 | 137063.5094 | +8405527.29 | 44.21 |
| ${}^{147}$Eu | 147 | 84 | 70.0841 | -942305286.09 | 137996.7460 | +8364193.41 | 18.77 |
| ${}^{148}$Eu | 148 | 85 | 76.4028 | -937454936.11 | 138929.9927 | +8311240.02 | 72.29 |
| ${}^{149}$Eu | 149 | 86 | 82.7116 | -932742740.02 | 139863.2493 | +8269180.74 | 28.14 |
| ${}^{150}$Eu | 150 | 87 | 89.0106 | -927996731.17 | 140796.5157 | +8214809.31 | 44.61 |
| ${}^{151}$Eu | 151 | 88 | 95.2999 | -923400612.32 | 141729.7918 | +8172054.83 | 8.29 |
| ${}^{152}$Eu | 152 | 89 | 101.5797 | -918764869.48 | 142663.0775 | +8118351.86 | 8.24 |
| ${}^{153}$Eu | 153 | 90 | 107.8502 | -914336037.00 | 143596.3724 | +8081295.73 | 8.22 |
| ${}^{154}$Eu | 154 | 91 | 114.1114 | -909824263.13 | 144529.6766 | +8029964.13 | 8.28 |
| ${}^{155}$Eu | 155 | 92 | 120.3635 | -905492337.20 | 145462.9899 | +7991296.92 | 8.67 |
| ${}^{156}$Eu | 156 | 93 | 126.6067 | -901082391.41 | 146396.3122 | +7940588.43 | 24.31 |
| ${}^{157}$Eu | 157 | 94 | 132.8410 | -896811947.15 | 147329.6433 | +7898253.67 | 28.96 |
| ${}^{158}$Eu | 158 | 95 | 139.0667 | -892467381.36 | 148262.9831 | +7845792.84 | 13.81 |
| ${}^{159}$Eu | 159 | 96 | 145.2837 | -888251476.60 | 149196.3314 | +7800597.75 | 29.18 |
| ${}^{160}$Eu | 160 | 97 | 151.4923 | -883968752.68 | 150129.6883 | +7747076.75 | 6.07 |
| ${}^{161}$Eu | 161 | 98 | 157.6926 | -879806199.59 | 151063.0534 | +7699979.19 | 69.37 |
| ${}^{162}$Eu | 162 | 99 | 163.8846 | -875561089.42 | 151996.4268 | +7644388.38 | 8.71 |
| ${}^{163}$Eu | 163 | 100 | 170.0686 | -871443655.28 | 152929.8083 | +7595639.95 | 5.95 |
| ${}^{164}$Eu | 164 | 101 | 176.2445 | -867249797.37 | 153863.1977 | +7539671.84 | 13.54 |
| ${}^{165}$Eu | 165 | 102 | 182.4126 | -863177746.47 | 154796.5951 | +7489935.11 | 33.93 |
| ${}^{166}$Eu | 166 | 103 | 188.5729 | -858989380.53 | 155730.0002 | +7431222.65 | 644.77 |
| ${}^{167}$Eu | 167 | 104 | 194.7256 | -854936365.64 | 156663.4129 | +7379751.80 | 2569.59 |
| ${}^{168}$Eu | 168 | 105 | 200.8707 | -850766496.94 | 157596.8333 | +7319024.24 | 2554.21 |
| ${}^{169}$Eu | 169 | 106 | 207.0083 | -846714891.37 | 158530.2611 | +7265015.92 | 3178.23 |
| ${}^{170}$Eu | 170 | 107 | 213.1386 | -842552244.01 | 159463.6962 | +7203994.24 | 3159.44 |

### Gadolinium (Z = 64)

_40 of 40 isotopes with a framework prediction; 40 of 40 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{133}$Gd | 133 | 69 | -39.5566 | -1037335897.57 | 124951.6884 | +8873710.35 | 4038.77 |
| ${}^{134}$Gd | 134 | 70 | -33.0384 | -1030788653.10 | 125884.7357 | +8864138.68 | 3202.56 |
| ${}^{135}$Gd | 135 | 71 | -26.5332 | -1024482096.27 | 126817.7959 | +8832742.49 | 3178.90 |
| ${}^{136}$Gd | 136 | 72 | -20.0406 | -1018273518.03 | 127750.8687 | +8818796.00 | 2353.85 |
| ${}^{137}$Gd | 137 | 73 | -13.5605 | -1012250246.42 | 128683.9541 | +8783669.11 | 2336.70 |
| ${}^{138}$Gd | 138 | 74 | -7.0927 | -1006335825.43 | 129617.0516 | +8767376.87 | 1558.65 |
| ${}^{139}$Gd | 139 | 75 | -0.6369 | -1000563848.12 | 130550.1612 | +8732127.45 | 1511.46 |
| ${}^{140}$Gd | 140 | 76 | 5.8071 | -994913645.26 | 131483.2827 | +8714332.14 | 214.39 |
| ${}^{141}$Gd | 141 | 77 | 12.2394 | -989368264.57 | 132416.4159 | +8676063.60 | 150.52 |
| ${}^{142}$Gd | 142 | 78 | 18.6602 | -983955371.32 | 133349.5605 | +8655916.94 | 211.37 |
| ${}^{143}$Gd | 143 | 79 | 25.0697 | -978616046.04 | 134282.7164 | +8617472.37 | 1504.49 |
| ${}^{144}$Gd | 144 | 80 | 31.4681 | -973421307.06 | 135215.8834 | +8596619.52 | 208.44 |
| ${}^{145}$Gd | 145 | 81 | 37.8555 | -968273863.09 | 136149.0614 | +8558494.07 | 146.04 |
| ${}^{146}$Gd | 146 | 82 | 44.2322 | -963275313.08 | 137082.2501 | +8535750.69 | 29.99 |
| ${}^{147}$Gd | 147 | 83 | 50.5983 | -958244289.73 | 138015.4494 | +8484741.01 | 13.78 |
| ${}^{148}$Gd | 148 | 84 | 56.9540 | -953345243.85 | 138948.6592 | +8446510.46 | 10.59 |
| ${}^{149}$Gd | 149 | 85 | 63.2994 | -948439984.33 | 139881.8792 | +8393930.01 | 23.86 |
| ${}^{150}$Gd | 150 | 86 | 69.6346 | -943679143.10 | 140815.1094 | +8354970.64 | 43.36 |
| ${}^{151}$Gd | 151 | 87 | 75.9599 | -938884325.95 | 141748.3495 | +8300732.54 | 21.28 |
| ${}^{152}$Gd | 152 | 88 | 82.2754 | -934257389.40 | 142681.5995 | +8262194.93 | 7.12 |
| ${}^{153}$Gd | 153 | 89 | 88.5812 | -929570266.16 | 143614.8591 | +8207647.13 | 7.03 |
| ${}^{154}$Gd | 154 | 90 | 94.8775 | -925093925.84 | 144548.1282 | +8172493.80 | 6.93 |
| ${}^{155}$Gd | 155 | 91 | 101.1644 | -920534147.54 | 145481.4068 | +8120677.22 | 6.81 |
| ${}^{156}$Gd | 156 | 92 | 107.4420 | -916165135.50 | 146414.6946 | +8084173.18 | 6.76 |
| ${}^{157}$Gd | 157 | 93 | 113.7105 | -911712061.81 | 147347.9915 | +8033187.06 | 6.68 |
| ${}^{158}$Gd | 158 | 94 | 119.9700 | -907422524.75 | 148281.2974 | +7993718.18 | 6.64 |
| ${}^{159}$Gd | 159 | 95 | 126.2207 | -903043712.43 | 149214.6121 | +7941228.04 | 6.61 |
| ${}^{160}$Gd | 160 | 96 | 132.4627 | -898828060.25 | 150147.9356 | +7899659.18 | 7.54 |
| ${}^{161}$Gd | 161 | 97 | 138.6960 | -894521173.31 | 151081.2676 | +7846454.33 | 10.03 |
| ${}^{162}$Gd | 162 | 98 | 144.9209 | -890357973.83 | 152014.6082 | +7802052.25 | 26.27 |
| ${}^{163}$Gd | 163 | 99 | 151.1374 | -886101088.48 | 152947.9571 | +7747184.20 | 5.25 |
| ${}^{164}$Gd | 164 | 100 | 157.3456 | -881989555.25 | 153881.3143 | +7700942.04 | 6.55 |
| ${}^{165}$Gd | 165 | 101 | 163.5458 | -877788860.77 | 154814.6796 | +7645653.79 | 8.49 |
| ${}^{166}$Gd | 166 | 102 | 169.7379 | -873720054.12 | 155748.0529 | +7597689.64 | 10.24 |
| ${}^{167}$Gd | 167 | 103 | 175.9221 | -869553601.18 | 156681.4341 | +7541020.27 | 33.52 |
| ${}^{168}$Gd | 168 | 104 | 182.0984 | -865518698.67 | 157614.8232 | +7491320.62 | 1917.26 |
| ${}^{169}$Gd | 169 | 105 | 188.2671 | -861355733.90 | 158548.2199 | +7431800.95 | 2539.17 |
| ${}^{170}$Gd | 170 | 106 | 194.4282 | -857341221.61 | 159481.6242 | +7380791.63 | 3159.64 |
| ${}^{171}$Gd | 171 | 107 | 200.5818 | -853192350.28 | 160415.0361 | +7320311.21 | 3141.06 |
| ${}^{172}$Gd | 172 | 108 | 206.7280 | -849233923.36 | 161348.4553 | +7269387.47 | 1872.48 |

### Terbium (Z = 65)

_40 of 40 isotopes with a framework prediction; 40 of 40 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{135}$Tb | 135 | 70 | -46.7653 | -1043633955.30 | 126837.2457 | +8897604.38 | 3178.61 |
| ${}^{136}$Tb | 136 | 71 | -40.2309 | -1037158077.73 | 127770.2767 | +8866974.30 | 3949.65 |
| ${}^{137}$Tb | 137 | 72 | -33.7093 | -1030760518.60 | 128703.3205 | +8854451.79 | 3139.69 |
| ${}^{138}$Tb | 138 | 73 | -27.2004 | -1024579639.54 | 129636.3770 | +8823099.55 | 2334.13 |
| ${}^{139}$Tb | 139 | 74 | -20.7039 | -1018498341.44 | 130569.4459 | +8807075.15 | 2303.01 |
| ${}^{140}$Tb | 140 | 75 | -14.2196 | -1012588002.56 | 131502.5270 | +8774518.80 | 6140.66 |
| ${}^{141}$Tb | 141 | 76 | -7.7473 | -1006785537.84 | 132435.6202 | +8755627.58 | 801.75 |
| ${}^{142}$Tb | 142 | 77 | -1.2870 | -1001117306.01 | 133368.7252 | +8721527.68 | 5298.60 |
| ${}^{143}$Tb | 143 | 78 | 5.1618 | -995564575.50 | 134301.8419 | +8701938.67 | 384.79 |
| ${}^{144}$Tb | 144 | 79 | 11.5991 | -990118238.87 | 135234.9701 | +8668331.51 | 208.43 |
| ${}^{145}$Tb | 145 | 80 | 18.0251 | -984800377.33 | 136168.1095 | +8650829.95 | 821.45 |
| ${}^{146}$Tb | 146 | 81 | 24.4399 | -979553711.79 | 137101.2601 | +8613855.12 | 330.02 |
| ${}^{147}$Tb | 147 | 82 | 30.8439 | -974432581.87 | 138034.4215 | +8589365.06 | 59.15 |
| ${}^{148}$Tb | 148 | 83 | 37.2370 | -969333041.68 | 138967.5938 | +8541972.25 | 90.44 |
| ${}^{149}$Tb | 149 | 84 | 43.6196 | -964341592.93 | 139900.7767 | +8503706.88 | 26.15 |
| ${}^{150}$Tb | 150 | 85 | 49.9917 | -959387733.18 | 140833.9700 | +8456389.20 | 52.77 |
| ${}^{151}$Tb | 151 | 86 | 56.3535 | -954536733.16 | 141767.1736 | +8416232.00 | 29.12 |
| ${}^{152}$Tb | 152 | 87 | 62.7052 | -949703231.18 | 142700.3873 | +8366528.12 | 282.74 |
| ${}^{153}$Tb | 153 | 88 | 69.0470 | -944998838.63 | 143633.6110 | +8328180.76 | 27.71 |
| ${}^{154}$Tb | 154 | 89 | 75.3788 | -940283916.31 | 144566.8445 | +8278070.84 | 316.01 |
| ${}^{155}$Tb | 155 | 90 | 81.7010 | -935741945.16 | 145500.0877 | +8244399.87 | 68.11 |
| ${}^{156}$Tb | 156 | 91 | 88.0137 | -931151304.72 | 146433.3405 | +8195585.58 | 25.94 |
| ${}^{157}$Tb | 157 | 92 | 94.3169 | -926721821.43 | 147366.6027 | +8160095.53 | 6.96 |
| ${}^{158}$Tb | 158 | 93 | 100.6109 | -922241310.89 | 148299.8741 | +8111645.93 | 8.61 |
| ${}^{159}$Tb | 159 | 94 | 106.8958 | -917900033.39 | 149233.1547 | +8073093.18 | 7.45 |
| ${}^{160}$Tb | 160 | 95 | 113.1716 | -913503478.96 | 150166.4443 | +8023188.54 | 7.45 |
| ${}^{161}$Tb | 161 | 96 | 119.4386 | -909247524.13 | 151099.7428 | +7982849.87 | 8.13 |
| ${}^{162}$Tb | 162 | 97 | 125.6968 | -904960979.48 | 152033.0500 | +7934998.47 | 13.59 |
| ${}^{163}$Tb | 163 | 98 | 131.9463 | -900745072.76 | 152966.3658 | +7889774.22 | 26.75 |
| ${}^{164}$Tb | 164 | 99 | 138.1874 | -896484859.68 | 153899.6902 | +7837192.10 | 12.20 |
| ${}^{165}$Tb | 165 | 100 | 144.4201 | -892344649.45 | 154833.0230 | +7791697.12 | 10.03 |
| ${}^{166}$Tb | 166 | 101 | 150.6445 | -888145969.44 | 155766.3640 | +7738564.47 | 9.46 |
| ${}^{167}$Tb | 167 | 102 | 156.8607 | -884059452.18 | 156699.7132 | +7691659.23 | 12.41 |
| ${}^{168}$Tb | 168 | 103 | 163.0689 | -879911887.75 | 157633.0704 | +7637789.07 | 26.79 |
| ${}^{169}$Tb | 169 | 104 | 169.2691 | -875871577.09 | 158566.4356 | +7589738.83 | 1905.94 |
| ${}^{170}$Tb | 170 | 105 | 175.4615 | -871737742.21 | 159499.8086 | +7532949.39 | 1894.68 |
| ${}^{171}$Tb | 171 | 106 | 181.6462 | -867713798.99 | 160433.1894 | +7482132.41 | 2509.46 |
| ${}^{172}$Tb | 172 | 107 | 187.8232 | -863602888.21 | 161366.5778 | +7424785.01 | 3122.87 |
| ${}^{173}$Tb | 173 | 108 | 193.9927 | -859621298.81 | 162299.9737 | +7373776.60 | 3104.75 |
| ${}^{174}$Tb | 174 | 109 | 200.1548 | -855542533.60 | 163233.3770 | +7314948.54 | 3086.82 |

### Dysprosium (Z = 66)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{138}$Dy | 138 | 72 | -47.5823 | -1043370979.33 | 129655.9766 | +8907556.67 | 3914.11 |
| ${}^{139}$Dy | 139 | 73 | -41.0445 | -1037044764.25 | 130589.0041 | +8876887.10 | 3864.43 |
| ${}^{140}$Dy | 140 | 74 | -34.5192 | -1030789939.69 | 131522.0443 | +8865017.41 | 3072.44 |
| ${}^{141}$Dy | 141 | 75 | -28.0064 | -1024744852.82 | 132455.0969 | +8833605.07 | 2270.29 |
| ${}^{142}$Dy | 142 | 76 | -21.5058 | -1018787897.46 | 133388.1618 | +8819399.36 | 5509.13 |
| ${}^{143}$Dy | 143 | 77 | -15.0172 | -1013004921.71 | 134321.2386 | +8785111.82 | 97.94 |
| ${}^{144}$Dy | 144 | 78 | -8.5404 | -1007317008.65 | 135254.3273 | +8769084.56 | 53.49 |
| ${}^{145}$Dy | 145 | 79 | -2.0753 | -1001763317.46 | 136187.4276 | +8732975.97 | 48.30 |
| ${}^{146}$Dy | 146 | 80 | 4.3783 | -996318674.80 | 137120.5393 | +8717034.07 | 49.25 |
| ${}^{147}$Dy | 147 | 81 | 10.8207 | -990975574.84 | 138053.6624 | +8681703.80 | 64.66 |
| ${}^{148}$Dy | 148 | 82 | 17.2520 | -985751366.98 | 138986.7965 | +8661733.70 | 63.31 |
| ${}^{149}$Dy | 149 | 83 | 23.6723 | -980575564.08 | 139919.9416 | +8614271.44 | 66.19 |
| ${}^{150}$Dy | 150 | 84 | 30.0818 | -975510822.29 | 140853.0975 | +8580381.94 | 30.92 |
| ${}^{151}$Dy | 151 | 85 | 36.4808 | -970482100.25 | 141786.2640 | +8531428.50 | 23.10 |
| ${}^{152}$Dy | 152 | 86 | 42.8693 | -965575794.74 | 142719.4409 | +8496896.07 | 32.45 |
| ${}^{153}$Dy | 153 | 87 | 49.2475 | -960678150.86 | 143652.6281 | +8446318.56 | 28.09 |
| ${}^{154}$Dy | 154 | 88 | 55.6155 | -955921635.04 | 144585.8255 | +8412122.27 | 51.82 |
| ${}^{155}$Dy | 155 | 89 | 61.9736 | -951147089.70 | 145519.0329 | +8361045.02 | 66.83 |
| ${}^{156}$Dy | 156 | 90 | 68.3218 | -946540887.80 | 146452.2501 | +8328821.42 | 6.80 |
| ${}^{157}$Dy | 157 | 91 | 74.6603 | -941897965.36 | 147385.4770 | +8279980.23 | 35.25 |
| ${}^{158}$Dy | 158 | 92 | 80.9893 | -937413626.67 | 148318.7134 | +8246128.53 | 15.89 |
| ${}^{159}$Dy | 159 | 93 | 87.3088 | -932884368.18 | 149251.9593 | +8197630.34 | 9.72 |
| ${}^{160}$Dy | 160 | 94 | 93.6191 | -928504945.67 | 150185.2145 | +8161612.03 | 4.70 |
| ${}^{161}$Dy | 161 | 95 | 99.9202 | -924067206.66 | 151118.4788 | +8111830.39 | 4.65 |
| ${}^{162}$Dy | 162 | 96 | 106.2122 | -919785323.44 | 152051.7522 | +8074370.83 | 4.61 |
| ${}^{163}$Dy | 163 | 97 | 112.4954 | -915440569.76 | 152985.0344 | +8024637.30 | 4.57 |
| ${}^{164}$Dy | 164 | 98 | 118.7698 | -911235267.76 | 153918.3255 | +7984725.53 | 4.55 |
| ${}^{165}$Dy | 165 | 99 | 125.0355 | -906949966.72 | 154851.6252 | +7932612.35 | 4.54 |
| ${}^{166}$Dy | 166 | 100 | 131.2927 | -902802912.60 | 155784.9334 | +7889840.67 | 5.19 |
| ${}^{167}$Dy | 167 | 101 | 137.5415 | -898582201.91 | 156718.2501 | +7836973.00 | 25.76 |
| ${}^{168}$Dy | 168 | 102 | 143.7819 | -894503330.70 | 157651.5750 | +7793293.47 | 895.00 |
| ${}^{169}$Dy | 169 | 103 | 150.0142 | -890341606.80 | 158584.9082 | +7739877.95 | 1910.62 |
| ${}^{170}$Dy | 170 | 104 | 156.2384 | -886312547.35 | 159518.2494 | +7693995.66 | 1265.13 |
| ${}^{171}$Dy | 171 | 105 | 162.4546 | -882159892.23 | 160451.5986 | +7637223.32 | 1257.70 |
| ${}^{172}$Dy | 172 | 106 | 168.6630 | -878171377.72 | 161384.9557 | +7590280.88 | 1872.65 |
| ${}^{173}$Dy | 173 | 107 | 174.8635 | -874062807.85 | 162318.3205 | +7532868.10 | 2480.44 |
| ${}^{174}$Dy | 174 | 108 | 181.0565 | -870109303.04 | 163251.6930 | +7484928.16 | 3086.99 |
| ${}^{175}$Dy | 175 | 109 | 187.2418 | -866021379.77 | 164185.0731 | +7426517.13 | 3069.26 |
| ${}^{176}$Dy | 176 | 110 | 193.4197 | -862093654.83 | 165118.4606 | +7376690.35 | 3051.76 |

### Holmium (Z = 67)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{140}$Ho | 140 | 73 | -55.0918 | -1049773966.01 | 131541.8346 | +8912250.36 | 3836.58 |
| ${}^{141}$Ho | 141 | 74 | -48.5378 | -1043338744.35 | 132474.8460 | +8899359.87 | 3050.44 |
| ${}^{142}$Ho | 142 | 75 | -41.9964 | -1037131071.38 | 133407.8700 | +8870257.37 | 3029.02 |
| ${}^{143}$Ho | 143 | 76 | -35.4673 | -1031006771.09 | 134340.9064 | +8856134.91 | 2238.47 |
| ${}^{144}$Ho | 144 | 77 | -28.9505 | -1025077015.56 | 135273.9549 | +8825480.98 | 63.22 |
| ${}^{145}$Ho | 145 | 78 | -22.4456 | -1019232880.09 | 136207.0155 | +8809897.74 | 55.19 |
| ${}^{146}$Ho | 146 | 79 | -15.9526 | -1013550911.38 | 137140.0879 | +8776860.54 | 48.45 |
| ${}^{147}$Ho | 147 | 80 | -9.4712 | -1007960159.79 | 138073.1719 | +8762050.27 | 36.53 |
| ${}^{148}$Ho | 148 | 81 | -3.0012 | -1002500763.09 | 139006.2674 | +8730797.09 | 608.36 |
| ${}^{149}$Ho | 149 | 82 | 3.4574 | -997146991.31 | 139939.3742 | +8710373.08 | 86.39 |
| ${}^{150}$Ho | 150 | 83 | 9.9050 | -991882654.31 | 140872.4920 | +8666071.48 | 101.44 |
| ${}^{151}$Ho | 151 | 84 | 16.3416 | -986713848.18 | 141805.6208 | +8632311.96 | 59.02 |
| ${}^{152}$Ho | 152 | 85 | 22.7675 | -981609874.75 | 142738.7604 | +8586992.62 | 88.52 |
| ${}^{153}$Ho | 153 | 86 | 29.1827 | -976607151.75 | 143671.9105 | +8552433.04 | 35.56 |
| ${}^{154}$Ho | 154 | 87 | 35.5875 | -971648043.38 | 144605.0712 | +8505873.96 | 57.30 |
| ${}^{155}$Ho | 155 | 88 | 41.9820 | -966804159.49 | 145538.2421 | +8472377.84 | 121.05 |
| ${}^{156}$Ho | 156 | 89 | 48.3664 | -961983513.46 | 146471.4232 | +8426176.46 | 264.54 |
| ${}^{157}$Ho | 157 | 90 | 54.7407 | -957287644.16 | 147404.6143 | +8393021.03 | 160.54 |
| ${}^{158}$Ho | 158 | 91 | 61.1052 | -952596312.20 | 148337.8152 | +8347054.73 | 184.25 |
| ${}^{159}$Ho | 159 | 92 | 67.4599 | -948037866.48 | 149271.0259 | +8313908.86 | 20.56 |
| ${}^{160}$Ho | 160 | 93 | 73.8051 | -943460636.48 | 150204.2461 | +8267099.62 | 100.79 |
| ${}^{161}$Ho | 161 | 94 | 80.1409 | -939022107.26 | 151137.4758 | +8232780.24 | 14.35 |
| ${}^{162}$Ho | 162 | 95 | 86.4673 | -934552800.07 | 152070.7148 | +8185781.15 | 20.56 |
| ${}^{163}$Ho | 163 | 96 | 92.7846 | -930215407.29 | 153003.9629 | +8149338.96 | 4.57 |
| ${}^{164}$Ho | 164 | 97 | 99.0928 | -925843136.73 | 153937.2201 | +8101946.33 | 9.10 |
| ${}^{165}$Ho | 165 | 98 | 105.3921 | -921597738.88 | 154870.4862 | +8063815.77 | 5.12 |
| ${}^{166}$Ho | 166 | 99 | 111.6826 | -917302282.96 | 155803.7612 | +8014820.27 | 5.09 |
| ${}^{167}$Ho | 167 | 100 | 117.9644 | -913119152.93 | 156737.0448 | +7973189.49 | 33.37 |
| ${}^{168}$Ho | 168 | 101 | 124.2377 | -908891517.00 | 157670.3370 | +7922899.94 | 191.78 |
| ${}^{169}$Ho | 169 | 102 | 130.5025 | -904772718.23 | 158603.6376 | +7879390.21 | 127.40 |
| ${}^{170}$Ho | 170 | 103 | 136.7589 | -900607213.33 | 159536.9465 | +7828199.25 | 315.98 |
| ${}^{171}$Ho | 171 | 104 | 143.0072 | -896543722.09 | 160470.2637 | +7782969.29 | 3768.12 |
| ${}^{172}$Ho | 172 | 105 | 149.2473 | -892422876.97 | 161403.5890 | +7730046.72 | 1221.32 |
| ${}^{173}$Ho | 173 | 106 | 155.4795 | -888412554.38 | 162336.9223 | +7683423.73 | 1850.28 |
| ${}^{174}$Ho | 174 | 107 | 161.7037 | -884325157.07 | 163270.2634 | +7629004.80 | 1851.10 |
| ${}^{175}$Ho | 175 | 108 | 167.9202 | -880341220.08 | 164203.6124 | +7580890.52 | 2452.08 |
| ${}^{176}$Ho | 176 | 109 | 174.1289 | -876282507.34 | 165136.9691 | +7525137.59 | 3051.87 |
| ${}^{177}$Ho | 177 | 110 | 180.3301 | -872329084.20 | 166070.3334 | +7474948.24 | 3034.57 |
| ${}^{178}$Ho | 178 | 111 | 186.5237 | -868306388.62 | 167003.7051 | +7419052.59 | 3017.44 |

### Erbium (Z = 68)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{142}$Er | 142 | 74 | -62.7586 | -1055994205.37 | 133427.8499 | +8950236.25 | 3782.49 |
| ${}^{143}$Er | 143 | 75 | -56.1885 | -1049630763.12 | 134360.8452 | +8923379.70 | 3000.70 |
| ${}^{144}$Er | 144 | 76 | -49.6310 | -1043320707.97 | 135293.8531 | +8913668.03 | 1458.73 |
| ${}^{145}$Er | 145 | 77 | -43.0858 | -1037259361.20 | 136226.8734 | +8883148.12 | 1483.19 |
| ${}^{146}$Er | 146 | 78 | -36.5528 | -1031254123.52 | 137159.9058 | +8871311.41 | 49.31 |
| ${}^{147}$Er | 147 | 79 | -30.0318 | -1025452978.90 | 138092.9502 | +8839114.54 | 279.01 |
| ${}^{148}$Er | 148 | 80 | -23.5225 | -1019719873.45 | 139026.0064 | +8826363.30 | 74.35 |
| ${}^{149}$Er | 149 | 81 | -17.0249 | -1014150092.42 | 139959.0742 | +8794898.49 | 201.42 |
| ${}^{150}$Er | 150 | 82 | -10.5388 | -1008671547.29 | 140892.1535 | +8777130.68 | 123.10 |
| ${}^{151}$Er | 151 | 83 | -4.0639 | -1003320624.54 | 141825.2440 | +8733455.40 | 117.14 |
| ${}^{152}$Er | 152 | 84 | 2.3999 | -998055418.07 | 142758.3456 | +8703254.77 | 62.38 |
| ${}^{153}$Er | 153 | 85 | 8.8527 | -992873215.31 | 143691.4582 | +8657470.14 | 65.17 |
| ${}^{154}$Er | 154 | 86 | 15.2948 | -987787478.05 | 144624.5815 | +8627632.54 | 34.59 |
| ${}^{155}$Er | 155 | 87 | 21.7263 | -982757789.94 | 145557.7155 | +8580542.87 | 42.08 |
| ${}^{156}$Er | 156 | 88 | 28.1473 | -977839179.60 | 146490.8599 | +8550782.08 | 169.56 |
| ${}^{157}$Er | 157 | 89 | 34.5580 | -972946846.77 | 147424.0146 | +8502148.97 | 181.31 |
| ${}^{158}$Er | 158 | 90 | 40.9585 | -968184390.61 | 148357.1795 | +8472629.11 | 171.43 |
| ${}^{159}$Er | 159 | 91 | 47.3491 | -963428568.21 | 149290.3544 | +8425613.00 | 24.60 |
| ${}^{160}$Er | 160 | 92 | 53.7297 | -958804915.51 | 150223.5392 | +8394452.76 | 162.75 |
| ${}^{161}$Er | 161 | 93 | 60.1007 | -954173531.78 | 151156.7337 | +8347829.19 | 58.53 |
| ${}^{162}$Er | 162 | 94 | 66.4620 | -949676217.38 | 152089.9377 | +8315186.97 | 5.01 |
| ${}^{163}$Er | 163 | 95 | 72.8139 | -945153423.03 | 153023.1513 | +8267729.00 | 30.49 |
| ${}^{164}$Er | 164 | 96 | 79.1565 | -940770605.85 | 153956.3741 | +8233733.91 | 4.61 |
| ${}^{165}$Er | 165 | 97 | 85.4899 | -936348345.96 | 154889.6062 | +8185796.96 | 5.97 |
| ${}^{166}$Er | 166 | 98 | 91.8142 | -932068182.34 | 155822.8473 | +8150394.48 | 2.16 |
| ${}^{167}$Er | 167 | 99 | 98.1295 | -927739668.32 | 156756.0973 | +8102262.78 | 1.83 |
| ${}^{168}$Er | 168 | 100 | 104.4361 | -923533267.26 | 157689.3562 | +8063363.84 | 1.67 |
| ${}^{169}$Er | 169 | 101 | 110.7339 | -919276892.74 | 158622.6238 | +8013655.17 | 1.93 |
| ${}^{170}$Er | 170 | 102 | 117.0231 | -915141103.09 | 159555.9000 | +7972574.80 | 8.76 |
| ${}^{171}$Er | 171 | 103 | 123.3039 | -910953492.20 | 160489.1846 | +7922052.16 | 8.84 |
| ${}^{172}$Er | 172 | 104 | 129.5763 | -906883433.00 | 161422.4776 | +7879435.69 | 24.74 |
| ${}^{173}$Er | 173 | 105 | 135.8405 | -902748920.80 | 162355.7789 | +7827396.12 | 1214.28 |
| ${}^{174}$Er | 174 | 106 | 142.0965 | -898729321.78 | 163289.0883 | +7782997.23 | 1839.67 |
| ${}^{175}$Er | 175 | 107 | 148.3445 | -894632311.77 | 164222.4057 | +7729306.15 | 2457.88 |
| ${}^{176}$Er | 176 | 108 | 154.5846 | -890674430.88 | 165155.7311 | +7684121.97 | 2443.88 |
| ${}^{177}$Er | 177 | 109 | 160.8169 | -886613031.16 | 166089.0642 | +7628791.68 | 3051.64 |
| ${}^{178}$Er | 178 | 110 | 167.0414 | -882681000.87 | 167022.4051 | +7581272.00 | 3596.38 |
| ${}^{179}$Er | 179 | 111 | 173.2583 | -878645527.07 | 167955.7537 | +7524765.41 | 3000.65 |
| ${}^{180}$Er | 180 | 112 | 179.4676 | -874743417.37 | 168889.1097 | +7476631.99 | 2983.92 |

### Thulium (Z = 69)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{144}$Tm | 144 | 75 | -70.5820 | -1062439831.86 | 135314.0218 | +8955360.36 | 2979.66 |
| ${}^{145}$Tm | 145 | 76 | -63.9959 | -1055945087.03 | 136247.0011 | +8945104.49 | 1448.57 |
| ${}^{146}$Tm | 146 | 77 | -57.4223 | -1049697158.46 | 137179.9929 | +8920606.64 | 1472.94 |
| ${}^{147}$Tm | 147 | 78 | -50.8610 | -1043527670.29 | 138112.9971 | +8907193.31 | 49.95 |
| ${}^{148}$Tm | 148 | 79 | -44.3120 | -1037573587.91 | 139046.0135 | +8878465.92 | 74.35 |
| ${}^{149}$Tm | 149 | 80 | -37.7749 | -1031674475.84 | 139979.0418 | +8867549.22 | 1443.41 |
| ${}^{150}$Tm | 150 | 81 | -31.2495 | -1025973092.67 | 140912.0819 | +8837902.16 | 1400.47 |
| ${}^{151}$Tm | 151 | 82 | -24.7358 | -1020349332.08 | 141845.1336 | +8821144.01 | 137.79 |
| ${}^{152}$Tm | 152 | 83 | -18.2335 | -1014889628.98 | 142778.1967 | +8780936.56 | 381.72 |
| ${}^{153}$Tm | 153 | 84 | -11.7425 | -1009508848.82 | 143711.2711 | +8750564.21 | 84.08 |
| ${}^{154}$Tm | 154 | 85 | -5.2626 | -1004232309.30 | 144644.3566 | +8708016.22 | 100.50 |
| ${}^{155}$Tm | 155 | 86 | 1.2064 | -999037709.31 | 145577.4530 | +8678283.21 | 68.74 |
| ${}^{156}$Tm | 156 | 87 | 7.6646 | -993926483.28 | 146510.5602 | +8635184.42 | 98.29 |
| ${}^{157}$Tm | 157 | 88 | 14.1123 | -988904801.08 | 147443.6780 | +8604204.27 | 191.16 |
| ${}^{158}$Tm | 158 | 89 | 20.5494 | -983945650.41 | 148376.8063 | +8560791.83 | 171.42 |
| ${}^{159}$Tm | 159 | 90 | 26.9762 | -979087024.00 | 149309.9449 | +8530756.40 | 188.76 |
| ${}^{160}$Tm | 160 | 91 | 33.3929 | -974268218.05 | 150243.0937 | +8486700.69 | 219.40 |
| ${}^{161}$Tm | 161 | 92 | 39.7996 | -969558216.83 | 151176.2524 | +8455819.16 | 186.41 |
| ${}^{162}$Tm | 162 | 93 | 46.1963 | -964871021.81 | 152109.4211 | +8411886.72 | 172.75 |
| ${}^{163}$Tm | 163 | 94 | 52.5834 | -960295603.71 | 153042.5995 | +8379667.85 | 36.33 |
| ${}^{164}$Tm | 164 | 95 | 58.9608 | -955722613.24 | 153975.7875 | +8334232.90 | 163.76 |
| ${}^{165}$Tm | 165 | 96 | 65.3288 | -951273219.73 | 154908.9849 | +8301490.47 | 10.79 |
| ${}^{166}$Tm | 166 | 97 | 71.6874 | -946809328.84 | 155842.1917 | +8255734.66 | 74.73 |
| ${}^{167}$Tm | 167 | 98 | 78.0368 | -942470747.93 | 156775.4078 | +8221610.54 | 8.09 |
| ${}^{168}$Tm | 168 | 99 | 84.3771 | -938108732.81 | 157708.6329 | +8175786.51 | 10.72 |
| ${}^{169}$Tm | 169 | 100 | 90.7085 | -933854409.52 | 158641.8669 | +8138205.67 | 4.69 |
| ${}^{170}$Tm | 170 | 101 | 97.0310 | -929582457.63 | 159575.1098 | +8091942.04 | 4.62 |
| ${}^{171}$Tm | 171 | 102 | 103.3448 | -925405667.97 | 160508.3615 | +8051937.07 | 6.10 |
| ${}^{172}$Tm | 172 | 103 | 109.6499 | -921209153.43 | 161441.6217 | +8004573.70 | 34.22 |
| ${}^{173}$Tm | 173 | 104 | 115.9466 | -917098803.12 | 162374.8904 | +7962312.13 | 27.31 |
| ${}^{174}$Tm | 174 | 105 | 122.2349 | -912956187.11 | 163308.1676 | +7912663.23 | 276.01 |
| ${}^{175}$Tm | 175 | 106 | 128.5150 | -908906928.13 | 164241.4530 | +7868814.40 | 306.82 |
| ${}^{176}$Tm | 176 | 107 | 134.7868 | -904807630.96 | 165174.7465 | +7816996.27 | 610.15 |
| ${}^{177}$Tm | 177 | 108 | 141.0506 | -900821888.02 | 166108.0481 | +7772769.05 | 1215.04 |
| ${}^{178}$Tm | 178 | 109 | 147.3065 | -896773807.74 | 167041.3577 | +7719802.34 | 1809.47 |
| ${}^{179}$Tm | 179 | 110 | 153.5545 | -892822826.96 | 167974.6752 | +7673456.78 | 2397.25 |
| ${}^{180}$Tm | 180 | 111 | 159.7947 | -888795157.67 | 168908.0003 | +7619314.23 | 2383.88 |
| ${}^{181}$Tm | 181 | 112 | 166.0273 | -884894251.97 | 169841.3332 | +7571797.74 | 2967.47 |
| ${}^{182}$Tm | 182 | 113 | 172.2523 | -880920846.10 | 170774.6736 | +7517601.87 | 2951.10 |

### Ytterbium (Z = 70)

_38 of 38 isotopes with a framework prediction; 38 of 38 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{148}$Yb | 148 | 78 | -65.3695 | -1055867167.25 | 139066.2887 | +8963092.55 | 2899.28 |
| ${}^{149}$Yb | 149 | 79 | -58.7923 | -1049776605.80 | 139999.2769 | +8936231.95 | 2161.59 |
| ${}^{150}$Yb | 150 | 80 | -52.2272 | -1043713932.12 | 140932.2772 | +8927153.14 | 2147.26 |
| ${}^{151}$Yb | 151 | 81 | -45.6741 | -1037886614.21 | 141865.2895 | +8898272.00 | 2137.00 |
| ${}^{152}$Yb | 152 | 82 | -39.1327 | -1032119555.71 | 142798.3136 | +8884222.25 | 1057.70 |
| ${}^{153}$Yb | 153 | 83 | -32.6030 | -1026563380.81 | 143731.3493 | +8843253.75 | 1405.69 |
| ${}^{154}$Yb | 154 | 84 | -26.0847 | -1021067432.38 | 144664.3964 | +8816144.12 | 120.50 |
| ${}^{155}$Yb | 155 | 85 | -19.5776 | -1015702355.25 | 145597.4547 | +8774071.46 | 115.01 |
| ${}^{156}$Yb | 156 | 86 | -13.0816 | -1010401808.33 | 146530.5241 | +8747839.16 | 64.07 |
| ${}^{157}$Yb | 157 | 87 | -6.5965 | -1005211140.35 | 147463.6045 | +8704015.89 | 74.59 |
| ${}^{158}$Yb | 158 | 88 | -0.1222 | -1000095766.80 | 148396.6956 | +8677517.40 | 54.19 |
| ${}^{159}$Yb | 159 | 89 | 6.3414 | -995062768.02 | 149329.7974 | +8632580.13 | 118.75 |
| ${}^{160}$Yb | 160 | 90 | 12.7946 | -990118524.19 | 150262.9096 | +8605239.28 | 36.89 |
| ${}^{161}$Yb | 161 | 91 | 19.2375 | -985230899.25 | 151196.0321 | +8560419.11 | 100.73 |
| ${}^{162}$Yb | 162 | 92 | 25.6702 | -980443361.99 | 152129.1648 | +8531703.96 | 100.12 |
| ${}^{163}$Yb | 163 | 93 | 32.0929 | -975690009.70 | 153062.3076 | +8486700.33 | 99.52 |
| ${}^{164}$Yb | 164 | 94 | 38.5057 | -971047091.10 | 153995.4602 | +8457140.37 | 98.92 |
| ${}^{165}$Yb | 165 | 95 | 44.9088 | -966418265.63 | 154928.6225 | +8412018.47 | 172.73 |
| ${}^{166}$Yb | 166 | 96 | 51.3022 | -961904315.85 | 155861.7945 | +8380649.25 | 45.29 |
| ${}^{167}$Yb | 167 | 97 | 57.6862 | -957387396.95 | 156794.9760 | +8334787.96 | 25.47 |
| ${}^{168}$Yb | 168 | 98 | 64.0608 | -952993142.66 | 157728.1668 | +8302384.39 | 0.60 |
| ${}^{169}$Yb | 169 | 99 | 70.4262 | -948581419.40 | 158661.3669 | +8256363.07 | 1.13 |
| ${}^{170}$Yb | 170 | 100 | 76.7824 | -944284794.30 | 159594.5760 | +8221086.16 | 0.06 |
| ${}^{171}$Yb | 171 | 101 | 83.1297 | -939967172.90 | 160527.7942 | +8174592.87 | 0.08 |
| ${}^{172}$Yb | 172 | 102 | 89.4682 | -935761874.27 | 161461.0212 | +8137545.20 | 0.08 |
| ${}^{173}$Yb | 173 | 103 | 95.7978 | -931530181.79 | 162394.2569 | +8090636.76 | 0.07 |
| ${}^{174}$Yb | 174 | 104 | 102.1189 | -927399661.26 | 163327.5013 | +8051150.21 | 0.06 |
| ${}^{175}$Yb | 175 | 105 | 108.4314 | -923229614.70 | 164260.7542 | +8002009.09 | 0.43 |
| ${}^{176}$Yb | 176 | 106 | 114.7355 | -919159285.48 | 165194.0155 | +7959904.51 | 0.09 |
| ${}^{177}$Yb | 177 | 107 | 121.0314 | -915056502.65 | 166127.2851 | +7910372.93 | 1.33 |
| ${}^{178}$Yb | 178 | 108 | 127.3190 | -911065716.63 | 167060.5629 | +7868719.00 | 39.74 |
| ${}^{179}$Yb | 179 | 109 | 133.5985 | -907007164.31 | 167993.8487 | +7817132.35 | 1201.45 |
| ${}^{180}$Yb | 180 | 110 | 139.8701 | -903061869.11 | 168927.1426 | +7772886.53 | 1789.37 |
| ${}^{181}$Yb | 181 | 111 | 146.1338 | -899028403.49 | 169860.4443 | +7718941.84 | 1768.39 |
| ${}^{182}$Yb | 182 | 112 | 152.3897 | -895127024.27 | 170793.7539 | +7674222.04 | 2357.68 |
| ${}^{183}$Yb | 183 | 113 | 158.6379 | -891137308.90 | 171727.0711 | +7619914.91 | 2344.74 |
| ${}^{184}$Yb | 184 | 114 | 164.8785 | -887299869.47 | 172660.3959 | +7575068.31 | 2935.34 |
| ${}^{185}$Yb | 185 | 115 | 171.1116 | -883348768.72 | 173593.7282 | +7520690.76 | 2903.18 |

### Lutetium (Z = 71)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{150}$Lu | 150 | 79 | -73.4719 | -1062269572.42 | 140952.7395 | +8972090.83 | 2147.05 |
| ${}^{151}$Lu | 151 | 80 | -66.8788 | -1056035647.35 | 141885.7119 | +8962844.48 | 2132.91 |
| ${}^{152}$Lu | 152 | 81 | -60.2978 | -1050049955.54 | 142818.6963 | +8936641.78 | 1381.91 |
| ${}^{153}$Lu | 153 | 82 | -53.7287 | -1044121659.90 | 143751.6927 | +8923836.91 | 1052.90 |
| ${}^{154}$Lu | 154 | 83 | -47.1714 | -1038442272.29 | 144684.7008 | +8885515.61 | 1402.99 |
| ${}^{155}$Lu | 155 | 84 | -40.6257 | -1032814210.62 | 145617.7205 | +8858860.92 | 133.33 |
| ${}^{156}$Lu | 156 | 85 | -34.0914 | -1027332645.98 | 146550.7516 | +8820654.40 | 372.56 |
| ${}^{157}$Lu | 157 | 86 | -27.5684 | -1021912873.40 | 147483.7940 | +8793953.09 | 82.58 |
| ${}^{158}$Lu | 158 | 87 | -21.0564 | -1016619968.56 | 148416.8475 | +8754171.70 | 102.79 |
| ${}^{159}$Lu | 159 | 88 | -14.5554 | -1011393611.42 | 149349.9118 | +8726709.99 | 254.38 |
| ${}^{160}$Lu | 160 | 89 | -8.0651 | -1006270792.63 | 150282.9870 | +8686561.97 | 381.38 |
| ${}^{161}$Lu | 161 | 90 | -1.5854 | -1001222849.08 | 151216.0727 | +8658630.03 | 186.40 |
| ${}^{162}$Lu | 162 | 91 | 4.8838 | -996257183.06 | 152149.1690 | +8617585.10 | 497.42 |
| ${}^{163}$Lu | 163 | 92 | 11.3426 | -991373557.98 | 153082.2755 | +8588343.58 | 184.12 |
| ${}^{164}$Lu | 164 | 93 | 17.7913 | -986550155.35 | 154015.3922 | +8545598.02 | 182.99 |
| ${}^{165}$Lu | 165 | 94 | 24.2300 | -981818352.56 | 154948.5190 | +8516228.95 | 172.73 |
| ${}^{166}$Lu | 166 | 95 | 30.6588 | -977125659.52 | 155881.6557 | +8472785.66 | 192.84 |
| ${}^{167}$Lu | 167 | 96 | 37.0778 | -972532729.00 | 156814.8021 | +8442419.55 | 239.61 |
| ${}^{168}$Lu | 168 | 97 | 43.4872 | -967965433.45 | 157747.9581 | +8399849.48 | 242.74 |
| ${}^{169}$Lu | 169 | 98 | 49.8871 | -963495194.43 | 158681.1237 | +8367219.50 | 19.10 |
| ${}^{170}$Lu | 170 | 99 | 56.2776 | -959037603.75 | 159614.2986 | +8323655.74 | 106.40 |
| ${}^{171}$Lu | 171 | 100 | 62.6588 | -954676405.10 | 160547.4827 | +8288882.83 | 11.69 |
| ${}^{172}$Lu | 172 | 101 | 69.0310 | -950317980.74 | 161480.6760 | +8244406.62 | 14.58 |
| ${}^{173}$Lu | 173 | 102 | 75.3941 | -946057362.03 | 162413.8783 | +8208245.13 | 9.73 |
| ${}^{174}$Lu | 174 | 103 | 81.7484 | -941792592.70 | 163347.0894 | +8163496.55 | 9.67 |
| ${}^{175}$Lu | 175 | 104 | 88.0939 | -937614954.29 | 164280.3093 | +8124919.66 | 7.40 |
| ${}^{176}$Lu | 176 | 105 | 94.4308 | -933423875.43 | 165213.5379 | +8078353.67 | 7.39 |
| ${}^{177}$Lu | 177 | 106 | 100.7591 | -929314729.95 | 166146.7750 | +8037167.28 | 7.40 |
| ${}^{178}$Lu | 178 | 107 | 107.0789 | -925197343.81 | 167080.0206 | +7990124.52 | 13.58 |
| ${}^{179}$Lu | 179 | 108 | 113.3905 | -921162336.14 | 168013.2744 | +7948297.50 | 30.89 |
| ${}^{180}$Lu | 180 | 109 | 119.6938 | -917107637.18 | 168946.5365 | +7900348.69 | 421.93 |
| ${}^{181}$Lu | 181 | 110 | 125.9891 | -913120531.57 | 169879.8067 | +7855989.77 | 746.05 |
| ${}^{182}$Lu | 182 | 111 | 132.2763 | -909105450.90 | 170813.0849 | +7805338.76 | 1181.61 |
| ${}^{183}$Lu | 183 | 112 | 138.5556 | -905178182.60 | 171746.3710 | +7761045.67 | 470.05 |
| ${}^{184}$Lu | 184 | 113 | 144.8271 | -901204493.93 | 172679.6649 | +7709272.11 | 1168.73 |
| ${}^{185}$Lu | 185 | 114 | 151.0909 | -897334070.89 | 173612.9666 | +7664397.49 | 1740.88 |
| ${}^{186}$Lu | 186 | 115 | 157.3470 | -893403244.76 | 174546.2758 | +7612486.80 | 2306.86 |
| ${}^{187}$Lu | 187 | 116 | 163.5957 | -889581823.73 | 175479.5926 | +7567481.76 | 2294.48 |
| ${}^{188}$Lu | 188 | 117 | 169.8369 | -885690539.00 | 176412.9169 | +7514948.79 | 2282.23 |

### Hafnium (Z = 72)

_38 of 38 isotopes with a framework prediction; 38 of 38 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{153}$Hf | 153 | 81 | -75.1197 | -1062291117.60 | 143772.3013 | +8990048.60 | 2104.98 |
| ${}^{154}$Hf | 154 | 82 | -68.5229 | -1056195243.37 | 144705.2699 | +8980139.18 | 2091.39 |
| ${}^{155}$Hf | 155 | 83 | -61.9380 | -1050397278.78 | 145638.2505 | +8943529.35 | 2077.91 |
| ${}^{156}$Hf | 156 | 84 | -55.3648 | -1044626891.05 | 146571.2427 | +8920872.32 | 1030.73 |
| ${}^{157}$Hf | 157 | 85 | -48.8032 | -1039051346.83 | 147504.2465 | +8881504.41 | 1369.79 |
| ${}^{158}$Hf | 158 | 86 | -42.2531 | -1033506473.27 | 148437.2618 | +8857885.28 | 118.89 |
| ${}^{159}$Hf | 159 | 87 | -35.7141 | -1028124373.81 | 149370.2883 | +8817620.13 | 113.55 |
| ${}^{160}$Hf | 160 | 88 | -29.1862 | -1022783577.43 | 150303.3258 | +8793748.14 | 64.03 |
| ${}^{161}$Hf | 161 | 89 | -22.6693 | -1017580321.02 | 151236.3743 | +8752016.57 | 156.41 |
| ${}^{162}$Hf | 162 | 90 | -16.1631 | -1012429390.87 | 152169.4335 | +8727424.76 | 59.34 |
| ${}^{163}$Hf | 163 | 91 | -9.6675 | -1007387878.51 | 153102.5034 | +8684916.91 | 169.27 |
| ${}^{164}$Hf | 164 | 92 | -3.1824 | -1002412409.54 | 154035.5837 | +8659165.63 | 103.54 |
| ${}^{165}$Hf | 165 | 93 | 3.2924 | -997519078.17 | 154968.6743 | +8615858.94 | 181.88 |
| ${}^{166}$Hf | 166 | 94 | 9.7570 | -992704353.81 | 155901.7751 | +8588841.02 | 180.79 |
| ${}^{167}$Hf | 167 | 95 | 16.2115 | -987947254.54 | 156834.8860 | +8545252.45 | 179.70 |
| ${}^{168}$Hf | 168 | 96 | 22.6562 | -983279724.63 | 157768.0068 | +8516971.04 | 178.63 |
| ${}^{169}$Hf | 169 | 97 | 29.0911 | -978647819.15 | 158701.1373 | +8472830.98 | 177.58 |
| ${}^{170}$Hf | 170 | 98 | 35.5163 | -974114385.44 | 159634.2775 | +8443163.24 | 176.53 |
| ${}^{171}$Hf | 171 | 99 | 41.9321 | -969598970.10 | 160567.4271 | +8398959.07 | 181.35 |
| ${}^{172}$Hf | 172 | 100 | 48.3384 | -965182568.51 | 161500.5862 | +8366619.12 | 152.52 |
| ${}^{173}$Hf | 173 | 101 | 54.7355 | -960774892.99 | 162433.7545 | +8322433.69 | 173.47 |
| ${}^{174}$Hf | 174 | 102 | 61.1235 | -956462419.00 | 163366.9320 | +8287670.05 | 13.94 |
| ${}^{175}$Hf | 175 | 103 | 67.5024 | -952147425.15 | 164300.1185 | +8242249.13 | 14.00 |
| ${}^{176}$Hf | 176 | 104 | 73.8725 | -947933099.43 | 165233.3138 | +8206365.62 | 9.04 |
| ${}^{177}$Hf | 177 | 105 | 80.2338 | -943702529.58 | 166166.5180 | +8159989.89 | 8.56 |
| ${}^{178}$Hf | 178 | 106 | 86.5863 | -939568480.79 | 167099.7308 | +8121793.00 | 8.54 |
| ${}^{179}$Hf | 179 | 107 | 92.9304 | -935415684.77 | 168032.9522 | +8074839.96 | 8.49 |
| ${}^{180}$Hf | 180 | 108 | 99.2659 | -931365008.07 | 168966.1821 | +8036210.70 | 8.47 |
| ${}^{181}$Hf | 181 | 109 | 105.5932 | -927276550.07 | 169899.4203 | +7987933.83 | 8.44 |
| ${}^{182}$Hf | 182 | 110 | 111.9122 | -923279542.71 | 170832.6667 | +7946322.59 | 36.38 |
| ${}^{183}$Hf | 183 | 111 | 118.2230 | -919246883.94 | 171765.9213 | +7896859.20 | 176.28 |
| ${}^{184}$Hf | 184 | 112 | 124.5258 | -915305420.34 | 172699.1839 | +7853757.86 | 231.71 |
| ${}^{185}$Hf | 185 | 113 | 130.8207 | -911319080.90 | 173632.4544 | +7803006.15 | 373.06 |
| ${}^{186}$Hf | 186 | 114 | 137.1078 | -907444686.17 | 174565.7328 | +7760317.67 | 295.76 |
| ${}^{187}$Hf | 187 | 115 | 143.3871 | -903513800.77 | 175499.0189 | +7709286.41 | 1149.95 |
| ${}^{188}$Hf | 188 | 116 | 149.6587 | -899690385.83 | 176432.3127 | +7666059.49 | 1713.07 |
| ${}^{189}$Hf | 189 | 117 | 155.9228 | -895795308.68 | 177365.6140 | +7614695.96 | 1703.97 |
| ${}^{190}$Hf | 190 | 118 | 162.1795 | -892020726.36 | 178298.9228 | +7571485.87 | 2258.21 |

### Tantalum (Z = 73)

_40 of 40 isotopes with a framework prediction; 40 of 40 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{155}$Ta | 155 | 82 | -83.5144 | -1068567413.17 | 145659.0445 | +9015433.32 | 2077.76 |
| ${}^{156}$Ta | 156 | 83 | -76.9019 | -1062622025.11 | 146591.9974 | +8981652.13 | 2064.47 |
| ${}^{157}$Ta | 157 | 84 | -70.3012 | -1056709059.78 | 147524.9621 | +8959299.64 | 1026.24 |
| ${}^{158}$Ta | 158 | 85 | -63.7122 | -1050998093.24 | 148457.9386 | +8923096.90 | 1361.05 |
| ${}^{159}$Ta | 159 | 86 | -57.1348 | -1045321096.61 | 149390.9266 | +8899679.26 | 132.97 |
| ${}^{160}$Ta | 160 | 87 | -50.5688 | -1039814108.57 | 150323.9261 | +8863520.19 | 364.53 |
| ${}^{161}$Ta | 161 | 88 | -44.0141 | -1034355126.39 | 151256.9367 | +8838450.74 | 162.61 |
| ${}^{162}$Ta | 162 | 89 | -37.4703 | -1029041747.43 | 152189.9584 | +8800709.99 | 419.73 |
| ${}^{163}$Ta | 163 | 90 | -30.9376 | -1023778950.81 | 153122.9911 | +8775136.54 | 250.75 |
| ${}^{164}$Ta | 164 | 91 | -24.4155 | -1018639696.62 | 154056.0345 | +8736700.91 | 182.98 |
| ${}^{165}$Ta | 165 | 92 | -17.9041 | -1013558553.83 | 154989.0885 | +8710727.71 | 88.34 |
| ${}^{166}$Ta | 166 | 93 | -11.4032 | -1008581400.92 | 155922.1530 | +8670027.41 | 180.78 |
| ${}^{167}$Ta | 167 | 94 | -4.9126 | -1003668419.91 | 156855.2278 | +8642874.65 | 179.70 |
| ${}^{168}$Ta | 168 | 95 | 1.5679 | -998836256.00 | 157788.3127 | +8601858.44 | 178.63 |
| ${}^{169}$Ta | 169 | 96 | 8.0383 | -994077460.76 | 158721.4078 | +8573271.34 | 177.57 |
| ${}^{170}$Ta | 170 | 97 | 14.4987 | -989379385.17 | 159654.5127 | +8532026.71 | 176.53 |
| ${}^{171}$Ta | 171 | 98 | 20.9494 | -984761877.86 | 160587.6274 | +8502316.92 | 175.50 |
| ${}^{172}$Ta | 172 | 99 | 27.3905 | -980187502.40 | 161520.7518 | +8460590.09 | 174.47 |
| ${}^{173}$Ta | 173 | 100 | 33.8220 | -975695994.32 | 162453.8857 | +8428524.64 | 173.47 |
| ${}^{174}$Ta | 174 | 101 | 40.2442 | -971234424.79 | 163387.0290 | +8386166.36 | 172.47 |
| ${}^{175}$Ta | 175 | 102 | 46.6570 | -966857686.29 | 164320.1816 | +8352539.96 | 171.48 |
| ${}^{176}$Ta | 176 | 103 | 53.0607 | -962496108.38 | 165253.3433 | +8308823.73 | 187.56 |
| ${}^{177}$Ta | 177 | 104 | 59.4554 | -958224919.21 | 166186.5140 | +8274176.14 | 20.11 |
| ${}^{178}$Ta | 178 | 105 | 65.8412 | -953964625.87 | 167119.6937 | +8231058.32 | 314.70 |
| ${}^{179}$Ta | 179 | 106 | 72.2181 | -949779188.53 | 168052.8821 | +8193766.21 | 8.80 |
| ${}^{180}$Ta | 180 | 107 | 78.5864 | -945602131.37 | 168986.0793 | +8149828.23 | 12.33 |
| ${}^{181}$Ta | 181 | 108 | 84.9461 | -941506704.22 | 169919.2850 | +8111985.41 | 9.35 |
| ${}^{182}$Ta | 182 | 109 | 91.2973 | -937394672.33 | 170852.4992 | +8065604.84 | 9.30 |
| ${}^{183}$Ta | 183 | 110 | 97.6401 | -933362051.54 | 171785.7218 | +8024934.87 | 9.33 |
| ${}^{184}$Ta | 184 | 111 | 103.9747 | -929309795.01 | 172718.9526 | +7977008.79 | 151.79 |
| ${}^{185}$Ta | 185 | 112 | 110.3012 | -925344917.99 | 173652.1916 | +7935552.77 | 82.19 |
| ${}^{186}$Ta | 186 | 113 | 116.6195 | -921349774.66 | 174585.4387 | +7886783.10 | 346.45 |
| ${}^{187}$Ta | 187 | 114 | 122.9299 | -917447978.46 | 175518.6937 | +7844801.90 | 320.92 |
| ${}^{188}$Ta | 188 | 115 | 129.2325 | -913511988.41 | 176451.9566 | +7795983.51 | 1143.84 |
| ${}^{189}$Ta | 189 | 116 | 135.5272 | -909665494.69 | 177385.2273 | +7753652.52 | 1137.77 |
| ${}^{190}$Ta | 190 | 117 | 141.8143 | -905782479.97 | 178318.5056 | +7704469.93 | 1131.76 |
| ${}^{191}$Ta | 191 | 118 | 148.0938 | -901989582.91 | 179251.7915 | +7661735.37 | 1686.12 |
| ${}^{192}$Ta | 192 | 119 | 154.3659 | -898151907.88 | 180185.0849 | +7612618.44 | 2234.66 |
| ${}^{193}$Ta | 193 | 120 | 160.6305 | -894420621.50 | 181118.3857 | +7570381.62 | 2223.06 |
| ${}^{194}$Ta | 194 | 121 | 166.8878 | -890623490.68 | 182051.6938 | +7520877.68 | 2768.30 |

### Tungsten (Z = 74)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{157}$W | 157 | 83 | -92.0621 | -1074908418.30 | 147545.9408 | +9034415.86 | 2732.85 |
| ${}^{158}$W | 158 | 84 | -85.4339 | -1068837791.59 | 148478.8779 | +9014479.75 | 2038.30 |
| ${}^{159}$W | 159 | 85 | -78.8175 | -1063011018.63 | 149411.8270 | +8979463.15 | 2025.51 |
| ${}^{160}$W | 160 | 86 | -72.2129 | -1057182618.48 | 150344.7878 | +8959550.87 | 1005.37 |
| ${}^{161}$W | 161 | 87 | -65.6197 | -1051585368.83 | 151277.7601 | +8921677.57 | 1335.68 |
| ${}^{162}$W | 162 | 88 | -59.0380 | -1045991957.99 | 152210.7437 | +8899818.03 | 117.03 |
| ${}^{163}$W | 163 | 89 | -52.4675 | -1040589404.67 | 153143.7386 | +8861135.09 | 384.89 |
| ${}^{164}$W | 164 | 90 | -45.9080 | -1035204504.56 | 154076.7446 | +8838967.16 | 63.33 |
| ${}^{165}$W | 165 | 91 | -39.3595 | -1029982792.77 | 155009.7615 | +8799402.70 | 167.61 |
| ${}^{166}$W | 166 | 92 | -32.8217 | -1024792920.69 | 155942.7891 | +8776048.23 | 61.22 |
| ${}^{167}$W | 167 | 93 | -26.2945 | -1019738990.75 | 156875.8274 | +8734746.44 | 120.26 |
| ${}^{168}$W | 168 | 94 | -19.7778 | -1014726787.80 | 157808.8761 | +8710728.06 | 84.74 |
| ${}^{169}$W | 169 | 95 | -13.2714 | -1009822837.65 | 158741.9351 | +8669274.25 | 98.08 |
| ${}^{170}$W | 170 | 96 | -6.7752 | -1004976209.18 | 159675.0043 | +8643332.55 | 83.35 |
| ${}^{171}$W | 171 | 97 | -0.2891 | -1000211094.26 | 160608.0836 | +8601429.86 | 175.49 |
| ${}^{172}$W | 172 | 98 | 6.1872 | -995514830.75 | 161541.1728 | +8574029.27 | 174.47 |
| ${}^{173}$W | 173 | 99 | 12.6536 | -990878130.93 | 162474.2718 | +8532100.25 | 173.46 |
| ${}^{174}$W | 174 | 100 | 19.1104 | -986317893.38 | 163407.3804 | +8502349.14 | 172.47 |
| ${}^{175}$W | 175 | 101 | 25.5576 | -981799403.97 | 164340.4986 | +8460037.58 | 171.48 |
| ${}^{176}$W | 176 | 102 | 31.9955 | -977361150.64 | 165273.6262 | +8428128.46 | 170.51 |
| ${}^{177}$W | 177 | 103 | 38.4240 | -972949030.43 | 166206.7630 | +8384713.90 | 169.54 |
| ${}^{178}$W | 178 | 104 | 44.8434 | -968623572.30 | 167139.9091 | +8351851.42 | 91.69 |
| ${}^{179}$W | 179 | 105 | 51.2538 | -964312109.10 | 168073.0641 | +8308418.02 | 87.42 |
| ${}^{180}$W | 180 | 106 | 57.6552 | -960088599.68 | 169006.2281 | +8274260.20 | 8.59 |
| ${}^{181}$W | 181 | 107 | 64.0478 | -955867115.74 | 169939.4010 | +8230104.14 | 8.59 |
| ${}^{182}$W | 182 | 108 | 70.4317 | -951737051.53 | 170872.5825 | +8194899.82 | 4.39 |
| ${}^{183}$W | 183 | 109 | 76.8070 | -947590753.07 | 171805.7727 | +8148934.01 | 4.36 |
| ${}^{184}$W | 184 | 110 | 83.1738 | -943531929.58 | 172738.9713 | +8110697.79 | 4.31 |
| ${}^{185}$W | 185 | 111 | 89.5322 | -939451622.86 | 173672.1783 | +8063226.31 | 4.29 |
| ${}^{186}$W | 186 | 112 | 95.8823 | -935471051.51 | 174605.3936 | +8024684.66 | 7.00 |
| ${}^{187}$W | 187 | 113 | 102.2242 | -931455103.62 | 175538.6171 | +7976616.64 | 6.96 |
| ${}^{188}$W | 188 | 114 | 108.5581 | -927540134.31 | 176471.8487 | +7936985.38 | 17.64 |
| ${}^{189}$W | 189 | 115 | 114.8839 | -923579142.87 | 177405.0882 | +7888530.05 | 1137.80 |
| ${}^{190}$W | 190 | 116 | 121.2019 | -919735194.40 | 178338.3357 | +7848706.62 | 200.00 |
| ${}^{191}$W | 191 | 117 | 127.5121 | -915828282.49 | 179271.5909 | +7799418.35 | 235.64 |
| ${}^{192}$W | 192 | 118 | 133.8146 | -912045569.27 | 180204.8539 | +7759909.07 | 1119.98 |
| ${}^{193}$W | 193 | 119 | 140.1094 | -908188228.33 | 181138.1244 | +7710350.63 | 1114.15 |
| ${}^{194}$W | 194 | 120 | 146.3968 | -904466050.55 | 182071.4025 | +7670546.71 | 1660.02 |
| ${}^{195}$W | 195 | 121 | 152.6767 | -900652515.76 | 183004.6880 | +7620707.06 | 1651.47 |
| ${}^{196}$W | 196 | 122 | 158.9493 | -896980973.61 | 183937.9808 | +7580636.43 | 2189.00 |
| ${}^{197}$W | 197 | 123 | 165.2146 | -893206057.38 | 184871.2809 | +7530747.60 | 2177.84 |

### Rhenium (Z = 75)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{159}$Re | 159 | 84 | -100.7622 | -1081298836.91 | 149432.9893 | +9049949.68 | 2056.81 |
| ${}^{160}$Re | 160 | 85 | -94.1183 | -1075318765.35 | 150365.9109 | +9016999.95 | 2012.73 |
| ${}^{161}$Re | 161 | 86 | -87.4863 | -1069342846.87 | 151298.8443 | +8997259.55 | 999.70 |
| ${}^{162}$Re | 162 | 87 | -80.8660 | -1063605125.86 | 152231.7894 | +8962095.88 | 1327.36 |
| ${}^{163}$Re | 163 | 88 | -74.2573 | -1057880037.25 | 153164.7461 | +8940329.74 | 122.09 |
| ${}^{164}$Re | 164 | 89 | -67.6598 | -1052348346.70 | 154097.7141 | +8905167.34 | 357.17 |
| ${}^{165}$Re | 165 | 90 | -61.0737 | -1046844575.24 | 155030.6933 | +8881774.40 | 153.53 |
| ${}^{166}$Re | 166 | 91 | -54.4985 | -1041506860.76 | 155963.6836 | +8845624.11 | 570.79 |
| ${}^{167}$Re | 167 | 92 | -47.9343 | -1036200226.35 | 156896.6848 | +8821774.27 | 257.54 |
| ${}^{168}$Re | 168 | 93 | -41.3808 | -1031041022.17 | 157829.6967 | +8785147.94 | 196.99 |
| ${}^{169}$Re | 169 | 94 | -34.8379 | -1025925203.91 | 158762.7193 | +8759620.97 | 72.23 |
| ${}^{170}$Re | 170 | 95 | -28.3055 | -1020930587.22 | 159695.7523 | +8720954.18 | 72.18 |
| ${}^{171}$Re | 171 | 96 | -21.7834 | -1015984687.25 | 160628.7957 | +8694532.35 | 175.48 |
| ${}^{172}$Re | 172 | 97 | -15.2716 | -1011137714.17 | 161561.8492 | +8655698.89 | 222.05 |
| ${}^{173}$Re | 173 | 98 | -8.7697 | -1006349282.22 | 162494.9128 | +8627834.97 | 173.46 |
| ${}^{174}$Re | 174 | 99 | -2.2778 | -1001639420.27 | 163427.9863 | +8588725.79 | 172.46 |
| ${}^{175}$Re | 175 | 100 | 4.2043 | -996994985.62 | 164361.0696 | +8559381.91 | 171.48 |
| ${}^{176}$Re | 176 | 101 | 10.6767 | -992411365.72 | 165294.1626 | +8519103.81 | 170.50 |
| ${}^{177}$Re | 177 | 102 | 17.1397 | -987897574.72 | 166227.2651 | +8488098.65 | 169.54 |
| ${}^{178}$Re | 178 | 103 | 23.5931 | -983427963.30 | 167160.3770 | +8446413.58 | 168.59 |
| ${}^{179}$Re | 179 | 104 | 30.0373 | -979034075.22 | 168093.4983 | +8414606.54 | 147.81 |
| ${}^{180}$Re | 180 | 105 | 36.4724 | -974671950.70 | 169026.6287 | +8373114.13 | 127.62 |
| ${}^{181}$Re | 181 | 106 | 42.8983 | -970389432.69 | 169959.7681 | +8340671.11 | 74.45 |
| ${}^{182}$Re | 182 | 107 | 49.3153 | -966123776.90 | 170892.9166 | +8298218.32 | 601.72 |
| ${}^{183}$Re | 183 | 108 | 55.7235 | -961942319.58 | 171826.0738 | +8264770.76 | 47.14 |
| ${}^{184}$Re | 184 | 109 | 62.1229 | -957758657.52 | 172759.2398 | +8220244.01 | 24.95 |
| ${}^{185}$Re | 185 | 110 | 68.5137 | -953654851.93 | 173692.4144 | +8183207.89 | 4.75 |
| ${}^{186}$Re | 186 | 111 | 74.8961 | -949548521.59 | 174625.5975 | +8137941.82 | 4.73 |
| ${}^{187}$Re | 187 | 112 | 81.2700 | -945525032.64 | 175558.7890 | +8100045.45 | 4.23 |
| ${}^{188}$Re | 188 | 113 | 87.6355 | -941488482.19 | 176491.9889 | +8054027.52 | 4.21 |
| ${}^{189}$Re | 189 | 114 | 93.9929 | -937537181.43 | 177425.1969 | +8015198.35 | 46.53 |
| ${}^{190}$Re | 190 | 115 | 100.3422 | -933568322.22 | 178358.4130 | +7969086.79 | 27.52 |
| ${}^{191}$Re | 191 | 116 | 106.6835 | -929688414.90 | 179291.6372 | +7930097.00 | 57.70 |
| ${}^{192}$Re | 192 | 117 | 113.0169 | -925774055.86 | 180224.8692 | +7882940.18 | 395.90 |
| ${}^{193}$Re | 193 | 118 | 119.3424 | -921963747.65 | 181158.1091 | +7844191.39 | 217.65 |
| ${}^{194}$Re | 194 | 119 | 125.6602 | -918101772.88 | 182091.3567 | +7796881.41 | 1108.41 |
| ${}^{195}$Re | 195 | 120 | 131.9704 | -914343593.43 | 183024.6120 | +7757155.56 | 1651.51 |
| ${}^{196}$Re | 196 | 121 | 138.2730 | -910540876.64 | 183957.8748 | +7709593.37 | 1643.06 |
| ${}^{197}$Re | 197 | 122 | 144.5682 | -906836516.64 | 184891.1450 | +7669099.27 | 1634.70 |
| ${}^{198}$Re | 198 | 123 | 150.8560 | -903078612.37 | 185824.4226 | +7621675.32 | 2166.87 |
| ${}^{199}$Re | 199 | 124 | 157.1365 | -899410093.63 | 186757.7075 | +7580744.10 | 2155.95 |

### Osmium (Z = 76)

_43 of 43 isotopes with a framework prediction; 43 of 43 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{161}$Os | 161 | 85 | -109.6138 | -1087679501.66 | 151320.1895 | +9067962.90 | 2664.78 |
| ${}^{162}$Os | 162 | 86 | -102.9545 | -1081539818.33 | 152253.0955 | +9050119.84 | 1987.85 |
| ${}^{163}$Os | 163 | 87 | -96.3069 | -1075680793.58 | 153186.0134 | +9016178.84 | 1975.67 |
| ${}^{164}$Os | 164 | 88 | -89.6710 | -1069801246.00 | 154118.9430 | +8997598.63 | 981.39 |
| ${}^{165}$Os | 165 | 89 | -83.0467 | -1064173565.09 | 155051.8840 | +8961155.34 | 1303.21 |
| ${}^{166}$Os | 166 | 90 | -76.4337 | -1058533459.30 | 155984.8365 | +8940644.32 | 116.21 |
| ${}^{167}$Os | 167 | 91 | -69.8319 | -1053106095.84 | 156917.8001 | +8903470.48 | 520.09 |
| ${}^{168}$Os | 168 | 92 | -63.2411 | -1047674542.88 | 157850.7748 | +8882470.36 | 63.29 |
| ${}^{169}$Os | 169 | 93 | -56.6613 | -1042432825.65 | 158783.7603 | +8844043.66 | 164.81 |
| ${}^{170}$Os | 170 | 94 | -50.0922 | -1037199248.47 | 159716.7566 | +8821905.44 | 61.64 |
| ${}^{171}$Os | 171 | 95 | -43.5337 | -1032127375.00 | 160649.7636 | +8782157.52 | 114.58 |
| ${}^{172}$Os | 172 | 96 | -36.9857 | -1027074859.93 | 161582.7810 | +8759152.37 | 79.69 |
| ${}^{173}$Os | 173 | 97 | -30.4480 | -1022154965.49 | 162515.8087 | +8719247.19 | 92.85 |
| ${}^{174}$Os | 174 | 98 | -23.9205 | -1017271757.46 | 163448.8466 | +8694570.03 | 63.28 |
| ${}^{175}$Os | 175 | 99 | -17.4030 | -1012492041.21 | 164381.8946 | +8655089.85 | 72.25 |
| ${}^{176}$Os | 176 | 100 | -10.8955 | -1007764604.96 | 165314.9525 | +8627908.72 | 66.80 |
| ${}^{177}$Os | 177 | 101 | -4.3978 | -1003116502.74 | 166248.0202 | +8587628.47 | 88.65 |
| ${}^{178}$Os | 178 | 102 | 2.0903 | -998528776.46 | 167181.0976 | +8558583.14 | 82.24 |
| ${}^{179}$Os | 179 | 103 | 8.5688 | -994000826.67 | 168114.1845 | +8517141.79 | 93.01 |
| ${}^{180}$Os | 180 | 104 | 15.0379 | -989540592.32 | 169047.2808 | +8487408.80 | 93.79 |
| ${}^{181}$Os | 181 | 105 | 21.4976 | -985122755.66 | 169980.3865 | +8445242.09 | 150.32 |
| ${}^{182}$Os | 182 | 106 | 27.9482 | -980780136.51 | 170913.5013 | +8414691.96 | 128.30 |
| ${}^{183}$Os | 183 | 107 | 34.3897 | -976465675.21 | 171846.6253 | +8372667.98 | 292.03 |
| ${}^{184}$Os | 184 | 108 | 40.8222 | -972228209.60 | 172779.7582 | +8340181.57 | 4.84 |
| ${}^{185}$Os | 185 | 109 | 47.2459 | -968002320.07 | 173712.8999 | +8296184.86 | 4.83 |
| ${}^{186}$Os | 186 | 110 | 53.6608 | -963860057.09 | 174646.0504 | +8262263.24 | 4.39 |
| ${}^{187}$Os | 187 | 111 | 60.0671 | -959716149.56 | 175579.2095 | +8217318.97 | 4.23 |
| ${}^{188}$Os | 188 | 112 | 66.4649 | -955663071.06 | 176512.3772 | +8182687.79 | 4.19 |
| ${}^{189}$Os | 189 | 113 | 72.8542 | -951592107.99 | 177445.5532 | +8136621.73 | 3.78 |
| ${}^{190}$Os | 190 | 114 | 79.2353 | -947623437.70 | 178378.7377 | +8101751.28 | 3.67 |
| ${}^{191}$Os | 191 | 115 | 85.6080 | -943625458.00 | 179311.9303 | +8055767.63 | 3.70 |
| ${}^{192}$Os | 192 | 116 | 91.9727 | -939734169.51 | 180245.1310 | +8020454.86 | 12.94 |
| ${}^{193}$Os | 193 | 117 | 98.3293 | -935803805.63 | 181178.3398 | +7974477.65 | 12.90 |
| ${}^{194}$Os | 194 | 118 | 104.6780 | -931974797.96 | 182111.5566 | +7937547.59 | 13.30 |
| ${}^{195}$Os | 195 | 119 | 111.0189 | -928094728.31 | 183044.7811 | +7890138.25 | 307.74 |
| ${}^{196}$Os | 196 | 120 | 117.3520 | -924327959.65 | 183978.0135 | +7852582.44 | 219.42 |
| ${}^{197}$Os | 197 | 121 | 123.6774 | -920500930.05 | 184911.2535 | +7804667.27 | 1091.52 |
| ${}^{198}$Os | 198 | 122 | 129.9953 | -916788106.59 | 185844.5010 | +7766669.22 | 1086.00 |
| ${}^{199}$Os | 199 | 123 | 136.3057 | -913010783.87 | 186777.7561 | +7719030.90 | 1080.52 |
| ${}^{200}$Os | 200 | 124 | 142.6086 | -909362752.31 | 187711.0185 | +7680617.58 | 1610.16 |
| ${}^{201}$Os | 201 | 125 | 148.9043 | -905616324.27 | 188644.2883 | +7631917.36 | 1602.12 |
| ${}^{202}$Os | 202 | 126 | 155.1927 | -901992483.68 | 189577.5652 | +7591242.22 | 2123.90 |
| ${}^{203}$Os | 203 | 127 | 161.4740 | -898203407.76 | 190510.8494 | +7535282.29 | 2113.38 |

### Iridium (Z = 77)

_43 of 43 isotopes with a framework prediction; 43 of 43 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{163}$Ir | 163 | 86 | -118.6164 | -1094092090.98 | 153207.5406 | +9084688.40 | 2631.99 |
| ${}^{164}$Ir | 164 | 87 | -111.9416 | -1088073640.26 | 154140.4312 | +9052788.56 | 2067.17 |
| ${}^{165}$Ir | 165 | 88 | -105.2786 | -1082054008.02 | 155073.3336 | +9034078.30 | 1030.38 |
| ${}^{166}$Ir | 166 | 89 | -98.6272 | -1076279346.56 | 156006.2476 | +8999996.41 | 1295.29 |
| ${}^{167}$Ir | 167 | 90 | -91.9873 | -1070502337.14 | 156939.1732 | +8979737.65 | 117.94 |
| ${}^{168}$Ir | 168 | 91 | -85.3588 | -1064940945.30 | 157872.1101 | +8945778.43 | 352.88 |
| ${}^{169}$Ir | 169 | 92 | -78.7415 | -1059386964.71 | 158805.0582 | +8924043.38 | 148.07 |
| ${}^{170}$Ir | 170 | 93 | -72.1352 | -1054033460.39 | 159738.0173 | +8887731.61 | 641.27 |
| ${}^{171}$Ir | 171 | 94 | -65.5398 | -1048679019.36 | 160670.9874 | +8865476.64 | 241.53 |
| ${}^{172}$Ir | 172 | 95 | -58.9552 | -1043496329.68 | 161603.9681 | +8829297.30 | 202.27 |
| ${}^{173}$Ir | 173 | 96 | -52.3811 | -1038336081.88 | 162536.9595 | +8805634.08 | 65.42 |
| ${}^{174}$Ir | 174 | 97 | -45.8175 | -1033322938.40 | 163469.9613 | +8767543.03 | 69.24 |
| ${}^{175}$Ir | 175 | 98 | -39.2643 | -1028336672.72 | 164402.9735 | +8742893.05 | 75.99 |
| ${}^{176}$Ir | 176 | 99 | -32.7212 | -1023469636.81 | 165335.9959 | +8705530.73 | 49.32 |
| ${}^{177}$Ir | 177 | 100 | -26.1882 | -1018646858.00 | 166269.0283 | +8678919.94 | 119.87 |
| ${}^{178}$Ir | 178 | 101 | -19.6651 | -1013920169.76 | 167202.0706 | +8640749.95 | 113.53 |
| ${}^{179}$Ir | 179 | 102 | -13.1519 | -1009244910.98 | 168135.1228 | +8612870.09 | 58.61 |
| ${}^{180}$Ir | 180 | 103 | -6.6483 | -1004647289.04 | 169068.1846 | +8573735.38 | 129.48 |
| ${}^{181}$Ir | 181 | 104 | -0.1543 | -1000107119.20 | 170001.2560 | +8544601.41 | 31.12 |
| ${}^{182}$Ir | 182 | 105 | 6.3303 | -995627598.89 | 170934.3369 | +8504556.18 | 123.70 |
| ${}^{183}$Ir | 183 | 106 | 12.8056 | -991211063.82 | 171867.4270 | +8474245.44 | 144.77 |
| ${}^{184}$Ir | 184 | 107 | 19.2717 | -986840728.67 | 172800.5264 | +8434067.23 | 163.08 |
| ${}^{185}$Ir | 185 | 108 | 25.7286 | -982536598.30 | 173733.6348 | +8402079.00 | 162.20 |
| ${}^{186}$Ir | 186 | 109 | 32.1766 | -978261923.98 | 174666.7523 | +8359496.15 | 95.40 |
| ${}^{187}$Ir | 187 | 110 | 38.6158 | -974059794.03 | 175599.8785 | +8326338.18 | 160.46 |
| ${}^{188}$Ir | 188 | 111 | 45.0461 | -969879123.33 | 176533.0136 | +8284475.43 | 53.82 |
| ${}^{189}$Ir | 189 | 112 | 51.4679 | -965772254.37 | 177466.1573 | +8250604.39 | 71.44 |
| ${}^{190}$Ir | 190 | 113 | 57.8810 | -961669804.90 | 178399.3096 | +8206877.93 | 7.74 |
| ${}^{191}$Ir | 191 | 114 | 64.2857 | -957653530.53 | 179332.4703 | +8173016.54 | 7.36 |
| ${}^{192}$Ir | 192 | 115 | 70.6821 | -953629415.97 | 180265.6393 | +8129246.10 | 7.35 |
| ${}^{193}$Ir | 193 | 116 | 77.0703 | -949695013.76 | 181198.8166 | +8094803.10 | 7.38 |
| ${}^{194}$Ir | 194 | 117 | 83.4502 | -945745538.51 | 182132.0020 | +8051246.55 | 7.37 |
| ${}^{195}$Ir | 195 | 118 | 89.8222 | -941876164.62 | 183065.1955 | +8014648.73 | 7.34 |
| ${}^{196}$Ir | 196 | 119 | 96.1861 | -937991357.02 | 183998.3970 | +7970642.02 | 210.44 |
| ${}^{197}$Ir | 197 | 120 | 102.5422 | -934186496.09 | 184931.6063 | +7933088.75 | 109.60 |
| ${}^{198}$Ir | 198 | 121 | 108.8906 | -930359324.57 | 185864.8234 | +7888401.11 | 1086.01 |
| ${}^{199}$Ir | 199 | 122 | 115.2312 | -926620680.26 | 186798.0482 | +7850960.75 | 221.50 |
| ${}^{200}$Ir | 200 | 123 | 121.5643 | -922845728.04 | 187731.2805 | +7805727.53 | 1050.12 |
| ${}^{201}$Ir | 201 | 124 | 127.8898 | -919152769.76 | 188664.5204 | +7766902.28 | 1069.77 |
| ${}^{202}$Ir | 202 | 125 | 134.2079 | -915417486.53 | 189597.7677 | +7720628.70 | 1594.20 |
| ${}^{203}$Ir | 203 | 126 | 140.5187 | -911764143.11 | 190531.0224 | +7679805.81 | 2113.46 |
| ${}^{204}$Ir | 204 | 127 | 146.8222 | -907999913.62 | 191464.2843 | +7626006.24 | 2103.05 |
| ${}^{205}$Ir | 205 | 128 | 153.1185 | -904302410.48 | 192397.5534 | +7577151.23 | 2619.59 |

### Platinum (Z = 78)

_44 of 44 isotopes with a framework prediction; 44 of 44 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{165}$Pt | 165 | 87 | -127.7693 | -1100526994.53 | 155095.0420 | +9101287.87 | 2600.01 |
| ${}^{166}$Pt | 166 | 88 | -121.0791 | -1094321998.78 | 156027.9172 | +9084522.19 | 1939.82 |
| ${}^{167}$Pt | 167 | 89 | -114.4006 | -1088437103.99 | 156960.8042 | +9051862.26 | 1970.15 |
| ${}^{168}$Pt | 168 | 90 | -107.7339 | -1082493463.23 | 157893.7028 | +9034403.51 | 958.16 |
| ${}^{169}$Pt | 169 | 91 | -101.0786 | -1076836842.81 | 158826.6129 | +8999259.04 | 1272.29 |
| ${}^{170}$Pt | 170 | 92 | -94.4346 | -1071142515.38 | 159759.5344 | +8979768.95 | 115.24 |
| ${}^{171}$Pt | 171 | 93 | -87.8018 | -1065688496.19 | 160692.4670 | +8943677.43 | 508.27 |
| ${}^{172}$Pt | 172 | 94 | -81.1800 | -1060206933.92 | 161625.4107 | +8923647.16 | 64.77 |
| ${}^{173}$Pt | 173 | 95 | -74.5692 | -1054941291.61 | 162558.3652 | +8886320.06 | 393.67 |
| ${}^{174}$Pt | 174 | 96 | -67.9690 | -1049659409.47 | 163491.3305 | +8865367.39 | 63.79 |
| ${}^{175}$Pt | 175 | 97 | -61.3795 | -1044569412.73 | 164424.3064 | +8826212.38 | 114.20 |
| ${}^{176}$Pt | 176 | 98 | -54.8004 | -1039468409.96 | 165357.2927 | +8805008.48 | 77.55 |
| ${}^{177}$Pt | 177 | 99 | -48.2317 | -1034525904.84 | 166290.2894 | +8767040.24 | 90.92 |
| ${}^{178}$Pt | 178 | 100 | -41.6731 | -1029604349.47 | 167223.2963 | +8742889.30 | 61.12 |
| ${}^{179}$Pt | 179 | 101 | -35.1246 | -1024805344.31 | 168156.3132 | +8704809.45 | 47.85 |
| ${}^{180}$Pt | 180 | 102 | -28.5861 | -1020042916.15 | 169089.3401 | +8678590.84 | 59.96 |
| ${}^{181}$Pt | 181 | 103 | -22.0574 | -1015378831.30 | 170022.3768 | +8639494.74 | 81.20 |
| ${}^{182}$Pt | 182 | 104 | -15.5383 | -1010759660.48 | 170955.4232 | +8611806.66 | 77.25 |
| ${}^{183}$Pt | 183 | 105 | -9.0288 | -1006219039.54 | 171888.4791 | +8571562.94 | 83.41 |
| ${}^{184}$Pt | 184 | 106 | -2.5288 | -1001730336.35 | 172821.5445 | +8543315.42 | 86.04 |
| ${}^{185}$Pt | 185 | 107 | 3.9619 | -997302707.03 | 173754.6192 | +8502527.80 | 149.93 |
| ${}^{186}$Pt | 186 | 108 | 10.4434 | -992934582.45 | 174687.7031 | +8472831.89 | 125.53 |
| ${}^{187}$Pt | 187 | 109 | 16.9158 | -988608855.56 | 175620.7961 | +8429866.46 | 138.19 |
| ${}^{188}$Pt | 188 | 110 | 23.3792 | -984353399.07 | 176553.8982 | +8400741.56 | 30.29 |
| ${}^{189}$Pt | 189 | 111 | 29.8338 | -980123087.59 | 177487.0091 | +8357726.34 | 57.32 |
| ${}^{190}$Pt | 190 | 112 | 36.2795 | -975971189.27 | 178420.1287 | +8327686.15 | 3.71 |
| ${}^{191}$Pt | 191 | 113 | 42.7166 | -971828348.07 | 179353.2571 | +8284148.24 | 23.20 |
| ${}^{192}$Pt | 192 | 114 | 49.1451 | -967772824.41 | 180286.3940 | +8253508.26 | 14.37 |
| ${}^{193}$Pt | 193 | 115 | 55.5652 | -963711863.62 | 181219.5394 | +8209776.02 | 7.56 |
| ${}^{194}$Pt | 194 | 116 | 61.9768 | -959744128.93 | 182152.6931 | +8178200.01 | 2.74 |
| ${}^{195}$Pt | 195 | 117 | 68.3803 | -955760339.62 | 183085.8551 | +8134521.73 | 2.77 |
| ${}^{196}$Pt | 196 | 118 | 74.7755 | -951869514.29 | 184019.0253 | +8101368.78 | 2.79 |
| ${}^{197}$Pt | 197 | 119 | 81.1627 | -947954162.79 | 184952.2035 | +8057193.44 | 2.92 |
| ${}^{198}$Pt | 198 | 120 | 87.5419 | -944134153.92 | 185885.3897 | +8022850.62 | 11.39 |
| ${}^{199}$Pt | 199 | 121 | 93.9132 | -940279975.11 | 186818.5838 | +7978020.96 | 11.64 |
| ${}^{200}$Pt | 200 | 122 | 100.2767 | -936527289.53 | 187751.7858 | +7943021.15 | 107.96 |
| ${}^{201}$Pt | 201 | 123 | 106.6325 | -932726199.08 | 188684.9954 | +7897272.02 | 267.64 |
| ${}^{202}$Pt | 202 | 124 | 112.9807 | -929035585.25 | 189618.2126 | +7861713.32 | 133.68 |
| ${}^{203}$Pt | 203 | 125 | 119.3213 | -925284118.49 | 190551.4374 | +7815173.47 | 1059.22 |
| ${}^{204}$Pt | 204 | 126 | 125.6545 | -921624431.84 | 191484.6696 | +7775983.18 | 1054.02 |
| ${}^{205}$Pt | 205 | 127 | 131.9804 | -917839888.38 | 192417.9092 | +7721856.67 | 1570.84 |
| ${}^{206}$Pt | 206 | 128 | 138.2989 | -914149118.09 | 193351.1561 | +7674704.64 | 1563.18 |
| ${}^{207}$Pt | 207 | 129 | 144.6102 | -910401411.13 | 194284.4102 | +7620098.09 | 2072.51 |
| ${}^{208}$Pt | 208 | 130 | 150.9145 | -906741611.80 | 195217.6714 | +7573656.60 | 2062.51 |

### Gold (Z = 79)

_43 of 43 isotopes with a framework prediction; 43 of 43 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{168}$Au | 168 | 89 | -130.3662 | -1100935155.56 | 157915.5528 | +9086723.21 | 2553.53 |
| ${}^{169}$Au | 169 | 90 | -123.6725 | -1094840557.26 | 158848.4245 | +9069387.32 | 1893.51 |
| ${}^{170}$Au | 170 | 91 | -116.9903 | -1089026958.54 | 159781.3078 | +9037013.65 | 1270.62 |
| ${}^{171}$Au | 171 | 92 | -110.3197 | -1083200322.18 | 160714.2025 | +9017401.89 | 130.04 |
| ${}^{172}$Au | 172 | 93 | -103.6603 | -1077602868.74 | 161647.1086 | +8984843.21 | 350.53 |
| ${}^{173}$Au | 173 | 94 | -97.0121 | -1072001387.38 | 162580.0258 | +8963739.16 | 141.39 |
| ${}^{174}$Au | 174 | 95 | -90.3750 | -1066614892.92 | 163512.9541 | +8928701.37 | 626.49 |
| ${}^{175}$Au | 175 | 96 | -83.7487 | -1061216259.06 | 164445.8932 | +8907249.36 | 236.59 |
| ${}^{176}$Au | 176 | 97 | -77.1331 | -1056004460.05 | 165378.8431 | +8872391.54 | 202.44 |
| ${}^{177}$Au | 177 | 98 | -70.5282 | -1050799494.95 | 166311.8036 | +8849664.57 | 60.46 |
| ${}^{178}$Au | 178 | 99 | -63.9337 | -1045758683.83 | 167244.7745 | +8813457.20 | 61.81 |
| ${}^{179}$Au | 179 | 100 | -57.3495 | -1040732659.54 | 168177.7558 | +8789383.89 | 70.15 |
| ${}^{180}$Au | 180 | 101 | -50.7755 | -1035841789.28 | 169110.7472 | +8753311.85 | 28.38 |
| ${}^{181}$Au | 181 | 102 | -44.2116 | -1030982781.92 | 170043.7487 | +8727322.46 | 118.50 |
| ${}^{182}$Au | 182 | 103 | -37.6577 | -1026233530.05 | 170976.7602 | +8690889.72 | 110.69 |
| ${}^{183}$Au | 183 | 104 | -31.1135 | -1021525330.43 | 171909.7815 | +8663521.64 | 55.29 |
| ${}^{184}$Au | 184 | 105 | -24.5791 | -1016908675.24 | 172842.8124 | +8626146.18 | 129.98 |
| ${}^{185}$Au | 185 | 106 | -18.0542 | -1012338432.75 | 173775.8530 | +8597497.24 | 15.14 |
| ${}^{186}$Au | 186 | 107 | -11.5387 | -1007843214.32 | 174708.9030 | +8559413.18 | 121.04 |
| ${}^{187}$Au | 187 | 108 | -5.0326 | -1003399149.83 | 175641.9623 | +8530228.80 | 129.18 |
| ${}^{188}$Au | 188 | 109 | 1.4642 | -999015961.55 | 176575.0308 | +8490052.08 | 15.43 |
| ${}^{189}$Au | 189 | 110 | 7.9520 | -994688964.28 | 177508.1085 | +8461055.48 | 114.09 |
| ${}^{190}$Au | 190 | 111 | 14.4307 | -990408789.23 | 178441.1952 | +8421250.09 | 19.48 |
| ${}^{191}$Au | 191 | 112 | 20.9006 | -986191602.80 | 179374.2907 | +8391621.44 | 27.69 |
| ${}^{192}$Au | 192 | 113 | 27.3617 | -982006722.50 | 180307.3951 | +8351127.82 | 88.51 |
| ${}^{193}$Au | 193 | 114 | 33.8140 | -977890128.31 | 181240.5081 | +8320405.62 | 48.25 |
| ${}^{194}$Au | 194 | 115 | 40.2578 | -973794602.26 | 182173.6298 | +8279859.95 | 11.72 |
| ${}^{195}$Au | 195 | 116 | 46.6932 | -969771408.03 | 183106.7599 | +8248371.44 | 6.16 |
| ${}^{196}$Au | 196 | 117 | 53.1201 | -965757945.68 | 184039.8983 | +8207399.68 | 16.22 |
| ${}^{197}$Au | 197 | 118 | 59.5388 | -961819056.92 | 184973.0451 | +8174744.03 | 2.95 |
| ${}^{198}$Au | 198 | 119 | 65.9492 | -957884047.16 | 185906.2001 | +8133934.27 | 2.92 |
| ${}^{199}$Au | 199 | 120 | 72.3516 | -954018125.51 | 186839.3631 | +8099409.46 | 2.92 |
| ${}^{200}$Au | 200 | 121 | 78.7460 | -950151266.09 | 187772.5342 | +8057877.22 | 143.43 |
| ${}^{201}$Au | 201 | 122 | 85.1324 | -946354023.40 | 188705.7131 | +8022262.80 | 17.19 |
| ${}^{202}$Au | 202 | 123 | 91.5111 | -942552595.68 | 189638.8999 | +7980569.01 | 123.78 |
| ${}^{203}$Au | 203 | 124 | 97.8820 | -938816716.26 | 190572.0944 | +7943796.24 | 16.30 |
| ${}^{204}$Au | 204 | 125 | 104.2452 | -935052610.67 | 191505.2966 | +7899236.99 | 1054.03 |
| ${}^{205}$Au | 205 | 126 | 110.6009 | -931359187.28 | 192438.5063 | +7860077.65 | 1048.88 |
| ${}^{206}$Au | 206 | 127 | 116.9492 | -927587445.51 | 193371.7235 | +7807893.09 | 1563.22 |
| ${}^{207}$Au | 207 | 128 | 123.2900 | -923874755.27 | 194304.9481 | +7760591.43 | 1555.64 |
| ${}^{208}$Au | 208 | 129 | 129.6235 | -920134552.47 | 195238.1800 | +7707645.57 | 1548.12 |
| ${}^{209}$Au | 209 | 130 | 135.9498 | -916455473.67 | 196171.4191 | +7660679.76 | 2052.66 |
| ${}^{210}$Au | 210 | 131 | 142.2690 | -912741970.47 | 197104.6654 | +7607866.09 | 2042.83 |

### Mercury (Z = 80)

_47 of 47 isotopes with a framework prediction; 47 of 47 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{170}$Hg | 170 | 90 | -139.8024 | -1107204690.00 | 159803.3375 | +9118019.38 | 1905.82 |
| ${}^{171}$Hg | 171 | 91 | -133.0934 | -1101265143.35 | 160736.1939 | +9086404.71 | 1923.94 |
| ${}^{172}$Hg | 172 | 92 | -126.3960 | -1095268049.01 | 161669.0619 | +9069869.00 | 936.62 |
| ${}^{173}$Hg | 173 | 93 | -119.7100 | -1089574790.94 | 162601.9414 | +9036056.44 | 1242.80 |
| ${}^{174}$Hg | 174 | 94 | -113.0353 | -1083825331.21 | 163534.8321 | +9017517.43 | 118.53 |
| ${}^{175}$Hg | 175 | 95 | -106.3718 | -1078337702.38 | 164467.7340 | +8982846.09 | 497.44 |
| ${}^{176}$Hg | 176 | 96 | -99.7193 | -1072801169.70 | 165400.6470 | +8963940.73 | 67.82 |
| ${}^{177}$Hg | 177 | 97 | -93.0777 | -1067505747.72 | 166333.5708 | +8928031.25 | 513.89 |
| ${}^{178}$Hg | 178 | 98 | -86.4468 | -1062173053.26 | 167266.5053 | +8908097.17 | 64.88 |
| ${}^{179}$Hg | 179 | 99 | -79.8265 | -1057055145.95 | 168199.4504 | +8870766.74 | 168.67 |
| ${}^{180}$Hg | 180 | 100 | -73.2166 | -1051908287.17 | 169132.4060 | +8850160.69 | 75.42 |
| ${}^{181}$Hg | 181 | 101 | -66.6171 | -1046947119.98 | 170065.3719 | +8812446.62 | 91.24 |
| ${}^{182}$Hg | 182 | 102 | -60.0278 | -1041978382.63 | 170998.3480 | +8790115.58 | 57.76 |
| ${}^{183}$Hg | 183 | 103 | -53.4485 | -1037161726.07 | 171931.3341 | +8752177.74 | 41.56 |
| ${}^{184}$Hg | 184 | 104 | -46.8792 | -1032355488.42 | 172864.3302 | +8728321.32 | 55.63 |
| ${}^{185}$Hg | 185 | 105 | -40.3197 | -1027677093.14 | 173797.3362 | +8688965.00 | 79.15 |
| ${}^{186}$Hg | 186 | 106 | -33.7699 | -1023016305.82 | 174730.3518 | +8664740.88 | 67.25 |
| ${}^{187}$Hg | 187 | 107 | -27.2297 | -1018462461.36 | 175663.3770 | +8624753.50 | 73.86 |
| ${}^{188}$Hg | 188 | 108 | -20.6989 | -1013938492.67 | 176596.4116 | +8599648.97 | 38.76 |
| ${}^{189}$Hg | 189 | 109 | -14.1775 | -1009499052.59 | 177529.4557 | +8559668.30 | 179.25 |
| ${}^{190}$Hg | 190 | 110 | -7.6653 | -1005102280.30 | 178462.5089 | +8533362.01 | 89.89 |
| ${}^{191}$Hg | 191 | 111 | -1.1623 | -1000769906.57 | 179395.5713 | +8493077.88 | 125.25 |
| ${}^{192}$Hg | 192 | 112 | 5.3318 | -996490217.92 | 180328.6427 | +8465662.46 | 86.89 |
| ${}^{193}$Hg | 193 | 113 | 11.8169 | -992257502.09 | 181261.7229 | +8425289.79 | 86.26 |
| ${}^{194}$Hg | 194 | 114 | 18.2932 | -988085938.73 | 182194.8120 | +8396941.63 | 15.98 |
| ${}^{195}$Hg | 195 | 115 | 24.7609 | -983945836.73 | 183127.9098 | +8356203.57 | 127.42 |
| ${}^{196}$Hg | 196 | 116 | 31.2199 | -979873930.19 | 184061.0162 | +8326883.72 | 16.14 |
| ${}^{197}$Hg | 197 | 117 | 37.6704 | -975821324.91 | 184994.1311 | +8286376.15 | 17.47 |
| ${}^{198}$Hg | 198 | 118 | 44.1126 | -971839824.96 | 185927.2544 | +8255617.68 | 2.48 |
| ${}^{199}$Hg | 199 | 119 | 50.5464 | -967869320.91 | 186860.3860 | +8215299.68 | 2.83 |
| ${}^{200}$Hg | 200 | 120 | 56.9720 | -963968646.31 | 187793.5258 | +8182820.03 | 2.84 |
| ${}^{201}$Hg | 201 | 121 | 63.3895 | -960067311.05 | 188726.6737 | +8141024.45 | 3.80 |
| ${}^{202}$Hg | 202 | 122 | 69.7990 | -956243346.11 | 189659.8296 | +8107849.81 | 3.75 |
| ${}^{203}$Hg | 203 | 123 | 76.2006 | -952409103.70 | 190592.9935 | +8065666.07 | 8.62 |
| ${}^{204}$Hg | 204 | 124 | 82.5943 | -948656173.11 | 191526.1652 | +8031880.58 | 2.62 |
| ${}^{205}$Hg | 205 | 125 | 88.9803 | -944880648.81 | 192459.3446 | +7988839.41 | 19.14 |
| ${}^{206}$Hg | 206 | 126 | 95.3586 | -941174788.25 | 193392.5318 | +7951828.07 | 106.53 |
| ${}^{207}$Hg | 207 | 127 | 101.7293 | -937384351.48 | 194325.7265 | +7898923.16 | 154.60 |
| ${}^{208}$Hg | 208 | 128 | 108.0925 | -933665705.69 | 195258.9287 | +7852999.23 | 158.66 |
| ${}^{209}$Hg | 209 | 129 | 114.4483 | -929911735.49 | 196192.1383 | +7800132.94 | 770.37 |
| ${}^{210}$Hg | 210 | 130 | 120.7968 | -926244032.56 | 197125.3552 | +7754744.61 | 1023.84 |
| ${}^{211}$Hg | 211 | 131 | 127.1380 | -922521569.73 | 198058.5795 | +7701619.99 | 1018.96 |
| ${}^{212}$Hg | 212 | 132 | 133.4720 | -918888809.66 | 198991.8108 | +7656687.83 | 1518.84 |
| ${}^{213}$Hg | 213 | 133 | 139.7990 | -915191474.03 | 199925.0493 | +7603227.15 | 1511.67 |
| ${}^{214}$Hg | 214 | 134 | 146.1189 | -911600400.94 | 200858.2948 | +7558439.34 | 2004.55 |
| ${}^{215}$Hg | 215 | 135 | 152.4318 | -907935941.27 | 201791.5473 | +7505206.25 | 1995.18 |
| ${}^{216}$Hg | 216 | 136 | 158.7379 | -904372435.65 | 202724.8066 | +7460156.04 | 1985.90 |

### Thallium (Z = 81)

_43 of 43 isotopes with a framework prediction; 43 of 43 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{176}$Tl | 176 | 95 | -122.5590 | -1090342963.30 | 165422.7043 | +9022357.83 | 506.62 |
| ${}^{177}$Tl | 177 | 96 | -115.8802 | -1084671055.50 | 166355.5910 | +9003849.56 | 131.18 |
| ${}^{178}$Tl | 178 | 97 | -109.2125 | -1079260201.91 | 167288.4886 | +8969480.57 | 617.99 |
| ${}^{179}$Tl | 179 | 98 | -102.5556 | -1073798747.01 | 168221.3972 | +8949976.67 | 231.83 |
| ${}^{180}$Tl | 180 | 99 | -95.9094 | -1068562654.51 | 169154.3164 | +8915496.83 | 417.01 |
| ${}^{181}$Tl | 181 | 100 | -89.2738 | -1063299609.90 | 170087.2462 | +8895149.49 | 53.99 |
| ${}^{182}$Tl | 182 | 101 | -82.6487 | -1058246882.15 | 171020.1865 | +8857947.46 | 70.64 |
| ${}^{183}$Tl | 183 | 102 | -76.0338 | -1053160540.64 | 171953.1371 | +8837379.77 | 54.74 |
| ${}^{184}$Tl | 184 | 103 | -69.4292 | -1048260455.17 | 172886.0979 | +8799647.05 | 58.41 |
| ${}^{185}$Tl | 185 | 104 | -62.8347 | -1043346762.12 | 173819.0688 | +8777475.13 | 119.98 |
| ${}^{186}$Tl | 186 | 105 | -56.2501 | -1038586159.73 | 174752.0496 | +8739589.89 | 119.78 |
| ${}^{187}$Tl | 187 | 106 | -49.6753 | -1033829267.97 | 175685.0402 | +8716277.18 | 46.21 |
| ${}^{188}$Tl | 188 | 107 | -43.1102 | -1029200040.57 | 176618.0406 | +8677887.04 | 170.78 |
| ${}^{189}$Tl | 189 | 108 | -36.5547 | -1024587386.18 | 177551.0505 | +8653640.32 | 47.54 |
| ${}^{190}$Tl | 190 | 109 | -30.0087 | -1020078768.65 | 178484.0699 | +8615283.77 | 40.97 |
| ${}^{191}$Tl | 191 | 110 | -23.4720 | -1015600824.65 | 179417.0986 | +8589665.48 | 41.31 |
| ${}^{192}$Tl | 192 | 111 | -16.9446 | -1011205266.60 | 180350.1366 | +8551238.43 | 177.11 |
| ${}^{193}$Tl | 193 | 112 | -10.4263 | -1006850942.90 | 181283.1838 | +8524569.80 | 37.31 |
| ${}^{194}$Tl | 194 | 113 | -3.9170 | -1002561120.21 | 182216.2399 | +8486254.84 | 77.33 |
| ${}^{195}$Tl | 195 | 114 | 2.5834 | -998321065.03 | 183149.3050 | +8458141.26 | 61.26 |
| ${}^{196}$Tl | 196 | 115 | 9.0749 | -994130477.14 | 184082.3789 | +8419996.28 | 66.34 |
| ${}^{197}$Tl | 197 | 116 | 15.5577 | -989995253.98 | 185015.4615 | +8390620.04 | 73.99 |
| ${}^{198}$Tl | 198 | 117 | 22.0319 | -985897578.21 | 185948.5527 | +8352383.71 | 40.92 |
| ${}^{199}$Tl | 199 | 118 | 28.4976 | -981858835.51 | 186881.6524 | +8321955.75 | 150.78 |
| ${}^{200}$Tl | 200 | 119 | 34.9549 | -977847773.39 | 187814.7606 | +8283525.85 | 30.91 |
| ${}^{201}$Tl | 201 | 120 | 41.4039 | -973896557.26 | 188747.8770 | +8251693.91 | 75.77 |
| ${}^{202}$Tl | 202 | 121 | 47.8446 | -969966039.44 | 189681.0017 | +8213072.42 | 9.76 |
| ${}^{203}$Tl | 203 | 122 | 54.2772 | -966095159.45 | 190614.1345 | +8180107.36 | 6.19 |
| ${}^{204}$Tl | 204 | 123 | 60.7018 | -962238989.48 | 191547.2754 | +8141161.23 | 6.07 |
| ${}^{205}$Tl | 205 | 124 | 67.1184 | -958442458.67 | 192480.4242 | +8107336.29 | 6.49 |
| ${}^{206}$Tl | 206 | 125 | 73.5271 | -954656960.72 | 193413.5809 | +8068404.93 | 6.70 |
| ${}^{207}$Tl | 207 | 126 | 79.9281 | -950916993.31 | 194346.7453 | +8031713.63 | 28.21 |
| ${}^{208}$Tl | 208 | 127 | 86.3214 | -947113932.91 | 195279.9175 | +7979465.77 | 9.56 |
| ${}^{209}$Tl | 209 | 128 | 92.7071 | -943373935.20 | 196213.0972 | +7933863.69 | 31.38 |
| ${}^{210}$Tl | 210 | 129 | 99.0852 | -939613610.37 | 197146.2845 | +7882076.14 | 59.32 |
| ${}^{211}$Tl | 211 | 130 | 105.4560 | -935922487.62 | 198079.4792 | +7837120.81 | 213.28 |
| ${}^{212}$Tl | 212 | 131 | 111.8193 | -932204423.34 | 199012.6812 | +7785697.57 | 1014.16 |
| ${}^{213}$Tl | 213 | 132 | 118.1754 | -928553347.72 | 199945.8906 | +7740852.02 | 136.15 |
| ${}^{214}$Tl | 214 | 133 | 124.5243 | -924869060.19 | 200879.1071 | +7689659.13 | 981.28 |
| ${}^{215}$Tl | 215 | 134 | 130.8660 | -921257541.82 | 201812.3308 | +7644590.07 | 1497.60 |
| ${}^{216}$Tl | 216 | 135 | 137.2007 | -917604282.89 | 202745.5615 | +7593593.93 | 1490.63 |
| ${}^{217}$Tl | 217 | 136 | 143.5285 | -914022943.28 | 203678.7992 | +7548341.59 | 1976.78 |
| ${}^{218}$Tl | 218 | 137 | 149.8493 | -910403794.86 | 204612.0438 | +7497283.14 | 1967.66 |

### Lead (Z = 82)

_43 of 43 isotopes with a framework prediction; 43 of 43 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{178}$Pb | 178 | 96 | -132.2307 | -1096591477.14 | 167310.7245 | +9053766.53 | 139.82 |
| ${}^{179}$Pb | 179 | 97 | -125.5368 | -1091063563.84 | 168243.5960 | +9020657.21 | 487.16 |
| ${}^{180}$Pb | 180 | 98 | -118.8538 | -1085467839.76 | 169176.4785 | +9002850.22 | 73.92 |
| ${}^{181}$Pb | 181 | 99 | -112.1817 | -1080137395.01 | 170109.3718 | +8968408.36 | 504.37 |
| ${}^{182}$Pb | 182 | 100 | -105.5203 | -1074749496.35 | 171042.2758 | +8949550.58 | 71.29 |
| ${}^{183}$Pb | 183 | 101 | -98.8695 | -1069602912.13 | 171975.1904 | +8913448.92 | 170.01 |
| ${}^{184}$Pb | 184 | 102 | -92.2291 | -1064404816.08 | 172908.1155 | +8893789.25 | 74.70 |
| ${}^{185}$Pb | 185 | 103 | -85.5990 | -1059419741.30 | 173841.0508 | +8856942.41 | 93.87 |
| ${}^{186}$Pb | 186 | 104 | -78.9792 | -1054401116.67 | 174773.9964 | +8835982.11 | 63.52 |
| ${}^{187}$Pb | 187 | 105 | -72.3694 | -1049562284.87 | 175706.9520 | +8798890.74 | 29.24 |
| ${}^{188}$Pb | 188 | 106 | -65.7696 | -1044708773.65 | 176639.9176 | +8776756.84 | 57.81 |
| ${}^{189}$Pb | 189 | 107 | -59.1796 | -1040008609.02 | 177572.8930 | +8738918.21 | 79.88 |
| ${}^{190}$Pb | 190 | 108 | -52.5993 | -1035305907.92 | 178505.8782 | +8716008.58 | 70.71 |
| ${}^{191}$Pb | 191 | 109 | -46.0285 | -1030731576.26 | 179438.8729 | +8678094.31 | 37.17 |
| ${}^{192}$Pb | 192 | 110 | -39.4673 | -1026170347.49 | 180371.8771 | +8654085.87 | 32.02 |
| ${}^{193}$Pb | 193 | 111 | -32.9154 | -1021714298.77 | 181304.8906 | +8615883.17 | 57.23 |
| ${}^{194}$Pb | 194 | 112 | -26.3728 | -1017283543.78 | 182237.9134 | +8590970.90 | 96.49 |
| ${}^{195}$Pb | 195 | 113 | -19.8393 | -1012937347.69 | 183170.9453 | +8552767.23 | 28.01 |
| ${}^{196}$Pb | 196 | 114 | -13.3149 | -1008628245.61 | 184103.9863 | +8526494.57 | 42.24 |
| ${}^{197}$Pb | 197 | 115 | -6.7994 | -1004384875.93 | 185037.0362 | +8488372.83 | 26.18 |
| ${}^{198}$Pb | 198 | 116 | -0.2927 | -1000187619.78 | 185970.0950 | +8461210.76 | 47.45 |
| ${}^{199}$Pb | 199 | 117 | 6.2053 | -996040723.45 | 186903.1624 | +8422628.14 | 36.80 |
| ${}^{200}$Pb | 200 | 118 | 12.6946 | -991946906.69 | 187836.2385 | +8394519.16 | 53.73 |
| ${}^{201}$Pb | 201 | 119 | 19.1754 | -987890145.81 | 188769.3232 | +8355967.97 | 73.43 |
| ${}^{202}$Pb | 202 | 120 | 25.6478 | -983891564.48 | 189702.4162 | +8326683.73 | 20.18 |
| ${}^{203}$Pb | 203 | 121 | 32.1118 | -979918978.29 | 190635.5176 | +8288006.19 | 34.66 |
| ${}^{204}$Pb | 204 | 122 | 38.5676 | -976007815.75 | 191568.6272 | +8257591.98 | 6.04 |
| ${}^{205}$Pb | 205 | 123 | 45.0152 | -972113634.95 | 192501.7450 | +8218735.66 | 5.99 |
| ${}^{206}$Pb | 206 | 124 | 51.4548 | -968283282.38 | 193434.8709 | +8187419.22 | 5.96 |
| ${}^{207}$Pb | 207 | 125 | 57.8864 | -964466416.38 | 194368.0047 | +8149393.27 | 5.95 |
| ${}^{208}$Pb | 208 | 126 | 64.3102 | -960700949.58 | 195301.1464 | +8115053.01 | 5.92 |
| ${}^{209}$Pb | 209 | 127 | 70.7261 | -956884000.02 | 196234.2958 | +8063316.68 | 8.97 |
| ${}^{210}$Pb | 210 | 128 | 77.1343 | -953125590.49 | 197167.4530 | +8018545.22 | 7.40 |
| ${}^{211}$Pb | 211 | 129 | 83.5349 | -949354014.97 | 198100.6179 | +7967318.22 | 11.50 |
| ${}^{212}$Pb | 212 | 130 | 89.9280 | -945646960.04 | 199033.7902 | +7923206.10 | 9.32 |
| ${}^{213}$Pb | 213 | 131 | 96.3136 | -941918267.57 | 199966.9701 | +7872428.89 | 35.05 |
| ${}^{214}$Pb | 214 | 132 | 102.6918 | -938259948.96 | 200900.1573 | +7828863.17 | 9.88 |
| ${}^{215}$Pb | 215 | 133 | 109.0627 | -934569145.95 | 201833.3518 | +7778168.93 | 263.06 |
| ${}^{216}$Pb | 216 | 134 | 115.4264 | -930958488.83 | 202766.5535 | +7734782.58 | 995.33 |
| ${}^{217}$Pb | 217 | 135 | 121.7829 | -927294794.51 | 203699.7624 | +7683940.82 | 1483.78 |
| ${}^{218}$Pb | 218 | 136 | 128.1323 | -923716668.81 | 204632.9784 | +7640456.83 | 1476.95 |
| ${}^{219}$Pb | 219 | 137 | 134.4748 | -920088468.45 | 205566.2014 | +7589400.91 | 1958.71 |
| ${}^{220}$Pb | 220 | 138 | 140.8103 | -916551893.02 | 206499.4313 | +7546117.10 | 1949.77 |

### Bismuth (Z = 83)

_41 of 41 isotopes with a framework prediction; 41 of 41 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{184}$Bi | 184 | 101 | -115.2788 | -1081239026.00 | 172930.3829 | +8951268.03 | 711.95 |
| ${}^{185}$Bi | 185 | 102 | -108.6129 | -1075930741.13 | 173863.2823 | +8931473.01 | 470.28 |
| ${}^{186}$Bi | 186 | 103 | -101.9573 | -1070829475.57 | 174796.1922 | +8896923.96 | 97.85 |
| ${}^{187}$Bi | 187 | 104 | -95.3121 | -1065696923.02 | 175729.1124 | +8876286.23 | 57.44 |
| ${}^{188}$Bi | 188 | 105 | -88.6771 | -1060751554.19 | 176662.0428 | +8841947.51 | 63.84 |
| ${}^{189}$Bi | 189 | 106 | -82.0521 | -1055794665.27 | 177594.9833 | +8819824.33 | 118.44 |
| ${}^{190}$Bi | 190 | 107 | -75.4371 | -1050998203.97 | 178527.9337 | +8784658.73 | 118.51 |
| ${}^{191}$Bi | 191 | 108 | -68.8320 | -1046198228.41 | 179460.8939 | +8761893.14 | 42.08 |
| ${}^{192}$Bi | 192 | 109 | -62.2365 | -1041538269.43 | 180393.8639 | +8726172.58 | 168.38 |
| ${}^{193}$Bi | 193 | 110 | -55.6506 | -1036886125.97 | 181326.8435 | +8702405.69 | 42.14 |
| ${}^{194}$Bi | 194 | 111 | -49.0742 | -1032351149.18 | 182259.8325 | +8666590.14 | 29.06 |
| ${}^{195}$Bi | 195 | 112 | -42.5072 | -1027837115.87 | 183192.8309 | +8641545.59 | 29.11 |
| ${}^{196}$Bi | 196 | 113 | -35.9495 | -1023419039.78 | 184125.8386 | +8605651.37 | 133.81 |
| ${}^{197}$Bi | 197 | 114 | -29.4009 | -1019032116.85 | 185058.8554 | +8579486.82 | 45.42 |
| ${}^{198}$Bi | 198 | 115 | -22.8613 | -1014724903.08 | 185991.8812 | +8542743.83 | 149.50 |
| ${}^{199}$Bi | 199 | 116 | -16.3307 | -1010454612.88 | 186924.9161 | +8515870.48 | 57.27 |
| ${}^{200}$Bi | 200 | 117 | -9.8089 | -1006248908.09 | 187857.9597 | +8479292.88 | 121.86 |
| ${}^{201}$Bi | 201 | 118 | -3.2959 | -1002087541.92 | 188791.0121 | +8451127.97 | 65.04 |
| ${}^{202}$Bi | 202 | 119 | 3.2085 | -997977255.05 | 189724.0731 | +8413979.60 | 74.42 |
| ${}^{203}$Bi | 203 | 120 | 9.7044 | -993916009.86 | 190657.1427 | +8384987.68 | 67.58 |
| ${}^{204}$Bi | 204 | 121 | 16.1918 | -989894410.12 | 191590.2207 | +8347551.70 | 48.31 |
| ${}^{205}$Bi | 205 | 122 | 22.6708 | -985925299.65 | 192523.3071 | +8317382.91 | 25.18 |
| ${}^{206}$Bi | 206 | 123 | 29.1416 | -981986707.44 | 193456.4017 | +8279893.19 | 39.78 |
| ${}^{207}$Bi | 207 | 124 | 35.6043 | -978101578.74 | 194389.5045 | +8248371.23 | 12.43 |
| ${}^{208}$Bi | 208 | 125 | 42.0588 | -974240813.81 | 195322.6154 | +8210893.08 | 11.90 |
| ${}^{209}$Bi | 209 | 126 | 48.5054 | -970427684.61 | 196255.7342 | +8176781.86 | 7.01 |
| ${}^{210}$Bi | 210 | 127 | 54.9440 | -966595995.44 | 197188.8610 | +8128320.47 | 6.97 |
| ${}^{211}$Bi | 211 | 128 | 61.3749 | -962802477.47 | 198121.9956 | +8083098.45 | 27.69 |
| ${}^{212}$Bi | 212 | 129 | 67.7980 | -959017168.92 | 199055.1379 | +8034216.92 | 9.38 |
| ${}^{213}$Bi | 213 | 130 | 74.2135 | -955279285.66 | 199988.2878 | +7990178.09 | 25.61 |
| ${}^{214}$Bi | 214 | 131 | 80.6214 | -951535907.98 | 200921.4453 | +7940802.35 | 56.23 |
| ${}^{215}$Bi | 215 | 132 | 87.0218 | -947852710.93 | 201854.6103 | +7897968.61 | 28.08 |
| ${}^{216}$Bi | 216 | 133 | 93.4148 | -944149803.79 | 202787.7828 | +7848483.41 | 55.55 |
| ${}^{217}$Bi | 217 | 134 | 99.8005 | -940517446.36 | 203720.9625 | +7806416.27 | 87.55 |
| ${}^{218}$Bi | 218 | 135 | 106.1789 | -936850745.02 | 204654.1495 | +7756682.67 | 133.02 |
| ${}^{219}$Bi | 219 | 136 | 112.5502 | -933256121.83 | 205587.3436 | +7714268.51 | 981.66 |
| ${}^{220}$Bi | 220 | 137 | 118.9144 | -929628973.26 | 206520.5449 | +7664723.62 | 1463.49 |
| ${}^{221}$Bi | 221 | 138 | 125.2715 | -926077280.52 | 207453.7532 | +7622510.74 | 1456.84 |
| ${}^{222}$Bi | 222 | 139 | 131.6217 | -922477701.29 | 208386.9684 | +7573361.45 | 1450.25 |
| ${}^{223}$Bi | 223 | 140 | 137.9650 | -918978893.23 | 209320.1905 | +7531766.94 | 1923.47 |
| ${}^{224}$Bi | 224 | 141 | 144.3015 | -915414500.71 | 210253.4194 | +7483144.26 | 1914.84 |

### Polonium (Z = 84)

_42 of 42 isotopes with a framework prediction; 42 of 42 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{186}$Po | 186 | 102 | -125.1844 | -1087453100.98 | 174818.6370 | +8984267.26 | 105.49 |
| ${}^{187}$Po | 187 | 103 | -118.5034 | -1082248560.87 | 175751.5213 | +8951605.95 | 187.32 |
| ${}^{188}$Po | 188 | 104 | -111.8327 | -1077007318.53 | 176684.4161 | +8931395.02 | 114.03 |
| ${}^{189}$Po | 189 | 105 | -105.1724 | -1071977526.34 | 177617.3212 | +8897182.85 | 125.30 |
| ${}^{190}$Po | 190 | 106 | -98.5223 | -1066912896.25 | 178550.2365 | +8876288.74 | 74.38 |
| ${}^{191}$Po | 191 | 107 | -91.8822 | -1062041779.89 | 179483.1619 | +8840729.05 | 39.92 |
| ${}^{192}$Po | 192 | 108 | -85.2521 | -1057137860.80 | 180416.0972 | +8819650.72 | 59.46 |
| ${}^{193}$Po | 193 | 109 | -78.6318 | -1052408204.43 | 181349.0423 | +8783474.98 | 80.83 |
| ${}^{194}$Po | 194 | 110 | -72.0213 | -1047660750.51 | 182281.9972 | +8761238.24 | 71.45 |
| ${}^{195}$Po | 195 | 111 | -65.4203 | -1043059314.67 | 183214.9616 | +8725023.62 | 33.26 |
| ${}^{196}$Po | 196 | 112 | -58.8288 | -1038456996.42 | 184147.9356 | +8701607.30 | 29.48 |
| ${}^{197}$Po | 197 | 113 | -52.2467 | -1033976618.61 | 185080.9189 | +8665133.61 | 53.73 |
| ${}^{198}$Po | 198 | 114 | -45.6739 | -1029507433.94 | 186013.9115 | +8640869.42 | 94.48 |
| ${}^{199}$Po | 199 | 115 | -39.1102 | -1025139716.44 | 186946.9133 | +8604302.53 | 29.29 |
| ${}^{200}$Po | 200 | 116 | -32.5556 | -1020795808.71 | 187879.9241 | +8578639.02 | 40.68 |
| ${}^{201}$Po | 201 | 117 | -26.0099 | -1016533777.03 | 188812.9438 | +8541839.27 | 26.40 |
| ${}^{202}$Po | 202 | 118 | -19.4731 | -1012304270.88 | 189745.9724 | +8515318.98 | 46.08 |
| ${}^{203}$Po | 203 | 119 | -12.9451 | -1008141179.81 | 190679.0098 | +8478165.49 | 24.54 |
| ${}^{204}$Po | 204 | 120 | -6.4256 | -1004018107.41 | 191612.0558 | +8450237.55 | 53.00 |
| ${}^{205}$Po | 205 | 121 | 0.0852 | -999946960.70 | 192545.1104 | +8412856.71 | 52.68 |
| ${}^{206}$Po | 206 | 122 | 6.5876 | -995921405.87 | 193478.1734 | +8383697.76 | 20.90 |
| ${}^{207}$Po | 207 | 123 | 13.0816 | -991935835.42 | 194411.2448 | +8345919.23 | 34.53 |
| ${}^{208}$Po | 208 | 124 | 19.5674 | -987999795.78 | 195344.3245 | +8315659.09 | 8.63 |
| ${}^{209}$Po | 209 | 125 | 26.0449 | -984095225.19 | 196277.4123 | +8278340.79 | 9.13 |
| ${}^{210}$Po | 210 | 126 | 32.5144 | -980236960.35 | 197210.5083 | +8244977.68 | 5.86 |
| ${}^{211}$Po | 211 | 127 | 38.9759 | -976374874.79 | 198143.6122 | +8196029.68 | 6.38 |
| ${}^{212}$Po | 212 | 128 | 45.4294 | -972562996.60 | 199076.7241 | +8155026.39 | 5.84 |
| ${}^{213}$Po | 213 | 129 | 51.8751 | -968752318.07 | 200009.8438 | +8106050.25 | 15.39 |
| ${}^{214}$Po | 214 | 130 | 58.3131 | -964998461.50 | 200942.9713 | +8065321.76 | 7.27 |
| ${}^{215}$Po | 215 | 131 | 64.7434 | -961235178.63 | 201876.1064 | +8016229.91 | 10.59 |
| ${}^{216}$Po | 216 | 132 | 71.1661 | -957535735.02 | 202809.2491 | +7975668.22 | 9.02 |
| ${}^{217}$Po | 217 | 133 | 77.5813 | -953817239.38 | 203742.3994 | +7926657.68 | 32.37 |
| ${}^{218}$Po | 218 | 134 | 83.9891 | -950168865.46 | 204675.5570 | +7886214.83 | 9.69 |
| ${}^{219}$Po | 219 | 135 | 90.3895 | -946490406.11 | 205608.7220 | +7837031.51 | 77.62 |
| ${}^{220}$Po | 220 | 136 | 96.7826 | -942891306.96 | 206541.8943 | +7796901.91 | 86.36 |
| ${}^{221}$Po | 221 | 137 | 103.1686 | -939250784.68 | 207475.0737 | +7747733.13 | 95.01 |
| ${}^{222}$Po | 222 | 138 | 109.5474 | -935697610.76 | 208408.2603 | +7707803.52 | 193.67 |
| ${}^{223}$Po | 223 | 139 | 115.9192 | -932094435.00 | 209341.4540 | +7659149.42 | 941.58 |
| ${}^{224}$Po | 224 | 140 | 122.2840 | -928583096.09 | 210274.6546 | +7619465.74 | 937.37 |
| ${}^{225}$Po | 225 | 141 | 128.6419 | -925027289.23 | 211207.8621 | +7571334.86 | 1430.88 |
| ${}^{226}$Po | 226 | 142 | 134.9930 | -921550547.22 | 212141.0765 | +7531803.41 | 1902.32 |
| ${}^{227}$Po | 227 | 143 | 141.3373 | -918031692.68 | 213074.2976 | +7484253.29 | 1893.89 |

### Astatine (Z = 85)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{191}$At | 191 | 106 | -115.1793 | -1078286277.61 | 179505.6767 | +8916623.98 | 90.51 |
| ${}^{192}$At | 192 | 107 | -108.5142 | -1073307116.09 | 180438.5769 | +8883338.51 | 155.84 |
| ${}^{193}$At | 193 | 108 | -101.8591 | -1068300717.39 | 181371.4872 | +8861984.92 | 120.32 |
| ${}^{194}$At | 194 | 109 | -95.2139 | -1063473705.05 | 182304.4075 | +8827820.60 | 130.05 |
| ${}^{195}$At | 195 | 110 | -88.5786 | -1058627226.79 | 183237.3376 | +8805749.48 | 52.70 |
| ${}^{196}$At | 196 | 111 | -81.9530 | -1053938000.66 | 184170.2774 | +8771187.09 | 165.61 |
| ${}^{197}$At | 197 | 112 | -75.3370 | -1049242888.41 | 185103.2268 | +8748017.93 | 43.50 |
| ${}^{198}$At | 198 | 113 | -68.7304 | -1044678605.22 | 186036.1857 | +8713710.24 | 26.59 |
| ${}^{199}$At | 199 | 114 | -62.1333 | -1040124423.58 | 186969.1540 | +8689381.58 | 29.05 |
| ${}^{200}$At | 200 | 115 | -55.5455 | -1035680354.42 | 187902.1316 | +8654786.57 | 131.33 |
| ${}^{201}$At | 201 | 116 | -48.9668 | -1031256224.19 | 188835.1183 | +8629404.02 | 43.71 |
| ${}^{202}$At | 202 | 117 | -42.3972 | -1026927346.95 | 189768.1141 | +8593621.35 | 146.70 |
| ${}^{203}$At | 203 | 118 | -35.8365 | -1022622044.24 | 190701.1189 | +8567636.35 | 56.18 |
| ${}^{204}$At | 204 | 119 | -29.2847 | -1018395786.14 | 191634.1325 | +8532107.20 | 119.30 |
| ${}^{205}$At | 205 | 120 | -22.7417 | -1014203734.13 | 192567.1549 | +8504347.19 | 63.13 |
| ${}^{206}$At | 206 | 121 | -16.2073 | -1010075213.99 | 193500.1860 | +8468206.20 | 70.50 |
| ${}^{207}$At | 207 | 122 | -9.6815 | -1005985510.27 | 194433.2256 | +8439432.23 | 64.34 |
| ${}^{208}$At | 208 | 123 | -3.1642 | -1001947424.76 | 195366.2737 | +8402933.20 | 46.05 |
| ${}^{209}$At | 209 | 124 | 3.3448 | -997952134.96 | 196299.3302 | +8372894.81 | 24.37 |
| ${}^{210}$At | 210 | 125 | 9.8454 | -993998346.67 | 197232.3949 | +8336351.47 | 39.34 |
| ${}^{211}$At | 211 | 126 | 16.3379 | -990087427.51 | 198165.4679 | +8303206.96 | 13.88 |
| ${}^{212}$At | 212 | 127 | 22.8222 | -986195537.56 | 199098.5490 | +8256660.10 | 12.07 |
| ${}^{213}$At | 213 | 128 | 29.2985 | -982342533.46 | 200031.6381 | +8215523.50 | 24.69 |
| ${}^{214}$At | 214 | 129 | 35.7669 | -978507300.83 | 200964.7352 | +8168986.91 | 19.97 |
| ${}^{215}$At | 215 | 130 | 42.2274 | -974715487.25 | 201897.8400 | +8128349.37 | 33.10 |
| ${}^{216}$At | 216 | 131 | 48.6802 | -970931105.42 | 202830.9527 | +8081159.85 | 17.76 |
| ${}^{217}$At | 217 | 132 | 55.1253 | -967198712.43 | 203764.0731 | +8041303.54 | 24.74 |
| ${}^{218}$At | 218 | 133 | 61.5627 | -963463128.17 | 204697.2010 | +7994069.53 | 56.64 |
| ${}^{219}$At | 219 | 134 | 67.9927 | -959784869.18 | 205630.3365 | +7954271.00 | 15.86 |
| ${}^{220}$At | 220 | 135 | 74.4151 | -956092462.11 | 206563.4794 | +7906589.91 | 68.18 |
| ${}^{221}$At | 221 | 136 | 80.8303 | -952466182.96 | 207496.6297 | +7867077.22 | 67.87 |
| ${}^{222}$At | 222 | 137 | 87.2381 | -948815357.73 | 208429.7873 | +7819363.75 | 76.57 |
| ${}^{223}$At | 223 | 138 | 93.6387 | -945239776.66 | 209362.9522 | +7780338.75 | 67.26 |
| ${}^{224}$At | 224 | 139 | 100.0322 | -941630172.87 | 210296.1241 | +7732966.22 | 107.13 |
| ${}^{225}$At | 225 | 140 | 106.4185 | -938100865.74 | 211229.3032 | +7694195.79 | 1430.90 |
| ${}^{226}$At | 226 | 141 | 112.7979 | -934534906.75 | 212162.4892 | +7647323.64 | 1424.54 |
| ${}^{227}$At | 227 | 142 | 119.1704 | -931041682.65 | 213095.6822 | +7608474.72 | 1418.25 |
| ${}^{228}$At | 228 | 143 | 125.5360 | -927514952.66 | 214028.8820 | +7562033.64 | 1881.21 |
| ${}^{229}$At | 229 | 144 | 131.8948 | -924065947.58 | 214962.0886 | +7522832.24 | 1872.97 |

### Radon (Z = 86)

_39 of 39 isotopes with a framework prediction; 39 of 39 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{193}$Rn | 193 | 107 | -125.3323 | -1084601697.37 | 181394.1781 | +8937073.24 | 139.67 |
| ${}^{194}$Rn | 194 | 108 | -118.6521 | -1079481391.99 | 182327.0634 | +8917231.45 | 92.18 |
| ${}^{195}$Rn | 195 | 109 | -111.9821 | -1074576401.03 | 183259.9587 | +8882962.83 | 284.54 |
| ${}^{196}$Rn | 196 | 110 | -105.3219 | -1069624129.50 | 184192.8640 | +8862364.03 | 76.97 |
| ${}^{197}$Rn | 197 | 111 | -98.6716 | -1064861864.03 | 185125.7791 | +8827676.78 | 88.24 |
| ${}^{198}$Rn | 198 | 112 | -92.0310 | -1060069730.91 | 186058.7039 | +8805840.74 | 72.76 |
| ${}^{199}$Rn | 199 | 113 | -85.4000 | -1055437623.62 | 186991.6384 | +8771153.49 | 39.36 |
| ${}^{200}$Rn | 200 | 114 | -78.7785 | -1050792666.66 | 187924.5823 | +8748294.92 | 31.09 |
| ${}^{201}$Rn | 201 | 115 | -72.1664 | -1046285434.67 | 188857.5356 | +8713140.26 | 54.06 |
| ${}^{202}$Rn | 202 | 116 | -65.5636 | -1041776248.81 | 189790.4982 | +8689427.38 | 93.11 |
| ${}^{203}$Rn | 203 | 117 | -58.9700 | -1037384756.55 | 190723.4700 | +8653952.85 | 30.75 |
| ${}^{204}$Rn | 204 | 118 | -52.3854 | -1033004135.10 | 191656.4509 | +8628834.92 | 39.17 |
| ${}^{205}$Rn | 205 | 119 | -45.8098 | -1028720006.39 | 192589.4407 | +8593199.23 | 26.60 |
| ${}^{206}$Rn | 206 | 120 | -39.2431 | -1024457479.65 | 193522.4394 | +8566804.76 | 44.77 |
| ${}^{207}$Rn | 207 | 121 | -32.6851 | -1020274671.46 | 194455.4469 | +8530660.46 | 24.59 |
| ${}^{208}$Rn | 208 | 122 | -26.1358 | -1016121218.06 | 195388.4630 | +8502814.75 | 52.45 |
| ${}^{209}$Rn | 209 | 123 | -19.5952 | -1012032159.97 | 196321.4878 | +8466291.46 | 51.16 |
| ${}^{210}$Rn | 210 | 124 | -13.0629 | -1007978347.82 | 197254.5210 | +8437264.21 | 23.30 |
| ${}^{211}$Rn | 211 | 125 | -6.5391 | -1003976316.34 | 198187.5626 | +8400790.82 | 34.67 |
| ${}^{212}$Rn | 212 | 126 | -0.0236 | -1000014302.20 | 199120.6125 | +8368550.72 | 15.75 |
| ${}^{213}$Rn | 213 | 127 | 6.4837 | -996088540.56 | 200053.6706 | +8322083.11 | 16.99 |
| ${}^{214}$Rn | 214 | 128 | 12.9828 | -992199233.10 | 200986.7369 | +8284119.20 | 46.09 |
| ${}^{215}$Rn | 215 | 129 | 19.4739 | -988333514.83 | 201919.8112 | +8237616.07 | 30.41 |
| ${}^{216}$Rn | 216 | 130 | 25.9571 | -984511263.00 | 202852.8935 | +8200245.06 | 28.67 |
| ${}^{217}$Rn | 217 | 131 | 32.4324 | -980701153.88 | 203785.9836 | +8153367.98 | 20.76 |
| ${}^{218}$Rn | 218 | 132 | 38.8999 | -976942029.21 | 204719.0815 | +8116127.01 | 11.40 |
| ${}^{219}$Rn | 219 | 133 | 45.3597 | -973183856.58 | 205652.1871 | +8069119.35 | 10.29 |
| ${}^{220}$Rn | 220 | 134 | 51.8119 | -969482860.06 | 206585.3004 | +8031575.39 | 8.85 |
| ${}^{221}$Rn | 221 | 135 | 58.2565 | -965771895.12 | 207518.4212 | +7984240.60 | 27.75 |
| ${}^{222}$Rn | 222 | 136 | 64.6937 | -962127107.38 | 208451.5494 | +7946916.67 | 9.40 |
| ${}^{223}$Rn | 223 | 137 | 71.1234 | -958461571.44 | 209384.6851 | +7899691.78 | 37.65 |
| ${}^{224}$Rn | 224 | 138 | 77.5459 | -954869215.26 | 210317.8280 | +7862403.32 | 47.03 |
| ${}^{225}$Rn | 225 | 139 | 83.9611 | -951248625.80 | 211250.9783 | +7815703.53 | 53.14 |
| ${}^{226}$Rn | 226 | 140 | 90.3692 | -947705725.65 | 212184.1356 | +7778432.15 | 49.76 |
| ${}^{227}$Rn | 227 | 141 | 96.7701 | -944128811.29 | 213117.3001 | +7732347.74 | 66.63 |
| ${}^{228}$Rn | 228 | 142 | 103.1640 | -940633056.68 | 214050.4716 | +7695151.34 | 83.22 |
| ${}^{229}$Rn | 229 | 143 | 109.5510 | -937100659.25 | 214983.6501 | +7649994.54 | 61.12 |
| ${}^{230}$Rn | 230 | 144 | 115.9311 | -933634203.50 | 215916.8354 | +7611431.83 | 934.60 |
| ${}^{231}$Rn | 231 | 145 | 122.3044 | -930141689.98 | 216850.0275 | +7565873.31 | 1393.64 |

### Francium (Z = 87)

_37 of 37 isotopes with a framework prediction; 37 of 37 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{197}$Fr | 197 | 110 | -122.2506 | -1080867937.45 | 185148.5758 | +8903833.64 | 307.52 |
| ${}^{198}$Fr | 198 | 111 | -115.5755 | -1076012576.60 | 186081.4661 | +8870136.22 | 168.77 |
| ${}^{199}$Fr | 199 | 112 | -108.9103 | -1071120131.02 | 187014.3663 | +8848422.29 | 74.04 |
| ${}^{200}$Fr | 200 | 113 | -102.2548 | -1066396362.08 | 187947.2762 | +8815234.76 | 163.84 |
| ${}^{201}$Fr | 201 | 114 | -95.6089 | -1061655998.32 | 188880.1957 | +8792704.16 | 48.49 |
| ${}^{202}$Fr | 202 | 115 | -88.9724 | -1057061399.86 | 189813.1248 | +8759413.54 | 32.06 |
| ${}^{203}$Fr | 203 | 116 | -82.3454 | -1052464791.61 | 190746.0632 | +8735772.29 | 32.95 |
| ${}^{204}$Fr | 204 | 117 | -75.7277 | -1047993399.85 | 191679.0109 | +8702027.98 | 129.36 |
| ${}^{205}$Fr | 205 | 118 | -69.1192 | -1043529594.03 | 192611.9677 | +8677366.11 | 40.97 |
| ${}^{206}$Fr | 206 | 119 | -62.5197 | -1039175827.01 | 193544.9337 | +8642582.20 | 144.93 |
| ${}^{207}$Fr | 207 | 120 | -55.9292 | -1034834972.29 | 194477.9086 | +8616891.08 | 91.05 |
| ${}^{208}$Fr | 208 | 121 | -49.3476 | -1030585434.55 | 195410.8925 | +8582193.74 | 60.16 |
| ${}^{209}$Fr | 209 | 122 | -42.7748 | -1026361501.58 | 196343.8851 | +8554615.16 | 59.09 |
| ${}^{210}$Fr | 210 | 123 | -36.2107 | -1022211640.01 | 197276.8864 | +8519321.68 | 68.61 |
| ${}^{211}$Fr | 211 | 124 | -29.6551 | -1018092055.64 | 198209.8962 | +8490745.89 | 61.01 |
| ${}^{212}$Fr | 212 | 125 | -23.1081 | -1014034067.93 | 199142.9146 | +8455225.06 | 44.43 |
| ${}^{213}$Fr | 213 | 126 | -16.5695 | -1010013694.52 | 200075.9414 | +8423447.72 | 23.72 |
| ${}^{214}$Fr | 214 | 127 | -10.0392 | -1006047118.67 | 201008.9765 | +8378684.14 | 42.73 |
| ${}^{215}$Fr | 215 | 128 | -3.5171 | -1002109891.34 | 201942.0199 | +8341022.22 | 35.28 |
| ${}^{216}$Fr | 216 | 129 | 2.9968 | -998208022.89 | 202875.0714 | +8296852.29 | 20.74 |
| ${}^{217}$Fr | 217 | 130 | 9.5027 | -994340574.83 | 203808.1309 | +8259660.89 | 32.31 |
| ${}^{218}$Fr | 218 | 131 | 16.0006 | -990500828.25 | 204741.1984 | +8215894.02 | 20.85 |
| ${}^{219}$Fr | 219 | 132 | 22.4906 | -986699303.04 | 205674.2738 | +8178434.06 | 33.70 |
| ${}^{220}$Fr | 220 | 133 | 28.9729 | -982918391.08 | 206607.3571 | +8134919.50 | 19.65 |
| ${}^{221}$Fr | 221 | 134 | 35.4473 | -979178258.20 | 207540.4480 | +8097079.17 | 23.73 |
| ${}^{222}$Fr | 222 | 135 | 41.9142 | -975451314.05 | 208473.5466 | +8053251.75 | 36.03 |
| ${}^{223}$Fr | 223 | 136 | 48.3735 | -971768504.33 | 209406.6527 | +8015176.17 | 9.30 |
| ${}^{224}$Fr | 224 | 137 | 54.8253 | -968090762.26 | 210339.7664 | +7970897.93 | 53.57 |
| ${}^{225}$Fr | 225 | 138 | 61.2696 | -964464106.07 | 211272.8874 | +7933273.75 | 57.09 |
| ${}^{226}$Fr | 226 | 139 | 67.7067 | -960829985.13 | 212206.0158 | +7888224.95 | 29.59 |
| ${}^{227}$Fr | 227 | 140 | 74.1364 | -957256326.75 | 213139.1514 | +7850938.70 | 27.89 |
| ${}^{228}$Fr | 228 | 141 | 80.5590 | -953670074.79 | 214072.2943 | +7806708.05 | 31.69 |
| ${}^{229}$Fr | 229 | 142 | 86.9745 | -950146431.32 | 215005.4442 | +7769595.33 | 23.44 |
| ${}^{230}$Fr | 230 | 143 | 93.3829 | -946603302.74 | 215938.6012 | +7725622.56 | 30.52 |
| ${}^{231}$Fr | 231 | 144 | 99.7844 | -943121079.17 | 216871.7652 | +7687798.70 | 35.92 |
| ${}^{232}$Fr | 232 | 145 | 106.1789 | -939616472.85 | 217804.9361 | +7643814.45 | 64.64 |
| ${}^{233}$Fr | 233 | 146 | 112.5666 | -936173435.77 | 218738.1138 | +7605555.45 | 90.11 |

### Radium (Z = 88)

_35 of 35 isotopes with a framework prediction; 35 of 35 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{201}$Ra | 201 | 113 | -119.2941 | -1077385725.89 | 188903.0986 | +8870043.80 | 108.42 |
| ${}^{202}$Ra | 202 | 114 | -112.6237 | -1072544151.99 | 189835.9937 | +8848923.82 | 79.81 |
| ${}^{203}$Ra | 203 | 115 | -105.9629 | -1067880139.61 | 190768.8983 | +8815320.66 | 51.23 |
| ${}^{204}$Ra | 204 | 116 | -99.3116 | -1063189763.04 | 191701.8125 | +8793067.69 | 46.96 |
| ${}^{205}$Ra | 205 | 117 | -92.6698 | -1058652868.08 | 192634.7360 | +8759020.40 | 119.25 |
| ${}^{206}$Ra | 206 | 118 | -86.0372 | -1054101925.55 | 193567.6688 | +8735765.59 | 93.84 |
| ${}^{207}$Ra | 207 | 119 | -79.4138 | -1049683225.48 | 194500.6109 | +8701343.77 | 302.27 |
| ${}^{208}$Ra | 208 | 120 | -72.7995 | -1045265996.72 | 195433.5620 | +8676329.17 | 46.57 |
| ${}^{209}$Ra | 209 | 121 | -66.1942 | -1040956647.06 | 196366.5221 | +8641671.06 | 29.52 |
| ${}^{210}$Ra | 210 | 122 | -59.5977 | -1036660021.89 | 197299.4911 | +8615358.35 | 46.99 |
| ${}^{211}$Ra | 211 | 123 | -53.0101 | -1032454443.96 | 198232.4689 | +8580079.86 | 25.27 |
| ${}^{212}$Ra | 212 | 124 | -46.4312 | -1028269087.03 | 199165.4554 | +8552428.82 | 51.92 |
| ${}^{213}$Ra | 213 | 125 | -39.8608 | -1024158108.99 | 200098.4505 | +8517074.91 | 49.48 |
| ${}^{214}$Ra | 214 | 126 | -33.2990 | -1020079947.15 | 201031.4541 | +8486127.11 | 26.34 |
| ${}^{215}$Ra | 215 | 127 | -26.7456 | -1016073538.42 | 201964.4661 | +8441953.55 | 35.95 |
| ${}^{216}$Ra | 216 | 128 | -20.2006 | -1012086989.60 | 202897.4865 | +8406650.17 | 39.78 |
| ${}^{217}$Ra | 217 | 129 | -13.6638 | -1008149008.64 | 203830.5151 | +8362541.40 | 34.86 |
| ${}^{218}$Ra | 218 | 130 | -7.1351 | -1004236862.76 | 204763.5518 | +8328024.94 | 48.29 |
| ${}^{219}$Ra | 219 | 131 | -0.6145 | -1000363758.46 | 205696.5967 | +8284016.77 | 33.40 |
| ${}^{220}$Ra | 220 | 132 | 5.8981 | -996523534.34 | 206629.6495 | +8249648.96 | 37.06 |
| ${}^{221}$Ra | 221 | 133 | 12.4028 | -992712618.74 | 207562.7102 | +8206749.41 | 22.49 |
| ${}^{222}$Ra | 222 | 134 | 18.8996 | -988938952.14 | 208495.7788 | +8170785.52 | 21.53 |
| ${}^{223}$Ra | 223 | 135 | 25.3888 | -985185899.88 | 209428.8551 | +8127627.39 | 10.06 |
| ${}^{224}$Ra | 224 | 136 | 31.8702 | -981474060.47 | 210361.9390 | +8091271.48 | 8.68 |
| ${}^{225}$Ra | 225 | 137 | 38.3441 | -977774198.98 | 211295.0306 | +8047702.71 | 12.38 |
| ${}^{226}$Ra | 226 | 138 | 44.8105 | -974121978.66 | 212228.1296 | +8011702.89 | 9.15 |
| ${}^{227}$Ra | 227 | 139 | 51.2694 | -970469733.94 | 213161.2361 | +7967307.94 | 9.20 |
| ${}^{228}$Ra | 228 | 140 | 57.7210 | -966874105.03 | 214094.3500 | +7931629.04 | 9.39 |
| ${}^{229}$Ra | 229 | 141 | 64.1653 | -963269536.20 | 215027.4711 | +7887513.85 | 72.37 |
| ${}^{230}$Ra | 230 | 142 | 70.6024 | -959725743.61 | 215960.5994 | +7851659.98 | 48.05 |
| ${}^{231}$Ra | 231 | 143 | 77.0323 | -956167153.29 | 216893.7349 | +7807974.76 | 52.83 |
| ${}^{232}$Ra | 232 | 144 | 83.4552 | -952668374.35 | 217826.8774 | +7771319.54 | 42.33 |
| ${}^{233}$Ra | 233 | 145 | 89.8711 | -949151713.93 | 218760.0270 | +7727785.71 | 39.63 |
| ${}^{234}$Ra | 234 | 146 | 96.2801 | -945693800.32 | 219693.1834 | +7690391.03 | 38.45 |
| ${}^{235}$Ra | 235 | 147 | 102.6822 | -942210633.81 | 220626.3468 | +7645971.74 | 1369.89 |

### Actinium (Z = 89)

_33 of 33 isotopes with a framework prediction; 33 of 33 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{205}$Ac | 205 | 116 | -116.4616 | -1074137595.13 | 192657.7455 | +8835649.83 | 310.62 |
| ${}^{206}$Ac | 206 | 117 | -109.7955 | -1069509407.81 | 193590.6449 | +8803353.58 | 339.17 |
| ${}^{207}$Ac | 207 | 118 | -103.1388 | -1064867695.47 | 194523.5536 | +8780398.05 | 291.69 |
| ${}^{208}$Ac | 208 | 119 | -96.4915 | -1060365848.91 | 195456.4716 | +8747542.21 | 332.79 |
| ${}^{209}$Ac | 209 | 120 | -89.8533 | -1055863897.87 | 196389.3989 | +8722978.04 | 286.84 |
| ${}^{210}$Ac | 210 | 121 | -83.2242 | -1051481507.13 | 197322.3352 | +8689231.08 | 318.00 |
| ${}^{211}$Ac | 211 | 122 | -76.6041 | -1047103989.21 | 198255.2805 | +8663751.52 | 273.48 |
| ${}^{212}$Ac | 212 | 123 | -69.9929 | -1042830293.69 | 199188.2347 | +8629482.53 | 110.81 |
| ${}^{213}$Ac | 213 | 124 | -63.3905 | -1038572277.91 | 200121.1978 | +8602262.64 | 58.79 |
| ${}^{214}$Ac | 214 | 125 | -56.7968 | -1034397289.66 | 201054.1695 | +8568000.24 | 67.97 |
| ${}^{215}$Ac | 215 | 126 | -50.2117 | -1030253974.68 | 201987.1499 | +8537599.29 | 61.94 |
| ${}^{216}$Ac | 216 | 127 | -43.6352 | -1026197470.44 | 202920.1387 | +8494881.79 | 45.87 |
| ${}^{217}$Ac | 217 | 128 | -37.0671 | -1022154138.06 | 203853.1361 | +8460416.07 | 55.52 |
| ${}^{218}$Ac | 218 | 129 | -30.5073 | -1018169201.67 | 204786.1417 | +8418382.80 | 283.71 |
| ${}^{219}$Ac | 219 | 130 | -23.9558 | -1014205126.68 | 205719.1556 | +8383842.03 | 252.33 |
| ${}^{220}$Ac | 220 | 131 | -17.4125 | -1010289133.67 | 206652.1777 | +8342494.11 | 29.90 |
| ${}^{221}$Ac | 221 | 132 | -10.8772 | -1006399872.88 | 207585.2079 | +8308353.09 | 276.39 |
| ${}^{222}$Ac | 222 | 133 | -4.3500 | -1002550442.92 | 208518.2461 | +8268203.71 | 22.72 |
| ${}^{223}$Ac | 223 | 134 | 2.1693 | -998733199.14 | 209451.2922 | +8232760.58 | 33.44 |
| ${}^{224}$Ac | 224 | 135 | 8.6808 | -994947468.56 | 210384.3461 | +8191845.94 | 19.59 |
| ${}^{225}$Ac | 225 | 136 | 15.1845 | -991196247.73 | 211317.4078 | +8156171.16 | 22.70 |
| ${}^{226}$Ac | 226 | 137 | 21.6806 | -987469174.08 | 212250.4772 | +8114774.02 | 14.72 |
| ${}^{227}$Ac | 227 | 138 | 28.1690 | -983780246.39 | 213183.5542 | +8079172.66 | 9.11 |
| ${}^{228}$Ac | 228 | 139 | 34.6499 | -980106103.92 | 214116.6387 | +8036777.97 | 9.85 |
| ${}^{229}$Ac | 229 | 140 | 41.1234 | -976474204.38 | 215049.7307 | +8000694.89 | 56.76 |
| ${}^{230}$Ac | 230 | 141 | 47.5895 | -972851555.51 | 215982.8300 | +7958595.24 | 73.90 |
| ${}^{231}$Ac | 231 | 142 | 54.0483 | -969274745.12 | 216915.9366 | +7922627.59 | 60.60 |
| ${}^{232}$Ac | 232 | 143 | 60.4998 | -965698432.67 | 217849.0505 | +7880162.94 | 60.33 |
| ${}^{233}$Ac | 233 | 144 | 66.9442 | -962171577.09 | 218782.1715 | +7843844.51 | 60.07 |
| ${}^{234}$Ac | 234 | 145 | 73.3815 | -958640088.64 | 219715.2997 | +7801492.51 | 64.09 |
| ${}^{235}$Ac | 235 | 146 | 79.8118 | -955156210.36 | 220648.4348 | +7764216.14 | 63.82 |
| ${}^{236}$Ac | 236 | 147 | 86.2351 | -951661413.03 | 221581.5769 | +7721110.78 | 173.69 |
| ${}^{237}$Ac | 237 | 148 | 92.6516 | -948220539.46 | 222514.7259 | +7683260.40 | 1809.68 |

### Thorium (Z = 90)

_32 of 32 isotopes with a framework prediction; 32 of 32 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{208}$Th | 208 | 118 | -120.4235 | -1075655523.26 | 195479.6214 | +8836157.25 | 164.45 |
| ${}^{209}$Th | 209 | 119 | -113.7521 | -1071090441.43 | 196412.5154 | +8802589.77 | 531.06 |
| ${}^{210}$Th | 210 | 120 | -107.0900 | -1066494606.93 | 197345.4187 | +8779923.73 | 96.65 |
| ${}^{211}$Th | 211 | 121 | -100.4370 | -1062045643.23 | 198278.3311 | +8746471.57 | 437.88 |
| ${}^{212}$Th | 212 | 122 | -93.7932 | -1057591404.08 | 199211.2527 | +8721463.35 | 51.19 |
| ${}^{213}$Th | 213 | 123 | -87.1584 | -1053253829.47 | 200144.1833 | +8687712.79 | 46.45 |
| ${}^{214}$Th | 214 | 124 | -80.5325 | -1048921529.18 | 201077.1228 | +8661579.95 | 53.48 |
| ${}^{215}$Th | 215 | 125 | -73.9154 | -1044688831.46 | 202010.0712 | +8627415.84 | 31.63 |
| ${}^{216}$Th | 216 | 126 | -67.3070 | -1040480651.30 | 202943.0282 | +8597869.13 | 55.18 |
| ${}^{217}$Th | 217 | 127 | -60.7072 | -1036376478.86 | 203875.9939 | +8556013.60 | 52.50 |
| ${}^{218}$Th | 218 | 128 | -54.1160 | -1032273962.04 | 204808.9681 | +8523257.11 | 51.78 |
| ${}^{219}$Th | 219 | 129 | -47.5332 | -1028247431.24 | 205741.9507 | +8481275.59 | 276.74 |
| ${}^{220}$Th | 220 | 130 | -40.9588 | -1024227526.27 | 206674.9417 | +8448915.25 | 66.78 |
| ${}^{221}$Th | 221 | 131 | -34.3926 | -1020273780.24 | 207607.9410 | +8406975.94 | 38.83 |
| ${}^{222}$Th | 222 | 132 | -27.8347 | -1016332815.71 | 208540.9484 | +8375144.54 | 49.39 |
| ${}^{223}$Th | 223 | 133 | -21.2848 | -1012446483.97 | 209473.9640 | +8334321.99 | 38.23 |
| ${}^{224}$Th | 224 | 134 | -14.7430 | -1008583634.92 | 210406.9876 | +8301499.80 | 46.02 |
| ${}^{225}$Th | 225 | 135 | -8.2091 | -1004763508.49 | 211340.0191 | +8260808.64 | 24.30 |
| ${}^{226}$Th | 226 | 136 | -1.6830 | -1000972559.74 | 212273.0585 | +8227349.99 | 21.28 |
| ${}^{227}$Th | 227 | 137 | 4.8353 | -997214674.20 | 213206.1056 | +8186024.80 | 9.87 |
| ${}^{228}$Th | 228 | 138 | 11.3458 | -993490925.32 | 214139.1605 | +8152887.82 | 8.50 |
| ${}^{229}$Th | 229 | 139 | 17.8488 | -989790982.57 | 215072.2229 | +8111341.48 | 11.27 |
| ${}^{230}$Th | 230 | 140 | 24.3442 | -986129686.75 | 216005.2929 | +8077426.52 | 5.64 |
| ${}^{231}$Th | 231 | 141 | 30.8321 | -982484203.27 | 216938.3704 | +8035988.41 | 5.65 |
| ${}^{232}$Th | 232 | 142 | 37.3127 | -978879866.70 | 217871.4553 | +8001109.92 | 6.57 |
| ${}^{233}$Th | 233 | 143 | 43.7859 | -975282786.71 | 218804.5475 | +7958884.75 | 6.56 |
| ${}^{234}$Th | 234 | 144 | 50.2519 | -971731512.33 | 219737.6470 | +7923544.23 | 11.87 |
| ${}^{235}$Th | 235 | 145 | 56.7107 | -968181734.76 | 220670.7536 | +7881524.64 | 59.56 |
| ${}^{236}$Th | 236 | 146 | 63.1624 | -964677549.87 | 221603.8673 | +7845245.39 | 63.55 |
| ${}^{237}$Th | 237 | 147 | 69.6070 | -961168424.88 | 222536.9881 | +7802630.14 | 71.71 |
| ${}^{238}$Th | 238 | 148 | 76.0447 | -957708085.59 | 223470.1159 | +7765540.77 | 1277.01 |
| ${}^{239}$Th | 239 | 149 | 82.4754 | -954232693.61 | 224403.2505 | +7722436.78 | 1794.52 |

### Protactinium (Z = 91)

_31 of 31 isotopes with a framework prediction; 31 of 31 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{211}$Pa | 211 | 120 | -124.5090 | -1077344270.66 | 198301.6208 | +8822996.39 | 353.42 |
| ${}^{212}$Pa | 212 | 121 | -117.8322 | -1072810987.52 | 199234.5094 | +8790771.53 | 443.57 |
| ${}^{213}$Pa | 213 | 122 | -111.1645 | -1068268501.56 | 200167.4072 | +8766453.12 | 288.11 |
| ${}^{214}$Pa | 214 | 123 | -104.5060 | -1063855232.30 | 201100.3141 | +8733562.29 | 407.34 |
| ${}^{215}$Pa | 215 | 124 | -97.8565 | -1059438998.96 | 202033.2300 | +8708380.53 | 411.65 |
| ${}^{216}$Pa | 216 | 125 | -91.2159 | -1055135778.32 | 202966.1548 | +8675081.24 | 122.48 |
| ${}^{217}$Pa | 217 | 126 | -84.5842 | -1050855434.32 | 203899.0885 | +8646065.78 | 61.82 |
| ${}^{218}$Pa | 218 | 127 | -77.9611 | -1046691581.89 | 204832.0309 | +8605619.11 | 87.87 |
| ${}^{219}$Pa | 219 | 128 | -71.3467 | -1042522916.28 | 205764.9819 | +8573796.82 | 341.66 |
| ${}^{220}$Pa | 220 | 129 | -64.7409 | -1038439722.97 | 206697.9415 | +8533637.14 | 71.50 |
| ${}^{221}$Pa | 221 | 130 | -58.1435 | -1034359841.95 | 207630.9095 | +8501713.41 | 288.41 |
| ${}^{222}$Pa | 222 | 131 | -51.5544 | -1030351594.13 | 208563.8859 | +8462350.51 | 418.76 |
| ${}^{223}$Pa | 223 | 132 | -44.9737 | -1026356320.01 | 209496.8706 | +8430255.37 | 364.06 |
| ${}^{224}$Pa | 224 | 133 | -38.4012 | -1022418546.79 | 210429.8634 | +8392438.60 | 36.36 |
| ${}^{225}$Pa | 225 | 134 | -31.8367 | -1018504388.42 | 211362.8644 | +8359954.29 | 390.56 |
| ${}^{226}$Pa | 226 | 135 | -25.2803 | -1014639221.88 | 212295.8735 | +8322131.71 | 53.25 |
| ${}^{227}$Pa | 227 | 136 | -18.7319 | -1010801676.01 | 213228.8904 | +8288877.14 | 34.34 |
| ${}^{228}$Pa | 228 | 137 | -12.1913 | -1007005927.23 | 214161.9153 | +8249797.58 | 20.43 |
| ${}^{229}$Pa | 229 | 138 | -5.6585 | -1003238554.33 | 215094.9479 | +8216389.35 | 15.37 |
| ${}^{230}$Pa | 230 | 139 | 0.8665 | -999505697.27 | 216027.9883 | +8177175.10 | 14.18 |
| ${}^{231}$Pa | 231 | 140 | 7.3840 | -995804226.53 | 216961.0363 | +8143142.42 | 8.23 |
| ${}^{232}$Pa | 232 | 141 | 13.8938 | -992129952.57 | 217894.0918 | +8103508.46 | 35.36 |
| ${}^{233}$Pa | 233 | 142 | 20.3962 | -988489298.02 | 218827.1549 | +8068798.00 | 6.15 |
| ${}^{234}$Pa | 234 | 143 | 26.8912 | -984868423.94 | 219760.2253 | +8028377.21 | 18.78 |
| ${}^{235}$Pa | 235 | 144 | 33.3788 | -981282330.36 | 220693.3031 | +7992475.79 | 63.82 |
| ${}^{236}$Pa | 236 | 145 | 39.8591 | -977711195.00 | 221626.3882 | +7951892.50 | 63.55 |
| ${}^{237}$Pa | 237 | 146 | 46.3323 | -974176352.20 | 222559.4805 | +7915571.55 | 59.06 |
| ${}^{238}$Pa | 238 | 147 | 52.7983 | -970649432.80 | 223492.5799 | +7874258.25 | 71.41 |
| ${}^{239}$Pa | 239 | 148 | 59.2573 | -967160470.09 | 224425.6863 | +7837501.46 | 878.45 |
| ${}^{240}$Pa | 240 | 149 | 65.7093 | -963674064.20 | 225358.7998 | +7795541.49 | 895.60 |
| ${}^{241}$Pa | 241 | 150 | 72.1543 | -960229086.28 | 226291.9202 | +7758192.46 | 1335.74 |

### Uranium (Z = 92)

_29 of 29 isotopes with a framework prediction; 29 of 29 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{215}$U | 215 | 123 | -122.0352 | -1074481285.87 | 202056.6263 | +8789509.85 | 519.91 |
| ${}^{216}$U | 216 | 124 | -115.3621 | -1069985867.09 | 202989.5186 | +8764909.13 | 139.60 |
| ${}^{217}$U | 217 | 125 | -108.6979 | -1065615950.57 | 203922.4199 | +8731961.28 | 396.27 |
| ${}^{218}$U | 218 | 126 | -102.0427 | -1061262026.56 | 204855.3301 | +8704228.06 | 67.52 |
| ${}^{219}$U | 219 | 127 | -95.3964 | -1057043406.19 | 205788.2492 | +8664543.37 | 65.38 |
| ${}^{220}$U | 220 | 128 | -88.7587 | -1052807423.15 | 206721.1770 | +8633548.83 | 490.85 |
| ${}^{221}$U | 221 | 129 | -82.1297 | -1048676233.39 | 207654.1134 | +8594112.76 | 350.37 |
| ${}^{222}$U | 222 | 130 | -75.5093 | -1044532911.08 | 208587.0584 | +8563625.76 | 251.40 |
| ${}^{223}$U | 223 | 131 | -68.8973 | -1040482998.42 | 209520.0118 | +8523648.53 | 284.25 |
| ${}^{224}$U | 224 | 132 | -62.2937 | -1036423614.60 | 210452.9737 | +8494096.97 | 73.13 |
| ${}^{225}$U | 225 | 133 | -55.6984 | -1032445086.95 | 211385.9438 | +8455553.07 | 47.39 |
| ${}^{226}$U | 226 | 134 | -49.1114 | -1028473435.77 | 212318.9221 | +8425400.42 | 52.58 |
| ${}^{227}$U | 227 | 135 | -42.5324 | -1024568614.54 | 213251.9086 | +8387162.25 | 40.24 |
| ${}^{228}$U | 228 | 136 | -35.9615 | -1020678645.63 | 214184.9031 | +8356614.65 | 63.43 |
| ${}^{229}$U | 229 | 137 | -29.3986 | -1016845910.75 | 215117.9056 | +8317789.86 | 27.83 |
| ${}^{230}$U | 230 | 138 | -22.8435 | -1013032491.03 | 216050.9160 | +8286804.18 | 21.04 |
| ${}^{231}$U | 231 | 139 | -16.2963 | -1009266124.81 | 216983.9342 | +8247753.17 | 12.40 |
| ${}^{232}$U | 232 | 140 | -9.7568 | -1005524898.11 | 217916.9601 | +8215547.15 | 8.37 |
| ${}^{233}$U | 233 | 141 | -3.2249 | -1001820201.99 | 218849.9936 | +8176657.77 | 10.38 |
| ${}^{234}$U | 234 | 142 | 3.2994 | -998144918.27 | 219783.0348 | +8143148.22 | 5.18 |
| ${}^{235}$U | 235 | 143 | 9.8162 | -994497250.07 | 220716.0834 | +8102830.88 | 5.10 |
| ${}^{236}$U | 236 | 144 | 16.3255 | -990881696.73 | 221649.1395 | +8068611.78 | 5.05 |
| ${}^{237}$U | 237 | 145 | 22.8275 | -987286534.15 | 222582.2029 | +8028233.78 | 5.44 |
| ${}^{238}$U | 238 | 146 | 29.3222 | -983725178.34 | 223515.2737 | +7992901.77 | 6.73 |
| ${}^{239}$U | 239 | 147 | 35.8097 | -980177287.15 | 224448.3516 | +7951799.63 | 6.74 |
| ${}^{240}$U | 240 | 148 | 42.2900 | -976666627.54 | 225381.4367 | +7916130.90 | 11.41 |
| ${}^{241}$U | 241 | 149 | 48.7632 | -973161287.26 | 226314.5289 | +7874781.48 | 871.15 |
| ${}^{242}$U | 242 | 150 | 55.2295 | -969699825.73 | 227247.6281 | +7838538.30 | 888.20 |
| ${}^{243}$U | 243 | 151 | 61.6887 | -966232622.74 | 228180.7342 | +7796227.23 | 1324.74 |

### Neptunium (Z = 93)

_27 of 27 isotopes with a framework prediction; 27 of 27 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{219}$Np | 219 | 126 | -119.6821 | -1071862865.25 | 205811.7526 | +8749381.32 | 450.77 |
| ${}^{220}$Np | 220 | 127 | -113.0123 | -1067572646.65 | 206744.6482 | +8711346.39 | 149.87 |
| ${}^{221}$Np | 221 | 128 | -106.3514 | -1063261204.96 | 207677.5527 | +8681551.26 | 972.71 |
| ${}^{222}$Np | 222 | 129 | -99.6992 | -1059070511.53 | 208610.4659 | +8642658.59 | 183.98 |
| ${}^{223}$Np | 223 | 130 | -93.0557 | -1054851966.10 | 209543.3878 | +8613771.41 | 398.85 |
| ${}^{224}$Np | 224 | 131 | -86.4207 | -1050740638.13 | 210476.3183 | +8575566.64 | 138.60 |
| ${}^{225}$Np | 225 | 132 | -79.7942 | -1046617733.77 | 211409.2572 | +8546344.10 | 437.07 |
| ${}^{226}$Np | 226 | 133 | -73.1761 | -1042580311.12 | 212342.2045 | +8509694.10 | 484.74 |
| ${}^{227}$Np | 227 | 134 | -66.5663 | -1038547770.56 | 213275.1602 | +8480257.42 | 364.05 |
| ${}^{228}$Np | 228 | 135 | -59.9647 | -1034587475.55 | 214208.1240 | +8444071.29 | 473.61 |
| ${}^{229}$Np | 229 | 136 | -53.3713 | -1030641948.28 | 215141.0960 | +8414243.95 | 474.24 |
| ${}^{230}$Np | 230 | 137 | -46.7859 | -1026759153.60 | 216074.0761 | +8377846.61 | 256.70 |
| ${}^{231}$Np | 231 | 138 | -40.2085 | -1022896594.16 | 217007.0641 | +8346712.96 | 237.69 |
| ${}^{232}$Np | 232 | 139 | -33.6391 | -1019085942.88 | 217940.0600 | +8309592.71 | 461.13 |
| ${}^{233}$Np | 233 | 140 | -27.0774 | -1015298733.80 | 218873.0638 | +8278153.63 | 234.85 |
| ${}^{234}$Np | 234 | 141 | -20.5235 | -1011556167.77 | 219806.0753 | +8240464.77 | 38.51 |
| ${}^{235}$Np | 235 | 142 | -13.9772 | -1007839342.46 | 220739.0945 | +8207359.77 | 6.34 |
| ${}^{236}$Np | 236 | 143 | -7.4386 | -1004158658.31 | 221672.1212 | +8168853.28 | 229.31 |
| ${}^{237}$Np | 237 | 144 | -0.9074 | -1000505461.16 | 222605.1555 | +8134548.72 | 5.07 |
| ${}^{238}$Np | 238 | 145 | 5.6162 | -996881185.18 | 223538.1973 | +8095613.31 | 5.12 |
| ${}^{239}$Np | 239 | 146 | 12.1325 | -993285719.59 | 224471.2464 | +8060326.97 | 5.88 |
| ${}^{240}$Np | 240 | 147 | 18.6415 | -989712413.50 | 225404.3028 | +8020189.08 | 76.17 |
| ${}^{241}$Np | 241 | 148 | 25.1433 | -986170674.02 | 226337.3665 | +7984934.96 | 445.37 |
| ${}^{242}$Np | 242 | 149 | 31.6379 | -982645952.05 | 227270.4373 | +7945074.40 | 887.01 |
| ${}^{243}$Np | 243 | 150 | 38.1254 | -979152998.16 | 228203.5153 | +7908748.24 | 139.88 |
| ${}^{244}$Np | 244 | 151 | 44.6058 | -975670646.21 | 229136.6002 | +7868115.92 | 438.40 |
| ${}^{245}$Np | 245 | 152 | 51.0793 | -972223955.32 | 230069.6922 | +7831486.42 | 877.30 |

### Plutonium (Z = 94)

_27 of 27 isotopes with a framework prediction; 27 of 27 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{221}$Pu | 221 | 127 | -130.8085 | -1078127441.89 | 207701.2275 | +8767046.67 | 1456.76 |
| ${}^{222}$Pu | 222 | 128 | -124.1242 | -1073742794.96 | 208634.1086 | +8738511.74 | 1450.20 |
| ${}^{223}$Pu | 223 | 129 | -117.4487 | -1069482302.45 | 209566.9986 | +8700899.71 | 1443.70 |
| ${}^{224}$Pu | 224 | 130 | -110.7820 | -1065194116.85 | 210499.8973 | +8672854.76 | 1437.26 |
| ${}^{225}$Pu | 225 | 131 | -104.1240 | -1061027725.78 | 211432.8047 | +8636149.44 | 1430.86 |
| ${}^{226}$Pu | 226 | 132 | -97.4745 | -1056840166.74 | 212365.7206 | +8607908.63 | 951.17 |
| ${}^{227}$Pu | 227 | 133 | -90.8335 | -1052755147.06 | 213298.6451 | +8571320.70 | 471.28 |
| ${}^{228}$Pu | 228 | 134 | -84.2010 | -1048653872.67 | 214231.5779 | +8543650.00 | 109.93 |
| ${}^{229}$Pu | 229 | 135 | -77.5767 | -1044651143.21 | 215164.5191 | +8507046.22 | 284.19 |
| ${}^{230}$Pu | 230 | 136 | -70.9607 | -1040643498.02 | 216097.4685 | +8479034.96 | 67.44 |
| ${}^{231}$Pu | 231 | 137 | -64.3529 | -1036717978.90 | 217030.4261 | +8442685.98 | 102.51 |
| ${}^{232}$Pu | 232 | 138 | -57.7531 | -1032802237.52 | 217963.3917 | +8412865.45 | 78.12 |
| ${}^{233}$Pu | 233 | 139 | -51.1613 | -1028953347.23 | 218896.3654 | +8375726.04 | 249.58 |
| ${}^{234}$Pu | 234 | 140 | -44.5774 | -1025116889.21 | 219829.3469 | +8345382.72 | 31.18 |
| ${}^{235}$Pu | 235 | 141 | -38.0014 | -1021336650.94 | 220762.3363 | +8308267.87 | 93.73 |
| ${}^{236}$Pu | 236 | 142 | -31.4331 | -1017576199.63 | 221695.3334 | +8276608.14 | 8.23 |
| ${}^{237}$Pu | 237 | 143 | -24.8725 | -1013862175.93 | 222628.3383 | +8238533.78 | 7.68 |
| ${}^{238}$Pu | 238 | 144 | -18.3195 | -1010170328.13 | 223561.3507 | +8205900.68 | 5.13 |
| ${}^{239}$Pu | 239 | 145 | -11.7741 | -1006516109.47 | 224494.3707 | +8167446.36 | 4.99 |
| ${}^{240}$Pu | 240 | 146 | -5.2361 | -1002887361.64 | 225427.3981 | +8133350.02 | 4.94 |
| ${}^{241}$Pu | 241 | 147 | 1.2945 | -999288227.88 | 226360.4330 | +8093766.33 | 4.92 |
| ${}^{242}$Pu | 242 | 148 | 7.8178 | -995716304.48 | 227293.4751 | +8059318.12 | 5.52 |
| ${}^{243}$Pu | 243 | 149 | 14.3338 | -992167499.21 | 228226.5245 | +8019505.29 | 11.22 |
| ${}^{244}$Pu | 244 | 150 | 20.8426 | -988648180.16 | 229159.5812 | +7984424.03 | 10.32 |
| ${}^{245}$Pu | 245 | 151 | 27.3443 | -985145078.12 | 230092.6449 | +7943829.47 | 59.66 |
| ${}^{246}$Pu | 246 | 152 | 33.8389 | -981675112.58 | 231025.7157 | +7908678.05 | 65.38 |
| ${}^{247}$Pu | 247 | 153 | 40.3266 | -978210944.20 | 231958.7934 | +7866841.39 | 870.18 |

### Americium (Z = 95)

_27 of 27 isotopes with a framework prediction; 27 of 27 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{223}$Am | 223 | 128 | -142.0765 | -1084419553.72 | 209590.8440 | +8783728.84 | 1443.65 |
| ${}^{224}$Am | 224 | 129 | -135.3777 | -1080090763.07 | 210523.7107 | +8748390.09 | 1914.78 |
| ${}^{225}$Am | 225 | 130 | -128.6878 | -1075724330.18 | 211456.5862 | +8720292.56 | 1906.28 |
| ${}^{226}$Am | 226 | 131 | -122.0067 | -1071484704.81 | 212389.4704 | +8685541.61 | 1424.49 |
| ${}^{227}$Am | 227 | 132 | -115.3342 | -1067224143.71 | 213322.3634 | +8657668.47 | 946.95 |
| ${}^{228}$Am | 228 | 133 | -108.6703 | -1063070533.52 | 214255.2649 | +8623149.26 | 942.79 |
| ${}^{229}$Am | 229 | 134 | -102.0149 | -1058905877.08 | 215188.1749 | +8595301.32 | 498.46 |
| ${}^{230}$Am | 230 | 135 | -95.3679 | -1054832449.04 | 216121.0934 | +8561329.56 | 665.08 |
| ${}^{231}$Am | 231 | 136 | -88.7292 | -1050767803.69 | 217054.0201 | +8533096.77 | 1393.66 |
| ${}^{232}$Am | 232 | 137 | -82.0988 | -1046784002.66 | 217986.9551 | +8498278.47 | 1387.65 |
| ${}^{233}$Am | 233 | 138 | -75.4766 | -1042808743.75 | 218919.8983 | +8469115.17 | 527.79 |
| ${}^{234}$Am | 234 | 139 | -68.8624 | -1038905841.74 | 219852.8496 | +8434171.49 | 734.89 |
| ${}^{235}$Am | 235 | 140 | -62.2563 | -1035018464.06 | 220785.8088 | +8404227.77 | 241.06 |
| ${}^{236}$Am | 236 | 141 | -55.6580 | -1031191521.43 | 221718.7760 | +8368827.99 | 538.02 |
| ${}^{237}$Am | 237 | 142 | -49.0677 | -1027382159.29 | 222651.7511 | +8337814.60 | 269.99 |
| ${}^{238}$Am | 238 | 143 | -42.4851 | -1023626049.13 | 223584.7339 | +8301084.35 | 265.67 |
| ${}^{239}$Am | 239 | 144 | -35.9102 | -1019891168.36 | 224517.7244 | +8268692.20 | 8.90 |
| ${}^{240}$Am | 240 | 145 | -29.3429 | -1016200054.10 | 225450.7226 | +8231415.41 | 61.86 |
| ${}^{241}$Am | 241 | 146 | -22.7832 | -1012532477.65 | 226383.7283 | +8197605.14 | 4.96 |
| ${}^{242}$Am | 242 | 147 | -16.2309 | -1008901137.39 | 227316.7415 | +8159147.20 | 4.95 |
| ${}^{243}$Am | 243 | 148 | -9.6861 | -1005293446.00 | 228249.7621 | +8124720.23 | 6.13 |
| ${}^{244}$Am | 244 | 149 | -3.1486 | -1001715693.73 | 229182.7900 | +8086186.68 | 6.56 |
| ${}^{245}$Am | 245 | 150 | 3.3816 | -998163440.27 | 230115.8252 | +8051015.75 | 8.26 |
| ${}^{246}$Am | 246 | 151 | 9.9046 | -994635248.81 | 231048.8677 | +8011446.74 | 77.21 |
| ${}^{247}$Am | 247 | 152 | 16.4204 | -991134890.20 | 231981.9172 | +7976322.72 | 433.07 |
| ${}^{248}$Am | 248 | 153 | 22.9292 | -987651059.77 | 232914.9739 | +7936060.53 | 866.67 |
| ${}^{249}$Am | 249 | 154 | 29.4310 | -984196178.34 | 233848.0375 | +7899924.35 | 1284.74 |

### Curium (Z = 96)

_22 of 22 isotopes with a framework prediction; 22 of 22 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{231}$Cm | 231 | 135 | -113.3376 | -1065054248.34 | 217077.8462 | +8621029.11 | 1393.63 |
| ${}^{232}$Cm | 232 | 136 | -106.6763 | -1060918327.93 | 218010.7503 | +8594773.06 | 930.83 |
| ${}^{233}$Cm | 233 | 137 | -100.0233 | -1056888978.55 | 218943.6627 | +8559962.96 | 373.56 |
| ${}^{234}$Cm | 234 | 138 | -93.3785 | -1052849942.04 | 219876.5833 | +8532574.25 | 78.33 |
| ${}^{235}$Cm | 235 | 139 | -86.7419 | -1048908765.82 | 220809.5121 | +8496877.44 | 467.98 |
| ${}^{236}$Cm | 236 | 140 | -80.1134 | -1044960223.92 | 221742.4491 | +8468182.07 | 80.20 |
| ${}^{237}$Cm | 237 | 141 | -73.4929 | -1041090792.54 | 222675.3940 | +8432661.78 | 336.93 |
| ${}^{238}$Cm | 238 | 142 | -66.8804 | -1037229759.18 | 223608.3469 | +8402916.32 | 55.17 |
| ${}^{239}$Cm | 239 | 143 | -60.2757 | -1033434646.05 | 224541.3077 | +8366645.73 | 673.93 |
| ${}^{240}$Cm | 240 | 144 | -53.6789 | -1029652131.35 | 225474.2762 | +8335783.43 | 8.52 |
| ${}^{241}$Cm | 241 | 145 | -47.0897 | -1025925020.12 | 226407.2525 | +8298923.78 | 7.16 |
| ${}^{242}$Cm | 242 | 146 | -40.5082 | -1022216352.33 | 227340.2364 | +8266318.72 | 5.06 |
| ${}^{243}$Cm | 243 | 147 | -33.9342 | -1018553001.40 | 228273.2279 | +8228332.14 | 6.60 |
| ${}^{244}$Cm | 244 | 148 | -27.3678 | -1014907466.45 | 229206.2268 | +8195605.73 | 4.86 |
| ${}^{245}$Cm | 245 | 149 | -20.8088 | -1011300742.22 | 230139.2332 | +8157513.99 | 5.03 |
| ${}^{246}$Cm | 246 | 150 | -14.2571 | -1007715628.62 | 231072.2470 | +8123900.48 | 6.65 |
| ${}^{247}$Cm | 247 | 151 | -7.7127 | -1004162349.04 | 232005.2681 | +8084880.22 | 16.50 |
| ${}^{248}$Cm | 248 | 152 | -1.1756 | -1000632313.27 | 232938.2963 | +8050815.85 | 10.20 |
| ${}^{249}$Cm | 249 | 153 | 5.3544 | -997127315.99 | 233871.3318 | +8010546.76 | 10.22 |
| ${}^{250}$Cm | 250 | 154 | 11.8773 | -993647599.29 | 234804.3743 | +7975473.53 | 44.10 |
| ${}^{251}$Cm | 251 | 155 | 18.3932 | -990185842.21 | 235737.4238 | +7934592.88 | 97.05 |
| ${}^{252}$Cm | 252 | 156 | 24.9021 | -986753641.25 | 236670.4803 | +7899434.86 | 1269.41 |

### Berkelium (Z = 97)

_22 of 22 isotopes with a framework prediction; 22 of 22 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{233}$Bk | 233 | 136 | -124.8013 | -1071236606.98 | 218967.6584 | +8645048.03 | 1072.70 |
| ${}^{234}$Bk | 234 | 137 | -118.1256 | -1067137974.41 | 219900.5481 | +8611626.41 | 700.68 |
| ${}^{235}$Bk | 235 | 138 | -111.4583 | -1063037030.88 | 220833.4462 | +8584281.43 | 1829.35 |
| ${}^{236}$Bk | 236 | 139 | -104.7992 | -1059027580.73 | 221766.3526 | +8550801.09 | 1639.43 |
| ${}^{237}$Bk | 237 | 140 | -98.1483 | -1055018995.91 | 222699.2671 | +8522677.65 | 1041.94 |
| ${}^{238}$Bk | 238 | 141 | -91.5056 | -1051093304.25 | 223632.1897 | +8488739.35 | 1155.18 |
| ${}^{239}$Bk | 239 | 142 | -84.8708 | -1047177889.58 | 224565.1204 | +8459533.86 | 928.64 |
| ${}^{240}$Bk | 240 | 143 | -78.2440 | -1043335999.11 | 225498.0590 | +8424373.36 | 670.67 |
| ${}^{241}$Bk | 241 | 144 | -71.6251 | -1039500209.96 | 226431.0055 | +8394472.03 | 738.41 |
| ${}^{242}$Bk | 242 | 145 | -65.0140 | -1035729863.38 | 227363.9599 | +8358349.75 | 594.89 |
| ${}^{243}$Bk | 243 | 146 | -58.4106 | -1031975098.26 | 228296.9219 | +8326268.46 | 19.98 |
| ${}^{244}$Bk | 244 | 147 | -51.8149 | -1028270885.88 | 229229.8916 | +8289666.31 | 63.33 |
| ${}^{245}$Bk | 245 | 148 | -45.2267 | -1024582805.15 | 230162.8689 | +8257478.95 | 7.85 |
| ${}^{246}$Bk | 246 | 149 | -38.6461 | -1020938579.38 | 231095.8537 | +8220953.67 | 261.85 |
| ${}^{247}$Bk | 247 | 150 | -32.0729 | -1017315772.89 | 232028.8459 | +8187519.21 | 22.54 |
| ${}^{248}$Bk | 248 | 151 | -25.5071 | -1013730726.61 | 232961.8455 | +8149505.01 | 216.63 |
| ${}^{249}$Bk | 249 | 152 | -18.9486 | -1010165445.15 | 233894.8525 | +8115853.05 | 5.38 |
| ${}^{250}$Bk | 250 | 153 | -12.3974 | -1006633196.91 | 234827.8666 | +8076484.84 | 12.44 |
| ${}^{251}$Bk | 251 | 154 | -5.8533 | -1003122114.01 | 235760.8880 | +8041037.98 | 45.89 |
| ${}^{252}$Bk | 252 | 155 | 0.6837 | -999636274.38 | 236693.9164 | +8001480.42 | 852.89 |
| ${}^{253}$Bk | 253 | 156 | 7.2136 | -996173356.87 | 237626.9519 | +7966167.26 | 1521.22 |
| ${}^{254}$Bk | 254 | 157 | 13.7366 | -992731050.62 | 238559.9944 | +7926600.42 | 1259.39 |

### Californium (Z = 98)

_20 of 20 isotopes with a framework prediction; 20 of 20 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{237}$Cf | 237 | 139 | -123.0338 | -1069186444.56 | 222723.3703 | +8610233.96 | 440.84 |
| ${}^{238}$Cf | 238 | 140 | -116.3605 | -1065109826.31 | 223656.2624 | +8583375.08 | 1344.19 |
| ${}^{239}$Cf | 239 | 141 | -109.6954 | -1061139790.96 | 224589.1626 | +8549600.24 | 539.61 |
| ${}^{240}$Cf | 240 | 142 | -103.0383 | -1057165472.07 | 225522.0710 | +8521270.99 | 80.65 |
| ${}^{241}$Cf | 241 | 143 | -96.3894 | -1053277720.88 | 226454.9875 | +8486246.55 | 746.69 |
| ${}^{242}$Cf | 242 | 144 | -89.7483 | -1049388206.65 | 227387.9119 | +8457263.10 | 57.18 |
| ${}^{243}$Cf | 243 | 145 | -83.1152 | -1045574678.74 | 228320.8442 | +8421682.97 | 798.14 |
| ${}^{244}$Cf | 244 | 146 | -76.4899 | -1041769159.91 | 229253.7843 | +8391370.73 | 11.51 |
| ${}^{245}$Cf | 245 | 147 | -69.8724 | -1038027475.16 | 230186.7322 | +8355073.94 | 10.63 |
| ${}^{246}$Cf | 246 | 148 | -63.2625 | -1034292615.39 | 231119.6877 | +8324393.82 | 6.60 |
| ${}^{247}$Cf | 247 | 149 | -56.6602 | -1030613286.72 | 232052.6508 | +8288238.07 | 62.25 |
| ${}^{248}$Cf | 248 | 150 | -50.0654 | -1026949071.44 | 232985.6215 | +8256292.99 | 22.16 |
| ${}^{249}$Cf | 249 | 151 | -43.4781 | -1023333112.05 | 233918.5996 | +8218743.31 | 5.09 |
| ${}^{250}$Cf | 250 | 152 | -36.8982 | -1019731774.29 | 234851.5851 | +8186015.35 | 6.60 |
| ${}^{251}$Cf | 251 | 153 | -30.3256 | -1016172835.66 | 235784.5780 | +8147040.50 | 16.68 |
| ${}^{252}$Cf | 252 | 154 | -23.7603 | -1012629934.73 | 236717.5781 | +8112979.12 | 10.04 |
| ${}^{253}$Cf | 253 | 155 | -17.2021 | -1009120620.46 | 237650.5853 | +8073371.17 | 18.06 |
| ${}^{254}$Cf | 254 | 156 | -10.6511 | -1005629254.41 | 238583.5997 | +8039332.52 | 48.42 |
| ${}^{255}$Cf | 255 | 157 | -4.1072 | -1002165444.88 | 239516.6212 | +7999535.01 | 842.84 |
| ${}^{256}$Cf | 256 | 158 | 2.4298 | -998722911.54 | 240449.6497 | +7965299.47 | 1319.83 |

### Einsteinium (Z = 99)

_20 of 20 isotopes with a framework prediction; 20 of 20 with $M_{\mathrm{atom}}$ $M = N \cdot m_n + Z \cdot m_p + Z \cdot m_e - B$._

| Atom | $A$ | $N$ | Binding $B_q$ (MeV) | Binding Error (ppb) | Mass $M_{\mathrm{atom}}$ (MeV) | Mass Error (pred ppb) | Mass Error (exp ppb) |
|---|---|---|---|---|---|---|---|
| ${}^{239}$Es | 239 | 140 | -134.7494 | -1075364930.64 | 224613.4343 | +8634006.76 | 1346.90 |
| ${}^{240}$Es | 240 | 141 | -128.0618 | -1071326160.52 | 225546.3122 | +8601545.24 | 1637.03 |
| ${}^{241}$Es | 241 | 142 | -121.3825 | -1067289481.58 | 226479.1983 | +8573556.78 | 1028.75 |
| ${}^{242}$Es | 242 | 143 | -114.7113 | -1063345380.40 | 227412.0925 | +8540285.96 | 1140.17 |
| ${}^{243}$Es | 243 | 144 | -108.0481 | -1059396521.17 | 228344.9947 | +8511614.85 | 913.32 |
| ${}^{244}$Es | 244 | 145 | -101.3929 | -1055531829.31 | 229277.9050 | +8477296.85 | 798.95 |
| ${}^{245}$Es | 245 | 146 | -94.7456 | -1051665569.99 | 230210.8231 | +8447663.94 | 726.32 |
| ${}^{246}$Es | 246 | 147 | -88.1062 | -1047876674.65 | 231143.7491 | +8412964.41 | 392.31 |
| ${}^{247}$Es | 247 | 148 | -81.4745 | -1044097815.37 | 232076.6828 | +8381840.94 | 84.47 |
| ${}^{248}$Es | 248 | 149 | -74.8504 | -1040371359.26 | 233009.6242 | +8346808.66 | 225.74 |
| ${}^{249}$Es | 249 | 150 | -68.2340 | -1036664740.42 | 233942.5732 | +8315763.01 | 128.47 |
| ${}^{250}$Es | 250 | 151 | -61.6252 | -1033003173.83 | 234875.5298 | +8279910.05 | 427.87 |
| ${}^{251}$Es | 251 | 152 | -55.0238 | -1029362670.18 | 235808.4938 | +8247674.38 | 22.61 |
| ${}^{252}$Es | 252 | 153 | -48.4298 | -1025771160.77 | 236741.4652 | +8209297.87 | 213.17 |
| ${}^{253}$Es | 253 | 154 | -41.8432 | -1022191135.67 | 237674.4440 | +8175820.48 | 5.30 |
| ${}^{254}$Es | 254 | 155 | -35.2638 | -1018651505.52 | 238607.4301 | +8137237.68 | 12.41 |
| ${}^{255}$Es | 255 | 156 | -28.6917 | -1015127584.96 | 239540.4234 | +8102758.55 | 45.52 |
| ${}^{256}$Es | 256 | 157 | -22.1266 | -1011635994.27 | 240473.4238 | +8064350.32 | 417.82 |
| ${}^{257}$Es | 257 | 158 | -15.5687 | -1008162029.66 | 241406.4312 | +8029962.85 | 1715.31 |
| ${}^{258}$Es | 258 | 159 | -9.0178 | -1004715678.51 | 242339.4457 | +7991345.25 | 1666.02 |

<!-- AUTO:per-z-sections END -->
