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
| $K_{11a259}$ | HT-table | 11 | 12.5201 | $^6$Li (volume-match at $\rho = 5$) | `deprecated-volume-match` ⚠ |
| $L_{11a62}$ | HT-table | 11 | 15.3600 | $^7$Li (volume-match at $\rho = 5$) | `deprecated-volume-match` ⚠ |

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

### ⚠ Provisional / deprecated methodology — ⁶Li, ⁷Li

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
| Methodology | ⚠ `deprecated-volume-match` (no GB-NF derivation in $H_{18}(q_0)$). |
| Braid (NF) | *Not derived.*  Volume-match search at $\rho = 5$ returned closure $= K_{11a259}$ (HT-table 11-crossing alternating, $\mathrm{Vol} = 12.5201$).  No explicit $\sigma$-word in $H_{18}$ available. |
| Provisional prediction | $B_\mathrm{pred} = 5 \cdot m_e \cdot 12.5201 = 31.989$ MeV vs $B_\mathrm{AME} = 31.994$.  err $= -164{,}991$ ppb (near search noise floor). |

**⁷Li (PROVISIONAL — `deprecated-volume-match`)**

| Row | Content |
|--:|---|
| Methodology | ⚠ `deprecated-volume-match` (no GB-NF derivation in $H_{21}(q_0)$). |
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

6. [`li-atom-knot-search.witness.json`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/li-atom-knot-search.witness.json) — ⚠ provisional volume-match search.

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
