# Euler–Poincaré Obstructions and Pauli–Wigner Extensive Cell-Sum Carriers for Nuclear $b_3$

**Date:** 2026-11-24
**Beans:** `qou-eptr`, `qou-q8vl` (towards open kernel `qou-brng`; per `AGENTS.md` §13a `qou-brng` stays open)
**Lean 4 Module:** `folio/quantum-observable-universe/lean/QOU/MassTheory/B3ExtensiveCellSumCarrier.lean` (`0 sorry`, generic `[CommRing R]` / `[Field F] [LinearOrder F] [IsStrictOrderedRing F]`)
**80-dps Probe & Witness:** `computations/probes/b3_extensive_ep_cell_carrier_probe.py` / `computations/probes/b3-extensive-ep-cell-carrier-probe.witness.json` (`mpmath` 80 dps + `sympy` over $\mathbb{Q}(q)$, `q0Anchor: "comparison"`, zero `float64`, zero fitting)

---

## 1. Executive Summary

Beans `qou-eptr` and `qou-q8vl` isolate two complementary barriers to deriving the connected three-body nuclear binding cumulant
$$b_3^{\mathrm{AME,sym}} := \frac{B({}^3\mathrm{H}) + B({}^3\mathrm{He})}{2} - 3\,B({}^2\mathrm{H}) = +1.42622016\;\mathrm{MeV}$$
(positive in the binding-energy sign convention $B > 0$, meaning three-nucleon shells bind super-pairwisely relative to three deuterons, vs $b_3 = 0$ in pair-local Symbolic Q-CLT and $b_3 < 0$ on single-bond chains):

1. **Geometric Epstein–Penner & Homological Euler–Poincaré Route (`qou-eptr`, Route A — Proved Obstructions):**
   - **Light-end & Hecke-element obstruction:** ${}^2\mathrm{H}$ has $\mathrm{Vol} = 0$ (non-hyperbolic by Thurston's trichotomy), the legacy knot lookup collapses $A \ge 4$ onto `L6a4` (`constant_above_four_not_extensive`), and `atom_canonical_crossings(Z, N)` has $12A - 1$ letters splitting for every $A \ge 2$ into $10A - 2$ pure braid crossings ($b_3 = 28 - 3(18) = -26 < 0$, `layeredBraidCell_b3_eq_neg_26`) plus $2A$ `averaged` and $1$ `averaged_weighted` non-braid Hecke letters outside $\mathrm{im}(B_{3A} \to H_{3A}(q))$, so no Alexander/Markov 3-manifold closure exists.
   - **Topological & homological sign inversion:** On any contractible simplicial complex $\mathcal{K}_A$ on $A$ vertices, the unweighted reduced Euler–Poincaré cell sum $\widetilde{\chi}(\mathcal{K}_A) = c_1 - c_2 + c_3$ collapses identically to $A - 1$ (`contractible_ep_reduced_eq_sub_one`), forcing $b_3 = -1 < 0$ (`contractible_ep_b3_eq_neg_one`). Under $q$-graded weights $(w_1, w_2, w_3)$ on $\Delta^{A-1}$, homological $(-1)^{d-1}$ Euler–Poincaré sign alternation yields $b_3 = -w_2 < 0$ for all $w_2 > 0$ (`simplexEp_b3_eq_neg_w2`) — the cellular dual of Mayer/Ursell sign alternation (`UrsellPartitionFunctionB3`). Flipping from alternating homology to the **unsigned positive-measure simplex cell sum** yields $b_3 = +w_2 > 0$ and $b_4 = +w_3 > 0$ (`simplexUnsigned_b3_eq_pos_w2`, `simplexUnsigned_b4_eq_pos_w3`).

2. **Pauli–Wigner Intra-Shell Bratteli Cell-Sum Carrier (`qou-eptr` + `qou-q8vl`, Route B — Proved Extensivity, Sign Escape & 80-dps Probe):**
   - **Global vs intra-shell Young-diagram content:** Summing global content $j - i$ across $m$ filled 4-column Wigner $SU(4)$ shells ($A = 4m$) gives $6m - 2m(m - 1)$ with constant negative second difference $-4$ (`globalContent_second_diff_eq_neg_four`, non-extensive $-A^2/8$ Pauli drift). By contrast, the $(Z, N)$-resolved **intra-shell Pauli–Wigner cell sum**
     $$S_\phi(Z, N) = \sum_{\text{shell } i} \sum_{j=0}^{r_i(Z, N) - 1} \phi(j), \qquad \phi(0) = 0, \quad r_i(Z, N) = \min(2, Z_{\mathrm{rem}}) + \min(2, N_{\mathrm{rem}}) \in \{1, 2, 3, 4\},$$
     requires no 3-manifold closure (well-defined on ${}^2\mathrm{H}$ with $S_\phi(1, 1) = \phi(1)$), scales strictly linearly on $\alpha$-conjugate nuclei $S_\phi(2m, 2m) = m(\phi(1) + \phi(2) + \phi(3))$ (`pauliWignerCellSum_alpha_mul`, escaping `exchangeDet_pow_two_le_four`), and satisfies exact cumulants
     $$b_3(S_\phi) = \phi(2) - 2\,\phi(1), \qquad b_4(S_\phi) = \phi(3) - 3\,\phi(2) + 3\,\phi(1)$$
     (`pauliWigner_b3_eq`, `pauliWigner_b4_eq`).
   - **Discrete convexity escape (`qou-q8vl`) & Pauli three-body filter:** Over any strict ordered ring, $b_3(S_\phi) > 0 \iff 2\,\phi(1) < \phi(2)$ (`pauliWigner_b3_pos_iff`), escaping `(0, 1)` multiplicative chain confinement (`B3SignOneRoot`) with zero bond factors above $1$. Simultaneously, Fermi–Pauli spin exclusion splits $(0, 3)$ and $(3, 0)$ into rows `[2, 1]` while $(1, 2)$ and $(2, 1)$ occupy a single width-3 shell `[3]`, giving $S_\phi(1, 2) - S_\phi(0, 3) = \phi(2)$ (`pauliWigner_triton_sub_trineutron`) and an exact $|N - Z|$ Wigner symmetry deficit at fixed $A$ (`pauliWignerCellSum_alpha_plus_excessPairs`).
   - **Zero-parameter $\mathbb{Q}(q)$ kernels at 80 dps (`q_p` and `q_mu`, zero fitting):**
     - **Quantum integer content $\phi(j) = [j]_q \, w_1$ (`M3`):** $b_3 = \frac{(q-1)^2}{q} w_1 > 0$ (`qInt_b3_and_b4_pos`), right sign on both $b_3$ and $b_4$, but $O(\hbar_q^2)$-suppressed at $+0.0225679\;\mathrm{MeV}$ ($63.2\times$ below $b_3^{\mathrm{AME,sym}}$).
     - **Unsigned Wenzl-normalised quantum simplex carrier $\phi_{\mathrm{qSimplex}}(j) = E_0^{\mathrm{tower}} \sum_{d=1}^3 \frac{\binom{j}{d}_q}{[d+1]_q}$ (`M4`, working-assumption probe):**
       $$\frac{b_2}{E_0^{\mathrm{tower}}} = \frac{q}{q^2 + 1}, \qquad \frac{b_3}{E_0^{\mathrm{tower}}} = \frac{(q - 1)^2}{q^2 + 1} + \frac{q^2}{q^4 + q^2 + 1} > 0 \quad (\forall q > 0)$$
       (`qSimplex_b2_and_b3_eq`, `qSimplex_b3_pos`), giving at $q_p = q_{\mathrm{at}}(80)$ ($E_0^{\mathrm{tower}} = 4.2274833556\;\mathrm{MeV}$):
       - $b_2 = \mathbf{+2.10228750\;\mathrm{MeV}}$ vs $B({}^2\mathrm{H}) = 2.2245662\;\mathrm{MeV}$ ($-5.50\%$),
       - $b_3 = \mathbf{+1.41183457\;\mathrm{MeV}}$ vs $b_3^{\mathrm{AME,sym}} = +1.42622016\;\mathrm{MeV}$ (**$-1.0087\%$**, cross-anchor swing $q_p$ vs $q_\mu$: $126.30\;\mathrm{ppb}$),
       - $b_4 = \mathbf{+1.11252692\;\mathrm{MeV}} > 0$ vs $b_4^{\mathrm{AME,sym}} = +9.24338456\;\mathrm{MeV}$,
       - By contrast, restoring the $(-1)^{d-1}$ Euler–Poincaré sign (`M2`, `epQSimplex_b3_neg_of_mem_Icc`) flips $b_3$ to $\mathbf{-1.36601787\;\mathrm{MeV} < 0}$.

---

## 2. Symbolic $\mathbb{Q}(q)$ Closed Forms & 80-dps Benchmark Table (Proton Pin $q_p$)

All models below use zero fitted parameters and zero superseded single-crossing `atom_braid_word_3A` bond shifts (`docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`), depending solely on $(q_0, m_e)$ via $E_0^{\mathrm{tower}} = \frac{m_e}{q_0(q_0 - 1)(1 - \hbar_q^2)}$ and $z_D = \frac{q_0^3}{q_0^2 + 1}$ ($w_1 = E_0^{\mathrm{tower}} \ln(1/z_D) = 2.07104149\;\mathrm{MeV}$):

| Carrier Model (`zero fitting`) | $b_2$ (MeV) | $b_3$ (MeV) | $b_4$ (MeV) | Light $A \in \{3,4,6,12,16\}$ ($n=6$) MAE($B/A$) | Light All Isobars ($n=22$) MAE($B/A$) | Med/Heavy $A=16..240$ ($n=2385$) MAE($B/A$) | Med/Heavy RMSE($B/A$) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **AME2020 Reference** | `2.22457` | **`+1.42622`** | `+9.24338` | `0` | `0` | `0` | `0` |
| `M0_chain_zD`: $(A-1) w_1$ | `2.07104` | `-2.07104` | `+2.07104` | `3.93033` | `3.36438` | `6.10636` | `6.12137` |
| `M1_pw_shell_zD_b3_zero`: $c_1(Z,N) w_1$ | `2.07104` | `0` | `0` | `2.93076` | `2.75640` | `5.38306` | `5.39699` |
| `M2_ep_alternating_qSimplex` (`(-1)^{d-1}`) | `2.10229` | `-1.36602` | `+0.99112` | `3.72598` | `3.39293` | `6.27985` | `6.29288` |
| `M3_qInt_bratteli_zD`: $S_{[j]_q} w_1$ | `2.07104` | `+0.02257` | `+0.02281` | `2.91098` | `2.74002` | `5.35939` | `5.37336` |
| **`M4_unsigned_qSimplex_wenzl`** ($\sum_{d=1}^3 \frac{\binom{j}{d}_q}{[d+1]_q} E_0^{\mathrm{tower}}$) | **`2.10229`** | **`+1.41183`** | **`+1.11253`** | **`1.70128`** | **`1.76185`** | **`3.92621`** | **`3.94545`** |
| `M5_unsigned_simplex_uniform_zD`: $(c_1+c_2+c_3) w_1$ | `2.07104` | `+2.07104` | `+2.07104` | `1.18150` | `1.30510` | `3.21591` | `3.24117` |

*(Exact 24- to 80-digit values for both `proton` and `muon` pins, including all 22 non-estimated light isobars at $A \in \{3,4,6,12,16\}$, are recorded in `computations/probes/b3-extensive-ep-cell-carrier-probe.witness.json`.)*

---

## 3. Honest Limitations & What Remains Open (`qou-brng`)

1. **Working-assumption status of the $1/[d+1]_q$ Wenzl simplex measure:** While `M4_unsigned_qSimplex_wenzl` has **zero free parameters** and lands at $b_3 = +1.41183457\;\mathrm{MeV}$ ($-1.0087\%$ from $b_3^{\mathrm{AME,sym}} = +1.42622016\;\mathrm{MeV}$) while separating bound ${}^3\mathrm{H}/{}^3\mathrm{He}$ ($7.71869708\;\mathrm{MeV}$) from Pauli-split ${}^3\mathrm{n}$ ($2.10228750\;\mathrm{MeV}$, $\Delta = \phi(2) = +5.61640957\;\mathrm{MeV}$), deriving the unsigned $1/[d+1]_q$ intra-shell sum from the full $3A$-strand $\gamma\gamma$-selected Hecke trace (`PR #7876`) remains open and is formalized as the `§3b-cond` hypothesis class `ExtensiveShellCarrierHypotheses` in `B3ExtensiveCellSumCarrier.lean`.
2. **Four-body $b_4$ and inter-shell $\alpha$–$\alpha$ + Coulomb structure at $A \ge 4$:** Purely intra-shell carriers have constant $\alpha$-conjugate bulk slope $B(4m)/(4m) = B(4)/4$ ($4.8434\;\mathrm{MeV}/A$ for `M4`), leaving an $8.13\;\mathrm{MeV}$ 4-body shortfall on ${}^4\mathrm{He}$ ($19.3736$ vs $28.2957\;\mathrm{MeV}$) and a $\sim 3.93\;\mathrm{MeV}/A$ medium/heavy shortfall where inter-shell $\alpha$–$\alpha$ contacts and $Z(Z-1)/A^{1/3}$ Coulomb repulsion govern the curve (`assembly_shortfall_shape_probe.py`). Neither `qou-eptr`, `qou-q8vl`, nor `qou-brng` is closed by this probe (`AGENTS.md` §13a).
