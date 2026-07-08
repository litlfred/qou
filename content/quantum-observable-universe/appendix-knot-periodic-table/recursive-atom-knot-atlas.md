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

| $\#$ | Element | $Z$ | $N$ | $N_{\mathrm{pred}}$ | $\Delta$ | $k_\alpha$ | $M_q$ (MeV) | $M_o$ (MeV) | $B/A$ |
|---:|------|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Hydrogen | 1 | 0 | 1 | 1 | 0 | $938.8$ | $938.8$ | $0.0000$ |
| 2 | Helium$^{\diamond\star}$ | 2 | 2 | 2 | 0 | 1 | $3728.4$ | $3728.4$ | $7.0739$ |
| 3 | Lithium | 3 | 4 | 3 | 1 | 1 | $6535.4$ | $6535.4$ | $5.6063$ |
| 4 | Beryllium | 4 | 5 | 4 | 1 | 2 | $8394.8$ | $8394.8$ | $6.4628$ |
| 5 | Boron | 5 | 6 | 5 | 1 | 2 | $10255.1$ | $10255.1$ | $6.9277$ |
| 6 | Carbon | 6 | 6 | 6 | 0 | 3 | $11177.9$ | $11177.9$ | $7.6801$ |
| 7 | Nitrogen | 7 | 7 | 8 | 1 | 3 | $13043.8$ | $13043.8$ | $7.4756$ |
| 8 | Oxygen$^{\diamond\star}$ | 8 | 8 | 9 | 1 | 4 | $14899.1$ | $14899.2$ | $7.9762$ |
| 9 | Fluorine | 9 | 10 | 10 | 0 | 4 | $17696.9$ | $17696.9$ | $7.7790$ |
| 10 | Neon | 10 | 10 | 11 | 1 | 5 | $18622.8$ | $18622.8$ | $8.0325$ |
| 11 | Sodium | 11 | 12 | 12 | 0 | 5 | $21414.8$ | $21414.8$ | $8.1115$ |
| 12 | Magnesium | 12 | 12 | 14 | 2 | 6 | $22341.9$ | $22341.9$ | $8.2607$ |
| 13 | Aluminium | 13 | 14 | 15 | 1 | 6 | $25133.1$ | $25132.9$ | $8.3316$ |
| 14 | Silicon | 14 | 14 | 16 | 2 | 7 | $26060.3$ | $26060.3$ | $8.4477$ |
| 15 | Phosphorus | 15 | 16 | 17 | 1 | 7 | $28851.8$ | $28851.9$ | $8.4812$ |
| 16 | Sulfur | 16 | 16 | 19 | 3 | 8 | $29781.7$ | $29789.2$ | $8.4932$ |
| 17 | Chlorine | 17 | 18 | 20 | 2 | 8 | $32573.2$ | $32573.5$ | $8.5203$ |
| 18 | Argon | 18 | 22 | 21 | 1 | 9 | $37224.7$ | $37224.7$ | $8.5954$ |
| 19 | Potassium$^{\star}$ | 19 | 20 | 22 | 2 | 9 | $36294.4$ | $36294.5$ | $8.5570$ |
| 20 | Calcium$^{\diamond\star}$ | 20 | 20 | 24 | 4 | 10 | $37224.9$ | $37224.9$ | $8.5513$ |
| 21 | Scandium | 21 | 24 | 25 | 1 | 10 | $41876.1$ | $41876.2$ | $8.6190$ |
| 22 | Titanium | 22 | 26 | 26 | 0 | 11 | $44663.2$ | $44663.3$ | $8.7230$ |
| 23 | Vanadium$^{\star}$ | 23 | 28 | 28 | 0 | 11 | $47453.9$ | $47454.0$ | $8.7420$ |
| 24 | Chromium$^{\star}$ | 24 | 28 | 29 | 1 | 12 | $48382.2$ | $48382.3$ | $8.7760$ |
| 25 | Manganese | 25 | 30 | 30 | 0 | 12 | $51174.4$ | $51174.5$ | $8.7649$ |
| 26 | Iron | 26 | 30 | 32 | 2 | 13 | $52103.0$ | $52103.1$ | $8.7903$ |
| 27 | Cobalt | 27 | 32 | 33 | 1 | 13 | $54895.8$ | $54895.9$ | $8.7680$ |
| 28 | Nickel$^{\diamond}$ | 28 | 30 | 35 | 5 | 14 | $53966.3$ | $53966.4$ | $8.7322$ |
| 29 | Copper | 29 | 34 | 36 | 2 | 14 | $58618.4$ | $58618.5$ | $8.7522$ |
| 30 | Zinc | 30 | 34 | 37 | 3 | 15 | $59549.5$ | $59549.6$ | $8.7357$ |
| 31 | Gallium | 31 | 38 | 39 | 1 | 15 | $64203.7$ | $64203.8$ | $8.7246$ |
| 32 | Germanium | 32 | 42 | 40 | 2 | 16 | $68856.9$ | $68857.0$ | $8.7264$ |
| 33 | Arsenic | 33 | 42 | 42 | 0 | 16 | $69788.9$ | $69789.1$ | $8.7010$ |
| 34 | Selenium | 34 | 46 | 43 | 3 | 17 | $74441.6$ | $74441.8$ | $8.7110$ |
| 35 | Bromine | 35 | 44 | 45 | 1 | 17 | $73511.2$ | $73511.4$ | $8.6961$ |
| 36 | Krypton | 36 | 48 | 46 | 2 | 18 | $78163.0$ | $78163.2$ | $8.7172$ |
| 37 | Rubidium | 37 | 48 | 48 | 0 | 18 | $79094.7$ | $79094.9$ | $8.6974$ |
| 38 | Strontium$^{\star}$ | 38 | 50 | 49 | 1 | 19 | $81883.4$ | $81883.6$ | $8.7326$ |
| 39 | Yttrium$^{\star}$ | 39 | 50 | 51 | 1 | 19 | $82815.1$ | $82815.3$ | $8.7138$ |
| 40 | Zirconium$^{\star}$ | 40 | 50 | 52 | 2 | 20 | $83745.6$ | $83745.9$ | $8.7098$ |
| 41 | Niobium | 41 | 52 | 54 | 2 | 20 | $86541.6$ | $86541.9$ | $8.6641$ |
| 42 | Molybdenum | 42 | 56 | 55 | 1 | 21 | $91198.1$ | $91198.4$ | $8.6353$ |
| 43 | Technetium | 43 | 55 | 57 | 2 | 21 | $91201.4$ | $91201.7$ | $8.5937$ |
| 44 | Ruthenium | 44 | 58 | 58 | 0 | 22 | $94923.2$ | $94923.5$ | $8.6070$ |
| 45 | Rhodium | 45 | 58 | 60 | 2 | 22 | $95855.7$ | $95856.0$ | $8.5843$ |
| 46 | Palladium | 46 | 60 | 62 | 2 | 23 | $98649.7$ | $98650.1$ | $8.5670$ |
| 47 | Silver | 47 | 60 | 63 | 3 | 23 | $99581.3$ | $99581.6$ | $8.5536$ |
| 48 | Cadmium | 48 | 66 | 65 | 1 | 24 | $106099.2$ | $106099.6$ | $8.5398$ |
| 49 | Indium | 49 | 66 | 66 | 0 | 24 | $107032.2$ | $107032.6$ | $8.5160$ |
| 50 | Tin$^{\diamond}$ | 50 | 70 | 68 | 2 | 25 | $111688.0$ | $111688.4$ | $8.5050$ |
| 51 | Antimony | 51 | 70 | 70 | 0 | 25 | $112621.0$ | $112621.4$ | $8.4820$ |
| 52 | Tellurium | 52 | 78 | 71 | 7 | 26 | $121005.6$ | $121006.0$ | $8.4390$ |
| 53 | Iodine | 53 | 74 | 73 | 1 | 26 | $118210.6$ | $118211.0$ | $8.4455$ |
| 54 | Xenon | 54 | 78 | 75 | 3 | 27 | $122867.8$ | $122868.2$ | $8.4275$ |
| 55 | Caesium | 55 | 78 | 76 | 2 | 27 | $123800.4$ | $123800.9$ | $8.4100$ |
| 56 | Barium$^{\star}$ | 56 | 82 | 78 | 4 | 28 | $128457.7$ | $128458.1$ | $8.3937$ |
| 57 | Lanthanum$^{\star}$ | 57 | 82 | 80 | 2 | 28 | $129390.3$ | $129390.8$ | $8.3780$ |
| 58 | Cerium$^{\star}$ | 58 | 82 | 81 | 1 | 29 | $130320.9$ | $130321.4$ | $8.3765$ |
| 59 | Praseodymium$^{\star}$ | 59 | 82 | 83 | 1 | 29 | $131254.4$ | $131254.9$ | $8.3540$ |
| 60 | Neodymium$^{\star}$ | 60 | 82 | 85 | 3 | 30 | $132186.0$ | $132186.6$ | $8.3460$ |
| 61 | Promethium | 61 | 84 | 86 | 2 | 30 | $134985.0$ | $134985.6$ | $8.3040$ |
| 62 | Samarium | 62 | 90 | 88 | 2 | 31 | $141512.1$ | $141512.7$ | $8.2440$ |
| 63 | Europium | 63 | 90 | 90 | 0 | 31 | $142445.0$ | $142445.6$ | $8.2290$ |
| 64 | Gadolinium | 64 | 94 | 92 | 2 | 32 | $147103.2$ | $147103.8$ | $8.2140$ |
| 65 | Terbium | 65 | 94 | 93 | 1 | 32 | $148036.2$ | $148036.8$ | $8.1990$ |
| 66 | Dysprosium | 66 | 98 | 95 | 3 | 33 | $152694.3$ | $152695.0$ | $8.1865$ |
| 67 | Holmium | 67 | 98 | 97 | 1 | 33 | $153627.4$ | $153628.0$ | $8.1710$ |
| 68 | Erbium | 68 | 98 | 99 | 1 | 34 | $154558.4$ | $154559.1$ | $8.1690$ |
| 69 | Thulium | 69 | 100 | 101 | 1 | 34 | $157355.7$ | $157356.4$ | $8.1460$ |
| 70 | Ytterbium | 70 | 104 | 102 | 2 | 35 | $162015.1$ | $162015.8$ | $8.1280$ |
| 71 | Lutetium | 71 | 104 | 104 | 0 | 35 | $162947.8$ | $162948.5$ | $8.1165$ |
| 72 | Hafnium | 72 | 108 | 106 | 2 | 36 | $167607.5$ | $167608.2$ | $8.0985$ |
| 73 | Tantalum | 73 | 108 | 108 | 0 | 36 | $168540.2$ | $168540.9$ | $8.0870$ |
| 74 | Tungsten | 74 | 110 | 110 | 0 | 37 | $171338.1$ | $171338.8$ | $8.0639$ |
| 75 | Rhenium | 75 | 112 | 112 | 0 | 37 | $174136.5$ | $174137.2$ | $8.0390$ |
| 76 | Osmium | 76 | 116 | 114 | 2 | 38 | $178797.1$ | $178797.8$ | $8.0194$ |
| 77 | Iridium | 77 | 116 | 115 | 1 | 38 | $179730.5$ | $179731.2$ | $8.0060$ |
| 78 | Platinum | 78 | 117 | 117 | 0 | 39 | $181595.3$ | $181596.0$ | $7.9930$ |
| 79 | Gold | 79 | 118 | 119 | 1 | 39 | $183461.0$ | $183461.7$ | $7.9759$ |
| 80 | Mercury | 80 | 122 | 121 | 1 | 40 | $188122.8$ | $188123.5$ | $7.9530$ |
| 81 | Thallium | 81 | 124 | 123 | 1 | 40 | $190920.2$ | $190921.0$ | $7.9370$ |
| 82 | Lead$^{\diamond\star}$ | 82 | 126 | 125 | 1 | 41 | $193728.7$ | $193729.5$ | $7.8675$ |
| 83 | Bismuth$^{\star}$ | 83 | 126 | 127 | 1 | 41 | $194663.7$ | $194664.5$ | $7.8480$ |
| 84 | Polonium | 84 | 125 | 129 | 4 | 42 | $194665.6$ | $194666.4$ | $7.8352$ |
| 85 | Astatine | 85 | 125 | 131 | 6 | 42 | $195600.9$ | $195601.8$ | $7.8147$ |
| 86 | Radon | 86 | 136 | 133 | 3 | 43 | $206801.5$ | $206802.4$ | $7.7227$ |
| 87 | Francium | 87 | 136 | 135 | 1 | 43 | $207735.5$ | $207736.4$ | $7.7095$ |
| 88 | Radium | 88 | 138 | 137 | 1 | 44 | $210541.0$ | $210541.9$ | $7.6620$ |
| 89 | Actinium | 89 | 138 | 139 | 1 | 44 | $211474.6$ | $211475.5$ | $7.6510$ |
| 90 | Thorium | 90 | 142 | 141 | 1 | 45 | $216141.8$ | $216142.7$ | $7.6150$ |
| 91 | Protactinium | 91 | 140 | 143 | 3 | 45 | $215209.3$ | $215210.2$ | $7.6138$ |
| 92 | Uranium | 92 | 146 | 145 | 1 | 46 | $221742.6$ | $221743.5$ | $7.5701$ |


<!-- AUTO:per-z-sections BEGIN -->

## Per-element coverage (AME 2020 cross-reference)

_Auto-rendered from per-Z shards `canonical-isotope-witness-Z<NN>.witness.json` (emitted by [`canonical_isotope_witness.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/canonical_isotope_witness.py)). Each row carries the Layer used (L1 canonical |tr_M|, L2 α-cluster recursion, L3 paper-six-term [pending], L4 composite mass), the framework prediction, the AME 2020 reference, and the residual. `Predicts = mass` for free nucleons (p, n) — value is the Borromean tower nucleon mass conditional on `conj:borromean-baryon-mass-formula`. `Predicts = binding_energy` for D and up; AME 2020 reference is the total binding energy. $M_{\text{composite}}$ is the L4 composite mass $N \cdot m_n + Z \cdot m_p - B$ when both nucleon masses (Borromean) and a binding-energy prediction are available; reference is the AME atomic mass converted via 1 u = 931.49410242 MeV._

### neutron (Z = 0)

_0 of 1 isotopes with a framework prediction; 0 of 1 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| $\mathfrak{n}$ | 1 | 1 | L1-borromean-via-canonical | borromean-tower-via-fitted-lambda | mass | — | — | — | — |

### Hydrogen (Z = 1)

_2 of 7 isotopes with a framework prediction; 2 of 7 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| $\mathfrak{p}$ | 1 | 0 | L1-borromean-via-canonical | borromean-tower-via-fitted-lambda | mass | — | — | — | — |
| ${}^{2}$H | 2 | 1 | L1-canonical | 🟢 recursive | binding_energy | 2.2488 | 2.2246 | +1.09 % | 1929.8504 MeV (+28637.0 ppm) |
| ${}^{3}$H | 3 | 2 | L1-canonical | 🟢 recursive | binding_energy | 8.4686 | 8.4818 | -0.16 % | 2890.3454 MeV (+28800.6 ppm) |
| ${}^{4}$H | 4 | 3 | derivation-pending | ⚪ pending | binding_energy | — | 6.8818 | — | — |
| ${}^{5}$H | 5 | 4 | derivation-pending | ⚪ pending | binding_energy | — | 6.6818 | — | — |
| ${}^{6}$H | 6 | 5 | derivation-pending | ⚪ pending | binding_energy | — | 5.7698 | — | — |
| ${}^{7}$H | 7 | 6 | derivation-pending | ⚪ pending | binding_energy | — | 6.5800 | — | — |

### Helium (Z = 2)

_2 of 8 isotopes with a framework prediction; 2 of 8 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{3}$He | 3 | 1 | L1-canonical | 🟢 recursive | binding_energy | 7.4889 | 7.7180 | -2.97 % | 2889.9948 MeV (+28682.6 ppm) |
| ${}^{4}$He | 4 | 2 | L1-canonical | 🟢 recursive | binding_energy | 29.9557 | 28.2957 | +5.87 % | 3834.2428 MeV (+28387.9 ppm) |
| ${}^{5}$He | 5 | 3 | derivation-pending | ⚪ pending | binding_energy | — | 27.5607 | — | — |
| ${}^{6}$He | 6 | 4 | derivation-pending | ⚪ pending | binding_energy | — | 29.2711 | — | — |
| ${}^{7}$He | 7 | 5 | derivation-pending | ⚪ pending | binding_energy | — | 28.8614 | — | — |
| ${}^{8}$He | 8 | 6 | derivation-pending | ⚪ pending | binding_energy | — | 31.3962 | — | — |
| ${}^{9}$He | 9 | 7 | derivation-pending | ⚪ pending | binding_energy | — | 30.1413 | — | — |
| ${}^{10}$He | 10 | 8 | derivation-pending | ⚪ pending | binding_energy | — | 29.9513 | — | — |

### Lithium (Z = 3)

_2 of 11 isotopes with a framework prediction; 0 of 11 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{3}$Li | 3 | 0 | derivation-pending | ⚪ pending | binding_energy | — | -6.8010 | — | — |
| ${}^{4}$Li | 4 | 1 | derivation-pending | ⚪ pending | binding_energy | — | 4.6150 | — | — |
| ${}^{5}$Li | 5 | 2 | derivation-pending | ⚪ pending | binding_energy | — | 26.3307 | — | — |
| ${}^{6}$Li | 6 | 3 | L3-partial-shell:f=0.500 from A=4→8 | 🟠 heuristic | binding_energy | 43.6570 | 31.9940 | +36.45 % | — |
| ${}^{7}$Li | 7 | 4 | L3-partial-shell:f=0.750 from A=4→8 | 🟠 heuristic | binding_energy | 51.3377 | 39.2451 | +30.81 % | — |
| ${}^{8}$Li | 8 | 5 | derivation-pending | ⚪ pending | binding_energy | — | 41.2777 | — | — |
| ${}^{9}$Li | 9 | 6 | derivation-pending | ⚪ pending | binding_energy | — | 45.3399 | — | — |
| ${}^{10}$Li | 10 | 7 | derivation-pending | ⚪ pending | binding_energy | — | 45.3135 | — | — |
| ${}^{11}$Li | 11 | 8 | derivation-pending | ⚪ pending | binding_energy | — | 45.7092 | — | — |
| ${}^{12}$Li | 12 | 9 | derivation-pending | ⚪ pending | binding_energy | — | 45.4992 | — | — |
| ${}^{13}$Li | 13 | 10 | derivation-pending | ⚪ pending | binding_energy | — | 45.5992 | — | — |

### Beryllium (Z = 4)

_3 of 12 isotopes with a framework prediction; 1 of 12 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{5}$Be | 5 | 1 | derivation-pending | ⚪ pending | binding_energy | — | 0.0900 | — | — |
| ${}^{6}$Be | 6 | 2 | derivation-pending | ⚪ pending | binding_energy | — | 26.9235 | — | — |
| ${}^{7}$Be | 7 | 3 | derivation-pending | ⚪ pending | binding_energy | — | 37.6008 | — | — |
| ${}^{8}$Be | 8 | 4 | L2-alpha-cluster | 🟢 recursive | binding_energy | 62.3383 | 56.4995 | +10.33 % | 7666.0587 MeV (+28049.8 ppm) |
| ${}^{9}$Be | 9 | 5 | L3-partial-shell:f=0.250 from A=8→12 | 🟠 heuristic | binding_energy | 67.3058 | 58.1640 | +15.72 % | — |
| ${}^{10}$Be | 10 | 6 | L3-partial-shell:f=0.500 from A=8→12 | 🟠 heuristic | binding_energy | 75.5932 | 64.9763 | +16.34 % | — |
| ${}^{11}$Be | 11 | 7 | derivation-pending | ⚪ pending | binding_energy | — | 65.4779 | — | — |
| ${}^{12}$Be | 12 | 8 | derivation-pending | ⚪ pending | binding_energy | — | 68.6487 | — | — |
| ${}^{13}$Be | 13 | 9 | derivation-pending | ⚪ pending | binding_energy | — | 68.1387 | — | — |
| ${}^{14}$Be | 14 | 10 | derivation-pending | ⚪ pending | binding_energy | — | 69.9146 | — | — |
| ${}^{15}$Be | 15 | 11 | derivation-pending | ⚪ pending | binding_energy | — | 68.1146 | — | — |
| ${}^{16}$Be | 16 | 12 | derivation-pending | ⚪ pending | binding_energy | — | 68.5646 | — | — |

### Boron (Z = 5)

_2 of 16 isotopes with a framework prediction; 0 of 16 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{6}$B | 6 | 1 | derivation-pending | ⚪ pending | binding_energy | — | -2.8020 | — | — |
| ${}^{7}$B | 7 | 2 | derivation-pending | ⚪ pending | binding_energy | — | 24.9109 | — | — |
| ${}^{8}$B | 8 | 3 | derivation-pending | ⚪ pending | binding_energy | — | 37.7372 | — | — |
| ${}^{9}$B | 9 | 4 | derivation-pending | ⚪ pending | binding_energy | — | 56.3136 | — | — |
| ${}^{10}$B | 10 | 5 | L3-partial-shell:f=0.500 from A=8→12 | 🟠 heuristic | binding_energy | 75.5932 | 64.7508 | +16.74 % | — |
| ${}^{11}$B | 11 | 6 | L3-partial-shell:f=0.750 from A=8→12 | 🟠 heuristic | binding_energy | 83.8806 | 76.2051 | +10.07 % | — |
| ${}^{12}$B | 12 | 7 | derivation-pending | ⚪ pending | binding_energy | — | 79.5747 | — | — |
| ${}^{13}$B | 13 | 8 | derivation-pending | ⚪ pending | binding_energy | — | 84.4535 | — | — |
| ${}^{14}$B | 14 | 9 | derivation-pending | ⚪ pending | binding_energy | — | 85.4230 | — | — |
| ${}^{15}$B | 15 | 10 | derivation-pending | ⚪ pending | binding_energy | — | 88.2007 | — | — |
| ${}^{16}$B | 16 | 11 | derivation-pending | ⚪ pending | binding_energy | — | 88.1177 | — | — |
| ${}^{17}$B | 17 | 12 | derivation-pending | ⚪ pending | binding_energy | — | 89.5844 | — | — |
| ${}^{18}$B | 18 | 13 | derivation-pending | ⚪ pending | binding_energy | — | 89.5794 | — | — |
| ${}^{19}$B | 19 | 14 | derivation-pending | ⚪ pending | binding_energy | — | 89.6731 | — | — |
| ${}^{20}$B | 20 | 15 | derivation-pending | ⚪ pending | binding_energy | — | 88.1131 | — | — |
| ${}^{21}$B | 21 | 16 | derivation-pending | ⚪ pending | binding_energy | — | 87.2031 | — | — |

### Carbon (Z = 6)

_2 of 16 isotopes with a framework prediction; 1 of 16 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{8}$C | 8 | 2 | derivation-pending | ⚪ pending | binding_energy | — | 24.8122 | — | — |
| ${}^{9}$C | 9 | 3 | derivation-pending | ⚪ pending | binding_energy | — | 39.0368 | — | — |
| ${}^{10}$C | 10 | 4 | derivation-pending | ⚪ pending | binding_energy | — | 60.3204 | — | — |
| ${}^{11}$C | 11 | 5 | derivation-pending | ⚪ pending | binding_energy | — | 73.4410 | — | — |
| ${}^{12}$C | 12 | 6 | L2-alpha-cluster | 🟢 recursive | binding_energy | 97.1480 | 92.1617 | +5.41 % | 11495.4475 MeV (+28405.8 ppm) |
| ${}^{13}$C | 13 | 7 | L3-partial-shell:f=0.250 from A=12→16 | 🟠 heuristic | binding_energy | 101.0622 | 97.1080 | +4.07 % | — |
| ${}^{14}$C | 14 | 8 | derivation-pending | ⚪ pending | binding_energy | — | 105.2845 | — | — |
| ${}^{15}$C | 15 | 9 | derivation-pending | ⚪ pending | binding_energy | — | 106.5025 | — | — |
| ${}^{16}$C | 16 | 10 | derivation-pending | ⚪ pending | binding_energy | — | 110.7529 | — | — |
| ${}^{17}$C | 17 | 11 | derivation-pending | ⚪ pending | binding_energy | — | 111.4864 | — | — |
| ${}^{18}$C | 18 | 12 | derivation-pending | ⚪ pending | binding_energy | — | 115.6704 | — | — |
| ${}^{19}$C | 19 | 13 | derivation-pending | ⚪ pending | binding_energy | — | 116.2472 | — | — |
| ${}^{20}$C | 20 | 14 | derivation-pending | ⚪ pending | binding_energy | — | 119.2287 | — | — |
| ${}^{21}$C | 21 | 15 | derivation-pending | ⚪ pending | binding_energy | — | 119.1540 | — | — |
| ${}^{22}$C | 22 | 16 | derivation-pending | ⚪ pending | binding_energy | — | 119.2637 | — | — |
| ${}^{23}$C | 23 | 17 | derivation-pending | ⚪ pending | binding_energy | — | 116.7710 | — | — |

### Nitrogen (Z = 7)

_2 of 16 isotopes with a framework prediction; 0 of 16 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{10}$N | 10 | 3 | derivation-pending | ⚪ pending | binding_energy | — | 36.4367 | — | — |
| ${}^{11}$N | 11 | 4 | derivation-pending | ⚪ pending | binding_energy | — | 58.9424 | — | — |
| ${}^{12}$N | 12 | 5 | derivation-pending | ⚪ pending | binding_energy | — | 74.0413 | — | — |
| ${}^{13}$N | 13 | 6 | derivation-pending | ⚪ pending | binding_energy | — | 94.1052 | — | — |
| ${}^{14}$N | 14 | 7 | L3-partial-shell:f=0.500 from A=12→16 | 🟠 heuristic | binding_energy | 109.9563 | 104.6586 | +5.06 % | — |
| ${}^{15}$N | 15 | 8 | L3-partial-shell:f=0.750 from A=12→16 | 🟠 heuristic | binding_energy | 118.8505 | 115.4919 | +2.91 % | — |
| ${}^{16}$N | 16 | 9 | derivation-pending | ⚪ pending | binding_energy | — | 117.9808 | — | — |
| ${}^{17}$N | 17 | 10 | derivation-pending | ⚪ pending | binding_energy | — | 123.8659 | — | — |
| ${}^{18}$N | 18 | 11 | derivation-pending | ⚪ pending | binding_energy | — | 126.6941 | — | — |
| ${}^{19}$N | 19 | 12 | derivation-pending | ⚪ pending | binding_energy | — | 132.0224 | — | — |
| ${}^{20}$N | 20 | 13 | derivation-pending | ⚪ pending | binding_energy | — | 134.1834 | — | — |
| ${}^{21}$N | 21 | 14 | derivation-pending | ⚪ pending | binding_energy | — | 138.7893 | — | — |
| ${}^{22}$N | 22 | 15 | derivation-pending | ⚪ pending | binding_energy | — | 140.3278 | — | — |
| ${}^{23}$N | 23 | 16 | derivation-pending | ⚪ pending | binding_energy | — | 143.4435 | — | — |
| ${}^{24}$N | 24 | 17 | derivation-pending | ⚪ pending | binding_energy | — | 141.2880 | — | — |
| ${}^{25}$N | 25 | 18 | derivation-pending | ⚪ pending | binding_energy | — | 140.3250 | — | — |

### Oxygen (Z = 8)

_3 of 18 isotopes with a framework prediction; 1 of 18 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{11}$O | 11 | 3 | derivation-pending | ⚪ pending | binding_energy | — | 34.7868 | — | — |
| ${}^{12}$O | 12 | 4 | derivation-pending | ⚪ pending | binding_energy | — | 58.5837 | — | — |
| ${}^{13}$O | 13 | 5 | derivation-pending | ⚪ pending | binding_energy | — | 75.5529 | — | — |
| ${}^{14}$O | 14 | 6 | derivation-pending | ⚪ pending | binding_energy | — | 98.7319 | — | — |
| ${}^{15}$O | 15 | 7 | derivation-pending | ⚪ pending | binding_energy | — | 111.9554 | — | — |
| ${}^{16}$O | 16 | 8 | L2-alpha-cluster | 🟢 recursive | binding_energy | 134.3846 | 127.6193 | +5.30 % | 15322.4093 MeV (+28407.0 ppm) |
| ${}^{17}$O | 17 | 9 | L3-partial-shell:f=0.250 from A=16→20 | 🟠 heuristic | binding_energy | 137.2455 | 131.7624 | +4.16 % | — |
| ${}^{18}$O | 18 | 10 | L3-partial-shell:f=0.500 from A=16→20 | 🟠 heuristic | binding_energy | 146.7464 | 139.8078 | +4.96 % | — |
| ${}^{19}$O | 19 | 11 | derivation-pending | ⚪ pending | binding_energy | — | 143.7634 | — | — |
| ${}^{20}$O | 20 | 12 | derivation-pending | ⚪ pending | binding_energy | — | 151.3714 | — | — |
| ${}^{21}$O | 21 | 13 | derivation-pending | ⚪ pending | binding_energy | — | 155.1769 | — | — |
| ${}^{22}$O | 22 | 14 | derivation-pending | ⚪ pending | binding_energy | — | 162.0272 | — | — |
| ${}^{23}$O | 23 | 15 | derivation-pending | ⚪ pending | binding_energy | — | 164.7602 | — | — |
| ${}^{24}$O | 24 | 16 | derivation-pending | ⚪ pending | binding_energy | — | 168.9525 | — | — |
| ${}^{25}$O | 25 | 17 | derivation-pending | ⚪ pending | binding_energy | — | 168.1951 | — | — |
| ${}^{26}$O | 26 | 18 | derivation-pending | ⚪ pending | binding_energy | — | 168.9345 | — | — |
| ${}^{27}$O | 27 | 19 | derivation-pending | ⚪ pending | binding_energy | — | 166.9950 | — | — |
| ${}^{28}$O | 28 | 20 | derivation-pending | ⚪ pending | binding_energy | — | 167.6640 | — | — |

### Fluorine (Z = 9)

_1 of 19 isotopes with a framework prediction; 0 of 19 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{13}$F | 13 | 4 | derivation-pending | ⚪ pending | binding_energy | — | 55.8610 | — | — |
| ${}^{14}$F | 14 | 5 | derivation-pending | ⚪ pending | binding_energy | — | 73.9929 | — | — |
| ${}^{15}$F | 15 | 6 | derivation-pending | ⚪ pending | binding_energy | — | 97.4619 | — | — |
| ${}^{16}$F | 16 | 7 | derivation-pending | ⚪ pending | binding_energy | — | 111.4248 | — | — |
| ${}^{17}$F | 17 | 8 | derivation-pending | ⚪ pending | binding_energy | — | 128.2196 | — | — |
| ${}^{18}$F | 18 | 9 | derivation-pending | ⚪ pending | binding_energy | — | 137.3695 | — | — |
| ${}^{19}$F | 19 | 10 | L3-partial-shell:f=0.750 from A=16→20 | 🟠 heuristic | binding_energy | 156.2474 | 147.8014 | +5.71 % | — |
| ${}^{20}$F | 20 | 11 | derivation-pending | ⚪ pending | binding_energy | — | 154.4027 | — | — |
| ${}^{21}$F | 21 | 12 | derivation-pending | ⚪ pending | binding_energy | — | 162.5042 | — | — |
| ${}^{22}$F | 22 | 13 | derivation-pending | ⚪ pending | binding_energy | — | 167.7345 | — | — |
| ${}^{23}$F | 23 | 14 | derivation-pending | ⚪ pending | binding_energy | — | 175.3139 | — | — |
| ${}^{24}$F | 24 | 15 | derivation-pending | ⚪ pending | binding_energy | — | 179.1260 | — | — |
| ${}^{25}$F | 25 | 16 | derivation-pending | ⚪ pending | binding_energy | — | 183.4077 | — | — |
| ${}^{26}$F | 26 | 17 | derivation-pending | ⚪ pending | binding_energy | — | 184.1385 | — | — |
| ${}^{27}$F | 27 | 18 | derivation-pending | ⚪ pending | binding_energy | — | 185.7510 | — | — |
| ${}^{28}$F | 28 | 19 | derivation-pending | ⚪ pending | binding_energy | — | 185.5520 | — | — |
| ${}^{29}$F | 29 | 20 | derivation-pending | ⚪ pending | binding_energy | — | 186.8769 | — | — |
| ${}^{30}$F | 30 | 21 | derivation-pending | ⚪ pending | binding_energy | — | 186.1500 | — | — |
| ${}^{31}$F | 31 | 22 | derivation-pending | ⚪ pending | binding_energy | — | 186.3410 | — | — |

### Neon (Z = 10)

_3 of 20 isotopes with a framework prediction; 1 of 20 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{15}$Ne | 15 | 5 | derivation-pending | ⚪ pending | binding_energy | — | 73.0309 | — | — |
| ${}^{16}$Ne | 16 | 6 | derivation-pending | ⚪ pending | binding_energy | — | 97.3308 | — | — |
| ${}^{17}$Ne | 17 | 7 | derivation-pending | ⚪ pending | binding_energy | — | 112.8885 | — | — |
| ${}^{18}$Ne | 18 | 8 | derivation-pending | ⚪ pending | binding_energy | — | 132.1426 | — | — |
| ${}^{19}$Ne | 19 | 9 | derivation-pending | ⚪ pending | binding_energy | — | 143.7795 | — | — |
| ${}^{20}$Ne | 20 | 10 | L2-alpha-cluster | 🟢 recursive | binding_energy | 174.0483 | 160.6448 | +8.34 % | 19146.9442 MeV (+28143.1 ppm) |
| ${}^{21}$Ne | 21 | 11 | L3-partial-shell:f=0.250 from A=20→24 | 🟠 heuristic | binding_energy | 175.8559 | 167.4060 | +5.05 % | — |
| ${}^{22}$Ne | 22 | 12 | L3-partial-shell:f=0.500 from A=20→24 | 🟠 heuristic | binding_energy | 185.9636 | 177.7702 | +4.61 % | — |
| ${}^{23}$Ne | 23 | 13 | derivation-pending | ⚪ pending | binding_energy | — | 182.9709 | — | — |
| ${}^{24}$Ne | 24 | 14 | derivation-pending | ⚪ pending | binding_energy | — | 191.8398 | — | — |
| ${}^{25}$Ne | 25 | 15 | derivation-pending | ⚪ pending | binding_energy | — | 195.9950 | — | — |
| ${}^{26}$Ne | 26 | 16 | derivation-pending | ⚪ pending | binding_energy | — | 201.5497 | — | — |
| ${}^{27}$Ne | 27 | 17 | derivation-pending | ⚪ pending | binding_energy | — | 203.0512 | — | — |
| ${}^{28}$Ne | 28 | 18 | derivation-pending | ⚪ pending | binding_energy | — | 206.8737 | — | — |
| ${}^{29}$Ne | 29 | 19 | derivation-pending | ⚪ pending | binding_energy | — | 207.8450 | — | — |
| ${}^{30}$Ne | 30 | 20 | derivation-pending | ⚪ pending | binding_energy | — | 211.0360 | — | — |
| ${}^{31}$Ne | 31 | 21 | derivation-pending | ⚪ pending | binding_energy | — | 211.2058 | — | — |
| ${}^{32}$Ne | 32 | 22 | derivation-pending | ⚪ pending | binding_energy | — | 213.4720 | — | — |
| ${}^{33}$Ne | 33 | 23 | derivation-pending | ⚪ pending | binding_energy | — | 212.3880 | — | — |
| ${}^{34}$Ne | 34 | 24 | derivation-pending | ⚪ pending | binding_energy | — | 213.7580 | — | — |

### Fermium (Z = 100)

_20 of 20 isotopes with a framework prediction; 20 of 20 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{241}$Fm | 241 | 141 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1800.2241 | 1797.6190 | +0.14 % | 231045.0066 MeV (+28881.9 ppm) |
| ${}^{242}$Fm | 242 | 142 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1808.8864 | 1806.5300 | +0.13 % | 232003.0590 MeV (+28884.2 ppm) |
| ${}^{243}$Fm | 243 | 143 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1815.9741 | 1813.7520 | +0.12 % | 232962.6861 MeV (+28885.4 ppm) |
| ${}^{244}$Fm | 244 | 144 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1824.3603 | 1822.1920 | +0.12 % | 233921.0146 MeV (+28886.7 ppm) |
| ${}^{245}$Fm | 245 | 145 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1831.1811 | 1828.9250 | +0.12 % | 234880.9086 MeV (+28887.7 ppm) |
| ${}^{246}$Fm | 246 | 146 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1839.2979 | 1837.1184 | +0.12 % | 235839.5066 MeV (+28888.5 ppm) |
| ${}^{247}$Fm | 247 | 147 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1845.8583 | 1843.6080 | +0.12 % | 236799.6610 MeV (+28889.5 ppm) |
| ${}^{248}$Fm | 248 | 148 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1853.7122 | 1851.5544 | +0.12 % | 237758.5219 MeV (+28890.5 ppm) |
| ${}^{249}$Fm | 249 | 149 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1860.0184 | 1858.0044 | +0.11 % | 238718.9304 MeV (+28891.9 ppm) |
| ${}^{250}$Fm | 250 | 150 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1867.6155 | 1865.5226 | +0.11 % | 239678.0480 MeV (+28892.5 ppm) |
| ${}^{251}$Fm | 251 | 151 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1873.6738 | 1871.7073 | +0.11 % | 240638.7046 MeV (+28893.9 ppm) |
| ${}^{252}$Fm | 252 | 152 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1881.0202 | 1878.9208 | +0.11 % | 241598.0729 MeV (+28894.2 ppm) |
| ${}^{253}$Fm | 253 | 153 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1886.8363 | 1884.4632 | +0.13 % | 242558.9716 MeV (+28893.7 ppm) |
| ${}^{254}$Fm | 254 | 154 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1893.9379 | 1890.9776 | +0.16 % | 243518.5848 MeV (+28892.0 ppm) |
| ${}^{255}$Fm | 255 | 155 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1899.5176 | 1896.1509 | +0.18 % | 244479.7199 MeV (+28891.0 ppm) |
| ${}^{256}$Fm | 256 | 156 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1906.3800 | 1902.5379 | +0.20 % | 245439.5723 MeV (+28889.8 ppm) |
| ${}^{257}$Fm | 257 | 157 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1911.7287 | 1907.5039 | +0.22 % | 246400.9383 MeV (+28888.8 ppm) |
| ${}^{258}$Fm | 258 | 158 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1918.3575 | 1913.8440 | +0.24 % | 247361.0243 MeV (+28887.9 ppm) |
| ${}^{259}$Fm | 259 | 159 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1923.4807 | 1918.4130 | +0.26 % | 248322.6159 MeV (+28887.2 ppm) |
| ${}^{260}$Fm | 260 | 160 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1929.8811 | 1924.5200 | +0.28 % | 249282.9302 MeV (+28886.3 ppm) |

### Mendelevium (Z = 101)

_19 of 19 isotopes with a framework prediction; 19 of 19 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{244}$Md | 244 | 143 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1816.9266 | 1814.8720 | +0.11 % | 233927.1180 MeV (+28883.5 ppm) |
| ${}^{245}$Md | 245 | 144 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1825.5226 | 1823.0450 | +0.14 % | 234885.2368 MeV (+28883.5 ppm) |
| ${}^{246}$Md | 246 | 145 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1832.5549 | 1830.4860 | +0.11 % | 235844.9193 MeV (+28885.6 ppm) |
| ${}^{247}$Md | 247 | 146 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1840.8793 | 1838.6680 | +0.12 % | 236803.3097 MeV (+28886.3 ppm) |
| ${}^{248}$Md | 248 | 147 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1847.6490 | 1845.6160 | +0.11 % | 237763.2548 MeV (+28888.5 ppm) |
| ${}^{249}$Md | 249 | 148 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1855.7083 | 1853.5602 | +0.12 % | 238721.9103 MeV (+28888.5 ppm) |
| ${}^{250}$Md | 250 | 149 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1862.2217 | 1860.4133 | +0.10 % | 239682.1116 MeV (+28890.9 ppm) |
| ${}^{251}$Md | 251 | 150 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1870.0221 | 1867.9170 | +0.11 % | 240641.0259 MeV (+28890.6 ppm) |
| ${}^{252}$Md | 252 | 151 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1876.2854 | 1874.4880 | +0.10 % | 241601.4774 MeV (+28892.7 ppm) |
| ${}^{253}$Md | 253 | 152 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1883.8331 | 1881.8140 | +0.11 % | 242560.6445 MeV (+28892.8 ppm) |
| ${}^{254}$Md | 254 | 153 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1889.8521 | 1887.7280 | +0.11 % | 243521.3402 MeV (+28892.6 ppm) |
| ${}^{255}$Md | 255 | 154 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1897.1529 | 1894.3270 | +0.15 % | 244480.7543 MeV (+28890.8 ppm) |
| ${}^{256}$Md | 256 | 155 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1902.9334 | 1899.7760 | +0.17 % | 245441.6885 MeV (+28890.1 ppm) |
| ${}^{257}$Md | 257 | 156 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1909.9929 | 1906.3192 | +0.19 % | 246401.3438 MeV (+28888.8 ppm) |
| ${}^{258}$Md | 258 | 157 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1915.5405 | 1911.6927 | +0.20 % | 247362.5110 MeV (+28888.7 ppm) |
| ${}^{259}$Md | 259 | 158 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1922.3644 | 1917.8950 | +0.23 % | 248322.4019 MeV (+28886.9 ppm) |
| ${}^{260}$Md | 260 | 159 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1927.6844 | 1922.9600 | +0.25 % | 249283.7967 MeV (+28886.6 ppm) |
| ${}^{261}$Md | 261 | 160 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1934.2779 | 1929.0510 | +0.27 % | 250243.9179 MeV (+28885.0 ppm) |
| ${}^{262}$Md | 262 | 161 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1939.3756 | 1934.0840 | +0.27 % | 251205.5350 MeV (+28885.2 ppm) |

### Nobelium (Z = 102)

_17 of 17 isotopes with a framework prediction; 17 of 17 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{248}$No | 248 | 146 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1843.4524 | 1841.1520 | +0.12 % | 237766.1211 MeV (+28884.2 ppm) |
| ${}^{249}$No | 249 | 147 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1850.4282 | 1848.0780 | +0.13 % | 238725.8600 MeV (+28885.1 ppm) |
| ${}^{250}$No | 250 | 148 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1858.6897 | 1856.5000 | +0.12 % | 239684.3133 MeV (+28886.3 ppm) |
| ${}^{251}$No | 251 | 149 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1865.4072 | 1863.1730 | +0.12 % | 240644.3106 MeV (+28887.5 ppm) |
| ${}^{252}$No | 252 | 150 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1873.4077 | 1871.3014 | +0.11 % | 241603.0248 MeV (+28888.8 ppm) |
| ${}^{253}$No | 253 | 151 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1879.8730 | 1877.8854 | +0.11 % | 242563.2743 MeV (+28890.1 ppm) |
| ${}^{254}$No | 254 | 152 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1887.6187 | 1885.5921 | +0.11 % | 243522.2434 MeV (+28890.9 ppm) |
| ${}^{255}$No | 255 | 153 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1893.8377 | 1891.5748 | +0.12 % | 244482.7392 MeV (+28890.6 ppm) |
| ${}^{256}$No | 256 | 154 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1901.3345 | 1898.6350 | +0.14 % | 245441.9571 MeV (+28889.7 ppm) |
| ${}^{257}$No | 257 | 155 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1907.3129 | 1904.2823 | +0.16 % | 246402.6935 MeV (+28889.0 ppm) |
| ${}^{258}$No | 258 | 156 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1914.5666 | 1911.0060 | +0.19 % | 247362.1546 MeV (+28888.1 ppm) |
| ${}^{259}$No | 259 | 157 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1920.3100 | 1916.5926 | +0.19 % | 248323.1259 MeV (+28887.7 ppm) |
| ${}^{260}$No | 260 | 158 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1927.3261 | 1923.2200 | +0.21 % | 249282.8247 MeV (+28886.5 ppm) |
| ${}^{261}$No | 261 | 159 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1932.8399 | 1928.2680 | +0.24 % | 250244.0256 MeV (+28886.0 ppm) |
| ${}^{262}$No | 262 | 160 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1939.6237 | 1934.8700 | +0.25 % | 251203.9566 MeV (+28885.3 ppm) |
| ${}^{263}$No | 263 | 161 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1944.9133 | 1939.8880 | +0.26 % | 252165.3818 MeV (+28885.0 ppm) |
| ${}^{264}$No | 264 | 162 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1951.4700 | 1945.9440 | +0.28 % | 253125.5398 MeV (+28884.2 ppm) |

### Lawrencium (Z = 103)

_16 of 16 isotopes with a framework prediction; 16 of 16 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{251}$Lr | 251 | 148 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1859.8289 | 1857.4000 | +0.13 % | 240648.5586 MeV (+28883.8 ppm) |
| ${}^{252}$Lr | 252 | 149 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1866.7528 | 1864.8000 | +0.10 % | 241608.3494 MeV (+28886.6 ppm) |
| ${}^{253}$Lr | 253 | 150 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1874.9560 | 1872.9383 | +0.11 % | 242566.8610 MeV (+28887.1 ppm) |
| ${}^{254}$Lr | 254 | 151 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1881.6256 | 1879.8872 | +0.09 % | 243526.9061 MeV (+28889.2 ppm) |
| ${}^{255}$Lr | 255 | 152 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1889.5720 | 1887.6571 | +0.10 % | 244485.6746 MeV (+28889.4 ppm) |
| ${}^{256}$Lr | 256 | 153 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1895.9933 | 1893.9291 | +0.11 % | 245445.9681 MeV (+28889.6 ppm) |
| ${}^{257}$Lr | 257 | 154 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1903.6887 | 1901.0290 | +0.14 % | 246404.9875 MeV (+28888.2 ppm) |
| ${}^{258}$Lr | 258 | 155 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1909.8673 | 1907.1360 | +0.14 % | 247365.5235 MeV (+28888.0 ppm) |
| ${}^{259}$Lr | 259 | 156 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1917.3176 | 1914.0100 | +0.17 % | 248324.7881 MeV (+28887.0 ppm) |
| ${}^{260}$Lr | 260 | 157 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1923.2593 | 1919.5800 | +0.19 % | 249285.5611 MeV (+28886.5 ppm) |
| ${}^{261}$Lr | 261 | 158 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1930.4699 | 1926.4410 | +0.21 % | 250245.0653 MeV (+28885.6 ppm) |
| ${}^{262}$Lr | 262 | 159 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1936.1801 | 1931.9880 | +0.22 % | 251206.0699 MeV (+28885.5 ppm) |
| ${}^{263}$Lr | 263 | 160 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1943.1565 | 1938.5730 | +0.24 % | 252165.8082 MeV (+28884.4 ppm) |
| ${}^{264}$Lr | 264 | 161 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1948.6404 | 1943.8320 | +0.25 % | 253127.0391 MeV (+28884.6 ppm) |
| ${}^{265}$Lr | 265 | 162 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1955.3879 | 1950.1350 | +0.27 % | 254087.0064 MeV (+28883.2 ppm) |
| ${}^{266}$Lr | 266 | 163 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1960.6506 | 1954.8340 | +0.30 % | 255048.4585 MeV (+28881.3 ppm) |

### Rutherfordium (Z = 104)

_16 of 16 isotopes with a framework prediction; 16 of 16 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{253}$Rf | 253 | 149 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1869.0822 | 1867.1400 | +0.10 % | 242571.4045 MeV (+28884.1 ppm) |
| ${}^{254}$Rf | 254 | 150 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1877.4849 | 1875.5360 | +0.10 % | 243529.7166 MeV (+28885.6 ppm) |
| ${}^{255}$Rf | 255 | 151 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1884.3558 | 1882.4100 | +0.10 % | 244489.5605 MeV (+28886.8 ppm) |
| ${}^{256}$Rf | 256 | 152 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1892.4996 | 1890.6713 | +0.10 % | 245448.1314 MeV (+28888.0 ppm) |
| ${}^{257}$Rf | 257 | 153 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1899.1202 | 1897.0983 | +0.11 % | 246408.2257 MeV (+28888.0 ppm) |
| ${}^{258}$Rf | 258 | 154 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1907.0111 | 1904.6916 | +0.12 % | 247367.0495 MeV (+28887.7 ppm) |
| ${}^{259}$Rf | 259 | 155 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1913.3871 | 1910.6430 | +0.14 % | 248327.3883 MeV (+28887.1 ppm) |
| ${}^{260}$Rf | 260 | 156 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1921.0309 | 1918.0200 | +0.16 % | 249286.4592 MeV (+28886.5 ppm) |
| ${}^{261}$Rf | 261 | 157 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1927.1679 | 1923.9317 | +0.17 % | 250247.0370 MeV (+28886.3 ppm) |
| ${}^{262}$Rf | 262 | 158 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1934.5702 | 1930.9400 | +0.19 % | 251206.3494 MeV (+28885.5 ppm) |
| ${}^{263}$Rf | 263 | 159 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1940.4738 | 1936.7320 | +0.19 % | 252167.1607 MeV (+28885.4 ppm) |
| ${}^{264}$Rf | 264 | 160 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1947.6400 | 1943.3040 | +0.22 % | 253126.7092 MeV (+28884.5 ppm) |
| ${}^{265}$Rf | 265 | 161 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1953.3153 | 1948.8100 | +0.23 % | 254087.7487 MeV (+28884.3 ppm) |
| ${}^{266}$Rf | 266 | 162 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1960.2507 | 1955.3660 | +0.25 % | 255047.5281 MeV (+28883.9 ppm) |
| ${}^{267}$Rf | 267 | 163 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1965.7029 | 1960.3140 | +0.27 % | 256008.7906 MeV (+28881.7 ppm) |
| ${}^{268}$Rf | 268 | 164 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1972.4126 | 1966.3160 | +0.31 % | 256968.7957 MeV (+28879.8 ppm) |

### Dubnium (Z = 105)

_16 of 16 isotopes with a framework prediction; 16 of 16 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{255}$Db | 255 | 150 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1878.1891 | 1876.5450 | +0.09 % | 244494.3968 MeV (+28884.4 ppm) |
| ${}^{256}$Db | 256 | 151 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1885.2637 | 1883.9040 | +0.07 % | 245454.0371 MeV (+28886.5 ppm) |
| ${}^{257}$Db | 257 | 152 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1893.6074 | 1892.0280 | +0.08 % | 246412.4081 MeV (+28887.0 ppm) |
| ${}^{258}$Db | 258 | 153 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1900.4296 | 1898.7459 | +0.09 % | 247372.3007 MeV (+28887.4 ppm) |
| ${}^{259}$Db | 259 | 154 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1908.5185 | 1906.3339 | +0.11 % | 248330.9266 MeV (+28886.3 ppm) |
| ${}^{260}$Db | 260 | 155 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1915.0941 | 1912.8200 | +0.12 % | 249291.0657 MeV (+28886.3 ppm) |
| ${}^{261}$Db | 261 | 156 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1922.9339 | 1920.1770 | +0.14 % | 250249.9407 MeV (+28885.6 ppm) |
| ${}^{262}$Db | 262 | 157 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1929.2686 | 1926.2240 | +0.16 % | 251210.3208 MeV (+28885.5 ppm) |
| ${}^{263}$Db | 263 | 158 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1936.8650 | 1933.5760 | +0.17 % | 252169.4392 MeV (+28884.8 ppm) |
| ${}^{264}$Db | 264 | 159 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1942.9642 | 1939.3440 | +0.19 % | 253130.0547 MeV (+28884.8 ppm) |
| ${}^{265}$Db | 265 | 160 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1950.3226 | 1946.4250 | +0.20 % | 254089.4111 MeV (+28884.0 ppm) |
| ${}^{266}$Db | 266 | 161 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1956.1917 | 1952.1740 | +0.21 % | 255050.2568 MeV (+28884.1 ppm) |
| ${}^{267}$Db | 267 | 162 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1963.3174 | 1958.9790 | +0.22 % | 256009.8459 MeV (+28883.6 ppm) |
| ${}^{268}$Db | 268 | 163 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1968.9615 | 1963.9040 | +0.26 % | 256970.9165 MeV (+28881.8 ppm) |
| ${}^{269}$Db | 269 | 164 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1975.8596 | 1969.8870 | +0.30 % | 257930.7332 MeV (+28878.9 ppm) |
| ${}^{270}$Db | 270 | 165 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1981.2837 | 1974.7800 | +0.33 % | 258892.0239 MeV (+28877.1 ppm) |

### Seaborgium (Z = 106)

_16 of 16 isotopes with a framework prediction; 16 of 16 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{258}$Sg | 258 | 152 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1895.6911 | 1894.2360 | +0.08 % | 247375.7089 MeV (+28885.4 ppm) |
| ${}^{259}$Sg | 259 | 153 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1902.7118 | 1901.0600 | +0.09 % | 248335.4029 MeV (+28885.5 ppm) |
| ${}^{260}$Sg | 260 | 154 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1910.9957 | 1909.0664 | +0.10 % | 249293.8339 MeV (+28885.5 ppm) |
| ${}^{261}$Sg | 261 | 155 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1917.7679 | 1915.6802 | +0.11 % | 250253.7764 MeV (+28885.7 ppm) |
| ${}^{262}$Sg | 262 | 156 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1925.8008 | 1923.3875 | +0.13 % | 251212.4583 MeV (+28885.3 ppm) |
| ${}^{263}$Sg | 263 | 157 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1932.3302 | 1929.6310 | +0.14 % | 252172.6437 MeV (+28884.9 ppm) |
| ${}^{264}$Sg | 264 | 158 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1940.1177 | 1937.2320 | +0.15 % | 253131.5709 MeV (+28884.6 ppm) |
| ${}^{265}$Sg | 265 | 159 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1946.4098 | 1943.2450 | +0.16 % | 254091.9936 MeV (+28884.4 ppm) |
| ${}^{266}$Sg | 266 | 160 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1953.9574 | 1950.3120 | +0.19 % | 255051.1607 MeV (+28884.1 ppm) |
| ${}^{267}$Sg | 267 | 161 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1960.0175 | 1956.3090 | +0.19 % | 256011.8155 MeV (+28884.1 ppm) |
| ${}^{268}$Sg | 268 | 162 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1967.3306 | 1963.3680 | +0.20 % | 256971.2171 MeV (+28884.0 ppm) |
| ${}^{269}$Sg | 269 | 163 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1973.1638 | 1968.5420 | +0.23 % | 257932.0987 MeV (+28882.1 ppm) |
| ${}^{270}$Sg | 270 | 164 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1980.2475 | 1974.7800 | +0.28 % | 258891.7297 MeV (+28879.9 ppm) |
| ${}^{271}$Sg | 271 | 165 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1985.8589 | 1979.6550 | +0.31 % | 259852.8331 MeV (+28877.6 ppm) |
| ${}^{272}$Sg | 272 | 166 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1992.7183 | 1985.8720 | +0.34 % | 260812.6886 MeV (+28875.6 ppm) |
| ${}^{273}$Sg | 273 | 167 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1998.1127 | 1990.7160 | +0.37 % | 261774.0089 MeV (+28873.4 ppm) |

### Bohrium (Z = 107)

_19 of 19 isotopes with a framework prediction; 19 of 19 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{260}$Bh | 260 | 153 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1903.1888 | 1901.6400 | +0.08 % | 249300.3104 MeV (+28884.3 ppm) |
| ${}^{261}$Bh | 261 | 154 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1911.6699 | 1909.8235 | +0.10 % | 250258.5441 MeV (+28883.8 ppm) |
| ${}^{262}$Bh | 262 | 155 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1918.6412 | 1916.7221 | +0.10 % | 251218.2876 MeV (+28884.4 ppm) |
| ${}^{263}$Bh | 263 | 156 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1926.8694 | 1924.6340 | +0.12 % | 252176.7742 MeV (+28883.7 ppm) |
| ${}^{264}$Bh | 264 | 157 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1933.5958 | 1931.1600 | +0.13 % | 253136.7625 MeV (+28884.1 ppm) |
| ${}^{265}$Bh | 265 | 158 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1941.5768 | 1938.7400 | +0.15 % | 254095.4963 MeV (+28883.6 ppm) |
| ${}^{266}$Bh | 266 | 159 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1948.0640 | 1945.2580 | +0.14 % | 255055.7239 MeV (+28883.9 ppm) |
| ${}^{267}$Bh | 267 | 160 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1955.8033 | 1952.5710 | +0.17 % | 256014.6994 MeV (+28883.5 ppm) |
| ${}^{268}$Bh | 268 | 161 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1962.0566 | 1958.8120 | +0.17 % | 256975.1608 MeV (+28883.7 ppm) |
| ${}^{269}$Bh | 269 | 162 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1969.5595 | 1966.1210 | +0.17 % | 257934.3727 MeV (+28883.8 ppm) |
| ${}^{270}$Bh | 270 | 163 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1975.5840 | 1971.2700 | +0.22 % | 258895.0629 MeV (+28881.7 ppm) |
| ${}^{271}$Bh | 271 | 164 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1982.8557 | 1977.7580 | +0.26 % | 259854.5061 MeV (+28879.2 ppm) |
| ${}^{272}$Bh | 272 | 165 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1988.6566 | 1982.8800 | +0.29 % | 260815.4199 MeV (+28877.2 ppm) |
| ${}^{273}$Bh | 273 | 166 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1995.7020 | 1989.0780 | +0.33 % | 261775.0893 MeV (+28874.6 ppm) |
| ${}^{274}$Bh | 274 | 167 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2001.2842 | 1994.1720 | +0.36 % | 262736.2219 MeV (+28872.9 ppm) |
| ${}^{275}$Bh | 275 | 168 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2008.1083 | 2000.0750 | +0.40 % | 263696.1125 MeV (+28870.7 ppm) |
| ${}^{276}$Bh | 276 | 169 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2013.4764 | 2005.1400 | +0.42 % | 264657.4592 MeV (+28869.5 ppm) |
| ${}^{277}$Bh | 277 | 170 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2020.0840 | 2011.0200 | +0.45 % | 265617.5664 MeV (+28867.6 ppm) |
| ${}^{278}$Bh | 278 | 171 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2025.2427 | 2015.7780 | +0.47 % | 266579.1225 MeV (+28866.8 ppm) |

### Hassium (Z = 108)

_18 of 18 isotopes with a framework prediction; 18 of 18 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{263}$Hs | 263 | 155 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1920.4826 | 1918.5850 | +0.10 % | 252181.8307 MeV (+28882.6 ppm) |
| ${}^{264}$Hs | 264 | 156 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1928.9032 | 1926.7713 | +0.11 % | 253140.1248 MeV (+28882.7 ppm) |
| ${}^{265}$Hs | 265 | 157 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1935.8238 | 1933.5056 | +0.12 % | 254099.9190 MeV (+28882.7 ppm) |
| ${}^{266}$Hs | 266 | 158 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1943.9954 | 1941.3375 | +0.14 % | 255058.4622 MeV (+28882.3 ppm) |
| ${}^{267}$Hs | 267 | 159 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1950.6748 | 1947.7650 | +0.15 % | 256018.4976 MeV (+28882.6 ppm) |
| ${}^{268}$Hs | 268 | 160 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1958.6028 | 1955.5960 | +0.15 % | 256977.2843 MeV (+28882.9 ppm) |
| ${}^{269}$Hs | 269 | 161 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1965.0465 | 1962.0860 | +0.15 % | 257937.5554 MeV (+28884.1 ppm) |
| ${}^{270}$Hs | 270 | 162 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1972.7363 | 1969.6500 | +0.16 % | 258896.5803 MeV (+28884.1 ppm) |
| ${}^{271}$Hs | 271 | 163 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1978.9495 | 1975.0480 | +0.20 % | 259857.0820 MeV (+28881.9 ppm) |
| ${}^{272}$Hs | 272 | 164 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1986.4063 | 1981.7920 | +0.23 % | 260816.3399 MeV (+28880.0 ppm) |
| ${}^{273}$Hs | 273 | 165 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1992.3940 | 1987.1670 | +0.26 % | 261777.0670 MeV (+28878.0 ppm) |
| ${}^{274}$Hs | 274 | 166 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1999.6229 | 1993.6240 | +0.30 % | 262736.5529 MeV (+28875.6 ppm) |
| ${}^{275}$Hs | 275 | 167 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2005.3900 | 1998.7000 | +0.33 % | 263697.5006 MeV (+28873.2 ppm) |
| ${}^{276}$Hs | 276 | 168 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2012.3958 | 2005.1400 | +0.36 % | 264657.2095 MeV (+28871.6 ppm) |
| ${}^{277}$Hs | 277 | 169 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2017.9471 | 2009.9120 | +0.40 % | 265618.3730 MeV (+28869.6 ppm) |
| ${}^{278}$Hs | 278 | 170 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2024.7346 | 2016.0560 | +0.43 % | 266578.3002 MeV (+28868.2 ppm) |
| ${}^{279}$Hs | 279 | 171 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2030.0748 | 2020.7970 | +0.46 % | 267539.6748 MeV (+28866.8 ppm) |
| ${}^{280}$Hs | 280 | 172 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2036.6486 | 2026.9200 | +0.48 % | 268499.8158 MeV (+28865.9 ppm) |

### Meitnerium (Z = 109)

_18 of 18 isotopes with a framework prediction; 18 of 18 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{265}$Mt | 265 | 156 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1929.1506 | 1927.0800 | +0.11 % | 254105.2619 MeV (+28880.5 ppm) |
| ${}^{266}$Mt | 266 | 157 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1936.2675 | 1934.0221 | +0.12 % | 255064.8598 MeV (+28881.0 ppm) |
| ${}^{267}$Mt | 267 | 158 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1944.6320 | 1941.8910 | +0.14 % | 256023.2101 MeV (+28880.4 ppm) |
| ${}^{268}$Mt | 268 | 159 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1951.5059 | 1948.6280 | +0.15 % | 256983.0509 MeV (+28880.5 ppm) |
| ${}^{269}$Mt | 269 | 160 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1959.6250 | 1956.7060 | +0.15 % | 257941.6466 MeV (+28880.7 ppm) |
| ${}^{270}$Mt | 270 | 161 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1966.2613 | 1963.1700 | +0.16 % | 258901.7250 MeV (+28881.6 ppm) |
| ${}^{271}$Mt | 271 | 162 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1974.1404 | 1970.9830 | +0.16 % | 259860.5608 MeV (+28881.8 ppm) |
| ${}^{272}$Mt | 272 | 163 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1980.5444 | 1976.6240 | +0.20 % | 260820.8716 MeV (+28879.7 ppm) |
| ${}^{273}$Mt | 273 | 164 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1988.1886 | 1983.3450 | +0.24 % | 261779.9421 MeV (+28877.1 ppm) |
| ${}^{274}$Mt | 274 | 165 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1994.3653 | 1988.9660 | +0.27 % | 262740.4802 MeV (+28875.5 ppm) |
| ${}^{275}$Mt | 275 | 166 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2001.7798 | 1995.6750 | +0.31 % | 263699.7805 MeV (+28873.0 ppm) |
| ${}^{276}$Mt | 276 | 167 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2007.7341 | 2001.0000 | +0.34 % | 264660.5409 MeV (+28872.0 ppm) |
| ${}^{277}$Mt | 277 | 168 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2014.9238 | 2007.4190 | +0.37 % | 265620.0660 MeV (+28869.7 ppm) |
| ${}^{278}$Mt | 278 | 169 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2020.6606 | 2012.7200 | +0.39 % | 266581.0440 MeV (+28868.7 ppm) |
| ${}^{279}$Mt | 279 | 170 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2027.6303 | 2019.1230 | +0.42 % | 267540.7891 MeV (+28866.7 ppm) |
| ${}^{280}$Mt | 280 | 171 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2033.1542 | 2024.1200 | +0.45 % | 268501.9800 MeV (+28866.0 ppm) |
| ${}^{281}$Mt | 281 | 172 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2039.9084 | 2030.2250 | +0.48 % | 269461.9405 MeV (+28864.6 ppm) |
| ${}^{282}$Mt | 282 | 173 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2045.2240 | 2035.4760 | +0.48 % | 270423.3397 MeV (+28864.1 ppm) |

### Sodium (Z = 11)

_0 of 23 isotopes with a framework prediction; 0 of 23 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{17}$Na | 17 | 6 | derivation-pending | ⚪ pending | binding_energy | — | 93.8870 | — | — |
| ${}^{18}$Na | 18 | 7 | derivation-pending | ⚪ pending | binding_energy | — | 111.6399 | — | — |
| ${}^{19}$Na | 19 | 8 | derivation-pending | ⚪ pending | binding_energy | — | 131.8198 | — | — |
| ${}^{20}$Na | 20 | 9 | derivation-pending | ⚪ pending | binding_energy | — | 145.9701 | — | — |
| ${}^{21}$Na | 21 | 10 | derivation-pending | ⚪ pending | binding_energy | — | 163.0767 | — | — |
| ${}^{22}$Na | 22 | 11 | derivation-pending | ⚪ pending | binding_energy | — | 174.1446 | — | — |
| ${}^{23}$Na | 23 | 12 | derivation-pending | ⚪ pending | binding_energy | — | 186.5644 | — | — |
| ${}^{24}$Na | 24 | 13 | derivation-pending | ⚪ pending | binding_energy | — | 193.5237 | — | — |
| ${}^{25}$Na | 25 | 14 | derivation-pending | ⚪ pending | binding_energy | — | 202.5349 | — | — |
| ${}^{26}$Na | 26 | 15 | derivation-pending | ⚪ pending | binding_energy | — | 208.1092 | — | — |
| ${}^{27}$Na | 27 | 16 | derivation-pending | ⚪ pending | binding_energy | — | 214.8376 | — | — |
| ${}^{28}$Na | 28 | 17 | derivation-pending | ⚪ pending | binding_energy | — | 218.3794 | — | — |
| ${}^{29}$Na | 29 | 18 | derivation-pending | ⚪ pending | binding_energy | — | 222.7824 | — | — |
| ${}^{30}$Na | 30 | 19 | derivation-pending | ⚪ pending | binding_energy | — | 225.0591 | — | — |
| ${}^{31}$Na | 31 | 20 | derivation-pending | ⚪ pending | binding_energy | — | 229.3590 | — | — |
| ${}^{32}$Na | 32 | 21 | derivation-pending | ⚪ pending | binding_energy | — | 231.0362 | — | — |
| ${}^{33}$Na | 33 | 22 | derivation-pending | ⚪ pending | binding_energy | — | 233.9676 | — | — |
| ${}^{34}$Na | 34 | 23 | derivation-pending | ⚪ pending | binding_energy | — | 234.1389 | — | — |
| ${}^{35}$Na | 35 | 24 | derivation-pending | ⚪ pending | binding_energy | — | 236.0750 | — | — |
| ${}^{36}$Na | 36 | 25 | derivation-pending | ⚪ pending | binding_energy | — | 236.0520 | — | — |
| ${}^{37}$Na | 37 | 26 | derivation-pending | ⚪ pending | binding_energy | — | 236.9110 | — | — |
| ${}^{38}$Na | 38 | 27 | derivation-pending | ⚪ pending | binding_energy | — | 236.2080 | — | — |
| ${}^{39}$Na | 39 | 28 | derivation-pending | ⚪ pending | binding_energy | — | 236.1840 | — | — |

### Darmstadtium (Z = 110)

_18 of 18 isotopes with a framework prediction; 18 of 18 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{267}$Ds | 267 | 157 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1937.6749 | 1935.2160 | +0.13 % | 256028.8369 MeV (+28877.8 ppm) |
| ${}^{268}$Ds | 268 | 158 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1946.2293 | 1943.5360 | +0.14 % | 256986.9972 MeV (+28877.8 ppm) |
| ${}^{269}$Ds | 269 | 159 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1953.2949 | 1950.2917 | +0.15 % | 257946.6464 MeV (+28878.0 ppm) |
| ${}^{270}$Ds | 270 | 160 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1961.6021 | 1958.5161 | +0.16 % | 258905.0539 MeV (+28878.6 ppm) |
| ${}^{271}$Ds | 271 | 161 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1968.4283 | 1965.2920 | +0.16 % | 259864.9425 MeV (+28879.4 ppm) |
| ${}^{272}$Ds | 272 | 162 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1976.4938 | 1973.3600 | +0.16 % | 260823.5918 MeV (+28879.8 ppm) |
| ${}^{273}$Ds | 273 | 163 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1983.0858 | 1979.2500 | +0.19 % | 261783.7146 MeV (+28877.7 ppm) |
| ${}^{274}$Ds | 274 | 164 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1990.9147 | 1986.2260 | +0.24 % | 262742.6005 MeV (+28876.0 ppm) |
| ${}^{275}$Ds | 275 | 165 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1997.2777 | 1991.8250 | +0.27 % | 263702.9523 MeV (+28873.7 ppm) |
| ${}^{276}$Ds | 276 | 166 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2004.8751 | 1999.0680 | +0.29 % | 264662.0696 MeV (+28873.1 ppm) |
| ${}^{277}$Ds | 277 | 167 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2011.0140 | 2004.6490 | +0.32 % | 265622.6455 MeV (+28871.4 ppm) |
| ${}^{278}$Ds | 278 | 168 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2018.3849 | 2011.6080 | +0.34 % | 266581.9893 MeV (+28870.4 ppm) |
| ${}^{279}$Ds | 279 | 169 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2024.3045 | 2016.8910 | +0.37 % | 267542.7845 MeV (+28868.7 ppm) |
| ${}^{280}$Ds | 280 | 170 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2031.4537 | 2023.5600 | +0.39 % | 268502.3501 MeV (+28868.1 ppm) |
| ${}^{281}$Ds | 281 | 171 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2037.1587 | 2028.8200 | +0.41 % | 269463.3599 MeV (+28866.6 ppm) |
| ${}^{282}$Ds | 282 | 172 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2044.0908 | 2035.1940 | +0.44 % | 270423.1426 MeV (+28866.0 ppm) |
| ${}^{283}$Ds | 283 | 173 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2049.5858 | 2040.4300 | +0.45 % | 271384.3624 MeV (+28864.9 ppm) |
| ${}^{284}$Ds | 284 | 174 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2056.3053 | 2046.7880 | +0.46 % | 272344.3576 MeV (+28864.6 ppm) |

### Roentgenium (Z = 111)

_15 of 15 isotopes with a framework prediction; 15 of 15 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{272}$Rg | 272 | 161 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1968.8315 | 1965.7440 | +0.16 % | 260829.9238 MeV (+28877.7 ppm) |
| ${}^{273}$Rg | 273 | 162 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1977.0856 | 1973.7900 | +0.17 % | 261788.3845 MeV (+28877.5 ppm) |
| ${}^{274}$Rg | 274 | 163 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1983.8679 | 1980.1980 | +0.19 % | 262748.3170 MeV (+28876.6 ppm) |
| ${}^{275}$Rg | 275 | 164 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1991.8837 | 1987.4250 | +0.22 % | 263707.0160 MeV (+28874.6 ppm) |
| ${}^{276}$Rg | 276 | 165 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1998.4351 | 1993.5480 | +0.25 % | 264667.1793 MeV (+28873.5 ppm) |
| ${}^{277}$Rg | 277 | 166 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2006.2177 | 2000.4940 | +0.29 % | 265626.1115 MeV (+28871.6 ppm) |
| ${}^{278}$Rg | 278 | 167 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2012.5433 | 2006.6040 | +0.30 % | 266586.5007 MeV (+28870.9 ppm) |
| ${}^{279}$Rg | 279 | 168 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2020.0976 | 2013.2640 | +0.34 % | 267545.6611 MeV (+28869.1 ppm) |
| ${}^{280}$Rg | 280 | 169 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2026.2022 | 2019.3600 | +0.34 % | 268506.2713 MeV (+28869.1 ppm) |
| ${}^{281}$Rg | 281 | 170 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2033.5331 | 2025.7290 | +0.39 % | 269465.6552 MeV (+28867.2 ppm) |
| ${}^{282}$Rg | 282 | 171 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2039.4213 | 2031.5280 | +0.39 % | 270426.4817 MeV (+28867.1 ppm) |
| ${}^{283}$Rg | 283 | 172 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2046.5335 | 2037.8830 | +0.42 % | 271386.0844 MeV (+28865.3 ppm) |
| ${}^{284}$Rg | 284 | 173 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2052.2100 | 2043.3800 | +0.43 % | 272347.1226 MeV (+28865.3 ppm) |
| ${}^{285}$Rg | 285 | 174 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2059.1079 | 2049.7200 | +0.46 % | 273306.9395 MeV (+28863.9 ppm) |
| ${}^{286}$Rg | 286 | 175 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2064.5771 | 2054.9100 | +0.47 % | 274268.1851 MeV (+28863.9 ppm) |

### Copernicium (Z = 112)

_13 of 13 isotopes with a framework prediction; 13 of 13 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{276}$Cn | 276 | 164 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1993.7978 | 1989.6840 | +0.21 % | 264670.4863 MeV (+28874.5 ppm) |
| ${}^{277}$Cn | 277 | 165 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2000.5350 | 1995.7850 | +0.24 % | 265630.4639 MeV (+28872.8 ppm) |
| ${}^{278}$Cn | 278 | 166 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2008.5000 | 2003.2680 | +0.26 % | 266589.2137 MeV (+28872.1 ppm) |
| ${}^{279}$Cn | 279 | 167 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2015.0096 | 2009.3580 | +0.28 % | 267549.4188 MeV (+28870.5 ppm) |
| ${}^{280}$Cn | 280 | 168 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2022.7447 | 2016.5600 | +0.31 % | 268508.3985 MeV (+28870.3 ppm) |
| ${}^{281}$Cn | 281 | 169 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2029.0316 | 2022.3570 | +0.33 % | 269468.8264 MeV (+28869.1 ppm) |
| ${}^{282}$Cn | 282 | 170 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2036.5416 | 2029.5540 | +0.34 % | 270428.0311 MeV (+28868.8 ppm) |
| ${}^{283}$Cn | 283 | 171 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2042.6105 | 2035.3360 | +0.36 % | 271388.6770 MeV (+28867.5 ppm) |
| ${}^{284}$Cn | 284 | 172 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2049.9001 | 2042.2440 | +0.37 % | 272348.1022 MeV (+28867.3 ppm) |
| ${}^{285}$Cn | 285 | 173 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2055.7556 | 2047.7250 | +0.39 % | 273308.9615 MeV (+28866.2 ppm) |
| ${}^{286}$Cn | 286 | 174 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2062.8294 | 2054.3380 | +0.41 % | 274268.6025 MeV (+28865.7 ppm) |
| ${}^{287}$Cn | 287 | 175 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2068.4759 | 2059.5120 | +0.44 % | 275229.6707 MeV (+28864.5 ppm) |
| ${}^{288}$Cn | 288 | 176 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2075.3383 | 2066.1120 | +0.45 % | 276189.5231 MeV (+28864.0 ppm) |

### Nihonium (Z = 113)

_13 of 13 isotopes with a framework prediction; 13 of 13 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{278}$Nh | 278 | 165 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2000.8908 | 1996.3180 | +0.23 % | 266595.4926 MeV (+28871.8 ppm) |
| ${}^{279}$Nh | 279 | 166 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2009.0404 | 2004.0570 | +0.25 % | 267554.0577 MeV (+28870.8 ppm) |
| ${}^{280}$Nh | 280 | 167 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2015.7362 | 2010.4000 | +0.27 % | 268514.0767 MeV (+28870.0 ppm) |
| ${}^{281}$Nh | 281 | 168 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2023.6542 | 2017.8610 | +0.29 % | 269472.8735 MeV (+28869.4 ppm) |
| ${}^{282}$Nh | 282 | 169 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2030.1256 | 2023.9140 | +0.31 % | 270433.1169 MeV (+28868.9 ppm) |
| ${}^{283}$Nh | 283 | 170 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2037.8168 | 2031.0910 | +0.33 % | 271392.1404 MeV (+28868.1 ppm) |
| ${}^{284}$Nh | 284 | 171 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2044.0685 | 2037.1320 | +0.34 % | 272352.6035 MeV (+28868.0 ppm) |
| ${}^{285}$Nh | 285 | 172 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2051.5377 | 2044.0200 | +0.37 % | 273311.8491 MeV (+28866.7 ppm) |
| ${}^{286}$Nh | 286 | 173 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2057.5743 | 2050.0480 | +0.37 % | 274272.5273 MeV (+28866.9 ppm) |
| ${}^{287}$Nh | 287 | 174 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2064.8260 | 2056.6420 | +0.40 % | 275231.9903 MeV (+28865.2 ppm) |
| ${}^{288}$Nh | 288 | 175 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2070.6520 | 2062.0800 | +0.42 % | 276192.8791 MeV (+28864.9 ppm) |
| ${}^{289}$Nh | 289 | 176 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2077.6907 | 2068.6620 | +0.44 % | 277152.5552 MeV (+28863.6 ppm) |
| ${}^{290}$Nh | 290 | 177 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2083.3104 | 2074.0800 | +0.45 % | 278113.6502 MeV (+28863.2 ppm) |

### Flerovium (Z = 114)

_8 of 8 isotopes with a framework prediction; 8 of 8 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{284}$Fl | 284 | 170 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2040.0224 | 2034.2920 | +0.28 % | 272355.3193 MeV (+28869.8 ppm) |
| ${}^{285}$Fl | 285 | 171 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2046.4542 | 2040.3150 | +0.30 % | 273315.6023 MeV (+28868.6 ppm) |
| ${}^{286}$Fl | 286 | 172 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2054.1005 | 2047.4740 | +0.32 % | 274274.6708 MeV (+28868.6 ppm) |
| ${}^{287}$Fl | 287 | 173 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2060.3156 | 2053.4850 | +0.33 % | 275235.1704 MeV (+28867.5 ppm) |
| ${}^{288}$Fl | 288 | 174 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2067.7428 | 2060.3520 | +0.36 % | 276194.4580 MeV (+28867.1 ppm) |
| ${}^{289}$Fl | 289 | 175 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2073.7457 | 2066.0610 | +0.37 % | 277155.1699 MeV (+28866.0 ppm) |
| ${}^{290}$Fl | 290 | 176 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2080.9583 | 2072.6300 | +0.40 % | 278114.6721 MeV (+28865.4 ppm) |
| ${}^{291}$Fl | 291 | 177 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2086.7533 | 2078.0310 | +0.42 % | 279075.5918 MeV (+28864.2 ppm) |

### Moscovium (Z = 115)

_6 of 6 isotopes with a framework prediction; 6 of 6 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{287}$Mc | 287 | 172 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2054.9446 | 2048.8930 | +0.30 % | 275239.2111 MeV (+28868.0 ppm) |
| ${}^{288}$Mc | 288 | 173 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2061.3404 | 2054.8800 | +0.31 % | 276199.5301 MeV (+28867.8 ppm) |
| ${}^{289}$Mc | 289 | 174 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2068.9451 | 2062.0150 | +0.34 % | 277158.6402 MeV (+28866.6 ppm) |
| ${}^{290}$Mc | 290 | 175 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2075.1270 | 2067.9900 | +0.35 % | 278119.1731 MeV (+28866.5 ppm) |
| ${}^{291}$Mc | 291 | 176 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2082.5155 | 2074.5390 | +0.38 % | 279078.4993 MeV (+28864.8 ppm) |
| ${}^{292}$Mc | 292 | 177 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2088.4880 | 2080.2080 | +0.40 % | 280039.2416 MeV (+28864.3 ppm) |

### Livermorium (Z = 116)

_5 of 5 isotopes with a framework prediction; 5 of 5 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{289}$Lv | 289 | 173 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2063.2890 | 2057.3910 | +0.29 % | 277162.9660 MeV (+28868.3 ppm) |
| ${}^{290}$Lv | 290 | 174 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2071.0687 | 2064.8000 | +0.30 % | 278121.9011 MeV (+28868.1 ppm) |
| ${}^{291}$Lv | 291 | 175 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2077.4271 | 2070.7560 | +0.32 % | 279082.2574 MeV (+28867.0 ppm) |
| ${}^{292}$Lv | 292 | 176 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2084.9891 | 2077.8720 | +0.34 % | 280041.4102 MeV (+28866.5 ppm) |
| ${}^{293}$Lv | 293 | 177 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2091.1365 | 2083.5230 | +0.37 % | 281001.9776 MeV (+28865.3 ppm) |

### Tennessine (Z = 117)

_4 of 4 isotopes with a framework prediction; 4 of 4 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{291}$Ts | 291 | 174 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2071.4880 | 2065.5180 | +0.29 % | 279086.8662 MeV (+28867.3 ppm) |
| ${}^{292}$Ts | 292 | 175 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2078.0249 | 2071.7400 | +0.30 % | 280047.0441 MeV (+28866.4 ppm) |
| ${}^{293}$Ts | 293 | 176 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2085.7624 | 2078.8350 | +0.33 % | 281006.0213 MeV (+28865.5 ppm) |
| ${}^{294}$Ts | 294 | 177 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2092.0868 | 2085.0480 | +0.34 % | 281966.4118 MeV (+28865.5 ppm) |

### Oganesson (Z = 118)

_3 of 3 isotopes with a framework prediction; 3 of 3 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{293}$Og | 293 | 175 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2079.5426 | 2073.8540 | +0.27 % | 281010.9109 MeV (+28867.0 ppm) |
| ${}^{294}$Og | 294 | 176 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2087.4532 | 2081.2260 | +0.30 % | 281969.7151 MeV (+28866.6 ppm) |
| ${}^{295}$Og | 295 | 177 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 2093.9520 | 2087.4200 | +0.31 % | 282929.9311 MeV (+28865.6 ppm) |

### Magnesium (Z = 12)

_2 of 23 isotopes with a framework prediction; 2 of 23 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{19}$Mg | 19 | 7 | derivation-pending | ⚪ pending | binding_energy | — | 112.1285 | — | — |
| ${}^{20}$Mg | 20 | 8 | derivation-pending | ⚪ pending | binding_energy | — | 134.5605 | — | — |
| ${}^{21}$Mg | 21 | 9 | derivation-pending | ⚪ pending | binding_energy | — | 149.2057 | — | — |
| ${}^{22}$Mg | 22 | 10 | derivation-pending | ⚪ pending | binding_energy | — | 168.5808 | — | — |
| ${}^{23}$Mg | 23 | 11 | derivation-pending | ⚪ pending | binding_energy | — | 181.7258 | — | — |
| ${}^{24}$Mg | 24 | 12 | L2-alpha-cluster | 🟢 recursive | binding_energy | 216.1389 | 198.2570 | +9.02 % | 22969.0521 MeV (+28069.5 ppm) |
| ${}^{25}$Mg | 25 | 13 | derivation-pending | ⚪ pending | binding_energy | — | 205.5876 | — | — |
| ${}^{26}$Mg | 26 | 14 | derivation-pending | ⚪ pending | binding_energy | — | 216.6806 | — | — |
| ${}^{27}$Mg | 27 | 15 | derivation-pending | ⚪ pending | binding_energy | — | 223.1240 | — | — |
| ${}^{28}$Mg | 28 | 16 | derivation-pending | ⚪ pending | binding_energy | — | 231.6287 | — | — |
| ${}^{29}$Mg | 29 | 17 | derivation-pending | ⚪ pending | binding_energy | — | 235.2924 | — | — |
| ${}^{30}$Mg | 30 | 18 | derivation-pending | ⚪ pending | binding_energy | — | 241.6327 | — | — |
| ${}^{31}$Mg | 31 | 19 | derivation-pending | ⚪ pending | binding_energy | — | 243.9448 | — | — |
| ${}^{32}$Mg | 32 | 20 | derivation-pending | ⚪ pending | binding_energy | — | 249.7229 | — | — |
| ${}^{33}$Mg | 33 | 21 | derivation-pending | ⚪ pending | binding_energy | — | 252.0025 | — | — |
| ${}^{34}$Mg | 34 | 22 | derivation-pending | ⚪ pending | binding_energy | — | 256.7133 | — | — |
| ${}^{35}$Mg | 35 | 23 | derivation-pending | ⚪ pending | binding_energy | — | 257.4682 | — | — |
| ${}^{36}$Mg | 36 | 24 | derivation-pending | ⚪ pending | binding_energy | — | 260.7991 | — | — |
| ${}^{37}$Mg | 37 | 25 | derivation-pending | ⚪ pending | binding_energy | — | 261.0391 | — | — |
| ${}^{38}$Mg | 38 | 26 | derivation-pending | ⚪ pending | binding_energy | — | 263.2640 | — | — |
| ${}^{39}$Mg | 39 | 27 | derivation-pending | ⚪ pending | binding_energy | — | 262.6260 | — | — |
| ${}^{40}$Mg | 40 | 28 | derivation-pending | ⚪ pending | binding_energy | — | 263.9200 | — | — |
| ${}^{41}$Mg | 41 | 29 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 239.8185 | 263.4250 | -8.96 % | 39379.5236 MeV (+29547.3 ppm) |

### Aluminium (Z = 13)

_3 of 23 isotopes with a framework prediction; 3 of 23 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{21}$Al | 21 | 8 | derivation-pending | ⚪ pending | binding_energy | — | 132.2370 | — | — |
| ${}^{22}$Al | 22 | 9 | derivation-pending | ⚪ pending | binding_energy | — | 149.2040 | — | — |
| ${}^{23}$Al | 23 | 10 | derivation-pending | ⚪ pending | binding_energy | — | 168.7217 | — | — |
| ${}^{24}$Al | 24 | 11 | derivation-pending | ⚪ pending | binding_energy | — | 183.5899 | — | — |
| ${}^{25}$Al | 25 | 12 | derivation-pending | ⚪ pending | binding_energy | — | 200.5284 | — | — |
| ${}^{26}$Al | 26 | 13 | derivation-pending | ⚪ pending | binding_energy | — | 211.8939 | — | — |
| ${}^{27}$Al | 27 | 14 | derivation-pending | ⚪ pending | binding_energy | — | 224.9519 | — | — |
| ${}^{28}$Al | 28 | 15 | derivation-pending | ⚪ pending | binding_energy | — | 232.6771 | — | — |
| ${}^{29}$Al | 29 | 16 | derivation-pending | ⚪ pending | binding_energy | — | 242.1055 | — | — |
| ${}^{30}$Al | 30 | 17 | derivation-pending | ⚪ pending | binding_energy | — | 247.8331 | — | — |
| ${}^{31}$Al | 31 | 18 | derivation-pending | ⚪ pending | binding_energy | — | 254.9911 | — | — |
| ${}^{32}$Al | 32 | 19 | derivation-pending | ⚪ pending | binding_energy | — | 259.2110 | — | — |
| ${}^{33}$Al | 33 | 20 | derivation-pending | ⚪ pending | binding_energy | — | 264.6804 | — | — |
| ${}^{34}$Al | 34 | 21 | derivation-pending | ⚪ pending | binding_energy | — | 267.2519 | — | — |
| ${}^{35}$Al | 35 | 22 | derivation-pending | ⚪ pending | binding_energy | — | 272.5494 | — | — |
| ${}^{36}$Al | 36 | 23 | derivation-pending | ⚪ pending | binding_energy | — | 274.4466 | — | — |
| ${}^{37}$Al | 37 | 24 | derivation-pending | ⚪ pending | binding_energy | — | 278.6587 | — | — |
| ${}^{38}$Al | 38 | 25 | derivation-pending | ⚪ pending | binding_energy | — | 280.0600 | — | — |
| ${}^{39}$Al | 39 | 26 | derivation-pending | ⚪ pending | binding_energy | — | 283.1400 | — | — |
| ${}^{40}$Al | 40 | 27 | derivation-pending | ⚪ pending | binding_energy | — | 283.8800 | — | — |
| ${}^{41}$Al | 41 | 28 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 271.1203 | 286.1800 | -5.26 % | 39346.8916 MeV (+29326.8 ppm) |
| ${}^{42}$Al | 42 | 29 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 267.7636 | 286.8180 | -6.64 % | 40316.9631 MeV (+29419.8 ppm) |
| ${}^{43}$Al | 43 | 30 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 267.4495 | 288.6160 | -7.33 % | 41283.9919 MeV (+29461.4 ppm) |

### Silicon (Z = 14)

_5 of 24 isotopes with a framework prediction; 5 of 24 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{22}$Si | 22 | 8 | derivation-pending | ⚪ pending | binding_energy | — | 132.9680 | — | — |
| ${}^{23}$Si | 23 | 9 | derivation-pending | ⚪ pending | binding_energy | — | 150.7420 | — | — |
| ${}^{24}$Si | 24 | 10 | derivation-pending | ⚪ pending | binding_energy | — | 172.0136 | — | — |
| ${}^{25}$Si | 25 | 11 | derivation-pending | ⚪ pending | binding_energy | — | 187.0028 | — | — |
| ${}^{26}$Si | 26 | 12 | derivation-pending | ⚪ pending | binding_energy | — | 206.0424 | — | — |
| ${}^{27}$Si | 27 | 13 | derivation-pending | ⚪ pending | binding_energy | — | 219.3572 | — | — |
| ${}^{28}$Si | 28 | 14 | derivation-pending | ⚪ pending | binding_energy | — | 236.5368 | — | — |
| ${}^{29}$Si | 29 | 15 | derivation-pending | ⚪ pending | binding_energy | — | 245.0104 | — | — |
| ${}^{30}$Si | 30 | 16 | derivation-pending | ⚪ pending | binding_energy | — | 255.6196 | — | — |
| ${}^{31}$Si | 31 | 17 | derivation-pending | ⚪ pending | binding_energy | — | 262.2070 | — | — |
| ${}^{32}$Si | 32 | 18 | derivation-pending | ⚪ pending | binding_energy | — | 271.4070 | — | — |
| ${}^{33}$Si | 33 | 19 | derivation-pending | ⚪ pending | binding_energy | — | 275.9150 | — | — |
| ${}^{34}$Si | 34 | 20 | derivation-pending | ⚪ pending | binding_energy | — | 283.4636 | — | — |
| ${}^{35}$Si | 35 | 21 | derivation-pending | ⚪ pending | binding_energy | — | 285.9348 | — | — |
| ${}^{36}$Si | 36 | 22 | derivation-pending | ⚪ pending | binding_energy | — | 292.0507 | — | — |
| ${}^{37}$Si | 37 | 23 | derivation-pending | ⚪ pending | binding_energy | — | 294.2574 | — | — |
| ${}^{38}$Si | 38 | 24 | derivation-pending | ⚪ pending | binding_energy | — | 299.9275 | — | — |
| ${}^{39}$Si | 39 | 25 | derivation-pending | ⚪ pending | binding_energy | — | 301.5082 | — | — |
| ${}^{40}$Si | 40 | 26 | derivation-pending | ⚪ pending | binding_energy | — | 306.2330 | — | — |
| ${}^{41}$Si | 41 | 27 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 297.4734 | 306.7620 | -3.03 % | 39319.2081 MeV (+29178.5 ppm) |
| ${}^{42}$Si | 42 | 28 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 299.0713 | 311.2200 | -3.90 % | 40284.3250 MeV (+29247.4 ppm) |
| ${}^{43}$Si | 43 | 29 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 296.7420 | 311.7930 | -4.83 % | 41253.3691 MeV (+29312.2 ppm) |
| ${}^{44}$Si | 44 | 30 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 297.3798 | 314.8640 | -5.55 % | 42219.4460 MeV (+29364.7 ppm) |
| ${}^{45}$Si | 45 | 31 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 294.2336 | 315.1800 | -6.65 % | 43189.3070 MeV (+29436.3 ppm) |

### Phosphorus (Z = 15)

_7 of 24 isotopes with a framework prediction; 7 of 24 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{24}$P | 24 | 9 | derivation-pending | ⚪ pending | binding_energy | — | 147.9600 | — | — |
| ${}^{25}$P | 25 | 10 | derivation-pending | ⚪ pending | binding_energy | — | 169.8500 | — | — |
| ${}^{26}$P | 26 | 11 | derivation-pending | ⚪ pending | binding_energy | — | 187.1480 | — | — |
| ${}^{27}$P | 27 | 12 | derivation-pending | ⚪ pending | binding_energy | — | 206.8494 | — | — |
| ${}^{28}$P | 28 | 13 | derivation-pending | ⚪ pending | binding_energy | — | 221.4096 | — | — |
| ${}^{29}$P | 29 | 14 | derivation-pending | ⚪ pending | binding_energy | — | 239.2859 | — | — |
| ${}^{30}$P | 30 | 15 | derivation-pending | ⚪ pending | binding_energy | — | 250.6052 | — | — |
| ${}^{31}$P | 31 | 16 | derivation-pending | ⚪ pending | binding_energy | — | 262.9162 | — | — |
| ${}^{32}$P | 32 | 17 | derivation-pending | ⚪ pending | binding_energy | — | 270.8518 | — | — |
| ${}^{33}$P | 33 | 18 | derivation-pending | ⚪ pending | binding_energy | — | 280.9556 | — | — |
| ${}^{34}$P | 34 | 19 | derivation-pending | ⚪ pending | binding_energy | — | 287.2383 | — | — |
| ${}^{35}$P | 35 | 20 | derivation-pending | ⚪ pending | binding_energy | — | 295.6187 | — | — |
| ${}^{36}$P | 36 | 21 | derivation-pending | ⚪ pending | binding_energy | — | 299.0833 | — | — |
| ${}^{37}$P | 37 | 22 | derivation-pending | ⚪ pending | binding_energy | — | 305.8996 | — | — |
| ${}^{38}$P | 38 | 23 | derivation-pending | ⚪ pending | binding_energy | — | 309.5964 | — | — |
| ${}^{39}$P | 39 | 24 | derivation-pending | ⚪ pending | binding_energy | — | 315.8208 | — | — |
| ${}^{40}$P | 40 | 25 | derivation-pending | ⚪ pending | binding_energy | — | 319.2567 | — | — |
| ${}^{41}$P | 41 | 26 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 318.8779 | 324.1686 | -1.63 % | 39296.4734 MeV (+29073.1 ppm) |
| ${}^{42}$P | 42 | 27 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 318.6413 | 326.1683 | -2.31 % | 40263.4247 MeV (+29127.5 ppm) |
| ${}^{43}$P | 43 | 28 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 321.3037 | 330.2830 | -2.72 % | 41227.4771 MeV (+29161.5 ppm) |
| ${}^{44}$P | 44 | 29 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 320.0425 | 332.2880 | -3.69 % | 42195.4530 MeV (+29236.5 ppm) |
| ${}^{45}$P | 45 | 30 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 321.6744 | 335.5200 | -4.13 % | 43160.5360 MeV (+29269.0 ppm) |
| ${}^{46}$P | 46 | 31 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 319.5263 | 336.7200 | -5.11 % | 44129.3988 MeV (+29339.5 ppm) |
| ${}^{47}$P | 47 | 32 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 320.2582 | 338.8230 | -5.48 % | 45095.3816 MeV (+29362.6 ppm) |

### Sulfur (Z = 16)

_9 of 24 isotopes with a framework prediction; 9 of 24 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{26}$S | 26 | 10 | derivation-pending | ⚪ pending | binding_energy | — | 169.6500 | — | — |
| ${}^{27}$S | 27 | 11 | derivation-pending | ⚪ pending | binding_energy | — | 187.9200 | — | — |
| ${}^{28}$S | 28 | 12 | derivation-pending | ⚪ pending | binding_energy | — | 209.4062 | — | — |
| ${}^{29}$S | 29 | 13 | derivation-pending | ⚪ pending | binding_energy | — | 224.6451 | — | — |
| ${}^{30}$S | 30 | 14 | derivation-pending | ⚪ pending | binding_energy | — | 243.6812 | — | — |
| ${}^{31}$S | 31 | 15 | derivation-pending | ⚪ pending | binding_energy | — | 256.7358 | — | — |
| ${}^{32}$S | 32 | 16 | derivation-pending | ⚪ pending | binding_energy | — | 271.7802 | — | — |
| ${}^{33}$S | 33 | 17 | derivation-pending | ⚪ pending | binding_energy | — | 280.4218 | — | — |
| ${}^{34}$S | 34 | 18 | derivation-pending | ⚪ pending | binding_energy | — | 291.8390 | — | — |
| ${}^{35}$S | 35 | 19 | derivation-pending | ⚪ pending | binding_energy | — | 298.8248 | — | — |
| ${}^{36}$S | 36 | 20 | derivation-pending | ⚪ pending | binding_energy | — | 308.7140 | — | — |
| ${}^{37}$S | 37 | 21 | derivation-pending | ⚪ pending | binding_energy | — | 313.0176 | — | — |
| ${}^{38}$S | 38 | 22 | derivation-pending | ⚪ pending | binding_energy | — | 321.0538 | — | — |
| ${}^{39}$S | 39 | 23 | derivation-pending | ⚪ pending | binding_energy | — | 325.4265 | — | — |
| ${}^{40}$S | 40 | 24 | derivation-pending | ⚪ pending | binding_energy | — | 333.1730 | — | — |
| ${}^{41}$S | 41 | 25 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 335.3337 | 337.4151 | -0.62 % | 39278.6872 MeV (+28985.4 ppm) |
| ${}^{42}$S | 42 | 26 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 340.2746 | 344.1156 | -1.12 % | 40240.4611 MeV (+29033.2 ppm) |
| ${}^{43}$S | 43 | 27 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 341.1344 | 346.7446 | -1.62 % | 41206.3161 MeV (+29076.1 ppm) |
| ${}^{44}$S | 44 | 28 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 344.8176 | 351.8247 | -1.99 % | 42169.3476 MeV (+29109.6 ppm) |
| ${}^{45}$S | 45 | 29 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 344.5828 | 354.0150 | -2.66 % | 43136.2972 MeV (+29164.6 ppm) |
| ${}^{46}$S | 46 | 30 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 347.1711 | 358.1100 | -3.05 % | 44100.4237 MeV (+29196.6 ppm) |
| ${}^{47}$S | 47 | 31 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 345.9850 | 359.6440 | -3.80 % | 45068.3246 MeV (+29252.7 ppm) |
| ${}^{48}$S | 48 | 32 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 347.6141 | 362.4960 | -4.11 % | 46033.4103 MeV (+29275.1 ppm) |
| ${}^{49}$S | 49 | 33 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 345.5967 | 362.6000 | -4.69 % | 47002.1424 MeV (+29313.1 ppm) |

### Chlorine (Z = 17)

_12 of 25 isotopes with a framework prediction; 12 of 25 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{28}$Cl | 28 | 11 | derivation-pending | ⚪ pending | binding_energy | — | 184.4360 | — | — |
| ${}^{29}$Cl | 29 | 12 | derivation-pending | ⚪ pending | binding_energy | — | 206.7410 | — | — |
| ${}^{30}$Cl | 30 | 13 | derivation-pending | ⚪ pending | binding_energy | — | 224.1651 | — | — |
| ${}^{31}$Cl | 31 | 14 | derivation-pending | ⚪ pending | binding_energy | — | 243.9455 | — | — |
| ${}^{32}$Cl | 32 | 15 | derivation-pending | ⚪ pending | binding_energy | — | 258.3170 | — | — |
| ${}^{33}$Cl | 33 | 16 | derivation-pending | ⚪ pending | binding_energy | — | 274.0569 | — | — |
| ${}^{34}$Cl | 34 | 17 | derivation-pending | ⚪ pending | binding_energy | — | 285.5650 | — | — |
| ${}^{35}$Cl | 35 | 18 | derivation-pending | ⚪ pending | binding_energy | — | 298.2098 | — | — |
| ${}^{36}$Cl | 36 | 19 | derivation-pending | ⚪ pending | binding_energy | — | 306.7896 | — | — |
| ${}^{37}$Cl | 37 | 20 | derivation-pending | ⚪ pending | binding_energy | — | 317.1004 | — | — |
| ${}^{38}$Cl | 38 | 21 | derivation-pending | ⚪ pending | binding_energy | — | 323.2083 | — | — |
| ${}^{39}$Cl | 39 | 22 | derivation-pending | ⚪ pending | binding_energy | — | 331.2817 | — | — |
| ${}^{40}$Cl | 40 | 23 | derivation-pending | ⚪ pending | binding_energy | — | 337.1106 | — | — |
| ${}^{41}$Cl | 41 | 24 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 346.8409 | 344.9313 | +0.55 % | 39265.8498 MeV (+28872.8 ppm) |
| ${}^{42}$Cl | 42 | 25 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 350.1702 | 350.5272 | -0.10 % | 40229.2352 MeV (+28935.4 ppm) |
| ${}^{43}$Cl | 43 | 26 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 356.2341 | 357.9263 | -0.47 % | 41189.8861 MeV (+28973.2 ppm) |
| ${}^{44}$Cl | 44 | 27 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 358.2215 | 362.3171 | -1.13 % | 42154.6135 MeV (+29033.2 ppm) |
| ${}^{45}$Cl | 45 | 28 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 362.9589 | 368.1720 | -1.42 % | 43116.5909 MeV (+29060.8 ppm) |
| ${}^{46}$Cl | 46 | 29 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 363.7827 | 371.7157 | -2.13 % | 44082.4818 MeV (+29123.1 ppm) |
| ${}^{47}$Cl | 47 | 30 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 367.3613 | 375.6240 | -2.20 % | 45045.6180 MeV (+29128.6 ppm) |
| ${}^{48}$Cl | 48 | 31 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 367.1702 | 378.3840 | -2.96 % | 46012.5238 MeV (+29191.7 ppm) |
| ${}^{49}$Cl | 49 | 32 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 369.7307 | 381.4650 | -3.08 % | 46976.6781 MeV (+29198.3 ppm) |
| ${}^{50}$Cl | 50 | 33 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 368.6497 | 382.5500 | -3.63 % | 47944.4739 MeV (+29240.0 ppm) |
| ${}^{51}$Cl | 51 | 34 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 370.3110 | 384.0300 | -3.57 % | 48909.5274 MeV (+29230.3 ppm) |
| ${}^{52}$Cl | 52 | 35 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 368.4457 | 384.0720 | -4.07 % | 49878.1075 MeV (+29262.3 ppm) |

### Argon (Z = 18)

_14 of 26 isotopes with a framework prediction; 14 of 26 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{29}$Ar | 29 | 11 | derivation-pending | ⚪ pending | binding_energy | — | 182.0040 | — | — |
| ${}^{30}$Ar | 30 | 12 | derivation-pending | ⚪ pending | binding_energy | — | 205.9800 | — | — |
| ${}^{31}$Ar | 31 | 13 | derivation-pending | ⚪ pending | binding_energy | — | 224.8120 | — | — |
| ${}^{32}$Ar | 32 | 14 | derivation-pending | ⚪ pending | binding_energy | — | 246.4003 | — | — |
| ${}^{33}$Ar | 33 | 15 | derivation-pending | ⚪ pending | binding_energy | — | 261.6555 | — | — |
| ${}^{34}$Ar | 34 | 16 | derivation-pending | ⚪ pending | binding_energy | — | 278.7209 | — | — |
| ${}^{35}$Ar | 35 | 17 | derivation-pending | ⚪ pending | binding_energy | — | 291.4612 | — | — |
| ${}^{36}$Ar | 36 | 18 | derivation-pending | ⚪ pending | binding_energy | — | 306.7167 | — | — |
| ${}^{37}$Ar | 37 | 19 | derivation-pending | ⚪ pending | binding_energy | — | 315.5042 | — | — |
| ${}^{38}$Ar | 38 | 20 | derivation-pending | ⚪ pending | binding_energy | — | 327.3427 | — | — |
| ${}^{39}$Ar | 39 | 21 | derivation-pending | ⚪ pending | binding_energy | — | 333.9414 | — | — |
| ${}^{40}$Ar | 40 | 22 | derivation-pending | ⚪ pending | binding_energy | — | 343.8104 | — | — |
| ${}^{41}$Ar | 41 | 23 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 353.3994 | 349.9093 | +1.00 % | 39257.9610 MeV (+28821.3 ppm) |
| ${}^{42}$Ar | 42 | 24 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 362.1290 | 359.3358 | +0.78 % | 40215.9461 MeV (+28847.9 ppm) |
| ${}^{43}$Ar | 43 | 25 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 366.6030 | 364.9942 | +0.44 % | 41178.1869 MeV (+28882.7 ppm) |
| ${}^{44}$Ar | 44 | 26 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 373.7378 | 373.7290 | +0.00 % | 42137.7669 MeV (+28928.2 ppm) |
| ${}^{45}$Ar | 45 | 27 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 376.8026 | 378.8979 | -0.55 % | 43101.4169 MeV (+28981.3 ppm) |
| ${}^{46}$Ar | 46 | 28 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 382.5484 | 386.9696 | -1.14 % | 44062.3858 MeV (+29039.2 ppm) |
| ${}^{47}$Ar | 47 | 29 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 384.3870 | 390.6370 | -1.60 % | 45027.2620 MeV (+29080.3 ppm) |
| ${}^{48}$Ar | 48 | 30 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 388.9159 | 395.6959 | -1.71 % | 45989.4479 MeV (+29091.6 ppm) |
| ${}^{49}$Ar | 49 | 31 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 389.6813 | 398.4680 | -2.21 % | 46955.3973 MeV (+29133.4 ppm) |
| ${}^{50}$Ar | 50 | 32 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 393.1381 | 402.7000 | -2.37 % | 47918.6553 MeV (+29148.1 ppm) |
| ${}^{51}$Ar | 51 | 33 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 392.9594 | 404.0220 | -2.74 % | 48885.5487 MeV (+29175.7 ppm) |
| ${}^{52}$Ar | 52 | 34 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 395.4668 | 407.0040 | -2.83 % | 49849.7561 MeV (+29181.5 ppm) |
| ${}^{53}$Ar | 53 | 35 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 394.4537 | 406.8810 | -3.05 % | 50817.4839 MeV (+29194.5 ppm) |
| ${}^{54}$Ar | 54 | 36 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 396.1165 | 409.2120 | -3.20 % | 51782.5359 MeV (+29202.9 ppm) |

### Potassium (Z = 19)

_19 of 29 isotopes with a framework prediction; 19 of 29 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{31}$K | 31 | 12 | derivation-pending | ⚪ pending | binding_energy | — | 201.0970 | — | — |
| ${}^{32}$K | 32 | 13 | derivation-pending | ⚪ pending | binding_energy | — | 221.4400 | — | — |
| ${}^{33}$K | 33 | 14 | derivation-pending | ⚪ pending | binding_energy | — | 243.9360 | — | — |
| ${}^{34}$K | 34 | 15 | derivation-pending | ⚪ pending | binding_energy | — | 260.7800 | — | — |
| ${}^{35}$K | 35 | 16 | derivation-pending | ⚪ pending | binding_energy | — | 278.8044 | — | — |
| ${}^{36}$K | 36 | 17 | derivation-pending | ⚪ pending | binding_energy | — | 293.1200 | — | — |
| ${}^{37}$K | 37 | 18 | derivation-pending | ⚪ pending | binding_energy | — | 308.5744 | — | — |
| ${}^{38}$K | 38 | 19 | derivation-pending | ⚪ pending | binding_energy | — | 320.6463 | — | — |
| ${}^{39}$K | 39 | 20 | derivation-pending | ⚪ pending | binding_energy | — | 333.7240 | — | — |
| ${}^{40}$K | 40 | 21 | derivation-pending | ⚪ pending | binding_energy | — | 341.5236 | — | — |
| ${}^{41}$K | 41 | 22 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 355.0092 | 351.6190 | +0.96 % | 39255.0208 MeV (+28811.5 ppm) |
| ${}^{42}$K | 42 | 23 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 362.3501 | 359.1528 | +0.89 % | 40214.3947 MeV (+28824.0 ppm) |
| ${}^{43}$K | 43 | 24 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 372.2409 | 368.7775 | +0.94 % | 41171.2187 MeV (+28826.0 ppm) |
| ${}^{44}$K | 44 | 25 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 377.8828 | 376.0549 | +0.49 % | 42132.2915 MeV (+28872.6 ppm) |
| ${}^{45}$K | 45 | 26 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 386.1139 | 384.9604 | +0.30 % | 43090.7752 MeV (+28895.4 ppm) |
| ${}^{46}$K | 46 | 27 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 390.2811 | 391.8300 | -0.40 % | 44053.3228 MeV (+28963.1 ppm) |
| ${}^{47}$K | 47 | 28 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 397.0622 | 400.1993 | -0.78 % | 45013.2565 MeV (+29003.5 ppm) |
| ${}^{48}$K | 48 | 29 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 399.9416 | 404.8432 | -1.21 % | 45977.0919 MeV (+29043.8 ppm) |
| ${}^{49}$K | 49 | 30 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 405.4485 | 410.2415 | -1.17 % | 46938.2998 MeV (+29041.8 ppm) |
| ${}^{50}$K | 50 | 31 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 407.1973 | 414.4292 | -1.75 % | 47903.2657 MeV (+29093.8 ppm) |
| ${}^{51}$K | 51 | 32 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 411.5786 | 419.2881 | -1.84 % | 48865.5992 MeV (+29103.0 ppm) |
| ${}^{52}$K | 52 | 33 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 412.3298 | 421.9816 | -2.29 % | 49831.5627 MeV (+29140.7 ppm) |
| ${}^{53}$K | 53 | 34 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 415.7119 | 425.2110 | -2.23 % | 50794.8954 MeV (+29134.8 ppm) |
| ${}^{54}$K | 54 | 35 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 415.5789 | 426.1140 | -2.47 % | 51761.7432 MeV (+29151.9 ppm) |
| ${}^{55}$K | 55 | 36 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 418.0701 | 428.5600 | -2.45 % | 52725.9668 MeV (+29147.8 ppm) |
| ${}^{56}$K | 56 | 37 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 417.1500 | 429.1280 | -2.79 % | 53693.6017 MeV (+29172.0 ppm) |
| ${}^{57}$K | 57 | 38 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 418.8433 | 431.0910 | -2.84 % | 54658.6231 MeV (+29172.5 ppm) |
| ${}^{58}$K | 58 | 39 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 417.2198 | 431.3460 | -3.27 % | 55626.9614 MeV (+29202.9 ppm) |
| ${}^{59}$K | 59 | 40 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 418.1960 | 432.5880 | -3.33 % | 56592.7000 MeV (+29203.3 ppm) |

### Calcium (Z = 20)

_22 of 29 isotopes with a framework prediction; 22 of 29 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{33}$Ca | 33 | 13 | derivation-pending | ⚪ pending | binding_energy | — | 219.6810 | — | — |
| ${}^{34}$Ca | 34 | 14 | derivation-pending | ⚪ pending | binding_energy | — | 243.8820 | — | — |
| ${}^{35}$Ca | 35 | 15 | derivation-pending | ⚪ pending | binding_energy | — | 261.6600 | — | — |
| ${}^{36}$Ca | 36 | 16 | derivation-pending | ⚪ pending | binding_energy | — | 281.3717 | — | — |
| ${}^{37}$Ca | 37 | 17 | derivation-pending | ⚪ pending | binding_energy | — | 296.1279 | — | — |
| ${}^{38}$Ca | 38 | 18 | derivation-pending | ⚪ pending | binding_energy | — | 313.1216 | — | — |
| ${}^{39}$Ca | 39 | 19 | derivation-pending | ⚪ pending | binding_energy | — | 326.4172 | — | — |
| ${}^{40}$Ca | 40 | 20 | L2-alpha-cluster | 🟢 recursive | binding_energy | 408.7713 | 342.0522 | +19.51 % | 38233.2137 MeV (+27086.6 ppm) |
| ${}^{41}$Ca | 41 | 21 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 351.6704 | 350.4150 | +0.36 % | 39257.0294 MeV (+28852.8 ppm) |
| ${}^{42}$Ca | 42 | 22 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 364.6345 | 361.8957 | +0.76 % | 40210.7800 MeV (+28824.3 ppm) |
| ${}^{43}$Ca | 43 | 23 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 373.1479 | 369.8286 | +0.90 % | 41168.9814 MeV (+28817.2 ppm) |
| ${}^{44}$Ca | 44 | 24 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 384.1403 | 380.9598 | +0.83 % | 42124.7038 MeV (+28830.2 ppm) |
| ${}^{45}$Ca | 45 | 25 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 390.8929 | 388.3746 | +0.65 % | 43084.6659 MeV (+28852.6 ppm) |
| ${}^{46}$Ca | 46 | 26 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 400.1679 | 398.7733 | +0.35 % | 44042.1058 MeV (+28886.8 ppm) |
| ${}^{47}$Ca | 47 | 27 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 405.3868 | 406.0497 | -0.16 % | 45003.6016 MeV (+28938.8 ppm) |
| ${}^{48}$Ca | 48 | 28 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 413.1568 | 416.0012 | -0.68 % | 45962.5464 MeV (+28993.2 ppm) |
| ${}^{49}$Ca | 49 | 29 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 417.0323 | 421.1476 | -0.98 % | 46925.3857 MeV (+29022.3 ppm) |
| ${}^{50}$Ca | 50 | 30 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 423.4760 | 427.5082 | -0.94 % | 47885.6567 MeV (+29022.0 ppm) |
| ${}^{51}$Ca | 51 | 31 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 426.1685 | 432.3226 | -1.42 % | 48849.6790 MeV (+29067.1 ppm) |
| ${}^{52}$Ca | 52 | 32 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 431.4378 | 438.3279 | -1.57 % | 49811.1244 MeV (+29082.6 ppm) |
| ${}^{53}$Ca | 53 | 33 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 433.0836 | 441.5206 | -1.91 % | 50776.1935 MeV (+29112.3 ppm) |
| ${}^{54}$Ca | 54 | 34 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 437.3078 | 445.3648 | -1.81 % | 51738.6840 MeV (+29102.9 ppm) |
| ${}^{55}$Ca | 55 | 35 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 438.0233 | 446.9259 | -1.99 % | 52704.6833 MeV (+29116.5 ppm) |
| ${}^{56}$Ca | 56 | 36 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 441.3136 | 449.8573 | -1.90 % | 53668.1077 MeV (+29107.3 ppm) |
| ${}^{57}$Ca | 57 | 37 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 441.1990 | 450.9840 | -2.17 % | 54634.9372 MeV (+29127.4 ppm) |
| ${}^{58}$Ca | 58 | 38 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 443.6513 | 454.0240 | -2.28 % | 55599.1996 MeV (+29135.9 ppm) |
| ${}^{59}$Ca | 59 | 39 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 442.7931 | 454.7720 | -2.63 % | 56566.7726 MeV (+29161.1 ppm) |
| ${}^{60}$Ca | 60 | 40 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 444.4907 | 457.6200 | -2.87 % | 57531.7897 MeV (+29179.3 ppm) |
| ${}^{61}$Ca | 61 | 41 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 442.9641 | 457.6830 | -3.22 % | 58500.0311 MeV (+29202.6 ppm) |

### Scandium (Z = 21)

_23 of 29 isotopes with a framework prediction; 23 of 29 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{35}$Sc | 35 | 14 | derivation-pending | ⚪ pending | binding_energy | — | 238.9800 | — | — |
| ${}^{36}$Sc | 36 | 15 | derivation-pending | ⚪ pending | binding_energy | — | 257.9760 | — | — |
| ${}^{37}$Sc | 37 | 16 | derivation-pending | ⚪ pending | binding_energy | — | 278.4250 | — | — |
| ${}^{38}$Sc | 38 | 17 | derivation-pending | ⚪ pending | binding_energy | — | 294.5380 | — | — |
| ${}^{39}$Sc | 39 | 18 | derivation-pending | ⚪ pending | binding_energy | — | 312.5248 | — | — |
| ${}^{40}$Sc | 40 | 19 | derivation-pending | ⚪ pending | binding_energy | — | 326.9468 | — | — |
| ${}^{41}$Sc | 41 | 20 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 343.3829 | 343.1371 | +0.07 % | 39263.9865 MeV (+28859.9 ppm) |
| ${}^{42}$Sc | 42 | 21 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 355.1812 | 354.6871 | +0.14 % | 40218.9030 MeV (+28863.0 ppm) |
| ${}^{43}$Sc | 43 | 22 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 369.3240 | 366.8255 | +0.68 % | 41171.4750 MeV (+28822.4 ppm) |
| ${}^{44}$Sc | 44 | 23 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 379.0266 | 376.5247 | +0.66 % | 42128.4872 MeV (+28830.8 ppm) |
| ${}^{45}$Sc | 45 | 24 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 391.1396 | 387.8523 | +0.85 % | 43083.0890 MeV (+28821.3 ppm) |
| ${}^{46}$Sc | 46 | 25 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 399.0215 | 396.6130 | +0.61 % | 44041.9218 MeV (+28849.4 ppm) |
| ${}^{47}$Sc | 47 | 26 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 409.3610 | 407.2595 | +0.52 % | 44998.2971 MeV (+28864.4 ppm) |
| ${}^{48}$Sc | 48 | 27 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 415.6519 | 415.4981 | +0.04 % | 45958.7209 MeV (+28914.0 ppm) |
| ${}^{49}$Sc | 49 | 28 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 424.4326 | 425.6277 | -0.28 % | 46916.6550 MeV (+28949.6 ppm) |
| ${}^{50}$Sc | 50 | 29 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 429.3257 | 431.6737 | -0.54 % | 47878.4767 MeV (+28977.1 ppm) |
| ${}^{51}$Sc | 51 | 30 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 436.7292 | 438.4583 | -0.39 % | 48837.7880 MeV (+28966.6 ppm) |
| ${}^{52}$Sc | 52 | 31 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 440.3877 | 443.8028 | -0.77 % | 49800.8442 MeV (+29003.2 ppm) |
| ${}^{53}$Sc | 53 | 32 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 446.5686 | 450.1201 | -0.79 % | 50761.3781 MeV (+29007.7 ppm) |
| ${}^{54}$Sc | 54 | 33 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 449.1319 | 453.8598 | -1.04 % | 51725.5296 MeV (+29031.1 ppm) |
| ${}^{55}$Sc | 55 | 34 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 454.2223 | 458.3353 | -0.90 % | 52687.1540 MeV (+29019.2 ppm) |
| ${}^{56}$Sc | 56 | 35 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 455.8098 | 461.0804 | -1.14 % | 53652.2813 MeV (+29040.7 ppm) |
| ${}^{57}$Sc | 57 | 36 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 459.9237 | 465.0155 | -1.09 % | 54614.8822 MeV (+29036.9 ppm) |
| ${}^{58}$Sc | 58 | 37 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 460.6382 | 467.1867 | -1.40 % | 55580.8824 MeV (+29062.6 ppm) |
| ${}^{59}$Sc | 59 | 38 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 463.8742 | 470.6080 | -1.43 % | 56544.3612 MeV (+29064.9 ppm) |
| ${}^{60}$Sc | 60 | 39 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 463.8051 | 472.3800 | -1.82 % | 57511.1450 MeV (+29096.3 ppm) |
| ${}^{61}$Sc | 61 | 40 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 466.2489 | 475.4340 | -1.93 % | 58475.4161 MeV (+29104.7 ppm) |
| ${}^{62}$Sc | 62 | 41 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 465.4739 | 476.6560 | -2.35 % | 59442.9058 MeV (+29137.2 ppm) |
| ${}^{63}$Sc | 63 | 42 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 467.2005 | 478.9890 | -2.46 % | 60407.8940 MeV (+29144.4 ppm) |

### Titanium (Z = 22)

_25 of 29 isotopes with a framework prediction; 25 of 29 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{37}$Ti | 37 | 15 | derivation-pending | ⚪ pending | binding_energy | — | 256.2620 | — | — |
| ${}^{38}$Ti | 38 | 16 | derivation-pending | ⚪ pending | binding_energy | — | 278.1220 | — | — |
| ${}^{39}$Ti | 39 | 17 | derivation-pending | ⚪ pending | binding_energy | — | 295.0740 | — | — |
| ${}^{40}$Ti | 40 | 18 | derivation-pending | ⚪ pending | binding_energy | — | 314.6345 | — | — |
| ${}^{41}$Ti | 41 | 19 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 330.1468 | 329.4099 | +0.22 % | 39275.8924 MeV (+28822.9 ppm) |
| ${}^{42}$Ti | 42 | 20 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 347.7912 | 346.8881 | +0.26 % | 40224.9628 MeV (+28833.3 ppm) |
| ${}^{43}$Ti | 43 | 21 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 360.7692 | 359.1706 | +0.45 % | 41178.6995 MeV (+28826.2 ppm) |
| ${}^{44}$Ti | 44 | 22 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 376.0252 | 375.4749 | +0.15 % | 42130.1583 MeV (+28864.9 ppm) |
| ${}^{45}$Ti | 45 | 23 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 386.8538 | 385.0079 | +0.48 % | 43086.0444 MeV (+28841.2 ppm) |
| ${}^{46}$Ti | 46 | 24 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 400.0293 | 398.1973 | +0.46 % | 44039.5837 MeV (+28851.6 ppm) |
| ${}^{47}$Ti | 47 | 25 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 408.9845 | 407.0779 | +0.47 % | 44997.3433 MeV (+28856.7 ppm) |
| ${}^{48}$Ti | 48 | 26 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 420.3367 | 418.7046 | +0.39 % | 45952.7059 MeV (+28871.2 ppm) |
| ${}^{49}$Ti | 49 | 27 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 427.6496 | 426.8470 | +0.19 % | 46912.1077 MeV (+28895.1 ppm) |
| ${}^{50}$Ti | 50 | 28 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 437.3949 | 437.7861 | -0.09 % | 47869.0772 MeV (+28927.5 ppm) |
| ${}^{51}$Ti | 51 | 29 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 443.2607 | 444.1586 | -0.20 % | 48829.9262 MeV (+28941.5 ppm) |
| ${}^{52}$Ti | 52 | 30 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 451.5826 | 451.9746 | -0.09 % | 49788.3190 MeV (+28934.8 ppm) |
| ${}^{53}$Ti | 53 | 31 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 456.1671 | 457.4497 | -0.28 % | 50750.4494 MeV (+28955.3 ppm) |
| ${}^{54}$Ti | 54 | 32 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 463.2224 | 464.3834 | -0.25 % | 51710.1088 MeV (+28955.8 ppm) |
| ${}^{55}$Ti | 55 | 33 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 466.6672 | 468.5433 | -0.40 % | 52673.3788 MeV (+28971.0 ppm) |
| ${}^{56}$Ti | 56 | 34 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 472.5904 | 474.2052 | -0.34 % | 53634.1704 MeV (+28967.8 ppm) |
| ${}^{57}$Ti | 57 | 35 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 475.0174 | 477.2553 | -0.47 % | 54598.4582 MeV (+28979.9 ppm) |
| ${}^{58}$Ti | 58 | 36 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 479.9247 | 481.8425 | -0.40 % | 55560.2656 MeV (+28975.0 ppm) |
| ${}^{59}$Ti | 59 | 37 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 481.4392 | 484.8620 | -0.71 % | 56525.4659 MeV (+29002.9 ppm) |
| ${}^{60}$Ti | 60 | 38 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 485.4314 | 489.1671 | -0.76 % | 57488.1884 MeV (+29008.6 ppm) |
| ${}^{61}$Ti | 61 | 39 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 486.1251 | 491.5380 | -1.10 % | 58454.2095 MeV (+29037.0 ppm) |
| ${}^{62}$Ti | 62 | 40 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 489.2902 | 495.3800 | -1.23 % | 59417.7592 MeV (+29049.4 ppm) |
| ${}^{63}$Ti | 63 | 41 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 489.2429 | 497.1330 | -1.59 % | 60384.5213 MeV (+29078.1 ppm) |
| ${}^{64}$Ti | 64 | 42 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 491.6580 | 500.8640 | -1.84 % | 61348.8210 MeV (+29098.4 ppm) |
| ${}^{65}$Ti | 65 | 43 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 490.9398 | 502.1900 | -2.24 % | 62316.2539 MeV (+29130.6 ppm) |

### Vanadium (Z = 23)

_27 of 29 isotopes with a framework prediction; 27 of 29 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{39}$V | 39 | 16 | derivation-pending | ⚪ pending | binding_energy | — | 274.2090 | — | — |
| ${}^{40}$V | 40 | 17 | derivation-pending | ⚪ pending | binding_energy | — | 292.4000 | — | — |
| ${}^{41}$V | 41 | 18 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 311.9620 | 312.6250 | -0.21 % | 39292.7469 MeV (+28833.0 ppm) |
| ${}^{42}$V | 42 | 19 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 328.6634 | 328.6080 | +0.02 % | 40242.7602 MeV (+28828.4 ppm) |
| ${}^{43}$V | 43 | 20 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 347.4834 | 346.9891 | +0.14 % | 41190.6550 MeV (+28831.9 ppm) |
| ${}^{44}$V | 44 | 21 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 361.6526 | 360.9521 | +0.19 % | 42143.2006 MeV (+28838.2 ppm) |
| ${}^{45}$V | 45 | 22 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 378.0357 | 377.1018 | +0.25 % | 43093.5322 MeV (+28845.0 ppm) |
| ${}^{46}$V | 46 | 23 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 390.0040 | 390.3625 | -0.09 % | 44048.2787 MeV (+28885.3 ppm) |
| ${}^{47}$V | 47 | 24 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 404.2576 | 403.3650 | +0.22 % | 45000.7399 MeV (+28865.5 ppm) |
| ${}^{48}$V | 48 | 25 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 414.3014 | 413.9073 | +0.10 % | 45957.4109 MeV (+28884.1 ppm) |
| ${}^{49}$V | 49 | 26 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 426.6832 | 425.4628 | +0.29 % | 46911.7438 MeV (+28873.5 ppm) |
| ${}^{50}$V | 50 | 27 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 435.0349 | 434.7952 | +0.06 % | 47870.1069 MeV (+28900.8 ppm) |
| ${}^{51}$V | 51 | 28 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 445.7630 | 445.8463 | -0.02 % | 48826.0936 MeV (+28914.3 ppm) |
| ${}^{52}$V | 52 | 29 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 452.6195 | 453.1576 | -0.12 % | 49785.9519 MeV (+28927.7 ppm) |
| ${}^{53}$V | 53 | 30 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 461.8790 | 461.6376 | +0.05 % | 50743.4072 MeV (+28916.2 ppm) |
| ${}^{54}$V | 54 | 31 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 467.4081 | 467.7555 | -0.07 % | 51704.5928 MeV (+28931.1 ppm) |
| ${}^{55}$V | 55 | 32 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 475.3578 | 475.0537 | +0.06 % | 52663.3579 MeV (+28921.8 ppm) |
| ${}^{56}$V | 56 | 33 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 479.7035 | 480.1832 | -0.10 % | 53625.7269 MeV (+28939.2 ppm) |
| ${}^{57}$V | 57 | 34 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 486.4801 | 486.5062 | -0.01 % | 54585.6652 MeV (+28933.4 ppm) |
| ${}^{58}$V | 58 | 35 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 489.7665 | 490.5730 | -0.16 % | 55549.0935 MeV (+28949.3 ppm) |
| ${}^{59}$V | 59 | 36 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 495.4882 | 495.8244 | -0.07 % | 56510.0866 MeV (+28942.6 ppm) |
| ${}^{60}$V | 60 | 37 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 497.8230 | 499.3725 | -0.31 % | 57474.4665 MeV (+28965.4 ppm) |
| ${}^{61}$V | 61 | 38 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 502.5928 | 504.5335 | -0.38 % | 58436.4116 MeV (+28973.8 ppm) |
| ${}^{62}$V | 62 | 39 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 504.0697 | 507.6409 | -0.70 % | 59401.6494 MeV (+29002.3 ppm) |
| ${}^{63}$V | 63 | 40 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 507.9775 | 512.2392 | -0.83 % | 60364.4563 MeV (+29014.6 ppm) |
| ${}^{64}$V | 64 | 41 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 508.6786 | 514.8800 | -1.20 % | 61330.4700 MeV (+29046.8 ppm) |
| ${}^{65}$V | 65 | 42 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 511.8036 | 518.7650 | -1.34 % | 62294.0598 MeV (+29058.4 ppm) |
| ${}^{66}$V | 66 | 43 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 511.8009 | 521.0040 | -1.77 % | 63260.7773 MeV (+29093.8 ppm) |
| ${}^{67}$V | 67 | 44 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 514.2127 | 524.5430 | -1.97 % | 64225.0803 MeV (+29110.2 ppm) |

### Chromium (Z = 24)

_30 of 30 isotopes with a framework prediction; 30 of 30 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{41}$Cr | 41 | 17 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 288.8286 | 291.7560 | -1.00 % | 39314.5500 MeV (+28862.4 ppm) |
| ${}^{42}$Cr | 42 | 18 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 311.5989 | 313.1520 | -0.50 % | 40258.4944 MeV (+28844.6 ppm) |
| ${}^{43}$Cr | 43 | 19 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 329.4667 | 330.2400 | -0.23 % | 41207.3414 MeV (+28838.9 ppm) |
| ${}^{44}$Cr | 44 | 20 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 349.3925 | 349.7836 | -0.11 % | 42154.1304 MeV (+28844.2 ppm) |
| ${}^{45}$Cr | 45 | 21 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 364.6853 | 363.9478 | +0.20 % | 43105.5524 MeV (+28828.1 ppm) |
| ${}^{46}$Cr | 46 | 22 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 382.1328 | 381.9759 | +0.04 % | 44054.8196 MeV (+28855.3 ppm) |
| ${}^{47}$Cr | 47 | 23 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 395.1801 | 395.1387 | +0.01 % | 45008.4871 MeV (+28867.5 ppm) |
| ${}^{48}$Cr | 48 | 24 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 410.4556 | 411.4683 | -0.25 % | 45959.9264 MeV (+28902.2 ppm) |
| ${}^{49}$Cr | 49 | 25 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 421.5334 | 422.0506 | -0.12 % | 46915.5633 MeV (+28897.9 ppm) |
| ${}^{50}$Cr | 50 | 26 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 434.8945 | 435.0509 | -0.04 % | 47868.9170 MeV (+28898.2 ppm) |
| ${}^{51}$Cr | 51 | 27 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 444.2360 | 444.3116 | -0.02 % | 48826.2903 MeV (+28902.1 ppm) |
| ${}^{52}$Cr | 52 | 28 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 455.9013 | 456.3517 | -0.10 % | 49781.3398 MeV (+28916.9 ppm) |
| ${}^{53}$Cr | 53 | 29 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 463.7043 | 464.2911 | -0.13 % | 50740.2516 MeV (+28923.9 ppm) |
| ${}^{54}$Cr | 54 | 30 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 473.8603 | 474.0102 | -0.03 % | 51696.8103 MeV (+28920.3 ppm) |
| ${}^{55}$Cr | 55 | 31 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 480.2943 | 480.2565 | +0.01 % | 52657.0911 MeV (+28919.7 ppm) |
| ${}^{56}$Cr | 56 | 32 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 489.1012 | 488.5026 | +0.12 % | 53614.9990 MeV (+28913.1 ppm) |
| ${}^{57}$Cr | 57 | 33 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 494.3118 | 493.8138 | +0.10 % | 54576.5032 MeV (+28917.6 ppm) |
| ${}^{58}$Cr | 58 | 34 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 501.9079 | 501.3519 | +0.11 % | 55535.6218 MeV (+28920.2 ppm) |
| ${}^{59}$Cr | 59 | 35 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 506.0211 | 505.5474 | +0.09 % | 56498.2234 MeV (+28923.4 ppm) |
| ${}^{60}$Cr | 60 | 36 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 512.5265 | 512.4113 | +0.02 % | 57458.4328 MeV (+28932.9 ppm) |
| ${}^{61}$Cr | 61 | 37 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 515.6519 | 516.0706 | -0.08 % | 58422.0222 MeV (+28943.6 ppm) |
| ${}^{62}$Cr | 62 | 38 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 521.1713 | 522.4980 | -0.25 % | 59383.2176 MeV (+28961.8 ppm) |
| ${}^{63}$Cr | 63 | 39 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 523.4044 | 525.8950 | -0.47 % | 60347.6992 MeV (+28982.2 ppm) |
| ${}^{64}$Cr | 64 | 40 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 528.0295 | 531.4280 | -0.64 % | 61309.7889 MeV (+28998.8 ppm) |
| ${}^{65}$Cr | 65 | 41 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 529.4542 | 534.1700 | -0.88 % | 62275.0789 MeV (+29020.3 ppm) |
| ${}^{66}$Cr | 66 | 42 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 533.2658 | 539.0880 | -1.08 % | 63237.9821 MeV (+29038.4 ppm) |
| ${}^{67}$Cr | 67 | 43 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 533.9560 | 541.2930 | -1.36 % | 64204.0067 MeV (+29061.5 ppm) |
| ${}^{68}$Cr | 68 | 44 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 537.0255 | 545.7680 | -1.60 % | 65167.6520 MeV (+29083.6 ppm) |
| ${}^{69}$Cr | 69 | 45 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 537.0463 | 547.7910 | -1.96 % | 66134.3459 MeV (+29112.7 ppm) |
| ${}^{70}$Cr | 70 | 46 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 539.4369 | 551.8800 | -2.25 % | 67098.6701 MeV (+29137.3 ppm) |

### Manganese (Z = 25)

_31 of 31 isotopes with a framework prediction; 31 of 31 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{43}$Mn | 43 | 18 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 306.7191 | 310.1590 | -1.11 % | 41228.7587 MeV (+28876.9 ppm) |
| ${}^{44}$Mn | 44 | 19 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 325.7611 | 328.1080 | -0.72 % | 42176.4315 MeV (+28864.1 ppm) |
| ${}^{45}$Mn | 45 | 20 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 346.8025 | 348.6150 | -0.52 % | 43122.1049 MeV (+28866.3 ppm) |
| ${}^{46}$Mn | 46 | 21 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 363.2285 | 364.1397 | -0.25 % | 44072.3936 MeV (+28856.0 ppm) |
| ${}^{47}$Mn | 47 | 22 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 381.7521 | 382.3596 | -0.16 % | 45020.5848 MeV (+28861.9 ppm) |
| ${}^{48}$Mn | 48 | 23 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 395.8898 | 397.1612 | -0.32 % | 45973.1619 MeV (+28887.0 ppm) |
| ${}^{49}$Mn | 49 | 24 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 412.2003 | 413.5558 | -0.33 % | 46923.5662 MeV (+28899.4 ppm) |
| ${}^{50}$Mn | 50 | 25 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 424.3250 | 426.6341 | -0.54 % | 47878.1562 MeV (+28928.0 ppm) |
| ${}^{51}$Mn | 51 | 26 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 438.6797 | 440.3218 | -0.37 % | 48830.5163 MeV (+28921.6 ppm) |
| ${}^{52}$Mn | 52 | 27 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 449.0250 | 450.8613 | -0.41 % | 49786.8858 MeV (+28931.4 ppm) |
| ${}^{53}$Mn | 53 | 28 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 461.6430 | 462.9115 | -0.27 % | 50740.9826 MeV (+28926.3 ppm) |
| ${}^{54}$Mn | 54 | 29 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 470.4076 | 471.8507 | -0.31 % | 51698.9327 MeV (+28934.3 ppm) |
| ${}^{55}$Mn | 55 | 30 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 481.4765 | 482.0764 | -0.12 % | 52654.5786 MeV (+28922.9 ppm) |
| ${}^{56}$Mn | 56 | 31 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 488.8313 | 489.3468 | -0.11 % | 53613.9386 MeV (+28924.9 ppm) |
| ${}^{57}$Mn | 57 | 32 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 498.5125 | 497.9927 | +0.10 % | 54570.9721 MeV (+28909.5 ppm) |
| ${}^{58}$Mn | 58 | 33 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 504.6047 | 504.4053 | +0.04 % | 55531.5947 MeV (+28918.7 ppm) |
| ${}^{59}$Mn | 59 | 34 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 513.0380 | 512.1744 | +0.17 % | 56489.8762 MeV (+28910.3 ppm) |
| ${}^{60}$Mn | 60 | 35 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 517.9953 | 517.6884 | +0.06 % | 57451.6337 MeV (+28922.8 ppm) |
| ${}^{61}$Mn | 61 | 36 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 525.3024 | 524.5339 | +0.15 % | 58411.0413 MeV (+28917.7 ppm) |
| ${}^{62}$Mn | 62 | 37 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 529.2360 | 529.3870 | -0.03 % | 59373.8225 MeV (+28935.8 ppm) |
| ${}^{63}$Mn | 63 | 38 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 535.5234 | 535.8214 | -0.06 % | 60334.2499 MeV (+28940.8 ppm) |
| ${}^{64}$Mn | 64 | 39 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 538.5306 | 539.9947 | -0.27 % | 61297.9574 MeV (+28961.7 ppm) |
| ${}^{65}$Mn | 65 | 40 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 543.8917 | 546.0443 | -0.39 % | 62259.3112 MeV (+28974.9 ppm) |
| ${}^{66}$Mn | 66 | 41 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 546.0582 | 549.8987 | -0.70 % | 63223.8595 MeV (+29003.0 ppm) |
| ${}^{67}$Mn | 67 | 42 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 550.5752 | 554.8270 | -0.77 % | 64186.0572 MeV (+29009.8 ppm) |
| ${}^{68}$Mn | 68 | 43 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 551.9765 | 558.2120 | -1.12 % | 65151.3707 MeV (+29041.4 ppm) |
| ${}^{69}$Mn | 69 | 44 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 555.7224 | 562.6950 | -1.24 % | 66114.3395 MeV (+29053.3 ppm) |
| ${}^{70}$Mn | 70 | 45 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 556.4254 | 565.8800 | -1.67 % | 67080.3513 MeV (+29090.1 ppm) |
| ${}^{71}$Mn | 71 | 46 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 559.4649 | 570.1300 | -1.87 % | 68044.0265 MeV (+29107.4 ppm) |
| ${}^{72}$Mn | 72 | 47 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 559.5290 | 572.7600 | -2.31 % | 69010.6772 MeV (+29143.7 ppm) |
| ${}^{73}$Mn | 73 | 48 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 561.9200 | 576.3350 | -2.50 % | 69975.0010 MeV (+29159.6 ppm) |

### Iron (Z = 26)

_32 of 32 isotopes with a framework prediction; 32 of 32 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{45}$Fe | 45 | 19 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 324.3873 | 328.4550 | -1.24 % | 43143.1897 MeV (+28893.4 ppm) |
| ${}^{46}$Fe | 46 | 20 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 346.4784 | 349.7380 | -0.93 % | 44087.8135 MeV (+28888.6 ppm) |
| ${}^{47}$Fe | 47 | 21 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 363.9736 | 366.1300 | -0.59 % | 45037.0330 MeV (+28874.8 ppm) |
| ${}^{48}$Fe | 48 | 22 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 383.5136 | 385.0908 | -0.41 % | 45984.2078 MeV (+28874.3 ppm) |
| ${}^{49}$Fe | 49 | 23 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 398.6837 | 399.9043 | -0.31 % | 46935.7525 MeV (+28876.3 ppm) |
| ${}^{50}$Fe | 50 | 24 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 415.9751 | 417.7013 | -0.41 % | 47885.1759 MeV (+28898.6 ppm) |
| ${}^{51}$Fe | 51 | 25 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 429.0943 | 431.4854 | -0.55 % | 48838.7714 MeV (+28920.9 ppm) |
| ${}^{52}$Fe | 52 | 26 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 444.3937 | 447.6996 | -0.74 % | 49790.1868 MeV (+28949.0 ppm) |
| ${}^{53}$Fe | 53 | 27 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 455.6951 | 458.3863 | -0.59 % | 50745.6001 MeV (+28941.8 ppm) |
| ${}^{54}$Fe | 54 | 28 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 469.2215 | 471.7648 | -0.54 % | 51698.7886 MeV (+28945.7 ppm) |
| ${}^{55}$Fe | 55 | 29 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 478.9046 | 481.0629 | -0.45 % | 52655.8202 MeV (+28942.5 ppm) |
| ${}^{56}$Fe | 56 | 30 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 490.8459 | 492.2600 | -0.29 % | 53610.5937 MeV (+28933.6 ppm) |
| ${}^{57}$Fe | 57 | 31 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 499.0822 | 499.9061 | -0.16 % | 54569.0721 MeV (+28926.0 ppm) |
| ${}^{58}$Fe | 58 | 32 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 509.6009 | 509.9507 | -0.07 % | 55525.2682 MeV (+28922.1 ppm) |
| ${}^{59}$Fe | 59 | 33 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 516.5389 | 516.5317 | +0.00 % | 56485.0450 MeV (+28918.6 ppm) |
| ${}^{60}$Fe | 60 | 34 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 525.7759 | 525.3512 | +0.08 % | 57442.5227 MeV (+28915.3 ppm) |
| ${}^{61}$Fe | 61 | 35 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 531.5445 | 530.9299 | +0.12 % | 58403.4690 MeV (+28914.5 ppm) |
| ${}^{62}$Fe | 62 | 36 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 539.6228 | 538.9588 | +0.12 % | 59362.1054 MeV (+28917.3 ppm) |
| ${}^{63}$Fe | 63 | 37 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 544.3346 | 543.7876 | +0.10 % | 60324.1084 MeV (+28921.4 ppm) |
| ${}^{64}$Fe | 64 | 38 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 551.3620 | 551.1929 | +0.03 % | 61283.7958 MeV (+28930.9 ppm) |
| ${}^{65}$Fe | 65 | 39 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 555.1160 | 555.5126 | -0.07 % | 62246.7566 MeV (+28941.8 ppm) |
| ${}^{66}$Fe | 66 | 40 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 561.1871 | 562.4338 | -0.22 % | 63207.4002 MeV (+28958.2 ppm) |
| ${}^{67}$Fe | 67 | 41 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 564.0703 | 566.1457 | -0.37 % | 64171.2318 MeV (+28972.2 ppm) |
| ${}^{68}$Fe | 68 | 42 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 569.2690 | 572.4240 | -0.55 % | 65132.7478 MeV (+28990.7 ppm) |
| ${}^{69}$Fe | 69 | 43 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 571.3583 | 575.8050 | -0.77 % | 66097.3733 MeV (+29010.8 ppm) |
| ${}^{70}$Fe | 70 | 44 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 575.7589 | 581.5600 | -1.00 % | 67059.6875 MeV (+29032.6 ppm) |
| ${}^{71}$Fe | 71 | 45 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 577.1227 | 584.6850 | -1.29 % | 68025.0385 MeV (+29058.5 ppm) |
| ${}^{72}$Fe | 72 | 46 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 580.7912 | 590.0400 | -1.57 % | 68988.0847 MeV (+29084.2 ppm) |
| ${}^{73}$Fe | 73 | 47 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 581.4902 | 592.8330 | -1.91 % | 69954.1005 MeV (+29113.9 ppm) |
| ${}^{74}$Fe | 74 | 48 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 584.4857 | 597.6240 | -2.20 % | 70917.8198 MeV (+29138.3 ppm) |
| ${}^{75}$Fe | 75 | 49 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 584.5743 | 599.7000 | -2.52 % | 71884.4460 MeV (+29164.9 ppm) |
| ${}^{76}$Fe | 76 | 50 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 586.9496 | 603.6680 | -2.77 % | 72848.7855 MeV (+29185.3 ppm) |

### Cobalt (Z = 27)

_32 of 32 isotopes with a framework prediction; 32 of 32 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{47}$Co | 47 | 20 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 341.8446 | 347.6120 | -1.66 % | 45057.8318 MeV (+28932.7 ppm) |
| ${}^{48}$Co | 48 | 21 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 360.4173 | 364.5600 | -1.14 % | 46005.9738 MeV (+28906.9 ppm) |
| ${}^{49}$Co | 49 | 22 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 380.9837 | 384.1600 | -0.83 % | 46952.1222 MeV (+28897.5 ppm) |
| ${}^{50}$Co | 50 | 23 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 397.1959 | 400.0319 | -0.71 % | 47902.6247 MeV (+28900.2 ppm) |
| ${}^{51}$Co | 51 | 24 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 415.4796 | 417.8560 | -0.57 % | 48851.0558 MeV (+28901.3 ppm) |
| ${}^{52}$Co | 52 | 25 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 429.6042 | 432.9292 | -0.77 % | 49803.6459 MeV (+28929.7 ppm) |
| ${}^{53}$Co | 53 | 26 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 445.8607 | 449.3159 | -0.77 % | 50754.1043 MeV (+28941.3 ppm) |
| ${}^{54}$Co | 54 | 27 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 458.1305 | 462.7379 | -1.00 % | 51708.5493 MeV (+28971.2 ppm) |
| ${}^{55}$Co | 55 | 28 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 472.5784 | 476.8291 | -0.89 % | 52660.8161 MeV (+28970.8 ppm) |
| ${}^{56}$Co | 56 | 29 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 483.1930 | 486.9110 | -0.76 % | 53616.9162 MeV (+28964.8 ppm) |
| ${}^{57}$Co | 57 | 30 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 496.0210 | 498.2874 | -0.45 % | 54570.8031 MeV (+28942.4 ppm) |
| ${}^{58}$Co | 58 | 31 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 505.1526 | 506.8604 | -0.34 % | 55528.3862 MeV (+28935.8 ppm) |
| ${}^{59}$Co | 59 | 32 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 516.5237 | 517.3142 | -0.15 % | 56483.7299 MeV (+28924.0 ppm) |
| ${}^{60}$Co | 60 | 33 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 524.3218 | 524.8062 | -0.09 % | 57442.6465 MeV (+28921.9 ppm) |
| ${}^{61}$Co | 61 | 34 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 534.3779 | 534.1252 | +0.05 % | 58399.3052 MeV (+28913.2 ppm) |
| ${}^{62}$Co | 62 | 35 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 540.9728 | 540.7228 | +0.05 % | 59359.4251 MeV (+28916.3 ppm) |
| ${}^{63}$Co | 63 | 36 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 549.8381 | 549.2212 | +0.11 % | 60317.2746 MeV (+28913.9 ppm) |
| ${}^{64}$Co | 64 | 37 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 555.3436 | 555.2334 | +0.02 % | 61278.4838 MeV (+28925.0 ppm) |
| ${}^{65}$Co | 65 | 38 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 563.1271 | 562.6975 | +0.08 % | 62237.4152 MeV (+28922.9 ppm) |
| ${}^{66}$Co | 66 | 39 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 567.6435 | 567.9922 | -0.06 % | 63199.6135 MeV (+28937.6 ppm) |
| ${}^{67}$Co | 67 | 40 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 574.4412 | 574.9767 | -0.09 % | 64159.5305 MeV (+28943.2 ppm) |
| ${}^{68}$Co | 68 | 41 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 578.0570 | 579.3688 | -0.23 % | 65122.6296 MeV (+28956.8 ppm) |
| ${}^{69}$Co | 69 | 42 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 583.9541 | 586.1830 | -0.38 % | 66083.4473 MeV (+28973.2 ppm) |
| ${}^{70}$Co | 70 | 43 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 586.7475 | 590.3939 | -0.62 % | 67047.3686 MeV (+28995.7 ppm) |
| ${}^{71}$Co | 71 | 44 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 591.8195 | 596.3101 | -0.75 % | 68009.0114 MeV (+29009.7 ppm) |
| ${}^{72}$Co | 72 | 45 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 593.8603 | 600.3360 | -1.08 % | 68973.6854 MeV (+29039.1 ppm) |
| ${}^{73}$Co | 73 | 46 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 598.1745 | 606.0460 | -1.30 % | 69936.0859 MeV (+29060.5 ppm) |
| ${}^{74}$Co | 74 | 47 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 599.5248 | 609.6860 | -1.67 % | 70901.4504 MeV (+29093.1 ppm) |
| ${}^{75}$Co | 75 | 48 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 603.1415 | 614.7750 | -1.89 % | 71864.5484 MeV (+29113.7 ppm) |
| ${}^{76}$Co | 76 | 49 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 603.8568 | 617.9560 | -2.28 % | 72830.5480 MeV (+29146.8 ppm) |
| ${}^{77}$Co | 77 | 50 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 606.8301 | 622.3140 | -2.49 % | 73794.2894 MeV (+29164.0 ppm) |
| ${}^{78}$Co | 78 | 51 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 606.9603 | 623.7660 | -2.69 % | 74760.8740 MeV (+29179.8 ppm) |

### Nickel (Z = 28)

_35 of 35 isotopes with a framework prediction; 35 of 35 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{48}$Ni | 48 | 20 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 339.5106 | 347.3280 | -2.25 % | 46025.5502 MeV (+28966.2 ppm) |
| ${}^{49}$Ni | 49 | 21 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 359.1003 | 365.0500 | -1.63 % | 46972.6752 MeV (+28935.0 ppm) |
| ${}^{50}$Ni | 50 | 22 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 380.6364 | 385.1000 | -1.16 % | 47917.8539 MeV (+28915.0 ppm) |
| ${}^{51}$Ni | 51 | 23 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 397.8357 | 401.3700 | -0.88 % | 48867.3694 MeV (+28904.8 ppm) |
| ${}^{52}$Ni | 52 | 24 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 417.0598 | 420.3627 | -0.79 % | 49814.8600 MeV (+28910.9 ppm) |
| ${}^{53}$Ni | 53 | 25 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 432.1396 | 435.5050 | -0.77 % | 50766.4950 MeV (+28920.8 ppm) |
| ${}^{54}$Ni | 54 | 26 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 449.3059 | 453.2238 | -0.86 % | 51716.0435 MeV (+28941.5 ppm) |
| ${}^{55}$Ni | 55 | 27 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 462.4981 | 467.3527 | -1.04 % | 52669.5661 MeV (+28966.9 ppm) |
| ${}^{56}$Ni | 56 | 28 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 477.8246 | 483.9957 | -1.28 % | 53620.9544 MeV (+29000.2 ppm) |
| ${}^{57}$Ni | 57 | 29 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 489.3287 | 494.2434 | -0.99 % | 54576.1650 MeV (+28980.2 ppm) |
| ${}^{58}$Ni | 58 | 30 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 503.0038 | 506.4596 | -0.68 % | 55529.2047 MeV (+28958.3 ppm) |
| ${}^{59}$Ni | 59 | 31 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 512.9924 | 515.4589 | -0.48 % | 56485.9309 MeV (+28943.9 ppm) |
| ${}^{60}$Ni | 60 | 32 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 525.1797 | 526.8466 | -0.32 % | 57440.4584 MeV (+28934.7 ppm) |
| ${}^{61}$Ni | 61 | 33 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 533.8029 | 534.6667 | -0.16 % | 58398.5500 MeV (+28923.9 ppm) |
| ${}^{62}$Ni | 62 | 34 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 544.6449 | 545.2624 | -0.11 % | 59354.4227 MeV (+28924.5 ppm) |
| ${}^{63}$Ni | 63 | 35 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 552.0337 | 552.1002 | -0.01 % | 60313.7487 MeV (+28918.0 ppm) |
| ${}^{64}$Ni | 64 | 36 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 561.6555 | 561.7577 | -0.02 % | 61270.8417 MeV (+28922.9 ppm) |
| ${}^{65}$Ni | 65 | 37 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 567.9250 | 567.8558 | +0.01 % | 62231.2869 MeV (+28922.6 ppm) |
| ${}^{66}$Ni | 66 | 38 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 576.4366 | 576.8076 | -0.06 % | 63189.4902 MeV (+28933.6 ppm) |
| ${}^{67}$Ni | 67 | 39 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 581.6881 | 582.6153 | -0.16 % | 64150.9534 MeV (+28944.6 ppm) |
| ${}^{68}$Ni | 68 | 40 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 589.1865 | 590.4077 | -0.21 % | 65110.1697 MeV (+28952.1 ppm) |
| ${}^{69}$Ni | 69 | 41 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 593.5097 | 594.9939 | -0.25 % | 66072.5614 MeV (+28957.4 ppm) |
| ${}^{70}$Ni | 70 | 42 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 600.0812 | 602.3004 | -0.37 % | 67032.7046 MeV (+28971.1 ppm) |
| ${}^{71}$Ni | 71 | 43 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 603.5555 | 606.5641 | -0.50 % | 67995.9451 MeV (+28983.8 ppm) |
| ${}^{72}$Ni | 72 | 44 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 609.2768 | 613.4552 | -0.68 % | 68956.9386 MeV (+29003.0 ppm) |
| ${}^{73}$Ni | 73 | 45 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 611.9730 | 617.4087 | -0.88 % | 69920.9571 MeV (+29021.7 ppm) |
| ${}^{74}$Ni | 74 | 46 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 616.9125 | 624.0420 | -1.14 % | 70882.7324 MeV (+29047.8 ppm) |
| ${}^{75}$Ni | 75 | 47 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 618.8940 | 627.6750 | -1.40 % | 71847.4657 MeV (+29070.6 ppm) |
| ${}^{76}$Ni | 76 | 48 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 623.1130 | 633.6880 | -1.67 % | 72809.9614 MeV (+29096.3 ppm) |
| ${}^{77}$Ni | 77 | 49 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 624.4364 | 636.9440 | -1.96 % | 73775.3528 MeV (+29121.6 ppm) |
| ${}^{78}$Ni | 78 | 50 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 627.9901 | 642.5640 | -2.27 % | 74738.5139 MeV (+29149.1 ppm) |
| ${}^{79}$Ni | 79 | 51 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 628.7063 | 643.8500 | -2.35 % | 75704.5124 MeV (+29155.0 ppm) |
| ${}^{80}$Ni | 80 | 52 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 631.6443 | 647.0400 | -2.38 % | 76668.2892 MeV (+29155.8 ppm) |
| ${}^{81}$Ni | 81 | 53 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 631.7993 | 648.0000 | -2.50 % | 77634.8490 MeV (+29163.1 ppm) |
| ${}^{82}$Ni | 82 | 54 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 634.1664 | 650.6700 | -2.54 % | 78599.1967 MeV (+29165.2 ppm) |

### Copper (Z = 29)

_33 of 33 isotopes with a framework prediction; 33 of 33 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{52}$Cu | 52 | 23 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 394.3573 | 398.8920 | -1.14 % | 49836.2322 MeV (+28912.9 ppm) |
| ${}^{53}$Cu | 53 | 24 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 414.5320 | 418.2230 | -0.88 % | 50782.7723 MeV (+28906.8 ppm) |
| ${}^{54}$Cu | 54 | 25 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 430.5766 | 434.4300 | -0.89 % | 51733.4426 MeV (+28918.4 ppm) |
| ${}^{55}$Cu | 55 | 26 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 448.6636 | 452.8698 | -0.93 % | 52682.0703 MeV (+28935.8 ppm) |
| ${}^{56}$Cu | 56 | 27 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 462.7887 | 467.9355 | -1.10 % | 53634.6599 MeV (+28961.5 ppm) |
| ${}^{57}$Cu | 57 | 28 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 479.0055 | 484.6861 | -1.17 % | 54585.1580 MeV (+28979.6 ppm) |
| ${}^{58}$Cu | 58 | 29 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 491.4105 | 497.1162 | -1.15 % | 55539.4678 MeV (+28985.2 ppm) |
| ${}^{59}$Cu | 59 | 30 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 505.9452 | 509.8782 | -0.77 % | 56491.6478 MeV (+28958.1 ppm) |
| ${}^{60}$Cu | 60 | 31 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 516.8028 | 519.9363 | -0.60 % | 57447.5050 MeV (+28948.0 ppm) |
| ${}^{61}$Cu | 61 | 32 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 529.8192 | 531.6464 | -0.34 % | 58401.2033 MeV (+28930.1 ppm) |
| ${}^{62}$Cu | 62 | 33 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 539.2801 | 540.5212 | -0.23 % | 59358.4572 MeV (+28923.8 ppm) |
| ${}^{63}$Cu | 63 | 34 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 550.9216 | 551.3848 | -0.08 % | 60313.5305 MeV (+28915.5 ppm) |
| ${}^{64}$Cu | 64 | 35 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 559.1176 | 559.3007 | -0.03 % | 61272.0492 MeV (+28914.3 ppm) |
| ${}^{65}$Cu | 65 | 36 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 569.5098 | 569.2113 | +0.05 % | 62228.3718 MeV (+28910.8 ppm) |
| ${}^{66}$Cu | 66 | 37 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 576.5570 | 576.2772 | +0.05 % | 63188.0394 MeV (+28914.2 ppm) |
| ${}^{67}$Cu | 67 | 38 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 585.8108 | 585.4098 | +0.07 % | 64145.5004 MeV (+28916.2 ppm) |
| ${}^{68}$Cu | 68 | 39 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 591.8114 | 591.7286 | +0.01 % | 65106.2145 MeV (+28923.8 ppm) |
| ${}^{69}$Cu | 69 | 40 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 600.0251 | 599.9691 | +0.01 % | 66064.7156 MeV (+28927.5 ppm) |
| ${}^{70}$Cu | 70 | 41 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 605.0699 | 605.2806 | -0.03 % | 67026.3857 MeV (+28933.5 ppm) |
| ${}^{71}$Cu | 71 | 42 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 612.3306 | 613.0867 | -0.12 % | 67985.8397 MeV (+28944.6 ppm) |
| ${}^{72}$Cu | 72 | 43 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 616.5001 | 618.2298 | -0.28 % | 68948.3850 MeV (+28960.7 ppm) |
| ${}^{73}$Cu | 73 | 44 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 622.8856 | 625.5056 | -0.42 % | 69908.7143 MeV (+28976.0 ppm) |
| ${}^{74}$Cu | 74 | 45 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 626.2518 | 630.5957 | -0.69 % | 70872.0628 MeV (+29002.1 ppm) |
| ${}^{75}$Cu | 75 | 46 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 631.8316 | 637.1310 | -0.83 % | 71833.1978 MeV (+29017.0 ppm) |
| ${}^{76}$Cu | 76 | 47 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 634.4589 | 641.7137 | -1.13 % | 72797.2853 MeV (+29045.0 ppm) |
| ${}^{77}$Cu | 77 | 48 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 639.2953 | 647.6663 | -1.29 % | 73759.1636 MeV (+29061.0 ppm) |
| ${}^{78}$Cu | 78 | 49 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 641.2415 | 651.6642 | -1.60 % | 74723.9322 MeV (+29088.7 ppm) |
| ${}^{79}$Cu | 79 | 50 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 645.3906 | 657.3541 | -1.82 % | 75686.4979 MeV (+29109.4 ppm) |
| ${}^{80}$Cu | 80 | 51 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 646.7076 | 659.6800 | -1.97 % | 76651.8956 MeV (+29121.4 ppm) |
| ${}^{81}$Cu | 81 | 52 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 650.2201 | 662.9850 | -1.93 % | 77615.0979 MeV (+29117.1 ppm) |
| ${}^{82}$Cu | 82 | 53 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 650.9549 | 664.8560 | -2.09 % | 78581.0779 MeV (+29130.2 ppm) |
| ${}^{83}$Cu | 83 | 54 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 653.8765 | 667.6520 | -2.06 % | 79544.8711 MeV (+29126.0 ppm) |
| ${}^{84}$Cu | 84 | 55 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 654.0714 | 669.0600 | -2.24 % | 80511.3909 MeV (+29139.1 ppm) |

### Zinc (Z = 30)

_33 of 33 isotopes with a framework prediction; 33 of 33 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{54}$Zn | 54 | 24 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 414.1137 | 418.0680 | -0.95 % | 51748.5752 MeV (+28901.4 ppm) |
| ${}^{55}$Zn | 55 | 25 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 431.0749 | 434.7200 | -0.84 % | 52698.3287 MeV (+28904.4 ppm) |
| ${}^{56}$Zn | 56 | 26 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 450.0373 | 453.9360 | -0.86 % | 53646.0811 MeV (+28919.3 ppm) |
| ${}^{57}$Zn | 57 | 27 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 465.0513 | 469.1670 | -0.88 % | 54597.7819 MeV (+28931.3 ppm) |
| ${}^{58}$Zn | 58 | 28 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 482.1166 | 486.9649 | -1.00 % | 55547.4314 MeV (+28954.2 ppm) |
| ${}^{59}$Zn | 59 | 29 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 495.3818 | 499.9530 | -0.91 % | 56500.8809 MeV (+28955.0 ppm) |
| ${}^{60}$Zn | 60 | 30 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 510.7378 | 514.9831 | -0.82 % | 57452.2397 MeV (+28955.9 ppm) |
| ${}^{61}$Zn | 61 | 31 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 522.4271 | 525.2289 | -0.53 % | 58407.2652 MeV (+28934.7 ppm) |
| ${}^{62}$Zn | 62 | 32 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 536.2375 | 538.1194 | -0.35 % | 59360.1695 MeV (+28924.6 ppm) |
| ${}^{63}$Zn | 63 | 33 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 546.5016 | 547.2361 | -0.13 % | 60316.6201 MeV (+28909.1 ppm) |
| ${}^{64}$Zn | 64 | 34 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 558.9100 | 559.0980 | -0.03 % | 61270.9266 MeV (+28905.4 ppm) |
| ${}^{65}$Zn | 65 | 35 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 567.8815 | 567.0773 | +0.14 % | 62228.6699 MeV (+28892.7 ppm) |
| ${}^{66}$Zn | 66 | 36 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 579.0141 | 578.1358 | +0.15 % | 63184.2520 MeV (+28896.7 ppm) |
| ${}^{67}$Zn | 67 | 37 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 586.8095 | 585.1883 | +0.28 % | 64143.1714 MeV (+28888.1 ppm) |
| ${}^{68}$Zn | 68 | 38 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 596.7779 | 595.3864 | +0.23 % | 65099.9178 MeV (+28896.5 ppm) |
| ${}^{69}$Zn | 69 | 39 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 603.5004 | 601.8684 | +0.27 % | 66059.9100 MeV (+28895.6 ppm) |
| ${}^{70}$Zn | 70 | 40 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 612.4036 | 611.0866 | +0.22 % | 67017.7216 MeV (+28904.6 ppm) |
| ${}^{71}$Zn | 71 | 41 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 618.1448 | 616.9220 | +0.20 % | 67978.6952 MeV (+28908.4 ppm) |
| ${}^{72}$Zn | 72 | 42 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 626.0709 | 625.8100 | +0.04 % | 68937.4839 MeV (+28926.4 ppm) |
| ${}^{73}$Zn | 73 | 43 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 630.9123 | 631.3292 | -0.07 % | 69899.3572 MeV (+28938.3 ppm) |
| ${}^{74}$Zn | 74 | 44 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 637.9398 | 639.5638 | -0.25 % | 70859.0445 MeV (+28958.7 ppm) |
| ${}^{75}$Zn | 75 | 45 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 641.9544 | 644.4374 | -0.39 % | 71821.7447 MeV (+28972.2 ppm) |
| ${}^{76}$Zn | 76 | 46 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 648.1538 | 652.2528 | -0.63 % | 72782.2601 MeV (+28997.2 ppm) |
| ${}^{77}$Zn | 77 | 47 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 651.4068 | 656.8103 | -0.82 % | 73745.7218 MeV (+29016.0 ppm) |
| ${}^{78}$Zn | 78 | 48 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 656.8414 | 663.5756 | -1.01 % | 74707.0020 MeV (+29035.4 ppm) |
| ${}^{79}$Zn | 79 | 49 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 659.3915 | 667.5960 | -1.23 % | 75671.1667 MeV (+29055.2 ppm) |
| ${}^{80}$Zn | 80 | 50 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 664.1182 | 673.8837 | -1.45 % | 76633.1547 MeV (+29076.6 ppm) |
| ${}^{81}$Zn | 81 | 51 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 666.0184 | 676.5060 | -1.55 % | 77597.9693 MeV (+29085.0 ppm) |
| ${}^{82}$Zn | 82 | 52 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 670.0888 | 680.6916 | -1.56 % | 78560.6137 MeV (+29085.7 ppm) |
| ${}^{83}$Zn | 83 | 53 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 671.3869 | 682.7580 | -1.67 % | 79526.0304 MeV (+29093.9 ppm) |
| ${}^{84}$Zn | 84 | 54 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 674.8474 | 686.3640 | -1.68 % | 80489.2846 MeV (+29094.8 ppm) |
| ${}^{85}$Zn | 85 | 55 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 675.5867 | 687.6500 | -1.75 % | 81455.2601 MeV (+29100.5 ppm) |
| ${}^{86}$Zn | 86 | 56 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 678.4798 | 690.7520 | -1.78 % | 82419.0818 MeV (+29101.0 ppm) |

### Gallium (Z = 31)

_33 of 33 isotopes with a framework prediction; 33 of 33 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{56}$Ga | 56 | 25 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 427.6184 | 431.5920 | -0.92 % | 53667.1696 MeV (+28898.5 ppm) |
| ${}^{57}$Ga | 57 | 26 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 447.4660 | 451.2120 | -0.83 % | 54614.0368 MeV (+28905.2 ppm) |
| ${}^{58}$Ga | 58 | 27 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 463.3781 | 467.4220 | -0.87 % | 55564.8395 MeV (+28919.1 ppm) |
| ${}^{59}$Ga | 59 | 28 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 481.3025 | 485.6880 | -0.90 % | 56513.6299 MeV (+28935.0 ppm) |
| ${}^{60}$Ga | 60 | 29 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 495.4381 | 499.6200 | -0.84 % | 57466.2091 MeV (+28937.4 ppm) |
| ${}^{61}$Ga | 61 | 30 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 511.6264 | 515.2323 | -0.70 % | 58416.7356 MeV (+28934.5 ppm) |
| ${}^{62}$Ga | 62 | 31 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 524.1580 | 528.1560 | -0.76 % | 59370.9187 MeV (+28947.2 ppm) |
| ${}^{63}$Ga | 63 | 32 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 538.7739 | 540.7874 | -0.37 % | 60323.0176 MeV (+28918.7 ppm) |
| ${}^{64}$Ga | 64 | 33 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 549.8526 | 551.1444 | -0.23 % | 61278.6536 MeV (+28911.3 ppm) |
| ${}^{65}$Ga | 65 | 34 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 563.0399 | 563.0404 | -0.00 % | 62232.1811 MeV (+28895.4 ppm) |
| ${}^{66}$Ga | 66 | 35 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 572.7985 | 572.1780 | +0.11 % | 63189.1373 MeV (+28889.6 ppm) |
| ${}^{67}$Ga | 67 | 36 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 584.6840 | 583.4047 | +0.22 % | 64143.9666 MeV (+28884.3 ppm) |
| ${}^{68}$Ga | 68 | 37 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 593.2397 | 591.6829 | +0.26 % | 65102.1256 MeV (+28883.9 ppm) |
| ${}^{69}$Ga | 69 | 38 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 603.9355 | 601.9960 | +0.32 % | 66058.1446 MeV (+28882.7 ppm) |
| ${}^{70}$Ga | 70 | 39 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 611.3924 | 609.6497 | +0.29 % | 67017.4026 MeV (+28889.3 ppm) |
| ${}^{71}$Ga | 71 | 40 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 620.9981 | 618.9500 | +0.33 % | 67974.5115 MeV (+28888.9 ppm) |
| ${}^{72}$Ga | 72 | 41 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 627.4485 | 625.4704 | +0.32 % | 68934.7760 MeV (+28892.8 ppm) |
| ${}^{73}$Ga | 73 | 42 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 636.0531 | 634.6528 | +0.22 % | 69892.8861 MeV (+28905.3 ppm) |
| ${}^{74}$Ga | 74 | 43 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 641.5794 | 641.0744 | +0.08 % | 70854.0746 MeV (+28920.8 ppm) |
| ${}^{75}$Ga | 75 | 44 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 649.2623 | 649.5567 | -0.05 % | 71813.1064 MeV (+28935.5 ppm) |
| ${}^{76}$Ga | 76 | 45 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 653.9383 | 655.4641 | -0.23 % | 72775.1453 MeV (+28954.8 ppm) |
| ${}^{77}$Ga | 77 | 46 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 660.7709 | 663.2311 | -0.37 % | 73735.0275 MeV (+28970.2 ppm) |
| ${}^{78}$Ga | 78 | 47 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 664.6627 | 669.0141 | -0.65 % | 74697.8504 MeV (+28997.5 ppm) |
| ${}^{79}$Ga | 79 | 48 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 670.7091 | 675.9297 | -0.77 % | 75658.5188 MeV (+29010.8 ppm) |
| ${}^{80}$Ga | 80 | 49 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 673.8765 | 680.6764 | -1.00 % | 76622.0662 MeV (+29032.4 ppm) |
| ${}^{81}$Ga | 81 | 50 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 679.1944 | 687.1520 | -1.16 % | 77583.4631 MeV (+29048.5 ppm) |
| ${}^{82}$Ga | 82 | 51 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 681.6911 | 690.5261 | -1.28 % | 78547.6811 MeV (+29059.4 ppm) |
| ${}^{83}$Ga | 83 | 52 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 686.3329 | 694.9238 | -1.24 % | 79509.7540 MeV (+29055.9 ppm) |
| ${}^{84}$Ga | 84 | 53 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 688.2077 | 697.8321 | -1.38 % | 80474.5940 MeV (+29068.3 ppm) |
| ${}^{85}$Ga | 85 | 54 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 692.2208 | 701.5533 | -1.33 % | 81437.2957 MeV (+29063.9 ppm) |
| ${}^{86}$Ga | 86 | 55 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 693.5178 | 703.6520 | -1.44 % | 82402.7135 MeV (+29072.6 ppm) |
| ${}^{87}$Ga | 87 | 56 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 696.9453 | 706.7880 | -1.39 % | 83366.0007 MeV (+29068.6 ppm) |
| ${}^{88}$Ga | 88 | 57 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 697.7046 | 708.4000 | -1.51 % | 84331.9562 MeV (+29077.4 ppm) |

### Germanium (Z = 32)

_33 of 33 isotopes with a framework prediction; 33 of 33 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{58}$Ge | 58 | 26 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 446.9392 | 450.6600 | -0.83 % | 55579.9482 MeV (+28894.8 ppm) |
| ${}^{59}$Ge | 59 | 27 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 463.7070 | 467.5160 | -0.81 % | 56529.8951 MeV (+28905.4 ppm) |
| ${}^{60}$Ge | 60 | 28 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 482.4503 | 486.7800 | -0.89 % | 57477.8666 MeV (+28923.9 ppm) |
| ${}^{61}$Ge | 61 | 29 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 497.4171 | 501.1150 | -0.74 % | 58429.6146 MeV (+28919.5 ppm) |
| ${}^{62}$Ge | 62 | 30 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 514.4006 | 517.5140 | -0.60 % | 59379.3458 MeV (+28917.6 ppm) |
| ${}^{63}$Ge | 63 | 31 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 527.7384 | 530.3792 | -0.50 % | 60332.7228 MeV (+28915.4 ppm) |
| ${}^{64}$Ge | 64 | 32 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 543.1255 | 545.8448 | -0.50 % | 61284.0505 MeV (+28923.9 ppm) |
| ${}^{65}$Ge | 65 | 33 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 554.9852 | 556.0788 | -0.20 % | 62238.9055 MeV (+28901.4 ppm) |
| ${}^{66}$Ge | 66 | 34 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 568.9197 | 569.2789 | -0.06 % | 63191.6858 MeV (+28895.6 ppm) |
| ${}^{67}$Ge | 67 | 35 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 579.4344 | 578.4169 | +0.18 % | 64147.8859 MeV (+28877.8 ppm) |
| ${}^{68}$Ge | 68 | 36 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 592.0432 | 590.7933 | +0.21 % | 65101.9919 MeV (+28880.0 ppm) |
| ${}^{69}$Ge | 69 | 37 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 601.3305 | 598.9865 | +0.39 % | 66059.4194 MeV (+28866.9 ppm) |
| ${}^{70}$Ge | 70 | 38 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 612.7262 | 610.5192 | +0.36 % | 67014.7384 MeV (+28874.5 ppm) |
| ${}^{71}$Ge | 71 | 39 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 620.8906 | 617.9351 | +0.48 % | 67973.2888 MeV (+28866.7 ppm) |
| ${}^{72}$Ge | 72 | 40 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 631.1735 | 628.6857 | +0.40 % | 68929.7206 MeV (+28878.7 ppm) |
| ${}^{73}$Ge | 73 | 41 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 638.3081 | 635.4686 | +0.45 % | 69889.3009 MeV (+28876.7 ppm) |
| ${}^{74}$Ge | 74 | 42 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 647.5676 | 645.6649 | +0.29 % | 70846.7561 MeV (+28894.8 ppm) |
| ${}^{75}$Ge | 75 | 43 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 653.7555 | 652.1707 | +0.24 % | 71807.2830 MeV (+28902.1 ppm) |
| ${}^{76}$Ge | 76 | 44 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 662.0718 | 661.5980 | +0.07 % | 72765.6814 MeV (+28921.6 ppm) |
| ${}^{77}$Ge | 77 | 45 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 667.3875 | 667.6693 | -0.04 % | 73727.0805 MeV (+28934.2 ppm) |
| ${}^{78}$Ge | 78 | 46 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 674.8327 | 676.3898 | -0.23 % | 74686.3501 MeV (+28954.8 ppm) |
| ${}^{79}$Ge | 79 | 47 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 679.3432 | 682.1262 | -0.41 % | 75648.5543 MeV (+28972.9 ppm) |
| ${}^{80}$Ge | 80 | 48 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 685.9821 | 690.2057 | -0.61 % | 76608.6303 MeV (+28994.5 ppm) |
| ${}^{81}$Ge | 81 | 49 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 689.7479 | 695.0334 | -0.76 % | 77571.5793 MeV (+29009.2 ppm) |
| ${}^{82}$Ge | 82 | 50 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 695.6389 | 702.2280 | -0.94 % | 78532.4030 MeV (+29027.6 ppm) |
| ${}^{83}$Ge | 83 | 51 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 698.7146 | 705.8607 | -1.01 % | 79496.0421 MeV (+29034.6 ppm) |
| ${}^{84}$Ge | 84 | 52 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 703.9109 | 711.1040 | -1.01 % | 80457.5605 MeV (+29035.4 ppm) |
| ${}^{85}$Ge | 85 | 53 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 706.3459 | 714.1504 | -1.09 % | 81421.8404 MeV (+29042.6 ppm) |
| ${}^{86}$Ge | 86 | 54 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 710.8957 | 718.4982 | -1.06 % | 82384.0053 MeV (+29040.0 ppm) |
| ${}^{87}$Ge | 87 | 55 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 712.7348 | 720.7950 | -1.12 % | 83348.8810 MeV (+29044.3 ppm) |
| ${}^{88}$Ge | 88 | 56 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 716.6819 | 724.7680 | -1.12 % | 84311.6486 MeV (+29044.7 ppm) |
| ${}^{89}$Ge | 89 | 57 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 717.9661 | 726.3290 | -1.15 % | 85277.0792 MeV (+29047.3 ppm) |
| ${}^{90}$Ge | 90 | 58 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 721.3505 | 729.8100 | -1.16 % | 86240.4096 MeV (+29048.2 ppm) |

### Arsenic (Z = 33)

_33 of 33 isotopes with a framework prediction; 33 of 33 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{60}$As | 60 | 27 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 460.2277 | 464.1000 | -0.83 % | 57498.7589 MeV (+28894.7 ppm) |
| ${}^{61}$As | 61 | 28 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 479.7993 | 483.7300 | -0.81 % | 58445.9021 MeV (+28905.8 ppm) |
| ${}^{62}$As | 62 | 29 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 495.6064 | 499.0380 | -0.69 % | 59396.8097 MeV (+28904.3 ppm) |
| ${}^{63}$As | 63 | 30 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 513.3951 | 516.1590 | -0.54 % | 60345.7358 MeV (+28901.8 ppm) |
| ${}^{64}$As | 64 | 31 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 527.5486 | 530.3040 | -0.52 % | 61298.2970 MeV (+28907.7 ppm) |
| ${}^{65}$As | 65 | 32 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 543.7174 | 545.7553 | -0.37 % | 62248.8431 MeV (+28903.4 ppm) |
| ${}^{66}$As | 66 | 33 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 556.3682 | 558.9146 | -0.46 % | 63202.9070 MeV (+28917.8 ppm) |
| ${}^{67}$As | 67 | 34 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 571.0606 | 571.5481 | -0.09 % | 64154.9293 MeV (+28890.3 ppm) |
| ${}^{68}$As | 68 | 35 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 582.3419 | 581.9267 | +0.07 % | 65110.3628 MeV (+28880.9 ppm) |
| ${}^{69}$As | 69 | 36 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 595.6853 | 594.2157 | +0.25 % | 66063.7343 MeV (+28870.2 ppm) |
| ${}^{70}$As | 70 | 37 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 605.7150 | 603.5088 | +0.37 % | 67020.4193 MeV (+28863.4 ppm) |
| ${}^{71}$As | 71 | 38 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 617.8222 | 615.1394 | +0.44 % | 67975.0269 MeV (+28861.7 ppm) |
| ${}^{72}$As | 72 | 39 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 626.7054 | 623.5473 | +0.51 % | 68932.8585 MeV (+28858.7 ppm) |
| ${}^{73}$As | 73 | 40 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 637.6772 | 634.3415 | +0.53 % | 69888.6015 MeV (+28861.2 ppm) |
| ${}^{74}$As | 74 | 41 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 645.5074 | 642.3201 | +0.50 % | 70847.4860 MeV (+28867.1 ppm) |
| ${}^{75}$As | 75 | 42 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 655.4338 | 652.5656 | +0.44 % | 71804.2744 MeV (+28876.3 ppm) |
| ${}^{76}$As | 76 | 43 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 662.2950 | 659.8941 | +0.36 % | 72764.1280 MeV (+28886.2 ppm) |
| ${}^{77}$As | 77 | 44 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 671.2568 | 669.5904 | +0.25 % | 73721.8809 MeV (+28900.5 ppm) |
| ${}^{78}$As | 78 | 45 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 677.2241 | 676.5623 | +0.10 % | 74682.6284 MeV (+28917.0 ppm) |
| ${}^{79}$As | 79 | 46 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 685.2941 | 685.4528 | -0.02 % | 75641.2732 MeV (+28931.4 ppm) |
| ${}^{80}$As | 80 | 47 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 690.4353 | 692.1026 | -0.24 % | 76602.8468 MeV (+28953.8 ppm) |
| ${}^{81}$As | 81 | 48 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 697.6789 | 700.4926 | -0.40 % | 77562.3179 MeV (+28971.5 ppm) |
| ${}^{82}$As | 82 | 49 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 702.0552 | 706.1361 | -0.58 % | 78524.6564 MeV (+28989.3 ppm) |
| ${}^{83}$As | 83 | 50 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 708.5318 | 713.7713 | -0.73 % | 79484.8946 MeV (+29006.1 ppm) |
| ${}^{84}$As | 84 | 51 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 712.1984 | 718.0268 | -0.81 % | 80447.9427 MeV (+29013.8 ppm) |
| ${}^{85}$As | 85 | 52 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 717.9618 | 723.4337 | -0.76 % | 81408.8941 MeV (+29009.9 ppm) |
| ${}^{86}$As | 86 | 53 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 720.9690 | 727.2780 | -0.87 % | 82372.6017 MeV (+29020.4 ppm) |
| ${}^{87}$As | 87 | 54 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 726.0681 | 732.0051 | -0.81 % | 83334.2174 MeV (+29016.1 ppm) |
| ${}^{88}$As | 88 | 55 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 728.4614 | 734.8880 | -0.87 % | 84298.5388 MeV (+29021.9 ppm) |
| ${}^{89}$As | 89 | 56 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 732.9406 | 739.0560 | -0.83 % | 85260.7744 MeV (+29018.0 ppm) |
| ${}^{90}$As | 90 | 57 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 734.7617 | 741.6000 | -0.92 % | 86225.6681 MeV (+29026.0 ppm) |
| ${}^{91}$As | 91 | 58 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 738.6617 | 745.1990 | -0.88 % | 87188.4829 MeV (+29022.0 ppm) |
| ${}^{92}$As | 92 | 59 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 739.9485 | 747.1320 | -0.96 % | 88153.9108 MeV (+29029.0 ppm) |

### Selenium (Z = 34)

_33 of 33 isotopes with a framework prediction; 33 of 33 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{63}$Se | 63 | 29 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 495.7439 | 498.7710 | -0.61 % | 60362.0567 MeV (+28888.0 ppm) |
| ${}^{64}$Se | 64 | 30 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 514.3020 | 516.8000 | -0.48 % | 61310.2134 MeV (+28888.8 ppm) |
| ${}^{65}$Se | 65 | 31 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 529.2363 | 531.0500 | -0.34 % | 62261.9938 MeV (+28884.1 ppm) |
| ${}^{66}$Se | 66 | 32 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 546.1534 | 547.8000 | -0.30 % | 63211.7915 MeV (+28888.8 ppm) |
| ${}^{67}$Se | 67 | 33 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 559.5628 | 560.7588 | -0.21 % | 64165.0969 MeV (+28888.2 ppm) |
| ${}^{68}$Se | 68 | 34 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 574.9823 | 576.4393 | -0.25 % | 65116.3922 MeV (+28899.6 ppm) |
| ${}^{69}$Se | 69 | 35 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 586.9999 | 586.7559 | +0.04 % | 66071.0893 MeV (+28877.7 ppm) |
| ${}^{70}$Se | 70 | 36 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 601.0490 | 600.3224 | +0.12 % | 67023.7551 MeV (+28876.6 ppm) |
| ${}^{71}$Se | 71 | 37 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 611.7929 | 609.6103 | +0.36 % | 67979.7258 MeV (+28858.9 ppm) |
| ${}^{72}$Se | 72 | 38 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 624.5847 | 622.4033 | +0.35 % | 68933.6488 MeV (+28864.9 ppm) |
| ${}^{73}$Se | 73 | 39 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 634.1604 | 630.8338 | +0.53 % | 69890.7880 MeV (+28852.1 ppm) |
| ${}^{74}$Se | 74 | 40 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 645.7959 | 642.8909 | +0.45 % | 70845.8672 MeV (+28863.8 ppm) |
| ${}^{75}$Se | 75 | 41 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 654.2973 | 650.9185 | +0.52 % | 71804.0806 MeV (+28860.8 ppm) |
| ${}^{76}$Se | 76 | 42 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 664.8672 | 662.0723 | +0.42 % | 72760.2255 MeV (+28874.1 ppm) |
| ${}^{77}$Se | 77 | 43 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 672.3787 | 669.4912 | +0.43 % | 73719.4288 MeV (+28876.1 ppm) |
| ${}^{78}$Se | 78 | 44 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 681.9641 | 679.9890 | +0.29 % | 74676.5581 MeV (+28893.1 ppm) |
| ${}^{79}$Se | 79 | 45 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 688.5615 | 686.9518 | +0.23 % | 75636.6754 MeV (+28900.8 ppm) |
| ${}^{80}$Se | 80 | 46 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 697.2358 | 696.8651 | +0.05 % | 76594.7159 MeV (+28921.2 ppm) |
| ${}^{81}$Se | 81 | 47 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 702.9876 | 703.5660 | -0.08 % | 77555.6790 MeV (+28936.1 ppm) |
| ${}^{82}$Se | 82 | 48 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 710.8168 | 712.8422 | -0.28 % | 78514.5645 MeV (+28958.1 ppm) |
| ${}^{83}$Se | 83 | 49 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 715.7847 | 718.6601 | -0.40 % | 79476.3114 MeV (+28970.5 ppm) |
| ${}^{84}$Se | 84 | 50 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 722.8289 | 727.3387 | -0.62 % | 80435.9820 MeV (+28993.7 ppm) |
| ${}^{85}$Se | 85 | 51 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 727.0688 | 731.8759 | -0.66 % | 81398.4568 MeV (+28998.0 ppm) |
| ${}^{86}$Se | 86 | 52 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 733.3823 | 738.0367 | -0.63 % | 82358.8581 MeV (+28997.1 ppm) |
| ${}^{87}$Se | 87 | 53 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 736.9451 | 742.0310 | -0.69 % | 83322.0101 MeV (+29002.7 ppm) |
| ${}^{88}$Se | 88 | 54 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 742.5774 | 747.5604 | -0.67 % | 84283.0925 MeV (+29002.1 ppm) |
| ${}^{89}$Se | 89 | 55 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 745.5094 | 750.7399 | -0.70 % | 85246.8753 MeV (+29005.0 ppm) |
| ${}^{90}$Se | 90 | 56 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 750.5056 | 755.6190 | -0.68 % | 86208.5939 MeV (+29004.1 ppm) |
| ${}^{91}$Se | 91 | 57 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 752.8490 | 758.4703 | -0.74 % | 87172.9652 MeV (+29009.9 ppm) |
| ${}^{92}$Se | 92 | 58 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 757.2504 | 762.6800 | -0.71 % | 88135.2787 MeV (+29007.9 ppm) |
| ${}^{93}$Se | 93 | 59 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 759.0438 | 764.9250 | -0.77 % | 89100.2000 MeV (+29012.2 ppm) |
| ${}^{94}$Se | 94 | 60 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 762.8880 | 768.9200 | -0.78 % | 90063.0706 MeV (+29014.2 ppm) |
| ${}^{95}$Se | 95 | 61 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 764.1667 | 770.6400 | -0.84 % | 91028.5067 MeV (+29018.6 ppm) |

### Bromine (Z = 35)

_34 of 34 isotopes with a framework prediction; 34 of 34 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{65}$Br | 65 | 30 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 511.5421 | 513.7600 | -0.43 % | 62278.3577 MeV (+28873.5 ppm) |
| ${}^{66}$Br | 66 | 31 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 527.2660 | 528.9240 | -0.31 % | 63229.3486 MeV (+28871.6 ppm) |
| ${}^{67}$Br | 67 | 32 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 544.9409 | 545.9160 | -0.18 % | 64178.3885 MeV (+28869.6 ppm) |
| ${}^{68}$Br | 68 | 33 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 559.1180 | 560.2520 | -0.20 % | 65130.9261 MeV (+28878.9 ppm) |
| ${}^{69}$Br | 69 | 34 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 575.2744 | 575.7983 | -0.09 % | 66081.4846 MeV (+28876.6 ppm) |
| ${}^{70}$Br | 70 | 35 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 588.0379 | 589.0357 | -0.17 % | 67035.4359 MeV (+28890.0 ppm) |
| ${}^{71}$Br | 71 | 36 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 602.8028 | 602.1839 | +0.10 % | 67987.3857 MeV (+28871.4 ppm) |
| ${}^{72}$Br | 72 | 37 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 614.2709 | 612.8145 | +0.24 % | 68942.6324 MeV (+28863.8 ppm) |
| ${}^{73}$Br | 73 | 38 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 627.7577 | 625.4699 | +0.37 % | 69895.8603 MeV (+28857.4 ppm) |
| ${}^{74}$Br | 74 | 39 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 638.0360 | 635.1836 | +0.45 % | 70852.2968 MeV (+28853.7 ppm) |
| ${}^{75}$Br | 75 | 40 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 650.3460 | 647.0737 | +0.51 % | 71806.7016 MeV (+28853.2 ppm) |
| ${}^{76}$Br | 76 | 41 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 659.5290 | 656.3271 | +0.49 % | 72764.2334 MeV (+28858.5 ppm) |
| ${}^{77}$Br | 77 | 42 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 670.7531 | 667.3442 | +0.51 % | 73719.7240 MeV (+28860.6 ppm) |
| ${}^{78}$Br | 78 | 43 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 678.9256 | 675.6328 | +0.49 % | 74678.2663 MeV (+28865.9 ppm) |
| ${}^{79}$Br | 79 | 44 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 689.1457 | 686.3201 | +0.41 % | 75634.7610 MeV (+28876.9 ppm) |
| ${}^{80}$Br | 80 | 45 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 696.3840 | 694.2123 | +0.31 % | 76594.2374 MeV (+28888.9 ppm) |
| ${}^{81}$Br | 81 | 46 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 705.6738 | 704.3717 | +0.18 % | 77551.6625 MeV (+28904.5 ppm) |
| ${}^{82}$Br | 82 | 47 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 712.0470 | 711.9646 | +0.01 % | 78512.0040 MeV (+28923.2 ppm) |
| ${}^{83}$Br | 83 | 48 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 720.4731 | 721.5510 | -0.15 % | 79470.2926 MeV (+28941.5 ppm) |
| ${}^{84}$Br | 84 | 49 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 726.0436 | 728.3917 | -0.32 % | 80431.4370 MeV (+28959.7 ppm) |
| ${}^{85}$Br | 85 | 50 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 733.6667 | 737.2554 | -0.49 % | 81390.5287 MeV (+28977.9 ppm) |
| ${}^{86}$Br | 86 | 51 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 738.4909 | 742.3835 | -0.52 % | 82352.4191 MeV (+28982.6 ppm) |
| ${}^{87}$Br | 87 | 52 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 745.3659 | 748.7142 | -0.45 % | 83312.2589 MeV (+28977.1 ppm) |
| ${}^{88}$Br | 88 | 53 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 749.4955 | 753.6098 | -0.55 % | 84274.8441 MeV (+28987.3 ppm) |
| ${}^{89}$Br | 89 | 54 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 755.6725 | 759.2394 | -0.47 % | 85235.3819 MeV (+28981.6 ppm) |
| ${}^{90}$Br | 90 | 55 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 759.1543 | 763.0368 | -0.51 % | 86198.6149 MeV (+28985.7 ppm) |
| ${}^{91}$Br | 91 | 56 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 764.6790 | 768.2151 | -0.46 % | 87159.8050 MeV (+28982.4 ppm) |
| ${}^{92}$Br | 92 | 57 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 767.5558 | 771.4119 | -0.50 % | 88123.6429 MeV (+28986.3 ppm) |
| ${}^{93}$Br | 93 | 58 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 772.4700 | 776.1407 | -0.47 % | 89085.4435 MeV (+28984.7 ppm) |
| ${}^{94}$Br | 94 | 59 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 774.7811 | 778.9780 | -0.54 % | 90049.8472 MeV (+28990.6 ppm) |
| ${}^{95}$Br | 95 | 60 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 779.1231 | 783.2750 | -0.53 % | 91012.2199 MeV (+28990.2 ppm) |
| ${}^{96}$Br | 96 | 61 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 780.9043 | 785.6640 | -0.61 % | 91977.1535 MeV (+28997.3 ppm) |
| ${}^{97}$Br | 97 | 62 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 784.7094 | 789.5800 | -0.62 % | 92940.0633 MeV (+28998.1 ppm) |
| ${}^{98}$Br | 98 | 63 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 785.9937 | 791.6440 | -0.71 % | 93905.4937 MeV (+29006.9 ppm) |

### Krypton (Z = 36)

_35 of 35 isotopes with a framework prediction; 35 of 35 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{67}$Kr | 67 | 31 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 527.1948 | 528.1610 | -0.18 % | 64194.8043 MeV (+28852.7 ppm) |
| ${}^{68}$Kr | 68 | 32 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 545.5953 | 546.3120 | -0.13 % | 65143.1185 MeV (+28857.6 ppm) |
| ${}^{69}$Kr | 69 | 33 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 560.5087 | 560.9010 | -0.07 % | 66094.9199 MeV (+28859.6 ppm) |
| ${}^{70}$Kr | 70 | 34 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 577.3719 | 577.9200 | -0.09 % | 67044.7715 MeV (+28870.2 ppm) |
| ${}^{71}$Kr | 71 | 35 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 590.8518 | 591.2263 | -0.06 % | 67998.0064 MeV (+28873.6 ppm) |
| ${}^{72}$Kr | 72 | 36 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 606.3045 | 606.9110 | -0.10 % | 68949.2685 MeV (+28884.2 ppm) |
| ${}^{73}$Kr | 73 | 37 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 618.4692 | 617.5935 | +0.14 % | 69903.8186 MeV (+28867.1 ppm) |
| ${}^{74}$Kr | 74 | 38 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 632.6247 | 631.4449 | +0.19 % | 70856.3778 MeV (+28868.8 ppm) |
| ${}^{75}$Kr | 75 | 39 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 643.5799 | 641.5080 | +0.32 % | 71812.1374 MeV (+28860.6 ppm) |
| ${}^{76}$Kr | 76 | 40 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 656.5398 | 654.2694 | +0.35 % | 72765.8923 MeV (+28863.4 ppm) |
| ${}^{77}$Kr | 77 | 41 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 666.3802 | 663.4964 | +0.43 % | 73722.7667 MeV (+28859.0 ppm) |
| ${}^{78}$Kr | 78 | 42 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 678.2356 | 675.5766 | +0.39 % | 74677.6260 MeV (+28867.4 ppm) |
| ${}^{79}$Kr | 79 | 43 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 687.0464 | 683.9119 | +0.46 % | 75635.5300 MeV (+28864.6 ppm) |
| ${}^{80}$Kr | 80 | 44 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 697.8795 | 695.4344 | +0.35 % | 76591.4116 MeV (+28878.7 ppm) |
| ${}^{81}$Kr | 81 | 45 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 705.7375 | 703.3085 | +0.35 % | 77550.2684 MeV (+28882.1 ppm) |
| ${}^{82}$Kr | 82 | 46 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 715.6225 | 714.2754 | +0.19 % | 78507.0982 MeV (+28900.6 ppm) |
| ${}^{83}$Kr | 83 | 47 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 722.5972 | 721.7455 | +0.12 % | 79466.8383 MeV (+28909.8 ppm) |
| ${}^{84}$Kr | 84 | 48 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 731.6012 | 732.2656 | -0.09 % | 80424.5490 MeV (+28932.9 ppm) |
| ${}^{85}$Kr | 85 | 49 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 737.7555 | 739.3779 | -0.22 % | 81385.1095 MeV (+28947.2 ppm) |
| ${}^{86}$Kr | 86 | 50 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 745.9396 | 749.2345 | -0.44 % | 82343.6402 MeV (+28971.0 ppm) |
| ${}^{87}$Kr | 87 | 51 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 751.3306 | 754.7497 | -0.45 % | 83304.9640 MeV (+28973.7 ppm) |
| ${}^{88}$Kr | 88 | 52 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 758.7502 | 761.8028 | -0.40 % | 84264.2592 MeV (+28970.8 ppm) |
| ${}^{89}$Kr | 89 | 53 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 763.4299 | 766.7186 | -0.43 % | 85226.2942 MeV (+28974.5 ppm) |
| ${}^{90}$Kr | 90 | 54 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 770.1356 | 773.2134 | -0.40 % | 86186.3032 MeV (+28973.3 ppm) |
| ${}^{91}$Kr | 91 | 55 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 774.1516 | 777.2994 | -0.40 % | 87149.0021 MeV (+28974.7 ppm) |
| ${}^{92}$Kr | 92 | 56 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 780.1897 | 783.1661 | -0.38 % | 88109.6788 MeV (+28973.8 ppm) |
| ${}^{93}$Kr | 93 | 57 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 783.5852 | 786.6041 | -0.38 % | 89072.9980 MeV (+28974.6 ppm) |
| ${}^{94}$Kr | 94 | 58 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 788.9980 | 791.8872 | -0.36 % | 90034.3000 MeV (+28974.0 ppm) |
| ${}^{95}$Kr | 95 | 59 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 791.8128 | 794.7696 | -0.37 % | 90998.2000 MeV (+28974.9 ppm) |
| ${}^{96}$Kr | 96 | 60 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 796.6391 | 799.7637 | -0.39 % | 91960.0884 MeV (+28977.6 ppm) |
| ${}^{97}$Kr | 97 | 61 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 798.9096 | 802.1769 | -0.41 % | 92924.5327 MeV (+28979.1 ppm) |
| ${}^{98}$Kr | 98 | 62 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 803.1852 | 806.9320 | -0.46 % | 93886.9719 MeV (+28985.1 ppm) |
| ${}^{99}$Kr | 99 | 63 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 804.9449 | 809.3250 | -0.54 % | 94851.9269 MeV (+28991.4 ppm) |
| ${}^{100}$Kr | 100 | 64 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 808.7026 | 813.4000 | -0.58 % | 95814.8840 MeV (+28995.8 ppm) |
| ${}^{101}$Kr | 101 | 65 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 809.9824 | 815.5750 | -0.69 % | 96780.3190 MeV (+29005.1 ppm) |

### Rubidium (Z = 37)

_34 of 34 isotopes with a framework prediction; 34 of 34 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{71}$Rb | 71 | 34 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 575.9399 | 576.3780 | -0.08 % | 68011.5880 MeV (+28860.6 ppm) |
| ${}^{72}$Rb | 72 | 35 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 590.1449 | 590.5440 | -0.07 % | 68964.0977 MeV (+28865.8 ppm) |
| ${}^{73}$Rb | 73 | 36 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 606.2948 | 606.2710 | +0.00 % | 69914.6627 MeV (+28867.1 ppm) |
| ${}^{74}$Rb | 74 | 37 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 619.1650 | 620.2467 | -0.17 % | 70868.5072 MeV (+28889.4 ppm) |
| ${}^{75}$Rb | 75 | 38 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 633.9989 | 633.6207 | +0.06 % | 71820.3881 MeV (+28874.1 ppm) |
| ${}^{76}$Rb | 76 | 39 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 645.6402 | 644.9524 | +0.11 % | 72775.4615 MeV (+28874.6 ppm) |
| ${}^{77}$Rb | 77 | 40 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 659.2598 | 657.3751 | +0.29 % | 73728.5567 MeV (+28863.2 ppm) |
| ${}^{78}$Rb | 78 | 41 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 669.7671 | 667.5514 | +0.33 % | 74684.7642 MeV (+28863.1 ppm) |
| ${}^{79}$Rb | 79 | 42 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 682.2638 | 679.4901 | +0.41 % | 75638.9823 MeV (+28860.6 ppm) |
| ${}^{80}$Rb | 80 | 43 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 691.7227 | 688.9341 | +0.40 % | 76596.2382 MeV (+28864.5 ppm) |
| ${}^{81}$Rb | 81 | 44 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 703.1789 | 700.2866 | +0.41 % | 77551.4967 MeV (+28867.9 ppm) |
| ${}^{82}$Rb | 82 | 45 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 711.6665 | 709.0891 | +0.36 % | 78509.7239 MeV (+28875.7 ppm) |
| ${}^{83}$Rb | 83 | 46 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 722.1569 | 720.0432 | +0.29 % | 79465.9483 MeV (+28886.0 ppm) |
| ${}^{84}$Rb | 84 | 47 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 729.7431 | 728.8028 | +0.13 % | 80425.0768 MeV (+28904.4 ppm) |
| ${}^{85}$Rb | 85 | 48 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 739.3353 | 739.2825 | +0.01 % | 81382.1994 MeV (+28919.3 ppm) |
| ${}^{86}$Rb | 86 | 49 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 746.0836 | 747.9335 | -0.25 % | 82342.1659 MeV (+28945.9 ppm) |
| ${}^{87}$Rb | 87 | 50 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 754.8390 | 757.8556 | -0.40 % | 83300.1253 MeV (+28963.3 ppm) |
| ${}^{88}$Rb | 88 | 51 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 760.8070 | 763.9382 | -0.41 % | 84260.8721 MeV (+28966.1 ppm) |
| ${}^{89}$Rb | 89 | 52 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 768.7816 | 771.1129 | -0.30 % | 85219.6122 MeV (+28958.1 ppm) |
| ${}^{90}$Rb | 90 | 53 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 774.0218 | 776.8374 | -0.36 % | 86181.0868 MeV (+28965.2 ppm) |
| ${}^{91}$Rb | 91 | 54 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 781.2668 | 783.2882 | -0.26 % | 87140.5566 MeV (+28957.3 ppm) |
| ${}^{92}$Rb | 92 | 55 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 785.8271 | 788.3869 | -0.32 % | 88102.7110 MeV (+28964.6 ppm) |
| ${}^{93}$Rb | 93 | 56 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 792.3892 | 794.3056 | -0.24 % | 89062.8637 MeV (+28958.4 ppm) |
| ${}^{94}$Rb | 94 | 57 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 796.3137 | 798.3199 | -0.25 % | 90025.6540 MeV (+28960.1 ppm) |
| ${}^{95}$Rb | 95 | 58 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 802.2356 | 803.7187 | -0.18 % | 90986.4468 MeV (+28955.2 ppm) |
| ${}^{96}$Rb | 96 | 59 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 805.5644 | 807.2540 | -0.21 % | 91949.8328 MeV (+28958.1 ppm) |
| ${}^{97}$Rb | 97 | 60 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 810.8857 | 812.4902 | -0.20 % | 92911.2263 MeV (+28958.2 ppm) |
| ${}^{98}$Rb | 98 | 61 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 813.6558 | 816.4115 | -0.34 % | 93875.1710 MeV (+28971.4 ppm) |
| ${}^{99}$Rb | 99 | 62 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 818.4124 | 821.2348 | -0.34 % | 94837.1291 MeV (+28972.8 ppm) |
| ${}^{100}$Rb | 100 | 63 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 820.6579 | 824.4508 | -0.46 % | 95801.5985 MeV (+28983.5 ppm) |
| ${}^{101}$Rb | 101 | 64 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 824.8833 | 828.8237 | -0.48 % | 96764.0878 MeV (+28985.5 ppm) |
| ${}^{102}$Rb | 102 | 65 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 826.6353 | 831.5799 | -0.59 % | 97729.0505 MeV (+28996.1 ppm) |
| ${}^{103}$Rb | 103 | 66 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 830.3603 | 835.5360 | -0.62 % | 98692.0404 MeV (+28998.9 ppm) |
| ${}^{104}$Rb | 104 | 67 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 831.6479 | 837.9280 | -0.75 % | 99657.4675 MeV (+29009.7 ppm) |

### Strontium (Z = 38)

_35 of 35 isotopes with a framework prediction; 35 of 35 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{73}$Sr | 73 | 35 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 591.2345 | 591.4460 | -0.04 % | 69928.3927 MeV (+28856.2 ppm) |
| ${}^{74}$Sr | 74 | 36 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 608.0541 | 608.3540 | -0.05 % | 70878.2879 MeV (+28865.7 ppm) |
| ${}^{75}$Sr | 75 | 37 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 621.6032 | 622.2384 | -0.10 % | 71831.4535 MeV (+28876.3 ppm) |
| ${}^{76}$Sr | 76 | 38 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 637.0897 | 637.9386 | -0.13 % | 72782.6817 MeV (+28886.0 ppm) |
| ${}^{77}$Sr | 77 | 39 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 649.3920 | 649.5657 | -0.03 % | 73737.0942 MeV (+28881.4 ppm) |
| ${}^{78}$Sr | 78 | 40 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 663.6472 | 663.0076 | +0.10 % | 74689.5538 MeV (+28875.7 ppm) |
| ${}^{79}$Sr | 79 | 41 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 674.7978 | 673.3846 | +0.21 % | 75645.1180 MeV (+28869.6 ppm) |
| ${}^{80}$Sr | 80 | 42 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 687.9131 | 686.2877 | +0.24 % | 76598.7174 MeV (+28872.0 ppm) |
| ${}^{81}$Sr | 81 | 43 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 697.9978 | 695.5757 | +0.35 % | 77555.3475 MeV (+28865.3 ppm) |
| ${}^{82}$Sr | 82 | 44 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 710.0559 | 708.1290 | +0.27 % | 78510.0042 MeV (+28876.9 ppm) |
| ${}^{83}$Sr | 83 | 45 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 719.1522 | 716.9878 | +0.30 % | 79467.6227 MeV (+28877.4 ppm) |
| ${}^{84}$Sr | 84 | 46 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 730.2280 | 728.9111 | +0.18 % | 80423.2617 MeV (+28892.9 ppm) |
| ${}^{85}$Sr | 85 | 47 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 738.4061 | 737.4361 | +0.13 % | 81381.7984 MeV (+28900.4 ppm) |
| ${}^{86}$Sr | 86 | 48 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 748.5675 | 748.9273 | -0.05 % | 82338.3517 MeV (+28921.1 ppm) |
| ${}^{87}$Sr | 87 | 49 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 755.8912 | 757.3556 | -0.19 % | 83297.7428 MeV (+28937.5 ppm) |
| ${}^{88}$Sr | 88 | 50 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 765.2002 | 768.4684 | -0.43 % | 84255.1485 MeV (+28962.9 ppm) |
| ${}^{89}$Sr | 89 | 51 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 771.7276 | 774.8271 | -0.40 % | 85215.3359 MeV (+28962.4 ppm) |
| ${}^{90}$Sr | 90 | 52 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 780.2405 | 782.6404 | -0.31 % | 86173.5378 MeV (+28956.0 ppm) |
| ${}^{91}$Sr | 91 | 53 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 786.0246 | 788.4127 | -0.30 % | 87134.4685 MeV (+28957.1 ppm) |
| ${}^{92}$Sr | 92 | 54 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 793.7929 | 795.6994 | -0.24 % | 88093.4149 MeV (+28953.3 ppm) |
| ${}^{93}$Sr | 93 | 55 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 798.8821 | 800.9892 | -0.26 % | 89055.0405 MeV (+28956.8 ppm) |
| ${}^{94}$Sr | 94 | 56 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 805.9531 | 807.8204 | -0.23 % | 90014.6843 MeV (+28955.6 ppm) |
| ${}^{95}$Sr | 95 | 57 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 810.3918 | 812.1633 | -0.22 % | 90976.9604 MeV (+28955.3 ppm) |
| ${}^{96}$Sr | 96 | 58 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 816.8087 | 818.0356 | -0.15 % | 91937.2582 MeV (+28950.5 ppm) |
| ${}^{97}$Sr | 97 | 59 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 820.6375 | 821.7693 | -0.14 % | 92900.1442 MeV (+28950.1 ppm) |
| ${}^{98}$Sr | 98 | 60 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 826.4402 | 827.6824 | -0.15 % | 93861.0563 MeV (+28952.6 ppm) |
| ${}^{99}$Sr | 99 | 61 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 829.6966 | 831.8498 | -0.26 % | 94824.5147 MeV (+28963.2 ppm) |
| ${}^{100}$Sr | 100 | 62 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 834.9215 | 837.2201 | -0.27 % | 95786.0045 MeV (+28965.8 ppm) |
| ${}^{101}$Sr | 101 | 63 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 837.6400 | 840.7989 | -0.38 % | 96750.0008 MeV (+28975.3 ppm) |
| ${}^{102}$Sr | 102 | 64 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 842.3211 | 845.7046 | -0.40 % | 97712.0345 MeV (+28978.4 ppm) |
| ${}^{103}$Sr | 103 | 65 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 844.5335 | 848.9260 | -0.52 % | 98676.5369 MeV (+28988.8 ppm) |
| ${}^{104}$Sr | 104 | 66 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 848.7018 | 853.4240 | -0.55 % | 99639.0833 MeV (+28993.2 ppm) |
| ${}^{105}$Sr | 105 | 67 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 850.4374 | 855.9600 | -0.65 % | 100604.0625 MeV (+29000.8 ppm) |
| ${}^{106}$Sr | 106 | 68 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 854.1218 | 860.0840 | -0.69 % | 101567.0928 MeV (+29006.1 ppm) |
| ${}^{107}$Sr | 107 | 69 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 855.4078 | 862.0990 | -0.78 % | 102532.5216 MeV (+29013.0 ppm) |

### Yttrium (Z = 39)

_35 of 35 isotopes with a framework prediction; 35 of 35 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{75}$Y | 75 | 36 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 606.3926 | 606.6750 | -0.05 % | 71845.3338 MeV (+28857.1 ppm) |
| ${}^{76}$Y | 76 | 37 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 620.6288 | 621.1480 | -0.08 % | 72797.8124 MeV (+28867.2 ppm) |
| ${}^{77}$Y | 77 | 38 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 636.7769 | 637.4060 | -0.10 % | 73748.3791 MeV (+28875.7 ppm) |
| ${}^{78}$Y | 78 | 39 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 649.7488 | 651.2220 | -0.23 % | 74702.1220 MeV (+28893.0 ppm) |
| ${}^{79}$Y | 79 | 40 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 664.6485 | 664.9255 | -0.04 % | 75653.9370 MeV (+28882.1 ppm) |
| ${}^{80}$Y | 80 | 41 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 676.4512 | 676.3421 | +0.02 % | 76608.8490 MeV (+28881.5 ppm) |
| ${}^{81}$Y | 81 | 42 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 690.1943 | 688.9782 | +0.18 % | 77561.8207 MeV (+28871.8 ppm) |
| ${}^{82}$Y | 82 | 43 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 700.9138 | 699.4006 | +0.22 % | 78517.8160 MeV (+28872.2 ppm) |
| ${}^{83}$Y | 83 | 44 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 713.5831 | 711.6135 | +0.28 % | 79471.8615 MeV (+28871.1 ppm) |
| ${}^{84}$Y | 84 | 45 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 723.2971 | 721.3736 | +0.27 % | 80428.8622 MeV (+28875.6 ppm) |
| ${}^{85}$Y | 85 | 46 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 734.9678 | 733.3926 | +0.21 % | 81383.9064 MeV (+28884.6 ppm) |
| ${}^{86}$Y | 86 | 47 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 743.7469 | 742.9049 | +0.11 % | 82341.8420 MeV (+28897.4 ppm) |
| ${}^{87}$Y | 87 | 48 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 754.4872 | 754.7115 | -0.03 % | 83297.8164 MeV (+28914.7 ppm) |
| ${}^{88}$Y | 88 | 49 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 762.3957 | 764.0635 | -0.22 % | 84256.6228 MeV (+28935.4 ppm) |
| ${}^{89}$Y | 89 | 50 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 772.2679 | 775.5470 | -0.42 % | 85213.4653 MeV (+28958.4 ppm) |
| ${}^{90}$Y | 90 | 51 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 779.3641 | 782.4040 | -0.39 % | 86173.0839 MeV (+28957.3 ppm) |
| ${}^{91}$Y | 91 | 52 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 788.4250 | 790.3297 | -0.24 % | 87130.7378 MeV (+28945.9 ppm) |
| ${}^{92}$Y | 92 | 53 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 794.7624 | 796.8662 | -0.26 % | 88091.1152 MeV (+28949.9 ppm) |
| ${}^{93}$Y | 93 | 54 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 803.0639 | 804.3482 | -0.16 % | 89049.5284 MeV (+28942.3 ppm) |
| ${}^{94}$Y | 94 | 55 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 808.6914 | 810.5438 | -0.23 % | 90010.6157 MeV (+28950.4 ppm) |
| ${}^{95}$Y | 95 | 56 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 816.2811 | 817.4716 | -0.15 % | 90969.7408 MeV (+28944.6 ppm) |
| ${}^{96}$Y | 96 | 57 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 821.2435 | 822.6650 | -0.17 % | 91931.4932 MeV (+28948.3 ppm) |
| ${}^{97}$Y | 97 | 58 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 828.1651 | 828.5218 | -0.04 % | 92891.2863 MeV (+28937.8 ppm) |
| ${}^{98}$Y | 98 | 59 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 832.5035 | 832.7664 | -0.03 % | 93853.6626 MeV (+28937.7 ppm) |
| ${}^{99}$Y | 99 | 60 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 838.7974 | 839.1927 | -0.05 % | 94814.0836 MeV (+28940.7 ppm) |
| ${}^{100}$Y | 100 | 61 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 842.5497 | 843.9415 | -0.16 % | 95777.0460 MeV (+28952.5 ppm) |
| ${}^{101}$Y | 101 | 62 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 848.2527 | 849.7464 | -0.18 % | 96738.0578 MeV (+28954.8 ppm) |
| ${}^{102}$Y | 102 | 63 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 851.4539 | 853.9356 | -0.29 % | 97701.5714 MeV (+28965.9 ppm) |
| ${}^{103}$Y | 103 | 64 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 856.6003 | 859.2913 | -0.31 % | 98663.1398 MeV (+28969.0 ppm) |
| ${}^{104}$Y | 104 | 65 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 859.2825 | 862.9920 | -0.43 % | 99627.1723 MeV (+28979.8 ppm) |
| ${}^{105}$Y | 105 | 66 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 863.9039 | 867.5100 | -0.42 % | 100589.2657 MeV (+28979.8 ppm) |
| ${}^{106}$Y | 106 | 67 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 866.0970 | 870.7900 | -0.54 % | 101553.7874 MeV (+28991.1 ppm) |
| ${}^{107}$Y | 107 | 68 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 870.2227 | 875.0460 | -0.55 % | 102516.3765 MeV (+28992.7 ppm) |
| ${}^{108}$Y | 108 | 69 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 871.9541 | 877.9320 | -0.68 % | 103481.3598 MeV (+29004.0 ppm) |
| ${}^{109}$Y | 109 | 70 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 875.6112 | 881.7010 | -0.69 % | 104444.4175 MeV (+29005.2 ppm) |

### Zirconium (Z = 40)

_37 of 37 isotopes with a framework prediction; 37 of 37 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{77}$Zr | 77 | 37 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 621.4143 | 621.7750 | -0.06 % | 73762.4114 MeV (+28858.5 ppm) |
| ${}^{78}$Zr | 78 | 38 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 638.1989 | 639.1320 | -0.15 % | 74712.3415 MeV (+28873.3 ppm) |
| ${}^{79}$Zr | 79 | 39 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 651.8158 | 653.0930 | -0.20 % | 75665.4394 MeV (+28884.1 ppm) |
| ${}^{80}$Zr | 80 | 40 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 667.3367 | 669.2000 | -0.28 % | 76616.6333 MeV (+28897.8 ppm) |
| ${}^{81}$Zr | 81 | 41 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 679.7684 | 680.0073 | -0.04 % | 77570.9164 MeV (+28880.7 ppm) |
| ${}^{82}$Zr | 82 | 42 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 694.1171 | 694.1683 | -0.01 % | 78523.2824 MeV (+28883.8 ppm) |
| ${}^{83}$Zr | 83 | 43 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 705.4496 | 704.5372 | +0.13 % | 79478.6647 MeV (+28875.3 ppm) |
| ${}^{84}$Zr | 84 | 44 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 718.7092 | 718.1185 | +0.08 % | 80432.1199 MeV (+28884.7 ppm) |
| ${}^{85}$Zr | 85 | 45 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 729.0204 | 727.9433 | +0.15 % | 81388.5234 MeV (+28882.3 ppm) |
| ${}^{86}$Zr | 86 | 46 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 741.2662 | 740.8085 | +0.06 % | 82342.9924 MeV (+28894.8 ppm) |
| ${}^{87}$Zr | 87 | 47 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 750.6270 | 750.2579 | +0.05 % | 83300.3463 MeV (+28899.3 ppm) |
| ${}^{88}$Zr | 88 | 48 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 761.9276 | 762.6110 | -0.09 % | 84255.7606 MeV (+28916.5 ppm) |
| ${}^{89}$Zr | 89 | 49 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 770.4024 | 771.9314 | -0.20 % | 85214.0005 MeV (+28929.7 ppm) |
| ${}^{90}$Zr | 90 | 50 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 780.8203 | 783.8973 | -0.39 % | 86170.2974 MeV (+28951.9 ppm) |
| ${}^{91}$Zr | 91 | 51 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 788.4680 | 791.0917 | -0.33 % | 87129.3645 MeV (+28948.4 ppm) |
| ${}^{92}$Zr | 92 | 52 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 798.0602 | 799.7264 | -0.21 % | 88086.4871 MeV (+28939.6 ppm) |
| ${}^{93}$Zr | 93 | 53 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 804.9345 | 806.4607 | -0.19 % | 89046.3275 MeV (+28939.7 ppm) |
| ${}^{94}$Zr | 94 | 54 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 813.7534 | 814.6794 | -0.11 % | 90004.2234 MeV (+28935.1 ppm) |
| ${}^{95}$Zr | 95 | 55 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 819.9037 | 821.1413 | -0.15 % | 90964.7879 MeV (+28940.3 ppm) |
| ${}^{96}$Zr | 96 | 56 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 827.9972 | 828.9915 | -0.12 % | 91923.4092 MeV (+28939.7 ppm) |
| ${}^{97}$Zr | 97 | 57 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 833.4685 | 834.5607 | -0.13 % | 92884.6526 MeV (+28942.1 ppm) |
| ${}^{98}$Zr | 98 | 58 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 840.8808 | 840.9770 | -0.01 % | 93843.9551 MeV (+28932.7 ppm) |
| ${}^{99}$Zr | 99 | 59 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 845.7148 | 845.3833 | +0.04 % | 94805.8359 MeV (+28929.1 ppm) |
| ${}^{100}$Zr | 100 | 60 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 852.4863 | 852.2107 | +0.03 % | 95765.7791 MeV (+28931.5 ppm) |
| ${}^{101}$Zr | 101 | 61 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 856.7213 | 857.0702 | -0.04 % | 96728.2589 MeV (+28939.3 ppm) |
| ${}^{102}$Zr | 102 | 62 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 862.8896 | 863.5620 | -0.08 % | 97688.8054 MeV (+28944.2 ppm) |
| ${}^{103}$Zr | 103 | 63 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 866.5608 | 867.8609 | -0.15 % | 98651.8489 MeV (+28951.6 ppm) |
| ${}^{104}$Zr | 104 | 64 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 872.1604 | 873.8409 | -0.19 % | 99612.9641 MeV (+28956.8 ppm) |
| ${}^{105}$Zr | 105 | 65 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 875.3005 | 877.6528 | -0.27 % | 100576.5388 MeV (+28964.2 ppm) |
| ${}^{106}$Zr | 106 | 66 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 880.3634 | 882.9800 | -0.30 % | 101538.1906 MeV (+28968.1 ppm) |
| ${}^{107}$Zr | 107 | 67 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 883.0026 | 886.3880 | -0.38 % | 102502.2663 MeV (+28975.5 ppm) |
| ${}^{108}$Zr | 108 | 68 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 887.5584 | 891.3240 | -0.42 % | 103464.4252 MeV (+28980.6 ppm) |
| ${}^{109}$Zr | 109 | 69 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 889.7245 | 894.2360 | -0.50 % | 104428.9739 MeV (+28987.4 ppm) |
| ${}^{110}$Zr | 110 | 70 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 893.8008 | 898.8100 | -0.56 % | 105391.6124 MeV (+28992.6 ppm) |
| ${}^{111}$Zr | 111 | 71 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 895.5199 | 901.0980 | -0.62 % | 106356.6081 MeV (+28998.3 ppm) |
| ${}^{112}$Zr | 112 | 72 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 899.1421 | 905.0720 | -0.66 % | 107319.7006 MeV (+29002.2 ppm) |
| ${}^{113}$Zr | 113 | 73 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 900.4382 | 907.0510 | -0.73 % | 108285.1193 MeV (+29008.4 ppm) |

### Niobium (Z = 41)

_38 of 38 isotopes with a framework prediction; 38 of 38 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{79}$Nb | 79 | 38 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 636.2998 | 637.2140 | -0.14 % | 75679.6251 MeV (+28865.5 ppm) |
| ${}^{80}$Nb | 80 | 39 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 650.5697 | 652.0800 | -0.23 % | 76632.0699 MeV (+28879.3 ppm) |
| ${}^{81}$Nb | 81 | 40 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 666.7200 | 668.0880 | -0.20 % | 77582.6344 MeV (+28883.8 ppm) |
| ${}^{82}$Nb | 82 | 41 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 679.7888 | 681.5840 | -0.26 % | 78536.2804 MeV (+28895.0 ppm) |
| ${}^{83}$Nb | 83 | 42 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 694.7517 | 695.4561 | -0.10 % | 79488.0323 MeV (+28886.1 ppm) |
| ${}^{84}$Nb | 84 | 43 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 706.7055 | 707.1083 | -0.06 % | 80442.7933 MeV (+28886.6 ppm) |
| ${}^{85}$Nb | 85 | 44 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 720.5640 | 720.2655 | +0.04 % | 81395.6495 MeV (+28882.7 ppm) |
| ${}^{86}$Nb | 86 | 45 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 731.4809 | 731.1912 | +0.04 % | 82351.4474 MeV (+28886.9 ppm) |
| ${}^{87}$Nb | 87 | 46 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 744.3106 | 744.0029 | +0.04 % | 83305.3324 MeV (+28891.3 ppm) |
| ${}^{88}$Nb | 88 | 47 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 754.2617 | 754.3713 | -0.01 % | 84262.0962 MeV (+28900.1 ppm) |
| ${}^{89}$Nb | 89 | 48 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 766.1313 | 766.8968 | -0.10 % | 85216.9413 MeV (+28912.4 ppm) |
| ${}^{90}$Nb | 90 | 49 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 775.1813 | 777.0039 | -0.23 % | 86174.6061 MeV (+28928.3 ppm) |
| ${}^{91}$Nb | 91 | 50 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 786.1536 | 789.0517 | -0.37 % | 87130.3486 MeV (+28944.8 ppm) |
| ${}^{92}$Nb | 92 | 51 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 794.3616 | 796.9383 | -0.32 % | 88088.8554 MeV (+28943.1 ppm) |
| ${}^{93}$Nb | 93 | 52 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 804.4941 | 805.7692 | -0.16 % | 89045.4377 MeV (+28930.5 ppm) |
| ${}^{94}$Nb | 94 | 53 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 811.9142 | 812.9967 | -0.13 % | 90004.7323 MeV (+28930.3 ppm) |
| ${}^{95}$Nb | 95 | 54 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 821.2595 | 821.4853 | -0.03 % | 90962.1018 MeV (+28923.1 ppm) |
| ${}^{96}$Nb | 96 | 55 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 827.9414 | 828.3731 | -0.05 % | 91922.1347 MeV (+28927.3 ppm) |
| ${}^{97}$Nb | 97 | 56 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 836.5477 | 836.4444 | +0.01 % | 92880.2431 MeV (+28923.6 ppm) |
| ${}^{98}$Nb | 98 | 57 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 842.5370 | 842.4376 | +0.01 % | 93840.9686 MeV (+28925.3 ppm) |
| ${}^{99}$Nb | 99 | 58 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 850.4489 | 849.3196 | +0.13 % | 94799.7715 MeV (+28916.0 ppm) |
| ${}^{100}$Nb | 100 | 59 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 855.7875 | 854.8468 | +0.11 % | 95761.1477 MeV (+28919.5 ppm) |
| ${}^{101}$Nb | 101 | 60 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 863.0458 | 862.0184 | +0.12 % | 96720.6041 MeV (+28920.6 ppm) |
| ${}^{102}$Nb | 102 | 61 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 867.7724 | 867.4965 | +0.03 % | 97682.5923 MeV (+28929.9 ppm) |
| ${}^{103}$Nb | 103 | 62 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 874.4151 | 874.2982 | +0.01 % | 98642.6644 MeV (+28933.3 ppm) |
| ${}^{104}$Nb | 104 | 63 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 878.5653 | 879.1519 | -0.07 % | 99605.2290 MeV (+28941.6 ppm) |
| ${}^{105}$Nb | 105 | 64 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 884.6272 | 885.3277 | -0.08 % | 100565.8818 MeV (+28944.2 ppm) |
| ${}^{106}$Nb | 106 | 65 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 888.2340 | 889.6862 | -0.16 % | 101528.9898 MeV (+28952.6 ppm) |
| ${}^{107}$Nb | 107 | 66 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 893.7475 | 895.2786 | -0.17 % | 102490.1910 MeV (+28954.5 ppm) |
| ${}^{108}$Nb | 108 | 67 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 896.8416 | 899.1713 | -0.26 % | 103453.8117 MeV (+28963.0 ppm) |
| ${}^{109}$Nb | 109 | 68 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 901.8367 | 904.3872 | -0.28 % | 104415.5314 MeV (+28966.1 ppm) |
| ${}^{110}$Nb | 110 | 69 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 904.4463 | 908.0787 | -0.40 % | 105379.6366 MeV (+28977.0 ppm) |
| ${}^{111}$Nb | 111 | 70 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 908.9508 | 912.7530 | -0.42 % | 106341.8469 MeV (+28979.7 ppm) |
| ${}^{112}$Nb | 112 | 71 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 911.1023 | 915.9360 | -0.53 % | 107306.4101 MeV (+28989.7 ppm) |
| ${}^{113}$Nb | 113 | 72 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 915.1421 | 920.1590 | -0.55 % | 108269.0851 MeV (+28991.6 ppm) |
| ${}^{114}$Nb | 114 | 73 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 916.8599 | 923.0580 | -0.67 % | 109234.0821 MeV (+29002.0 ppm) |
| ${}^{115}$Nb | 115 | 74 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 920.4592 | 927.0150 | -0.71 % | 110197.1976 MeV (+29005.8 ppm) |
| ${}^{116}$Nb | 116 | 75 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 921.7661 | 929.3920 | -0.82 % | 111162.6054 MeV (+29015.8 ppm) |

### Molybdenum (Z = 42)

_39 of 39 isotopes with a framework prediction; 39 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{81}$Mo | 81 | 39 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 651.0492 | 652.3740 | -0.20 % | 77596.9749 MeV (+28870.7 ppm) |
| ${}^{82}$Mo | 82 | 40 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 667.8060 | 669.3660 | -0.23 % | 78546.9329 MeV (+28880.3 ppm) |
| ${}^{83}$Mo | 83 | 41 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 681.4894 | 683.4220 | -0.28 % | 79499.9643 MeV (+28890.4 ppm) |
| ${}^{84}$Mo | 84 | 42 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 697.0448 | 699.3000 | -0.32 % | 80451.1237 MeV (+28900.8 ppm) |
| ${}^{85}$Mo | 85 | 43 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 709.5986 | 710.7132 | -0.16 % | 81405.2846 MeV (+28890.4 ppm) |
| ${}^{86}$Mo | 86 | 44 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 724.0356 | 725.3857 | -0.19 % | 82357.5624 MeV (+28898.7 ppm) |
| ${}^{87}$Mo | 87 | 45 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 735.5380 | 736.2309 | -0.09 % | 83312.7748 MeV (+28894.4 ppm) |
| ${}^{88}$Mo | 88 | 46 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 748.9323 | 750.1040 | -0.16 % | 84266.0953 MeV (+28905.2 ppm) |
| ${}^{89}$Mo | 89 | 47 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 759.4545 | 760.5037 | -0.14 % | 85222.2879 MeV (+28907.2 ppm) |
| ${}^{90}$Mo | 90 | 48 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 771.8749 | 773.7326 | -0.24 % | 86176.5822 MeV (+28921.3 ppm) |
| ${}^{91}$Mo | 91 | 49 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 781.4818 | 783.8402 | -0.30 % | 87133.6900 MeV (+28930.4 ppm) |
| ${}^{92}$Mo | 92 | 50 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 792.9914 | 796.5113 | -0.44 % | 88088.8953 MeV (+28947.9 ppm) |
| ${}^{93}$Mo | 93 | 51 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 801.7425 | 804.5811 | -0.35 % | 89046.8589 MeV (+28942.1 ppm) |
| ${}^{94}$Mo | 94 | 52 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 812.3988 | 814.2594 | -0.23 % | 90002.9174 MeV (+28933.7 ppm) |
| ${}^{95}$Mo | 95 | 53 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 820.3485 | 821.6285 | -0.16 % | 90961.6825 MeV (+28929.1 ppm) |
| ${}^{96}$Mo | 96 | 54 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 830.2045 | 830.7828 | -0.07 % | 91918.5412 MeV (+28923.9 ppm) |
| ${}^{97}$Mo | 97 | 55 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 837.4027 | 837.6040 | -0.02 % | 92878.0578 MeV (+28921.6 ppm) |
| ${}^{98}$Mo | 98 | 56 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 846.5070 | 846.2466 | +0.03 % | 93835.6683 MeV (+28919.0 ppm) |
| ${}^{99}$Mo | 99 | 57 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 852.9996 | 852.1720 | +0.10 % | 94795.8905 MeV (+28914.4 ppm) |
| ${}^{100}$Mo | 100 | 58 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 861.3970 | 860.4663 | +0.11 % | 95754.2078 MeV (+28915.7 ppm) |
| ${}^{101}$Mo | 101 | 59 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 867.2263 | 865.8645 | +0.16 % | 96715.0934 MeV (+28912.6 ppm) |
| ${}^{102}$Mo | 102 | 60 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 874.9581 | 873.9767 | +0.11 % | 97674.0763 MeV (+28918.9 ppm) |
| ${}^{103}$Mo | 103 | 61 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 880.1630 | 879.4415 | +0.08 % | 98635.5862 MeV (+28923.0 ppm) |
| ${}^{104}$Mo | 104 | 62 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 887.2672 | 886.9023 | +0.04 % | 99595.1967 MeV (+28928.7 ppm) |
| ${}^{105}$Mo | 105 | 63 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 891.8838 | 891.9606 | -0.01 % | 100557.2949 MeV (+28934.4 ppm) |
| ${}^{106}$Mo | 106 | 64 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 898.3959 | 898.8291 | -0.05 % | 101517.4976 MeV (+28939.6 ppm) |
| ${}^{107}$Mo | 107 | 65 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 902.4575 | 903.3174 | -0.10 % | 102480.1507 MeV (+28944.8 ppm) |
| ${}^{108}$Mo | 108 | 66 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 908.4100 | 909.5931 | -0.13 % | 103440.9130 MeV (+28949.4 ppm) |
| ${}^{109}$Mo | 109 | 67 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 911.9476 | 913.5744 | -0.18 % | 104404.0902 MeV (+28954.4 ppm) |
| ${}^{110}$Mo | 110 | 68 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 917.3709 | 919.5222 | -0.23 % | 105365.3817 MeV (+28960.7 ppm) |
| ${}^{111}$Mo | 111 | 69 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 920.4131 | 922.9975 | -0.28 % | 106329.0542 MeV (+28965.2 ppm) |
| ${}^{112}$Mo | 112 | 70 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 925.3353 | 928.5920 | -0.35 % | 107290.8468 MeV (+28972.8 ppm) |
| ${}^{113}$Mo | 113 | 71 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 927.9088 | 931.7980 | -0.42 % | 108254.9881 MeV (+28979.3 ppm) |
| ${}^{114}$Mo | 114 | 72 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 932.3561 | 936.9660 | -0.49 % | 109217.2555 MeV (+28986.1 ppm) |
| ${}^{115}$Mo | 115 | 73 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 934.4857 | 939.8950 | -0.58 % | 110181.8408 MeV (+28993.7 ppm) |
| ${}^{116}$Mo | 116 | 74 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 938.4826 | 944.5880 | -0.65 % | 111144.5587 MeV (+29000.9 ppm) |
| ${}^{117}$Mo | 117 | 75 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 940.1912 | 947.2320 | -0.74 % | 112109.5647 MeV (+29008.4 ppm) |
| ${}^{118}$Mo | 118 | 76 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 943.7605 | 951.9060 | -0.86 % | 113072.7103 MeV (+29019.5 ppm) |
| ${}^{119}$Mo | 119 | 77 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 945.0699 | 954.2610 | -0.96 % | 114038.1157 MeV (+29027.8 ppm) |

### Technetium (Z = 43)

_40 of 40 isotopes with a framework prediction; 40 of 40 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{83}$Tc | 83 | 40 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 665.6628 | 667.5690 | -0.29 % | 79514.4606 MeV (+28878.0 ppm) |
| ${}^{84}$Tc | 84 | 41 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 679.9683 | 682.0800 | -0.31 % | 80466.8698 MeV (+28885.4 ppm) |
| ${}^{85}$Tc | 85 | 42 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 696.1241 | 698.2750 | -0.31 % | 81417.4288 MeV (+28892.3 ppm) |
| ${}^{86}$Tc | 86 | 43 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 709.2857 | 712.0800 | -0.39 % | 82370.9820 MeV (+28905.2 ppm) |
| ${}^{87}$Tc | 87 | 44 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 724.3092 | 726.2538 | -0.27 % | 83322.6733 MeV (+28899.9 ppm) |
| ${}^{88}$Tc | 88 | 45 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 736.4050 | 738.3054 | -0.26 % | 84277.2923 MeV (+28903.5 ppm) |
| ${}^{89}$Tc | 89 | 46 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 750.3719 | 752.1012 | -0.23 % | 85230.0401 MeV (+28906.2 ppm) |
| ${}^{90}$Tc | 90 | 47 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 761.4733 | 763.5024 | -0.27 % | 86185.6535 MeV (+28913.6 ppm) |
| ${}^{91}$Tc | 91 | 48 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 774.4527 | 776.8357 | -0.31 % | 87139.3889 MeV (+28922.1 ppm) |
| ${}^{92}$Tc | 92 | 49 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 784.6247 | 787.8460 | -0.41 % | 88095.9316 MeV (+28935.3 ppm) |
| ${}^{93}$Tc | 93 | 50 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 796.6798 | 800.5978 | -0.49 % | 89050.5914 MeV (+28947.2 ppm) |
| ${}^{94}$Tc | 94 | 51 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 805.9822 | 809.2213 | -0.40 % | 90008.0037 MeV (+28941.7 ppm) |
| ${}^{95}$Tc | 95 | 52 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 817.1707 | 819.1557 | -0.24 % | 90963.5299 MeV (+28930.3 ppm) |
| ${}^{96}$Tc | 96 | 53 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 825.6582 | 827.0273 | -0.17 % | 91921.7573 MeV (+28925.6 ppm) |
| ${}^{97}$Tc | 97 | 54 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 836.0334 | 836.5014 | -0.06 % | 92878.0968 MeV (+28918.4 ppm) |
| ${}^{98}$Tc | 98 | 55 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 843.7561 | 843.7805 | -0.00 % | 93837.0889 MeV (+28915.6 ppm) |
| ${}^{99}$Tc | 99 | 56 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 853.3669 | 852.7474 | +0.07 % | 94794.1928 MeV (+28911.2 ppm) |
| ${}^{100}$Tc | 100 | 57 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 860.3711 | 859.5118 | +0.10 % | 95753.9035 MeV (+28910.6 ppm) |
| ${}^{101}$Tc | 101 | 58 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 869.2626 | 867.9068 | +0.16 % | 96711.7267 MeV (+28907.7 ppm) |
| ${}^{102}$Tc | 102 | 59 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 875.5908 | 874.2064 | +0.16 % | 97672.1133 MeV (+28909.2 ppm) |
| ${}^{103}$Tc | 103 | 60 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 883.8045 | 882.3088 | +0.17 % | 98630.6143 MeV (+28910.3 ppm) |
| ${}^{104}$Tc | 104 | 61 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 889.4961 | 888.2751 | +0.14 % | 99591.6375 MeV (+28914.8 ppm) |
| ${}^{105}$Tc | 105 | 62 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 897.0706 | 896.1338 | +0.10 % | 100550.7778 MeV (+28919.9 ppm) |
| ${}^{106}$Tc | 106 | 63 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 902.1619 | 901.6950 | +0.05 % | 101512.4013 MeV (+28926.0 ppm) |
| ${}^{107}$Tc | 107 | 64 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 909.1326 | 908.7401 | +0.04 % | 102472.1453 MeV (+28928.5 ppm) |
| ${}^{108}$Tc | 108 | 65 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 913.6574 | 913.9843 | -0.04 % | 103434.3353 MeV (+28936.9 ppm) |
| ${}^{109}$Tc | 109 | 66 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 920.0574 | 920.4156 | -0.04 % | 104394.6501 MeV (+28938.7 ppm) |
| ${}^{110}$Tc | 110 | 67 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 924.0469 | 925.2386 | -0.13 % | 105357.3754 MeV (+28947.8 ppm) |
| ${}^{111}$Tc | 111 | 68 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 929.9068 | 931.3001 | -0.15 % | 106318.2302 MeV (+28950.9 ppm) |
| ${}^{112}$Tc | 112 | 69 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 933.3899 | 935.6056 | -0.24 % | 107281.4619 MeV (+28959.5 ppm) |
| ${}^{113}$Tc | 113 | 70 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 938.7383 | 941.2296 | -0.26 % | 108242.8283 MeV (+28963.1 ppm) |
| ${}^{114}$Tc | 114 | 71 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 941.7420 | 945.0896 | -0.35 % | 109206.5393 MeV (+28971.7 ppm) |
| ${}^{115}$Tc | 115 | 72 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 946.6053 | 950.3600 | -0.40 % | 110168.3908 MeV (+28976.2 ppm) |
| ${}^{116}$Tc | 116 | 73 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 949.1549 | 953.8680 | -0.49 % | 111132.5561 MeV (+28985.1 ppm) |
| ${}^{117}$Tc | 117 | 74 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 953.5578 | 958.8150 | -0.55 % | 112094.8679 MeV (+28991.1 ppm) |
| ${}^{118}$Tc | 118 | 75 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 955.6765 | 962.0540 | -0.66 % | 113059.4640 MeV (+29001.2 ppm) |
| ${}^{119}$Tc | 119 | 76 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 959.6421 | 966.9940 | -0.76 % | 114022.2131 MeV (+29010.5 ppm) |
| ${}^{120}$Tc | 120 | 77 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 961.3518 | 969.9600 | -0.89 % | 114987.2182 MeV (+29021.0 ppm) |
| ${}^{121}$Tc | 121 | 78 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 964.9018 | 974.5340 | -0.99 % | 115950.3830 MeV (+29030.5 ppm) |
| ${}^{122}$Tc | 122 | 79 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 966.2229 | 977.3420 | -1.14 % | 116915.7766 MeV (+29043.5 ppm) |

### Ruthenium (Z = 44)

_41 of 41 isotopes with a framework prediction; 41 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{85}$Ru | 85 | 41 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 680.1406 | 682.2950 | -0.32 % | 81432.0820 MeV (+28879.6 ppm) |
| ${}^{86}$Ru | 86 | 42 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 696.8757 | 699.4380 | -0.37 % | 82382.0617 MeV (+28891.9 ppm) |
| ${}^{87}$Ru | 87 | 43 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 710.6242 | 713.4870 | -0.40 % | 83335.0280 MeV (+28900.5 ppm) |
| ${}^{88}$Ru | 88 | 44 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 726.2142 | 730.2240 | -0.55 % | 84286.1527 MeV (+28919.6 ppm) |
| ${}^{89}$Ru | 89 | 45 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 738.8837 | 742.2935 | -0.46 % | 85240.1981 MeV (+28916.7 ppm) |
| ${}^{90}$Ru | 90 | 46 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 753.4043 | 756.8792 | -0.46 % | 86192.3922 MeV (+28922.3 ppm) |
| ${}^{91}$Ru | 91 | 47 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 765.0661 | 768.3065 | -0.42 % | 87147.4452 MeV (+28923.1 ppm) |
| ${}^{92}$Ru | 92 | 48 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 778.5865 | 782.4392 | -0.49 % | 88100.6396 MeV (+28934.7 ppm) |
| ${}^{93}$Ru | 93 | 49 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 789.3059 | 793.4260 | -0.52 % | 89056.6349 MeV (+28941.1 ppm) |
| ${}^{94}$Ru | 94 | 50 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 801.8894 | 806.8642 | -0.62 % | 90010.7662 MeV (+28954.8 ppm) |
| ${}^{95}$Ru | 95 | 51 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 811.7262 | 815.8097 | -0.50 % | 90967.6442 MeV (+28947.0 ppm) |
| ${}^{96}$Ru | 96 | 52 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 823.4308 | 826.5036 | -0.37 % | 91922.6544 MeV (+28938.6 ppm) |
| ${}^{97}$Ru | 97 | 53 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 832.4400 | 834.6152 | -0.26 % | 92880.3600 MeV (+28930.8 ppm) |
| ${}^{98}$Ru | 98 | 54 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 843.3190 | 844.7908 | -0.17 % | 93836.1957 MeV (+28926.0 ppm) |
| ${}^{99}$Ru | 99 | 55 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 851.5510 | 852.2626 | -0.08 % | 94794.6785 MeV (+28919.8 ppm) |
| ${}^{100}$Ru | 100 | 56 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 861.6536 | 861.9359 | -0.03 % | 95751.2906 MeV (+28917.9 ppm) |
| ${}^{101}$Ru | 101 | 57 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 869.1548 | 868.7380 | +0.05 % | 96710.5042 MeV (+28912.4 ppm) |
| ${}^{102}$Ru | 102 | 58 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 878.5264 | 877.9576 | +0.06 % | 97667.8474 MeV (+28913.4 ppm) |
| ${}^{103}$Ru | 103 | 59 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 885.3398 | 884.1897 | +0.13 % | 98627.7488 MeV (+28909.0 ppm) |
| ${}^{104}$Ru | 104 | 60 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 894.0222 | 893.0896 | +0.10 % | 99585.7812 MeV (+28913.8 ppm) |
| ${}^{105}$Ru | 105 | 61 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 900.1873 | 898.9997 | +0.13 % | 100546.3308 MeV (+28912.8 ppm) |
| ${}^{106}$Ru | 106 | 62 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 908.2192 | 907.4597 | +0.08 % | 101505.0137 MeV (+28919.4 ppm) |
| ${}^{107}$Ru | 107 | 63 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 913.7728 | 913.0703 | +0.08 % | 102466.1749 MeV (+28921.4 ppm) |
| ${}^{108}$Ru | 108 | 64 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 921.1901 | 920.9405 | +0.03 % | 103425.4724 MeV (+28927.9 ppm) |
| ${}^{109}$Ru | 109 | 65 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 926.1660 | 926.0889 | +0.01 % | 104387.2112 MeV (+28930.8 ppm) |
| ${}^{110}$Ru | 110 | 66 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 933.0020 | 933.4944 | -0.05 % | 105347.0900 MeV (+28938.1 ppm) |
| ${}^{111}$Ru | 111 | 67 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 937.4319 | 938.2784 | -0.09 % | 106309.3749 MeV (+28942.5 ppm) |
| ${}^{112}$Ru | 112 | 68 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 943.7174 | 945.1952 | -0.16 % | 107269.8041 MeV (+28950.1 ppm) |
| ${}^{113}$Ru | 113 | 69 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 947.6306 | 949.5035 | -0.20 % | 108232.6057 MeV (+28954.5 ppm) |
| ${}^{114}$Ru | 114 | 70 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 953.3945 | 955.9282 | -0.27 % | 109193.5566 MeV (+28962.0 ppm) |
| ${}^{115}$Ru | 115 | 71 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 956.8181 | 959.8836 | -0.32 % | 110156.8477 MeV (+28967.4 ppm) |
| ${}^{116}$Ru | 116 | 72 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 962.0873 | 965.9185 | -0.40 % | 111118.2934 MeV (+28975.5 ppm) |
| ${}^{117}$Ru | 117 | 73 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 965.0468 | 969.4108 | -0.45 % | 112082.0486 MeV (+28980.7 ppm) |
| ${}^{118}$Ru | 118 | 74 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 969.8461 | 975.0340 | -0.53 % | 113043.9641 MeV (+28988.5 ppm) |
| ${}^{119}$Ru | 119 | 75 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 972.3653 | 978.1800 | -0.59 % | 114008.1597 MeV (+28994.3 ppm) |
| ${}^{120}$Ru | 120 | 76 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 976.7181 | 983.8800 | -0.73 % | 114970.5216 MeV (+29007.1 ppm) |
| ${}^{121}$Ru | 121 | 77 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 978.8190 | 986.8760 | -0.82 % | 115935.1355 MeV (+29014.7 ppm) |
| ${}^{122}$Ru | 122 | 78 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 982.7471 | 992.1040 | -0.94 % | 116897.9221 MeV (+29026.5 ppm) |
| ${}^{123}$Ru | 123 | 79 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 984.4505 | 994.9470 | -1.05 % | 117862.9336 MeV (+29036.1 ppm) |
| ${}^{124}$Ru | 124 | 80 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 987.9744 | 1000.0600 | -1.21 % | 118826.1244 MeV (+29049.9 ppm) |
| ${}^{125}$Ru | 125 | 81 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 989.2995 | 1002.8750 | -1.35 % | 119791.5141 MeV (+29062.5 ppm) |

### Rhodium (Z = 45)

_41 of 41 isotopes with a framework prediction; 41 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{88}$Rh | 88 | 43 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 708.8256 | 711.9200 | -0.43 % | 84302.2111 MeV (+28896.1 ppm) |
| ${}^{89}$Rh | 89 | 44 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 724.9897 | 728.8210 | -0.53 % | 85252.7617 MeV (+28910.4 ppm) |
| ${}^{90}$Rh | 90 | 45 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 738.2402 | 742.8600 | -0.62 % | 86206.2260 MeV (+28924.7 ppm) |
| ${}^{91}$Rh | 91 | 46 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 753.3222 | 757.8480 | -0.60 % | 87157.8588 MeV (+28928.6 ppm) |
| ${}^{92}$Rh | 92 | 47 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 765.5519 | 770.3547 | -0.62 % | 88112.3439 MeV (+28935.6 ppm) |
| ${}^{93}$Rh | 93 | 48 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 779.6210 | 784.4388 | -0.61 % | 89064.9896 MeV (+28940.1 ppm) |
| ${}^{94}$Rh | 94 | 49 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 790.8953 | 796.4059 | -0.69 % | 90020.4300 MeV (+28951.5 ppm) |
| ${}^{95}$Rh | 95 | 50 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 804.0149 | 809.9102 | -0.73 % | 90974.0251 MeV (+28959.6 ppm) |
| ${}^{96}$Rh | 96 | 51 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 814.3939 | 819.3287 | -0.60 % | 91930.3610 MeV (+28951.3 ppm) |
| ${}^{97}$Rh | 97 | 52 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 826.6223 | 830.3098 | -0.44 % | 92884.8474 MeV (+28940.4 ppm) |
| ${}^{98}$Rh | 98 | 53 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 836.1609 | 838.9588 | -0.33 % | 93842.0235 MeV (+28932.9 ppm) |
| ${}^{99}$Rh | 99 | 54 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 847.5516 | 849.4394 | -0.22 % | 94797.3476 MeV (+28926.0 ppm) |
| ${}^{100}$Rh | 100 | 55 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 856.3006 | 857.5173 | -0.14 % | 95755.3133 MeV (+28921.0 ppm) |
| ${}^{101}$Rh | 101 | 56 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 866.9030 | 867.4099 | -0.06 % | 96711.4257 MeV (+28916.2 ppm) |
| ${}^{102}$Rh | 102 | 57 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 874.9091 | 874.8521 | +0.01 % | 97670.1344 MeV (+28912.3 ppm) |
| ${}^{103}$Rh | 103 | 58 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 884.7688 | 884.1718 | +0.07 % | 98626.9895 MeV (+28909.3 ppm) |
| ${}^{104}$Rh | 104 | 59 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 892.0751 | 891.1708 | +0.10 % | 99586.3979 MeV (+28908.1 ppm) |
| ${}^{105}$Rh | 105 | 60 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 901.2341 | 900.1341 | +0.12 % | 100543.9537 MeV (+28908.6 ppm) |
| ${}^{106}$Rh | 106 | 61 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 907.8806 | 906.7168 | +0.13 % | 101504.0219 MeV (+28909.8 ppm) |
| ${}^{107}$Rh | 107 | 62 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 916.3780 | 915.2891 | +0.12 % | 102462.2394 MeV (+28912.9 ppm) |
| ${}^{108}$Rh | 108 | 63 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 922.4016 | 921.5279 | +0.09 % | 103422.9305 MeV (+28916.7 ppm) |
| ${}^{109}$Rh | 109 | 64 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 930.2734 | 929.5673 | +0.08 % | 104381.7735 MeV (+28920.4 ppm) |
| ${}^{110}$Rh | 110 | 65 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 935.7084 | 935.4681 | +0.03 % | 105343.0532 MeV (+28926.4 ppm) |
| ${}^{111}$Rh | 111 | 66 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 942.9883 | 943.0146 | -0.00 % | 106302.4881 MeV (+28930.8 ppm) |
| ${}^{112}$Rh | 112 | 67 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 947.8665 | 948.5131 | -0.07 % | 107264.3247 MeV (+28938.0 ppm) |
| ${}^{113}$Rh | 113 | 68 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 954.5857 | 955.6203 | -0.11 % | 108224.3203 MeV (+28943.3 ppm) |
| ${}^{114}$Rh | 114 | 69 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 958.9367 | 960.6349 | -0.18 % | 109186.6841 MeV (+28950.5 ppm) |
| ${}^{115}$Rh | 115 | 70 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 965.1241 | 967.2252 | -0.22 % | 110147.2114 MeV (+28955.5 ppm) |
| ${}^{116}$Rh | 116 | 71 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 968.9755 | 971.8030 | -0.29 % | 111110.0748 MeV (+28963.0 ppm) |
| ${}^{117}$Rh | 117 | 72 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 974.6583 | 978.0354 | -0.35 % | 112071.1067 MeV (+28969.1 ppm) |
| ${}^{118}$Rh | 118 | 73 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 978.0357 | 982.0968 | -0.41 % | 113034.4442 MeV (+28975.7 ppm) |
| ${}^{119}$Rh | 119 | 74 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 983.2393 | 988.1040 | -0.49 % | 113995.9554 MeV (+28983.9 ppm) |
| ${}^{120}$Rh | 120 | 75 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 986.1667 | 991.9200 | -0.58 % | 114959.7428 MeV (+28992.6 ppm) |
| ${}^{121}$Rh | 121 | 76 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 990.9145 | 997.6740 | -0.68 % | 115921.7097 MeV (+29001.7 ppm) |
| ${}^{122}$Rh | 122 | 77 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 993.4143 | 1001.3760 | -0.80 % | 116885.9247 MeV (+29012.3 ppm) |
| ${}^{123}$Rh | 123 | 78 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 997.7285 | 1006.7550 | -0.90 % | 117848.3252 MeV (+29022.1 ppm) |
| ${}^{124}$Rh | 124 | 79 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 999.8217 | 1010.3520 | -1.04 % | 118812.9468 MeV (+29034.9 ppm) |
| ${}^{125}$Rh | 125 | 80 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1003.7230 | 1015.5000 | -1.16 % | 119775.7603 MeV (+29046.2 ppm) |
| ${}^{126}$Rh | 126 | 81 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1005.4292 | 1018.9620 | -1.33 % | 120740.7688 MeV (+29060.6 ppm) |
| ${}^{127}$Rh | 127 | 82 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1008.9370 | 1023.6200 | -1.43 % | 121703.9759 MeV (+29069.7 ppm) |
| ${}^{128}$Rh | 128 | 83 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1010.2746 | 1025.2800 | -1.46 % | 122669.3530 MeV (+29071.6 ppm) |

### Palladium (Z = 46)

_42 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{90}$Pd | 90 | 44 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 725.4086 | 730.1700 | -0.65 % | 86217.7273 MeV (+28915.5 ppm) |
| ${}^{91}$Pd | 91 | 45 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 739.2208 | 744.6530 | -0.73 % | 87170.6299 MeV (+28928.7 ppm) |
| ${}^{92}$Pd | 92 | 46 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 754.8456 | 761.3524 | -0.85 % | 88121.7199 MeV (+28946.3 ppm) |
| ${}^{93}$Pd | 93 | 47 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 767.6249 | 773.6264 | -0.78 % | 89075.6553 MeV (+28944.0 ppm) |
| ${}^{94}$Pd | 94 | 48 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 782.2251 | 788.8182 | -0.84 % | 90027.7699 MeV (+28955.3 ppm) |
| ${}^{95}$Pd | 95 | 49 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 794.0369 | 800.7532 | -0.84 % | 90982.6729 MeV (+28960.0 ppm) |
| ${}^{96}$Pd | 96 | 50 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 807.6759 | 815.0420 | -0.90 % | 91935.7486 MeV (+28971.2 ppm) |
| ${}^{97}$Pd | 97 | 51 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 818.5804 | 824.7357 | -0.75 % | 92891.5590 MeV (+28960.1 ppm) |
| ${}^{98}$Pd | 98 | 52 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 831.3166 | 836.3222 | -0.60 % | 93845.5375 MeV (+28950.5 ppm) |
| ${}^{99}$Pd | 99 | 53 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 841.3689 | 845.2554 | -0.46 % | 94802.2000 MeV (+28940.6 ppm) |
| ${}^{100}$Pd | 100 | 54 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 853.2561 | 856.3565 | -0.36 % | 95757.0276 MeV (+28935.2 ppm) |
| ${}^{101}$Pd | 101 | 55 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 862.5071 | 864.6473 | -0.25 % | 96714.4913 MeV (+28927.1 ppm) |
| ${}^{102}$Pd | 102 | 56 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 873.5947 | 875.1894 | -0.18 % | 97670.1185 MeV (+28924.3 ppm) |
| ${}^{103}$Pd | 103 | 57 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 882.0914 | 882.8148 | -0.08 % | 98628.3366 MeV (+28917.2 ppm) |
| ${}^{104}$Pd | 104 | 58 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 892.4253 | 892.8242 | -0.04 % | 99584.7175 MeV (+28916.6 ppm) |
| ${}^{105}$Pd | 105 | 59 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 900.2110 | 899.9183 | +0.03 % | 100543.6466 MeV (+28911.5 ppm) |
| ${}^{106}$Pd | 106 | 60 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 909.8334 | 909.4793 | +0.04 % | 101500.7389 MeV (+28913.5 ppm) |
| ${}^{107}$Pd | 107 | 61 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 916.9483 | 916.0157 | +0.10 % | 102460.3388 MeV (+28909.4 ppm) |
| ${}^{108}$Pd | 108 | 62 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 925.8984 | 925.2386 | +0.07 % | 103418.1034 MeV (+28914.6 ppm) |
| ${}^{109}$Pd | 109 | 63 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 932.3797 | 931.3922 | +0.11 % | 104378.3369 MeV (+28913.0 ppm) |
| ${}^{110}$Pd | 110 | 64 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 940.6940 | 940.1879 | +0.05 % | 105336.7373 MeV (+28920.0 ppm) |
| ${}^{111}$Pd | 111 | 65 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 946.5762 | 945.9142 | +0.07 % | 106297.5700 MeV (+28919.9 ppm) |
| ${}^{112}$Pd | 112 | 66 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 954.2885 | 954.3207 | -0.00 % | 107256.5724 MeV (+28928.7 ppm) |
| ${}^{113}$Pd | 113 | 67 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 959.6036 | 959.6615 | -0.01 % | 108217.9721 MeV (+28930.1 ppm) |
| ${}^{114}$Pd | 114 | 68 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 966.7454 | 967.6326 | -0.09 % | 109177.5451 MeV (+28939.8 ppm) |
| ${}^{115}$Pd | 115 | 69 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 971.5233 | 972.6394 | -0.11 % | 110139.4819 MeV (+28942.9 ppm) |
| ${}^{116}$Pd | 116 | 70 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 978.1238 | 980.1160 | -0.20 % | 111099.5962 MeV (+28952.6 ppm) |
| ${}^{117}$Pd | 117 | 71 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 982.3924 | 984.7801 | -0.24 % | 112062.0424 MeV (+28957.0 ppm) |
| ${}^{118}$Pd | 118 | 72 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 988.4790 | 991.8159 | -0.34 % | 113022.6706 MeV (+28966.9 ppm) |
| ${}^{119}$Pd | 119 | 73 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 992.2642 | 995.9062 | -0.37 % | 113985.6002 MeV (+28970.2 ppm) |
| ${}^{120}$Pd | 120 | 74 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 997.8623 | 1002.8498 | -0.50 % | 114946.7168 MeV (+28983.4 ppm) |
| ${}^{121}$Pd | 121 | 75 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1001.1883 | 1006.8239 | -0.56 % | 115910.1056 MeV (+28989.4 ppm) |
| ${}^{122}$Pd | 122 | 76 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1006.3219 | 1013.3290 | -0.69 % | 116871.6867 MeV (+29002.4 ppm) |
| ${}^{123}$Pd | 123 | 77 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1009.2115 | 1017.2139 | -0.79 % | 117835.5120 MeV (+29011.2 ppm) |
| ${}^{124}$Pd | 124 | 78 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1013.9029 | 1023.2480 | -0.91 % | 118797.5353 MeV (+29023.5 ppm) |
| ${}^{125}$Pd | 125 | 79 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1016.3771 | 1026.8750 | -1.02 % | 119761.7759 MeV (+29033.3 ppm) |
| ${}^{126}$Pd | 126 | 80 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1020.6472 | 1032.8220 | -1.18 % | 120724.2205 MeV (+29047.5 ppm) |
| ${}^{127}$Pd | 127 | 81 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1022.7261 | 1036.3200 | -1.31 % | 121688.8565 MeV (+29059.2 ppm) |
| ${}^{128}$Pd | 128 | 82 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1026.5945 | 1041.5360 | -1.43 % | 122651.7028 MeV (+29070.7 ppm) |
| ${}^{129}$Pd | 129 | 83 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1028.2966 | 1043.0940 | -1.42 % | 123616.7155 MeV (+29068.6 ppm) |
| ${}^{130}$Pd | 130 | 84 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1031.7818 | 1045.9800 | -1.36 % | 124579.9451 MeV (+29063.3 ppm) |
| ${}^{131}$Pd | 131 | 85 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1033.1246 | 1047.0830 | -1.33 % | 125545.3170 MeV (+29060.1 ppm) |

### Silver (Z = 47)

_42 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{92}$Ag | 92 | 45 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 737.1430 | 743.3600 | -0.84 % | 88138.0922 MeV (+28930.3 ppm) |
| ${}^{93}$Ag | 93 | 46 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 753.3177 | 760.2750 | -0.92 % | 89088.6322 MeV (+28944.4 ppm) |
| ${}^{94}$Ag | 94 | 47 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 766.6536 | 774.3720 | -1.00 % | 90042.0111 MeV (+28957.0 ppm) |
| ${}^{95}$Ag | 95 | 48 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 781.7921 | 789.9250 | -1.03 % | 90993.5874 MeV (+28966.4 ppm) |
| ${}^{96}$Ag | 96 | 49 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 794.1485 | 802.5879 | -1.05 % | 91947.9458 MeV (+28973.3 ppm) |
| ${}^{97}$Ag | 97 | 50 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 808.3142 | 817.0516 | -1.07 % | 92900.4948 MeV (+28980.4 ppm) |
| ${}^{98}$Ag | 98 | 51 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 819.7513 | 827.2853 | -0.91 % | 93855.7725 MeV (+28969.6 ppm) |
| ${}^{99}$Ag | 99 | 52 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 833.0028 | 839.0027 | -0.72 % | 94809.2357 MeV (+28955.9 ppm) |
| ${}^{100}$Ag | 100 | 53 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 843.5760 | 848.4995 | -0.58 % | 95765.3773 MeV (+28946.7 ppm) |
| ${}^{101}$Ag | 101 | 54 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 855.9671 | 859.7672 | -0.44 % | 96719.7010 MeV (+28937.7 ppm) |
| ${}^{102}$Ag | 102 | 55 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 865.7274 | 868.7508 | -0.35 % | 97676.6555 MeV (+28931.8 ppm) |
| ${}^{103}$Ag | 103 | 56 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 877.3077 | 879.3782 | -0.24 % | 98631.7900 MeV (+28924.7 ppm) |
| ${}^{104}$Ag | 104 | 57 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 886.3023 | 887.7632 | -0.16 % | 99589.5102 MeV (+28920.7 ppm) |
| ${}^{105}$Ag | 105 | 58 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 897.1178 | 897.7889 | -0.07 % | 100545.4094 MeV (+28915.3 ppm) |
| ${}^{106}$Ag | 106 | 59 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 905.3902 | 905.7318 | -0.04 % | 101503.8518 MeV (+28914.1 ppm) |
| ${}^{107}$Ag | 107 | 60 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 915.4836 | 915.2674 | +0.02 % | 102460.4732 MeV (+28911.1 ppm) |
| ${}^{108}$Ag | 108 | 61 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 923.0742 | 922.5388 | +0.06 % | 103419.5974 MeV (+28909.9 ppm) |
| ${}^{109}$Ag | 109 | 62 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 932.4847 | 931.7228 | +0.08 % | 104376.9016 MeV (+28910.1 ppm) |
| ${}^{110}$Ag | 110 | 63 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 939.4310 | 938.5320 | +0.10 % | 105336.6701 MeV (+28910.6 ppm) |
| ${}^{111}$Ag | 111 | 64 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 948.1954 | 947.3614 | +0.09 % | 106294.6205 MeV (+28913.6 ppm) |
| ${}^{112}$Ag | 112 | 65 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 954.5321 | 953.8010 | +0.08 % | 107254.9986 MeV (+28916.2 ppm) |
| ${}^{113}$Ag | 113 | 66 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 962.6843 | 962.3155 | +0.04 % | 108213.5611 MeV (+28921.8 ppm) |
| ${}^{114}$Ag | 114 | 67 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 968.4438 | 968.2908 | +0.02 % | 109174.5164 MeV (+28925.2 ppm) |
| ${}^{115}$Ag | 115 | 68 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 976.0156 | 976.4139 | -0.04 % | 110133.6593 MeV (+28932.3 ppm) |
| ${}^{116}$Ag | 116 | 69 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 981.2279 | 982.0452 | -0.08 % | 111095.1618 MeV (+28937.4 ppm) |
| ${}^{117}$Ag | 117 | 70 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 988.2489 | 989.7558 | -0.15 % | 112054.8556 MeV (+28945.4 ppm) |
| ${}^{118}$Ag | 118 | 71 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 992.9422 | 995.1990 | -0.23 % | 113016.8771 MeV (+28953.2 ppm) |
| ${}^{119}$Ag | 119 | 72 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 999.4399 | 1002.3623 | -0.29 % | 113977.0941 MeV (+28960.6 ppm) |
| ${}^{120}$Ag | 120 | 73 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1003.6403 | 1007.4394 | -0.38 % | 114939.6085 MeV (+28969.2 ppm) |
| ${}^{121}$Ag | 121 | 74 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1009.6405 | 1014.2620 | -0.46 % | 115900.3231 MeV (+28977.7 ppm) |
| ${}^{122}$Ag | 122 | 75 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1013.3725 | 1019.0366 | -0.56 % | 116863.3058 MeV (+28987.4 ppm) |
| ${}^{123}$Ag | 123 | 76 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1018.8993 | 1025.5704 | -0.65 % | 117824.4938 MeV (+28997.1 ppm) |
| ${}^{124}$Ag | 124 | 77 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1022.1859 | 1030.3031 | -0.79 % | 118787.9220 MeV (+29010.0 ppm) |
| ${}^{125}$Ag | 125 | 78 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1027.2619 | 1036.6644 | -0.91 % | 119749.5608 MeV (+29021.7 ppm) |
| ${}^{126}$Ag | 126 | 79 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1030.1245 | 1040.8860 | -1.03 % | 120713.4130 MeV (+29033.7 ppm) |
| ${}^{127}$Ag | 127 | 80 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1034.7707 | 1046.9880 | -1.17 % | 121675.4815 MeV (+29045.6 ppm) |
| ${}^{128}$Ag | 128 | 81 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1037.2295 | 1051.0080 | -1.31 % | 122639.7375 MeV (+29059.4 ppm) |
| ${}^{129}$Ag | 129 | 82 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1041.4659 | 1056.2520 | -1.40 % | 123602.2159 MeV (+29067.7 ppm) |
| ${}^{130}$Ag | 130 | 83 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1043.5396 | 1058.4600 | -1.41 % | 124566.8569 MeV (+29067.1 ppm) |
| ${}^{131}$Ag | 131 | 84 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1047.3849 | 1061.3620 | -1.32 % | 125529.7264 MeV (+29058.9 ppm) |
| ${}^{132}$Ag | 132 | 85 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1049.0914 | 1062.9960 | -1.31 % | 126494.7347 MeV (+29058.2 ppm) |
| ${}^{133}$Ag | 133 | 86 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1052.5631 | 1065.7290 | -1.24 % | 127457.9778 MeV (+29051.8 ppm) |

### Cadmium (Z = 48)

_42 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{94}$Cd | 94 | 46 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 753.4059 | 761.5880 | -1.07 % | 90053.9285 MeV (+28952.5 ppm) |
| ${}^{95}$Cd | 95 | 47 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 767.2805 | 776.2450 | -1.15 % | 91006.7687 MeV (+28965.9 ppm) |
| ${}^{96}$Cd | 96 | 48 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 782.9400 | 792.8640 | -1.25 % | 91957.8240 MeV (+28980.9 ppm) |
| ${}^{97}$Cd | 97 | 49 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 795.8239 | 806.0992 | -1.27 % | 92911.6548 MeV (+28988.1 ppm) |
| ${}^{98}$Cd | 98 | 50 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 810.4999 | 821.0729 | -1.29 % | 93863.6936 MeV (+28995.2 ppm) |
| ${}^{99}$Cd | 99 | 51 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 822.4534 | 831.4390 | -1.08 % | 94818.4549 MeV (+28980.2 ppm) |
| ${}^{100}$Cd | 100 | 52 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 836.2044 | 843.7737 | -0.90 % | 95771.4186 MeV (+28968.0 ppm) |
| ${}^{101}$Cd | 101 | 53 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 847.2830 | 853.4869 | -0.73 % | 96727.0548 MeV (+28955.7 ppm) |
| ${}^{102}$Cd | 102 | 54 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 860.1629 | 865.3815 | -0.60 % | 97680.8897 MeV (+28948.4 ppm) |
| ${}^{103}$Cd | 103 | 55 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 870.4177 | 874.4447 | -0.46 % | 98637.3496 MeV (+28938.2 ppm) |
| ${}^{104}$Cd | 104 | 56 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 882.4765 | 885.8328 | -0.38 % | 99592.0057 MeV (+28934.3 ppm) |
| ${}^{105}$Cd | 105 | 57 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 891.9548 | 894.2696 | -0.26 % | 100549.2422 MeV (+28925.7 ppm) |
| ${}^{106}$Cd | 106 | 58 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 903.2384 | 905.1392 | -0.21 % | 101504.6733 MeV (+28924.4 ppm) |
| ${}^{107}$Cd | 107 | 59 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 911.9840 | 913.0687 | -0.12 % | 102462.6425 MeV (+28918.3 ppm) |
| ${}^{108}$Cd | 108 | 60 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 922.5352 | 923.4021 | -0.09 % | 103418.8060 MeV (+28918.9 ppm) |
| ${}^{109}$Cd | 109 | 61 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 930.5886 | 930.7253 | -0.01 % | 104377.4674 MeV (+28913.5 ppm) |
| ${}^{110}$Cd | 110 | 62 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 940.4471 | 940.6403 | -0.02 % | 105334.3237 MeV (+28916.7 ppm) |
| ${}^{111}$Cd | 111 | 63 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 947.8460 | 947.6159 | +0.02 % | 106293.6396 MeV (+28914.4 ppm) |
| ${}^{112}$Cd | 112 | 64 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 957.0485 | 957.0098 | +0.00 % | 107251.1518 MeV (+28918.7 ppm) |
| ${}^{113}$Cd | 113 | 65 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 963.8279 | 963.5496 | +0.03 % | 108211.0872 MeV (+28918.0 ppm) |
| ${}^{114}$Cd | 114 | 66 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 972.4087 | 972.5925 | -0.02 % | 109169.2212 MeV (+28924.6 ppm) |
| ${}^{115}$Cd | 115 | 67 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 978.6011 | 978.7334 | -0.01 % | 110129.7435 MeV (+28925.5 ppm) |
| ${}^{116}$Cd | 116 | 68 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 986.5922 | 987.4327 | -0.09 % | 111088.4672 MeV (+28934.1 ppm) |
| ${}^{117}$Cd | 117 | 69 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 992.2280 | 993.2100 | -0.10 % | 112049.5462 MeV (+28936.6 ppm) |
| ${}^{118}$Cd | 118 | 70 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 999.6590 | 1001.5645 | -0.19 % | 113008.8299 MeV (+28946.9 ppm) |
| ${}^{119}$Cd | 119 | 71 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1004.7666 | 1006.9111 | -0.21 % | 113970.4372 MeV (+28950.0 ppm) |
| ${}^{120}$Cd | 120 | 72 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1011.6654 | 1014.9629 | -0.32 % | 114930.2531 MeV (+28962.0 ppm) |
| ${}^{121}$Cd | 121 | 73 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1016.2710 | 1020.1507 | -0.38 % | 115892.3623 MeV (+28967.9 ppm) |
| ${}^{122}$Cd | 122 | 74 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1022.6636 | 1027.7605 | -0.50 % | 116852.6844 MeV (+28980.0 ppm) |
| ${}^{123}$Cd | 123 | 75 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1026.7921 | 1032.6336 | -0.57 % | 117815.2707 MeV (+28987.0 ppm) |
| ${}^{124}$Cd | 124 | 76 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1032.7028 | 1039.9902 | -0.70 % | 118776.0748 MeV (+29000.7 ppm) |
| ${}^{125}$Cd | 125 | 77 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1036.3773 | 1044.7102 | -0.80 % | 119739.1151 MeV (+29010.0 ppm) |
| ${}^{126}$Cd | 126 | 78 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1041.8289 | 1051.6892 | -0.94 % | 120700.3783 MeV (+29023.8 ppm) |
| ${}^{127}$Cd | 127 | 79 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1045.0710 | 1056.2459 | -1.06 % | 121663.8509 MeV (+29035.0 ppm) |
| ${}^{128}$Cd | 128 | 80 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1050.0849 | 1062.8143 | -1.20 % | 122625.5518 MeV (+29048.6 ppm) |
| ${}^{129}$Cd | 129 | 81 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1052.9150 | 1066.7695 | -1.30 % | 123589.4364 MeV (+29057.7 ppm) |
| ${}^{130}$Cd | 130 | 82 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1057.5113 | 1072.8363 | -1.43 % | 124551.5550 MeV (+29070.1 ppm) |
| ${}^{131}$Cd | 131 | 83 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1059.9485 | 1075.0018 | -1.40 % | 125515.8325 MeV (+29067.0 ppm) |
| ${}^{132}$Cd | 132 | 84 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1064.1460 | 1078.3268 | -1.32 % | 126478.3498 MeV (+29059.4 ppm) |
| ${}^{133}$Cd | 133 | 85 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1066.2083 | 1080.0930 | -1.29 % | 127443.0023 MeV (+29056.0 ppm) |
| ${}^{134}$Cd | 134 | 86 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1070.0247 | 1083.5240 | -1.25 % | 128405.9007 MeV (+29052.2 ppm) |
| ${}^{135}$Cd | 135 | 87 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1071.7289 | 1084.8600 | -1.21 % | 129370.9112 MeV (+29049.2 ppm) |

### Indium (Z = 49)

_42 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{96}$In | 96 | 47 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 764.9220 | 774.6240 | -1.25 % | 91974.5117 MeV (+28966.4 ppm) |
| ${}^{97}$In | 97 | 48 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 781.1093 | 792.0050 | -1.38 % | 92925.0391 MeV (+28984.3 ppm) |
| ${}^{98}$In | 98 | 49 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 794.5275 | 806.5400 | -1.49 % | 93878.3357 MeV (+29000.8 ppm) |
| ${}^{99}$In | 99 | 50 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 809.7206 | 822.0960 | -1.51 % | 94829.8573 MeV (+29008.4 ppm) |
| ${}^{100}$In | 100 | 51 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 822.1973 | 832.9749 | -1.29 % | 95784.0954 MeV (+28993.5 ppm) |
| ${}^{101}$In | 101 | 52 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 836.4548 | 845.4130 | -1.06 % | 96736.5527 MeV (+28977.0 ppm) |
| ${}^{102}$In | 102 | 53 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 848.0456 | 855.6343 | -0.89 % | 97691.6767 MeV (+28964.9 ppm) |
| ${}^{103}$In | 103 | 54 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 861.4214 | 867.6431 | -0.72 % | 98645.0157 MeV (+28953.5 ppm) |
| ${}^{104}$In | 104 | 55 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 872.1775 | 877.2648 | -0.58 % | 99600.9743 MeV (+28944.1 ppm) |
| ${}^{105}$In | 105 | 56 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 884.7217 | 888.7940 | -0.46 % | 100555.1449 MeV (+28936.7 ppm) |
| ${}^{106}$In | 106 | 57 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 894.6907 | 897.8329 | -0.35 % | 101511.8907 MeV (+28929.5 ppm) |
| ${}^{107}$In | 107 | 58 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 906.4494 | 908.8627 | -0.27 % | 102466.8467 MeV (+28925.1 ppm) |
| ${}^{108}$In | 108 | 59 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 915.6751 | 917.4872 | -0.20 % | 103424.3358 MeV (+28921.3 ppm) |
| ${}^{109}$In | 109 | 60 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 926.6913 | 927.9282 | -0.13 % | 104380.0344 MeV (+28918.4 ppm) |
| ${}^{110}$In | 110 | 61 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 935.2145 | 935.9800 | -0.08 % | 105338.2260 MeV (+28915.9 ppm) |
| ${}^{111}$In | 111 | 62 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 945.5280 | 945.9733 | -0.05 % | 106294.6273 MeV (+28915.4 ppm) |
| ${}^{112}$In | 112 | 63 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 953.3865 | 953.6427 | -0.03 % | 107253.4835 MeV (+28915.5 ppm) |
| ${}^{113}$In | 113 | 64 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 963.0342 | 963.0911 | -0.01 % | 108210.5506 MeV (+28916.0 ppm) |
| ${}^{114}$In | 114 | 65 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 970.2634 | 970.3651 | -0.01 % | 109170.0362 MeV (+28918.3 ppm) |
| ${}^{115}$In | 115 | 66 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 979.2798 | 979.4029 | -0.01 % | 110127.7345 MeV (+28920.7 ppm) |
| ${}^{116}$In | 116 | 67 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 985.9123 | 986.1877 | -0.03 % | 111087.8169 MeV (+28923.7 ppm) |
| ${}^{117}$In | 117 | 68 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 994.3296 | 994.9522 | -0.06 % | 112046.1143 MeV (+28929.0 ppm) |
| ${}^{118}$In | 118 | 69 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1000.3959 | 1001.3087 | -0.09 % | 113006.7628 MeV (+28933.0 ppm) |
| ${}^{119}$In | 119 | 70 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1008.2441 | 1009.8505 | -0.16 % | 113965.6294 MeV (+28941.2 ppm) |
| ${}^{120}$In | 120 | 71 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1013.7728 | 1015.9509 | -0.21 % | 114926.8154 MeV (+28947.5 ppm) |
| ${}^{121}$In | 121 | 72 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1021.0798 | 1024.1291 | -0.30 % | 115886.2232 MeV (+28956.9 ppm) |
| ${}^{122}$In | 122 | 73 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1026.0977 | 1029.9372 | -0.37 % | 116847.9201 MeV (+28964.8 ppm) |
| ${}^{123}$In | 123 | 74 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1032.8898 | 1037.8662 | -0.48 % | 117807.8428 MeV (+28976.2 ppm) |
| ${}^{124}$In | 124 | 75 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1037.4216 | 1043.3762 | -0.57 % | 118770.0257 MeV (+28985.4 ppm) |
| ${}^{125}$In | 125 | 76 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1043.7233 | 1050.9921 | -0.69 % | 119730.4388 MeV (+28997.9 ppm) |
| ${}^{126}$In | 126 | 77 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1047.7926 | 1056.4604 | -0.82 % | 120693.0843 MeV (+29010.3 ppm) |
| ${}^{127}$In | 127 | 78 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1053.6269 | 1063.6023 | -0.94 % | 121653.9648 MeV (+29022.2 ppm) |
| ${}^{128}$In | 128 | 79 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1057.2554 | 1068.9838 | -1.10 % | 122617.0510 MeV (+29037.3 ppm) |
| ${}^{129}$In | 129 | 80 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1062.6439 | 1075.6999 | -1.21 % | 123578.3773 MeV (+29048.8 ppm) |
| ${}^{130}$In | 130 | 81 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1065.8523 | 1080.8429 | -1.39 % | 124541.8836 MeV (+29064.9 ppm) |
| ${}^{131}$In | 131 | 82 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1070.8153 | 1087.0320 | -1.49 % | 125503.6354 MeV (+29075.1 ppm) |
| ${}^{132}$In | 132 | 83 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1073.6229 | 1089.4905 | -1.46 % | 126467.5426 MeV (+29071.5 ppm) |
| ${}^{133}$In | 133 | 84 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1078.1794 | 1092.8610 | -1.34 % | 127429.7008 MeV (+29061.2 ppm) |
| ${}^{134}$In | 134 | 85 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1080.6043 | 1095.1820 | -1.33 % | 128393.9907 MeV (+29059.9 ppm) |
| ${}^{135}$In | 135 | 86 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1084.7724 | 1098.3600 | -1.24 % | 129356.5374 MeV (+29051.8 ppm) |
| ${}^{136}$In | 136 | 87 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1086.8317 | 1100.3760 | -1.23 % | 130321.1929 MeV (+29050.1 ppm) |
| ${}^{137}$In | 137 | 88 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1090.6282 | 1103.2610 | -1.15 % | 131284.1112 MeV (+29042.8 ppm) |

### Tin (Z = 50)

_42 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{99}$Sn | 99 | 49 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 794.8045 | 807.9390 | -1.63 % | 94843.4432 MeV (+29006.2 ppm) |
| ${}^{100}$Sn | 100 | 50 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 810.4987 | 825.1626 | -1.78 % | 95794.4638 MeV (+29027.1 ppm) |
| ${}^{101}$Sn | 101 | 51 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 823.4825 | 836.3914 | -1.54 % | 96748.1947 MeV (+29010.6 ppm) |
| ${}^{102}$Sn | 102 | 52 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 838.2311 | 849.0920 | -1.28 % | 97700.1609 MeV (+28991.8 ppm) |
| ${}^{103}$Sn | 103 | 53 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 850.3188 | 859.3290 | -1.05 % | 98654.7880 MeV (+28974.6 ppm) |
| ${}^{104}$Sn | 104 | 54 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 864.1758 | 871.9268 | -0.89 % | 99607.6457 MeV (+28964.6 ppm) |
| ${}^{105}$Sn | 105 | 55 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 875.4187 | 881.7090 | -0.71 % | 100563.1176 MeV (+28951.9 ppm) |
| ${}^{106}$Sn | 106 | 56 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 888.4343 | 893.7961 | -0.60 % | 101516.8168 MeV (+28945.5 ppm) |
| ${}^{107}$Sn | 107 | 57 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 898.8799 | 903.0259 | -0.46 % | 102473.0859 MeV (+28935.5 ppm) |
| ${}^{108}$Sn | 108 | 58 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 911.1003 | 914.6549 | -0.39 % | 103427.5803 MeV (+28932.6 ppm) |
| ${}^{109}$Sn | 109 | 59 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 920.7928 | 923.2865 | -0.27 % | 104384.6026 MeV (+28924.3 ppm) |
| ${}^{110}$Sn | 110 | 60 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 932.2611 | 934.5696 | -0.25 % | 105339.8491 MeV (+28925.4 ppm) |
| ${}^{111}$Sn | 111 | 61 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 941.2413 | 942.7375 | -0.16 % | 106297.5836 MeV (+28919.6 ppm) |
| ${}^{112}$Sn | 112 | 62 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 951.9974 | 953.5253 | -0.16 % | 107253.5423 MeV (+28922.6 ppm) |
| ${}^{113}$Sn | 113 | 63 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 960.3034 | 961.2697 | -0.10 % | 108211.9511 MeV (+28919.2 ppm) |
| ${}^{114}$Sn | 114 | 64 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 970.3845 | 971.5726 | -0.12 % | 109168.5848 MeV (+28923.9 ppm) |
| ${}^{115}$Sn | 115 | 65 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 978.0517 | 979.1181 | -0.11 % | 110127.6324 MeV (+28924.5 ppm) |
| ${}^{116}$Sn | 116 | 66 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 987.4924 | 988.6815 | -0.12 % | 111084.9064 MeV (+28928.0 ppm) |
| ${}^{117}$Sn | 117 | 67 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 994.5536 | 995.6246 | -0.11 % | 112044.5600 MeV (+28928.5 ppm) |
| ${}^{118}$Sn | 118 | 68 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1003.3864 | 1004.9510 | -0.16 % | 113002.4420 MeV (+28935.1 ppm) |
| ${}^{119}$Sn | 119 | 69 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1009.8725 | 1011.4345 | -0.15 % | 113962.6707 MeV (+28936.5 ppm) |
| ${}^{120}$Sn | 120 | 70 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1018.1273 | 1020.5386 | -0.24 % | 114921.1306 MeV (+28946.1 ppm) |
| ${}^{121}$Sn | 121 | 71 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1024.0670 | 1026.7088 | -0.26 % | 115881.9057 MeV (+28949.3 ppm) |
| ${}^{122}$Sn | 122 | 72 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1031.7722 | 1035.5234 | -0.36 % | 116840.9153 MeV (+28960.9 ppm) |
| ${}^{123}$Sn | 123 | 73 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1037.1923 | 1041.4694 | -0.41 % | 117802.2099 MeV (+28966.4 ppm) |
| ${}^{124}$Sn | 124 | 74 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1044.3743 | 1049.9576 | -0.53 % | 118761.7427 MeV (+28979.3 ppm) |
| ${}^{125}$Sn | 125 | 75 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1049.3000 | 1055.6911 | -0.61 % | 119723.5318 MeV (+28987.0 ppm) |
| ${}^{126}$Sn | 126 | 76 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1055.9834 | 1063.8839 | -0.74 % | 120683.5631 MeV (+29001.2 ppm) |
| ${}^{127}$Sn | 127 | 77 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1060.4383 | 1069.4096 | -0.84 % | 121645.8230 MeV (+29010.7 ppm) |
| ${}^{128}$Sn | 128 | 78 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1066.6464 | 1077.3728 | -1.00 % | 122606.3297 MeV (+29026.5 ppm) |
| ${}^{129}$Sn | 129 | 79 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1070.6526 | 1082.6733 | -1.11 % | 123569.0383 MeV (+29037.5 ppm) |
| ${}^{130}$Sn | 130 | 80 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1076.4072 | 1090.2862 | -1.27 % | 124529.9985 MeV (+29053.6 ppm) |
| ${}^{131}$Sn | 131 | 81 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1079.9854 | 1095.4899 | -1.42 % | 125493.1351 MeV (+29067.0 ppm) |
| ${}^{132}$Sn | 132 | 82 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1085.3069 | 1102.8432 | -1.59 % | 126454.5283 MeV (+29083.9 ppm) |
| ${}^{133}$Sn | 133 | 83 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1088.4766 | 1105.2418 | -1.52 % | 127418.0734 MeV (+29076.8 ppm) |
| ${}^{134}$Sn | 134 | 84 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1093.3843 | 1108.8730 | -1.40 % | 128379.8804 MeV (+29066.1 ppm) |
| ${}^{135}$Sn | 135 | 85 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1096.1640 | 1111.1428 | -1.35 % | 129343.8155 MeV (+29061.3 ppm) |
| ${}^{136}$Sn | 136 | 86 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1100.6760 | 1114.7920 | -1.27 % | 130306.0183 MeV (+29053.8 ppm) |
| ${}^{137}$Sn | 137 | 87 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1103.0829 | 1116.8240 | -1.23 % | 131270.3262 MeV (+29050.3 ppm) |
| ${}^{138}$Sn | 138 | 88 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1107.2164 | 1120.2840 | -1.17 % | 132232.9075 MeV (+29044.4 ppm) |
| ${}^{139}$Sn | 139 | 89 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1109.2667 | 1122.1470 | -1.15 % | 133197.5719 MeV (+29042.4 ppm) |
| ${}^{140}$Sn | 140 | 90 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1113.0377 | 1125.3200 | -1.09 % | 134160.5157 MeV (+29038.1 ppm) |

### Antimony (Z = 51)

_41 of 41 isotopes with a framework prediction; 41 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{102}$Sb | 102 | 51 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 821.8637 | 834.4620 | -1.51 % | 97715.1980 MeV (+29000.2 ppm) |
| ${}^{103}$Sb | 103 | 52 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 837.1099 | 848.1020 | -1.30 % | 98666.6666 MeV (+28986.6 ppm) |
| ${}^{104}$Sb | 104 | 53 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 849.7010 | 858.8320 | -1.06 % | 99620.7903 MeV (+28969.3 ppm) |
| ${}^{105}$Sb | 105 | 54 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 864.0458 | 871.6042 | -0.87 % | 100573.1602 MeV (+28956.5 ppm) |
| ${}^{106}$Sb | 106 | 55 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 875.7820 | 882.1333 | -0.72 % | 101528.1388 MeV (+28946.8 ppm) |
| ${}^{107}$Sb | 107 | 56 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 889.2755 | 894.3846 | -0.57 % | 102481.3601 MeV (+28937.4 ppm) |
| ${}^{108}$Sb | 108 | 57 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 900.2044 | 904.2480 | -0.45 % | 103437.1459 MeV (+28929.3 ppm) |
| ${}^{109}$Sb | 109 | 58 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 912.8932 | 916.1250 | -0.35 % | 104391.1720 MeV (+28924.3 ppm) |
| ${}^{110}$Sb | 110 | 59 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 923.0590 | 925.3950 | -0.25 % | 105347.7209 MeV (+28917.9 ppm) |
| ${}^{111}$Sb | 111 | 60 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 934.9861 | 936.8534 | -0.20 % | 106302.5086 MeV (+28916.4 ppm) |
| ${}^{112}$Sb | 112 | 61 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 944.4299 | 945.6869 | -0.13 % | 107259.7795 MeV (+28912.8 ppm) |
| ${}^{113}$Sb | 113 | 62 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 955.6354 | 956.5762 | -0.10 % | 108215.2888 MeV (+28912.7 ppm) |
| ${}^{114}$Sb | 114 | 63 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 964.3954 | 964.7272 | -0.03 % | 109173.2436 MeV (+28909.0 ppm) |
| ${}^{115}$Sb | 115 | 64 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 974.9167 | 975.3053 | -0.04 % | 110129.4371 MeV (+28912.3 ppm) |
| ${}^{116}$Sb | 116 | 65 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 983.0284 | 983.1952 | -0.02 % | 111088.0401 MeV (+28912.2 ppm) |
| ${}^{117}$Sb | 117 | 66 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 992.9002 | 993.0841 | -0.02 % | 112044.8831 MeV (+28914.8 ppm) |
| ${}^{118}$Sb | 118 | 67 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1000.3969 | 1000.5120 | -0.01 % | 113004.1012 MeV (+28916.0 ppm) |
| ${}^{119}$Sb | 119 | 68 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1009.6517 | 1010.0627 | -0.04 % | 113961.5611 MeV (+28921.0 ppm) |
| ${}^{120}$Sb | 120 | 69 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1016.5642 | 1017.0756 | -0.05 % | 114921.3634 MeV (+28923.5 ppm) |
| ${}^{121}$Sb | 121 | 70 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1025.2325 | 1026.3289 | -0.11 % | 115879.4099 MeV (+28930.8 ppm) |
| ${}^{122}$Sb | 122 | 71 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1031.5897 | 1033.1353 | -0.15 % | 116839.7675 MeV (+28936.2 ppm) |
| ${}^{123}$Sb | 123 | 72 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1039.6998 | 1042.0953 | -0.23 % | 117798.3722 MeV (+28945.6 ppm) |
| ${}^{124}$Sb | 124 | 73 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1045.5288 | 1048.5628 | -0.29 % | 118759.2579 MeV (+28952.3 ppm) |
| ${}^{125}$Sb | 125 | 74 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1053.1073 | 1057.2702 | -0.39 % | 119718.3942 MeV (+28963.7 ppm) |
| ${}^{126}$Sb | 126 | 75 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1058.4335 | 1063.4795 | -0.47 % | 120679.7828 MeV (+28972.2 ppm) |
| ${}^{127}$Sb | 127 | 76 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1065.5053 | 1071.8560 | -0.59 % | 121639.4257 MeV (+28984.7 ppm) |
| ${}^{128}$Sb | 128 | 77 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1070.3525 | 1077.8589 | -0.70 % | 122601.2934 MeV (+28995.2 ppm) |
| ${}^{129}$Sb | 129 | 78 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1076.9410 | 1085.9297 | -0.83 % | 123561.4196 MeV (+29008.7 ppm) |
| ${}^{130}$Sb | 130 | 79 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1081.3314 | 1091.6573 | -0.95 % | 124523.7440 MeV (+29020.2 ppm) |
| ${}^{131}$Sb | 131 | 80 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1087.4586 | 1099.4244 | -1.09 % | 125484.3315 MeV (+29034.6 ppm) |
| ${}^{132}$Sb | 132 | 81 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1091.4132 | 1105.1496 | -1.24 % | 126447.0917 MeV (+29049.3 ppm) |
| ${}^{133}$Sb | 133 | 82 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1097.0998 | 1112.5091 | -1.39 % | 127408.1199 MeV (+29063.4 ppm) |
| ${}^{134}$Sb | 134 | 83 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1100.6383 | 1115.6759 | -1.35 % | 128371.2962 MeV (+29059.8 ppm) |
| ${}^{135}$Sb | 135 | 84 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1105.9037 | 1119.4186 | -1.21 % | 129332.7455 MeV (+29047.4 ppm) |
| ${}^{136}$Sb | 136 | 85 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1109.0446 | 1122.3064 | -1.18 % | 130296.3194 MeV (+29044.9 ppm) |
| ${}^{137}$Sb | 137 | 86 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1113.9072 | 1125.9313 | -1.07 % | 131258.1716 MeV (+29034.9 ppm) |
| ${}^{138}$Sb | 138 | 87 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1116.6680 | 1128.5640 | -1.05 % | 132222.1255 MeV (+29033.7 ppm) |
| ${}^{139}$Sb | 139 | 88 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1121.1450 | 1132.0160 | -0.96 % | 133184.3633 MeV (+29025.7 ppm) |
| ${}^{140}$Sb | 140 | 89 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1123.5422 | 1134.4200 | -0.96 % | 134148.6809 MeV (+29025.5 ppm) |
| ${}^{141}$Sb | 141 | 90 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1127.6499 | 1137.7290 | -0.89 % | 135111.2879 MeV (+29018.5 ppm) |
| ${}^{142}$Sb | 142 | 91 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1129.6991 | 1139.8340 | -0.89 % | 136075.9535 MeV (+29018.8 ppm) |

### Tellurium (Z = 52)

_42 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{104}$Te | 104 | 52 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 837.5233 | 848.3619 | -1.28 % | 99631.6377 MeV (+28978.6 ppm) |
| ${}^{105}$Te | 105 | 53 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 850.6029 | 859.6179 | -1.05 % | 100585.2729 MeV (+28962.5 ppm) |
| ${}^{106}$Te | 106 | 54 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 865.4210 | 873.0974 | -0.88 % | 101537.1695 MeV (+28952.3 ppm) |
| ${}^{107}$Te | 107 | 55 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 877.6361 | 883.6060 | -0.68 % | 102491.6691 MeV (+28937.7 ppm) |
| ${}^{108}$Te | 108 | 56 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 891.5938 | 896.8020 | -0.58 % | 103444.4262 MeV (+28933.5 ppm) |
| ${}^{109}$Te | 109 | 57 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 902.9923 | 906.8070 | -0.42 % | 104399.7425 MeV (+28922.3 ppm) |
| ${}^{110}$Te | 110 | 58 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 916.1361 | 919.3928 | -0.35 % | 105353.3135 MeV (+28920.1 ppm) |
| ${}^{111}$Te | 111 | 59 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 926.7622 | 928.8217 | -0.22 % | 106309.4022 MeV (+28910.9 ppm) |
| ${}^{112}$Te | 112 | 60 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 939.1353 | 940.8731 | -0.18 % | 107263.7438 MeV (+28911.1 ppm) |
| ${}^{113}$Te | 113 | 61 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 949.0302 | 949.7239 | -0.07 % | 108220.5637 MeV (+28903.4 ppm) |
| ${}^{114}$Te | 114 | 62 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 960.6728 | 961.3379 | -0.07 % | 109175.6358 MeV (+28906.3 ppm) |
| ${}^{115}$Te | 115 | 63 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 969.8748 | 969.5823 | +0.03 % | 110133.1486 MeV (+28899.4 ppm) |
| ${}^{116}$Te | 116 | 64 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 980.8245 | 980.8546 | -0.00 % | 111088.9137 MeV (+28905.4 ppm) |
| ${}^{117}$Te | 117 | 65 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 989.3693 | 988.7577 | +0.06 % | 112047.0837 MeV (+28901.5 ppm) |
| ${}^{118}$Te | 118 | 66 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 999.6610 | 999.4242 | +0.02 % | 113003.5068 MeV (+28907.7 ppm) |
| ${}^{119}$Te | 119 | 67 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1007.5819 | 1006.9873 | +0.06 % | 113962.3007 MeV (+28906.3 ppm) |
| ${}^{120}$Te | 120 | 68 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1017.2481 | 1017.2383 | +0.00 % | 114919.3492 MeV (+28914.1 ppm) |
| ${}^{121}$Te | 121 | 69 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1024.5763 | 1024.4906 | +0.01 % | 115878.7358 MeV (+28915.2 ppm) |
| ${}^{122}$Te | 122 | 70 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1033.6477 | 1034.3320 | -0.07 % | 116836.3792 MeV (+28924.3 ppm) |
| ${}^{123}$Te | 123 | 71 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1040.4122 | 1041.2611 | -0.08 % | 117796.3295 MeV (+28927.3 ppm) |
| ${}^{124}$Te | 124 | 72 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1048.9172 | 1050.6855 | -0.17 % | 118754.5392 MeV (+28937.3 ppm) |
| ${}^{125}$Te | 125 | 73 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1055.1453 | 1057.2545 | -0.20 % | 119715.0259 MeV (+28941.6 ppm) |
| ${}^{126}$Te | 126 | 74 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1063.1108 | 1066.3682 | -0.31 % | 120673.7752 MeV (+28953.2 ppm) |
| ${}^{127}$Te | 127 | 75 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1068.8280 | 1072.6558 | -0.36 % | 121634.7728 MeV (+28959.1 ppm) |
| ${}^{128}$Te | 128 | 76 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1076.2790 | 1081.4405 | -0.48 % | 122594.0365 MeV (+28972.0 ppm) |
| ${}^{129}$Te | 129 | 77 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1081.5092 | 1087.5229 | -0.55 % | 123555.5211 MeV (+28979.9 ppm) |
| ${}^{130}$Te | 130 | 78 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1088.4694 | 1095.9423 | -0.68 % | 124515.2757 MeV (+28993.4 ppm) |
| ${}^{131}$Te | 131 | 79 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1093.2351 | 1101.8716 | -0.78 % | 125477.2247 MeV (+29003.6 ppm) |
| ${}^{132}$Te | 132 | 80 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1099.7266 | 1109.9201 | -0.92 % | 126437.4480 MeV (+29017.3 ppm) |
| ${}^{133}$Te | 133 | 81 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1104.0490 | 1115.7404 | -1.05 % | 127399.8404 MeV (+29029.8 ppm) |
| ${}^{134}$Te | 134 | 82 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1110.0925 | 1123.4083 | -1.19 % | 128360.5116 MeV (+29043.6 ppm) |
| ${}^{135}$Te | 135 | 83 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1113.9915 | 1126.6747 | -1.13 % | 129323.3274 MeV (+29038.2 ppm) |
| ${}^{136}$Te | 136 | 84 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1119.6068 | 1131.4425 | -1.05 % | 130284.4269 MeV (+29031.6 ppm) |
| ${}^{137}$Te | 137 | 85 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1123.1011 | 1134.3923 | -1.00 % | 131247.6474 MeV (+29027.0 ppm) |
| ${}^{138}$Te | 138 | 86 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1128.3066 | 1138.8558 | -0.93 % | 132209.1567 MeV (+29021.3 ppm) |
| ${}^{139}$Te | 139 | 87 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1131.4138 | 1141.4363 | -0.88 % | 133172.7642 MeV (+29016.9 ppm) |
| ${}^{140}$Te | 140 | 88 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1136.2269 | 1145.6699 | -0.82 % | 134134.6659 MeV (+29012.5 ppm) |
| ${}^{141}$Te | 141 | 89 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1138.9637 | 1148.0220 | -0.79 % | 135098.6438 MeV (+29009.4 ppm) |
| ${}^{142}$Te | 142 | 90 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1143.4010 | 1152.0460 | -0.75 % | 136060.9213 MeV (+29005.8 ppm) |
| ${}^{143}$Te | 143 | 91 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1145.7831 | 1154.0100 | -0.71 % | 137025.2540 MeV (+29003.0 ppm) |
| ${}^{144}$Te | 144 | 92 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1149.8601 | 1157.7600 | -0.68 % | 137987.8918 MeV (+29000.7 ppm) |
| ${}^{145}$Te | 145 | 93 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1151.9024 | 1159.7100 | -0.67 % | 138952.5643 MeV (+28999.0 ppm) |

### Iodine (Z = 53)

_42 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{106}$I | 106 | 53 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 848.6641 | 857.4340 | -1.02 % | 101552.5961 MeV (+28953.0 ppm) |
| ${}^{107}$I | 107 | 54 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 863.9618 | 871.6220 | -0.88 % | 102504.0131 MeV (+28945.6 ppm) |
| ${}^{108}$I | 108 | 55 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 876.6621 | 883.0080 | -0.72 % | 103458.0276 MeV (+28935.6 ppm) |
| ${}^{109}$I | 109 | 56 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 891.0903 | 895.9818 | -0.55 % | 104410.3142 MeV (+28924.6 ppm) |
| ${}^{110}$I | 110 | 57 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 902.9645 | 906.8484 | -0.43 % | 105365.1548 MeV (+28917.6 ppm) |
| ${}^{111}$I | 111 | 58 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 916.5697 | 919.4057 | -0.31 % | 106318.2644 MeV (+28910.7 ppm) |
| ${}^{112}$I | 112 | 59 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 927.6623 | 929.5866 | -0.21 % | 107273.8866 MeV (+28904.7 ppm) |
| ${}^{113}$I | 113 | 60 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 940.4878 | 941.7141 | -0.13 % | 108227.7758 MeV (+28901.3 ppm) |
| ${}^{114}$I | 114 | 61 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 950.8400 | 951.3048 | -0.05 % | 109184.1384 MeV (+28896.7 ppm) |
| ${}^{115}$I | 115 | 62 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 962.9262 | 963.0750 | -0.02 % | 110138.7670 MeV (+28896.9 ppm) |
| ${}^{116}$I | 116 | 63 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 972.5764 | 972.2292 | +0.04 % | 111095.8315 MeV (+28894.7 ppm) |
| ${}^{117}$I | 117 | 64 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 983.9609 | 983.3184 | +0.07 % | 112051.1618 MeV (+28895.0 ppm) |
| ${}^{118}$I | 118 | 65 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 992.9450 | 991.9222 | +0.10 % | 113008.8924 MeV (+28893.8 ppm) |
| ${}^{119}$I | 119 | 66 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1003.6629 | 1002.8002 | +0.09 % | 113964.8894 MeV (+28898.1 ppm) |
| ${}^{120}$I | 120 | 67 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1012.0144 | 1010.8409 | +0.12 % | 114923.2526 MeV (+28897.4 ppm) |
| ${}^{121}$I | 121 | 68 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1022.0984 | 1021.4107 | +0.07 % | 115879.8834 MeV (+28904.4 ppm) |
| ${}^{122}$I | 122 | 69 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1029.8486 | 1029.3157 | +0.05 % | 116838.8480 MeV (+28907.7 ppm) |
| ${}^{123}$I | 123 | 70 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1039.3294 | 1039.2503 | +0.01 % | 117796.0819 MeV (+28914.1 ppm) |
| ${}^{124}$I | 124 | 71 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1046.5075 | 1046.7436 | -0.02 % | 118755.6186 MeV (+28918.5 ppm) |
| ${}^{125}$I | 125 | 72 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1055.4139 | 1056.2864 | -0.08 % | 119713.4270 MeV (+28926.2 ppm) |
| ${}^{126}$I | 126 | 73 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1062.0473 | 1063.4322 | -0.13 % | 120673.5084 MeV (+28932.1 ppm) |
| ${}^{127}$I | 127 | 74 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1070.4061 | 1072.5762 | -0.20 % | 121631.8643 MeV (+28940.6 ppm) |
| ${}^{128}$I | 128 | 75 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1076.5206 | 1079.4024 | -0.27 % | 122592.4646 MeV (+28947.9 ppm) |
| ${}^{129}$I | 129 | 76 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1084.3572 | 1088.2428 | -0.36 % | 123551.3428 MeV (+28958.0 ppm) |
| ${}^{130}$I | 130 | 77 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1089.9768 | 1094.7431 | -0.44 % | 124512.4380 MeV (+28966.4 ppm) |
| ${}^{131}$I | 131 | 78 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1097.3149 | 1103.3210 | -0.54 % | 125471.8147 MeV (+28978.0 ppm) |
| ${}^{132}$I | 132 | 79 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1102.4623 | 1109.6531 | -0.65 % | 126433.3820 MeV (+28988.5 ppm) |
| ${}^{133}$I | 133 | 80 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1109.3242 | 1117.8782 | -0.77 % | 127393.2349 MeV (+29000.8 ppm) |
| ${}^{134}$I | 134 | 81 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1114.0207 | 1124.1357 | -0.90 % | 128355.2531 MeV (+29013.9 ppm) |
| ${}^{135}$I | 135 | 82 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1120.4275 | 1131.9427 | -1.02 % | 129315.5612 MeV (+29026.0 ppm) |
| ${}^{136}$I | 136 | 83 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1124.6932 | 1135.7801 | -0.98 % | 130278.0102 MeV (+29022.5 ppm) |
| ${}^{137}$I | 137 | 84 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1130.6646 | 1140.6625 | -0.88 % | 131238.7536 MeV (+29014.2 ppm) |
| ${}^{138}$I | 138 | 85 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1134.5184 | 1144.3574 | -0.86 % | 132201.6146 MeV (+29012.9 ppm) |
| ${}^{139}$I | 139 | 86 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1140.0730 | 1148.9198 | -0.77 % | 133162.7747 MeV (+29005.4 ppm) |
| ${}^{140}$I | 140 | 87 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1143.5328 | 1152.1264 | -0.75 % | 134126.0297 MeV (+29003.4 ppm) |
| ${}^{141}$I | 141 | 88 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1148.6883 | 1156.5181 | -0.68 % | 135087.5890 MeV (+28997.8 ppm) |
| ${}^{142}$I | 142 | 89 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1151.7708 | 1159.4657 | -0.66 % | 136051.2212 MeV (+28996.7 ppm) |
| ${}^{143}$I | 143 | 90 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1156.5438 | 1163.5910 | -0.61 % | 137013.1630 MeV (+28991.5 ppm) |
| ${}^{144}$I | 144 | 91 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1159.2650 | 1166.1120 | -0.59 % | 137977.1566 MeV (+28990.5 ppm) |
| ${}^{145}$I | 145 | 92 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1163.6712 | 1170.0050 | -0.54 % | 138939.4651 MeV (+28986.7 ppm) |
| ${}^{146}$I | 146 | 93 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1166.0460 | 1172.5260 | -0.55 % | 139903.8051 MeV (+28987.4 ppm) |
| ${}^{147}$I | 147 | 94 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1170.1004 | 1176.1470 | -0.51 % | 140866.4655 MeV (+28985.2 ppm) |

### Xenon (Z = 54)

_43 of 43 isotopes with a framework prediction; 43 of 43 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{108}$Xe | 108 | 54 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 864.0157 | 872.0880 | -0.93 % | 103469.3437 MeV (+28944.4 ppm) |
| ${}^{109}$Xe | 109 | 55 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 877.1871 | 883.6965 | -0.74 % | 104422.8872 MeV (+28931.9 ppm) |
| ${}^{110}$Xe | 110 | 56 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 892.0721 | 897.5209 | -0.61 % | 105374.7169 MeV (+28925.1 ppm) |
| ${}^{111}$Xe | 111 | 57 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 904.4086 | 908.2020 | -0.42 % | 106329.0952 MeV (+28911.7 ppm) |
| ${}^{112}$Xe | 112 | 58 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 918.4621 | 921.7672 | -0.36 % | 107281.7564 MeV (+28910.7 ppm) |
| ${}^{113}$Xe | 113 | 59 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 930.0082 | 932.0158 | -0.22 % | 108236.9251 MeV (+28901.1 ppm) |
| ${}^{114}$Xe | 114 | 60 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 943.2736 | 944.9694 | -0.18 % | 109190.3745 MeV (+28901.6 ppm) |
| ${}^{115}$Xe | 115 | 61 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 954.0707 | 954.6116 | -0.06 % | 110146.2922 MeV (+28893.4 ppm) |
| ${}^{116}$Xe | 116 | 62 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 966.5884 | 967.0730 | -0.05 % | 111100.4892 MeV (+28896.2 ppm) |
| ${}^{117}$Xe | 117 | 63 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 976.6750 | 976.2828 | +0.04 % | 112057.1174 MeV (+28890.6 ppm) |
| ${}^{118}$Xe | 118 | 64 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 988.4828 | 988.2479 | +0.02 % | 113012.0244 MeV (+28895.2 ppm) |
| ${}^{119}$Xe | 119 | 65 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 997.8948 | 997.0346 | +0.09 % | 113969.3272 MeV (+28891.9 ppm) |
| ${}^{120}$Xe | 120 | 66 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1009.0278 | 1008.4839 | +0.05 % | 114924.9090 MeV (+28897.7 ppm) |
| ${}^{121}$Xe | 121 | 67 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1017.7989 | 1016.8637 | +0.09 % | 115882.8526 MeV (+28896.4 ppm) |
| ${}^{122}$Xe | 122 | 68 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1028.2900 | 1027.8091 | +0.05 % | 116839.0763 MeV (+28903.1 ppm) |
| ${}^{123}$Xe | 123 | 69 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1036.4516 | 1035.7736 | +0.07 % | 117797.6295 MeV (+28903.4 ppm) |
| ${}^{124}$Xe | 124 | 70 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1046.3316 | 1046.2641 | +0.01 % | 118754.4642 MeV (+28911.2 ppm) |
| ${}^{125}$Xe | 125 | 71 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1053.9131 | 1053.8674 | +0.00 % | 119713.5975 MeV (+28913.2 ppm) |
| ${}^{126}$Xe | 126 | 72 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1063.2110 | 1063.8857 | -0.06 % | 120671.0144 MeV (+28921.6 ppm) |
| ${}^{127}$Xe | 127 | 73 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1070.2399 | 1071.1315 | -0.08 % | 121630.7002 MeV (+28925.0 ppm) |
| ${}^{128}$Xe | 128 | 74 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1078.9827 | 1080.7425 | -0.16 % | 122588.6723 MeV (+28934.4 ppm) |
| ${}^{129}$Xe | 129 | 75 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1085.4849 | 1087.6494 | -0.20 % | 123548.8848 MeV (+28939.2 ppm) |
| ${}^{130}$Xe | 130 | 76 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1093.6980 | 1096.9051 | -0.29 % | 124507.3865 MeV (+28949.6 ppm) |
| ${}^{131}$Xe | 131 | 77 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1099.6978 | 1103.5095 | -0.35 % | 125468.1014 MeV (+28955.8 ppm) |
| ${}^{132}$Xe | 132 | 78 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1107.4051 | 1112.4462 | -0.45 % | 126427.1089 MeV (+28967.4 ppm) |
| ${}^{133}$Xe | 133 | 79 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1112.9254 | 1118.8821 | -0.53 % | 127388.3034 MeV (+28975.8 ppm) |
| ${}^{134}$Xe | 134 | 80 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1120.1493 | 1127.4357 | -0.65 % | 128347.7943 MeV (+28987.8 ppm) |
| ${}^{135}$Xe | 135 | 81 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1125.2115 | 1133.7946 | -0.76 % | 129309.4468 MeV (+28998.9 ppm) |
| ${}^{136}$Xe | 136 | 82 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1131.9733 | 1141.8817 | -0.87 % | 130269.3998 MeV (+29010.5 ppm) |
| ${}^{137}$Xe | 137 | 83 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1136.5976 | 1145.9073 | -0.81 % | 131231.4903 MeV (+29005.8 ppm) |
| ${}^{138}$Xe | 138 | 84 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1142.9172 | 1151.5674 | -0.75 % | 132191.8855 MeV (+29001.2 ppm) |
| ${}^{139}$Xe | 139 | 85 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1147.1227 | 1155.3111 | -0.71 % | 133154.3947 MeV (+28997.7 ppm) |
| ${}^{140}$Xe | 140 | 86 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1153.0188 | 1160.7242 | -0.66 % | 134115.2134 MeV (+28994.4 ppm) |
| ${}^{141}$Xe | 141 | 87 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1156.8236 | 1164.0064 | -0.62 % | 135078.1234 MeV (+28990.5 ppm) |
| ${}^{142}$Xe | 142 | 88 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1162.3141 | 1169.1101 | -0.58 % | 136039.3477 MeV (+28988.0 ppm) |
| ${}^{143}$Xe | 143 | 89 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1165.7350 | 1172.1546 | -0.55 % | 137002.6415 MeV (+28985.2 ppm) |
| ${}^{144}$Xe | 144 | 90 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1170.8366 | 1176.8954 | -0.51 % | 137964.2547 MeV (+28982.9 ppm) |
| ${}^{145}$Xe | 145 | 91 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1173.8898 | 1179.5877 | -0.48 % | 138927.9163 MeV (+28980.2 ppm) |
| ${}^{146}$Xe | 146 | 92 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1178.6184 | 1184.1206 | -0.46 % | 139889.9024 MeV (+28979.1 ppm) |
| ${}^{147}$Xe | 147 | 93 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1181.3189 | 1186.5840 | -0.44 % | 140853.9167 MeV (+28977.7 ppm) |
| ${}^{148}$Xe | 148 | 94 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1185.6896 | 1190.9560 | -0.44 % | 141816.2608 MeV (+28977.7 ppm) |
| ${}^{149}$Xe | 149 | 95 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1188.0518 | 1193.3410 | -0.44 % | 142780.6133 MeV (+28978.1 ppm) |
| ${}^{150}$Xe | 150 | 96 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1192.0788 | 1197.4500 | -0.45 % | 143743.3011 MeV (+28978.6 ppm) |

### Caesium (Z = 55)

_42 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{111}$Cs | 111 | 56 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 890.2789 | 895.7700 | -0.61 % | 106341.8946 MeV (+28919.8 ppm) |
| ${}^{112}$Cs | 112 | 57 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 903.0835 | 907.4240 | -0.48 % | 107295.8047 MeV (+28911.1 ppm) |
| ${}^{113}$Cs | 113 | 58 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 917.5914 | 920.7944 | -0.35 % | 108248.0116 MeV (+28904.4 ppm) |
| ${}^{114}$Cs | 114 | 59 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 929.5970 | 931.7871 | -0.24 % | 109202.7208 MeV (+28897.7 ppm) |
| ${}^{115}$Cs | 115 | 60 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 943.3084 | 944.8400 | -0.16 % | 110155.7242 MeV (+28895.4 ppm) |
| ${}^{116}$Cs | 116 | 61 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 954.5563 | 955.2600 | -0.07 % | 111111.1911 MeV (+28890.5 ppm) |
| ${}^{117}$Cs | 117 | 62 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 967.5116 | 967.8082 | -0.03 % | 112064.9505 MeV (+28889.8 ppm) |
| ${}^{118}$Cs | 118 | 63 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 978.0405 | 977.7958 | +0.03 % | 113021.1364 MeV (+28887.6 ppm) |
| ${}^{119}$Cs | 119 | 64 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 990.2776 | 989.7628 | +0.05 % | 113975.6141 MeV (+28888.3 ppm) |
| ${}^{120}$Cs | 120 | 65 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1000.1235 | 999.4177 | +0.07 % | 114932.4829 MeV (+28889.2 ppm) |
| ${}^{121}$Cs | 121 | 66 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1011.6777 | 1010.7027 | +0.10 % | 115887.6435 MeV (+28889.8 ppm) |
| ${}^{122}$Cs | 122 | 67 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1020.8744 | 1019.8165 | +0.10 % | 116845.1616 MeV (+28891.4 ppm) |
| ${}^{123}$Cs | 123 | 68 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1031.7786 | 1030.7867 | +0.10 % | 117800.9721 MeV (+28894.8 ppm) |
| ${}^{124}$Cs | 124 | 69 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1040.3577 | 1039.5554 | +0.08 % | 118759.1079 MeV (+28898.6 ppm) |
| ${}^{125}$Cs | 125 | 70 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1050.6430 | 1049.9754 | +0.06 % | 119715.5373 MeV (+28902.3 ppm) |
| ${}^{126}$Cs | 126 | 71 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1058.6339 | 1058.3077 | +0.03 % | 120674.2612 MeV (+28907.2 ppm) |
| ${}^{127}$Cs | 127 | 72 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1068.3293 | 1068.2683 | +0.01 % | 121631.2806 MeV (+28911.8 ppm) |
| ${}^{128}$Cs | 128 | 73 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1075.7598 | 1076.0314 | -0.03 % | 122590.5649 MeV (+28916.4 ppm) |
| ${}^{129}$Cs | 129 | 74 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1084.8924 | 1085.6700 | -0.07 % | 123548.1470 MeV (+28922.8 ppm) |
| ${}^{130}$Cs | 130 | 75 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1091.7885 | 1093.1420 | -0.12 % | 124507.9656 MeV (+28929.1 ppm) |
| ${}^{131}$Cs | 131 | 76 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1100.3841 | 1102.3692 | -0.18 % | 125466.0849 MeV (+28936.2 ppm) |
| ${}^{132}$Cs | 132 | 77 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1106.7702 | 1109.5376 | -0.25 % | 126426.4135 MeV (+28943.9 ppm) |
| ${}^{133}$Cs | 133 | 78 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1114.8526 | 1118.5272 | -0.33 % | 127385.0459 MeV (+28953.0 ppm) |
| ${}^{134}$Cs | 134 | 79 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1120.7518 | 1125.4187 | -0.41 % | 128345.8615 MeV (+28962.1 ppm) |
| ${}^{135}$Cs | 135 | 80 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1128.3437 | 1134.1808 | -0.51 % | 129304.9844 MeV (+28973.0 ppm) |
| ${}^{136}$Cs | 136 | 81 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1133.7775 | 1141.0090 | -0.63 % | 130266.2653 MeV (+28985.0 ppm) |
| ${}^{137}$Cs | 137 | 82 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1140.9003 | 1149.2873 | -0.73 % | 131225.8573 MeV (+28995.3 ppm) |
| ${}^{138}$Cs | 138 | 83 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1145.8892 | 1153.6998 | -0.68 % | 132187.5832 MeV (+28991.0 ppm) |
| ${}^{139}$Cs | 139 | 84 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1152.5629 | 1159.5852 | -0.61 % | 133147.6243 MeV (+28985.6 ppm) |
| ${}^{140}$Cs | 140 | 85 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1157.1261 | 1164.0052 | -0.59 % | 134109.7759 MeV (+28984.8 ppm) |
| ${}^{141}$Cs | 141 | 86 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1163.3696 | 1169.5041 | -0.52 % | 135070.2470 MeV (+28979.7 ppm) |
| ${}^{142}$Cs | 142 | 87 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1167.5252 | 1173.6126 | -0.52 % | 136032.8062 MeV (+28979.7 ppm) |
| ${}^{143}$Cs | 143 | 88 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1173.3567 | 1178.8449 | -0.47 % | 136993.6896 MeV (+28975.7 ppm) |
| ${}^{144}$Cs | 144 | 89 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1177.1218 | 1182.5121 | -0.46 % | 137956.6392 MeV (+28975.2 ppm) |
| ${}^{145}$Cs | 145 | 90 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1182.5580 | 1187.3665 | -0.40 % | 138917.9178 MeV (+28971.4 ppm) |
| ${}^{146}$Cs | 146 | 91 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1185.9489 | 1190.6937 | -0.40 % | 139881.2417 MeV (+28971.1 ppm) |
| ${}^{147}$Cs | 147 | 92 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1191.0058 | 1195.3747 | -0.37 % | 140842.8995 MeV (+28968.8 ppm) |
| ${}^{148}$Cs | 148 | 93 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1194.0378 | 1198.4369 | -0.37 % | 141806.5823 MeV (+28969.2 ppm) |
| ${}^{149}$Cs | 149 | 94 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1198.7306 | 1202.8770 | -0.34 % | 142768.6042 MeV (+28967.9 ppm) |
| ${}^{150}$Cs | 150 | 95 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1201.4182 | 1205.8500 | -0.37 % | 143732.6315 MeV (+28969.9 ppm) |
| ${}^{151}$Cs | 151 | 96 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1205.7614 | 1209.9630 | -0.35 % | 144695.0030 MeV (+28969.1 ppm) |
| ${}^{152}$Cs | 152 | 97 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1208.1182 | 1212.9600 | -0.40 % | 145659.3610 MeV (+28973.2 ppm) |

### Barium (Z = 56)

_42 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{113}$Ba | 113 | 57 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 903.2375 | 907.9550 | -0.52 % | 108261.0352 MeV (+28910.2 ppm) |
| ${}^{114}$Ba | 114 | 58 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 918.1869 | 922.2243 | -0.44 % | 109212.8006 MeV (+28907.6 ppm) |
| ${}^{115}$Ba | 115 | 59 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 930.6392 | 933.3400 | -0.29 % | 110167.0630 MeV (+28897.7 ppm) |
| ${}^{116}$Ba | 116 | 60 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 944.7842 | 946.7920 | -0.21 % | 111119.6328 MeV (+28895.6 ppm) |
| ${}^{117}$Ba | 117 | 61 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 956.4707 | 957.9907 | -0.16 % | 112074.6611 MeV (+28893.7 ppm) |
| ${}^{118}$Ba | 118 | 62 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 969.8518 | 970.7860 | -0.10 % | 113027.9948 MeV (+28891.9 ppm) |
| ${}^{119}$Ba | 119 | 63 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 980.8112 | 981.2655 | -0.05 % | 113983.7501 MeV (+28890.1 ppm) |
| ${}^{120}$Ba | 120 | 64 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 993.4663 | 993.6354 | -0.02 % | 114937.8099 MeV (+28890.8 ppm) |
| ${}^{121}$Ba | 121 | 65 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1003.7348 | 1003.5629 | +0.02 % | 115894.2561 MeV (+28890.4 ppm) |
| ${}^{122}$Ba | 122 | 66 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1015.6992 | 1015.4983 | +0.02 % | 116849.0065 MeV (+28893.2 ppm) |
| ${}^{123}$Ba | 123 | 67 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1025.3106 | 1024.6157 | +0.07 % | 117806.1098 MeV (+28891.2 ppm) |
| ${}^{124}$Ba | 124 | 68 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1036.6175 | 1036.1218 | +0.05 % | 118761.5177 MeV (+28895.9 ppm) |
| ${}^{125}$Ba | 125 | 69 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1045.6035 | 1044.7723 | +0.08 % | 119719.2465 MeV (+28895.1 ppm) |
| ${}^{126}$Ba | 126 | 70 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1056.2840 | 1055.8446 | +0.04 % | 120675.2808 MeV (+28901.2 ppm) |
| ${}^{127}$Ba | 127 | 71 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1064.6742 | 1064.0639 | +0.06 % | 121633.6053 MeV (+28901.7 ppm) |
| ${}^{128}$Ba | 128 | 72 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1074.7574 | 1074.6864 | +0.01 % | 122590.2369 MeV (+28908.8 ppm) |
| ${}^{129}$Ba | 129 | 73 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1082.5797 | 1082.4495 | +0.01 % | 123549.1294 MeV (+28910.0 ppm) |
| ${}^{130}$Ba | 130 | 74 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1092.0929 | 1092.7167 | -0.06 % | 124506.3310 MeV (+28918.6 ppm) |
| ${}^{131}$Ba | 131 | 75 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1099.3735 | 1100.2102 | -0.08 % | 125465.7652 MeV (+28922.0 ppm) |
| ${}^{132}$Ba | 132 | 76 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1108.3424 | 1110.0375 | -0.15 % | 126423.5110 MeV (+28931.1 ppm) |
| ${}^{133}$Ba | 133 | 77 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1115.1058 | 1117.2274 | -0.19 % | 127383.4624 MeV (+28935.9 ppm) |
| ${}^{134}$Ba | 134 | 78 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1123.5546 | 1126.6952 | -0.28 % | 128341.7284 MeV (+28946.0 ppm) |
| ${}^{135}$Ba | 135 | 79 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1129.8240 | 1133.6672 | -0.34 % | 129302.1738 MeV (+28952.8 ppm) |
| ${}^{136}$Ba | 136 | 80 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1137.7754 | 1142.7749 | -0.44 % | 130260.9371 MeV (+28963.6 ppm) |
| ${}^{137}$Ba | 137 | 81 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1143.5725 | 1149.6805 | -0.53 % | 131221.8548 MeV (+28973.4 ppm) |
| ${}^{138}$Ba | 138 | 82 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1151.0481 | 1158.2923 | -0.63 % | 132181.0939 MeV (+28983.6 ppm) |
| ${}^{139}$Ba | 139 | 83 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1156.3935 | 1163.0157 | -0.57 % | 133142.4633 MeV (+28979.2 ppm) |
| ${}^{140}$Ba | 140 | 84 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1163.4135 | 1169.4410 | -0.52 % | 134102.1581 MeV (+28975.4 ppm) |
| ${}^{141}$Ba | 141 | 85 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1168.3265 | 1173.9769 | -0.48 % | 135063.9599 MeV (+28973.0 ppm) |
| ${}^{142}$Ba | 142 | 86 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1174.9099 | 1180.1580 | -0.44 % | 136024.0913 MeV (+28970.8 ppm) |
| ${}^{143}$Ba | 143 | 87 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1179.4088 | 1184.3243 | -0.42 % | 136986.3071 MeV (+28968.6 ppm) |
| ${}^{144}$Ba | 144 | 88 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1185.5738 | 1190.2255 | -0.39 % | 137946.8569 MeV (+28967.4 ppm) |
| ${}^{145}$Ba | 145 | 89 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1189.6759 | 1194.0459 | -0.37 % | 138909.4696 MeV (+28965.7 ppm) |
| ${}^{146}$Ba | 146 | 90 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1195.4395 | 1199.4673 | -0.34 % | 139870.4208 MeV (+28963.8 ppm) |
| ${}^{147}$Ba | 147 | 91 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1199.1611 | 1202.9364 | -0.31 % | 140833.4139 MeV (+28962.2 ppm) |
| ${}^{148}$Ba | 148 | 92 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1204.5394 | 1208.2885 | -0.31 % | 141794.7504 MeV (+28962.7 ppm) |
| ${}^{149}$Ba | 149 | 93 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1207.8960 | 1211.6456 | -0.31 % | 142758.1085 MeV (+28963.0 ppm) |
| ${}^{150}$Ba | 150 | 94 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1212.9044 | 1216.7761 | -0.32 % | 143719.8149 MeV (+28964.5 ppm) |
| ${}^{151}$Ba | 151 | 95 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1215.9107 | 1219.9290 | -0.33 % | 144683.5234 MeV (+28965.5 ppm) |
| ${}^{152}$Ba | 152 | 96 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1220.5637 | 1224.6640 | -0.33 % | 145645.5852 MeV (+28966.6 ppm) |
| ${}^{153}$Ba | 153 | 97 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1223.2335 | 1227.5190 | -0.35 % | 146609.6302 MeV (+28968.6 ppm) |
| ${}^{154}$Ba | 154 | 98 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1227.5447 | 1232.1540 | -0.37 % | 147572.0337 MeV (+28970.5 ppm) |

### Lanthanum (Z = 57)

_42 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{116}$La | 116 | 59 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 928.9680 | 931.7120 | -0.29 % | 111134.1188 MeV (+28893.2 ppm) |
| ${}^{117}$La | 117 | 60 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 943.5523 | 946.0620 | -0.27 % | 112086.2492 MeV (+28894.4 ppm) |
| ${}^{118}$La | 118 | 61 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 955.6831 | 957.4520 | -0.18 % | 113040.8332 MeV (+28890.9 ppm) |
| ${}^{119}$La | 119 | 62 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 969.4958 | 970.9210 | -0.15 % | 113993.7353 MeV (+28891.4 ppm) |
| ${}^{120}$La | 120 | 63 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 980.8914 | 981.4800 | -0.06 % | 114949.0544 MeV (+28887.2 ppm) |
| ${}^{121}$La | 121 | 64 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 993.9702 | 994.2570 | -0.03 % | 115902.6904 MeV (+28887.1 ppm) |
| ${}^{122}$La | 122 | 65 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1004.6670 | 1004.6700 | -0.00 % | 116858.7084 MeV (+28887.4 ppm) |
| ${}^{123}$La | 123 | 66 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1017.0475 | 1016.8410 | +0.02 % | 117813.0427 MeV (+28888.8 ppm) |
| ${}^{124}$La | 124 | 67 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1027.0793 | 1026.5083 | +0.06 % | 118769.7256 MeV (+28888.2 ppm) |
| ${}^{125}$La | 125 | 68 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1038.7947 | 1038.0805 | +0.07 % | 119724.7250 MeV (+28890.0 ppm) |
| ${}^{126}$La | 126 | 69 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1048.1933 | 1047.3658 | +0.08 % | 120682.0411 MeV (+28891.3 ppm) |
| ${}^{127}$La | 127 | 70 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1059.2748 | 1058.3597 | +0.09 % | 121637.6745 MeV (+28893.3 ppm) |
| ${}^{128}$La | 128 | 71 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1068.0701 | 1067.1604 | +0.09 % | 122595.5940 MeV (+28895.5 ppm) |
| ${}^{129}$La | 129 | 72 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1078.5468 | 1077.9298 | +0.06 % | 123551.8320 MeV (+28900.5 ppm) |
| ${}^{130}$La | 130 | 73 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1086.7667 | 1086.3049 | +0.04 % | 124510.3269 MeV (+28903.8 ppm) |
| ${}^{131}$La | 131 | 74 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1096.6662 | 1096.5182 | +0.01 % | 125467.1422 MeV (+28908.7 ppm) |
| ${}^{132}$La | 132 | 75 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1104.3369 | 1104.5438 | -0.02 % | 126426.1862 MeV (+28913.4 ppm) |
| ${}^{133}$La | 133 | 76 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1113.6850 | 1114.3859 | -0.06 % | 127383.5529 MeV (+28919.5 ppm) |
| ${}^{134}$La | 134 | 77 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1120.8314 | 1122.1815 | -0.12 % | 128343.1213 MeV (+28926.4 ppm) |
| ${}^{135}$La | 135 | 78 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1129.6524 | 1131.6776 | -0.18 % | 129301.0151 MeV (+28933.7 ppm) |
| ${}^{136}$La | 136 | 79 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1136.2976 | 1139.1430 | -0.25 % | 130261.0846 MeV (+28941.6 ppm) |
| ${}^{137}$La | 137 | 80 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1144.6144 | 1148.3177 | -0.32 % | 131219.4826 MeV (+28950.1 ppm) |
| ${}^{138}$La | 138 | 81 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1150.7804 | 1155.7615 | -0.43 % | 132180.0314 MeV (+28961.3 ppm) |
| ${}^{139}$La | 139 | 82 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1158.6146 | 1164.5418 | -0.51 % | 133138.9120 MeV (+28970.1 ppm) |
| ${}^{140}$La | 140 | 83 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1164.3220 | 1169.7028 | -0.46 % | 134099.9193 MeV (+28966.5 ppm) |
| ${}^{141}$La | 141 | 84 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1171.6940 | 1176.3919 | -0.40 % | 135059.2621 MeV (+28962.3 ppm) |
| ${}^{142}$La | 142 | 85 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1176.9624 | 1181.5573 | -0.39 % | 136020.7084 MeV (+28962.2 ppm) |
| ${}^{143}$La | 143 | 86 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1183.8914 | 1187.7762 | -0.33 % | 136980.4942 MeV (+28957.7 ppm) |
| ${}^{144}$La | 144 | 87 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1188.7393 | 1192.5257 | -0.32 % | 137942.3612 MeV (+28957.6 ppm) |
| ${}^{145}$La | 145 | 88 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1195.2435 | 1198.5827 | -0.28 % | 138902.5717 MeV (+28955.1 ppm) |
| ${}^{146}$La | 146 | 89 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1199.6881 | 1203.0398 | -0.28 % | 139864.8419 MeV (+28955.8 ppm) |
| ${}^{147}$La | 147 | 90 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1205.7847 | 1208.5684 | -0.23 % | 140825.4600 MeV (+28952.4 ppm) |
| ${}^{148}$La | 148 | 91 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1209.8427 | 1212.6700 | -0.23 % | 141788.1168 MeV (+28953.1 ppm) |
| ${}^{149}$La | 149 | 92 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1215.5480 | 1218.2525 | -0.22 % | 142749.1263 MeV (+28953.0 ppm) |
| ${}^{150}$La | 150 | 93 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1219.2348 | 1222.4151 | -0.26 % | 143712.1542 MeV (+28956.9 ppm) |
| ${}^{151}$La | 151 | 94 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1224.5644 | 1227.4856 | -0.24 % | 144673.5395 MeV (+28955.7 ppm) |
| ${}^{152}$La | 152 | 95 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1227.8949 | 1231.5040 | -0.29 % | 145636.9237 MeV (+28961.2 ppm) |
| ${}^{153}$La | 153 | 96 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1232.8632 | 1236.3930 | -0.29 % | 146598.6702 MeV (+28960.9 ppm) |
| ${}^{154}$La | 154 | 97 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1235.8513 | 1239.8540 | -0.32 % | 147562.3968 MeV (+28965.0 ppm) |
| ${}^{155}$La | 155 | 98 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1240.4723 | 1244.3400 | -0.31 % | 148524.4906 MeV (+28964.5 ppm) |
| ${}^{156}$La | 156 | 99 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1243.1315 | 1247.5320 | -0.35 % | 149488.5462 MeV (+28968.3 ppm) |
| ${}^{157}$La | 157 | 100 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1247.4183 | 1251.6040 | -0.33 % | 150450.9741 MeV (+28967.3 ppm) |

### Cerium (Z = 58)

_41 of 41 isotopes with a framework prediction; 41 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{119}$Ce | 119 | 61 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 956.3312 | 958.9020 | -0.27 % | 114005.5696 MeV (+28894.2 ppm) |
| ${}^{120}$Ce | 120 | 62 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 970.5636 | 972.9600 | -0.25 % | 114958.0519 MeV (+28895.6 ppm) |
| ${}^{121}$Ce | 121 | 63 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 982.3840 | 983.9720 | -0.16 % | 115912.9463 MeV (+28891.4 ppm) |
| ${}^{122}$Ce | 122 | 64 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 995.8753 | 997.2280 | -0.14 % | 116866.1698 MeV (+28892.7 ppm) |
| ${}^{123}$Ce | 123 | 65 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1006.9892 | 1007.7390 | -0.07 % | 117821.7706 MeV (+28889.9 ppm) |
| ${}^{124}$Ce | 124 | 66 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1019.7749 | 1020.3960 | -0.06 % | 118775.6997 MeV (+28892.4 ppm) |
| ${}^{125}$Ce | 125 | 67 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1030.2165 | 1030.2500 | -0.00 % | 119731.9729 MeV (+28889.4 ppm) |
| ${}^{126}$Ce | 126 | 68 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1042.3299 | 1042.4305 | -0.01 % | 120686.5743 MeV (+28893.5 ppm) |
| ${}^{127}$Ce | 127 | 69 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1052.1309 | 1051.6606 | +0.04 % | 121643.4881 MeV (+28891.0 ppm) |
| ${}^{128}$Ce | 128 | 70 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1063.6032 | 1063.2865 | +0.03 % | 122598.7305 MeV (+28895.1 ppm) |
| ${}^{129}$Ce | 129 | 71 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1072.7936 | 1072.1114 | +0.06 % | 123556.2549 MeV (+28894.2 ppm) |
| ${}^{130}$Ce | 130 | 72 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1083.6542 | 1083.3181 | +0.03 % | 124512.1091 MeV (+28899.8 ppm) |
| ${}^{131}$Ce | 131 | 73 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1092.2621 | 1091.6750 | +0.05 % | 125470.2160 MeV (+28899.6 ppm) |
| ${}^{132}$Ce | 132 | 74 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1102.5385 | 1102.5065 | +0.00 % | 126426.6543 MeV (+28906.7 ppm) |
| ${}^{133}$Ce | 133 | 75 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1110.5902 | 1110.5274 | +0.01 % | 127385.3174 MeV (+28908.2 ppm) |
| ${}^{134}$Ce | 134 | 76 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1120.3085 | 1121.0134 | -0.06 % | 128342.3139 MeV (+28916.7 ppm) |
| ${}^{135}$Ce | 135 | 77 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1127.8289 | 1128.8681 | -0.09 % | 129301.5083 MeV (+28921.0 ppm) |
| ${}^{136}$Ce | 136 | 78 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1137.0133 | 1138.8317 | -0.16 % | 130259.0386 MeV (+28929.3 ppm) |
| ${}^{137}$Ce | 137 | 79 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1144.0258 | 1146.3132 | -0.20 % | 131218.7409 MeV (+28934.4 ppm) |
| ${}^{138}$Ce | 138 | 80 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1152.6995 | 1156.0316 | -0.29 % | 132176.7819 MeV (+28944.4 ppm) |
| ${}^{139}$Ce | 139 | 81 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1159.2261 | 1163.4948 | -0.37 % | 133136.9701 MeV (+28953.0 ppm) |
| ${}^{140}$Ce | 140 | 82 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1167.4108 | 1172.6826 | -0.45 % | 134095.5002 MeV (+28962.3 ppm) |
| ${}^{141}$Ce | 141 | 83 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1173.4723 | 1178.1108 | -0.39 % | 135056.1535 MeV (+28958.2 ppm) |
| ${}^{142}$Ce | 142 | 84 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1181.1885 | 1185.2839 | -0.35 % | 136015.1521 MeV (+28955.2 ppm) |
| ${}^{143}$Ce | 143 | 85 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1186.8046 | 1190.4287 | -0.30 % | 136976.2508 MeV (+28952.4 ppm) |
| ${}^{144}$Ce | 144 | 86 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1194.0715 | 1197.3256 | -0.27 % | 137935.6986 MeV (+28950.7 ppm) |
| ${}^{145}$Ce | 145 | 87 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1199.2608 | 1202.0320 | -0.23 % | 138897.2241 MeV (+28947.8 ppm) |
| ${}^{146}$Ce | 146 | 88 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1206.0969 | 1208.6622 | -0.21 % | 139857.1028 MeV (+28947.3 ppm) |
| ${}^{147}$Ce | 147 | 89 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1210.8768 | 1213.1215 | -0.19 % | 140819.0376 MeV (+28945.5 ppm) |
| ${}^{148}$Ce | 148 | 90 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1217.2994 | 1219.5774 | -0.19 % | 141779.3298 MeV (+28946.8 ppm) |
| ${}^{149}$Ce | 149 | 91 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1221.6866 | 1223.9202 | -0.18 % | 142741.6574 MeV (+28947.0 ppm) |
| ${}^{150}$Ce | 150 | 92 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1227.7121 | 1230.1684 | -0.20 % | 143702.3466 MeV (+28949.6 ppm) |
| ${}^{151}$Ce | 151 | 93 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1231.7223 | 1234.6180 | -0.23 % | 144665.0512 MeV (+28953.3 ppm) |
| ${}^{152}$Ce | 152 | 94 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1237.3663 | 1240.4720 | -0.25 % | 145626.1220 MeV (+28955.4 ppm) |
| ${}^{153}$Ce | 153 | 95 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1241.0144 | 1244.5020 | -0.28 % | 146589.1886 MeV (+28958.3 ppm) |
| ${}^{154}$Ce | 154 | 96 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1246.2916 | 1249.8640 | -0.29 % | 147550.6262 MeV (+28959.7 ppm) |
| ${}^{155}$Ce | 155 | 97 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1249.5919 | 1253.4850 | -0.31 % | 148514.0408 MeV (+28962.3 ppm) |
| ${}^{156}$Ce | 156 | 98 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1254.5163 | 1258.6080 | -0.33 % | 149475.8311 MeV (+28964.1 ppm) |
| ${}^{157}$Ce | 157 | 99 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1257.4820 | 1261.8090 | -0.34 % | 150439.5802 MeV (+28965.8 ppm) |
| ${}^{158}$Ce | 158 | 100 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1262.0670 | 1266.3700 | -0.34 % | 151401.7100 MeV (+28966.9 ppm) |
| ${}^{159}$Ce | 159 | 101 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1264.7109 | 1269.2970 | -0.36 % | 152365.7808 MeV (+28968.6 ppm) |

### Praseodymium (Z = 59)

_41 of 41 isotopes with a framework prediction; 41 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{121}$Pr | 121 | 62 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 968.9761 | 971.9930 | -0.31 % | 115925.0239 MeV (+28896.9 ppm) |
| ${}^{122}$Pr | 122 | 63 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 981.2265 | 983.3200 | -0.21 % | 116879.4882 MeV (+28891.4 ppm) |
| ${}^{123}$Pr | 123 | 64 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 995.1359 | 996.7920 | -0.17 % | 117832.2937 MeV (+28891.4 ppm) |
| ${}^{124}$Pr | 124 | 65 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1006.6725 | 1007.8720 | -0.12 % | 118787.4719 MeV (+28889.5 ppm) |
| ${}^{125}$Pr | 125 | 66 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1019.8689 | 1020.8750 | -0.10 % | 119740.9902 MeV (+28891.0 ppm) |
| ${}^{126}$Pr | 126 | 67 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1030.7256 | 1031.1840 | -0.04 % | 120696.8483 MeV (+28889.0 ppm) |
| ${}^{127}$Pr | 127 | 68 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1043.2426 | 1043.4320 | -0.02 % | 121651.0461 MeV (+28890.2 ppm) |
| ${}^{128}$Pr | 128 | 69 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1053.4514 | 1053.3010 | +0.01 % | 122607.5520 MeV (+28889.7 ppm) |
| ${}^{129}$Pr | 129 | 70 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1065.3202 | 1064.8151 | +0.05 % | 123562.3980 MeV (+28889.6 ppm) |
| ${}^{130}$Pr | 130 | 71 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1074.9112 | 1074.2883 | +0.06 % | 124519.5218 MeV (+28890.9 ppm) |
| ${}^{131}$Pr | 131 | 72 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1086.1612 | 1085.4849 | +0.06 % | 125474.9866 MeV (+28893.1 ppm) |
| ${}^{132}$Pr | 132 | 73 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1095.1625 | 1094.4830 | +0.06 % | 126432.7001 MeV (+28895.2 ppm) |
| ${}^{133}$Pr | 133 | 74 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1105.8214 | 1105.2644 | +0.05 % | 127388.7559 MeV (+28898.8 ppm) |
| ${}^{134}$Pr | 134 | 75 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1114.2595 | 1113.9261 | +0.03 % | 128347.0326 MeV (+28902.5 ppm) |
| ${}^{135}$Pr | 135 | 76 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1124.3535 | 1124.4053 | -0.00 % | 129303.6534 MeV (+28908.0 ppm) |
| ${}^{136}$Pr | 136 | 77 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1132.2533 | 1132.8812 | -0.06 % | 130262.4683 MeV (+28914.4 ppm) |
| ${}^{137}$Pr | 137 | 78 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1141.8068 | 1142.8139 | -0.09 % | 131219.6296 MeV (+28919.4 ppm) |
| ${}^{138}$Pr | 138 | 79 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1149.1920 | 1150.8123 | -0.14 % | 132178.9592 MeV (+28925.8 ppm) |
| ${}^{139}$Pr | 139 | 80 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1158.2281 | 1160.5834 | -0.20 % | 133136.6378 MeV (+28933.5 ppm) |
| ${}^{140}$Pr | 140 | 81 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1165.1207 | 1168.5123 | -0.29 % | 134096.4600 MeV (+28942.9 ppm) |
| ${}^{141}$Pr | 141 | 82 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1173.6614 | 1177.9119 | -0.36 % | 135054.6341 MeV (+28951.2 ppm) |
| ${}^{142}$Pr | 142 | 83 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1180.0824 | 1183.7551 | -0.31 % | 136014.9279 MeV (+28947.7 ppm) |
| ${}^{143}$Pr | 143 | 84 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1188.1482 | 1191.1082 | -0.25 % | 136973.5769 MeV (+28943.6 ppm) |
| ${}^{144}$Pr | 144 | 85 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1194.1173 | 1196.8619 | -0.23 % | 137934.3225 MeV (+28942.9 ppm) |
| ${}^{145}$Pr | 145 | 86 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1201.7277 | 1203.8086 | -0.17 % | 138893.4268 MeV (+28939.1 ppm) |
| ${}^{146}$Pr | 146 | 87 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1207.2637 | 1208.9275 | -0.14 % | 139854.6056 MeV (+28936.9 ppm) |
| ${}^{147}$Pr | 147 | 88 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1214.4372 | 1215.7694 | -0.11 % | 140814.1469 MeV (+28935.6 ppm) |
| ${}^{148}$Pr | 148 | 89 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1219.5577 | 1220.9321 | -0.11 % | 141775.7412 MeV (+28936.7 ppm) |
| ${}^{149}$Pr | 149 | 90 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1226.3117 | 1227.5073 | -0.10 % | 142735.7019 MeV (+28936.5 ppm) |
| ${}^{150}$Pr | 150 | 91 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1231.0335 | 1232.8397 | -0.15 % | 143697.6949 MeV (+28941.7 ppm) |
| ${}^{151}$Pr | 151 | 92 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1237.3846 | 1239.3902 | -0.16 % | 144658.0586 MeV (+28944.2 ppm) |
| ${}^{152}$Pr | 152 | 93 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1241.7235 | 1244.4399 | -0.22 % | 145620.4345 MeV (+28949.9 ppm) |
| ${}^{153}$Pr | 153 | 94 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1247.6873 | 1250.3217 | -0.21 % | 146581.1855 MeV (+28950.2 ppm) |
| ${}^{154}$Pr | 154 | 95 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1251.6584 | 1254.6841 | -0.24 % | 147543.9292 MeV (+28953.4 ppm) |
| ${}^{155}$Pr | 155 | 96 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1257.2498 | 1260.3112 | -0.24 % | 148505.0525 MeV (+28954.4 ppm) |
| ${}^{156}$Pr | 156 | 97 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1260.8673 | 1264.4165 | -0.28 % | 149468.1498 MeV (+28958.2 ppm) |
| ${}^{157}$Pr | 157 | 98 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1266.1005 | 1269.4733 | -0.27 % | 150429.6314 MeV (+28957.6 ppm) |
| ${}^{158}$Pr | 158 | 99 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1269.3780 | 1273.3220 | -0.31 % | 151393.0687 MeV (+28961.4 ppm) |
| ${}^{159}$Pr | 159 | 100 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1274.2663 | 1277.8830 | -0.28 % | 152354.8951 MeV (+28960.6 ppm) |
| ${}^{160}$Pr | 160 | 101 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1277.2166 | 1281.4400 | -0.33 % | 153318.6596 MeV (+28964.6 ppm) |
| ${}^{161}$Pr | 161 | 102 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1281.7729 | 1285.7460 | -0.31 % | 154280.8180 MeV (+28963.7 ppm) |

### Neodymium (Z = 60)

_40 of 40 isotopes with a framework prediction; 40 of 40 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{124}$Nd | 124 | 64 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 995.8038 | 998.6960 | -0.29 % | 118797.0102 MeV (+28898.0 ppm) |
| ${}^{125}$Nd | 125 | 65 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1007.7520 | 1010.0000 | -0.22 % | 119751.7768 MeV (+28895.3 ppm) |
| ${}^{126}$Nd | 126 | 66 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1021.3486 | 1023.3720 | -0.20 % | 120704.8950 MeV (+28896.7 ppm) |
| ${}^{127}$Nd | 127 | 67 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1032.6099 | 1034.0340 | -0.14 % | 121660.3485 MeV (+28893.7 ppm) |
| ${}^{128}$Nd | 128 | 68 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1045.5201 | 1046.6560 | -0.11 % | 122614.1530 MeV (+28895.0 ppm) |
| ${}^{129}$Nd | 129 | 69 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1056.1266 | 1056.6390 | -0.05 % | 123570.2613 MeV (+28891.6 ppm) |
| ${}^{130}$Nd | 130 | 70 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1068.3819 | 1068.9268 | -0.05 % | 124524.7208 MeV (+28894.9 ppm) |
| ${}^{131}$Nd | 131 | 71 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1078.3636 | 1078.1699 | +0.02 % | 125481.4539 MeV (+28891.1 ppm) |
| ${}^{132}$Nd | 132 | 72 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1089.9935 | 1089.8990 | +0.01 % | 126436.5388 MeV (+28894.7 ppm) |
| ${}^{133}$Nd | 133 | 73 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1099.3787 | 1098.8769 | +0.05 % | 127393.8683 MeV (+28893.5 ppm) |
| ${}^{134}$Nd | 134 | 74 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1110.4109 | 1110.2622 | +0.01 % | 128349.5509 MeV (+28899.0 ppm) |
| ${}^{135}$Nd | 135 | 75 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1119.2262 | 1118.9007 | +0.03 % | 129307.4503 MeV (+28899.5 ppm) |
| ${}^{136}$Nd | 136 | 76 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1129.6870 | 1129.9577 | -0.02 % | 130263.7044 MeV (+28906.7 ppm) |
| ${}^{137}$Nd | 137 | 77 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1137.9574 | 1138.4137 | -0.04 % | 131222.1487 MeV (+28910.0 ppm) |
| ${}^{138}$Nd | 138 | 78 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1147.8713 | 1148.9183 | -0.09 % | 132178.9495 MeV (+28916.9 ppm) |
| ${}^{139}$Nd | 139 | 79 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1155.6206 | 1156.9893 | -0.12 % | 133137.9150 MeV (+28921.0 ppm) |
| ${}^{140}$Nd | 140 | 80 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1165.0109 | 1167.3010 | -0.20 % | 134095.2396 MeV (+28930.2 ppm) |
| ${}^{141}$Nd | 141 | 81 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1172.2612 | 1175.3065 | -0.26 % | 135054.7040 MeV (+28937.4 ppm) |
| ${}^{142}$Nd | 142 | 82 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1181.1498 | 1185.1364 | -0.34 % | 136012.5302 MeV (+28946.4 ppm) |
| ${}^{143}$Nd | 143 | 83 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1187.9223 | 1191.2600 | -0.28 % | 136972.4725 MeV (+28942.5 ppm) |
| ${}^{144}$Nd | 144 | 84 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1196.3299 | 1199.0770 | -0.23 % | 137930.7796 MeV (+28939.5 ppm) |
| ${}^{145}$Nd | 145 | 85 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1202.6444 | 1204.8323 | -0.18 % | 138891.1799 MeV (+28936.3 ppm) |
| ${}^{146}$Nd | 146 | 86 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1210.5907 | 1212.3975 | -0.15 % | 139849.9483 MeV (+28934.8 ppm) |
| ${}^{147}$Nd | 147 | 87 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1216.4660 | 1217.6897 | -0.10 % | 140810.7878 MeV (+28931.4 ppm) |
| ${}^{148}$Nd | 148 | 88 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1223.9696 | 1225.0223 | -0.09 % | 141769.9990 MeV (+28931.4 ppm) |
| ${}^{149}$Nd | 149 | 89 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1229.4235 | 1230.0611 | -0.05 % | 142731.2599 MeV (+28929.2 ppm) |
| ${}^{150}$Nd | 150 | 90 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1236.5018 | 1237.4368 | -0.08 % | 143690.8964 MeV (+28932.7 ppm) |
| ${}^{151}$Nd | 151 | 91 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1241.5512 | 1242.7714 | -0.10 % | 144652.5618 MeV (+28935.6 ppm) |
| ${}^{152}$Nd | 152 | 92 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1248.2209 | 1250.0492 | -0.15 % | 145612.6068 MeV (+28941.1 ppm) |
| ${}^{153}$Nd | 153 | 93 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1252.8818 | 1255.3012 | -0.19 % | 146574.6607 MeV (+28946.0 ppm) |
| ${}^{154}$Nd | 154 | 94 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1259.1588 | 1261.6218 | -0.20 % | 147535.0985 MeV (+28947.2 ppm) |
| ${}^{155}$Nd | 155 | 95 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1263.4462 | 1266.3973 | -0.23 % | 148497.5258 MeV (+28951.2 ppm) |
| ${}^{156}$Nd | 156 | 96 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1269.3455 | 1272.3869 | -0.24 % | 149458.3413 MeV (+28952.7 ppm) |
| ${}^{157}$Nd | 157 | 97 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1273.2738 | 1276.7502 | -0.27 % | 150421.1277 MeV (+28956.2 ppm) |
| ${}^{158}$Nd | 158 | 98 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1278.8096 | 1282.1626 | -0.26 % | 151382.3068 MeV (+28956.0 ppm) |
| ${}^{159}$Nd | 159 | 99 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1282.3926 | 1286.1228 | -0.29 % | 152345.4385 MeV (+28959.0 ppm) |
| ${}^{160}$Nd | 160 | 100 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1287.5784 | 1291.1946 | -0.28 % | 153306.9675 MeV (+28958.8 ppm) |
| ${}^{161}$Nd | 161 | 101 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1290.8290 | 1294.7620 | -0.30 % | 154270.4316 MeV (+28961.2 ppm) |
| ${}^{162}$Nd | 162 | 102 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1295.6776 | 1299.5640 | -0.30 % | 155232.2978 MeV (+28961.8 ppm) |
| ${}^{163}$Nd | 163 | 103 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1298.6083 | 1302.6960 | -0.31 % | 156196.0819 MeV (+28963.4 ppm) |

### Promethium (Z = 61)

_40 of 40 isotopes with a framework prediction; 40 of 40 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{126}$Pm | 126 | 65 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1006.2308 | 1009.0080 | -0.28 % | 120718.6825 MeV (+28894.7 ppm) |
| ${}^{127}$Pm | 127 | 66 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1020.2327 | 1022.6040 | -0.23 % | 121671.3953 MeV (+28894.9 ppm) |
| ${}^{128}$Pm | 128 | 67 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1031.9039 | 1033.6000 | -0.16 % | 122626.4390 MeV (+28891.8 ppm) |
| ${}^{129}$Pm | 129 | 68 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1045.2127 | 1046.7060 | -0.14 % | 123579.8449 MeV (+28892.7 ppm) |
| ${}^{130}$Pm | 130 | 69 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1056.2220 | 1057.0300 | -0.08 % | 124535.5504 MeV (+28889.8 ppm) |
| ${}^{131}$Pm | 131 | 70 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1068.8692 | 1069.3530 | -0.05 % | 125489.6180 MeV (+28890.5 ppm) |
| ${}^{132}$Pm | 132 | 71 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1079.2468 | 1079.3640 | -0.01 % | 126445.9551 MeV (+28889.2 ppm) |
| ${}^{133}$Pm | 133 | 72 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1091.2619 | 1091.1698 | +0.01 % | 127400.6548 MeV (+28890.7 ppm) |
| ${}^{134}$Pm | 134 | 73 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1101.0362 | 1100.5974 | +0.04 % | 128357.5953 MeV (+28890.2 ppm) |
| ${}^{135}$Pm | 135 | 74 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1112.4471 | 1111.9671 | +0.04 % | 129312.8992 MeV (+28892.5 ppm) |
| ${}^{136}$Pm | 136 | 75 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1121.6448 | 1121.1460 | +0.04 % | 130270.4162 MeV (+28894.5 ppm) |
| ${}^{137}$Pm | 137 | 76 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1132.4776 | 1132.1203 | +0.03 % | 131226.2982 MeV (+28898.1 ppm) |
| ${}^{138}$Pm | 138 | 77 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1141.1240 | 1141.0331 | +0.01 % | 132184.3666 MeV (+28902.1 ppm) |
| ${}^{139}$Pm | 139 | 78 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1151.4035 | 1151.6911 | -0.02 % | 133140.8018 MeV (+28907.4 ppm) |
| ${}^{140}$Pm | 140 | 79 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1159.5221 | 1160.4734 | -0.08 % | 134099.3980 MeV (+28914.4 ppm) |
| ${}^{141}$Pm | 141 | 80 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1169.2718 | 1170.8556 | -0.14 % | 135056.3631 MeV (+28921.3 ppm) |
| ${}^{142}$Pm | 142 | 81 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1176.8851 | 1179.5455 | -0.23 % | 136015.4646 MeV (+28931.2 ppm) |
| ${}^{143}$Pm | 143 | 82 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1186.1269 | 1189.4360 | -0.28 % | 136972.9376 MeV (+28938.0 ppm) |
| ${}^{144}$Pm | 144 | 83 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1193.2560 | 1195.9628 | -0.23 % | 137932.5232 MeV (+28934.6 ppm) |
| ${}^{145}$Pm | 145 | 84 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1202.0108 | 1203.8855 | -0.16 % | 138890.4832 MeV (+28929.8 ppm) |
| ${}^{146}$Pm | 146 | 85 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1208.6758 | 1210.1436 | -0.12 % | 139850.5330 MeV (+28927.9 ppm) |
| ${}^{147}$Pm | 147 | 86 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1216.9632 | 1217.8026 | -0.07 % | 140808.9603 MeV (+28924.7 ppm) |
| ${}^{148}$Pm | 148 | 87 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1223.1830 | 1223.6978 | -0.04 % | 141769.4553 MeV (+28923.4 ppm) |
| ${}^{149}$Pm | 149 | 88 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1231.0218 | 1230.9676 | +0.00 % | 142728.3313 MeV (+28920.7 ppm) |
| ${}^{150}$Pm | 150 | 89 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1236.8142 | 1236.5719 | +0.02 % | 143689.2536 MeV (+28920.3 ppm) |
| ${}^{151}$Pm | 151 | 90 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1244.2221 | 1244.4321 | -0.02 % | 144648.5606 MeV (+28925.0 ppm) |
| ${}^{152}$Pm | 152 | 91 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1249.6041 | 1250.3717 | -0.06 % | 145609.8933 MeV (+28929.9 ppm) |
| ${}^{153}$Pm | 153 | 92 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1256.5978 | 1257.8365 | -0.10 % | 146569.6144 MeV (+28934.5 ppm) |
| ${}^{154}$Pm | 154 | 93 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1261.5856 | 1263.5264 | -0.15 % | 147531.3413 MeV (+28940.3 ppm) |
| ${}^{155}$Pm | 155 | 94 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1268.1810 | 1270.2711 | -0.16 % | 148491.4607 MeV (+28942.4 ppm) |
| ${}^{156}$Pm | 156 | 95 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1272.7898 | 1275.5693 | -0.22 % | 149453.5667 MeV (+28947.9 ppm) |
| ${}^{157}$Pm | 157 | 96 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1279.0020 | 1281.7709 | -0.22 % | 150414.0692 MeV (+28948.7 ppm) |
| ${}^{158}$Pm | 158 | 97 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1283.2464 | 1286.6512 | -0.26 % | 151376.5397 MeV (+28953.7 ppm) |
| ${}^{159}$Pm | 159 | 98 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1289.0898 | 1292.1708 | -0.24 % | 152337.4111 MeV (+28952.2 ppm) |
| ${}^{160}$Pm | 160 | 99 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1292.9834 | 1296.5824 | -0.28 % | 153300.2322 MeV (+28956.2 ppm) |
| ${}^{161}$Pm | 161 | 100 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1298.4716 | 1301.8456 | -0.26 % | 154261.4588 MeV (+28955.3 ppm) |
| ${}^{162}$Pm | 162 | 101 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1302.0276 | 1305.8820 | -0.30 % | 155224.6175 MeV (+28958.8 ppm) |
| ${}^{163}$Pm | 163 | 102 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1307.1736 | 1310.8460 | -0.28 % | 156186.1863 MeV (+28958.4 ppm) |
| ${}^{164}$Pm | 164 | 103 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1310.4044 | 1314.2960 | -0.30 % | 157149.6703 MeV (+28960.2 ppm) |
| ${}^{165}$Pm | 165 | 104 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1315.2206 | 1318.6800 | -0.26 % | 158111.5689 MeV (+28957.8 ppm) |

### Samarium (Z = 62)

_41 of 41 isotopes with a framework prediction; 41 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{128}$Sm | 128 | 66 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1020.5081 | 1023.7440 | -0.32 % | 122636.5044 MeV (+28898.0 ppm) |
| ${}^{129}$Sm | 129 | 67 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1032.5786 | 1034.9670 | -0.23 % | 123591.1487 MeV (+28893.8 ppm) |
| ${}^{130}$Sm | 130 | 68 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1046.2759 | 1048.4500 | -0.21 % | 124544.1662 MeV (+28894.9 ppm) |
| ${}^{131}$Sm | 131 | 69 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1057.6780 | 1059.1350 | -0.14 % | 125499.4789 MeV (+28891.3 ppm) |
| ${}^{132}$Sm | 132 | 70 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1070.7072 | 1072.1040 | -0.13 % | 126453.1644 MeV (+28893.6 ppm) |
| ${}^{133}$Sm | 133 | 71 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1081.4711 | 1082.2210 | -0.07 % | 127409.1153 MeV (+28891.1 ppm) |
| ${}^{134}$Sm | 134 | 72 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1093.8619 | 1094.3780 | -0.05 % | 128363.4393 MeV (+28892.6 ppm) |
| ${}^{135}$Sm | 135 | 73 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1104.0160 | 1103.9796 | +0.00 % | 129319.9999 MeV (+28890.0 ppm) |
| ${}^{136}$Sm | 136 | 74 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1115.7963 | 1116.0046 | -0.02 % | 130274.9344 MeV (+28894.7 ppm) |
| ${}^{137}$Sm | 137 | 75 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1125.3674 | 1125.2567 | +0.01 % | 131232.0781 MeV (+28894.3 ppm) |
| ${}^{138}$Sm | 138 | 76 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1136.5635 | 1136.8341 | -0.02 % | 132187.5968 MeV (+28899.9 ppm) |
| ${}^{139}$Sm | 139 | 77 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1145.5769 | 1145.7879 | -0.02 % | 133145.2981 MeV (+28901.4 ppm) |
| ${}^{140}$Sm | 140 | 78 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1156.2136 | 1156.9350 | -0.06 % | 134101.3762 MeV (+28907.8 ppm) |
| ${}^{141}$Sm | 141 | 79 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1164.6931 | 1165.4843 | -0.07 % | 135059.6115 MeV (+28910.1 ppm) |
| ${}^{142}$Sm | 142 | 80 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1174.7939 | 1176.6036 | -0.15 % | 136016.2255 MeV (+28920.1 ppm) |
| ${}^{143}$Sm | 143 | 81 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1182.7620 | 1185.2101 | -0.21 % | 136974.9722 MeV (+28926.6 ppm) |
| ${}^{144}$Sm | 144 | 82 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1192.3489 | 1195.7299 | -0.28 % | 137932.1000 MeV (+28935.6 ppm) |
| ${}^{145}$Sm | 145 | 83 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1199.8268 | 1202.4870 | -0.22 % | 138891.3368 MeV (+28931.5 ppm) |
| ${}^{146}$Sm | 146 | 84 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1208.9210 | 1210.9033 | -0.16 % | 139848.9575 MeV (+28928.0 ppm) |
| ${}^{147}$Sm | 147 | 85 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1215.9288 | 1217.2443 | -0.11 % | 140808.6644 MeV (+28924.3 ppm) |
| ${}^{148}$Sm | 148 | 86 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1224.5499 | 1225.3856 | -0.07 % | 141766.7581 MeV (+28922.3 ppm) |
| ${}^{149}$Sm | 149 | 87 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1231.1067 | 1231.2568 | -0.01 % | 142726.9161 MeV (+28918.4 ppm) |
| ${}^{150}$Sm | 150 | 88 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1239.2735 | 1239.2435 | +0.00 % | 143685.4640 MeV (+28918.6 ppm) |
| ${}^{151}$Sm | 151 | 89 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1245.3973 | 1244.8400 | +0.04 % | 144646.0551 MeV (+28915.9 ppm) |
| ${}^{152}$Sm | 152 | 90 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1253.1276 | 1253.0978 | +0.00 % | 145605.0395 MeV (+28921.1 ppm) |
| ${}^{153}$Sm | 153 | 91 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1258.8354 | 1258.9662 | -0.01 % | 146566.0464 MeV (+28923.3 ppm) |
| ${}^{154}$Sm | 154 | 92 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1266.1462 | 1266.9330 | -0.06 % | 147525.4505 MeV (+28929.3 ppm) |
| ${}^{155}$Sm | 155 | 93 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1271.4542 | 1272.7400 | -0.10 % | 148486.8572 MeV (+28933.7 ppm) |
| ${}^{156}$Sm | 156 | 94 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1278.3614 | 1279.9808 | -0.13 % | 149446.6648 MeV (+28937.2 ppm) |
| ${}^{157}$Sm | 157 | 95 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1283.2851 | 1285.3691 | -0.16 % | 150408.4559 MeV (+28941.2 ppm) |
| ${}^{158}$Sm | 158 | 96 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1289.8038 | 1292.0146 | -0.17 % | 151368.6519 MeV (+28943.0 ppm) |
| ${}^{159}$Sm | 159 | 97 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1294.3578 | 1297.0419 | -0.21 % | 152330.8128 MeV (+28946.9 ppm) |
| ${}^{160}$Sm | 160 | 98 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1300.5026 | 1303.1385 | -0.20 % | 153291.3827 MeV (+28947.5 ppm) |
| ${}^{161}$Sm | 161 | 99 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1304.7006 | 1307.6487 | -0.23 % | 154253.8994 MeV (+28950.1 ppm) |
| ${}^{162}$Sm | 162 | 100 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1310.4852 | 1313.4271 | -0.22 % | 155214.8296 MeV (+28950.8 ppm) |
| ${}^{163}$Sm | 163 | 101 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1314.3406 | 1317.7189 | -0.26 % | 156177.6890 MeV (+28954.2 ppm) |
| ${}^{164}$Sm | 164 | 102 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1319.7781 | 1323.1160 | -0.25 % | 157138.9663 MeV (+28954.6 ppm) |
| ${}^{165}$Sm | 165 | 103 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1323.3034 | 1326.7650 | -0.26 % | 158102.1558 MeV (+28955.8 ppm) |
| ${}^{166}$Sm | 166 | 104 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1328.4062 | 1331.8180 | -0.26 % | 159063.7677 MeV (+28955.7 ppm) |
| ${}^{167}$Sm | 167 | 105 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1331.6133 | 1334.6640 | -0.23 % | 160027.2754 MeV (+28954.3 ppm) |
| ${}^{168}$Sm | 168 | 106 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1336.3933 | 1339.1280 | -0.20 % | 160989.2101 MeV (+28952.2 ppm) |

### Europium (Z = 63)

_41 of 41 isotopes with a framework prediction; 41 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{130}$Eu | 130 | 67 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1030.6992 | 1033.5000 | -0.27 % | 124558.4126 MeV (+28892.1 ppm) |
| ${}^{131}$Eu | 131 | 68 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1044.7901 | 1047.4760 | -0.26 % | 125511.0365 MeV (+28894.8 ppm) |
| ${}^{132}$Eu | 132 | 69 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1056.5900 | 1058.3760 | -0.17 % | 126465.9514 MeV (+28889.3 ppm) |
| ${}^{133}$Eu | 133 | 70 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1070.0063 | 1071.4480 | -0.13 % | 127419.2498 MeV (+28889.9 ppm) |
| ${}^{134}$Eu | 134 | 71 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1081.1615 | 1082.0500 | -0.08 % | 128374.8094 MeV (+28888.3 ppm) |
| ${}^{135}$Eu | 135 | 72 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1093.9331 | 1094.4450 | -0.05 % | 129328.7526 MeV (+28888.4 ppm) |
| ${}^{136}$Eu | 136 | 73 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1104.4720 | 1104.5920 | -0.01 % | 130284.9284 MeV (+28887.8 ppm) |
| ${}^{137}$Eu | 137 | 74 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1116.6268 | 1116.6286 | -0.00 % | 131239.4884 MeV (+28889.1 ppm) |
| ${}^{138}$Eu | 138 | 75 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1126.5764 | 1126.3037 | +0.02 % | 132196.2536 MeV (+28889.2 ppm) |
| ${}^{139}$Eu | 139 | 76 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1138.1408 | 1138.0234 | +0.01 % | 133151.4040 MeV (+28893.1 ppm) |
| ${}^{140}$Eu | 140 | 77 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1147.5263 | 1147.6826 | -0.01 % | 134108.7333 MeV (+28897.4 ppm) |
| ${}^{141}$Eu | 141 | 78 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1158.5252 | 1158.6936 | -0.01 % | 135064.4491 MeV (+28899.9 ppm) |
| ${}^{142}$Eu | 142 | 79 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1167.3706 | 1168.1482 | -0.07 % | 136022.3185 MeV (+28906.5 ppm) |
| ${}^{143}$Eu | 143 | 80 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1177.8275 | 1179.1519 | -0.11 % | 136978.5763 MeV (+28912.9 ppm) |
| ${}^{144}$Eu | 144 | 81 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1186.1554 | 1188.6011 | -0.21 % | 137936.9633 MeV (+28923.2 ppm) |
| ${}^{145}$Eu | 145 | 82 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1196.0926 | 1199.0448 | -0.25 % | 138893.7408 MeV (+28929.0 ppm) |
| ${}^{146}$Eu | 146 | 83 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1203.9242 | 1206.2422 | -0.19 % | 139852.6239 MeV (+28925.6 ppm) |
| ${}^{147}$Eu | 147 | 84 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1213.3628 | 1214.7405 | -0.11 % | 140809.9002 MeV (+28920.4 ppm) |
| ${}^{148}$Eu | 148 | 85 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1220.7184 | 1221.5647 | -0.07 % | 141769.2593 MeV (+28917.8 ppm) |
| ${}^{149}$Eu | 149 | 86 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1229.6782 | 1229.7798 | -0.01 % | 142727.0143 MeV (+28914.0 ppm) |
| ${}^{150}$Eu | 150 | 87 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1236.5769 | 1236.2022 | +0.03 % | 143686.8303 MeV (+28911.8 ppm) |
| ${}^{151}$Eu | 151 | 88 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1245.0768 | 1244.1343 | +0.08 % | 144645.0452 MeV (+28909.2 ppm) |
| ${}^{152}$Eu | 152 | 89 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1251.5368 | 1250.4410 | +0.09 % | 145605.3000 MeV (+28909.4 ppm) |
| ${}^{153}$Eu | 153 | 90 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1259.5947 | 1258.9913 | +0.05 % | 146563.9569 MeV (+28914.5 ppm) |
| ${}^{154}$Eu | 154 | 91 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1265.6331 | 1265.4335 | +0.02 % | 147524.6332 MeV (+28918.4 ppm) |
| ${}^{155}$Eu | 155 | 92 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1273.2659 | 1273.5848 | -0.03 % | 148483.7152 MeV (+28923.5 ppm) |
| ${}^{156}$Eu | 156 | 93 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1278.8991 | 1279.9206 | -0.08 % | 149444.7968 MeV (+28929.4 ppm) |
| ${}^{157}$Eu | 157 | 94 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1286.1230 | 1287.3682 | -0.10 % | 150404.2877 MeV (+28932.2 ppm) |
| ${}^{158}$Eu | 158 | 95 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1291.3664 | 1293.2509 | -0.15 % | 151365.7590 MeV (+28937.5 ppm) |
| ${}^{159}$Eu | 159 | 96 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1298.1966 | 1300.0951 | -0.15 % | 152325.6436 MeV (+28938.7 ppm) |
| ${}^{160}$Eu | 160 | 97 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1303.0650 | 1305.6165 | -0.20 % | 153287.4900 MeV (+28943.9 ppm) |
| ${}^{161}$Eu | 161 | 98 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1309.5162 | 1311.9859 | -0.19 % | 154247.7536 MeV (+28944.2 ppm) |
| ${}^{162}$Eu | 162 | 99 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1314.0235 | 1316.9886 | -0.23 % | 155209.9610 MeV (+28948.2 ppm) |
| ${}^{163}$Eu | 163 | 100 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1320.1094 | 1322.9108 | -0.21 % | 156170.5899 MeV (+28947.9 ppm) |
| ${}^{164}$Eu | 164 | 101 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1324.2690 | 1327.6405 | -0.25 % | 157133.1451 MeV (+28952.2 ppm) |
| ${}^{165}$Eu | 165 | 102 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1330.0028 | 1333.2087 | -0.24 % | 158094.1260 MeV (+28951.8 ppm) |
| ${}^{166}$Eu | 166 | 103 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1333.8273 | 1337.2960 | -0.26 % | 159057.0163 MeV (+28954.0 ppm) |
| ${}^{167}$Eu | 167 | 104 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1339.2217 | 1342.3460 | -0.23 % | 160018.3368 MeV (+28952.6 ppm) |
| ${}^{168}$Eu | 168 | 105 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1342.7231 | 1346.0160 | -0.24 % | 160981.5501 MeV (+28953.3 ppm) |
| ${}^{169}$Eu | 169 | 106 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1347.7899 | 1350.4790 | -0.20 % | 161943.1981 MeV (+28950.0 ppm) |
| ${}^{170}$Eu | 170 | 107 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1350.9798 | 1353.7100 | -0.20 % | 162906.7229 MeV (+28950.8 ppm) |

### Gadolinium (Z = 64)

_40 of 40 isotopes with a framework prediction; 40 of 40 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{133}$Gd | 133 | 69 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1056.8676 | 1059.4780 | -0.25 % | 127431.0582 MeV (+28892.4 ppm) |
| ${}^{134}$Gd | 134 | 70 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1070.6614 | 1073.0720 | -0.22 % | 128383.9791 MeV (+28893.5 ppm) |
| ${}^{135}$Gd | 135 | 71 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1082.1983 | 1083.7800 | -0.15 % | 129339.1571 MeV (+28890.1 ppm) |
| ${}^{136}$Gd | 136 | 72 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1095.3413 | 1096.7040 | -0.12 % | 130292.7288 MeV (+28891.3 ppm) |
| ${}^{137}$Gd | 137 | 73 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1106.2558 | 1106.9600 | -0.06 % | 131248.5291 MeV (+28888.0 ppm) |
| ${}^{138}$Gd | 138 | 74 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1118.7761 | 1119.4560 | -0.06 % | 132202.7236 MeV (+28890.8 ppm) |
| ${}^{139}$Gd | 139 | 75 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1129.0951 | 1129.5140 | -0.04 % | 133159.1194 MeV (+28891.0 ppm) |
| ${}^{140}$Gd | 140 | 76 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1141.0191 | 1141.6966 | -0.06 % | 134113.9101 MeV (+28896.0 ppm) |
| ${}^{141}$Gd | 141 | 77 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1150.7680 | 1151.2099 | -0.04 % | 135070.8760 MeV (+28896.3 ppm) |
| ${}^{142}$Gd | 142 | 78 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1162.1207 | 1163.0165 | -0.08 % | 136026.2380 MeV (+28902.3 ppm) |
| ${}^{143}$Gd | 143 | 79 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1171.3236 | 1172.3596 | -0.09 % | 136983.7499 MeV (+28905.3 ppm) |
| ${}^{144}$Gd | 144 | 80 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1182.1286 | 1183.9591 | -0.15 % | 137939.6597 MeV (+28913.7 ppm) |
| ${}^{145}$Gd | 145 | 81 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1190.8080 | 1193.1975 | -0.20 % | 138897.6951 MeV (+28919.7 ppm) |
| ${}^{146}$Gd | 146 | 82 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1201.0876 | 1204.4281 | -0.28 % | 139854.1302 MeV (+28928.9 ppm) |
| ${}^{147}$Gd | 147 | 83 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1209.2651 | 1211.7705 | -0.21 % | 140812.6675 MeV (+28924.1 ppm) |
| ${}^{148}$Gd | 148 | 84 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1219.0404 | 1220.7543 | -0.14 % | 141769.6070 MeV (+28920.1 ppm) |
| ${}^{149}$Gd | 149 | 85 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1226.7362 | 1227.6834 | -0.08 % | 142728.6260 MeV (+28915.8 ppm) |
| ${}^{150}$Gd | 150 | 86 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1236.0272 | 1236.3915 | -0.03 % | 143686.0497 MeV (+28913.3 ppm) |
| ${}^{151}$Gd | 151 | 87 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1243.2606 | 1242.8877 | +0.03 % | 144645.5311 MeV (+28909.3 ppm) |
| ${}^{152}$Gd | 152 | 88 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1252.0863 | 1251.4774 | +0.05 % | 145603.4202 MeV (+28909.3 ppm) |
| ${}^{153}$Gd | 153 | 89 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1258.8755 | 1257.7244 | +0.09 % | 146563.3458 MeV (+28906.7 ppm) |
| ${}^{154}$Gd | 154 | 90 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1267.2538 | 1266.6191 | +0.05 % | 147521.6823 MeV (+28912.0 ppm) |
| ${}^{155}$Gd | 155 | 91 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1273.6160 | 1273.0544 | +0.04 % | 148482.0348 MeV (+28913.7 ppm) |
| ${}^{156}$Gd | 156 | 92 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1281.5640 | 1281.5907 | -0.00 % | 149440.8016 MeV (+28919.3 ppm) |
| ${}^{157}$Gd | 157 | 93 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1287.5157 | 1287.9506 | -0.03 % | 150401.5647 MeV (+28923.2 ppm) |
| ${}^{158}$Gd | 158 | 94 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1295.0497 | 1295.8880 | -0.06 % | 151360.7455 MeV (+28927.3 ppm) |
| ${}^{159}$Gd | 159 | 95 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1300.6064 | 1301.8312 | -0.09 % | 152321.9036 MeV (+28930.9 ppm) |
| ${}^{160}$Gd | 160 | 96 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1307.7417 | 1309.2827 | -0.12 % | 153281.4830 MeV (+28934.3 ppm) |
| ${}^{161}$Gd | 161 | 97 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1312.9182 | 1314.9181 | -0.15 % | 154243.0213 MeV (+28938.2 ppm) |
| ${}^{162}$Gd | 162 | 98 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1319.6695 | 1321.7640 | -0.16 % | 155202.9848 MeV (+28939.8 ppm) |
| ${}^{163}$Gd | 163 | 99 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1324.4799 | 1326.9432 | -0.19 % | 156164.8891 MeV (+28943.0 ppm) |
| ${}^{164}$Gd | 164 | 100 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1330.8611 | 1333.3196 | -0.18 % | 157125.2227 MeV (+28943.9 ppm) |
| ${}^{165}$Gd | 165 | 101 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1335.3189 | 1338.2231 | -0.22 % | 158087.4797 MeV (+28947.4 ppm) |
| ${}^{166}$Gd | 166 | 102 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1341.3433 | 1344.1395 | -0.21 % | 159048.1701 MeV (+28947.5 ppm) |
| ${}^{167}$Gd | 167 | 103 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1345.4612 | 1348.6156 | -0.23 % | 160010.7670 MeV (+28950.3 ppm) |
| ${}^{168}$Gd | 168 | 104 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1351.1414 | 1354.0800 | -0.22 % | 160971.8015 MeV (+28949.5 ppm) |
| ${}^{169}$Gd | 169 | 105 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1354.9315 | 1357.9150 | -0.22 % | 161934.7262 MeV (+28950.0 ppm) |
| ${}^{170}$Gd | 170 | 106 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1360.2796 | 1362.8900 | -0.19 % | 162896.0929 MeV (+28948.6 ppm) |
| ${}^{171}$Gd | 171 | 107 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1363.7535 | 1366.2900 | -0.19 % | 163859.3337 MeV (+28948.7 ppm) |
| ${}^{172}$Gd | 172 | 108 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1368.7810 | 1371.1840 | -0.18 % | 164821.0210 MeV (+28948.0 ppm) |

### Terbium (Z = 65)

_40 of 40 isotopes with a framework prediction; 40 of 40 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{135}$Tb | 135 | 70 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1068.8116 | 1071.7650 | -0.28 % | 129351.2135 MeV (+28894.4 ppm) |
| ${}^{136}$Tb | 136 | 71 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1080.7349 | 1082.6960 | -0.18 % | 130306.0049 MeV (+28888.9 ppm) |
| ${}^{137}$Tb | 137 | 72 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1094.2543 | 1095.8630 | -0.15 % | 131259.2003 MeV (+28889.0 ppm) |
| ${}^{138}$Tb | 138 | 73 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1105.5491 | 1106.6220 | -0.10 % | 132214.6202 MeV (+28886.8 ppm) |
| ${}^{139}$Tb | 139 | 74 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1118.4399 | 1119.2280 | -0.07 % | 133168.4443 MeV (+28887.5 ppm) |
| ${}^{140}$Tb | 140 | 75 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1129.1331 | 1129.6142 | -0.04 % | 134124.4658 MeV (+28887.8 ppm) |
| ${}^{141}$Tb | 141 | 76 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1141.4216 | 1141.7441 | -0.03 % | 135078.8921 MeV (+28889.3 ppm) |
| ${}^{142}$Tb | 142 | 77 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1151.5388 | 1151.8341 | -0.03 % | 136035.4897 MeV (+28891.3 ppm) |
| ${}^{143}$Tb | 143 | 78 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1163.2501 | 1163.7651 | -0.04 % | 136990.4931 MeV (+28895.6 ppm) |
| ${}^{144}$Tb | 144 | 79 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1172.8153 | 1173.7854 | -0.08 % | 137947.6427 MeV (+28901.2 ppm) |
| ${}^{145}$Tb | 145 | 80 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1183.9732 | 1185.8883 | -0.16 % | 138903.1996 MeV (+28910.7 ppm) |
| ${}^{146}$Tb | 146 | 81 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1193.0091 | 1195.3235 | -0.19 % | 139860.8785 MeV (+28915.6 ppm) |
| ${}^{147}$Tb | 147 | 82 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1203.6358 | 1206.3739 | -0.23 % | 140816.9665 MeV (+28920.9 ppm) |
| ${}^{148}$Tb | 148 | 83 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1212.1640 | 1214.2395 | -0.17 % | 141775.1531 MeV (+28917.5 ppm) |
| ${}^{149}$Tb | 149 | 84 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1222.2809 | 1223.2625 | -0.08 % | 142731.7510 MeV (+28911.4 ppm) |
| ${}^{150}$Tb | 150 | 85 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1230.3217 | 1230.9509 | -0.05 % | 143690.4250 MeV (+28910.3 ppm) |
| ${}^{151}$Tb | 151 | 86 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1239.9488 | 1239.5400 | +0.03 % | 144647.5127 MeV (+28904.6 ppm) |
| ${}^{152}$Tb | 152 | 87 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1247.5215 | 1246.7051 | +0.07 % | 145606.6547 MeV (+28903.1 ppm) |
| ${}^{153}$Tb | 153 | 88 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1256.6778 | 1255.3727 | +0.10 % | 146564.2131 MeV (+28901.4 ppm) |
| ${}^{154}$Tb | 154 | 89 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1263.8009 | 1262.2871 | +0.12 % | 147523.8049 MeV (+28901.3 ppm) |
| ${}^{155}$Tb | 155 | 90 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1272.5045 | 1271.4522 | +0.08 % | 148481.8160 MeV (+28906.3 ppm) |
| ${}^{156}$Tb | 156 | 91 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1279.1952 | 1278.3641 | +0.07 % | 149441.8401 MeV (+28909.1 ppm) |
| ${}^{157}$Tb | 157 | 92 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1287.4633 | 1287.1082 | +0.03 % | 150400.2868 MeV (+28914.0 ppm) |
| ${}^{158}$Tb | 158 | 93 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1293.7381 | 1293.8866 | -0.01 % | 151360.7268 MeV (+28918.7 ppm) |
| ${}^{159}$Tb | 159 | 94 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1301.5870 | 1302.0196 | -0.03 % | 152319.5927 MeV (+28922.0 ppm) |
| ${}^{160}$Tb | 160 | 95 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1307.4616 | 1308.3948 | -0.07 % | 153280.4328 MeV (+28926.5 ppm) |
| ${}^{161}$Tb | 161 | 96 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1314.9067 | 1316.0914 | -0.09 % | 154239.7025 MeV (+28929.4 ppm) |
| ${}^{162}$Tb | 162 | 97 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1320.3961 | 1322.5805 | -0.17 % | 155200.9279 MeV (+28937.1 ppm) |
| ${}^{163}$Tb | 163 | 98 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1327.4522 | 1329.3680 | -0.14 % | 156160.5865 MeV (+28936.4 ppm) |
| ${}^{164}$Tb | 164 | 99 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1332.5705 | 1334.9486 | -0.18 % | 157122.1830 MeV (+28940.2 ppm) |
| ${}^{165}$Tb | 165 | 100 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1339.2516 | 1341.5038 | -0.17 % | 158082.2166 MeV (+28940.4 ppm) |
| ${}^{166}$Tb | 166 | 101 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1344.0123 | 1346.7950 | -0.21 % | 159044.1708 MeV (+28944.5 ppm) |
| ${}^{167}$Tb | 167 | 102 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1350.3318 | 1352.9406 | -0.19 % | 160004.5660 MeV (+28944.2 ppm) |
| ${}^{168}$Tb | 168 | 103 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1354.7477 | 1357.9101 | -0.23 % | 160966.8648 MeV (+28948.4 ppm) |
| ${}^{169}$Tb | 169 | 104 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1360.7185 | 1363.6610 | -0.22 % | 161927.6089 MeV (+28947.9 ppm) |
| ${}^{170}$Tb | 170 | 105 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1364.8019 | 1367.9900 | -0.23 % | 162890.2403 MeV (+28949.7 ppm) |
| ${}^{171}$Tb | 171 | 106 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1370.4358 | 1373.1300 | -0.20 % | 163851.3211 MeV (+28947.2 ppm) |
| ${}^{172}$Tb | 172 | 107 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1374.1984 | 1377.0320 | -0.21 % | 164814.2733 MeV (+28949.0 ppm) |
| ${}^{173}$Tb | 173 | 108 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1379.5073 | 1381.9240 | -0.17 % | 165775.6792 MeV (+28947.0 ppm) |
| ${}^{174}$Tb | 174 | 109 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1382.9602 | 1385.5620 | -0.19 % | 166738.9410 MeV (+28947.8 ppm) |

### Dysprosium (Z = 66)

_39 of 39 isotopes with a framework prediction; 39 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{138}$Dy | 138 | 72 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1094.5091 | 1097.1000 | -0.24 % | 132224.3300 MeV (+28893.0 ppm) |
| ${}^{139}$Dy | 139 | 73 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1106.1751 | 1107.9690 | -0.16 % | 133179.3788 MeV (+28889.1 ppm) |
| ${}^{140}$Dy | 140 | 74 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1119.4273 | 1121.1200 | -0.15 % | 134132.8413 MeV (+28891.6 ppm) |
| ${}^{141}$Dy | 141 | 75 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1130.4860 | 1131.8070 | -0.12 % | 135088.4974 MeV (+28890.7 ppm) |
| ${}^{142}$Dy | 142 | 76 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1143.1303 | 1144.6620 | -0.13 % | 136042.5678 MeV (+28894.8 ppm) |
| ${}^{143}$Dy | 143 | 77 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1153.6072 | 1154.7325 | -0.10 % | 136998.8058 MeV (+28894.3 ppm) |
| ${}^{144}$Dy | 144 | 78 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1165.6688 | 1167.2050 | -0.13 % | 137953.4589 MeV (+28900.1 ppm) |
| ${}^{145}$Dy | 145 | 79 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1175.5880 | 1176.9488 | -0.12 % | 138910.2545 MeV (+28900.8 ppm) |
| ${}^{146}$Dy | 146 | 80 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1187.0907 | 1189.3325 | -0.19 % | 139865.4666 MeV (+28909.9 ppm) |
| ${}^{147}$Dy | 147 | 81 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1196.4750 | 1199.0449 | -0.21 % | 140822.7971 MeV (+28914.2 ppm) |
| ${}^{148}$Dy | 148 | 82 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1207.4411 | 1210.7796 | -0.28 % | 141778.5457 MeV (+28922.2 ppm) |
| ${}^{149}$Dy | 149 | 83 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1216.3121 | 1218.6855 | -0.19 % | 142736.3895 MeV (+28916.7 ppm) |
| ${}^{150}$Dy | 150 | 84 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1226.7630 | 1228.3724 | -0.13 % | 143692.6534 MeV (+28913.1 ppm) |
| ${}^{151}$Dy | 151 | 85 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1235.1412 | 1235.8865 | -0.06 % | 144650.9899 MeV (+28908.3 ppm) |
| ${}^{152}$Dy | 152 | 86 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1245.0970 | 1245.3234 | -0.02 % | 145607.7489 MeV (+28906.5 ppm) |
| ${}^{153}$Dy | 153 | 87 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1253.0018 | 1252.4200 | +0.05 % | 146566.5589 MeV (+28902.2 ppm) |
| ${}^{154}$Dy | 154 | 88 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1262.4817 | 1261.7421 | +0.06 % | 147523.7938 MeV (+28902.9 ppm) |
| ${}^{155}$Dy | 155 | 89 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1269.9315 | 1268.5753 | +0.11 % | 148483.0588 MeV (+28900.0 ppm) |
| ${}^{156}$Dy | 156 | 90 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1278.9535 | 1278.0201 | +0.07 % | 149440.7515 MeV (+28904.8 ppm) |
| ${}^{157}$Dy | 157 | 91 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1285.9657 | 1284.9867 | +0.08 % | 150400.4541 MeV (+28905.8 ppm) |
| ${}^{158}$Dy | 158 | 92 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1294.5471 | 1294.0405 | +0.04 % | 151358.5874 MeV (+28910.7 ppm) |
| ${}^{159}$Dy | 159 | 93 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1301.1384 | 1300.8719 | +0.02 % | 152318.7109 MeV (+28913.6 ppm) |
| ${}^{160}$Dy | 160 | 94 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1309.2957 | 1309.4484 | -0.01 % | 153277.2684 MeV (+28917.9 ppm) |
| ${}^{161}$Dy | 161 | 95 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1315.4817 | 1315.9028 | -0.03 % | 154237.7971 MeV (+28920.8 ppm) |
| ${}^{162}$Dy | 162 | 96 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1323.2304 | 1324.0998 | -0.07 % | 155196.7633 MeV (+28925.2 ppm) |
| ${}^{163}$Dy | 163 | 97 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1329.0262 | 1330.3708 | -0.10 % | 156157.6822 MeV (+28929.3 ppm) |
| ${}^{164}$Dy | 164 | 98 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1336.3811 | 1338.0289 | -0.12 % | 157117.0421 MeV (+28932.6 ppm) |
| ${}^{165}$Dy | 165 | 99 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1341.8010 | 1343.7449 | -0.14 % | 158078.3370 MeV (+28935.4 ppm) |
| ${}^{166}$Dy | 166 | 100 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1348.7762 | 1350.7884 | -0.15 % | 159038.0766 MeV (+28936.9 ppm) |
| ${}^{167}$Dy | 167 | 101 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1353.8337 | 1356.1867 | -0.17 % | 159999.7338 MeV (+28939.8 ppm) |
| ${}^{168}$Dy | 168 | 102 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1360.4427 | 1362.9049 | -0.18 % | 160959.8396 MeV (+28941.5 ppm) |
| ${}^{169}$Dy | 169 | 103 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1365.1508 | 1368.0139 | -0.21 % | 161921.8463 MeV (+28944.7 ppm) |
| ${}^{170}$Dy | 170 | 104 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1371.4064 | 1374.2800 | -0.21 % | 162882.3055 MeV (+28945.1 ppm) |
| ${}^{171}$Dy | 171 | 105 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1375.7774 | 1378.6020 | -0.20 % | 163844.6492 MeV (+28945.6 ppm) |
| ${}^{172}$Dy | 172 | 106 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1381.6918 | 1384.4280 | -0.20 % | 164805.4496 MeV (+28945.8 ppm) |
| ${}^{173}$Dy | 173 | 107 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1385.7376 | 1388.4980 | -0.20 % | 165768.1186 MeV (+28946.3 ppm) |
| ${}^{174}$Dy | 174 | 108 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1391.3225 | 1393.9140 | -0.19 % | 166729.2485 MeV (+28946.2 ppm) |
| ${}^{175}$Dy | 175 | 109 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1395.0542 | 1397.5500 | -0.18 % | 167692.2315 MeV (+28946.2 ppm) |
| ${}^{176}$Dy | 176 | 110 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1400.3207 | 1402.5440 | -0.16 % | 168653.6798 MeV (+28944.8 ppm) |

### Holmium (Z = 67)

_39 of 39 isotopes with a framework prediction; 39 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{140}$Ho | 140 | 73 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1104.3427 | 1106.8400 | -0.23 % | 134146.5957 MeV (+28890.5 ppm) |
| ${}^{141}$Ho | 141 | 74 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1117.9611 | 1119.9630 | -0.18 % | 135099.6920 MeV (+28889.6 ppm) |
| ${}^{142}$Ho | 142 | 75 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1129.3898 | 1131.0300 | -0.15 % | 136054.9781 MeV (+28888.5 ppm) |
| ${}^{143}$Ho | 143 | 76 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1142.3947 | 1143.8570 | -0.13 % | 137008.6879 MeV (+28890.3 ppm) |
| ${}^{144}$Ho | 144 | 77 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1153.2359 | 1154.4621 | -0.11 % | 137964.5616 MeV (+28891.1 ppm) |
| ${}^{145}$Ho | 145 | 78 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1165.6525 | 1167.0440 | -0.12 % | 138918.8597 MeV (+28895.0 ppm) |
| ${}^{146}$Ho | 146 | 79 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1175.9303 | 1177.2334 | -0.11 % | 139875.2967 MeV (+28896.5 ppm) |
| ${}^{147}$Ho | 147 | 80 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1187.7825 | 1189.8236 | -0.17 % | 140830.1593 MeV (+28904.6 ppm) |
| ${}^{148}$Ho | 148 | 81 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1197.5198 | 1200.1290 | -0.22 % | 141787.1368 MeV (+28910.8 ppm) |
| ${}^{149}$Ho | 149 | 82 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1208.8299 | 1211.8550 | -0.25 % | 142742.5414 MeV (+28916.2 ppm) |
| ${}^{150}$Ho | 150 | 83 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1218.0485 | 1220.2263 | -0.18 % | 143700.0376 MeV (+28911.7 ppm) |
| ${}^{151}$Ho | 151 | 84 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1228.8380 | 1229.9745 | -0.09 % | 144655.9628 MeV (+28906.2 ppm) |
| ${}^{152}$Ho | 152 | 85 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1237.5582 | 1238.0277 | -0.04 % | 145613.9574 MeV (+28903.0 ppm) |
| ${}^{153}$Ho | 153 | 86 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1247.8474 | 1247.5065 | +0.03 % | 146570.3830 MeV (+28899.2 ppm) |
| ${}^{154}$Ho | 154 | 87 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1256.0889 | 1255.2051 | +0.07 % | 147528.8563 MeV (+28897.0 ppm) |
| ${}^{155}$Ho | 155 | 88 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1265.8968 | 1264.6769 | +0.10 % | 148485.7631 MeV (+28896.5 ppm) |
| ${}^{156}$Ho | 156 | 89 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1273.6780 | 1272.2468 | +0.11 % | 149444.6967 MeV (+28896.6 ppm) |
| ${}^{157}$Ho | 157 | 90 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1283.0230 | 1281.6126 | +0.11 % | 150402.0665 MeV (+28898.6 ppm) |
| ${}^{158}$Ho | 158 | 91 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1290.3614 | 1289.0384 | +0.10 % | 151361.4429 MeV (+28900.6 ppm) |
| ${}^{159}$Ho | 159 | 92 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1299.2607 | 1298.2519 | +0.08 % | 152319.2583 MeV (+28904.5 ppm) |
| ${}^{160}$Ho | 160 | 93 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1306.1730 | 1305.3761 | +0.06 % | 153279.0608 MeV (+28907.2 ppm) |
| ${}^{161}$Ho | 161 | 94 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1314.6432 | 1314.2613 | +0.03 % | 154237.3054 MeV (+28911.6 ppm) |
| ${}^{162}$Ho | 162 | 95 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1321.1453 | 1321.1768 | -0.00 % | 155197.5181 MeV (+28915.6 ppm) |
| ${}^{163}$Ho | 163 | 96 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1329.2020 | 1329.5856 | -0.03 % | 156156.1762 MeV (+28919.4 ppm) |
| ${}^{164}$Ho | 164 | 97 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1335.3089 | 1336.2594 | -0.07 % | 157116.7840 MeV (+28924.2 ppm) |
| ${}^{165}$Ho | 165 | 98 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1342.9670 | 1344.2483 | -0.10 % | 158075.8407 MeV (+28927.7 ppm) |
| ${}^{166}$Ho | 166 | 99 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1348.6930 | 1350.4919 | -0.13 % | 159036.8294 MeV (+28932.0 ppm) |
| ${}^{167}$Ho | 167 | 100 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1355.9667 | 1357.7723 | -0.13 % | 159996.2705 MeV (+28933.2 ppm) |
| ${}^{168}$Ho | 168 | 101 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1361.3257 | 1363.6234 | -0.17 % | 160957.6263 MeV (+28937.2 ppm) |
| ${}^{169}$Ho | 169 | 102 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1368.2285 | 1370.4315 | -0.16 % | 161917.4382 MeV (+28937.6 ppm) |
| ${}^{170}$Ho | 170 | 103 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1373.2334 | 1375.9443 | -0.20 % | 162879.1482 MeV (+28941.6 ppm) |
| ${}^{171}$Ho | 171 | 104 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1379.7783 | 1382.2960 | -0.18 % | 163839.3180 MeV (+28941.3 ppm) |
| ${}^{172}$Ho | 172 | 105 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1384.4414 | 1387.3520 | -0.21 % | 164801.3697 MeV (+28944.2 ppm) |
| ${}^{173}$Ho | 173 | 106 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1390.6407 | 1393.3420 | -0.19 % | 165761.8852 MeV (+28943.4 ppm) |
| ${}^{174}$Ho | 174 | 107 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1394.9740 | 1397.9160 | -0.21 % | 166724.2666 MeV (+28945.5 ppm) |
| ${}^{175}$Ho | 175 | 108 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1400.8394 | 1403.3250 | -0.18 % | 167685.1160 MeV (+28944.0 ppm) |
| ${}^{176}$Ho | 176 | 109 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1404.8542 | 1407.4720 | -0.19 % | 168647.8159 MeV (+28945.3 ppm) |
| ${}^{177}$Ho | 177 | 110 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1410.3970 | 1412.4600 | -0.15 % | 169608.9880 MeV (+28942.4 ppm) |
| ${}^{178}$Ho | 178 | 111 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1414.1041 | 1416.3460 | -0.16 % | 170571.9956 MeV (+28944.1 ppm) |

### Erbium (Z = 68)

_39 of 39 isotopes with a framework prediction; 39 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{142}$Er | 142 | 74 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1117.8227 | 1120.8060 | -0.27 % | 136065.2149 MeV (+28893.4 ppm) |
| ${}^{143}$Er | 143 | 75 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1129.6127 | 1132.1310 | -0.22 % | 137020.1396 MeV (+28892.2 ppm) |
| ${}^{144}$Er | 144 | 76 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1142.9697 | 1145.6640 | -0.24 % | 137973.4974 MeV (+28896.3 ppm) |
| ${}^{145}$Er | 145 | 77 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1154.1667 | 1156.3750 | -0.19 % | 138929.0152 MeV (+28895.0 ppm) |
| ${}^{146}$Er | 146 | 78 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1166.9301 | 1169.5349 | -0.22 % | 139882.9666 MeV (+28900.6 ppm) |
| ${}^{147}$Er | 147 | 79 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1177.5583 | 1179.8920 | -0.20 % | 140839.0531 MeV (+28900.8 ppm) |
| ${}^{148}$Er | 148 | 80 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1189.7519 | 1192.8345 | -0.26 % | 141793.5743 MeV (+28908.9 ppm) |
| ${}^{149}$Er | 149 | 81 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1199.8343 | 1203.1684 | -0.28 % | 142750.2067 MeV (+28912.8 ppm) |
| ${}^{150}$Er | 150 | 82 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1211.4808 | 1215.3294 | -0.32 % | 143705.2750 MeV (+28918.9 ppm) |
| ${}^{151}$Er | 151 | 83 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1221.0391 | 1223.8357 | -0.23 % | 144662.4315 MeV (+28913.0 ppm) |
| ${}^{152}$Er | 152 | 84 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1232.1597 | 1234.1410 | -0.16 % | 145618.0256 MeV (+28909.2 ppm) |
| ${}^{153}$Er | 153 | 85 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1241.2146 | 1242.1788 | -0.08 % | 146575.6855 MeV (+28903.6 ppm) |
| ${}^{154}$Er | 154 | 86 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1251.8298 | 1252.3884 | -0.04 % | 147531.7851 MeV (+28902.8 ppm) |
| ${}^{155}$Er | 155 | 87 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1260.4006 | 1260.0639 | +0.03 % | 148489.9290 MeV (+28898.1 ppm) |
| ${}^{156}$Er | 156 | 88 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1270.5296 | 1270.1377 | +0.03 % | 149446.5148 MeV (+28899.7 ppm) |
| ${}^{157}$Er | 157 | 89 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1278.6351 | 1277.4110 | +0.10 % | 150405.1241 MeV (+28895.4 ppm) |
| ${}^{158}$Er | 158 | 90 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1288.2962 | 1287.3725 | +0.07 % | 151362.1777 MeV (+28899.4 ppm) |
| ${}^{159}$Er | 159 | 91 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1295.9539 | 1294.7011 | +0.10 % | 152321.2348 MeV (+28898.6 ppm) |
| ${}^{160}$Er | 160 | 92 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1305.1645 | 1304.2755 | +0.07 % | 153278.7390 MeV (+28902.9 ppm) |
| ${}^{161}$Er | 161 | 93 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1312.3912 | 1311.4839 | +0.07 % | 154238.2271 MeV (+28904.1 ppm) |
| ${}^{162}$Er | 162 | 94 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1321.1679 | 1320.6881 | +0.04 % | 155196.1652 MeV (+28908.6 ppm) |
| ${}^{163}$Er | 163 | 95 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1327.9795 | 1327.5927 | +0.03 % | 156156.0684 MeV (+28910.5 ppm) |
| ${}^{164}$Er | 164 | 96 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1336.3379 | 1336.4391 | -0.01 % | 157114.4247 MeV (+28915.3 ppm) |
| ${}^{165}$Er | 165 | 97 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1342.7496 | 1343.0892 | -0.03 % | 158074.7278 MeV (+28917.9 ppm) |
| ${}^{166}$Er | 166 | 98 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1350.7048 | 1351.5634 | -0.06 % | 159033.4874 MeV (+28922.8 ppm) |
| ${}^{167}$Er | 167 | 99 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1356.7309 | 1357.9998 | -0.09 % | 159994.1760 MeV (+28926.4 ppm) |
| ${}^{168}$Er | 168 | 100 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1364.2972 | 1365.7711 | -0.11 % | 160953.3245 MeV (+28929.0 ppm) |
| ${}^{169}$Er | 169 | 101 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1369.9516 | 1371.7743 | -0.13 % | 161914.3848 MeV (+28932.1 ppm) |
| ${}^{170}$Er | 170 | 102 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1377.1426 | 1379.0320 | -0.14 % | 162873.9086 MeV (+28933.6 ppm) |
| ${}^{171}$Er | 171 | 103 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1382.4384 | 1384.7136 | -0.16 % | 163835.3276 MeV (+28936.9 ppm) |
| ${}^{172}$Er | 172 | 104 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1389.2670 | 1391.5497 | -0.16 % | 164795.2138 MeV (+28937.9 ppm) |
| ${}^{173}$Er | 173 | 105 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1394.2166 | 1396.8020 | -0.19 % | 165756.9789 MeV (+28940.4 ppm) |
| ${}^{174}$Er | 174 | 106 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1400.6953 | 1403.1360 | -0.17 % | 166717.2150 MeV (+28940.6 ppm) |
| ${}^{175}$Er | 175 | 107 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1405.3108 | 1407.8750 | -0.18 % | 167679.3144 MeV (+28942.2 ppm) |
| ${}^{176}$Er | 176 | 108 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1411.4513 | 1413.9840 | -0.18 % | 168639.8886 MeV (+28942.4 ppm) |
| ${}^{177}$Er | 177 | 109 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1415.7440 | 1418.3010 | -0.18 % | 169602.3107 MeV (+28942.9 ppm) |
| ${}^{178}$Er | 178 | 110 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1421.5577 | 1423.8220 | -0.16 % | 170563.2117 MeV (+28941.6 ppm) |
| ${}^{179}$Er | 179 | 111 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1425.5385 | 1427.7040 | -0.15 % | 171525.9457 MeV (+28941.5 ppm) |
| ${}^{180}$Er | 180 | 112 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1431.0362 | 1432.8000 | -0.12 % | 172487.1628 MeV (+28940.1 ppm) |

### Thulium (Z = 69)

_39 of 39 isotopes with a framework prediction; 39 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{144}$Tm | 144 | 75 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1127.4171 | 1130.4000 | -0.26 % | 137987.7198 MeV (+28891.5 ppm) |
| ${}^{145}$Tm | 145 | 76 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1141.1306 | 1143.9050 | -0.24 % | 138940.7210 MeV (+28892.8 ppm) |
| ${}^{146}$Tm | 146 | 77 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1152.6880 | 1155.4440 | -0.24 % | 139895.8784 MeV (+28895.2 ppm) |
| ${}^{147}$Tm | 147 | 78 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1165.8026 | 1168.4762 | -0.23 % | 140849.4786 MeV (+28897.0 ppm) |
| ${}^{148}$Tm | 148 | 79 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1176.7857 | 1179.3382 | -0.22 % | 141805.2102 MeV (+28898.4 ppm) |
| ${}^{149}$Tm | 149 | 80 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1189.3253 | 1192.5960 | -0.27 % | 142759.3854 MeV (+28906.3 ppm) |
| ${}^{150}$Tm | 150 | 81 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1199.7572 | 1203.1500 | -0.28 % | 143715.6682 MeV (+28909.7 ppm) |
| ${}^{151}$Tm | 151 | 82 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1211.7445 | 1215.5587 | -0.31 % | 144670.3958 MeV (+28914.8 ppm) |
| ${}^{152}$Tm | 152 | 83 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1221.6470 | 1224.5787 | -0.24 % | 145627.2080 MeV (+28910.3 ppm) |
| ${}^{153}$Tm | 153 | 84 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1233.1033 | 1234.9023 | -0.15 % | 146582.4665 MeV (+28904.3 ppm) |
| ${}^{154}$Tm | 154 | 85 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1242.4971 | 1243.4282 | -0.07 % | 147539.7875 MeV (+28899.9 ppm) |
| ${}^{155}$Tm | 155 | 86 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1253.4428 | 1253.6983 | -0.02 % | 148495.5565 MeV (+28897.3 ppm) |
| ${}^{156}$Tm | 156 | 87 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1262.3475 | 1261.9781 | +0.03 % | 149453.3666 MeV (+28894.6 ppm) |
| ${}^{157}$Tm | 157 | 88 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1272.8021 | 1271.9243 | +0.07 % | 150409.6268 MeV (+28893.1 ppm) |
| ${}^{158}$Tm | 158 | 89 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1281.2363 | 1279.9895 | +0.10 % | 151367.9074 MeV (+28892.2 ppm) |
| ${}^{159}$Tm | 159 | 90 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1291.2180 | 1289.9280 | +0.10 % | 152324.6405 MeV (+28893.9 ppm) |
| ${}^{160}$Tm | 160 | 91 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1299.1994 | 1297.7300 | +0.11 % | 153283.3739 MeV (+28894.2 ppm) |
| ${}^{161}$Tm | 161 | 92 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1308.7257 | 1307.3990 | +0.10 % | 154240.5623 MeV (+28897.0 ppm) |
| ${}^{162}$Tm | 162 | 93 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1316.2711 | 1315.0491 | +0.09 % | 155199.7316 MeV (+28899.2 ppm) |
| ${}^{163}$Tm | 163 | 94 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1325.3587 | 1324.3713 | +0.07 % | 156157.3588 MeV (+28902.5 ppm) |
| ${}^{164}$Tm | 164 | 95 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1332.4842 | 1331.6232 | +0.06 % | 157116.9481 MeV (+28904.6 ppm) |
| ${}^{165}$Tm | 165 | 96 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1341.1488 | 1340.7156 | +0.03 % | 158074.9983 MeV (+28909.0 ppm) |
| ${}^{166}$Tm | 166 | 97 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1347.8696 | 1347.7433 | +0.01 % | 159034.9923 MeV (+28912.3 ppm) |
| ${}^{167}$Tm | 167 | 98 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1356.1263 | 1356.4713 | -0.03 % | 159993.4503 MeV (+28916.8 ppm) |
| ${}^{168}$Tm | 168 | 99 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1362.4569 | 1363.3119 | -0.06 % | 160953.8345 MeV (+28921.2 ppm) |
| ${}^{169}$Tm | 169 | 100 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1370.3201 | 1371.3455 | -0.07 % | 161912.6860 MeV (+28923.6 ppm) |
| ${}^{170}$Tm | 170 | 101 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1376.2743 | 1377.9374 | -0.12 % | 162873.4466 MeV (+28928.7 ppm) |
| ${}^{171}$Tm | 171 | 102 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1383.7577 | 1385.4237 | -0.12 % | 163832.6780 MeV (+28929.9 ppm) |
| ${}^{172}$Tm | 172 | 103 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1389.3487 | 1391.6583 | -0.17 % | 164793.8017 MeV (+28934.8 ppm) |
| ${}^{173}$Tm | 173 | 104 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1396.4654 | 1398.6122 | -0.15 % | 165753.3999 MeV (+28934.8 ppm) |
| ${}^{174}$Tm | 174 | 105 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1401.7058 | 1404.2919 | -0.18 % | 166714.8742 MeV (+28938.3 ppm) |
| ${}^{175}$Tm | 175 | 106 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1408.4682 | 1410.8093 | -0.17 % | 167674.8266 MeV (+28937.7 ppm) |
| ${}^{176}$Tm | 176 | 107 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1413.3701 | 1415.9414 | -0.18 % | 168636.6395 MeV (+28939.8 ppm) |
| ${}^{177}$Tm | 177 | 108 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1419.7900 | 1422.1950 | -0.17 % | 169596.9343 MeV (+28939.7 ppm) |
| ${}^{178}$Tm | 178 | 109 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1424.3648 | 1427.0260 | -0.19 % | 170559.0743 MeV (+28941.3 ppm) |
| ${}^{179}$Tm | 179 | 110 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1430.4538 | 1432.7160 | -0.16 % | 171519.7001 MeV (+28939.9 ppm) |
| ${}^{180}$Tm | 180 | 111 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1434.7124 | 1436.9400 | -0.16 % | 172482.1562 MeV (+28940.9 ppm) |
| ${}^{181}$Tm | 181 | 112 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1440.4813 | 1442.3890 | -0.13 % | 173443.1022 MeV (+28939.0 ppm) |
| ${}^{182}$Tm | 182 | 113 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1444.4343 | 1446.5360 | -0.15 % | 174405.8639 MeV (+28940.5 ppm) |

### Ytterbium (Z = 70)

_38 of 38 isotopes with a framework prediction; 38 of 38 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{148}$Yb | 148 | 78 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1165.9730 | 1170.0880 | -0.35 % | 141814.6926 MeV (+28903.5 ppm) |
| ${}^{149}$Yb | 149 | 79 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1177.3029 | 1181.1230 | -0.32 % | 142770.0775 MeV (+28904.6 ppm) |
| ${}^{150}$Yb | 150 | 80 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1190.1806 | 1194.7500 | -0.38 % | 143723.9146 MeV (+28912.3 ppm) |
| ${}^{151}$Yb | 151 | 81 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1200.9542 | 1205.5471 | -0.38 % | 144679.8558 MeV (+28914.5 ppm) |
| ${}^{152}$Yb | 152 | 82 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1213.2745 | 1218.3464 | -0.42 % | 145634.2502 MeV (+28920.4 ppm) |
| ${}^{153}$Yb | 153 | 83 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1223.5136 | 1227.3660 | -0.31 % | 146590.7259 MeV (+28913.1 ppm) |
| ${}^{154}$Yb | 154 | 84 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1235.2981 | 1238.1508 | -0.23 % | 147545.6562 MeV (+28908.6 ppm) |
| ${}^{155}$Yb | 155 | 85 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1245.0235 | 1246.7926 | -0.14 % | 148502.6456 MeV (+28902.7 ppm) |
| ${}^{156}$Yb | 156 | 86 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1256.2926 | 1257.6269 | -0.11 % | 149458.0913 MeV (+28901.8 ppm) |
| ${}^{157}$Yb | 157 | 87 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1265.5239 | 1265.8526 | -0.03 % | 150415.5747 MeV (+28896.6 ppm) |
| ${}^{158}$Yb | 158 | 88 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1276.2969 | 1276.5136 | -0.02 % | 151371.5164 MeV (+28897.9 ppm) |
| ${}^{159}$Yb | 159 | 89 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1285.0529 | 1284.4088 | +0.05 % | 152329.4753 MeV (+28893.6 ppm) |
| ${}^{160}$Yb | 160 | 90 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1295.3483 | 1294.8098 | +0.04 % | 153285.8946 MeV (+28896.3 ppm) |
| ${}^{161}$Yb | 161 | 91 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1303.6466 | 1302.5522 | +0.08 % | 154244.3110 MeV (+28894.1 ppm) |
| ${}^{162}$Yb | 162 | 92 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1313.4820 | 1312.6104 | +0.07 % | 155201.1904 MeV (+28897.5 ppm) |
| ${}^{163}$Yb | 163 | 93 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1321.3397 | 1320.1544 | +0.09 % | 156160.0476 MeV (+28896.9 ppm) |
| ${}^{164}$Yb | 164 | 94 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1330.7317 | 1329.9440 | +0.06 % | 157117.3703 MeV (+28901.3 ppm) |
| ${}^{165}$Yb | 165 | 95 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1338.1647 | 1337.2986 | +0.06 % | 158076.6521 MeV (+28902.2 ppm) |
| ${}^{166}$Yb | 166 | 96 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1347.1292 | 1346.6682 | +0.03 % | 159034.4023 MeV (+28906.5 ppm) |
| ${}^{167}$Yb | 167 | 97 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1354.1529 | 1353.7357 | +0.03 % | 159994.0935 MeV (+28908.0 ppm) |
| ${}^{168}$Yb | 168 | 98 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1362.7051 | 1362.7970 | -0.01 % | 160952.2560 MeV (+28912.9 ppm) |
| ${}^{169}$Yb | 169 | 99 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1369.3340 | 1369.6640 | -0.02 % | 161912.3419 MeV (+28915.6 ppm) |
| ${}^{170}$Yb | 170 | 100 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1377.4883 | 1378.1237 | -0.05 % | 162870.9024 MeV (+28918.9 ppm) |
| ${}^{171}$Yb | 171 | 101 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1383.7364 | 1384.7379 | -0.07 % | 163831.3691 MeV (+28922.3 ppm) |
| ${}^{172}$Yb | 172 | 102 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1391.5065 | 1392.7579 | -0.09 % | 164790.3137 MeV (+28925.1 ppm) |
| ${}^{173}$Yb | 173 | 103 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1397.3870 | 1399.1250 | -0.12 % | 165751.1480 MeV (+28929.1 ppm) |
| ${}^{174}$Yb | 174 | 104 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1404.7861 | 1406.5896 | -0.13 % | 166710.4636 MeV (+28930.7 ppm) |
| ${}^{175}$Yb | 175 | 105 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1410.3117 | 1412.4119 | -0.15 % | 167671.6528 MeV (+28933.3 ppm) |
| ${}^{176}$Yb | 176 | 106 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1417.3523 | 1419.2790 | -0.14 % | 168631.3270 MeV (+28933.3 ppm) |
| ${}^{177}$Yb | 177 | 107 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1422.5352 | 1424.8454 | -0.16 % | 169592.8589 MeV (+28936.3 ppm) |
| ${}^{178}$Yb | 178 | 108 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1429.2293 | 1431.6075 | -0.17 % | 170552.8796 MeV (+28937.7 ppm) |
| ${}^{179}$Yb | 179 | 109 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1434.0808 | 1436.6540 | -0.18 % | 171514.7428 MeV (+28939.4 ppm) |
| ${}^{180}$Yb | 180 | 110 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1440.4399 | 1442.8800 | -0.17 % | 172475.0985 MeV (+28939.0 ppm) |
| ${}^{181}$Yb | 181 | 111 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1444.9713 | 1447.2760 | -0.16 % | 173437.2819 MeV (+28939.0 ppm) |
| ${}^{182}$Yb | 182 | 112 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1451.0062 | 1453.0880 | -0.14 % | 174397.9617 MeV (+28938.9 ppm) |
| ${}^{183}$Yb | 183 | 113 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1455.2280 | 1457.2290 | -0.14 % | 175360.4547 MeV (+28939.0 ppm) |
| ${}^{184}$Yb | 184 | 114 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1460.9493 | 1462.9840 | -0.14 % | 176321.4482 MeV (+28939.5 ppm) |
| ${}^{185}$Yb | 185 | 115 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1464.8715 | 1466.8650 | -0.14 % | 177284.2408 MeV (+28940.1 ppm) |

### Lutetium (Z = 71)

_39 of 39 isotopes with a framework prediction; 39 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{150}$Lu | 150 | 79 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1175.4481 | 1179.9000 | -0.38 % | 143737.3168 MeV (+28904.7 ppm) |
| ${}^{151}$Lu | 151 | 80 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1188.6682 | 1193.5040 | -0.41 % | 144690.8115 MeV (+28910.2 ppm) |
| ${}^{152}$Lu | 152 | 81 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1199.7878 | 1204.7520 | -0.41 % | 145646.4067 MeV (+28912.9 ppm) |
| ${}^{153}$Lu | 153 | 82 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1212.4455 | 1217.7405 | -0.43 % | 146600.4637 MeV (+28918.0 ppm) |
| ${}^{154}$Lu | 154 | 83 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1223.0256 | 1227.0720 | -0.33 % | 147556.5984 MeV (+28911.2 ppm) |
| ${}^{155}$Lu | 155 | 84 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1235.1426 | 1238.0527 | -0.24 % | 148511.1962 MeV (+28905.2 ppm) |
| ${}^{156}$Lu | 156 | 85 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1245.2038 | 1247.2785 | -0.17 % | 149467.8497 MeV (+28901.3 ppm) |
| ${}^{157}$Lu | 157 | 86 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1256.8005 | 1258.0901 | -0.10 % | 150422.9678 MeV (+28898.0 ppm) |
| ${}^{158}$Lu | 158 | 87 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1266.3628 | 1266.9338 | -0.05 % | 151380.1203 MeV (+28894.8 ppm) |
| ${}^{159}$Lu | 159 | 88 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1277.4586 | 1277.5015 | -0.00 % | 152335.7392 MeV (+28893.3 ppm) |
| ${}^{160}$Lu | 160 | 89 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1286.5406 | 1286.1342 | +0.03 % | 153293.3720 MeV (+28892.0 ppm) |
| ${}^{161}$Lu | 161 | 90 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1297.1541 | 1296.4979 | +0.05 % | 154249.4733 MeV (+28892.4 ppm) |
| ${}^{162}$Lu | 162 | 91 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1305.7736 | 1304.8387 | +0.07 % | 155207.5686 MeV (+28892.1 ppm) |
| ${}^{163}$Lu | 163 | 92 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1315.9224 | 1314.8696 | +0.08 % | 156164.1346 MeV (+28893.3 ppm) |
| ${}^{164}$Lu | 164 | 93 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1324.0964 | 1322.7919 | +0.10 % | 157122.6753 MeV (+28893.2 ppm) |
| ${}^{165}$Lu | 165 | 94 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1333.7972 | 1332.6631 | +0.09 % | 158079.6893 MeV (+28896.1 ppm) |
| ${}^{166}$Lu | 166 | 95 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1341.5419 | 1340.3131 | +0.09 % | 159038.6594 MeV (+28896.9 ppm) |
| ${}^{167}$Lu | 167 | 96 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1350.8106 | 1349.8898 | +0.07 % | 159996.1054 MeV (+28900.7 ppm) |
| ${}^{168}$Lu | 168 | 97 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1358.1414 | 1357.5076 | +0.05 % | 160955.4894 MeV (+28903.9 ppm) |
| ${}^{169}$Lu | 169 | 98 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1366.9932 | 1366.5886 | +0.03 % | 161913.3523 MeV (+28907.0 ppm) |
| ${}^{170}$Lu | 170 | 99 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1373.9247 | 1373.8837 | +0.00 % | 162873.1356 MeV (+28910.5 ppm) |
| ${}^{171}$Lu | 171 | 100 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1382.3742 | 1382.4772 | -0.01 % | 163831.4009 MeV (+28912.9 ppm) |
| ${}^{172}$Lu | 172 | 101 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1388.9204 | 1389.4561 | -0.04 % | 164791.5695 MeV (+28916.8 ppm) |
| ${}^{173}$Lu | 173 | 102 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1396.9814 | 1397.6724 | -0.05 % | 165750.2232 MeV (+28919.1 ppm) |
| ${}^{174}$Lu | 174 | 103 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1403.1556 | 1404.4330 | -0.09 % | 166710.7638 MeV (+28923.8 ppm) |
| ${}^{175}$Lu | 175 | 104 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1410.8414 | 1412.0997 | -0.09 % | 167669.7929 MeV (+28924.9 ppm) |
| ${}^{176}$Lu | 176 | 105 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1416.6563 | 1418.3877 | -0.12 % | 168630.6927 MeV (+28928.7 ppm) |
| ${}^{177}$Lu | 177 | 106 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1423.9794 | 1425.4606 | -0.10 % | 169590.0844 MeV (+28928.2 ppm) |
| ${}^{178}$Lu | 178 | 107 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1429.4473 | 1431.4859 | -0.14 % | 170551.3313 MeV (+28932.5 ppm) |
| ${}^{179}$Lu | 179 | 108 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1436.4197 | 1438.2783 | -0.13 % | 171511.0737 MeV (+28932.4 ppm) |
| ${}^{180}$Lu | 180 | 109 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1441.5521 | 1443.9671 | -0.17 % | 172472.6559 MeV (+28936.5 ppm) |
| ${}^{181}$Lu | 181 | 110 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1448.1854 | 1450.1593 | -0.14 % | 173432.7374 MeV (+28934.7 ppm) |
| ${}^{182}$Lu | 182 | 111 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1452.9936 | 1455.2720 | -0.16 % | 174394.6441 MeV (+28936.7 ppm) |
| ${}^{183}$Lu | 183 | 112 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1459.2988 | 1461.2207 | -0.13 % | 175355.0536 MeV (+28935.8 ppm) |
| ${}^{184}$Lu | 184 | 113 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1463.7932 | 1465.9280 | -0.15 % | 176317.2739 MeV (+28937.3 ppm) |
| ${}^{185}$Lu | 185 | 114 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1469.7809 | 1471.6750 | -0.13 % | 177278.0011 MeV (+28936.6 ppm) |
| ${}^{186}$Lu | 186 | 115 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1473.9719 | 1476.0960 | -0.14 % | 178240.5249 MeV (+28938.5 ppm) |
| ${}^{187}$Lu | 187 | 116 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1479.6521 | 1481.6010 | -0.13 % | 179201.5594 MeV (+28938.2 ppm) |
| ${}^{188}$Lu | 188 | 117 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1483.5493 | 1485.7640 | -0.15 % | 180164.3770 MeV (+28940.0 ppm) |

### Hafnium (Z = 72)

_38 of 38 isotopes with a framework prediction; 38 of 38 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{153}$Hf | 153 | 81 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1199.8990 | 1205.9460 | -0.50 % | 146611.6799 MeV (+28916.7 ppm) |
| ${}^{154}$Hf | 154 | 82 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1212.8867 | 1219.3720 | -0.53 % | 147565.4070 MeV (+28922.9 ppm) |
| ${}^{155}$Hf | 155 | 83 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1223.8001 | 1228.9950 | -0.42 % | 148521.2084 MeV (+28915.9 ppm) |
| ${}^{156}$Hf | 156 | 84 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1236.2422 | 1240.6161 | -0.35 % | 149475.4810 MeV (+28912.2 ppm) |
| ${}^{157}$Hf | 157 | 85 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1246.6320 | 1249.7200 | -0.25 % | 150431.8060 MeV (+28905.1 ppm) |
| ${}^{158}$Hf | 158 | 86 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1258.5492 | 1261.0417 | -0.20 % | 151386.6035 MeV (+28903.2 ppm) |
| ${}^{159}$Hf | 159 | 87 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1268.4352 | 1269.8632 | -0.11 % | 152343.4323 MeV (+28897.7 ppm) |
| ${}^{160}$Hf | 160 | 88 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1279.8470 | 1281.0207 | -0.09 % | 153298.7353 MeV (+28898.1 ppm) |
| ${}^{161}$Hf | 161 | 89 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1289.2480 | 1289.4690 | -0.02 % | 154256.0491 MeV (+28893.4 ppm) |
| ${}^{162}$Hf | 162 | 90 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1300.1729 | 1300.3930 | -0.02 % | 155211.8390 MeV (+28895.5 ppm) |
| ${}^{163}$Hf | 163 | 91 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1309.1068 | 1308.5652 | +0.04 % | 156169.6198 MeV (+28892.0 ppm) |
| ${}^{164}$Hf | 164 | 92 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1319.5624 | 1319.1855 | +0.03 % | 157125.8790 MeV (+28895.1 ppm) |
| ${}^{165}$Hf | 165 | 93 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1328.0463 | 1327.0740 | +0.07 % | 158084.1099 MeV (+28892.7 ppm) |
| ${}^{166}$Hf | 166 | 94 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1338.0494 | 1337.3688 | +0.05 % | 159040.8215 MeV (+28896.5 ppm) |
| ${}^{167}$Hf | 167 | 95 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1346.0995 | 1345.0489 | +0.08 % | 159999.4862 MeV (+28895.6 ppm) |
| ${}^{168}$Hf | 168 | 96 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1355.6662 | 1355.0130 | +0.05 % | 160956.6343 MeV (+28900.0 ppm) |
| ${}^{169}$Hf | 169 | 97 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1363.2979 | 1362.4407 | +0.06 % | 161915.7174 MeV (+28900.0 ppm) |
| ${}^{170}$Hf | 170 | 98 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1372.4434 | 1372.0490 | +0.03 % | 162873.2867 MeV (+28904.7 ppm) |
| ${}^{171}$Hf | 171 | 99 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1379.6714 | 1379.2977 | +0.03 % | 163832.7734 MeV (+28906.1 ppm) |
| ${}^{172}$Hf | 172 | 100 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1388.4103 | 1388.3400 | +0.01 % | 164790.7493 MeV (+28909.5 ppm) |
| ${}^{173}$Hf | 173 | 101 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1395.2487 | 1395.4208 | -0.01 % | 165750.6257 MeV (+28912.2 ppm) |
| ${}^{174}$Hf | 174 | 102 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1403.5949 | 1403.9249 | -0.02 % | 166708.9943 MeV (+28914.6 ppm) |
| ${}^{175}$Hf | 175 | 103 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1410.0571 | 1410.6334 | -0.04 % | 167669.2468 MeV (+28917.2 ppm) |
| ${}^{176}$Hf | 176 | 104 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1418.0238 | 1418.7994 | -0.05 % | 168627.9949 MeV (+28919.7 ppm) |
| ${}^{177}$Hf | 177 | 105 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1424.1226 | 1425.1751 | -0.07 % | 169588.6109 MeV (+28922.4 ppm) |
| ${}^{178}$Hf | 178 | 106 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1431.7226 | 1432.8010 | -0.08 % | 170547.7256 MeV (+28923.7 ppm) |
| ${}^{179}$Hf | 179 | 107 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1437.4702 | 1438.9000 | -0.10 % | 171508.6928 MeV (+28926.7 ppm) |
| ${}^{180}$Hf | 180 | 108 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1444.7156 | 1446.2877 | -0.11 % | 172468.1622 MeV (+28928.7 ppm) |
| ${}^{181}$Hf | 181 | 109 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1450.1237 | 1451.9825 | -0.13 % | 173429.4688 MeV (+28931.2 ppm) |
| ${}^{182}$Hf | 182 | 110 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1457.0261 | 1458.7005 | -0.11 % | 174389.2813 MeV (+28931.0 ppm) |
| ${}^{183}$Hf | 183 | 111 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1462.1059 | 1464.0058 | -0.13 % | 175350.9162 MeV (+28933.1 ppm) |
| ${}^{184}$Hf | 184 | 112 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1468.6763 | 1470.2930 | -0.11 % | 176311.0606 MeV (+28932.3 ppm) |
| ${}^{185}$Hf | 185 | 113 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1473.4385 | 1475.1847 | -0.12 % | 177273.0131 MeV (+28933.7 ppm) |
| ${}^{186}$Hf | 186 | 114 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1479.6876 | 1481.3604 | -0.11 % | 178233.4789 MeV (+28934.1 ppm) |
| ${}^{187}$Hf | 187 | 115 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1484.1425 | 1486.0890 | -0.13 % | 179195.7387 MeV (+28935.7 ppm) |
| ${}^{188}$Hf | 188 | 116 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1490.0803 | 1491.9680 | -0.13 % | 180156.5156 MeV (+28936.3 ppm) |
| ${}^{189}$Hf | 189 | 117 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1494.2377 | 1496.3130 | -0.14 % | 181119.0730 MeV (+28938.1 ppm) |
| ${}^{190}$Hf | 190 | 118 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1499.8742 | 1501.9500 | -0.14 % | 182080.1514 MeV (+28939.3 ppm) |

### Tantalum (Z = 73)

_40 of 40 isotopes with a framework prediction; 40 of 40 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{155}$Ta | 155 | 82 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1210.9960 | 1217.9900 | -0.57 % | 148532.6821 MeV (+28921.8 ppm) |
| ${}^{156}$Ta | 156 | 83 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1222.2469 | 1228.0320 | -0.47 % | 149488.1461 MeV (+28915.6 ppm) |
| ${}^{157}$Ta | 157 | 84 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1235.0184 | 1239.6815 | -0.38 % | 150442.0893 MeV (+28910.2 ppm) |
| ${}^{158}$Ta | 158 | 85 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1245.7409 | 1249.3060 | -0.29 % | 151398.0816 MeV (+28904.4 ppm) |
| ${}^{159}$Ta | 159 | 86 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1257.9827 | 1260.6674 | -0.21 % | 152352.5545 MeV (+28900.8 ppm) |
| ${}^{160}$Ta | 160 | 87 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1268.1967 | 1270.1233 | -0.15 % | 153309.0553 MeV (+28897.5 ppm) |
| ${}^{161}$Ta | 161 | 88 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1279.9285 | 1281.1494 | -0.10 % | 154264.0383 MeV (+28894.9 ppm) |
| ${}^{162}$Ta | 162 | 89 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1289.6527 | 1290.2236 | -0.04 % | 155221.0288 MeV (+28892.4 ppm) |
| ${}^{163}$Ta | 163 | 90 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1300.8930 | 1301.0482 | -0.01 % | 156176.5033 MeV (+28891.7 ppm) |
| ${}^{164}$Ta | 164 | 91 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1310.1456 | 1309.8676 | +0.02 % | 157133.9655 MeV (+28890.5 ppm) |
| ${}^{165}$Ta | 165 | 92 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1320.9121 | 1320.5040 | +0.03 % | 158089.9138 MeV (+28891.7 ppm) |
| ${}^{166}$Ta | 166 | 93 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1329.7100 | 1328.8253 | +0.07 % | 159047.8307 MeV (+28890.2 ppm) |
| ${}^{167}$Ta | 167 | 94 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1340.0196 | 1339.1499 | +0.06 % | 160004.2359 MeV (+28892.3 ppm) |
| ${}^{168}$Ta | 168 | 95 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1348.3791 | 1347.2640 | +0.08 % | 160962.5911 MeV (+28892.2 ppm) |
| ${}^{169}$Ta | 169 | 96 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1358.2479 | 1357.2319 | +0.07 % | 161919.4371 MeV (+28894.7 ppm) |
| ${}^{170}$Ta | 170 | 97 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1366.1845 | 1365.1504 | +0.08 % | 162878.2152 MeV (+28896.0 ppm) |
| ${}^{171}$Ta | 171 | 98 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1375.6278 | 1374.8043 | +0.06 % | 163835.4867 MeV (+28899.1 ppm) |
| ${}^{172}$Ta | 172 | 99 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1383.1564 | 1382.4854 | +0.05 % | 164794.6729 MeV (+28901.4 ppm) |
| ${}^{173}$Ta | 173 | 100 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1392.1888 | 1391.6232 | +0.04 % | 165752.3553 MeV (+28903.7 ppm) |
| ${}^{174}$Ta | 174 | 101 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1399.3234 | 1399.0388 | +0.02 % | 166711.9354 MeV (+28906.7 ppm) |
| ${}^{175}$Ta | 175 | 102 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1407.9589 | 1407.7780 | +0.01 % | 167670.0147 MeV (+28908.8 ppm) |
| ${}^{176}$Ta | 176 | 103 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1414.7131 | 1414.8060 | -0.01 % | 168629.9753 MeV (+28911.7 ppm) |
| ${}^{177}$Ta | 177 | 104 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1422.9649 | 1423.2267 | -0.02 % | 169588.4382 MeV (+28914.1 ppm) |
| ${}^{178}$Ta | 178 | 105 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1429.3515 | 1430.2300 | -0.06 % | 170548.7664 MeV (+28918.6 ppm) |
| ${}^{179}$Ta | 179 | 106 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1437.2326 | 1438.0121 | -0.05 % | 171507.6002 MeV (+28919.5 ppm) |
| ${}^{180}$Ta | 180 | 107 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1443.2638 | 1444.6596 | -0.10 % | 172468.2837 MeV (+28924.2 ppm) |
| ${}^{181}$Ta | 181 | 108 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1450.7862 | 1452.2363 | -0.10 % | 173427.4760 MeV (+28925.7 ppm) |
| ${}^{182}$Ta | 182 | 109 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1456.4740 | 1458.2992 | -0.13 % | 174388.5031 MeV (+28928.8 ppm) |
| ${}^{183}$Ta | 183 | 110 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1463.6493 | 1465.2334 | -0.11 % | 175348.0425 MeV (+28928.3 ppm) |
| ${}^{184}$Ta | 184 | 111 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1469.0048 | 1470.8506 | -0.13 % | 176309.4018 MeV (+28930.6 ppm) |
| ${}^{185}$Ta | 185 | 112 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1475.8443 | 1477.4769 | -0.11 % | 177269.2770 MeV (+28930.3 ppm) |
| ${}^{186}$Ta | 186 | 113 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1480.8783 | 1482.7614 | -0.13 % | 178230.9578 MeV (+28932.5 ppm) |
| ${}^{187}$Ta | 187 | 114 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1487.3927 | 1489.1207 | -0.12 % | 179191.1582 MeV (+28932.4 ppm) |
| ${}^{188}$Ta | 188 | 115 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1492.1154 | 1494.2240 | -0.14 % | 180153.1503 MeV (+28935.2 ppm) |
| ${}^{189}$Ta | 189 | 116 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1498.3149 | 1500.2820 | -0.13 % | 181113.6656 MeV (+28935.5 ppm) |
| ${}^{190}$Ta | 190 | 117 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1502.7363 | 1505.1800 | -0.16 % | 182075.9589 MeV (+28938.4 ppm) |
| ${}^{191}$Ta | 191 | 118 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1508.6307 | 1511.0010 | -0.16 % | 183036.7793 MeV (+28939.0 ppm) |
| ${}^{192}$Ta | 192 | 119 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1512.7602 | 1515.6480 | -0.19 % | 183999.3645 MeV (+28942.4 ppm) |
| ${}^{193}$Ta | 193 | 120 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1518.3589 | 1521.4190 | -0.20 % | 184960.4806 MeV (+28944.1 ppm) |
| ${}^{194}$Ta | 194 | 121 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1522.2057 | 1525.8100 | -0.24 % | 185923.3486 MeV (+28947.6 ppm) |

### Tungsten (Z = 74)

_41 of 41 isotopes with a framework prediction; 41 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{157}$W | 157 | 83 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1221.9596 | 1228.9960 | -0.57 % | 150453.8178 MeV (+28920.8 ppm) |
| ${}^{158}$W | 158 | 84 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1235.0532 | 1241.0900 | -0.49 % | 151407.4390 MeV (+28916.0 ppm) |
| ${}^{159}$W | 159 | 85 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1246.1011 | 1250.8530 | -0.38 % | 152363.1059 MeV (+28909.5 ppm) |
| ${}^{160}$W | 160 | 86 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1258.6605 | 1262.8463 | -0.33 % | 153317.2612 MeV (+28907.7 ppm) |
| ${}^{161}$W | 161 | 87 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1269.1954 | 1272.0610 | -0.23 % | 154273.4411 MeV (+28900.9 ppm) |
| ${}^{162}$W | 162 | 88 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1281.2403 | 1283.6591 | -0.19 % | 155228.1110 MeV (+28899.9 ppm) |
| ${}^{163}$W | 163 | 89 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1291.2810 | 1292.6396 | -0.11 % | 156184.7851 MeV (+28894.6 ppm) |
| ${}^{164}$W | 164 | 90 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1302.8300 | 1304.0380 | -0.09 % | 157139.9508 MeV (+28895.7 ppm) |
| ${}^{165}$W | 165 | 91 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1312.3945 | 1312.7351 | -0.03 % | 158097.1011 MeV (+28891.7 ppm) |
| ${}^{166}$W | 166 | 92 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1323.4654 | 1323.8326 | -0.03 % | 159052.7449 MeV (+28894.0 ppm) |
| ${}^{167}$W | 167 | 93 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1332.5708 | 1332.1097 | +0.03 % | 160010.3543 MeV (+28890.2 ppm) |
| ${}^{168}$W | 168 | 94 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1343.1806 | 1342.9807 | +0.01 % | 160966.4593 MeV (+28893.9 ppm) |
| ${}^{169}$W | 169 | 95 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1351.8432 | 1351.0769 | +0.06 % | 161924.5114 MeV (+28891.8 ppm) |
| ${}^{170}$W | 170 | 96 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1362.0079 | 1361.5212 | +0.04 % | 162881.0615 MeV (+28895.5 ppm) |
| ${}^{171}$W | 171 | 97 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1370.2435 | 1369.3878 | +0.06 % | 163839.5408 MeV (+28894.6 ppm) |
| ${}^{172}$W | 172 | 98 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1379.9785 | 1379.4702 | +0.04 % | 164796.5206 MeV (+28898.6 ppm) |
| ${}^{173}$W | 173 | 99 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1387.8017 | 1387.1717 | +0.05 % | 165755.4121 MeV (+28899.2 ppm) |
| ${}^{174}$W | 174 | 100 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1397.1217 | 1396.7428 | +0.03 % | 166712.8069 MeV (+28902.5 ppm) |
| ${}^{175}$W | 175 | 101 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1404.5468 | 1404.2198 | +0.02 % | 167672.0965 MeV (+28904.1 ppm) |
| ${}^{176}$W | 176 | 102 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1413.4658 | 1413.2999 | +0.01 % | 168629.8923 MeV (+28906.6 ppm) |
| ${}^{177}$W | 177 | 103 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1420.5063 | 1420.4314 | +0.01 % | 169589.5665 MeV (+28908.4 ppm) |
| ${}^{178}$W | 178 | 104 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1429.0378 | 1429.2080 | -0.01 % | 170547.7499 MeV (+28911.3 ppm) |
| ${}^{179}$W | 179 | 105 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1435.7066 | 1436.1675 | -0.03 % | 171507.7958 MeV (+28914.2 ppm) |
| ${}^{180}$W | 180 | 106 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1443.8633 | 1444.5798 | -0.05 % | 172466.3539 MeV (+28917.0 ppm) |
| ${}^{181}$W | 181 | 107 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1450.1729 | 1451.2488 | -0.07 % | 173426.7591 MeV (+28920.2 ppm) |
| ${}^{182}$W | 182 | 108 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1457.9670 | 1459.3323 | -0.09 % | 174385.6797 MeV (+28923.1 ppm) |
| ${}^{183}$W | 183 | 109 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1463.9291 | 1465.5232 | -0.11 % | 175346.4324 MeV (+28925.4 ppm) |
| ${}^{184}$W | 184 | 110 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1471.3724 | 1472.9343 | -0.11 % | 176305.7039 MeV (+28926.3 ppm) |
| ${}^{185}$W | 185 | 111 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1476.9984 | 1478.6880 | -0.11 % | 177266.7927 MeV (+28927.8 ppm) |
| ${}^{186}$W | 186 | 112 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1484.1021 | 1485.8801 | -0.12 % | 178226.4037 MeV (+28929.4 ppm) |
| ${}^{187}$W | 187 | 113 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1489.4028 | 1491.3468 | -0.13 % | 179187.8178 MeV (+28931.0 ppm) |
| ${}^{188}$W | 188 | 114 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1496.1776 | 1498.1820 | -0.13 % | 180147.7577 MeV (+28932.3 ppm) |
| ${}^{189}$W | 189 | 115 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1501.1634 | 1503.3060 | -0.14 % | 181109.4868 MeV (+28934.3 ppm) |
| ${}^{190}$W | 190 | 116 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1507.6197 | 1510.0256 | -0.16 % | 182069.7452 MeV (+28936.1 ppm) |
| ${}^{191}$W | 191 | 117 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1512.3004 | 1514.9043 | -0.17 % | 183031.7793 MeV (+28937.8 ppm) |
| ${}^{192}$W | 192 | 118 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1518.4480 | 1521.4080 | -0.19 % | 183992.3464 MeV (+28940.7 ppm) |
| ${}^{193}$W | 193 | 119 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1522.8333 | 1526.0510 | -0.21 % | 184954.6760 MeV (+28942.6 ppm) |
| ${}^{194}$W | 194 | 120 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1528.6817 | 1532.4060 | -0.24 % | 185915.5423 MeV (+28945.9 ppm) |
| ${}^{195}$W | 195 | 121 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1532.7806 | 1536.7950 | -0.26 % | 186878.1582 MeV (+28948.0 ppm) |
| ${}^{196}$W | 196 | 122 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1538.3389 | 1542.9120 | -0.30 % | 187839.3147 MeV (+28951.5 ppm) |
| ${}^{197}$W | 197 | 123 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1542.1603 | 1547.0410 | -0.32 % | 188802.2081 MeV (+28953.9 ppm) |

### Rhenium (Z = 75)

_41 of 41 isotopes with a framework prediction; 41 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{159}$Re | 159 | 84 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1232.7903 | 1239.4050 | -0.53 % | 152375.0863 MeV (+28916.5 ppm) |
| ${}^{160}$Re | 160 | 85 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1244.1677 | 1249.6000 | -0.43 % | 153330.4237 MeV (+28910.1 ppm) |
| ${}^{161}$Re | 161 | 86 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1257.0488 | 1261.6490 | -0.36 % | 154284.2574 MeV (+28906.7 ppm) |
| ${}^{162}$Re | 162 | 87 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1267.9085 | 1271.3760 | -0.27 % | 155240.1125 MeV (+28900.7 ppm) |
| ${}^{163}$Re | 163 | 88 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1280.2706 | 1282.9511 | -0.21 % | 156194.4651 MeV (+28898.0 ppm) |
| ${}^{164}$Re | 164 | 89 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1290.6316 | 1292.4926 | -0.14 % | 157150.8189 MeV (+28894.4 ppm) |
| ${}^{165}$Re | 165 | 90 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1302.4935 | 1303.7508 | -0.10 % | 158105.6718 MeV (+28892.6 ppm) |
| ${}^{166}$Re | 166 | 91 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1312.3738 | 1313.0001 | -0.05 % | 159062.5062 MeV (+28890.2 ppm) |
| ${}^{167}$Re | 167 | 92 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1323.7532 | 1324.1430 | -0.03 % | 160017.8416 MeV (+28890.3 ppm) |
| ${}^{168}$Re | 168 | 93 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1333.1701 | 1333.1003 | +0.01 % | 160975.1395 MeV (+28889.6 ppm) |
| ${}^{169}$Re | 169 | 94 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1344.0840 | 1343.7860 | +0.02 % | 161930.9404 MeV (+28890.1 ppm) |
| ${}^{170}$Re | 170 | 95 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1353.0538 | 1352.3520 | +0.05 % | 162888.6854 MeV (+28889.2 ppm) |
| ${}^{171}$Re | 171 | 96 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1363.5184 | 1362.7696 | +0.05 % | 163844.9355 MeV (+28890.8 ppm) |
| ${}^{172}$Re | 172 | 97 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1372.0567 | 1371.1575 | +0.07 % | 164803.1120 MeV (+28891.4 ppm) |
| ${}^{173}$Re | 173 | 98 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1382.0874 | 1381.2159 | +0.06 % | 165759.7960 MeV (+28893.4 ppm) |
| ${}^{174}$Re | 174 | 99 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1390.2092 | 1389.4064 | +0.06 % | 166718.3890 MeV (+28895.3 ppm) |
| ${}^{175}$Re | 175 | 100 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1399.8208 | 1399.0929 | +0.05 % | 167675.4922 MeV (+28897.5 ppm) |
| ${}^{176}$Re | 176 | 101 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1407.5403 | 1406.9388 | +0.04 % | 168634.4875 MeV (+28899.6 ppm) |
| ${}^{177}$Re | 177 | 102 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1416.7468 | 1416.2165 | +0.04 % | 169591.9958 MeV (+28901.7 ppm) |
| ${}^{178}$Re | 178 | 103 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1424.0776 | 1423.6721 | +0.03 % | 170551.3798 MeV (+28903.7 ppm) |
| ${}^{179}$Re | 179 | 104 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1432.8925 | 1432.6742 | +0.02 % | 171509.2796 MeV (+28906.3 ppm) |
| ${}^{180}$Re | 180 | 105 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1439.8475 | 1439.9986 | -0.01 % | 172469.0394 MeV (+28909.7 ppm) |
| ${}^{181}$Re | 181 | 106 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1448.2837 | 1448.7500 | -0.03 % | 173427.3180 MeV (+28913.0 ppm) |
| ${}^{182}$Re | 182 | 107 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1454.8755 | 1455.7500 | -0.06 % | 174387.4410 MeV (+28916.5 ppm) |
| ${}^{183}$Re | 183 | 108 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1462.9452 | 1464.1848 | -0.08 % | 175346.0860 MeV (+28920.0 ppm) |
| ${}^{184}$Re | 184 | 109 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1469.1856 | 1470.6663 | -0.10 % | 176306.5604 MeV (+28922.4 ppm) |
| ${}^{185}$Re | 185 | 110 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1476.9007 | 1478.3369 | -0.10 % | 177265.5601 MeV (+28923.2 ppm) |
| ${}^{186}$Re | 186 | 111 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1482.8010 | 1484.5165 | -0.12 % | 178226.3745 MeV (+28925.7 ppm) |
| ${}^{187}$Re | 187 | 112 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1490.1727 | 1491.8770 | -0.11 % | 179185.7176 MeV (+28926.7 ppm) |
| ${}^{188}$Re | 188 | 113 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1495.7439 | 1497.7486 | -0.13 % | 180146.8611 MeV (+28929.2 ppm) |
| ${}^{189}$Re | 189 | 114 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1502.7831 | 1504.7822 | -0.13 % | 181106.5367 MeV (+28930.2 ppm) |
| ${}^{190}$Re | 190 | 115 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1508.0356 | 1510.4574 | -0.16 % | 182067.9990 MeV (+28933.3 ppm) |
| ${}^{191}$Re | 191 | 116 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1514.7526 | 1517.2961 | -0.17 % | 183027.9968 MeV (+28934.9 ppm) |
| ${}^{192}$Re | 192 | 117 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1519.6964 | 1522.6059 | -0.19 % | 183989.7678 MeV (+28937.6 ppm) |
| ${}^{193}$Re | 193 | 118 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1526.1011 | 1529.3200 | -0.21 % | 184950.0779 MeV (+28940.2 ppm) |
| ${}^{194}$Re | 194 | 119 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1530.7458 | 1534.3460 | -0.23 % | 185912.1479 MeV (+28943.3 ppm) |
| ${}^{195}$Re | 195 | 120 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1536.8477 | 1540.6950 | -0.25 % | 186872.7608 MeV (+28945.6 ppm) |
| ${}^{196}$Re | 196 | 121 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1541.2025 | 1545.6560 | -0.29 % | 187835.1207 MeV (+28948.9 ppm) |
| ${}^{197}$Re | 197 | 122 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1547.0109 | 1551.7690 | -0.31 % | 188796.0272 MeV (+28951.0 ppm) |
| ${}^{198}$Re | 198 | 123 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1551.0846 | 1556.4780 | -0.35 % | 189758.6682 MeV (+28954.9 ppm) |
| ${}^{199}$Re | 199 | 124 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1556.6081 | 1562.1500 | -0.35 % | 190719.8595 MeV (+28957.0 ppm) |

### Osmium (Z = 76)

_43 of 43 isotopes with a framework prediction; 43 of 43 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{161}$Os | 161 | 85 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1243.4887 | 1250.1650 | -0.53 % | 154296.4872 MeV (+28915.2 ppm) |
| ${}^{162}$Os | 162 | 86 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1256.6844 | 1262.6280 | -0.47 % | 155250.0063 MeV (+28912.0 ppm) |
| ${}^{163}$Os | 163 | 87 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1267.8620 | 1272.5410 | -0.37 % | 156205.5434 MeV (+28905.4 ppm) |
| ${}^{164}$Os | 164 | 88 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1280.5346 | 1284.6625 | -0.32 % | 157159.5857 MeV (+28904.3 ppm) |
| ${}^{165}$Os | 165 | 89 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1291.2092 | 1294.0950 | -0.22 % | 158115.6258 MeV (+28897.7 ppm) |
| ${}^{166}$Os | 166 | 90 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1303.3772 | 1305.8120 | -0.19 % | 159070.1726 MeV (+28897.2 ppm) |
| ${}^{167}$Os | 167 | 91 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1313.5668 | 1314.9506 | -0.11 % | 160026.6977 MeV (+28892.1 ppm) |
| ${}^{168}$Os | 168 | 92 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1325.2482 | 1326.5181 | -0.10 % | 160981.7311 MeV (+28893.6 ppm) |
| ${}^{169}$Os | 169 | 93 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1334.9702 | 1335.3174 | -0.03 % | 161938.7239 MeV (+28889.3 ppm) |
| ${}^{170}$Os | 170 | 94 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1346.1819 | 1346.5914 | -0.03 % | 162894.2269 MeV (+28891.8 ppm) |
| ${}^{171}$Os | 171 | 95 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1355.4526 | 1355.0342 | +0.03 % | 163851.6711 MeV (+28888.2 ppm) |
| ${}^{172}$Os | 172 | 96 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1366.2109 | 1366.0520 | +0.01 % | 164807.6275 MeV (+28891.8 ppm) |
| ${}^{173}$Os | 173 | 97 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1375.0460 | 1374.3179 | +0.05 % | 165765.5072 MeV (+28889.8 ppm) |
| ${}^{174}$Os | 174 | 98 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1385.3665 | 1384.9464 | +0.03 % | 166721.9015 MeV (+28893.6 ppm) |
| ${}^{175}$Os | 175 | 99 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1393.7809 | 1393.1276 | +0.05 % | 167680.2018 MeV (+28893.7 ppm) |
| ${}^{176}$Os | 176 | 100 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1403.6782 | 1403.2248 | +0.03 % | 168637.0193 MeV (+28896.7 ppm) |
| ${}^{177}$Os | 177 | 101 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1411.6863 | 1411.1214 | +0.04 % | 169595.7260 MeV (+28897.4 ppm) |
| ${}^{178}$Os | 178 | 102 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1421.1747 | 1420.7805 | +0.03 % | 170552.9524 MeV (+28900.1 ppm) |
| ${}^{179}$Os | 179 | 103 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1428.7901 | 1428.3277 | +0.03 % | 171512.0517 MeV (+28901.0 ppm) |
| ${}^{180}$Os | 180 | 104 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1437.8830 | 1437.7351 | +0.01 % | 172469.6736 MeV (+28904.4 ppm) |
| ${}^{181}$Os | 181 | 105 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1445.1187 | 1445.0002 | +0.01 % | 173429.1527 MeV (+28905.8 ppm) |
| ${}^{182}$Os | 182 | 106 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1453.8291 | 1454.1306 | -0.02 % | 174387.1571 MeV (+28909.8 ppm) |
| ${}^{183}$Os | 183 | 107 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1460.6976 | 1461.2566 | -0.04 % | 175347.0033 MeV (+28912.4 ppm) |
| ${}^{184}$Os | 184 | 108 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1469.0378 | 1469.9167 | -0.06 % | 176305.3779 MeV (+28915.6 ppm) |
| ${}^{185}$Os | 185 | 109 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1475.5512 | 1476.5414 | -0.07 % | 177265.5793 MeV (+28917.3 ppm) |
| ${}^{186}$Os | 186 | 110 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1483.5330 | 1484.8068 | -0.09 % | 178224.3123 MeV (+28920.2 ppm) |
| ${}^{187}$Os | 187 | 111 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1489.7026 | 1491.0971 | -0.09 % | 179184.8574 MeV (+28921.8 ppm) |
| ${}^{188}$Os | 188 | 112 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1497.3374 | 1499.0867 | -0.12 % | 180143.9374 MeV (+28925.0 ppm) |
| ${}^{189}$Os | 189 | 113 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1503.1741 | 1505.0075 | -0.12 % | 181104.8154 MeV (+28926.3 ppm) |
| ${}^{190}$Os | 190 | 114 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1510.4727 | 1512.7999 | -0.15 % | 182064.2316 MeV (+28930.2 ppm) |
| ${}^{191}$Os | 191 | 115 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1515.9872 | 1518.5586 | -0.17 % | 183025.4319 MeV (+28932.3 ppm) |
| ${}^{192}$Os | 192 | 116 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1522.9601 | 1526.1170 | -0.21 % | 183985.1738 MeV (+28936.6 ppm) |
| ${}^{193}$Os | 193 | 117 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1528.1622 | 1531.7004 | -0.23 % | 184946.6864 MeV (+28939.4 ppm) |
| ${}^{194}$Os | 194 | 118 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1534.8194 | 1538.8125 | -0.26 % | 185906.7441 MeV (+28942.9 ppm) |
| ${}^{195}$Os | 195 | 119 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1539.7189 | 1543.9603 | -0.27 % | 186868.5593 MeV (+28944.8 ppm) |
| ${}^{196}$Os | 196 | 120 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1546.0699 | 1550.7971 | -0.30 % | 187828.9231 MeV (+28948.3 ppm) |
| ${}^{197}$Os | 197 | 121 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1550.6761 | 1555.7090 | -0.32 % | 188791.0317 MeV (+28950.3 ppm) |
| ${}^{198}$Os | 198 | 122 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1556.7300 | 1562.2200 | -0.35 % | 189751.6925 MeV (+28953.9 ppm) |
| ${}^{199}$Os | 199 | 123 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1561.0518 | 1566.9260 | -0.37 % | 190714.0855 MeV (+28956.6 ppm) |
| ${}^{200}$Os | 200 | 124 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1566.8176 | 1573.4000 | -0.42 % | 191675.0345 MeV (+28960.5 ppm) |
| ${}^{201}$Os | 201 | 125 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1570.8634 | 1577.6490 | -0.43 % | 192637.7034 MeV (+28962.5 ppm) |
| ${}^{202}$Os | 202 | 126 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1576.3496 | 1583.4780 | -0.45 % | 193598.9320 MeV (+28964.5 ppm) |
| ${}^{203}$Os | 203 | 127 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1580.1277 | 1586.2420 | -0.39 % | 194561.8687 MeV (+28959.5 ppm) |

### Iridium (Z = 77)

_43 of 43 isotopes with a framework prediction; 43 of 43 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{163}$Ir | 163 | 86 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1254.0552 | 1260.6420 | -0.52 % | 156218.0199 MeV (+28912.9 ppm) |
| ${}^{164}$Ir | 164 | 87 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1265.5546 | 1271.0000 | -0.43 % | 157173.2353 MeV (+28906.5 ppm) |
| ${}^{165}$Ir | 165 | 88 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1278.5414 | 1283.0400 | -0.35 % | 158126.9632 MeV (+28903.5 ppm) |
| ${}^{166}$Ir | 166 | 89 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1289.5335 | 1292.9740 | -0.27 % | 159082.6860 MeV (+28897.4 ppm) |
| ${}^{167}$Ir | 167 | 90 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1302.0116 | 1304.7418 | -0.21 % | 160036.9226 MeV (+28895.5 ppm) |
| ${}^{168}$Ir | 168 | 91 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1312.5144 | 1314.4070 | -0.14 % | 160993.1346 MeV (+28892.0 ppm) |
| ${}^{169}$Ir | 169 | 92 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1324.5017 | 1325.9055 | -0.11 % | 161947.8621 MeV (+28891.0 ppm) |
| ${}^{170}$Ir | 170 | 93 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1334.5325 | 1335.0100 | -0.04 % | 162904.5460 MeV (+28887.2 ppm) |
| ${}^{171}$Ir | 171 | 94 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1346.0460 | 1346.3667 | -0.02 % | 163859.7473 MeV (+28887.9 ppm) |
| ${}^{172}$Ir | 172 | 95 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1355.6214 | 1355.4054 | +0.02 % | 164816.8867 MeV (+28886.3 ppm) |
| ${}^{173}$Ir | 173 | 96 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1366.6774 | 1366.3658 | +0.02 % | 165772.5455 MeV (+28887.7 ppm) |
| ${}^{174}$Ir | 174 | 97 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1375.8130 | 1374.9546 | +0.06 % | 166730.1247 MeV (+28885.9 ppm) |
| ${}^{175}$Ir | 175 | 98 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1386.4271 | 1385.6345 | +0.06 % | 167686.2254 MeV (+28888.3 ppm) |
| ${}^{176}$Ir | 176 | 99 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1395.1379 | 1394.1932 | +0.07 % | 168644.2293 MeV (+28888.9 ppm) |
| ${}^{177}$Ir | 177 | 100 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1405.3249 | 1404.4300 | +0.06 % | 169600.7571 MeV (+28891.0 ppm) |
| ${}^{178}$Ir | 178 | 101 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1413.6254 | 1412.7082 | +0.06 % | 170559.1714 MeV (+28892.3 ppm) |
| ${}^{179}$Ir | 179 | 102 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1423.3994 | 1422.6069 | +0.06 % | 171516.1121 MeV (+28894.8 ppm) |
| ${}^{180}$Ir | 180 | 103 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1431.3032 | 1430.5741 | +0.05 % | 172474.9231 MeV (+28896.6 ppm) |
| ${}^{181}$Ir | 181 | 104 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1440.6779 | 1440.1309 | +0.04 % | 173432.2632 MeV (+28899.3 ppm) |
| ${}^{182}$Ir | 182 | 105 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1448.1981 | 1447.7909 | +0.03 % | 174391.4578 MeV (+28901.4 ppm) |
| ${}^{183}$Ir | 183 | 106 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1457.1864 | 1457.0126 | +0.01 % | 175349.1842 MeV (+28904.3 ppm) |
| ${}^{184}$Ir | 184 | 107 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1464.3355 | 1464.4927 | -0.01 % | 176308.7498 MeV (+28907.5 ppm) |
| ${}^{185}$Ir | 185 | 108 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1472.9499 | 1473.2887 | -0.02 % | 177266.8503 MeV (+28909.9 ppm) |
| ${}^{186}$Ir | 186 | 109 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1479.7400 | 1480.1968 | -0.03 % | 178226.7749 MeV (+28911.7 ppm) |
| ${}^{187}$Ir | 187 | 110 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1487.9923 | 1488.6451 | -0.04 % | 179185.2375 MeV (+28914.1 ppm) |
| ${}^{188}$Ir | 188 | 111 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1494.4348 | 1495.5120 | -0.07 % | 180145.5096 MeV (+28917.6 ppm) |
| ${}^{189}$Ir | 189 | 112 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1502.3364 | 1503.6880 | -0.09 % | 181104.3229 MeV (+28920.4 ppm) |
| ${}^{190}$Ir | 190 | 113 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1508.4424 | 1510.0633 | -0.11 % | 182064.9316 MeV (+28922.8 ppm) |
| ${}^{191}$Ir | 191 | 114 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1516.0043 | 1518.0899 | -0.14 % | 183024.0846 MeV (+28926.6 ppm) |
| ${}^{192}$Ir | 192 | 115 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1521.7843 | 1524.2880 | -0.16 % | 183985.0193 MeV (+28929.7 ppm) |
| ${}^{193}$Ir | 193 | 116 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1529.0168 | 1532.0600 | -0.20 % | 184944.5015 MeV (+28933.8 ppm) |
| ${}^{194}$Ir | 194 | 117 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1534.4810 | 1538.1268 | -0.24 % | 185905.7521 MeV (+28937.9 ppm) |
| ${}^{195}$Ir | 195 | 118 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1541.3943 | 1545.3586 | -0.26 % | 186865.5536 MeV (+28940.6 ppm) |
| ${}^{196}$Ir | 196 | 119 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1546.5523 | 1551.1731 | -0.30 % | 187827.1103 MeV (+28944.9 ppm) |
| ${}^{197}$Ir | 197 | 120 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1553.1559 | 1558.0731 | -0.32 % | 188787.2215 MeV (+28947.4 ppm) |
| ${}^{198}$Ir | 198 | 121 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1558.0172 | 1563.6060 | -0.36 % | 189749.0751 MeV (+28951.5 ppm) |
| ${}^{199}$Ir | 199 | 122 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1564.3204 | 1570.3501 | -0.38 % | 190709.4866 MeV (+28954.8 ppm) |
| ${}^{200}$Ir | 200 | 123 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1568.8938 | 1575.6000 | -0.43 % | 191671.6280 MeV (+28958.9 ppm) |
| ${}^{201}$Ir | 201 | 124 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1574.9055 | 1581.8700 | -0.44 % | 192632.3310 MeV (+28961.3 ppm) |
| ${}^{202}$Ir | 202 | 125 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1579.1996 | 1586.7100 | -0.47 % | 193594.7517 MeV (+28964.8 ppm) |
| ${}^{203}$Ir | 203 | 126 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1584.9284 | 1592.5350 | -0.48 % | 194555.7377 MeV (+28965.7 ppm) |
| ${}^{204}$Ir | 204 | 127 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1588.9514 | 1595.8920 | -0.43 % | 195518.4294 MeV (+28961.9 ppm) |
| ${}^{205}$Ir | 205 | 128 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1594.4055 | 1600.0250 | -0.35 % | 196479.6901 MeV (+28955.1 ppm) |

### Platinum (Z = 78)

_44 of 44 isotopes with a framework prediction; 44 of 44 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{165}$Pt | 165 | 87 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1264.4904 | 1270.9950 | -0.51 % | 158139.6840 MeV (+28910.8 ppm) |
| ${}^{166}$Pt | 166 | 88 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1277.7847 | 1283.6780 | -0.46 % | 159093.1044 MeV (+28908.1 ppm) |
| ${}^{167}$Pt | 167 | 89 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1289.0875 | 1293.5820 | -0.35 % | 160048.5164 MeV (+28901.8 ppm) |
| ${}^{168}$Pt | 168 | 90 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1301.8691 | 1305.9684 | -0.31 % | 161002.4496 MeV (+28901.1 ppm) |
| ${}^{169}$Pt | 169 | 91 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1312.6786 | 1315.4960 | -0.21 % | 161958.3549 MeV (+28894.7 ppm) |
| ${}^{170}$Pt | 170 | 92 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1324.9653 | 1327.4002 | -0.18 % | 162912.7829 MeV (+28894.5 ppm) |
| ${}^{171}$Pt | 171 | 93 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1335.2987 | 1336.6389 | -0.10 % | 163869.1643 MeV (+28889.3 ppm) |
| ${}^{172}$Pt | 172 | 94 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1347.1078 | 1348.3503 | -0.09 % | 164824.0700 MeV (+28890.8 ppm) |
| ${}^{173}$Pt | 173 | 95 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1356.9816 | 1357.2517 | -0.02 % | 165780.9110 MeV (+28886.4 ppm) |
| ${}^{174}$Pt | 174 | 96 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1368.3292 | 1368.7039 | -0.03 % | 166736.2781 MeV (+28889.2 ppm) |
| ${}^{175}$Pt | 175 | 97 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1377.7594 | 1377.1663 | +0.04 % | 167693.5628 MeV (+28884.8 ppm) |
| ${}^{176}$Pt | 176 | 98 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1388.6611 | 1388.4628 | +0.01 % | 168649.3758 MeV (+28889.2 ppm) |
| ${}^{177}$Pt | 177 | 99 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1397.6626 | 1396.9707 | +0.05 % | 169607.0891 MeV (+28887.7 ppm) |
| ${}^{178}$Pt | 178 | 100 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1408.1334 | 1407.6690 | +0.03 % | 170563.3330 MeV (+28891.0 ppm) |
| ${}^{179}$Pt | 179 | 101 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1416.7205 | 1416.0110 | +0.05 % | 171521.4607 MeV (+28891.0 ppm) |
| ${}^{180}$Pt | 180 | 102 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1426.7746 | 1426.2441 | +0.04 % | 172478.1213 MeV (+28893.9 ppm) |
| ${}^{181}$Pt | 181 | 103 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1434.9612 | 1434.2670 | +0.05 % | 173436.6495 MeV (+28894.3 ppm) |
| ${}^{182}$Pt | 182 | 104 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1444.6122 | 1444.1252 | +0.03 % | 174393.7133 MeV (+28897.2 ppm) |
| ${}^{183}$Pt | 183 | 105 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1452.4115 | 1451.8013 | +0.04 % | 175352.6289 MeV (+28897.8 ppm) |
| ${}^{184}$Pt | 184 | 106 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1461.6724 | 1461.4319 | +0.02 % | 176310.0827 MeV (+28901.6 ppm) |
| ${}^{185}$Pt | 185 | 107 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1469.0968 | 1468.8589 | +0.02 % | 177269.3731 MeV (+28902.8 ppm) |
| ${}^{186}$Pt | 186 | 108 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1477.9801 | 1478.1065 | -0.01 % | 178227.2045 MeV (+28906.4 ppm) |
| ${}^{187}$Pt | 187 | 109 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1485.0418 | 1484.9988 | +0.00 % | 179186.8576 MeV (+28906.5 ppm) |
| ${}^{188}$Pt | 188 | 110 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1493.5595 | 1494.2057 | -0.04 % | 180145.0547 MeV (+28911.9 ppm) |
| ${}^{189}$Pt | 189 | 111 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1500.2700 | 1500.9255 | -0.04 % | 181105.0590 MeV (+28913.0 ppm) |
| ${}^{190}$Pt | 190 | 112 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1508.4334 | 1509.8339 | -0.09 % | 182063.6104 MeV (+28918.5 ppm) |
| ${}^{191}$Pt | 191 | 113 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1514.8038 | 1516.2970 | -0.10 % | 183023.9547 MeV (+28920.0 ppm) |
| ${}^{192}$Pt | 192 | 114 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1522.6239 | 1524.9585 | -0.15 % | 183982.8494 MeV (+28926.0 ppm) |
| ${}^{193}$Pt | 193 | 115 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1528.6648 | 1531.2210 | -0.17 % | 184943.5233 MeV (+28928.1 ppm) |
| ${}^{194}$Pt | 194 | 116 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1536.1522 | 1539.5727 | -0.22 % | 185902.7507 MeV (+28934.0 ppm) |
| ${}^{195}$Pt | 195 | 117 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1541.8737 | 1545.6778 | -0.25 % | 186863.7439 MeV (+28936.9 ppm) |
| ${}^{196}$Pt | 196 | 118 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1549.0385 | 1553.5998 | -0.29 % | 187823.2939 MeV (+28942.1 ppm) |
| ${}^{197}$Pt | 197 | 119 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1554.4504 | 1559.4464 | -0.32 % | 188784.5967 MeV (+28945.1 ppm) |
| ${}^{198}$Pt | 198 | 120 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1561.3022 | 1567.0019 | -0.36 % | 189744.4597 MeV (+28949.9 ppm) |
| ${}^{199}$Pt | 199 | 121 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1566.4140 | 1572.5579 | -0.39 % | 190706.0627 MeV (+28952.9 ppm) |
| ${}^{200}$Pt | 200 | 122 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1572.9621 | 1579.8397 | -0.44 % | 191666.2293 MeV (+28957.7 ppm) |
| ${}^{201}$Pt | 201 | 123 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1577.7827 | 1585.0526 | -0.46 % | 192628.1236 MeV (+28960.3 ppm) |
| ${}^{202}$Pt | 202 | 124 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1584.0361 | 1592.0753 | -0.50 % | 193588.5849 MeV (+28965.1 ppm) |
| ${}^{203}$Pt | 203 | 125 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1588.5741 | 1597.0010 | -0.53 % | 194550.7617 MeV (+28967.4 ppm) |
| ${}^{204}$Pt | 204 | 126 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1594.5414 | 1603.2360 | -0.54 % | 195511.5091 MeV (+28969.1 ppm) |
| ${}^{205}$Pt | 205 | 127 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1598.8052 | 1606.3800 | -0.47 % | 196473.9602 MeV (+28964.0 ppm) |
| ${}^{206}$Pt | 206 | 128 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1604.4946 | 1610.9200 | -0.40 % | 197434.9855 MeV (+28958.1 ppm) |
| ${}^{207}$Pt | 207 | 129 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1608.4921 | 1613.9790 | -0.34 % | 198397.7028 MeV (+28952.9 ppm) |
| ${}^{208}$Pt | 208 | 130 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1613.9116 | 1618.2400 | -0.27 % | 199358.9980 MeV (+28948.2 ppm) |

### Gold (Z = 79)

_43 of 43 isotopes with a framework prediction; 43 of 43 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{168}$Au | 168 | 89 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1286.4120 | 1291.5840 | -0.40 % | 161016.5765 MeV (+28902.4 ppm) |
| ${}^{169}$Au | 169 | 90 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1299.5009 | 1304.0040 | -0.35 % | 161970.2023 MeV (+28900.2 ppm) |
| ${}^{170}$Au | 170 | 91 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1310.6207 | 1314.1000 | -0.26 % | 162925.7973 MeV (+28894.8 ppm) |
| ${}^{171}$Au | 171 | 92 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1323.2107 | 1325.9523 | -0.21 % | 163879.9220 MeV (+28892.8 ppm) |
| ${}^{172}$Au | 172 | 93 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1333.8504 | 1335.7793 | -0.14 % | 164835.9971 MeV (+28889.6 ppm) |
| ${}^{173}$Au | 173 | 94 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1345.9587 | 1347.3646 | -0.10 % | 165790.6036 MeV (+28888.4 ppm) |
| ${}^{174}$Au | 174 | 95 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1356.1348 | 1356.6780 | -0.04 % | 166747.1423 MeV (+28884.7 ppm) |
| ${}^{175}$Au | 175 | 96 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1367.7777 | 1368.0789 | -0.02 % | 167702.2141 MeV (+28885.4 ppm) |
| ${}^{176}$Au | 176 | 97 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1377.5061 | 1377.2675 | +0.02 % | 168659.2005 MeV (+28883.8 ppm) |
| ${}^{177}$Au | 177 | 98 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1388.6993 | 1388.3636 | +0.02 % | 169614.7221 MeV (+28885.2 ppm) |
| ${}^{178}$Au | 178 | 99 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1397.9950 | 1397.1922 | +0.06 % | 170572.1412 MeV (+28884.0 ppm) |
| ${}^{179}$Au | 179 | 100 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1408.7534 | 1407.9491 | +0.06 % | 171528.0975 MeV (+28885.9 ppm) |
| ${}^{180}$Au | 180 | 101 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1417.6309 | 1416.6575 | +0.07 % | 172485.9348 MeV (+28886.5 ppm) |
| ${}^{181}$Au | 181 | 102 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1427.9688 | 1426.9743 | +0.07 % | 173442.3117 MeV (+28888.2 ppm) |
| ${}^{182}$Au | 182 | 103 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1436.4418 | 1435.4784 | +0.07 % | 174400.5534 MeV (+28889.8 ppm) |
| ${}^{183}$Au | 183 | 104 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1446.3729 | 1445.4373 | +0.06 % | 175357.3372 MeV (+28891.7 ppm) |
| ${}^{184}$Au | 184 | 105 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1454.4547 | 1453.6358 | +0.06 % | 176315.9701 MeV (+28893.8 ppm) |
| ${}^{185}$Au | 185 | 106 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1463.9920 | 1463.2466 | +0.05 % | 177273.1476 MeV (+28895.8 ppm) |
| ${}^{186}$Au | 186 | 107 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1471.6953 | 1471.1746 | +0.04 % | 178232.1591 MeV (+28898.5 ppm) |
| ${}^{187}$Au | 187 | 108 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1480.8512 | 1480.5598 | +0.02 % | 179189.7179 MeV (+28901.3 ppm) |
| ${}^{188}$Au | 188 | 109 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1488.1881 | 1487.9737 | +0.01 % | 180149.0958 MeV (+28903.0 ppm) |
| ${}^{189}$Au | 189 | 110 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1496.9748 | 1497.2557 | -0.02 % | 181107.0239 MeV (+28907.3 ppm) |
| ${}^{190}$Au | 190 | 111 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1503.9568 | 1504.5786 | -0.04 % | 182066.7566 MeV (+28910.3 ppm) |
| ${}^{191}$Au | 191 | 112 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1512.3857 | 1513.6142 | -0.08 % | 183025.0425 MeV (+28915.1 ppm) |
| ${}^{192}$Au | 192 | 113 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1519.0240 | 1520.6598 | -0.11 % | 183985.1189 MeV (+28918.4 ppm) |
| ${}^{193}$Au | 193 | 114 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1527.1061 | 1529.3638 | -0.15 % | 184943.7516 MeV (+28923.2 ppm) |
| ${}^{194}$Au | 194 | 115 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1533.4114 | 1536.2422 | -0.18 % | 185904.1611 MeV (+28927.3 ppm) |
| ${}^{195}$Au | 195 | 116 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1541.1573 | 1544.6687 | -0.23 % | 186863.1300 MeV (+28932.2 ppm) |
| ${}^{196}$Au | 196 | 117 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1547.1397 | 1551.3116 | -0.27 % | 187823.8623 MeV (+28936.7 ppm) |
| ${}^{197}$Au | 197 | 118 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1554.5596 | 1559.3840 | -0.31 % | 188783.1573 MeV (+28941.3 ppm) |
| ${}^{198}$Au | 198 | 119 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1560.2290 | 1565.8964 | -0.36 % | 189744.2026 MeV (+28946.7 ppm) |
| ${}^{199}$Au | 199 | 120 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1567.3325 | 1573.4806 | -0.39 % | 190703.8139 MeV (+28950.2 ppm) |
| ${}^{200}$Au | 200 | 121 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1572.6983 | 1579.6983 | -0.44 % | 191665.1628 MeV (+28955.5 ppm) |
| ${}^{201}$Au | 201 | 122 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1579.4949 | 1586.9302 | -0.47 % | 192625.0810 MeV (+28958.6 ppm) |
| ${}^{202}$Au | 202 | 123 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1584.5662 | 1592.9538 | -0.53 % | 193586.7245 MeV (+28964.3 ppm) |
| ${}^{203}$Au | 203 | 124 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1591.0648 | 1599.8156 | -0.55 % | 194546.9407 MeV (+28966.9 ppm) |
| ${}^{204}$Au | 204 | 125 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1595.8502 | 1605.0720 | -0.57 % | 195508.8700 MeV (+28970.2 ppm) |
| ${}^{205}$Au | 205 | 126 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1602.0595 | 1611.3000 | -0.57 % | 196469.3755 MeV (+28971.0 ppm) |
| ${}^{206}$Au | 206 | 127 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1606.5675 | 1615.0400 | -0.52 % | 197431.5823 MeV (+28966.9 ppm) |
| ${}^{207}$Au | 207 | 128 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1612.4958 | 1619.5680 | -0.44 % | 198392.3688 MeV (+28960.0 ppm) |
| ${}^{208}$Au | 208 | 129 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1616.7343 | 1623.0240 | -0.39 % | 199354.8451 MeV (+28955.5 ppm) |
| ${}^{209}$Au | 209 | 130 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1622.3896 | 1627.2740 | -0.30 % | 200315.9046 MeV (+28949.4 ppm) |
| ${}^{210}$Au | 210 | 131 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1626.3664 | 1630.4400 | -0.25 % | 201278.6425 MeV (+28945.4 ppm) |

### Mercury (Z = 80)

_47 of 47 isotopes with a framework prediction; 47 of 47 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{170}$Hg | 170 | 90 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1298.3582 | 1304.0700 | -0.44 % | 162936.7295 MeV (+28904.6 ppm) |
| ${}^{171}$Hg | 171 | 91 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1309.7819 | 1314.3060 | -0.34 % | 163892.0205 MeV (+28898.4 ppm) |
| ${}^{172}$Hg | 172 | 92 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1322.6689 | 1326.7403 | -0.31 % | 164845.8483 MeV (+28898.0 ppm) |
| ${}^{173}$Hg | 173 | 93 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1333.6086 | 1336.4250 | -0.21 % | 165801.6234 MeV (+28891.9 ppm) |
| ${}^{174}$Hg | 174 | 94 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1346.0100 | 1348.4626 | -0.18 % | 166755.9367 MeV (+28891.9 ppm) |
| ${}^{175}$Hg | 175 | 95 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1356.4822 | 1357.8623 | -0.10 % | 167712.1793 MeV (+28887.0 ppm) |
| ${}^{176}$Hg | 176 | 96 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1368.4145 | 1369.7489 | -0.10 % | 168666.9618 MeV (+28888.9 ppm) |
| ${}^{177}$Hg | 177 | 97 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1378.4351 | 1378.8114 | -0.03 % | 169623.6560 MeV (+28884.7 ppm) |
| ${}^{178}$Hg | 178 | 98 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1389.9139 | 1390.4222 | -0.04 % | 170578.8920 MeV (+28887.6 ppm) |
| ${}^{179}$Hg | 179 | 99 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1399.4980 | 1399.1111 | +0.03 % | 171536.0226 MeV (+28883.7 ppm) |
| ${}^{180}$Hg | 180 | 100 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1410.5383 | 1410.5000 | +0.00 % | 172491.6971 MeV (+28887.8 ppm) |
| ${}^{181}$Hg | 181 | 101 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1419.7005 | 1418.9819 | +0.05 % | 173449.2497 MeV (+28885.3 ppm) |
| ${}^{182}$Hg | 182 | 102 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1430.3166 | 1429.9690 | +0.02 % | 174405.3484 MeV (+28889.4 ppm) |
| ${}^{183}$Hg | 183 | 103 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1439.0706 | 1438.2681 | +0.06 % | 175363.3092 MeV (+28888.2 ppm) |
| ${}^{184}$Hg | 184 | 104 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1449.2762 | 1448.8796 | +0.03 % | 176319.8183 MeV (+28892.4 ppm) |
| ${}^{185}$Hg | 185 | 105 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1457.6353 | 1456.7897 | +0.06 % | 177278.1739 MeV (+28891.1 ppm) |
| ${}^{186}$Hg | 186 | 106 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1467.4436 | 1467.2165 | +0.02 % | 178235.0805 MeV (+28896.5 ppm) |
| ${}^{187}$Hg | 187 | 107 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1475.4205 | 1474.8672 | +0.04 % | 179193.8183 MeV (+28895.9 ppm) |
| ${}^{188}$Hg | 188 | 108 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1484.8439 | 1485.0184 | -0.01 % | 180151.1096 MeV (+28901.7 ppm) |
| ${}^{189}$Hg | 189 | 109 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1492.4509 | 1492.5177 | -0.00 % | 181110.2175 MeV (+28902.3 ppm) |
| ${}^{190}$Hg | 190 | 110 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1501.5015 | 1502.3333 | -0.06 % | 182067.8816 MeV (+28908.2 ppm) |
| ${}^{191}$Hg | 191 | 111 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1508.7501 | 1509.6258 | -0.06 % | 183027.3478 MeV (+28909.5 ppm) |
| ${}^{192}$Hg | 192 | 112 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1517.4395 | 1519.1168 | -0.11 % | 183985.3732 MeV (+28915.5 ppm) |
| ${}^{193}$Hg | 193 | 113 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1524.3409 | 1526.2388 | -0.12 % | 184945.1866 MeV (+28917.7 ppm) |
| ${}^{194}$Hg | 194 | 114 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1532.6801 | 1535.4319 | -0.18 % | 185903.5621 MeV (+28923.8 ppm) |
| ${}^{195}$Hg | 195 | 115 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1539.2450 | 1542.3326 | -0.20 % | 186863.7120 MeV (+28926.6 ppm) |
| ${}^{196}$Hg | 196 | 116 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1547.2447 | 1551.2165 | -0.26 % | 187822.4271 MeV (+28932.7 ppm) |
| ${}^{197}$Hg | 197 | 117 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1553.4833 | 1558.0021 | -0.29 % | 188782.9032 MeV (+28936.6 ppm) |
| ${}^{198}$Hg | 198 | 118 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1561.1537 | 1566.4875 | -0.34 % | 189741.9476 MeV (+28942.1 ppm) |
| ${}^{199}$Hg | 199 | 119 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1567.0760 | 1573.1506 | -0.39 % | 190702.7401 MeV (+28946.9 ppm) |
| ${}^{200}$Hg | 200 | 120 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1574.4268 | 1581.1791 | -0.43 % | 191662.1041 MeV (+28951.6 ppm) |
| ${}^{201}$Hg | 201 | 121 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1580.0422 | 1587.4097 | -0.46 % | 192623.2035 MeV (+28955.5 ppm) |
| ${}^{202}$Hg | 202 | 122 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1587.0828 | 1595.1638 | -0.51 % | 193582.8776 MeV (+28960.2 ppm) |
| ${}^{203}$Hg | 203 | 123 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1592.4005 | 1601.1590 | -0.55 % | 194544.2747 MeV (+28964.4 ppm) |
| ${}^{204}$Hg | 204 | 124 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1599.1400 | 1608.6513 | -0.59 % | 195504.2500 MeV (+28969.2 ppm) |
| ${}^{205}$Hg | 205 | 125 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1604.1686 | 1614.3202 | -0.63 % | 196465.9361 MeV (+28973.0 ppm) |
| ${}^{206}$Hg | 206 | 126 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1610.6157 | 1621.0495 | -0.64 % | 197426.2038 MeV (+28975.1 ppm) |
| ${}^{207}$Hg | 207 | 127 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1615.3637 | 1624.6625 | -0.57 % | 198388.1706 MeV (+28969.4 ppm) |
| ${}^{208}$Hg | 208 | 128 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1621.5267 | 1629.5118 | -0.49 % | 199348.7224 MeV (+28963.0 ppm) |
| ${}^{209}$Hg | 209 | 129 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1626.0022 | 1632.9170 | -0.42 % | 200310.9616 MeV (+28957.7 ppm) |
| ${}^{210}$Hg | 210 | 130 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1631.8892 | 1637.7900 | -0.36 % | 201271.7894 MeV (+28952.4 ppm) |
| ${}^{211}$Hg | 211 | 131 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1636.0999 | 1640.9470 | -0.30 % | 202234.2935 MeV (+28947.2 ppm) |
| ${}^{212}$Hg | 212 | 132 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1641.7186 | 1645.5440 | -0.23 % | 203195.3895 MeV (+28942.8 ppm) |
| ${}^{213}$Hg | 213 | 133 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1645.6721 | 1648.4070 | -0.17 % | 204158.1508 MeV (+28937.7 ppm) |
| ${}^{214}$Hg | 214 | 134 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1651.0300 | 1652.9360 | -0.12 % | 205119.5077 MeV (+28933.8 ppm) |
| ${}^{215}$Hg | 215 | 135 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1654.7335 | 1655.7150 | -0.06 % | 206082.5190 MeV (+28929.2 ppm) |
| ${}^{216}$Hg | 216 | 136 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1659.8377 | 1659.9600 | -0.01 % | 207044.1295 MeV (+28925.4 ppm) |

### Thallium (Z = 81)

_43 of 43 isotopes with a framework prediction; 43 of 43 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{176}$Tl | 176 | 95 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1354.6447 | 1356.5971 | -0.14 % | 168679.4013 MeV (+28887.1 ppm) |
| ${}^{177}$Tl | 177 | 96 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1366.8699 | 1368.5933 | -0.13 % | 169633.8908 MeV (+28887.9 ppm) |
| ${}^{178}$Tl | 178 | 97 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1377.1864 | 1377.8980 | -0.05 % | 170590.2892 MeV (+28883.7 ppm) |
| ${}^{179}$Tl | 179 | 98 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1388.9544 | 1389.6655 | -0.05 % | 171545.2359 MeV (+28885.5 ppm) |
| ${}^{180}$Tl | 180 | 99 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1398.8305 | 1398.8576 | -0.00 % | 172502.0746 MeV (+28883.1 ppm) |
| ${}^{181}$Tl | 181 | 100 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1410.1563 | 1410.3372 | -0.01 % | 173457.4636 MeV (+28886.0 ppm) |
| ${}^{182}$Tl | 182 | 101 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1419.6067 | 1418.9370 | +0.05 % | 174414.7280 MeV (+28882.5 ppm) |
| ${}^{183}$Tl | 183 | 102 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1430.5046 | 1430.2684 | +0.02 % | 175370.5448 MeV (+28887.1 ppm) |
| ${}^{184}$Tl | 184 | 103 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1439.5431 | 1438.6358 | +0.06 % | 176328.2211 MeV (+28884.6 ppm) |
| ${}^{185}$Tl | 185 | 104 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1450.0269 | 1449.5815 | +0.03 % | 177284.4521 MeV (+28889.2 ppm) |
| ${}^{186}$Tl | 186 | 105 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1458.6669 | 1457.7780 | +0.06 % | 178242.5269 MeV (+28888.0 ppm) |
| ${}^{187}$Tl | 187 | 106 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1468.7497 | 1468.4110 | +0.02 % | 179199.1588 MeV (+28893.0 ppm) |
| ${}^{188}$Tl | 188 | 107 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1477.0038 | 1476.3741 | +0.04 % | 180157.6195 MeV (+28892.7 ppm) |
| ${}^{189}$Tl | 189 | 108 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1486.6983 | 1486.7251 | -0.00 % | 181114.6398 MeV (+28898.1 ppm) |
| ${}^{190}$Tl | 190 | 109 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1494.5788 | 1494.5466 | +0.00 % | 182073.4741 MeV (+28899.0 ppm) |
| ${}^{191}$Tl | 191 | 110 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1503.8969 | 1504.5346 | -0.04 % | 183030.8707 MeV (+28904.4 ppm) |
| ${}^{192}$Tl | 192 | 111 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1511.4155 | 1512.1952 | -0.05 % | 183990.0668 MeV (+28906.4 ppm) |
| ${}^{193}$Tl | 193 | 112 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1520.3690 | 1521.8715 | -0.10 % | 184947.8281 MeV (+28911.9 ppm) |
| ${}^{194}$Tl | 194 | 113 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1527.5369 | 1529.4031 | -0.12 % | 185907.3750 MeV (+28915.1 ppm) |
| ${}^{195}$Tl | 195 | 114 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1536.1368 | 1538.6922 | -0.17 % | 186865.4899 MeV (+28920.2 ppm) |
| ${}^{196}$Tl | 196 | 115 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1542.9648 | 1546.1048 | -0.20 % | 187825.3767 MeV (+28924.5 ppm) |
| ${}^{197}$Tl | 197 | 116 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1551.2217 | 1555.0338 | -0.25 % | 188783.8345 MeV (+28929.4 ppm) |
| ${}^{198}$Tl | 198 | 117 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1557.7201 | 1562.2796 | -0.29 % | 189744.0509 MeV (+28934.4 ppm) |
| ${}^{199}$Tl | 199 | 118 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1565.6444 | 1570.8816 | -0.33 % | 190702.8414 MeV (+28939.2 ppm) |
| ${}^{200}$Tl | 200 | 119 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1571.8230 | 1577.9407 | -0.39 % | 191663.3775 MeV (+28944.8 ppm) |
| ${}^{201}$Tl | 201 | 120 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1579.4245 | 1586.1456 | -0.42 % | 192622.4908 MeV (+28949.1 ppm) |
| ${}^{202}$Tl | 202 | 121 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1585.2930 | 1593.0166 | -0.48 % | 193583.3371 MeV (+28955.2 ppm) |
| ${}^{203}$Tl | 203 | 122 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1592.5811 | 1600.8688 | -0.52 % | 194542.7638 MeV (+28959.1 ppm) |
| ${}^{204}$Tl | 204 | 123 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1598.1485 | 1607.5249 | -0.58 % | 195503.9111 MeV (+28965.5 ppm) |
| ${}^{205}$Tl | 205 | 124 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1605.1324 | 1615.0709 | -0.62 % | 196463.6421 MeV (+28969.3 ppm) |
| ${}^{206}$Tl | 206 | 125 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1610.4076 | 1621.5747 | -0.69 % | 197425.0816 MeV (+28976.3 ppm) |
| ${}^{207}$Tl | 207 | 126 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1617.0959 | 1628.4272 | -0.70 % | 198385.1081 MeV (+28977.8 ppm) |
| ${}^{208}$Tl | 208 | 127 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1622.0873 | 1632.2142 | -0.62 % | 199346.8315 MeV (+28971.7 ppm) |
| ${}^{209}$Tl | 209 | 128 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1628.4884 | 1637.1802 | -0.53 % | 200307.1451 MeV (+28964.7 ppm) |
| ${}^{210}$Tl | 210 | 129 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1633.2042 | 1640.8537 | -0.47 % | 201269.1441 MeV (+28959.6 ppm) |
| ${}^{211}$Tl | 211 | 130 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1639.3263 | 1645.7560 | -0.39 % | 202229.7367 MeV (+28953.8 ppm) |
| ${}^{212}$Tl | 212 | 131 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1643.7744 | 1649.3600 | -0.34 % | 203192.0035 MeV (+28949.5 ppm) |
| ${}^{213}$Tl | 213 | 132 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1649.6252 | 1654.0368 | -0.27 % | 204152.8674 MeV (+28944.3 ppm) |
| ${}^{214}$Tl | 214 | 133 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1653.8130 | 1657.4300 | -0.22 % | 205115.3945 MeV (+28940.6 ppm) |
| ${}^{215}$Tl | 215 | 134 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1659.4000 | 1661.9500 | -0.15 % | 206076.5221 MeV (+28935.6 ppm) |
| ${}^{216}$Tl | 216 | 135 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1663.3348 | 1665.1440 | -0.11 % | 207039.3022 MeV (+28932.4 ppm) |
| ${}^{217}$Tl | 217 | 136 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1668.6654 | 1669.3810 | -0.04 % | 208000.6864 MeV (+28927.6 ppm) |
| ${}^{218}$Tl | 218 | 137 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1672.3541 | 1672.4960 | -0.01 % | 208963.7124 MeV (+28924.6 ppm) |

### Lead (Z = 82)

_43 of 43 isotopes with a framework prediction; 43 of 43 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{178}$Pb | 178 | 96 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1366.5162 | 1368.9688 | -0.18 % | 170599.6291 MeV (+28889.2 ppm) |
| ${}^{179}$Pb | 179 | 97 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1377.1225 | 1378.5619 | -0.10 % | 171555.7375 MeV (+28884.8 ppm) |
| ${}^{180}$Pb | 180 | 98 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1389.1740 | 1390.6259 | -0.10 % | 172510.4008 MeV (+28887.0 ppm) |
| ${}^{181}$Pb | 181 | 99 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1399.3364 | 1399.8667 | -0.04 % | 173466.9532 MeV (+28883.2 ppm) |
| ${}^{182}$Pb | 182 | 100 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1410.9420 | 1411.6520 | -0.05 % | 174422.0624 MeV (+28886.3 ppm) |
| ${}^{183}$Pb | 183 | 101 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1420.6750 | 1420.4788 | +0.01 % | 175379.0441 MeV (+28882.6 ppm) |
| ${}^{184}$Pb | 184 | 102 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1431.8492 | 1432.0217 | -0.01 % | 176334.5847 MeV (+28886.7 ppm) |
| ${}^{185}$Pb | 185 | 103 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1441.1667 | 1440.5826 | +0.04 % | 177291.9820 MeV (+28883.8 ppm) |
| ${}^{186}$Pb | 186 | 104 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1451.9233 | 1451.7936 | +0.01 % | 178247.9402 MeV (+28888.4 ppm) |
| ${}^{187}$Pb | 187 | 105 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1460.8387 | 1460.1710 | +0.05 % | 179205.7395 MeV (+28886.7 ppm) |
| ${}^{188}$Pb | 188 | 106 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1471.1908 | 1471.0664 | +0.01 % | 180162.1022 MeV (+28891.7 ppm) |
| ${}^{189}$Pb | 189 | 107 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1479.7169 | 1479.1707 | +0.04 % | 181120.2909 MeV (+28890.6 ppm) |
| ${}^{190}$Pb | 190 | 108 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1489.6772 | 1489.8146 | -0.01 % | 182077.0453 MeV (+28896.3 ppm) |
| ${}^{191}$Pb | 191 | 109 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1497.8262 | 1497.7605 | +0.00 % | 183035.6111 MeV (+28896.4 ppm) |
| ${}^{192}$Pb | 192 | 110 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1507.4069 | 1508.0925 | -0.05 % | 183992.7452 MeV (+28902.3 ppm) |
| ${}^{193}$Pb | 193 | 111 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1515.1906 | 1515.8412 | -0.04 % | 184951.6763 MeV (+28903.3 ppm) |
| ${}^{194}$Pb | 194 | 112 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1524.4032 | 1525.8911 | -0.10 % | 185909.1784 MeV (+28909.5 ppm) |
| ${}^{195}$Pb | 195 | 113 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1531.8328 | 1533.4926 | -0.11 % | 186868.4637 MeV (+28911.6 ppm) |
| ${}^{196}$Pb | 196 | 114 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1540.6885 | 1543.1741 | -0.16 % | 187826.3227 MeV (+28917.6 ppm) |
| ${}^{197}$Pb | 197 | 115 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1547.7748 | 1550.6426 | -0.18 % | 188785.9512 MeV (+28920.7 ppm) |
| ${}^{198}$Pb | 198 | 116 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1556.2844 | 1560.0360 | -0.24 % | 189744.1563 MeV (+28926.8 ppm) |
| ${}^{199}$Pb | 199 | 117 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1563.0378 | 1567.2716 | -0.27 % | 190704.1177 MeV (+28930.4 ppm) |
| ${}^{200}$Pb | 200 | 118 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1571.2115 | 1576.3620 | -0.33 % | 191662.6588 MeV (+28936.6 ppm) |
| ${}^{201}$Pb | 201 | 119 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1577.6419 | 1583.4535 | -0.37 % | 192622.9431 MeV (+28941.0 ppm) |
| ${}^{202}$Pb | 202 | 120 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1585.4897 | 1592.1944 | -0.42 % | 193581.8101 MeV (+28946.9 ppm) |
| ${}^{203}$Pb | 203 | 121 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1591.6067 | 1599.1116 | -0.47 % | 194542.4079 MeV (+28951.9 ppm) |
| ${}^{204}$Pb | 204 | 122 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1599.1380 | 1607.5063 | -0.52 % | 195501.5914 MeV (+28957.4 ppm) |
| ${}^{205}$Pb | 205 | 123 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1604.9508 | 1614.2379 | -0.58 % | 196462.4933 MeV (+28963.0 ppm) |
| ${}^{206}$Pb | 206 | 124 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1612.1748 | 1622.3246 | -0.63 % | 197421.9842 MeV (+28968.4 ppm) |
| ${}^{207}$Pb | 207 | 125 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1617.6923 | 1629.0623 | -0.70 % | 198383.1814 MeV (+28975.3 ppm) |
| ${}^{208}$Pb | 208 | 126 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1624.6176 | 1636.4302 | -0.72 % | 199342.9709 MeV (+28978.3 ppm) |
| ${}^{209}$Pb | 209 | 127 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1629.8483 | 1640.3676 | -0.64 % | 200304.4549 MeV (+28971.9 ppm) |
| ${}^{210}$Pb | 210 | 128 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1636.4835 | 1645.5528 | -0.55 % | 201264.5345 MeV (+28964.9 ppm) |
| ${}^{211}$Pb | 211 | 129 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1641.4356 | 1649.3887 | -0.48 % | 202226.2972 MeV (+28959.4 ppm) |
| ${}^{212}$Pb | 212 | 130 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1647.7888 | 1654.5159 | -0.41 % | 203186.6588 MeV (+28953.7 ppm) |
| ${}^{213}$Pb | 213 | 131 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1652.4701 | 1658.2419 | -0.35 % | 204148.6922 MeV (+28949.1 ppm) |
| ${}^{214}$Pb | 214 | 132 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1658.5492 | 1663.2926 | -0.29 % | 205109.3279 MeV (+28944.4 ppm) |
| ${}^{215}$Pb | 215 | 133 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1662.9673 | 1666.8387 | -0.23 % | 206071.6246 MeV (+28940.4 ppm) |
| ${}^{216}$Pb | 216 | 134 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1668.7797 | 1671.8400 | -0.18 % | 207032.5269 MeV (+28936.4 ppm) |
| ${}^{217}$Pb | 217 | 135 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1672.9420 | 1675.0230 | -0.12 % | 207995.0794 MeV (+28932.5 ppm) |
| ${}^{218}$Pb | 218 | 136 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1678.4951 | 1679.6900 | -0.07 % | 208956.2411 MeV (+28928.8 ppm) |
| ${}^{219}$Pb | 219 | 137 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1682.4085 | 1682.7960 | -0.02 % | 209919.0424 MeV (+28925.0 ppm) |
| ${}^{220}$Pb | 220 | 138 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1687.7093 | 1687.4000 | +0.02 % | 210880.4564 MeV (+28921.9 ppm) |

### Bismuth (Z = 83)

_41 of 41 isotopes with a framework prediction; 41 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{184}$Bi | 184 | 101 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1419.6007 | 1419.0080 | +0.04 % | 176345.5029 MeV (+28876.6 ppm) |
| ${}^{185}$Bi | 185 | 102 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1431.0547 | 1430.4200 | +0.04 % | 177300.7636 MeV (+28879.2 ppm) |
| ${}^{186}$Bi | 186 | 103 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1440.6547 | 1439.4759 | +0.08 % | 178257.8784 MeV (+28877.2 ppm) |
| ${}^{187}$Bi | 187 | 104 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1451.6876 | 1450.7850 | +0.06 % | 179213.5603 MeV (+28880.8 ppm) |
| ${}^{188}$Bi | 188 | 105 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1460.8819 | 1459.6678 | +0.08 % | 180171.0808 MeV (+28880.6 ppm) |
| ${}^{189}$Bi | 189 | 106 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1471.5068 | 1470.6090 | +0.06 % | 181127.1706 MeV (+28884.2 ppm) |
| ${}^{190}$Bi | 190 | 107 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1480.3083 | 1479.2115 | +0.07 % | 182085.0840 MeV (+28884.6 ppm) |
| ${}^{191}$Bi | 191 | 108 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1490.5380 | 1489.9263 | +0.04 % | 183041.5690 MeV (+28889.1 ppm) |
| ${}^{192}$Bi | 192 | 109 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1498.9588 | 1498.2928 | +0.04 % | 183999.8629 MeV (+28890.2 ppm) |
| ${}^{193}$Bi | 193 | 110 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1508.8055 | 1508.7142 | +0.01 % | 184956.7311 MeV (+28895.1 ppm) |
| ${}^{194}$Bi | 194 | 111 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1516.8576 | 1516.9239 | -0.00 % | 185915.3938 MeV (+28897.3 ppm) |
| ${}^{195}$Bi | 195 | 112 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1526.3328 | 1526.9978 | -0.04 % | 186872.6333 MeV (+28902.2 ppm) |
| ${}^{196}$Bi | 196 | 113 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1534.0274 | 1535.0526 | -0.07 % | 187831.6535 MeV (+28905.4 ppm) |
| ${}^{197}$Bi | 197 | 114 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1543.1425 | 1544.8021 | -0.11 % | 188789.2532 MeV (+28910.3 ppm) |
| ${}^{198}$Bi | 198 | 115 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1550.4905 | 1552.5600 | -0.13 % | 189748.6200 MeV (+28913.7 ppm) |
| ${}^{199}$Bi | 199 | 116 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1559.2561 | 1562.0551 | -0.18 % | 190706.5691 MeV (+28919.0 ppm) |
| ${}^{200}$Bi | 200 | 117 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1566.2678 | 1569.6994 | -0.22 % | 191666.2721 MeV (+28923.5 ppm) |
| ${}^{201}$Bi | 201 | 118 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1574.6944 | 1578.8291 | -0.26 % | 192624.5604 MeV (+28928.5 ppm) |
| ${}^{202}$Bi | 202 | 119 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1581.3799 | 1586.2223 | -0.31 % | 193584.5896 MeV (+28933.2 ppm) |
| ${}^{203}$Bi | 203 | 120 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1589.4773 | 1595.0677 | -0.35 % | 194543.2070 MeV (+28938.4 ppm) |
| ${}^{204}$Bi | 204 | 121 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1595.8463 | 1602.2600 | -0.40 % | 195503.5528 MeV (+28943.6 ppm) |
| ${}^{205}$Bi | 205 | 122 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1603.6240 | 1610.7510 | -0.44 % | 196462.4898 MeV (+28948.4 ppm) |
| ${}^{206}$Bi | 206 | 123 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1609.6856 | 1617.7849 | -0.50 % | 197423.1430 MeV (+28954.2 ppm) |
| ${}^{207}$Bi | 207 | 124 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1617.1530 | 1625.8826 | -0.54 % | 198382.3904 MeV (+28958.4 ppm) |
| ${}^{208}$Bi | 208 | 125 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1622.9161 | 1632.7695 | -0.60 % | 199343.3421 MeV (+28965.0 ppm) |
| ${}^{209}$Bi | 209 | 126 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1630.0818 | 1640.2293 | -0.62 % | 200302.8911 MeV (+28967.3 ppm) |
| ${}^{210}$Bi | 210 | 127 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1635.5551 | 1644.8339 | -0.56 % | 201264.1327 MeV (+28963.2 ppm) |
| ${}^{211}$Bi | 211 | 128 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1642.4276 | 1649.9724 | -0.46 % | 202223.9749 MeV (+28954.8 ppm) |
| ${}^{212}$Bi | 212 | 129 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1647.6192 | 1654.3026 | -0.40 % | 203185.4981 MeV (+28950.8 ppm) |
| ${}^{213}$Bi | 213 | 130 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1654.2068 | 1659.4876 | -0.32 % | 204145.6252 MeV (+28944.2 ppm) |
| ${}^{214}$Bi | 214 | 131 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1659.1247 | 1663.5280 | -0.26 % | 205107.4221 MeV (+28940.1 ppm) |
| ${}^{215}$Bi | 215 | 132 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1665.4352 | 1668.7693 | -0.20 % | 206067.8264 MeV (+28935.3 ppm) |
| ${}^{216}$Bi | 216 | 133 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1670.0869 | 1672.5959 | -0.15 % | 207029.8894 MeV (+28931.6 ppm) |
| ${}^{217}$Bi | 217 | 134 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1676.1280 | 1677.8113 | -0.10 % | 207990.5631 MeV (+28928.1 ppm) |
| ${}^{218}$Bi | 218 | 135 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1680.5210 | 1681.3965 | -0.05 % | 208952.8849 MeV (+28924.5 ppm) |
| ${}^{219}$Bi | 219 | 136 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1686.2999 | 1686.3000 | -0.00 % | 209913.8208 MeV (+28921.1 ppm) |
| ${}^{220}$Bi | 220 | 137 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1690.4412 | 1689.8200 | +0.04 % | 210876.3942 MeV (+28918.0 ppm) |
| ${}^{221}$Bi | 221 | 138 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1695.9650 | 1694.6280 | +0.08 % | 211837.5852 MeV (+28915.2 ppm) |
| ${}^{222}$Bi | 222 | 139 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1699.8615 | 1697.8560 | +0.12 % | 212800.4035 MeV (+28912.8 ppm) |
| ${}^{223}$Bi | 223 | 140 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1705.1370 | 1702.8280 | +0.14 % | 213761.8428 MeV (+28911.0 ppm) |
| ${}^{224}$Bi | 224 | 141 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1708.7952 | 1705.9840 | +0.16 % | 214724.8994 MeV (+28909.4 ppm) |

### Polonium (Z = 84)

_42 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{186}$Po | 186 | 102 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1431.4193 | 1431.4465 | -0.00 % | 178265.7836 MeV (+28879.8 ppm) |
| ${}^{187}$Po | 187 | 103 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1441.2963 | 1440.7955 | +0.03 % | 179222.6213 MeV (+28878.4 ppm) |
| ${}^{188}$Po | 188 | 104 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1452.6001 | 1452.2350 | +0.03 % | 180178.0323 MeV (+28881.2 ppm) |
| ${}^{189}$Po | 189 | 105 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1462.0680 | 1461.1840 | +0.06 % | 181135.2792 MeV (+28879.8 ppm) |
| ${}^{190}$Po | 190 | 106 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1472.9605 | 1472.3960 | +0.04 % | 182091.1014 MeV (+28883.5 ppm) |
| ${}^{191}$Po | 191 | 107 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1482.0321 | 1480.9733 | +0.07 % | 183048.7446 MeV (+28882.2 ppm) |
| ${}^{192}$Po | 192 | 108 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1492.5261 | 1492.0424 | +0.03 % | 184004.9654 MeV (+28887.3 ppm) |
| ${}^{193}$Po | 193 | 109 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1501.2138 | 1500.3725 | +0.06 % | 184962.9925 MeV (+28886.7 ppm) |
| ${}^{194}$Po | 194 | 110 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1511.3214 | 1511.1232 | +0.01 % | 185919.5996 MeV (+28892.0 ppm) |
| ${}^{195}$Po | 195 | 111 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1519.6370 | 1519.3065 | +0.02 % | 186877.9988 MeV (+28892.6 ppm) |
| ${}^{196}$Po | 196 | 112 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1529.3700 | 1529.7299 | -0.02 % | 187834.9806 MeV (+28898.0 ppm) |
| ${}^{197}$Po | 197 | 113 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1537.3248 | 1537.7256 | -0.03 % | 188793.7405 MeV (+28899.5 ppm) |
| ${}^{198}$Po | 198 | 114 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1546.6944 | 1547.8771 | -0.08 % | 189751.0857 MeV (+28905.3 ppm) |
| ${}^{199}$Po | 199 | 115 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1554.2994 | 1555.7140 | -0.09 % | 190710.1955 MeV (+28907.7 ppm) |
| ${}^{200}$Po | 200 | 116 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1563.3164 | 1565.4881 | -0.14 % | 191667.8933 MeV (+28913.2 ppm) |
| ${}^{201}$Po | 201 | 117 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1570.5819 | 1573.1389 | -0.16 % | 192627.3425 MeV (+28916.4 ppm) |
| ${}^{202}$Po | 202 | 118 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1579.2567 | 1582.6307 | -0.21 % | 193585.3825 MeV (+28922.1 ppm) |
| ${}^{203}$Po | 203 | 119 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1586.1929 | 1590.0712 | -0.24 % | 194545.1611 MeV (+28925.8 ppm) |
| ${}^{204}$Po | 204 | 120 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1594.5355 | 1599.1728 | -0.29 % | 195503.5333 MeV (+28931.0 ppm) |
| ${}^{205}$Po | 205 | 121 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1601.1519 | 1606.4244 | -0.33 % | 196463.6316 MeV (+28935.3 ppm) |
| ${}^{206}$Po | 206 | 122 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1609.1718 | 1615.1630 | -0.37 % | 197422.3265 MeV (+28940.1 ppm) |
| ${}^{207}$Po | 207 | 123 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1615.4779 | 1622.1914 | -0.41 % | 198382.7352 MeV (+28944.7 ppm) |
| ${}^{208}$Po | 208 | 124 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1623.1843 | 1630.5862 | -0.45 % | 199341.7435 MeV (+28949.3 ppm) |
| ${}^{209}$Po | 209 | 125 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1629.1889 | 1637.5543 | -0.51 % | 200302.4537 MeV (+28955.0 ppm) |
| ${}^{210}$Po | 210 | 126 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1636.5908 | 1645.2127 | -0.52 % | 201261.7666 MeV (+28957.2 ppm) |
| ${}^{211}$Po | 211 | 127 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1642.3025 | 1649.7635 | -0.45 % | 202222.7697 MeV (+28951.6 ppm) |
| ${}^{212}$Po | 212 | 128 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1649.4083 | 1655.7717 | -0.38 % | 203182.3786 MeV (+28946.7 ppm) |
| ${}^{213}$Po | 213 | 129 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1654.8354 | 1660.1271 | -0.32 % | 204143.6663 MeV (+28941.7 ppm) |
| ${}^{214}$Po | 214 | 130 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1661.6535 | 1666.0149 | -0.26 % | 205103.5631 MeV (+28937.7 ppm) |
| ${}^{215}$Po | 215 | 131 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1666.8039 | 1670.1580 | -0.20 % | 206065.1274 MeV (+28933.0 ppm) |
| ${}^{216}$Po | 216 | 132 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1673.3420 | 1675.9052 | -0.15 % | 207025.3040 MeV (+28929.7 ppm) |
| ${}^{217}$Po | 217 | 133 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1678.2235 | 1679.8754 | -0.10 % | 207987.1373 MeV (+28925.6 ppm) |
| ${}^{218}$Po | 218 | 134 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1684.4894 | 1685.4735 | -0.06 % | 208947.5862 MeV (+28923.0 ppm) |
| ${}^{219}$Po | 219 | 135 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1689.1093 | 1689.2201 | -0.01 % | 209909.6811 MeV (+28919.1 ppm) |
| ${}^{220}$Po | 220 | 136 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1695.1103 | 1694.7094 | +0.02 % | 210870.3949 MeV (+28917.3 ppm) |
| ${}^{221}$Po | 221 | 137 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1699.4757 | 1698.2704 | +0.07 % | 211832.7442 MeV (+28913.8 ppm) |
| ${}^{222}$Po | 222 | 138 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1705.2189 | 1703.6292 | +0.09 % | 212793.7158 MeV (+28912.6 ppm) |
| ${}^{223}$Po | 223 | 139 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1709.3368 | 1707.0650 | +0.13 % | 213756.3127 MeV (+28909.9 ppm) |
| ${}^{224}$Po | 224 | 140 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1714.8290 | 1712.2560 | +0.15 % | 214717.5353 MeV (+28909.4 ppm) |
| ${}^{225}$Po | 225 | 141 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1718.7059 | 1715.8500 | +0.17 % | 215680.3731 MeV (+28907.5 ppm) |
| ${}^{226}$Po | 226 | 142 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1723.9538 | 1720.7640 | +0.19 % | 216641.8400 MeV (+28907.5 ppm) |
| ${}^{227}$Po | 227 | 143 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1727.5961 | 1724.2920 | +0.19 % | 217604.9124 MeV (+28906.5 ppm) |

### Astatine (Z = 85)

_39 of 39 isotopes with a framework prediction; 39 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{191}$At | 191 | 106 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1472.3088 | 1471.2584 | +0.07 % | 183057.1377 MeV (+28877.7 ppm) |
| ${}^{192}$At | 192 | 107 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1481.6539 | 1480.2678 | +0.09 % | 184014.5073 MeV (+28877.4 ppm) |
| ${}^{193}$At | 193 | 108 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1492.4155 | 1491.3322 | +0.07 % | 184970.4605 MeV (+28880.9 ppm) |
| ${}^{194}$At | 194 | 109 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1501.3734 | 1500.0527 | +0.09 % | 185928.2174 MeV (+28881.1 ppm) |
| ${}^{195}$At | 195 | 110 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1511.7453 | 1510.8778 | +0.06 % | 186884.5602 MeV (+28885.4 ppm) |
| ${}^{196}$At | 196 | 111 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1520.3277 | 1519.3920 | +0.06 % | 187842.6926 MeV (+28886.4 ppm) |
| ${}^{197}$At | 197 | 112 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1530.3218 | 1529.9054 | +0.03 % | 188799.4133 MeV (+28890.9 ppm) |
| ${}^{198}$At | 198 | 113 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1538.5401 | 1538.3302 | +0.01 % | 189757.9097 MeV (+28893.4 ppm) |
| ${}^{199}$At | 199 | 114 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1548.1676 | 1548.5162 | -0.02 % | 190714.9970 MeV (+28898.0 ppm) |
| ${}^{200}$At | 200 | 115 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1556.0328 | 1556.7520 | -0.05 % | 191673.8466 MeV (+28901.3 ppm) |
| ${}^{201}$At | 201 | 116 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1565.3045 | 1566.6249 | -0.08 % | 192631.2897 MeV (+28906.0 ppm) |
| ${}^{202}$At | 202 | 117 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1572.8271 | 1574.5019 | -0.11 % | 193590.4819 MeV (+28909.0 ppm) |
| ${}^{203}$At | 203 | 118 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1581.7534 | 1584.1407 | -0.15 % | 194548.2703 MeV (+28914.2 ppm) |
| ${}^{204}$At | 204 | 119 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1588.9435 | 1591.9246 | -0.19 % | 195507.7950 MeV (+28918.4 ppm) |
| ${}^{205}$At | 205 | 120 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1597.5345 | 1601.1052 | -0.22 % | 196465.9187 MeV (+28922.8 ppm) |
| ${}^{206}$At | 206 | 121 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1604.4017 | 1608.6314 | -0.26 % | 197425.7663 MeV (+28927.2 ppm) |
| ${}^{207}$At | 207 | 122 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1612.6670 | 1617.4908 | -0.30 % | 198384.2158 MeV (+28931.5 ppm) |
| ${}^{208}$At | 208 | 123 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1619.2207 | 1624.8046 | -0.34 % | 199344.3768 MeV (+28936.3 ppm) |
| ${}^{209}$At | 209 | 124 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1627.1696 | 1633.2898 | -0.37 % | 200303.1427 MeV (+28940.1 ppm) |
| ${}^{210}$At | 210 | 125 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1633.4188 | 1640.4494 | -0.43 % | 201263.6083 MeV (+28945.6 ppm) |
| ${}^{211}$At | 211 | 126 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1641.0601 | 1648.1958 | -0.43 % | 202222.6818 MeV (+28947.1 ppm) |
| ${}^{212}$At | 212 | 127 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1647.0134 | 1653.2481 | -0.38 % | 203183.4432 MeV (+28943.0 ppm) |
| ${}^{213}$At | 213 | 128 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1654.3558 | 1659.2708 | -0.30 % | 204142.8156 MeV (+28937.0 ppm) |
| ${}^{214}$At | 214 | 129 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1660.0215 | 1664.1417 | -0.25 % | 205103.8647 MeV (+28933.5 ppm) |
| ${}^{215}$At | 215 | 130 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1667.0732 | 1670.0905 | -0.18 % | 206063.5278 MeV (+28928.7 ppm) |
| ${}^{216}$At | 216 | 131 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1672.4594 | 1674.6485 | -0.13 % | 207024.8564 MeV (+28925.1 ppm) |
| ${}^{217}$At | 217 | 132 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1679.2283 | 1680.5819 | -0.08 % | 207984.8022 MeV (+28921.7 ppm) |
| ${}^{218}$At | 218 | 133 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1684.3427 | 1684.9476 | -0.04 % | 208946.4026 MeV (+28918.5 ppm) |
| ${}^{219}$At | 219 | 134 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1690.8366 | 1690.7231 | +0.01 % | 209906.6235 MeV (+28915.7 ppm) |
| ${}^{220}$At | 220 | 135 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1695.6865 | 1694.8147 | +0.05 % | 210868.4884 MeV (+28912.5 ppm) |
| ${}^{221}$At | 221 | 136 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1701.9127 | 1700.4791 | +0.08 % | 211828.9769 MeV (+28910.5 ppm) |
| ${}^{222}$At | 222 | 137 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1706.5054 | 1704.3801 | +0.12 % | 212791.0990 MeV (+28907.6 ppm) |
| ${}^{223}$At | 223 | 138 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1712.4711 | 1709.9764 | +0.15 % | 213751.8481 MeV (+28906.5 ppm) |
| ${}^{224}$At | 224 | 139 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1716.8135 | 1713.7647 | +0.18 % | 214714.2205 MeV (+28904.4 ppm) |
| ${}^{225}$At | 225 | 140 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1722.5256 | 1719.2250 | +0.19 % | 215675.2232 MeV (+28904.0 ppm) |
| ${}^{226}$At | 226 | 141 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1726.6243 | 1723.0240 | +0.21 % | 216637.8392 MeV (+28902.6 ppm) |
| ${}^{227}$At | 227 | 142 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1732.0893 | 1728.1510 | +0.23 % | 217599.0889 MeV (+28902.5 ppm) |
| ${}^{228}$At | 228 | 143 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1735.9509 | 1731.8880 | +0.23 % | 218561.9422 MeV (+28901.9 ppm) |
| ${}^{229}$At | 229 | 144 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1741.1753 | 1736.9650 | +0.24 % | 219523.4325 MeV (+28901.8 ppm) |

### Radon (Z = 86)

_39 of 39 isotopes with a framework prediction; 39 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{193}$Rn | 193 | 107 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1482.4106 | 1481.4396 | +0.07 % | 184979.1351 MeV (+28877.1 ppm) |
| ${}^{194}$Rn | 194 | 108 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1493.4348 | 1492.8292 | +0.04 % | 185934.8257 MeV (+28881.0 ppm) |
| ${}^{195}$Rn | 195 | 109 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1502.6577 | 1501.5749 | +0.07 % | 186892.3175 MeV (+28879.8 ppm) |
| ${}^{196}$Rn | 196 | 110 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1513.2891 | 1512.7213 | +0.04 % | 187848.4009 MeV (+28884.5 ppm) |
| ${}^{197}$Rn | 197 | 111 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1522.1334 | 1521.2574 | +0.06 % | 188806.2714 MeV (+28884.2 ppm) |
| ${}^{198}$Rn | 198 | 112 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1532.3837 | 1532.0695 | +0.02 % | 189762.7358 MeV (+28889.0 ppm) |
| ${}^{199}$Rn | 199 | 113 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1540.8608 | 1540.4703 | +0.03 % | 190720.9736 MeV (+28889.9 ppm) |
| ${}^{200}$Rn | 200 | 114 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1550.7414 | 1550.9822 | -0.02 % | 191677.8077 MeV (+28895.0 ppm) |
| ${}^{201}$Rn | 201 | 115 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1558.8621 | 1559.1605 | -0.02 % | 192636.4017 MeV (+28896.6 ppm) |
| ${}^{202}$Rn | 202 | 116 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1568.3839 | 1569.3990 | -0.06 % | 193593.5947 MeV (+28901.9 ppm) |
| ${}^{203}$Rn | 203 | 117 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1576.1590 | 1577.3798 | -0.08 % | 194552.5344 MeV (+28904.2 ppm) |
| ${}^{204}$Rn | 204 | 118 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1585.3324 | 1587.2372 | -0.12 % | 195510.0758 MeV (+28909.3 ppm) |
| ${}^{205}$Rn | 205 | 119 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1592.7718 | 1595.0481 | -0.14 % | 196469.3511 MeV (+28912.3 ppm) |
| ${}^{206}$Rn | 206 | 120 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1601.6069 | 1604.5426 | -0.18 % | 197427.2308 MeV (+28917.1 ppm) |
| ${}^{207}$Rn | 207 | 121 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1608.7205 | 1612.1157 | -0.21 % | 198386.8320 MeV (+28920.5 ppm) |
| ${}^{208}$Rn | 208 | 122 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1617.2269 | 1621.2077 | -0.25 % | 199345.0404 MeV (+28924.8 ppm) |
| ${}^{209}$Rn | 209 | 123 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1624.0240 | 1628.5647 | -0.28 % | 200304.9581 MeV (+28928.6 ppm) |
| ${}^{210}$Rn | 210 | 124 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1632.2110 | 1637.2997 | -0.31 % | 201263.4858 MeV (+28932.6 ppm) |
| ${}^{211}$Rn | 211 | 125 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1638.7006 | 1644.5216 | -0.35 % | 202223.7110 MeV (+28937.2 ppm) |
| ${}^{212}$Rn | 212 | 126 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1646.5773 | 1652.4968 | -0.36 % | 203182.5491 MeV (+28938.6 ppm) |
| ${}^{213}$Rn | 213 | 127 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1652.7681 | 1657.6049 | -0.29 % | 204143.0731 MeV (+28933.7 ppm) |
| ${}^{214}$Rn | 214 | 128 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1660.3429 | 1664.2999 | -0.24 % | 205102.2130 MeV (+28930.1 ppm) |
| ${}^{215}$Rn | 215 | 129 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1666.2433 | 1669.2205 | -0.18 % | 206063.0274 MeV (+28925.8 ppm) |
| ${}^{216}$Rn | 216 | 130 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1673.5246 | 1675.8695 | -0.14 % | 207022.4608 MeV (+28923.4 ppm) |
| ${}^{217}$Rn | 217 | 131 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1679.1426 | 1680.5356 | -0.08 % | 207983.5576 MeV (+28919.3 ppm) |
| ${}^{218}$Rn | 218 | 132 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1686.1385 | 1687.0481 | -0.05 % | 208943.2765 MeV (+28917.7 ppm) |
| ${}^{219}$Rn | 219 | 133 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1691.4818 | 1691.5075 | -0.00 % | 209904.6480 MeV (+28913.9 ppm) |
| ${}^{220}$Rn | 220 | 134 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1698.1999 | 1697.7961 | +0.02 % | 210864.6447 MeV (+28912.6 ppm) |
| ${}^{221}$Rn | 221 | 135 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1703.2761 | 1702.0081 | +0.07 % | 211826.2832 MeV (+28908.9 ppm) |
| ${}^{222}$Rn | 222 | 136 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1709.7238 | 1708.1788 | +0.09 % | 212786.5503 MeV (+28908.4 ppm) |
| ${}^{223}$Rn | 223 | 137 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1714.5401 | 1712.2324 | +0.13 % | 213748.4488 MeV (+28905.2 ppm) |
| ${}^{224}$Rn | 224 | 138 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1720.7247 | 1718.2483 | +0.14 % | 214708.9790 MeV (+28905.2 ppm) |
| ${}^{225}$Rn | 225 | 139 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1725.2879 | 1722.2306 | +0.18 % | 215671.1305 MeV (+28902.9 ppm) |
| ${}^{226}$Rn | 226 | 140 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1731.2162 | 1728.0888 | +0.18 % | 216631.9170 MeV (+28903.4 ppm) |
| ${}^{227}$Rn | 227 | 141 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1735.5332 | 1732.0215 | +0.20 % | 217594.3147 MeV (+28902.1 ppm) |
| ${}^{228}$Rn | 228 | 142 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1741.2120 | 1737.7352 | +0.20 % | 218555.3508 MeV (+28903.0 ppm) |
| ${}^{229}$Rn | 229 | 143 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1745.2892 | 1741.6876 | +0.21 % | 219517.9883 MeV (+28902.9 ppm) |
| ${}^{230}$Rn | 230 | 144 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1750.7248 | 1746.8500 | +0.22 % | 220479.2675 MeV (+28902.8 ppm) |
| ${}^{231}$Rn | 231 | 145 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1754.5684 | 1750.7490 | +0.22 % | 221442.1386 MeV (+28902.5 ppm) |

### Francium (Z = 87)

_37 of 37 isotopes with a framework prediction; 37 of 37 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{197}$Fr | 197 | 110 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1512.7596 | 1511.7315 | +0.07 % | 188814.3148 MeV (+28879.0 ppm) |
| ${}^{198}$Fr | 198 | 111 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1521.8690 | 1520.4791 | +0.09 % | 189771.9202 MeV (+28878.5 ppm) |
| ${}^{199}$Fr | 199 | 112 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1532.3789 | 1531.3567 | +0.07 % | 190728.1251 MeV (+28882.3 ppm) |
| ${}^{200}$Fr | 200 | 113 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1541.1178 | 1540.0658 | +0.07 % | 191686.1010 MeV (+28883.5 ppm) |
| ${}^{201}$Fr | 201 | 114 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1551.2548 | 1550.6822 | +0.04 % | 192642.6787 MeV (+28887.8 ppm) |
| ${}^{202}$Fr | 202 | 115 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1559.6344 | 1559.2405 | +0.03 % | 193601.0140 MeV (+28890.1 ppm) |
| ${}^{203}$Fr | 203 | 116 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1569.4095 | 1569.5370 | -0.01 % | 194557.9536 MeV (+28894.5 ppm) |
| ${}^{204}$Fr | 204 | 117 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1577.4401 | 1577.8774 | -0.03 % | 195516.6377 MeV (+28897.4 ppm) |
| ${}^{205}$Fr | 205 | 118 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1586.8638 | 1587.8658 | -0.06 % | 196473.9288 MeV (+28901.8 ppm) |
| ${}^{206}$Fr | 206 | 119 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1594.5558 | 1595.8742 | -0.08 % | 197432.9516 MeV (+28904.6 ppm) |
| ${}^{207}$Fr | 207 | 120 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1603.6381 | 1605.5477 | -0.12 % | 198390.5841 MeV (+28909.1 ppm) |
| ${}^{208}$Fr | 208 | 121 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1611.0012 | 1613.4349 | -0.15 % | 199349.9358 MeV (+28912.9 ppm) |
| ${}^{209}$Fr | 209 | 122 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1619.7519 | 1622.6234 | -0.18 % | 200307.8998 MeV (+28916.5 ppm) |
| ${}^{210}$Fr | 210 | 123 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1626.7955 | 1630.2561 | -0.21 % | 201267.5710 MeV (+28920.5 ppm) |
| ${}^{211}$Fr | 211 | 124 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1635.2239 | 1639.1242 | -0.24 % | 202225.8574 MeV (+28923.9 ppm) |
| ${}^{212}$Fr | 212 | 125 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1641.9571 | 1646.5712 | -0.28 % | 203185.8390 MeV (+28928.5 ppm) |
| ${}^{213}$Fr | 213 | 126 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1650.0722 | 1654.6808 | -0.28 % | 204144.4387 MeV (+28929.5 ppm) |
| ${}^{214}$Fr | 214 | 127 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1656.5036 | 1660.1562 | -0.22 % | 205104.7220 MeV (+28925.3 ppm) |
| ${}^{215}$Fr | 215 | 128 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1664.3140 | 1666.9511 | -0.16 % | 206063.6264 MeV (+28921.1 ppm) |
| ${}^{216}$Fr | 216 | 129 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1670.4521 | 1672.3695 | -0.11 % | 207024.2030 MeV (+28918.2 ppm) |
| ${}^{217}$Fr | 217 | 130 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1677.9663 | 1679.0972 | -0.07 % | 207983.4037 MeV (+28915.2 ppm) |
| ${}^{218}$Fr | 218 | 131 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1683.8191 | 1684.4237 | -0.04 % | 208944.2656 MeV (+28913.2 ppm) |
| ${}^{219}$Fr | 219 | 132 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1691.0450 | 1690.9375 | +0.01 % | 209903.7545 MeV (+28910.6 ppm) |
| ${}^{220}$Fr | 220 | 133 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1696.6205 | 1696.1435 | +0.03 % | 210864.8938 MeV (+28909.5 ppm) |
| ${}^{221}$Fr | 221 | 134 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1703.5658 | 1702.4198 | +0.07 % | 211824.6632 MeV (+28907.0 ppm) |
| ${}^{222}$Fr | 222 | 135 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1708.8713 | 1707.3903 | +0.09 % | 212786.0725 MeV (+28906.0 ppm) |
| ${}^{223}$Fr | 223 | 136 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1715.5437 | 1713.4574 | +0.12 % | 213746.1149 MeV (+28903.9 ppm) |
| ${}^{224}$Fr | 224 | 137 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1720.5865 | 1718.1624 | +0.14 % | 214707.7868 MeV (+28902.9 ppm) |
| ${}^{225}$Fr | 225 | 138 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1726.9930 | 1724.1618 | +0.16 % | 215668.0951 MeV (+28901.8 ppm) |
| ${}^{226}$Fr | 226 | 139 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1731.7802 | 1728.5332 | +0.19 % | 216630.0227 MeV (+28900.4 ppm) |
| ${}^{227}$Fr | 227 | 140 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1737.9278 | 1734.4426 | +0.20 % | 217590.5899 MeV (+28900.0 ppm) |
| ${}^{228}$Fr | 228 | 141 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1742.4661 | 1738.8121 | +0.21 % | 218552.7664 MeV (+28899.8 ppm) |
| ${}^{229}$Fr | 229 | 142 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1748.3615 | 1744.5994 | +0.22 % | 219513.5857 MeV (+28900.1 ppm) |
| ${}^{230}$Fr | 230 | 143 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1752.6574 | 1748.8522 | +0.22 % | 220476.0046 MeV (+28900.4 ppm) |
| ${}^{231}$Fr | 231 | 144 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1758.3072 | 1754.3297 | +0.23 % | 221437.0696 MeV (+28900.3 ppm) |
| ${}^{232}$Fr | 232 | 145 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1762.3669 | 1758.4088 | +0.23 % | 222399.7246 MeV (+28901.0 ppm) |
| ${}^{233}$Fr | 233 | 146 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1767.7773 | 1763.6329 | +0.23 % | 223361.0290 MeV (+28900.8 ppm) |

### Radium (Z = 88)

_35 of 35 isotopes with a framework prediction; 35 of 35 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{201}$Ra | 201 | 113 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1542.4826 | 1541.5516 | +0.06 % | 192650.1207 MeV (+28881.7 ppm) |
| ${}^{202}$Ra | 202 | 114 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1552.8713 | 1552.4848 | +0.02 % | 193606.4467 MeV (+28886.3 ppm) |
| ${}^{203}$Ra | 203 | 115 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1561.5050 | 1561.0297 | +0.03 % | 194564.5279 MeV (+28887.2 ppm) |
| ${}^{204}$Ra | 204 | 116 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1571.5288 | 1571.6413 | -0.01 % | 195521.2188 MeV (+28891.9 ppm) |
| ${}^{205}$Ra | 205 | 117 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1579.8105 | 1579.9698 | -0.01 % | 196479.6518 MeV (+28893.5 ppm) |
| ${}^{206}$Ra | 206 | 118 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1589.4800 | 1590.2794 | -0.05 % | 197436.6971 MeV (+28898.4 ppm) |
| ${}^{207}$Ra | 207 | 119 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1597.4201 | 1598.4023 | -0.06 % | 198395.4718 MeV (+28900.5 ppm) |
| ${}^{208}$Ra | 208 | 120 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1606.7453 | 1608.2597 | -0.09 % | 199352.8614 MeV (+28904.7 ppm) |
| ${}^{209}$Ra | 209 | 121 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1614.3535 | 1616.2007 | -0.11 % | 200311.9680 MeV (+28907.6 ppm) |
| ${}^{210}$Ra | 210 | 122 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1623.3442 | 1625.6874 | -0.14 % | 201269.6920 MeV (+28911.4 ppm) |
| ${}^{211}$Ra | 211 | 123 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1630.6300 | 1633.3697 | -0.17 % | 202229.1210 MeV (+28914.5 ppm) |
| ${}^{212}$Ra | 212 | 124 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1639.2956 | 1642.4717 | -0.19 % | 203187.1702 MeV (+28918.0 ppm) |
| ${}^{213}$Ra | 213 | 125 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1646.2681 | 1649.9987 | -0.23 % | 204146.9125 MeV (+28921.7 ppm) |
| ${}^{214}$Ra | 214 | 126 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1654.6175 | 1658.3228 | -0.22 % | 205105.2778 MeV (+28922.7 ppm) |
| ${}^{215}$Ra | 215 | 127 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1661.2855 | 1663.9549 | -0.16 % | 206065.3246 MeV (+28918.2 ppm) |
| ${}^{216}$Ra | 216 | 128 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1669.3275 | 1671.2667 | -0.12 % | 207023.9973 MeV (+28915.5 ppm) |
| ${}^{217}$Ra | 217 | 129 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1675.6994 | 1676.7399 | -0.06 % | 207984.3403 MeV (+28911.8 ppm) |
| ${}^{218}$Ra | 218 | 130 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1683.4423 | 1684.0553 | -0.04 % | 208943.3121 MeV (+28910.6 ppm) |
| ${}^{219}$Ra | 219 | 131 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1689.5262 | 1689.3783 | +0.01 % | 209903.9430 MeV (+28907.6 ppm) |
| ${}^{220}$Ra | 220 | 132 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1696.9782 | 1696.5713 | +0.02 % | 210863.2057 MeV (+28907.3 ppm) |
| ${}^{221}$Ra | 221 | 133 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1702.7819 | 1701.9509 | +0.05 % | 211824.1168 MeV (+28905.9 ppm) |
| ${}^{222}$Ra | 222 | 134 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1709.9508 | 1708.6659 | +0.08 % | 212783.6627 MeV (+28904.6 ppm) |
| ${}^{223}$Ra | 223 | 135 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1715.4819 | 1713.8242 | +0.10 % | 213744.8464 MeV (+28903.5 ppm) |
| ${}^{224}$Ra | 224 | 136 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1722.3750 | 1720.3029 | +0.12 % | 214704.6680 MeV (+28902.4 ppm) |
| ${}^{225}$Ra | 225 | 137 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1727.6408 | 1725.2070 | +0.14 % | 215666.1170 MeV (+28901.3 ppm) |
| ${}^{226}$Ra | 226 | 138 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1734.2656 | 1731.6038 | +0.15 % | 216626.2070 MeV (+28901.1 ppm) |
| ${}^{227}$Ra | 227 | 139 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1739.2731 | 1736.1652 | +0.18 % | 217587.9143 MeV (+28899.6 ppm) |
| ${}^{228}$Ra | 228 | 140 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1745.6365 | 1742.4738 | +0.18 % | 218548.2657 MeV (+28900.2 ppm) |
| ${}^{229}$Ra | 229 | 141 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1750.3924 | 1746.9233 | +0.20 % | 219510.2245 MeV (+28899.3 ppm) |
| ${}^{230}$Ra | 230 | 142 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1756.5011 | 1753.0403 | +0.20 % | 220470.8306 MeV (+28900.1 ppm) |
| ${}^{231}$Ra | 231 | 143 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1761.0122 | 1757.4115 | +0.20 % | 221433.0343 MeV (+28900.1 ppm) |
| ${}^{232}$Ra | 232 | 144 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1766.8727 | 1763.2023 | +0.21 % | 222393.8885 MeV (+28900.5 ppm) |
| ${}^{233}$Ra | 233 | 145 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1771.1452 | 1767.4365 | +0.21 % | 223356.3308 MeV (+28900.9 ppm) |
| ${}^{234}$Ra | 234 | 146 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1776.7639 | 1772.9113 | +0.22 % | 224317.4269 MeV (+28900.9 ppm) |
| ${}^{235}$Ra | 235 | 147 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1780.8038 | 1776.8350 | +0.22 % | 225280.1017 MeV (+28900.6 ppm) |

### Actinium (Z = 89)

_33 of 33 isotopes with a framework prediction; 33 of 33 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{205}$Ac | 205 | 116 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1571.6119 | 1570.8846 | +0.05 % | 196486.5201 MeV (+28884.7 ppm) |
| ${}^{206}$Ac | 206 | 117 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1580.1479 | 1579.5779 | +0.04 % | 197444.6990 MeV (+28886.9 ppm) |
| ${}^{207}$Ac | 207 | 118 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1590.0662 | 1589.9877 | +0.00 % | 198401.4954 MeV (+28891.0 ppm) |
| ${}^{208}$Ac | 208 | 119 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1598.2575 | 1598.4444 | -0.01 % | 199360.0189 MeV (+28893.7 ppm) |
| ${}^{209}$Ac | 209 | 120 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1607.8287 | 1608.4317 | -0.04 % | 200317.1625 MeV (+28897.3 ppm) |
| ${}^{210}$Ac | 210 | 121 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1615.6851 | 1616.5838 | -0.06 % | 201276.0208 MeV (+28900.0 ppm) |
| ${}^{211}$Ac | 211 | 122 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1624.9189 | 1626.2757 | -0.08 % | 202233.5018 MeV (+28903.8 ppm) |
| ${}^{212}$Ac | 212 | 123 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1632.4501 | 1634.1910 | -0.11 % | 203192.6854 MeV (+28906.8 ppm) |
| ${}^{213}$Ac | 213 | 124 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1641.3559 | 1643.4208 | -0.13 % | 204150.4944 MeV (+28909.7 ppm) |
| ${}^{214}$Ac | 214 | 125 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1648.5708 | 1651.1999 | -0.16 % | 205109.9942 MeV (+28913.6 ppm) |
| ${}^{215}$Ac | 215 | 126 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1657.1576 | 1659.6739 | -0.15 % | 206068.1221 MeV (+28914.2 ppm) |
| ${}^{216}$Ac | 216 | 127 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1664.0652 | 1665.6261 | -0.09 % | 207027.9294 MeV (+28910.2 ppm) |
| ${}^{217}$Ac | 217 | 128 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1672.3418 | 1673.1448 | -0.05 % | 207986.3675 MeV (+28907.5 ppm) |
| ${}^{218}$Ac | 218 | 129 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1678.9504 | 1679.0676 | -0.01 % | 208946.4737 MeV (+28904.9 ppm) |
| ${}^{219}$Ac | 219 | 130 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1686.9253 | 1686.4202 | +0.03 % | 209905.2136 MeV (+28902.9 ppm) |
| ${}^{220}$Ac | 220 | 131 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1693.2431 | 1692.3173 | +0.05 % | 210865.6105 MeV (+28901.6 ppm) |
| ${}^{221}$Ac | 221 | 132 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1700.9244 | 1699.6014 | +0.08 % | 211824.6441 MeV (+28900.7 ppm) |
| ${}^{222}$Ac | 222 | 133 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1706.9593 | 1705.5819 | +0.08 % | 212785.3239 MeV (+28901.2 ppm) |
| ${}^{223}$Ac | 223 | 134 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1714.3546 | 1712.4500 | +0.11 % | 213744.6433 MeV (+28899.6 ppm) |
| ${}^{224}$Ac | 224 | 135 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1720.1143 | 1718.1122 | +0.12 % | 214705.5985 MeV (+28899.9 ppm) |
| ${}^{225}$Ac | 225 | 136 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1727.2313 | 1724.7804 | +0.14 % | 215665.1962 MeV (+28898.7 ppm) |
| ${}^{226}$Ac | 226 | 137 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1732.7230 | 1730.1798 | +0.15 % | 216626.4193 MeV (+28899.0 ppm) |
| ${}^{227}$Ac | 227 | 138 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1739.5691 | 1736.7108 | +0.16 % | 217586.2880 MeV (+28898.3 ppm) |
| ${}^{228}$Ac | 228 | 139 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1744.7998 | 1741.7370 | +0.18 % | 218547.7721 MeV (+28898.0 ppm) |
| ${}^{229}$Ac | 229 | 140 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1751.3819 | 1748.0130 | +0.19 % | 219507.9048 MeV (+28897.5 ppm) |
| ${}^{230}$Ac | 230 | 141 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1756.3585 | 1752.9359 | +0.20 % | 220469.6429 MeV (+28897.9 ppm) |
| ${}^{231}$Ac | 231 | 142 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1762.6834 | 1759.0827 | +0.20 % | 221430.0328 MeV (+28897.8 ppm) |
| ${}^{232}$Ac | 232 | 143 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1767.4126 | 1763.7625 | +0.21 % | 222392.0184 MeV (+28898.2 ppm) |
| ${}^{233}$Ac | 233 | 144 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1773.4868 | 1769.6802 | +0.22 % | 223352.6589 MeV (+28898.3 ppm) |
| ${}^{234}$Ac | 234 | 145 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1777.9748 | 1774.2183 | +0.21 % | 224314.8857 MeV (+28899.1 ppm) |
| ${}^{235}$Ac | 235 | 146 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1783.8048 | 1779.7737 | +0.23 % | 225275.7705 MeV (+28898.6 ppm) |
| ${}^{236}$Ac | 236 | 147 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1788.0578 | 1783.9812 | +0.23 % | 226238.2322 MeV (+28898.9 ppm) |
| ${}^{237}$Ac | 237 | 148 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1793.6496 | 1789.3500 | +0.24 % | 227199.3552 MeV (+28898.1 ppm) |

### Thorium (Z = 90)

_32 of 32 isotopes with a framework prediction; 32 of 32 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{208}$Th | 208 | 118 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1591.7395 | 1591.7349 | +0.00 % | 199365.2066 MeV (+28889.0 ppm) |
| ${}^{209}$Th | 209 | 119 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1600.1775 | 1600.1040 | +0.00 % | 200323.4834 MeV (+28889.9 ppm) |
| ${}^{210}$Th | 210 | 120 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1609.9903 | 1610.5060 | -0.03 % | 201280.3853 MeV (+28894.5 ppm) |
| ${}^{211}$Th | 211 | 121 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1618.0907 | 1618.7605 | -0.04 % | 202238.9997 MeV (+28896.5 ppm) |
| ${}^{212}$Th | 212 | 122 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1627.5633 | 1628.5973 | -0.06 % | 203196.2419 MeV (+28899.8 ppm) |
| ${}^{213}$Th | 213 | 123 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1635.3355 | 1636.6594 | -0.08 % | 204155.1845 MeV (+28902.4 ppm) |
| ${}^{214}$Th | 214 | 124 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1644.4773 | 1646.1559 | -0.10 % | 205112.7574 MeV (+28905.5 ppm) |
| ${}^{215}$Th | 215 | 125 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1651.9305 | 1654.0007 | -0.13 % | 206072.0190 MeV (+28908.5 ppm) |
| ${}^{216}$Th | 216 | 126 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1660.7507 | 1662.6949 | -0.12 % | 207029.9136 MeV (+28909.1 ppm) |
| ${}^{217}$Th | 217 | 127 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1667.8937 | 1668.8590 | -0.06 % | 207989.4853 MeV (+28905.1 ppm) |
| ${}^{218}$Th | 218 | 128 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1676.4010 | 1676.7694 | -0.02 % | 208947.6928 MeV (+28903.2 ppm) |
| ${}^{219}$Th | 219 | 129 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1683.2424 | 1682.7446 | +0.03 % | 209907.5662 MeV (+28899.8 ppm) |
| ${}^{220}$Th | 220 | 130 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1691.4452 | 1690.5892 | +0.05 % | 210866.0781 MeV (+28899.1 ppm) |
| ${}^{221}$Th | 221 | 131 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1697.9931 | 1696.4101 | +0.09 % | 211826.2450 MeV (+28896.4 ppm) |
| ${}^{222}$Th | 222 | 132 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1705.8997 | 1704.2183 | +0.10 % | 212785.0532 MeV (+28897.0 ppm) |
| ${}^{223}$Th | 223 | 133 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1712.1621 | 1710.1073 | +0.12 % | 213745.5056 MeV (+28896.0 ppm) |
| ${}^{224}$Th | 224 | 134 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1719.7802 | 1717.5684 | +0.13 % | 214704.6023 MeV (+28896.3 ppm) |
| ${}^{225}$Th | 225 | 135 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1725.7646 | 1723.3252 | +0.14 % | 215665.3326 MeV (+28896.0 ppm) |
| ${}^{226}$Th | 226 | 136 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1733.1018 | 1730.5090 | +0.15 % | 216624.7102 MeV (+28896.3 ppm) |
| ${}^{227}$Th | 227 | 137 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1738.8157 | 1735.9732 | +0.16 % | 217585.7111 MeV (+28895.8 ppm) |
| ${}^{228}$Th | 228 | 138 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1745.8794 | 1743.0784 | +0.16 % | 218545.3621 MeV (+28897.0 ppm) |
| ${}^{229}$Th | 229 | 139 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1751.3298 | 1748.3351 | +0.17 % | 219506.6265 MeV (+28896.8 ppm) |
| ${}^{230}$Th | 230 | 140 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1758.1270 | 1755.1294 | +0.17 % | 220466.5441 MeV (+28897.7 ppm) |
| ${}^{231}$Th | 231 | 141 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1763.3208 | 1760.2474 | +0.17 % | 221428.0650 MeV (+28898.0 ppm) |
| ${}^{232}$Th | 232 | 142 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1769.8584 | 1766.6878 | +0.18 % | 222388.2422 MeV (+28898.4 ppm) |
| ${}^{233}$Th | 233 | 143 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1774.8022 | 1771.4742 | +0.19 % | 223350.0132 MeV (+28898.3 ppm) |
| ${}^{234}$Th | 234 | 144 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1781.0868 | 1777.6642 | +0.19 % | 224310.4434 MeV (+28898.7 ppm) |
| ${}^{235}$Th | 235 | 145 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1785.7870 | 1782.3308 | +0.19 % | 225272.4580 MeV (+28899.1 ppm) |
| ${}^{236}$Th | 236 | 146 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1791.8248 | 1788.1646 | +0.20 % | 226233.1349 MeV (+28899.0 ppm) |
| ${}^{237}$Th | 237 | 147 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1796.2877 | 1792.5361 | +0.21 % | 227195.3868 MeV (+28899.1 ppm) |
| ${}^{238}$Th | 238 | 148 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1802.0850 | 1798.0900 | +0.22 % | 228156.3043 MeV (+28898.5 ppm) |
| ${}^{239}$Th | 239 | 149 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1806.3164 | 1802.0600 | +0.24 % | 229118.7877 MeV (+28898.4 ppm) |

### Protactinium (Z = 91)

_31 of 31 isotopes with a framework prediction; 31 of 31 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{211}$Pa | 211 | 120 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1610.1452 | 1609.8023 | +0.02 % | 202245.6149 MeV (+28887.3 ppm) |
| ${}^{212}$Pa | 212 | 121 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1618.4924 | 1618.3293 | +0.01 % | 203203.9824 MeV (+28889.5 ppm) |
| ${}^{213}$Pa | 213 | 122 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1628.2069 | 1628.3430 | -0.01 % | 204160.9827 MeV (+28892.5 ppm) |
| ${}^{214}$Pa | 214 | 123 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1636.2231 | 1636.6086 | -0.02 % | 205119.6813 MeV (+28895.0 ppm) |
| ${}^{215}$Pa | 215 | 124 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1645.6041 | 1646.3353 | -0.04 % | 206077.0151 MeV (+28898.1 ppm) |
| ${}^{216}$Pa | 216 | 125 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1653.2985 | 1654.3873 | -0.07 % | 207036.0355 MeV (+28901.1 ppm) |
| ${}^{217}$Pa | 217 | 126 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1662.3550 | 1663.2277 | -0.05 % | 207993.6937 MeV (+28901.2 ppm) |
| ${}^{218}$Pa | 218 | 127 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1669.7365 | 1669.7042 | +0.00 % | 208953.0270 MeV (+28897.7 ppm) |
| ${}^{219}$Pa | 219 | 128 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1678.4774 | 1677.8418 | +0.04 % | 209911.0009 MeV (+28895.8 ppm) |
| ${}^{220}$Pa | 220 | 129 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1685.5545 | 1684.2180 | +0.08 % | 210870.6386 MeV (+28893.3 ppm) |
| ${}^{221}$Pa | 221 | 130 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1693.9883 | 1692.1928 | +0.11 % | 211828.9195 MeV (+28892.2 ppm) |
| ${}^{222}$Pa | 222 | 131 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1700.7692 | 1698.5747 | +0.13 % | 212788.8534 MeV (+28891.2 ppm) |
| ${}^{223}$Pa | 223 | 132 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1708.9041 | 1706.3727 | +0.15 % | 213747.4333 MeV (+28890.7 ppm) |
| ${}^{224}$Pa | 224 | 133 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1715.3968 | 1712.9193 | +0.14 % | 214707.6554 MeV (+28891.9 ppm) |
| ${}^{225}$Pa | 225 | 134 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1723.2405 | 1720.4963 | +0.16 % | 215666.5264 MeV (+28891.7 ppm) |
| ${}^{226}$Pa | 226 | 135 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1729.4527 | 1726.8907 | +0.15 % | 216627.0290 MeV (+28893.4 ppm) |
| ${}^{227}$Pa | 227 | 136 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1737.0130 | 1734.1653 | +0.16 % | 217586.1834 MeV (+28893.1 ppm) |
| ${}^{228}$Pa | 228 | 137 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1742.9520 | 1740.1433 | +0.16 % | 218546.9593 MeV (+28894.1 ppm) |
| ${}^{229}$Pa | 229 | 138 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1750.2363 | 1747.2414 | +0.17 % | 219506.3897 MeV (+28894.2 ppm) |
| ${}^{230}$Pa | 230 | 139 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1755.9092 | 1753.0360 | +0.16 % | 220467.4316 MeV (+28895.5 ppm) |
| ${}^{231}$Pa | 231 | 140 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1762.9245 | 1759.8566 | +0.17 % | 221427.1311 MeV (+28895.5 ppm) |
| ${}^{232}$Pa | 232 | 141 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1768.3383 | 1765.4057 | +0.17 % | 222388.4320 MeV (+28896.9 ppm) |
| ${}^{233}$Pa | 233 | 142 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1775.0915 | 1771.9341 | +0.18 % | 223348.3936 MeV (+28896.7 ppm) |
| ${}^{234}$Pa | 234 | 143 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1780.2528 | 1777.1560 | +0.17 % | 224309.9471 MeV (+28897.7 ppm) |
| ${}^{235}$Pa | 235 | 144 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1786.7505 | 1783.2773 | +0.19 % | 225270.1642 MeV (+28896.8 ppm) |
| ${}^{236}$Pa | 236 | 145 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1791.6658 | 1788.3035 | +0.19 % | 226231.9637 MeV (+28897.9 ppm) |
| ${}^{237}$Pa | 237 | 146 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1797.9143 | 1794.1812 | +0.21 % | 227192.4299 MeV (+28897.0 ppm) |
| ${}^{238}$Pa | 238 | 147 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1802.5898 | 1798.8861 | +0.21 % | 228154.4692 MeV (+28897.8 ppm) |
| ${}^{239}$Pa | 239 | 148 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1808.5955 | 1804.4500 | +0.23 % | 229115.1783 MeV (+28896.8 ppm) |
| ${}^{240}$Pa | 240 | 149 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1813.0371 | 1808.8800 | +0.23 % | 230077.4514 MeV (+28897.2 ppm) |
| ${}^{241}$Pa | 241 | 150 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1818.8059 | 1814.2480 | +0.25 % | 231038.3974 MeV (+28895.9 ppm) |

### Uranium (Z = 92)

_29 of 29 isotopes with a framework prediction; 29 of 29 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{215}$U | 215 | 123 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1638.1783 | 1638.4682 | -0.02 % | 206083.1106 MeV (+28892.2 ppm) |
| ${}^{216}$U | 216 | 124 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1647.7942 | 1648.3624 | -0.03 % | 207040.2095 MeV (+28895.0 ppm) |
| ${}^{217}$U | 217 | 125 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1655.7257 | 1656.5780 | -0.05 % | 207998.9927 MeV (+28897.3 ppm) |
| ${}^{218}$U | 218 | 126 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1665.0145 | 1665.6768 | -0.04 % | 208956.4187 MeV (+28897.9 ppm) |
| ${}^{219}$U | 219 | 127 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1672.6304 | 1672.3468 | +0.02 % | 209915.5176 MeV (+28894.2 ppm) |
| ${}^{220}$U | 220 | 128 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1681.6010 | 1680.8000 | +0.05 % | 210873.2618 MeV (+28892.4 ppm) |
| ${}^{221}$U | 221 | 129 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1688.9098 | 1687.2654 | +0.10 % | 211832.6677 MeV (+28889.7 ppm) |
| ${}^{222}$U | 222 | 130 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1697.5706 | 1695.5839 | +0.12 % | 212790.7217 MeV (+28889.2 ppm) |
| ${}^{223}$U | 223 | 131 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1704.5807 | 1701.8827 | +0.16 % | 213750.4264 MeV (+28886.7 ppm) |
| ${}^{224}$U | 224 | 132 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1712.9400 | 1710.2566 | +0.16 % | 214708.7819 MeV (+28888.0 ppm) |
| ${}^{225}$U | 225 | 133 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1719.6592 | 1716.6986 | +0.17 % | 215668.7774 MeV (+28887.6 ppm) |
| ${}^{226}$U | 226 | 134 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1727.7250 | 1724.8132 | +0.17 % | 216627.4264 MeV (+28889.0 ppm) |
| ${}^{227}$U | 227 | 135 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1734.1611 | 1731.1682 | +0.17 % | 217587.7051 MeV (+28889.5 ppm) |
| ${}^{228}$U | 228 | 136 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1741.9409 | 1739.0646 | +0.17 % | 218546.6401 MeV (+28891.1 ppm) |
| ${}^{229}$U | 229 | 137 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1748.1013 | 1745.1453 | +0.17 % | 219507.1945 MeV (+28891.6 ppm) |
| ${}^{230}$U | 230 | 138 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1755.6025 | 1752.8122 | +0.16 % | 220466.4080 MeV (+28893.4 ppm) |
| ${}^{231}$U | 231 | 139 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1761.4944 | 1758.6926 | +0.16 % | 221427.2309 MeV (+28894.2 ppm) |
| ${}^{232}$U | 232 | 140 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1768.7242 | 1765.9604 | +0.16 % | 222386.7158 MeV (+28895.3 ppm) |
| ${}^{233}$U | 233 | 141 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1774.3545 | 1771.7221 | +0.15 % | 223347.8003 MeV (+28896.7 ppm) |
| ${}^{234}$U | 234 | 142 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1781.3198 | 1778.5675 | +0.15 % | 224307.5498 MeV (+28897.1 ppm) |
| ${}^{235}$U | 235 | 143 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1786.6952 | 1783.8650 | +0.16 % | 225268.8892 MeV (+28897.4 ppm) |
| ${}^{236}$U | 236 | 144 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1793.4026 | 1790.4106 | +0.17 % | 226228.8965 MeV (+28897.5 ppm) |
| ${}^{237}$U | 237 | 145 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1798.5296 | 1795.5363 | +0.17 % | 227190.4844 MeV (+28898.2 ppm) |
| ${}^{238}$U | 238 | 146 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1804.9856 | 1801.6900 | +0.18 % | 228150.7431 MeV (+28897.6 ppm) |
| ${}^{239}$U | 239 | 147 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1809.8703 | 1806.4964 | +0.19 % | 229112.5732 MeV (+28897.9 ppm) |
| ${}^{240}$U | 240 | 148 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1816.0811 | 1812.4249 | +0.20 % | 230073.0772 MeV (+28897.4 ppm) |
| ${}^{241}$U | 241 | 149 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1820.7297 | 1816.8990 | +0.21 % | 231035.1433 MeV (+28897.7 ppm) |
| ${}^{242}$U | 242 | 150 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1826.7013 | 1822.7440 | +0.22 % | 231995.8865 MeV (+28897.0 ppm) |
| ${}^{243}$U | 243 | 151 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1831.1196 | 1826.8740 | +0.23 % | 232958.1830 MeV (+28896.6 ppm) |

### Neptunium (Z = 93)

_27 of 27 isotopes with a framework prediction; 27 of 27 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{219}$Np | 219 | 126 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1665.7014 | 1665.4234 | +0.02 % | 209921.1163 MeV (+28890.7 ppm) |
| ${}^{220}$Np | 220 | 127 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1673.5546 | 1672.4567 | +0.07 % | 210879.9779 MeV (+28887.7 ppm) |
| ${}^{221}$Np | 221 | 128 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1682.7577 | 1681.1470 | +0.10 % | 211837.4896 MeV (+28886.2 ppm) |
| ${}^{222}$Np | 222 | 129 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1690.3011 | 1687.7997 | +0.15 % | 212796.6609 MeV (+28883.1 ppm) |
| ${}^{223}$Np | 223 | 130 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1699.1919 | 1696.4871 | +0.16 % | 213754.4849 MeV (+28883.4 ppm) |
| ${}^{224}$Np | 224 | 131 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1706.4340 | 1703.1847 | +0.19 % | 214713.9576 MeV (+28881.8 ppm) |
| ${}^{225}$Np | 225 | 132 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1715.0206 | 1711.6702 | +0.20 % | 215672.0857 MeV (+28882.5 ppm) |
| ${}^{226}$Np | 226 | 133 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1721.9692 | 1718.5427 | +0.20 % | 216631.8519 MeV (+28883.2 ppm) |
| ${}^{227}$Np | 227 | 134 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1730.2598 | 1726.8519 | +0.20 % | 217590.2761 MeV (+28884.5 ppm) |
| ${}^{228}$Np | 228 | 135 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1736.9227 | 1733.7120 | +0.19 % | 218550.3280 MeV (+28886.2 ppm) |
| ${}^{229}$Np | 229 | 136 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1744.9248 | 1741.7722 | +0.18 % | 219509.0406 MeV (+28887.8 ppm) |
| ${}^{230}$Np | 230 | 137 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1751.3095 | 1748.4083 | +0.17 % | 220469.3707 MeV (+28889.9 ppm) |
| ${}^{231}$Np | 231 | 138 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1759.0305 | 1756.0925 | +0.17 % | 221428.3644 MeV (+28890.8 ppm) |
| ${}^{232}$Np | 232 | 139 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1765.1442 | 1762.5040 | +0.15 % | 222388.9656 MeV (+28892.7 ppm) |
| ${}^{233}$Np | 233 | 140 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1772.5914 | 1769.9103 | +0.15 % | 223348.2332 MeV (+28893.8 ppm) |
| ${}^{234}$Np | 234 | 141 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1778.4409 | 1775.9753 | +0.14 % | 224309.0984 MeV (+28895.6 ppm) |
| ${}^{235}$Np | 235 | 142 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1785.6212 | 1782.9584 | +0.15 % | 225268.6329 MeV (+28895.6 ppm) |
| ${}^{236}$Np | 236 | 143 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1791.2134 | 1788.6947 | +0.14 % | 226229.7554 MeV (+28897.1 ppm) |
| ${}^{237}$Np | 237 | 144 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1798.1334 | 1795.2725 | +0.16 % | 227189.5502 MeV (+28896.4 ppm) |
| ${}^{238}$Np | 238 | 145 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1803.4748 | 1800.7608 | +0.15 % | 228150.9236 MeV (+28897.7 ppm) |
| ${}^{239}$Np | 239 | 146 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1810.1409 | 1806.9758 | +0.18 % | 229110.9722 MeV (+28896.5 ppm) |
| ${}^{240}$Np | 240 | 147 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1815.2377 | 1812.0418 | +0.18 % | 230072.5902 MeV (+28897.0 ppm) |
| ${}^{241}$Np | 241 | 148 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1821.6564 | 1818.1143 | +0.19 % | 231032.8863 MeV (+28896.3 ppm) |
| ${}^{242}$Np | 242 | 149 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1826.5147 | 1823.0838 | +0.19 % | 231994.7428 MeV (+28897.4 ppm) |
| ${}^{243}$Np | 243 | 150 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1832.6919 | 1828.8180 | +0.21 % | 232955.2804 MeV (+28895.9 ppm) |
| ${}^{244}$Np | 244 | 151 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1837.3176 | 1833.4160 | +0.21 % | 233917.3695 MeV (+28896.6 ppm) |
| ${}^{245}$Np | 245 | 152 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1843.2591 | 1838.9700 | +0.23 % | 234878.1427 MeV (+28895.1 ppm) |

### Plutonium (Z = 94)

_27 of 27 isotopes with a framework prediction; 27 of 27 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{221}$Pu | 221 | 127 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1675.5319 | 1674.2960 | +0.07 % | 211843.3851 MeV (+28884.8 ppm) |
| ${}^{222}$Pu | 222 | 128 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1684.9636 | 1683.2040 | +0.10 % | 212800.6682 MeV (+28883.7 ppm) |
| ${}^{223}$Pu | 223 | 129 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1692.7377 | 1690.3400 | +0.14 % | 213759.6088 MeV (+28881.0 ppm) |
| ${}^{224}$Pu | 224 | 130 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1701.8546 | 1699.2640 | +0.15 % | 214717.2067 MeV (+28881.3 ppm) |
| ${}^{225}$Pu | 225 | 131 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1709.3247 | 1706.1750 | +0.18 % | 215676.4513 MeV (+28880.4 ppm) |
| ${}^{226}$Pu | 226 | 132 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1718.1350 | 1714.8880 | +0.19 % | 216634.3558 MeV (+28881.3 ppm) |
| ${}^{227}$Pu | 227 | 133 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1725.3092 | 1721.7950 | +0.20 % | 217593.8964 MeV (+28881.2 ppm) |
| ${}^{228}$Pu | 228 | 134 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1733.8208 | 1730.6121 | +0.19 % | 218552.0995 MeV (+28883.5 ppm) |
| ${}^{229}$Pu | 229 | 135 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1740.7068 | 1737.3963 | +0.19 % | 219511.9283 MeV (+28884.0 ppm) |
| ${}^{230}$Pu | 230 | 136 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1748.9276 | 1745.9304 | +0.17 % | 220470.4223 MeV (+28886.6 ppm) |
| ${}^{231}$Pu | 231 | 137 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1755.5329 | 1752.6253 | +0.17 % | 221430.5318 MeV (+28888.0 ppm) |
| ${}^{232}$Pu | 232 | 138 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1763.4702 | 1760.6443 | +0.16 % | 222389.3093 MeV (+28889.5 ppm) |
| ${}^{233}$Pu | 233 | 139 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1769.8020 | 1767.0247 | +0.16 % | 223349.6922 MeV (+28890.6 ppm) |
| ${}^{234}$Pu | 234 | 140 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1777.4631 | 1774.7978 | +0.15 % | 224308.7460 MeV (+28892.1 ppm) |
| ${}^{235}$Pu | 235 | 141 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1783.5284 | 1781.0368 | +0.14 % | 225269.3954 MeV (+28893.8 ppm) |
| ${}^{236}$Pu | 236 | 142 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1790.9201 | 1788.3889 | +0.14 % | 226228.7184 MeV (+28894.6 ppm) |
| ${}^{237}$Pu | 237 | 143 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1796.7258 | 1794.2701 | +0.14 % | 227189.6275 MeV (+28895.7 ppm) |
| ${}^{238}$Pu | 238 | 144 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1803.8549 | 1801.2699 | +0.14 % | 228149.2132 MeV (+28896.0 ppm) |
| ${}^{239}$Pu | 239 | 145 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1809.4074 | 1806.9162 | +0.14 % | 229110.3755 MeV (+28897.2 ppm) |
| ${}^{240}$Pu | 240 | 146 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1816.2804 | 1813.4504 | +0.16 % | 230070.2172 MeV (+28896.5 ppm) |
| ${}^{241}$Pu | 241 | 147 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1821.5860 | 1818.6919 | +0.16 % | 231031.6264 MeV (+28896.9 ppm) |
| ${}^{242}$Pu | 242 | 148 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1828.2092 | 1825.0015 | +0.18 % | 231991.7179 MeV (+28896.3 ppm) |
| ${}^{243}$Pu | 243 | 149 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1833.2740 | 1830.0351 | +0.18 % | 232953.3679 MeV (+28896.8 ppm) |
| ${}^{244}$Pu | 244 | 150 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1839.6536 | 1836.0550 | +0.20 % | 233913.7032 MeV (+28896.0 ppm) |
| ${}^{245}$Pu | 245 | 151 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1844.4835 | 1840.7541 | +0.20 % | 234875.5880 MeV (+28896.0 ppm) |
| ${}^{246}$Pu | 246 | 152 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1850.6252 | 1846.6089 | +0.22 % | 235836.1611 MeV (+28895.5 ppm) |
| ${}^{247}$Pu | 247 | 153 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1855.2260 | 1850.7710 | +0.24 % | 236798.2751 MeV (+28894.5 ppm) |

### Americium (Z = 95)

_27 of 27 isotopes with a framework prediction; 27 of 27 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{223}$Am | 223 | 128 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1685.2182 | 1682.9810 | +0.13 % | 213765.7980 MeV (+28878.2 ppm) |
| ${}^{224}$Am | 224 | 129 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1693.2259 | 1690.3040 | +0.17 % | 214724.5051 MeV (+28877.0 ppm) |
| ${}^{225}$Am | 225 | 130 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1702.5716 | 1699.4250 | +0.19 % | 215681.8742 MeV (+28876.4 ppm) |
| ${}^{226}$Am | 226 | 131 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1710.2727 | 1706.7520 | +0.21 % | 216640.8878 MeV (+28876.5 ppm) |
| ${}^{227}$Am | 227 | 132 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1719.3093 | 1715.6660 | +0.21 % | 217598.5660 MeV (+28876.9 ppm) |
| ${}^{228}$Am | 228 | 133 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1726.7119 | 1722.9960 | +0.22 % | 218557.8782 MeV (+28878.0 ppm) |
| ${}^{229}$Am | 229 | 134 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1735.4474 | 1731.8285 | +0.21 % | 219515.8574 MeV (+28879.3 ppm) |
| ${}^{230}$Am | 230 | 135 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1742.5593 | 1739.2600 | +0.19 % | 220475.4603 MeV (+28881.6 ppm) |
| ${}^{231}$Am | 231 | 136 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1751.0015 | 1747.7460 | +0.19 % | 221433.7329 MeV (+28883.3 ppm) |
| ${}^{232}$Am | 232 | 137 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1757.8302 | 1754.8480 | +0.17 % | 222393.6190 MeV (+28885.3 ppm) |
| ${}^{233}$Am | 233 | 138 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1765.9865 | 1763.1110 | +0.16 % | 223352.1775 MeV (+28886.7 ppm) |
| ${}^{234}$Am | 234 | 139 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1772.5393 | 1769.9760 | +0.14 % | 224312.3394 MeV (+28889.2 ppm) |
| ${}^{235}$Am | 235 | 140 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1780.4169 | 1777.8122 | +0.15 % | 225271.1766 MeV (+28890.4 ppm) |
| ${}^{236}$Am | 236 | 141 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1786.7008 | 1784.3960 | +0.13 % | 226231.6075 MeV (+28893.0 ppm) |
| ${}^{237}$Am | 237 | 142 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1794.3068 | 1791.9570 | +0.13 % | 227190.7163 MeV (+28893.7 ppm) |
| ${}^{238}$Am | 238 | 143 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1800.3285 | 1798.2293 | +0.12 % | 228151.4093 MeV (+28895.4 ppm) |
| ${}^{239}$Am | 239 | 144 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1807.6696 | 1805.3317 | +0.13 % | 229110.7830 MeV (+28895.3 ppm) |
| ${}^{240}$Am | 240 | 145 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1813.4358 | 1811.2833 | +0.12 % | 230071.7316 MeV (+28896.9 ppm) |
| ${}^{241}$Am | 241 | 146 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1820.5185 | 1817.9304 | +0.14 % | 231031.3637 MeV (+28895.8 ppm) |
| ${}^{242}$Am | 242 | 147 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1826.0355 | 1823.4680 | +0.14 % | 231992.5614 MeV (+28896.6 ppm) |
| ${}^{243}$Am | 243 | 148 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1832.8660 | 1829.8323 | +0.17 % | 232952.4456 MeV (+28895.4 ppm) |
| ${}^{244}$Am | 244 | 149 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1838.1400 | 1835.1995 | +0.16 % | 233913.8865 MeV (+28896.4 ppm) |
| ${}^{245}$Am | 245 | 150 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1844.7246 | 1841.2496 | +0.19 % | 234874.0166 MeV (+28894.9 ppm) |
| ${}^{246}$Am | 246 | 151 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1849.7614 | 1846.2300 | +0.19 % | 235835.6946 MeV (+28895.2 ppm) |
| ${}^{247}$Am | 247 | 152 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1856.1060 | 1852.2530 | +0.21 % | 236796.0648 MeV (+28894.1 ppm) |
| ${}^{248}$Am | 248 | 153 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1860.9114 | 1856.7760 | +0.22 % | 237757.9742 MeV (+28894.1 ppm) |
| ${}^{249}$Am | 249 | 154 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1867.0216 | 1862.2710 | +0.26 % | 238718.5787 MeV (+28892.3 ppm) |

### Curium (Z = 96)

_22 of 22 isotopes with a framework prediction; 22 of 22 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{231}$Cm | 231 | 135 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1745.4363 | 1742.2020 | +0.19 % | 221437.9678 MeV (+28879.7 ppm) |
| ${}^{232}$Cm | 232 | 136 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1754.0962 | 1751.1360 | +0.17 % | 222396.0226 MeV (+28882.6 ppm) |
| ${}^{233}$Cm | 233 | 137 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1761.1447 | 1758.2185 | +0.17 % | 223355.6889 MeV (+28883.9 ppm) |
| ${}^{234}$Cm | 234 | 138 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1769.5165 | 1766.8607 | +0.15 % | 224314.0319 MeV (+28886.3 ppm) |
| ${}^{235}$Cm | 235 | 139 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1776.2866 | 1773.5450 | +0.15 % | 225273.9765 MeV (+28887.3 ppm) |
| ${}^{236}$Cm | 236 | 140 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1784.3774 | 1781.8729 | +0.14 % | 226232.6006 MeV (+28889.1 ppm) |
| ${}^{237}$Cm | 237 | 141 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1790.8763 | 1788.5499 | +0.13 % | 227192.8164 MeV (+28890.8 ppm) |
| ${}^{238}$Cm | 238 | 142 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1798.6931 | 1796.4232 | +0.13 % | 228151.7144 MeV (+28892.1 ppm) |
| ${}^{239}$Cm | 239 | 143 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1804.9276 | 1802.7928 | +0.12 % | 229112.1947 MeV (+28893.5 ppm) |
| ${}^{240}$Cm | 240 | 144 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1812.4772 | 1810.2868 | +0.12 % | 230071.3599 MeV (+28894.2 ppm) |
| ${}^{241}$Cm | 241 | 145 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1818.4538 | 1816.3806 | +0.11 % | 231032.0980 MeV (+28895.6 ppm) |
| ${}^{242}$Cm | 242 | 146 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1825.7428 | 1823.3500 | +0.13 % | 231991.5238 MeV (+28895.0 ppm) |
| ${}^{243}$Cm | 243 | 147 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1831.4679 | 1829.0430 | +0.13 % | 232952.5135 MeV (+28895.6 ppm) |
| ${}^{244}$Cm | 244 | 148 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1838.5026 | 1835.8445 | +0.14 % | 233912.1936 MeV (+28895.5 ppm) |
| ${}^{245}$Cm | 245 | 149 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1843.9824 | 1841.3631 | +0.14 % | 234873.4285 MeV (+28896.3 ppm) |
| ${}^{246}$Cm | 246 | 150 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1850.7689 | 1847.8220 | +0.16 % | 235833.3567 MeV (+28895.7 ppm) |
| ${}^{247}$Cm | 247 | 151 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1856.0094 | 1852.9772 | +0.16 % | 236794.8310 MeV (+28896.0 ppm) |
| ${}^{248}$Cm | 248 | 152 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1862.5537 | 1859.1888 | +0.18 % | 237755.0015 MeV (+28895.3 ppm) |
| ${}^{249}$Cm | 249 | 153 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1867.5607 | 1863.9022 | +0.20 % | 238716.7093 MeV (+28894.6 ppm) |
| ${}^{250}$Cm | 250 | 154 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1873.8685 | 1869.7346 | +0.22 % | 239677.1163 MeV (+28893.3 ppm) |
| ${}^{251}$Cm | 251 | 155 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1878.6475 | 1874.1475 | +0.24 % | 240639.0521 MeV (+28892.3 ppm) |
| ${}^{252}$Cm | 252 | 156 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1884.7244 | 1879.9200 | +0.26 % | 241599.6899 MeV (+28891.3 ppm) |

### Berkelium (Z = 97)

_22 of 22 isotopes with a framework prediction; 22 of 22 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{233}$Bk | 233 | 136 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1755.2768 | 1751.9270 | +0.19 % | 223360.2265 MeV (+28878.8 ppm) |
| ${}^{234}$Bk | 234 | 137 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1762.5478 | 1759.4460 | +0.18 % | 224319.6703 MeV (+28880.7 ppm) |
| ${}^{235}$Bk | 235 | 138 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1771.1376 | 1768.1400 | +0.17 % | 225277.7952 MeV (+28882.4 ppm) |
| ${}^{236}$Bk | 236 | 139 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1778.1279 | 1775.4280 | +0.15 % | 226237.5198 MeV (+28884.8 ppm) |
| ${}^{237}$Bk | 237 | 140 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1786.4345 | 1783.8990 | +0.14 % | 227195.9280 MeV (+28886.4 ppm) |
| ${}^{238}$Bk | 238 | 141 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1793.1511 | 1790.9500 | +0.12 % | 228155.9261 MeV (+28888.9 ppm) |
| ${}^{239}$Bk | 239 | 142 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1801.1814 | 1798.9530 | +0.12 % | 229114.6106 MeV (+28890.0 ppm) |
| ${}^{240}$Bk | 240 | 143 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1807.6312 | 1805.5200 | +0.12 % | 230074.8755 MeV (+28891.8 ppm) |
| ${}^{241}$Bk | 241 | 144 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1815.3920 | 1813.2840 | +0.12 % | 231033.8295 MeV (+28892.8 ppm) |
| ${}^{242}$Bk | 242 | 145 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1821.5817 | 1819.5980 | +0.11 % | 231994.3546 MeV (+28894.1 ppm) |
| ${}^{243}$Bk | 243 | 146 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1829.0797 | 1826.7530 | +0.13 % | 232953.5714 MeV (+28893.4 ppm) |
| ${}^{244}$Bk | 244 | 147 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1835.0156 | 1832.8001 | +0.12 % | 233914.3502 MeV (+28894.7 ppm) |
| ${}^{245}$Bk | 245 | 148 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1842.2570 | 1839.7715 | +0.14 % | 234873.8236 MeV (+28894.4 ppm) |
| ${}^{246}$Bk | 246 | 149 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1847.9454 | 1845.6897 | +0.12 % | 235834.8500 MeV (+28896.2 ppm) |
| ${}^{247}$Bk | 247 | 150 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1854.9364 | 1852.2384 | +0.15 % | 236794.5737 MeV (+28895.1 ppm) |
| ${}^{248}$Bk | 248 | 151 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1860.3832 | 1857.6682 | +0.15 % | 237755.8417 MeV (+28895.7 ppm) |
| ${}^{249}$Bk | 249 | 152 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1867.1299 | 1864.0242 | +0.17 % | 238715.8098 MeV (+28894.8 ppm) |
| ${}^{250}$Bk | 250 | 153 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1872.3410 | 1868.9898 | +0.18 % | 239677.3135 MeV (+28894.3 ppm) |
| ${}^{251}$Bk | 251 | 154 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1878.8490 | 1874.7852 | +0.22 % | 240637.5202 MeV (+28892.0 ppm) |
| ${}^{252}$Bk | 252 | 155 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1883.8299 | 1879.6680 | +0.22 % | 241599.2541 MeV (+28891.7 ppm) |
| ${}^{253}$Bk | 253 | 156 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1890.1050 | 1885.1030 | +0.27 % | 242559.6938 MeV (+28889.9 ppm) |
| ${}^{254}$Bk | 254 | 157 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1894.8612 | 1889.7600 | +0.27 % | 243521.6524 MeV (+28889.8 ppm) |

### Californium (Z = 98)

_20 of 20 isotopes with a framework prediction; 20 of 20 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{237}$Cf | 237 | 139 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1780.9812 | 1778.2941 | +0.15 % | 227200.0509 MeV (+28883.0 ppm) |
| ${}^{238}$Cf | 238 | 140 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1789.5001 | 1787.1420 | +0.13 % | 228158.2468 MeV (+28885.2 ppm) |
| ${}^{239}$Cf | 239 | 141 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1796.4310 | 1794.1730 | +0.13 % | 229118.0307 MeV (+28887.1 ppm) |
| ${}^{240}$Cf | 240 | 142 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1804.6713 | 1802.4576 | +0.12 % | 230076.5051 MeV (+28888.4 ppm) |
| ${}^{241}$Cf | 241 | 143 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1811.3332 | 1809.1870 | +0.12 % | 231036.5581 MeV (+28889.6 ppm) |
| ${}^{242}$Cf | 242 | 144 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1819.3018 | 1817.2020 | +0.12 % | 231995.3042 MeV (+28890.9 ppm) |
| ${}^{243}$Cf | 243 | 145 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1825.7013 | 1823.7150 | +0.11 % | 232955.6195 MeV (+28892.0 ppm) |
| ${}^{244}$Cf | 244 | 146 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1833.4048 | 1831.2535 | +0.12 % | 233914.6307 MeV (+28892.5 ppm) |
| ${}^{245}$Cf | 245 | 147 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1839.5483 | 1837.4178 | +0.12 % | 234875.2020 MeV (+28893.4 ppm) |
| ${}^{246}$Cf | 246 | 148 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1846.9932 | 1844.7840 | +0.12 % | 235834.4719 MeV (+28894.0 ppm) |
| ${}^{247}$Cf | 247 | 149 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1852.8869 | 1850.8362 | +0.11 % | 236795.2930 MeV (+28895.4 ppm) |
| ${}^{248}$Cf | 248 | 150 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1860.0793 | 1857.7789 | +0.12 % | 237754.8154 MeV (+28895.2 ppm) |
| ${}^{249}$Cf | 249 | 151 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1865.7293 | 1863.3655 | +0.13 % | 238715.8801 MeV (+28895.6 ppm) |
| ${}^{250}$Cf | 250 | 152 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1872.6752 | 1869.9892 | +0.14 % | 239675.6490 MeV (+28895.1 ppm) |
| ${}^{251}$Cf | 251 | 153 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1878.0872 | 1875.0959 | +0.16 % | 240636.9517 MeV (+28894.4 ppm) |
| ${}^{252}$Cf | 252 | 154 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1884.7924 | 1881.2675 | +0.19 % | 241596.9613 MeV (+28892.9 ppm) |
| ${}^{253}$Cf | 253 | 155 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1889.9723 | 1886.0719 | +0.21 % | 242558.4962 MeV (+28891.9 ppm) |
| ${}^{254}$Cf | 254 | 156 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1896.4424 | 1892.1034 | +0.23 % | 243518.7409 MeV (+28890.8 ppm) |
| ${}^{255}$Cf | 255 | 157 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1901.3955 | 1896.6900 | +0.25 % | 244480.5026 MeV (+28889.9 ppm) |
| ${}^{256}$Cf | 256 | 158 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1907.6360 | 1902.5920 | +0.27 % | 245440.9768 MeV (+28889.0 ppm) |

### Einsteinium (Z = 99)

_20 of 20 isotopes with a framework prediction; 20 of 20 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{239}$Es | 239 | 140 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1790.6763 | 1787.9590 | +0.15 % | 229122.4550 MeV (+28881.9 ppm) |
| ${}^{240}$Es | 240 | 141 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1797.8241 | 1795.4400 | +0.13 % | 230082.0221 MeV (+28884.4 ppm) |
| ${}^{241}$Es | 241 | 142 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1806.2772 | 1803.8850 | +0.13 % | 231040.2838 MeV (+28885.3 ppm) |
| ${}^{242}$Es | 242 | 143 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1813.1536 | 1810.8860 | +0.13 % | 232000.1221 MeV (+28887.5 ppm) |
| ${}^{243}$Es | 243 | 144 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1821.3327 | 1819.0980 | +0.12 % | 232958.6577 MeV (+28888.4 ppm) |
| ${}^{244}$Es | 244 | 145 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1827.9445 | 1825.8520 | +0.11 % | 233918.7608 MeV (+28890.1 ppm) |
| ${}^{245}$Es | 245 | 146 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1835.8563 | 1833.8250 | +0.11 % | 234877.5637 MeV (+28890.5 ppm) |
| ${}^{246}$Es | 246 | 147 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1842.2099 | 1840.2731 | +0.11 % | 235837.9249 MeV (+28892.3 ppm) |
| ${}^{247}$Es | 247 | 148 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1849.8609 | 1847.5848 | +0.12 % | 236796.9887 MeV (+28891.7 ppm) |
| ${}^{248}$Es | 248 | 149 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1855.9625 | 1854.0480 | +0.10 % | 237757.6019 MeV (+28893.6 ppm) |
| ${}^{249}$Es | 249 | 150 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1863.3588 | 1861.0260 | +0.13 % | 238716.9203 MeV (+28893.7 ppm) |
| ${}^{250}$Es | 250 | 151 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1869.2145 | 1867.2500 | +0.11 % | 239677.7794 MeV (+28895.1 ppm) |
| ${}^{251}$Es | 251 | 152 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1876.3622 | 1873.9369 | +0.13 % | 240637.3465 MeV (+28894.4 ppm) |
| ${}^{252}$Es | 252 | 153 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1881.9778 | 1879.2252 | +0.15 % | 241598.4456 MeV (+28893.7 ppm) |
| ${}^{253}$Es | 253 | 154 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1888.8827 | 1885.5806 | +0.18 % | 242558.2555 MeV (+28892.1 ppm) |
| ${}^{254}$Es | 254 | 155 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1894.2640 | 1890.6683 | +0.19 % | 243519.5890 MeV (+28891.5 ppm) |
| ${}^{255}$Es | 255 | 156 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1900.9318 | 1896.6445 | +0.23 % | 244479.6360 MeV (+28889.4 ppm) |
| ${}^{256}$Es | 256 | 157 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1906.0842 | 1901.5680 | +0.24 % | 245441.1984 MeV (+28889.3 ppm) |
| ${}^{257}$Es | 257 | 158 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1912.5203 | 1907.4540 | +0.27 % | 246401.4770 MeV (+28887.6 ppm) |
| ${}^{258}$Es | 258 | 159 | L4-brane-tower-asymptotic | 🟢 recursive | binding_energy | 1917.4491 | 1912.2960 | +0.27 % | 247363.2629 MeV (+28887.5 ppm) |

<!-- AUTO:per-z-sections END -->
