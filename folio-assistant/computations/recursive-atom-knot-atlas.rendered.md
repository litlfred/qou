# Recursive Atom-Knot Atlas (auto-rendered from witnesses)

**Pipeline status**: HP=ENABLED (≥50 dps via mpmath.workdps).  Principled-derivation entries (electron, proton, neutron) have their hyperbolic volume computed from the σ-braid closure at ≥50 decimal digits via `hp_volume_of_link_closure(braid_word, digits=50)`.

**Sources of truth**:

- `confined-particle.md` — GB-NF registry (canonical T_w).
- `mass-table-ppb.witness.json` — D..⁴⁰Ca (manual-historical, recursive, magic-A).
- `methodology-deprecation.witness.json` — per-particle methodology audit.
- `hp_volume.py` — symbolic-q + ≥50-digit Markov-closure → Vol_hyp.
- `li-atom-knot-search.witness.json` — ⚠ DEPRECATED, provisional only.

## Methodology classification

Each entry carries a **methodology** tag.  The atlas is split into a *principled* section and a *quarantined / provisional* section.  Volume-match results are NEVER mixed with derivation-based results.

- **principled** (GB-NF or explicit braid → closure): 6
- **manual-historical** (volume-match in earlier work, established): 3
- **magic-A or recursive-on-⁴He**: 2
- **deprecated-volume-match** (PROVISIONAL): 2

## Table layout

Each particle/atom has TWO rows. **Column 1** spans both (particle notation). **Row 1** shows the math: Z, N, e⁻ count, confinement level ℓ, strand count n₀, the braid in σ_* generators (NF), the Markov closure as a named knot/link or recursive structure, and hyperbolic volume.  **Row 2** shows the physics: AME binding, model prediction, error in **whole-integer ppb** (no scientific notation), and the ρ prefactor in $B = \rho \cdot m_e \cdot \mathrm{Vol}_{\mathrm{hyp}}$.

Magic-number markers: ★ next to Z or N indicates a nuclear shell closure (Z, N ∈ {2, 8, 20, 28, 50, 82, 126}).

## Principled atlas

Entries below have either a GB-NF derivation (fundamental particles) or are *manual-historical* (²H, ³H, ³He), *recursive* (⁸Be onward), or *magic-A* (⁴He).  Volumes for principled-derivation entries are computed at ≥50 digits.


### $\ell = 0, 1$ — fundamental particles

<table>
<thead>
<tr><th rowspan='2'>Particle / atom</th><th colspan='3'>Composition</th><th colspan='2'>Confinement</th><th colspan='3'>Math (row 1) / Physics (row 2)</th></tr>
<tr><th>Z</th><th>N</th><th>e<sup>−</sup></th><th>ℓ</th><th>n₀</th><th>Braid (NF) / AME (MeV)</th><th>Closure / Pred (MeV)</th><th>Vol<sub>hyp</sub> / err ppb (ρ)</th></tr>
</thead>
<tbody>
<tr><td rowspan='2'><strong>Neutrino $\nu$</strong></td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>$\mathbf{1} \in H_1$</td><td>$0_1$ (unknot)</td><td>Vol<sub>hyp</sub>: 0</td></tr>
<tr><td colspan='5'><em>(physics)</em></td><td>AME: $\le 1$ eV</td><td>Pred: $\approx 0$ MeV</td><td>err: — ppb (ρ=—)</td></tr>
<tr><td rowspan='2'><strong>Photon $\gamma$</strong></td><td>0</td><td>0</td><td>0</td><td>0</td><td>4</td><td>$\mathbf{1}_{B_4} \in H_4$</td><td>$4 \cdot 0_1$ (4-strand id)</td><td>Vol<sub>hyp</sub>: 0</td></tr>
<tr><td colspan='5'><em>(physics)</em></td><td>AME: 0 MeV</td><td>Pred: 0 MeV</td><td>err: — ppb (ρ=—)</td></tr>
<tr><td rowspan='2'><strong>Quark $\mathfrak{q}$</strong></td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>$\sigma_0 \in H_1$</td><td>(in $\mathcal{B}_3$)</td><td>Vol<sub>hyp</sub>: —</td></tr>
<tr><td colspan='5'><em>(physics)</em></td><td>AME: (confined)</td><td>Pred: —</td><td>err: — ppb (ρ=—)</td></tr>
<tr><td rowspan='2'><strong>Electron $e^-$</strong></td><td>0</td><td>0</td><td>1</td><td>1</td><td>2</td><td>$\sigma_1^3 \in H_2$</td><td>$T_{2,3} = 3_1$ (trefoil)</td><td>Vol<sub>hyp</sub>: 0 (torus knot, non-hyp)</td></tr>
<tr><td colspan='5'><em>(physics)</em></td><td>AME: 0.51099895 MeV</td><td>Pred: 0.51099895 MeV</td><td>err: (anchor) ppb (ρ=—)</td></tr>
<tr><td rowspan='2'><strong>Proton $\mathfrak{p}$</strong></td><td>1</td><td>0</td><td>0</td><td>1</td><td>3</td><td>$(\sigma_1 \sigma_2^{-1})^3$ flav-uud</td><td>$\mathcal{B}_3(\mathrm{uud})$</td><td>Vol<sub>hyp</sub>: 7.3277</td></tr>
<tr><td colspan='5'><em>(physics)</em></td><td>AME: 938.272 MeV</td><td>Pred: 938.272 MeV</td><td>err: (anchor) ppb (ρ=—)</td></tr>
<tr><td rowspan='2'><strong>Neutron $\mathfrak{n}$</strong></td><td>0</td><td>1</td><td>0</td><td>1</td><td>3</td><td>$(\sigma_1 \sigma_2^{-1})^3$ flav-udd</td><td>$\mathcal{B}_3(\mathrm{udd})$</td><td>Vol<sub>hyp</sub>: 7.3277</td></tr>
<tr><td colspan='5'><em>(physics)</em></td><td>AME: 939.565 MeV</td><td>Pred: 939.565 MeV</td><td>err: (anchor) ppb (ρ=—)</td></tr>
</tbody></table>

### $\ell = 2$ — light atoms (mass-table-ppb)

<table>
<thead>
<tr><th rowspan='2'>Particle / atom</th><th colspan='3'>Composition</th><th colspan='2'>Confinement</th><th colspan='3'>Math (row 1) / Physics (row 2)</th></tr>
<tr><th>Z</th><th>N</th><th>e<sup>−</sup></th><th>ℓ</th><th>n₀</th><th>Braid (NF) / AME (MeV)</th><th>Closure / Pred (MeV)</th><th>Vol<sub>hyp</sub> / err ppb (ρ)</th></tr>
</thead>
<tbody>
<tr><td rowspan='2'><strong>$^{2}\mathrm{H}$</strong></td><td>1</td><td>1</td><td>1</td><td>2</td><td>6</td><td>closure = $6_{2}$ — atomic-braid in $H_{6}$</td><td>$6_{2}$</td><td>Vol<sub>hyp</sub>: 4.4008</td></tr>
<tr><td colspan='5'><em>(physics)</em></td><td>AME: 2.2246 MeV</td><td>Pred: 2.2488 MeV</td><td>err: +10,903,104 ppb (ρ=1)</td></tr>
<tr><td rowspan='2'><strong>$^{3}\mathrm{H}$</strong></td><td>1</td><td>2 ★</td><td>1</td><td>2</td><td>9</td><td>closure = $8_{11}$ — atomic-braid in $H_{9}$</td><td>$8_{11}$</td><td>Vol<sub>hyp</sub>: 8.2863</td></tr>
<tr><td colspan='5'><em>(physics)</em></td><td>AME: 8.4818 MeV</td><td>Pred: 8.4686 MeV</td><td>err: -1,556,275 ppb (ρ=2)</td></tr>
<tr><td rowspan='2'><strong>$^{3}\mathrm{He}$</strong></td><td>2 ★</td><td>1</td><td>2</td><td>2</td><td>9</td><td>closure = $L_{6a4}$ — atomic-braid in $H_{9}$</td><td>$L_{6a4}$</td><td>Vol<sub>hyp</sub>: 7.3277</td></tr>
<tr><td colspan='5'><em>(physics)</em></td><td>AME: 7.7180 MeV</td><td>Pred: 7.4889 MeV</td><td>err: -29,686,069 ppb (ρ=2)</td></tr>
<tr><td rowspan='2'><strong>$^{4}\mathrm{He}$</strong></td><td>2 ★</td><td>2 ★</td><td>2</td><td>2</td><td>12</td><td>$A \cdot 8G$ magic-A formula — atomic-braid in $H_{12}$</td><td>$A \cdot 8G$ magic-A</td><td>Vol<sub>hyp</sub>: —</td></tr>
<tr><td colspan='5'><em>(physics)</em></td><td>AME: 28.2957 MeV</td><td>Pred: 29.9557 MeV</td><td>err: +58,665,683 ppb (ρ=2)</td></tr>
<tr><td rowspan='2'><strong>$^{8}\mathrm{Be}$</strong></td><td>4</td><td>4</td><td>4</td><td>2</td><td>24</td><td>recursive: 2 $\times {}^{4}\mathrm{He}$ $\bowtie c_{\alpha\alpha}$ — atomic-braid in $H_{24}$</td><td>$2 \cdot {}^{4}\mathrm{He} + 1 \cdot c_{\alpha\alpha}$</td><td>Vol<sub>hyp</sub>: —</td></tr>
<tr><td colspan='5'><em>(physics)</em></td><td>AME: 56.4995 MeV</td><td>Pred: 62.3383 MeV</td><td>err: +103,343,091 ppb (ρ=—)</td></tr>
<tr><td rowspan='2'><strong>$^{12}\mathrm{C}$</strong></td><td>6</td><td>6</td><td>6</td><td>2</td><td>36</td><td>recursive: 3 $\times {}^{4}\mathrm{He}$ $\bowtie c_{\alpha\alpha}$ — atomic-braid in $H_{36}$</td><td>$3 \cdot {}^{4}\mathrm{He} + 3 \cdot c_{\alpha\alpha}$</td><td>Vol<sub>hyp</sub>: —</td></tr>
<tr><td colspan='5'><em>(physics)</em></td><td>AME: 92.1617 MeV</td><td>Pred: 97.1480 MeV</td><td>err: +54,103,250 ppb (ρ=—)</td></tr>
<tr><td rowspan='2'><strong>$^{16}\mathrm{O}$</strong></td><td>8 ★</td><td>8 ★</td><td>8</td><td>2</td><td>48</td><td>recursive: 4 $\times {}^{4}\mathrm{He}$ $\bowtie c_{\alpha\alpha}$ — atomic-braid in $H_{48}$</td><td>$4 \cdot {}^{4}\mathrm{He} + 6 \cdot c_{\alpha\alpha}$</td><td>Vol<sub>hyp</sub>: —</td></tr>
<tr><td colspan='5'><em>(physics)</em></td><td>AME: 127.6193 MeV</td><td>Pred: 134.3846 MeV</td><td>err: +53,012,017 ppb (ρ=—)</td></tr>
<tr><td rowspan='2'><strong>$^{20}\mathrm{Ne}$</strong></td><td>10</td><td>10</td><td>10</td><td>2</td><td>60</td><td>recursive: 5 $\times {}^{4}\mathrm{He}$ $\bowtie c_{\alpha\alpha}$ — atomic-braid in $H_{60}$</td><td>$5 \cdot {}^{4}\mathrm{He} + 10 \cdot c_{\alpha\alpha}$</td><td>Vol<sub>hyp</sub>: —</td></tr>
<tr><td colspan='5'><em>(physics)</em></td><td>AME: 160.6449 MeV</td><td>Pred: 174.0483 MeV</td><td>err: +83,435,108 ppb (ρ=—)</td></tr>
<tr><td rowspan='2'><strong>$^{24}\mathrm{Mg}$</strong></td><td>12</td><td>12</td><td>12</td><td>2</td><td>72</td><td>recursive: 6 $\times {}^{4}\mathrm{He}$ $\bowtie c_{\alpha\alpha}$ — atomic-braid in $H_{72}$</td><td>$6 \cdot {}^{4}\mathrm{He} + 15 \cdot c_{\alpha\alpha}$</td><td>Vol<sub>hyp</sub>: —</td></tr>
<tr><td colspan='5'><em>(physics)</em></td><td>AME: 198.2569 MeV</td><td>Pred: 216.1389 MeV</td><td>err: +90,196,134 ppb (ρ=—)</td></tr>
<tr><td rowspan='2'><strong>$^{40}\mathrm{Ca}$</strong></td><td>20 ★</td><td>20 ★</td><td>20</td><td>2</td><td>120</td><td>recursive: 10 $\times {}^{4}\mathrm{He}$ $\bowtie c_{\alpha\alpha}$ — atomic-braid in $H_{120}$</td><td>$10 \cdot {}^{4}\mathrm{He} + 45 \cdot c_{\alpha\alpha}$</td><td>Vol<sub>hyp</sub>: —</td></tr>
<tr><td colspan='5'><em>(physics)</em></td><td>AME: 342.0521 MeV</td><td>Pred: 408.7713 MeV</td><td>err: +195,055,596 ppb (ρ=—)</td></tr>
</tbody></table>

## ⚠ Provisional / deprecated methodology

**The entries below are NOT principled.**  They come from a brute-force SnapPy volume-match search (`li_atom_knot_search.py`), which picks the knot whose Vol_hyp matches the AME target — i.e. it reverse-engineers the answer.  At ~2400 knots searched, residuals below ~10 ppb are indistinguishable from numerical coincidence absent an independent GB-NF derivation in $H_{18}(q_0)$ / $H_{21}(q_0)$.  Listed here for historical transparency only.  **Do NOT cite these as evidence for the mass-table-ppb framework.**  See `methodology-deprecation.witness.json`.


### ⚠ ⁶Li, ⁷Li — provisional volume-match (DEPRECATED methodology)

<table>
<thead>
<tr><th rowspan='2'>Particle / atom</th><th colspan='3'>Composition</th><th colspan='2'>Confinement</th><th colspan='3'>Math (row 1) / Physics (row 2)</th></tr>
<tr><th>Z</th><th>N</th><th>e<sup>−</sup></th><th>ℓ</th><th>n₀</th><th>Braid (NF) / AME (MeV)</th><th>Closure / Pred (MeV)</th><th>Vol<sub>hyp</sub> / err ppb (ρ)</th></tr>
</thead>
<tbody>
<tr><td rowspan='2'><strong>$^{6}\mathrm{Li}$ \textbf{[PROVISIONAL]}</strong></td><td>3</td><td>3</td><td>3</td><td>2</td><td>18</td><td>⚠ volume-match (DEPRECATED) → $K_{11a259}(0,0)$ in $H_{18}$ (no GB-NF derivation)</td><td>$K_{11a259}(0,0)$ \emph{(provisional)}</td><td>Vol<sub>hyp</sub>: 12.5201</td></tr>
<tr><td colspan='5'><em>(physics)</em></td><td>AME: 31.9941 MeV</td><td>Pred: 31.9888 MeV</td><td>err: -164,991 ppb (ρ=5)</td></tr>
<tr><td rowspan='2'><strong>$^{7}\mathrm{Li}$ \textbf{[PROVISIONAL]}</strong></td><td>3</td><td>4</td><td>3</td><td>2</td><td>21</td><td>⚠ volume-match (DEPRECATED) → $L_{11a62}(0,0)(0,0)$ in $H_{21}$ (no GB-NF derivation)</td><td>$L_{11a62}(0,0)(0,0)$ \emph{(provisional)}</td><td>Vol<sub>hyp</sub>: 15.3600</td></tr>
<tr><td colspan='5'><em>(physics)</em></td><td>AME: 39.2445 MeV</td><td>Pred: 39.2447 MeV</td><td>err: +4,009 ppb (ρ=5)</td></tr>
</tbody></table>
