---
# qou-q1a4
title: Trace where u and d first become distinguished in the γγ chain (photons → condensate → nucleons)
status: todo
type: task
priority: high
tags:
    - needs-owner
    - convention-d
created_at: 2026-11-15T18:54:18Z
updated_at: 2026-11-21T16:41:14Z
parent: qou-avtq
---

Owner, 2026-11-15: "dont we see u and d come into play as part of chain from photons -> quarks/gluon condensate -> protons/neutrons?" / "can we track/derive that?"

Context (n–p thread, PR #7966, bean qou-jwl8): every consistent model gives n − p = 0 until a u/d asymmetry is put in by hand: the γγ word (p and n are the same word V³), and pure two-colour Yokonuma–Hecke (colour flip t ↦ −t preserves the trace at the forced x = 0). The −18.5 % comes from mismatched words in the traced product plus the imported rule dd → σ⁻¹.

Goal: walk the chain step by step and record, for each step, whether u and d are distinguished, and by what (derived, census, or imported):
1. γγ vertex σ_g σ_{g+1}⁻¹ and the 6-letter core (qou-ales): no flavour label.
2. The 11-letter Q_β nucleon words: p and n differ only in the 3-letter tail; tail letters are census-derived (qou-99qc). Currently this is the FIRST place u/d differ, and it is not derived.
3. Level-2 Schur–Weyl (convention D = gl₂, Jimbo action, JimboActionKernel.lean): V = C² carries a two-valued label (isospin or spin, not decided). The quantum trace weights the two basis vectors by K = diag(q^{±1}), which breaks u ↔ d by construction. Candidate derived source, to be probed pre-registered.
4. Weak vertex / chirality (weak-vertex thread, PR #7960): tr_D is not ι-invariant (pullback is z_T); d = ι(u) is not forced by colouring.

Status: open. No fitted asymmetry may be used; any labelling choice (which basis vector is u) must be reported both ways.


## 2026-11-15 19:00Z step 3 result
Level-2 (gl₂ Jimbo) D trace restricted to weight spaces: n/p = q^∓2 exactly, the same for the half twist, the full twist and γγ V³. |ΔΦ| = 2 ln q (Δm = 0.7814 MeV, −39.58 % vs CODATA, comparison only). Mechanism: K^{⊗3} is the scalar q^{±1} on the p and n weight spaces, and the plain traces agree. Derived: the magnitude. Not derived: the sign, i.e. which basis vector is u. Sector-normalised: n/p = 1. Probe np_level2_weight_space_probe.py (PR #7966, audit §13).
Next: find independent corpus input that fixes the orientation (e.g. the charge/weight of the γγ core).


## 2026-11-15 step 4 (orientation), partial
A grep of folio/ content and Lean for an isospin orientation convention (e₁ = u, highest-weight = up, etc.) found none. That is the surface searched, not a full six-path check. Note that the published splitting formula Δm = α·|ΔΦ| uses an absolute value, so the 2 ln q magnitude does not depend on the orientation. The orientation only matters for the claim 'n heavier than p', which needs a monotone mass ↔ trace relation the corpus does not state in this formula.


- Lead checked (from the weak-vertex thread): g-action-on-substrate-table1-data.md assigns gauge components A^(W±) = (1,0)|_{T±} and A^(Z) = (1,0)|_{(T³,Y)}. It names the generators but does not identify the gl₂ Schur–Weyl V = C² with the quark isospin doublet, and does not say which basis vector has T³ = +½. So it does not fix the orientation as it stands.


**Correction (2026-11-15, commit e606f824a8).** An earlier note here said both K = diag(q^{±1}) give a Markov trace with z = z_D. That is wrong. It came from a weaker test (full traces of 1 and Ř). The partial quantum trace tr₂((1⊗K)Ř) is z_D·1 only for K = diag(q, 1/q); for diag(1/q, q) it is diag(q/(q²+1), (q⁴+q²−1)/(q³+q)), not a scalar. Raised by the weak-vertex thread and re-checked with sympy. So D forces K = q on e₁ (T³ = +½). Step 4 is still open: which quark sits on e₁ (positive crossing ↔ K = q would give u = +½). Same claim also appeared in audit §13 (fixed) and PR #7966 comment 6899536326 (superseded by a new comment).


**2026-11-15 §14 (commit above):** (1) α = m_e·8G is asserted for the n–p log-trace in one sentence of the proof, not derived; the −39.58 % is conditional on it. (2) Level 3 (gl₃, K = q^{2ρ}) gives the same q^{∓2} for adjacent u,d, at any level (permutation-module argument). Non-adjacent placement gives q^{∓4}, but that is a choice. (3) K = diag(q,1/q) is Markov for both Ř and Ř⁻¹, so crossing sign does not select u's vector. Step 4 reduces to identifying the writhe T₃ (u = T(2,3)) with the Cartan weight in K = q^{2T³}. Open.


**2026-11-15 19:13Z, from the weak-vertex thread (not adopted).** A candidate link: on the D-forced Ř, a crossing (σ or σ⁻¹) is a pure swap iff the over-strand carries e₁. Checked by hand: Ř(e₁⊗e₂) = e₂⊗e₁, Ř(e₂⊗e₁) = e₁⊗e₂ + h e₂⊗e₁, Ř⁻¹ = Ř − h. With def:down-quark (u passes over d, flavour kept), this gives u = e₁ = T³ = +½. It depends on the over-strand convention for σᵢ, and the owner has a card on that. Not adopted yet.


**2026-11-15 §15 (3e0aa5fce5).** Scale: each corpus mass formula, applied to the weight ratio, gives 89–219 MeV (canonical facade, linearised facade, unified formula). Only the asserted α route gives a MeV-scale value (−39.58 %). No corpus formula derives a MeV-scale multiplier; the scale is the open object. Lean MarkovOrientationForced.lean (sorry-free, generic Field): the Markov condition is a = b q² for both Ř and Ř⁻¹; the K-weights of adjacent basis vectors differ by q². The permutation-module half is not formalised.


**2026-11-15 §16.** Step 4: PR #7971 (draft, weak-vertex thread) proves that under D a crossing is a pure swap iff the over strand carries K = q. With corpus conventions (lower strand over in σᵢ; u over d) this gives u = e₁ = T³ = +½. Then n/p = q⁻², which makes the neutron heavier (correct sign). The sign is derived, conditional on #7971 landing. The magnitude is still open (the scale, §15). Keep open.


**2026-11-15 §17.** Lean NucleonWeightSpaceTraces.lean (sorry-free): an explicit intertwiner shows every braid word has equal plain trace on the p and n weight spaces, so level-2 n/p = q^{∓2} is word-independent and proved. Scale: Φ = Σ log V̂ᵢ, and α = m_e·∏V̂ᵢ(B₃) is built from the same object. The asserted α·ΔΦ multiplies a volume by a log-volume, whereas the corpus scale block is linear in the volume. Still open.


**2026-11-15 §18 (e7e9b93deb2).** Derivation attempt with the corpus's derived scale E₀ = m_e/(q(q−1)), tower-summed, used linearly on the D trace restricted to the γγ nucleon V³: 0.3254 MeV (−74.8 %), and V⁶ agrees to 0.6 %. The log form with E₀ gives −31.8 %, but the log form has no corpus support. The derivation does not close. Proposed wording for the n–p block (Option A: named hypothesis H_α; Option B: demote to conjecture) is at qou-np-splitting/proposed-np-block-wording.md, not applied.


2026-11-15 (§19 + H_α applied): Route 1 done. Φ = Σ log|V̂ᵢ| is a log of algebraic quantum-volume factors, not a hyperbolic volume; the γγ nucleon V³ closes to the Borromean rings for p and n alike, so ΔVol = 0 (scope-(a) negative for the 'Φ is a volume' route). Option A applied (6baace0e793): statement now assumes (H_α). Route 4 done (dc79a1c9153): Lean class ScaleHypothesis + splitting_of_scaleHypothesis, sorry-free, tautological rfl def removed. Route 2 (n–p = Q_β + m_e from the derived Q_β route) next. STAYS OPEN: H_α is an open conjecture.


2026-11-15 §20 (6ae1b559261): route 2 done. n-p = Q_beta + m_e on ruled z_D base: 0.9557 MeV (-26.1 %); tower-summed E0 -25.8 %; nuc11 cell -10.1 % but element fails SDP. Production 1.2938 is fit-tier (Form A, z_C, N chosen by target). Route 2 does not validate H_alpha (linear vs log functional). Next: FE/EF weak term in sibling thread.


2026-11-15 CORRECTION (§21): §18's 't_p is negative' was wrong. t_p = +0.40872, t_n = +0.33174 at q0. Under the linear form the neutron is LIGHTER (wrong sign), a scope-(a) negative. Bridge B (derivation-chain thread): a linear map normalised by the electron gives m_p/m_e ~ 1; a weight-space route needs ~55x derived suppression plus a sign flip. FE/EF must pre-register its order in h.


2026-11-15 §22: FE/EF (sibling thread, folded into #7966). FE alone or EF alone gives a larger |ln r|, but the two have opposite signs and the choice between them is an ordering choice. The omega-symmetric insertion gives exactly q^-2. The extra factor A -> 2 at q=1 is the isospin 3/2-vs-1/2 weight. No derived u/d term beyond q^-2 on the U_q side. H_alpha still open.


2026-11-15: PR #7966 merged (rebase, b2b349f3607) on owner's tap. Landed: audit §1–§22, H_alpha wording in the block, ScaleHypothesis class, Lean NucleonWeightSpaceSecondOrder. Bean STAYS OPEN: H_alpha (the n-p MeV scale) is an open conjecture; the bridge-B thread is working on the 1/hbar_q^2 hierarchy.

2026-11-21: PR #8886 merged (3a865b37). The n–p block now shows both model values side by side: 1.0541 MeV (−18.5 %, conditional on H_α) and Q_β + m_e = 0.8364 MeV (−35.3 %, ruled Q_β). Neither is selected by residual; sign of the ordering open. H_α derivation still open; bean stays open.
