# Pre-Registration: Closing Open Gap 1 (Option 1A) — ${}^4\mathrm{He}$ $12$-Quark Pauli Antisymmetrizer & Wigner $\mathrm{SU}(4)$ Spin-Isospin Chromomagnetic Binding (2026-11-23)

Branch: `claude/gap1-4he-wigner-pauli-12q-20261123` (off `origin/main` `e330ab6aa04`).
Written, committed, and pushed **before** running any numerical evaluation of the $6q/9q/12q$ colour-spin-isospin Hamiltonians, Schur-complement shifts, Lanczos eigenvalues, or AME2020/CODATA-2022 MeV comparisons.

---

## 1. Context, Prior Baseline (`#9221`), and Exact Mathematical Scope

On `origin/main` (`ColourReconnectionStokesAssembly.lean` + `computations/probes/w4_colour_reconn_stokes_aomega/`), pure $\mathrm{SU}(3)_c$-singlet colour reconnection on Hoefsmit's irreducible module $S^{[A,A,A]}_{H_{3A}(q_0)}$ ($\dim = 1, 5, 42, 462$ for $A = 1, 2, 3, 4$) with intra-cluster central Casimir gap $H_{\mathrm{G2}}$ and inter-nucleon Fierz coupling $V_{\mathrm{V2}}$ yielded in the $E_{\mathrm{osc}}(q_0) = m_e / (q_0 - 1)^2 = 42.2478\text{ MeV}$ chart:
- $A = 2$ (${}^2\mathrm{H}$): $2.2648\text{ MeV}$ ($+1.81\%$ vs CODATA/AME $2.2246\text{ MeV}$),
- $A = 3$ (${}^3\mathrm{H}/{}^3\mathrm{He}$): $5.1059\text{ MeV}$ (vs $8.4818 / 7.7180\text{ MeV}$),
- $A = 4$ (${}^4\mathrm{He}$): $14.4877\text{ MeV}$ ($-48.8\%$ vs $28.2956\text{ MeV}$), scaling as $1 : 2.254 : 6.397$ instead of the empirical $1 : 3.813 : 12.720$.

Algebraic preflight identifies two purely structural omissions in `#9221`:
1. **Spin-isospin Pauli antisymmetry (`[1^{3A}]`):** For $3A$ light quarks ($u, d$) in a symmetric $s$-wave spatial configuration $[3A]$, Fermi statistics forces total colour-spin-isospin antisymmetry $[1^{3A}]$ under $S_{3A}$. By Schur–Weyl duality and Frobenius reciprocity ($\dim \operatorname{Hom}_{S_n}([1^n], S^\lambda \otimes S^\mu) = \delta_{\mu, \lambda'}$), the $\mathrm{SU}(3)_c$-singlet colour Specht module $S^{[A,A,A]}_{\mathrm{col}}$ pairs **uniquely** with the conjugate spin-isospin Specht module $S^{[3^A]}_{\sigma\tau}$ ($[A,A,A]' = [3^A]$, $A$ rows of length $3$). In `#9221`, spin-isospin was omitted, so:
   - horizontal quark pairs in $[A,A,A]$ carried repulsive colour eigenvalue $+q_0$ without the compensating column antisymmetry $-q_0^{-1}$ of $[3^A]$, and
   - exciting a $3q$ cluster $[1,1,1]_{\mathrm{col}} \to [2,1]_{\mathrm{col}}$ without simultaneously exciting $[3]_{\sigma\tau} \to [2,1]_{\sigma\tau}$ violated intra-nucleon $S_3$ Fermi statistics ($\operatorname{Hom}_{S_3}([1^3], [2,1] \otimes [3]) = 0$, whereas $\operatorname{Hom}_{S_3}([1^3], [2,1] \otimes [2,1]) \cong \mathbb{C}$).
2. **Braid-transport word ordering in `#9221` `V2`:** In `w4_colour_reconn_stokes_aomega_probe.py`, the non-adjacent pair word (`prefix` / `suffix`) applied generators in reversed order under right-to-left evaluation, causing $(a, b) = (0, 2), (0, 3), (1, 3)$ to act on adjacent chain interfaces rather than forming the true complete graph $K_A$ (giving 2nd-order ratios $1 : 1.990 : 5.035$ instead of $1 : 3 : 6$).

Companion Lean 4 module (`0 sorry`, `0` custom `axiom`s, generic `§7c` rings/fields + `_real` bridge, zero empirical literals):
- `folio/quantum-observable-universe/lean/QOU/Nuclear/TwelveQuarkWignerPauliBinding.lean`

---

## 2. Pre-Registered Algebraic Theorems & 80-dps Verifications (Zero Free Parameters)

### Part A — Conjugate Young-Diagram Pairing, Wigner $\mathrm{SU}(4)_{\sigma\tau}$ Shell Closure & Chromomagnetic Operator $\mathcal{O}_{\mathrm{CM}}$

1. **Hook-Length Equivalence, $\mathrm{SU}(4)_{\sigma\tau}$ Multiplicity & $A = 5$ Pauli Shell Closure:**
   - Verify `[A, A, A]' = [3^A]` (`colThree A`), $\dim S^{[3^A]} = \dim S^{[A,A,A]} = d_A \in \{1, 5, 42, 462\}$ ($A = 1..4$), and the exact $\mathrm{SU}(4)_{\sigma\tau}$ Weyl hook-content dimensions:
     $$\dim V^{\mathrm{SU}(4)_{\sigma\tau}}_{[3^A]} = \prod_{(i,j) \in [3^A]} \frac{4 + j - i}{h_{[3^A]}(i,j)} = (20,\; 50,\; 20,\; \mathbf{1},\; \mathbf{0}) \quad \text{for } A = (1, 2, 3, 4, 5),$$
     together with nucleon-level Wigner supermultiplet dimensions $\dim \Lambda^A(\mathbf{4}_N) = \binom{4}{A} = (4, 6, 4, 1, 0)$ and exact $(S=1, T=0)$ vs $(S=0, T=1)$ pair counts $N_{(1,0)}(A, S, T) = \frac{1}{4}A(A-1) + \frac{1}{4}(S(S+1) - T(T+1))$.
   - At $A = 4$ (${}^4\mathrm{He}$), $\dim V^{\mathrm{SU}(4)_{\sigma\tau}}_{[3,3,3,3]} = 1$ (unique $(S=0, T=0)$ Wigner singlet; all $\Delta$ resonances Pauli-blocked in the global $\mathrm{SU}(4)$ weight space), and at $A \ge 5$, $\dim V^{\mathrm{SU}(4)_{\sigma\tau}}_{[3^A]} = 0$ (exact $12$-quark $1s$-shell closure).

2. **Exact $\mathrm{SU}(4)_{\sigma\tau}$ Casimir & Chromomagnetic Operator $\mathcal{O}_{\mathrm{CM}}$ on $\mathcal{H}_{\mathrm{phys}}(A)$:**
   - Verify the exact content sums $\kappa([3^A]) = \frac{3}{2}A(3 - A) \in \{3, 3, 0, -6\}$, quadratic Casimir $C_2^{\mathrm{SU}(4)}([3^A]) = \kappa([3^A]) + \frac{3A(16 - 3A)}{8} \in \{\frac{63}{8}, \frac{21}{2}, \frac{63}{8}, 0\}$, and exact chromomagnetic identity on $(0s)^{3A}$ totally antisymmetric states:
     $$\mathcal{O}_{\mathrm{CM}}(3A, [3^A], S, T) = -\sum_{1 \le i < j \le 3A} (\lambda_i \cdot \lambda_j)(\sigma_i \cdot \sigma_j) = 3A(3A - 5) - 2\kappa([3^A]) + \frac{4}{3} S(S+1) + 4 T(T+1).$$
   - Cross-check by explicit microscopic $6$-quark tensor evaluation on $(0s)^6$: $\mathcal{O}_{\mathrm{CM}}(N) = -8$, $\mathcal{O}_{\mathrm{CM}}(\Delta) = +8$, $\mathcal{O}_{\mathrm{CM}}((0s)^6; S=1,T=0) = +8/3$ ($\Delta\mathcal{O}_{\mathrm{CM}} = +56/3$ short-range repulsive core), $\mathcal{O}_{\mathrm{CM}}((0s)^6; S=0,T=1) = +8$ ($\Delta\mathcal{O}_{\mathrm{CM}} = +24$, $+\frac{16}{3}$ more repulsive than deuteron), Matveev–Sorba / Harvey cluster weights $(P_{NN}, P_{\Delta\Delta}, P_{88}) = (1/9, 4/45, 4/5)$, general hidden-colour fraction $P_{\mathrm{hid}}(\Psi_{\mathrm{Pauli}}(A)) = (d_A - 1)/d_A \in \{0, 4/5, 41/42, 461/462\}$, and exact Pauli antisymmetrizer norm $\langle NN | \mathcal{A}_6 | NN \rangle = 1/9$ from $\langle P_{3,4}^{\mathrm{col}}\rangle = +1/3$ and $\langle P_{3,4}^{\sigma\tau}\rangle_{\Lambda^2(\mathbf{4}_N)} = -1/27$.

3. **Exact $q_0$-Deformed Hoefsmit Conjugate-Duality & Pauli Invariance:**
   - Build Hoefsmit generators independently on $S^{[A,A,A]}(q_0)$ and $S^{[3^A]}(q_0)$ at 80 dps for $A = 2, 3, 4$, and certify that for every generator $0 \le k < 3A - 1$ and every positive-braid-conjugated inter-nucleon strand transposition $\mathcal{B}_{s,t}(q_0) = \check{R}_s^{-1}\cdots\check{R}_{t-2}^{-1}\check{R}_{t-1}\check{R}_{t-2}\cdots\check{R}_s$ ($s < t$):
     $$\check{R}_k^{[3^A]}(q_0) = -D_\eta \bigl(\check{R}_k^{[A,A,A]}(q_0)\bigr)^{-1} D_\eta, \qquad \Bigl(\mathcal{B}_{s,t}^{[A,A,A]}(q_0) \otimes \mathcal{B}_{s,t}^{[3^A]}(q_0)\Bigr) |\Psi_{\mathrm{Pauli}}(A; q_0)\rangle = -|\Psi_{\mathrm{Pauli}}(A; q_0)\rangle,$$
     where $|\Psi_{\mathrm{Pauli}}(A; q_0)\rangle = d_A^{-1/2} \sum_{T \in \mathrm{SYT}([A,A,A])} \eta(T) |T\rangle_{[A,A,A]} \otimes |T'\rangle_{[3^A]}$.

---

### Part B — Six Pre-Registered Zero-Parameter Colour-Spin-Isospin Hamiltonians ($A = 2, 3, 4$)

Let $C_a = \{3a, 3a+1, 3a+2\}$ denote the quarks of nucleon $a \in \{0, \dots, A-1\}$, let $|\Phi_{\mathrm{fac}}^{(A)}\rangle = |T_{\mathrm{fac}}^{\mathrm{col}}\rangle \otimes |T_{\mathrm{fac}}^{\sigma\tau}\rangle$ be the unique factorized $A$-nucleon state ($T_{\mathrm{fac}}^{\sigma\tau} = (T_{\mathrm{fac}}^{\mathrm{col}})'$), and let $\mathcal{D}_{\mathrm{Pauli}}(A) = \operatorname{span}\{ |e_T\rangle := \eta(T)|T\rangle_{[A,A,A]} \otimes |T'\rangle_{[3^A]} \}$ ($\dim = d_A \in \{5, 42, 462\}$) be the conjugate-tableau Pauli carrier. Define the central intra-cluster ribbon full-twist Casimir gaps:
$$H_{\mathrm{col, G2}}^{(A)}(q_0) = \sum_{a=0}^{A-1} \frac{(\check{R}_{3a}^{\mathrm{col}}\check{R}_{3a+1}^{\mathrm{col}}\check{R}_{3a}^{\mathrm{col}})^2 - q_0^{-6} I}{q_0 - q_0^{-1}}, \qquad H_{\sigma\tau, \mathrm{G2}}^{(A)}(q_0) = \sum_{a=0}^{A-1} \frac{q_0^6 I - (\check{R}_{3a}^{\sigma\tau}\check{R}_{3a+1}^{\sigma\tau}\check{R}_{3a}^{\sigma\tau})^2}{q_0 - q_0^{-1}}.$$
Both vanish on $|\Phi_{\mathrm{fac}}^{(A)}\rangle$ and have strictly positive single-cluster $[2,1]$ eigenvalues $q_0^{-3}[3]_{q_0}$ and $q_0^{+3}[3]_{q_0}$ respectively (both $\to 3$ as $q_0 \to 1$).

We pre-register and report verbatim all **six** parameter-free models across $A = 2, 3, 4$:
1. **`M0_w4_baseline_colour_V2`:** Exact reproduction of `#9221`'s `G2_intra_casimir__V2_allpairs_fierz` on $S^{[A,A,A]}(q_0)$ as regression baseline.
2. **`M1_colour_only_true_KA_fierz`:** Pure colour $S^{[A,A,A]}(q_0)$ with $H_{\mathrm{col, G2}}^{(A)}(q_0)$ and the **corrected** $K_A$ positive-braid Fierz coupling $V_{\mathrm{M1}}^{(A)}(q_0) = \frac{1}{2}\sum_{0 \le a < b < A} \bigl(\mathcal{B}_{3a+2, 3b}^{[A,A,A], \mathrm{sym}}(q_0) - d_{ab}^{\mathrm{col}} I\bigr)$, isolating the pure $K_A$ braid-transport fix without spin-isospin.
3. **`M2_pauli_conjugate_KA_G2col`:** Conjugate-tableau Pauli carrier $\mathcal{D}_{\mathrm{Pauli}}(A)$ with $H_{\mathrm{col, G2}}^{(A)}(q_0)$ and $K_A$ Fermi-antisymmetric colour $\otimes$ $[3^A]$ spin-isospin exchange:
   $$V_{\mathrm{Pauli}, K_A}^{(A)}(q_0) = -\frac{1}{2} \sum_{0 \le a < b < A} \Bigl(\Pi_{\mathcal{D}}\bigl(\mathcal{B}_{3a+2, 3b}^{[A,A,A]}(q_0) \otimes \mathcal{B}_{3a+2, 3b}^{[3^A]}(q_0)\bigr)\Pi_{\mathcal{D}} - d_{ab}^{\mathrm{Pauli}} I\Bigr).$$
4. **`M3_pauli_conjugate_KA_G2barsym`:** Same $V_{\mathrm{Pauli}, K_A}^{(A)}(q_0)$ on $\mathcal{D}_{\mathrm{Pauli}}(A)$ paired with the bar-symmetric ($q_0 \leftrightarrow q_0^{-1}$) colour + Wigner $\mathrm{SU}(4)$ Casimir half-sum gap $\frac{1}{2}\bigl(H_{\mathrm{col, G2}}^{(A)}(q_0) + H_{\sigma\tau, \mathrm{G2}}^{(A)}(q_0)\bigr)$.
5. **`M4_pauli_all9_baryon_norm_G2sum`:** All-$9$-inter-nucleon-quark-pair Pauli exchange on $\mathcal{D}_{\mathrm{Pauli}}(A)$ with large-$N_c$ per-baryon normalization ($N_c = 3$) and full additive colour + spin-isospin Casimir gap $H_{\mathrm{col, G2}}^{(A)}(q_0) + H_{\sigma\tau, \mathrm{G2}}^{(A)}(q_0)$:
   $$V_{\mathrm{all9}, N_c}^{(A)}(q_0) = -\frac{1}{2 N_c} \sum_{0 \le a < b < A} \sum_{s \in C_a} \sum_{t \in C_b} \Bigl(\Pi_{\mathcal{D}}\bigl(\mathcal{B}_{s,t}^{[A,A,A]}(q_0) \otimes \mathcal{B}_{s,t}^{[3^A]}(q_0)\bigr)\Pi_{\mathcal{D}} - d_{s,t}^{\mathrm{Pauli}} I\Bigr).$$
6. **`M5_pauli_all9_pair_avg_G2barsym`:** All-$9$-inter-nucleon-quark-pair average ($1/(2 N_c^2) = 1/18$ per quark pair) on $\mathcal{D}_{\mathrm{Pauli}}(A)$ with bar-symmetric Casimir half-sum gap $\frac{1}{2}\bigl(H_{\mathrm{col, G2}}^{(A)}(q_0) + H_{\sigma\tau, \mathrm{G2}}^{(A)}(q_0)\bigr)$, plus exact unprojected $25 \times 25$ full-tensor $\mathcal{W}_2(q_0) = S^{[2,2,2]}(q_0) \otimes S^{[3,3]}(q_0)$ diagonalization at $A = 2$ auditing off-$\mathcal{D}_{\mathrm{Pauli}}$ leakage.

For every pre-registered model, we compute at 80 dps:
- Second-order Bloch–Horowitz Schur-complement shift $\Delta\mathcal{E}_{\mathrm{BH}}^{(2)}(A; q_0) < 0$,
- Exact ground-state eigenvalue $E_-(A; q_0) < 0$ and hidden-channel admixture probability $P_{\mathrm{hid}}(A; q_0)$,
- Dimensionless scaling ratios $|E_-(3)| / |E_-(2)|$ and $|E_-(4)| / |E_-(2)|$ vs AME2020/CODATA-2022 ($3.8128 / 3.4694$ and $12.7196$),
- Absolute MeV readouts in the documented zero-fit CAL-1/2/3 charts $E_{\mathrm{osc}}(q_0) = m_e / (q_0 - 1)^2$ and $E_0(q_0) = m_e / (q_0(q_0 - 1))$ against CODATA-2022/AME2020 binding energies (${}^2\mathrm{H} = 2.224566\text{ MeV}$, ${}^3\mathrm{H} = 8.481797\text{ MeV}$, ${}^3\mathrm{He} = 7.717990\text{ MeV}$, ${}^4\mathrm{He} = 28.295611\text{ MeV}$).

---

## 3. Strict Precision, Anti-Fit & Gate Rules

- **Precision:** `mpmath` at `workdps = 80` (`OUT_DPS = 50` serialized), `q0Anchor = "proton"` (`qou_substrate.constants.q_at(80)`), exact rational/symbolic `sympy` verification for $6q$ CMI & Pauli antisymmetrizer identities.
- **Zero float64:** Clean on `scripts/probe-float64-guard.py --diff`, `computations/witness_raw_float64_audit.py --strict`, and `scripts/compute-qa.py`.
- **Zero fitting (`NO FITTING, EXCEPT CAL-1/2/3`):** Zero per-isotope parameters, zero fitted couplings, zero post-hoc model cherry-picking; all six models are reported honestly and completely in the stamped witness and `RESULTS.md`.
