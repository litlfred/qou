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
| 2026-11-16, re-confirmed 2026-11-21 | **Virtual photons do not exist in QOU.** An exchange is reformulated either as prior entangled photons or as intermediary emitters produced in ED that cannot be seen. Recorded from the owner's 2026-11-16 instruction (paraphrase kept in the retired project memory; the verbatim chat text is not on file). Re-confirmed 2026-11-21 on a card in the project thread "Review main and revive stalled PR work". | this ledger |
| 2026-11-21 | **Agents carry the 2026-11-18/20 photon only.** The 2026-11-16 project-memory wording "L± is part of the photon; γγ words use all three photon terms" is superseded: L₊ = σ₀σ₁ and L₋ = σ₁σ₀ are not photons. Owner card choice A, project thread "Review main and revive stalled PR work". | this ledger; #8543 (wording fix) |
| 2026-11-20 | **Q_β is derived algebraically from γγ pair production**, not chosen. The T³ weight-split value (0.3254 MeV) is the scored cell, and that number is Q_β, not m_n − m_p. | `docs/audits/2026-11-20-qbeta-flavour-weight-split.md` |
| 2026-11-20 | **β-decay is a particle interaction**, not a standalone transition — ultimately a Gröbner–Shirshov basis calculation (γγ / Breit–Wheeler route). | this ledger |
| 2026-11-20 | **The up quark is an unknot strand** (a component of the Borromean braid), not a knot type of its own. | `docs/audits/2026-11-20-up-quark-electron-knot-clash.md` |
| 2026-11-21 | **The electron is σ₀σ₁σ₀ ∈ B₃, whose closure is the Hopf link** — ruling for now. Verbatim: *"I think it is hopf link so take. That as ruling for now, but keep trefoil as backup in case need to recisit"*. **Backup:** the trefoil σ₀³ ∈ B₂ (leptons in H₂). Supersedes the 2026-11-20 wording "the trefoil T(2,3) is the electron". | `docs/audits/2026-11-21-electron-word-gs-interactions.md`; `docs/audits/2026-11-21-electron-word-options-downstream.md`; `QOU/BraidKnot/ElectronWordCandidates.lean`, `QOU/BraidKnot/LongestWordNotTwoPhoton.lean` |
| 2026-11-21 | **The scoreboard and all β-decay routes use the two-term Lagrangian trace**, not only the one-term trace. | this ledger |
| 2026-11-21 | **Nuclear Regime-I shell-size rule T(2,n_s) withdrawn.** Its basis was a mislabel: (σ₀σ₁)²σ₀ closes to T(2,4), not the cinquefoil T(2,5). Kept withdrawn until derived. | `nuclear-interactions/nuclear-operator-regimes.ts` (caveat); `docs/audits/2026-11-21-electron-word-gs-interactions.md` §7 |
| 2026-11-21 | **Spin-involution LP-dual statement corrected (card: "Correct the conclusion").** It concludes y₀*(σ(β)*) = y₀*(β), assuming σ commutes with * and n_target(σ(β)*) = n_target(β); not y₀*(σ(β)) = y₀*(β). | `mass-theory/spin-involution-lp-dual-invariance.md`; PR #8765 |
| 2026-11-21 | **Physics claims are scoped to what is proved (cards on issue #8810).** (1) Narrow over-claiming prose: CCC proposition states CCC-1/CCC-3 only with CCC-2 conjectural; "TQFT" names the algebraic model, no 3d TQFT is constructed; the categorical Einstein equation is postulated (a class field), not derived; no "vanishing masses" at q → 1. (2) **The perturbative-QFT epic `qou-3fjn` is re-scoped to math only**: pure-mathematics targets (Herm₂(ℂ) ≅ ℝ^{1,3}, Cl(1,3) traces, su(3) structure constants, sin²θ_W = 3/8 as a trace ratio, g_A⁽⁰⁾ = 5/3, 4T/chord jet); no empirical pins in formal targets and no constructions needing virtual quanta; `qou-n1ks` scrapped as subsumed. | `docs/audits/2026-11-21-physics-claim-scope-recheck.md` |

## Working instructions for agents

| date | instruction |
|---|---|
| 2026-11-20 | **No phone / push notifications.** Leave push off when creating scheduled tasks or sessions. |
| 2026-11-20 | **Propagate every owner correction or ruling** to all sibling agents/sessions and to this ledger (and `AGENTS.md` where it is a standing rule), so none repeat the mistake. |
| 2026-11-20 | **Rulings are conjectures until derived**: formalize first (Lean conjecture), then attempt proof and derivation. |
| 2026-11-21 | **Resource-limited work goes to a bean for Antigravity.** Work that fails here because of time or resource limits (e.g. Lean modules too heavy to build in this environment) is recorded as a bean for Antigravity, not dropped. |
| 2026-11-21 | **No project memory.** Rulings and instructions live in the repo (this file), never in chat-app memory. |
