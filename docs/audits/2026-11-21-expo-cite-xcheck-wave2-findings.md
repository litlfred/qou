# Cite and cross-check exposition blocks: wave-2 findings (2026-11-21)

Bean-drain list `expo-cite-xcheck` (47 beans), issue #8802, branch
`claude/expo-cite-xcheck-wave2-2026-11-21`. Wave 1 is
[`2026-11-21-expo-cite-xcheck-findings.md`](2026-11-21-expo-cite-xcheck-findings.md)
(merged in #8852); its findings F1–F10 are not repeated here, and this file
numbers its findings from F11.

Every cross-check below is a pre-registered probe under
`computations/probes/`. Each probe's criteria sit in its docstring, written
before the first run. Any change after a run is recorded there as an
AMENDMENT with thresholds unchanged. Arithmetic is exact (sympy) or mpmath at
60–400 dps. No float64 enters a result. Source claims were checked against the
held text (`library/<doc-id>/sections/`), and every source misprint below was
confirmed on the PDF page image, not just the text layer.

No mathematical statement in the corpus was rewritten. Every bean was checked
against `docs/coordination/owner-rulings.md` and the AGENTS.md rulings for
superseded premises; those are in §3.

## 1. Cross-checks run (12 beans, all PASS after documented amendments)

| bean(s) | probe | result |
|---|---|---|
| qou-epkn, qou-ohl6, qou-68uk, qou-u33z (wave-1 F3) | `one_loop_torsion_crosscheck_probe.py` | Resolves F3. The three "disagreeing" values of \|τ(4₁)\| are τ_μ = √3/2, τ_λ = 3, and √3 (the known factor-2 bug). They agree once the peripheral curve is named. The twisted torsion of 4₁ is t(t−1)(t²−5t+1) (arXiv 2109.00379 eq. 69) and d/dt at t = 1 gives −3 = τ_λ. The ratio τ_λ/τ_μ is the conjugate cusp shape 2√3. \|τ(5₂)\| = 1.16116273813391… is invariant over 8 triangulations and over every flattening. See F11. |
| qou-t579 | `twist_knot_minimal_relation_character_variety_probe.py` | The t = −1 factor of the Gelca–Nagasato relation vanishes on Riley's nonabelian component for 3₁, 4₁, 5₂, 6₁. The corpus 4₁ A-polynomial vanishes on the Riley curve. See F12, F13. |
| qou-tiwv | `takata_twist_knot_colored_jones_probe.py` | [takata2008] Cor. 5 gives the Jones polynomials of 3₁, 4₁, 5₂ (checked against a Kauffman-bracket state sum). The Kashaev invariant of 5₂ extrapolates to \|ω\| = 0.6562033703. That agrees with Ohtsuki's printed value to 2.8e-10 and with the corpus closed form (2\|τ(5₂)\|)^{-1/2} to 3.5e-10. See F14. |
| qou-7q3s | `takata2004_masbaum_twist_knot_probe.py` | [takata2004]'s Masbaum form equals the corpus 4₁ Habiro tower (n ≤ 6) and the corpus trefoil tower (n ≤ 5). Its A-polynomials contain Hoste–Shanahan's, and A_{K₋₁} equals minus the corpus 4₁ A-polynomial. The 4₁ Kashaev limit is 3^{-1/4} (rel 2e-10). See F15. |
| qou-o4k6 | `ohtsuki_5_2_asymptotic_crosscheck_probe.py` | [ohtsuki2016] Thm 1.1 for 5₂: 2π Re ς = Vol(5₂) (5.6e-11), 2π Im ς = CS(5₂) mod π² (4.1e-10). κ₁ is recovered from the Takata Kashaev values to 2.4e-6, and the N = 200 table entry is reproduced to 4.5e-7. See F16. |
| qou-5zbn | `schlesinger_distribution_li2q_probe.py` | Schlesinger Lemma 4 in QOU's Li₂^q normalisation: Σ_{yⁿ=x} Li₂^q(y) = Li₂^{qⁿ}(x)/[n]_q, to 1e-58 (via [nm]_q = [n]_q[m]_{qⁿ}). The same-q decoy misses by 5.3 %. See F17. |
| qou-0seq | `evans_berger_third_order_winding_probe.py` | Evans–Berger Ψ₁₂₃ on (σ₁σ₂⁻¹)³ is 1, which is the Magnus μ̄, independent of shape. Ψ(PP⁻¹) = 0. With a Hopf spectator Ψ is additive, and Ψ(Hopf) = 0. Agrees with the corpus μ̄ machinery. |
| qou-2pp7 | `broadhurst_dedekind_zeta_volume_probe.py` | [broadhurst] rational invariants a/b reproduced for 4₁, 5²₁ (1) and 6³₁ (2). The corpus value for 8G is 1/2. 8₁₁ has a degree-10 shape field, which the formula does not cover. See F18. |
| qou-cp1x | `morita_ramanujan_qairy_connection_probe.py` | Morita's connection formula holds to 8e-40. The corpus A_w zeros are zeros of Morita's bracket, the θ lattice gives w^{1−2n}, and the −κwⁿ refinement is confirmed at w = 0.49 and 0.7. At w_p the n ≤ 6 zeros are pre-asymptotic (n₀ ≥ 10). |
| qou-godb | `gw_modular_monodromy_vs_routeB_probe.py` | Garoufalidis–Wheeler eq. (28) equals the corpus GGM eq. 49 under p = 1/q, t = p^m, f = q^m z. M₂₁ of (25)/(31) is q-elliptic (3e-49). See F19. |
| qou-spds | `weaving_link_rmatrix_state_sum_vs_borromean_tower_probe.py` | The R-matrix state model of [arxiv-2209.06973v1] (§5) gives W(3,1) = 1. W(3,2) = 4₁ equals the corpus Habiro tower (n = 1, 2, 3). W(3,3) = Borromean equals the corpus J_B(N,N,N) times [N]², a pure normalisation: the paper divides by the long component only. See F20. |
| qou-ipnr | `drsz_two_level_qborel_vs_c1_degree_budget_probe.py` | DRSZ Thm 4.13 (Δ = (xσ−1)(x²σ−1), ΔŶ = 1 + x) holds exactly, and so does the q-Borel product rule. The order-≥ 3 growth of P holds (log₂\|p_n\|/n² → −1/6). C1 has one Newton slope at ∞ against Δ's two at 0. Slopes are gauge invariant, so C1 is not of that multi-level type. See F21, F22. |

## 2. Statement-correctness findings for the owner

Source misprints (each confirmed on the page image; none changes a corpus number):

- **F12 (qou-t579).** Gelca–Nagasato Thm 4 as printed does not reproduce the paper's own §3 factorizations. The paper's Lemma 1 + Lemma 3 recursion does, and so does Thm 4 with two signs flipped (S_m(y) carries t⁻⁶ **+** t⁻²x²). The character-variety claim holds.
- **F14 (qou-tiwv).** [takata2008] p. 278: the Habiro/Le form has a spurious (q)_m in the denominator. Without it, it equals the paper's (14) for n = 1..6.
- **F15 (qou-7q3s).** [takata2004] eq. (2) carries an extra (−1)^{k+1} (it gives J(1) = −1), and eq. (4) has (1 − q^k) where the ratio needs (1 − q^{k+1}). Neither reaches Thm 2.2.
- **F21 (qou-ipnr).** DRSZ (4.11.5) is short by a factor 2: P(q^m) = **2**·(−1)^m q^{m(3m+1)/2}(q⁻¹;q⁻¹)_m(q⁻¹;q⁻¹)_∞ for m = 0..5, to 1e-40. The factor 2 is forced by the k ↔ n−k symmetry of the Borel coefficients Σ_k q^{−k(n−k)}.
- **F22 (qou-ipnr).** DRSZ Ex. 4.11(2) drops the sign (−1)^n from the Taylor coefficients of Π(1 − q^{−n}ξ). This is harmless for the growth claim, which uses |a_n|.
- **F20 (qou-spds), minor.** [arxiv-2209.06973v1] states the jump direction both ways (§3: colours increase along an overcrossing; §5: they decrease). The per-sign (i,j) labelling appears only in Figure 8. The model cannot be implemented from the text alone. The probe pins the convention with the paper's own framed-unknot examples and RII/RIII.

Corpus-side findings (labels, scope and normalisation; no number is wrong):

- **F11 (qou-epkn and the F3 group).** `torsion_nu_sdp_probe` labels the value 3 as T_μ. It is τ_λ (the longitude torsion), and τ_μ = √3/2. The value is right and the name is wrong. Any sentence quoting "T_μ = 3" inherits the mislabel. Rename and grep are the owner's call (no sweep done).
- **F13 (qou-t579, bean premise).** The named target `computations/complex_volume_witness.py` uses no character-variety polynomial, so there was nothing there to compare. The only 4₁ character-variety object in `computations/` is the A-polynomial in `qbeta_substrate_meridian_branchpoint_probe.py`, and it agrees.
- **F16 (qou-o4k6, bean premise).** The named Lean target `QOU.QBeta.Stokes3LargeOrderAmplitude` concerns 4₁ only and carries no 5₂ object. The comparison was made against the corpus 5₂ one-loop probe instead.
- **F17 (qou-5zbn, scope).** `prop:cl3-zeta5-orbit-sum-identity` is classical (q = 1). Schlesinger's q-distribution relation changes the base on the right side (q → qⁿ), so a q-deformation of the orbit-sum identity cannot keep a single q. The N = 5 orbit-sum ratio at q₀ is −0.834, not 1.
- **F19 (qou-godb, category).** The corpus "Route-B" growth (γ = 0.274 and 0.249 in the witness) is a growth exponent of a θ-quotient. Garoufalidis–Wheeler's M₂₁ is a modular **monodromy** entry. These are different kinds of object, so the bean's comparison does not apply as worded. The identity GGM eq. 49 = GW eq. (28) does hold, and that is the usable link.

## 3. Superseded premises

- **F18 (qou-2pp7).** `binding-link-volumes.witness.json` scores the deuteron with a hyperbolic volume and picks census links by volume. Ruling A (2026-08-29) says the deuteron binding is not a volume term, and the census route was retired on 2026-09-05. The Broadhurst invariants were checked as mathematics only. No binding comparison was made.
- **qou-hjnx (not run, left open).** The triton, ³He, ⁴He and deuteron binding values in `canonical-mass-table-extended.witness.json` sit on the inter-nucleon bond letters ('averaged', 'averaged_weighted'). The 2026-11-15 γγ ruling made those letters non-canonical (`2026-11-15-gg-rule-rescopes-old-letter-binding.md`). Placing them on the Tjon band would test a superseded word. The band is located in [klein-fewbody] §§ sec-030, sec-034, sec-041, ready for the redo after #7876.
- **qou-c9uj (not run, left open).** The target `gmo_meson_crosscheck.py` is marked SUPERSEDED in its own docstring (2026-08-07), and no derived π±/π⁰ splitting exists. The textbook mechanism is a virtual-photon self-energy, which the 2026-11-16 ruling excludes from QOU. Recorded instead: [kleinkreisler1996]'s negative (one q of U_q(sl₂) cannot fit the splitting) constrains any future route that puts it in an isospin deformation at q₀ alone.

## 4. Not done in this wave (unchanged from wave 1)

`qou-1rgm` (F5), `qou-njry` (F6), `qou-udpt` (F7), `qou-jncu` (source re-upload
needed), `qou-xugx` (Gasper–Rahman not held). Each is either an owner call or
blocked on a missing source; see wave-1 §4–5.

## 5. Tally

Of the 47 beans, 36 are completed, 4 were scrapped in wave 1, and 7 are open:
the 5 above plus `qou-hjnx` and `qou-c9uj` (premise-blocked).
