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
updated_at: 2026-11-15T19:13:24Z
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
