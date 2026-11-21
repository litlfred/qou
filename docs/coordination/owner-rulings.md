# Owner rulings ledger

The single in-repo record of the owner's standing rulings and working
instructions. **Owner directive 2026-11-21: no project memory — everything
lives in the repo.** Agents read this file; they do not keep rulings in
chat-app memory, and they add each new ruling here (dated, with the verbatim
words where available) in the same session it is given.

Status of a ruling: an owner ruling is a **working conjecture**, not a
derivation. Formalize it first (state it in Lean as a conjecture / class
carrier), then try to prove and derive it.

## Physics / mathematics rulings

| date | ruling | where it is recorded in detail |
|---|---|---|
| 2026-11-18, reaffirmed 2026-11-20 | **The photon is** γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹ (fourth term the chiral vertex σ₀σ₁⁻¹; the σ₀σ₁ form is old and wrong). A ruling, not a working assumption. | `AGENTS.md` §THE PHOTON; `predicted-spectra/photon.md`; `QOU/Photon.lean` |
| 2026-11-20 | **Q_β is derived algebraically from γγ pair production**, not chosen. The T³ weight-split value (0.3254 MeV) is the scored cell, and that number is Q_β, not m_n − m_p. | `docs/audits/2026-11-20-qbeta-flavour-weight-split.md` |
| 2026-11-20 | **β-decay is a particle interaction**, not a standalone transition — ultimately a Gröbner–Shirshov basis calculation (γγ / Breit–Wheeler route). | this ledger |
| 2026-11-20 | **The up quark is an unknot strand** (a component of the Borromean braid), not a knot type of its own. | `docs/audits/2026-11-20-up-quark-electron-knot-clash.md` |
| 2026-11-21 | **The electron is σ₀σ₁σ₀ ∈ B₃, whose closure is the Hopf link** — ruling for now. Verbatim: *"I think it is hopf link so take. That as ruling for now, but keep trefoil as backup in case need to recisit"*. **Backup:** the trefoil σ₀³ ∈ B₂ (leptons in H₂). Supersedes the 2026-11-20 wording "the trefoil T(2,3) is the electron". | `docs/audits/2026-11-21-electron-word-gs-interactions.md`; `docs/audits/2026-11-21-electron-word-options-downstream.md`; `QOU/BraidKnot/ElectronWordCandidates.lean`, `QOU/BraidKnot/LongestWordNotTwoPhoton.lean` |
| 2026-11-21 | **The scoreboard and all β-decay routes use the two-term Lagrangian trace**, not only the one-term trace. | this ledger |
| 2026-11-20 | **The quark's generation label 3/5/7 is the lepton partner's crossing count**, not a crossing count of the quark strand (meson cluster, option 1); `CanonicalWeakIsospinFromBowtie` restated as κ = ε · partnerCrossings (option A). | PR #8698 (merged) |
| 2026-11-21 | **Right-handed singlet adopted:** the matter⊗Higgs right line of the Jimbo crossing, spanned by s = q·ud − du, is e_R (lepton⊗Φ̃, Q −1, Y −2), d_R (quark⊗Φ̃), u_R (quark⊗Φ), ν_R (lepton⊗Φ). Right-handed fields are two-strand composites, not new strands. Strand order and the four Yukawa strengths are not derived by the corpus (#8740); owner chose to research a type-dependent (quark vs lepton) strength — it must be derived, never chosen to fit. | PR #8694 (merged); PR #8740; `QOU/QuarkState/RightHandedSingletChannel.lean`, `YukawaStrandOrder.lean` |
| 2026-11-21 | **Photon colour weights: no new rule.** n and p keep the same nucleon element β_Bor = V³; colour weights are not assigned to flavour. | PR #8705 (merged) |
| 2026-11-21 | **Two-term trace with a lepton strand is derived, not chosen:** the owner's instruction was to derive it as the nucleon one was (Lagrangian + non-abelian Stokes). The derivation forces the full braid group with species carried; the connected part is 0 on every β route, so scored two-term = one-term. | PR #8743; supersedes §4 of PR #8707's audit |
| 2026-11-21 | **γγ grammar stays V-only** (mirror vertices σᵢ⁻¹σᵢ₊₁ not admitted). Reason: no Hecke-letter map is parity (D-H5 = D, 2026-11-15), and V̄ᵏ is conjugate to Vᵏ (`mirror_pow_conj`), so the V-only set is CPT-closed up to conjugacy. Proved for single-vertex powers only; multi-index words not yet checked. | PR #8742; `QOU/QBeta/ParityMapCandidates.lean` |
| 2026-11-21 | **Reading R1 adopted: q ↦ q⁻¹ is antilinear.** Hence ι (σ ↦ −σ⁻¹) = CP, neg (σ ↦ −σ, q ↦ q⁻¹) = T, bar (σ ↦ σ⁻¹, q ↦ q⁻¹) = CPT, a closed set; there is still no P. | PR #8742 |
| 2026-11-21 | **Route L (additive κ·log|tr|) is HELD**, not stopped: additivity holds for every κ, so it fixes neither scale nor sign. | PR #8693 (draft) |

## Working instructions for agents

| date | instruction |
|---|---|
| 2026-11-20 | **No phone / push notifications.** Leave push off when creating scheduled tasks or sessions. |
| 2026-11-20 | **Propagate every owner correction or ruling** to all sibling agents/sessions and to this ledger (and `AGENTS.md` where it is a standing rule), so none repeat the mistake. |
| 2026-11-20 | **Rulings are conjectures until derived**: formalize first (Lean conjecture), then attempt proof and derivation. |
| 2026-11-21 | **Resource-limited work goes to a bean for Antigravity.** Work that fails here because of time or resource limits (e.g. Lean modules too heavy to build in this environment) is recorded as a bean for Antigravity, not dropped. |
| 2026-11-21 | **No project memory.** Rulings and instructions live in the repo (this file), never in chat-app memory. |
