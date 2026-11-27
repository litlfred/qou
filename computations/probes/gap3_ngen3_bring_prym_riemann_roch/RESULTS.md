# Results: Closing Open Gap 3 (Option 3A Primary) — Why $N_{\mathrm{gen}} = 3$ Fermion Generations via Riemann–Roch + Chevalley–Weil Zero-Mode Count on Bring's Curve Twisted by the $\mathbb{Z}_3$ Colour Kummer Line Bundle

- **Branch**: `claude/gap3-ngen3-bring-prym-riemann-roch-20261123`
- **Pre-registration**: `computations/probes/gap3_ngen3_bring_prym_riemann_roch/PREREGISTRATION.md` (`92cfc2cd42c`)
- **Lean 4 formalization**: `folio/quantum-observable-universe/lean/QOU/StandardModel/BringPrymRiemannRochGenerations.lean` (`315b794d12f` — 1,194 lines, `0 sorry`, `0` custom `axiom`s, `[propext, Classical.choice, Quot.sound]` only, §7c generic ring/field)
- **Exact + 80-dps verification probe**: `computations/probes/gap3_ngen3_bring_prym_riemann_roch/gap3_ngen3_bring_prym_riemann_roch_probe.py` (`5fce852e66b`)
- **80-dps witness**: `computations/probes/gap3_ngen3_bring_prym_riemann_roch/gap3-ngen3-bring-prym-riemann-roch.witness.json` (`a87869d4d45`, `11/11` assertions passed, `q0Anchor = "proton"`, `scriptCommitSha = 5fce852e66b`)

---

## 1. Executive Summary & Epistemic Ledger

| Claim / Structural Step | Verdict | Lean 4 Theorem / Witness Check |
|---|---|---|
| Effective degree-$0$ divisor vanishing ($D \ge 0, \sum_P D(P) = 0 \implies D = 0$) | **PROVED UNCONDITIONALLY** | `effective_deg_zero_divisor_eq_zero` |
| Every non-trivial $3$-torsion class $\mathcal{L} \in \mathrm{Pic}^0(\mathcal{B})[3] \setminus \{0\}$ on genus $g = 4$ gives $(h^0, h^1) = (3, 0)$ on $K_{\mathcal{B}} \otimes \mathcal{L}$ and $K_{\mathcal{B}} \otimes \mathcal{L}^2$, and $(4, 1)$ on $K_{\mathcal{B}}$ | **PROVED UNCONDITIONALLY** | `bring_z3_prym_chevalley_weil_ten_split`, `bringGenus4PicModel_evaluates_to_4_3_3` |
| Étale $\mathbb{Z}_3$ Kummer–Prym cover $\tilde{\mathcal{B}} \to \mathcal{B}$ has $\tilde{g} = 10 = 4 + 3 + 3$, $\dim_{\mathbb{C}} \mathrm{Prym}(\tilde{\mathcal{B}}/\mathcal{B}) = 6$, and uniform Dolbeault index $h^0 - h^1 = 3$ across all $t \in \{0, 1, 2\}$ | **PROVED UNCONDITIONALLY** | `unramified_z3_over_bring_genus_ten`, `bring_z3_prym_chevalley_weil_ten_split` |
| Untwisted spin structure $S = K_{\mathcal{B}}^{1/2}$ ($2S = K_{\mathcal{B}}, \deg S = 3$) has chiral index $h^0(S + \mathcal{L}) - h^1(S + \mathcal{L}) = 0$ (canonical/Spin$^c$ twist $K_{\mathcal{B}}$ is necessary) | **PROVED UNCONDITIONALLY (Honest Contrast)** | `untwisted_spin_structure_zero_index` |
| Descending cyclic $\mathbb{Z}_3$-covers $\Sigma_4 \to \mathcal{B}_0$ ($\chi_{\mathrm{eu}} = -6$) satisfy $3g_0 + r = 6 \implies (g_0, r) \in \{(2,0), (1,3), (0,6)\}$ and **never** yield $(d_1, d_2) = (3, 3)$ | **PROVED UNCONDITIONALLY (No-Go on Case II)** | `descending_z3_from_genus4_solutions`, `descending_z3_cannot_give_three_three` |
| Central $Z(\mathrm{SU}(3)_c) \cong \mu_3$ Kummer holonomy ($\mathcal{W}_3 = \mathbb{C}^3 \otimes \mathcal{L}$, $\det \mathcal{W}_3 \cong \mathcal{O}_{\mathcal{B}}$) preserves unbroken $\mathrm{SU}(3)_c$ and assigns triality $t = 1$ to $Q_L$, $t = 2$ to $u_R^c, d_R^c$, and $t = 0$ to $L_L, e_R^c$ | **PROVED UNCONDITIONALLY** | `exterior_multiplet_triality_and_dim` |
| $|C_{S_5}(C_3)| = 6$, $N_{S_5}(C_3) = S_3 \times S_2$ (`order = 12`), $D^{(4,1)} = V_{\mathrm{std}}(\mathbb{F}_3)$ is $\mathbb{F}_3[S_5]$-simple, $\mathrm{Ext}^1_{\mathbb{F}_3[S_5]}(D^{(4,1)}, D^{(4,1)}) = 0$, and $M^{C_5} = M^{A_5} = M^{S_5} = \{0\}$ | **PROVED UNCONDITIONALLY** | `s5_centralizer_and_normalizer_of_c3`, `bringStdF3_simple_s5`, `no_c5_a5_s5_fixed_in_any_pic3_extension` |
| Both $S_4$ and $S_3 \times S_2$ fix $8$ non-trivial $3$-torsion classes in $\mathrm{Pic}^0(\mathcal{B})[3]$ (`4` cyclic $\mathbb{Z}_3$-covers each; for $S_4$, $\mathrm{Pic}^0(\mathcal{B})[3]^{S_4} \cong E_{\tau_0}[3]$ via $\det M = 125 \equiv 2 \pmod 3$) | **PROVED UNCONDITIONALLY** | `bringStdF3_stabilizer_subspaces`, witness §5 |
| Under $2y_2 + 3y_3 = 0$ on $\Lambda^1 F \oplus \Lambda^2 F^*$, $2\mathcal{A}_{[\mathrm{SU}(2)_L]^2 \mathrm{U}(1)_Y} = (N_\ell - N_q)y_2$ and $9\mathcal{A}_{[\mathrm{U}(1)_Y]^3} = 54(N_q - N_\ell)y_2^3$ refute naive $H^0$-only $(3, 4)$ and vanish on Dolbeault $(3-0, 4-1) = (3, 3)$ | **PROVED UNCONDITIONALLY** | `exterior_su5_anomaly_identities`, `anomaly_matching_and_h0_only_refutation` |
| Unbroken $S_5$ forbids $H^0(K_{\mathcal{B}}) \to H^1(K_{\mathcal{B}})$ Dirac pairing ($\mathrm{Hom}_{S_5} = 0$); breaking $S_5 \to S_4$ via $\mathcal{L} \ne 0$ unlocks a unique $1\mathrm{D}$ pairing whose kernel (when $M_{\mathrm{vec}} \ne 0$) has exact dimension $3$ | **PROVED UNCONDITIONALLY** | `s5_protects_fourth_lepton_s4_unlocks_pairing` |
| Physical selection of canonical Spin$^c$ twist $K_{\mathcal{B}}$, non-trivial $\mathcal{L} \in \mathrm{Pic}^0(\mathcal{B})[3] \setminus \{0\}$, and nonzero vector-like singlet coupling $M_{\mathrm{vec}} \ne 0$ | **CONDITIONAL (Rule 13a, 0 instances)** | `BringKummerGenerationClosureHypothesis`, `quark_and_lepton_generations_eq_three_of_closure` |

---

## 2. Case I vs Case II: Why Ascending Prym–Kummer Works and Descending Covers Fail

### Case I — Ascending Unramified Kummer / Prym Cover $\pi : \tilde{\mathcal{B}} \to \mathcal{B}$ ($10 = 4 + 3 + 3$)
For any smooth projective curve $\mathcal{B}$ of genus $g = 4$ and any non-trivial $3$-torsion line bundle $\mathcal{L} \in \mathrm{Pic}^0(\mathcal{B})[3] \setminus \{\mathcal{O}_{\mathcal{B}}\}$:
1. Because $3$ is prime and $\mathrm{deg} : \mathrm{Pic}(\mathcal{B}) \to \mathbb{Z}$ is torsion-free, $3\mathcal{L} = 0$ and $\mathcal{L} \ne 0$ automatically imply $\deg \mathcal{L} = 0$, $\deg(2\mathcal{L}) = 0$, and $2\mathcal{L} = -\mathcal{L} \ne 0$.
2. By effective degree-$0$ divisor vanishing (`effective_deg_zero_divisor_eq_zero`), $h^0(\mathcal{B}, \mathcal{L}^{-1}) = h^0(\mathcal{B}, \mathcal{L}^{-2}) = 0$. By Serre duality, $h^1(\mathcal{B}, K_{\mathcal{B}} \otimes \mathcal{L}) = h^1(\mathcal{B}, K_{\mathcal{B}} \otimes \mathcal{L}^2) = 0$.
3. By Riemann–Roch ($\deg K_{\mathcal{B}} = 2g - 2 = 6$):
   $$h^0(\mathcal{B}, K_{\mathcal{B}} \otimes \mathcal{L}^t) = \begin{cases} 4 \quad (h^1 = 1, \text{ index } 4 - 1 = 3) & t = 0, \\ 3 \quad (h^1 = 0, \text{ index } 3 - 0 = 3) & t = 1, \\ 3 \quad (h^1 = 0, \text{ index } 3 - 0 = 3) & t = 2. \end{cases}$$
   On the degree-$3$ étale Kummer cover $\pi : \tilde{\mathcal{B}} \to \mathcal{B}$, Riemann–Hurwitz gives $2\tilde{g} - 2 = 3(2\cdot 4 - 2) = 18 \implies \tilde{g} = 10$, matching $\pi_* K_{\tilde{\mathcal{B}}} = K_{\mathcal{B}} \oplus (K_{\mathcal{B}} \otimes \mathcal{L}) \oplus (K_{\mathcal{B}} \otimes \mathcal{L}^2)$ of total zero-mode dimension $4 + 3 + 3 = 10$ and Prym cotangent dimension $\dim_{\mathbb{C}} \mathrm{Prym}(\tilde{\mathcal{B}}/\mathcal{B}) = 3 + 3 = 6$.
4. **Central vs Non-Central $\mathrm{SU}(3)_c$ Bundle Structure**:
   - The naive direct-image rank-$3$ bundle $\pi_* \mathcal{O}_{\tilde{\mathcal{B}}} = \mathcal{O}_{\mathcal{B}} \oplus \mathcal{L} \oplus \mathcal{L}^2$ has non-central holonomy $\mathrm{diag}(1, \omega, \omega^2) \in \mathrm{SU}(3)_c$, which **breaks** $\mathrm{SU}(3)_c \to \mathrm{U}(1)^2$ and assigns unequal zero-mode counts $(4, 3, 3)$ to the three colour lines.
   - Placing the Kummer holonomy instead in the **centre** $Z(\mathrm{SU}(3)_c) = \{I_3, \omega I_3, \omega^2 I_3\} \cong \mu_3 \subset \mathrm{SU}(3)_c$ defines the flat $\mathrm{SU}(3)_c$-bundle $\mathcal{W}_3 = \mathbb{C}^3 \otimes \mathcal{L}$ ($\det \mathcal{W}_3 = \mathcal{L}^3 \cong \mathcal{O}_{\mathcal{B}}$) with **unbroken $\mathrm{SU}(3)_c$** centralizer. Every representation of $\mathrm{SU}(3)_c$ then twists by $\mathcal{L}^t$ according to its triality $t \in \mathbb{Z}/3\mathbb{Z}$ (`QOU.Eightfold.TrialitySelectionRule.triality`), yielding **exact $(h^0, h^1) = (3, 0)$ across all three colours** for $Q_L$ ($t = 1$), $u_R^c$ ($t = 2$), and $d_R^c$ ($t = 2$).

### Case II — Complete Exclusion of Descending $\mathbb{Z}_3$-Covers $\Sigma_4 \to \mathcal{B}_0$ ($\chi_{\mathrm{eu}} = -6$)
For any cyclic $\mathbb{Z}_3$ Galois cover $\pi : \Sigma_4 \to \mathcal{B}_0$ *from* a genus-$4$ curve onto a smooth curve $\mathcal{B}_0$ of genus $g_0$ branched at $r$ points ($e_P = 3$), Riemann–Hurwitz reads $6 = 3(2g_0 - 2) + 2r \iff 3g_0 + r = 6$. Exhausting all solutions and applying Chevalley–Weil (`descending_z3_cannot_give_three_three`):

| $(g_0, r)$ | Geometric Realization on Bring's Curve $\mathcal{B}$ | Admissible Local Monodromies $(m_1, m_2)$ | Chevalley–Weil $(d_0, d_1, d_2)$ | Gives $(*, 3, 3)$? |
|---|---|---|---|---|
| $(2, 0)$ | **Realized uniquely**: $\mathcal{B} \to \mathcal{C}_2 = \mathcal{B}/C_3$ (all $20$ order-$3$ elements in $S_5$ act freely) | $(0, 0)$ | $(2, 1, 1)$ | **No** ($d_1 = d_2 = 1$) |
| $(1, 3)$ | **Obstructed as Galois quotient of $\mathcal{B}$** (no order-$3$ element of $\mathrm{Aut}(\mathcal{B}) = S_5$ has fixed points) | $(3, 0), (0, 3)$ | $(1, 2, 1), (1, 1, 2)$ | **No** |
| $(0, 6)$ | **Obstructed as Galois quotient of $\mathcal{B}$** (non-Galois trigonal rulings exist; cyclic trigonal $\Sigma_4$ has $\mathrm{Aut} \not\cong S_5$) | $(6, 0), (3, 3), (0, 6)$ | $(0, 3, 1), (0, 2, 2), (0, 1, 3)$ | **No** |

Because $d_0 + d_1 + d_2 = g(\Sigma_4) = 4 < 6$, **no descending $\mathbb{Z}_3$-cover from genus $4$ can ever give $3$ zero modes in both conjugate $\mathbb{Z}_3$-sectors**. Conversely, among unramified $\mathbb{Z}_3$-covers $\tilde{\Sigma} \to \Sigma_{g_0}$, $(d_1, d_2) = (3, 3)$ holds **uniquely at $g_0 = 4$** ($\tilde{g} = 10$).

---

## 3. Exact $\mathbb{F}_3[S_5]$ Structure of $\mathrm{Pic}^0(\mathcal{B})[3]$ & 80-dps Bring Period Lock

1. **Normalizer of $C_3$ in $S_5$**: Over all $120$ elements of $S_5$, there are $20$ elements of order $3$ (conjugacy class `3·1²`), and for $C_3 = \langle(0\,1\,2)\rangle$:
   $$|C_{S_5}(C_3)| = 6 \quad (C_3 \times S_2), \qquad N_{S_5}(C_3) = S_3 \times S_2 \quad (|N_{S_5}(C_3)| = 12).$$
2. **Simplicity, $\mathrm{Ext}^1 = 0$ Splitting, & Subgroup Fixed-Point Census on $\mathrm{Pic}^0(\mathcal{B})[3]$ (`card = 6561`)**:
   - Because $5 \equiv 2 \not\equiv 0 \pmod 3$, $D^{(4,1)} = V_{\mathrm{std}}(\mathbb{F}_3)$ (`card = 81`) is a **simple** $\mathbb{F}_3[S_5]$-module (`bringStdF3_simple_s5`), decomposing into $7$ $S_5$-orbits of sizes $1 + 5 + 5 + 10 + 10 + 20 + 30 = 81$.
   - Solving the $64$-variable Coxeter $1$-cocycle system over $\mathbb{F}_3$ gives $\dim_{\mathbb{F}_3} Z^1(S_5, \mathrm{End}_{\mathbb{F}_3}(D^{(4,1)})) = 15 = \dim_{\mathbb{F}_3} B^1$, hence **$\mathrm{Ext}^1_{\mathbb{F}_3[S_5]}(D^{(4,1)}, D^{(4,1)}) = 0$**: every $S_5$-stable integral homology lattice reduces mod $3$ to the split module $D^{(4,1)} \oplus D^{(4,1)}$ (`6561` elements, `3280` cyclic $\mathbb{Z}_3$-subgroups, partitioning into $S_5$-orbits `{1: 1, 5: 8, 10: 8, 20: 28, 30: 28, 60: 56, 120: 14}`).
   - Fixed-point cardinalities $|\mathrm{Pic}^0(\mathcal{B})[3]^H|$ (`no_c5_a5_s5_fixed_in_any_pic3_extension`, `bringStdF3_stabilizer_subspaces`):

     | Subgroup $H \subseteq S_5$ | $|H|$ | $|\mathrm{Pic}^0(\mathcal{B})[3]^H|$ | Non-trivial $\mathcal{L} \ne 0$ | Cyclic $\mathbb{Z}_3$-covers |
     |---|---:|---:|---:|---:|
     | $S_5, A_5, F_{20}, C_5$ | $120, 60, 20, 5$ | $1$ | **$0$** | **$0$** |
     | $S_4, A_4$ | $24, 12$ | $9$ | **$8$** | **$4$** |
     | $S_3 \times S_2 = N_{S_5}(C_3)$ | $12$ | $9$ | **$8$** | **$4$** |
     | $S_3, C_3$ | $6, 3$ | $81$ | $80$ | $40$ |

3. **80-dps Bring Period Matrix & $X_0(5)$ / Mod-$3$ Isogeny Confirmation**:
   - Inverting the exact rational $j(\tau_0) = -29^3 \cdot 5 / 2^5 = -121945/32$ on $\mathrm{Re}(\tau_0) = -1/2$ at `work_dps = 80` yields:
     $$\tau_0 = -\tfrac{1}{2} + i \cdot 0.18667646246280992320616288136312402946369525221883\ldots$$
     which **independently** satisfies the $X_0(5)$ relation $j(5\tau_0) = -25/2$ with residual $8.23 \times 10^{-79}$.
   - Braden–Disney-Hogg's principal polarization multiplier $M$ ($\Omega_{\mathcal{B}} = \tau_0 M$) has spectrum $\{1^1, 5^3\}$ (`1 ⊕ 3` orthogonal eigenprojector residual $5.27 \times 10^{-82}$) and $\det(M) = 125 \equiv 2 \not\equiv 0 \pmod 3$. Because $\gcd(125, 3) = 1$, the isogeny $\mathrm{Jac}(\mathcal{B}) \to E_{5\tau_0}^3 \times E_{\tau_0}$ is an **isomorphism on $3$-torsion**, identifying the $8$ non-trivial $S_4$-invariant classes $\mathrm{Pic}^0(\mathcal{B})[3]^{S_4} \setminus \{0\}$ directly with $E_{\tau_0}[3] \setminus \{0\}$ (`theta_3` quasi-periodicity residual $6.14 \times 10^{-80}$).

---

## 4. Gauge Anomaly Cancellation on $\Lambda^1 F \oplus \Lambda^2 F^*$ & Honest Lepton Scope

For $F = W_2(y_2) \oplus W_3^*(y_3)$ satisfying $2y_2 + 3y_3 = 0$, the five Weyl multiplets of $\Lambda^1 F \oplus \Lambda^2 F^*$ ($L_L, e_R^c, d_R^c, Q_L, u_R^c$; $2 + 1 + 3 + 6 + 3 = 15$ states/family) satisfy exact division-free anomaly identities over any commutative ring (`exterior_su5_anomaly_identities`):
$$2\mathcal{A}_{[\mathrm{SU}(3)_c]^2 \mathrm{U}(1)_Y} = 0, \quad \mathrm{Tr}(Y) = 0, \quad 2\mathcal{A}_{[\mathrm{SU}(2)_L]^2 \mathrm{U}(1)_Y} = (N_\ell - N_q) y_2, \quad 9\mathcal{A}_{[\mathrm{U}(1)_Y]^3} = 54(N_q - N_\ell) y_2^3.$$

This sharply separates what is **kinematically/anomalously forced** from what remains **dynamical**:
1. **Naive $H^0$-only truncation $(N_q, N_\ell) = (3, 4)$ is strictly forbidden**: Discarding $H^1(\mathcal{B}, K_{\mathcal{B}}) \cong \mathbb{C}$ while keeping $H^0(\mathcal{B}, K_{\mathcal{B}}) \cong \mathbb{C}^4$ violates $[\mathrm{SU}(2)_L]^2 \mathrm{U}(1)_Y$ ($= y_2/2 \ne 0$), $[\mathrm{U}(1)_Y]^3$ ($= -6y_2^3 \ne 0$), and Witten's global $\mathrm{SU}(2)_L$ $\mathbb{Z}_2$ anomaly ($4 + 3\cdot 3 = 13$ odd Weyl doublets).
2. **Full Dolbeault complex $(3, 0)_{\mathrm{quark}} + (4, 1)_{\mathrm{lepton}}$ is anomaly-free**: Retaining $H^1(\mathcal{B}, K_{\mathcal{B}})$ gives $N_\ell^{\mathrm{net}} = 4 - 1 = 3 = N_q$ ($12$ even net doublets; 80-dps residual $8.43 \times 10^{-81}$), consisting of $3$ chiral lepton families plus $1$ vector-like pair $(L_{4,L} \oplus \overline{L_{4,L}}, e_{4,R}^c \oplus \overline{e_{4,R}^c})$.
3. **$S_5 \to S_4$ breaking removes chiral protection on the 4th lepton pair**: At $\mathcal{L} = 0$ (unbroken $S_5$), $\mathrm{Hom}_{S_5}(V_{\mathrm{std}}(F), F) = 0$, protecting all $4$ modes of $H^0(K_{\mathcal{B}})$ from pairing with $H^1(K_{\mathcal{B}})$. Because $\mathrm{Pic}^0(\mathcal{B})[3]^{S_5} = \{0\}$, any $\mathcal{L} \ne 0$ breaks $S_5$; for $\mathcal{L} \in \mathrm{Pic}^0(\mathcal{B})[3]^{S_4} \setminus \{0\}$, $\dim_F \mathrm{Hom}_{S_4}(V_{\mathrm{std}}(F), F) = 1$ (`s5_protects_fourth_lepton_s4_unlocks_pairing`), permitting a unique $G_{\mathrm{SM}} \times S_4$-invariant Dirac mass term $M_{\mathrm{vec}}$ whose kernel (whenever $M_{\mathrm{vec}} \ne 0$) has exact dimension $3$ (`V_{(3,1)}`).
4. **Honest Residual Hypotheses (`BringKummerGenerationClosureHypothesis`, Rule 13a)**: Because a vector-like pair $(1_L, 1_R)$ has zero gauge anomaly even at $M_{\mathrm{vec}} = 0$, anomaly cancellation forbids $(3,0)+(4,0)$ rather than forcing $M_{\mathrm{vec}} \ne 0$ by itself. The three surviving physical inputs—(i) Spin$^c$/canonical bundle coupling $K_{\mathcal{B}}$ rather than untwisted $K_{\mathcal{B}}^{1/2}$, (ii) vacuum selection of a non-trivial central $\mu_3$ Kummer class $\mathcal{L} \in \mathrm{Pic}^0(\mathcal{B})[3]^{S_4} \setminus \{0\}$, and (iii) nonzero vector-like singlet mass $M_{\mathrm{vec}} \ne 0$ (Georgi survival hypothesis)—are cleanly isolated in `BringKummerGenerationClosureHypothesis` with zero instances.
