# Audit & Derivation Ledger: Baryon Octet $\Lambda^0$–$\Sigma^0$ Diquark Exchange, $U_q(\mathfrak{sl}_3)$ Schur Cube, and 2nd-Order Gell-Mann–Okubo / Decuplet Curvature (`qou-8fw2`, `qou-d7h1`, `qou-wyy9`)

**Date:** 2026-11-24  
**Beans:** `qou-8fw2`, `qou-d7h1`, `qou-wyy9` (Issue `#9375`)  
**Pre-Registration:** [`baryon_octet_diquark_gmo_preregistration.md`](../../computations/mesons/baryon_octet_diquark_gmo_preregistration.md) (`ccc7d2b78a0`)  
**80-dps Probe:** [`baryon_octet_diquark_gmo_probe.py`](../../computations/mesons/baryon_octet_diquark_gmo_probe.py)  
**Witness:** [`baryon_octet_diquark_gmo_probe.witness.json`](../../computations/mesons/baryon_octet_diquark_gmo_probe.witness.json)  
**Lean 4 Formalization (`0 sorry`, `0` custom axioms, `§7c` generic):** [`BaryonOctetDiquarkGmoDerivation.lean`](../../folio/quantum-observable-universe/lean/QOU/EightfoldWay/BaryonOctetDiquarkGmoDerivation.lean)

---

## 1. Exact $U_q(\mathfrak{sl}_3)$ Schur–Weyl Cube & Zero-Weight Multiplicity (`schur3_cube_decomposition`, `uq_sl3_weyl_qdim_cube_identity`)

Over any commutative ring $R$, the 3-variable Schur characters $s_{(3)}, s_{(2,1)}, s_{(1,1,1)} \in R[x_1, x_2, x_3]$ satisfy:
$$s_{(3)}(x_1, x_2, x_3) + 2\,s_{(2,1)}(x_1, x_2, x_3) + s_{(1,1,1)}(x_1, x_2, x_3) = (x_1 + x_2 + x_3)^3,$$
with exact zero-weight $(x_1 x_2 x_3)$ multiplicities $(1_{\Sigma^{*0}}, 2_{\Lambda^0 \oplus \Sigma^0}, 1_{\Lambda_1})$ summing to $1 + 2 \cdot 2 + 1 = 6 = |S_3|$ and classical values $(10, 8, 1)$ at $(1, 1, 1)$. Specializing $(x_1, x_2, x_3) = (q^2, 1, q^{-2})$ over any field $K$ (`q ≠ 0, q - q⁻¹ ≠ 0, q + q⁻¹ ≠ 0`) recovers the canonical Weyl quantum dimensions in `qIntBal`:
$$s_{(3)}(q^2, 1, q^{-2}) = \frac{[4]_q[5]_q}{[2]_q} = \frac{[3]_q[4]_q[5]_q}{[2]_q[3]_q}, \qquad s_{(2,1)}(q^2, 1, q^{-2}) = [2]_q[4]_q = [3]_q^2 - 1, \qquad s_{(1,1,1)}(q^2, 1, q^{-2}) = 1,$$
$$\frac{[4]_q[5]_q}{[2]_q} + 2\,[2]_q[4]_q + 1 = [3]_q^3.$$

---

## 2. Temperley–Lieb $(u, d)$ Diquark Exchange $e_{12}$ & Pre-Committed $\Sigma^0 - \Lambda^0$ Scale Catalog (`80 dps`)

Although $\Lambda^0(uds)$ and $\Sigma^0(uds)$ share identical quark content and identical weight $(2I_3, Y_f) = (0, 0)$, on the mixed-symmetry Hecke module $S^{(2,1)}$ the Temperley–Lieb $(u, d)$ diquark exchange operator $e_{12} = q I_2 - \sigma_1$ satisfies $e_{12}^2 = [2]_q e_{12}$, annihilates the $I = 1$ symmetric diquark $P_{\Sigma^0}$ ($\operatorname{Sym}_q^2 V_2$, $\dim_q = [3]_q$), and acts with exact eigenvalue $[2]_q = q + q^{-1}$ on the $I = 0$ antisymmetric diquark $P_{\Lambda}$ ($\Lambda_q^2 V_2$, $\dim_q = 1$). On any hyperfine Hamiltonian $H_{\mathrm{hf}} = M_{uds} I_2 - \kappa_{\mathrm{hf}} e_{12}$, the common $(u,d,s)$ baseline cancels and $\operatorname{tr}(P_{\Sigma^0} H_{\mathrm{hf}}) - \operatorname{tr}(P_{\Lambda} H_{\mathrm{hf}}) = \kappa_{\mathrm{hf}} [2]_q$.

Evaluating the six pre-committed zero-parameter QOU energy combinations (`baryon_octet_diquark_gmo_preregistration.md`) against PDG 2024 $\Delta m_{\Sigma^0 - \Lambda^0} = 1192.642(24) - 1115.683(6) = 76.959(25)\text{ MeV}$:

| Pre-Committed Zero-Parameter Scale Candidate | Value @ $q_{\mathrm{proton}}$ (MeV) | Value @ $q_{\mathrm{muon}}$ (MeV) | Residual vs `76.959 MeV` |
|---|---:|---:|---:|
| **`S1_E0_b3sq_b2`** ($E_0 [3]_q^2 [2]_q$, $E_0 = \frac{m_e}{q(q-1)}$) | **`77.9817 MeV`** | **`77.9817 MeV`** | **`+1.023 MeV` (`+1.329%`)** |
| `S2_E0_dimq8_b2` ($E_0 \dim_q(\mathbf{8}_q) [2]_q = E_0 [2]_q^2 [4]_q$) | `69.5641 MeV` | `69.5641 MeV` | `-7.395 MeV` (`-9.609%`) |
| `S3_mpi_over_b2` ($m_{\pi^\pm} / [2]_q$) | `69.4070 MeV` | `69.4070 MeV` | `-7.552 MeV` (`-9.813%`) |
| `S4_mp_h_over_b3` ($m_p (q - q^{-1}) / [3]_q$) | `64.4462 MeV` | `64.4463 MeV` | `-12.513 MeV` (`-16.259%`) |
| `S5_mp_hbar_b2_over_b3` ($m_p (1 - q^{-1})[2]_q / [3]_q$) | `61.4199 MeV` | `61.4199 MeV` | `-15.539 MeV` (`-20.191%`) |
| `S6_mp_V3_diquark_split` ($m_p \operatorname{tr}_{\mathrm{split}}(V^3)$) | `26.5201 MeV` | `26.5201 MeV` | `-50.439 MeV` (`-65.540%`) |

*(No candidate is selected post-hoc or wired into production; deriving the physical scale $\kappa_{\mathrm{hf}}$ from the confined 3-strand baryon action remains open.)*

---

## 3. 2nd-Order Baryon Octet GMO & Decuplet Curvature Asymmetry (`qCasimir_decuplet_second_differences_and_ratio`)

1. **Baryon Octet GMO Residual:**
   - First-order linear + Casimir breaking $M_0 + a Y + b(I(I+1) - \frac{1}{4}Y^2)$ satisfies $2(M_N + M_\Xi) - (3 M_\Lambda + M_\Sigma) = 0$ identically (`firstOrder_baryon_gmo_and_decuplet_equal_spacing`).
   - In CODATA-2022 / PDG-2024 isospin-averaged masses ($M_N = 938.9188\text{ MeV}$, $M_\Xi = 1318.285\text{ MeV}$, $M_\Sigma = 1193.1537\text{ MeV}$, $M_\Lambda = 1115.683\text{ MeV}$), the doubled residual is $2(M_N + M_\Xi) - (3 M_\Lambda + M_\Sigma) = -25.7952\text{ MeV}$ (half-combination $(M_N + M_\Xi) - \frac{3 M_\Lambda + M_\Sigma}{2} = -12.8976\text{ MeV}$; neutral-only $2(m_n + m_{\Xi^0}) - 3 m_{\Lambda^0} - m_{\Sigma^0} = -30.8402\text{ MeV}$).
   - Under the rational quantum Casimir $d_q(I, Y) = [I]_q[I+1]_q - [Y/2]_q^2$, the parameter-free universal ratio $-\left(\frac{q-1}{q+1}\right)^2 = -0.00271682$ predicts $-0.2105\text{ MeV}$ (`0.816%` of the empirical magnitude, matching the negative sign on baryons and positive sign on mesons simultaneously), whereas the weighted Jucys–Murphy operator gives $\mathrm{GMO}/(M_\Xi - M_N) = +0.01854$ (`u < d < s`) vs $-0.01839$ (`s < u < d`) against PDG $-0.06800$ (order-dependent sign and reversed $\Lambda > \Sigma^0$ ordering).
2. **Decuplet Second-Difference Asymmetry & Parameter-Free Sign Falsification:**
   - Evaluating $d_q(I, Y)$ on $\Delta(\frac{3}{2}, +1), \Sigma^*(1, 0), \Xi^*(\frac{1}{2}, -1), \Omega^-(0, -2)$ breaks the classical quadratic-ansatz identity `spacingUpper = spacingLower` with the exact $(M_0, a, c)$-free ratio:
     $$\frac{M_{\Omega^-} - 2 M_{\Xi^*} + M_{\Sigma^*}}{M_{\Xi^*} - 2 M_{\Sigma^*} + M_\Delta} = \frac{1}{q + 1 + q^{-1}} = 0.33213 \quad (\to \tfrac{1}{3} \neq 1 \text{ as } q \to 1).$$
   - However, fixing $c_{\mathrm{octet}} = (M_\Sigma - M_\Lambda)/[2]_q = +38.5254\text{ MeV} > 0$ yields **positive** $q$-Casimir decuplet second differences (`+0.9489 MeV` lower, `+0.3151 MeV` upper), opposite in sign to PDG 2024 (`-3.7533 MeV` lower, `-9.7733 MeV` upper, ratio `+2.6039`), proving cleanly that empirical decuplet curvature is dominated by non-octet chiral/threshold effects rather than pure $d_q(I, Y)$ tree deformation.
