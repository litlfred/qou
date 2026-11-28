# Untapped Algebraic Invariants on $\mathcal{O}_q(\mathrm{SU}(2))$, $U_q(\mathfrak{sl}_2)$, and $H_n(q)$ at the Proton Pin (2026-11-28)

- **Date:** 2026-11-28 · **Branch:** `claude/untapped-jm-center-gns-lepton-order-20261128` · **Beans:** `qou-u9o1` (discharged), `qou-s028`, `qou-myts`
- **Lean 4 Formalizations (`0 sorry`, `0` custom `axiom`s, `[CommRing R]` core):**
  - [`BraidKnotOctonion/HeckeJucysMurphySymmetricCenter.lean`](../../folio/quantum-observable-universe/lean/BraidKnotOctonion/HeckeJucysMurphySymmetricCenter.lean)
  - [`QOU/StandardModel/LeptonFramedGNSAndStrainOrder.lean`](../../folio/quantum-observable-universe/lean/QOU/StandardModel/LeptonFramedGNSAndStrainOrder.lean)
- **80-dps Proton-Pin Probe & Witness (`q0Anchor = "proton"`, `probe-float64-guard --strict` clean):**
  - [`computations/probes/untapped_algebraic_invariants_proton_probe.py`](../../computations/probes/untapped_algebraic_invariants_proton_probe.py)
  - [`computations/probes/untapped_algebraic_invariants_proton_probe.witness.json`](../../computations/probes/untapped_algebraic_invariants_proton_probe.witness.json)

---

## 1. Scope & Motivation

Prior `origin/main` audits established:
1. `#9777` (`3571e500084`, `2026-11-27-nucleon-split-two-scale-em.md` §9 & `NucleonSplitSingleElement.lean`): single-element nucleon traces with $K_p = q > q^{-1} = K_n$ give the wrong linear sign ($m_n < m_p$) and wrong nucleon-chart scale (`-163` / `-2029 MeV`).
2. `#10002` (`49a728bc03a`, `KoideSingletDoubletEquipartition.lean` & `2026-11-28-muon-mass-relation.md`): on the 2026-11-28 ruled least-crossing 2-component lepton link words (`e = \sigma_0\sigma_1\sigma_0`, `\mu = \sigma_0^4\sigma_1^{-1}`, `\tau = \sigma_0^2\sigma_1^{-1}\sigma_0\sigma_1^{-1}`), bare linear Convention-D / $N=2$ ring traces satisfy $\mu < \tau < e$ ($\tau_D$) or $\mu < e < \tau$ (framed $J_N$).
3. `HeckeJucysMurphyCommutation.lean` (bean `qou-u9o1`): halted at adjacent Jucys–Murphy commutativity $L_i L_{i+1} = L_{i+1} L_i$, leaving general commutativity, general $n \ge 4$ full-twist factorization $\prod_{k<n} L_k = \Delta_n^2$, and centrality of $e_k(L_0,\dots,L_{n-1}) \in Z(H_n(q))$ open.

This audit systematically evaluates **four untapped algebraic invariant families** at `mp.dps = 85` on the physical proton pin $q_0^{(p)} = 1.10997858275138080759166909561076887987449912187358\dots$ (`0` `float64`, `0` fitted parameters), proving the positive structural hits in Lean 4 over `[CommRing R]` and recording all quantitative scale misses cleanly.

---

## 2. Formalized Breakthroughs (`0 sorry`, `[CommRing R]`)

### 2.1 Complete Discharge of Bean `qou-u9o1` (`HeckeJucysMurphySymmetricCenter.lean`)

1. **Below-Commutation & Unconditional Braid-Monoid JM Commutativity (`sigma_comm_jmMon_below`, `jmMon_comm`):**
   Without using inverses or the Hecke quadratic relation, two applications of the braid relation $\sigma_k \sigma_{k+1} \sigma_k = \sigma_{k+1} \sigma_k \sigma_{k+1}$ separated by above-commutation $\sigma_{k+1} L_k = L_k \sigma_{k+1}$ prove $\sigma_k L_m = L_m \sigma_k$ for all $k + 2 \le m$, whence $L_a L_b = L_b L_a$ holds for **every** $a, b \in \mathbb{N}$ (including $b = a + 1$).
2. **General Full-Twist Factorization (`jmMon_prod_eq_fullTwist`):**
   Using the Coxeter shift identity $\sigma_{j+1} C_{k+1} = C_{k+1} \sigma_j$ ($j < k$), $(C_{m+1})^{m+1} = C_m^{m+1} (\sigma_m \cdots \sigma_0) C_{m+1} = \Delta_{m+1}^2 L_{m+1}$, proving $\prod_{k=0}^{n-1} L_k = \Delta_n^2$ for **all** $n \ge 1$.
3. **Symmetric Center over `[CommRing R]` (`sigma_comm_elemSymmJM`):**
   Combining $\sigma_i(L_i + L_{i+1}) = (L_i + L_{i+1})\sigma_i$, $\sigma_i(L_i L_{i+1}) = (L_i L_{i+1})\sigma_i$, and $\sigma_i L_j = L_j \sigma_i$ ($j \notin \{i, i+1\}$), every elementary symmetric polynomial $e_k(L_0, \dots, L_{n-1})$ commutes with every generator $\sigma_i$ ($i + 1 < n$) over any `[CommRing R]`.
4. **Balanced-Convention Eigenvalue Normalization (`jmRing_trivialHeckeModel`, `jm_eq_pow_smul_jmRaw`):**
   Under $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$, unnormalized `jmRaw` ($L_0 = 1, L_{k+1} = \sigma_k L_k \sigma_k$) already acts on $[n]$ by $q^{2k} = q^{2 c(0,k)}$ and on $[1^n]$ by $q^{-2k} = q^{2 c(k,0)}$; `jm H k = (q⁻¹)^k • jmRaw H k` shifts by an extra Dipper–James factor.

### 2.2 Wenzl $(2,1)$ Strain Minimum, Real-$q_0^{(p)}$ $e < \mu < \tau$ Ordering, & $\mathcal{O}_q(\mathrm{SU}(2))$ Spinor Dichotomy (`LeptonFramedGNSAndStrainOrder.lean`)

1. **Division-Free Wenzl $(2,1)$ Strain & Global Electron Minimum:**
   In the $[2]_q$-free basis $T_0 = \begin{pmatrix} q & 1 \\ 0 & -q^{-1} \end{pmatrix}$, $T_1 = \begin{pmatrix} -q^{-1} & 0 \\ 1 & q \end{pmatrix}$, the symmetric metric $M_q = \begin{pmatrix} q + q^{-1} & 1 \\ 1 & q + q^{-1} \end{pmatrix}$ ($\det M_q = [3]_q$) intertwines the Wenzl $C^*$-involution $\sigma_i^* = \sigma_i$ (`M_q \rho_{21}(w) = \rho_{21}(w^{\mathrm{rev}})^T M_q`). Hence $G_{(2,1)}(w) := \rho_{21}(w^{\mathrm{rev}})\rho_{21}(w)$ satisfies:
   $$\det G_{(2,1)}(w) = 1, \qquad \bigl(\mathrm{tr}\,G_{(2,1)}(w)\bigr)^2 - 4 = (q^2 + 1 + q^{-2})(y - z)^2 + (y + z)^2 \ge 0,$$
   forcing $\mathrm{tr}\,G_{(2,1)}(w) \ge 2$ for every $w \in B_3$ over any strict ordered commutative ring ($q > 0$), with **exact global minimum $\mathrm{tr}\,G_{(2,1)}(e) = 2$** ($G_{(2,1)}(e) = I_2$, $[e^*, e] = 0$, $e - e^* = 0$).
2. **Exact Muon Generic-Degree Vanishing:** $[3]_q!\,\tau_{\mathrm{GenDeg}}(\mu) = q^3 \chi^{(3)}(\mu) + (q + q^{-1})\chi^{(2,1)}(\mu) + q^{-3}\chi^{(1,1,1)}(\mu) = 0$ identically over `[CommRing R]`.
3. **Strict Real-$q$ Lepton Ordering:** On $q \in (1, 6/5]$ (which includes $q_0^{(p)} \approx 1.1100$), the zero-writhe framed Convention-D GNS norm $\|\widetilde{W}\|_D^2 = \tau_D(\widetilde{W}^* \widetilde{W})$ ($\widetilde{W} = q^{-\mathrm{wr}(W)} W$) satisfies **strict $\|\widetilde{e}\|_D^2 < \|\widetilde{\mu}\|_D^2 < \|\widetilde{\tau}\|_D^2$**, and on $q \in [11/10, 6/5]$, $\tau_D(\Delta_3^2 e) > \tau_D(\Delta_3^2 \mu) > \tau_D(\Delta_3^2 \tau)$ (note the exact polynomial crossover root $q_* \approx 1.0795$ below which $\mu$ and $\tau$ swap in $\tau_D(\Delta_3^2 W)$!).
4. **$\mathcal{O}_q(\mathrm{SU}(2))$ Ordered 3-Quark Spinor GNS Dichotomy:** For unit quantum 2-sphere spinor coordinates $(u, d) = (\alpha, \gamma)$ ($W_p = \alpha^2\gamma$, $W_n = \alpha\gamma^2$), $h(W_p W_p^*) = h(W_n W_n^*) = \frac{q^4}{[3]_{q^2}[4]_{q^2}}$ is strictly isospin-symmetric, whereas $h(W_p^* W_p) = q^2 h(W_n^* W_n) = \frac{q^8}{[3]_{q^2}[4]_{q^2}}$ carries Woronowicz's exact KMS factor $q^2$; on $j=1/2$ Peter–Weyl coefficients, $\|t^{1/2}_{\cdot,-1/2}\|_R^2 - \|t^{1/2}_{\cdot,+1/2}\|_R^2 = +\frac{q - q^{-1}}{[2]_q} > 0$ ($m_n > m_p$ linearly).

---

## 3. Summary 80-dps Proton-Pin Tables (`q0 = 1.10997858275138080759...`)

### 3.1 Family 1 — $\mathcal{O}_q(\mathrm{SU}(2))$ Haar & Peter–Weyl Norms
- $h(\alpha\delta) = 0.448018144973794927$, $h(\delta\alpha) = 0.551981855026205073$, $h(\beta\gamma) = -0.497290545604915556$, $h(\alpha\delta - \delta\alpha) = -0.103963710052410146 = -\tanh(\ln q_0)$.
- 3-quark spinor monomials: $h(W_p^* W_p) = 0.109328352931813445$, $h(W_n^* W_n) = 0.088736768115731014$ (ratio $q_0^2 = 1.23205245416676393$), $h(W_p W_p^*) = h(W_n W_n^*) = 0.072023530991416772$.
- Candidate linear $\Delta m_{np}$ splits vs `1.29333251 MeV`: $\tanh(\ln q_0) m_e = 0.053125\text{ MeV}$, $\tanh(\ln q_0)|c_{\mathrm{cat}}| = 0.143825\text{ MeV}$, $\tanh(\ln q_0) E_0 = 0.435190\text{ MeV}$, $[2]_{q_0}(q_0 - q_0^{-1}) E_0 = 1.759781\text{ MeV}$ (all right sign $m_n > m_p$; none adopted without derived scale).

### 3.2 Family 2 — Jucys–Murphy Symmetric Center ($H_3, H_6, H_9, H_{12}$)
- Chiral content skewness $p_3(C)$ ($C_m = \frac{J_m - J_m^{-1}}{q^2 - q^{-2}}$) vanishes identically on self-conjugate $\lambda = (2,1) \vdash 3$ and $\lambda = [3,3,3] \vdash 9$ (${}^3\mathrm{H}/{}^3\mathrm{He}$ colour-singlet sector!), while equal and opposite ($\pm 9.5360193874$) on $(3)$ vs $(1,1,1)$.
- ${}^3\mathrm{H}$ vs ${}^3\mathrm{He}$ ($H_9$): $\chi^{[3,3,3]}({}^3\mathrm{H}) = -1.1606791182$ vs $\chi^{[3,3,3]}({}^3\mathrm{He}) = -0.5598787202$; $\ell = 3$ Plancherel $p_3(C)$ shifts `-0.128081` $\to$ `-0.212833`.

### 3.3 Family 3 — Real-$q_0^{(p)}$ Lepton Invariants (`e`, `\mu`, `\tau`)

| Invariant | $e$ | $\mu$ | $\tau$ | $\mu/e$ | $\tau/e$ | $Q_{\mathrm{Koide}}$ | Order |
|---|---:|---:|---:|---:|---:|---:|---|
| $p_1 = \tau_D(W)$ | `0.69116648` | `0.52692874` | `0.61956565` | `0.762376` | `0.896406` | `0.334354` | $\mu < \tau < e$ |
| $\mathrm{Var}_D^*(W) = \det G_2(W)$ | `0.96209066` | `1.40862816` | `0.78313036` | `1.464132` | `0.813988` | `0.338441` | $\tau < e < \mu$ |
| $\mathrm{tr}\,G_{(2,1)}(W)$ | `2.00000000` | `2.99669387` | `2.20101939` | `1.498347` | `1.100510` | `0.335923` | $e < \tau < \mu$ |
| **$\|\widetilde{W}\|_D^2$ (framed GNS)** | **`0.76986594`** | **`0.90165962`** | **`0.94719341`** | **`1.171190`** | **`1.230336`** | **`0.333969`** | **STRICT $e < \mu < \tau$** |
| **$1/\tau_D(e_3(J) W)$** | **`0.77362365`** | **`0.88622593`** | **`0.90274202`** | **`1.145552`** | **`1.166901`** | **`0.333719`** | **STRICT $e < \mu < \tau$** |
| **$1/\tau_D(\psi^3 W)$ ($H_9$)** | **`0.98948188`** | **`1.95206999`** | **`2.64123909`** | **`1.972820`** | **`2.669315`** | **`0.345963`** | **STRICT $e < \mu < \tau$** |

### 3.4 Family 4 — Quantum $6j$-Symbols & Doubled-$K_4$ Turaev–Viro Sums
- $\{1/2,1/2,1;1/2,1/2,0\}_{q_0} = \frac{1}{[2]_{q_0}} = 0.497290545604915556 = -h(\beta\gamma)$; $\{1,1,1;1/2,1/2,1/2\}_{q_0} = -\frac{\sqrt{[4]_{q_0}}}{[2]_{q_0}[3]_{q_0}} = -0.331216225165781586$; $\{1,1,1;1,1,1\}_{q_0} = 0.167786522263675397$.
- At real $q_0 > 1$, $[2j+1]_{q_0} \to +\infty$ causes untruncated Turaev–Viro state sums to diverge and hard cutoffs $J_{\max} \in \{1/2, 1, 3/2\}$ to break 2–3 Pachner invariance (`W/D^6 = 0.228405 -> 0.211678 -> 0.170731`), confirming that bare $\{6j\}_{q_0}$ spin recoupling does not supply the ${}^4\mathrm{He}$ $K_4$ 2-body shortfall (`13.9690 MeV`).

---

## 4. Honest Negative Exclusions

1. **Quantitative Lepton Hierarchy:** Finite-rank real-$q_0^{(p)}$ algebraic trace/norm/satellite invariants on $(e, \mu, \tau)$ yield $O(1\text{–}8)$ ratios and $Q \in [0.3337, 0.4617]$, never `206.768` / `3477.23` / `2/3` without the $\hbar_{q_0}^{-2}$ Compton pole (`CAL-2`) or asymptotic $N \to \infty$ volume scaling.
2. **$\Delta m_{np}$ Scale:** Right-GNS Peter–Weyl norms resolve the linear sign ($m_n > m_p$), and left-GNS spinor monomials reproduce $q_0^2$, but fixing the MeV magnitude requires deriving the mass-chart electron scale $E$.
3. **Real-$q_0$ Turaev–Viro:** Non-truncation at real $q_0 > 1$ breaks state-sum finiteness and Pachner invariance.
