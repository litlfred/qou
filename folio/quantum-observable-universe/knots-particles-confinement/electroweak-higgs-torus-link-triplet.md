**Conjecture (electroweak/Higgs torus-link identification).**
*In any QOU built on Bring's surface with EM/strong sector $\{T_{2,9}, T_{3,5}\}$, the standard-model electroweak gauge bosons $W^\pm, Z$ and the Higgs scalar $H$ correspond to the three even-twist $2$-component torus links of the sub-saturating complement:*

$$
  W^{\pm} \;\longleftrightarrow\; T(2,4),
  \qquad
  Z \;\longleftrightarrow\; T(2,6),
  \qquad
  H \;\longleftrightarrow\; T(2,8).
$$

This is the top of the electroweak chain of conjectures. Its provable base — that these three links exist, have Seifert genera $1, 2, 3$, co-embed in Bring's genus-$4$ fiber alongside the saturating carriers, and fit minimally in $B_6$ at the far-commuting triple $(1,3,5)$ — is proved. What remains conjectural is the identification itself. Charge and spin are proved consequences of a single sector postulate.

**The chain of conjectures.**

| Node | Kind | Rests on | Content |
|------|------|----------|---------|
| **C1** selection | primary | — | EW carriers are the nontrivial, strictly sub-saturating even-twist links ($0 < g < 4$). |
| **C2** enumeration | dependent (C1) | C1 | These carriers are exactly $\{T(2,4), T(2,6), T(2,8)\}$. |
| **C$_{\text{sector}}$** sector assignment | primary | — | Which link sits in the singlet $A_+$ versus doublet $A_-$ of the spin involution. |
| **C$_{\text{top}}$** identification | dependent (C1, C$_{\text{sector}}$) | C1, C$_{\text{sector}}$ | The full map above. |

Charge and spin are proved consequences of C$_{\text{sector}}$ rather than
independent postulates.

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

Spin fixes each carrier's sector (scalar $H \to A_+$; vectors $W, Z \to A_-$). It does not fix which of the two $A_-$ vector slots is the charged $W^\pm$ and which is the neutral $Z$. The crossing-to-charge map $Q = \tfrac12\,\mathrm{writhe}$ on the all-positive braid $\sigma_1^{2k}$ gives $Q(T(2,2k)) = k > 0$ for all three carriers. It cannot single out the neutral slot. The assignment $W = \sigma_1^4$ relies on the mass ordering $4 < 6 < 8$. Both $W = \sigma_1^4$ and the mirror $W = \sigma_3^6$ satisfy every proved constraint.

**Supporting evidence.**

1. **Mass ordering.** The standard-model ordering $m_{W^\pm} < m_Z < m_H$ maps monotonically onto the crossing-number ordering $4 < 6 < 8$.
2. **PSD-feasibility probe.** An exploratory SDP-feasibility probe shows PSD discrimination. Among the candidates tested, only the even-twist torus links, here the triplet $\{T(2,4), T(2,6), T(2,8)\}$, produced positive-semidefinite Hecke certificates on every Wedderburn block. 

PSD-feasibility is necessary but not sufficient. It holds for every even-twist $T(2, 2k)$ at any $k \geq 1$.

**Scope of the closure.**

If true, the identification supplies the categorical structure for the weak scale in proton units, $N_v = v / m_p$ (the crossing count is $3v/m_e$), in the Fermi-constant decomposition $G_F = 1/(\sqrt{2}\,v^2)$. The following hold, with the numerical values verified at 50 dps:

1. **Electroweak Bring Seifert–Hodge Zero-Mode ($1/\pi$) and 1-Loop Schwinger Fixed Point ($-29.37\;\mathrm{ppb}$ on $v$):**
   The Seifert genera of $\{W^\pm = T(2,4),\, Z^0 = T(2,6),\, H = T(2,8)\}$ are $(g_W, g_Z, g_H) = (1, 2, 3)$, whose sum $G_{\mathrm{EW}} = 1 + 2 + 3 = 6$ equals the absolute Euler characteristic $-\chi(\Sigma_4) = 2g - 2 = 6$ of Bring's genus-$4$ surface. Dividing the total Seifert first-Betti count $2(g_W + g_Z + g_H) = 12$ by the Bring Gauss–Bonnet area $\mathrm{Area}(\Sigma_4) = 4\pi(g - 1) = 12\pi$ yields the zero-mode shift (no parameter is fitted, but counting Seifert genera rather than the surface genus, as the electromagnetic sector does, is a choice; see the scope note below)
   $$
     T_{\mathrm{zero}}^{\mathrm{EW}} \;=\; \frac{2(g_W + g_Z + g_H)}{4\pi(g - 1)}\Bigg|_{g=4} \;=\; \frac{12}{12\pi} \;=\; \frac{1}{\pi} \;=\; \frac{3}{2}\cdot\frac{2}{3\pi}
   $$
   Combining the $2$-strand quantum-dimension-dressed tree complexity $N_v^{\mathrm{tree}}(q) = q\,\tfrac{[2]_q}{2}\,[4]_q\,[6]_q\,[8]_q$ with $1/\pi$ and the 1-loop Schwinger/Habiro self-consistency term ($H = [2]_q/(8\pi)$, $\hbar_q = 1 - q^{-1}$; the fixed-point relation is equivalent to a cubic in $\alpha_v$),
   $$
     N_v \;=\; \frac{1}{\alpha_v} \;=\; \underbrace{q\,\frac{[2]_q}{2}\,[4]_q\,[6]_q\,[8]_q + \frac{1}{\pi}}_{T_{\mathrm{EW}}(q)} \;-\; \alpha_v\,H\,\bigl(1 - \hbar_q^2\,\alpha_v\bigr),
   $$
   gives at the proton-pinned $q_0$ (conditional on the hypothesis that $\alpha_v = m_p/v$ is a positive root of this fixed-point relation; no continuous parameter is fitted, but four discrete choices are not derived, see the scope note below):
   - $N_v^{\mathrm{pred}} = 262.418168819\ldots$ vs. $v_{\mathrm{exp}}/m_p = 262.418176527\ldots$ ($-29.37\;\mathrm{ppb} = -0.114\,\sigma_{G_F}$),
   - $v^{\mathrm{pred}} = N_v^{\mathrm{pred}}\,m_p = 246.21964356\;\mathrm{GeV}$ vs. $246.21965079(63)\;\mathrm{GeV}$ ($-29.37\;\mathrm{ppb} = -0.114\,\sigma_{G_F}$),
   - $G_F^{\mathrm{pred}} = 1/(\sqrt{2}\,(v^{\mathrm{pred}})^2) = 1.1663787685\times 10^{-5}\;\mathrm{GeV}^{-2}$ vs. CODATA 2022 $1.1663787(6)\times 10^{-5}\;\mathrm{GeV}^{-2}$ ($+58.74\;\mathrm{ppb} = +0.114\,\sigma_{G_F}$).
   - *Scope.* The agreement rests on four choices that no proved result fixes: the tree prefactor $q\,[2]_q/2$, the counting rule that gives the zero mode $1/\pi$ (the electromagnetic sector uses a different rule, and no single rule gives both), the loop sign, and the identification of the loop coupling with $\alpha_v = m_p/v$, which is not an electroweak gauge coupling. Changing any one of them alone moves $N_v$ by between $4.4\,\sigma_{G_F}$ and $4\times 10^{4}\,\sigma_{G_F}$; with the electromagnetic loop sign the miss is $+2294\;\mathrm{ppb}$. The proved skein contraction gives $h^2$ in place of $\hbar_q^2$ in the loop term, which moves the result by $0.15\;\mathrm{ppb}$. So the $-29.37\;\mathrm{ppb}$ is the miss of one selected formula, not of a derivation.
2. **2-Strand Plancherel Trace Polynomials $P_m(h)$ and $W/Z$-Anchor Reconciliation for $m_H$:**
   The binomial trace polynomials $P_m(h) = \sum_{j=0}^m \tfrac{1}{2}\binom{m+j}{2j}h^{2j}$ ($h = q - q^{-1}$) satisfy the exact Laurent identity $(q + q^{-1})\cdot 2P_m(q - q^{-1}) = q^{2m+1} + q^{-(2m+1)}$. Including the $2$-strand quantum-dimension dressing $([2]_q/2)^2 = 1 + h^2/4$ across the $W \to Z$ genus step gives $m_Z / m_W = (P_3(h_0)/P_2(h_0))\cdot([2]_{q_0}/2)^2 = 1.1348070$ vs. PDG $1.1346088$ ($+174.7\;\mathrm{ppm} = +1.06\,\sigma_W$, or $m_W^{\mathrm{pred}} = 80.3552\;\mathrm{GeV}$ from $m_Z$) and brings the $W$-anchored and $Z$-anchored Higgs mass formulas together, collapsing their previously reported $1.34\;\mathrm{GeV}$ discrepancy down to $21.9\;\mathrm{MeV}$ ($174.7\;\mathrm{ppm}$). Two choices enter this ratio and neither is derived: the dressing exponent is $2$ here, while $N_v$ uses $1$, and the step is taken as $P_3/P_2$. The residual to close is C1 (selection), C$_{\text{sector}}$ (sector assignment), and the first-principles derivation of that fixed-point hypothesis.
