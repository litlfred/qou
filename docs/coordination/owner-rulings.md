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
| 2026-11-21 | **Nuclear Regime-I shell-size rule T(2,n_s) withdrawn.** Its basis was a mislabel: (σ₀σ₁)²σ₀ closes to T(2,4), not the cinquefoil T(2,5). Kept withdrawn until derived. | `nuclear-interactions/nuclear-operator-regimes.ts` (caveat); `docs/audits/2026-11-21-electron-word-gs-interactions.md` §7 |
| 2026-11-21 | **Spin-involution LP-dual statement corrected (card: "Correct the conclusion").** It concludes y₀*(σ(β)*) = y₀*(β), assuming σ commutes with * and n_target(σ(β)*) = n_target(β); not y₀*(σ(β)) = y₀*(β). | `mass-theory/spin-involution-lp-dual-invariance.md`; PR #8765 |

## Working instructions for agents

| date | instruction |
|---|---|
| 2026-11-20 | **No phone / push notifications.** Leave push off when creating scheduled tasks or sessions. |
| 2026-11-20 | **Propagate every owner correction or ruling** to all sibling agents/sessions and to this ledger (and `AGENTS.md` where it is a standing rule), so none repeat the mistake. |
| 2026-11-20 | **Rulings are conjectures until derived**: formalize first (Lean conjecture), then attempt proof and derivation. |
| 2026-11-21 | **Resource-limited work goes to a bean for Antigravity.** Work that fails here because of time or resource limits (e.g. Lean modules too heavy to build in this environment) is recorded as a bean for Antigravity, not dropped. |
| 2026-11-21 | **No project memory.** Rulings and instructions live in the repo (this file), never in chat-app memory. |
| 2026-11-21 | **Measured MeV comparisons stay out of Lean.** The two `norm_num` theorems in `TjonSimplexForm.lean` that compared measured MeV values (`mu4_target_exceeds_n3lo_bound`, `mu4_target_exceeds_35_percent_of_B4He`) are removed; the arithmetic stays in `mu4_vs_nuclear_4n_force_bound_probe.py` and its witness (decision card, option "Move them out of Lean", PR #8852). The `ExternalNumerics` section (`ame_ratio_below_universal`, `operator_ladder_below_pairwise`) was removed under the same standing rule; `tjon_external_cross_check_probe.py` keeps it. |
