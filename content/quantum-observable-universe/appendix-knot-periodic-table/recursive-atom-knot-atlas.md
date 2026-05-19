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

## Methodology classification (STRICT)

Every atlas entry carries a **methodology tag**.  The atlas is split
into a *principled* section and a *quarantined / provisional* section;
volume-match results are **never** mixed with derivation-based ones.

| Tag | Definition | Examples |
|---|---|---|
| `principled-derivation` | Knot is the closure of an explicit $\sigma$-braid word in $H_{n_0}(q_0)$ from [`def:confined-particle`](#def:confined-particle); $\mathrm{Vol}_{\mathrm{hyp}}$ computed at $\geq 50$ decimal digits via `hp_volume_of_link_closure(braid_word, digits=50)`. | electron $\sigma_1^3$ → $3_1$, proton/neutron $(\sigma_1 \sigma_2^{-1})^3$ → $\mathcal{B}_3$. |
| `principled-gb-nf` | Trivial-NF entries (single strand or pure identity); closure is unknot or disjoint unknots. | neutrino, photon, quark. |
| `manual-historical-volume-match` | Knot was identified in earlier work via volume-match against AME; well-established but the GB-NF derivation in $H_{n_0}(q_0)$ has not been computed yet. | ²H = $6_2$, ³H = $8_{11}$, ³He = $L_{6a4}$. |
| `magic-A-formula` | Algebraic shell-closure formula $A \cdot 8G$ for double-magic light nuclei; no single hyperbolic knot. | ⁴He. |
| `recursive-on-⁴He` | Built from $n \cdot {}^{4}\mathrm{He} + n_{\alpha\alpha} \cdot c_{\alpha\alpha}$ recursion; principled given ⁴He. | ⁸Be–⁴⁰Ca. |
| `deprecated-volume-match` | **PROVISIONAL — do not cite as principled.**  Brute-force SnapPy volume search picked the closest knot to the AME-derived volume target; reverse-engineers the answer.  See [`methodology-deprecation.witness.json`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/methodology-deprecation.witness.json). | ⁶Li, ⁷Li (quarantined below). |

The principled pipeline computes $\mathrm{Vol}_{\mathrm{hyp}}$ from the
$\sigma$-braid word at $\geq 50$ decimal digits via SnapPy's
`Link(braid_closure=...).exterior().high_precision()` inside
`mpmath.workdps(50)`; symbolic-in-$q$ Markov-trace coefficients $y_\lambda$
are supplied by the Wenzl bridge ([`y_lambda_wenzl_bridge_extended.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/y_lambda_wenzl_bridge_extended.py)).
Volume-match search (`li_atom_knot_search.py`) is **deprecated** and
its output is consumed only in the quarantined provisional section
below.

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
Hyperbolic volume: $\mathrm{Vol}(4_1) = :val[Vol_4_1]{precision=6} \cdot \pi$, the
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

### Hyperbolic atom-knots inventory

Brief inventory of the hyperbolic-knot identifications used in
the atlas.  Methodology tag indicates how each identification was
obtained.

| Knot / link | Source | Crossings | $\mathrm{Vol}_{\mathrm{hyp}}$ | Used for | Methodology |
|---|---|---|---|---|---|
| $6_2$ | Rolfsen | 6 | 4.4008 | Deuteron $^2$H | `manual-historical-volume-match` |
| $8_{11}$ | Rolfsen | 8 | 8.2863 | Tritium $^3$H | `manual-historical-volume-match` |
| $L_{6a4}$ | Thistlethwaite link | 6 | 7.3277 | $^3$He | `manual-historical-volume-match` |
| $\mathcal{B}_3$ | Borromean | 6 | 7.3277… (hp50) | Proton/neutron $B_3$ | `principled-derivation` (closure of $(\sigma_1 \sigma_2^{-1})^3$) |
| $K_{11a259}$ | HT-table | 11 | 12.5201 | $^6$Li (volume-match at $\rho = 5$) | `deprecated-volume-match` *(deprecated)* |
| $L_{11a62}$ | HT-table | 11 | 15.3600 | $^7$Li (volume-match at $\rho = 5$) | `deprecated-volume-match` *(deprecated)* |

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

### Caveat — provisional / deprecated methodology — ⁶Li, ⁷Li

> **The two entries below are NOT principled.**  They come from a
> brute-force SnapPy volume-match search
> ([`li_atom_knot_search.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/li_atom_knot_search.py))
> which picks the knot whose hyperbolic volume matches the AME
> binding-energy target — i.e. it **reverse-engineers** the answer.
> At $\sim 2400$ knots/links searched, residuals below $\sim 10$ ppb
> are indistinguishable from numerical coincidence absent an independent
> GB-NF derivation in $H_{18}(q_0)$ / $H_{21}(q_0)$.  Listed here for
> historical transparency only.  **Do not cite these as evidence for
> the mass-table-ppb framework.**  See
> [`methodology-deprecation.witness.json`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/methodology-deprecation.witness.json)
> for the full per-particle methodology audit.

**⁶Li (PROVISIONAL — `deprecated-volume-match`)**

| Row | Content |
|--:|---|
| Methodology | `deprecated-volume-match` *(deprecated)* — no GB-NF derivation in $H_{18}(q_0)$). |
| Braid (NF) | *Not derived.*  Volume-match search at $\rho = 5$ returned closure $= K_{11a259}$ (HT-table 11-crossing alternating, $\mathrm{Vol} = 12.5201$).  No explicit $\sigma$-word in $H_{18}$ available. |
| Provisional prediction | $B_\mathrm{pred} = 5 \cdot m_e \cdot 12.5201 = 31.989$ MeV vs $B_\mathrm{AME} = 31.994$.  err $= -164{,}991$ ppb (near search noise floor). |

**⁷Li (PROVISIONAL — `deprecated-volume-match`)**

| Row | Content |
|--:|---|
| Methodology | `deprecated-volume-match` *(deprecated)* — no GB-NF derivation in $H_{21}(q_0)$). |
| Braid (NF) | *Not derived.*  Volume-match search at $\rho = 5$ returned closure $= L_{11a62}$ (HT-table 11-crossing link, $\mathrm{Vol} = 15.3600$).  No explicit $\sigma$-word in $H_{21}$ available. |
| Provisional prediction | $B_\mathrm{pred} = 5 \cdot m_e \cdot 15.3600 = 39.245$ MeV vs $B_\mathrm{AME} = 39.245$.  err $= +4{,}009$ ppb.  **Striking precision but cannot be distinguished from numerical coincidence in a $\sim 2400$-knot search absent an independent $\sigma$-word derivation.** |

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

Restricted to **principled** entries (excludes the quarantined
provisional ⁶Li / ⁷Li volume-match results):

- Tritium $^3$H at $\sim 1.6 \times 10^{-3}$ (`manual-historical`).
- Deuteron $^2$H at $\sim 1.1 \times 10^{-2}$ (`manual-historical`).
- $\alpha$-cluster atoms ⁸Be–⁴⁰Ca: mean $|\mathrm{err}| \sim 8$%
  (`recursive-on-⁴He`).

Provisional (⁶Li, ⁷Li) — **not counted in the principled summary**:

- ⁷Li: $+4{,}009$ ppb at $L_{11a62}$, $\rho = 5$ (volume-match coincidence;
  see methodology caveat above).
- ⁶Li: $-164{,}991$ ppb at $K_{11a259}$, $\rho = 5$ (search noise floor).

Atlas covers $\ell \leq 2$ at $q_0$; further atoms ($\ell = 3$
molecules, heavier nuclei) defer to
[appendix-atomic-mass-calculations](#app:atomic-mass-calculations).

## All-atoms / all-isotopes extension (2026-05-18)

A layered framework extends the atlas to every isotope (real or
theoretical) under a single registry:

| Layer | Coverage | Pipeline |
|---|---|---|
| **Layer 1** | Light isotopes ($A \leq 7$) | Canonical $\sum_\lambda y_\lambda \cdot \chi^\lambda(\beta_{\text{atom}})$ via Rust `hecke-canonical-chi` + mpmath $y_\lambda$ |
| **Layer 2** | $\alpha$-cluster magic nuclei ($A = 4 n_\alpha$) | Recursive on $^4$He + $\alpha$–$\alpha$ coupling $c_{\alpha\alpha}$ |
| **Layer 3** | Non-$\alpha$ intermediate ($5 \leq A \leq 40$) | Hybrid: nearest-$\alpha$-cluster + valence-nucleon via canonical interface |
| **Layer 4** | Heavy nuclei ($A > 40$) | Brane-tower asymptotic + LP-active-set ansatz |
| **Layer 5** | Theoretical / hypothetical isotopes | Same Layer-1/3 machinery; flagged `prediction-only` |

Per-isotope records follow the [`IsotopeRecord`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/isotope_record_schema.py)
dataclass schema with explicit knot-operator catalogue. Layer-1
pipeline implementation: [`canonical_mass_table_extended.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/canonical_mass_table_extended.py).

### Knot-operator catalogue — per-step primitives

Every per-isotope record exposes a structured list of the knot
operators used to build its canonical braid. The primitives are:

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
| $c_{\alpha\alpha}$ | $\alpha$–$\alpha$ pair-energy correction (⁸Be, ¹²C, …, ⁴⁰Ca) |
| $\alpha$–N attachment | Layer 3: $^4$He cluster + valence nucleon (for non-magic $A$) |

For an atom with mass number $A$, the canonical braid word in
$B_{3A}$ is built sequentially per nucleon: at each $k \in \{0,
\ldots, A-1\}$ apply the intra block at base $3k$ and $3k+1$,
then (for $k < A-1$) apply the inter-nucleon interface at $3k+2$
between nucleon $k$ and $k+1$. The full sequence is enumerated by
[`build_knot_operator_catalogue(Z, N)`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/isotope_record_schema.py)
and reported in every per-isotope record.

### Layer-1 canonical $|\mathrm{tr}_M(q_0)|$ table

<!-- AUTO:canonical-tr-m-table BEGIN -->

| Atom | $A$ | $n$ | $\|\mathrm{tr}_M(\beta_{\text{atom}}, q_0)\|$ | Predicting | Prediction (MeV) | Reference (MeV) | Error |
|---|---|---|---|---|---|---|---|
| $\mathfrak{p}$ | 1 | 3 | $1.0653062285923887$ | mass | 938.2719 | 938.2721 | -0.251 ppm |
| $\mathfrak{n}$ | 1 | 3 | $0.9232332971695832$ | mass | 939.5652 | 939.5654 | -0.251 ppm |
| D | 2 | 6 | $0.3882864715477129$ | B (binding) | 2.2488 | 2.2246 | +1.09 % |
| T | 3 | 9 | $0.1040521186755255$ | B (binding) | 8.4686 | 8.4818 | -0.16 % |
| ${}^3$He | 3 | 9 | $0.2065408585622623$ | B (binding) | 7.4889 | 7.7180 | -2.97 % |
| ${}^4$He | 4 | 12 | $0.0553483458766979$ | B (binding) | 29.9557 | 28.2957 | +5.87 % |
| ${}^5$Li | 5 | 15 | $0.0294413937003971$ | B (binding) | — | 26.3280 | — |
| ${}^6$Li | 6 | 18 | $0.0078896372028510$ | B (binding) | — | 31.9941 | — |

_Computed via [`canonical_mass_table_extended.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/canonical_mass_table_extended.py) (method=`markov_peel`). Witness: [`canonical-mass-table-extended.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/canonical-mass-table-extended.witness.json). Nucleon masses (m_p, m_n) via [`m-p-borromean-verification-50dps.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/m-p-borromean-verification-50dps.witness.json). Paper hard floor (CAL-2 propagation): ~780 ppb._

<!-- AUTO:canonical-tr-m-table END -->

## Build-pipeline integration

The atlas is auto-rendered by
[`recursive_atom_knot_atlas_render.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/recursive_atom_knot_atlas_render.py).

**Sources of truth** (in order):

1. [`confined-particle.md`](#def:confined-particle) — GB-NF particle registry (canonical $T_w$).
2. [`mass-table-ppb.witness.json`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/mass-table-ppb.witness.json) — D..⁴⁰Ca (manual-historical, recursive, magic-A).
3. [`methodology-deprecation.witness.json`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/methodology-deprecation.witness.json) — per-particle methodology audit.
4. [`hp_volume.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/hp_volume.py) — $\geq 50$-digit symbolic-$q$ Markov-closure $\to$ $\mathrm{Vol}_{\mathrm{hyp}}$.
5. [`y_lambda_wenzl_bridge_extended.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/y_lambda_wenzl_bridge_extended.py) — symbolic-$q$ Wenzl bridge for $y_\lambda$.

**Deprecated input** (consumed only by the quarantined provisional
section):

6. [`li-atom-knot-search.witness.json`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/li-atom-knot-search.witness.json) — *(provisional)* volume-match search.

For `principled-derivation` entries (electron, proton, neutron) the
hyperbolic volume of the Markov closure is computed from the
$\sigma$-braid word at $\geq 50$ decimal digits via
`hp_volume_of_link_closure(braid_word, digits=50)` which calls
SnapPy's `Link(braid_closure=...).exterior().high_precision()`
inside `mpmath.workdps(50)`.  Updates to any input propagate via
[`witness_staleness_tracker.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/witness_staleness_tracker.py)
to the rendered appendix on the next `bun run build`.

## Open

- **Principled derivation for ⁶Li, ⁷Li (and any new atom)**: the only
  admissible path is a **joint SDP on the full mass tower** — over all
  confinement levels $\ell$ and all atoms simultaneously — with
  **Gröbner–Shirshov filtration tracking** and **jet-order tracking**,
  yielding a canonical $T_w \in H_{n_0}(q_0)$ *per atom* as a structured
  certificate.  Status: **certificate format proof-of-concept complete**
  ([`gb_filtration_jet_tracker.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/gb_filtration_jet_tracker.py)
  + [`gb-filtration-jet-order.witness.json`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/gb-filtration-jet-order.witness.json)).
  The reducer computes filtration grade + jet-order events exactly in
  symbolic $q$ via SymPy on the test cases $\sigma_1^3$ (electron) and
  $(\sigma_1 \sigma_2^{-1})^3$ (proton/neutron body).  The joint-tower
  SDP solver consumes this certificate format; until that solver lands,
  the volume-match results stay quarantined.  The Markov closure of $T_w$ is then taken in $S^3$ and
  $\mathrm{Vol}_{\mathrm{hyp}}$ is computed at $\geq 50$ decimal digits
  via `hp_volume_of_link_closure(braid_word, digits=50)`; comparison to
  $K_{11a259}$ / $L_{11a62}$ (or whatever closure the SDP yields) happens
  *a posteriori*.  Per-atom volume-match search is FORBIDDEN as a
  derivation route — the SDP must be joint over the tower so the GB
  filtration and the jet ordering are consistent across confinement
  levels.  Until that joint SDP is run, the volume-match results stay
  quarantined.
- **Structural rule for $\rho$ in $B = \rho \cdot m_e \cdot \mathrm{Vol}(K)$**:
  pattern $\rho \in \{1, 2\}$ for $\ell \leq 2$ atoms breaks at
  ⁶Li, ⁷Li (both at $\rho = 5$ in the volume-match search).  Open:
  derive $\rho(Z, N)$ from ILP / confinement structure.
- **Hyperbolic-knot identification beyond $\ell = 2$**: ⁹Be, ¹¹B,
  ¹⁴N — no entries are in scope until a *principled* (GB-NF) derivation
  exists.  Volume-match search will not be used.
- **Photon $\rho$-factor**: photon mass $= 0$ trivially (no $\rho$
  needed), but for the recursive structure may tie to gauge-boson
  Higgs coupling.


## Per-element stability summary ($Z = 1$ to $92$)

_Merged from the legacy `knot-periodic-table-grid` block (deleted as
part of the atlas consolidation): the predicted neutron count
$N_{\mathrm{pred}}$ from the β-stability formula, the closed
$\alpha$ sub-links $k_\alpha$ (structural cluster count), and the
QOU mass $M_q$ vs. the observed AME2020 mass $M_o$. The per-Z
sections below give the full isotope chain + L1/L2/L3 layer
attribution; this section is the one-row-per-element rollup. See
[knot-periodic-table intro](#prose:knot-periodic-table) for the
mass-formula derivation and column-key conventions._

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

_1 of 1 isotopes with a framework prediction; 0 of 1 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| $\mathfrak{n}$ | 1 | 1 | L1-borromean-via-canonical | mass | 939.5652 | 939.5654 | -0.251 ppm | — |

### Hydrogen (Z = 1)

_3 of 7 isotopes with a framework prediction; 6 of 7 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| $\mathfrak{p}$ | 1 | 0 | L1-borromean-via-canonical | mass | 938.2719 | 938.2721 | -0.251 ppm | — |
| ${}^{2}$H | 2 | 1 | L1-canonical | binding_energy | 2.2488 | 2.2246 | +1.09 % | 1875.5882 MeV (-285.5 ppm) |
| ${}^{3}$H | 3 | 2 | L1-canonical | binding_energy | 8.4686 | 8.4818 | -0.16 % | 2808.9336 MeV (-177.4 ppm) |
| ${}^{4}$H | 4 | 3 | L?-pending | binding_energy | — | 6.8818 | — | 3750.0856 MeV (-136.5 ppm) |
| ${}^{5}$H | 5 | 4 | L?-pending | binding_energy | — | 6.6818 | — | 4689.8508 MeV (-109.2 ppm) |
| ${}^{6}$H | 6 | 5 | L?-pending | binding_energy | — | 5.7698 | — | 5630.3279 MeV (-91.0 ppm) |
| ${}^{7}$H | 7 | 6 | L?-pending | binding_energy | — | 6.5800 | — | 6569.0830 MeV (-77.8 ppm) |

### Helium (Z = 2)

_2 of 8 isotopes with a framework prediction; 8 of 8 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{3}$He | 3 | 1 | L1-canonical | binding_energy | 7.4889 | 7.7180 | -2.97 % | 2808.6200 MeV (-282.5 ppm) |
| ${}^{4}$He | 4 | 2 | L1-canonical | binding_energy | 29.9557 | 28.2957 | +5.87 % | 3725.7184 MeV (-719.6 ppm) |
| ${}^{5}$He | 5 | 3 | L?-pending | binding_energy | — | 27.5607 | — | 4667.6786 MeV (-219.2 ppm) |
| ${}^{6}$He | 6 | 4 | L?-pending | binding_energy | — | 29.2711 | — | 5605.5333 MeV (-182.5 ppm) |
| ${}^{7}$He | 7 | 5 | L?-pending | binding_energy | — | 28.8614 | — | 6545.5082 MeV (-156.4 ppm) |
| ${}^{8}$He | 8 | 6 | L?-pending | binding_energy | — | 31.3962 | — | 7482.5386 MeV (-136.8 ppm) |
| ${}^{9}$He | 9 | 7 | L?-pending | binding_energy | — | 30.1413 | — | 8423.3587 MeV (-121.6 ppm) |
| ${}^{10}$He | 10 | 8 | L?-pending | binding_energy | — | 29.9513 | — | 9363.1138 MeV (-109.4 ppm) |

### Lithium (Z = 3)

_2 of 11 isotopes with a framework prediction; 11 of 11 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{3}$Li | 3 | 0 | L?-pending | binding_energy | — | -6.8010 | — | 2821.6166 MeV (-542.8 ppm) |
| ${}^{4}$Li | 4 | 1 | L?-pending | binding_energy | — | 4.6150 | — | 3749.7657 MeV (-408.9 ppm) |
| ${}^{5}$Li | 5 | 2 | L?-pending | binding_energy | — | 26.3307 | — | 4667.6153 MeV (-328.6 ppm) |
| ${}^{6}$Li | 6 | 3 | L3-partial-shell:f=0.500 from A=4→8 | binding_energy | 43.6570 | 31.9940 | +36.45 % | 5589.8541 MeV (-2355.4 ppm) |
| ${}^{7}$Li | 7 | 4 | L3-partial-shell:f=0.750 from A=4→8 | binding_energy | 51.3377 | 39.2451 | +30.81 % | 6521.7386 MeV (-2085.1 ppm) |
| ${}^{8}$Li | 8 | 5 | L?-pending | binding_energy | — | 41.2777 | — | 7471.3638 MeV (-205.4 ppm) |
| ${}^{9}$Li | 9 | 6 | L?-pending | binding_energy | — | 45.3399 | — | 8406.8667 MeV (-182.6 ppm) |
| ${}^{10}$Li | 10 | 7 | L?-pending | binding_energy | — | 45.3135 | — | 9346.4583 MeV (-164.2 ppm) |
| ${}^{11}$Li | 11 | 8 | L?-pending | binding_energy | — | 45.7092 | — | 10285.6278 MeV (-149.3 ppm) |
| ${}^{12}$Li | 12 | 9 | L?-pending | binding_energy | — | 45.4992 | — | 11225.4030 MeV (-136.8 ppm) |
| ${}^{13}$Li | 13 | 10 | L?-pending | binding_energy | — | 45.5992 | — | 12164.8682 MeV (-126.3 ppm) |

### Beryllium (Z = 4)

_3 of 12 isotopes with a framework prediction; 12 of 12 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{5}$Be | 5 | 1 | L?-pending | binding_energy | — | 0.0900 | — | 4692.5626 MeV (-435.9 ppm) |
| ${}^{6}$Be | 6 | 2 | L?-pending | binding_energy | — | 26.9235 | — | 5605.2943 MeV (-364.8 ppm) |
| ${}^{7}$Be | 7 | 3 | L?-pending | binding_energy | — | 37.6008 | — | 6534.1821 MeV (-313.0 ppm) |
| ${}^{8}$Be | 8 | 4 | L2-alpha-cluster | binding_energy | 62.3383 | 56.4995 | +10.33 % | 7449.0098 MeV (-1057.4 ppm) |
| ${}^{9}$Be | 9 | 5 | L3-partial-shell:f=0.250 from A=8→12 | binding_energy | 67.3058 | 58.1640 | +15.72 % | 8383.6076 MeV (-1332.7 ppm) |
| ${}^{10}$Be | 10 | 6 | L3-partial-shell:f=0.500 from A=8→12 | binding_energy | 75.5932 | 64.9763 | +16.34 % | 9314.8854 MeV (-1357.6 ppm) |
| ${}^{11}$Be | 11 | 7 | L?-pending | binding_energy | — | 65.4779 | — | 10264.5658 MeV (-199.3 ppm) |
| ${}^{12}$Be | 12 | 8 | L?-pending | binding_energy | — | 68.6487 | — | 11200.9602 MeV (-182.7 ppm) |
| ${}^{13}$Be | 13 | 9 | L?-pending | binding_energy | — | 68.1387 | — | 12141.0354 MeV (-168.6 ppm) |
| ${}^{14}$Be | 14 | 10 | L?-pending | binding_energy | — | 69.9146 | — | 13078.8247 MeV (-156.5 ppm) |
| ${}^{15}$Be | 15 | 11 | L?-pending | binding_energy | — | 68.1146 | — | 14020.1899 MeV (-146.0 ppm) |
| ${}^{16}$Be | 16 | 12 | L?-pending | binding_energy | — | 68.5646 | — | 14959.3051 MeV (-136.9 ppm) |

### Boron (Z = 5)

_2 of 16 isotopes with a framework prediction; 16 of 16 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{6}$B | 6 | 1 | L?-pending | binding_energy | — | -2.8020 | — | 5633.7264 MeV (-453.9 ppm) |
| ${}^{7}$B | 7 | 2 | L?-pending | binding_energy | — | 24.9109 | — | 6545.5787 MeV (-390.4 ppm) |
| ${}^{8}$B | 8 | 3 | L?-pending | binding_energy | — | 37.7372 | — | 7472.3176 MeV (-342.1 ppm) |
| ${}^{9}$B | 9 | 4 | L?-pending | binding_energy | — | 56.3136 | — | 8393.3064 MeV (-304.6 ppm) |
| ${}^{10}$B | 10 | 5 | L3-partial-shell:f=0.500 from A=8→12 | binding_energy | 75.5932 | 64.7508 | +16.74 % | 9313.5920 MeV (-1436.6 ppm) |
| ${}^{11}$B | 11 | 6 | L3-partial-shell:f=0.750 from A=8→12 | binding_energy | 83.8806 | 76.2051 | +10.07 % | 10244.8698 MeV (-997.8 ppm) |
| ${}^{12}$B | 12 | 7 | L?-pending | binding_energy | — | 79.5747 | — | 11188.7409 MeV (-228.5 ppm) |
| ${}^{13}$B | 13 | 8 | L?-pending | binding_energy | — | 84.4535 | — | 12123.4273 MeV (-211.0 ppm) |
| ${}^{14}$B | 14 | 9 | L?-pending | binding_energy | — | 85.4230 | — | 13062.0229 MeV (-195.8 ppm) |
| ${}^{15}$B | 15 | 10 | L?-pending | binding_energy | — | 88.2007 | — | 13998.8105 MeV (-182.7 ppm) |
| ${}^{16}$B | 16 | 11 | L?-pending | binding_energy | — | 88.1177 | — | 14938.4586 MeV (-171.3 ppm) |
| ${}^{17}$B | 17 | 12 | L?-pending | binding_energy | — | 89.5844 | — | 15876.5571 MeV (-161.2 ppm) |
| ${}^{18}$B | 18 | 13 | L?-pending | binding_energy | — | 89.5794 | — | 16816.1273 MeV (-152.2 ppm) |
| ${}^{19}$B | 19 | 14 | L?-pending | binding_energy | — | 89.6731 | — | 17755.5988 MeV (-144.1 ppm) |
| ${}^{20}$B | 20 | 15 | L?-pending | binding_energy | — | 88.1131 | — | 18696.7240 MeV (-136.9 ppm) |
| ${}^{21}$B | 21 | 16 | L?-pending | binding_energy | — | 87.2031 | — | 19637.1992 MeV (-130.3 ppm) |

### Carbon (Z = 6)

_2 of 16 isotopes with a framework prediction; 16 of 16 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{8}$C | 8 | 2 | L?-pending | binding_energy | — | 24.8122 | — | 7483.9493 MeV (-409.7 ppm) |
| ${}^{9}$C | 9 | 3 | L?-pending | binding_energy | — | 39.0368 | — | 8409.2899 MeV (-364.7 ppm) |
| ${}^{10}$C | 10 | 4 | L?-pending | binding_energy | — | 60.3204 | — | 9327.5714 MeV (-328.8 ppm) |
| ${}^{11}$C | 11 | 5 | L?-pending | binding_energy | — | 73.4410 | — | 10254.0160 MeV (-299.2 ppm) |
| ${}^{12}$C | 12 | 6 | L2-alpha-cluster | binding_energy | 97.1480 | 92.1617 | +5.41 % | 11169.8742 MeV (-720.6 ppm) |
| ${}^{13}$C | 13 | 7 | L3-partial-shell:f=0.250 from A=12→16 | binding_energy | 101.0622 | 97.1080 | +4.07 % | 12105.5253 MeV (-579.8 ppm) |
| ${}^{14}$C | 14 | 8 | L?-pending | binding_energy | — | 105.2845 | — | 13040.8681 MeV (-235.3 ppm) |
| ${}^{15}$C | 15 | 9 | L?-pending | binding_energy | — | 106.5025 | — | 13979.2152 MeV (-219.5 ppm) |
| ${}^{16}$C | 16 | 10 | L?-pending | binding_energy | — | 110.7529 | — | 14914.5301 MeV (-205.8 ppm) |
| ${}^{17}$C | 17 | 11 | L?-pending | binding_energy | — | 111.4864 | — | 15853.3617 MeV (-193.6 ppm) |
| ${}^{18}$C | 18 | 12 | L?-pending | binding_energy | — | 115.6704 | — | 16788.7430 MeV (-182.8 ppm) |
| ${}^{19}$C | 19 | 13 | L?-pending | binding_energy | — | 116.2472 | — | 17727.7313 MeV (-173.2 ppm) |
| ${}^{20}$C | 20 | 14 | L?-pending | binding_energy | — | 119.2287 | — | 18664.3150 MeV (-164.5 ppm) |
| ${}^{21}$C | 21 | 15 | L?-pending | binding_energy | — | 119.1540 | — | 19603.9549 MeV (-156.3 ppm) |
| ${}^{22}$C | 22 | 16 | L?-pending | binding_energy | — | 119.2637 | — | 20543.4104 MeV (-149.5 ppm) |
| ${}^{23}$C | 23 | 17 | L?-pending | binding_energy | — | 116.7710 | — | 21485.4683 MeV (-142.7 ppm) |

### Nitrogen (Z = 7)

_2 of 16 isotopes with a framework prediction; 16 of 16 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{10}$N | 10 | 3 | L?-pending | binding_energy | — | 36.4367 | — | 9350.1618 MeV (-382.7 ppm) |
| ${}^{11}$N | 11 | 4 | L?-pending | binding_energy | — | 58.9424 | — | 10267.2213 MeV (-348.5 ppm) |
| ${}^{12}$N | 12 | 5 | L?-pending | binding_energy | — | 74.0413 | — | 11191.6876 MeV (-319.8 ppm) |
| ${}^{13}$N | 13 | 6 | L?-pending | binding_energy | — | 94.1052 | — | 12111.1889 MeV (-295.5 ppm) |
| ${}^{14}$N | 14 | 7 | L3-partial-shell:f=0.500 from A=12→16 | binding_energy | 109.9563 | 104.6586 | +5.06 % | 13034.9029 MeV (-680.6 ppm) |
| ${}^{15}$N | 15 | 8 | L3-partial-shell:f=0.750 from A=12→16 | binding_energy | 118.8505 | 115.4919 | +2.91 % | 13965.5740 MeV (-496.6 ppm) |
| ${}^{16}$N | 16 | 9 | L?-pending | binding_energy | — | 117.9808 | — | 14906.0089 MeV (-240.2 ppm) |
| ${}^{17}$N | 17 | 10 | L?-pending | binding_energy | — | 123.8659 | — | 15839.6889 MeV (-226.0 ppm) |
| ${}^{18}$N | 18 | 11 | L?-pending | binding_energy | — | 126.6941 | — | 16776.4259 MeV (-213.4 ppm) |
| ${}^{19}$N | 19 | 12 | L?-pending | binding_energy | — | 132.0224 | — | 17710.6628 MeV (-202.2 ppm) |
| ${}^{20}$N | 20 | 13 | L?-pending | binding_energy | — | 134.1834 | — | 18648.0669 MeV (-192.0 ppm) |
| ${}^{21}$N | 21 | 14 | L?-pending | binding_energy | — | 138.7893 | — | 19583.0262 MeV (-182.9 ppm) |
| ${}^{22}$N | 22 | 15 | L?-pending | binding_energy | — | 140.3278 | — | 20521.0530 MeV (-174.5 ppm) |
| ${}^{23}$N | 23 | 16 | L?-pending | binding_energy | — | 143.4435 | — | 21457.5025 MeV (-166.9 ppm) |
| ${}^{24}$N | 24 | 17 | L?-pending | binding_energy | — | 141.2880 | — | 22399.2231 MeV (-159.5 ppm) |
| ${}^{25}$N | 25 | 18 | L?-pending | binding_energy | — | 140.3250 | — | 23339.7513 MeV (-153.5 ppm) |

### Oxygen (Z = 8)

_3 of 18 isotopes with a framework prediction; 18 of 18 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{11}$O | 11 | 3 | L?-pending | binding_energy | — | 34.7868 | — | 10290.0836 MeV (-397.4 ppm) |
| ${}^{12}$O | 12 | 4 | L?-pending | binding_energy | — | 58.5837 | — | 11205.8519 MeV (-364.9 ppm) |
| ${}^{13}$O | 13 | 5 | L?-pending | binding_energy | — | 75.5529 | — | 12128.4478 MeV (-337.2 ppm) |
| ${}^{14}$O | 14 | 6 | L?-pending | binding_energy | — | 98.7319 | — | 13044.8340 MeV (-313.5 ppm) |
| ${}^{15}$O | 15 | 7 | L?-pending | binding_energy | — | 111.9554 | — | 13971.1757 MeV (-292.8 ppm) |
| ${}^{16}$O | 16 | 8 | L2-alpha-cluster | binding_energy | 134.3846 | 127.6193 | +5.30 % | 14888.3117 MeV (-728.7 ppm) |
| ${}^{17}$O | 17 | 9 | L3-partial-shell:f=0.250 from A=16→20 | binding_energy | 137.2455 | 131.7624 | +4.16 % | 15825.0159 MeV (-604.7 ppm) |
| ${}^{18}$O | 18 | 10 | L3-partial-shell:f=0.500 from A=16→20 | binding_energy | 146.7464 | 139.8078 | +4.96 % | 16755.0802 MeV (-657.9 ppm) |
| ${}^{19}$O | 19 | 11 | L?-pending | binding_energy | — | 143.7634 | — | 17697.6284 MeV (-231.2 ppm) |
| ${}^{20}$O | 20 | 12 | L?-pending | binding_energy | — | 151.3714 | — | 18629.5856 MeV (-219.6 ppm) |
| ${}^{21}$O | 21 | 13 | L?-pending | binding_energy | — | 155.1769 | — | 19565.3454 MeV (-209.1 ppm) |
| ${}^{22}$O | 22 | 14 | L?-pending | binding_energy | — | 162.0272 | — | 20498.0602 MeV (-199.6 ppm) |
| ${}^{23}$O | 23 | 15 | L?-pending | binding_energy | — | 164.7602 | — | 21434.8924 MeV (-190.9 ppm) |
| ${}^{24}$O | 24 | 16 | L?-pending | binding_energy | — | 168.9525 | — | 22370.2653 MeV (-183.0 ppm) |
| ${}^{25}$O | 25 | 17 | L?-pending | binding_energy | — | 168.1951 | — | 23310.5878 MeV (-175.6 ppm) |
| ${}^{26}$O | 26 | 18 | L?-pending | binding_energy | — | 168.9345 | — | 24249.4137 MeV (-168.8 ppm) |
| ${}^{27}$O | 27 | 19 | L?-pending | binding_energy | — | 166.9950 | — | 25190.9183 MeV (-162.4 ppm) |
| ${}^{28}$O | 28 | 20 | L?-pending | binding_energy | — | 167.6640 | — | 26129.8145 MeV (-156.9 ppm) |

### Fluorine (Z = 9)

_1 of 19 isotopes with a framework prediction; 19 of 19 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{13}$F | 13 | 4 | L?-pending | binding_energy | — | 55.8610 | — | 12146.8464 MeV (-379.1 ppm) |
| ${}^{14}$F | 14 | 5 | L?-pending | binding_energy | — | 73.9929 | — | 13068.2797 MeV (-352.0 ppm) |
| ${}^{15}$F | 15 | 6 | L?-pending | binding_energy | — | 97.4619 | — | 13984.3759 MeV (-329.0 ppm) |
| ${}^{16}$F | 16 | 7 | L?-pending | binding_energy | — | 111.4248 | — | 14909.9782 MeV (-308.6 ppm) |
| ${}^{17}$F | 17 | 8 | L?-pending | binding_energy | — | 128.2196 | — | 15832.7486 MeV (-290.6 ppm) |
| ${}^{18}$F | 18 | 9 | L?-pending | binding_energy | — | 137.3695 | — | 16763.1638 MeV (-274.5 ppm) |
| ${}^{19}$F | 19 | 10 | L3-partial-shell:f=0.750 from A=16→20 | binding_energy | 156.2474 | 147.8014 | +5.71 % | 17683.8512 MeV (-737.4 ppm) |
| ${}^{20}$F | 20 | 11 | L?-pending | binding_energy | — | 154.4027 | — | 18625.2610 MeV (-247.1 ppm) |
| ${}^{21}$F | 21 | 12 | L?-pending | binding_energy | — | 162.5042 | — | 19556.7247 MeV (-235.4 ppm) |
| ${}^{22}$F | 22 | 13 | L?-pending | binding_energy | — | 167.7345 | — | 20491.0596 MeV (-224.6 ppm) |
| ${}^{23}$F | 23 | 14 | L?-pending | binding_energy | — | 175.3139 | — | 21423.0453 MeV (-214.9 ppm) |
| ${}^{24}$F | 24 | 15 | L?-pending | binding_energy | — | 179.1260 | — | 22358.7984 MeV (-205.9 ppm) |
| ${}^{25}$F | 25 | 16 | L?-pending | binding_energy | — | 183.4077 | — | 23294.0820 MeV (-197.6 ppm) |
| ${}^{26}$F | 26 | 17 | L?-pending | binding_energy | — | 184.1385 | — | 24232.9163 MeV (-190.0 ppm) |
| ${}^{27}$F | 27 | 18 | L?-pending | binding_energy | — | 185.7510 | — | 25170.8690 MeV (-182.9 ppm) |
| ${}^{28}$F | 28 | 19 | L?-pending | binding_energy | — | 185.5520 | — | 26110.6332 MeV (-176.4 ppm) |
| ${}^{29}$F | 29 | 20 | L?-pending | binding_energy | — | 186.8769 | — | 27048.8735 MeV (-170.2 ppm) |
| ${}^{30}$F | 30 | 21 | L?-pending | binding_energy | — | 186.1500 | — | 27989.1656 MeV (-165.0 ppm) |
| ${}^{31}$F | 31 | 22 | L?-pending | binding_energy | — | 186.3410 | — | 28928.5397 MeV (-159.7 ppm) |

### Neon (Z = 10)

_3 of 20 isotopes with a framework prediction; 20 of 20 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{15}$Ne | 15 | 5 | L?-pending | binding_energy | — | 73.0309 | — | 14007.5135 MeV (-364.9 ppm) |
| ${}^{16}$Ne | 16 | 6 | L?-pending | binding_energy | — | 97.3308 | — | 14922.7788 MeV (-342.6 ppm) |
| ${}^{17}$Ne | 17 | 7 | L?-pending | binding_energy | — | 112.8885 | — | 15846.7863 MeV (-322.6 ppm) |
| ${}^{18}$Ne | 18 | 8 | L?-pending | binding_energy | — | 132.1426 | — | 16767.0974 MeV (-304.9 ppm) |
| ${}^{19}$Ne | 19 | 9 | L?-pending | binding_energy | — | 143.7795 | — | 17695.0257 MeV (-288.9 ppm) |
| ${}^{20}$Ne | 20 | 10 | L2-alpha-cluster | binding_energy | 174.0483 | 160.6448 | +8.34 % | 18604.3221 MeV (-994.4 ppm) |
| ${}^{21}$Ne | 21 | 11 | L3-partial-shell:f=0.250 from A=20→24 | binding_energy | 175.8559 | 167.4060 | +5.05 % | 19542.0796 MeV (-693.6 ppm) |
| ${}^{22}$Ne | 22 | 12 | L3-partial-shell:f=0.500 from A=20→24 | binding_energy | 185.9636 | 177.7702 | +4.61 % | 20471.5372 MeV (-649.7 ppm) |
| ${}^{23}$Ne | 23 | 13 | L?-pending | binding_energy | — | 182.9709 | — | 21414.0950 MeV (-238.8 ppm) |
| ${}^{24}$Ne | 24 | 14 | L?-pending | binding_energy | — | 191.8398 | — | 22344.7913 MeV (-228.9 ppm) |
| ${}^{25}$Ne | 25 | 15 | L?-pending | binding_energy | — | 195.9950 | — | 23280.2013 MeV (-219.7 ppm) |
| ${}^{26}$Ne | 26 | 16 | L?-pending | binding_energy | — | 201.5497 | — | 24214.2118 MeV (-211.2 ppm) |
| ${}^{27}$Ne | 27 | 17 | L?-pending | binding_energy | — | 203.0512 | — | 25152.2755 MeV (-203.4 ppm) |
| ${}^{28}$Ne | 28 | 18 | L?-pending | binding_energy | — | 206.8737 | — | 26088.0182 MeV (-196.1 ppm) |
| ${}^{29}$Ne | 29 | 19 | L?-pending | binding_energy | — | 207.8450 | — | 27026.6121 MeV (-189.3 ppm) |
| ${}^{30}$Ne | 30 | 20 | L?-pending | binding_energy | — | 211.0360 | — | 27962.9863 MeV (-183.0 ppm) |
| ${}^{31}$Ne | 31 | 21 | L?-pending | binding_energy | — | 211.2058 | — | 28902.3816 MeV (-177.0 ppm) |
| ${}^{32}$Ne | 32 | 22 | L?-pending | binding_energy | — | 213.4720 | — | 29839.6806 MeV (-171.9 ppm) |
| ${}^{33}$Ne | 33 | 23 | L?-pending | binding_energy | — | 212.3880 | — | 30780.3298 MeV (-165.9 ppm) |
| ${}^{34}$Ne | 34 | 24 | L?-pending | binding_energy | — | 213.7580 | — | 31718.5250 MeV (-161.3 ppm) |

### Fermium (Z = 100)

_0 of 20 isotopes with a framework prediction; 20 of 20 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{241}$Fm | 241 | 141 | L?-pending | binding_energy | — | 1797.6190 | — | 224508.2573 MeV (-227.3 ppm) |
| ${}^{242}$Fm | 242 | 142 | L?-pending | binding_energy | — | 1806.5300 | — | 225438.9115 MeV (-226.4 ppm) |
| ${}^{243}$Fm | 243 | 143 | L?-pending | binding_energy | — | 1813.7520 | — | 226371.2547 MeV (-225.8 ppm) |
| ${}^{244}$Fm | 244 | 144 | L?-pending | binding_energy | — | 1822.1920 | — | 227302.3799 MeV (-225.0 ppm) |
| ${}^{245}$Fm | 245 | 145 | L?-pending | binding_energy | — | 1828.9250 | — | 228235.2120 MeV (-223.6 ppm) |
| ${}^{246}$Fm | 246 | 146 | L?-pending | binding_energy | — | 1837.1184 | — | 229166.5839 MeV (-223.2 ppm) |
| ${}^{247}$Fm | 247 | 147 | L?-pending | binding_energy | — | 1843.6080 | — | 230099.6594 MeV (-221.8 ppm) |
| ${}^{248}$Fm | 248 | 148 | L?-pending | binding_energy | — | 1851.5544 | — | 231031.2782 MeV (-221.4 ppm) |
| ${}^{249}$Fm | 249 | 149 | L?-pending | binding_energy | — | 1858.0044 | — | 231964.3934 MeV (-220.5 ppm) |
| ${}^{250}$Fm | 250 | 150 | L?-pending | binding_energy | — | 1865.5226 | — | 232896.4403 MeV (-219.6 ppm) |
| ${}^{251}$Fm | 251 | 151 | L?-pending | binding_energy | — | 1871.7073 | — | 233829.8208 MeV (-218.7 ppm) |
| ${}^{252}$Fm | 252 | 152 | L?-pending | binding_energy | — | 1878.9208 | — | 234762.1725 MeV (-217.9 ppm) |
| ${}^{253}$Fm | 253 | 153 | L?-pending | binding_energy | — | 1884.4632 | — | 235696.1953 MeV (-217.0 ppm) |
| ${}^{254}$Fm | 254 | 154 | L?-pending | binding_energy | — | 1890.9776 | — | 236629.2461 MeV (-216.1 ppm) |
| ${}^{255}$Fm | 255 | 155 | L?-pending | binding_energy | — | 1896.1509 | — | 237563.6380 MeV (-215.3 ppm) |
| ${}^{256}$Fm | 256 | 156 | L?-pending | binding_energy | — | 1902.5379 | — | 238496.8161 MeV (-214.5 ppm) |
| ${}^{257}$Fm | 257 | 157 | L?-pending | binding_energy | — | 1907.5039 | — | 239431.4153 MeV (-213.6 ppm) |
| ${}^{258}$Fm | 258 | 158 | L?-pending | binding_energy | — | 1913.8440 | — | 240364.6404 MeV (-213.2 ppm) |
| ${}^{259}$Fm | 259 | 159 | L?-pending | binding_energy | — | 1918.4130 | — | 241299.6366 MeV (-211.5 ppm) |
| ${}^{260}$Fm | 260 | 160 | L?-pending | binding_energy | — | 1924.5200 | — | 242233.0948 MeV (-211.1 ppm) |

### Mendelevium (Z = 101)

_0 of 19 isotopes with a framework prediction; 19 of 19 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{244}$Md | 244 | 143 | L?-pending | binding_energy | — | 1814.8720 | — | 227308.4065 MeV (-227.6 ppm) |
| ${}^{245}$Md | 245 | 144 | L?-pending | binding_energy | — | 1823.0450 | — | 228239.7987 MeV (-225.9 ppm) |
| ${}^{246}$Md | 246 | 145 | L?-pending | binding_energy | — | 1830.4860 | — | 229171.9229 MeV (-225.7 ppm) |
| ${}^{247}$Md | 247 | 146 | L?-pending | binding_energy | — | 1838.6680 | — | 230103.3061 MeV (-224.5 ppm) |
| ${}^{248}$Md | 248 | 147 | L?-pending | binding_energy | — | 1845.6160 | — | 231035.9233 MeV (-223.1 ppm) |
| ${}^{249}$Md | 249 | 148 | L?-pending | binding_energy | — | 1853.5602 | — | 231967.5442 MeV (-222.7 ppm) |
| ${}^{250}$Md | 250 | 149 | L?-pending | binding_energy | — | 1860.4133 | — | 232900.2563 MeV (-221.8 ppm) |
| ${}^{251}$Md | 251 | 150 | L?-pending | binding_energy | — | 1867.9170 | — | 233832.3178 MeV (-220.9 ppm) |
| ${}^{252}$Md | 252 | 151 | L?-pending | binding_energy | — | 1874.4880 | — | 234765.3120 MeV (-220.0 ppm) |
| ${}^{253}$Md | 253 | 152 | L?-pending | binding_energy | — | 1881.8140 | — | 235697.5512 MeV (-219.0 ppm) |
| ${}^{254}$Md | 254 | 153 | L?-pending | binding_energy | — | 1887.7280 | — | 236631.2024 MeV (-218.7 ppm) |
| ${}^{255}$Md | 255 | 154 | L?-pending | binding_energy | — | 1894.3270 | — | 237564.1686 MeV (-217.5 ppm) |
| ${}^{256}$Md | 256 | 155 | L?-pending | binding_energy | — | 1899.7760 | — | 238498.2847 MeV (-216.6 ppm) |
| ${}^{257}$Md | 257 | 156 | L?-pending | binding_energy | — | 1906.3192 | — | 239431.3067 MeV (-215.8 ppm) |
| ${}^{258}$Md | 258 | 157 | L?-pending | binding_energy | — | 1911.6927 | — | 240365.4984 MeV (-214.9 ppm) |
| ${}^{259}$Md | 259 | 158 | L?-pending | binding_energy | — | 1917.8950 | — | 241298.8613 MeV (-214.1 ppm) |
| ${}^{260}$Md | 260 | 159 | L?-pending | binding_energy | — | 1922.9600 | — | 242233.3615 MeV (-213.2 ppm) |
| ${}^{261}$Md | 261 | 160 | L?-pending | binding_energy | — | 1929.0510 | — | 243166.8357 MeV (-212.6 ppm) |
| ${}^{262}$Md | 262 | 161 | L?-pending | binding_energy | — | 1934.0840 | — | 244101.3678 MeV (-212.0 ppm) |

### Nobelium (Z = 102)

_0 of 17 isotopes with a framework prediction; 17 of 17 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{248}$No | 248 | 146 | L?-pending | binding_energy | — | 1841.1520 | — | 231039.0939 MeV (-225.6 ppm) |
| ${}^{249}$No | 249 | 147 | L?-pending | binding_energy | — | 1848.0780 | — | 231971.7331 MeV (-224.5 ppm) |
| ${}^{250}$No | 250 | 148 | L?-pending | binding_energy | — | 1856.5000 | — | 232902.8763 MeV (-224.1 ppm) |
| ${}^{251}$No | 251 | 149 | L?-pending | binding_energy | — | 1863.1730 | — | 233835.7685 MeV (-222.8 ppm) |
| ${}^{252}$No | 252 | 150 | L?-pending | binding_energy | — | 1871.3014 | — | 234767.2053 MeV (-222.2 ppm) |
| ${}^{253}$No | 253 | 151 | L?-pending | binding_energy | — | 1877.8854 | — | 235700.1865 MeV (-221.3 ppm) |
| ${}^{254}$No | 254 | 152 | L?-pending | binding_energy | — | 1885.5921 | — | 236632.0449 MeV (-220.5 ppm) |
| ${}^{255}$No | 255 | 153 | L?-pending | binding_energy | — | 1891.5748 | — | 237565.6274 MeV (-219.6 ppm) |
| ${}^{256}$No | 256 | 154 | L?-pending | binding_energy | — | 1898.6350 | — | 238498.1324 MeV (-218.7 ppm) |
| ${}^{257}$No | 257 | 155 | L?-pending | binding_energy | — | 1904.2823 | — | 239432.0503 MeV (-217.9 ppm) |
| ${}^{258}$No | 258 | 156 | L?-pending | binding_energy | — | 1911.0060 | — | 240364.8918 MeV (-216.6 ppm) |
| ${}^{259}$No | 259 | 157 | L?-pending | binding_energy | — | 1916.5926 | — | 241298.8704 MeV (-216.2 ppm) |
| ${}^{260}$No | 260 | 158 | L?-pending | binding_energy | — | 1923.2200 | — | 242231.8081 MeV (-215.7 ppm) |
| ${}^{261}$No | 261 | 159 | L?-pending | binding_energy | — | 1928.2680 | — | 243166.3253 MeV (-214.2 ppm) |
| ${}^{262}$No | 262 | 160 | L?-pending | binding_energy | — | 1934.8700 | — | 244099.2885 MeV (-214.1 ppm) |
| ${}^{263}$No | 263 | 161 | L?-pending | binding_energy | — | 1939.8880 | — | 245033.8357 MeV (-213.2 ppm) |
| ${}^{264}$No | 264 | 162 | L?-pending | binding_energy | — | 1945.9440 | — | 245967.3449 MeV (-211.8 ppm) |

### Lawrencium (Z = 103)

_0 of 16 isotopes with a framework prediction; 16 of 16 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{251}$Lr | 251 | 148 | L?-pending | binding_energy | — | 1857.4000 | — | 233840.2482 MeV (-224.9 ppm) |
| ${}^{252}$Lr | 252 | 149 | L?-pending | binding_energy | — | 1864.8000 | — | 234772.4133 MeV (-224.2 ppm) |
| ${}^{253}$Lr | 253 | 150 | L?-pending | binding_energy | — | 1872.9383 | — | 235703.8403 MeV (-223.5 ppm) |
| ${}^{254}$Lr | 254 | 151 | L?-pending | binding_energy | — | 1879.8872 | — | 236636.4565 MeV (-222.6 ppm) |
| ${}^{255}$Lr | 255 | 152 | L?-pending | binding_energy | — | 1887.6571 | — | 237568.2518 MeV (-221.7 ppm) |
| ${}^{256}$Lr | 256 | 153 | L?-pending | binding_energy | — | 1893.9291 | — | 238501.5450 MeV (-220.9 ppm) |
| ${}^{257}$Lr | 257 | 154 | L?-pending | binding_energy | — | 1901.0290 | — | 239434.0103 MeV (-219.8 ppm) |
| ${}^{258}$Lr | 258 | 155 | L?-pending | binding_energy | — | 1907.1360 | — | 240367.4684 MeV (-219.6 ppm) |
| ${}^{259}$Lr | 259 | 156 | L?-pending | binding_energy | — | 1914.0100 | — | 241300.1596 MeV (-218.2 ppm) |
| ${}^{260}$Lr | 260 | 157 | L?-pending | binding_energy | — | 1919.5800 | — | 242234.1548 MeV (-217.0 ppm) |
| ${}^{261}$Lr | 261 | 158 | L?-pending | binding_energy | — | 1926.4410 | — | 243166.8590 MeV (-216.5 ppm) |
| ${}^{262}$Lr | 262 | 159 | L?-pending | binding_energy | — | 1931.9880 | — | 244100.8772 MeV (-215.8 ppm) |
| ${}^{263}$Lr | 263 | 160 | L?-pending | binding_energy | — | 1938.5730 | — | 245033.8574 MeV (-215.3 ppm) |
| ${}^{264}$Lr | 264 | 161 | L?-pending | binding_energy | — | 1943.8320 | — | 245968.1636 MeV (-214.0 ppm) |
| ${}^{265}$Lr | 265 | 162 | L?-pending | binding_energy | — | 1950.1350 | — | 246901.4257 MeV (-213.6 ppm) |
| ${}^{266}$Lr | 266 | 163 | L?-pending | binding_energy | — | 1954.8340 | — | 247836.2919 MeV (-213.0 ppm) |

### Rutherfordium (Z = 104)

_0 of 16 isotopes with a framework prediction; 16 of 16 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{253}$Rf | 253 | 149 | L?-pending | binding_energy | — | 1867.1400 | — | 235708.3452 MeV (-226.1 ppm) |
| ${}^{254}$Rf | 254 | 150 | L?-pending | binding_energy | — | 1875.5360 | — | 236639.5144 MeV (-224.7 ppm) |
| ${}^{255}$Rf | 255 | 151 | L?-pending | binding_energy | — | 1882.4100 | — | 237572.2056 MeV (-223.5 ppm) |
| ${}^{256}$Rf | 256 | 152 | L?-pending | binding_energy | — | 1890.6713 | — | 238503.5094 MeV (-223.0 ppm) |
| ${}^{257}$Rf | 257 | 153 | L?-pending | binding_energy | — | 1897.0983 | — | 239436.6477 MeV (-222.2 ppm) |
| ${}^{258}$Rf | 258 | 154 | L?-pending | binding_energy | — | 1904.6916 | — | 240368.6195 MeV (-221.3 ppm) |
| ${}^{259}$Rf | 259 | 155 | L?-pending | binding_energy | — | 1910.6430 | — | 241302.2333 MeV (-220.0 ppm) |
| ${}^{260}$Rf | 260 | 156 | L?-pending | binding_energy | — | 1918.0200 | — | 242234.4215 MeV (-219.5 ppm) |
| ${}^{261}$Rf | 261 | 157 | L?-pending | binding_energy | — | 1923.9317 | — | 243168.0750 MeV (-218.7 ppm) |
| ${}^{262}$Rf | 262 | 158 | L?-pending | binding_energy | — | 1930.9400 | — | 244100.6319 MeV (-218.0 ppm) |
| ${}^{263}$Rf | 263 | 159 | L?-pending | binding_energy | — | 1936.7320 | — | 245034.4050 MeV (-217.5 ppm) |
| ${}^{264}$Rf | 264 | 160 | L?-pending | binding_energy | — | 1943.3040 | — | 245967.3982 MeV (-215.9 ppm) |
| ${}^{265}$Rf | 265 | 161 | L?-pending | binding_energy | — | 1948.8100 | — | 246901.4574 MeV (-215.3 ppm) |
| ${}^{266}$Rf | 266 | 162 | L?-pending | binding_energy | — | 1955.3660 | — | 247834.4666 MeV (-214.2 ppm) |
| ${}^{267}$Rf | 267 | 163 | L?-pending | binding_energy | — | 1960.3140 | — | 248769.0838 MeV (-214.2 ppm) |
| ${}^{268}$Rf | 268 | 164 | L?-pending | binding_energy | — | 1966.3160 | — | 249702.6470 MeV (-213.2 ppm) |

### Dubnium (Z = 105)

_0 of 16 isotopes with a framework prediction; 16 of 16 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{255}$Db | 255 | 150 | L?-pending | binding_energy | — | 1876.5450 | — | 237576.7772 MeV (-226.5 ppm) |
| ${}^{256}$Db | 256 | 151 | L?-pending | binding_energy | — | 1883.9040 | — | 238508.9834 MeV (-225.5 ppm) |
| ${}^{257}$Db | 257 | 152 | L?-pending | binding_energy | — | 1892.0280 | — | 239440.4246 MeV (-224.3 ppm) |
| ${}^{258}$Db | 258 | 153 | L?-pending | binding_energy | — | 1898.7459 | — | 240373.2719 MeV (-223.4 ppm) |
| ${}^{259}$Db | 259 | 154 | L?-pending | binding_energy | — | 1906.3339 | — | 241305.2491 MeV (-222.6 ppm) |
| ${}^{260}$Db | 260 | 155 | L?-pending | binding_energy | — | 1912.8200 | — | 242238.3282 MeV (-222.1 ppm) |
| ${}^{261}$Db | 261 | 156 | L?-pending | binding_energy | — | 1920.1770 | — | 243170.5363 MeV (-220.9 ppm) |
| ${}^{262}$Db | 262 | 157 | L?-pending | binding_energy | — | 1926.2240 | — | 244104.0545 MeV (-219.7 ppm) |
| ${}^{263}$Db | 263 | 158 | L?-pending | binding_energy | — | 1933.5760 | — | 245036.2677 MeV (-219.5 ppm) |
| ${}^{264}$Db | 264 | 159 | L?-pending | binding_energy | — | 1939.3440 | — | 245970.0649 MeV (-218.0 ppm) |
| ${}^{265}$Db | 265 | 160 | L?-pending | binding_energy | — | 1946.4250 | — | 246902.5491 MeV (-217.7 ppm) |
| ${}^{266}$Db | 266 | 161 | L?-pending | binding_energy | — | 1952.1740 | — | 247836.3653 MeV (-217.1 ppm) |
| ${}^{267}$Db | 267 | 162 | L?-pending | binding_energy | — | 1958.9790 | — | 248769.1254 MeV (-216.3 ppm) |
| ${}^{268}$Db | 268 | 163 | L?-pending | binding_energy | — | 1963.9040 | — | 249703.7656 MeV (-215.1 ppm) |
| ${}^{269}$Db | 269 | 164 | L?-pending | binding_energy | — | 1969.8870 | — | 250637.3478 MeV (-214.3 ppm) |
| ${}^{270}$Db | 270 | 165 | L?-pending | binding_energy | — | 1974.7800 | — | 251572.0200 MeV (-213.8 ppm) |

### Seaborgium (Z = 106)

_0 of 16 isotopes with a framework prediction; 16 of 16 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{258}$Sg | 258 | 152 | L?-pending | binding_energy | — | 1894.2360 | — | 240376.4884 MeV (-225.8 ppm) |
| ${}^{259}$Sg | 259 | 153 | L?-pending | binding_energy | — | 1901.0600 | — | 241309.2296 MeV (-224.8 ppm) |
| ${}^{260}$Sg | 260 | 154 | L?-pending | binding_energy | — | 1909.0664 | — | 242240.7884 MeV (-223.8 ppm) |
| ${}^{261}$Sg | 261 | 155 | L?-pending | binding_energy | — | 1915.6802 | — | 243173.7398 MeV (-222.9 ppm) |
| ${}^{262}$Sg | 262 | 156 | L?-pending | binding_energy | — | 1923.3875 | — | 244105.5977 MeV (-222.1 ppm) |
| ${}^{263}$Sg | 263 | 157 | L?-pending | binding_energy | — | 1929.6310 | — | 245038.9194 MeV (-221.2 ppm) |
| ${}^{264}$Sg | 264 | 158 | L?-pending | binding_energy | — | 1937.2320 | — | 245970.8836 MeV (-220.9 ppm) |
| ${}^{265}$Sg | 265 | 159 | L?-pending | binding_energy | — | 1943.2450 | — | 246904.4357 MeV (-219.9 ppm) |
| ${}^{266}$Sg | 266 | 160 | L?-pending | binding_energy | — | 1950.3120 | — | 247836.9339 MeV (-218.3 ppm) |
| ${}^{267}$Sg | 267 | 161 | L?-pending | binding_energy | — | 1956.3090 | — | 248770.5021 MeV (-217.9 ppm) |
| ${}^{268}$Sg | 268 | 162 | L?-pending | binding_energy | — | 1963.3680 | — | 249703.0083 MeV (-217.1 ppm) |
| ${}^{269}$Sg | 269 | 163 | L?-pending | binding_energy | — | 1968.5420 | — | 250637.3995 MeV (-216.2 ppm) |
| ${}^{270}$Sg | 270 | 164 | L?-pending | binding_energy | — | 1974.7800 | — | 251570.7267 MeV (-215.1 ppm) |
| ${}^{271}$Sg | 271 | 165 | L?-pending | binding_energy | — | 1979.6550 | — | 252505.4168 MeV (-214.2 ppm) |
| ${}^{272}$Sg | 272 | 166 | L?-pending | binding_energy | — | 1985.8720 | — | 253438.7650 MeV (-213.6 ppm) |
| ${}^{273}$Sg | 273 | 167 | L?-pending | binding_energy | — | 1990.7160 | — | 254373.4862 MeV (-213.5 ppm) |

### Bohrium (Z = 107)

_0 of 19 isotopes with a framework prediction; 19 of 19 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{260}$Bh | 260 | 153 | L?-pending | binding_energy | — | 1901.6400 | — | 242246.9215 MeV (-225.6 ppm) |
| ${}^{261}$Bh | 261 | 154 | L?-pending | binding_energy | — | 1909.8235 | — | 243178.3032 MeV (-225.0 ppm) |
| ${}^{262}$Bh | 262 | 155 | L?-pending | binding_energy | — | 1916.7221 | — | 244110.9698 MeV (-224.2 ppm) |
| ${}^{263}$Bh | 263 | 156 | L?-pending | binding_energy | — | 1924.6340 | — | 245042.6230 MeV (-223.7 ppm) |
| ${}^{264}$Bh | 264 | 157 | L?-pending | binding_energy | — | 1931.1600 | — | 245975.6622 MeV (-222.5 ppm) |
| ${}^{265}$Bh | 265 | 158 | L?-pending | binding_energy | — | 1938.7400 | — | 246907.6474 MeV (-221.4 ppm) |
| ${}^{266}$Bh | 266 | 159 | L?-pending | binding_energy | — | 1945.2580 | — | 247840.6946 MeV (-221.2 ppm) |
| ${}^{267}$Bh | 267 | 160 | L?-pending | binding_energy | — | 1952.5710 | — | 248772.9468 MeV (-220.0 ppm) |
| ${}^{268}$Bh | 268 | 161 | L?-pending | binding_energy | — | 1958.8120 | — | 249706.2710 MeV (-219.6 ppm) |
| ${}^{269}$Bh | 269 | 162 | L?-pending | binding_energy | — | 1966.1210 | — | 250638.5271 MeV (-218.8 ppm) |
| ${}^{270}$Bh | 270 | 163 | L?-pending | binding_energy | — | 1971.2700 | — | 251572.9433 MeV (-217.4 ppm) |
| ${}^{271}$Bh | 271 | 164 | L?-pending | binding_energy | — | 1977.7580 | — | 252506.0205 MeV (-216.7 ppm) |
| ${}^{272}$Bh | 272 | 165 | L?-pending | binding_energy | — | 1982.8800 | — | 253440.4637 MeV (-215.9 ppm) |
| ${}^{273}$Bh | 273 | 166 | L?-pending | binding_energy | — | 1989.0780 | — | 254373.8309 MeV (-215.2 ppm) |
| ${}^{274}$Bh | 274 | 167 | L?-pending | binding_energy | — | 1994.1720 | — | 255308.3021 MeV (-214.8 ppm) |
| ${}^{275}$Bh | 275 | 168 | L?-pending | binding_energy | — | 2000.0750 | — | 256241.9643 MeV (-213.4 ppm) |
| ${}^{276}$Bh | 276 | 169 | L?-pending | binding_energy | — | 2005.1400 | — | 257176.4644 MeV (-213.3 ppm) |
| ${}^{277}$Bh | 277 | 170 | L?-pending | binding_energy | — | 2011.0200 | — | 258110.1496 MeV (-212.3 ppm) |
| ${}^{278}$Bh | 278 | 171 | L?-pending | binding_energy | — | 2015.7780 | — | 259044.9568 MeV (-211.4 ppm) |

### Hassium (Z = 108)

_0 of 18 isotopes with a framework prediction; 18 of 18 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{263}$Hs | 263 | 155 | L?-pending | binding_energy | — | 1918.5850 | — | 245047.3787 MeV (-225.4 ppm) |
| ${}^{264}$Hs | 264 | 156 | L?-pending | binding_energy | — | 1926.7713 | — | 245978.7576 MeV (-224.6 ppm) |
| ${}^{265}$Hs | 265 | 157 | L?-pending | binding_energy | — | 1933.5056 | — | 246911.5885 MeV (-223.7 ppm) |
| ${}^{266}$Hs | 266 | 158 | L?-pending | binding_energy | — | 1941.3375 | — | 247843.3218 MeV (-222.9 ppm) |
| ${}^{267}$Hs | 267 | 159 | L?-pending | binding_energy | — | 1947.7650 | — | 248776.4594 MeV (-221.5 ppm) |
| ${}^{268}$Hs | 268 | 160 | L?-pending | binding_energy | — | 1955.5960 | — | 249708.1936 MeV (-221.0 ppm) |
| ${}^{269}$Hs | 269 | 161 | L?-pending | binding_energy | — | 1962.0860 | — | 250641.2688 MeV (-219.9 ppm) |
| ${}^{270}$Hs | 270 | 162 | L?-pending | binding_energy | — | 1969.6500 | — | 251573.2700 MeV (-219.6 ppm) |
| ${}^{271}$Hs | 271 | 163 | L?-pending | binding_energy | — | 1975.0480 | — | 252507.4372 MeV (-218.4 ppm) |
| ${}^{272}$Hs | 272 | 164 | L?-pending | binding_energy | — | 1981.7920 | — | 253440.2584 MeV (-217.5 ppm) |
| ${}^{273}$Hs | 273 | 165 | L?-pending | binding_energy | — | 1987.1670 | — | 254374.4486 MeV (-217.0 ppm) |
| ${}^{274}$Hs | 274 | 166 | L?-pending | binding_energy | — | 1993.6240 | — | 255307.5567 MeV (-216.3 ppm) |
| ${}^{275}$Hs | 275 | 167 | L?-pending | binding_energy | — | 1998.7000 | — | 256242.0459 MeV (-215.9 ppm) |
| ${}^{276}$Hs | 276 | 168 | L?-pending | binding_energy | — | 2005.1400 | — | 257175.1711 MeV (-215.3 ppm) |
| ${}^{277}$Hs | 277 | 169 | L?-pending | binding_energy | — | 2009.9120 | — | 258109.9643 MeV (-214.1 ppm) |
| ${}^{278}$Hs | 278 | 170 | L?-pending | binding_energy | — | 2016.0560 | — | 259043.3855 MeV (-213.0 ppm) |
| ${}^{279}$Hs | 279 | 171 | L?-pending | binding_energy | — | 2020.7970 | — | 259978.2097 MeV (-212.1 ppm) |
| ${}^{280}$Hs | 280 | 172 | L?-pending | binding_energy | — | 2026.9200 | — | 260911.6518 MeV (-211.2 ppm) |

### Meitnerium (Z = 109)

_0 of 18 isotopes with a framework prediction; 18 of 18 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{265}$Mt | 265 | 156 | L?-pending | binding_energy | — | 1927.0800 | — | 246916.7207 MeV (-226.1 ppm) |
| ${}^{266}$Mt | 266 | 157 | L?-pending | binding_energy | — | 1934.0221 | — | 247849.3438 MeV (-224.9 ppm) |
| ${}^{267}$Mt | 267 | 158 | L?-pending | binding_energy | — | 1941.8910 | — | 248781.0401 MeV (-223.7 ppm) |
| ${}^{268}$Mt | 268 | 159 | L?-pending | binding_energy | — | 1948.6280 | — | 249713.8683 MeV (-223.0 ppm) |
| ${}^{269}$Mt | 269 | 160 | L?-pending | binding_energy | — | 1956.7060 | — | 250645.3555 MeV (-222.8 ppm) |
| ${}^{270}$Mt | 270 | 161 | L?-pending | binding_energy | — | 1963.1700 | — | 251578.4567 MeV (-221.2 ppm) |
| ${}^{271}$Mt | 271 | 162 | L?-pending | binding_energy | — | 1970.9830 | — | 252510.2089 MeV (-220.9 ppm) |
| ${}^{272}$Mt | 272 | 163 | L?-pending | binding_energy | — | 1976.6240 | — | 253444.1330 MeV (-219.9 ppm) |
| ${}^{273}$Mt | 273 | 164 | L?-pending | binding_energy | — | 1983.3450 | — | 254376.9772 MeV (-218.9 ppm) |
| ${}^{274}$Mt | 274 | 165 | L?-pending | binding_energy | — | 1988.9660 | — | 255310.9214 MeV (-218.2 ppm) |
| ${}^{275}$Mt | 275 | 166 | L?-pending | binding_energy | — | 1995.6750 | — | 256243.7776 MeV (-218.0 ppm) |
| ${}^{276}$Mt | 276 | 167 | L?-pending | binding_energy | — | 2001.0000 | — | 257178.0178 MeV (-216.4 ppm) |
| ${}^{277}$Mt | 277 | 168 | L?-pending | binding_energy | — | 2007.4190 | — | 258111.1640 MeV (-215.8 ppm) |
| ${}^{278}$Mt | 278 | 169 | L?-pending | binding_energy | — | 2012.7200 | — | 259045.4281 MeV (-215.0 ppm) |
| ${}^{279}$Mt | 279 | 170 | L?-pending | binding_energy | — | 2019.1230 | — | 259978.5903 MeV (-214.8 ppm) |
| ${}^{280}$Mt | 280 | 171 | L?-pending | binding_energy | — | 2024.1200 | — | 260913.1585 MeV (-213.4 ppm) |
| ${}^{281}$Mt | 281 | 172 | L?-pending | binding_energy | — | 2030.2250 | — | 261846.6187 MeV (-212.4 ppm) |
| ${}^{282}$Mt | 282 | 173 | L?-pending | binding_energy | — | 2035.4760 | — | 262780.9329 MeV (-212.5 ppm) |

### Sodium (Z = 11)

_0 of 23 isotopes with a framework prediction; 23 of 23 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{17}$Na | 17 | 6 | L?-pending | binding_energy | — | 93.8870 | — | 15864.4945 MeV (-354.4 ppm) |
| ${}^{18}$Na | 18 | 7 | L?-pending | binding_energy | — | 111.6399 | — | 16786.3068 MeV (-335.0 ppm) |
| ${}^{19}$Na | 19 | 8 | L?-pending | binding_energy | — | 131.8198 | — | 17705.6920 MeV (-317.6 ppm) |
| ${}^{20}$Na | 20 | 9 | L?-pending | binding_energy | — | 145.9701 | — | 18631.1070 MeV (-301.9 ppm) |
| ${}^{21}$Na | 21 | 10 | L?-pending | binding_energy | — | 163.0767 | — | 19553.5655 MeV (-287.6 ppm) |
| ${}^{22}$Na | 22 | 11 | L?-pending | binding_energy | — | 174.1446 | — | 20482.0628 MeV (-274.6 ppm) |
| ${}^{23}$Na | 23 | 12 | L?-pending | binding_energy | — | 186.5644 | — | 21409.2082 MeV (-262.7 ppm) |
| ${}^{24}$Na | 24 | 13 | L?-pending | binding_energy | — | 193.5237 | — | 22341.8141 MeV (-251.8 ppm) |
| ${}^{25}$Na | 25 | 14 | L?-pending | binding_energy | — | 202.5349 | — | 23272.3680 MeV (-241.7 ppm) |
| ${}^{26}$Na | 26 | 15 | L?-pending | binding_energy | — | 208.1092 | — | 24206.3589 MeV (-232.4 ppm) |
| ${}^{27}$Na | 27 | 16 | L?-pending | binding_energy | — | 214.8376 | — | 25139.1958 MeV (-223.8 ppm) |
| ${}^{28}$Na | 28 | 17 | L?-pending | binding_energy | — | 218.3794 | — | 26075.2191 MeV (-215.8 ppm) |
| ${}^{29}$Na | 29 | 18 | L?-pending | binding_energy | — | 222.7824 | — | 27010.3813 MeV (-208.3 ppm) |
| ${}^{30}$Na | 30 | 19 | L?-pending | binding_energy | — | 225.0591 | — | 27947.6698 MeV (-201.3 ppm) |
| ${}^{31}$Na | 31 | 20 | L?-pending | binding_energy | — | 229.3590 | — | 28882.9351 MeV (-194.8 ppm) |
| ${}^{32}$Na | 32 | 21 | L?-pending | binding_energy | — | 231.0362 | — | 29820.8230 MeV (-188.7 ppm) |
| ${}^{33}$Na | 33 | 22 | L?-pending | binding_energy | — | 233.9676 | — | 30757.4569 MeV (-183.0 ppm) |
| ${}^{34}$Na | 34 | 23 | L?-pending | binding_energy | — | 234.1389 | — | 31696.8507 MeV (-177.6 ppm) |
| ${}^{35}$Na | 35 | 24 | L?-pending | binding_energy | — | 236.0750 | — | 32634.4798 MeV (-173.0 ppm) |
| ${}^{36}$Na | 36 | 25 | L?-pending | binding_energy | — | 236.0520 | — | 33574.0680 MeV (-167.4 ppm) |
| ${}^{37}$Na | 37 | 26 | L?-pending | binding_energy | — | 236.9110 | — | 34512.7742 MeV (-163.4 ppm) |
| ${}^{38}$Na | 38 | 27 | L?-pending | binding_energy | — | 236.2080 | — | 35453.0424 MeV (-159.0 ppm) |
| ${}^{39}$Na | 39 | 28 | L?-pending | binding_energy | — | 236.1840 | — | 36392.6315 MeV (-154.3 ppm) |

### Darmstadtium (Z = 110)

_0 of 18 isotopes with a framework prediction; 18 of 18 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{267}$Ds | 267 | 157 | L?-pending | binding_energy | — | 1935.2160 | — | 248786.4218 MeV (-226.6 ppm) |
| ${}^{268}$Ds | 268 | 158 | L?-pending | binding_energy | — | 1943.5360 | — | 249717.6670 MeV (-225.8 ppm) |
| ${}^{269}$Ds | 269 | 159 | L?-pending | binding_energy | — | 1950.2917 | — | 250650.4764 MeV (-224.5 ppm) |
| ${}^{270}$Ds | 270 | 160 | L?-pending | binding_energy | — | 1958.5161 | — | 251581.8172 MeV (-223.6 ppm) |
| ${}^{271}$Ds | 271 | 161 | L?-pending | binding_energy | — | 1965.2920 | — | 252514.6065 MeV (-222.7 ppm) |
| ${}^{272}$Ds | 272 | 162 | L?-pending | binding_energy | — | 1973.3600 | — | 253446.1037 MeV (-222.4 ppm) |
| ${}^{273}$Ds | 273 | 163 | L?-pending | binding_energy | — | 1979.2500 | — | 254379.7789 MeV (-221.7 ppm) |
| ${}^{274}$Ds | 274 | 164 | L?-pending | binding_energy | — | 1986.2260 | — | 255312.3681 MeV (-220.1 ppm) |
| ${}^{275}$Ds | 275 | 165 | L?-pending | binding_energy | — | 1991.8250 | — | 256246.3343 MeV (-219.3 ppm) |
| ${}^{276}$Ds | 276 | 166 | L?-pending | binding_energy | — | 1999.0680 | — | 257178.6564 MeV (-218.7 ppm) |
| ${}^{277}$Ds | 277 | 167 | L?-pending | binding_energy | — | 2004.6490 | — | 258112.6406 MeV (-218.1 ppm) |
| ${}^{278}$Ds | 278 | 168 | L?-pending | binding_energy | — | 2011.6080 | — | 259045.2468 MeV (-217.5 ppm) |
| ${}^{279}$Ds | 279 | 169 | L?-pending | binding_energy | — | 2016.8910 | — | 259979.5290 MeV (-216.7 ppm) |
| ${}^{280}$Ds | 280 | 170 | L?-pending | binding_energy | — | 2023.5600 | — | 260912.4252 MeV (-215.5 ppm) |
| ${}^{281}$Ds | 281 | 171 | L?-pending | binding_energy | — | 2028.8200 | — | 261846.7304 MeV (-215.3 ppm) |
| ${}^{282}$Ds | 282 | 172 | L?-pending | binding_energy | — | 2035.1940 | — | 262779.9216 MeV (-213.8 ppm) |
| ${}^{283}$Ds | 283 | 173 | L?-pending | binding_energy | — | 2040.4300 | — | 263714.2507 MeV (-213.9 ppm) |
| ${}^{284}$Ds | 284 | 174 | L?-pending | binding_energy | — | 2046.7880 | — | 264647.4579 MeV (-212.8 ppm) |

### Roentgenium (Z = 111)

_0 of 15 isotopes with a framework prediction; 15 of 15 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{272}$Rg | 272 | 161 | L?-pending | binding_energy | — | 1965.7440 | — | 253452.4264 MeV (-223.8 ppm) |
| ${}^{273}$Rg | 273 | 162 | L?-pending | binding_energy | — | 1973.7900 | — | 254383.9456 MeV (-223.3 ppm) |
| ${}^{274}$Rg | 274 | 163 | L?-pending | binding_energy | — | 1980.1980 | — | 255317.1027 MeV (-222.8 ppm) |
| ${}^{275}$Rg | 275 | 164 | L?-pending | binding_energy | — | 1987.4250 | — | 256249.4409 MeV (-221.7 ppm) |
| ${}^{276}$Rg | 276 | 165 | L?-pending | binding_energy | — | 1993.5480 | — | 257182.8831 MeV (-221.1 ppm) |
| ${}^{277}$Rg | 277 | 166 | L?-pending | binding_energy | — | 2000.4940 | — | 258115.5023 MeV (-219.9 ppm) |
| ${}^{278}$Rg | 278 | 167 | L?-pending | binding_energy | — | 2006.6040 | — | 259048.9575 MeV (-219.7 ppm) |
| ${}^{279}$Rg | 279 | 168 | L?-pending | binding_energy | — | 2013.2640 | — | 259981.8627 MeV (-218.1 ppm) |
| ${}^{280}$Rg | 280 | 169 | L?-pending | binding_energy | — | 2019.3600 | — | 260915.3319 MeV (-218.0 ppm) |
| ${}^{281}$Rg | 281 | 170 | L?-pending | binding_energy | — | 2025.7290 | — | 261848.5280 MeV (-216.3 ppm) |
| ${}^{282}$Rg | 282 | 171 | L?-pending | binding_energy | — | 2031.5280 | — | 262782.2942 MeV (-216.0 ppm) |
| ${}^{283}$Rg | 283 | 172 | L?-pending | binding_energy | — | 2037.8830 | — | 263715.5044 MeV (-215.0 ppm) |
| ${}^{284}$Rg | 284 | 173 | L?-pending | binding_energy | — | 2043.3800 | — | 264649.5726 MeV (-214.3 ppm) |
| ${}^{285}$Rg | 285 | 174 | L?-pending | binding_energy | — | 2049.7200 | — | 265582.7978 MeV (-213.6 ppm) |
| ${}^{286}$Rg | 286 | 175 | L?-pending | binding_energy | — | 2054.9100 | — | 266517.1730 MeV (-212.5 ppm) |

### Copernicium (Z = 112)

_0 of 13 isotopes with a framework prediction; 13 of 13 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{276}$Cn | 276 | 164 | L?-pending | binding_energy | — | 1989.6840 | — | 257185.4538 MeV (-222.7 ppm) |
| ${}^{277}$Cn | 277 | 165 | L?-pending | binding_energy | — | 1995.7850 | — | 258118.9180 MeV (-221.9 ppm) |
| ${}^{278}$Cn | 278 | 166 | L?-pending | binding_energy | — | 2003.2680 | — | 259051.0002 MeV (-220.8 ppm) |
| ${}^{279}$Cn | 279 | 167 | L?-pending | binding_energy | — | 2009.3580 | — | 259984.4753 MeV (-220.7 ppm) |
| ${}^{280}$Cn | 280 | 168 | L?-pending | binding_energy | — | 2016.5600 | — | 260916.8385 MeV (-219.0 ppm) |
| ${}^{281}$Cn | 281 | 169 | L?-pending | binding_energy | — | 2022.3570 | — | 261850.6067 MeV (-218.3 ppm) |
| ${}^{282}$Cn | 282 | 170 | L?-pending | binding_energy | — | 2029.5540 | — | 262782.9749 MeV (-217.6 ppm) |
| ${}^{283}$Cn | 283 | 171 | L?-pending | binding_energy | — | 2035.3360 | — | 263716.7581 MeV (-217.6 ppm) |
| ${}^{284}$Cn | 284 | 172 | L?-pending | binding_energy | — | 2042.2440 | — | 264649.4153 MeV (-216.6 ppm) |
| ${}^{285}$Cn | 285 | 173 | L?-pending | binding_energy | — | 2047.7250 | — | 265583.4994 MeV (-216.1 ppm) |
| ${}^{286}$Cn | 286 | 174 | L?-pending | binding_energy | — | 2054.3380 | — | 266516.4516 MeV (-215.0 ppm) |
| ${}^{287}$Cn | 287 | 175 | L?-pending | binding_energy | — | 2059.5120 | — | 267450.8428 MeV (-214.3 ppm) |
| ${}^{288}$Cn | 288 | 176 | L?-pending | binding_energy | — | 2066.1120 | — | 268383.8080 MeV (-213.9 ppm) |

### Nihonium (Z = 113)

_0 of 13 isotopes with a framework prediction; 13 of 13 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{278}$Nh | 278 | 165 | L?-pending | binding_energy | — | 1996.3180 | — | 259056.6568 MeV (-222.8 ppm) |
| ${}^{279}$Nh | 279 | 166 | L?-pending | binding_energy | — | 2004.0570 | — | 259988.4830 MeV (-222.4 ppm) |
| ${}^{280}$Nh | 280 | 167 | L?-pending | binding_energy | — | 2010.4000 | — | 260921.7052 MeV (-221.8 ppm) |
| ${}^{281}$Nh | 281 | 168 | L?-pending | binding_energy | — | 2017.8610 | — | 261853.8094 MeV (-220.9 ppm) |
| ${}^{282}$Nh | 282 | 169 | L?-pending | binding_energy | — | 2023.9140 | — | 262787.3216 MeV (-219.7 ppm) |
| ${}^{283}$Nh | 283 | 170 | L?-pending | binding_energy | — | 2031.0910 | — | 263719.7097 MeV (-218.7 ppm) |
| ${}^{284}$Nh | 284 | 171 | L?-pending | binding_energy | — | 2037.1320 | — | 264653.2339 MeV (-217.9 ppm) |
| ${}^{285}$Nh | 285 | 172 | L?-pending | binding_energy | — | 2044.0200 | — | 265585.9111 MeV (-217.1 ppm) |
| ${}^{286}$Nh | 286 | 173 | L?-pending | binding_energy | — | 2050.0480 | — | 266519.4483 MeV (-216.9 ppm) |
| ${}^{287}$Nh | 287 | 174 | L?-pending | binding_energy | — | 2056.6420 | — | 267452.4195 MeV (-216.2 ppm) |
| ${}^{288}$Nh | 288 | 175 | L?-pending | binding_energy | — | 2062.0800 | — | 268386.5467 MeV (-215.0 ppm) |
| ${}^{289}$Nh | 289 | 176 | L?-pending | binding_energy | — | 2068.6620 | — | 269319.5298 MeV (-214.6 ppm) |
| ${}^{290}$Nh | 290 | 177 | L?-pending | binding_energy | — | 2074.0800 | — | 270253.6770 MeV (-214.3 ppm) |

### Flerovium (Z = 114)

_0 of 8 isotopes with a framework prediction; 8 of 8 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{284}$Fl | 284 | 170 | L?-pending | binding_energy | — | 2034.2920 | — | 264654.7806 MeV (-220.3 ppm) |
| ${}^{285}$Fl | 285 | 171 | L?-pending | binding_energy | — | 2040.3150 | — | 265588.3228 MeV (-219.9 ppm) |
| ${}^{286}$Fl | 286 | 172 | L?-pending | binding_energy | — | 2047.4740 | — | 266520.7290 MeV (-218.3 ppm) |
| ${}^{287}$Fl | 287 | 173 | L?-pending | binding_energy | — | 2053.4850 | — | 267454.2831 MeV (-218.5 ppm) |
| ${}^{288}$Fl | 288 | 174 | L?-pending | binding_energy | — | 2060.3520 | — | 268386.9813 MeV (-216.9 ppm) |
| ${}^{289}$Fl | 289 | 175 | L?-pending | binding_energy | — | 2066.0610 | — | 269320.8375 MeV (-216.9 ppm) |
| ${}^{290}$Fl | 290 | 176 | L?-pending | binding_energy | — | 2072.6300 | — | 270253.8337 MeV (-215.3 ppm) |
| ${}^{291}$Fl | 291 | 177 | L?-pending | binding_energy | — | 2078.0310 | — | 271187.9979 MeV (-214.9 ppm) |

### Moscovium (Z = 115)

_0 of 6 isotopes with a framework prediction; 6 of 6 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{287}$Mc | 287 | 172 | L?-pending | binding_energy | — | 2048.8930 | — | 267457.5818 MeV (-220.4 ppm) |
| ${}^{288}$Mc | 288 | 173 | L?-pending | binding_energy | — | 2054.8800 | — | 268391.1600 MeV (-219.1 ppm) |
| ${}^{289}$Mc | 289 | 174 | L?-pending | binding_energy | — | 2062.0150 | — | 269323.5902 MeV (-218.6 ppm) |
| ${}^{290}$Mc | 290 | 175 | L?-pending | binding_energy | — | 2067.9900 | — | 270257.1804 MeV (-217.9 ppm) |
| ${}^{291}$Mc | 291 | 176 | L?-pending | binding_energy | — | 2074.5390 | — | 271190.1966 MeV (-216.7 ppm) |
| ${}^{292}$Mc | 292 | 177 | L?-pending | binding_energy | — | 2080.2080 | — | 272124.0927 MeV (-216.0 ppm) |

### Livermorium (Z = 116)

_0 of 5 isotopes with a framework prediction; 5 of 5 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{289}$Lv | 289 | 173 | L?-pending | binding_energy | — | 2057.3910 | — | 269326.9209 MeV (-220.2 ppm) |
| ${}^{290}$Lv | 290 | 174 | L?-pending | binding_energy | — | 2064.8000 | — | 270259.0770 MeV (-219.1 ppm) |
| ${}^{291}$Lv | 291 | 175 | L?-pending | binding_energy | — | 2070.7560 | — | 271192.6862 MeV (-218.8 ppm) |
| ${}^{292}$Lv | 292 | 176 | L?-pending | binding_energy | — | 2077.8720 | — | 272125.1354 MeV (-217.8 ppm) |
| ${}^{293}$Lv | 293 | 177 | L?-pending | binding_energy | — | 2083.5230 | — | 273059.0496 MeV (-217.1 ppm) |

### Tennessine (Z = 117)

_0 of 4 isotopes with a framework prediction; 4 of 4 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{291}$Ts | 291 | 174 | L?-pending | binding_energy | — | 2065.5180 | — | 271196.6309 MeV (-220.5 ppm) |
| ${}^{292}$Ts | 292 | 175 | L?-pending | binding_energy | — | 2071.7400 | — | 272129.9741 MeV (-220.2 ppm) |
| ${}^{293}$Ts | 293 | 176 | L?-pending | binding_energy | — | 2078.8350 | — | 273062.4443 MeV (-218.8 ppm) |
| ${}^{294}$Ts | 294 | 177 | L?-pending | binding_energy | — | 2085.0480 | — | 273995.7964 MeV (-218.4 ppm) |

### Oganesson (Z = 118)

_0 of 3 isotopes with a framework prediction; 3 of 3 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{293}$Og | 293 | 175 | L?-pending | binding_energy | — | 2073.8540 | — | 273066.1319 MeV (-221.3 ppm) |
| ${}^{294}$Og | 294 | 176 | L?-pending | binding_energy | — | 2081.2260 | — | 273998.3251 MeV (-219.9 ppm) |
| ${}^{295}$Og | 295 | 177 | L?-pending | binding_energy | — | 2087.4200 | — | 274931.6963 MeV (-219.8 ppm) |

### Magnesium (Z = 12)

_1 of 23 isotopes with a framework prediction; 23 of 23 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{19}$Mg | 19 | 7 | L?-pending | binding_energy | — | 112.1285 | — | 17724.0900 MeV (-346.1 ppm) |
| ${}^{20}$Mg | 20 | 8 | L?-pending | binding_energy | — | 134.5605 | — | 18641.2232 MeV (-329.1 ppm) |
| ${}^{21}$Mg | 21 | 9 | L?-pending | binding_energy | — | 149.2057 | — | 19566.1432 MeV (-313.5 ppm) |
| ${}^{22}$Mg | 22 | 10 | L?-pending | binding_energy | — | 168.5808 | — | 20486.3333 MeV (-299.5 ppm) |
| ${}^{23}$Mg | 23 | 11 | L?-pending | binding_energy | — | 181.7258 | — | 21412.7534 MeV (-286.5 ppm) |
| ${}^{24}$Mg | 24 | 12 | L2-alpha-cluster | binding_energy | 216.1389 | 198.2570 | +9.02 % | 22317.9055 MeV (-1075.1 ppm) |
| ${}^{25}$Mg | 25 | 13 | L?-pending | binding_energy | — | 205.5876 | — | 23268.0221 MeV (-263.7 ppm) |
| ${}^{26}$Mg | 26 | 14 | L?-pending | binding_energy | — | 216.6806 | — | 24196.4942 MeV (-253.6 ppm) |
| ${}^{27}$Mg | 27 | 15 | L?-pending | binding_energy | — | 223.1240 | — | 25129.6160 MeV (-244.2 ppm) |
| ${}^{28}$Mg | 28 | 16 | L?-pending | binding_energy | — | 231.6287 | — | 26060.6765 MeV (-235.5 ppm) |
| ${}^{29}$Mg | 29 | 17 | L?-pending | binding_energy | — | 235.2924 | — | 26996.5780 MeV (-227.3 ppm) |
| ${}^{30}$Mg | 30 | 18 | L?-pending | binding_energy | — | 241.6327 | — | 27929.8028 MeV (-219.7 ppm) |
| ${}^{31}$Mg | 31 | 19 | L?-pending | binding_energy | — | 243.9448 | — | 28867.0559 MeV (-212.6 ppm) |
| ${}^{32}$Mg | 32 | 20 | L?-pending | binding_energy | — | 249.7229 | — | 29800.8430 MeV (-206.0 ppm) |
| ${}^{33}$Mg | 33 | 21 | L?-pending | binding_energy | — | 252.0025 | — | 30738.1286 MeV (-199.7 ppm) |
| ${}^{34}$Mg | 34 | 22 | L?-pending | binding_energy | — | 256.7133 | — | 31672.9830 MeV (-193.8 ppm) |
| ${}^{35}$Mg | 35 | 23 | L?-pending | binding_energy | — | 257.4682 | — | 32611.7933 MeV (-188.2 ppm) |
| ${}^{36}$Mg | 36 | 24 | L?-pending | binding_energy | — | 260.7991 | — | 33548.0275 MeV (-183.0 ppm) |
| ${}^{37}$Mg | 37 | 25 | L?-pending | binding_energy | — | 261.0391 | — | 34487.3527 MeV (-178.0 ppm) |
| ${}^{38}$Mg | 38 | 26 | L?-pending | binding_energy | — | 263.2640 | — | 35424.6930 MeV (-173.8 ppm) |
| ${}^{39}$Mg | 39 | 27 | L?-pending | binding_energy | — | 262.6260 | — | 36364.8962 MeV (-169.1 ppm) |
| ${}^{40}$Mg | 40 | 28 | L?-pending | binding_energy | — | 263.9200 | — | 37303.1674 MeV (-164.7 ppm) |
| ${}^{41}$Mg | 41 | 29 | L?-pending | binding_energy | — | 263.4250 | — | 38243.2276 MeV (-160.3 ppm) |

### Aluminium (Z = 13)

_0 of 23 isotopes with a framework prediction; 23 of 23 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{21}$Al | 21 | 8 | L?-pending | binding_energy | — | 132.2370 | — | 19581.8186 MeV (-339.3 ppm) |
| ${}^{22}$Al | 22 | 9 | L?-pending | binding_energy | — | 149.2040 | — | 20504.4167 MeV (-324.5 ppm) |
| ${}^{23}$Al | 23 | 10 | L?-pending | binding_energy | — | 168.7217 | — | 21424.4642 MeV (-310.2 ppm) |
| ${}^{24}$Al | 24 | 11 | L?-pending | binding_energy | — | 183.5899 | — | 22349.1612 MeV (-297.4 ppm) |
| ${}^{25}$Al | 25 | 12 | L?-pending | binding_energy | — | 200.5284 | — | 23271.7879 MeV (-285.6 ppm) |
| ${}^{26}$Al | 26 | 13 | L?-pending | binding_energy | — | 211.8939 | — | 24199.9876 MeV (-274.7 ppm) |
| ${}^{27}$Al | 27 | 14 | L?-pending | binding_energy | — | 224.9519 | — | 25126.4947 MeV (-264.6 ppm) |
| ${}^{28}$Al | 28 | 15 | L?-pending | binding_energy | — | 232.6771 | — | 26058.3347 MeV (-255.1 ppm) |
| ${}^{29}$Al | 29 | 16 | L?-pending | binding_energy | — | 242.1055 | — | 26988.4716 MeV (-246.3 ppm) |
| ${}^{30}$Al | 30 | 17 | L?-pending | binding_energy | — | 247.8331 | — | 27922.3091 MeV (-238.1 ppm) |
| ${}^{31}$Al | 31 | 18 | L?-pending | binding_energy | — | 254.9911 | — | 28854.7164 MeV (-230.4 ppm) |
| ${}^{32}$Al | 32 | 19 | L?-pending | binding_energy | — | 259.2110 | — | 29790.0616 MeV (-223.2 ppm) |
| ${}^{33}$Al | 33 | 20 | L?-pending | binding_energy | — | 264.6804 | — | 30724.1574 MeV (-216.4 ppm) |
| ${}^{34}$Al | 34 | 21 | L?-pending | binding_energy | — | 267.2519 | — | 31661.1510 MeV (-210.0 ppm) |
| ${}^{35}$Al | 35 | 22 | L?-pending | binding_energy | — | 272.5494 | — | 32595.4188 MeV (-204.0 ppm) |
| ${}^{36}$Al | 36 | 23 | L?-pending | binding_energy | — | 274.4466 | — | 33533.0868 MeV (-198.3 ppm) |
| ${}^{37}$Al | 37 | 24 | L?-pending | binding_energy | — | 278.6587 | — | 34468.4398 MeV (-192.9 ppm) |
| ${}^{38}$Al | 38 | 25 | L?-pending | binding_energy | — | 280.0600 | — | 35406.6037 MeV (-187.6 ppm) |
| ${}^{39}$Al | 39 | 26 | L?-pending | binding_energy | — | 283.1400 | — | 36343.0889 MeV (-183.5 ppm) |
| ${}^{40}$Al | 40 | 27 | L?-pending | binding_energy | — | 283.8800 | — | 37281.9141 MeV (-178.9 ppm) |
| ${}^{41}$Al | 41 | 28 | L?-pending | binding_energy | — | 286.1800 | — | 38219.1793 MeV (-174.5 ppm) |
| ${}^{42}$Al | 42 | 29 | L?-pending | binding_energy | — | 286.8180 | — | 39158.1064 MeV (-169.4 ppm) |
| ${}^{43}$Al | 43 | 30 | L?-pending | binding_energy | — | 288.6160 | — | 40095.8736 MeV (-165.6 ppm) |

### Silicon (Z = 14)

_0 of 24 isotopes with a framework prediction; 24 of 24 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{22}$Si | 22 | 8 | L?-pending | binding_energy | — | 132.9680 | — | 20519.3594 MeV (-348.4 ppm) |
| ${}^{23}$Si | 23 | 9 | L?-pending | binding_energy | — | 150.7420 | — | 21441.1506 MeV (-334.0 ppm) |
| ${}^{24}$Si | 24 | 10 | L?-pending | binding_energy | — | 172.0136 | — | 22359.4442 MeV (-320.1 ppm) |
| ${}^{25}$Si | 25 | 11 | L?-pending | binding_energy | — | 187.0028 | — | 23284.0202 MeV (-307.4 ppm) |
| ${}^{26}$Si | 26 | 12 | L?-pending | binding_energy | — | 206.0424 | — | 24204.5457 MeV (-295.7 ppm) |
| ${}^{27}$Si | 27 | 13 | L?-pending | binding_energy | — | 219.3572 | — | 25130.7961 MeV (-284.8 ppm) |
| ${}^{28}$Si | 28 | 14 | L?-pending | binding_energy | — | 236.5368 | — | 26053.1817 MeV (-274.8 ppm) |
| ${}^{29}$Si | 29 | 15 | L?-pending | binding_energy | — | 245.0104 | — | 26984.2733 MeV (-265.3 ppm) |
| ${}^{30}$Si | 30 | 16 | L?-pending | binding_energy | — | 255.6196 | — | 27913.2292 MeV (-256.5 ppm) |
| ${}^{31}$Si | 31 | 17 | L?-pending | binding_energy | — | 262.2070 | — | 28846.2070 MeV (-248.2 ppm) |
| ${}^{32}$Si | 32 | 18 | L?-pending | binding_energy | — | 271.4070 | — | 29776.5723 MeV (-240.4 ppm) |
| ${}^{33}$Si | 33 | 19 | L?-pending | binding_energy | — | 275.9150 | — | 30711.6295 MeV (-233.1 ppm) |
| ${}^{34}$Si | 34 | 20 | L?-pending | binding_energy | — | 283.4636 | — | 31643.6460 MeV (-226.3 ppm) |
| ${}^{35}$Si | 35 | 21 | L?-pending | binding_energy | — | 285.9348 | — | 32580.7401 MeV (-219.8 ppm) |
| ${}^{36}$Si | 36 | 22 | L?-pending | binding_energy | — | 292.0507 | — | 33514.1893 MeV (-213.7 ppm) |
| ${}^{37}$Si | 37 | 23 | L?-pending | binding_energy | — | 294.2574 | — | 34451.5478 MeV (-207.9 ppm) |
| ${}^{38}$Si | 38 | 24 | L?-pending | binding_energy | — | 299.9275 | — | 35385.4428 MeV (-202.4 ppm) |
| ${}^{39}$Si | 39 | 25 | L?-pending | binding_energy | — | 301.5082 | — | 36323.4274 MeV (-197.2 ppm) |
| ${}^{40}$Si | 40 | 26 | L?-pending | binding_energy | — | 306.2330 | — | 37258.2678 MeV (-192.2 ppm) |
| ${}^{41}$Si | 41 | 27 | L?-pending | binding_energy | — | 306.7620 | — | 38197.3039 MeV (-187.3 ppm) |
| ${}^{42}$Si | 42 | 28 | L?-pending | binding_energy | — | 311.2200 | — | 39132.4111 MeV (-183.5 ppm) |
| ${}^{43}$Si | 43 | 29 | L?-pending | binding_energy | — | 311.7930 | — | 40071.4033 MeV (-179.0 ppm) |
| ${}^{44}$Si | 44 | 30 | L?-pending | binding_energy | — | 314.8640 | — | 41007.8975 MeV (-174.4 ppm) |
| ${}^{45}$Si | 45 | 31 | L?-pending | binding_energy | — | 315.1800 | — | 41947.1467 MeV (-171.1 ppm) |

### Phosphorus (Z = 15)

_0 of 24 isotopes with a framework prediction; 24 of 24 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{24}$P | 24 | 9 | L?-pending | binding_energy | — | 147.9600 | — | 22382.2045 MeV (-342.7 ppm) |
| ${}^{25}$P | 25 | 10 | L?-pending | binding_energy | — | 169.8500 | — | 23299.8796 MeV (-328.8 ppm) |
| ${}^{26}$P | 26 | 11 | L?-pending | binding_energy | — | 187.1480 | — | 24222.1468 MeV (-316.7 ppm) |
| ${}^{27}$P | 27 | 12 | L?-pending | binding_energy | — | 206.8494 | — | 25142.0106 MeV (-305.0 ppm) |
| ${}^{28}$P | 28 | 13 | L?-pending | binding_energy | — | 221.4096 | — | 26067.0156 MeV (-294.2 ppm) |
| ${}^{29}$P | 29 | 14 | L?-pending | binding_energy | — | 239.2859 | — | 26988.7045 MeV (-284.2 ppm) |
| ${}^{30}$P | 30 | 15 | L?-pending | binding_energy | — | 250.6052 | — | 27916.9504 MeV (-274.7 ppm) |
| ${}^{31}$P | 31 | 16 | L?-pending | binding_energy | — | 262.9162 | — | 28844.2045 MeV (-265.9 ppm) |
| ${}^{32}$P | 32 | 17 | L?-pending | binding_energy | — | 270.8518 | — | 29775.8341 MeV (-257.6 ppm) |
| ${}^{33}$P | 33 | 18 | L?-pending | binding_energy | — | 280.9556 | — | 30705.2955 MeV (-249.8 ppm) |
| ${}^{34}$P | 34 | 19 | L?-pending | binding_energy | — | 287.2383 | — | 31638.5780 MeV (-242.5 ppm) |
| ${}^{35}$P | 35 | 20 | L?-pending | binding_energy | — | 295.6187 | — | 32569.7627 MeV (-235.5 ppm) |
| ${}^{36}$P | 36 | 21 | L?-pending | binding_energy | — | 299.0833 | — | 33505.8634 MeV (-229.0 ppm) |
| ${}^{37}$P | 37 | 22 | L?-pending | binding_energy | — | 305.8996 | — | 34438.6123 MeV (-222.8 ppm) |
| ${}^{38}$P | 38 | 23 | L?-pending | binding_energy | — | 309.5964 | — | 35374.4806 MeV (-216.9 ppm) |
| ${}^{39}$P | 39 | 24 | L?-pending | binding_energy | — | 315.8208 | — | 36307.8214 MeV (-211.3 ppm) |
| ${}^{40}$P | 40 | 25 | L?-pending | binding_energy | — | 319.2567 | — | 37243.9507 MeV (-206.0 ppm) |
| ${}^{41}$P | 41 | 26 | L?-pending | binding_energy | — | 324.1686 | — | 38178.6040 MeV (-201.0 ppm) |
| ${}^{42}$P | 42 | 27 | L?-pending | binding_energy | — | 326.1683 | — | 39116.1695 MeV (-196.2 ppm) |
| ${}^{43}$P | 43 | 28 | L?-pending | binding_energy | — | 330.2830 | — | 40051.6200 MeV (-191.4 ppm) |
| ${}^{44}$P | 44 | 29 | L?-pending | binding_energy | — | 332.2880 | — | 40989.1801 MeV (-187.1 ppm) |
| ${}^{45}$P | 45 | 30 | L?-pending | binding_energy | — | 335.5200 | — | 41925.5133 MeV (-183.2 ppm) |
| ${}^{46}$P | 46 | 31 | L?-pending | binding_energy | — | 336.7200 | — | 42863.8785 MeV (-179.4 ppm) |
| ${}^{47}$P | 47 | 32 | L?-pending | binding_energy | — | 338.8230 | — | 43801.3407 MeV (-175.6 ppm) |

### Sulfur (Z = 16)

_0 of 24 isotopes with a framework prediction; 24 of 24 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{26}$S | 26 | 10 | L?-pending | binding_energy | — | 169.6500 | — | 24238.3515 MeV (-337.2 ppm) |
| ${}^{27}$S | 27 | 11 | L?-pending | binding_energy | — | 187.9200 | — | 25159.6467 MeV (-325.2 ppm) |
| ${}^{28}$S | 28 | 12 | L?-pending | binding_energy | — | 209.4062 | — | 26077.7257 MeV (-313.7 ppm) |
| ${}^{29}$S | 29 | 13 | L?-pending | binding_energy | — | 224.6451 | — | 27002.0519 MeV (-302.9 ppm) |
| ${}^{30}$S | 30 | 14 | L?-pending | binding_energy | — | 243.6812 | — | 27922.5810 MeV (-293.0 ppm) |
| ${}^{31}$S | 31 | 15 | L?-pending | binding_energy | — | 256.7358 | — | 28849.0916 MeV (-283.6 ppm) |
| ${}^{32}$S | 32 | 16 | L?-pending | binding_energy | — | 271.7802 | — | 29773.6124 MeV (-274.8 ppm) |
| ${}^{33}$S | 33 | 17 | L?-pending | binding_energy | — | 280.4218 | — | 30704.5360 MeV (-266.5 ppm) |
| ${}^{34}$S | 34 | 18 | L?-pending | binding_energy | — | 291.8390 | — | 31632.6840 MeV (-258.6 ppm) |
| ${}^{35}$S | 35 | 19 | L?-pending | binding_energy | — | 298.8248 | — | 32565.2634 MeV (-251.2 ppm) |
| ${}^{36}$S | 36 | 20 | L?-pending | binding_energy | — | 308.7140 | — | 33494.9393 MeV (-244.3 ppm) |
| ${}^{37}$S | 37 | 21 | L?-pending | binding_energy | — | 313.0176 | — | 34430.2009 MeV (-237.7 ppm) |
| ${}^{38}$S | 38 | 22 | L?-pending | binding_energy | — | 321.0538 | — | 35361.7300 MeV (-231.4 ppm) |
| ${}^{39}$S | 39 | 23 | L?-pending | binding_energy | — | 325.4265 | — | 36296.9224 MeV (-225.4 ppm) |
| ${}^{40}$S | 40 | 24 | L?-pending | binding_energy | — | 333.1730 | — | 37228.7411 MeV (-219.8 ppm) |
| ${}^{41}$S | 41 | 25 | L?-pending | binding_energy | — | 337.4151 | — | 38164.0642 MeV (-214.4 ppm) |
| ${}^{42}$S | 42 | 26 | L?-pending | binding_energy | — | 344.1156 | — | 39096.9289 MeV (-209.3 ppm) |
| ${}^{43}$S | 43 | 27 | L?-pending | binding_energy | — | 346.7446 | — | 40033.8650 MeV (-204.4 ppm) |
| ${}^{44}$S | 44 | 28 | L?-pending | binding_energy | — | 351.8247 | — | 40968.3501 MeV (-199.8 ppm) |
| ${}^{45}$S | 45 | 29 | L?-pending | binding_energy | — | 354.0150 | — | 41905.7250 MeV (-194.9 ppm) |
| ${}^{46}$S | 46 | 30 | L?-pending | binding_energy | — | 358.1100 | — | 42841.1952 MeV (-190.7 ppm) |
| ${}^{47}$S | 47 | 31 | L?-pending | binding_energy | — | 359.6440 | — | 43779.2264 MeV (-187.2 ppm) |
| ${}^{48}$S | 48 | 32 | L?-pending | binding_energy | — | 362.4960 | — | 44715.9396 MeV (-182.6 ppm) |
| ${}^{49}$S | 49 | 33 | L?-pending | binding_energy | — | 362.6000 | — | 45655.4007 MeV (-179.6 ppm) |

### Chlorine (Z = 17)

_0 of 25 isotopes with a framework prediction; 25 of 25 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{28}$Cl | 28 | 11 | L?-pending | binding_energy | — | 184.4360 | — | 26101.4025 MeV (-333.3 ppm) |
| ${}^{29}$Cl | 29 | 12 | L?-pending | binding_energy | — | 206.7410 | — | 27018.6627 MeV (-321.5 ppm) |
| ${}^{30}$Cl | 30 | 13 | L?-pending | binding_energy | — | 224.1651 | — | 27940.8038 MeV (-311.1 ppm) |
| ${}^{31}$Cl | 31 | 14 | L?-pending | binding_energy | — | 243.9455 | — | 28860.5886 MeV (-301.2 ppm) |
| ${}^{32}$Cl | 32 | 15 | L?-pending | binding_energy | — | 258.3170 | — | 29785.7823 MeV (-291.8 ppm) |
| ${}^{33}$Cl | 33 | 16 | L?-pending | binding_energy | — | 274.0569 | — | 30709.6075 MeV (-283.0 ppm) |
| ${}^{34}$Cl | 34 | 17 | L?-pending | binding_energy | — | 285.5650 | — | 31637.6646 MeV (-274.7 ppm) |
| ${}^{35}$Cl | 35 | 18 | L?-pending | binding_energy | — | 298.2098 | — | 32564.5851 MeV (-266.9 ppm) |
| ${}^{36}$Cl | 36 | 19 | L?-pending | binding_energy | — | 306.7896 | — | 33495.5704 MeV (-259.5 ppm) |
| ${}^{37}$Cl | 37 | 20 | L?-pending | binding_energy | — | 317.1004 | — | 34424.8248 MeV (-252.5 ppm) |
| ${}^{38}$Cl | 38 | 21 | L?-pending | binding_energy | — | 323.2083 | — | 35358.2821 MeV (-245.9 ppm) |
| ${}^{39}$Cl | 39 | 22 | L?-pending | binding_energy | — | 331.2817 | — | 36289.7738 MeV (-239.6 ppm) |
| ${}^{40}$Cl | 40 | 23 | L?-pending | binding_energy | — | 337.1106 | — | 37223.5101 MeV (-233.6 ppm) |
| ${}^{41}$Cl | 41 | 24 | L?-pending | binding_energy | — | 344.9313 | — | 38155.2546 MeV (-227.9 ppm) |
| ${}^{42}$Cl | 42 | 25 | L?-pending | binding_energy | — | 350.5272 | — | 39089.2239 MeV (-222.4 ppm) |
| ${}^{43}$Cl | 43 | 26 | L?-pending | binding_energy | — | 357.9263 | — | 40021.3900 MeV (-217.3 ppm) |
| ${}^{44}$Cl | 44 | 27 | L?-pending | binding_energy | — | 362.3171 | — | 40956.5644 MeV (-212.3 ppm) |
| ${}^{45}$Cl | 45 | 28 | L?-pending | binding_energy | — | 368.1720 | — | 41890.2747 MeV (-207.6 ppm) |
| ${}^{46}$Cl | 46 | 29 | L?-pending | binding_energy | — | 371.7157 | — | 42826.2962 MeV (-203.0 ppm) |
| ${}^{47}$Cl | 47 | 30 | L?-pending | binding_energy | — | 375.6240 | — | 43761.9530 MeV (-198.5 ppm) |
| ${}^{48}$Cl | 48 | 31 | L?-pending | binding_energy | — | 378.3840 | — | 44698.7582 MeV (-194.1 ppm) |
| ${}^{49}$Cl | 49 | 32 | L?-pending | binding_energy | — | 381.4650 | — | 45635.2424 MeV (-190.8 ppm) |
| ${}^{50}$Cl | 50 | 33 | L?-pending | binding_energy | — | 382.5500 | — | 46573.7226 MeV (-186.4 ppm) |
| ${}^{51}$Cl | 51 | 34 | L?-pending | binding_energy | — | 384.0300 | — | 47511.8078 MeV (-182.7 ppm) |
| ${}^{52}$Cl | 52 | 35 | L?-pending | binding_energy | — | 384.0720 | — | 48451.3310 MeV (-180.0 ppm) |

### Argon (Z = 18)

_0 of 26 isotopes with a framework prediction; 26 of 26 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{29}$Ar | 29 | 11 | L?-pending | binding_energy | — | 182.0040 | — | 27042.1064 MeV (-339.8 ppm) |
| ${}^{30}$Ar | 30 | 12 | L?-pending | binding_energy | — | 205.9800 | — | 27957.6956 MeV (-328.9 ppm) |
| ${}^{31}$Ar | 31 | 13 | L?-pending | binding_energy | — | 224.8120 | — | 28878.4287 MeV (-318.9 ppm) |
| ${}^{32}$Ar | 32 | 14 | L?-pending | binding_energy | — | 246.4003 | — | 29796.4056 MeV (-308.8 ppm) |
| ${}^{33}$Ar | 33 | 15 | L?-pending | binding_energy | — | 261.6555 | — | 30720.7156 MeV (-299.6 ppm) |
| ${}^{34}$Ar | 34 | 16 | L?-pending | binding_energy | — | 278.7209 | — | 31643.2154 MeV (-290.8 ppm) |
| ${}^{35}$Ar | 35 | 17 | L?-pending | binding_energy | — | 291.4612 | — | 32570.0403 MeV (-282.6 ppm) |
| ${}^{36}$Ar | 36 | 18 | L?-pending | binding_energy | — | 306.7167 | — | 33494.3499 MeV (-274.8 ppm) |
| ${}^{37}$Ar | 37 | 19 | L?-pending | binding_energy | — | 315.5042 | — | 34425.1277 MeV (-267.4 ppm) |
| ${}^{38}$Ar | 38 | 20 | L?-pending | binding_energy | — | 327.3427 | — | 35352.8544 MeV (-260.4 ppm) |
| ${}^{39}$Ar | 39 | 21 | L?-pending | binding_energy | — | 333.9414 | — | 36285.8209 MeV (-253.7 ppm) |
| ${}^{40}$Ar | 40 | 22 | L?-pending | binding_energy | — | 343.8104 | — | 37215.5170 MeV (-247.3 ppm) |
| ${}^{41}$Ar | 41 | 23 | L?-pending | binding_energy | — | 349.9093 | — | 38148.9833 MeV (-241.3 ppm) |
| ${}^{42}$Ar | 42 | 24 | L?-pending | binding_energy | — | 359.3358 | — | 39079.1220 MeV (-235.6 ppm) |
| ${}^{43}$Ar | 43 | 25 | L?-pending | binding_energy | — | 364.9942 | — | 40013.0287 MeV (-230.1 ppm) |
| ${}^{44}$Ar | 44 | 26 | L?-pending | binding_energy | — | 373.7290 | — | 40943.8591 MeV (-224.8 ppm) |
| ${}^{45}$Ar | 45 | 27 | L?-pending | binding_energy | — | 378.8979 | — | 41878.2555 MeV (-219.8 ppm) |
| ${}^{46}$Ar | 46 | 28 | L?-pending | binding_energy | — | 386.9696 | — | 42809.7489 MeV (-215.1 ppm) |
| ${}^{47}$Ar | 47 | 29 | L?-pending | binding_energy | — | 390.6370 | — | 43745.6467 MeV (-210.5 ppm) |
| ${}^{48}$Ar | 48 | 30 | L?-pending | binding_energy | — | 395.6959 | — | 44680.1529 MeV (-206.1 ppm) |
| ${}^{49}$Ar | 49 | 31 | L?-pending | binding_energy | — | 398.4680 | — | 45616.9461 MeV (-201.7 ppm) |
| ${}^{50}$Ar | 50 | 32 | L?-pending | binding_energy | — | 402.7000 | — | 46552.2793 MeV (-197.5 ppm) |
| ${}^{51}$Ar | 51 | 33 | L?-pending | binding_energy | — | 404.0220 | — | 47490.5224 MeV (-193.4 ppm) |
| ${}^{52}$Ar | 52 | 34 | L?-pending | binding_energy | — | 407.0040 | — | 48427.1056 MeV (-190.1 ppm) |
| ${}^{53}$Ar | 53 | 35 | L?-pending | binding_energy | — | 406.8810 | — | 49366.7938 MeV (-186.0 ppm) |
| ${}^{54}$Ar | 54 | 36 | L?-pending | binding_energy | — | 409.2120 | — | 50304.0280 MeV (-183.1 ppm) |

### Potassium (Z = 19)

_0 of 29 isotopes with a framework prediction; 29 of 29 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{31}$K | 31 | 12 | L?-pending | binding_energy | — | 201.0970 | — | 28900.8504 MeV (-336.5 ppm) |
| ${}^{32}$K | 32 | 13 | L?-pending | binding_energy | — | 221.4400 | — | 29820.0726 MeV (-326.1 ppm) |
| ${}^{33}$K | 33 | 14 | L?-pending | binding_energy | — | 243.9360 | — | 30737.1418 MeV (-315.6 ppm) |
| ${}^{34}$K | 34 | 15 | L?-pending | binding_energy | — | 260.7800 | — | 31659.8630 MeV (-306.8 ppm) |
| ${}^{35}$K | 35 | 16 | L?-pending | binding_energy | — | 278.8044 | — | 32581.4037 MeV (-298.1 ppm) |
| ${}^{36}$K | 36 | 17 | L?-pending | binding_energy | — | 293.1200 | — | 33506.6533 MeV (-289.9 ppm) |
| ${}^{37}$K | 37 | 18 | L?-pending | binding_energy | — | 308.5744 | — | 34430.7641 MeV (-282.2 ppm) |
| ${}^{38}$K | 38 | 19 | L?-pending | binding_energy | — | 320.6463 | — | 35358.2575 MeV (-274.8 ppm) |
| ${}^{39}$K | 39 | 20 | L?-pending | binding_energy | — | 333.7240 | — | 36284.7449 MeV (-267.8 ppm) |
| ${}^{40}$K | 40 | 21 | L?-pending | binding_energy | — | 341.5236 | — | 37216.5105 MeV (-261.1 ppm) |
| ${}^{41}$K | 41 | 22 | L?-pending | binding_energy | — | 351.6190 | — | 38145.9803 MeV (-254.7 ppm) |
| ${}^{42}$K | 42 | 23 | L?-pending | binding_energy | — | 359.1528 | — | 39078.0116 MeV (-248.6 ppm) |
| ${}^{43}$K | 43 | 24 | L?-pending | binding_energy | — | 368.7775 | — | 40007.9522 MeV (-242.9 ppm) |
| ${}^{44}$K | 44 | 25 | L?-pending | binding_energy | — | 376.0549 | — | 40940.2399 MeV (-237.3 ppm) |
| ${}^{45}$K | 45 | 26 | L?-pending | binding_energy | — | 384.9604 | — | 41870.8996 MeV (-232.1 ppm) |
| ${}^{46}$K | 46 | 27 | L?-pending | binding_energy | — | 391.8300 | — | 42803.5952 MeV (-227.0 ppm) |
| ${}^{47}$K | 47 | 28 | L?-pending | binding_energy | — | 400.1993 | — | 43734.7910 MeV (-222.2 ppm) |
| ${}^{48}$K | 48 | 29 | L?-pending | binding_energy | — | 404.8432 | — | 44669.7124 MeV (-217.6 ppm) |
| ${}^{49}$K | 49 | 30 | L?-pending | binding_energy | — | 410.2415 | — | 45603.8793 MeV (-213.1 ppm) |
| ${}^{50}$K | 50 | 31 | L?-pending | binding_energy | — | 414.4292 | — | 46539.2568 MeV (-208.8 ppm) |
| ${}^{51}$K | 51 | 32 | L?-pending | binding_energy | — | 419.2881 | — | 47473.9630 MeV (-204.7 ppm) |
| ${}^{52}$K | 52 | 33 | L?-pending | binding_energy | — | 421.9816 | — | 48410.8347 MeV (-200.8 ppm) |
| ${}^{53}$K | 53 | 34 | L?-pending | binding_energy | — | 425.2110 | — | 49347.1705 MeV (-197.0 ppm) |
| ${}^{54}$K | 54 | 35 | L?-pending | binding_energy | — | 426.1140 | — | 50285.8327 MeV (-192.8 ppm) |
| ${}^{55}$K | 55 | 36 | L?-pending | binding_energy | — | 428.5600 | — | 51222.9518 MeV (-189.2 ppm) |
| ${}^{56}$K | 56 | 37 | L?-pending | binding_energy | — | 429.1280 | — | 52161.9490 MeV (-185.9 ppm) |
| ${}^{57}$K | 57 | 38 | L?-pending | binding_energy | — | 431.0910 | — | 53099.5512 MeV (-183.4 ppm) |
| ${}^{58}$K | 58 | 39 | L?-pending | binding_energy | — | 431.3460 | — | 54038.8614 MeV (-180.0 ppm) |
| ${}^{59}$K | 59 | 40 | L?-pending | binding_energy | — | 432.5880 | — | 54977.1846 MeV (-176.7 ppm) |

### Calcium (Z = 20)

_1 of 29 isotopes with a framework prediction; 29 of 29 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{33}$Ca | 33 | 13 | L?-pending | binding_energy | — | 219.6810 | — | 30760.1035 MeV (-332.5 ppm) |
| ${}^{34}$Ca | 34 | 14 | L?-pending | binding_energy | — | 243.8820 | — | 31675.4676 MeV (-322.6 ppm) |
| ${}^{35}$Ca | 35 | 15 | L?-pending | binding_energy | — | 261.6600 | — | 32597.2548 MeV (-313.7 ppm) |
| ${}^{36}$Ca | 36 | 16 | L?-pending | binding_energy | — | 281.3717 | — | 33517.1083 MeV (-305.1 ppm) |
| ${}^{37}$Ca | 37 | 17 | L?-pending | binding_energy | — | 296.1279 | — | 34441.9173 MeV (-296.9 ppm) |
| ${}^{38}$Ca | 38 | 18 | L?-pending | binding_energy | — | 313.1216 | — | 35364.4887 MeV (-289.2 ppm) |
| ${}^{39}$Ca | 39 | 19 | L?-pending | binding_energy | — | 326.4172 | — | 36290.7584 MeV (-281.8 ppm) |
| ${}^{40}$Ca | 40 | 20 | L2-alpha-cluster | binding_energy | 408.7713 | 342.0522 | +19.51 % | 37147.9694 MeV (-2067.1 ppm) |
| ${}^{41}$Ca | 41 | 21 | L?-pending | binding_energy | — | 350.4150 | — | 38145.8909 MeV (-268.1 ppm) |
| ${}^{42}$Ca | 42 | 22 | L?-pending | binding_energy | — | 361.8957 | — | 39073.9754 MeV (-261.7 ppm) |
| ${}^{43}$Ca | 43 | 23 | L?-pending | binding_energy | — | 369.8286 | — | 40005.6077 MeV (-255.6 ppm) |
| ${}^{44}$Ca | 44 | 24 | L?-pending | binding_energy | — | 380.9598 | — | 40934.0417 MeV (-249.9 ppm) |
| ${}^{45}$Ca | 45 | 25 | L?-pending | binding_energy | — | 388.3746 | — | 41866.1921 MeV (-244.3 ppm) |
| ${}^{46}$Ca | 46 | 26 | L?-pending | binding_energy | — | 398.7733 | — | 42795.3586 MeV (-239.0 ppm) |
| ${}^{47}$Ca | 47 | 27 | L?-pending | binding_energy | — | 406.0497 | — | 43727.6474 MeV (-233.9 ppm) |
| ${}^{48}$Ca | 48 | 28 | L?-pending | binding_energy | — | 416.0012 | — | 44657.2610 MeV (-229.0 ppm) |
| ${}^{49}$Ca | 49 | 29 | L?-pending | binding_energy | — | 421.1476 | — | 45591.6798 MeV (-224.4 ppm) |
| ${}^{50}$Ca | 50 | 30 | L?-pending | binding_energy | — | 427.5082 | — | 46524.8844 MeV (-219.9 ppm) |
| ${}^{51}$Ca | 51 | 31 | L?-pending | binding_energy | — | 432.3226 | — | 47459.6352 MeV (-215.5 ppm) |
| ${}^{52}$Ca | 52 | 32 | L?-pending | binding_energy | — | 438.3279 | — | 48393.1951 MeV (-211.4 ppm) |
| ${}^{53}$Ca | 53 | 33 | L?-pending | binding_energy | — | 441.5206 | — | 49329.5675 MeV (-207.4 ppm) |
| ${}^{54}$Ca | 54 | 34 | L?-pending | binding_energy | — | 445.3648 | — | 50265.2885 MeV (-203.5 ppm) |
| ${}^{55}$Ca | 55 | 35 | L?-pending | binding_energy | — | 446.9259 | — | 51203.2926 MeV (-199.8 ppm) |
| ${}^{56}$Ca | 56 | 36 | L?-pending | binding_energy | — | 449.8573 | — | 52139.9264 MeV (-196.2 ppm) |
| ${}^{57}$Ca | 57 | 37 | L?-pending | binding_energy | — | 450.9840 | — | 53078.3649 MeV (-192.9 ppm) |
| ${}^{58}$Ca | 58 | 38 | L?-pending | binding_energy | — | 454.0240 | — | 54014.8901 MeV (-189.5 ppm) |
| ${}^{59}$Ca | 59 | 39 | L?-pending | binding_energy | — | 454.7720 | — | 54953.7073 MeV (-186.6 ppm) |
| ${}^{60}$Ca | 60 | 40 | L?-pending | binding_energy | — | 457.6200 | — | 55890.4244 MeV (-182.9 ppm) |
| ${}^{61}$Ca | 61 | 41 | L?-pending | binding_energy | — | 457.6830 | — | 56829.9266 MeV (-179.9 ppm) |

### Scandium (Z = 21)

_0 of 29 isotopes with a framework prediction; 29 of 29 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{35}$Sc | 35 | 14 | L?-pending | binding_energy | — | 238.9800 | — | 32618.6415 MeV (-329.5 ppm) |
| ${}^{36}$Sc | 36 | 15 | L?-pending | binding_energy | — | 257.9760 | — | 33539.2107 MeV (-319.7 ppm) |
| ${}^{37}$Sc | 37 | 16 | L?-pending | binding_energy | — | 278.4250 | — | 34458.3269 MeV (-311.4 ppm) |
| ${}^{38}$Sc | 38 | 17 | L?-pending | binding_energy | — | 294.5380 | — | 35381.7790 MeV (-303.7 ppm) |
| ${}^{39}$Sc | 39 | 18 | L?-pending | binding_energy | — | 312.5248 | — | 36303.3574 MeV (-295.7 ppm) |
| ${}^{40}$Sc | 40 | 19 | L?-pending | binding_energy | — | 326.9468 | — | 37228.5006 MeV (-288.4 ppm) |
| ${}^{41}$Sc | 41 | 20 | L?-pending | binding_energy | — | 343.1371 | — | 38151.8755 MeV (-281.4 ppm) |
| ${}^{42}$Sc | 42 | 21 | L?-pending | binding_energy | — | 354.6871 | — | 39079.8907 MeV (-274.8 ppm) |
| ${}^{43}$Sc | 43 | 22 | L?-pending | binding_energy | — | 366.8255 | — | 40007.3174 MeV (-268.4 ppm) |
| ${}^{44}$Sc | 44 | 23 | L?-pending | binding_energy | — | 376.5247 | — | 40937.1834 MeV (-262.3 ppm) |
| ${}^{45}$Sc | 45 | 24 | L?-pending | binding_energy | — | 387.8523 | — | 41865.4210 MeV (-256.5 ppm) |
| ${}^{46}$Sc | 46 | 25 | L?-pending | binding_energy | — | 396.6130 | — | 42796.2255 MeV (-250.9 ppm) |
| ${}^{47}$Sc | 47 | 26 | L?-pending | binding_energy | — | 407.2595 | — | 43725.1442 MeV (-245.6 ppm) |
| ${}^{48}$Sc | 48 | 27 | L?-pending | binding_energy | — | 415.4981 | — | 44656.4708 MeV (-240.5 ppm) |
| ${}^{49}$Sc | 49 | 28 | L?-pending | binding_energy | — | 425.6277 | — | 45585.9063 MeV (-235.6 ppm) |
| ${}^{50}$Sc | 50 | 29 | L?-pending | binding_energy | — | 431.6737 | — | 46519.4255 MeV (-230.9 ppm) |
| ${}^{51}$Sc | 51 | 30 | L?-pending | binding_energy | — | 438.4583 | — | 47452.2062 MeV (-226.3 ppm) |
| ${}^{52}$Sc | 52 | 31 | L?-pending | binding_energy | — | 443.8028 | — | 48386.4268 MeV (-222.0 ppm) |
| ${}^{53}$Sc | 53 | 32 | L?-pending | binding_energy | — | 450.1201 | — | 49319.6747 MeV (-217.8 ppm) |
| ${}^{54}$Sc | 54 | 33 | L?-pending | binding_energy | — | 453.8598 | — | 50255.5002 MeV (-213.7 ppm) |
| ${}^{55}$Sc | 55 | 34 | L?-pending | binding_energy | — | 458.3353 | — | 51190.5899 MeV (-209.8 ppm) |
| ${}^{56}$Sc | 56 | 35 | L?-pending | binding_energy | — | 461.0804 | — | 52127.4100 MeV (-206.1 ppm) |
| ${}^{57}$Sc | 57 | 36 | L?-pending | binding_energy | — | 465.0155 | — | 53063.0401 MeV (-202.4 ppm) |
| ${}^{58}$Sc | 58 | 37 | L?-pending | binding_energy | — | 467.1867 | — | 54000.4340 MeV (-198.9 ppm) |
| ${}^{59}$Sc | 59 | 38 | L?-pending | binding_energy | — | 470.6080 | — | 54936.5779 MeV (-195.5 ppm) |
| ${}^{60}$Sc | 60 | 39 | L?-pending | binding_energy | — | 472.3800 | — | 55874.3711 MeV (-191.9 ppm) |
| ${}^{61}$Sc | 61 | 40 | L?-pending | binding_energy | — | 475.4340 | — | 56810.8823 MeV (-189.3 ppm) |
| ${}^{62}$Sc | 62 | 41 | L?-pending | binding_energy | — | 476.6560 | — | 57749.2255 MeV (-185.6 ppm) |
| ${}^{63}$Sc | 63 | 42 | L?-pending | binding_energy | — | 478.9890 | — | 58686.4577 MeV (-183.0 ppm) |

### Titanium (Z = 22)

_0 of 29 isotopes with a framework prediction; 29 of 29 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{37}$Ti | 37 | 15 | L?-pending | binding_energy | — | 256.2620 | — | 34479.1965 MeV (-326.3 ppm) |
| ${}^{38}$Ti | 38 | 16 | L?-pending | binding_energy | — | 278.1220 | — | 35396.9017 MeV (-317.6 ppm) |
| ${}^{39}$Ti | 39 | 17 | L?-pending | binding_energy | — | 295.0740 | — | 36319.5149 MeV (-309.8 ppm) |
| ${}^{40}$Ti | 40 | 18 | L?-pending | binding_energy | — | 314.6345 | — | 37239.5196 MeV (-302.0 ppm) |
| ${}^{41}$Ti | 41 | 19 | L?-pending | binding_energy | — | 329.4099 | — | 38164.3093 MeV (-294.7 ppm) |
| ${}^{42}$Ti | 42 | 20 | L?-pending | binding_energy | — | 346.8881 | — | 39086.3964 MeV (-287.8 ppm) |
| ${}^{43}$Ti | 43 | 21 | L?-pending | binding_energy | — | 359.1706 | — | 40013.6790 MeV (-281.1 ppm) |
| ${}^{44}$Ti | 44 | 22 | L?-pending | binding_energy | — | 375.4749 | — | 40936.9399 MeV (-274.8 ppm) |
| ${}^{45}$Ti | 45 | 23 | L?-pending | binding_energy | — | 385.0079 | — | 41866.9721 MeV (-268.7 ppm) |
| ${}^{46}$Ti | 46 | 24 | L?-pending | binding_energy | — | 398.1973 | — | 42793.3479 MeV (-262.9 ppm) |
| ${}^{47}$Ti | 47 | 25 | L?-pending | binding_energy | — | 407.0779 | — | 43724.0324 MeV (-257.3 ppm) |
| ${}^{48}$Ti | 48 | 26 | L?-pending | binding_energy | — | 418.7046 | — | 44651.9710 MeV (-252.0 ppm) |
| ${}^{49}$Ti | 49 | 27 | L?-pending | binding_energy | — | 426.8470 | — | 45583.3938 MeV (-246.8 ppm) |
| ${}^{50}$Ti | 50 | 28 | L?-pending | binding_energy | — | 437.7861 | — | 46512.0198 MeV (-241.9 ppm) |
| ${}^{51}$Ti | 51 | 29 | L?-pending | binding_energy | — | 444.1586 | — | 47445.2126 MeV (-237.1 ppm) |
| ${}^{52}$Ti | 52 | 30 | L?-pending | binding_energy | — | 451.9746 | — | 48376.9617 MeV (-232.6 ppm) |
| ${}^{53}$Ti | 53 | 31 | L?-pending | binding_energy | — | 457.4497 | — | 49311.0518 MeV (-228.2 ppm) |
| ${}^{54}$Ti | 54 | 32 | L?-pending | binding_energy | — | 464.3834 | — | 50243.6833 MeV (-223.9 ppm) |
| ${}^{55}$Ti | 55 | 33 | L?-pending | binding_energy | — | 468.5433 | — | 51179.0885 MeV (-219.9 ppm) |
| ${}^{56}$Ti | 56 | 34 | L?-pending | binding_energy | — | 474.2052 | — | 52112.9919 MeV (-215.9 ppm) |
| ${}^{57}$Ti | 57 | 35 | L?-pending | binding_energy | — | 477.2553 | — | 53049.5069 MeV (-212.1 ppm) |
| ${}^{58}$Ti | 58 | 36 | L?-pending | binding_energy | — | 481.8425 | — | 53984.4849 MeV (-208.4 ppm) |
| ${}^{59}$Ti | 59 | 37 | L?-pending | binding_energy | — | 484.8620 | — | 54921.0306 MeV (-204.6 ppm) |
| ${}^{60}$Ti | 60 | 38 | L?-pending | binding_energy | — | 489.1671 | — | 55856.2906 MeV (-201.5 ppm) |
| ${}^{61}$Ti | 61 | 39 | L?-pending | binding_energy | — | 491.5380 | — | 56793.4850 MeV (-198.7 ppm) |
| ${}^{62}$Ti | 62 | 40 | L?-pending | binding_energy | — | 495.3800 | — | 57729.2081 MeV (-194.4 ppm) |
| ${}^{63}$Ti | 63 | 41 | L?-pending | binding_energy | — | 497.1330 | — | 58667.0203 MeV (-191.7 ppm) |
| ${}^{64}$Ti | 64 | 42 | L?-pending | binding_energy | — | 500.8640 | — | 59602.8545 MeV (-189.3 ppm) |
| ${}^{65}$Ti | 65 | 43 | L?-pending | binding_energy | — | 502.1900 | — | 60541.0937 MeV (-185.5 ppm) |

### Vanadium (Z = 23)

_0 of 29 isotopes with a framework prediction; 29 of 29 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{39}$V | 39 | 16 | L?-pending | binding_energy | — | 274.2090 | — | 36339.0866 MeV (-323.3 ppm) |
| ${}^{40}$V | 40 | 17 | L?-pending | binding_energy | — | 292.4000 | — | 37260.4607 MeV (-315.9 ppm) |
| ${}^{41}$V | 41 | 18 | L?-pending | binding_energy | — | 312.6250 | — | 38179.8009 MeV (-308.1 ppm) |
| ${}^{42}$V | 42 | 19 | L?-pending | binding_energy | — | 328.6080 | — | 39103.3831 MeV (-300.4 ppm) |
| ${}^{43}$V | 43 | 20 | L?-pending | binding_energy | — | 346.9891 | — | 40024.5672 MeV (-293.8 ppm) |
| ${}^{44}$V | 44 | 21 | L?-pending | binding_energy | — | 360.9521 | — | 40950.1694 MeV (-287.2 ppm) |
| ${}^{45}$V | 45 | 22 | L?-pending | binding_energy | — | 377.1018 | — | 41873.5849 MeV (-280.8 ppm) |
| ${}^{46}$V | 46 | 23 | L?-pending | binding_energy | — | 390.3625 | — | 42799.8893 MeV (-274.8 ppm) |
| ${}^{47}$V | 47 | 24 | L?-pending | binding_energy | — | 403.3650 | — | 43726.4520 MeV (-269.0 ppm) |
| ${}^{48}$V | 48 | 25 | L?-pending | binding_energy | — | 413.9073 | — | 44655.4749 MeV (-263.4 ppm) |
| ${}^{49}$V | 49 | 26 | L?-pending | binding_energy | — | 425.4628 | — | 45583.4847 MeV (-258.0 ppm) |
| ${}^{50}$V | 50 | 27 | L?-pending | binding_energy | — | 434.7952 | — | 46513.7174 MeV (-252.9 ppm) |
| ${}^{51}$V | 51 | 28 | L?-pending | binding_energy | — | 445.8463 | — | 47442.2314 MeV (-247.9 ppm) |
| ${}^{52}$V | 52 | 29 | L?-pending | binding_energy | — | 453.1576 | — | 48374.4854 MeV (-243.1 ppm) |
| ${}^{53}$V | 53 | 30 | L?-pending | binding_energy | — | 461.6376 | — | 49305.5706 MeV (-238.6 ppm) |
| ${}^{54}$V | 54 | 31 | L?-pending | binding_energy | — | 467.7555 | — | 50239.0179 MeV (-234.1 ppm) |
| ${}^{55}$V | 55 | 32 | L?-pending | binding_energy | — | 475.0537 | — | 51171.2849 MeV (-229.9 ppm) |
| ${}^{56}$V | 56 | 33 | L?-pending | binding_energy | — | 480.1832 | — | 52105.7205 MeV (-225.8 ppm) |
| ${}^{57}$V | 57 | 34 | L?-pending | binding_energy | — | 486.5062 | — | 53038.9627 MeV (-221.8 ppm) |
| ${}^{58}$V | 58 | 35 | L?-pending | binding_energy | — | 490.5730 | — | 53974.4610 MeV (-218.0 ppm) |
| ${}^{59}$V | 59 | 36 | L?-pending | binding_energy | — | 495.8244 | — | 54908.7749 MeV (-214.2 ppm) |
| ${}^{60}$V | 60 | 37 | L?-pending | binding_energy | — | 499.3725 | — | 55844.7919 MeV (-210.7 ppm) |
| ${}^{61}$V | 61 | 38 | L?-pending | binding_energy | — | 504.5335 | — | 56779.1961 MeV (-207.2 ppm) |
| ${}^{62}$V | 62 | 39 | L?-pending | binding_energy | — | 507.6409 | — | 57715.6539 MeV (-203.8 ppm) |
| ${}^{63}$V | 63 | 40 | L?-pending | binding_energy | — | 512.2392 | — | 58650.6208 MeV (-200.6 ppm) |
| ${}^{64}$V | 64 | 41 | L?-pending | binding_energy | — | 514.8800 | — | 59587.5452 MeV (-197.3 ppm) |
| ${}^{65}$V | 65 | 42 | L?-pending | binding_energy | — | 518.7650 | — | 60523.2254 MeV (-194.6 ppm) |
| ${}^{66}$V | 66 | 43 | L?-pending | binding_energy | — | 521.0040 | — | 61460.5516 MeV (-191.3 ppm) |
| ${}^{67}$V | 67 | 44 | L?-pending | binding_energy | — | 524.5430 | — | 62396.5777 MeV (-188.8 ppm) |

### Chromium (Z = 24)

_0 of 30 isotopes with a framework prediction; 30 of 30 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{41}$Cr | 41 | 17 | L?-pending | binding_energy | — | 291.7560 | — | 38199.3766 MeV (-321.7 ppm) |
| ${}^{42}$Cr | 42 | 18 | L?-pending | binding_energy | — | 313.1520 | — | 39117.5458 MeV (-313.5 ppm) |
| ${}^{43}$Cr | 43 | 19 | L?-pending | binding_energy | — | 330.2400 | — | 40040.0230 MeV (-305.9 ppm) |
| ${}^{44}$Cr | 44 | 20 | L?-pending | binding_energy | — | 349.7836 | — | 40960.0446 MeV (-299.6 ppm) |
| ${}^{45}$Cr | 45 | 21 | L?-pending | binding_energy | — | 363.9478 | — | 41885.4456 MeV (-293.0 ppm) |
| ${}^{46}$Cr | 46 | 22 | L?-pending | binding_energy | — | 381.9759 | — | 42806.9827 MeV (-286.7 ppm) |
| ${}^{47}$Cr | 47 | 23 | L?-pending | binding_energy | — | 395.1387 | — | 43733.3850 MeV (-280.6 ppm) |
| ${}^{48}$Cr | 48 | 24 | L?-pending | binding_energy | — | 411.4683 | — | 44656.6206 MeV (-274.8 ppm) |
| ${}^{49}$Cr | 49 | 25 | L?-pending | binding_energy | — | 422.0506 | — | 45585.6035 MeV (-269.2 ppm) |
| ${}^{50}$Cr | 50 | 26 | L?-pending | binding_energy | — | 435.0509 | — | 46512.1683 MeV (-263.8 ppm) |
| ${}^{51}$Cr | 51 | 27 | L?-pending | binding_energy | — | 444.3116 | — | 47442.4728 MeV (-258.7 ppm) |
| ${}^{52}$Cr | 52 | 28 | L?-pending | binding_energy | — | 456.3517 | — | 48369.9979 MeV (-253.7 ppm) |
| ${}^{53}$Cr | 53 | 29 | L?-pending | binding_energy | — | 464.2911 | — | 49301.6237 MeV (-248.9 ppm) |
| ${}^{54}$Cr | 54 | 30 | L?-pending | binding_energy | — | 474.0102 | — | 50231.4698 MeV (-244.3 ppm) |
| ${}^{55}$Cr | 55 | 31 | L?-pending | binding_energy | — | 480.2565 | — | 51164.7887 MeV (-239.9 ppm) |
| ${}^{56}$Cr | 56 | 32 | L?-pending | binding_energy | — | 488.5026 | — | 52096.1078 MeV (-235.6 ppm) |
| ${}^{57}$Cr | 57 | 33 | L?-pending | binding_energy | — | 493.8138 | — | 53030.3618 MeV (-231.5 ppm) |
| ${}^{58}$Cr | 58 | 34 | L?-pending | binding_energy | — | 501.3519 | — | 53962.3888 MeV (-227.5 ppm) |
| ${}^{59}$Cr | 59 | 35 | L?-pending | binding_energy | — | 505.5474 | — | 54897.7586 MeV (-223.6 ppm) |
| ${}^{60}$Cr | 60 | 36 | L?-pending | binding_energy | — | 512.4113 | — | 55830.4599 MeV (-219.9 ppm) |
| ${}^{61}$Cr | 61 | 37 | L?-pending | binding_energy | — | 516.0706 | — | 56766.3657 MeV (-216.2 ppm) |
| ${}^{62}$Cr | 62 | 38 | L?-pending | binding_energy | — | 522.4980 | — | 57699.5035 MeV (-212.8 ppm) |
| ${}^{63}$Cr | 63 | 39 | L?-pending | binding_energy | — | 525.8950 | — | 58635.6717 MeV (-209.4 ppm) |
| ${}^{64}$Cr | 64 | 40 | L?-pending | binding_energy | — | 531.4280 | — | 59569.7038 MeV (-206.1 ppm) |
| ${}^{65}$Cr | 65 | 41 | L?-pending | binding_energy | — | 534.1700 | — | 60506.5270 MeV (-202.9 ppm) |
| ${}^{66}$Cr | 66 | 42 | L?-pending | binding_energy | — | 539.0880 | — | 61441.1742 MeV (-200.1 ppm) |
| ${}^{67}$Cr | 67 | 43 | L?-pending | binding_energy | — | 541.2930 | — | 62378.5344 MeV (-197.2 ppm) |
| ${}^{68}$Cr | 68 | 44 | L?-pending | binding_energy | — | 545.7680 | — | 63313.6246 MeV (-194.0 ppm) |
| ${}^{69}$Cr | 69 | 45 | L?-pending | binding_energy | — | 547.7910 | — | 64251.1668 MeV (-191.3 ppm) |
| ${}^{70}$Cr | 70 | 46 | L?-pending | binding_energy | — | 551.8800 | — | 65186.6430 MeV (-188.7 ppm) |

### Manganese (Z = 25)

_0 of 31 isotopes with a framework prediction; 31 of 31 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{43}$Mn | 43 | 18 | L?-pending | binding_energy | — | 310.1590 | — | 40058.8106 MeV (-319.6 ppm) |
| ${}^{44}$Mn | 44 | 19 | L?-pending | binding_energy | — | 328.1080 | — | 40980.4268 MeV (-311.6 ppm) |
| ${}^{45}$Mn | 45 | 20 | L?-pending | binding_energy | — | 348.6150 | — | 41899.4850 MeV (-304.7 ppm) |
| ${}^{46}$Mn | 46 | 21 | L?-pending | binding_energy | — | 364.1397 | — | 42823.5255 MeV (-298.5 ppm) |
| ${}^{47}$Mn | 47 | 22 | L?-pending | binding_energy | — | 382.3596 | — | 43744.8707 MeV (-292.2 ppm) |
| ${}^{48}$Mn | 48 | 23 | L?-pending | binding_energy | — | 397.1612 | — | 44669.6343 MeV (-286.2 ppm) |
| ${}^{49}$Mn | 49 | 24 | L?-pending | binding_energy | — | 413.5558 | — | 45592.8049 MeV (-280.4 ppm) |
| ${}^{50}$Mn | 50 | 25 | L?-pending | binding_energy | — | 426.6341 | — | 46519.2918 MeV (-274.8 ppm) |
| ${}^{51}$Mn | 51 | 26 | L?-pending | binding_energy | — | 440.3218 | — | 47445.1693 MeV (-269.4 ppm) |
| ${}^{52}$Mn | 52 | 27 | L?-pending | binding_energy | — | 450.8613 | — | 48374.1950 MeV (-264.3 ppm) |
| ${}^{53}$Mn | 53 | 28 | L?-pending | binding_energy | — | 462.9115 | — | 49301.7100 MeV (-259.3 ppm) |
| ${}^{54}$Mn | 54 | 29 | L?-pending | binding_energy | — | 471.8507 | — | 50232.3359 MeV (-254.5 ppm) |
| ${}^{55}$Mn | 55 | 30 | L?-pending | binding_energy | — | 482.0764 | — | 51161.6755 MeV (-249.9 ppm) |
| ${}^{56}$Mn | 56 | 31 | L?-pending | binding_energy | — | 489.3468 | — | 52093.9702 MeV (-245.4 ppm) |
| ${}^{57}$Mn | 57 | 32 | L?-pending | binding_energy | — | 497.9927 | — | 53024.8895 MeV (-241.1 ppm) |
| ${}^{58}$Mn | 58 | 33 | L?-pending | binding_energy | — | 504.4053 | — | 53958.0421 MeV (-236.9 ppm) |
| ${}^{59}$Mn | 59 | 34 | L?-pending | binding_energy | — | 512.1744 | — | 54889.8382 MeV (-232.9 ppm) |
| ${}^{60}$Mn | 60 | 35 | L?-pending | binding_energy | — | 517.6884 | — | 55823.8894 MeV (-229.0 ppm) |
| ${}^{61}$Mn | 61 | 36 | L?-pending | binding_energy | — | 524.5339 | — | 56756.6091 MeV (-225.3 ppm) |
| ${}^{62}$Mn | 62 | 37 | L?-pending | binding_energy | — | 529.3870 | — | 57691.3211 MeV (-221.6 ppm) |
| ${}^{63}$Mn | 63 | 38 | L?-pending | binding_energy | — | 535.8214 | — | 58624.4519 MeV (-218.1 ppm) |
| ${}^{64}$Mn | 64 | 39 | L?-pending | binding_energy | — | 539.9947 | — | 59559.8438 MeV (-214.7 ppm) |
| ${}^{65}$Mn | 65 | 40 | L?-pending | binding_energy | — | 546.0443 | — | 60493.3594 MeV (-211.4 ppm) |
| ${}^{66}$Mn | 66 | 41 | L?-pending | binding_energy | — | 549.8987 | — | 61429.0702 MeV (-208.2 ppm) |
| ${}^{67}$Mn | 67 | 42 | L?-pending | binding_energy | — | 554.8270 | — | 62363.7071 MeV (-205.5 ppm) |
| ${}^{68}$Mn | 68 | 43 | L?-pending | binding_energy | — | 558.2120 | — | 63299.8873 MeV (-202.0 ppm) |
| ${}^{69}$Mn | 69 | 44 | L?-pending | binding_energy | — | 562.6950 | — | 64234.9694 MeV (-198.7 ppm) |
| ${}^{70}$Mn | 70 | 45 | L?-pending | binding_energy | — | 565.8800 | — | 65171.3496 MeV (-196.2 ppm) |
| ${}^{71}$Mn | 71 | 46 | L?-pending | binding_energy | — | 570.1300 | — | 66106.6648 MeV (-193.5 ppm) |
| ${}^{72}$Mn | 72 | 47 | L?-pending | binding_energy | — | 572.7600 | — | 67043.6000 MeV (-191.0 ppm) |
| ${}^{73}$Mn | 73 | 48 | L?-pending | binding_energy | — | 576.3350 | — | 67979.5902 MeV (-187.9 ppm) |

### Iron (Z = 26)

_0 of 32 isotopes with a framework prediction; 32 of 32 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{45}$Fe | 45 | 19 | L?-pending | binding_energy | — | 328.4550 | — | 41918.3517 MeV (-317.0 ppm) |
| ${}^{46}$Fe | 46 | 20 | L?-pending | binding_energy | — | 349.7380 | — | 42836.6339 MeV (-310.5 ppm) |
| ${}^{47}$Fe | 47 | 21 | L?-pending | binding_energy | — | 366.1300 | — | 43759.8070 MeV (-303.5 ppm) |
| ${}^{48}$Fe | 48 | 22 | L?-pending | binding_energy | — | 385.0908 | — | 44680.4114 MeV (-297.5 ppm) |
| ${}^{49}$Fe | 49 | 23 | L?-pending | binding_energy | — | 399.9043 | — | 45605.1631 MeV (-291.5 ppm) |
| ${}^{50}$Fe | 50 | 24 | L?-pending | binding_energy | — | 417.7013 | — | 46526.9313 MeV (-285.7 ppm) |
| ${}^{51}$Fe | 51 | 25 | L?-pending | binding_energy | — | 431.4854 | — | 47452.7124 MeV (-280.2 ppm) |
| ${}^{52}$Fe | 52 | 26 | L?-pending | binding_energy | — | 447.6996 | — | 48376.0634 MeV (-274.8 ppm) |
| ${}^{53}$Fe | 53 | 27 | L?-pending | binding_energy | — | 458.3863 | — | 49304.9418 MeV (-269.6 ppm) |
| ${}^{54}$Fe | 54 | 28 | L?-pending | binding_energy | — | 471.7648 | — | 50231.1286 MeV (-264.7 ppm) |
| ${}^{55}$Fe | 55 | 29 | L?-pending | binding_energy | — | 481.0629 | — | 51161.3956 MeV (-259.9 ppm) |
| ${}^{56}$Fe | 56 | 30 | L?-pending | binding_energy | — | 492.2600 | — | 52089.7638 MeV (-255.2 ppm) |
| ${}^{57}$Fe | 57 | 31 | L?-pending | binding_energy | — | 499.9061 | — | 53021.6828 MeV (-250.8 ppm) |
| ${}^{58}$Fe | 58 | 32 | L?-pending | binding_energy | — | 509.9507 | — | 53951.2034 MeV (-246.4 ppm) |
| ${}^{59}$Fe | 59 | 33 | L?-pending | binding_energy | — | 516.5317 | — | 54884.1876 MeV (-242.3 ppm) |
| ${}^{60}$Fe | 60 | 34 | L?-pending | binding_energy | — | 525.3512 | — | 55814.9332 MeV (-238.2 ppm) |
| ${}^{61}$Fe | 61 | 35 | L?-pending | binding_energy | — | 530.9299 | — | 56748.9197 MeV (-234.3 ppm) |
| ${}^{62}$Fe | 62 | 36 | L?-pending | binding_energy | — | 538.9588 | — | 57680.4561 MeV (-230.5 ppm) |
| ${}^{63}$Fe | 63 | 37 | L?-pending | binding_energy | — | 543.7876 | — | 58615.1924 MeV (-226.9 ppm) |
| ${}^{64}$Fe | 64 | 38 | L?-pending | binding_energy | — | 551.1929 | — | 59547.3523 MeV (-223.3 ppm) |
| ${}^{65}$Fe | 65 | 39 | L?-pending | binding_energy | — | 555.5126 | — | 60482.5978 MeV (-219.9 ppm) |
| ${}^{66}$Fe | 66 | 40 | L?-pending | binding_energy | — | 562.4338 | — | 61415.2417 MeV (-216.5 ppm) |
| ${}^{67}$Fe | 67 | 41 | L?-pending | binding_energy | — | 566.1457 | — | 62351.0950 MeV (-213.3 ppm) |
| ${}^{68}$Fe | 68 | 42 | L?-pending | binding_energy | — | 572.4240 | — | 63284.3819 MeV (-210.4 ppm) |
| ${}^{69}$Fe | 69 | 43 | L?-pending | binding_energy | — | 575.8050 | — | 64220.5661 MeV (-207.5 ppm) |
| ${}^{70}$Fe | 70 | 44 | L?-pending | binding_energy | — | 581.5600 | — | 65154.3763 MeV (-204.4 ppm) |
| ${}^{71}$Fe | 71 | 45 | L?-pending | binding_energy | — | 584.6850 | — | 66090.8165 MeV (-201.7 ppm) |
| ${}^{72}$Fe | 72 | 46 | L?-pending | binding_energy | — | 590.0400 | — | 67025.0267 MeV (-198.4 ppm) |
| ${}^{73}$Fe | 73 | 47 | L?-pending | binding_energy | — | 592.8330 | — | 67961.7988 MeV (-195.4 ppm) |
| ${}^{74}$Fe | 74 | 48 | L?-pending | binding_energy | — | 597.6240 | — | 68896.5730 MeV (-193.5 ppm) |
| ${}^{75}$Fe | 75 | 49 | L?-pending | binding_energy | — | 599.7000 | — | 69834.0622 MeV (-190.4 ppm) |
| ${}^{76}$Fe | 76 | 50 | L?-pending | binding_energy | — | 603.6680 | — | 70769.6594 MeV (-187.9 ppm) |

### Cobalt (Z = 27)

_0 of 32 isotopes with a framework prediction; 32 of 32 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{47}$Co | 47 | 20 | L?-pending | binding_energy | — | 347.6120 | — | 43777.0317 MeV (-315.4 ppm) |
| ${}^{48}$Co | 48 | 21 | L?-pending | binding_energy | — | 364.5600 | — | 44699.6489 MeV (-308.6 ppm) |
| ${}^{49}$Co | 49 | 22 | L?-pending | binding_energy | — | 384.1600 | — | 45619.6141 MeV (-302.8 ppm) |
| ${}^{50}$Co | 50 | 23 | L?-pending | binding_energy | — | 400.0319 | — | 46543.3073 MeV (-296.6 ppm) |
| ${}^{51}$Co | 51 | 24 | L?-pending | binding_energy | — | 417.8560 | — | 47465.0485 MeV (-290.8 ppm) |
| ${}^{52}$Co | 52 | 25 | L?-pending | binding_energy | — | 432.9292 | — | 48389.5405 MeV (-285.3 ppm) |
| ${}^{53}$Co | 53 | 26 | L?-pending | binding_energy | — | 449.3159 | — | 49312.7190 MeV (-280.0 ppm) |
| ${}^{54}$Co | 54 | 27 | L?-pending | binding_energy | — | 462.7379 | — | 50238.8621 MeV (-274.8 ppm) |
| ${}^{55}$Co | 55 | 28 | L?-pending | binding_energy | — | 476.8291 | — | 51164.3361 MeV (-269.8 ppm) |
| ${}^{56}$Co | 56 | 29 | L?-pending | binding_energy | — | 486.9110 | — | 52093.8194 MeV (-265.0 ppm) |
| ${}^{57}$Co | 57 | 30 | L?-pending | binding_energy | — | 498.2874 | — | 53022.0081 MeV (-260.4 ppm) |
| ${}^{58}$Co | 58 | 31 | L?-pending | binding_energy | — | 506.8604 | — | 53953.0004 MeV (-255.9 ppm) |
| ${}^{59}$Co | 59 | 32 | L?-pending | binding_energy | — | 517.3142 | — | 54882.1117 MeV (-251.6 ppm) |
| ${}^{60}$Co | 60 | 33 | L?-pending | binding_energy | — | 524.8062 | — | 55814.1850 MeV (-247.4 ppm) |
| ${}^{61}$Co | 61 | 34 | L?-pending | binding_energy | — | 534.1252 | — | 56744.4311 MeV (-243.3 ppm) |
| ${}^{62}$Co | 62 | 35 | L?-pending | binding_energy | — | 540.7228 | — | 57677.3987 MeV (-239.4 ppm) |
| ${}^{63}$Co | 63 | 36 | L?-pending | binding_energy | — | 549.2212 | — | 58608.4654 MeV (-235.6 ppm) |
| ${}^{64}$Co | 64 | 37 | L?-pending | binding_energy | — | 555.2334 | — | 59542.0184 MeV (-231.9 ppm) |
| ${}^{65}$Co | 65 | 38 | L?-pending | binding_energy | — | 562.6975 | — | 60474.1195 MeV (-228.3 ppm) |
| ${}^{66}$Co | 66 | 39 | L?-pending | binding_energy | — | 567.9922 | — | 61408.3901 MeV (-224.9 ppm) |
| ${}^{67}$Co | 67 | 40 | L?-pending | binding_energy | — | 574.9767 | — | 62340.9707 MeV (-221.5 ppm) |
| ${}^{68}$Co | 68 | 41 | L?-pending | binding_energy | — | 579.3688 | — | 63276.1437 MeV (-218.2 ppm) |
| ${}^{69}$Co | 69 | 42 | L?-pending | binding_energy | — | 586.1830 | — | 64208.8947 MeV (-215.1 ppm) |
| ${}^{70}$Co | 70 | 43 | L?-pending | binding_energy | — | 590.3939 | — | 65144.2491 MeV (-212.0 ppm) |
| ${}^{71}$Co | 71 | 44 | L?-pending | binding_energy | — | 596.3101 | — | 66077.8980 MeV (-209.0 ppm) |
| ${}^{72}$Co | 72 | 45 | L?-pending | binding_energy | — | 600.3360 | — | 67013.4373 MeV (-206.5 ppm) |
| ${}^{73}$Co | 73 | 46 | L?-pending | binding_energy | — | 606.0460 | — | 67947.2925 MeV (-203.2 ppm) |
| ${}^{74}$Co | 74 | 47 | L?-pending | binding_energy | — | 609.6860 | — | 68883.2177 MeV (-200.4 ppm) |
| ${}^{75}$Co | 75 | 48 | L?-pending | binding_energy | — | 614.7750 | — | 69817.6939 MeV (-197.7 ppm) |
| ${}^{76}$Co | 76 | 49 | L?-pending | binding_energy | — | 617.9560 | — | 70754.0781 MeV (-195.2 ppm) |
| ${}^{77}$Co | 77 | 50 | L?-pending | binding_energy | — | 622.3140 | — | 71689.2853 MeV (-193.2 ppm) |
| ${}^{78}$Co | 78 | 51 | L?-pending | binding_energy | — | 623.7660 | — | 72627.3984 MeV (-190.3 ppm) |

### Nickel (Z = 28)

_0 of 35 isotopes with a framework prediction; 35 of 35 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{48}$Ni | 48 | 20 | L?-pending | binding_energy | — | 347.3280 | — | 44715.5876 MeV (-319.9 ppm) |
| ${}^{49}$Ni | 49 | 21 | L?-pending | binding_energy | — | 365.0500 | — | 45637.4308 MeV (-313.5 ppm) |
| ${}^{50}$Ni | 50 | 22 | L?-pending | binding_energy | — | 385.1000 | — | 46556.9459 MeV (-307.0 ppm) |
| ${}^{51}$Ni | 51 | 23 | L?-pending | binding_energy | — | 401.3700 | — | 47480.2411 MeV (-301.3 ppm) |
| ${}^{52}$Ni | 52 | 24 | L?-pending | binding_energy | — | 420.3627 | — | 48400.8136 MeV (-295.8 ppm) |
| ${}^{53}$Ni | 53 | 25 | L?-pending | binding_energy | — | 435.5050 | — | 49325.2365 MeV (-290.2 ppm) |
| ${}^{54}$Ni | 54 | 26 | L?-pending | binding_energy | — | 453.2238 | — | 50247.0829 MeV (-284.9 ppm) |
| ${}^{55}$Ni | 55 | 27 | L?-pending | binding_energy | — | 467.3527 | — | 51172.5191 MeV (-279.8 ppm) |
| ${}^{56}$Ni | 56 | 28 | L?-pending | binding_energy | — | 483.9957 | — | 52095.4413 MeV (-274.8 ppm) |
| ${}^{57}$Ni | 57 | 29 | L?-pending | binding_energy | — | 494.2434 | — | 53024.7589 MeV (-270.0 ppm) |
| ${}^{58}$Ni | 58 | 30 | L?-pending | binding_energy | — | 506.4596 | — | 53952.1078 MeV (-265.4 ppm) |
| ${}^{59}$Ni | 59 | 31 | L?-pending | binding_energy | — | 515.4589 | — | 54882.6737 MeV (-260.9 ppm) |
| ${}^{60}$Ni | 60 | 32 | L?-pending | binding_energy | — | 526.8466 | — | 55810.8512 MeV (-256.5 ppm) |
| ${}^{61}$Ni | 61 | 33 | L?-pending | binding_energy | — | 534.6667 | — | 56742.5963 MeV (-252.3 ppm) |
| ${}^{62}$Ni | 62 | 34 | L?-pending | binding_energy | — | 545.2624 | — | 57671.5657 MeV (-248.3 ppm) |
| ${}^{63}$Ni | 63 | 35 | L?-pending | binding_energy | — | 552.1002 | — | 58604.2931 MeV (-244.3 ppm) |
| ${}^{64}$Ni | 64 | 36 | L?-pending | binding_energy | — | 561.7577 | — | 59534.2008 MeV (-240.5 ppm) |
| ${}^{65}$Ni | 65 | 37 | L?-pending | binding_energy | — | 567.8558 | — | 60467.6680 MeV (-236.8 ppm) |
| ${}^{66}$Ni | 66 | 38 | L?-pending | binding_energy | — | 576.8076 | — | 61398.2813 MeV (-233.2 ppm) |
| ${}^{67}$Ni | 67 | 39 | L?-pending | binding_energy | — | 582.6153 | — | 62332.0388 MeV (-229.7 ppm) |
| ${}^{68}$Ni | 68 | 40 | L?-pending | binding_energy | — | 590.4077 | — | 63263.8115 MeV (-226.4 ppm) |
| ${}^{69}$Ni | 69 | 41 | L?-pending | binding_energy | — | 594.9939 | — | 64198.7906 MeV (-223.1 ppm) |
| ${}^{70}$Ni | 70 | 42 | L?-pending | binding_energy | — | 602.3004 | — | 65131.0492 MeV (-219.9 ppm) |
| ${}^{71}$Ni | 71 | 43 | L?-pending | binding_energy | — | 606.5641 | — | 66066.3507 MeV (-216.8 ppm) |
| ${}^{72}$Ni | 72 | 44 | L?-pending | binding_energy | — | 613.4552 | — | 66999.0247 MeV (-213.8 ppm) |
| ${}^{73}$Ni | 73 | 45 | L?-pending | binding_energy | — | 617.4087 | — | 67934.6365 MeV (-210.8 ppm) |
| ${}^{74}$Ni | 74 | 46 | L?-pending | binding_energy | — | 624.0420 | — | 68867.5684 MeV (-207.5 ppm) |
| ${}^{75}$Ni | 75 | 47 | L?-pending | binding_energy | — | 627.6750 | — | 69803.5006 MeV (-205.1 ppm) |
| ${}^{76}$Ni | 76 | 48 | L?-pending | binding_energy | — | 633.6880 | — | 70737.0527 MeV (-202.2 ppm) |
| ${}^{77}$Ni | 77 | 49 | L?-pending | binding_energy | — | 636.9440 | — | 71673.3619 MeV (-199.9 ppm) |
| ${}^{78}$Ni | 78 | 50 | L?-pending | binding_energy | — | 642.5640 | — | 72607.3071 MeV (-197.6 ppm) |
| ${}^{79}$Ni | 79 | 51 | L?-pending | binding_energy | — | 643.8500 | — | 73545.5863 MeV (-194.2 ppm) |
| ${}^{80}$Ni | 80 | 52 | L?-pending | binding_energy | — | 647.0400 | — | 74481.9615 MeV (-192.3 ppm) |
| ${}^{81}$Ni | 81 | 53 | L?-pending | binding_energy | — | 648.0000 | — | 75420.5667 MeV (-190.4 ppm) |
| ${}^{82}$Ni | 82 | 54 | L?-pending | binding_energy | — | 650.6700 | — | 76357.4618 MeV (-187.7 ppm) |

### Copper (Z = 29)

_0 of 33 isotopes with a framework prediction; 33 of 33 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{52}$Cu | 52 | 23 | L?-pending | binding_energy | — | 398.8920 | — | 48420.9910 MeV (-306.0 ppm) |
| ${}^{53}$Cu | 53 | 24 | L?-pending | binding_energy | — | 418.2230 | — | 49341.2252 MeV (-300.3 ppm) |
| ${}^{54}$Cu | 54 | 25 | L?-pending | binding_energy | — | 434.4300 | — | 50264.5833 MeV (-295.5 ppm) |
| ${}^{55}$Cu | 55 | 26 | L?-pending | binding_energy | — | 452.8698 | — | 51185.7087 MeV (-289.7 ppm) |
| ${}^{56}$Cu | 56 | 27 | L?-pending | binding_energy | — | 467.9355 | — | 52110.2082 MeV (-284.5 ppm) |
| ${}^{57}$Cu | 57 | 28 | L?-pending | binding_energy | — | 484.6861 | — | 53033.0228 MeV (-279.6 ppm) |
| ${}^{58}$Cu | 58 | 29 | L?-pending | binding_energy | — | 497.1162 | — | 53960.1578 MeV (-274.8 ppm) |
| ${}^{59}$Cu | 59 | 30 | L?-pending | binding_energy | — | 509.8782 | — | 54886.9611 MeV (-270.2 ppm) |
| ${}^{60}$Cu | 60 | 31 | L?-pending | binding_energy | — | 519.9363 | — | 55816.4682 MeV (-265.7 ppm) |
| ${}^{61}$Cu | 61 | 32 | L?-pending | binding_energy | — | 531.6464 | — | 56744.3232 MeV (-261.3 ppm) |
| ${}^{62}$Cu | 62 | 33 | L?-pending | binding_energy | — | 540.5212 | — | 57675.0136 MeV (-257.1 ppm) |
| ${}^{63}$Cu | 63 | 34 | L?-pending | binding_energy | — | 551.3848 | — | 58603.7152 MeV (-253.1 ppm) |
| ${}^{64}$Cu | 64 | 35 | L?-pending | binding_energy | — | 559.3007 | — | 59535.3645 MeV (-249.1 ppm) |
| ${}^{65}$Cu | 65 | 36 | L?-pending | binding_energy | — | 569.2113 | — | 60465.0191 MeV (-245.3 ppm) |
| ${}^{66}$Cu | 66 | 37 | L?-pending | binding_energy | — | 576.2772 | — | 61397.5183 MeV (-241.5 ppm) |
| ${}^{67}$Cu | 67 | 38 | L?-pending | binding_energy | — | 585.4098 | — | 62327.9509 MeV (-237.9 ppm) |
| ${}^{68}$Cu | 68 | 39 | L?-pending | binding_energy | — | 591.7286 | — | 63261.1973 MeV (-234.4 ppm) |
| ${}^{69}$Cu | 69 | 40 | L?-pending | binding_energy | — | 599.9691 | — | 64192.5220 MeV (-231.0 ppm) |
| ${}^{70}$Cu | 70 | 41 | L?-pending | binding_energy | — | 605.2806 | — | 65126.7757 MeV (-227.7 ppm) |
| ${}^{71}$Cu | 71 | 42 | L?-pending | binding_energy | — | 613.0867 | — | 66058.5348 MeV (-224.5 ppm) |
| ${}^{72}$Cu | 72 | 43 | L?-pending | binding_energy | — | 618.2298 | — | 66992.9568 MeV (-221.4 ppm) |
| ${}^{73}$Cu | 73 | 44 | L?-pending | binding_energy | — | 625.5056 | — | 67925.2462 MeV (-218.4 ppm) |
| ${}^{74}$Cu | 74 | 45 | L?-pending | binding_energy | — | 630.5957 | — | 68859.7214 MeV (-215.4 ppm) |
| ${}^{75}$Cu | 75 | 46 | L?-pending | binding_energy | — | 637.1310 | — | 69792.7512 MeV (-212.5 ppm) |
| ${}^{76}$Cu | 76 | 47 | L?-pending | binding_energy | — | 641.7137 | — | 70727.7337 MeV (-209.7 ppm) |
| ${}^{77}$Cu | 77 | 48 | L?-pending | binding_energy | — | 647.6663 | — | 71661.3463 MeV (-207.0 ppm) |
| ${}^{78}$Cu | 78 | 49 | L?-pending | binding_energy | — | 651.6642 | — | 72596.9136 MeV (-204.3 ppm) |
| ${}^{79}$Cu | 79 | 50 | L?-pending | binding_energy | — | 657.3541 | — | 73530.7889 MeV (-201.7 ppm) |
| ${}^{80}$Cu | 80 | 51 | L?-pending | binding_energy | — | 659.6800 | — | 74468.0281 MeV (-199.0 ppm) |
| ${}^{81}$Cu | 81 | 52 | L?-pending | binding_energy | — | 662.9850 | — | 75404.2883 MeV (-196.6 ppm) |
| ${}^{82}$Cu | 82 | 53 | L?-pending | binding_energy | — | 664.8560 | — | 76341.9825 MeV (-193.9 ppm) |
| ${}^{83}$Cu | 83 | 54 | L?-pending | binding_energy | — | 667.6520 | — | 77278.7517 MeV (-192.4 ppm) |
| ${}^{84}$Cu | 84 | 55 | L?-pending | binding_energy | — | 669.0600 | — | 78216.9089 MeV (-190.1 ppm) |

### Zinc (Z = 30)

_0 of 33 isotopes with a framework prediction; 33 of 33 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{54}$Zn | 54 | 24 | L?-pending | binding_energy | — | 418.0680 | — | 50279.6520 MeV (-304.8 ppm) |
| ${}^{55}$Zn | 55 | 25 | L?-pending | binding_energy | — | 434.7200 | — | 51202.5652 MeV (-299.5 ppm) |
| ${}^{56}$Zn | 56 | 26 | L?-pending | binding_energy | — | 453.9360 | — | 52122.9144 MeV (-294.7 ppm) |
| ${}^{57}$Zn | 57 | 27 | L?-pending | binding_energy | — | 469.1670 | — | 53047.2486 MeV (-289.6 ppm) |
| ${}^{58}$Zn | 58 | 28 | L?-pending | binding_energy | — | 486.9649 | — | 53969.0158 MeV (-284.2 ppm) |
| ${}^{59}$Zn | 59 | 29 | L?-pending | binding_energy | — | 499.9530 | — | 54895.5929 MeV (-279.4 ppm) |
| ${}^{60}$Zn | 60 | 30 | L?-pending | binding_energy | — | 514.9831 | — | 55820.1280 MeV (-274.8 ppm) |
| ${}^{61}$Zn | 61 | 31 | L?-pending | binding_energy | — | 525.2289 | — | 56749.4474 MeV (-270.3 ppm) |
| ${}^{62}$Zn | 62 | 32 | L?-pending | binding_energy | — | 538.1194 | — | 57676.1221 MeV (-266.0 ppm) |
| ${}^{63}$Zn | 63 | 33 | L?-pending | binding_energy | — | 547.2361 | — | 58606.5706 MeV (-261.8 ppm) |
| ${}^{64}$Zn | 64 | 34 | L?-pending | binding_energy | — | 559.0980 | — | 59534.2739 MeV (-257.7 ppm) |
| ${}^{65}$Zn | 65 | 35 | L?-pending | binding_energy | — | 567.0773 | — | 60465.8598 MeV (-253.7 ppm) |
| ${}^{66}$Zn | 66 | 36 | L?-pending | binding_energy | — | 578.1358 | — | 61394.3664 MeV (-249.9 ppm) |
| ${}^{67}$Zn | 67 | 37 | L?-pending | binding_energy | — | 585.1883 | — | 62326.8791 MeV (-246.1 ppm) |
| ${}^{68}$Zn | 68 | 38 | L?-pending | binding_energy | — | 595.3864 | — | 63256.2462 MeV (-242.5 ppm) |
| ${}^{69}$Zn | 69 | 39 | L?-pending | binding_energy | — | 601.8684 | — | 64189.3293 MeV (-239.0 ppm) |
| ${}^{70}$Zn | 70 | 40 | L?-pending | binding_energy | — | 611.0866 | — | 65119.6764 MeV (-235.6 ppm) |
| ${}^{71}$Zn | 71 | 41 | L?-pending | binding_energy | — | 616.9220 | — | 66053.4062 MeV (-232.3 ppm) |
| ${}^{72}$Zn | 72 | 42 | L?-pending | binding_energy | — | 625.8100 | — | 66984.0834 MeV (-229.1 ppm) |
| ${}^{73}$Zn | 73 | 43 | L?-pending | binding_energy | — | 631.3292 | — | 67918.1293 MeV (-225.9 ppm) |
| ${}^{74}$Zn | 74 | 44 | L?-pending | binding_energy | — | 639.5638 | — | 68849.4599 MeV (-222.9 ppm) |
| ${}^{75}$Zn | 75 | 45 | L?-pending | binding_energy | — | 644.4374 | — | 69784.1515 MeV (-219.9 ppm) |
| ${}^{76}$Zn | 76 | 46 | L?-pending | binding_energy | — | 652.2528 | — | 70715.9013 MeV (-217.0 ppm) |
| ${}^{77}$Zn | 77 | 47 | L?-pending | binding_energy | — | 656.8103 | — | 71650.9090 MeV (-214.2 ppm) |
| ${}^{78}$Zn | 78 | 48 | L?-pending | binding_energy | — | 663.5756 | — | 72583.7088 MeV (-211.4 ppm) |
| ${}^{79}$Zn | 79 | 49 | L?-pending | binding_energy | — | 667.5960 | — | 73519.2536 MeV (-208.7 ppm) |
| ${}^{80}$Zn | 80 | 50 | L?-pending | binding_energy | — | 673.8837 | — | 74452.5312 MeV (-206.1 ppm) |
| ${}^{81}$Zn | 81 | 51 | L?-pending | binding_energy | — | 676.5060 | — | 75389.4740 MeV (-203.5 ppm) |
| ${}^{82}$Zn | 82 | 52 | L?-pending | binding_energy | — | 680.6916 | — | 76324.8535 MeV (-201.1 ppm) |
| ${}^{83}$Zn | 83 | 53 | L?-pending | binding_energy | — | 682.7580 | — | 77262.3524 MeV (-198.9 ppm) |
| ${}^{84}$Zn | 84 | 54 | L?-pending | binding_energy | — | 686.3640 | — | 78198.3116 MeV (-196.4 ppm) |
| ${}^{85}$Zn | 85 | 55 | L?-pending | binding_energy | — | 687.6500 | — | 79136.5907 MeV (-193.4 ppm) |
| ${}^{86}$Zn | 86 | 56 | L?-pending | binding_energy | — | 690.7520 | — | 80073.0539 MeV (-192.0 ppm) |

### Gallium (Z = 31)

_0 of 33 isotopes with a framework prediction; 33 of 33 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{56}$Ga | 56 | 25 | L?-pending | binding_energy | — | 431.5920 | — | 52143.9650 MeV (-304.2 ppm) |
| ${}^{57}$Ga | 57 | 26 | L?-pending | binding_energy | — | 451.2120 | — | 53063.9102 MeV (-298.5 ppm) |
| ${}^{58}$Ga | 58 | 27 | L?-pending | binding_energy | — | 467.4220 | — | 53987.2654 MeV (-293.6 ppm) |
| ${}^{59}$Ga | 59 | 28 | L?-pending | binding_energy | — | 485.6880 | — | 54908.5646 MeV (-288.2 ppm) |
| ${}^{60}$Ga | 60 | 29 | L?-pending | binding_energy | — | 499.6200 | — | 55834.1978 MeV (-283.9 ppm) |
| ${}^{61}$Ga | 61 | 30 | L?-pending | binding_energy | — | 515.2323 | — | 56758.1507 MeV (-279.3 ppm) |
| ${}^{62}$Ga | 62 | 31 | L?-pending | binding_energy | — | 528.1560 | — | 57684.7922 MeV (-274.8 ppm) |
| ${}^{63}$Ga | 63 | 32 | L?-pending | binding_energy | — | 540.7874 | — | 58611.7260 MeV (-270.4 ppm) |
| ${}^{64}$Ga | 64 | 33 | L?-pending | binding_energy | — | 551.1444 | — | 59540.9341 MeV (-266.2 ppm) |
| ${}^{65}$Ga | 65 | 34 | L?-pending | binding_energy | — | 563.0404 | — | 60468.6033 MeV (-262.1 ppm) |
| ${}^{66}$Ga | 66 | 35 | L?-pending | binding_energy | — | 572.1780 | — | 61399.0309 MeV (-258.2 ppm) |
| ${}^{67}$Ga | 67 | 36 | L?-pending | binding_energy | — | 583.4047 | — | 62327.3694 MeV (-254.3 ppm) |
| ${}^{68}$Ga | 68 | 37 | L?-pending | binding_energy | — | 591.6829 | — | 63258.6563 MeV (-250.6 ppm) |
| ${}^{69}$Ga | 69 | 38 | L?-pending | binding_energy | — | 601.9960 | — | 64187.9084 MeV (-247.0 ppm) |
| ${}^{70}$Ga | 70 | 39 | L?-pending | binding_energy | — | 609.6497 | — | 65119.8200 MeV (-243.4 ppm) |
| ${}^{71}$Ga | 71 | 40 | L?-pending | binding_energy | — | 618.9500 | — | 66050.0849 MeV (-240.0 ppm) |
| ${}^{72}$Ga | 72 | 41 | L?-pending | binding_energy | — | 625.4704 | — | 66983.1296 MeV (-236.7 ppm) |
| ${}^{73}$Ga | 73 | 42 | L?-pending | binding_energy | — | 634.6528 | — | 67913.5124 MeV (-233.4 ppm) |
| ${}^{74}$Ga | 74 | 43 | L?-pending | binding_energy | — | 641.0744 | — | 68846.6560 MeV (-230.3 ppm) |
| ${}^{75}$Ga | 75 | 44 | L?-pending | binding_energy | — | 649.5567 | — | 69777.7388 MeV (-227.2 ppm) |
| ${}^{76}$Ga | 76 | 45 | L?-pending | binding_energy | — | 655.4641 | — | 70711.3967 MeV (-224.2 ppm) |
| ${}^{77}$Ga | 77 | 46 | L?-pending | binding_energy | — | 663.2311 | — | 71643.1948 MeV (-221.3 ppm) |
| ${}^{78}$Ga | 78 | 47 | L?-pending | binding_energy | — | 669.0141 | — | 72576.9770 MeV (-218.5 ppm) |
| ${}^{79}$Ga | 79 | 48 | L?-pending | binding_energy | — | 675.9297 | — | 73509.6266 MeV (-215.7 ppm) |
| ${}^{80}$Ga | 80 | 49 | L?-pending | binding_energy | — | 680.6764 | — | 74444.4451 MeV (-213.0 ppm) |
| ${}^{81}$Ga | 81 | 50 | L?-pending | binding_energy | — | 687.1520 | — | 75377.5347 MeV (-210.4 ppm) |
| ${}^{82}$Ga | 82 | 51 | L?-pending | binding_energy | — | 690.5261 | — | 76313.7258 MeV (-207.8 ppm) |
| ${}^{83}$Ga | 83 | 52 | L?-pending | binding_energy | — | 694.9238 | — | 77248.8933 MeV (-205.3 ppm) |
| ${}^{84}$Ga | 84 | 53 | L?-pending | binding_energy | — | 697.8321 | — | 78185.5501 MeV (-202.8 ppm) |
| ${}^{85}$Ga | 85 | 54 | L?-pending | binding_energy | — | 701.5533 | — | 79121.3941 MeV (-200.4 ppm) |
| ${}^{86}$Ga | 86 | 55 | L?-pending | binding_energy | — | 703.6520 | — | 80058.8606 MeV (-198.2 ppm) |
| ${}^{87}$Ga | 87 | 56 | L?-pending | binding_energy | — | 706.7880 | — | 80995.2898 MeV (-195.4 ppm) |
| ${}^{88}$Ga | 88 | 57 | L?-pending | binding_energy | — | 708.4000 | — | 81933.2430 MeV (-193.4 ppm) |

### Germanium (Z = 32)

_0 of 33 isotopes with a framework prediction; 33 of 33 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{58}$Ge | 58 | 26 | L?-pending | binding_energy | — | 450.6600 | — | 54002.7341 MeV (-302.6 ppm) |
| ${}^{59}$Ge | 59 | 27 | L?-pending | binding_energy | — | 467.5160 | — | 54925.4433 MeV (-297.4 ppm) |
| ${}^{60}$Ge | 60 | 28 | L?-pending | binding_energy | — | 486.7800 | — | 55845.7445 MeV (-293.1 ppm) |
| ${}^{61}$Ge | 61 | 29 | L?-pending | binding_energy | — | 501.1150 | — | 56770.9746 MeV (-288.4 ppm) |
| ${}^{62}$Ge | 62 | 30 | L?-pending | binding_energy | — | 517.5140 | — | 57694.1408 MeV (-283.4 ppm) |
| ${}^{63}$Ge | 63 | 31 | L?-pending | binding_energy | — | 530.3792 | — | 58620.8409 MeV (-279.1 ppm) |
| ${}^{64}$Ge | 64 | 32 | L?-pending | binding_energy | — | 545.8448 | — | 59544.9404 MeV (-274.8 ppm) |
| ${}^{65}$Ge | 65 | 33 | L?-pending | binding_energy | — | 556.0788 | — | 60474.2716 MeV (-270.6 ppm) |
| ${}^{66}$Ge | 66 | 34 | L?-pending | binding_energy | — | 569.2789 | — | 61400.6366 MeV (-266.5 ppm) |
| ${}^{67}$Ge | 67 | 35 | L?-pending | binding_energy | — | 578.4169 | — | 62331.0638 MeV (-262.5 ppm) |
| ${}^{68}$Ge | 68 | 36 | L?-pending | binding_energy | — | 590.7933 | — | 63258.2526 MeV (-258.7 ppm) |
| ${}^{69}$Ge | 69 | 37 | L?-pending | binding_energy | — | 598.9865 | — | 64189.6246 MeV (-254.9 ppm) |
| ${}^{70}$Ge | 70 | 38 | L?-pending | binding_energy | — | 610.5192 | — | 65117.6571 MeV (-251.3 ppm) |
| ${}^{71}$Ge | 71 | 39 | L?-pending | binding_energy | — | 617.9351 | — | 66049.8063 MeV (-247.8 ppm) |
| ${}^{72}$Ge | 72 | 40 | L?-pending | binding_energy | — | 628.6857 | — | 66978.6210 MeV (-244.3 ppm) |
| ${}^{73}$Ge | 73 | 41 | L?-pending | binding_energy | — | 635.4686 | — | 67911.4032 MeV (-241.0 ppm) |
| ${}^{74}$Ge | 74 | 42 | L?-pending | binding_energy | — | 645.6649 | — | 68840.7722 MeV (-237.7 ppm) |
| ${}^{75}$Ge | 75 | 43 | L?-pending | binding_energy | — | 652.1707 | — | 69773.8315 MeV (-234.5 ppm) |
| ${}^{76}$Ge | 76 | 44 | L?-pending | binding_energy | — | 661.5980 | — | 70703.9694 MeV (-231.5 ppm) |
| ${}^{77}$Ge | 77 | 45 | L?-pending | binding_energy | — | 667.6693 | — | 71637.4633 MeV (-228.5 ppm) |
| ${}^{78}$Ge | 78 | 46 | L?-pending | binding_energy | — | 676.3898 | — | 72568.3080 MeV (-225.5 ppm) |
| ${}^{79}$Ge | 79 | 47 | L?-pending | binding_energy | — | 682.1262 | — | 73502.1368 MeV (-222.7 ppm) |
| ${}^{80}$Ge | 80 | 48 | L?-pending | binding_energy | — | 690.2057 | — | 74433.6225 MeV (-219.9 ppm) |
| ${}^{81}$Ge | 81 | 49 | L?-pending | binding_energy | — | 695.0334 | — | 75368.3600 MeV (-217.2 ppm) |
| ${}^{82}$Ge | 82 | 50 | L?-pending | binding_energy | — | 702.2280 | — | 76300.7305 MeV (-214.5 ppm) |
| ${}^{83}$Ge | 83 | 51 | L?-pending | binding_energy | — | 705.8607 | — | 77236.6630 MeV (-211.9 ppm) |
| ${}^{84}$Ge | 84 | 52 | L?-pending | binding_energy | — | 711.1040 | — | 78170.9848 MeV (-209.4 ppm) |
| ${}^{85}$Ge | 85 | 53 | L?-pending | binding_energy | — | 714.1504 | — | 79107.5037 MeV (-206.9 ppm) |
| ${}^{86}$Ge | 86 | 54 | L?-pending | binding_energy | — | 718.4982 | — | 80042.7211 MeV (-204.5 ppm) |
| ${}^{87}$Ge | 87 | 55 | L?-pending | binding_energy | — | 720.7950 | — | 80979.9894 MeV (-202.6 ppm) |
| ${}^{88}$Ge | 88 | 56 | L?-pending | binding_energy | — | 724.7680 | — | 81915.5816 MeV (-199.9 ppm) |
| ${}^{89}$Ge | 89 | 57 | L?-pending | binding_energy | — | 726.3290 | — | 82853.5858 MeV (-197.3 ppm) |
| ${}^{90}$Ge | 90 | 58 | L?-pending | binding_energy | — | 729.8100 | — | 83789.6700 MeV (-194.8 ppm) |

### Arsenic (Z = 33)

_0 of 33 isotopes with a framework prediction; 33 of 33 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{60}$As | 60 | 27 | L?-pending | binding_energy | — | 464.1000 | — | 55867.1311 MeV (-302.0 ppm) |
| ${}^{61}$As | 61 | 28 | L?-pending | binding_energy | — | 483.7300 | — | 56787.0663 MeV (-297.1 ppm) |
| ${}^{62}$As | 62 | 29 | L?-pending | binding_energy | — | 499.0380 | — | 57711.3235 MeV (-292.6 ppm) |
| ${}^{63}$As | 63 | 30 | L?-pending | binding_energy | — | 516.1590 | — | 58633.7677 MeV (-287.5 ppm) |
| ${}^{64}$As | 64 | 31 | L?-pending | binding_energy | — | 530.3040 | — | 59559.1879 MeV (-283.7 ppm) |
| ${}^{65}$As | 65 | 32 | L?-pending | binding_energy | — | 545.7553 | — | 60483.3018 MeV (-279.0 ppm) |
| ${}^{66}$As | 66 | 33 | L?-pending | binding_energy | — | 558.9146 | — | 61409.7076 MeV (-274.8 ppm) |
| ${}^{67}$As | 67 | 34 | L?-pending | binding_energy | — | 571.5481 | — | 62336.6393 MeV (-270.7 ppm) |
| ${}^{68}$As | 68 | 35 | L?-pending | binding_energy | — | 581.9267 | — | 63265.8259 MeV (-266.7 ppm) |
| ${}^{69}$As | 69 | 36 | L?-pending | binding_energy | — | 594.2157 | — | 64193.1021 MeV (-262.9 ppm) |
| ${}^{70}$As | 70 | 37 | L?-pending | binding_energy | — | 603.5088 | — | 65123.3742 MeV (-259.1 ppm) |
| ${}^{71}$As | 71 | 38 | L?-pending | binding_energy | — | 615.1394 | — | 66051.3088 MeV (-255.5 ppm) |
| ${}^{72}$As | 72 | 39 | L?-pending | binding_energy | — | 623.5473 | — | 66982.4661 MeV (-251.9 ppm) |
| ${}^{73}$As | 73 | 40 | L?-pending | binding_energy | — | 634.3415 | — | 67911.2370 MeV (-248.5 ppm) |
| ${}^{74}$As | 74 | 41 | L?-pending | binding_energy | — | 642.3201 | — | 68842.8236 MeV (-245.1 ppm) |
| ${}^{75}$As | 75 | 42 | L?-pending | binding_energy | — | 652.5656 | — | 69772.1433 MeV (-241.9 ppm) |
| ${}^{76}$As | 76 | 43 | L?-pending | binding_energy | — | 659.8941 | — | 70704.3800 MeV (-238.7 ppm) |
| ${}^{77}$As | 77 | 44 | L?-pending | binding_energy | — | 669.5904 | — | 71634.2489 MeV (-235.6 ppm) |
| ${}^{78}$As | 78 | 45 | L?-pending | binding_energy | — | 676.5623 | — | 72566.8421 MeV (-232.6 ppm) |
| ${}^{79}$As | 79 | 46 | L?-pending | binding_energy | — | 685.4528 | — | 73497.5169 MeV (-229.6 ppm) |
| ${}^{80}$As | 80 | 47 | L?-pending | binding_energy | — | 692.1026 | — | 74430.4322 MeV (-226.8 ppm) |
| ${}^{81}$As | 81 | 48 | L?-pending | binding_energy | — | 700.4926 | — | 75361.6074 MeV (-224.0 ppm) |
| ${}^{82}$As | 82 | 49 | L?-pending | binding_energy | — | 706.1361 | — | 76295.5291 MeV (-221.2 ppm) |
| ${}^{83}$As | 83 | 50 | L?-pending | binding_energy | — | 713.7713 | — | 77227.4591 MeV (-218.6 ppm) |
| ${}^{84}$As | 84 | 51 | L?-pending | binding_energy | — | 718.0268 | — | 78162.7687 MeV (-215.9 ppm) |
| ${}^{85}$As | 85 | 52 | L?-pending | binding_energy | — | 723.4337 | — | 79096.9270 MeV (-213.4 ppm) |
| ${}^{86}$As | 86 | 53 | L?-pending | binding_energy | — | 727.2780 | — | 80032.6479 MeV (-210.9 ppm) |
| ${}^{87}$As | 87 | 54 | L?-pending | binding_energy | — | 732.0051 | — | 80967.4860 MeV (-208.5 ppm) |
| ${}^{88}$As | 88 | 55 | L?-pending | binding_energy | — | 734.8880 | — | 81904.1683 MeV (-205.8 ppm) |
| ${}^{89}$As | 89 | 56 | L?-pending | binding_energy | — | 739.0560 | — | 82839.5655 MeV (-203.7 ppm) |
| ${}^{90}$As | 90 | 57 | L?-pending | binding_energy | — | 741.6000 | — | 83776.5867 MeV (-201.6 ppm) |
| ${}^{91}$As | 91 | 58 | L?-pending | binding_energy | — | 745.1990 | — | 84712.5528 MeV (-199.6 ppm) |
| ${}^{92}$As | 92 | 59 | L?-pending | binding_energy | — | 747.1320 | — | 85650.1850 MeV (-197.2 ppm) |

### Selenium (Z = 34)

_0 of 33 isotopes with a framework prediction; 33 of 33 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{63}$Se | 63 | 29 | L?-pending | binding_energy | — | 498.7710 | — | 58649.8623 MeV (-296.9 ppm) |
| ${}^{64}$Se | 64 | 30 | L?-pending | binding_energy | — | 516.8000 | — | 59571.3985 MeV (-291.4 ppm) |
| ${}^{65}$Se | 65 | 31 | L?-pending | binding_energy | — | 531.0500 | — | 60496.7137 MeV (-287.3 ppm) |
| ${}^{66}$Se | 66 | 32 | L?-pending | binding_energy | — | 547.8000 | — | 61419.5289 MeV (-283.6 ppm) |
| ${}^{67}$Se | 67 | 33 | L?-pending | binding_energy | — | 560.7588 | — | 62346.1353 MeV (-278.8 ppm) |
| ${}^{68}$Se | 68 | 34 | L?-pending | binding_energy | — | 576.4393 | — | 63270.0200 MeV (-274.8 ppm) |
| ${}^{69}$Se | 69 | 35 | L?-pending | binding_energy | — | 586.7559 | — | 64199.2686 MeV (-270.8 ppm) |
| ${}^{70}$Se | 70 | 36 | L?-pending | binding_energy | — | 600.3224 | — | 65125.2673 MeV (-267.0 ppm) |
| ${}^{71}$Se | 71 | 37 | L?-pending | binding_energy | — | 609.6103 | — | 66055.5445 MeV (-263.2 ppm) |
| ${}^{72}$Se | 72 | 38 | L?-pending | binding_energy | — | 622.4033 | — | 66982.3167 MeV (-259.6 ppm) |
| ${}^{73}$Se | 73 | 39 | L?-pending | binding_energy | — | 630.8338 | — | 67913.4514 MeV (-256.0 ppm) |
| ${}^{74}$Se | 74 | 40 | L?-pending | binding_energy | — | 642.8909 | — | 68840.9594 MeV (-252.6 ppm) |
| ${}^{75}$Se | 75 | 41 | L?-pending | binding_energy | — | 650.9185 | — | 69772.4970 MeV (-249.2 ppm) |
| ${}^{76}$Se | 76 | 42 | L?-pending | binding_energy | — | 662.0723 | — | 70700.9084 MeV (-245.9 ppm) |
| ${}^{77}$Se | 77 | 43 | L?-pending | binding_energy | — | 669.4912 | — | 71633.0547 MeV (-242.7 ppm) |
| ${}^{78}$Se | 78 | 44 | L?-pending | binding_energy | — | 679.9890 | — | 72562.1222 MeV (-239.6 ppm) |
| ${}^{79}$Se | 79 | 45 | L?-pending | binding_energy | — | 686.9518 | — | 73494.7245 MeV (-236.6 ppm) |
| ${}^{80}$Se | 80 | 46 | L?-pending | binding_energy | — | 696.8651 | — | 74424.3763 MeV (-233.6 ppm) |
| ${}^{81}$Se | 81 | 47 | L?-pending | binding_energy | — | 703.5660 | — | 75357.2407 MeV (-230.7 ppm) |
| ${}^{82}$Se | 82 | 48 | L?-pending | binding_energy | — | 712.8422 | — | 76287.5297 MeV (-227.9 ppm) |
| ${}^{83}$Se | 83 | 49 | L?-pending | binding_energy | — | 718.6601 | — | 77221.2769 MeV (-225.2 ppm) |
| ${}^{84}$Se | 84 | 50 | L?-pending | binding_energy | — | 727.3387 | — | 78152.1636 MeV (-222.5 ppm) |
| ${}^{85}$Se | 85 | 51 | L?-pending | binding_energy | — | 731.8759 | — | 79087.1915 MeV (-219.9 ppm) |
| ${}^{86}$Se | 86 | 52 | L?-pending | binding_energy | — | 738.0367 | — | 80020.5959 MeV (-217.3 ppm) |
| ${}^{87}$Se | 87 | 53 | L?-pending | binding_energy | — | 742.0310 | — | 80956.1668 MeV (-214.8 ppm) |
| ${}^{88}$Se | 88 | 54 | L?-pending | binding_energy | — | 747.5604 | — | 81890.2026 MeV (-212.4 ppm) |
| ${}^{89}$Se | 89 | 55 | L?-pending | binding_energy | — | 750.7399 | — | 82826.5882 MeV (-210.0 ppm) |
| ${}^{90}$Se | 90 | 56 | L?-pending | binding_energy | — | 755.6190 | — | 83761.2743 MeV (-207.6 ppm) |
| ${}^{91}$Se | 91 | 57 | L?-pending | binding_energy | — | 758.4703 | — | 84697.9882 MeV (-205.3 ppm) |
| ${}^{92}$Se | 92 | 58 | L?-pending | binding_energy | — | 762.6800 | — | 85633.3437 MeV (-203.0 ppm) |
| ${}^{93}$Se | 93 | 59 | L?-pending | binding_energy | — | 764.9250 | — | 86570.6639 MeV (-201.3 ppm) |
| ${}^{94}$Se | 94 | 60 | L?-pending | binding_energy | — | 768.9200 | — | 87506.2341 MeV (-198.9 ppm) |
| ${}^{95}$Se | 95 | 61 | L?-pending | binding_energy | — | 770.6400 | — | 88444.0793 MeV (-196.7 ppm) |

### Bromine (Z = 35)

_0 of 34 isotopes with a framework prediction; 34 of 34 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{65}$Br | 65 | 30 | L?-pending | binding_energy | — | 513.7600 | — | 60512.7104 MeV (-296.0 ppm) |
| ${}^{66}$Br | 66 | 31 | L?-pending | binding_energy | — | 528.9240 | — | 61437.1116 MeV (-291.8 ppm) |
| ${}^{67}$Br | 67 | 32 | L?-pending | binding_energy | — | 545.9160 | — | 62359.6848 MeV (-286.8 ppm) |
| ${}^{68}$Br | 68 | 33 | L?-pending | binding_energy | — | 560.2520 | — | 63284.9139 MeV (-282.7 ppm) |
| ${}^{69}$Br | 69 | 34 | L?-pending | binding_energy | — | 575.7983 | — | 64208.9328 MeV (-278.7 ppm) |
| ${}^{70}$Br | 70 | 35 | L?-pending | binding_energy | — | 589.0357 | — | 65135.2606 MeV (-274.8 ppm) |
| ${}^{71}$Br | 71 | 36 | L?-pending | binding_energy | — | 602.1839 | — | 66061.6776 MeV (-270.9 ppm) |
| ${}^{72}$Br | 72 | 37 | L?-pending | binding_energy | — | 612.8145 | — | 66990.6122 MeV (-267.2 ppm) |
| ${}^{73}$Br | 73 | 38 | L?-pending | binding_energy | — | 625.4699 | — | 67917.5220 MeV (-263.5 ppm) |
| ${}^{74}$Br | 74 | 39 | L?-pending | binding_energy | — | 635.1836 | — | 68847.3735 MeV (-260.0 ppm) |
| ${}^{75}$Br | 75 | 40 | L?-pending | binding_energy | — | 647.0737 | — | 69775.0485 MeV (-256.5 ppm) |
| ${}^{76}$Br | 76 | 41 | L?-pending | binding_energy | — | 656.3271 | — | 70705.3603 MeV (-253.1 ppm) |
| ${}^{77}$Br | 77 | 42 | L?-pending | binding_energy | — | 667.3442 | — | 71633.9084 MeV (-249.9 ppm) |
| ${}^{78}$Br | 78 | 43 | L?-pending | binding_energy | — | 675.6328 | — | 72565.1849 MeV (-246.7 ppm) |
| ${}^{79}$Br | 79 | 44 | L?-pending | binding_energy | — | 686.3201 | — | 73494.0629 MeV (-243.5 ppm) |
| ${}^{80}$Br | 80 | 45 | L?-pending | binding_energy | — | 694.2123 | — | 74425.7358 MeV (-240.5 ppm) |
| ${}^{81}$Br | 81 | 46 | L?-pending | binding_energy | — | 704.3717 | — | 75355.1417 MeV (-237.5 ppm) |
| ${}^{82}$Br | 82 | 47 | L?-pending | binding_energy | — | 711.9646 | — | 76287.1139 MeV (-234.6 ppm) |
| ${}^{83}$Br | 83 | 48 | L?-pending | binding_energy | — | 721.5510 | — | 77217.0927 MeV (-231.8 ppm) |
| ${}^{84}$Br | 84 | 49 | L?-pending | binding_energy | — | 728.3917 | — | 78149.8172 MeV (-229.0 ppm) |
| ${}^{85}$Br | 85 | 50 | L?-pending | binding_energy | — | 737.2554 | — | 79080.5187 MeV (-226.4 ppm) |
| ${}^{86}$Br | 86 | 51 | L?-pending | binding_energy | — | 742.3835 | — | 80014.9558 MeV (-223.7 ppm) |
| ${}^{87}$Br | 87 | 52 | L?-pending | binding_energy | — | 748.7142 | — | 80948.1902 MeV (-221.1 ppm) |
| ${}^{88}$Br | 88 | 53 | L?-pending | binding_energy | — | 753.6098 | — | 81882.8598 MeV (-218.6 ppm) |
| ${}^{89}$Br | 89 | 54 | L?-pending | binding_energy | — | 759.2394 | — | 82816.7954 MeV (-216.2 ppm) |
| ${}^{90}$Br | 90 | 55 | L?-pending | binding_energy | — | 763.0368 | — | 83752.5632 MeV (-213.7 ppm) |
| ${}^{91}$Br | 91 | 56 | L?-pending | binding_energy | — | 768.2151 | — | 84686.9501 MeV (-211.4 ppm) |
| ${}^{92}$Br | 92 | 57 | L?-pending | binding_energy | — | 771.4119 | — | 85623.3184 MeV (-209.1 ppm) |
| ${}^{93}$Br | 93 | 58 | L?-pending | binding_energy | — | 776.1407 | — | 86558.1549 MeV (-206.8 ppm) |
| ${}^{94}$Br | 94 | 59 | L?-pending | binding_energy | — | 778.9780 | — | 87494.8827 MeV (-204.7 ppm) |
| ${}^{95}$Br | 95 | 60 | L?-pending | binding_energy | — | 783.2750 | — | 88430.1509 MeV (-202.8 ppm) |
| ${}^{96}$Br | 96 | 61 | L?-pending | binding_energy | — | 785.6640 | — | 89367.3271 MeV (-200.2 ppm) |
| ${}^{97}$Br | 97 | 62 | L?-pending | binding_energy | — | 789.5800 | — | 90302.9763 MeV (-198.7 ppm) |
| ${}^{98}$Br | 98 | 63 | L?-pending | binding_energy | — | 791.6440 | — | 91240.4775 MeV (-196.1 ppm) |

### Krypton (Z = 36)

_0 of 35 isotopes with a framework prediction; 35 of 35 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{67}$Kr | 67 | 31 | L?-pending | binding_energy | — | 528.1610 | — | 62376.1464 MeV (-295.0 ppm) |
| ${}^{68}$Kr | 68 | 32 | L?-pending | binding_energy | — | 546.3120 | — | 63297.5606 MeV (-290.8 ppm) |
| ${}^{69}$Kr | 69 | 33 | L?-pending | binding_energy | — | 560.9010 | — | 64222.5368 MeV (-286.7 ppm) |
| ${}^{70}$Kr | 70 | 34 | L?-pending | binding_energy | — | 577.9200 | — | 65145.0830 MeV (-282.4 ppm) |
| ${}^{71}$Kr | 71 | 35 | L?-pending | binding_energy | — | 591.2263 | — | 66071.3419 MeV (-278.6 ppm) |
| ${}^{72}$Kr | 72 | 36 | L?-pending | binding_energy | — | 606.9110 | — | 66995.2224 MeV (-274.8 ppm) |
| ${}^{73}$Kr | 73 | 37 | L?-pending | binding_energy | — | 617.5935 | — | 67924.1050 MeV (-271.0 ppm) |
| ${}^{74}$Kr | 74 | 38 | L?-pending | binding_energy | — | 631.4449 | — | 68849.8188 MeV (-267.4 ppm) |
| ${}^{75}$Kr | 75 | 39 | L?-pending | binding_energy | — | 641.5080 | — | 69779.3209 MeV (-263.8 ppm) |
| ${}^{76}$Kr | 76 | 40 | L?-pending | binding_energy | — | 654.2694 | — | 70706.1247 MeV (-260.4 ppm) |
| ${}^{77}$Kr | 77 | 41 | L?-pending | binding_energy | — | 663.4964 | — | 71636.4628 MeV (-257.0 ppm) |
| ${}^{78}$Kr | 78 | 42 | L?-pending | binding_energy | — | 675.5766 | — | 72563.9478 MeV (-253.7 ppm) |
| ${}^{79}$Kr | 79 | 43 | L?-pending | binding_energy | — | 683.9119 | — | 73495.1777 MeV (-250.5 ppm) |
| ${}^{80}$Kr | 80 | 44 | L?-pending | binding_energy | — | 695.4344 | — | 74423.2204 MeV (-247.4 ppm) |
| ${}^{81}$Kr | 81 | 45 | L?-pending | binding_energy | — | 703.3085 | — | 75354.9115 MeV (-244.3 ppm) |
| ${}^{82}$Kr | 82 | 46 | L?-pending | binding_energy | — | 714.2754 | — | 76283.5098 MeV (-241.3 ppm) |
| ${}^{83}$Kr | 83 | 47 | L?-pending | binding_energy | — | 721.7455 | — | 77215.6048 MeV (-238.4 ppm) |
| ${}^{84}$Kr | 84 | 48 | L?-pending | binding_energy | — | 732.2656 | — | 78144.6500 MeV (-235.6 ppm) |
| ${}^{85}$Kr | 85 | 49 | L?-pending | binding_energy | — | 739.3779 | — | 79077.1029 MeV (-232.8 ppm) |
| ${}^{86}$Kr | 86 | 50 | L?-pending | binding_energy | — | 749.2345 | — | 80006.8114 MeV (-230.1 ppm) |
| ${}^{87}$Kr | 87 | 51 | L?-pending | binding_energy | — | 754.7497 | — | 80940.8614 MeV (-227.5 ppm) |
| ${}^{88}$Kr | 88 | 52 | L?-pending | binding_energy | — | 761.8028 | — | 81873.3735 MeV (-224.9 ppm) |
| ${}^{89}$Kr | 89 | 53 | L?-pending | binding_energy | — | 766.7186 | — | 82808.0229 MeV (-222.3 ppm) |
| ${}^{90}$Kr | 90 | 54 | L?-pending | binding_energy | — | 773.2134 | — | 83741.0933 MeV (-219.9 ppm) |
| ${}^{91}$Kr | 91 | 55 | L?-pending | binding_energy | — | 777.2994 | — | 84676.5724 MeV (-217.4 ppm) |
| ${}^{92}$Kr | 92 | 56 | L?-pending | binding_energy | — | 783.1661 | — | 85610.2709 MeV (-215.1 ppm) |
| ${}^{93}$Kr | 93 | 57 | L?-pending | binding_energy | — | 786.6041 | — | 86546.3981 MeV (-212.8 ppm) |
| ${}^{94}$Kr | 94 | 58 | L?-pending | binding_energy | — | 791.8872 | — | 87480.6802 MeV (-210.5 ppm) |
| ${}^{95}$Kr | 95 | 59 | L?-pending | binding_energy | — | 794.7696 | — | 88417.3629 MeV (-208.3 ppm) |
| ${}^{96}$Kr | 96 | 60 | L?-pending | binding_energy | — | 799.7637 | — | 89351.9341 MeV (-206.1 ppm) |
| ${}^{97}$Kr | 97 | 61 | L?-pending | binding_energy | — | 802.1769 | — | 90289.0861 MeV (-204.0 ppm) |
| ${}^{98}$Kr | 98 | 62 | L?-pending | binding_energy | — | 806.9320 | — | 91223.8961 MeV (-201.7 ppm) |
| ${}^{99}$Kr | 99 | 63 | L?-pending | binding_energy | — | 809.3250 | — | 92161.0683 MeV (-200.1 ppm) |
| ${}^{100}$Kr | 100 | 64 | L?-pending | binding_energy | — | 813.4000 | — | 93096.5585 MeV (-197.4 ppm) |
| ${}^{101}$Kr | 101 | 65 | L?-pending | binding_energy | — | 815.5750 | — | 94033.9487 MeV (-195.4 ppm) |

### Rubidium (Z = 37)

_0 of 34 isotopes with a framework prediction; 34 of 34 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{71}$Rb | 71 | 34 | L?-pending | binding_energy | — | 576.3780 | — | 66084.8968 MeV (-285.8 ppm) |
| ${}^{72}$Rb | 72 | 35 | L?-pending | binding_energy | — | 590.5440 | — | 67010.2960 MeV (-282.7 ppm) |
| ${}^{73}$Rb | 73 | 36 | L?-pending | binding_energy | — | 606.2710 | — | 67934.1342 MeV (-278.5 ppm) |
| ${}^{74}$Rb | 74 | 37 | L?-pending | binding_energy | — | 620.2467 | — | 68859.7237 MeV (-274.7 ppm) |
| ${}^{75}$Rb | 75 | 38 | L?-pending | binding_energy | — | 633.6207 | — | 69785.9148 MeV (-271.1 ppm) |
| ${}^{76}$Rb | 76 | 39 | L?-pending | binding_energy | — | 644.9524 | — | 70714.1483 MeV (-267.5 ppm) |
| ${}^{77}$Rb | 77 | 40 | L?-pending | binding_energy | — | 657.3751 | — | 71641.2908 MeV (-264.1 ppm) |
| ${}^{78}$Rb | 78 | 41 | L?-pending | binding_energy | — | 667.5514 | — | 72570.6797 MeV (-260.7 ppm) |
| ${}^{79}$Rb | 79 | 42 | L?-pending | binding_energy | — | 679.4901 | — | 73498.3062 MeV (-257.4 ppm) |
| ${}^{80}$Rb | 80 | 43 | L?-pending | binding_energy | — | 688.9341 | — | 74428.4274 MeV (-254.2 ppm) |
| ${}^{81}$Rb | 81 | 44 | L?-pending | binding_energy | — | 700.2866 | — | 75356.6400 MeV (-251.1 ppm) |
| ${}^{82}$Rb | 82 | 45 | L?-pending | binding_energy | — | 709.0891 | — | 76287.4028 MeV (-248.0 ppm) |
| ${}^{83}$Rb | 83 | 46 | L?-pending | binding_energy | — | 720.0432 | — | 77216.0138 MeV (-245.0 ppm) |
| ${}^{84}$Rb | 84 | 47 | L?-pending | binding_energy | — | 728.8028 | — | 78146.8194 MeV (-242.1 ppm) |
| ${}^{85}$Rb | 85 | 48 | L?-pending | binding_energy | — | 739.2825 | — | 79075.9049 MeV (-239.3 ppm) |
| ${}^{86}$Rb | 86 | 49 | L?-pending | binding_energy | — | 747.9335 | — | 80006.8191 MeV (-236.5 ppm) |
| ${}^{87}$Rb | 87 | 50 | L?-pending | binding_energy | — | 757.8556 | — | 80936.4621 MeV (-233.8 ppm) |
| ${}^{88}$Rb | 88 | 51 | L?-pending | binding_energy | — | 763.9382 | — | 81869.9448 MeV (-231.1 ppm) |
| ${}^{89}$Rb | 89 | 52 | L?-pending | binding_energy | — | 771.1129 | — | 82802.3353 MeV (-228.5 ppm) |
| ${}^{90}$Rb | 90 | 53 | L?-pending | binding_energy | — | 776.8374 | — | 83736.1760 MeV (-226.0 ppm) |
| ${}^{91}$Rb | 91 | 54 | L?-pending | binding_energy | — | 783.2882 | — | 84669.2904 MeV (-223.5 ppm) |
| ${}^{92}$Rb | 92 | 55 | L?-pending | binding_energy | — | 788.3869 | — | 85603.7568 MeV (-221.1 ppm) |
| ${}^{93}$Rb | 93 | 56 | L?-pending | binding_energy | — | 794.3056 | — | 86537.4032 MeV (-218.7 ppm) |
| ${}^{94}$Rb | 94 | 57 | L?-pending | binding_energy | — | 798.3199 | — | 87472.9542 MeV (-216.3 ppm) |
| ${}^{95}$Rb | 95 | 58 | L?-pending | binding_energy | — | 803.7187 | — | 88407.1206 MeV (-214.1 ppm) |
| ${}^{96}$Rb | 96 | 59 | L?-pending | binding_energy | — | 807.2540 | — | 89343.1504 MeV (-211.8 ppm) |
| ${}^{97}$Rb | 97 | 60 | L?-pending | binding_energy | — | 812.4902 | — | 90277.4795 MeV (-209.6 ppm) |
| ${}^{98}$Rb | 98 | 61 | L?-pending | binding_energy | — | 816.4115 | — | 91213.1233 MeV (-207.5 ppm) |
| ${}^{99}$Rb | 99 | 62 | L?-pending | binding_energy | — | 821.2348 | — | 92147.8652 MeV (-205.4 ppm) |
| ${}^{100}$Rb | 100 | 63 | L?-pending | binding_energy | — | 824.4508 | — | 93084.2143 MeV (-203.3 ppm) |
| ${}^{101}$Rb | 101 | 64 | L?-pending | binding_energy | — | 828.8237 | — | 94019.4067 MeV (-201.3 ppm) |
| ${}^{102}$Rb | 102 | 65 | L?-pending | binding_energy | — | 831.5799 | — | 94956.2156 MeV (-199.3 ppm) |
| ${}^{103}$Rb | 103 | 66 | L?-pending | binding_energy | — | 835.5360 | — | 95891.8247 MeV (-197.1 ppm) |
| ${}^{104}$Rb | 104 | 67 | L?-pending | binding_energy | — | 837.9280 | — | 96828.9979 MeV (-195.5 ppm) |

### Strontium (Z = 38)

_0 of 35 isotopes with a framework prediction; 35 of 35 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{73}$Sr | 73 | 35 | L?-pending | binding_energy | — | 591.4460 | — | 67947.6659 MeV (-286.2 ppm) |
| ${}^{74}$Sr | 74 | 36 | L?-pending | binding_energy | — | 608.3540 | — | 68870.3230 MeV (-281.8 ppm) |
| ${}^{75}$Sr | 75 | 37 | L?-pending | binding_energy | — | 622.2384 | — | 69796.0039 MeV (-278.4 ppm) |
| ${}^{76}$Sr | 76 | 38 | L?-pending | binding_energy | — | 637.9386 | — | 70719.8688 MeV (-274.7 ppm) |
| ${}^{77}$Sr | 77 | 39 | L?-pending | binding_energy | — | 649.5657 | — | 71647.8069 MeV (-271.2 ppm) |
| ${}^{78}$Sr | 78 | 40 | L?-pending | binding_energy | — | 663.0076 | — | 72573.9302 MeV (-267.7 ppm) |
| ${}^{79}$Sr | 79 | 41 | L?-pending | binding_energy | — | 673.3846 | — | 73503.1184 MeV (-264.4 ppm) |
| ${}^{80}$Sr | 80 | 42 | L?-pending | binding_energy | — | 686.2877 | — | 74429.7804 MeV (-261.1 ppm) |
| ${}^{81}$Sr | 81 | 43 | L?-pending | binding_energy | — | 695.5757 | — | 75360.0576 MeV (-257.8 ppm) |
| ${}^{82}$Sr | 82 | 44 | L?-pending | binding_energy | — | 708.1290 | — | 76287.0696 MeV (-254.7 ppm) |
| ${}^{83}$Sr | 83 | 45 | L?-pending | binding_energy | — | 716.9878 | — | 77217.7759 MeV (-251.7 ppm) |
| ${}^{84}$Sr | 84 | 46 | L?-pending | binding_energy | — | 728.9111 | — | 78145.4178 MeV (-248.7 ppm) |
| ${}^{85}$Sr | 85 | 47 | L?-pending | binding_energy | — | 737.4361 | — | 79076.4579 MeV (-245.7 ppm) |
| ${}^{86}$Sr | 86 | 48 | L?-pending | binding_energy | — | 748.9273 | — | 80004.5320 MeV (-242.9 ppm) |
| ${}^{87}$Sr | 87 | 49 | L?-pending | binding_energy | — | 757.3556 | — | 80935.6689 MeV (-240.1 ppm) |
| ${}^{88}$Sr | 88 | 50 | L?-pending | binding_energy | — | 768.4684 | — | 81864.1212 MeV (-237.4 ppm) |
| ${}^{89}$Sr | 89 | 51 | L?-pending | binding_energy | — | 774.8271 | — | 82797.3277 MeV (-234.7 ppm) |
| ${}^{90}$Sr | 90 | 52 | L?-pending | binding_energy | — | 782.6404 | — | 83729.0796 MeV (-232.1 ppm) |
| ${}^{91}$Sr | 91 | 53 | L?-pending | binding_energy | — | 788.4127 | — | 84662.8725 MeV (-229.6 ppm) |
| ${}^{92}$Sr | 92 | 54 | L?-pending | binding_energy | — | 795.6994 | — | 85595.1509 MeV (-227.1 ppm) |
| ${}^{93}$Sr | 93 | 55 | L?-pending | binding_energy | — | 800.9892 | — | 86529.4263 MeV (-224.6 ppm) |
| ${}^{94}$Sr | 94 | 56 | L?-pending | binding_energy | — | 807.8204 | — | 87462.1603 MeV (-222.2 ppm) |
| ${}^{95}$Sr | 95 | 57 | L?-pending | binding_energy | — | 812.1633 | — | 88397.3826 MeV (-219.9 ppm) |
| ${}^{96}$Sr | 96 | 58 | L?-pending | binding_energy | — | 818.0356 | — | 89331.0755 MeV (-217.6 ppm) |
| ${}^{97}$Sr | 97 | 59 | L?-pending | binding_energy | — | 821.7693 | — | 90266.9070 MeV (-215.3 ppm) |
| ${}^{98}$Sr | 98 | 60 | L?-pending | binding_energy | — | 827.6824 | — | 91200.5591 MeV (-213.1 ppm) |
| ${}^{99}$Sr | 99 | 61 | L?-pending | binding_energy | — | 831.8498 | — | 92135.9568 MeV (-211.0 ppm) |
| ${}^{100}$Sr | 100 | 62 | L?-pending | binding_energy | — | 837.2201 | — | 93070.1517 MeV (-208.8 ppm) |
| ${}^{101}$Sr | 101 | 63 | L?-pending | binding_energy | — | 840.7989 | — | 94006.1382 MeV (-206.8 ppm) |
| ${}^{102}$Sr | 102 | 64 | L?-pending | binding_energy | — | 845.7046 | — | 94940.7976 MeV (-204.7 ppm) |
| ${}^{103}$Sr | 103 | 65 | L?-pending | binding_energy | — | 848.9260 | — | 95877.1414 MeV (-203.0 ppm) |
| ${}^{104}$Sr | 104 | 66 | L?-pending | binding_energy | — | 853.4240 | — | 96812.2086 MeV (-200.5 ppm) |
| ${}^{105}$Sr | 105 | 67 | L?-pending | binding_energy | — | 855.9600 | — | 97749.2378 MeV (-199.0 ppm) |
| ${}^{106}$Sr | 106 | 68 | L?-pending | binding_energy | — | 860.0840 | — | 98684.6790 MeV (-196.5 ppm) |
| ${}^{107}$Sr | 107 | 69 | L?-pending | binding_energy | — | 862.0990 | — | 99622.2291 MeV (-194.6 ppm) |

### Yttrium (Z = 39)

_0 of 35 isotopes with a framework prediction; 35 of 35 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{75}$Y | 75 | 36 | L?-pending | binding_energy | — | 606.6750 | — | 69810.2739 MeV (-285.9 ppm) |
| ${}^{76}$Y | 76 | 37 | L?-pending | binding_energy | — | 621.1480 | — | 70735.3661 MeV (-281.8 ppm) |
| ${}^{77}$Y | 77 | 38 | L?-pending | binding_energy | — | 637.4060 | — | 71658.6733 MeV (-278.1 ppm) |
| ${}^{78}$Y | 78 | 39 | L?-pending | binding_energy | — | 651.2220 | — | 72584.4225 MeV (-274.7 ppm) |
| ${}^{79}$Y | 79 | 40 | L?-pending | binding_energy | — | 664.9255 | — | 73510.2841 MeV (-271.3 ppm) |
| ${}^{80}$Y | 80 | 41 | L?-pending | binding_energy | — | 676.3421 | — | 74438.4328 MeV (-267.9 ppm) |
| ${}^{81}$Y | 81 | 42 | L?-pending | binding_energy | — | 688.9782 | — | 75365.3619 MeV (-264.6 ppm) |
| ${}^{82}$Y | 82 | 43 | L?-pending | binding_energy | — | 699.4006 | — | 76294.5045 MeV (-261.4 ppm) |
| ${}^{83}$Y | 83 | 44 | L?-pending | binding_energy | — | 711.6135 | — | 77221.8568 MeV (-258.3 ppm) |
| ${}^{84}$Y | 84 | 45 | L?-pending | binding_energy | — | 721.3736 | — | 78151.6619 MeV (-255.2 ppm) |
| ${}^{85}$Y | 85 | 46 | L?-pending | binding_energy | — | 733.3926 | — | 79079.2081 MeV (-252.2 ppm) |
| ${}^{86}$Y | 86 | 47 | L?-pending | binding_energy | — | 742.9049 | — | 80009.2610 MeV (-249.3 ppm) |
| ${}^{87}$Y | 87 | 48 | L?-pending | binding_energy | — | 754.7115 | — | 80937.0196 MeV (-246.4 ppm) |
| ${}^{88}$Y | 88 | 49 | L?-pending | binding_energy | — | 764.0635 | — | 81867.2328 MeV (-243.6 ppm) |
| ${}^{89}$Y | 89 | 50 | L?-pending | binding_energy | — | 775.5470 | — | 82795.3145 MeV (-240.9 ppm) |
| ${}^{90}$Y | 90 | 51 | L?-pending | binding_energy | — | 782.4040 | — | 83728.0227 MeV (-238.2 ppm) |
| ${}^{91}$Y | 91 | 52 | L?-pending | binding_energy | — | 790.3297 | — | 84659.6621 MeV (-235.6 ppm) |
| ${}^{92}$Y | 92 | 53 | L?-pending | binding_energy | — | 796.8662 | — | 85592.6908 MeV (-233.0 ppm) |
| ${}^{93}$Y | 93 | 54 | L?-pending | binding_energy | — | 804.3482 | — | 86524.7740 MeV (-230.5 ppm) |
| ${}^{94}$Y | 94 | 55 | L?-pending | binding_energy | — | 810.5438 | — | 87458.1436 MeV (-228.1 ppm) |
| ${}^{95}$Y | 95 | 56 | L?-pending | binding_energy | — | 817.4716 | — | 88390.7810 MeV (-225.7 ppm) |
| ${}^{96}$Y | 96 | 57 | L?-pending | binding_energy | — | 822.6650 | — | 89325.1528 MeV (-223.3 ppm) |
| ${}^{97}$Y | 97 | 58 | L?-pending | binding_energy | — | 828.5218 | — | 90258.8612 MeV (-221.0 ppm) |
| ${}^{98}$Y | 98 | 59 | L?-pending | binding_energy | — | 832.7664 | — | 91194.1818 MeV (-218.7 ppm) |
| ${}^{99}$Y | 99 | 60 | L?-pending | binding_energy | — | 839.1927 | — | 92127.3206 MeV (-216.5 ppm) |
| ${}^{100}$Y | 100 | 61 | L?-pending | binding_energy | — | 843.9415 | — | 93062.1370 MeV (-214.3 ppm) |
| ${}^{101}$Y | 101 | 62 | L?-pending | binding_energy | — | 849.7464 | — | 93995.8973 MeV (-212.2 ppm) |
| ${}^{102}$Y | 102 | 63 | L?-pending | binding_energy | — | 853.9356 | — | 94931.2733 MeV (-210.1 ppm) |
| ${}^{103}$Y | 103 | 64 | L?-pending | binding_energy | — | 859.2913 | — | 95865.4828 MeV (-208.1 ppm) |
| ${}^{104}$Y | 104 | 65 | L?-pending | binding_energy | — | 862.9920 | — | 96801.3473 MeV (-206.1 ppm) |
| ${}^{105}$Y | 105 | 66 | L?-pending | binding_energy | — | 867.5100 | — | 97736.3944 MeV (-203.7 ppm) |
| ${}^{106}$Y | 106 | 67 | L?-pending | binding_energy | — | 870.7900 | — | 98672.6796 MeV (-201.7 ppm) |
| ${}^{107}$Y | 107 | 68 | L?-pending | binding_energy | — | 875.0460 | — | 99607.9888 MeV (-199.8 ppm) |
| ${}^{108}$Y | 108 | 69 | L?-pending | binding_energy | — | 877.9320 | — | 100544.6680 MeV (-198.0 ppm) |
| ${}^{109}$Y | 109 | 70 | L?-pending | binding_energy | — | 881.7010 | — | 101480.4642 MeV (-196.2 ppm) |

### Zirconium (Z = 40)

_0 of 37 isotopes with a framework prediction; 37 of 37 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{77}$Zr | 77 | 37 | L?-pending | binding_energy | — | 621.7750 | — | 71673.0109 MeV (-285.0 ppm) |
| ${}^{78}$Zr | 78 | 38 | L?-pending | binding_energy | — | 639.1320 | — | 72595.2191 MeV (-281.9 ppm) |
| ${}^{79}$Zr | 79 | 39 | L?-pending | binding_energy | — | 653.0930 | — | 73520.8233 MeV (-277.9 ppm) |
| ${}^{80}$Zr | 80 | 40 | L?-pending | binding_energy | — | 669.2000 | — | 74444.2815 MeV (-275.1 ppm) |
| ${}^{81}$Zr | 81 | 41 | L?-pending | binding_energy | — | 680.0073 | — | 75373.0394 MeV (-271.4 ppm) |
| ${}^{82}$Zr | 82 | 42 | L?-pending | binding_energy | — | 694.1683 | — | 76298.4436 MeV (-268.1 ppm) |
| ${}^{83}$Zr | 83 | 43 | L?-pending | binding_energy | — | 704.5372 | — | 77227.6399 MeV (-264.8 ppm) |
| ${}^{84}$Zr | 84 | 44 | L?-pending | binding_energy | — | 718.1185 | — | 78153.6237 MeV (-261.7 ppm) |
| ${}^{85}$Zr | 85 | 45 | L?-pending | binding_energy | — | 727.9433 | — | 79083.3641 MeV (-258.6 ppm) |
| ${}^{86}$Zr | 86 | 46 | L?-pending | binding_energy | — | 740.8085 | — | 80010.0641 MeV (-255.6 ppm) |
| ${}^{87}$Zr | 87 | 47 | L?-pending | binding_energy | — | 750.2579 | — | 80940.1798 MeV (-252.7 ppm) |
| ${}^{88}$Zr | 88 | 48 | L?-pending | binding_energy | — | 762.6110 | — | 81867.3920 MeV (-249.9 ppm) |
| ${}^{89}$Zr | 89 | 49 | L?-pending | binding_energy | — | 771.9314 | — | 82797.6368 MeV (-247.1 ppm) |
| ${}^{90}$Zr | 90 | 50 | L?-pending | binding_energy | — | 783.8973 | — | 83725.2360 MeV (-244.3 ppm) |
| ${}^{91}$Zr | 91 | 51 | L?-pending | binding_energy | — | 791.0917 | — | 84657.6069 MeV (-241.6 ppm) |
| ${}^{92}$Zr | 92 | 52 | L?-pending | binding_energy | — | 799.7264 | — | 85588.5373 MeV (-239.0 ppm) |
| ${}^{93}$Zr | 93 | 53 | L?-pending | binding_energy | — | 806.4607 | — | 86521.3682 MeV (-236.4 ppm) |
| ${}^{94}$Zr | 94 | 54 | L?-pending | binding_energy | — | 814.6794 | — | 87452.7147 MeV (-233.9 ppm) |
| ${}^{95}$Zr | 95 | 55 | L?-pending | binding_energy | — | 821.1413 | — | 88385.8180 MeV (-231.5 ppm) |
| ${}^{96}$Zr | 96 | 56 | L?-pending | binding_energy | — | 828.9915 | — | 89317.5329 MeV (-229.0 ppm) |
| ${}^{97}$Zr | 97 | 57 | L?-pending | binding_energy | — | 834.5607 | — | 90251.5290 MeV (-226.7 ppm) |
| ${}^{98}$Zr | 98 | 58 | L?-pending | binding_energy | — | 840.9770 | — | 91184.6778 MeV (-224.4 ppm) |
| ${}^{99}$Zr | 99 | 59 | L?-pending | binding_energy | — | 845.3833 | — | 92119.8367 MeV (-222.1 ppm) |
| ${}^{100}$Zr | 100 | 60 | L?-pending | binding_energy | — | 852.2107 | — | 93052.5745 MeV (-219.9 ppm) |
| ${}^{101}$Zr | 101 | 61 | L?-pending | binding_energy | — | 857.0702 | — | 93987.2801 MeV (-217.7 ppm) |
| ${}^{102}$Zr | 102 | 62 | L?-pending | binding_energy | — | 863.5620 | — | 94920.3536 MeV (-215.5 ppm) |
| ${}^{103}$Zr | 103 | 63 | L?-pending | binding_energy | — | 867.8609 | — | 95855.6199 MeV (-213.4 ppm) |
| ${}^{104}$Zr | 104 | 64 | L?-pending | binding_energy | — | 873.8409 | — | 96789.2051 MeV (-211.4 ppm) |
| ${}^{105}$Zr | 105 | 65 | L?-pending | binding_energy | — | 877.6528 | — | 97724.9583 MeV (-209.4 ppm) |
| ${}^{106}$Zr | 106 | 66 | L?-pending | binding_energy | — | 882.9800 | — | 98659.1963 MeV (-207.0 ppm) |
| ${}^{107}$Zr | 107 | 67 | L?-pending | binding_energy | — | 886.3880 | — | 99595.3535 MeV (-205.7 ppm) |
| ${}^{108}$Zr | 108 | 68 | L?-pending | binding_energy | — | 891.3240 | — | 100529.9827 MeV (-203.2 ppm) |
| ${}^{109}$Zr | 109 | 69 | L?-pending | binding_energy | — | 894.2360 | — | 101466.6358 MeV (-201.9 ppm) |
| ${}^{110}$Zr | 110 | 70 | L?-pending | binding_energy | — | 898.8100 | — | 102401.6270 MeV (-200.2 ppm) |
| ${}^{111}$Zr | 111 | 71 | L?-pending | binding_energy | — | 901.0980 | — | 103338.9042 MeV (-198.0 ppm) |
| ${}^{112}$Zr | 112 | 72 | L?-pending | binding_energy | — | 905.0720 | — | 104274.4954 MeV (-195.8 ppm) |
| ${}^{113}$Zr | 113 | 73 | L?-pending | binding_energy | — | 907.0510 | — | 105212.0816 MeV (-194.0 ppm) |

### Niobium (Z = 41)

_0 of 38 isotopes with a framework prediction; 38 of 38 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{79}$Nb | 79 | 38 | L?-pending | binding_energy | — | 637.2140 | — | 73535.4090 MeV (-285.2 ppm) |
| ${}^{80}$Nb | 80 | 39 | L?-pending | binding_energy | — | 652.0800 | — | 74460.1082 MeV (-281.9 ppm) |
| ${}^{81}$Nb | 81 | 40 | L?-pending | binding_energy | — | 668.0880 | — | 75383.6653 MeV (-278.5 ppm) |
| ${}^{82}$Nb | 82 | 41 | L?-pending | binding_energy | — | 681.5840 | — | 76309.7345 MeV (-274.8 ppm) |
| ${}^{83}$Nb | 83 | 42 | L?-pending | binding_energy | — | 695.4561 | — | 77235.4276 MeV (-271.4 ppm) |
| ${}^{84}$Nb | 84 | 43 | L?-pending | binding_energy | — | 707.1083 | — | 78163.3406 MeV (-268.2 ppm) |
| ${}^{85}$Nb | 85 | 44 | L?-pending | binding_energy | — | 720.2655 | — | 79089.7486 MeV (-265.1 ppm) |
| ${}^{86}$Nb | 86 | 45 | L?-pending | binding_energy | — | 731.1912 | — | 80018.3881 MeV (-262.0 ppm) |
| ${}^{87}$Nb | 87 | 46 | L?-pending | binding_energy | — | 744.0029 | — | 80945.1415 MeV (-259.0 ppm) |
| ${}^{88}$Nb | 88 | 47 | L?-pending | binding_energy | — | 754.3713 | — | 81874.3383 MeV (-256.1 ppm) |
| ${}^{89}$Nb | 89 | 48 | L?-pending | binding_energy | — | 766.8968 | — | 82801.3780 MeV (-253.2 ppm) |
| ${}^{90}$Nb | 90 | 49 | L?-pending | binding_energy | — | 777.0039 | — | 83730.8361 MeV (-250.4 ppm) |
| ${}^{91}$Nb | 91 | 50 | L?-pending | binding_energy | — | 789.0517 | — | 84658.3534 MeV (-247.7 ppm) |
| ${}^{92}$Nb | 92 | 51 | L?-pending | binding_energy | — | 796.9383 | — | 85590.0321 MeV (-245.0 ppm) |
| ${}^{93}$Nb | 93 | 52 | L?-pending | binding_energy | — | 805.7692 | — | 86520.7664 MeV (-242.3 ppm) |
| ${}^{94}$Nb | 94 | 53 | L?-pending | binding_energy | — | 812.9967 | — | 87453.1040 MeV (-239.8 ppm) |
| ${}^{95}$Nb | 95 | 54 | L?-pending | binding_energy | — | 821.4853 | — | 88384.1807 MeV (-237.2 ppm) |
| ${}^{96}$Nb | 96 | 55 | L?-pending | binding_energy | — | 828.3731 | — | 89316.8580 MeV (-234.8 ppm) |
| ${}^{97}$Nb | 97 | 56 | L?-pending | binding_energy | — | 836.4444 | — | 90248.3519 MeV (-232.3 ppm) |
| ${}^{98}$Nb | 98 | 57 | L?-pending | binding_energy | — | 842.4376 | — | 91181.9239 MeV (-230.0 ppm) |
| ${}^{99}$Nb | 99 | 58 | L?-pending | binding_energy | — | 849.3196 | — | 92114.6071 MeV (-227.6 ppm) |
| ${}^{100}$Nb | 100 | 59 | L?-pending | binding_energy | — | 854.8468 | — | 93048.6450 MeV (-225.4 ppm) |
| ${}^{101}$Nb | 101 | 60 | L?-pending | binding_energy | — | 862.0184 | — | 93981.0387 MeV (-223.1 ppm) |
| ${}^{102}$Nb | 102 | 61 | L?-pending | binding_energy | — | 867.4965 | — | 94915.1257 MeV (-220.9 ppm) |
| ${}^{103}$Nb | 103 | 62 | L?-pending | binding_energy | — | 874.2982 | — | 95847.8892 MeV (-218.8 ppm) |
| ${}^{104}$Nb | 104 | 63 | L?-pending | binding_energy | — | 879.1519 | — | 96782.6007 MeV (-216.7 ppm) |
| ${}^{105}$Nb | 105 | 64 | L?-pending | binding_energy | — | 885.3277 | — | 97715.9901 MeV (-214.6 ppm) |
| ${}^{106}$Nb | 106 | 65 | L?-pending | binding_energy | — | 889.6862 | — | 98651.1968 MeV (-212.6 ppm) |
| ${}^{107}$Nb | 107 | 66 | L?-pending | binding_energy | — | 895.2786 | — | 99585.1695 MeV (-210.6 ppm) |
| ${}^{108}$Nb | 108 | 67 | L?-pending | binding_energy | — | 899.1713 | — | 100520.8420 MeV (-208.6 ppm) |
| ${}^{109}$Nb | 109 | 68 | L?-pending | binding_energy | — | 904.3872 | — | 101455.1913 MeV (-206.7 ppm) |
| ${}^{110}$Nb | 110 | 69 | L?-pending | binding_energy | — | 908.0787 | — | 102391.0650 MeV (-204.8 ppm) |
| ${}^{111}$Nb | 111 | 70 | L?-pending | binding_energy | — | 912.7530 | — | 103325.9559 MeV (-202.5 ppm) |
| ${}^{112}$Nb | 112 | 71 | L?-pending | binding_energy | — | 915.9360 | — | 104262.3381 MeV (-200.7 ppm) |
| ${}^{113}$Nb | 113 | 72 | L?-pending | binding_energy | — | 920.1590 | — | 105197.6803 MeV (-199.0 ppm) |
| ${}^{114}$Nb | 114 | 73 | L?-pending | binding_energy | — | 923.0580 | — | 106134.3464 MeV (-198.0 ppm) |
| ${}^{115}$Nb | 115 | 74 | L?-pending | binding_energy | — | 927.0150 | — | 107069.9546 MeV (-196.0 ppm) |
| ${}^{116}$Nb | 116 | 75 | L?-pending | binding_energy | — | 929.3920 | — | 108007.1428 MeV (-193.9 ppm) |

### Molybdenum (Z = 42)

_0 of 39 isotopes with a framework prediction; 39 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{81}$Mo | 81 | 39 | L?-pending | binding_energy | — | 652.3740 | — | 75398.0860 MeV (-284.8 ppm) |
| ${}^{82}$Mo | 82 | 40 | L?-pending | binding_energy | — | 669.3660 | — | 76320.6592 MeV (-281.5 ppm) |
| ${}^{83}$Mo | 83 | 41 | L?-pending | binding_energy | — | 683.4220 | — | 77246.1684 MeV (-278.3 ppm) |
| ${}^{84}$Mo | 84 | 42 | L?-pending | binding_energy | — | 699.3000 | — | 78169.8556 MeV (-274.7 ppm) |
| ${}^{85}$Mo | 85 | 43 | L?-pending | binding_energy | — | 710.7132 | — | 79098.0075 MeV (-271.5 ppm) |
| ${}^{86}$Mo | 86 | 44 | L?-pending | binding_energy | — | 725.3857 | — | 80022.9002 MeV (-268.4 ppm) |
| ${}^{87}$Mo | 87 | 45 | L?-pending | binding_energy | — | 736.2309 | — | 80951.6202 MeV (-265.3 ppm) |
| ${}^{88}$Mo | 88 | 46 | L?-pending | binding_energy | — | 750.1040 | — | 81877.3123 MeV (-262.3 ppm) |
| ${}^{89}$Mo | 89 | 47 | L?-pending | binding_energy | — | 760.5037 | — | 82806.4778 MeV (-259.4 ppm) |
| ${}^{90}$Mo | 90 | 48 | L?-pending | binding_energy | — | 773.7326 | — | 83732.8141 MeV (-256.5 ppm) |
| ${}^{91}$Mo | 91 | 49 | L?-pending | binding_energy | — | 783.8402 | — | 84662.2717 MeV (-253.7 ppm) |
| ${}^{92}$Mo | 92 | 50 | L?-pending | binding_energy | — | 796.5113 | — | 85589.1658 MeV (-250.9 ppm) |
| ${}^{93}$Mo | 93 | 51 | L?-pending | binding_energy | — | 804.5811 | — | 86520.6611 MeV (-248.2 ppm) |
| ${}^{94}$Mo | 94 | 52 | L?-pending | binding_energy | — | 814.2594 | — | 87450.5480 MeV (-245.6 ppm) |
| ${}^{95}$Mo | 95 | 53 | L?-pending | binding_energy | — | 821.6285 | — | 88382.7441 MeV (-243.0 ppm) |
| ${}^{96}$Mo | 96 | 54 | L?-pending | binding_energy | — | 830.7828 | — | 89313.1549 MeV (-240.5 ppm) |
| ${}^{97}$Mo | 97 | 55 | L?-pending | binding_energy | — | 837.6040 | — | 90245.8990 MeV (-238.0 ppm) |
| ${}^{98}$Mo | 98 | 56 | L?-pending | binding_energy | — | 846.2466 | — | 91176.8216 MeV (-235.6 ppm) |
| ${}^{99}$Mo | 99 | 57 | L?-pending | binding_energy | — | 852.1720 | — | 92110.4613 MeV (-233.2 ppm) |
| ${}^{100}$Mo | 100 | 58 | L?-pending | binding_energy | — | 860.4663 | — | 93041.7323 MeV (-230.9 ppm) |
| ${}^{101}$Mo | 101 | 59 | L?-pending | binding_energy | — | 865.8645 | — | 93975.8992 MeV (-228.6 ppm) |
| ${}^{102}$Mo | 102 | 60 | L?-pending | binding_energy | — | 873.9767 | — | 94907.3522 MeV (-226.3 ppm) |
| ${}^{103}$Mo | 103 | 61 | L?-pending | binding_energy | — | 879.4415 | — | 95841.4526 MeV (-224.1 ppm) |
| ${}^{104}$Mo | 104 | 62 | L?-pending | binding_energy | — | 886.9023 | — | 96773.5570 MeV (-222.0 ppm) |
| ${}^{105}$Mo | 105 | 63 | L?-pending | binding_energy | — | 891.9606 | — | 97708.0638 MeV (-219.9 ppm) |
| ${}^{106}$Mo | 106 | 64 | L?-pending | binding_energy | — | 898.8291 | — | 98640.7605 MeV (-217.8 ppm) |
| ${}^{107}$Mo | 107 | 65 | L?-pending | binding_energy | — | 903.3174 | — | 99575.8374 MeV (-215.7 ppm) |
| ${}^{108}$Mo | 108 | 66 | L?-pending | binding_energy | — | 909.5931 | — | 100509.1269 MeV (-213.7 ppm) |
| ${}^{109}$Mo | 109 | 67 | L?-pending | binding_energy | — | 913.5744 | — | 101444.7108 MeV (-211.8 ppm) |
| ${}^{110}$Mo | 110 | 68 | L?-pending | binding_energy | — | 919.5222 | — | 102378.3281 MeV (-209.8 ppm) |
| ${}^{111}$Mo | 111 | 69 | L?-pending | binding_energy | — | 922.9975 | — | 103314.4180 MeV (-207.9 ppm) |
| ${}^{112}$Mo | 112 | 70 | L?-pending | binding_energy | — | 928.5920 | — | 104248.3887 MeV (-205.9 ppm) |
| ${}^{113}$Mo | 113 | 71 | L?-pending | binding_energy | — | 931.7980 | — | 105184.7479 MeV (-203.7 ppm) |
| ${}^{114}$Mo | 114 | 72 | L?-pending | binding_energy | — | 936.9660 | — | 106119.1451 MeV (-202.6 ppm) |
| ${}^{115}$Mo | 115 | 73 | L?-pending | binding_energy | — | 939.8950 | — | 107055.7813 MeV (-200.7 ppm) |
| ${}^{116}$Mo | 116 | 74 | L?-pending | binding_energy | — | 944.5880 | — | 107990.6535 MeV (-198.6 ppm) |
| ${}^{117}$Mo | 117 | 75 | L?-pending | binding_energy | — | 947.2320 | — | 108927.5747 MeV (-197.8 ppm) |
| ${}^{118}$Mo | 118 | 76 | L?-pending | binding_energy | — | 951.9060 | — | 109862.4658 MeV (-195.4 ppm) |
| ${}^{119}$Mo | 119 | 77 | L?-pending | binding_energy | — | 954.2610 | — | 110799.6760 MeV (-194.4 ppm) |

### Technetium (Z = 43)

_0 of 40 isotopes with a framework prediction; 40 of 40 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{83}$Tc | 83 | 40 | L?-pending | binding_energy | — | 667.5690 | — | 77260.7281 MeV (-284.2 ppm) |
| ${}^{84}$Tc | 84 | 41 | L?-pending | binding_energy | — | 682.0800 | — | 78185.7822 MeV (-281.6 ppm) |
| ${}^{85}$Tc | 85 | 42 | L?-pending | binding_energy | — | 698.2750 | — | 79109.1524 MeV (-278.0 ppm) |
| ${}^{86}$Tc | 86 | 43 | L?-pending | binding_energy | — | 712.0800 | — | 80034.9126 MeV (-274.9 ppm) |
| ${}^{87}$Tc | 87 | 44 | L?-pending | binding_energy | — | 726.2538 | — | 80960.3040 MeV (-271.6 ppm) |
| ${}^{88}$Tc | 88 | 45 | L?-pending | binding_energy | — | 738.3054 | — | 81887.8176 MeV (-268.5 ppm) |
| ${}^{89}$Tc | 89 | 46 | L?-pending | binding_energy | — | 752.1012 | — | 82813.5869 MeV (-265.5 ppm) |
| ${}^{90}$Tc | 90 | 47 | L?-pending | binding_energy | — | 763.5024 | — | 83741.7509 MeV (-262.6 ppm) |
| ${}^{91}$Tc | 91 | 48 | L?-pending | binding_energy | — | 776.8357 | — | 84667.9828 MeV (-259.7 ppm) |
| ${}^{92}$Tc | 92 | 49 | L?-pending | binding_energy | — | 787.8460 | — | 85596.5377 MeV (-256.9 ppm) |
| ${}^{93}$Tc | 93 | 50 | L?-pending | binding_energy | — | 800.5978 | — | 86523.3511 MeV (-254.1 ppm) |
| ${}^{94}$Tc | 94 | 51 | L?-pending | binding_energy | — | 809.2213 | — | 87454.2928 MeV (-251.4 ppm) |
| ${}^{95}$Tc | 95 | 52 | L?-pending | binding_energy | — | 819.1557 | — | 88383.9236 MeV (-248.8 ppm) |
| ${}^{96}$Tc | 96 | 53 | L?-pending | binding_energy | — | 827.0273 | — | 89315.6172 MeV (-246.2 ppm) |
| ${}^{97}$Tc | 97 | 54 | L?-pending | binding_energy | — | 836.5014 | — | 90245.7083 MeV (-243.7 ppm) |
| ${}^{98}$Tc | 98 | 55 | L?-pending | binding_energy | — | 843.7805 | — | 91177.9944 MeV (-241.2 ppm) |
| ${}^{99}$Tc | 99 | 56 | L?-pending | binding_energy | — | 852.7474 | — | 92108.5926 MeV (-238.7 ppm) |
| ${}^{100}$Tc | 100 | 57 | L?-pending | binding_energy | — | 859.5118 | — | 93041.3933 MeV (-236.4 ppm) |
| ${}^{101}$Tc | 101 | 58 | L?-pending | binding_energy | — | 867.9068 | — | 93972.5636 MeV (-234.0 ppm) |
| ${}^{102}$Tc | 102 | 59 | L?-pending | binding_energy | — | 874.2064 | — | 94905.8291 MeV (-231.7 ppm) |
| ${}^{103}$Tc | 103 | 60 | L?-pending | binding_energy | — | 882.3088 | — | 95837.2920 MeV (-229.5 ppm) |
| ${}^{104}$Tc | 104 | 61 | L?-pending | binding_energy | — | 888.2751 | — | 96770.8908 MeV (-227.3 ppm) |
| ${}^{105}$Tc | 105 | 62 | L?-pending | binding_energy | — | 896.1338 | — | 97702.5973 MeV (-225.1 ppm) |
| ${}^{106}$Tc | 106 | 63 | L?-pending | binding_energy | — | 901.6950 | — | 98636.6013 MeV (-223.0 ppm) |
| ${}^{107}$Tc | 107 | 64 | L?-pending | binding_energy | — | 908.7401 | — | 99569.1214 MeV (-220.9 ppm) |
| ${}^{108}$Tc | 108 | 65 | L?-pending | binding_energy | — | 913.9843 | — | 100503.4424 MeV (-218.8 ppm) |
| ${}^{109}$Tc | 109 | 66 | L?-pending | binding_energy | — | 920.4156 | — | 101436.5763 MeV (-216.8 ppm) |
| ${}^{110}$Tc | 110 | 67 | L?-pending | binding_energy | — | 925.2386 | — | 102371.3184 MeV (-214.8 ppm) |
| ${}^{111}$Tc | 111 | 68 | L?-pending | binding_energy | — | 931.3001 | — | 103304.8222 MeV (-212.9 ppm) |
| ${}^{112}$Tc | 112 | 69 | L?-pending | binding_energy | — | 935.6056 | — | 104240.0818 MeV (-211.0 ppm) |
| ${}^{113}$Tc | 113 | 70 | L?-pending | binding_energy | — | 941.2296 | — | 105174.0230 MeV (-209.1 ppm) |
| ${}^{114}$Tc | 114 | 71 | L?-pending | binding_energy | — | 945.0896 | — | 106109.7281 MeV (-207.3 ppm) |
| ${}^{115}$Tc | 115 | 72 | L?-pending | binding_energy | — | 950.3600 | — | 107044.0230 MeV (-205.5 ppm) |
| ${}^{116}$Tc | 116 | 73 | L?-pending | binding_energy | — | 953.8680 | — | 107980.0801 MeV (-203.9 ppm) |
| ${}^{117}$Tc | 117 | 74 | L?-pending | binding_energy | — | 958.8150 | — | 108914.6983 MeV (-201.7 ppm) |
| ${}^{118}$Tc | 118 | 75 | L?-pending | binding_energy | — | 962.0540 | — | 109851.0245 MeV (-200.1 ppm) |
| ${}^{119}$Tc | 119 | 76 | L?-pending | binding_energy | — | 966.9940 | — | 110785.6497 MeV (-198.4 ppm) |
| ${}^{120}$Tc | 120 | 77 | L?-pending | binding_energy | — | 969.9600 | — | 111722.2489 MeV (-197.3 ppm) |
| ${}^{121}$Tc | 121 | 78 | L?-pending | binding_energy | — | 974.5340 | — | 112657.2401 MeV (-195.3 ppm) |
| ${}^{122}$Tc | 122 | 79 | L?-pending | binding_energy | — | 977.3420 | — | 113593.9973 MeV (-193.4 ppm) |

### Ruthenium (Z = 44)

_0 of 41 isotopes with a framework prediction; 41 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{85}$Ru | 85 | 41 | L?-pending | binding_energy | — | 682.2950 | — | 79123.8391 MeV (-284.7 ppm) |
| ${}^{86}$Ru | 86 | 42 | L?-pending | binding_energy | — | 699.4380 | — | 80046.2613 MeV (-280.5 ppm) |
| ${}^{87}$Ru | 87 | 43 | L?-pending | binding_energy | — | 713.4870 | — | 80971.7775 MeV (-277.5 ppm) |
| ${}^{88}$Ru | 88 | 44 | L?-pending | binding_energy | — | 730.2240 | — | 81894.6056 MeV (-275.1 ppm) |
| ${}^{89}$Ru | 89 | 45 | L?-pending | binding_energy | — | 742.2935 | — | 82822.1014 MeV (-271.6 ppm) |
| ${}^{90}$Ru | 90 | 46 | L?-pending | binding_energy | — | 756.8792 | — | 83747.0809 MeV (-268.6 ppm) |
| ${}^{91}$Ru | 91 | 47 | L?-pending | binding_energy | — | 768.3065 | — | 84675.2187 MeV (-265.7 ppm) |
| ${}^{92}$Ru | 92 | 48 | L?-pending | binding_energy | — | 782.4392 | — | 85600.6512 MeV (-262.8 ppm) |
| ${}^{93}$Ru | 93 | 49 | L?-pending | binding_energy | — | 793.4260 | — | 86529.2295 MeV (-260.0 ppm) |
| ${}^{94}$Ru | 94 | 50 | L?-pending | binding_energy | — | 806.8642 | — | 87455.3565 MeV (-257.3 ppm) |
| ${}^{95}$Ru | 95 | 51 | L?-pending | binding_energy | — | 815.8097 | — | 88385.9762 MeV (-254.6 ppm) |
| ${}^{96}$Ru | 96 | 52 | L?-pending | binding_energy | — | 826.5036 | — | 89314.8475 MeV (-251.9 ppm) |
| ${}^{97}$Ru | 97 | 53 | L?-pending | binding_energy | — | 834.6152 | — | 90246.3012 MeV (-249.3 ppm) |
| ${}^{98}$Ru | 98 | 54 | L?-pending | binding_energy | — | 844.7908 | — | 91175.6907 MeV (-246.8 ppm) |
| ${}^{99}$Ru | 99 | 55 | L?-pending | binding_energy | — | 852.2626 | — | 92107.7841 MeV (-244.3 ppm) |
| ${}^{100}$Ru | 100 | 56 | L?-pending | binding_energy | — | 861.9359 | — | 93037.6759 MeV (-241.9 ppm) |
| ${}^{101}$Ru | 101 | 57 | L?-pending | binding_energy | — | 868.7380 | — | 93970.4391 MeV (-239.5 ppm) |
| ${}^{102}$Ru | 102 | 58 | L?-pending | binding_energy | — | 877.9576 | — | 94900.7846 MeV (-237.1 ppm) |
| ${}^{103}$Ru | 103 | 59 | L?-pending | binding_energy | — | 884.1897 | — | 95834.1178 MeV (-234.8 ppm) |
| ${}^{104}$Ru | 104 | 60 | L?-pending | binding_energy | — | 893.0896 | — | 96764.7830 MeV (-232.5 ppm) |
| ${}^{105}$Ru | 105 | 61 | L?-pending | binding_energy | — | 898.9997 | — | 97698.4381 MeV (-230.3 ppm) |
| ${}^{106}$Ru | 106 | 62 | L?-pending | binding_energy | — | 907.4597 | — | 98629.5433 MeV (-228.2 ppm) |
| ${}^{107}$Ru | 107 | 63 | L?-pending | binding_energy | — | 913.0703 | — | 99563.4978 MeV (-226.0 ppm) |
| ${}^{108}$Ru | 108 | 64 | L?-pending | binding_energy | — | 920.9405 | — | 100495.1929 MeV (-223.9 ppm) |
| ${}^{109}$Ru | 109 | 65 | L?-pending | binding_energy | — | 926.0889 | — | 101429.6097 MeV (-221.9 ppm) |
| ${}^{110}$Ru | 110 | 66 | L?-pending | binding_energy | — | 933.4944 | — | 102361.7694 MeV (-219.9 ppm) |
| ${}^{111}$Ru | 111 | 67 | L?-pending | binding_energy | — | 938.2784 | — | 103296.5505 MeV (-217.9 ppm) |
| ${}^{112}$Ru | 112 | 68 | L?-pending | binding_energy | — | 945.1952 | — | 104229.1988 MeV (-215.9 ppm) |
| ${}^{113}$Ru | 113 | 69 | L?-pending | binding_energy | — | 949.5035 | — | 105164.4558 MeV (-214.0 ppm) |
| ${}^{114}$Ru | 114 | 70 | L?-pending | binding_energy | — | 955.9282 | — | 106097.5962 MeV (-212.1 ppm) |
| ${}^{115}$Ru | 115 | 71 | L?-pending | binding_energy | — | 959.8836 | — | 107033.2060 MeV (-210.3 ppm) |
| ${}^{116}$Ru | 116 | 72 | L?-pending | binding_energy | — | 965.9185 | — | 107966.7363 MeV (-208.5 ppm) |
| ${}^{117}$Ru | 117 | 73 | L?-pending | binding_energy | — | 969.4108 | — | 108902.8092 MeV (-206.7 ppm) |
| ${}^{118}$Ru | 118 | 74 | L?-pending | binding_energy | — | 975.0340 | — | 109836.7512 MeV (-205.3 ppm) |
| ${}^{119}$Ru | 119 | 75 | L?-pending | binding_energy | — | 978.1800 | — | 110773.1704 MeV (-203.5 ppm) |
| ${}^{120}$Ru | 120 | 76 | L?-pending | binding_energy | — | 983.8800 | — | 111707.0356 MeV (-201.7 ppm) |
| ${}^{121}$Ru | 121 | 77 | L?-pending | binding_energy | — | 986.8760 | — | 112643.6047 MeV (-200.2 ppm) |
| ${}^{122}$Ru | 122 | 78 | L?-pending | binding_energy | — | 992.1040 | — | 113577.9419 MeV (-198.6 ppm) |
| ${}^{123}$Ru | 123 | 79 | L?-pending | binding_energy | — | 994.9470 | — | 114514.6641 MeV (-197.0 ppm) |
| ${}^{124}$Ru | 124 | 80 | L?-pending | binding_energy | — | 1000.0600 | — | 115449.1163 MeV (-195.4 ppm) |
| ${}^{125}$Ru | 125 | 81 | L?-pending | binding_energy | — | 1002.8750 | — | 116385.8665 MeV (-193.5 ppm) |

### Rhodium (Z = 45)

_0 of 41 isotopes with a framework prediction; 41 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{88}$Rh | 88 | 43 | L?-pending | binding_energy | — | 711.9200 | — | 81911.6163 MeV (-280.8 ppm) |
| ${}^{89}$Rh | 89 | 44 | L?-pending | binding_energy | — | 728.8210 | — | 82834.2805 MeV (-278.1 ppm) |
| ${}^{90}$Rh | 90 | 45 | L?-pending | binding_energy | — | 742.8600 | — | 83759.8067 MeV (-274.9 ppm) |
| ${}^{91}$Rh | 91 | 46 | L?-pending | binding_energy | — | 757.8480 | — | 84684.3839 MeV (-271.6 ppm) |
| ${}^{92}$Rh | 92 | 47 | L?-pending | binding_energy | — | 770.3547 | — | 85611.4423 MeV (-268.8 ppm) |
| ${}^{93}$Rh | 93 | 48 | L?-pending | binding_energy | — | 784.4388 | — | 86536.9235 MeV (-265.9 ppm) |
| ${}^{94}$Rh | 94 | 49 | L?-pending | binding_energy | — | 796.4059 | — | 87464.5215 MeV (-263.1 ppm) |
| ${}^{95}$Rh | 95 | 50 | L?-pending | binding_energy | — | 809.9102 | — | 88390.5824 MeV (-260.3 ppm) |
| ${}^{96}$Rh | 96 | 51 | L?-pending | binding_energy | — | 819.3287 | — | 89320.7291 MeV (-257.6 ppm) |
| ${}^{97}$Rh | 97 | 52 | L?-pending | binding_energy | — | 830.3098 | — | 90249.3132 MeV (-255.0 ppm) |
| ${}^{98}$Rh | 98 | 53 | L?-pending | binding_energy | — | 838.9588 | — | 91180.2294 MeV (-252.4 ppm) |
| ${}^{99}$Rh | 99 | 54 | L?-pending | binding_energy | — | 849.4394 | — | 92109.3139 MeV (-249.8 ppm) |
| ${}^{100}$Rh | 100 | 55 | L?-pending | binding_energy | — | 857.5173 | — | 93040.8012 MeV (-247.3 ppm) |
| ${}^{101}$Rh | 101 | 56 | L?-pending | binding_energy | — | 867.4099 | — | 93970.4738 MeV (-244.9 ppm) |
| ${}^{102}$Rh | 102 | 57 | L?-pending | binding_energy | — | 874.8521 | — | 94902.5968 MeV (-242.5 ppm) |
| ${}^{103}$Rh | 103 | 58 | L?-pending | binding_energy | — | 884.1718 | — | 95832.8422 MeV (-240.1 ppm) |
| ${}^{104}$Rh | 104 | 59 | L?-pending | binding_energy | — | 891.1708 | — | 96765.4085 MeV (-237.8 ppm) |
| ${}^{105}$Rh | 105 | 60 | L?-pending | binding_energy | — | 900.1341 | — | 97696.0104 MeV (-235.6 ppm) |
| ${}^{106}$Rh | 106 | 61 | L?-pending | binding_energy | — | 906.7168 | — | 98628.9929 MeV (-233.3 ppm) |
| ${}^{107}$Rh | 107 | 62 | L?-pending | binding_energy | — | 915.2891 | — | 99559.9857 MeV (-231.2 ppm) |
| ${}^{108}$Rh | 108 | 63 | L?-pending | binding_energy | — | 921.5279 | — | 100493.3121 MeV (-229.0 ppm) |
| ${}^{109}$Rh | 109 | 64 | L?-pending | binding_energy | — | 929.5673 | — | 101424.8379 MeV (-226.9 ppm) |
| ${}^{110}$Rh | 110 | 65 | L?-pending | binding_energy | — | 935.4681 | — | 102358.5023 MeV (-224.8 ppm) |
| ${}^{111}$Rh | 111 | 66 | L?-pending | binding_energy | — | 943.0146 | — | 103290.5210 MeV (-222.8 ppm) |
| ${}^{112}$Rh | 112 | 67 | L?-pending | binding_energy | — | 948.5131 | — | 104224.5877 MeV (-220.8 ppm) |
| ${}^{113}$Rh | 113 | 68 | L?-pending | binding_energy | — | 955.6203 | — | 105157.0457 MeV (-218.9 ppm) |
| ${}^{114}$Rh | 114 | 69 | L?-pending | binding_energy | — | 960.6349 | — | 106091.5962 MeV (-216.9 ppm) |
| ${}^{115}$Rh | 115 | 70 | L?-pending | binding_energy | — | 967.2252 | — | 107024.5711 MeV (-215.1 ppm) |
| ${}^{116}$Rh | 116 | 71 | L?-pending | binding_energy | — | 971.8030 | — | 107959.5585 MeV (-213.2 ppm) |
| ${}^{117}$Rh | 117 | 72 | L?-pending | binding_energy | — | 978.0354 | — | 108892.8913 MeV (-211.4 ppm) |
| ${}^{118}$Rh | 118 | 73 | L?-pending | binding_energy | — | 982.0968 | — | 109828.3951 MeV (-209.6 ppm) |
| ${}^{119}$Rh | 119 | 74 | L?-pending | binding_energy | — | 988.1040 | — | 110761.9530 MeV (-207.8 ppm) |
| ${}^{120}$Rh | 120 | 75 | L?-pending | binding_energy | — | 991.9200 | — | 111697.7022 MeV (-205.6 ppm) |
| ${}^{121}$Rh | 121 | 76 | L?-pending | binding_energy | — | 997.6740 | — | 112631.5134 MeV (-204.4 ppm) |
| ${}^{122}$Rh | 122 | 77 | L?-pending | binding_energy | — | 1001.3760 | — | 113567.3766 MeV (-202.7 ppm) |
| ${}^{123}$Rh | 123 | 78 | L?-pending | binding_energy | — | 1006.7550 | — | 114501.5628 MeV (-201.0 ppm) |
| ${}^{124}$Rh | 124 | 79 | L?-pending | binding_energy | — | 1010.3520 | — | 115437.5310 MeV (-199.4 ppm) |
| ${}^{125}$Rh | 125 | 80 | L?-pending | binding_energy | — | 1015.5000 | — | 116371.9481 MeV (-197.5 ppm) |
| ${}^{126}$Rh | 126 | 81 | L?-pending | binding_energy | — | 1018.9620 | — | 117308.0513 MeV (-196.1 ppm) |
| ${}^{127}$Rh | 127 | 82 | L?-pending | binding_energy | — | 1023.6200 | — | 118242.9585 MeV (-195.0 ppm) |
| ${}^{128}$Rh | 128 | 83 | L?-pending | binding_energy | — | 1025.2800 | — | 119180.8637 MeV (-193.3 ppm) |

### Palladium (Z = 46)

_0 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{90}$Pd | 90 | 44 | L?-pending | binding_energy | — | 730.1700 | — | 83771.2033 MeV (-281.1 ppm) |
| ${}^{91}$Pd | 91 | 45 | L?-pending | binding_energy | — | 744.6530 | — | 84696.2855 MeV (-277.5 ppm) |
| ${}^{92}$Pd | 92 | 46 | L?-pending | binding_energy | — | 761.3524 | — | 85619.1513 MeV (-274.7 ppm) |
| ${}^{93}$Pd | 93 | 47 | L?-pending | binding_energy | — | 773.6264 | — | 86546.4425 MeV (-271.8 ppm) |
| ${}^{94}$Pd | 94 | 48 | L?-pending | binding_energy | — | 788.8182 | — | 87470.8159 MeV (-268.9 ppm) |
| ${}^{95}$Pd | 95 | 49 | L?-pending | binding_energy | — | 800.7532 | — | 88398.4461 MeV (-266.1 ppm) |
| ${}^{96}$Pd | 96 | 50 | L?-pending | binding_energy | — | 815.0420 | — | 89323.7225 MeV (-263.3 ppm) |
| ${}^{97}$Pd | 97 | 51 | L?-pending | binding_energy | — | 824.7357 | — | 90253.5939 MeV (-260.6 ppm) |
| ${}^{98}$Pd | 98 | 52 | L?-pending | binding_energy | — | 836.3222 | — | 91181.5726 MeV (-258.0 ppm) |
| ${}^{99}$Pd | 99 | 53 | L?-pending | binding_energy | — | 845.2554 | — | 92112.2046 MeV (-255.4 ppm) |
| ${}^{100}$Pd | 100 | 54 | L?-pending | binding_energy | — | 856.3565 | — | 93040.6687 MeV (-252.8 ppm) |
| ${}^{101}$Pd | 101 | 55 | L?-pending | binding_energy | — | 864.6473 | — | 93971.9431 MeV (-250.3 ppm) |
| ${}^{102}$Pd | 102 | 56 | L?-pending | binding_energy | — | 875.1894 | — | 94900.9661 MeV (-247.9 ppm) |
| ${}^{103}$Pd | 103 | 57 | L?-pending | binding_energy | — | 882.8148 | — | 95832.9060 MeV (-245.5 ppm) |
| ${}^{104}$Pd | 104 | 58 | L?-pending | binding_energy | — | 892.8242 | — | 96762.4617 MeV (-243.1 ppm) |
| ${}^{105}$Pd | 105 | 59 | L?-pending | binding_energy | — | 899.9183 | — | 97694.9328 MeV (-240.8 ppm) |
| ${}^{106}$Pd | 106 | 60 | L?-pending | binding_energy | — | 909.4793 | — | 98624.9370 MeV (-238.5 ppm) |
| ${}^{107}$Pd | 107 | 61 | L?-pending | binding_energy | — | 916.0157 | — | 99557.9658 MeV (-236.3 ppm) |
| ${}^{108}$Pd | 108 | 62 | L?-pending | binding_energy | — | 925.2386 | — | 100488.3081 MeV (-234.1 ppm) |
| ${}^{109}$Pd | 109 | 63 | L?-pending | binding_energy | — | 931.3922 | — | 101421.7197 MeV (-232.0 ppm) |
| ${}^{110}$Pd | 110 | 64 | L?-pending | binding_energy | — | 940.1879 | — | 102352.4891 MeV (-229.9 ppm) |
| ${}^{111}$Pd | 111 | 65 | L?-pending | binding_energy | — | 945.9142 | — | 103286.3280 MeV (-227.8 ppm) |
| ${}^{112}$Pd | 112 | 66 | L?-pending | binding_energy | — | 954.3207 | — | 104217.4867 MeV (-225.7 ppm) |
| ${}^{113}$Pd | 113 | 67 | L?-pending | binding_energy | — | 959.6615 | — | 105151.7111 MeV (-223.7 ppm) |
| ${}^{114}$Pd | 114 | 68 | L?-pending | binding_energy | — | 967.6326 | — | 106083.3051 MeV (-221.8 ppm) |
| ${}^{115}$Pd | 115 | 69 | L?-pending | binding_energy | — | 972.6394 | — | 107017.8635 MeV (-219.8 ppm) |
| ${}^{116}$Pd | 116 | 70 | L?-pending | binding_energy | — | 980.1160 | — | 107949.9522 MeV (-217.9 ppm) |
| ${}^{117}$Pd | 117 | 71 | L?-pending | binding_energy | — | 984.7801 | — | 108884.8532 MeV (-216.1 ppm) |
| ${}^{118}$Pd | 118 | 72 | L?-pending | binding_energy | — | 991.8159 | — | 109817.3826 MeV (-214.2 ppm) |
| ${}^{119}$Pd | 119 | 73 | L?-pending | binding_energy | — | 995.9062 | — | 110752.8575 MeV (-212.4 ppm) |
| ${}^{120}$Pd | 120 | 74 | L?-pending | binding_energy | — | 1002.8498 | — | 111685.4791 MeV (-210.7 ppm) |
| ${}^{121}$Pd | 121 | 75 | L?-pending | binding_energy | — | 1006.8239 | — | 112621.0702 MeV (-208.9 ppm) |
| ${}^{122}$Pd | 122 | 76 | L?-pending | binding_energy | — | 1013.3290 | — | 113554.1302 MeV (-207.2 ppm) |
| ${}^{123}$Pd | 123 | 77 | L?-pending | binding_energy | — | 1017.2139 | — | 114489.8105 MeV (-205.5 ppm) |
| ${}^{124}$Pd | 124 | 78 | L?-pending | binding_energy | — | 1023.2480 | — | 115423.3416 MeV (-203.8 ppm) |
| ${}^{125}$Pd | 125 | 79 | L?-pending | binding_energy | — | 1026.8750 | — | 116359.2798 MeV (-202.1 ppm) |
| ${}^{126}$Pd | 126 | 80 | L?-pending | binding_energy | — | 1032.8220 | — | 117292.8980 MeV (-200.9 ppm) |
| ${}^{127}$Pd | 127 | 81 | L?-pending | binding_energy | — | 1036.3200 | — | 118228.9652 MeV (-199.3 ppm) |
| ${}^{128}$Pd | 128 | 82 | L?-pending | binding_energy | — | 1041.5360 | — | 119163.3144 MeV (-197.5 ppm) |
| ${}^{129}$Pd | 129 | 83 | L?-pending | binding_energy | — | 1043.0940 | — | 120101.3215 MeV (-195.9 ppm) |
| ${}^{130}$Pd | 130 | 84 | L?-pending | binding_energy | — | 1045.9800 | — | 121038.0007 MeV (-194.1 ppm) |
| ${}^{131}$Pd | 131 | 85 | L?-pending | binding_energy | — | 1047.0830 | — | 121976.4629 MeV (-192.8 ppm) |

### Silver (Z = 47)

_0 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{92}$Ag | 92 | 45 | L?-pending | binding_energy | — | 743.3600 | — | 85635.8504 MeV (-281.1 ppm) |
| ${}^{93}$Ag | 93 | 46 | L?-pending | binding_energy | — | 760.2750 | — | 86558.5006 MeV (-277.8 ppm) |
| ${}^{94}$Ag | 94 | 47 | L?-pending | binding_energy | — | 774.3720 | — | 87483.9688 MeV (-275.1 ppm) |
| ${}^{95}$Ag | 95 | 48 | L?-pending | binding_energy | — | 789.9250 | — | 88407.9809 MeV (-272.0 ppm) |
| ${}^{96}$Ag | 96 | 49 | L?-pending | binding_energy | — | 802.5879 | — | 89334.8833 MeV (-269.0 ppm) |
| ${}^{97}$Ag | 97 | 50 | L?-pending | binding_energy | — | 817.0516 | — | 90259.9847 MeV (-266.3 ppm) |
| ${}^{98}$Ag | 98 | 51 | L?-pending | binding_energy | — | 827.2853 | — | 91189.3162 MeV (-263.6 ppm) |
| ${}^{99}$Ag | 99 | 52 | L?-pending | binding_energy | — | 839.0027 | — | 92117.1640 MeV (-260.9 ppm) |
| ${}^{100}$Ag | 100 | 53 | L?-pending | binding_energy | — | 848.4995 | — | 93047.2324 MeV (-258.3 ppm) |
| ${}^{101}$Ag | 101 | 54 | L?-pending | binding_energy | — | 859.7672 | — | 93975.5298 MeV (-255.7 ppm) |
| ${}^{102}$Ag | 102 | 55 | L?-pending | binding_energy | — | 868.7508 | — | 94906.1114 MeV (-253.2 ppm) |
| ${}^{103}$Ag | 103 | 56 | L?-pending | binding_energy | — | 879.3782 | — | 95835.0493 MeV (-250.8 ppm) |
| ${}^{104}$Ag | 104 | 57 | L?-pending | binding_energy | — | 887.7632 | — | 96766.2294 MeV (-248.4 ppm) |
| ${}^{105}$Ag | 105 | 58 | L?-pending | binding_energy | — | 897.7889 | — | 97695.7689 MeV (-246.0 ppm) |
| ${}^{106}$Ag | 106 | 59 | L?-pending | binding_energy | — | 905.7318 | — | 98627.3912 MeV (-243.7 ppm) |
| ${}^{107}$Ag | 107 | 60 | L?-pending | binding_energy | — | 915.2674 | — | 99557.4207 MeV (-241.4 ppm) |
| ${}^{108}$Ag | 108 | 61 | L?-pending | binding_energy | — | 922.5388 | — | 100489.7145 MeV (-239.2 ppm) |
| ${}^{109}$Ag | 109 | 62 | L?-pending | binding_energy | — | 931.7228 | — | 101420.0957 MeV (-237.0 ppm) |
| ${}^{110}$Ag | 110 | 63 | L?-pending | binding_energy | — | 938.5320 | — | 102352.8517 MeV (-234.8 ppm) |
| ${}^{111}$Ag | 111 | 64 | L?-pending | binding_energy | — | 947.3614 | — | 103283.5874 MeV (-232.7 ppm) |
| ${}^{112}$Ag | 112 | 65 | L?-pending | binding_energy | — | 953.8010 | — | 104216.7130 MeV (-230.6 ppm) |
| ${}^{113}$Ag | 113 | 66 | L?-pending | binding_energy | — | 962.3155 | — | 105147.7638 MeV (-228.6 ppm) |
| ${}^{114}$Ag | 114 | 67 | L?-pending | binding_energy | — | 968.2908 | — | 106081.3537 MeV (-226.6 ppm) |
| ${}^{115}$Ag | 115 | 68 | L?-pending | binding_energy | — | 976.4139 | — | 107012.7958 MeV (-224.6 ppm) |
| ${}^{116}$Ag | 116 | 69 | L?-pending | binding_energy | — | 982.0452 | — | 107946.7296 MeV (-222.7 ppm) |
| ${}^{117}$Ag | 117 | 70 | L?-pending | binding_energy | — | 989.7558 | — | 108878.5842 MeV (-220.8 ppm) |
| ${}^{118}$Ag | 118 | 71 | L?-pending | binding_energy | — | 995.1990 | — | 109812.7062 MeV (-218.9 ppm) |
| ${}^{119}$Ag | 119 | 72 | L?-pending | binding_energy | — | 1002.3623 | — | 110745.1081 MeV (-217.1 ppm) |
| ${}^{120}$Ag | 120 | 73 | L?-pending | binding_energy | — | 1007.4394 | — | 111679.5962 MeV (-215.3 ppm) |
| ${}^{121}$Ag | 121 | 74 | L?-pending | binding_energy | — | 1014.2620 | — | 112612.3387 MeV (-213.5 ppm) |
| ${}^{122}$Ag | 122 | 75 | L?-pending | binding_energy | — | 1019.0366 | — | 113547.1293 MeV (-211.7 ppm) |
| ${}^{123}$Ag | 123 | 76 | L?-pending | binding_energy | — | 1025.5704 | — | 114480.1607 MeV (-210.0 ppm) |
| ${}^{124}$Ag | 124 | 77 | L?-pending | binding_energy | — | 1030.3031 | — | 115414.9932 MeV (-208.3 ppm) |
| ${}^{125}$Ag | 125 | 78 | L?-pending | binding_energy | — | 1036.6644 | — | 116348.1971 MeV (-206.6 ppm) |
| ${}^{126}$Ag | 126 | 79 | L?-pending | binding_energy | — | 1040.8860 | — | 117283.5407 MeV (-204.6 ppm) |
| ${}^{127}$Ag | 127 | 80 | L?-pending | binding_energy | — | 1046.9880 | — | 118217.0038 MeV (-203.8 ppm) |
| ${}^{128}$Ag | 128 | 81 | L?-pending | binding_energy | — | 1051.0080 | — | 119152.5490 MeV (-201.3 ppm) |
| ${}^{129}$Ag | 129 | 82 | L?-pending | binding_energy | — | 1056.2520 | — | 120086.8702 MeV (-199.8 ppm) |
| ${}^{130}$Ag | 130 | 83 | L?-pending | binding_energy | — | 1058.4600 | — | 121024.2274 MeV (-199.2 ppm) |
| ${}^{131}$Ag | 131 | 84 | L?-pending | binding_energy | — | 1061.3620 | — | 121960.8906 MeV (-197.5 ppm) |
| ${}^{132}$Ag | 132 | 85 | L?-pending | binding_energy | — | 1062.9960 | — | 122898.8218 MeV (-195.2 ppm) |
| ${}^{133}$Ag | 133 | 86 | L?-pending | binding_energy | — | 1065.7290 | — | 123835.6540 MeV (-193.6 ppm) |

### Cadmium (Z = 48)

_0 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{94}$Cd | 94 | 46 | L?-pending | binding_energy | — | 761.5880 | — | 87495.4594 MeV (-280.5 ppm) |
| ${}^{95}$Cd | 95 | 47 | L?-pending | binding_energy | — | 776.2450 | — | 88420.3676 MeV (-277.2 ppm) |
| ${}^{96}$Cd | 96 | 48 | L?-pending | binding_energy | — | 792.8640 | — | 89343.3138 MeV (-274.7 ppm) |
| ${}^{97}$Cd | 97 | 49 | L?-pending | binding_energy | — | 806.0992 | — | 90269.6437 MeV (-271.9 ppm) |
| ${}^{98}$Cd | 98 | 50 | L?-pending | binding_energy | — | 821.0729 | — | 91194.2352 MeV (-269.1 ppm) |
| ${}^{99}$Cd | 99 | 51 | L?-pending | binding_energy | — | 831.4390 | — | 92123.4344 MeV (-266.4 ppm) |
| ${}^{100}$Cd | 100 | 52 | L?-pending | binding_energy | — | 843.7737 | — | 93050.6648 MeV (-263.8 ppm) |
| ${}^{101}$Cd | 101 | 53 | L?-pending | binding_energy | — | 853.4869 | — | 93980.5168 MeV (-261.2 ppm) |
| ${}^{102}$Cd | 102 | 54 | L?-pending | binding_energy | — | 865.3815 | — | 94908.1874 MeV (-258.6 ppm) |
| ${}^{103}$Cd | 103 | 55 | L?-pending | binding_energy | — | 874.4447 | — | 95838.6893 MeV (-256.1 ppm) |
| ${}^{104}$Cd | 104 | 56 | L?-pending | binding_energy | — | 885.8328 | — | 96766.8665 MeV (-253.7 ppm) |
| ${}^{105}$Cd | 105 | 57 | L?-pending | binding_energy | — | 894.2696 | — | 97697.9949 MeV (-251.2 ppm) |
| ${}^{106}$Cd | 106 | 58 | L?-pending | binding_energy | — | 905.1392 | — | 98626.6904 MeV (-248.9 ppm) |
| ${}^{107}$Cd | 107 | 59 | L?-pending | binding_energy | — | 913.0687 | — | 99558.3261 MeV (-246.6 ppm) |
| ${}^{108}$Cd | 108 | 60 | L?-pending | binding_energy | — | 923.4021 | — | 100487.5579 MeV (-244.3 ppm) |
| ${}^{109}$Cd | 109 | 61 | L?-pending | binding_energy | — | 930.7253 | — | 101419.7998 MeV (-242.0 ppm) |
| ${}^{110}$Cd | 110 | 62 | L?-pending | binding_energy | — | 940.6403 | — | 102349.4501 MeV (-239.8 ppm) |
| ${}^{111}$Cd | 111 | 63 | L?-pending | binding_energy | — | 947.6159 | — | 103282.0397 MeV (-237.7 ppm) |
| ${}^{112}$Cd | 112 | 64 | L?-pending | binding_energy | — | 957.0098 | — | 104212.2109 MeV (-235.6 ppm) |
| ${}^{113}$Cd | 113 | 65 | L?-pending | binding_energy | — | 963.5496 | — | 105145.2364 MeV (-233.5 ppm) |
| ${}^{114}$Cd | 114 | 66 | L?-pending | binding_energy | — | 972.5925 | — | 106075.7586 MeV (-231.4 ppm) |
| ${}^{115}$Cd | 115 | 67 | L?-pending | binding_energy | — | 978.7334 | — | 107009.1829 MeV (-229.4 ppm) |
| ${}^{116}$Cd | 116 | 68 | L?-pending | binding_energy | — | 987.4327 | — | 107940.0488 MeV (-227.4 ppm) |
| ${}^{117}$Cd | 117 | 69 | L?-pending | binding_energy | — | 993.2100 | — | 108873.8367 MeV (-225.5 ppm) |
| ${}^{118}$Cd | 118 | 70 | L?-pending | binding_energy | — | 1001.5645 | — | 109805.0473 MeV (-223.6 ppm) |
| ${}^{119}$Cd | 119 | 71 | L?-pending | binding_energy | — | 1006.9111 | — | 110739.2659 MeV (-221.7 ppm) |
| ${}^{120}$Cd | 120 | 72 | L?-pending | binding_energy | — | 1014.9629 | — | 111670.7793 MeV (-219.8 ppm) |
| ${}^{121}$Cd | 121 | 73 | L?-pending | binding_energy | — | 1020.1507 | — | 112605.1567 MeV (-218.0 ppm) |
| ${}^{122}$Cd | 122 | 74 | L?-pending | binding_energy | — | 1027.7605 | — | 113537.1121 MeV (-216.2 ppm) |
| ${}^{123}$Cd | 123 | 75 | L?-pending | binding_energy | — | 1032.6336 | — | 114471.8041 MeV (-214.5 ppm) |
| ${}^{124}$Cd | 124 | 76 | L?-pending | binding_energy | — | 1039.9902 | — | 115404.0127 MeV (-212.7 ppm) |
| ${}^{125}$Cd | 125 | 77 | L?-pending | binding_energy | — | 1044.7102 | — | 116338.8580 MeV (-211.0 ppm) |
| ${}^{126}$Cd | 126 | 78 | L?-pending | binding_energy | — | 1051.6892 | — | 117271.4442 MeV (-209.4 ppm) |
| ${}^{127}$Cd | 127 | 79 | L?-pending | binding_energy | — | 1056.2459 | — | 118206.4526 MeV (-207.7 ppm) |
| ${}^{128}$Cd | 128 | 80 | L?-pending | binding_energy | — | 1062.8143 | — | 119139.4494 MeV (-206.1 ppm) |
| ${}^{129}$Cd | 129 | 81 | L?-pending | binding_energy | — | 1066.7695 | — | 120075.0594 MeV (-204.5 ppm) |
| ${}^{130}$Cd | 130 | 82 | L?-pending | binding_energy | — | 1072.8363 | — | 121008.5578 MeV (-202.9 ppm) |
| ${}^{131}$Cd | 131 | 83 | L?-pending | binding_energy | — | 1075.0018 | — | 121945.9575 MeV (-201.3 ppm) |
| ${}^{132}$Cd | 132 | 84 | L?-pending | binding_energy | — | 1078.3268 | — | 122882.1977 MeV (-199.8 ppm) |
| ${}^{133}$Cd | 133 | 85 | L?-pending | binding_energy | — | 1080.0930 | — | 123819.9966 MeV (-198.5 ppm) |
| ${}^{134}$Cd | 134 | 86 | L?-pending | binding_energy | — | 1083.5240 | — | 124756.1308 MeV (-197.3 ppm) |
| ${}^{135}$Cd | 135 | 87 | L?-pending | binding_energy | — | 1084.8600 | — | 125694.3600 MeV (-195.1 ppm) |

### Indium (Z = 49)

_0 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{96}$In | 96 | 47 | L?-pending | binding_energy | — | 774.6240 | — | 89360.2605 MeV (-280.6 ppm) |
| ${}^{97}$In | 97 | 48 | L?-pending | binding_energy | — | 792.0050 | — | 90282.4446 MeV (-277.9 ppm) |
| ${}^{98}$In | 98 | 49 | L?-pending | binding_energy | — | 806.5400 | — | 91207.4748 MeV (-274.5 ppm) |
| ${}^{99}$In | 99 | 50 | L?-pending | binding_energy | — | 822.0960 | — | 92131.4840 MeV (-271.9 ppm) |
| ${}^{100}$In | 100 | 51 | L?-pending | binding_energy | — | 832.9749 | — | 93060.1702 MeV (-269.2 ppm) |
| ${}^{101}$In | 101 | 52 | L?-pending | binding_energy | — | 845.4130 | — | 93987.2974 MeV (-266.6 ppm) |
| ${}^{102}$In | 102 | 53 | L?-pending | binding_energy | — | 855.6343 | — | 94916.6412 MeV (-264.0 ppm) |
| ${}^{103}$In | 103 | 54 | L?-pending | binding_energy | — | 867.6431 | — | 95844.1976 MeV (-261.4 ppm) |
| ${}^{104}$In | 104 | 55 | L?-pending | binding_energy | — | 877.2648 | — | 96774.1412 MeV (-258.9 ppm) |
| ${}^{105}$In | 105 | 56 | L?-pending | binding_energy | — | 888.7940 | — | 97702.1771 MeV (-256.5 ppm) |
| ${}^{106}$In | 106 | 57 | L?-pending | binding_energy | — | 897.8329 | — | 98632.7034 MeV (-254.0 ppm) |
| ${}^{107}$In | 107 | 58 | L?-pending | binding_energy | — | 908.8627 | — | 99561.2388 MeV (-251.7 ppm) |
| ${}^{108}$In | 108 | 59 | L?-pending | binding_energy | — | 917.4872 | — | 100492.1795 MeV (-249.3 ppm) |
| ${}^{109}$In | 109 | 60 | L?-pending | binding_energy | — | 927.9282 | — | 101421.3037 MeV (-247.1 ppm) |
| ${}^{110}$In | 110 | 61 | L?-pending | binding_energy | — | 935.9800 | — | 102352.8171 MeV (-244.8 ppm) |
| ${}^{111}$In | 111 | 62 | L?-pending | binding_energy | — | 945.9733 | — | 103282.3889 MeV (-242.6 ppm) |
| ${}^{112}$In | 112 | 63 | L?-pending | binding_energy | — | 953.6427 | — | 104214.2847 MeV (-240.5 ppm) |
| ${}^{113}$In | 113 | 64 | L?-pending | binding_energy | — | 963.0911 | — | 105144.4015 MeV (-238.3 ppm) |
| ${}^{114}$In | 114 | 65 | L?-pending | binding_energy | — | 970.3651 | — | 106076.6927 MeV (-236.2 ppm) |
| ${}^{115}$In | 115 | 66 | L?-pending | binding_energy | — | 979.4029 | — | 107007.2200 MeV (-234.2 ppm) |
| ${}^{116}$In | 116 | 67 | L?-pending | binding_energy | — | 986.1877 | — | 107940.0005 MeV (-232.2 ppm) |
| ${}^{117}$In | 117 | 68 | L?-pending | binding_energy | — | 994.9522 | — | 108870.8011 MeV (-230.2 ppm) |
| ${}^{118}$In | 118 | 69 | L?-pending | binding_energy | — | 1001.3087 | — | 109804.0098 MeV (-228.2 ppm) |
| ${}^{119}$In | 119 | 70 | L?-pending | binding_energy | — | 1009.8505 | — | 110735.0332 MeV (-226.3 ppm) |
| ${}^{120}$In | 120 | 71 | L?-pending | binding_energy | — | 1015.9509 | — | 111668.4980 MeV (-224.4 ppm) |
| ${}^{121}$In | 121 | 72 | L?-pending | binding_energy | — | 1024.1291 | — | 112599.8850 MeV (-222.6 ppm) |
| ${}^{122}$In | 122 | 73 | L?-pending | binding_energy | — | 1029.9372 | — | 113533.6421 MeV (-220.7 ppm) |
| ${}^{123}$In | 123 | 74 | L?-pending | binding_energy | — | 1037.8662 | — | 114465.2783 MeV (-218.9 ppm) |
| ${}^{124}$In | 124 | 75 | L?-pending | binding_energy | — | 1043.3762 | — | 115399.3334 MeV (-217.2 ppm) |
| ${}^{125}$In | 125 | 76 | L?-pending | binding_energy | — | 1050.9921 | — | 116331.2828 MeV (-215.4 ppm) |
| ${}^{126}$In | 126 | 77 | L?-pending | binding_energy | — | 1056.4604 | — | 117265.3796 MeV (-213.7 ppm) |
| ${}^{127}$In | 127 | 78 | L?-pending | binding_energy | — | 1063.6023 | — | 118197.8029 MeV (-212.0 ppm) |
| ${}^{128}$In | 128 | 79 | L?-pending | binding_energy | — | 1068.9838 | — | 119131.9865 MeV (-210.4 ppm) |
| ${}^{129}$In | 129 | 80 | L?-pending | binding_energy | — | 1075.6999 | — | 120064.8356 MeV (-208.7 ppm) |
| ${}^{130}$In | 130 | 81 | L?-pending | binding_energy | — | 1080.8429 | — | 120999.2579 MeV (-207.1 ppm) |
| ${}^{131}$In | 131 | 82 | L?-pending | binding_energy | — | 1087.0320 | — | 121932.6339 MeV (-205.6 ppm) |
| ${}^{132}$In | 132 | 83 | L?-pending | binding_energy | — | 1089.4905 | — | 122869.7406 MeV (-204.0 ppm) |
| ${}^{133}$In | 133 | 84 | L?-pending | binding_energy | — | 1092.8610 | — | 123805.9353 MeV (-202.6 ppm) |
| ${}^{134}$In | 134 | 85 | L?-pending | binding_energy | — | 1095.1820 | — | 124743.1795 MeV (-200.9 ppm) |
| ${}^{135}$In | 135 | 86 | L?-pending | binding_energy | — | 1098.3600 | — | 125679.5667 MeV (-199.1 ppm) |
| ${}^{136}$In | 136 | 87 | L?-pending | binding_energy | — | 1100.3760 | — | 126617.1158 MeV (-198.3 ppm) |
| ${}^{137}$In | 137 | 88 | L?-pending | binding_energy | — | 1103.2610 | — | 127553.7960 MeV (-196.5 ppm) |

### Tin (Z = 50)

_0 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{99}$Sn | 99 | 49 | L?-pending | binding_energy | — | 807.9390 | — | 92144.3477 MeV (-277.7 ppm) |
| ${}^{100}$Sn | 100 | 50 | L?-pending | binding_energy | — | 825.1626 | — | 93066.6893 MeV (-274.7 ppm) |
| ${}^{101}$Sn | 101 | 51 | L?-pending | binding_energy | — | 836.3914 | — | 93995.0256 MeV (-272.0 ppm) |
| ${}^{102}$Sn | 102 | 52 | L?-pending | binding_energy | — | 849.0920 | — | 94921.8902 MeV (-269.3 ppm) |
| ${}^{103}$Sn | 103 | 53 | L?-pending | binding_energy | — | 859.3290 | — | 95851.2184 MeV (-266.8 ppm) |
| ${}^{104}$Sn | 104 | 54 | L?-pending | binding_energy | — | 871.9268 | — | 96778.1858 MeV (-264.2 ppm) |
| ${}^{105}$Sn | 105 | 55 | L?-pending | binding_energy | — | 881.7090 | — | 97707.9687 MeV (-261.7 ppm) |
| ${}^{106}$Sn | 106 | 56 | L?-pending | binding_energy | — | 893.7961 | — | 98635.4469 MeV (-259.2 ppm) |
| ${}^{107}$Sn | 107 | 57 | L?-pending | binding_energy | — | 903.0259 | — | 99565.7822 MeV (-256.8 ppm) |
| ${}^{108}$Sn | 108 | 58 | L?-pending | binding_energy | — | 914.6549 | — | 100493.7184 MeV (-254.4 ppm) |
| ${}^{109}$Sn | 109 | 59 | L?-pending | binding_energy | — | 923.2865 | — | 101424.6520 MeV (-252.1 ppm) |
| ${}^{110}$Sn | 110 | 60 | L?-pending | binding_energy | — | 934.5696 | — | 102352.9341 MeV (-249.8 ppm) |
| ${}^{111}$Sn | 111 | 61 | L?-pending | binding_energy | — | 942.7375 | — | 103284.3314 MeV (-247.6 ppm) |
| ${}^{112}$Sn | 112 | 62 | L?-pending | binding_energy | — | 953.5253 | — | 104213.1088 MeV (-245.4 ppm) |
| ${}^{113}$Sn | 113 | 63 | L?-pending | binding_energy | — | 961.2697 | — | 105144.9295 MeV (-243.2 ppm) |
| ${}^{114}$Sn | 114 | 64 | L?-pending | binding_energy | — | 971.5726 | — | 106074.1918 MeV (-241.1 ppm) |
| ${}^{115}$Sn | 115 | 65 | L?-pending | binding_energy | — | 979.1181 | — | 107006.2116 MeV (-239.0 ppm) |
| ${}^{116}$Sn | 116 | 66 | L?-pending | binding_energy | — | 988.6815 | — | 107936.2133 MeV (-236.9 ppm) |
| ${}^{117}$Sn | 117 | 67 | L?-pending | binding_energy | — | 995.6246 | — | 108868.8354 MeV (-234.9 ppm) |
| ${}^{118}$Sn | 118 | 68 | L?-pending | binding_energy | — | 1004.9510 | — | 109799.0742 MeV (-232.9 ppm) |
| ${}^{119}$Sn | 119 | 69 | L?-pending | binding_energy | — | 1011.4345 | — | 110732.1559 MeV (-230.9 ppm) |
| ${}^{120}$Sn | 120 | 70 | L?-pending | binding_energy | — | 1020.5386 | — | 111662.6170 MeV (-229.0 ppm) |
| ${}^{121}$Sn | 121 | 71 | L?-pending | binding_energy | — | 1026.7088 | — | 112596.0120 MeV (-227.1 ppm) |
| ${}^{122}$Sn | 122 | 72 | L?-pending | binding_energy | — | 1035.5234 | — | 113526.7625 MeV (-225.3 ppm) |
| ${}^{123}$Sn | 123 | 73 | L?-pending | binding_energy | — | 1041.4694 | — | 114460.3817 MeV (-223.4 ppm) |
| ${}^{124}$Sn | 124 | 74 | L?-pending | binding_energy | — | 1049.9576 | — | 115391.4587 MeV (-221.6 ppm) |
| ${}^{125}$Sn | 125 | 75 | L?-pending | binding_energy | — | 1055.6911 | — | 116325.2904 MeV (-219.8 ppm) |
| ${}^{126}$Sn | 126 | 76 | L?-pending | binding_energy | — | 1063.8839 | — | 117256.6628 MeV (-218.1 ppm) |
| ${}^{127}$Sn | 127 | 77 | L?-pending | binding_energy | — | 1069.4096 | — | 118190.7022 MeV (-216.4 ppm) |
| ${}^{128}$Sn | 128 | 78 | L?-pending | binding_energy | — | 1077.3728 | — | 119122.3042 MeV (-214.7 ppm) |
| ${}^{129}$Sn | 129 | 79 | L?-pending | binding_energy | — | 1082.6733 | — | 120056.5689 MeV (-213.0 ppm) |
| ${}^{130}$Sn | 130 | 80 | L?-pending | binding_energy | — | 1090.2862 | — | 120988.5212 MeV (-211.4 ppm) |
| ${}^{131}$Sn | 131 | 81 | L?-pending | binding_energy | — | 1095.4899 | — | 121922.8827 MeV (-209.8 ppm) |
| ${}^{132}$Sn | 132 | 82 | L?-pending | binding_energy | — | 1102.8432 | — | 122855.0946 MeV (-208.2 ppm) |
| ${}^{133}$Sn | 133 | 83 | L?-pending | binding_energy | — | 1105.2418 | — | 123792.2611 MeV (-206.6 ppm) |
| ${}^{134}$Sn | 134 | 84 | L?-pending | binding_energy | — | 1108.8730 | — | 124728.1951 MeV (-205.1 ppm) |
| ${}^{135}$Sn | 135 | 85 | L?-pending | binding_energy | — | 1111.1428 | — | 125665.4905 MeV (-203.5 ppm) |
| ${}^{136}$Sn | 136 | 86 | L?-pending | binding_energy | — | 1114.7920 | — | 126601.4065 MeV (-202.3 ppm) |
| ${}^{137}$Sn | 137 | 87 | L?-pending | binding_energy | — | 1116.8240 | — | 127538.9397 MeV (-200.7 ppm) |
| ${}^{138}$Sn | 138 | 88 | L?-pending | binding_energy | — | 1120.2840 | — | 128475.0449 MeV (-199.5 ppm) |
| ${}^{139}$Sn | 139 | 89 | L?-pending | binding_energy | — | 1122.1470 | — | 129412.7471 MeV (-198.0 ppm) |
| ${}^{140}$Sn | 140 | 90 | L?-pending | binding_energy | — | 1125.3200 | — | 130349.1393 MeV (-195.9 ppm) |

### Antimony (Z = 51)

_0 of 41 isotopes with a framework prediction; 41 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{102}$Sb | 102 | 51 | L?-pending | binding_energy | — | 834.4620 | — | 94935.2269 MeV (-274.6 ppm) |
| ${}^{103}$Sb | 103 | 52 | L?-pending | binding_energy | — | 848.1020 | — | 95861.1521 MeV (-271.9 ppm) |
| ${}^{104}$Sb | 104 | 53 | L?-pending | binding_energy | — | 858.8320 | — | 96789.9873 MeV (-269.6 ppm) |
| ${}^{105}$Sb | 105 | 54 | L?-pending | binding_energy | — | 871.6042 | — | 97716.7803 MeV (-266.9 ppm) |
| ${}^{106}$Sb | 106 | 55 | L?-pending | binding_energy | — | 882.1333 | — | 98645.8163 MeV (-264.4 ppm) |
| ${}^{107}$Sb | 107 | 56 | L?-pending | binding_energy | — | 894.3846 | — | 99573.1302 MeV (-261.9 ppm) |
| ${}^{108}$Sb | 108 | 57 | L?-pending | binding_energy | — | 904.2480 | — | 100502.8320 MeV (-259.5 ppm) |
| ${}^{109}$Sb | 109 | 58 | L?-pending | binding_energy | — | 916.1250 | — | 101430.5202 MeV (-257.1 ppm) |
| ${}^{110}$Sb | 110 | 59 | L?-pending | binding_energy | — | 925.3950 | — | 102360.8153 MeV (-254.8 ppm) |
| ${}^{111}$Sb | 111 | 60 | L?-pending | binding_energy | — | 936.8534 | — | 103288.9222 MeV (-252.5 ppm) |
| ${}^{112}$Sb | 112 | 61 | L?-pending | binding_energy | — | 945.6869 | — | 104219.6539 MeV (-250.2 ppm) |
| ${}^{113}$Sb | 113 | 62 | L?-pending | binding_energy | — | 956.5762 | — | 105148.3297 MeV (-248.0 ppm) |
| ${}^{114}$Sb | 114 | 63 | L?-pending | binding_energy | — | 964.7272 | — | 106079.7439 MeV (-245.9 ppm) |
| ${}^{115}$Sb | 115 | 64 | L?-pending | binding_energy | — | 975.3053 | — | 107008.7310 MeV (-243.7 ppm) |
| ${}^{116}$Sb | 116 | 65 | L?-pending | binding_energy | — | 983.1952 | — | 107940.4063 MeV (-241.6 ppm) |
| ${}^{117}$Sb | 117 | 66 | L?-pending | binding_energy | — | 993.0841 | — | 108870.0826 MeV (-239.6 ppm) |
| ${}^{118}$Sb | 118 | 67 | L?-pending | binding_energy | — | 1000.5120 | — | 109802.2198 MeV (-237.5 ppm) |
| ${}^{119}$Sb | 119 | 68 | L?-pending | binding_energy | — | 1010.0627 | — | 110732.2343 MeV (-235.5 ppm) |
| ${}^{120}$Sb | 120 | 69 | L?-pending | binding_energy | — | 1017.0756 | — | 111664.7866 MeV (-233.6 ppm) |
| ${}^{121}$Sb | 121 | 70 | L?-pending | binding_energy | — | 1026.3289 | — | 112595.0985 MeV (-231.7 ppm) |
| ${}^{122}$Sb | 122 | 71 | L?-pending | binding_energy | — | 1033.1353 | — | 113527.8573 MeV (-229.7 ppm) |
| ${}^{123}$Sb | 123 | 72 | L?-pending | binding_energy | — | 1042.0953 | — | 114458.4625 MeV (-227.9 ppm) |
| ${}^{124}$Sb | 124 | 73 | L?-pending | binding_energy | — | 1048.5628 | — | 115391.5602 MeV (-226.0 ppm) |
| ${}^{125}$Sb | 125 | 74 | L?-pending | binding_energy | — | 1057.2702 | — | 116322.4180 MeV (-224.2 ppm) |
| ${}^{126}$Sb | 126 | 75 | L?-pending | binding_energy | — | 1063.4795 | — | 117255.7738 MeV (-222.5 ppm) |
| ${}^{127}$Sb | 127 | 76 | L?-pending | binding_energy | — | 1071.8560 | — | 118186.9625 MeV (-220.7 ppm) |
| ${}^{128}$Sb | 128 | 77 | L?-pending | binding_energy | — | 1077.8589 | — | 119120.5248 MeV (-219.0 ppm) |
| ${}^{129}$Sb | 129 | 78 | L?-pending | binding_energy | — | 1085.9297 | — | 120052.0192 MeV (-217.3 ppm) |
| ${}^{130}$Sb | 130 | 79 | L?-pending | binding_energy | — | 1091.6573 | — | 120985.8567 MeV (-215.6 ppm) |
| ${}^{131}$Sb | 131 | 80 | L?-pending | binding_energy | — | 1099.4244 | — | 121917.6549 MeV (-214.0 ppm) |
| ${}^{132}$Sb | 132 | 81 | L?-pending | binding_energy | — | 1105.1496 | — | 122851.4949 MeV (-212.3 ppm) |
| ${}^{133}$Sb | 133 | 82 | L?-pending | binding_energy | — | 1112.5091 | — | 123783.7005 MeV (-210.7 ppm) |
| ${}^{134}$Sb | 134 | 83 | L?-pending | binding_energy | — | 1115.6759 | — | 124720.0989 MeV (-209.2 ppm) |
| ${}^{135}$Sb | 135 | 84 | L?-pending | binding_energy | — | 1119.4186 | — | 125655.9214 MeV (-207.6 ppm) |
| ${}^{136}$Sb | 136 | 85 | L?-pending | binding_energy | — | 1122.3064 | — | 126592.5987 MeV (-206.1 ppm) |
| ${}^{137}$Sb | 137 | 86 | L?-pending | binding_energy | — | 1125.9313 | — | 127528.5391 MeV (-204.6 ppm) |
| ${}^{138}$Sb | 138 | 87 | L?-pending | binding_energy | — | 1128.5640 | — | 128465.4716 MeV (-202.9 ppm) |
| ${}^{139}$Sb | 139 | 88 | L?-pending | binding_energy | — | 1132.0160 | — | 129401.5847 MeV (-201.2 ppm) |
| ${}^{140}$Sb | 140 | 89 | L?-pending | binding_energy | — | 1134.4200 | — | 130338.7459 MeV (-199.7 ppm) |
| ${}^{141}$Sb | 141 | 90 | L?-pending | binding_energy | — | 1137.7290 | — | 131275.0021 MeV (-199.0 ppm) |
| ${}^{142}$Sb | 142 | 91 | L?-pending | binding_energy | — | 1139.8340 | — | 132212.4623 MeV (-197.3 ppm) |

### Tellurium (Z = 52)

_0 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{104}$Te | 104 | 52 | L?-pending | binding_energy | — | 848.3619 | — | 96799.1641 MeV (-274.7 ppm) |
| ${}^{105}$Te | 105 | 53 | L?-pending | binding_energy | — | 859.6179 | — | 97727.4733 MeV (-272.1 ppm) |
| ${}^{106}$Te | 106 | 54 | L?-pending | binding_energy | — | 873.0974 | — | 98653.5589 MeV (-269.5 ppm) |
| ${}^{107}$Te | 107 | 55 | L?-pending | binding_energy | — | 883.6060 | — | 99582.6155 MeV (-267.0 ppm) |
| ${}^{108}$Te | 108 | 56 | L?-pending | binding_energy | — | 896.8020 | — | 100508.9847 MeV (-264.6 ppm) |
| ${}^{109}$Te | 109 | 57 | L?-pending | binding_energy | — | 906.8070 | — | 101438.5448 MeV (-262.1 ppm) |
| ${}^{110}$Te | 110 | 58 | L?-pending | binding_energy | — | 919.3928 | — | 102365.5243 MeV (-259.8 ppm) |
| ${}^{111}$Te | 111 | 59 | L?-pending | binding_energy | — | 928.8217 | — | 103295.6605 MeV (-257.4 ppm) |
| ${}^{112}$Te | 112 | 60 | L?-pending | binding_energy | — | 940.8731 | — | 104223.1743 MeV (-255.1 ppm) |
| ${}^{113}$Te | 113 | 61 | L?-pending | binding_energy | — | 949.7239 | — | 105153.8887 MeV (-252.9 ppm) |
| ${}^{114}$Te | 114 | 62 | L?-pending | binding_energy | — | 961.3379 | — | 106081.8399 MeV (-250.7 ppm) |
| ${}^{115}$Te | 115 | 63 | L?-pending | binding_energy | — | 969.5823 | — | 107013.1607 MeV (-248.5 ppm) |
| ${}^{116}$Te | 116 | 64 | L?-pending | binding_energy | — | 980.8546 | — | 107941.4535 MeV (-246.4 ppm) |
| ${}^{117}$Te | 117 | 65 | L?-pending | binding_energy | — | 988.7577 | — | 108873.1157 MeV (-244.3 ppm) |
| ${}^{118}$Te | 118 | 66 | L?-pending | binding_energy | — | 999.4242 | — | 109802.0143 MeV (-242.2 ppm) |
| ${}^{119}$Te | 119 | 67 | L?-pending | binding_energy | — | 1006.9873 | — | 110734.0164 MeV (-240.2 ppm) |
| ${}^{120}$Te | 120 | 68 | L?-pending | binding_energy | — | 1017.2383 | — | 111663.3306 MeV (-238.2 ppm) |
| ${}^{121}$Te | 121 | 69 | L?-pending | binding_energy | — | 1024.4906 | — | 112595.6435 MeV (-236.2 ppm) |
| ${}^{122}$Te | 122 | 70 | L?-pending | binding_energy | — | 1034.3320 | — | 113525.3672 MeV (-234.3 ppm) |
| ${}^{123}$Te | 123 | 71 | L?-pending | binding_energy | — | 1041.2611 | — | 114458.0034 MeV (-232.3 ppm) |
| ${}^{124}$Te | 124 | 72 | L?-pending | binding_energy | — | 1050.6855 | — | 115388.1441 MeV (-230.5 ppm) |
| ${}^{125}$Te | 125 | 73 | L?-pending | binding_energy | — | 1057.2545 | — | 116321.1403 MeV (-228.6 ppm) |
| ${}^{126}$Te | 126 | 74 | L?-pending | binding_energy | — | 1066.3682 | — | 117251.5918 MeV (-226.8 ppm) |
| ${}^{127}$Te | 127 | 75 | L?-pending | binding_energy | — | 1072.6558 | — | 118184.8693 MeV (-225.0 ppm) |
| ${}^{128}$Te | 128 | 76 | L?-pending | binding_energy | — | 1081.4405 | — | 119115.6499 MeV (-223.3 ppm) |
| ${}^{129}$Te | 129 | 77 | L?-pending | binding_energy | — | 1087.5229 | — | 120049.1327 MeV (-221.5 ppm) |
| ${}^{130}$Te | 130 | 78 | L?-pending | binding_energy | — | 1095.9423 | — | 120980.2785 MeV (-219.8 ppm) |
| ${}^{131}$Te | 131 | 79 | L?-pending | binding_energy | — | 1101.8716 | — | 121913.9143 MeV (-218.2 ppm) |
| ${}^{132}$Te | 132 | 80 | L?-pending | binding_energy | — | 1109.9201 | — | 122845.4310 MeV (-216.5 ppm) |
| ${}^{133}$Te | 133 | 81 | L?-pending | binding_energy | — | 1115.7404 | — | 123779.1759 MeV (-214.9 ppm) |
| ${}^{134}$Te | 134 | 82 | L?-pending | binding_energy | — | 1123.4083 | — | 124711.0732 MeV (-213.3 ppm) |
| ${}^{135}$Te | 135 | 83 | L?-pending | binding_energy | — | 1126.6747 | — | 125647.3720 MeV (-211.7 ppm) |
| ${}^{136}$Te | 136 | 84 | L?-pending | binding_energy | — | 1131.4425 | — | 126582.1694 MeV (-210.1 ppm) |
| ${}^{137}$Te | 137 | 85 | L?-pending | binding_energy | — | 1134.3923 | — | 127518.7847 MeV (-208.6 ppm) |
| ${}^{138}$Te | 138 | 86 | L?-pending | binding_energy | — | 1138.8558 | — | 128453.8864 MeV (-207.1 ppm) |
| ${}^{139}$Te | 139 | 87 | L?-pending | binding_energy | — | 1141.4363 | — | 129390.8712 MeV (-205.6 ppm) |
| ${}^{140}$Te | 140 | 88 | L?-pending | binding_energy | — | 1145.6699 | — | 130326.2026 MeV (-204.1 ppm) |
| ${}^{141}$Te | 141 | 89 | L?-pending | binding_energy | — | 1148.0220 | — | 131263.4158 MeV (-202.5 ppm) |
| ${}^{142}$Te | 142 | 90 | L?-pending | binding_energy | — | 1152.0460 | — | 132198.9570 MeV (-201.6 ppm) |
| ${}^{143}$Te | 143 | 91 | L?-pending | binding_energy | — | 1154.0100 | — | 133136.5581 MeV (-199.5 ppm) |
| ${}^{144}$Te | 144 | 92 | L?-pending | binding_energy | — | 1157.7600 | — | 134072.3733 MeV (-198.0 ppm) |
| ${}^{145}$Te | 145 | 93 | L?-pending | binding_energy | — | 1159.7100 | — | 135009.9885 MeV (-197.3 ppm) |

### Iodine (Z = 53)

_0 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{106}$I | 106 | 53 | L?-pending | binding_energy | — | 857.4340 | — | 98667.9290 MeV (-275.1 ppm) |
| ${}^{107}$I | 107 | 54 | L?-pending | binding_energy | — | 871.6220 | — | 99593.3062 MeV (-272.4 ppm) |
| ${}^{108}$I | 108 | 55 | L?-pending | binding_energy | — | 883.0080 | — | 100521.4853 MeV (-269.6 ppm) |
| ${}^{109}$I | 109 | 56 | L?-pending | binding_energy | — | 895.9818 | — | 101448.0767 MeV (-267.1 ppm) |
| ${}^{110}$I | 110 | 57 | L?-pending | binding_energy | — | 906.8484 | — | 102376.7753 MeV (-264.7 ppm) |
| ${}^{111}$I | 111 | 58 | L?-pending | binding_energy | — | 919.4057 | — | 103303.7832 MeV (-262.3 ppm) |
| ${}^{112}$I | 112 | 59 | L?-pending | binding_energy | — | 929.5866 | — | 104233.1675 MeV (-260.0 ppm) |
| ${}^{113}$I | 113 | 60 | L?-pending | binding_energy | — | 941.7141 | — | 105160.6052 MeV (-257.7 ppm) |
| ${}^{114}$I | 114 | 61 | L?-pending | binding_energy | — | 951.3048 | — | 106090.5796 MeV (-255.5 ppm) |
| ${}^{115}$I | 115 | 62 | L?-pending | binding_energy | — | 963.0750 | — | 107018.3747 MeV (-253.3 ppm) |
| ${}^{116}$I | 116 | 63 | L?-pending | binding_energy | — | 972.2292 | — | 107948.7857 MeV (-251.1 ppm) |
| ${}^{117}$I | 117 | 64 | L?-pending | binding_energy | — | 983.3184 | — | 108877.2616 MeV (-248.9 ppm) |
| ${}^{118}$I | 118 | 65 | L?-pending | binding_energy | — | 991.9222 | — | 109808.2230 MeV (-246.8 ppm) |
| ${}^{119}$I | 119 | 66 | L?-pending | binding_energy | — | 1002.8002 | — | 110736.9102 MeV (-244.8 ppm) |
| ${}^{120}$I | 120 | 67 | L?-pending | binding_energy | — | 1010.8409 | — | 111668.4346 MeV (-242.7 ppm) |
| ${}^{121}$I | 121 | 68 | L?-pending | binding_energy | — | 1021.4107 | — | 112597.4300 MeV (-240.7 ppm) |
| ${}^{122}$I | 122 | 69 | L?-pending | binding_energy | — | 1029.3157 | — | 113529.0902 MeV (-238.7 ppm) |
| ${}^{123}$I | 123 | 70 | L?-pending | binding_energy | — | 1039.2503 | — | 114458.7208 MeV (-236.8 ppm) |
| ${}^{124}$I | 124 | 71 | L?-pending | binding_energy | — | 1046.7436 | — | 115390.7927 MeV (-234.9 ppm) |
| ${}^{125}$I | 125 | 72 | L?-pending | binding_energy | — | 1056.2864 | — | 116320.8151 MeV (-233.0 ppm) |
| ${}^{126}$I | 126 | 73 | L?-pending | binding_energy | — | 1063.4322 | — | 117253.2345 MeV (-231.2 ppm) |
| ${}^{127}$I | 127 | 74 | L?-pending | binding_energy | — | 1072.5762 | — | 118183.6556 MeV (-229.4 ppm) |
| ${}^{128}$I | 128 | 75 | L?-pending | binding_energy | — | 1079.4024 | — | 119116.3947 MeV (-227.6 ppm) |
| ${}^{129}$I | 129 | 76 | L?-pending | binding_energy | — | 1088.2428 | — | 120047.1194 MeV (-225.8 ppm) |
| ${}^{130}$I | 130 | 77 | L?-pending | binding_energy | — | 1094.7431 | — | 120980.1843 MeV (-224.1 ppm) |
| ${}^{131}$I | 131 | 78 | L?-pending | binding_energy | — | 1103.3210 | — | 121911.1716 MeV (-222.4 ppm) |
| ${}^{132}$I | 132 | 79 | L?-pending | binding_energy | — | 1109.6531 | — | 122844.4047 MeV (-220.7 ppm) |
| ${}^{133}$I | 133 | 80 | L?-pending | binding_energy | — | 1117.8782 | — | 123775.7448 MeV (-219.0 ppm) |
| ${}^{134}$I | 134 | 81 | L?-pending | binding_energy | — | 1124.1357 | — | 124709.0525 MeV (-217.4 ppm) |
| ${}^{135}$I | 135 | 82 | L?-pending | binding_energy | — | 1131.9427 | — | 125640.8106 MeV (-215.8 ppm) |
| ${}^{136}$I | 136 | 83 | L?-pending | binding_energy | — | 1135.7801 | — | 126576.5384 MeV (-214.2 ppm) |
| ${}^{137}$I | 137 | 84 | L?-pending | binding_energy | — | 1140.6625 | — | 127511.2212 MeV (-212.6 ppm) |
| ${}^{138}$I | 138 | 85 | L?-pending | binding_energy | — | 1144.3574 | — | 128447.0915 MeV (-211.1 ppm) |
| ${}^{139}$I | 139 | 86 | L?-pending | binding_energy | — | 1148.9198 | — | 129382.0943 MeV (-209.5 ppm) |
| ${}^{140}$I | 140 | 87 | L?-pending | binding_energy | — | 1152.1264 | — | 130318.4529 MeV (-208.0 ppm) |
| ${}^{141}$I | 141 | 88 | L?-pending | binding_energy | — | 1156.5181 | — | 131253.6263 MeV (-206.5 ppm) |
| ${}^{142}$I | 142 | 89 | L?-pending | binding_energy | — | 1159.4657 | — | 132190.2439 MeV (-205.1 ppm) |
| ${}^{143}$I | 143 | 90 | L?-pending | binding_energy | — | 1163.5910 | — | 133125.6838 MeV (-204.1 ppm) |
| ${}^{144}$I | 144 | 91 | L?-pending | binding_energy | — | 1166.1120 | — | 134062.7280 MeV (-202.0 ppm) |
| ${}^{145}$I | 145 | 92 | L?-pending | binding_energy | — | 1170.0050 | — | 134998.4002 MeV (-200.8 ppm) |
| ${}^{146}$I | 146 | 93 | L?-pending | binding_energy | — | 1172.5260 | — | 135935.4444 MeV (-199.7 ppm) |
| ${}^{147}$I | 147 | 94 | L?-pending | binding_energy | — | 1176.1470 | — | 136871.3885 MeV (-197.5 ppm) |

### Xenon (Z = 54)

_0 of 43 isotopes with a framework prediction; 43 of 43 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{108}$Xe | 108 | 54 | L?-pending | binding_energy | — | 872.0880 | — | 100531.1120 MeV (-274.7 ppm) |
| ${}^{109}$Xe | 109 | 55 | L?-pending | binding_energy | — | 883.6965 | — | 101459.0687 MeV (-272.1 ppm) |
| ${}^{110}$Xe | 110 | 56 | L?-pending | binding_energy | — | 897.5209 | — | 102384.8095 MeV (-269.7 ppm) |
| ${}^{111}$Xe | 111 | 57 | L?-pending | binding_energy | — | 908.2020 | — | 103313.6936 MeV (-267.4 ppm) |
| ${}^{112}$Xe | 112 | 58 | L?-pending | binding_energy | — | 921.7672 | — | 104239.6935 MeV (-264.9 ppm) |
| ${}^{113}$Xe | 113 | 59 | L?-pending | binding_energy | — | 932.0158 | — | 105169.0101 MeV (-262.6 ppm) |
| ${}^{114}$Xe | 114 | 60 | L?-pending | binding_energy | — | 944.9694 | — | 106095.6217 MeV (-260.3 ppm) |
| ${}^{115}$Xe | 115 | 61 | L?-pending | binding_energy | — | 954.6116 | — | 107025.5447 MeV (-258.0 ppm) |
| ${}^{116}$Xe | 116 | 62 | L?-pending | binding_energy | — | 967.0730 | — | 107952.6485 MeV (-255.8 ppm) |
| ${}^{117}$Xe | 117 | 63 | L?-pending | binding_energy | — | 976.2828 | — | 108883.0039 MeV (-253.6 ppm) |
| ${}^{118}$Xe | 118 | 64 | L?-pending | binding_energy | — | 988.2479 | — | 109810.6040 MeV (-251.5 ppm) |
| ${}^{119}$Xe | 119 | 65 | L?-pending | binding_energy | — | 997.0346 | — | 110741.3824 MeV (-249.4 ppm) |
| ${}^{120}$Xe | 120 | 66 | L?-pending | binding_energy | — | 1008.4839 | — | 111669.4984 MeV (-247.3 ppm) |
| ${}^{121}$Xe | 121 | 67 | L?-pending | binding_energy | — | 1016.8637 | — | 112600.6837 MeV (-245.2 ppm) |
| ${}^{122}$Xe | 122 | 68 | L?-pending | binding_energy | — | 1027.8091 | — | 113529.3035 MeV (-243.2 ppm) |
| ${}^{123}$Xe | 123 | 69 | L?-pending | binding_energy | — | 1035.7736 | — | 114460.9041 MeV (-241.3 ppm) |
| ${}^{124}$Xe | 124 | 70 | L?-pending | binding_energy | — | 1046.2641 | — | 115389.9789 MeV (-239.3 ppm) |
| ${}^{125}$Xe | 125 | 71 | L?-pending | binding_energy | — | 1053.8674 | — | 116321.9408 MeV (-237.4 ppm) |
| ${}^{126}$Xe | 126 | 72 | L?-pending | binding_energy | — | 1063.8857 | — | 117251.4876 MeV (-235.5 ppm) |
| ${}^{127}$Xe | 127 | 73 | L?-pending | binding_energy | — | 1071.1315 | — | 118183.8070 MeV (-233.7 ppm) |
| ${}^{128}$Xe | 128 | 74 | L?-pending | binding_energy | — | 1080.7425 | — | 119113.7612 MeV (-231.9 ppm) |
| ${}^{129}$Xe | 129 | 75 | L?-pending | binding_energy | — | 1087.6494 | — | 120046.4195 MeV (-230.1 ppm) |
| ${}^{130}$Xe | 130 | 76 | L?-pending | binding_energy | — | 1096.9051 | — | 120976.7290 MeV (-228.3 ppm) |
| ${}^{131}$Xe | 131 | 77 | L?-pending | binding_energy | — | 1103.5095 | — | 121909.6898 MeV (-226.5 ppm) |
| ${}^{132}$Xe | 132 | 78 | L?-pending | binding_energy | — | 1112.4462 | — | 122840.3182 MeV (-224.8 ppm) |
| ${}^{133}$Xe | 133 | 79 | L?-pending | binding_energy | — | 1118.8821 | — | 123773.4475 MeV (-223.1 ppm) |
| ${}^{134}$Xe | 134 | 80 | L?-pending | binding_energy | — | 1127.4357 | — | 124704.4591 MeV (-221.5 ppm) |
| ${}^{135}$Xe | 135 | 81 | L?-pending | binding_energy | — | 1133.7946 | — | 125637.6654 MeV (-219.8 ppm) |
| ${}^{136}$Xe | 136 | 82 | L?-pending | binding_energy | — | 1141.8817 | — | 126569.1435 MeV (-218.2 ppm) |
| ${}^{137}$Xe | 137 | 83 | L?-pending | binding_energy | — | 1145.9073 | — | 127504.6831 MeV (-216.6 ppm) |
| ${}^{138}$Xe | 138 | 84 | L?-pending | binding_energy | — | 1151.5674 | — | 128438.5882 MeV (-215.0 ppm) |
| ${}^{139}$Xe | 139 | 85 | L?-pending | binding_energy | — | 1155.3111 | — | 129374.4097 MeV (-213.5 ppm) |
| ${}^{140}$Xe | 140 | 86 | L?-pending | binding_energy | — | 1160.7242 | — | 130308.5617 MeV (-212.0 ppm) |
| ${}^{141}$Xe | 141 | 87 | L?-pending | binding_energy | — | 1164.0064 | — | 131244.8447 MeV (-210.5 ppm) |
| ${}^{142}$Xe | 142 | 88 | L?-pending | binding_energy | — | 1169.1101 | — | 132179.3062 MeV (-209.0 ppm) |
| ${}^{143}$Xe | 143 | 89 | L?-pending | binding_energy | — | 1172.1546 | — | 133115.8269 MeV (-207.5 ppm) |
| ${}^{144}$Xe | 144 | 90 | L?-pending | binding_energy | — | 1176.8954 | — | 134050.6513 MeV (-206.1 ppm) |
| ${}^{145}$Xe | 145 | 91 | L?-pending | binding_energy | — | 1179.5877 | — | 134987.5241 MeV (-204.6 ppm) |
| ${}^{146}$Xe | 146 | 92 | L?-pending | binding_energy | — | 1184.1206 | — | 135922.5564 MeV (-203.2 ppm) |
| ${}^{147}$Xe | 147 | 93 | L?-pending | binding_energy | — | 1186.5840 | — | 136859.6582 MeV (-201.4 ppm) |
| ${}^{148}$Xe | 148 | 94 | L?-pending | binding_energy | — | 1190.9560 | — | 137794.8514 MeV (-200.4 ppm) |
| ${}^{149}$Xe | 149 | 95 | L?-pending | binding_energy | — | 1193.3410 | — | 138732.0316 MeV (-198.8 ppm) |
| ${}^{150}$Xe | 150 | 96 | L?-pending | binding_energy | — | 1197.4500 | — | 139667.4878 MeV (-197.8 ppm) |

### Caesium (Z = 55)

_0 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{111}$Cs | 111 | 56 | L?-pending | binding_energy | — | 895.7700 | — | 103324.8322 MeV (-272.0 ppm) |
| ${}^{112}$Cs | 112 | 57 | L?-pending | binding_energy | — | 907.4240 | — | 104252.7434 MeV (-270.2 ppm) |
| ${}^{113}$Cs | 113 | 58 | L?-pending | binding_energy | — | 920.7944 | — | 105178.9382 MeV (-267.4 ppm) |
| ${}^{114}$Cs | 114 | 59 | L?-pending | binding_energy | — | 931.7871 | — | 106107.5107 MeV (-265.0 ppm) |
| ${}^{115}$Cs | 115 | 60 | L?-pending | binding_energy | — | 944.8400 | — | 107034.0230 MeV (-262.5 ppm) |
| ${}^{116}$Cs | 116 | 61 | L?-pending | binding_energy | — | 955.2600 | — | 107963.1682 MeV (-260.3 ppm) |
| ${}^{117}$Cs | 117 | 62 | L?-pending | binding_energy | — | 967.8082 | — | 108890.1851 MeV (-258.3 ppm) |
| ${}^{118}$Cs | 118 | 63 | L?-pending | binding_energy | — | 977.7958 | — | 109819.7627 MeV (-256.1 ppm) |
| ${}^{119}$Cs | 119 | 64 | L?-pending | binding_energy | — | 989.7628 | — | 110747.3609 MeV (-254.0 ppm) |
| ${}^{120}$Cs | 120 | 65 | L?-pending | binding_energy | — | 999.4177 | — | 111677.2712 MeV (-251.8 ppm) |
| ${}^{121}$Cs | 121 | 66 | L?-pending | binding_energy | — | 1010.7027 | — | 112605.5513 MeV (-249.8 ppm) |
| ${}^{122}$Cs | 122 | 67 | L?-pending | binding_energy | — | 1019.8165 | — | 113536.0028 MeV (-247.7 ppm) |
| ${}^{123}$Cs | 123 | 68 | L?-pending | binding_energy | — | 1030.7867 | — | 114464.5978 MeV (-245.7 ppm) |
| ${}^{124}$Cs | 124 | 69 | L?-pending | binding_energy | — | 1039.5554 | — | 115395.3942 MeV (-243.7 ppm) |
| ${}^{125}$Cs | 125 | 70 | L?-pending | binding_energy | — | 1049.9754 | — | 116324.5394 MeV (-241.8 ppm) |
| ${}^{126}$Cs | 126 | 71 | L?-pending | binding_energy | — | 1058.3077 | — | 117255.7723 MeV (-239.9 ppm) |
| ${}^{127}$Cs | 127 | 72 | L?-pending | binding_energy | — | 1068.2683 | — | 118185.3769 MeV (-238.0 ppm) |
| ${}^{128}$Cs | 128 | 73 | L?-pending | binding_energy | — | 1076.0314 | — | 119117.1790 MeV (-236.1 ppm) |
| ${}^{129}$Cs | 129 | 74 | L?-pending | binding_energy | — | 1085.6700 | — | 120047.1056 MeV (-234.3 ppm) |
| ${}^{130}$Cs | 130 | 75 | L?-pending | binding_energy | — | 1093.1420 | — | 120979.1987 MeV (-232.5 ppm) |
| ${}^{131}$Cs | 131 | 76 | L?-pending | binding_energy | — | 1102.3692 | — | 121909.5368 MeV (-230.7 ppm) |
| ${}^{132}$Cs | 132 | 77 | L?-pending | binding_energy | — | 1109.5376 | — | 122841.9335 MeV (-229.0 ppm) |
| ${}^{133}$Cs | 133 | 78 | L?-pending | binding_energy | — | 1118.5272 | — | 123772.5091 MeV (-227.3 ppm) |
| ${}^{134}$Cs | 134 | 79 | L?-pending | binding_energy | — | 1125.4187 | — | 124705.1828 MeV (-225.6 ppm) |
| ${}^{135}$Cs | 135 | 80 | L?-pending | binding_energy | — | 1134.1808 | — | 125635.9859 MeV (-223.9 ppm) |
| ${}^{136}$Cs | 136 | 81 | L?-pending | binding_energy | — | 1141.0090 | — | 126568.7228 MeV (-222.3 ppm) |
| ${}^{137}$Cs | 137 | 82 | L?-pending | binding_energy | — | 1149.2873 | — | 127500.0098 MeV (-220.6 ppm) |
| ${}^{138}$Cs | 138 | 83 | L?-pending | binding_energy | — | 1153.6998 | — | 128435.1624 MeV (-219.0 ppm) |
| ${}^{139}$Cs | 139 | 84 | L?-pending | binding_energy | — | 1159.5852 | — | 129368.8422 MeV (-217.4 ppm) |
| ${}^{140}$Cs | 140 | 85 | L?-pending | binding_energy | — | 1164.0052 | — | 130303.9874 MeV (-215.9 ppm) |
| ${}^{141}$Cs | 141 | 86 | L?-pending | binding_energy | — | 1169.5041 | — | 131238.0537 MeV (-214.4 ppm) |
| ${}^{142}$Cs | 142 | 87 | L?-pending | binding_energy | — | 1173.6126 | — | 132173.5103 MeV (-212.8 ppm) |
| ${}^{143}$Cs | 143 | 88 | L?-pending | binding_energy | — | 1178.8449 | — | 133107.8432 MeV (-211.3 ppm) |
| ${}^{144}$Cs | 144 | 89 | L?-pending | binding_energy | — | 1182.5121 | — | 134043.7413 MeV (-209.9 ppm) |
| ${}^{145}$Cs | 145 | 90 | L?-pending | binding_energy | — | 1187.3665 | — | 134978.4521 MeV (-208.4 ppm) |
| ${}^{146}$Cs | 146 | 91 | L?-pending | binding_energy | — | 1190.6937 | — | 135914.6900 MeV (-207.0 ppm) |
| ${}^{147}$Cs | 147 | 92 | L?-pending | binding_energy | — | 1195.3747 | — | 136849.5741 MeV (-205.6 ppm) |
| ${}^{148}$Cs | 148 | 93 | L?-pending | binding_energy | — | 1198.4369 | — | 137786.0771 MeV (-204.2 ppm) |
| ${}^{149}$Cs | 149 | 94 | L?-pending | binding_energy | — | 1202.8770 | — | 138721.2023 MeV (-202.7 ppm) |
| ${}^{150}$Cs | 150 | 95 | L?-pending | binding_energy | — | 1205.8500 | — | 139657.7944 MeV (-201.5 ppm) |
| ${}^{151}$Cs | 151 | 96 | L?-pending | binding_energy | — | 1209.9630 | — | 140593.2466 MeV (-199.7 ppm) |
| ${}^{152}$Cs | 152 | 97 | L?-pending | binding_energy | — | 1212.9600 | — | 141529.8148 MeV (-198.9 ppm) |

### Barium (Z = 56)

_0 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{113}$Ba | 113 | 57 | L?-pending | binding_energy | — | 907.9550 | — | 105190.4843 MeV (-272.2 ppm) |
| ${}^{114}$Ba | 114 | 58 | L?-pending | binding_energy | — | 922.2243 | — | 106115.7802 MeV (-269.8 ppm) |
| ${}^{115}$Ba | 115 | 59 | L?-pending | binding_energy | — | 933.3400 | — | 107044.2296 MeV (-267.8 ppm) |
| ${}^{116}$Ba | 116 | 60 | L?-pending | binding_energy | — | 946.7920 | — | 107970.3428 MeV (-264.8 ppm) |
| ${}^{117}$Ba | 117 | 61 | L?-pending | binding_energy | — | 957.9907 | — | 108898.7093 MeV (-263.0 ppm) |
| ${}^{118}$Ba | 118 | 62 | L?-pending | binding_energy | — | 970.7860 | — | 109825.4792 MeV (-260.6 ppm) |
| ${}^{119}$Ba | 119 | 63 | L?-pending | binding_energy | — | 981.2655 | — | 110754.5649 MeV (-258.6 ppm) |
| ${}^{120}$Ba | 120 | 64 | L?-pending | binding_energy | — | 993.6354 | — | 111681.7602 MeV (-256.4 ppm) |
| ${}^{121}$Ba | 121 | 65 | L?-pending | binding_energy | — | 1003.5629 | — | 112611.3978 MeV (-254.3 ppm) |
| ${}^{122}$Ba | 122 | 66 | L?-pending | binding_energy | — | 1015.4983 | — | 113539.0276 MeV (-252.2 ppm) |
| ${}^{123}$Ba | 123 | 67 | L?-pending | binding_energy | — | 1024.6157 | — | 114469.4755 MeV (-250.2 ppm) |
| ${}^{124}$Ba | 124 | 68 | L?-pending | binding_energy | — | 1036.1218 | — | 115397.5345 MeV (-248.2 ppm) |
| ${}^{125}$Ba | 125 | 69 | L?-pending | binding_energy | — | 1044.7723 | — | 116328.4492 MeV (-246.2 ppm) |
| ${}^{126}$Ba | 126 | 70 | L?-pending | binding_energy | — | 1055.8446 | — | 117256.9421 MeV (-244.2 ppm) |
| ${}^{127}$Ba | 127 | 71 | L?-pending | binding_energy | — | 1064.0639 | — | 118188.2879 MeV (-242.3 ppm) |
| ${}^{128}$Ba | 128 | 72 | L?-pending | binding_energy | — | 1074.6864 | — | 119117.2306 MeV (-240.4 ppm) |
| ${}^{129}$Ba | 129 | 73 | L?-pending | binding_energy | — | 1082.4495 | — | 120049.0328 MeV (-238.6 ppm) |
| ${}^{130}$Ba | 130 | 74 | L?-pending | binding_energy | — | 1092.7167 | — | 120978.3307 MeV (-236.7 ppm) |
| ${}^{131}$Ba | 131 | 75 | L?-pending | binding_energy | — | 1100.2102 | — | 121910.4024 MeV (-234.9 ppm) |
| ${}^{132}$Ba | 132 | 76 | L?-pending | binding_energy | — | 1110.0375 | — | 122840.1403 MeV (-233.1 ppm) |
| ${}^{133}$Ba | 133 | 77 | L?-pending | binding_energy | — | 1117.2274 | — | 123772.5156 MeV (-231.4 ppm) |
| ${}^{134}$Ba | 134 | 78 | L?-pending | binding_energy | — | 1126.6952 | — | 124702.6130 MeV (-229.7 ppm) |
| ${}^{135}$Ba | 135 | 79 | L?-pending | binding_energy | — | 1133.6672 | — | 125635.2062 MeV (-228.0 ppm) |
| ${}^{136}$Ba | 136 | 80 | L?-pending | binding_energy | — | 1142.7749 | — | 126565.6636 MeV (-226.3 ppm) |
| ${}^{137}$Ba | 137 | 81 | L?-pending | binding_energy | — | 1149.6805 | — | 127498.3232 MeV (-224.6 ppm) |
| ${}^{138}$Ba | 138 | 82 | L?-pending | binding_energy | — | 1158.2923 | — | 128429.2766 MeV (-223.0 ppm) |
| ${}^{139}$Ba | 139 | 83 | L?-pending | binding_energy | — | 1163.0157 | — | 129364.1184 MeV (-221.4 ppm) |
| ${}^{140}$Ba | 140 | 84 | L?-pending | binding_energy | — | 1169.4410 | — | 130297.2583 MeV (-219.8 ppm) |
| ${}^{141}$Ba | 141 | 85 | L?-pending | binding_energy | — | 1173.9769 | — | 131232.2875 MeV (-218.3 ppm) |
| ${}^{142}$Ba | 142 | 86 | L?-pending | binding_energy | — | 1180.1580 | — | 132165.6716 MeV (-216.7 ppm) |
| ${}^{143}$Ba | 143 | 87 | L?-pending | binding_energy | — | 1184.3243 | — | 133101.0706 MeV (-215.2 ppm) |
| ${}^{144}$Ba | 144 | 88 | L?-pending | binding_energy | — | 1190.2255 | — | 134034.7345 MeV (-213.7 ppm) |
| ${}^{145}$Ba | 145 | 89 | L?-pending | binding_energy | — | 1194.0459 | — | 134970.4793 MeV (-212.2 ppm) |
| ${}^{146}$Ba | 146 | 90 | L?-pending | binding_energy | — | 1199.4673 | — | 135904.6231 MeV (-210.8 ppm) |
| ${}^{147}$Ba | 147 | 91 | L?-pending | binding_energy | — | 1202.9364 | — | 136840.7192 MeV (-209.3 ppm) |
| ${}^{148}$Ba | 148 | 92 | L?-pending | binding_energy | — | 1208.2885 | — | 137774.9322 MeV (-207.9 ppm) |
| ${}^{149}$Ba | 149 | 93 | L?-pending | binding_energy | — | 1211.6456 | — | 138711.1403 MeV (-206.5 ppm) |
| ${}^{150}$Ba | 150 | 94 | L?-pending | binding_energy | — | 1216.7761 | — | 139645.5750 MeV (-205.1 ppm) |
| ${}^{151}$Ba | 151 | 95 | L?-pending | binding_energy | — | 1219.9290 | — | 140581.9873 MeV (-204.0 ppm) |
| ${}^{152}$Ba | 152 | 96 | L?-pending | binding_energy | — | 1224.6640 | — | 141516.8175 MeV (-202.6 ppm) |
| ${}^{153}$Ba | 153 | 97 | L?-pending | binding_energy | — | 1227.5190 | — | 142453.5277 MeV (-200.7 ppm) |
| ${}^{154}$Ba | 154 | 98 | L?-pending | binding_energy | — | 1232.1540 | — | 143388.4578 MeV (-200.2 ppm) |

### Lanthanum (Z = 57)

_0 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{116}$La | 116 | 59 | L?-pending | binding_energy | — | 931.7120 | — | 107984.1295 MeV (-269.8 ppm) |
| ${}^{117}$La | 117 | 60 | L?-pending | binding_energy | — | 946.0620 | — | 108909.3447 MeV (-268.0 ppm) |
| ${}^{118}$La | 118 | 61 | L?-pending | binding_energy | — | 957.4520 | — | 109837.5199 MeV (-265.5 ppm) |
| ${}^{119}$La | 119 | 62 | L?-pending | binding_energy | — | 970.9210 | — | 110763.6160 MeV (-263.2 ppm) |
| ${}^{120}$La | 120 | 63 | L?-pending | binding_energy | — | 981.4800 | — | 111692.6222 MeV (-260.5 ppm) |
| ${}^{121}$La | 121 | 64 | L?-pending | binding_energy | — | 994.2570 | — | 112619.4104 MeV (-259.1 ppm) |
| ${}^{122}$La | 122 | 65 | L?-pending | binding_energy | — | 1004.6700 | — | 113548.5626 MeV (-256.9 ppm) |
| ${}^{123}$La | 123 | 66 | L?-pending | binding_energy | — | 1016.8410 | — | 114475.9568 MeV (-254.7 ppm) |
| ${}^{124}$La | 124 | 67 | L?-pending | binding_energy | — | 1026.5083 | — | 115405.8547 MeV (-252.6 ppm) |
| ${}^{125}$La | 125 | 68 | L?-pending | binding_energy | — | 1038.0805 | — | 116333.8477 MeV (-250.6 ppm) |
| ${}^{126}$La | 126 | 69 | L?-pending | binding_energy | — | 1047.3658 | — | 117264.1276 MeV (-248.6 ppm) |
| ${}^{127}$La | 127 | 70 | L?-pending | binding_energy | — | 1058.3597 | — | 118192.6988 MeV (-246.6 ppm) |
| ${}^{128}$La | 128 | 71 | L?-pending | binding_energy | — | 1067.1604 | — | 119123.4633 MeV (-244.7 ppm) |
| ${}^{129}$La | 129 | 72 | L?-pending | binding_energy | — | 1077.9298 | — | 120052.2591 MeV (-242.8 ppm) |
| ${}^{130}$La | 130 | 73 | L?-pending | binding_energy | — | 1086.3049 | — | 120983.4491 MeV (-240.9 ppm) |
| ${}^{131}$La | 131 | 74 | L?-pending | binding_energy | — | 1096.5182 | — | 121912.8011 MeV (-239.1 ppm) |
| ${}^{132}$La | 132 | 75 | L?-pending | binding_energy | — | 1104.5438 | — | 122844.3407 MeV (-237.3 ppm) |
| ${}^{133}$La | 133 | 76 | L?-pending | binding_energy | — | 1114.3859 | — | 123774.0637 MeV (-235.5 ppm) |
| ${}^{134}$La | 134 | 77 | L?-pending | binding_energy | — | 1122.1815 | — | 124705.8333 MeV (-233.8 ppm) |
| ${}^{135}$La | 135 | 78 | L?-pending | binding_energy | — | 1131.6776 | — | 125635.9024 MeV (-232.0 ppm) |
| ${}^{136}$La | 136 | 79 | L?-pending | binding_energy | — | 1139.1430 | — | 126568.0022 MeV (-230.3 ppm) |
| ${}^{137}$La | 137 | 80 | L?-pending | binding_energy | — | 1148.3177 | — | 127498.3927 MeV (-228.6 ppm) |
| ${}^{138}$La | 138 | 81 | L?-pending | binding_energy | — | 1155.7615 | — | 128430.5140 MeV (-227.0 ppm) |
| ${}^{139}$La | 139 | 82 | L?-pending | binding_energy | — | 1164.5418 | — | 129361.2989 MeV (-225.4 ppm) |
| ${}^{140}$La | 140 | 83 | L?-pending | binding_energy | — | 1169.7028 | — | 130295.7031 MeV (-223.7 ppm) |
| ${}^{141}$La | 141 | 84 | L?-pending | binding_energy | — | 1176.3919 | — | 131228.5792 MeV (-222.2 ppm) |
| ${}^{142}$La | 142 | 85 | L?-pending | binding_energy | — | 1181.5573 | — | 132162.9790 MeV (-220.6 ppm) |
| ${}^{143}$La | 143 | 86 | L?-pending | binding_energy | — | 1187.7762 | — | 133096.3253 MeV (-219.0 ppm) |
| ${}^{144}$La | 144 | 87 | L?-pending | binding_energy | — | 1192.5257 | — | 134031.1410 MeV (-217.5 ppm) |
| ${}^{145}$La | 145 | 88 | L?-pending | binding_energy | — | 1198.5827 | — | 134964.6492 MeV (-216.0 ppm) |
| ${}^{146}$La | 146 | 89 | L?-pending | binding_energy | — | 1203.0398 | — | 135899.7572 MeV (-214.5 ppm) |
| ${}^{147}$La | 147 | 90 | L?-pending | binding_energy | — | 1208.5684 | — | 136833.7938 MeV (-213.1 ppm) |
| ${}^{148}$La | 148 | 91 | L?-pending | binding_energy | — | 1212.6700 | — | 137769.2574 MeV (-211.6 ppm) |
| ${}^{149}$La | 149 | 92 | L?-pending | binding_energy | — | 1218.2525 | — | 138703.2401 MeV (-210.2 ppm) |
| ${}^{150}$La | 150 | 93 | L?-pending | binding_energy | — | 1222.4151 | — | 139638.6427 MeV (-208.8 ppm) |
| ${}^{151}$La | 151 | 94 | L?-pending | binding_energy | — | 1227.4856 | — | 140573.1374 MeV (-207.4 ppm) |
| ${}^{152}$La | 152 | 95 | L?-pending | binding_energy | — | 1231.5040 | — | 141508.6841 MeV (-205.8 ppm) |
| ${}^{153}$La | 153 | 96 | L?-pending | binding_energy | — | 1236.3930 | — | 142443.3603 MeV (-204.8 ppm) |
| ${}^{154}$La | 154 | 97 | L?-pending | binding_energy | — | 1239.8540 | — | 143379.4645 MeV (-202.9 ppm) |
| ${}^{155}$La | 155 | 98 | L?-pending | binding_energy | — | 1244.3400 | — | 144314.5437 MeV (-201.7 ppm) |
| ${}^{156}$La | 156 | 99 | L?-pending | binding_energy | — | 1247.5320 | — | 145250.9169 MeV (-200.4 ppm) |
| ${}^{157}$La | 157 | 100 | L?-pending | binding_energy | — | 1251.6040 | — | 146186.4101 MeV (-199.0 ppm) |

### Cerium (Z = 58)

_0 of 41 isotopes with a framework prediction; 41 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{119}$Ce | 119 | 61 | L?-pending | binding_energy | — | 958.9020 | — | 110774.3417 MeV (-267.5 ppm) |
| ${}^{120}$Ce | 120 | 62 | L?-pending | binding_energy | — | 972.9600 | — | 111699.8489 MeV (-265.9 ppm) |
| ${}^{121}$Ce | 121 | 63 | L?-pending | binding_energy | — | 983.9720 | — | 112628.4021 MeV (-263.6 ppm) |
| ${}^{122}$Ce | 122 | 64 | L?-pending | binding_energy | — | 997.2280 | — | 113554.7113 MeV (-261.4 ppm) |
| ${}^{123}$Ce | 123 | 65 | L?-pending | binding_energy | — | 1007.7390 | — | 114483.7655 MeV (-259.6 ppm) |
| ${}^{124}$Ce | 124 | 66 | L?-pending | binding_energy | — | 1020.3960 | — | 115410.6736 MeV (-257.1 ppm) |
| ${}^{125}$Ce | 125 | 67 | L?-pending | binding_energy | — | 1030.2500 | — | 116340.3848 MeV (-255.4 ppm) |
| ${}^{126}$Ce | 126 | 68 | L?-pending | binding_energy | — | 1042.4305 | — | 117267.7695 MeV (-252.9 ppm) |
| ${}^{127}$Ce | 127 | 69 | L?-pending | binding_energy | — | 1051.6606 | — | 118198.1046 MeV (-250.9 ppm) |
| ${}^{128}$Ce | 128 | 70 | L?-pending | binding_energy | — | 1063.2865 | — | 119126.0439 MeV (-249.0 ppm) |
| ${}^{129}$Ce | 129 | 71 | L?-pending | binding_energy | — | 1072.1114 | — | 120056.7842 MeV (-247.1 ppm) |
| ${}^{130}$Ce | 130 | 72 | L?-pending | binding_energy | — | 1083.3181 | — | 120985.1426 MeV (-245.2 ppm) |
| ${}^{131}$Ce | 131 | 73 | L?-pending | binding_energy | — | 1091.6750 | — | 121916.3509 MeV (-243.3 ppm) |
| ${}^{132}$Ce | 132 | 74 | L?-pending | binding_energy | — | 1102.5065 | — | 122845.0846 MeV (-241.5 ppm) |
| ${}^{133}$Ce | 133 | 75 | L?-pending | binding_energy | — | 1110.5274 | — | 123776.6289 MeV (-239.6 ppm) |
| ${}^{134}$Ce | 134 | 76 | L?-pending | binding_energy | — | 1121.0134 | — | 124705.7081 MeV (-237.9 ppm) |
| ${}^{135}$Ce | 135 | 77 | L?-pending | binding_energy | — | 1128.8681 | — | 125637.4185 MeV (-236.1 ppm) |
| ${}^{136}$Ce | 136 | 78 | L?-pending | binding_energy | — | 1138.8317 | — | 126567.0202 MeV (-234.4 ppm) |
| ${}^{137}$Ce | 137 | 79 | L?-pending | binding_energy | — | 1146.3132 | — | 127499.1038 MeV (-232.6 ppm) |
| ${}^{138}$Ce | 138 | 80 | L?-pending | binding_energy | — | 1156.0316 | — | 128428.9506 MeV (-231.0 ppm) |
| ${}^{139}$Ce | 139 | 81 | L?-pending | binding_energy | — | 1163.4948 | — | 129361.0526 MeV (-229.3 ppm) |
| ${}^{140}$Ce | 140 | 82 | L?-pending | binding_energy | — | 1172.6826 | — | 130291.4300 MeV (-227.7 ppm) |
| ${}^{141}$Ce | 141 | 83 | L?-pending | binding_energy | — | 1178.1108 | — | 131225.5670 MeV (-226.1 ppm) |
| ${}^{142}$Ce | 142 | 84 | L?-pending | binding_energy | — | 1185.2839 | — | 132157.9590 MeV (-224.5 ppm) |
| ${}^{143}$Ce | 143 | 85 | L?-pending | binding_energy | — | 1190.4287 | — | 133092.3794 MeV (-222.9 ppm) |
| ${}^{144}$Ce | 144 | 86 | L?-pending | binding_energy | — | 1197.3256 | — | 134025.0477 MeV (-221.3 ppm) |
| ${}^{145}$Ce | 145 | 87 | L?-pending | binding_energy | — | 1202.0320 | — | 134959.9065 MeV (-219.8 ppm) |
| ${}^{146}$Ce | 146 | 88 | L?-pending | binding_energy | — | 1208.6622 | — | 135892.8415 MeV (-218.3 ppm) |
| ${}^{147}$Ce | 147 | 89 | L?-pending | binding_energy | — | 1213.1215 | — | 136827.9474 MeV (-216.8 ppm) |
| ${}^{148}$Ce | 148 | 90 | L?-pending | binding_energy | — | 1219.5774 | — | 137761.0567 MeV (-215.3 ppm) |
| ${}^{149}$Ce | 149 | 91 | L?-pending | binding_energy | — | 1223.9202 | — | 138696.2791 MeV (-213.9 ppm) |
| ${}^{150}$Ce | 150 | 92 | L?-pending | binding_energy | — | 1230.1684 | — | 139629.5960 MeV (-212.5 ppm) |
| ${}^{151}$Ce | 151 | 93 | L?-pending | binding_energy | — | 1234.6180 | — | 140564.7117 MeV (-211.1 ppm) |
| ${}^{152}$Ce | 152 | 94 | L?-pending | binding_energy | — | 1240.4720 | — | 141498.4228 MeV (-209.9 ppm) |
| ${}^{153}$Ce | 153 | 95 | L?-pending | binding_energy | — | 1244.5020 | — | 142433.9580 MeV (-208.7 ppm) |
| ${}^{154}$Ce | 154 | 96 | L?-pending | binding_energy | — | 1249.8640 | — | 143368.1612 MeV (-207.2 ppm) |
| ${}^{155}$Ce | 155 | 97 | L?-pending | binding_energy | — | 1253.4850 | — | 144304.1054 MeV (-205.8 ppm) |
| ${}^{156}$Ce | 156 | 98 | L?-pending | binding_energy | — | 1258.6080 | — | 145238.5476 MeV (-204.5 ppm) |
| ${}^{157}$Ce | 157 | 99 | L?-pending | binding_energy | — | 1261.8090 | — | 146174.9117 MeV (-203.4 ppm) |
| ${}^{158}$Ce | 158 | 100 | L?-pending | binding_energy | — | 1266.3700 | — | 147109.9159 MeV (-201.3 ppm) |
| ${}^{159}$Ce | 159 | 101 | L?-pending | binding_energy | — | 1269.2970 | — | 148046.5541 MeV (-200.4 ppm) |

### Praseodymium (Z = 59)

_0 of 41 isotopes with a framework prediction; 41 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{121}$Pr | 121 | 62 | L?-pending | binding_energy | — | 971.9930 | — | 112639.0878 MeV (-267.6 ppm) |
| ${}^{122}$Pr | 122 | 63 | L?-pending | binding_energy | — | 983.3200 | — | 113567.3259 MeV (-265.6 ppm) |
| ${}^{123}$Pr | 123 | 64 | L?-pending | binding_energy | — | 996.7920 | — | 114493.4191 MeV (-263.1 ppm) |
| ${}^{124}$Pr | 124 | 65 | L?-pending | binding_energy | — | 1007.8720 | — | 115421.9043 MeV (-261.7 ppm) |
| ${}^{125}$Pr | 125 | 66 | L?-pending | binding_energy | — | 1020.8750 | — | 116348.4665 MeV (-259.7 ppm) |
| ${}^{126}$Pr | 126 | 67 | L?-pending | binding_energy | — | 1031.1840 | — | 117277.7227 MeV (-257.5 ppm) |
| ${}^{127}$Pr | 127 | 68 | L?-pending | binding_energy | — | 1043.4320 | — | 118205.0399 MeV (-255.2 ppm) |
| ${}^{128}$Pr | 128 | 69 | L?-pending | binding_energy | — | 1053.3010 | — | 119134.7360 MeV (-253.2 ppm) |
| ${}^{129}$Pr | 129 | 70 | L?-pending | binding_energy | — | 1064.8151 | — | 120062.7871 MeV (-251.3 ppm) |
| ${}^{130}$Pr | 130 | 71 | L?-pending | binding_energy | — | 1074.2883 | — | 120992.8791 MeV (-249.4 ppm) |
| ${}^{131}$Pr | 131 | 72 | L?-pending | binding_energy | — | 1085.4849 | — | 121921.2478 MeV (-247.5 ppm) |
| ${}^{132}$Pr | 132 | 73 | L?-pending | binding_energy | — | 1094.4830 | — | 122851.8148 MeV (-245.6 ppm) |
| ${}^{133}$Pr | 133 | 74 | L?-pending | binding_energy | — | 1105.2644 | — | 123780.5986 MeV (-243.8 ppm) |
| ${}^{134}$Pr | 134 | 75 | L?-pending | binding_energy | — | 1113.9261 | — | 124711.5020 MeV (-241.9 ppm) |
| ${}^{135}$Pr | 135 | 76 | L?-pending | binding_energy | — | 1124.4053 | — | 125640.5880 MeV (-240.2 ppm) |
| ${}^{136}$Pr | 136 | 77 | L?-pending | binding_energy | — | 1132.8812 | — | 126571.6773 MeV (-238.4 ppm) |
| ${}^{137}$Pr | 137 | 78 | L?-pending | binding_energy | — | 1142.8139 | — | 127501.3098 MeV (-236.7 ppm) |
| ${}^{138}$Pr | 138 | 79 | L?-pending | binding_energy | — | 1150.8123 | — | 128432.8766 MeV (-234.9 ppm) |
| ${}^{139}$Pr | 139 | 80 | L?-pending | binding_energy | — | 1160.5834 | — | 129362.6707 MeV (-233.3 ppm) |
| ${}^{140}$Pr | 140 | 81 | L?-pending | binding_energy | — | 1168.5123 | — | 130294.3070 MeV (-231.6 ppm) |
| ${}^{141}$Pr | 141 | 82 | L?-pending | binding_energy | — | 1177.9119 | — | 131224.4725 MeV (-229.9 ppm) |
| ${}^{142}$Pr | 142 | 83 | L?-pending | binding_energy | — | 1183.7551 | — | 132158.1946 MeV (-228.3 ppm) |
| ${}^{143}$Pr | 143 | 84 | L?-pending | binding_energy | — | 1191.1082 | — | 133090.4066 MeV (-226.7 ppm) |
| ${}^{144}$Pr | 144 | 85 | L?-pending | binding_energy | — | 1196.8619 | — | 134024.2181 MeV (-225.1 ppm) |
| ${}^{145}$Pr | 145 | 86 | L?-pending | binding_energy | — | 1203.8086 | — | 134956.8366 MeV (-223.6 ppm) |
| ${}^{146}$Pr | 146 | 87 | L?-pending | binding_energy | — | 1208.9275 | — | 135891.2829 MeV (-222.1 ppm) |
| ${}^{147}$Pr | 147 | 88 | L?-pending | binding_energy | — | 1215.7694 | — | 136824.0062 MeV (-220.5 ppm) |
| ${}^{148}$Pr | 148 | 89 | L?-pending | binding_energy | — | 1220.9321 | — | 137758.4087 MeV (-219.1 ppm) |
| ${}^{149}$Pr | 149 | 90 | L?-pending | binding_energy | — | 1227.5073 | — | 138691.3986 MeV (-217.6 ppm) |
| ${}^{150}$Pr | 150 | 91 | L?-pending | binding_energy | — | 1232.8397 | — | 139625.6314 MeV (-216.1 ppm) |
| ${}^{151}$Pr | 151 | 92 | L?-pending | binding_energy | — | 1239.3902 | — | 140558.6461 MeV (-214.7 ppm) |
| ${}^{152}$Pr | 152 | 93 | L?-pending | binding_energy | — | 1244.4399 | — | 141493.1615 MeV (-213.3 ppm) |
| ${}^{153}$Pr | 153 | 94 | L?-pending | binding_energy | — | 1250.3217 | — | 142426.8450 MeV (-211.9 ppm) |
| ${}^{154}$Pr | 154 | 95 | L?-pending | binding_energy | — | 1254.6841 | — | 143362.0477 MeV (-210.5 ppm) |
| ${}^{155}$Pr | 155 | 96 | L?-pending | binding_energy | — | 1260.3112 | — | 144295.9859 MeV (-209.1 ppm) |
| ${}^{156}$Pr | 156 | 97 | L?-pending | binding_energy | — | 1264.4165 | — | 145231.4458 MeV (-207.8 ppm) |
| ${}^{157}$Pr | 157 | 98 | L?-pending | binding_energy | — | 1269.4733 | — | 146165.9541 MeV (-206.5 ppm) |
| ${}^{158}$Pr | 158 | 99 | L?-pending | binding_energy | — | 1273.3220 | — | 147101.6706 MeV (-205.6 ppm) |
| ${}^{159}$Pr | 159 | 100 | L?-pending | binding_energy | — | 1277.8830 | — | 148036.6748 MeV (-203.4 ppm) |
| ${}^{160}$Pr | 160 | 101 | L?-pending | binding_energy | — | 1281.4400 | — | 148972.6830 MeV (-202.5 ppm) |
| ${}^{161}$Pr | 161 | 102 | L?-pending | binding_energy | — | 1285.7460 | — | 149907.9421 MeV (-200.9 ppm) |

### Neodymium (Z = 60)

_0 of 40 isotopes with a framework prediction; 40 of 40 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{124}$Nd | 124 | 64 | L?-pending | binding_energy | — | 998.6960 | — | 115429.7870 MeV (-265.5 ppm) |
| ${}^{125}$Nd | 125 | 65 | L?-pending | binding_energy | — | 1010.0000 | — | 116358.0482 MeV (-263.3 ppm) |
| ${}^{126}$Nd | 126 | 66 | L?-pending | binding_energy | — | 1023.3720 | — | 117284.2413 MeV (-261.1 ppm) |
| ${}^{127}$Nd | 127 | 67 | L?-pending | binding_energy | — | 1034.0340 | — | 118213.1445 MeV (-259.6 ppm) |
| ${}^{128}$Nd | 128 | 68 | L?-pending | binding_energy | — | 1046.6560 | — | 119140.0877 MeV (-257.0 ppm) |
| ${}^{129}$Nd | 129 | 69 | L?-pending | binding_energy | — | 1056.6390 | — | 120069.6699 MeV (-255.6 ppm) |
| ${}^{130}$Nd | 130 | 70 | L?-pending | binding_energy | — | 1068.9268 | — | 120996.9473 MeV (-253.6 ppm) |
| ${}^{131}$Nd | 131 | 71 | L?-pending | binding_energy | — | 1078.1699 | — | 121927.2694 MeV (-251.6 ppm) |
| ${}^{132}$Nd | 132 | 72 | L?-pending | binding_energy | — | 1089.8990 | — | 122855.1055 MeV (-249.7 ppm) |
| ${}^{133}$Nd | 133 | 73 | L?-pending | binding_energy | — | 1098.8769 | — | 123785.6928 MeV (-247.9 ppm) |
| ${}^{134}$Nd | 134 | 74 | L?-pending | binding_energy | — | 1110.2622 | — | 124713.8726 MeV (-246.0 ppm) |
| ${}^{135}$Nd | 135 | 75 | L?-pending | binding_energy | — | 1118.9007 | — | 125644.7993 MeV (-244.2 ppm) |
| ${}^{136}$Nd | 136 | 76 | L?-pending | binding_energy | — | 1129.9577 | — | 126573.3075 MeV (-242.4 ppm) |
| ${}^{137}$Nd | 137 | 77 | L?-pending | binding_energy | — | 1138.4137 | — | 127504.4167 MeV (-240.7 ppm) |
| ${}^{138}$Nd | 138 | 78 | L?-pending | binding_energy | — | 1148.9183 | — | 128433.4773 MeV (-238.9 ppm) |
| ${}^{139}$Nd | 139 | 79 | L?-pending | binding_energy | — | 1156.9893 | — | 129364.9714 MeV (-237.2 ppm) |
| ${}^{140}$Nd | 140 | 80 | L?-pending | binding_energy | — | 1167.3010 | — | 130294.2250 MeV (-235.5 ppm) |
| ${}^{141}$Nd | 141 | 81 | L?-pending | binding_energy | — | 1175.3065 | — | 131225.7846 MeV (-233.8 ppm) |
| ${}^{142}$Nd | 142 | 82 | L?-pending | binding_energy | — | 1185.1364 | — | 132155.5199 MeV (-232.2 ppm) |
| ${}^{143}$Nd | 143 | 83 | L?-pending | binding_energy | — | 1191.2600 | — | 133088.9615 MeV (-230.6 ppm) |
| ${}^{144}$Nd | 144 | 84 | L?-pending | binding_energy | — | 1199.0770 | — | 134020.7097 MeV (-229.0 ppm) |
| ${}^{145}$Nd | 145 | 85 | L?-pending | binding_energy | — | 1204.8323 | — | 134954.5196 MeV (-227.4 ppm) |
| ${}^{146}$Nd | 146 | 86 | L?-pending | binding_energy | — | 1212.3975 | — | 135886.5195 MeV (-225.8 ppm) |
| ${}^{147}$Nd | 147 | 87 | L?-pending | binding_energy | — | 1217.6897 | — | 136820.7925 MeV (-224.3 ppm) |
| ${}^{148}$Nd | 148 | 88 | L?-pending | binding_energy | — | 1225.0223 | — | 137753.0251 MeV (-222.8 ppm) |
| ${}^{149}$Nd | 149 | 89 | L?-pending | binding_energy | — | 1230.0611 | — | 138687.5515 MeV (-221.3 ppm) |
| ${}^{150}$Nd | 150 | 90 | L?-pending | binding_energy | — | 1237.4368 | — | 139619.7409 MeV (-219.8 ppm) |
| ${}^{151}$Nd | 151 | 91 | L?-pending | binding_energy | — | 1242.7714 | — | 140553.9716 MeV (-218.3 ppm) |
| ${}^{152}$Nd | 152 | 92 | L?-pending | binding_energy | — | 1250.0492 | — | 141486.2590 MeV (-216.9 ppm) |
| ${}^{153}$Nd | 153 | 93 | L?-pending | binding_energy | — | 1255.3012 | — | 142420.5721 MeV (-215.5 ppm) |
| ${}^{154}$Nd | 154 | 94 | L?-pending | binding_energy | — | 1261.6218 | — | 143353.8168 MeV (-214.1 ppm) |
| ${}^{155}$Nd | 155 | 95 | L?-pending | binding_energy | — | 1266.3973 | — | 144288.6064 MeV (-212.7 ppm) |
| ${}^{156}$Nd | 156 | 96 | L?-pending | binding_energy | — | 1272.3869 | — | 145222.1820 MeV (-211.3 ppm) |
| ${}^{157}$Nd | 157 | 97 | L?-pending | binding_energy | — | 1276.7502 | — | 146157.3838 MeV (-210.0 ppm) |
| ${}^{158}$Nd | 158 | 98 | L?-pending | binding_energy | — | 1282.1626 | — | 147091.5367 MeV (-208.6 ppm) |
| ${}^{159}$Nd | 159 | 99 | L?-pending | binding_energy | — | 1286.1228 | — | 148027.1417 MeV (-207.3 ppm) |
| ${}^{160}$Nd | 160 | 100 | L?-pending | binding_energy | — | 1291.1946 | — | 148961.6350 MeV (-206.0 ppm) |
| ${}^{161}$Nd | 161 | 101 | L?-pending | binding_energy | — | 1294.7620 | — | 149897.6328 MeV (-204.7 ppm) |
| ${}^{162}$Nd | 162 | 102 | L?-pending | binding_energy | — | 1299.5640 | — | 150832.3960 MeV (-203.1 ppm) |
| ${}^{163}$Nd | 163 | 103 | L?-pending | binding_energy | — | 1302.6960 | — | 151768.8292 MeV (-201.8 ppm) |

### Promethium (Z = 61)

_0 of 40 isotopes with a framework prediction; 40 of 40 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{126}$Pm | 126 | 65 | L?-pending | binding_energy | — | 1009.0080 | — | 117297.3120 MeV (-265.9 ppm) |
| ${}^{127}$Pm | 127 | 66 | L?-pending | binding_energy | — | 1022.6040 | — | 118223.2812 MeV (-263.5 ppm) |
| ${}^{128}$Pm | 128 | 67 | L?-pending | binding_energy | — | 1033.6000 | — | 119151.8504 MeV (-261.6 ppm) |
| ${}^{129}$Pm | 129 | 68 | L?-pending | binding_energy | — | 1046.7060 | — | 120078.3096 MeV (-260.2 ppm) |
| ${}^{130}$Pm | 130 | 69 | L?-pending | binding_energy | — | 1057.0300 | — | 121007.5508 MeV (-257.9 ppm) |
| ${}^{131}$Pm | 131 | 70 | L?-pending | binding_energy | — | 1069.3530 | — | 121934.7929 MeV (-255.5 ppm) |
| ${}^{132}$Pm | 132 | 71 | L?-pending | binding_energy | — | 1079.3640 | — | 122864.3471 MeV (-254.3 ppm) |
| ${}^{133}$Pm | 133 | 72 | L?-pending | binding_energy | — | 1091.1698 | — | 123792.1065 MeV (-252.0 ppm) |
| ${}^{134}$Pm | 134 | 73 | L?-pending | binding_energy | — | 1100.5974 | — | 124722.2441 MeV (-250.1 ppm) |
| ${}^{135}$Pm | 135 | 74 | L?-pending | binding_energy | — | 1111.9671 | — | 125650.4396 MeV (-248.3 ppm) |
| ${}^{136}$Pm | 136 | 75 | L?-pending | binding_energy | — | 1121.1460 | — | 126580.8258 MeV (-246.4 ppm) |
| ${}^{137}$Pm | 137 | 76 | L?-pending | binding_energy | — | 1132.1203 | — | 127509.4168 MeV (-244.6 ppm) |
| ${}^{138}$Pm | 138 | 77 | L?-pending | binding_energy | — | 1141.0331 | — | 128440.0691 MeV (-242.9 ppm) |
| ${}^{139}$Pm | 139 | 78 | L?-pending | binding_energy | — | 1151.6911 | — | 129368.9763 MeV (-241.1 ppm) |
| ${}^{140}$Pm | 140 | 79 | L?-pending | binding_energy | — | 1160.4734 | — | 130299.7592 MeV (-239.4 ppm) |
| ${}^{141}$Pm | 141 | 80 | L?-pending | binding_energy | — | 1170.8556 | — | 131228.9422 MeV (-237.7 ppm) |
| ${}^{142}$Pm | 142 | 81 | L?-pending | binding_energy | — | 1179.5455 | — | 132159.8174 MeV (-236.0 ppm) |
| ${}^{143}$Pm | 143 | 82 | L?-pending | binding_energy | — | 1189.4360 | — | 133089.4922 MeV (-234.4 ppm) |
| ${}^{144}$Pm | 144 | 83 | L?-pending | binding_energy | — | 1195.9628 | — | 134022.5306 MeV (-232.8 ppm) |
| ${}^{145}$Pm | 145 | 84 | L?-pending | binding_energy | — | 1203.8855 | — | 134954.1731 MeV (-231.2 ppm) |
| ${}^{146}$Pm | 146 | 85 | L?-pending | binding_energy | — | 1210.1436 | — | 135887.4801 MeV (-229.6 ppm) |
| ${}^{147}$Pm | 147 | 86 | L?-pending | binding_energy | — | 1217.8026 | — | 136819.3863 MeV (-228.0 ppm) |
| ${}^{148}$Pm | 148 | 87 | L?-pending | binding_energy | — | 1223.6978 | — | 137753.0563 MeV (-226.5 ppm) |
| ${}^{149}$Pm | 149 | 88 | L?-pending | binding_energy | — | 1230.9676 | — | 138685.3516 MeV (-225.0 ppm) |
| ${}^{150}$Pm | 150 | 89 | L?-pending | binding_energy | — | 1236.5719 | — | 139619.3126 MeV (-223.5 ppm) |
| ${}^{151}$Pm | 151 | 90 | L?-pending | binding_energy | — | 1244.4321 | — | 140551.0175 MeV (-222.0 ppm) |
| ${}^{152}$Pm | 152 | 91 | L?-pending | binding_energy | — | 1250.3717 | — | 141484.6432 MeV (-220.5 ppm) |
| ${}^{153}$Pm | 153 | 92 | L?-pending | binding_energy | — | 1257.8365 | — | 142416.7435 MeV (-219.1 ppm) |
| ${}^{154}$Pm | 154 | 93 | L?-pending | binding_energy | — | 1263.5264 | — | 143350.6188 MeV (-217.6 ppm) |
| ${}^{155}$Pm | 155 | 94 | L?-pending | binding_energy | — | 1270.2711 | — | 144283.4392 MeV (-216.2 ppm) |
| ${}^{156}$Pm | 156 | 95 | L?-pending | binding_energy | — | 1275.5693 | — | 145217.7063 MeV (-214.9 ppm) |
| ${}^{157}$Pm | 157 | 96 | L?-pending | binding_energy | — | 1281.7709 | — | 146151.0698 MeV (-213.5 ppm) |
| ${}^{158}$Pm | 158 | 97 | L?-pending | binding_energy | — | 1286.6512 | — | 147085.7547 MeV (-212.1 ppm) |
| ${}^{159}$Pm | 159 | 98 | L?-pending | binding_energy | — | 1292.1708 | — | 148019.8004 MeV (-210.8 ppm) |
| ${}^{160}$Pm | 160 | 99 | L?-pending | binding_energy | — | 1296.5824 | — | 148954.9539 MeV (-209.5 ppm) |
| ${}^{161}$Pm | 161 | 100 | L?-pending | binding_energy | — | 1301.8456 | — | 149889.2558 MeV (-208.2 ppm) |
| ${}^{162}$Pm | 162 | 101 | L?-pending | binding_energy | — | 1305.8820 | — | 150824.7847 MeV (-207.0 ppm) |
| ${}^{163}$Pm | 163 | 102 | L?-pending | binding_energy | — | 1310.8460 | — | 151759.3858 MeV (-205.5 ppm) |
| ${}^{164}$Pm | 164 | 103 | L?-pending | binding_energy | — | 1314.2960 | — | 152695.5010 MeV (-204.1 ppm) |
| ${}^{165}$Pm | 165 | 104 | L?-pending | binding_energy | — | 1318.6800 | — | 153630.6822 MeV (-202.9 ppm) |

### Samarium (Z = 62)

_0 of 41 isotopes with a framework prediction; 41 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{128}$Sm | 128 | 66 | L?-pending | binding_energy | — | 1023.7440 | — | 119160.4131 MeV (-265.8 ppm) |
| ${}^{129}$Sm | 129 | 67 | L?-pending | binding_energy | — | 1034.9670 | — | 120088.7552 MeV (-263.5 ppm) |
| ${}^{130}$Sm | 130 | 68 | L?-pending | binding_energy | — | 1048.4500 | — | 121014.8374 MeV (-261.8 ppm) |
| ${}^{131}$Sm | 131 | 69 | L?-pending | binding_energy | — | 1059.1350 | — | 121943.7176 MeV (-260.1 ppm) |
| ${}^{132}$Sm | 132 | 70 | L?-pending | binding_energy | — | 1072.1040 | — | 122870.3138 MeV (-258.5 ppm) |
| ${}^{133}$Sm | 133 | 71 | L?-pending | binding_energy | — | 1082.2210 | — | 123799.7620 MeV (-256.2 ppm) |
| ${}^{134}$Sm | 134 | 72 | L?-pending | binding_energy | — | 1094.3780 | — | 124727.1702 MeV (-253.8 ppm) |
| ${}^{135}$Sm | 135 | 73 | L?-pending | binding_energy | — | 1103.9796 | — | 125657.1337 MeV (-252.3 ppm) |
| ${}^{136}$Sm | 136 | 74 | L?-pending | binding_energy | — | 1116.0046 | — | 126584.6739 MeV (-250.5 ppm) |
| ${}^{137}$Sm | 137 | 75 | L?-pending | binding_energy | — | 1125.2567 | — | 127514.9870 MeV (-248.6 ppm) |
| ${}^{138}$Sm | 138 | 76 | L?-pending | binding_energy | — | 1136.8341 | — | 128442.9748 MeV (-246.8 ppm) |
| ${}^{139}$Sm | 139 | 77 | L?-pending | binding_energy | — | 1145.7879 | — | 129373.5862 MeV (-245.1 ppm) |
| ${}^{140}$Sm | 140 | 78 | L?-pending | binding_energy | — | 1156.9350 | — | 130302.0043 MeV (-243.3 ppm) |
| ${}^{141}$Sm | 141 | 79 | L?-pending | binding_energy | — | 1165.4843 | — | 131233.0202 MeV (-241.6 ppm) |
| ${}^{142}$Sm | 142 | 80 | L?-pending | binding_energy | — | 1176.6036 | — | 132161.4661 MeV (-239.9 ppm) |
| ${}^{143}$Sm | 143 | 81 | L?-pending | binding_energy | — | 1185.2101 | — | 133092.4247 MeV (-238.2 ppm) |
| ${}^{144}$Sm | 144 | 82 | L?-pending | binding_energy | — | 1195.7299 | — | 134021.4701 MeV (-236.6 ppm) |
| ${}^{145}$Sm | 145 | 83 | L?-pending | binding_energy | — | 1202.4870 | — | 134954.2782 MeV (-235.0 ppm) |
| ${}^{146}$Sm | 146 | 84 | L?-pending | binding_energy | — | 1210.9033 | — | 135885.4271 MeV (-233.3 ppm) |
| ${}^{147}$Sm | 147 | 85 | L?-pending | binding_energy | — | 1217.2443 | — | 136818.6513 MeV (-231.8 ppm) |
| ${}^{148}$Sm | 148 | 86 | L?-pending | binding_energy | — | 1225.3856 | — | 137750.0751 MeV (-230.2 ppm) |
| ${}^{149}$Sm | 149 | 87 | L?-pending | binding_energy | — | 1231.2568 | — | 138683.7692 MeV (-228.6 ppm) |
| ${}^{150}$Sm | 150 | 88 | L?-pending | binding_energy | — | 1239.2435 | — | 139615.3476 MeV (-227.1 ppm) |
| ${}^{151}$Sm | 151 | 89 | L?-pending | binding_energy | — | 1244.8400 | — | 140549.3163 MeV (-225.6 ppm) |
| ${}^{152}$Sm | 152 | 90 | L?-pending | binding_energy | — | 1253.0978 | — | 141480.6237 MeV (-224.1 ppm) |
| ${}^{153}$Sm | 153 | 91 | L?-pending | binding_energy | — | 1258.9662 | — | 142414.3205 MeV (-222.7 ppm) |
| ${}^{154}$Sm | 154 | 92 | L?-pending | binding_energy | — | 1266.9330 | — | 143345.9188 MeV (-221.2 ppm) |
| ${}^{155}$Sm | 155 | 93 | L?-pending | binding_energy | — | 1272.7400 | — | 144279.6770 MeV (-219.8 ppm) |
| ${}^{156}$Sm | 156 | 94 | L?-pending | binding_energy | — | 1279.9808 | — | 145212.0014 MeV (-218.4 ppm) |
| ${}^{157}$Sm | 157 | 95 | L?-pending | binding_energy | — | 1285.3691 | — | 146146.1783 MeV (-217.0 ppm) |
| ${}^{158}$Sm | 158 | 96 | L?-pending | binding_energy | — | 1292.0146 | — | 147079.0980 MeV (-215.6 ppm) |
| ${}^{159}$Sm | 159 | 97 | L?-pending | binding_energy | — | 1297.0419 | — | 148013.6359 MeV (-214.2 ppm) |
| ${}^{160}$Sm | 160 | 98 | L?-pending | binding_energy | — | 1303.1385 | — | 148947.1044 MeV (-212.9 ppm) |
| ${}^{161}$Sm | 161 | 99 | L?-pending | binding_energy | — | 1307.6487 | — | 149882.1594 MeV (-211.6 ppm) |
| ${}^{162}$Sm | 162 | 100 | L?-pending | binding_energy | — | 1313.4271 | — | 150815.9463 MeV (-210.3 ppm) |
| ${}^{163}$Sm | 163 | 101 | L?-pending | binding_energy | — | 1317.7189 | — | 151751.2196 MeV (-209.0 ppm) |
| ${}^{164}$Sm | 164 | 102 | L?-pending | binding_energy | — | 1323.1160 | — | 152685.3877 MeV (-207.7 ppm) |
| ${}^{165}$Sm | 165 | 103 | L?-pending | binding_energy | — | 1326.7650 | — | 153621.3039 MeV (-206.4 ppm) |
| ${}^{166}$Sm | 166 | 104 | L?-pending | binding_energy | — | 1331.8180 | — | 154555.8161 MeV (-205.4 ppm) |
| ${}^{167}$Sm | 167 | 105 | L?-pending | binding_energy | — | 1334.6640 | — | 155492.5353 MeV (-203.5 ppm) |
| ${}^{168}$Sm | 168 | 106 | L?-pending | binding_energy | — | 1339.1280 | — | 156427.6364 MeV (-202.8 ppm) |

### Europium (Z = 63)

_0 of 41 isotopes with a framework prediction; 41 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{130}$Eu | 130 | 67 | L?-pending | binding_energy | — | 1033.5000 | — | 121028.4941 MeV (-266.2 ppm) |
| ${}^{131}$Eu | 131 | 68 | L?-pending | binding_energy | — | 1047.4760 | — | 121954.0833 MeV (-263.8 ppm) |
| ${}^{132}$Eu | 132 | 69 | L?-pending | binding_energy | — | 1058.3760 | — | 122882.7485 MeV (-262.6 ppm) |
| ${}^{133}$Eu | 133 | 70 | L?-pending | binding_energy | — | 1071.4480 | — | 123809.2416 MeV (-260.3 ppm) |
| ${}^{134}$Eu | 134 | 71 | L?-pending | binding_energy | — | 1082.0500 | — | 124738.2048 MeV (-258.1 ppm) |
| ${}^{135}$Eu | 135 | 72 | L?-pending | binding_energy | — | 1094.4450 | — | 125665.3750 MeV (-256.0 ppm) |
| ${}^{136}$Eu | 136 | 73 | L?-pending | binding_energy | — | 1104.5920 | — | 126594.7932 MeV (-254.0 ppm) |
| ${}^{137}$Eu | 137 | 74 | L?-pending | binding_energy | — | 1116.6286 | — | 127522.3218 MeV (-252.6 ppm) |
| ${}^{138}$Eu | 138 | 75 | L?-pending | binding_energy | — | 1126.3037 | — | 128452.2119 MeV (-250.8 ppm) |
| ${}^{139}$Eu | 139 | 76 | L?-pending | binding_energy | — | 1138.0234 | — | 129380.0574 MeV (-249.0 ppm) |
| ${}^{140}$Eu | 140 | 77 | L?-pending | binding_energy | — | 1147.6826 | — | 130309.9633 MeV (-247.2 ppm) |
| ${}^{141}$Eu | 141 | 78 | L?-pending | binding_energy | — | 1158.6936 | — | 131238.5175 MeV (-245.5 ppm) |
| ${}^{142}$Eu | 142 | 79 | L?-pending | binding_energy | — | 1168.1482 | — | 132168.6281 MeV (-243.8 ppm) |
| ${}^{143}$Eu | 143 | 80 | L?-pending | binding_energy | — | 1179.1519 | — | 133097.1896 MeV (-242.1 ppm) |
| ${}^{144}$Eu | 144 | 81 | L?-pending | binding_energy | — | 1188.6011 | — | 134027.3056 MeV (-240.4 ppm) |
| ${}^{145}$Eu | 145 | 82 | L?-pending | binding_energy | — | 1199.0448 | — | 134956.4271 MeV (-238.7 ppm) |
| ${}^{146}$Eu | 146 | 83 | L?-pending | binding_energy | — | 1206.2422 | — | 135888.7949 MeV (-237.1 ppm) |
| ${}^{147}$Eu | 147 | 84 | L?-pending | binding_energy | — | 1214.7405 | — | 136819.8617 MeV (-235.5 ppm) |
| ${}^{148}$Eu | 148 | 85 | L?-pending | binding_energy | — | 1221.5647 | — | 137752.6027 MeV (-233.9 ppm) |
| ${}^{149}$Eu | 149 | 86 | L?-pending | binding_energy | — | 1229.7798 | — | 138683.9528 MeV (-232.3 ppm) |
| ${}^{150}$Eu | 150 | 87 | L?-pending | binding_energy | — | 1236.2022 | — | 139617.0956 MeV (-230.8 ppm) |
| ${}^{151}$Eu | 151 | 88 | L?-pending | binding_energy | — | 1244.1343 | — | 140548.7287 MeV (-229.2 ppm) |
| ${}^{152}$Eu | 152 | 89 | L?-pending | binding_energy | — | 1250.4410 | — | 141481.9872 MeV (-227.7 ppm) |
| ${}^{153}$Eu | 153 | 90 | L?-pending | binding_energy | — | 1258.9913 | — | 142413.0021 MeV (-226.2 ppm) |
| ${}^{154}$Eu | 154 | 91 | L?-pending | binding_energy | — | 1265.4335 | — | 143346.1250 MeV (-224.8 ppm) |
| ${}^{155}$Eu | 155 | 92 | L?-pending | binding_energy | — | 1273.5848 | — | 144277.5389 MeV (-223.3 ppm) |
| ${}^{156}$Eu | 156 | 93 | L?-pending | binding_energy | — | 1279.9206 | — | 145210.7683 MeV (-221.9 ppm) |
| ${}^{157}$Eu | 157 | 94 | L?-pending | binding_energy | — | 1287.3682 | — | 146142.8859 MeV (-220.5 ppm) |
| ${}^{158}$Eu | 158 | 95 | L?-pending | binding_energy | — | 1293.2509 | — | 147076.5684 MeV (-219.1 ppm) |
| ${}^{159}$Eu | 159 | 96 | L?-pending | binding_energy | — | 1300.0951 | — | 148009.2894 MeV (-217.7 ppm) |
| ${}^{160}$Eu | 160 | 97 | L?-pending | binding_energy | — | 1305.6165 | — | 148943.3331 MeV (-216.3 ppm) |
| ${}^{161}$Eu | 161 | 98 | L?-pending | binding_energy | — | 1311.9859 | — | 149876.5289 MeV (-215.0 ppm) |
| ${}^{162}$Eu | 162 | 99 | L?-pending | binding_energy | — | 1316.9886 | — | 150811.0914 MeV (-213.7 ppm) |
| ${}^{163}$Eu | 163 | 100 | L?-pending | binding_energy | — | 1322.9108 | — | 151744.7344 MeV (-212.4 ppm) |
| ${}^{164}$Eu | 164 | 101 | L?-pending | binding_energy | — | 1327.6405 | — | 152679.5699 MeV (-211.1 ppm) |
| ${}^{165}$Eu | 165 | 102 | L?-pending | binding_energy | — | 1333.2087 | — | 153613.5668 MeV (-209.8 ppm) |
| ${}^{166}$Eu | 166 | 103 | L?-pending | binding_energy | — | 1337.2960 | — | 154549.0447 MeV (-208.5 ppm) |
| ${}^{167}$Eu | 167 | 104 | L?-pending | binding_energy | — | 1342.3460 | — | 155483.5599 MeV (-207.0 ppm) |
| ${}^{168}$Eu | 168 | 105 | L?-pending | binding_energy | — | 1346.0160 | — | 156419.4551 MeV (-206.5 ppm) |
| ${}^{169}$Eu | 169 | 106 | L?-pending | binding_energy | — | 1350.4790 | — | 157354.5573 MeV (-205.1 ppm) |
| ${}^{170}$Eu | 170 | 107 | L?-pending | binding_energy | — | 1353.7100 | — | 158290.8915 MeV (-203.7 ppm) |

### Gadolinium (Z = 64)

_0 of 40 isotopes with a framework prediction; 40 of 40 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{133}$Gd | 133 | 69 | L?-pending | binding_energy | — | 1059.4780 | — | 123819.9183 MeV (-264.3 ppm) |
| ${}^{134}$Gd | 134 | 70 | L?-pending | binding_energy | — | 1073.0720 | — | 124745.8895 MeV (-262.8 ppm) |
| ${}^{135}$Gd | 135 | 71 | L?-pending | binding_energy | — | 1083.7800 | — | 125674.7467 MeV (-260.2 ppm) |
| ${}^{136}$Gd | 136 | 72 | L?-pending | binding_energy | — | 1096.7040 | — | 126601.3879 MeV (-258.4 ppm) |
| ${}^{137}$Gd | 137 | 73 | L?-pending | binding_energy | — | 1106.9600 | — | 127530.6970 MeV (-257.0 ppm) |
| ${}^{138}$Gd | 138 | 74 | L?-pending | binding_energy | — | 1119.4560 | — | 128457.7662 MeV (-255.0 ppm) |
| ${}^{139}$Gd | 139 | 75 | L?-pending | binding_energy | — | 1129.5140 | — | 129387.2734 MeV (-253.2 ppm) |
| ${}^{140}$Gd | 140 | 76 | L?-pending | binding_energy | — | 1141.6966 | — | 130314.6560 MeV (-251.1 ppm) |
| ${}^{141}$Gd | 141 | 77 | L?-pending | binding_energy | — | 1151.2099 | — | 131244.7079 MeV (-249.4 ppm) |
| ${}^{142}$Gd | 142 | 78 | L?-pending | binding_energy | — | 1163.0165 | — | 132172.4665 MeV (-247.6 ppm) |
| ${}^{143}$Gd | 143 | 79 | L?-pending | binding_energy | — | 1172.3596 | — | 133102.6886 MeV (-245.9 ppm) |
| ${}^{144}$Gd | 144 | 80 | L?-pending | binding_energy | — | 1183.9591 | — | 134030.6542 MeV (-244.2 ppm) |
| ${}^{145}$Gd | 145 | 81 | L?-pending | binding_energy | — | 1193.1975 | — | 134960.9810 MeV (-242.5 ppm) |
| ${}^{146}$Gd | 146 | 82 | L?-pending | binding_energy | — | 1204.4281 | — | 135889.3157 MeV (-240.9 ppm) |
| ${}^{147}$Gd | 147 | 83 | L?-pending | binding_energy | — | 1211.7705 | — | 136821.5384 MeV (-239.2 ppm) |
| ${}^{148}$Gd | 148 | 84 | L?-pending | binding_energy | — | 1220.7543 | — | 137752.1198 MeV (-237.6 ppm) |
| ${}^{149}$Gd | 149 | 85 | L?-pending | binding_energy | — | 1227.6834 | — | 138684.7559 MeV (-236.0 ppm) |
| ${}^{150}$Gd | 150 | 86 | L?-pending | binding_energy | — | 1236.3915 | — | 139615.6129 MeV (-234.4 ppm) |
| ${}^{151}$Gd | 151 | 87 | L?-pending | binding_energy | — | 1242.8877 | — | 140548.6819 MeV (-232.9 ppm) |
| ${}^{152}$Gd | 152 | 88 | L?-pending | binding_energy | — | 1251.4774 | — | 141479.6574 MeV (-231.3 ppm) |
| ${}^{153}$Gd | 153 | 89 | L?-pending | binding_energy | — | 1257.7244 | — | 142412.9756 MeV (-229.8 ppm) |
| ${}^{154}$Gd | 154 | 90 | L?-pending | binding_energy | — | 1266.6191 | — | 143343.6461 MeV (-228.3 ppm) |
| ${}^{155}$Gd | 155 | 91 | L?-pending | binding_energy | — | 1273.0544 | — | 144276.7760 MeV (-226.9 ppm) |
| ${}^{156}$Gd | 156 | 92 | L?-pending | binding_energy | — | 1281.5907 | — | 145207.8048 MeV (-225.4 ppm) |
| ${}^{157}$Gd | 157 | 93 | L?-pending | binding_energy | — | 1287.9506 | — | 146141.0101 MeV (-224.0 ppm) |
| ${}^{158}$Gd | 158 | 94 | L?-pending | binding_energy | — | 1295.8880 | — | 147072.6379 MeV (-222.6 ppm) |
| ${}^{159}$Gd | 159 | 95 | L?-pending | binding_energy | — | 1301.8312 | — | 148006.2599 MeV (-221.2 ppm) |
| ${}^{160}$Gd | 160 | 96 | L?-pending | binding_energy | — | 1309.2827 | — | 148938.3736 MeV (-219.8 ppm) |
| ${}^{161}$Gd | 161 | 97 | L?-pending | binding_energy | — | 1314.9181 | — | 149872.3033 MeV (-218.4 ppm) |
| ${}^{162}$Gd | 162 | 98 | L?-pending | binding_energy | — | 1321.7640 | — | 150805.0226 MeV (-217.1 ppm) |
| ${}^{163}$Gd | 163 | 99 | L?-pending | binding_energy | — | 1326.9432 | — | 151739.4086 MeV (-215.7 ppm) |
| ${}^{164}$Gd | 164 | 100 | L?-pending | binding_energy | — | 1333.3196 | — | 152672.5974 MeV (-214.4 ppm) |
| ${}^{165}$Gd | 165 | 101 | L?-pending | binding_energy | — | 1338.2231 | — | 153607.2592 MeV (-213.1 ppm) |
| ${}^{166}$Gd | 166 | 102 | L?-pending | binding_energy | — | 1344.1395 | — | 154540.9079 MeV (-211.8 ppm) |
| ${}^{167}$Gd | 167 | 103 | L?-pending | binding_energy | — | 1348.6156 | — | 155475.9969 MeV (-210.6 ppm) |
| ${}^{168}$Gd | 168 | 104 | L?-pending | binding_energy | — | 1354.0800 | — | 156410.0978 MeV (-209.4 ppm) |
| ${}^{169}$Gd | 169 | 105 | L?-pending | binding_energy | — | 1357.9150 | — | 157345.8280 MeV (-208.3 ppm) |
| ${}^{170}$Gd | 170 | 106 | L?-pending | binding_energy | — | 1362.8900 | — | 158280.4181 MeV (-206.7 ppm) |
| ${}^{171}$Gd | 171 | 107 | L?-pending | binding_energy | — | 1366.2900 | — | 159216.5833 MeV (-205.3 ppm) |
| ${}^{172}$Gd | 172 | 108 | L?-pending | binding_energy | — | 1371.1840 | — | 160151.2545 MeV (-204.5 ppm) |

### Terbium (Z = 65)

_0 of 40 isotopes with a framework prediction; 40 of 40 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{135}$Tb | 135 | 70 | L?-pending | binding_energy | — | 1071.7650 | — | 125685.4683 MeV (-263.9 ppm) |
| ${}^{136}$Tb | 136 | 71 | L?-pending | binding_energy | — | 1082.6960 | — | 126614.1025 MeV (-262.1 ppm) |
| ${}^{137}$Tb | 137 | 72 | L?-pending | binding_energy | — | 1095.8630 | — | 127540.5007 MeV (-260.4 ppm) |
| ${}^{138}$Tb | 138 | 73 | L?-pending | binding_energy | — | 1106.6220 | — | 128469.3069 MeV (-259.0 ppm) |
| ${}^{139}$Tb | 139 | 74 | L?-pending | binding_energy | — | 1119.2280 | — | 129396.2661 MeV (-257.2 ppm) |
| ${}^{140}$Tb | 140 | 75 | L?-pending | binding_energy | — | 1129.6142 | — | 130325.4450 MeV (-255.0 ppm) |
| ${}^{141}$Tb | 141 | 76 | L?-pending | binding_energy | — | 1141.7441 | — | 131252.8803 MeV (-253.2 ppm) |
| ${}^{142}$Tb | 142 | 77 | L?-pending | binding_energy | — | 1151.8341 | — | 132182.3555 MeV (-251.5 ppm) |
| ${}^{143}$Tb | 143 | 78 | L?-pending | binding_energy | — | 1163.7651 | — | 133109.9897 MeV (-249.7 ppm) |
| ${}^{144}$Tb | 144 | 79 | L?-pending | binding_energy | — | 1173.7854 | — | 134039.5346 MeV (-248.0 ppm) |
| ${}^{145}$Tb | 145 | 80 | L?-pending | binding_energy | — | 1185.8883 | — | 134966.9969 MeV (-246.3 ppm) |
| ${}^{146}$Tb | 146 | 81 | L?-pending | binding_energy | — | 1195.3235 | — | 135897.1269 MeV (-244.6 ppm) |
| ${}^{147}$Tb | 147 | 82 | L?-pending | binding_energy | — | 1206.3739 | — | 136825.6417 MeV (-242.9 ppm) |
| ${}^{148}$Tb | 148 | 83 | L?-pending | binding_energy | — | 1214.2395 | — | 137757.3413 MeV (-241.3 ppm) |
| ${}^{149}$Tb | 149 | 84 | L?-pending | binding_energy | — | 1223.2625 | — | 138687.8835 MeV (-239.7 ppm) |
| ${}^{150}$Tb | 150 | 85 | L?-pending | binding_energy | — | 1230.9509 | — | 139619.7602 MeV (-238.1 ppm) |
| ${}^{151}$Tb | 151 | 86 | L?-pending | binding_energy | — | 1239.5400 | — | 140550.7363 MeV (-236.5 ppm) |
| ${}^{152}$Tb | 152 | 87 | L?-pending | binding_energy | — | 1246.7051 | — | 141483.1364 MeV (-235.0 ppm) |
| ${}^{153}$Tb | 153 | 88 | L?-pending | binding_energy | — | 1255.3727 | — | 142414.0340 MeV (-233.4 ppm) |
| ${}^{154}$Tb | 154 | 89 | L?-pending | binding_energy | — | 1262.2871 | — | 143346.6847 MeV (-231.9 ppm) |
| ${}^{155}$Tb | 155 | 90 | L?-pending | binding_energy | — | 1271.4522 | — | 144277.0849 MeV (-230.4 ppm) |
| ${}^{156}$Tb | 156 | 91 | L?-pending | binding_energy | — | 1278.3641 | — | 145209.7382 MeV (-228.9 ppm) |
| ${}^{157}$Tb | 157 | 92 | L?-pending | binding_energy | — | 1287.1082 | — | 146140.5592 MeV (-227.5 ppm) |
| ${}^{158}$Tb | 158 | 93 | L?-pending | binding_energy | — | 1293.8866 | — | 147073.3460 MeV (-226.0 ppm) |
| ${}^{159}$Tb | 159 | 94 | L?-pending | binding_energy | — | 1302.0196 | — | 148004.7782 MeV (-224.6 ppm) |
| ${}^{160}$Tb | 160 | 95 | L?-pending | binding_energy | — | 1308.3948 | — | 148937.9681 MeV (-223.2 ppm) |
| ${}^{161}$Tb | 161 | 96 | L?-pending | binding_energy | — | 1316.0914 | — | 149869.8367 MeV (-221.8 ppm) |
| ${}^{162}$Tb | 162 | 97 | L?-pending | binding_energy | — | 1322.5805 | — | 150802.9128 MeV (-220.5 ppm) |
| ${}^{163}$Tb | 163 | 98 | L?-pending | binding_energy | — | 1329.3680 | — | 151735.6905 MeV (-219.1 ppm) |
| ${}^{164}$Tb | 164 | 99 | L?-pending | binding_energy | — | 1334.9486 | — | 152669.6751 MeV (-217.8 ppm) |
| ${}^{165}$Tb | 165 | 100 | L?-pending | binding_energy | — | 1341.5038 | — | 153602.6851 MeV (-216.4 ppm) |
| ${}^{166}$Tb | 166 | 101 | L?-pending | binding_energy | — | 1346.7950 | — | 154536.9591 MeV (-215.1 ppm) |
| ${}^{167}$Tb | 167 | 102 | L?-pending | binding_energy | — | 1352.9406 | — | 155470.3786 MeV (-213.8 ppm) |
| ${}^{168}$Tb | 168 | 103 | L?-pending | binding_energy | — | 1357.9101 | — | 156404.9744 MeV (-212.6 ppm) |
| ${}^{169}$Tb | 169 | 104 | L?-pending | binding_energy | — | 1363.6610 | — | 157338.7886 MeV (-211.2 ppm) |
| ${}^{170}$Tb | 170 | 105 | L?-pending | binding_energy | — | 1367.9900 | — | 158274.0248 MeV (-210.1 ppm) |
| ${}^{171}$Tb | 171 | 106 | L?-pending | binding_energy | — | 1373.1300 | — | 159208.4500 MeV (-208.9 ppm) |
| ${}^{172}$Tb | 172 | 107 | L?-pending | binding_energy | — | 1377.0320 | — | 160144.1132 MeV (-207.2 ppm) |
| ${}^{173}$Tb | 173 | 108 | L?-pending | binding_energy | — | 1381.9240 | — | 161078.7864 MeV (-206.0 ppm) |
| ${}^{174}$Tb | 174 | 109 | L?-pending | binding_energy | — | 1385.5620 | — | 162014.7136 MeV (-205.4 ppm) |

### Dysprosium (Z = 66)

_0 of 39 isotopes with a framework prediction; 39 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{138}$Dy | 138 | 72 | L?-pending | binding_energy | — | 1097.1000 | — | 128477.5356 MeV (-262.4 ppm) |
| ${}^{139}$Dy | 139 | 73 | L?-pending | binding_energy | — | 1107.9690 | — | 129406.2318 MeV (-260.7 ppm) |
| ${}^{140}$Dy | 140 | 74 | L?-pending | binding_energy | — | 1121.1200 | — | 130332.6459 MeV (-258.5 ppm) |
| ${}^{141}$Dy | 141 | 75 | L?-pending | binding_energy | — | 1131.8070 | — | 131261.5241 MeV (-257.1 ppm) |
| ${}^{142}$Dy | 142 | 76 | L?-pending | binding_energy | — | 1144.6620 | — | 132188.2343 MeV (-255.7 ppm) |
| ${}^{143}$Dy | 143 | 77 | L?-pending | binding_energy | — | 1154.7325 | — | 133117.7290 MeV (-253.5 ppm) |
| ${}^{144}$Dy | 144 | 78 | L?-pending | binding_energy | — | 1167.2050 | — | 134044.8217 MeV (-251.8 ppm) |
| ${}^{145}$Dy | 145 | 79 | L?-pending | binding_energy | — | 1176.9488 | — | 134974.6430 MeV (-250.1 ppm) |
| ${}^{146}$Dy | 146 | 80 | L?-pending | binding_energy | — | 1189.3325 | — | 135901.8246 MeV (-248.3 ppm) |
| ${}^{147}$Dy | 147 | 81 | L?-pending | binding_energy | — | 1199.0449 | — | 136831.6773 MeV (-246.7 ppm) |
| ${}^{148}$Dy | 148 | 82 | L?-pending | binding_energy | — | 1210.7796 | — | 137759.5079 MeV (-245.0 ppm) |
| ${}^{149}$Dy | 149 | 83 | L?-pending | binding_energy | — | 1218.6855 | — | 138691.1671 MeV (-243.4 ppm) |
| ${}^{150}$Dy | 150 | 84 | L?-pending | binding_energy | — | 1228.3724 | — | 139621.0454 MeV (-241.7 ppm) |
| ${}^{151}$Dy | 151 | 85 | L?-pending | binding_energy | — | 1235.8865 | — | 140553.0965 MeV (-240.1 ppm) |
| ${}^{152}$Dy | 152 | 86 | L?-pending | binding_energy | — | 1245.3234 | — | 141483.2248 MeV (-238.6 ppm) |
| ${}^{153}$Dy | 153 | 87 | L?-pending | binding_energy | — | 1252.4200 | — | 142415.6934 MeV (-237.0 ppm) |
| ${}^{154}$Dy | 154 | 88 | L?-pending | binding_energy | — | 1261.7421 | — | 143345.9364 MeV (-235.5 ppm) |
| ${}^{155}$Dy | 155 | 89 | L?-pending | binding_energy | — | 1268.5753 | — | 144278.6684 MeV (-233.9 ppm) |
| ${}^{156}$Dy | 156 | 90 | L?-pending | binding_energy | — | 1278.0201 | — | 145208.7888 MeV (-232.5 ppm) |
| ${}^{157}$Dy | 157 | 91 | L?-pending | binding_energy | — | 1284.9867 | — | 146141.3874 MeV (-231.0 ppm) |
| ${}^{158}$Dy | 158 | 92 | L?-pending | binding_energy | — | 1294.0405 | — | 147071.8988 MeV (-229.5 ppm) |
| ${}^{159}$Dy | 159 | 93 | L?-pending | binding_energy | — | 1300.8719 | — | 148004.6326 MeV (-228.1 ppm) |
| ${}^{160}$Dy | 160 | 94 | L?-pending | binding_energy | — | 1309.4484 | — | 148935.6212 MeV (-226.6 ppm) |
| ${}^{161}$Dy | 161 | 95 | L?-pending | binding_energy | — | 1315.9028 | — | 149868.7320 MeV (-225.2 ppm) |
| ${}^{162}$Dy | 162 | 96 | L?-pending | binding_energy | — | 1324.0998 | — | 150800.1002 MeV (-223.8 ppm) |
| ${}^{163}$Dy | 163 | 97 | L?-pending | binding_energy | — | 1330.3708 | — | 151733.3944 MeV (-222.5 ppm) |
| ${}^{164}$Dy | 164 | 98 | L?-pending | binding_energy | — | 1338.0289 | — | 152665.3015 MeV (-221.1 ppm) |
| ${}^{165}$Dy | 165 | 99 | L?-pending | binding_energy | — | 1343.7449 | — | 153599.1507 MeV (-219.8 ppm) |
| ${}^{166}$Dy | 166 | 100 | L?-pending | binding_energy | — | 1350.7884 | — | 154531.6724 MeV (-218.4 ppm) |
| ${}^{167}$Dy | 167 | 101 | L?-pending | binding_energy | — | 1356.1867 | — | 155465.8393 MeV (-217.1 ppm) |
| ${}^{168}$Dy | 168 | 102 | L?-pending | binding_energy | — | 1362.9049 | — | 156398.6862 MeV (-215.8 ppm) |
| ${}^{169}$Dy | 169 | 103 | L?-pending | binding_energy | — | 1368.0139 | — | 157333.1424 MeV (-214.6 ppm) |
| ${}^{170}$Dy | 170 | 104 | L?-pending | binding_energy | — | 1374.2800 | — | 158266.4415 MeV (-213.8 ppm) |
| ${}^{171}$Dy | 171 | 105 | L?-pending | binding_energy | — | 1378.6020 | — | 159201.6847 MeV (-212.2 ppm) |
| ${}^{172}$Dy | 172 | 106 | L?-pending | binding_energy | — | 1384.4280 | — | 160135.4238 MeV (-211.0 ppm) |
| ${}^{173}$Dy | 173 | 107 | L?-pending | binding_energy | — | 1388.4980 | — | 161070.9190 MeV (-209.9 ppm) |
| ${}^{174}$Dy | 174 | 108 | L?-pending | binding_energy | — | 1393.9140 | — | 162005.0682 MeV (-208.4 ppm) |
| ${}^{175}$Dy | 175 | 109 | L?-pending | binding_energy | — | 1397.5500 | — | 162940.9974 MeV (-207.0 ppm) |
| ${}^{176}$Dy | 176 | 110 | L?-pending | binding_energy | — | 1402.5440 | — | 163875.5686 MeV (-206.1 ppm) |

### Holmium (Z = 67)

_0 of 39 isotopes with a framework prediction; 39 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{140}$Ho | 140 | 73 | L?-pending | binding_energy | — | 1106.8400 | — | 130345.6326 MeV (-262.5 ppm) |
| ${}^{141}$Ho | 141 | 74 | L?-pending | binding_energy | — | 1119.9630 | — | 131272.0748 MeV (-260.7 ppm) |
| ${}^{142}$Ho | 142 | 75 | L?-pending | binding_energy | — | 1131.0300 | — | 132200.5730 MeV (-259.7 ppm) |
| ${}^{143}$Ho | 143 | 76 | L?-pending | binding_energy | — | 1143.8570 | — | 133127.3112 MeV (-257.6 ppm) |
| ${}^{144}$Ho | 144 | 77 | L?-pending | binding_energy | — | 1154.4621 | — | 134056.2713 MeV (-255.6 ppm) |
| ${}^{145}$Ho | 145 | 78 | L?-pending | binding_energy | — | 1167.0440 | — | 134983.2545 MeV (-253.8 ppm) |
| ${}^{146}$Ho | 146 | 79 | L?-pending | binding_energy | — | 1177.2334 | — | 135912.6303 MeV (-252.1 ppm) |
| ${}^{147}$Ho | 147 | 80 | L?-pending | binding_energy | — | 1189.8236 | — | 136839.6053 MeV (-250.4 ppm) |
| ${}^{148}$Ho | 148 | 81 | L?-pending | binding_energy | — | 1200.1290 | — | 137768.8651 MeV (-248.7 ppm) |
| ${}^{149}$Ho | 149 | 82 | L?-pending | binding_energy | — | 1211.8550 | — | 138696.7043 MeV (-247.0 ppm) |
| ${}^{150}$Ho | 150 | 83 | L?-pending | binding_energy | — | 1220.2263 | — | 139627.8981 MeV (-245.4 ppm) |
| ${}^{151}$Ho | 151 | 84 | L?-pending | binding_energy | — | 1229.9745 | — | 140557.7151 MeV (-243.8 ppm) |
| ${}^{152}$Ho | 152 | 85 | L?-pending | binding_energy | — | 1238.0277 | — | 141489.2271 MeV (-242.2 ppm) |
| ${}^{153}$Ho | 153 | 86 | L?-pending | binding_energy | — | 1247.5065 | — | 142419.3135 MeV (-240.6 ppm) |
| ${}^{154}$Ho | 154 | 87 | L?-pending | binding_energy | — | 1255.2051 | — | 143351.1801 MeV (-239.0 ppm) |
| ${}^{155}$Ho | 155 | 88 | L?-pending | binding_energy | — | 1264.6769 | — | 144281.2735 MeV (-237.5 ppm) |
| ${}^{156}$Ho | 156 | 89 | L?-pending | binding_energy | — | 1272.2468 | — | 145213.2688 MeV (-236.0 ppm) |
| ${}^{157}$Ho | 157 | 90 | L?-pending | binding_energy | — | 1281.6126 | — | 146143.4682 MeV (-234.5 ppm) |
| ${}^{158}$Ho | 158 | 91 | L?-pending | binding_energy | — | 1289.0384 | — | 147075.6075 MeV (-233.0 ppm) |
| ${}^{159}$Ho | 159 | 92 | L?-pending | binding_energy | — | 1298.2519 | — | 148005.9592 MeV (-231.5 ppm) |
| ${}^{160}$Ho | 160 | 93 | L?-pending | binding_energy | — | 1305.3761 | — | 148938.4002 MeV (-230.1 ppm) |
| ${}^{161}$Ho | 161 | 94 | L?-pending | binding_energy | — | 1314.2613 | — | 149869.0802 MeV (-228.6 ppm) |
| ${}^{162}$Ho | 162 | 95 | L?-pending | binding_energy | — | 1321.1768 | — | 150801.7298 MeV (-227.2 ppm) |
| ${}^{163}$Ho | 163 | 96 | L?-pending | binding_energy | — | 1329.5856 | — | 151732.8862 MeV (-225.8 ppm) |
| ${}^{164}$Ho | 164 | 97 | L?-pending | binding_energy | — | 1336.2594 | — | 152665.7776 MeV (-224.5 ppm) |
| ${}^{165}$Ho | 165 | 98 | L?-pending | binding_energy | — | 1344.2483 | — | 153597.3540 MeV (-223.1 ppm) |
| ${}^{166}$Ho | 166 | 99 | L?-pending | binding_energy | — | 1350.4919 | — | 154530.6755 MeV (-221.8 ppm) |
| ${}^{167}$Ho | 167 | 100 | L?-pending | binding_energy | — | 1357.7723 | — | 155462.9603 MeV (-220.4 ppm) |
| ${}^{168}$Ho | 168 | 101 | L?-pending | binding_energy | — | 1363.6234 | — | 156396.6744 MeV (-219.1 ppm) |
| ${}^{169}$Ho | 169 | 102 | L?-pending | binding_energy | — | 1370.4315 | — | 157329.4315 MeV (-217.8 ppm) |
| ${}^{170}$Ho | 170 | 103 | L?-pending | binding_energy | — | 1375.9443 | — | 158263.4838 MeV (-216.5 ppm) |
| ${}^{171}$Ho | 171 | 104 | L?-pending | binding_energy | — | 1382.2960 | — | 159196.6974 MeV (-215.3 ppm) |
| ${}^{172}$Ho | 172 | 105 | L?-pending | binding_energy | — | 1387.3520 | — | 160131.2065 MeV (-214.1 ppm) |
| ${}^{173}$Ho | 173 | 106 | L?-pending | binding_energy | — | 1393.3420 | — | 161064.7817 MeV (-213.2 ppm) |
| ${}^{174}$Ho | 174 | 107 | L?-pending | binding_energy | — | 1397.9160 | — | 161999.7729 MeV (-211.9 ppm) |
| ${}^{175}$Ho | 175 | 108 | L?-pending | binding_energy | — | 1403.3250 | — | 162933.9291 MeV (-210.1 ppm) |
| ${}^{176}$Ho | 176 | 109 | L?-pending | binding_energy | — | 1407.4720 | — | 163869.3473 MeV (-208.8 ppm) |
| ${}^{177}$Ho | 177 | 110 | L?-pending | binding_energy | — | 1412.4600 | — | 164803.9244 MeV (-207.8 ppm) |
| ${}^{178}$Ho | 178 | 111 | L?-pending | binding_energy | — | 1416.3460 | — | 165739.6036 MeV (-206.4 ppm) |

### Erbium (Z = 68)

_0 of 39 isotopes with a framework prediction; 39 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{142}$Er | 142 | 74 | L?-pending | binding_energy | — | 1120.8060 | — | 132209.5036 MeV (-262.6 ppm) |
| ${}^{143}$Er | 143 | 75 | L?-pending | binding_energy | — | 1132.1310 | — | 133137.7438 MeV (-261.0 ppm) |
| ${}^{144}$Er | 144 | 76 | L?-pending | binding_energy | — | 1145.6640 | — | 134063.7760 MeV (-259.3 ppm) |
| ${}^{145}$Er | 145 | 77 | L?-pending | binding_energy | — | 1156.3750 | — | 134992.6302 MeV (-257.5 ppm) |
| ${}^{146}$Er | 146 | 78 | L?-pending | binding_energy | — | 1169.5349 | — | 135919.0355 MeV (-255.8 ppm) |
| ${}^{147}$Er | 147 | 79 | L?-pending | binding_energy | — | 1179.8920 | — | 136848.2436 MeV (-254.1 ppm) |
| ${}^{148}$Er | 148 | 80 | L?-pending | binding_energy | — | 1192.8345 | — | 137774.8663 MeV (-252.4 ppm) |
| ${}^{149}$Er | 149 | 81 | L?-pending | binding_energy | — | 1203.1684 | — | 138704.0975 MeV (-250.7 ppm) |
| ${}^{150}$Er | 150 | 82 | L?-pending | binding_energy | — | 1215.3294 | — | 139631.5017 MeV (-249.0 ppm) |
| ${}^{151}$Er | 151 | 83 | L?-pending | binding_energy | — | 1223.8357 | — | 140562.5606 MeV (-247.4 ppm) |
| ${}^{152}$Er | 152 | 84 | L?-pending | binding_energy | — | 1234.1410 | — | 141491.8205 MeV (-245.8 ppm) |
| ${}^{153}$Er | 153 | 85 | L?-pending | binding_energy | — | 1242.1788 | — | 142423.3479 MeV (-244.2 ppm) |
| ${}^{154}$Er | 154 | 86 | L?-pending | binding_energy | — | 1252.3884 | — | 143352.7035 MeV (-242.6 ppm) |
| ${}^{155}$Er | 155 | 87 | L?-pending | binding_energy | — | 1260.0639 | — | 144284.5932 MeV (-241.0 ppm) |
| ${}^{156}$Er | 156 | 88 | L?-pending | binding_energy | — | 1270.1377 | — | 145214.0845 MeV (-239.5 ppm) |
| ${}^{157}$Er | 157 | 89 | L?-pending | binding_energy | — | 1277.4110 | — | 146146.3764 MeV (-238.0 ppm) |
| ${}^{158}$Er | 158 | 90 | L?-pending | binding_energy | — | 1287.3725 | — | 147075.9801 MeV (-236.4 ppm) |
| ${}^{159}$Er | 159 | 91 | L?-pending | binding_energy | — | 1294.7011 | — | 148008.2167 MeV (-235.0 ppm) |
| ${}^{160}$Er | 160 | 92 | L?-pending | binding_energy | — | 1304.2755 | — | 148938.2075 MeV (-233.5 ppm) |
| ${}^{161}$Er | 161 | 93 | L?-pending | binding_energy | — | 1311.4839 | — | 149870.5642 MeV (-232.0 ppm) |
| ${}^{162}$Er | 162 | 94 | L?-pending | binding_energy | — | 1320.6881 | — | 150800.9252 MeV (-230.6 ppm) |
| ${}^{163}$Er | 163 | 95 | L?-pending | binding_energy | — | 1327.5927 | — | 151733.5859 MeV (-229.2 ppm) |
| ${}^{164}$Er | 164 | 96 | L?-pending | binding_energy | — | 1336.4391 | — | 152664.3046 MeV (-227.8 ppm) |
| ${}^{165}$Er | 165 | 97 | L?-pending | binding_energy | — | 1343.0892 | — | 153597.2197 MeV (-226.4 ppm) |
| ${}^{166}$Er | 166 | 98 | L?-pending | binding_energy | — | 1351.5634 | — | 154528.3107 MeV (-225.1 ppm) |
| ${}^{167}$Er | 167 | 99 | L?-pending | binding_energy | — | 1357.9998 | — | 155461.4395 MeV (-223.7 ppm) |
| ${}^{168}$Er | 168 | 100 | L?-pending | binding_energy | — | 1365.7711 | — | 156393.2334 MeV (-222.4 ppm) |
| ${}^{169}$Er | 169 | 101 | L?-pending | binding_energy | — | 1371.7743 | — | 157326.7953 MeV (-221.1 ppm) |
| ${}^{170}$Er | 170 | 102 | L?-pending | binding_energy | — | 1379.0320 | — | 158259.1028 MeV (-219.8 ppm) |
| ${}^{171}$Er | 171 | 103 | L?-pending | binding_energy | — | 1384.7136 | — | 159192.9864 MeV (-218.5 ppm) |
| ${}^{172}$Er | 172 | 104 | L?-pending | binding_energy | — | 1391.5497 | — | 160125.7155 MeV (-217.2 ppm) |
| ${}^{173}$Er | 173 | 105 | L?-pending | binding_energy | — | 1396.8020 | — | 161060.0284 MeV (-216.0 ppm) |
| ${}^{174}$Er | 174 | 106 | L?-pending | binding_energy | — | 1403.1360 | — | 161993.2596 MeV (-214.6 ppm) |
| ${}^{175}$Er | 175 | 107 | L?-pending | binding_energy | — | 1407.8750 | — | 162928.0857 MeV (-213.1 ppm) |
| ${}^{176}$Er | 176 | 108 | L?-pending | binding_energy | — | 1413.9840 | — | 163861.5419 MeV (-212.3 ppm) |
| ${}^{177}$Er | 177 | 109 | L?-pending | binding_energy | — | 1418.3010 | — | 164796.7901 MeV (-211.2 ppm) |
| ${}^{178}$Er | 178 | 110 | L?-pending | binding_energy | — | 1423.8220 | — | 165730.8343 MeV (-210.3 ppm) |
| ${}^{179}$Er | 179 | 111 | L?-pending | binding_energy | — | 1427.7040 | — | 166666.5175 MeV (-209.0 ppm) |
| ${}^{180}$Er | 180 | 112 | L?-pending | binding_energy | — | 1432.8000 | — | 167600.9867 MeV (-207.4 ppm) |

### Thulium (Z = 69)

_0 of 39 isotopes with a framework prediction; 39 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{144}$Tm | 144 | 75 | L?-pending | binding_energy | — | 1130.4000 | — | 134077.7467 MeV (-262.8 ppm) |
| ${}^{145}$Tm | 145 | 76 | L?-pending | binding_energy | — | 1143.9050 | — | 135003.8069 MeV (-261.1 ppm) |
| ${}^{146}$Tm | 146 | 77 | L?-pending | binding_energy | — | 1155.4440 | — | 135931.8331 MeV (-259.3 ppm) |
| ${}^{147}$Tm | 147 | 78 | L?-pending | binding_energy | — | 1168.4762 | — | 136858.3660 MeV (-257.8 ppm) |
| ${}^{148}$Tm | 148 | 79 | L?-pending | binding_energy | — | 1179.3382 | — | 137787.0693 MeV (-256.1 ppm) |
| ${}^{149}$Tm | 149 | 80 | L?-pending | binding_energy | — | 1192.5960 | — | 138713.3766 MeV (-254.4 ppm) |
| ${}^{150}$Tm | 150 | 81 | L?-pending | binding_energy | — | 1203.1500 | — | 139642.3878 MeV (-252.3 ppm) |
| ${}^{151}$Tm | 151 | 82 | L?-pending | binding_energy | — | 1215.5587 | — | 140569.5443 MeV (-251.0 ppm) |
| ${}^{152}$Tm | 152 | 83 | L?-pending | binding_energy | — | 1224.5787 | — | 141500.0895 MeV (-249.4 ppm) |
| ${}^{153}$Tm | 153 | 84 | L?-pending | binding_energy | — | 1234.9023 | — | 142429.3310 MeV (-247.7 ppm) |
| ${}^{154}$Tm | 154 | 85 | L?-pending | binding_energy | — | 1243.4282 | — | 143360.3703 MeV (-246.1 ppm) |
| ${}^{155}$Tm | 155 | 86 | L?-pending | binding_energy | — | 1253.6983 | — | 144289.6654 MeV (-244.5 ppm) |
| ${}^{156}$Tm | 156 | 87 | L?-pending | binding_energy | — | 1261.9781 | — | 145220.9508 MeV (-243.0 ppm) |
| ${}^{157}$Tm | 157 | 88 | L?-pending | binding_energy | — | 1271.9243 | — | 146150.5698 MeV (-241.4 ppm) |
| ${}^{158}$Tm | 158 | 89 | L?-pending | binding_energy | — | 1279.9895 | — | 147082.0698 MeV (-239.9 ppm) |
| ${}^{159}$Tm | 159 | 90 | L?-pending | binding_energy | — | 1289.9280 | — | 148011.6964 MeV (-238.4 ppm) |
| ${}^{160}$Tm | 160 | 91 | L?-pending | binding_energy | — | 1297.7300 | — | 148943.4597 MeV (-236.9 ppm) |
| ${}^{161}$Tm | 161 | 92 | L?-pending | binding_energy | — | 1307.3990 | — | 149873.3558 MeV (-235.4 ppm) |
| ${}^{162}$Tm | 162 | 93 | L?-pending | binding_energy | — | 1315.0491 | — | 150805.2709 MeV (-234.0 ppm) |
| ${}^{163}$Tm | 163 | 94 | L?-pending | binding_energy | — | 1324.3713 | — | 151735.5139 MeV (-232.6 ppm) |
| ${}^{164}$Tm | 164 | 95 | L?-pending | binding_energy | — | 1331.6232 | — | 152667.8272 MeV (-231.1 ppm) |
| ${}^{165}$Tm | 165 | 96 | L?-pending | binding_energy | — | 1340.7156 | — | 153598.3000 MeV (-229.7 ppm) |
| ${}^{166}$Tm | 166 | 97 | L?-pending | binding_energy | — | 1347.7433 | — | 154530.8374 MeV (-228.4 ppm) |
| ${}^{167}$Tm | 167 | 98 | L?-pending | binding_energy | — | 1356.4713 | — | 155461.6746 MeV (-227.0 ppm) |
| ${}^{168}$Tm | 168 | 99 | L?-pending | binding_energy | — | 1363.3119 | — | 156394.3992 MeV (-225.6 ppm) |
| ${}^{169}$Tm | 169 | 100 | L?-pending | binding_energy | — | 1371.3455 | — | 157325.9308 MeV (-224.3 ppm) |
| ${}^{170}$Tm | 170 | 101 | L?-pending | binding_energy | — | 1377.9374 | — | 158258.9040 MeV (-223.0 ppm) |
| ${}^{171}$Tm | 171 | 102 | L?-pending | binding_energy | — | 1385.4237 | — | 159190.9829 MeV (-221.7 ppm) |
| ${}^{172}$Tm | 172 | 103 | L?-pending | binding_energy | — | 1391.6583 | — | 160124.3135 MeV (-220.4 ppm) |
| ${}^{173}$Tm | 173 | 104 | L?-pending | binding_energy | — | 1398.6122 | — | 161056.9249 MeV (-219.1 ppm) |
| ${}^{174}$Tm | 174 | 105 | L?-pending | binding_energy | — | 1404.2919 | — | 161990.8103 MeV (-217.9 ppm) |
| ${}^{175}$Tm | 175 | 106 | L?-pending | binding_energy | — | 1410.8093 | — | 162923.8581 MeV (-216.6 ppm) |
| ${}^{176}$Tm | 176 | 107 | L?-pending | binding_energy | — | 1415.9414 | — | 163858.2912 MeV (-215.4 ppm) |
| ${}^{177}$Tm | 177 | 108 | L?-pending | binding_energy | — | 1422.1950 | — | 164791.6028 MeV (-214.1 ppm) |
| ${}^{178}$Tm | 178 | 109 | L?-pending | binding_energy | — | 1427.0260 | — | 165726.3370 MeV (-213.4 ppm) |
| ${}^{179}$Tm | 179 | 110 | L?-pending | binding_energy | — | 1432.7160 | — | 166660.2121 MeV (-212.0 ppm) |
| ${}^{180}$Tm | 180 | 111 | L?-pending | binding_energy | — | 1436.9400 | — | 167595.5533 MeV (-210.1 ppm) |
| ${}^{181}$Tm | 181 | 112 | L?-pending | binding_energy | — | 1442.3890 | — | 168529.6695 MeV (-209.6 ppm) |
| ${}^{182}$Tm | 182 | 113 | L?-pending | binding_energy | — | 1446.5360 | — | 169465.0877 MeV (-208.5 ppm) |

### Ytterbium (Z = 70)

_0 of 38 isotopes with a framework prediction; 38 of 38 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{148}$Yb | 148 | 78 | L?-pending | binding_energy | — | 1170.0880 | — | 137795.0261 MeV (-260.3 ppm) |
| ${}^{149}$Yb | 149 | 79 | L?-pending | binding_energy | — | 1181.1230 | — | 138723.5563 MeV (-257.5 ppm) |
| ${}^{150}$Yb | 150 | 80 | L?-pending | binding_energy | — | 1194.7500 | — | 139649.4945 MeV (-256.2 ppm) |
| ${}^{151}$Yb | 151 | 81 | L?-pending | binding_energy | — | 1205.5471 | — | 140578.2625 MeV (-254.6 ppm) |
| ${}^{152}$Yb | 152 | 82 | L?-pending | binding_energy | — | 1218.3464 | — | 141505.0284 MeV (-253.0 ppm) |
| ${}^{153}$Yb | 153 | 83 | L?-pending | binding_energy | — | 1227.3660 | — | 142435.5740 MeV (-251.7 ppm) |
| ${}^{154}$Yb | 154 | 84 | L?-pending | binding_energy | — | 1238.1508 | — | 143364.3544 MeV (-249.7 ppm) |
| ${}^{155}$Yb | 155 | 85 | L?-pending | binding_energy | — | 1246.7926 | — | 144295.2778 MeV (-248.1 ppm) |
| ${}^{156}$Yb | 156 | 86 | L?-pending | binding_energy | — | 1257.6269 | — | 145224.0087 MeV (-246.5 ppm) |
| ${}^{157}$Yb | 157 | 87 | L?-pending | binding_energy | — | 1265.8526 | — | 146155.3482 MeV (-244.9 ppm) |
| ${}^{158}$Yb | 158 | 88 | L?-pending | binding_energy | — | 1276.5136 | — | 147084.2524 MeV (-243.4 ppm) |
| ${}^{159}$Yb | 159 | 89 | L?-pending | binding_energy | — | 1284.4088 | — | 148015.9223 MeV (-241.9 ppm) |
| ${}^{160}$Yb | 160 | 90 | L?-pending | binding_energy | — | 1294.8098 | — | 148945.0865 MeV (-240.3 ppm) |
| ${}^{161}$Yb | 161 | 91 | L?-pending | binding_energy | — | 1302.5522 | — | 149876.9093 MeV (-238.9 ppm) |
| ${}^{162}$Yb | 162 | 92 | L?-pending | binding_energy | — | 1312.6104 | — | 150806.4163 MeV (-237.4 ppm) |
| ${}^{163}$Yb | 163 | 93 | L?-pending | binding_energy | — | 1320.1544 | — | 151738.4374 MeV (-235.9 ppm) |
| ${}^{164}$Yb | 164 | 94 | L?-pending | binding_energy | — | 1329.9440 | — | 152668.2130 MeV (-234.5 ppm) |
| ${}^{165}$Yb | 165 | 95 | L?-pending | binding_energy | — | 1337.2986 | — | 153600.4236 MeV (-233.1 ppm) |
| ${}^{166}$Yb | 166 | 96 | L?-pending | binding_energy | — | 1346.6682 | — | 154530.6192 MeV (-231.7 ppm) |
| ${}^{167}$Yb | 167 | 97 | L?-pending | binding_energy | — | 1353.7357 | — | 155463.1169 MeV (-230.3 ppm) |
| ${}^{168}$Yb | 168 | 98 | L?-pending | binding_energy | — | 1362.7970 | — | 156393.6208 MeV (-228.9 ppm) |
| ${}^{169}$Yb | 169 | 99 | L?-pending | binding_energy | — | 1369.6640 | — | 157326.3190 MeV (-227.6 ppm) |
| ${}^{170}$Yb | 170 | 100 | L?-pending | binding_energy | — | 1378.1237 | — | 158257.4244 MeV (-226.2 ppm) |
| ${}^{171}$Yb | 171 | 101 | L?-pending | binding_energy | — | 1384.7379 | — | 159190.3754 MeV (-224.9 ppm) |
| ${}^{172}$Yb | 172 | 102 | L?-pending | binding_energy | — | 1392.7579 | — | 160121.9206 MeV (-223.6 ppm) |
| ${}^{173}$Yb | 173 | 103 | L?-pending | binding_energy | — | 1399.1250 | — | 161055.1187 MeV (-222.3 ppm) |
| ${}^{174}$Yb | 174 | 104 | L?-pending | binding_energy | — | 1406.5896 | — | 161987.2193 MeV (-221.0 ppm) |
| ${}^{175}$Yb | 175 | 105 | L?-pending | binding_energy | — | 1412.4119 | — | 162920.9621 MeV (-219.8 ppm) |
| ${}^{176}$Yb | 176 | 106 | L?-pending | binding_energy | — | 1419.2790 | — | 163853.6602 MeV (-218.5 ppm) |
| ${}^{177}$Yb | 177 | 107 | L?-pending | binding_energy | — | 1424.8454 | — | 164787.6590 MeV (-217.3 ppm) |
| ${}^{178}$Yb | 178 | 108 | L?-pending | binding_energy | — | 1431.6075 | — | 165720.4622 MeV (-216.0 ppm) |
| ${}^{179}$Yb | 179 | 109 | L?-pending | binding_energy | — | 1436.6540 | — | 166654.9808 MeV (-214.9 ppm) |
| ${}^{180}$Yb | 180 | 110 | L?-pending | binding_energy | — | 1442.8800 | — | 167588.3200 MeV (-214.2 ppm) |
| ${}^{181}$Yb | 181 | 111 | L?-pending | binding_energy | — | 1447.2760 | — | 168523.4892 MeV (-212.7 ppm) |
| ${}^{182}$Yb | 182 | 112 | L?-pending | binding_energy | — | 1453.0880 | — | 169457.2424 MeV (-211.1 ppm) |
| ${}^{183}$Yb | 183 | 113 | L?-pending | binding_energy | — | 1457.2290 | — | 170392.6666 MeV (-209.8 ppm) |
| ${}^{184}$Yb | 184 | 114 | L?-pending | binding_energy | — | 1462.9840 | — | 171326.4767 MeV (-209.1 ppm) |
| ${}^{185}$Yb | 185 | 115 | L?-pending | binding_energy | — | 1466.8650 | — | 172262.1609 MeV (-207.6 ppm) |

### Lutetium (Z = 71)

_0 of 39 isotopes with a framework prediction; 39 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{150}$Lu | 150 | 79 | L?-pending | binding_energy | — | 1179.9000 | — | 139663.0511 MeV (-259.8 ppm) |
| ${}^{151}$Lu | 151 | 80 | L?-pending | binding_energy | — | 1193.5040 | — | 140589.0123 MeV (-258.1 ppm) |
| ${}^{152}$Lu | 152 | 81 | L?-pending | binding_energy | — | 1204.7520 | — | 141517.3295 MeV (-256.8 ppm) |
| ${}^{153}$Lu | 153 | 82 | L?-pending | binding_energy | — | 1217.7405 | — | 142443.9062 MeV (-254.9 ppm) |
| ${}^{154}$Lu | 154 | 83 | L?-pending | binding_energy | — | 1227.0720 | — | 143374.1399 MeV (-253.0 ppm) |
| ${}^{155}$Lu | 155 | 84 | L?-pending | binding_energy | — | 1238.0527 | — | 144302.7243 MeV (-251.6 ppm) |
| ${}^{156}$Lu | 156 | 85 | L?-pending | binding_energy | — | 1247.2785 | — | 145233.0637 MeV (-250.0 ppm) |
| ${}^{157}$Lu | 157 | 86 | L?-pending | binding_energy | — | 1258.0901 | — | 146161.8173 MeV (-248.4 ppm) |
| ${}^{158}$Lu | 158 | 87 | L?-pending | binding_energy | — | 1266.9338 | — | 147092.5388 MeV (-246.8 ppm) |
| ${}^{159}$Lu | 159 | 88 | L?-pending | binding_energy | — | 1277.5015 | — | 148021.5362 MeV (-245.3 ppm) |
| ${}^{160}$Lu | 160 | 89 | L?-pending | binding_energy | — | 1286.1342 | — | 148952.4688 MeV (-243.8 ppm) |
| ${}^{161}$Lu | 161 | 90 | L?-pending | binding_energy | — | 1296.4979 | — | 149881.6702 MeV (-242.3 ppm) |
| ${}^{162}$Lu | 162 | 91 | L?-pending | binding_energy | — | 1304.8387 | — | 150812.8947 MeV (-240.8 ppm) |
| ${}^{163}$Lu | 163 | 92 | L?-pending | binding_energy | — | 1314.8696 | — | 151742.4289 MeV (-239.3 ppm) |
| ${}^{164}$Lu | 164 | 93 | L?-pending | binding_energy | — | 1322.7919 | — | 152674.0718 MeV (-237.8 ppm) |
| ${}^{165}$Lu | 165 | 94 | L?-pending | binding_energy | — | 1332.6631 | — | 153603.7658 MeV (-236.4 ppm) |
| ${}^{166}$Lu | 166 | 95 | L?-pending | binding_energy | — | 1340.3131 | — | 154535.6809 MeV (-235.0 ppm) |
| ${}^{167}$Lu | 167 | 96 | L?-pending | binding_energy | — | 1349.8898 | — | 155465.6695 MeV (-233.6 ppm) |
| ${}^{168}$Lu | 168 | 97 | L?-pending | binding_energy | — | 1357.5076 | — | 156397.6168 MeV (-232.2 ppm) |
| ${}^{169}$Lu | 169 | 98 | L?-pending | binding_energy | — | 1366.5886 | — | 157328.1010 MeV (-230.8 ppm) |
| ${}^{170}$Lu | 170 | 99 | L?-pending | binding_energy | — | 1373.8837 | — | 158260.3712 MeV (-229.4 ppm) |
| ${}^{171}$Lu | 171 | 100 | L?-pending | binding_energy | — | 1382.4772 | — | 159191.3428 MeV (-228.1 ppm) |
| ${}^{172}$Lu | 172 | 101 | L?-pending | binding_energy | — | 1389.4561 | — | 160123.9290 MeV (-226.8 ppm) |
| ${}^{173}$Lu | 173 | 102 | L?-pending | binding_energy | — | 1397.6724 | — | 161055.2780 MeV (-225.5 ppm) |
| ${}^{174}$Lu | 174 | 103 | L?-pending | binding_energy | — | 1404.4330 | — | 161988.0826 MeV (-224.2 ppm) |
| ${}^{175}$Lu | 175 | 104 | L?-pending | binding_energy | — | 1412.0997 | — | 162919.9810 MeV (-222.9 ppm) |
| ${}^{176}$Lu | 176 | 105 | L?-pending | binding_energy | — | 1418.3877 | — | 163853.2582 MeV (-221.6 ppm) |
| ${}^{177}$Lu | 177 | 106 | L?-pending | binding_energy | — | 1425.4606 | — | 164785.7506 MeV (-220.4 ppm) |
| ${}^{178}$Lu | 178 | 107 | L?-pending | binding_energy | — | 1431.4859 | — | 165719.2904 MeV (-219.1 ppm) |
| ${}^{179}$Lu | 179 | 108 | L?-pending | binding_energy | — | 1438.2783 | — | 166652.0632 MeV (-217.9 ppm) |
| ${}^{180}$Lu | 180 | 109 | L?-pending | binding_energy | — | 1443.9671 | — | 167585.9396 MeV (-216.7 ppm) |
| ${}^{181}$Lu | 181 | 110 | L?-pending | binding_energy | — | 1450.1593 | — | 168519.3125 MeV (-215.5 ppm) |
| ${}^{182}$Lu | 182 | 111 | L?-pending | binding_energy | — | 1455.2720 | — | 169453.7650 MeV (-214.7 ppm) |
| ${}^{183}$Lu | 183 | 112 | L?-pending | binding_energy | — | 1461.2207 | — | 170387.3815 MeV (-213.1 ppm) |
| ${}^{184}$Lu | 184 | 113 | L?-pending | binding_energy | — | 1465.9280 | — | 171322.2394 MeV (-212.3 ppm) |
| ${}^{185}$Lu | 185 | 114 | L?-pending | binding_energy | — | 1471.6750 | — | 172256.0576 MeV (-211.2 ppm) |
| ${}^{186}$Lu | 186 | 115 | L?-pending | binding_energy | — | 1476.0960 | — | 173191.2018 MeV (-210.0 ppm) |
| ${}^{187}$Lu | 187 | 116 | L?-pending | binding_energy | — | 1481.6010 | — | 174125.2620 MeV (-208.8 ppm) |
| ${}^{188}$Lu | 188 | 117 | L?-pending | binding_energy | — | 1485.7640 | — | 175060.6641 MeV (-207.9 ppm) |

### Hafnium (Z = 72)

_0 of 38 isotopes with a framework prediction; 38 of 38 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{153}$Hf | 153 | 81 | L?-pending | binding_energy | — | 1205.9460 | — | 142454.4073 MeV (-258.9 ppm) |
| ${}^{154}$Hf | 154 | 82 | L?-pending | binding_energy | — | 1219.3720 | — | 143380.5465 MeV (-256.7 ppm) |
| ${}^{155}$Hf | 155 | 83 | L?-pending | binding_energy | — | 1228.9950 | — | 144310.4887 MeV (-254.9 ppm) |
| ${}^{156}$Hf | 156 | 84 | L?-pending | binding_energy | — | 1240.6161 | — | 145238.4328 MeV (-253.5 ppm) |
| ${}^{157}$Hf | 157 | 85 | L?-pending | binding_energy | — | 1249.7200 | — | 146168.8941 MeV (-251.9 ppm) |
| ${}^{158}$Hf | 158 | 86 | L?-pending | binding_energy | — | 1261.0417 | — | 147097.1376 MeV (-250.3 ppm) |
| ${}^{159}$Hf | 159 | 87 | L?-pending | binding_energy | — | 1269.8632 | — | 148027.8813 MeV (-248.7 ppm) |
| ${}^{160}$Hf | 160 | 88 | L?-pending | binding_energy | — | 1281.0207 | — | 148956.2890 MeV (-247.2 ppm) |
| ${}^{161}$Hf | 161 | 89 | L?-pending | binding_energy | — | 1289.4690 | — | 149887.4058 MeV (-245.7 ppm) |
| ${}^{162}$Hf | 162 | 90 | L?-pending | binding_energy | — | 1300.3930 | — | 150816.0470 MeV (-244.1 ppm) |
| ${}^{163}$Hf | 163 | 91 | L?-pending | binding_energy | — | 1308.5652 | — | 151747.4400 MeV (-242.6 ppm) |
| ${}^{164}$Hf | 164 | 92 | L?-pending | binding_energy | — | 1319.1855 | — | 152676.3849 MeV (-241.2 ppm) |
| ${}^{165}$Hf | 165 | 93 | L?-pending | binding_energy | — | 1327.0740 | — | 153608.0616 MeV (-239.7 ppm) |
| ${}^{166}$Hf | 166 | 94 | L?-pending | binding_energy | — | 1337.3688 | — | 154537.3319 MeV (-238.3 ppm) |
| ${}^{167}$Hf | 167 | 95 | L?-pending | binding_energy | — | 1345.0489 | — | 155469.2170 MeV (-236.8 ppm) |
| ${}^{168}$Hf | 168 | 96 | L?-pending | binding_energy | — | 1355.0130 | — | 156398.8181 MeV (-235.4 ppm) |
| ${}^{169}$Hf | 169 | 97 | L?-pending | binding_energy | — | 1362.4407 | — | 157330.9556 MeV (-234.0 ppm) |
| ${}^{170}$Hf | 170 | 98 | L?-pending | binding_energy | — | 1372.0490 | — | 158260.9125 MeV (-232.7 ppm) |
| ${}^{171}$Hf | 171 | 99 | L?-pending | binding_energy | — | 1379.2977 | — | 159193.2289 MeV (-231.3 ppm) |
| ${}^{172}$Hf | 172 | 100 | L?-pending | binding_energy | — | 1388.3400 | — | 160123.7519 MeV (-230.0 ppm) |
| ${}^{173}$Hf | 173 | 101 | L?-pending | binding_energy | — | 1395.4208 | — | 161056.2362 MeV (-228.6 ppm) |
| ${}^{174}$Hf | 174 | 102 | L?-pending | binding_energy | — | 1403.9249 | — | 161987.2973 MeV (-227.3 ppm) |
| ${}^{175}$Hf | 175 | 103 | L?-pending | binding_energy | — | 1410.6334 | — | 162920.1540 MeV (-226.0 ppm) |
| ${}^{176}$Hf | 176 | 104 | L?-pending | binding_energy | — | 1418.7994 | — | 163851.5532 MeV (-224.7 ppm) |
| ${}^{177}$Hf | 177 | 105 | L?-pending | binding_energy | — | 1425.1751 | — | 164784.7427 MeV (-223.5 ppm) |
| ${}^{178}$Hf | 178 | 106 | L?-pending | binding_energy | — | 1432.8010 | — | 165716.6820 MeV (-222.2 ppm) |
| ${}^{179}$Hf | 179 | 107 | L?-pending | binding_energy | — | 1438.9000 | — | 166650.1482 MeV (-221.0 ppm) |
| ${}^{180}$Hf | 180 | 108 | L?-pending | binding_energy | — | 1446.2877 | — | 167582.3256 MeV (-219.7 ppm) |
| ${}^{181}$Hf | 181 | 109 | L?-pending | binding_energy | — | 1451.9825 | — | 168516.1960 MeV (-218.5 ppm) |
| ${}^{182}$Hf | 182 | 110 | L?-pending | binding_energy | — | 1458.7005 | — | 169449.0432 MeV (-217.3 ppm) |
| ${}^{183}$Hf | 183 | 111 | L?-pending | binding_energy | — | 1464.0058 | — | 170383.3031 MeV (-216.1 ppm) |
| ${}^{184}$Hf | 184 | 112 | L?-pending | binding_energy | — | 1470.2930 | — | 171316.5811 MeV (-215.0 ppm) |
| ${}^{185}$Hf | 185 | 113 | L?-pending | binding_energy | — | 1475.1847 | — | 172251.2546 MeV (-213.8 ppm) |
| ${}^{186}$Hf | 186 | 114 | L?-pending | binding_energy | — | 1481.3604 | — | 173184.6440 MeV (-212.6 ppm) |
| ${}^{187}$Hf | 187 | 115 | L?-pending | binding_energy | — | 1486.0890 | — | 174119.4806 MeV (-212.0 ppm) |
| ${}^{188}$Hf | 188 | 116 | L?-pending | binding_energy | — | 1491.9680 | — | 175053.1668 MeV (-210.7 ppm) |
| ${}^{189}$Hf | 189 | 117 | L?-pending | binding_energy | — | 1496.3130 | — | 175988.3870 MeV (-209.3 ppm) |
| ${}^{190}$Hf | 190 | 118 | L?-pending | binding_energy | — | 1501.9500 | — | 176922.3152 MeV (-207.8 ppm) |

### Tantalum (Z = 73)

_0 of 40 isotopes with a framework prediction; 40 of 40 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{155}$Ta | 155 | 82 | L?-pending | binding_energy | — | 1217.9900 | — | 144320.2004 MeV (-259.1 ppm) |
| ${}^{156}$Ta | 156 | 83 | L?-pending | binding_energy | — | 1228.0320 | — | 145249.7236 MeV (-257.1 ppm) |
| ${}^{157}$Ta | 157 | 84 | L?-pending | binding_energy | — | 1239.6815 | — | 146177.6392 MeV (-255.4 ppm) |
| ${}^{158}$Ta | 158 | 85 | L?-pending | binding_energy | — | 1249.3060 | — | 147107.5799 MeV (-254.0 ppm) |
| ${}^{159}$Ta | 159 | 86 | L?-pending | binding_energy | — | 1260.6674 | — | 148035.7837 MeV (-252.2 ppm) |
| ${}^{160}$Ta | 160 | 87 | L?-pending | binding_energy | — | 1270.1233 | — | 148965.8930 MeV (-250.6 ppm) |
| ${}^{161}$Ta | 161 | 88 | L?-pending | binding_energy | — | 1281.1494 | — | 149894.4320 MeV (-249.0 ppm) |
| ${}^{162}$Ta | 162 | 89 | L?-pending | binding_energy | — | 1290.2236 | — | 150824.9231 MeV (-247.5 ppm) |
| ${}^{163}$Ta | 163 | 90 | L?-pending | binding_energy | — | 1301.0482 | — | 151753.6637 MeV (-246.0 ppm) |
| ${}^{164}$Ta | 164 | 91 | L?-pending | binding_energy | — | 1309.8676 | — | 152684.4094 MeV (-244.5 ppm) |
| ${}^{165}$Ta | 165 | 92 | L?-pending | binding_energy | — | 1320.5040 | — | 153613.3382 MeV (-243.0 ppm) |
| ${}^{166}$Ta | 166 | 93 | L?-pending | binding_energy | — | 1328.8253 | — | 154544.5822 MeV (-241.6 ppm) |
| ${}^{167}$Ta | 167 | 94 | L?-pending | binding_energy | — | 1339.1499 | — | 155473.8227 MeV (-240.1 ppm) |
| ${}^{168}$Ta | 168 | 95 | L?-pending | binding_energy | — | 1347.2640 | — | 156405.2738 MeV (-238.7 ppm) |
| ${}^{169}$Ta | 169 | 96 | L?-pending | binding_energy | — | 1357.2319 | — | 157334.8711 MeV (-237.3 ppm) |
| ${}^{170}$Ta | 170 | 97 | L?-pending | binding_energy | — | 1365.1504 | — | 158266.5178 MeV (-235.9 ppm) |
| ${}^{171}$Ta | 171 | 98 | L?-pending | binding_energy | — | 1374.8043 | — | 159196.4290 MeV (-234.5 ppm) |
| ${}^{172}$Ta | 172 | 99 | L?-pending | binding_energy | — | 1382.4854 | — | 160128.3132 MeV (-233.1 ppm) |
| ${}^{173}$Ta | 173 | 100 | L?-pending | binding_energy | — | 1391.6232 | — | 161058.7405 MeV (-231.8 ppm) |
| ${}^{174}$Ta | 174 | 101 | L?-pending | binding_energy | — | 1399.0388 | — | 161990.8901 MeV (-230.5 ppm) |
| ${}^{175}$Ta | 175 | 102 | L?-pending | binding_energy | — | 1407.7780 | — | 162921.7161 MeV (-229.2 ppm) |
| ${}^{176}$Ta | 176 | 103 | L?-pending | binding_energy | — | 1414.8060 | — | 163854.2532 MeV (-227.9 ppm) |
| ${}^{177}$Ta | 177 | 104 | L?-pending | binding_energy | — | 1423.2267 | — | 164785.3977 MeV (-226.6 ppm) |
| ${}^{178}$Ta | 178 | 105 | L?-pending | binding_energy | — | 1430.2300 | — | 165717.9596 MeV (-225.6 ppm) |
| ${}^{179}$Ta | 179 | 106 | L?-pending | binding_energy | — | 1438.0121 | — | 166649.7428 MeV (-224.0 ppm) |
| ${}^{180}$Ta | 180 | 107 | L?-pending | binding_energy | — | 1444.6596 | — | 167582.6604 MeV (-222.8 ppm) |
| ${}^{181}$Ta | 181 | 108 | L?-pending | binding_energy | — | 1452.2363 | — | 168514.6489 MeV (-221.6 ppm) |
| ${}^{182}$Ta | 182 | 109 | L?-pending | binding_energy | — | 1458.2992 | — | 169448.1511 MeV (-220.3 ppm) |
| ${}^{183}$Ta | 183 | 110 | L?-pending | binding_energy | — | 1465.2334 | — | 170380.7821 MeV (-219.1 ppm) |
| ${}^{184}$Ta | 184 | 111 | L?-pending | binding_energy | — | 1470.8506 | — | 171314.7301 MeV (-217.9 ppm) |
| ${}^{185}$Ta | 185 | 112 | L?-pending | binding_energy | — | 1477.4769 | — | 172247.6690 MeV (-216.8 ppm) |
| ${}^{186}$Ta | 186 | 113 | L?-pending | binding_energy | — | 1482.7614 | — | 173181.9497 MeV (-215.6 ppm) |
| ${}^{187}$Ta | 187 | 114 | L?-pending | binding_energy | — | 1489.1207 | — | 174115.1556 MeV (-214.4 ppm) |
| ${}^{188}$Ta | 188 | 115 | L?-pending | binding_energy | — | 1494.2240 | — | 175049.6175 MeV (-213.4 ppm) |
| ${}^{189}$Ta | 189 | 116 | L?-pending | binding_energy | — | 1500.2820 | — | 175983.1247 MeV (-211.9 ppm) |
| ${}^{190}$Ta | 190 | 117 | L?-pending | binding_energy | — | 1505.1800 | — | 176917.7918 MeV (-211.2 ppm) |
| ${}^{191}$Ta | 191 | 118 | L?-pending | binding_energy | — | 1511.0010 | — | 177851.5360 MeV (-209.8 ppm) |
| ${}^{192}$Ta | 192 | 119 | L?-pending | binding_energy | — | 1515.6480 | — | 178786.4542 MeV (-208.7 ppm) |
| ${}^{193}$Ta | 193 | 120 | L?-pending | binding_energy | — | 1521.4190 | — | 179720.2484 MeV (-207.5 ppm) |
| ${}^{194}$Ta | 194 | 121 | L?-pending | binding_energy | — | 1525.8100 | — | 180655.4226 MeV (-206.4 ppm) |

### Tungsten (Z = 74)

_0 of 41 isotopes with a framework prediction; 41 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{157}$W | 157 | 83 | L?-pending | binding_energy | — | 1228.9960 | — | 146187.0314 MeV (-258.9 ppm) |
| ${}^{158}$W | 158 | 84 | L?-pending | binding_energy | — | 1241.0900 | — | 147114.5026 MeV (-257.4 ppm) |
| ${}^{159}$W | 159 | 85 | L?-pending | binding_energy | — | 1250.8530 | — | 148044.3048 MeV (-255.4 ppm) |
| ${}^{160}$W | 160 | 86 | L?-pending | binding_energy | — | 1262.8463 | — | 148971.8767 MeV (-254.0 ppm) |
| ${}^{161}$W | 161 | 87 | L?-pending | binding_energy | — | 1272.0610 | — | 149902.2272 MeV (-252.2 ppm) |
| ${}^{162}$W | 162 | 88 | L?-pending | binding_energy | — | 1283.6591 | — | 150830.1943 MeV (-250.9 ppm) |
| ${}^{163}$W | 163 | 89 | L?-pending | binding_energy | — | 1292.6396 | — | 151760.7789 MeV (-249.4 ppm) |
| ${}^{164}$W | 164 | 90 | L?-pending | binding_energy | — | 1304.0380 | — | 152688.9457 MeV (-247.8 ppm) |
| ${}^{165}$W | 165 | 91 | L?-pending | binding_energy | — | 1312.7351 | — | 153619.8138 MeV (-246.3 ppm) |
| ${}^{166}$W | 166 | 92 | L?-pending | binding_energy | — | 1323.8326 | — | 154548.2815 MeV (-244.9 ppm) |
| ${}^{167}$W | 167 | 93 | L?-pending | binding_energy | — | 1332.1097 | — | 155479.5696 MeV (-243.4 ppm) |
| ${}^{168}$W | 168 | 94 | L?-pending | binding_energy | — | 1342.9807 | — | 156408.2638 MeV (-242.0 ppm) |
| ${}^{169}$W | 169 | 95 | L?-pending | binding_energy | — | 1351.0769 | — | 157339.7327 MeV (-240.5 ppm) |
| ${}^{170}$W | 170 | 96 | L?-pending | binding_energy | — | 1361.5212 | — | 158268.8536 MeV (-239.1 ppm) |
| ${}^{171}$W | 171 | 97 | L?-pending | binding_energy | — | 1369.3878 | — | 159200.5522 MeV (-237.7 ppm) |
| ${}^{172}$W | 172 | 98 | L?-pending | binding_energy | — | 1379.4702 | — | 160130.0350 MeV (-236.3 ppm) |
| ${}^{173}$W | 173 | 99 | L?-pending | binding_energy | — | 1387.1717 | — | 161061.8986 MeV (-235.0 ppm) |
| ${}^{174}$W | 174 | 100 | L?-pending | binding_energy | — | 1396.7428 | — | 161991.8928 MeV (-233.6 ppm) |
| ${}^{175}$W | 175 | 101 | L?-pending | binding_energy | — | 1404.2198 | — | 162923.9810 MeV (-232.3 ppm) |
| ${}^{176}$W | 176 | 102 | L?-pending | binding_energy | — | 1413.2999 | — | 163854.4660 MeV (-231.0 ppm) |
| ${}^{177}$W | 177 | 103 | L?-pending | binding_energy | — | 1420.4314 | — | 164786.8998 MeV (-229.7 ppm) |
| ${}^{178}$W | 178 | 104 | L?-pending | binding_energy | — | 1429.2080 | — | 165717.6883 MeV (-228.4 ppm) |
| ${}^{179}$W | 179 | 105 | L?-pending | binding_energy | — | 1436.1675 | — | 166650.2940 MeV (-227.1 ppm) |
| ${}^{180}$W | 180 | 106 | L?-pending | binding_energy | — | 1444.5798 | — | 167581.4469 MeV (-225.8 ppm) |
| ${}^{181}$W | 181 | 107 | L?-pending | binding_energy | — | 1451.2488 | — | 168514.3430 MeV (-224.6 ppm) |
| ${}^{182}$W | 182 | 108 | L?-pending | binding_energy | — | 1459.3323 | — | 169445.8247 MeV (-223.4 ppm) |
| ${}^{183}$W | 183 | 109 | L?-pending | binding_energy | — | 1465.5232 | — | 170379.1990 MeV (-222.1 ppm) |
| ${}^{184}$W | 184 | 110 | L?-pending | binding_energy | — | 1472.9343 | — | 171311.3531 MeV (-220.9 ppm) |
| ${}^{185}$W | 185 | 111 | L?-pending | binding_energy | — | 1478.6880 | — | 172245.1646 MeV (-219.7 ppm) |
| ${}^{186}$W | 186 | 112 | L?-pending | binding_energy | — | 1485.8801 | — | 173177.5377 MeV (-218.6 ppm) |
| ${}^{187}$W | 187 | 113 | L?-pending | binding_energy | — | 1491.3468 | — | 174111.6361 MeV (-217.4 ppm) |
| ${}^{188}$W | 188 | 114 | L?-pending | binding_energy | — | 1498.1820 | — | 175044.3661 MeV (-216.2 ppm) |
| ${}^{189}$W | 189 | 115 | L?-pending | binding_energy | — | 1503.3060 | — | 175978.8073 MeV (-214.6 ppm) |
| ${}^{190}$W | 190 | 116 | L?-pending | binding_energy | — | 1510.0256 | — | 176911.6529 MeV (-213.9 ppm) |
| ${}^{191}$W | 191 | 117 | L?-pending | binding_energy | — | 1514.9043 | — | 177846.3394 MeV (-212.8 ppm) |
| ${}^{192}$W | 192 | 118 | L?-pending | binding_energy | — | 1521.4080 | — | 178779.4009 MeV (-211.7 ppm) |
| ${}^{193}$W | 193 | 119 | L?-pending | binding_energy | — | 1526.0510 | — | 179714.3231 MeV (-210.6 ppm) |
| ${}^{194}$W | 194 | 120 | L?-pending | binding_energy | — | 1532.4060 | — | 180647.5333 MeV (-209.8 ppm) |
| ${}^{195}$W | 195 | 121 | L?-pending | binding_energy | — | 1536.7950 | — | 181582.7094 MeV (-208.7 ppm) |
| ${}^{196}$W | 196 | 122 | L?-pending | binding_energy | — | 1542.9120 | — | 182516.1576 MeV (-207.9 ppm) |
| ${}^{197}$W | 197 | 123 | L?-pending | binding_energy | — | 1547.0410 | — | 183451.5938 MeV (-206.4 ppm) |

### Rhenium (Z = 75)

_0 of 41 isotopes with a framework prediction; 41 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{159}$Re | 159 | 84 | L?-pending | binding_energy | — | 1239.4050 | — | 148054.4595 MeV (-258.6 ppm) |
| ${}^{160}$Re | 160 | 85 | L?-pending | binding_energy | — | 1249.6000 | — | 148983.8296 MeV (-257.3 ppm) |
| ${}^{161}$Re | 161 | 86 | L?-pending | binding_energy | — | 1261.6490 | — | 149911.3458 MeV (-255.8 ppm) |
| ${}^{162}$Re | 162 | 87 | L?-pending | binding_energy | — | 1271.3760 | — | 150841.1840 MeV (-254.6 ppm) |
| ${}^{163}$Re | 163 | 88 | L?-pending | binding_energy | — | 1282.9511 | — | 151769.1741 MeV (-252.7 ppm) |
| ${}^{164}$Re | 164 | 89 | L?-pending | binding_energy | — | 1292.4926 | — | 152699.1978 MeV (-251.2 ppm) |
| ${}^{165}$Re | 165 | 90 | L?-pending | binding_energy | — | 1303.7508 | — | 153627.5048 MeV (-249.7 ppm) |
| ${}^{166}$Re | 166 | 91 | L?-pending | binding_energy | — | 1313.0001 | — | 154557.8206 MeV (-248.1 ppm) |
| ${}^{167}$Re | 167 | 92 | L?-pending | binding_energy | — | 1324.1430 | — | 155486.2429 MeV (-247.2 ppm) |
| ${}^{168}$Re | 168 | 93 | L?-pending | binding_energy | — | 1333.1003 | — | 156416.8508 MeV (-245.2 ppm) |
| ${}^{169}$Re | 169 | 94 | L?-pending | binding_energy | — | 1343.7860 | — | 157345.7303 MeV (-243.8 ppm) |
| ${}^{170}$Re | 170 | 95 | L?-pending | binding_energy | — | 1352.3520 | — | 158276.7295 MeV (-242.3 ppm) |
| ${}^{171}$Re | 171 | 96 | L?-pending | binding_energy | — | 1362.7696 | — | 159205.8770 MeV (-240.9 ppm) |
| ${}^{172}$Re | 172 | 97 | L?-pending | binding_energy | — | 1371.1575 | — | 160137.0543 MeV (-239.5 ppm) |
| ${}^{173}$Re | 173 | 98 | L?-pending | binding_energy | — | 1381.2159 | — | 161066.5612 MeV (-238.1 ppm) |
| ${}^{174}$Re | 174 | 99 | L?-pending | binding_energy | — | 1389.4064 | — | 161997.9358 MeV (-236.8 ppm) |
| ${}^{175}$Re | 175 | 100 | L?-pending | binding_energy | — | 1399.0929 | — | 162927.8145 MeV (-235.4 ppm) |
| ${}^{176}$Re | 176 | 101 | L?-pending | binding_energy | — | 1406.9388 | — | 163859.5338 MeV (-234.1 ppm) |
| ${}^{177}$Re | 177 | 102 | L?-pending | binding_energy | — | 1416.2165 | — | 164789.8213 MeV (-232.8 ppm) |
| ${}^{178}$Re | 178 | 103 | L?-pending | binding_energy | — | 1423.6721 | — | 165721.9309 MeV (-231.5 ppm) |
| ${}^{179}$Re | 179 | 104 | L?-pending | binding_energy | — | 1432.6742 | — | 166652.4939 MeV (-230.2 ppm) |
| ${}^{180}$Re | 180 | 105 | L?-pending | binding_energy | — | 1439.9986 | — | 167584.7347 MeV (-228.9 ppm) |
| ${}^{181}$Re | 181 | 106 | L?-pending | binding_energy | — | 1448.7500 | — | 168515.5486 MeV (-227.6 ppm) |
| ${}^{182}$Re | 182 | 107 | L?-pending | binding_energy | — | 1455.7500 | — | 169448.1137 MeV (-226.4 ppm) |
| ${}^{183}$Re | 183 | 108 | L?-pending | binding_energy | — | 1464.1848 | — | 170379.2440 MeV (-225.1 ppm) |
| ${}^{184}$Re | 184 | 109 | L?-pending | binding_energy | — | 1470.6663 | — | 171312.3278 MeV (-223.9 ppm) |
| ${}^{185}$Re | 185 | 110 | L?-pending | binding_energy | — | 1478.3369 | — | 172244.2224 MeV (-222.7 ppm) |
| ${}^{186}$Re | 186 | 111 | L?-pending | binding_energy | — | 1484.5165 | — | 173177.6080 MeV (-221.5 ppm) |
| ${}^{187}$Re | 187 | 112 | L?-pending | binding_energy | — | 1491.8770 | — | 174109.8126 MeV (-220.3 ppm) |
| ${}^{188}$Re | 188 | 113 | L?-pending | binding_energy | — | 1497.7486 | — | 175043.5062 MeV (-219.1 ppm) |
| ${}^{189}$Re | 189 | 114 | L?-pending | binding_energy | — | 1504.7822 | — | 175976.0378 MeV (-218.0 ppm) |
| ${}^{190}$Re | 190 | 115 | L?-pending | binding_energy | — | 1510.4574 | — | 176909.9278 MeV (-216.8 ppm) |
| ${}^{191}$Re | 191 | 116 | L?-pending | binding_energy | — | 1517.2961 | — | 177842.6542 MeV (-215.7 ppm) |
| ${}^{192}$Re | 192 | 117 | L?-pending | binding_energy | — | 1522.6059 | — | 178776.9097 MeV (-214.6 ppm) |
| ${}^{193}$Re | 193 | 118 | L?-pending | binding_energy | — | 1529.3200 | — | 179709.7607 MeV (-213.5 ppm) |
| ${}^{194}$Re | 194 | 119 | L?-pending | binding_energy | — | 1534.3460 | — | 180644.2999 MeV (-212.0 ppm) |
| ${}^{195}$Re | 195 | 120 | L?-pending | binding_energy | — | 1540.6950 | — | 181577.5161 MeV (-210.7 ppm) |
| ${}^{196}$Re | 196 | 121 | L?-pending | binding_energy | — | 1545.6560 | — | 182512.1203 MeV (-210.2 ppm) |
| ${}^{197}$Re | 197 | 122 | L?-pending | binding_energy | — | 1551.7690 | — | 183445.5725 MeV (-209.4 ppm) |
| ${}^{198}$Re | 198 | 123 | L?-pending | binding_energy | — | 1556.4780 | — | 184380.4287 MeV (-208.3 ppm) |
| ${}^{199}$Re | 199 | 124 | L?-pending | binding_energy | — | 1562.1500 | — | 185314.3218 MeV (-206.5 ppm) |

### Osmium (Z = 76)

_0 of 43 isotopes with a framework prediction; 43 of 43 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{161}$Os | 161 | 85 | L?-pending | binding_energy | — | 1250.1650 | — | 149921.5365 MeV (-258.9 ppm) |
| ${}^{162}$Os | 162 | 86 | L?-pending | binding_energy | — | 1262.6280 | — | 150848.6387 MeV (-257.8 ppm) |
| ${}^{163}$Os | 163 | 87 | L?-pending | binding_energy | — | 1272.5410 | — | 151778.2909 MeV (-256.3 ppm) |
| ${}^{164}$Os | 164 | 88 | L?-pending | binding_energy | — | 1284.6625 | — | 152705.7345 MeV (-254.5 ppm) |
| ${}^{165}$Os | 165 | 89 | L?-pending | binding_energy | — | 1294.0950 | — | 153635.8672 MeV (-253.2 ppm) |
| ${}^{166}$Os | 166 | 90 | L?-pending | binding_energy | — | 1305.8120 | — | 154563.7155 MeV (-251.4 ppm) |
| ${}^{167}$Os | 167 | 91 | L?-pending | binding_energy | — | 1314.9506 | — | 155494.1420 MeV (-249.9 ppm) |
| ${}^{168}$Os | 168 | 92 | L?-pending | binding_energy | — | 1326.5181 | — | 156422.1397 MeV (-248.5 ppm) |
| ${}^{169}$Os | 169 | 93 | L?-pending | binding_energy | — | 1335.3174 | — | 157352.9056 MeV (-247.0 ppm) |
| ${}^{170}$Os | 170 | 94 | L?-pending | binding_energy | — | 1346.5914 | — | 158281.1968 MeV (-245.5 ppm) |
| ${}^{171}$Os | 171 | 95 | L?-pending | binding_energy | — | 1355.0342 | — | 159212.3191 MeV (-244.1 ppm) |
| ${}^{172}$Os | 172 | 96 | L?-pending | binding_energy | — | 1366.0520 | — | 160140.8666 MeV (-242.7 ppm) |
| ${}^{173}$Os | 173 | 97 | L?-pending | binding_energy | — | 1374.3179 | — | 161072.1658 MeV (-241.3 ppm) |
| ${}^{174}$Os | 174 | 98 | L?-pending | binding_energy | — | 1384.9464 | — | 162001.1025 MeV (-239.9 ppm) |
| ${}^{175}$Os | 175 | 99 | L?-pending | binding_energy | — | 1393.1276 | — | 162932.4864 MeV (-238.5 ppm) |
| ${}^{176}$Os | 176 | 100 | L?-pending | binding_energy | — | 1403.2248 | — | 163861.9545 MeV (-237.2 ppm) |
| ${}^{177}$Os | 177 | 101 | L?-pending | binding_energy | — | 1411.1214 | — | 164793.6231 MeV (-235.9 ppm) |
| ${}^{178}$Os | 178 | 102 | L?-pending | binding_energy | — | 1420.7805 | — | 165723.5292 MeV (-234.5 ppm) |
| ${}^{179}$Os | 179 | 103 | L?-pending | binding_energy | — | 1428.3277 | — | 166655.5471 MeV (-233.2 ppm) |
| ${}^{180}$Os | 180 | 104 | L?-pending | binding_energy | — | 1437.7351 | — | 167585.7049 MeV (-231.9 ppm) |
| ${}^{181}$Os | 181 | 105 | L?-pending | binding_energy | — | 1445.0002 | — | 168518.0050 MeV (-230.6 ppm) |
| ${}^{182}$Os | 182 | 106 | L?-pending | binding_energy | — | 1454.1306 | — | 169448.4398 MeV (-229.4 ppm) |
| ${}^{183}$Os | 183 | 107 | L?-pending | binding_energy | — | 1461.2566 | — | 170380.8790 MeV (-228.1 ppm) |
| ${}^{184}$Os | 184 | 108 | L?-pending | binding_energy | — | 1469.9167 | — | 171311.7840 MeV (-226.9 ppm) |
| ${}^{185}$Os | 185 | 109 | L?-pending | binding_energy | — | 1476.5414 | — | 172244.7246 MeV (-225.7 ppm) |
| ${}^{186}$Os | 186 | 110 | L?-pending | binding_energy | — | 1484.8068 | — | 173176.0243 MeV (-224.5 ppm) |
| ${}^{187}$Os | 187 | 111 | L?-pending | binding_energy | — | 1491.0971 | — | 174109.2992 MeV (-223.3 ppm) |
| ${}^{188}$Os | 188 | 112 | L?-pending | binding_energy | — | 1499.0867 | — | 175040.8748 MeV (-222.1 ppm) |
| ${}^{189}$Os | 189 | 113 | L?-pending | binding_energy | — | 1505.0075 | — | 175974.5191 MeV (-220.9 ppm) |
| ${}^{190}$Os | 190 | 114 | L?-pending | binding_energy | — | 1512.7999 | — | 176906.2920 MeV (-219.7 ppm) |
| ${}^{191}$Os | 191 | 115 | L?-pending | binding_energy | — | 1518.5586 | — | 177840.0984 MeV (-218.6 ppm) |
| ${}^{192}$Os | 192 | 116 | L?-pending | binding_energy | — | 1526.1170 | — | 178772.1052 MeV (-217.4 ppm) |
| ${}^{193}$Os | 193 | 117 | L?-pending | binding_energy | — | 1531.7004 | — | 179706.0870 MeV (-216.3 ppm) |
| ${}^{194}$Os | 194 | 118 | L?-pending | binding_energy | — | 1538.8125 | — | 180638.5401 MeV (-215.2 ppm) |
| ${}^{195}$Os | 195 | 119 | L?-pending | binding_energy | — | 1543.9603 | — | 181572.9575 MeV (-214.1 ppm) |
| ${}^{196}$Os | 196 | 120 | L?-pending | binding_energy | — | 1550.7971 | — | 182505.6859 MeV (-213.0 ppm) |
| ${}^{197}$Os | 197 | 121 | L?-pending | binding_energy | — | 1555.7090 | — | 183440.3391 MeV (-212.1 ppm) |
| ${}^{198}$Os | 198 | 122 | L?-pending | binding_energy | — | 1562.2200 | — | 184373.3933 MeV (-210.6 ppm) |
| ${}^{199}$Os | 199 | 123 | L?-pending | binding_energy | — | 1566.9260 | — | 185308.2525 MeV (-209.4 ppm) |
| ${}^{200}$Os | 200 | 124 | L?-pending | binding_energy | — | 1573.4000 | — | 186241.3437 MeV (-209.0 ppm) |
| ${}^{201}$Os | 201 | 125 | L?-pending | binding_energy | — | 1577.6490 | — | 187176.6599 MeV (-207.3 ppm) |
| ${}^{202}$Os | 202 | 126 | L?-pending | binding_energy | — | 1583.4780 | — | 188110.3961 MeV (-206.7 ppm) |
| ${}^{203}$Os | 203 | 127 | L?-pending | binding_energy | — | 1586.2420 | — | 189047.1973 MeV (-205.4 ppm) |

### Iridium (Z = 77)

_0 of 43 isotopes with a framework prediction; 43 of 43 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{163}$Ir | 163 | 86 | L?-pending | binding_energy | — | 1260.6420 | — | 151788.8965 MeV (-259.1 ppm) |
| ${}^{164}$Ir | 164 | 87 | L?-pending | binding_energy | — | 1271.0000 | — | 152718.1037 MeV (-258.2 ppm) |
| ${}^{165}$Ir | 165 | 88 | L?-pending | binding_energy | — | 1283.0400 | — | 153645.6289 MeV (-255.7 ppm) |
| ${}^{166}$Ir | 166 | 89 | L?-pending | binding_energy | — | 1292.9740 | — | 154575.2601 MeV (-255.2 ppm) |
| ${}^{167}$Ir | 167 | 90 | L?-pending | binding_energy | — | 1304.7418 | — | 155503.0574 MeV (-253.2 ppm) |
| ${}^{168}$Ir | 168 | 91 | L?-pending | binding_energy | — | 1314.4070 | — | 156432.9575 MeV (-251.7 ppm) |
| ${}^{169}$Ir | 169 | 92 | L?-pending | binding_energy | — | 1325.9055 | — | 157361.0242 MeV (-250.2 ppm) |
| ${}^{170}$Ir | 170 | 93 | L?-pending | binding_energy | — | 1335.0100 | — | 158291.4848 MeV (-248.4 ppm) |
| ${}^{171}$Ir | 171 | 94 | L?-pending | binding_energy | — | 1346.3667 | — | 159219.6933 MeV (-247.3 ppm) |
| ${}^{172}$Ir | 172 | 95 | L?-pending | binding_energy | — | 1355.4054 | — | 160150.2198 MeV (-245.9 ppm) |
| ${}^{173}$Ir | 173 | 96 | L?-pending | binding_energy | — | 1366.3658 | — | 161078.8246 MeV (-244.5 ppm) |
| ${}^{174}$Ir | 174 | 97 | L?-pending | binding_energy | — | 1374.9546 | — | 162009.8010 MeV (-243.1 ppm) |
| ${}^{175}$Ir | 175 | 98 | L?-pending | binding_energy | — | 1385.6345 | — | 162938.6863 MeV (-241.7 ppm) |
| ${}^{176}$Ir | 176 | 99 | L?-pending | binding_energy | — | 1394.1932 | — | 163869.6927 MeV (-240.3 ppm) |
| ${}^{177}$Ir | 177 | 100 | L?-pending | binding_energy | — | 1404.4300 | — | 164799.0211 MeV (-238.9 ppm) |
| ${}^{178}$Ir | 178 | 101 | L?-pending | binding_energy | — | 1412.7082 | — | 165730.3081 MeV (-237.6 ppm) |
| ${}^{179}$Ir | 179 | 102 | L?-pending | binding_energy | — | 1422.6069 | — | 166659.9745 MeV (-236.3 ppm) |
| ${}^{180}$Ir | 180 | 103 | L?-pending | binding_energy | — | 1430.5741 | — | 167591.5726 MeV (-235.0 ppm) |
| ${}^{181}$Ir | 181 | 104 | L?-pending | binding_energy | — | 1440.1309 | — | 168521.5810 MeV (-233.7 ppm) |
| ${}^{182}$Ir | 182 | 105 | L?-pending | binding_energy | — | 1447.7909 | — | 169453.4862 MeV (-232.4 ppm) |
| ${}^{183}$Ir | 183 | 106 | L?-pending | binding_energy | — | 1457.0126 | — | 170383.8296 MeV (-231.1 ppm) |
| ${}^{184}$Ir | 184 | 107 | L?-pending | binding_energy | — | 1464.4927 | — | 171315.9148 MeV (-229.9 ppm) |
| ${}^{185}$Ir | 185 | 108 | L?-pending | binding_energy | — | 1473.2887 | — | 172246.6839 MeV (-228.6 ppm) |
| ${}^{186}$Ir | 186 | 109 | L?-pending | binding_energy | — | 1480.1968 | — | 173179.3410 MeV (-227.4 ppm) |
| ${}^{187}$Ir | 187 | 110 | L?-pending | binding_energy | — | 1488.6451 | — | 174110.4578 MeV (-226.2 ppm) |
| ${}^{188}$Ir | 188 | 111 | L?-pending | binding_energy | — | 1495.5120 | — | 175043.1561 MeV (-225.0 ppm) |
| ${}^{189}$Ir | 189 | 112 | L?-pending | binding_energy | — | 1503.6880 | — | 175974.5453 MeV (-223.8 ppm) |
| ${}^{190}$Ir | 190 | 113 | L?-pending | binding_energy | — | 1510.0633 | — | 176907.7352 MeV (-222.6 ppm) |
| ${}^{191}$Ir | 191 | 114 | L?-pending | binding_energy | — | 1518.0899 | — | 177839.2739 MeV (-221.4 ppm) |
| ${}^{192}$Ir | 192 | 115 | L?-pending | binding_energy | — | 1524.2880 | — | 178772.6409 MeV (-220.3 ppm) |
| ${}^{193}$Ir | 193 | 116 | L?-pending | binding_energy | — | 1532.0600 | — | 179704.4341 MeV (-219.2 ppm) |
| ${}^{194}$Ir | 194 | 117 | L?-pending | binding_energy | — | 1538.1268 | — | 180637.9325 MeV (-218.0 ppm) |
| ${}^{195}$Ir | 195 | 118 | L?-pending | binding_energy | — | 1545.3586 | — | 181570.2658 MeV (-216.9 ppm) |
| ${}^{196}$Ir | 196 | 119 | L?-pending | binding_energy | — | 1551.1731 | — | 182504.0165 MeV (-215.8 ppm) |
| ${}^{197}$Ir | 197 | 120 | L?-pending | binding_energy | — | 1558.0731 | — | 183436.6818 MeV (-214.7 ppm) |
| ${}^{198}$Ir | 198 | 121 | L?-pending | binding_energy | — | 1563.6060 | — | 184370.7140 MeV (-213.7 ppm) |
| ${}^{199}$Ir | 199 | 122 | L?-pending | binding_energy | — | 1570.3501 | — | 185303.5351 MeV (-212.5 ppm) |
| ${}^{200}$Ir | 200 | 123 | L?-pending | binding_energy | — | 1575.6000 | — | 186237.8504 MeV (-211.5 ppm) |
| ${}^{201}$Ir | 201 | 124 | L?-pending | binding_energy | — | 1581.8700 | — | 187171.1456 MeV (-210.1 ppm) |
| ${}^{202}$Ir | 202 | 125 | L?-pending | binding_energy | — | 1586.7100 | — | 188105.8707 MeV (-208.9 ppm) |
| ${}^{203}$Ir | 203 | 126 | L?-pending | binding_energy | — | 1592.5350 | — | 189039.6109 MeV (-208.0 ppm) |
| ${}^{204}$Ir | 204 | 127 | L?-pending | binding_energy | — | 1595.8920 | — | 189975.8191 MeV (-207.4 ppm) |
| ${}^{205}$Ir | 205 | 128 | L?-pending | binding_energy | — | 1600.0250 | — | 190911.2513 MeV (-206.5 ppm) |

### Platinum (Z = 78)

_0 of 44 isotopes with a framework prediction; 44 of 44 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{165}$Pt | 165 | 87 | L?-pending | binding_energy | — | 1270.9950 | — | 153656.3806 MeV (-259.1 ppm) |
| ${}^{166}$Pt | 166 | 88 | L?-pending | binding_energy | — | 1283.6780 | — | 154583.2628 MeV (-258.5 ppm) |
| ${}^{167}$Pt | 167 | 89 | L?-pending | binding_energy | — | 1293.5820 | — | 155512.9239 MeV (-256.1 ppm) |
| ${}^{168}$Pt | 168 | 90 | L?-pending | binding_energy | — | 1305.9684 | — | 156440.1027 MeV (-255.0 ppm) |
| ${}^{169}$Pt | 169 | 91 | L?-pending | binding_energy | — | 1315.4960 | — | 157370.1403 MeV (-253.5 ppm) |
| ${}^{170}$Pt | 170 | 92 | L?-pending | binding_energy | — | 1327.4002 | — | 158297.8013 MeV (-252.0 ppm) |
| ${}^{171}$Pt | 171 | 93 | L?-pending | binding_energy | — | 1336.6389 | — | 159228.1278 MeV (-250.5 ppm) |
| ${}^{172}$Pt | 172 | 94 | L?-pending | binding_energy | — | 1348.3503 | — | 160155.9816 MeV (-249.1 ppm) |
| ${}^{173}$Pt | 173 | 95 | L?-pending | binding_energy | — | 1357.2517 | — | 161086.6453 MeV (-247.6 ppm) |
| ${}^{174}$Pt | 174 | 96 | L?-pending | binding_energy | — | 1368.7039 | — | 162014.7583 MeV (-246.2 ppm) |
| ${}^{175}$Pt | 175 | 97 | L?-pending | binding_energy | — | 1377.1663 | — | 162945.8611 MeV (-244.8 ppm) |
| ${}^{176}$Pt | 176 | 98 | L?-pending | binding_energy | — | 1388.4628 | — | 163874.1298 MeV (-243.4 ppm) |
| ${}^{177}$Pt | 177 | 99 | L?-pending | binding_energy | — | 1396.9707 | — | 164805.1871 MeV (-242.0 ppm) |
| ${}^{178}$Pt | 178 | 100 | L?-pending | binding_energy | — | 1407.6690 | — | 165734.0539 MeV (-240.7 ppm) |
| ${}^{179}$Pt | 179 | 101 | L?-pending | binding_energy | — | 1416.0110 | — | 166665.2772 MeV (-239.3 ppm) |
| ${}^{180}$Pt | 180 | 102 | L?-pending | binding_energy | — | 1426.2441 | — | 167594.6093 MeV (-238.0 ppm) |
| ${}^{181}$Pt | 181 | 103 | L?-pending | binding_energy | — | 1434.2670 | — | 168526.1515 MeV (-236.7 ppm) |
| ${}^{182}$Pt | 182 | 104 | L?-pending | binding_energy | — | 1444.1252 | — | 169455.8585 MeV (-235.4 ppm) |
| ${}^{183}$Pt | 183 | 105 | L?-pending | binding_energy | — | 1451.8013 | — | 170387.7476 MeV (-234.1 ppm) |
| ${}^{184}$Pt | 184 | 106 | L?-pending | binding_energy | — | 1461.4319 | — | 171317.6821 MeV (-232.8 ppm) |
| ${}^{185}$Pt | 185 | 107 | L?-pending | binding_energy | — | 1468.8589 | — | 172249.8204 MeV (-231.6 ppm) |
| ${}^{186}$Pt | 186 | 108 | L?-pending | binding_energy | — | 1478.1065 | — | 173180.1379 MeV (-230.3 ppm) |
| ${}^{187}$Pt | 187 | 109 | L?-pending | binding_energy | — | 1484.9988 | — | 174112.8109 MeV (-229.1 ppm) |
| ${}^{188}$Pt | 188 | 110 | L?-pending | binding_energy | — | 1494.2057 | — | 175043.1691 MeV (-227.9 ppm) |
| ${}^{189}$Pt | 189 | 111 | L?-pending | binding_energy | — | 1500.9255 | — | 175976.0146 MeV (-226.7 ppm) |
| ${}^{190}$Pt | 190 | 112 | L?-pending | binding_energy | — | 1509.8339 | — | 176906.6713 MeV (-225.5 ppm) |
| ${}^{191}$Pt | 191 | 113 | L?-pending | binding_energy | — | 1516.2970 | — | 177839.7733 MeV (-224.3 ppm) |
| ${}^{192}$Pt | 192 | 114 | L?-pending | binding_energy | — | 1524.9585 | — | 178770.6770 MeV (-223.2 ppm) |
| ${}^{193}$Pt | 193 | 115 | L?-pending | binding_energy | — | 1531.2210 | — | 179703.9798 MeV (-222.0 ppm) |
| ${}^{194}$Pt | 194 | 116 | L?-pending | binding_energy | — | 1539.5727 | — | 180635.1932 MeV (-220.9 ppm) |
| ${}^{195}$Pt | 195 | 117 | L?-pending | binding_energy | — | 1545.6778 | — | 181568.6533 MeV (-219.7 ppm) |
| ${}^{196}$Pt | 196 | 118 | L?-pending | binding_energy | — | 1553.5998 | — | 182500.2965 MeV (-218.6 ppm) |
| ${}^{197}$Pt | 197 | 119 | L?-pending | binding_energy | — | 1559.4464 | — | 183434.0151 MeV (-217.5 ppm) |
| ${}^{198}$Pt | 198 | 120 | L?-pending | binding_energy | — | 1567.0019 | — | 184366.0247 MeV (-216.4 ppm) |
| ${}^{199}$Pt | 199 | 121 | L?-pending | binding_energy | — | 1572.5579 | — | 185300.0339 MeV (-215.3 ppm) |
| ${}^{200}$Pt | 200 | 122 | L?-pending | binding_energy | — | 1579.8397 | — | 186232.3173 MeV (-214.2 ppm) |
| ${}^{201}$Pt | 201 | 123 | L?-pending | binding_energy | — | 1585.0526 | — | 187166.6696 MeV (-213.2 ppm) |
| ${}^{202}$Pt | 202 | 124 | L?-pending | binding_energy | — | 1592.0753 | — | 188099.2121 MeV (-212.1 ppm) |
| ${}^{203}$Pt | 203 | 125 | L?-pending | binding_energy | — | 1597.0010 | — | 189033.8516 MeV (-211.2 ppm) |
| ${}^{204}$Pt | 204 | 126 | L?-pending | binding_energy | — | 1603.2360 | — | 189967.1818 MeV (-210.5 ppm) |
| ${}^{205}$Pt | 205 | 127 | L?-pending | binding_energy | — | 1606.3800 | — | 190903.6030 MeV (-208.8 ppm) |
| ${}^{206}$Pt | 206 | 128 | L?-pending | binding_energy | — | 1610.9200 | — | 191838.6281 MeV (-208.0 ppm) |
| ${}^{207}$Pt | 207 | 129 | L?-pending | binding_energy | — | 1613.9790 | — | 192775.1343 MeV (-207.5 ppm) |
| ${}^{208}$Pt | 208 | 130 | L?-pending | binding_energy | — | 1618.2400 | — | 193710.4385 MeV (-205.6 ppm) |

### Gold (Z = 79)

_0 of 43 isotopes with a framework prediction; 43 of 43 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{168}$Au | 168 | 89 | L?-pending | binding_energy | — | 1291.5840 | — | 156453.1938 MeV (-257.8 ppm) |
| ${}^{169}$Au | 169 | 90 | L?-pending | binding_energy | — | 1304.0040 | — | 157380.3390 MeV (-256.5 ppm) |
| ${}^{170}$Au | 170 | 91 | L?-pending | binding_energy | — | 1314.1000 | — | 158309.8082 MeV (-255.7 ppm) |
| ${}^{171}$Au | 171 | 92 | L?-pending | binding_energy | — | 1325.9523 | — | 159237.5211 MeV (-253.7 ppm) |
| ${}^{172}$Au | 172 | 93 | L?-pending | binding_energy | — | 1335.7793 | — | 160167.2592 MeV (-252.2 ppm) |
| ${}^{173}$Au | 173 | 94 | L?-pending | binding_energy | — | 1347.3646 | — | 161095.2391 MeV (-250.8 ppm) |
| ${}^{174}$Au | 174 | 95 | L?-pending | binding_energy | — | 1356.6780 | — | 162025.4909 MeV (-249.4 ppm) |
| ${}^{175}$Au | 175 | 96 | L?-pending | binding_energy | — | 1368.0789 | — | 162953.6552 MeV (-247.9 ppm) |
| ${}^{176}$Au | 176 | 97 | L?-pending | binding_energy | — | 1377.2675 | — | 163884.0317 MeV (-246.5 ppm) |
| ${}^{177}$Au | 177 | 98 | L?-pending | binding_energy | — | 1388.3636 | — | 164812.5008 MeV (-245.1 ppm) |
| ${}^{178}$Au | 178 | 99 | L?-pending | binding_energy | — | 1397.1922 | — | 165743.2374 MeV (-243.8 ppm) |
| ${}^{179}$Au | 179 | 100 | L?-pending | binding_energy | — | 1407.9491 | — | 166672.0457 MeV (-242.4 ppm) |
| ${}^{180}$Au | 180 | 101 | L?-pending | binding_energy | — | 1416.6575 | — | 167602.9025 MeV (-241.0 ppm) |
| ${}^{181}$Au | 181 | 102 | L?-pending | binding_energy | — | 1426.9743 | — | 168532.1509 MeV (-239.7 ppm) |
| ${}^{182}$Au | 182 | 103 | L?-pending | binding_energy | — | 1435.4784 | — | 169463.2119 MeV (-238.4 ppm) |
| ${}^{183}$Au | 183 | 104 | L?-pending | binding_energy | — | 1445.4373 | — | 170392.8183 MeV (-237.1 ppm) |
| ${}^{184}$Au | 184 | 105 | L?-pending | binding_energy | — | 1453.6358 | — | 171324.1849 MeV (-235.8 ppm) |
| ${}^{185}$Au | 185 | 106 | L?-pending | binding_energy | — | 1463.2466 | — | 172254.1393 MeV (-234.5 ppm) |
| ${}^{186}$Au | 186 | 107 | L?-pending | binding_energy | — | 1471.1746 | — | 173185.7765 MeV (-233.3 ppm) |
| ${}^{187}$Au | 187 | 108 | L?-pending | binding_energy | — | 1480.5598 | — | 174115.9565 MeV (-232.0 ppm) |
| ${}^{188}$Au | 188 | 109 | L?-pending | binding_energy | — | 1487.9737 | — | 175048.1078 MeV (-230.8 ppm) |
| ${}^{189}$Au | 189 | 110 | L?-pending | binding_energy | — | 1497.2557 | — | 175978.3910 MeV (-229.6 ppm) |
| ${}^{190}$Au | 190 | 111 | L?-pending | binding_energy | — | 1504.5786 | — | 176910.6333 MeV (-228.4 ppm) |
| ${}^{191}$Au | 191 | 112 | L?-pending | binding_energy | — | 1513.6142 | — | 177841.1628 MeV (-227.2 ppm) |
| ${}^{192}$Au | 192 | 113 | L?-pending | binding_energy | — | 1520.6598 | — | 178773.6824 MeV (-226.0 ppm) |
| ${}^{193}$Au | 193 | 114 | L?-pending | binding_energy | — | 1529.3638 | — | 179704.5436 MeV (-224.8 ppm) |
| ${}^{194}$Au | 194 | 115 | L?-pending | binding_energy | — | 1536.2422 | — | 180637.2304 MeV (-223.7 ppm) |
| ${}^{195}$Au | 195 | 116 | L?-pending | binding_energy | — | 1544.6687 | — | 181568.3691 MeV (-222.5 ppm) |
| ${}^{196}$Au | 196 | 117 | L?-pending | binding_energy | — | 1551.3116 | — | 182501.2913 MeV (-221.4 ppm) |
| ${}^{197}$Au | 197 | 118 | L?-pending | binding_energy | — | 1559.3840 | — | 183432.7842 MeV (-220.3 ppm) |
| ${}^{198}$Au | 198 | 119 | L?-pending | binding_energy | — | 1565.8964 | — | 184365.8370 MeV (-219.2 ppm) |
| ${}^{199}$Au | 199 | 120 | L?-pending | binding_energy | — | 1573.4806 | — | 185297.8179 MeV (-218.1 ppm) |
| ${}^{200}$Au | 200 | 121 | L?-pending | binding_energy | — | 1579.6983 | — | 186231.1654 MeV (-217.0 ppm) |
| ${}^{201}$Au | 201 | 122 | L?-pending | binding_energy | — | 1586.9302 | — | 187163.4987 MeV (-215.9 ppm) |
| ${}^{202}$Au | 202 | 123 | L?-pending | binding_energy | — | 1592.9538 | — | 188097.0403 MeV (-214.8 ppm) |
| ${}^{203}$Au | 203 | 124 | L?-pending | binding_energy | — | 1599.8156 | — | 189029.7437 MeV (-213.8 ppm) |
| ${}^{204}$Au | 204 | 125 | L?-pending | binding_energy | — | 1605.0720 | — | 189964.0524 MeV (-212.4 ppm) |
| ${}^{205}$Au | 205 | 126 | L?-pending | binding_energy | — | 1611.3000 | — | 190897.3896 MeV (-211.2 ppm) |
| ${}^{206}$Au | 206 | 127 | L?-pending | binding_energy | — | 1615.0400 | — | 191833.2148 MeV (-210.5 ppm) |
| ${}^{207}$Au | 207 | 128 | L?-pending | binding_energy | — | 1619.5680 | — | 192768.2520 MeV (-209.5 ppm) |
| ${}^{208}$Au | 208 | 129 | L?-pending | binding_energy | — | 1623.0240 | — | 193704.3612 MeV (-209.0 ppm) |
| ${}^{209}$Au | 209 | 130 | L?-pending | binding_energy | — | 1627.2740 | — | 194639.6764 MeV (-207.3 ppm) |
| ${}^{210}$Au | 210 | 131 | L?-pending | binding_energy | — | 1630.4400 | — | 195576.0755 MeV (-206.4 ppm) |

### Mercury (Z = 80)

_0 of 47 isotopes with a framework prediction; 47 of 47 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{170}$Hg | 170 | 90 | L?-pending | binding_energy | — | 1304.0700 | — | 158318.5448 MeV (-258.1 ppm) |
| ${}^{171}$Hg | 171 | 91 | L?-pending | binding_energy | — | 1314.3060 | — | 159247.8740 MeV (-257.1 ppm) |
| ${}^{172}$Hg | 172 | 92 | L?-pending | binding_energy | — | 1326.7403 | — | 160175.0049 MeV (-255.4 ppm) |
| ${}^{173}$Hg | 173 | 93 | L?-pending | binding_energy | — | 1336.4250 | — | 161104.8854 MeV (-254.0 ppm) |
| ${}^{174}$Hg | 174 | 94 | L?-pending | binding_energy | — | 1348.4626 | — | 162032.4130 MeV (-252.5 ppm) |
| ${}^{175}$Hg | 175 | 95 | L?-pending | binding_energy | — | 1357.8623 | — | 162962.5784 MeV (-251.0 ppm) |
| ${}^{176}$Hg | 176 | 96 | L?-pending | binding_energy | — | 1369.7489 | — | 163890.2571 MeV (-249.6 ppm) |
| ${}^{177}$Hg | 177 | 97 | L?-pending | binding_energy | — | 1378.8114 | — | 164820.7598 MeV (-248.2 ppm) |
| ${}^{178}$Hg | 178 | 98 | L?-pending | binding_energy | — | 1390.4222 | — | 165748.7141 MeV (-246.8 ppm) |
| ${}^{179}$Hg | 179 | 99 | L?-pending | binding_energy | — | 1399.1111 | — | 166679.5904 MeV (-245.4 ppm) |
| ${}^{180}$Hg | 180 | 100 | L?-pending | binding_energy | — | 1410.5000 | — | 167607.7667 MeV (-244.1 ppm) |
| ${}^{181}$Hg | 181 | 101 | L?-pending | binding_energy | — | 1418.9819 | — | 168538.8499 MeV (-242.7 ppm) |
| ${}^{182}$Hg | 182 | 102 | L?-pending | binding_energy | — | 1429.9690 | — | 169467.4280 MeV (-241.4 ppm) |
| ${}^{183}$Hg | 183 | 103 | L?-pending | binding_energy | — | 1438.2681 | — | 170398.6941 MeV (-240.1 ppm) |
| ${}^{184}$Hg | 184 | 104 | L?-pending | binding_energy | — | 1448.8796 | — | 171327.6479 MeV (-238.8 ppm) |
| ${}^{185}$Hg | 185 | 105 | L?-pending | binding_energy | — | 1456.7897 | — | 172259.3029 MeV (-237.5 ppm) |
| ${}^{186}$Hg | 186 | 106 | L?-pending | binding_energy | — | 1467.2165 | — | 173188.4413 MeV (-236.2 ppm) |
| ${}^{187}$Hg | 187 | 107 | L?-pending | binding_energy | — | 1474.8672 | — | 174120.3557 MeV (-235.0 ppm) |
| ${}^{188}$Hg | 188 | 108 | L?-pending | binding_energy | — | 1485.0184 | — | 175049.7698 MeV (-233.7 ppm) |
| ${}^{189}$Hg | 189 | 109 | L?-pending | binding_energy | — | 1492.5177 | — | 175981.8356 MeV (-232.5 ppm) |
| ${}^{190}$Hg | 190 | 110 | L?-pending | binding_energy | — | 1502.3333 | — | 176911.5852 MeV (-231.3 ppm) |
| ${}^{191}$Hg | 191 | 111 | L?-pending | binding_energy | — | 1509.6258 | — | 177843.8579 MeV (-230.1 ppm) |
| ${}^{192}$Hg | 192 | 112 | L?-pending | binding_energy | — | 1519.1168 | — | 178773.9321 MeV (-228.9 ppm) |
| ${}^{193}$Hg | 193 | 113 | L?-pending | binding_energy | — | 1526.2388 | — | 179706.3753 MeV (-227.7 ppm) |
| ${}^{194}$Hg | 194 | 114 | L?-pending | binding_energy | — | 1535.4319 | — | 180636.7474 MeV (-226.5 ppm) |
| ${}^{195}$Hg | 195 | 115 | L?-pending | binding_energy | — | 1542.3326 | — | 181569.4118 MeV (-225.3 ppm) |
| ${}^{196}$Hg | 196 | 116 | L?-pending | binding_energy | — | 1551.2165 | — | 182500.0931 MeV (-224.2 ppm) |
| ${}^{197}$Hg | 197 | 117 | L?-pending | binding_energy | — | 1558.0021 | — | 183432.8727 MeV (-223.1 ppm) |
| ${}^{198}$Hg | 198 | 118 | L?-pending | binding_energy | — | 1566.4875 | — | 184363.9525 MeV (-221.9 ppm) |
| ${}^{199}$Hg | 199 | 119 | L?-pending | binding_energy | — | 1573.1506 | — | 185296.8546 MeV (-220.8 ppm) |
| ${}^{200}$Hg | 200 | 120 | L?-pending | binding_energy | — | 1581.1791 | — | 186228.3913 MeV (-219.7 ppm) |
| ${}^{201}$Hg | 201 | 121 | L?-pending | binding_energy | — | 1587.4097 | — | 187161.7259 MeV (-218.6 ppm) |
| ${}^{202}$Hg | 202 | 122 | L?-pending | binding_energy | — | 1595.1638 | — | 188093.5369 MeV (-217.5 ppm) |
| ${}^{203}$Hg | 203 | 123 | L?-pending | binding_energy | — | 1601.1590 | — | 189027.1069 MeV (-216.5 ppm) |
| ${}^{204}$Hg | 204 | 124 | L?-pending | binding_energy | — | 1608.6513 | — | 189959.1798 MeV (-215.4 ppm) |
| ${}^{205}$Hg | 205 | 125 | L?-pending | binding_energy | — | 1614.3202 | — | 190893.0761 MeV (-214.4 ppm) |
| ${}^{206}$Hg | 206 | 126 | L?-pending | binding_energy | — | 1621.0495 | — | 191825.9120 MeV (-213.3 ppm) |
| ${}^{207}$Hg | 207 | 127 | L?-pending | binding_energy | — | 1624.6625 | — | 192761.8641 MeV (-212.3 ppm) |
| ${}^{208}$Hg | 208 | 128 | L?-pending | binding_energy | — | 1629.5118 | — | 193696.5800 MeV (-211.3 ppm) |
| ${}^{209}$Hg | 209 | 129 | L?-pending | binding_energy | — | 1632.9170 | — | 194632.7400 MeV (-210.2 ppm) |
| ${}^{210}$Hg | 210 | 130 | L?-pending | binding_energy | — | 1637.7900 | — | 195567.4322 MeV (-209.8 ppm) |
| ${}^{211}$Hg | 211 | 131 | L?-pending | binding_energy | — | 1640.9470 | — | 196503.8404 MeV (-208.7 ppm) |
| ${}^{212}$Hg | 212 | 132 | L?-pending | binding_energy | — | 1645.5440 | — | 197438.8086 MeV (-207.4 ppm) |
| ${}^{213}$Hg | 213 | 133 | L?-pending | binding_energy | — | 1648.4070 | — | 198375.5108 MeV (-206.3 ppm) |
| ${}^{214}$Hg | 214 | 134 | L?-pending | binding_energy | — | 1652.9360 | — | 199310.5470 MeV (-205.5 ppm) |
| ${}^{215}$Hg | 215 | 135 | L?-pending | binding_energy | — | 1655.7150 | — | 200247.3331 MeV (-204.7 ppm) |
| ${}^{216}$Hg | 216 | 136 | L?-pending | binding_energy | — | 1659.9600 | — | 201182.6533 MeV (-203.7 ppm) |

### Thallium (Z = 81)

_0 of 43 isotopes with a framework prediction; 43 of 43 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{176}$Tl | 176 | 95 | L?-pending | binding_energy | — | 1356.5971 | — | 163902.1155 MeV (-252.7 ppm) |
| ${}^{177}$Tl | 177 | 96 | L?-pending | binding_energy | — | 1368.5933 | — | 164829.6845 MeV (-251.3 ppm) |
| ${}^{178}$Tl | 178 | 97 | L?-pending | binding_energy | — | 1377.8980 | — | 165759.9450 MeV (-249.6 ppm) |
| ${}^{179}$Tl | 179 | 98 | L?-pending | binding_energy | — | 1389.6655 | — | 166687.7427 MeV (-248.5 ppm) |
| ${}^{180}$Tl | 180 | 99 | L?-pending | binding_energy | — | 1398.8576 | — | 167618.1158 MeV (-247.1 ppm) |
| ${}^{181}$Tl | 181 | 100 | L?-pending | binding_energy | — | 1410.3372 | — | 168546.2013 MeV (-245.8 ppm) |
| ${}^{182}$Tl | 182 | 101 | L?-pending | binding_energy | — | 1418.9370 | — | 169477.1667 MeV (-244.4 ppm) |
| ${}^{183}$Tl | 183 | 102 | L?-pending | binding_energy | — | 1430.2684 | — | 170405.4005 MeV (-243.1 ppm) |
| ${}^{184}$Tl | 184 | 103 | L?-pending | binding_energy | — | 1438.6358 | — | 171336.5983 MeV (-241.8 ppm) |
| ${}^{185}$Tl | 185 | 104 | L?-pending | binding_energy | — | 1449.5815 | — | 172265.2178 MeV (-240.5 ppm) |
| ${}^{186}$Tl | 186 | 105 | L?-pending | binding_energy | — | 1457.7780 | — | 173196.5865 MeV (-239.2 ppm) |
| ${}^{187}$Tl | 187 | 106 | L?-pending | binding_energy | — | 1468.4110 | — | 174125.5187 MeV (-237.9 ppm) |
| ${}^{188}$Tl | 188 | 107 | L?-pending | binding_energy | — | 1476.3741 | — | 175057.1207 MeV (-236.6 ppm) |
| ${}^{189}$Tl | 189 | 108 | L?-pending | binding_energy | — | 1486.7251 | — | 175986.3349 MeV (-235.4 ppm) |
| ${}^{190}$Tl | 190 | 109 | L?-pending | binding_energy | — | 1494.5466 | — | 176918.0786 MeV (-234.1 ppm) |
| ${}^{191}$Tl | 191 | 110 | L?-pending | binding_energy | — | 1504.5346 | — | 177847.6558 MeV (-232.9 ppm) |
| ${}^{192}$Tl | 192 | 111 | L?-pending | binding_energy | — | 1512.1952 | — | 178779.5604 MeV (-231.7 ppm) |
| ${}^{193}$Tl | 193 | 112 | L?-pending | binding_energy | — | 1521.8715 | — | 179709.4493 MeV (-230.5 ppm) |
| ${}^{194}$Tl | 194 | 113 | L?-pending | binding_energy | — | 1529.4031 | — | 180641.4828 MeV (-229.3 ppm) |
| ${}^{195}$Tl | 195 | 114 | L?-pending | binding_energy | — | 1538.6922 | — | 181571.7589 MeV (-228.2 ppm) |
| ${}^{196}$Tl | 196 | 115 | L?-pending | binding_energy | — | 1546.1048 | — | 182503.9115 MeV (-227.0 ppm) |
| ${}^{197}$Tl | 197 | 116 | L?-pending | binding_energy | — | 1555.0338 | — | 183434.5477 MeV (-225.8 ppm) |
| ${}^{198}$Tl | 198 | 117 | L?-pending | binding_energy | — | 1562.2796 | — | 184366.8671 MeV (-224.7 ppm) |
| ${}^{199}$Tl | 199 | 118 | L?-pending | binding_energy | — | 1570.8816 | — | 185297.8303 MeV (-223.6 ppm) |
| ${}^{200}$Tl | 200 | 119 | L?-pending | binding_energy | — | 1577.9407 | — | 186230.3363 MeV (-222.5 ppm) |
| ${}^{201}$Tl | 201 | 120 | L?-pending | binding_energy | — | 1586.1456 | — | 187161.6966 MeV (-221.3 ppm) |
| ${}^{202}$Tl | 202 | 121 | L?-pending | binding_energy | — | 1593.0166 | — | 188094.3908 MeV (-220.3 ppm) |
| ${}^{203}$Tl | 203 | 122 | L?-pending | binding_energy | — | 1600.8688 | — | 189026.1038 MeV (-219.2 ppm) |
| ${}^{204}$Tl | 204 | 123 | L?-pending | binding_energy | — | 1607.5249 | — | 189959.0129 MeV (-218.1 ppm) |
| ${}^{205}$Tl | 205 | 124 | L?-pending | binding_energy | — | 1615.0709 | — | 190891.0321 MeV (-217.0 ppm) |
| ${}^{206}$Tl | 206 | 125 | L?-pending | binding_energy | — | 1621.5747 | — | 191824.0934 MeV (-216.0 ppm) |
| ${}^{207}$Tl | 207 | 126 | L?-pending | binding_energy | — | 1628.4272 | — | 192756.8062 MeV (-214.9 ppm) |
| ${}^{208}$Tl | 208 | 127 | L?-pending | binding_energy | — | 1632.2142 | — | 193692.5843 MeV (-213.9 ppm) |
| ${}^{209}$Tl | 209 | 128 | L?-pending | binding_energy | — | 1637.1802 | — | 194627.1835 MeV (-212.9 ppm) |
| ${}^{210}$Tl | 210 | 129 | L?-pending | binding_energy | — | 1640.8537 | — | 195563.0752 MeV (-211.9 ppm) |
| ${}^{211}$Tl | 211 | 130 | L?-pending | binding_energy | — | 1645.7560 | — | 196497.7381 MeV (-210.8 ppm) |
| ${}^{212}$Tl | 212 | 131 | L?-pending | binding_energy | — | 1649.3600 | — | 197433.6993 MeV (-210.2 ppm) |
| ${}^{213}$Tl | 213 | 132 | L?-pending | binding_energy | — | 1654.0368 | — | 198368.5876 MeV (-208.9 ppm) |
| ${}^{214}$Tl | 214 | 133 | L?-pending | binding_energy | — | 1657.4300 | — | 199304.7596 MeV (-207.9 ppm) |
| ${}^{215}$Tl | 215 | 134 | L?-pending | binding_energy | — | 1661.9500 | — | 200239.8048 MeV (-207.0 ppm) |
| ${}^{216}$Tl | 216 | 135 | L?-pending | binding_energy | — | 1665.1440 | — | 201176.1760 MeV (-205.8 ppm) |
| ${}^{217}$Tl | 217 | 136 | L?-pending | binding_energy | — | 1669.3810 | — | 202111.5042 MeV (-204.7 ppm) |
| ${}^{218}$Tl | 218 | 137 | L?-pending | binding_energy | — | 1672.4960 | — | 203047.9544 MeV (-204.2 ppm) |

### Lead (Z = 82)

_0 of 43 isotopes with a framework prediction; 43 of 43 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{178}$Pb | 178 | 96 | L?-pending | binding_energy | — | 1368.9688 | — | 165767.5809 MeV (-253.0 ppm) |
| ${}^{179}$Pb | 179 | 97 | L?-pending | binding_energy | — | 1378.5619 | — | 166697.5530 MeV (-251.5 ppm) |
| ${}^{180}$Pb | 180 | 98 | L?-pending | binding_energy | — | 1390.6259 | — | 167625.0541 MeV (-250.2 ppm) |
| ${}^{181}$Pb | 181 | 99 | L?-pending | binding_energy | — | 1399.8667 | — | 168555.3785 MeV (-248.8 ppm) |
| ${}^{182}$Pb | 182 | 100 | L?-pending | binding_energy | — | 1411.6520 | — | 169483.1584 MeV (-247.4 ppm) |
| ${}^{183}$Pb | 183 | 101 | L?-pending | binding_energy | — | 1420.4788 | — | 170413.8968 MeV (-246.1 ppm) |
| ${}^{184}$Pb | 184 | 102 | L?-pending | binding_energy | — | 1432.0217 | — | 171341.9191 MeV (-244.7 ppm) |
| ${}^{185}$Pb | 185 | 103 | L?-pending | binding_energy | — | 1440.5826 | — | 172272.9233 MeV (-243.4 ppm) |
| ${}^{186}$Pb | 186 | 104 | L?-pending | binding_energy | — | 1451.7936 | — | 173201.2775 MeV (-242.1 ppm) |
| ${}^{187}$Pb | 187 | 105 | L?-pending | binding_energy | — | 1460.1710 | — | 174132.4653 MeV (-240.8 ppm) |
| ${}^{188}$Pb | 188 | 106 | L?-pending | binding_energy | — | 1471.0664 | — | 175061.1351 MeV (-239.5 ppm) |
| ${}^{189}$Pb | 189 | 107 | L?-pending | binding_energy | — | 1479.1707 | — | 175992.5960 MeV (-238.3 ppm) |
| ${}^{190}$Pb | 190 | 108 | L?-pending | binding_energy | — | 1489.8146 | — | 176921.5173 MeV (-237.0 ppm) |
| ${}^{191}$Pb | 191 | 109 | L?-pending | binding_energy | — | 1497.7605 | — | 177853.1365 MeV (-235.8 ppm) |
| ${}^{192}$Pb | 192 | 110 | L?-pending | binding_energy | — | 1508.0925 | — | 178782.3698 MeV (-234.6 ppm) |
| ${}^{193}$Pb | 193 | 111 | L?-pending | binding_energy | — | 1515.8412 | — | 179714.1862 MeV (-233.4 ppm) |
| ${}^{194}$Pb | 194 | 112 | L?-pending | binding_energy | — | 1525.8911 | — | 180643.7015 MeV (-232.2 ppm) |
| ${}^{195}$Pb | 195 | 113 | L?-pending | binding_energy | — | 1533.4926 | — | 181575.6652 MeV (-231.0 ppm) |
| ${}^{196}$Pb | 196 | 114 | L?-pending | binding_energy | — | 1543.1741 | — | 182505.5488 MeV (-229.8 ppm) |
| ${}^{197}$Pb | 197 | 115 | L?-pending | binding_energy | — | 1550.6426 | — | 183437.6456 MeV (-228.6 ppm) |
| ${}^{198}$Pb | 198 | 116 | L?-pending | binding_energy | — | 1560.0360 | — | 184367.8174 MeV (-227.5 ppm) |
| ${}^{199}$Pb | 199 | 117 | L?-pending | binding_energy | — | 1567.2716 | — | 185300.1469 MeV (-226.3 ppm) |
| ${}^{200}$Pb | 200 | 118 | L?-pending | binding_energy | — | 1576.3620 | — | 186230.6217 MeV (-225.2 ppm) |
| ${}^{201}$Pb | 201 | 119 | L?-pending | binding_energy | — | 1583.4535 | — | 187163.0954 MeV (-224.1 ppm) |
| ${}^{202}$Pb | 202 | 120 | L?-pending | binding_energy | — | 1592.1944 | — | 188093.9197 MeV (-223.0 ppm) |
| ${}^{203}$Pb | 203 | 121 | L?-pending | binding_energy | — | 1599.1116 | — | 189026.5677 MeV (-221.9 ppm) |
| ${}^{204}$Pb | 204 | 122 | L?-pending | binding_energy | — | 1607.5063 | — | 189957.7382 MeV (-220.8 ppm) |
| ${}^{205}$Pb | 205 | 123 | L?-pending | binding_energy | — | 1614.2379 | — | 190890.5717 MeV (-219.7 ppm) |
| ${}^{206}$Pb | 206 | 124 | L?-pending | binding_energy | — | 1622.3246 | — | 191822.0502 MeV (-218.6 ppm) |
| ${}^{207}$Pb | 207 | 125 | L?-pending | binding_energy | — | 1629.0623 | — | 192754.8777 MeV (-217.6 ppm) |
| ${}^{208}$Pb | 208 | 126 | L?-pending | binding_energy | — | 1636.4302 | — | 193687.0750 MeV (-216.5 ppm) |
| ${}^{209}$Pb | 209 | 127 | L?-pending | binding_energy | — | 1640.3676 | — | 194622.7028 MeV (-215.5 ppm) |
| ${}^{210}$Pb | 210 | 128 | L?-pending | binding_energy | — | 1645.5528 | — | 195557.0828 MeV (-214.5 ppm) |
| ${}^{211}$Pb | 211 | 129 | L?-pending | binding_energy | — | 1649.3887 | — | 196492.8121 MeV (-213.5 ppm) |
| ${}^{212}$Pb | 212 | 130 | L?-pending | binding_energy | — | 1654.5159 | — | 197427.2500 MeV (-212.4 ppm) |
| ${}^{213}$Pb | 213 | 131 | L?-pending | binding_energy | — | 1658.2419 | — | 198363.0892 MeV (-211.4 ppm) |
| ${}^{214}$Pb | 214 | 132 | L?-pending | binding_energy | — | 1663.2926 | — | 199297.6037 MeV (-210.5 ppm) |
| ${}^{215}$Pb | 215 | 133 | L?-pending | binding_energy | — | 1666.8387 | — | 200233.6228 MeV (-209.5 ppm) |
| ${}^{216}$Pb | 216 | 134 | L?-pending | binding_energy | — | 1671.8400 | — | 201168.1867 MeV (-209.0 ppm) |
| ${}^{217}$Pb | 217 | 135 | L?-pending | binding_energy | — | 1675.0230 | — | 202104.5688 MeV (-207.3 ppm) |
| ${}^{218}$Pb | 218 | 136 | L?-pending | binding_energy | — | 1679.6900 | — | 203039.4670 MeV (-206.2 ppm) |
| ${}^{219}$Pb | 219 | 137 | L?-pending | binding_energy | — | 1682.7960 | — | 203975.9262 MeV (-205.4 ppm) |
| ${}^{220}$Pb | 220 | 138 | L?-pending | binding_energy | — | 1687.4000 | — | 204910.8874 MeV (-204.7 ppm) |

### Bismuth (Z = 83)

_0 of 41 isotopes with a framework prediction; 41 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{184}$Bi | 184 | 101 | L?-pending | binding_energy | — | 1419.0080 | — | 171353.6394 MeV (-248.1 ppm) |
| ${}^{185}$Bi | 185 | 102 | L?-pending | binding_energy | — | 1430.4200 | — | 172281.7926 MeV (-245.9 ppm) |
| ${}^{186}$Bi | 186 | 103 | L?-pending | binding_energy | — | 1439.4759 | — | 173212.3019 MeV (-245.0 ppm) |
| ${}^{187}$Bi | 187 | 104 | L?-pending | binding_energy | — | 1450.7850 | — | 174140.5580 MeV (-243.7 ppm) |
| ${}^{188}$Bi | 188 | 105 | L?-pending | binding_energy | — | 1459.6678 | — | 175071.2404 MeV (-242.4 ppm) |
| ${}^{189}$Bi | 189 | 106 | L?-pending | binding_energy | — | 1470.6090 | — | 175999.8644 MeV (-241.2 ppm) |
| ${}^{190}$Bi | 190 | 107 | L?-pending | binding_energy | — | 1479.2115 | — | 176930.8270 MeV (-239.9 ppm) |
| ${}^{191}$Bi | 191 | 108 | L?-pending | binding_energy | — | 1489.9263 | — | 177859.6774 MeV (-238.7 ppm) |
| ${}^{192}$Bi | 192 | 109 | L?-pending | binding_energy | — | 1498.2928 | — | 178790.8761 MeV (-237.4 ppm) |
| ${}^{193}$Bi | 193 | 110 | L?-pending | binding_energy | — | 1508.7142 | — | 179720.0199 MeV (-236.2 ppm) |
| ${}^{194}$Bi | 194 | 111 | L?-pending | binding_energy | — | 1516.9239 | — | 180651.3753 MeV (-235.0 ppm) |
| ${}^{195}$Bi | 195 | 112 | L?-pending | binding_energy | — | 1526.9978 | — | 181580.8667 MeV (-233.8 ppm) |
| ${}^{196}$Bi | 196 | 113 | L?-pending | binding_energy | — | 1535.0526 | — | 182512.3771 MeV (-232.6 ppm) |
| ${}^{197}$Bi | 197 | 114 | L?-pending | binding_energy | — | 1544.8021 | — | 183442.1928 MeV (-231.4 ppm) |
| ${}^{198}$Bi | 198 | 115 | L?-pending | binding_energy | — | 1552.5600 | — | 184374.0000 MeV (-230.2 ppm) |
| ${}^{199}$Bi | 199 | 116 | L?-pending | binding_energy | — | 1562.0551 | — | 185304.0701 MeV (-229.1 ppm) |
| ${}^{200}$Bi | 200 | 117 | L?-pending | binding_energy | — | 1569.6994 | — | 186235.9910 MeV (-227.9 ppm) |
| ${}^{201}$Bi | 201 | 118 | L?-pending | binding_energy | — | 1578.8291 | — | 187166.4264 MeV (-226.8 ppm) |
| ${}^{202}$Bi | 202 | 119 | L?-pending | binding_energy | — | 1586.2223 | — | 188098.5984 MeV (-225.7 ppm) |
| ${}^{203}$Bi | 203 | 120 | L?-pending | binding_energy | — | 1595.0677 | — | 189029.3183 MeV (-224.6 ppm) |
| ${}^{204}$Bi | 204 | 121 | L?-pending | binding_energy | — | 1602.2600 | — | 189961.6911 MeV (-223.5 ppm) |
| ${}^{205}$Bi | 205 | 122 | L?-pending | binding_energy | — | 1610.7510 | — | 190892.7653 MeV (-222.4 ppm) |
| ${}^{206}$Bi | 206 | 123 | L?-pending | binding_energy | — | 1617.7849 | — | 191825.2966 MeV (-221.3 ppm) |
| ${}^{207}$Bi | 207 | 124 | L?-pending | binding_energy | — | 1625.8826 | — | 192756.7641 MeV (-220.2 ppm) |
| ${}^{208}$Bi | 208 | 125 | L?-pending | binding_energy | — | 1632.7695 | — | 193689.4423 MeV (-219.2 ppm) |
| ${}^{209}$Bi | 209 | 126 | L?-pending | binding_energy | — | 1640.2293 | — | 194621.5478 MeV (-218.1 ppm) |
| ${}^{210}$Bi | 210 | 127 | L?-pending | binding_energy | — | 1644.8339 | — | 195556.5083 MeV (-217.1 ppm) |
| ${}^{211}$Bi | 211 | 128 | L?-pending | binding_energy | — | 1649.9724 | — | 196490.9350 MeV (-216.1 ppm) |
| ${}^{212}$Bi | 212 | 129 | L?-pending | binding_energy | — | 1654.3026 | — | 197426.1700 MeV (-215.0 ppm) |
| ${}^{213}$Bi | 213 | 130 | L?-pending | binding_energy | — | 1659.4876 | — | 198360.5502 MeV (-214.0 ppm) |
| ${}^{214}$Bi | 214 | 131 | L?-pending | binding_energy | — | 1663.5280 | — | 199296.0749 MeV (-213.0 ppm) |
| ${}^{215}$Bi | 215 | 132 | L?-pending | binding_energy | — | 1668.7693 | — | 200230.3988 MeV (-212.0 ppm) |
| ${}^{216}$Bi | 216 | 133 | L?-pending | binding_energy | — | 1672.5959 | — | 201166.1374 MeV (-211.0 ppm) |
| ${}^{217}$Bi | 217 | 134 | L?-pending | binding_energy | — | 1677.8113 | — | 202100.4873 MeV (-210.1 ppm) |
| ${}^{218}$Bi | 218 | 135 | L?-pending | binding_energy | — | 1681.3965 | — | 203036.4672 MeV (-209.1 ppm) |
| ${}^{219}$Bi | 219 | 136 | L?-pending | binding_energy | — | 1686.3000 | — | 203971.1289 MeV (-207.8 ppm) |
| ${}^{220}$Bi | 220 | 137 | L?-pending | binding_energy | — | 1689.8200 | — | 204907.1741 MeV (-207.3 ppm) |
| ${}^{221}$Bi | 221 | 138 | L?-pending | binding_energy | — | 1694.6280 | — | 205841.9313 MeV (-206.3 ppm) |
| ${}^{222}$Bi | 222 | 139 | L?-pending | binding_energy | — | 1697.8560 | — | 206778.2684 MeV (-204.9 ppm) |
| ${}^{223}$Bi | 223 | 140 | L?-pending | binding_energy | — | 1702.8280 | — | 207712.8616 MeV (-204.9 ppm) |
| ${}^{224}$Bi | 224 | 141 | L?-pending | binding_energy | — | 1705.9840 | — | 208649.2708 MeV (-203.5 ppm) |

### Polonium (Z = 84)

_0 of 42 isotopes with a framework prediction; 42 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{186}$Po | 186 | 102 | L?-pending | binding_energy | — | 1431.4465 | — | 173219.0380 MeV (-248.0 ppm) |
| ${}^{187}$Po | 187 | 103 | L?-pending | binding_energy | — | 1440.7955 | — | 174149.2541 MeV (-246.7 ppm) |
| ${}^{188}$Po | 188 | 104 | L?-pending | binding_energy | — | 1452.2350 | — | 175077.3798 MeV (-245.4 ppm) |
| ${}^{189}$Po | 189 | 105 | L?-pending | binding_energy | — | 1461.1840 | — | 176007.9960 MeV (-244.1 ppm) |
| ${}^{190}$Po | 190 | 106 | L?-pending | binding_energy | — | 1472.3960 | — | 176936.3492 MeV (-242.8 ppm) |
| ${}^{191}$Po | 191 | 107 | L?-pending | binding_energy | — | 1480.9733 | — | 177867.3370 MeV (-241.5 ppm) |
| ${}^{192}$Po | 192 | 108 | L?-pending | binding_energy | — | 1492.0424 | — | 178795.8332 MeV (-240.3 ppm) |
| ${}^{193}$Po | 193 | 109 | L?-pending | binding_energy | — | 1500.3725 | — | 179727.0682 MeV (-239.0 ppm) |
| ${}^{194}$Po | 194 | 110 | L?-pending | binding_energy | — | 1511.1232 | — | 180655.8828 MeV (-237.8 ppm) |
| ${}^{195}$Po | 195 | 111 | L?-pending | binding_energy | — | 1519.3065 | — | 181587.2646 MeV (-236.6 ppm) |
| ${}^{196}$Po | 196 | 112 | L?-pending | binding_energy | — | 1529.7299 | — | 182516.4064 MeV (-235.4 ppm) |
| ${}^{197}$Po | 197 | 113 | L?-pending | binding_energy | — | 1537.7256 | — | 183447.9759 MeV (-234.2 ppm) |
| ${}^{198}$Po | 198 | 114 | L?-pending | binding_energy | — | 1547.8771 | — | 184377.3896 MeV (-233.0 ppm) |
| ${}^{199}$Po | 199 | 115 | L?-pending | binding_energy | — | 1555.7140 | — | 185309.1179 MeV (-231.8 ppm) |
| ${}^{200}$Po | 200 | 116 | L?-pending | binding_energy | — | 1565.4881 | — | 186238.9089 MeV (-230.7 ppm) |
| ${}^{201}$Po | 201 | 117 | L?-pending | binding_energy | — | 1573.1389 | — | 187170.8233 MeV (-229.5 ppm) |
| ${}^{202}$Po | 202 | 118 | L?-pending | binding_energy | — | 1582.6307 | — | 188100.8967 MeV (-228.4 ppm) |
| ${}^{203}$Po | 203 | 119 | L?-pending | binding_energy | — | 1590.0712 | — | 189033.0214 MeV (-227.3 ppm) |
| ${}^{204}$Po | 204 | 120 | L?-pending | binding_energy | — | 1599.1728 | — | 189963.4850 MeV (-226.2 ppm) |
| ${}^{205}$Po | 205 | 121 | L?-pending | binding_energy | — | 1606.4244 | — | 190895.7985 MeV (-225.1 ppm) |
| ${}^{206}$Po | 206 | 122 | L?-pending | binding_energy | — | 1615.1630 | — | 191826.6251 MeV (-224.0 ppm) |
| ${}^{207}$Po | 207 | 123 | L?-pending | binding_energy | — | 1622.1914 | — | 192759.1619 MeV (-222.9 ppm) |
| ${}^{208}$Po | 208 | 124 | L?-pending | binding_energy | — | 1630.5862 | — | 193690.3323 MeV (-221.8 ppm) |
| ${}^{209}$Po | 209 | 125 | L?-pending | binding_energy | — | 1637.5543 | — | 194622.9294 MeV (-220.7 ppm) |
| ${}^{210}$Po | 210 | 126 | L?-pending | binding_energy | — | 1645.2127 | — | 195554.8362 MeV (-219.7 ppm) |
| ${}^{211}$Po | 211 | 127 | L?-pending | binding_energy | — | 1649.7635 | — | 196489.8506 MeV (-218.7 ppm) |
| ${}^{212}$Po | 212 | 128 | L?-pending | binding_energy | — | 1655.7717 | — | 197423.4076 MeV (-217.6 ppm) |
| ${}^{213}$Po | 213 | 129 | L?-pending | binding_energy | — | 1660.1271 | — | 198358.6173 MeV (-216.6 ppm) |
| ${}^{214}$Po | 214 | 130 | L?-pending | binding_energy | — | 1666.0149 | — | 199292.2947 MeV (-215.6 ppm) |
| ${}^{215}$Po | 215 | 131 | L?-pending | binding_energy | — | 1670.1580 | — | 200227.7168 MeV (-214.6 ppm) |
| ${}^{216}$Po | 216 | 132 | L?-pending | binding_energy | — | 1675.9052 | — | 201161.5348 MeV (-213.6 ppm) |
| ${}^{217}$Po | 217 | 133 | L?-pending | binding_energy | — | 1679.8754 | — | 202097.1298 MeV (-212.6 ppm) |
| ${}^{218}$Po | 218 | 134 | L?-pending | binding_energy | — | 1685.4735 | — | 203031.0968 MeV (-211.6 ppm) |
| ${}^{219}$Po | 219 | 135 | L?-pending | binding_energy | — | 1689.2201 | — | 203966.9154 MeV (-210.6 ppm) |
| ${}^{220}$Po | 220 | 136 | L?-pending | binding_energy | — | 1694.7094 | — | 204900.9914 MeV (-209.7 ppm) |
| ${}^{221}$Po | 221 | 137 | L?-pending | binding_energy | — | 1698.2704 | — | 205836.9955 MeV (-208.7 ppm) |
| ${}^{222}$Po | 222 | 138 | L?-pending | binding_energy | — | 1703.6292 | — | 206771.2019 MeV (-207.8 ppm) |
| ${}^{223}$Po | 223 | 139 | L?-pending | binding_energy | — | 1707.0650 | — | 207707.3313 MeV (-206.7 ppm) |
| ${}^{224}$Po | 224 | 140 | L?-pending | binding_energy | — | 1712.2560 | — | 208641.7055 MeV (-205.5 ppm) |
| ${}^{225}$Po | 225 | 141 | L?-pending | binding_energy | — | 1715.8500 | — | 209577.6767 MeV (-205.5 ppm) |
| ${}^{226}$Po | 226 | 142 | L?-pending | binding_energy | — | 1720.7640 | — | 210512.3278 MeV (-203.7 ppm) |
| ${}^{227}$Po | 227 | 143 | L?-pending | binding_energy | — | 1724.2920 | — | 211448.3650 MeV (-203.7 ppm) |

### Astatine (Z = 85)

_0 of 39 isotopes with a framework prediction; 39 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{191}$At | 191 | 106 | L?-pending | binding_energy | — | 1471.2584 | — | 177875.7587 MeV (-244.4 ppm) |
| ${}^{192}$At | 192 | 107 | L?-pending | binding_energy | — | 1480.2678 | — | 178806.3144 MeV (-243.1 ppm) |
| ${}^{193}$At | 193 | 108 | L?-pending | binding_energy | — | 1491.3322 | — | 179734.8152 MeV (-241.8 ppm) |
| ${}^{194}$At | 194 | 109 | L?-pending | binding_energy | — | 1500.0527 | — | 180665.6599 MeV (-240.6 ppm) |
| ${}^{195}$At | 195 | 110 | L?-pending | binding_energy | — | 1510.8778 | — | 181594.4000 MeV (-239.4 ppm) |
| ${}^{196}$At | 196 | 111 | L?-pending | binding_energy | — | 1519.3920 | — | 182525.4510 MeV (-238.2 ppm) |
| ${}^{197}$At | 197 | 112 | L?-pending | binding_energy | — | 1529.9054 | — | 183454.5027 MeV (-237.0 ppm) |
| ${}^{198}$At | 198 | 113 | L?-pending | binding_energy | — | 1538.3302 | — | 184385.6431 MeV (-235.8 ppm) |
| ${}^{199}$At | 199 | 114 | L?-pending | binding_energy | — | 1548.5162 | — | 185315.0224 MeV (-234.6 ppm) |
| ${}^{200}$At | 200 | 115 | L?-pending | binding_energy | — | 1556.7520 | — | 186246.3517 MeV (-233.4 ppm) |
| ${}^{201}$At | 201 | 116 | L?-pending | binding_energy | — | 1566.6249 | — | 187176.0440 MeV (-232.2 ppm) |
| ${}^{202}$At | 202 | 117 | L?-pending | binding_energy | — | 1574.5019 | — | 188107.7322 MeV (-231.1 ppm) |
| ${}^{203}$At | 203 | 118 | L?-pending | binding_energy | — | 1584.1407 | — | 189037.6586 MeV (-230.0 ppm) |
| ${}^{204}$At | 204 | 119 | L?-pending | binding_energy | — | 1591.9246 | — | 189969.4398 MeV (-228.8 ppm) |
| ${}^{205}$At | 205 | 120 | L?-pending | binding_energy | — | 1601.1052 | — | 190899.8244 MeV (-227.7 ppm) |
| ${}^{206}$At | 206 | 121 | L?-pending | binding_energy | — | 1608.6314 | — | 191831.8634 MeV (-226.6 ppm) |
| ${}^{207}$At | 207 | 122 | L?-pending | binding_energy | — | 1617.4908 | — | 192762.5692 MeV (-225.5 ppm) |
| ${}^{208}$At | 208 | 123 | L?-pending | binding_energy | — | 1624.8046 | — | 193694.8206 MeV (-224.4 ppm) |
| ${}^{209}$At | 209 | 124 | L?-pending | binding_energy | — | 1633.2898 | — | 194625.9006 MeV (-223.4 ppm) |
| ${}^{210}$At | 210 | 125 | L?-pending | binding_energy | — | 1640.4494 | — | 195558.3062 MeV (-222.3 ppm) |
| ${}^{211}$At | 211 | 126 | L?-pending | binding_energy | — | 1648.1958 | — | 196490.1249 MeV (-221.3 ppm) |
| ${}^{212}$At | 212 | 127 | L?-pending | binding_energy | — | 1653.2481 | — | 197424.6378 MeV (-220.2 ppm) |
| ${}^{213}$At | 213 | 128 | L?-pending | binding_energy | — | 1659.2708 | — | 198358.1803 MeV (-219.2 ppm) |
| ${}^{214}$At | 214 | 129 | L?-pending | binding_energy | — | 1664.1417 | — | 199292.8746 MeV (-218.1 ppm) |
| ${}^{215}$At | 215 | 130 | L?-pending | binding_energy | — | 1670.0905 | — | 200226.4910 MeV (-217.1 ppm) |
| ${}^{216}$At | 216 | 131 | L?-pending | binding_energy | — | 1674.6485 | — | 201161.4981 MeV (-216.1 ppm) |
| ${}^{217}$At | 217 | 132 | L?-pending | binding_energy | — | 1680.5819 | — | 202095.1299 MeV (-215.1 ppm) |
| ${}^{218}$At | 218 | 133 | L?-pending | binding_energy | — | 1684.9476 | — | 203030.3294 MeV (-214.1 ppm) |
| ${}^{219}$At | 219 | 134 | L?-pending | binding_energy | — | 1690.7231 | — | 203964.1191 MeV (-213.2 ppm) |
| ${}^{220}$At | 220 | 135 | L?-pending | binding_energy | — | 1694.8147 | — | 204899.5927 MeV (-212.2 ppm) |
| ${}^{221}$At | 221 | 136 | L?-pending | binding_energy | — | 1700.4791 | — | 205833.4935 MeV (-211.2 ppm) |
| ${}^{222}$At | 222 | 137 | L?-pending | binding_energy | — | 1704.3801 | — | 206769.1577 MeV (-210.3 ppm) |
| ${}^{223}$At | 223 | 138 | L?-pending | binding_energy | — | 1709.9764 | — | 207703.1265 MeV (-209.3 ppm) |
| ${}^{224}$At | 224 | 139 | L?-pending | binding_energy | — | 1713.7647 | — | 208638.9034 MeV (-208.4 ppm) |
| ${}^{225}$At | 225 | 140 | L?-pending | binding_energy | — | 1719.2250 | — | 209573.0083 MeV (-207.4 ppm) |
| ${}^{226}$At | 226 | 141 | L?-pending | binding_energy | — | 1723.0240 | — | 210508.7745 MeV (-206.8 ppm) |
| ${}^{227}$At | 227 | 142 | L?-pending | binding_energy | — | 1728.1510 | — | 211443.2127 MeV (-205.1 ppm) |
| ${}^{228}$At | 228 | 143 | L?-pending | binding_energy | — | 1731.8880 | — | 212379.0409 MeV (-204.8 ppm) |
| ${}^{229}$At | 229 | 144 | L?-pending | binding_energy | — | 1736.9650 | — | 213313.5291 MeV (-203.9 ppm) |

### Radon (Z = 86)

_0 of 39 isotopes with a framework prediction; 39 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{193}$Rn | 193 | 107 | L?-pending | binding_energy | — | 1481.4396 | — | 179743.4145 MeV (-244.7 ppm) |
| ${}^{194}$Rn | 194 | 108 | L?-pending | binding_energy | — | 1492.8292 | — | 180671.5900 MeV (-243.4 ppm) |
| ${}^{195}$Rn | 195 | 109 | L?-pending | binding_energy | — | 1501.5749 | — | 181602.4096 MeV (-242.2 ppm) |
| ${}^{196}$Rn | 196 | 110 | L?-pending | binding_energy | — | 1512.7213 | — | 182530.8283 MeV (-240.9 ppm) |
| ${}^{197}$Rn | 197 | 111 | L?-pending | binding_energy | — | 1521.2574 | — | 183461.8574 MeV (-239.7 ppm) |
| ${}^{198}$Rn | 198 | 112 | L?-pending | binding_energy | — | 1532.0695 | — | 184390.6106 MeV (-238.5 ppm) |
| ${}^{199}$Rn | 199 | 113 | L?-pending | binding_energy | — | 1540.4703 | — | 185321.7749 MeV (-237.3 ppm) |
| ${}^{200}$Rn | 200 | 114 | L?-pending | binding_energy | — | 1550.9822 | — | 186250.8282 MeV (-236.1 ppm) |
| ${}^{201}$Rn | 201 | 115 | L?-pending | binding_energy | — | 1559.1605 | — | 187182.2151 MeV (-235.0 ppm) |
| ${}^{202}$Rn | 202 | 116 | L?-pending | binding_energy | — | 1569.3990 | — | 188111.5418 MeV (-233.8 ppm) |
| ${}^{203}$Rn | 203 | 117 | L?-pending | binding_energy | — | 1577.3798 | — | 189043.1262 MeV (-232.7 ppm) |
| ${}^{204}$Rn | 204 | 118 | L?-pending | binding_energy | — | 1587.2372 | — | 189972.8340 MeV (-231.5 ppm) |
| ${}^{205}$Rn | 205 | 119 | L?-pending | binding_energy | — | 1595.0481 | — | 190904.5882 MeV (-230.4 ppm) |
| ${}^{206}$Rn | 206 | 120 | L?-pending | binding_energy | — | 1604.5426 | — | 191834.6589 MeV (-229.3 ppm) |
| ${}^{207}$Rn | 207 | 121 | L?-pending | binding_energy | — | 1612.1157 | — | 192766.6509 MeV (-228.2 ppm) |
| ${}^{208}$Rn | 208 | 122 | L?-pending | binding_energy | — | 1621.2077 | — | 193697.1242 MeV (-227.1 ppm) |
| ${}^{209}$Rn | 209 | 123 | L?-pending | binding_energy | — | 1628.5647 | — | 194629.3324 MeV (-226.0 ppm) |
| ${}^{210}$Rn | 210 | 124 | L?-pending | binding_energy | — | 1637.2997 | — | 195560.1625 MeV (-224.9 ppm) |
| ${}^{211}$Rn | 211 | 125 | L?-pending | binding_energy | — | 1644.5216 | — | 196492.5058 MeV (-223.8 ppm) |
| ${}^{212}$Rn | 212 | 126 | L?-pending | binding_energy | — | 1652.4968 | — | 197424.0958 MeV (-222.8 ppm) |
| ${}^{213}$Rn | 213 | 127 | L?-pending | binding_energy | — | 1657.6049 | — | 198358.5529 MeV (-221.7 ppm) |
| ${}^{214}$Rn | 214 | 128 | L?-pending | binding_energy | — | 1664.2999 | — | 199291.4231 MeV (-220.7 ppm) |
| ${}^{215}$Rn | 215 | 129 | L?-pending | binding_energy | — | 1669.2205 | — | 200226.0676 MeV (-219.7 ppm) |
| ${}^{216}$Rn | 216 | 130 | L?-pending | binding_energy | — | 1675.8695 | — | 201158.9838 MeV (-218.7 ppm) |
| ${}^{217}$Rn | 217 | 131 | L?-pending | binding_energy | — | 1680.5356 | — | 202093.8829 MeV (-217.7 ppm) |
| ${}^{218}$Rn | 218 | 132 | L?-pending | binding_energy | — | 1687.0481 | — | 203026.9356 MeV (-216.7 ppm) |
| ${}^{219}$Rn | 219 | 133 | L?-pending | binding_energy | — | 1691.5075 | — | 203962.0414 MeV (-215.7 ppm) |
| ${}^{220}$Rn | 220 | 134 | L?-pending | binding_energy | — | 1697.7961 | — | 204895.3179 MeV (-214.7 ppm) |
| ${}^{221}$Rn | 221 | 135 | L?-pending | binding_energy | — | 1702.0081 | — | 205830.6712 MeV (-213.7 ppm) |
| ${}^{222}$Rn | 222 | 136 | L?-pending | binding_energy | — | 1708.1788 | — | 206764.0656 MeV (-212.7 ppm) |
| ${}^{223}$Rn | 223 | 137 | L?-pending | binding_energy | — | 1712.2324 | — | 207699.5773 MeV (-211.8 ppm) |
| ${}^{224}$Rn | 224 | 138 | L?-pending | binding_energy | — | 1718.2483 | — | 208633.1265 MeV (-210.8 ppm) |
| ${}^{225}$Rn | 225 | 139 | L?-pending | binding_energy | — | 1722.2306 | — | 209568.7094 MeV (-209.9 ppm) |
| ${}^{226}$Rn | 226 | 140 | L?-pending | binding_energy | — | 1728.0888 | — | 210502.4163 MeV (-209.0 ppm) |
| ${}^{227}$Rn | 227 | 141 | L?-pending | binding_energy | — | 1732.0215 | — | 211438.0488 MeV (-208.0 ppm) |
| ${}^{228}$Rn | 228 | 142 | L?-pending | binding_energy | — | 1737.7352 | — | 212371.9003 MeV (-207.1 ppm) |
| ${}^{229}$Rn | 229 | 143 | L?-pending | binding_energy | — | 1741.6876 | — | 213307.5131 MeV (-206.2 ppm) |
| ${}^{230}$Rn | 230 | 144 | L?-pending | binding_energy | — | 1746.8500 | — | 214241.9159 MeV (-204.9 ppm) |
| ${}^{231}$Rn | 231 | 145 | L?-pending | binding_energy | — | 1750.7490 | — | 215177.5821 MeV (-204.9 ppm) |

### Francium (Z = 87)

_0 of 37 isotopes with a framework prediction; 37 of 37 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{197}$Fr | 197 | 110 | L?-pending | binding_energy | — | 1511.7315 | — | 183470.0900 MeV (-242.5 ppm) |
| ${}^{198}$Fr | 198 | 111 | L?-pending | binding_energy | — | 1520.4791 | — | 184400.9076 MeV (-241.3 ppm) |
| ${}^{199}$Fr | 199 | 112 | L?-pending | binding_energy | — | 1531.3567 | — | 185329.5951 MeV (-240.1 ppm) |
| ${}^{200}$Fr | 200 | 113 | L?-pending | binding_energy | — | 1540.0658 | — | 186260.4512 MeV (-238.9 ppm) |
| ${}^{201}$Fr | 201 | 114 | L?-pending | binding_energy | — | 1550.6822 | — | 187189.4001 MeV (-237.7 ppm) |
| ${}^{202}$Fr | 202 | 115 | L?-pending | binding_energy | — | 1559.2405 | — | 188120.4069 MeV (-236.5 ppm) |
| ${}^{203}$Fr | 203 | 116 | L?-pending | binding_energy | — | 1569.5370 | — | 189049.6756 MeV (-235.4 ppm) |
| ${}^{204}$Fr | 204 | 117 | L?-pending | binding_energy | — | 1577.8774 | — | 189980.9004 MeV (-234.2 ppm) |
| ${}^{205}$Fr | 205 | 118 | L?-pending | binding_energy | — | 1587.8658 | — | 190910.4771 MeV (-233.1 ppm) |
| ${}^{206}$Fr | 206 | 119 | L?-pending | binding_energy | — | 1595.8742 | — | 191842.0340 MeV (-231.9 ppm) |
| ${}^{207}$Fr | 207 | 120 | L?-pending | binding_energy | — | 1605.5477 | — | 192771.9257 MeV (-230.8 ppm) |
| ${}^{208}$Fr | 208 | 121 | L?-pending | binding_energy | — | 1613.4349 | — | 193703.6036 MeV (-229.7 ppm) |
| ${}^{209}$Fr | 209 | 122 | L?-pending | binding_energy | — | 1622.6234 | — | 194633.9803 MeV (-228.6 ppm) |
| ${}^{210}$Fr | 210 | 123 | L?-pending | binding_energy | — | 1630.2561 | — | 195565.9128 MeV (-227.5 ppm) |
| ${}^{211}$Fr | 211 | 124 | L?-pending | binding_energy | — | 1639.1242 | — | 196496.6098 MeV (-226.4 ppm) |
| ${}^{212}$Fr | 212 | 125 | L?-pending | binding_energy | — | 1646.5712 | — | 197428.7280 MeV (-225.4 ppm) |
| ${}^{213}$Fr | 213 | 126 | L?-pending | binding_energy | — | 1654.6808 | — | 198360.1837 MeV (-224.3 ppm) |
| ${}^{214}$Fr | 214 | 127 | L?-pending | binding_energy | — | 1660.1562 | — | 199294.2734 MeV (-223.3 ppm) |
| ${}^{215}$Fr | 215 | 128 | L?-pending | binding_energy | — | 1666.9511 | — | 200227.0438 MeV (-222.2 ppm) |
| ${}^{216}$Fr | 216 | 129 | L?-pending | binding_energy | — | 1672.3695 | — | 201161.1905 MeV (-221.2 ppm) |
| ${}^{217}$Fr | 217 | 130 | L?-pending | binding_energy | — | 1679.0972 | — | 202094.0280 MeV (-220.2 ppm) |
| ${}^{218}$Fr | 218 | 131 | L?-pending | binding_energy | — | 1684.4237 | — | 203028.2667 MeV (-219.2 ppm) |
| ${}^{219}$Fr | 219 | 132 | L?-pending | binding_energy | — | 1690.9375 | — | 203961.3180 MeV (-218.2 ppm) |
| ${}^{220}$Fr | 220 | 133 | L?-pending | binding_energy | — | 1696.1435 | — | 204895.6773 MeV (-217.2 ppm) |
| ${}^{221}$Fr | 221 | 134 | L?-pending | binding_energy | — | 1702.4198 | — | 205828.9661 MeV (-216.2 ppm) |
| ${}^{222}$Fr | 222 | 135 | L?-pending | binding_energy | — | 1707.3903 | — | 206763.5608 MeV (-215.2 ppm) |
| ${}^{223}$Fr | 223 | 136 | L?-pending | binding_energy | — | 1713.4574 | — | 207697.0589 MeV (-214.2 ppm) |
| ${}^{224}$Fr | 224 | 137 | L?-pending | binding_energy | — | 1718.1624 | — | 208631.9190 MeV (-213.3 ppm) |
| ${}^{225}$Fr | 225 | 138 | L?-pending | binding_energy | — | 1724.1618 | — | 209565.4849 MeV (-212.3 ppm) |
| ${}^{226}$Fr | 226 | 139 | L?-pending | binding_energy | — | 1728.5332 | — | 210500.6787 MeV (-211.4 ppm) |
| ${}^{227}$Fr | 227 | 140 | L?-pending | binding_energy | — | 1734.4426 | — | 211434.3345 MeV (-210.5 ppm) |
| ${}^{228}$Fr | 228 | 141 | L?-pending | binding_energy | — | 1738.8121 | — | 212369.5301 MeV (-209.5 ppm) |
| ${}^{229}$Fr | 229 | 142 | L?-pending | binding_energy | — | 1744.5994 | — | 213303.3080 MeV (-208.6 ppm) |
| ${}^{230}$Fr | 230 | 143 | L?-pending | binding_energy | — | 1748.8522 | — | 214238.6204 MeV (-207.7 ppm) |
| ${}^{231}$Fr | 231 | 144 | L?-pending | binding_energy | — | 1754.3297 | — | 215172.7081 MeV (-206.8 ppm) |
| ${}^{232}$Fr | 232 | 145 | L?-pending | binding_energy | — | 1758.4088 | — | 216108.1942 MeV (-205.9 ppm) |
| ${}^{233}$Fr | 233 | 146 | L?-pending | binding_energy | — | 1763.6329 | — | 217042.5353 MeV (-205.0 ppm) |

### Radium (Z = 88)

_0 of 35 isotopes with a framework prediction; 35 of 35 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{201}$Ra | 201 | 113 | L?-pending | binding_energy | — | 1541.5516 | — | 187197.2373 MeV (-240.4 ppm) |
| ${}^{202}$Ra | 202 | 114 | L?-pending | binding_energy | — | 1552.4848 | — | 188125.8693 MeV (-239.2 ppm) |
| ${}^{203}$Ra | 203 | 115 | L?-pending | binding_energy | — | 1561.0297 | — | 189056.8896 MeV (-238.0 ppm) |
| ${}^{204}$Ra | 204 | 116 | L?-pending | binding_energy | — | 1571.6413 | — | 189985.8432 MeV (-236.9 ppm) |
| ${}^{205}$Ra | 205 | 117 | L?-pending | binding_energy | — | 1579.9698 | — | 190917.0798 MeV (-235.7 ppm) |
| ${}^{206}$Ra | 206 | 118 | L?-pending | binding_energy | — | 1590.2794 | — | 191846.3354 MeV (-234.6 ppm) |
| ${}^{207}$Ra | 207 | 119 | L?-pending | binding_energy | — | 1598.4023 | — | 192777.7777 MeV (-233.5 ppm) |
| ${}^{208}$Ra | 208 | 120 | L?-pending | binding_energy | — | 1608.2597 | — | 193707.4855 MeV (-232.3 ppm) |
| ${}^{209}$Ra | 209 | 121 | L?-pending | binding_energy | — | 1616.2007 | — | 194639.1097 MeV (-231.2 ppm) |
| ${}^{210}$Ra | 210 | 122 | L?-pending | binding_energy | — | 1625.6874 | — | 195569.1881 MeV (-230.1 ppm) |
| ${}^{211}$Ra | 211 | 123 | L?-pending | binding_energy | — | 1633.3697 | — | 196501.0710 MeV (-229.0 ppm) |
| ${}^{212}$Ra | 212 | 124 | L?-pending | binding_energy | — | 1642.4717 | — | 197431.5343 MeV (-228.0 ppm) |
| ${}^{213}$Ra | 213 | 125 | L?-pending | binding_energy | — | 1649.9987 | — | 198363.5725 MeV (-226.9 ppm) |
| ${}^{214}$Ra | 214 | 126 | L?-pending | binding_energy | — | 1658.3228 | — | 199294.8135 MeV (-225.8 ppm) |
| ${}^{215}$Ra | 215 | 127 | L?-pending | binding_energy | — | 1663.9549 | — | 200228.7466 MeV (-224.8 ppm) |
| ${}^{216}$Ra | 216 | 128 | L?-pending | binding_energy | — | 1671.2667 | — | 201161.0000 MeV (-223.7 ppm) |
| ${}^{217}$Ra | 217 | 129 | L?-pending | binding_energy | — | 1676.7399 | — | 202095.0919 MeV (-222.7 ppm) |
| ${}^{218}$Ra | 218 | 130 | L?-pending | binding_energy | — | 1684.0553 | — | 203027.3418 MeV (-221.7 ppm) |
| ${}^{219}$Ra | 219 | 131 | L?-pending | binding_energy | — | 1689.3783 | — | 203961.5840 MeV (-220.7 ppm) |
| ${}^{220}$Ra | 220 | 132 | L?-pending | binding_energy | — | 1696.5713 | — | 204893.9561 MeV (-219.7 ppm) |
| ${}^{221}$Ra | 221 | 133 | L?-pending | binding_energy | — | 1701.9509 | — | 205828.1417 MeV (-218.7 ppm) |
| ${}^{222}$Ra | 222 | 134 | L?-pending | binding_energy | — | 1708.6659 | — | 206760.9919 MeV (-217.7 ppm) |
| ${}^{223}$Ra | 223 | 135 | L?-pending | binding_energy | — | 1713.8242 | — | 207695.3988 MeV (-216.7 ppm) |
| ${}^{224}$Ra | 224 | 136 | L?-pending | binding_energy | — | 1720.3029 | — | 208628.4853 MeV (-215.7 ppm) |
| ${}^{225}$Ra | 225 | 137 | L?-pending | binding_energy | — | 1725.2070 | — | 209563.1463 MeV (-214.8 ppm) |
| ${}^{226}$Ra | 226 | 138 | L?-pending | binding_energy | — | 1731.6038 | — | 210496.3147 MeV (-213.8 ppm) |
| ${}^{227}$Ra | 227 | 139 | L?-pending | binding_energy | — | 1736.1652 | — | 211431.3185 MeV (-212.9 ppm) |
| ${}^{228}$Ra | 228 | 140 | L?-pending | binding_energy | — | 1742.4738 | — | 212364.5751 MeV (-212.0 ppm) |
| ${}^{229}$Ra | 229 | 141 | L?-pending | binding_energy | — | 1746.9233 | — | 213299.6907 MeV (-211.0 ppm) |
| ${}^{230}$Ra | 230 | 142 | L?-pending | binding_energy | — | 1753.0403 | — | 214233.1389 MeV (-210.1 ppm) |
| ${}^{231}$Ra | 231 | 143 | L?-pending | binding_energy | — | 1757.4115 | — | 215168.3330 MeV (-209.2 ppm) |
| ${}^{232}$Ra | 232 | 144 | L?-pending | binding_energy | — | 1763.2023 | — | 216102.1073 MeV (-208.3 ppm) |
| ${}^{233}$Ra | 233 | 145 | L?-pending | binding_energy | — | 1767.4365 | — | 217037.4383 MeV (-207.4 ppm) |
| ${}^{234}$Ra | 234 | 146 | L?-pending | binding_energy | — | 1772.9113 | — | 217971.5287 MeV (-206.5 ppm) |
| ${}^{235}$Ra | 235 | 147 | L?-pending | binding_energy | — | 1776.8350 | — | 218907.1702 MeV (-205.9 ppm) |

### Actinium (Z = 89)

_0 of 33 isotopes with a framework prediction; 33 of 33 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{205}$Ac | 205 | 116 | L?-pending | binding_energy | — | 1570.8846 | — | 190924.8717 MeV (-238.4 ppm) |
| ${}^{206}$Ac | 206 | 117 | L?-pending | binding_energy | — | 1579.5779 | — | 191855.7436 MeV (-237.2 ppm) |
| ${}^{207}$Ac | 207 | 118 | L?-pending | binding_energy | — | 1589.9877 | — | 192784.8990 MeV (-236.1 ppm) |
| ${}^{208}$Ac | 208 | 119 | L?-pending | binding_energy | — | 1598.4444 | — | 193716.0074 MeV (-235.0 ppm) |
| ${}^{209}$Ac | 209 | 120 | L?-pending | binding_energy | — | 1608.4317 | — | 194645.5853 MeV (-233.8 ppm) |
| ${}^{210}$Ac | 210 | 121 | L?-pending | binding_energy | — | 1616.5838 | — | 195576.9984 MeV (-232.7 ppm) |
| ${}^{211}$Ac | 211 | 122 | L?-pending | binding_energy | — | 1626.2757 | — | 196506.8717 MeV (-231.6 ppm) |
| ${}^{212}$Ac | 212 | 123 | L?-pending | binding_energy | — | 1634.1910 | — | 197438.5216 MeV (-230.5 ppm) |
| ${}^{213}$Ac | 213 | 124 | L?-pending | binding_energy | — | 1643.4208 | — | 198368.8569 MeV (-229.5 ppm) |
| ${}^{214}$Ac | 214 | 125 | L?-pending | binding_energy | — | 1651.1999 | — | 199300.6431 MeV (-228.4 ppm) |
| ${}^{215}$Ac | 215 | 126 | L?-pending | binding_energy | — | 1659.6739 | — | 200231.7342 MeV (-227.3 ppm) |
| ${}^{216}$Ac | 216 | 127 | L?-pending | binding_energy | — | 1665.6261 | — | 201165.3472 MeV (-226.3 ppm) |
| ${}^{217}$Ac | 217 | 128 | L?-pending | binding_energy | — | 1673.1448 | — | 202097.3937 MeV (-225.2 ppm) |
| ${}^{218}$Ac | 218 | 129 | L?-pending | binding_energy | — | 1679.0676 | — | 203031.0361 MeV (-224.2 ppm) |
| ${}^{219}$Ac | 219 | 130 | L?-pending | binding_energy | — | 1686.4202 | — | 203963.2487 MeV (-223.2 ppm) |
| ${}^{220}$Ac | 220 | 131 | L?-pending | binding_energy | — | 1692.3173 | — | 204896.9167 MeV (-222.2 ppm) |
| ${}^{221}$Ac | 221 | 132 | L?-pending | binding_energy | — | 1699.6014 | — | 205829.1979 MeV (-221.2 ppm) |
| ${}^{222}$Ac | 222 | 133 | L?-pending | binding_energy | — | 1705.5819 | — | 206762.7825 MeV (-220.2 ppm) |
| ${}^{223}$Ac | 223 | 134 | L?-pending | binding_energy | — | 1712.4500 | — | 207695.4796 MeV (-219.2 ppm) |
| ${}^{224}$Ac | 224 | 135 | L?-pending | binding_energy | — | 1718.1122 | — | 208629.3826 MeV (-218.2 ppm) |
| ${}^{225}$Ac | 225 | 136 | L?-pending | binding_energy | — | 1724.7804 | — | 209562.2796 MeV (-217.2 ppm) |
| ${}^{226}$Ac | 226 | 137 | L?-pending | binding_energy | — | 1730.1798 | — | 210496.4454 MeV (-216.3 ppm) |
| ${}^{227}$Ac | 227 | 138 | L?-pending | binding_energy | — | 1736.7108 | — | 211429.4796 MeV (-215.3 ppm) |
| ${}^{228}$Ac | 228 | 139 | L?-pending | binding_energy | — | 1741.7370 | — | 212364.0186 MeV (-214.4 ppm) |
| ${}^{229}$Ac | 229 | 140 | L?-pending | binding_energy | — | 1748.0130 | — | 213297.3077 MeV (-213.4 ppm) |
| ${}^{230}$Ac | 230 | 141 | L?-pending | binding_energy | — | 1752.9359 | — | 214231.9500 MeV (-212.5 ppm) |
| ${}^{231}$Ac | 231 | 142 | L?-pending | binding_energy | — | 1759.0827 | — | 215165.3684 MeV (-211.6 ppm) |
| ${}^{232}$Ac | 232 | 143 | L?-pending | binding_energy | — | 1763.7625 | — | 216100.2538 MeV (-210.7 ppm) |
| ${}^{233}$Ac | 233 | 144 | L?-pending | binding_energy | — | 1769.6802 | — | 217033.9013 MeV (-209.8 ppm) |
| ${}^{234}$Ac | 234 | 145 | L?-pending | binding_energy | — | 1774.2183 | — | 217968.9283 MeV (-208.9 ppm) |
| ${}^{235}$Ac | 235 | 146 | L?-pending | binding_energy | — | 1779.7737 | — | 218902.9381 MeV (-208.0 ppm) |
| ${}^{236}$Ac | 236 | 147 | L?-pending | binding_energy | — | 1783.9812 | — | 219838.2958 MeV (-207.1 ppm) |
| ${}^{237}$Ac | 237 | 148 | L?-pending | binding_energy | — | 1789.3500 | — | 220772.4922 MeV (-206.6 ppm) |

### Thorium (Z = 90)

_0 of 32 isotopes with a framework prediction; 32 of 32 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{208}$Th | 208 | 118 | L?-pending | binding_energy | — | 1591.7349 | — | 193721.4236 MeV (-237.6 ppm) |
| ${}^{209}$Th | 209 | 119 | L?-pending | binding_energy | — | 1600.1040 | — | 194652.6197 MeV (-236.5 ppm) |
| ${}^{210}$Th | 210 | 120 | L?-pending | binding_energy | — | 1610.5060 | — | 195581.7829 MeV (-235.3 ppm) |
| ${}^{211}$Th | 211 | 121 | L?-pending | binding_energy | — | 1618.7605 | — | 196513.0936 MeV (-234.2 ppm) |
| ${}^{212}$Th | 212 | 122 | L?-pending | binding_energy | — | 1628.5973 | — | 197442.8220 MeV (-233.1 ppm) |
| ${}^{213}$Th | 213 | 123 | L?-pending | binding_energy | — | 1636.6594 | — | 198374.3250 MeV (-232.0 ppm) |
| ${}^{214}$Th | 214 | 124 | L?-pending | binding_energy | — | 1646.1559 | — | 199304.3937 MeV (-230.9 ppm) |
| ${}^{215}$Th | 215 | 125 | L?-pending | binding_energy | — | 1654.0007 | — | 200236.1141 MeV (-229.9 ppm) |
| ${}^{216}$Th | 216 | 126 | L?-pending | binding_energy | — | 1662.6949 | — | 201166.9851 MeV (-228.8 ppm) |
| ${}^{217}$Th | 217 | 127 | L?-pending | binding_energy | — | 1668.8590 | — | 202100.3862 MeV (-227.8 ppm) |
| ${}^{218}$Th | 218 | 128 | L?-pending | binding_energy | — | 1676.7694 | — | 203032.0410 MeV (-226.7 ppm) |
| ${}^{219}$Th | 219 | 129 | L?-pending | binding_energy | — | 1682.7446 | — | 203965.6309 MeV (-225.7 ppm) |
| ${}^{220}$Th | 220 | 130 | L?-pending | binding_energy | — | 1690.5892 | — | 204897.3515 MeV (-224.7 ppm) |
| ${}^{221}$Th | 221 | 131 | L?-pending | binding_energy | — | 1696.4101 | — | 205831.0958 MeV (-223.6 ppm) |
| ${}^{222}$Th | 222 | 132 | L?-pending | binding_energy | — | 1704.2183 | — | 206762.8528 MeV (-222.6 ppm) |
| ${}^{223}$Th | 223 | 133 | L?-pending | binding_energy | — | 1710.1073 | — | 207696.5290 MeV (-221.6 ppm) |
| ${}^{224}$Th | 224 | 134 | L?-pending | binding_energy | — | 1717.5684 | — | 208628.6331 MeV (-220.6 ppm) |
| ${}^{225}$Th | 225 | 135 | L?-pending | binding_energy | — | 1723.3252 | — | 209562.4415 MeV (-219.7 ppm) |
| ${}^{226}$Th | 226 | 136 | L?-pending | binding_energy | — | 1730.5090 | — | 210494.8228 MeV (-218.7 ppm) |
| ${}^{227}$Th | 227 | 137 | L?-pending | binding_energy | — | 1735.9732 | — | 211428.9238 MeV (-217.7 ppm) |
| ${}^{228}$Th | 228 | 138 | L?-pending | binding_energy | — | 1743.0784 | — | 212361.3838 MeV (-216.8 ppm) |
| ${}^{229}$Th | 229 | 139 | L?-pending | binding_energy | — | 1748.3351 | — | 213295.6923 MeV (-215.8 ppm) |
| ${}^{230}$Th | 230 | 140 | L?-pending | binding_energy | — | 1755.1294 | — | 214228.4632 MeV (-214.9 ppm) |
| ${}^{231}$Th | 231 | 141 | L?-pending | binding_energy | — | 1760.2474 | — | 215162.9103 MeV (-213.9 ppm) |
| ${}^{232}$Th | 232 | 142 | L?-pending | binding_energy | — | 1766.6878 | — | 216096.0351 MeV (-213.0 ppm) |
| ${}^{233}$Th | 233 | 143 | L?-pending | binding_energy | — | 1771.4742 | — | 217030.8139 MeV (-212.1 ppm) |
| ${}^{234}$Th | 234 | 144 | L?-pending | binding_energy | — | 1777.6642 | — | 217964.1891 MeV (-211.2 ppm) |
| ${}^{235}$Th | 235 | 145 | L?-pending | binding_energy | — | 1782.3308 | — | 218899.0878 MeV (-210.3 ppm) |
| ${}^{236}$Th | 236 | 146 | L?-pending | binding_energy | — | 1788.1646 | — | 219832.8191 MeV (-209.4 ppm) |
| ${}^{237}$Th | 237 | 147 | L?-pending | binding_energy | — | 1792.5361 | — | 220768.0128 MeV (-208.5 ppm) |
| ${}^{238}$Th | 238 | 148 | L?-pending | binding_energy | — | 1798.0900 | — | 221702.0241 MeV (-207.9 ppm) |
| ${}^{239}$Th | 239 | 149 | L?-pending | binding_energy | — | 1802.0600 | — | 222637.6193 MeV (-206.4 ppm) |

### Protactinium (Z = 91)

_0 of 31 isotopes with a framework prediction; 31 of 31 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{211}$Pa | 211 | 120 | L?-pending | binding_energy | — | 1609.8023 | — | 196520.7584 MeV (-236.8 ppm) |
| ${}^{212}$Pa | 212 | 121 | L?-pending | binding_energy | — | 1618.3293 | — | 197451.7966 MeV (-235.7 ppm) |
| ${}^{213}$Pa | 213 | 122 | L?-pending | binding_energy | — | 1628.3430 | — | 198381.3481 MeV (-234.6 ppm) |
| ${}^{214}$Pa | 214 | 123 | L?-pending | binding_energy | — | 1636.6086 | — | 199312.6477 MeV (-233.5 ppm) |
| ${}^{215}$Pa | 215 | 124 | L?-pending | binding_energy | — | 1646.3353 | — | 200242.4862 MeV (-232.4 ppm) |
| ${}^{216}$Pa | 216 | 125 | L?-pending | binding_energy | — | 1654.3873 | — | 201173.9993 MeV (-231.3 ppm) |
| ${}^{217}$Pa | 217 | 126 | L?-pending | binding_energy | — | 1663.2277 | — | 202104.7242 MeV (-230.3 ppm) |
| ${}^{218}$Pa | 218 | 127 | L?-pending | binding_energy | — | 1669.7042 | — | 203037.8129 MeV (-229.2 ppm) |
| ${}^{219}$Pa | 219 | 128 | L?-pending | binding_energy | — | 1677.8418 | — | 203969.2404 MeV (-228.2 ppm) |
| ${}^{220}$Pa | 220 | 129 | L?-pending | binding_energy | — | 1684.2180 | — | 204902.4294 MeV (-227.1 ppm) |
| ${}^{221}$Pa | 221 | 130 | L?-pending | binding_energy | — | 1692.1928 | — | 205834.0198 MeV (-226.1 ppm) |
| ${}^{222}$Pa | 222 | 131 | L?-pending | binding_energy | — | 1698.5747 | — | 206767.2031 MeV (-225.1 ppm) |
| ${}^{223}$Pa | 223 | 132 | L?-pending | binding_energy | — | 1706.3727 | — | 207698.9702 MeV (-224.1 ppm) |
| ${}^{224}$Pa | 224 | 133 | L?-pending | binding_energy | — | 1712.9193 | — | 208631.9888 MeV (-223.1 ppm) |
| ${}^{225}$Pa | 225 | 134 | L?-pending | binding_energy | — | 1720.4963 | — | 209563.9770 MeV (-222.1 ppm) |
| ${}^{226}$Pa | 226 | 135 | L?-pending | binding_energy | — | 1726.8907 | — | 210497.1478 MeV (-221.1 ppm) |
| ${}^{227}$Pa | 227 | 136 | L?-pending | binding_energy | — | 1734.1653 | — | 211429.4385 MeV (-220.1 ppm) |
| ${}^{228}$Pa | 228 | 137 | L?-pending | binding_energy | — | 1740.1433 | — | 212363.0256 MeV (-219.2 ppm) |
| ${}^{229}$Pa | 229 | 138 | L?-pending | binding_energy | — | 1747.2414 | — | 213295.4927 MeV (-218.2 ppm) |
| ${}^{230}$Pa | 230 | 139 | L?-pending | binding_energy | — | 1753.0360 | — | 214229.2632 MeV (-217.3 ppm) |
| ${}^{231}$Pa | 231 | 140 | L?-pending | binding_energy | — | 1759.8566 | — | 215162.0079 MeV (-216.3 ppm) |
| ${}^{232}$Pa | 232 | 141 | L?-pending | binding_energy | — | 1765.4057 | — | 216096.0240 MeV (-215.4 ppm) |
| ${}^{233}$Pa | 233 | 142 | L?-pending | binding_energy | — | 1771.9341 | — | 217029.0607 MeV (-214.5 ppm) |
| ${}^{234}$Pa | 234 | 143 | L?-pending | binding_energy | — | 1777.1560 | — | 217963.4040 MeV (-213.5 ppm) |
| ${}^{235}$Pa | 235 | 144 | L?-pending | binding_energy | — | 1783.2773 | — | 218896.8479 MeV (-212.6 ppm) |
| ${}^{236}$Pa | 236 | 145 | L?-pending | binding_energy | — | 1788.3035 | — | 219831.3868 MeV (-211.7 ppm) |
| ${}^{237}$Pa | 237 | 146 | L?-pending | binding_energy | — | 1794.1812 | — | 220765.0744 MeV (-210.8 ppm) |
| ${}^{238}$Pa | 238 | 147 | L?-pending | binding_energy | — | 1798.8861 | — | 221699.9346 MeV (-210.0 ppm) |
| ${}^{239}$Pa | 239 | 148 | L?-pending | binding_energy | — | 1804.4500 | — | 222633.9359 MeV (-208.8 ppm) |
| ${}^{240}$Pa | 240 | 149 | L?-pending | binding_energy | — | 1808.8800 | — | 223569.0711 MeV (-208.1 ppm) |
| ${}^{241}$Pa | 241 | 150 | L?-pending | binding_energy | — | 1814.2480 | — | 224503.2683 MeV (-207.3 ppm) |

### Uranium (Z = 92)

_0 of 29 isotopes with a framework prediction; 29 of 29 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{215}$U | 215 | 123 | L?-pending | binding_energy | — | 1638.4682 | — | 200249.0600 MeV (-235.0 ppm) |
| ${}^{216}$U | 216 | 124 | L?-pending | binding_energy | — | 1648.3624 | — | 201178.7310 MeV (-233.9 ppm) |
| ${}^{217}$U | 217 | 125 | L?-pending | binding_energy | — | 1656.5780 | — | 202110.0805 MeV (-233.0 ppm) |
| ${}^{218}$U | 218 | 126 | L?-pending | binding_energy | — | 1665.6768 | — | 203040.5469 MeV (-231.7 ppm) |
| ${}^{219}$U | 219 | 127 | L?-pending | binding_energy | — | 1672.3468 | — | 203973.4421 MeV (-230.7 ppm) |
| ${}^{220}$U | 220 | 128 | L?-pending | binding_energy | — | 1680.8000 | — | 204904.5541 MeV (-230.1 ppm) |
| ${}^{221}$U | 221 | 129 | L?-pending | binding_energy | — | 1687.2654 | — | 205837.6539 MeV (-228.6 ppm) |
| ${}^{222}$U | 222 | 130 | L?-pending | binding_energy | — | 1695.5839 | — | 206768.9006 MeV (-227.6 ppm) |
| ${}^{223}$U | 223 | 131 | L?-pending | binding_energy | — | 1701.8827 | — | 207702.1669 MeV (-226.5 ppm) |
| ${}^{224}$U | 224 | 132 | L?-pending | binding_energy | — | 1710.2566 | — | 208633.3582 MeV (-225.5 ppm) |
| ${}^{225}$U | 225 | 133 | L?-pending | binding_energy | — | 1716.6986 | — | 209566.4814 MeV (-224.5 ppm) |
| ${}^{226}$U | 226 | 134 | L?-pending | binding_energy | — | 1724.8132 | — | 210497.9320 MeV (-223.5 ppm) |
| ${}^{227}$U | 227 | 135 | L?-pending | binding_energy | — | 1731.1682 | — | 211431.1421 MeV (-222.5 ppm) |
| ${}^{228}$U | 228 | 136 | L?-pending | binding_energy | — | 1739.0646 | — | 212362.8110 MeV (-221.6 ppm) |
| ${}^{229}$U | 229 | 137 | L?-pending | binding_energy | — | 1745.1453 | — | 213296.2954 MeV (-220.6 ppm) |
| ${}^{230}$U | 230 | 138 | L?-pending | binding_energy | — | 1752.8122 | — | 214228.1937 MeV (-219.6 ppm) |
| ${}^{231}$U | 231 | 139 | L?-pending | binding_energy | — | 1758.6926 | — | 215161.8785 MeV (-218.7 ppm) |
| ${}^{232}$U | 232 | 140 | L?-pending | binding_energy | — | 1765.9604 | — | 216094.1759 MeV (-217.8 ppm) |
| ${}^{233}$U | 233 | 141 | L?-pending | binding_energy | — | 1771.7221 | — | 217027.9794 MeV (-216.8 ppm) |
| ${}^{234}$U | 234 | 142 | L?-pending | binding_energy | — | 1778.5675 | — | 217960.6991 MeV (-215.9 ppm) |
| ${}^{235}$U | 235 | 143 | L?-pending | binding_energy | — | 1783.8650 | — | 218894.9668 MeV (-215.0 ppm) |
| ${}^{236}$U | 236 | 144 | L?-pending | binding_energy | — | 1790.4106 | — | 219827.9865 MeV (-214.1 ppm) |
| ${}^{237}$U | 237 | 145 | L?-pending | binding_energy | — | 1795.5363 | — | 220762.4259 MeV (-213.2 ppm) |
| ${}^{238}$U | 238 | 146 | L?-pending | binding_energy | — | 1801.6900 | — | 221695.8374 MeV (-212.3 ppm) |
| ${}^{239}$U | 239 | 147 | L?-pending | binding_energy | — | 1806.4964 | — | 222630.5962 MeV (-211.4 ppm) |
| ${}^{240}$U | 240 | 148 | L?-pending | binding_energy | — | 1812.4249 | — | 223564.2329 MeV (-210.5 ppm) |
| ${}^{241}$U | 241 | 149 | L?-pending | binding_energy | — | 1816.8990 | — | 224499.3240 MeV (-209.1 ppm) |
| ${}^{242}$U | 242 | 150 | L?-pending | binding_energy | — | 1822.7440 | — | 225433.0441 MeV (-209.1 ppm) |
| ${}^{243}$U | 243 | 151 | L?-pending | binding_energy | — | 1826.8740 | — | 226368.4793 MeV (-207.9 ppm) |

### Neptunium (Z = 93)

_0 of 27 isotopes with a framework prediction; 27 of 27 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{219}$Np | 219 | 126 | L?-pending | binding_energy | — | 1665.4234 | — | 203979.0721 MeV (-233.2 ppm) |
| ${}^{220}$Np | 220 | 127 | L?-pending | binding_energy | — | 1672.4567 | — | 204911.6041 MeV (-232.1 ppm) |
| ${}^{221}$Np | 221 | 128 | L?-pending | binding_energy | — | 1681.1470 | — | 205842.4789 MeV (-231.3 ppm) |
| ${}^{222}$Np | 222 | 129 | L?-pending | binding_energy | — | 1687.7997 | — | 206775.3914 MeV (-230.0 ppm) |
| ${}^{223}$Np | 223 | 130 | L?-pending | binding_energy | — | 1696.4871 | — | 207706.2692 MeV (-229.0 ppm) |
| ${}^{224}$Np | 224 | 131 | L?-pending | binding_energy | — | 1703.1847 | — | 208639.1368 MeV (-228.0 ppm) |
| ${}^{225}$Np | 225 | 132 | L?-pending | binding_energy | — | 1711.6702 | — | 209570.2165 MeV (-227.0 ppm) |
| ${}^{226}$Np | 226 | 133 | L?-pending | binding_energy | — | 1718.5427 | — | 210502.9091 MeV (-226.0 ppm) |
| ${}^{227}$Np | 227 | 134 | L?-pending | binding_energy | — | 1726.8519 | — | 211434.1651 MeV (-225.0 ppm) |
| ${}^{228}$Np | 228 | 135 | L?-pending | binding_energy | — | 1733.7120 | — | 212366.8702 MeV (-224.1 ppm) |
| ${}^{229}$Np | 229 | 136 | L?-pending | binding_energy | — | 1741.7722 | — | 213298.3752 MeV (-223.0 ppm) |
| ${}^{230}$Np | 230 | 137 | L?-pending | binding_energy | — | 1748.4083 | — | 214231.3043 MeV (-222.0 ppm) |
| ${}^{231}$Np | 231 | 138 | L?-pending | binding_energy | — | 1756.0925 | — | 215163.1853 MeV (-221.1 ppm) |
| ${}^{232}$Np | 232 | 139 | L?-pending | binding_energy | — | 1762.5040 | — | 216096.3390 MeV (-220.5 ppm) |
| ${}^{233}$Np | 233 | 140 | L?-pending | binding_energy | — | 1769.9103 | — | 217028.4978 MeV (-219.2 ppm) |
| ${}^{234}$Np | 234 | 141 | L?-pending | binding_energy | — | 1775.9753 | — | 217961.9980 MeV (-218.2 ppm) |
| ${}^{235}$Np | 235 | 142 | L?-pending | binding_energy | — | 1782.9584 | — | 218894.5801 MeV (-217.3 ppm) |
| ${}^{236}$Np | 236 | 143 | L?-pending | binding_energy | — | 1788.6947 | — | 219828.4090 MeV (-216.4 ppm) |
| ${}^{237}$Np | 237 | 144 | L?-pending | binding_energy | — | 1795.2725 | — | 220761.3964 MeV (-215.5 ppm) |
| ${}^{238}$Np | 238 | 145 | L?-pending | binding_energy | — | 1800.7608 | — | 221695.4732 MeV (-214.6 ppm) |
| ${}^{239}$Np | 239 | 146 | L?-pending | binding_energy | — | 1806.9758 | — | 222628.8235 MeV (-213.7 ppm) |
| ${}^{240}$Np | 240 | 147 | L?-pending | binding_energy | — | 1812.0418 | — | 223563.3226 MeV (-212.8 ppm) |
| ${}^{241}$Np | 241 | 148 | L?-pending | binding_energy | — | 1818.1143 | — | 224496.8154 MeV (-211.9 ppm) |
| ${}^{242}$Np | 242 | 149 | L?-pending | binding_energy | — | 1823.0838 | — | 225431.4110 MeV (-211.0 ppm) |
| ${}^{243}$Np | 243 | 150 | L?-pending | binding_energy | — | 1828.8180 | — | 226365.2420 MeV (-210.4 ppm) |
| ${}^{244}$Np | 244 | 151 | L?-pending | binding_energy | — | 1833.4160 | — | 227300.2092 MeV (-209.3 ppm) |
| ${}^{245}$Np | 245 | 152 | L?-pending | binding_energy | — | 1838.9700 | — | 228234.2204 MeV (-208.9 ppm) |

### Plutonium (Z = 94)

_0 of 27 isotopes with a framework prediction; 27 of 27 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{221}$Pu | 221 | 127 | L?-pending | binding_energy | — | 1674.2960 | — | 205848.0366 MeV (-233.6 ppm) |
| ${}^{222}$Pu | 222 | 128 | L?-pending | binding_energy | — | 1683.2040 | — | 206778.6938 MeV (-232.4 ppm) |
| ${}^{223}$Pu | 223 | 129 | L?-pending | binding_energy | — | 1690.3400 | — | 207711.1230 MeV (-231.9 ppm) |
| ${}^{224}$Pu | 224 | 130 | L?-pending | binding_energy | — | 1699.2640 | — | 208641.7642 MeV (-230.9 ppm) |
| ${}^{225}$Pu | 225 | 131 | L?-pending | binding_energy | — | 1706.1750 | — | 209574.4183 MeV (-229.2 ppm) |
| ${}^{226}$Pu | 226 | 132 | L?-pending | binding_energy | — | 1714.8880 | — | 210505.2705 MeV (-228.1 ppm) |
| ${}^{227}$Pu | 227 | 133 | L?-pending | binding_energy | — | 1721.7950 | — | 211437.9287 MeV (-227.0 ppm) |
| ${}^{228}$Pu | 228 | 134 | L?-pending | binding_energy | — | 1730.6121 | — | 212368.6768 MeV (-226.4 ppm) |
| ${}^{229}$Pu | 229 | 135 | L?-pending | binding_energy | — | 1737.3963 | — | 213301.4578 MeV (-225.4 ppm) |
| ${}^{230}$Pu | 230 | 136 | L?-pending | binding_energy | — | 1745.9304 | — | 214232.4889 MeV (-224.4 ppm) |
| ${}^{231}$Pu | 231 | 137 | L?-pending | binding_energy | — | 1752.6253 | — | 215165.3592 MeV (-223.4 ppm) |
| ${}^{232}$Pu | 232 | 138 | L?-pending | binding_energy | — | 1760.6443 | — | 216096.9054 MeV (-222.5 ppm) |
| ${}^{233}$Pu | 233 | 139 | L?-pending | binding_energy | — | 1767.0247 | — | 217030.0902 MeV (-221.5 ppm) |
| ${}^{234}$Pu | 234 | 140 | L?-pending | binding_energy | — | 1774.7978 | — | 217961.8822 MeV (-220.6 ppm) |
| ${}^{235}$Pu | 235 | 141 | L?-pending | binding_energy | — | 1781.0368 | — | 218895.2084 MeV (-219.6 ppm) |
| ${}^{236}$Pu | 236 | 142 | L?-pending | binding_energy | — | 1788.3889 | — | 219827.4214 MeV (-218.7 ppm) |
| ${}^{237}$Pu | 237 | 143 | L?-pending | binding_energy | — | 1794.2701 | — | 220761.1055 MeV (-217.8 ppm) |
| ${}^{238}$Pu | 238 | 144 | L?-pending | binding_energy | — | 1801.2699 | — | 221693.6708 MeV (-216.9 ppm) |
| ${}^{239}$Pu | 239 | 145 | L?-pending | binding_energy | — | 1806.9162 | — | 222627.5898 MeV (-216.0 ppm) |
| ${}^{240}$Pu | 240 | 146 | L?-pending | binding_energy | — | 1813.4504 | — | 223560.6207 MeV (-215.1 ppm) |
| ${}^{241}$Pu | 241 | 147 | L?-pending | binding_energy | — | 1818.6919 | — | 224494.9444 MeV (-214.2 ppm) |
| ${}^{242}$Pu | 242 | 148 | L?-pending | binding_energy | — | 1825.0015 | — | 225428.2000 MeV (-213.3 ppm) |
| ${}^{243}$Pu | 243 | 149 | L?-pending | binding_energy | — | 1830.0351 | — | 226362.7315 MeV (-212.4 ppm) |
| ${}^{244}$Pu | 244 | 150 | L?-pending | binding_energy | — | 1836.0550 | — | 227296.2769 MeV (-211.5 ppm) |
| ${}^{245}$Pu | 245 | 151 | L?-pending | binding_energy | — | 1840.7541 | — | 228231.1429 MeV (-210.7 ppm) |
| ${}^{246}$Pu | 246 | 152 | L?-pending | binding_energy | — | 1846.6089 | — | 229164.8534 MeV (-209.8 ppm) |
| ${}^{247}$Pu | 247 | 153 | L?-pending | binding_energy | — | 1850.7710 | — | 230100.2564 MeV (-208.5 ppm) |

### Americium (Z = 95)

_0 of 27 isotopes with a framework prediction; 27 of 27 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{223}$Am | 223 | 128 | L?-pending | binding_energy | — | 1682.9810 | — | 207717.1886 MeV (-234.4 ppm) |
| ${}^{224}$Am | 224 | 129 | L?-pending | binding_energy | — | 1690.3040 | — | 208649.4308 MeV (-232.4 ppm) |
| ${}^{225}$Am | 225 | 130 | L?-pending | binding_energy | — | 1699.4250 | — | 209579.8750 MeV (-232.3 ppm) |
| ${}^{226}$Am | 226 | 131 | L?-pending | binding_energy | — | 1706.7520 | — | 210512.1132 MeV (-230.5 ppm) |
| ${}^{227}$Am | 227 | 132 | L?-pending | binding_energy | — | 1715.6660 | — | 211442.7644 MeV (-229.7 ppm) |
| ${}^{228}$Am | 228 | 133 | L?-pending | binding_energy | — | 1722.9960 | — | 212374.9996 MeV (-228.3 ppm) |
| ${}^{229}$Am | 229 | 134 | L?-pending | binding_energy | — | 1731.8285 | — | 213305.7323 MeV (-227.8 ppm) |
| ${}^{230}$Am | 230 | 135 | L?-pending | binding_energy | — | 1739.2600 | — | 214237.8659 MeV (-227.0 ppm) |
| ${}^{231}$Am | 231 | 136 | L?-pending | binding_energy | — | 1747.7460 | — | 215168.9451 MeV (-225.8 ppm) |
| ${}^{232}$Am | 232 | 137 | L?-pending | binding_energy | — | 1754.8480 | — | 216101.4083 MeV (-225.0 ppm) |
| ${}^{233}$Am | 233 | 138 | L?-pending | binding_energy | — | 1763.1110 | — | 217032.7105 MeV (-224.3 ppm) |
| ${}^{234}$Am | 234 | 139 | L?-pending | binding_energy | — | 1769.9760 | — | 217965.4107 MeV (-223.2 ppm) |
| ${}^{235}$Am | 235 | 140 | L?-pending | binding_energy | — | 1777.8122 | — | 218897.1397 MeV (-222.0 ppm) |
| ${}^{236}$Am | 236 | 141 | L?-pending | binding_energy | — | 1784.3960 | — | 219830.1210 MeV (-220.7 ppm) |
| ${}^{237}$Am | 237 | 142 | L?-pending | binding_energy | — | 1791.9570 | — | 220762.1252 MeV (-219.9 ppm) |
| ${}^{238}$Am | 238 | 143 | L?-pending | binding_energy | — | 1798.2293 | — | 221695.4181 MeV (-219.2 ppm) |
| ${}^{239}$Am | 239 | 144 | L?-pending | binding_energy | — | 1805.3317 | — | 222627.8809 MeV (-218.3 ppm) |
| ${}^{240}$Am | 240 | 145 | L?-pending | binding_energy | — | 1811.2833 | — | 223561.4945 MeV (-217.3 ppm) |
| ${}^{241}$Am | 241 | 146 | L?-pending | binding_energy | — | 1817.9304 | — | 224494.4126 MeV (-216.4 ppm) |
| ${}^{242}$Am | 242 | 147 | L?-pending | binding_energy | — | 1823.4680 | — | 225428.4402 MeV (-215.5 ppm) |
| ${}^{243}$Am | 243 | 148 | L?-pending | binding_energy | — | 1829.8323 | — | 226361.6410 MeV (-214.7 ppm) |
| ${}^{244}$Am | 244 | 149 | L?-pending | binding_energy | — | 1835.1995 | — | 227295.8390 MeV (-213.8 ppm) |
| ${}^{245}$Am | 245 | 150 | L?-pending | binding_energy | — | 1841.2496 | — | 228229.3541 MeV (-212.9 ppm) |
| ${}^{246}$Am | 246 | 151 | L?-pending | binding_energy | — | 1846.2300 | — | 229163.9389 MeV (-212.0 ppm) |
| ${}^{247}$Am | 247 | 152 | L?-pending | binding_energy | — | 1852.2530 | — | 230097.4811 MeV (-211.7 ppm) |
| ${}^{248}$Am | 248 | 153 | L?-pending | binding_energy | — | 1856.7760 | — | 231032.5233 MeV (-210.2 ppm) |
| ${}^{249}$Am | 249 | 154 | L?-pending | binding_energy | — | 1862.2710 | — | 231966.5934 MeV (-209.2 ppm) |

### Curium (Z = 96)

_0 of 22 isotopes with a framework prediction; 22 of 22 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{231}$Cm | 231 | 135 | L?-pending | binding_energy | — | 1742.2020 | — | 215173.1958 MeV (-228.7 ppm) |
| ${}^{232}$Cm | 232 | 136 | L?-pending | binding_energy | — | 1751.1360 | — | 216103.8270 MeV (-227.3 ppm) |
| ${}^{233}$Cm | 233 | 137 | L?-pending | binding_energy | — | 1758.2185 | — | 217036.3097 MeV (-226.2 ppm) |
| ${}^{234}$Cm | 234 | 138 | L?-pending | binding_energy | — | 1766.8607 | — | 217967.2326 MeV (-225.3 ppm) |
| ${}^{235}$Cm | 235 | 139 | L?-pending | binding_energy | — | 1773.5450 | — | 218900.1135 MeV (-223.9 ppm) |
| ${}^{236}$Cm | 236 | 140 | L?-pending | binding_energy | — | 1781.8729 | — | 219831.3508 MeV (-223.3 ppm) |
| ${}^{237}$Cm | 237 | 141 | L?-pending | binding_energy | — | 1788.5499 | — | 220764.2390 MeV (-222.4 ppm) |
| ${}^{238}$Cm | 238 | 142 | L?-pending | binding_energy | — | 1796.4232 | — | 221695.9309 MeV (-221.5 ppm) |
| ${}^{239}$Cm | 239 | 143 | L?-pending | binding_energy | — | 1802.7928 | — | 222629.1265 MeV (-220.5 ppm) |
| ${}^{240}$Cm | 240 | 144 | L?-pending | binding_energy | — | 1810.2868 | — | 223561.1976 MeV (-219.6 ppm) |
| ${}^{241}$Cm | 241 | 145 | L?-pending | binding_energy | — | 1816.3806 | — | 224494.6691 MeV (-218.7 ppm) |
| ${}^{242}$Cm | 242 | 146 | L?-pending | binding_energy | — | 1823.3500 | — | 225427.2648 MeV (-217.8 ppm) |
| ${}^{243}$Cm | 243 | 147 | L?-pending | binding_energy | — | 1829.0430 | — | 226361.1370 MeV (-216.9 ppm) |
| ${}^{244}$Cm | 244 | 148 | L?-pending | binding_energy | — | 1835.8445 | — | 227293.9007 MeV (-216.0 ppm) |
| ${}^{245}$Cm | 245 | 149 | L?-pending | binding_energy | — | 1841.3631 | — | 228227.9473 MeV (-215.1 ppm) |
| ${}^{246}$Cm | 246 | 150 | L?-pending | binding_energy | — | 1847.8220 | — | 229161.0535 MeV (-214.3 ppm) |
| ${}^{247}$Cm | 247 | 151 | L?-pending | binding_energy | — | 1852.9772 | — | 230095.4636 MeV (-213.4 ppm) |
| ${}^{248}$Cm | 248 | 152 | L?-pending | binding_energy | — | 1859.1888 | — | 231028.8171 MeV (-212.5 ppm) |
| ${}^{249}$Cm | 249 | 153 | L?-pending | binding_energy | — | 1863.9022 | — | 231963.6689 MeV (-211.7 ppm) |
| ${}^{250}$Cm | 250 | 154 | L?-pending | binding_energy | — | 1869.7346 | — | 232897.4017 MeV (-210.8 ppm) |
| ${}^{251}$Cm | 251 | 155 | L?-pending | binding_energy | — | 1874.1475 | — | 233832.5539 MeV (-210.0 ppm) |
| ${}^{252}$Cm | 252 | 156 | L?-pending | binding_energy | — | 1879.9200 | — | 234766.3467 MeV (-209.6 ppm) |

### Berkelium (Z = 97)

_0 of 22 isotopes with a framework prediction; 22 of 22 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{233}$Bk | 233 | 136 | L?-pending | binding_energy | — | 1751.9270 | — | 217041.3078 MeV (-228.4 ppm) |
| ${}^{234}$Bk | 234 | 137 | L?-pending | binding_energy | — | 1759.4460 | — | 217973.3540 MeV (-227.8 ppm) |
| ${}^{235}$Bk | 235 | 138 | L?-pending | binding_energy | — | 1768.1400 | — | 218904.2252 MeV (-226.8 ppm) |
| ${}^{236}$Bk | 236 | 139 | L?-pending | binding_energy | — | 1775.4280 | — | 219836.5024 MeV (-225.8 ppm) |
| ${}^{237}$Bk | 237 | 140 | L?-pending | binding_energy | — | 1783.8990 | — | 220767.5966 MeV (-225.1 ppm) |
| ${}^{238}$Bk | 238 | 141 | L?-pending | binding_energy | — | 1790.9500 | — | 221700.1107 MeV (-224.1 ppm) |
| ${}^{239}$Bk | 239 | 142 | L?-pending | binding_energy | — | 1798.9530 | — | 222631.6729 MeV (-223.0 ppm) |
| ${}^{240}$Bk | 240 | 143 | L?-pending | binding_energy | — | 1805.5200 | — | 223564.6711 MeV (-221.7 ppm) |
| ${}^{241}$Bk | 241 | 144 | L?-pending | binding_energy | — | 1813.2840 | — | 224496.4723 MeV (-220.8 ppm) |
| ${}^{242}$Bk | 242 | 145 | L?-pending | binding_energy | — | 1819.5980 | — | 225429.7235 MeV (-220.0 ppm) |
| ${}^{243}$Bk | 243 | 146 | L?-pending | binding_energy | — | 1826.7530 | — | 226362.1337 MeV (-219.2 ppm) |
| ${}^{244}$Bk | 244 | 147 | L?-pending | binding_energy | — | 1832.8001 | — | 227295.6517 MeV (-218.3 ppm) |
| ${}^{245}$Bk | 245 | 148 | L?-pending | binding_energy | — | 1839.7715 | — | 228228.2455 MeV (-217.4 ppm) |
| ${}^{246}$Bk | 246 | 149 | L?-pending | binding_energy | — | 1845.6897 | — | 229161.8926 MeV (-216.5 ppm) |
| ${}^{247}$Bk | 247 | 150 | L?-pending | binding_energy | — | 1852.2384 | — | 230094.9090 MeV (-215.6 ppm) |
| ${}^{248}$Bk | 248 | 151 | L?-pending | binding_energy | — | 1857.6682 | — | 231029.0444 MeV (-214.7 ppm) |
| ${}^{249}$Bk | 249 | 152 | L?-pending | binding_energy | — | 1864.0242 | — | 231962.2536 MeV (-213.9 ppm) |
| ${}^{250}$Bk | 250 | 153 | L?-pending | binding_energy | — | 1868.9898 | — | 232896.8531 MeV (-213.0 ppm) |
| ${}^{251}$Bk | 251 | 154 | L?-pending | binding_energy | — | 1874.7852 | — | 233830.6230 MeV (-212.2 ppm) |
| ${}^{252}$Bk | 252 | 155 | L?-pending | binding_energy | — | 1879.6680 | — | 234765.3053 MeV (-211.8 ppm) |
| ${}^{253}$Bk | 253 | 156 | L?-pending | binding_energy | — | 1885.1030 | — | 235699.4355 MeV (-210.0 ppm) |
| ${}^{254}$Bk | 254 | 157 | L?-pending | binding_energy | — | 1889.7600 | — | 236634.3437 MeV (-209.4 ppm) |

### Californium (Z = 98)

_0 of 20 isotopes with a framework prediction; 20 of 20 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{237}$Cf | 237 | 139 | L?-pending | binding_energy | — | 1778.2941 | — | 220771.9081 MeV (-227.0 ppm) |
| ${}^{238}$Cf | 238 | 140 | L?-pending | binding_energy | — | 1787.1420 | — | 221702.6254 MeV (-226.6 ppm) |
| ${}^{239}$Cf | 239 | 141 | L?-pending | binding_energy | — | 1794.1730 | — | 222635.1596 MeV (-225.1 ppm) |
| ${}^{240}$Cf | 240 | 142 | L?-pending | binding_energy | — | 1802.4576 | — | 223566.4402 MeV (-224.2 ppm) |
| ${}^{241}$Cf | 241 | 143 | L?-pending | binding_energy | — | 1809.1870 | — | 224499.2760 MeV (-223.2 ppm) |
| ${}^{242}$Cf | 242 | 144 | L?-pending | binding_energy | — | 1817.2020 | — | 225430.8262 MeV (-222.3 ppm) |
| ${}^{243}$Cf | 243 | 145 | L?-pending | binding_energy | — | 1823.7150 | — | 226363.8783 MeV (-221.6 ppm) |
| ${}^{244}$Cf | 244 | 146 | L?-pending | binding_energy | — | 1831.2535 | — | 227295.9050 MeV (-220.5 ppm) |
| ${}^{245}$Cf | 245 | 147 | L?-pending | binding_energy | — | 1837.4178 | — | 228229.3059 MeV (-219.6 ppm) |
| ${}^{246}$Cf | 246 | 148 | L?-pending | binding_energy | — | 1844.7840 | — | 229161.5049 MeV (-218.7 ppm) |
| ${}^{247}$Cf | 247 | 149 | L?-pending | binding_energy | — | 1850.8362 | — | 230095.0179 MeV (-217.8 ppm) |
| ${}^{248}$Cf | 248 | 150 | L?-pending | binding_energy | — | 1857.7789 | — | 231027.6403 MeV (-217.0 ppm) |
| ${}^{249}$Cf | 249 | 151 | L?-pending | binding_energy | — | 1863.3655 | — | 231961.6190 MeV (-216.1 ppm) |
| ${}^{250}$Cf | 250 | 152 | L?-pending | binding_energy | — | 1869.9892 | — | 232894.5605 MeV (-215.2 ppm) |
| ${}^{251}$Cf | 251 | 153 | L?-pending | binding_energy | — | 1875.0959 | — | 233829.0190 MeV (-214.4 ppm) |
| ${}^{252}$Cf | 252 | 154 | L?-pending | binding_energy | — | 1881.2675 | — | 234762.4125 MeV (-213.5 ppm) |
| ${}^{253}$Cf | 253 | 155 | L?-pending | binding_energy | — | 1886.0719 | — | 235697.1733 MeV (-212.7 ppm) |
| ${}^{254}$Cf | 254 | 156 | L?-pending | binding_energy | — | 1892.1034 | — | 236630.7070 MeV (-211.8 ppm) |
| ${}^{255}$Cf | 255 | 157 | L?-pending | binding_energy | — | 1896.6900 | — | 237565.6856 MeV (-210.9 ppm) |
| ${}^{256}$Cf | 256 | 158 | L?-pending | binding_energy | — | 1902.5920 | — | 238499.3487 MeV (-210.4 ppm) |

### Einsteinium (Z = 99)

_0 of 20 isotopes with a framework prediction; 20 of 20 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{239}$Es | 239 | 140 | L?-pending | binding_energy | — | 1787.9590 | — | 222640.0803 MeV (-227.4 ppm) |
| ${}^{240}$Es | 240 | 141 | L?-pending | binding_energy | — | 1795.4400 | — | 223572.1644 MeV (-226.5 ppm) |
| ${}^{241}$Es | 241 | 142 | L?-pending | binding_energy | — | 1803.8850 | — | 224503.2846 MeV (-225.7 ppm) |
| ${}^{242}$Es | 242 | 143 | L?-pending | binding_energy | — | 1810.8860 | — | 225435.8488 MeV (-224.1 ppm) |
| ${}^{243}$Es | 243 | 144 | L?-pending | binding_energy | — | 1819.0980 | — | 226367.2020 MeV (-223.5 ppm) |
| ${}^{244}$Es | 244 | 145 | L?-pending | binding_energy | — | 1825.8520 | — | 227300.0132 MeV (-222.4 ppm) |
| ${}^{245}$Es | 245 | 146 | L?-pending | binding_energy | — | 1833.8250 | — | 228231.6054 MeV (-222.4 ppm) |
| ${}^{246}$Es | 246 | 147 | L?-pending | binding_energy | — | 1840.2731 | — | 229164.7225 MeV (-221.0 ppm) |
| ${}^{247}$Es | 247 | 148 | L?-pending | binding_energy | — | 1847.5848 | — | 230096.9759 MeV (-220.1 ppm) |
| ${}^{248}$Es | 248 | 149 | L?-pending | binding_energy | — | 1854.0480 | — | 231030.0779 MeV (-219.7 ppm) |
| ${}^{249}$Es | 249 | 150 | L?-pending | binding_energy | — | 1861.0260 | — | 231962.6651 MeV (-217.8 ppm) |
| ${}^{250}$Es | 250 | 151 | L?-pending | binding_energy | — | 1867.2500 | — | 232896.0063 MeV (-217.8 ppm) |
| ${}^{251}$Es | 251 | 152 | L?-pending | binding_energy | — | 1873.9369 | — | 233828.8845 MeV (-216.6 ppm) |
| ${}^{252}$Es | 252 | 153 | L?-pending | binding_energy | — | 1879.2252 | — | 234763.1615 MeV (-215.7 ppm) |
| ${}^{253}$Es | 253 | 154 | L?-pending | binding_energy | — | 1885.5806 | — | 235696.3712 MeV (-214.8 ppm) |
| ${}^{254}$Es | 254 | 155 | L?-pending | binding_energy | — | 1890.6683 | — | 236630.8488 MeV (-214.0 ppm) |
| ${}^{255}$Es | 255 | 156 | L?-pending | binding_energy | — | 1896.6445 | — | 237564.4377 MeV (-213.1 ppm) |
| ${}^{256}$Es | 256 | 157 | L?-pending | binding_energy | — | 1901.5680 | — | 238499.0794 MeV (-212.1 ppm) |
| ${}^{257}$Es | 257 | 158 | L?-pending | binding_energy | — | 1907.4540 | — | 239432.7586 MeV (-211.4 ppm) |
| ${}^{258}$Es | 258 | 159 | L?-pending | binding_energy | — | 1912.2960 | — | 240367.4818 MeV (-210.9 ppm) |

<!-- AUTO:per-z-sections END -->
