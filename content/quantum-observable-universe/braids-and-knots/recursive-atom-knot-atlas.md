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

_0 of 11 isotopes with a framework prediction; 11 of 11 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{3}$Li | 3 | 0 | L?-pending | binding_energy | — | -6.8010 | — | 2821.6166 MeV (-542.8 ppm) |
| ${}^{4}$Li | 4 | 1 | L?-pending | binding_energy | — | 4.6150 | — | 3749.7657 MeV (-408.9 ppm) |
| ${}^{5}$Li | 5 | 2 | L?-pending | binding_energy | — | 26.3307 | — | 4667.6153 MeV (-328.6 ppm) |
| ${}^{6}$Li | 6 | 3 | L?-pending | binding_energy | — | 31.9940 | — | 5601.5171 MeV (-273.8 ppm) |
| ${}^{7}$Li | 7 | 4 | L?-pending | binding_energy | — | 39.2451 | — | 6533.8312 MeV (-234.8 ppm) |
| ${}^{8}$Li | 8 | 5 | L?-pending | binding_energy | — | 41.2777 | — | 7471.3638 MeV (-205.4 ppm) |
| ${}^{9}$Li | 9 | 6 | L?-pending | binding_energy | — | 45.3399 | — | 8406.8667 MeV (-182.6 ppm) |
| ${}^{10}$Li | 10 | 7 | L?-pending | binding_energy | — | 45.3135 | — | 9346.4583 MeV (-164.2 ppm) |
| ${}^{11}$Li | 11 | 8 | L?-pending | binding_energy | — | 45.7092 | — | 10285.6278 MeV (-149.3 ppm) |
| ${}^{12}$Li | 12 | 9 | L?-pending | binding_energy | — | 45.4992 | — | 11225.4030 MeV (-136.8 ppm) |
| ${}^{13}$Li | 13 | 10 | L?-pending | binding_energy | — | 45.5992 | — | 12164.8682 MeV (-126.3 ppm) |

### Beryllium (Z = 4)

_1 of 12 isotopes with a framework prediction; 12 of 12 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{5}$Be | 5 | 1 | L?-pending | binding_energy | — | 0.0900 | — | 4692.5626 MeV (-435.9 ppm) |
| ${}^{6}$Be | 6 | 2 | L?-pending | binding_energy | — | 26.9235 | — | 5605.2943 MeV (-364.8 ppm) |
| ${}^{7}$Be | 7 | 3 | L?-pending | binding_energy | — | 37.6008 | — | 6534.1821 MeV (-313.0 ppm) |
| ${}^{8}$Be | 8 | 4 | L2-alpha-cluster | binding_energy | 62.3383 | 56.4995 | +10.33 % | 7449.0098 MeV (-1057.4 ppm) |
| ${}^{9}$Be | 9 | 5 | L?-pending | binding_energy | — | 58.1640 | — | 8392.7493 MeV (-243.7 ppm) |
| ${}^{10}$Be | 10 | 6 | L?-pending | binding_energy | — | 64.9763 | — | 9325.5022 MeV (-219.4 ppm) |
| ${}^{11}$Be | 11 | 7 | L?-pending | binding_energy | — | 65.4779 | — | 10264.5658 MeV (-199.3 ppm) |
| ${}^{12}$Be | 12 | 8 | L?-pending | binding_energy | — | 68.6487 | — | 11200.9602 MeV (-182.7 ppm) |
| ${}^{13}$Be | 13 | 9 | L?-pending | binding_energy | — | 68.1387 | — | 12141.0354 MeV (-168.6 ppm) |
| ${}^{14}$Be | 14 | 10 | L?-pending | binding_energy | — | 69.9146 | — | 13078.8247 MeV (-156.5 ppm) |
| ${}^{15}$Be | 15 | 11 | L?-pending | binding_energy | — | 68.1146 | — | 14020.1899 MeV (-146.0 ppm) |
| ${}^{16}$Be | 16 | 12 | L?-pending | binding_energy | — | 68.5646 | — | 14959.3051 MeV (-136.9 ppm) |

### Boron (Z = 5)

_0 of 16 isotopes with a framework prediction; 16 of 16 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{6}$B | 6 | 1 | L?-pending | binding_energy | — | -2.8020 | — | 5633.7264 MeV (-453.9 ppm) |
| ${}^{7}$B | 7 | 2 | L?-pending | binding_energy | — | 24.9109 | — | 6545.5787 MeV (-390.4 ppm) |
| ${}^{8}$B | 8 | 3 | L?-pending | binding_energy | — | 37.7372 | — | 7472.3176 MeV (-342.1 ppm) |
| ${}^{9}$B | 9 | 4 | L?-pending | binding_energy | — | 56.3136 | — | 8393.3064 MeV (-304.6 ppm) |
| ${}^{10}$B | 10 | 5 | L?-pending | binding_energy | — | 64.7508 | — | 9324.4344 MeV (-274.2 ppm) |
| ${}^{11}$B | 11 | 6 | L?-pending | binding_energy | — | 76.2051 | — | 10252.5453 MeV (-249.4 ppm) |
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

_1 of 16 isotopes with a framework prediction; 16 of 16 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{8}$C | 8 | 2 | L?-pending | binding_energy | — | 24.8122 | — | 7483.9493 MeV (-409.7 ppm) |
| ${}^{9}$C | 9 | 3 | L?-pending | binding_energy | — | 39.0368 | — | 8409.2899 MeV (-364.7 ppm) |
| ${}^{10}$C | 10 | 4 | L?-pending | binding_energy | — | 60.3204 | — | 9327.5714 MeV (-328.8 ppm) |
| ${}^{11}$C | 11 | 5 | L?-pending | binding_energy | — | 73.4410 | — | 10254.0160 MeV (-299.2 ppm) |
| ${}^{12}$C | 12 | 6 | L2-alpha-cluster | binding_energy | 97.1480 | 92.1617 | +5.41 % | 11169.8742 MeV (-720.6 ppm) |
| ${}^{13}$C | 13 | 7 | L?-pending | binding_energy | — | 97.1080 | — | 12109.4794 MeV (-253.4 ppm) |
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

_0 of 16 isotopes with a framework prediction; 16 of 16 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{10}$N | 10 | 3 | L?-pending | binding_energy | — | 36.4367 | — | 9350.1618 MeV (-382.7 ppm) |
| ${}^{11}$N | 11 | 4 | L?-pending | binding_energy | — | 58.9424 | — | 10267.2213 MeV (-348.5 ppm) |
| ${}^{12}$N | 12 | 5 | L?-pending | binding_energy | — | 74.0413 | — | 11191.6876 MeV (-319.8 ppm) |
| ${}^{13}$N | 13 | 6 | L?-pending | binding_energy | — | 94.1052 | — | 12111.1889 MeV (-295.5 ppm) |
| ${}^{14}$N | 14 | 7 | L?-pending | binding_energy | — | 104.6586 | — | 13040.2007 MeV (-274.5 ppm) |
| ${}^{15}$N | 15 | 8 | L?-pending | binding_energy | — | 115.4919 | — | 13968.9325 MeV (-256.2 ppm) |
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

_1 of 18 isotopes with a framework prediction; 18 of 18 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{11}$O | 11 | 3 | L?-pending | binding_energy | — | 34.7868 | — | 10290.0836 MeV (-397.4 ppm) |
| ${}^{12}$O | 12 | 4 | L?-pending | binding_energy | — | 58.5837 | — | 11205.8519 MeV (-364.9 ppm) |
| ${}^{13}$O | 13 | 5 | L?-pending | binding_energy | — | 75.5529 | — | 12128.4478 MeV (-337.2 ppm) |
| ${}^{14}$O | 14 | 6 | L?-pending | binding_energy | — | 98.7319 | — | 13044.8340 MeV (-313.5 ppm) |
| ${}^{15}$O | 15 | 7 | L?-pending | binding_energy | — | 111.9554 | — | 13971.1757 MeV (-292.8 ppm) |
| ${}^{16}$O | 16 | 8 | L2-alpha-cluster | binding_energy | 134.3846 | 127.6193 | +5.30 % | 14888.3117 MeV (-728.7 ppm) |
| ${}^{17}$O | 17 | 9 | L?-pending | binding_energy | — | 131.7624 | — | 15830.4991 MeV (-258.4 ppm) |
| ${}^{18}$O | 18 | 10 | L?-pending | binding_energy | — | 139.8078 | — | 16762.0189 MeV (-244.1 ppm) |
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

_0 of 19 isotopes with a framework prediction; 19 of 19 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{13}$F | 13 | 4 | L?-pending | binding_energy | — | 55.8610 | — | 12146.8464 MeV (-379.1 ppm) |
| ${}^{14}$F | 14 | 5 | L?-pending | binding_energy | — | 73.9929 | — | 13068.2797 MeV (-352.0 ppm) |
| ${}^{15}$F | 15 | 6 | L?-pending | binding_energy | — | 97.4619 | — | 13984.3759 MeV (-329.0 ppm) |
| ${}^{16}$F | 16 | 7 | L?-pending | binding_energy | — | 111.4248 | — | 14909.9782 MeV (-308.6 ppm) |
| ${}^{17}$F | 17 | 8 | L?-pending | binding_energy | — | 128.2196 | — | 15832.7486 MeV (-290.6 ppm) |
| ${}^{18}$F | 18 | 9 | L?-pending | binding_energy | — | 137.3695 | — | 16763.1638 MeV (-274.5 ppm) |
| ${}^{19}$F | 19 | 10 | L?-pending | binding_energy | — | 147.8014 | — | 17692.2972 MeV (-260.1 ppm) |
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

_1 of 20 isotopes with a framework prediction; 20 of 20 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|
| ${}^{15}$Ne | 15 | 5 | L?-pending | binding_energy | — | 73.0309 | — | 14007.5135 MeV (-364.9 ppm) |
| ${}^{16}$Ne | 16 | 6 | L?-pending | binding_energy | — | 97.3308 | — | 14922.7788 MeV (-342.6 ppm) |
| ${}^{17}$Ne | 17 | 7 | L?-pending | binding_energy | — | 112.8885 | — | 15846.7863 MeV (-322.6 ppm) |
| ${}^{18}$Ne | 18 | 8 | L?-pending | binding_energy | — | 132.1426 | — | 16767.0974 MeV (-304.9 ppm) |
| ${}^{19}$Ne | 19 | 9 | L?-pending | binding_energy | — | 143.7795 | — | 17695.0257 MeV (-288.9 ppm) |
| ${}^{20}$Ne | 20 | 10 | L2-alpha-cluster | binding_energy | 174.0483 | 160.6448 | +8.34 % | 18604.3221 MeV (-994.4 ppm) |
| ${}^{21}$Ne | 21 | 11 | L?-pending | binding_energy | — | 167.4060 | — | 19550.5296 MeV (-261.6 ppm) |
| ${}^{22}$Ne | 22 | 12 | L?-pending | binding_energy | — | 177.7702 | — | 20479.7305 MeV (-249.7 ppm) |
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

<!-- AUTO:per-z-sections END -->
