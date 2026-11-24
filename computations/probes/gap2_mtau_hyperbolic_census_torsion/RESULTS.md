# Results: Complete $\le 7$-Crossing 3-Braid Hyperbolic Census, Zickert Complex Volume, and `#9213` 1-Loop Reidemeister-Torsion Tau Mass Evaluation (Open Gap 2, Option 2A + Bean `qou-r0dn`)

- **Pre-Registration**: `computations/probes/gap2_mtau_hyperbolic_census_torsion/PREREGISTRATION.md` (committed & pushed at `ff23e8d7c6c` prior to evaluating any $m_\tau / m_e$ ratios)
- **Lean 4 Module**: `folio/quantum-observable-universe/lean/QOU/StandardModel/LowCrossingThreeBraidTauSelection.lean` (`0 sorry`, `0` custom axioms, `§7c` generic `[CommRing R]` / `[Field K]`, zero empirical literals)
- **80-dps Probe & Witness**: `gap2_mtau_hyperbolic_census_torsion_probe.py` + `gap2-mtau-hyperbolic-census-torsion.witness.json` (`9/9` assertions passed, `workdps = 80`, `q0Anchor = "proton"`)

---

## 1. Executive Verdict (`selected = "none"`, Rule 13a)

Under strict zero-fit discipline (`q_0 = q_at(80) = 1.1099785827513808075916690956107688798744991218736...`, $\hbar_{q_0} = 1 - q_0^{-1} = 0.099081716044258507839177117518906063985258373389446...$), matching CODATA-2022 $m_\tau / m_e = 3477.23 \pm 0.23$ (Belle-II/PDG-2024 $3477.228 \pm 0.023$) at generation-3 pole order $k = 3$ requires an effective geometric numerator
$$\mathrm{Vol}_{\mathrm{req}} = \hbar_{q_0}^3 \cdot (m_\tau / m_e) = 3.3823144193484566912964520313545022692383256146295\dots$$

1. **Exact Braid-Index Census Exclusion**:
   - Across all $35$ prime knots up to $8$ crossings, the Franks–Williams–Morton HOMFLY-PT bound $\beta_{\mathrm{FWM}}(K) = \frac{1}{2}(\max\deg_v P_K - \min\deg_v P_K) + 1$ is sharp (`fwm_sharp_all_prime_knots_le8`).
   - All bare-volume near-runners in $[3.16, 3.43]$ are **excluded from $B_3$**:
     - $6_1$ (stevedore, $\mathrm{Vol} = 3.163963228883143984\dots$, $-6.456\%$): exact braid index $\beta(6_1) = 4$.
     - $7_2$ ($\mathrm{Vol} = 3.331744231641114824\dots$, $-1.495\%$): exact braid index $\beta(7_2) = 4$.
     - $8_1$ ($\mathrm{Vol} = 3.427205246274016220\dots$, $+1.327\%$): exact braid index $\beta(8_1) = 5$.
     - $7_4, 7_6, 7_7$ likewise have $\beta(K) = 4$.
   - Up to $7$ crossings, there are **exactly six** prime hyperbolic 3-braids: $\{4_1, 5_2, 6_2, 6_3, 7_3, 7_5\}$ (`complete_hyperbolic_three_braid_census`). Removing $\mu^- = 4_1$ leaves **five** primary candidates $\{5_2^-, 6_2^-, 6_3, 7_3^-, 7_5^-\}$, whose bare volumes jump across the target gap from $\mathrm{Vol}(5_2) = 2.828122\dots$ ($-16.385\%$) directly to $\mathrm{Vol}(6_2) = 4.400833\dots$ ($+30.113\%$).
   - Among all $10$ prime hyperbolic $8$-crossing 3-braids $\{8_2, 8_5, 8_7, 8_9, 8_{10}, 8_{16}, 8_{17}, 8_{18}, 8_{20}, 8_{21}\}$, the minimum volume is $\mathrm{Vol}(8_{20}) = 4.124903251807676156\dots$ ($+21.955\%$).

2. **All Pre-Registered Maps Miss the $< 1\%$ Gate**:
   - **No candidate** in $\{5_2^-, 6_2^-, 6_3, 7_3^-, 7_5^-\}$ achieves $< 1\%$ relative error under `Map A`, `Map B`, `Map B_PSL2`, `Map C1`, `Map C1u`, `Map C2a`, or `Map C2b`.
   - Closest primary evaluation is **$5_2^-$ under `Map C2a`** ($2911.191$, **$-16.278\%$** vs CODATA-2022), followed by $5_2^-$ under `Map A` ($2907.486$, $-16.385\%$), $5_2^-$ under `Map B` ($4256.678$, $+22.416\%$), and Gate-G2 unique winner $6_2^-$ under `Map C1u` ($4448.488$, $+27.932\%$) / `Map C1` ($4476.464$, $+28.737\%$).
   - Per `PREREGISTRATION.md` §1.3, the probe records `selected = "none"` and `LowCrossingThreeBraidTauSelection.lean` isolates the unresolved tau carrier and loop-dressing datum as the zero-instance class `TauHyperbolicThreeBraidCarrierHypothesis` under **Rule 13a**.

---

## 2. Exact 80-dps Invariants & Pre-Registered Mass-Map Evaluations

### 2.1 Exact Geometric & Cohomological Invariants ($w \le 0$ Chiral Branch)

| Knot $K$ | Gate Uniqueness | $\mathrm{Vol}(K)$ (exact $\overline{\mathbb{Q}}$ spinor) | $\mathrm{CS}_{2\pi^2}(K)$ | $|\mathbb{T}_{\mathrm{Ad}}(K; \mu)|$ | $|T_{\mathrm{Reid}}(K; q_0)/T_{\mathrm{Reid}}(K; 1)|$ | $\widehat{W}_{\mathrm{alg}}(K; q_0)$ |
|---|---|---:|---:|---:|---:|---:|
| $4_1$ ($\mu^-$) | `CAL-2` ($w=0$) | `2.029883212819307250` | `0` | `1.732050807568877294` ($\sqrt{3}$) | `1.003672208269074195` | `0.1552469503` |
| $5_2^-$ | G1 ($w=-4$) | `2.828122088330783163` | `+3.024128376509301660` | `2.322325476267820146` | `1.001248196452638848` | `0.0763281699` |
| $6_2^-$ | **G2 unique** ($w=-2$) | `4.400832516123046101` | `-5.872562693630051519` | `4.433179861782237813` | `1.000914314499508789` | `0.2853884687` |
| $6_3$ | **G3 unique** ($w=0$) | `5.693021091281300765` | `0` | `5.752796543037491191` | `1.004675645658909876` | `0.3081201154` |
| $7_3^-$ | G1 ($w=-6$) | `4.592125697027062550` | `-3.695578187060886850` | `5.543482780497809560` | `1.000871248105330129` | `-0.0797183696` |
| $7_5^-$ | G1 ($w=-6$) | `6.443537380850573086` | `-2.379677470747391404` | `8.458473236186071510` | `1.003503041141925694` | `-0.0321209288` |

### 2.2 Predicted $m_\tau / m_e$ Ratios & Signed Percentage Errors vs CODATA-2022 ($3477.23$)

| Knot $K$ | `Map A` ($\mathrm{Vol}/\hbar^3$) | `Map B` ($|\mathrm{Vol}+i\mathrm{CS}_{2\pi^2}|/\hbar^3$) | `Map C1` (1-loop $\ln|\mathbb{T}/\mathbb{T}_{4_1}|$) | `Map C2a` (`#9213` cone + $W_{\mathrm{alg}}$) | `Map C2b` ($\sqrt{3}/|\mathbb{T}_{\mathrm{Ad}}|$) |
|---|---:|---:|---:|---:|---:|
| $5_2^-$ | `2907.49` (`-16.385%`) | `4256.68` (`+22.416%`) | `2892.55` (`-16.815%`) | **`2911.19` (`-16.278%`)** | `2168.48` (`-37.638%`) |
| $6_2^-$ | `4524.33` (`+30.113%`) | `7544.49` (`+116.968%`) | `4476.46` (`+28.737%`) | `4528.75` (`+30.240%`) | `1767.66` (`-49.165%`) |
| $6_3$ | `5852.78` (`+68.317%`) | `5852.78` (`+68.317%`) | `5791.64` (`+66.559%`) | `5880.45` (`+69.113%`) | `1762.15` (`-49.323%`) |
| $7_3^-$ | `4720.99` (`+35.769%`) | `6059.89` (`+74.274%`) | `4661.74` (`+34.065%`) | `4725.02` (`+35.885%`) | `1475.06` (`-57.579%`) |
| $7_5^-$ | `6624.36` (`+90.507%`) | `7061.68` (`+103.083%`) | `6543.59` (`+88.184%`) | `6647.53` (`+91.173%`) | `1356.48` (`-60.990%`) |

*(Why `Map B` and `Map C` cannot rescue Option 2A: for $5_2^-$, $\mathrm{CS}_{2\pi^2} = +3.024128$ overshoots $3477.23$ by $+22.42\%$; for all knots with $c(K) \in \{6, 7\}$, $\mathrm{Vol}(K) \ge 4.4008 > 3.3823$, so adding $\mathrm{CS}^2 \ge 0$ strictly worsens the overshoot (`complex_volume_sq_ge_real_volume_sq`), 1-loop saddle log-torsion $-\frac{1}{2}\hbar_{q_0}\ln|\mathbb{T}_{\mathrm{Ad}}/\sqrt{3}|$ shifts $\mathrm{Vol}(K)$ by only $-0.047$ to $-0.078$ ($\sim -1.4\%$ to $-2.3\%$), and Murakami's bar-symmetric cone-manifold ratio $|T_{\mathrm{Reid}}(K; q_0)/T_{\mathrm{Reid}}(K; 1)| = 1 + O(\hbar_{q_0}^2) \in [1.00087, 1.00468]$ shifts `Map A` by $+0.09\%$ to $+0.47\%$.)*

---

## 3. Audit & Resolution of Bean `qou-r0dn` (`Vol(6_2)`)

1. **Historical Defect (`qou-r0dn`)**: `docs/audits/2026-08-21-deuteron-knot-assignment-adjudication.md:135` flagged `computations/m_tau_knot_prediction.py` for carrying `"6_2": "4.0597664956578801590"` ($7.75\%$ low, matching $2\,\mathrm{Vol}(4_1) = 4.0597664256\dots$ to 8 digits).
2. **Current Tree Status**: Commit `4552fa0dd5d` (`qou-ckbv`, 2026-08-30) updated the string table in `computations/m_tau_knot_prediction.py:104` to `"4.4008325161230461014"`, and `computations/m-tau-knot-prediction.witness.json` on `origin/main` is stamped under `mpmath 1.4.1`. Because this build environment runs `mpmath 1.3.0`, re-writing `m-tau-knot-prediction.witness.json` here would trigger an `engineVersion` provenance downgrade (`mpmath 1.4.1 -> 1.3.0`), violating the strict witness-provenance hygiene rule.
3. **Zero-Literal Algebraic Verification**: Instead, `LowCrossingThreeBraidTauSelection.lean` proves over `[CommRing R]` (`spinor_closure_6_2`) that $6_2$'s parabolic $B_3$ spinor coordinates are governed by the exact integer quintic
   $$P_{6_2}(x) = x^5 - x^4 - 2x^3 + x^2 + x + 1 = 0, \quad p(x) = -x^3 + 2x, \quad r(x) = -x^4 - x^3 + x^2 + 2x + 1,$$
   and `gap2_mtau_hyperbolic_census_torsion_probe.py` solves $P_{6_2}(x) = 0$ at `mp.dps = 80` with zero decimal literals, obtaining
   $$\mathrm{Vol}(6_2) = 4.4008325161230461014412038656409280339834854185165\dots$$
   and verifying agreement to $< 10^{-48}$ against `substrate/knot_volumes.py` (`qou_r0dn_vol62_exact_quintic_matches_registry_50dps`).
