# Audit & Adjudication: Bring $N_{\mathrm{gen}} = 3$ Complete-Intersection Fission Weld & Zero-Parameter Satellite $T(2,n)\text{–}4_1$ Tau Mass Catalog (`qou-gen3` + `qou-htk4`)

- **Date:** 2026-11-24
- **Beans:** `qou-gen3`, `qou-htk4` (`Q-Gap-7`)
- **Lean 4 Formalization:** [`folio/quantum-observable-universe/lean/QOU/StandardModel/BringThreeGenerationsAndTauSatellite.lean`](../../folio/quantum-observable-universe/lean/QOU/StandardModel/BringThreeGenerationsAndTauSatellite.lean) (`0 sorry`, `0` custom `axiom`s, `§7c` generic `[CommRing R]` / `[Field F]`)
- **80-dps Probe & Witness:** [`computations/probes/tau_satellite_41_bring_3gen_probe.py`](../../computations/probes/tau_satellite_41_bring_3gen_probe.py) $\to$ [`computations/probes/tau-satellite-41-bring-3gen-probe.witness.json`](../../computations/probes/tau-satellite-41-bring-3gen-probe.witness.json) (`8/8` assertions passed, `mp.mp.dps = 80`, `QOU_WITNESS_STRICT_FLOAT64=1`)

---

## 1. Unified `4 = 3 + 1` Bring Complete-Intersection & Composite $T(2,9)$ Fission Theorem (`qou-gen3`)

On Bring's complete-intersection curve $\Sigma_4 = \{z_1 + \dots + z_5 = 0,\;\sum z_i^2 = 0,\;\sum z_i^3 = 0\} \subset \mathbb{P}^4$:
- **Adjunction (`bring_adjunction_euler_and_h10_dim`):** Intersection degree $d = 1 \cdot 2 \cdot 3 = 6$, canonical degree $\deg K_{\Sigma_4} = 6(1 + 2 + 3 - 5) = 6$, Euler characteristic $\chi(\Sigma_4) = -6$, and genus $g(\Sigma_4) = 4 = \dim H^{1,0}(\Sigma_4)$.
- **Representation & Topological Fission Weld (`bring_three_plus_one_generation_fission_weld`):** Restricting $H^{1,0}(\Sigma_4) \cong V_{(4,1)}$ along $\mathbb{Z}_3 = A_3 \subset \mathfrak{S}_3 \subset \mathfrak{S}_4 \subset \mathfrak{S}_5$ yields $4 = 3 + 1$ ($\mathfrak{S}_4$) and $4 = (2 \oplus 1) \oplus 1$ ($\mathbb{Z}_3$), matching the exact disjoint partition of Bring's four admissible odd torus-knot windings `admissibleOddTorusSet = {3, 5, 7, 9}` (`card = 4`) into:
  1. `indecomposableGenerationWindings = {3, 5, 7}` (`card = 3`), each possessing **zero** 3-body odd-knot decay channels (`threeOddKnotChannels n = ∅`), and
  2. `compositeFissionWindings = {9}` (`card = 1`), where $T(2,9)$ uniquely crosses the 3-body threshold via $T(2,9) \to 3\,T(2,3)$ (`threeOddKnotChannels 9 = {((3,3),3)}`, $f_3(h) \mid f_9(h)$).

---

## 2. Scope-(b) Exclusions of Pure Satellite JSJ Volumes & Cyclic Branched Covers (`qou-htk4`)

1. **Soma–Agol Satellite Forbidden-Gap Theorem (`soma_agol_satellite_forbidden_gap_k3`):**
   By Gromov–Thurston–Soma JSJ additivity, any satellite $P(4_1)$ with pattern $P \subset S^1 \times D^2$ has $\mathrm{Vol}(P(4_1)) = \mathrm{Vol}(4_1) + \mathrm{Vol}(S^3 \setminus L_P)$.
   - **Seifert cables ($C_{2,3}(4_1), C_{2,5}(4_1), C_{2,7}(4_1)$):** $\mathrm{Vol}(S^3 \setminus L_P) = 0 \implies \mathrm{Vol}(C_{2,2m+1}(4_1)) = \mathrm{Vol}(4_1) = 2.029883\ldots$ (`bend = 1`, `-39.99%` at $k = 3$).
   - **Hyperbolic satellites (Whitehead $5^2_1$, Mazur $7^2_2$, twisted Whitehead, Berge, or iterated patterns):** By Agol's two-cusped volume theorem (*Duke Math. J.* 156 (2010), 399), $\mathrm{Vol}(S^3 \setminus L_P) \ge 4 G_{\mathrm{Catalan}} = 3.663862\ldots$, forcing $\mathrm{Vol}(P(4_1)) \ge 5.693746\ldots$ (`\ge +68.34%` at $k = 3$; Mazur's magic-manifold parent $6^3_1$ has $\mathrm{Vol} = 5\mathrm{Cl}_2(\pi/3) = 5.074708$).
   - Because $\mathrm{Vol}_{\mathrm{req}}^{(k=3)} = \hbar_{q_0}^3 (m_\tau / m_e) = 3.382314\ldots$ lies strictly inside the forbidden interval $(2.029883, 5.693746)$, **zero** pure JSJ-volume satellites match $m_\tau / m_e$ at $k = 3$, and reaching $\mathrm{Vol}_{\mathrm{req}}^{(k=2)} = 34.138718\ldots$ at $k = 2$ would require $\ge 9$ iterated Whitehead pieces.

2. **Mednykh–Vesnin Cyclic Branched Covers $M_n(4_1)$ (`figEightLongTrace_hyperbolic_window`):**
   Using the exact $A$-polynomial Schläfli integral $\mathrm{Vol}(M_n(4_1)) = n \int_{2\pi/n}^{2\pi/3} \operatorname{arccosh}(2 + \cos t - 2\cos^2 t)\,dt$ ($n \ge 4$, Euclidean `0` for $n \le 3$; verified to $10^{-78}$ against $\mathrm{Vol}(M_4(4_1)) = \mathrm{Vol}(4_1)$ and $\mathrm{Vol}(M_6(4_1)) = 8 G_{\mathrm{Catalan}}$):
   - At $k = 3$, $n = 4$ (`2086.85`, `-39.99%`) and $n = 5$ (`4817.54`, `+38.55%`) straddle `3477.23`.
   - At $k = 2$, $n = 17$ (`3314.71`, `-4.67%`) and $n = 18$ (`3532.17`, `+1.58%`) straddle `3477.23`.

---

## 3. Zero-Parameter Candidate Scorecard, `gap2b` Uncertainty Correction, & Entropy Ceiling

### 3.1 Correction of `10x` Parenthetical Uncertainty Slip in `gap2b` / `ACCURACY.md`
- **Contaminated surface:** `computations/probes/gap2b_mtau_s3_circulant_koide_test/gap2b_mtau_s3_circulant_koide_probe.py:276-277` (`r_tau_pdg = 3477.228`, `r_tau_pdg_err = 0.023`), carried into `ACCURACY.md:59` (`+9.32σ`).
- **Measured reality:** `3477.228275` is $1776.86\;\mathrm{MeV} / m_e$ (pre-Belle-II PDG), whose $0.12\;\mathrm{MeV}$ uncertainty equals $0.12 / 0.51099895 = \mathbf{\pm 0.23483}$ (`67.54 ppm`, rounded in CODATA-2022 to `3477.23(23)` = `±0.23`), **not** `±0.023`! Furthermore, the post-Belle-II PDG-2024 world average (*Phys. Rev. D* 110, 030001) is $1776.93 \pm 0.09\;\mathrm{MeV} \implies m_\tau / m_e = \mathbf{3477.3653 \pm 0.1761}$ (`50.65 ppm`).
- **True pulls of `D2` (`Protected Q = 2/3 Koide + Vol(4_1)/ħ_{q_p}² = 3477.442306`):**
  - vs CODATA-2022 (`3477.23 ± 0.23`): **`+61.06 ppm` = `+0.923σ`** (`< 1σ`)
  - vs PDG pre-Belle-II (`1776.86 ± 0.12 MeV` = `3477.2283 ± 0.2348`): **`+61.55 ppm` = `+0.911σ`** (`< 1σ`, correcting the spurious `+9.32σ`)
  - vs PDG-2024 post-Belle-II (`1776.93 ± 0.09 MeV` = `3477.3653 ± 0.1761`): **`+22.15 ppm` = `+0.437σ`** (`< 0.5σ`!)

### 3.2 Proton-Pin (`q_p`) Summary Table Across Pre-Committed Zero-Parameter Families

| ID | Zero-Parameter Formula | Predicted $m_\tau / m_e$ | vs CODATA-2022 (`3477.23±0.23`) | vs PDG-2024 (`3477.365±0.176`) | Verdict |
|---|---|---:|---:|---:|---|
| `A2` | $\mathrm{Vol}(4_1)/\hbar_q^3$ (Seifert cable $C_{2,7}(4_1)$, $k=3$) | `2086.846` | `-39.985%` (`-6045σ`) | `-39.988%` (`-7895σ`) | Excluded (Soma–Agol) |
| `A4` | $(\mathrm{Vol}(4_1) + 4G)/\hbar_q^3$ (Whitehead min hyp sat, $k=3$) | `5853.525` | `+68.339%` (`+10332σ`) | `+68.332%` (`+13491σ`) | Excluded (Soma–Agol) |
| `B1` | $\mathrm{Vol}(M_5(4_1))/\hbar_q^3$ (5-fold cover, $k=3$) | `4817.535` | `+38.545%` (`+5827σ`) | `+38.540%` (`+7609σ`) | Excluded (straddle) |
| `B3` | $\mathrm{Vol}(M_{17}(4_1))/\hbar_q^2$ (17-fold cover, $k=2$) | `3314.714` | `-4.674%` (`-706.6σ`) | `-4.677%` (`-923.5σ`) | Excluded (straddle) |
| `B4` | $\mathrm{Vol}(M_{18}(4_1))/\hbar_q^2$ (18-fold cover, $k=2$) | `3532.166` | `+1.580%` (`+238.9σ`) | `+1.576%` (`+311.1σ`) | Excluded (straddle) |
| `C1` | $[4]_q^2\,\mathrm{Vol}(4_1)/\hbar_q^2$ ($\dim_q H^{1,0}(\Sigma_4)^2$) | `3492.211` | `+0.431%` (`+65.1σ`) | `+0.427%` (`+84.3σ`) | Order-of-mag (`<0.5%`), fails `1σ` |
| `C2` | $[3]_q[5]_q\,\mathrm{Vol}(4_1)/\hbar_q^2$ ($\mathfrak{su}_q(4)$ adjoint) | `3285.443` | `-5.515%` (`-833.9σ`) | `-5.519%` (`-1089.7σ`) | Excluded |
| `C3` | $[2]_q^4\,\mathrm{Vol}(4_1)/\hbar_q^2$ | `3380.985` | `-2.768%` (`-418.5σ`) | `-2.772%` (`-547.2σ`) | Excluded |
| `D1` | Koide at finite-$q_0$ $Q_{\mathrm{TL3}}(q_0) = 0.659538$ | `3199.126` | `-7.998%` (`-1209σ`) | `-8.001%` (`-1580σ`) | Excluded (`q_0` drift) |
| **`D2`** | **Protected $Q=2/3$ Koide on $\mathrm{Vol}(4_1)/\hbar_q^2$** | **`3477.4423`** | **`+61.1 ppm` (`+0.92σ`)** | **`+22.2 ppm` (`+0.44σ`)** | **Within `< 1σ` (Rule 13a)** |

### 3.3 Precision-Entropy Ceiling (`compute-author.md` §3.3)
Because $\sigma(m_\tau)/m_\tau = 67.54\;\mathrm{ppm}$ (`PDG 1776.86(12)`) / `50.65 ppm` (`PDG-2024 1776.93(9)`) furnishes $-\log_{10}(2\sigma_{\mathrm{rel}}) = \mathbf{3.87\text{ to }3.99\text{ decimal digits}}$ of discriminating precision while `D2` already matches to **`+0.91σ` / `+0.44σ`** (`4.21`–`4.65` digits), **zero statistically significant experimental bits remain today** to constrain any sub-`68 ppm` $q_0$-skew or radiative term beyond protected $Q = 2/3$. The sole remaining theoretical obligation is deriving `KoideTopologicalProtectionHypothesis` from first principles.
