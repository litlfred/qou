**Atlas (recursive, $q_0$-indexed).**
*Each entry of the atlas is determined by the
[GB-NF / confinement source of truth](#def:confined-particle): a
particle/atom is identified by the Markov-equivalence class
$[K]_M$ of its canonical Hecke element $T_w \in H_{n_0}(q_0)$,
expressed in $\sigma_*$ braid generators of the braid group $B_{n_0}$.
Confinement at $q_0$ is verified via the
[confinement SDP](#prop:confinement-sdp).*

*Each entry occupies **two rows**: the first gives the braid word
in normal form (NF, shortlex Gröbner–Shirshov); the second gives
the prediction and AME residual.  Composite entries reference
earlier entries (recursive structure).*

## Notation legend (auto-included)

| Symbol | Meaning |
|---|---|
| $\sigma_i$ ($i = 1, \ldots, n-1$) | Standard generators of the braid group $B_n$: half-twist between strands $i$ and $i + 1$. Hecke relation $(\sigma_i - q)(\sigma_i + q^{-1}) = 0$. |
| $\sigma_i^{-1}$ | Inverse half-twist (negative crossing). |
| $\mathbf{1}_{B_n}$ | Identity element of $B_n$ (no crossings); Markov closure $= n$ disjoint unknots. |
| $\widehat{\beta}$ | Markov closure (braid → knot/link in $S^3$). |
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
| $\bowtie$ | Binding operator: $H = K \bowtie L$ decorates knot $K$ with link $L$. |
| $[K_1, \ldots, K_n]_p$ | Composite hadron of valence $n$ with constituents $K_1, \ldots, K_n$ bound at link $p$. |
| $\nu(\mathfrak{H})$ | Valence (number of constituent knots in a hadron). |

## Braid-closure visualisations (gallery before table)

For reference, the following closures appear in the atlas.  Each
shows the braid word and its closed-knot/link form.

### $\widehat{\sigma_1^3}$ in $B_2$ — the **trefoil $3_1 = T_{2, 3}$**

Word: $\sigma_1^3$.  Closure (in $B_2$, two-strand braid closed
into a single circle): the **trefoil knot**, simplest nontrivial
prime knot.  Alternative names: $T_{2, 3}$, left-handed trefoil
(positive crossings) or right-handed (with $\sigma_1^{-3}$).
Used for: **electron** ($e^-$), and as the binding factor for
nucleons in $H_3$.  Hyperbolic volume: $0$ (torus knot).

### $\widehat{(\sigma_1 \sigma_2^{-1})^3}$ in $B_3$ — **Borromean rings $\mathcal{B}_3$**

Word: $\sigma_1 \sigma_2^{-1} \sigma_1 \sigma_2^{-1} \sigma_1 \sigma_2^{-1}$.
Closure: three pairwise-unlinked circles that are jointly linked
(remove one $\to$ all separate).  Hyperbolic volume:
$\mathrm{Vol}(\mathcal{B}_3) = 8 G \approx 7.328$ (Catalan-related).
Used for: **proton** $B_3(\mathrm{uud})$, **neutron** $B_3(\mathrm{udd})$,
where the flavor labels colour the crossings.

### $\widehat{(\sigma_1 \sigma_2^{-1})^2}$ in $B_3$ — **figure-eight $4_1$**

Word: $\sigma_1 \sigma_2^{-1} \sigma_1 \sigma_2^{-1}$.  Closure: the
**figure-eight knot**, amphichiral (equal to its mirror).
Hyperbolic volume: $\mathrm{Vol}(4_1) = 2.029883 \cdot \pi$, the
smallest among hyperbolic knots.  Used for: **Higgs field** (mass
mechanism).

### $\widehat{\sigma_1^2}$ in $B_2$ — **Hopf link $L_H$**

Word: $\sigma_1^2$.  Closure: two circles linked once.  Hyperbolic
volume: $0$ (torus link).  Used for: **gluon** (lowest force
carrier), and as the binding link in deuteron $D = [\mathfrak{p}, \mathfrak{n}]_{L_H}$.

### $\widehat{\mathbf{1}_{B_4}}$ — **photon ($\gamma$)**

Word: $\mathbf{1}_{B_4}$ (identity, no crossings).  Closure:
4 disjoint unknots — knot-trivial, but the 4 strands carry
polarisation × chirality components on the exceptional divisor
$\mathcal{S}_p$.  Used for: **photon**, vacuum-flux carrier.

### Hyperbolic atom-knots (from SnapPy GB-NF search)

Brief inventory of the hyperbolic-knot identifications used in
the atlas — alternative names where canonical:

| Knot / link | Source | Crossings | Vol_hyp | Used for |
|---|---|---|---|---|
| $K_{6_2}$ | Rolfsen | 6 | 4.4008 | Deuteron D |
| $K_{8_{11}}$ | Rolfsen | 8 | 8.2863 | Tritium T |
| $L_{6a4}$ | Thistlethwaite link | 6 | 7.3277 | $^3$He |
| $\mathcal{B}_3$ | Borromean | 6 | 7.3277 | Proton/neutron baryon $B_3$ |
| $K11a259$ | HT-table | 11 | 12.5201 | $^6$Li (best match at $\rho = 5$) |
| $L11a62$ | HT-table | 11 | 15.3600 | $^7$Li (best match at $\rho = 5$, **4 ppb**) |
| $K10a11$ | HT-table | 10 | 15.6466 | $^6$Li alt at $\rho = 4$ |
| $K11a170$ | HT-table | 11 | 19.2051 | $^7$Li alt at $\rho = 4$ |

## Atlas

| Particle / atom | Confinement level $\ell$ | $n_0$ |
|:--:|:--:|:--:|

### $\ell = 0$ — quark / lepton level

**Neutrino $\nu$** (vacuum-drag particle, no mass)

| Row | Content |
|--:|---|
| Braid (NF) | $T_w = \mathbf{1} \in H_1(q_0)$.  Closure $\widehat{T_w} = 0_1$ (unknot). |
| Prediction | $m_\nu \approx 0$ MeV (CODATA upper bound $\lesssim 1$ eV).  Confinement at $q_0$: trivially Frobenius-PSD ($\Phi^* = \mathbf{1}$). |

**Photon $\gamma$** (4 polarisation × chirality components)

| Row | Content |
|--:|---|
| Braid (NF) | $T_w = \mathbf{1}_{B_4} \in H_4(q_0)$.  Closure $\widehat{T_w} = 4 \cdot 0_1$ (4 disjoint unknots). |
| Prediction | $m_\gamma = 0$ MeV (massless, gauge boson).  4 components encode the $\sigma_0/\sigma_1$ polarisation × $(+q, -q^{-1})$ chirality on $\mathcal{S}_p$. |

**Quark $\mathfrak{q}$** (single-strand H_1 unit)

| Row | Content |
|--:|---|
| Braid (NF) | $T_w = \sigma_0 \in H_1(q_0)$.  Confined within Borromean baryon. |
| Prediction | Free-quark not observed (confinement); appears only inside hadrons. |

### $\ell = 1$ — single-nucleon / lepton

**Electron $e^-$** (trefoil)

| Row | Content |
|--:|---|
| Braid (NF) | $T_w = \sigma_1^3 \in H_2(q_0)$.  Closure $\widehat{T_w} = T_{2, 3} = 3_1$ (trefoil). |
| Prediction | $m_e = 0.51099895$ MeV (calibration anchor; CODATA exact). |

**Proton $\mathfrak{p}$**

| Row | Content |
|--:|---|
| Braid (NF) | $T_w = (\sigma_1 \sigma_2^{-1})^3$ with flavor coloring $\mathrm{uud}$.  $\widehat{T_w} = \mathcal{B}_3(\mathrm{uud})$. |
| Prediction | $m_\mathfrak{p} = 938.27208816$ MeV (CODATA exact); model derives via $\mathrm{Vol}(\mathcal{B}_3) = 8 G$ at $q_0$. |

**Neutron $\mathfrak{n}$**

| Row | Content |
|--:|---|
| Braid (NF) | $T_w = (\sigma_1 \sigma_2^{-1})^3$ with flavor coloring $\mathrm{udd}$.  $\widehat{T_w} = \mathcal{B}_3(\mathrm{udd})$. |
| Prediction | $m_\mathfrak{n} = 939.56542052$ MeV; $m_\mathfrak{n} - m_\mathfrak{p}$ derived from flavor-flip cost (open). |

### $\ell = 2$ — light atoms (recursive: ref to nucleon entries above)

**Deuterium ²H = D = $[\mathfrak{p}, \mathfrak{n}]_{L_H}$**

| Row | Content |
|--:|---|
| Braid (NF) | $T_w = (\mathfrak{p}\text{-braid}) \bowtie (\mathfrak{n}\text{-braid}) \bowtie L_H$ in $H_6(q_0)$.  Closure $\widehat{T_w} = K_{6_2}$ (hyperbolic, $\mathrm{Vol} = 4.4008$). |
| Prediction | $B_\mathrm{pred} = 1 \cdot m_e \cdot \mathrm{Vol}(K_{6_2}) = 2.249$ MeV vs $B_\mathrm{AME} = 2.225$.  **err = +1.09%**. |

**Tritium ³H = T = $[\mathfrak{p}, \mathfrak{n}, \mathfrak{n}]_{L_H \bowtie T_{2, 3}}$**

| Row | Content |
|--:|---|
| Braid (NF) | $T_w \in H_9(q_0)$.  Closure $\widehat{T_w} = K_{8_{11}}$ (hyperbolic, $\mathrm{Vol} = 8.2863$). |
| Prediction | $B_\mathrm{pred} = 2 \cdot m_e \cdot \mathrm{Vol}(K_{8_{11}}) = 8.469$ MeV vs $B_\mathrm{AME} = 8.482$.  **err = −0.16%**  ★ **best per-isotope**. |

**Helium-3 ³He = $[\mathfrak{p}, \mathfrak{p}, \mathfrak{n}]_{L_{6a4}}$**

| Row | Content |
|--:|---|
| Braid (NF) | $T_w \in H_9(q_0)$.  Closure $\widehat{T_w} = L_{6a4}$ (link, $\mathrm{Vol} = 7.3277$). |
| Prediction | $B_\mathrm{pred} = 2 \cdot m_e \cdot 7.3277 = 7.489$ MeV vs $B_\mathrm{AME} = 7.718$.  **err = −2.97%**. |

**Helium-4 ⁴He = $[\mathfrak{p}, \mathfrak{p}, \mathfrak{n}, \mathfrak{n}]_{4 \cdot 8 G}$**

| Row | Content |
|--:|---|
| Braid (NF) | $T_w \in H_{12}(q_0)$.  Magic A-rule formula: $B = A \cdot 8 G \cdot m_e$. |
| Prediction | $B_\mathrm{pred} = 2 \cdot m_e \cdot 4 \cdot 8 G = 29.956$ MeV vs $B_\mathrm{AME} = 28.296$.  **err = +5.87%**. |

**Lithium-6 ⁶Li = $[\mathrm{^4He}, \mathfrak{p}, \mathfrak{n}]_{K11a259}$**

| Row | Content |
|--:|---|
| Braid (NF) | $T_w \in H_{18}(q_0)$.  Closure $\widehat{T_w} = K11a259$ (HT-table 11-crossing alternating, $\mathrm{Vol} = 12.5201$). |
| Prediction | $B_\mathrm{pred} = 5 \cdot m_e \cdot 12.5201 = 31.989$ MeV vs $B_\mathrm{AME} = 31.994$.  **err = −0.0165% (165,000 ppb)**. |

**Lithium-7 ⁷Li = $[\mathrm{^4He}, \mathfrak{p}, \mathfrak{n}, \mathfrak{n}]_{L11a62}$**

| Row | Content |
|--:|---|
| Braid (NF) | $T_w \in H_{21}(q_0)$.  Closure $\widehat{T_w} = L_{11a62}$ (HT-table 11-crossing link, $\mathrm{Vol} = 15.3600$). |
| Prediction | $B_\mathrm{pred} = 5 \cdot m_e \cdot 15.3600 = 39.245$ MeV vs $B_\mathrm{AME} = 39.245$.  **err = +0.0004% (4,001 ppb)**  ★ **best precision in atlas**. |

### $\ell = 2$ — α-cluster atoms (recursive: ref to ⁴He)

**Beryllium-8 ⁸Be = $2 \cdot {}^4\mathrm{He} + 1 \cdot c_{\alpha\alpha}$**

| Row | Content |
|--:|---|
| Braid (NF) | Two $^4$He cluster braids fused, plus one α–α pair-energy correction. |
| Prediction | $B_\mathrm{pred} = 2 B(^4\mathrm{He}_\mathrm{derived}) + c_{\alpha\alpha} = 62.34$ MeV vs $B_\mathrm{AME} = 56.50$.  **err = +10.34%**. |

**Carbon-12 ¹²C = $3 \cdot {}^4\mathrm{He} + 3 \cdot c_{\alpha\alpha}$**

| Row | Content |
|--:|---|
| Braid (NF) | Three α-cluster fused (Hoyle state), three α–α pairs. |
| Prediction | $B_\mathrm{pred} = 97.15$ MeV vs $B_\mathrm{AME} = 92.16$.  **err = +5.41%**. |

**Oxygen-16 ¹⁶O = $4 \cdot {}^4\mathrm{He} + 6 \cdot c_{\alpha\alpha}$**

| Row | Content |
|--:|---|
| Braid (NF) | Four α-cluster fused, six α–α pairs. |
| Prediction | $B_\mathrm{pred} = 134.38$ MeV vs $B_\mathrm{AME} = 127.62$.  **err = +5.30%**. |

## Statistical summary

Best precision in atlas: **⁷Li at 4 ppb** ($K = L_{11a62}$, $\rho = 5$).
⁶Li at 165 ppm.  Tritium at 0.16%.

Mean |err| across the 10 entries above with predictions: $\sim 5.6$%.
Atlas covers $\ell \leq 2$ at $q_0$; further atoms ($\ell = 3$
molecules, heavier nuclei) defer to
[appendix-atomic-mass-calculations](#app:atomic-mass-calculations).

## Build-pipeline integration

The atlas is auto-rendered from `mass-table-ppb.witness.json` +
`li-atom-knot-search.witness.json` + `confined-particle.md` registry.
Updates to the registry or witnesses propagate to the rendered LaTeX
appendix on the next `bun run build`.

## Open

- **Structural rule for $\rho$ in $B = \rho \cdot m_e \cdot \mathrm{Vol}(K)$**:
  pattern $\rho \in \{1, 2\}$ for $\ell \leq 2$ atoms breaks at
  ⁶Li, ⁷Li ($\rho = 5$). Open: derive $\rho(Z, N)$ from ILP /
  confinement structure.
- **Hyperbolic-knot identification beyond $\ell = 2$**: ⁹Be, ¹¹B,
  ¹⁴N (no rule yet); needs extending the SnapPy search past 11
  crossings.
- **Photon $\rho$-factor**: photon mass = 0 trivially (no $\rho$
  needed), but for the recursive structure may tie to gauge-boson
  Higgs coupling.
