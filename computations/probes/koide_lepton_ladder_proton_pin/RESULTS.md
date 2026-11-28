# Results: Division-Free $S_3/\mathbb{Z}_3$ Singlet–Doublet Koide Equipartition & 2026-11-28 Least-Crossing Lepton Ladder Invariants at the Proton Pin (`qou-cw8i`)

- **Bean / Epics**: `qou-cw8i` (under Stability Epic `qou-s028` & Compute-Accuracy Epic `qou-myts`)
- **Lean 4 Modules (`0 sorry`, `0` custom `axiom`s, `[propext, Classical.choice, Quot.sound]` only)**:
  - [`QOU/StandardModel/KoideSingletDoubletEquipartition.lean`](../../../folio/quantum-observable-universe/lean/QOU/StandardModel/KoideSingletDoubletEquipartition.lean) (`100%` `[CommRing R]`, `0` `[Field]`, `0` `field_simp`, `0` transcendental APIs)
  - [`QOU/StandardModel/BringThreeGenerationsAndTauSatellite.lean`](../../../folio/quantum-observable-universe/lean/QOU/StandardModel/BringThreeGenerationsAndTauSatellite.lean) (`koideTopologicalProtection_of_singletDoubletBridge`)
  - [`QOU/StandardModel/S3CirculantKoideTraceIdentity.lean`](../../../folio/quantum-observable-universe/lean/QOU/StandardModel/S3CirculantKoideTraceIdentity.lean) (`fourier_circulant_equipartition_implies_resolvent_ring`)
- **80-dps Proton-Pin Probe & Witness**:
  - [`koide_lepton_ladder_proton_pin_probe.py`](koide_lepton_ladder_proton_pin_probe.py) (`probe-float64-guard` clean, `q0Anchor = "proton"`)
  - [`koide-lepton-ladder-proton-pin-probe.witness.json`](koide-lepton-ladder-proton-pin-probe.witness.json) (`6/6` assertions passed, `allPassed = true`, two-step SHA witness stamp)

---

## 1. Algebraic Core Discharged Unconditionally over `[CommRing R]` (`qou-cw8i`)

Previously, `KoideTopologicalProtectionHypothesis` (`BringThreeGenerationsAndTauSatellite.lean`) and `KoideCirculantEquipartitionHypothesis` (`S3CirculantKoideTraceIdentity.lean`) required `[Field F]` and bundled pure circulant/projector/moment algebra with the physical equipartition bridge. `KoideSingletDoubletEquipartition.lean` discharges **100% of the algebraic core** unconditionally over any `[CommRing R]`:

1. **Division-Free $S_3$ Projectors & Bring Ambient-$R^5$ Stretch (`threeProj_idempotent_orthog_and_trace`, `singlet_doublet_equipartition_iff_koide_ring`, `bring5_singlet_doublet_metric_stretch`)**:
   - Scaled projectors $3 P_{\mathbf{1}} = J_3$ and $3 P_{\mathrm{std}} = 3 I_3 - J_3$ satisfy $9\|v\|_3^2 = \|3 P_{\mathbf{1}} v\|_3^2 + \|3 P_{\mathrm{std}} v\|_3^2$ and $\|3 P_{\mathrm{std}} v\|_3^2 = \|3 P_{\mathbf{1}} v\|_3^2 + 3(3\|v\|_3^2 - 2(v_0 + v_1 + v_2)^2)$, proving $\|3 P_{\mathbf{1}} v\|_3^2 = \|3 P_{\mathrm{std}} v\|_3^2 \iff 3\|v\|_3^2 = 2(v_0 + v_1 + v_2)^2$ over any $3$-torsion-free `[CommRing R]`.
2. **Operator Trace Equipartition, Circulant Fourier Moments & $V^{\otimes 3}$ Schur–Weyl $4 = 4$ Split (`matrix_trace_equipartition_iff_koide_ring`, `circulant3FourierSpec_moments`, `q3SchurWeyl_partition_and_classical_equipartition`)**:
   - Discharges `trace_moment` and `sq_trace_moment` automatically for every circulant $S(a_0, b, c)$ ($1 + \omega + \omega^2 = 0$).
   - Proves $q^3 [4]_q + 2 q^3 [2]_q = (q^2 + 1)^3$, establishing **unconditional $4 = 4$ singlet–doublet dimension equipartition** on the 3-strand state space $(\mathbb{C}^2)^{\otimes 3} = (V_{3/2} \otimes \mathbf{1}) \oplus (V_{1/2} \otimes V_{\mathrm{std}})$ at $q^2 = 1$ and exact $(q^2 + 1)(q^2 - 1)^2$ quantum-dimension excess for $q^2 \neq 1$.
3. **Ordered-Ring Discriminant Positivity & Radical-Free Quartic Koide Mass Polynomial (`koide_discriminant_pos_and_upper_root_dominance`, `koide_saddle_quartic_eliminating_v`, `koideMassQuarticPoly_galois_factorization`)**:
   - Eliminates all radicals $(\sqrt{m_1}, \sqrt{m_2}, \sqrt{m_3})$ via the 4-branch Galois factorization of $K_4(m_1, m_2, m_3) = ((m_1 + m_2 + m_3)^2 - 16(m_1 m_2 + m_2 m_3 + m_3 m_1))^2 - 1536(m_1 + m_2 + m_3) m_1 m_2 m_3$, verified at 80 dps to `3.25e-68` absolute residual (`0.0` relative residual on the $v$-eliminated figure-eight saddle quartic).
   - At the proton pin $q_0 = 1.1099785827513808...$ (with the `CAL-2` muon pin on hold per the 2026-11-28 owner directive), $\mathrm{Vol}(4_1)/\hbar_{q_0}^2 = 206.76832637...$ gives $m_\tau / m_e = 3477.44230642$ (`+0.923σ` vs CODATA-2022 `3477.23 ± 0.23`, `+0.437σ` vs PDG-2024 `3477.3653 ± 0.1761`), narrowing `ACCURACY.md` Table 3.1a's `Conditional` basis strictly to the 1-equation class `KoideSingletDoubletEquipartitionBridge`.

---

## 2. 2026-11-28 Ruled Least-Crossing 2-Component Lepton Link Ladder (`owner-rulings.md` rows 17–18)

On `e = \sigma_0\sigma_1\sigma_0` (Hopf, `lk = 1`, `c = 2`), `\mu = \sigma_0^4\sigma_1^{-1}` ($T(2,4)$, `lk = 2`, `c = 4`), `\tau = \sigma_0^2\sigma_1^{-1}\sigma_0\sigma_1^{-1}` (Whitehead, `lk = 0`, `c = 5`):

1. **Exact `[CommRing R]` Theorems (`least_crossing_ladder_combinatorial_invariants`, `det_one_sub_burau_neg_one_eq_two_sub_trace`, `morton_birman_burau_ladder_invariants`, `q12_ring_mass_skein_differences_and_singlet_collapse`)**:
   - Proves the **universal 3-braid identity** $\det(I_2 - B_w(-1)) = 2 - \mathrm{tr}(\mathrm{imgZ}\,w)$ for **all** $w \in B_3$, yielding link determinants $|2 - \mathrm{tr}| = (2, 4, 8)$ (`tr = 0, 6, 10`) on $(e, \mu, \tau)$ and $-5$ (`tr = 7`) on $4_1$.
   - Proves exact cleared-denominator $N = 2$ ring-mass skein differences $m_e(q) - m_\mu(q) = 1 - q^{-12}$ and $m_\tau(q) - m_e(q) = q^4(1 - q^{-12})$ (`6.33e-81` residual at 80 dps), establishing $m_\mu(q) < m_e(q) < m_\tau(q)$ for every $q > 1$ and pure $S_3$-singlet collapse $(4, 4, 4)$ ($Q = 1/3$) at $q = 1$.
2. **80-dps Proton-Pin $N = 2, 3, 4$ Ring Traces & $\zeta_N$ Kashaev Cut-Axis Growth (Unscored per `owner-rulings.md` row 18)**:

| Colour $N$ | Bare $\mu / e$ | Bare $\tau / e$ | Bare $Q_{\mathrm{Koide}}$ | `closure ∪ axis` $\mu / e$ | `closure ∪ axis` $\tau / e$ | Axis $Q_{\mathrm{Koide}}$ |
|---:|---:|---:|---:|---:|---:|---:|
| `2` | `0.76237600` | `1.36070212` | `0.33801859` | `0.77689814` | `1.35283983` | `0.33764951` |
| `3` | `0.56693754` | `2.23311456` | `0.36036377` | `0.64800359` | `2.05101913` | `0.35299467` |
| `4` | `0.45253782` | `4.41357784` | `0.41195319` | `0.61811367` | `3.11889508` | `0.37540429` |

   - At Kashaev roots of unity $q = e^{i\pi/N}$ (`N = 2..14`, cross-checked against 4-strand partial trace to `1.12e-78`), $|c_N(e)| \le N^2$ remains polynomially bounded (`74.081` at $N = 14$, $\mathrm{Vol} = 0$), while $|c_N(\mu)|$ (`1.3060e7` at $N = 14$, $\mathrm{Vol}(\mu \cup A) \approx 6.3546$) and $|c_N(\tau)|$ (`8.9160e9` at $N = 14$, $\mathrm{Vol}(\tau \cup A) \approx 9.5034$) grow strictly monotonically $|c_N(e)| < |c_N(\mu)| < |c_N(\tau)|$ for all $N \ge 4$.
