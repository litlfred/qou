---
# qou-g0jn
title: 'GAP: beta-decay rate law — μ₀, |M_q|², f(Q) underived; no trigger/probability mechanism; no SDP→rate link'
status: todo
type: task
priority: normal
created_at: 2026-11-15T19:00:22Z
updated_at: 2026-11-15T20:13:09Z
---

Opened 2026-11-15 from owner question on a decay trigger and translating ILP/SDP likelihood into a rate; owner chose 'bean both gaps, then probe'. prop:hadron-half-life: Γ_β = |W|²μ₀/(2π³)·[2]_q·|M_q|²·f(Q). W(q) has a D closed form (qou-egvf); μ₀, |M_q|² (prop:trace-ratio-observable, proportionality only) and f(Q) do not. def:beta-decay-skein says WHAT, not WHEN. LP/SDP shadow prices are used only for shell binding from measured Q-values. Candidate to test, pre-registered: per-step probability = trace weight of the channel where the insertion reduces to the daughter. half-life-as-q-probe states environmental predictions (neutron-star q ≫ q₀; 1e-9 per metre) with no derivation — scope (a). Neutron lifetime not derived.



## 2026-11-15 pre-registration blocked by qou-0whz C3 (PR #7968)
The planned probe was 'per-step decay probability = trace weight of the channel where the T(3,5) insertion reduces to the daughter'. C3 shows that insertion can never reduce to daughter ⊔ T(2,3) ⊔ unknot (≤3 components vs ≥5). So the 'channel' has no definition yet, and building one now would be a choice made against the target. The probe waits until a strand-creating W morphism (E/F ⊗ coevaluation) is defined. Then the channel weight is the trace of that morphism's image, fixed before any comparison with τ_n.


## PRE-REGISTRATION 2026-11-15 19:35Z (owner card: 'Probe both, compare'), written before any computing
Question Q (same for both arms): applied to the neutron state (labels udd, with u = the K = q vector, as derived in #7971), does the map give a component proton-labels (uud) ⊗ X, where X has weight T³ = -1 (W⁻ quantum numbers)? Report the coefficient as an exact function of q, for each variant. No target value; CODATA/PDG are not used. A nonzero coefficient means 'allowed', not 'rate'.
Arm A, strand/categorical: maps built from the braiding and coev (U_q intertwiners). Concretely V -> V ⊗ (V ⊗ V*) by coev, then one crossing of the incoming strand with the created V. Variants: crossing sign ±; coev plain Σ e_i⊗e^i or pivotal Σ K e_i⊗e^i; both R conventions.
Arm B, 𝓗_q substrate Δ, read as deconcatenation of braid words (q-shuffle Hopf algebra, notation register table 4). This reading is an assumption, flagged. Test words: s1^4, (s1 s2)^5, s1 s2 s1. Each tensor factor of Δ(w) acts on the same 3 strands.
Prediction made in advance, stated before computing: Arm B coefficient = 0 for every word, by C2 (letters preserve weight). Arm A: nonzero only through the transposition term. Either outcome gets reported.


RESULT 2026-11-15 (PR #7973, d4ba09a0b0). Arm A gives a W⁻ coefficient of 1 (plain coev) or q (pivotal). It is the same for both signs and both R conventions, and comes from the transposition term, so no strand changes flavour: this is quark rearrangement, a d ū pair with π⁻ and W⁻ quantum numbers. It carries no chirality or weak suppression, so no rate. Arm B (deconcatenation, an assumed reading) gives 0, as predicted. Next: the flavour-changing E/F vertex (left projector) that composes with the arm A split. Bean stays open.


## PRE-REGISTRATION 2 (2026-11-15 19:43Z): flavour-changing vertex, written before computing
Fact used: Hom_{U_q}(V, V⊗V⊗V*) ≅ End_{U_q}(V⊗V) = span{1, Ř}, so every equivariant one-quark vertex is (a·1 + b·Ř) ⊗ id after coev. Check: the coefficient of u⊗(d ūbar) (W⁻), as an exact function of q, for the vertex built from P₊ = (Ř+q⁻¹)/[2] (left line, |eig| = q > 1), from P₋ = (q−Ř)/[2] (right line), and from the weak vertex W = σP_R + σ⁻¹P_L (corpus). Compare left with right: is |amplitude| different? I predict the same magnitude 1/[2] on both lines, opposite sign. If so, the magnitude cannot carry chirality at one crossing.


RESULT 2 (PR #7977, a6c632fc1f): the prediction held. The W⁻ amplitude b is +1/[2] on the left line and −1/[2] on the right, the same magnitude. Chirality is only in the non-emitting part a, as a ratio of q². The corpus W gives b = 2/(q²+1). So at one crossing the emission rate cannot see chirality. Next candidate: chirality enters through what follows the vertex (W⁻ → e⁻ ν̄ on the lepton strands), or across several crossings.


## PRE-REGISTRATION 3 (2026-11-15 19:55Z): lepton strands, written before computing
Owner choice: both, leptons first. Leptons are taken as a second copy of the same doublet V (ν = the K = q vector, e = the other); this is an ASSUMPTION about how leptons carry T³.
Q3a: dim End_{U_q}(V⊗V*), and the action of each equivariant endomorphism on the W⁻ line (weight −1). Prediction: dimension 2, spanned by id and coev∘ev, and coev∘ev kills the W⁻ line, so any quark-pair → lepton-pair transfer acts on W⁻ as a single scalar.
Q3b: the full chain amplitude n → p e⁻ ν̄ = b_q · c · b_ℓ, for the four left/right choices of the quark and lepton vertices (b = ±1/[2] from PR #7977). Prediction: |amplitude|² is the same for all four (chirality-blind). Only the sign differs: LL = RR = +, LR = RL = −. So the sign can matter only through interference, which is test 4.


## RESULT 3 (Q3a/Q3b; pushed with test 4)
Both predictions held. End(V⊗V*) has dimension 2. The W⁻ line has K eigenvalue q⁻², and each generator acts on it as a scalar (1 and −q⁻²). The chain amplitude is c·q²/(q²+1)² × (+1 for LL and RR, −1 for LR and RL), with the same magnitude for all four. Caveat: Q3b is almost arithmetic once b = ±1/[2] is known.
## PRE-REGISTRATION 4 (2026-11-15 20:00Z), multi-crossing interference, written before computing
At each letter of a word, the vertex's deviation from the bare letter is δ = W(letter) − letter. On σ this is −hP_L. On σ⁻¹ it is hP_R, from W(σ⁻¹) = W(σ) (#7975). The local W⁻ amplitude per site is the Ř-coefficient of δ. Q4: compute the site amplitudes, and their sum, for words of mixed sign: s1 s2⁻¹ (γγ letter), (s1 s2⁻¹)³, s1⁴, (s1 s2)⁵. Do the same for the mirror vertex (P_L ↔ P_R). Prediction: every site gives the same amplitude −h/[2] whatever the letter's sign, so the sum is −len(w)·h/[2] (constructive interference), and the mirror vertex gives +len·h/[2], the same magnitude. LIMITATION, stated in advance: these are local site amplitudes; dressing by the rest of the word acting on the state is not included.


RESULT 4 (PR #7979, ac53c140f1): the prediction held. Every site gives −h/[2] whatever the letter's sign, so the sum is −len·h/[2]; the mirror vertex gives +len·h/[2]. Neither leptons nor local interference carry chirality. Open: dressing by the rest of the word, where the a-part q² ratio could enter, and the spin/helicity sector.


## PRE-REGISTRATION 5 (2026-11-15 20:04Z): dressing on the actual state, written before computing
Space (C²)^⊗3 ⊗ V ⊗ V*, 32-dimensional: quark strands 1–3 and a created pair on strands 4–5. Initial state |u d d⟩ ⊗ coev_{45} (plain). For a word w on strands 1–3 and each site k, replace letter k by its deviation δ_k = W(letter) − letter (corpus vertex, or the mirror with P_L ↔ P_R), act with the full word, then apply the emission crossing Ř on strands (3,4) as in #7973 arm A. A(w) = Σ_k of the component on |p-labels⟩_{123} ⊗ |d ūbar⟩_{45}, where p-labels means any basis state with two u and one d. Report A_corpus, A_mirror and |A_c|²/|A_m|², exact in q, for s1 s2⁻¹, (s1 s2⁻¹)³, s1⁴, (s1 s2)⁵. Expectation, stated in advance: they differ, because the dd pair lies in the left line P₊, which δ_corpus keeps and δ_mirror kills. Whatever comes out gets reported.


RESULT 5 (PR #7981, 4439872c62): the expectation held; the magnitudes differ for all words. |A_c|²/|A_m|² at q₀: s1 s2⁻¹ 2.71, V³ = (s1 s2⁻¹)³ 0.387, s1⁴ 1045, (s1 s2)⁵ 55.2. On the canonical γγ nucleon V³, the MIRROR vertex is larger: with the corpus W, the nucleon prefers right-handed emission. This is a real tension. Open: is the corpus W's P_L/P_R assignment (W = σP_R + σ⁻¹P_L) the mirror of the physical one, or is the nucleon word or the insertion rule wrong? Bean stays open.


## PRE-REGISTRATION 6 (2026-11-15 20:15Z): closed-trace amplitude, written before computing
The 'both, closed trace first' route was chosen. M_w = Σ_k (word w with letter k replaced by δ_k) on (C²)^⊗3, for the corpus vertex and for its mirror. Close the spectator strands 1 and 2 with the D Markov weights (partial quantum trace with K⊗K, K = diag(q, q⁻¹)), leaving a 2×2 operator T_w on strand 3, the converting strand. The emission amplitude (#7973 arm A) is the d→d entry T_w[d,d]. Report T_corpus[d,d], T_mirror[d,d] and the squared ratio, exact in q, for V³ = (s1 s2⁻¹)³, s1 s2⁻¹, s1⁴, (s1 s2)⁵. Also report whether T_w is a scalar (Markov). No direction is predicted. Whatever comes out gets reported. Then the corpus audit of W's P_L/P_R.
