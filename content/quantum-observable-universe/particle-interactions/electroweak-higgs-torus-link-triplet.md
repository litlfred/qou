**Conjecture (electroweak/Higgs torus-link identification).**
*In any QOU built on Bring's surface with EM/strong sector $\{T_{2,9}, T_{3,5}\}$, the standard-model electroweak gauge bosons $W^\pm, Z$ and the Higgs scalar $H$ correspond to the three even-twist $2$-component torus links of the sub-saturating complement:*

$$
  W^{\pm} \;\longleftrightarrow\; T(2,4),
  \qquad
  Z \;\longleftrightarrow\; T(2,6),
  \qquad
  H \;\longleftrightarrow\; T(2,8).
$$

This is the top node of the electroweak conjecture lattice. Its provable base — that these three links exist, have Seifert genera $1, 2, 3$, co-embed in Bring's genus-$4$ fiber alongside the saturating carriers, and fit minimally in $B_6$ at the far-commuting triple $(1,3,5)$ — is proved. What remains conjectural is the identification itself. Charge and spin are proved consequences of a single sector postulate.

**The conjecture lattice (narrowed).**

| Node | Kind | Rests on | Content |
|------|------|----------|---------|
| **C1** selection | primary | — | EW carriers are the nontrivial, strictly sub-saturating even-twist links ($0 < g < 4$). |
| **C2** enumeration | dependent (C1) | C1 | These carriers are exactly $\{T(2,4), T(2,6), T(2,8)\}$. |
| **C$_{\text{sector}}$** sector assignment | primary | — | Which link sits in the singlet $A_+$ versus doublet $A_-$ of the spin involution. |
| **C$_{\text{top}}$** identification | dependent (C1, C$_{\text{sector}}$) | C1, C$_{\text{sector}}$ | The full map above. |

The former C3 (charge) and C4 (spin) are proved consequences of C$_{\text{sector}}$.

**C1 — the selection principle.**

The electroweak carriers are the nontrivial, strictly sub-saturating even-twist $2$-component torus links. Their Seifert genus $g$ lies in the window $0 < g < 4 = g(\Sigma_4)$. This forms the sub-saturating complement of the genus-$4$ saturating force-carrier knots $\{T_{2,9}, T_{3,5}\}$. These two are the only coprime solutions of $(p-1)(q-1) = 8$, exhausting Bring's genus-$4$ capacity. The Hopf link $T(2,2)$ (genus $0$) is the trivial endpoint and is excluded. The saturation mechanism that forces $\{T_{2,9}, T_{3,5}\}$ for the strong carriers selects the sub-saturating window for the weak carriers.

**C2 — enumeration.**

Given C1, the carrier window $0 < g < 4$ contains exactly the genera $1, 2, 3$ ($k \in \{2, 3, 4\}$): the triplet $T(2,4), T(2,6), T(2,8)$. The forward inclusion is a provable enumeration. The conjectural content of C2 is the reverse inclusion: all three genera are realised as carriers.

**C$_{\text{sector}}$ — the single sector-assignment postulate.**

Charge and spin are unified by one $\mathbb{Z}/2$ datum: the assignment of each carrier to a sector of the spin involution $\sigma$, $A = A_+ \oplus A_-$. Restricted to the sym/alt Hecke block, $\sigma$ is the swap of the eigenvalues $q^{2k} \leftrightarrow q^{-2k}$. Its projections give a bar-even part in $A_+$ (neutral, retained by the Markov trace) and a bar-odd part in $A_-$ (charged, traceless). The Higgs is the bar-even self-dual carrier.

Given the sector assignment ($H$ singlet, $W^\pm, Z$ doublets), spin and charge follow. $H \in A_+$ implies scalar (spin $0$) and neutral. $W^\pm \in A_-$ implies vector (spin $1$) with $T_3 = \pm 1$. $Z \in A_-$ implies vector, neutral with $T_3 = 0$ via the $(W^3, B) \mapsto (Z, \gamma)$ Weinberg mixing. The remaining conjectural input is the sector assignment itself.

**The $\sigma_5^8$ bar-grading is derived from spin.**

The Weinberg-angle block reads the Hoefsmit slot $\sigma_5^8$ as the $\mathrm{U}(1)_Y$ hypercharge gauge boson $B$. This block reads $\sigma_5^8$ ($= T(2,8)$, strands $5$–$6$) as the Higgs. There is no conflict: $\sigma_5^8$ carries both, bar-graded by the spin involution. The Higgs boson $H$ is the $A_+$ (bar-even, scalar) part. The hypercharge gauge boson $B$ is the $A_-$ (bar-odd, vector) part.

This bar-grading is derived from the two carriers' spins. The sector$\to$spin map is injective and inverts. Spin determines the sector. The Higgs is a scalar and $B$ a vector as independent physical inputs, so $H \in A_+$ and $B \in A_-$ are forced. The residual postulate is that both $H$ and $B$ inhabit the one $\sigma_5^8$ slot. The self-dual figure-eight $4_1$ is the Higgs mass mechanism, not the $125\,$GeV Higgs boson. The boson is the electroweak-slot link $T(2,8) = A_+$ of $\sigma_5^8$.

**The $W$ vs $Z$ slot assignment is a free label.**

Spin fixes each carrier's sector (scalar $H \to A_+$; vectors $W, Z \to A_-$). It does not fix which of the two $A_-$ vector slots is the charged $W^\pm$ and which is the neutral $Z$. The corpus map $Q = \tfrac12\,\mathrm{writhe}$ on the all-positive braid $\sigma_1^{2k}$ gives $Q(T(2,2k)) = k > 0$ for all three carriers. It cannot single out the neutral slot. The assignment $W = \sigma_1^4$ relies on the mass ordering $4 < 6 < 8$. Both $W = \sigma_1^4$ and the mirror $W = \sigma_3^6$ satisfy every proved constraint.

**Supporting evidence.**

1. **Mass ordering.** The standard-model ordering $m_{W^\pm} < m_Z < m_H$ maps monotonically onto the crossing-number ordering $4 < 6 < 8$.
2. **PSD-feasibility probe.** An exploratory SDP-feasibility probe shows PSD discrimination. Only the even-twist torus-link triplet $\{T(2,4), T(2,6), T(2,8)\}$ produced positive-semidefinite Hecke certificates on every Wedderburn block. 

PSD-feasibility is necessary but not sufficient. It holds for every even-twist $T(2, 2k)$ at any $k \geq 1$.

**Scope of the closure.**

If true, the identification supplies the categorical structure for the weak-scale crossing count $N_v$ in the Fermi-constant decomposition $G_F = 1/(\sqrt{2}\,v^2)$, $v = N_v\,E_\times\,\mu_0$. The residual to close is C1 (selection) and C$_{\text{sector}}$ (sector assignment).
