---
# qou-ni4b
title: 'GAP: SU(3) colour action on the QOU three-strand Hecke state space — abstract module exists, framework-native action open'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-colour
created_at: 2026-07-31T19:56:30Z
updated_at: 2026-11-23T21:03:57Z
parent: qou-8lxd
---

2026-08-02 sharpened status.

This is now strictly the framework-native colour-action gap.

- CLOSED precursor: the abstract colour-action class is already satisfied on the octonion base module `O = C ⊕ C^3` (`sm-colour-stabilizer-action`; `OctonionColourActionBaseModule.lean`). So this is no longer 'octonion fragments only'.
- OPEN content: construct an injective colour action on the framework's own three-strand Hecke / braid-state module, not merely on some faithful module somewhere.
- Required strengthening for real closure: the action should target the QOU three-strand state space and be compatible with its Hecke / braid structure.

Keep this bean separate from qou-d7h1: colour SU(3) acts on the underlying strand state space; flavor SU(3) organizes hadron multiplets.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-02 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress update 2026-11-16 (PR #8139, `0435e799b9eb320f989c979717153b33245cefc1`)

Formalized the exact 3-strand Hecke vs $\mathfrak{su}(3)$ dimension, derived commutant Lie algebra, and reality/cubic-anomaly obstructions in `folio/quantum-observable-universe/lean/QOU/StandardModel/ThreeStrandColourTowerCP.lean` (wired into `QOU.lean`, `0` `sorry`, `0` custom axioms) with 50-dps + symbolic probe `computations/probes/three_strand_colour_tower_cp_probe.py`:
- `h3_wedderburn_dim_sum`: $\dim H_3(q) = 1^2 + 2^2 + 1^2 = 6 = 3!$.
- `h3_irrep_dim_lt_su3_fund` & `specht_end_dim_lt_su3`: every irreducible Specht module $V_\lambda$ of $H_3(q)$ has $\dim V_\lambda \le 2 < 3 = \dim_{\mathbb{C}} \mathbf{3}$ and $\dim \mathrm{End}(V_\lambda) \le 4 < 8 = \dim \mathfrak{su}(3)$.
- `h3_commutant_derived_lie_dim_eq_three`: the derived Lie algebra $[\mathrm{End}_{H_3}(H_3), \mathrm{End}_{H_3}(H_3)] \cong 0 \oplus \mathfrak{sl}_2 \oplus 0$ of the 6D regular commutant has dimension $0 + 3 + 0 = 3 < 8 = \dim [\mathfrak{su}(3), \mathfrak{su}(3)]$.
- `specht21_vs_su3_triplet_obstruction` & `schurWeyl_su3_three_strand_decomp`: at real $q_0 > 1$, $V_{(2,1)}$ is real self-conjugate ($C_3 = 0$), whereas $\mathbf{3}$ of $\mathfrak{su}(3)$ has non-zero cubic Casimir anomaly $C_3(\mathbf{3}) = -C_3(\bar{\mathbf{3}}) \ne 0$ ($\mathbf{3} \not\simeq \bar{\mathbf{3}}$), requiring the complexified octonion/tensor module $\mathbb{O} = \mathbb{C} \oplus \mathbb{C}^3_e$ (`OctonionColourActionBaseModule`) and $(\mathbb{C}^3)^{\otimes 3} = (10 \times 1) \oplus (8 \times 2) \oplus (1 \times 1)$ ($\dim_{\mathbb{C}} = 27$, unique 1D singlet $\Lambda^3(\mathbb{C}^3) \otimes V_{(1^3)}$). Kept `in-progress` per owner bean policy.


## 2026-11-22 — colour action family K0–K4 (PR #9059, prereg c7a93364905, probe 72f583c6d27, result 59695ad7ecd)
computations/probes/qcd_colour_action/RESULT.md. Exact over Q(p,q).
- K0 (R = 1_c ⊗ Ř_f, colour as fixed-position label): (a)–(e) pass; the singlet sector is exactly the nucleon model, z = q³/(q²+1). (f) fails: colour does not move with the strand.
- K1 gl₃ Jimbo: z₃ = q³/[3]_q ≠ z_D. K2 gl₆ Jimbo: Hecke holds, but no colour action in the searched class (classical: witness 1−q; summed q-Chevalley: [e,f] ≠ [k]); z₆ = q⁶/[6]_q. K3/K3′ not Hecke.
- K4 (s_c⊗X + a_c⊗Y, 32 members): a transported colour⊗flavour braid holds iff p²=1 and q²=1 (Gröbner basis). This is a structural exclusion inside the class, scope (a) outside it.
Still open. Closure needs either an owner ruling that K0 counts, or a coideal / twisted colour symmetry of gl₆ outside K4. Not formalised in Lean.

2026-11-22 (spin/background-field probe, PR #9059, computations/probes/qcd_spin_background/, prereg 0415291e97a, probe 4a21dae23ee 39/39, RESULT aa514549e55): scope-(a) MISS. Background colour holonomy K^{(x)n} on (C^N)^{(x)n} (exact Q(q), N=2,3,4): susceptibility at q=1 is sum l_i^2 N^(#cyc-1) (strand winding squared, not spin); Hecke-sign (S2) ratio 2/N; full-twist (S1) expansion 2N+8hbar+4N hbar^2, all positive, only negative constant the -1/N sl-framing. N=3 coincidences 2/N=1-1/N=2/3=(2*1/2)^2-1/3 are N-dependent traps, do not cite. Post-hoc: photon s0s1^-1 alone has negative hbar^2 coefficient -4(N^2-3). No paramagnetic/diamagnetic split exists in colour-only data; the 11/3:-1/3 structure needs a non-colour spin factor = the un-derived theta_I=1 hypothesis of TwistedChannelSplitting.lean. Heat-kernel per-state susceptibility 1 -> 12/17; its RG sign is convention-set. No gluon selected.

2026-11-22 spin-factor probe (PR #9059; 2abaa8ed425 prereg, c3f1b05557a probe, 18dfa1a27e4 result). P1: no transported member of the 16-member commutant class (Jimbo R for colour (x) spin, eigenvalues q, -1/q) braids at real q>1; elim ideal contains q^2(q^2-1)^2(q^2+1)^3(q^4+q^2+1). Scope (b) within the class only. P2: theta_I=1 derived in D/F; no (2s)^2-1/3 split. P3 MISS; -1/3 at N=2 for Lambda^2 W is a post-hoc coincidence. Gluon stays open.



## 2026-11-22 — full-tower colour (owner: "What about looking in the full Tower for the color")
PR #9059. Prereg e16afb61a6d, probe in c3f1b05557a (swept into the sibling's commit, after the prereg), RESULT 5ab55a24497, computations/probes/qcd_colour_full_tower/. 27/27 exact over Q(q).

**T1.** On (C^3)^n the full H_n(q) has U_q(gl3) as commutant, and that action meets (a)(b)(c)(f). The diagonal Markov twists K give z by rank: rank 1 gives q, rank 2 gives z_D (all three supports), rank 3 gives z_3. The unique U_q(gl3)-invariant twist is diag(q^-4,q^-2,1), which is rank 3, i.e. z_3. So convention D is the colour-twisted trace with a SINGULAR twist. Its stabiliser is U_q(gl2) x U(1), and (d) fails: scope (b) within diagonal twists on C^3.

**T4, confirmed.** The colour-singlet sector of (C^3)^{3A} is the (A,A,A) block, which lies in D's radical (dim n!-Catalan) for every A. Scope (b), from ocneanuWeight_conventionD_eq_zero_of_three_rows. In other words, the colour is in the tower and D puts every colour singlet in its radical.

**T2.** The relative commutants have M3 blocks at depth 3, which is generic (a pre-declared coincidence). (b) fails because the centre is commutative.

**T3.** There is no Z3 at real q>1: V^3 is scalar on (2,1) iff h^2(h^2+2)=0, and the branching-graph automorphism group is {id, transpose} / trivial.

**Not tested:** non-diagonal or non-grouplike central twists. Those would be selection.

**Bean stays open.**



## 2026-11-22 — residual symmetry of the D colour twist (PR #9059, computations/probes/qcd_d_residual_symmetry/)

Prereg 3f7b5b43e13; probe 3b45170517a; out 055432050b4; RESULT 2556e7c3247. 27/28 exact over Q(q); the one FAIL is my own pre-registered R3 prediction.
- R1: on (C^3)^n, D = the U_q(gl2) quantum trace on (C^2)^n, extended by zero (K_D = pivotal * q P_12). The twist forces the 2+1 split and the selection rule N3 = 0 (K_D^n N3 = 0). It does not force U(1) charge values; the traceless diag(1,1,-2) is a convention.
- R2: [N3, rho(w)] = 0 for the photon, the electron s0s1s0, the trefoil, the quark letters and V^3. Scope (b) by Schur-Weyl: the U(1) labels colour states, never words. So it cannot be the missing word-level hypercharge.
- R3: each of {1,2}, {2,3} and {1,3} leaves a rank-1 U_q(gl2)xU(1); on {1,3} this is the root-(a1+a2) q-sl2. The pre-registered prediction 'Cartan only' FAILED. All three give the same H_n trace, so the choice is a selection that no Hecke observable sees.
- R4: the -2 ratio comes from tracelessness alone; the mixing family is 1/(12 s^2+1). No Weinberg angle is forced.
Verdict: a colour-breaking stabiliser, not electroweak. This is a reading argument, not an invariant. Bean stays open.



2026-11-22 (Lean): QOU/Braiding/ColourTwistMarkov.lean, commit 84123d764ed on claude/qcd-heat-kernel-beta0-sign-2026-11-22 (PR #9059). Sorry-free over a generic [Field R]. Proved:
- Jimbo gl3 Hecke relation (jimboR_hecke).
- Markov step for all n (twisted_trace_markov): P K = s K implies tr_{n+1} = s tr_n, so z = s/tr K.
- The rank of K fixes z: rank 1 gives q, rank 2 (all supports) gives q^3/(q^2+1), rank 3 gives q^5/(q^4+q^2+1) with K forced to k2*(q^-4,q^-2,1).
- rank_two_twist_conventionD: z(q+q^-1) = q^2; composed with ocneanuWeight_conventionD_eq_zero_of_three_rows.
- An E1,E2-invariant diagonal twist is m2*(q^-4,q^-2,1): invertible, never rank 2, never z_D.

NOT proved: the braid relation for Ř; the trace property on the image of H_n; Ocneanu uniqueness. So the D identification holds at the parameter level only.

Verification: lean-direct exit 0; #print axioms shows no sorryAx.

2026-11-22 coideal-colour probe (PR #9059, computations/probes/qcd_coideal_colour/; prereg 096d888f561, probe d97eaeddd46 35/35 exact Q(q,c1,c2), RESULT d14cd6d8b34): Letzter coideals of U_q(gl3), AI (so3) and AIII (gl2+gl1), s=0, c free. Both commute with Hecke and transport (inherited from B in U, not new), but the q->1 Lie dims are 3 and 4, not 8, so NOT colour (Q4 fail, pre-registered). AIII K-matrix: the RE on the commutant pencil cuts out J ~ J0^-1, a quadratic type-B generator with ratio -c2/(c1 q) set by the free c. On type-A H_n every B-invariant product twist T1(x)g^(n-1) gives z3 (Schur on the partial quantum trace); no c makes any rank-2 D twist B-invariant. D not recovered. Remaining untested lead: the (gl6, gl3+gl3) coideal on C3(x)C2, whose fixed points contain the diagonal sl3(x)1. Also: LITERATURE.md cites math/0512581 as Kolb-Stokman; it is Kolb, 'Quantum symmetric pairs and the reflection equation'. Gluon open. Bean stays open.


### 2026-11-22: rank-2 twist = convention D at the level of the weights (n = 2, 3), commit 47c1f59411e, PR #9059

`QOU/Braiding/ColourTwistMarkov.lean` adds the following, all sorry-free over a generic `Field R` (lean-direct exits 0):
- `sig_braid`: the braid relation for Ř on (R³)^⊗3.
- `sig1_sq` / `sig2_sq`: the Hecke relations.
- `twist_two_comm`: [K⊗K, Ř] = 0.
- `twist_comm_last` and `twist_comm_extend`: the all-n induction steps of the trace property.
- `twisted_trace_comm_H3`: the trace property on the subalgebra generated by σ₁ and σ₂.
- `rank_two_twisted_values`: τ(σ) = z_D and τ(σ₁σ₂) = z_D².
- `rank_two_twist_weights_H2` / `_H3`: the moment equations force the convention-D weights. y_(1³) = 0 comes via `threeRow_eq_zero_of_jones_ocneanu`; [2]²·y_(2,1) = 1.

Scope: n ≤ 3. That a trace on H₃ is fixed by its values on 1, σ₁, σ₁σ₂ (Geck–Pfeiffer / Ocneanu) is cited, not proved. The corpus has no general-n uniqueness theorem. This is a formal check of Turaev 1988 and Wenzl 1988. The bean stays open: the SU(3) colour action itself is still the gap.


2026-11-22 (gl6 coideal probe, PR #9059, d1eba94ddc9): the (gl6, gl3+gl3) Letzter coideal contains B^col = <B1,B2,B4,B5,T1..T3>, which satisfies the U_q(sl3) relations exactly on (C^6)^n, n<=3. It is gl3(x)1 at q=1 and commutes with the transported gl6 Hecke action. It meets (a)(b)(c)(e)(f) and evades K4 (q^2=1), because its coproduct is flavour-dependent at q!=1. (d) fails: the singlet sector is S^(1^3)x4 + S^(2,1)x2, i.e. the fermionic flavour model -R_f^-1, with z = z_D(-q^-1). The reason is that at q=1 the epsilon singlet gives sigma = -P_f. So (d) and (f) are incompatible for any transported sl3(x)1 colour: scope (b), S3 sign invariant, argument not in Lean. Open: whether (d) is the right test (owner). Bean stays open.

Claimed by claude/w7-chen-mult-integral-masstrace-20261123 (Worker 17, 2026-11-23)
