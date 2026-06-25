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
the prediction and AME residual. Composite entries reference
earlier entries (recursive structure).*

## Methodology classification (STRICT)

Every atlas entry carries a **methodology tag** recording how its
particle–knot identification was obtained.

| Tag | Definition | Examples |
|---|---|---|
| `principled-derivation` | Knot is the closure of an explicit $\sigma$-braid word in $H_{n_0}(q_0)$ from [`def:confined-particle`](#def:confined-particle); $\mathrm{Vol}_{\mathrm{hyp}}$ computed at $\geq 50$ decimal digits via `hp_volume_of_link_closure(braid_word, digits=50)`. | electron $\sigma_1^3$ $\to$ $3_1$, proton/neutron $(\sigma_1 \sigma_2^{-1})^3$ $\to$ $\mathcal{B}_3$. |
| `principled-gb-nf` | Trivial-NF entries: a single strand (unknot $0_1$) or the pure identity $\mathbf{1}$. | neutrino ($0_1$), quark; the bare photon (identity $\mathbf{1}$, not the unknot). |
| `manual-historical-volume-match` | Knot was identified in earlier work via volume-match against AME; well-established but the GB-NF derivation in $H_{n_0}(q_0)$ has not been computed yet. | ${}^2$H = $6_2$, ${}^{3}$H = $8_{11}$, ${}^{3}$He = $L_{6a4}$. |
| `magic-A-formula` | Algebraic shell-closure formula $A \cdot 8G$ for double-magic light nuclei; no single hyperbolic knot. | ${}^{4}$He. |
| `recursive-on-⁴He` | Built from $n \cdot {}^{4}\mathrm{He} + n_{\alpha\alpha} \cdot c_{\alpha\alpha}$ recursion; principled given ${}^{4}$He. | ${}^{8}$Be–${}^{40}$Ca. |

The principled pipeline computes $\mathrm{Vol}_{\mathrm{hyp}}$ from the
$\sigma$-braid word at $\geq 50$ decimal digits via SnapPy's
`Link(braid_closure=...).exterior.high_precision` inside
`mpmath.workdps(50)`; symbolic-in-$q$ Markov-trace coefficients $y_\lambda$
are supplied by the Wenzl bridge ([`y_lambda_wenzl_bridge_extended.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/y_lambda_wenzl_bridge_extended.py)).

For atoms $A \geq 5$, where the combinatorics of the full $\mathcal{H}_{3A}$ space explode and `SnapPea` topological limits fail, we bypass the full evaluation by taking the exact symbolic trace restricted solely to **active block-partitions** (`closed_form_tau_M`), sidestepping the combinatorial blow-up. This exact symbolic trace $B_{sym} = -\alpha \ln |\tau_M|$ is shown side-by-side with the rigorous Q-CLT finite-sum approximation $B_{qCLT} = -\alpha \sum \ln |\hat{V}_i|$.

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

For reference, the following closures appear in the atlas. Each
shows the braid word and its closed-knot/link form.

### $\widehat{\sigma_1^3}$ in $B_2$ — the **trefoil $3_1 = T_{2, 3}$**

Word: $\sigma_1^3$. Closure (in $B_2$, two-strand braid closed
into a single circle): the **trefoil knot**, simplest nontrivial
prime knot. Alternative names: $T_{2, 3}$, left-handed trefoil
(positive crossings) or right-handed (with $\sigma_1^{-3}$).
Used for: **electron** ($e^-$), and as the binding factor for
nucleons in $H_3$. Hyperbolic volume: $0$ (torus knot).

### $\widehat{(\sigma_1 \sigma_2^{-1})^3}$ in $B_3$ — **Borromean rings $\mathcal{B}_3$**

Word: $\sigma_1 \sigma_2^{-1} \sigma_1 \sigma_2^{-1} \sigma_1 \sigma_2^{-1}$.
Closure: three pairwise-unlinked circles that are jointly linked
(remove one $\to$ all separate). Hyperbolic volume:
$\mathrm{Vol}(\mathcal{B}_3) = 8 G \approx 7.328$ (Catalan-related).
Used for: **proton** $B_3(\mathrm{uud})$, **neutron** $B_3(\mathrm{udd})$,
where the flavor labels colour the crossings.

### $\widehat{(\sigma_1 \sigma_2^{-1})^2}$ in $B_3$ — **figure-eight $4_1$**

Word: $\sigma_1 \sigma_2^{-1} \sigma_1 \sigma_2^{-1}$. Closure: the
**figure-eight knot**, amphichiral (equal to its mirror).
Hyperbolic volume: $\mathrm{Vol}(4_1) = :val[Vol_4_1]{precision=6} \cdot \pi$, the
smallest among hyperbolic knots. Used for: **Higgs field** (mass
mechanism).

### $\widehat{\sigma_1^2}$ in $B_2$ — **Hopf link $L_H$**

Word: $\sigma_1^2$. Closure: two circles linked once. Hyperbolic
volume: $0$ (torus link). Used for: **gluon** (lowest force
carrier), and as the binding link in deuteron $D = [\mathfrak{p}, \mathfrak{n}]_{L_H}$.

### $\widehat{\mathbf{1}_{B_4}}$ — **photon ($\gamma$)**

Word: $\mathbf{1}_{B_4}$ (identity, no crossings). Closure:
4 disjoint unknots — knot-trivial, but the 4 strands carry
polarisation $\times$ chirality components on the exceptional divisor
$\mathcal{S}_p$. Used for: **photon**, vacuum-flux carrier.

### Hyperbolic atom-knots inventory

Brief inventory of the hyperbolic-knot identifications used in
the atlas. Methodology tag indicates how each identification was
obtained.

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

Principled entries:

- Tritium $^3$H at $\sim 1.6 \times 10^{-3}$ (`manual-historical`).
- Deuteron $^2$H at $\sim 1.1 \times 10^{-2}$ (`manual-historical`).
- $\alpha$-cluster atoms ${}^{8}$Be–${}^{40}$Ca: mean $|\mathrm{err}| \sim 8$%
 (`recursive-on-⁴He`).

Atlas covers $\ell \leq 2$ at $q_0$; further atoms ($\ell = 3$
molecules, heavier nuclei) defer to
[appendix-atomic-mass-calculations](#app:atomic-mass-calculations).

## All-atoms / all-isotopes extension

A layered framework extends the atlas to every isotope (real or
theoretical) under a single registry:

| Layer | Coverage | Pipeline |
|---|---|---|
| **Layer 1** | Light isotopes ($A \leq 7$) | Canonical $\sum_\lambda y_\lambda \cdot \chi^\lambda(\beta_{\text{atom}})$ via Rust `hecke-canonical-chi` + mpmath $y_\lambda$ |
| **Layer 2** | $\alpha$-cluster magic nuclei ($A = 4 n_\alpha$) | Recursive on $^4$He + $\alpha$–$\alpha$ coupling $c_{\alpha\alpha}$ |
| **Layer 3** | Non-$\alpha$ intermediate ($5 \leq A \leq 40$) | Hybrid: nearest-$\alpha$-cluster + valence-nucleon via canonical interface |
| **Layer 4** | Heavy nuclei ($A > 40$) | Brane-tower asymptotic + LP-active-set ansatz |
| **Layer 5** | Theoretical / hypothetical isotopes | Same Layer-1/3 machinery; flagged `prediction-only` |

Per-isotope records follow the [`IsotopeRecord`](https://github.com/litlfred/qou/blob/main/computations/isotope_record_schema.py)
dataclass schema with explicit knot-operator catalogue. Layer-1
pipeline implementation: [`canonical_mass_table_extended.py`](https://github.com/litlfred/qou/blob/main/computations/canonical_mass_table_extended.py).

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
| $c_{\alpha\alpha}$ | $\alpha$–$\alpha$ pair-energy correction (${}^{8}$Be, ${}^{12}$C, $\ldots$, ${}^{40}$Ca) |
| $\alpha$–N attachment | Layer 3: $^4$He cluster + valence nucleon (for non-magic $A$) |

For an atom with mass number $A$, the canonical braid word in
$B_{3A}$ is built sequentially per nucleon: at each $k \in \{0,
\ldots, A-1\}$ apply the intra block at base $3k$ and $3k+1$,
then (for $k < A-1$) apply the inter-nucleon interface at $3k+2$
between nucleon $k$ and $k+1$. The full sequence is enumerated by
[`build_knot_operator_catalogue(Z, N)`](https://github.com/litlfred/qou/blob/main/computations/isotope_record_schema.py)
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

_Computed via [`canonical_mass_table_extended.py`](https://github.com/litlfred/qou/blob/main/computations/canonical_mass_table_extended.py) (method=`markov_peel`). Witness: [`canonical-mass-table-extended.witness.json`](https://github.com/litlfred/qou/blob/main/computations/canonical-mass-table-extended.witness.json). Nucleon masses (m_p, m_n) via [`m-p-borromean-verification-50dps.witness.json`](https://github.com/litlfred/qou/blob/main/computations/m-p-borromean-verification-50dps.witness.json). Paper hard floor (CAL-2 propagation): ~780 ppb._

<!-- AUTO:canonical-tr-m-table END -->

## Build-pipeline integration

The atlas is auto-rendered by
[`recursive_atom_knot_atlas_render.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/recursive_atom_knot_atlas_render.py).

**Sources of truth** (in order):

1. [`confined-particle.md`](#def:confined-particle) — GB-NF particle registry (canonical $T_w$).
2. [`mass-table-ppb.witness.json`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/mass-table-ppb.witness.json) — D..${}^{40}$Ca (manual-historical, recursive, magic-A).
3. [`methodology-deprecation.witness.json`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/methodology-deprecation.witness.json) — per-particle methodology audit.
4. [`hp_volume.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/hp_volume.py) — $\geq 50$-digit symbolic-$q$ Markov-closure $\to$ $\mathrm{Vol}_{\mathrm{hyp}}$.
5. [`y_lambda_wenzl_bridge_extended.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/y_lambda_wenzl_bridge_extended.py) — symbolic-$q$ Wenzl bridge for $y_\lambda$.

For `principled-derivation` entries (electron, proton, neutron) the
hyperbolic volume of the Markov closure is computed from the
$\sigma$-braid word at $\geq 50$ decimal digits via
`hp_volume_of_link_closure(braid_word, digits=50)` which calls
SnapPy's `Link(braid_closure=...).exterior.high_precision`
inside `mpmath.workdps(50)`. Updates to any input propagate via
[`witness_staleness_tracker.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/witness_staleness_tracker.py)
to the rendered appendix on the next `bun run build`.

## SDP-uniqueness wiring (Lean side)

Each atlas entry has a corresponding **sorry-free SDP-uniqueness
theorem** in the Lean side, via the parameterised
`NucleusEmptySDPUniqueness` module and its three specialisation
layers. For any nucleus
characterised by mass number $A$ (yielding strand count $n = 3A$),
the canonical $T_w$ knot operator's uniqueness at the
empty-constraint SDP demonstration level is certified by:

$$
\texttt{nucleus\_uniqueness\_closed}\ (3A)\ : \ \text{(sorry-free, axiom-free)}
$$

Named wrappers exist at multiple granularity layers:

| Granularity | Lean file | Coverage |
|---|---|---|
| QOU-tracked R5-full nuclei | `Applied<Nucleus>Uniqueness.lean` (10 files) | $^2$H, $^3$H, $^3$He, $^4$He, $^6$Li, $^9$Be, $^{11}$B, $^{12}$C, $^{14}$N, $^{16}$O |
| Per-element (AME2020 ref) | `PeriodicTableUniqueness.lean` | 118 elements H..Og |
| Per-stable-isotope | `StableIsotopeUniqueness.lean` | 252 stable nuclides H..Bi |
| Generic | `NucleusEmptySDPUniqueness.lean` | Any $n : \mathbb{N}$ |

Usage example for any atlas entry: cite
`qou:QOU.BraidKnot.<isotope>_uniqueness_closed` in the
corresponding `.lean` content block's docstring. **Naming
convention**: the element symbol is taken from `AtomicMass.lean`;
elements whose short symbol collides with a reserved Lean
identifier (`n`, `p`, `s`, `b`, `k`, `v`, `y`, `i`, `u`, `w`)
receive an `_el` suffix (e.g. `n_el_uniqueness_closed` for
nitrogen, `b_el_uniqueness_closed` for boron). For atoms beyond
the named-isotope set, consumers can directly use
`@nucleus_uniqueness_closed (3*A)` with the appropriate $A$ value
from the atlas entry.

**What this wiring certifies**: the *abstract framework demonstration*
of $T_w$ uniqueness at the empty-constraint SDP for the
nucleus's strand count. The **real per-nucleus SDP** (with
non-empty constraints from the mass formula and multi-term cost)
is per-nucleus substantive open work — see
[`docs/coordination/2026-05-30-sdp-uniqueness-status.md`](https://github.com/litlfred/qou/blob/main/docs/coordination/2026-05-30-sdp-uniqueness-status.md)
for the gating analysis.

## Open

- **Principled derivation for ${}^{6}$Li, ${}^{7}$Li (and any new atom)**: the only
 admissible path is a **joint SDP on the full mass tower** — over all
 confinement levels $\ell$ and all atoms simultaneously — with
 **Gröbner–Shirshov filtration tracking** and **jet-order tracking**,
 yielding a canonical $T_w \in H_{n_0}(q_0)$ *per atom* as a structured
 certificate. Status: **certificate format proof-of-concept complete**
 ([`gb_filtration_jet_tracker.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/gb_filtration_jet_tracker.py)
 + [`gb-filtration-jet-order.witness.json`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/gb-filtration-jet-order.witness.json)).
 The reducer computes filtration grade + jet-order events exactly in
 symbolic $q$ via SymPy on the test cases $\sigma_1^3$ (electron) and
 $(\sigma_1 \sigma_2^{-1})^3$ (proton/neutron body). The joint-tower
 SDP solver consumes this certificate format. The Markov closure of $T_w$ is then taken in $S^3$ and
 $\mathrm{Vol}_{\mathrm{hyp}}$ is computed at $\geq 50$ decimal digits
 via `hp_volume_of_link_closure(braid_word, digits=50)`; comparison to
 the AME binding energy happens *a posteriori*. Per-atom volume-match search is FORBIDDEN as a
 derivation route — the SDP must be joint over the tower so the GB
 filtration and the jet ordering are consistent across confinement
 levels. Until that joint SDP is run, no principled ${}^{6}$Li / ${}^{7}$Li
 entry exists.
- **Structural rule for $\rho$ in $B = \rho \cdot m_e \cdot \mathrm{Vol}(K)$**:
 the pattern $\rho \in \{1, 2\}$ for $\ell \leq 2$ atoms does not extend to
 ${}^{6}$Li, ${}^{7}$Li. Open:
 derive $\rho(Z, N)$ from ILP / confinement structure.
- **Hyperbolic-knot identification beyond $\ell = 2$**: ${}^{9}$Be, ${}^{11}$B,
 ${}^{14}$N — no entries are in scope until a *principled* (GB-NF) derivation
 exists. Volume-match search will not be used.
- **Photon $\rho$-factor**: photon mass $= 0$ by definition (no $\rho$
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

_Auto-rendered from per-Z shards `canonical-isotope-witness-Z<NN>.witness.json` (emitted by [`canonical_isotope_witness.py`](https://github.com/litlfred/qou/blob/main/computations/canonical_isotope_witness.py)). Each row carries the Layer used (L1 canonical |tr_M|, L2 α-cluster recursion, L3 paper-six-term [pending], L4 composite mass), the framework prediction, the AME 2020 reference, and the residual. `Predicts = mass` for free nucleons (p, n) — value is the Borromean tower nucleon mass conditional on `conj:borromean-baryon-mass-formula`. `Predicts = binding_energy` for D and up; AME 2020 reference is the total binding energy. $M_{\text{composite}}$ is the L4 composite mass $N \cdot m_n + Z \cdot m_p - B$ when both nucleon masses (Borromean) and a binding-energy prediction are available; reference is the AME atomic mass converted via 1 u = 931.49410242 MeV._

### neutron (Z = 0)

_1 of 1 isotopes with a framework prediction; 0 of 1 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| $\mathfrak{n}$ | 1 | 1 | L1-borromean-via-canonical | substrate | mass | 939.5652 | 939.5654 | -0.251 ppm | — |

### Hydrogen (Z = 1)

_3 of 7 isotopes with a framework prediction; 2 of 7 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| $\mathfrak{p}$ | 1 | 0 | L1-borromean-via-canonical | substrate | mass | 938.2719 | 938.2721 | -0.251 ppm | — |
| ${}^{2}$H | 2 | 1 | L1-canonical | +empirical-(K,ρ) | binding_energy | 2.2488 | 2.2246 | +1.09 % | 1875.5882 MeV (-285.5 ppm) |
| ${}^{3}$H | 3 | 2 | L1-canonical | +empirical-(K,ρ) | binding_energy | 8.4686 | 8.4818 | -0.16 % | 2808.9336 MeV (-177.4 ppm) |
| ${}^{4}$H | 4 | 3 | L?-pending | pending | binding_energy | — | 6.8818 | — | — |
| ${}^{5}$H | 5 | 4 | L?-pending | pending | binding_energy | — | 6.6818 | — | — |
| ${}^{6}$H | 6 | 5 | L?-pending | pending | binding_energy | — | 5.7698 | — | — |
| ${}^{7}$H | 7 | 6 | L?-pending | pending | binding_energy | — | 6.5800 | — | — |

### Helium (Z = 2)

_2 of 8 isotopes with a framework prediction; 2 of 8 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{3}$He | 3 | 1 | L1-canonical | +empirical-(K,ρ) | binding_energy | 7.4889 | 7.7180 | -2.97 % | 2808.6200 MeV (-282.5 ppm) |
| ${}^{4}$He | 4 | 2 | L1-canonical | +empirical-(K,ρ) | binding_energy | 29.9557 | 28.2957 | +5.87 % | 3725.7184 MeV (-719.6 ppm) |
| ${}^{5}$He | 5 | 3 | L?-pending | pending | binding_energy | — | 27.5607 | — | — |
| ${}^{6}$He | 6 | 4 | L?-pending | pending | binding_energy | — | 29.2711 | — | — |
| ${}^{7}$He | 7 | 5 | L?-pending | pending | binding_energy | — | 28.8614 | — | — |
| ${}^{8}$He | 8 | 6 | L?-pending | pending | binding_energy | — | 31.3962 | — | — |
| ${}^{9}$He | 9 | 7 | L?-pending | pending | binding_energy | — | 30.1413 | — | — |
| ${}^{10}$He | 10 | 8 | L?-pending | pending | binding_energy | — | 29.9513 | — | — |

### Lithium (Z = 3)

_2 of 11 isotopes with a framework prediction; 0 of 11 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{3}$Li | 3 | 0 | L?-pending | pending | binding_energy | — | -6.8010 | — | — |
| ${}^{4}$Li | 4 | 1 | L?-pending | pending | binding_energy | — | 4.6150 | — | — |
| ${}^{5}$Li | 5 | 2 | L?-pending | pending | binding_energy | — | 26.3307 | — | — |
| ${}^{6}$Li | 6 | 3 | L3-partial-shell:f=0.500 from A=4$\to$8 | heuristic | binding_energy | 43.6570 | 31.9940 | +36.45 % | — |
| ${}^{7}$Li | 7 | 4 | L3-partial-shell:f=0.750 from A=4$\to$8 | heuristic | binding_energy | 51.3377 | 39.2451 | +30.81 % | — |
| ${}^{8}$Li | 8 | 5 | L?-pending | pending | binding_energy | — | 41.2777 | — | — |
| ${}^{9}$Li | 9 | 6 | L?-pending | pending | binding_energy | — | 45.3399 | — | — |
| ${}^{10}$Li | 10 | 7 | L?-pending | pending | binding_energy | — | 45.3135 | — | — |
| ${}^{11}$Li | 11 | 8 | L?-pending | pending | binding_energy | — | 45.7092 | — | — |
| ${}^{12}$Li | 12 | 9 | L?-pending | pending | binding_energy | — | 45.4992 | — | — |
| ${}^{13}$Li | 13 | 10 | L?-pending | pending | binding_energy | — | 45.5992 | — | — |

### Beryllium (Z = 4)

_3 of 12 isotopes with a framework prediction; 1 of 12 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{5}$Be | 5 | 1 | L?-pending | pending | binding_energy | — | 0.0900 | — | — |
| ${}^{6}$Be | 6 | 2 | L?-pending | pending | binding_energy | — | 26.9235 | — | — |
| ${}^{7}$Be | 7 | 3 | L?-pending | pending | binding_energy | — | 37.6008 | — | — |
| ${}^{8}$Be | 8 | 4 | L2-alpha-cluster | recursive | binding_energy | 62.3383 | 56.4995 | +10.33 % | 7449.0098 MeV (-1057.4 ppm) |
| ${}^{9}$Be | 9 | 5 | L3-partial-shell:f=0.250 from A=8$\to$12 | heuristic | binding_energy | 67.3058 | 58.1640 | +15.72 % | — |
| ${}^{10}$Be | 10 | 6 | L3-partial-shell:f=0.500 from A=8$\to$12 | heuristic | binding_energy | 75.5932 | 64.9763 | +16.34 % | — |
| ${}^{11}$Be | 11 | 7 | L?-pending | pending | binding_energy | — | 65.4779 | — | — |
| ${}^{12}$Be | 12 | 8 | L?-pending | pending | binding_energy | — | 68.6487 | — | — |
| ${}^{13}$Be | 13 | 9 | L?-pending | pending | binding_energy | — | 68.1387 | — | — |
| ${}^{14}$Be | 14 | 10 | L?-pending | pending | binding_energy | — | 69.9146 | — | — |
| ${}^{15}$Be | 15 | 11 | L?-pending | pending | binding_energy | — | 68.1146 | — | — |
| ${}^{16}$Be | 16 | 12 | L?-pending | pending | binding_energy | — | 68.5646 | — | — |

### Boron (Z = 5)

_2 of 16 isotopes with a framework prediction; 0 of 16 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{6}$B | 6 | 1 | L?-pending | pending | binding_energy | — | -2.8020 | — | — |
| ${}^{7}$B | 7 | 2 | L?-pending | pending | binding_energy | — | 24.9109 | — | — |
| ${}^{8}$B | 8 | 3 | L?-pending | pending | binding_energy | — | 37.7372 | — | — |
| ${}^{9}$B | 9 | 4 | L?-pending | pending | binding_energy | — | 56.3136 | — | — |
| ${}^{10}$B | 10 | 5 | L3-partial-shell:f=0.500 from A=8$\to$12 | heuristic | binding_energy | 75.5932 | 64.7508 | +16.74 % | — |
| ${}^{11}$B | 11 | 6 | L3-partial-shell:f=0.750 from A=8$\to$12 | heuristic | binding_energy | 83.8806 | 76.2051 | +10.07 % | — |
| ${}^{12}$B | 12 | 7 | L?-pending | pending | binding_energy | — | 79.5747 | — | — |
| ${}^{13}$B | 13 | 8 | L?-pending | pending | binding_energy | — | 84.4535 | — | — |
| ${}^{14}$B | 14 | 9 | L?-pending | pending | binding_energy | — | 85.4230 | — | — |
| ${}^{15}$B | 15 | 10 | L?-pending | pending | binding_energy | — | 88.2007 | — | — |
| ${}^{16}$B | 16 | 11 | L?-pending | pending | binding_energy | — | 88.1177 | — | — |
| ${}^{17}$B | 17 | 12 | L?-pending | pending | binding_energy | — | 89.5844 | — | — |
| ${}^{18}$B | 18 | 13 | L?-pending | pending | binding_energy | — | 89.5794 | — | — |
| ${}^{19}$B | 19 | 14 | L?-pending | pending | binding_energy | — | 89.6731 | — | — |
| ${}^{20}$B | 20 | 15 | L?-pending | pending | binding_energy | — | 88.1131 | — | — |
| ${}^{21}$B | 21 | 16 | L?-pending | pending | binding_energy | — | 87.2031 | — | — |

### Carbon (Z = 6)

_2 of 16 isotopes with a framework prediction; 1 of 16 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{8}$C | 8 | 2 | L?-pending | pending | binding_energy | — | 24.8122 | — | — |
| ${}^{9}$C | 9 | 3 | L?-pending | pending | binding_energy | — | 39.0368 | — | — |
| ${}^{10}$C | 10 | 4 | L?-pending | pending | binding_energy | — | 60.3204 | — | — |
| ${}^{11}$C | 11 | 5 | L?-pending | pending | binding_energy | — | 73.4410 | — | — |
| ${}^{12}$C | 12 | 6 | L2-alpha-cluster | recursive | binding_energy | 97.1480 | 92.1617 | +5.41 % | 11169.8742 MeV (-720.6 ppm) |
| ${}^{13}$C | 13 | 7 | L3-partial-shell:f=0.250 from A=12$\to$16 | heuristic | binding_energy | 101.0622 | 97.1080 | +4.07 % | — |
| ${}^{14}$C | 14 | 8 | L?-pending | pending | binding_energy | — | 105.2845 | — | — |
| ${}^{15}$C | 15 | 9 | L?-pending | pending | binding_energy | — | 106.5025 | — | — |
| ${}^{16}$C | 16 | 10 | L?-pending | pending | binding_energy | — | 110.7529 | — | — |
| ${}^{17}$C | 17 | 11 | L?-pending | pending | binding_energy | — | 111.4864 | — | — |
| ${}^{18}$C | 18 | 12 | L?-pending | pending | binding_energy | — | 115.6704 | — | — |
| ${}^{19}$C | 19 | 13 | L?-pending | pending | binding_energy | — | 116.2472 | — | — |
| ${}^{20}$C | 20 | 14 | L?-pending | pending | binding_energy | — | 119.2287 | — | — |
| ${}^{21}$C | 21 | 15 | L?-pending | pending | binding_energy | — | 119.1540 | — | — |
| ${}^{22}$C | 22 | 16 | L?-pending | pending | binding_energy | — | 119.2637 | — | — |
| ${}^{23}$C | 23 | 17 | L?-pending | pending | binding_energy | — | 116.7710 | — | — |

### Nitrogen (Z = 7)

_2 of 16 isotopes with a framework prediction; 0 of 16 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{10}$N | 10 | 3 | L?-pending | pending | binding_energy | — | 36.4367 | — | — |
| ${}^{11}$N | 11 | 4 | L?-pending | pending | binding_energy | — | 58.9424 | — | — |
| ${}^{12}$N | 12 | 5 | L?-pending | pending | binding_energy | — | 74.0413 | — | — |
| ${}^{13}$N | 13 | 6 | L?-pending | pending | binding_energy | — | 94.1052 | — | — |
| ${}^{14}$N | 14 | 7 | L3-partial-shell:f=0.500 from A=12$\to$16 | heuristic | binding_energy | 109.9563 | 104.6586 | +5.06 % | — |
| ${}^{15}$N | 15 | 8 | L3-partial-shell:f=0.750 from A=12$\to$16 | heuristic | binding_energy | 118.8505 | 115.4919 | +2.91 % | — |
| ${}^{16}$N | 16 | 9 | L?-pending | pending | binding_energy | — | 117.9808 | — | — |
| ${}^{17}$N | 17 | 10 | L?-pending | pending | binding_energy | — | 123.8659 | — | — |
| ${}^{18}$N | 18 | 11 | L?-pending | pending | binding_energy | — | 126.6941 | — | — |
| ${}^{19}$N | 19 | 12 | L?-pending | pending | binding_energy | — | 132.0224 | — | — |
| ${}^{20}$N | 20 | 13 | L?-pending | pending | binding_energy | — | 134.1834 | — | — |
| ${}^{21}$N | 21 | 14 | L?-pending | pending | binding_energy | — | 138.7893 | — | — |
| ${}^{22}$N | 22 | 15 | L?-pending | pending | binding_energy | — | 140.3278 | — | — |
| ${}^{23}$N | 23 | 16 | L?-pending | pending | binding_energy | — | 143.4435 | — | — |
| ${}^{24}$N | 24 | 17 | L?-pending | pending | binding_energy | — | 141.2880 | — | — |
| ${}^{25}$N | 25 | 18 | L?-pending | pending | binding_energy | — | 140.3250 | — | — |

### Oxygen (Z = 8)

_3 of 18 isotopes with a framework prediction; 1 of 18 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{11}$O | 11 | 3 | L?-pending | pending | binding_energy | — | 34.7868 | — | — |
| ${}^{12}$O | 12 | 4 | L?-pending | pending | binding_energy | — | 58.5837 | — | — |
| ${}^{13}$O | 13 | 5 | L?-pending | pending | binding_energy | — | 75.5529 | — | — |
| ${}^{14}$O | 14 | 6 | L?-pending | pending | binding_energy | — | 98.7319 | — | — |
| ${}^{15}$O | 15 | 7 | L?-pending | pending | binding_energy | — | 111.9554 | — | — |
| ${}^{16}$O | 16 | 8 | L2-alpha-cluster | recursive | binding_energy | 134.3846 | 127.6193 | +5.30 % | 14888.3117 MeV (-728.7 ppm) |
| ${}^{17}$O | 17 | 9 | L3-partial-shell:f=0.250 from A=16$\to$20 | heuristic | binding_energy | 137.2455 | 131.7624 | +4.16 % | — |
| ${}^{18}$O | 18 | 10 | L3-partial-shell:f=0.500 from A=16$\to$20 | heuristic | binding_energy | 146.7464 | 139.8078 | +4.96 % | — |
| ${}^{19}$O | 19 | 11 | L?-pending | pending | binding_energy | — | 143.7634 | — | — |
| ${}^{20}$O | 20 | 12 | L?-pending | pending | binding_energy | — | 151.3714 | — | — |
| ${}^{21}$O | 21 | 13 | L?-pending | pending | binding_energy | — | 155.1769 | — | — |
| ${}^{22}$O | 22 | 14 | L?-pending | pending | binding_energy | — | 162.0272 | — | — |
| ${}^{23}$O | 23 | 15 | L?-pending | pending | binding_energy | — | 164.7602 | — | — |
| ${}^{24}$O | 24 | 16 | L?-pending | pending | binding_energy | — | 168.9525 | — | — |
| ${}^{25}$O | 25 | 17 | L?-pending | pending | binding_energy | — | 168.1951 | — | — |
| ${}^{26}$O | 26 | 18 | L?-pending | pending | binding_energy | — | 168.9345 | — | — |
| ${}^{27}$O | 27 | 19 | L?-pending | pending | binding_energy | — | 166.9950 | — | — |
| ${}^{28}$O | 28 | 20 | L?-pending | pending | binding_energy | — | 167.6640 | — | — |

### Fluorine (Z = 9)

_1 of 19 isotopes with a framework prediction; 0 of 19 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{13}$F | 13 | 4 | L?-pending | pending | binding_energy | — | 55.8610 | — | — |
| ${}^{14}$F | 14 | 5 | L?-pending | pending | binding_energy | — | 73.9929 | — | — |
| ${}^{15}$F | 15 | 6 | L?-pending | pending | binding_energy | — | 97.4619 | — | — |
| ${}^{16}$F | 16 | 7 | L?-pending | pending | binding_energy | — | 111.4248 | — | — |
| ${}^{17}$F | 17 | 8 | L?-pending | pending | binding_energy | — | 128.2196 | — | — |
| ${}^{18}$F | 18 | 9 | L?-pending | pending | binding_energy | — | 137.3695 | — | — |
| ${}^{19}$F | 19 | 10 | L3-partial-shell:f=0.750 from A=16$\to$20 | heuristic | binding_energy | 156.2474 | 147.8014 | +5.71 % | — |
| ${}^{20}$F | 20 | 11 | L?-pending | pending | binding_energy | — | 154.4027 | — | — |
| ${}^{21}$F | 21 | 12 | L?-pending | pending | binding_energy | — | 162.5042 | — | — |
| ${}^{22}$F | 22 | 13 | L?-pending | pending | binding_energy | — | 167.7345 | — | — |
| ${}^{23}$F | 23 | 14 | L?-pending | pending | binding_energy | — | 175.3139 | — | — |
| ${}^{24}$F | 24 | 15 | L?-pending | pending | binding_energy | — | 179.1260 | — | — |
| ${}^{25}$F | 25 | 16 | L?-pending | pending | binding_energy | — | 183.4077 | — | — |
| ${}^{26}$F | 26 | 17 | L?-pending | pending | binding_energy | — | 184.1385 | — | — |
| ${}^{27}$F | 27 | 18 | L?-pending | pending | binding_energy | — | 185.7510 | — | — |
| ${}^{28}$F | 28 | 19 | L?-pending | pending | binding_energy | — | 185.5520 | — | — |
| ${}^{29}$F | 29 | 20 | L?-pending | pending | binding_energy | — | 186.8769 | — | — |
| ${}^{30}$F | 30 | 21 | L?-pending | pending | binding_energy | — | 186.1500 | — | — |
| ${}^{31}$F | 31 | 22 | L?-pending | pending | binding_energy | — | 186.3410 | — | — |

### Neon (Z = 10)

_3 of 20 isotopes with a framework prediction; 1 of 20 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{15}$Ne | 15 | 5 | L?-pending | pending | binding_energy | — | 73.0309 | — | — |
| ${}^{16}$Ne | 16 | 6 | L?-pending | pending | binding_energy | — | 97.3308 | — | — |
| ${}^{17}$Ne | 17 | 7 | L?-pending | pending | binding_energy | — | 112.8885 | — | — |
| ${}^{18}$Ne | 18 | 8 | L?-pending | pending | binding_energy | — | 132.1426 | — | — |
| ${}^{19}$Ne | 19 | 9 | L?-pending | pending | binding_energy | — | 143.7795 | — | — |
| ${}^{20}$Ne | 20 | 10 | L2-alpha-cluster | recursive | binding_energy | 174.0483 | 160.6448 | +8.34 % | 18604.3221 MeV (-994.4 ppm) |
| ${}^{21}$Ne | 21 | 11 | L3-partial-shell:f=0.250 from A=20$\to$24 | heuristic | binding_energy | 175.8559 | 167.4060 | +5.05 % | — |
| ${}^{22}$Ne | 22 | 12 | L3-partial-shell:f=0.500 from A=20$\to$24 | heuristic | binding_energy | 185.9636 | 177.7702 | +4.61 % | — |
| ${}^{23}$Ne | 23 | 13 | L?-pending | pending | binding_energy | — | 182.9709 | — | — |
| ${}^{24}$Ne | 24 | 14 | L?-pending | pending | binding_energy | — | 191.8398 | — | — |
| ${}^{25}$Ne | 25 | 15 | L?-pending | pending | binding_energy | — | 195.9950 | — | — |
| ${}^{26}$Ne | 26 | 16 | L?-pending | pending | binding_energy | — | 201.5497 | — | — |
| ${}^{27}$Ne | 27 | 17 | L?-pending | pending | binding_energy | — | 203.0512 | — | — |
| ${}^{28}$Ne | 28 | 18 | L?-pending | pending | binding_energy | — | 206.8737 | — | — |
| ${}^{29}$Ne | 29 | 19 | L?-pending | pending | binding_energy | — | 207.8450 | — | — |
| ${}^{30}$Ne | 30 | 20 | L?-pending | pending | binding_energy | — | 211.0360 | — | — |
| ${}^{31}$Ne | 31 | 21 | L?-pending | pending | binding_energy | — | 211.2058 | — | — |
| ${}^{32}$Ne | 32 | 22 | L?-pending | pending | binding_energy | — | 213.4720 | — | — |
| ${}^{33}$Ne | 33 | 23 | L?-pending | pending | binding_energy | — | 212.3880 | — | — |
| ${}^{34}$Ne | 34 | 24 | L?-pending | pending | binding_energy | — | 213.7580 | — | — |

### Fermium (Z = 100)

_0 of 20 isotopes with a framework prediction; 0 of 20 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{241}$Fm | 241 | 141 | L?-pending | pending | binding_energy | — | 1797.6190 | — | — |
| ${}^{242}$Fm | 242 | 142 | L?-pending | pending | binding_energy | — | 1806.5300 | — | — |
| ${}^{243}$Fm | 243 | 143 | L?-pending | pending | binding_energy | — | 1813.7520 | — | — |
| ${}^{244}$Fm | 244 | 144 | L?-pending | pending | binding_energy | — | 1822.1920 | — | — |
| ${}^{245}$Fm | 245 | 145 | L?-pending | pending | binding_energy | — | 1828.9250 | — | — |
| ${}^{246}$Fm | 246 | 146 | L?-pending | pending | binding_energy | — | 1837.1184 | — | — |
| ${}^{247}$Fm | 247 | 147 | L?-pending | pending | binding_energy | — | 1843.6080 | — | — |
| ${}^{248}$Fm | 248 | 148 | L?-pending | pending | binding_energy | — | 1851.5544 | — | — |
| ${}^{249}$Fm | 249 | 149 | L?-pending | pending | binding_energy | — | 1858.0044 | — | — |
| ${}^{250}$Fm | 250 | 150 | L?-pending | pending | binding_energy | — | 1865.5226 | — | — |
| ${}^{251}$Fm | 251 | 151 | L?-pending | pending | binding_energy | — | 1871.7073 | — | — |
| ${}^{252}$Fm | 252 | 152 | L?-pending | pending | binding_energy | — | 1878.9208 | — | — |
| ${}^{253}$Fm | 253 | 153 | L?-pending | pending | binding_energy | — | 1884.4632 | — | — |
| ${}^{254}$Fm | 254 | 154 | L?-pending | pending | binding_energy | — | 1890.9776 | — | — |
| ${}^{255}$Fm | 255 | 155 | L?-pending | pending | binding_energy | — | 1896.1509 | — | — |
| ${}^{256}$Fm | 256 | 156 | L?-pending | pending | binding_energy | — | 1902.5379 | — | — |
| ${}^{257}$Fm | 257 | 157 | L?-pending | pending | binding_energy | — | 1907.5039 | — | — |
| ${}^{258}$Fm | 258 | 158 | L?-pending | pending | binding_energy | — | 1913.8440 | — | — |
| ${}^{259}$Fm | 259 | 159 | L?-pending | pending | binding_energy | — | 1918.4130 | — | — |
| ${}^{260}$Fm | 260 | 160 | L?-pending | pending | binding_energy | — | 1924.5200 | — | — |

### Mendelevium (Z = 101)

_0 of 19 isotopes with a framework prediction; 0 of 19 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{244}$Md | 244 | 143 | L?-pending | pending | binding_energy | — | 1814.8720 | — | — |
| ${}^{245}$Md | 245 | 144 | L?-pending | pending | binding_energy | — | 1823.0450 | — | — |
| ${}^{246}$Md | 246 | 145 | L?-pending | pending | binding_energy | — | 1830.4860 | — | — |
| ${}^{247}$Md | 247 | 146 | L?-pending | pending | binding_energy | — | 1838.6680 | — | — |
| ${}^{248}$Md | 248 | 147 | L?-pending | pending | binding_energy | — | 1845.6160 | — | — |
| ${}^{249}$Md | 249 | 148 | L?-pending | pending | binding_energy | — | 1853.5602 | — | — |
| ${}^{250}$Md | 250 | 149 | L?-pending | pending | binding_energy | — | 1860.4133 | — | — |
| ${}^{251}$Md | 251 | 150 | L?-pending | pending | binding_energy | — | 1867.9170 | — | — |
| ${}^{252}$Md | 252 | 151 | L?-pending | pending | binding_energy | — | 1874.4880 | — | — |
| ${}^{253}$Md | 253 | 152 | L?-pending | pending | binding_energy | — | 1881.8140 | — | — |
| ${}^{254}$Md | 254 | 153 | L?-pending | pending | binding_energy | — | 1887.7280 | — | — |
| ${}^{255}$Md | 255 | 154 | L?-pending | pending | binding_energy | — | 1894.3270 | — | — |
| ${}^{256}$Md | 256 | 155 | L?-pending | pending | binding_energy | — | 1899.7760 | — | — |
| ${}^{257}$Md | 257 | 156 | L?-pending | pending | binding_energy | — | 1906.3192 | — | — |
| ${}^{258}$Md | 258 | 157 | L?-pending | pending | binding_energy | — | 1911.6927 | — | — |
| ${}^{259}$Md | 259 | 158 | L?-pending | pending | binding_energy | — | 1917.8950 | — | — |
| ${}^{260}$Md | 260 | 159 | L?-pending | pending | binding_energy | — | 1922.9600 | — | — |
| ${}^{261}$Md | 261 | 160 | L?-pending | pending | binding_energy | — | 1929.0510 | — | — |
| ${}^{262}$Md | 262 | 161 | L?-pending | pending | binding_energy | — | 1934.0840 | — | — |

### Nobelium (Z = 102)

_0 of 17 isotopes with a framework prediction; 0 of 17 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{248}$No | 248 | 146 | L?-pending | pending | binding_energy | — | 1841.1520 | — | — |
| ${}^{249}$No | 249 | 147 | L?-pending | pending | binding_energy | — | 1848.0780 | — | — |
| ${}^{250}$No | 250 | 148 | L?-pending | pending | binding_energy | — | 1856.5000 | — | — |
| ${}^{251}$No | 251 | 149 | L?-pending | pending | binding_energy | — | 1863.1730 | — | — |
| ${}^{252}$No | 252 | 150 | L?-pending | pending | binding_energy | — | 1871.3014 | — | — |
| ${}^{253}$No | 253 | 151 | L?-pending | pending | binding_energy | — | 1877.8854 | — | — |
| ${}^{254}$No | 254 | 152 | L?-pending | pending | binding_energy | — | 1885.5921 | — | — |
| ${}^{255}$No | 255 | 153 | L?-pending | pending | binding_energy | — | 1891.5748 | — | — |
| ${}^{256}$No | 256 | 154 | L?-pending | pending | binding_energy | — | 1898.6350 | — | — |
| ${}^{257}$No | 257 | 155 | L?-pending | pending | binding_energy | — | 1904.2823 | — | — |
| ${}^{258}$No | 258 | 156 | L?-pending | pending | binding_energy | — | 1911.0060 | — | — |
| ${}^{259}$No | 259 | 157 | L?-pending | pending | binding_energy | — | 1916.5926 | — | — |
| ${}^{260}$No | 260 | 158 | L?-pending | pending | binding_energy | — | 1923.2200 | — | — |
| ${}^{261}$No | 261 | 159 | L?-pending | pending | binding_energy | — | 1928.2680 | — | — |
| ${}^{262}$No | 262 | 160 | L?-pending | pending | binding_energy | — | 1934.8700 | — | — |
| ${}^{263}$No | 263 | 161 | L?-pending | pending | binding_energy | — | 1939.8880 | — | — |
| ${}^{264}$No | 264 | 162 | L?-pending | pending | binding_energy | — | 1945.9440 | — | — |

### Lawrencium (Z = 103)

_0 of 16 isotopes with a framework prediction; 0 of 16 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{251}$Lr | 251 | 148 | L?-pending | pending | binding_energy | — | 1857.4000 | — | — |
| ${}^{252}$Lr | 252 | 149 | L?-pending | pending | binding_energy | — | 1864.8000 | — | — |
| ${}^{253}$Lr | 253 | 150 | L?-pending | pending | binding_energy | — | 1872.9383 | — | — |
| ${}^{254}$Lr | 254 | 151 | L?-pending | pending | binding_energy | — | 1879.8872 | — | — |
| ${}^{255}$Lr | 255 | 152 | L?-pending | pending | binding_energy | — | 1887.6571 | — | — |
| ${}^{256}$Lr | 256 | 153 | L?-pending | pending | binding_energy | — | 1893.9291 | — | — |
| ${}^{257}$Lr | 257 | 154 | L?-pending | pending | binding_energy | — | 1901.0290 | — | — |
| ${}^{258}$Lr | 258 | 155 | L?-pending | pending | binding_energy | — | 1907.1360 | — | — |
| ${}^{259}$Lr | 259 | 156 | L?-pending | pending | binding_energy | — | 1914.0100 | — | — |
| ${}^{260}$Lr | 260 | 157 | L?-pending | pending | binding_energy | — | 1919.5800 | — | — |
| ${}^{261}$Lr | 261 | 158 | L?-pending | pending | binding_energy | — | 1926.4410 | — | — |
| ${}^{262}$Lr | 262 | 159 | L?-pending | pending | binding_energy | — | 1931.9880 | — | — |
| ${}^{263}$Lr | 263 | 160 | L?-pending | pending | binding_energy | — | 1938.5730 | — | — |
| ${}^{264}$Lr | 264 | 161 | L?-pending | pending | binding_energy | — | 1943.8320 | — | — |
| ${}^{265}$Lr | 265 | 162 | L?-pending | pending | binding_energy | — | 1950.1350 | — | — |
| ${}^{266}$Lr | 266 | 163 | L?-pending | pending | binding_energy | — | 1954.8340 | — | — |

### Rutherfordium (Z = 104)

_0 of 16 isotopes with a framework prediction; 0 of 16 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{253}$Rf | 253 | 149 | L?-pending | pending | binding_energy | — | 1867.1400 | — | — |
| ${}^{254}$Rf | 254 | 150 | L?-pending | pending | binding_energy | — | 1875.5360 | — | — |
| ${}^{255}$Rf | 255 | 151 | L?-pending | pending | binding_energy | — | 1882.4100 | — | — |
| ${}^{256}$Rf | 256 | 152 | L?-pending | pending | binding_energy | — | 1890.6713 | — | — |
| ${}^{257}$Rf | 257 | 153 | L?-pending | pending | binding_energy | — | 1897.0983 | — | — |
| ${}^{258}$Rf | 258 | 154 | L?-pending | pending | binding_energy | — | 1904.6916 | — | — |
| ${}^{259}$Rf | 259 | 155 | L?-pending | pending | binding_energy | — | 1910.6430 | — | — |
| ${}^{260}$Rf | 260 | 156 | L?-pending | pending | binding_energy | — | 1918.0200 | — | — |
| ${}^{261}$Rf | 261 | 157 | L?-pending | pending | binding_energy | — | 1923.9317 | — | — |
| ${}^{262}$Rf | 262 | 158 | L?-pending | pending | binding_energy | — | 1930.9400 | — | — |
| ${}^{263}$Rf | 263 | 159 | L?-pending | pending | binding_energy | — | 1936.7320 | — | — |
| ${}^{264}$Rf | 264 | 160 | L?-pending | pending | binding_energy | — | 1943.3040 | — | — |
| ${}^{265}$Rf | 265 | 161 | L?-pending | pending | binding_energy | — | 1948.8100 | — | — |
| ${}^{266}$Rf | 266 | 162 | L?-pending | pending | binding_energy | — | 1955.3660 | — | — |
| ${}^{267}$Rf | 267 | 163 | L?-pending | pending | binding_energy | — | 1960.3140 | — | — |
| ${}^{268}$Rf | 268 | 164 | L?-pending | pending | binding_energy | — | 1966.3160 | — | — |

### Dubnium (Z = 105)

_0 of 16 isotopes with a framework prediction; 0 of 16 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{255}$Db | 255 | 150 | L?-pending | pending | binding_energy | — | 1876.5450 | — | — |
| ${}^{256}$Db | 256 | 151 | L?-pending | pending | binding_energy | — | 1883.9040 | — | — |
| ${}^{257}$Db | 257 | 152 | L?-pending | pending | binding_energy | — | 1892.0280 | — | — |
| ${}^{258}$Db | 258 | 153 | L?-pending | pending | binding_energy | — | 1898.7459 | — | — |
| ${}^{259}$Db | 259 | 154 | L?-pending | pending | binding_energy | — | 1906.3339 | — | — |
| ${}^{260}$Db | 260 | 155 | L?-pending | pending | binding_energy | — | 1912.8200 | — | — |
| ${}^{261}$Db | 261 | 156 | L?-pending | pending | binding_energy | — | 1920.1770 | — | — |
| ${}^{262}$Db | 262 | 157 | L?-pending | pending | binding_energy | — | 1926.2240 | — | — |
| ${}^{263}$Db | 263 | 158 | L?-pending | pending | binding_energy | — | 1933.5760 | — | — |
| ${}^{264}$Db | 264 | 159 | L?-pending | pending | binding_energy | — | 1939.3440 | — | — |
| ${}^{265}$Db | 265 | 160 | L?-pending | pending | binding_energy | — | 1946.4250 | — | — |
| ${}^{266}$Db | 266 | 161 | L?-pending | pending | binding_energy | — | 1952.1740 | — | — |
| ${}^{267}$Db | 267 | 162 | L?-pending | pending | binding_energy | — | 1958.9790 | — | — |
| ${}^{268}$Db | 268 | 163 | L?-pending | pending | binding_energy | — | 1963.9040 | — | — |
| ${}^{269}$Db | 269 | 164 | L?-pending | pending | binding_energy | — | 1969.8870 | — | — |
| ${}^{270}$Db | 270 | 165 | L?-pending | pending | binding_energy | — | 1974.7800 | — | — |

### Seaborgium (Z = 106)

_0 of 16 isotopes with a framework prediction; 0 of 16 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{258}$Sg | 258 | 152 | L?-pending | pending | binding_energy | — | 1894.2360 | — | — |
| ${}^{259}$Sg | 259 | 153 | L?-pending | pending | binding_energy | — | 1901.0600 | — | — |
| ${}^{260}$Sg | 260 | 154 | L?-pending | pending | binding_energy | — | 1909.0664 | — | — |
| ${}^{261}$Sg | 261 | 155 | L?-pending | pending | binding_energy | — | 1915.6802 | — | — |
| ${}^{262}$Sg | 262 | 156 | L?-pending | pending | binding_energy | — | 1923.3875 | — | — |
| ${}^{263}$Sg | 263 | 157 | L?-pending | pending | binding_energy | — | 1929.6310 | — | — |
| ${}^{264}$Sg | 264 | 158 | L?-pending | pending | binding_energy | — | 1937.2320 | — | — |
| ${}^{265}$Sg | 265 | 159 | L?-pending | pending | binding_energy | — | 1943.2450 | — | — |
| ${}^{266}$Sg | 266 | 160 | L?-pending | pending | binding_energy | — | 1950.3120 | — | — |
| ${}^{267}$Sg | 267 | 161 | L?-pending | pending | binding_energy | — | 1956.3090 | — | — |
| ${}^{268}$Sg | 268 | 162 | L?-pending | pending | binding_energy | — | 1963.3680 | — | — |
| ${}^{269}$Sg | 269 | 163 | L?-pending | pending | binding_energy | — | 1968.5420 | — | — |
| ${}^{270}$Sg | 270 | 164 | L?-pending | pending | binding_energy | — | 1974.7800 | — | — |
| ${}^{271}$Sg | 271 | 165 | L?-pending | pending | binding_energy | — | 1979.6550 | — | — |
| ${}^{272}$Sg | 272 | 166 | L?-pending | pending | binding_energy | — | 1985.8720 | — | — |
| ${}^{273}$Sg | 273 | 167 | L?-pending | pending | binding_energy | — | 1990.7160 | — | — |

### Bohrium (Z = 107)

_0 of 19 isotopes with a framework prediction; 0 of 19 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{260}$Bh | 260 | 153 | L?-pending | pending | binding_energy | — | 1901.6400 | — | — |
| ${}^{261}$Bh | 261 | 154 | L?-pending | pending | binding_energy | — | 1909.8235 | — | — |
| ${}^{262}$Bh | 262 | 155 | L?-pending | pending | binding_energy | — | 1916.7221 | — | — |
| ${}^{263}$Bh | 263 | 156 | L?-pending | pending | binding_energy | — | 1924.6340 | — | — |
| ${}^{264}$Bh | 264 | 157 | L?-pending | pending | binding_energy | — | 1931.1600 | — | — |
| ${}^{265}$Bh | 265 | 158 | L?-pending | pending | binding_energy | — | 1938.7400 | — | — |
| ${}^{266}$Bh | 266 | 159 | L?-pending | pending | binding_energy | — | 1945.2580 | — | — |
| ${}^{267}$Bh | 267 | 160 | L?-pending | pending | binding_energy | — | 1952.5710 | — | — |
| ${}^{268}$Bh | 268 | 161 | L?-pending | pending | binding_energy | — | 1958.8120 | — | — |
| ${}^{269}$Bh | 269 | 162 | L?-pending | pending | binding_energy | — | 1966.1210 | — | — |
| ${}^{270}$Bh | 270 | 163 | L?-pending | pending | binding_energy | — | 1971.2700 | — | — |
| ${}^{271}$Bh | 271 | 164 | L?-pending | pending | binding_energy | — | 1977.7580 | — | — |
| ${}^{272}$Bh | 272 | 165 | L?-pending | pending | binding_energy | — | 1982.8800 | — | — |
| ${}^{273}$Bh | 273 | 166 | L?-pending | pending | binding_energy | — | 1989.0780 | — | — |
| ${}^{274}$Bh | 274 | 167 | L?-pending | pending | binding_energy | — | 1994.1720 | — | — |
| ${}^{275}$Bh | 275 | 168 | L?-pending | pending | binding_energy | — | 2000.0750 | — | — |
| ${}^{276}$Bh | 276 | 169 | L?-pending | pending | binding_energy | — | 2005.1400 | — | — |
| ${}^{277}$Bh | 277 | 170 | L?-pending | pending | binding_energy | — | 2011.0200 | — | — |
| ${}^{278}$Bh | 278 | 171 | L?-pending | pending | binding_energy | — | 2015.7780 | — | — |

### Hassium (Z = 108)

_0 of 18 isotopes with a framework prediction; 0 of 18 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{263}$Hs | 263 | 155 | L?-pending | pending | binding_energy | — | 1918.5850 | — | — |
| ${}^{264}$Hs | 264 | 156 | L?-pending | pending | binding_energy | — | 1926.7713 | — | — |
| ${}^{265}$Hs | 265 | 157 | L?-pending | pending | binding_energy | — | 1933.5056 | — | — |
| ${}^{266}$Hs | 266 | 158 | L?-pending | pending | binding_energy | — | 1941.3375 | — | — |
| ${}^{267}$Hs | 267 | 159 | L?-pending | pending | binding_energy | — | 1947.7650 | — | — |
| ${}^{268}$Hs | 268 | 160 | L?-pending | pending | binding_energy | — | 1955.5960 | — | — |
| ${}^{269}$Hs | 269 | 161 | L?-pending | pending | binding_energy | — | 1962.0860 | — | — |
| ${}^{270}$Hs | 270 | 162 | L?-pending | pending | binding_energy | — | 1969.6500 | — | — |
| ${}^{271}$Hs | 271 | 163 | L?-pending | pending | binding_energy | — | 1975.0480 | — | — |
| ${}^{272}$Hs | 272 | 164 | L?-pending | pending | binding_energy | — | 1981.7920 | — | — |
| ${}^{273}$Hs | 273 | 165 | L?-pending | pending | binding_energy | — | 1987.1670 | — | — |
| ${}^{274}$Hs | 274 | 166 | L?-pending | pending | binding_energy | — | 1993.6240 | — | — |
| ${}^{275}$Hs | 275 | 167 | L?-pending | pending | binding_energy | — | 1998.7000 | — | — |
| ${}^{276}$Hs | 276 | 168 | L?-pending | pending | binding_energy | — | 2005.1400 | — | — |
| ${}^{277}$Hs | 277 | 169 | L?-pending | pending | binding_energy | — | 2009.9120 | — | — |
| ${}^{278}$Hs | 278 | 170 | L?-pending | pending | binding_energy | — | 2016.0560 | — | — |
| ${}^{279}$Hs | 279 | 171 | L?-pending | pending | binding_energy | — | 2020.7970 | — | — |
| ${}^{280}$Hs | 280 | 172 | L?-pending | pending | binding_energy | — | 2026.9200 | — | — |

### Meitnerium (Z = 109)

_0 of 18 isotopes with a framework prediction; 0 of 18 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{265}$Mt | 265 | 156 | L?-pending | pending | binding_energy | — | 1927.0800 | — | — |
| ${}^{266}$Mt | 266 | 157 | L?-pending | pending | binding_energy | — | 1934.0221 | — | — |
| ${}^{267}$Mt | 267 | 158 | L?-pending | pending | binding_energy | — | 1941.8910 | — | — |
| ${}^{268}$Mt | 268 | 159 | L?-pending | pending | binding_energy | — | 1948.6280 | — | — |
| ${}^{269}$Mt | 269 | 160 | L?-pending | pending | binding_energy | — | 1956.7060 | — | — |
| ${}^{270}$Mt | 270 | 161 | L?-pending | pending | binding_energy | — | 1963.1700 | — | — |
| ${}^{271}$Mt | 271 | 162 | L?-pending | pending | binding_energy | — | 1970.9830 | — | — |
| ${}^{272}$Mt | 272 | 163 | L?-pending | pending | binding_energy | — | 1976.6240 | — | — |
| ${}^{273}$Mt | 273 | 164 | L?-pending | pending | binding_energy | — | 1983.3450 | — | — |
| ${}^{274}$Mt | 274 | 165 | L?-pending | pending | binding_energy | — | 1988.9660 | — | — |
| ${}^{275}$Mt | 275 | 166 | L?-pending | pending | binding_energy | — | 1995.6750 | — | — |
| ${}^{276}$Mt | 276 | 167 | L?-pending | pending | binding_energy | — | 2001.0000 | — | — |
| ${}^{277}$Mt | 277 | 168 | L?-pending | pending | binding_energy | — | 2007.4190 | — | — |
| ${}^{278}$Mt | 278 | 169 | L?-pending | pending | binding_energy | — | 2012.7200 | — | — |
| ${}^{279}$Mt | 279 | 170 | L?-pending | pending | binding_energy | — | 2019.1230 | — | — |
| ${}^{280}$Mt | 280 | 171 | L?-pending | pending | binding_energy | — | 2024.1200 | — | — |
| ${}^{281}$Mt | 281 | 172 | L?-pending | pending | binding_energy | — | 2030.2250 | — | — |
| ${}^{282}$Mt | 282 | 173 | L?-pending | pending | binding_energy | — | 2035.4760 | — | — |

### Sodium (Z = 11)

_0 of 23 isotopes with a framework prediction; 0 of 23 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{17}$Na | 17 | 6 | L?-pending | pending | binding_energy | — | 93.8870 | — | — |
| ${}^{18}$Na | 18 | 7 | L?-pending | pending | binding_energy | — | 111.6399 | — | — |
| ${}^{19}$Na | 19 | 8 | L?-pending | pending | binding_energy | — | 131.8198 | — | — |
| ${}^{20}$Na | 20 | 9 | L?-pending | pending | binding_energy | — | 145.9701 | — | — |
| ${}^{21}$Na | 21 | 10 | L?-pending | pending | binding_energy | — | 163.0767 | — | — |
| ${}^{22}$Na | 22 | 11 | L?-pending | pending | binding_energy | — | 174.1446 | — | — |
| ${}^{23}$Na | 23 | 12 | L?-pending | pending | binding_energy | — | 186.5644 | — | — |
| ${}^{24}$Na | 24 | 13 | L?-pending | pending | binding_energy | — | 193.5237 | — | — |
| ${}^{25}$Na | 25 | 14 | L?-pending | pending | binding_energy | — | 202.5349 | — | — |
| ${}^{26}$Na | 26 | 15 | L?-pending | pending | binding_energy | — | 208.1092 | — | — |
| ${}^{27}$Na | 27 | 16 | L?-pending | pending | binding_energy | — | 214.8376 | — | — |
| ${}^{28}$Na | 28 | 17 | L?-pending | pending | binding_energy | — | 218.3794 | — | — |
| ${}^{29}$Na | 29 | 18 | L?-pending | pending | binding_energy | — | 222.7824 | — | — |
| ${}^{30}$Na | 30 | 19 | L?-pending | pending | binding_energy | — | 225.0591 | — | — |
| ${}^{31}$Na | 31 | 20 | L?-pending | pending | binding_energy | — | 229.3590 | — | — |
| ${}^{32}$Na | 32 | 21 | L?-pending | pending | binding_energy | — | 231.0362 | — | — |
| ${}^{33}$Na | 33 | 22 | L?-pending | pending | binding_energy | — | 233.9676 | — | — |
| ${}^{34}$Na | 34 | 23 | L?-pending | pending | binding_energy | — | 234.1389 | — | — |
| ${}^{35}$Na | 35 | 24 | L?-pending | pending | binding_energy | — | 236.0750 | — | — |
| ${}^{36}$Na | 36 | 25 | L?-pending | pending | binding_energy | — | 236.0520 | — | — |
| ${}^{37}$Na | 37 | 26 | L?-pending | pending | binding_energy | — | 236.9110 | — | — |
| ${}^{38}$Na | 38 | 27 | L?-pending | pending | binding_energy | — | 236.2080 | — | — |
| ${}^{39}$Na | 39 | 28 | L?-pending | pending | binding_energy | — | 236.1840 | — | — |

### Darmstadtium (Z = 110)

_0 of 18 isotopes with a framework prediction; 0 of 18 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{267}$Ds | 267 | 157 | L?-pending | pending | binding_energy | — | 1935.2160 | — | — |
| ${}^{268}$Ds | 268 | 158 | L?-pending | pending | binding_energy | — | 1943.5360 | — | — |
| ${}^{269}$Ds | 269 | 159 | L?-pending | pending | binding_energy | — | 1950.2917 | — | — |
| ${}^{270}$Ds | 270 | 160 | L?-pending | pending | binding_energy | — | 1958.5161 | — | — |
| ${}^{271}$Ds | 271 | 161 | L?-pending | pending | binding_energy | — | 1965.2920 | — | — |
| ${}^{272}$Ds | 272 | 162 | L?-pending | pending | binding_energy | — | 1973.3600 | — | — |
| ${}^{273}$Ds | 273 | 163 | L?-pending | pending | binding_energy | — | 1979.2500 | — | — |
| ${}^{274}$Ds | 274 | 164 | L?-pending | pending | binding_energy | — | 1986.2260 | — | — |
| ${}^{275}$Ds | 275 | 165 | L?-pending | pending | binding_energy | — | 1991.8250 | — | — |
| ${}^{276}$Ds | 276 | 166 | L?-pending | pending | binding_energy | — | 1999.0680 | — | — |
| ${}^{277}$Ds | 277 | 167 | L?-pending | pending | binding_energy | — | 2004.6490 | — | — |
| ${}^{278}$Ds | 278 | 168 | L?-pending | pending | binding_energy | — | 2011.6080 | — | — |
| ${}^{279}$Ds | 279 | 169 | L?-pending | pending | binding_energy | — | 2016.8910 | — | — |
| ${}^{280}$Ds | 280 | 170 | L?-pending | pending | binding_energy | — | 2023.5600 | — | — |
| ${}^{281}$Ds | 281 | 171 | L?-pending | pending | binding_energy | — | 2028.8200 | — | — |
| ${}^{282}$Ds | 282 | 172 | L?-pending | pending | binding_energy | — | 2035.1940 | — | — |
| ${}^{283}$Ds | 283 | 173 | L?-pending | pending | binding_energy | — | 2040.4300 | — | — |
| ${}^{284}$Ds | 284 | 174 | L?-pending | pending | binding_energy | — | 2046.7880 | — | — |

### Roentgenium (Z = 111)

_0 of 15 isotopes with a framework prediction; 0 of 15 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{272}$Rg | 272 | 161 | L?-pending | pending | binding_energy | — | 1965.7440 | — | — |
| ${}^{273}$Rg | 273 | 162 | L?-pending | pending | binding_energy | — | 1973.7900 | — | — |
| ${}^{274}$Rg | 274 | 163 | L?-pending | pending | binding_energy | — | 1980.1980 | — | — |
| ${}^{275}$Rg | 275 | 164 | L?-pending | pending | binding_energy | — | 1987.4250 | — | — |
| ${}^{276}$Rg | 276 | 165 | L?-pending | pending | binding_energy | — | 1993.5480 | — | — |
| ${}^{277}$Rg | 277 | 166 | L?-pending | pending | binding_energy | — | 2000.4940 | — | — |
| ${}^{278}$Rg | 278 | 167 | L?-pending | pending | binding_energy | — | 2006.6040 | — | — |
| ${}^{279}$Rg | 279 | 168 | L?-pending | pending | binding_energy | — | 2013.2640 | — | — |
| ${}^{280}$Rg | 280 | 169 | L?-pending | pending | binding_energy | — | 2019.3600 | — | — |
| ${}^{281}$Rg | 281 | 170 | L?-pending | pending | binding_energy | — | 2025.7290 | — | — |
| ${}^{282}$Rg | 282 | 171 | L?-pending | pending | binding_energy | — | 2031.5280 | — | — |
| ${}^{283}$Rg | 283 | 172 | L?-pending | pending | binding_energy | — | 2037.8830 | — | — |
| ${}^{284}$Rg | 284 | 173 | L?-pending | pending | binding_energy | — | 2043.3800 | — | — |
| ${}^{285}$Rg | 285 | 174 | L?-pending | pending | binding_energy | — | 2049.7200 | — | — |
| ${}^{286}$Rg | 286 | 175 | L?-pending | pending | binding_energy | — | 2054.9100 | — | — |

### Copernicium (Z = 112)

_0 of 13 isotopes with a framework prediction; 0 of 13 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{276}$Cn | 276 | 164 | L?-pending | pending | binding_energy | — | 1989.6840 | — | — |
| ${}^{277}$Cn | 277 | 165 | L?-pending | pending | binding_energy | — | 1995.7850 | — | — |
| ${}^{278}$Cn | 278 | 166 | L?-pending | pending | binding_energy | — | 2003.2680 | — | — |
| ${}^{279}$Cn | 279 | 167 | L?-pending | pending | binding_energy | — | 2009.3580 | — | — |
| ${}^{280}$Cn | 280 | 168 | L?-pending | pending | binding_energy | — | 2016.5600 | — | — |
| ${}^{281}$Cn | 281 | 169 | L?-pending | pending | binding_energy | — | 2022.3570 | — | — |
| ${}^{282}$Cn | 282 | 170 | L?-pending | pending | binding_energy | — | 2029.5540 | — | — |
| ${}^{283}$Cn | 283 | 171 | L?-pending | pending | binding_energy | — | 2035.3360 | — | — |
| ${}^{284}$Cn | 284 | 172 | L?-pending | pending | binding_energy | — | 2042.2440 | — | — |
| ${}^{285}$Cn | 285 | 173 | L?-pending | pending | binding_energy | — | 2047.7250 | — | — |
| ${}^{286}$Cn | 286 | 174 | L?-pending | pending | binding_energy | — | 2054.3380 | — | — |
| ${}^{287}$Cn | 287 | 175 | L?-pending | pending | binding_energy | — | 2059.5120 | — | — |
| ${}^{288}$Cn | 288 | 176 | L?-pending | pending | binding_energy | — | 2066.1120 | — | — |

### Nihonium (Z = 113)

_0 of 13 isotopes with a framework prediction; 0 of 13 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{278}$Nh | 278 | 165 | L?-pending | pending | binding_energy | — | 1996.3180 | — | — |
| ${}^{279}$Nh | 279 | 166 | L?-pending | pending | binding_energy | — | 2004.0570 | — | — |
| ${}^{280}$Nh | 280 | 167 | L?-pending | pending | binding_energy | — | 2010.4000 | — | — |
| ${}^{281}$Nh | 281 | 168 | L?-pending | pending | binding_energy | — | 2017.8610 | — | — |
| ${}^{282}$Nh | 282 | 169 | L?-pending | pending | binding_energy | — | 2023.9140 | — | — |
| ${}^{283}$Nh | 283 | 170 | L?-pending | pending | binding_energy | — | 2031.0910 | — | — |
| ${}^{284}$Nh | 284 | 171 | L?-pending | pending | binding_energy | — | 2037.1320 | — | — |
| ${}^{285}$Nh | 285 | 172 | L?-pending | pending | binding_energy | — | 2044.0200 | — | — |
| ${}^{286}$Nh | 286 | 173 | L?-pending | pending | binding_energy | — | 2050.0480 | — | — |
| ${}^{287}$Nh | 287 | 174 | L?-pending | pending | binding_energy | — | 2056.6420 | — | — |
| ${}^{288}$Nh | 288 | 175 | L?-pending | pending | binding_energy | — | 2062.0800 | — | — |
| ${}^{289}$Nh | 289 | 176 | L?-pending | pending | binding_energy | — | 2068.6620 | — | — |
| ${}^{290}$Nh | 290 | 177 | L?-pending | pending | binding_energy | — | 2074.0800 | — | — |

### Flerovium (Z = 114)

_0 of 8 isotopes with a framework prediction; 0 of 8 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{284}$Fl | 284 | 170 | L?-pending | pending | binding_energy | — | 2034.2920 | — | — |
| ${}^{285}$Fl | 285 | 171 | L?-pending | pending | binding_energy | — | 2040.3150 | — | — |
| ${}^{286}$Fl | 286 | 172 | L?-pending | pending | binding_energy | — | 2047.4740 | — | — |
| ${}^{287}$Fl | 287 | 173 | L?-pending | pending | binding_energy | — | 2053.4850 | — | — |
| ${}^{288}$Fl | 288 | 174 | L?-pending | pending | binding_energy | — | 2060.3520 | — | — |
| ${}^{289}$Fl | 289 | 175 | L?-pending | pending | binding_energy | — | 2066.0610 | — | — |
| ${}^{290}$Fl | 290 | 176 | L?-pending | pending | binding_energy | — | 2072.6300 | — | — |
| ${}^{291}$Fl | 291 | 177 | L?-pending | pending | binding_energy | — | 2078.0310 | — | — |

### Moscovium (Z = 115)

_0 of 6 isotopes with a framework prediction; 0 of 6 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{287}$Mc | 287 | 172 | L?-pending | pending | binding_energy | — | 2048.8930 | — | — |
| ${}^{288}$Mc | 288 | 173 | L?-pending | pending | binding_energy | — | 2054.8800 | — | — |
| ${}^{289}$Mc | 289 | 174 | L?-pending | pending | binding_energy | — | 2062.0150 | — | — |
| ${}^{290}$Mc | 290 | 175 | L?-pending | pending | binding_energy | — | 2067.9900 | — | — |
| ${}^{291}$Mc | 291 | 176 | L?-pending | pending | binding_energy | — | 2074.5390 | — | — |
| ${}^{292}$Mc | 292 | 177 | L?-pending | pending | binding_energy | — | 2080.2080 | — | — |

### Livermorium (Z = 116)

_0 of 5 isotopes with a framework prediction; 0 of 5 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{289}$Lv | 289 | 173 | L?-pending | pending | binding_energy | — | 2057.3910 | — | — |
| ${}^{290}$Lv | 290 | 174 | L?-pending | pending | binding_energy | — | 2064.8000 | — | — |
| ${}^{291}$Lv | 291 | 175 | L?-pending | pending | binding_energy | — | 2070.7560 | — | — |
| ${}^{292}$Lv | 292 | 176 | L?-pending | pending | binding_energy | — | 2077.8720 | — | — |
| ${}^{293}$Lv | 293 | 177 | L?-pending | pending | binding_energy | — | 2083.5230 | — | — |

### Tennessine (Z = 117)

_0 of 4 isotopes with a framework prediction; 0 of 4 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{291}$Ts | 291 | 174 | L?-pending | pending | binding_energy | — | 2065.5180 | — | — |
| ${}^{292}$Ts | 292 | 175 | L?-pending | pending | binding_energy | — | 2071.7400 | — | — |
| ${}^{293}$Ts | 293 | 176 | L?-pending | pending | binding_energy | — | 2078.8350 | — | — |
| ${}^{294}$Ts | 294 | 177 | L?-pending | pending | binding_energy | — | 2085.0480 | — | — |

### Oganesson (Z = 118)

_0 of 3 isotopes with a framework prediction; 0 of 3 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{293}$Og | 293 | 175 | L?-pending | pending | binding_energy | — | 2073.8540 | — | — |
| ${}^{294}$Og | 294 | 176 | L?-pending | pending | binding_energy | — | 2081.2260 | — | — |
| ${}^{295}$Og | 295 | 177 | L?-pending | pending | binding_energy | — | 2087.4200 | — | — |

### Magnesium (Z = 12)

_1 of 23 isotopes with a framework prediction; 1 of 23 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{19}$Mg | 19 | 7 | L?-pending | pending | binding_energy | — | 112.1285 | — | — |
| ${}^{20}$Mg | 20 | 8 | L?-pending | pending | binding_energy | — | 134.5605 | — | — |
| ${}^{21}$Mg | 21 | 9 | L?-pending | pending | binding_energy | — | 149.2057 | — | — |
| ${}^{22}$Mg | 22 | 10 | L?-pending | pending | binding_energy | — | 168.5808 | — | — |
| ${}^{23}$Mg | 23 | 11 | L?-pending | pending | binding_energy | — | 181.7258 | — | — |
| ${}^{24}$Mg | 24 | 12 | L2-alpha-cluster | recursive | binding_energy | 216.1389 | 198.2570 | +9.02 % | 22317.9055 MeV (-1075.1 ppm) |
| ${}^{25}$Mg | 25 | 13 | L?-pending | pending | binding_energy | — | 205.5876 | — | — |
| ${}^{26}$Mg | 26 | 14 | L?-pending | pending | binding_energy | — | 216.6806 | — | — |
| ${}^{27}$Mg | 27 | 15 | L?-pending | pending | binding_energy | — | 223.1240 | — | — |
| ${}^{28}$Mg | 28 | 16 | L?-pending | pending | binding_energy | — | 231.6287 | — | — |
| ${}^{29}$Mg | 29 | 17 | L?-pending | pending | binding_energy | — | 235.2924 | — | — |
| ${}^{30}$Mg | 30 | 18 | L?-pending | pending | binding_energy | — | 241.6327 | — | — |
| ${}^{31}$Mg | 31 | 19 | L?-pending | pending | binding_energy | — | 243.9448 | — | — |
| ${}^{32}$Mg | 32 | 20 | L?-pending | pending | binding_energy | — | 249.7229 | — | — |
| ${}^{33}$Mg | 33 | 21 | L?-pending | pending | binding_energy | — | 252.0025 | — | — |
| ${}^{34}$Mg | 34 | 22 | L?-pending | pending | binding_energy | — | 256.7133 | — | — |
| ${}^{35}$Mg | 35 | 23 | L?-pending | pending | binding_energy | — | 257.4682 | — | — |
| ${}^{36}$Mg | 36 | 24 | L?-pending | pending | binding_energy | — | 260.7991 | — | — |
| ${}^{37}$Mg | 37 | 25 | L?-pending | pending | binding_energy | — | 261.0391 | — | — |
| ${}^{38}$Mg | 38 | 26 | L?-pending | pending | binding_energy | — | 263.2640 | — | — |
| ${}^{39}$Mg | 39 | 27 | L?-pending | pending | binding_energy | — | 262.6260 | — | — |
| ${}^{40}$Mg | 40 | 28 | L?-pending | pending | binding_energy | — | 263.9200 | — | — |
| ${}^{41}$Mg | 41 | 29 | L?-pending | pending | binding_energy | — | 263.4250 | — | — |

### Aluminium (Z = 13)

_0 of 23 isotopes with a framework prediction; 0 of 23 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{21}$Al | 21 | 8 | L?-pending | pending | binding_energy | — | 132.2370 | — | — |
| ${}^{22}$Al | 22 | 9 | L?-pending | pending | binding_energy | — | 149.2040 | — | — |
| ${}^{23}$Al | 23 | 10 | L?-pending | pending | binding_energy | — | 168.7217 | — | — |
| ${}^{24}$Al | 24 | 11 | L?-pending | pending | binding_energy | — | 183.5899 | — | — |
| ${}^{25}$Al | 25 | 12 | L?-pending | pending | binding_energy | — | 200.5284 | — | — |
| ${}^{26}$Al | 26 | 13 | L?-pending | pending | binding_energy | — | 211.8939 | — | — |
| ${}^{27}$Al | 27 | 14 | L?-pending | pending | binding_energy | — | 224.9519 | — | — |
| ${}^{28}$Al | 28 | 15 | L?-pending | pending | binding_energy | — | 232.6771 | — | — |
| ${}^{29}$Al | 29 | 16 | L?-pending | pending | binding_energy | — | 242.1055 | — | — |
| ${}^{30}$Al | 30 | 17 | L?-pending | pending | binding_energy | — | 247.8331 | — | — |
| ${}^{31}$Al | 31 | 18 | L?-pending | pending | binding_energy | — | 254.9911 | — | — |
| ${}^{32}$Al | 32 | 19 | L?-pending | pending | binding_energy | — | 259.2110 | — | — |
| ${}^{33}$Al | 33 | 20 | L?-pending | pending | binding_energy | — | 264.6804 | — | — |
| ${}^{34}$Al | 34 | 21 | L?-pending | pending | binding_energy | — | 267.2519 | — | — |
| ${}^{35}$Al | 35 | 22 | L?-pending | pending | binding_energy | — | 272.5494 | — | — |
| ${}^{36}$Al | 36 | 23 | L?-pending | pending | binding_energy | — | 274.4466 | — | — |
| ${}^{37}$Al | 37 | 24 | L?-pending | pending | binding_energy | — | 278.6587 | — | — |
| ${}^{38}$Al | 38 | 25 | L?-pending | pending | binding_energy | — | 280.0600 | — | — |
| ${}^{39}$Al | 39 | 26 | L?-pending | pending | binding_energy | — | 283.1400 | — | — |
| ${}^{40}$Al | 40 | 27 | L?-pending | pending | binding_energy | — | 283.8800 | — | — |
| ${}^{41}$Al | 41 | 28 | L?-pending | pending | binding_energy | — | 286.1800 | — | — |
| ${}^{42}$Al | 42 | 29 | L?-pending | pending | binding_energy | — | 286.8180 | — | — |
| ${}^{43}$Al | 43 | 30 | L?-pending | pending | binding_energy | — | 288.6160 | — | — |

### Silicon (Z = 14)

_0 of 24 isotopes with a framework prediction; 0 of 24 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{22}$Si | 22 | 8 | L?-pending | pending | binding_energy | — | 132.9680 | — | — |
| ${}^{23}$Si | 23 | 9 | L?-pending | pending | binding_energy | — | 150.7420 | — | — |
| ${}^{24}$Si | 24 | 10 | L?-pending | pending | binding_energy | — | 172.0136 | — | — |
| ${}^{25}$Si | 25 | 11 | L?-pending | pending | binding_energy | — | 187.0028 | — | — |
| ${}^{26}$Si | 26 | 12 | L?-pending | pending | binding_energy | — | 206.0424 | — | — |
| ${}^{27}$Si | 27 | 13 | L?-pending | pending | binding_energy | — | 219.3572 | — | — |
| ${}^{28}$Si | 28 | 14 | L?-pending | pending | binding_energy | — | 236.5368 | — | — |
| ${}^{29}$Si | 29 | 15 | L?-pending | pending | binding_energy | — | 245.0104 | — | — |
| ${}^{30}$Si | 30 | 16 | L?-pending | pending | binding_energy | — | 255.6196 | — | — |
| ${}^{31}$Si | 31 | 17 | L?-pending | pending | binding_energy | — | 262.2070 | — | — |
| ${}^{32}$Si | 32 | 18 | L?-pending | pending | binding_energy | — | 271.4070 | — | — |
| ${}^{33}$Si | 33 | 19 | L?-pending | pending | binding_energy | — | 275.9150 | — | — |
| ${}^{34}$Si | 34 | 20 | L?-pending | pending | binding_energy | — | 283.4636 | — | — |
| ${}^{35}$Si | 35 | 21 | L?-pending | pending | binding_energy | — | 285.9348 | — | — |
| ${}^{36}$Si | 36 | 22 | L?-pending | pending | binding_energy | — | 292.0507 | — | — |
| ${}^{37}$Si | 37 | 23 | L?-pending | pending | binding_energy | — | 294.2574 | — | — |
| ${}^{38}$Si | 38 | 24 | L?-pending | pending | binding_energy | — | 299.9275 | — | — |
| ${}^{39}$Si | 39 | 25 | L?-pending | pending | binding_energy | — | 301.5082 | — | — |
| ${}^{40}$Si | 40 | 26 | L?-pending | pending | binding_energy | — | 306.2330 | — | — |
| ${}^{41}$Si | 41 | 27 | L?-pending | pending | binding_energy | — | 306.7620 | — | — |
| ${}^{42}$Si | 42 | 28 | L?-pending | pending | binding_energy | — | 311.2200 | — | — |
| ${}^{43}$Si | 43 | 29 | L?-pending | pending | binding_energy | — | 311.7930 | — | — |
| ${}^{44}$Si | 44 | 30 | L?-pending | pending | binding_energy | — | 314.8640 | — | — |
| ${}^{45}$Si | 45 | 31 | L?-pending | pending | binding_energy | — | 315.1800 | — | — |

### Phosphorus (Z = 15)

_0 of 24 isotopes with a framework prediction; 0 of 24 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{24}$P | 24 | 9 | L?-pending | pending | binding_energy | — | 147.9600 | — | — |
| ${}^{25}$P | 25 | 10 | L?-pending | pending | binding_energy | — | 169.8500 | — | — |
| ${}^{26}$P | 26 | 11 | L?-pending | pending | binding_energy | — | 187.1480 | — | — |
| ${}^{27}$P | 27 | 12 | L?-pending | pending | binding_energy | — | 206.8494 | — | — |
| ${}^{28}$P | 28 | 13 | L?-pending | pending | binding_energy | — | 221.4096 | — | — |
| ${}^{29}$P | 29 | 14 | L?-pending | pending | binding_energy | — | 239.2859 | — | — |
| ${}^{30}$P | 30 | 15 | L?-pending | pending | binding_energy | — | 250.6052 | — | — |
| ${}^{31}$P | 31 | 16 | L?-pending | pending | binding_energy | — | 262.9162 | — | — |
| ${}^{32}$P | 32 | 17 | L?-pending | pending | binding_energy | — | 270.8518 | — | — |
| ${}^{33}$P | 33 | 18 | L?-pending | pending | binding_energy | — | 280.9556 | — | — |
| ${}^{34}$P | 34 | 19 | L?-pending | pending | binding_energy | — | 287.2383 | — | — |
| ${}^{35}$P | 35 | 20 | L?-pending | pending | binding_energy | — | 295.6187 | — | — |
| ${}^{36}$P | 36 | 21 | L?-pending | pending | binding_energy | — | 299.0833 | — | — |
| ${}^{37}$P | 37 | 22 | L?-pending | pending | binding_energy | — | 305.8996 | — | — |
| ${}^{38}$P | 38 | 23 | L?-pending | pending | binding_energy | — | 309.5964 | — | — |
| ${}^{39}$P | 39 | 24 | L?-pending | pending | binding_energy | — | 315.8208 | — | — |
| ${}^{40}$P | 40 | 25 | L?-pending | pending | binding_energy | — | 319.2567 | — | — |
| ${}^{41}$P | 41 | 26 | L?-pending | pending | binding_energy | — | 324.1686 | — | — |
| ${}^{42}$P | 42 | 27 | L?-pending | pending | binding_energy | — | 326.1683 | — | — |
| ${}^{43}$P | 43 | 28 | L?-pending | pending | binding_energy | — | 330.2830 | — | — |
| ${}^{44}$P | 44 | 29 | L?-pending | pending | binding_energy | — | 332.2880 | — | — |
| ${}^{45}$P | 45 | 30 | L?-pending | pending | binding_energy | — | 335.5200 | — | — |
| ${}^{46}$P | 46 | 31 | L?-pending | pending | binding_energy | — | 336.7200 | — | — |
| ${}^{47}$P | 47 | 32 | L?-pending | pending | binding_energy | — | 338.8230 | — | — |

### Sulfur (Z = 16)

_0 of 24 isotopes with a framework prediction; 0 of 24 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{26}$S | 26 | 10 | L?-pending | pending | binding_energy | — | 169.6500 | — | — |
| ${}^{27}$S | 27 | 11 | L?-pending | pending | binding_energy | — | 187.9200 | — | — |
| ${}^{28}$S | 28 | 12 | L?-pending | pending | binding_energy | — | 209.4062 | — | — |
| ${}^{29}$S | 29 | 13 | L?-pending | pending | binding_energy | — | 224.6451 | — | — |
| ${}^{30}$S | 30 | 14 | L?-pending | pending | binding_energy | — | 243.6812 | — | — |
| ${}^{31}$S | 31 | 15 | L?-pending | pending | binding_energy | — | 256.7358 | — | — |
| ${}^{32}$S | 32 | 16 | L?-pending | pending | binding_energy | — | 271.7802 | — | — |
| ${}^{33}$S | 33 | 17 | L?-pending | pending | binding_energy | — | 280.4218 | — | — |
| ${}^{34}$S | 34 | 18 | L?-pending | pending | binding_energy | — | 291.8390 | — | — |
| ${}^{35}$S | 35 | 19 | L?-pending | pending | binding_energy | — | 298.8248 | — | — |
| ${}^{36}$S | 36 | 20 | L?-pending | pending | binding_energy | — | 308.7140 | — | — |
| ${}^{37}$S | 37 | 21 | L?-pending | pending | binding_energy | — | 313.0176 | — | — |
| ${}^{38}$S | 38 | 22 | L?-pending | pending | binding_energy | — | 321.0538 | — | — |
| ${}^{39}$S | 39 | 23 | L?-pending | pending | binding_energy | — | 325.4265 | — | — |
| ${}^{40}$S | 40 | 24 | L?-pending | pending | binding_energy | — | 333.1730 | — | — |
| ${}^{41}$S | 41 | 25 | L?-pending | pending | binding_energy | — | 337.4151 | — | — |
| ${}^{42}$S | 42 | 26 | L?-pending | pending | binding_energy | — | 344.1156 | — | — |
| ${}^{43}$S | 43 | 27 | L?-pending | pending | binding_energy | — | 346.7446 | — | — |
| ${}^{44}$S | 44 | 28 | L?-pending | pending | binding_energy | — | 351.8247 | — | — |
| ${}^{45}$S | 45 | 29 | L?-pending | pending | binding_energy | — | 354.0150 | — | — |
| ${}^{46}$S | 46 | 30 | L?-pending | pending | binding_energy | — | 358.1100 | — | — |
| ${}^{47}$S | 47 | 31 | L?-pending | pending | binding_energy | — | 359.6440 | — | — |
| ${}^{48}$S | 48 | 32 | L?-pending | pending | binding_energy | — | 362.4960 | — | — |
| ${}^{49}$S | 49 | 33 | L?-pending | pending | binding_energy | — | 362.6000 | — | — |

### Chlorine (Z = 17)

_0 of 25 isotopes with a framework prediction; 0 of 25 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{28}$Cl | 28 | 11 | L?-pending | pending | binding_energy | — | 184.4360 | — | — |
| ${}^{29}$Cl | 29 | 12 | L?-pending | pending | binding_energy | — | 206.7410 | — | — |
| ${}^{30}$Cl | 30 | 13 | L?-pending | pending | binding_energy | — | 224.1651 | — | — |
| ${}^{31}$Cl | 31 | 14 | L?-pending | pending | binding_energy | — | 243.9455 | — | — |
| ${}^{32}$Cl | 32 | 15 | L?-pending | pending | binding_energy | — | 258.3170 | — | — |
| ${}^{33}$Cl | 33 | 16 | L?-pending | pending | binding_energy | — | 274.0569 | — | — |
| ${}^{34}$Cl | 34 | 17 | L?-pending | pending | binding_energy | — | 285.5650 | — | — |
| ${}^{35}$Cl | 35 | 18 | L?-pending | pending | binding_energy | — | 298.2098 | — | — |
| ${}^{36}$Cl | 36 | 19 | L?-pending | pending | binding_energy | — | 306.7896 | — | — |
| ${}^{37}$Cl | 37 | 20 | L?-pending | pending | binding_energy | — | 317.1004 | — | — |
| ${}^{38}$Cl | 38 | 21 | L?-pending | pending | binding_energy | — | 323.2083 | — | — |
| ${}^{39}$Cl | 39 | 22 | L?-pending | pending | binding_energy | — | 331.2817 | — | — |
| ${}^{40}$Cl | 40 | 23 | L?-pending | pending | binding_energy | — | 337.1106 | — | — |
| ${}^{41}$Cl | 41 | 24 | L?-pending | pending | binding_energy | — | 344.9313 | — | — |
| ${}^{42}$Cl | 42 | 25 | L?-pending | pending | binding_energy | — | 350.5272 | — | — |
| ${}^{43}$Cl | 43 | 26 | L?-pending | pending | binding_energy | — | 357.9263 | — | — |
| ${}^{44}$Cl | 44 | 27 | L?-pending | pending | binding_energy | — | 362.3171 | — | — |
| ${}^{45}$Cl | 45 | 28 | L?-pending | pending | binding_energy | — | 368.1720 | — | — |
| ${}^{46}$Cl | 46 | 29 | L?-pending | pending | binding_energy | — | 371.7157 | — | — |
| ${}^{47}$Cl | 47 | 30 | L?-pending | pending | binding_energy | — | 375.6240 | — | — |
| ${}^{48}$Cl | 48 | 31 | L?-pending | pending | binding_energy | — | 378.3840 | — | — |
| ${}^{49}$Cl | 49 | 32 | L?-pending | pending | binding_energy | — | 381.4650 | — | — |
| ${}^{50}$Cl | 50 | 33 | L?-pending | pending | binding_energy | — | 382.5500 | — | — |
| ${}^{51}$Cl | 51 | 34 | L?-pending | pending | binding_energy | — | 384.0300 | — | — |
| ${}^{52}$Cl | 52 | 35 | L?-pending | pending | binding_energy | — | 384.0720 | — | — |

### Argon (Z = 18)

_0 of 26 isotopes with a framework prediction; 0 of 26 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{29}$Ar | 29 | 11 | L?-pending | pending | binding_energy | — | 182.0040 | — | — |
| ${}^{30}$Ar | 30 | 12 | L?-pending | pending | binding_energy | — | 205.9800 | — | — |
| ${}^{31}$Ar | 31 | 13 | L?-pending | pending | binding_energy | — | 224.8120 | — | — |
| ${}^{32}$Ar | 32 | 14 | L?-pending | pending | binding_energy | — | 246.4003 | — | — |
| ${}^{33}$Ar | 33 | 15 | L?-pending | pending | binding_energy | — | 261.6555 | — | — |
| ${}^{34}$Ar | 34 | 16 | L?-pending | pending | binding_energy | — | 278.7209 | — | — |
| ${}^{35}$Ar | 35 | 17 | L?-pending | pending | binding_energy | — | 291.4612 | — | — |
| ${}^{36}$Ar | 36 | 18 | L?-pending | pending | binding_energy | — | 306.7167 | — | — |
| ${}^{37}$Ar | 37 | 19 | L?-pending | pending | binding_energy | — | 315.5042 | — | — |
| ${}^{38}$Ar | 38 | 20 | L?-pending | pending | binding_energy | — | 327.3427 | — | — |
| ${}^{39}$Ar | 39 | 21 | L?-pending | pending | binding_energy | — | 333.9414 | — | — |
| ${}^{40}$Ar | 40 | 22 | L?-pending | pending | binding_energy | — | 343.8104 | — | — |
| ${}^{41}$Ar | 41 | 23 | L?-pending | pending | binding_energy | — | 349.9093 | — | — |
| ${}^{42}$Ar | 42 | 24 | L?-pending | pending | binding_energy | — | 359.3358 | — | — |
| ${}^{43}$Ar | 43 | 25 | L?-pending | pending | binding_energy | — | 364.9942 | — | — |
| ${}^{44}$Ar | 44 | 26 | L?-pending | pending | binding_energy | — | 373.7290 | — | — |
| ${}^{45}$Ar | 45 | 27 | L?-pending | pending | binding_energy | — | 378.8979 | — | — |
| ${}^{46}$Ar | 46 | 28 | L?-pending | pending | binding_energy | — | 386.9696 | — | — |
| ${}^{47}$Ar | 47 | 29 | L?-pending | pending | binding_energy | — | 390.6370 | — | — |
| ${}^{48}$Ar | 48 | 30 | L?-pending | pending | binding_energy | — | 395.6959 | — | — |
| ${}^{49}$Ar | 49 | 31 | L?-pending | pending | binding_energy | — | 398.4680 | — | — |
| ${}^{50}$Ar | 50 | 32 | L?-pending | pending | binding_energy | — | 402.7000 | — | — |
| ${}^{51}$Ar | 51 | 33 | L?-pending | pending | binding_energy | — | 404.0220 | — | — |
| ${}^{52}$Ar | 52 | 34 | L?-pending | pending | binding_energy | — | 407.0040 | — | — |
| ${}^{53}$Ar | 53 | 35 | L?-pending | pending | binding_energy | — | 406.8810 | — | — |
| ${}^{54}$Ar | 54 | 36 | L?-pending | pending | binding_energy | — | 409.2120 | — | — |

### Potassium (Z = 19)

_0 of 29 isotopes with a framework prediction; 0 of 29 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{31}$K | 31 | 12 | L?-pending | pending | binding_energy | — | 201.0970 | — | — |
| ${}^{32}$K | 32 | 13 | L?-pending | pending | binding_energy | — | 221.4400 | — | — |
| ${}^{33}$K | 33 | 14 | L?-pending | pending | binding_energy | — | 243.9360 | — | — |
| ${}^{34}$K | 34 | 15 | L?-pending | pending | binding_energy | — | 260.7800 | — | — |
| ${}^{35}$K | 35 | 16 | L?-pending | pending | binding_energy | — | 278.8044 | — | — |
| ${}^{36}$K | 36 | 17 | L?-pending | pending | binding_energy | — | 293.1200 | — | — |
| ${}^{37}$K | 37 | 18 | L?-pending | pending | binding_energy | — | 308.5744 | — | — |
| ${}^{38}$K | 38 | 19 | L?-pending | pending | binding_energy | — | 320.6463 | — | — |
| ${}^{39}$K | 39 | 20 | L?-pending | pending | binding_energy | — | 333.7240 | — | — |
| ${}^{40}$K | 40 | 21 | L?-pending | pending | binding_energy | — | 341.5236 | — | — |
| ${}^{41}$K | 41 | 22 | L?-pending | pending | binding_energy | — | 351.6190 | — | — |
| ${}^{42}$K | 42 | 23 | L?-pending | pending | binding_energy | — | 359.1528 | — | — |
| ${}^{43}$K | 43 | 24 | L?-pending | pending | binding_energy | — | 368.7775 | — | — |
| ${}^{44}$K | 44 | 25 | L?-pending | pending | binding_energy | — | 376.0549 | — | — |
| ${}^{45}$K | 45 | 26 | L?-pending | pending | binding_energy | — | 384.9604 | — | — |
| ${}^{46}$K | 46 | 27 | L?-pending | pending | binding_energy | — | 391.8300 | — | — |
| ${}^{47}$K | 47 | 28 | L?-pending | pending | binding_energy | — | 400.1993 | — | — |
| ${}^{48}$K | 48 | 29 | L?-pending | pending | binding_energy | — | 404.8432 | — | — |
| ${}^{49}$K | 49 | 30 | L?-pending | pending | binding_energy | — | 410.2415 | — | — |
| ${}^{50}$K | 50 | 31 | L?-pending | pending | binding_energy | — | 414.4292 | — | — |
| ${}^{51}$K | 51 | 32 | L?-pending | pending | binding_energy | — | 419.2881 | — | — |
| ${}^{52}$K | 52 | 33 | L?-pending | pending | binding_energy | — | 421.9816 | — | — |
| ${}^{53}$K | 53 | 34 | L?-pending | pending | binding_energy | — | 425.2110 | — | — |
| ${}^{54}$K | 54 | 35 | L?-pending | pending | binding_energy | — | 426.1140 | — | — |
| ${}^{55}$K | 55 | 36 | L?-pending | pending | binding_energy | — | 428.5600 | — | — |
| ${}^{56}$K | 56 | 37 | L?-pending | pending | binding_energy | — | 429.1280 | — | — |
| ${}^{57}$K | 57 | 38 | L?-pending | pending | binding_energy | — | 431.0910 | — | — |
| ${}^{58}$K | 58 | 39 | L?-pending | pending | binding_energy | — | 431.3460 | — | — |
| ${}^{59}$K | 59 | 40 | L?-pending | pending | binding_energy | — | 432.5880 | — | — |

### Calcium (Z = 20)

_1 of 29 isotopes with a framework prediction; 1 of 29 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{33}$Ca | 33 | 13 | L?-pending | pending | binding_energy | — | 219.6810 | — | — |
| ${}^{34}$Ca | 34 | 14 | L?-pending | pending | binding_energy | — | 243.8820 | — | — |
| ${}^{35}$Ca | 35 | 15 | L?-pending | pending | binding_energy | — | 261.6600 | — | — |
| ${}^{36}$Ca | 36 | 16 | L?-pending | pending | binding_energy | — | 281.3717 | — | — |
| ${}^{37}$Ca | 37 | 17 | L?-pending | pending | binding_energy | — | 296.1279 | — | — |
| ${}^{38}$Ca | 38 | 18 | L?-pending | pending | binding_energy | — | 313.1216 | — | — |
| ${}^{39}$Ca | 39 | 19 | L?-pending | pending | binding_energy | — | 326.4172 | — | — |
| ${}^{40}$Ca | 40 | 20 | L2-alpha-cluster | recursive | binding_energy | 408.7713 | 342.0522 | +19.51 % | 37147.9694 MeV (-2067.1 ppm) |
| ${}^{41}$Ca | 41 | 21 | L?-pending | pending | binding_energy | — | 350.4150 | — | — |
| ${}^{42}$Ca | 42 | 22 | L?-pending | pending | binding_energy | — | 361.8957 | — | — |
| ${}^{43}$Ca | 43 | 23 | L?-pending | pending | binding_energy | — | 369.8286 | — | — |
| ${}^{44}$Ca | 44 | 24 | L?-pending | pending | binding_energy | — | 380.9598 | — | — |
| ${}^{45}$Ca | 45 | 25 | L?-pending | pending | binding_energy | — | 388.3746 | — | — |
| ${}^{46}$Ca | 46 | 26 | L?-pending | pending | binding_energy | — | 398.7733 | — | — |
| ${}^{47}$Ca | 47 | 27 | L?-pending | pending | binding_energy | — | 406.0497 | — | — |
| ${}^{48}$Ca | 48 | 28 | L?-pending | pending | binding_energy | — | 416.0012 | — | — |
| ${}^{49}$Ca | 49 | 29 | L?-pending | pending | binding_energy | — | 421.1476 | — | — |
| ${}^{50}$Ca | 50 | 30 | L?-pending | pending | binding_energy | — | 427.5082 | — | — |
| ${}^{51}$Ca | 51 | 31 | L?-pending | pending | binding_energy | — | 432.3226 | — | — |
| ${}^{52}$Ca | 52 | 32 | L?-pending | pending | binding_energy | — | 438.3279 | — | — |
| ${}^{53}$Ca | 53 | 33 | L?-pending | pending | binding_energy | — | 441.5206 | — | — |
| ${}^{54}$Ca | 54 | 34 | L?-pending | pending | binding_energy | — | 445.3648 | — | — |
| ${}^{55}$Ca | 55 | 35 | L?-pending | pending | binding_energy | — | 446.9259 | — | — |
| ${}^{56}$Ca | 56 | 36 | L?-pending | pending | binding_energy | — | 449.8573 | — | — |
| ${}^{57}$Ca | 57 | 37 | L?-pending | pending | binding_energy | — | 450.9840 | — | — |
| ${}^{58}$Ca | 58 | 38 | L?-pending | pending | binding_energy | — | 454.0240 | — | — |
| ${}^{59}$Ca | 59 | 39 | L?-pending | pending | binding_energy | — | 454.7720 | — | — |
| ${}^{60}$Ca | 60 | 40 | L?-pending | pending | binding_energy | — | 457.6200 | — | — |
| ${}^{61}$Ca | 61 | 41 | L?-pending | pending | binding_energy | — | 457.6830 | — | — |

### Scandium (Z = 21)

_0 of 29 isotopes with a framework prediction; 0 of 29 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{35}$Sc | 35 | 14 | L?-pending | pending | binding_energy | — | 238.9800 | — | — |
| ${}^{36}$Sc | 36 | 15 | L?-pending | pending | binding_energy | — | 257.9760 | — | — |
| ${}^{37}$Sc | 37 | 16 | L?-pending | pending | binding_energy | — | 278.4250 | — | — |
| ${}^{38}$Sc | 38 | 17 | L?-pending | pending | binding_energy | — | 294.5380 | — | — |
| ${}^{39}$Sc | 39 | 18 | L?-pending | pending | binding_energy | — | 312.5248 | — | — |
| ${}^{40}$Sc | 40 | 19 | L?-pending | pending | binding_energy | — | 326.9468 | — | — |
| ${}^{41}$Sc | 41 | 20 | L?-pending | pending | binding_energy | — | 343.1371 | — | — |
| ${}^{42}$Sc | 42 | 21 | L?-pending | pending | binding_energy | — | 354.6871 | — | — |
| ${}^{43}$Sc | 43 | 22 | L?-pending | pending | binding_energy | — | 366.8255 | — | — |
| ${}^{44}$Sc | 44 | 23 | L?-pending | pending | binding_energy | — | 376.5247 | — | — |
| ${}^{45}$Sc | 45 | 24 | L?-pending | pending | binding_energy | — | 387.8523 | — | — |
| ${}^{46}$Sc | 46 | 25 | L?-pending | pending | binding_energy | — | 396.6130 | — | — |
| ${}^{47}$Sc | 47 | 26 | L?-pending | pending | binding_energy | — | 407.2595 | — | — |
| ${}^{48}$Sc | 48 | 27 | L?-pending | pending | binding_energy | — | 415.4981 | — | — |
| ${}^{49}$Sc | 49 | 28 | L?-pending | pending | binding_energy | — | 425.6277 | — | — |
| ${}^{50}$Sc | 50 | 29 | L?-pending | pending | binding_energy | — | 431.6737 | — | — |
| ${}^{51}$Sc | 51 | 30 | L?-pending | pending | binding_energy | — | 438.4583 | — | — |
| ${}^{52}$Sc | 52 | 31 | L?-pending | pending | binding_energy | — | 443.8028 | — | — |
| ${}^{53}$Sc | 53 | 32 | L?-pending | pending | binding_energy | — | 450.1201 | — | — |
| ${}^{54}$Sc | 54 | 33 | L?-pending | pending | binding_energy | — | 453.8598 | — | — |
| ${}^{55}$Sc | 55 | 34 | L?-pending | pending | binding_energy | — | 458.3353 | — | — |
| ${}^{56}$Sc | 56 | 35 | L?-pending | pending | binding_energy | — | 461.0804 | — | — |
| ${}^{57}$Sc | 57 | 36 | L?-pending | pending | binding_energy | — | 465.0155 | — | — |
| ${}^{58}$Sc | 58 | 37 | L?-pending | pending | binding_energy | — | 467.1867 | — | — |
| ${}^{59}$Sc | 59 | 38 | L?-pending | pending | binding_energy | — | 470.6080 | — | — |
| ${}^{60}$Sc | 60 | 39 | L?-pending | pending | binding_energy | — | 472.3800 | — | — |
| ${}^{61}$Sc | 61 | 40 | L?-pending | pending | binding_energy | — | 475.4340 | — | — |
| ${}^{62}$Sc | 62 | 41 | L?-pending | pending | binding_energy | — | 476.6560 | — | — |
| ${}^{63}$Sc | 63 | 42 | L?-pending | pending | binding_energy | — | 478.9890 | — | — |

### Titanium (Z = 22)

_0 of 29 isotopes with a framework prediction; 0 of 29 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{37}$Ti | 37 | 15 | L?-pending | pending | binding_energy | — | 256.2620 | — | — |
| ${}^{38}$Ti | 38 | 16 | L?-pending | pending | binding_energy | — | 278.1220 | — | — |
| ${}^{39}$Ti | 39 | 17 | L?-pending | pending | binding_energy | — | 295.0740 | — | — |
| ${}^{40}$Ti | 40 | 18 | L?-pending | pending | binding_energy | — | 314.6345 | — | — |
| ${}^{41}$Ti | 41 | 19 | L?-pending | pending | binding_energy | — | 329.4099 | — | — |
| ${}^{42}$Ti | 42 | 20 | L?-pending | pending | binding_energy | — | 346.8881 | — | — |
| ${}^{43}$Ti | 43 | 21 | L?-pending | pending | binding_energy | — | 359.1706 | — | — |
| ${}^{44}$Ti | 44 | 22 | L?-pending | pending | binding_energy | — | 375.4749 | — | — |
| ${}^{45}$Ti | 45 | 23 | L?-pending | pending | binding_energy | — | 385.0079 | — | — |
| ${}^{46}$Ti | 46 | 24 | L?-pending | pending | binding_energy | — | 398.1973 | — | — |
| ${}^{47}$Ti | 47 | 25 | L?-pending | pending | binding_energy | — | 407.0779 | — | — |
| ${}^{48}$Ti | 48 | 26 | L?-pending | pending | binding_energy | — | 418.7046 | — | — |
| ${}^{49}$Ti | 49 | 27 | L?-pending | pending | binding_energy | — | 426.8470 | — | — |
| ${}^{50}$Ti | 50 | 28 | L?-pending | pending | binding_energy | — | 437.7861 | — | — |
| ${}^{51}$Ti | 51 | 29 | L?-pending | pending | binding_energy | — | 444.1586 | — | — |
| ${}^{52}$Ti | 52 | 30 | L?-pending | pending | binding_energy | — | 451.9746 | — | — |
| ${}^{53}$Ti | 53 | 31 | L?-pending | pending | binding_energy | — | 457.4497 | — | — |
| ${}^{54}$Ti | 54 | 32 | L?-pending | pending | binding_energy | — | 464.3834 | — | — |
| ${}^{55}$Ti | 55 | 33 | L?-pending | pending | binding_energy | — | 468.5433 | — | — |
| ${}^{56}$Ti | 56 | 34 | L?-pending | pending | binding_energy | — | 474.2052 | — | — |
| ${}^{57}$Ti | 57 | 35 | L?-pending | pending | binding_energy | — | 477.2553 | — | — |
| ${}^{58}$Ti | 58 | 36 | L?-pending | pending | binding_energy | — | 481.8425 | — | — |
| ${}^{59}$Ti | 59 | 37 | L?-pending | pending | binding_energy | — | 484.8620 | — | — |
| ${}^{60}$Ti | 60 | 38 | L?-pending | pending | binding_energy | — | 489.1671 | — | — |
| ${}^{61}$Ti | 61 | 39 | L?-pending | pending | binding_energy | — | 491.5380 | — | — |
| ${}^{62}$Ti | 62 | 40 | L?-pending | pending | binding_energy | — | 495.3800 | — | — |
| ${}^{63}$Ti | 63 | 41 | L?-pending | pending | binding_energy | — | 497.1330 | — | — |
| ${}^{64}$Ti | 64 | 42 | L?-pending | pending | binding_energy | — | 500.8640 | — | — |
| ${}^{65}$Ti | 65 | 43 | L?-pending | pending | binding_energy | — | 502.1900 | — | — |

### Vanadium (Z = 23)

_0 of 29 isotopes with a framework prediction; 0 of 29 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{39}$V | 39 | 16 | L?-pending | pending | binding_energy | — | 274.2090 | — | — |
| ${}^{40}$V | 40 | 17 | L?-pending | pending | binding_energy | — | 292.4000 | — | — |
| ${}^{41}$V | 41 | 18 | L?-pending | pending | binding_energy | — | 312.6250 | — | — |
| ${}^{42}$V | 42 | 19 | L?-pending | pending | binding_energy | — | 328.6080 | — | — |
| ${}^{43}$V | 43 | 20 | L?-pending | pending | binding_energy | — | 346.9891 | — | — |
| ${}^{44}$V | 44 | 21 | L?-pending | pending | binding_energy | — | 360.9521 | — | — |
| ${}^{45}$V | 45 | 22 | L?-pending | pending | binding_energy | — | 377.1018 | — | — |
| ${}^{46}$V | 46 | 23 | L?-pending | pending | binding_energy | — | 390.3625 | — | — |
| ${}^{47}$V | 47 | 24 | L?-pending | pending | binding_energy | — | 403.3650 | — | — |
| ${}^{48}$V | 48 | 25 | L?-pending | pending | binding_energy | — | 413.9073 | — | — |
| ${}^{49}$V | 49 | 26 | L?-pending | pending | binding_energy | — | 425.4628 | — | — |
| ${}^{50}$V | 50 | 27 | L?-pending | pending | binding_energy | — | 434.7952 | — | — |
| ${}^{51}$V | 51 | 28 | L?-pending | pending | binding_energy | — | 445.8463 | — | — |
| ${}^{52}$V | 52 | 29 | L?-pending | pending | binding_energy | — | 453.1576 | — | — |
| ${}^{53}$V | 53 | 30 | L?-pending | pending | binding_energy | — | 461.6376 | — | — |
| ${}^{54}$V | 54 | 31 | L?-pending | pending | binding_energy | — | 467.7555 | — | — |
| ${}^{55}$V | 55 | 32 | L?-pending | pending | binding_energy | — | 475.0537 | — | — |
| ${}^{56}$V | 56 | 33 | L?-pending | pending | binding_energy | — | 480.1832 | — | — |
| ${}^{57}$V | 57 | 34 | L?-pending | pending | binding_energy | — | 486.5062 | — | — |
| ${}^{58}$V | 58 | 35 | L?-pending | pending | binding_energy | — | 490.5730 | — | — |
| ${}^{59}$V | 59 | 36 | L?-pending | pending | binding_energy | — | 495.8244 | — | — |
| ${}^{60}$V | 60 | 37 | L?-pending | pending | binding_energy | — | 499.3725 | — | — |
| ${}^{61}$V | 61 | 38 | L?-pending | pending | binding_energy | — | 504.5335 | — | — |
| ${}^{62}$V | 62 | 39 | L?-pending | pending | binding_energy | — | 507.6409 | — | — |
| ${}^{63}$V | 63 | 40 | L?-pending | pending | binding_energy | — | 512.2392 | — | — |
| ${}^{64}$V | 64 | 41 | L?-pending | pending | binding_energy | — | 514.8800 | — | — |
| ${}^{65}$V | 65 | 42 | L?-pending | pending | binding_energy | — | 518.7650 | — | — |
| ${}^{66}$V | 66 | 43 | L?-pending | pending | binding_energy | — | 521.0040 | — | — |
| ${}^{67}$V | 67 | 44 | L?-pending | pending | binding_energy | — | 524.5430 | — | — |

### Chromium (Z = 24)

_0 of 30 isotopes with a framework prediction; 0 of 30 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{41}$Cr | 41 | 17 | L?-pending | pending | binding_energy | — | 291.7560 | — | — |
| ${}^{42}$Cr | 42 | 18 | L?-pending | pending | binding_energy | — | 313.1520 | — | — |
| ${}^{43}$Cr | 43 | 19 | L?-pending | pending | binding_energy | — | 330.2400 | — | — |
| ${}^{44}$Cr | 44 | 20 | L?-pending | pending | binding_energy | — | 349.7836 | — | — |
| ${}^{45}$Cr | 45 | 21 | L?-pending | pending | binding_energy | — | 363.9478 | — | — |
| ${}^{46}$Cr | 46 | 22 | L?-pending | pending | binding_energy | — | 381.9759 | — | — |
| ${}^{47}$Cr | 47 | 23 | L?-pending | pending | binding_energy | — | 395.1387 | — | — |
| ${}^{48}$Cr | 48 | 24 | L?-pending | pending | binding_energy | — | 411.4683 | — | — |
| ${}^{49}$Cr | 49 | 25 | L?-pending | pending | binding_energy | — | 422.0506 | — | — |
| ${}^{50}$Cr | 50 | 26 | L?-pending | pending | binding_energy | — | 435.0509 | — | — |
| ${}^{51}$Cr | 51 | 27 | L?-pending | pending | binding_energy | — | 444.3116 | — | — |
| ${}^{52}$Cr | 52 | 28 | L?-pending | pending | binding_energy | — | 456.3517 | — | — |
| ${}^{53}$Cr | 53 | 29 | L?-pending | pending | binding_energy | — | 464.2911 | — | — |
| ${}^{54}$Cr | 54 | 30 | L?-pending | pending | binding_energy | — | 474.0102 | — | — |
| ${}^{55}$Cr | 55 | 31 | L?-pending | pending | binding_energy | — | 480.2565 | — | — |
| ${}^{56}$Cr | 56 | 32 | L?-pending | pending | binding_energy | — | 488.5026 | — | — |
| ${}^{57}$Cr | 57 | 33 | L?-pending | pending | binding_energy | — | 493.8138 | — | — |
| ${}^{58}$Cr | 58 | 34 | L?-pending | pending | binding_energy | — | 501.3519 | — | — |
| ${}^{59}$Cr | 59 | 35 | L?-pending | pending | binding_energy | — | 505.5474 | — | — |
| ${}^{60}$Cr | 60 | 36 | L?-pending | pending | binding_energy | — | 512.4113 | — | — |
| ${}^{61}$Cr | 61 | 37 | L?-pending | pending | binding_energy | — | 516.0706 | — | — |
| ${}^{62}$Cr | 62 | 38 | L?-pending | pending | binding_energy | — | 522.4980 | — | — |
| ${}^{63}$Cr | 63 | 39 | L?-pending | pending | binding_energy | — | 525.8950 | — | — |
| ${}^{64}$Cr | 64 | 40 | L?-pending | pending | binding_energy | — | 531.4280 | — | — |
| ${}^{65}$Cr | 65 | 41 | L?-pending | pending | binding_energy | — | 534.1700 | — | — |
| ${}^{66}$Cr | 66 | 42 | L?-pending | pending | binding_energy | — | 539.0880 | — | — |
| ${}^{67}$Cr | 67 | 43 | L?-pending | pending | binding_energy | — | 541.2930 | — | — |
| ${}^{68}$Cr | 68 | 44 | L?-pending | pending | binding_energy | — | 545.7680 | — | — |
| ${}^{69}$Cr | 69 | 45 | L?-pending | pending | binding_energy | — | 547.7910 | — | — |
| ${}^{70}$Cr | 70 | 46 | L?-pending | pending | binding_energy | — | 551.8800 | — | — |

### Manganese (Z = 25)

_0 of 31 isotopes with a framework prediction; 0 of 31 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{43}$Mn | 43 | 18 | L?-pending | pending | binding_energy | — | 310.1590 | — | — |
| ${}^{44}$Mn | 44 | 19 | L?-pending | pending | binding_energy | — | 328.1080 | — | — |
| ${}^{45}$Mn | 45 | 20 | L?-pending | pending | binding_energy | — | 348.6150 | — | — |
| ${}^{46}$Mn | 46 | 21 | L?-pending | pending | binding_energy | — | 364.1397 | — | — |
| ${}^{47}$Mn | 47 | 22 | L?-pending | pending | binding_energy | — | 382.3596 | — | — |
| ${}^{48}$Mn | 48 | 23 | L?-pending | pending | binding_energy | — | 397.1612 | — | — |
| ${}^{49}$Mn | 49 | 24 | L?-pending | pending | binding_energy | — | 413.5558 | — | — |
| ${}^{50}$Mn | 50 | 25 | L?-pending | pending | binding_energy | — | 426.6341 | — | — |
| ${}^{51}$Mn | 51 | 26 | L?-pending | pending | binding_energy | — | 440.3218 | — | — |
| ${}^{52}$Mn | 52 | 27 | L?-pending | pending | binding_energy | — | 450.8613 | — | — |
| ${}^{53}$Mn | 53 | 28 | L?-pending | pending | binding_energy | — | 462.9115 | — | — |
| ${}^{54}$Mn | 54 | 29 | L?-pending | pending | binding_energy | — | 471.8507 | — | — |
| ${}^{55}$Mn | 55 | 30 | L?-pending | pending | binding_energy | — | 482.0764 | — | — |
| ${}^{56}$Mn | 56 | 31 | L?-pending | pending | binding_energy | — | 489.3468 | — | — |
| ${}^{57}$Mn | 57 | 32 | L?-pending | pending | binding_energy | — | 497.9927 | — | — |
| ${}^{58}$Mn | 58 | 33 | L?-pending | pending | binding_energy | — | 504.4053 | — | — |
| ${}^{59}$Mn | 59 | 34 | L?-pending | pending | binding_energy | — | 512.1744 | — | — |
| ${}^{60}$Mn | 60 | 35 | L?-pending | pending | binding_energy | — | 517.6884 | — | — |
| ${}^{61}$Mn | 61 | 36 | L?-pending | pending | binding_energy | — | 524.5339 | — | — |
| ${}^{62}$Mn | 62 | 37 | L?-pending | pending | binding_energy | — | 529.3870 | — | — |
| ${}^{63}$Mn | 63 | 38 | L?-pending | pending | binding_energy | — | 535.8214 | — | — |
| ${}^{64}$Mn | 64 | 39 | L?-pending | pending | binding_energy | — | 539.9947 | — | — |
| ${}^{65}$Mn | 65 | 40 | L?-pending | pending | binding_energy | — | 546.0443 | — | — |
| ${}^{66}$Mn | 66 | 41 | L?-pending | pending | binding_energy | — | 549.8987 | — | — |
| ${}^{67}$Mn | 67 | 42 | L?-pending | pending | binding_energy | — | 554.8270 | — | — |
| ${}^{68}$Mn | 68 | 43 | L?-pending | pending | binding_energy | — | 558.2120 | — | — |
| ${}^{69}$Mn | 69 | 44 | L?-pending | pending | binding_energy | — | 562.6950 | — | — |
| ${}^{70}$Mn | 70 | 45 | L?-pending | pending | binding_energy | — | 565.8800 | — | — |
| ${}^{71}$Mn | 71 | 46 | L?-pending | pending | binding_energy | — | 570.1300 | — | — |
| ${}^{72}$Mn | 72 | 47 | L?-pending | pending | binding_energy | — | 572.7600 | — | — |
| ${}^{73}$Mn | 73 | 48 | L?-pending | pending | binding_energy | — | 576.3350 | — | — |

### Iron (Z = 26)

_0 of 32 isotopes with a framework prediction; 0 of 32 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{45}$Fe | 45 | 19 | L?-pending | pending | binding_energy | — | 328.4550 | — | — |
| ${}^{46}$Fe | 46 | 20 | L?-pending | pending | binding_energy | — | 349.7380 | — | — |
| ${}^{47}$Fe | 47 | 21 | L?-pending | pending | binding_energy | — | 366.1300 | — | — |
| ${}^{48}$Fe | 48 | 22 | L?-pending | pending | binding_energy | — | 385.0908 | — | — |
| ${}^{49}$Fe | 49 | 23 | L?-pending | pending | binding_energy | — | 399.9043 | — | — |
| ${}^{50}$Fe | 50 | 24 | L?-pending | pending | binding_energy | — | 417.7013 | — | — |
| ${}^{51}$Fe | 51 | 25 | L?-pending | pending | binding_energy | — | 431.4854 | — | — |
| ${}^{52}$Fe | 52 | 26 | L?-pending | pending | binding_energy | — | 447.6996 | — | — |
| ${}^{53}$Fe | 53 | 27 | L?-pending | pending | binding_energy | — | 458.3863 | — | — |
| ${}^{54}$Fe | 54 | 28 | L?-pending | pending | binding_energy | — | 471.7648 | — | — |
| ${}^{55}$Fe | 55 | 29 | L?-pending | pending | binding_energy | — | 481.0629 | — | — |
| ${}^{56}$Fe | 56 | 30 | L?-pending | pending | binding_energy | — | 492.2600 | — | — |
| ${}^{57}$Fe | 57 | 31 | L?-pending | pending | binding_energy | — | 499.9061 | — | — |
| ${}^{58}$Fe | 58 | 32 | L?-pending | pending | binding_energy | — | 509.9507 | — | — |
| ${}^{59}$Fe | 59 | 33 | L?-pending | pending | binding_energy | — | 516.5317 | — | — |
| ${}^{60}$Fe | 60 | 34 | L?-pending | pending | binding_energy | — | 525.3512 | — | — |
| ${}^{61}$Fe | 61 | 35 | L?-pending | pending | binding_energy | — | 530.9299 | — | — |
| ${}^{62}$Fe | 62 | 36 | L?-pending | pending | binding_energy | — | 538.9588 | — | — |
| ${}^{63}$Fe | 63 | 37 | L?-pending | pending | binding_energy | — | 543.7876 | — | — |
| ${}^{64}$Fe | 64 | 38 | L?-pending | pending | binding_energy | — | 551.1929 | — | — |
| ${}^{65}$Fe | 65 | 39 | L?-pending | pending | binding_energy | — | 555.5126 | — | — |
| ${}^{66}$Fe | 66 | 40 | L?-pending | pending | binding_energy | — | 562.4338 | — | — |
| ${}^{67}$Fe | 67 | 41 | L?-pending | pending | binding_energy | — | 566.1457 | — | — |
| ${}^{68}$Fe | 68 | 42 | L?-pending | pending | binding_energy | — | 572.4240 | — | — |
| ${}^{69}$Fe | 69 | 43 | L?-pending | pending | binding_energy | — | 575.8050 | — | — |
| ${}^{70}$Fe | 70 | 44 | L?-pending | pending | binding_energy | — | 581.5600 | — | — |
| ${}^{71}$Fe | 71 | 45 | L?-pending | pending | binding_energy | — | 584.6850 | — | — |
| ${}^{72}$Fe | 72 | 46 | L?-pending | pending | binding_energy | — | 590.0400 | — | — |
| ${}^{73}$Fe | 73 | 47 | L?-pending | pending | binding_energy | — | 592.8330 | — | — |
| ${}^{74}$Fe | 74 | 48 | L?-pending | pending | binding_energy | — | 597.6240 | — | — |
| ${}^{75}$Fe | 75 | 49 | L?-pending | pending | binding_energy | — | 599.7000 | — | — |
| ${}^{76}$Fe | 76 | 50 | L?-pending | pending | binding_energy | — | 603.6680 | — | — |

### Cobalt (Z = 27)

_0 of 32 isotopes with a framework prediction; 0 of 32 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{47}$Co | 47 | 20 | L?-pending | pending | binding_energy | — | 347.6120 | — | — |
| ${}^{48}$Co | 48 | 21 | L?-pending | pending | binding_energy | — | 364.5600 | — | — |
| ${}^{49}$Co | 49 | 22 | L?-pending | pending | binding_energy | — | 384.1600 | — | — |
| ${}^{50}$Co | 50 | 23 | L?-pending | pending | binding_energy | — | 400.0319 | — | — |
| ${}^{51}$Co | 51 | 24 | L?-pending | pending | binding_energy | — | 417.8560 | — | — |
| ${}^{52}$Co | 52 | 25 | L?-pending | pending | binding_energy | — | 432.9292 | — | — |
| ${}^{53}$Co | 53 | 26 | L?-pending | pending | binding_energy | — | 449.3159 | — | — |
| ${}^{54}$Co | 54 | 27 | L?-pending | pending | binding_energy | — | 462.7379 | — | — |
| ${}^{55}$Co | 55 | 28 | L?-pending | pending | binding_energy | — | 476.8291 | — | — |
| ${}^{56}$Co | 56 | 29 | L?-pending | pending | binding_energy | — | 486.9110 | — | — |
| ${}^{57}$Co | 57 | 30 | L?-pending | pending | binding_energy | — | 498.2874 | — | — |
| ${}^{58}$Co | 58 | 31 | L?-pending | pending | binding_energy | — | 506.8604 | — | — |
| ${}^{59}$Co | 59 | 32 | L?-pending | pending | binding_energy | — | 517.3142 | — | — |
| ${}^{60}$Co | 60 | 33 | L?-pending | pending | binding_energy | — | 524.8062 | — | — |
| ${}^{61}$Co | 61 | 34 | L?-pending | pending | binding_energy | — | 534.1252 | — | — |
| ${}^{62}$Co | 62 | 35 | L?-pending | pending | binding_energy | — | 540.7228 | — | — |
| ${}^{63}$Co | 63 | 36 | L?-pending | pending | binding_energy | — | 549.2212 | — | — |
| ${}^{64}$Co | 64 | 37 | L?-pending | pending | binding_energy | — | 555.2334 | — | — |
| ${}^{65}$Co | 65 | 38 | L?-pending | pending | binding_energy | — | 562.6975 | — | — |
| ${}^{66}$Co | 66 | 39 | L?-pending | pending | binding_energy | — | 567.9922 | — | — |
| ${}^{67}$Co | 67 | 40 | L?-pending | pending | binding_energy | — | 574.9767 | — | — |
| ${}^{68}$Co | 68 | 41 | L?-pending | pending | binding_energy | — | 579.3688 | — | — |
| ${}^{69}$Co | 69 | 42 | L?-pending | pending | binding_energy | — | 586.1830 | — | — |
| ${}^{70}$Co | 70 | 43 | L?-pending | pending | binding_energy | — | 590.3939 | — | — |
| ${}^{71}$Co | 71 | 44 | L?-pending | pending | binding_energy | — | 596.3101 | — | — |
| ${}^{72}$Co | 72 | 45 | L?-pending | pending | binding_energy | — | 600.3360 | — | — |
| ${}^{73}$Co | 73 | 46 | L?-pending | pending | binding_energy | — | 606.0460 | — | — |
| ${}^{74}$Co | 74 | 47 | L?-pending | pending | binding_energy | — | 609.6860 | — | — |
| ${}^{75}$Co | 75 | 48 | L?-pending | pending | binding_energy | — | 614.7750 | — | — |
| ${}^{76}$Co | 76 | 49 | L?-pending | pending | binding_energy | — | 617.9560 | — | — |
| ${}^{77}$Co | 77 | 50 | L?-pending | pending | binding_energy | — | 622.3140 | — | — |
| ${}^{78}$Co | 78 | 51 | L?-pending | pending | binding_energy | — | 623.7660 | — | — |

### Nickel (Z = 28)

_0 of 35 isotopes with a framework prediction; 0 of 35 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{48}$Ni | 48 | 20 | L?-pending | pending | binding_energy | — | 347.3280 | — | — |
| ${}^{49}$Ni | 49 | 21 | L?-pending | pending | binding_energy | — | 365.0500 | — | — |
| ${}^{50}$Ni | 50 | 22 | L?-pending | pending | binding_energy | — | 385.1000 | — | — |
| ${}^{51}$Ni | 51 | 23 | L?-pending | pending | binding_energy | — | 401.3700 | — | — |
| ${}^{52}$Ni | 52 | 24 | L?-pending | pending | binding_energy | — | 420.3627 | — | — |
| ${}^{53}$Ni | 53 | 25 | L?-pending | pending | binding_energy | — | 435.5050 | — | — |
| ${}^{54}$Ni | 54 | 26 | L?-pending | pending | binding_energy | — | 453.2238 | — | — |
| ${}^{55}$Ni | 55 | 27 | L?-pending | pending | binding_energy | — | 467.3527 | — | — |
| ${}^{56}$Ni | 56 | 28 | L?-pending | pending | binding_energy | — | 483.9957 | — | — |
| ${}^{57}$Ni | 57 | 29 | L?-pending | pending | binding_energy | — | 494.2434 | — | — |
| ${}^{58}$Ni | 58 | 30 | L?-pending | pending | binding_energy | — | 506.4596 | — | — |
| ${}^{59}$Ni | 59 | 31 | L?-pending | pending | binding_energy | — | 515.4589 | — | — |
| ${}^{60}$Ni | 60 | 32 | L?-pending | pending | binding_energy | — | 526.8466 | — | — |
| ${}^{61}$Ni | 61 | 33 | L?-pending | pending | binding_energy | — | 534.6667 | — | — |
| ${}^{62}$Ni | 62 | 34 | L?-pending | pending | binding_energy | — | 545.2624 | — | — |
| ${}^{63}$Ni | 63 | 35 | L?-pending | pending | binding_energy | — | 552.1002 | — | — |
| ${}^{64}$Ni | 64 | 36 | L?-pending | pending | binding_energy | — | 561.7577 | — | — |
| ${}^{65}$Ni | 65 | 37 | L?-pending | pending | binding_energy | — | 567.8558 | — | — |
| ${}^{66}$Ni | 66 | 38 | L?-pending | pending | binding_energy | — | 576.8076 | — | — |
| ${}^{67}$Ni | 67 | 39 | L?-pending | pending | binding_energy | — | 582.6153 | — | — |
| ${}^{68}$Ni | 68 | 40 | L?-pending | pending | binding_energy | — | 590.4077 | — | — |
| ${}^{69}$Ni | 69 | 41 | L?-pending | pending | binding_energy | — | 594.9939 | — | — |
| ${}^{70}$Ni | 70 | 42 | L?-pending | pending | binding_energy | — | 602.3004 | — | — |
| ${}^{71}$Ni | 71 | 43 | L?-pending | pending | binding_energy | — | 606.5641 | — | — |
| ${}^{72}$Ni | 72 | 44 | L?-pending | pending | binding_energy | — | 613.4552 | — | — |
| ${}^{73}$Ni | 73 | 45 | L?-pending | pending | binding_energy | — | 617.4087 | — | — |
| ${}^{74}$Ni | 74 | 46 | L?-pending | pending | binding_energy | — | 624.0420 | — | — |
| ${}^{75}$Ni | 75 | 47 | L?-pending | pending | binding_energy | — | 627.6750 | — | — |
| ${}^{76}$Ni | 76 | 48 | L?-pending | pending | binding_energy | — | 633.6880 | — | — |
| ${}^{77}$Ni | 77 | 49 | L?-pending | pending | binding_energy | — | 636.9440 | — | — |
| ${}^{78}$Ni | 78 | 50 | L?-pending | pending | binding_energy | — | 642.5640 | — | — |
| ${}^{79}$Ni | 79 | 51 | L?-pending | pending | binding_energy | — | 643.8500 | — | — |
| ${}^{80}$Ni | 80 | 52 | L?-pending | pending | binding_energy | — | 647.0400 | — | — |
| ${}^{81}$Ni | 81 | 53 | L?-pending | pending | binding_energy | — | 648.0000 | — | — |
| ${}^{82}$Ni | 82 | 54 | L?-pending | pending | binding_energy | — | 650.6700 | — | — |

### Copper (Z = 29)

_0 of 33 isotopes with a framework prediction; 0 of 33 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{52}$Cu | 52 | 23 | L?-pending | pending | binding_energy | — | 398.8920 | — | — |
| ${}^{53}$Cu | 53 | 24 | L?-pending | pending | binding_energy | — | 418.2230 | — | — |
| ${}^{54}$Cu | 54 | 25 | L?-pending | pending | binding_energy | — | 434.4300 | — | — |
| ${}^{55}$Cu | 55 | 26 | L?-pending | pending | binding_energy | — | 452.8698 | — | — |
| ${}^{56}$Cu | 56 | 27 | L?-pending | pending | binding_energy | — | 467.9355 | — | — |
| ${}^{57}$Cu | 57 | 28 | L?-pending | pending | binding_energy | — | 484.6861 | — | — |
| ${}^{58}$Cu | 58 | 29 | L?-pending | pending | binding_energy | — | 497.1162 | — | — |
| ${}^{59}$Cu | 59 | 30 | L?-pending | pending | binding_energy | — | 509.8782 | — | — |
| ${}^{60}$Cu | 60 | 31 | L?-pending | pending | binding_energy | — | 519.9363 | — | — |
| ${}^{61}$Cu | 61 | 32 | L?-pending | pending | binding_energy | — | 531.6464 | — | — |
| ${}^{62}$Cu | 62 | 33 | L?-pending | pending | binding_energy | — | 540.5212 | — | — |
| ${}^{63}$Cu | 63 | 34 | L?-pending | pending | binding_energy | — | 551.3848 | — | — |
| ${}^{64}$Cu | 64 | 35 | L?-pending | pending | binding_energy | — | 559.3007 | — | — |
| ${}^{65}$Cu | 65 | 36 | L?-pending | pending | binding_energy | — | 569.2113 | — | — |
| ${}^{66}$Cu | 66 | 37 | L?-pending | pending | binding_energy | — | 576.2772 | — | — |
| ${}^{67}$Cu | 67 | 38 | L?-pending | pending | binding_energy | — | 585.4098 | — | — |
| ${}^{68}$Cu | 68 | 39 | L?-pending | pending | binding_energy | — | 591.7286 | — | — |
| ${}^{69}$Cu | 69 | 40 | L?-pending | pending | binding_energy | — | 599.9691 | — | — |
| ${}^{70}$Cu | 70 | 41 | L?-pending | pending | binding_energy | — | 605.2806 | — | — |
| ${}^{71}$Cu | 71 | 42 | L?-pending | pending | binding_energy | — | 613.0867 | — | — |
| ${}^{72}$Cu | 72 | 43 | L?-pending | pending | binding_energy | — | 618.2298 | — | — |
| ${}^{73}$Cu | 73 | 44 | L?-pending | pending | binding_energy | — | 625.5056 | — | — |
| ${}^{74}$Cu | 74 | 45 | L?-pending | pending | binding_energy | — | 630.5957 | — | — |
| ${}^{75}$Cu | 75 | 46 | L?-pending | pending | binding_energy | — | 637.1310 | — | — |
| ${}^{76}$Cu | 76 | 47 | L?-pending | pending | binding_energy | — | 641.7137 | — | — |
| ${}^{77}$Cu | 77 | 48 | L?-pending | pending | binding_energy | — | 647.6663 | — | — |
| ${}^{78}$Cu | 78 | 49 | L?-pending | pending | binding_energy | — | 651.6642 | — | — |
| ${}^{79}$Cu | 79 | 50 | L?-pending | pending | binding_energy | — | 657.3541 | — | — |
| ${}^{80}$Cu | 80 | 51 | L?-pending | pending | binding_energy | — | 659.6800 | — | — |
| ${}^{81}$Cu | 81 | 52 | L?-pending | pending | binding_energy | — | 662.9850 | — | — |
| ${}^{82}$Cu | 82 | 53 | L?-pending | pending | binding_energy | — | 664.8560 | — | — |
| ${}^{83}$Cu | 83 | 54 | L?-pending | pending | binding_energy | — | 667.6520 | — | — |
| ${}^{84}$Cu | 84 | 55 | L?-pending | pending | binding_energy | — | 669.0600 | — | — |

### Zinc (Z = 30)

_0 of 33 isotopes with a framework prediction; 0 of 33 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{54}$Zn | 54 | 24 | L?-pending | pending | binding_energy | — | 418.0680 | — | — |
| ${}^{55}$Zn | 55 | 25 | L?-pending | pending | binding_energy | — | 434.7200 | — | — |
| ${}^{56}$Zn | 56 | 26 | L?-pending | pending | binding_energy | — | 453.9360 | — | — |
| ${}^{57}$Zn | 57 | 27 | L?-pending | pending | binding_energy | — | 469.1670 | — | — |
| ${}^{58}$Zn | 58 | 28 | L?-pending | pending | binding_energy | — | 486.9649 | — | — |
| ${}^{59}$Zn | 59 | 29 | L?-pending | pending | binding_energy | — | 499.9530 | — | — |
| ${}^{60}$Zn | 60 | 30 | L?-pending | pending | binding_energy | — | 514.9831 | — | — |
| ${}^{61}$Zn | 61 | 31 | L?-pending | pending | binding_energy | — | 525.2289 | — | — |
| ${}^{62}$Zn | 62 | 32 | L?-pending | pending | binding_energy | — | 538.1194 | — | — |
| ${}^{63}$Zn | 63 | 33 | L?-pending | pending | binding_energy | — | 547.2361 | — | — |
| ${}^{64}$Zn | 64 | 34 | L?-pending | pending | binding_energy | — | 559.0980 | — | — |
| ${}^{65}$Zn | 65 | 35 | L?-pending | pending | binding_energy | — | 567.0773 | — | — |
| ${}^{66}$Zn | 66 | 36 | L?-pending | pending | binding_energy | — | 578.1358 | — | — |
| ${}^{67}$Zn | 67 | 37 | L?-pending | pending | binding_energy | — | 585.1883 | — | — |
| ${}^{68}$Zn | 68 | 38 | L?-pending | pending | binding_energy | — | 595.3864 | — | — |
| ${}^{69}$Zn | 69 | 39 | L?-pending | pending | binding_energy | — | 601.8684 | — | — |
| ${}^{70}$Zn | 70 | 40 | L?-pending | pending | binding_energy | — | 611.0866 | — | — |
| ${}^{71}$Zn | 71 | 41 | L?-pending | pending | binding_energy | — | 616.9220 | — | — |
| ${}^{72}$Zn | 72 | 42 | L?-pending | pending | binding_energy | — | 625.8100 | — | — |
| ${}^{73}$Zn | 73 | 43 | L?-pending | pending | binding_energy | — | 631.3292 | — | — |
| ${}^{74}$Zn | 74 | 44 | L?-pending | pending | binding_energy | — | 639.5638 | — | — |
| ${}^{75}$Zn | 75 | 45 | L?-pending | pending | binding_energy | — | 644.4374 | — | — |
| ${}^{76}$Zn | 76 | 46 | L?-pending | pending | binding_energy | — | 652.2528 | — | — |
| ${}^{77}$Zn | 77 | 47 | L?-pending | pending | binding_energy | — | 656.8103 | — | — |
| ${}^{78}$Zn | 78 | 48 | L?-pending | pending | binding_energy | — | 663.5756 | — | — |
| ${}^{79}$Zn | 79 | 49 | L?-pending | pending | binding_energy | — | 667.5960 | — | — |
| ${}^{80}$Zn | 80 | 50 | L?-pending | pending | binding_energy | — | 673.8837 | — | — |
| ${}^{81}$Zn | 81 | 51 | L?-pending | pending | binding_energy | — | 676.5060 | — | — |
| ${}^{82}$Zn | 82 | 52 | L?-pending | pending | binding_energy | — | 680.6916 | — | — |
| ${}^{83}$Zn | 83 | 53 | L?-pending | pending | binding_energy | — | 682.7580 | — | — |
| ${}^{84}$Zn | 84 | 54 | L?-pending | pending | binding_energy | — | 686.3640 | — | — |
| ${}^{85}$Zn | 85 | 55 | L?-pending | pending | binding_energy | — | 687.6500 | — | — |
| ${}^{86}$Zn | 86 | 56 | L?-pending | pending | binding_energy | — | 690.7520 | — | — |

### Gallium (Z = 31)

_0 of 33 isotopes with a framework prediction; 0 of 33 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{56}$Ga | 56 | 25 | L?-pending | pending | binding_energy | — | 431.5920 | — | — |
| ${}^{57}$Ga | 57 | 26 | L?-pending | pending | binding_energy | — | 451.2120 | — | — |
| ${}^{58}$Ga | 58 | 27 | L?-pending | pending | binding_energy | — | 467.4220 | — | — |
| ${}^{59}$Ga | 59 | 28 | L?-pending | pending | binding_energy | — | 485.6880 | — | — |
| ${}^{60}$Ga | 60 | 29 | L?-pending | pending | binding_energy | — | 499.6200 | — | — |
| ${}^{61}$Ga | 61 | 30 | L?-pending | pending | binding_energy | — | 515.2323 | — | — |
| ${}^{62}$Ga | 62 | 31 | L?-pending | pending | binding_energy | — | 528.1560 | — | — |
| ${}^{63}$Ga | 63 | 32 | L?-pending | pending | binding_energy | — | 540.7874 | — | — |
| ${}^{64}$Ga | 64 | 33 | L?-pending | pending | binding_energy | — | 551.1444 | — | — |
| ${}^{65}$Ga | 65 | 34 | L?-pending | pending | binding_energy | — | 563.0404 | — | — |
| ${}^{66}$Ga | 66 | 35 | L?-pending | pending | binding_energy | — | 572.1780 | — | — |
| ${}^{67}$Ga | 67 | 36 | L?-pending | pending | binding_energy | — | 583.4047 | — | — |
| ${}^{68}$Ga | 68 | 37 | L?-pending | pending | binding_energy | — | 591.6829 | — | — |
| ${}^{69}$Ga | 69 | 38 | L?-pending | pending | binding_energy | — | 601.9960 | — | — |
| ${}^{70}$Ga | 70 | 39 | L?-pending | pending | binding_energy | — | 609.6497 | — | — |
| ${}^{71}$Ga | 71 | 40 | L?-pending | pending | binding_energy | — | 618.9500 | — | — |
| ${}^{72}$Ga | 72 | 41 | L?-pending | pending | binding_energy | — | 625.4704 | — | — |
| ${}^{73}$Ga | 73 | 42 | L?-pending | pending | binding_energy | — | 634.6528 | — | — |
| ${}^{74}$Ga | 74 | 43 | L?-pending | pending | binding_energy | — | 641.0744 | — | — |
| ${}^{75}$Ga | 75 | 44 | L?-pending | pending | binding_energy | — | 649.5567 | — | — |
| ${}^{76}$Ga | 76 | 45 | L?-pending | pending | binding_energy | — | 655.4641 | — | — |
| ${}^{77}$Ga | 77 | 46 | L?-pending | pending | binding_energy | — | 663.2311 | — | — |
| ${}^{78}$Ga | 78 | 47 | L?-pending | pending | binding_energy | — | 669.0141 | — | — |
| ${}^{79}$Ga | 79 | 48 | L?-pending | pending | binding_energy | — | 675.9297 | — | — |
| ${}^{80}$Ga | 80 | 49 | L?-pending | pending | binding_energy | — | 680.6764 | — | — |
| ${}^{81}$Ga | 81 | 50 | L?-pending | pending | binding_energy | — | 687.1520 | — | — |
| ${}^{82}$Ga | 82 | 51 | L?-pending | pending | binding_energy | — | 690.5261 | — | — |
| ${}^{83}$Ga | 83 | 52 | L?-pending | pending | binding_energy | — | 694.9238 | — | — |
| ${}^{84}$Ga | 84 | 53 | L?-pending | pending | binding_energy | — | 697.8321 | — | — |
| ${}^{85}$Ga | 85 | 54 | L?-pending | pending | binding_energy | — | 701.5533 | — | — |
| ${}^{86}$Ga | 86 | 55 | L?-pending | pending | binding_energy | — | 703.6520 | — | — |
| ${}^{87}$Ga | 87 | 56 | L?-pending | pending | binding_energy | — | 706.7880 | — | — |
| ${}^{88}$Ga | 88 | 57 | L?-pending | pending | binding_energy | — | 708.4000 | — | — |

### Germanium (Z = 32)

_0 of 33 isotopes with a framework prediction; 0 of 33 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{58}$Ge | 58 | 26 | L?-pending | pending | binding_energy | — | 450.6600 | — | — |
| ${}^{59}$Ge | 59 | 27 | L?-pending | pending | binding_energy | — | 467.5160 | — | — |
| ${}^{60}$Ge | 60 | 28 | L?-pending | pending | binding_energy | — | 486.7800 | — | — |
| ${}^{61}$Ge | 61 | 29 | L?-pending | pending | binding_energy | — | 501.1150 | — | — |
| ${}^{62}$Ge | 62 | 30 | L?-pending | pending | binding_energy | — | 517.5140 | — | — |
| ${}^{63}$Ge | 63 | 31 | L?-pending | pending | binding_energy | — | 530.3792 | — | — |
| ${}^{64}$Ge | 64 | 32 | L?-pending | pending | binding_energy | — | 545.8448 | — | — |
| ${}^{65}$Ge | 65 | 33 | L?-pending | pending | binding_energy | — | 556.0788 | — | — |
| ${}^{66}$Ge | 66 | 34 | L?-pending | pending | binding_energy | — | 569.2789 | — | — |
| ${}^{67}$Ge | 67 | 35 | L?-pending | pending | binding_energy | — | 578.4169 | — | — |
| ${}^{68}$Ge | 68 | 36 | L?-pending | pending | binding_energy | — | 590.7933 | — | — |
| ${}^{69}$Ge | 69 | 37 | L?-pending | pending | binding_energy | — | 598.9865 | — | — |
| ${}^{70}$Ge | 70 | 38 | L?-pending | pending | binding_energy | — | 610.5192 | — | — |
| ${}^{71}$Ge | 71 | 39 | L?-pending | pending | binding_energy | — | 617.9351 | — | — |
| ${}^{72}$Ge | 72 | 40 | L?-pending | pending | binding_energy | — | 628.6857 | — | — |
| ${}^{73}$Ge | 73 | 41 | L?-pending | pending | binding_energy | — | 635.4686 | — | — |
| ${}^{74}$Ge | 74 | 42 | L?-pending | pending | binding_energy | — | 645.6649 | — | — |
| ${}^{75}$Ge | 75 | 43 | L?-pending | pending | binding_energy | — | 652.1707 | — | — |
| ${}^{76}$Ge | 76 | 44 | L?-pending | pending | binding_energy | — | 661.5980 | — | — |
| ${}^{77}$Ge | 77 | 45 | L?-pending | pending | binding_energy | — | 667.6693 | — | — |
| ${}^{78}$Ge | 78 | 46 | L?-pending | pending | binding_energy | — | 676.3898 | — | — |
| ${}^{79}$Ge | 79 | 47 | L?-pending | pending | binding_energy | — | 682.1262 | — | — |
| ${}^{80}$Ge | 80 | 48 | L?-pending | pending | binding_energy | — | 690.2057 | — | — |
| ${}^{81}$Ge | 81 | 49 | L?-pending | pending | binding_energy | — | 695.0334 | — | — |
| ${}^{82}$Ge | 82 | 50 | L?-pending | pending | binding_energy | — | 702.2280 | — | — |
| ${}^{83}$Ge | 83 | 51 | L?-pending | pending | binding_energy | — | 705.8607 | — | — |
| ${}^{84}$Ge | 84 | 52 | L?-pending | pending | binding_energy | — | 711.1040 | — | — |
| ${}^{85}$Ge | 85 | 53 | L?-pending | pending | binding_energy | — | 714.1504 | — | — |
| ${}^{86}$Ge | 86 | 54 | L?-pending | pending | binding_energy | — | 718.4982 | — | — |
| ${}^{87}$Ge | 87 | 55 | L?-pending | pending | binding_energy | — | 720.7950 | — | — |
| ${}^{88}$Ge | 88 | 56 | L?-pending | pending | binding_energy | — | 724.7680 | — | — |
| ${}^{89}$Ge | 89 | 57 | L?-pending | pending | binding_energy | — | 726.3290 | — | — |
| ${}^{90}$Ge | 90 | 58 | L?-pending | pending | binding_energy | — | 729.8100 | — | — |

### Arsenic (Z = 33)

_0 of 33 isotopes with a framework prediction; 0 of 33 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{60}$As | 60 | 27 | L?-pending | pending | binding_energy | — | 464.1000 | — | — |
| ${}^{61}$As | 61 | 28 | L?-pending | pending | binding_energy | — | 483.7300 | — | — |
| ${}^{62}$As | 62 | 29 | L?-pending | pending | binding_energy | — | 499.0380 | — | — |
| ${}^{63}$As | 63 | 30 | L?-pending | pending | binding_energy | — | 516.1590 | — | — |
| ${}^{64}$As | 64 | 31 | L?-pending | pending | binding_energy | — | 530.3040 | — | — |
| ${}^{65}$As | 65 | 32 | L?-pending | pending | binding_energy | — | 545.7553 | — | — |
| ${}^{66}$As | 66 | 33 | L?-pending | pending | binding_energy | — | 558.9146 | — | — |
| ${}^{67}$As | 67 | 34 | L?-pending | pending | binding_energy | — | 571.5481 | — | — |
| ${}^{68}$As | 68 | 35 | L?-pending | pending | binding_energy | — | 581.9267 | — | — |
| ${}^{69}$As | 69 | 36 | L?-pending | pending | binding_energy | — | 594.2157 | — | — |
| ${}^{70}$As | 70 | 37 | L?-pending | pending | binding_energy | — | 603.5088 | — | — |
| ${}^{71}$As | 71 | 38 | L?-pending | pending | binding_energy | — | 615.1394 | — | — |
| ${}^{72}$As | 72 | 39 | L?-pending | pending | binding_energy | — | 623.5473 | — | — |
| ${}^{73}$As | 73 | 40 | L?-pending | pending | binding_energy | — | 634.3415 | — | — |
| ${}^{74}$As | 74 | 41 | L?-pending | pending | binding_energy | — | 642.3201 | — | — |
| ${}^{75}$As | 75 | 42 | L?-pending | pending | binding_energy | — | 652.5656 | — | — |
| ${}^{76}$As | 76 | 43 | L?-pending | pending | binding_energy | — | 659.8941 | — | — |
| ${}^{77}$As | 77 | 44 | L?-pending | pending | binding_energy | — | 669.5904 | — | — |
| ${}^{78}$As | 78 | 45 | L?-pending | pending | binding_energy | — | 676.5623 | — | — |
| ${}^{79}$As | 79 | 46 | L?-pending | pending | binding_energy | — | 685.4528 | — | — |
| ${}^{80}$As | 80 | 47 | L?-pending | pending | binding_energy | — | 692.1026 | — | — |
| ${}^{81}$As | 81 | 48 | L?-pending | pending | binding_energy | — | 700.4926 | — | — |
| ${}^{82}$As | 82 | 49 | L?-pending | pending | binding_energy | — | 706.1361 | — | — |
| ${}^{83}$As | 83 | 50 | L?-pending | pending | binding_energy | — | 713.7713 | — | — |
| ${}^{84}$As | 84 | 51 | L?-pending | pending | binding_energy | — | 718.0268 | — | — |
| ${}^{85}$As | 85 | 52 | L?-pending | pending | binding_energy | — | 723.4337 | — | — |
| ${}^{86}$As | 86 | 53 | L?-pending | pending | binding_energy | — | 727.2780 | — | — |
| ${}^{87}$As | 87 | 54 | L?-pending | pending | binding_energy | — | 732.0051 | — | — |
| ${}^{88}$As | 88 | 55 | L?-pending | pending | binding_energy | — | 734.8880 | — | — |
| ${}^{89}$As | 89 | 56 | L?-pending | pending | binding_energy | — | 739.0560 | — | — |
| ${}^{90}$As | 90 | 57 | L?-pending | pending | binding_energy | — | 741.6000 | — | — |
| ${}^{91}$As | 91 | 58 | L?-pending | pending | binding_energy | — | 745.1990 | — | — |
| ${}^{92}$As | 92 | 59 | L?-pending | pending | binding_energy | — | 747.1320 | — | — |

### Selenium (Z = 34)

_0 of 33 isotopes with a framework prediction; 0 of 33 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{63}$Se | 63 | 29 | L?-pending | pending | binding_energy | — | 498.7710 | — | — |
| ${}^{64}$Se | 64 | 30 | L?-pending | pending | binding_energy | — | 516.8000 | — | — |
| ${}^{65}$Se | 65 | 31 | L?-pending | pending | binding_energy | — | 531.0500 | — | — |
| ${}^{66}$Se | 66 | 32 | L?-pending | pending | binding_energy | — | 547.8000 | — | — |
| ${}^{67}$Se | 67 | 33 | L?-pending | pending | binding_energy | — | 560.7588 | — | — |
| ${}^{68}$Se | 68 | 34 | L?-pending | pending | binding_energy | — | 576.4393 | — | — |
| ${}^{69}$Se | 69 | 35 | L?-pending | pending | binding_energy | — | 586.7559 | — | — |
| ${}^{70}$Se | 70 | 36 | L?-pending | pending | binding_energy | — | 600.3224 | — | — |
| ${}^{71}$Se | 71 | 37 | L?-pending | pending | binding_energy | — | 609.6103 | — | — |
| ${}^{72}$Se | 72 | 38 | L?-pending | pending | binding_energy | — | 622.4033 | — | — |
| ${}^{73}$Se | 73 | 39 | L?-pending | pending | binding_energy | — | 630.8338 | — | — |
| ${}^{74}$Se | 74 | 40 | L?-pending | pending | binding_energy | — | 642.8909 | — | — |
| ${}^{75}$Se | 75 | 41 | L?-pending | pending | binding_energy | — | 650.9185 | — | — |
| ${}^{76}$Se | 76 | 42 | L?-pending | pending | binding_energy | — | 662.0723 | — | — |
| ${}^{77}$Se | 77 | 43 | L?-pending | pending | binding_energy | — | 669.4912 | — | — |
| ${}^{78}$Se | 78 | 44 | L?-pending | pending | binding_energy | — | 679.9890 | — | — |
| ${}^{79}$Se | 79 | 45 | L?-pending | pending | binding_energy | — | 686.9518 | — | — |
| ${}^{80}$Se | 80 | 46 | L?-pending | pending | binding_energy | — | 696.8651 | — | — |
| ${}^{81}$Se | 81 | 47 | L?-pending | pending | binding_energy | — | 703.5660 | — | — |
| ${}^{82}$Se | 82 | 48 | L?-pending | pending | binding_energy | — | 712.8422 | — | — |
| ${}^{83}$Se | 83 | 49 | L?-pending | pending | binding_energy | — | 718.6601 | — | — |
| ${}^{84}$Se | 84 | 50 | L?-pending | pending | binding_energy | — | 727.3387 | — | — |
| ${}^{85}$Se | 85 | 51 | L?-pending | pending | binding_energy | — | 731.8759 | — | — |
| ${}^{86}$Se | 86 | 52 | L?-pending | pending | binding_energy | — | 738.0367 | — | — |
| ${}^{87}$Se | 87 | 53 | L?-pending | pending | binding_energy | — | 742.0310 | — | — |
| ${}^{88}$Se | 88 | 54 | L?-pending | pending | binding_energy | — | 747.5604 | — | — |
| ${}^{89}$Se | 89 | 55 | L?-pending | pending | binding_energy | — | 750.7399 | — | — |
| ${}^{90}$Se | 90 | 56 | L?-pending | pending | binding_energy | — | 755.6190 | — | — |
| ${}^{91}$Se | 91 | 57 | L?-pending | pending | binding_energy | — | 758.4703 | — | — |
| ${}^{92}$Se | 92 | 58 | L?-pending | pending | binding_energy | — | 762.6800 | — | — |
| ${}^{93}$Se | 93 | 59 | L?-pending | pending | binding_energy | — | 764.9250 | — | — |
| ${}^{94}$Se | 94 | 60 | L?-pending | pending | binding_energy | — | 768.9200 | — | — |
| ${}^{95}$Se | 95 | 61 | L?-pending | pending | binding_energy | — | 770.6400 | — | — |

### Bromine (Z = 35)

_0 of 34 isotopes with a framework prediction; 0 of 34 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{65}$Br | 65 | 30 | L?-pending | pending | binding_energy | — | 513.7600 | — | — |
| ${}^{66}$Br | 66 | 31 | L?-pending | pending | binding_energy | — | 528.9240 | — | — |
| ${}^{67}$Br | 67 | 32 | L?-pending | pending | binding_energy | — | 545.9160 | — | — |
| ${}^{68}$Br | 68 | 33 | L?-pending | pending | binding_energy | — | 560.2520 | — | — |
| ${}^{69}$Br | 69 | 34 | L?-pending | pending | binding_energy | — | 575.7983 | — | — |
| ${}^{70}$Br | 70 | 35 | L?-pending | pending | binding_energy | — | 589.0357 | — | — |
| ${}^{71}$Br | 71 | 36 | L?-pending | pending | binding_energy | — | 602.1839 | — | — |
| ${}^{72}$Br | 72 | 37 | L?-pending | pending | binding_energy | — | 612.8145 | — | — |
| ${}^{73}$Br | 73 | 38 | L?-pending | pending | binding_energy | — | 625.4699 | — | — |
| ${}^{74}$Br | 74 | 39 | L?-pending | pending | binding_energy | — | 635.1836 | — | — |
| ${}^{75}$Br | 75 | 40 | L?-pending | pending | binding_energy | — | 647.0737 | — | — |
| ${}^{76}$Br | 76 | 41 | L?-pending | pending | binding_energy | — | 656.3271 | — | — |
| ${}^{77}$Br | 77 | 42 | L?-pending | pending | binding_energy | — | 667.3442 | — | — |
| ${}^{78}$Br | 78 | 43 | L?-pending | pending | binding_energy | — | 675.6328 | — | — |
| ${}^{79}$Br | 79 | 44 | L?-pending | pending | binding_energy | — | 686.3201 | — | — |
| ${}^{80}$Br | 80 | 45 | L?-pending | pending | binding_energy | — | 694.2123 | — | — |
| ${}^{81}$Br | 81 | 46 | L?-pending | pending | binding_energy | — | 704.3717 | — | — |
| ${}^{82}$Br | 82 | 47 | L?-pending | pending | binding_energy | — | 711.9646 | — | — |
| ${}^{83}$Br | 83 | 48 | L?-pending | pending | binding_energy | — | 721.5510 | — | — |
| ${}^{84}$Br | 84 | 49 | L?-pending | pending | binding_energy | — | 728.3917 | — | — |
| ${}^{85}$Br | 85 | 50 | L?-pending | pending | binding_energy | — | 737.2554 | — | — |
| ${}^{86}$Br | 86 | 51 | L?-pending | pending | binding_energy | — | 742.3835 | — | — |
| ${}^{87}$Br | 87 | 52 | L?-pending | pending | binding_energy | — | 748.7142 | — | — |
| ${}^{88}$Br | 88 | 53 | L?-pending | pending | binding_energy | — | 753.6098 | — | — |
| ${}^{89}$Br | 89 | 54 | L?-pending | pending | binding_energy | — | 759.2394 | — | — |
| ${}^{90}$Br | 90 | 55 | L?-pending | pending | binding_energy | — | 763.0368 | — | — |
| ${}^{91}$Br | 91 | 56 | L?-pending | pending | binding_energy | — | 768.2151 | — | — |
| ${}^{92}$Br | 92 | 57 | L?-pending | pending | binding_energy | — | 771.4119 | — | — |
| ${}^{93}$Br | 93 | 58 | L?-pending | pending | binding_energy | — | 776.1407 | — | — |
| ${}^{94}$Br | 94 | 59 | L?-pending | pending | binding_energy | — | 778.9780 | — | — |
| ${}^{95}$Br | 95 | 60 | L?-pending | pending | binding_energy | — | 783.2750 | — | — |
| ${}^{96}$Br | 96 | 61 | L?-pending | pending | binding_energy | — | 785.6640 | — | — |
| ${}^{97}$Br | 97 | 62 | L?-pending | pending | binding_energy | — | 789.5800 | — | — |
| ${}^{98}$Br | 98 | 63 | L?-pending | pending | binding_energy | — | 791.6440 | — | — |

### Krypton (Z = 36)

_0 of 35 isotopes with a framework prediction; 0 of 35 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{67}$Kr | 67 | 31 | L?-pending | pending | binding_energy | — | 528.1610 | — | — |
| ${}^{68}$Kr | 68 | 32 | L?-pending | pending | binding_energy | — | 546.3120 | — | — |
| ${}^{69}$Kr | 69 | 33 | L?-pending | pending | binding_energy | — | 560.9010 | — | — |
| ${}^{70}$Kr | 70 | 34 | L?-pending | pending | binding_energy | — | 577.9200 | — | — |
| ${}^{71}$Kr | 71 | 35 | L?-pending | pending | binding_energy | — | 591.2263 | — | — |
| ${}^{72}$Kr | 72 | 36 | L?-pending | pending | binding_energy | — | 606.9110 | — | — |
| ${}^{73}$Kr | 73 | 37 | L?-pending | pending | binding_energy | — | 617.5935 | — | — |
| ${}^{74}$Kr | 74 | 38 | L?-pending | pending | binding_energy | — | 631.4449 | — | — |
| ${}^{75}$Kr | 75 | 39 | L?-pending | pending | binding_energy | — | 641.5080 | — | — |
| ${}^{76}$Kr | 76 | 40 | L?-pending | pending | binding_energy | — | 654.2694 | — | — |
| ${}^{77}$Kr | 77 | 41 | L?-pending | pending | binding_energy | — | 663.4964 | — | — |
| ${}^{78}$Kr | 78 | 42 | L?-pending | pending | binding_energy | — | 675.5766 | — | — |
| ${}^{79}$Kr | 79 | 43 | L?-pending | pending | binding_energy | — | 683.9119 | — | — |
| ${}^{80}$Kr | 80 | 44 | L?-pending | pending | binding_energy | — | 695.4344 | — | — |
| ${}^{81}$Kr | 81 | 45 | L?-pending | pending | binding_energy | — | 703.3085 | — | — |
| ${}^{82}$Kr | 82 | 46 | L?-pending | pending | binding_energy | — | 714.2754 | — | — |
| ${}^{83}$Kr | 83 | 47 | L?-pending | pending | binding_energy | — | 721.7455 | — | — |
| ${}^{84}$Kr | 84 | 48 | L?-pending | pending | binding_energy | — | 732.2656 | — | — |
| ${}^{85}$Kr | 85 | 49 | L?-pending | pending | binding_energy | — | 739.3779 | — | — |
| ${}^{86}$Kr | 86 | 50 | L?-pending | pending | binding_energy | — | 749.2345 | — | — |
| ${}^{87}$Kr | 87 | 51 | L?-pending | pending | binding_energy | — | 754.7497 | — | — |
| ${}^{88}$Kr | 88 | 52 | L?-pending | pending | binding_energy | — | 761.8028 | — | — |
| ${}^{89}$Kr | 89 | 53 | L?-pending | pending | binding_energy | — | 766.7186 | — | — |
| ${}^{90}$Kr | 90 | 54 | L?-pending | pending | binding_energy | — | 773.2134 | — | — |
| ${}^{91}$Kr | 91 | 55 | L?-pending | pending | binding_energy | — | 777.2994 | — | — |
| ${}^{92}$Kr | 92 | 56 | L?-pending | pending | binding_energy | — | 783.1661 | — | — |
| ${}^{93}$Kr | 93 | 57 | L?-pending | pending | binding_energy | — | 786.6041 | — | — |
| ${}^{94}$Kr | 94 | 58 | L?-pending | pending | binding_energy | — | 791.8872 | — | — |
| ${}^{95}$Kr | 95 | 59 | L?-pending | pending | binding_energy | — | 794.7696 | — | — |
| ${}^{96}$Kr | 96 | 60 | L?-pending | pending | binding_energy | — | 799.7637 | — | — |
| ${}^{97}$Kr | 97 | 61 | L?-pending | pending | binding_energy | — | 802.1769 | — | — |
| ${}^{98}$Kr | 98 | 62 | L?-pending | pending | binding_energy | — | 806.9320 | — | — |
| ${}^{99}$Kr | 99 | 63 | L?-pending | pending | binding_energy | — | 809.3250 | — | — |
| ${}^{100}$Kr | 100 | 64 | L?-pending | pending | binding_energy | — | 813.4000 | — | — |
| ${}^{101}$Kr | 101 | 65 | L?-pending | pending | binding_energy | — | 815.5750 | — | — |

### Rubidium (Z = 37)

_0 of 34 isotopes with a framework prediction; 0 of 34 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{71}$Rb | 71 | 34 | L?-pending | pending | binding_energy | — | 576.3780 | — | — |
| ${}^{72}$Rb | 72 | 35 | L?-pending | pending | binding_energy | — | 590.5440 | — | — |
| ${}^{73}$Rb | 73 | 36 | L?-pending | pending | binding_energy | — | 606.2710 | — | — |
| ${}^{74}$Rb | 74 | 37 | L?-pending | pending | binding_energy | — | 620.2467 | — | — |
| ${}^{75}$Rb | 75 | 38 | L?-pending | pending | binding_energy | — | 633.6207 | — | — |
| ${}^{76}$Rb | 76 | 39 | L?-pending | pending | binding_energy | — | 644.9524 | — | — |
| ${}^{77}$Rb | 77 | 40 | L?-pending | pending | binding_energy | — | 657.3751 | — | — |
| ${}^{78}$Rb | 78 | 41 | L?-pending | pending | binding_energy | — | 667.5514 | — | — |
| ${}^{79}$Rb | 79 | 42 | L?-pending | pending | binding_energy | — | 679.4901 | — | — |
| ${}^{80}$Rb | 80 | 43 | L?-pending | pending | binding_energy | — | 688.9341 | — | — |
| ${}^{81}$Rb | 81 | 44 | L?-pending | pending | binding_energy | — | 700.2866 | — | — |
| ${}^{82}$Rb | 82 | 45 | L?-pending | pending | binding_energy | — | 709.0891 | — | — |
| ${}^{83}$Rb | 83 | 46 | L?-pending | pending | binding_energy | — | 720.0432 | — | — |
| ${}^{84}$Rb | 84 | 47 | L?-pending | pending | binding_energy | — | 728.8028 | — | — |
| ${}^{85}$Rb | 85 | 48 | L?-pending | pending | binding_energy | — | 739.2825 | — | — |
| ${}^{86}$Rb | 86 | 49 | L?-pending | pending | binding_energy | — | 747.9335 | — | — |
| ${}^{87}$Rb | 87 | 50 | L?-pending | pending | binding_energy | — | 757.8556 | — | — |
| ${}^{88}$Rb | 88 | 51 | L?-pending | pending | binding_energy | — | 763.9382 | — | — |
| ${}^{89}$Rb | 89 | 52 | L?-pending | pending | binding_energy | — | 771.1129 | — | — |
| ${}^{90}$Rb | 90 | 53 | L?-pending | pending | binding_energy | — | 776.8374 | — | — |
| ${}^{91}$Rb | 91 | 54 | L?-pending | pending | binding_energy | — | 783.2882 | — | — |
| ${}^{92}$Rb | 92 | 55 | L?-pending | pending | binding_energy | — | 788.3869 | — | — |
| ${}^{93}$Rb | 93 | 56 | L?-pending | pending | binding_energy | — | 794.3056 | — | — |
| ${}^{94}$Rb | 94 | 57 | L?-pending | pending | binding_energy | — | 798.3199 | — | — |
| ${}^{95}$Rb | 95 | 58 | L?-pending | pending | binding_energy | — | 803.7187 | — | — |
| ${}^{96}$Rb | 96 | 59 | L?-pending | pending | binding_energy | — | 807.2540 | — | — |
| ${}^{97}$Rb | 97 | 60 | L?-pending | pending | binding_energy | — | 812.4902 | — | — |
| ${}^{98}$Rb | 98 | 61 | L?-pending | pending | binding_energy | — | 816.4115 | — | — |
| ${}^{99}$Rb | 99 | 62 | L?-pending | pending | binding_energy | — | 821.2348 | — | — |
| ${}^{100}$Rb | 100 | 63 | L?-pending | pending | binding_energy | — | 824.4508 | — | — |
| ${}^{101}$Rb | 101 | 64 | L?-pending | pending | binding_energy | — | 828.8237 | — | — |
| ${}^{102}$Rb | 102 | 65 | L?-pending | pending | binding_energy | — | 831.5799 | — | — |
| ${}^{103}$Rb | 103 | 66 | L?-pending | pending | binding_energy | — | 835.5360 | — | — |
| ${}^{104}$Rb | 104 | 67 | L?-pending | pending | binding_energy | — | 837.9280 | — | — |

### Strontium (Z = 38)

_0 of 35 isotopes with a framework prediction; 0 of 35 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{73}$Sr | 73 | 35 | L?-pending | pending | binding_energy | — | 591.4460 | — | — |
| ${}^{74}$Sr | 74 | 36 | L?-pending | pending | binding_energy | — | 608.3540 | — | — |
| ${}^{75}$Sr | 75 | 37 | L?-pending | pending | binding_energy | — | 622.2384 | — | — |
| ${}^{76}$Sr | 76 | 38 | L?-pending | pending | binding_energy | — | 637.9386 | — | — |
| ${}^{77}$Sr | 77 | 39 | L?-pending | pending | binding_energy | — | 649.5657 | — | — |
| ${}^{78}$Sr | 78 | 40 | L?-pending | pending | binding_energy | — | 663.0076 | — | — |
| ${}^{79}$Sr | 79 | 41 | L?-pending | pending | binding_energy | — | 673.3846 | — | — |
| ${}^{80}$Sr | 80 | 42 | L?-pending | pending | binding_energy | — | 686.2877 | — | — |
| ${}^{81}$Sr | 81 | 43 | L?-pending | pending | binding_energy | — | 695.5757 | — | — |
| ${}^{82}$Sr | 82 | 44 | L?-pending | pending | binding_energy | — | 708.1290 | — | — |
| ${}^{83}$Sr | 83 | 45 | L?-pending | pending | binding_energy | — | 716.9878 | — | — |
| ${}^{84}$Sr | 84 | 46 | L?-pending | pending | binding_energy | — | 728.9111 | — | — |
| ${}^{85}$Sr | 85 | 47 | L?-pending | pending | binding_energy | — | 737.4361 | — | — |
| ${}^{86}$Sr | 86 | 48 | L?-pending | pending | binding_energy | — | 748.9273 | — | — |
| ${}^{87}$Sr | 87 | 49 | L?-pending | pending | binding_energy | — | 757.3556 | — | — |
| ${}^{88}$Sr | 88 | 50 | L?-pending | pending | binding_energy | — | 768.4684 | — | — |
| ${}^{89}$Sr | 89 | 51 | L?-pending | pending | binding_energy | — | 774.8271 | — | — |
| ${}^{90}$Sr | 90 | 52 | L?-pending | pending | binding_energy | — | 782.6404 | — | — |
| ${}^{91}$Sr | 91 | 53 | L?-pending | pending | binding_energy | — | 788.4127 | — | — |
| ${}^{92}$Sr | 92 | 54 | L?-pending | pending | binding_energy | — | 795.6994 | — | — |
| ${}^{93}$Sr | 93 | 55 | L?-pending | pending | binding_energy | — | 800.9892 | — | — |
| ${}^{94}$Sr | 94 | 56 | L?-pending | pending | binding_energy | — | 807.8204 | — | — |
| ${}^{95}$Sr | 95 | 57 | L?-pending | pending | binding_energy | — | 812.1633 | — | — |
| ${}^{96}$Sr | 96 | 58 | L?-pending | pending | binding_energy | — | 818.0356 | — | — |
| ${}^{97}$Sr | 97 | 59 | L?-pending | pending | binding_energy | — | 821.7693 | — | — |
| ${}^{98}$Sr | 98 | 60 | L?-pending | pending | binding_energy | — | 827.6824 | — | — |
| ${}^{99}$Sr | 99 | 61 | L?-pending | pending | binding_energy | — | 831.8498 | — | — |
| ${}^{100}$Sr | 100 | 62 | L?-pending | pending | binding_energy | — | 837.2201 | — | — |
| ${}^{101}$Sr | 101 | 63 | L?-pending | pending | binding_energy | — | 840.7989 | — | — |
| ${}^{102}$Sr | 102 | 64 | L?-pending | pending | binding_energy | — | 845.7046 | — | — |
| ${}^{103}$Sr | 103 | 65 | L?-pending | pending | binding_energy | — | 848.9260 | — | — |
| ${}^{104}$Sr | 104 | 66 | L?-pending | pending | binding_energy | — | 853.4240 | — | — |
| ${}^{105}$Sr | 105 | 67 | L?-pending | pending | binding_energy | — | 855.9600 | — | — |
| ${}^{106}$Sr | 106 | 68 | L?-pending | pending | binding_energy | — | 860.0840 | — | — |
| ${}^{107}$Sr | 107 | 69 | L?-pending | pending | binding_energy | — | 862.0990 | — | — |

### Yttrium (Z = 39)

_0 of 35 isotopes with a framework prediction; 0 of 35 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{75}$Y | 75 | 36 | L?-pending | pending | binding_energy | — | 606.6750 | — | — |
| ${}^{76}$Y | 76 | 37 | L?-pending | pending | binding_energy | — | 621.1480 | — | — |
| ${}^{77}$Y | 77 | 38 | L?-pending | pending | binding_energy | — | 637.4060 | — | — |
| ${}^{78}$Y | 78 | 39 | L?-pending | pending | binding_energy | — | 651.2220 | — | — |
| ${}^{79}$Y | 79 | 40 | L?-pending | pending | binding_energy | — | 664.9255 | — | — |
| ${}^{80}$Y | 80 | 41 | L?-pending | pending | binding_energy | — | 676.3421 | — | — |
| ${}^{81}$Y | 81 | 42 | L?-pending | pending | binding_energy | — | 688.9782 | — | — |
| ${}^{82}$Y | 82 | 43 | L?-pending | pending | binding_energy | — | 699.4006 | — | — |
| ${}^{83}$Y | 83 | 44 | L?-pending | pending | binding_energy | — | 711.6135 | — | — |
| ${}^{84}$Y | 84 | 45 | L?-pending | pending | binding_energy | — | 721.3736 | — | — |
| ${}^{85}$Y | 85 | 46 | L?-pending | pending | binding_energy | — | 733.3926 | — | — |
| ${}^{86}$Y | 86 | 47 | L?-pending | pending | binding_energy | — | 742.9049 | — | — |
| ${}^{87}$Y | 87 | 48 | L?-pending | pending | binding_energy | — | 754.7115 | — | — |
| ${}^{88}$Y | 88 | 49 | L?-pending | pending | binding_energy | — | 764.0635 | — | — |
| ${}^{89}$Y | 89 | 50 | L?-pending | pending | binding_energy | — | 775.5470 | — | — |
| ${}^{90}$Y | 90 | 51 | L?-pending | pending | binding_energy | — | 782.4040 | — | — |
| ${}^{91}$Y | 91 | 52 | L?-pending | pending | binding_energy | — | 790.3297 | — | — |
| ${}^{92}$Y | 92 | 53 | L?-pending | pending | binding_energy | — | 796.8662 | — | — |
| ${}^{93}$Y | 93 | 54 | L?-pending | pending | binding_energy | — | 804.3482 | — | — |
| ${}^{94}$Y | 94 | 55 | L?-pending | pending | binding_energy | — | 810.5438 | — | — |
| ${}^{95}$Y | 95 | 56 | L?-pending | pending | binding_energy | — | 817.4716 | — | — |
| ${}^{96}$Y | 96 | 57 | L?-pending | pending | binding_energy | — | 822.6650 | — | — |
| ${}^{97}$Y | 97 | 58 | L?-pending | pending | binding_energy | — | 828.5218 | — | — |
| ${}^{98}$Y | 98 | 59 | L?-pending | pending | binding_energy | — | 832.7664 | — | — |
| ${}^{99}$Y | 99 | 60 | L?-pending | pending | binding_energy | — | 839.1927 | — | — |
| ${}^{100}$Y | 100 | 61 | L?-pending | pending | binding_energy | — | 843.9415 | — | — |
| ${}^{101}$Y | 101 | 62 | L?-pending | pending | binding_energy | — | 849.7464 | — | — |
| ${}^{102}$Y | 102 | 63 | L?-pending | pending | binding_energy | — | 853.9356 | — | — |
| ${}^{103}$Y | 103 | 64 | L?-pending | pending | binding_energy | — | 859.2913 | — | — |
| ${}^{104}$Y | 104 | 65 | L?-pending | pending | binding_energy | — | 862.9920 | — | — |
| ${}^{105}$Y | 105 | 66 | L?-pending | pending | binding_energy | — | 867.5100 | — | — |
| ${}^{106}$Y | 106 | 67 | L?-pending | pending | binding_energy | — | 870.7900 | — | — |
| ${}^{107}$Y | 107 | 68 | L?-pending | pending | binding_energy | — | 875.0460 | — | — |
| ${}^{108}$Y | 108 | 69 | L?-pending | pending | binding_energy | — | 877.9320 | — | — |
| ${}^{109}$Y | 109 | 70 | L?-pending | pending | binding_energy | — | 881.7010 | — | — |

### Zirconium (Z = 40)

_0 of 37 isotopes with a framework prediction; 0 of 37 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{77}$Zr | 77 | 37 | L?-pending | pending | binding_energy | — | 621.7750 | — | — |
| ${}^{78}$Zr | 78 | 38 | L?-pending | pending | binding_energy | — | 639.1320 | — | — |
| ${}^{79}$Zr | 79 | 39 | L?-pending | pending | binding_energy | — | 653.0930 | — | — |
| ${}^{80}$Zr | 80 | 40 | L?-pending | pending | binding_energy | — | 669.2000 | — | — |
| ${}^{81}$Zr | 81 | 41 | L?-pending | pending | binding_energy | — | 680.0073 | — | — |
| ${}^{82}$Zr | 82 | 42 | L?-pending | pending | binding_energy | — | 694.1683 | — | — |
| ${}^{83}$Zr | 83 | 43 | L?-pending | pending | binding_energy | — | 704.5372 | — | — |
| ${}^{84}$Zr | 84 | 44 | L?-pending | pending | binding_energy | — | 718.1185 | — | — |
| ${}^{85}$Zr | 85 | 45 | L?-pending | pending | binding_energy | — | 727.9433 | — | — |
| ${}^{86}$Zr | 86 | 46 | L?-pending | pending | binding_energy | — | 740.8085 | — | — |
| ${}^{87}$Zr | 87 | 47 | L?-pending | pending | binding_energy | — | 750.2579 | — | — |
| ${}^{88}$Zr | 88 | 48 | L?-pending | pending | binding_energy | — | 762.6110 | — | — |
| ${}^{89}$Zr | 89 | 49 | L?-pending | pending | binding_energy | — | 771.9314 | — | — |
| ${}^{90}$Zr | 90 | 50 | L?-pending | pending | binding_energy | — | 783.8973 | — | — |
| ${}^{91}$Zr | 91 | 51 | L?-pending | pending | binding_energy | — | 791.0917 | — | — |
| ${}^{92}$Zr | 92 | 52 | L?-pending | pending | binding_energy | — | 799.7264 | — | — |
| ${}^{93}$Zr | 93 | 53 | L?-pending | pending | binding_energy | — | 806.4607 | — | — |
| ${}^{94}$Zr | 94 | 54 | L?-pending | pending | binding_energy | — | 814.6794 | — | — |
| ${}^{95}$Zr | 95 | 55 | L?-pending | pending | binding_energy | — | 821.1413 | — | — |
| ${}^{96}$Zr | 96 | 56 | L?-pending | pending | binding_energy | — | 828.9915 | — | — |
| ${}^{97}$Zr | 97 | 57 | L?-pending | pending | binding_energy | — | 834.5607 | — | — |
| ${}^{98}$Zr | 98 | 58 | L?-pending | pending | binding_energy | — | 840.9770 | — | — |
| ${}^{99}$Zr | 99 | 59 | L?-pending | pending | binding_energy | — | 845.3833 | — | — |
| ${}^{100}$Zr | 100 | 60 | L?-pending | pending | binding_energy | — | 852.2107 | — | — |
| ${}^{101}$Zr | 101 | 61 | L?-pending | pending | binding_energy | — | 857.0702 | — | — |
| ${}^{102}$Zr | 102 | 62 | L?-pending | pending | binding_energy | — | 863.5620 | — | — |
| ${}^{103}$Zr | 103 | 63 | L?-pending | pending | binding_energy | — | 867.8609 | — | — |
| ${}^{104}$Zr | 104 | 64 | L?-pending | pending | binding_energy | — | 873.8409 | — | — |
| ${}^{105}$Zr | 105 | 65 | L?-pending | pending | binding_energy | — | 877.6528 | — | — |
| ${}^{106}$Zr | 106 | 66 | L?-pending | pending | binding_energy | — | 882.9800 | — | — |
| ${}^{107}$Zr | 107 | 67 | L?-pending | pending | binding_energy | — | 886.3880 | — | — |
| ${}^{108}$Zr | 108 | 68 | L?-pending | pending | binding_energy | — | 891.3240 | — | — |
| ${}^{109}$Zr | 109 | 69 | L?-pending | pending | binding_energy | — | 894.2360 | — | — |
| ${}^{110}$Zr | 110 | 70 | L?-pending | pending | binding_energy | — | 898.8100 | — | — |
| ${}^{111}$Zr | 111 | 71 | L?-pending | pending | binding_energy | — | 901.0980 | — | — |
| ${}^{112}$Zr | 112 | 72 | L?-pending | pending | binding_energy | — | 905.0720 | — | — |
| ${}^{113}$Zr | 113 | 73 | L?-pending | pending | binding_energy | — | 907.0510 | — | — |

### Niobium (Z = 41)

_0 of 38 isotopes with a framework prediction; 0 of 38 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{79}$Nb | 79 | 38 | L?-pending | pending | binding_energy | — | 637.2140 | — | — |
| ${}^{80}$Nb | 80 | 39 | L?-pending | pending | binding_energy | — | 652.0800 | — | — |
| ${}^{81}$Nb | 81 | 40 | L?-pending | pending | binding_energy | — | 668.0880 | — | — |
| ${}^{82}$Nb | 82 | 41 | L?-pending | pending | binding_energy | — | 681.5840 | — | — |
| ${}^{83}$Nb | 83 | 42 | L?-pending | pending | binding_energy | — | 695.4561 | — | — |
| ${}^{84}$Nb | 84 | 43 | L?-pending | pending | binding_energy | — | 707.1083 | — | — |
| ${}^{85}$Nb | 85 | 44 | L?-pending | pending | binding_energy | — | 720.2655 | — | — |
| ${}^{86}$Nb | 86 | 45 | L?-pending | pending | binding_energy | — | 731.1912 | — | — |
| ${}^{87}$Nb | 87 | 46 | L?-pending | pending | binding_energy | — | 744.0029 | — | — |
| ${}^{88}$Nb | 88 | 47 | L?-pending | pending | binding_energy | — | 754.3713 | — | — |
| ${}^{89}$Nb | 89 | 48 | L?-pending | pending | binding_energy | — | 766.8968 | — | — |
| ${}^{90}$Nb | 90 | 49 | L?-pending | pending | binding_energy | — | 777.0039 | — | — |
| ${}^{91}$Nb | 91 | 50 | L?-pending | pending | binding_energy | — | 789.0517 | — | — |
| ${}^{92}$Nb | 92 | 51 | L?-pending | pending | binding_energy | — | 796.9383 | — | — |
| ${}^{93}$Nb | 93 | 52 | L?-pending | pending | binding_energy | — | 805.7692 | — | — |
| ${}^{94}$Nb | 94 | 53 | L?-pending | pending | binding_energy | — | 812.9967 | — | — |
| ${}^{95}$Nb | 95 | 54 | L?-pending | pending | binding_energy | — | 821.4853 | — | — |
| ${}^{96}$Nb | 96 | 55 | L?-pending | pending | binding_energy | — | 828.3731 | — | — |
| ${}^{97}$Nb | 97 | 56 | L?-pending | pending | binding_energy | — | 836.4444 | — | — |
| ${}^{98}$Nb | 98 | 57 | L?-pending | pending | binding_energy | — | 842.4376 | — | — |
| ${}^{99}$Nb | 99 | 58 | L?-pending | pending | binding_energy | — | 849.3196 | — | — |
| ${}^{100}$Nb | 100 | 59 | L?-pending | pending | binding_energy | — | 854.8468 | — | — |
| ${}^{101}$Nb | 101 | 60 | L?-pending | pending | binding_energy | — | 862.0184 | — | — |
| ${}^{102}$Nb | 102 | 61 | L?-pending | pending | binding_energy | — | 867.4965 | — | — |
| ${}^{103}$Nb | 103 | 62 | L?-pending | pending | binding_energy | — | 874.2982 | — | — |
| ${}^{104}$Nb | 104 | 63 | L?-pending | pending | binding_energy | — | 879.1519 | — | — |
| ${}^{105}$Nb | 105 | 64 | L?-pending | pending | binding_energy | — | 885.3277 | — | — |
| ${}^{106}$Nb | 106 | 65 | L?-pending | pending | binding_energy | — | 889.6862 | — | — |
| ${}^{107}$Nb | 107 | 66 | L?-pending | pending | binding_energy | — | 895.2786 | — | — |
| ${}^{108}$Nb | 108 | 67 | L?-pending | pending | binding_energy | — | 899.1713 | — | — |
| ${}^{109}$Nb | 109 | 68 | L?-pending | pending | binding_energy | — | 904.3872 | — | — |
| ${}^{110}$Nb | 110 | 69 | L?-pending | pending | binding_energy | — | 908.0787 | — | — |
| ${}^{111}$Nb | 111 | 70 | L?-pending | pending | binding_energy | — | 912.7530 | — | — |
| ${}^{112}$Nb | 112 | 71 | L?-pending | pending | binding_energy | — | 915.9360 | — | — |
| ${}^{113}$Nb | 113 | 72 | L?-pending | pending | binding_energy | — | 920.1590 | — | — |
| ${}^{114}$Nb | 114 | 73 | L?-pending | pending | binding_energy | — | 923.0580 | — | — |
| ${}^{115}$Nb | 115 | 74 | L?-pending | pending | binding_energy | — | 927.0150 | — | — |
| ${}^{116}$Nb | 116 | 75 | L?-pending | pending | binding_energy | — | 929.3920 | — | — |

### Molybdenum (Z = 42)

_0 of 39 isotopes with a framework prediction; 0 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{81}$Mo | 81 | 39 | L?-pending | pending | binding_energy | — | 652.3740 | — | — |
| ${}^{82}$Mo | 82 | 40 | L?-pending | pending | binding_energy | — | 669.3660 | — | — |
| ${}^{83}$Mo | 83 | 41 | L?-pending | pending | binding_energy | — | 683.4220 | — | — |
| ${}^{84}$Mo | 84 | 42 | L?-pending | pending | binding_energy | — | 699.3000 | — | — |
| ${}^{85}$Mo | 85 | 43 | L?-pending | pending | binding_energy | — | 710.7132 | — | — |
| ${}^{86}$Mo | 86 | 44 | L?-pending | pending | binding_energy | — | 725.3857 | — | — |
| ${}^{87}$Mo | 87 | 45 | L?-pending | pending | binding_energy | — | 736.2309 | — | — |
| ${}^{88}$Mo | 88 | 46 | L?-pending | pending | binding_energy | — | 750.1040 | — | — |
| ${}^{89}$Mo | 89 | 47 | L?-pending | pending | binding_energy | — | 760.5037 | — | — |
| ${}^{90}$Mo | 90 | 48 | L?-pending | pending | binding_energy | — | 773.7326 | — | — |
| ${}^{91}$Mo | 91 | 49 | L?-pending | pending | binding_energy | — | 783.8402 | — | — |
| ${}^{92}$Mo | 92 | 50 | L?-pending | pending | binding_energy | — | 796.5113 | — | — |
| ${}^{93}$Mo | 93 | 51 | L?-pending | pending | binding_energy | — | 804.5811 | — | — |
| ${}^{94}$Mo | 94 | 52 | L?-pending | pending | binding_energy | — | 814.2594 | — | — |
| ${}^{95}$Mo | 95 | 53 | L?-pending | pending | binding_energy | — | 821.6285 | — | — |
| ${}^{96}$Mo | 96 | 54 | L?-pending | pending | binding_energy | — | 830.7828 | — | — |
| ${}^{97}$Mo | 97 | 55 | L?-pending | pending | binding_energy | — | 837.6040 | — | — |
| ${}^{98}$Mo | 98 | 56 | L?-pending | pending | binding_energy | — | 846.2466 | — | — |
| ${}^{99}$Mo | 99 | 57 | L?-pending | pending | binding_energy | — | 852.1720 | — | — |
| ${}^{100}$Mo | 100 | 58 | L?-pending | pending | binding_energy | — | 860.4663 | — | — |
| ${}^{101}$Mo | 101 | 59 | L?-pending | pending | binding_energy | — | 865.8645 | — | — |
| ${}^{102}$Mo | 102 | 60 | L?-pending | pending | binding_energy | — | 873.9767 | — | — |
| ${}^{103}$Mo | 103 | 61 | L?-pending | pending | binding_energy | — | 879.4415 | — | — |
| ${}^{104}$Mo | 104 | 62 | L?-pending | pending | binding_energy | — | 886.9023 | — | — |
| ${}^{105}$Mo | 105 | 63 | L?-pending | pending | binding_energy | — | 891.9606 | — | — |
| ${}^{106}$Mo | 106 | 64 | L?-pending | pending | binding_energy | — | 898.8291 | — | — |
| ${}^{107}$Mo | 107 | 65 | L?-pending | pending | binding_energy | — | 903.3174 | — | — |
| ${}^{108}$Mo | 108 | 66 | L?-pending | pending | binding_energy | — | 909.5931 | — | — |
| ${}^{109}$Mo | 109 | 67 | L?-pending | pending | binding_energy | — | 913.5744 | — | — |
| ${}^{110}$Mo | 110 | 68 | L?-pending | pending | binding_energy | — | 919.5222 | — | — |
| ${}^{111}$Mo | 111 | 69 | L?-pending | pending | binding_energy | — | 922.9975 | — | — |
| ${}^{112}$Mo | 112 | 70 | L?-pending | pending | binding_energy | — | 928.5920 | — | — |
| ${}^{113}$Mo | 113 | 71 | L?-pending | pending | binding_energy | — | 931.7980 | — | — |
| ${}^{114}$Mo | 114 | 72 | L?-pending | pending | binding_energy | — | 936.9660 | — | — |
| ${}^{115}$Mo | 115 | 73 | L?-pending | pending | binding_energy | — | 939.8950 | — | — |
| ${}^{116}$Mo | 116 | 74 | L?-pending | pending | binding_energy | — | 944.5880 | — | — |
| ${}^{117}$Mo | 117 | 75 | L?-pending | pending | binding_energy | — | 947.2320 | — | — |
| ${}^{118}$Mo | 118 | 76 | L?-pending | pending | binding_energy | — | 951.9060 | — | — |
| ${}^{119}$Mo | 119 | 77 | L?-pending | pending | binding_energy | — | 954.2610 | — | — |

### Technetium (Z = 43)

_0 of 40 isotopes with a framework prediction; 0 of 40 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{83}$Tc | 83 | 40 | L?-pending | pending | binding_energy | — | 667.5690 | — | — |
| ${}^{84}$Tc | 84 | 41 | L?-pending | pending | binding_energy | — | 682.0800 | — | — |
| ${}^{85}$Tc | 85 | 42 | L?-pending | pending | binding_energy | — | 698.2750 | — | — |
| ${}^{86}$Tc | 86 | 43 | L?-pending | pending | binding_energy | — | 712.0800 | — | — |
| ${}^{87}$Tc | 87 | 44 | L?-pending | pending | binding_energy | — | 726.2538 | — | — |
| ${}^{88}$Tc | 88 | 45 | L?-pending | pending | binding_energy | — | 738.3054 | — | — |
| ${}^{89}$Tc | 89 | 46 | L?-pending | pending | binding_energy | — | 752.1012 | — | — |
| ${}^{90}$Tc | 90 | 47 | L?-pending | pending | binding_energy | — | 763.5024 | — | — |
| ${}^{91}$Tc | 91 | 48 | L?-pending | pending | binding_energy | — | 776.8357 | — | — |
| ${}^{92}$Tc | 92 | 49 | L?-pending | pending | binding_energy | — | 787.8460 | — | — |
| ${}^{93}$Tc | 93 | 50 | L?-pending | pending | binding_energy | — | 800.5978 | — | — |
| ${}^{94}$Tc | 94 | 51 | L?-pending | pending | binding_energy | — | 809.2213 | — | — |
| ${}^{95}$Tc | 95 | 52 | L?-pending | pending | binding_energy | — | 819.1557 | — | — |
| ${}^{96}$Tc | 96 | 53 | L?-pending | pending | binding_energy | — | 827.0273 | — | — |
| ${}^{97}$Tc | 97 | 54 | L?-pending | pending | binding_energy | — | 836.5014 | — | — |
| ${}^{98}$Tc | 98 | 55 | L?-pending | pending | binding_energy | — | 843.7805 | — | — |
| ${}^{99}$Tc | 99 | 56 | L?-pending | pending | binding_energy | — | 852.7474 | — | — |
| ${}^{100}$Tc | 100 | 57 | L?-pending | pending | binding_energy | — | 859.5118 | — | — |
| ${}^{101}$Tc | 101 | 58 | L?-pending | pending | binding_energy | — | 867.9068 | — | — |
| ${}^{102}$Tc | 102 | 59 | L?-pending | pending | binding_energy | — | 874.2064 | — | — |
| ${}^{103}$Tc | 103 | 60 | L?-pending | pending | binding_energy | — | 882.3088 | — | — |
| ${}^{104}$Tc | 104 | 61 | L?-pending | pending | binding_energy | — | 888.2751 | — | — |
| ${}^{105}$Tc | 105 | 62 | L?-pending | pending | binding_energy | — | 896.1338 | — | — |
| ${}^{106}$Tc | 106 | 63 | L?-pending | pending | binding_energy | — | 901.6950 | — | — |
| ${}^{107}$Tc | 107 | 64 | L?-pending | pending | binding_energy | — | 908.7401 | — | — |
| ${}^{108}$Tc | 108 | 65 | L?-pending | pending | binding_energy | — | 913.9843 | — | — |
| ${}^{109}$Tc | 109 | 66 | L?-pending | pending | binding_energy | — | 920.4156 | — | — |
| ${}^{110}$Tc | 110 | 67 | L?-pending | pending | binding_energy | — | 925.2386 | — | — |
| ${}^{111}$Tc | 111 | 68 | L?-pending | pending | binding_energy | — | 931.3001 | — | — |
| ${}^{112}$Tc | 112 | 69 | L?-pending | pending | binding_energy | — | 935.6056 | — | — |
| ${}^{113}$Tc | 113 | 70 | L?-pending | pending | binding_energy | — | 941.2296 | — | — |
| ${}^{114}$Tc | 114 | 71 | L?-pending | pending | binding_energy | — | 945.0896 | — | — |
| ${}^{115}$Tc | 115 | 72 | L?-pending | pending | binding_energy | — | 950.3600 | — | — |
| ${}^{116}$Tc | 116 | 73 | L?-pending | pending | binding_energy | — | 953.8680 | — | — |
| ${}^{117}$Tc | 117 | 74 | L?-pending | pending | binding_energy | — | 958.8150 | — | — |
| ${}^{118}$Tc | 118 | 75 | L?-pending | pending | binding_energy | — | 962.0540 | — | — |
| ${}^{119}$Tc | 119 | 76 | L?-pending | pending | binding_energy | — | 966.9940 | — | — |
| ${}^{120}$Tc | 120 | 77 | L?-pending | pending | binding_energy | — | 969.9600 | — | — |
| ${}^{121}$Tc | 121 | 78 | L?-pending | pending | binding_energy | — | 974.5340 | — | — |
| ${}^{122}$Tc | 122 | 79 | L?-pending | pending | binding_energy | — | 977.3420 | — | — |

### Ruthenium (Z = 44)

_0 of 41 isotopes with a framework prediction; 0 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{85}$Ru | 85 | 41 | L?-pending | pending | binding_energy | — | 682.2950 | — | — |
| ${}^{86}$Ru | 86 | 42 | L?-pending | pending | binding_energy | — | 699.4380 | — | — |
| ${}^{87}$Ru | 87 | 43 | L?-pending | pending | binding_energy | — | 713.4870 | — | — |
| ${}^{88}$Ru | 88 | 44 | L?-pending | pending | binding_energy | — | 730.2240 | — | — |
| ${}^{89}$Ru | 89 | 45 | L?-pending | pending | binding_energy | — | 742.2935 | — | — |
| ${}^{90}$Ru | 90 | 46 | L?-pending | pending | binding_energy | — | 756.8792 | — | — |
| ${}^{91}$Ru | 91 | 47 | L?-pending | pending | binding_energy | — | 768.3065 | — | — |
| ${}^{92}$Ru | 92 | 48 | L?-pending | pending | binding_energy | — | 782.4392 | — | — |
| ${}^{93}$Ru | 93 | 49 | L?-pending | pending | binding_energy | — | 793.4260 | — | — |
| ${}^{94}$Ru | 94 | 50 | L?-pending | pending | binding_energy | — | 806.8642 | — | — |
| ${}^{95}$Ru | 95 | 51 | L?-pending | pending | binding_energy | — | 815.8097 | — | — |
| ${}^{96}$Ru | 96 | 52 | L?-pending | pending | binding_energy | — | 826.5036 | — | — |
| ${}^{97}$Ru | 97 | 53 | L?-pending | pending | binding_energy | — | 834.6152 | — | — |
| ${}^{98}$Ru | 98 | 54 | L?-pending | pending | binding_energy | — | 844.7908 | — | — |
| ${}^{99}$Ru | 99 | 55 | L?-pending | pending | binding_energy | — | 852.2626 | — | — |
| ${}^{100}$Ru | 100 | 56 | L?-pending | pending | binding_energy | — | 861.9359 | — | — |
| ${}^{101}$Ru | 101 | 57 | L?-pending | pending | binding_energy | — | 868.7380 | — | — |
| ${}^{102}$Ru | 102 | 58 | L?-pending | pending | binding_energy | — | 877.9576 | — | — |
| ${}^{103}$Ru | 103 | 59 | L?-pending | pending | binding_energy | — | 884.1897 | — | — |
| ${}^{104}$Ru | 104 | 60 | L?-pending | pending | binding_energy | — | 893.0896 | — | — |
| ${}^{105}$Ru | 105 | 61 | L?-pending | pending | binding_energy | — | 898.9997 | — | — |
| ${}^{106}$Ru | 106 | 62 | L?-pending | pending | binding_energy | — | 907.4597 | — | — |
| ${}^{107}$Ru | 107 | 63 | L?-pending | pending | binding_energy | — | 913.0703 | — | — |
| ${}^{108}$Ru | 108 | 64 | L?-pending | pending | binding_energy | — | 920.9405 | — | — |
| ${}^{109}$Ru | 109 | 65 | L?-pending | pending | binding_energy | — | 926.0889 | — | — |
| ${}^{110}$Ru | 110 | 66 | L?-pending | pending | binding_energy | — | 933.4944 | — | — |
| ${}^{111}$Ru | 111 | 67 | L?-pending | pending | binding_energy | — | 938.2784 | — | — |
| ${}^{112}$Ru | 112 | 68 | L?-pending | pending | binding_energy | — | 945.1952 | — | — |
| ${}^{113}$Ru | 113 | 69 | L?-pending | pending | binding_energy | — | 949.5035 | — | — |
| ${}^{114}$Ru | 114 | 70 | L?-pending | pending | binding_energy | — | 955.9282 | — | — |
| ${}^{115}$Ru | 115 | 71 | L?-pending | pending | binding_energy | — | 959.8836 | — | — |
| ${}^{116}$Ru | 116 | 72 | L?-pending | pending | binding_energy | — | 965.9185 | — | — |
| ${}^{117}$Ru | 117 | 73 | L?-pending | pending | binding_energy | — | 969.4108 | — | — |
| ${}^{118}$Ru | 118 | 74 | L?-pending | pending | binding_energy | — | 975.0340 | — | — |
| ${}^{119}$Ru | 119 | 75 | L?-pending | pending | binding_energy | — | 978.1800 | — | — |
| ${}^{120}$Ru | 120 | 76 | L?-pending | pending | binding_energy | — | 983.8800 | — | — |
| ${}^{121}$Ru | 121 | 77 | L?-pending | pending | binding_energy | — | 986.8760 | — | — |
| ${}^{122}$Ru | 122 | 78 | L?-pending | pending | binding_energy | — | 992.1040 | — | — |
| ${}^{123}$Ru | 123 | 79 | L?-pending | pending | binding_energy | — | 994.9470 | — | — |
| ${}^{124}$Ru | 124 | 80 | L?-pending | pending | binding_energy | — | 1000.0600 | — | — |
| ${}^{125}$Ru | 125 | 81 | L?-pending | pending | binding_energy | — | 1002.8750 | — | — |

### Rhodium (Z = 45)

_0 of 41 isotopes with a framework prediction; 0 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{88}$Rh | 88 | 43 | L?-pending | pending | binding_energy | — | 711.9200 | — | — |
| ${}^{89}$Rh | 89 | 44 | L?-pending | pending | binding_energy | — | 728.8210 | — | — |
| ${}^{90}$Rh | 90 | 45 | L?-pending | pending | binding_energy | — | 742.8600 | — | — |
| ${}^{91}$Rh | 91 | 46 | L?-pending | pending | binding_energy | — | 757.8480 | — | — |
| ${}^{92}$Rh | 92 | 47 | L?-pending | pending | binding_energy | — | 770.3547 | — | — |
| ${}^{93}$Rh | 93 | 48 | L?-pending | pending | binding_energy | — | 784.4388 | — | — |
| ${}^{94}$Rh | 94 | 49 | L?-pending | pending | binding_energy | — | 796.4059 | — | — |
| ${}^{95}$Rh | 95 | 50 | L?-pending | pending | binding_energy | — | 809.9102 | — | — |
| ${}^{96}$Rh | 96 | 51 | L?-pending | pending | binding_energy | — | 819.3287 | — | — |
| ${}^{97}$Rh | 97 | 52 | L?-pending | pending | binding_energy | — | 830.3098 | — | — |
| ${}^{98}$Rh | 98 | 53 | L?-pending | pending | binding_energy | — | 838.9588 | — | — |
| ${}^{99}$Rh | 99 | 54 | L?-pending | pending | binding_energy | — | 849.4394 | — | — |
| ${}^{100}$Rh | 100 | 55 | L?-pending | pending | binding_energy | — | 857.5173 | — | — |
| ${}^{101}$Rh | 101 | 56 | L?-pending | pending | binding_energy | — | 867.4099 | — | — |
| ${}^{102}$Rh | 102 | 57 | L?-pending | pending | binding_energy | — | 874.8521 | — | — |
| ${}^{103}$Rh | 103 | 58 | L?-pending | pending | binding_energy | — | 884.1718 | — | — |
| ${}^{104}$Rh | 104 | 59 | L?-pending | pending | binding_energy | — | 891.1708 | — | — |
| ${}^{105}$Rh | 105 | 60 | L?-pending | pending | binding_energy | — | 900.1341 | — | — |
| ${}^{106}$Rh | 106 | 61 | L?-pending | pending | binding_energy | — | 906.7168 | — | — |
| ${}^{107}$Rh | 107 | 62 | L?-pending | pending | binding_energy | — | 915.2891 | — | — |
| ${}^{108}$Rh | 108 | 63 | L?-pending | pending | binding_energy | — | 921.5279 | — | — |
| ${}^{109}$Rh | 109 | 64 | L?-pending | pending | binding_energy | — | 929.5673 | — | — |
| ${}^{110}$Rh | 110 | 65 | L?-pending | pending | binding_energy | — | 935.4681 | — | — |
| ${}^{111}$Rh | 111 | 66 | L?-pending | pending | binding_energy | — | 943.0146 | — | — |
| ${}^{112}$Rh | 112 | 67 | L?-pending | pending | binding_energy | — | 948.5131 | — | — |
| ${}^{113}$Rh | 113 | 68 | L?-pending | pending | binding_energy | — | 955.6203 | — | — |
| ${}^{114}$Rh | 114 | 69 | L?-pending | pending | binding_energy | — | 960.6349 | — | — |
| ${}^{115}$Rh | 115 | 70 | L?-pending | pending | binding_energy | — | 967.2252 | — | — |
| ${}^{116}$Rh | 116 | 71 | L?-pending | pending | binding_energy | — | 971.8030 | — | — |
| ${}^{117}$Rh | 117 | 72 | L?-pending | pending | binding_energy | — | 978.0354 | — | — |
| ${}^{118}$Rh | 118 | 73 | L?-pending | pending | binding_energy | — | 982.0968 | — | — |
| ${}^{119}$Rh | 119 | 74 | L?-pending | pending | binding_energy | — | 988.1040 | — | — |
| ${}^{120}$Rh | 120 | 75 | L?-pending | pending | binding_energy | — | 991.9200 | — | — |
| ${}^{121}$Rh | 121 | 76 | L?-pending | pending | binding_energy | — | 997.6740 | — | — |
| ${}^{122}$Rh | 122 | 77 | L?-pending | pending | binding_energy | — | 1001.3760 | — | — |
| ${}^{123}$Rh | 123 | 78 | L?-pending | pending | binding_energy | — | 1006.7550 | — | — |
| ${}^{124}$Rh | 124 | 79 | L?-pending | pending | binding_energy | — | 1010.3520 | — | — |
| ${}^{125}$Rh | 125 | 80 | L?-pending | pending | binding_energy | — | 1015.5000 | — | — |
| ${}^{126}$Rh | 126 | 81 | L?-pending | pending | binding_energy | — | 1018.9620 | — | — |
| ${}^{127}$Rh | 127 | 82 | L?-pending | pending | binding_energy | — | 1023.6200 | — | — |
| ${}^{128}$Rh | 128 | 83 | L?-pending | pending | binding_energy | — | 1025.2800 | — | — |

### Palladium (Z = 46)

_0 of 42 isotopes with a framework prediction; 0 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{90}$Pd | 90 | 44 | L?-pending | pending | binding_energy | — | 730.1700 | — | — |
| ${}^{91}$Pd | 91 | 45 | L?-pending | pending | binding_energy | — | 744.6530 | — | — |
| ${}^{92}$Pd | 92 | 46 | L?-pending | pending | binding_energy | — | 761.3524 | — | — |
| ${}^{93}$Pd | 93 | 47 | L?-pending | pending | binding_energy | — | 773.6264 | — | — |
| ${}^{94}$Pd | 94 | 48 | L?-pending | pending | binding_energy | — | 788.8182 | — | — |
| ${}^{95}$Pd | 95 | 49 | L?-pending | pending | binding_energy | — | 800.7532 | — | — |
| ${}^{96}$Pd | 96 | 50 | L?-pending | pending | binding_energy | — | 815.0420 | — | — |
| ${}^{97}$Pd | 97 | 51 | L?-pending | pending | binding_energy | — | 824.7357 | — | — |
| ${}^{98}$Pd | 98 | 52 | L?-pending | pending | binding_energy | — | 836.3222 | — | — |
| ${}^{99}$Pd | 99 | 53 | L?-pending | pending | binding_energy | — | 845.2554 | — | — |
| ${}^{100}$Pd | 100 | 54 | L?-pending | pending | binding_energy | — | 856.3565 | — | — |
| ${}^{101}$Pd | 101 | 55 | L?-pending | pending | binding_energy | — | 864.6473 | — | — |
| ${}^{102}$Pd | 102 | 56 | L?-pending | pending | binding_energy | — | 875.1894 | — | — |
| ${}^{103}$Pd | 103 | 57 | L?-pending | pending | binding_energy | — | 882.8148 | — | — |
| ${}^{104}$Pd | 104 | 58 | L?-pending | pending | binding_energy | — | 892.8242 | — | — |
| ${}^{105}$Pd | 105 | 59 | L?-pending | pending | binding_energy | — | 899.9183 | — | — |
| ${}^{106}$Pd | 106 | 60 | L?-pending | pending | binding_energy | — | 909.4793 | — | — |
| ${}^{107}$Pd | 107 | 61 | L?-pending | pending | binding_energy | — | 916.0157 | — | — |
| ${}^{108}$Pd | 108 | 62 | L?-pending | pending | binding_energy | — | 925.2386 | — | — |
| ${}^{109}$Pd | 109 | 63 | L?-pending | pending | binding_energy | — | 931.3922 | — | — |
| ${}^{110}$Pd | 110 | 64 | L?-pending | pending | binding_energy | — | 940.1879 | — | — |
| ${}^{111}$Pd | 111 | 65 | L?-pending | pending | binding_energy | — | 945.9142 | — | — |
| ${}^{112}$Pd | 112 | 66 | L?-pending | pending | binding_energy | — | 954.3207 | — | — |
| ${}^{113}$Pd | 113 | 67 | L?-pending | pending | binding_energy | — | 959.6615 | — | — |
| ${}^{114}$Pd | 114 | 68 | L?-pending | pending | binding_energy | — | 967.6326 | — | — |
| ${}^{115}$Pd | 115 | 69 | L?-pending | pending | binding_energy | — | 972.6394 | — | — |
| ${}^{116}$Pd | 116 | 70 | L?-pending | pending | binding_energy | — | 980.1160 | — | — |
| ${}^{117}$Pd | 117 | 71 | L?-pending | pending | binding_energy | — | 984.7801 | — | — |
| ${}^{118}$Pd | 118 | 72 | L?-pending | pending | binding_energy | — | 991.8159 | — | — |
| ${}^{119}$Pd | 119 | 73 | L?-pending | pending | binding_energy | — | 995.9062 | — | — |
| ${}^{120}$Pd | 120 | 74 | L?-pending | pending | binding_energy | — | 1002.8498 | — | — |
| ${}^{121}$Pd | 121 | 75 | L?-pending | pending | binding_energy | — | 1006.8239 | — | — |
| ${}^{122}$Pd | 122 | 76 | L?-pending | pending | binding_energy | — | 1013.3290 | — | — |
| ${}^{123}$Pd | 123 | 77 | L?-pending | pending | binding_energy | — | 1017.2139 | — | — |
| ${}^{124}$Pd | 124 | 78 | L?-pending | pending | binding_energy | — | 1023.2480 | — | — |
| ${}^{125}$Pd | 125 | 79 | L?-pending | pending | binding_energy | — | 1026.8750 | — | — |
| ${}^{126}$Pd | 126 | 80 | L?-pending | pending | binding_energy | — | 1032.8220 | — | — |
| ${}^{127}$Pd | 127 | 81 | L?-pending | pending | binding_energy | — | 1036.3200 | — | — |
| ${}^{128}$Pd | 128 | 82 | L?-pending | pending | binding_energy | — | 1041.5360 | — | — |
| ${}^{129}$Pd | 129 | 83 | L?-pending | pending | binding_energy | — | 1043.0940 | — | — |
| ${}^{130}$Pd | 130 | 84 | L?-pending | pending | binding_energy | — | 1045.9800 | — | — |
| ${}^{131}$Pd | 131 | 85 | L?-pending | pending | binding_energy | — | 1047.0830 | — | — |

### Silver (Z = 47)

_0 of 42 isotopes with a framework prediction; 0 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{92}$Ag | 92 | 45 | L?-pending | pending | binding_energy | — | 743.3600 | — | — |
| ${}^{93}$Ag | 93 | 46 | L?-pending | pending | binding_energy | — | 760.2750 | — | — |
| ${}^{94}$Ag | 94 | 47 | L?-pending | pending | binding_energy | — | 774.3720 | — | — |
| ${}^{95}$Ag | 95 | 48 | L?-pending | pending | binding_energy | — | 789.9250 | — | — |
| ${}^{96}$Ag | 96 | 49 | L?-pending | pending | binding_energy | — | 802.5879 | — | — |
| ${}^{97}$Ag | 97 | 50 | L?-pending | pending | binding_energy | — | 817.0516 | — | — |
| ${}^{98}$Ag | 98 | 51 | L?-pending | pending | binding_energy | — | 827.2853 | — | — |
| ${}^{99}$Ag | 99 | 52 | L?-pending | pending | binding_energy | — | 839.0027 | — | — |
| ${}^{100}$Ag | 100 | 53 | L?-pending | pending | binding_energy | — | 848.4995 | — | — |
| ${}^{101}$Ag | 101 | 54 | L?-pending | pending | binding_energy | — | 859.7672 | — | — |
| ${}^{102}$Ag | 102 | 55 | L?-pending | pending | binding_energy | — | 868.7508 | — | — |
| ${}^{103}$Ag | 103 | 56 | L?-pending | pending | binding_energy | — | 879.3782 | — | — |
| ${}^{104}$Ag | 104 | 57 | L?-pending | pending | binding_energy | — | 887.7632 | — | — |
| ${}^{105}$Ag | 105 | 58 | L?-pending | pending | binding_energy | — | 897.7889 | — | — |
| ${}^{106}$Ag | 106 | 59 | L?-pending | pending | binding_energy | — | 905.7318 | — | — |
| ${}^{107}$Ag | 107 | 60 | L?-pending | pending | binding_energy | — | 915.2674 | — | — |
| ${}^{108}$Ag | 108 | 61 | L?-pending | pending | binding_energy | — | 922.5388 | — | — |
| ${}^{109}$Ag | 109 | 62 | L?-pending | pending | binding_energy | — | 931.7228 | — | — |
| ${}^{110}$Ag | 110 | 63 | L?-pending | pending | binding_energy | — | 938.5320 | — | — |
| ${}^{111}$Ag | 111 | 64 | L?-pending | pending | binding_energy | — | 947.3614 | — | — |
| ${}^{112}$Ag | 112 | 65 | L?-pending | pending | binding_energy | — | 953.8010 | — | — |
| ${}^{113}$Ag | 113 | 66 | L?-pending | pending | binding_energy | — | 962.3155 | — | — |
| ${}^{114}$Ag | 114 | 67 | L?-pending | pending | binding_energy | — | 968.2908 | — | — |
| ${}^{115}$Ag | 115 | 68 | L?-pending | pending | binding_energy | — | 976.4139 | — | — |
| ${}^{116}$Ag | 116 | 69 | L?-pending | pending | binding_energy | — | 982.0452 | — | — |
| ${}^{117}$Ag | 117 | 70 | L?-pending | pending | binding_energy | — | 989.7558 | — | — |
| ${}^{118}$Ag | 118 | 71 | L?-pending | pending | binding_energy | — | 995.1990 | — | — |
| ${}^{119}$Ag | 119 | 72 | L?-pending | pending | binding_energy | — | 1002.3623 | — | — |
| ${}^{120}$Ag | 120 | 73 | L?-pending | pending | binding_energy | — | 1007.4394 | — | — |
| ${}^{121}$Ag | 121 | 74 | L?-pending | pending | binding_energy | — | 1014.2620 | — | — |
| ${}^{122}$Ag | 122 | 75 | L?-pending | pending | binding_energy | — | 1019.0366 | — | — |
| ${}^{123}$Ag | 123 | 76 | L?-pending | pending | binding_energy | — | 1025.5704 | — | — |
| ${}^{124}$Ag | 124 | 77 | L?-pending | pending | binding_energy | — | 1030.3031 | — | — |
| ${}^{125}$Ag | 125 | 78 | L?-pending | pending | binding_energy | — | 1036.6644 | — | — |
| ${}^{126}$Ag | 126 | 79 | L?-pending | pending | binding_energy | — | 1040.8860 | — | — |
| ${}^{127}$Ag | 127 | 80 | L?-pending | pending | binding_energy | — | 1046.9880 | — | — |
| ${}^{128}$Ag | 128 | 81 | L?-pending | pending | binding_energy | — | 1051.0080 | — | — |
| ${}^{129}$Ag | 129 | 82 | L?-pending | pending | binding_energy | — | 1056.2520 | — | — |
| ${}^{130}$Ag | 130 | 83 | L?-pending | pending | binding_energy | — | 1058.4600 | — | — |
| ${}^{131}$Ag | 131 | 84 | L?-pending | pending | binding_energy | — | 1061.3620 | — | — |
| ${}^{132}$Ag | 132 | 85 | L?-pending | pending | binding_energy | — | 1062.9960 | — | — |
| ${}^{133}$Ag | 133 | 86 | L?-pending | pending | binding_energy | — | 1065.7290 | — | — |

### Cadmium (Z = 48)

_0 of 42 isotopes with a framework prediction; 0 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{94}$Cd | 94 | 46 | L?-pending | pending | binding_energy | — | 761.5880 | — | — |
| ${}^{95}$Cd | 95 | 47 | L?-pending | pending | binding_energy | — | 776.2450 | — | — |
| ${}^{96}$Cd | 96 | 48 | L?-pending | pending | binding_energy | — | 792.8640 | — | — |
| ${}^{97}$Cd | 97 | 49 | L?-pending | pending | binding_energy | — | 806.0992 | — | — |
| ${}^{98}$Cd | 98 | 50 | L?-pending | pending | binding_energy | — | 821.0729 | — | — |
| ${}^{99}$Cd | 99 | 51 | L?-pending | pending | binding_energy | — | 831.4390 | — | — |
| ${}^{100}$Cd | 100 | 52 | L?-pending | pending | binding_energy | — | 843.7737 | — | — |
| ${}^{101}$Cd | 101 | 53 | L?-pending | pending | binding_energy | — | 853.4869 | — | — |
| ${}^{102}$Cd | 102 | 54 | L?-pending | pending | binding_energy | — | 865.3815 | — | — |
| ${}^{103}$Cd | 103 | 55 | L?-pending | pending | binding_energy | — | 874.4447 | — | — |
| ${}^{104}$Cd | 104 | 56 | L?-pending | pending | binding_energy | — | 885.8328 | — | — |
| ${}^{105}$Cd | 105 | 57 | L?-pending | pending | binding_energy | — | 894.2696 | — | — |
| ${}^{106}$Cd | 106 | 58 | L?-pending | pending | binding_energy | — | 905.1392 | — | — |
| ${}^{107}$Cd | 107 | 59 | L?-pending | pending | binding_energy | — | 913.0687 | — | — |
| ${}^{108}$Cd | 108 | 60 | L?-pending | pending | binding_energy | — | 923.4021 | — | — |
| ${}^{109}$Cd | 109 | 61 | L?-pending | pending | binding_energy | — | 930.7253 | — | — |
| ${}^{110}$Cd | 110 | 62 | L?-pending | pending | binding_energy | — | 940.6403 | — | — |
| ${}^{111}$Cd | 111 | 63 | L?-pending | pending | binding_energy | — | 947.6159 | — | — |
| ${}^{112}$Cd | 112 | 64 | L?-pending | pending | binding_energy | — | 957.0098 | — | — |
| ${}^{113}$Cd | 113 | 65 | L?-pending | pending | binding_energy | — | 963.5496 | — | — |
| ${}^{114}$Cd | 114 | 66 | L?-pending | pending | binding_energy | — | 972.5925 | — | — |
| ${}^{115}$Cd | 115 | 67 | L?-pending | pending | binding_energy | — | 978.7334 | — | — |
| ${}^{116}$Cd | 116 | 68 | L?-pending | pending | binding_energy | — | 987.4327 | — | — |
| ${}^{117}$Cd | 117 | 69 | L?-pending | pending | binding_energy | — | 993.2100 | — | — |
| ${}^{118}$Cd | 118 | 70 | L?-pending | pending | binding_energy | — | 1001.5645 | — | — |
| ${}^{119}$Cd | 119 | 71 | L?-pending | pending | binding_energy | — | 1006.9111 | — | — |
| ${}^{120}$Cd | 120 | 72 | L?-pending | pending | binding_energy | — | 1014.9629 | — | — |
| ${}^{121}$Cd | 121 | 73 | L?-pending | pending | binding_energy | — | 1020.1507 | — | — |
| ${}^{122}$Cd | 122 | 74 | L?-pending | pending | binding_energy | — | 1027.7605 | — | — |
| ${}^{123}$Cd | 123 | 75 | L?-pending | pending | binding_energy | — | 1032.6336 | — | — |
| ${}^{124}$Cd | 124 | 76 | L?-pending | pending | binding_energy | — | 1039.9902 | — | — |
| ${}^{125}$Cd | 125 | 77 | L?-pending | pending | binding_energy | — | 1044.7102 | — | — |
| ${}^{126}$Cd | 126 | 78 | L?-pending | pending | binding_energy | — | 1051.6892 | — | — |
| ${}^{127}$Cd | 127 | 79 | L?-pending | pending | binding_energy | — | 1056.2459 | — | — |
| ${}^{128}$Cd | 128 | 80 | L?-pending | pending | binding_energy | — | 1062.8143 | — | — |
| ${}^{129}$Cd | 129 | 81 | L?-pending | pending | binding_energy | — | 1066.7695 | — | — |
| ${}^{130}$Cd | 130 | 82 | L?-pending | pending | binding_energy | — | 1072.8363 | — | — |
| ${}^{131}$Cd | 131 | 83 | L?-pending | pending | binding_energy | — | 1075.0018 | — | — |
| ${}^{132}$Cd | 132 | 84 | L?-pending | pending | binding_energy | — | 1078.3268 | — | — |
| ${}^{133}$Cd | 133 | 85 | L?-pending | pending | binding_energy | — | 1080.0930 | — | — |
| ${}^{134}$Cd | 134 | 86 | L?-pending | pending | binding_energy | — | 1083.5240 | — | — |
| ${}^{135}$Cd | 135 | 87 | L?-pending | pending | binding_energy | — | 1084.8600 | — | — |

### Indium (Z = 49)

_0 of 42 isotopes with a framework prediction; 0 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{96}$In | 96 | 47 | L?-pending | pending | binding_energy | — | 774.6240 | — | — |
| ${}^{97}$In | 97 | 48 | L?-pending | pending | binding_energy | — | 792.0050 | — | — |
| ${}^{98}$In | 98 | 49 | L?-pending | pending | binding_energy | — | 806.5400 | — | — |
| ${}^{99}$In | 99 | 50 | L?-pending | pending | binding_energy | — | 822.0960 | — | — |
| ${}^{100}$In | 100 | 51 | L?-pending | pending | binding_energy | — | 832.9749 | — | — |
| ${}^{101}$In | 101 | 52 | L?-pending | pending | binding_energy | — | 845.4130 | — | — |
| ${}^{102}$In | 102 | 53 | L?-pending | pending | binding_energy | — | 855.6343 | — | — |
| ${}^{103}$In | 103 | 54 | L?-pending | pending | binding_energy | — | 867.6431 | — | — |
| ${}^{104}$In | 104 | 55 | L?-pending | pending | binding_energy | — | 877.2648 | — | — |
| ${}^{105}$In | 105 | 56 | L?-pending | pending | binding_energy | — | 888.7940 | — | — |
| ${}^{106}$In | 106 | 57 | L?-pending | pending | binding_energy | — | 897.8329 | — | — |
| ${}^{107}$In | 107 | 58 | L?-pending | pending | binding_energy | — | 908.8627 | — | — |
| ${}^{108}$In | 108 | 59 | L?-pending | pending | binding_energy | — | 917.4872 | — | — |
| ${}^{109}$In | 109 | 60 | L?-pending | pending | binding_energy | — | 927.9282 | — | — |
| ${}^{110}$In | 110 | 61 | L?-pending | pending | binding_energy | — | 935.9800 | — | — |
| ${}^{111}$In | 111 | 62 | L?-pending | pending | binding_energy | — | 945.9733 | — | — |
| ${}^{112}$In | 112 | 63 | L?-pending | pending | binding_energy | — | 953.6427 | — | — |
| ${}^{113}$In | 113 | 64 | L?-pending | pending | binding_energy | — | 963.0911 | — | — |
| ${}^{114}$In | 114 | 65 | L?-pending | pending | binding_energy | — | 970.3651 | — | — |
| ${}^{115}$In | 115 | 66 | L?-pending | pending | binding_energy | — | 979.4029 | — | — |
| ${}^{116}$In | 116 | 67 | L?-pending | pending | binding_energy | — | 986.1877 | — | — |
| ${}^{117}$In | 117 | 68 | L?-pending | pending | binding_energy | — | 994.9522 | — | — |
| ${}^{118}$In | 118 | 69 | L?-pending | pending | binding_energy | — | 1001.3087 | — | — |
| ${}^{119}$In | 119 | 70 | L?-pending | pending | binding_energy | — | 1009.8505 | — | — |
| ${}^{120}$In | 120 | 71 | L?-pending | pending | binding_energy | — | 1015.9509 | — | — |
| ${}^{121}$In | 121 | 72 | L?-pending | pending | binding_energy | — | 1024.1291 | — | — |
| ${}^{122}$In | 122 | 73 | L?-pending | pending | binding_energy | — | 1029.9372 | — | — |
| ${}^{123}$In | 123 | 74 | L?-pending | pending | binding_energy | — | 1037.8662 | — | — |
| ${}^{124}$In | 124 | 75 | L?-pending | pending | binding_energy | — | 1043.3762 | — | — |
| ${}^{125}$In | 125 | 76 | L?-pending | pending | binding_energy | — | 1050.9921 | — | — |
| ${}^{126}$In | 126 | 77 | L?-pending | pending | binding_energy | — | 1056.4604 | — | — |
| ${}^{127}$In | 127 | 78 | L?-pending | pending | binding_energy | — | 1063.6023 | — | — |
| ${}^{128}$In | 128 | 79 | L?-pending | pending | binding_energy | — | 1068.9838 | — | — |
| ${}^{129}$In | 129 | 80 | L?-pending | pending | binding_energy | — | 1075.6999 | — | — |
| ${}^{130}$In | 130 | 81 | L?-pending | pending | binding_energy | — | 1080.8429 | — | — |
| ${}^{131}$In | 131 | 82 | L?-pending | pending | binding_energy | — | 1087.0320 | — | — |
| ${}^{132}$In | 132 | 83 | L?-pending | pending | binding_energy | — | 1089.4905 | — | — |
| ${}^{133}$In | 133 | 84 | L?-pending | pending | binding_energy | — | 1092.8610 | — | — |
| ${}^{134}$In | 134 | 85 | L?-pending | pending | binding_energy | — | 1095.1820 | — | — |
| ${}^{135}$In | 135 | 86 | L?-pending | pending | binding_energy | — | 1098.3600 | — | — |
| ${}^{136}$In | 136 | 87 | L?-pending | pending | binding_energy | — | 1100.3760 | — | — |
| ${}^{137}$In | 137 | 88 | L?-pending | pending | binding_energy | — | 1103.2610 | — | — |

### Tin (Z = 50)

_0 of 42 isotopes with a framework prediction; 0 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{99}$Sn | 99 | 49 | L?-pending | pending | binding_energy | — | 807.9390 | — | — |
| ${}^{100}$Sn | 100 | 50 | L?-pending | pending | binding_energy | — | 825.1626 | — | — |
| ${}^{101}$Sn | 101 | 51 | L?-pending | pending | binding_energy | — | 836.3914 | — | — |
| ${}^{102}$Sn | 102 | 52 | L?-pending | pending | binding_energy | — | 849.0920 | — | — |
| ${}^{103}$Sn | 103 | 53 | L?-pending | pending | binding_energy | — | 859.3290 | — | — |
| ${}^{104}$Sn | 104 | 54 | L?-pending | pending | binding_energy | — | 871.9268 | — | — |
| ${}^{105}$Sn | 105 | 55 | L?-pending | pending | binding_energy | — | 881.7090 | — | — |
| ${}^{106}$Sn | 106 | 56 | L?-pending | pending | binding_energy | — | 893.7961 | — | — |
| ${}^{107}$Sn | 107 | 57 | L?-pending | pending | binding_energy | — | 903.0259 | — | — |
| ${}^{108}$Sn | 108 | 58 | L?-pending | pending | binding_energy | — | 914.6549 | — | — |
| ${}^{109}$Sn | 109 | 59 | L?-pending | pending | binding_energy | — | 923.2865 | — | — |
| ${}^{110}$Sn | 110 | 60 | L?-pending | pending | binding_energy | — | 934.5696 | — | — |
| ${}^{111}$Sn | 111 | 61 | L?-pending | pending | binding_energy | — | 942.7375 | — | — |
| ${}^{112}$Sn | 112 | 62 | L?-pending | pending | binding_energy | — | 953.5253 | — | — |
| ${}^{113}$Sn | 113 | 63 | L?-pending | pending | binding_energy | — | 961.2697 | — | — |
| ${}^{114}$Sn | 114 | 64 | L?-pending | pending | binding_energy | — | 971.5726 | — | — |
| ${}^{115}$Sn | 115 | 65 | L?-pending | pending | binding_energy | — | 979.1181 | — | — |
| ${}^{116}$Sn | 116 | 66 | L?-pending | pending | binding_energy | — | 988.6815 | — | — |
| ${}^{117}$Sn | 117 | 67 | L?-pending | pending | binding_energy | — | 995.6246 | — | — |
| ${}^{118}$Sn | 118 | 68 | L?-pending | pending | binding_energy | — | 1004.9510 | — | — |
| ${}^{119}$Sn | 119 | 69 | L?-pending | pending | binding_energy | — | 1011.4345 | — | — |
| ${}^{120}$Sn | 120 | 70 | L?-pending | pending | binding_energy | — | 1020.5386 | — | — |
| ${}^{121}$Sn | 121 | 71 | L?-pending | pending | binding_energy | — | 1026.7088 | — | — |
| ${}^{122}$Sn | 122 | 72 | L?-pending | pending | binding_energy | — | 1035.5234 | — | — |
| ${}^{123}$Sn | 123 | 73 | L?-pending | pending | binding_energy | — | 1041.4694 | — | — |
| ${}^{124}$Sn | 124 | 74 | L?-pending | pending | binding_energy | — | 1049.9576 | — | — |
| ${}^{125}$Sn | 125 | 75 | L?-pending | pending | binding_energy | — | 1055.6911 | — | — |
| ${}^{126}$Sn | 126 | 76 | L?-pending | pending | binding_energy | — | 1063.8839 | — | — |
| ${}^{127}$Sn | 127 | 77 | L?-pending | pending | binding_energy | — | 1069.4096 | — | — |
| ${}^{128}$Sn | 128 | 78 | L?-pending | pending | binding_energy | — | 1077.3728 | — | — |
| ${}^{129}$Sn | 129 | 79 | L?-pending | pending | binding_energy | — | 1082.6733 | — | — |
| ${}^{130}$Sn | 130 | 80 | L?-pending | pending | binding_energy | — | 1090.2862 | — | — |
| ${}^{131}$Sn | 131 | 81 | L?-pending | pending | binding_energy | — | 1095.4899 | — | — |
| ${}^{132}$Sn | 132 | 82 | L?-pending | pending | binding_energy | — | 1102.8432 | — | — |
| ${}^{133}$Sn | 133 | 83 | L?-pending | pending | binding_energy | — | 1105.2418 | — | — |
| ${}^{134}$Sn | 134 | 84 | L?-pending | pending | binding_energy | — | 1108.8730 | — | — |
| ${}^{135}$Sn | 135 | 85 | L?-pending | pending | binding_energy | — | 1111.1428 | — | — |
| ${}^{136}$Sn | 136 | 86 | L?-pending | pending | binding_energy | — | 1114.7920 | — | — |
| ${}^{137}$Sn | 137 | 87 | L?-pending | pending | binding_energy | — | 1116.8240 | — | — |
| ${}^{138}$Sn | 138 | 88 | L?-pending | pending | binding_energy | — | 1120.2840 | — | — |
| ${}^{139}$Sn | 139 | 89 | L?-pending | pending | binding_energy | — | 1122.1470 | — | — |
| ${}^{140}$Sn | 140 | 90 | L?-pending | pending | binding_energy | — | 1125.3200 | — | — |

### Antimony (Z = 51)

_0 of 41 isotopes with a framework prediction; 0 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{102}$Sb | 102 | 51 | L?-pending | pending | binding_energy | — | 834.4620 | — | — |
| ${}^{103}$Sb | 103 | 52 | L?-pending | pending | binding_energy | — | 848.1020 | — | — |
| ${}^{104}$Sb | 104 | 53 | L?-pending | pending | binding_energy | — | 858.8320 | — | — |
| ${}^{105}$Sb | 105 | 54 | L?-pending | pending | binding_energy | — | 871.6042 | — | — |
| ${}^{106}$Sb | 106 | 55 | L?-pending | pending | binding_energy | — | 882.1333 | — | — |
| ${}^{107}$Sb | 107 | 56 | L?-pending | pending | binding_energy | — | 894.3846 | — | — |
| ${}^{108}$Sb | 108 | 57 | L?-pending | pending | binding_energy | — | 904.2480 | — | — |
| ${}^{109}$Sb | 109 | 58 | L?-pending | pending | binding_energy | — | 916.1250 | — | — |
| ${}^{110}$Sb | 110 | 59 | L?-pending | pending | binding_energy | — | 925.3950 | — | — |
| ${}^{111}$Sb | 111 | 60 | L?-pending | pending | binding_energy | — | 936.8534 | — | — |
| ${}^{112}$Sb | 112 | 61 | L?-pending | pending | binding_energy | — | 945.6869 | — | — |
| ${}^{113}$Sb | 113 | 62 | L?-pending | pending | binding_energy | — | 956.5762 | — | — |
| ${}^{114}$Sb | 114 | 63 | L?-pending | pending | binding_energy | — | 964.7272 | — | — |
| ${}^{115}$Sb | 115 | 64 | L?-pending | pending | binding_energy | — | 975.3053 | — | — |
| ${}^{116}$Sb | 116 | 65 | L?-pending | pending | binding_energy | — | 983.1952 | — | — |
| ${}^{117}$Sb | 117 | 66 | L?-pending | pending | binding_energy | — | 993.0841 | — | — |
| ${}^{118}$Sb | 118 | 67 | L?-pending | pending | binding_energy | — | 1000.5120 | — | — |
| ${}^{119}$Sb | 119 | 68 | L?-pending | pending | binding_energy | — | 1010.0627 | — | — |
| ${}^{120}$Sb | 120 | 69 | L?-pending | pending | binding_energy | — | 1017.0756 | — | — |
| ${}^{121}$Sb | 121 | 70 | L?-pending | pending | binding_energy | — | 1026.3289 | — | — |
| ${}^{122}$Sb | 122 | 71 | L?-pending | pending | binding_energy | — | 1033.1353 | — | — |
| ${}^{123}$Sb | 123 | 72 | L?-pending | pending | binding_energy | — | 1042.0953 | — | — |
| ${}^{124}$Sb | 124 | 73 | L?-pending | pending | binding_energy | — | 1048.5628 | — | — |
| ${}^{125}$Sb | 125 | 74 | L?-pending | pending | binding_energy | — | 1057.2702 | — | — |
| ${}^{126}$Sb | 126 | 75 | L?-pending | pending | binding_energy | — | 1063.4795 | — | — |
| ${}^{127}$Sb | 127 | 76 | L?-pending | pending | binding_energy | — | 1071.8560 | — | — |
| ${}^{128}$Sb | 128 | 77 | L?-pending | pending | binding_energy | — | 1077.8589 | — | — |
| ${}^{129}$Sb | 129 | 78 | L?-pending | pending | binding_energy | — | 1085.9297 | — | — |
| ${}^{130}$Sb | 130 | 79 | L?-pending | pending | binding_energy | — | 1091.6573 | — | — |
| ${}^{131}$Sb | 131 | 80 | L?-pending | pending | binding_energy | — | 1099.4244 | — | — |
| ${}^{132}$Sb | 132 | 81 | L?-pending | pending | binding_energy | — | 1105.1496 | — | — |
| ${}^{133}$Sb | 133 | 82 | L?-pending | pending | binding_energy | — | 1112.5091 | — | — |
| ${}^{134}$Sb | 134 | 83 | L?-pending | pending | binding_energy | — | 1115.6759 | — | — |
| ${}^{135}$Sb | 135 | 84 | L?-pending | pending | binding_energy | — | 1119.4186 | — | — |
| ${}^{136}$Sb | 136 | 85 | L?-pending | pending | binding_energy | — | 1122.3064 | — | — |
| ${}^{137}$Sb | 137 | 86 | L?-pending | pending | binding_energy | — | 1125.9313 | — | — |
| ${}^{138}$Sb | 138 | 87 | L?-pending | pending | binding_energy | — | 1128.5640 | — | — |
| ${}^{139}$Sb | 139 | 88 | L?-pending | pending | binding_energy | — | 1132.0160 | — | — |
| ${}^{140}$Sb | 140 | 89 | L?-pending | pending | binding_energy | — | 1134.4200 | — | — |
| ${}^{141}$Sb | 141 | 90 | L?-pending | pending | binding_energy | — | 1137.7290 | — | — |
| ${}^{142}$Sb | 142 | 91 | L?-pending | pending | binding_energy | — | 1139.8340 | — | — |

### Tellurium (Z = 52)

_0 of 42 isotopes with a framework prediction; 0 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{104}$Te | 104 | 52 | L?-pending | pending | binding_energy | — | 848.3619 | — | — |
| ${}^{105}$Te | 105 | 53 | L?-pending | pending | binding_energy | — | 859.6179 | — | — |
| ${}^{106}$Te | 106 | 54 | L?-pending | pending | binding_energy | — | 873.0974 | — | — |
| ${}^{107}$Te | 107 | 55 | L?-pending | pending | binding_energy | — | 883.6060 | — | — |
| ${}^{108}$Te | 108 | 56 | L?-pending | pending | binding_energy | — | 896.8020 | — | — |
| ${}^{109}$Te | 109 | 57 | L?-pending | pending | binding_energy | — | 906.8070 | — | — |
| ${}^{110}$Te | 110 | 58 | L?-pending | pending | binding_energy | — | 919.3928 | — | — |
| ${}^{111}$Te | 111 | 59 | L?-pending | pending | binding_energy | — | 928.8217 | — | — |
| ${}^{112}$Te | 112 | 60 | L?-pending | pending | binding_energy | — | 940.8731 | — | — |
| ${}^{113}$Te | 113 | 61 | L?-pending | pending | binding_energy | — | 949.7239 | — | — |
| ${}^{114}$Te | 114 | 62 | L?-pending | pending | binding_energy | — | 961.3379 | — | — |
| ${}^{115}$Te | 115 | 63 | L?-pending | pending | binding_energy | — | 969.5823 | — | — |
| ${}^{116}$Te | 116 | 64 | L?-pending | pending | binding_energy | — | 980.8546 | — | — |
| ${}^{117}$Te | 117 | 65 | L?-pending | pending | binding_energy | — | 988.7577 | — | — |
| ${}^{118}$Te | 118 | 66 | L?-pending | pending | binding_energy | — | 999.4242 | — | — |
| ${}^{119}$Te | 119 | 67 | L?-pending | pending | binding_energy | — | 1006.9873 | — | — |
| ${}^{120}$Te | 120 | 68 | L?-pending | pending | binding_energy | — | 1017.2383 | — | — |
| ${}^{121}$Te | 121 | 69 | L?-pending | pending | binding_energy | — | 1024.4906 | — | — |
| ${}^{122}$Te | 122 | 70 | L?-pending | pending | binding_energy | — | 1034.3320 | — | — |
| ${}^{123}$Te | 123 | 71 | L?-pending | pending | binding_energy | — | 1041.2611 | — | — |
| ${}^{124}$Te | 124 | 72 | L?-pending | pending | binding_energy | — | 1050.6855 | — | — |
| ${}^{125}$Te | 125 | 73 | L?-pending | pending | binding_energy | — | 1057.2545 | — | — |
| ${}^{126}$Te | 126 | 74 | L?-pending | pending | binding_energy | — | 1066.3682 | — | — |
| ${}^{127}$Te | 127 | 75 | L?-pending | pending | binding_energy | — | 1072.6558 | — | — |
| ${}^{128}$Te | 128 | 76 | L?-pending | pending | binding_energy | — | 1081.4405 | — | — |
| ${}^{129}$Te | 129 | 77 | L?-pending | pending | binding_energy | — | 1087.5229 | — | — |
| ${}^{130}$Te | 130 | 78 | L?-pending | pending | binding_energy | — | 1095.9423 | — | — |
| ${}^{131}$Te | 131 | 79 | L?-pending | pending | binding_energy | — | 1101.8716 | — | — |
| ${}^{132}$Te | 132 | 80 | L?-pending | pending | binding_energy | — | 1109.9201 | — | — |
| ${}^{133}$Te | 133 | 81 | L?-pending | pending | binding_energy | — | 1115.7404 | — | — |
| ${}^{134}$Te | 134 | 82 | L?-pending | pending | binding_energy | — | 1123.4083 | — | — |
| ${}^{135}$Te | 135 | 83 | L?-pending | pending | binding_energy | — | 1126.6747 | — | — |
| ${}^{136}$Te | 136 | 84 | L?-pending | pending | binding_energy | — | 1131.4425 | — | — |
| ${}^{137}$Te | 137 | 85 | L?-pending | pending | binding_energy | — | 1134.3923 | — | — |
| ${}^{138}$Te | 138 | 86 | L?-pending | pending | binding_energy | — | 1138.8558 | — | — |
| ${}^{139}$Te | 139 | 87 | L?-pending | pending | binding_energy | — | 1141.4363 | — | — |
| ${}^{140}$Te | 140 | 88 | L?-pending | pending | binding_energy | — | 1145.6699 | — | — |
| ${}^{141}$Te | 141 | 89 | L?-pending | pending | binding_energy | — | 1148.0220 | — | — |
| ${}^{142}$Te | 142 | 90 | L?-pending | pending | binding_energy | — | 1152.0460 | — | — |
| ${}^{143}$Te | 143 | 91 | L?-pending | pending | binding_energy | — | 1154.0100 | — | — |
| ${}^{144}$Te | 144 | 92 | L?-pending | pending | binding_energy | — | 1157.7600 | — | — |
| ${}^{145}$Te | 145 | 93 | L?-pending | pending | binding_energy | — | 1159.7100 | — | — |

### Iodine (Z = 53)

_0 of 42 isotopes with a framework prediction; 0 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{106}$I | 106 | 53 | L?-pending | pending | binding_energy | — | 857.4340 | — | — |
| ${}^{107}$I | 107 | 54 | L?-pending | pending | binding_energy | — | 871.6220 | — | — |
| ${}^{108}$I | 108 | 55 | L?-pending | pending | binding_energy | — | 883.0080 | — | — |
| ${}^{109}$I | 109 | 56 | L?-pending | pending | binding_energy | — | 895.9818 | — | — |
| ${}^{110}$I | 110 | 57 | L?-pending | pending | binding_energy | — | 906.8484 | — | — |
| ${}^{111}$I | 111 | 58 | L?-pending | pending | binding_energy | — | 919.4057 | — | — |
| ${}^{112}$I | 112 | 59 | L?-pending | pending | binding_energy | — | 929.5866 | — | — |
| ${}^{113}$I | 113 | 60 | L?-pending | pending | binding_energy | — | 941.7141 | — | — |
| ${}^{114}$I | 114 | 61 | L?-pending | pending | binding_energy | — | 951.3048 | — | — |
| ${}^{115}$I | 115 | 62 | L?-pending | pending | binding_energy | — | 963.0750 | — | — |
| ${}^{116}$I | 116 | 63 | L?-pending | pending | binding_energy | — | 972.2292 | — | — |
| ${}^{117}$I | 117 | 64 | L?-pending | pending | binding_energy | — | 983.3184 | — | — |
| ${}^{118}$I | 118 | 65 | L?-pending | pending | binding_energy | — | 991.9222 | — | — |
| ${}^{119}$I | 119 | 66 | L?-pending | pending | binding_energy | — | 1002.8002 | — | — |
| ${}^{120}$I | 120 | 67 | L?-pending | pending | binding_energy | — | 1010.8409 | — | — |
| ${}^{121}$I | 121 | 68 | L?-pending | pending | binding_energy | — | 1021.4107 | — | — |
| ${}^{122}$I | 122 | 69 | L?-pending | pending | binding_energy | — | 1029.3157 | — | — |
| ${}^{123}$I | 123 | 70 | L?-pending | pending | binding_energy | — | 1039.2503 | — | — |
| ${}^{124}$I | 124 | 71 | L?-pending | pending | binding_energy | — | 1046.7436 | — | — |
| ${}^{125}$I | 125 | 72 | L?-pending | pending | binding_energy | — | 1056.2864 | — | — |
| ${}^{126}$I | 126 | 73 | L?-pending | pending | binding_energy | — | 1063.4322 | — | — |
| ${}^{127}$I | 127 | 74 | L?-pending | pending | binding_energy | — | 1072.5762 | — | — |
| ${}^{128}$I | 128 | 75 | L?-pending | pending | binding_energy | — | 1079.4024 | — | — |
| ${}^{129}$I | 129 | 76 | L?-pending | pending | binding_energy | — | 1088.2428 | — | — |
| ${}^{130}$I | 130 | 77 | L?-pending | pending | binding_energy | — | 1094.7431 | — | — |
| ${}^{131}$I | 131 | 78 | L?-pending | pending | binding_energy | — | 1103.3210 | — | — |
| ${}^{132}$I | 132 | 79 | L?-pending | pending | binding_energy | — | 1109.6531 | — | — |
| ${}^{133}$I | 133 | 80 | L?-pending | pending | binding_energy | — | 1117.8782 | — | — |
| ${}^{134}$I | 134 | 81 | L?-pending | pending | binding_energy | — | 1124.1357 | — | — |
| ${}^{135}$I | 135 | 82 | L?-pending | pending | binding_energy | — | 1131.9427 | — | — |
| ${}^{136}$I | 136 | 83 | L?-pending | pending | binding_energy | — | 1135.7801 | — | — |
| ${}^{137}$I | 137 | 84 | L?-pending | pending | binding_energy | — | 1140.6625 | — | — |
| ${}^{138}$I | 138 | 85 | L?-pending | pending | binding_energy | — | 1144.3574 | — | — |
| ${}^{139}$I | 139 | 86 | L?-pending | pending | binding_energy | — | 1148.9198 | — | — |
| ${}^{140}$I | 140 | 87 | L?-pending | pending | binding_energy | — | 1152.1264 | — | — |
| ${}^{141}$I | 141 | 88 | L?-pending | pending | binding_energy | — | 1156.5181 | — | — |
| ${}^{142}$I | 142 | 89 | L?-pending | pending | binding_energy | — | 1159.4657 | — | — |
| ${}^{143}$I | 143 | 90 | L?-pending | pending | binding_energy | — | 1163.5910 | — | — |
| ${}^{144}$I | 144 | 91 | L?-pending | pending | binding_energy | — | 1166.1120 | — | — |
| ${}^{145}$I | 145 | 92 | L?-pending | pending | binding_energy | — | 1170.0050 | — | — |
| ${}^{146}$I | 146 | 93 | L?-pending | pending | binding_energy | — | 1172.5260 | — | — |
| ${}^{147}$I | 147 | 94 | L?-pending | pending | binding_energy | — | 1176.1470 | — | — |

### Xenon (Z = 54)

_0 of 43 isotopes with a framework prediction; 0 of 43 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{108}$Xe | 108 | 54 | L?-pending | pending | binding_energy | — | 872.0880 | — | — |
| ${}^{109}$Xe | 109 | 55 | L?-pending | pending | binding_energy | — | 883.6965 | — | — |
| ${}^{110}$Xe | 110 | 56 | L?-pending | pending | binding_energy | — | 897.5209 | — | — |
| ${}^{111}$Xe | 111 | 57 | L?-pending | pending | binding_energy | — | 908.2020 | — | — |
| ${}^{112}$Xe | 112 | 58 | L?-pending | pending | binding_energy | — | 921.7672 | — | — |
| ${}^{113}$Xe | 113 | 59 | L?-pending | pending | binding_energy | — | 932.0158 | — | — |
| ${}^{114}$Xe | 114 | 60 | L?-pending | pending | binding_energy | — | 944.9694 | — | — |
| ${}^{115}$Xe | 115 | 61 | L?-pending | pending | binding_energy | — | 954.6116 | — | — |
| ${}^{116}$Xe | 116 | 62 | L?-pending | pending | binding_energy | — | 967.0730 | — | — |
| ${}^{117}$Xe | 117 | 63 | L?-pending | pending | binding_energy | — | 976.2828 | — | — |
| ${}^{118}$Xe | 118 | 64 | L?-pending | pending | binding_energy | — | 988.2479 | — | — |
| ${}^{119}$Xe | 119 | 65 | L?-pending | pending | binding_energy | — | 997.0346 | — | — |
| ${}^{120}$Xe | 120 | 66 | L?-pending | pending | binding_energy | — | 1008.4839 | — | — |
| ${}^{121}$Xe | 121 | 67 | L?-pending | pending | binding_energy | — | 1016.8637 | — | — |
| ${}^{122}$Xe | 122 | 68 | L?-pending | pending | binding_energy | — | 1027.8091 | — | — |
| ${}^{123}$Xe | 123 | 69 | L?-pending | pending | binding_energy | — | 1035.7736 | — | — |
| ${}^{124}$Xe | 124 | 70 | L?-pending | pending | binding_energy | — | 1046.2641 | — | — |
| ${}^{125}$Xe | 125 | 71 | L?-pending | pending | binding_energy | — | 1053.8674 | — | — |
| ${}^{126}$Xe | 126 | 72 | L?-pending | pending | binding_energy | — | 1063.8857 | — | — |
| ${}^{127}$Xe | 127 | 73 | L?-pending | pending | binding_energy | — | 1071.1315 | — | — |
| ${}^{128}$Xe | 128 | 74 | L?-pending | pending | binding_energy | — | 1080.7425 | — | — |
| ${}^{129}$Xe | 129 | 75 | L?-pending | pending | binding_energy | — | 1087.6494 | — | — |
| ${}^{130}$Xe | 130 | 76 | L?-pending | pending | binding_energy | — | 1096.9051 | — | — |
| ${}^{131}$Xe | 131 | 77 | L?-pending | pending | binding_energy | — | 1103.5095 | — | — |
| ${}^{132}$Xe | 132 | 78 | L?-pending | pending | binding_energy | — | 1112.4462 | — | — |
| ${}^{133}$Xe | 133 | 79 | L?-pending | pending | binding_energy | — | 1118.8821 | — | — |
| ${}^{134}$Xe | 134 | 80 | L?-pending | pending | binding_energy | — | 1127.4357 | — | — |
| ${}^{135}$Xe | 135 | 81 | L?-pending | pending | binding_energy | — | 1133.7946 | — | — |
| ${}^{136}$Xe | 136 | 82 | L?-pending | pending | binding_energy | — | 1141.8817 | — | — |
| ${}^{137}$Xe | 137 | 83 | L?-pending | pending | binding_energy | — | 1145.9073 | — | — |
| ${}^{138}$Xe | 138 | 84 | L?-pending | pending | binding_energy | — | 1151.5674 | — | — |
| ${}^{139}$Xe | 139 | 85 | L?-pending | pending | binding_energy | — | 1155.3111 | — | — |
| ${}^{140}$Xe | 140 | 86 | L?-pending | pending | binding_energy | — | 1160.7242 | — | — |
| ${}^{141}$Xe | 141 | 87 | L?-pending | pending | binding_energy | — | 1164.0064 | — | — |
| ${}^{142}$Xe | 142 | 88 | L?-pending | pending | binding_energy | — | 1169.1101 | — | — |
| ${}^{143}$Xe | 143 | 89 | L?-pending | pending | binding_energy | — | 1172.1546 | — | — |
| ${}^{144}$Xe | 144 | 90 | L?-pending | pending | binding_energy | — | 1176.8954 | — | — |
| ${}^{145}$Xe | 145 | 91 | L?-pending | pending | binding_energy | — | 1179.5877 | — | — |
| ${}^{146}$Xe | 146 | 92 | L?-pending | pending | binding_energy | — | 1184.1206 | — | — |
| ${}^{147}$Xe | 147 | 93 | L?-pending | pending | binding_energy | — | 1186.5840 | — | — |
| ${}^{148}$Xe | 148 | 94 | L?-pending | pending | binding_energy | — | 1190.9560 | — | — |
| ${}^{149}$Xe | 149 | 95 | L?-pending | pending | binding_energy | — | 1193.3410 | — | — |
| ${}^{150}$Xe | 150 | 96 | L?-pending | pending | binding_energy | — | 1197.4500 | — | — |

### Caesium (Z = 55)

_0 of 42 isotopes with a framework prediction; 0 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{111}$Cs | 111 | 56 | L?-pending | pending | binding_energy | — | 895.7700 | — | — |
| ${}^{112}$Cs | 112 | 57 | L?-pending | pending | binding_energy | — | 907.4240 | — | — |
| ${}^{113}$Cs | 113 | 58 | L?-pending | pending | binding_energy | — | 920.7944 | — | — |
| ${}^{114}$Cs | 114 | 59 | L?-pending | pending | binding_energy | — | 931.7871 | — | — |
| ${}^{115}$Cs | 115 | 60 | L?-pending | pending | binding_energy | — | 944.8400 | — | — |
| ${}^{116}$Cs | 116 | 61 | L?-pending | pending | binding_energy | — | 955.2600 | — | — |
| ${}^{117}$Cs | 117 | 62 | L?-pending | pending | binding_energy | — | 967.8082 | — | — |
| ${}^{118}$Cs | 118 | 63 | L?-pending | pending | binding_energy | — | 977.7958 | — | — |
| ${}^{119}$Cs | 119 | 64 | L?-pending | pending | binding_energy | — | 989.7628 | — | — |
| ${}^{120}$Cs | 120 | 65 | L?-pending | pending | binding_energy | — | 999.4177 | — | — |
| ${}^{121}$Cs | 121 | 66 | L?-pending | pending | binding_energy | — | 1010.7027 | — | — |
| ${}^{122}$Cs | 122 | 67 | L?-pending | pending | binding_energy | — | 1019.8165 | — | — |
| ${}^{123}$Cs | 123 | 68 | L?-pending | pending | binding_energy | — | 1030.7867 | — | — |
| ${}^{124}$Cs | 124 | 69 | L?-pending | pending | binding_energy | — | 1039.5554 | — | — |
| ${}^{125}$Cs | 125 | 70 | L?-pending | pending | binding_energy | — | 1049.9754 | — | — |
| ${}^{126}$Cs | 126 | 71 | L?-pending | pending | binding_energy | — | 1058.3077 | — | — |
| ${}^{127}$Cs | 127 | 72 | L?-pending | pending | binding_energy | — | 1068.2683 | — | — |
| ${}^{128}$Cs | 128 | 73 | L?-pending | pending | binding_energy | — | 1076.0314 | — | — |
| ${}^{129}$Cs | 129 | 74 | L?-pending | pending | binding_energy | — | 1085.6700 | — | — |
| ${}^{130}$Cs | 130 | 75 | L?-pending | pending | binding_energy | — | 1093.1420 | — | — |
| ${}^{131}$Cs | 131 | 76 | L?-pending | pending | binding_energy | — | 1102.3692 | — | — |
| ${}^{132}$Cs | 132 | 77 | L?-pending | pending | binding_energy | — | 1109.5376 | — | — |
| ${}^{133}$Cs | 133 | 78 | L?-pending | pending | binding_energy | — | 1118.5272 | — | — |
| ${}^{134}$Cs | 134 | 79 | L?-pending | pending | binding_energy | — | 1125.4187 | — | — |
| ${}^{135}$Cs | 135 | 80 | L?-pending | pending | binding_energy | — | 1134.1808 | — | — |
| ${}^{136}$Cs | 136 | 81 | L?-pending | pending | binding_energy | — | 1141.0090 | — | — |
| ${}^{137}$Cs | 137 | 82 | L?-pending | pending | binding_energy | — | 1149.2873 | — | — |
| ${}^{138}$Cs | 138 | 83 | L?-pending | pending | binding_energy | — | 1153.6998 | — | — |
| ${}^{139}$Cs | 139 | 84 | L?-pending | pending | binding_energy | — | 1159.5852 | — | — |
| ${}^{140}$Cs | 140 | 85 | L?-pending | pending | binding_energy | — | 1164.0052 | — | — |
| ${}^{141}$Cs | 141 | 86 | L?-pending | pending | binding_energy | — | 1169.5041 | — | — |
| ${}^{142}$Cs | 142 | 87 | L?-pending | pending | binding_energy | — | 1173.6126 | — | — |
| ${}^{143}$Cs | 143 | 88 | L?-pending | pending | binding_energy | — | 1178.8449 | — | — |
| ${}^{144}$Cs | 144 | 89 | L?-pending | pending | binding_energy | — | 1182.5121 | — | — |
| ${}^{145}$Cs | 145 | 90 | L?-pending | pending | binding_energy | — | 1187.3665 | — | — |
| ${}^{146}$Cs | 146 | 91 | L?-pending | pending | binding_energy | — | 1190.6937 | — | — |
| ${}^{147}$Cs | 147 | 92 | L?-pending | pending | binding_energy | — | 1195.3747 | — | — |
| ${}^{148}$Cs | 148 | 93 | L?-pending | pending | binding_energy | — | 1198.4369 | — | — |
| ${}^{149}$Cs | 149 | 94 | L?-pending | pending | binding_energy | — | 1202.8770 | — | — |
| ${}^{150}$Cs | 150 | 95 | L?-pending | pending | binding_energy | — | 1205.8500 | — | — |
| ${}^{151}$Cs | 151 | 96 | L?-pending | pending | binding_energy | — | 1209.9630 | — | — |
| ${}^{152}$Cs | 152 | 97 | L?-pending | pending | binding_energy | — | 1212.9600 | — | — |

### Barium (Z = 56)

_0 of 42 isotopes with a framework prediction; 0 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{113}$Ba | 113 | 57 | L?-pending | pending | binding_energy | — | 907.9550 | — | — |
| ${}^{114}$Ba | 114 | 58 | L?-pending | pending | binding_energy | — | 922.2243 | — | — |
| ${}^{115}$Ba | 115 | 59 | L?-pending | pending | binding_energy | — | 933.3400 | — | — |
| ${}^{116}$Ba | 116 | 60 | L?-pending | pending | binding_energy | — | 946.7920 | — | — |
| ${}^{117}$Ba | 117 | 61 | L?-pending | pending | binding_energy | — | 957.9907 | — | — |
| ${}^{118}$Ba | 118 | 62 | L?-pending | pending | binding_energy | — | 970.7860 | — | — |
| ${}^{119}$Ba | 119 | 63 | L?-pending | pending | binding_energy | — | 981.2655 | — | — |
| ${}^{120}$Ba | 120 | 64 | L?-pending | pending | binding_energy | — | 993.6354 | — | — |
| ${}^{121}$Ba | 121 | 65 | L?-pending | pending | binding_energy | — | 1003.5629 | — | — |
| ${}^{122}$Ba | 122 | 66 | L?-pending | pending | binding_energy | — | 1015.4983 | — | — |
| ${}^{123}$Ba | 123 | 67 | L?-pending | pending | binding_energy | — | 1024.6157 | — | — |
| ${}^{124}$Ba | 124 | 68 | L?-pending | pending | binding_energy | — | 1036.1218 | — | — |
| ${}^{125}$Ba | 125 | 69 | L?-pending | pending | binding_energy | — | 1044.7723 | — | — |
| ${}^{126}$Ba | 126 | 70 | L?-pending | pending | binding_energy | — | 1055.8446 | — | — |
| ${}^{127}$Ba | 127 | 71 | L?-pending | pending | binding_energy | — | 1064.0639 | — | — |
| ${}^{128}$Ba | 128 | 72 | L?-pending | pending | binding_energy | — | 1074.6864 | — | — |
| ${}^{129}$Ba | 129 | 73 | L?-pending | pending | binding_energy | — | 1082.4495 | — | — |
| ${}^{130}$Ba | 130 | 74 | L?-pending | pending | binding_energy | — | 1092.7167 | — | — |
| ${}^{131}$Ba | 131 | 75 | L?-pending | pending | binding_energy | — | 1100.2102 | — | — |
| ${}^{132}$Ba | 132 | 76 | L?-pending | pending | binding_energy | — | 1110.0375 | — | — |
| ${}^{133}$Ba | 133 | 77 | L?-pending | pending | binding_energy | — | 1117.2274 | — | — |
| ${}^{134}$Ba | 134 | 78 | L?-pending | pending | binding_energy | — | 1126.6952 | — | — |
| ${}^{135}$Ba | 135 | 79 | L?-pending | pending | binding_energy | — | 1133.6672 | — | — |
| ${}^{136}$Ba | 136 | 80 | L?-pending | pending | binding_energy | — | 1142.7749 | — | — |
| ${}^{137}$Ba | 137 | 81 | L?-pending | pending | binding_energy | — | 1149.6805 | — | — |
| ${}^{138}$Ba | 138 | 82 | L?-pending | pending | binding_energy | — | 1158.2923 | — | — |
| ${}^{139}$Ba | 139 | 83 | L?-pending | pending | binding_energy | — | 1163.0157 | — | — |
| ${}^{140}$Ba | 140 | 84 | L?-pending | pending | binding_energy | — | 1169.4410 | — | — |
| ${}^{141}$Ba | 141 | 85 | L?-pending | pending | binding_energy | — | 1173.9769 | — | — |
| ${}^{142}$Ba | 142 | 86 | L?-pending | pending | binding_energy | — | 1180.1580 | — | — |
| ${}^{143}$Ba | 143 | 87 | L?-pending | pending | binding_energy | — | 1184.3243 | — | — |
| ${}^{144}$Ba | 144 | 88 | L?-pending | pending | binding_energy | — | 1190.2255 | — | — |
| ${}^{145}$Ba | 145 | 89 | L?-pending | pending | binding_energy | — | 1194.0459 | — | — |
| ${}^{146}$Ba | 146 | 90 | L?-pending | pending | binding_energy | — | 1199.4673 | — | — |
| ${}^{147}$Ba | 147 | 91 | L?-pending | pending | binding_energy | — | 1202.9364 | — | — |
| ${}^{148}$Ba | 148 | 92 | L?-pending | pending | binding_energy | — | 1208.2885 | — | — |
| ${}^{149}$Ba | 149 | 93 | L?-pending | pending | binding_energy | — | 1211.6456 | — | — |
| ${}^{150}$Ba | 150 | 94 | L?-pending | pending | binding_energy | — | 1216.7761 | — | — |
| ${}^{151}$Ba | 151 | 95 | L?-pending | pending | binding_energy | — | 1219.9290 | — | — |
| ${}^{152}$Ba | 152 | 96 | L?-pending | pending | binding_energy | — | 1224.6640 | — | — |
| ${}^{153}$Ba | 153 | 97 | L?-pending | pending | binding_energy | — | 1227.5190 | — | — |
| ${}^{154}$Ba | 154 | 98 | L?-pending | pending | binding_energy | — | 1232.1540 | — | — |

### Lanthanum (Z = 57)

_0 of 42 isotopes with a framework prediction; 0 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{116}$La | 116 | 59 | L?-pending | pending | binding_energy | — | 931.7120 | — | — |
| ${}^{117}$La | 117 | 60 | L?-pending | pending | binding_energy | — | 946.0620 | — | — |
| ${}^{118}$La | 118 | 61 | L?-pending | pending | binding_energy | — | 957.4520 | — | — |
| ${}^{119}$La | 119 | 62 | L?-pending | pending | binding_energy | — | 970.9210 | — | — |
| ${}^{120}$La | 120 | 63 | L?-pending | pending | binding_energy | — | 981.4800 | — | — |
| ${}^{121}$La | 121 | 64 | L?-pending | pending | binding_energy | — | 994.2570 | — | — |
| ${}^{122}$La | 122 | 65 | L?-pending | pending | binding_energy | — | 1004.6700 | — | — |
| ${}^{123}$La | 123 | 66 | L?-pending | pending | binding_energy | — | 1016.8410 | — | — |
| ${}^{124}$La | 124 | 67 | L?-pending | pending | binding_energy | — | 1026.5083 | — | — |
| ${}^{125}$La | 125 | 68 | L?-pending | pending | binding_energy | — | 1038.0805 | — | — |
| ${}^{126}$La | 126 | 69 | L?-pending | pending | binding_energy | — | 1047.3658 | — | — |
| ${}^{127}$La | 127 | 70 | L?-pending | pending | binding_energy | — | 1058.3597 | — | — |
| ${}^{128}$La | 128 | 71 | L?-pending | pending | binding_energy | — | 1067.1604 | — | — |
| ${}^{129}$La | 129 | 72 | L?-pending | pending | binding_energy | — | 1077.9298 | — | — |
| ${}^{130}$La | 130 | 73 | L?-pending | pending | binding_energy | — | 1086.3049 | — | — |
| ${}^{131}$La | 131 | 74 | L?-pending | pending | binding_energy | — | 1096.5182 | — | — |
| ${}^{132}$La | 132 | 75 | L?-pending | pending | binding_energy | — | 1104.5438 | — | — |
| ${}^{133}$La | 133 | 76 | L?-pending | pending | binding_energy | — | 1114.3859 | — | — |
| ${}^{134}$La | 134 | 77 | L?-pending | pending | binding_energy | — | 1122.1815 | — | — |
| ${}^{135}$La | 135 | 78 | L?-pending | pending | binding_energy | — | 1131.6776 | — | — |
| ${}^{136}$La | 136 | 79 | L?-pending | pending | binding_energy | — | 1139.1430 | — | — |
| ${}^{137}$La | 137 | 80 | L?-pending | pending | binding_energy | — | 1148.3177 | — | — |
| ${}^{138}$La | 138 | 81 | L?-pending | pending | binding_energy | — | 1155.7615 | — | — |
| ${}^{139}$La | 139 | 82 | L?-pending | pending | binding_energy | — | 1164.5418 | — | — |
| ${}^{140}$La | 140 | 83 | L?-pending | pending | binding_energy | — | 1169.7028 | — | — |
| ${}^{141}$La | 141 | 84 | L?-pending | pending | binding_energy | — | 1176.3919 | — | — |
| ${}^{142}$La | 142 | 85 | L?-pending | pending | binding_energy | — | 1181.5573 | — | — |
| ${}^{143}$La | 143 | 86 | L?-pending | pending | binding_energy | — | 1187.7762 | — | — |
| ${}^{144}$La | 144 | 87 | L?-pending | pending | binding_energy | — | 1192.5257 | — | — |
| ${}^{145}$La | 145 | 88 | L?-pending | pending | binding_energy | — | 1198.5827 | — | — |
| ${}^{146}$La | 146 | 89 | L?-pending | pending | binding_energy | — | 1203.0398 | — | — |
| ${}^{147}$La | 147 | 90 | L?-pending | pending | binding_energy | — | 1208.5684 | — | — |
| ${}^{148}$La | 148 | 91 | L?-pending | pending | binding_energy | — | 1212.6700 | — | — |
| ${}^{149}$La | 149 | 92 | L?-pending | pending | binding_energy | — | 1218.2525 | — | — |
| ${}^{150}$La | 150 | 93 | L?-pending | pending | binding_energy | — | 1222.4151 | — | — |
| ${}^{151}$La | 151 | 94 | L?-pending | pending | binding_energy | — | 1227.4856 | — | — |
| ${}^{152}$La | 152 | 95 | L?-pending | pending | binding_energy | — | 1231.5040 | — | — |
| ${}^{153}$La | 153 | 96 | L?-pending | pending | binding_energy | — | 1236.3930 | — | — |
| ${}^{154}$La | 154 | 97 | L?-pending | pending | binding_energy | — | 1239.8540 | — | — |
| ${}^{155}$La | 155 | 98 | L?-pending | pending | binding_energy | — | 1244.3400 | — | — |
| ${}^{156}$La | 156 | 99 | L?-pending | pending | binding_energy | — | 1247.5320 | — | — |
| ${}^{157}$La | 157 | 100 | L?-pending | pending | binding_energy | — | 1251.6040 | — | — |

### Cerium (Z = 58)

_0 of 41 isotopes with a framework prediction; 0 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{119}$Ce | 119 | 61 | L?-pending | pending | binding_energy | — | 958.9020 | — | — |
| ${}^{120}$Ce | 120 | 62 | L?-pending | pending | binding_energy | — | 972.9600 | — | — |
| ${}^{121}$Ce | 121 | 63 | L?-pending | pending | binding_energy | — | 983.9720 | — | — |
| ${}^{122}$Ce | 122 | 64 | L?-pending | pending | binding_energy | — | 997.2280 | — | — |
| ${}^{123}$Ce | 123 | 65 | L?-pending | pending | binding_energy | — | 1007.7390 | — | — |
| ${}^{124}$Ce | 124 | 66 | L?-pending | pending | binding_energy | — | 1020.3960 | — | — |
| ${}^{125}$Ce | 125 | 67 | L?-pending | pending | binding_energy | — | 1030.2500 | — | — |
| ${}^{126}$Ce | 126 | 68 | L?-pending | pending | binding_energy | — | 1042.4305 | — | — |
| ${}^{127}$Ce | 127 | 69 | L?-pending | pending | binding_energy | — | 1051.6606 | — | — |
| ${}^{128}$Ce | 128 | 70 | L?-pending | pending | binding_energy | — | 1063.2865 | — | — |
| ${}^{129}$Ce | 129 | 71 | L?-pending | pending | binding_energy | — | 1072.1114 | — | — |
| ${}^{130}$Ce | 130 | 72 | L?-pending | pending | binding_energy | — | 1083.3181 | — | — |
| ${}^{131}$Ce | 131 | 73 | L?-pending | pending | binding_energy | — | 1091.6750 | — | — |
| ${}^{132}$Ce | 132 | 74 | L?-pending | pending | binding_energy | — | 1102.5065 | — | — |
| ${}^{133}$Ce | 133 | 75 | L?-pending | pending | binding_energy | — | 1110.5274 | — | — |
| ${}^{134}$Ce | 134 | 76 | L?-pending | pending | binding_energy | — | 1121.0134 | — | — |
| ${}^{135}$Ce | 135 | 77 | L?-pending | pending | binding_energy | — | 1128.8681 | — | — |
| ${}^{136}$Ce | 136 | 78 | L?-pending | pending | binding_energy | — | 1138.8317 | — | — |
| ${}^{137}$Ce | 137 | 79 | L?-pending | pending | binding_energy | — | 1146.3132 | — | — |
| ${}^{138}$Ce | 138 | 80 | L?-pending | pending | binding_energy | — | 1156.0316 | — | — |
| ${}^{139}$Ce | 139 | 81 | L?-pending | pending | binding_energy | — | 1163.4948 | — | — |
| ${}^{140}$Ce | 140 | 82 | L?-pending | pending | binding_energy | — | 1172.6826 | — | — |
| ${}^{141}$Ce | 141 | 83 | L?-pending | pending | binding_energy | — | 1178.1108 | — | — |
| ${}^{142}$Ce | 142 | 84 | L?-pending | pending | binding_energy | — | 1185.2839 | — | — |
| ${}^{143}$Ce | 143 | 85 | L?-pending | pending | binding_energy | — | 1190.4287 | — | — |
| ${}^{144}$Ce | 144 | 86 | L?-pending | pending | binding_energy | — | 1197.3256 | — | — |
| ${}^{145}$Ce | 145 | 87 | L?-pending | pending | binding_energy | — | 1202.0320 | — | — |
| ${}^{146}$Ce | 146 | 88 | L?-pending | pending | binding_energy | — | 1208.6622 | — | — |
| ${}^{147}$Ce | 147 | 89 | L?-pending | pending | binding_energy | — | 1213.1215 | — | — |
| ${}^{148}$Ce | 148 | 90 | L?-pending | pending | binding_energy | — | 1219.5774 | — | — |
| ${}^{149}$Ce | 149 | 91 | L?-pending | pending | binding_energy | — | 1223.9202 | — | — |
| ${}^{150}$Ce | 150 | 92 | L?-pending | pending | binding_energy | — | 1230.1684 | — | — |
| ${}^{151}$Ce | 151 | 93 | L?-pending | pending | binding_energy | — | 1234.6180 | — | — |
| ${}^{152}$Ce | 152 | 94 | L?-pending | pending | binding_energy | — | 1240.4720 | — | — |
| ${}^{153}$Ce | 153 | 95 | L?-pending | pending | binding_energy | — | 1244.5020 | — | — |
| ${}^{154}$Ce | 154 | 96 | L?-pending | pending | binding_energy | — | 1249.8640 | — | — |
| ${}^{155}$Ce | 155 | 97 | L?-pending | pending | binding_energy | — | 1253.4850 | — | — |
| ${}^{156}$Ce | 156 | 98 | L?-pending | pending | binding_energy | — | 1258.6080 | — | — |
| ${}^{157}$Ce | 157 | 99 | L?-pending | pending | binding_energy | — | 1261.8090 | — | — |
| ${}^{158}$Ce | 158 | 100 | L?-pending | pending | binding_energy | — | 1266.3700 | — | — |
| ${}^{159}$Ce | 159 | 101 | L?-pending | pending | binding_energy | — | 1269.2970 | — | — |

### Praseodymium (Z = 59)

_0 of 41 isotopes with a framework prediction; 0 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{121}$Pr | 121 | 62 | L?-pending | pending | binding_energy | — | 971.9930 | — | — |
| ${}^{122}$Pr | 122 | 63 | L?-pending | pending | binding_energy | — | 983.3200 | — | — |
| ${}^{123}$Pr | 123 | 64 | L?-pending | pending | binding_energy | — | 996.7920 | — | — |
| ${}^{124}$Pr | 124 | 65 | L?-pending | pending | binding_energy | — | 1007.8720 | — | — |
| ${}^{125}$Pr | 125 | 66 | L?-pending | pending | binding_energy | — | 1020.8750 | — | — |
| ${}^{126}$Pr | 126 | 67 | L?-pending | pending | binding_energy | — | 1031.1840 | — | — |
| ${}^{127}$Pr | 127 | 68 | L?-pending | pending | binding_energy | — | 1043.4320 | — | — |
| ${}^{128}$Pr | 128 | 69 | L?-pending | pending | binding_energy | — | 1053.3010 | — | — |
| ${}^{129}$Pr | 129 | 70 | L?-pending | pending | binding_energy | — | 1064.8151 | — | — |
| ${}^{130}$Pr | 130 | 71 | L?-pending | pending | binding_energy | — | 1074.2883 | — | — |
| ${}^{131}$Pr | 131 | 72 | L?-pending | pending | binding_energy | — | 1085.4849 | — | — |
| ${}^{132}$Pr | 132 | 73 | L?-pending | pending | binding_energy | — | 1094.4830 | — | — |
| ${}^{133}$Pr | 133 | 74 | L?-pending | pending | binding_energy | — | 1105.2644 | — | — |
| ${}^{134}$Pr | 134 | 75 | L?-pending | pending | binding_energy | — | 1113.9261 | — | — |
| ${}^{135}$Pr | 135 | 76 | L?-pending | pending | binding_energy | — | 1124.4053 | — | — |
| ${}^{136}$Pr | 136 | 77 | L?-pending | pending | binding_energy | — | 1132.8812 | — | — |
| ${}^{137}$Pr | 137 | 78 | L?-pending | pending | binding_energy | — | 1142.8139 | — | — |
| ${}^{138}$Pr | 138 | 79 | L?-pending | pending | binding_energy | — | 1150.8123 | — | — |
| ${}^{139}$Pr | 139 | 80 | L?-pending | pending | binding_energy | — | 1160.5834 | — | — |
| ${}^{140}$Pr | 140 | 81 | L?-pending | pending | binding_energy | — | 1168.5123 | — | — |
| ${}^{141}$Pr | 141 | 82 | L?-pending | pending | binding_energy | — | 1177.9119 | — | — |
| ${}^{142}$Pr | 142 | 83 | L?-pending | pending | binding_energy | — | 1183.7551 | — | — |
| ${}^{143}$Pr | 143 | 84 | L?-pending | pending | binding_energy | — | 1191.1082 | — | — |
| ${}^{144}$Pr | 144 | 85 | L?-pending | pending | binding_energy | — | 1196.8619 | — | — |
| ${}^{145}$Pr | 145 | 86 | L?-pending | pending | binding_energy | — | 1203.8086 | — | — |
| ${}^{146}$Pr | 146 | 87 | L?-pending | pending | binding_energy | — | 1208.9275 | — | — |
| ${}^{147}$Pr | 147 | 88 | L?-pending | pending | binding_energy | — | 1215.7694 | — | — |
| ${}^{148}$Pr | 148 | 89 | L?-pending | pending | binding_energy | — | 1220.9321 | — | — |
| ${}^{149}$Pr | 149 | 90 | L?-pending | pending | binding_energy | — | 1227.5073 | — | — |
| ${}^{150}$Pr | 150 | 91 | L?-pending | pending | binding_energy | — | 1232.8397 | — | — |
| ${}^{151}$Pr | 151 | 92 | L?-pending | pending | binding_energy | — | 1239.3902 | — | — |
| ${}^{152}$Pr | 152 | 93 | L?-pending | pending | binding_energy | — | 1244.4399 | — | — |
| ${}^{153}$Pr | 153 | 94 | L?-pending | pending | binding_energy | — | 1250.3217 | — | — |
| ${}^{154}$Pr | 154 | 95 | L?-pending | pending | binding_energy | — | 1254.6841 | — | — |
| ${}^{155}$Pr | 155 | 96 | L?-pending | pending | binding_energy | — | 1260.3112 | — | — |
| ${}^{156}$Pr | 156 | 97 | L?-pending | pending | binding_energy | — | 1264.4165 | — | — |
| ${}^{157}$Pr | 157 | 98 | L?-pending | pending | binding_energy | — | 1269.4733 | — | — |
| ${}^{158}$Pr | 158 | 99 | L?-pending | pending | binding_energy | — | 1273.3220 | — | — |
| ${}^{159}$Pr | 159 | 100 | L?-pending | pending | binding_energy | — | 1277.8830 | — | — |
| ${}^{160}$Pr | 160 | 101 | L?-pending | pending | binding_energy | — | 1281.4400 | — | — |
| ${}^{161}$Pr | 161 | 102 | L?-pending | pending | binding_energy | — | 1285.7460 | — | — |

### Neodymium (Z = 60)

_0 of 40 isotopes with a framework prediction; 0 of 40 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{124}$Nd | 124 | 64 | L?-pending | pending | binding_energy | — | 998.6960 | — | — |
| ${}^{125}$Nd | 125 | 65 | L?-pending | pending | binding_energy | — | 1010.0000 | — | — |
| ${}^{126}$Nd | 126 | 66 | L?-pending | pending | binding_energy | — | 1023.3720 | — | — |
| ${}^{127}$Nd | 127 | 67 | L?-pending | pending | binding_energy | — | 1034.0340 | — | — |
| ${}^{128}$Nd | 128 | 68 | L?-pending | pending | binding_energy | — | 1046.6560 | — | — |
| ${}^{129}$Nd | 129 | 69 | L?-pending | pending | binding_energy | — | 1056.6390 | — | — |
| ${}^{130}$Nd | 130 | 70 | L?-pending | pending | binding_energy | — | 1068.9268 | — | — |
| ${}^{131}$Nd | 131 | 71 | L?-pending | pending | binding_energy | — | 1078.1699 | — | — |
| ${}^{132}$Nd | 132 | 72 | L?-pending | pending | binding_energy | — | 1089.8990 | — | — |
| ${}^{133}$Nd | 133 | 73 | L?-pending | pending | binding_energy | — | 1098.8769 | — | — |
| ${}^{134}$Nd | 134 | 74 | L?-pending | pending | binding_energy | — | 1110.2622 | — | — |
| ${}^{135}$Nd | 135 | 75 | L?-pending | pending | binding_energy | — | 1118.9007 | — | — |
| ${}^{136}$Nd | 136 | 76 | L?-pending | pending | binding_energy | — | 1129.9577 | — | — |
| ${}^{137}$Nd | 137 | 77 | L?-pending | pending | binding_energy | — | 1138.4137 | — | — |
| ${}^{138}$Nd | 138 | 78 | L?-pending | pending | binding_energy | — | 1148.9183 | — | — |
| ${}^{139}$Nd | 139 | 79 | L?-pending | pending | binding_energy | — | 1156.9893 | — | — |
| ${}^{140}$Nd | 140 | 80 | L?-pending | pending | binding_energy | — | 1167.3010 | — | — |
| ${}^{141}$Nd | 141 | 81 | L?-pending | pending | binding_energy | — | 1175.3065 | — | — |
| ${}^{142}$Nd | 142 | 82 | L?-pending | pending | binding_energy | — | 1185.1364 | — | — |
| ${}^{143}$Nd | 143 | 83 | L?-pending | pending | binding_energy | — | 1191.2600 | — | — |
| ${}^{144}$Nd | 144 | 84 | L?-pending | pending | binding_energy | — | 1199.0770 | — | — |
| ${}^{145}$Nd | 145 | 85 | L?-pending | pending | binding_energy | — | 1204.8323 | — | — |
| ${}^{146}$Nd | 146 | 86 | L?-pending | pending | binding_energy | — | 1212.3975 | — | — |
| ${}^{147}$Nd | 147 | 87 | L?-pending | pending | binding_energy | — | 1217.6897 | — | — |
| ${}^{148}$Nd | 148 | 88 | L?-pending | pending | binding_energy | — | 1225.0223 | — | — |
| ${}^{149}$Nd | 149 | 89 | L?-pending | pending | binding_energy | — | 1230.0611 | — | — |
| ${}^{150}$Nd | 150 | 90 | L?-pending | pending | binding_energy | — | 1237.4368 | — | — |
| ${}^{151}$Nd | 151 | 91 | L?-pending | pending | binding_energy | — | 1242.7714 | — | — |
| ${}^{152}$Nd | 152 | 92 | L?-pending | pending | binding_energy | — | 1250.0492 | — | — |
| ${}^{153}$Nd | 153 | 93 | L?-pending | pending | binding_energy | — | 1255.3012 | — | — |
| ${}^{154}$Nd | 154 | 94 | L?-pending | pending | binding_energy | — | 1261.6218 | — | — |
| ${}^{155}$Nd | 155 | 95 | L?-pending | pending | binding_energy | — | 1266.3973 | — | — |
| ${}^{156}$Nd | 156 | 96 | L?-pending | pending | binding_energy | — | 1272.3869 | — | — |
| ${}^{157}$Nd | 157 | 97 | L?-pending | pending | binding_energy | — | 1276.7502 | — | — |
| ${}^{158}$Nd | 158 | 98 | L?-pending | pending | binding_energy | — | 1282.1626 | — | — |
| ${}^{159}$Nd | 159 | 99 | L?-pending | pending | binding_energy | — | 1286.1228 | — | — |
| ${}^{160}$Nd | 160 | 100 | L?-pending | pending | binding_energy | — | 1291.1946 | — | — |
| ${}^{161}$Nd | 161 | 101 | L?-pending | pending | binding_energy | — | 1294.7620 | — | — |
| ${}^{162}$Nd | 162 | 102 | L?-pending | pending | binding_energy | — | 1299.5640 | — | — |
| ${}^{163}$Nd | 163 | 103 | L?-pending | pending | binding_energy | — | 1302.6960 | — | — |

### Promethium (Z = 61)

_0 of 40 isotopes with a framework prediction; 0 of 40 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{126}$Pm | 126 | 65 | L?-pending | pending | binding_energy | — | 1009.0080 | — | — |
| ${}^{127}$Pm | 127 | 66 | L?-pending | pending | binding_energy | — | 1022.6040 | — | — |
| ${}^{128}$Pm | 128 | 67 | L?-pending | pending | binding_energy | — | 1033.6000 | — | — |
| ${}^{129}$Pm | 129 | 68 | L?-pending | pending | binding_energy | — | 1046.7060 | — | — |
| ${}^{130}$Pm | 130 | 69 | L?-pending | pending | binding_energy | — | 1057.0300 | — | — |
| ${}^{131}$Pm | 131 | 70 | L?-pending | pending | binding_energy | — | 1069.3530 | — | — |
| ${}^{132}$Pm | 132 | 71 | L?-pending | pending | binding_energy | — | 1079.3640 | — | — |
| ${}^{133}$Pm | 133 | 72 | L?-pending | pending | binding_energy | — | 1091.1698 | — | — |
| ${}^{134}$Pm | 134 | 73 | L?-pending | pending | binding_energy | — | 1100.5974 | — | — |
| ${}^{135}$Pm | 135 | 74 | L?-pending | pending | binding_energy | — | 1111.9671 | — | — |
| ${}^{136}$Pm | 136 | 75 | L?-pending | pending | binding_energy | — | 1121.1460 | — | — |
| ${}^{137}$Pm | 137 | 76 | L?-pending | pending | binding_energy | — | 1132.1203 | — | — |
| ${}^{138}$Pm | 138 | 77 | L?-pending | pending | binding_energy | — | 1141.0331 | — | — |
| ${}^{139}$Pm | 139 | 78 | L?-pending | pending | binding_energy | — | 1151.6911 | — | — |
| ${}^{140}$Pm | 140 | 79 | L?-pending | pending | binding_energy | — | 1160.4734 | — | — |
| ${}^{141}$Pm | 141 | 80 | L?-pending | pending | binding_energy | — | 1170.8556 | — | — |
| ${}^{142}$Pm | 142 | 81 | L?-pending | pending | binding_energy | — | 1179.5455 | — | — |
| ${}^{143}$Pm | 143 | 82 | L?-pending | pending | binding_energy | — | 1189.4360 | — | — |
| ${}^{144}$Pm | 144 | 83 | L?-pending | pending | binding_energy | — | 1195.9628 | — | — |
| ${}^{145}$Pm | 145 | 84 | L?-pending | pending | binding_energy | — | 1203.8855 | — | — |
| ${}^{146}$Pm | 146 | 85 | L?-pending | pending | binding_energy | — | 1210.1436 | — | — |
| ${}^{147}$Pm | 147 | 86 | L?-pending | pending | binding_energy | — | 1217.8026 | — | — |
| ${}^{148}$Pm | 148 | 87 | L?-pending | pending | binding_energy | — | 1223.6978 | — | — |
| ${}^{149}$Pm | 149 | 88 | L?-pending | pending | binding_energy | — | 1230.9676 | — | — |
| ${}^{150}$Pm | 150 | 89 | L?-pending | pending | binding_energy | — | 1236.5719 | — | — |
| ${}^{151}$Pm | 151 | 90 | L?-pending | pending | binding_energy | — | 1244.4321 | — | — |
| ${}^{152}$Pm | 152 | 91 | L?-pending | pending | binding_energy | — | 1250.3717 | — | — |
| ${}^{153}$Pm | 153 | 92 | L?-pending | pending | binding_energy | — | 1257.8365 | — | — |
| ${}^{154}$Pm | 154 | 93 | L?-pending | pending | binding_energy | — | 1263.5264 | — | — |
| ${}^{155}$Pm | 155 | 94 | L?-pending | pending | binding_energy | — | 1270.2711 | — | — |
| ${}^{156}$Pm | 156 | 95 | L?-pending | pending | binding_energy | — | 1275.5693 | — | — |
| ${}^{157}$Pm | 157 | 96 | L?-pending | pending | binding_energy | — | 1281.7709 | — | — |
| ${}^{158}$Pm | 158 | 97 | L?-pending | pending | binding_energy | — | 1286.6512 | — | — |
| ${}^{159}$Pm | 159 | 98 | L?-pending | pending | binding_energy | — | 1292.1708 | — | — |
| ${}^{160}$Pm | 160 | 99 | L?-pending | pending | binding_energy | — | 1296.5824 | — | — |
| ${}^{161}$Pm | 161 | 100 | L?-pending | pending | binding_energy | — | 1301.8456 | — | — |
| ${}^{162}$Pm | 162 | 101 | L?-pending | pending | binding_energy | — | 1305.8820 | — | — |
| ${}^{163}$Pm | 163 | 102 | L?-pending | pending | binding_energy | — | 1310.8460 | — | — |
| ${}^{164}$Pm | 164 | 103 | L?-pending | pending | binding_energy | — | 1314.2960 | — | — |
| ${}^{165}$Pm | 165 | 104 | L?-pending | pending | binding_energy | — | 1318.6800 | — | — |

### Samarium (Z = 62)

_0 of 41 isotopes with a framework prediction; 0 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{128}$Sm | 128 | 66 | L?-pending | pending | binding_energy | — | 1023.7440 | — | — |
| ${}^{129}$Sm | 129 | 67 | L?-pending | pending | binding_energy | — | 1034.9670 | — | — |
| ${}^{130}$Sm | 130 | 68 | L?-pending | pending | binding_energy | — | 1048.4500 | — | — |
| ${}^{131}$Sm | 131 | 69 | L?-pending | pending | binding_energy | — | 1059.1350 | — | — |
| ${}^{132}$Sm | 132 | 70 | L?-pending | pending | binding_energy | — | 1072.1040 | — | — |
| ${}^{133}$Sm | 133 | 71 | L?-pending | pending | binding_energy | — | 1082.2210 | — | — |
| ${}^{134}$Sm | 134 | 72 | L?-pending | pending | binding_energy | — | 1094.3780 | — | — |
| ${}^{135}$Sm | 135 | 73 | L?-pending | pending | binding_energy | — | 1103.9796 | — | — |
| ${}^{136}$Sm | 136 | 74 | L?-pending | pending | binding_energy | — | 1116.0046 | — | — |
| ${}^{137}$Sm | 137 | 75 | L?-pending | pending | binding_energy | — | 1125.2567 | — | — |
| ${}^{138}$Sm | 138 | 76 | L?-pending | pending | binding_energy | — | 1136.8341 | — | — |
| ${}^{139}$Sm | 139 | 77 | L?-pending | pending | binding_energy | — | 1145.7879 | — | — |
| ${}^{140}$Sm | 140 | 78 | L?-pending | pending | binding_energy | — | 1156.9350 | — | — |
| ${}^{141}$Sm | 141 | 79 | L?-pending | pending | binding_energy | — | 1165.4843 | — | — |
| ${}^{142}$Sm | 142 | 80 | L?-pending | pending | binding_energy | — | 1176.6036 | — | — |
| ${}^{143}$Sm | 143 | 81 | L?-pending | pending | binding_energy | — | 1185.2101 | — | — |
| ${}^{144}$Sm | 144 | 82 | L?-pending | pending | binding_energy | — | 1195.7299 | — | — |
| ${}^{145}$Sm | 145 | 83 | L?-pending | pending | binding_energy | — | 1202.4870 | — | — |
| ${}^{146}$Sm | 146 | 84 | L?-pending | pending | binding_energy | — | 1210.9033 | — | — |
| ${}^{147}$Sm | 147 | 85 | L?-pending | pending | binding_energy | — | 1217.2443 | — | — |
| ${}^{148}$Sm | 148 | 86 | L?-pending | pending | binding_energy | — | 1225.3856 | — | — |
| ${}^{149}$Sm | 149 | 87 | L?-pending | pending | binding_energy | — | 1231.2568 | — | — |
| ${}^{150}$Sm | 150 | 88 | L?-pending | pending | binding_energy | — | 1239.2435 | — | — |
| ${}^{151}$Sm | 151 | 89 | L?-pending | pending | binding_energy | — | 1244.8400 | — | — |
| ${}^{152}$Sm | 152 | 90 | L?-pending | pending | binding_energy | — | 1253.0978 | — | — |
| ${}^{153}$Sm | 153 | 91 | L?-pending | pending | binding_energy | — | 1258.9662 | — | — |
| ${}^{154}$Sm | 154 | 92 | L?-pending | pending | binding_energy | — | 1266.9330 | — | — |
| ${}^{155}$Sm | 155 | 93 | L?-pending | pending | binding_energy | — | 1272.7400 | — | — |
| ${}^{156}$Sm | 156 | 94 | L?-pending | pending | binding_energy | — | 1279.9808 | — | — |
| ${}^{157}$Sm | 157 | 95 | L?-pending | pending | binding_energy | — | 1285.3691 | — | — |
| ${}^{158}$Sm | 158 | 96 | L?-pending | pending | binding_energy | — | 1292.0146 | — | — |
| ${}^{159}$Sm | 159 | 97 | L?-pending | pending | binding_energy | — | 1297.0419 | — | — |
| ${}^{160}$Sm | 160 | 98 | L?-pending | pending | binding_energy | — | 1303.1385 | — | — |
| ${}^{161}$Sm | 161 | 99 | L?-pending | pending | binding_energy | — | 1307.6487 | — | — |
| ${}^{162}$Sm | 162 | 100 | L?-pending | pending | binding_energy | — | 1313.4271 | — | — |
| ${}^{163}$Sm | 163 | 101 | L?-pending | pending | binding_energy | — | 1317.7189 | — | — |
| ${}^{164}$Sm | 164 | 102 | L?-pending | pending | binding_energy | — | 1323.1160 | — | — |
| ${}^{165}$Sm | 165 | 103 | L?-pending | pending | binding_energy | — | 1326.7650 | — | — |
| ${}^{166}$Sm | 166 | 104 | L?-pending | pending | binding_energy | — | 1331.8180 | — | — |
| ${}^{167}$Sm | 167 | 105 | L?-pending | pending | binding_energy | — | 1334.6640 | — | — |
| ${}^{168}$Sm | 168 | 106 | L?-pending | pending | binding_energy | — | 1339.1280 | — | — |

### Europium (Z = 63)

_0 of 41 isotopes with a framework prediction; 0 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{130}$Eu | 130 | 67 | L?-pending | pending | binding_energy | — | 1033.5000 | — | — |
| ${}^{131}$Eu | 131 | 68 | L?-pending | pending | binding_energy | — | 1047.4760 | — | — |
| ${}^{132}$Eu | 132 | 69 | L?-pending | pending | binding_energy | — | 1058.3760 | — | — |
| ${}^{133}$Eu | 133 | 70 | L?-pending | pending | binding_energy | — | 1071.4480 | — | — |
| ${}^{134}$Eu | 134 | 71 | L?-pending | pending | binding_energy | — | 1082.0500 | — | — |
| ${}^{135}$Eu | 135 | 72 | L?-pending | pending | binding_energy | — | 1094.4450 | — | — |
| ${}^{136}$Eu | 136 | 73 | L?-pending | pending | binding_energy | — | 1104.5920 | — | — |
| ${}^{137}$Eu | 137 | 74 | L?-pending | pending | binding_energy | — | 1116.6286 | — | — |
| ${}^{138}$Eu | 138 | 75 | L?-pending | pending | binding_energy | — | 1126.3037 | — | — |
| ${}^{139}$Eu | 139 | 76 | L?-pending | pending | binding_energy | — | 1138.0234 | — | — |
| ${}^{140}$Eu | 140 | 77 | L?-pending | pending | binding_energy | — | 1147.6826 | — | — |
| ${}^{141}$Eu | 141 | 78 | L?-pending | pending | binding_energy | — | 1158.6936 | — | — |
| ${}^{142}$Eu | 142 | 79 | L?-pending | pending | binding_energy | — | 1168.1482 | — | — |
| ${}^{143}$Eu | 143 | 80 | L?-pending | pending | binding_energy | — | 1179.1519 | — | — |
| ${}^{144}$Eu | 144 | 81 | L?-pending | pending | binding_energy | — | 1188.6011 | — | — |
| ${}^{145}$Eu | 145 | 82 | L?-pending | pending | binding_energy | — | 1199.0448 | — | — |
| ${}^{146}$Eu | 146 | 83 | L?-pending | pending | binding_energy | — | 1206.2422 | — | — |
| ${}^{147}$Eu | 147 | 84 | L?-pending | pending | binding_energy | — | 1214.7405 | — | — |
| ${}^{148}$Eu | 148 | 85 | L?-pending | pending | binding_energy | — | 1221.5647 | — | — |
| ${}^{149}$Eu | 149 | 86 | L?-pending | pending | binding_energy | — | 1229.7798 | — | — |
| ${}^{150}$Eu | 150 | 87 | L?-pending | pending | binding_energy | — | 1236.2022 | — | — |
| ${}^{151}$Eu | 151 | 88 | L?-pending | pending | binding_energy | — | 1244.1343 | — | — |
| ${}^{152}$Eu | 152 | 89 | L?-pending | pending | binding_energy | — | 1250.4410 | — | — |
| ${}^{153}$Eu | 153 | 90 | L?-pending | pending | binding_energy | — | 1258.9913 | — | — |
| ${}^{154}$Eu | 154 | 91 | L?-pending | pending | binding_energy | — | 1265.4335 | — | — |
| ${}^{155}$Eu | 155 | 92 | L?-pending | pending | binding_energy | — | 1273.5848 | — | — |
| ${}^{156}$Eu | 156 | 93 | L?-pending | pending | binding_energy | — | 1279.9206 | — | — |
| ${}^{157}$Eu | 157 | 94 | L?-pending | pending | binding_energy | — | 1287.3682 | — | — |
| ${}^{158}$Eu | 158 | 95 | L?-pending | pending | binding_energy | — | 1293.2509 | — | — |
| ${}^{159}$Eu | 159 | 96 | L?-pending | pending | binding_energy | — | 1300.0951 | — | — |
| ${}^{160}$Eu | 160 | 97 | L?-pending | pending | binding_energy | — | 1305.6165 | — | — |
| ${}^{161}$Eu | 161 | 98 | L?-pending | pending | binding_energy | — | 1311.9859 | — | — |
| ${}^{162}$Eu | 162 | 99 | L?-pending | pending | binding_energy | — | 1316.9886 | — | — |
| ${}^{163}$Eu | 163 | 100 | L?-pending | pending | binding_energy | — | 1322.9108 | — | — |
| ${}^{164}$Eu | 164 | 101 | L?-pending | pending | binding_energy | — | 1327.6405 | — | — |
| ${}^{165}$Eu | 165 | 102 | L?-pending | pending | binding_energy | — | 1333.2087 | — | — |
| ${}^{166}$Eu | 166 | 103 | L?-pending | pending | binding_energy | — | 1337.2960 | — | — |
| ${}^{167}$Eu | 167 | 104 | L?-pending | pending | binding_energy | — | 1342.3460 | — | — |
| ${}^{168}$Eu | 168 | 105 | L?-pending | pending | binding_energy | — | 1346.0160 | — | — |
| ${}^{169}$Eu | 169 | 106 | L?-pending | pending | binding_energy | — | 1350.4790 | — | — |
| ${}^{170}$Eu | 170 | 107 | L?-pending | pending | binding_energy | — | 1353.7100 | — | — |

### Gadolinium (Z = 64)

_0 of 40 isotopes with a framework prediction; 0 of 40 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{133}$Gd | 133 | 69 | L?-pending | pending | binding_energy | — | 1059.4780 | — | — |
| ${}^{134}$Gd | 134 | 70 | L?-pending | pending | binding_energy | — | 1073.0720 | — | — |
| ${}^{135}$Gd | 135 | 71 | L?-pending | pending | binding_energy | — | 1083.7800 | — | — |
| ${}^{136}$Gd | 136 | 72 | L?-pending | pending | binding_energy | — | 1096.7040 | — | — |
| ${}^{137}$Gd | 137 | 73 | L?-pending | pending | binding_energy | — | 1106.9600 | — | — |
| ${}^{138}$Gd | 138 | 74 | L?-pending | pending | binding_energy | — | 1119.4560 | — | — |
| ${}^{139}$Gd | 139 | 75 | L?-pending | pending | binding_energy | — | 1129.5140 | — | — |
| ${}^{140}$Gd | 140 | 76 | L?-pending | pending | binding_energy | — | 1141.6966 | — | — |
| ${}^{141}$Gd | 141 | 77 | L?-pending | pending | binding_energy | — | 1151.2099 | — | — |
| ${}^{142}$Gd | 142 | 78 | L?-pending | pending | binding_energy | — | 1163.0165 | — | — |
| ${}^{143}$Gd | 143 | 79 | L?-pending | pending | binding_energy | — | 1172.3596 | — | — |
| ${}^{144}$Gd | 144 | 80 | L?-pending | pending | binding_energy | — | 1183.9591 | — | — |
| ${}^{145}$Gd | 145 | 81 | L?-pending | pending | binding_energy | — | 1193.1975 | — | — |
| ${}^{146}$Gd | 146 | 82 | L?-pending | pending | binding_energy | — | 1204.4281 | — | — |
| ${}^{147}$Gd | 147 | 83 | L?-pending | pending | binding_energy | — | 1211.7705 | — | — |
| ${}^{148}$Gd | 148 | 84 | L?-pending | pending | binding_energy | — | 1220.7543 | — | — |
| ${}^{149}$Gd | 149 | 85 | L?-pending | pending | binding_energy | — | 1227.6834 | — | — |
| ${}^{150}$Gd | 150 | 86 | L?-pending | pending | binding_energy | — | 1236.3915 | — | — |
| ${}^{151}$Gd | 151 | 87 | L?-pending | pending | binding_energy | — | 1242.8877 | — | — |
| ${}^{152}$Gd | 152 | 88 | L?-pending | pending | binding_energy | — | 1251.4774 | — | — |
| ${}^{153}$Gd | 153 | 89 | L?-pending | pending | binding_energy | — | 1257.7244 | — | — |
| ${}^{154}$Gd | 154 | 90 | L?-pending | pending | binding_energy | — | 1266.6191 | — | — |
| ${}^{155}$Gd | 155 | 91 | L?-pending | pending | binding_energy | — | 1273.0544 | — | — |
| ${}^{156}$Gd | 156 | 92 | L?-pending | pending | binding_energy | — | 1281.5907 | — | — |
| ${}^{157}$Gd | 157 | 93 | L?-pending | pending | binding_energy | — | 1287.9506 | — | — |
| ${}^{158}$Gd | 158 | 94 | L?-pending | pending | binding_energy | — | 1295.8880 | — | — |
| ${}^{159}$Gd | 159 | 95 | L?-pending | pending | binding_energy | — | 1301.8312 | — | — |
| ${}^{160}$Gd | 160 | 96 | L?-pending | pending | binding_energy | — | 1309.2827 | — | — |
| ${}^{161}$Gd | 161 | 97 | L?-pending | pending | binding_energy | — | 1314.9181 | — | — |
| ${}^{162}$Gd | 162 | 98 | L?-pending | pending | binding_energy | — | 1321.7640 | — | — |
| ${}^{163}$Gd | 163 | 99 | L?-pending | pending | binding_energy | — | 1326.9432 | — | — |
| ${}^{164}$Gd | 164 | 100 | L?-pending | pending | binding_energy | — | 1333.3196 | — | — |
| ${}^{165}$Gd | 165 | 101 | L?-pending | pending | binding_energy | — | 1338.2231 | — | — |
| ${}^{166}$Gd | 166 | 102 | L?-pending | pending | binding_energy | — | 1344.1395 | — | — |
| ${}^{167}$Gd | 167 | 103 | L?-pending | pending | binding_energy | — | 1348.6156 | — | — |
| ${}^{168}$Gd | 168 | 104 | L?-pending | pending | binding_energy | — | 1354.0800 | — | — |
| ${}^{169}$Gd | 169 | 105 | L?-pending | pending | binding_energy | — | 1357.9150 | — | — |
| ${}^{170}$Gd | 170 | 106 | L?-pending | pending | binding_energy | — | 1362.8900 | — | — |
| ${}^{171}$Gd | 171 | 107 | L?-pending | pending | binding_energy | — | 1366.2900 | — | — |
| ${}^{172}$Gd | 172 | 108 | L?-pending | pending | binding_energy | — | 1371.1840 | — | — |

### Terbium (Z = 65)

_0 of 40 isotopes with a framework prediction; 0 of 40 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{135}$Tb | 135 | 70 | L?-pending | pending | binding_energy | — | 1071.7650 | — | — |
| ${}^{136}$Tb | 136 | 71 | L?-pending | pending | binding_energy | — | 1082.6960 | — | — |
| ${}^{137}$Tb | 137 | 72 | L?-pending | pending | binding_energy | — | 1095.8630 | — | — |
| ${}^{138}$Tb | 138 | 73 | L?-pending | pending | binding_energy | — | 1106.6220 | — | — |
| ${}^{139}$Tb | 139 | 74 | L?-pending | pending | binding_energy | — | 1119.2280 | — | — |
| ${}^{140}$Tb | 140 | 75 | L?-pending | pending | binding_energy | — | 1129.6142 | — | — |
| ${}^{141}$Tb | 141 | 76 | L?-pending | pending | binding_energy | — | 1141.7441 | — | — |
| ${}^{142}$Tb | 142 | 77 | L?-pending | pending | binding_energy | — | 1151.8341 | — | — |
| ${}^{143}$Tb | 143 | 78 | L?-pending | pending | binding_energy | — | 1163.7651 | — | — |
| ${}^{144}$Tb | 144 | 79 | L?-pending | pending | binding_energy | — | 1173.7854 | — | — |
| ${}^{145}$Tb | 145 | 80 | L?-pending | pending | binding_energy | — | 1185.8883 | — | — |
| ${}^{146}$Tb | 146 | 81 | L?-pending | pending | binding_energy | — | 1195.3235 | — | — |
| ${}^{147}$Tb | 147 | 82 | L?-pending | pending | binding_energy | — | 1206.3739 | — | — |
| ${}^{148}$Tb | 148 | 83 | L?-pending | pending | binding_energy | — | 1214.2395 | — | — |
| ${}^{149}$Tb | 149 | 84 | L?-pending | pending | binding_energy | — | 1223.2625 | — | — |
| ${}^{150}$Tb | 150 | 85 | L?-pending | pending | binding_energy | — | 1230.9509 | — | — |
| ${}^{151}$Tb | 151 | 86 | L?-pending | pending | binding_energy | — | 1239.5400 | — | — |
| ${}^{152}$Tb | 152 | 87 | L?-pending | pending | binding_energy | — | 1246.7051 | — | — |
| ${}^{153}$Tb | 153 | 88 | L?-pending | pending | binding_energy | — | 1255.3727 | — | — |
| ${}^{154}$Tb | 154 | 89 | L?-pending | pending | binding_energy | — | 1262.2871 | — | — |
| ${}^{155}$Tb | 155 | 90 | L?-pending | pending | binding_energy | — | 1271.4522 | — | — |
| ${}^{156}$Tb | 156 | 91 | L?-pending | pending | binding_energy | — | 1278.3641 | — | — |
| ${}^{157}$Tb | 157 | 92 | L?-pending | pending | binding_energy | — | 1287.1082 | — | — |
| ${}^{158}$Tb | 158 | 93 | L?-pending | pending | binding_energy | — | 1293.8866 | — | — |
| ${}^{159}$Tb | 159 | 94 | L?-pending | pending | binding_energy | — | 1302.0196 | — | — |
| ${}^{160}$Tb | 160 | 95 | L?-pending | pending | binding_energy | — | 1308.3948 | — | — |
| ${}^{161}$Tb | 161 | 96 | L?-pending | pending | binding_energy | — | 1316.0914 | — | — |
| ${}^{162}$Tb | 162 | 97 | L?-pending | pending | binding_energy | — | 1322.5805 | — | — |
| ${}^{163}$Tb | 163 | 98 | L?-pending | pending | binding_energy | — | 1329.3680 | — | — |
| ${}^{164}$Tb | 164 | 99 | L?-pending | pending | binding_energy | — | 1334.9486 | — | — |
| ${}^{165}$Tb | 165 | 100 | L?-pending | pending | binding_energy | — | 1341.5038 | — | — |
| ${}^{166}$Tb | 166 | 101 | L?-pending | pending | binding_energy | — | 1346.7950 | — | — |
| ${}^{167}$Tb | 167 | 102 | L?-pending | pending | binding_energy | — | 1352.9406 | — | — |
| ${}^{168}$Tb | 168 | 103 | L?-pending | pending | binding_energy | — | 1357.9101 | — | — |
| ${}^{169}$Tb | 169 | 104 | L?-pending | pending | binding_energy | — | 1363.6610 | — | — |
| ${}^{170}$Tb | 170 | 105 | L?-pending | pending | binding_energy | — | 1367.9900 | — | — |
| ${}^{171}$Tb | 171 | 106 | L?-pending | pending | binding_energy | — | 1373.1300 | — | — |
| ${}^{172}$Tb | 172 | 107 | L?-pending | pending | binding_energy | — | 1377.0320 | — | — |
| ${}^{173}$Tb | 173 | 108 | L?-pending | pending | binding_energy | — | 1381.9240 | — | — |
| ${}^{174}$Tb | 174 | 109 | L?-pending | pending | binding_energy | — | 1385.5620 | — | — |

### Dysprosium (Z = 66)

_0 of 39 isotopes with a framework prediction; 0 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{138}$Dy | 138 | 72 | L?-pending | pending | binding_energy | — | 1097.1000 | — | — |
| ${}^{139}$Dy | 139 | 73 | L?-pending | pending | binding_energy | — | 1107.9690 | — | — |
| ${}^{140}$Dy | 140 | 74 | L?-pending | pending | binding_energy | — | 1121.1200 | — | — |
| ${}^{141}$Dy | 141 | 75 | L?-pending | pending | binding_energy | — | 1131.8070 | — | — |
| ${}^{142}$Dy | 142 | 76 | L?-pending | pending | binding_energy | — | 1144.6620 | — | — |
| ${}^{143}$Dy | 143 | 77 | L?-pending | pending | binding_energy | — | 1154.7325 | — | — |
| ${}^{144}$Dy | 144 | 78 | L?-pending | pending | binding_energy | — | 1167.2050 | — | — |
| ${}^{145}$Dy | 145 | 79 | L?-pending | pending | binding_energy | — | 1176.9488 | — | — |
| ${}^{146}$Dy | 146 | 80 | L?-pending | pending | binding_energy | — | 1189.3325 | — | — |
| ${}^{147}$Dy | 147 | 81 | L?-pending | pending | binding_energy | — | 1199.0449 | — | — |
| ${}^{148}$Dy | 148 | 82 | L?-pending | pending | binding_energy | — | 1210.7796 | — | — |
| ${}^{149}$Dy | 149 | 83 | L?-pending | pending | binding_energy | — | 1218.6855 | — | — |
| ${}^{150}$Dy | 150 | 84 | L?-pending | pending | binding_energy | — | 1228.3724 | — | — |
| ${}^{151}$Dy | 151 | 85 | L?-pending | pending | binding_energy | — | 1235.8865 | — | — |
| ${}^{152}$Dy | 152 | 86 | L?-pending | pending | binding_energy | — | 1245.3234 | — | — |
| ${}^{153}$Dy | 153 | 87 | L?-pending | pending | binding_energy | — | 1252.4200 | — | — |
| ${}^{154}$Dy | 154 | 88 | L?-pending | pending | binding_energy | — | 1261.7421 | — | — |
| ${}^{155}$Dy | 155 | 89 | L?-pending | pending | binding_energy | — | 1268.5753 | — | — |
| ${}^{156}$Dy | 156 | 90 | L?-pending | pending | binding_energy | — | 1278.0201 | — | — |
| ${}^{157}$Dy | 157 | 91 | L?-pending | pending | binding_energy | — | 1284.9867 | — | — |
| ${}^{158}$Dy | 158 | 92 | L?-pending | pending | binding_energy | — | 1294.0405 | — | — |
| ${}^{159}$Dy | 159 | 93 | L?-pending | pending | binding_energy | — | 1300.8719 | — | — |
| ${}^{160}$Dy | 160 | 94 | L?-pending | pending | binding_energy | — | 1309.4484 | — | — |
| ${}^{161}$Dy | 161 | 95 | L?-pending | pending | binding_energy | — | 1315.9028 | — | — |
| ${}^{162}$Dy | 162 | 96 | L?-pending | pending | binding_energy | — | 1324.0998 | — | — |
| ${}^{163}$Dy | 163 | 97 | L?-pending | pending | binding_energy | — | 1330.3708 | — | — |
| ${}^{164}$Dy | 164 | 98 | L?-pending | pending | binding_energy | — | 1338.0289 | — | — |
| ${}^{165}$Dy | 165 | 99 | L?-pending | pending | binding_energy | — | 1343.7449 | — | — |
| ${}^{166}$Dy | 166 | 100 | L?-pending | pending | binding_energy | — | 1350.7884 | — | — |
| ${}^{167}$Dy | 167 | 101 | L?-pending | pending | binding_energy | — | 1356.1867 | — | — |
| ${}^{168}$Dy | 168 | 102 | L?-pending | pending | binding_energy | — | 1362.9049 | — | — |
| ${}^{169}$Dy | 169 | 103 | L?-pending | pending | binding_energy | — | 1368.0139 | — | — |
| ${}^{170}$Dy | 170 | 104 | L?-pending | pending | binding_energy | — | 1374.2800 | — | — |
| ${}^{171}$Dy | 171 | 105 | L?-pending | pending | binding_energy | — | 1378.6020 | — | — |
| ${}^{172}$Dy | 172 | 106 | L?-pending | pending | binding_energy | — | 1384.4280 | — | — |
| ${}^{173}$Dy | 173 | 107 | L?-pending | pending | binding_energy | — | 1388.4980 | — | — |
| ${}^{174}$Dy | 174 | 108 | L?-pending | pending | binding_energy | — | 1393.9140 | — | — |
| ${}^{175}$Dy | 175 | 109 | L?-pending | pending | binding_energy | — | 1397.5500 | — | — |
| ${}^{176}$Dy | 176 | 110 | L?-pending | pending | binding_energy | — | 1402.5440 | — | — |

### Holmium (Z = 67)

_0 of 39 isotopes with a framework prediction; 0 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{140}$Ho | 140 | 73 | L?-pending | pending | binding_energy | — | 1106.8400 | — | — |
| ${}^{141}$Ho | 141 | 74 | L?-pending | pending | binding_energy | — | 1119.9630 | — | — |
| ${}^{142}$Ho | 142 | 75 | L?-pending | pending | binding_energy | — | 1131.0300 | — | — |
| ${}^{143}$Ho | 143 | 76 | L?-pending | pending | binding_energy | — | 1143.8570 | — | — |
| ${}^{144}$Ho | 144 | 77 | L?-pending | pending | binding_energy | — | 1154.4621 | — | — |
| ${}^{145}$Ho | 145 | 78 | L?-pending | pending | binding_energy | — | 1167.0440 | — | — |
| ${}^{146}$Ho | 146 | 79 | L?-pending | pending | binding_energy | — | 1177.2334 | — | — |
| ${}^{147}$Ho | 147 | 80 | L?-pending | pending | binding_energy | — | 1189.8236 | — | — |
| ${}^{148}$Ho | 148 | 81 | L?-pending | pending | binding_energy | — | 1200.1290 | — | — |
| ${}^{149}$Ho | 149 | 82 | L?-pending | pending | binding_energy | — | 1211.8550 | — | — |
| ${}^{150}$Ho | 150 | 83 | L?-pending | pending | binding_energy | — | 1220.2263 | — | — |
| ${}^{151}$Ho | 151 | 84 | L?-pending | pending | binding_energy | — | 1229.9745 | — | — |
| ${}^{152}$Ho | 152 | 85 | L?-pending | pending | binding_energy | — | 1238.0277 | — | — |
| ${}^{153}$Ho | 153 | 86 | L?-pending | pending | binding_energy | — | 1247.5065 | — | — |
| ${}^{154}$Ho | 154 | 87 | L?-pending | pending | binding_energy | — | 1255.2051 | — | — |
| ${}^{155}$Ho | 155 | 88 | L?-pending | pending | binding_energy | — | 1264.6769 | — | — |
| ${}^{156}$Ho | 156 | 89 | L?-pending | pending | binding_energy | — | 1272.2468 | — | — |
| ${}^{157}$Ho | 157 | 90 | L?-pending | pending | binding_energy | — | 1281.6126 | — | — |
| ${}^{158}$Ho | 158 | 91 | L?-pending | pending | binding_energy | — | 1289.0384 | — | — |
| ${}^{159}$Ho | 159 | 92 | L?-pending | pending | binding_energy | — | 1298.2519 | — | — |
| ${}^{160}$Ho | 160 | 93 | L?-pending | pending | binding_energy | — | 1305.3761 | — | — |
| ${}^{161}$Ho | 161 | 94 | L?-pending | pending | binding_energy | — | 1314.2613 | — | — |
| ${}^{162}$Ho | 162 | 95 | L?-pending | pending | binding_energy | — | 1321.1768 | — | — |
| ${}^{163}$Ho | 163 | 96 | L?-pending | pending | binding_energy | — | 1329.5856 | — | — |
| ${}^{164}$Ho | 164 | 97 | L?-pending | pending | binding_energy | — | 1336.2594 | — | — |
| ${}^{165}$Ho | 165 | 98 | L?-pending | pending | binding_energy | — | 1344.2483 | — | — |
| ${}^{166}$Ho | 166 | 99 | L?-pending | pending | binding_energy | — | 1350.4919 | — | — |
| ${}^{167}$Ho | 167 | 100 | L?-pending | pending | binding_energy | — | 1357.7723 | — | — |
| ${}^{168}$Ho | 168 | 101 | L?-pending | pending | binding_energy | — | 1363.6234 | — | — |
| ${}^{169}$Ho | 169 | 102 | L?-pending | pending | binding_energy | — | 1370.4315 | — | — |
| ${}^{170}$Ho | 170 | 103 | L?-pending | pending | binding_energy | — | 1375.9443 | — | — |
| ${}^{171}$Ho | 171 | 104 | L?-pending | pending | binding_energy | — | 1382.2960 | — | — |
| ${}^{172}$Ho | 172 | 105 | L?-pending | pending | binding_energy | — | 1387.3520 | — | — |
| ${}^{173}$Ho | 173 | 106 | L?-pending | pending | binding_energy | — | 1393.3420 | — | — |
| ${}^{174}$Ho | 174 | 107 | L?-pending | pending | binding_energy | — | 1397.9160 | — | — |
| ${}^{175}$Ho | 175 | 108 | L?-pending | pending | binding_energy | — | 1403.3250 | — | — |
| ${}^{176}$Ho | 176 | 109 | L?-pending | pending | binding_energy | — | 1407.4720 | — | — |
| ${}^{177}$Ho | 177 | 110 | L?-pending | pending | binding_energy | — | 1412.4600 | — | — |
| ${}^{178}$Ho | 178 | 111 | L?-pending | pending | binding_energy | — | 1416.3460 | — | — |

### Erbium (Z = 68)

_0 of 39 isotopes with a framework prediction; 0 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{142}$Er | 142 | 74 | L?-pending | pending | binding_energy | — | 1120.8060 | — | — |
| ${}^{143}$Er | 143 | 75 | L?-pending | pending | binding_energy | — | 1132.1310 | — | — |
| ${}^{144}$Er | 144 | 76 | L?-pending | pending | binding_energy | — | 1145.6640 | — | — |
| ${}^{145}$Er | 145 | 77 | L?-pending | pending | binding_energy | — | 1156.3750 | — | — |
| ${}^{146}$Er | 146 | 78 | L?-pending | pending | binding_energy | — | 1169.5349 | — | — |
| ${}^{147}$Er | 147 | 79 | L?-pending | pending | binding_energy | — | 1179.8920 | — | — |
| ${}^{148}$Er | 148 | 80 | L?-pending | pending | binding_energy | — | 1192.8345 | — | — |
| ${}^{149}$Er | 149 | 81 | L?-pending | pending | binding_energy | — | 1203.1684 | — | — |
| ${}^{150}$Er | 150 | 82 | L?-pending | pending | binding_energy | — | 1215.3294 | — | — |
| ${}^{151}$Er | 151 | 83 | L?-pending | pending | binding_energy | — | 1223.8357 | — | — |
| ${}^{152}$Er | 152 | 84 | L?-pending | pending | binding_energy | — | 1234.1410 | — | — |
| ${}^{153}$Er | 153 | 85 | L?-pending | pending | binding_energy | — | 1242.1788 | — | — |
| ${}^{154}$Er | 154 | 86 | L?-pending | pending | binding_energy | — | 1252.3884 | — | — |
| ${}^{155}$Er | 155 | 87 | L?-pending | pending | binding_energy | — | 1260.0639 | — | — |
| ${}^{156}$Er | 156 | 88 | L?-pending | pending | binding_energy | — | 1270.1377 | — | — |
| ${}^{157}$Er | 157 | 89 | L?-pending | pending | binding_energy | — | 1277.4110 | — | — |
| ${}^{158}$Er | 158 | 90 | L?-pending | pending | binding_energy | — | 1287.3725 | — | — |
| ${}^{159}$Er | 159 | 91 | L?-pending | pending | binding_energy | — | 1294.7011 | — | — |
| ${}^{160}$Er | 160 | 92 | L?-pending | pending | binding_energy | — | 1304.2755 | — | — |
| ${}^{161}$Er | 161 | 93 | L?-pending | pending | binding_energy | — | 1311.4839 | — | — |
| ${}^{162}$Er | 162 | 94 | L?-pending | pending | binding_energy | — | 1320.6881 | — | — |
| ${}^{163}$Er | 163 | 95 | L?-pending | pending | binding_energy | — | 1327.5927 | — | — |
| ${}^{164}$Er | 164 | 96 | L?-pending | pending | binding_energy | — | 1336.4391 | — | — |
| ${}^{165}$Er | 165 | 97 | L?-pending | pending | binding_energy | — | 1343.0892 | — | — |
| ${}^{166}$Er | 166 | 98 | L?-pending | pending | binding_energy | — | 1351.5634 | — | — |
| ${}^{167}$Er | 167 | 99 | L?-pending | pending | binding_energy | — | 1357.9998 | — | — |
| ${}^{168}$Er | 168 | 100 | L?-pending | pending | binding_energy | — | 1365.7711 | — | — |
| ${}^{169}$Er | 169 | 101 | L?-pending | pending | binding_energy | — | 1371.7743 | — | — |
| ${}^{170}$Er | 170 | 102 | L?-pending | pending | binding_energy | — | 1379.0320 | — | — |
| ${}^{171}$Er | 171 | 103 | L?-pending | pending | binding_energy | — | 1384.7136 | — | — |
| ${}^{172}$Er | 172 | 104 | L?-pending | pending | binding_energy | — | 1391.5497 | — | — |
| ${}^{173}$Er | 173 | 105 | L?-pending | pending | binding_energy | — | 1396.8020 | — | — |
| ${}^{174}$Er | 174 | 106 | L?-pending | pending | binding_energy | — | 1403.1360 | — | — |
| ${}^{175}$Er | 175 | 107 | L?-pending | pending | binding_energy | — | 1407.8750 | — | — |
| ${}^{176}$Er | 176 | 108 | L?-pending | pending | binding_energy | — | 1413.9840 | — | — |
| ${}^{177}$Er | 177 | 109 | L?-pending | pending | binding_energy | — | 1418.3010 | — | — |
| ${}^{178}$Er | 178 | 110 | L?-pending | pending | binding_energy | — | 1423.8220 | — | — |
| ${}^{179}$Er | 179 | 111 | L?-pending | pending | binding_energy | — | 1427.7040 | — | — |
| ${}^{180}$Er | 180 | 112 | L?-pending | pending | binding_energy | — | 1432.8000 | — | — |

### Thulium (Z = 69)

_0 of 39 isotopes with a framework prediction; 0 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{144}$Tm | 144 | 75 | L?-pending | pending | binding_energy | — | 1130.4000 | — | — |
| ${}^{145}$Tm | 145 | 76 | L?-pending | pending | binding_energy | — | 1143.9050 | — | — |
| ${}^{146}$Tm | 146 | 77 | L?-pending | pending | binding_energy | — | 1155.4440 | — | — |
| ${}^{147}$Tm | 147 | 78 | L?-pending | pending | binding_energy | — | 1168.4762 | — | — |
| ${}^{148}$Tm | 148 | 79 | L?-pending | pending | binding_energy | — | 1179.3382 | — | — |
| ${}^{149}$Tm | 149 | 80 | L?-pending | pending | binding_energy | — | 1192.5960 | — | — |
| ${}^{150}$Tm | 150 | 81 | L?-pending | pending | binding_energy | — | 1203.1500 | — | — |
| ${}^{151}$Tm | 151 | 82 | L?-pending | pending | binding_energy | — | 1215.5587 | — | — |
| ${}^{152}$Tm | 152 | 83 | L?-pending | pending | binding_energy | — | 1224.5787 | — | — |
| ${}^{153}$Tm | 153 | 84 | L?-pending | pending | binding_energy | — | 1234.9023 | — | — |
| ${}^{154}$Tm | 154 | 85 | L?-pending | pending | binding_energy | — | 1243.4282 | — | — |
| ${}^{155}$Tm | 155 | 86 | L?-pending | pending | binding_energy | — | 1253.6983 | — | — |
| ${}^{156}$Tm | 156 | 87 | L?-pending | pending | binding_energy | — | 1261.9781 | — | — |
| ${}^{157}$Tm | 157 | 88 | L?-pending | pending | binding_energy | — | 1271.9243 | — | — |
| ${}^{158}$Tm | 158 | 89 | L?-pending | pending | binding_energy | — | 1279.9895 | — | — |
| ${}^{159}$Tm | 159 | 90 | L?-pending | pending | binding_energy | — | 1289.9280 | — | — |
| ${}^{160}$Tm | 160 | 91 | L?-pending | pending | binding_energy | — | 1297.7300 | — | — |
| ${}^{161}$Tm | 161 | 92 | L?-pending | pending | binding_energy | — | 1307.3990 | — | — |
| ${}^{162}$Tm | 162 | 93 | L?-pending | pending | binding_energy | — | 1315.0491 | — | — |
| ${}^{163}$Tm | 163 | 94 | L?-pending | pending | binding_energy | — | 1324.3713 | — | — |
| ${}^{164}$Tm | 164 | 95 | L?-pending | pending | binding_energy | — | 1331.6232 | — | — |
| ${}^{165}$Tm | 165 | 96 | L?-pending | pending | binding_energy | — | 1340.7156 | — | — |
| ${}^{166}$Tm | 166 | 97 | L?-pending | pending | binding_energy | — | 1347.7433 | — | — |
| ${}^{167}$Tm | 167 | 98 | L?-pending | pending | binding_energy | — | 1356.4713 | — | — |
| ${}^{168}$Tm | 168 | 99 | L?-pending | pending | binding_energy | — | 1363.3119 | — | — |
| ${}^{169}$Tm | 169 | 100 | L?-pending | pending | binding_energy | — | 1371.3455 | — | — |
| ${}^{170}$Tm | 170 | 101 | L?-pending | pending | binding_energy | — | 1377.9374 | — | — |
| ${}^{171}$Tm | 171 | 102 | L?-pending | pending | binding_energy | — | 1385.4237 | — | — |
| ${}^{172}$Tm | 172 | 103 | L?-pending | pending | binding_energy | — | 1391.6583 | — | — |
| ${}^{173}$Tm | 173 | 104 | L?-pending | pending | binding_energy | — | 1398.6122 | — | — |
| ${}^{174}$Tm | 174 | 105 | L?-pending | pending | binding_energy | — | 1404.2919 | — | — |
| ${}^{175}$Tm | 175 | 106 | L?-pending | pending | binding_energy | — | 1410.8093 | — | — |
| ${}^{176}$Tm | 176 | 107 | L?-pending | pending | binding_energy | — | 1415.9414 | — | — |
| ${}^{177}$Tm | 177 | 108 | L?-pending | pending | binding_energy | — | 1422.1950 | — | — |
| ${}^{178}$Tm | 178 | 109 | L?-pending | pending | binding_energy | — | 1427.0260 | — | — |
| ${}^{179}$Tm | 179 | 110 | L?-pending | pending | binding_energy | — | 1432.7160 | — | — |
| ${}^{180}$Tm | 180 | 111 | L?-pending | pending | binding_energy | — | 1436.9400 | — | — |
| ${}^{181}$Tm | 181 | 112 | L?-pending | pending | binding_energy | — | 1442.3890 | — | — |
| ${}^{182}$Tm | 182 | 113 | L?-pending | pending | binding_energy | — | 1446.5360 | — | — |

### Ytterbium (Z = 70)

_0 of 38 isotopes with a framework prediction; 0 of 38 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{148}$Yb | 148 | 78 | L?-pending | pending | binding_energy | — | 1170.0880 | — | — |
| ${}^{149}$Yb | 149 | 79 | L?-pending | pending | binding_energy | — | 1181.1230 | — | — |
| ${}^{150}$Yb | 150 | 80 | L?-pending | pending | binding_energy | — | 1194.7500 | — | — |
| ${}^{151}$Yb | 151 | 81 | L?-pending | pending | binding_energy | — | 1205.5471 | — | — |
| ${}^{152}$Yb | 152 | 82 | L?-pending | pending | binding_energy | — | 1218.3464 | — | — |
| ${}^{153}$Yb | 153 | 83 | L?-pending | pending | binding_energy | — | 1227.3660 | — | — |
| ${}^{154}$Yb | 154 | 84 | L?-pending | pending | binding_energy | — | 1238.1508 | — | — |
| ${}^{155}$Yb | 155 | 85 | L?-pending | pending | binding_energy | — | 1246.7926 | — | — |
| ${}^{156}$Yb | 156 | 86 | L?-pending | pending | binding_energy | — | 1257.6269 | — | — |
| ${}^{157}$Yb | 157 | 87 | L?-pending | pending | binding_energy | — | 1265.8526 | — | — |
| ${}^{158}$Yb | 158 | 88 | L?-pending | pending | binding_energy | — | 1276.5136 | — | — |
| ${}^{159}$Yb | 159 | 89 | L?-pending | pending | binding_energy | — | 1284.4088 | — | — |
| ${}^{160}$Yb | 160 | 90 | L?-pending | pending | binding_energy | — | 1294.8098 | — | — |
| ${}^{161}$Yb | 161 | 91 | L?-pending | pending | binding_energy | — | 1302.5522 | — | — |
| ${}^{162}$Yb | 162 | 92 | L?-pending | pending | binding_energy | — | 1312.6104 | — | — |
| ${}^{163}$Yb | 163 | 93 | L?-pending | pending | binding_energy | — | 1320.1544 | — | — |
| ${}^{164}$Yb | 164 | 94 | L?-pending | pending | binding_energy | — | 1329.9440 | — | — |
| ${}^{165}$Yb | 165 | 95 | L?-pending | pending | binding_energy | — | 1337.2986 | — | — |
| ${}^{166}$Yb | 166 | 96 | L?-pending | pending | binding_energy | — | 1346.6682 | — | — |
| ${}^{167}$Yb | 167 | 97 | L?-pending | pending | binding_energy | — | 1353.7357 | — | — |
| ${}^{168}$Yb | 168 | 98 | L?-pending | pending | binding_energy | — | 1362.7970 | — | — |
| ${}^{169}$Yb | 169 | 99 | L?-pending | pending | binding_energy | — | 1369.6640 | — | — |
| ${}^{170}$Yb | 170 | 100 | L?-pending | pending | binding_energy | — | 1378.1237 | — | — |
| ${}^{171}$Yb | 171 | 101 | L?-pending | pending | binding_energy | — | 1384.7379 | — | — |
| ${}^{172}$Yb | 172 | 102 | L?-pending | pending | binding_energy | — | 1392.7579 | — | — |
| ${}^{173}$Yb | 173 | 103 | L?-pending | pending | binding_energy | — | 1399.1250 | — | — |
| ${}^{174}$Yb | 174 | 104 | L?-pending | pending | binding_energy | — | 1406.5896 | — | — |
| ${}^{175}$Yb | 175 | 105 | L?-pending | pending | binding_energy | — | 1412.4119 | — | — |
| ${}^{176}$Yb | 176 | 106 | L?-pending | pending | binding_energy | — | 1419.2790 | — | — |
| ${}^{177}$Yb | 177 | 107 | L?-pending | pending | binding_energy | — | 1424.8454 | — | — |
| ${}^{178}$Yb | 178 | 108 | L?-pending | pending | binding_energy | — | 1431.6075 | — | — |
| ${}^{179}$Yb | 179 | 109 | L?-pending | pending | binding_energy | — | 1436.6540 | — | — |
| ${}^{180}$Yb | 180 | 110 | L?-pending | pending | binding_energy | — | 1442.8800 | — | — |
| ${}^{181}$Yb | 181 | 111 | L?-pending | pending | binding_energy | — | 1447.2760 | — | — |
| ${}^{182}$Yb | 182 | 112 | L?-pending | pending | binding_energy | — | 1453.0880 | — | — |
| ${}^{183}$Yb | 183 | 113 | L?-pending | pending | binding_energy | — | 1457.2290 | — | — |
| ${}^{184}$Yb | 184 | 114 | L?-pending | pending | binding_energy | — | 1462.9840 | — | — |
| ${}^{185}$Yb | 185 | 115 | L?-pending | pending | binding_energy | — | 1466.8650 | — | — |

### Lutetium (Z = 71)

_0 of 39 isotopes with a framework prediction; 0 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{150}$Lu | 150 | 79 | L?-pending | pending | binding_energy | — | 1179.9000 | — | — |
| ${}^{151}$Lu | 151 | 80 | L?-pending | pending | binding_energy | — | 1193.5040 | — | — |
| ${}^{152}$Lu | 152 | 81 | L?-pending | pending | binding_energy | — | 1204.7520 | — | — |
| ${}^{153}$Lu | 153 | 82 | L?-pending | pending | binding_energy | — | 1217.7405 | — | — |
| ${}^{154}$Lu | 154 | 83 | L?-pending | pending | binding_energy | — | 1227.0720 | — | — |
| ${}^{155}$Lu | 155 | 84 | L?-pending | pending | binding_energy | — | 1238.0527 | — | — |
| ${}^{156}$Lu | 156 | 85 | L?-pending | pending | binding_energy | — | 1247.2785 | — | — |
| ${}^{157}$Lu | 157 | 86 | L?-pending | pending | binding_energy | — | 1258.0901 | — | — |
| ${}^{158}$Lu | 158 | 87 | L?-pending | pending | binding_energy | — | 1266.9338 | — | — |
| ${}^{159}$Lu | 159 | 88 | L?-pending | pending | binding_energy | — | 1277.5015 | — | — |
| ${}^{160}$Lu | 160 | 89 | L?-pending | pending | binding_energy | — | 1286.1342 | — | — |
| ${}^{161}$Lu | 161 | 90 | L?-pending | pending | binding_energy | — | 1296.4979 | — | — |
| ${}^{162}$Lu | 162 | 91 | L?-pending | pending | binding_energy | — | 1304.8387 | — | — |
| ${}^{163}$Lu | 163 | 92 | L?-pending | pending | binding_energy | — | 1314.8696 | — | — |
| ${}^{164}$Lu | 164 | 93 | L?-pending | pending | binding_energy | — | 1322.7919 | — | — |
| ${}^{165}$Lu | 165 | 94 | L?-pending | pending | binding_energy | — | 1332.6631 | — | — |
| ${}^{166}$Lu | 166 | 95 | L?-pending | pending | binding_energy | — | 1340.3131 | — | — |
| ${}^{167}$Lu | 167 | 96 | L?-pending | pending | binding_energy | — | 1349.8898 | — | — |
| ${}^{168}$Lu | 168 | 97 | L?-pending | pending | binding_energy | — | 1357.5076 | — | — |
| ${}^{169}$Lu | 169 | 98 | L?-pending | pending | binding_energy | — | 1366.5886 | — | — |
| ${}^{170}$Lu | 170 | 99 | L?-pending | pending | binding_energy | — | 1373.8837 | — | — |
| ${}^{171}$Lu | 171 | 100 | L?-pending | pending | binding_energy | — | 1382.4772 | — | — |
| ${}^{172}$Lu | 172 | 101 | L?-pending | pending | binding_energy | — | 1389.4561 | — | — |
| ${}^{173}$Lu | 173 | 102 | L?-pending | pending | binding_energy | — | 1397.6724 | — | — |
| ${}^{174}$Lu | 174 | 103 | L?-pending | pending | binding_energy | — | 1404.4330 | — | — |
| ${}^{175}$Lu | 175 | 104 | L?-pending | pending | binding_energy | — | 1412.0997 | — | — |
| ${}^{176}$Lu | 176 | 105 | L?-pending | pending | binding_energy | — | 1418.3877 | — | — |
| ${}^{177}$Lu | 177 | 106 | L?-pending | pending | binding_energy | — | 1425.4606 | — | — |
| ${}^{178}$Lu | 178 | 107 | L?-pending | pending | binding_energy | — | 1431.4859 | — | — |
| ${}^{179}$Lu | 179 | 108 | L?-pending | pending | binding_energy | — | 1438.2783 | — | — |
| ${}^{180}$Lu | 180 | 109 | L?-pending | pending | binding_energy | — | 1443.9671 | — | — |
| ${}^{181}$Lu | 181 | 110 | L?-pending | pending | binding_energy | — | 1450.1593 | — | — |
| ${}^{182}$Lu | 182 | 111 | L?-pending | pending | binding_energy | — | 1455.2720 | — | — |
| ${}^{183}$Lu | 183 | 112 | L?-pending | pending | binding_energy | — | 1461.2207 | — | — |
| ${}^{184}$Lu | 184 | 113 | L?-pending | pending | binding_energy | — | 1465.9280 | — | — |
| ${}^{185}$Lu | 185 | 114 | L?-pending | pending | binding_energy | — | 1471.6750 | — | — |
| ${}^{186}$Lu | 186 | 115 | L?-pending | pending | binding_energy | — | 1476.0960 | — | — |
| ${}^{187}$Lu | 187 | 116 | L?-pending | pending | binding_energy | — | 1481.6010 | — | — |
| ${}^{188}$Lu | 188 | 117 | L?-pending | pending | binding_energy | — | 1485.7640 | — | — |

### Hafnium (Z = 72)

_0 of 38 isotopes with a framework prediction; 0 of 38 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{153}$Hf | 153 | 81 | L?-pending | pending | binding_energy | — | 1205.9460 | — | — |
| ${}^{154}$Hf | 154 | 82 | L?-pending | pending | binding_energy | — | 1219.3720 | — | — |
| ${}^{155}$Hf | 155 | 83 | L?-pending | pending | binding_energy | — | 1228.9950 | — | — |
| ${}^{156}$Hf | 156 | 84 | L?-pending | pending | binding_energy | — | 1240.6161 | — | — |
| ${}^{157}$Hf | 157 | 85 | L?-pending | pending | binding_energy | — | 1249.7200 | — | — |
| ${}^{158}$Hf | 158 | 86 | L?-pending | pending | binding_energy | — | 1261.0417 | — | — |
| ${}^{159}$Hf | 159 | 87 | L?-pending | pending | binding_energy | — | 1269.8632 | — | — |
| ${}^{160}$Hf | 160 | 88 | L?-pending | pending | binding_energy | — | 1281.0207 | — | — |
| ${}^{161}$Hf | 161 | 89 | L?-pending | pending | binding_energy | — | 1289.4690 | — | — |
| ${}^{162}$Hf | 162 | 90 | L?-pending | pending | binding_energy | — | 1300.3930 | — | — |
| ${}^{163}$Hf | 163 | 91 | L?-pending | pending | binding_energy | — | 1308.5652 | — | — |
| ${}^{164}$Hf | 164 | 92 | L?-pending | pending | binding_energy | — | 1319.1855 | — | — |
| ${}^{165}$Hf | 165 | 93 | L?-pending | pending | binding_energy | — | 1327.0740 | — | — |
| ${}^{166}$Hf | 166 | 94 | L?-pending | pending | binding_energy | — | 1337.3688 | — | — |
| ${}^{167}$Hf | 167 | 95 | L?-pending | pending | binding_energy | — | 1345.0489 | — | — |
| ${}^{168}$Hf | 168 | 96 | L?-pending | pending | binding_energy | — | 1355.0130 | — | — |
| ${}^{169}$Hf | 169 | 97 | L?-pending | pending | binding_energy | — | 1362.4407 | — | — |
| ${}^{170}$Hf | 170 | 98 | L?-pending | pending | binding_energy | — | 1372.0490 | — | — |
| ${}^{171}$Hf | 171 | 99 | L?-pending | pending | binding_energy | — | 1379.2977 | — | — |
| ${}^{172}$Hf | 172 | 100 | L?-pending | pending | binding_energy | — | 1388.3400 | — | — |
| ${}^{173}$Hf | 173 | 101 | L?-pending | pending | binding_energy | — | 1395.4208 | — | — |
| ${}^{174}$Hf | 174 | 102 | L?-pending | pending | binding_energy | — | 1403.9249 | — | — |
| ${}^{175}$Hf | 175 | 103 | L?-pending | pending | binding_energy | — | 1410.6334 | — | — |
| ${}^{176}$Hf | 176 | 104 | L?-pending | pending | binding_energy | — | 1418.7994 | — | — |
| ${}^{177}$Hf | 177 | 105 | L?-pending | pending | binding_energy | — | 1425.1751 | — | — |
| ${}^{178}$Hf | 178 | 106 | L?-pending | pending | binding_energy | — | 1432.8010 | — | — |
| ${}^{179}$Hf | 179 | 107 | L?-pending | pending | binding_energy | — | 1438.9000 | — | — |
| ${}^{180}$Hf | 180 | 108 | L?-pending | pending | binding_energy | — | 1446.2877 | — | — |
| ${}^{181}$Hf | 181 | 109 | L?-pending | pending | binding_energy | — | 1451.9825 | — | — |
| ${}^{182}$Hf | 182 | 110 | L?-pending | pending | binding_energy | — | 1458.7005 | — | — |
| ${}^{183}$Hf | 183 | 111 | L?-pending | pending | binding_energy | — | 1464.0058 | — | — |
| ${}^{184}$Hf | 184 | 112 | L?-pending | pending | binding_energy | — | 1470.2930 | — | — |
| ${}^{185}$Hf | 185 | 113 | L?-pending | pending | binding_energy | — | 1475.1847 | — | — |
| ${}^{186}$Hf | 186 | 114 | L?-pending | pending | binding_energy | — | 1481.3604 | — | — |
| ${}^{187}$Hf | 187 | 115 | L?-pending | pending | binding_energy | — | 1486.0890 | — | — |
| ${}^{188}$Hf | 188 | 116 | L?-pending | pending | binding_energy | — | 1491.9680 | — | — |
| ${}^{189}$Hf | 189 | 117 | L?-pending | pending | binding_energy | — | 1496.3130 | — | — |
| ${}^{190}$Hf | 190 | 118 | L?-pending | pending | binding_energy | — | 1501.9500 | — | — |

### Tantalum (Z = 73)

_0 of 40 isotopes with a framework prediction; 0 of 40 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{155}$Ta | 155 | 82 | L?-pending | pending | binding_energy | — | 1217.9900 | — | — |
| ${}^{156}$Ta | 156 | 83 | L?-pending | pending | binding_energy | — | 1228.0320 | — | — |
| ${}^{157}$Ta | 157 | 84 | L?-pending | pending | binding_energy | — | 1239.6815 | — | — |
| ${}^{158}$Ta | 158 | 85 | L?-pending | pending | binding_energy | — | 1249.3060 | — | — |
| ${}^{159}$Ta | 159 | 86 | L?-pending | pending | binding_energy | — | 1260.6674 | — | — |
| ${}^{160}$Ta | 160 | 87 | L?-pending | pending | binding_energy | — | 1270.1233 | — | — |
| ${}^{161}$Ta | 161 | 88 | L?-pending | pending | binding_energy | — | 1281.1494 | — | — |
| ${}^{162}$Ta | 162 | 89 | L?-pending | pending | binding_energy | — | 1290.2236 | — | — |
| ${}^{163}$Ta | 163 | 90 | L?-pending | pending | binding_energy | — | 1301.0482 | — | — |
| ${}^{164}$Ta | 164 | 91 | L?-pending | pending | binding_energy | — | 1309.8676 | — | — |
| ${}^{165}$Ta | 165 | 92 | L?-pending | pending | binding_energy | — | 1320.5040 | — | — |
| ${}^{166}$Ta | 166 | 93 | L?-pending | pending | binding_energy | — | 1328.8253 | — | — |
| ${}^{167}$Ta | 167 | 94 | L?-pending | pending | binding_energy | — | 1339.1499 | — | — |
| ${}^{168}$Ta | 168 | 95 | L?-pending | pending | binding_energy | — | 1347.2640 | — | — |
| ${}^{169}$Ta | 169 | 96 | L?-pending | pending | binding_energy | — | 1357.2319 | — | — |
| ${}^{170}$Ta | 170 | 97 | L?-pending | pending | binding_energy | — | 1365.1504 | — | — |
| ${}^{171}$Ta | 171 | 98 | L?-pending | pending | binding_energy | — | 1374.8043 | — | — |
| ${}^{172}$Ta | 172 | 99 | L?-pending | pending | binding_energy | — | 1382.4854 | — | — |
| ${}^{173}$Ta | 173 | 100 | L?-pending | pending | binding_energy | — | 1391.6232 | — | — |
| ${}^{174}$Ta | 174 | 101 | L?-pending | pending | binding_energy | — | 1399.0388 | — | — |
| ${}^{175}$Ta | 175 | 102 | L?-pending | pending | binding_energy | — | 1407.7780 | — | — |
| ${}^{176}$Ta | 176 | 103 | L?-pending | pending | binding_energy | — | 1414.8060 | — | — |
| ${}^{177}$Ta | 177 | 104 | L?-pending | pending | binding_energy | — | 1423.2267 | — | — |
| ${}^{178}$Ta | 178 | 105 | L?-pending | pending | binding_energy | — | 1430.2300 | — | — |
| ${}^{179}$Ta | 179 | 106 | L?-pending | pending | binding_energy | — | 1438.0121 | — | — |
| ${}^{180}$Ta | 180 | 107 | L?-pending | pending | binding_energy | — | 1444.6596 | — | — |
| ${}^{181}$Ta | 181 | 108 | L?-pending | pending | binding_energy | — | 1452.2363 | — | — |
| ${}^{182}$Ta | 182 | 109 | L?-pending | pending | binding_energy | — | 1458.2992 | — | — |
| ${}^{183}$Ta | 183 | 110 | L?-pending | pending | binding_energy | — | 1465.2334 | — | — |
| ${}^{184}$Ta | 184 | 111 | L?-pending | pending | binding_energy | — | 1470.8506 | — | — |
| ${}^{185}$Ta | 185 | 112 | L?-pending | pending | binding_energy | — | 1477.4769 | — | — |
| ${}^{186}$Ta | 186 | 113 | L?-pending | pending | binding_energy | — | 1482.7614 | — | — |
| ${}^{187}$Ta | 187 | 114 | L?-pending | pending | binding_energy | — | 1489.1207 | — | — |
| ${}^{188}$Ta | 188 | 115 | L?-pending | pending | binding_energy | — | 1494.2240 | — | — |
| ${}^{189}$Ta | 189 | 116 | L?-pending | pending | binding_energy | — | 1500.2820 | — | — |
| ${}^{190}$Ta | 190 | 117 | L?-pending | pending | binding_energy | — | 1505.1800 | — | — |
| ${}^{191}$Ta | 191 | 118 | L?-pending | pending | binding_energy | — | 1511.0010 | — | — |
| ${}^{192}$Ta | 192 | 119 | L?-pending | pending | binding_energy | — | 1515.6480 | — | — |
| ${}^{193}$Ta | 193 | 120 | L?-pending | pending | binding_energy | — | 1521.4190 | — | — |
| ${}^{194}$Ta | 194 | 121 | L?-pending | pending | binding_energy | — | 1525.8100 | — | — |

### Tungsten (Z = 74)

_0 of 41 isotopes with a framework prediction; 0 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{157}$W | 157 | 83 | L?-pending | pending | binding_energy | — | 1228.9960 | — | — |
| ${}^{158}$W | 158 | 84 | L?-pending | pending | binding_energy | — | 1241.0900 | — | — |
| ${}^{159}$W | 159 | 85 | L?-pending | pending | binding_energy | — | 1250.8530 | — | — |
| ${}^{160}$W | 160 | 86 | L?-pending | pending | binding_energy | — | 1262.8463 | — | — |
| ${}^{161}$W | 161 | 87 | L?-pending | pending | binding_energy | — | 1272.0610 | — | — |
| ${}^{162}$W | 162 | 88 | L?-pending | pending | binding_energy | — | 1283.6591 | — | — |
| ${}^{163}$W | 163 | 89 | L?-pending | pending | binding_energy | — | 1292.6396 | — | — |
| ${}^{164}$W | 164 | 90 | L?-pending | pending | binding_energy | — | 1304.0380 | — | — |
| ${}^{165}$W | 165 | 91 | L?-pending | pending | binding_energy | — | 1312.7351 | — | — |
| ${}^{166}$W | 166 | 92 | L?-pending | pending | binding_energy | — | 1323.8326 | — | — |
| ${}^{167}$W | 167 | 93 | L?-pending | pending | binding_energy | — | 1332.1097 | — | — |
| ${}^{168}$W | 168 | 94 | L?-pending | pending | binding_energy | — | 1342.9807 | — | — |
| ${}^{169}$W | 169 | 95 | L?-pending | pending | binding_energy | — | 1351.0769 | — | — |
| ${}^{170}$W | 170 | 96 | L?-pending | pending | binding_energy | — | 1361.5212 | — | — |
| ${}^{171}$W | 171 | 97 | L?-pending | pending | binding_energy | — | 1369.3878 | — | — |
| ${}^{172}$W | 172 | 98 | L?-pending | pending | binding_energy | — | 1379.4702 | — | — |
| ${}^{173}$W | 173 | 99 | L?-pending | pending | binding_energy | — | 1387.1717 | — | — |
| ${}^{174}$W | 174 | 100 | L?-pending | pending | binding_energy | — | 1396.7428 | — | — |
| ${}^{175}$W | 175 | 101 | L?-pending | pending | binding_energy | — | 1404.2198 | — | — |
| ${}^{176}$W | 176 | 102 | L?-pending | pending | binding_energy | — | 1413.2999 | — | — |
| ${}^{177}$W | 177 | 103 | L?-pending | pending | binding_energy | — | 1420.4314 | — | — |
| ${}^{178}$W | 178 | 104 | L?-pending | pending | binding_energy | — | 1429.2080 | — | — |
| ${}^{179}$W | 179 | 105 | L?-pending | pending | binding_energy | — | 1436.1675 | — | — |
| ${}^{180}$W | 180 | 106 | L?-pending | pending | binding_energy | — | 1444.5798 | — | — |
| ${}^{181}$W | 181 | 107 | L?-pending | pending | binding_energy | — | 1451.2488 | — | — |
| ${}^{182}$W | 182 | 108 | L?-pending | pending | binding_energy | — | 1459.3323 | — | — |
| ${}^{183}$W | 183 | 109 | L?-pending | pending | binding_energy | — | 1465.5232 | — | — |
| ${}^{184}$W | 184 | 110 | L?-pending | pending | binding_energy | — | 1472.9343 | — | — |
| ${}^{185}$W | 185 | 111 | L?-pending | pending | binding_energy | — | 1478.6880 | — | — |
| ${}^{186}$W | 186 | 112 | L?-pending | pending | binding_energy | — | 1485.8801 | — | — |
| ${}^{187}$W | 187 | 113 | L?-pending | pending | binding_energy | — | 1491.3468 | — | — |
| ${}^{188}$W | 188 | 114 | L?-pending | pending | binding_energy | — | 1498.1820 | — | — |
| ${}^{189}$W | 189 | 115 | L?-pending | pending | binding_energy | — | 1503.3060 | — | — |
| ${}^{190}$W | 190 | 116 | L?-pending | pending | binding_energy | — | 1510.0256 | — | — |
| ${}^{191}$W | 191 | 117 | L?-pending | pending | binding_energy | — | 1514.9043 | — | — |
| ${}^{192}$W | 192 | 118 | L?-pending | pending | binding_energy | — | 1521.4080 | — | — |
| ${}^{193}$W | 193 | 119 | L?-pending | pending | binding_energy | — | 1526.0510 | — | — |
| ${}^{194}$W | 194 | 120 | L?-pending | pending | binding_energy | — | 1532.4060 | — | — |
| ${}^{195}$W | 195 | 121 | L?-pending | pending | binding_energy | — | 1536.7950 | — | — |
| ${}^{196}$W | 196 | 122 | L?-pending | pending | binding_energy | — | 1542.9120 | — | — |
| ${}^{197}$W | 197 | 123 | L?-pending | pending | binding_energy | — | 1547.0410 | — | — |

### Rhenium (Z = 75)

_0 of 41 isotopes with a framework prediction; 0 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{159}$Re | 159 | 84 | L?-pending | pending | binding_energy | — | 1239.4050 | — | — |
| ${}^{160}$Re | 160 | 85 | L?-pending | pending | binding_energy | — | 1249.6000 | — | — |
| ${}^{161}$Re | 161 | 86 | L?-pending | pending | binding_energy | — | 1261.6490 | — | — |
| ${}^{162}$Re | 162 | 87 | L?-pending | pending | binding_energy | — | 1271.3760 | — | — |
| ${}^{163}$Re | 163 | 88 | L?-pending | pending | binding_energy | — | 1282.9511 | — | — |
| ${}^{164}$Re | 164 | 89 | L?-pending | pending | binding_energy | — | 1292.4926 | — | — |
| ${}^{165}$Re | 165 | 90 | L?-pending | pending | binding_energy | — | 1303.7508 | — | — |
| ${}^{166}$Re | 166 | 91 | L?-pending | pending | binding_energy | — | 1313.0001 | — | — |
| ${}^{167}$Re | 167 | 92 | L?-pending | pending | binding_energy | — | 1324.1430 | — | — |
| ${}^{168}$Re | 168 | 93 | L?-pending | pending | binding_energy | — | 1333.1003 | — | — |
| ${}^{169}$Re | 169 | 94 | L?-pending | pending | binding_energy | — | 1343.7860 | — | — |
| ${}^{170}$Re | 170 | 95 | L?-pending | pending | binding_energy | — | 1352.3520 | — | — |
| ${}^{171}$Re | 171 | 96 | L?-pending | pending | binding_energy | — | 1362.7696 | — | — |
| ${}^{172}$Re | 172 | 97 | L?-pending | pending | binding_energy | — | 1371.1575 | — | — |
| ${}^{173}$Re | 173 | 98 | L?-pending | pending | binding_energy | — | 1381.2159 | — | — |
| ${}^{174}$Re | 174 | 99 | L?-pending | pending | binding_energy | — | 1389.4064 | — | — |
| ${}^{175}$Re | 175 | 100 | L?-pending | pending | binding_energy | — | 1399.0929 | — | — |
| ${}^{176}$Re | 176 | 101 | L?-pending | pending | binding_energy | — | 1406.9388 | — | — |
| ${}^{177}$Re | 177 | 102 | L?-pending | pending | binding_energy | — | 1416.2165 | — | — |
| ${}^{178}$Re | 178 | 103 | L?-pending | pending | binding_energy | — | 1423.6721 | — | — |
| ${}^{179}$Re | 179 | 104 | L?-pending | pending | binding_energy | — | 1432.6742 | — | — |
| ${}^{180}$Re | 180 | 105 | L?-pending | pending | binding_energy | — | 1439.9986 | — | — |
| ${}^{181}$Re | 181 | 106 | L?-pending | pending | binding_energy | — | 1448.7500 | — | — |
| ${}^{182}$Re | 182 | 107 | L?-pending | pending | binding_energy | — | 1455.7500 | — | — |
| ${}^{183}$Re | 183 | 108 | L?-pending | pending | binding_energy | — | 1464.1848 | — | — |
| ${}^{184}$Re | 184 | 109 | L?-pending | pending | binding_energy | — | 1470.6663 | — | — |
| ${}^{185}$Re | 185 | 110 | L?-pending | pending | binding_energy | — | 1478.3369 | — | — |
| ${}^{186}$Re | 186 | 111 | L?-pending | pending | binding_energy | — | 1484.5165 | — | — |
| ${}^{187}$Re | 187 | 112 | L?-pending | pending | binding_energy | — | 1491.8770 | — | — |
| ${}^{188}$Re | 188 | 113 | L?-pending | pending | binding_energy | — | 1497.7486 | — | — |
| ${}^{189}$Re | 189 | 114 | L?-pending | pending | binding_energy | — | 1504.7822 | — | — |
| ${}^{190}$Re | 190 | 115 | L?-pending | pending | binding_energy | — | 1510.4574 | — | — |
| ${}^{191}$Re | 191 | 116 | L?-pending | pending | binding_energy | — | 1517.2961 | — | — |
| ${}^{192}$Re | 192 | 117 | L?-pending | pending | binding_energy | — | 1522.6059 | — | — |
| ${}^{193}$Re | 193 | 118 | L?-pending | pending | binding_energy | — | 1529.3200 | — | — |
| ${}^{194}$Re | 194 | 119 | L?-pending | pending | binding_energy | — | 1534.3460 | — | — |
| ${}^{195}$Re | 195 | 120 | L?-pending | pending | binding_energy | — | 1540.6950 | — | — |
| ${}^{196}$Re | 196 | 121 | L?-pending | pending | binding_energy | — | 1545.6560 | — | — |
| ${}^{197}$Re | 197 | 122 | L?-pending | pending | binding_energy | — | 1551.7690 | — | — |
| ${}^{198}$Re | 198 | 123 | L?-pending | pending | binding_energy | — | 1556.4780 | — | — |
| ${}^{199}$Re | 199 | 124 | L?-pending | pending | binding_energy | — | 1562.1500 | — | — |

### Osmium (Z = 76)

_0 of 43 isotopes with a framework prediction; 0 of 43 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{161}$Os | 161 | 85 | L?-pending | pending | binding_energy | — | 1250.1650 | — | — |
| ${}^{162}$Os | 162 | 86 | L?-pending | pending | binding_energy | — | 1262.6280 | — | — |
| ${}^{163}$Os | 163 | 87 | L?-pending | pending | binding_energy | — | 1272.5410 | — | — |
| ${}^{164}$Os | 164 | 88 | L?-pending | pending | binding_energy | — | 1284.6625 | — | — |
| ${}^{165}$Os | 165 | 89 | L?-pending | pending | binding_energy | — | 1294.0950 | — | — |
| ${}^{166}$Os | 166 | 90 | L?-pending | pending | binding_energy | — | 1305.8120 | — | — |
| ${}^{167}$Os | 167 | 91 | L?-pending | pending | binding_energy | — | 1314.9506 | — | — |
| ${}^{168}$Os | 168 | 92 | L?-pending | pending | binding_energy | — | 1326.5181 | — | — |
| ${}^{169}$Os | 169 | 93 | L?-pending | pending | binding_energy | — | 1335.3174 | — | — |
| ${}^{170}$Os | 170 | 94 | L?-pending | pending | binding_energy | — | 1346.5914 | — | — |
| ${}^{171}$Os | 171 | 95 | L?-pending | pending | binding_energy | — | 1355.0342 | — | — |
| ${}^{172}$Os | 172 | 96 | L?-pending | pending | binding_energy | — | 1366.0520 | — | — |
| ${}^{173}$Os | 173 | 97 | L?-pending | pending | binding_energy | — | 1374.3179 | — | — |
| ${}^{174}$Os | 174 | 98 | L?-pending | pending | binding_energy | — | 1384.9464 | — | — |
| ${}^{175}$Os | 175 | 99 | L?-pending | pending | binding_energy | — | 1393.1276 | — | — |
| ${}^{176}$Os | 176 | 100 | L?-pending | pending | binding_energy | — | 1403.2248 | — | — |
| ${}^{177}$Os | 177 | 101 | L?-pending | pending | binding_energy | — | 1411.1214 | — | — |
| ${}^{178}$Os | 178 | 102 | L?-pending | pending | binding_energy | — | 1420.7805 | — | — |
| ${}^{179}$Os | 179 | 103 | L?-pending | pending | binding_energy | — | 1428.3277 | — | — |
| ${}^{180}$Os | 180 | 104 | L?-pending | pending | binding_energy | — | 1437.7351 | — | — |
| ${}^{181}$Os | 181 | 105 | L?-pending | pending | binding_energy | — | 1445.0002 | — | — |
| ${}^{182}$Os | 182 | 106 | L?-pending | pending | binding_energy | — | 1454.1306 | — | — |
| ${}^{183}$Os | 183 | 107 | L?-pending | pending | binding_energy | — | 1461.2566 | — | — |
| ${}^{184}$Os | 184 | 108 | L?-pending | pending | binding_energy | — | 1469.9167 | — | — |
| ${}^{185}$Os | 185 | 109 | L?-pending | pending | binding_energy | — | 1476.5414 | — | — |
| ${}^{186}$Os | 186 | 110 | L?-pending | pending | binding_energy | — | 1484.8068 | — | — |
| ${}^{187}$Os | 187 | 111 | L?-pending | pending | binding_energy | — | 1491.0971 | — | — |
| ${}^{188}$Os | 188 | 112 | L?-pending | pending | binding_energy | — | 1499.0867 | — | — |
| ${}^{189}$Os | 189 | 113 | L?-pending | pending | binding_energy | — | 1505.0075 | — | — |
| ${}^{190}$Os | 190 | 114 | L?-pending | pending | binding_energy | — | 1512.7999 | — | — |
| ${}^{191}$Os | 191 | 115 | L?-pending | pending | binding_energy | — | 1518.5586 | — | — |
| ${}^{192}$Os | 192 | 116 | L?-pending | pending | binding_energy | — | 1526.1170 | — | — |
| ${}^{193}$Os | 193 | 117 | L?-pending | pending | binding_energy | — | 1531.7004 | — | — |
| ${}^{194}$Os | 194 | 118 | L?-pending | pending | binding_energy | — | 1538.8125 | — | — |
| ${}^{195}$Os | 195 | 119 | L?-pending | pending | binding_energy | — | 1543.9603 | — | — |
| ${}^{196}$Os | 196 | 120 | L?-pending | pending | binding_energy | — | 1550.7971 | — | — |
| ${}^{197}$Os | 197 | 121 | L?-pending | pending | binding_energy | — | 1555.7090 | — | — |
| ${}^{198}$Os | 198 | 122 | L?-pending | pending | binding_energy | — | 1562.2200 | — | — |
| ${}^{199}$Os | 199 | 123 | L?-pending | pending | binding_energy | — | 1566.9260 | — | — |
| ${}^{200}$Os | 200 | 124 | L?-pending | pending | binding_energy | — | 1573.4000 | — | — |
| ${}^{201}$Os | 201 | 125 | L?-pending | pending | binding_energy | — | 1577.6490 | — | — |
| ${}^{202}$Os | 202 | 126 | L?-pending | pending | binding_energy | — | 1583.4780 | — | — |
| ${}^{203}$Os | 203 | 127 | L?-pending | pending | binding_energy | — | 1586.2420 | — | — |

### Iridium (Z = 77)

_0 of 43 isotopes with a framework prediction; 0 of 43 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{163}$Ir | 163 | 86 | L?-pending | pending | binding_energy | — | 1260.6420 | — | — |
| ${}^{164}$Ir | 164 | 87 | L?-pending | pending | binding_energy | — | 1271.0000 | — | — |
| ${}^{165}$Ir | 165 | 88 | L?-pending | pending | binding_energy | — | 1283.0400 | — | — |
| ${}^{166}$Ir | 166 | 89 | L?-pending | pending | binding_energy | — | 1292.9740 | — | — |
| ${}^{167}$Ir | 167 | 90 | L?-pending | pending | binding_energy | — | 1304.7418 | — | — |
| ${}^{168}$Ir | 168 | 91 | L?-pending | pending | binding_energy | — | 1314.4070 | — | — |
| ${}^{169}$Ir | 169 | 92 | L?-pending | pending | binding_energy | — | 1325.9055 | — | — |
| ${}^{170}$Ir | 170 | 93 | L?-pending | pending | binding_energy | — | 1335.0100 | — | — |
| ${}^{171}$Ir | 171 | 94 | L?-pending | pending | binding_energy | — | 1346.3667 | — | — |
| ${}^{172}$Ir | 172 | 95 | L?-pending | pending | binding_energy | — | 1355.4054 | — | — |
| ${}^{173}$Ir | 173 | 96 | L?-pending | pending | binding_energy | — | 1366.3658 | — | — |
| ${}^{174}$Ir | 174 | 97 | L?-pending | pending | binding_energy | — | 1374.9546 | — | — |
| ${}^{175}$Ir | 175 | 98 | L?-pending | pending | binding_energy | — | 1385.6345 | — | — |
| ${}^{176}$Ir | 176 | 99 | L?-pending | pending | binding_energy | — | 1394.1932 | — | — |
| ${}^{177}$Ir | 177 | 100 | L?-pending | pending | binding_energy | — | 1404.4300 | — | — |
| ${}^{178}$Ir | 178 | 101 | L?-pending | pending | binding_energy | — | 1412.7082 | — | — |
| ${}^{179}$Ir | 179 | 102 | L?-pending | pending | binding_energy | — | 1422.6069 | — | — |
| ${}^{180}$Ir | 180 | 103 | L?-pending | pending | binding_energy | — | 1430.5741 | — | — |
| ${}^{181}$Ir | 181 | 104 | L?-pending | pending | binding_energy | — | 1440.1309 | — | — |
| ${}^{182}$Ir | 182 | 105 | L?-pending | pending | binding_energy | — | 1447.7909 | — | — |
| ${}^{183}$Ir | 183 | 106 | L?-pending | pending | binding_energy | — | 1457.0126 | — | — |
| ${}^{184}$Ir | 184 | 107 | L?-pending | pending | binding_energy | — | 1464.4927 | — | — |
| ${}^{185}$Ir | 185 | 108 | L?-pending | pending | binding_energy | — | 1473.2887 | — | — |
| ${}^{186}$Ir | 186 | 109 | L?-pending | pending | binding_energy | — | 1480.1968 | — | — |
| ${}^{187}$Ir | 187 | 110 | L?-pending | pending | binding_energy | — | 1488.6451 | — | — |
| ${}^{188}$Ir | 188 | 111 | L?-pending | pending | binding_energy | — | 1495.5120 | — | — |
| ${}^{189}$Ir | 189 | 112 | L?-pending | pending | binding_energy | — | 1503.6880 | — | — |
| ${}^{190}$Ir | 190 | 113 | L?-pending | pending | binding_energy | — | 1510.0633 | — | — |
| ${}^{191}$Ir | 191 | 114 | L?-pending | pending | binding_energy | — | 1518.0899 | — | — |
| ${}^{192}$Ir | 192 | 115 | L?-pending | pending | binding_energy | — | 1524.2880 | — | — |
| ${}^{193}$Ir | 193 | 116 | L?-pending | pending | binding_energy | — | 1532.0600 | — | — |
| ${}^{194}$Ir | 194 | 117 | L?-pending | pending | binding_energy | — | 1538.1268 | — | — |
| ${}^{195}$Ir | 195 | 118 | L?-pending | pending | binding_energy | — | 1545.3586 | — | — |
| ${}^{196}$Ir | 196 | 119 | L?-pending | pending | binding_energy | — | 1551.1731 | — | — |
| ${}^{197}$Ir | 197 | 120 | L?-pending | pending | binding_energy | — | 1558.0731 | — | — |
| ${}^{198}$Ir | 198 | 121 | L?-pending | pending | binding_energy | — | 1563.6060 | — | — |
| ${}^{199}$Ir | 199 | 122 | L?-pending | pending | binding_energy | — | 1570.3501 | — | — |
| ${}^{200}$Ir | 200 | 123 | L?-pending | pending | binding_energy | — | 1575.6000 | — | — |
| ${}^{201}$Ir | 201 | 124 | L?-pending | pending | binding_energy | — | 1581.8700 | — | — |
| ${}^{202}$Ir | 202 | 125 | L?-pending | pending | binding_energy | — | 1586.7100 | — | — |
| ${}^{203}$Ir | 203 | 126 | L?-pending | pending | binding_energy | — | 1592.5350 | — | — |
| ${}^{204}$Ir | 204 | 127 | L?-pending | pending | binding_energy | — | 1595.8920 | — | — |
| ${}^{205}$Ir | 205 | 128 | L?-pending | pending | binding_energy | — | 1600.0250 | — | — |

### Platinum (Z = 78)

_0 of 44 isotopes with a framework prediction; 0 of 44 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{165}$Pt | 165 | 87 | L?-pending | pending | binding_energy | — | 1270.9950 | — | — |
| ${}^{166}$Pt | 166 | 88 | L?-pending | pending | binding_energy | — | 1283.6780 | — | — |
| ${}^{167}$Pt | 167 | 89 | L?-pending | pending | binding_energy | — | 1293.5820 | — | — |
| ${}^{168}$Pt | 168 | 90 | L?-pending | pending | binding_energy | — | 1305.9684 | — | — |
| ${}^{169}$Pt | 169 | 91 | L?-pending | pending | binding_energy | — | 1315.4960 | — | — |
| ${}^{170}$Pt | 170 | 92 | L?-pending | pending | binding_energy | — | 1327.4002 | — | — |
| ${}^{171}$Pt | 171 | 93 | L?-pending | pending | binding_energy | — | 1336.6389 | — | — |
| ${}^{172}$Pt | 172 | 94 | L?-pending | pending | binding_energy | — | 1348.3503 | — | — |
| ${}^{173}$Pt | 173 | 95 | L?-pending | pending | binding_energy | — | 1357.2517 | — | — |
| ${}^{174}$Pt | 174 | 96 | L?-pending | pending | binding_energy | — | 1368.7039 | — | — |
| ${}^{175}$Pt | 175 | 97 | L?-pending | pending | binding_energy | — | 1377.1663 | — | — |
| ${}^{176}$Pt | 176 | 98 | L?-pending | pending | binding_energy | — | 1388.4628 | — | — |
| ${}^{177}$Pt | 177 | 99 | L?-pending | pending | binding_energy | — | 1396.9707 | — | — |
| ${}^{178}$Pt | 178 | 100 | L?-pending | pending | binding_energy | — | 1407.6690 | — | — |
| ${}^{179}$Pt | 179 | 101 | L?-pending | pending | binding_energy | — | 1416.0110 | — | — |
| ${}^{180}$Pt | 180 | 102 | L?-pending | pending | binding_energy | — | 1426.2441 | — | — |
| ${}^{181}$Pt | 181 | 103 | L?-pending | pending | binding_energy | — | 1434.2670 | — | — |
| ${}^{182}$Pt | 182 | 104 | L?-pending | pending | binding_energy | — | 1444.1252 | — | — |
| ${}^{183}$Pt | 183 | 105 | L?-pending | pending | binding_energy | — | 1451.8013 | — | — |
| ${}^{184}$Pt | 184 | 106 | L?-pending | pending | binding_energy | — | 1461.4319 | — | — |
| ${}^{185}$Pt | 185 | 107 | L?-pending | pending | binding_energy | — | 1468.8589 | — | — |
| ${}^{186}$Pt | 186 | 108 | L?-pending | pending | binding_energy | — | 1478.1065 | — | — |
| ${}^{187}$Pt | 187 | 109 | L?-pending | pending | binding_energy | — | 1484.9988 | — | — |
| ${}^{188}$Pt | 188 | 110 | L?-pending | pending | binding_energy | — | 1494.2057 | — | — |
| ${}^{189}$Pt | 189 | 111 | L?-pending | pending | binding_energy | — | 1500.9255 | — | — |
| ${}^{190}$Pt | 190 | 112 | L?-pending | pending | binding_energy | — | 1509.8339 | — | — |
| ${}^{191}$Pt | 191 | 113 | L?-pending | pending | binding_energy | — | 1516.2970 | — | — |
| ${}^{192}$Pt | 192 | 114 | L?-pending | pending | binding_energy | — | 1524.9585 | — | — |
| ${}^{193}$Pt | 193 | 115 | L?-pending | pending | binding_energy | — | 1531.2210 | — | — |
| ${}^{194}$Pt | 194 | 116 | L?-pending | pending | binding_energy | — | 1539.5727 | — | — |
| ${}^{195}$Pt | 195 | 117 | L?-pending | pending | binding_energy | — | 1545.6778 | — | — |
| ${}^{196}$Pt | 196 | 118 | L?-pending | pending | binding_energy | — | 1553.5998 | — | — |
| ${}^{197}$Pt | 197 | 119 | L?-pending | pending | binding_energy | — | 1559.4464 | — | — |
| ${}^{198}$Pt | 198 | 120 | L?-pending | pending | binding_energy | — | 1567.0019 | — | — |
| ${}^{199}$Pt | 199 | 121 | L?-pending | pending | binding_energy | — | 1572.5579 | — | — |
| ${}^{200}$Pt | 200 | 122 | L?-pending | pending | binding_energy | — | 1579.8397 | — | — |
| ${}^{201}$Pt | 201 | 123 | L?-pending | pending | binding_energy | — | 1585.0526 | — | — |
| ${}^{202}$Pt | 202 | 124 | L?-pending | pending | binding_energy | — | 1592.0753 | — | — |
| ${}^{203}$Pt | 203 | 125 | L?-pending | pending | binding_energy | — | 1597.0010 | — | — |
| ${}^{204}$Pt | 204 | 126 | L?-pending | pending | binding_energy | — | 1603.2360 | — | — |
| ${}^{205}$Pt | 205 | 127 | L?-pending | pending | binding_energy | — | 1606.3800 | — | — |
| ${}^{206}$Pt | 206 | 128 | L?-pending | pending | binding_energy | — | 1610.9200 | — | — |
| ${}^{207}$Pt | 207 | 129 | L?-pending | pending | binding_energy | — | 1613.9790 | — | — |
| ${}^{208}$Pt | 208 | 130 | L?-pending | pending | binding_energy | — | 1618.2400 | — | — |

### Gold (Z = 79)

_0 of 43 isotopes with a framework prediction; 0 of 43 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{168}$Au | 168 | 89 | L?-pending | pending | binding_energy | — | 1291.5840 | — | — |
| ${}^{169}$Au | 169 | 90 | L?-pending | pending | binding_energy | — | 1304.0040 | — | — |
| ${}^{170}$Au | 170 | 91 | L?-pending | pending | binding_energy | — | 1314.1000 | — | — |
| ${}^{171}$Au | 171 | 92 | L?-pending | pending | binding_energy | — | 1325.9523 | — | — |
| ${}^{172}$Au | 172 | 93 | L?-pending | pending | binding_energy | — | 1335.7793 | — | — |
| ${}^{173}$Au | 173 | 94 | L?-pending | pending | binding_energy | — | 1347.3646 | — | — |
| ${}^{174}$Au | 174 | 95 | L?-pending | pending | binding_energy | — | 1356.6780 | — | — |
| ${}^{175}$Au | 175 | 96 | L?-pending | pending | binding_energy | — | 1368.0789 | — | — |
| ${}^{176}$Au | 176 | 97 | L?-pending | pending | binding_energy | — | 1377.2675 | — | — |
| ${}^{177}$Au | 177 | 98 | L?-pending | pending | binding_energy | — | 1388.3636 | — | — |
| ${}^{178}$Au | 178 | 99 | L?-pending | pending | binding_energy | — | 1397.1922 | — | — |
| ${}^{179}$Au | 179 | 100 | L?-pending | pending | binding_energy | — | 1407.9491 | — | — |
| ${}^{180}$Au | 180 | 101 | L?-pending | pending | binding_energy | — | 1416.6575 | — | — |
| ${}^{181}$Au | 181 | 102 | L?-pending | pending | binding_energy | — | 1426.9743 | — | — |
| ${}^{182}$Au | 182 | 103 | L?-pending | pending | binding_energy | — | 1435.4784 | — | — |
| ${}^{183}$Au | 183 | 104 | L?-pending | pending | binding_energy | — | 1445.4373 | — | — |
| ${}^{184}$Au | 184 | 105 | L?-pending | pending | binding_energy | — | 1453.6358 | — | — |
| ${}^{185}$Au | 185 | 106 | L?-pending | pending | binding_energy | — | 1463.2466 | — | — |
| ${}^{186}$Au | 186 | 107 | L?-pending | pending | binding_energy | — | 1471.1746 | — | — |
| ${}^{187}$Au | 187 | 108 | L?-pending | pending | binding_energy | — | 1480.5598 | — | — |
| ${}^{188}$Au | 188 | 109 | L?-pending | pending | binding_energy | — | 1487.9737 | — | — |
| ${}^{189}$Au | 189 | 110 | L?-pending | pending | binding_energy | — | 1497.2557 | — | — |
| ${}^{190}$Au | 190 | 111 | L?-pending | pending | binding_energy | — | 1504.5786 | — | — |
| ${}^{191}$Au | 191 | 112 | L?-pending | pending | binding_energy | — | 1513.6142 | — | — |
| ${}^{192}$Au | 192 | 113 | L?-pending | pending | binding_energy | — | 1520.6598 | — | — |
| ${}^{193}$Au | 193 | 114 | L?-pending | pending | binding_energy | — | 1529.3638 | — | — |
| ${}^{194}$Au | 194 | 115 | L?-pending | pending | binding_energy | — | 1536.2422 | — | — |
| ${}^{195}$Au | 195 | 116 | L?-pending | pending | binding_energy | — | 1544.6687 | — | — |
| ${}^{196}$Au | 196 | 117 | L?-pending | pending | binding_energy | — | 1551.3116 | — | — |
| ${}^{197}$Au | 197 | 118 | L?-pending | pending | binding_energy | — | 1559.3840 | — | — |
| ${}^{198}$Au | 198 | 119 | L?-pending | pending | binding_energy | — | 1565.8964 | — | — |
| ${}^{199}$Au | 199 | 120 | L?-pending | pending | binding_energy | — | 1573.4806 | — | — |
| ${}^{200}$Au | 200 | 121 | L?-pending | pending | binding_energy | — | 1579.6983 | — | — |
| ${}^{201}$Au | 201 | 122 | L?-pending | pending | binding_energy | — | 1586.9302 | — | — |
| ${}^{202}$Au | 202 | 123 | L?-pending | pending | binding_energy | — | 1592.9538 | — | — |
| ${}^{203}$Au | 203 | 124 | L?-pending | pending | binding_energy | — | 1599.8156 | — | — |
| ${}^{204}$Au | 204 | 125 | L?-pending | pending | binding_energy | — | 1605.0720 | — | — |
| ${}^{205}$Au | 205 | 126 | L?-pending | pending | binding_energy | — | 1611.3000 | — | — |
| ${}^{206}$Au | 206 | 127 | L?-pending | pending | binding_energy | — | 1615.0400 | — | — |
| ${}^{207}$Au | 207 | 128 | L?-pending | pending | binding_energy | — | 1619.5680 | — | — |
| ${}^{208}$Au | 208 | 129 | L?-pending | pending | binding_energy | — | 1623.0240 | — | — |
| ${}^{209}$Au | 209 | 130 | L?-pending | pending | binding_energy | — | 1627.2740 | — | — |
| ${}^{210}$Au | 210 | 131 | L?-pending | pending | binding_energy | — | 1630.4400 | — | — |

### Mercury (Z = 80)

_0 of 47 isotopes with a framework prediction; 0 of 47 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{170}$Hg | 170 | 90 | L?-pending | pending | binding_energy | — | 1304.0700 | — | — |
| ${}^{171}$Hg | 171 | 91 | L?-pending | pending | binding_energy | — | 1314.3060 | — | — |
| ${}^{172}$Hg | 172 | 92 | L?-pending | pending | binding_energy | — | 1326.7403 | — | — |
| ${}^{173}$Hg | 173 | 93 | L?-pending | pending | binding_energy | — | 1336.4250 | — | — |
| ${}^{174}$Hg | 174 | 94 | L?-pending | pending | binding_energy | — | 1348.4626 | — | — |
| ${}^{175}$Hg | 175 | 95 | L?-pending | pending | binding_energy | — | 1357.8623 | — | — |
| ${}^{176}$Hg | 176 | 96 | L?-pending | pending | binding_energy | — | 1369.7489 | — | — |
| ${}^{177}$Hg | 177 | 97 | L?-pending | pending | binding_energy | — | 1378.8114 | — | — |
| ${}^{178}$Hg | 178 | 98 | L?-pending | pending | binding_energy | — | 1390.4222 | — | — |
| ${}^{179}$Hg | 179 | 99 | L?-pending | pending | binding_energy | — | 1399.1111 | — | — |
| ${}^{180}$Hg | 180 | 100 | L?-pending | pending | binding_energy | — | 1410.5000 | — | — |
| ${}^{181}$Hg | 181 | 101 | L?-pending | pending | binding_energy | — | 1418.9819 | — | — |
| ${}^{182}$Hg | 182 | 102 | L?-pending | pending | binding_energy | — | 1429.9690 | — | — |
| ${}^{183}$Hg | 183 | 103 | L?-pending | pending | binding_energy | — | 1438.2681 | — | — |
| ${}^{184}$Hg | 184 | 104 | L?-pending | pending | binding_energy | — | 1448.8796 | — | — |
| ${}^{185}$Hg | 185 | 105 | L?-pending | pending | binding_energy | — | 1456.7897 | — | — |
| ${}^{186}$Hg | 186 | 106 | L?-pending | pending | binding_energy | — | 1467.2165 | — | — |
| ${}^{187}$Hg | 187 | 107 | L?-pending | pending | binding_energy | — | 1474.8672 | — | — |
| ${}^{188}$Hg | 188 | 108 | L?-pending | pending | binding_energy | — | 1485.0184 | — | — |
| ${}^{189}$Hg | 189 | 109 | L?-pending | pending | binding_energy | — | 1492.5177 | — | — |
| ${}^{190}$Hg | 190 | 110 | L?-pending | pending | binding_energy | — | 1502.3333 | — | — |
| ${}^{191}$Hg | 191 | 111 | L?-pending | pending | binding_energy | — | 1509.6258 | — | — |
| ${}^{192}$Hg | 192 | 112 | L?-pending | pending | binding_energy | — | 1519.1168 | — | — |
| ${}^{193}$Hg | 193 | 113 | L?-pending | pending | binding_energy | — | 1526.2388 | — | — |
| ${}^{194}$Hg | 194 | 114 | L?-pending | pending | binding_energy | — | 1535.4319 | — | — |
| ${}^{195}$Hg | 195 | 115 | L?-pending | pending | binding_energy | — | 1542.3326 | — | — |
| ${}^{196}$Hg | 196 | 116 | L?-pending | pending | binding_energy | — | 1551.2165 | — | — |
| ${}^{197}$Hg | 197 | 117 | L?-pending | pending | binding_energy | — | 1558.0021 | — | — |
| ${}^{198}$Hg | 198 | 118 | L?-pending | pending | binding_energy | — | 1566.4875 | — | — |
| ${}^{199}$Hg | 199 | 119 | L?-pending | pending | binding_energy | — | 1573.1506 | — | — |
| ${}^{200}$Hg | 200 | 120 | L?-pending | pending | binding_energy | — | 1581.1791 | — | — |
| ${}^{201}$Hg | 201 | 121 | L?-pending | pending | binding_energy | — | 1587.4097 | — | — |
| ${}^{202}$Hg | 202 | 122 | L?-pending | pending | binding_energy | — | 1595.1638 | — | — |
| ${}^{203}$Hg | 203 | 123 | L?-pending | pending | binding_energy | — | 1601.1590 | — | — |
| ${}^{204}$Hg | 204 | 124 | L?-pending | pending | binding_energy | — | 1608.6513 | — | — |
| ${}^{205}$Hg | 205 | 125 | L?-pending | pending | binding_energy | — | 1614.3202 | — | — |
| ${}^{206}$Hg | 206 | 126 | L?-pending | pending | binding_energy | — | 1621.0495 | — | — |
| ${}^{207}$Hg | 207 | 127 | L?-pending | pending | binding_energy | — | 1624.6625 | — | — |
| ${}^{208}$Hg | 208 | 128 | L?-pending | pending | binding_energy | — | 1629.5118 | — | — |
| ${}^{209}$Hg | 209 | 129 | L?-pending | pending | binding_energy | — | 1632.9170 | — | — |
| ${}^{210}$Hg | 210 | 130 | L?-pending | pending | binding_energy | — | 1637.7900 | — | — |
| ${}^{211}$Hg | 211 | 131 | L?-pending | pending | binding_energy | — | 1640.9470 | — | — |
| ${}^{212}$Hg | 212 | 132 | L?-pending | pending | binding_energy | — | 1645.5440 | — | — |
| ${}^{213}$Hg | 213 | 133 | L?-pending | pending | binding_energy | — | 1648.4070 | — | — |
| ${}^{214}$Hg | 214 | 134 | L?-pending | pending | binding_energy | — | 1652.9360 | — | — |
| ${}^{215}$Hg | 215 | 135 | L?-pending | pending | binding_energy | — | 1655.7150 | — | — |
| ${}^{216}$Hg | 216 | 136 | L?-pending | pending | binding_energy | — | 1659.9600 | — | — |

### Thallium (Z = 81)

_0 of 43 isotopes with a framework prediction; 0 of 43 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{176}$Tl | 176 | 95 | L?-pending | pending | binding_energy | — | 1356.5971 | — | — |
| ${}^{177}$Tl | 177 | 96 | L?-pending | pending | binding_energy | — | 1368.5933 | — | — |
| ${}^{178}$Tl | 178 | 97 | L?-pending | pending | binding_energy | — | 1377.8980 | — | — |
| ${}^{179}$Tl | 179 | 98 | L?-pending | pending | binding_energy | — | 1389.6655 | — | — |
| ${}^{180}$Tl | 180 | 99 | L?-pending | pending | binding_energy | — | 1398.8576 | — | — |
| ${}^{181}$Tl | 181 | 100 | L?-pending | pending | binding_energy | — | 1410.3372 | — | — |
| ${}^{182}$Tl | 182 | 101 | L?-pending | pending | binding_energy | — | 1418.9370 | — | — |
| ${}^{183}$Tl | 183 | 102 | L?-pending | pending | binding_energy | — | 1430.2684 | — | — |
| ${}^{184}$Tl | 184 | 103 | L?-pending | pending | binding_energy | — | 1438.6358 | — | — |
| ${}^{185}$Tl | 185 | 104 | L?-pending | pending | binding_energy | — | 1449.5815 | — | — |
| ${}^{186}$Tl | 186 | 105 | L?-pending | pending | binding_energy | — | 1457.7780 | — | — |
| ${}^{187}$Tl | 187 | 106 | L?-pending | pending | binding_energy | — | 1468.4110 | — | — |
| ${}^{188}$Tl | 188 | 107 | L?-pending | pending | binding_energy | — | 1476.3741 | — | — |
| ${}^{189}$Tl | 189 | 108 | L?-pending | pending | binding_energy | — | 1486.7251 | — | — |
| ${}^{190}$Tl | 190 | 109 | L?-pending | pending | binding_energy | — | 1494.5466 | — | — |
| ${}^{191}$Tl | 191 | 110 | L?-pending | pending | binding_energy | — | 1504.5346 | — | — |
| ${}^{192}$Tl | 192 | 111 | L?-pending | pending | binding_energy | — | 1512.1952 | — | — |
| ${}^{193}$Tl | 193 | 112 | L?-pending | pending | binding_energy | — | 1521.8715 | — | — |
| ${}^{194}$Tl | 194 | 113 | L?-pending | pending | binding_energy | — | 1529.4031 | — | — |
| ${}^{195}$Tl | 195 | 114 | L?-pending | pending | binding_energy | — | 1538.6922 | — | — |
| ${}^{196}$Tl | 196 | 115 | L?-pending | pending | binding_energy | — | 1546.1048 | — | — |
| ${}^{197}$Tl | 197 | 116 | L?-pending | pending | binding_energy | — | 1555.0338 | — | — |
| ${}^{198}$Tl | 198 | 117 | L?-pending | pending | binding_energy | — | 1562.2796 | — | — |
| ${}^{199}$Tl | 199 | 118 | L?-pending | pending | binding_energy | — | 1570.8816 | — | — |
| ${}^{200}$Tl | 200 | 119 | L?-pending | pending | binding_energy | — | 1577.9407 | — | — |
| ${}^{201}$Tl | 201 | 120 | L?-pending | pending | binding_energy | — | 1586.1456 | — | — |
| ${}^{202}$Tl | 202 | 121 | L?-pending | pending | binding_energy | — | 1593.0166 | — | — |
| ${}^{203}$Tl | 203 | 122 | L?-pending | pending | binding_energy | — | 1600.8688 | — | — |
| ${}^{204}$Tl | 204 | 123 | L?-pending | pending | binding_energy | — | 1607.5249 | — | — |
| ${}^{205}$Tl | 205 | 124 | L?-pending | pending | binding_energy | — | 1615.0709 | — | — |
| ${}^{206}$Tl | 206 | 125 | L?-pending | pending | binding_energy | — | 1621.5747 | — | — |
| ${}^{207}$Tl | 207 | 126 | L?-pending | pending | binding_energy | — | 1628.4272 | — | — |
| ${}^{208}$Tl | 208 | 127 | L?-pending | pending | binding_energy | — | 1632.2142 | — | — |
| ${}^{209}$Tl | 209 | 128 | L?-pending | pending | binding_energy | — | 1637.1802 | — | — |
| ${}^{210}$Tl | 210 | 129 | L?-pending | pending | binding_energy | — | 1640.8537 | — | — |
| ${}^{211}$Tl | 211 | 130 | L?-pending | pending | binding_energy | — | 1645.7560 | — | — |
| ${}^{212}$Tl | 212 | 131 | L?-pending | pending | binding_energy | — | 1649.3600 | — | — |
| ${}^{213}$Tl | 213 | 132 | L?-pending | pending | binding_energy | — | 1654.0368 | — | — |
| ${}^{214}$Tl | 214 | 133 | L?-pending | pending | binding_energy | — | 1657.4300 | — | — |
| ${}^{215}$Tl | 215 | 134 | L?-pending | pending | binding_energy | — | 1661.9500 | — | — |
| ${}^{216}$Tl | 216 | 135 | L?-pending | pending | binding_energy | — | 1665.1440 | — | — |
| ${}^{217}$Tl | 217 | 136 | L?-pending | pending | binding_energy | — | 1669.3810 | — | — |
| ${}^{218}$Tl | 218 | 137 | L?-pending | pending | binding_energy | — | 1672.4960 | — | — |

### Lead (Z = 82)

_0 of 43 isotopes with a framework prediction; 0 of 43 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{178}$Pb | 178 | 96 | L?-pending | pending | binding_energy | — | 1368.9688 | — | — |
| ${}^{179}$Pb | 179 | 97 | L?-pending | pending | binding_energy | — | 1378.5619 | — | — |
| ${}^{180}$Pb | 180 | 98 | L?-pending | pending | binding_energy | — | 1390.6259 | — | — |
| ${}^{181}$Pb | 181 | 99 | L?-pending | pending | binding_energy | — | 1399.8667 | — | — |
| ${}^{182}$Pb | 182 | 100 | L?-pending | pending | binding_energy | — | 1411.6520 | — | — |
| ${}^{183}$Pb | 183 | 101 | L?-pending | pending | binding_energy | — | 1420.4788 | — | — |
| ${}^{184}$Pb | 184 | 102 | L?-pending | pending | binding_energy | — | 1432.0217 | — | — |
| ${}^{185}$Pb | 185 | 103 | L?-pending | pending | binding_energy | — | 1440.5826 | — | — |
| ${}^{186}$Pb | 186 | 104 | L?-pending | pending | binding_energy | — | 1451.7936 | — | — |
| ${}^{187}$Pb | 187 | 105 | L?-pending | pending | binding_energy | — | 1460.1710 | — | — |
| ${}^{188}$Pb | 188 | 106 | L?-pending | pending | binding_energy | — | 1471.0664 | — | — |
| ${}^{189}$Pb | 189 | 107 | L?-pending | pending | binding_energy | — | 1479.1707 | — | — |
| ${}^{190}$Pb | 190 | 108 | L?-pending | pending | binding_energy | — | 1489.8146 | — | — |
| ${}^{191}$Pb | 191 | 109 | L?-pending | pending | binding_energy | — | 1497.7605 | — | — |
| ${}^{192}$Pb | 192 | 110 | L?-pending | pending | binding_energy | — | 1508.0925 | — | — |
| ${}^{193}$Pb | 193 | 111 | L?-pending | pending | binding_energy | — | 1515.8412 | — | — |
| ${}^{194}$Pb | 194 | 112 | L?-pending | pending | binding_energy | — | 1525.8911 | — | — |
| ${}^{195}$Pb | 195 | 113 | L?-pending | pending | binding_energy | — | 1533.4926 | — | — |
| ${}^{196}$Pb | 196 | 114 | L?-pending | pending | binding_energy | — | 1543.1741 | — | — |
| ${}^{197}$Pb | 197 | 115 | L?-pending | pending | binding_energy | — | 1550.6426 | — | — |
| ${}^{198}$Pb | 198 | 116 | L?-pending | pending | binding_energy | — | 1560.0360 | — | — |
| ${}^{199}$Pb | 199 | 117 | L?-pending | pending | binding_energy | — | 1567.2716 | — | — |
| ${}^{200}$Pb | 200 | 118 | L?-pending | pending | binding_energy | — | 1576.3620 | — | — |
| ${}^{201}$Pb | 201 | 119 | L?-pending | pending | binding_energy | — | 1583.4535 | — | — |
| ${}^{202}$Pb | 202 | 120 | L?-pending | pending | binding_energy | — | 1592.1944 | — | — |
| ${}^{203}$Pb | 203 | 121 | L?-pending | pending | binding_energy | — | 1599.1116 | — | — |
| ${}^{204}$Pb | 204 | 122 | L?-pending | pending | binding_energy | — | 1607.5063 | — | — |
| ${}^{205}$Pb | 205 | 123 | L?-pending | pending | binding_energy | — | 1614.2379 | — | — |
| ${}^{206}$Pb | 206 | 124 | L?-pending | pending | binding_energy | — | 1622.3246 | — | — |
| ${}^{207}$Pb | 207 | 125 | L?-pending | pending | binding_energy | — | 1629.0623 | — | — |
| ${}^{208}$Pb | 208 | 126 | L?-pending | pending | binding_energy | — | 1636.4302 | — | — |
| ${}^{209}$Pb | 209 | 127 | L?-pending | pending | binding_energy | — | 1640.3676 | — | — |
| ${}^{210}$Pb | 210 | 128 | L?-pending | pending | binding_energy | — | 1645.5528 | — | — |
| ${}^{211}$Pb | 211 | 129 | L?-pending | pending | binding_energy | — | 1649.3887 | — | — |
| ${}^{212}$Pb | 212 | 130 | L?-pending | pending | binding_energy | — | 1654.5159 | — | — |
| ${}^{213}$Pb | 213 | 131 | L?-pending | pending | binding_energy | — | 1658.2419 | — | — |
| ${}^{214}$Pb | 214 | 132 | L?-pending | pending | binding_energy | — | 1663.2926 | — | — |
| ${}^{215}$Pb | 215 | 133 | L?-pending | pending | binding_energy | — | 1666.8387 | — | — |
| ${}^{216}$Pb | 216 | 134 | L?-pending | pending | binding_energy | — | 1671.8400 | — | — |
| ${}^{217}$Pb | 217 | 135 | L?-pending | pending | binding_energy | — | 1675.0230 | — | — |
| ${}^{218}$Pb | 218 | 136 | L?-pending | pending | binding_energy | — | 1679.6900 | — | — |
| ${}^{219}$Pb | 219 | 137 | L?-pending | pending | binding_energy | — | 1682.7960 | — | — |
| ${}^{220}$Pb | 220 | 138 | L?-pending | pending | binding_energy | — | 1687.4000 | — | — |

### Bismuth (Z = 83)

_0 of 41 isotopes with a framework prediction; 0 of 41 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{184}$Bi | 184 | 101 | L?-pending | pending | binding_energy | — | 1419.0080 | — | — |
| ${}^{185}$Bi | 185 | 102 | L?-pending | pending | binding_energy | — | 1430.4200 | — | — |
| ${}^{186}$Bi | 186 | 103 | L?-pending | pending | binding_energy | — | 1439.4759 | — | — |
| ${}^{187}$Bi | 187 | 104 | L?-pending | pending | binding_energy | — | 1450.7850 | — | — |
| ${}^{188}$Bi | 188 | 105 | L?-pending | pending | binding_energy | — | 1459.6678 | — | — |
| ${}^{189}$Bi | 189 | 106 | L?-pending | pending | binding_energy | — | 1470.6090 | — | — |
| ${}^{190}$Bi | 190 | 107 | L?-pending | pending | binding_energy | — | 1479.2115 | — | — |
| ${}^{191}$Bi | 191 | 108 | L?-pending | pending | binding_energy | — | 1489.9263 | — | — |
| ${}^{192}$Bi | 192 | 109 | L?-pending | pending | binding_energy | — | 1498.2928 | — | — |
| ${}^{193}$Bi | 193 | 110 | L?-pending | pending | binding_energy | — | 1508.7142 | — | — |
| ${}^{194}$Bi | 194 | 111 | L?-pending | pending | binding_energy | — | 1516.9239 | — | — |
| ${}^{195}$Bi | 195 | 112 | L?-pending | pending | binding_energy | — | 1526.9978 | — | — |
| ${}^{196}$Bi | 196 | 113 | L?-pending | pending | binding_energy | — | 1535.0526 | — | — |
| ${}^{197}$Bi | 197 | 114 | L?-pending | pending | binding_energy | — | 1544.8021 | — | — |
| ${}^{198}$Bi | 198 | 115 | L?-pending | pending | binding_energy | — | 1552.5600 | — | — |
| ${}^{199}$Bi | 199 | 116 | L?-pending | pending | binding_energy | — | 1562.0551 | — | — |
| ${}^{200}$Bi | 200 | 117 | L?-pending | pending | binding_energy | — | 1569.6994 | — | — |
| ${}^{201}$Bi | 201 | 118 | L?-pending | pending | binding_energy | — | 1578.8291 | — | — |
| ${}^{202}$Bi | 202 | 119 | L?-pending | pending | binding_energy | — | 1586.2223 | — | — |
| ${}^{203}$Bi | 203 | 120 | L?-pending | pending | binding_energy | — | 1595.0677 | — | — |
| ${}^{204}$Bi | 204 | 121 | L?-pending | pending | binding_energy | — | 1602.2600 | — | — |
| ${}^{205}$Bi | 205 | 122 | L?-pending | pending | binding_energy | — | 1610.7510 | — | — |
| ${}^{206}$Bi | 206 | 123 | L?-pending | pending | binding_energy | — | 1617.7849 | — | — |
| ${}^{207}$Bi | 207 | 124 | L?-pending | pending | binding_energy | — | 1625.8826 | — | — |
| ${}^{208}$Bi | 208 | 125 | L?-pending | pending | binding_energy | — | 1632.7695 | — | — |
| ${}^{209}$Bi | 209 | 126 | L?-pending | pending | binding_energy | — | 1640.2293 | — | — |
| ${}^{210}$Bi | 210 | 127 | L?-pending | pending | binding_energy | — | 1644.8339 | — | — |
| ${}^{211}$Bi | 211 | 128 | L?-pending | pending | binding_energy | — | 1649.9724 | — | — |
| ${}^{212}$Bi | 212 | 129 | L?-pending | pending | binding_energy | — | 1654.3026 | — | — |
| ${}^{213}$Bi | 213 | 130 | L?-pending | pending | binding_energy | — | 1659.4876 | — | — |
| ${}^{214}$Bi | 214 | 131 | L?-pending | pending | binding_energy | — | 1663.5280 | — | — |
| ${}^{215}$Bi | 215 | 132 | L?-pending | pending | binding_energy | — | 1668.7693 | — | — |
| ${}^{216}$Bi | 216 | 133 | L?-pending | pending | binding_energy | — | 1672.5959 | — | — |
| ${}^{217}$Bi | 217 | 134 | L?-pending | pending | binding_energy | — | 1677.8113 | — | — |
| ${}^{218}$Bi | 218 | 135 | L?-pending | pending | binding_energy | — | 1681.3965 | — | — |
| ${}^{219}$Bi | 219 | 136 | L?-pending | pending | binding_energy | — | 1686.3000 | — | — |
| ${}^{220}$Bi | 220 | 137 | L?-pending | pending | binding_energy | — | 1689.8200 | — | — |
| ${}^{221}$Bi | 221 | 138 | L?-pending | pending | binding_energy | — | 1694.6280 | — | — |
| ${}^{222}$Bi | 222 | 139 | L?-pending | pending | binding_energy | — | 1697.8560 | — | — |
| ${}^{223}$Bi | 223 | 140 | L?-pending | pending | binding_energy | — | 1702.8280 | — | — |
| ${}^{224}$Bi | 224 | 141 | L?-pending | pending | binding_energy | — | 1705.9840 | — | — |

### Polonium (Z = 84)

_0 of 42 isotopes with a framework prediction; 0 of 42 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{186}$Po | 186 | 102 | L?-pending | pending | binding_energy | — | 1431.4465 | — | — |
| ${}^{187}$Po | 187 | 103 | L?-pending | pending | binding_energy | — | 1440.7955 | — | — |
| ${}^{188}$Po | 188 | 104 | L?-pending | pending | binding_energy | — | 1452.2350 | — | — |
| ${}^{189}$Po | 189 | 105 | L?-pending | pending | binding_energy | — | 1461.1840 | — | — |
| ${}^{190}$Po | 190 | 106 | L?-pending | pending | binding_energy | — | 1472.3960 | — | — |
| ${}^{191}$Po | 191 | 107 | L?-pending | pending | binding_energy | — | 1480.9733 | — | — |
| ${}^{192}$Po | 192 | 108 | L?-pending | pending | binding_energy | — | 1492.0424 | — | — |
| ${}^{193}$Po | 193 | 109 | L?-pending | pending | binding_energy | — | 1500.3725 | — | — |
| ${}^{194}$Po | 194 | 110 | L?-pending | pending | binding_energy | — | 1511.1232 | — | — |
| ${}^{195}$Po | 195 | 111 | L?-pending | pending | binding_energy | — | 1519.3065 | — | — |
| ${}^{196}$Po | 196 | 112 | L?-pending | pending | binding_energy | — | 1529.7299 | — | — |
| ${}^{197}$Po | 197 | 113 | L?-pending | pending | binding_energy | — | 1537.7256 | — | — |
| ${}^{198}$Po | 198 | 114 | L?-pending | pending | binding_energy | — | 1547.8771 | — | — |
| ${}^{199}$Po | 199 | 115 | L?-pending | pending | binding_energy | — | 1555.7140 | — | — |
| ${}^{200}$Po | 200 | 116 | L?-pending | pending | binding_energy | — | 1565.4881 | — | — |
| ${}^{201}$Po | 201 | 117 | L?-pending | pending | binding_energy | — | 1573.1389 | — | — |
| ${}^{202}$Po | 202 | 118 | L?-pending | pending | binding_energy | — | 1582.6307 | — | — |
| ${}^{203}$Po | 203 | 119 | L?-pending | pending | binding_energy | — | 1590.0712 | — | — |
| ${}^{204}$Po | 204 | 120 | L?-pending | pending | binding_energy | — | 1599.1728 | — | — |
| ${}^{205}$Po | 205 | 121 | L?-pending | pending | binding_energy | — | 1606.4244 | — | — |
| ${}^{206}$Po | 206 | 122 | L?-pending | pending | binding_energy | — | 1615.1630 | — | — |
| ${}^{207}$Po | 207 | 123 | L?-pending | pending | binding_energy | — | 1622.1914 | — | — |
| ${}^{208}$Po | 208 | 124 | L?-pending | pending | binding_energy | — | 1630.5862 | — | — |
| ${}^{209}$Po | 209 | 125 | L?-pending | pending | binding_energy | — | 1637.5543 | — | — |
| ${}^{210}$Po | 210 | 126 | L?-pending | pending | binding_energy | — | 1645.2127 | — | — |
| ${}^{211}$Po | 211 | 127 | L?-pending | pending | binding_energy | — | 1649.7635 | — | — |
| ${}^{212}$Po | 212 | 128 | L?-pending | pending | binding_energy | — | 1655.7717 | — | — |
| ${}^{213}$Po | 213 | 129 | L?-pending | pending | binding_energy | — | 1660.1271 | — | — |
| ${}^{214}$Po | 214 | 130 | L?-pending | pending | binding_energy | — | 1666.0149 | — | — |
| ${}^{215}$Po | 215 | 131 | L?-pending | pending | binding_energy | — | 1670.1580 | — | — |
| ${}^{216}$Po | 216 | 132 | L?-pending | pending | binding_energy | — | 1675.9052 | — | — |
| ${}^{217}$Po | 217 | 133 | L?-pending | pending | binding_energy | — | 1679.8754 | — | — |
| ${}^{218}$Po | 218 | 134 | L?-pending | pending | binding_energy | — | 1685.4735 | — | — |
| ${}^{219}$Po | 219 | 135 | L?-pending | pending | binding_energy | — | 1689.2201 | — | — |
| ${}^{220}$Po | 220 | 136 | L?-pending | pending | binding_energy | — | 1694.7094 | — | — |
| ${}^{221}$Po | 221 | 137 | L?-pending | pending | binding_energy | — | 1698.2704 | — | — |
| ${}^{222}$Po | 222 | 138 | L?-pending | pending | binding_energy | — | 1703.6292 | — | — |
| ${}^{223}$Po | 223 | 139 | L?-pending | pending | binding_energy | — | 1707.0650 | — | — |
| ${}^{224}$Po | 224 | 140 | L?-pending | pending | binding_energy | — | 1712.2560 | — | — |
| ${}^{225}$Po | 225 | 141 | L?-pending | pending | binding_energy | — | 1715.8500 | — | — |
| ${}^{226}$Po | 226 | 142 | L?-pending | pending | binding_energy | — | 1720.7640 | — | — |
| ${}^{227}$Po | 227 | 143 | L?-pending | pending | binding_energy | — | 1724.2920 | — | — |

### Astatine (Z = 85)

_0 of 39 isotopes with a framework prediction; 0 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{191}$At | 191 | 106 | L?-pending | pending | binding_energy | — | 1471.2584 | — | — |
| ${}^{192}$At | 192 | 107 | L?-pending | pending | binding_energy | — | 1480.2678 | — | — |
| ${}^{193}$At | 193 | 108 | L?-pending | pending | binding_energy | — | 1491.3322 | — | — |
| ${}^{194}$At | 194 | 109 | L?-pending | pending | binding_energy | — | 1500.0527 | — | — |
| ${}^{195}$At | 195 | 110 | L?-pending | pending | binding_energy | — | 1510.8778 | — | — |
| ${}^{196}$At | 196 | 111 | L?-pending | pending | binding_energy | — | 1519.3920 | — | — |
| ${}^{197}$At | 197 | 112 | L?-pending | pending | binding_energy | — | 1529.9054 | — | — |
| ${}^{198}$At | 198 | 113 | L?-pending | pending | binding_energy | — | 1538.3302 | — | — |
| ${}^{199}$At | 199 | 114 | L?-pending | pending | binding_energy | — | 1548.5162 | — | — |
| ${}^{200}$At | 200 | 115 | L?-pending | pending | binding_energy | — | 1556.7520 | — | — |
| ${}^{201}$At | 201 | 116 | L?-pending | pending | binding_energy | — | 1566.6249 | — | — |
| ${}^{202}$At | 202 | 117 | L?-pending | pending | binding_energy | — | 1574.5019 | — | — |
| ${}^{203}$At | 203 | 118 | L?-pending | pending | binding_energy | — | 1584.1407 | — | — |
| ${}^{204}$At | 204 | 119 | L?-pending | pending | binding_energy | — | 1591.9246 | — | — |
| ${}^{205}$At | 205 | 120 | L?-pending | pending | binding_energy | — | 1601.1052 | — | — |
| ${}^{206}$At | 206 | 121 | L?-pending | pending | binding_energy | — | 1608.6314 | — | — |
| ${}^{207}$At | 207 | 122 | L?-pending | pending | binding_energy | — | 1617.4908 | — | — |
| ${}^{208}$At | 208 | 123 | L?-pending | pending | binding_energy | — | 1624.8046 | — | — |
| ${}^{209}$At | 209 | 124 | L?-pending | pending | binding_energy | — | 1633.2898 | — | — |
| ${}^{210}$At | 210 | 125 | L?-pending | pending | binding_energy | — | 1640.4494 | — | — |
| ${}^{211}$At | 211 | 126 | L?-pending | pending | binding_energy | — | 1648.1958 | — | — |
| ${}^{212}$At | 212 | 127 | L?-pending | pending | binding_energy | — | 1653.2481 | — | — |
| ${}^{213}$At | 213 | 128 | L?-pending | pending | binding_energy | — | 1659.2708 | — | — |
| ${}^{214}$At | 214 | 129 | L?-pending | pending | binding_energy | — | 1664.1417 | — | — |
| ${}^{215}$At | 215 | 130 | L?-pending | pending | binding_energy | — | 1670.0905 | — | — |
| ${}^{216}$At | 216 | 131 | L?-pending | pending | binding_energy | — | 1674.6485 | — | — |
| ${}^{217}$At | 217 | 132 | L?-pending | pending | binding_energy | — | 1680.5819 | — | — |
| ${}^{218}$At | 218 | 133 | L?-pending | pending | binding_energy | — | 1684.9476 | — | — |
| ${}^{219}$At | 219 | 134 | L?-pending | pending | binding_energy | — | 1690.7231 | — | — |
| ${}^{220}$At | 220 | 135 | L?-pending | pending | binding_energy | — | 1694.8147 | — | — |
| ${}^{221}$At | 221 | 136 | L?-pending | pending | binding_energy | — | 1700.4791 | — | — |
| ${}^{222}$At | 222 | 137 | L?-pending | pending | binding_energy | — | 1704.3801 | — | — |
| ${}^{223}$At | 223 | 138 | L?-pending | pending | binding_energy | — | 1709.9764 | — | — |
| ${}^{224}$At | 224 | 139 | L?-pending | pending | binding_energy | — | 1713.7647 | — | — |
| ${}^{225}$At | 225 | 140 | L?-pending | pending | binding_energy | — | 1719.2250 | — | — |
| ${}^{226}$At | 226 | 141 | L?-pending | pending | binding_energy | — | 1723.0240 | — | — |
| ${}^{227}$At | 227 | 142 | L?-pending | pending | binding_energy | — | 1728.1510 | — | — |
| ${}^{228}$At | 228 | 143 | L?-pending | pending | binding_energy | — | 1731.8880 | — | — |
| ${}^{229}$At | 229 | 144 | L?-pending | pending | binding_energy | — | 1736.9650 | — | — |

### Radon (Z = 86)

_0 of 39 isotopes with a framework prediction; 0 of 39 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{193}$Rn | 193 | 107 | L?-pending | pending | binding_energy | — | 1481.4396 | — | — |
| ${}^{194}$Rn | 194 | 108 | L?-pending | pending | binding_energy | — | 1492.8292 | — | — |
| ${}^{195}$Rn | 195 | 109 | L?-pending | pending | binding_energy | — | 1501.5749 | — | — |
| ${}^{196}$Rn | 196 | 110 | L?-pending | pending | binding_energy | — | 1512.7213 | — | — |
| ${}^{197}$Rn | 197 | 111 | L?-pending | pending | binding_energy | — | 1521.2574 | — | — |
| ${}^{198}$Rn | 198 | 112 | L?-pending | pending | binding_energy | — | 1532.0695 | — | — |
| ${}^{199}$Rn | 199 | 113 | L?-pending | pending | binding_energy | — | 1540.4703 | — | — |
| ${}^{200}$Rn | 200 | 114 | L?-pending | pending | binding_energy | — | 1550.9822 | — | — |
| ${}^{201}$Rn | 201 | 115 | L?-pending | pending | binding_energy | — | 1559.1605 | — | — |
| ${}^{202}$Rn | 202 | 116 | L?-pending | pending | binding_energy | — | 1569.3990 | — | — |
| ${}^{203}$Rn | 203 | 117 | L?-pending | pending | binding_energy | — | 1577.3798 | — | — |
| ${}^{204}$Rn | 204 | 118 | L?-pending | pending | binding_energy | — | 1587.2372 | — | — |
| ${}^{205}$Rn | 205 | 119 | L?-pending | pending | binding_energy | — | 1595.0481 | — | — |
| ${}^{206}$Rn | 206 | 120 | L?-pending | pending | binding_energy | — | 1604.5426 | — | — |
| ${}^{207}$Rn | 207 | 121 | L?-pending | pending | binding_energy | — | 1612.1157 | — | — |
| ${}^{208}$Rn | 208 | 122 | L?-pending | pending | binding_energy | — | 1621.2077 | — | — |
| ${}^{209}$Rn | 209 | 123 | L?-pending | pending | binding_energy | — | 1628.5647 | — | — |
| ${}^{210}$Rn | 210 | 124 | L?-pending | pending | binding_energy | — | 1637.2997 | — | — |
| ${}^{211}$Rn | 211 | 125 | L?-pending | pending | binding_energy | — | 1644.5216 | — | — |
| ${}^{212}$Rn | 212 | 126 | L?-pending | pending | binding_energy | — | 1652.4968 | — | — |
| ${}^{213}$Rn | 213 | 127 | L?-pending | pending | binding_energy | — | 1657.6049 | — | — |
| ${}^{214}$Rn | 214 | 128 | L?-pending | pending | binding_energy | — | 1664.2999 | — | — |
| ${}^{215}$Rn | 215 | 129 | L?-pending | pending | binding_energy | — | 1669.2205 | — | — |
| ${}^{216}$Rn | 216 | 130 | L?-pending | pending | binding_energy | — | 1675.8695 | — | — |
| ${}^{217}$Rn | 217 | 131 | L?-pending | pending | binding_energy | — | 1680.5356 | — | — |
| ${}^{218}$Rn | 218 | 132 | L?-pending | pending | binding_energy | — | 1687.0481 | — | — |
| ${}^{219}$Rn | 219 | 133 | L?-pending | pending | binding_energy | — | 1691.5075 | — | — |
| ${}^{220}$Rn | 220 | 134 | L?-pending | pending | binding_energy | — | 1697.7961 | — | — |
| ${}^{221}$Rn | 221 | 135 | L?-pending | pending | binding_energy | — | 1702.0081 | — | — |
| ${}^{222}$Rn | 222 | 136 | L?-pending | pending | binding_energy | — | 1708.1788 | — | — |
| ${}^{223}$Rn | 223 | 137 | L?-pending | pending | binding_energy | — | 1712.2324 | — | — |
| ${}^{224}$Rn | 224 | 138 | L?-pending | pending | binding_energy | — | 1718.2483 | — | — |
| ${}^{225}$Rn | 225 | 139 | L?-pending | pending | binding_energy | — | 1722.2306 | — | — |
| ${}^{226}$Rn | 226 | 140 | L?-pending | pending | binding_energy | — | 1728.0888 | — | — |
| ${}^{227}$Rn | 227 | 141 | L?-pending | pending | binding_energy | — | 1732.0215 | — | — |
| ${}^{228}$Rn | 228 | 142 | L?-pending | pending | binding_energy | — | 1737.7352 | — | — |
| ${}^{229}$Rn | 229 | 143 | L?-pending | pending | binding_energy | — | 1741.6876 | — | — |
| ${}^{230}$Rn | 230 | 144 | L?-pending | pending | binding_energy | — | 1746.8500 | — | — |
| ${}^{231}$Rn | 231 | 145 | L?-pending | pending | binding_energy | — | 1750.7490 | — | — |

### Francium (Z = 87)

_0 of 37 isotopes with a framework prediction; 0 of 37 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{197}$Fr | 197 | 110 | L?-pending | pending | binding_energy | — | 1511.7315 | — | — |
| ${}^{198}$Fr | 198 | 111 | L?-pending | pending | binding_energy | — | 1520.4791 | — | — |
| ${}^{199}$Fr | 199 | 112 | L?-pending | pending | binding_energy | — | 1531.3567 | — | — |
| ${}^{200}$Fr | 200 | 113 | L?-pending | pending | binding_energy | — | 1540.0658 | — | — |
| ${}^{201}$Fr | 201 | 114 | L?-pending | pending | binding_energy | — | 1550.6822 | — | — |
| ${}^{202}$Fr | 202 | 115 | L?-pending | pending | binding_energy | — | 1559.2405 | — | — |
| ${}^{203}$Fr | 203 | 116 | L?-pending | pending | binding_energy | — | 1569.5370 | — | — |
| ${}^{204}$Fr | 204 | 117 | L?-pending | pending | binding_energy | — | 1577.8774 | — | — |
| ${}^{205}$Fr | 205 | 118 | L?-pending | pending | binding_energy | — | 1587.8658 | — | — |
| ${}^{206}$Fr | 206 | 119 | L?-pending | pending | binding_energy | — | 1595.8742 | — | — |
| ${}^{207}$Fr | 207 | 120 | L?-pending | pending | binding_energy | — | 1605.5477 | — | — |
| ${}^{208}$Fr | 208 | 121 | L?-pending | pending | binding_energy | — | 1613.4349 | — | — |
| ${}^{209}$Fr | 209 | 122 | L?-pending | pending | binding_energy | — | 1622.6234 | — | — |
| ${}^{210}$Fr | 210 | 123 | L?-pending | pending | binding_energy | — | 1630.2561 | — | — |
| ${}^{211}$Fr | 211 | 124 | L?-pending | pending | binding_energy | — | 1639.1242 | — | — |
| ${}^{212}$Fr | 212 | 125 | L?-pending | pending | binding_energy | — | 1646.5712 | — | — |
| ${}^{213}$Fr | 213 | 126 | L?-pending | pending | binding_energy | — | 1654.6808 | — | — |
| ${}^{214}$Fr | 214 | 127 | L?-pending | pending | binding_energy | — | 1660.1562 | — | — |
| ${}^{215}$Fr | 215 | 128 | L?-pending | pending | binding_energy | — | 1666.9511 | — | — |
| ${}^{216}$Fr | 216 | 129 | L?-pending | pending | binding_energy | — | 1672.3695 | — | — |
| ${}^{217}$Fr | 217 | 130 | L?-pending | pending | binding_energy | — | 1679.0972 | — | — |
| ${}^{218}$Fr | 218 | 131 | L?-pending | pending | binding_energy | — | 1684.4237 | — | — |
| ${}^{219}$Fr | 219 | 132 | L?-pending | pending | binding_energy | — | 1690.9375 | — | — |
| ${}^{220}$Fr | 220 | 133 | L?-pending | pending | binding_energy | — | 1696.1435 | — | — |
| ${}^{221}$Fr | 221 | 134 | L?-pending | pending | binding_energy | — | 1702.4198 | — | — |
| ${}^{222}$Fr | 222 | 135 | L?-pending | pending | binding_energy | — | 1707.3903 | — | — |
| ${}^{223}$Fr | 223 | 136 | L?-pending | pending | binding_energy | — | 1713.4574 | — | — |
| ${}^{224}$Fr | 224 | 137 | L?-pending | pending | binding_energy | — | 1718.1624 | — | — |
| ${}^{225}$Fr | 225 | 138 | L?-pending | pending | binding_energy | — | 1724.1618 | — | — |
| ${}^{226}$Fr | 226 | 139 | L?-pending | pending | binding_energy | — | 1728.5332 | — | — |
| ${}^{227}$Fr | 227 | 140 | L?-pending | pending | binding_energy | — | 1734.4426 | — | — |
| ${}^{228}$Fr | 228 | 141 | L?-pending | pending | binding_energy | — | 1738.8121 | — | — |
| ${}^{229}$Fr | 229 | 142 | L?-pending | pending | binding_energy | — | 1744.5994 | — | — |
| ${}^{230}$Fr | 230 | 143 | L?-pending | pending | binding_energy | — | 1748.8522 | — | — |
| ${}^{231}$Fr | 231 | 144 | L?-pending | pending | binding_energy | — | 1754.3297 | — | — |
| ${}^{232}$Fr | 232 | 145 | L?-pending | pending | binding_energy | — | 1758.4088 | — | — |
| ${}^{233}$Fr | 233 | 146 | L?-pending | pending | binding_energy | — | 1763.6329 | — | — |

### Radium (Z = 88)

_0 of 35 isotopes with a framework prediction; 0 of 35 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{201}$Ra | 201 | 113 | L?-pending | pending | binding_energy | — | 1541.5516 | — | — |
| ${}^{202}$Ra | 202 | 114 | L?-pending | pending | binding_energy | — | 1552.4848 | — | — |
| ${}^{203}$Ra | 203 | 115 | L?-pending | pending | binding_energy | — | 1561.0297 | — | — |
| ${}^{204}$Ra | 204 | 116 | L?-pending | pending | binding_energy | — | 1571.6413 | — | — |
| ${}^{205}$Ra | 205 | 117 | L?-pending | pending | binding_energy | — | 1579.9698 | — | — |
| ${}^{206}$Ra | 206 | 118 | L?-pending | pending | binding_energy | — | 1590.2794 | — | — |
| ${}^{207}$Ra | 207 | 119 | L?-pending | pending | binding_energy | — | 1598.4023 | — | — |
| ${}^{208}$Ra | 208 | 120 | L?-pending | pending | binding_energy | — | 1608.2597 | — | — |
| ${}^{209}$Ra | 209 | 121 | L?-pending | pending | binding_energy | — | 1616.2007 | — | — |
| ${}^{210}$Ra | 210 | 122 | L?-pending | pending | binding_energy | — | 1625.6874 | — | — |
| ${}^{211}$Ra | 211 | 123 | L?-pending | pending | binding_energy | — | 1633.3697 | — | — |
| ${}^{212}$Ra | 212 | 124 | L?-pending | pending | binding_energy | — | 1642.4717 | — | — |
| ${}^{213}$Ra | 213 | 125 | L?-pending | pending | binding_energy | — | 1649.9987 | — | — |
| ${}^{214}$Ra | 214 | 126 | L?-pending | pending | binding_energy | — | 1658.3228 | — | — |
| ${}^{215}$Ra | 215 | 127 | L?-pending | pending | binding_energy | — | 1663.9549 | — | — |
| ${}^{216}$Ra | 216 | 128 | L?-pending | pending | binding_energy | — | 1671.2667 | — | — |
| ${}^{217}$Ra | 217 | 129 | L?-pending | pending | binding_energy | — | 1676.7399 | — | — |
| ${}^{218}$Ra | 218 | 130 | L?-pending | pending | binding_energy | — | 1684.0553 | — | — |
| ${}^{219}$Ra | 219 | 131 | L?-pending | pending | binding_energy | — | 1689.3783 | — | — |
| ${}^{220}$Ra | 220 | 132 | L?-pending | pending | binding_energy | — | 1696.5713 | — | — |
| ${}^{221}$Ra | 221 | 133 | L?-pending | pending | binding_energy | — | 1701.9509 | — | — |
| ${}^{222}$Ra | 222 | 134 | L?-pending | pending | binding_energy | — | 1708.6659 | — | — |
| ${}^{223}$Ra | 223 | 135 | L?-pending | pending | binding_energy | — | 1713.8242 | — | — |
| ${}^{224}$Ra | 224 | 136 | L?-pending | pending | binding_energy | — | 1720.3029 | — | — |
| ${}^{225}$Ra | 225 | 137 | L?-pending | pending | binding_energy | — | 1725.2070 | — | — |
| ${}^{226}$Ra | 226 | 138 | L?-pending | pending | binding_energy | — | 1731.6038 | — | — |
| ${}^{227}$Ra | 227 | 139 | L?-pending | pending | binding_energy | — | 1736.1652 | — | — |
| ${}^{228}$Ra | 228 | 140 | L?-pending | pending | binding_energy | — | 1742.4738 | — | — |
| ${}^{229}$Ra | 229 | 141 | L?-pending | pending | binding_energy | — | 1746.9233 | — | — |
| ${}^{230}$Ra | 230 | 142 | L?-pending | pending | binding_energy | — | 1753.0403 | — | — |
| ${}^{231}$Ra | 231 | 143 | L?-pending | pending | binding_energy | — | 1757.4115 | — | — |
| ${}^{232}$Ra | 232 | 144 | L?-pending | pending | binding_energy | — | 1763.2023 | — | — |
| ${}^{233}$Ra | 233 | 145 | L?-pending | pending | binding_energy | — | 1767.4365 | — | — |
| ${}^{234}$Ra | 234 | 146 | L?-pending | pending | binding_energy | — | 1772.9113 | — | — |
| ${}^{235}$Ra | 235 | 147 | L?-pending | pending | binding_energy | — | 1776.8350 | — | — |

### Actinium (Z = 89)

_0 of 33 isotopes with a framework prediction; 0 of 33 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{205}$Ac | 205 | 116 | L?-pending | pending | binding_energy | — | 1570.8846 | — | — |
| ${}^{206}$Ac | 206 | 117 | L?-pending | pending | binding_energy | — | 1579.5779 | — | — |
| ${}^{207}$Ac | 207 | 118 | L?-pending | pending | binding_energy | — | 1589.9877 | — | — |
| ${}^{208}$Ac | 208 | 119 | L?-pending | pending | binding_energy | — | 1598.4444 | — | — |
| ${}^{209}$Ac | 209 | 120 | L?-pending | pending | binding_energy | — | 1608.4317 | — | — |
| ${}^{210}$Ac | 210 | 121 | L?-pending | pending | binding_energy | — | 1616.5838 | — | — |
| ${}^{211}$Ac | 211 | 122 | L?-pending | pending | binding_energy | — | 1626.2757 | — | — |
| ${}^{212}$Ac | 212 | 123 | L?-pending | pending | binding_energy | — | 1634.1910 | — | — |
| ${}^{213}$Ac | 213 | 124 | L?-pending | pending | binding_energy | — | 1643.4208 | — | — |
| ${}^{214}$Ac | 214 | 125 | L?-pending | pending | binding_energy | — | 1651.1999 | — | — |
| ${}^{215}$Ac | 215 | 126 | L?-pending | pending | binding_energy | — | 1659.6739 | — | — |
| ${}^{216}$Ac | 216 | 127 | L?-pending | pending | binding_energy | — | 1665.6261 | — | — |
| ${}^{217}$Ac | 217 | 128 | L?-pending | pending | binding_energy | — | 1673.1448 | — | — |
| ${}^{218}$Ac | 218 | 129 | L?-pending | pending | binding_energy | — | 1679.0676 | — | — |
| ${}^{219}$Ac | 219 | 130 | L?-pending | pending | binding_energy | — | 1686.4202 | — | — |
| ${}^{220}$Ac | 220 | 131 | L?-pending | pending | binding_energy | — | 1692.3173 | — | — |
| ${}^{221}$Ac | 221 | 132 | L?-pending | pending | binding_energy | — | 1699.6014 | — | — |
| ${}^{222}$Ac | 222 | 133 | L?-pending | pending | binding_energy | — | 1705.5819 | — | — |
| ${}^{223}$Ac | 223 | 134 | L?-pending | pending | binding_energy | — | 1712.4500 | — | — |
| ${}^{224}$Ac | 224 | 135 | L?-pending | pending | binding_energy | — | 1718.1122 | — | — |
| ${}^{225}$Ac | 225 | 136 | L?-pending | pending | binding_energy | — | 1724.7804 | — | — |
| ${}^{226}$Ac | 226 | 137 | L?-pending | pending | binding_energy | — | 1730.1798 | — | — |
| ${}^{227}$Ac | 227 | 138 | L?-pending | pending | binding_energy | — | 1736.7108 | — | — |
| ${}^{228}$Ac | 228 | 139 | L?-pending | pending | binding_energy | — | 1741.7370 | — | — |
| ${}^{229}$Ac | 229 | 140 | L?-pending | pending | binding_energy | — | 1748.0130 | — | — |
| ${}^{230}$Ac | 230 | 141 | L?-pending | pending | binding_energy | — | 1752.9359 | — | — |
| ${}^{231}$Ac | 231 | 142 | L?-pending | pending | binding_energy | — | 1759.0827 | — | — |
| ${}^{232}$Ac | 232 | 143 | L?-pending | pending | binding_energy | — | 1763.7625 | — | — |
| ${}^{233}$Ac | 233 | 144 | L?-pending | pending | binding_energy | — | 1769.6802 | — | — |
| ${}^{234}$Ac | 234 | 145 | L?-pending | pending | binding_energy | — | 1774.2183 | — | — |
| ${}^{235}$Ac | 235 | 146 | L?-pending | pending | binding_energy | — | 1779.7737 | — | — |
| ${}^{236}$Ac | 236 | 147 | L?-pending | pending | binding_energy | — | 1783.9812 | — | — |
| ${}^{237}$Ac | 237 | 148 | L?-pending | pending | binding_energy | — | 1789.3500 | — | — |

### Thorium (Z = 90)

_0 of 32 isotopes with a framework prediction; 0 of 32 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{208}$Th | 208 | 118 | L?-pending | pending | binding_energy | — | 1591.7349 | — | — |
| ${}^{209}$Th | 209 | 119 | L?-pending | pending | binding_energy | — | 1600.1040 | — | — |
| ${}^{210}$Th | 210 | 120 | L?-pending | pending | binding_energy | — | 1610.5060 | — | — |
| ${}^{211}$Th | 211 | 121 | L?-pending | pending | binding_energy | — | 1618.7605 | — | — |
| ${}^{212}$Th | 212 | 122 | L?-pending | pending | binding_energy | — | 1628.5973 | — | — |
| ${}^{213}$Th | 213 | 123 | L?-pending | pending | binding_energy | — | 1636.6594 | — | — |
| ${}^{214}$Th | 214 | 124 | L?-pending | pending | binding_energy | — | 1646.1559 | — | — |
| ${}^{215}$Th | 215 | 125 | L?-pending | pending | binding_energy | — | 1654.0007 | — | — |
| ${}^{216}$Th | 216 | 126 | L?-pending | pending | binding_energy | — | 1662.6949 | — | — |
| ${}^{217}$Th | 217 | 127 | L?-pending | pending | binding_energy | — | 1668.8590 | — | — |
| ${}^{218}$Th | 218 | 128 | L?-pending | pending | binding_energy | — | 1676.7694 | — | — |
| ${}^{219}$Th | 219 | 129 | L?-pending | pending | binding_energy | — | 1682.7446 | — | — |
| ${}^{220}$Th | 220 | 130 | L?-pending | pending | binding_energy | — | 1690.5892 | — | — |
| ${}^{221}$Th | 221 | 131 | L?-pending | pending | binding_energy | — | 1696.4101 | — | — |
| ${}^{222}$Th | 222 | 132 | L?-pending | pending | binding_energy | — | 1704.2183 | — | — |
| ${}^{223}$Th | 223 | 133 | L?-pending | pending | binding_energy | — | 1710.1073 | — | — |
| ${}^{224}$Th | 224 | 134 | L?-pending | pending | binding_energy | — | 1717.5684 | — | — |
| ${}^{225}$Th | 225 | 135 | L?-pending | pending | binding_energy | — | 1723.3252 | — | — |
| ${}^{226}$Th | 226 | 136 | L?-pending | pending | binding_energy | — | 1730.5090 | — | — |
| ${}^{227}$Th | 227 | 137 | L?-pending | pending | binding_energy | — | 1735.9732 | — | — |
| ${}^{228}$Th | 228 | 138 | L?-pending | pending | binding_energy | — | 1743.0784 | — | — |
| ${}^{229}$Th | 229 | 139 | L?-pending | pending | binding_energy | — | 1748.3351 | — | — |
| ${}^{230}$Th | 230 | 140 | L?-pending | pending | binding_energy | — | 1755.1294 | — | — |
| ${}^{231}$Th | 231 | 141 | L?-pending | pending | binding_energy | — | 1760.2474 | — | — |
| ${}^{232}$Th | 232 | 142 | L?-pending | pending | binding_energy | — | 1766.6878 | — | — |
| ${}^{233}$Th | 233 | 143 | L?-pending | pending | binding_energy | — | 1771.4742 | — | — |
| ${}^{234}$Th | 234 | 144 | L?-pending | pending | binding_energy | — | 1777.6642 | — | — |
| ${}^{235}$Th | 235 | 145 | L?-pending | pending | binding_energy | — | 1782.3308 | — | — |
| ${}^{236}$Th | 236 | 146 | L?-pending | pending | binding_energy | — | 1788.1646 | — | — |
| ${}^{237}$Th | 237 | 147 | L?-pending | pending | binding_energy | — | 1792.5361 | — | — |
| ${}^{238}$Th | 238 | 148 | L?-pending | pending | binding_energy | — | 1798.0900 | — | — |
| ${}^{239}$Th | 239 | 149 | L?-pending | pending | binding_energy | — | 1802.0600 | — | — |

### Protactinium (Z = 91)

_0 of 31 isotopes with a framework prediction; 0 of 31 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{211}$Pa | 211 | 120 | L?-pending | pending | binding_energy | — | 1609.8023 | — | — |
| ${}^{212}$Pa | 212 | 121 | L?-pending | pending | binding_energy | — | 1618.3293 | — | — |
| ${}^{213}$Pa | 213 | 122 | L?-pending | pending | binding_energy | — | 1628.3430 | — | — |
| ${}^{214}$Pa | 214 | 123 | L?-pending | pending | binding_energy | — | 1636.6086 | — | — |
| ${}^{215}$Pa | 215 | 124 | L?-pending | pending | binding_energy | — | 1646.3353 | — | — |
| ${}^{216}$Pa | 216 | 125 | L?-pending | pending | binding_energy | — | 1654.3873 | — | — |
| ${}^{217}$Pa | 217 | 126 | L?-pending | pending | binding_energy | — | 1663.2277 | — | — |
| ${}^{218}$Pa | 218 | 127 | L?-pending | pending | binding_energy | — | 1669.7042 | — | — |
| ${}^{219}$Pa | 219 | 128 | L?-pending | pending | binding_energy | — | 1677.8418 | — | — |
| ${}^{220}$Pa | 220 | 129 | L?-pending | pending | binding_energy | — | 1684.2180 | — | — |
| ${}^{221}$Pa | 221 | 130 | L?-pending | pending | binding_energy | — | 1692.1928 | — | — |
| ${}^{222}$Pa | 222 | 131 | L?-pending | pending | binding_energy | — | 1698.5747 | — | — |
| ${}^{223}$Pa | 223 | 132 | L?-pending | pending | binding_energy | — | 1706.3727 | — | — |
| ${}^{224}$Pa | 224 | 133 | L?-pending | pending | binding_energy | — | 1712.9193 | — | — |
| ${}^{225}$Pa | 225 | 134 | L?-pending | pending | binding_energy | — | 1720.4963 | — | — |
| ${}^{226}$Pa | 226 | 135 | L?-pending | pending | binding_energy | — | 1726.8907 | — | — |
| ${}^{227}$Pa | 227 | 136 | L?-pending | pending | binding_energy | — | 1734.1653 | — | — |
| ${}^{228}$Pa | 228 | 137 | L?-pending | pending | binding_energy | — | 1740.1433 | — | — |
| ${}^{229}$Pa | 229 | 138 | L?-pending | pending | binding_energy | — | 1747.2414 | — | — |
| ${}^{230}$Pa | 230 | 139 | L?-pending | pending | binding_energy | — | 1753.0360 | — | — |
| ${}^{231}$Pa | 231 | 140 | L?-pending | pending | binding_energy | — | 1759.8566 | — | — |
| ${}^{232}$Pa | 232 | 141 | L?-pending | pending | binding_energy | — | 1765.4057 | — | — |
| ${}^{233}$Pa | 233 | 142 | L?-pending | pending | binding_energy | — | 1771.9341 | — | — |
| ${}^{234}$Pa | 234 | 143 | L?-pending | pending | binding_energy | — | 1777.1560 | — | — |
| ${}^{235}$Pa | 235 | 144 | L?-pending | pending | binding_energy | — | 1783.2773 | — | — |
| ${}^{236}$Pa | 236 | 145 | L?-pending | pending | binding_energy | — | 1788.3035 | — | — |
| ${}^{237}$Pa | 237 | 146 | L?-pending | pending | binding_energy | — | 1794.1812 | — | — |
| ${}^{238}$Pa | 238 | 147 | L?-pending | pending | binding_energy | — | 1798.8861 | — | — |
| ${}^{239}$Pa | 239 | 148 | L?-pending | pending | binding_energy | — | 1804.4500 | — | — |
| ${}^{240}$Pa | 240 | 149 | L?-pending | pending | binding_energy | — | 1808.8800 | — | — |
| ${}^{241}$Pa | 241 | 150 | L?-pending | pending | binding_energy | — | 1814.2480 | — | — |

### Uranium (Z = 92)

_0 of 29 isotopes with a framework prediction; 0 of 29 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{215}$U | 215 | 123 | L?-pending | pending | binding_energy | — | 1638.4682 | — | — |
| ${}^{216}$U | 216 | 124 | L?-pending | pending | binding_energy | — | 1648.3624 | — | — |
| ${}^{217}$U | 217 | 125 | L?-pending | pending | binding_energy | — | 1656.5780 | — | — |
| ${}^{218}$U | 218 | 126 | L?-pending | pending | binding_energy | — | 1665.6768 | — | — |
| ${}^{219}$U | 219 | 127 | L?-pending | pending | binding_energy | — | 1672.3468 | — | — |
| ${}^{220}$U | 220 | 128 | L?-pending | pending | binding_energy | — | 1680.8000 | — | — |
| ${}^{221}$U | 221 | 129 | L?-pending | pending | binding_energy | — | 1687.2654 | — | — |
| ${}^{222}$U | 222 | 130 | L?-pending | pending | binding_energy | — | 1695.5839 | — | — |
| ${}^{223}$U | 223 | 131 | L?-pending | pending | binding_energy | — | 1701.8827 | — | — |
| ${}^{224}$U | 224 | 132 | L?-pending | pending | binding_energy | — | 1710.2566 | — | — |
| ${}^{225}$U | 225 | 133 | L?-pending | pending | binding_energy | — | 1716.6986 | — | — |
| ${}^{226}$U | 226 | 134 | L?-pending | pending | binding_energy | — | 1724.8132 | — | — |
| ${}^{227}$U | 227 | 135 | L?-pending | pending | binding_energy | — | 1731.1682 | — | — |
| ${}^{228}$U | 228 | 136 | L?-pending | pending | binding_energy | — | 1739.0646 | — | — |
| ${}^{229}$U | 229 | 137 | L?-pending | pending | binding_energy | — | 1745.1453 | — | — |
| ${}^{230}$U | 230 | 138 | L?-pending | pending | binding_energy | — | 1752.8122 | — | — |
| ${}^{231}$U | 231 | 139 | L?-pending | pending | binding_energy | — | 1758.6926 | — | — |
| ${}^{232}$U | 232 | 140 | L?-pending | pending | binding_energy | — | 1765.9604 | — | — |
| ${}^{233}$U | 233 | 141 | L?-pending | pending | binding_energy | — | 1771.7221 | — | — |
| ${}^{234}$U | 234 | 142 | L?-pending | pending | binding_energy | — | 1778.5675 | — | — |
| ${}^{235}$U | 235 | 143 | L?-pending | pending | binding_energy | — | 1783.8650 | — | — |
| ${}^{236}$U | 236 | 144 | L?-pending | pending | binding_energy | — | 1790.4106 | — | — |
| ${}^{237}$U | 237 | 145 | L?-pending | pending | binding_energy | — | 1795.5363 | — | — |
| ${}^{238}$U | 238 | 146 | L?-pending | pending | binding_energy | — | 1801.6900 | — | — |
| ${}^{239}$U | 239 | 147 | L?-pending | pending | binding_energy | — | 1806.4964 | — | — |
| ${}^{240}$U | 240 | 148 | L?-pending | pending | binding_energy | — | 1812.4249 | — | — |
| ${}^{241}$U | 241 | 149 | L?-pending | pending | binding_energy | — | 1816.8990 | — | — |
| ${}^{242}$U | 242 | 150 | L?-pending | pending | binding_energy | — | 1822.7440 | — | — |
| ${}^{243}$U | 243 | 151 | L?-pending | pending | binding_energy | — | 1826.8740 | — | — |

### Neptunium (Z = 93)

_0 of 27 isotopes with a framework prediction; 0 of 27 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{219}$Np | 219 | 126 | L?-pending | pending | binding_energy | — | 1665.4234 | — | — |
| ${}^{220}$Np | 220 | 127 | L?-pending | pending | binding_energy | — | 1672.4567 | — | — |
| ${}^{221}$Np | 221 | 128 | L?-pending | pending | binding_energy | — | 1681.1470 | — | — |
| ${}^{222}$Np | 222 | 129 | L?-pending | pending | binding_energy | — | 1687.7997 | — | — |
| ${}^{223}$Np | 223 | 130 | L?-pending | pending | binding_energy | — | 1696.4871 | — | — |
| ${}^{224}$Np | 224 | 131 | L?-pending | pending | binding_energy | — | 1703.1847 | — | — |
| ${}^{225}$Np | 225 | 132 | L?-pending | pending | binding_energy | — | 1711.6702 | — | — |
| ${}^{226}$Np | 226 | 133 | L?-pending | pending | binding_energy | — | 1718.5427 | — | — |
| ${}^{227}$Np | 227 | 134 | L?-pending | pending | binding_energy | — | 1726.8519 | — | — |
| ${}^{228}$Np | 228 | 135 | L?-pending | pending | binding_energy | — | 1733.7120 | — | — |
| ${}^{229}$Np | 229 | 136 | L?-pending | pending | binding_energy | — | 1741.7722 | — | — |
| ${}^{230}$Np | 230 | 137 | L?-pending | pending | binding_energy | — | 1748.4083 | — | — |
| ${}^{231}$Np | 231 | 138 | L?-pending | pending | binding_energy | — | 1756.0925 | — | — |
| ${}^{232}$Np | 232 | 139 | L?-pending | pending | binding_energy | — | 1762.5040 | — | — |
| ${}^{233}$Np | 233 | 140 | L?-pending | pending | binding_energy | — | 1769.9103 | — | — |
| ${}^{234}$Np | 234 | 141 | L?-pending | pending | binding_energy | — | 1775.9753 | — | — |
| ${}^{235}$Np | 235 | 142 | L?-pending | pending | binding_energy | — | 1782.9584 | — | — |
| ${}^{236}$Np | 236 | 143 | L?-pending | pending | binding_energy | — | 1788.6947 | — | — |
| ${}^{237}$Np | 237 | 144 | L?-pending | pending | binding_energy | — | 1795.2725 | — | — |
| ${}^{238}$Np | 238 | 145 | L?-pending | pending | binding_energy | — | 1800.7608 | — | — |
| ${}^{239}$Np | 239 | 146 | L?-pending | pending | binding_energy | — | 1806.9758 | — | — |
| ${}^{240}$Np | 240 | 147 | L?-pending | pending | binding_energy | — | 1812.0418 | — | — |
| ${}^{241}$Np | 241 | 148 | L?-pending | pending | binding_energy | — | 1818.1143 | — | — |
| ${}^{242}$Np | 242 | 149 | L?-pending | pending | binding_energy | — | 1823.0838 | — | — |
| ${}^{243}$Np | 243 | 150 | L?-pending | pending | binding_energy | — | 1828.8180 | — | — |
| ${}^{244}$Np | 244 | 151 | L?-pending | pending | binding_energy | — | 1833.4160 | — | — |
| ${}^{245}$Np | 245 | 152 | L?-pending | pending | binding_energy | — | 1838.9700 | — | — |

### Plutonium (Z = 94)

_0 of 27 isotopes with a framework prediction; 0 of 27 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{221}$Pu | 221 | 127 | L?-pending | pending | binding_energy | — | 1674.2960 | — | — |
| ${}^{222}$Pu | 222 | 128 | L?-pending | pending | binding_energy | — | 1683.2040 | — | — |
| ${}^{223}$Pu | 223 | 129 | L?-pending | pending | binding_energy | — | 1690.3400 | — | — |
| ${}^{224}$Pu | 224 | 130 | L?-pending | pending | binding_energy | — | 1699.2640 | — | — |
| ${}^{225}$Pu | 225 | 131 | L?-pending | pending | binding_energy | — | 1706.1750 | — | — |
| ${}^{226}$Pu | 226 | 132 | L?-pending | pending | binding_energy | — | 1714.8880 | — | — |
| ${}^{227}$Pu | 227 | 133 | L?-pending | pending | binding_energy | — | 1721.7950 | — | — |
| ${}^{228}$Pu | 228 | 134 | L?-pending | pending | binding_energy | — | 1730.6121 | — | — |
| ${}^{229}$Pu | 229 | 135 | L?-pending | pending | binding_energy | — | 1737.3963 | — | — |
| ${}^{230}$Pu | 230 | 136 | L?-pending | pending | binding_energy | — | 1745.9304 | — | — |
| ${}^{231}$Pu | 231 | 137 | L?-pending | pending | binding_energy | — | 1752.6253 | — | — |
| ${}^{232}$Pu | 232 | 138 | L?-pending | pending | binding_energy | — | 1760.6443 | — | — |
| ${}^{233}$Pu | 233 | 139 | L?-pending | pending | binding_energy | — | 1767.0247 | — | — |
| ${}^{234}$Pu | 234 | 140 | L?-pending | pending | binding_energy | — | 1774.7978 | — | — |
| ${}^{235}$Pu | 235 | 141 | L?-pending | pending | binding_energy | — | 1781.0368 | — | — |
| ${}^{236}$Pu | 236 | 142 | L?-pending | pending | binding_energy | — | 1788.3889 | — | — |
| ${}^{237}$Pu | 237 | 143 | L?-pending | pending | binding_energy | — | 1794.2701 | — | — |
| ${}^{238}$Pu | 238 | 144 | L?-pending | pending | binding_energy | — | 1801.2699 | — | — |
| ${}^{239}$Pu | 239 | 145 | L?-pending | pending | binding_energy | — | 1806.9162 | — | — |
| ${}^{240}$Pu | 240 | 146 | L?-pending | pending | binding_energy | — | 1813.4504 | — | — |
| ${}^{241}$Pu | 241 | 147 | L?-pending | pending | binding_energy | — | 1818.6919 | — | — |
| ${}^{242}$Pu | 242 | 148 | L?-pending | pending | binding_energy | — | 1825.0015 | — | — |
| ${}^{243}$Pu | 243 | 149 | L?-pending | pending | binding_energy | — | 1830.0351 | — | — |
| ${}^{244}$Pu | 244 | 150 | L?-pending | pending | binding_energy | — | 1836.0550 | — | — |
| ${}^{245}$Pu | 245 | 151 | L?-pending | pending | binding_energy | — | 1840.7541 | — | — |
| ${}^{246}$Pu | 246 | 152 | L?-pending | pending | binding_energy | — | 1846.6089 | — | — |
| ${}^{247}$Pu | 247 | 153 | L?-pending | pending | binding_energy | — | 1850.7710 | — | — |

### Americium (Z = 95)

_0 of 27 isotopes with a framework prediction; 0 of 27 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{223}$Am | 223 | 128 | L?-pending | pending | binding_energy | — | 1682.9810 | — | — |
| ${}^{224}$Am | 224 | 129 | L?-pending | pending | binding_energy | — | 1690.3040 | — | — |
| ${}^{225}$Am | 225 | 130 | L?-pending | pending | binding_energy | — | 1699.4250 | — | — |
| ${}^{226}$Am | 226 | 131 | L?-pending | pending | binding_energy | — | 1706.7520 | — | — |
| ${}^{227}$Am | 227 | 132 | L?-pending | pending | binding_energy | — | 1715.6660 | — | — |
| ${}^{228}$Am | 228 | 133 | L?-pending | pending | binding_energy | — | 1722.9960 | — | — |
| ${}^{229}$Am | 229 | 134 | L?-pending | pending | binding_energy | — | 1731.8285 | — | — |
| ${}^{230}$Am | 230 | 135 | L?-pending | pending | binding_energy | — | 1739.2600 | — | — |
| ${}^{231}$Am | 231 | 136 | L?-pending | pending | binding_energy | — | 1747.7460 | — | — |
| ${}^{232}$Am | 232 | 137 | L?-pending | pending | binding_energy | — | 1754.8480 | — | — |
| ${}^{233}$Am | 233 | 138 | L?-pending | pending | binding_energy | — | 1763.1110 | — | — |
| ${}^{234}$Am | 234 | 139 | L?-pending | pending | binding_energy | — | 1769.9760 | — | — |
| ${}^{235}$Am | 235 | 140 | L?-pending | pending | binding_energy | — | 1777.8122 | — | — |
| ${}^{236}$Am | 236 | 141 | L?-pending | pending | binding_energy | — | 1784.3960 | — | — |
| ${}^{237}$Am | 237 | 142 | L?-pending | pending | binding_energy | — | 1791.9570 | — | — |
| ${}^{238}$Am | 238 | 143 | L?-pending | pending | binding_energy | — | 1798.2293 | — | — |
| ${}^{239}$Am | 239 | 144 | L?-pending | pending | binding_energy | — | 1805.3317 | — | — |
| ${}^{240}$Am | 240 | 145 | L?-pending | pending | binding_energy | — | 1811.2833 | — | — |
| ${}^{241}$Am | 241 | 146 | L?-pending | pending | binding_energy | — | 1817.9304 | — | — |
| ${}^{242}$Am | 242 | 147 | L?-pending | pending | binding_energy | — | 1823.4680 | — | — |
| ${}^{243}$Am | 243 | 148 | L?-pending | pending | binding_energy | — | 1829.8323 | — | — |
| ${}^{244}$Am | 244 | 149 | L?-pending | pending | binding_energy | — | 1835.1995 | — | — |
| ${}^{245}$Am | 245 | 150 | L?-pending | pending | binding_energy | — | 1841.2496 | — | — |
| ${}^{246}$Am | 246 | 151 | L?-pending | pending | binding_energy | — | 1846.2300 | — | — |
| ${}^{247}$Am | 247 | 152 | L?-pending | pending | binding_energy | — | 1852.2530 | — | — |
| ${}^{248}$Am | 248 | 153 | L?-pending | pending | binding_energy | — | 1856.7760 | — | — |
| ${}^{249}$Am | 249 | 154 | L?-pending | pending | binding_energy | — | 1862.2710 | — | — |

### Curium (Z = 96)

_0 of 22 isotopes with a framework prediction; 0 of 22 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{231}$Cm | 231 | 135 | L?-pending | pending | binding_energy | — | 1742.2020 | — | — |
| ${}^{232}$Cm | 232 | 136 | L?-pending | pending | binding_energy | — | 1751.1360 | — | — |
| ${}^{233}$Cm | 233 | 137 | L?-pending | pending | binding_energy | — | 1758.2185 | — | — |
| ${}^{234}$Cm | 234 | 138 | L?-pending | pending | binding_energy | — | 1766.8607 | — | — |
| ${}^{235}$Cm | 235 | 139 | L?-pending | pending | binding_energy | — | 1773.5450 | — | — |
| ${}^{236}$Cm | 236 | 140 | L?-pending | pending | binding_energy | — | 1781.8729 | — | — |
| ${}^{237}$Cm | 237 | 141 | L?-pending | pending | binding_energy | — | 1788.5499 | — | — |
| ${}^{238}$Cm | 238 | 142 | L?-pending | pending | binding_energy | — | 1796.4232 | — | — |
| ${}^{239}$Cm | 239 | 143 | L?-pending | pending | binding_energy | — | 1802.7928 | — | — |
| ${}^{240}$Cm | 240 | 144 | L?-pending | pending | binding_energy | — | 1810.2868 | — | — |
| ${}^{241}$Cm | 241 | 145 | L?-pending | pending | binding_energy | — | 1816.3806 | — | — |
| ${}^{242}$Cm | 242 | 146 | L?-pending | pending | binding_energy | — | 1823.3500 | — | — |
| ${}^{243}$Cm | 243 | 147 | L?-pending | pending | binding_energy | — | 1829.0430 | — | — |
| ${}^{244}$Cm | 244 | 148 | L?-pending | pending | binding_energy | — | 1835.8445 | — | — |
| ${}^{245}$Cm | 245 | 149 | L?-pending | pending | binding_energy | — | 1841.3631 | — | — |
| ${}^{246}$Cm | 246 | 150 | L?-pending | pending | binding_energy | — | 1847.8220 | — | — |
| ${}^{247}$Cm | 247 | 151 | L?-pending | pending | binding_energy | — | 1852.9772 | — | — |
| ${}^{248}$Cm | 248 | 152 | L?-pending | pending | binding_energy | — | 1859.1888 | — | — |
| ${}^{249}$Cm | 249 | 153 | L?-pending | pending | binding_energy | — | 1863.9022 | — | — |
| ${}^{250}$Cm | 250 | 154 | L?-pending | pending | binding_energy | — | 1869.7346 | — | — |
| ${}^{251}$Cm | 251 | 155 | L?-pending | pending | binding_energy | — | 1874.1475 | — | — |
| ${}^{252}$Cm | 252 | 156 | L?-pending | pending | binding_energy | — | 1879.9200 | — | — |

### Berkelium (Z = 97)

_0 of 22 isotopes with a framework prediction; 0 of 22 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{233}$Bk | 233 | 136 | L?-pending | pending | binding_energy | — | 1751.9270 | — | — |
| ${}^{234}$Bk | 234 | 137 | L?-pending | pending | binding_energy | — | 1759.4460 | — | — |
| ${}^{235}$Bk | 235 | 138 | L?-pending | pending | binding_energy | — | 1768.1400 | — | — |
| ${}^{236}$Bk | 236 | 139 | L?-pending | pending | binding_energy | — | 1775.4280 | — | — |
| ${}^{237}$Bk | 237 | 140 | L?-pending | pending | binding_energy | — | 1783.8990 | — | — |
| ${}^{238}$Bk | 238 | 141 | L?-pending | pending | binding_energy | — | 1790.9500 | — | — |
| ${}^{239}$Bk | 239 | 142 | L?-pending | pending | binding_energy | — | 1798.9530 | — | — |
| ${}^{240}$Bk | 240 | 143 | L?-pending | pending | binding_energy | — | 1805.5200 | — | — |
| ${}^{241}$Bk | 241 | 144 | L?-pending | pending | binding_energy | — | 1813.2840 | — | — |
| ${}^{242}$Bk | 242 | 145 | L?-pending | pending | binding_energy | — | 1819.5980 | — | — |
| ${}^{243}$Bk | 243 | 146 | L?-pending | pending | binding_energy | — | 1826.7530 | — | — |
| ${}^{244}$Bk | 244 | 147 | L?-pending | pending | binding_energy | — | 1832.8001 | — | — |
| ${}^{245}$Bk | 245 | 148 | L?-pending | pending | binding_energy | — | 1839.7715 | — | — |
| ${}^{246}$Bk | 246 | 149 | L?-pending | pending | binding_energy | — | 1845.6897 | — | — |
| ${}^{247}$Bk | 247 | 150 | L?-pending | pending | binding_energy | — | 1852.2384 | — | — |
| ${}^{248}$Bk | 248 | 151 | L?-pending | pending | binding_energy | — | 1857.6682 | — | — |
| ${}^{249}$Bk | 249 | 152 | L?-pending | pending | binding_energy | — | 1864.0242 | — | — |
| ${}^{250}$Bk | 250 | 153 | L?-pending | pending | binding_energy | — | 1868.9898 | — | — |
| ${}^{251}$Bk | 251 | 154 | L?-pending | pending | binding_energy | — | 1874.7852 | — | — |
| ${}^{252}$Bk | 252 | 155 | L?-pending | pending | binding_energy | — | 1879.6680 | — | — |
| ${}^{253}$Bk | 253 | 156 | L?-pending | pending | binding_energy | — | 1885.1030 | — | — |
| ${}^{254}$Bk | 254 | 157 | L?-pending | pending | binding_energy | — | 1889.7600 | — | — |

### Californium (Z = 98)

_0 of 20 isotopes with a framework prediction; 0 of 20 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{237}$Cf | 237 | 139 | L?-pending | pending | binding_energy | — | 1778.2941 | — | — |
| ${}^{238}$Cf | 238 | 140 | L?-pending | pending | binding_energy | — | 1787.1420 | — | — |
| ${}^{239}$Cf | 239 | 141 | L?-pending | pending | binding_energy | — | 1794.1730 | — | — |
| ${}^{240}$Cf | 240 | 142 | L?-pending | pending | binding_energy | — | 1802.4576 | — | — |
| ${}^{241}$Cf | 241 | 143 | L?-pending | pending | binding_energy | — | 1809.1870 | — | — |
| ${}^{242}$Cf | 242 | 144 | L?-pending | pending | binding_energy | — | 1817.2020 | — | — |
| ${}^{243}$Cf | 243 | 145 | L?-pending | pending | binding_energy | — | 1823.7150 | — | — |
| ${}^{244}$Cf | 244 | 146 | L?-pending | pending | binding_energy | — | 1831.2535 | — | — |
| ${}^{245}$Cf | 245 | 147 | L?-pending | pending | binding_energy | — | 1837.4178 | — | — |
| ${}^{246}$Cf | 246 | 148 | L?-pending | pending | binding_energy | — | 1844.7840 | — | — |
| ${}^{247}$Cf | 247 | 149 | L?-pending | pending | binding_energy | — | 1850.8362 | — | — |
| ${}^{248}$Cf | 248 | 150 | L?-pending | pending | binding_energy | — | 1857.7789 | — | — |
| ${}^{249}$Cf | 249 | 151 | L?-pending | pending | binding_energy | — | 1863.3655 | — | — |
| ${}^{250}$Cf | 250 | 152 | L?-pending | pending | binding_energy | — | 1869.9892 | — | — |
| ${}^{251}$Cf | 251 | 153 | L?-pending | pending | binding_energy | — | 1875.0959 | — | — |
| ${}^{252}$Cf | 252 | 154 | L?-pending | pending | binding_energy | — | 1881.2675 | — | — |
| ${}^{253}$Cf | 253 | 155 | L?-pending | pending | binding_energy | — | 1886.0719 | — | — |
| ${}^{254}$Cf | 254 | 156 | L?-pending | pending | binding_energy | — | 1892.1034 | — | — |
| ${}^{255}$Cf | 255 | 157 | L?-pending | pending | binding_energy | — | 1896.6900 | — | — |
| ${}^{256}$Cf | 256 | 158 | L?-pending | pending | binding_energy | — | 1902.5920 | — | — |

### Einsteinium (Z = 99)

_0 of 20 isotopes with a framework prediction; 0 of 20 with L4 composite mass $M = N \cdot m_n + Z \cdot m_p - B$._

| Atom | $A$ | $N$ | Layer | Status | Predicts | Prediction (MeV) | Reference (MeV) | Error | $M_{\text{composite}}$ |
|---|---|---|---|---|---|---|---|---|---|
| ${}^{239}$Es | 239 | 140 | L?-pending | pending | binding_energy | — | 1787.9590 | — | — |
| ${}^{240}$Es | 240 | 141 | L?-pending | pending | binding_energy | — | 1795.4400 | — | — |
| ${}^{241}$Es | 241 | 142 | L?-pending | pending | binding_energy | — | 1803.8850 | — | — |
| ${}^{242}$Es | 242 | 143 | L?-pending | pending | binding_energy | — | 1810.8860 | — | — |
| ${}^{243}$Es | 243 | 144 | L?-pending | pending | binding_energy | — | 1819.0980 | — | — |
| ${}^{244}$Es | 244 | 145 | L?-pending | pending | binding_energy | — | 1825.8520 | — | — |
| ${}^{245}$Es | 245 | 146 | L?-pending | pending | binding_energy | — | 1833.8250 | — | — |
| ${}^{246}$Es | 246 | 147 | L?-pending | pending | binding_energy | — | 1840.2731 | — | — |
| ${}^{247}$Es | 247 | 148 | L?-pending | pending | binding_energy | — | 1847.5848 | — | — |
| ${}^{248}$Es | 248 | 149 | L?-pending | pending | binding_energy | — | 1854.0480 | — | — |
| ${}^{249}$Es | 249 | 150 | L?-pending | pending | binding_energy | — | 1861.0260 | — | — |
| ${}^{250}$Es | 250 | 151 | L?-pending | pending | binding_energy | — | 1867.2500 | — | — |
| ${}^{251}$Es | 251 | 152 | L?-pending | pending | binding_energy | — | 1873.9369 | — | — |
| ${}^{252}$Es | 252 | 153 | L?-pending | pending | binding_energy | — | 1879.2252 | — | — |
| ${}^{253}$Es | 253 | 154 | L?-pending | pending | binding_energy | — | 1885.5806 | — | — |
| ${}^{254}$Es | 254 | 155 | L?-pending | pending | binding_energy | — | 1890.6683 | — | — |
| ${}^{255}$Es | 255 | 156 | L?-pending | pending | binding_energy | — | 1896.6445 | — | — |
| ${}^{256}$Es | 256 | 157 | L?-pending | pending | binding_energy | — | 1901.5680 | — | — |
| ${}^{257}$Es | 257 | 158 | L?-pending | pending | binding_energy | — | 1907.4540 | — | — |
| ${}^{258}$Es | 258 | 159 | L?-pending | pending | binding_energy | — | 1912.2960 | — | — |

<!-- AUTO:per-z-sections END -->
