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
updated_at: 2026-11-22T16:47:11Z
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
