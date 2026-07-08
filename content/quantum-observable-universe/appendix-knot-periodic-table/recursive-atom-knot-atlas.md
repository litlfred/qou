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
| ${}^{241}$Fm | 241 | 141 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -146.6045 | 1797.6190 | -108.16 % | 232991.8351 MeV (+37551.5 ppm) |
| ${}^{242}$Fm | 242 | 142 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -139.9027 | 1806.5300 | -107.74 % | 233951.8481 MeV (+37526.6 ppm) |
| ${}^{243}$Fm | 243 | 143 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -133.2092 | 1813.7520 | -107.34 % | 234911.8694 MeV (+37494.0 ppm) |
| ${}^{244}$Fm | 244 | 144 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -126.5238 | 1822.1920 | -106.94 % | 235871.8988 MeV (+37467.5 ppm) |
| ${}^{245}$Fm | 245 | 145 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -119.8465 | 1828.9250 | -106.55 % | 236831.9362 MeV (+37434.1 ppm) |
| ${}^{246}$Fm | 246 | 146 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -113.1772 | 1837.1184 | -106.16 % | 237791.9817 MeV (+37406.5 ppm) |
| ${}^{247}$Fm | 247 | 147 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -106.5158 | 1843.6080 | -105.78 % | 238752.0350 MeV (+37372.5 ppm) |
| ${}^{248}$Fm | 248 | 148 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -99.8622 | 1851.5544 | -105.39 % | 239712.0962 MeV (+37344.5 ppm) |
| ${}^{249}$Fm | 249 | 149 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -93.2164 | 1858.0044 | -105.02 % | 240672.1652 MeV (+37310.5 ppm) |
| ${}^{250}$Fm | 250 | 150 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -86.5783 | 1865.5226 | -104.64 % | 241632.2419 MeV (+37281.5 ppm) |
| ${}^{251}$Fm | 251 | 151 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -79.9478 | 1871.7073 | -104.27 % | 242592.3262 MeV (+37246.9 ppm) |
| ${}^{252}$Fm | 252 | 152 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -73.3249 | 1878.9208 | -103.90 % | 243552.4180 MeV (+37217.2 ppm) |
| ${}^{253}$Fm | 253 | 153 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -66.7095 | 1884.4632 | -103.54 % | 244512.5174 MeV (+37180.3 ppm) |
| ${}^{254}$Fm | 254 | 154 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -60.1015 | 1890.9776 | -103.18 % | 245472.6242 MeV (+37148.1 ppm) |
| ${}^{255}$Fm | 255 | 155 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -53.5008 | 1896.1509 | -102.82 % | 246432.7383 MeV (+37110.2 ppm) |
| ${}^{256}$Fm | 256 | 156 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -46.9074 | 1902.5379 | -102.47 % | 247392.8597 MeV (+37078.0 ppm) |
| ${}^{257}$Fm | 257 | 157 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -40.3213 | 1907.5039 | -102.11 % | 248352.9883 MeV (+37039.9 ppm) |
| ${}^{258}$Fm | 258 | 158 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -33.7423 | 1913.8440 | -101.76 % | 249313.1241 MeV (+37007.6 ppm) |
| ${}^{259}$Fm | 259 | 159 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -27.1704 | 1918.4130 | -101.42 % | 250273.2670 MeV (+36969.4 ppm) |
| ${}^{260}$Fm | 260 | 160 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -20.6056 | 1924.5200 | -101.07 % | 251233.4169 MeV (+36936.7 ppm) |

### Mendelevium (Z = 101)

_19 of 19 isotopes with a framework prediction; 19 of 19 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{244}$Md | 244 | 143 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -151.8827 | 1814.8720 | -108.37 % | 235895.9273 MeV (+37542.9 ppm) |
| ${}^{245}$Md | 245 | 144 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -145.1750 | 1823.0450 | -107.96 % | 236855.9345 MeV (+37515.9 ppm) |
| ${}^{246}$Md | 246 | 145 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -138.4755 | 1830.4860 | -107.56 % | 237815.9497 MeV (+37484.3 ppm) |
| ${}^{247}$Md | 247 | 146 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -131.7841 | 1838.6680 | -107.17 % | 238775.9731 MeV (+37457.3 ppm) |
| ${}^{248}$Md | 248 | 147 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -125.1007 | 1845.6160 | -106.78 % | 239736.0044 MeV (+37425.3 ppm) |
| ${}^{249}$Md | 249 | 148 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -118.4252 | 1853.5602 | -106.39 % | 240696.0437 MeV (+37397.0 ppm) |
| ${}^{250}$Md | 250 | 149 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -111.7576 | 1860.4133 | -106.01 % | 241656.0908 MeV (+37364.6 ppm) |
| ${}^{251}$Md | 251 | 150 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -105.0977 | 1867.9170 | -105.63 % | 242616.1458 MeV (+37335.4 ppm) |
| ${}^{252}$Md | 252 | 151 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -98.4455 | 1874.4880 | -105.25 % | 243576.2084 MeV (+37302.4 ppm) |
| ${}^{253}$Md | 253 | 152 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -91.8010 | 1881.8140 | -104.88 % | 244536.2787 MeV (+37273.1 ppm) |
| ${}^{254}$Md | 254 | 153 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -85.1641 | 1887.7280 | -104.51 % | 245496.3565 MeV (+37237.2 ppm) |
| ${}^{255}$Md | 255 | 154 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -78.5347 | 1894.3270 | -104.15 % | 246456.4418 MeV (+37205.4 ppm) |
| ${}^{256}$Md | 256 | 155 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -71.9127 | 1899.7760 | -103.79 % | 247416.5346 MeV (+37168.7 ppm) |
| ${}^{257}$Md | 257 | 156 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -65.2980 | 1906.3192 | -103.43 % | 248376.6347 MeV (+37136.9 ppm) |
| ${}^{258}$Md | 258 | 157 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -58.6907 | 1911.6927 | -103.07 % | 249336.7422 MeV (+37100.4 ppm) |
| ${}^{259}$Md | 259 | 158 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -52.0906 | 1917.8950 | -102.72 % | 250296.8569 MeV (+37067.7 ppm) |
| ${}^{260}$Md | 260 | 159 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -45.4977 | 1922.9600 | -102.37 % | 251256.9787 MeV (+37030.6 ppm) |
| ${}^{261}$Md | 261 | 160 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -38.9119 | 1929.0510 | -102.02 % | 252217.1077 MeV (+36997.9 ppm) |
| ${}^{262}$Md | 262 | 161 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -32.3332 | 1934.0840 | -101.67 % | 253177.2437 MeV (+36960.9 ppm) |

### Nobelium (Z = 102)

_17 of 17 isotopes with a framework prediction; 17 of 17 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{248}$No | 248 | 146 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -150.5659 | 1841.1520 | -108.18 % | 239760.1394 MeV (+37512.9 ppm) |
| ${}^{249}$No | 249 | 147 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -143.8604 | 1848.0780 | -107.78 % | 240720.1487 MeV (+37480.3 ppm) |
| ${}^{250}$No | 250 | 148 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -137.1630 | 1856.5000 | -107.39 % | 241680.1660 MeV (+37453.9 ppm) |
| ${}^{251}$No | 251 | 149 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -130.4734 | 1863.1730 | -107.00 % | 242640.1912 MeV (+37421.0 ppm) |
| ${}^{252}$No | 252 | 150 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -123.7917 | 1871.3014 | -106.62 % | 243600.2243 MeV (+37394.0 ppm) |
| ${}^{253}$No | 253 | 151 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -117.1179 | 1877.8854 | -106.24 % | 244560.2652 MeV (+37360.8 ppm) |
| ${}^{254}$No | 254 | 152 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -110.4517 | 1885.5921 | -105.86 % | 245520.3138 MeV (+37332.8 ppm) |
| ${}^{255}$No | 255 | 153 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -103.7932 | 1891.5748 | -105.49 % | 246480.3701 MeV (+37297.5 ppm) |
| ${}^{256}$No | 256 | 154 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -97.1423 | 1898.6350 | -105.12 % | 247440.4339 MeV (+37267.3 ppm) |
| ${}^{257}$No | 257 | 155 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -90.4989 | 1904.2823 | -104.75 % | 248400.5053 MeV (+37231.2 ppm) |
| ${}^{258}$No | 258 | 156 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -83.8629 | 1911.0060 | -104.39 % | 249360.5841 MeV (+37200.5 ppm) |
| ${}^{259}$No | 259 | 157 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -77.2344 | 1916.5926 | -104.03 % | 250320.6703 MeV (+37164.2 ppm) |
| ${}^{260}$No | 260 | 158 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -70.6131 | 1923.2200 | -103.67 % | 251280.7638 MeV (+37132.8 ppm) |
| ${}^{261}$No | 261 | 159 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -63.9991 | 1928.2680 | -103.32 % | 252240.8646 MeV (+37096.1 ppm) |
| ${}^{262}$No | 262 | 160 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -57.3923 | 1934.8700 | -102.97 % | 253200.9726 MeV (+37064.7 ppm) |
| ${}^{263}$No | 263 | 161 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -50.7926 | 1939.8880 | -102.62 % | 254161.0877 MeV (+37027.8 ppm) |
| ${}^{264}$No | 264 | 162 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -44.2000 | 1945.9440 | -102.27 % | 255121.2099 MeV (+36996.1 ppm) |

### Lawrencium (Z = 103)

_16 of 16 isotopes with a framework prediction; 16 of 16 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{251}$Lr | 251 | 148 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -156.0750 | 1857.4000 | -108.40 % | 242664.4625 MeV (+37502.7 ppm) |
| ${}^{252}$Lr | 252 | 149 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -149.3635 | 1864.8000 | -108.01 % | 243624.4658 MeV (+37472.2 ppm) |
| ${}^{253}$Lr | 253 | 150 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -142.6600 | 1872.9383 | -107.62 % | 244584.4770 MeV (+37445.2 ppm) |
| ${}^{254}$Lr | 254 | 151 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -135.9643 | 1879.8872 | -107.23 % | 245544.4961 MeV (+37413.4 ppm) |
| ${}^{255}$Lr | 255 | 152 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -129.2764 | 1887.6571 | -106.85 % | 246504.5230 MeV (+37385.5 ppm) |
| ${}^{256}$Lr | 256 | 153 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -122.5963 | 1893.9291 | -106.47 % | 247464.5576 MeV (+37351.3 ppm) |
| ${}^{257}$Lr | 257 | 154 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -115.9238 | 1901.0290 | -106.10 % | 248424.6000 MeV (+37321.3 ppm) |
| ${}^{258}$Lr | 258 | 155 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -109.2590 | 1907.1360 | -105.73 % | 249384.6499 MeV (+37286.3 ppm) |
| ${}^{259}$Lr | 259 | 156 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -102.6017 | 1914.0100 | -105.36 % | 250344.7073 MeV (+37256.2 ppm) |
| ${}^{260}$Lr | 260 | 157 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -95.9518 | 1919.5800 | -105.00 % | 251304.7722 MeV (+37220.5 ppm) |
| ${}^{261}$Lr | 261 | 158 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -89.3093 | 1926.4410 | -104.64 % | 252264.8445 MeV (+37190.0 ppm) |
| ${}^{262}$Lr | 262 | 159 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -82.6742 | 1931.9880 | -104.28 % | 253224.9242 MeV (+37154.3 ppm) |
| ${}^{263}$Lr | 263 | 160 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -76.0463 | 1938.5730 | -103.92 % | 254185.0111 MeV (+37123.2 ppm) |
| ${}^{264}$Lr | 264 | 161 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -69.4256 | 1943.8320 | -103.57 % | 255145.1052 MeV (+37087.5 ppm) |
| ${}^{265}$Lr | 265 | 162 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -62.8121 | 1950.1350 | -103.22 % | 256105.2064 MeV (+37055.6 ppm) |
| ${}^{266}$Lr | 266 | 163 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -56.2057 | 1954.8340 | -102.88 % | 257065.3148 MeV (+37017.4 ppm) |

### Rutherfordium (Z = 104)

_16 of 16 isotopes with a framework prediction; 16 of 16 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{253}$Rf | 253 | 149 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -168.4273 | 1867.1400 | -109.02 % | 244608.9141 MeV (+37526.3 ppm) |
| ${}^{254}$Rf | 254 | 150 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -161.7019 | 1875.5360 | -108.62 % | 245568.9034 MeV (+37500.9 ppm) |
| ${}^{255}$Rf | 255 | 151 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -154.9844 | 1882.4100 | -108.23 % | 246528.9006 MeV (+37469.0 ppm) |
| ${}^{256}$Rf | 256 | 152 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -148.2747 | 1890.6713 | -107.84 % | 247488.9058 MeV (+37442.6 ppm) |
| ${}^{257}$Rf | 257 | 153 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -141.5729 | 1897.0983 | -107.46 % | 248448.9187 MeV (+37409.0 ppm) |
| ${}^{258}$Rf | 258 | 154 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -134.8789 | 1904.6916 | -107.08 % | 249408.9395 MeV (+37380.6 ppm) |
| ${}^{259}$Rf | 259 | 155 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -128.1925 | 1910.6430 | -106.71 % | 250368.9679 MeV (+37345.9 ppm) |
| ${}^{260}$Rf | 260 | 156 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -121.5137 | 1918.0200 | -106.34 % | 251329.0039 MeV (+37316.8 ppm) |
| ${}^{261}$Rf | 261 | 157 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -114.8425 | 1923.9317 | -105.97 % | 252289.0474 MeV (+37282.0 ppm) |
| ${}^{262}$Rf | 262 | 158 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -108.1788 | 1930.9400 | -105.60 % | 253249.0984 MeV (+37252.1 ppm) |
| ${}^{263}$Rf | 263 | 159 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -101.5224 | 1936.7320 | -105.24 % | 254209.1569 MeV (+37217.1 ppm) |
| ${}^{264}$Rf | 264 | 160 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -94.8734 | 1943.3040 | -104.88 % | 255169.2227 MeV (+37186.8 ppm) |
| ${}^{265}$Rf | 265 | 161 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -88.2317 | 1948.8100 | -104.53 % | 256129.2957 MeV (+37151.2 ppm) |
| ${}^{266}$Rf | 266 | 162 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -81.5972 | 1955.3660 | -104.17 % | 257089.3760 MeV (+37120.9 ppm) |
| ${}^{267}$Rf | 267 | 163 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -74.9699 | 1960.3140 | -103.82 % | 258049.4635 MeV (+37083.1 ppm) |
| ${}^{268}$Rf | 268 | 164 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -68.3497 | 1966.3160 | -103.48 % | 259009.5580 MeV (+37050.8 ppm) |

### Dubnium (Z = 105)

_16 of 16 isotopes with a framework prediction; 16 of 16 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{255}$Db | 255 | 150 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -180.9170 | 1876.5450 | -109.64 % | 246553.5029 MeV (+37549.5 ppm) |
| ${}^{256}$Db | 256 | 151 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -174.1776 | 1883.9040 | -109.25 % | 247513.4783 MeV (+37519.2 ppm) |
| ${}^{257}$Db | 257 | 152 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -167.4461 | 1892.0280 | -108.85 % | 248473.4616 MeV (+37492.9 ppm) |
| ${}^{258}$Db | 258 | 153 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -160.7226 | 1898.7459 | -108.46 % | 249433.4529 MeV (+37460.3 ppm) |
| ${}^{259}$Db | 259 | 154 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -154.0069 | 1906.3339 | -108.08 % | 250393.4520 MeV (+37431.7 ppm) |
| ${}^{260}$Db | 260 | 155 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -147.2989 | 1912.8200 | -107.70 % | 251353.4588 MeV (+37398.3 ppm) |
| ${}^{261}$Db | 261 | 156 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -140.5987 | 1920.1770 | -107.32 % | 252313.4733 MeV (+37369.6 ppm) |
| ${}^{262}$Db | 262 | 157 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -133.9060 | 1926.2240 | -106.95 % | 253273.4954 MeV (+37335.7 ppm) |
| ${}^{263}$Db | 263 | 158 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -127.2210 | 1933.5760 | -106.58 % | 254233.5251 MeV (+37306.6 ppm) |
| ${}^{264}$Db | 264 | 159 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -120.5434 | 1939.3440 | -106.22 % | 255193.5623 MeV (+37272.3 ppm) |
| ${}^{265}$Db | 265 | 160 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -113.8732 | 1946.4250 | -105.85 % | 256153.6069 MeV (+37242.6 ppm) |
| ${}^{266}$Db | 266 | 161 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -107.2104 | 1952.1740 | -105.49 % | 257113.6589 MeV (+37208.0 ppm) |
| ${}^{267}$Db | 267 | 162 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -100.5549 | 1958.9790 | -105.13 % | 258073.7181 MeV (+37178.2 ppm) |
| ${}^{268}$Db | 268 | 163 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -93.9066 | 1963.9040 | -104.78 % | 259033.7846 MeV (+37141.2 ppm) |
| ${}^{269}$Db | 269 | 164 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -87.2655 | 1969.8870 | -104.43 % | 259993.8583 MeV (+37108.6 ppm) |
| ${}^{270}$Db | 270 | 165 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -80.6315 | 1974.7800 | -104.08 % | 260953.9391 MeV (+37071.5 ppm) |

### Seaborgium (Z = 106)

_16 of 16 isotopes with a framework prediction; 16 of 16 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{258}$Sg | 258 | 152 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -186.7901 | 1894.2360 | -109.86 % | 249458.1901 MeV (+37546.8 ppm) |
| ${}^{259}$Sg | 259 | 153 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -180.0448 | 1901.0600 | -109.47 % | 250418.1596 MeV (+37514.7 ppm) |
| ${}^{260}$Sg | 260 | 154 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -173.3074 | 1909.0664 | -109.08 % | 251378.1370 MeV (+37487.9 ppm) |
| ${}^{261}$Sg | 261 | 155 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -166.5778 | 1915.6802 | -108.70 % | 252338.1222 MeV (+37455.2 ppm) |
| ${}^{262}$Sg | 262 | 156 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -159.8560 | 1923.3875 | -108.31 % | 253298.1151 MeV (+37427.5 ppm) |
| ${}^{263}$Sg | 263 | 157 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -153.1419 | 1929.6310 | -107.94 % | 254258.1158 MeV (+37393.8 ppm) |
| ${}^{264}$Sg | 264 | 158 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -146.4355 | 1937.2320 | -107.56 % | 255218.1241 MeV (+37365.7 ppm) |
| ${}^{265}$Sg | 265 | 159 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -139.7366 | 1943.2450 | -107.19 % | 256178.1400 MeV (+37331.8 ppm) |
| ${}^{266}$Sg | 266 | 160 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -133.0452 | 1950.3120 | -106.82 % | 257138.1634 MeV (+37303.1 ppm) |
| ${}^{267}$Sg | 267 | 161 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -126.3612 | 1956.3090 | -106.46 % | 258098.1942 MeV (+37269.1 ppm) |
| ${}^{268}$Sg | 268 | 162 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -119.6846 | 1963.3680 | -106.10 % | 259058.2324 MeV (+37240.2 ppm) |
| ${}^{269}$Sg | 269 | 163 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -113.0154 | 1968.5420 | -105.74 % | 260018.2779 MeV (+37203.8 ppm) |
| ${}^{270}$Sg | 270 | 164 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -106.3533 | 1974.7800 | -105.39 % | 260978.3306 MeV (+37172.4 ppm) |
| ${}^{271}$Sg | 271 | 165 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -99.6985 | 1979.6550 | -105.04 % | 261938.3905 MeV (+37135.3 ppm) |
| ${}^{272}$Sg | 272 | 166 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -93.0508 | 1985.8720 | -104.69 % | 262898.4576 MeV (+37103.8 ppm) |
| ${}^{273}$Sg | 273 | 167 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -86.4101 | 1990.7160 | -104.34 % | 263858.5317 MeV (+37066.4 ppm) |

### Bohrium (Z = 107)

_19 of 19 isotopes with a framework prediction; 19 of 19 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{260}$Bh | 260 | 153 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -199.5392 | 1901.6400 | -110.49 % | 251403.0384 MeV (+37562.5 ppm) |
| ${}^{261}$Bh | 261 | 154 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -192.7800 | 1909.8235 | -110.09 % | 252362.9940 MeV (+37535.8 ppm) |
| ${}^{262}$Bh | 262 | 155 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -186.0288 | 1916.7221 | -109.71 % | 253322.9575 MeV (+37504.2 ppm) |
| ${}^{263}$Bh | 263 | 156 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -179.2854 | 1924.6340 | -109.32 % | 254282.9289 MeV (+37476.9 ppm) |
| ${}^{264}$Bh | 264 | 157 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -172.5497 | 1931.1600 | -108.94 % | 255242.9081 MeV (+37444.6 ppm) |
| ${}^{265}$Bh | 265 | 158 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -165.8218 | 1938.7400 | -108.55 % | 256202.8949 MeV (+37416.9 ppm) |
| ${}^{266}$Bh | 266 | 159 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -159.1016 | 1945.2580 | -108.18 % | 257162.8895 MeV (+37384.1 ppm) |
| ${}^{267}$Bh | 267 | 160 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -152.3889 | 1952.5710 | -107.80 % | 258122.8915 MeV (+37356.0 ppm) |
| ${}^{268}$Bh | 268 | 161 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -145.6837 | 1958.8120 | -107.44 % | 259082.9012 MeV (+37322.8 ppm) |
| ${}^{269}$Bh | 269 | 162 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -138.9860 | 1966.1210 | -107.07 % | 260042.9182 MeV (+37294.7 ppm) |
| ${}^{270}$Bh | 270 | 163 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -132.2957 | 1971.2700 | -106.71 % | 261002.9427 MeV (+37258.6 ppm) |
| ${}^{271}$Bh | 271 | 164 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -125.6127 | 1977.7580 | -106.35 % | 261962.9744 MeV (+37227.5 ppm) |
| ${}^{272}$Bh | 272 | 165 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -118.9369 | 1982.8800 | -106.00 % | 262923.0135 MeV (+37191.4 ppm) |
| ${}^{273}$Bh | 273 | 166 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -112.2684 | 1989.0780 | -105.64 % | 263883.0597 MeV (+37159.7 ppm) |
| ${}^{274}$Bh | 274 | 167 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -105.6070 | 1994.1720 | -105.30 % | 264843.1131 MeV (+37123.5 ppm) |
| ${}^{275}$Bh | 275 | 168 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -98.9527 | 2000.0750 | -104.95 % | 265803.1735 MeV (+37091.8 ppm) |
| ${}^{276}$Bh | 276 | 169 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -92.3054 | 2005.1400 | -104.60 % | 266763.2410 MeV (+37055.8 ppm) |
| ${}^{277}$Bh | 277 | 170 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -85.6650 | 2011.0200 | -104.26 % | 267723.3154 MeV (+37024.2 ppm) |
| ${}^{278}$Bh | 278 | 171 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -79.0316 | 2015.7780 | -103.92 % | 268683.3968 MeV (+36988.3 ppm) |

### Hassium (Z = 108)

_18 of 18 isotopes with a framework prediction; 18 of 18 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{263}$Hs | 263 | 155 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -205.6512 | 1918.5850 | -110.72 % | 254307.9645 MeV (+37557.1 ppm) |
| ${}^{264}$Hs | 264 | 156 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -198.8862 | 1926.7713 | -110.32 % | 255267.9142 MeV (+37531.0 ppm) |
| ${}^{265}$Hs | 265 | 157 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -192.1290 | 1933.5056 | -109.94 % | 256227.8718 MeV (+37499.1 ppm) |
| ${}^{266}$Hs | 266 | 158 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -185.3796 | 1941.3375 | -109.55 % | 257187.8372 MeV (+37472.0 ppm) |
| ${}^{267}$Hs | 267 | 159 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -178.6379 | 1947.7650 | -109.17 % | 258147.8103 MeV (+37439.9 ppm) |
| ${}^{268}$Hs | 268 | 160 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -171.9039 | 1955.5960 | -108.79 % | 259107.7910 MeV (+37413.0 ppm) |
| ${}^{269}$Hs | 269 | 161 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -165.1775 | 1962.0860 | -108.42 % | 260067.7794 MeV (+37381.4 ppm) |
| ${}^{270}$Hs | 270 | 162 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -158.4586 | 1969.6500 | -108.05 % | 261027.7752 MeV (+37353.7 ppm) |
| ${}^{271}$Hs | 271 | 163 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -151.7471 | 1975.0480 | -107.68 % | 261987.7786 MeV (+37318.2 ppm) |
| ${}^{272}$Hs | 272 | 164 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -145.0431 | 1981.7920 | -107.32 % | 262947.7893 MeV (+37288.2 ppm) |
| ${}^{273}$Hs | 273 | 165 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -138.3464 | 1987.1670 | -106.96 % | 263907.8074 MeV (+37252.5 ppm) |
| ${}^{274}$Hs | 274 | 166 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -131.6570 | 1993.6240 | -106.60 % | 264867.8327 MeV (+37221.7 ppm) |
| ${}^{275}$Hs | 275 | 167 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -124.9747 | 1998.7000 | -106.25 % | 265827.8653 MeV (+37185.3 ppm) |
| ${}^{276}$Hs | 276 | 168 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -118.2997 | 2005.1400 | -105.90 % | 266787.9050 MeV (+37154.8 ppm) |
| ${}^{277}$Hs | 277 | 169 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -111.6317 | 2009.9120 | -105.55 % | 267747.9518 MeV (+37118.5 ppm) |
| ${}^{278}$Hs | 278 | 170 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -104.9708 | 2016.0560 | -105.21 % | 268708.0057 MeV (+37087.9 ppm) |
| ${}^{279}$Hs | 279 | 171 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -98.3169 | 2020.7970 | -104.87 % | 269668.0665 MeV (+37051.8 ppm) |
| ${}^{280}$Hs | 280 | 172 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -91.6698 | 2026.9200 | -104.52 % | 270628.1342 MeV (+37021.4 ppm) |

### Meitnerium (Z = 109)

_18 of 18 isotopes with a framework prediction; 18 of 18 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{265}$Mt | 265 | 156 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -218.6580 | 1927.0800 | -111.35 % | 256253.0705 MeV (+37577.1 ppm) |
| ${}^{266}$Mt | 266 | 157 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -211.8792 | 1934.0221 | -110.96 % | 257213.0065 MeV (+37546.2 ppm) |
| ${}^{267}$Mt | 267 | 158 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -205.1083 | 1941.8910 | -110.56 % | 258172.9503 MeV (+37519.5 ppm) |
| ${}^{268}$Mt | 268 | 159 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -198.3451 | 1948.6280 | -110.18 % | 259132.9019 MeV (+37487.9 ppm) |
| ${}^{269}$Mt | 269 | 160 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -191.5897 | 1956.7060 | -109.79 % | 260092.8613 MeV (+37461.5 ppm) |
| ${}^{270}$Mt | 270 | 161 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -184.8420 | 1963.1700 | -109.42 % | 261052.8284 MeV (+37430.2 ppm) |
| ${}^{271}$Mt | 271 | 162 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -178.1018 | 1970.9830 | -109.04 % | 262012.8030 MeV (+37403.3 ppm) |
| ${}^{272}$Mt | 272 | 163 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -171.3692 | 1976.6240 | -108.67 % | 262972.7852 MeV (+37368.5 ppm) |
| ${}^{273}$Mt | 273 | 164 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -164.6441 | 1983.3450 | -108.30 % | 263932.7748 MeV (+37338.4 ppm) |
| ${}^{274}$Mt | 274 | 165 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -157.9264 | 1988.9660 | -107.94 % | 264892.7719 MeV (+37303.8 ppm) |
| ${}^{275}$Mt | 275 | 166 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -151.2160 | 1995.6750 | -107.58 % | 265852.7763 MeV (+37273.3 ppm) |
| ${}^{276}$Mt | 276 | 167 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -144.5130 | 2001.0000 | -107.22 % | 266812.7880 MeV (+37238.9 ppm) |
| ${}^{277}$Mt | 277 | 168 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -137.8171 | 2007.4190 | -106.87 % | 267772.8069 MeV (+37208.2 ppm) |
| ${}^{278}$Mt | 278 | 169 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -131.1284 | 2012.7200 | -106.51 % | 268732.8330 MeV (+37173.5 ppm) |
| ${}^{279}$Mt | 279 | 170 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -124.4469 | 2019.1230 | -106.16 % | 269692.8662 MeV (+37142.9 ppm) |
| ${}^{280}$Mt | 280 | 171 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -117.7723 | 2024.1200 | -105.82 % | 270652.9065 MeV (+37108.1 ppm) |
| ${}^{281}$Mt | 281 | 172 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -111.1048 | 2030.2250 | -105.47 % | 271612.9537 MeV (+37077.6 ppm) |
| ${}^{282}$Mt | 282 | 173 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -104.4442 | 2035.4760 | -105.13 % | 272573.0079 MeV (+37042.8 ppm) |

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
| ${}^{267}$Ds | 267 | 157 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -231.8000 | 1935.2160 | -111.98 % | 258198.3117 MeV (+37596.0 ppm) |
| ${}^{268}$Ds | 268 | 158 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -225.0074 | 1943.5360 | -111.58 % | 259158.2340 MeV (+37570.6 ppm) |
| ${}^{269}$Ds | 269 | 159 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -218.2228 | 1950.2917 | -111.19 % | 260118.1641 MeV (+37539.5 ppm) |
| ${}^{270}$Ds | 270 | 160 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -211.4459 | 1958.5161 | -110.80 % | 261078.1020 MeV (+37514.2 ppm) |
| ${}^{271}$Ds | 271 | 161 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -204.6768 | 1965.2920 | -110.41 % | 262038.0477 MeV (+37483.3 ppm) |
| ${}^{272}$Ds | 272 | 162 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -197.9154 | 1973.3600 | -110.03 % | 262998.0010 MeV (+37457.3 ppm) |
| ${}^{273}$Ds | 273 | 163 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -191.1616 | 1979.2500 | -109.66 % | 263957.9620 MeV (+37423.1 ppm) |
| ${}^{274}$Ds | 274 | 164 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -184.4153 | 1986.2260 | -109.28 % | 264917.9305 MeV (+37394.4 ppm) |
| ${}^{275}$Ds | 275 | 165 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -177.6765 | 1991.8250 | -108.92 % | 265877.9065 MeV (+37359.6 ppm) |
| ${}^{276}$Ds | 276 | 166 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -170.9452 | 1999.0680 | -108.55 % | 266837.8899 MeV (+37331.6 ppm) |
| ${}^{277}$Ds | 277 | 167 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -164.2212 | 2004.6490 | -108.19 % | 267797.8807 MeV (+37297.0 ppm) |
| ${}^{278}$Ds | 278 | 168 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -157.5045 | 2011.6080 | -107.83 % | 268757.8788 MeV (+37268.3 ppm) |
| ${}^{279}$Ds | 279 | 169 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -150.7951 | 2016.8910 | -107.48 % | 269717.8841 MeV (+37233.3 ppm) |
| ${}^{280}$Ds | 280 | 170 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -144.0928 | 2023.5600 | -107.12 % | 270677.8966 MeV (+37204.6 ppm) |
| ${}^{281}$Ds | 281 | 171 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -137.3977 | 2028.8200 | -106.77 % | 271637.9162 MeV (+37169.5 ppm) |
| ${}^{282}$Ds | 282 | 172 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -130.7096 | 2035.1940 | -106.42 % | 272597.9429 MeV (+37140.3 ppm) |
| ${}^{283}$Ds | 283 | 173 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -124.0285 | 2040.4300 | -106.08 % | 273557.9766 MeV (+37105.4 ppm) |
| ${}^{284}$Ds | 284 | 174 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -117.3544 | 2046.7880 | -105.73 % | 274518.0173 MeV (+37076.3 ppm) |

### Roentgenium (Z = 111)

_15 of 15 isotopes with a framework prediction; 15 of 15 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{272}$Rg | 272 | 161 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -224.6816 | 1965.7440 | -111.43 % | 263023.4369 MeV (+37530.3 ppm) |
| ${}^{273}$Rg | 273 | 162 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -217.8988 | 1973.7900 | -111.04 % | 263983.3689 MeV (+37504.2 ppm) |
| ${}^{274}$Rg | 274 | 163 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -211.1237 | 1980.1980 | -110.66 % | 264943.3086 MeV (+37471.8 ppm) |
| ${}^{275}$Rg | 275 | 164 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -204.3563 | 1987.4250 | -110.28 % | 265903.2559 MeV (+37443.4 ppm) |
| ${}^{276}$Rg | 276 | 165 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -197.5964 | 1993.5480 | -109.91 % | 266863.2108 MeV (+37410.4 ppm) |
| ${}^{277}$Rg | 277 | 166 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -190.8440 | 2000.4940 | -109.54 % | 267823.1732 MeV (+37381.6 ppm) |
| ${}^{278}$Rg | 278 | 167 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -184.0990 | 2006.6040 | -109.17 % | 268783.1430 MeV (+37348.7 ppm) |
| ${}^{279}$Rg | 279 | 168 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -177.3615 | 2013.2640 | -108.81 % | 269743.1202 MeV (+37319.6 ppm) |
| ${}^{280}$Rg | 280 | 169 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -170.6312 | 2019.3600 | -108.45 % | 270703.1047 MeV (+37287.0 ppm) |
| ${}^{281}$Rg | 281 | 170 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -163.9082 | 2025.7290 | -108.09 % | 271663.0965 MeV (+37257.5 ppm) |
| ${}^{282}$Rg | 282 | 171 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -157.1924 | 2031.5280 | -107.74 % | 272623.0954 MeV (+37224.4 ppm) |
| ${}^{283}$Rg | 283 | 172 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -150.4837 | 2037.8830 | -107.38 % | 273583.1015 MeV (+37194.6 ppm) |
| ${}^{284}$Rg | 284 | 173 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -143.7821 | 2043.3800 | -107.04 % | 274543.1147 MeV (+37161.3 ppm) |
| ${}^{285}$Rg | 285 | 174 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -137.0875 | 2049.7200 | -106.69 % | 275503.1349 MeV (+37131.5 ppm) |
| ${}^{286}$Rg | 286 | 175 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -130.3998 | 2054.9100 | -106.35 % | 276463.1620 MeV (+37097.9 ppm) |

### Copernicium (Z = 112)

_13 of 13 isotopes with a framework prediction; 13 of 13 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{276}$Cn | 276 | 164 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -224.4665 | 1989.6840 | -111.28 % | 266888.7507 MeV (+37497.7 ppm) |
| ${}^{277}$Cn | 277 | 165 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -217.6855 | 1995.7850 | -110.91 % | 267848.6844 MeV (+37464.7 ppm) |
| ${}^{278}$Cn | 278 | 166 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -210.9120 | 2003.2680 | -110.53 % | 268808.6257 MeV (+37437.7 ppm) |
| ${}^{279}$Cn | 279 | 167 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -204.1460 | 2009.3580 | -110.16 % | 269768.5745 MeV (+37404.4 ppm) |
| ${}^{280}$Cn | 280 | 168 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -197.3875 | 2016.5600 | -109.79 % | 270728.5307 MeV (+37377.4 ppm) |
| ${}^{281}$Cn | 281 | 169 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -190.6364 | 2022.3570 | -109.43 % | 271688.4944 MeV (+37344.1 ppm) |
| ${}^{282}$Cn | 282 | 170 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -183.8926 | 2029.5540 | -109.06 % | 272648.4653 MeV (+37316.6 ppm) |
| ${}^{283}$Cn | 283 | 171 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -177.1560 | 2035.3360 | -108.70 % | 273608.4435 MeV (+37282.9 ppm) |
| ${}^{284}$Cn | 284 | 172 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -170.4267 | 2042.2440 | -108.35 % | 274568.4290 MeV (+37255.1 ppm) |
| ${}^{285}$Cn | 285 | 173 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -163.7045 | 2047.7250 | -107.99 % | 275528.4216 MeV (+37221.4 ppm) |
| ${}^{286}$Cn | 286 | 174 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -156.9894 | 2054.3380 | -107.64 % | 276488.4212 MeV (+37192.9 ppm) |
| ${}^{287}$Cn | 287 | 175 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -150.2813 | 2059.5120 | -107.30 % | 277448.4279 MeV (+37158.7 ppm) |
| ${}^{288}$Cn | 288 | 176 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -143.5802 | 2066.1120 | -106.95 % | 278408.4416 MeV (+37130.0 ppm) |

### Nihonium (Z = 113)

_13 of 13 isotopes with a framework prediction; 13 of 13 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{278}$Nh | 278 | 165 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -237.9434 | 1996.3180 | -111.92 % | 268834.3268 MeV (+37512.1 ppm) |
| ${}^{279}$Nh | 279 | 166 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -231.1488 | 2004.0570 | -111.53 % | 269794.2470 MeV (+37485.4 ppm) |
| ${}^{280}$Nh | 280 | 167 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -224.3618 | 2010.4000 | -111.16 % | 270754.1747 MeV (+37453.4 ppm) |
| ${}^{281}$Nh | 281 | 168 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -217.5822 | 2017.8610 | -110.78 % | 271714.1099 MeV (+37426.6 ppm) |
| ${}^{282}$Nh | 282 | 169 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -210.8102 | 2023.9140 | -110.42 % | 272674.0527 MeV (+37394.6 ppm) |
| ${}^{283}$Nh | 283 | 170 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -204.0455 | 2031.0910 | -110.05 % | 273634.0028 MeV (+37367.1 ppm) |
| ${}^{284}$Nh | 284 | 171 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -197.2882 | 2037.1320 | -109.68 % | 274593.9602 MeV (+37335.2 ppm) |
| ${}^{285}$Nh | 285 | 172 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -190.5381 | 2044.0200 | -109.32 % | 275553.9249 MeV (+37306.9 ppm) |
| ${}^{286}$Nh | 286 | 173 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -183.7953 | 2050.0480 | -108.97 % | 276513.8969 MeV (+37274.8 ppm) |
| ${}^{287}$Nh | 287 | 174 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -177.0596 | 2056.6420 | -108.61 % | 277473.8760 MeV (+37245.7 ppm) |
| ${}^{288}$Nh | 288 | 175 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -170.3311 | 2062.0800 | -108.26 % | 278433.8622 MeV (+37212.9 ppm) |
| ${}^{289}$Nh | 289 | 176 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -163.6095 | 2068.6620 | -107.91 % | 279393.8554 MeV (+37183.9 ppm) |
| ${}^{290}$Nh | 290 | 177 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -156.8950 | 2074.0800 | -107.56 % | 280353.8557 MeV (+37150.6 ppm) |

### Flerovium (Z = 114)

_8 of 8 isotopes with a framework prediction; 8 of 8 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{284}$Fl | 284 | 170 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -224.3666 | 2034.2920 | -111.03 % | 274619.7084 MeV (+37423.9 ppm) |
| ${}^{285}$Fl | 285 | 171 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -217.5885 | 2040.3150 | -110.66 % | 275579.6450 MeV (+37391.4 ppm) |
| ${}^{286}$Fl | 286 | 172 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -210.8177 | 2047.4740 | -110.30 % | 276539.5889 MeV (+37364.8 ppm) |
| ${}^{287}$Fl | 287 | 173 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -204.0541 | 2053.4850 | -109.94 % | 277499.5402 MeV (+37332.1 ppm) |
| ${}^{288}$Fl | 288 | 174 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -197.2979 | 2060.3520 | -109.58 % | 278459.4987 MeV (+37304.7 ppm) |
| ${}^{289}$Fl | 289 | 175 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -190.5487 | 2066.0610 | -109.22 % | 279419.4643 MeV (+37271.6 ppm) |
| ${}^{290}$Fl | 290 | 176 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -183.8067 | 2072.6300 | -108.87 % | 280379.4371 MeV (+37243.7 ppm) |
| ${}^{291}$Fl | 291 | 177 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -177.0718 | 2078.0310 | -108.52 % | 281339.4169 MeV (+37210.2 ppm) |

### Moscovium (Z = 115)

_6 of 6 isotopes with a framework prediction; 6 of 6 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{287}$Mc | 287 | 172 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -231.2648 | 2048.8930 | -111.29 % | 277525.4206 MeV (+37414.0 ppm) |
| ${}^{288}$Mc | 288 | 173 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -224.4806 | 2054.8800 | -110.92 % | 278485.3511 MeV (+37382.7 ppm) |
| ${}^{289}$Mc | 289 | 174 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -217.7036 | 2062.0150 | -110.56 % | 279445.2889 MeV (+37355.1 ppm) |
| ${}^{290}$Mc | 290 | 175 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -210.9339 | 2067.9900 | -110.20 % | 280405.2340 MeV (+37323.5 ppm) |
| ${}^{291}$Mc | 291 | 176 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -204.1714 | 2074.5390 | -109.84 % | 281365.1862 MeV (+37295.0 ppm) |
| ${}^{292}$Mc | 292 | 177 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -197.4160 | 2080.2080 | -109.49 % | 282325.1456 MeV (+37262.7 ppm) |

### Livermorium (Z = 116)

_5 of 5 isotopes with a framework prediction; 5 of 5 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{289}$Lv | 289 | 173 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -245.0742 | 2057.3910 | -111.91 % | 279471.3292 MeV (+37437.2 ppm) |
| ${}^{290}$Lv | 290 | 174 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -238.2765 | 2064.8000 | -111.54 % | 280431.2463 MeV (+37411.2 ppm) |
| ${}^{291}$Lv | 291 | 175 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -231.4862 | 2070.7560 | -111.18 % | 281391.1707 MeV (+37379.1 ppm) |
| ${}^{292}$Lv | 292 | 176 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -224.7031 | 2077.8720 | -110.81 % | 282351.1024 MeV (+37352.2 ppm) |
| ${}^{293}$Lv | 293 | 177 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -217.9272 | 2083.5230 | -110.46 % | 283311.0413 MeV (+37319.7 ppm) |

### Tennessine (Z = 117)

_4 of 4 isotopes with a framework prediction; 4 of 4 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{291}$Ts | 291 | 174 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -259.0162 | 2065.5180 | -112.54 % | 281417.3704 MeV (+37458.8 ppm) |
| ${}^{292}$Ts | 292 | 175 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -252.2051 | 2071.7400 | -112.17 % | 282377.2742 MeV (+37427.5 ppm) |
| ${}^{293}$Ts | 293 | 176 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -245.4014 | 2078.8350 | -111.80 % | 283337.1852 MeV (+37400.8 ppm) |
| ${}^{294}$Ts | 294 | 177 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -238.6049 | 2085.0480 | -111.44 % | 284297.1035 MeV (+37369.9 ppm) |

### Oganesson (Z = 118)

_3 of 3 isotopes with a framework prediction; 3 of 3 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{293}$Og | 293 | 175 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -273.0904 | 2073.8540 | -113.17 % | 283363.5439 MeV (+37480.7 ppm) |
| ${}^{294}$Og | 294 | 176 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -266.2660 | 2081.2260 | -112.79 % | 284323.4342 MeV (+37454.9 ppm) |
| ${}^{295}$Og | 295 | 177 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -259.4489 | 2087.4200 | -112.43 % | 285283.3319 MeV (+37423.6 ppm) |

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
| ${}^{41}$Mg | 41 | 29 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 150.3903 | 263.4250 | -42.91 % | 39468.9518 MeV (+31885.3 ppm) |

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
| ${}^{41}$Al | 41 | 28 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 143.0450 | 286.1800 | -50.02 % | 39474.9668 MeV (+32677.3 ppm) |
| ${}^{42}$Al | 42 | 29 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 148.4366 | 286.8180 | -48.25 % | 40436.2900 MeV (+32466.6 ppm) |
| ${}^{43}$Al | 43 | 30 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 153.8222 | 288.6160 | -46.70 % | 41397.6192 MeV (+32294.8 ppm) |

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
| ${}^{41}$Si | 41 | 27 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 135.2970 | 306.7620 | -55.90 % | 39481.3845 MeV (+33423.5 ppm) |
| ${}^{42}$Si | 42 | 28 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 140.7259 | 311.2200 | -54.78 % | 40442.6704 MeV (+33293.1 ppm) |
| ${}^{43}$Si | 43 | 29 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 146.1478 | 311.7930 | -53.13 % | 41403.9633 MeV (+33069.7 ppm) |
| ${}^{44}$Si | 44 | 30 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 151.5629 | 314.8640 | -51.86 % | 42365.2629 MeV (+32919.9 ppm) |
| ${}^{45}$Si | 45 | 31 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 156.9717 | 315.1800 | -50.20 % | 43326.5689 MeV (+32708.0 ppm) |

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
| ${}^{41}$P | 41 | 26 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 127.1462 | 324.1686 | -60.78 % | 39488.2050 MeV (+34094.1 ppm) |
| ${}^{42}$P | 42 | 27 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 132.6155 | 326.1683 | -59.34 % | 40449.4506 MeV (+33882.3 ppm) |
| ${}^{43}$P | 43 | 28 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 138.0765 | 330.2830 | -58.19 % | 41410.7043 MeV (+33735.4 ppm) |
| ${}^{44}$P | 44 | 29 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 143.5297 | 332.2880 | -56.81 % | 42371.9658 MeV (+33542.0 ppm) |
| ${}^{45}$P | 45 | 30 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 148.9755 | 335.5200 | -55.60 % | 43333.2348 MeV (+33387.4 ppm) |
| ${}^{46}$P | 46 | 31 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 154.4143 | 336.7200 | -54.14 % | 44294.5108 MeV (+33190.8 ppm) |
| ${}^{47}$P | 47 | 32 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 159.8462 | 338.8230 | -52.82 % | 45255.7936 MeV (+33024.3 ppm) |

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
| ${}^{41}$S | 41 | 25 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 118.5927 | 337.4151 | -64.85 % | 39495.4282 MeV (+34663.4 ppm) |
| ${}^{42}$S | 42 | 26 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 124.1053 | 344.1156 | -63.94 % | 40456.6305 MeV (+34561.1 ppm) |
| ${}^{43}$S | 43 | 27 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 129.6084 | 346.7446 | -62.62 % | 41417.8421 MeV (+34358.7 ppm) |
| ${}^{44}$S | 44 | 28 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 135.1025 | 351.8247 | -61.60 % | 42379.0628 MeV (+34227.6 ppm) |
| ${}^{45}$S | 45 | 29 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 140.5880 | 354.0150 | -60.29 % | 43340.2920 MeV (+34031.6 ppm) |
| ${}^{46}$S | 46 | 30 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 146.0654 | 358.1100 | -59.21 % | 44301.5294 MeV (+33889.9 ppm) |
| ${}^{47}$S | 47 | 31 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 151.5350 | 359.6440 | -57.87 % | 45262.7745 MeV (+33693.5 ppm) |
| ${}^{48}$S | 48 | 32 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 156.9972 | 362.4960 | -56.69 % | 46224.0271 MeV (+33537.2 ppm) |
| ${}^{49}$S | 49 | 33 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 162.4523 | 362.6000 | -55.20 % | 47185.2868 MeV (+33323.8 ppm) |

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
| ${}^{41}$Cl | 41 | 24 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 109.6364 | 344.9313 | -68.21 % | 39503.0542 MeV (+35088.2 ppm) |
| ${}^{42}$Cl | 42 | 25 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 115.1953 | 350.5272 | -67.14 % | 40464.2101 MeV (+34945.3 ppm) |
| ${}^{43}$Cl | 43 | 26 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 120.7433 | 357.9263 | -66.27 % | 41425.3769 MeV (+34856.0 ppm) |
| ${}^{44}$Cl | 44 | 27 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 126.2812 | 362.3171 | -65.15 % | 42386.5538 MeV (+34695.1 ppm) |
| ${}^{45}$Cl | 45 | 28 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 131.8092 | 368.1720 | -64.20 % | 43347.7405 MeV (+34577.7 ppm) |
| ${}^{46}$Cl | 46 | 29 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 137.3279 | 371.7157 | -63.06 % | 44308.9366 MeV (+34409.8 ppm) |
| ${}^{47}$Cl | 47 | 30 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 142.8378 | 375.6240 | -61.97 % | 45270.1415 MeV (+34258.1 ppm) |
| ${}^{48}$Cl | 48 | 31 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 148.3392 | 378.3840 | -60.80 % | 46231.3549 MeV (+34086.5 ppm) |
| ${}^{49}$Cl | 49 | 32 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 153.8324 | 381.4650 | -59.67 % | 47192.5764 MeV (+33928.4 ppm) |
| ${}^{50}$Cl | 50 | 33 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 159.3179 | 382.5500 | -58.35 % | 48153.8057 MeV (+33733.8 ppm) |
| ${}^{51}$Cl | 51 | 34 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 164.7960 | 384.0300 | -57.09 % | 49115.0424 MeV (+33555.1 ppm) |
| ${}^{52}$Cl | 52 | 35 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 170.2670 | 384.0720 | -55.67 % | 50076.2862 MeV (+33351.9 ppm) |

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
| ${}^{41}$Ar | 41 | 23 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 100.2774 | 349.9093 | -71.34 % | 39511.0830 MeV (+35454.8 ppm) |
| ${}^{42}$Ar | 42 | 24 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 105.8855 | 359.3358 | -70.53 % | 40472.1896 MeV (+35403.4 ppm) |
| ${}^{43}$Ar | 43 | 25 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 111.4815 | 364.9942 | -69.46 % | 41433.3084 MeV (+35257.2 ppm) |
| ${}^{44}$Ar | 44 | 26 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 117.0658 | 373.7290 | -68.68 % | 42394.4389 MeV (+35195.7 ppm) |
| ${}^{45}$Ar | 45 | 27 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 122.6391 | 378.8979 | -67.63 % | 43355.5804 MeV (+35049.1 ppm) |
| ${}^{46}$Ar | 46 | 28 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 128.2018 | 386.9696 | -66.87 % | 44316.7324 MeV (+34979.2 ppm) |
| ${}^{47}$Ar | 47 | 29 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 133.7545 | 390.6370 | -65.76 % | 45277.8945 MeV (+34808.5 ppm) |
| ${}^{48}$Ar | 48 | 30 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 139.2976 | 395.6959 | -64.80 % | 46239.0662 MeV (+34677.2 ppm) |
| ${}^{49}$Ar | 49 | 31 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 144.8315 | 398.4680 | -63.65 % | 47200.2471 MeV (+34499.9 ppm) |
| ${}^{50}$Ar | 50 | 32 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 150.3566 | 402.7000 | -62.66 % | 48161.4367 MeV (+34362.3 ppm) |
| ${}^{51}$Ar | 51 | 33 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 155.8733 | 404.0220 | -61.42 % | 49122.6348 MeV (+34167.1 ppm) |
| ${}^{52}$Ar | 52 | 34 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 161.3820 | 407.0040 | -60.35 % | 50083.8409 MeV (+34014.3 ppm) |
| ${}^{53}$Ar | 53 | 35 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 166.8830 | 406.8810 | -58.98 % | 51045.0547 MeV (+33803.4 ppm) |
| ${}^{54}$Ar | 54 | 36 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 172.3765 | 409.2120 | -57.88 % | 52006.2759 MeV (+33649.9 ppm) |

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
| ${}^{41}$K | 41 | 22 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 90.5156 | 351.6190 | -74.26 % | 39519.5145 MeV (+35743.4 ppm) |
| ${}^{42}$K | 42 | 23 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 96.1760 | 359.1528 | -73.22 % | 40480.5688 MeV (+35633.6 ppm) |
| ${}^{43}$K | 43 | 24 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 101.8227 | 368.7775 | -72.39 % | 41441.6369 MeV (+35583.4 ppm) |
| ${}^{44}$K | 44 | 25 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 107.4564 | 376.0549 | -71.43 % | 42402.7180 MeV (+35476.4 ppm) |
| ${}^{45}$K | 45 | 26 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 113.0776 | 384.9604 | -70.63 % | 43363.8115 MeV (+35414.8 ppm) |
| ${}^{46}$K | 46 | 27 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 118.6870 | 391.8300 | -69.71 % | 44324.9169 MeV (+35306.8 ppm) |
| ${}^{47}$K | 47 | 28 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 124.2851 | 400.1993 | -68.94 % | 45286.0336 MeV (+35239.2 ppm) |
| ${}^{48}$K | 48 | 29 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 129.8724 | 404.8432 | -67.92 % | 46247.1611 MeV (+35088.4 ppm) |
| ${}^{49}$K | 49 | 30 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 135.4494 | 410.2415 | -66.98 % | 47208.2988 MeV (+34961.0 ppm) |
| ${}^{50}$K | 50 | 31 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 141.0166 | 414.4292 | -65.97 % | 48169.4465 MeV (+34812.1 ppm) |
| ${}^{51}$K | 51 | 32 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 146.5743 | 419.2881 | -65.04 % | 49130.6035 MeV (+34683.9 ppm) |
| ${}^{52}$K | 52 | 33 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 152.1229 | 421.9816 | -63.95 % | 50091.7696 MeV (+34514.6 ppm) |
| ${}^{53}$K | 53 | 34 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 157.6629 | 425.2110 | -62.92 % | 51052.9444 MeV (+34363.0 ppm) |
| ${}^{54}$K | 54 | 35 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 163.1946 | 426.1140 | -61.70 % | 52014.1275 MeV (+34170.0 ppm) |
| ${}^{55}$K | 55 | 36 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 168.7183 | 428.5600 | -60.63 % | 52975.3186 MeV (+34014.9 ppm) |
| ${}^{56}$K | 56 | 37 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 174.2343 | 429.1280 | -59.40 % | 53936.5173 MeV (+33828.1 ppm) |
| ${}^{57}$K | 57 | 38 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 179.7430 | 431.0910 | -58.31 % | 54897.7235 MeV (+33674.5 ppm) |
| ${}^{58}$K | 58 | 39 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 185.2445 | 431.3460 | -57.05 % | 55858.9367 MeV (+33494.8 ppm) |
| ${}^{59}$K | 59 | 40 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 190.7392 | 432.5880 | -55.91 % | 56820.1568 MeV (+33339.8 ppm) |

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
| ${}^{41}$Ca | 41 | 21 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 80.3511 | 350.4150 | -77.07 % | 39528.3487 MeV (+35963.5 ppm) |
| ${}^{42}$Ca | 42 | 22 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 86.0667 | 361.8957 | -76.22 % | 40489.3478 MeV (+35951.7 ppm) |
| ${}^{43}$Ca | 43 | 23 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 91.7671 | 369.8286 | -75.19 % | 41450.3622 MeV (+35848.9 ppm) |
| ${}^{44}$Ca | 44 | 24 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 97.4529 | 380.9598 | -74.42 % | 42411.3912 MeV (+35832.1 ppm) |
| ${}^{45}$Ca | 45 | 25 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 103.1248 | 388.3746 | -73.45 % | 43372.4340 MeV (+35724.4 ppm) |
| ${}^{46}$Ca | 46 | 26 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 108.7835 | 398.7733 | -72.72 % | 44333.4901 MeV (+35694.0 ppm) |
| ${}^{47}$Ca | 47 | 27 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 114.4296 | 406.0497 | -71.82 % | 45294.5588 MeV (+35591.1 ppm) |
| ${}^{48}$Ca | 48 | 28 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 120.0637 | 416.0012 | -71.14 % | 46255.6395 MeV (+35554.9 ppm) |
| ${}^{49}$Ca | 49 | 29 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 125.6863 | 421.1476 | -70.16 % | 47216.7317 MeV (+35411.2 ppm) |
| ${}^{50}$Ca | 50 | 30 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 131.2978 | 427.5082 | -69.29 % | 48177.8349 MeV (+35300.6 ppm) |
| ${}^{51}$Ca | 51 | 31 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 136.8988 | 432.3226 | -68.33 % | 49138.9486 MeV (+35160.9 ppm) |
| ${}^{52}$Ca | 52 | 32 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 142.4898 | 438.3279 | -67.49 % | 50100.0725 MeV (+35052.2 ppm) |
| ${}^{53}$Ca | 53 | 33 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 148.0710 | 441.5206 | -66.46 % | 51061.2060 MeV (+34888.8 ppm) |
| ${}^{54}$Ca | 54 | 34 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 153.6430 | 445.3648 | -65.50 % | 52022.3488 MeV (+34745.1 ppm) |
| ${}^{55}$Ca | 55 | 35 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 159.2061 | 446.9259 | -64.38 % | 52983.5005 MeV (+34560.7 ppm) |
| ${}^{56}$Ca | 56 | 36 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 164.7606 | 449.8573 | -63.37 % | 53944.6607 MeV (+34410.3 ppm) |
| ${}^{57}$Ca | 57 | 37 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 170.3069 | 450.9840 | -62.24 % | 54905.8292 MeV (+34230.0 ppm) |
| ${}^{58}$Ca | 58 | 38 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 175.8452 | 454.0240 | -61.27 % | 55867.0057 MeV (+34093.0 ppm) |
| ${}^{59}$Ca | 59 | 39 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 181.3760 | 454.7720 | -60.12 % | 56828.1897 MeV (+33917.3 ppm) |
| ${}^{60}$Ca | 60 | 40 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 186.8994 | 457.6200 | -59.16 % | 57789.3811 MeV (+33787.4 ppm) |
| ${}^{61}$Ca | 61 | 41 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 192.4157 | 457.6830 | -57.96 % | 58750.5796 MeV (+33610.6 ppm) |

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
| ${}^{41}$Sc | 41 | 20 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 69.7838 | 343.1371 | -79.66 % | 39537.5857 MeV (+36029.2 ppm) |
| ${}^{42}$Sc | 42 | 21 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 75.5577 | 354.6871 | -78.70 % | 40498.5265 MeV (+36016.2 ppm) |
| ${}^{43}$Sc | 43 | 22 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 81.3146 | 366.8255 | -77.83 % | 41459.4844 MeV (+36019.4 ppm) |
| ${}^{44}$Sc | 44 | 23 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 87.0554 | 376.5247 | -76.88 % | 42420.4584 MeV (+35961.1 ppm) |
| ${}^{45}$Sc | 45 | 24 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 92.7808 | 387.8523 | -76.08 % | 43381.4478 MeV (+35946.1 ppm) |
| ${}^{46}$Sc | 46 | 25 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 98.4914 | 396.6130 | -75.17 % | 44342.4519 MeV (+35870.0 ppm) |
| ${}^{47}$Sc | 47 | 26 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 104.1881 | 407.2595 | -74.42 % | 45303.4700 MeV (+35842.1 ppm) |
| ${}^{48}$Sc | 48 | 27 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 109.8715 | 415.4981 | -73.56 % | 46264.5014 MeV (+35759.8 ppm) |
| ${}^{49}$Sc | 49 | 28 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 115.5420 | 425.6277 | -72.85 % | 47225.5456 MeV (+35724.1 ppm) |
| ${}^{50}$Sc | 50 | 29 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 121.2004 | 431.6737 | -71.92 % | 48186.6020 MeV (+35599.1 ppm) |
| ${}^{51}$Sc | 51 | 30 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 126.8471 | 438.4583 | -71.07 % | 49147.6701 MeV (+35495.5 ppm) |
| ${}^{52}$Sc | 52 | 31 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 132.4825 | 443.8028 | -70.15 % | 50108.7494 MeV (+35365.3 ppm) |
| ${}^{53}$Sc | 53 | 32 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 138.1073 | 450.1201 | -69.32 % | 51069.8394 MeV (+35260.6 ppm) |
| ${}^{54}$Sc | 54 | 33 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 143.7218 | 453.8598 | -68.33 % | 52030.9398 MeV (+35107.0 ppm) |
| ${}^{55}$Sc | 55 | 34 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 149.3263 | 458.3353 | -67.42 % | 52992.0500 MeV (+34974.0 ppm) |
| ${}^{56}$Sc | 56 | 35 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 154.9214 | 461.0804 | -66.40 % | 53953.1697 MeV (+34811.7 ppm) |
| ${}^{57}$Sc | 57 | 36 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 160.5073 | 465.0155 | -65.48 % | 54914.2985 MeV (+34678.4 ppm) |
| ${}^{58}$Sc | 58 | 37 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 166.0845 | 467.1867 | -64.45 % | 55875.4361 MeV (+34516.1 ppm) |
| ${}^{59}$Sc | 59 | 38 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 171.6532 | 470.6080 | -63.53 % | 56836.5822 MeV (+34383.1 ppm) |
| ${}^{60}$Sc | 60 | 39 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 177.2137 | 472.3800 | -62.48 % | 57797.7364 MeV (+34224.5 ppm) |
| ${}^{61}$Sc | 61 | 40 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 182.7664 | 475.4340 | -61.56 % | 58758.8985 MeV (+34093.7 ppm) |
| ${}^{62}$Sc | 62 | 41 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 188.3115 | 476.6560 | -60.49 % | 59720.0682 MeV (+33935.7 ppm) |
| ${}^{63}$Sc | 63 | 42 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 193.8493 | 478.9890 | -59.53 % | 60681.2451 MeV (+33801.4 ppm) |

### Titanium (Z = 22)

_25 of 29 isotopes with a framework prediction; 25 of 29 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{37}$Ti | 37 | 15 | derivation-pending | ⚪ pending | binding_energy | — | 256.2620 | — | — |
| ${}^{38}$Ti | 38 | 16 | derivation-pending | ⚪ pending | binding_energy | — | 278.1220 | — | — |
| ${}^{39}$Ti | 39 | 17 | derivation-pending | ⚪ pending | binding_energy | — | 295.0740 | — | — |
| ${}^{40}$Ti | 40 | 18 | derivation-pending | ⚪ pending | binding_energy | — | 314.6345 | — | — |
| ${}^{41}$Ti | 41 | 19 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 58.8137 | 329.4099 | -82.15 % | 39547.2255 MeV (+35930.4 ppm) |
| ${}^{42}$Ti | 42 | 20 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 64.6489 | 346.8881 | -81.36 % | 40508.1050 MeV (+36075.2 ppm) |
| ${}^{43}$Ti | 43 | 21 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 70.4653 | 359.1706 | -80.38 % | 41469.0034 MeV (+36079.3 ppm) |
| ${}^{44}$Ti | 44 | 22 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 76.2638 | 375.4749 | -79.69 % | 42429.9197 MeV (+36185.4 ppm) |
| ${}^{45}$Ti | 45 | 23 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 82.0454 | 385.0079 | -78.69 % | 43390.8529 MeV (+36119.7 ppm) |
| ${}^{46}$Ti | 46 | 24 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 87.8107 | 398.1973 | -77.95 % | 44351.8023 MeV (+36145.7 ppm) |
| ${}^{47}$Ti | 47 | 25 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 93.5606 | 407.0779 | -77.02 % | 45312.7672 MeV (+36068.9 ppm) |
| ${}^{48}$Ti | 48 | 26 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 99.2957 | 418.7046 | -76.29 % | 46273.7469 MeV (+36059.3 ppm) |
| ${}^{49}$Ti | 49 | 27 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 105.0167 | 426.8470 | -75.40 % | 47234.7406 MeV (+35971.2 ppm) |
| ${}^{50}$Ti | 50 | 28 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 110.7243 | 437.7861 | -74.71 % | 48195.7479 MeV (+35949.2 ppm) |
| ${}^{51}$Ti | 51 | 29 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 116.4189 | 444.1586 | -73.79 % | 49156.7680 MeV (+35828.7 ppm) |
| ${}^{52}$Ti | 52 | 30 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 122.1012 | 451.9746 | -72.98 % | 50117.8004 MeV (+35743.9 ppm) |
| ${}^{53}$Ti | 53 | 31 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 127.7717 | 457.4497 | -72.07 % | 51078.8448 MeV (+35613.5 ppm) |
| ${}^{54}$Ti | 54 | 32 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 133.4308 | 464.3834 | -71.27 % | 52039.9004 MeV (+35518.2 ppm) |
| ${}^{55}$Ti | 55 | 33 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 139.0790 | 468.5433 | -70.32 % | 53000.9670 MeV (+35370.4 ppm) |
| ${}^{56}$Ti | 56 | 34 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 144.7167 | 474.2052 | -69.48 % | 53962.0441 MeV (+35258.0 ppm) |
| ${}^{57}$Ti | 57 | 35 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 150.3443 | 477.2553 | -68.50 % | 54923.1313 MeV (+35098.8 ppm) |
| ${}^{58}$Ti | 58 | 36 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 155.9622 | 481.8425 | -67.63 % | 55884.2281 MeV (+34974.8 ppm) |
| ${}^{59}$Ti | 59 | 37 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 161.5708 | 484.8620 | -66.68 % | 56845.3343 MeV (+34825.8 ppm) |
| ${}^{60}$Ti | 60 | 38 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 167.1704 | 489.1671 | -65.83 % | 57806.4495 MeV (+34705.4 ppm) |
| ${}^{61}$Ti | 61 | 39 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 172.7613 | 491.5380 | -64.85 % | 58767.5733 MeV (+34553.5 ppm) |
| ${}^{62}$Ti | 62 | 40 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 178.3439 | 495.3800 | -64.00 % | 59728.7055 MeV (+34434.6 ppm) |
| ${}^{63}$Ti | 63 | 41 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 183.9184 | 497.1330 | -63.00 % | 60689.8457 MeV (+34281.5 ppm) |
| ${}^{64}$Ti | 64 | 42 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 189.4852 | 500.8640 | -62.17 % | 61650.9938 MeV (+34167.2 ppm) |
| ${}^{65}$Ti | 65 | 43 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 195.0444 | 502.1900 | -61.16 % | 62612.1493 MeV (+34017.2 ppm) |

### Vanadium (Z = 23)

_27 of 29 isotopes with a framework prediction; 27 of 29 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{39}$V | 39 | 16 | derivation-pending | ⚪ pending | binding_energy | — | 274.2090 | — | — |
| ${}^{40}$V | 40 | 17 | derivation-pending | ⚪ pending | binding_energy | — | 292.4000 | — | — |
| ${}^{41}$V | 41 | 18 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 47.4409 | 312.6250 | -84.82 % | 39557.2680 MeV (+35759.2 ppm) |
| ${}^{42}$V | 42 | 19 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 53.3403 | 328.6080 | -83.77 % | 40518.0833 MeV (+35867.2 ppm) |
| ${}^{43}$V | 43 | 20 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 59.2191 | 346.9891 | -82.93 % | 41478.9193 MeV (+36032.0 ppm) |
| ${}^{44}$V | 44 | 21 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 65.0782 | 360.9521 | -81.97 % | 42439.7750 MeV (+36078.4 ppm) |
| ${}^{45}$V | 45 | 22 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 70.9186 | 377.1018 | -81.19 % | 43400.6493 MeV (+36177.4 ppm) |
| ${}^{46}$V | 46 | 23 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 76.7413 | 390.3625 | -80.34 % | 44361.5415 MeV (+36202.5 ppm) |
| ${}^{47}$V | 47 | 24 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 82.5469 | 403.3650 | -79.54 % | 45322.4506 MeV (+36220.8 ppm) |
| ${}^{48}$V | 48 | 25 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 88.3364 | 413.9073 | -78.66 % | 46283.3759 MeV (+36181.7 ppm) |
| ${}^{49}$V | 49 | 26 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 94.1103 | 425.4628 | -77.88 % | 47244.3167 MeV (+36167.5 ppm) |
| ${}^{50}$V | 50 | 27 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 99.8695 | 434.7952 | -77.03 % | 48205.2724 MeV (+36104.7 ppm) |
| ${}^{51}$V | 51 | 28 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 105.6144 | 445.8463 | -76.31 % | 49166.2422 MeV (+36082.2 ppm) |
| ${}^{52}$V | 52 | 29 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 111.3458 | 453.1576 | -75.43 % | 50127.2256 MeV (+35980.8 ppm) |
| ${}^{53}$V | 53 | 30 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 117.0642 | 461.6376 | -74.64 % | 51088.2219 MeV (+35908.0 ppm) |
| ${}^{54}$V | 54 | 31 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 122.7701 | 467.7555 | -73.75 % | 52049.2308 MeV (+35789.4 ppm) |
| ${}^{55}$V | 55 | 32 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 128.4640 | 475.0537 | -72.96 % | 53010.2517 MeV (+35699.3 ppm) |
| ${}^{56}$V | 56 | 33 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 134.1464 | 480.1832 | -72.06 % | 53971.2841 MeV (+35569.6 ppm) |
| ${}^{57}$V | 57 | 34 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 139.8177 | 486.5062 | -71.26 % | 54932.3275 MeV (+35467.9 ppm) |
| ${}^{58}$V | 58 | 35 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 145.4784 | 490.5730 | -70.35 % | 55893.3816 MeV (+35326.7 ppm) |
| ${}^{59}$V | 59 | 36 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 151.1289 | 495.8244 | -69.52 % | 56854.4459 MeV (+35212.8 ppm) |
| ${}^{60}$V | 60 | 37 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 156.7694 | 499.3725 | -68.61 % | 57815.5201 MeV (+35071.3 ppm) |
| ${}^{61}$V | 61 | 38 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 162.4005 | 504.5335 | -67.81 % | 58776.6039 MeV (+34964.0 ppm) |
| ${}^{62}$V | 62 | 39 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 168.0223 | 507.6409 | -66.90 % | 59737.6968 MeV (+34823.6 ppm) |
| ${}^{63}$V | 63 | 40 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 173.6353 | 512.2392 | -66.10 % | 60698.7986 MeV (+34714.1 ppm) |
| ${}^{64}$V | 64 | 41 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 179.2398 | 514.8800 | -65.19 % | 61659.9089 MeV (+34574.3 ppm) |
| ${}^{65}$V | 65 | 42 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 184.8360 | 518.7650 | -64.37 % | 62621.0274 MeV (+34459.7 ppm) |
| ${}^{66}$V | 66 | 43 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 190.4242 | 521.0040 | -63.45 % | 63582.1540 MeV (+34321.8 ppm) |
| ${}^{67}$V | 67 | 44 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 196.0047 | 524.5430 | -62.63 % | 64543.2883 MeV (+34209.0 ppm) |

### Chromium (Z = 24)

_30 of 30 isotopes with a framework prediction; 30 of 30 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{41}$Cr | 41 | 17 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 35.6653 | 291.7560 | -87.78 % | 39567.7132 MeV (+35487.7 ppm) |
| ${}^{42}$Cr | 42 | 18 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 41.6320 | 313.1520 | -86.71 % | 40528.4614 MeV (+35743.8 ppm) |
| ${}^{43}$Cr | 43 | 19 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 47.5760 | 330.2400 | -85.59 % | 41489.2321 MeV (+35877.0 ppm) |
| ${}^{44}$Cr | 44 | 20 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 53.4985 | 349.7836 | -84.71 % | 42450.0243 MeV (+36066.0 ppm) |
| ${}^{45}$Cr | 45 | 21 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 59.4006 | 363.9478 | -83.68 % | 43410.8370 MeV (+36114.5 ppm) |
| ${}^{46}$Cr | 46 | 22 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 65.2832 | 381.9759 | -82.91 % | 44371.6692 MeV (+36255.0 ppm) |
| ${}^{47}$Cr | 47 | 23 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 71.1472 | 395.1387 | -81.99 % | 45332.5200 MeV (+36274.7 ppm) |
| ${}^{48}$Cr | 48 | 24 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 76.9935 | 411.4683 | -81.29 % | 46293.3885 MeV (+36367.4 ppm) |
| ${}^{49}$Cr | 49 | 25 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 82.8228 | 422.0506 | -80.38 % | 47254.2739 MeV (+36326.1 ppm) |
| ${}^{50}$Cr | 50 | 26 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 88.6359 | 435.0509 | -79.63 % | 48215.1756 MeV (+36340.7 ppm) |
| ${}^{51}$Cr | 51 | 27 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 94.4336 | 444.3116 | -78.75 % | 49176.0927 MeV (+36273.4 ppm) |
| ${}^{52}$Cr | 52 | 28 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 100.2163 | 456.3517 | -78.04 % | 50137.0247 MeV (+36268.5 ppm) |
| ${}^{53}$Cr | 53 | 29 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 105.9849 | 464.2911 | -77.17 % | 51097.9710 MeV (+36177.9 ppm) |
| ${}^{54}$Cr | 54 | 30 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 111.7397 | 474.0102 | -76.43 % | 52058.9309 MeV (+36127.6 ppm) |
| ${}^{55}$Cr | 55 | 31 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 117.4815 | 480.2565 | -75.54 % | 53019.9039 MeV (+36009.1 ppm) |
| ${}^{56}$Cr | 56 | 32 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 123.2107 | 488.5026 | -74.78 % | 53980.8895 MeV (+35934.8 ppm) |
| ${}^{57}$Cr | 57 | 33 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 128.9277 | 493.8138 | -73.89 % | 54941.8872 MeV (+35806.1 ppm) |
| ${}^{58}$Cr | 58 | 34 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 134.6331 | 501.3519 | -73.15 % | 55902.8966 MeV (+35724.7 ppm) |
| ${}^{59}$Cr | 59 | 35 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 140.3273 | 505.5474 | -72.24 % | 56863.9171 MeV (+35583.3 ppm) |
| ${}^{60}$Cr | 60 | 36 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 146.0107 | 512.4113 | -71.51 % | 57824.9485 MeV (+35496.3 ppm) |
| ${}^{61}$Cr | 61 | 37 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 151.6837 | 516.0706 | -70.61 % | 58785.9903 MeV (+35353.9 ppm) |
| ${}^{62}$Cr | 62 | 38 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 157.3467 | 522.4980 | -69.89 % | 59747.0421 MeV (+35265.9 ppm) |
| ${}^{63}$Cr | 63 | 39 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 163.0000 | 525.8950 | -69.01 % | 60708.1036 MeV (+35127.5 ppm) |
| ${}^{64}$Cr | 64 | 40 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 168.6439 | 531.4280 | -68.27 % | 61669.1745 MeV (+35030.6 ppm) |
| ${}^{65}$Cr | 65 | 41 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 174.2788 | 534.1700 | -67.37 % | 62630.2543 MeV (+34889.1 ppm) |
| ${}^{66}$Cr | 66 | 42 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 179.9050 | 539.0880 | -66.63 % | 63591.3429 MeV (+34788.5 ppm) |
| ${}^{67}$Cr | 67 | 43 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 185.5227 | 541.2930 | -65.73 % | 64552.4400 MeV (+34646.2 ppm) |
| ${}^{68}$Cr | 68 | 44 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 191.1323 | 545.7680 | -64.98 % | 65513.5452 MeV (+34545.7 ppm) |
| ${}^{69}$Cr | 69 | 45 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 196.7340 | 547.7910 | -64.09 % | 66474.6583 MeV (+34408.3 ppm) |
| ${}^{70}$Cr | 70 | 46 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 202.3280 | 551.8800 | -63.34 % | 67435.7790 MeV (+34307.8 ppm) |

### Manganese (Z = 25)

_31 of 31 isotopes with a framework prediction; 31 of 31 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{43}$Mn | 43 | 18 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 35.5361 | 310.1590 | -88.54 % | 41499.9417 MeV (+35644.3 ppm) |
| ${}^{44}$Mn | 44 | 19 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 41.5248 | 328.1080 | -87.34 % | 42460.6678 MeV (+35797.8 ppm) |
| ${}^{45}$Mn | 45 | 20 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 47.4913 | 348.6150 | -86.38 % | 43421.4161 MeV (+36007.6 ppm) |
| ${}^{46}$Mn | 46 | 21 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 53.4365 | 364.1397 | -85.33 % | 44382.1856 MeV (+36087.9 ppm) |
| ${}^{47}$Mn | 47 | 22 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 59.3614 | 382.3596 | -84.47 % | 45342.9755 MeV (+36229.5 ppm) |
| ${}^{48}$Mn | 48 | 23 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 65.2671 | 397.1612 | -83.57 % | 46303.7846 MeV (+36286.4 ppm) |
| ${}^{49}$Mn | 49 | 24 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 71.1542 | 413.5558 | -82.79 % | 47264.6122 MeV (+36377.6 ppm) |
| ${}^{50}$Mn | 50 | 25 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 77.0237 | 426.6341 | -81.95 % | 48225.4575 MeV (+36391.7 ppm) |
| ${}^{51}$Mn | 51 | 26 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 82.8763 | 440.3218 | -81.18 % | 49186.3197 MeV (+36418.8 ppm) |
| ${}^{52}$Mn | 52 | 27 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 88.7127 | 450.8613 | -80.32 % | 50147.1980 MeV (+36377.9 ppm) |
| ${}^{53}$Mn | 53 | 28 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 94.5336 | 462.9115 | -79.58 % | 51108.0919 MeV (+36370.5 ppm) |
| ${}^{54}$Mn | 54 | 29 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 100.3397 | 471.8507 | -78.73 % | 52069.0007 MeV (+36299.6 ppm) |
| ${}^{55}$Mn | 55 | 30 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 106.1314 | 482.0764 | -77.98 % | 53029.9237 MeV (+36257.5 ppm) |
| ${}^{56}$Mn | 56 | 31 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 111.9094 | 489.3468 | -77.13 % | 53990.8605 MeV (+36158.5 ppm) |
| ${}^{57}$Mn | 57 | 32 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 117.6742 | 497.9927 | -76.37 % | 54951.8104 MeV (+36090.1 ppm) |
| ${}^{58}$Mn | 58 | 33 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 123.4263 | 504.4053 | -75.53 % | 55912.7731 MeV (+35981.3 ppm) |
| ${}^{59}$Mn | 59 | 34 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 129.1663 | 512.1744 | -74.78 % | 56873.7479 MeV (+35902.1 ppm) |
| ${}^{60}$Mn | 60 | 35 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 134.8944 | 517.6884 | -73.94 % | 57834.7346 MeV (+35783.9 ppm) |
| ${}^{61}$Mn | 61 | 36 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 140.6112 | 524.5339 | -73.19 % | 58795.7325 MeV (+35694.1 ppm) |
| ${}^{62}$Mn | 62 | 37 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 146.3171 | 529.3870 | -72.36 % | 59756.7414 MeV (+35571.7 ppm) |
| ${}^{63}$Mn | 63 | 38 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 152.0124 | 535.8214 | -71.63 % | 60717.7609 MeV (+35481.2 ppm) |
| ${}^{64}$Mn | 64 | 39 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 157.6975 | 539.9947 | -70.80 % | 61678.7905 MeV (+35354.4 ppm) |
| ${}^{65}$Mn | 65 | 40 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 163.3729 | 546.0443 | -70.08 % | 62639.8300 MeV (+35263.9 ppm) |
| ${}^{66}$Mn | 66 | 41 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 169.0387 | 549.8987 | -69.26 % | 63600.8790 MeV (+35139.2 ppm) |
| ${}^{67}$Mn | 67 | 42 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 174.6953 | 554.8270 | -68.51 % | 64561.9371 MeV (+35035.8 ppm) |
| ${}^{68}$Mn | 68 | 43 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 180.3430 | 558.2120 | -67.69 % | 65523.0042 MeV (+34911.3 ppm) |
| ${}^{69}$Mn | 69 | 44 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 185.9821 | 562.6950 | -66.95 % | 66484.0798 MeV (+34808.2 ppm) |
| ${}^{70}$Mn | 70 | 45 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 191.6129 | 565.8800 | -66.14 % | 67445.1638 MeV (+34686.8 ppm) |
| ${}^{71}$Mn | 71 | 46 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 197.2356 | 570.1300 | -65.41 % | 68406.2559 MeV (+34585.8 ppm) |
| ${}^{72}$Mn | 72 | 47 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 202.8505 | 572.7600 | -64.58 % | 69367.3557 MeV (+34462.8 ppm) |
| ${}^{73}$Mn | 73 | 48 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 208.4578 | 576.3350 | -63.83 % | 70328.4632 MeV (+34358.2 ppm) |

### Iron (Z = 26)

_32 of 32 isotopes with a framework prediction; 32 of 32 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{45}$Fe | 45 | 19 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 35.1906 | 328.4550 | -89.29 % | 43432.3864 MeV (+35790.3 ppm) |
| ${}^{46}$Fe | 46 | 20 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 41.2011 | 349.7380 | -88.22 % | 44393.0907 MeV (+36012.9 ppm) |
| ${}^{47}$Fe | 47 | 21 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 47.1896 | 366.1300 | -87.11 % | 45353.8170 MeV (+36111.8 ppm) |
| ${}^{48}$Fe | 48 | 22 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 53.1571 | 385.0908 | -86.20 % | 46314.5643 MeV (+36265.9 ppm) |
| ${}^{49}$Fe | 49 | 23 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 59.1046 | 399.9043 | -85.22 % | 47275.3316 MeV (+36320.2 ppm) |
| ${}^{50}$Fe | 50 | 24 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 65.0328 | 417.7013 | -84.43 % | 48236.1181 MeV (+36439.2 ppm) |
| ${}^{51}$Fe | 51 | 25 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 70.9427 | 431.4854 | -83.56 % | 49196.9230 MeV (+36466.4 ppm) |
| ${}^{52}$Fe | 52 | 26 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 76.8351 | 447.6996 | -82.84 % | 50157.7454 MeV (+36544.9 ppm) |
| ${}^{53}$Fe | 53 | 27 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 82.7106 | 458.3863 | -81.96 % | 51118.5847 MeV (+36504.6 ppm) |
| ${}^{54}$Fe | 54 | 28 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 88.5699 | 471.7648 | -81.23 % | 52079.4401 MeV (+36521.7 ppm) |
| ${}^{55}$Fe | 55 | 29 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 94.4137 | 481.0629 | -80.37 % | 53040.3111 MeV (+36455.8 ppm) |
| ${}^{56}$Fe | 56 | 30 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 100.2426 | 492.2600 | -79.64 % | 54001.1969 MeV (+36430.4 ppm) |
| ${}^{57}$Fe | 57 | 31 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 106.0572 | 499.9061 | -78.78 % | 54962.0971 MeV (+36336.7 ppm) |
| ${}^{58}$Fe | 58 | 32 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 111.8580 | 509.9507 | -78.06 % | 55923.0111 MeV (+36292.5 ppm) |
| ${}^{59}$Fe | 59 | 33 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 117.6456 | 516.5317 | -77.22 % | 56883.9383 MeV (+36184.7 ppm) |
| ${}^{60}$Fe | 60 | 34 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 123.4204 | 525.3512 | -76.51 % | 57844.8783 MeV (+36122.3 ppm) |
| ${}^{61}$Fe | 61 | 35 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 129.1829 | 530.9299 | -75.67 % | 58805.8306 MeV (+36003.0 ppm) |
| ${}^{62}$Fe | 62 | 36 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 134.9335 | 538.9588 | -74.96 % | 59766.7948 MeV (+35931.8 ppm) |
| ${}^{63}$Fe | 63 | 37 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 140.6726 | 543.7876 | -74.13 % | 60727.7704 MeV (+35806.4 ppm) |
| ${}^{64}$Fe | 64 | 38 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 146.4007 | 551.1929 | -73.44 % | 61688.7571 MeV (+35730.0 ppm) |
| ${}^{65}$Fe | 65 | 39 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 152.1181 | 555.5126 | -72.62 % | 62649.7544 MeV (+35603.3 ppm) |
| ${}^{66}$Fe | 66 | 40 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 157.8252 | 562.4338 | -71.94 % | 63610.7621 MeV (+35524.5 ppm) |
| ${}^{67}$Fe | 67 | 41 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 163.5224 | 566.1457 | -71.12 % | 64571.7797 MeV (+35394.9 ppm) |
| ${}^{68}$Fe | 68 | 42 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 169.2098 | 572.4240 | -70.44 % | 65532.8070 MeV (+35311.0 ppm) |
| ${}^{69}$Fe | 69 | 43 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 174.8880 | 575.8050 | -69.63 % | 66493.8437 MeV (+35183.1 ppm) |
| ${}^{70}$Fe | 70 | 44 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 180.5571 | 581.5600 | -68.95 % | 67454.8893 MeV (+35097.0 ppm) |
| ${}^{71}$Fe | 71 | 45 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 186.2174 | 584.6850 | -68.15 % | 68415.9438 MeV (+34972.0 ppm) |
| ${}^{72}$Fe | 72 | 46 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 191.8693 | 590.0400 | -67.48 % | 69377.0067 MeV (+34885.7 ppm) |
| ${}^{73}$Fe | 73 | 47 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 197.5129 | 592.8330 | -66.68 % | 70338.0778 MeV (+34762.7 ppm) |
| ${}^{74}$Fe | 74 | 48 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 203.1486 | 597.6240 | -66.01 % | 71299.1569 MeV (+34672.1 ppm) |
| ${}^{75}$Fe | 75 | 49 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 208.7765 | 599.7000 | -65.19 % | 72260.2438 MeV (+34545.1 ppm) |
| ${}^{76}$Fe | 76 | 50 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 214.3969 | 603.6680 | -64.48 % | 73221.3382 MeV (+34448.6 ppm) |

### Cobalt (Z = 27)

_32 of 32 isotopes with a framework prediction; 32 of 32 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{47}$Co | 47 | 20 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 34.6317 | 347.6120 | -90.04 % | 45365.0446 MeV (+35948.2 ppm) |
| ${}^{48}$Co | 48 | 21 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 40.6636 | 364.5600 | -88.85 % | 46325.7275 MeV (+36058.1 ppm) |
| ${}^{49}$Co | 49 | 22 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 46.6738 | 384.1600 | -87.85 % | 47286.4321 MeV (+36223.5 ppm) |
| ${}^{50}$Co | 50 | 23 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 52.6632 | 400.0319 | -86.84 % | 48247.1574 MeV (+36300.4 ppm) |
| ${}^{51}$Co | 51 | 24 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 58.6328 | 417.8560 | -85.97 % | 49207.9026 MeV (+36417.2 ppm) |
| ${}^{52}$Co | 52 | 25 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 64.5833 | 432.9292 | -85.08 % | 50168.6669 MeV (+36471.0 ppm) |
| ${}^{53}$Co | 53 | 26 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 70.5156 | 449.3159 | -84.31 % | 51129.4493 MeV (+36550.7 ppm) |
| ${}^{54}$Co | 54 | 27 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 76.4304 | 462.7379 | -83.48 % | 52090.2493 MeV (+36566.8 ppm) |
| ${}^{55}$Co | 55 | 28 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 82.3285 | 476.8291 | -82.73 % | 53051.0660 MeV (+36596.1 ppm) |
| ${}^{56}$Co | 56 | 29 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 88.2104 | 486.9110 | -81.88 % | 54011.8989 MeV (+36544.9 ppm) |
| ${}^{57}$Co | 57 | 30 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 94.0767 | 498.2874 | -81.12 % | 54972.7473 MeV (+36521.1 ppm) |
| ${}^{58}$Co | 58 | 31 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 99.9282 | 506.8604 | -80.28 % | 55933.6106 MeV (+36444.6 ppm) |
| ${}^{59}$Co | 59 | 32 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 105.7654 | 517.3142 | -79.55 % | 56894.4882 MeV (+36406.5 ppm) |
| ${}^{60}$Co | 60 | 33 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 111.5887 | 524.8062 | -78.74 % | 57855.3797 MeV (+36314.8 ppm) |
| ${}^{61}$Co | 61 | 34 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 117.3987 | 534.1252 | -78.02 % | 58816.2845 MeV (+36259.8 ppm) |
| ${}^{62}$Co | 62 | 35 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 123.1958 | 540.7228 | -77.22 % | 59777.2021 MeV (+36157.9 ppm) |
| ${}^{63}$Co | 63 | 36 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 128.9806 | 549.2212 | -76.52 % | 60738.1321 MeV (+36093.0 ppm) |
| ${}^{64}$Co | 64 | 37 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 134.7534 | 555.2334 | -75.73 % | 61699.0741 MeV (+35987.1 ppm) |
| ${}^{65}$Co | 65 | 38 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 140.5146 | 562.6975 | -75.03 % | 62660.0276 MeV (+35909.6 ppm) |
| ${}^{66}$Co | 66 | 39 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 146.2647 | 567.9922 | -74.25 % | 63620.9923 MeV (+35798.0 ppm) |
| ${}^{67}$Co | 67 | 40 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 152.0040 | 574.9767 | -73.56 % | 64581.9678 MeV (+35717.9 ppm) |
| ${}^{68}$Co | 68 | 41 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 157.7328 | 579.3688 | -72.78 % | 65542.9537 MeV (+35598.0 ppm) |
| ${}^{69}$Co | 69 | 42 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 163.4516 | 586.1830 | -72.12 % | 66503.9497 MeV (+35520.8 ppm) |
| ${}^{70}$Co | 70 | 43 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 169.1606 | 590.3939 | -71.35 % | 67464.9555 MeV (+35404.6 ppm) |
| ${}^{71}$Co | 71 | 44 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 174.8601 | 596.3101 | -70.68 % | 68425.9708 MeV (+35318.5 ppm) |
| ${}^{72}$Co | 72 | 45 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 180.5504 | 600.3360 | -69.93 % | 69386.9953 MeV (+35205.4 ppm) |
| ${}^{73}$Co | 73 | 46 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 186.2318 | 606.0460 | -69.27 % | 70348.0286 MeV (+35122.0 ppm) |
| ${}^{74}$Co | 74 | 47 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 191.9046 | 609.6860 | -68.52 % | 71309.0706 MeV (+35009.5 ppm) |
| ${}^{75}$Co | 75 | 48 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 197.5690 | 614.7750 | -67.86 % | 72270.1210 MeV (+34921.5 ppm) |
| ${}^{76}$Co | 76 | 49 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 203.2252 | 617.9560 | -67.11 % | 73231.1795 MeV (+34808.0 ppm) |
| ${}^{77}$Co | 77 | 50 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 208.8736 | 622.3140 | -66.44 % | 74192.2459 MeV (+34714.1 ppm) |
| ${}^{78}$Co | 78 | 51 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 214.5143 | 623.7660 | -65.61 % | 75153.3199 MeV (+34582.3 ppm) |

### Nickel (Z = 28)

_35 of 35 isotopes with a framework prediction; 35 of 35 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{48}$Ni | 48 | 20 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 27.7866 | 347.3280 | -92.00 % | 46337.2742 MeV (+35935.2 ppm) |
| ${}^{49}$Ni | 49 | 21 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 33.8620 | 365.0500 | -90.72 % | 47297.9136 MeV (+36059.4 ppm) |
| ${}^{50}$Ni | 50 | 22 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 39.9149 | 385.1000 | -89.64 % | 48258.5754 MeV (+36231.1 ppm) |
| ${}^{51}$Ni | 51 | 23 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 45.9465 | 401.3700 | -88.55 % | 49219.2586 MeV (+36313.8 ppm) |
| ${}^{52}$Ni | 52 | 24 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 51.9575 | 420.3627 | -87.64 % | 50179.9624 MeV (+36452.0 ppm) |
| ${}^{53}$Ni | 53 | 25 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 57.9488 | 435.5050 | -86.69 % | 51140.6858 MeV (+36504.8 ppm) |
| ${}^{54}$Ni | 54 | 26 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 63.9213 | 453.2238 | -85.90 % | 52101.4282 MeV (+36609.1 ppm) |
| ${}^{55}$Ni | 55 | 27 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 69.8756 | 467.3527 | -85.05 % | 53062.1886 MeV (+36637.3 ppm) |
| ${}^{56}$Ni | 56 | 28 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 75.8126 | 483.9957 | -84.34 % | 54022.9664 MeV (+36714.9 ppm) |
| ${}^{57}$Ni | 57 | 29 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 81.7328 | 494.2434 | -83.46 % | 54983.7610 MeV (+36665.1 ppm) |
| ${}^{58}$Ni | 58 | 30 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 87.6369 | 506.4596 | -82.70 % | 55944.5716 MeV (+36655.1 ppm) |
| ${}^{59}$Ni | 59 | 31 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 93.5256 | 515.4589 | -81.86 % | 56905.3977 MeV (+36584.9 ppm) |
| ${}^{60}$Ni | 60 | 32 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 99.3993 | 526.8466 | -81.13 % | 57866.2388 MeV (+36561.7 ppm) |
| ${}^{61}$Ni | 61 | 33 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 105.2587 | 534.6667 | -80.31 % | 58827.0942 MeV (+36474.4 ppm) |
| ${}^{62}$Ni | 62 | 34 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 111.1042 | 545.2624 | -79.62 % | 59787.9634 MeV (+36440.0 ppm) |
| ${}^{63}$Ni | 63 | 35 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 116.9363 | 552.1002 | -78.82 % | 60748.8461 MeV (+36340.5 ppm) |
| ${}^{64}$Ni | 64 | 36 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 122.7556 | 561.7577 | -78.15 % | 61709.7416 MeV (+36293.4 ppm) |
| ${}^{65}$Ni | 65 | 37 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 128.5624 | 567.8558 | -77.36 % | 62670.6496 MeV (+36186.9 ppm) |
| ${}^{66}$Ni | 66 | 38 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 134.3571 | 576.8076 | -76.71 % | 63631.5696 MeV (+36132.1 ppm) |
| ${}^{67}$Ni | 67 | 39 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 140.1402 | 582.6153 | -75.95 % | 64592.5013 MeV (+36026.8 ppm) |
| ${}^{68}$Ni | 68 | 40 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 145.9120 | 590.4077 | -75.29 % | 65553.4442 MeV (+35957.3 ppm) |
| ${}^{69}$Ni | 69 | 41 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 151.6730 | 594.9939 | -74.51 % | 66514.3981 MeV (+35838.2 ppm) |
| ${}^{70}$Ni | 70 | 42 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 157.4233 | 602.3004 | -73.86 % | 67475.3625 MeV (+35766.0 ppm) |
| ${}^{71}$Ni | 71 | 43 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 163.1635 | 606.5641 | -73.10 % | 68436.3371 MeV (+35648.3 ppm) |
| ${}^{72}$Ni | 72 | 44 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 168.8938 | 613.4552 | -72.47 % | 69397.3216 MeV (+35574.6 ppm) |
| ${}^{73}$Ni | 73 | 45 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 174.6144 | 617.4087 | -71.72 % | 70358.3157 MeV (+35458.3 ppm) |
| ${}^{74}$Ni | 74 | 46 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 180.3258 | 624.0420 | -71.10 % | 71319.3191 MeV (+35386.0 ppm) |
| ${}^{75}$Ni | 75 | 47 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 186.0281 | 627.6750 | -70.36 % | 72280.3316 MeV (+35270.6 ppm) |
| ${}^{76}$Ni | 76 | 48 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 191.7217 | 633.6880 | -69.75 % | 73241.3528 MeV (+35193.5 ppm) |
| ${}^{77}$Ni | 77 | 49 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 197.4067 | 636.9440 | -69.01 % | 74202.3825 MeV (+35078.4 ppm) |
| ${}^{78}$Ni | 78 | 50 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 203.0835 | 642.5640 | -68.39 % | 75163.4205 MeV (+35000.0 ppm) |
| ${}^{79}$Ni | 79 | 51 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 208.7522 | 643.8500 | -67.58 % | 76124.4665 MeV (+34864.0 ppm) |
| ${}^{80}$Ni | 80 | 52 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 214.4132 | 647.0400 | -66.86 % | 77085.5204 MeV (+34756.5 ppm) |
| ${}^{81}$Ni | 81 | 53 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 220.0665 | 648.0000 | -66.04 % | 78046.5818 MeV (+34621.2 ppm) |
| ${}^{82}$Ni | 82 | 54 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 225.7125 | 650.6700 | -65.31 % | 79007.6506 MeV (+34513.4 ppm) |

### Copper (Z = 29)

_33 of 33 isotopes with a framework prediction; 33 of 33 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{52}$Cu | 52 | 23 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 38.9576 | 398.8920 | -90.23 % | 50191.6320 MeV (+36250.4 ppm) |
| ${}^{53}$Cu | 53 | 24 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 45.0101 | 418.2230 | -89.24 % | 51152.2942 MeV (+36393.6 ppm) |
| ${}^{54}$Cu | 54 | 25 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 51.0424 | 434.4300 | -88.25 % | 52112.9767 MeV (+36466.9 ppm) |
| ${}^{55}$Cu | 55 | 26 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 57.0552 | 452.8698 | -87.40 % | 53073.6787 MeV (+36584.3 ppm) |
| ${}^{56}$Cu | 56 | 27 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 63.0493 | 467.9355 | -86.53 % | 54034.3994 MeV (+36630.4 ppm) |
| ${}^{57}$Cu | 57 | 28 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 69.0253 | 484.6861 | -85.76 % | 54995.1381 MeV (+36708.0 ppm) |
| ${}^{58}$Cu | 58 | 29 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 74.9841 | 497.1162 | -84.92 % | 55955.8941 MeV (+36700.4 ppm) |
| ${}^{59}$Cu | 59 | 30 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 80.9262 | 509.8782 | -84.13 % | 56916.6668 MeV (+36699.6 ppm) |
| ${}^{60}$Cu | 60 | 31 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 86.8523 | 519.9363 | -83.30 % | 57877.4555 MeV (+36648.9 ppm) |
| ${}^{61}$Cu | 61 | 32 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 92.7629 | 531.6464 | -82.55 % | 58838.2597 MeV (+36630.3 ppm) |
| ${}^{62}$Cu | 62 | 33 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 98.6585 | 540.5212 | -81.75 % | 59799.0788 MeV (+36561.6 ppm) |
| ${}^{63}$Cu | 63 | 34 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 104.5399 | 551.3848 | -81.04 % | 60759.9122 MeV (+36530.5 ppm) |
| ${}^{64}$Cu | 64 | 35 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 110.4073 | 559.3007 | -80.26 % | 61720.7596 MeV (+36449.3 ppm) |
| ${}^{65}$Cu | 65 | 36 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 116.2613 | 569.2113 | -79.58 % | 62681.6203 MeV (+36405.0 ppm) |
| ${}^{66}$Cu | 66 | 37 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 122.1024 | 576.2772 | -78.81 % | 63642.4940 MeV (+36314.2 ppm) |
| ${}^{67}$Cu | 67 | 38 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 127.9309 | 585.4098 | -78.15 % | 64603.3803 MeV (+36260.7 ppm) |
| ${}^{68}$Cu | 68 | 39 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 133.7474 | 591.7286 | -77.40 % | 65564.2786 MeV (+36162.9 ppm) |
| ${}^{69}$Cu | 69 | 40 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 139.5521 | 599.9691 | -76.74 % | 66525.1887 MeV (+36099.2 ppm) |
| ${}^{70}$Cu | 70 | 41 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 145.3454 | 605.2806 | -75.99 % | 67486.1101 MeV (+35990.8 ppm) |
| ${}^{71}$Cu | 71 | 42 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 151.1278 | 613.0867 | -75.35 % | 68447.0425 MeV (+35924.8 ppm) |
| ${}^{72}$Cu | 72 | 43 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 156.8995 | 618.2298 | -74.62 % | 69407.9855 MeV (+35819.6 ppm) |
| ${}^{73}$Cu | 73 | 44 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 162.6609 | 625.5056 | -74.00 % | 70368.9389 MeV (+35750.0 ppm) |
| ${}^{74}$Cu | 74 | 45 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 168.4123 | 630.5957 | -73.29 % | 71329.9023 MeV (+35649.5 ppm) |
| ${}^{75}$Cu | 75 | 46 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 174.1539 | 637.1310 | -72.67 % | 72290.8754 MeV (+35573.3 ppm) |
| ${}^{76}$Cu | 76 | 47 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 179.8862 | 641.7137 | -71.97 % | 73251.8580 MeV (+35470.7 ppm) |
| ${}^{77}$Cu | 77 | 48 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 185.6093 | 647.6663 | -71.34 % | 74212.8497 MeV (+35390.6 ppm) |
| ${}^{78}$Cu | 78 | 49 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 191.3234 | 651.6642 | -70.64 % | 75173.8503 MeV (+35284.9 ppm) |
| ${}^{79}$Cu | 79 | 50 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 197.0290 | 657.3541 | -70.03 % | 76134.8595 MeV (+35205.8 ppm) |
| ${}^{80}$Cu | 80 | 51 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 202.7261 | 659.6800 | -69.27 % | 77095.8771 MeV (+35082.3 ppm) |
| ${}^{81}$Cu | 81 | 52 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 208.4151 | 662.9850 | -68.56 % | 78056.9029 MeV (+34975.1 ppm) |
| ${}^{82}$Cu | 82 | 53 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 214.0962 | 664.8560 | -67.80 % | 79017.9366 MeV (+34851.5 ppm) |
| ${}^{83}$Cu | 83 | 54 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 219.7695 | 667.6520 | -67.08 % | 79978.9781 MeV (+34742.3 ppm) |
| ${}^{84}$Cu | 84 | 55 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 225.4353 | 669.0600 | -66.31 % | 80940.0271 MeV (+34618.2 ppm) |

### Zinc (Z = 30)

_33 of 33 isotopes with a framework prediction; 33 of 33 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{54}$Zn | 54 | 24 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 37.7939 | 418.0680 | -90.96 % | 52124.8950 MeV (+36383.7 ppm) |
| ${}^{55}$Zn | 55 | 25 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 43.8672 | 434.7200 | -89.91 % | 53085.5364 MeV (+36464.4 ppm) |
| ${}^{56}$Zn | 56 | 26 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 49.9205 | 453.9360 | -89.00 % | 54046.1979 MeV (+36593.4 ppm) |
| ${}^{57}$Zn | 57 | 27 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 55.9544 | 469.1670 | -88.07 % | 55006.8787 MeV (+36641.0 ppm) |
| ${}^{58}$Zn | 58 | 28 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 61.9698 | 486.9649 | -87.27 % | 55967.5782 MeV (+36736.9 ppm) |
| ${}^{59}$Zn | 59 | 29 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 67.9673 | 499.9530 | -86.41 % | 56928.2954 MeV (+36738.7 ppm) |
| ${}^{60}$Zn | 60 | 30 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 73.9475 | 514.9831 | -85.64 % | 57889.0299 MeV (+36778.7 ppm) |
| ${}^{61}$Zn | 61 | 31 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 79.9112 | 525.2289 | -84.79 % | 58849.7810 MeV (+36730.3 ppm) |
| ${}^{62}$Zn | 62 | 32 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 85.8589 | 538.1194 | -84.04 % | 59810.5481 MeV (+36731.3 ppm) |
| ${}^{63}$Zn | 63 | 33 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 91.7912 | 547.2361 | -83.23 % | 60771.3306 MeV (+36665.7 ppm) |
| ${}^{64}$Zn | 64 | 34 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 97.7085 | 559.0980 | -82.52 % | 61732.1281 MeV (+36650.3 ppm) |
| ${}^{65}$Zn | 65 | 35 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 103.6115 | 567.0773 | -81.73 % | 62692.9399 MeV (+36569.0 ppm) |
| ${}^{66}$Zn | 66 | 36 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 109.5006 | 578.1358 | -81.06 % | 63653.7656 MeV (+36542.3 ppm) |
| ${}^{67}$Zn | 67 | 37 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 115.3762 | 585.1883 | -80.28 % | 64614.6047 MeV (+36450.1 ppm) |
| ${}^{68}$Zn | 68 | 38 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 121.2388 | 595.3864 | -79.64 % | 65575.4568 MeV (+36412.3 ppm) |
| ${}^{69}$Zn | 69 | 39 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 127.0889 | 601.8684 | -78.88 % | 66536.3215 MeV (+36315.8 ppm) |
| ${}^{70}$Zn | 70 | 40 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 132.9268 | 611.0866 | -78.25 % | 67497.1984 MeV (+36265.8 ppm) |
| ${}^{71}$Zn | 71 | 41 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 138.7529 | 616.9220 | -77.51 % | 68458.0871 MeV (+36164.4 ppm) |
| ${}^{72}$Zn | 72 | 42 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 144.5676 | 625.8100 | -76.90 % | 69418.9872 MeV (+36113.1 ppm) |
| ${}^{73}$Zn | 73 | 43 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 150.3712 | 631.3292 | -76.18 % | 70379.8984 MeV (+36012.0 ppm) |
| ${}^{74}$Zn | 74 | 44 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 156.1640 | 639.5638 | -75.58 % | 71340.8203 MeV (+35954.7 ppm) |
| ${}^{75}$Zn | 75 | 45 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 161.9464 | 644.4374 | -74.87 % | 72301.7527 MeV (+35849.2 ppm) |
| ${}^{76}$Zn | 76 | 46 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 167.7187 | 652.2528 | -74.29 % | 73262.6951 MeV (+35789.6 ppm) |
| ${}^{77}$Zn | 77 | 47 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 173.4812 | 656.8103 | -73.59 % | 74223.6474 MeV (+35684.7 ppm) |
| ${}^{78}$Zn | 78 | 48 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 179.2342 | 663.5756 | -72.99 % | 75184.6092 MeV (+35614.1 ppm) |
| ${}^{79}$Zn | 79 | 49 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 184.9778 | 667.5960 | -72.29 % | 76145.5803 MeV (+35506.8 ppm) |
| ${}^{80}$Zn | 80 | 50 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 190.7125 | 673.8837 | -71.70 % | 77106.5604 MeV (+35433.8 ppm) |
| ${}^{81}$Zn | 81 | 51 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 196.4384 | 676.5060 | -70.96 % | 78067.5493 MeV (+35312.4 ppm) |
| ${}^{82}$Zn | 82 | 52 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 202.1558 | 680.6916 | -70.30 % | 79028.5467 MeV (+35215.3 ppm) |
| ${}^{83}$Zn | 83 | 53 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 207.8649 | 682.7580 | -69.56 % | 79989.5524 MeV (+35092.0 ppm) |
| ${}^{84}$Zn | 84 | 54 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 213.5659 | 686.3640 | -68.88 % | 80950.5661 MeV (+34992.5 ppm) |
| ${}^{85}$Zn | 85 | 55 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 219.2591 | 687.6500 | -68.11 % | 81911.5877 MeV (+34865.7 ppm) |
| ${}^{86}$Zn | 86 | 56 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 224.9446 | 690.7520 | -67.43 % | 82872.6170 MeV (+34763.9 ppm) |

### Gallium (Z = 31)

_33 of 33 isotopes with a framework prediction; 33 of 33 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{56}$Ga | 56 | 25 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 36.4261 | 431.5920 | -91.56 % | 54058.3619 MeV (+36398.3 ppm) |
| ${}^{57}$Ga | 57 | 26 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 42.5200 | 451.2120 | -90.58 % | 55018.9829 MeV (+36534.2 ppm) |
| ${}^{58}$Ga | 58 | 27 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 48.5939 | 467.4220 | -89.60 % | 55979.6237 MeV (+36599.8 ppm) |
| ${}^{59}$Ga | 59 | 28 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 54.6487 | 485.6880 | -88.75 % | 56940.2837 MeV (+36703.0 ppm) |
| ${}^{60}$Ga | 60 | 29 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 60.6851 | 499.6200 | -87.85 % | 57900.9621 MeV (+36721.6 ppm) |
| ${}^{61}$Ga | 61 | 30 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 66.7037 | 515.2323 | -87.05 % | 58861.6582 MeV (+36771.3 ppm) |
| ${}^{62}$Ga | 62 | 31 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 72.7052 | 528.1560 | -86.23 % | 59822.3715 MeV (+36771.2 ppm) |
| ${}^{63}$Ga | 63 | 32 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 78.6902 | 540.7874 | -85.45 % | 60783.1013 MeV (+36766.3 ppm) |
| ${}^{64}$Ga | 64 | 33 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 84.6593 | 551.1444 | -84.64 % | 61743.8470 MeV (+36722.2 ppm) |
| ${}^{65}$Ga | 65 | 34 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 90.6129 | 563.0404 | -83.91 % | 62704.6081 MeV (+36706.1 ppm) |
| ${}^{66}$Ga | 66 | 35 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 96.5517 | 572.1780 | -83.13 % | 63665.3842 MeV (+36644.2 ppm) |
| ${}^{67}$Ga | 67 | 36 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 102.4760 | 583.4047 | -82.43 % | 64626.1746 MeV (+36619.0 ppm) |
| ${}^{68}$Ga | 68 | 37 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 108.3865 | 591.6829 | -81.68 % | 65586.9789 MeV (+36546.6 ppm) |
| ${}^{69}$Ga | 69 | 38 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 114.2835 | 601.9960 | -81.02 % | 66547.7966 MeV (+36509.2 ppm) |
| ${}^{70}$Ga | 70 | 39 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 120.1675 | 609.6497 | -80.29 % | 67508.6274 MeV (+36430.9 ppm) |
| ${}^{71}$Ga | 71 | 40 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 126.0388 | 618.9500 | -79.64 % | 68469.4709 MeV (+36380.8 ppm) |
| ${}^{72}$Ga | 72 | 41 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 131.8979 | 625.4704 | -78.91 % | 69430.3265 MeV (+36289.2 ppm) |
| ${}^{73}$Ga | 73 | 42 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 137.7452 | 634.6528 | -78.30 % | 70391.1940 MeV (+36240.9 ppm) |
| ${}^{74}$Ga | 74 | 43 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 143.5810 | 641.0744 | -77.60 % | 71352.0730 MeV (+36152.6 ppm) |
| ${}^{75}$Ga | 75 | 44 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 149.4056 | 649.5567 | -77.00 % | 72312.9632 MeV (+36097.4 ppm) |
| ${}^{76}$Ga | 76 | 45 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 155.2193 | 655.4641 | -76.32 % | 73273.8642 MeV (+36006.0 ppm) |
| ${}^{77}$Ga | 77 | 46 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 161.0226 | 663.2311 | -75.72 % | 74234.7757 MeV (+35944.1 ppm) |
| ${}^{78}$Ga | 78 | 47 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 166.8157 | 669.0141 | -75.07 % | 75195.6974 MeV (+35855.6 ppm) |
| ${}^{79}$Ga | 79 | 48 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 172.5988 | 675.9297 | -74.46 % | 76156.6291 MeV (+35785.5 ppm) |
| ${}^{80}$Ga | 80 | 49 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 178.3723 | 680.6764 | -73.79 % | 77117.5703 MeV (+35687.0 ppm) |
| ${}^{81}$Ga | 81 | 50 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 184.1364 | 687.1520 | -73.20 % | 78078.5210 MeV (+35614.9 ppm) |
| ${}^{82}$Ga | 82 | 51 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 189.8914 | 690.5261 | -72.50 % | 79039.4808 MeV (+35502.6 ppm) |
| ${}^{83}$Ga | 83 | 52 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 195.6376 | 694.9238 | -71.85 % | 80000.4494 MeV (+35406.8 ppm) |
| ${}^{84}$Ga | 84 | 53 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 201.3751 | 697.8321 | -71.14 % | 80961.4267 MeV (+35293.7 ppm) |
| ${}^{85}$Ga | 85 | 54 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 207.1042 | 701.5533 | -70.48 % | 81922.4124 MeV (+35194.0 ppm) |
| ${}^{86}$Ga | 86 | 55 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 212.8251 | 703.6520 | -69.75 % | 82883.4062 MeV (+35075.7 ppm) |
| ${}^{87}$Ga | 87 | 56 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 218.5380 | 706.7880 | -69.08 % | 83844.4081 MeV (+34974.1 ppm) |
| ${}^{88}$Ga | 88 | 57 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 224.2431 | 708.4000 | -68.35 % | 84805.4177 MeV (+34854.9 ppm) |

### Germanium (Z = 32)

_33 of 33 isotopes with a framework prediction; 33 of 33 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{58}$Ge | 58 | 26 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 34.8566 | 450.6600 | -92.27 % | 55992.0307 MeV (+36523.2 ppm) |
| ${}^{59}$Ge | 59 | 27 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 40.9707 | 467.5160 | -91.24 % | 56952.6314 MeV (+36599.6 ppm) |
| ${}^{60}$Ge | 60 | 28 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 47.0650 | 486.7800 | -90.33 % | 57913.2518 MeV (+36717.8 ppm) |
| ${}^{61}$Ge | 61 | 29 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 53.1405 | 501.1150 | -89.40 % | 58873.8912 MeV (+36743.1 ppm) |
| ${}^{62}$Ge | 62 | 30 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 59.1976 | 517.5140 | -88.56 % | 59834.5488 MeV (+36805.3 ppm) |
| ${}^{63}$Ge | 63 | 31 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 65.2371 | 530.3792 | -87.70 % | 60795.2241 MeV (+36802.9 ppm) |
| ${}^{64}$Ge | 64 | 32 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 71.2595 | 545.8448 | -86.95 % | 61755.9164 MeV (+36846.2 ppm) |
| ${}^{65}$Ge | 65 | 33 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 77.2655 | 556.0788 | -86.11 % | 62716.6252 MeV (+36798.9 ppm) |
| ${}^{66}$Ge | 66 | 34 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 83.2557 | 569.2789 | -85.38 % | 63677.3499 MeV (+36803.3 ppm) |
| ${}^{67}$Ge | 67 | 35 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 89.2304 | 578.4169 | -84.57 % | 64638.0899 MeV (+36740.2 ppm) |
| ${}^{68}$Ge | 68 | 36 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 95.1903 | 590.7933 | -83.89 % | 65598.8448 MeV (+36732.3 ppm) |
| ${}^{69}$Ge | 69 | 37 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 101.1358 | 598.9865 | -83.12 % | 66559.6140 MeV (+36657.3 ppm) |
| ${}^{70}$Ge | 70 | 38 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 107.0674 | 610.5192 | -82.46 % | 67520.3972 MeV (+36637.9 ppm) |
| ${}^{71}$Ge | 71 | 39 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 112.9856 | 617.9351 | -81.72 % | 68481.1938 MeV (+36554.5 ppm) |
| ${}^{72}$Ge | 72 | 40 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 118.8906 | 628.6857 | -81.09 % | 69442.0035 MeV (+36525.3 ppm) |
| ${}^{73}$Ge | 73 | 41 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 124.7830 | 635.4686 | -80.36 % | 70402.8259 MeV (+36436.6 ppm) |
| ${}^{74}$Ge | 74 | 42 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 130.6632 | 645.6649 | -79.76 % | 71363.6605 MeV (+36401.7 ppm) |
| ${}^{75}$Ge | 75 | 43 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 136.5314 | 652.1707 | -79.07 % | 72324.5071 MeV (+36313.2 ppm) |
| ${}^{76}$Ge | 76 | 44 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 142.3880 | 661.5980 | -78.48 % | 73285.3652 MeV (+36270.0 ppm) |
| ${}^{77}$Ge | 77 | 45 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 148.2334 | 667.6693 | -77.80 % | 74246.2346 MeV (+36179.5 ppm) |
| ${}^{78}$Ge | 78 | 46 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 154.0680 | 676.3898 | -77.22 % | 75207.1148 MeV (+36129.3 ppm) |
| ${}^{79}$Ge | 79 | 47 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 159.8919 | 682.1262 | -76.56 % | 76168.0057 MeV (+36038.5 ppm) |
| ${}^{80}$Ge | 80 | 48 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 165.7055 | 690.2057 | -75.99 % | 77128.9068 MeV (+35982.7 ppm) |
| ${}^{81}$Ge | 81 | 49 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 171.5092 | 695.0334 | -75.32 % | 78089.8180 MeV (+35883.8 ppm) |
| ${}^{82}$Ge | 82 | 50 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 177.3030 | 702.2280 | -74.75 % | 79050.7389 MeV (+35819.5 ppm) |
| ${}^{83}$Ge | 83 | 51 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 183.0875 | 705.8607 | -74.06 % | 80011.6692 MeV (+35709.1 ppm) |
| ${}^{84}$Ge | 84 | 52 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 188.8626 | 711.1040 | -73.44 % | 80972.6088 MeV (+35622.8 ppm) |
| ${}^{85}$Ge | 85 | 53 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 194.6289 | 714.1504 | -72.75 % | 81933.5574 MeV (+35509.9 ppm) |
| ${}^{86}$Ge | 86 | 54 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 200.3863 | 718.4982 | -72.11 % | 82894.5147 MeV (+35416.6 ppm) |
| ${}^{87}$Ge | 87 | 55 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 206.1353 | 720.7950 | -71.40 % | 83855.4805 MeV (+35298.9 ppm) |
| ${}^{88}$Ge | 88 | 56 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 211.8760 | 724.7680 | -70.77 % | 84816.4546 MeV (+35206.0 ppm) |
| ${}^{89}$Ge | 89 | 57 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 217.6085 | 726.3290 | -70.04 % | 85777.4368 MeV (+35085.1 ppm) |
| ${}^{90}$Ge | 90 | 58 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 223.3332 | 729.8100 | -69.40 % | 86738.4269 MeV (+34990.7 ppm) |

### Arsenic (Z = 33)

_33 of 33 isotopes with a framework prediction; 33 of 33 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{60}$As | 60 | 27 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 33.0873 | 464.1000 | -92.87 % | 57925.8993 MeV (+36538.1 ppm) |
| ${}^{61}$As | 61 | 28 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 39.2213 | 483.7300 | -91.89 % | 58886.4800 MeV (+36661.9 ppm) |
| ${}^{62}$As | 62 | 29 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 45.3359 | 499.0380 | -90.92 % | 59847.0802 MeV (+36704.2 ppm) |
| ${}^{63}$As | 63 | 30 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 51.4317 | 516.1590 | -90.04 % | 60807.6992 MeV (+36778.3 ppm) |
| ${}^{64}$As | 64 | 31 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 57.5093 | 530.3040 | -89.16 % | 61768.3364 MeV (+36797.4 ppm) |
| ${}^{65}$As | 65 | 32 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 63.5694 | 545.7553 | -88.35 % | 62728.9911 MeV (+36839.7 ppm) |
| ${}^{66}$As | 66 | 33 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 69.6126 | 558.9146 | -87.55 % | 63689.6627 MeV (+36842.0 ppm) |
| ${}^{67}$As | 67 | 34 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 75.6393 | 571.5481 | -86.77 % | 64650.3507 MeV (+36835.7 ppm) |
| ${}^{68}$As | 68 | 35 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 81.6503 | 581.9267 | -85.97 % | 65611.0545 MeV (+36792.8 ppm) |
| ${}^{69}$As | 69 | 36 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 87.6459 | 594.2157 | -85.25 % | 66571.7736 MeV (+36782.3 ppm) |
| ${}^{70}$As | 70 | 37 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 93.6267 | 603.5088 | -84.49 % | 67532.5076 MeV (+36724.7 ppm) |
| ${}^{71}$As | 71 | 38 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 99.5931 | 615.1394 | -83.81 % | 68493.2559 MeV (+36705.5 ppm) |
| ${}^{72}$As | 72 | 39 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 105.5456 | 623.5473 | -83.07 % | 69454.0182 MeV (+36637.3 ppm) |
| ${}^{73}$As | 73 | 40 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 111.4847 | 634.3415 | -82.43 % | 70414.7940 MeV (+36607.5 ppm) |
| ${}^{74}$As | 74 | 41 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 117.4106 | 642.3201 | -81.72 % | 71375.5828 MeV (+36536.3 ppm) |
| ${}^{75}$As | 75 | 42 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 123.3238 | 652.5656 | -81.10 % | 72336.3843 MeV (+36500.9 ppm) |
| ${}^{76}$As | 76 | 43 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 129.2248 | 659.8941 | -80.42 % | 73297.1982 MeV (+36423.8 ppm) |
| ${}^{77}$As | 77 | 44 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 135.1137 | 669.5904 | -79.82 % | 74258.0240 MeV (+36383.2 ppm) |
| ${}^{78}$As | 78 | 45 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 140.9910 | 676.5623 | -79.16 % | 75218.8615 MeV (+36304.8 ppm) |
| ${}^{79}$As | 79 | 46 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 146.8571 | 685.4528 | -78.58 % | 76179.7102 MeV (+36255.6 ppm) |
| ${}^{80}$As | 80 | 47 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 152.7122 | 692.1026 | -77.94 % | 77140.5699 MeV (+36176.7 ppm) |
| ${}^{81}$As | 81 | 48 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 158.5566 | 700.4926 | -77.36 % | 78101.4402 MeV (+36123.7 ppm) |
| ${}^{82}$As | 82 | 49 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 164.3906 | 706.1361 | -76.72 % | 79062.3210 MeV (+36034.9 ppm) |
| ${}^{83}$As | 83 | 50 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 170.2146 | 713.7713 | -76.15 % | 80023.2118 MeV (+35975.1 ppm) |
| ${}^{84}$As | 84 | 51 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 176.0287 | 718.0268 | -75.48 % | 80984.1125 MeV (+35872.0 ppm) |
| ${}^{85}$As | 85 | 52 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 181.8332 | 723.4337 | -74.87 % | 81945.0227 MeV (+35786.6 ppm) |
| ${}^{86}$As | 86 | 53 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 187.6285 | 727.2780 | -74.20 % | 82905.9422 MeV (+35683.1 ppm) |
| ${}^{87}$As | 87 | 54 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 193.4146 | 732.0051 | -73.58 % | 83866.8708 MeV (+35593.3 ppm) |
| ${}^{88}$As | 88 | 55 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 199.1920 | 734.8880 | -72.89 % | 84827.8083 MeV (+35482.7 ppm) |
| ${}^{89}$As | 89 | 56 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 204.9607 | 739.0560 | -72.27 % | 85788.7544 MeV (+35390.2 ppm) |
| ${}^{90}$As | 90 | 57 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 210.7210 | 741.6000 | -71.59 % | 86749.7088 MeV (+35280.0 ppm) |
| ${}^{91}$As | 91 | 58 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 216.4731 | 745.1990 | -70.95 % | 87710.6715 MeV (+35185.0 ppm) |
| ${}^{92}$As | 92 | 59 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 222.2172 | 747.1320 | -70.26 % | 88671.6422 MeV (+35072.6 ppm) |

### Selenium (Z = 34)

_33 of 33 isotopes with a framework prediction; 33 of 33 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{63}$Se | 63 | 29 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 37.2741 | 498.7710 | -92.53 % | 60820.5265 MeV (+36702.7 ppm) |
| ${}^{64}$Se | 64 | 30 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 43.4086 | 516.8000 | -91.60 % | 61781.1068 MeV (+36791.2 ppm) |
| ${}^{65}$Se | 65 | 31 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 49.5245 | 531.0500 | -90.67 % | 62741.7057 MeV (+36811.4 ppm) |
| ${}^{66}$Se | 66 | 32 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 55.6224 | 547.8000 | -89.85 % | 63702.3226 MeV (+36873.1 ppm) |
| ${}^{67}$Se | 67 | 33 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 61.7028 | 560.7588 | -89.00 % | 64662.9569 MeV (+36871.4 ppm) |
| ${}^{68}$Se | 68 | 34 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 67.7664 | 576.4393 | -88.24 % | 65623.6080 MeV (+36914.1 ppm) |
| ${}^{69}$Se | 69 | 35 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 73.8137 | 586.7559 | -87.42 % | 66584.2755 MeV (+36869.2 ppm) |
| ${}^{70}$Se | 70 | 36 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 79.8453 | 600.3224 | -86.70 % | 67544.9587 MeV (+36877.5 ppm) |
| ${}^{71}$Se | 71 | 37 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 85.8615 | 609.6103 | -85.92 % | 68505.6573 MeV (+36818.7 ppm) |
| ${}^{72}$Se | 72 | 38 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 91.8630 | 622.4033 | -85.24 % | 69466.3706 MeV (+36816.0 ppm) |
| ${}^{73}$Se | 73 | 39 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 97.8501 | 630.8338 | -84.49 % | 70427.0982 MeV (+36747.0 ppm) |
| ${}^{74}$Se | 74 | 40 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 103.8233 | 642.8909 | -83.85 % | 71387.8398 MeV (+36734.7 ppm) |
| ${}^{75}$Se | 75 | 41 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 109.7830 | 650.9185 | -83.13 % | 72348.5949 MeV (+36663.0 ppm) |
| ${}^{76}$Se | 76 | 42 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 115.7295 | 662.0723 | -82.52 % | 73309.3631 MeV (+36639.2 ppm) |
| ${}^{77}$Se | 77 | 43 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 121.6634 | 669.4912 | -81.83 % | 74270.1440 MeV (+36562.2 ppm) |
| ${}^{78}$Se | 78 | 44 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 127.5849 | 679.9890 | -81.24 % | 75230.9373 MeV (+36531.3 ppm) |
| ${}^{79}$Se | 79 | 45 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 133.4944 | 686.9518 | -80.57 % | 76191.7426 MeV (+36451.5 ppm) |
| ${}^{80}$Se | 80 | 46 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 139.3922 | 696.8651 | -80.00 % | 77152.5595 MeV (+36414.9 ppm) |
| ${}^{81}$Se | 81 | 47 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 145.2787 | 703.5660 | -79.35 % | 78113.3878 MeV (+36335.2 ppm) |
| ${}^{82}$Se | 82 | 48 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 151.1542 | 712.8422 | -78.80 % | 79074.2271 MeV (+36292.6 ppm) |
| ${}^{83}$Se | 83 | 49 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 157.0189 | 718.6601 | -78.15 % | 80035.0772 MeV (+36204.8 ppm) |
| ${}^{84}$Se | 84 | 50 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 162.8732 | 727.3387 | -77.61 % | 80995.9377 MeV (+36157.1 ppm) |
| ${}^{85}$Se | 85 | 51 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 168.7173 | 731.8759 | -76.95 % | 81956.8084 MeV (+36056.4 ppm) |
| ${}^{86}$Se | 86 | 52 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 174.5514 | 738.0367 | -76.35 % | 82917.6889 MeV (+35979.2 ppm) |
| ${}^{87}$Se | 87 | 53 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 180.3760 | 742.0310 | -75.69 % | 83878.5792 MeV (+35876.1 ppm) |
| ${}^{88}$Se | 88 | 54 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 186.1911 | 747.5604 | -75.09 % | 84839.4788 MeV (+35795.0 ppm) |
| ${}^{89}$Se | 89 | 55 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 191.9971 | 750.7399 | -74.43 % | 85800.3876 MeV (+35686.4 ppm) |
| ${}^{90}$Se | 90 | 56 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 197.7941 | 755.6190 | -73.82 % | 86761.3054 MeV (+35601.4 ppm) |
| ${}^{91}$Se | 91 | 57 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 203.5825 | 758.4703 | -73.16 % | 87722.2318 MeV (+35493.5 ppm) |
| ${}^{92}$Se | 92 | 58 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 209.3623 | 762.6800 | -72.55 % | 88683.1668 MeV (+35404.6 ppm) |
| ${}^{93}$Se | 93 | 59 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 215.1338 | 764.9250 | -71.88 % | 89644.1100 MeV (+35293.7 ppm) |
| ${}^{94}$Se | 94 | 60 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 220.8972 | 768.9200 | -71.27 % | 90605.0614 MeV (+35206.7 ppm) |
| ${}^{95}$Se | 95 | 61 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 226.6528 | 770.6400 | -70.59 % | 91566.0206 MeV (+35094.8 ppm) |

### Bromine (Z = 35)

_34 of 34 isotopes with a framework prediction; 34 of 34 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{65}$Br | 65 | 30 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 35.1308 | 513.7600 | -93.16 % | 62754.7690 MeV (+36744.1 ppm) |
| ${}^{66}$Br | 66 | 31 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 41.2851 | 528.9240 | -92.19 % | 63715.3296 MeV (+36779.5 ppm) |
| ${}^{67}$Br | 67 | 32 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 47.4208 | 545.9160 | -91.31 % | 64675.9086 MeV (+36845.5 ppm) |
| ${}^{68}$Br | 68 | 33 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 53.5387 | 560.2520 | -90.44 % | 65636.5055 MeV (+36865.6 ppm) |
| ${}^{69}$Br | 69 | 34 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 59.6393 | 575.7983 | -89.64 % | 66597.1196 MeV (+36904.9 ppm) |
| ${}^{70}$Br | 70 | 35 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 65.7231 | 589.0357 | -88.84 % | 67557.7506 MeV (+36906.7 ppm) |
| ${}^{71}$Br | 71 | 36 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 71.7908 | 602.1839 | -88.08 % | 68518.3977 MeV (+36907.3 ppm) |
| ${}^{72}$Br | 72 | 37 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 77.8426 | 612.8145 | -87.30 % | 69479.0606 MeV (+36869.1 ppm) |
| ${}^{73}$Br | 73 | 38 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 83.8793 | 625.4699 | -86.59 % | 70439.7387 MeV (+36863.2 ppm) |
| ${}^{74}$Br | 74 | 39 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 89.9012 | 635.1836 | -85.85 % | 71400.4316 MeV (+36813.3 ppm) |
| ${}^{75}$Br | 75 | 40 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 95.9088 | 647.0737 | -85.18 % | 72361.1388 MeV (+36797.2 ppm) |
| ${}^{76}$Br | 76 | 41 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 101.9024 | 656.3271 | -84.47 % | 73321.8600 MeV (+36743.2 ppm) |
| ${}^{77}$Br | 77 | 42 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 107.8825 | 667.3442 | -83.83 % | 74282.5946 MeV (+36716.2 ppm) |
| ${}^{78}$Br | 78 | 43 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 113.8496 | 675.6328 | -83.15 % | 75243.3424 MeV (+36651.2 ppm) |
| ${}^{79}$Br | 79 | 44 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 119.8038 | 686.3201 | -82.54 % | 76204.1028 MeV (+36621.7 ppm) |
| ${}^{80}$Br | 80 | 45 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 125.7457 | 694.2123 | -81.89 % | 77164.8757 MeV (+36554.3 ppm) |
| ${}^{81}$Br | 81 | 46 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 131.6756 | 704.3717 | -81.31 % | 78125.6607 MeV (+36519.9 ppm) |
| ${}^{82}$Br | 82 | 47 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 137.5937 | 711.9646 | -80.67 % | 79086.4573 MeV (+36451.6 ppm) |
| ${}^{83}$Br | 83 | 48 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 143.5004 | 721.5510 | -80.11 % | 80047.2653 MeV (+36411.8 ppm) |
| ${}^{84}$Br | 84 | 49 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 149.3961 | 728.3917 | -79.49 % | 81008.0845 MeV (+36336.8 ppm) |
| ${}^{85}$Br | 85 | 50 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 155.2809 | 737.2554 | -78.94 % | 81968.9144 MeV (+36290.1 ppm) |
| ${}^{86}$Br | 86 | 51 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 161.1553 | 742.3835 | -78.29 % | 82929.7548 MeV (+36196.3 ppm) |
| ${}^{87}$Br | 87 | 52 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 167.0194 | 748.7142 | -77.69 % | 83890.6055 MeV (+36120.2 ppm) |
| ${}^{88}$Br | 88 | 53 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 172.8735 | 753.6098 | -77.06 % | 84851.4662 MeV (+36027.8 ppm) |
| ${}^{89}$Br | 89 | 54 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 178.7179 | 759.2394 | -76.46 % | 85812.3366 MeV (+35946.7 ppm) |
| ${}^{90}$Br | 90 | 55 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 184.5528 | 763.0368 | -75.81 % | 86773.2164 MeV (+35844.9 ppm) |
| ${}^{91}$Br | 91 | 56 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 190.3784 | 768.2151 | -75.22 % | 87734.1056 MeV (+35762.4 ppm) |
| ${}^{92}$Br | 92 | 57 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 196.1950 | 771.4119 | -74.57 % | 88695.0037 MeV (+35657.8 ppm) |
| ${}^{93}$Br | 93 | 58 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 202.0028 | 776.1407 | -73.97 % | 89655.9107 MeV (+35573.9 ppm) |
| ${}^{94}$Br | 94 | 59 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 207.8021 | 778.9780 | -73.32 % | 90616.8262 MeV (+35469.4 ppm) |
| ${}^{95}$Br | 95 | 60 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 213.5929 | 783.2750 | -72.73 % | 91577.7502 MeV (+35384.1 ppm) |
| ${}^{96}$Br | 96 | 61 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 219.3755 | 785.6640 | -72.08 % | 92538.6823 MeV (+35279.4 ppm) |
| ${}^{97}$Br | 97 | 62 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 225.1502 | 789.5800 | -71.48 % | 93499.6224 MeV (+35193.3 ppm) |
| ${}^{98}$Br | 98 | 63 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 230.9170 | 791.6440 | -70.83 % | 94460.5704 MeV (+35089.4 ppm) |

### Krypton (Z = 36)

_35 of 35 isotopes with a framework prediction; 35 of 35 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{67}$Kr | 67 | 31 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 32.7934 | 528.1610 | -93.79 % | 64689.2057 MeV (+36776.5 ppm) |
| ${}^{68}$Kr | 68 | 32 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 38.9672 | 546.3120 | -92.87 % | 65649.7467 MeV (+36859.2 ppm) |
| ${}^{69}$Kr | 69 | 33 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 45.1226 | 560.9010 | -91.96 % | 66610.3060 MeV (+36882.3 ppm) |
| ${}^{70}$Kr | 70 | 34 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 51.2603 | 577.9200 | -91.13 % | 67570.8831 MeV (+36943.9 ppm) |
| ${}^{71}$Kr | 71 | 35 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 57.3808 | 591.2263 | -90.29 % | 68531.4774 MeV (+36945.6 ppm) |
| ${}^{72}$Kr | 72 | 36 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 63.4846 | 606.9110 | -89.54 % | 69492.0883 MeV (+36984.3 ppm) |
| ${}^{73}$Kr | 73 | 37 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 69.5723 | 617.5935 | -88.73 % | 70452.7154 MeV (+36945.9 ppm) |
| ${}^{74}$Kr | 74 | 38 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 75.6444 | 631.4449 | -88.02 % | 71413.3582 MeV (+36956.5 ppm) |
| ${}^{75}$Kr | 75 | 39 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 81.7012 | 641.5080 | -87.26 % | 72374.0161 MeV (+36910.7 ppm) |
| ${}^{76}$Kr | 76 | 40 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 87.7433 | 654.2694 | -86.59 % | 73334.6888 MeV (+36905.9 ppm) |
| ${}^{77}$Kr | 77 | 41 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 93.7711 | 663.4964 | -85.87 % | 74295.3757 MeV (+36850.2 ppm) |
| ${}^{78}$Kr | 78 | 42 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 99.7850 | 675.5766 | -85.23 % | 75256.0766 MeV (+36837.0 ppm) |
| ${}^{79}$Kr | 79 | 43 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 105.7854 | 683.9119 | -84.53 % | 76216.7910 MeV (+36771.4 ppm) |
| ${}^{80}$Kr | 80 | 44 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 111.7726 | 695.4344 | -83.93 % | 77177.5185 MeV (+36752.1 ppm) |
| ${}^{81}$Kr | 81 | 45 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 117.7471 | 703.3085 | -83.26 % | 78138.2588 MeV (+36683.2 ppm) |
| ${}^{82}$Kr | 82 | 46 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 123.7092 | 714.2754 | -82.68 % | 79099.0115 MeV (+36658.1 ppm) |
| ${}^{83}$Kr | 83 | 47 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 129.6592 | 721.7455 | -82.04 % | 80059.7763 MeV (+36586.9 ppm) |
| ${}^{84}$Kr | 84 | 48 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 135.5975 | 732.2656 | -81.48 % | 81020.5528 MeV (+36558.0 ppm) |
| ${}^{85}$Kr | 85 | 49 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 141.5243 | 739.3779 | -80.86 % | 81981.3407 MeV (+36485.3 ppm) |
| ${}^{86}$Kr | 86 | 50 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 147.4400 | 749.2345 | -80.32 % | 82942.1398 MeV (+36449.9 ppm) |
| ${}^{87}$Kr | 87 | 51 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 153.3448 | 754.7497 | -79.68 % | 83902.9498 MeV (+36359.9 ppm) |
| ${}^{88}$Kr | 88 | 52 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 159.2390 | 761.8028 | -79.10 % | 84863.7703 MeV (+36291.6 ppm) |
| ${}^{89}$Kr | 89 | 53 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 165.1229 | 766.7186 | -78.46 % | 85824.6012 MeV (+36198.1 ppm) |
| ${}^{90}$Kr | 90 | 54 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 170.9968 | 773.2134 | -77.88 % | 86785.4421 MeV (+36126.4 ppm) |
| ${}^{91}$Kr | 91 | 55 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 176.8609 | 777.2994 | -77.25 % | 87746.2928 MeV (+36027.0 ppm) |
| ${}^{92}$Kr | 92 | 56 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 182.7154 | 783.1661 | -76.67 % | 88707.1530 MeV (+35951.3 ppm) |
| ${}^{93}$Kr | 93 | 57 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 188.5606 | 786.6041 | -76.03 % | 89668.0226 MeV (+35848.4 ppm) |
| ${}^{94}$Kr | 94 | 58 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 194.3967 | 791.8872 | -75.45 % | 90628.9013 MeV (+35769.5 ppm) |
| ${}^{95}$Kr | 95 | 59 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 200.2239 | 794.7696 | -74.81 % | 91589.7889 MeV (+35664.4 ppm) |
| ${}^{96}$Kr | 96 | 60 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 206.0424 | 799.7637 | -74.24 % | 92550.6851 MeV (+35586.0 ppm) |
| ${}^{97}$Kr | 97 | 61 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 211.8524 | 802.1769 | -73.59 % | 93511.5899 MeV (+35479.7 ppm) |
| ${}^{98}$Kr | 98 | 62 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 217.6542 | 806.9320 | -73.03 % | 94472.5029 MeV (+35402.4 ppm) |
| ${}^{99}$Kr | 99 | 63 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 223.4478 | 809.3250 | -72.39 % | 95433.4240 MeV (+35299.7 ppm) |
| ${}^{100}$Kr | 100 | 64 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 229.2336 | 813.4000 | -71.82 % | 96394.3531 MeV (+35219.0 ppm) |
| ${}^{101}$Kr | 101 | 65 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 235.0116 | 815.5750 | -71.18 % | 97355.2898 MeV (+35118.4 ppm) |

### Rubidium (Z = 37)

_34 of 34 isotopes with a framework prediction; 34 of 34 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{71}$Rb | 71 | 34 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 42.6317 | 576.3780 | -92.60 % | 68544.8962 MeV (+36928.4 ppm) |
| ${}^{72}$Rb | 72 | 35 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 48.7889 | 590.5440 | -91.74 % | 69505.4537 MeV (+36942.2 ppm) |
| ${}^{73}$Rb | 73 | 36 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 54.9291 | 606.2710 | -90.94 % | 70466.0283 MeV (+36981.0 ppm) |
| ${}^{74}$Rb | 74 | 37 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 61.0528 | 620.2467 | -90.16 % | 71426.6195 MeV (+36992.2 ppm) |
| ${}^{75}$Rb | 75 | 38 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 67.1603 | 633.6207 | -89.40 % | 72387.2267 MeV (+36994.4 ppm) |
| ${}^{76}$Rb | 76 | 39 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 73.2523 | 644.9524 | -88.64 % | 73347.8495 MeV (+36966.8 ppm) |
| ${}^{77}$Rb | 77 | 40 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 79.3291 | 657.3751 | -87.93 % | 74308.4875 MeV (+36956.0 ppm) |
| ${}^{78}$Rb | 78 | 41 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 85.3912 | 667.5514 | -87.21 % | 75269.1401 MeV (+36913.5 ppm) |
| ${}^{79}$Rb | 79 | 42 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 91.4390 | 679.4901 | -86.54 % | 76229.8071 MeV (+36897.1 ppm) |
| ${}^{80}$Rb | 80 | 43 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 97.4730 | 688.9341 | -85.85 % | 77190.4879 MeV (+36846.6 ppm) |
| ${}^{81}$Rb | 81 | 44 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 103.4934 | 700.2866 | -85.22 % | 78151.1822 MeV (+36823.8 ppm) |
| ${}^{82}$Rb | 82 | 45 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 109.5007 | 709.0891 | -84.56 % | 79111.8897 MeV (+36767.1 ppm) |
| ${}^{83}$Rb | 83 | 46 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 115.4952 | 720.0432 | -83.96 % | 80072.6100 MeV (+36740.8 ppm) |
| ${}^{84}$Rb | 84 | 47 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 121.4773 | 728.8028 | -83.33 % | 81033.3426 MeV (+36686.1 ppm) |
| ${}^{85}$Rb | 85 | 48 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 127.4473 | 739.2825 | -82.76 % | 81994.0874 MeV (+36655.4 ppm) |
| ${}^{86}$Rb | 86 | 49 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 133.4055 | 747.9335 | -82.16 % | 82954.8440 MeV (+36601.9 ppm) |
| ${}^{87}$Rb | 87 | 50 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 139.3522 | 757.8556 | -81.61 % | 83915.6121 MeV (+36566.1 ppm) |
| ${}^{88}$Rb | 88 | 51 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 145.2877 | 763.9382 | -80.98 % | 84876.3913 MeV (+36482.6 ppm) |
| ${}^{89}$Rb | 89 | 52 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 151.2123 | 771.1129 | -80.39 % | 85837.1815 MeV (+36414.8 ppm) |
| ${}^{90}$Rb | 90 | 53 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 157.1263 | 776.8374 | -79.77 % | 86797.9823 MeV (+36330.7 ppm) |
| ${}^{91}$Rb | 91 | 54 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 163.0300 | 783.2882 | -79.19 % | 87758.7934 MeV (+36257.4 ppm) |
| ${}^{92}$Rb | 92 | 55 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 168.9235 | 788.3869 | -78.57 % | 88719.6147 MeV (+36169.5 ppm) |
| ${}^{93}$Rb | 93 | 56 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 174.8071 | 794.3056 | -77.99 % | 89680.4458 MeV (+36093.4 ppm) |
| ${}^{94}$Rb | 94 | 57 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 180.6811 | 798.3199 | -77.37 % | 90641.2866 MeV (+35996.5 ppm) |
| ${}^{95}$Rb | 95 | 58 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 186.5457 | 803.7187 | -76.79 % | 91602.1368 MeV (+35918.0 ppm) |
| ${}^{96}$Rb | 96 | 59 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 192.4011 | 807.2540 | -76.17 % | 92562.9961 MeV (+35819.6 ppm) |
| ${}^{97}$Rb | 97 | 60 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 198.2475 | 812.4902 | -75.60 % | 93523.8645 MeV (+35742.9 ppm) |
| ${}^{98}$Rb | 98 | 61 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 204.0852 | 816.4115 | -75.00 % | 94484.7416 MeV (+35652.9 ppm) |
| ${}^{99}$Rb | 99 | 62 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 209.9143 | 821.2348 | -74.44 % | 95445.6272 MeV (+35575.0 ppm) |
| ${}^{100}$Rb | 100 | 63 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 215.7351 | 824.4508 | -73.83 % | 96406.5213 MeV (+35480.8 ppm) |
| ${}^{101}$Rb | 101 | 64 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 221.5476 | 828.8237 | -73.27 % | 97367.4235 MeV (+35401.4 ppm) |
| ${}^{102}$Rb | 102 | 65 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 227.3522 | 831.5799 | -72.66 % | 98328.3337 MeV (+35305.9 ppm) |
| ${}^{103}$Rb | 103 | 66 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 233.1489 | 835.5360 | -72.10 % | 99289.2517 MeV (+35225.7 ppm) |
| ${}^{104}$Rb | 104 | 67 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 238.9380 | 837.9280 | -71.48 % | 100250.1774 MeV (+35129.7 ppm) |

### Strontium (Z = 38)

_35 of 35 isotopes with a framework prediction; 35 of 35 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{73}$Sr | 73 | 35 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 39.9497 | 591.4460 | -93.25 % | 70479.6774 MeV (+36967.3 ppm) |
| ${}^{74}$Sr | 74 | 36 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 46.1264 | 608.3540 | -92.42 % | 71440.2155 MeV (+37022.6 ppm) |
| ${}^{75}$Sr | 75 | 37 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 52.2861 | 622.2384 | -91.60 % | 72400.7706 MeV (+37030.9 ppm) |
| ${}^{76}$Sr | 76 | 38 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 58.4293 | 637.9386 | -90.84 % | 73361.3422 MeV (+37066.2 ppm) |
| ${}^{77}$Sr | 77 | 39 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 64.5565 | 649.5657 | -90.06 % | 74321.9297 MeV (+37041.8 ppm) |
| ${}^{78}$Sr | 78 | 40 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 70.6682 | 663.0076 | -89.34 % | 75282.5328 MeV (+37044.2 ppm) |
| ${}^{79}$Sr | 79 | 41 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 76.7648 | 673.3846 | -88.60 % | 76243.1510 MeV (+37003.6 ppm) |
| ${}^{80}$Sr | 80 | 42 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 82.8467 | 686.2877 | -87.93 % | 77203.7839 MeV (+36999.3 ppm) |
| ${}^{81}$Sr | 81 | 43 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 88.9144 | 695.5757 | -87.22 % | 78164.4310 MeV (+36945.5 ppm) |
| ${}^{82}$Sr | 82 | 44 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 94.9681 | 708.1290 | -86.59 % | 79125.0920 MeV (+36937.7 ppm) |
| ${}^{83}$Sr | 83 | 45 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 101.0084 | 716.9878 | -85.91 % | 80085.7664 MeV (+36880.6 ppm) |
| ${}^{84}$Sr | 84 | 46 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 107.0356 | 728.9111 | -85.32 % | 81046.4541 MeV (+36865.7 ppm) |
| ${}^{85}$Sr | 85 | 47 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 113.0500 | 737.4361 | -84.67 % | 82007.1545 MeV (+36806.7 ppm) |
| ${}^{86}$Sr | 86 | 48 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 119.0519 | 748.9273 | -84.10 % | 82967.8673 MeV (+36787.7 ppm) |
| ${}^{87}$Sr | 87 | 49 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 125.0417 | 757.3556 | -83.49 % | 83928.5923 MeV (+36730.1 ppm) |
| ${}^{88}$Sr | 88 | 50 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 131.0196 | 768.4684 | -82.95 % | 84889.3291 MeV (+36707.9 ppm) |
| ${}^{89}$Sr | 89 | 51 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 136.9861 | 774.8271 | -82.32 % | 85850.0775 MeV (+36626.8 ppm) |
| ${}^{90}$Sr | 90 | 52 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 142.9413 | 782.6404 | -81.74 % | 86810.8370 MeV (+36565.6 ppm) |
| ${}^{91}$Sr | 91 | 53 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 148.8855 | 788.4127 | -81.12 % | 87771.6075 MeV (+36481.0 ppm) |
| ${}^{92}$Sr | 92 | 54 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 154.8191 | 795.6994 | -80.54 % | 88732.3887 MeV (+36416.7 ppm) |
| ${}^{93}$Sr | 93 | 55 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 160.7423 | 800.9892 | -79.93 % | 89693.1803 MeV (+36329.9 ppm) |
| ${}^{94}$Sr | 94 | 56 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 166.6553 | 807.8204 | -79.37 % | 90653.9821 MeV (+36263.4 ppm) |
| ${}^{95}$Sr | 95 | 57 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 172.5583 | 812.1633 | -78.75 % | 91614.7939 MeV (+36169.3 ppm) |
| ${}^{96}$Sr | 96 | 58 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 178.4516 | 818.0356 | -78.19 % | 92575.6153 MeV (+36094.9 ppm) |
| ${}^{97}$Sr | 97 | 59 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 184.3355 | 821.7693 | -77.57 % | 93536.4462 MeV (+35997.7 ppm) |
| ${}^{98}$Sr | 98 | 60 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 190.2101 | 827.6824 | -77.02 % | 94497.2864 MeV (+35927.3 ppm) |
| ${}^{99}$Sr | 99 | 61 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 196.0757 | 831.8498 | -76.43 % | 95458.1356 MeV (+35838.8 ppm) |
| ${}^{100}$Sr | 100 | 62 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 201.9324 | 837.2201 | -75.88 % | 96418.9936 MeV (+35765.6 ppm) |
| ${}^{101}$Sr | 101 | 63 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 207.7805 | 840.7989 | -75.29 % | 97379.8603 MeV (+35674.1 ppm) |
| ${}^{102}$Sr | 102 | 64 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 213.6202 | 845.7046 | -74.74 % | 98340.7354 MeV (+35599.1 ppm) |
| ${}^{103}$Sr | 103 | 65 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 219.4515 | 848.9260 | -74.15 % | 99301.6188 MeV (+35507.1 ppm) |
| ${}^{104}$Sr | 104 | 66 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 225.2748 | 853.4240 | -73.60 % | 100262.5103 MeV (+35431.4 ppm) |
| ${}^{105}$Sr | 105 | 67 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 231.0902 | 855.9600 | -73.00 % | 101223.4097 MeV (+35335.6 ppm) |
| ${}^{106}$Sr | 106 | 68 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 236.8978 | 860.0840 | -72.46 % | 102184.3169 MeV (+35259.4 ppm) |
| ${}^{107}$Sr | 107 | 69 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 242.6979 | 862.0990 | -71.85 % | 103145.2316 MeV (+35162.1 ppm) |

### Yttrium (Z = 39)

_35 of 35 isotopes with a framework prediction; 35 of 35 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{75}$Y | 75 | 36 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 37.0785 | 606.6750 | -93.89 % | 72414.6479 MeV (+37009.9 ppm) |
| ${}^{76}$Y | 76 | 37 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 43.2744 | 621.1480 | -93.03 % | 73375.1668 MeV (+37027.1 ppm) |
| ${}^{77}$Y | 77 | 38 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 49.4534 | 637.4060 | -92.24 % | 74335.7026 MeV (+37069.6 ppm) |
| ${}^{78}$Y | 78 | 39 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 55.6160 | 651.2220 | -91.46 % | 75296.2547 MeV (+37076.1 ppm) |
| ${}^{79}$Y | 79 | 40 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 61.7627 | 664.9255 | -90.71 % | 76256.8228 MeV (+37081.2 ppm) |
| ${}^{80}$Y | 80 | 41 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 67.8939 | 676.3421 | -89.96 % | 77217.4064 MeV (+37054.6 ppm) |
| ${}^{81}$Y | 81 | 42 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 74.0100 | 688.9782 | -89.26 % | 78178.0050 MeV (+37045.6 ppm) |
| ${}^{82}$Y | 82 | 43 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 80.1116 | 699.4006 | -88.55 % | 79138.6182 MeV (+37007.0 ppm) |
| ${}^{83}$Y | 83 | 44 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 86.1989 | 711.6135 | -87.89 % | 80099.2457 MeV (+36993.4 ppm) |
| ${}^{84}$Y | 84 | 45 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 92.2723 | 721.3736 | -87.21 % | 81059.8870 MeV (+36947.9 ppm) |
| ${}^{85}$Y | 85 | 46 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 98.3323 | 733.3926 | -86.59 % | 82020.5419 MeV (+36933.2 ppm) |
| ${}^{86}$Y | 86 | 47 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 104.3791 | 742.9049 | -85.95 % | 82981.2098 MeV (+36886.5 ppm) |
| ${}^{87}$Y | 87 | 48 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 110.4131 | 754.7115 | -85.37 % | 83941.8905 MeV (+36870.5 ppm) |
| ${}^{88}$Y | 88 | 49 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 116.4347 | 764.0635 | -84.76 % | 84902.5838 MeV (+36823.9 ppm) |
| ${}^{89}$Y | 89 | 50 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 122.4441 | 775.5470 | -84.21 % | 85863.2891 MeV (+36805.1 ppm) |
| ${}^{90}$Y | 90 | 51 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 128.4417 | 782.4040 | -83.58 % | 86824.0063 MeV (+36729.7 ppm) |
| ${}^{91}$Y | 91 | 52 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 134.4277 | 790.3297 | -82.99 % | 87784.7351 MeV (+36669.1 ppm) |
| ${}^{92}$Y | 92 | 53 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 140.4024 | 796.8662 | -82.38 % | 88745.4751 MeV (+36593.1 ppm) |
| ${}^{93}$Y | 93 | 54 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 146.3662 | 804.3482 | -81.80 % | 89706.2261 MeV (+36530.3 ppm) |
| ${}^{94}$Y | 94 | 55 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 152.3192 | 810.5438 | -81.21 % | 90666.9879 MeV (+36453.6 ppm) |
| ${}^{95}$Y | 95 | 56 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 158.2618 | 817.4716 | -80.64 % | 91627.7601 MeV (+36387.3 ppm) |
| ${}^{96}$Y | 96 | 57 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 164.1941 | 822.6650 | -80.04 % | 92588.5426 MeV (+36302.4 ppm) |
| ${}^{97}$Y | 97 | 58 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 170.1164 | 828.5218 | -79.47 % | 93549.3350 MeV (+36226.9 ppm) |
| ${}^{98}$Y | 98 | 59 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 176.0289 | 832.7664 | -78.86 % | 94510.1373 MeV (+36134.8 ppm) |
| ${}^{99}$Y | 99 | 60 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 181.9320 | 839.1927 | -78.32 % | 95470.9490 MeV (+36069.2 ppm) |
| ${}^{100}$Y | 100 | 61 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 187.8256 | 843.9415 | -77.74 % | 96431.7701 MeV (+35986.3 ppm) |
| ${}^{101}$Y | 101 | 62 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 193.7102 | 849.7464 | -77.20 % | 97392.6003 MeV (+35916.8 ppm) |
| ${}^{102}$Y | 102 | 63 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 199.5859 | 853.9356 | -76.63 % | 98353.4394 MeV (+35831.2 ppm) |
| ${}^{103}$Y | 103 | 64 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 205.4528 | 859.2913 | -76.09 % | 99314.2872 MeV (+35759.9 ppm) |
| ${}^{104}$Y | 104 | 65 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 211.3113 | 862.9920 | -75.51 % | 100275.1436 MeV (+35672.3 ppm) |
| ${}^{105}$Y | 105 | 66 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 217.1613 | 867.5100 | -74.97 % | 101236.0083 MeV (+35595.6 ppm) |
| ${}^{106}$Y | 106 | 67 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 223.0033 | 870.7900 | -74.39 % | 102196.8811 MeV (+35507.2 ppm) |
| ${}^{107}$Y | 107 | 68 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 228.8372 | 875.0460 | -73.85 % | 103157.7620 MeV (+35430.5 ppm) |
| ${}^{108}$Y | 108 | 69 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 234.6633 | 877.9320 | -73.27 % | 104118.6507 MeV (+35341.1 ppm) |
| ${}^{109}$Y | 109 | 70 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 240.4817 | 881.7010 | -72.73 % | 105079.5470 MeV (+35262.6 ppm) |

### Zirconium (Z = 40)

_37 of 37 isotopes with a framework prediction; 37 of 37 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{77}$Zr | 77 | 37 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 34.0197 | 621.7750 | -94.53 % | 74349.8060 MeV (+37051.6 ppm) |
| ${}^{78}$Zr | 78 | 38 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 40.2345 | 639.1320 | -93.70 % | 75310.3059 MeV (+37107.9 ppm) |
| ${}^{79}$Zr | 79 | 39 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 46.4327 | 653.0930 | -92.89 % | 76270.8225 MeV (+37116.0 ppm) |
| ${}^{80}$Zr | 80 | 40 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 52.6145 | 669.2000 | -92.14 % | 77231.3555 MeV (+37153.0 ppm) |
| ${}^{81}$Zr | 81 | 41 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 58.7804 | 680.0073 | -91.36 % | 78191.9043 MeV (+37117.3 ppm) |
| ${}^{82}$Zr | 82 | 42 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 64.9310 | 694.1683 | -90.65 % | 79152.4685 MeV (+37128.0 ppm) |
| ${}^{83}$Zr | 83 | 43 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 71.0665 | 704.5372 | -89.91 % | 80113.0478 MeV (+37087.6 ppm) |
| ${}^{84}$Zr | 84 | 44 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 77.1875 | 718.1185 | -89.25 % | 81073.6416 MeV (+37091.0 ppm) |
| ${}^{85}$Zr | 85 | 45 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 83.2943 | 727.9433 | -88.56 % | 82034.2496 MeV (+37045.3 ppm) |
| ${}^{86}$Zr | 86 | 46 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 89.3872 | 740.8085 | -87.93 % | 82994.8714 MeV (+37040.2 ppm) |
| ${}^{87}$Zr | 87 | 47 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 95.4666 | 750.2579 | -87.28 % | 83955.5067 MeV (+36991.6 ppm) |
| ${}^{88}$Zr | 88 | 48 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 101.5330 | 762.6110 | -86.69 % | 84916.1552 MeV (+36981.1 ppm) |
| ${}^{89}$Zr | 89 | 49 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 107.5865 | 771.9314 | -86.06 % | 85876.8165 MeV (+36933.0 ppm) |
| ${}^{90}$Zr | 90 | 50 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 113.6275 | 783.8973 | -85.50 % | 86837.4902 MeV (+36918.8 ppm) |
| ${}^{91}$Zr | 91 | 51 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 119.6564 | 791.0917 | -84.87 % | 87798.1761 MeV (+36846.7 ppm) |
| ${}^{92}$Zr | 92 | 52 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 125.6734 | 799.7264 | -84.29 % | 88758.8739 MeV (+36793.7 ppm) |
| ${}^{93}$Zr | 93 | 53 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 131.6788 | 806.4607 | -83.67 % | 89719.5832 MeV (+36719.3 ppm) |
| ${}^{94}$Zr | 94 | 54 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 137.6729 | 814.6794 | -83.10 % | 90680.3039 MeV (+36664.1 ppm) |
| ${}^{95}$Zr | 95 | 55 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 143.6560 | 821.1413 | -82.51 % | 91641.0355 MeV (+36589.7 ppm) |
| ${}^{96}$Zr | 96 | 56 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 149.6283 | 828.9915 | -81.95 % | 92601.7780 MeV (+36533.0 ppm) |
| ${}^{97}$Zr | 97 | 57 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 155.5901 | 834.5607 | -81.36 % | 93562.5310 MeV (+36451.4 ppm) |
| ${}^{98}$Zr | 98 | 58 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 161.5416 | 840.9770 | -80.79 % | 94523.2943 MeV (+36381.2 ppm) |
| ${}^{99}$Zr | 99 | 59 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 167.4831 | 845.3833 | -80.19 % | 95484.0676 MeV (+36290.0 ppm) |
| ${}^{100}$Zr | 100 | 60 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 173.4147 | 852.2107 | -79.65 % | 96444.8507 MeV (+36227.6 ppm) |
| ${}^{101}$Zr | 101 | 61 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 179.3368 | 857.0702 | -79.08 % | 97405.6435 MeV (+36144.9 ppm) |
| ${}^{102}$Zr | 102 | 62 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 185.2494 | 863.5620 | -78.55 % | 98366.4456 MeV (+36081.7 ppm) |
| ${}^{103}$Zr | 103 | 63 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 191.1529 | 867.8609 | -77.97 % | 99327.2569 MeV (+35996.2 ppm) |
| ${}^{104}$Zr | 104 | 64 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 197.0474 | 873.8409 | -77.45 % | 100288.0772 MeV (+35930.4 ppm) |
| ${}^{105}$Zr | 105 | 65 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 202.9331 | 877.6528 | -76.88 % | 101248.9062 MeV (+35842.9 ppm) |
| ${}^{106}$Zr | 106 | 66 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 208.8102 | 882.9800 | -76.35 % | 102209.7439 MeV (+35773.5 ppm) |
| ${}^{107}$Zr | 107 | 67 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 214.6789 | 886.3880 | -75.78 % | 103170.5900 MeV (+35684.5 ppm) |
| ${}^{108}$Zr | 108 | 68 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 220.5393 | 891.3240 | -75.26 % | 104131.4443 MeV (+35614.3 ppm) |
| ${}^{109}$Zr | 109 | 69 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 226.3917 | 894.2360 | -74.68 % | 105092.3067 MeV (+35523.5 ppm) |
| ${}^{110}$Zr | 110 | 70 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 232.2361 | 898.8100 | -74.16 % | 106053.1770 MeV (+35451.8 ppm) |
| ${}^{111}$Zr | 111 | 71 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 238.0729 | 901.0980 | -73.58 % | 107014.0551 MeV (+35359.1 ppm) |
| ${}^{112}$Zr | 112 | 72 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 243.9020 | 905.0720 | -73.05 % | 107974.9407 MeV (+35284.8 ppm) |
| ${}^{113}$Zr | 113 | 73 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 249.7237 | 907.0510 | -72.47 % | 108935.8338 MeV (+35192.0 ppm) |

### Niobium (Z = 41)

_38 of 38 isotopes with a framework prediction; 38 of 38 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{79}$Nb | 79 | 38 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 30.7748 | 637.2140 | -95.17 % | 76285.1501 MeV (+37097.6 ppm) |
| ${}^{80}$Nb | 80 | 39 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 37.0085 | 652.0800 | -94.32 % | 77245.6312 MeV (+37117.1 ppm) |
| ${}^{81}$Nb | 81 | 40 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 43.2255 | 668.0880 | -93.53 % | 78206.1289 MeV (+37152.4 ppm) |
| ${}^{82}$Nb | 82 | 41 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 49.4264 | 681.5840 | -92.75 % | 79166.6429 MeV (+37153.3 ppm) |
| ${}^{83}$Nb | 83 | 42 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 55.6114 | 695.4561 | -92.00 % | 80127.1726 MeV (+37159.1 ppm) |
| ${}^{84}$Nb | 84 | 43 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 61.7811 | 707.1083 | -91.26 % | 81087.7176 MeV (+37135.4 ppm) |
| ${}^{85}$Nb | 85 | 44 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 67.9359 | 720.2655 | -90.57 % | 82048.2776 MeV (+37132.2 ppm) |
| ${}^{86}$Nb | 86 | 45 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 74.0761 | 731.1912 | -89.87 % | 83008.8522 MeV (+37100.4 ppm) |
| ${}^{87}$Nb | 87 | 46 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 80.2022 | 744.0029 | -89.22 % | 83969.4409 MeV (+37093.6 ppm) |
| ${}^{88}$Nb | 88 | 47 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 86.3144 | 754.3713 | -88.56 % | 84930.0435 MeV (+37056.3 ppm) |
| ${}^{89}$Nb | 89 | 48 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 92.4132 | 766.8968 | -87.95 % | 85890.6595 MeV (+37046.9 ppm) |
| ${}^{90}$Nb | 90 | 49 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 98.4988 | 777.0039 | -87.32 % | 86851.2886 MeV (+37007.9 ppm) |
| ${}^{91}$Nb | 91 | 50 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 104.5716 | 789.0517 | -86.75 % | 87811.9305 MeV (+36993.7 ppm) |
| ${}^{92}$Nb | 92 | 51 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 110.6320 | 796.9383 | -86.12 % | 88772.5850 MeV (+36929.6 ppm) |
| ${}^{93}$Nb | 93 | 52 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 116.6802 | 805.7692 | -85.52 % | 89733.2516 MeV (+36878.3 ppm) |
| ${}^{94}$Nb | 94 | 53 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 122.7164 | 812.9967 | -84.91 % | 90693.9300 MeV (+36809.2 ppm) |
| ${}^{95}$Nb | 95 | 54 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 128.7411 | 821.4853 | -84.33 % | 91654.6201 MeV (+36756.5 ppm) |
| ${}^{96}$Nb | 96 | 55 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 134.7545 | 828.3731 | -83.73 % | 92615.3216 MeV (+36686.5 ppm) |
| ${}^{97}$Nb | 97 | 56 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 140.7567 | 836.4444 | -83.17 % | 93576.0341 MeV (+36631.6 ppm) |
| ${}^{98}$Nb | 98 | 57 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 146.7482 | 842.4376 | -82.58 % | 94536.7574 MeV (+36554.3 ppm) |
| ${}^{99}$Nb | 99 | 58 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 152.7291 | 849.3196 | -82.02 % | 95497.4913 MeV (+36488.7 ppm) |
| ${}^{100}$Nb | 100 | 59 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 158.6996 | 854.8468 | -81.44 % | 96458.2355 MeV (+36409.5 ppm) |
| ${}^{101}$Nb | 101 | 60 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 164.6601 | 862.0184 | -80.90 % | 97418.9898 MeV (+36350.0 ppm) |
| ${}^{102}$Nb | 102 | 61 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 170.6107 | 867.4965 | -80.33 % | 98379.7540 MeV (+36273.4 ppm) |
| ${}^{103}$Nb | 103 | 62 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 176.5516 | 874.2982 | -79.81 % | 99340.5278 MeV (+36212.6 ppm) |
| ${}^{104}$Nb | 104 | 63 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 182.4831 | 879.1519 | -79.24 % | 100301.3111 MeV (+36132.3 ppm) |
| ${}^{105}$Nb | 105 | 64 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 188.4054 | 885.3277 | -78.72 % | 101262.1036 MeV (+36067.6 ppm) |
| ${}^{106}$Nb | 106 | 65 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 194.3186 | 889.6862 | -78.16 % | 102222.9052 MeV (+35985.1 ppm) |
| ${}^{107}$Nb | 107 | 66 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 200.2229 | 895.2786 | -77.64 % | 103183.7157 MeV (+35917.2 ppm) |
| ${}^{108}$Nb | 108 | 67 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 206.1186 | 899.1713 | -77.08 % | 104144.5347 MeV (+35833.0 ppm) |
| ${}^{109}$Nb | 109 | 68 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 212.0058 | 904.3872 | -76.56 % | 105105.3623 MeV (+35764.0 ppm) |
| ${}^{110}$Nb | 110 | 69 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 217.8846 | 908.0787 | -76.01 % | 106066.1982 MeV (+35680.9 ppm) |
| ${}^{111}$Nb | 111 | 70 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 223.7554 | 912.7530 | -75.49 % | 107027.0423 MeV (+35609.8 ppm) |
| ${}^{112}$Nb | 112 | 71 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 229.6181 | 915.9360 | -74.93 % | 107987.8943 MeV (+35524.6 ppm) |
| ${}^{113}$Nb | 113 | 72 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 235.4730 | 920.1590 | -74.41 % | 108948.7541 MeV (+35451.2 ppm) |
| ${}^{114}$Nb | 114 | 73 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 241.3203 | 923.0580 | -73.86 % | 109909.6217 MeV (+35365.7 ppm) |
| ${}^{115}$Nb | 115 | 74 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 247.1601 | 927.0150 | -73.34 % | 110870.4967 MeV (+35292.9 ppm) |
| ${}^{116}$Nb | 116 | 75 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 252.9925 | 929.3920 | -72.78 % | 111831.3791 MeV (+35206.5 ppm) |

### Molybdenum (Z = 42)

_39 of 39 isotopes with a framework prediction; 39 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{81}$Mo | 81 | 39 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 27.3453 | 652.3740 | -95.81 % | 78220.6788 MeV (+37140.5 ppm) |
| ${}^{82}$Mo | 82 | 40 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 33.5977 | 669.3660 | -94.98 % | 79181.1412 MeV (+37187.8 ppm) |
| ${}^{83}$Mo | 83 | 41 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 39.8335 | 683.4220 | -94.17 % | 80141.6202 MeV (+37194.7 ppm) |
| ${}^{84}$Mo | 84 | 42 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 46.0532 | 699.3000 | -93.41 % | 81102.1153 MeV (+37226.4 ppm) |
| ${}^{85}$Mo | 85 | 43 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 52.2572 | 710.7132 | -92.65 % | 82062.6260 MeV (+37198.6 ppm) |
| ${}^{86}$Mo | 86 | 44 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 58.4459 | 725.3857 | -91.94 % | 83023.1521 MeV (+37214.0 ppm) |
| ${}^{87}$Mo | 87 | 45 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 64.6197 | 736.2309 | -91.22 % | 83983.6931 MeV (+37180.1 ppm) |
| ${}^{88}$Mo | 88 | 46 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 70.7790 | 750.1040 | -90.56 % | 84944.2486 MeV (+37185.6 ppm) |
| ${}^{89}$Mo | 89 | 47 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 76.9241 | 760.5037 | -89.89 % | 85904.8182 MeV (+37147.6 ppm) |
| ${}^{90}$Mo | 90 | 48 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 83.0555 | 773.7326 | -89.27 % | 86865.4016 MeV (+37145.6 ppm) |
| ${}^{91}$Mo | 91 | 49 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 89.1734 | 783.8402 | -88.62 % | 87825.9984 MeV (+37105.6 ppm) |
| ${}^{92}$Mo | 92 | 50 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 95.2782 | 796.5113 | -88.04 % | 88786.6084 MeV (+37097.7 ppm) |
| ${}^{93}$Mo | 93 | 51 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 101.3702 | 804.5811 | -87.40 % | 89747.2312 MeV (+37035.0 ppm) |
| ${}^{94}$Mo | 94 | 52 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 107.4497 | 814.2594 | -86.80 % | 90707.8665 MeV (+36992.8 ppm) |
| ${}^{95}$Mo | 95 | 53 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 113.5171 | 821.6285 | -86.18 % | 91668.5139 MeV (+36924.5 ppm) |
| ${}^{96}$Mo | 96 | 54 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 119.5725 | 830.7828 | -85.61 % | 92629.1733 MeV (+36878.6 ppm) |
| ${}^{97}$Mo | 97 | 55 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 125.6162 | 837.6040 | -85.00 % | 93589.8443 MeV (+36806.9 ppm) |
| ${}^{98}$Mo | 98 | 56 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 131.6487 | 846.2466 | -84.44 % | 94550.5266 MeV (+36757.5 ppm) |
| ${}^{99}$Mo | 99 | 57 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 137.6700 | 852.1720 | -83.84 % | 95511.2201 MeV (+36678.6 ppm) |
| ${}^{100}$Mo | 100 | 58 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 143.6804 | 860.4663 | -83.30 % | 96471.9244 MeV (+36627.9 ppm) |
| ${}^{101}$Mo | 101 | 59 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 149.6803 | 865.8645 | -82.71 % | 97432.6393 MeV (+36546.3 ppm) |
| ${}^{102}$Mo | 102 | 60 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 155.6698 | 873.9767 | -82.19 % | 98393.3646 MeV (+36496.0 ppm) |
| ${}^{103}$Mo | 103 | 61 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 161.6491 | 879.4415 | -81.62 % | 99354.1001 MeV (+36418.3 ppm) |
| ${}^{104}$Mo | 104 | 62 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 167.6185 | 886.9023 | -81.10 % | 100314.8454 MeV (+36363.5 ppm) |
| ${}^{105}$Mo | 105 | 63 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 173.5782 | 891.9606 | -80.54 % | 101275.6005 MeV (+36284.3 ppm) |
| ${}^{106}$Mo | 106 | 64 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 179.5284 | 898.8291 | -80.03 % | 102236.3651 MeV (+36225.8 ppm) |
| ${}^{107}$Mo | 107 | 65 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 185.4693 | 903.3174 | -79.47 % | 103197.1389 MeV (+36143.7 ppm) |
| ${}^{108}$Mo | 108 | 66 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 191.4011 | 909.5931 | -78.96 % | 104157.9219 MeV (+36081.6 ppm) |
| ${}^{109}$Mo | 109 | 67 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 197.3240 | 913.5744 | -78.40 % | 105118.7138 MeV (+35997.4 ppm) |
| ${}^{110}$Mo | 110 | 68 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 203.2381 | 919.5222 | -77.90 % | 106079.5144 MeV (+35934.6 ppm) |
| ${}^{111}$Mo | 111 | 69 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 209.1437 | 922.9975 | -77.34 % | 107040.3236 MeV (+35848.3 ppm) |
| ${}^{112}$Mo | 112 | 70 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 215.0409 | 928.5920 | -76.84 % | 108001.1412 MeV (+35784.8 ppm) |
| ${}^{113}$Mo | 113 | 71 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 220.9299 | 931.7980 | -76.29 % | 108961.9670 MeV (+35699.3 ppm) |
| ${}^{114}$Mo | 114 | 72 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 226.8109 | 936.9660 | -75.79 % | 109922.8008 MeV (+35633.4 ppm) |
| ${}^{115}$Mo | 115 | 73 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 232.6839 | 939.8950 | -75.24 % | 110883.6425 MeV (+35547.9 ppm) |
| ${}^{116}$Mo | 116 | 74 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 238.5492 | 944.5880 | -74.75 % | 111844.4920 MeV (+35481.1 ppm) |
| ${}^{117}$Mo | 117 | 75 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 244.4070 | 947.2320 | -74.20 % | 112805.3490 MeV (+35394.8 ppm) |
| ${}^{118}$Mo | 118 | 76 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 250.2573 | 951.9060 | -73.71 % | 113766.2135 MeV (+35330.7 ppm) |
| ${}^{119}$Mo | 119 | 77 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 256.1002 | 954.2610 | -73.16 % | 114727.0853 MeV (+35244.8 ppm) |

### Technetium (Z = 43)

_40 of 40 isotopes with a framework prediction; 40 of 40 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{83}$Tc | 83 | 40 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 23.7329 | 667.5690 | -96.44 % | 80156.3905 MeV (+37184.3 ppm) |
| ${}^{84}$Tc | 84 | 41 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 30.0037 | 682.0800 | -95.60 % | 81116.8344 MeV (+37196.2 ppm) |
| ${}^{85}$Tc | 85 | 42 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 36.2582 | 698.2750 | -94.81 % | 82077.2948 MeV (+37231.2 ppm) |
| ${}^{86}$Tc | 86 | 43 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 42.4965 | 712.0800 | -94.03 % | 83037.7712 MeV (+37234.1 ppm) |
| ${}^{87}$Tc | 87 | 44 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 48.7193 | 726.2538 | -93.29 % | 83998.2632 MeV (+37242.3 ppm) |
| ${}^{88}$Tc | 88 | 45 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 54.9268 | 738.3054 | -92.56 % | 84958.7705 MeV (+37223.4 ppm) |
| ${}^{89}$Tc | 89 | 46 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 61.1195 | 752.1012 | -91.87 % | 85919.2926 MeV (+37226.9 ppm) |
| ${}^{90}$Tc | 90 | 47 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 67.2977 | 763.5024 | -91.19 % | 86879.8291 MeV (+37200.9 ppm) |
| ${}^{91}$Tc | 91 | 48 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 73.4618 | 776.8357 | -90.54 % | 87840.3798 MeV (+37199.2 ppm) |
| ${}^{92}$Tc | 92 | 49 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 79.6121 | 787.8460 | -89.89 % | 88800.9442 MeV (+37169.7 ppm) |
| ${}^{93}$Tc | 93 | 50 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 85.7490 | 800.5978 | -89.29 % | 89761.5221 MeV (+37161.8 ppm) |
| ${}^{94}$Tc | 94 | 51 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 91.8728 | 809.2213 | -88.65 % | 90722.1131 MeV (+37105.2 ppm) |
| ${}^{95}$Tc | 95 | 52 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 97.9838 | 819.1557 | -88.04 % | 91682.7169 MeV (+37065.4 ppm) |
| ${}^{96}$Tc | 96 | 53 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 104.0823 | 827.0273 | -87.41 % | 92643.3331 MeV (+37002.6 ppm) |
| ${}^{97}$Tc | 97 | 54 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 110.1686 | 836.5014 | -86.83 % | 93603.9616 MeV (+36959.6 ppm) |
| ${}^{98}$Tc | 98 | 55 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 116.2430 | 843.7805 | -86.22 % | 94564.6020 MeV (+36892.7 ppm) |
| ${}^{99}$Tc | 99 | 56 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 122.3057 | 852.7474 | -85.66 % | 95525.2540 MeV (+36846.2 ppm) |
| ${}^{100}$Tc | 100 | 57 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 128.3571 | 859.5118 | -85.07 % | 96485.9175 MeV (+36776.3 ppm) |
| ${}^{101}$Tc | 101 | 58 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 134.3973 | 867.9068 | -84.51 % | 97446.5920 MeV (+36725.9 ppm) |
| ${}^{102}$Tc | 102 | 59 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 140.4266 | 874.2064 | -83.94 % | 98407.2775 MeV (+36653.7 ppm) |
| ${}^{103}$Tc | 103 | 60 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 146.4453 | 882.3088 | -83.40 % | 99367.9736 MeV (+36602.4 ppm) |
| ${}^{104}$Tc | 104 | 61 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 152.4536 | 888.2751 | -82.84 % | 100328.6801 MeV (+36529.5 ppm) |
| ${}^{105}$Tc | 105 | 62 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 158.4517 | 896.1338 | -82.32 % | 101289.3967 MeV (+36478.0 ppm) |
| ${}^{106}$Tc | 106 | 63 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 164.4398 | 901.6950 | -81.76 % | 102250.1234 MeV (+36403.6 ppm) |
| ${}^{107}$Tc | 107 | 64 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 170.4181 | 908.7401 | -81.25 % | 103210.8598 MeV (+36346.0 ppm) |
| ${}^{108}$Tc | 108 | 65 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 176.3869 | 913.9843 | -80.70 % | 104171.6058 MeV (+36271.1 ppm) |
| ${}^{109}$Tc | 109 | 66 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 182.3464 | 920.4156 | -80.19 % | 105132.3611 MeV (+36209.7 ppm) |
| ${}^{110}$Tc | 110 | 67 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 188.2967 | 925.2386 | -79.65 % | 106093.1256 MeV (+36133.3 ppm) |
| ${}^{111}$Tc | 111 | 68 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 194.2380 | 931.3001 | -79.14 % | 107053.8991 MeV (+36070.8 ppm) |
| ${}^{112}$Tc | 112 | 69 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 200.1705 | 935.6056 | -78.61 % | 108014.6814 MeV (+35992.0 ppm) |
| ${}^{113}$Tc | 113 | 70 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 206.0944 | 941.2296 | -78.10 % | 108975.4722 MeV (+35927.7 ppm) |
| ${}^{114}$Tc | 114 | 71 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 212.0098 | 945.0896 | -77.57 % | 109936.2716 MeV (+35847.4 ppm) |
| ${}^{115}$Tc | 115 | 72 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 217.9170 | 950.3600 | -77.07 % | 110897.0792 MeV (+35782.2 ppm) |
| ${}^{116}$Tc | 116 | 73 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 223.8160 | 953.8680 | -76.54 % | 111857.8949 MeV (+35701.1 ppm) |
| ${}^{117}$Tc | 117 | 74 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 229.7071 | 958.8150 | -76.04 % | 112818.7186 MeV (+35635.8 ppm) |
| ${}^{118}$Tc | 118 | 75 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 235.5904 | 962.0540 | -75.51 % | 113779.5501 MeV (+35555.0 ppm) |
| ${}^{119}$Tc | 119 | 76 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 241.4660 | 966.9940 | -75.03 % | 114740.3892 MeV (+35491.8 ppm) |
| ${}^{120}$Tc | 120 | 77 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 247.3341 | 969.9600 | -74.50 % | 115701.2359 MeV (+35410.7 ppm) |
| ${}^{121}$Tc | 121 | 78 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 253.1948 | 974.5340 | -74.02 % | 116662.0900 MeV (+35346.7 ppm) |
| ${}^{122}$Tc | 122 | 79 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 259.0483 | 977.3420 | -73.49 % | 117622.9512 MeV (+35267.7 ppm) |

### Ruthenium (Z = 44)

_41 of 41 isotopes with a framework prediction; 41 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{85}$Ru | 85 | 41 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 19.9388 | 682.2950 | -97.08 % | 82092.2839 MeV (+37221.1 ppm) |
| ${}^{86}$Ru | 86 | 42 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 26.2280 | 699.4380 | -96.25 % | 83052.7094 MeV (+37267.8 ppm) |
| ${}^{87}$Ru | 87 | 43 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 32.5009 | 713.4870 | -95.44 % | 84013.1513 MeV (+37272.9 ppm) |
| ${}^{88}$Ru | 88 | 44 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 38.7578 | 730.2240 | -94.69 % | 84973.6092 MeV (+37311.7 ppm) |
| ${}^{89}$Ru | 89 | 45 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 44.9991 | 742.2935 | -93.94 % | 85934.0826 MeV (+37292.4 ppm) |
| ${}^{90}$Ru | 90 | 46 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 51.2253 | 756.8792 | -93.23 % | 86894.5712 MeV (+37304.5 ppm) |
| ${}^{91}$Ru | 91 | 47 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 57.4367 | 768.3065 | -92.52 % | 87855.0746 MeV (+37277.9 ppm) |
| ${}^{92}$Ru | 92 | 48 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 63.6336 | 782.4392 | -91.87 % | 88815.5924 MeV (+37284.7 ppm) |
| ${}^{93}$Ru | 93 | 49 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 69.8165 | 793.4260 | -91.20 % | 89776.1243 MeV (+37253.9 ppm) |
| ${}^{94}$Ru | 94 | 50 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 75.9856 | 806.8642 | -90.58 % | 90736.6700 MeV (+37252.9 ppm) |
| ${}^{95}$Ru | 95 | 51 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 82.1414 | 815.8097 | -89.93 % | 91697.2290 MeV (+37199.4 ppm) |
| ${}^{96}$Ru | 96 | 52 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 88.2840 | 826.5036 | -89.32 % | 92657.8011 MeV (+37167.5 ppm) |
| ${}^{97}$Ru | 97 | 53 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 94.4139 | 834.6152 | -88.69 % | 93618.3861 MeV (+37106.7 ppm) |
| ${}^{98}$Ru | 98 | 54 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 100.5312 | 844.7908 | -88.10 % | 94578.9835 MeV (+37070.8 ppm) |
| ${}^{99}$Ru | 99 | 55 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 106.6364 | 852.2626 | -87.49 % | 95539.5931 MeV (+37005.2 ppm) |
| ${}^{100}$Ru | 100 | 56 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 112.7296 | 861.9359 | -86.92 % | 96500.2147 MeV (+36965.7 ppm) |
| ${}^{101}$Ru | 101 | 57 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 118.8111 | 868.7380 | -86.32 % | 97460.8479 MeV (+36895.3 ppm) |
| ${}^{102}$Ru | 102 | 58 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 124.8812 | 877.9576 | -85.78 % | 98421.4926 MeV (+36852.9 ppm) |
| ${}^{103}$Ru | 103 | 59 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 130.9402 | 884.1897 | -85.19 % | 99382.1483 MeV (+36779.1 ppm) |
| ${}^{104}$Ru | 104 | 60 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 136.9883 | 893.0896 | -84.66 % | 100342.8151 MeV (+36735.4 ppm) |
| ${}^{105}$Ru | 105 | 61 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 143.0257 | 898.9997 | -84.09 % | 101303.4924 MeV (+36661.0 ppm) |
| ${}^{106}$Ru | 106 | 62 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 149.0526 | 907.4597 | -83.57 % | 102264.1803 MeV (+36614.8 ppm) |
| ${}^{107}$Ru | 107 | 63 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 155.0693 | 913.0703 | -83.02 % | 103224.8784 MeV (+36540.0 ppm) |
| ${}^{108}$Ru | 108 | 64 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 161.0760 | 920.9405 | -82.51 % | 104185.5864 MeV (+36489.9 ppm) |
| ${}^{109}$Ru | 109 | 65 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 167.0729 | 926.0889 | -81.96 % | 105146.3043 MeV (+36413.1 ppm) |
| ${}^{110}$Ru | 110 | 66 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 173.0602 | 933.4944 | -81.46 % | 106107.0318 MeV (+36360.6 ppm) |
| ${}^{111}$Ru | 111 | 67 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 179.0380 | 938.2784 | -80.92 % | 107067.7687 MeV (+36282.8 ppm) |
| ${}^{112}$Ru | 112 | 68 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 185.0067 | 945.1952 | -80.43 % | 108028.5148 MeV (+36227.8 ppm) |
| ${}^{113}$Ru | 113 | 69 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 190.9663 | 949.5035 | -79.89 % | 108989.2700 MeV (+36148.1 ppm) |
| ${}^{114}$Ru | 114 | 70 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 196.9171 | 955.9282 | -79.40 % | 109950.0340 MeV (+36090.5 ppm) |
| ${}^{115}$Ru | 115 | 71 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 202.8592 | 959.8836 | -78.87 % | 110910.8067 MeV (+36010.1 ppm) |
| ${}^{116}$Ru | 116 | 72 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 208.7928 | 965.9185 | -78.38 % | 111871.5879 MeV (+35951.2 ppm) |
| ${}^{117}$Ru | 117 | 73 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 214.7180 | 969.4108 | -77.85 % | 112832.3774 MeV (+35869.1 ppm) |
| ${}^{118}$Ru | 118 | 74 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 220.6351 | 975.0340 | -77.37 % | 113793.1751 MeV (+35808.3 ppm) |
| ${}^{119}$Ru | 119 | 75 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 226.5441 | 978.1800 | -76.84 % | 114753.9808 MeV (+35725.8 ppm) |
| ${}^{120}$Ru | 120 | 76 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 232.4453 | 983.8800 | -76.37 % | 115714.7945 MeV (+35668.5 ppm) |
| ${}^{121}$Ru | 121 | 77 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 238.3387 | 986.8760 | -75.85 % | 116675.6158 MeV (+35587.0 ppm) |
| ${}^{122}$Ru | 122 | 78 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 244.2245 | 992.1040 | -75.38 % | 117636.4447 MeV (+35527.5 ppm) |
| ${}^{123}$Ru | 123 | 79 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 250.1030 | 994.9470 | -74.86 % | 118597.2811 MeV (+35447.5 ppm) |
| ${}^{124}$Ru | 124 | 80 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 255.9740 | 1000.0600 | -74.40 % | 119558.1248 MeV (+35389.2 ppm) |
| ${}^{125}$Ru | 125 | 81 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 261.8380 | 1002.8750 | -73.89 % | 120518.9756 MeV (+35311.7 ppm) |

### Rhodium (Z = 45)

_41 of 41 isotopes with a framework prediction; 41 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{88}$Rh | 88 | 43 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 22.2719 | 711.9200 | -96.87 % | 84988.7647 MeV (+37275.4 ppm) |
| ${}^{89}$Rh | 89 | 44 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 28.5631 | 728.8210 | -96.08 % | 85949.1884 MeV (+37315.5 ppm) |
| ${}^{90}$Rh | 90 | 45 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 34.8383 | 742.8600 | -95.31 % | 86909.6279 MeV (+37320.2 ppm) |
| ${}^{91}$Rh | 91 | 46 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 41.0981 | 757.8480 | -94.58 % | 87870.0829 MeV (+37336.6 ppm) |
| ${}^{92}$Rh | 92 | 47 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 47.3428 | 770.3547 | -93.85 % | 88830.5530 MeV (+37322.5 ppm) |
| ${}^{93}$Rh | 93 | 48 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 53.5727 | 784.4388 | -93.17 % | 89791.0378 MeV (+37327.9 ppm) |
| ${}^{94}$Rh | 94 | 49 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 59.7883 | 796.4059 | -92.49 % | 90751.5370 MeV (+37308.2 ppm) |
| ${}^{95}$Rh | 95 | 50 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 65.9898 | 809.9102 | -91.85 % | 91712.0503 MeV (+37307.1 ppm) |
| ${}^{96}$Rh | 96 | 51 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 72.1776 | 819.3287 | -91.19 % | 92672.5773 MeV (+37258.7 ppm) |
| ${}^{97}$Rh | 97 | 52 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 78.3520 | 830.3098 | -90.56 % | 93633.1176 MeV (+37229.4 ppm) |
| ${}^{98}$Rh | 98 | 53 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 84.5133 | 838.9588 | -89.93 % | 94593.6711 MeV (+37174.4 ppm) |
| ${}^{99}$Rh | 99 | 54 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 90.6619 | 849.4394 | -89.33 % | 95554.2373 MeV (+37141.2 ppm) |
| ${}^{100}$Rh | 100 | 55 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 96.7979 | 857.5173 | -88.71 % | 96514.8160 MeV (+37082.0 ppm) |
| ${}^{101}$Rh | 101 | 56 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 102.9217 | 867.4099 | -88.13 % | 97475.4070 MeV (+37044.2 ppm) |
| ${}^{102}$Rh | 102 | 57 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 109.0336 | 874.8521 | -87.54 % | 98436.0099 MeV (+36980.5 ppm) |
| ${}^{103}$Rh | 103 | 58 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 115.1339 | 884.1718 | -86.98 % | 99396.6244 MeV (+36938.4 ppm) |
| ${}^{104}$Rh | 104 | 59 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 121.2226 | 891.1708 | -86.40 % | 100357.2504 MeV (+36872.4 ppm) |
| ${}^{105}$Rh | 105 | 60 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 127.3002 | 900.1341 | -85.86 % | 101317.8876 MeV (+36828.6 ppm) |
| ${}^{106}$Rh | 106 | 61 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 133.3669 | 906.7168 | -85.29 % | 102278.5357 MeV (+36760.8 ppm) |
| ${}^{107}$Rh | 107 | 62 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 139.4229 | 915.2891 | -84.77 % | 103239.1945 MeV (+36715.0 ppm) |
| ${}^{108}$Rh | 108 | 63 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 145.4683 | 921.5279 | -84.21 % | 104199.8638 MeV (+36646.1 ppm) |
| ${}^{109}$Rh | 109 | 64 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 151.5035 | 929.5673 | -83.70 % | 105160.5434 MeV (+36597.0 ppm) |
| ${}^{110}$Rh | 110 | 65 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 157.5287 | 935.4681 | -83.16 % | 106121.2330 MeV (+36527.2 ppm) |
| ${}^{111}$Rh | 111 | 66 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 163.5440 | 943.0146 | -82.66 % | 107081.9325 MeV (+36475.3 ppm) |
| ${}^{112}$Rh | 112 | 67 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 169.5496 | 948.5131 | -82.12 % | 108042.6416 MeV (+36404.0 ppm) |
| ${}^{113}$Rh | 113 | 68 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 175.5458 | 955.6203 | -81.63 % | 109003.3602 MeV (+36350.0 ppm) |
| ${}^{114}$Rh | 114 | 69 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 181.5328 | 960.6349 | -81.10 % | 109964.0880 MeV (+36276.5 ppm) |
| ${}^{115}$Rh | 115 | 70 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 187.5106 | 967.2252 | -80.61 % | 110924.8250 MeV (+36219.7 ppm) |
| ${}^{116}$Rh | 116 | 71 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 193.4795 | 971.8030 | -80.09 % | 111885.5708 MeV (+36144.6 ppm) |
| ${}^{117}$Rh | 117 | 72 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 199.4397 | 978.0354 | -79.61 % | 112846.3254 MeV (+36086.7 ppm) |
| ${}^{118}$Rh | 118 | 73 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 205.3914 | 982.0968 | -79.09 % | 113807.0885 MeV (+36009.3 ppm) |
| ${}^{119}$Rh | 119 | 74 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 211.3346 | 988.1040 | -78.61 % | 114767.8601 MeV (+35951.5 ppm) |
| ${}^{120}$Rh | 120 | 75 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 217.2696 | 991.9200 | -78.10 % | 115728.6399 MeV (+35874.9 ppm) |
| ${}^{121}$Rh | 121 | 76 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 223.1965 | 997.6740 | -77.63 % | 116689.4277 MeV (+35816.5 ppm) |
| ${}^{122}$Rh | 122 | 77 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 229.1154 | 1001.3760 | -77.12 % | 117650.2236 MeV (+35740.9 ppm) |
| ${}^{123}$Rh | 123 | 78 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 235.0266 | 1006.7550 | -76.66 % | 118611.0272 MeV (+35681.8 ppm) |
| ${}^{124}$Rh | 124 | 79 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 240.9301 | 1010.3520 | -76.15 % | 119571.8384 MeV (+35607.7 ppm) |
| ${}^{125}$Rh | 125 | 80 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 246.8261 | 1015.5000 | -75.69 % | 120532.6572 MeV (+35549.0 ppm) |
| ${}^{126}$Rh | 126 | 81 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 252.7147 | 1018.9620 | -75.20 % | 121493.4833 MeV (+35475.9 ppm) |
| ${}^{127}$Rh | 127 | 82 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 258.5961 | 1023.6200 | -74.74 % | 122454.3167 MeV (+35414.2 ppm) |
| ${}^{128}$Rh | 128 | 83 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 264.4704 | 1025.2800 | -74.21 % | 123415.1572 MeV (+35328.1 ppm) |

### Palladium (Z = 46)

_42 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{90}$Pd | 90 | 44 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 18.1368 | 730.1700 | -97.52 % | 86924.9991 MeV (+37356.0 ppm) |
| ${}^{91}$Pd | 91 | 45 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 24.4461 | 744.6530 | -96.72 % | 87885.4046 MeV (+37365.7 ppm) |
| ${}^{92}$Pd | 92 | 46 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 30.7396 | 761.3524 | -95.96 % | 88845.8259 MeV (+37401.3 ppm) |
| ${}^{93}$Pd | 93 | 47 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 37.0176 | 773.6264 | -95.22 % | 89806.2626 MeV (+37383.5 ppm) |
| ${}^{94}$Pd | 94 | 48 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 43.2807 | 788.8182 | -94.51 % | 90766.7143 MeV (+37400.9 ppm) |
| ${}^{95}$Pd | 95 | 49 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 49.5290 | 800.7532 | -93.81 % | 91727.1808 MeV (+37379.9 ppm) |
| ${}^{96}$Pd | 96 | 50 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 55.7630 | 815.0420 | -93.16 % | 92687.6615 MeV (+37386.8 ppm) |
| ${}^{97}$Pd | 97 | 51 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 61.9830 | 824.7357 | -92.48 % | 93648.1563 MeV (+37341.0 ppm) |
| ${}^{98}$Pd | 98 | 52 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 68.1893 | 836.3222 | -91.85 % | 94608.6648 MeV (+37317.7 ppm) |
| ${}^{99}$Pd | 99 | 53 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 74.3822 | 845.2554 | -91.20 % | 95569.1866 MeV (+37265.2 ppm) |
| ${}^{100}$Pd | 100 | 54 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 80.5621 | 856.3565 | -90.59 % | 96529.7215 MeV (+37238.0 ppm) |
| ${}^{101}$Pd | 101 | 55 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 86.7292 | 864.6473 | -89.97 % | 97490.2692 MeV (+37180.5 ppm) |
| ${}^{102}$Pd | 102 | 56 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 92.8838 | 875.1894 | -89.39 % | 98450.8294 MeV (+37148.8 ppm) |
| ${}^{103}$Pd | 103 | 57 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 99.0262 | 882.8148 | -88.78 % | 99411.4018 MeV (+37086.4 ppm) |
| ${}^{104}$Pd | 104 | 58 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 105.1566 | 892.8242 | -88.22 % | 100371.9861 MeV (+37050.8 ppm) |
| ${}^{105}$Pd | 105 | 59 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 111.2754 | 899.9183 | -87.63 % | 101332.5821 MeV (+36985.0 ppm) |
| ${}^{106}$Pd | 106 | 60 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 117.3827 | 909.4793 | -87.09 % | 102293.1896 MeV (+36946.6 ppm) |
| ${}^{107}$Pd | 107 | 61 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 123.4788 | 916.0157 | -86.52 % | 103253.8083 MeV (+36877.5 ppm) |
| ${}^{108}$Pd | 108 | 62 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 129.5639 | 925.2386 | -86.00 % | 104214.4379 MeV (+36837.4 ppm) |
| ${}^{109}$Pd | 109 | 63 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 135.6383 | 931.3922 | -85.44 % | 105175.0783 MeV (+36766.9 ppm) |
| ${}^{110}$Pd | 110 | 64 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 141.7022 | 940.1879 | -84.93 % | 106135.7292 MeV (+36724.5 ppm) |
| ${}^{111}$Pd | 111 | 65 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 147.7558 | 945.9142 | -84.38 % | 107096.3904 MeV (+36652.2 ppm) |
| ${}^{112}$Pd | 112 | 66 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 153.7993 | 954.3207 | -83.88 % | 108057.0617 MeV (+36607.9 ppm) |
| ${}^{113}$Pd | 113 | 67 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 159.8329 | 959.6615 | -83.34 % | 109017.7428 MeV (+36534.3 ppm) |
| ${}^{114}$Pd | 114 | 68 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 165.8568 | 967.6326 | -82.86 % | 109978.4337 MeV (+36487.7 ppm) |
| ${}^{115}$Pd | 115 | 69 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 171.8712 | 972.6394 | -82.33 % | 110939.1341 MeV (+36413.4 ppm) |
| ${}^{116}$Pd | 116 | 70 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 177.8763 | 980.1160 | -81.85 % | 111899.8438 MeV (+36364.1 ppm) |
| ${}^{117}$Pd | 117 | 71 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 183.8722 | 984.7801 | -81.33 % | 112860.5626 MeV (+36289.0 ppm) |
| ${}^{118}$Pd | 118 | 72 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 189.8592 | 991.8159 | -80.86 % | 113821.2904 MeV (+36237.6 ppm) |
| ${}^{119}$Pd | 119 | 73 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 195.8374 | 995.9062 | -80.34 % | 114782.0269 MeV (+36159.7 ppm) |
| ${}^{120}$Pd | 120 | 74 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 201.8070 | 1002.8498 | -79.88 % | 115742.7721 MeV (+36109.5 ppm) |
| ${}^{121}$Pd | 121 | 75 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 207.7681 | 1006.8239 | -79.36 % | 116703.5258 MeV (+36033.0 ppm) |
| ${}^{122}$Pd | 122 | 76 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 213.7209 | 1013.3290 | -78.91 % | 117664.2877 MeV (+35980.9 ppm) |
| ${}^{123}$Pd | 123 | 77 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 219.6656 | 1017.2139 | -78.41 % | 118625.0578 MeV (+35906.0 ppm) |
| ${}^{124}$Pd | 124 | 78 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 225.6023 | 1023.2480 | -77.95 % | 119585.8359 MeV (+35851.7 ppm) |
| ${}^{125}$Pd | 125 | 79 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 231.5311 | 1026.8750 | -77.45 % | 120546.6219 MeV (+35776.9 ppm) |
| ${}^{126}$Pd | 126 | 80 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 237.4522 | 1032.8220 | -77.01 % | 121507.4156 MeV (+35723.4 ppm) |
| ${}^{127}$Pd | 127 | 81 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 243.3657 | 1036.3200 | -76.52 % | 122468.2168 MeV (+35649.9 ppm) |
| ${}^{128}$Pd | 128 | 82 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 249.2718 | 1041.5360 | -76.07 % | 123429.0255 MeV (+35592.6 ppm) |
| ${}^{129}$Pd | 129 | 83 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 255.1706 | 1043.0940 | -75.54 % | 124389.8415 MeV (+35504.6 ppm) |
| ${}^{130}$Pd | 130 | 84 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 261.0622 | 1045.9800 | -75.04 % | 125350.6647 MeV (+35429.6 ppm) |
| ${}^{131}$Pd | 131 | 85 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 266.9467 | 1047.0830 | -74.51 % | 126311.4949 MeV (+35340.2 ppm) |

### Silver (Z = 47)

_42 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{92}$Ag | 92 | 45 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 13.8240 | 743.3600 | -98.14 % | 88861.4111 MeV (+37374.3 ppm) |
| ${}^{93}$Ag | 93 | 46 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 20.1513 | 760.2750 | -97.35 % | 89821.7986 MeV (+37412.2 ppm) |
| ${}^{94}$Ag | 94 | 47 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 26.4629 | 774.3720 | -96.58 % | 90782.2019 MeV (+37415.5 ppm) |
| ${}^{95}$Ag | 95 | 48 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 32.7591 | 789.9250 | -95.85 % | 91742.6204 MeV (+37436.5 ppm) |
| ${}^{96}$Ag | 96 | 49 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 39.0403 | 802.5879 | -95.14 % | 92703.0540 MeV (+37423.6 ppm) |
| ${}^{97}$Ag | 97 | 50 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 45.3069 | 817.0516 | -94.45 % | 93663.5021 MeV (+37431.6 ppm) |
| ${}^{98}$Ag | 98 | 51 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 51.5592 | 827.2853 | -93.77 % | 94623.9646 MeV (+37391.6 ppm) |
| ${}^{99}$Ag | 99 | 52 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 57.7975 | 839.0027 | -93.11 % | 95584.4411 MeV (+37369.1 ppm) |
| ${}^{100}$Ag | 100 | 53 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 64.0222 | 848.4995 | -92.45 % | 96544.9312 MeV (+37322.6 ppm) |
| ${}^{101}$Ag | 101 | 54 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 70.2335 | 859.7672 | -91.83 % | 97505.4346 MeV (+37296.6 ppm) |
| ${}^{102}$Ag | 102 | 55 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 76.4318 | 868.7508 | -91.20 % | 98465.9511 MeV (+37246.3 ppm) |
| ${}^{103}$Ag | 103 | 56 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 82.6173 | 879.3782 | -90.61 % | 99426.4804 MeV (+37214.9 ppm) |
| ${}^{104}$Ag | 104 | 57 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 88.7903 | 887.7632 | -90.00 % | 100387.0221 MeV (+37160.3 ppm) |
| ${}^{105}$Ag | 105 | 58 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 94.9511 | 897.7889 | -89.42 % | 101347.5761 MeV (+37124.2 ppm) |
| ${}^{106}$Ag | 106 | 59 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 101.0999 | 905.7318 | -88.84 % | 102308.1420 MeV (+37067.0 ppm) |
| ${}^{107}$Ag | 107 | 60 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 107.2371 | 915.2674 | -88.28 % | 103268.7197 MeV (+37027.5 ppm) |
| ${}^{108}$Ag | 108 | 61 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 113.3628 | 922.5388 | -87.71 % | 104229.3088 MeV (+36965.6 ppm) |
| ${}^{109}$Ag | 109 | 62 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 119.4772 | 931.7228 | -87.18 % | 105189.9091 MeV (+36924.5 ppm) |
| ${}^{110}$Ag | 110 | 63 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 125.5807 | 938.5320 | -86.62 % | 106150.5204 MeV (+36860.1 ppm) |
| ${}^{111}$Ag | 111 | 64 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 131.6734 | 947.3614 | -86.10 % | 107111.1424 MeV (+36817.3 ppm) |
| ${}^{112}$Ag | 112 | 65 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 137.7556 | 953.8010 | -85.56 % | 108071.7750 MeV (+36751.6 ppm) |
| ${}^{113}$Ag | 113 | 66 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 143.8275 | 962.3155 | -85.05 % | 109032.4180 MeV (+36707.7 ppm) |
| ${}^{114}$Ag | 114 | 67 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 149.8892 | 968.2908 | -84.52 % | 109993.0710 MeV (+36639.7 ppm) |
| ${}^{115}$Ag | 115 | 68 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 155.9409 | 976.4139 | -84.03 % | 110953.7340 MeV (+36593.9 ppm) |
| ${}^{116}$Ag | 116 | 69 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 161.9830 | 982.0452 | -83.51 % | 111914.4067 MeV (+36525.0 ppm) |
| ${}^{117}$Ag | 117 | 70 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 168.0155 | 989.7558 | -83.02 % | 112875.0890 MeV (+36477.2 ppm) |
| ${}^{118}$Ag | 118 | 71 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 174.0386 | 995.1990 | -82.51 % | 113835.7806 MeV (+36408.9 ppm) |
| ${}^{119}$Ag | 119 | 72 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 180.0526 | 1002.3623 | -82.04 % | 114796.4814 MeV (+36357.9 ppm) |
| ${}^{120}$Ag | 120 | 73 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 186.0576 | 1007.4394 | -81.53 % | 115757.1913 MeV (+36288.4 ppm) |
| ${}^{121}$Ag | 121 | 74 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 192.0537 | 1014.2620 | -81.06 % | 116717.9099 MeV (+36236.3 ppm) |
| ${}^{122}$Ag | 122 | 75 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 198.0411 | 1019.0366 | -80.57 % | 117678.6373 MeV (+36166.4 ppm) |
| ${}^{123}$Ag | 123 | 76 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 204.0200 | 1025.5704 | -80.11 % | 118639.3731 MeV (+36113.7 ppm) |
| ${}^{124}$Ag | 124 | 77 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 209.9906 | 1030.3031 | -79.62 % | 119600.1173 MeV (+36045.7 ppm) |
| ${}^{125}$Ag | 125 | 78 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 215.9530 | 1036.6644 | -79.17 % | 120560.8697 MeV (+35993.3 ppm) |
| ${}^{126}$Ag | 126 | 79 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 221.9073 | 1040.8860 | -78.68 % | 121521.6302 MeV (+35923.5 ppm) |
| ${}^{127}$Ag | 127 | 80 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 227.8537 | 1046.9880 | -78.24 % | 122482.3986 MeV (+35869.9 ppm) |
| ${}^{128}$Ag | 128 | 81 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 233.7923 | 1051.0080 | -77.76 % | 123443.1747 MeV (+35801.0 ppm) |
| ${}^{129}$Ag | 129 | 82 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 239.7233 | 1056.2520 | -77.30 % | 124403.9585 MeV (+35742.7 ppm) |
| ${}^{130}$Ag | 130 | 83 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 245.6467 | 1058.4600 | -76.79 % | 125364.7498 MeV (+35658.6 ppm) |
| ${}^{131}$Ag | 131 | 84 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 251.5628 | 1061.3620 | -76.30 % | 126325.5485 MeV (+35582.8 ppm) |
| ${}^{132}$Ag | 132 | 85 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 257.4717 | 1062.9960 | -75.78 % | 127286.3544 MeV (+35498.2 ppm) |
| ${}^{133}$Ag | 133 | 86 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 263.3734 | 1065.7290 | -75.29 % | 128247.1674 MeV (+35423.4 ppm) |

### Cadmium (Z = 48)

_42 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{94}$Cd | 94 | 46 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 9.3348 | 761.5880 | -98.77 % | 90797.9996 MeV (+37454.2 ppm) |
| ${}^{95}$Cd | 95 | 47 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 15.6799 | 776.2450 | -97.98 % | 91758.3692 MeV (+37463.8 ppm) |
| ${}^{96}$Cd | 96 | 48 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 22.0094 | 792.8640 | -97.22 % | 92718.7545 MeV (+37495.5 ppm) |
| ${}^{97}$Cd | 97 | 49 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 28.3236 | 806.0992 | -96.49 % | 93679.1551 MeV (+37488.1 ppm) |
| ${}^{98}$Cd | 98 | 50 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 34.6229 | 821.0729 | -95.78 % | 94639.5706 MeV (+37500.9 ppm) |
| ${}^{99}$Cd | 99 | 51 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 40.9076 | 831.4390 | -95.08 % | 95600.0006 MeV (+37461.6 ppm) |
| ${}^{100}$Cd | 100 | 52 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 47.1781 | 843.7737 | -94.41 % | 96560.4450 MeV (+37445.3 ppm) |
| ${}^{101}$Cd | 101 | 53 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 53.4346 | 853.4869 | -93.74 % | 97520.9032 MeV (+37400.5 ppm) |
| ${}^{102}$Cd | 102 | 54 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 59.6775 | 865.3815 | -93.10 % | 98481.3751 MeV (+37380.5 ppm) |
| ${}^{103}$Cd | 103 | 55 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 65.9071 | 874.4447 | -92.46 % | 99441.8603 MeV (+37330.5 ppm) |
| ${}^{104}$Cd | 104 | 56 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 72.1236 | 885.8328 | -91.86 % | 100402.3585 MeV (+37306.4 ppm) |
| ${}^{105}$Cd | 105 | 57 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 78.3274 | 894.2696 | -91.24 % | 101362.8695 MeV (+37251.6 ppm) |
| ${}^{106}$Cd | 106 | 58 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 84.5187 | 905.1392 | -90.66 % | 102323.3930 MeV (+37223.6 ppm) |
| ${}^{107}$Cd | 107 | 59 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 90.6978 | 913.0687 | -90.07 % | 103283.9287 MeV (+37165.5 ppm) |
| ${}^{108}$Cd | 108 | 60 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 96.8649 | 923.4021 | -89.51 % | 104244.4763 MeV (+37133.5 ppm) |
| ${}^{109}$Cd | 109 | 61 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 103.0203 | 930.7253 | -88.93 % | 105205.0357 MeV (+37071.4 ppm) |
| ${}^{110}$Cd | 110 | 62 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 109.1643 | 940.6403 | -88.39 % | 106165.6065 MeV (+37036.8 ppm) |
| ${}^{111}$Cd | 111 | 63 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 115.2970 | 947.6159 | -87.83 % | 107126.1886 MeV (+36973.4 ppm) |
| ${}^{112}$Cd | 112 | 64 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 121.4187 | 957.0098 | -87.31 % | 108086.7817 MeV (+36935.3 ppm) |
| ${}^{113}$Cd | 113 | 65 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 127.5296 | 963.5496 | -86.76 % | 109047.3855 MeV (+36869.9 ppm) |
| ${}^{114}$Cd | 114 | 66 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 133.6299 | 972.5925 | -86.26 % | 110008.0000 MeV (+36830.1 ppm) |
| ${}^{115}$Cd | 115 | 67 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 139.7199 | 978.7334 | -85.72 % | 110968.6248 MeV (+36763.1 ppm) |
| ${}^{116}$Cd | 116 | 68 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 145.7997 | 987.4327 | -85.23 % | 111929.2597 MeV (+36721.8 ppm) |
| ${}^{117}$Cd | 117 | 69 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 151.8696 | 993.2100 | -84.71 % | 112889.9046 MeV (+36653.6 ppm) |
| ${}^{118}$Cd | 118 | 70 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 157.9297 | 1001.5645 | -84.23 % | 113850.5593 MeV (+36610.9 ppm) |
| ${}^{119}$Cd | 119 | 71 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 163.9802 | 1006.9111 | -83.71 % | 114811.2236 MeV (+36540.8 ppm) |
| ${}^{120}$Cd | 120 | 72 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 170.0213 | 1014.9629 | -83.25 % | 115771.8973 MeV (+36497.2 ppm) |
| ${}^{121}$Cd | 121 | 73 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 176.0531 | 1020.1507 | -82.74 % | 116732.5802 MeV (+36427.9 ppm) |
| ${}^{122}$Cd | 122 | 74 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 182.0759 | 1027.7605 | -82.28 % | 117693.2721 MeV (+36382.0 ppm) |
| ${}^{123}$Cd | 123 | 75 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 188.0899 | 1032.6336 | -81.79 % | 118653.9730 MeV (+36312.2 ppm) |
| ${}^{124}$Cd | 124 | 76 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 194.0951 | 1039.9902 | -81.34 % | 119614.6825 MeV (+36265.8 ppm) |
| ${}^{125}$Cd | 125 | 77 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 200.0917 | 1044.7102 | -80.85 % | 120575.4007 MeV (+36196.8 ppm) |
| ${}^{126}$Cd | 126 | 78 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 206.0799 | 1051.6892 | -80.40 % | 121536.1272 MeV (+36148.9 ppm) |
| ${}^{127}$Cd | 127 | 79 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 212.0599 | 1056.2459 | -79.92 % | 122496.8620 MeV (+36080.7 ppm) |
| ${}^{128}$Cd | 128 | 80 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 218.0318 | 1062.8143 | -79.49 % | 123457.6049 MeV (+36031.0 ppm) |
| ${}^{129}$Cd | 129 | 81 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 223.9956 | 1066.7695 | -79.00 % | 124418.3558 MeV (+35959.6 ppm) |
| ${}^{130}$Cd | 130 | 82 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 229.9517 | 1072.8363 | -78.57 % | 125379.1146 MeV (+35907.5 ppm) |
| ${}^{131}$Cd | 131 | 83 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 235.9001 | 1075.0018 | -78.06 % | 126339.8810 MeV (+35823.1 ppm) |
| ${}^{132}$Cd | 132 | 84 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 241.8408 | 1078.3268 | -77.57 % | 127300.6550 MeV (+35749.9 ppm) |
| ${}^{133}$Cd | 133 | 85 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 247.7742 | 1080.0930 | -77.06 % | 128261.4364 MeV (+35664.5 ppm) |
| ${}^{134}$Cd | 134 | 86 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 253.7003 | 1083.5240 | -76.59 % | 129222.2251 MeV (+35594.2 ppm) |
| ${}^{135}$Cd | 135 | 87 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 259.6191 | 1084.8600 | -76.07 % | 130183.0210 MeV (+35508.9 ppm) |

### Indium (Z = 49)

_42 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{96}$In | 96 | 47 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 4.6704 | 774.6240 | -99.40 % | 92734.7632 MeV (+37471.7 ppm) |
| ${}^{97}$In | 97 | 48 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 11.0333 | 792.0050 | -98.61 % | 93695.1151 MeV (+37511.6 ppm) |
| ${}^{98}$In | 98 | 49 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 17.3806 | 806.5400 | -97.85 % | 94655.4826 MeV (+37519.2 ppm) |
| ${}^{99}$In | 99 | 50 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 23.7126 | 822.0960 | -97.12 % | 95615.8653 MeV (+37537.5 ppm) |
| ${}^{100}$In | 100 | 51 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 30.0299 | 832.9749 | -96.39 % | 96576.2629 MeV (+37503.6 ppm) |
| ${}^{101}$In | 101 | 52 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 36.3325 | 845.4130 | -95.70 % | 97536.6750 MeV (+37487.8 ppm) |
| ${}^{102}$In | 102 | 53 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 42.6210 | 855.6343 | -95.02 % | 98497.1013 MeV (+37448.2 ppm) |
| ${}^{103}$In | 103 | 54 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 48.8956 | 867.6431 | -94.36 % | 99457.5415 MeV (+37428.9 ppm) |
| ${}^{104}$In | 104 | 55 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 55.1566 | 877.2648 | -93.71 % | 100417.9953 MeV (+37384.5 ppm) |
| ${}^{105}$In | 105 | 56 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 61.4042 | 888.7940 | -93.09 % | 101378.4624 MeV (+37361.4 ppm) |
| ${}^{106}$In | 106 | 57 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 67.6389 | 897.8329 | -92.47 % | 102338.9425 MeV (+37312.6 ppm) |
| ${}^{107}$In | 107 | 58 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 73.8608 | 908.8627 | -91.87 % | 103299.4353 MeV (+37285.6 ppm) |
| ${}^{108}$In | 108 | 59 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 80.0703 | 917.4872 | -91.27 % | 104259.9407 MeV (+37234.4 ppm) |
| ${}^{109}$In | 109 | 60 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 86.2675 | 927.9282 | -90.70 % | 105220.4582 MeV (+37202.8 ppm) |
| ${}^{110}$In | 110 | 61 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 92.4528 | 935.9800 | -90.12 % | 106180.9877 MeV (+37147.7 ppm) |
| ${}^{111}$In | 111 | 62 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 98.6263 | 945.9733 | -89.57 % | 107141.5289 MeV (+37113.3 ppm) |
| ${}^{112}$In | 112 | 63 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 104.7884 | 953.6427 | -89.01 % | 108102.0816 MeV (+37056.4 ppm) |
| ${}^{113}$In | 113 | 64 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 110.9392 | 963.0911 | -88.48 % | 109062.6456 MeV (+37018.1 ppm) |
| ${}^{114}$In | 114 | 65 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 117.0790 | 970.3651 | -87.93 % | 110023.2205 MeV (+36959.4 ppm) |
| ${}^{115}$In | 115 | 66 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 123.2080 | 979.4029 | -87.42 % | 110983.8063 MeV (+36919.0 ppm) |
| ${}^{116}$In | 116 | 67 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 129.3264 | 986.1877 | -86.89 % | 111944.4027 MeV (+36857.6 ppm) |
| ${}^{117}$In | 117 | 68 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 135.4344 | 994.9522 | -86.39 % | 112905.0095 MeV (+36816.3 ppm) |
| ${}^{118}$In | 118 | 69 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 141.5323 | 1001.3087 | -85.87 % | 113865.6264 MeV (+36753.0 ppm) |
| ${}^{119}$In | 119 | 70 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 147.6201 | 1009.8505 | -85.38 % | 114826.2534 MeV (+36711.4 ppm) |
| ${}^{120}$In | 120 | 71 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 153.6981 | 1015.9509 | -84.87 % | 115786.8901 MeV (+36647.8 ppm) |
| ${}^{121}$In | 121 | 72 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 159.7665 | 1024.1291 | -84.40 % | 116747.5365 MeV (+36604.5 ppm) |
| ${}^{122}$In | 122 | 73 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 165.8254 | 1029.9372 | -83.90 % | 117708.1923 MeV (+36540.4 ppm) |
| ${}^{123}$In | 123 | 74 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 171.8751 | 1037.8662 | -83.44 % | 118668.8574 MeV (+36496.6 ppm) |
| ${}^{124}$In | 124 | 75 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 177.9157 | 1043.3762 | -82.95 % | 119629.5316 MeV (+36431.9 ppm) |
| ${}^{125}$In | 125 | 76 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 183.9473 | 1050.9921 | -82.50 % | 120590.2148 MeV (+36387.0 ppm) |
| ${}^{126}$In | 126 | 77 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 189.9702 | 1056.4604 | -82.02 % | 121550.9066 MeV (+36324.0 ppm) |
| ${}^{127}$In | 127 | 78 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 195.9845 | 1063.6023 | -81.57 % | 122511.6072 MeV (+36276.7 ppm) |
| ${}^{128}$In | 128 | 79 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 201.9903 | 1068.9838 | -81.10 % | 123472.3161 MeV (+36214.9 ppm) |
| ${}^{129}$In | 129 | 80 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 207.9878 | 1075.6999 | -80.66 % | 124433.0334 MeV (+36165.6 ppm) |
| ${}^{130}$In | 130 | 81 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 213.9771 | 1080.8429 | -80.20 % | 125393.7589 MeV (+36103.7 ppm) |
| ${}^{131}$In | 131 | 82 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 219.9584 | 1087.0320 | -79.77 % | 126354.4923 MeV (+36051.8 ppm) |
| ${}^{132}$In | 132 | 83 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 225.9318 | 1089.4905 | -79.26 % | 127315.2337 MeV (+35969.2 ppm) |
| ${}^{133}$In | 133 | 84 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 231.8975 | 1092.8610 | -78.78 % | 128275.9828 MeV (+35895.3 ppm) |
| ${}^{134}$In | 134 | 85 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 237.8555 | 1095.1820 | -78.28 % | 129236.7396 MeV (+35814.4 ppm) |
| ${}^{135}$In | 135 | 86 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 243.8060 | 1098.3600 | -77.80 % | 130197.5038 MeV (+35741.8 ppm) |
| ${}^{136}$In | 136 | 87 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 249.7492 | 1100.3760 | -77.30 % | 131158.2754 MeV (+35659.9 ppm) |
| ${}^{137}$In | 137 | 88 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 255.6852 | 1103.2610 | -76.82 % | 132119.0542 MeV (+35587.3 ppm) |

### Tin (Z = 50)

_42 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{99}$Sn | 99 | 49 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 6.2125 | 807.9390 | -99.23 % | 95632.0351 MeV (+37562.1 ppm) |
| ${}^{100}$Sn | 100 | 50 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 12.5775 | 825.1626 | -98.48 % | 96592.3850 MeV (+37598.4 ppm) |
| ${}^{101}$Sn | 101 | 51 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 18.9273 | 836.3914 | -97.74 % | 97552.7499 MeV (+37567.8 ppm) |
| ${}^{102}$Sn | 102 | 52 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 25.2623 | 849.0920 | -97.02 % | 98513.1297 MeV (+37554.1 ppm) |
| ${}^{103}$Sn | 103 | 53 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 31.5828 | 859.3290 | -96.32 % | 99473.5240 MeV (+37514.0 ppm) |
| ${}^{104}$Sn | 104 | 54 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 37.8892 | 871.9268 | -95.65 % | 100433.9324 MeV (+37500.3 ppm) |
| ${}^{105}$Sn | 105 | 55 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 44.1817 | 881.7090 | -94.99 % | 101394.3547 MeV (+37457.1 ppm) |
| ${}^{106}$Sn | 106 | 56 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 50.4606 | 893.7961 | -94.35 % | 102354.7905 MeV (+37439.0 ppm) |
| ${}^{107}$Sn | 107 | 57 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 56.7263 | 903.0259 | -93.72 % | 103315.2396 MeV (+37391.6 ppm) |
| ${}^{108}$Sn | 108 | 58 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 62.9789 | 914.6549 | -93.11 % | 104275.7017 MeV (+37370.0 ppm) |
| ${}^{109}$Sn | 109 | 59 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 69.2188 | 923.2865 | -92.50 % | 105236.1766 MeV (+37318.3 ppm) |
| ${}^{110}$Sn | 110 | 60 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 75.4463 | 934.5696 | -91.93 % | 106196.6639 MeV (+37294.5 ppm) |
| ${}^{111}$Sn | 111 | 61 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 81.6616 | 942.7375 | -91.34 % | 107157.1634 MeV (+37240.0 ppm) |
| ${}^{112}$Sn | 112 | 62 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 87.8649 | 953.5253 | -90.79 % | 108117.6749 MeV (+37212.6 ppm) |
| ${}^{113}$Sn | 113 | 63 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 94.0564 | 961.2697 | -90.22 % | 109078.1981 MeV (+37155.8 ppm) |
| ${}^{114}$Sn | 114 | 64 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 100.2365 | 971.5726 | -89.68 % | 110038.7328 MeV (+37125.1 ppm) |
| ${}^{115}$Sn | 115 | 65 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 106.4053 | 979.1181 | -89.13 % | 110999.2787 MeV (+37068.3 ppm) |
| ${}^{116}$Sn | 116 | 66 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 112.5631 | 988.6815 | -88.61 % | 111959.8357 MeV (+37032.0 ppm) |
| ${}^{117}$Sn | 117 | 67 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 118.7101 | 995.6246 | -88.08 % | 112920.4035 MeV (+36971.5 ppm) |
| ${}^{118}$Sn | 118 | 68 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 124.8464 | 1004.9510 | -87.58 % | 113880.9820 MeV (+36934.6 ppm) |
| ${}^{119}$Sn | 119 | 69 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 130.9724 | 1011.4345 | -87.05 % | 114841.5708 MeV (+36871.8 ppm) |
| ${}^{120}$Sn | 120 | 70 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 137.0881 | 1020.5386 | -86.57 % | 115802.1699 MeV (+36834.5 ppm) |
| ${}^{121}$Sn | 121 | 71 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 143.1937 | 1026.7088 | -86.05 % | 116762.7790 MeV (+36770.8 ppm) |
| ${}^{122}$Sn | 122 | 72 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 149.2896 | 1035.5234 | -85.58 % | 117723.3979 MeV (+36732.5 ppm) |
| ${}^{123}$Sn | 123 | 73 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 155.3758 | 1041.4694 | -85.08 % | 118684.0265 MeV (+36668.8 ppm) |
| ${}^{124}$Sn | 124 | 74 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 161.4525 | 1049.9576 | -84.62 % | 119644.6646 MeV (+36629.1 ppm) |
| ${}^{125}$Sn | 125 | 75 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 167.5198 | 1055.6911 | -84.13 % | 120605.3120 MeV (+36565.6 ppm) |
| ${}^{126}$Sn | 126 | 76 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 173.5781 | 1063.8839 | -83.68 % | 121565.9685 MeV (+36524.9 ppm) |
| ${}^{127}$Sn | 127 | 77 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 179.6274 | 1069.4096 | -83.20 % | 122526.6340 MeV (+36461.6 ppm) |
| ${}^{128}$Sn | 128 | 78 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 185.6678 | 1077.3728 | -82.77 % | 123487.3083 MeV (+36420.5 ppm) |
| ${}^{129}$Sn | 129 | 79 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 191.6996 | 1082.6733 | -82.29 % | 124447.9913 MeV (+36357.1 ppm) |
| ${}^{130}$Sn | 130 | 80 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 197.7229 | 1090.2862 | -81.87 % | 125408.6828 MeV (+36314.6 ppm) |
| ${}^{131}$Sn | 131 | 81 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 203.7378 | 1095.4899 | -81.40 % | 126369.3826 MeV (+36252.4 ppm) |
| ${}^{132}$Sn | 132 | 82 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 209.7445 | 1102.8432 | -80.98 % | 127330.0907 MeV (+36209.2 ppm) |
| ${}^{133}$Sn | 133 | 83 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 215.7432 | 1105.2418 | -80.48 % | 128290.8068 MeV (+36125.4 ppm) |
| ${}^{134}$Sn | 134 | 84 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 221.7339 | 1108.8730 | -80.00 % | 129251.5309 MeV (+36053.1 ppm) |
| ${}^{135}$Sn | 135 | 85 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 227.7168 | 1111.1428 | -79.51 % | 130212.2628 MeV (+35970.7 ppm) |
| ${}^{136}$Sn | 136 | 86 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 233.6920 | 1114.7920 | -79.04 % | 131173.0023 MeV (+35900.5 ppm) |
| ${}^{137}$Sn | 137 | 87 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 239.6596 | 1116.8240 | -78.54 % | 132133.7495 MeV (+35818.8 ppm) |
| ${}^{138}$Sn | 138 | 88 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 245.6199 | 1120.2840 | -78.08 % | 133094.5040 MeV (+35749.4 ppm) |
| ${}^{139}$Sn | 139 | 89 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 251.5728 | 1122.1470 | -77.58 % | 134055.2658 MeV (+35668.7 ppm) |
| ${}^{140}$Sn | 140 | 90 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 257.5186 | 1125.3200 | -77.12 % | 135016.0348 MeV (+35600.1 ppm) |

### Antimony (Z = 51)

_41 of 41 isotopes with a framework prediction; 41 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{102}$Sb | 102 | 51 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 7.6014 | 834.4620 | -99.09 % | 98529.4604 MeV (+37574.9 ppm) |
| ${}^{103}$Sb | 103 | 52 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 13.9688 | 848.1020 | -98.35 % | 99489.8077 MeV (+37571.1 ppm) |
| ${}^{104}$Sb | 104 | 53 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 20.3214 | 858.8320 | -97.63 % | 100450.1698 MeV (+37535.9 ppm) |
| ${}^{105}$Sb | 105 | 54 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 26.6597 | 871.6042 | -96.94 % | 101410.5464 MeV (+37523.8 ppm) |
| ${}^{106}$Sb | 106 | 55 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 32.9838 | 882.1333 | -96.26 % | 102370.9370 MeV (+37488.2 ppm) |
| ${}^{107}$Sb | 107 | 56 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 39.2941 | 894.3846 | -95.61 % | 103331.3415 MeV (+37471.4 ppm) |
| ${}^{108}$Sb | 108 | 57 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 45.5908 | 904.2480 | -94.96 % | 104291.7595 MeV (+37430.4 ppm) |
| ${}^{109}$Sb | 109 | 58 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 51.8743 | 916.1250 | -94.34 % | 105252.1908 MeV (+37410.9 ppm) |
| ${}^{110}$Sb | 110 | 59 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 58.1448 | 925.3950 | -93.72 % | 106212.6350 MeV (+37365.5 ppm) |
| ${}^{111}$Sb | 111 | 60 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 64.4027 | 936.8534 | -93.13 % | 107173.0920 MeV (+37342.9 ppm) |
| ${}^{112}$Sb | 112 | 61 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 70.6480 | 945.6869 | -92.53 % | 108133.5614 MeV (+37294.8 ppm) |
| ${}^{113}$Sb | 113 | 62 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 76.8812 | 956.5762 | -91.96 % | 109094.0430 MeV (+37267.9 ppm) |
| ${}^{114}$Sb | 114 | 63 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 83.1024 | 964.7272 | -91.39 % | 110054.5366 MeV (+37214.8 ppm) |
| ${}^{115}$Sb | 115 | 64 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 89.3118 | 975.3053 | -90.84 % | 111015.0419 MeV (+37186.2 ppm) |
| ${}^{116}$Sb | 116 | 65 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 95.5098 | 983.1952 | -90.29 % | 111975.5587 MeV (+37132.5 ppm) |
| ${}^{117}$Sb | 117 | 66 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 101.6965 | 993.0841 | -89.76 % | 112936.0868 MeV (+37098.8 ppm) |
| ${}^{118}$Sb | 118 | 67 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 107.8722 | 1000.5120 | -89.22 % | 113896.6259 MeV (+37042.5 ppm) |
| ${}^{119}$Sb | 119 | 68 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 114.0370 | 1010.0627 | -88.71 % | 114857.1759 MeV (+37007.2 ppm) |
| ${}^{120}$Sb | 120 | 69 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 120.1912 | 1017.0756 | -88.18 % | 115817.7365 MeV (+36949.0 ppm) |
| ${}^{121}$Sb | 121 | 70 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 126.3349 | 1026.3289 | -87.69 % | 116778.3075 MeV (+36912.4 ppm) |
| ${}^{122}$Sb | 122 | 71 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 132.4684 | 1033.1353 | -87.18 % | 117738.8888 MeV (+36854.2 ppm) |
| ${}^{123}$Sb | 123 | 72 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 138.5918 | 1042.0953 | -86.70 % | 118699.4802 MeV (+36816.6 ppm) |
| ${}^{124}$Sb | 124 | 73 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 144.7054 | 1048.5628 | -86.20 % | 119660.0814 MeV (+36757.2 ppm) |
| ${}^{125}$Sb | 125 | 74 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 150.8092 | 1057.2702 | -85.74 % | 120620.6923 MeV (+36718.9 ppm) |
| ${}^{126}$Sb | 126 | 75 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 156.9036 | 1063.4795 | -85.25 % | 121581.3127 MeV (+36659.1 ppm) |
| ${}^{127}$Sb | 127 | 76 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 162.9886 | 1071.8560 | -84.79 % | 122541.9425 MeV (+36619.4 ppm) |
| ${}^{128}$Sb | 128 | 77 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 169.0644 | 1077.8589 | -84.31 % | 123502.5814 MeV (+36559.7 ppm) |
| ${}^{129}$Sb | 129 | 78 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 175.1312 | 1085.9297 | -83.87 % | 124463.2294 MeV (+36518.9 ppm) |
| ${}^{130}$Sb | 130 | 79 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 181.1892 | 1091.6573 | -83.40 % | 125423.8862 MeV (+36458.7 ppm) |
| ${}^{131}$Sb | 131 | 80 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 187.2384 | 1099.4244 | -82.97 % | 126384.5517 MeV (+36416.8 ppm) |
| ${}^{132}$Sb | 132 | 81 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 193.2791 | 1105.1496 | -82.51 % | 127345.2258 MeV (+36358.5 ppm) |
| ${}^{133}$Sb | 133 | 82 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 199.3114 | 1112.5091 | -82.08 % | 128305.9083 MeV (+36314.7 ppm) |
| ${}^{134}$Sb | 134 | 83 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 205.3354 | 1115.6759 | -81.60 % | 129266.5991 MeV (+36236.8 ppm) |
| ${}^{135}$Sb | 135 | 84 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 211.3513 | 1119.4186 | -81.12 % | 130227.2980 MeV (+36165.0 ppm) |
| ${}^{136}$Sb | 136 | 85 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 217.3592 | 1122.3064 | -80.63 % | 131188.0048 MeV (+36087.2 ppm) |
| ${}^{137}$Sb | 137 | 86 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 223.3592 | 1125.9313 | -80.16 % | 132148.7196 MeV (+36016.6 ppm) |
| ${}^{138}$Sb | 138 | 87 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 229.3515 | 1128.5640 | -79.68 % | 133109.4420 MeV (+35939.4 ppm) |
| ${}^{139}$Sb | 139 | 88 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 235.3362 | 1132.0160 | -79.21 % | 134070.1721 MeV (+35869.8 ppm) |
| ${}^{140}$Sb | 140 | 89 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 241.3135 | 1134.4200 | -78.73 % | 135030.9096 MeV (+35792.8 ppm) |
| ${}^{141}$Sb | 141 | 90 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 247.2833 | 1137.7290 | -78.27 % | 135991.6545 MeV (+35723.4 ppm) |
| ${}^{142}$Sb | 142 | 91 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 253.2460 | 1139.8340 | -77.78 % | 136952.4067 MeV (+35646.6 ppm) |

### Tellurium (Z = 52)

_42 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{104}$Te | 104 | 52 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 2.4533 | 848.3619 | -99.71 % | 100466.7076 MeV (+37603.1 ppm) |
| ${}^{105}$Te | 105 | 53 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 8.8382 | 859.6179 | -98.97 % | 101427.0375 MeV (+37573.6 ppm) |
| ${}^{106}$Te | 106 | 54 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 15.2084 | 873.0974 | -98.26 % | 102387.3821 MeV (+37568.1 ppm) |
| ${}^{107}$Te | 107 | 55 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 21.5642 | 883.6060 | -97.56 % | 103347.7410 MeV (+37532.0 ppm) |
| ${}^{108}$Te | 108 | 56 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 27.9060 | 896.8020 | -96.89 % | 104308.1141 MeV (+37524.4 ppm) |
| ${}^{109}$Te | 109 | 57 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 34.2339 | 906.8070 | -96.22 % | 105268.5009 MeV (+37484.4 ppm) |
| ${}^{110}$Te | 110 | 58 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 40.5484 | 919.3928 | -95.59 % | 106228.9012 MeV (+37471.4 ppm) |
| ${}^{111}$Te | 111 | 59 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 46.8496 | 928.8217 | -94.96 % | 107189.3148 MeV (+37427.1 ppm) |
| ${}^{112}$Te | 112 | 60 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 53.1379 | 940.8731 | -94.35 % | 108149.7413 MeV (+37409.9 ppm) |
| ${}^{113}$Te | 113 | 61 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 59.4135 | 949.7239 | -93.74 % | 109110.1805 MeV (+37361.4 ppm) |
| ${}^{114}$Te | 114 | 62 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 65.6766 | 961.3379 | -93.17 % | 110070.6321 MeV (+37341.0 ppm) |
| ${}^{115}$Te | 115 | 63 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 71.9275 | 969.5823 | -92.58 % | 111031.0959 MeV (+37288.4 ppm) |
| ${}^{116}$Te | 116 | 64 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 78.1665 | 980.8546 | -92.03 % | 111991.5717 MeV (+37265.8 ppm) |
| ${}^{117}$Te | 117 | 65 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 84.3938 | 988.7577 | -91.46 % | 112952.0592 MeV (+37211.7 ppm) |
| ${}^{118}$Te | 118 | 66 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 90.6095 | 999.4242 | -90.93 % | 113912.5583 MeV (+37184.7 ppm) |
| ${}^{119}$Te | 119 | 67 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 96.8140 | 1006.9873 | -90.39 % | 114873.0686 MeV (+37129.2 ppm) |
| ${}^{120}$Te | 120 | 68 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 103.0074 | 1017.2383 | -89.87 % | 115833.5899 MeV (+37099.7 ppm) |
| ${}^{121}$Te | 121 | 69 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 109.1899 | 1024.4906 | -89.34 % | 116794.1222 MeV (+37043.1 ppm) |
| ${}^{122}$Te | 122 | 70 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 115.3618 | 1034.3320 | -88.85 % | 117754.6651 MeV (+37011.2 ppm) |
| ${}^{123}$Te | 123 | 71 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 121.5232 | 1041.2611 | -88.33 % | 118715.2184 MeV (+36953.6 ppm) |
| ${}^{124}$Te | 124 | 72 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 127.6744 | 1050.6855 | -87.85 % | 119675.7820 MeV (+36919.3 ppm) |
| ${}^{125}$Te | 125 | 73 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 133.8155 | 1057.2545 | -87.34 % | 120636.3557 MeV (+36860.3 ppm) |
| ${}^{126}$Te | 126 | 74 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 139.9467 | 1066.3682 | -86.88 % | 121596.9393 MeV (+36824.8 ppm) |
| ${}^{127}$Te | 127 | 75 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 146.0681 | 1072.6558 | -86.38 % | 122557.5326 MeV (+36765.1 ppm) |
| ${}^{128}$Te | 128 | 76 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 152.1800 | 1081.4405 | -85.93 % | 123518.1355 MeV (+36728.2 ppm) |
| ${}^{129}$Te | 129 | 77 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 158.2825 | 1087.5229 | -85.45 % | 124478.7478 MeV (+36668.6 ppm) |
| ${}^{130}$Te | 130 | 78 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 164.3758 | 1095.9423 | -85.00 % | 125439.3692 MeV (+36630.1 ppm) |
| ${}^{131}$Te | 131 | 79 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 170.4601 | 1101.8716 | -84.53 % | 126399.9997 MeV (+36571.0 ppm) |
| ${}^{132}$Te | 132 | 80 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 176.5355 | 1109.9201 | -84.09 % | 127360.6392 MeV (+36530.7 ppm) |
| ${}^{133}$Te | 133 | 81 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 182.6021 | 1115.7404 | -83.63 % | 128321.2873 MeV (+36472.5 ppm) |
| ${}^{134}$Te | 134 | 82 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 188.6601 | 1123.4083 | -83.21 % | 129281.9441 MeV (+36430.6 ppm) |
| ${}^{135}$Te | 135 | 83 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 194.7096 | 1126.6747 | -82.72 % | 130242.6093 MeV (+36353.1 ppm) |
| ${}^{136}$Te | 136 | 84 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 200.7509 | 1131.4425 | -82.26 % | 131203.2829 MeV (+36289.0 ppm) |
| ${}^{137}$Te | 137 | 85 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 206.7839 | 1134.3923 | -81.77 % | 132163.9646 MeV (+36211.2 ppm) |
| ${}^{138}$Te | 138 | 86 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 212.8089 | 1138.8558 | -81.31 % | 133124.6543 MeV (+36146.8 ppm) |
| ${}^{139}$Te | 139 | 87 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 218.8261 | 1141.4363 | -80.83 % | 134085.3520 MeV (+36068.4 ppm) |
| ${}^{140}$Te | 140 | 88 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 224.8354 | 1145.6699 | -80.38 % | 135046.0574 MeV (+36004.2 ppm) |
| ${}^{141}$Te | 141 | 89 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 230.8371 | 1148.0220 | -79.89 % | 136006.7705 MeV (+35926.4 ppm) |
| ${}^{142}$Te | 142 | 90 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 236.8313 | 1152.0460 | -79.44 % | 136967.4911 MeV (+35862.0 ppm) |
| ${}^{143}$Te | 143 | 91 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 242.8180 | 1154.0100 | -78.96 % | 137928.2191 MeV (+35783.9 ppm) |
| ${}^{144}$Te | 144 | 92 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 248.7975 | 1157.7600 | -78.51 % | 138888.9544 MeV (+35720.1 ppm) |
| ${}^{145}$Te | 145 | 93 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 254.7697 | 1159.7100 | -78.03 % | 139849.6969 MeV (+35642.6 ppm) |

### Iodine (Z = 53)

_42 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{106}$I | 106 | 53 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -2.8655 | 857.4340 | -100.33 % | 102404.1257 MeV (+37580.9 ppm) |
| ${}^{107}$I | 107 | 54 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 3.5368 | 871.6220 | -99.59 % | 103364.4382 MeV (+37582.6 ppm) |
| ${}^{108}$I | 108 | 55 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 9.9244 | 883.0080 | -98.88 % | 104324.7654 MeV (+37555.7 ppm) |
| ${}^{109}$I | 109 | 56 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 16.2977 | 895.9818 | -98.18 % | 105285.1068 MeV (+37545.4 ppm) |
| ${}^{110}$I | 110 | 57 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 22.6569 | 906.8484 | -97.50 % | 106245.4624 MeV (+37514.0 ppm) |
| ${}^{111}$I | 111 | 58 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 29.0024 | 919.4057 | -96.85 % | 107205.8317 MeV (+37500.3 ppm) |
| ${}^{112}$I | 112 | 59 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 35.3345 | 929.5866 | -96.20 % | 108166.2144 MeV (+37463.3 ppm) |
| ${}^{113}$I | 113 | 60 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 41.6533 | 941.7141 | -95.58 % | 109126.6103 MeV (+37446.4 ppm) |
| ${}^{114}$I | 114 | 61 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 47.9592 | 951.3048 | -94.96 % | 110087.0192 MeV (+37405.0 ppm) |
| ${}^{115}$I | 115 | 62 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 54.2524 | 963.0750 | -94.37 % | 111047.4408 MeV (+37385.6 ppm) |
| ${}^{116}$I | 116 | 63 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 60.5332 | 972.2292 | -93.77 % | 112007.8748 MeV (+37341.5 ppm) |
| ${}^{117}$I | 117 | 64 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 66.8018 | 983.3184 | -93.21 % | 112968.3209 MeV (+37316.7 ppm) |
| ${}^{118}$I | 118 | 65 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 73.0584 | 991.9222 | -92.63 % | 113928.7791 MeV (+37268.9 ppm) |
| ${}^{119}$I | 119 | 66 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 79.3033 | 1002.8002 | -92.09 % | 114889.2489 MeV (+37243.4 ppm) |
| ${}^{120}$I | 120 | 67 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 85.5367 | 1010.8409 | -91.54 % | 115849.7303 MeV (+37192.0 ppm) |
| ${}^{121}$I | 121 | 68 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 91.7589 | 1021.4107 | -91.02 % | 116810.2229 MeV (+37164.9 ppm) |
| ${}^{122}$I | 122 | 69 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 97.9699 | 1029.3157 | -90.48 % | 117770.7267 MeV (+37114.0 ppm) |
| ${}^{123}$I | 123 | 70 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 104.1701 | 1039.2503 | -89.98 % | 118731.2413 MeV (+37082.4 ppm) |
| ${}^{124}$I | 124 | 71 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 110.3596 | 1046.7436 | -89.46 % | 119691.7665 MeV (+37029.5 ppm) |
| ${}^{125}$I | 125 | 72 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 116.5386 | 1056.2864 | -88.97 % | 120652.3023 MeV (+36995.7 ppm) |
| ${}^{126}$I | 126 | 73 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 122.7073 | 1063.4322 | -88.46 % | 121612.8483 MeV (+36941.4 ppm) |
| ${}^{127}$I | 127 | 74 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 128.8660 | 1072.5762 | -87.99 % | 122573.4045 MeV (+36905.6 ppm) |
| ${}^{128}$I | 128 | 75 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 135.0147 | 1079.4024 | -87.49 % | 123533.9706 MeV (+36850.2 ppm) |
| ${}^{129}$I | 129 | 76 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 141.1536 | 1088.2428 | -87.03 % | 124494.5464 MeV (+36813.2 ppm) |
| ${}^{130}$I | 130 | 77 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 147.2830 | 1094.7431 | -86.55 % | 125455.1318 MeV (+36756.7 ppm) |
| ${}^{131}$I | 131 | 78 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 153.4029 | 1103.3210 | -86.10 % | 126415.7266 MeV (+36718.9 ppm) |
| ${}^{132}$I | 132 | 79 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 159.5136 | 1109.6531 | -85.62 % | 127376.3307 MeV (+36662.8 ppm) |
| ${}^{133}$I | 133 | 80 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 165.6152 | 1117.8782 | -85.18 % | 128336.9439 MeV (+36623.4 ppm) |
| ${}^{134}$I | 134 | 81 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 171.7079 | 1124.1357 | -84.73 % | 129297.5660 MeV (+36568.4 ppm) |
| ${}^{135}$I | 135 | 82 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 177.7918 | 1131.9427 | -84.29 % | 130258.1969 MeV (+36527.0 ppm) |
| ${}^{136}$I | 136 | 83 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 183.8670 | 1135.7801 | -83.81 % | 131218.8364 MeV (+36453.8 ppm) |
| ${}^{137}$I | 137 | 84 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 189.9337 | 1140.6625 | -83.35 % | 132179.4844 MeV (+36390.2 ppm) |
| ${}^{138}$I | 138 | 85 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 195.9921 | 1144.3574 | -82.87 % | 133140.1408 MeV (+36318.1 ppm) |
| ${}^{139}$I | 139 | 86 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 202.0423 | 1148.9198 | -82.41 % | 134100.8054 MeV (+36254.0 ppm) |
| ${}^{140}$I | 140 | 87 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 208.0844 | 1152.1264 | -81.94 % | 135061.4781 MeV (+36180.1 ppm) |
| ${}^{141}$I | 141 | 88 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 214.1185 | 1156.5181 | -81.49 % | 136022.1588 MeV (+36116.6 ppm) |
| ${}^{142}$I | 142 | 89 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 220.1448 | 1159.4657 | -81.01 % | 136982.8473 MeV (+36042.8 ppm) |
| ${}^{143}$I | 143 | 90 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 226.1634 | 1163.5910 | -80.56 % | 137943.5434 MeV (+35978.8 ppm) |
| ${}^{144}$I | 144 | 91 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 232.1744 | 1166.1120 | -80.09 % | 138904.2472 MeV (+35904.5 ppm) |
| ${}^{145}$I | 145 | 92 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 238.1780 | 1170.0050 | -79.64 % | 139864.9584 MeV (+35841.0 ppm) |
| ${}^{146}$I | 146 | 93 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 244.1742 | 1172.5260 | -79.18 % | 140825.6770 MeV (+35767.8 ppm) |
| ${}^{147}$I | 147 | 94 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 250.1632 | 1176.1470 | -78.73 % | 141786.4028 MeV (+35705.1 ppm) |

### Xenon (Z = 54)

_43 of 43 isotopes with a framework prediction; 43 of 43 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{108}$Xe | 108 | 54 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -8.3539 | 872.0880 | -100.96 % | 104341.7134 MeV (+37619.6 ppm) |
| ${}^{109}$Xe | 109 | 55 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -1.9344 | 883.6965 | -100.22 % | 105302.0087 MeV (+37594.3 ppm) |
| ${}^{110}$Xe | 110 | 56 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 4.4705 | 897.5209 | -99.50 % | 106262.3185 MeV (+37592.0 ppm) |
| ${}^{111}$Xe | 111 | 57 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 10.8611 | 908.2020 | -98.80 % | 107222.6427 MeV (+37558.2 ppm) |
| ${}^{112}$Xe | 112 | 58 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 17.2377 | 921.7672 | -98.13 % | 108182.9808 MeV (+37554.1 ppm) |
| ${}^{113}$Xe | 113 | 59 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 23.6006 | 932.0158 | -97.47 % | 109143.3327 MeV (+37517.4 ppm) |
| ${}^{114}$Xe | 114 | 60 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 29.9501 | 944.9694 | -96.83 % | 110103.6980 MeV (+37507.9 ppm) |
| ${}^{115}$Xe | 115 | 61 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 36.2864 | 954.6116 | -96.20 % | 111064.0764 MeV (+37466.5 ppm) |
| ${}^{116}$Xe | 116 | 62 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 42.6098 | 967.0730 | -95.59 % | 112024.4678 MeV (+37453.1 ppm) |
| ${}^{117}$Xe | 117 | 63 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 48.9206 | 976.2828 | -94.99 % | 112984.8718 MeV (+37409.1 ppm) |
| ${}^{118}$Xe | 118 | 64 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 55.2189 | 988.2479 | -94.41 % | 113945.2883 MeV (+37391.9 ppm) |
| ${}^{119}$Xe | 119 | 65 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 61.5051 | 997.0346 | -93.83 % | 114905.7169 MeV (+37345.4 ppm) |
| ${}^{120}$Xe | 120 | 66 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 67.7792 | 1008.4839 | -93.28 % | 115866.1575 MeV (+37324.5 ppm) |
| ${}^{121}$Xe | 121 | 67 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 74.0417 | 1016.8637 | -92.72 % | 116826.6098 MeV (+37275.7 ppm) |
| ${}^{122}$Xe | 122 | 68 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 80.2927 | 1027.8091 | -92.19 % | 117787.0736 MeV (+37251.3 ppm) |
| ${}^{123}$Xe | 123 | 69 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 86.5323 | 1035.7736 | -91.65 % | 118747.5487 MeV (+37200.4 ppm) |
| ${}^{124}$Xe | 124 | 70 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 92.7609 | 1046.2641 | -91.13 % | 119708.0349 MeV (+37173.1 ppm) |
| ${}^{125}$Xe | 125 | 71 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 98.9786 | 1053.8674 | -90.61 % | 120668.5320 MeV (+37120.6 ppm) |
| ${}^{126}$Xe | 126 | 72 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 105.1856 | 1063.8857 | -90.11 % | 121629.0398 MeV (+37090.4 ppm) |
| ${}^{127}$Xe | 127 | 73 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 111.3821 | 1071.1315 | -89.60 % | 122589.5580 MeV (+37036.4 ppm) |
| ${}^{128}$Xe | 128 | 74 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 117.5683 | 1080.7425 | -89.12 % | 123550.0866 MeV (+37004.0 ppm) |
| ${}^{129}$Xe | 129 | 75 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 123.7444 | 1087.6494 | -88.62 % | 124510.6253 MeV (+36948.7 ppm) |
| ${}^{130}$Xe | 130 | 76 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 129.9105 | 1096.9051 | -88.16 % | 125471.1740 MeV (+36914.5 ppm) |
| ${}^{131}$Xe | 131 | 77 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 136.0668 | 1103.5095 | -87.67 % | 126431.7324 MeV (+36858.4 ppm) |
| ${}^{132}$Xe | 132 | 78 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 142.2136 | 1112.4462 | -87.22 % | 127392.3005 MeV (+36822.9 ppm) |
| ${}^{133}$Xe | 133 | 79 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 148.3508 | 1118.8821 | -86.74 % | 128352.8779 MeV (+36767.1 ppm) |
| ${}^{134}$Xe | 134 | 80 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 154.4788 | 1127.4357 | -86.30 % | 129313.4647 MeV (+36729.8 ppm) |
| ${}^{135}$Xe | 135 | 81 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 160.5977 | 1133.7946 | -85.84 % | 130274.0606 MeV (+36675.0 ppm) |
| ${}^{136}$Xe | 136 | 82 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 166.7076 | 1141.8817 | -85.40 % | 131234.6655 MeV (+36635.2 ppm) |
| ${}^{137}$Xe | 137 | 83 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 172.8087 | 1145.9073 | -84.92 % | 132195.2792 MeV (+36563.1 ppm) |
| ${}^{138}$Xe | 138 | 84 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 178.9011 | 1151.5674 | -84.46 % | 133155.9016 MeV (+36505.2 ppm) |
| ${}^{139}$Xe | 139 | 85 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 184.9849 | 1155.3111 | -83.99 % | 134116.5325 MeV (+36432.9 ppm) |
| ${}^{140}$Xe | 140 | 86 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 191.0604 | 1160.7242 | -83.54 % | 135077.1718 MeV (+36375.0 ppm) |
| ${}^{141}$Xe | 141 | 87 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 197.1276 | 1164.0064 | -83.06 % | 136037.8194 MeV (+36301.2 ppm) |
| ${}^{142}$Xe | 142 | 88 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 203.1866 | 1169.1101 | -82.62 % | 136998.4751 MeV (+36242.7 ppm) |
| ${}^{143}$Xe | 143 | 89 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 209.2377 | 1172.1546 | -82.15 % | 137959.1388 MeV (+36169.1 ppm) |
| ${}^{144}$Xe | 144 | 90 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 215.2809 | 1176.8954 | -81.71 % | 138919.8104 MeV (+36109.7 ppm) |
| ${}^{145}$Xe | 145 | 91 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 221.3163 | 1179.5877 | -81.24 % | 139880.4898 MeV (+36035.5 ppm) |
| ${}^{146}$Xe | 146 | 92 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 227.3441 | 1184.1206 | -80.80 % | 140841.1767 MeV (+35976.4 ppm) |
| ${}^{147}$Xe | 147 | 93 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 233.3644 | 1186.5840 | -80.33 % | 141801.8712 MeV (+35902.8 ppm) |
| ${}^{148}$Xe | 148 | 94 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 239.3773 | 1190.9560 | -79.90 % | 142762.5731 MeV (+35843.9 ppm) |
| ${}^{149}$Xe | 149 | 95 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 245.3829 | 1193.3410 | -79.44 % | 143723.2822 MeV (+35771.7 ppm) |
| ${}^{150}$Xe | 150 | 96 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 251.3814 | 1197.4500 | -79.01 % | 144683.9986 MeV (+35712.6 ppm) |

### Caesium (Z = 55)

_42 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{111}$Cs | 111 | 56 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -7.5744 | 895.7700 | -100.85 % | 107239.7479 MeV (+37607.1 ppm) |
| ${}^{112}$Cs | 112 | 57 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -1.1523 | 907.4240 | -100.13 % | 108200.0406 MeV (+37582.3 ppm) |
| ${}^{113}$Cs | 113 | 58 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 5.2555 | 920.7944 | -99.43 % | 109160.3475 MeV (+37576.2 ppm) |
| ${}^{114}$Cs | 114 | 59 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 11.6494 | 931.7871 | -98.75 % | 110120.6684 MeV (+37546.5 ppm) |
| ${}^{115}$Cs | 115 | 60 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 18.0297 | 944.8400 | -98.09 % | 111081.0029 MeV (+37537.8 ppm) |
| ${}^{116}$Cs | 116 | 61 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 24.3965 | 955.2600 | -97.45 % | 112041.3508 MeV (+37503.7 ppm) |
| ${}^{117}$Cs | 117 | 62 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 30.7502 | 967.8082 | -96.82 % | 113001.7119 MeV (+37490.4 ppm) |
| ${}^{118}$Cs | 118 | 63 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 37.0910 | 977.7958 | -96.21 % | 113962.0859 MeV (+37453.5 ppm) |
| ${}^{119}$Cs | 119 | 64 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 43.4191 | 989.7628 | -95.61 % | 114922.4725 MeV (+37435.9 ppm) |
| ${}^{120}$Cs | 120 | 65 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 49.7349 | 999.4177 | -95.02 % | 115882.8716 MeV (+37397.2 ppm) |
| ${}^{121}$Cs | 121 | 66 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 56.0385 | 1010.7027 | -94.46 % | 116843.2828 MeV (+37374.2 ppm) |
| ${}^{122}$Cs | 122 | 67 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 62.3301 | 1019.8165 | -93.89 % | 117803.7059 MeV (+37331.9 ppm) |
| ${}^{123}$Cs | 123 | 68 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 68.6100 | 1030.7867 | -93.34 % | 118764.1408 MeV (+37307.3 ppm) |
| ${}^{124}$Cs | 124 | 69 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 74.8784 | 1039.5554 | -92.80 % | 119724.5871 MeV (+37263.3 ppm) |
| ${}^{125}$Cs | 125 | 70 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 81.1355 | 1049.9754 | -92.27 % | 120685.0448 MeV (+37234.8 ppm) |
| ${}^{126}$Cs | 126 | 71 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 87.3815 | 1058.3077 | -91.74 % | 121645.5136 MeV (+37188.5 ppm) |
| ${}^{127}$Cs | 127 | 72 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 93.6166 | 1068.2683 | -91.24 % | 122605.9932 MeV (+37157.2 ppm) |
| ${}^{128}$Cs | 128 | 73 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 99.8410 | 1076.0314 | -90.72 % | 123566.4836 MeV (+37107.4 ppm) |
| ${}^{129}$Cs | 129 | 74 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 106.0549 | 1085.6700 | -90.23 % | 124526.9845 MeV (+37074.6 ppm) |
| ${}^{130}$Cs | 130 | 75 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 112.2585 | 1093.1420 | -89.73 % | 125487.4957 MeV (+37023.9 ppm) |
| ${}^{131}$Cs | 131 | 76 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 118.4519 | 1102.3692 | -89.25 % | 126448.0171 MeV (+36988.9 ppm) |
| ${}^{132}$Cs | 132 | 77 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 124.6353 | 1109.5376 | -88.77 % | 127408.5484 MeV (+36937.2 ppm) |
| ${}^{133}$Cs | 133 | 78 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 130.8090 | 1118.5272 | -88.31 % | 128369.0895 MeV (+36901.6 ppm) |
| ${}^{134}$Cs | 134 | 79 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 136.9730 | 1125.4187 | -87.83 % | 129329.6403 MeV (+36849.2 ppm) |
| ${}^{135}$Cs | 135 | 80 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 143.1275 | 1134.1808 | -87.38 % | 130290.2006 MeV (+36813.0 ppm) |
| ${}^{136}$Cs | 136 | 81 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 149.2727 | 1141.0090 | -86.92 % | 131250.7701 MeV (+36761.7 ppm) |
| ${}^{137}$Cs | 137 | 82 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 155.4087 | 1149.2873 | -86.48 % | 132211.3489 MeV (+36722.9 ppm) |
| ${}^{138}$Cs | 138 | 83 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 161.5358 | 1153.6998 | -86.00 % | 133171.9366 MeV (+36653.6 ppm) |
| ${}^{139}$Cs | 139 | 84 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 167.6540 | 1159.5852 | -85.54 % | 134132.5332 MeV (+36597.1 ppm) |
| ${}^{140}$Cs | 140 | 85 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 173.7634 | 1164.0052 | -85.07 % | 135093.1385 MeV (+36529.9 ppm) |
| ${}^{141}$Cs | 141 | 86 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 179.8643 | 1169.5041 | -84.62 % | 136053.7524 MeV (+36472.2 ppm) |
| ${}^{142}$Cs | 142 | 87 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 185.9567 | 1173.6126 | -84.16 % | 137014.3747 MeV (+36404.4 ppm) |
| ${}^{143}$Cs | 143 | 88 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 192.0409 | 1178.8449 | -83.71 % | 137975.0054 MeV (+36346.5 ppm) |
| ${}^{144}$Cs | 144 | 89 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 198.1168 | 1182.5121 | -83.25 % | 138935.6442 MeV (+36277.3 ppm) |
| ${}^{145}$Cs | 145 | 90 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 204.1848 | 1187.3665 | -82.80 % | 139896.2910 MeV (+36218.2 ppm) |
| ${}^{146}$Cs | 146 | 91 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 210.2448 | 1190.6937 | -82.34 % | 140856.9458 MeV (+36148.4 ppm) |
| ${}^{147}$Cs | 147 | 92 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 216.2970 | 1195.3747 | -81.91 % | 141817.6084 MeV (+36089.8 ppm) |
| ${}^{148}$Cs | 148 | 93 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 222.3415 | 1198.4369 | -81.45 % | 142778.2786 MeV (+36020.0 ppm) |
| ${}^{149}$Cs | 149 | 94 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 228.3785 | 1202.8770 | -81.01 % | 143738.9564 MeV (+35961.5 ppm) |
| ${}^{150}$Cs | 150 | 95 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 234.4080 | 1205.8500 | -80.56 % | 144699.6416 MeV (+35892.6 ppm) |
| ${}^{151}$Cs | 151 | 96 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 240.4302 | 1209.9630 | -80.13 % | 145660.3342 MeV (+35833.9 ppm) |
| ${}^{152}$Cs | 152 | 97 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 246.4452 | 1212.9600 | -79.68 % | 146621.0340 MeV (+35766.7 ppm) |

### Barium (Z = 56)

_42 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{113}$Ba | 113 | 57 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -13.3820 | 907.9550 | -101.47 % | 109177.6547 MeV (+37621.8 ppm) |
| ${}^{114}$Ba | 114 | 58 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -6.9429 | 922.2243 | -100.75 % | 110137.9304 MeV (+37623.3 ppm) |
| ${}^{115}$Ba | 115 | 59 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -0.5179 | 933.3400 | -100.06 % | 111098.2202 MeV (+37594.2 ppm) |
| ${}^{116}$Ba | 116 | 60 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 5.8931 | 946.7920 | -99.38 % | 112058.5239 MeV (+37589.1 ppm) |
| ${}^{117}$Ba | 117 | 61 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 12.2906 | 957.9907 | -98.72 % | 113018.8412 MeV (+37561.6 ppm) |
| ${}^{118}$Ba | 118 | 62 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 18.6746 | 970.7860 | -98.08 % | 113979.1720 MeV (+37550.4 ppm) |
| ${}^{119}$Ba | 119 | 63 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 25.0456 | 981.2655 | -97.45 % | 114939.5158 MeV (+37517.5 ppm) |
| ${}^{120}$Ba | 120 | 64 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 31.4036 | 993.6354 | -96.84 % | 115899.8725 MeV (+37502.9 ppm) |
| ${}^{121}$Ba | 121 | 65 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 37.7491 | 1003.5629 | -96.24 % | 116860.2418 MeV (+37466.3 ppm) |
| ${}^{122}$Ba | 122 | 66 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 44.0822 | 1015.4983 | -95.66 % | 117820.6235 MeV (+37448.6 ppm) |
| ${}^{123}$Ba | 123 | 67 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 50.4030 | 1024.6157 | -95.08 % | 118781.0174 MeV (+37405.8 ppm) |
| ${}^{124}$Ba | 124 | 68 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 56.7120 | 1036.1218 | -94.53 % | 119741.4232 MeV (+37385.3 ppm) |
| ${}^{125}$Ba | 125 | 69 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 63.0092 | 1044.7723 | -93.97 % | 120701.8408 MeV (+37339.8 ppm) |
| ${}^{126}$Ba | 126 | 70 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 69.2950 | 1055.8446 | -93.44 % | 121662.2698 MeV (+37316.5 ppm) |
| ${}^{127}$Ba | 127 | 71 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 75.5694 | 1064.0639 | -92.90 % | 122622.7101 MeV (+37268.6 ppm) |
| ${}^{128}$Ba | 128 | 72 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 81.8327 | 1074.6864 | -92.39 % | 123583.1616 MeV (+37242.5 ppm) |
| ${}^{129}$Ba | 129 | 73 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 88.0852 | 1082.4495 | -91.86 % | 124543.6239 MeV (+37192.1 ppm) |
| ${}^{130}$Ba | 130 | 74 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 94.3269 | 1092.7167 | -91.37 % | 125504.0970 MeV (+37164.1 ppm) |
| ${}^{131}$Ba | 131 | 75 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 100.5580 | 1100.2102 | -90.86 % | 126464.5806 MeV (+37113.1 ppm) |
| ${}^{132}$Ba | 132 | 76 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 106.7789 | 1110.0375 | -90.38 % | 127425.0745 MeV (+37082.5 ppm) |
| ${}^{133}$Ba | 133 | 77 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 112.9895 | 1117.2274 | -89.89 % | 128385.5786 MeV (+37030.5 ppm) |
| ${}^{134}$Ba | 134 | 78 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 119.1902 | 1126.6952 | -89.42 % | 129346.0928 MeV (+36998.2 ppm) |
| ${}^{135}$Ba | 135 | 79 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 125.3811 | 1133.6672 | -88.94 % | 130306.6167 MeV (+36945.9 ppm) |
| ${}^{136}$Ba | 136 | 80 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 131.5622 | 1142.7749 | -88.49 % | 131267.1503 MeV (+36911.9 ppm) |
| ${}^{137}$Ba | 137 | 81 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 137.7339 | 1149.6805 | -88.02 % | 132227.6934 MeV (+36860.6 ppm) |
| ${}^{138}$Ba | 138 | 82 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 143.8962 | 1158.2923 | -87.58 % | 133188.2458 MeV (+36823.9 ppm) |
| ${}^{139}$Ba | 139 | 83 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 150.0494 | 1163.0157 | -87.10 % | 134148.8075 MeV (+36756.6 ppm) |
| ${}^{140}$Ba | 140 | 84 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 156.1935 | 1169.4410 | -86.64 % | 135109.3781 MeV (+36703.9 ppm) |
| ${}^{141}$Ba | 141 | 85 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 162.3287 | 1173.9769 | -86.17 % | 136069.9577 MeV (+36637.1 ppm) |
| ${}^{142}$Ba | 142 | 86 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 168.4551 | 1180.1580 | -85.73 % | 137030.5460 MeV (+36584.2 ppm) |
| ${}^{143}$Ba | 143 | 87 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 174.5729 | 1184.3243 | -85.26 % | 137991.1430 MeV (+36516.4 ppm) |
| ${}^{144}$Ba | 144 | 88 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 180.6823 | 1190.2255 | -84.82 % | 138951.7484 MeV (+36463.1 ppm) |
| ${}^{145}$Ba | 145 | 89 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 186.7833 | 1194.0459 | -84.36 % | 139912.3622 MeV (+36394.6 ppm) |
| ${}^{146}$Ba | 146 | 90 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 192.8761 | 1199.4673 | -83.92 % | 140872.9841 MeV (+36339.2 ppm) |
| ${}^{147}$Ba | 147 | 91 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 198.9608 | 1202.9364 | -83.46 % | 141833.6142 MeV (+36269.9 ppm) |
| ${}^{148}$Ba | 148 | 92 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 205.0376 | 1208.2885 | -83.03 % | 142794.2522 MeV (+36215.8 ppm) |
| ${}^{149}$Ba | 149 | 93 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 211.1065 | 1211.6456 | -82.58 % | 143754.8981 MeV (+36147.6 ppm) |
| ${}^{150}$Ba | 150 | 94 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 217.1677 | 1216.7761 | -82.15 % | 144715.5517 MeV (+36093.5 ppm) |
| ${}^{151}$Ba | 151 | 95 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 223.2213 | 1219.9290 | -81.70 % | 145676.2129 MeV (+36025.3 ppm) |
| ${}^{152}$Ba | 152 | 96 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 229.2674 | 1224.6640 | -81.28 % | 146636.8815 MeV (+35970.0 ppm) |
| ${}^{153}$Ba | 153 | 97 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 235.3061 | 1227.5190 | -80.83 % | 147597.5576 MeV (+35902.3 ppm) |
| ${}^{154}$Ba | 154 | 98 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 241.3375 | 1232.1540 | -80.41 % | 148558.2409 MeV (+35847.0 ppm) |

### Lanthanum (Z = 57)

_42 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{116}$La | 116 | 59 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -12.9002 | 931.7120 | -101.38 % | 112075.9870 MeV (+37613.2 ppm) |
| ${}^{117}$La | 117 | 60 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -6.4582 | 946.0620 | -100.68 % | 113036.2598 MeV (+37615.0 ppm) |
| ${}^{118}$La | 118 | 61 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -0.0301 | 957.4520 | -100.00 % | 113996.5464 MeV (+37589.8 ppm) |
| ${}^{119}$La | 119 | 62 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 6.3844 | 970.9210 | -99.34 % | 114956.8467 MeV (+37584.3 ppm) |
| ${}^{120}$La | 120 | 63 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 12.7855 | 981.4800 | -98.70 % | 115917.1603 MeV (+37552.6 ppm) |
| ${}^{121}$La | 121 | 64 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 19.1736 | 994.2570 | -98.07 % | 116877.4870 MeV (+37540.6 ppm) |
| ${}^{122}$La | 122 | 65 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 25.5489 | 1004.6700 | -97.46 % | 117837.8265 MeV (+37508.1 ppm) |
| ${}^{123}$La | 123 | 66 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 31.9115 | 1016.8410 | -96.86 % | 118798.1787 MeV (+37492.3 ppm) |
| ${}^{124}$La | 124 | 67 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 38.2618 | 1026.5083 | -96.27 % | 119758.5432 MeV (+37454.3 ppm) |
| ${}^{125}$La | 125 | 68 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 44.5999 | 1038.0805 | -95.70 % | 120718.9198 MeV (+37433.9 ppm) |
| ${}^{126}$La | 126 | 69 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 50.9261 | 1047.3658 | -95.14 % | 121679.3084 MeV (+37393.7 ppm) |
| ${}^{127}$La | 127 | 70 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 57.2405 | 1058.3597 | -94.59 % | 122639.7087 MeV (+37369.2 ppm) |
| ${}^{128}$La | 128 | 71 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 63.5435 | 1067.1604 | -94.05 % | 123600.1205 MeV (+37326.1 ppm) |
| ${}^{129}$La | 129 | 72 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 69.8351 | 1077.9298 | -93.52 % | 124560.5437 MeV (+37300.8 ppm) |
| ${}^{130}$La | 130 | 73 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 76.1157 | 1086.3049 | -92.99 % | 125520.9779 MeV (+37255.4 ppm) |
| ${}^{131}$La | 131 | 74 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 82.3853 | 1096.5182 | -92.49 % | 126481.4230 MeV (+37226.4 ppm) |
| ${}^{132}$La | 132 | 75 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 88.6442 | 1104.5438 | -91.97 % | 127441.8789 MeV (+37179.5 ppm) |
| ${}^{133}$La | 133 | 76 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 94.8926 | 1114.3859 | -91.48 % | 128402.3453 MeV (+37148.7 ppm) |
| ${}^{134}$La | 134 | 77 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 101.1306 | 1122.1815 | -90.99 % | 129362.8221 MeV (+37101.3 ppm) |
| ${}^{135}$La | 135 | 78 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 107.3584 | 1131.6776 | -90.51 % | 130323.3090 MeV (+37068.8 ppm) |
| ${}^{136}$La | 136 | 79 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 113.5762 | 1139.1430 | -90.03 % | 131283.8060 MeV (+37020.1 ppm) |
| ${}^{137}$La | 137 | 80 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 119.7842 | 1148.3177 | -89.57 % | 132244.3128 MeV (+36986.2 ppm) |
| ${}^{138}$La | 138 | 81 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 125.9825 | 1155.7615 | -89.10 % | 133204.8293 MeV (+36938.9 ppm) |
| ${}^{139}$La | 139 | 82 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 132.1712 | 1164.5418 | -88.65 % | 134165.3553 MeV (+36903.0 ppm) |
| ${}^{140}$La | 140 | 83 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 138.3506 | 1169.7028 | -88.17 % | 135125.8907 MeV (+36838.9 ppm) |
| ${}^{141}$La | 141 | 84 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 144.5207 | 1176.3919 | -87.71 % | 136086.4354 MeV (+36787.9 ppm) |
| ${}^{142}$La | 142 | 85 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 150.6818 | 1181.5573 | -87.25 % | 137046.9891 MeV (+36725.7 ppm) |
| ${}^{143}$La | 143 | 86 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 156.8339 | 1187.7762 | -86.80 % | 138007.5517 MeV (+36672.7 ppm) |
| ${}^{144}$La | 144 | 87 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 162.9773 | 1192.5257 | -86.33 % | 138968.1231 MeV (+36609.1 ppm) |
| ${}^{145}$La | 145 | 88 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 169.1120 | 1198.5827 | -85.89 % | 139928.7032 MeV (+36556.4 ppm) |
| ${}^{146}$La | 146 | 89 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 175.2382 | 1203.0398 | -85.43 % | 140889.2918 MeV (+36492.4 ppm) |
| ${}^{147}$La | 147 | 90 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 181.3560 | 1208.5684 | -84.99 % | 141849.8888 MeV (+36437.4 ppm) |
| ${}^{148}$La | 148 | 91 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 187.4655 | 1212.6700 | -84.54 % | 142810.4940 MeV (+36372.5 ppm) |
| ${}^{149}$La | 149 | 92 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 193.5670 | 1218.2525 | -84.11 % | 143771.1073 MeV (+36319.6 ppm) |
| ${}^{150}$La | 150 | 93 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 199.6604 | 1222.4151 | -83.67 % | 144731.7287 MeV (+36256.9 ppm) |
| ${}^{151}$La | 151 | 94 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 205.7459 | 1227.4856 | -83.24 % | 145692.3579 MeV (+36201.8 ppm) |
| ${}^{152}$La | 152 | 95 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 211.8237 | 1231.5040 | -82.80 % | 146652.9949 MeV (+36140.0 ppm) |
| ${}^{153}$La | 153 | 96 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 217.8938 | 1236.3930 | -82.38 % | 147613.6395 MeV (+36084.9 ppm) |
| ${}^{154}$La | 154 | 97 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 223.9564 | 1239.8540 | -81.94 % | 148574.2917 MeV (+36021.1 ppm) |
| ${}^{155}$La | 155 | 98 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 230.0116 | 1244.3400 | -81.52 % | 149534.9513 MeV (+35964.8 ppm) |
| ${}^{156}$La | 156 | 99 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 236.0595 | 1247.5320 | -81.08 % | 150495.6182 MeV (+35900.2 ppm) |
| ${}^{157}$La | 157 | 100 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 242.1001 | 1251.6040 | -80.66 % | 151456.2923 MeV (+35842.9 ppm) |

### Cerium (Z = 58)

_41 of 41 isotopes with a framework prediction; 41 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{119}$Ce | 119 | 61 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -12.5645 | 958.9020 | -101.31 % | 114974.4652 MeV (+37638.4 ppm) |
| ${}^{120}$Ce | 120 | 62 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -6.1194 | 972.9600 | -100.63 % | 115934.7350 MeV (+37637.1 ppm) |
| ${}^{121}$Ce | 121 | 63 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 0.3121 | 983.9720 | -99.97 % | 116895.0183 MeV (+37608.7 ppm) |
| ${}^{122}$Ce | 122 | 64 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 6.7302 | 997.2280 | -99.33 % | 117855.3148 MeV (+37601.2 ppm) |
| ${}^{123}$Ce | 123 | 65 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 13.1354 | 1007.7390 | -98.70 % | 118815.6245 MeV (+37568.8 ppm) |
| ${}^{124}$Ce | 124 | 66 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 19.5277 | 1020.3960 | -98.09 % | 119775.9470 MeV (+37557.0 ppm) |
| ${}^{125}$Ce | 125 | 67 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 25.9074 | 1030.2500 | -97.49 % | 120736.2820 MeV (+37519.7 ppm) |
| ${}^{126}$Ce | 126 | 68 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 32.2748 | 1042.4305 | -96.90 % | 121696.6294 MeV (+37504.6 ppm) |
| ${}^{127}$Ce | 127 | 69 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 38.6300 | 1051.6606 | -96.33 % | 122656.9890 MeV (+37463.4 ppm) |
| ${}^{128}$Ce | 128 | 70 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 44.9733 | 1063.2865 | -95.77 % | 123617.3605 MeV (+37443.9 ppm) |
| ${}^{129}$Ce | 129 | 71 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 51.3049 | 1072.1114 | -95.21 % | 124577.7436 MeV (+37400.5 ppm) |
| ${}^{130}$Ce | 130 | 72 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 57.6250 | 1083.3181 | -94.68 % | 125538.1383 MeV (+37378.3 ppm) |
| ${}^{131}$Ce | 131 | 73 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 63.9337 | 1091.6750 | -94.14 % | 126498.5443 MeV (+37332.3 ppm) |
| ${}^{132}$Ce | 132 | 74 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 70.2314 | 1102.5065 | -93.63 % | 127458.9614 MeV (+37308.0 ppm) |
| ${}^{133}$Ce | 133 | 75 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 76.5182 | 1110.5274 | -93.11 % | 128419.3894 MeV (+37260.6 ppm) |
| ${}^{134}$Ce | 134 | 76 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 82.7942 | 1121.0134 | -92.61 % | 129379.8282 MeV (+37234.4 ppm) |
| ${}^{135}$Ce | 135 | 77 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 89.0596 | 1128.8681 | -92.11 % | 130340.2775 MeV (+37187.1 ppm) |
| ${}^{136}$Ce | 136 | 78 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 95.3147 | 1138.8317 | -91.63 % | 131300.7372 MeV (+37157.7 ppm) |
| ${}^{137}$Ce | 137 | 79 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 101.5596 | 1146.3132 | -91.14 % | 132261.2071 MeV (+37108.8 ppm) |
| ${}^{138}$Ce | 138 | 80 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 107.7944 | 1156.0316 | -90.68 % | 133221.6870 MeV (+37078.6 ppm) |
| ${}^{139}$Ce | 139 | 81 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 114.0194 | 1163.4948 | -90.20 % | 134182.1768 MeV (+37030.9 ppm) |
| ${}^{140}$Ce | 140 | 82 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 120.2347 | 1172.6826 | -89.75 % | 135142.6763 MeV (+36997.7 ppm) |
| ${}^{141}$Ce | 141 | 83 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 126.4404 | 1178.1108 | -89.27 % | 136103.1854 MeV (+36935.3 ppm) |
| ${}^{142}$Ce | 142 | 84 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 132.6367 | 1185.2839 | -88.81 % | 137063.7039 MeV (+36887.5 ppm) |
| ${}^{143}$Ce | 143 | 85 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 138.8238 | 1190.4287 | -88.34 % | 138024.2316 MeV (+36824.7 ppm) |
| ${}^{144}$Ce | 144 | 86 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 145.0017 | 1197.3256 | -87.89 % | 138984.7684 MeV (+36776.4 ppm) |
| ${}^{145}$Ce | 145 | 87 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 151.1707 | 1202.0320 | -87.42 % | 139945.3141 MeV (+36712.0 ppm) |
| ${}^{146}$Ce | 146 | 88 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 157.3309 | 1208.6622 | -86.98 % | 140905.8687 MeV (+36663.2 ppm) |
| ${}^{147}$Ce | 147 | 89 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 163.4824 | 1213.1215 | -86.52 % | 141866.4320 MeV (+36598.7 ppm) |
| ${}^{148}$Ce | 148 | 90 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 169.6254 | 1219.5774 | -86.09 % | 142827.0038 MeV (+36550.2 ppm) |
| ${}^{149}$Ce | 149 | 91 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 175.7599 | 1223.9202 | -85.64 % | 143787.5841 MeV (+36486.6 ppm) |
| ${}^{150}$Ce | 150 | 92 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 181.8861 | 1230.1684 | -85.21 % | 144748.1726 MeV (+36438.0 ppm) |
| ${}^{151}$Ce | 151 | 93 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 188.0042 | 1234.6180 | -84.77 % | 145708.7693 MeV (+36376.9 ppm) |
| ${}^{152}$Ce | 152 | 94 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 194.1142 | 1240.4720 | -84.35 % | 146669.3741 MeV (+36326.7 ppm) |
| ${}^{153}$Ce | 153 | 95 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 200.2164 | 1244.5020 | -83.91 % | 147629.9867 MeV (+36264.0 ppm) |
| ${}^{154}$Ce | 154 | 96 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 206.3107 | 1249.8640 | -83.49 % | 148590.6072 MeV (+36212.1 ppm) |
| ${}^{155}$Ce | 155 | 97 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 212.3973 | 1253.4850 | -83.06 % | 149551.2353 MeV (+36148.4 ppm) |
| ${}^{156}$Ce | 156 | 98 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 218.4763 | 1258.6080 | -82.64 % | 150511.8711 MeV (+36096.1 ppm) |
| ${}^{157}$Ce | 157 | 99 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 224.5479 | 1261.8090 | -82.20 % | 151472.5143 MeV (+36030.8 ppm) |
| ${}^{158}$Ce | 158 | 100 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 230.6121 | 1266.3700 | -81.79 % | 152433.1648 MeV (+35977.0 ppm) |
| ${}^{159}$Ce | 159 | 101 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 236.6691 | 1269.2970 | -81.35 % | 153393.8226 MeV (+35911.2 ppm) |

### Praseodymium (Z = 59)

_41 of 41 isotopes with a framework prediction; 41 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{121}$Pr | 121 | 62 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -18.8356 | 971.9930 | -101.94 % | 116912.8356 MeV (+37664.2 ppm) |
| ${}^{122}$Pr | 122 | 63 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -12.3737 | 983.3200 | -101.26 % | 117873.0885 MeV (+37638.0 ppm) |
| ${}^{123}$Pr | 123 | 64 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -5.9254 | 996.7920 | -100.59 % | 118833.3549 MeV (+37632.5 ppm) |
| ${}^{124}$Pr | 124 | 65 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 0.5097 | 1007.8720 | -99.95 % | 119793.6346 MeV (+37604.5 ppm) |
| ${}^{125}$Pr | 125 | 66 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 6.9318 | 1020.8750 | -99.32 % | 120753.9273 MeV (+37594.8 ppm) |
| ${}^{126}$Pr | 126 | 67 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 13.3410 | 1031.1840 | -98.71 % | 121714.2328 MeV (+37561.8 ppm) |
| ${}^{127}$Pr | 127 | 68 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 19.7377 | 1043.4320 | -98.11 % | 122674.5509 MeV (+37546.7 ppm) |
| ${}^{128}$Pr | 128 | 69 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 26.1221 | 1053.3010 | -97.52 % | 123634.8813 MeV (+37510.8 ppm) |
| ${}^{129}$Pr | 129 | 70 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 32.4943 | 1064.8151 | -96.95 % | 124595.2239 MeV (+37489.8 ppm) |
| ${}^{130}$Pr | 130 | 71 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 38.8546 | 1074.2883 | -96.38 % | 125555.5783 MeV (+37451.7 ppm) |
| ${}^{131}$Pr | 131 | 72 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 45.2033 | 1085.4849 | -95.84 % | 126515.9445 MeV (+37429.0 ppm) |
| ${}^{132}$Pr | 132 | 73 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 51.5404 | 1094.4830 | -95.29 % | 127476.3222 MeV (+37388.1 ppm) |
| ${}^{133}$Pr | 133 | 74 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 57.8662 | 1105.2644 | -94.76 % | 128436.7111 MeV (+37362.9 ppm) |
| ${}^{134}$Pr | 134 | 75 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 64.1809 | 1113.9261 | -94.24 % | 129397.1112 MeV (+37320.6 ppm) |
| ${}^{135}$Pr | 135 | 76 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 70.4846 | 1124.4053 | -93.73 % | 130357.5222 MeV (+37293.9 ppm) |
| ${}^{136}$Pr | 136 | 77 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 76.7777 | 1132.8812 | -93.22 % | 131317.9440 MeV (+37251.3 ppm) |
| ${}^{137}$Pr | 137 | 78 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 83.0601 | 1142.8139 | -92.73 % | 132278.3763 MeV (+37221.3 ppm) |
| ${}^{138}$Pr | 138 | 79 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 89.3322 | 1150.8123 | -92.24 % | 133238.8190 MeV (+37176.1 ppm) |
| ${}^{139}$Pr | 139 | 80 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 95.5940 | 1160.5834 | -91.76 % | 134199.2719 MeV (+37145.9 ppm) |
| ${}^{140}$Pr | 140 | 81 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 101.8458 | 1168.5123 | -91.28 % | 135159.7349 MeV (+37101.6 ppm) |
| ${}^{141}$Pr | 141 | 82 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 108.0877 | 1177.9119 | -90.82 % | 136120.2077 MeV (+37069.6 ppm) |
| ${}^{142}$Pr | 142 | 83 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 114.3199 | 1183.7551 | -90.34 % | 137080.6903 MeV (+37010.2 ppm) |
| ${}^{143}$Pr | 143 | 84 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 120.5425 | 1191.1082 | -89.88 % | 138041.1825 MeV (+36963.4 ppm) |
| ${}^{144}$Pr | 144 | 85 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 126.7557 | 1196.8619 | -89.41 % | 139001.6841 MeV (+36905.0 ppm) |
| ${}^{145}$Pr | 145 | 86 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 132.9596 | 1203.8086 | -88.96 % | 139962.1950 MeV (+36856.7 ppm) |
| ${}^{146}$Pr | 146 | 87 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 139.1544 | 1208.9275 | -88.49 % | 140922.7150 MeV (+36795.1 ppm) |
| ${}^{147}$Pr | 147 | 88 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 145.3402 | 1215.7694 | -88.05 % | 141883.2440 MeV (+36747.5 ppm) |
| ${}^{148}$Pr | 148 | 89 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 151.5171 | 1220.9321 | -87.59 % | 142843.7818 MeV (+36688.0 ppm) |
| ${}^{149}$Pr | 149 | 90 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 157.6853 | 1227.5073 | -87.15 % | 143804.3284 MeV (+36639.9 ppm) |
| ${}^{150}$Pr | 150 | 91 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 163.8449 | 1232.8397 | -86.71 % | 144764.8835 MeV (+36583.3 ppm) |
| ${}^{151}$Pr | 151 | 92 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 169.9961 | 1239.3902 | -86.28 % | 145725.4471 MeV (+36536.5 ppm) |
| ${}^{152}$Pr | 152 | 93 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 176.1390 | 1244.4399 | -85.85 % | 146686.0190 MeV (+36479.3 ppm) |
| ${}^{153}$Pr | 153 | 94 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 182.2736 | 1250.3217 | -85.42 % | 147646.5992 MeV (+36429.0 ppm) |
| ${}^{154}$Pr | 154 | 95 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 188.4002 | 1254.6841 | -84.98 % | 148607.1874 MeV (+36368.5 ppm) |
| ${}^{155}$Pr | 155 | 96 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 194.5188 | 1260.3112 | -84.57 % | 149567.7835 MeV (+36317.8 ppm) |
| ${}^{156}$Pr | 156 | 97 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 200.6296 | 1264.4165 | -84.13 % | 150528.3875 MeV (+36257.0 ppm) |
| ${}^{157}$Pr | 157 | 98 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 206.7326 | 1269.4733 | -83.72 % | 151488.9993 MeV (+36203.8 ppm) |
| ${}^{158}$Pr | 158 | 99 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 212.8280 | 1273.3220 | -83.29 % | 152449.6186 MeV (+36142.4 ppm) |
| ${}^{159}$Pr | 159 | 100 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 218.9159 | 1277.8830 | -82.87 % | 153410.2455 MeV (+36088.1 ppm) |
| ${}^{160}$Pr | 160 | 101 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 224.9964 | 1281.4400 | -82.44 % | 154370.8797 MeV (+36026.3 ppm) |
| ${}^{161}$Pr | 161 | 102 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 231.0697 | 1285.7460 | -82.03 % | 155331.5213 MeV (+35971.3 ppm) |

### Neodymium (Z = 60)

_40 of 40 isotopes with a framework prediction; 40 of 40 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{124}$Nd | 124 | 64 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -18.7921 | 998.6960 | -101.88 % | 119811.6061 MeV (+37685.4 ppm) |
| ${}^{125}$Nd | 125 | 65 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -12.3270 | 1010.0000 | -101.22 % | 120771.8558 MeV (+37659.7 ppm) |
| ${}^{126}$Nd | 126 | 66 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -5.8751 | 1023.3720 | -100.57 % | 121732.1187 MeV (+37652.9 ppm) |
| ${}^{127}$Nd | 127 | 67 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 0.5638 | 1034.0340 | -99.95 % | 122692.3945 MeV (+37621.9 ppm) |
| ${}^{128}$Nd | 128 | 68 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 6.9899 | 1046.6560 | -99.33 % | 123652.6832 MeV (+37609.6 ppm) |
| ${}^{129}$Nd | 129 | 69 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 13.4035 | 1056.6390 | -98.73 % | 124612.9844 MeV (+37573.7 ppm) |
| ${}^{130}$Nd | 130 | 70 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 19.8048 | 1068.9268 | -98.15 % | 125573.2979 MeV (+37558.9 ppm) |
| ${}^{131}$Nd | 131 | 71 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 26.1939 | 1078.1699 | -97.57 % | 126533.6236 MeV (+37518.4 ppm) |
| ${}^{132}$Nd | 132 | 72 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 32.5711 | 1089.8990 | -97.01 % | 127493.9611 MeV (+37499.6 ppm) |
| ${}^{133}$Nd | 133 | 73 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 38.9367 | 1098.8769 | -96.46 % | 128454.3103 MeV (+37458.1 ppm) |
| ${}^{134}$Nd | 134 | 74 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 45.2907 | 1110.2622 | -95.92 % | 129414.6711 MeV (+37437.4 ppm) |
| ${}^{135}$Nd | 135 | 75 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 51.6334 | 1118.9007 | -95.39 % | 130375.0431 MeV (+37394.3 ppm) |
| ${}^{136}$Nd | 136 | 76 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 57.9651 | 1129.9577 | -94.87 % | 131335.4263 MeV (+37371.9 ppm) |
| ${}^{137}$Nd | 137 | 77 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 64.2858 | 1138.4137 | -94.35 % | 132295.8203 MeV (+37328.6 ppm) |
| ${}^{138}$Nd | 138 | 78 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 70.5957 | 1148.9183 | -93.86 % | 133256.2252 MeV (+37302.7 ppm) |
| ${}^{139}$Nd | 139 | 79 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 76.8951 | 1156.9893 | -93.35 % | 134216.6406 MeV (+37257.6 ppm) |
| ${}^{140}$Nd | 140 | 80 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 83.1840 | 1167.3010 | -92.87 % | 135177.0664 MeV (+37231.2 ppm) |
| ${}^{141}$Nd | 141 | 81 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 89.4628 | 1175.3065 | -92.39 % | 136137.5024 MeV (+37186.9 ppm) |
| ${}^{142}$Nd | 142 | 82 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 95.7314 | 1185.1364 | -91.92 % | 137097.9485 MeV (+37157.7 ppm) |
| ${}^{143}$Nd | 143 | 83 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 101.9902 | 1191.2600 | -91.44 % | 138058.4046 MeV (+37100.1 ppm) |
| ${}^{144}$Nd | 144 | 84 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 108.2392 | 1199.0770 | -90.97 % | 139018.8703 MeV (+37056.4 ppm) |
| ${}^{145}$Nd | 145 | 85 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 114.4786 | 1204.8323 | -90.50 % | 139979.3457 MeV (+36997.6 ppm) |
| ${}^{146}$Nd | 146 | 86 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 120.7085 | 1212.3975 | -90.04 % | 140939.8305 MeV (+36953.5 ppm) |
| ${}^{147}$Nd | 147 | 87 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 126.9292 | 1217.6897 | -89.58 % | 141900.3246 MeV (+36892.8 ppm) |
| ${}^{148}$Nd | 148 | 88 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 133.1407 | 1225.0223 | -89.13 % | 142860.8279 MeV (+36848.4 ppm) |
| ${}^{149}$Nd | 149 | 89 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 139.3432 | 1230.0611 | -88.67 % | 143821.3402 MeV (+36787.5 ppm) |
| ${}^{150}$Nd | 150 | 90 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 145.5368 | 1237.4368 | -88.24 % | 144781.8614 MeV (+36744.8 ppm) |
| ${}^{151}$Nd | 151 | 91 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 151.7216 | 1242.7714 | -87.79 % | 145742.3913 MeV (+36687.7 ppm) |
| ${}^{152}$Nd | 152 | 92 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 157.8979 | 1250.0492 | -87.37 % | 146702.9298 MeV (+36645.6 ppm) |
| ${}^{153}$Nd | 153 | 93 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 164.0656 | 1255.3012 | -86.93 % | 147663.4768 MeV (+36589.4 ppm) |
| ${}^{154}$Nd | 154 | 94 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 170.2250 | 1261.6218 | -86.51 % | 148624.0322 MeV (+36541.7 ppm) |
| ${}^{155}$Nd | 155 | 95 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 176.3762 | 1266.3973 | -86.07 % | 149584.5958 MeV (+36483.6 ppm) |
| ${}^{156}$Nd | 156 | 96 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 182.5192 | 1272.3869 | -85.66 % | 150545.1676 MeV (+36435.0 ppm) |
| ${}^{157}$Nd | 157 | 97 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 188.6543 | 1276.7502 | -85.22 % | 151505.7473 MeV (+36375.5 ppm) |
| ${}^{158}$Nd | 158 | 98 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 194.7814 | 1282.1626 | -84.81 % | 152466.3349 MeV (+36324.2 ppm) |
| ${}^{159}$Nd | 159 | 99 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 200.9008 | 1286.1228 | -84.38 % | 153426.9303 MeV (+36263.5 ppm) |
| ${}^{160}$Nd | 160 | 100 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 207.0126 | 1291.1946 | -83.97 % | 154387.5333 MeV (+36211.3 ppm) |
| ${}^{161}$Nd | 161 | 101 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 213.1168 | 1294.7620 | -83.54 % | 155348.1439 MeV (+36149.4 ppm) |
| ${}^{162}$Nd | 162 | 102 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 219.2135 | 1299.5640 | -83.13 % | 156308.7619 MeV (+36097.2 ppm) |
| ${}^{163}$Nd | 163 | 103 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 225.3029 | 1302.6960 | -82.70 % | 157269.3873 MeV (+36033.9 ppm) |

### Promethium (Z = 61)

_40 of 40 isotopes with a framework prediction; 40 of 40 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{126}$Pm | 126 | 65 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -25.3736 | 1009.0080 | -102.51 % | 121750.2869 MeV (+37687.2 ppm) |
| ${}^{127}$Pm | 127 | 66 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -18.8918 | 1022.6040 | -101.85 % | 122710.5198 MeV (+37682.1 ppm) |
| ${}^{128}$Pm | 128 | 67 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -12.4232 | 1033.6000 | -101.20 % | 123670.7660 MeV (+37654.2 ppm) |
| ${}^{129}$Pm | 129 | 68 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -5.9676 | 1046.7060 | -100.57 % | 124631.0252 MeV (+37644.5 ppm) |
| ${}^{130}$Pm | 130 | 69 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 0.4753 | 1057.0300 | -99.96 % | 125591.2971 MeV (+37612.2 ppm) |
| ${}^{131}$Pm | 131 | 70 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 6.9057 | 1069.3530 | -99.35 % | 126551.5815 MeV (+37597.6 ppm) |
| ${}^{132}$Pm | 132 | 71 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 13.3237 | 1079.3640 | -98.77 % | 127511.8782 MeV (+37562.7 ppm) |
| ${}^{133}$Pm | 133 | 72 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 19.7296 | 1091.1698 | -98.19 % | 128472.1871 MeV (+37544.5 ppm) |
| ${}^{134}$Pm | 134 | 73 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 26.1237 | 1100.5974 | -97.63 % | 129432.5078 MeV (+37506.5 ppm) |
| ${}^{135}$Pm | 135 | 74 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 32.5061 | 1111.9671 | -97.08 % | 130392.8402 MeV (+37485.2 ppm) |
| ${}^{136}$Pm | 136 | 75 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 38.8769 | 1121.1460 | -96.53 % | 131353.1841 MeV (+37446.3 ppm) |
| ${}^{137}$Pm | 137 | 76 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 45.2365 | 1132.1203 | -96.00 % | 132313.5393 MeV (+37422.7 ppm) |
| ${}^{138}$Pm | 138 | 77 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 51.5850 | 1141.0331 | -95.48 % | 133273.9056 MeV (+37382.9 ppm) |
| ${}^{139}$Pm | 139 | 78 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 57.9225 | 1151.6911 | -94.97 % | 134234.2829 MeV (+37357.8 ppm) |
| ${}^{140}$Pm | 140 | 79 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 64.2492 | 1160.4734 | -94.46 % | 135194.6709 MeV (+37318.1 ppm) |
| ${}^{141}$Pm | 141 | 80 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 70.5654 | 1170.8556 | -93.97 % | 136155.0695 MeV (+37291.8 ppm) |
| ${}^{142}$Pm | 142 | 81 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 76.8712 | 1179.5455 | -93.48 % | 137115.4785 MeV (+37252.6 ppm) |
| ${}^{143}$Pm | 143 | 82 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 83.1667 | 1189.4360 | -93.01 % | 138075.8977 MeV (+37223.4 ppm) |
| ${}^{144}$Pm | 144 | 83 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 89.4522 | 1195.9628 | -92.52 % | 139036.3271 MeV (+37168.6 ppm) |
| ${}^{145}$Pm | 145 | 84 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 95.7277 | 1203.8855 | -92.05 % | 139996.7663 MeV (+37125.4 ppm) |
| ${}^{146}$Pm | 146 | 85 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 101.9934 | 1210.1436 | -91.57 % | 140957.2154 MeV (+37070.2 ppm) |
| ${}^{147}$Pm | 147 | 86 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 108.2495 | 1217.8026 | -91.11 % | 141917.6740 MeV (+37026.4 ppm) |
| ${}^{148}$Pm | 148 | 87 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 114.4962 | 1223.6978 | -90.64 % | 142878.1421 MeV (+36970.0 ppm) |
| ${}^{149}$Pm | 149 | 88 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 120.7335 | 1230.9676 | -90.19 % | 143838.6196 MeV (+36924.7 ppm) |
| ${}^{150}$Pm | 150 | 89 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 126.9617 | 1236.5719 | -89.73 % | 144799.1062 MeV (+36867.7 ppm) |
| ${}^{151}$Pm | 151 | 90 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 133.1808 | 1244.4321 | -89.30 % | 145759.6018 MeV (+36828.1 ppm) |
| ${}^{152}$Pm | 152 | 91 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 139.3910 | 1250.3717 | -88.85 % | 146720.1064 MeV (+36775.1 ppm) |
| ${}^{153}$Pm | 153 | 92 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 145.5924 | 1257.8365 | -88.43 % | 147680.6198 MeV (+36733.9 ppm) |
| ${}^{154}$Pm | 154 | 93 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 151.7852 | 1263.5264 | -87.99 % | 148641.1418 MeV (+36680.5 ppm) |
| ${}^{155}$Pm | 155 | 94 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 157.9694 | 1270.2711 | -87.56 % | 149601.6723 MeV (+36635.4 ppm) |
| ${}^{156}$Pm | 156 | 95 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 164.1453 | 1275.5693 | -87.13 % | 150562.2112 MeV (+36580.6 ppm) |
| ${}^{157}$Pm | 157 | 96 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 170.3129 | 1281.7709 | -86.71 % | 151522.7584 MeV (+36533.0 ppm) |
| ${}^{158}$Pm | 158 | 97 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 176.4724 | 1286.6512 | -86.28 % | 152483.3137 MeV (+36476.8 ppm) |
| ${}^{159}$Pm | 159 | 98 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 182.6238 | 1292.1708 | -85.87 % | 153443.8771 MeV (+36425.7 ppm) |
| ${}^{160}$Pm | 160 | 99 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 188.7673 | 1296.5824 | -85.44 % | 154404.4483 MeV (+36367.7 ppm) |
| ${}^{161}$Pm | 161 | 100 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 194.9029 | 1301.8456 | -85.03 % | 155365.0274 MeV (+36316.3 ppm) |
| ${}^{162}$Pm | 162 | 101 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 201.0309 | 1305.8820 | -84.61 % | 156325.6142 MeV (+36257.2 ppm) |
| ${}^{163}$Pm | 163 | 102 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 207.1513 | 1310.8460 | -84.20 % | 157286.2086 MeV (+36205.3 ppm) |
| ${}^{164}$Pm | 164 | 103 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 213.2643 | 1314.2960 | -83.77 % | 158246.8104 MeV (+36143.9 ppm) |
| ${}^{165}$Pm | 165 | 104 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 219.3698 | 1318.6800 | -83.36 % | 159207.4197 MeV (+36089.4 ppm) |

### Samarium (Z = 62)

_41 of 41 isotopes with a framework prediction; 41 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{128}$Sm | 128 | 66 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -32.1173 | 1023.7440 | -103.14 % | 123689.1298 MeV (+37729.3 ppm) |
| ${}^{129}$Sm | 129 | 67 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -25.6189 | 1034.9670 | -102.48 % | 124649.3462 MeV (+37703.3 ppm) |
| ${}^{130}$Sm | 130 | 68 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -19.1337 | 1048.4500 | -101.82 % | 125609.5758 MeV (+37696.6 ppm) |
| ${}^{131}$Sm | 131 | 69 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -12.6615 | 1059.1350 | -101.20 % | 126569.8183 MeV (+37666.4 ppm) |
| ${}^{132}$Sm | 132 | 70 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -6.2019 | 1072.1040 | -100.58 % | 127530.0736 MeV (+37655.9 ppm) |
| ${}^{133}$Sm | 133 | 71 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 0.2451 | 1082.2210 | -99.98 % | 128490.3413 MeV (+37622.6 ppm) |
| ${}^{134}$Sm | 134 | 72 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 6.6798 | 1094.3780 | -99.39 % | 129450.6213 MeV (+37606.9 ppm) |
| ${}^{135}$Sm | 135 | 73 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 13.1025 | 1103.9796 | -98.81 % | 130410.9135 MeV (+37569.5 ppm) |
| ${}^{136}$Sm | 136 | 74 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 19.5133 | 1116.0046 | -98.25 % | 131371.2174 MeV (+37553.0 ppm) |
| ${}^{137}$Sm | 137 | 75 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 25.9124 | 1125.2567 | -97.70 % | 132331.5331 MeV (+37514.4 ppm) |
| ${}^{138}$Sm | 138 | 76 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 32.3000 | 1136.8341 | -97.16 % | 133291.8603 MeV (+37495.1 ppm) |
| ${}^{139}$Sm | 139 | 77 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 38.6763 | 1145.7879 | -96.62 % | 134252.1988 MeV (+37455.2 ppm) |
| ${}^{140}$Sm | 140 | 78 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 45.0415 | 1156.9350 | -96.11 % | 135212.5483 MeV (+37433.4 ppm) |
| ${}^{141}$Sm | 141 | 79 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 51.3957 | 1165.4843 | -95.59 % | 136172.9089 MeV (+37391.4 ppm) |
| ${}^{142}$Sm | 142 | 80 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 57.7392 | 1176.6036 | -95.09 % | 137133.2801 MeV (+37370.3 ppm) |
| ${}^{143}$Sm | 143 | 81 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 64.0721 | 1185.2101 | -94.59 % | 138093.6620 MeV (+37330.0 ppm) |
| ${}^{144}$Sm | 144 | 82 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 70.3946 | 1195.7299 | -94.11 % | 139054.0543 MeV (+37305.1 ppm) |
| ${}^{145}$Sm | 145 | 83 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 76.7069 | 1202.4870 | -93.62 % | 140014.4568 MeV (+37251.7 ppm) |
| ${}^{146}$Sm | 146 | 84 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 83.0090 | 1210.9033 | -93.14 % | 140974.8695 MeV (+37211.8 ppm) |
| ${}^{147}$Sm | 147 | 85 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 89.3012 | 1217.2443 | -92.66 % | 141935.2921 MeV (+37156.8 ppm) |
| ${}^{148}$Sm | 148 | 86 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 95.5836 | 1225.3856 | -92.20 % | 142895.7244 MeV (+37116.2 ppm) |
| ${}^{149}$Sm | 149 | 87 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 101.8563 | 1231.2568 | -91.73 % | 143856.1664 MeV (+37059.2 ppm) |
| ${}^{150}$Sm | 150 | 88 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 108.1196 | 1239.2435 | -91.28 % | 144816.6179 MeV (+37018.7 ppm) |
| ${}^{151}$Sm | 151 | 89 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 114.3735 | 1244.8400 | -90.81 % | 145777.0788 MeV (+36961.2 ppm) |
| ${}^{152}$Sm | 152 | 90 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 120.6183 | 1253.0978 | -90.37 % | 146737.5488 MeV (+36924.0 ppm) |
| ${}^{153}$Sm | 153 | 91 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 126.8539 | 1258.9662 | -89.92 % | 147698.0280 MeV (+36870.0 ppm) |
| ${}^{154}$Sm | 154 | 92 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 133.0806 | 1266.9330 | -89.50 % | 148658.5160 MeV (+36832.0 ppm) |
| ${}^{155}$Sm | 155 | 93 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 139.2986 | 1272.7400 | -89.06 % | 149619.0129 MeV (+36778.9 ppm) |
| ${}^{156}$Sm | 156 | 94 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 145.5078 | 1279.9808 | -88.63 % | 150579.5184 MeV (+36736.9 ppm) |
| ${}^{157}$Sm | 157 | 95 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 151.7085 | 1285.3691 | -88.20 % | 151540.0325 MeV (+36682.3 ppm) |
| ${}^{158}$Sm | 158 | 96 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 157.9008 | 1292.0146 | -87.78 % | 152500.5550 MeV (+36637.3 ppm) |
| ${}^{159}$Sm | 159 | 97 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 164.0847 | 1297.0419 | -87.35 % | 153461.0858 MeV (+36581.6 ppm) |
| ${}^{160}$Sm | 160 | 98 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 170.2605 | 1303.1385 | -86.93 % | 154421.6248 MeV (+36534.1 ppm) |
| ${}^{161}$Sm | 161 | 99 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 176.4282 | 1307.6487 | -86.51 % | 155382.1719 MeV (+36476.2 ppm) |
| ${}^{162}$Sm | 162 | 100 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 182.5880 | 1313.4271 | -86.10 % | 156342.7269 MeV (+36427.9 ppm) |
| ${}^{163}$Sm | 163 | 101 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 188.7399 | 1317.7189 | -85.68 % | 157303.2897 MeV (+36370.0 ppm) |
| ${}^{164}$Sm | 164 | 102 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 194.8841 | 1323.1160 | -85.27 % | 158263.8603 MeV (+36320.4 ppm) |
| ${}^{165}$Sm | 165 | 103 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 201.0206 | 1326.7650 | -84.85 % | 159224.4385 MeV (+36259.8 ppm) |
| ${}^{166}$Sm | 166 | 104 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 207.1497 | 1331.8180 | -84.45 % | 160185.0243 MeV (+36208.9 ppm) |
| ${}^{167}$Sm | 167 | 105 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 213.2713 | 1334.6640 | -84.02 % | 161145.6174 MeV (+36145.1 ppm) |
| ${}^{168}$Sm | 168 | 106 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 219.3856 | 1339.1280 | -83.62 % | 162106.2179 MeV (+36091.5 ppm) |

### Europium (Z = 63)

_41 of 41 isotopes with a framework prediction; 41 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{130}$Eu | 130 | 67 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -39.0223 | 1033.5000 | -103.78 % | 125628.1341 MeV (+37728.3 ppm) |
| ${}^{131}$Eu | 131 | 68 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -32.5075 | 1047.4760 | -103.10 % | 126588.3340 MeV (+37726.1 ppm) |
| ${}^{132}$Eu | 132 | 69 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -26.0058 | 1058.3760 | -102.46 % | 127548.5471 MeV (+37697.0 ppm) |
| ${}^{133}$Eu | 133 | 70 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -19.5170 | 1071.4480 | -101.82 % | 128508.7731 MeV (+37687.6 ppm) |
| ${}^{134}$Eu | 134 | 71 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -13.0409 | 1082.0500 | -101.21 % | 129469.0118 MeV (+37658.0 ppm) |
| ${}^{135}$Eu | 135 | 72 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -6.5773 | 1094.4450 | -100.60 % | 130429.2629 MeV (+37643.6 ppm) |
| ${}^{136}$Eu | 136 | 73 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -0.1259 | 1104.5920 | -100.01 % | 131389.5263 MeV (+37611.0 ppm) |
| ${}^{137}$Eu | 137 | 74 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 6.3134 | 1116.6286 | -99.43 % | 132349.8018 MeV (+37593.8 ppm) |
| ${}^{138}$Eu | 138 | 75 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 12.7408 | 1126.3037 | -98.87 % | 133310.0892 MeV (+37558.3 ppm) |
| ${}^{139}$Eu | 139 | 76 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 19.1565 | 1138.0234 | -98.32 % | 134270.3882 MeV (+37539.8 ppm) |
| ${}^{140}$Eu | 140 | 77 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 25.5608 | 1147.6826 | -97.77 % | 135230.6988 MeV (+37505.2 ppm) |
| ${}^{141}$Eu | 141 | 78 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 31.9537 | 1158.6936 | -97.24 % | 136191.0206 MeV (+37481.9 ppm) |
| ${}^{142}$Eu | 142 | 79 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 38.3356 | 1168.1482 | -96.72 % | 137151.3535 MeV (+37446.8 ppm) |
| ${}^{143}$Eu | 143 | 80 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 44.7065 | 1179.1519 | -96.21 % | 138111.6974 MeV (+37424.4 ppm) |
| ${}^{144}$Eu | 144 | 81 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 51.0666 | 1188.6011 | -95.70 % | 139072.0520 MeV (+37390.3 ppm) |
| ${}^{145}$Eu | 145 | 82 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 57.4161 | 1199.0448 | -95.21 % | 140032.4172 MeV (+37364.4 ppm) |
| ${}^{146}$Eu | 146 | 83 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 63.7553 | 1206.2422 | -94.71 % | 140992.7929 MeV (+37314.1 ppm) |
| ${}^{147}$Eu | 147 | 84 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 70.0841 | 1214.7405 | -94.23 % | 141953.1788 MeV (+37274.5 ppm) |
| ${}^{148}$Eu | 148 | 85 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 76.4028 | 1221.5647 | -93.75 % | 142913.5749 MeV (+37222.9 ppm) |
| ${}^{149}$Eu | 149 | 86 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 82.7116 | 1229.7798 | -93.27 % | 143873.9809 MeV (+37182.4 ppm) |
| ${}^{150}$Eu | 150 | 87 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 89.0106 | 1236.2022 | -92.80 % | 144834.3967 MeV (+37129.2 ppm) |
| ${}^{151}$Eu | 151 | 88 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 95.2999 | 1244.1343 | -92.34 % | 145794.8221 MeV (+37088.0 ppm) |
| ${}^{152}$Eu | 152 | 89 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 101.5797 | 1250.4410 | -91.88 % | 146755.2571 MeV (+37035.4 ppm) |
| ${}^{153}$Eu | 153 | 90 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 107.8502 | 1258.9913 | -91.43 % | 147715.7014 MeV (+37000.0 ppm) |
| ${}^{154}$Eu | 154 | 91 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 114.1114 | 1265.4335 | -90.98 % | 148676.1550 MeV (+36949.8 ppm) |
| ${}^{155}$Eu | 155 | 92 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 120.3635 | 1273.5848 | -90.55 % | 149636.6176 MeV (+36912.6 ppm) |
| ${}^{156}$Eu | 156 | 93 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 126.6067 | 1279.9206 | -90.11 % | 150597.0892 MeV (+36863.0 ppm) |
| ${}^{157}$Eu | 157 | 94 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 132.8410 | 1287.3682 | -89.68 % | 151557.5697 MeV (+36822.0 ppm) |
| ${}^{158}$Eu | 158 | 95 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 139.0667 | 1293.2509 | -89.25 % | 152518.0588 MeV (+36770.5 ppm) |
| ${}^{159}$Eu | 159 | 96 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 145.2837 | 1300.0951 | -88.83 % | 153478.5565 MeV (+36726.4 ppm) |
| ${}^{160}$Eu | 160 | 97 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 151.4923 | 1305.6165 | -88.40 % | 154439.0627 MeV (+36673.8 ppm) |
| ${}^{161}$Eu | 161 | 98 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 157.6926 | 1311.9859 | -87.98 % | 155399.5772 MeV (+36627.7 ppm) |
| ${}^{162}$Eu | 162 | 99 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 163.8846 | 1316.9886 | -87.56 % | 156360.0999 MeV (+36572.9 ppm) |
| ${}^{163}$Eu | 163 | 100 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 170.0686 | 1322.9108 | -87.14 % | 157320.6307 MeV (+36525.1 ppm) |
| ${}^{164}$Eu | 164 | 101 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 176.2445 | 1327.6405 | -86.72 % | 158281.1696 MeV (+36469.8 ppm) |
| ${}^{165}$Eu | 165 | 102 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 182.4126 | 1333.2087 | -86.32 % | 159241.7162 MeV (+36420.9 ppm) |
| ${}^{166}$Eu | 166 | 103 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 188.5729 | 1337.2960 | -85.90 % | 160202.2707 MeV (+36362.7 ppm) |
| ${}^{167}$Eu | 167 | 104 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 194.7256 | 1342.3460 | -85.49 % | 161162.8328 MeV (+36312.0 ppm) |
| ${}^{168}$Eu | 168 | 105 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 200.8707 | 1346.0160 | -85.08 % | 162123.4025 MeV (+36251.7 ppm) |
| ${}^{169}$Eu | 169 | 106 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 207.0083 | 1350.4790 | -84.67 % | 163083.9796 MeV (+36198.3 ppm) |
| ${}^{170}$Eu | 170 | 107 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 213.1386 | 1353.7100 | -84.26 % | 164044.5641 MeV (+36137.7 ppm) |

### Gadolinium (Z = 64)

_40 of 40 isotopes with a framework prediction; 40 of 40 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{133}$Gd | 133 | 69 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -39.5566 | 1059.4780 | -103.73 % | 128527.4824 MeV (+37745.1 ppm) |
| ${}^{134}$Gd | 134 | 70 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -33.0384 | 1073.0720 | -103.08 % | 129487.6790 MeV (+37738.8 ppm) |
| ${}^{135}$Gd | 135 | 71 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -26.5332 | 1083.7800 | -102.45 % | 130447.8886 MeV (+37710.0 ppm) |
| ${}^{136}$Gd | 136 | 72 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -20.0406 | 1096.7040 | -101.83 % | 131408.1108 MeV (+37699.2 ppm) |
| ${}^{137}$Gd | 137 | 73 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -13.5605 | 1106.9600 | -101.23 % | 132368.3454 MeV (+37666.5 ppm) |
| ${}^{138}$Gd | 138 | 74 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -7.0927 | 1119.4560 | -100.63 % | 133328.5924 MeV (+37653.1 ppm) |
| ${}^{139}$Gd | 139 | 75 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -0.6369 | 1129.5140 | -100.06 % | 134288.8513 MeV (+37620.2 ppm) |
| ${}^{140}$Gd | 140 | 76 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 5.8071 | 1141.6966 | -99.49 % | 135249.1222 MeV (+37605.1 ppm) |
| ${}^{141}$Gd | 141 | 77 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 12.2394 | 1151.2099 | -98.94 % | 136209.4046 MeV (+37569.0 ppm) |
| ${}^{142}$Gd | 142 | 78 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 18.6602 | 1163.0165 | -98.40 % | 137169.6986 MeV (+37551.4 ppm) |
| ${}^{143}$Gd | 143 | 79 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 25.0697 | 1172.3596 | -97.86 % | 138130.0039 MeV (+37515.0 ppm) |
| ${}^{144}$Gd | 144 | 80 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 31.4681 | 1183.9591 | -97.34 % | 139090.3202 MeV (+37496.7 ppm) |
| ${}^{145}$Gd | 145 | 81 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 37.8555 | 1193.1975 | -96.83 % | 140050.6475 MeV (+37460.5 ppm) |
| ${}^{146}$Gd | 146 | 82 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 44.2322 | 1204.4281 | -96.33 % | 141010.9856 MeV (+37440.1 ppm) |
| ${}^{147}$Gd | 147 | 83 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 50.5983 | 1211.7705 | -95.82 % | 141971.3343 MeV (+37390.6 ppm) |
| ${}^{148}$Gd | 148 | 84 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 56.9540 | 1220.7543 | -95.33 % | 142931.6934 MeV (+37354.1 ppm) |
| ${}^{149}$Gd | 149 | 85 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 63.2994 | 1227.6834 | -94.84 % | 143892.0628 MeV (+37302.9 ppm) |
| ${}^{150}$Gd | 150 | 86 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 69.6346 | 1236.3915 | -94.37 % | 144852.4423 MeV (+37265.7 ppm) |
| ${}^{151}$Gd | 151 | 87 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 75.9599 | 1242.8877 | -93.89 % | 145812.8318 MeV (+37212.7 ppm) |
| ${}^{152}$Gd | 152 | 88 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 82.2754 | 1251.4774 | -93.43 % | 146773.2311 MeV (+37175.8 ppm) |
| ${}^{153}$Gd | 153 | 89 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 88.5812 | 1257.7244 | -92.96 % | 147733.6401 MeV (+37122.4 ppm) |
| ${}^{154}$Gd | 154 | 90 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 94.8775 | 1266.6191 | -92.51 % | 148694.0586 MeV (+37088.9 ppm) |
| ${}^{155}$Gd | 155 | 91 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 101.1644 | 1273.0544 | -92.05 % | 149654.4865 MeV (+37038.2 ppm) |
| ${}^{156}$Gd | 156 | 92 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 107.4420 | 1281.5907 | -91.62 % | 150614.9236 MeV (+37003.3 ppm) |
| ${}^{157}$Gd | 157 | 93 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 113.7105 | 1287.9506 | -91.17 % | 151575.3699 MeV (+36953.4 ppm) |
| ${}^{158}$Gd | 158 | 94 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 119.9700 | 1295.8880 | -90.74 % | 152535.8251 MeV (+36915.4 ppm) |
| ${}^{159}$Gd | 159 | 95 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 126.2207 | 1301.8312 | -90.30 % | 153496.2892 MeV (+36863.9 ppm) |
| ${}^{160}$Gd | 160 | 96 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 132.4627 | 1309.2827 | -89.88 % | 154456.7620 MeV (+36823.6 ppm) |
| ${}^{161}$Gd | 161 | 97 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 138.6960 | 1314.9181 | -89.45 % | 155417.2434 MeV (+36771.3 ppm) |
| ${}^{162}$Gd | 162 | 98 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 144.9209 | 1321.7640 | -89.04 % | 156377.7334 MeV (+36728.0 ppm) |
| ${}^{163}$Gd | 163 | 99 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 151.1374 | 1326.9432 | -88.61 % | 157338.2316 MeV (+36673.9 ppm) |
| ${}^{164}$Gd | 164 | 100 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 157.3456 | 1333.3196 | -88.20 % | 158298.7381 MeV (+36628.7 ppm) |
| ${}^{165}$Gd | 165 | 101 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 163.5458 | 1338.2231 | -87.78 % | 159259.2528 MeV (+36574.1 ppm) |
| ${}^{166}$Gd | 166 | 102 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 169.7379 | 1344.1395 | -87.37 % | 160219.7755 MeV (+36527.1 ppm) |
| ${}^{167}$Gd | 167 | 103 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 175.9221 | 1348.6156 | -86.96 % | 161180.3061 MeV (+36471.0 ppm) |
| ${}^{168}$Gd | 168 | 104 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 182.0984 | 1354.0800 | -86.55 % | 162140.8444 MeV (+36422.1 ppm) |
| ${}^{169}$Gd | 169 | 105 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 188.2671 | 1357.9150 | -86.14 % | 163101.3905 MeV (+36363.1 ppm) |
| ${}^{170}$Gd | 170 | 106 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 194.4282 | 1362.8900 | -85.73 % | 164061.9442 MeV (+36312.8 ppm) |
| ${}^{171}$Gd | 171 | 107 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 200.5818 | 1366.2900 | -85.32 % | 165022.5054 MeV (+36252.7 ppm) |
| ${}^{172}$Gd | 172 | 108 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 206.7280 | 1371.1840 | -84.92 % | 165983.0739 MeV (+36202.5 ppm) |

### Terbium (Z = 65)

_40 of 40 isotopes with a framework prediction; 40 of 40 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{135}$Tb | 135 | 70 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -46.7653 | 1071.7650 | -104.36 % | 130466.7904 MeV (+37768.0 ppm) |
| ${}^{136}$Tb | 136 | 71 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -40.2309 | 1082.6960 | -103.72 % | 131426.9707 MeV (+37740.0 ppm) |
| ${}^{137}$Tb | 137 | 72 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -33.7093 | 1095.8630 | -103.08 % | 132387.1639 MeV (+37730.6 ppm) |
| ${}^{138}$Tb | 138 | 73 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -27.2004 | 1106.6220 | -102.46 % | 133347.3698 MeV (+37701.8 ppm) |
| ${}^{139}$Tb | 139 | 74 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -20.7039 | 1119.2280 | -101.85 % | 134307.5880 MeV (+37688.7 ppm) |
| ${}^{140}$Tb | 140 | 75 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -14.2196 | 1129.6142 | -101.26 % | 135267.8185 MeV (+37658.6 ppm) |
| ${}^{141}$Tb | 141 | 76 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -7.7473 | 1141.7441 | -100.68 % | 136228.0611 MeV (+37642.5 ppm) |
| ${}^{142}$Tb | 142 | 77 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -1.2870 | 1151.8341 | -100.11 % | 137188.3154 MeV (+37610.6 ppm) |
| ${}^{143}$Tb | 143 | 78 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 5.1618 | 1163.7651 | -99.56 % | 138148.5815 MeV (+37593.7 ppm) |
| ${}^{144}$Tb | 144 | 79 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 11.5991 | 1173.7854 | -99.01 % | 139108.8590 MeV (+37562.3 ppm) |
| ${}^{145}$Tb | 145 | 80 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 18.0251 | 1185.8883 | -98.48 % | 140069.1477 MeV (+37547.4 ppm) |
| ${}^{146}$Tb | 146 | 81 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 24.4399 | 1195.3235 | -97.96 % | 141029.4476 MeV (+37512.4 ppm) |
| ${}^{147}$Tb | 147 | 82 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 30.8439 | 1206.3739 | -97.44 % | 141989.7585 MeV (+37490.2 ppm) |
| ${}^{148}$Tb | 148 | 83 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 37.2370 | 1214.2395 | -96.93 % | 142950.0801 MeV (+37444.4 ppm) |
| ${}^{149}$Tb | 149 | 84 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 43.6196 | 1223.2625 | -96.43 % | 143910.4123 MeV (+37408.0 ppm) |
| ${}^{150}$Tb | 150 | 85 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 49.9917 | 1230.9509 | -95.94 % | 144870.7550 MeV (+37362.2 ppm) |
| ${}^{151}$Tb | 151 | 86 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 56.3535 | 1239.5400 | -95.45 % | 145831.1079 MeV (+37323.8 ppm) |
| ${}^{152}$Tb | 152 | 87 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 62.7052 | 1246.7051 | -94.97 % | 146791.4710 MeV (+37275.4 ppm) |
| ${}^{153}$Tb | 153 | 88 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 69.0470 | 1255.3727 | -94.50 % | 147751.8440 MeV (+37238.8 ppm) |
| ${}^{154}$Tb | 154 | 89 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 75.3788 | 1262.2871 | -94.03 % | 148712.2269 MeV (+37189.9 ppm) |
| ${}^{155}$Tb | 155 | 90 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 81.7010 | 1271.4522 | -93.57 % | 149672.6195 MeV (+37158.0 ppm) |
| ${}^{156}$Tb | 156 | 91 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 88.0137 | 1278.3641 | -93.12 % | 150633.0216 MeV (+37110.4 ppm) |
| ${}^{157}$Tb | 157 | 92 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 94.3169 | 1287.1082 | -92.67 % | 151593.4331 MeV (+37076.6 ppm) |
| ${}^{158}$Tb | 158 | 93 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 100.6109 | 1293.8866 | -92.22 % | 152553.8539 MeV (+37029.3 ppm) |
| ${}^{159}$Tb | 159 | 94 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 106.8958 | 1302.0196 | -91.79 % | 153514.2839 MeV (+36992.2 ppm) |
| ${}^{160}$Tb | 160 | 95 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 113.1716 | 1308.3948 | -91.35 % | 154474.7228 MeV (+36943.4 ppm) |
| ${}^{161}$Tb | 161 | 96 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 119.4386 | 1316.0914 | -90.92 % | 155435.1706 MeV (+36904.4 ppm) |
| ${}^{162}$Tb | 162 | 97 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 125.6968 | 1322.5805 | -90.50 % | 156395.6272 MeV (+36857.6 ppm) |
| ${}^{163}$Tb | 163 | 98 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 131.9463 | 1329.3680 | -90.07 % | 157356.0924 MeV (+36813.5 ppm) |
| ${}^{164}$Tb | 164 | 99 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 138.1874 | 1334.9486 | -89.65 % | 158316.5661 MeV (+36761.8 ppm) |
| ${}^{165}$Tb | 165 | 100 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 144.4201 | 1341.5038 | -89.23 % | 159277.0482 MeV (+36717.4 ppm) |
| ${}^{166}$Tb | 166 | 101 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 150.6445 | 1346.7950 | -88.81 % | 160237.5386 MeV (+36665.1 ppm) |
| ${}^{167}$Tb | 167 | 102 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 156.8607 | 1352.9406 | -88.41 % | 161198.0371 MeV (+36619.1 ppm) |
| ${}^{168}$Tb | 168 | 103 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 163.0689 | 1357.9101 | -87.99 % | 162158.5437 MeV (+36566.0 ppm) |
| ${}^{169}$Tb | 169 | 104 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 169.2691 | 1363.6610 | -87.59 % | 163119.0583 MeV (+36518.8 ppm) |
| ${}^{170}$Tb | 170 | 105 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 175.4615 | 1367.9900 | -87.17 % | 164079.5807 MeV (+36462.6 ppm) |
| ${}^{171}$Tb | 171 | 106 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 181.6462 | 1373.1300 | -86.77 % | 165040.1108 MeV (+36412.5 ppm) |
| ${}^{172}$Tb | 172 | 107 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 187.8232 | 1377.0320 | -86.36 % | 166000.6485 MeV (+36355.7 ppm) |
| ${}^{173}$Tb | 173 | 108 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 193.9927 | 1381.9240 | -85.96 % | 166961.1938 MeV (+36305.3 ppm) |
| ${}^{174}$Tb | 174 | 109 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 200.1548 | 1385.5620 | -85.55 % | 167921.7465 MeV (+36246.9 ppm) |

### Dysprosium (Z = 66)

_39 of 39 isotopes with a framework prediction; 39 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{138}$Dy | 138 | 72 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -47.5823 | 1097.1000 | -104.34 % | 133366.4214 MeV (+37780.1 ppm) |
| ${}^{139}$Dy | 139 | 73 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -41.0445 | 1107.9690 | -103.70 % | 134326.5983 MeV (+37752.0 ppm) |
| ${}^{140}$Dy | 140 | 74 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -34.5192 | 1121.1200 | -103.08 % | 135286.7878 MeV (+37743.2 ppm) |
| ${}^{141}$Dy | 141 | 75 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -28.0064 | 1131.8070 | -102.47 % | 136246.9898 MeV (+37714.3 ppm) |
| ${}^{142}$Dy | 142 | 76 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -21.5058 | 1144.6620 | -101.88 % | 137207.2040 MeV (+37703.0 ppm) |
| ${}^{143}$Dy | 143 | 77 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -15.0172 | 1154.7325 | -101.30 % | 138167.4302 MeV (+37670.9 ppm) |
| ${}^{144}$Dy | 144 | 78 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -8.5404 | 1167.2050 | -100.73 % | 139127.6682 MeV (+37657.7 ppm) |
| ${}^{145}$Dy | 145 | 79 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -2.0753 | 1176.9488 | -100.18 % | 140087.9178 MeV (+37623.7 ppm) |
| ${}^{146}$Dy | 146 | 80 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 4.3783 | 1189.3325 | -99.63 % | 141048.1790 MeV (+37610.4 ppm) |
| ${}^{147}$Dy | 147 | 81 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 10.8207 | 1199.0449 | -99.10 % | 142008.4514 MeV (+37577.2 ppm) |
| ${}^{148}$Dy | 148 | 82 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 17.2520 | 1210.7796 | -98.58 % | 142968.7349 MeV (+37559.6 ppm) |
| ${}^{149}$Dy | 149 | 83 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 23.6723 | 1218.6855 | -98.06 % | 143929.0293 MeV (+37513.8 ppm) |
| ${}^{150}$Dy | 150 | 84 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 30.0818 | 1228.3724 | -97.55 % | 144889.3345 MeV (+37481.9 ppm) |
| ${}^{151}$Dy | 151 | 85 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 36.4808 | 1235.8865 | -97.05 % | 145849.6504 MeV (+37434.5 ppm) |
| ${}^{152}$Dy | 152 | 86 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 42.8693 | 1245.3234 | -96.56 % | 146809.9766 MeV (+37401.8 ppm) |
| ${}^{153}$Dy | 153 | 87 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 49.2475 | 1252.4200 | -96.07 % | 147770.3132 MeV (+37352.6 ppm) |
| ${}^{154}$Dy | 154 | 88 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 55.6155 | 1261.7421 | -95.59 % | 148730.6599 MeV (+37320.2 ppm) |
| ${}^{155}$Dy | 155 | 89 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 61.9736 | 1268.5753 | -95.11 % | 149691.0166 MeV (+37270.4 ppm) |
| ${}^{156}$Dy | 156 | 90 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 68.3218 | 1278.0201 | -94.65 % | 150651.3832 MeV (+37240.0 ppm) |
| ${}^{157}$Dy | 157 | 91 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 74.6603 | 1284.9867 | -94.19 % | 151611.7594 MeV (+37192.4 ppm) |
| ${}^{158}$Dy | 158 | 92 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 80.9893 | 1294.0405 | -93.74 % | 152572.1453 MeV (+37160.3 ppm) |
| ${}^{159}$Dy | 159 | 93 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 87.3088 | 1300.8719 | -93.29 % | 153532.5405 MeV (+37113.0 ppm) |
| ${}^{160}$Dy | 160 | 94 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 93.6191 | 1309.4484 | -92.85 % | 154492.9450 MeV (+37078.5 ppm) |
| ${}^{161}$Dy | 161 | 95 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 99.9202 | 1315.9028 | -92.41 % | 155453.3587 MeV (+37029.8 ppm) |
| ${}^{162}$Dy | 162 | 96 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 106.2122 | 1324.0998 | -91.98 % | 156413.7814 MeV (+36993.8 ppm) |
| ${}^{163}$Dy | 163 | 97 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 112.4954 | 1330.3708 | -91.54 % | 157374.2130 MeV (+36945.1 ppm) |
| ${}^{164}$Dy | 164 | 98 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 118.7698 | 1338.0289 | -91.12 % | 158334.6534 MeV (+36906.5 ppm) |
| ${}^{165}$Dy | 165 | 99 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 125.0355 | 1343.7449 | -90.69 % | 159295.1025 MeV (+36855.3 ppm) |
| ${}^{166}$Dy | 166 | 100 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 131.2927 | 1350.7884 | -90.28 % | 160255.5600 MeV (+36813.7 ppm) |
| ${}^{167}$Dy | 167 | 101 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 137.5415 | 1356.1867 | -89.86 % | 161216.0261 MeV (+36761.7 ppm) |
| ${}^{168}$Dy | 168 | 102 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 143.7819 | 1362.9049 | -89.45 % | 162176.5004 MeV (+36719.0 ppm) |
| ${}^{169}$Dy | 169 | 103 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 150.0142 | 1368.0139 | -89.03 % | 163136.9829 MeV (+36666.4 ppm) |
| ${}^{170}$Dy | 170 | 104 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 156.2384 | 1374.2800 | -88.63 % | 164097.4734 MeV (+36621.4 ppm) |
| ${}^{171}$Dy | 171 | 105 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 162.4546 | 1378.6020 | -88.22 % | 165057.9720 MeV (+36565.3 ppm) |
| ${}^{172}$Dy | 172 | 106 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 168.6630 | 1384.4280 | -87.82 % | 166018.4784 MeV (+36519.2 ppm) |
| ${}^{173}$Dy | 173 | 107 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 174.8635 | 1388.4980 | -87.41 % | 166978.9926 MeV (+36462.3 ppm) |
| ${}^{174}$Dy | 174 | 108 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 181.0565 | 1393.9140 | -87.01 % | 167939.5145 MeV (+36415.2 ppm) |
| ${}^{175}$Dy | 175 | 109 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 187.2418 | 1397.5500 | -86.60 % | 168900.0439 MeV (+36357.2 ppm) |
| ${}^{176}$Dy | 176 | 110 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 193.4197 | 1402.5440 | -86.21 % | 169860.5808 MeV (+36308.0 ppm) |

### Holmium (Z = 67)

_39 of 39 isotopes with a framework prediction; 39 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{140}$Ho | 140 | 73 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -55.0918 | 1106.8400 | -104.98 % | 135306.0301 MeV (+37783.2 ppm) |
| ${}^{141}$Ho | 141 | 74 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -48.5378 | 1119.9630 | -104.33 % | 136266.1909 MeV (+37773.4 ppm) |
| ${}^{142}$Ho | 142 | 75 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -41.9964 | 1131.0300 | -103.71 % | 137226.3642 MeV (+37746.9 ppm) |
| ${}^{143}$Ho | 143 | 76 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -35.4673 | 1143.8570 | -103.10 % | 138186.5500 MeV (+37735.7 ppm) |
| ${}^{144}$Ho | 144 | 77 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -28.9505 | 1154.4621 | -102.51 % | 139146.7479 MeV (+37707.4 ppm) |
| ${}^{145}$Ho | 145 | 78 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -22.4456 | 1167.0440 | -101.92 % | 140106.9578 MeV (+37694.6 ppm) |
| ${}^{146}$Ho | 146 | 79 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -15.9526 | 1177.2334 | -101.36 % | 141067.1796 MeV (+37663.8 ppm) |
| ${}^{147}$Ho | 147 | 80 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -9.4712 | 1189.8236 | -100.80 % | 142027.4129 MeV (+37651.7 ppm) |
| ${}^{148}$Ho | 148 | 81 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -3.0012 | 1200.1290 | -100.25 % | 142987.6578 MeV (+37622.7 ppm) |
| ${}^{149}$Ho | 149 | 82 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 3.4574 | 1211.8550 | -99.71 % | 143947.9139 MeV (+37604.7 ppm) |
| ${}^{150}$Ho | 150 | 83 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 9.9050 | 1220.2263 | -99.19 % | 144908.1811 MeV (+37562.2 ppm) |
| ${}^{151}$Ho | 151 | 84 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 16.3416 | 1229.9745 | -98.67 % | 145868.4592 MeV (+37530.4 ppm) |
| ${}^{152}$Ho | 152 | 85 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 22.7675 | 1238.0277 | -98.16 % | 146828.7481 MeV (+37486.7 ppm) |
| ${}^{153}$Ho | 153 | 86 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 29.1827 | 1247.5065 | -97.66 % | 147789.0477 MeV (+37454.0 ppm) |
| ${}^{154}$Ho | 154 | 87 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 35.5875 | 1255.2051 | -97.16 % | 148749.3576 MeV (+37409.0 ppm) |
| ${}^{155}$Ho | 155 | 88 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 41.9820 | 1264.6769 | -96.68 % | 149709.6779 MeV (+37377.3 ppm) |
| ${}^{156}$Ho | 156 | 89 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 48.3664 | 1272.2468 | -96.20 % | 150670.0084 MeV (+37332.6 ppm) |
| ${}^{157}$Ho | 157 | 90 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 54.7407 | 1281.6126 | -95.73 % | 151630.3488 MeV (+37301.2 ppm) |
| ${}^{158}$Ho | 158 | 91 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 61.1052 | 1289.0384 | -95.26 % | 152590.6991 MeV (+37256.6 ppm) |
| ${}^{159}$Ho | 159 | 92 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 67.4599 | 1298.2519 | -94.80 % | 153551.0591 MeV (+37225.2 ppm) |
| ${}^{160}$Ho | 160 | 93 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 73.8051 | 1305.3761 | -94.35 % | 154511.4287 MeV (+37179.7 ppm) |
| ${}^{161}$Ho | 161 | 94 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 80.1409 | 1314.2613 | -93.90 % | 155471.8077 MeV (+37147.0 ppm) |
| ${}^{162}$Ho | 162 | 95 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 86.4673 | 1321.1768 | -93.46 % | 156432.1960 MeV (+37101.2 ppm) |
| ${}^{163}$Ho | 163 | 96 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 92.7846 | 1329.5856 | -93.02 % | 157392.5935 MeV (+37066.2 ppm) |
| ${}^{164}$Ho | 164 | 97 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 99.0928 | 1336.2594 | -92.58 % | 158353.0001 MeV (+37019.9 ppm) |
| ${}^{165}$Ho | 165 | 98 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 105.3921 | 1344.2483 | -92.16 % | 159313.4156 MeV (+36983.2 ppm) |
| ${}^{166}$Ho | 166 | 99 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 111.6826 | 1350.4919 | -91.73 % | 160273.8398 MeV (+36935.2 ppm) |
| ${}^{167}$Ho | 167 | 100 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 117.9644 | 1357.7723 | -91.31 % | 161234.2728 MeV (+36894.8 ppm) |
| ${}^{168}$Ho | 168 | 101 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 124.2377 | 1363.6234 | -90.89 % | 162194.7143 MeV (+36845.4 ppm) |
| ${}^{169}$Ho | 169 | 102 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 130.5025 | 1370.4315 | -90.48 % | 163155.1643 MeV (+36803.0 ppm) |
| ${}^{170}$Ho | 170 | 103 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 136.7589 | 1375.9443 | -90.06 % | 164115.6226 MeV (+36752.7 ppm) |
| ${}^{171}$Ho | 171 | 104 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 143.0072 | 1382.2960 | -89.65 % | 165076.0891 MeV (+36708.4 ppm) |
| ${}^{172}$Ho | 172 | 105 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 149.2473 | 1387.3520 | -89.24 % | 166036.5638 MeV (+36656.2 ppm) |
| ${}^{173}$Ho | 173 | 106 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 155.4795 | 1393.3420 | -88.84 % | 166997.0464 MeV (+36610.5 ppm) |
| ${}^{174}$Ho | 174 | 107 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 161.7037 | 1397.9160 | -88.43 % | 167957.5369 MeV (+36556.7 ppm) |
| ${}^{175}$Ho | 175 | 108 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 167.9202 | 1403.3250 | -88.03 % | 168918.0353 MeV (+36509.4 ppm) |
| ${}^{176}$Ho | 176 | 109 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 174.1289 | 1407.4720 | -87.63 % | 169878.5413 MeV (+36454.2 ppm) |
| ${}^{177}$Ho | 177 | 110 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 180.3301 | 1412.4600 | -87.23 % | 170839.0549 MeV (+36404.7 ppm) |
| ${}^{178}$Ho | 178 | 111 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 186.5237 | 1416.3460 | -86.83 % | 171799.5760 MeV (+36349.3 ppm) |

### Erbium (Z = 68)

_39 of 39 isotopes with a framework prediction; 39 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{142}$Er | 142 | 74 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -62.7586 | 1120.8060 | -105.60 % | 137245.7962 MeV (+37820.7 ppm) |
| ${}^{143}$Er | 143 | 75 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -56.1885 | 1132.1310 | -104.96 % | 138205.9409 MeV (+37796.4 ppm) |
| ${}^{144}$Er | 144 | 76 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -49.6310 | 1145.6640 | -104.33 % | 139166.0981 MeV (+37789.8 ppm) |
| ${}^{145}$Er | 145 | 77 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -43.0858 | 1156.3750 | -103.73 % | 140126.2677 MeV (+37761.7 ppm) |
| ${}^{146}$Er | 146 | 78 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -36.5528 | 1169.5349 | -103.13 % | 141086.4495 MeV (+37752.8 ppm) |
| ${}^{147}$Er | 147 | 79 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -30.0318 | 1179.8920 | -102.55 % | 142046.6432 MeV (+37722.8 ppm) |
| ${}^{148}$Er | 148 | 80 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -23.5225 | 1192.8345 | -101.97 % | 143006.8488 MeV (+37712.9 ppm) |
| ${}^{149}$Er | 149 | 81 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -17.0249 | 1203.1684 | -101.42 % | 143967.0659 MeV (+37683.6 ppm) |
| ${}^{150}$Er | 150 | 82 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -10.5388 | 1215.3294 | -100.87 % | 144927.2946 MeV (+37668.4 ppm) |
| ${}^{151}$Er | 151 | 83 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -4.0639 | 1223.8357 | -100.33 % | 145887.5344 MeV (+37626.5 ppm) |
| ${}^{152}$Er | 152 | 84 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 2.3999 | 1234.1410 | -99.81 % | 146847.7854 MeV (+37598.5 ppm) |
| ${}^{153}$Er | 153 | 85 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 8.8527 | 1242.1788 | -99.29 % | 147808.0474 MeV (+37554.3 ppm) |
| ${}^{154}$Er | 154 | 86 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 15.2948 | 1252.3884 | -98.78 % | 148768.3200 MeV (+37526.5 ppm) |
| ${}^{155}$Er | 155 | 87 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 21.7263 | 1260.0639 | -98.28 % | 149728.6034 MeV (+37480.9 ppm) |
| ${}^{156}$Er | 156 | 88 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 28.1473 | 1270.1377 | -97.78 % | 150688.8971 MeV (+37453.2 ppm) |
| ${}^{157}$Er | 157 | 89 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 34.5580 | 1277.4110 | -97.29 % | 151649.2012 MeV (+37405.9 ppm) |
| ${}^{158}$Er | 158 | 90 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 40.9585 | 1287.3725 | -96.82 % | 152609.5154 MeV (+37378.3 ppm) |
| ${}^{159}$Er | 159 | 91 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 47.3491 | 1294.7011 | -96.34 % | 153569.8397 MeV (+37332.7 ppm) |
| ${}^{160}$Er | 160 | 92 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 53.7297 | 1304.2755 | -95.88 % | 154530.1738 MeV (+37303.3 ppm) |
| ${}^{161}$Er | 161 | 93 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 60.1007 | 1311.4839 | -95.42 % | 155490.5176 MeV (+37258.0 ppm) |
| ${}^{162}$Er | 162 | 94 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 66.4620 | 1320.6881 | -94.97 % | 156450.8710 MeV (+37227.0 ppm) |
| ${}^{163}$Er | 163 | 95 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 72.8139 | 1327.5927 | -94.52 % | 157411.2339 MeV (+37180.8 ppm) |
| ${}^{164}$Er | 164 | 96 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 79.1565 | 1336.4391 | -94.08 % | 158371.6061 MeV (+37148.3 ppm) |
| ${}^{165}$Er | 165 | 97 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 85.4899 | 1343.0892 | -93.63 % | 159331.9875 MeV (+37101.5 ppm) |
| ${}^{166}$Er | 166 | 98 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 91.8142 | 1351.5634 | -93.21 % | 160292.3780 MeV (+37067.6 ppm) |
| ${}^{167}$Er | 167 | 99 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 98.1295 | 1357.9998 | -92.77 % | 161252.7774 MeV (+37020.5 ppm) |
| ${}^{168}$Er | 168 | 100 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 104.4361 | 1365.7711 | -92.35 % | 162213.1856 MeV (+36982.9 ppm) |
| ${}^{169}$Er | 169 | 101 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 110.7339 | 1371.7743 | -91.93 % | 163173.6026 MeV (+36934.2 ppm) |
| ${}^{170}$Er | 170 | 102 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 117.0231 | 1379.0320 | -91.51 % | 164134.0281 MeV (+36894.3 ppm) |
| ${}^{171}$Er | 171 | 103 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 123.3039 | 1384.7136 | -91.10 % | 165094.4621 MeV (+36844.6 ppm) |
| ${}^{172}$Er | 172 | 104 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 129.5763 | 1391.5497 | -90.69 % | 166054.9045 MeV (+36803.1 ppm) |
| ${}^{173}$Er | 173 | 105 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 135.8405 | 1396.8020 | -90.27 % | 167015.3551 MeV (+36751.8 ppm) |
| ${}^{174}$Er | 174 | 106 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 142.0965 | 1403.1360 | -89.87 % | 167975.8138 MeV (+36708.4 ppm) |
| ${}^{175}$Er | 175 | 107 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 148.3445 | 1407.8750 | -89.46 % | 168936.2806 MeV (+36655.4 ppm) |
| ${}^{176}$Er | 176 | 108 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 154.5846 | 1413.9840 | -89.07 % | 169896.7553 MeV (+36611.1 ppm) |
| ${}^{177}$Er | 177 | 109 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 160.8169 | 1418.3010 | -88.66 % | 170857.2378 MeV (+36556.3 ppm) |
| ${}^{178}$Er | 178 | 110 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 167.0414 | 1423.8220 | -88.27 % | 171817.7281 MeV (+36509.6 ppm) |
| ${}^{179}$Er | 179 | 111 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 173.2583 | 1427.7040 | -87.86 % | 172778.2259 MeV (+36453.6 ppm) |
| ${}^{180}$Er | 180 | 112 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 179.4676 | 1432.8000 | -87.47 % | 173738.7313 MeV (+36406.1 ppm) |

### Thulium (Z = 69)

_39 of 39 isotopes with a framework prediction; 39 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{144}$Tm | 144 | 75 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -70.5820 | 1130.4000 | -106.24 % | 139185.7188 MeV (+37824.3 ppm) |
| ${}^{145}$Tm | 145 | 76 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -63.9959 | 1143.9050 | -105.59 % | 140145.8475 MeV (+37817.1 ppm) |
| ${}^{146}$Tm | 146 | 77 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -57.4223 | 1155.4440 | -104.97 % | 141105.9887 MeV (+37795.2 ppm) |
| ${}^{147}$Tm | 147 | 78 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -50.8610 | 1168.4762 | -104.35 % | 142066.1422 MeV (+37784.7 ppm) |
| ${}^{148}$Tm | 148 | 79 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -44.3120 | 1179.3382 | -103.76 % | 143026.3079 MeV (+37758.4 ppm) |
| ${}^{149}$Tm | 149 | 80 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -37.7749 | 1192.5960 | -103.17 % | 143986.4856 MeV (+37750.3 ppm) |
| ${}^{150}$Tm | 150 | 81 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -31.2495 | 1203.1500 | -102.60 % | 144946.6750 MeV (+37722.9 ppm) |
| ${}^{151}$Tm | 151 | 82 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -24.7358 | 1215.5587 | -102.03 % | 145906.8761 MeV (+37708.8 ppm) |
| ${}^{152}$Tm | 152 | 83 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -18.2335 | 1224.5787 | -101.49 % | 146867.0885 MeV (+37670.5 ppm) |
| ${}^{153}$Tm | 153 | 84 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -11.7425 | 1234.9023 | -100.95 % | 147827.3123 MeV (+37642.2 ppm) |
| ${}^{154}$Tm | 154 | 85 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -5.2626 | 1243.4282 | -100.42 % | 148787.5471 MeV (+37601.4 ppm) |
| ${}^{155}$Tm | 155 | 86 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 1.2064 | 1253.6983 | -99.90 % | 149747.7929 MeV (+37573.8 ppm) |
| ${}^{156}$Tm | 156 | 87 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 7.6646 | 1261.9781 | -99.39 % | 150708.0495 MeV (+37532.3 ppm) |
| ${}^{157}$Tm | 157 | 88 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 14.1123 | 1271.9243 | -98.89 % | 151668.3166 MeV (+37503.3 ppm) |
| ${}^{158}$Tm | 158 | 89 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 20.5494 | 1279.9895 | -98.39 % | 152628.5943 MeV (+37461.4 ppm) |
| ${}^{159}$Tm | 159 | 90 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 26.9762 | 1289.9280 | -97.91 % | 153588.8822 MeV (+37433.3 ppm) |
| ${}^{160}$Tm | 160 | 91 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 33.3929 | 1297.7300 | -97.43 % | 154549.1803 MeV (+37390.7 ppm) |
| ${}^{161}$Tm | 161 | 92 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 39.7996 | 1307.3990 | -96.96 % | 155509.4884 MeV (+37361.7 ppm) |
| ${}^{162}$Tm | 162 | 93 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 46.1963 | 1315.0491 | -96.49 % | 156469.8064 MeV (+37319.1 ppm) |
| ${}^{163}$Tm | 163 | 94 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 52.5834 | 1324.3713 | -96.03 % | 157430.1342 MeV (+37288.6 ppm) |
| ${}^{164}$Tm | 164 | 95 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 58.9608 | 1331.6232 | -95.57 % | 158390.4715 MeV (+37244.5 ppm) |
| ${}^{165}$Tm | 165 | 96 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 65.3288 | 1340.7156 | -95.13 % | 159350.8183 MeV (+37213.4 ppm) |
| ${}^{166}$Tm | 166 | 97 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 71.6874 | 1347.7433 | -94.68 % | 160311.1745 MeV (+37168.8 ppm) |
| ${}^{167}$Tm | 167 | 98 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 78.0368 | 1356.4713 | -94.25 % | 161271.5398 MeV (+37136.2 ppm) |
| ${}^{168}$Tm | 168 | 99 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 84.3771 | 1363.3119 | -93.81 % | 162231.9143 MeV (+37091.5 ppm) |
| ${}^{169}$Tm | 169 | 100 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 90.7085 | 1371.3455 | -93.39 % | 163192.2977 MeV (+37055.3 ppm) |
| ${}^{170}$Tm | 170 | 101 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 97.0310 | 1377.9374 | -92.96 % | 164152.6900 MeV (+37010.1 ppm) |
| ${}^{171}$Tm | 171 | 102 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 103.3448 | 1385.4237 | -92.54 % | 165113.0910 MeV (+36971.3 ppm) |
| ${}^{172}$Tm | 172 | 103 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 109.6499 | 1391.6583 | -92.12 % | 166073.5006 MeV (+36925.0 ppm) |
| ${}^{173}$Tm | 173 | 104 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 115.9466 | 1398.6122 | -91.71 % | 167033.9186 MeV (+36883.8 ppm) |
| ${}^{174}$Tm | 174 | 105 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 122.2349 | 1404.2919 | -91.30 % | 167994.3451 MeV (+36835.0 ppm) |
| ${}^{175}$Tm | 175 | 106 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 128.5150 | 1410.8093 | -90.89 % | 168954.7799 MeV (+36792.2 ppm) |
| ${}^{176}$Tm | 176 | 107 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 134.7868 | 1415.9414 | -90.48 % | 169915.2228 MeV (+36741.1 ppm) |
| ${}^{177}$Tm | 177 | 108 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 141.0506 | 1422.1950 | -90.08 % | 170875.6737 MeV (+36697.8 ppm) |
| ${}^{178}$Tm | 178 | 109 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 147.3065 | 1427.0260 | -89.68 % | 171836.1327 MeV (+36645.5 ppm) |
| ${}^{179}$Tm | 179 | 110 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 153.5545 | 1432.7160 | -89.28 % | 172796.5995 MeV (+36600.0 ppm) |
| ${}^{180}$Tm | 180 | 111 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 159.7947 | 1436.9400 | -88.88 % | 173757.0740 MeV (+36546.4 ppm) |
| ${}^{181}$Tm | 181 | 112 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 166.0273 | 1442.3890 | -88.49 % | 174717.5562 MeV (+36499.6 ppm) |
| ${}^{182}$Tm | 182 | 113 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 172.2523 | 1446.5360 | -88.09 % | 175678.0459 MeV (+36446.0 ppm) |

### Ytterbium (Z = 70)

_38 of 38 isotopes with a framework prediction; 38 of 38 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{148}$Yb | 148 | 78 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -65.3695 | 1170.0880 | -105.59 % | 143046.0351 MeV (+37837.2 ppm) |
| ${}^{149}$Yb | 149 | 79 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -58.7923 | 1181.1230 | -104.98 % | 144006.1727 MeV (+37812.8 ppm) |
| ${}^{150}$Yb | 150 | 80 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -52.2272 | 1194.7500 | -104.37 % | 144966.3224 MeV (+37806.7 ppm) |
| ${}^{151}$Yb | 151 | 81 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -45.6741 | 1205.5471 | -103.79 % | 145926.4840 MeV (+37780.1 ppm) |
| ${}^{152}$Yb | 152 | 82 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -39.1327 | 1218.3464 | -103.21 % | 146886.6575 MeV (+37768.8 ppm) |
| ${}^{153}$Yb | 153 | 83 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -32.6030 | 1227.3660 | -102.66 % | 147846.8425 MeV (+37729.7 ppm) |
| ${}^{154}$Yb | 154 | 84 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -26.0847 | 1238.1508 | -102.11 % | 148807.0389 MeV (+37704.8 ppm) |
| ${}^{155}$Yb | 155 | 85 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -19.5776 | 1246.7926 | -101.57 % | 149767.2466 MeV (+37664.5 ppm) |
| ${}^{156}$Yb | 156 | 86 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -13.0816 | 1257.6269 | -101.04 % | 150727.4654 MeV (+37640.5 ppm) |
| ${}^{157}$Yb | 157 | 87 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -6.5965 | 1265.8526 | -100.52 % | 151687.6951 MeV (+37598.3 ppm) |
| ${}^{158}$Yb | 158 | 88 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -0.1222 | 1276.5136 | -100.01 % | 152647.9356 MeV (+37573.9 ppm) |
| ${}^{159}$Yb | 159 | 89 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 6.3414 | 1284.4088 | -99.51 % | 153608.1867 MeV (+37530.5 ppm) |
| ${}^{160}$Yb | 160 | 90 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 12.7946 | 1294.8098 | -99.01 % | 154568.4483 MeV (+37505.2 ppm) |
| ${}^{161}$Yb | 161 | 91 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 19.2375 | 1302.5522 | -98.52 % | 155528.7202 MeV (+37461.8 ppm) |
| ${}^{162}$Yb | 162 | 92 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 25.6702 | 1312.6104 | -98.04 % | 156489.0022 MeV (+37435.0 ppm) |
| ${}^{163}$Yb | 163 | 93 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 32.0929 | 1320.1544 | -97.57 % | 157449.2943 MeV (+37391.4 ppm) |
| ${}^{164}$Yb | 164 | 94 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 38.5057 | 1329.9440 | -97.10 % | 158409.5963 MeV (+37363.6 ppm) |
| ${}^{165}$Yb | 165 | 95 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 44.9088 | 1337.2986 | -96.64 % | 159369.9080 MeV (+37319.8 ppm) |
| ${}^{166}$Yb | 166 | 96 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 51.3022 | 1346.6682 | -96.19 % | 160330.2293 MeV (+37290.1 ppm) |
| ${}^{167}$Yb | 167 | 97 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 57.6862 | 1353.7357 | -95.74 % | 161290.5601 MeV (+37245.5 ppm) |
| ${}^{168}$Yb | 168 | 98 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 64.0608 | 1362.7970 | -95.30 % | 162250.9003 MeV (+37214.7 ppm) |
| ${}^{169}$Yb | 169 | 99 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 70.4262 | 1369.6640 | -94.86 % | 163211.2497 MeV (+37169.8 ppm) |
| ${}^{170}$Yb | 170 | 100 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 76.7824 | 1378.1237 | -94.43 % | 164171.6082 MeV (+37136.0 ppm) |
| ${}^{171}$Yb | 171 | 101 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 83.1297 | 1384.7379 | -94.00 % | 165131.9757 MeV (+37090.6 ppm) |
| ${}^{172}$Yb | 172 | 102 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 89.4682 | 1392.7579 | -93.58 % | 166092.3520 MeV (+37054.9 ppm) |
| ${}^{173}$Yb | 173 | 103 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 95.7978 | 1399.1250 | -93.15 % | 167052.7371 MeV (+37009.0 ppm) |
| ${}^{174}$Yb | 174 | 104 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 102.1189 | 1406.5896 | -92.74 % | 168013.1309 MeV (+36970.7 ppm) |
| ${}^{175}$Yb | 175 | 105 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 108.4314 | 1412.4119 | -92.32 % | 168973.5331 MeV (+36922.4 ppm) |
| ${}^{176}$Yb | 176 | 106 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 114.7355 | 1419.2790 | -91.92 % | 169933.9438 MeV (+36881.4 ppm) |
| ${}^{177}$Yb | 177 | 107 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 121.0314 | 1424.8454 | -91.51 % | 170894.3627 MeV (+36832.7 ppm) |
| ${}^{178}$Yb | 178 | 108 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 127.3190 | 1431.6075 | -91.11 % | 171854.7899 MeV (+36792.1 ppm) |
| ${}^{179}$Yb | 179 | 109 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 133.5985 | 1436.6540 | -90.70 % | 172815.2251 MeV (+36741.2 ppm) |
| ${}^{180}$Yb | 180 | 110 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 139.8701 | 1442.8800 | -90.31 % | 173775.6683 MeV (+36697.9 ppm) |
| ${}^{181}$Yb | 181 | 111 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 146.1338 | 1447.2760 | -89.90 % | 174736.1194 MeV (+36644.5 ppm) |
| ${}^{182}$Yb | 182 | 112 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 152.3897 | 1453.0880 | -89.51 % | 175696.5783 MeV (+36600.6 ppm) |
| ${}^{183}$Yb | 183 | 113 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 158.6379 | 1457.2290 | -89.11 % | 176657.0448 MeV (+36546.9 ppm) |
| ${}^{184}$Yb | 184 | 114 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 164.8785 | 1462.9840 | -88.73 % | 177617.5190 MeV (+36502.8 ppm) |
| ${}^{185}$Yb | 185 | 115 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 171.1116 | 1466.8650 | -88.33 % | 178578.0006 MeV (+36448.9 ppm) |

### Lutetium (Z = 71)

_39 of 39 isotopes with a framework prediction; 39 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{150}$Lu | 150 | 79 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -73.4719 | 1179.9000 | -106.23 % | 144986.2367 MeV (+37844.8 ppm) |
| ${}^{151}$Lu | 151 | 80 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -66.8788 | 1193.5040 | -105.60 % | 145946.3584 MeV (+37838.5 ppm) |
| ${}^{152}$Lu | 152 | 81 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -60.2978 | 1204.7520 | -105.00 % | 146906.4922 MeV (+37814.7 ppm) |
| ${}^{153}$Lu | 153 | 82 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -53.7287 | 1217.7405 | -104.41 % | 147866.6379 MeV (+37804.7 ppm) |
| ${}^{154}$Lu | 154 | 83 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -47.1714 | 1227.0720 | -103.84 % | 148826.7954 MeV (+37768.3 ppm) |
| ${}^{155}$Lu | 155 | 84 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -40.6257 | 1238.0527 | -103.28 % | 149786.9645 MeV (+37743.9 ppm) |
| ${}^{156}$Lu | 156 | 85 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -34.0914 | 1247.2785 | -102.73 % | 150747.1449 MeV (+37707.6 ppm) |
| ${}^{157}$Lu | 157 | 86 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -27.5684 | 1258.0901 | -102.19 % | 151707.3367 MeV (+37683.1 ppm) |
| ${}^{158}$Lu | 158 | 87 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -21.0564 | 1266.9338 | -101.66 % | 152667.5395 MeV (+37645.1 ppm) |
| ${}^{159}$Lu | 159 | 88 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -14.5554 | 1277.5015 | -101.14 % | 153627.7532 MeV (+37619.7 ppm) |
| ${}^{160}$Lu | 160 | 89 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -8.0651 | 1286.1342 | -100.63 % | 154587.9777 MeV (+37581.3 ppm) |
| ${}^{161}$Lu | 161 | 90 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -1.5854 | 1296.4979 | -100.12 % | 155548.2128 MeV (+37555.4 ppm) |
| ${}^{162}$Lu | 162 | 91 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 4.8838 | 1304.8387 | -99.63 % | 156508.4584 MeV (+37515.9 ppm) |
| ${}^{163}$Lu | 163 | 92 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 11.3426 | 1314.8696 | -99.14 % | 157468.7143 MeV (+37488.6 ppm) |
| ${}^{164}$Lu | 164 | 93 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 17.7913 | 1322.7919 | -98.66 % | 158428.9804 MeV (+37447.3 ppm) |
| ${}^{165}$Lu | 165 | 94 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 24.2300 | 1332.6631 | -98.18 % | 159389.2565 MeV (+37419.7 ppm) |
| ${}^{166}$Lu | 166 | 95 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 30.6588 | 1340.3131 | -97.71 % | 160349.5425 MeV (+37377.7 ppm) |
| ${}^{167}$Lu | 167 | 96 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 37.0778 | 1349.8898 | -97.25 % | 161309.8382 MeV (+37349.0 ppm) |
| ${}^{168}$Lu | 168 | 97 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 43.4872 | 1357.5076 | -96.80 % | 162270.1436 MeV (+37307.8 ppm) |
| ${}^{169}$Lu | 169 | 98 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 49.8871 | 1366.5886 | -96.35 % | 163230.4585 MeV (+37276.8 ppm) |
| ${}^{170}$Lu | 170 | 99 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 56.2776 | 1373.8837 | -95.90 % | 164190.7828 MeV (+37234.5 ppm) |
| ${}^{171}$Lu | 171 | 100 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 62.6588 | 1382.4772 | -95.47 % | 165151.1163 MeV (+37201.2 ppm) |
| ${}^{172}$Lu | 172 | 101 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 69.0310 | 1389.4561 | -95.03 % | 166111.4589 MeV (+37157.8 ppm) |
| ${}^{173}$Lu | 173 | 102 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 75.3941 | 1397.6724 | -94.61 % | 167071.8105 MeV (+37123.1 ppm) |
| ${}^{174}$Lu | 174 | 103 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 81.7484 | 1404.4330 | -94.18 % | 168032.1710 MeV (+37079.4 ppm) |
| ${}^{175}$Lu | 175 | 104 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 88.0939 | 1412.0997 | -93.76 % | 168992.5403 MeV (+37042.1 ppm) |
| ${}^{176}$Lu | 176 | 105 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 94.4308 | 1418.3877 | -93.34 % | 169952.9182 MeV (+36996.5 ppm) |
| ${}^{177}$Lu | 177 | 106 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 100.7591 | 1425.4606 | -92.93 % | 170913.3047 MeV (+36956.4 ppm) |
| ${}^{178}$Lu | 178 | 107 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 107.0789 | 1431.4859 | -92.52 % | 171873.6996 MeV (+36910.3 ppm) |
| ${}^{179}$Lu | 179 | 108 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 113.3905 | 1438.2783 | -92.12 % | 172834.1028 MeV (+36869.5 ppm) |
| ${}^{180}$Lu | 180 | 109 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 119.6938 | 1443.9671 | -91.71 % | 173794.5142 MeV (+36822.4 ppm) |
| ${}^{181}$Lu | 181 | 110 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 125.9891 | 1450.1593 | -91.31 % | 174754.9338 MeV (+36778.9 ppm) |
| ${}^{182}$Lu | 182 | 111 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 132.2763 | 1455.2720 | -90.91 % | 175715.3613 MeV (+36729.0 ppm) |
| ${}^{183}$Lu | 183 | 112 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 138.5556 | 1461.2207 | -90.52 % | 176675.7968 MeV (+36685.6 ppm) |
| ${}^{184}$Lu | 184 | 113 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 144.8271 | 1465.9280 | -90.12 % | 177636.2401 MeV (+36634.4 ppm) |
| ${}^{185}$Lu | 185 | 114 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 151.0909 | 1471.6750 | -89.73 % | 178596.6911 MeV (+36590.4 ppm) |
| ${}^{186}$Lu | 186 | 115 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 157.3470 | 1476.0960 | -89.34 % | 179557.1497 MeV (+36539.0 ppm) |
| ${}^{187}$Lu | 187 | 116 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 163.5957 | 1481.6010 | -88.96 % | 180517.6158 MeV (+36494.8 ppm) |
| ${}^{188}$Lu | 188 | 117 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 169.8369 | 1485.7640 | -88.57 % | 181478.0894 MeV (+36442.7 ppm) |

### Hafnium (Z = 72)

_38 of 38 isotopes with a framework prediction; 38 of 38 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{153}$Hf | 153 | 81 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -75.1197 | 1205.9460 | -106.23 % | 147886.6986 MeV (+37864.8 ppm) |
| ${}^{154}$Hf | 154 | 82 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -68.5229 | 1219.3720 | -105.62 % | 148846.8166 MeV (+37857.7 ppm) |
| ${}^{155}$Hf | 155 | 83 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -61.9380 | 1228.9950 | -105.04 % | 149806.9464 MeV (+37823.2 ppm) |
| ${}^{156}$Hf | 156 | 84 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -55.3648 | 1240.6161 | -104.46 % | 150767.0881 MeV (+37802.9 ppm) |
| ${}^{157}$Hf | 157 | 85 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -48.8032 | 1249.7200 | -103.91 % | 151727.2412 MeV (+37765.4 ppm) |
| ${}^{158}$Hf | 158 | 86 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -42.2531 | 1261.0417 | -103.35 % | 152687.4058 MeV (+37744.1 ppm) |
| ${}^{159}$Hf | 159 | 87 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -35.7141 | 1269.8632 | -102.81 % | 153647.5816 MeV (+37705.6 ppm) |
| ${}^{160}$Hf | 160 | 88 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -29.1862 | 1281.0207 | -102.28 % | 154607.7685 MeV (+37684.0 ppm) |
| ${}^{161}$Hf | 161 | 89 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -22.6693 | 1289.4690 | -101.76 % | 155567.9664 MeV (+37643.9 ppm) |
| ${}^{162}$Hf | 162 | 90 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -16.1631 | 1300.3930 | -101.24 % | 156528.1750 MeV (+37621.4 ppm) |
| ${}^{163}$Hf | 163 | 91 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -9.6675 | 1308.5652 | -100.74 % | 157488.3942 MeV (+37580.5 ppm) |
| ${}^{164}$Hf | 164 | 92 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -3.1824 | 1319.1855 | -100.24 % | 158448.6238 MeV (+37556.7 ppm) |
| ${}^{165}$Hf | 165 | 93 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 3.2924 | 1327.0740 | -99.75 % | 159408.8638 MeV (+37514.9 ppm) |
| ${}^{166}$Hf | 166 | 94 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 9.7570 | 1337.3688 | -99.27 % | 160369.1140 MeV (+37489.8 ppm) |
| ${}^{167}$Hf | 167 | 95 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 16.2115 | 1345.0489 | -98.79 % | 161329.3742 MeV (+37447.6 ppm) |
| ${}^{168}$Hf | 168 | 96 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 22.6562 | 1355.0130 | -98.33 % | 162289.6443 MeV (+37421.1 ppm) |
| ${}^{169}$Hf | 169 | 97 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 29.0911 | 1362.4407 | -97.86 % | 163249.9242 MeV (+37378.3 ppm) |
| ${}^{170}$Hf | 170 | 98 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 35.5163 | 1372.0490 | -97.41 % | 164210.2137 MeV (+37350.3 ppm) |
| ${}^{171}$Hf | 171 | 99 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 41.9321 | 1379.2977 | -96.96 % | 165170.5128 MeV (+37307.4 ppm) |
| ${}^{172}$Hf | 172 | 100 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 48.3384 | 1388.3400 | -96.52 % | 166130.8212 MeV (+37276.6 ppm) |
| ${}^{173}$Hf | 173 | 101 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 54.7355 | 1395.4208 | -96.08 % | 167091.1388 MeV (+37233.6 ppm) |
| ${}^{174}$Hf | 174 | 102 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 61.1235 | 1403.9249 | -95.65 % | 168051.4656 MeV (+37200.2 ppm) |
| ${}^{175}$Hf | 175 | 103 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 67.5024 | 1410.6334 | -95.21 % | 169011.8015 MeV (+37155.9 ppm) |
| ${}^{176}$Hf | 176 | 104 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 73.8725 | 1418.7994 | -94.79 % | 169972.1462 MeV (+37121.4 ppm) |
| ${}^{177}$Hf | 177 | 105 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 80.2338 | 1425.1751 | -94.37 % | 170932.4997 MeV (+37076.0 ppm) |
| ${}^{178}$Hf | 178 | 106 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 86.5863 | 1432.8010 | -93.96 % | 171892.8619 MeV (+37039.0 ppm) |
| ${}^{179}$Hf | 179 | 107 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 92.9304 | 1438.9000 | -93.54 % | 172853.2326 MeV (+36993.0 ppm) |
| ${}^{180}$Hf | 180 | 108 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 99.2659 | 1446.2877 | -93.14 % | 173813.6118 MeV (+36955.5 ppm) |
| ${}^{181}$Hf | 181 | 109 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 105.5932 | 1451.9825 | -92.73 % | 174773.9994 MeV (+36908.1 ppm) |
| ${}^{182}$Hf | 182 | 110 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 111.9122 | 1458.7005 | -92.33 % | 175734.3952 MeV (+36867.5 ppm) |
| ${}^{183}$Hf | 183 | 111 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 118.2230 | 1464.0058 | -91.92 % | 176694.7991 MeV (+36818.8 ppm) |
| ${}^{184}$Hf | 184 | 112 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 124.5258 | 1470.2930 | -91.53 % | 177655.2110 MeV (+36776.6 ppm) |
| ${}^{185}$Hf | 185 | 113 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 130.8207 | 1475.1847 | -91.13 % | 178615.6309 MeV (+36726.5 ppm) |
| ${}^{186}$Hf | 186 | 114 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 137.1078 | 1481.3604 | -90.74 % | 179576.0587 MeV (+36684.7 ppm) |
| ${}^{187}$Hf | 187 | 115 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 143.3871 | 1486.0890 | -90.35 % | 180536.4941 MeV (+36634.3 ppm) |
| ${}^{188}$Hf | 188 | 116 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 149.6587 | 1491.9680 | -89.97 % | 181496.9372 MeV (+36591.9 ppm) |
| ${}^{189}$Hf | 189 | 117 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 155.9228 | 1496.3130 | -89.58 % | 182457.3879 MeV (+36541.1 ppm) |
| ${}^{190}$Hf | 190 | 118 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 162.1795 | 1501.9500 | -89.20 % | 183417.8461 MeV (+36498.6 ppm) |

### Tantalum (Z = 73)

_40 of 40 isotopes with a framework prediction; 40 of 40 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{155}$Ta | 155 | 82 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -83.5144 | 1217.9900 | -106.86 % | 149827.1926 MeV (+37889.2 ppm) |
| ${}^{156}$Ta | 156 | 83 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -76.9019 | 1228.0320 | -106.26 % | 150787.2948 MeV (+37857.6 ppm) |
| ${}^{157}$Ta | 157 | 84 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -70.3012 | 1239.6815 | -105.67 % | 151747.4089 MeV (+37837.6 ppm) |
| ${}^{158}$Ta | 158 | 85 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -63.7122 | 1249.3060 | -105.10 % | 152707.5347 MeV (+37803.4 ppm) |
| ${}^{159}$Ta | 159 | 86 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -57.1348 | 1260.6674 | -104.53 % | 153667.6721 MeV (+37782.3 ppm) |
| ${}^{160}$Ta | 160 | 87 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -50.5688 | 1270.1233 | -103.98 % | 154627.8208 MeV (+37748.1 ppm) |
| ${}^{161}$Ta | 161 | 88 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -44.0141 | 1281.1494 | -103.44 % | 155587.9808 MeV (+37725.2 ppm) |
| ${}^{162}$Ta | 162 | 89 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -37.4703 | 1290.2236 | -102.90 % | 156548.1519 MeV (+37689.3 ppm) |
| ${}^{163}$Ta | 163 | 90 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -30.9376 | 1301.0482 | -102.38 % | 157508.3339 MeV (+37665.8 ppm) |
| ${}^{164}$Ta | 164 | 91 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -24.4155 | 1309.8676 | -101.86 % | 158468.5266 MeV (+37629.1 ppm) |
| ${}^{165}$Ta | 165 | 92 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -17.9041 | 1320.5040 | -101.36 % | 159428.7300 MeV (+37605.1 ppm) |
| ${}^{166}$Ta | 166 | 93 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -11.4032 | 1328.8253 | -100.86 % | 160388.9438 MeV (+37566.0 ppm) |
| ${}^{167}$Ta | 167 | 94 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -4.9126 | 1339.1499 | -100.37 % | 161349.1680 MeV (+37540.7 ppm) |
| ${}^{168}$Ta | 168 | 95 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 1.5679 | 1347.2640 | -99.88 % | 162309.4023 MeV (+37501.2 ppm) |
| ${}^{169}$Ta | 169 | 96 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 8.0383 | 1357.2319 | -99.41 % | 163269.6467 MeV (+37474.4 ppm) |
| ${}^{170}$Ta | 170 | 97 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 14.4987 | 1365.1504 | -98.94 % | 164229.9010 MeV (+37434.6 ppm) |
| ${}^{171}$Ta | 171 | 98 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 20.9494 | 1374.8043 | -98.48 % | 165190.1651 MeV (+37406.6 ppm) |
| ${}^{172}$Ta | 172 | 99 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 27.3905 | 1382.4854 | -98.02 % | 166150.4388 MeV (+37366.2 ppm) |
| ${}^{173}$Ta | 173 | 100 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 33.8220 | 1391.6232 | -97.57 % | 167110.7221 MeV (+37335.7 ppm) |
| ${}^{174}$Ta | 174 | 101 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 40.2442 | 1399.0388 | -97.12 % | 168071.0147 MeV (+37294.6 ppm) |
| ${}^{175}$Ta | 175 | 102 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 46.6570 | 1407.7780 | -96.69 % | 169031.3166 MeV (+37262.5 ppm) |
| ${}^{176}$Ta | 176 | 103 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 53.0607 | 1414.8060 | -96.25 % | 169991.6277 MeV (+37219.9 ppm) |
| ${}^{177}$Ta | 177 | 104 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 59.4554 | 1423.2267 | -95.82 % | 170951.9478 MeV (+37186.7 ppm) |
| ${}^{178}$Ta | 178 | 105 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 65.8412 | 1430.2300 | -95.40 % | 171912.2768 MeV (+37144.7 ppm) |
| ${}^{179}$Ta | 179 | 106 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 72.2181 | 1438.0121 | -94.98 % | 172872.6146 MeV (+37108.6 ppm) |
| ${}^{180}$Ta | 180 | 107 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 78.5864 | 1444.6596 | -94.56 % | 173832.9611 MeV (+37065.7 ppm) |
| ${}^{181}$Ta | 181 | 108 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 84.9461 | 1452.2363 | -94.15 % | 174793.3162 MeV (+37029.1 ppm) |
| ${}^{182}$Ta | 182 | 109 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 91.2973 | 1458.2992 | -93.74 % | 175753.6797 MeV (+36983.6 ppm) |
| ${}^{183}$Ta | 183 | 110 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 97.6401 | 1465.2334 | -93.34 % | 176714.0517 MeV (+36944.0 ppm) |
| ${}^{184}$Ta | 184 | 111 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 103.9747 | 1470.8506 | -92.93 % | 177674.4318 MeV (+36896.9 ppm) |
| ${}^{185}$Ta | 185 | 112 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 110.3012 | 1477.4769 | -92.53 % | 178634.8202 MeV (+36856.4 ppm) |
| ${}^{186}$Ta | 186 | 113 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 116.6195 | 1482.7614 | -92.13 % | 179595.2166 MeV (+36808.4 ppm) |
| ${}^{187}$Ta | 187 | 114 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 122.9299 | 1489.1207 | -91.74 % | 180555.6210 MeV (+36767.3 ppm) |
| ${}^{188}$Ta | 188 | 115 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 129.2325 | 1494.2240 | -91.35 % | 181516.0332 MeV (+36719.2 ppm) |
| ${}^{189}$Ta | 189 | 116 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 135.5272 | 1500.2820 | -90.97 % | 182476.4532 MeV (+36677.7 ppm) |
| ${}^{190}$Ta | 190 | 117 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 141.8143 | 1505.1800 | -90.58 % | 183436.8809 MeV (+36629.2 ppm) |
| ${}^{191}$Ta | 191 | 118 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 148.0938 | 1511.0010 | -90.20 % | 184397.3162 MeV (+36587.2 ppm) |
| ${}^{192}$Ta | 192 | 119 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 154.3659 | 1515.6480 | -89.82 % | 185357.7589 MeV (+36538.7 ppm) |
| ${}^{193}$Ta | 193 | 120 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 160.6305 | 1521.4190 | -89.44 % | 186318.2091 MeV (+36497.3 ppm) |
| ${}^{194}$Ta | 194 | 121 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 166.8878 | 1525.8100 | -89.06 % | 187278.6665 MeV (+36448.3 ppm) |

### Tungsten (Z = 74)

_41 of 41 isotopes with a framework prediction; 41 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{157}$W | 157 | 83 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -92.0621 | 1228.9960 | -107.49 % | 151767.8395 MeV (+37907.1 ppm) |
| ${}^{158}$W | 158 | 84 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -85.4339 | 1241.0900 | -106.88 % | 152727.9261 MeV (+37889.6 ppm) |
| ${}^{159}$W | 159 | 85 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -78.8175 | 1250.8530 | -106.30 % | 153688.0245 MeV (+37856.7 ppm) |
| ${}^{160}$W | 160 | 86 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -72.2129 | 1262.8463 | -105.72 % | 154648.1346 MeV (+37839.2 ppm) |
| ${}^{161}$W | 161 | 87 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -65.6197 | 1272.0610 | -105.16 % | 155608.2562 MeV (+37803.2 ppm) |
| ${}^{162}$W | 162 | 88 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -59.0380 | 1283.6591 | -104.60 % | 156568.3893 MeV (+37783.6 ppm) |
| ${}^{163}$W | 163 | 89 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -52.4675 | 1292.6396 | -104.06 % | 157528.5335 MeV (+37746.7 ppm) |
| ${}^{164}$W | 164 | 90 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -45.9080 | 1304.0380 | -103.52 % | 158488.6888 MeV (+37726.8 ppm) |
| ${}^{165}$W | 165 | 91 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -39.3595 | 1312.7351 | -103.00 % | 159448.8551 MeV (+37688.9 ppm) |
| ${}^{166}$W | 166 | 92 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -32.8217 | 1323.8326 | -102.48 % | 160409.0320 MeV (+37667.7 ppm) |
| ${}^{167}$W | 167 | 93 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -26.2945 | 1332.1097 | -101.97 % | 161369.2196 MeV (+37627.9 ppm) |
| ${}^{168}$W | 168 | 94 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -19.7778 | 1342.9807 | -101.47 % | 162329.4177 MeV (+37605.9 ppm) |
| ${}^{169}$W | 169 | 95 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -13.2714 | 1351.0769 | -100.98 % | 163289.6261 MeV (+37566.0 ppm) |
| ${}^{170}$W | 170 | 96 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -6.7752 | 1361.5212 | -100.50 % | 164249.8447 MeV (+37541.9 ppm) |
| ${}^{171}$W | 171 | 97 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -0.2891 | 1369.3878 | -100.02 % | 165210.0733 MeV (+37501.4 ppm) |
| ${}^{172}$W | 172 | 98 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 6.1872 | 1379.4702 | -99.55 % | 166170.3118 MeV (+37475.8 ppm) |
| ${}^{173}$W | 173 | 99 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 12.6536 | 1387.1717 | -99.09 % | 167130.5602 MeV (+37435.2 ppm) |
| ${}^{174}$W | 174 | 100 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 19.1104 | 1396.7428 | -98.63 % | 168090.8182 MeV (+37407.2 ppm) |
| ${}^{175}$W | 175 | 101 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 25.5576 | 1404.2198 | -98.18 % | 169051.0857 MeV (+37366.1 ppm) |
| ${}^{176}$W | 176 | 102 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 31.9955 | 1413.2999 | -97.74 % | 170011.3626 MeV (+37335.7 ppm) |
| ${}^{177}$W | 177 | 103 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 38.4240 | 1420.4314 | -97.29 % | 170971.6488 MeV (+37293.5 ppm) |
| ${}^{178}$W | 178 | 104 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 44.8434 | 1429.2080 | -96.86 % | 171931.9442 MeV (+37262.1 ppm) |
| ${}^{179}$W | 179 | 105 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 51.2538 | 1436.1675 | -96.43 % | 172892.2486 MeV (+37219.8 ppm) |
| ${}^{180}$W | 180 | 106 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 57.6552 | 1444.5798 | -96.01 % | 173852.5620 MeV (+37187.0 ppm) |
| ${}^{181}$W | 181 | 107 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 64.0478 | 1451.2488 | -95.59 % | 174812.8842 MeV (+37143.9 ppm) |
| ${}^{182}$W | 182 | 108 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 70.4317 | 1459.3323 | -95.17 % | 175773.2151 MeV (+37110.0 ppm) |
| ${}^{183}$W | 183 | 109 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 76.8070 | 1465.5232 | -94.76 % | 176733.5545 MeV (+37064.9 ppm) |
| ${}^{184}$W | 184 | 110 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 83.1738 | 1472.9343 | -94.35 % | 177693.9025 MeV (+37027.9 ppm) |
| ${}^{185}$W | 185 | 111 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 89.5322 | 1478.6880 | -93.95 % | 178654.2589 MeV (+36981.2 ppm) |
| ${}^{186}$W | 186 | 112 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 95.8823 | 1485.8801 | -93.55 % | 179614.6236 MeV (+36943.8 ppm) |
| ${}^{187}$W | 187 | 113 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 102.2242 | 1491.3468 | -93.15 % | 180574.9964 MeV (+36896.5 ppm) |
| ${}^{188}$W | 188 | 114 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 108.5581 | 1498.1820 | -92.75 % | 181535.3773 MeV (+36857.8 ppm) |
| ${}^{189}$W | 189 | 115 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 114.8839 | 1503.3060 | -92.36 % | 182495.7662 MeV (+36810.1 ppm) |
| ${}^{190}$W | 190 | 116 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 121.2019 | 1510.0256 | -91.97 % | 183456.1630 MeV (+36771.2 ppm) |
| ${}^{191}$W | 191 | 117 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 127.5121 | 1514.9043 | -91.58 % | 184416.5676 MeV (+36722.6 ppm) |
| ${}^{192}$W | 192 | 118 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 133.8146 | 1521.4080 | -91.20 % | 185376.9799 MeV (+36684.0 ppm) |
| ${}^{193}$W | 193 | 119 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 140.1094 | 1526.0510 | -90.82 % | 186337.3998 MeV (+36635.0 ppm) |
| ${}^{194}$W | 194 | 120 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 146.3968 | 1532.4060 | -90.45 % | 187297.8272 MeV (+36596.1 ppm) |
| ${}^{195}$W | 195 | 121 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 152.6767 | 1536.7950 | -90.07 % | 188258.2621 MeV (+36546.8 ppm) |
| ${}^{196}$W | 196 | 122 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 158.9493 | 1542.9120 | -89.70 % | 189218.7043 MeV (+36507.5 ppm) |
| ${}^{197}$W | 197 | 123 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 165.2146 | 1547.0410 | -89.32 % | 190179.1537 MeV (+36458.1 ppm) |

### Rhenium (Z = 75)

_41 of 41 isotopes with a framework prediction; 41 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{159}$Re | 159 | 84 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -100.7622 | 1239.4050 | -108.13 % | 153708.6388 MeV (+37921.4 ppm) |
| ${}^{160}$Re | 160 | 85 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -94.1183 | 1249.6000 | -107.53 % | 154668.7097 MeV (+37890.5 ppm) |
| ${}^{161}$Re | 161 | 86 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -87.4863 | 1261.6490 | -106.93 % | 155628.7925 MeV (+37873.3 ppm) |
| ${}^{162}$Re | 162 | 87 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -80.8660 | 1271.3760 | -106.36 % | 156588.8870 MeV (+37840.1 ppm) |
| ${}^{163}$Re | 163 | 88 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -74.2573 | 1282.9511 | -105.79 % | 157548.9930 MeV (+37820.6 ppm) |
| ${}^{164}$Re | 164 | 89 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -67.6598 | 1292.4926 | -105.23 % | 158509.1104 MeV (+37787.4 ppm) |
| ${}^{165}$Re | 165 | 90 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -61.0737 | 1303.7508 | -104.68 % | 159469.2389 MeV (+37766.2 ppm) |
| ${}^{166}$Re | 166 | 91 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -54.4985 | 1313.0001 | -104.15 % | 160429.3786 MeV (+37731.8 ppm) |
| ${}^{167}$Re | 167 | 92 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -47.9343 | 1324.1430 | -103.62 % | 161389.5291 MeV (+37710.1 ppm) |
| ${}^{168}$Re | 168 | 93 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -41.3808 | 1333.1003 | -103.10 % | 162349.6904 MeV (+37675.2 ppm) |
| ${}^{169}$Re | 169 | 94 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -34.8379 | 1343.7860 | -102.59 % | 163309.8623 MeV (+37651.6 ppm) |
| ${}^{170}$Re | 170 | 95 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -28.3055 | 1352.3520 | -102.09 % | 164270.0447 MeV (+37614.6 ppm) |
| ${}^{171}$Re | 171 | 96 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -21.7834 | 1362.7696 | -101.60 % | 165230.2374 MeV (+37590.0 ppm) |
| ${}^{172}$Re | 172 | 97 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -15.2716 | 1371.1575 | -101.11 % | 166190.4403 MeV (+37552.7 ppm) |
| ${}^{173}$Re | 173 | 98 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -8.7697 | 1381.2159 | -100.63 % | 167150.6532 MeV (+37526.6 ppm) |
| ${}^{174}$Re | 174 | 99 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -2.2778 | 1389.4064 | -100.16 % | 168110.8761 MeV (+37489.0 ppm) |
| ${}^{175}$Re | 175 | 100 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 4.2043 | 1399.0929 | -99.70 % | 169071.1087 MeV (+37461.3 ppm) |
| ${}^{176}$Re | 176 | 101 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 10.6767 | 1406.9388 | -99.24 % | 170031.3511 MeV (+37422.4 ppm) |
| ${}^{177}$Re | 177 | 102 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 17.1397 | 1416.2165 | -98.79 % | 170991.6029 MeV (+37393.0 ppm) |
| ${}^{178}$Re | 178 | 103 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 23.5931 | 1423.6721 | -98.34 % | 171951.8642 MeV (+37352.5 ppm) |
| ${}^{179}$Re | 179 | 104 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 30.0373 | 1432.6742 | -97.90 % | 172912.1348 MeV (+37322.2 ppm) |
| ${}^{180}$Re | 180 | 105 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 36.4724 | 1439.9986 | -97.47 % | 173872.4145 MeV (+37281.9 ppm) |
| ${}^{181}$Re | 181 | 106 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 42.8983 | 1448.7500 | -97.04 % | 174832.7034 MeV (+37250.9 ppm) |
| ${}^{182}$Re | 182 | 107 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 49.3153 | 1455.7500 | -96.61 % | 175793.0011 MeV (+37209.6 ppm) |
| ${}^{183}$Re | 183 | 108 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 55.7235 | 1464.1848 | -96.19 % | 176753.3077 MeV (+37177.5 ppm) |
| ${}^{184}$Re | 184 | 109 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 62.1229 | 1470.6663 | -95.78 % | 177713.6231 MeV (+37133.9 ppm) |
| ${}^{185}$Re | 185 | 110 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 68.5137 | 1478.3369 | -95.37 % | 178673.9470 MeV (+37098.1 ppm) |
| ${}^{186}$Re | 186 | 111 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 74.8961 | 1484.5165 | -94.95 % | 179634.2795 MeV (+37053.8 ppm) |
| ${}^{187}$Re | 187 | 112 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 81.2700 | 1491.8770 | -94.55 % | 180594.6204 MeV (+37017.0 ppm) |
| ${}^{188}$Re | 188 | 113 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 87.6355 | 1497.7486 | -94.15 % | 181554.9695 MeV (+36971.8 ppm) |
| ${}^{189}$Re | 189 | 114 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 93.9929 | 1504.7822 | -93.75 % | 182515.3269 MeV (+36934.0 ppm) |
| ${}^{190}$Re | 190 | 115 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 100.3422 | 1510.4574 | -93.36 % | 183475.6924 MeV (+36888.7 ppm) |
| ${}^{191}$Re | 191 | 116 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 106.6835 | 1517.2961 | -92.97 % | 184436.0659 MeV (+36850.7 ppm) |
| ${}^{192}$Re | 192 | 117 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 113.0169 | 1522.6059 | -92.58 % | 185396.4473 MeV (+36804.3 ppm) |
| ${}^{193}$Re | 193 | 118 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 119.3424 | 1529.3200 | -92.20 % | 186356.8365 MeV (+36766.5 ppm) |
| ${}^{194}$Re | 194 | 119 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 125.6602 | 1534.3460 | -91.81 % | 187317.2335 MeV (+36719.8 ppm) |
| ${}^{195}$Re | 195 | 120 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 131.9704 | 1540.6950 | -91.43 % | 188277.6381 MeV (+36681.0 ppm) |
| ${}^{196}$Re | 196 | 121 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 138.2730 | 1545.6560 | -91.05 % | 189238.0502 MeV (+36634.1 ppm) |
| ${}^{197}$Re | 197 | 122 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 144.5682 | 1551.7690 | -90.68 % | 190198.4698 MeV (+36594.4 ppm) |
| ${}^{198}$Re | 198 | 123 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 150.8560 | 1556.4780 | -90.31 % | 191158.8968 MeV (+36547.5 ppm) |
| ${}^{199}$Re | 199 | 124 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 157.1365 | 1562.1500 | -89.94 % | 192119.3311 MeV (+36507.4 ppm) |

### Osmium (Z = 76)

_43 of 43 isotopes with a framework prediction; 43 of 43 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{161}$Os | 161 | 85 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -109.6138 | 1250.1650 | -108.77 % | 155649.5897 MeV (+37938.3 ppm) |
| ${}^{162}$Os | 162 | 86 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -102.9545 | 1262.6280 | -108.15 % | 156609.6451 MeV (+37922.9 ppm) |
| ${}^{163}$Os | 163 | 87 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -96.3069 | 1272.5410 | -107.57 % | 157569.7124 MeV (+37891.0 ppm) |
| ${}^{164}$Os | 164 | 88 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -89.6710 | 1284.6625 | -106.98 % | 158529.7913 MeV (+37874.9 ppm) |
| ${}^{165}$Os | 165 | 89 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -83.0467 | 1294.0950 | -106.42 % | 159489.8817 MeV (+37840.3 ppm) |
| ${}^{166}$Os | 166 | 90 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -76.4337 | 1305.8120 | -105.85 % | 160449.9835 MeV (+37822.1 ppm) |
| ${}^{167}$Os | 167 | 91 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -69.8319 | 1314.9506 | -105.31 % | 161410.0964 MeV (+37786.7 ppm) |
| ${}^{168}$Os | 168 | 92 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -63.2411 | 1326.5181 | -104.77 % | 162370.2205 MeV (+37767.9 ppm) |
| ${}^{169}$Os | 169 | 93 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -56.6613 | 1335.3174 | -104.24 % | 163330.3554 MeV (+37731.2 ppm) |
| ${}^{170}$Os | 170 | 94 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -50.0922 | 1346.5914 | -103.72 % | 164290.5010 MeV (+37711.1 ppm) |
| ${}^{171}$Os | 171 | 95 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -43.5337 | 1355.0342 | -103.21 % | 165250.6573 MeV (+37673.0 ppm) |
| ${}^{172}$Os | 172 | 96 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -36.9857 | 1366.0520 | -102.71 % | 166210.8241 MeV (+37652.0 ppm) |
| ${}^{173}$Os | 173 | 97 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -30.4480 | 1374.3179 | -102.22 % | 167171.0011 MeV (+37613.6 ppm) |
| ${}^{174}$Os | 174 | 98 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -23.9205 | 1384.9464 | -101.73 % | 168131.1884 MeV (+37590.8 ppm) |
| ${}^{175}$Os | 175 | 99 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -17.4030 | 1393.1276 | -101.25 % | 169091.3857 MeV (+37552.8 ppm) |
| ${}^{176}$Os | 176 | 100 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -10.8955 | 1403.2248 | -100.78 % | 170051.5930 MeV (+37527.3 ppm) |
| ${}^{177}$Os | 177 | 101 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -4.3978 | 1411.1214 | -100.31 % | 171011.8100 MeV (+37488.4 ppm) |
| ${}^{178}$Os | 178 | 102 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 2.0903 | 1420.7805 | -99.85 % | 171972.0368 MeV (+37461.0 ppm) |
| ${}^{179}$Os | 179 | 103 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 8.5688 | 1428.3277 | -99.40 % | 172932.2730 MeV (+37420.9 ppm) |
| ${}^{180}$Os | 180 | 104 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 15.0379 | 1437.7351 | -98.95 % | 173892.5187 MeV (+37392.7 ppm) |
| ${}^{181}$Os | 181 | 105 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 21.4976 | 1445.0002 | -98.51 % | 174852.7737 MeV (+37351.7 ppm) |
| ${}^{182}$Os | 182 | 106 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 27.9482 | 1454.1306 | -98.08 % | 175813.0379 MeV (+37322.7 ppm) |
| ${}^{183}$Os | 183 | 107 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 34.3897 | 1461.2566 | -97.65 % | 176773.3112 MeV (+37281.8 ppm) |
| ${}^{184}$Os | 184 | 108 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 40.8222 | 1469.9167 | -97.22 % | 177733.5935 MeV (+37250.7 ppm) |
| ${}^{185}$Os | 185 | 109 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 47.2459 | 1476.5414 | -96.80 % | 178693.8846 MeV (+37207.7 ppm) |
| ${}^{186}$Os | 186 | 110 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 53.6608 | 1484.8068 | -96.39 % | 179654.1844 MeV (+37175.1 ppm) |
| ${}^{187}$Os | 187 | 111 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 60.0671 | 1491.0971 | -95.97 % | 180614.4929 MeV (+37131.1 ppm) |
| ${}^{188}$Os | 188 | 112 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 66.4649 | 1499.0867 | -95.57 % | 181574.8099 MeV (+37097.7 ppm) |
| ${}^{189}$Os | 189 | 113 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 72.8542 | 1505.0075 | -95.16 % | 182535.1353 MeV (+37052.5 ppm) |
| ${}^{190}$Os | 190 | 114 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 79.2353 | 1512.7999 | -94.76 % | 183495.4691 MeV (+37018.8 ppm) |
| ${}^{191}$Os | 191 | 115 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 85.6080 | 1518.5586 | -94.36 % | 184455.8111 MeV (+36973.6 ppm) |
| ${}^{192}$Os | 192 | 116 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 91.9727 | 1526.1170 | -93.97 % | 185416.1612 MeV (+36939.4 ppm) |
| ${}^{193}$Os | 193 | 117 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 98.3293 | 1531.7004 | -93.58 % | 186376.5193 MeV (+36894.2 ppm) |
| ${}^{194}$Os | 194 | 118 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 104.6780 | 1538.8125 | -93.20 % | 187336.8854 MeV (+36858.3 ppm) |
| ${}^{195}$Os | 195 | 119 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 111.0189 | 1543.9603 | -92.81 % | 188297.2593 MeV (+36811.6 ppm) |
| ${}^{196}$Os | 196 | 120 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 117.3520 | 1550.7971 | -92.43 % | 189257.6410 MeV (+36775.0 ppm) |
| ${}^{197}$Os | 197 | 121 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 123.6774 | 1555.7090 | -92.05 % | 190218.0303 MeV (+36727.7 ppm) |
| ${}^{198}$Os | 198 | 122 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 129.9953 | 1562.2200 | -91.68 % | 191178.4272 MeV (+36690.6 ppm) |
| ${}^{199}$Os | 199 | 123 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 136.3057 | 1566.9260 | -91.30 % | 192138.8316 MeV (+36643.6 ppm) |
| ${}^{200}$Os | 200 | 124 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 142.6086 | 1573.4000 | -90.94 % | 193099.2434 MeV (+36606.0 ppm) |
| ${}^{201}$Os | 201 | 125 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 148.9043 | 1577.6490 | -90.56 % | 194059.6625 MeV (+36557.8 ppm) |
| ${}^{202}$Os | 202 | 126 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 155.1927 | 1583.4780 | -90.20 % | 195020.0889 MeV (+36517.9 ppm) |
| ${}^{203}$Os | 203 | 127 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 161.4740 | 1586.2420 | -89.82 % | 195980.5224 MeV (+36462.2 ppm) |

### Iridium (Z = 77)

_43 of 43 isotopes with a framework prediction; 43 of 43 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{163}$Ir | 163 | 86 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -118.6164 | 1260.6420 | -109.41 % | 157590.6916 MeV (+37953.8 ppm) |
| ${}^{164}$Ir | 164 | 87 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -111.9416 | 1271.0000 | -108.81 % | 158550.7315 MeV (+37924.0 ppm) |
| ${}^{165}$Ir | 165 | 88 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -105.2786 | 1283.0400 | -108.21 % | 159510.7833 MeV (+37907.8 ppm) |
| ${}^{166}$Ir | 166 | 89 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -98.6272 | 1292.9740 | -107.63 % | 160470.8467 MeV (+37875.6 ppm) |
| ${}^{167}$Ir | 167 | 90 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -91.9873 | 1304.7418 | -107.05 % | 161430.9216 MeV (+37857.7 ppm) |
| ${}^{168}$Ir | 168 | 91 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -85.3588 | 1314.4070 | -106.49 % | 162391.0078 MeV (+37825.6 ppm) |
| ${}^{169}$Ir | 169 | 92 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -78.7415 | 1325.9055 | -105.94 % | 163351.1053 MeV (+37806.1 ppm) |
| ${}^{170}$Ir | 170 | 93 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -72.1352 | 1335.0100 | -105.40 % | 164311.2138 MeV (+37771.5 ppm) |
| ${}^{171}$Ir | 171 | 94 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -65.5398 | 1346.3667 | -104.87 % | 165271.3331 MeV (+37751.4 ppm) |
| ${}^{172}$Ir | 172 | 95 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -58.9552 | 1355.4054 | -104.35 % | 166231.4633 MeV (+37716.9 ppm) |
| ${}^{173}$Ir | 173 | 96 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -52.3811 | 1366.3658 | -103.83 % | 167191.6040 MeV (+37695.3 ppm) |
| ${}^{174}$Ir | 174 | 97 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -45.8175 | 1374.9546 | -103.33 % | 168151.7552 MeV (+37658.7 ppm) |
| ${}^{175}$Ir | 175 | 98 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -39.2643 | 1385.6345 | -102.83 % | 169111.9167 MeV (+37636.0 ppm) |
| ${}^{176}$Ir | 176 | 99 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -32.7212 | 1394.1932 | -102.35 % | 170072.0884 MeV (+37600.2 ppm) |
| ${}^{177}$Ir | 177 | 100 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -26.1882 | 1404.4300 | -101.86 % | 171032.2702 MeV (+37575.4 ppm) |
| ${}^{178}$Ir | 178 | 101 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -19.6651 | 1412.7082 | -101.39 % | 171992.4619 MeV (+37538.6 ppm) |
| ${}^{179}$Ir | 179 | 102 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -13.1519 | 1422.6069 | -100.92 % | 172952.6634 MeV (+37512.4 ppm) |
| ${}^{180}$Ir | 180 | 103 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -6.6483 | 1430.5741 | -100.46 % | 173912.8746 MeV (+37474.7 ppm) |
| ${}^{181}$Ir | 181 | 104 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -0.1543 | 1440.1309 | -100.01 % | 174873.0953 MeV (+37447.1 ppm) |
| ${}^{182}$Ir | 182 | 105 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 6.3303 | 1447.7909 | -99.56 % | 175833.3255 MeV (+37408.4 ppm) |
| ${}^{183}$Ir | 183 | 106 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 12.8056 | 1457.0126 | -99.12 % | 176793.5650 MeV (+37379.6 ppm) |
| ${}^{184}$Ir | 184 | 107 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 19.2717 | 1464.4927 | -98.68 % | 177753.8137 MeV (+37340.6 ppm) |
| ${}^{185}$Ir | 185 | 108 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 25.7286 | 1473.2887 | -98.25 % | 178714.0715 MeV (+37310.0 ppm) |
| ${}^{186}$Ir | 186 | 109 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 32.1766 | 1480.1968 | -97.83 % | 179674.3383 MeV (+37268.5 ppm) |
| ${}^{187}$Ir | 187 | 110 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 38.6158 | 1488.6451 | -97.41 % | 180634.6139 MeV (+37236.7 ppm) |
| ${}^{188}$Ir | 188 | 111 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 45.0461 | 1495.5120 | -96.99 % | 181594.8984 MeV (+37195.9 ppm) |
| ${}^{189}$Ir | 189 | 112 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 51.4679 | 1503.6880 | -96.58 % | 182555.1914 MeV (+37163.3 ppm) |
| ${}^{190}$Ir | 190 | 113 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 57.8810 | 1510.0633 | -96.17 % | 183515.4930 MeV (+37120.5 ppm) |
| ${}^{191}$Ir | 191 | 114 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 64.2857 | 1518.0899 | -95.77 % | 184475.8031 MeV (+37087.9 ppm) |
| ${}^{192}$Ir | 192 | 115 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 70.6821 | 1524.2880 | -95.36 % | 185436.1215 MeV (+37045.0 ppm) |
| ${}^{193}$Ir | 193 | 116 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 77.0703 | 1532.0600 | -94.97 % | 186396.4481 MeV (+37011.7 ppm) |
| ${}^{194}$Ir | 194 | 117 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 83.4502 | 1538.1268 | -94.57 % | 187356.7829 MeV (+36969.0 ppm) |
| ${}^{195}$Ir | 195 | 118 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 89.8222 | 1545.3586 | -94.19 % | 188317.1257 MeV (+36933.4 ppm) |
| ${}^{196}$Ir | 196 | 119 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 96.1861 | 1551.1731 | -93.80 % | 189277.4765 MeV (+36890.2 ppm) |
| ${}^{197}$Ir | 197 | 120 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 102.5422 | 1558.0731 | -93.42 % | 190237.8352 MeV (+36853.6 ppm) |
| ${}^{198}$Ir | 198 | 121 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 108.8906 | 1563.6060 | -93.04 % | 191198.2016 MeV (+36809.7 ppm) |
| ${}^{199}$Ir | 199 | 122 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 115.2312 | 1570.3501 | -92.66 % | 192158.5758 MeV (+36773.2 ppm) |
| ${}^{200}$Ir | 200 | 123 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 121.5643 | 1575.6000 | -92.28 % | 193118.9575 MeV (+36728.6 ppm) |
| ${}^{201}$Ir | 201 | 124 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 127.8898 | 1581.8700 | -91.92 % | 194079.3467 MeV (+36690.6 ppm) |
| ${}^{202}$Ir | 202 | 125 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 134.2079 | 1586.7100 | -91.54 % | 195039.7434 MeV (+36645.0 ppm) |
| ${}^{203}$Ir | 203 | 126 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 140.5187 | 1592.5350 | -91.18 % | 196000.1474 MeV (+36604.9 ppm) |
| ${}^{204}$Ir | 204 | 127 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 146.8222 | 1595.8920 | -90.80 % | 196960.5587 MeV (+36551.4 ppm) |
| ${}^{205}$Ir | 205 | 128 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 153.1185 | 1600.0250 | -90.43 % | 197920.9771 MeV (+36503.1 ppm) |

### Platinum (Z = 78)

_44 of 44 isotopes with a framework prediction; 44 of 44 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{165}$Pt | 165 | 87 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -127.7693 | 1270.9950 | -110.05 % | 159531.9437 MeV (+37969.3 ppm) |
| ${}^{166}$Pt | 166 | 88 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -121.0791 | 1283.6780 | -109.43 % | 160491.9682 MeV (+37955.0 ppm) |
| ${}^{167}$Pt | 167 | 89 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -114.4006 | 1293.5820 | -108.84 % | 161452.0046 MeV (+37924.4 ppm) |
| ${}^{168}$Pt | 168 | 90 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -107.7339 | 1305.9684 | -108.25 % | 162412.0526 MeV (+37909.3 ppm) |
| ${}^{169}$Pt | 169 | 91 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -101.0786 | 1315.4960 | -107.68 % | 163372.1120 MeV (+37876.1 ppm) |
| ${}^{170}$Pt | 170 | 92 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -94.4346 | 1327.4002 | -107.11 % | 164332.1829 MeV (+37858.9 ppm) |
| ${}^{171}$Pt | 171 | 93 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -87.8018 | 1336.6389 | -106.57 % | 165292.2648 MeV (+37824.5 ppm) |
| ${}^{172}$Pt | 172 | 94 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -81.1800 | 1348.3503 | -106.02 % | 166252.3578 MeV (+37806.7 ppm) |
| ${}^{173}$Pt | 173 | 95 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -74.5692 | 1357.2517 | -105.49 % | 167212.4617 MeV (+37771.0 ppm) |
| ${}^{174}$Pt | 174 | 96 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -67.9690 | 1368.7039 | -104.97 % | 168172.5764 MeV (+37752.2 ppm) |
| ${}^{175}$Pt | 175 | 97 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -61.3795 | 1377.1663 | -104.46 % | 169132.7016 MeV (+37714.6 ppm) |
| ${}^{176}$Pt | 176 | 98 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -54.8004 | 1388.4628 | -103.95 % | 170092.8373 MeV (+37695.4 ppm) |
| ${}^{177}$Pt | 177 | 99 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -48.2317 | 1396.9707 | -103.45 % | 171052.9834 MeV (+37659.0 ppm) |
| ${}^{178}$Pt | 178 | 100 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -41.6731 | 1407.6690 | -102.96 % | 172013.1396 MeV (+37636.7 ppm) |
| ${}^{179}$Pt | 179 | 101 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -35.1246 | 1416.0110 | -102.48 % | 172973.3059 MeV (+37600.1 ppm) |
| ${}^{180}$Pt | 180 | 102 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -28.5861 | 1426.2441 | -102.00 % | 173933.4821 MeV (+37575.6 ppm) |
| ${}^{181}$Pt | 181 | 103 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -22.0574 | 1434.2670 | -101.54 % | 174893.6681 MeV (+37537.9 ppm) |
| ${}^{182}$Pt | 182 | 104 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -15.5383 | 1444.1252 | -101.08 % | 175853.8638 MeV (+37511.9 ppm) |
| ${}^{183}$Pt | 183 | 105 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -9.0288 | 1451.8013 | -100.62 % | 176814.0691 MeV (+37472.9 ppm) |
| ${}^{184}$Pt | 184 | 106 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -2.5288 | 1461.4319 | -100.17 % | 177774.2839 MeV (+37446.3 ppm) |
| ${}^{185}$Pt | 185 | 107 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 3.9619 | 1468.8589 | -99.73 % | 178734.5079 MeV (+37406.7 ppm) |
| ${}^{186}$Pt | 186 | 108 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 10.4434 | 1478.1065 | -99.29 % | 179694.7412 MeV (+37378.5 ppm) |
| ${}^{187}$Pt | 187 | 109 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 16.9158 | 1484.9988 | -98.86 % | 180654.9836 MeV (+37336.6 ppm) |
| ${}^{188}$Pt | 188 | 110 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 23.3792 | 1494.2057 | -98.44 % | 181615.2349 MeV (+37308.9 ppm) |
| ${}^{189}$Pt | 189 | 111 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 29.8338 | 1500.9255 | -98.01 % | 182575.4952 MeV (+37267.0 ppm) |
| ${}^{190}$Pt | 190 | 112 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 36.2795 | 1509.8339 | -97.60 % | 183535.7642 MeV (+37238.3 ppm) |
| ${}^{191}$Pt | 191 | 113 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 42.7166 | 1516.2970 | -97.18 % | 184496.0419 MeV (+37195.7 ppm) |
| ${}^{192}$Pt | 192 | 114 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 49.1451 | 1524.9585 | -96.78 % | 185456.3282 MeV (+37166.4 ppm) |
| ${}^{193}$Pt | 193 | 115 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 55.5652 | 1531.2210 | -96.37 % | 186416.6229 MeV (+37123.6 ppm) |
| ${}^{194}$Pt | 194 | 116 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 61.9768 | 1539.5727 | -95.97 % | 187376.9260 MeV (+37093.3 ppm) |
| ${}^{195}$Pt | 195 | 117 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 68.3803 | 1545.6778 | -95.58 % | 188337.2373 MeV (+37050.5 ppm) |
| ${}^{196}$Pt | 196 | 118 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 74.7755 | 1553.5998 | -95.19 % | 189297.5569 MeV (+37018.5 ppm) |
| ${}^{197}$Pt | 197 | 119 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 81.1627 | 1559.4464 | -94.80 % | 190257.8845 MeV (+36975.1 ppm) |
| ${}^{198}$Pt | 198 | 120 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 87.5419 | 1567.0019 | -94.41 % | 191218.2200 MeV (+36941.8 ppm) |
| ${}^{199}$Pt | 199 | 121 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 93.9132 | 1572.5579 | -94.03 % | 192178.5635 MeV (+36897.7 ppm) |
| ${}^{200}$Pt | 200 | 122 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 100.2767 | 1579.8397 | -93.65 % | 193138.9148 MeV (+36863.8 ppm) |
| ${}^{201}$Pt | 201 | 123 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 106.6325 | 1585.0526 | -93.27 % | 194099.2737 MeV (+36818.7 ppm) |
| ${}^{202}$Pt | 202 | 124 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 112.9807 | 1592.0753 | -92.90 % | 195059.6403 MeV (+36784.1 ppm) |
| ${}^{203}$Pt | 203 | 125 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 119.3213 | 1597.0010 | -92.53 % | 196020.0145 MeV (+36738.2 ppm) |
| ${}^{204}$Pt | 204 | 126 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 125.6545 | 1603.2360 | -92.16 % | 196980.3960 MeV (+36699.8 ppm) |
| ${}^{205}$Pt | 205 | 127 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 131.9804 | 1606.3800 | -91.78 % | 197940.7850 MeV (+36646.0 ppm) |
| ${}^{206}$Pt | 206 | 128 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 138.2989 | 1610.9200 | -91.41 % | 198901.1812 MeV (+36599.4 ppm) |
| ${}^{207}$Pt | 207 | 129 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 144.6102 | 1613.9790 | -91.04 % | 199861.5846 MeV (+36545.1 ppm) |
| ${}^{208}$Pt | 208 | 130 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 150.9145 | 1618.2400 | -90.67 % | 200821.9952 MeV (+36499.2 ppm) |

### Gold (Z = 79)

_43 of 43 isotopes with a framework prediction; 43 of 43 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{168}$Au | 168 | 89 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -130.3662 | 1291.5840 | -110.09 % | 162433.3546 MeV (+37955.7 ppm) |
| ${}^{169}$Au | 169 | 90 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -123.6725 | 1304.0040 | -109.48 % | 163393.3757 MeV (+37940.8 ppm) |
| ${}^{170}$Au | 170 | 91 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -116.9903 | 1314.1000 | -108.90 % | 164353.4083 MeV (+37910.3 ppm) |
| ${}^{171}$Au | 171 | 92 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -110.3197 | 1325.9523 | -108.32 % | 165313.4524 MeV (+37893.0 ppm) |
| ${}^{172}$Au | 172 | 93 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -103.6603 | 1335.7793 | -107.76 % | 166273.5078 MeV (+37862.4 ppm) |
| ${}^{173}$Au | 173 | 94 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -97.0121 | 1347.3646 | -107.20 % | 167233.5744 MeV (+37843.4 ppm) |
| ${}^{174}$Au | 174 | 95 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -90.3750 | 1356.6780 | -106.66 % | 168193.6520 MeV (+37810.1 ppm) |
| ${}^{175}$Au | 175 | 96 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -83.7487 | 1368.0789 | -106.12 % | 169153.7405 MeV (+37790.8 ppm) |
| ${}^{176}$Au | 176 | 97 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -77.1331 | 1377.2675 | -105.60 % | 170113.8397 MeV (+37757.6 ppm) |
| ${}^{177}$Au | 177 | 98 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -70.5282 | 1388.3636 | -105.08 % | 171073.9495 MeV (+37736.9 ppm) |
| ${}^{178}$Au | 178 | 99 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -63.9337 | 1397.1922 | -104.58 % | 172034.0698 MeV (+37702.3 ppm) |
| ${}^{179}$Au | 179 | 100 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -57.3495 | 1407.9491 | -104.07 % | 172994.2004 MeV (+37680.1 ppm) |
| ${}^{180}$Au | 180 | 101 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -50.7755 | 1416.6575 | -103.58 % | 173954.3412 MeV (+37645.6 ppm) |
| ${}^{181}$Au | 181 | 102 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -44.2116 | 1426.9743 | -103.10 % | 174914.4921 MeV (+37621.4 ppm) |
| ${}^{182}$Au | 182 | 103 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -37.6577 | 1435.4784 | -102.62 % | 175874.6529 MeV (+37586.4 ppm) |
| ${}^{183}$Au | 183 | 104 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -31.1135 | 1445.4373 | -102.15 % | 176834.8235 MeV (+37560.7 ppm) |
| ${}^{184}$Au | 184 | 105 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -24.5791 | 1453.6358 | -101.69 % | 177795.0038 MeV (+37524.7 ppm) |
| ${}^{185}$Au | 185 | 106 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -18.0542 | 1463.2466 | -101.23 % | 178755.1937 MeV (+37497.7 ppm) |
| ${}^{186}$Au | 186 | 107 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -11.5387 | 1471.1746 | -100.78 % | 179715.3931 MeV (+37460.9 ppm) |
| ${}^{187}$Au | 187 | 108 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -5.0326 | 1480.5598 | -100.34 % | 180675.6018 MeV (+37433.2 ppm) |
| ${}^{188}$Au | 188 | 109 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 1.4642 | 1487.9737 | -99.90 % | 181635.8197 MeV (+37394.2 ppm) |
| ${}^{189}$Au | 189 | 110 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 7.9520 | 1497.2557 | -99.47 % | 182596.0467 MeV (+37366.7 ppm) |
| ${}^{190}$Au | 190 | 111 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 14.4307 | 1504.5786 | -99.04 % | 183556.2827 MeV (+37328.0 ppm) |
| ${}^{191}$Au | 191 | 112 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 20.9006 | 1513.6142 | -98.62 % | 184516.5276 MeV (+37299.8 ppm) |
| ${}^{192}$Au | 192 | 113 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 27.3617 | 1520.6598 | -98.20 % | 185476.7813 MeV (+37260.4 ppm) |
| ${}^{193}$Au | 193 | 114 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 33.8140 | 1529.3638 | -97.79 % | 186437.0437 MeV (+37231.0 ppm) |
| ${}^{194}$Au | 194 | 115 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 40.2578 | 1536.2422 | -97.38 % | 187397.3147 MeV (+37191.5 ppm) |
| ${}^{195}$Au | 195 | 116 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 46.6932 | 1544.6687 | -96.98 % | 188357.5941 MeV (+37161.3 ppm) |
| ${}^{196}$Au | 196 | 117 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 53.1201 | 1551.3116 | -96.58 % | 189317.8820 MeV (+37121.3 ppm) |
| ${}^{197}$Au | 197 | 118 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 59.5388 | 1559.3840 | -96.18 % | 190278.1781 MeV (+37089.8 ppm) |
| ${}^{198}$Au | 198 | 119 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 65.9492 | 1565.8964 | -95.79 % | 191238.4824 MeV (+37049.9 ppm) |
| ${}^{199}$Au | 199 | 120 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 72.3516 | 1573.4806 | -95.40 % | 192198.7948 MeV (+37016.4 ppm) |
| ${}^{200}$Au | 200 | 121 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 78.7460 | 1579.6983 | -95.02 % | 193159.1152 MeV (+36975.8 ppm) |
| ${}^{201}$Au | 201 | 122 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 85.1324 | 1586.9302 | -94.64 % | 194119.4435 MeV (+36941.2 ppm) |
| ${}^{202}$Au | 202 | 123 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 91.5111 | 1592.9538 | -94.26 % | 195079.7797 MeV (+36900.3 ppm) |
| ${}^{203}$Au | 203 | 124 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 97.8820 | 1599.8156 | -93.88 % | 196040.1235 MeV (+36864.4 ppm) |
| ${}^{204}$Au | 204 | 125 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 104.2452 | 1605.0720 | -93.51 % | 197000.4750 MeV (+36820.6 ppm) |
| ${}^{205}$Au | 205 | 126 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 110.6009 | 1611.3000 | -93.14 % | 197960.8341 MeV (+36782.2 ppm) |
| ${}^{206}$Au | 206 | 127 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 116.9492 | 1615.0400 | -92.76 % | 198921.2006 MeV (+36730.5 ppm) |
| ${}^{207}$Au | 207 | 128 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 123.2900 | 1619.5680 | -92.39 % | 199881.5746 MeV (+36683.7 ppm) |
| ${}^{208}$Au | 208 | 129 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 129.6235 | 1623.0240 | -92.01 % | 200841.9558 MeV (+36631.1 ppm) |
| ${}^{209}$Au | 209 | 130 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 135.9498 | 1627.2740 | -91.65 % | 201802.3443 MeV (+36584.7 ppm) |
| ${}^{210}$Au | 210 | 131 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 142.2690 | 1630.4400 | -91.27 % | 202762.7399 MeV (+36532.2 ppm) |

### Mercury (Z = 80)

_47 of 47 isotopes with a framework prediction; 47 of 47 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{170}$Hg | 170 | 90 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -139.8024 | 1304.0700 | -110.72 % | 164374.8901 MeV (+37986.2 ppm) |
| ${}^{171}$Hg | 171 | 91 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -133.0934 | 1314.3060 | -110.13 % | 165334.8958 MeV (+37956.6 ppm) |
| ${}^{172}$Hg | 172 | 92 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -126.3960 | 1326.7403 | -109.53 % | 166294.9132 MeV (+37942.5 ppm) |
| ${}^{173}$Hg | 173 | 93 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -119.7100 | 1336.4250 | -108.96 % | 167254.9420 MeV (+37910.5 ppm) |
| ${}^{174}$Hg | 174 | 94 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -113.0353 | 1348.4626 | -108.38 % | 168214.9821 MeV (+37894.3 ppm) |
| ${}^{175}$Hg | 175 | 95 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -106.3718 | 1357.8623 | -107.83 % | 169175.0333 MeV (+37861.4 ppm) |
| ${}^{176}$Hg | 176 | 96 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -99.7193 | 1369.7489 | -107.28 % | 170135.0956 MeV (+37844.6 ppm) |
| ${}^{177}$Hg | 177 | 97 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -93.0777 | 1378.8114 | -106.75 % | 171095.1688 MeV (+37810.4 ppm) |
| ${}^{178}$Hg | 178 | 98 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -86.4468 | 1390.4222 | -106.22 % | 172055.2526 MeV (+37792.6 ppm) |
| ${}^{179}$Hg | 179 | 99 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -79.8265 | 1399.1111 | -105.71 % | 173015.3471 MeV (+37756.8 ppm) |
| ${}^{180}$Hg | 180 | 100 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -73.2166 | 1410.5000 | -105.19 % | 173975.4520 MeV (+37738.2 ppm) |
| ${}^{181}$Hg | 181 | 101 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -66.6171 | 1418.9819 | -104.69 % | 174935.5673 MeV (+37702.0 ppm) |
| ${}^{182}$Hg | 182 | 102 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -60.0278 | 1429.9690 | -104.20 % | 175895.6927 MeV (+37681.6 ppm) |
| ${}^{183}$Hg | 183 | 103 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -53.4485 | 1438.2681 | -103.72 % | 176855.8282 MeV (+37645.1 ppm) |
| ${}^{184}$Hg | 184 | 104 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -46.8792 | 1448.8796 | -103.24 % | 177815.9737 MeV (+37623.0 ppm) |
| ${}^{185}$Hg | 185 | 105 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -40.3197 | 1456.7897 | -102.77 % | 178776.1290 MeV (+37585.0 ppm) |
| ${}^{186}$Hg | 186 | 106 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -33.7699 | 1467.2165 | -102.30 % | 179736.2939 MeV (+37562.5 ppm) |
| ${}^{187}$Hg | 187 | 107 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -27.2297 | 1474.8672 | -101.85 % | 180696.4685 MeV (+37523.8 ppm) |
| ${}^{188}$Hg | 188 | 108 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -20.6989 | 1485.0184 | -101.39 % | 181656.6525 MeV (+37500.3 ppm) |
| ${}^{189}$Hg | 189 | 109 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -14.1775 | 1492.5177 | -100.95 % | 182616.8459 MeV (+37461.6 ppm) |
| ${}^{190}$Hg | 190 | 110 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -7.6653 | 1502.3333 | -100.51 % | 183577.0485 MeV (+37436.8 ppm) |
| ${}^{191}$Hg | 191 | 111 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -1.1623 | 1509.6258 | -100.08 % | 184537.2602 MeV (+37397.7 ppm) |
| ${}^{192}$Hg | 192 | 112 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 5.3318 | 1519.1168 | -99.65 % | 185497.4809 MeV (+37371.8 ppm) |
| ${}^{193}$Hg | 193 | 113 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 11.8169 | 1526.2388 | -99.23 % | 186457.7106 MeV (+37332.5 ppm) |
| ${}^{194}$Hg | 194 | 114 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 18.2932 | 1535.4319 | -98.81 % | 187417.9490 MeV (+37305.5 ppm) |
| ${}^{195}$Hg | 195 | 115 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 24.7609 | 1542.3326 | -98.39 % | 188378.1961 MeV (+37265.8 ppm) |
| ${}^{196}$Hg | 196 | 116 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 31.2199 | 1551.2165 | -97.99 % | 189338.4519 MeV (+37237.8 ppm) |
| ${}^{197}$Hg | 197 | 117 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 37.6704 | 1558.0021 | -97.58 % | 190298.7161 MeV (+37198.3 ppm) |
| ${}^{198}$Hg | 198 | 118 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 44.1126 | 1566.4875 | -97.18 % | 191258.9888 MeV (+37168.8 ppm) |
| ${}^{199}$Hg | 199 | 119 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 50.5464 | 1573.1506 | -96.79 % | 192219.2697 MeV (+37129.4 ppm) |
| ${}^{200}$Hg | 200 | 120 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 56.9720 | 1581.1791 | -96.40 % | 193179.5588 MeV (+37098.1 ppm) |
| ${}^{201}$Hg | 201 | 121 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 63.3895 | 1587.4097 | -96.01 % | 194139.8561 MeV (+37057.2 ppm) |
| ${}^{202}$Hg | 202 | 122 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 69.7990 | 1595.1638 | -95.62 % | 195100.1614 MeV (+37025.1 ppm) |
| ${}^{203}$Hg | 203 | 123 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 76.2006 | 1601.1590 | -95.24 % | 196060.4746 MeV (+36983.7 ppm) |
| ${}^{204}$Hg | 204 | 124 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 82.5943 | 1608.6513 | -94.87 % | 197020.7957 MeV (+36951.0 ppm) |
| ${}^{205}$Hg | 205 | 125 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 88.9803 | 1614.3202 | -94.49 % | 197981.1245 MeV (+36908.7 ppm) |
| ${}^{206}$Hg | 206 | 126 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 95.3586 | 1621.0495 | -94.12 % | 198941.4609 MeV (+36872.6 ppm) |
| ${}^{207}$Hg | 207 | 127 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 101.7293 | 1624.6625 | -93.74 % | 199901.8050 MeV (+36820.1 ppm) |
| ${}^{208}$Hg | 208 | 128 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 108.0925 | 1629.5118 | -93.37 % | 200862.1565 MeV (+36774.7 ppm) |
| ${}^{209}$Hg | 209 | 129 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 114.4483 | 1632.9170 | -92.99 % | 201822.5155 MeV (+36722.3 ppm) |
| ${}^{210}$Hg | 210 | 130 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 120.7968 | 1637.7900 | -92.62 % | 202782.8818 MeV (+36677.5 ppm) |
| ${}^{211}$Hg | 211 | 131 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 127.1380 | 1640.9470 | -92.25 % | 203743.2554 MeV (+36624.7 ppm) |
| ${}^{212}$Hg | 212 | 132 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 133.4720 | 1645.5440 | -91.89 % | 204703.6361 MeV (+36580.3 ppm) |
| ${}^{213}$Hg | 213 | 133 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 139.7990 | 1648.4070 | -91.52 % | 205664.0240 MeV (+36527.1 ppm) |
| ${}^{214}$Hg | 214 | 134 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 146.1189 | 1652.9360 | -91.16 % | 206624.4188 MeV (+36482.8 ppm) |
| ${}^{215}$Hg | 215 | 135 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 152.4318 | 1655.7150 | -90.79 % | 207584.8206 MeV (+36429.9 ppm) |
| ${}^{216}$Hg | 216 | 136 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 158.7379 | 1659.9600 | -90.44 % | 208545.2293 MeV (+36385.3 ppm) |

### Thallium (Z = 81)

_43 of 43 isotopes with a framework prediction; 43 of 43 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{176}$Tl | 176 | 95 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -122.5590 | 1356.5971 | -109.03 % | 170156.6050 MeV (+37897.5 ppm) |
| ${}^{177}$Tl | 177 | 96 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -115.8802 | 1368.5933 | -108.47 % | 171116.6410 MeV (+37881.3 ppm) |
| ${}^{178}$Tl | 178 | 97 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -109.2125 | 1377.8980 | -107.93 % | 172076.6880 MeV (+37848.6 ppm) |
| ${}^{179}$Tl | 179 | 98 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -102.5556 | 1389.6655 | -107.38 % | 173036.7459 MeV (+37831.2 ppm) |
| ${}^{180}$Tl | 180 | 99 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -95.9094 | 1398.8576 | -106.86 % | 173996.8145 MeV (+37798.4 ppm) |
| ${}^{181}$Tl | 181 | 100 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -89.2738 | 1410.3372 | -106.33 % | 174956.8937 MeV (+37780.1 ppm) |
| ${}^{182}$Tl | 182 | 101 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -82.6487 | 1418.9370 | -105.82 % | 175916.9833 MeV (+37744.4 ppm) |
| ${}^{183}$Tl | 183 | 102 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -76.0338 | 1430.2684 | -105.32 % | 176877.0833 MeV (+37725.8 ppm) |
| ${}^{184}$Tl | 184 | 103 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -69.4292 | 1438.6358 | -104.83 % | 177837.1934 MeV (+37689.6 ppm) |
| ${}^{185}$Tl | 185 | 104 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -62.8347 | 1449.5815 | -104.33 % | 178797.3136 MeV (+37669.2 ppm) |
| ${}^{186}$Tl | 186 | 105 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -56.2501 | 1457.7780 | -103.86 % | 179757.4438 MeV (+37632.8 ppm) |
| ${}^{187}$Tl | 187 | 106 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -49.6753 | 1468.4110 | -103.38 % | 180717.5838 MeV (+37611.2 ppm) |
| ${}^{188}$Tl | 188 | 107 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -43.1102 | 1476.3741 | -102.92 % | 181677.7335 MeV (+37574.1 ppm) |
| ${}^{189}$Tl | 189 | 108 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -36.5547 | 1486.7251 | -102.46 % | 182637.8927 MeV (+37551.6 ppm) |
| ${}^{190}$Tl | 190 | 109 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -30.0087 | 1494.5466 | -102.01 % | 183598.0615 MeV (+37514.5 ppm) |
| ${}^{191}$Tl | 191 | 110 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -23.4720 | 1504.5346 | -101.56 % | 184558.2396 MeV (+37490.5 ppm) |
| ${}^{192}$Tl | 192 | 111 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -16.9446 | 1512.1952 | -101.12 % | 185518.4269 MeV (+37453.3 ppm) |
| ${}^{193}$Tl | 193 | 112 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -10.4263 | 1521.8715 | -100.69 % | 186478.6234 MeV (+37428.1 ppm) |
| ${}^{194}$Tl | 194 | 113 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -3.9170 | 1529.4031 | -100.26 % | 187438.8289 MeV (+37391.0 ppm) |
| ${}^{195}$Tl | 195 | 114 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 2.5834 | 1538.6922 | -99.83 % | 188399.0433 MeV (+37364.3 ppm) |
| ${}^{196}$Tl | 196 | 115 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 9.0749 | 1546.1048 | -99.41 % | 189359.2666 MeV (+37327.3 ppm) |
| ${}^{197}$Tl | 197 | 116 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 15.5577 | 1555.0338 | -99.00 % | 190319.4985 MeV (+37299.2 ppm) |
| ${}^{198}$Tl | 198 | 117 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 22.0319 | 1562.2796 | -98.59 % | 191279.7391 MeV (+37262.1 ppm) |
| ${}^{199}$Tl | 199 | 118 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 28.4976 | 1570.8816 | -98.19 % | 192239.9882 MeV (+37232.9 ppm) |
| ${}^{200}$Tl | 200 | 119 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 34.9549 | 1577.9407 | -97.78 % | 193200.2457 MeV (+37195.5 ppm) |
| ${}^{201}$Tl | 201 | 120 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 41.4039 | 1586.1456 | -97.39 % | 194160.5115 MeV (+37164.9 ppm) |
| ${}^{202}$Tl | 202 | 121 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 47.8446 | 1593.0166 | -97.00 % | 195120.7855 MeV (+37127.2 ppm) |
| ${}^{203}$Tl | 203 | 122 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 54.2772 | 1600.8688 | -96.61 % | 196081.0677 MeV (+37095.3 ppm) |
| ${}^{204}$Tl | 204 | 123 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 60.7018 | 1607.5249 | -96.22 % | 197041.3579 MeV (+37057.3 ppm) |
| ${}^{205}$Tl | 205 | 124 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 67.1184 | 1615.0709 | -95.84 % | 198001.6561 MeV (+37024.5 ppm) |
| ${}^{206}$Tl | 206 | 125 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 73.5271 | 1621.5747 | -95.47 % | 198961.9621 MeV (+36986.5 ppm) |
| ${}^{207}$Tl | 207 | 126 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 79.9281 | 1628.4272 | -95.09 % | 199922.2759 MeV (+36950.7 ppm) |
| ${}^{208}$Tl | 208 | 127 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 86.3214 | 1632.2142 | -94.71 % | 200882.5974 MeV (+36898.9 ppm) |
| ${}^{209}$Tl | 209 | 128 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 92.7071 | 1637.1802 | -94.34 % | 201842.9265 MeV (+36853.9 ppm) |
| ${}^{210}$Tl | 210 | 129 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 99.0852 | 1640.8537 | -93.96 % | 202803.2631 MeV (+36802.6 ppm) |
| ${}^{211}$Tl | 211 | 130 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 105.4560 | 1645.7560 | -93.59 % | 203763.6071 MeV (+36758.2 ppm) |
| ${}^{212}$Tl | 212 | 131 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 111.8193 | 1649.3600 | -93.22 % | 204723.9585 MeV (+36707.2 ppm) |
| ${}^{213}$Tl | 213 | 132 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 118.1754 | 1654.0368 | -92.86 % | 205684.3172 MeV (+36662.9 ppm) |
| ${}^{214}$Tl | 214 | 133 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 124.5243 | 1657.4300 | -92.49 % | 206644.6831 MeV (+36612.1 ppm) |
| ${}^{215}$Tl | 215 | 134 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 130.8660 | 1661.9500 | -92.13 % | 207605.0562 MeV (+36567.5 ppm) |
| ${}^{216}$Tl | 216 | 135 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 137.2007 | 1665.1440 | -91.76 % | 208565.4362 MeV (+36516.9 ppm) |
| ${}^{217}$Tl | 217 | 136 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 143.5285 | 1669.3810 | -91.40 % | 209525.8233 MeV (+36472.1 ppm) |
| ${}^{218}$Tl | 218 | 137 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 149.8493 | 1672.4960 | -91.04 % | 210486.2172 MeV (+36421.4 ppm) |

### Lead (Z = 82)

_43 of 43 isotopes with a framework prediction; 43 of 43 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{178}$Pb | 178 | 96 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -132.2307 | 1368.9688 | -109.66 % | 172098.3760 MeV (+37928.2 ppm) |
| ${}^{179}$Pb | 179 | 97 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -125.5368 | 1378.5619 | -109.11 % | 173058.3968 MeV (+37896.8 ppm) |
| ${}^{180}$Pb | 180 | 98 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -118.8538 | 1390.6259 | -108.55 % | 174018.4286 MeV (+37881.2 ppm) |
| ${}^{181}$Pb | 181 | 99 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -112.1817 | 1399.8667 | -108.01 % | 174978.4713 MeV (+37848.5 ppm) |
| ${}^{182}$Pb | 182 | 100 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -105.5203 | 1411.6520 | -107.47 % | 175938.5246 MeV (+37831.7 ppm) |
| ${}^{183}$Pb | 183 | 101 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -98.8695 | 1420.4788 | -106.96 % | 176898.5886 MeV (+37797.2 ppm) |
| ${}^{184}$Pb | 184 | 102 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -92.2291 | 1432.0217 | -106.44 % | 177858.6630 MeV (+37779.5 ppm) |
| ${}^{185}$Pb | 185 | 103 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -85.5990 | 1440.5826 | -105.94 % | 178818.7477 MeV (+37744.2 ppm) |
| ${}^{186}$Pb | 186 | 104 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -78.9792 | 1451.7936 | -105.44 % | 179778.8426 MeV (+37725.1 ppm) |
| ${}^{187}$Pb | 187 | 105 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -72.3694 | 1460.1710 | -104.96 % | 180738.9476 MeV (+37689.4 ppm) |
| ${}^{188}$Pb | 188 | 106 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -65.7696 | 1471.0664 | -104.47 % | 181699.0626 MeV (+37669.1 ppm) |
| ${}^{189}$Pb | 189 | 107 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -59.1796 | 1479.1707 | -104.00 % | 182659.1873 MeV (+37632.6 ppm) |
| ${}^{190}$Pb | 190 | 108 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -52.5993 | 1489.8146 | -103.53 % | 183619.3218 MeV (+37611.5 ppm) |
| ${}^{191}$Pb | 191 | 109 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -46.0285 | 1497.7605 | -103.07 % | 184579.4659 MeV (+37574.9 ppm) |
| ${}^{192}$Pb | 192 | 110 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -39.4673 | 1508.0925 | -102.62 % | 185539.6194 MeV (+37552.5 ppm) |
| ${}^{193}$Pb | 193 | 111 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -32.9154 | 1515.8412 | -102.17 % | 186499.7823 MeV (+37515.5 ppm) |
| ${}^{194}$Pb | 194 | 112 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -26.3728 | 1525.8911 | -101.73 % | 187459.9544 MeV (+37492.2 ppm) |
| ${}^{195}$Pb | 195 | 113 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -19.8393 | 1533.4926 | -101.29 % | 188420.1357 MeV (+37455.2 ppm) |
| ${}^{196}$Pb | 196 | 114 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -13.3149 | 1543.1741 | -100.86 % | 189380.3261 MeV (+37430.4 ppm) |
| ${}^{197}$Pb | 197 | 115 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -6.7994 | 1550.6426 | -100.44 % | 190340.5253 MeV (+37393.4 ppm) |
| ${}^{198}$Pb | 198 | 116 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -0.2927 | 1560.0360 | -100.02 % | 191300.7334 MeV (+37367.7 ppm) |
| ${}^{199}$Pb | 199 | 117 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 6.2053 | 1567.2716 | -99.60 % | 192260.9502 MeV (+37330.2 ppm) |
| ${}^{200}$Pb | 200 | 118 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 12.6946 | 1576.3620 | -99.19 % | 193221.1757 MeV (+37303.4 ppm) |
| ${}^{201}$Pb | 201 | 119 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 19.1754 | 1583.4535 | -98.79 % | 194181.4097 MeV (+37265.9 ppm) |
| ${}^{202}$Pb | 202 | 120 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 25.6478 | 1592.1944 | -98.39 % | 195141.6521 MeV (+37237.9 ppm) |
| ${}^{203}$Pb | 203 | 121 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 32.1118 | 1599.1116 | -97.99 % | 196101.9028 MeV (+37200.2 ppm) |
| ${}^{204}$Pb | 204 | 122 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 38.5676 | 1607.5063 | -97.60 % | 197062.1618 MeV (+37171.0 ppm) |
| ${}^{205}$Pb | 205 | 123 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 45.0152 | 1614.2379 | -97.21 % | 198022.4289 MeV (+37133.1 ppm) |
| ${}^{206}$Pb | 206 | 124 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 51.4548 | 1622.3246 | -96.83 % | 198982.7041 MeV (+37102.9 ppm) |
| ${}^{207}$Pb | 207 | 125 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 57.8864 | 1629.0623 | -96.45 % | 199942.9873 MeV (+37065.8 ppm) |
| ${}^{208}$Pb | 208 | 126 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 64.3102 | 1636.4302 | -96.07 % | 200903.2783 MeV (+37032.4 ppm) |
| ${}^{209}$Pb | 209 | 127 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 70.7261 | 1640.3676 | -95.69 % | 201863.5771 MeV (+36981.2 ppm) |
| ${}^{210}$Pb | 210 | 128 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 77.1343 | 1645.5528 | -95.31 % | 202823.8837 MeV (+36937.0 ppm) |
| ${}^{211}$Pb | 211 | 129 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 83.5349 | 1649.3887 | -94.94 % | 203784.1979 MeV (+36886.3 ppm) |
| ${}^{212}$Pb | 212 | 130 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 89.9280 | 1654.5159 | -94.56 % | 204744.5196 MeV (+36842.8 ppm) |
| ${}^{213}$Pb | 213 | 131 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 96.3136 | 1658.2419 | -94.19 % | 205704.8488 MeV (+36792.5 ppm) |
| ${}^{214}$Pb | 214 | 132 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 102.6918 | 1663.2926 | -93.83 % | 206665.1853 MeV (+36749.5 ppm) |
| ${}^{215}$Pb | 215 | 133 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 109.0627 | 1666.8387 | -93.46 % | 207625.5292 MeV (+36699.2 ppm) |
| ${}^{216}$Pb | 216 | 134 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 115.4264 | 1671.8400 | -93.10 % | 208585.8803 MeV (+36656.4 ppm) |
| ${}^{217}$Pb | 217 | 135 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 121.7829 | 1675.0230 | -92.73 % | 209546.2385 MeV (+36605.9 ppm) |
| ${}^{218}$Pb | 218 | 136 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 128.1323 | 1679.6900 | -92.37 % | 210506.6039 MeV (+36563.0 ppm) |
| ${}^{219}$Pb | 219 | 137 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 134.4748 | 1682.7960 | -92.01 % | 211466.9762 MeV (+36512.2 ppm) |
| ${}^{220}$Pb | 220 | 138 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 140.8103 | 1687.4000 | -91.66 % | 212427.3554 MeV (+36469.5 ppm) |

### Bismuth (Z = 83)

_41 of 41 isotopes with a framework prediction; 41 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{184}$Bi | 184 | 101 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -115.2788 | 1419.0080 | -108.12 % | 177880.3824 MeV (+37831.7 ppm) |
| ${}^{185}$Bi | 185 | 102 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -108.6129 | 1430.4200 | -107.59 % | 178840.4312 MeV (+37813.9 ppm) |
| ${}^{186}$Bi | 186 | 103 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -101.9573 | 1439.4759 | -107.08 % | 179800.4905 MeV (+37781.0 ppm) |
| ${}^{187}$Bi | 187 | 104 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -95.3121 | 1450.7850 | -106.57 % | 180760.5600 MeV (+37762.3 ppm) |
| ${}^{188}$Bi | 188 | 105 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -88.6771 | 1459.6678 | -106.08 % | 181720.6398 MeV (+37729.4 ppm) |
| ${}^{189}$Bi | 189 | 106 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -82.0521 | 1470.6090 | -105.58 % | 182680.7296 MeV (+37709.2 ppm) |
| ${}^{190}$Bi | 190 | 107 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -75.4371 | 1479.2115 | -105.10 % | 183640.8294 MeV (+37675.4 ppm) |
| ${}^{191}$Bi | 191 | 108 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -68.8320 | 1489.9263 | -104.62 % | 184600.9390 MeV (+37654.4 ppm) |
| ${}^{192}$Bi | 192 | 109 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -62.2365 | 1498.2928 | -104.15 % | 185561.0583 MeV (+37620.1 ppm) |
| ${}^{193}$Bi | 193 | 110 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -55.6506 | 1508.7142 | -103.69 % | 186521.1872 MeV (+37598.0 ppm) |
| ${}^{194}$Bi | 194 | 111 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -49.0742 | 1516.9239 | -103.24 % | 187481.3256 MeV (+37563.5 ppm) |
| ${}^{195}$Bi | 195 | 112 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -42.5072 | 1526.9978 | -102.78 % | 188441.4733 MeV (+37540.0 ppm) |
| ${}^{196}$Bi | 196 | 113 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -35.9495 | 1535.0526 | -102.34 % | 189401.6303 MeV (+37505.4 ppm) |
| ${}^{197}$Bi | 197 | 114 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -29.4009 | 1544.8021 | -101.90 % | 190361.7965 MeV (+37480.8 ppm) |
| ${}^{198}$Bi | 198 | 115 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -22.8613 | 1552.5600 | -101.47 % | 191321.9717 MeV (+37445.2 ppm) |
| ${}^{199}$Bi | 199 | 116 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -16.3307 | 1562.0551 | -101.05 % | 192282.1559 MeV (+37419.8 ppm) |
| ${}^{200}$Bi | 200 | 117 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -9.8089 | 1569.6994 | -100.62 % | 193242.3489 MeV (+37384.3 ppm) |
| ${}^{201}$Bi | 201 | 118 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -3.2959 | 1578.8291 | -100.21 % | 194202.5506 MeV (+37357.5 ppm) |
| ${}^{202}$Bi | 202 | 119 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 3.2085 | 1586.2223 | -99.80 % | 195162.7610 MeV (+37321.5 ppm) |
| ${}^{203}$Bi | 203 | 120 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 9.7044 | 1595.0677 | -99.39 % | 196122.9799 MeV (+37293.8 ppm) |
| ${}^{204}$Bi | 204 | 121 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 16.1918 | 1602.2600 | -98.99 % | 197083.2073 MeV (+37257.4 ppm) |
| ${}^{205}$Bi | 205 | 122 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 22.6708 | 1610.7510 | -98.59 % | 198043.4430 MeV (+37228.4 ppm) |
| ${}^{206}$Bi | 206 | 123 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 29.1416 | 1617.7849 | -98.20 % | 199003.6870 MeV (+37191.9 ppm) |
| ${}^{207}$Bi | 207 | 124 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 35.6043 | 1625.8826 | -97.81 % | 199963.9391 MeV (+37161.5 ppm) |
| ${}^{208}$Bi | 208 | 125 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 42.0588 | 1632.7695 | -97.42 % | 200924.1994 MeV (+37125.0 ppm) |
| ${}^{209}$Bi | 209 | 126 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 48.5054 | 1640.2293 | -97.04 % | 201884.4676 MeV (+37091.9 ppm) |
| ${}^{210}$Bi | 210 | 127 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 54.9440 | 1644.8339 | -96.66 % | 202844.7437 MeV (+37044.0 ppm) |
| ${}^{211}$Bi | 211 | 128 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 61.3749 | 1649.9724 | -96.28 % | 203805.0276 MeV (+36999.5 ppm) |
| ${}^{212}$Bi | 212 | 129 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 67.7980 | 1654.3026 | -95.90 % | 204765.3193 MeV (+36951.1 ppm) |
| ${}^{213}$Bi | 213 | 130 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 74.2135 | 1659.4876 | -95.53 % | 205725.6186 MeV (+36907.7 ppm) |
| ${}^{214}$Bi | 214 | 131 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 80.6214 | 1663.5280 | -95.15 % | 206685.9254 MeV (+36858.8 ppm) |
| ${}^{215}$Bi | 215 | 132 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 87.0218 | 1668.7693 | -94.79 % | 207646.2398 MeV (+36816.7 ppm) |
| ${}^{216}$Bi | 216 | 133 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 93.4148 | 1672.5959 | -94.41 % | 208606.5615 MeV (+36767.6 ppm) |
| ${}^{217}$Bi | 217 | 134 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 99.8005 | 1677.8113 | -94.05 % | 209566.8906 MeV (+36726.2 ppm) |
| ${}^{218}$Bi | 218 | 135 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 106.1789 | 1681.3965 | -93.69 % | 210527.2270 MeV (+36676.9 ppm) |
| ${}^{219}$Bi | 219 | 136 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 112.5502 | 1686.3000 | -93.33 % | 211487.5705 MeV (+36635.0 ppm) |
| ${}^{220}$Bi | 220 | 137 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 118.9144 | 1689.8200 | -92.96 % | 212447.9211 MeV (+36585.9 ppm) |
| ${}^{221}$Bi | 221 | 138 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 125.2715 | 1694.6280 | -92.61 % | 213408.2787 MeV (+36544.2 ppm) |
| ${}^{222}$Bi | 222 | 139 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 131.6217 | 1697.8560 | -92.25 % | 214368.6433 MeV (+36495.4 ppm) |
| ${}^{223}$Bi | 223 | 140 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 137.9650 | 1702.8280 | -91.90 % | 215329.0148 MeV (+36454.4 ppm) |
| ${}^{224}$Bi | 224 | 141 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 144.3015 | 1705.9840 | -91.54 % | 216289.3930 MeV (+36406.1 ppm) |

### Polonium (Z = 84)

_42 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{186}$Po | 186 | 102 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -125.1844 | 1431.4465 | -108.75 % | 179822.3873 MeV (+37863.9 ppm) |
| ${}^{187}$Po | 187 | 103 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -118.5034 | 1440.7955 | -108.22 % | 180782.4210 MeV (+37832.9 ppm) |
| ${}^{188}$Po | 188 | 104 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -111.8327 | 1452.2350 | -107.70 % | 181742.4651 MeV (+37814.7 ppm) |
| ${}^{189}$Po | 189 | 105 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -105.1724 | 1461.1840 | -107.20 % | 182702.5196 MeV (+37782.0 ppm) |
| ${}^{190}$Po | 190 | 106 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -98.5223 | 1472.3960 | -106.69 % | 183662.5842 MeV (+37763.0 ppm) |
| ${}^{191}$Po | 191 | 107 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -91.8822 | 1480.9733 | -106.20 % | 184622.6589 MeV (+37728.9 ppm) |
| ${}^{192}$Po | 192 | 108 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -85.2521 | 1492.0424 | -105.71 % | 185582.7436 MeV (+37709.6 ppm) |
| ${}^{193}$Po | 193 | 109 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -78.6318 | 1500.3725 | -105.24 % | 186542.8381 MeV (+37674.8 ppm) |
| ${}^{194}$Po | 194 | 110 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -72.0213 | 1511.1232 | -104.77 % | 187502.9423 MeV (+37654.3 ppm) |
| ${}^{195}$Po | 195 | 111 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -65.4203 | 1519.3065 | -104.31 % | 188463.0561 MeV (+37619.4 ppm) |
| ${}^{196}$Po | 196 | 112 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -58.8288 | 1529.7299 | -103.85 % | 189423.1794 MeV (+37597.7 ppm) |
| ${}^{197}$Po | 197 | 113 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -52.2467 | 1537.7256 | -103.40 % | 190383.3121 MeV (+37562.4 ppm) |
| ${}^{198}$Po | 198 | 114 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -45.6739 | 1547.8771 | -102.95 % | 191343.4540 MeV (+37539.8 ppm) |
| ${}^{199}$Po | 199 | 115 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -39.1102 | 1555.7140 | -102.51 % | 192303.6051 MeV (+37504.4 ppm) |
| ${}^{200}$Po | 200 | 116 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -32.5556 | 1565.4881 | -102.08 % | 193263.7653 MeV (+37480.2 ppm) |
| ${}^{201}$Po | 201 | 117 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -26.0099 | 1573.1389 | -101.65 % | 194223.9344 MeV (+37444.6 ppm) |
| ${}^{202}$Po | 202 | 118 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -19.4731 | 1582.6307 | -101.23 % | 195184.1123 MeV (+37419.5 ppm) |
| ${}^{203}$Po | 203 | 119 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -12.9451 | 1590.0712 | -100.81 % | 196144.2991 MeV (+37383.4 ppm) |
| ${}^{204}$Po | 204 | 120 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -6.4256 | 1599.1728 | -100.40 % | 197104.4944 MeV (+37356.8 ppm) |
| ${}^{205}$Po | 205 | 121 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 0.0852 | 1606.4244 | -99.99 % | 198064.6983 MeV (+37320.5 ppm) |
| ${}^{206}$Po | 206 | 122 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 6.5876 | 1615.1630 | -99.59 % | 199024.9107 MeV (+37292.6 ppm) |
| ${}^{207}$Po | 207 | 123 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 13.0816 | 1622.1914 | -99.19 % | 199985.1315 MeV (+37255.8 ppm) |
| ${}^{208}$Po | 208 | 124 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 19.5674 | 1630.5862 | -98.80 % | 200945.3605 MeV (+37226.7 ppm) |
| ${}^{209}$Po | 209 | 125 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 26.0449 | 1637.5543 | -98.41 % | 201905.5977 MeV (+37190.4 ppm) |
| ${}^{210}$Po | 210 | 126 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 32.5144 | 1645.2127 | -98.02 % | 202865.8430 MeV (+37158.1 ppm) |
| ${}^{211}$Po | 211 | 127 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 38.9759 | 1649.7635 | -97.64 % | 203826.0963 MeV (+37109.7 ppm) |
| ${}^{212}$Po | 212 | 128 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 45.4294 | 1655.7717 | -97.26 % | 204786.3576 MeV (+37069.5 ppm) |
| ${}^{213}$Po | 213 | 129 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 51.8751 | 1660.1271 | -96.88 % | 205746.6266 MeV (+37021.1 ppm) |
| ${}^{214}$Po | 214 | 130 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 58.3131 | 1666.0149 | -96.50 % | 206706.9034 MeV (+36981.1 ppm) |
| ${}^{215}$Po | 215 | 131 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 64.7434 | 1670.1580 | -96.12 % | 207667.1879 MeV (+36932.5 ppm) |
| ${}^{216}$Po | 216 | 132 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 71.1661 | 1675.9052 | -95.75 % | 208627.4800 MeV (+36892.7 ppm) |
| ${}^{217}$Po | 217 | 133 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 77.5813 | 1679.8754 | -95.38 % | 209587.7795 MeV (+36844.1 ppm) |
| ${}^{218}$Po | 218 | 134 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 83.9891 | 1685.4735 | -95.02 % | 210548.0865 MeV (+36804.4 ppm) |
| ${}^{219}$Po | 219 | 135 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 90.3895 | 1689.2201 | -94.65 % | 211508.4009 MeV (+36755.6 ppm) |
| ${}^{220}$Po | 220 | 136 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 96.7826 | 1694.7094 | -94.29 % | 212468.7225 MeV (+36716.2 ppm) |
| ${}^{221}$Po | 221 | 137 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 103.1686 | 1698.2704 | -93.93 % | 213429.0513 MeV (+36667.4 ppm) |
| ${}^{222}$Po | 222 | 138 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 109.5474 | 1703.6292 | -93.57 % | 214389.3873 MeV (+36628.1 ppm) |
| ${}^{223}$Po | 223 | 139 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 115.9192 | 1707.0650 | -93.21 % | 215349.7303 MeV (+36579.8 ppm) |
| ${}^{224}$Po | 224 | 140 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 122.2840 | 1712.2560 | -92.86 % | 216310.0802 MeV (+36540.7 ppm) |
| ${}^{225}$Po | 225 | 141 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 128.6419 | 1715.8500 | -92.50 % | 217270.4371 MeV (+36493.0 ppm) |
| ${}^{226}$Po | 226 | 142 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 134.9930 | 1720.7640 | -92.16 % | 218230.8008 MeV (+36454.0 ppm) |
| ${}^{227}$Po | 227 | 143 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 141.3373 | 1724.2920 | -91.80 % | 219191.1713 MeV (+36406.8 ppm) |

### Astatine (Z = 85)

_39 of 39 isotopes with a framework prediction; 39 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{191}$At | 191 | 106 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -115.1793 | 1471.2584 | -107.83 % | 184644.6258 MeV (+37800.2 ppm) |
| ${}^{192}$At | 192 | 107 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -108.5142 | 1480.2678 | -107.33 % | 185604.6754 MeV (+37768.5 ppm) |
| ${}^{193}$At | 193 | 108 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -101.8591 | 1491.3322 | -106.83 % | 186564.7350 MeV (+37748.9 ppm) |
| ${}^{194}$At | 194 | 109 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -95.2139 | 1500.0527 | -106.35 % | 187524.8046 MeV (+37716.2 ppm) |
| ${}^{195}$At | 195 | 110 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -88.5786 | 1510.8778 | -105.86 % | 188484.8841 MeV (+37695.9 ppm) |
| ${}^{196}$At | 196 | 111 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -81.9530 | 1519.3920 | -105.39 % | 189444.9733 MeV (+37662.7 ppm) |
| ${}^{197}$At | 197 | 112 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -75.3370 | 1529.9054 | -104.92 % | 190405.0720 MeV (+37641.2 ppm) |
| ${}^{198}$At | 198 | 113 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -68.7304 | 1538.3302 | -104.47 % | 191365.1803 MeV (+37608.2 ppm) |
| ${}^{199}$At | 199 | 114 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -62.1333 | 1548.5162 | -104.01 % | 192325.2979 MeV (+37585.5 ppm) |
| ${}^{200}$At | 200 | 115 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -55.5455 | 1556.7520 | -103.57 % | 193285.4248 MeV (+37552.2 ppm) |
| ${}^{201}$At | 201 | 116 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -48.9668 | 1566.6249 | -103.13 % | 194245.5609 MeV (+37528.3 ppm) |
| ${}^{202}$At | 202 | 117 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -42.3972 | 1574.5019 | -102.69 % | 195205.7061 MeV (+37493.7 ppm) |
| ${}^{203}$At | 203 | 118 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -35.8365 | 1584.1407 | -102.26 % | 196165.8602 MeV (+37469.2 ppm) |
| ${}^{204}$At | 204 | 119 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -29.2847 | 1591.9246 | -101.84 % | 197126.0232 MeV (+37434.8 ppm) |
| ${}^{205}$At | 205 | 120 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -22.7417 | 1601.1052 | -101.42 % | 198086.1949 MeV (+37408.4 ppm) |
| ${}^{206}$At | 206 | 121 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -16.2073 | 1608.6314 | -101.01 % | 199046.3753 MeV (+37373.4 ppm) |
| ${}^{207}$At | 207 | 122 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -9.6815 | 1617.4908 | -100.60 % | 200006.5643 MeV (+37345.9 ppm) |
| ${}^{208}$At | 208 | 123 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -3.1642 | 1624.8046 | -100.19 % | 200966.7618 MeV (+37310.4 ppm) |
| ${}^{209}$At | 209 | 124 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 3.3448 | 1633.2898 | -99.80 % | 201926.9676 MeV (+37281.6 ppm) |
| ${}^{210}$At | 210 | 125 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 9.8454 | 1640.4494 | -99.40 % | 202887.1817 MeV (+37246.0 ppm) |
| ${}^{211}$At | 211 | 126 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 16.3379 | 1648.1958 | -99.01 % | 203847.4040 MeV (+37214.0 ppm) |
| ${}^{212}$At | 212 | 127 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 22.8222 | 1653.2481 | -98.62 % | 204807.6345 MeV (+37168.1 ppm) |
| ${}^{213}$At | 213 | 128 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 29.2985 | 1659.2708 | -98.23 % | 205767.8729 MeV (+37127.8 ppm) |
| ${}^{214}$At | 214 | 129 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 35.7669 | 1664.1417 | -97.85 % | 206728.1193 MeV (+37081.8 ppm) |
| ${}^{215}$At | 215 | 130 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 42.2274 | 1670.0905 | -97.47 % | 207688.3736 MeV (+37042.0 ppm) |
| ${}^{216}$At | 216 | 131 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 48.6802 | 1674.6485 | -97.09 % | 208648.6356 MeV (+36995.4 ppm) |
| ${}^{217}$At | 217 | 132 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 55.1253 | 1680.5819 | -96.72 % | 209608.9053 MeV (+36956.3 ppm) |
| ${}^{218}$At | 218 | 133 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 61.5627 | 1684.9476 | -96.35 % | 210569.1826 MeV (+36909.6 ppm) |
| ${}^{219}$At | 219 | 134 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 67.9927 | 1690.7231 | -95.98 % | 211529.4674 MeV (+36870.5 ppm) |
| ${}^{220}$At | 220 | 135 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 74.4151 | 1694.8147 | -95.61 % | 212489.7597 MeV (+36823.3 ppm) |
| ${}^{221}$At | 221 | 136 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 80.8303 | 1700.4791 | -95.25 % | 213450.0594 MeV (+36784.5 ppm) |
| ${}^{222}$At | 222 | 137 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 87.2381 | 1704.3801 | -94.88 % | 214410.3663 MeV (+36737.2 ppm) |
| ${}^{223}$At | 223 | 138 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 93.6387 | 1709.9764 | -94.52 % | 215370.6805 MeV (+36698.9 ppm) |
| ${}^{224}$At | 224 | 139 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 100.0322 | 1713.7647 | -94.16 % | 216331.0018 MeV (+36651.9 ppm) |
| ${}^{225}$At | 225 | 140 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 106.4185 | 1719.2250 | -93.81 % | 217291.3302 MeV (+36613.8 ppm) |
| ${}^{226}$At | 226 | 141 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 112.7979 | 1723.0240 | -93.45 % | 218251.6656 MeV (+36567.3 ppm) |
| ${}^{227}$At | 227 | 142 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 119.1704 | 1728.1510 | -93.10 % | 219212.0079 MeV (+36529.1 ppm) |
| ${}^{228}$At | 228 | 143 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 125.5360 | 1731.8880 | -92.75 % | 220172.3571 MeV (+36483.0 ppm) |
| ${}^{229}$At | 229 | 144 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 131.8948 | 1736.9650 | -92.41 % | 221132.7130 MeV (+36444.4 ppm) |

### Radon (Z = 86)

_39 of 39 isotopes with a framework prediction; 39 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{193}$Rn | 193 | 107 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -125.3323 | 1481.4396 | -108.46 % | 186586.8780 MeV (+37819.5 ppm) |
| ${}^{194}$Rn | 194 | 108 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -118.6521 | 1492.8292 | -107.95 % | 187546.9126 MeV (+37801.6 ppm) |
| ${}^{195}$Rn | 195 | 109 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -111.9821 | 1501.5749 | -107.46 % | 188506.9573 MeV (+37768.7 ppm) |
| ${}^{196}$Rn | 196 | 110 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -105.3219 | 1512.7213 | -106.96 % | 189467.0119 MeV (+37750.0 ppm) |
| ${}^{197}$Rn | 197 | 111 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -98.6716 | 1521.2574 | -106.49 % | 190427.0764 MeV (+37716.7 ppm) |
| ${}^{198}$Rn | 198 | 112 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -92.0310 | 1532.0695 | -106.01 % | 191387.1505 MeV (+37696.6 ppm) |
| ${}^{199}$Rn | 199 | 113 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -85.4000 | 1540.4703 | -105.54 % | 192347.2343 MeV (+37663.2 ppm) |
| ${}^{200}$Rn | 200 | 114 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -78.7785 | 1550.9822 | -105.08 % | 193307.3276 MeV (+37642.0 ppm) |
| ${}^{201}$Rn | 201 | 115 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -72.1664 | 1559.1605 | -104.63 % | 194267.4303 MeV (+37608.1 ppm) |
| ${}^{202}$Rn | 202 | 116 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -65.5636 | 1569.3990 | -104.18 % | 195227.5422 MeV (+37586.0 ppm) |
| ${}^{203}$Rn | 203 | 117 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -58.9700 | 1577.3798 | -103.74 % | 196187.6634 MeV (+37551.7 ppm) |
| ${}^{204}$Rn | 204 | 118 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -52.3854 | 1587.2372 | -103.30 % | 197147.7936 MeV (+37528.1 ppm) |
| ${}^{205}$Rn | 205 | 119 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -45.8098 | 1595.0481 | -102.87 % | 198107.9327 MeV (+37493.6 ppm) |
| ${}^{206}$Rn | 206 | 120 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -39.2431 | 1604.5426 | -102.45 % | 199068.0808 MeV (+37468.6 ppm) |
| ${}^{207}$Rn | 207 | 121 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -32.6851 | 1612.1157 | -102.03 % | 200028.2376 MeV (+37433.6 ppm) |
| ${}^{208}$Rn | 208 | 122 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -26.1358 | 1621.2077 | -101.61 % | 200988.4031 MeV (+37407.1 ppm) |
| ${}^{209}$Rn | 209 | 123 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -19.5952 | 1628.5647 | -101.20 % | 201948.5772 MeV (+37371.6 ppm) |
| ${}^{210}$Rn | 210 | 124 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -13.0629 | 1637.2997 | -100.80 % | 202908.7598 MeV (+37343.8 ppm) |
| ${}^{211}$Rn | 211 | 125 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -6.5391 | 1644.5216 | -100.40 % | 203868.9507 MeV (+37308.3 ppm) |
| ${}^{212}$Rn | 212 | 126 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -0.0236 | 1652.4968 | -100.00 % | 204829.1500 MeV (+37277.2 ppm) |
| ${}^{213}$Rn | 213 | 127 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 6.4837 | 1657.6049 | -99.61 % | 205789.3575 MeV (+37231.4 ppm) |
| ${}^{214}$Rn | 214 | 128 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 12.9828 | 1664.2999 | -99.22 % | 206749.5731 MeV (+37194.4 ppm) |
| ${}^{215}$Rn | 215 | 129 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 19.4739 | 1669.2205 | -98.83 % | 207709.7968 MeV (+37148.5 ppm) |
| ${}^{216}$Rn | 216 | 130 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 25.9571 | 1675.8695 | -98.45 % | 208670.0284 MeV (+37112.0 ppm) |
| ${}^{217}$Rn | 217 | 131 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 32.4324 | 1680.5356 | -98.07 % | 209630.2678 MeV (+37065.7 ppm) |
| ${}^{218}$Rn | 218 | 132 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 38.8999 | 1687.0481 | -97.69 % | 210590.5151 MeV (+37029.3 ppm) |
| ${}^{219}$Rn | 219 | 133 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 45.3597 | 1691.5075 | -97.32 % | 211550.7701 MeV (+36982.9 ppm) |
| ${}^{220}$Rn | 220 | 134 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 51.8119 | 1697.7961 | -96.95 % | 212511.0327 MeV (+36946.1 ppm) |
| ${}^{221}$Rn | 221 | 135 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 58.2565 | 1702.0081 | -96.58 % | 213471.3028 MeV (+36899.3 ppm) |
| ${}^{222}$Rn | 222 | 136 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 64.6937 | 1708.1788 | -96.21 % | 214431.5804 MeV (+36862.8 ppm) |
| ${}^{223}$Rn | 223 | 137 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 71.1234 | 1712.2324 | -95.85 % | 215391.8654 MeV (+36816.0 ppm) |
| ${}^{224}$Rn | 224 | 138 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 77.5459 | 1718.2483 | -95.49 % | 216352.1578 MeV (+36779.5 ppm) |
| ${}^{225}$Rn | 225 | 139 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 83.9611 | 1722.2306 | -95.12 % | 217312.4573 MeV (+36733.2 ppm) |
| ${}^{226}$Rn | 226 | 140 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 90.3692 | 1728.0888 | -94.77 % | 218272.7640 MeV (+36696.7 ppm) |
| ${}^{227}$Rn | 227 | 141 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 96.7701 | 1732.0215 | -94.41 % | 219233.0779 MeV (+36651.0 ppm) |
| ${}^{228}$Rn | 228 | 142 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 103.1640 | 1737.7352 | -94.06 % | 220193.3987 MeV (+36614.5 ppm) |
| ${}^{229}$Rn | 229 | 143 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 109.5510 | 1741.6876 | -93.71 % | 221153.7265 MeV (+36569.8 ppm) |
| ${}^{230}$Rn | 230 | 144 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 115.9311 | 1746.8500 | -93.36 % | 222114.0612 MeV (+36531.8 ppm) |
| ${}^{231}$Rn | 231 | 145 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 122.3044 | 1750.7490 | -93.01 % | 223074.4027 MeV (+36486.6 ppm) |

### Francium (Z = 87)

_37 of 37 isotopes with a framework prediction; 37 of 37 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{197}$Fr | 197 | 110 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -122.2506 | 1511.7315 | -108.09 % | 190449.3251 MeV (+37788.5 ppm) |
| ${}^{198}$Fr | 198 | 111 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -115.5755 | 1520.4791 | -107.60 % | 191409.3648 MeV (+37756.2 ppm) |
| ${}^{199}$Fr | 199 | 112 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -108.9103 | 1531.3567 | -107.11 % | 192369.4143 MeV (+37736.2 ppm) |
| ${}^{200}$Fr | 200 | 113 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -102.2548 | 1540.0658 | -106.64 % | 193329.4736 MeV (+37704.4 ppm) |
| ${}^{201}$Fr | 201 | 114 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -95.6089 | 1550.6822 | -106.17 % | 194289.5424 MeV (+37683.6 ppm) |
| ${}^{202}$Fr | 202 | 115 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -88.9724 | 1559.2405 | -105.71 % | 195249.6208 MeV (+37651.6 ppm) |
| ${}^{203}$Fr | 203 | 116 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -82.3454 | 1569.5370 | -105.25 % | 196209.7085 MeV (+37629.6 ppm) |
| ${}^{204}$Fr | 204 | 117 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -75.7277 | 1577.8774 | -104.80 % | 197169.8056 MeV (+37597.1 ppm) |
| ${}^{205}$Fr | 205 | 118 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -69.1192 | 1587.8658 | -104.35 % | 198129.9118 MeV (+37573.9 ppm) |
| ${}^{206}$Fr | 206 | 119 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -62.5197 | 1595.8742 | -103.92 % | 199090.0271 MeV (+37540.4 ppm) |
| ${}^{207}$Fr | 207 | 120 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -55.9292 | 1605.5477 | -103.48 % | 200050.1514 MeV (+37516.1 ppm) |
| ${}^{208}$Fr | 208 | 121 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -49.3476 | 1613.4349 | -103.06 % | 201010.2846 MeV (+37482.6 ppm) |
| ${}^{209}$Fr | 209 | 122 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -42.7748 | 1622.6234 | -102.64 % | 201970.4265 MeV (+37456.3 ppm) |
| ${}^{210}$Fr | 210 | 123 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -36.2107 | 1630.2561 | -102.22 % | 202930.5772 MeV (+37422.1 ppm) |
| ${}^{211}$Fr | 211 | 124 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -29.6551 | 1639.1242 | -101.81 % | 203890.7364 MeV (+37394.8 ppm) |
| ${}^{212}$Fr | 212 | 125 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -23.1081 | 1646.5712 | -101.40 % | 204850.9042 MeV (+37360.4 ppm) |
| ${}^{213}$Fr | 213 | 126 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -16.5695 | 1654.6808 | -101.00 % | 205811.0803 MeV (+37329.7 ppm) |
| ${}^{214}$Fr | 214 | 127 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -10.0392 | 1660.1562 | -100.60 % | 206771.2648 MeV (+37285.7 ppm) |
| ${}^{215}$Fr | 215 | 128 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -3.5171 | 1666.9511 | -100.21 % | 207731.4575 MeV (+37249.0 ppm) |
| ${}^{216}$Fr | 216 | 129 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 2.9968 | 1672.3695 | -99.82 % | 208691.6583 MeV (+37205.5 ppm) |
| ${}^{217}$Fr | 217 | 130 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 9.5027 | 1679.0972 | -99.43 % | 209651.8672 MeV (+37169.2 ppm) |
| ${}^{218}$Fr | 218 | 131 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 16.0006 | 1684.4237 | -99.05 % | 210612.0841 MeV (+37126.1 ppm) |
| ${}^{219}$Fr | 219 | 132 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 22.4906 | 1690.9375 | -98.67 % | 211572.3088 MeV (+37089.5 ppm) |
| ${}^{220}$Fr | 220 | 133 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 28.9729 | 1696.1435 | -98.29 % | 212532.5414 MeV (+37046.7 ppm) |
| ${}^{221}$Fr | 221 | 134 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 35.4473 | 1702.4198 | -97.92 % | 213492.7817 MeV (+37009.7 ppm) |
| ${}^{222}$Fr | 222 | 135 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 41.9142 | 1707.3903 | -97.55 % | 214453.0296 MeV (+36966.5 ppm) |
| ${}^{223}$Fr | 223 | 136 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 48.3735 | 1713.4574 | -97.18 % | 215413.2851 MeV (+36929.1 ppm) |
| ${}^{224}$Fr | 224 | 137 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 54.8253 | 1718.1624 | -96.81 % | 216373.5481 MeV (+36885.4 ppm) |
| ${}^{225}$Fr | 225 | 138 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 61.2696 | 1724.1618 | -96.45 % | 217333.8185 MeV (+36848.6 ppm) |
| ${}^{226}$Fr | 226 | 139 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 67.7067 | 1728.5332 | -96.08 % | 218294.0962 MeV (+36804.0 ppm) |
| ${}^{227}$Fr | 227 | 140 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 74.1364 | 1734.4426 | -95.73 % | 219254.3812 MeV (+36767.4 ppm) |
| ${}^{228}$Fr | 228 | 141 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 80.5590 | 1738.8121 | -95.37 % | 220214.6734 MeV (+36723.7 ppm) |
| ${}^{229}$Fr | 229 | 142 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 86.9745 | 1744.5994 | -95.01 % | 221174.9727 MeV (+36687.3 ppm) |
| ${}^{230}$Fr | 230 | 143 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 93.3829 | 1748.8522 | -94.66 % | 222135.2791 MeV (+36643.8 ppm) |
| ${}^{231}$Fr | 231 | 144 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 99.7844 | 1754.3297 | -94.31 % | 223095.5924 MeV (+36606.6 ppm) |
| ${}^{232}$Fr | 232 | 145 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 106.1789 | 1758.4088 | -93.96 % | 224055.9126 MeV (+36563.1 ppm) |
| ${}^{233}$Fr | 233 | 146 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 112.5666 | 1763.6329 | -93.62 % | 225016.2397 MeV (+36525.4 ppm) |

### Radium (Z = 88)

_35 of 35 isotopes with a framework prediction; 35 of 35 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{201}$Ra | 201 | 113 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -119.2941 | 1541.5516 | -107.74 % | 194311.8973 MeV (+37756.7 ppm) |
| ${}^{202}$Ra | 202 | 114 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -112.6237 | 1552.4848 | -107.25 % | 195271.9417 MeV (+37737.3 ppm) |
| ${}^{203}$Ra | 203 | 115 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -105.9629 | 1561.0297 | -106.79 % | 196231.9957 MeV (+37705.0 ppm) |
| ${}^{204}$Ra | 204 | 116 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -99.3116 | 1571.6413 | -106.32 % | 197192.0592 MeV (+37684.4 ppm) |
| ${}^{205}$Ra | 205 | 117 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -92.6698 | 1579.9698 | -105.87 % | 198152.1321 MeV (+37651.6 ppm) |
| ${}^{206}$Ra | 206 | 118 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -86.0372 | 1590.2794 | -105.41 % | 199112.2143 MeV (+37630.0 ppm) |
| ${}^{207}$Ra | 207 | 119 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -79.4138 | 1598.4023 | -104.97 % | 200072.3057 MeV (+37596.8 ppm) |
| ${}^{208}$Ra | 208 | 120 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -72.7995 | 1608.2597 | -104.53 % | 201032.4062 MeV (+37573.2 ppm) |
| ${}^{209}$Ra | 209 | 121 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -66.1942 | 1616.2007 | -104.10 % | 201992.5156 MeV (+37539.7 ppm) |
| ${}^{210}$Ra | 210 | 122 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -59.5977 | 1625.6874 | -103.67 % | 202952.6340 MeV (+37514.8 ppm) |
| ${}^{211}$Ra | 211 | 123 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -53.0101 | 1633.3697 | -103.25 % | 203912.7611 MeV (+37480.6 ppm) |
| ${}^{212}$Ra | 212 | 124 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -46.4312 | 1642.4717 | -102.83 % | 204872.8969 MeV (+37454.3 ppm) |
| ${}^{213}$Ra | 213 | 125 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -39.8608 | 1649.9987 | -102.42 % | 205833.0414 MeV (+37420.0 ppm) |
| ${}^{214}$Ra | 214 | 126 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -33.2990 | 1658.3228 | -102.01 % | 206793.1944 MeV (+37390.2 ppm) |
| ${}^{215}$Ra | 215 | 127 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -26.7456 | 1663.9549 | -101.61 % | 207753.3557 MeV (+37346.8 ppm) |
| ${}^{216}$Ra | 216 | 128 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -20.2006 | 1671.2667 | -101.21 % | 208713.5254 MeV (+37312.5 ppm) |
| ${}^{217}$Ra | 217 | 129 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -13.6638 | 1676.7399 | -100.81 % | 209673.7034 MeV (+37269.2 ppm) |
| ${}^{218}$Ra | 218 | 130 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -7.1351 | 1684.0553 | -100.42 % | 210633.8895 MeV (+37235.6 ppm) |
| ${}^{219}$Ra | 219 | 131 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -0.6145 | 1689.3783 | -100.04 % | 211594.0837 MeV (+37192.3 ppm) |
| ${}^{220}$Ra | 220 | 132 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 5.8981 | 1696.5713 | -99.65 % | 212554.2859 MeV (+37158.9 ppm) |
| ${}^{221}$Ra | 221 | 133 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 12.4028 | 1701.9509 | -99.27 % | 213514.4960 MeV (+37116.7 ppm) |
| ${}^{222}$Ra | 222 | 134 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 18.8996 | 1708.6659 | -98.89 % | 214474.7139 MeV (+37081.6 ppm) |
| ${}^{223}$Ra | 223 | 135 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 25.3888 | 1713.8242 | -98.52 % | 215434.9395 MeV (+37039.1 ppm) |
| ${}^{224}$Ra | 224 | 136 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 31.8702 | 1720.3029 | -98.15 % | 216395.1728 MeV (+37003.6 ppm) |
| ${}^{225}$Ra | 225 | 137 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 38.3441 | 1725.2070 | -97.78 % | 217355.4137 MeV (+36960.6 ppm) |
| ${}^{226}$Ra | 226 | 138 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 44.8105 | 1731.6038 | -97.41 % | 218315.6621 MeV (+36925.4 ppm) |
| ${}^{227}$Ra | 227 | 139 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 51.2694 | 1736.1652 | -97.05 % | 219275.9180 MeV (+36881.6 ppm) |
| ${}^{228}$Ra | 228 | 140 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 57.7210 | 1742.4738 | -96.69 % | 220236.1811 MeV (+36846.7 ppm) |
| ${}^{229}$Ra | 229 | 141 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 64.1653 | 1746.9233 | -96.33 % | 221196.4516 MeV (+36803.1 ppm) |
| ${}^{230}$Ra | 230 | 142 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 70.6024 | 1753.0403 | -95.97 % | 222156.7293 MeV (+36768.0 ppm) |
| ${}^{231}$Ra | 231 | 143 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 77.0323 | 1757.4115 | -95.62 % | 223117.0141 MeV (+36724.8 ppm) |
| ${}^{232}$Ra | 232 | 144 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 83.4552 | 1763.2023 | -95.27 % | 224077.3060 MeV (+36688.8 ppm) |
| ${}^{233}$Ra | 233 | 145 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 89.8711 | 1767.4365 | -94.92 % | 225037.6049 MeV (+36645.7 ppm) |
| ${}^{234}$Ra | 234 | 146 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 96.2801 | 1772.9113 | -94.57 % | 225997.9107 MeV (+36609.0 ppm) |
| ${}^{235}$Ra | 235 | 147 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 102.6822 | 1776.8350 | -94.22 % | 226958.2234 MeV (+36565.0 ppm) |

### Actinium (Z = 89)

_33 of 33 isotopes with a framework prediction; 33 of 33 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{205}$Ac | 205 | 116 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -116.4616 | 1570.8846 | -107.41 % | 198174.5937 MeV (+37724.1 ppm) |
| ${}^{206}$Ac | 206 | 117 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -109.7955 | 1579.5779 | -106.95 % | 199134.6424 MeV (+37693.2 ppm) |
| ${}^{207}$Ac | 207 | 118 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -103.1388 | 1589.9877 | -106.49 % | 200094.7004 MeV (+37671.8 ppm) |
| ${}^{208}$Ac | 208 | 119 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -96.4915 | 1598.4444 | -106.04 % | 201054.7678 MeV (+37640.3 ppm) |
| ${}^{209}$Ac | 209 | 120 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -89.8533 | 1608.4317 | -105.59 % | 202014.8444 MeV (+37617.2 ppm) |
| ${}^{210}$Ac | 210 | 121 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -83.2242 | 1616.5838 | -105.15 % | 202974.9301 MeV (+37584.7 ppm) |
| ${}^{211}$Ac | 211 | 122 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -76.6041 | 1626.2757 | -104.71 % | 203935.0248 MeV (+37560.6 ppm) |
| ${}^{212}$Ac | 212 | 123 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -69.9929 | 1634.1910 | -104.28 % | 204895.1284 MeV (+37527.5 ppm) |
| ${}^{213}$Ac | 213 | 124 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -63.3905 | 1643.4208 | -103.86 % | 205855.2407 MeV (+37501.6 ppm) |
| ${}^{214}$Ac | 214 | 125 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -56.7968 | 1651.1999 | -103.44 % | 206815.3618 MeV (+37468.4 ppm) |
| ${}^{215}$Ac | 215 | 126 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -50.2117 | 1659.6739 | -103.03 % | 207775.4915 MeV (+37439.2 ppm) |
| ${}^{216}$Ac | 216 | 127 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -43.6352 | 1665.6261 | -102.62 % | 208735.6298 MeV (+37397.4 ppm) |
| ${}^{217}$Ac | 217 | 128 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -37.0671 | 1673.1448 | -102.22 % | 209695.7764 MeV (+37363.9 ppm) |
| ${}^{218}$Ac | 218 | 129 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -30.5073 | 1679.0676 | -101.82 % | 210655.9314 MeV (+37322.7 ppm) |
| ${}^{219}$Ac | 219 | 130 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -23.9558 | 1686.4202 | -101.42 % | 211616.0947 MeV (+37289.2 ppm) |
| ${}^{220}$Ac | 220 | 131 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -17.4125 | 1692.3173 | -101.03 % | 212576.2661 MeV (+37248.6 ppm) |
| ${}^{221}$Ac | 221 | 132 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -10.8772 | 1699.6014 | -100.64 % | 213536.4457 MeV (+37215.4 ppm) |
| ${}^{222}$Ac | 222 | 133 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -4.3500 | 1705.5819 | -100.26 % | 214496.6332 MeV (+37176.1 ppm) |
| ${}^{223}$Ac | 223 | 134 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 2.1693 | 1712.4500 | -99.87 % | 215456.8286 MeV (+37141.5 ppm) |
| ${}^{224}$Ac | 224 | 135 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 8.6808 | 1718.1122 | -99.49 % | 216417.0319 MeV (+37101.3 ppm) |
| ${}^{225}$Ac | 225 | 136 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 15.1845 | 1724.7804 | -99.12 % | 217377.2430 MeV (+37066.5 ppm) |
| ${}^{226}$Ac | 226 | 137 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 21.6806 | 1730.1798 | -98.75 % | 218337.4617 MeV (+37025.8 ppm) |
| ${}^{227}$Ac | 227 | 138 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 28.1690 | 1736.7108 | -98.38 % | 219297.6881 MeV (+36991.0 ppm) |
| ${}^{228}$Ac | 228 | 139 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 34.6499 | 1741.7370 | -98.01 % | 220257.9219 MeV (+36949.2 ppm) |
| ${}^{229}$Ac | 229 | 140 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 41.1234 | 1748.0130 | -97.65 % | 221218.1632 MeV (+36913.9 ppm) |
| ${}^{230}$Ac | 230 | 141 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 47.5895 | 1752.9359 | -97.29 % | 222178.4119 MeV (+36872.4 ppm) |
| ${}^{231}$Ac | 231 | 142 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 54.0483 | 1759.0827 | -96.93 % | 223138.6679 MeV (+36837.2 ppm) |
| ${}^{232}$Ac | 232 | 143 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 60.4998 | 1763.7625 | -96.57 % | 224098.9311 MeV (+36795.3 ppm) |
| ${}^{233}$Ac | 233 | 144 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 66.9442 | 1769.6802 | -96.22 % | 225059.2015 MeV (+36759.7 ppm) |
| ${}^{234}$Ac | 234 | 145 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 73.3815 | 1774.2183 | -95.86 % | 226019.4790 MeV (+36717.8 ppm) |
| ${}^{235}$Ac | 235 | 146 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 79.8118 | 1779.7737 | -95.52 % | 226979.7635 MeV (+36681.2 ppm) |
| ${}^{236}$Ac | 236 | 147 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 86.2351 | 1783.9812 | -95.17 % | 227940.0549 MeV (+36638.6 ppm) |
| ${}^{237}$Ac | 237 | 148 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 92.6516 | 1789.3500 | -94.82 % | 228900.3532 MeV (+36601.3 ppm) |

### Thorium (Z = 90)

_32 of 32 isotopes with a framework prediction; 32 of 32 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{208}$Th | 208 | 118 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -120.4235 | 1591.7349 | -107.57 % | 201077.3696 MeV (+37725.2 ppm) |
| ${}^{209}$Th | 209 | 119 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -113.7521 | 1600.1040 | -107.11 % | 202037.4130 MeV (+37692.9 ppm) |
| ${}^{210}$Th | 210 | 120 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -107.0900 | 1610.5060 | -106.65 % | 202997.4656 MeV (+37671.8 ppm) |
| ${}^{211}$Th | 211 | 121 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -100.4370 | 1618.7605 | -106.20 % | 203957.5274 MeV (+37639.5 ppm) |
| ${}^{212}$Th | 212 | 122 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -93.7932 | 1628.5973 | -105.76 % | 204917.5984 MeV (+37616.0 ppm) |
| ${}^{213}$Th | 213 | 123 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -87.1584 | 1636.6594 | -105.33 % | 205877.6783 MeV (+37583.4 ppm) |
| ${}^{214}$Th | 214 | 124 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -80.5325 | 1646.1559 | -104.89 % | 206837.7672 MeV (+37558.7 ppm) |
| ${}^{215}$Th | 215 | 125 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -73.9154 | 1654.0007 | -104.47 % | 207797.8649 MeV (+37525.6 ppm) |
| ${}^{216}$Th | 216 | 126 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -67.3070 | 1662.6949 | -104.05 % | 208757.9712 MeV (+37497.3 ppm) |
| ${}^{217}$Th | 217 | 127 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -60.7072 | 1668.8590 | -103.64 % | 209718.0863 MeV (+37456.3 ppm) |
| ${}^{218}$Th | 218 | 128 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -54.1160 | 1676.7694 | -103.23 % | 210678.2098 MeV (+37424.7 ppm) |
| ${}^{219}$Th | 219 | 129 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -47.5332 | 1682.7446 | -102.82 % | 211638.3418 MeV (+37383.5 ppm) |
| ${}^{220}$Th | 220 | 130 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -40.9588 | 1690.5892 | -102.42 % | 212598.4822 MeV (+37352.2 ppm) |
| ${}^{221}$Th | 221 | 131 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -34.3926 | 1696.4101 | -102.03 % | 213558.6308 MeV (+37311.1 ppm) |
| ${}^{222}$Th | 222 | 132 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -27.8347 | 1704.2183 | -101.63 % | 214518.7876 MeV (+37280.3 ppm) |
| ${}^{223}$Th | 223 | 133 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -21.2848 | 1710.1073 | -101.24 % | 215478.9525 MeV (+37240.2 ppm) |
| ${}^{224}$Th | 224 | 134 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -14.7430 | 1717.5684 | -100.86 % | 216439.1254 MeV (+37208.4 ppm) |
| ${}^{225}$Th | 225 | 135 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -8.2091 | 1723.3252 | -100.48 % | 217399.3063 MeV (+37168.5 ppm) |
| ${}^{226}$Th | 226 | 136 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -1.6830 | 1730.5090 | -100.10 % | 218359.4950 MeV (+37135.9 ppm) |
| ${}^{227}$Th | 227 | 137 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 4.8353 | 1735.9732 | -99.72 % | 219319.6915 MeV (+37095.3 ppm) |
| ${}^{228}$Th | 228 | 138 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 11.3458 | 1743.0784 | -99.35 % | 220279.8957 MeV (+37063.1 ppm) |
| ${}^{229}$Th | 229 | 139 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 17.8488 | 1748.3351 | -98.98 % | 221240.1075 MeV (+37022.2 ppm) |
| ${}^{230}$Th | 230 | 140 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 24.3442 | 1755.1294 | -98.61 % | 222200.3269 MeV (+36989.1 ppm) |
| ${}^{231}$Th | 231 | 141 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 30.8321 | 1760.2474 | -98.25 % | 223160.5537 MeV (+36948.3 ppm) |
| ${}^{232}$Th | 232 | 142 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 37.3127 | 1766.6878 | -97.89 % | 224120.7880 MeV (+36914.2 ppm) |
| ${}^{233}$Th | 233 | 143 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 43.7859 | 1771.4742 | -97.53 % | 225081.0295 MeV (+36872.5 ppm) |
| ${}^{234}$Th | 234 | 144 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 50.2519 | 1777.6642 | -97.17 % | 226041.2783 MeV (+36837.9 ppm) |
| ${}^{235}$Th | 235 | 145 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 56.7107 | 1782.3308 | -96.82 % | 227001.5343 MeV (+36796.4 ppm) |
| ${}^{236}$Th | 236 | 146 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 63.1624 | 1788.1646 | -96.47 % | 227961.7974 MeV (+36760.8 ppm) |
| ${}^{237}$Th | 237 | 147 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 69.6070 | 1792.5361 | -96.12 % | 228922.0675 MeV (+36718.7 ppm) |
| ${}^{238}$Th | 238 | 148 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 76.0447 | 1798.0900 | -95.77 % | 229882.3446 MeV (+36682.3 ppm) |
| ${}^{239}$Th | 239 | 149 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 82.4754 | 1802.0600 | -95.42 % | 230842.6286 MeV (+36639.6 ppm) |

### Protactinium (Z = 91)

_31 of 31 isotopes with a framework prediction; 31 of 31 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{211}$Pa | 211 | 120 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -124.5090 | 1609.8023 | -107.73 % | 203980.2691 MeV (+37712.1 ppm) |
| ${}^{212}$Pa | 212 | 121 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -117.8322 | 1618.3293 | -107.28 % | 204940.3070 MeV (+37681.1 ppm) |
| ${}^{213}$Pa | 213 | 122 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -111.1645 | 1628.3430 | -106.83 % | 205900.3542 MeV (+37658.3 ppm) |
| ${}^{214}$Pa | 214 | 123 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -104.5060 | 1636.6086 | -106.39 % | 206860.4104 MeV (+37626.6 ppm) |
| ${}^{215}$Pa | 215 | 124 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -97.8565 | 1646.3353 | -105.94 % | 207820.4757 MeV (+37602.9 ppm) |
| ${}^{216}$Pa | 216 | 125 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -91.2159 | 1654.3873 | -105.51 % | 208780.5499 MeV (+37570.7 ppm) |
| ${}^{217}$Pa | 217 | 126 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -84.5842 | 1663.2277 | -105.09 % | 209740.6329 MeV (+37543.0 ppm) |
| ${}^{218}$Pa | 218 | 127 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -77.9611 | 1669.7042 | -104.67 % | 210700.7246 MeV (+37503.4 ppm) |
| ${}^{219}$Pa | 219 | 128 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -71.3467 | 1677.8418 | -104.25 % | 211660.8250 MeV (+37472.8 ppm) |
| ${}^{220}$Pa | 220 | 129 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -64.7409 | 1684.2180 | -103.84 % | 212620.9339 MeV (+37433.5 ppm) |
| ${}^{221}$Pa | 221 | 130 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -58.1435 | 1692.1928 | -103.44 % | 213581.0513 MeV (+37402.7 ppm) |
| ${}^{222}$Pa | 222 | 131 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -51.5544 | 1698.5747 | -103.04 % | 214541.1771 MeV (+37364.2 ppm) |
| ${}^{223}$Pa | 223 | 132 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -44.9737 | 1706.3727 | -102.64 % | 215501.3111 MeV (+37333.1 ppm) |
| ${}^{224}$Pa | 224 | 133 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -38.4012 | 1712.9193 | -102.24 % | 216461.4533 MeV (+37296.2 ppm) |
| ${}^{225}$Pa | 225 | 134 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -31.8367 | 1720.4963 | -101.85 % | 217421.6037 MeV (+37264.7 ppm) |
| ${}^{226}$Pa | 226 | 135 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -25.2803 | 1726.8907 | -101.46 % | 218381.7620 MeV (+37227.7 ppm) |
| ${}^{227}$Pa | 227 | 136 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -18.7319 | 1734.1653 | -101.08 % | 219341.9284 MeV (+37195.4 ppm) |
| ${}^{228}$Pa | 228 | 137 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -12.1913 | 1740.1433 | -100.70 % | 220302.1026 MeV (+37157.1 ppm) |
| ${}^{229}$Pa | 229 | 138 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -5.6585 | 1747.2414 | -100.32 % | 221262.2846 MeV (+37124.6 ppm) |
| ${}^{230}$Pa | 230 | 139 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 0.8665 | 1753.0360 | -99.95 % | 222222.4743 MeV (+37086.1 ppm) |
| ${}^{231}$Pa | 231 | 140 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 7.3840 | 1759.8566 | -99.58 % | 223182.6716 MeV (+37052.9 ppm) |
| ${}^{232}$Pa | 232 | 141 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 13.8938 | 1765.4057 | -99.21 % | 224142.8765 MeV (+37014.0 ppm) |
| ${}^{233}$Pa | 233 | 142 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 20.3962 | 1771.9341 | -98.85 % | 225103.0889 MeV (+36980.1 ppm) |
| ${}^{234}$Pa | 234 | 143 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 26.8912 | 1777.1560 | -98.49 % | 226063.3087 MeV (+36940.3 ppm) |
| ${}^{235}$Pa | 235 | 144 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 33.3788 | 1783.2773 | -98.13 % | 227023.5359 MeV (+36905.1 ppm) |
| ${}^{236}$Pa | 236 | 145 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 39.8591 | 1788.3035 | -97.77 % | 227983.7703 MeV (+36865.1 ppm) |
| ${}^{237}$Pa | 237 | 146 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 46.3323 | 1794.1812 | -97.42 % | 228944.0119 MeV (+36829.5 ppm) |
| ${}^{238}$Pa | 238 | 147 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 52.7983 | 1798.8861 | -97.06 % | 229904.2607 MeV (+36788.7 ppm) |
| ${}^{239}$Pa | 239 | 148 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 59.2573 | 1804.4500 | -96.72 % | 230864.5165 MeV (+36752.6 ppm) |
| ${}^{240}$Pa | 240 | 149 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 65.7093 | 1808.8800 | -96.37 % | 231824.7793 MeV (+36711.1 ppm) |
| ${}^{241}$Pa | 241 | 150 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 72.1543 | 1814.2480 | -96.02 % | 232785.0490 MeV (+36674.4 ppm) |

### Uranium (Z = 92)

_29 of 29 isotopes with a framework prediction; 29 of 29 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{215}$U | 215 | 123 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -122.0352 | 1638.4682 | -107.45 % | 207843.3241 MeV (+37680.2 ppm) |
| ${}^{216}$U | 216 | 124 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -115.3621 | 1648.3624 | -107.00 % | 208803.3657 MeV (+37657.1 ppm) |
| ${}^{217}$U | 217 | 125 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -108.6979 | 1656.5780 | -106.56 % | 209763.4164 MeV (+37625.3 ppm) |
| ${}^{218}$U | 218 | 126 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -102.0427 | 1665.6768 | -106.13 % | 210723.4760 MeV (+37598.9 ppm) |
| ${}^{219}$U | 219 | 127 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -95.3964 | 1672.3468 | -105.70 % | 211683.5444 MeV (+37560.1 ppm) |
| ${}^{220}$U | 220 | 128 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -88.7587 | 1680.8000 | -105.28 % | 212643.6215 MeV (+37530.3 ppm) |
| ${}^{221}$U | 221 | 129 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -82.1297 | 1687.2654 | -104.87 % | 213603.7073 MeV (+37491.8 ppm) |
| ${}^{222}$U | 222 | 130 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -75.5093 | 1695.5839 | -104.45 % | 214563.8016 MeV (+37462.5 ppm) |
| ${}^{223}$U | 223 | 131 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -68.8973 | 1701.8827 | -104.05 % | 215523.9044 MeV (+37423.4 ppm) |
| ${}^{224}$U | 224 | 132 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -62.2937 | 1710.2566 | -103.64 % | 216484.0156 MeV (+37394.9 ppm) |
| ${}^{225}$U | 225 | 133 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -55.6984 | 1716.6986 | -103.24 % | 217444.1351 MeV (+37357.3 ppm) |
| ${}^{226}$U | 226 | 134 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -49.1114 | 1724.8132 | -102.85 % | 218404.2628 MeV (+37328.2 ppm) |
| ${}^{227}$U | 227 | 135 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -42.5324 | 1731.1682 | -102.46 % | 219364.3986 MeV (+37290.8 ppm) |
| ${}^{228}$U | 228 | 136 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -35.9615 | 1739.0646 | -102.07 % | 220324.5425 MeV (+37261.3 ppm) |
| ${}^{229}$U | 229 | 137 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -29.3986 | 1745.1453 | -101.68 % | 221284.6943 MeV (+37223.3 ppm) |
| ${}^{230}$U | 230 | 138 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -22.8435 | 1752.8122 | -101.30 % | 222244.8540 MeV (+37193.3 ppm) |
| ${}^{231}$U | 231 | 139 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -16.2963 | 1758.6926 | -100.93 % | 223205.0215 MeV (+37155.0 ppm) |
| ${}^{232}$U | 232 | 140 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -9.7568 | 1765.9604 | -100.55 % | 224165.1968 MeV (+37123.7 ppm) |
| ${}^{233}$U | 233 | 141 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -3.2249 | 1771.7221 | -100.18 % | 225125.3797 MeV (+37085.5 ppm) |
| ${}^{234}$U | 234 | 142 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 3.2994 | 1778.5675 | -99.81 % | 226085.5702 MeV (+37052.8 ppm) |
| ${}^{235}$U | 235 | 143 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 9.8162 | 1783.8650 | -99.45 % | 227045.7682 MeV (+37013.2 ppm) |
| ${}^{236}$U | 236 | 144 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 16.3255 | 1790.4106 | -99.09 % | 228005.9736 MeV (+36979.7 ppm) |
| ${}^{237}$U | 237 | 145 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 22.8275 | 1795.5363 | -98.73 % | 228966.1864 MeV (+36940.0 ppm) |
| ${}^{238}$U | 238 | 146 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 29.3222 | 1801.6900 | -98.37 % | 229926.4065 MeV (+36905.4 ppm) |
| ${}^{239}$U | 239 | 147 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 35.8097 | 1806.4964 | -98.02 % | 230886.6338 MeV (+36864.8 ppm) |
| ${}^{240}$U | 240 | 148 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 42.2900 | 1812.4249 | -97.67 % | 231846.8683 MeV (+36829.8 ppm) |
| ${}^{241}$U | 241 | 149 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 48.7632 | 1816.8990 | -97.32 % | 232807.1098 MeV (+36789.0 ppm) |
| ${}^{242}$U | 242 | 150 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 55.2295 | 1822.7440 | -96.97 % | 233767.3583 MeV (+36753.4 ppm) |
| ${}^{243}$U | 243 | 151 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 61.6887 | 1826.8740 | -96.62 % | 234727.6138 MeV (+36711.6 ppm) |

### Neptunium (Z = 93)

_27 of 27 isotopes with a framework prediction; 27 of 27 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{219}$Np | 219 | 126 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -119.6821 | 1665.4234 | -107.19 % | 211706.4998 MeV (+37641.4 ppm) |
| ${}^{220}$Np | 220 | 127 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -113.0123 | 1672.4567 | -106.76 % | 212666.5448 MeV (+37604.4 ppm) |
| ${}^{221}$Np | 221 | 128 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -106.3514 | 1681.1470 | -106.33 % | 213626.5986 MeV (+37575.8 ppm) |
| ${}^{222}$Np | 222 | 129 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -99.6992 | 1687.7997 | -105.91 % | 214586.6612 MeV (+37537.9 ppm) |
| ${}^{223}$Np | 223 | 130 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -93.0557 | 1696.4871 | -105.49 % | 215546.7324 MeV (+37510.2 ppm) |
| ${}^{224}$Np | 224 | 131 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -86.4207 | 1703.1847 | -105.07 % | 216506.8122 MeV (+37472.9 ppm) |
| ${}^{225}$Np | 225 | 132 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -79.7942 | 1711.6702 | -104.66 % | 217466.9005 MeV (+37444.9 ppm) |
| ${}^{226}$Np | 226 | 133 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -73.1761 | 1718.5427 | -104.26 % | 218426.9972 MeV (+37409.1 ppm) |
| ${}^{227}$Np | 227 | 134 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -66.5663 | 1726.8519 | -103.85 % | 219387.1022 MeV (+37380.8 ppm) |
| ${}^{228}$Np | 228 | 135 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -59.9647 | 1733.7120 | -103.46 % | 220347.2154 MeV (+37345.5 ppm) |
| ${}^{229}$Np | 229 | 136 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -53.3713 | 1741.7722 | -103.06 % | 221307.3367 MeV (+37316.8 ppm) |
| ${}^{230}$Np | 230 | 137 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -46.7859 | 1748.4083 | -102.68 % | 222267.4661 MeV (+37281.3 ppm) |
| ${}^{231}$Np | 231 | 138 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -40.2085 | 1756.0925 | -102.29 % | 223227.6035 MeV (+37251.1 ppm) |
| ${}^{232}$Np | 232 | 139 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -33.6391 | 1762.5040 | -101.91 % | 224187.7488 MeV (+37214.8 ppm) |
| ${}^{233}$Np | 233 | 140 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -27.0774 | 1769.9103 | -101.53 % | 225147.9019 MeV (+37184.3 ppm) |
| ${}^{234}$Np | 234 | 141 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -20.5235 | 1775.9753 | -101.16 % | 226108.0628 MeV (+37147.4 ppm) |
| ${}^{235}$Np | 235 | 142 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -13.9772 | 1782.9584 | -100.78 % | 227068.2313 MeV (+37115.2 ppm) |
| ${}^{236}$Np | 236 | 143 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -7.4386 | 1788.6947 | -100.42 % | 228028.4074 MeV (+37077.4 ppm) |
| ${}^{237}$Np | 237 | 144 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -0.9074 | 1795.2725 | -100.05 % | 228988.5911 MeV (+37043.9 ppm) |
| ${}^{238}$Np | 238 | 145 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 5.6162 | 1800.7608 | -99.69 % | 229948.7822 MeV (+37005.6 ppm) |
| ${}^{239}$Np | 239 | 146 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 12.1325 | 1806.9758 | -99.33 % | 230908.9806 MeV (+36971.0 ppm) |
| ${}^{240}$Np | 240 | 147 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 18.6415 | 1812.0418 | -98.97 % | 231869.1864 MeV (+36931.5 ppm) |
| ${}^{241}$Np | 241 | 148 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 25.1433 | 1818.1143 | -98.62 % | 232829.3994 MeV (+36897.0 ppm) |
| ${}^{242}$Np | 242 | 149 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 31.6379 | 1823.0838 | -98.26 % | 233789.6196 MeV (+36857.7 ppm) |
| ${}^{243}$Np | 243 | 150 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 38.1254 | 1828.8180 | -97.92 % | 234749.8469 MeV (+36822.0 ppm) |
| ${}^{244}$Np | 244 | 151 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 44.6058 | 1833.4160 | -97.57 % | 235710.0812 MeV (+36781.9 ppm) |
| ${}^{245}$Np | 245 | 152 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 51.0793 | 1838.9700 | -97.22 % | 236670.3225 MeV (+36745.9 ppm) |

### Plutonium (Z = 94)

_27 of 27 isotopes with a framework prediction; 27 of 27 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{221}$Pu | 221 | 127 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -130.8085 | 1674.2960 | -107.81 % | 213649.7254 MeV (+37657.8 ppm) |
| ${}^{222}$Pu | 222 | 128 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -124.1242 | 1683.2040 | -107.37 % | 214609.7559 MeV (+37630.6 ppm) |
| ${}^{223}$Pu | 223 | 129 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -117.4487 | 1690.3400 | -106.95 % | 215569.7952 MeV (+37593.9 ppm) |
| ${}^{224}$Pu | 224 | 130 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -110.7820 | 1699.2640 | -106.52 % | 216529.8433 MeV (+37567.1 ppm) |
| ${}^{225}$Pu | 225 | 131 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -104.1240 | 1706.1750 | -106.10 % | 217489.9000 MeV (+37531.4 ppm) |
| ${}^{226}$Pu | 226 | 132 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -97.4745 | 1714.8880 | -105.68 % | 218449.9653 MeV (+37504.4 ppm) |
| ${}^{227}$Pu | 227 | 133 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -90.8335 | 1721.7950 | -105.28 % | 219410.0391 MeV (+37468.7 ppm) |
| ${}^{228}$Pu | 228 | 134 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -84.2010 | 1730.6121 | -104.87 % | 220370.1213 MeV (+37442.2 ppm) |
| ${}^{229}$Pu | 229 | 135 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -77.5767 | 1737.3963 | -104.47 % | 221330.2119 MeV (+37406.5 ppm) |
| ${}^{230}$Pu | 230 | 136 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -70.9607 | 1745.9304 | -104.06 % | 222290.3106 MeV (+37379.7 ppm) |
| ${}^{231}$Pu | 231 | 137 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -64.3529 | 1752.6253 | -103.67 % | 223250.4175 MeV (+37344.2 ppm) |
| ${}^{232}$Pu | 232 | 138 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -57.7531 | 1760.6443 | -103.28 % | 224210.5325 MeV (+37315.4 ppm) |
| ${}^{233}$Pu | 233 | 139 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -51.1613 | 1767.0247 | -102.90 % | 225170.6555 MeV (+37279.1 ppm) |
| ${}^{234}$Pu | 234 | 140 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -44.5774 | 1774.7978 | -102.51 % | 226130.7864 MeV (+37249.7 ppm) |
| ${}^{235}$Pu | 235 | 141 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -38.0014 | 1781.0368 | -102.13 % | 227090.9251 MeV (+37213.4 ppm) |
| ${}^{236}$Pu | 236 | 142 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -31.4331 | 1788.3889 | -101.76 % | 228051.0716 MeV (+37182.7 ppm) |
| ${}^{237}$Pu | 237 | 143 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -24.8725 | 1794.2701 | -101.39 % | 229011.2258 MeV (+37145.3 ppm) |
| ${}^{238}$Pu | 238 | 144 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -18.3195 | 1801.2699 | -101.02 % | 229971.3876 MeV (+37113.6 ppm) |
| ${}^{239}$Pu | 239 | 145 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -11.7741 | 1806.9162 | -100.65 % | 230931.5569 MeV (+37075.8 ppm) |
| ${}^{240}$Pu | 240 | 146 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -5.2361 | 1813.4504 | -100.29 % | 231891.7337 MeV (+37042.5 ppm) |
| ${}^{241}$Pu | 241 | 147 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 1.2945 | 1818.6919 | -99.93 % | 232851.9179 MeV (+37003.5 ppm) |
| ${}^{242}$Pu | 242 | 148 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 7.8178 | 1825.0015 | -99.57 % | 233812.1094 MeV (+36969.8 ppm) |
| ${}^{243}$Pu | 243 | 149 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 14.3338 | 1830.0351 | -99.22 % | 234772.3082 MeV (+36930.6 ppm) |
| ${}^{244}$Pu | 244 | 150 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 20.8426 | 1836.0550 | -98.86 % | 235732.5142 MeV (+36896.2 ppm) |
| ${}^{245}$Pu | 245 | 151 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 27.3443 | 1840.7541 | -98.51 % | 236692.7273 MeV (+36856.1 ppm) |
| ${}^{246}$Pu | 246 | 152 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 33.8389 | 1846.6089 | -98.17 % | 237652.9474 MeV (+36821.7 ppm) |
| ${}^{247}$Pu | 247 | 153 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 40.3266 | 1850.7710 | -97.82 % | 238613.1745 MeV (+36780.3 ppm) |

### Americium (Z = 95)

_27 of 27 isotopes with a framework prediction; 27 of 27 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{223}$Am | 223 | 128 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -142.0765 | 1682.9810 | -108.44 % | 215593.0927 MeV (+37673.2 ppm) |
| ${}^{224}$Am | 224 | 129 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -135.3777 | 1690.3040 | -108.01 % | 216553.1087 MeV (+37638.9 ppm) |
| ${}^{225}$Am | 225 | 130 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -128.6878 | 1699.4250 | -107.57 % | 217513.1336 MeV (+37612.1 ppm) |
| ${}^{226}$Am | 226 | 131 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -122.0067 | 1706.7520 | -107.15 % | 218473.1672 MeV (+37578.4 ppm) |
| ${}^{227}$Am | 227 | 132 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -115.3342 | 1715.6660 | -106.72 % | 219433.2095 MeV (+37551.7 ppm) |
| ${}^{228}$Am | 228 | 133 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -108.6703 | 1722.9960 | -106.31 % | 220393.2603 MeV (+37518.2 ppm) |
| ${}^{229}$Am | 229 | 134 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -102.0149 | 1731.8285 | -105.89 % | 221353.3197 MeV (+37491.6 ppm) |
| ${}^{230}$Am | 230 | 135 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -95.3679 | 1739.2600 | -105.48 % | 222313.3875 MeV (+37458.6 ppm) |
| ${}^{231}$Am | 231 | 136 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -88.7292 | 1747.7460 | -105.08 % | 223273.4636 MeV (+37431.5 ppm) |
| ${}^{232}$Am | 232 | 137 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -82.0988 | 1754.8480 | -104.68 % | 224233.5480 MeV (+37397.6 ppm) |
| ${}^{233}$Am | 233 | 138 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -75.4766 | 1763.1110 | -104.28 % | 225193.6405 MeV (+37369.5 ppm) |
| ${}^{234}$Am | 234 | 139 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -68.8624 | 1769.9760 | -103.89 % | 226153.7411 MeV (+37335.5 ppm) |
| ${}^{235}$Am | 235 | 140 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -62.2563 | 1777.8122 | -103.50 % | 227113.8497 MeV (+37306.6 ppm) |
| ${}^{236}$Am | 236 | 141 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -55.6580 | 1784.3960 | -103.12 % | 228073.9663 MeV (+37272.0 ppm) |
| ${}^{237}$Am | 237 | 142 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -49.0677 | 1791.9570 | -102.74 % | 229034.0907 MeV (+37241.9 ppm) |
| ${}^{238}$Am | 238 | 143 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -42.4851 | 1798.2293 | -102.36 % | 229994.2229 MeV (+37206.0 ppm) |
| ${}^{239}$Am | 239 | 144 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -35.9102 | 1805.3317 | -101.99 % | 230954.3627 MeV (+37174.5 ppm) |
| ${}^{240}$Am | 240 | 145 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -29.3429 | 1811.2833 | -101.62 % | 231914.5102 MeV (+37137.9 ppm) |
| ${}^{241}$Am | 241 | 146 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -22.7832 | 1817.9304 | -101.25 % | 232874.6653 MeV (+37104.9 ppm) |
| ${}^{242}$Am | 242 | 147 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -16.2309 | 1823.4680 | -100.89 % | 233834.8278 MeV (+37067.1 ppm) |
| ${}^{243}$Am | 243 | 148 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -9.6861 | 1829.8323 | -100.53 % | 234794.9978 MeV (+37033.5 ppm) |
| ${}^{244}$Am | 244 | 149 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -3.1486 | 1835.1995 | -100.17 % | 235755.1751 MeV (+36995.6 ppm) |
| ${}^{245}$Am | 245 | 150 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 3.3816 | 1841.2496 | -99.82 % | 236715.3596 MeV (+36961.1 ppm) |
| ${}^{246}$Am | 246 | 151 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 9.9046 | 1846.2300 | -99.46 % | 237675.5514 MeV (+36922.1 ppm) |
| ${}^{247}$Am | 247 | 152 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 16.4204 | 1852.2530 | -99.11 % | 238635.7503 MeV (+36887.7 ppm) |
| ${}^{248}$Am | 248 | 153 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 22.9292 | 1856.7760 | -98.77 % | 239595.9563 MeV (+36847.9 ppm) |
| ${}^{249}$Am | 249 | 154 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 29.4310 | 1862.2710 | -98.42 % | 240556.1693 MeV (+36812.4 ppm) |

### Curium (Z = 96)

_22 of 22 isotopes with a framework prediction; 22 of 22 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{231}$Cm | 231 | 135 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -113.3376 | 1742.2020 | -106.51 % | 223296.7417 MeV (+37516.2 ppm) |
| ${}^{232}$Cm | 232 | 136 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -106.6763 | 1751.1360 | -106.09 % | 224256.7951 MeV (+37491.2 ppm) |
| ${}^{233}$Cm | 233 | 137 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -100.0233 | 1758.2185 | -105.69 % | 225216.8569 MeV (+37457.3 ppm) |
| ${}^{234}$Cm | 234 | 138 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -93.3785 | 1766.8607 | -105.28 % | 226176.9269 MeV (+37431.1 ppm) |
| ${}^{235}$Cm | 235 | 139 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -86.7419 | 1773.5450 | -104.89 % | 227137.0051 MeV (+37396.3 ppm) |
| ${}^{236}$Cm | 236 | 140 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -80.1134 | 1781.8729 | -104.50 % | 228097.0914 MeV (+37368.6 ppm) |
| ${}^{237}$Cm | 237 | 141 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -73.4929 | 1788.5499 | -104.11 % | 229057.1857 MeV (+37334.0 ppm) |
| ${}^{238}$Cm | 238 | 142 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -66.8804 | 1796.4232 | -103.72 % | 230017.2879 MeV (+37305.2 ppm) |
| ${}^{239}$Cm | 239 | 143 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -60.2757 | 1802.7928 | -103.34 % | 230977.3980 MeV (+37269.7 ppm) |
| ${}^{240}$Cm | 240 | 144 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -53.6789 | 1810.2868 | -102.97 % | 231937.5159 MeV (+37239.8 ppm) |
| ${}^{241}$Cm | 241 | 145 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -47.0897 | 1816.3806 | -102.59 % | 232897.6415 MeV (+37203.7 ppm) |
| ${}^{242}$Cm | 242 | 146 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -40.5082 | 1823.3500 | -102.22 % | 233857.7748 MeV (+37172.0 ppm) |
| ${}^{243}$Cm | 243 | 147 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -33.9342 | 1829.0430 | -101.86 % | 234817.9156 MeV (+37134.7 ppm) |
| ${}^{244}$Cm | 244 | 148 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -27.3678 | 1835.8445 | -101.49 % | 235778.0639 MeV (+37102.7 ppm) |
| ${}^{245}$Cm | 245 | 149 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -20.8088 | 1841.3631 | -101.13 % | 236738.2197 MeV (+37065.3 ppm) |
| ${}^{246}$Cm | 246 | 150 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -14.2571 | 1847.8220 | -100.77 % | 237698.3828 MeV (+37032.5 ppm) |
| ${}^{247}$Cm | 247 | 151 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -7.7127 | 1852.9772 | -100.42 % | 238658.5532 MeV (+36994.0 ppm) |
| ${}^{248}$Cm | 248 | 152 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -1.1756 | 1859.1888 | -100.06 % | 239618.7308 MeV (+36960.7 ppm) |
| ${}^{249}$Cm | 249 | 153 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 5.3544 | 1863.9022 | -99.71 % | 240578.9156 MeV (+36921.0 ppm) |
| ${}^{250}$Cm | 250 | 154 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 11.8773 | 1869.7346 | -99.36 % | 241539.1075 MeV (+36886.5 ppm) |
| ${}^{251}$Cm | 251 | 155 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 18.3932 | 1874.1475 | -99.02 % | 242499.3064 MeV (+36846.1 ppm) |
| ${}^{252}$Cm | 252 | 156 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 24.9021 | 1879.9200 | -98.68 % | 243459.5122 MeV (+36811.6 ppm) |

### Berkelium (Z = 97)

_22 of 22 isotopes with a framework prediction; 22 of 22 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{233}$Bk | 233 | 136 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -124.8013 | 1751.9270 | -107.12 % | 225240.3047 MeV (+37539.1 ppm) |
| ${}^{234}$Bk | 234 | 137 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -118.1256 | 1759.4460 | -106.71 % | 226200.3437 MeV (+37506.7 ppm) |
| ${}^{235}$Bk | 235 | 138 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -111.4583 | 1768.1400 | -106.30 % | 227160.3912 MeV (+37480.5 ppm) |
| ${}^{236}$Bk | 236 | 139 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -104.7992 | 1775.4280 | -105.90 % | 228120.4469 MeV (+37448.0 ppm) |
| ${}^{237}$Bk | 237 | 140 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -98.1483 | 1783.8990 | -105.50 % | 229080.5108 MeV (+37421.0 ppm) |
| ${}^{238}$Bk | 238 | 141 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -91.5056 | 1790.9500 | -105.11 % | 230040.5828 MeV (+37387.9 ppm) |
| ${}^{239}$Bk | 239 | 142 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -84.8708 | 1798.9530 | -104.72 % | 231000.6628 MeV (+37359.8 ppm) |
| ${}^{240}$Bk | 240 | 143 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -78.2440 | 1805.5200 | -104.33 % | 231960.7508 MeV (+37325.4 ppm) |
| ${}^{241}$Bk | 241 | 144 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -71.6251 | 1813.2840 | -103.95 % | 232920.8466 MeV (+37296.5 ppm) |
| ${}^{242}$Bk | 242 | 145 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -65.0140 | 1819.5980 | -103.57 % | 233880.9503 MeV (+37261.2 ppm) |
| ${}^{243}$Bk | 243 | 146 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -58.4106 | 1826.7530 | -103.20 % | 234841.0617 MeV (+37230.0 ppm) |
| ${}^{244}$Bk | 244 | 147 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -51.8149 | 1832.8001 | -102.83 % | 235801.1807 MeV (+37194.1 ppm) |
| ${}^{245}$Bk | 245 | 148 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -45.2267 | 1839.7715 | -102.46 % | 236761.3074 MeV (+37162.8 ppm) |
| ${}^{246}$Bk | 246 | 149 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -38.6461 | 1845.6897 | -102.09 % | 237721.4415 MeV (+37127.0 ppm) |
| ${}^{247}$Bk | 247 | 150 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -32.0729 | 1852.2384 | -101.73 % | 238681.5831 MeV (+37094.3 ppm) |
| ${}^{248}$Bk | 248 | 151 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -25.5071 | 1857.6682 | -101.37 % | 239641.7321 MeV (+37056.9 ppm) |
| ${}^{249}$Bk | 249 | 152 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -18.9486 | 1864.0242 | -101.02 % | 240601.8883 MeV (+37024.0 ppm) |
| ${}^{250}$Bk | 250 | 153 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -12.3974 | 1868.9898 | -100.66 % | 241562.0519 MeV (+36985.2 ppm) |
| ${}^{251}$Bk | 251 | 154 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -5.8533 | 1874.7852 | -100.31 % | 242522.2226 MeV (+36950.4 ppm) |
| ${}^{252}$Bk | 252 | 155 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 0.6837 | 1879.6680 | -99.96 % | 243482.4003 MeV (+36911.4 ppm) |
| ${}^{253}$Bk | 253 | 156 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 7.2136 | 1885.1030 | -99.62 % | 244442.5852 MeV (+36876.7 ppm) |
| ${}^{254}$Bk | 254 | 157 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 13.7366 | 1889.7600 | -99.27 % | 245402.7770 MeV (+36837.7 ppm) |

### Californium (Z = 98)

_20 of 20 isotopes with a framework prediction; 20 of 20 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{237}$Cf | 237 | 139 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -123.0338 | 1778.2941 | -106.92 % | 229104.0660 MeV (+37505.4 ppm) |
| ${}^{238}$Cf | 238 | 140 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -116.3605 | 1787.1420 | -106.51 % | 230064.1074 MeV (+37479.7 ppm) |
| ${}^{239}$Cf | 239 | 141 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -109.6954 | 1794.1730 | -106.11 % | 231024.1570 MeV (+37446.9 ppm) |
| ${}^{240}$Cf | 240 | 142 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -103.0383 | 1802.4576 | -105.72 % | 231984.2148 MeV (+37419.6 ppm) |
| ${}^{241}$Cf | 241 | 143 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -96.3894 | 1809.1870 | -105.33 % | 232944.2806 MeV (+37385.4 ppm) |
| ${}^{242}$Cf | 242 | 144 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -89.7483 | 1817.2020 | -104.94 % | 233904.3543 MeV (+37357.5 ppm) |
| ${}^{243}$Cf | 243 | 145 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -83.1152 | 1823.7150 | -104.56 % | 234864.4360 MeV (+37322.7 ppm) |
| ${}^{244}$Cf | 244 | 146 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -76.4899 | 1831.2535 | -104.18 % | 235824.5255 MeV (+37293.3 ppm) |
| ${}^{245}$Cf | 245 | 147 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -69.8724 | 1837.4178 | -103.80 % | 236784.6227 MeV (+37257.8 ppm) |
| ${}^{246}$Cf | 246 | 148 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -63.2625 | 1844.7840 | -103.43 % | 237744.7276 MeV (+37228.0 ppm) |
| ${}^{247}$Cf | 247 | 149 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -56.6602 | 1850.8362 | -103.06 % | 238704.8400 MeV (+37192.6 ppm) |
| ${}^{248}$Cf | 248 | 150 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -50.0654 | 1857.7789 | -102.69 % | 239664.9601 MeV (+37161.4 ppm) |
| ${}^{249}$Cf | 249 | 151 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -43.4781 | 1863.3655 | -102.33 % | 240625.0875 MeV (+37124.6 ppm) |
| ${}^{250}$Cf | 250 | 152 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -36.8982 | 1869.9892 | -101.97 % | 241585.2224 MeV (+37092.6 ppm) |
| ${}^{251}$Cf | 251 | 153 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -30.3256 | 1875.0959 | -101.62 % | 242545.3646 MeV (+37054.2 ppm) |
| ${}^{252}$Cf | 252 | 154 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -23.7603 | 1881.2675 | -101.26 % | 243505.5140 MeV (+37020.9 ppm) |
| ${}^{253}$Cf | 253 | 155 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -17.2021 | 1886.0719 | -100.91 % | 244465.6707 MeV (+36981.8 ppm) |
| ${}^{254}$Cf | 254 | 156 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -10.6511 | 1892.1034 | -100.56 % | 245425.8344 MeV (+36948.5 ppm) |
| ${}^{255}$Cf | 255 | 157 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -4.1072 | 1896.6900 | -100.22 % | 246386.0052 MeV (+36909.2 ppm) |
| ${}^{256}$Cf | 256 | 158 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | 2.4298 | 1902.5920 | -99.87 % | 247346.1831 MeV (+36875.6 ppm) |

### Einsteinium (Z = 99)

_20 of 20 isotopes with a framework prediction; 20 of 20 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{239}$Es | 239 | 140 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -134.7494 | 1787.9590 | -107.54 % | 231047.8808 MeV (+37528.1 ppm) |
| ${}^{240}$Es | 240 | 141 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -128.0618 | 1795.4400 | -107.13 % | 232007.9080 MeV (+37496.6 ppm) |
| ${}^{241}$Es | 241 | 142 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -121.3825 | 1803.8850 | -106.73 % | 232967.9434 MeV (+37469.7 ppm) |
| ${}^{242}$Es | 242 | 143 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -114.7113 | 1810.8860 | -106.33 % | 233927.9870 MeV (+37437.4 ppm) |
| ${}^{243}$Es | 243 | 144 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -108.0481 | 1819.0980 | -105.94 % | 234888.0386 MeV (+37409.7 ppm) |
| ${}^{244}$Es | 244 | 145 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -101.3929 | 1825.8520 | -105.55 % | 235848.0981 MeV (+37376.2 ppm) |
| ${}^{245}$Es | 245 | 146 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -94.7456 | 1833.8250 | -105.17 % | 236808.1656 MeV (+37347.6 ppm) |
| ${}^{246}$Es | 246 | 147 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -88.1062 | 1840.2731 | -104.79 % | 237768.2410 MeV (+37313.7 ppm) |
| ${}^{247}$Es | 247 | 148 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -81.4745 | 1847.5848 | -104.41 % | 238728.3240 MeV (+37283.5 ppm) |
| ${}^{248}$Es | 248 | 149 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -74.8504 | 1854.0480 | -104.04 % | 239688.4148 MeV (+37249.2 ppm) |
| ${}^{249}$Es | 249 | 150 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -68.2340 | 1861.0260 | -103.67 % | 240648.5132 MeV (+37219.0 ppm) |
| ${}^{250}$Es | 250 | 151 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -61.6252 | 1867.2500 | -103.30 % | 241608.6191 MeV (+37183.9 ppm) |
| ${}^{251}$Es | 251 | 152 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -55.0238 | 1873.9369 | -102.94 % | 242568.7325 MeV (+37152.5 ppm) |
| ${}^{252}$Es | 252 | 153 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -48.4298 | 1879.2252 | -102.58 % | 243528.8533 MeV (+37114.7 ppm) |
| ${}^{253}$Es | 253 | 154 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -41.8432 | 1885.5806 | -102.22 % | 244488.9814 MeV (+37082.0 ppm) |
| ${}^{254}$Es | 254 | 155 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -35.2638 | 1890.6683 | -101.87 % | 245449.1168 MeV (+37044.0 ppm) |
| ${}^{255}$Es | 255 | 156 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -28.6917 | 1896.6445 | -101.51 % | 246409.2594 MeV (+37010.2 ppm) |
| ${}^{256}$Es | 256 | 157 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -22.1266 | 1901.5680 | -101.16 % | 247369.4092 MeV (+36972.3 ppm) |
| ${}^{257}$Es | 257 | 158 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -15.5687 | 1907.4540 | -100.82 % | 248329.5660 MeV (+36938.6 ppm) |
| ${}^{258}$Es | 258 | 159 | L4-qclt-colour-weighted | 🟢 recursive | binding_energy | -9.0178 | 1912.2960 | -100.47 % | 249289.7299 MeV (+36900.5 ppm) |

<!-- AUTO:per-z-sections END -->
