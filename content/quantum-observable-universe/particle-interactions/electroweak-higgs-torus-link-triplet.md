**Conjecture (electroweak/Higgs torus-link identification).**
*In any QOU built on ([Bring's surface](#def:brings-surface)) with EM/strong sector $\{T_{2,9}, T_{3,5}\}$ ([force-carrier Bring uniqueness](#prop:force-carrier-bring-uniqueness)), the standard-model electroweak gauge bosons $W^\pm, Z$ and the Higgs scalar $H$ correspond to the three even-twist $2$-component torus links of the sub-saturating complement:*

$$
  W^{\pm} \;\longleftrightarrow\; T(2,4),
  \qquad
  Z \;\longleftrightarrow\; T(2,6),
  \qquad
  H \;\longleftrightarrow\; T(2,8).
$$

This is the **top node** of the electroweak conjecture lattice. Its provable base — that these three links exist, have Seifert genera $1, 2, 3$, co-embed in Bring's genus-$4$ fiber alongside the saturating carriers, and fit minimally in $B_6$ at the far-commuting triple $(1,3,5)$ — is discharged to the sorry-free ([prop:electroweak-triplet-bring-embedding](#prop:electroweak-triplet-bring-embedding)) and ([thm:ew-triplet-far-commuting-minimal](#thm:ew-triplet-far-commuting-minimal)). What remains conjectural is the *identification itself*. As of 2026-07-05, charge and spin are proved consequences of a single sector postulate.

**The conjecture lattice (narrowed).**

| Node | Kind | Rests on | Content |
|------|------|----------|---------|
| **C1** selection | primary | — | EW carriers *are* the nontrivial, strictly sub-saturating even-twist links ($0 < g < 4$). |
| **C2** enumeration | dependent (C1) | C1 | These carriers are exactly $\{T(2,4), T(2,6), T(2,8)\}$. |
| **C$_{\text{sector}}$** sector assignment | primary | — | Which link sits in the singlet $A_+$ versus doublet $A_-$ of the spin involution. |
| **C$_{\text{top}}$** identification | dependent (C1, C$_{\text{sector}}$) | C1, C$_{\text{sector}}$ | The full map above. |

The former **C3 (charge)** and **C4 (spin)** are proved consequences of C$_{\text{sector}}$ via ([thm:ew-triplet-charge-spin-from-involution](#thm:ew-triplet-charge-spin-from-involution)).

**C1 — the selection principle (strong corpus grounding).**

The electroweak carriers are the *nontrivial, strictly sub-saturating* even-twist $2$-component torus links. Their Seifert genus $g$ lies in the window $0 < g < 4 = g(\Sigma_4)$. This forms the sub-saturating complement of the genus-$4$ **saturating** force-carrier knots $\{T_{2,9}, T_{3,5}\}$. These two are the only coprime solutions of $(p-1)(q-1) = 8$, exhausting Bring's genus-$4$ capacity. The Hopf link $T(2,2)$ (genus $0$) is the trivial endpoint and is excluded. C1 ties to the $S_5$ action on the Hecke slice ([conj:n-v-bring-action](#conj:n-v-bring-action)). The saturation mechanism that forces $\{T_{2,9}, T_{3,5}\}$ for the strong carriers selects the sub-saturating window for the weak carriers.

**C2 — enumeration (dependent on C1).**

Given C1, the carrier window $0 < g < 4$ contains exactly the genera $1, 2, 3$ ($k \in \{2, 3, 4\}$): the triplet $T(2,4), T(2,6), T(2,8)$. The forward inclusion is the *provable* enumeration `ew_enumeration` of ([prop:electroweak-triplet-bring-embedding](#prop:electroweak-triplet-bring-embedding)). The conjectural content of C2 is the reverse inclusion: all three genera are realised as carriers.

**C$_{\text{sector}}$ — the single sector-assignment postulate.**

Charge and spin are unified by one $\mathbb{Z}/2$ datum: the assignment of each carrier to a sector of the spin involution $\sigma$ of ([def:spin-involution](#def:spin-involution)), $A = A_+ \oplus A_-$. Restricted to the sym/alt Hecke block, $\sigma$ is the swap of the eigenvalues $q^{2k} \leftrightarrow q^{-2k}$ (the bar involution $q \mapsto q^{-1}$). Its projections give a bar-even part in $A_+$ (neutral, retained by the Markov trace) and a bar-odd part in $A_-$ (charged, traceless), per ([prop:vdw-pskew-isolation](#prop:vdw-pskew-isolation)). The Higgs is the bar-even self-dual carrier ([prop:self-dual-higgs-real-volume](#prop:self-dual-higgs-real-volume)).

**Charge and spin are proved consequences.** Given the sector assignment ($H$ singlet, $W^\pm, Z$ doublets), ([thm:ew-triplet-charge-spin-from-involution](#thm:ew-triplet-charge-spin-from-involution)) derives: $H \in A_+$ implies scalar (spin $0$) and neutral; $W^\pm \in A_-$ implies vector (spin $1$) with $T_3 = \pm 1$; $Z \in A_-$ implies vector, neutral with $T_3 = 0$ via the $(W^3, B) \mapsto (Z, \gamma)$ Weinberg mixing ([conj:weinberg-angle-categorical](#conj:weinberg-angle-categorical)). The remaining conjectural input is the sector assignment itself.

**The $\sigma_5^8$ bar-grading is derived from spin.**

The Weinberg-angle block ([conj:weinberg-angle-categorical](#conj:weinberg-angle-categorical)) reads the Hoefsmit slot $\sigma_5^8$ as the $\mathrm{U}(1)_Y$ hypercharge gauge boson $B$ (pre-mixing). This block reads $\sigma_5^8$ ($= T(2,8)$, strands $5$–$6$) as the Higgs. There is no conflict: $\sigma_5^8$ **carries both, bar-graded** by the spin involution ([def:spin-involution](#def:spin-involution)). The Higgs boson $H$ is the $A_+$ (bar-even, scalar) part. The hypercharge gauge boson $B$ is the $A_-$ (bar-odd, vector) part.

This bar-grading is derived from the two carriers' spins (`ew_sigma5_bargrade_forced` in ([thm:ew-triplet-charge-spin-from-involution](#thm:ew-triplet-charge-spin-from-involution))). The sector$\to$spin map is injective and inverts. Spin determines the sector. The Higgs is a scalar and $B$ a vector as independent physical inputs, so $H \in A_+$ and $B \in A_-$ are forced. The residual postulate is that both $H$ and $B$ inhabit the one $\sigma_5^8$ slot. The self-dual figure-eight $4_1$ of ([prop:self-dual-higgs-real-volume](#prop:self-dual-higgs-real-volume)) is the Higgs *mass mechanism* ($m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$), not the $125\,$GeV Higgs boson. The boson is the electroweak-slot link $T(2,8) = A_+$ of $\sigma_5^8$.

**The $W$ vs $Z$ slot assignment is a free label.**

Spin fixes each carrier's sector (scalar $H \to A_+$; vectors $W, Z \to A_-$). It does not fix which of the two $A_-$ vector slots is the charged $W^\pm$ and which is the neutral $Z$. The corpus map ([def:coulomb-charge](#def:coulomb-charge)), $Q = \tfrac12(n_+ - n_-) = \tfrac12\,\mathrm{writhe}$, on the all-positive braid $\sigma_1^{2k}$ gives $Q(T(2,2k)) = k > 0$ for all three carriers. It cannot single out the neutral slot. The $\mathrm{writhe} \to Y$ map is falsified. Only $\mathrm{writhe} \to I_3$ survives. The assignment $W = \sigma_1^4$ relies on the mass ordering $4 < 6 < 8$. It is carried as the explicit free-label field `t3Label` of $C_{\text{sector}}$. Its underdetermination is proved sorry-free (`which_slot_is_W_free`). Both $W = \sigma_1^4$ and the mirror $W = \sigma_3^6$ satisfy every proved constraint.

**Supporting evidence.**

The identification aligns with the following observations:

1. **Mass ordering.** The standard-model ordering $m_{W^\pm} < m_Z < m_H$ ($80.4 < 91.2 < 125.3$ GeV) maps monotonically onto the crossing-number ordering $4 < 6 < 8$.
2. **PSD-feasibility probe.** An exploratory SDP-feasibility probe ([`ew-higgs-sdp-probe.witness.json`](https://github.com/litlfred/qou/blob/main/computations/probes/ew-higgs-sdp-probe.witness.json)) shows PSD discrimination. Only the even-twist torus-link triplet $\{T(2,4), T(2,6), T(2,8)\}$ produced positive-semidefinite Hecke certificates on every Wedderburn block. 

PSD-feasibility is necessary but not sufficient. It holds for every even-twist $T(2, 2k)$ at any $k \geq 1$. The probe cannot select the specific triplet from the infinite family.

See [Table 1](#tbl:electroweak-higgs-torus-link-triplet-table1-data) for the $1/\alpha_{EM}$-parallel pipeline ([`rem:alpha-em-categorical-trace`](#rem:alpha-em-categorical-trace)), [Table 2](#tbl:electroweak-higgs-torus-link-triplet-table2-data) for the sub-argument factorisation, and [Table 3](#tbl:electroweak-higgs-torus-link-triplet-table3-data) for the probe over $T(2, 2k)$, $k = 1 \ldots 7$.

**What the conjecture closes.**

If true, the identification supplies the categorical structure for the weak-scale crossing count $N_v$ in the Fermi-constant decomposition $G_F = 1/(\sqrt{2}\,v^2)$, $v = N_v\,E_\times\,\mu_0$ (the **NV-1** audit flag ([NV-1 / FROB-FILTER conjectures, 2026-05-02](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-02-nv-frob-filter-conjectures.md))). The residual to close is C1 (selection) and C$_{\text{sector}}$ (sector assignment). Enumeration and far-commuting minimality are discharged to ([prop:electroweak-triplet-bring-embedding](#prop:electroweak-triplet-bring-embedding)) and ([thm:ew-triplet-far-commuting-minimal](#thm:ew-triplet-far-commuting-minimal)). Charge and spin are discharged to ([thm:ew-triplet-charge-spin-from-involution](#thm:ew-triplet-charge-spin-from-involution)).
